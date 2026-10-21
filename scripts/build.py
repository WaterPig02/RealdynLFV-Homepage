"""Dependency-free, escaped static rendering; all URLs are explicit and reviewed."""
import json, html, pathlib, re
from urllib.parse import urlparse
ROOT = pathlib.Path(__file__).resolve().parents[1]
c = json.loads((ROOT/'content.json').read_text())
e = lambda s: html.escape(str(s), quote=True)
def link(url):
    if urlparse(url).scheme != 'https':
        raise ValueError('Resource links must use https')
    return e(url)
c['stats_html'] = ''.join(f'<div class="stat"><strong>{e(v)}</strong><span>{e(k)}</span></div>' for v,k in c['stats'])
c['resources_html'] = ''.join(f'<a class="resource" href="{link(r["url"])}">{e(r["label"])} <span>Available ↗</span></a>' if r['url'] else f'<div class="resource">{e(r["label"])}<span>{e(r["status"])}</span></div>' for r in c['resources'])
def media(g,i):
    if g['src']:
        p = pathlib.Path(g['src'])
        if p.is_absolute() or '..' in p.parts or not (ROOT/p).is_file() or not g['alt']: raise ValueError('Media needs a safe existing local file and alt text')
        visual = f'<img src="{e(g["src"])}" alt="{e(g["alt"])}" loading="lazy">'
    else:
        visual = f'<div class="placeholder" aria-hidden="true"><span class="frame-mark">{i+1:02}</span><span>REAL MEDIA PENDING</span></div>'
    return f'<figure>{visual}<figcaption><h3>{e(g["title"])}</h3><p>{e(g["spec"])}</p></figcaption></figure>'
c['gallery_html'] = ''.join(media(g,i) for i,g in enumerate(c['gallery']))
c['views_html'] = ''.join(f'<span class="view {"center" if i==12 else ""}">{"C" if i==12 else ""}</span>' for i in range(25))
c['authors_html'] = f'<p>{e(c["authors"])}</p>' if c['authors'] else ''
c['citation_html'] = f'<pre>{e(c["citation"])}</pre>' if c['citation'] else '<h3>Citation coming soon</h3><p>Verified publication metadata and BibTeX will be added here when available.</p>'
c['license_html'] = e(c['license'] or 'Dataset license to be confirmed.')
c['releases_html'] = ''.join(f'<li>{e(r["version"])} · <a href="{link(r["url"])}">{e(r["label"])}</a></li>' for r in c['releases'])
t = (ROOT/'template.html').read_text()
out = re.sub(r'{{(\w+)}}',lambda m: str(c[m[1]]) if m[1].endswith('_html') else e(c[m[1]]),t)
(ROOT/'index.html').write_text(out)
print('Built index.html')
