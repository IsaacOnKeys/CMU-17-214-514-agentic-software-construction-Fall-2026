# AGENTS.md — CMU 17-214/514 Fall 2026 Self-Study Reconstruction

## 1. Purpose

This project reconstructs Carnegie Mellon University's **Fall 2026 17-214/514: Agentic Software Development** as a rigorous, independently executable course. Preserve the original course's topics, pedagogical sequence, intended difficulty, lab objectives, and six-assignment progression. Supplement missing teaching; reconstruct inaccessible resources without misrepresenting them as official CMU materials.

**Primary course:** https://cmu-17-214.github.io/f2026/index.html  
**Fall source repository:** https://github.com/CMU-17-214/f2026  
**Spring 2026 reference course:** https://cmu-17-214.github.io/s2026/  
**Spring source repository:** https://github.com/CMU-17-214/s2026

The learner proceeds at their own pace. The course roadmap is **sequence-based, not date-based**. Do not require a fixed semester schedule, blanket upfront provisioning, or a semester-wide pilot test.

## 2. Governing principles

1. **Source fidelity.** Use official Fall 2026 materials as the authority for intended learning outcomes, lab tasks, and assignments. Reuse Spring 2026 materials where appropriate, followed by authoritative external sources only for demonstrable instructional gaps. Label every replacement or newly authored exercise as **reconstructed**, not official.
2. **Coverage before implementation.** Map the entire learning sequence and design the overarching assignment continuity upfront. Build individual runtime environments, starter packages, and operational infrastructure only when their checklist triggers come due.
3. **No stranded learner.** Every just-in-time (JIT) operation must be a visible, ordered Excel checklist entry with a saved, ready-to-use prompt and a verifiable completion criterion. The learner must never have to infer when or how to prepare a lab or assignment.
4. **Prompts before execution.** Pre-author and save **one tailored prompt for every JIT checklist task** when constructing the syllabus. Prompts may contain explicit placeholders for a file path or completed assignment artifact, but must not require the learner to reconstruct the operation from scratch. Generic templates alone are insufficient for the final syllabus.
5. **Assessment integrity.** Freeze each assignment's requirements and acceptance criteria before its implementation begins. Do not move the goalposts to accommodate a solution. Keep withheld checks, intentional defects, and worked solutions separate from learner-facing materials; avoid spoilers in prompts.
6. **Independent verification.** Technical review must use tests, reproducible demonstrations, code inspection, and reasoned critique. Do not treat an AI review as infallible or claim equivalence to official CMU assessment.
7. **Minimal necessary preparation.** Verify the starter and prerequisites when they become needed, not the learner's eventual completed solution. Preserve deliberate failures and bugs intended for debugging labs.
8. **Traceability.** Every checklist activity, prompt, prepared artifact, requirement, and review should link back to its source learning objective or course document.

## 3. Scope of reconstruction

### The curriculum

- Collect official Fall 2026 syllabus, learning goals, slides, lab handouts, public lab repositories, assignment briefs, and course policies, including newly published items as they become available.
- Review **each Fall lecture PDF** for explanations, examples, definitions, assumed prerequisites, and instructional gaps. Do not claim exhaustive PDF review until it has actually occurred.
- Compare the Fall topics with the Spring 2026 lectures, labs, and publicly linked instructional materials. Record precise, clickable supporting references.
- Select supplementary external sources only for gaps that the Fall and Spring materials do not adequately explain, particularly agent architecture, agent supervision, context management, engineering memory, evaluation of generated code, and repository-scale workflows.
- Preserve the Fall order as closely as reasonably possible. Insert required prerequisite study immediately ahead of the relevant task.

### The labs

- Prefer original public lab starter repositories and instructions. Maintain an audit of required tools, tests, missing files, and services.
- Adapt CMU-specific settings and resource assumptions when they block independent use (for example, AWS Academy identities/profiles). The learner can use a personal AWS account.
- Keep intentional broken behavior intact. Run only appropriate starter-health checks, not blanket tests requiring intentionally defective functionality to pass.

### The assignments

- Preserve six assignment themes:
  1. **Bad Slack:** audit, specify, test, and repair agent-generated software.
  2. **Better Slack:** build a specified Slack-like system; create a validation harness and engineering decision records.
  3. **Two Roads:** extend the system while preserving backward compatibility with the earlier contract.
  4. **Jenkins:** inspect and refactor an unfamiliar, large open-source codebase, focusing on the specified subsystem.
  5. **Scale What You Built:** add replicas, distributed guarantees, notifications, and performance evaluation.
  6. **Operate What You Built:** AWS deployment, CI/CD, observability, security gates, and incident analysis.
- Assignments **2, 3, 5, and 6 use one progressively evolving application**. Assignment 4 is separate; Assignment 1 is an intentionally flawed starting system for auditing.
- The publicly released assignment briefs define the educational target. Where student-only contracts, starter files, client simulators, hidden graders, or external services are inaccessible, create clearly designated replacements. Do not claim to have recovered CMU's hidden tests or private repositories.
- Specify the interface and acceptance obligations *before* the learner begins each assignment. Release versioned new requirements at the corresponding syllabus checkpoint; do not expose future contract changes prematurely.

## 4. Required project structure

Use this layout or preserve an existing equivalent with the same discoverability:

```text
AGENTS.md
README.md
syllabus/
  CMU-17-214-Fall-2026-Self-Study.xlsx
curriculum/
  concept-map.md
  source-and-gap-register.md
  assignment-continuity.md
prompts/
  INDEX.md
  JIT-001-<short-task>.md
  JIT-002-<short-task>.md
  ... (one file per JIT task, not merely one per task category)
labs/
  lab01/ ...
assignments/
  hw01/ ... hw06/
assessments/
  rubrics/
  withheld/  (never present this content as student-facing)
reviews/
progress/
  decisions.md
  change-log.md
```

Keep student deliverables and reconstructed instructor material clearly distinguished. If a public original repository is forked or cloned, avoid accidentally overwriting its original files without tracking the changes.

## 5. Excel syllabus: authoritative execution queue

Create an **ordered, filterable Excel table/checklist** modeled on the learner's earlier Spring 2026 course tracker. Use one sequential queue with no compulsory dates and no arbitrary weekly grouping. Freeze the header, use readable widths, add working source links, and provide a controlled status field (such as `Not started / Ready / In progress / Blocked / Complete`).

Each row must identify at least:

| Field | Requirement |
|---|---|
| `Order` | Unique sequential execution position |
| `ID` | Stable row/task identifier; do not renumber existing IDs casually |
| `Activity type` | Lecture, supplementary study, JIT preparation, lab, assignment, evaluation, cleanup, or review |
| `Topic / action` | Concrete learner-facing title; imperative for JIT actions |
| `Learning objective` | The intended competency or source requirement |
| `Core resources` | Clickable links to the official lecture/handout/repo |
| `Supplementary resources` | Clickable Spring/external references when relevant |
| `Dependencies` | Prior row IDs, prior outputs, or prerequisite skills |
| `Trigger` | When to do the task (e.g., "Immediately before Lab 08") |
| `Saved prompt` | Direct clickable hyperlink to a **specific** `prompts/JIT-...md` file on JIT rows |
| `Expected output` | Concrete artifacts or observed behavior |
| `Done when` | Unambiguous completion/verification criterion |
| `Status / Complete` | Filterable completion tracking / checklist |
| `Evidence / output link` | Link to resulting file, commit, test log, or review |
| `Notes` | Blockers, deviations, and observations |

**Critical ordering rule:** Put preparation in its own row **before** the corresponding lab/assignment, followed by the learning activity, independent verification, review, and any cleanup when relevant. Do not bury JIT tasks only in notes attached to a lab row. Distinguish provisioning from learning and from review.

Representative sequence (illustrative IDs only):

```text
... lecture: testing and testability
... supplementary study (only if needed)
JIT-014 prepare Lab 02 environment     -> prompts/JIT-014-prepare-lab02.md
... perform Lab 02
JIT-015 review Lab 02 deliverables     -> prompts/JIT-015-review-lab02.md
... incorporate review and mark complete
...
JIT-026 prepare Assignment 02 contract -> prompts/JIT-026-prepare-hw02.md
... release/check requirements; perform Assignment 02
JIT-027 evaluate Assignment 02          -> prompts/JIT-027-review-hw02.md
...
```

The **workbook is the source of truth for what happens next**. If work is blocked, record the blocker and a recovery task explicitly rather than silently skipping it.

## 6. Pre-written prompt library

During initial syllabus construction, enumerate **all** intended JIT operations and write their individual prompts in `prompts/`. Maintain `prompts/INDEX.md` with the prompt ID, related syllabus row ID, invocation trigger, file path, purpose, and required output. Every JIT row must link to its actual saved prompt. Verify that the file exists and the hyperlink works before calling the syllabus finished.

Each prompt must state:

- **Role and context:** the exact Fall 2026 unit/lab/assignment, relevant source links, and already completed prerequisites.
- **When to run:** the precise trigger in the Excel syllabus.
- **Inputs:** files, current repository state, service credentials/permissions to check without exposing secrets, and the prior unit's deliverables.
- **Task:** specific steps to prepare, provision, adapt, inspect, test, review, or deprovision only what is needed now.
- **Constraints:** preserve intended defects, avoid spoilers, retain earlier API contracts and architectural decisions, avoid unnecessary costs and destructive actions, keep grader material separate.
- **Outputs:** exact paths/files, commands/results to report, and updates to the syllabus/progress record.
- **Verification:** observable `Done when` criteria and how to handle failure/blocking.

Write **unit-specific** prompts for such tasks as: prerequisite check; starter repository setup; dependency installation; AWS provisioning/teardown; replacement contract release; simulator/test-harness setup; characterization-test or review session; architecture critique; assignment acceptance review; post-unit cleanup; and progress/syllabus reconciliation. Include tasks only when actually needed. Do not expose proposed solutions or withheld test details in learner-facing prompts.

**Prompt execution protocol:** The learner opens the relevant Excel row, follows the `Saved prompt` link, copies or invokes the prompt in the working session, supplies listed inputs, and records the output/evidence and completion state in the workbook. Do not assume the assistant retains all prior context: prompts must be self-contained and point to persistent project artifacts.

## 7. Work stages

### Stage A — Do upfront, once

1. Collect and inventory current Fall and Spring sources.
2. Inspect the lecture PDFs; create a comprehensive topic/prerequisite/coverage map.
3. Fill only demonstrable instructional gaps with Spring or authoritative external resources.
4. Audit published labs and six assignments for public resources, missing private artifacts, tool dependencies, and cross-assignment continuity.
5. Define the assignment progression and assessment principles, without building all runtime resources.
6. Enumerate JIT tasks and their exact placement, triggers, dependencies, expected outputs, and completion criteria.
7. **Author and save every JIT prompt**, build the prompt index, and link prompts to the corresponding workbook rows.
8. Build and validate the entire ordered Excel syllabus as the executable master checklist.

### Stage B — Repeat just before a unit

1. Read the next actionable Excel row; execute the linked preparation prompt if one is due.
2. Prepare only the current unit's starter materials, dependencies, environment, and infrastructure.
3. Release and freeze the current assignment contract/acceptance criteria before implementation; keep future requirements unreleased.
4. Run a minimal environment/preflight check, recording evidence and deviations. Preserve intended failing tests.
5. Mark the preparation row complete (or blocked with a named recovery action).

### Stage C — Study, complete, and assess

1. Study linked instructional materials and additional readings only when needed.
2. Complete the exercise independently, using agents under the course's supervision principles.
3. Run objective tests and perform a critical review of code, specification, architecture, agent decisions, and written reasoning.
4. Ask adversarial/oral-defense questions and document uncertainty, counterexamples, and tradeoffs. Never assert successful completion on unverified grounds.
5. Resolve findings, record evidence and progress, and deprovision any temporary billable resources.
6. Refine future course instructions when genuine gaps emerge **without retroactively changing a released assignment's acceptance contract**.

## 8. Resource, cost, and security controls

- The learner manages their own AWS account; AWS-specific JIT prompts must specify how to verify account/region/profile, estimate cost exposure, set guardrails as appropriate, and destroy temporary resources when done.
- Do not request or print secrets, access tokens, credential files, personal keys, or private connection strings. Favor environment variables or secure secret management and redact logs.
- Do not run destructive cloud or repository operations without the learner's explicit approval. Record all provisioned billable resources and the matching teardown step as linked Excel tasks.
- Keep generated code, external agent logs, and testing data in approved repositories. Respect source licenses and avoid publishing proprietary code or credentials.

## 9. Quality gates

Before the **initial curriculum package** is called complete, confirm that:

- Every available Fall instructional unit and exercise is mapped; missing/unreleased items are marked accurately.
- Every supplementary resource is relevant and linked; gaps have not been invented or casually ignored.
- Every required JIT operation has a separately ordered Excel row, a unique stable ID, a **saved task-specific prompt**, a working link, a trigger, and a `Done when` criterion.
- The project dependency graph and six-assignment continuity are documented.
- The workbook can be used to decide the very next action without consulting hidden plans.

Before **each unit** is called ready, confirm that its input artifacts exist, its starter can run as intended, local/cloud configuration is documented, released requirements are frozen, and no intentional defects have been inadvertently repaired.

Before **each unit** is called complete, confirm its checks/review are recorded, unresolved deviations are explicit, and billable temporary infrastructure has an executed or explicitly scheduled teardown.

## 10. Agent communication and updates

- Treat the learner as the engineering decision maker; explain recommendations and tradeoffs, not just commands.
- Do not do entire exercises on the learner's behalf when the goal is student learning, unless the learner explicitly asks for a demonstration or solution.
- Use a clear distinction between **original CMU**, **adapted**, and **reconstructed** content.
- Maintain `progress/decisions.md` and `progress/change-log.md`; keep syllabus row IDs and prompt references stable across edits.
- When a source, resource, or exercise is unavailable, state the constraint and implement the smallest faithful substitute needed at that stage.
- Never claim an assignment is officially graded, officially equivalent, or exhaustively validated merely because a recreated test harness passes.

**Operational rule:** Plan the full path and write its JIT instructions in advance; build, provision, validate, and improve individual exercises only when their Excel triggers are reached.
