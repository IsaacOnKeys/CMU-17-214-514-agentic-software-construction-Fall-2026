# Assignment continuity and staged release

Planning document, not a released implementation contract. Detailed future contracts, seeded defects, assessor controls and solutions are not included here. Six public handouts were read in full; the source links below preserve the educational target.

```text
HW1: isolated intentionally flawed audit system
HW2: new progressive app + core v1 + learner capability contract + harness + ADRs
             ↓ same repository, data and decisions
HW3: evolve/regenerate internals under v2; preserve v1 callers and capability client
             ↓ same application baseline (HW4 is separate)
HW5: v3 replicas + notifications + comparable load evidence; no AWS deploy
             ↓ same v3 system, no new API version
HW6: AWS + CI/CD + telemetry + ≥3.5h operation + incident + teardown
HW4: separate full-history Jenkins snapshot; XML persistence subsystem only
```

At each prepare/release row, obtain original private inputs only if lawfully available; otherwise create the smallest faithful labeled substitute. Freeze current requirements and acceptance before implementation; hash the source/contract/rubric/evaluator version and baseline commit. Do not release v2/v3 specifics at HW2. Source handouts already expose the themes; the queue controls detailed contract release.

The official HW2/HW5 handouts permit learner CAPABILITY/NOTIFICATIONS revisions. This reconstruction applies the user’s stricter freeze rule: review learner specifications at the checkpoint, freeze before main build, retain prior versions, and require prospective reviewed ADR/version changes without relaxing released acceptance to fit a solution. Record this adaptation explicitly.

## HW01: Bad Slack

[Original brief](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw1.md)

- Starting inputs: public hw1.md; private original starter if the learner has lawful access, otherwise a clearly reconstructed flawed Slack-like starter
- Inaccessible/reconstruction audit: Original generated app, README claims, harness skeleton, deliverable templates, log examples and transcript exporter; staff acceptance suite is withheld.
- Release responsibility: Create only the flawed starter, blank AUDIT/REPAIRS/SUPERVISION templates, smoke/property scaffolds and local run instructions. Keep deliberate defects and their registry outside learner-facing prompts.
- Checkpoint intent: Phase 1 audit: learner interprets every README claim, records evidence, and ranks most/least severe issues. There is no official checkpoint for HW1.
- Final deliverables: Repair system; claim-mapped AUDIT.md and REPAIRS.md; test adequacy note; meaningful fast-check property with scope comment; green-before/after testability-refactor commits; plan, 5–10 real decisions, reflection and transcripts.
- Independent verification design: Public HTTP obligations plus complete README-driven browser demonstration, including ordinary reload/restart/reconnection conditions where relevant; independent claim-derived checks and meaningful property. Do not reveal the defect inventory.
- Published rubric dimensions: Functionality 30; Verification 25; Process 20; Design 10; README audit 10; Defense 5

## HW02: Better Slack

[Original brief](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw2.md)

- Starting inputs: Lab 1 export evidence; lectures 1–5; private core-api-v1.md if available; fresh progressive application repository
- Inaccessible/reconstruction audit: core-api-v1.md, private repository/course templates, docs/adr-examples.md, export script, correct/broken evaluator targets and hidden tests.
- Release responsibility: Create blank application workspace and planning/decisions/transcripts conventions, a versioned requirements manifest and scaffold instructions. Do not implement the server, CAPABILITY.md or learner validation harness.
- Checkpoint intent: Learner writes CAPABILITY.md and a validation harness covering it and the core before server implementation; review precision and freeze the learner-owned capability contract before the build.
- Final deliverables: Server and frontend, CAPABILITY.md, suitably tested code, harness/Dockerfile using BASE_URL and CORE_ONLY=1, deterministic isolated checks completing within 5 minutes, README local/harness/frontend/AWS instructions, four founding ADRs, planning and transcripts.
- Independent verification design: Run the learner harness on independent conforming and nonconforming controls; verify separation of core/capability verdicts and independence from initial state. Independently test server and frontend; perform a bounded AWS deployment demonstration and teardown.
- Published rubric dimensions: Functionality 25; Verification 35; Process 15; Design and memory 15; Defense 5; Checkpoint 5

## HW03: Two Roads

[Original brief](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw3.md)

- Starting inputs: same HW2 application; frozen v1 and capability contract; HW2 final commit, harness and accepted ADRs
- Inaccessible/reconstruction audit: core-api-v2.md and student-specific ta-client/client.mjs based on HW2 CAPABILITY.md; hidden v1/v2 targets.
- Release responsibility: Snapshot HW2 baseline and generate an independent read-only v1 client from the frozen HW2 CAPABILITY.md; release v2 and conflict-analysis instructions without implementing the changes.
- Checkpoint intent: AUDIT.md: per feature one impact sentence and up to five code locations; two located contextual smells; compatibility analysis ≤250 words; evolve/regenerate decision ≤100 words. Preserve checkpoint text and later append ≤5 sentences.
- Final deliverables: v1/v2 system and old client, updated CAPABILITY.md and harness conventions, old/new tests, frontend, data-model record and one record per capability, confirmed/superseded HW2 ADRs, planning and transcripts.
- Independent verification design: Replay read-only v1 client without modifying it, test old/new public contracts and learner-frozen capability choices, judge harness on independent broken/correct v2 controls. If regenerated, check no server code was copied and memory/harness/frontend survived.
- Published rubric dimensions: Functionality 30; Verification 25; Design and memory 20; Process 15; Defense 5; Checkpoint 5

## HW04: Jenkins

[Original brief](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw4.md)

- Starting inputs: L12; exact Jenkins jenkins-2.568.1 with full history; Lab 7 characterization practice before structural changes
- Inaccessible/reconstruction audit: Private full-history course fork at tag jenkins-2.568.1 plus hw4-start course commit; hidden behavior-preservation and correct/broken mutation targets.
- Release responsibility: Acquire upstream history/tag without changing upstream refs, verify revision and licenses, add separately tracked reconstructed course scaffolds and a local hw4-start baseline. Use JDK21 (25 permitted) and Maven; build core/war and the documented unit/functional slices only when this task is due.
- Checkpoint intent: ARCHAEOLOGY.md: four decisions ≤250 words each; two written-record decisions and two evidence-based reconstructed ADRs. Cite records at their revision as of the tag date in the brief; label unsupported rationale unknown.
- Final deliverables: ARCHAEOLOGY.md; PROPOSAL.md ≤500 words before first refactor, two rejected refactors, characterization classes and fixtures committed first, pinned/unpinned lists, structural behavior-preserving subsystem-only diff, planning and transcripts.
- Independent verification design: Copy only allowed subsystem files and new test classes/fixtures into a clean exact-tag tree; ignore edits to existing tests, junit-platform.properties and META-INF. Run core suite and XStream2Security383Test,XStream2AnnotationTest,OldDataMonitorTest slice. Check new tests on original and refactor plus private correct/broken controls; preserve known bugs.
- Published rubric dimensions: Functionality 30; Verification 20; Design 10; Memory 15; Process 15; Defense 5 correctness; Checkpoint 5

## HW05: Scale What You Built

[Original brief](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw5.md)

- Starting inputs: same progressive HW2/HW3 app; v1/v2 contracts, old client, harness, CAPABILITY.md and ADRs; L16 replica concepts
- Inaccessible/reconstruction audit: core-api-v3.md, compose.starter.yaml, proxy/nginx.conf, load/scaling.js, notifier service/protocol, hidden scenario targets.
- Release responsibility: Prepare replica/proxy scaffold and an independent notifier simulator with received/stats inspection. Give learner blank audit/policy scaffolds and fixed scaling procedure; do not make the learner app replica-correct or implement notification design.
- Checkpoint intent: Learner stack runs behind proxy at 1–4 replicas even if incorrect; one-command failing checks for at-risk guarantees, SCALE-AUDIT.md with code/check/verdict, measured one-replica throughput and draft NOTIFICATIONS.md.
- Final deliverables: compose.yaml stack, preserved old client/frontend, corrected audit checks, precise NOTIFICATIONS.md, v3/load-aware harness with BASE_URL/CORE_ONLY/NOTIFY_URL, tests, superseded ADRs and notification transport/rate/dedup/restart decision, planning and transcripts.
- Independent verification design: Verify every replica gets traffic using X-Upstream, test guarantees under bursts and replica loss, rate limit/DM delivery and policy with independent service records. Repeat fixed comparable 1/2/4 load procedure and judge ≥1.25× per step, not an invented absolute speed. No AWS deployment in HW5.
- Published rubric dimensions: Functionality 30; Verification 20; Design 20; Memory 10; Process 10; Defense 5; Checkpoint 5

## HW06: Operate What You Built

[Original brief](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/assignments/hw6.md)

- Starting inputs: same HW5 v3 application and frozen contracts; prior client/harness, cloud cost ledger, L20 CI and deployment concepts
- Inaccessible/reconstruction audit: deploy/ baseline, load/traffic.js, operations/README.md, keyed deployed NOTIFY_URL, degradation service and independent service-side record; hidden operations/security checks.
- Release responsibility: Create only deployment/instrumentation scaffolds and the independent operational simulator specification. Keep service key outside repo/chat/logs. Stage gates for learner pipeline, telemetry and incident report without building their solution.
- Checkpoint intent: One adapted AWS deployment health check, pipeline running tests/static gate and publishing private images/stack, observability ADR ≤300 words. Preserve evidence and tear down idle checkpoint infrastructure before later operating-block redeployment.
- Final deliverables: v3 stack with x_ health commit field; deploy/; CI history; OPERATIONS.md ≤400 words excluding quoted telemetry; raw telemetry/; pipeline/observability/degradation ADRs; planning and transcripts. No official HW6 spoken defense.
- Independent verification design: Each operating commit passed full tests/static/audit/gitleaks8.30.1 gates and deployed-health exact-commit wait; blocking secret/critical-vulnerability probes; private images/history clean or rotated leak evidence. Operate ≥3.5h with frozen traffic, acknowledge ≥1 real degradation, cross-check incident timeline/localization/impact/DM trace against withheld service record; capture before teardown.
- Published rubric dimensions: Functionality 30; Operations 35; Verification 15; Memory 5; Process 10; Checkpoint 5

## HW4 exact subsystem and historical snapshot

Preserve the exact `jenkins-2.568.1` tag and full reachable history. Do not silently substitute a newer Jenkins if the tag cannot be obtained. The public brief describes its tag date as July 9, 2026; verify tag/history at the JIT trigger and record any discrepancy before proceeding. Preserve licenses. The allowlist is `hudson/XmlFile.java`, `hudson/util/XStream2.java`, `XStream2SecurityUtils.java`, three `Robust*Converter.java` files, `hudson/util/xstream/`, `jenkins/util/xstream/`, `AtomicFileWriter.java`, and `hudson/diagnosis/OldDataMonitor.java` under core/src/main/java. Views and everything else are read-only. Copy new tests/fixtures only into the clean evaluator tree, excluding junit-platform.properties and META-INF.

## HW6 self-paced operational substitute

Replace the inaccessible course-held notifier with a separate assessor-run service exposing only the frozen public protocol. Preserve private fault timing and an independent timestamped service-side record. The learner must really operate for ≥3.5 hours; source dates become ordered start/capture/teardown gates. No fabricated runtime, log evidence or incident is acceptable. Independent hosting/assessment may require the learner to designate a separate operator at that trigger; do not invent one or send messages. No official HW6 oral defense is added.

## Carry-forward evidence

HW2→3→5→6 carries the same application identity, earlier API contracts, accepted data model/schema, harness, old capability client, frontend, planning/transcripts and append-only decision history. Preserve immutable assignment-baseline commits. Regeneration under HW3 changes implementation, not the compatibility bar or decision history. The separate Jenkins tree never replaces the progressive application.
