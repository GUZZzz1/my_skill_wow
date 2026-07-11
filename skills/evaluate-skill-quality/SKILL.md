---
name: evaluate-skill-quality
description: Evaluate an existing or newly created Codex Skill with an evidence-based D1-D9 framework, admission gates, scorecard, trigger and workflow tests, and prioritized optimization tasks. Use when the user asks to review, audit, score, accept, publish, improve, compare, or determine whether a Skill is ready for personal, team, or public use, including as the final quality gate after creating or revising a Skill.
---

# Evaluate Skill Quality

Evaluate the actual Skill package, not only its prose. Produce a decision that a user can act on and an optimization plan that an Agent can execute.

## Workflow

1. Confirm the target Skill directory and intended audience: personal, team, or public.
2. Read the complete `SKILL.md`, `agents/openai.yaml` when present, and every directly referenced resource needed to evaluate the workflow. Inspect the directory structure, scripts, and assets without loading unrelated content.
3. Run the available structural validator. Run scripts or representative checks when safe and relevant. Never award validation credit for checks that were not executed.
4. Apply the hard admission gates in `references/admission-gates.md` before interpreting the numeric score.
5. Score D1-D9 using `references/scoring-rubric.md`. Cite concrete files, lines, commands, outputs, or test cases for every deduction.
6. Test or design at least three positive trigger prompts, three negative trigger prompts, two normal workflow cases, and one failure or edge case. Mark simulated cases clearly when they were not executed.
7. Issue one admission recommendation using `references/admission-gates.md`.
8. Produce the user-facing decision and Agent-facing optimization backlog using `references/output-template.md`.
9. If the user asks for optimization, patch only the admitted scope, rerun affected checks, rescore changed dimensions, and report the before/after evidence. Do not claim improvement from edits alone.

## Evaluation Rules

- State that the inherited evaluator has eight dimensions and D9, `Evaluation closure / verifiability`, is an explicit extension. Do not call D1-D9 an official nine-dimension framework.
- Separate structural validity, quality score, and real-use evidence. Passing a YAML validator does not prove the Skill works.
- Treat missing evidence as unverified, not passed.
- Do not average away a critical defect. Hard gates override total score.
- Do not inflate domain knowledge scores for generic instructions that any capable model already knows.
- Evaluate repository documentation only when it affects installation, discovery, invocation, or maintenance of the target Skill.
- Preserve the user's existing design intent unless it creates a concrete defect.

## Resources

- Read `references/scoring-rubric.md` for D1-D9 scoring and evidence requirements.
- Read `references/admission-gates.md` for hard blockers, score thresholds, and release recommendations.
- Read `references/output-template.md` before producing the final evaluation or Agent optimization backlog.
- Read `references/evaluation-cases.md` when testing this evaluator itself or when a target Skill has no existing evaluation set.
