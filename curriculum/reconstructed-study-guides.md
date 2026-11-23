# Reconstructed guides for currently unlinked Fall units

These are newly authored study instructions, not official Fall slides. Each queued source-refresh prompt first checks for newly published official material. If available, use and analyze it instead; preserve the historical snapshot and frozen assignment obligations.

## LEC-22: Supply Chain Security

First use the [Spring Supply Chain Security lecture](https://docs.google.com/presentation/d/1YoOMUDJGqPH7lUai7k1Q3NyLEe2X4vhGVYvr1_hjNAs/edit?usp=sharing) as the CMU explanation. Read its dependency/transitive-dependency, malicious-package, maintainer and build-access examples. Where build provenance remains unclear, read [SLSA v1.2 threats overview](https://slsa.dev/spec/v1.2/threats-overview): identify who can change source, dependencies, workflow and built output. Do not confuse a clean vulnerability audit with proof that a package is trustworthy.

Draw your HW6 build chain: source → dependencies/actions → builder → image registry → deployed instance. Label one trust decision and one evidence artifact at each edge. Explain lockfiles versus immutable digests, least-privilege workflow credentials, and why secret scanning cannot revoke an already exposed secret. Use [GitHub secure workflow guidance](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) only for your remaining workflow-specific questions. Leave gate implementation to the assignment.

Done when your notes cite the Spring pages actually read, distinguish known-vulnerability, malicious-content and provenance checks, and explain one threat your current gates cannot detect. If the Spring export is unavailable, record the access failure and use SLSA plus GitHub guidance as the labeled reconstructed explanation; do not report having read the deck.

## LEC-23: Observability and Monitoring

Read [Google SRE, Chapter 6](https://sre.google/sre-book/monitoring-distributed-systems/), specifically Definitions, Symptoms Versus Causes, Black-Box Versus White-Box, The Four Golden Signals, and As Simple as Possible, No Simpler. Read [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/) to distinguish logs, metrics and traces. This fills the unlinked Fall lecture without requiring an observability vendor stack.

For your own HW6 design, identify a user-visible symptom, an appropriate metric, a threshold/window and an alert action. Sketch a single DM from acceptance through notification attempt to outcome using request/message identifiers and timestamps. Explain what evidence distinguishes your service failing from the notifier failing; a 202 acceptance alone cannot establish delivery. Write which silent failures your public observation interface can and cannot detect. Never log the keyed NOTIFY_URL.

Done when the notes explain a telemetry-only request trace, a meaningful user-impact alert and at least one uncertainty; the actual implementation and alert demonstration remain learner work.

## LEC-24: Summary and What We Learned Together

Use the [official learning goals](https://github.com/CMU-17-214/f2026/blob/3f5235eb6a9c652823cb21167846f978eea66c7e/learninggoals.md), your six immutable assignment reviews and lab records. For verification, change/reuse, scale/operations, agent supervision, engineering memory and unfamiliar-code reasoning, point to one concrete personal artifact and one remaining weakness. Revisit one HW2 founding decision, its HW3/HW5 supersession and its HW6 operational consequence; keep the original ADR intact.

Done when each goal has evidence or a named gap, and the learner can explain one counterexample to an overly broad success claim without an agent.

## Lab 13 release design (not a ready starter)

At its queued refresh, prefer the actual official handout and repo. If absent, the preparation agent writes a labeled reconstructed three-milestone lab: (1) correlate a request with logs and a behavior-sensitive metric, (2) demonstrate an alert on a reproducible user-visible fault, (3) localize the failure and explain an observation blind spot. Reuse the learner’s HW6 artifacts or a minimal healthy local service; avoid a new billable stack. Freeze exact milestones and expected evidence before setup. Do not provide the fault diagnosis, instrumentation solution or private fault schedule in learner-facing instructions.
