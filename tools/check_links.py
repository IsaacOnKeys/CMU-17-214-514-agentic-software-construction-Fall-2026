"""Check public resource links; retain failures instead of hiding them."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urldefrag
import json
import re
import requests
ROOT=Path(__file__).resolve().parents[1]


def check(url):
    result={'url':url,'checked_on':'2026-11-23'}
    try:
        response=requests.get(url,timeout=(10,25),stream=True,headers={'User-Agent':'CMU-selfstudy-source-check/1.0'})
        result.update(status=response.status_code,final_url=response.url,ok=200<=response.status_code<300)
        result['content_type']=response.headers.get('Content-Type','')
        response.close()
    except requests.RequestException as exc:
        result.update(ok=False,error=type(exc).__name__)
    return result


if __name__=='__main__':
    urls={x['url'] for x in json.loads((ROOT/'curriculum/resource-catalog.json').read_text(encoding='utf-8'))}
    for path in list((ROOT/'prompts').glob('*.md'))+list((ROOT/'curriculum').glob('*.md'))+list((ROOT/'assessments/rubrics').glob('*.md')):
        urls.update(re.findall(r'https://[^\s)<>`"|]+',path.read_text(encoding='utf-8')))
    urls={urldefrag(u.rstrip('.,;'))[0] for u in urls}
    with ThreadPoolExecutor(max_workers=8) as pool:
        results=list(pool.map(check,sorted(urls)))
    failures=[r for r in results if not r['ok']]
    if failures:
        with ThreadPoolExecutor(max_workers=4) as pool:
            retries={r['url']:r for r in pool.map(check,[x['url'] for x in failures])}
        for i,r in enumerate(results):
            if r['url'] in retries:
                retried=retries[r['url']];retried['first_attempt']=r;results[i]=retried
    (ROOT/'curriculum/link-audit.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    print(json.dumps({'checked':len(results),'ok':sum(x['ok'] for x in results),'failures':[x for x in results if not x['ok']]}))
