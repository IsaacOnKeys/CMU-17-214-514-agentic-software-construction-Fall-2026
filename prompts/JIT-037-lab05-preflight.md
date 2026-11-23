# JIT-037: Verify Lab 05 starter health

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Verify Lab 05 starter health**. Its objective is: Identify consequential classic/agent smells and make one minimal behavior-preserving fix.

Authoritative course source: https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab05.md

Supporting resource: https://github.com/CMU-17-214/f26-lab05

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-037`.

## When to run

After JIT-036; execute this row before the next activity.

Required completed queue rows: JIT-036. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

Current unit metadata in `labs/lab05/LOCATION.md`; source handout https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab05.md; public starter https://github.com/CMU-17-214/f26-lab05; SETUP.md, package.json, package-lock.json, src/, tests/, SMELLS.md. Tools needed now: Node 20+; npm; TypeScript and Vitest from lockfile. Expected baseline: 39 shipped tests and the typecheck pass.. Do not edit any shipped test. Preparation must leave the smell inventory and candidate fix to the learner. Read `labs/lab05/preparation.md` and the working-tree diff.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. From the recorded Lab 05 working copy, run only this preflight: npm ci; npm test; npm run typecheck. Capture complete command/result and test-discovery counts; distinguish compile/dependency failures from intended behavior.
2. Compare against this documented baseline: 39 shipped tests and the typecheck pass.
3. Check the working diff and scope boundaries: Do not edit any shipped test. Preparation must leave the smell inventory and candidate fix to the learner.
4. If the baseline differs, record the exact runtime/source revision and investigate environment or source drift. Do not repair intended exercise failures or claim readiness from static inspection.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`labs/lab05/preflight.md` with commands, exit codes, expected/observed counts, source SHA and readiness verdict

Write the evidence record to `reviews/JIT-037.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-037` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **39 shipped tests and the typecheck pass.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
