# Spring 2026 cross-reference

All 25 linked public Spring lecture exports are retained and text-indexed. The table gives targeted comparisons actually inspected, not an assertion of exhaustive Spring slide review. Exact PDF page numbers are one-based; Google’s slide viewer may number slides differently. Other Spring decks remain catalogued for reference, not mandatory extra coursework.

| Fall unit | Exact Spring source | PDF pages / named section | Relevant explanation | Selection judgment |
|---|---|---|---|---|
| LEC-01 | [Intro, IDEs, Build Systems, CI, Libraries](https://docs.google.com/presentation/d/1U0qfmIeOkD6BGVgyaty5HmxcbqSBTjT9FT7t8sAxECg/edit?usp=sharing) | 24–38 | Requirements-to-code, quality attributes and the configurable-sort tradeoff | Fall supplies the agent-specific thesis; optional alternate design framing. |
| LEC-03 | [Testability](https://docs.google.com/presentation/d/1Mf46KEj-XPN08qRG2xjKrB2wzZrOwlsn4YjkWBBQdnU/edit?usp=sharing) | 8–10; 29–34; 40–42 | Responders/saboteurs, controllability/observability, substitution and dependency injection | Optional explanation if Fall Clock example is unclear; Spring Lab 7 defines doubles without requiring its exercise. |
| LEC-05–06 | [OO Analysis and UML](https://docs.google.com/presentation/d/10bsxafe_IYbS811YUQFcbFh1XQsjhCxLODgiY_xosfk/edit?usp=sharing) | 17–35 | Domain concepts/attributes, associations, multiplicities and composition | Optional diagram-reading prerequisite; Fall supplies ADR and durable-agent-context content. |
| LEC-07 | [Responsibility Assignment](https://docs.google.com/presentation/d/1TZ4_QRDg3VMI__uvTyfdRXfZPWWeiAXK9E_f-CB3WSg/edit?usp=sharing) | 59–72 | Controller, Information Expert and Creator with examples and tradeoffs | Optional deeper GRASP reading; do not implement Spring Santorini. |
| LEC-10 | [Inheritance and Delegation](https://docs.google.com/presentation/d/1S6J5aaNo8UydPikpECoZbJUJeriBo89RoxYv3GrW_eQ/edit?usp=sharing) | 15–34; 55–58 | LoggingList inheritance versus delegation and subtyping distinction | Conditional prerequisite when inheritance/composition is unfamiliar. |
| LEC-11 | [API Design](https://docs.google.com/presentation/d/1zp7MZu08Cx9dEm6T-PwnXqgy87UC8-yclEc-942huIM/edit?usp=sharing) | 5–16; 18–28; 35–46 | Hard-to-misuse API, requirements dialogue, naming, documentation and testing documentation | Optional reinforcement; Lab 6 already contains its early compatibility primer. |
| LEC-17 | [Concurrency and Hazards](https://docs.google.com/presentation/d/1--BO9HwGLfwnpdttSOSI_kRulmAsNQGzGVDTfGeqlK0/edit?usp=sharing) | 11–20; 36–42 | Shared mutable state, locks, safety/liveness and deadlock | Optional explanation of language-level hazards; Fall adds deterministic lab schedule and per-replica scope. |
| LEC-20 / LEC-23 | [DevOps](https://docs.google.com/presentation/d/142LnbouZQp9KrKxnd2P1rJStexp7Ho2I5HMo-42kqgY/edit?usp=sharing) | 47–60; 64–83 | Config/version control, containers, brief monitoring overview, experiments, canaries and flags | Fall L20 already teaches pipeline/rollout. Spring monitoring overview does not fully explain HW6 telemetry-only localization; use SRE Ch.6 for that gap. |
| LEC-21 | [Static & Dynamic Analyses](https://docs.google.com/presentation/d/1iQD9IO6CffsE37eEt9Q1CqGtl5a4blwO72Ljpeeg_o0/edit?usp=sharing) | 5–18; 31–47; 49–64 | Null/type examples, analyzer tree/rules, approximation and findings in review | Optional deeper mechanism explanation; Fall teaches current gates, baselines, suppressions, fuzzing and proof limitations. |
| LEC-22 | [Supply Chain Security](https://docs.google.com/presentation/d/1YoOMUDJGqPH7lUai7k1Q3NyLEe2X4vhGVYvr1_hjNAs/edit?usp=sharing) | 13; 21; 28–35; 46; 63–74 | Dependency isolation/abandonment, XZ, malicious packages and build-system attack surface | First CMU fallback for unlinked Fall unit; SLSA only deepens remaining provenance guarantees. |

The [concept map](concept-map.md) also maps each Fall lecture to its closest Spring topic, including Test Case Design, Refactoring and Anti-patterns, Libraries and Frameworks, Java Parallelism and Distributed Systems. Those are optional alternate readings, not claimed substitutes for the Fall agent-specific content. The public Spring handouts/assignments are preserved in course-materials/s2026.

Spring has no corresponding standalone agent-architecture, repo-supervision or engineering-memory unit. Fall L02/L06/L12–14 already explain those topics; no external replacement is justified merely by the course title.

## Retained lecture exports

| Spring schedule title | PDF pages | Public source |
|---|---:|---|
| Intro, IDEs, Build Systems, CI, Libraries | 68 | [Source](https://docs.google.com/presentation/d/1U0qfmIeOkD6BGVgyaty5HmxcbqSBTjT9FT7t8sAxECg/edit?usp=sharing) |
| OO basics, Dynamic dispatch, Encapsulation | 67 | [Source](https://docs.google.com/presentation/d/1sWLUaXcgR7-qcxlHuKNFYCjtZhXZPVMN64EOto_dTvk/edit?usp=sharing) |
| OO Analysis and UML | 59 | [Source](https://docs.google.com/presentation/d/10bsxafe_IYbS811YUQFcbFh1XQsjhCxLODgiY_xosfk/edit?usp=sharing) |
| Responsibility Assignment | 77 | [Source](https://docs.google.com/presentation/d/1TZ4_QRDg3VMI__uvTyfdRXfZPWWeiAXK9E_f-CB3WSg/edit?usp=sharing) |
| Inheritance and Delegation | 89 | [Source](https://docs.google.com/presentation/d/1S6J5aaNo8UydPikpECoZbJUJeriBo89RoxYv3GrW_eQ/edit?usp=sharing) |
| Design Patterns | 56 | [Source](https://docs.google.com/presentation/d/1j7jME89cDIFWRaUSsyaeLEmWyN91BoyV7xl1dvkw1Mo/edit?usp=sharing) |
| Design Practice | 33 | [Source](https://docs.google.com/presentation/d/1n6vHbUJ3KvN2VaApDFWtA_1EqsixtKOXjRj2lD3y7-o/edit?usp=sharing) |
| Refactoring and Anti-patterns | 68 | [Source](https://docs.google.com/presentation/d/1Bsh5GDdpP364Q4pQ1qfNkCiOjGqr2b0AOO1b61W-gU4/edit?usp=sharing) |
| Specifications and Unit Testing, Exceptions | 82 | [Source](https://docs.google.com/presentation/d/16oM13phJpG2aRg7BoA8wmk15ajg0wg06MhlNCWo78VU/edit?usp=sharing) |
| Test Case Design | 92 | [Source](https://docs.google.com/presentation/d/16yBPiNcjhJB9iYQA5b09ViOSllyOWBZBazVu2rnMlIQ/edit?usp=sharing) |
| Testability | 62 | [Source](https://docs.google.com/presentation/d/1Mf46KEj-XPN08qRG2xjKrB2wzZrOwlsn4YjkWBBQdnU/edit?usp=sharing) |
| Introduction to Concurrency | 64 | [Source](https://docs.google.com/presentation/d/1aFYWJ4QtANM2tWX1GtiIvT9L7rnw22Gbr7lfmLMPCdk/edit?usp=sharing) |
| Concurrency and Hazards | 71 | [Source](https://docs.google.com/presentation/d/1--BO9HwGLfwnpdttSOSI_kRulmAsNQGzGVDTfGeqlK0/edit?usp=sharing) |
| Java Parallelism | 37 | [Source](https://docs.google.com/presentation/d/14ASy4UV457jG7Cre1aAngkt_AHGQYT3vWbC0Ezxye2E/edit?usp=sharing) |
| Concurrency and Asynchrony in TypeScript | 70 | [Source](https://docs.google.com/presentation/d/1YUgVurfVymI_vfK3VP-uXVl_7vuBqn1PAGxl588NMTM/edit?usp=sharing) |
| Concurrency and Patterns | 107 | [Source](https://docs.google.com/presentation/d/1nkzV0PGuvGJyw83n7n3SlCuZS90lRDIKYHgs5Imwn7A/edit?usp=sharing) |
| GUIs | 75 | [Source](https://docs.google.com/presentation/d/1Q273J9GnuihOmkbCiiMlPHJrsIA1oyjMhhq-1yexBIY/edit?usp=sharing) |
| Libraries and Frameworks | 68 | [Source](https://docs.google.com/presentation/d/1JgJLly89jxganL_vthxo0R9HUcbTyea3yPRKjIShbRo/edit?usp=sharing) |
| API Design | 50 | [Source](https://docs.google.com/presentation/d/1zp7MZu08Cx9dEm6T-PwnXqgy87UC8-yclEc-942huIM/edit?usp=sharing) |
| API Design II | 50 | [Source](https://docs.google.com/presentation/d/1pS4GDqdAh6LLkPos4NxC2vPGl6MG0bdyB5C_vEYKQUg/edit?usp=sharing) |
| Supply Chain Security | 76 | [Source](https://docs.google.com/presentation/d/1YoOMUDJGqPH7lUai7k1Q3NyLEe2X4vhGVYvr1_hjNAs/edit?usp=sharing) |
| Distributed Systems: Designing for Robustness | 84 | [Source](https://docs.google.com/presentation/d/1rdvSOLc-snOvY_Do6kI8Vt4Sryo4CLeYaAgedfIMFO8/edit?usp=sharing) |
| DevOps | 84 | [Source](https://docs.google.com/presentation/d/142LnbouZQp9KrKxnd2P1rJStexp7Ho2I5HMo-42kqgY/edit?usp=sharing) |
| Static & Dynamic Analyses | 69 | [Source](https://docs.google.com/presentation/d/1iQD9IO6CffsE37eEt9Q1CqGtl5a4blwO72Ljpeeg_o0/edit?usp=sharing) |
| The Last One: Looking Back & Looking Forward | 248 | [Source](https://docs.google.com/presentation/d/1FptLpMefUQRSPE33cJczBuydqAeXq_AhljdFv7yoio8/edit?usp=sharing) |
