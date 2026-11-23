# JIT-019: Review Lab 03 milestones independently

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Review Lab 03 milestones independently**. Its objective is: Map implemented design, diagnose two consequential problems and defend alternative decompositions.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab03.md

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-019`.

## When to run

After LAB-03; execute this row before the next activity.

Required completed queue rows: LAB-03. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

Current unit metadata in `labs/lab03/LOCATION.md`; source handout https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab03.md; public starter https://github.com/CMU-17-214/f26-lab03; SETUP.md, DESIGN.md, CRITIQUE.md, service code. Tools needed now: JDK 21+ and Maven; no cloud deployment. Expected baseline: Shipped suite passes; CRITIQUE.md and DESIGN.md exist.. This is a writing-only lab: change no production code. Replace the Academy account pre-check with the separately queued personal-AWS readiness task. Learner deliverables: CRITIQUE.md: data/operations/structure, request trace, two problems, two decompositions and conditional preference; final commit/diff and actual run evidence.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Read the three milestones and learner evidence at the supplied commit. Review focus: Check each design claim against code and follow a reschedule request; require real costs and a condition that changes the preferred decomposition.
2. Run the smallest independent reproduction or inspect the relevant code trace; distinguish learner claims, actual results and remaining uncertainty. Respect handout rules on unchanged tests and staged patches.
3. Ask the learner, without an agent supplying answers, to explain one consequential decision and one limitation. Do not complete missing milestones for them. Record findings with severity and a concrete recheck.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`reviews/lab03-review.md` with three-milestone matrix, reproducible evidence, oral/self-recorded response and findings

Write the evidence record to `reviews/JIT-019.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-019` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **All three milestones have checked evidence and the learner can explain them; unresolved findings are recorded for the following correction row.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
