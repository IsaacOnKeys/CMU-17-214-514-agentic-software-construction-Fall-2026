# JIT-096: Verify Lab 13 starter health

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Verify Lab 13 starter health**. Its objective is: Use telemetry to localize a fault and trace one request across a boundary (reconstructed pending release).

Authoritative course source: https://cmu-17-214.github.io/f2026/index.html#schedule

Supporting resource: https://cmu-17-214.github.io/f2026/index.html#schedule

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-096`.

## When to run

After JIT-095; execute this row before the next activity.

Required completed queue rows: JIT-095. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

Current unit metadata in `labs/lab13/LOCATION.md`; source handout https://cmu-17-214.github.io/f2026/index.html#schedule; public starter https://cmu-17-214.github.io/f2026/index.html#schedule; Fall schedule, future official labs/lab13.md if published, HW6 frozen operations contract and learner telemetry, curriculum/reconstructed-study-guides.md. Tools needed now: Determined at JIT release; prefer the existing HW6 stack, logs and metrics; no extra cloud account. Expected baseline: A published official starter is healthy as documented, or the labeled reconstructed starter emits a traceable healthy request. Freeze the baseline before learner work.. The snapshot contains no Lab 13 handout/repository link. Refresh first. If still unavailable, write a reconstructed three-milestone lab without claiming original objectives beyond the published title; do not supply its solution. Read `labs/lab13/preparation.md` and the working-tree diff.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. From the recorded Lab 13 working copy, run only this preflight: Use the minimal start/health/log/metric command specified in the newly frozen Lab 13 handout; do not run the fault scenario during preflight.. Capture complete command/result and test-discovery counts; distinguish compile/dependency failures from intended behavior.
2. Compare against this documented baseline: A published official starter is healthy as documented, or the labeled reconstructed starter emits a traceable healthy request. Freeze the baseline before learner work.
3. Check the working diff and scope boundaries: The snapshot contains no Lab 13 handout/repository link. Refresh first. If still unavailable, write a reconstructed three-milestone lab without claiming original objectives beyond the published title; do not supply its solution.
4. If the baseline differs, record the exact runtime/source revision and investigate environment or source drift. Do not repair intended exercise failures or claim readiness from static inspection.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`labs/lab13/preflight.md` with commands, exit codes, expected/observed counts, source SHA and readiness verdict

Write the evidence record to `reviews/JIT-096.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-096` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **A published official starter is healthy as documented, or the labeled reconstructed starter emits a traceable healthy request. Freeze the baseline before learner work.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
