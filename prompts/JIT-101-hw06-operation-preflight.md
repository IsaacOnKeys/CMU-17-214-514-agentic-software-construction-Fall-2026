# JIT-101: Verify Assignment 06 operating readiness before deployment

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Verify Assignment 06 operating readiness before deployment**. Its objective is: Require objective pipeline and telemetry evidence before beginning the billable operating block.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw6.md

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-101`.

## When to run

After HW-06-INSTRUMENT; execute this row before the next activity.

Required completed queue rows: HW-06-INSTRUMENT. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

HW-06-INSTRUMENT commit, frozen HW6 requirements/acceptance, local health/alert evidence, CI history, source/image secret-scan and rotation evidence if applicable, private deploy configuration names and the cloud ledger.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Inspect the learner pipeline at the proposed commit and actual runs. Verify tests, chosen static gate, dependency audit and gitleaks 8.30.1, a whole-history scan at least once, then correct new-commit scan coverage, and a safely synthetic non-live-secret rejection proof. Judge the critical-vulnerability gate using an isolated controlled fixture, never a live vulnerable service.
2. Verify branch rules, separate checks, job timeouts, cancellation of obsolete runs, dependency cache, documentation-only skip, main-only deployment and private image publication. Confirm the final deploy step waits for the health x_ field to equal the built commit and has a bounded timeout.
3. Inspect structured log correlation/user/message/status fields, metric behavior and a demonstrated user-visible alert. Check the degradation ADR is committed before the operating block, no keyed URL leaks into logs/images/config commits, and the request trace can be followed without code.
4. Record gaps for learner correction. Do not start or authorize the operating block until the required pre-operation checks pass; environment/service provisioning remains in the following explicit rows.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`assignments/hw06/operating-preflight.md` and immutable pipeline/alert/security evidence

Write the evidence record to `reviews/JIT-101.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-101` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **The full pipeline, safe blocking probes, local instrumentation/alert and pre-operation records have independent evidence; every required gap is resolved before deployment.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
