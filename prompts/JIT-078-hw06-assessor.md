# JIT-078: Prepare independent Assignment 06 assessment controls

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Prepare independent Assignment 06 assessment controls**. Its objective is: Keep acceptance checks independent of the submitted implementation and evaluate the learner’s verification work.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw6.md

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-078`.

## When to run

After JIT-077; execute this row before the next activity.

Required completed queue rows: JIT-077. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

Frozen `assignments/hw06/release-manifest.json`, requirements.md and acceptance.md; `assessments/rubrics/hw06.md`; current public brief. Assessor session only, separate from learner work.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Create only current-unit assessor fixtures/checks under `assessments/withheld/hw06/`. Derive each check from a frozen requirement or published behavior-preservation obligation, not from the eventual solution. Record the mapping and hashes before inspecting learner implementation.
2. Each operating commit passed full tests/static/audit/gitleaks8.30.1 gates and deployed-health exact-commit wait; blocking secret/critical-vulnerability probes; private images/history clean or rotated leak evidence. Operate ≥3.5h with frozen traffic, acknowledge ≥1 real degradation, cross-check incident timeline/localization/impact/DM trace against withheld service record; capture before teardown.
3. Where the learner harness/characterization tests are assessed, create minimal correct and incorrect controls that distinguish checking behavior from pinning implementation. Validate control verdicts independently; a control is not a learner reference solution. Keep controls and expected failures out of prompts, notes and learner-visible logs.
4. Expose only an assessment interface/run command and output format in current acceptance.md; do not expose private expected values or mutation details. If the same learner controls both roles, record that filesystem separation prevents accidental spoilers but cannot provide genuine hidden-grader independence.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

Private `assessments/withheld/hw06/` evaluator and control-validation log; public invocation/criteria in `assignments/hw06/acceptance.md`

Write the evidence record to `reviews/JIT-078.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-078` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **Every independent check maps to frozen obligations, assessor controls have demonstrated expected verdicts, and no student solution was used to define acceptance.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
