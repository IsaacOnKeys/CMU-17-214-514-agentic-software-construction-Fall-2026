# JIT-072: Prepare Lab 11: Events, Replay, and Refunds

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Prepare Lab 11: Events, Replay, and Refunds**. Its objective is: Judge sync/event boundaries, demonstrate replay safety and recover a partial handler failure.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab11.md

Supporting resource: https://github.com/CMU-17-214/f26-lab11

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-072`.

## When to run

After LEC-19; execute this row before the next activity.

Required completed queue rows: LEC-19. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

Current unit metadata in `labs/lab11/LOCATION.md`; source handout https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab11.md; public starter https://github.com/CMU-17-214/f26-lab11; SETUP.md, TICKET.md, EVENTS.md, src/demos/replayDemo.ts, src/demos/failureDemo.ts. Tools needed now: Node 20+; npm; TypeScript/Vitest/tsx/fast-check from lockfile. Expected baseline: 33 shipped tests pass; replay/failure demos exist but are not preflight checks and are not run yet.. No real broker is needed. Do not run the replay demo before the learner writes the prediction, or repair the handler during setup.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Read the complete handout and SETUP.md for Lab 11; inspect only its build manifests, CI and named input files. Record the pinned public starter SHA from source-manifest.json.
2. Create an isolated working copy at `labs/lab11/work/` or record the learner-selected repository in LOCATION.md; use the pristine archived starter, not a previous lab solution. Track adaptation diffs separately. If a public fork/Actions evidence is required, prepare it locally first and obtain explicit authorization before publishing the fork or workflow.
3. Install only Node 20+; npm; TypeScript/Vitest/tsx/fast-check from lockfile. Follow the pinned setup/lockfiles. On Windows translate virtual-environment paths and Java classpath separators, or use the learner’s existing WSL environment; do not require WSL for all labs.
4. Check presence of SETUP.md, TICKET.md, EVENTS.md, src/demos/replayDemo.ts, src/demos/failureDemo.ts. No real broker is needed. Do not run the replay demo before the learner writes the prediction, or repair the handler during setup.
5. No cloud configuration is needed for this lab; preserve the current repository and staged discovery order.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`labs/lab11/LOCATION.md`, `labs/lab11/preparation.md`, baseline SHA, adaptation diff if any; dependencies installed only for this lab

Write the evidence record to `reviews/JIT-072.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-072` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **Lab 11 input files and current-unit tools exist, provenance is recorded, and no exercise behavior or solution was changed.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
