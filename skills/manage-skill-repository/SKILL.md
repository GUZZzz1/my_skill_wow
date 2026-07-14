---
name: manage-skill-repository
description: Add new Codex Skills to GUZZzz1/my_skill_wow or modify existing Skills, including package structure, metadata, references, scripts, assets, examples, validation, quality evaluation, README catalog and installation instructions, Git commit, push, and remote verification. Use when the user asks to add, create, revise, improve, or update a Skill in this repository.
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
- Inspect every affected component listed in `references/repository-contract.md`; do not treat `SKILL.md` as the whole package.

## Maintenance Workflow

1. Classify the operation as `add` or `update`. If the request is deletion, deprecation, repository migration, or rollback, explain that it is outside this Skill's scope and do not proceed under this workflow.
2. Inspect the local repository root, `git status`, branch, remotes, upstream divergence, root `README.md`, repository policy files, and every affected Skill component. Preserve unrelated changes.
3. Fetch or compare remote state before publishing when network access is available. Do not overwrite remote work or use destructive Git commands to resolve divergence.
4. For a new or substantially redesigned Skill, use the system `skill-creator` workflow. Keep `SKILL.md` concise and route detail to the correct package component.
5. Apply the component matrix in `references/repository-contract.md`: metadata, interface, references, scripts, assets, examples, dependencies, privacy, documentation, and install paths.
6. Validate the affected Skill with the system `skill-creator/scripts/quick_validate.py`. Run representative scripts and parse/render assets where applicable. Check all direct references.
7. Use the repository sibling `skills/evaluate-skill-quality` when present; otherwise use the installed `evaluate-skill-quality`. Require at least `DESIGN_PASS` before entering release testing. Do not call a Skill `TEST_PASS` or `RELEASE_READY` without the evidence required by the evaluator. Resolve P0/P1 items and rerun the affected tests. If neither evaluator is available, stop before public release and report the missing gate.
8. Update the root catalog, source link, Codex installation prompt, terminal installation command, repository tree, and any lifecycle notice affected by the change.
9. Run the release checklist in `references/release-checklist.md`, including a clean temporary installation smoke test for new or changed public Skills when feasible.
10. Review the exact diff, stage only in-scope files, commit intentionally, push, and verify the remote branch points to the new commit.
11. Report changed Skills, validation, admission recommendation, installation test, commit, remote verification, and unresolved risks.

## README Installation Entry

For each Skill, add:

- One row in the root catalog linking to `./skills/<skill-name>/` and its installation section.
- One short plain-language description.
- One copyable prompt asking Codex to use `$skill-installer` for only that Skill path.
- One copyable command that invokes the installed system Skill installer with `--repo GUZZzz1/my_skill_wow --path skills/<skill-name>`.

Never replace per-Skill installation with a command that copies the entire repository into `~/.codex/skills`.

## Update Rules

- Preserve unrelated user changes and unrelated Skills.
- Treat changing `name` or folder name as outside the normal update scope because it changes installation and invocation paths. Ask the user to handle it as a separate migration.
- When an installed destination already exists, do not silently overwrite it. Inspect the local and repository versions, explain the update scope, and use a reversible replacement or patch approved by the user.
- If validation cannot run, state that clearly and do not describe the release as verified.
- If pushing requires authentication or network access, request it explicitly; never claim a push succeeded without remote confirmation.
- Never add or change a license, dependency, external service, or executable script without surfacing its effect to the user.

## Resources

- Read `references/repository-contract.md` for the complete root and Skill component matrix.
- Read `references/release-checklist.md` before any release or public update.
- Read `references/maintenance-cases.md` when evaluating this maintainer or validating add/update boundaries.
