# JIT-061: Verify Assignment 05 inputs and starter

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Verify Assignment 05 inputs and starter**. Its objective is: Separate runnability from the functionality the learner is meant to implement.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw5.md

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-061`.

## When to run

After JIT-060; execute this row before the next activity.

Required completed queue rows: JIT-060. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

`assignments/hw05/LOCATION.md`, frozen release manifest, current scaffold, prior application commit where applicable and preparation evidence. same progressive HW2/HW3 app; v1/v2 contracts, old client, harness, CAPABILITY.md and ADRs; L16 replica concepts

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Verify manifest hashes and required files for Assignment 05. Run only the current starter’s documented build/start/health checks. For HW4, use the exact-tag quick build, core suite and specified functional slice from the brief; for HW5 validate scaffold/replica reachability without repairing correctness; for HW6 verify inputs/config locally without provisioning yet.
2. Record expected versus observed starter tests, including intended failures or missing future functionality. Verify the chosen tool’s complete private transcript export and current repository privacy without creating a new public remote.
3. Confirm previous contracts/client/ADRs are preserved for HW3/5/6 and the HW4 subsystem boundary is enforced. If requirements or scaffold are incomplete, block implementation and save a specific recovery task.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`assignments/hw05/preflight.md` with file/hash, runnability, transcript and continuity evidence

Write the evidence record to `reviews/JIT-061.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-061` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **Current inputs exist, frozen hashes match, the starter runs as documented and intentional deficiencies remain; any billable action waits for its cloud row.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
