"""Retain complete page text, page coverage evidence, and diagram contact sheets."""
from pathlib import Path
import sys
import json
import re
import html
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / '.tools/pylibs'), str(ROOT / '.tools/render')]
from pypdf import PdfReader

def extract(path, destination):
    reader = PdfReader(path)
    pages = [page.extract_text() or '' for page in reader.pages]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text('\n\n'.join(f'=== PAGE {i} ===\n{text}' for i, text in enumerate(pages, 1)), encoding='utf-8')
    return pages

if __name__ == '__main__':
    index = []
    lines = ['# Fall lecture page index', '',
             'Reconstructed extraction index, not official lecture prose. Page numbers are PDF pages (1-based).', '',
             'Full extracted text is retained locally in `curriculum/pdf-text/`; source PDFs are unmodified.', '',
             '| Deck | PDF page | Text characters | Opening text (index only) |', '|---|---:|---:|---|']
    for path in sorted((ROOT / 'course-materials/f2026/slides').glob('*.pdf')):
        pages = extract(path, ROOT / 'curriculum/pdf-text' / f'{path.stem}.txt')
        index.append(dict(file=path.name, pages=len(pages), text_chars=sum(map(len, pages)),
                          sparse_pages=[i for i, text in enumerate(pages, 1) if len(text.strip()) < 140]))
        for i, text in enumerate(pages, 1):
            opening = re.sub(r'\s+', ' ', text).strip()[:160].replace('|', '\\|')
            link = f'https://raw.githubusercontent.com/CMU-17-214/f2026/3f5235eb6a9c652823cb21167846f978eea66c7e/slides/{path.name}#page={i}'
            lines.append(f'| [{path.stem}]({link}) | {i} | {len(text)} | {opening} |')
    (ROOT / 'curriculum/lecture-page-index.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    (ROOT / 'curriculum/pdf-extraction.json').write_text(json.dumps(index, indent=2), encoding='utf-8')
    downloads = ROOT / 'curriculum/spring-deck-downloads.json'
    if downloads.exists():
        for entry in json.loads(downloads.read_text(encoding='utf-8')):
            if entry['downloaded']:
                extract(ROOT / entry['path'], ROOT / 'curriculum/pdf-text/spring' / (Path(entry['path']).stem+'.txt'))
    # Inspect diagrams and image-only slides without reproducing them in learner materials.
    import fitz
    dest = ROOT / 'curriculum/pdf-previews'
    dest.mkdir(exist_ok=True)
    for path in sorted((ROOT / 'course-materials/f2026/slides').glob('*.pdf')):
        doc = fitz.open(path)
        pages = [i for i in range(len(doc)) if len(doc[i].get_text().strip()) < 140]
        pages = sorted(set(pages + [min(len(doc)-1, p) for p in [10, 22, 30, 36]]))
        sheet = fitz.open()
        for start in range(0, len(pages), 12):
            page = sheet.new_page(width=1200, height=920)
            for j, n in enumerate(pages[start:start+12]):
                col, row = j % 3, j // 3
                rect = fitz.Rect(col*400, row*230+16, (col+1)*400, (row+1)*230)
                page.show_pdf_page(rect, doc, n)
                page.insert_text((col*400+4,row*230+12), f'{path.stem} / p{n+1}', fontsize=9)
        for i, page in enumerate(sheet):
            page.get_pixmap().save(dest / f'{path.stem}-{i+1}.png')
    print(json.dumps({'decks':len(index), 'pages':sum(x['pages'] for x in index), 'previews':len(list(dest.glob('*.png')))}))
