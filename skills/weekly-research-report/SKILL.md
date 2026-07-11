---
name: weekly-research-report
description: Generate concise HTML weekly research/work reports for computer-science graduate students, especially thesis, paper-submission, experiment, and advisor-facing progress reports. Use when the user asks to create, revise, template, or systematize a graduate weekly report, paper/thesis progress report, advisor report, or HTML report with timelines, milestones, Mermaid/ECharts/D3 visualizations, next-week priorities, or reusable reporting workflow.
---

# Weekly Research Report

Create a human-readable HTML weekly report for computer-science graduate research work. Prioritize facts, current state, next steps, risks, and verifiable outputs. Do not inflate reading, discussion, or plans into completed work.

## Workflow

1. **Collect inputs first.** If the user has not already provided enough information, ask the questions in `references/question-template.md`. Do not generate the HTML from vague inputs.
2. **Confirm understanding.** Before writing the report, summarize the intended report in 5-8 lines: completed work, paper status, thesis plan, next-week priorities, and content that must not be overstated.
3. **Generate the report.** Use `references/html-template.md` for section order, visualization choices, file naming, and writing rules.
4. **Validate.** After creating or editing HTML, run a parser check and inline JavaScript syntax check when possible. Search for old dates, old file names, and leftover placeholder text.
5. **Iterate from feedback.** If the user says the report is confusing, ugly, too official, or inaccurate, use `references/quality-and-defects.md` to identify the failure mode before rewriting.

## Report Modes

- **Advisor reading mode**: default. Keep it concise, factual, and easy to scan. Put work overview, node progress, and next-week priorities near the top.
- **Self-review mode**: use only if requested. Add sharper checks such as whether the week was idle, what must be delivered next week, and what failure would mean.

## Content Rules

- Separate `done`, `in progress`, `planned`, and `risk`.
- Keep the language simple. Avoid vague words such as “口径、闭环、沉淀、赋能、抓手、收束” unless the user explicitly wants that style.
- For paper work, record the exact paper state: not submitted, revising, submitted, under review, revision, accepted.
- For thesis work, connect weekly work to the thesis title, opening report, midterm report, and remaining modules when such materials are available.
- Use visualizations only when they clarify schedule, module relationships, results, or workload. Do not add visualizations just to satisfy aesthetics.

## Resources

- Read `references/question-template.md` when the user needs the first-round question set.
- Read `references/html-template.md` before generating or restructuring the HTML report.
- Read `references/quality-and-defects.md` when evaluating the skill, handling user complaints, or improving the skill itself.
- Read `assets/html-template-notes.md` for the template asset boundary and planned extensions.
