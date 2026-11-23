# JIT-014: Prepare and freeze Assignment 02: Better Slack

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Prepare and freeze Assignment 02: Better Slack**. Its objective is: Preserve the published Assignment 2 learning and acceptance obligations before learner implementation.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw2.md

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-014`.

## When to run

After LEC-05; execute this row before the next activity.

Required completed queue rows: LEC-05. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

Inputs: Lab 1 export evidence; lectures 1–5; private core-api-v1.md if available; fresh progressive application repository. Missing or private resources: core-api-v1.md, private repository/course templates, docs/adr-examples.md, export script, correct/broken evaluator targets and hidden tests.. Read `assignments/hw02/LOCATION.md` and assignment-continuity.md. Do not read future assignment releases.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Read the entire official hw2.md and current-unit audit; obtain legally accessible original inputs if present and record revisions. Do not request access to CMU private repositories or imply that public substitutes recover them.
2. Create blank application workspace and planning/decisions/transcripts conventions, a versioned requirements manifest and scaffold instructions. Do not implement the server, CAPABILITY.md or learner validation harness.
3. Release reconstructed core-api-v1.md only if the original is unavailable: users/channels/messages core with precise paths, schemas, errors, precedence, token/state rules, boot and extension rules; leave unseen messages/recent activity as the two learner-designed capabilities. Freeze the core and assessment bar before any implementation.
4. Write a requirement-to-source/verification matrix and `assignments/hw02/release-manifest.json` containing version, SHA256 of the handout/requirements/rubric/input artifacts, status FROZEN, and the baseline repository commit. Record every reconstructed decision and compatibility obligation. Create learner-facing contract files in the recorded work repository, never in future units.
5. Keep evaluator internals and any intentional-defect registry under assessments/withheld/ in an assessor-controlled session/repository; provide only criteria and bug-report-style findings to the learner. Do not write student specifications, designs, tests or solution code.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

This prompt does not authorize billable cloud provisioning. Keep tool installation local to the current exercise when needed; do not provision future units.

## Outputs and progress

`assignments/hw02/release-manifest.json`, `assignments/hw02/requirements.md`, current-unit `acceptance.md`, source mapping, private scaffold path and preparation evidence

Write the evidence record to `reviews/JIT-014.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-014` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **Assignment 02 has versioned, complete and frozen current requirements/acceptance with provenance, all necessary inputs or labeled substitutes, and no learner implementation has begun.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.
