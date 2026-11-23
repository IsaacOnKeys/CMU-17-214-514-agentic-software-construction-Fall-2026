# JIT-094: Refresh missing source: Lab 13 handout and starter

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Refresh missing source: Lab 13 handout and starter**. Its objective is: Distinguish newly published CMU material from a labeled reconstruction before this unit.

Authoritative course source: https://cmu-17-214.github.io/f2026/index.html

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-094`.

## When to run

After HW-06-CLOSE; execute this row before the next activity.

Required completed queue rows: HW-06-CLOSE. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

`curriculum/source-manifest.json`, source-and-gap-register.md, pinned Fall README and the current live Fall schedule/repository. Existing learner progress and any frozen contracts.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Recheck the official Fall schedule and repository for Lab 13 handout and starter; save any newly available public handout/PDF and its SHA/date without overwriting the pinned snapshot.
2. If official materials now exist, analyze them and update this unit’s resources, prerequisites, prompt specifics and coverage evidence. Keep current row IDs and preserve already released requirements.
3. No official Lab 13 handout/repo link in the pinned snapshot. If still absent, reconstruct a minimal three-milestone observability exercise from the published title and HW6 telemetry obligations, label its objectives inferred and freeze it before setup.
4. Record the source/fallback choice and any delta from the planning snapshot. Freeze this unit’s learner-facing handout and verification bar before its preparation or implementation.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`reviews/lab13-source-refresh.md`, updated source register and versioned handout/resource pointer

Write the evidence record to `reviews/JIT-094.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-094` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **The unit has a verified official source or explicitly labeled, source-traceable reconstruction; no unavailable material is presented as recovered CMU content.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
