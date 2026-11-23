# JIT-098: Prepare reconstructed Final Exam self-assessment

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Prepare reconstructed Final Exam self-assessment**. Its objective is: Assess independent reasoning with unseen questions while distinguishing self-study from official CMU exams.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/learninggoals.md

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-098`.

## When to run

After LAB-13-CLOSE; execute this row before the next activity.

Required completed queue rows: LAB-13-CLOSE. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

Completed notes and reviewed work in scope: All mapped Fall learning goals, six assignments and labs, including HW6 operations reasoning. Public learning goals and any officially published practice questions available at this trigger. No private Canvas exam is presumed recovered.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Create a reconstructed assessment blueprint for All mapped Fall learning goals, six assignments and labs, including HW6 operations reasoning, using explanation, code reading, counterexample and tradeoff questions. Preserve 180 minutes as a suggested sitting length, not a calendar deadline.
2. Save blank learner paper and rules separately from assessor-only questions/answers/rubric. Prefer an independent assessor to hold unseen questions; otherwise disclose the limitation. Include one check per major learning objective without giving model answers in the learner prompt.
3. Freeze scope and scoring criteria before the learner sees the questions. For Midterm 1 exclude L08 as new content; for Midterm 2 focus L08–L16 and Jenkins, not L17 as new content. Final covers the full mapped course.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`assessments/final/instructions.md`, frozen blueprint and assessor-only paper/key under withheld/

Write the evidence record to `reviews/JIT-098.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-098` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **A labeled reconstructed assessment has frozen scope/criteria and no learner-visible answer key.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
