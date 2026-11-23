# JIT-012: Evaluate Assignment 01 against the frozen contract

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Evaluate Assignment 01 against the frozen contract**. Its objective is: Judge functionality, verification quality, design, memory and supervision using independent evidence.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw1.md

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-012`.

## When to run

After HW-01-BUILD; execute this row before the next activity.

Required completed queue rows: HW-01-BUILD. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

Final learner commit and repository path from `assignments/hw01/LOCATION.md`; frozen release and checkpoint manifests; `assessments/rubrics/hw01.md`; private assessor run interface. Expected deliverables: Repair system; claim-mapped AUDIT.md and REPAIRS.md; test adequacy note; meaningful fast-check property with scope comment; green-before/after testability-refactor commits; plan, 5–10 real decisions, reflection and transcripts.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Verify frozen requirement and evaluator hashes before running. Use a clean workspace and redact secrets. Compare the final commit with its declared baseline; never modify the submission to make checks pass.
2. Public HTTP obligations plus complete README-driven browser demonstration, including ordinary reload/restart/reconnection conditions where relevant; independent claim-derived checks and meaningful property. Do not reveal the defect inventory.
3. Apply the published rubric dimensions and report independent evidence per item: Functionality 30; Verification 25; Process 20; Design 10; README audit 10; Defense 5. Preserve the distinction between a verified pass, fail, blocked input, and unassessed item. Original hidden-grader points receive reconstructed evidence, never a claim of official equivalence.
4. Inspect plans/transcripts/ADRs against commit history. Challenge one design assumption and one claimed testing boundary. Report reproducible behavior/requirement findings without dumping withheld tests or worked fixes.
5. Save findings and focused rechecks for the learner; do not implement corrections. Cloud activities in this unit must show executed cleanup or a visible learner-approved retention/teardown task.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`reviews/hw01-acceptance.md`, per-requirement results, rubric evidence, limits and findings at the assessed commit

Write the evidence record to `reviews/JIT-012.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-012` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **Every frozen obligation has an evidenced result or explicit unresolved finding; no claim relies solely on AI review or an unrecovered CMU grader.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
