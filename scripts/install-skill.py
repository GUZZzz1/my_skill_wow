#!/usr/bin/env python3
"""Install one Skill from this GitHub repository without cloning the full repo."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_REPO = "GUZZzz1/my_skill_wow"
DEFAULT_REF = "main"
VALID_SKILL = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class InstallError(Exception):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download one Skill into a user-level or workspace-level Skill directory."
    )
    parser.add_argument("--skill", required=True, help="Skill directory name under skills/.")
    parser.add_argument("--repo", default=DEFAULT_REPO, help="GitHub owner/repository.")
    parser.add_argument("--ref", default=DEFAULT_REF, help="Git ref to download.")
    parser.add_argument(
        "--method",
        choices=("auto", "download", "git"),
        default="auto",
        help="Try direct download, Git sparse checkout, or automatic fallback.",
    )
    parser.add_argument(
        "--scope",
        choices=("workspace", "user"),
        default="workspace",
        help="Install for the current workspace or the current user.",
    )
    parser.add_argument(
        "--agent",
        choices=("auto", "codex", "claude", "agents"),
        default="auto",
        help="Select the Agent-specific Skill directory convention.",
    )
    parser.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd(),
        help="Start path used to find the nearest Git workspace root.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        help="Explicit parent Skill directory; overrides scope and Agent detection.",
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        help="Copy from an existing repository root instead of downloading from GitHub.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the resolved destination without downloading files.",
    )
    return parser.parse_args()


def find_workspace_root(start: Path) -> Path:
    current = start.expanduser().resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return current


def detect_agent(workspace: Path, requested: str) -> str:
    if requested != "auto":
        return requested
    if (workspace / ".agents").exists():
        return "agents"
    if (workspace / ".codex").exists() or os.environ.get("CODEX_HOME"):
        return "codex"
    if (workspace / ".claude").exists():
        return "claude"
    return "agents"


def resolve_destination(args: argparse.Namespace) -> tuple[Path, str, Path]:
    workspace = find_workspace_root(args.workspace)
    agent = detect_agent(workspace, args.agent)

    if args.dest:
        skill_parent = args.dest.expanduser().resolve()
    elif args.scope == "user":
        if agent == "claude":
            skill_parent = Path.home() / ".claude" / "skills"
        else:
            skill_parent = Path.home() / ".agents" / "skills"
    elif agent == "claude":
        skill_parent = workspace / ".claude" / "skills"
    else:
        skill_parent = workspace / ".agents" / "skills"

    return skill_parent / args.skill, agent, workspace


def github_headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "my-skill-wow-installer",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def request_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers=github_headers())
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        raise InstallError(f"GitHub request failed with HTTP {exc.code}: {url}") from exc
    except urllib.error.URLError as exc:
        raise InstallError(f"GitHub request failed: {exc.reason}") from exc


def request_json(url: str):
    try:
        return json.loads(request_bytes(url).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise InstallError(f"GitHub returned invalid JSON: {url}") from exc


def contents_url(repo: str, path: str, ref: str) -> str:
    quoted_path = urllib.parse.quote(path, safe="/")
    quoted_ref = urllib.parse.quote(ref, safe="")
    return f"https://api.github.com/repos/{repo}/contents/{quoted_path}?ref={quoted_ref}"


def safe_child(parent: Path, name: str) -> Path:
    if not name or name in (".", "..") or "/" in name or "\\" in name:
        raise InstallError(f"Unsafe path returned by GitHub: {name!r}")
    child = parent / name
    if parent.resolve() not in child.resolve().parents:
        raise InstallError(f"Path escapes destination: {name!r}")
    return child


def download_tree(repo: str, ref: str, repo_path: str, destination: Path) -> None:
    entries = request_json(contents_url(repo, repo_path, ref))
    if not isinstance(entries, list):
        raise InstallError(f"Expected a directory at {repo_path}.")

    destination.mkdir(parents=True, exist_ok=False)
    for entry in entries:
        if not isinstance(entry, dict):
            raise InstallError("GitHub returned an unexpected directory entry.")
        name = entry.get("name")
        entry_type = entry.get("type")
        entry_path = entry.get("path")
        if not isinstance(name, str) or not isinstance(entry_path, str):
            raise InstallError("GitHub returned an incomplete directory entry.")
        target = safe_child(destination, name)
        if entry_type == "dir":
            download_tree(repo, ref, entry_path, target)
        elif entry_type == "file":
            download_url = entry.get("download_url")
            if not isinstance(download_url, str) or not download_url:
                raise InstallError(f"Missing download URL for {entry_path}.")
            target.write_bytes(request_bytes(download_url))
        else:
            raise InstallError(f"Unsupported GitHub entry type {entry_type!r}: {entry_path}")


def run_git(arguments: list[str]) -> None:
    environment = os.environ.copy()
    environment["GIT_TERMINAL_PROMPT"] = "0"
    try:
        result = subprocess.run(
            arguments,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120,
            env=environment,
        )
    except FileNotFoundError as exc:
        raise InstallError("Git is not installed; direct download also failed.") from exc
    except subprocess.TimeoutExpired as exc:
        raise InstallError("Git sparse checkout timed out.") from exc
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "unknown Git error"
        raise InstallError(f"Git sparse checkout failed: {detail}")


def download_with_git(repo: str, ref: str, skill: str, temp_root: Path, destination: Path) -> None:
    checkout = temp_root / "repository"
    repo_url = f"https://github.com/{repo}.git"
    run_git(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "--filter=blob:none",
            "--sparse",
            "--single-branch",
            "--branch",
            ref,
            repo_url,
            str(checkout),
        ]
    )
    run_git(["git", "-C", str(checkout), "sparse-checkout", "set", f"skills/{skill}"])
    source = checkout / "skills" / skill
    if not source.is_dir():
        raise InstallError(f"Skill not found in Git checkout: skills/{skill}")
    shutil.copytree(source, destination)


def install(args: argparse.Namespace) -> Path:
    if not VALID_SKILL.fullmatch(args.skill):
        raise InstallError("--skill must use lowercase letters, digits, and hyphens only.")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        raise InstallError("--repo must use owner/repository format.")

    target, agent, workspace = resolve_destination(args)
    print(f"Agent convention: {agent}")
    print(f"Workspace root: {workspace}")
    print(f"Destination: {target}")

    if target.exists():
        raise InstallError(f"Destination already exists; refusing to overwrite: {target}")
    if args.dry_run:
        return target

    target.parent.mkdir(parents=True, exist_ok=True)
    temp_root = Path(tempfile.mkdtemp(prefix=".skill-install-", dir=target.parent))
    staged = temp_root / args.skill
    try:
        if args.source_root:
            source = args.source_root.expanduser().resolve() / "skills" / args.skill
            if not source.is_dir():
                raise InstallError(f"Skill not found under --source-root: skills/{args.skill}")
            shutil.copytree(source, staged)
        elif args.method in ("auto", "download"):
            try:
                download_tree(args.repo, args.ref, f"skills/{args.skill}", staged)
            except InstallError as direct_error:
                if args.method == "download":
                    raise
                print(f"Direct download failed; trying Git sparse checkout: {direct_error}")
                shutil.rmtree(staged, ignore_errors=True)
                download_with_git(args.repo, args.ref, args.skill, temp_root, staged)
        else:
            download_with_git(args.repo, args.ref, args.skill, temp_root, staged)
        if not (staged / "SKILL.md").is_file():
            raise InstallError("Downloaded directory does not contain SKILL.md.")
        staged.rename(target)
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    print(f"Installed {args.skill} at {target}")
    print("Start a new Agent task or reload the Agent if the Skill is not detected immediately.")
    return target


def main() -> int:
    try:
        install(parse_args())
    except InstallError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
