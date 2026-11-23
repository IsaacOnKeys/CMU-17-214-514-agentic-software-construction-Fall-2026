# Public lab audit

Static audit only: complete Fall handouts and each public starter SETUP.md, manifests, CI configuration, named templates and staged-file presence were inspected. No lab runtime was installed, no starter tests were run and no defects were repaired during syllabus construction. Expected counts below are source claims, not observed passes. Exact source revisions and file hashes are in [source-manifest.json](source-manifest.json).

## Lab 01: Course Infrastructure and Your First Supervised Task

Handout: [lab01](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab01.md). [Original public starter](https://github.com/CMU-17-214/f26-lab01); archived at `course-materials/starters/f26-lab01/`.

- Objective: Trace a layered bug, supervise cancellation and review a plausible bad patch.
- Tools: JDK 21+; Maven 3.8+; editor; chosen agent with complete transcript export
- Minimal JIT health command: `mvn test`
- Expected starter state: Compilation and discovery succeed; exactly one intended test failure, as SETUP.md describes. Record the failing test name without diagnosing it.
- Required artifacts audited: SETUP.md, ARCHITECTURE.md, TASK.md, tools/export-transcripts.sh, changes/agent-attempt.patch
- Adaptation and scope: Leave the failing behavior and staged patch untouched in preparation. Do not inspect or explain the patch before the learner reaches milestone 3.
- Milestone evidence: root-cause explanation, small cancellation commits, cross-cutting test, patch verdict, local uncommitted transcripts and README tool/model line
- Review focus: Check the no-overlap invariant and waitlist effect with learner-supplied evidence; inspect commit scope and the patch accept/reject reasoning without revealing answers in advance.

## Lab 02: Testing, Testability, and Auditing a Generated Suite

Handout: [lab02](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab02.md). [Original public starter](https://github.com/CMU-17-214/f26-lab02); archived at `course-materials/starters/f26-lab02/`.

- Objective: Specify a full invariant, observe shrinking and critique high-coverage generated tests.
- Tools: JDK 21+; Maven; jqwik 1.8.4 and JaCoCo 0.8.12 from pom.xml; GitHub Actions access when performing the lab
- Minimal JIT health command: `mvn test`
- Expected starter state: Shipped examples and the provided property pass; target/site/jacoco/index.html is produced. Green is not evidence that the defect is absent.
- Required artifacts audited: SETUP.md, ARCHITECTURE.md, pom.xml, AvailabilityProperties.java and generated example suite
- Adaptation and scope: Do not strengthen the property, repair the calculator, or optimize tests during setup. Preserve the learner’s red-property commit before the repair.
- Milestone evidence: learner property, shrunk sample and explanation, red then green CI runs, three controllability/observability weaknesses
- Review focus: Verify the property was committed failing before the fix and was not weakened; trace each of the three suite weaknesses to a missing control or observation.

## Lab 03: Find the Design Gap

Handout: [lab03](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab03.md). [Original public starter](https://github.com/CMU-17-214/f26-lab03); archived at `course-materials/starters/f26-lab03/`.

- Objective: Map implemented design, diagnose two consequential problems and defend alternative decompositions.
- Tools: JDK 21+ and Maven; no cloud deployment
- Minimal JIT health command: `mvn test`
- Expected starter state: Shipped suite passes; CRITIQUE.md and DESIGN.md exist.
- Required artifacts audited: SETUP.md, DESIGN.md, CRITIQUE.md, service code
- Adaptation and scope: This is a writing-only lab: change no production code. Replace the Academy account pre-check with the separately queued personal-AWS readiness task.
- Milestone evidence: CRITIQUE.md: data/operations/structure, request trace, two problems, two decompositions and conditional preference
- Review focus: Check each design claim against code and follow a reschedule request; require real costs and a condition that changes the preferred decomposition.

## Lab 04: Baby AWS Deploy

Handout: [lab04](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab04.md). [Original public starter](https://github.com/CMU-17-214/f26-lab04); archived at `course-materials/starters/f26-lab04/`.

- Objective: Deploy, diagnose a deliberately broken deployment from logs, redeploy through IaC, and prove teardown.
- Tools: JDK/Maven; Docker Linux engine; AWS CLI v2; SSM plugin or console; personal AWS profile and region
- Minimal JIT health command: `from service/ run mvn test; return to the repository root, run docker info and docker build -t lab04-local .; run the README local container and curl /api/health, then stop only that container`
- Expected starter state: Tests and local health succeed; adapted infrastructure passes CloudFormation template validation; account, profile, region, estimated exposure and linked teardown are recorded before creating resources.
- Required artifacts audited: SETUP.md, README.md, Dockerfile, infra/template.yaml, infra/params-healthy.json, infra/params-scenario2.json, DEPLOYMENT.md
- Adaptation and scope: Keep healthy and broken scenario parameters distinct. Adapt LabInstanceProfile/vockey, default-network assumptions and ingress for a personal account without repairing the intended scenario. No cloud creation in preflight.
- Milestone evidence: DEPLOYMENT.md: healthy URL/check, broken-deploy logs and diagnosis, healthy IaC redeploy, deletion and resource-inventory proof
- Review focus: Verify warmup was allowed before failure diagnosis, URLs/instance IDs match each recreate, the fix was via IaC, and no billable resources remain before signoff.

## Lab 05: Anti-Pattern Critique of Generated Code

Handout: [lab05](https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab05.md). [Original public starter](https://github.com/CMU-17-214/f26-lab05); archived at `course-materials/starters/f26-lab05/`.

- Objective: Identify consequential classic/agent smells and make one minimal behavior-preserving fix.
- Tools: Node 20+; npm; TypeScript and Vitest from lockfile
- Minimal JIT health command: `npm ci; npm test; npm run typecheck`
- Expected starter state: 39 shipped tests and the typecheck pass.
- Required artifacts audited: SETUP.md, package.json, package-lock.json, src/, tests/, SMELLS.md
- Adaptation and scope: Do not edit any shipped test. Preparation must leave the smell inventory and candidate fix to the learner.
- Milestone evidence: SMELLS.md, three located smells, one scoped diff, two uncoded proposals, one contextual false positive
- Review focus: Map each smell to a principle and change cost; verify tests are unchanged, behavior is preserved and the scope line explains why work stopped.

## Lab 06: API Contract Under Pressure

Handout: [lab06](https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab06.md). [Original public starter](https://github.com/CMU-17-214/f26-lab06); archived at `course-materials/starters/f26-lab06/`.

- Objective: Predict additive/breaking effects and demonstrate a deprecation path against an untouched consumer.
- Tools: JDK 21+; Maven parent reactor
- Minimal JIT health command: `mvn -B test`
- Expected starter state: 5 api tests plus 7 consumer tests pass; all three reactor entries succeed.
- Required artifacts audited: SETUP.md, api/ BookingApi javadoc, consumer/FrontDesk.java, CONTRACT.md
- Adaptation and scope: consumer/ is read-only. Do not implement overloads or the request-object migration in preparation; predictions belong to the learner before each build.
- Milestone evidence: CONTRACT.md predictions and module outputs, overload/request/deprecation commits, misuse redesign with tradeoff
- Review focus: Compare the consumer tree with the baseline; verify clean builds expose both the breaking step and restored compatibility, and retained all five api tests.

## Lab 07: Direct a Refactor

Handout: [lab07](https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab07.md). [Original public starter](https://github.com/CMU-17-214/f26-lab07); archived at `course-materials/starters/f26-lab07/`.

- Objective: Characterize first, direct one named refactor and critique justified/missing patterns.
- Tools: JDK 21+ and Maven
- Minimal JIT health command: `mvn -B test`
- Expected starter state: 35 shipped tests pass (18 workflow, 7 reports, 6 pricing, 4 notifications).
- Required artifacts audited: SETUP.md, workflow/BookingWorkflow.java, notify/, pricing/, REFACTOR.md
- Adaptation and scope: Never edit or delete an existing test method. Leave characterization target, refactor choice and pattern judgments to the learner.
- Milestone evidence: REFACTOR.md, a new green characterization test committed first, scoped refactor across four methods, pattern critique and missing-pattern judgment
- Review focus: Read history to establish pin-before-refactor order; inspect all four repeated-condition sites, unchanged shipped tests and regenerate-versus-refactor rationale.

## Lab 08: Supervise a Repo-Scale Task

Handout: [lab08](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab08.md). [Original public starter](https://github.com/CMU-17-214/f26-lab08); archived at `course-materials/starters/f26-lab08/`.

- Objective: Decompose CampusReserve, demonstrate a binding guardrail, execute exactly one task and settle a refuter claim.
- Tools: JDK 21+; Maven; Python 3.11+ with isolated pytest; chosen agent guardrail/manual-mode support
- Minimal JIT health command: `mvn -B test; from analytics run the virtual environment’s python -m pytest`
- Expected starter state: 418 Java and 137 Python tests pass independently; seven Maven modules and analytics are discoverable.
- Required artifacts audited: SETUP.md, CHANGE-REQUEST.md, AGENTS.md, ARCHITECTURE.md, PLAN.md, guardrails/README.md
- Adaptation and scope: Never edit shipped tests. Do not implement the change request in setup. Select and prove the guardrail during the lab, not through a harmless configuration-only claim.
- Milestone evidence: PLAN.md: 3–4 tasks/gates/blind spots, out-of-scope modules, actual blocked agent tool call, predeclared takeover, one task diff, module gate, closing clean build, fresh refuter and settled finding
- Review focus: Confirm exactly one task ran, scope reconciles file by file, rule 3/4 checkpoints are named, 418+137 baselines are preserved plus new tests, and refuter probes are removed.

## Lab 09: Boundaries, State, and Copies

Handout: [lab09](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab09.md). [Original public starter](https://github.com/CMU-17-214/f26-lab09); archived at `course-materials/starters/f26-lab09/`.

- Objective: Recover implemented architecture and demonstrate cross-copy failures without changing platform code.
- Tools: JDK/Maven; Python 3.11+/pytest; Docker Compose; nginx; grafana/k6:2.3.0 container
- Minimal JIT health command: `mvn -B test; from analytics run isolated python -m pytest; docker info; docker compose version`
- Expected starter state: 478 Java and 150 Python tests pass; supplied Dockerfile and proxy/nginx.conf exist. Do not create the learner’s compose.yaml or k6 scripts in setup.
- Required artifacts audited: SETUP.md, ARCHITECTURE.md, AGENTS.md, BOUNDARIES.md, Dockerfile, proxy/nginx.conf
- Adaptation and scope: Production code and tests are read-only. Use fresh f26-lab09, not the learner’s modified Lab 8 tree. Preserve per-copy startup token evidence locally.
- Milestone evidence: BOUNDARIES.md, checked architecture drawing and two discrepancies, learner compose.yaml, two thresholded load scripts, two X-Upstream values and boundary proposal
- Review focus: Require evidence both copies received traffic; check scripts can fail their claims, auth masking is handled, and the proposed data owner/invariant/cost is concrete.

## Lab 10: Find the Race

Handout: [lab10](https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab10.md). [Original public starter](https://github.com/CMU-17-214/f26-lab10); archived at `course-materials/starters/f26-lab10/`.

- Objective: Force a deterministic interleaving, judge a proposed patch, and choose one bounded concurrency fix.
- Tools: JDK 21+ and Maven
- Minimal JIT health command: `mvn -B test`
- Expected starter state: 11 shipped tests pass; stress runner is separate and is not needed for starter health.
- Required artifacts audited: SETUP.md, README.md, TICKET.md, RACE.md, RaceTest.java, PausingStore
- Adaptation and scope: proposed-fix.diff is off-limits until milestone 2, including for the agent. Do not select the pause aim or investigate the race during preparation.
- Milestone evidence: RACE.md suspect table and committed prediction, two timestamped red deterministic runs, patch verdict with second schedule, one shipped-code fix and cost
- Review focus: Check the prediction predates the runs, red CI evidence remains until milestone 3, patch evaluation re-aimed the schedule, and the final fix was applied to shipped code.

## Lab 11: Events, Replay, and Refunds

Handout: [lab11](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab11.md). [Original public starter](https://github.com/CMU-17-214/f26-lab11); archived at `course-materials/starters/f26-lab11/`.

- Objective: Judge sync/event boundaries, demonstrate replay safety and recover a partial handler failure.
- Tools: Node 20+; npm; TypeScript/Vitest/tsx/fast-check from lockfile
- Minimal JIT health command: `npm ci; npm run typecheck; npm test`
- Expected starter state: 33 shipped tests pass; replay/failure demos exist but are not preflight checks and are not run yet.
- Required artifacts audited: SETUP.md, TICKET.md, EVENTS.md, src/demos/replayDemo.ts, src/demos/failureDemo.ts
- Adaptation and scope: No real broker is needed. Do not run the replay demo before the learner writes the prediction, or repair the handler during setup.
- Milestone evidence: EVENTS.md operations table and arguments, prediction, raw replay output before/after, handler diff, partial-failure recovery and alternative cost
- Review focus: Distinguish delivery semantics from races; verify actual side effects after repeated delivery and partial failure, not only green tests or a remembered message ID.

## Lab 12: Set Up a CI Gate

Handout: [lab12](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/labs/lab12.md). [Original public starter](https://github.com/CMU-17-214/f26-lab12); archived at `course-materials/starters/f26-lab12/`.

- Objective: Create CI, capture independent failing gates, triage an audit and show a bad PR blocked.
- Tools: Python 3.11+; isolated requirements-dev.txt; pytest, ruff, mypy, pip-audit; fork Actions permissions
- Minimal JIT health command: `isolated python -m pip install -r requirements-dev.txt; isolated python -m pytest`
- Expected starter state: 18 shipped tests pass. Do not run/fix ruff, mypy or the dependency audit as preparation.
- Required artifacts audited: SETUP.md, README.md, pyproject.toml, requirements.txt, requirements-dev.txt, changes/bad-change.patch
- Adaptation and scope: Do not write the student workflow or fix seeded static findings in setup. Preserve the independent red jobs and do not merge the staged bad-change PR.
- Milestone evidence: learner ci.yml, green tests-only run, red then green independent gate jobs, audit decision, open bad-change PR on own fork and limits
- Review focus: Verify test/lint/type/audit jobs are independent, the red run precedes fixes, accepted advisories have reasons, and the PR’s actual base is the learner fork.

## Lab 13: Make It Observable

Handout: [lab13](https://cmu-17-214.github.io/f2026/index.html#schedule). Handout/starter unlinked in snapshot; release or reconstruction is deferred to its source-refresh row.

- Objective: Use telemetry to localize a fault and trace one request across a boundary (reconstructed pending release).
- Tools: Determined at JIT release; prefer the existing HW6 stack, logs and metrics; no extra cloud account
- Minimal JIT health command: `Use the minimal start/health/log/metric command specified in the newly frozen Lab 13 handout; do not run the fault scenario during preflight.`
- Expected starter state: A published official starter is healthy as documented, or the labeled reconstructed starter emits a traceable healthy request. Freeze the baseline before learner work.
- Required artifacts audited: Fall schedule, future official labs/lab13.md if published, HW6 frozen operations contract and learner telemetry, curriculum/reconstructed-study-guides.md
- Adaptation and scope: The snapshot contains no Lab 13 handout/repository link. Refresh first. If still unavailable, write a reconstructed three-milestone lab without claiming original objectives beyond the published title; do not supply its solution.
- Milestone evidence: reconstructed-or-official handout provenance, request correlation evidence, meaningful metric/alert demonstration, localized incident explanation and limits
- Review focus: Judge only frozen milestones: signal and request trace, evidence of a user-visible alert, and localization against reproducible fault evidence; do not claim CMU signoff.

## Material personal-account adaptation: Lab 4

The actual `infra/template.yaml` sets `IamInstanceProfile: LabInstanceProfile`, `KeyName: vockey`, assumes usable default networking and opens SSH 22 to 0.0.0.0/0 in addition to the service port. Its comment claiming only service ingress does not match that SSH rule. The four-hour shutdown stops the instance but does not delete the stack/disks or guarantee zero charges.

At the Lab 4 JIT trigger, parameterize/provide the personal-account instance profile with required SSM permissions; remove the Academy key requirement when SSM is sufficient, or use an explicitly selected private key without copying it into the repo. Restrict/remove SSH and inspect network availability; create an explicit minimal VPC/subnet only if needed. Review all IAM/network changes and cost estimates before execution. Keep scenario parameters intact and track the adaptation diff against the archived original. Do not build the adaptation now.

## Other operational observations

- Labs 8 and 9 are distinct pristine starter revisions (418+137 versus 478+150 tests). Lab 9 is not the learner’s partially completed Lab 8 tree.
- `mvn -B clean test` is required to close Lab 8; a warm reactor can hide a cross-module compilation break. Python analytics runs separately.
- Lab 9 requires X-Upstream diversity before trusting a two-copy result; k6 `run --no-deps` avoids resetting the api service scale.
- Lab 10 proposed-fix.diff remains unopened until milestone 2. Lab 11 demo predictions precede execution. Lab 12 static/audit findings and staged PR remain part of learning, not preparation repairs.
- GitHub Actions/fork/PR demonstrations require the learner’s account and explicit publication authorization at execution. If access is blocked, record a recovery task; local tests alone do not prove the required remote CI history.
- Windows path translation is local and specific; do not provision a second OS, every runtime or a cloud account upfront.
