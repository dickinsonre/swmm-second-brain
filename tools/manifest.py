#!/usr/bin/env python3
"""Rebuild raw/MANIFEST.csv: one row per raw file.

Columns: path, kind, date, title, words, sha256, status, source_page.
status is `ingested` when a page in wiki/sources/ names the file in its
`raw:` front matter, otherwise `queued`. Run after adding raw files and
after every ingest. `--check` compares hashes with the existing manifest
and reports raw files that changed (raw files are never edited).
"""
import csv, os, re, sys
from common import RAW, WIKI, ROOT, read, front_matter, sha256, walk, rel

MAN = os.path.join(RAW, 'MANIFEST.csv')


def describe(path):
    kind = rel(path).split('/')[1]
    title, date, words = os.path.basename(path), '', ''
    if path.lower().endswith(('.md', '.txt', '.csv', '.json')):
        text = read(path)
        words = len(re.findall(r'\w+', text))
        fm, body = front_matter(text)
        title = fm.get('title') or fm.get('name') or ''
        if not title:
            m = re.search(r'^#\s+(.+)$', body, re.M)
            title = m.group(1).strip() if m else next((l.strip() for l in body.split('\n') if l.strip()), os.path.basename(path))[:120]
        date = (fm.get('published') or fm.get('date') or fm.get('created') or '')[:10]
        if not date:
            m = re.search(r'(\d{4}-\d\d-\d\d)', os.path.basename(path))
            date = m.group(1) if m else ''
    return kind, date, title, words


def main():
    ingested = {}
    for p in walk(os.path.join(WIKI, 'sources'), ('.md',)):
        fm, _ = front_matter(read(p))
        if fm.get('raw'):
            ingested[fm['raw']] = rel(p)
    old = {}
    if os.path.exists(MAN):
        with open(MAN, newline='', encoding='utf-8') as f:
            old = {r['path']: r for r in csv.DictReader(f)}
    rows, changed = [], []
    for p in walk(RAW):
        r = rel(p)
        if r == 'raw/MANIFEST.csv':
            continue
        kind, date, title, words = describe(p)
        h = sha256(p)
        if r in old and old[r]['sha256'] != h:
            changed.append(r)
        rows.append({'path': r, 'kind': kind, 'date': date, 'title': title, 'words': words, 'sha256': h,
                     'status': 'ingested' if r in ingested else 'queued', 'source_page': ingested.get(r, '')})
    missing = [r for r in ingested if not os.path.exists(os.path.join(ROOT, r))]
    if '--check' in sys.argv:
        for r in changed:
            print('CHANGED raw file (raw is immutable):', r)
        for r in missing:
            print('MISSING raw file named by a source page:', r)
        new = [x['path'] for x in rows if x['path'] not in old]
        for r in new:
            print('NEW raw file not yet in the manifest:', r)
        sys.exit(1 if (changed or missing) else 0)
    with open(MAN, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['path', 'kind', 'date', 'title', 'words', 'sha256', 'status', 'source_page'])
        w.writeheader()
        w.writerows(rows)
    n = sum(1 for x in rows if x['status'] == 'ingested')
    print('manifest: %d raw files, %d ingested, %d queued' % (len(rows), n, len(rows) - n))
    for r in changed:
        print('WARNING changed since last manifest:', r)


if __name__ == '__main__':
    main()
