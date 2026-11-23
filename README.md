# CMU 17-214/514 Fall 2026 self-study reconstruction

Open [the Excel execution queue](syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx). The first unfinished row is the next action. There are no compulsory dates. Preparation, learning, independent verification, correction and cleanup are separate rows; use each JIT row’s saved prompt in a fresh working session.

1. Open the workbook’s Start sheet, then the Queue table. Inspect its first unfinished row and dependencies.
2. For a JIT row, follow Saved prompt, supply the listed paths/commits and execute only that operation. For a learning row, study or do the exercise yourself under the course’s supervision rules.
3. Record Status and Evidence in that same row. A blocked task gets a named recovery row/prompt before the dependent activity; do not skip it. Save pending row-ID updates if Excel locks the file.

The initial reconstruction plans the full course; it does not prepare every runtime, build every starter, solve exercises or deploy cloud resources upfront. Detailed assignment requirements and independent controls are released/frozen only when their prompts come due. The learner still has to complete every study and assessment activity.

- [Prompt index](prompts/INDEX.md): every saved JIT operation, trigger and expected output.
- [Concept/prerequisite map](curriculum/concept-map.md) and [lecture analysis](curriculum/lecture-review.md).
- [Source/gap register](curriculum/source-and-gap-register.md), [lab audit](curriculum/lab-audit.md), [assignment continuity](curriculum/assignment-continuity.md).
- [Reconstructed guides for unlinked units](curriculum/reconstructed-study-guides.md).
- [Assessment policy](assessments/rubrics/assessment-policy.md), [decisions](progress/decisions.md), [change log](progress/change-log.md).
- [Package validation](reviews/package-validation.md): checks actually performed, live-source limits and next action.

Original public materials remain unmodified in local `course-materials/f2026/`, `s2026/`, `spring-decks/` and `starters/`. These downloaded nested repositories, PDF text/previews and analysis dependencies are ignored by the outer git repo. [source-manifest.json](curriculum/source-manifest.json) records original commits and hashes; [spring-deck-downloads.json](curriculum/spring-deck-downloads.json) records export availability. Do not redistribute copied teaching resources without checking their licenses. Keep learner code in unit working repositories, not source archives. The existing Spring course folder and tracker remain unchanged.

All new guides, prompts, workbook ordering adaptations and replacement assessment designs are **reconstructed**. Public CMU handouts are the target, not evidence that private starters, recordings or hidden graders were recovered. Results are independent self-study evidence, not official CMU grades or equivalence.

Reproduce the package structure check with `python tools/validate_package.py`. Generation uses `tools/course_data.py` and `tools/build_package.py`; after learning starts, preserve workbook status/evidence and review changes by stable ID. Source downloads/review helpers require locally installed dependencies and network authorization; they never execute exercise preparation.
