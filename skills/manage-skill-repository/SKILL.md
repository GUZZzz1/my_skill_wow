---
name: manage-skill-repository
description: Maintain the GUZZzz1/my_skill_wow multi-skill repository by adding, updating, validating, cataloging, and publishing individual Codex skills. Use when the user asks to add a skill to this repository, revise an existing repository skill, update the README catalog or install commands, check repository structure, validate skills before release, or prepare and publish a repository maintenance change.
---

# Manage Skill Repository

Maintain `GUZZzz1/my_skill_wow` as a collection of independently installable Codex Skills.

## Repository Contract

- Put every Skill under `skills/<skill-name>/`.
- Require every Skill directory to contain `SKILL.md` with valid `name` and `description` frontmatter.
- Keep the folder name equal to the Skill `name`.
- Keep repository-level documentation in the root `README.md`; do not put a Skill `README.md` inside individual Skill folders.
- Keep each Skill independently installable. Do not require users to clone or install the full repository.
- Do not publish credentials, private reports, personal source documents, local absolute paths, or generated cache files.

## Maintenance Workflow

1. Inspect `git status`, the current branch, remote URL, root `README.md`, and the affected Skill folders.
2. For a new or substantially redesigned Skill, use the system `skill-creator` workflow. Keep `SKILL.md` concise and place detailed material in `references/`, deterministic helpers in `scripts/`, and output resources in `assets/`.
3. Validate the affected Skill with the system `skill-creator/scripts/quick_validate.py` script.
4. Check referenced files, install paths, local absolute paths, placeholders, secrets, and personal information.
5. Update the root catalog table and add or revise the Skill's individual installation command.
6. Review the exact diff. Stage only files that belong to the requested change.
7. Commit and push only after validation succeeds. Report the branch, commit, pushed remote, and validation result.

## README Installation Entry

For each Skill, add:

- One row in the root catalog linking to `./skills/<skill-name>/` and its installation section.
- One short plain-language description.
- One copyable command that invokes the installed system Skill installer with `--repo GUZZzz1/my_skill_wow --path skills/<skill-name>`.

Never replace per-Skill installation with a command that copies the entire repository into `~/.codex/skills`.

## Update Rules

- Preserve unrelated user changes and unrelated Skills.
- Treat changing `name` or folder name as a migration because it changes installation and invocation paths.
- When an installed destination already exists, do not silently overwrite it. Inspect the local and repository versions, explain the update scope, and use a reversible replacement or patch approved by the user.
- If validation cannot run, state that clearly and do not describe the release as verified.
- If pushing requires authentication or network access, request it explicitly; never claim a push succeeded without remote confirmation.
