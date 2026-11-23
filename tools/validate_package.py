"""Validate the execution queue and traceability, without running course exercises."""
from pathlib import Path
from urllib.parse import unquote,urldefrag
import hashlib
import json
import re
import zipfile
import subprocess
from openpyxl import load_workbook

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'syllabus/CMU-17-214-Fall-2026-Self-Study.xlsx'


def validate():
    issues=[];checks=[]
    def require(condition,message):
        if not condition:issues.append(message)
    wb=load_workbook(BOOK)
    ws=wb['Queue'];headers=[c.value for c in ws[1]]
    rows=[dict(zip(headers,values)) for values in ws.iter_rows(min_row=2,values_only=True)]
    ids=[r['ID'] for r in rows];positions={rid:i for i,rid in enumerate(ids)}
    require(len(ids)==len(set(ids)),'Duplicate queue ID')
    require([r['Order'] for r in rows]==list(range(1,len(rows)+1)),'Order is not unique sequential positions')
    for row in rows:
        for field in ['Activity type','Topic / action','Learning objective','Core resources','Trigger','Expected output','Done when','Status / Complete']:
            require(bool(row[field]),f'{row["ID"]} missing {field}')
        require(row['Status / Complete'] in ['Not started','Ready','In progress','Blocked','Complete'],f'{row["ID"]} has invalid status')
        for dep in (row['Dependencies'] or '').split(', '):
            if dep:require(dep in positions and positions.get(dep,99999)<positions[row['ID']],f'{row["ID"]} has non-prior dependency {dep}')
    checks.append(f'{len(rows)} unique ordered rows; prior-only dependencies form a DAG; required fields/statuses populated')
    jit=[r for r in rows if r['Activity type'].startswith('JIT')]
    prompt_paths=[]
    index=(ROOT/'prompts/INDEX.md').read_text(encoding='utf-8')
    for row in jit:
        path=(BOOK.parent/(row['Saved prompt'] or '')).resolve()
        require(path.is_file(),f'{row["ID"]} prompt link missing: {path}')
        prompt_paths.append(path)
        if not path.is_file():continue
        body=path.read_text(encoding='utf-8')
        for heading in ['## Role and context','## When to run','## Inputs','## Task','## Constraints','## Outputs and progress','## Verification and failure handling']:
            require(heading in body,f'{row["ID"]} prompt lacks {heading}')
        require(row['ID'] in body and row['ID'] in index and path.name in index,f'{row["ID"]} index/body identity mismatch')
        require(row['Core resources'] in body,f'{row["ID"]} prompt lacks its exact source')
        require(row['Trigger'] in body,f'{row["ID"]} trigger mismatch')
        require(row['Done when'] in body,f'{row["ID"]} verification mismatch')
    require(len(prompt_paths)==len(set(prompt_paths)),'JIT rows share prompt files')
    actual=set((ROOT/'prompts').glob('JIT-*.md'))
    require(actual==set(prompt_paths),'Orphan or unindexed JIT prompt')
    checks.append(f'{len(jit)} one-to-one JIT files, row/index links, sources, triggers and seven required prompt sections checked')
    for n in range(1,25):require(f'LEC-{n:02}' in ids,f'Lecture {n} omitted')
    for n in range(1,14):
        labid=f'LAB-{n:02}';require(labid in ids,f'Lab {n} omitted')
        prep=next((r for r in jit if r['Topic / action'].startswith(f'Prepare Lab {n:02}:')),None)
        preflight=next((r for r in jit if r['Topic / action']==f'Verify Lab {n:02} starter health'),None)
        review=next((r for r in jit if r['Topic / action']==f'Review Lab {n:02} milestones independently'),None)
        require(all([prep,preflight,review]),f'Lab {n} missing prepare/preflight/review')
        if all([prep,preflight,review]):require(positions[prep['ID']]<positions[preflight['ID']]<positions[labid]<positions[review['ID']]<positions[labid+'-CLOSE'],f'Lab {n} gates out of order')
    for n in range(1,7):
        target=f'HW-{n:02}-BUILD';require(target in ids,f'HW{n} implementation omitted')
        prep=next(r for r in jit if r['Topic / action'].startswith(f'Prepare and freeze Assignment {n:02}:'))
        assessor=next(r for r in jit if r['Topic / action']==f'Prepare independent Assignment {n:02} assessment controls')
        require(positions[prep['ID']]<positions[assessor['ID']]<positions[target],f'HW{n} release/assessment not before build')
        if n>1:require(f'HW-{n:02}-CHECKPOINT' in ids and positions[f'HW-{n:02}-CHECKPOINT-CLOSE']<positions[target],f'HW{n} lacks accepted checkpoint before completion')
    for eid in ('EXAM1','EXAM2','FINAL'):require(eid in ids and eid+'-CLOSE' in ids,f'{eid} assessment or review omitted')
    checks.append('24 lectures, 13 labs, six assignments, five checkpoints, two midterms/final and per-unit gates represented')
    # Compare the sequence of official scheduled activities, ignoring inserted JIT/supplement/correction rows.
    original=(ROOT/'course-materials/f2026/README.md').read_text(encoding='utf-8')
    expected=[]
    for date,topic in re.findall(r'<tr[^>]*>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>\s*</tr>',original,re.S):
        if 'slides/' in topic:
            m=re.search('slides/(\\d+)-',topic);expected.append(f'LEC-{int(m.group(1)):02}')
        elif 'Lab ' in topic:
            m=re.search(r'Lab (\d+)',topic)
            if m:expected.append(f'LAB-{int(m.group(1)):02}')
        elif 'Assignment ' in topic:
            m=re.search(r'Assignment (\d+)',topic)
            if m:expected.append(f'HW-{int(m.group(1)):02}-'+('CHECKPOINT' if 'Checkpoint' in topic else 'BUILD'))
        elif 'Supply Chain Security' in topic:expected.append('LEC-22')
        elif 'Observability and Monitoring' in topic:expected.append('LEC-23')
        elif 'Summary and What We Learned Together' in topic:expected.append('LEC-24')
        elif 'Midterm 1' in topic:expected.append('EXAM1')
        elif 'Midterm 2' in topic:expected.append('EXAM2')
        elif 'Final Exam' in topic:expected.append('FINAL')
    actual_sequence=[rid for rid in ids if rid in expected]
    require(actual_sequence==expected,'Scheduled core activity sequence differs from pinned Fall schedule')
    checks.append(f'{len(expected)} scheduled core events retain exact Fall ordering; inserted operational gates do not change their order')
    pairs=json.loads((ROOT/'curriculum/cloud-task-pairs.json').read_text())
    for pair in pairs:
        require(pair['provision'] in positions and pair['teardown'] in positions and positions[pair['provision']]<positions[pair['teardown']],f'Invalid cloud pair {pair}')
        pr=next(r for r in jit if r['ID']==pair['provision'])
        body=(BOOK.parent/pr['Saved prompt']).resolve().read_text(encoding='utf-8')
        require(pair['teardown'] in body,f'Cloud prompt missing exact teardown {pair}')
    checks.append(f'{len(pairs)} explicit provisioning/teardown pairs checked, including independent HW6 service')
    require(bool(ws.freeze_panes),'Queue header/columns not frozen')
    require('ExecutionQueue' in ws.tables,'Missing filterable Excel table')
    require(bool(ws.data_validations.dataValidation),'Missing status validation')
    require(ws.tables['ExecutionQueue'].ref==f'A1:O{len(rows)+1}','Excel table range mismatch')
    local_count=0
    for sheet in wb:
        for cells in sheet:
            for cell in cells:
                if not cell.hyperlink:continue
                link=cell.hyperlink.target
                if link.startswith(('https://','http://','#')):continue
                path=(BOOK.parent/unquote(urldefrag(link)[0])).resolve()
                require(path.is_file(),f'Broken workbook local hyperlink {sheet.title}!{cell.coordinate}: {link}')
                local_count+=1
    checks.append(f'Workbook ZIP reopens, Excel table/filter/freeze/status validation exist; {local_count} local hyperlinks resolve')
    with zipfile.ZipFile(BOOK) as archive:require(archive.testzip() is None,'Workbook ZIP CRC failure')
    # Markdown navigation links (not future output paths in code spans) must resolve now.
    md_count=0
    active=[ROOT/'README.md']
    for folder in ('curriculum','prompts','assessments/rubrics'):
        active+=list((ROOT/folder).glob('*.md'))
    for path in active:
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
            if target.startswith(('http://','https://','#')):continue
            rel=urldefrag(unquote(target))[0]
            require((path.parent/rel).resolve().exists(),f'Broken Markdown navigation {path.relative_to(ROOT)}: {target}')
            md_count+=1
    checks.append(f'{md_count} local Markdown navigation links resolve')
    manifest=json.loads((ROOT/'curriculum/source-manifest.json').read_text())
    verified=0
    for repo in manifest['repositories']:
        directory=ROOT/repo['path']
        sha=subprocess.check_output(['git','-C',str(directory),'rev-parse','HEAD'],text=True).strip()
        require(sha==repo['commit'],f'Archived source SHA changed: {repo["path"]}')
        for entry in repo['files']:
            path=directory/entry['path']
            require(path.exists() and hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256'],f'Archived source file changed: {path}')
            verified+=1
    checks.append(f'{len(manifest["repositories"])} source repository SHAs and {verified} tracked file hashes unchanged')
    extraction=json.loads((ROOT/'curriculum/pdf-extraction.json').read_text())
    require(len(extraction)==21,'Fall PDF extraction coverage mismatch')
    require(all(e['text_chars']>0 for e in extraction),'Empty lecture extraction')
    checks.append(f'21 Fall decks / {sum(x["pages"] for x in extraction)} pages extracted and inventoried; selected visual review is documented separately')
    report={'checked_on':'2026-11-23','ok':not issues,'queue_rows':len(rows),'jit_prompts':len(jit),'checks':checks,'errors':issues}
    (ROOT/'reviews').mkdir(exist_ok=True)
    (ROOT/'reviews/structural-validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
    return 1 if issues else 0


if __name__=='__main__':raise SystemExit(validate())
