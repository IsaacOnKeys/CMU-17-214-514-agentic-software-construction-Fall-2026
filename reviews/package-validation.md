# Initial curriculum package validation

Checked 2026-11-23. This validates the curriculum package, not learner mastery or exercise runtime readiness.

## Deliverables

- `syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx`: 198 ordered rows, 107 separate JIT prompts, controlled statuses, a filterable Queue table, frozen header/columns, resource catalog and coverage sheet. The next action is **JIT-001: Check self-study prerequisites and progress conventions**.
- All 24 scheduled lecture topics, 13 labs, six assignment themes, five assignment checkpoints, two midterms and final assessment are mapped. The 51 original scheduled instructional/assessment events retain their relative Fall ordering.
- Individual prompts specify current-unit context, persistent inputs, trigger, steps, constraints, outputs, verification and blocker recovery. Provisioning, learning, review, correction and cleanup have explicit gates. Five provisioning/teardown pairs cover Lab4, HW2, the HW6 checkpoint, and both learner/assessor operating resources.
- Topic/prerequisite analysis, source/gap register, Spring cross-reference, static lab audit, assignment continuity and assessment policy are saved under curriculum/ and assessments/rubrics/.

## Checks and evidence

- Run `python tools/validate_package.py`; authoritative machine result: [structural-validation.json](structural-validation.json). It checks unique IDs/order, prior-only dependencies, required fields, one-to-one prompt/index/source/trigger/done criteria, all course units, official event ordering, gate placement, cloud pairs, workbook ZIP/table/freeze/status validation, local navigation and source hashes.
- [Effective link audit](../curriculum/link-audit-effective.json): **126/126 current public URLs** have successful actual HTTP observations. The original pass attempted 129 unique routes; seven GitHub file-view routes returned 503/timeouts. Seven verified same-commit raw-file alternatives replace them; three were already present elsewhere, leaving 126 unique current URLs. Original failures, successful alternatives and substitutions remain in link-audit.json, link-fallback-checks.json and source-link-overrides.json. Network observations are a point-in-time check, not an availability guarantee.
- All 21 published Fall PDFs (1,162 pages) were extracted and page-indexed. Review used page-indexed digests, targeted complete examples and 25 rendered contact sheets containing selected diagram/image/sparse slides from all decks. [Lecture analysis](../curriculum/lecture-review.md) states the text-led scope; no exhaustive visual or recorded-lecture review is claimed.
- All 25 linked Spring lecture exports were downloaded and text-indexed; [Spring inventory](../curriculum/spring-deck-inventory.json) includes source URLs, page counts and SHA256 hashes. [Spring cross-reference](../curriculum/spring-cross-reference.md) identifies targeted inspected sections. A failed supply-chain export succeeded on retry.
- Fourteen public source repository revisions and 751 tracked-file hashes are recorded and checked unchanged. [Starter static evidence](../curriculum/starter-static-audit.json) retains manifests/workflows without running tests. Lab4's Maven project is under service/, and its preflight command names that directory explicitly.
- The existing Spring folder/tracker was inspected read-only and remains ignored/preserved. No upstream source file was edited; source archives and local PDF analysis dependencies are ignored by the outer repository.

## Explicit limits and future gates

The pinned Fall snapshot has no linked PDFs for Supply Chain Security, Observability and Monitoring, or Summary and What We Learned Together, and no linked Lab13 handout/starter. Four individual refresh tasks precede those activities; clearly labeled reconstructed fallbacks are planned. Private assignment inputs, Canvas/Panopto instruction, original exam papers, hidden graders and the operational notifier were not recovered.

No learner unit is marked complete. No exercise dependencies were installed, starter-health tests run, assignment contract released, application implemented, GitHub fork/PR published, or AWS resource created. Analysis-only Python PDF packages were installed locally. Exercise preparation and technical readiness occur only at their queued JIT triggers. The workbook was programmatically opened and structurally checked with openpyxl; native Excel rendering and clicking links in the user's Excel UI were not exercised. Relative link targets were resolved from the workbook directory.

For HW6, the ≥3.5-hour operating block remains real future work. A separate assessor-operated service and retained timestamped record are prepared only when due; filesystem separation alone is not independent institutional assessment. No generated logs, elapsed runtime or official grade equivalence is claimed.
