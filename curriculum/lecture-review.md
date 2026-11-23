# Fall lecture review

Review basis: all 21 published PDF decks were extracted page by page and examined using page-indexed text digests, targeted full-text examples and selected rendered diagram/image slides. Complete text and PDFs are retained locally. This is a text-led instructional analysis, not an exhaustive visual review of every slide or access to recorded teaching. Sparse/image slides need the source visual; no unseen speech or Canvas material is inferred.

The [page index](lecture-page-index.md) records extraction coverage for every PDF page. [pdf-extraction.json](pdf-extraction.json) records counts and sparse pages. The following per-deck judgments distinguish supplied teaching from operational/prerequisite gaps.

## LEC-01: Course Introduction and Modern Software Engineering

Source: [01-introduction.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/01-introduction.pdf); focal pages 11–15; 18–28; 31–45.

**Supplied teaching and examples.** Tetris demo versus shippable system; reach, verifiability, and reversibility determine delegation; six assignment themes and accountable ownership.

**Assumed prerequisites.** Two programming courses or equivalent; basic algorithms, data structures, invariants.

**Gap judgment.** The live demo and image-only slides cannot substitute for explanation. Use the written course goals and compare a demo claim with a maintained-system obligation.

**Verification.** For a generated feature, name a cheap verification step and a failure whose reach makes human review necessary.

## LEC-02: Agentic Development and Design for Verification

Source: [02-agentic-development.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/02-agentic-development.pdf); focal pages 11–20; 23–37; 40–50.

**Supplied teaching and examples.** Tetris state/rules/input/rendering/scoring decomposition; finite context and rot; instructions versus enforced hooks; bad-generation recovery and disk-backed fresh-session loops.

**Assumed prerequisites.** L01; git diff/branch/commit concepts.

**Gap judgment.** CLI commands and permission semantics are tool/version specific. Verify the chosen tool and transcript export at Lab 1; do not install multiple agents or copy an unverified hook.

**Verification.** Write one task with inputs, scope, a gate, a rollback checkpoint, and a takeover condition; explain why an instruction file alone cannot enforce it.

## LEC-03: Testing and Testability

Source: [03-testing-and-testability.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/03-testing-and-testability.pdf); focal pages 4–22; 24–38; 40–54.

**Supplied teaching and examples.** BookingService hides a real clock and repository and returns void; injection makes time controllable, a result observable. Ports/adapters, test doubles including saboteurs, SOLID, discovery counts, oracle problems, and architecture tests.

**Assumed prerequisites.** L02; Java interfaces/visibility, exceptions, basic JUnit assertions.

**Gap judgment.** Framework syntax and fake/stub/mock distinctions may be unfamiliar. Spring Testability and the Test Doubles handout supply targeted prerequisite explanations; use only if the learner cannot explain the Clock example.

**Verification.** Explain how a passing booking test can lack either control or observation, and identify what its oracle should be.

## LEC-04: Test Design and Coverage

Source: [04-test-design-and-coverage.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/04-test-design-and-coverage.pdf); focal pages 10–18; 20–37; 39–57.

**Supplied teaching and examples.** Bank-account pre/postconditions and invariants; shipping-weight partitions; half-open intervals; jqwik-style generated sequences and shrinking; integration joints; branch/path coverage, Goodhart, mutation testing and adequacy rationale.

**Assumed prerequisites.** L03; Boolean conditions, interval arithmetic, deterministic test assertions.

**Gap judgment.** jqwik and fast-check use different APIs. Read their official property/generator/shrinking documentation before Lab 2 and HW1 respectively; the conceptual PBT explanation is already in Fall.

**Verification.** Give a boundary bug a 100% branch-covered suite could miss, and one invariant that generated sequences would test.

## LEC-05: What Is a Software System's Design?

Source: [05-what-is-design.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/05-what-is-design.pdf); focal pages 4–14; 22–46; 49–65.

**Supplied teaching and examples.** Next-free-booking ambiguity demonstrates validation-first design. Room/User/Booking entity/value model; half-open intervals versus slots; reference ownership, error precedence, tolerant readers, representational gap and availability caches.

**Assumed prerequisites.** L04; entities/values, references, basic HTTP request/response concepts.

**Gap judgment.** The public brief omits core-api-v1.md, so slide examples cannot recover its full interface. Release a clearly reconstructed contract at HW2 preparation. Spring OO/UML supports diagram reading if needed.

**Verification.** Compare interval and fixed-slot models; name an invariant every operation inherits and one change made expensive by each design.

## LEC-06: Communicating and Recording Designs

Source: [06-communicating-designs.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/06-communicating-designs.pdf); focal pages 12–27; 29–49; 54–60.

**Supplied teaching and examples.** ADR overlap-check and SQLite critiques; accepted records are superseded. A cancellation trace violates ordering and waitlist obligations. Architecture sketches, dataflow trust boundaries, instruction files, skills and pattern vocabulary.

**Assumed prerequisites.** L05; requests and object calls; distinguish what from why.

**Gap judgment.** Fall already provides ADR form, examples, and failure modes. No mandatory external ADR course is needed. Tool-specific instruction/skill behavior is checked at its JIT trigger.

**Verification.** Identify a fake alternative in an ADR and explain how a sequence diagram can contradict an invariant.

## LEC-07: Design for Change

Source: [07-design-for-change.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/07-design-for-change.pdf); focal pages 13–34; 37–45; 48–59.

**Supplied teaching and examples.** Booking waitlist coordinator versus Room doing everything; import, hidden/global, control and temporal coupling; Information Expert, Creator, Controller, Protected Variations, Pure Fabrication; stable dependency direction and safe delegation.

**Assumed prerequisites.** L05–L06; interfaces, object references and dependency direction.

**Gap judgment.** Spring Responsibility Assignment can deepen GRASP if the learner cannot price the waitlist tradeoff; do not require implementing Spring Santorini.

**Verification.** Assign waitlist promotion and notification responsibilities, then predict which modules an SMS requirement changes.

## LEC-08: Modularity and Anti-Patterns

Source: [08-modularity-and-anti-patterns.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/08-modularity-and-anti-patterns.pdf); focal pages 12–35; 40–58.

**Supplied teaching and examples.** God class, feature envy, intimacy, shotgun surgery, divergence, cycles, hidden dependencies, primitive obsession, flags, refused bequest; agent duplication, over-abstraction, convention drift, phantom complexity and inflated comments.

**Assumed prerequisites.** L07; cohesion/coupling and contextual change costs.

**Gap judgment.** The Spring refactoring lab appendix is a useful smell catalog, not a replacement exercise. Midterm 1 explicitly excludes this lecture despite occurring afterward.

**Verification.** Tie one smell to a file, violated principle, and likely change cost; give one justified false positive.

## LEC-09: Refactoring and Design Improvement

Source: [09-refactoring.pdf](https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/09-refactoring.pdf); focal pages 7–17; 19–38; 42–50.

**Supplied teaching and examples.** Two hats separate restructuring from behavior changes; characterize zero-length booking even if buggy; extraction rhythm; count read moved after insert changes fee tiers; coverage, code age, spec quality and reach decide two roads.

**Assumed prerequisites.** L08; test oracle distinction, git history and public behavior.

**Gap judgment.** Existing suite green is only a starting point. Spring refactoring offers extra examples; Lab 7 and Jenkins supply the required practice without another mandatory codebase.

**Verification.** Explain why a preserved bug belongs in a characterization test and identify a changed observation in a purported cleanup.

## LEC-10: Design Patterns and Tradeoffs

Source: [10-design-patterns.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/10-design-patterns.pdf); focal pages 7–29; 31–47.

**Supplied teaching and examples.** Pricing policy injected by composition; cancellation subscriptions; centralized notifier creation; Open/Closed along one axis; testability injection points, quality attributes and pattern soup.

**Assumed prerequisites.** L07–L09; interfaces, composition, inheritance and polymorphism.

**Gap judgment.** If composition versus inheritance is unfamiliar, read Spring Inheritance and Delegation before this deck. Fall teaches the patterns; no extra pattern implementation is required.

**Verification.** For one pattern, state the problem, roles, benefit and concrete cost; describe the requirement that would justify an otherwise excessive layer.

## LEC-11: APIs, Libraries, and Frameworks

Source: [11-apis-libraries-frameworks.pdf](https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/11-apis-libraries-frameworks.pdf); focal pages 6–25; 28–40; 43–56.

**Supplied teaching and examples.** Typed UserId/RoomId/TimeRange; errors and LSP/ISP; Hyrum and deprecation; contract tests with real versus fake collaborators; Template Method, Adapter, reuse versus generated RFC recurrence support.

**Assumed prerequisites.** L10 and Lab 6 introduction; compiler types and HTTP validation.

**Gap judgment.** Lab 6 precedes this lecture and has its own additive/breaking/deprecation primer. Read that primer before Lab 6; Spring API Design is optional explanation, not a prerequisite ordering change.

**Verification.** Show a compiler-enforced misuse constraint and a network boundary that still needs runtime validation; propose a compatibility path.

## LEC-12: Evolution, Drift, and Decision Archaeology

Source: [12-evolution-drift-memory.pdf](https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/12-evolution-drift-memory.pdf); focal pages 6–26; 29–47.

**Supplied teaching and examples.** Lehman and incremental drift; architecture import checks; examine/probe/modify; Jenkins modules and queue trace; git log -S and blame recover records, while unknown rationale stays unknown.

**Assumed prerequisites.** L11; git log/blame and bounded request tracing.

**Gap judgment.** HW4 requires full history and historical record revisions. A shallow Jenkins checkout is inadequate; acquire the exact tag and history only at HW4 preparation. Fall already teaches engineering memory.

**Verification.** Trace one claim to code, a dated record and a probe; label which part of the rationale remains unknown.

## LEC-13: Agent Architectures

Source: [13-agent-architectures.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/13-agent-architectures.pdf); focal pages 8–19; 21–36; 38–51.

**Supplied teaching and examples.** Bug-triage agent illustrates retrieval misses, tool APIs, permissions, MCP dependencies, lazy skills, structured output shape versus truth, coordination handoff loss and SWE-bench-style repeated evals.

**Assumed prerequisites.** L02, L06, L12; APIs and least privilege.

**Gap judgment.** Fall covers the concepts. Current MCP participants/layers documentation supplements the protocol boundary only. Tool counts and permission UI in slides are snapshot-specific, not promises about installed tools.

**Verification.** Give a triage agent its narrowest action space, distinguish schema validity from a correct severity judgment, and name an eval blind spot.

## LEC-14: Agent Supervision and Safety

Source: [14-agent-supervision.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/14-agent-supervision.pdf); focal pages 8–18; 20–40; 42–51.

**Supplied teaching and examples.** Exception-to-result migration template gate then batches; overnight loops compound mistakes; refuter findings need reproduction; deny rules/hooks/sandboxes and bypasses; prompt injection, reward hacking, budget/turn caps and externally recorded actions.

**Assumed prerequisites.** L13; tests, diff review and process records.

**Gap judgment.** Provider-specific permission behavior can drift. Lab 8 must demonstrate a real block in the selected tool and manual approval mode where relevant. Reading a configuration is insufficient; no blanket autonomous run is needed.

**Verification.** Write a slice gate that could still miss a bug; explain how to settle a refuter finding and why filesystem enforcement differs from a prompt.

## LEC-15: Software Architecture and Subsystem Design

Source: [15-software-architecture.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/15-software-architecture.pdf); focal pages 6–21; 23–43; 44–48.

**Supplied teaching and examples.** Layers, ports/adapters, pipes/filters and event styles; ArchUnit baselines; code versus stale diagrams; Conway, one data writer, modular monolith versus services, Segment consolidation and Facade costs.

**Assumed prerequisites.** L07, L11, L14; ownership and dependency direction.

**Gap judgment.** No conceptual replacement needed. Lab 9 uses import/call evidence rather than trusting ARCHITECTURE.md, and preserves production code/tests.

**Verification.** Draw one data owner and its public boundary, justify keeping or extracting a service, and name an enforceable architecture rule.

## LEC-16: Data Models at Scale (deck: State at Scale)

Source: [16-data-models-at-scale.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/16-data-models-at-scale.pdf); focal pages 5–15; 17–29; 31–52.

**Supplied teaching and examples.** Process-local sessions fail across copies; Compose DNS and X-Upstream checks; k6 correctness/throughput/p95; locked versus database-constrained curve; N+1, keys, cache freshness, lost updates, read models, sharding, expand/migrate/contract and restore checks.

**Assumed prerequisites.** L15; processes versus memory, basic persistence and percentiles.

**Gap judgment.** Compose/k6 are operational prerequisites for Lab 9 and HW5. Read official Compose scaling and k6 thresholds before those tasks; do not add a database administration course.

**Verification.** Explain a false scaling result caused by one active replica; choose a consistency requirement and an online schema transition.

## LEC-17: Concurrency and Asynchrony

Source: [17-concurrency.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/17-concurrency.pdf); focal pages 7–17; 19–33; 35–49.

**Supplied teaching and examples.** Double-booking and lost updates; one atomic map call is not a compound transaction; locks/visibility/deadlock ordering; immutability and confinement; await interleavings; per-instance lock mistake; PausingStore-controlled schedule.

**Assumed prerequisites.** L16; shared mutable state and request concurrency.

**Gap judgment.** Spring Java Parallelism and TS Asynchrony explain language mechanisms if needed. Midterm 2 focuses through L16 and explicitly excludes this lecture as new content.

**Verification.** Write the two-request interleaving and show why a per-process lock cannot enforce a multi-replica invariant.

## LEC-18: Coordinating and Communicating Systems

Source: [18-coordinating-systems.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/18-coordinating-systems.pdf); focal pages 8–20; 22–28; 30–47.

**Supplied teaching and examples.** Unknown timeout outcome, CAP under partition, queues/backpressure/streams/groups; transactional outbox closes dual-write gap but allows duplicates; Decorator, circuit breaker, idempotency transaction, dead letters, sagas and consumer lag.

**Assumed prerequisites.** L17; transactions and asynchronous completion.

**Gap judgment.** The in-memory Lab 11 bus intentionally removes broker provisioning and races. No Kafka service is required. Spring distributed robustness is optional reinforcement.

**Verification.** Place the crash window in a handler and explain what must share a transaction; distinguish retry safety from exactly-once claims.

## LEC-19: Containers and the Cloud

Source: [19-containers-and-cloud.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/19-containers-and-cloud.pdf); focal pages 8–23; 25–40; 42–47.

**Supplied teaching and examples.** Container versus VM; Lab 4 multi-stage Dockerfile and boot script; registries/digests, regions/zones and network hops; volumes and schema rollback; cold-start lag, liveness/readiness, SIGTERM, secret-free images and golden paths.

**Assumed prerequisites.** L16–L18; Lab 4 operational experience.

**Gap judgment.** Personal AWS lacks Academy profiles, keys and automatic budget limits. Unit-specific adaptation and teardown prompts cover this gap; stop timers do not remove disks or public IPv4 charges.

**Verification.** Trace a failed health request through DNS/network/port/process and identify state that would be lost on replacement.

## LEC-20: DevOps

Source: [20-devops.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/20-devops.pdf); focal pages 9–28; 29–44; 46–49.

**Supplied teaching and examples.** CI/trunk/required checks and delivery versus deployment; build once/promote; rolling, blue-green, canary and flags; user risk; CrowdStrike and Knight deploy checks; GitLab restore incident; blameless postmortems and delivery metrics.

**Assumed prerequisites.** L19; images, health, previous compatible schemas.

**Gap judgment.** Spring DevOps is optional explanation. HW6 must wait for deployed health to report its exact commit, not just a 200; no live CI pipeline is constructed in Stage A.

**Verification.** Select a rollout and a measurable rollback trigger; explain why reverting code cannot reverse a destructive schema change.

## LEC-21: Verification in the Pipeline

Source: [21-verification-pipeline.pdf](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/21-verification-pipeline.pdf); focal pages 6–22; 24–44; 47–55; 59–62.

**Supplied teaching and examples.** Floating promises missed by happy-path tests; lint/type/analyzer distinctions and false positives/negatives; baselines, suppression discipline, any/as escape hatches, flaky-test controllability, fuzz campaign triage, reviewer fallibility and optional formal proof/spec limits.

**Assumed prerequisites.** L03–L04, L17, L20; Python annotations and isolated environments for Lab 12.

**Gap judgment.** Lab 12 needs Python/pytest/ruff/mypy/pip-audit syntax but intentionally postpones static/audit findings until milestone 2. The bonus proof slides are enrichment, not a new required proof project.

**Verification.** Choose one blocking gate and one reporting check; explain a bypass and an independent demonstration that a bad change is actually blocked.
