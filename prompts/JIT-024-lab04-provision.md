# JIT-024: Authorize and provision the Lab 04 healthy stack

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Authorize and provision the Lab 04 healthy stack**. Its objective is: Use the learner’s personal AWS account with verifiable identity, bounded costs and linked teardown.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab04.md

Supporting resource: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-instance-profile.html

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-024`.

## When to run

After JIT-023; execute this row before the next activity.

Required completed queue rows: JIT-023. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

`progress/cloud-resources.md`; the current unit LOCATION.md and reviewed infrastructure diff; learner-selected profile and region names; prior AWS pre-check evidence. Do not read credentials files.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Use the reviewed adapted Lab 4 template and healthy parameters. Record the exact stack plan and cost estimate, then deploy only after the learner authorizes the named resources. The learner performs the broken-deploy investigation; do not diagnose it for them.
2. Apply the account/region/cost/approval controls below and update the per-resource ledger. Record actual resource IDs and whether the service is merely created or functionally healthy.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

Before any AWS mutation, verify the selected profile and region with explicit CLI flags and `aws sts get-caller-identity`; record a redacted account identifier, role and region, never credentials. Do not silently use the default profile. Inspect the exact template/plan and estimate current regional instance, EBS, public IPv4, storage, registry, telemetry, network and data-transfer exposure with AWS pricing sources. Set a learner-approved spend limit, duration and budget alerts; alerts and a stop timer are not hard billing caps. Tag and inventory every created resource in `progress/cloud-resources.md`, link this task to its named teardown row, and choose a minimal design without an unnecessary NAT gateway. A personal account has neither Academy's $50 enforcement nor automatic session cleanup. Preserve evidence before deletion. Before destructive teardown present exact account/region/resource IDs and obtain approval; delete only the approved inventory and verify resources, retained disks, addresses, logs and storage that can still incur costs.

## Outputs and progress

Unit-specific cloud evidence under reviews/ and updated `progress/cloud-resources.md` including matching teardown row

Write the evidence record to `reviews/JIT-024.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-024` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **Healthy stack exists in the approved account/region, is in the resource ledger, and its matching teardown row is LAB04 cleanup in this queue. The learner still owns milestone evidence.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.

Matching mandatory teardown queue row: **JIT-025**. Record this exact ID in the resource ledger before provisioning.
