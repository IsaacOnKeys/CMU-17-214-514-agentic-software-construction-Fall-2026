"""Read-only source collection and reproducible inventory; never prepares exercises."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import subprocess
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'curriculum'


def collect_spring_deck(url):
    deck_id = re.search(r'/presentation/d/([^/]+)', url).group(1)
    target = ROOT / 'course-materials/spring-decks' / f'{deck_id}.pdf'
    target.parent.mkdir(parents=True, exist_ok=True)
    export = f'https://docs.google.com/presentation/d/{deck_id}/export/pdf'
    try:
        response = requests.get(export, timeout=45)
        valid = response.status_code == 200 and response.content.startswith(b'%PDF')
        if valid:
            target.write_bytes(response.content)
        return dict(url=url, export=export, status=response.status_code,
                    downloaded=valid, path=target.relative_to(ROOT).as_posix() if valid else None)
    except requests.RequestException as exc:
        return dict(url=url, export=export, downloaded=False, error=type(exc).__name__)


def inventory():
    records = []
    for directory in sorted((ROOT / 'course-materials').glob('*')):
        if not (directory / '.git').exists():
            continue
        sha = subprocess.check_output(['git', '-C', str(directory), 'rev-parse', 'HEAD'], text=True).strip()
        origin = subprocess.check_output(['git', '-C', str(directory), 'remote', 'get-url', 'origin'], text=True).strip()
        files = subprocess.check_output(['git', '-C', str(directory), 'ls-files'], text=True).splitlines()
        records.append(dict(path=directory.relative_to(ROOT).as_posix(), origin=origin, commit=sha,
                            files=[dict(path=f, sha256=hashlib.sha256((directory / f).read_bytes()).hexdigest()) for f in files]))
    for directory in sorted((ROOT / 'course-materials/starters').glob('*')):
        if (directory / '.git').exists():
            sha = subprocess.check_output(['git', '-C', str(directory), 'rev-parse', 'HEAD'], text=True).strip()
            origin = subprocess.check_output(['git', '-C', str(directory), 'remote', 'get-url', 'origin'], text=True).strip()
            files = subprocess.check_output(['git', '-C', str(directory), 'ls-files'], text=True).splitlines()
            records.append(dict(path=directory.relative_to(ROOT).as_posix(), origin=origin, commit=sha,
                                files=[dict(path=f, sha256=hashlib.sha256((directory / f).read_bytes()).hexdigest()) for f in files]))
    (OUT / 'source-manifest.json').write_text(json.dumps({'checked_on': '2026-11-23', 'repositories': records}, indent=2), encoding='utf-8')


if __name__ == '__main__':
    text = (ROOT / 'course-materials/s2026/README.md').read_text(encoding='utf-8')
    links = sorted(set(re.findall(r'https://docs.google.com/presentation/d/[^\s)"<>]+', text)))
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(collect_spring_deck, links))
    (OUT / 'spring-deck-downloads.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
    inventory()
    print(json.dumps({'spring_decks': len(results), 'downloaded': sum(r['downloaded'] for r in results)}))
