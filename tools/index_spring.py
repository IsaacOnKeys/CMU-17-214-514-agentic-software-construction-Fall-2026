"""Inventory public Spring exports and retain precise targeted cross-references."""
from pathlib import Path
from urllib.parse import urlsplit
import hashlib
import json
import re
from build_package import ROOT, SPRING_DECKS, write

# PDF page numbers were checked against retained text; this does not claim exhaustive Spring review.
TARGETS=[
 ('LEC-01','Intro, IDEs, Build Systems, CI, Libraries','24–38','Requirements-to-code, quality attributes and the configurable-sort tradeoff','Fall supplies the agent-specific thesis; optional alternate design framing.'),
 ('LEC-03','Testability','8–10; 29–34; 40–42','Responders/saboteurs, controllability/observability, substitution and dependency injection','Optional explanation if Fall Clock example is unclear; Spring Lab 7 defines doubles without requiring its exercise.'),
 ('LEC-05–06','OO Analysis and UML','17–35','Domain concepts/attributes, associations, multiplicities and composition','Optional diagram-reading prerequisite; Fall supplies ADR and durable-agent-context content.'),
 ('LEC-07','Responsibility Assignment','59–72','Controller, Information Expert and Creator with examples and tradeoffs','Optional deeper GRASP reading; do not implement Spring Santorini.'),
 ('LEC-10','Inheritance and Delegation','15–34; 55–58','LoggingList inheritance versus delegation and subtyping distinction','Conditional prerequisite when inheritance/composition is unfamiliar.'),
 ('LEC-11','API Design','5–16; 18–28; 35–46','Hard-to-misuse API, requirements dialogue, naming, documentation and testing documentation','Optional reinforcement; Lab 6 already contains its early compatibility primer.'),
 ('LEC-17','Concurrency and Hazards','11–20; 36–42','Shared mutable state, locks, safety/liveness and deadlock','Optional explanation of language-level hazards; Fall adds deterministic lab schedule and per-replica scope.'),
 ('LEC-20 / LEC-23','DevOps','47–60; 64–83','Config/version control, containers, brief monitoring overview, experiments, canaries and flags','Fall L20 already teaches pipeline/rollout. Spring monitoring overview does not fully explain HW6 telemetry-only localization; use SRE Ch.6 for that gap.'),
 ('LEC-21','Static & Dynamic Analyses','5–18; 31–47; 49–64','Null/type examples, analyzer tree/rules, approximation and findings in review','Optional deeper mechanism explanation; Fall teaches current gates, baselines, suppressions, fuzzing and proof limitations.'),
 ('LEC-22','Supply Chain Security','13; 21; 28–35; 46; 63–74','Dependency isolation/abandonment, XZ, malicious packages and build-system attack surface','First CMU fallback for unlinked Fall unit; SLSA only deepens remaining provenance guarantees.'),
]

if __name__=='__main__':
    downloads=json.loads((ROOT/'curriculum/spring-deck-downloads.json').read_text(encoding='utf-8'))
    records=[]
    for title,url in SPRING_DECKS.items():
        deck_id=re.search(r'/d/([^/]+)',url).group(1)
        item=next(x for x in downloads if f'/d/{deck_id}/' in x['url'])
        txt=ROOT/'curriculum/pdf-text/spring'/f'{deck_id}.txt'
        path=ROOT/item['path'] if item['downloaded'] else None
        records.append(dict(title=title,url=url,path=item.get('path'),downloaded=item['downloaded'],
                            pdf_pages=len(re.findall('=== PAGE ',txt.read_text(encoding='utf-8'))) if txt.exists() else None,
                            sha256=hashlib.sha256(path.read_bytes()).hexdigest() if path else None))
    write('curriculum/spring-deck-inventory.json',json.dumps(records,indent=2))
    lines=['# Spring 2026 cross-reference','',
           'All 25 linked public Spring lecture exports are retained and text-indexed. The table gives targeted comparisons actually inspected, not an assertion of exhaustive Spring slide review. Exact PDF page numbers are one-based; Google’s slide viewer may number slides differently. Other Spring decks remain catalogued for reference, not mandatory extra coursework.','',
           '| Fall unit | Exact Spring source | PDF pages / named section | Relevant explanation | Selection judgment |',
           '|---|---|---|---|---|']
    for fall,title,pages,content,judgment in TARGETS:
        lines.append(f'| {fall} | [{title}]({SPRING_DECKS[title]}) | {pages} | {content} | {judgment} |')
    lines+=['','The [concept map](concept-map.md) also maps each Fall lecture to its closest Spring topic, including Test Case Design, Refactoring and Anti-patterns, Libraries and Frameworks, Java Parallelism and Distributed Systems. Those are optional alternate readings, not claimed substitutes for the Fall agent-specific content. The public Spring handouts/assignments are preserved in course-materials/s2026.','',
            'Spring has no corresponding standalone agent-architecture, repo-supervision or engineering-memory unit. Fall L02/L06/L12–14 already explain those topics; no external replacement is justified merely by the course title.','',
            '## Retained lecture exports','',
            '| Spring schedule title | PDF pages | Public source |','|---|---:|---|']
    for r in records:lines.append(f'| {r["title"]} | {r["pdf_pages"] or "Unavailable"} | [Source]({r["url"]}) |')
    write('curriculum/spring-cross-reference.md','\n'.join(lines))
    print(json.dumps({'spring_decks':len(records),'downloaded':sum(r['downloaded'] for r in records),'targeted_sections':len(TARGETS)}))
