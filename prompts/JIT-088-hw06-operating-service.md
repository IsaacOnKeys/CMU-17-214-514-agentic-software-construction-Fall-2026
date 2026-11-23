# JIT-088: Prepare the independent HW06 operating-block service and freeze its interface

Reconstructed self-study operations prompt. This is not an official CMU assessment or a worked solution.

## Role and context

Act as the preparation/evidence reviewer for this exact Fall 2026 task: **Prepare the independent HW06 operating-block service and freeze its interface**. Its objective is: Make operation independently executable without exposing a planned failure or rewriting v3 obligations.

Authoritative course source: https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw6.md

Supporting resource: Use the source and the specific local artifacts below; do not add unrelated preparation.

Workspace: `E:\CMU Agentic Software Construction` (if moved, use the directory containing AGENTS.md and the workbook). Read the root AGENTS.md and any instructions in the current working repository. Source snapshots and revisions are in `curriculum/source-manifest.json`. The ordered workbook is `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`; this row is `JIT-088`.

## When to run

After JIT-101; execute this row before the next activity.

Required completed queue rows: JIT-101. Open the workbook and inspect this row and its predecessor evidence. Follow the dependency chain recorded there. Do not rely on previous chat context or mark missing prerequisites complete.

## Inputs

HW6 frozen requirements and current learner stack; original course operations/ service if lawfully accessible; otherwise the current-unit reconstructed service specification; separate assessor repository/account and private NOTIFY_URL configuration.

Persistent references: `curriculum/concept-map.md`, `curriculum/source-and-gap-register.md`, `curriculum/assignment-continuity.md`, `curriculum/lab-audit.md`, `assessments/rubrics/assessment-policy.md`, `progress/decisions.md`, `progress/change-log.md`. Supply any requested learner repository path and immutable artifact/commit explicitly; if absent, inspect the named unit's `LOCATION.md` before asking. For cloud tasks only, the learner supplies profile/region names through configuration, never a secret in chat.

## Task

1. Assessor only: prepare a separate reachable service matching the frozen notify/ack interface, a retained timestamped service-side record and at least one latency/error/silent-delivery degradation during a ≥3.5-hour block. Save the schedule and reference record only under withheld/. A physically separate host/process with retained records is preferred; disclose learner-controlled assessor limitations.
2. Validate healthy interface and a private fault-mode control before the learner block; keep timing unknown to the learner, while exposing the allowed observation endpoints and acknowledgment protocol. Use no live credential in a test fixture or chat.
3. Freeze the synthetic traffic generator before the block. Obtain the learner’s chosen start trigger and duration without imposing semester dates. Prepare current-unit service run and capture instructions; link all service-side billable resources to the operating teardown row.

## Constraints

Preserve official source snapshots. Label every substitution adapted or reconstructed with its source and revision. Prepare only this task; do not solve the learner's exercise, reveal deliberate defects, expose withheld checks, or release later assignment changes. Keep accepted ADRs immutable except a superseded pointer. Preserve earlier API obligations. Do not print secrets or credential files. Assignment repositories and raw transcripts remain private; lab transcripts stay local and uncommitted. Do not contact staff, publish, create public forks/PRs, or change cloud resources without the learner's authorization for that action. Obtain explicit approval for destructive cloud/repository actions. A previously authorized exact action need not be reconfirmed. Use tests, observed runs, code inspection and justified critique; an AI verdict alone is insufficient.

Before any AWS mutation, verify the selected profile and region with explicit CLI flags and `aws sts get-caller-identity`; record a redacted account identifier, role and region, never credentials. Do not silently use the default profile. Inspect the exact template/plan and estimate current regional instance, EBS, public IPv4, storage, registry, telemetry, network and data-transfer exposure with AWS pricing sources. Set a learner-approved spend limit, duration and budget alerts; alerts and a stop timer are not hard billing caps. Tag and inventory every created resource in `progress/cloud-resources.md`, link this task to its named teardown row, and choose a minimal design without an unnecessary NAT gateway. A personal account has neither Academy's $50 enforcement nor automatic session cleanup. Preserve evidence before deletion. Before destructive teardown present exact account/region/resource IDs and obtain approval; delete only the approved inventory and verify resources, retained disks, addresses, logs and storage that can still incur costs.

## Outputs and progress

Private assessor service/runbook/fault record; public frozen operations interface and traffic hash; cost/teardown ledger if billable

Write the evidence record to `reviews/JIT-088.md`: source and starter revisions, input paths/commits, commands and exit codes, expected versus observed result, changed files, findings/deviations and decision. Link persistent deliverables from it; redact secrets. Add a dated entry to `progress/change-log.md` and any material adaptation to `progress/decisions.md`. Update only row `JIT-088` in the workbook with the status and evidence link. If Excel has the file locked, save a row-ID-based pending update under `progress/pending-updates/` and reconcile it before advancing; do not overwrite a newer workbook.

## Verification and failure handling

Done when: **A healthy and privately fault-tested assessor service is reachable, records independent evidence, keeps fault timing withheld and has a linked teardown; the learner can run the block from saved instructions.**

Check artifacts and observed behavior against that statement; report exactly what ran and what remains unverified. If a required input, permission, source, runtime or service is missing, mark this row `Blocked`, record the exact blocker and append a separately ordered recovery JIT row immediately after it, before the dependent activity. Assign a new stable JIT ID and save a tailored recovery prompt and index entry containing the failed command, required input and concrete retry check. Keep existing IDs stable. Do not skip forward or lower an already frozen acceptance bar. Resolve the blocker and complete both the recovery and original row before continuing.

Matching mandatory teardown queue row: **JIT-091**. Record this exact ID in the resource ledger before provisioning.
