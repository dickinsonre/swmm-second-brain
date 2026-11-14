#!/usr/bin/env python3
"""Convert a LinkedIn "Articles" data export into raw/linkedin/*.md.

Usage: python3 tools/li2md.py PATH/TO/Articles/Articles

Only published articles are converted. LinkedIn names a published article by
its URL slug and a draft by its creation time, so a file whose name starts
with a date is a draft and is skipped.

Each output file gets front matter (title, url, created, published, the
SHA-256 of the exported HTML) followed by the body converted with pandoc.
Files in raw/ are never edited after they are written; if LinkedIn's export
changes, rerun this script and commit the difference.
"""
import hashlib, os, re, subprocess, sys
from bs4 import BeautifulSoup

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw', 'linkedin')
os.makedirs(OUT, exist_ok=True)


def yq(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


n = skipped = 0
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith('.html'):
        continue
    if re.match(r'^\d{4}-\d\d-\d\d ', fn):
        skipped += 1
        continue
    raw = open(os.path.join(SRC, fn), 'rb').read()
    soup = BeautifulSoup(raw, 'html.parser')
    body = soup.body
    h1 = body.find('h1')
    title = h1.get_text(' ', strip=True) if h1 else fn
    a = h1.find('a') if h1 else None
    url = a['href'] if a and a.has_attr('href') else ''
    cr = body.find('p', class_='created')
    pu = body.find('p', class_='published')
    created = cr.get_text(strip=True).replace('Created on ', '') if cr else ''
    published = pu.get_text(strip=True).replace('Published on ', '') if pu else ''
    for t in ([h1, cr, pu] + body.find_all('iframe')):
        if t is not None:
            if t.name == 'iframe':
                src = t.get('src', '')
                m = re.search(r'originalUrl%2522%3A%2522(.*?)%2522', src)
                link = ''
                if m:
                    from urllib.parse import unquote
                    link = unquote(unquote(m.group(1)))
                p = soup.new_tag('p')
                p.string = ('[embedded link: ' + link + ']') if link else '[embedded item]'
                t.replace_with(p)
            else:
                t.decompose()
    html = str(body)
    md = subprocess.run(['pandoc', '-f', 'html', '-t', 'gfm-raw_html', '--wrap=none'],
                        input=html.encode(), capture_output=True, check=True).stdout.decode()
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    words = len(re.findall(r'\w+', md))
    slug = fn[:-5]
    date = (published or created)[:10]
    head = ['---', 'title: ' + yq(title), 'kind: linkedin-article', 'author: Robert Dickinson',
            'url: ' + url, 'created: ' + yq(created), 'published: ' + yq(published),
            'words: %d' % words, 'export_sha256: ' + hashlib.sha256(raw).hexdigest(), '---', '']
    with open(os.path.join(OUT, (date + '-' if date else '') + slug + '.md'), 'w') as f:
        f.write('\n'.join(head) + '# ' + title + '\n\n' + md + '\n')
    n += 1
print('converted', n, 'published articles; skipped', skipped, 'drafts')
