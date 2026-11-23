"""Match every currently linked URL to actual successful HTTP evidence."""
from pathlib import Path
from urllib.parse import urldefrag
import json
import re
from openpyxl import load_workbook

ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    observations=[]
    for name in ('link-audit.json','link-fallback-checks.json','link-additional-checks.json'):
        path=ROOT/'curriculum'/name
        if path.exists():observations+=json.loads(path.read_text(encoding='utf-8'))
    evidence={r['url']:r for r in observations if r['ok']}
    urls={r['url'] for r in json.loads((ROOT/'curriculum/resource-catalog.json').read_text(encoding='utf-8'))}
    docs=[ROOT/'README.md']
    for folder in ('curriculum','prompts','assessments/rubrics'):
        docs+=list((ROOT/folder).glob('*.md'))
    for path in docs:urls.update(re.findall(r'https://[^\s)<>`"|]+',path.read_text(encoding='utf-8')))
    wb=load_workbook(ROOT/'syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx')
    for sheet in wb:
        for row in sheet:
            for cell in row:
                if cell.hyperlink and cell.hyperlink.target.startswith('https://'):urls.add(cell.hyperlink.target)
    urls={urldefrag(u.rstrip('.,;'))[0] for u in urls}
    missing=sorted(urls-evidence.keys())
    report=dict(checked_on='2026-11-23',current_urls=len(urls),missing=missing,
                results=[evidence.get(u,dict(url=u,ok=False,error='No successful request')) for u in sorted(urls)])
    (ROOT/'curriculum/link-audit-effective.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(dict(current_urls=len(urls),verified=len(urls)-len(missing),missing=missing)))
    raise SystemExit(bool(missing))
