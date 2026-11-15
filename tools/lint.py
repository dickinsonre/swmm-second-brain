#!/usr/bin/env python3
"""Mechanical health check of the wiki. Run: python3 tools/lint.py

Errors (exit 1): broken links, missing front matter, a wiki page that cites
no source page, a source page whose raw file is missing, a raw file whose
hash changed, a page missing from index.md.
Warnings: orphan pages, em dashes, an app whose newest summary is not the
one ingested. Also reports pages not yet reviewed and open questions.

This finds structural faults only. Contradictions between sources, stale
claims and missing concept pages need a reader: see "Lint" in CLAUDE.md.
"""
import csv, os, re, sys
from urllib.parse import unquote
from common import ROOT, RAW, WIKI, read, front_matter, sha256, walk, rel, wiki_pages, links

errors, warns = [], []
pages = wiki_pages()
texts = {p: read(p) for p in pages}
inbound = {p: set() for p in pages}
index_path = os.path.join(ROOT, 'index.md')
REQUIRED = {'source': ['title', 'type', 'raw', 'ingested', 'reviewed'],
            'concept': ['title', 'type', 'updated', 'sources', 'reviewed'],
            'entity': ['title', 'type', 'updated', 'sources', 'reviewed'],
            'synthesis': ['title', 'type', 'updated', 'reviewed']}
unreviewed = 0
rereview = []
partial = []
for p, t in texts.items():
    r = rel(p)
    fm, body = front_matter(t)
    special = r in ('index.md', 'log.md')
    if not special:
        ty = fm.get('type')
        if ty not in REQUIRED:
            errors.append('%s: front matter `type` must be one of %s' % (r, sorted(REQUIRED)))
        else:
            for k in REQUIRED[ty]:
                if k not in fm:
                    errors.append('%s: front matter lacks `%s`' % (r, k))
            if ty == 'source' and fm.get('raw') and not os.path.exists(os.path.join(ROOT, fm['raw'])):
                errors.append('%s: raw file not found: %s' % (r, fm['raw']))
            if fm.get('reviewed', 'no') == 'no':
                unreviewed += 1
            elif fm.get('changed_after_review'):       # the agent added to a page Bob had already read
                rereview.append(r)
            if ty == 'source' and fm.get('coverage') == 'partial':
                partial.append(r)
    cites = 0
    for text, target in links(body):
        if re.match(r'^[a-z][a-z0-9+.-]*:', target) or target.startswith('#'):
            continue
        path = os.path.normpath(os.path.join(os.path.dirname(p), unquote(target.split('#')[0])))   # %20 in a link is a space in the file name
        if not os.path.exists(path):
            errors.append('%s: broken link -> %s' % (r, target))
            continue
        if path in inbound and path != p:
            inbound[path].add(p)
        if rel(path).startswith('wiki/sources/') or rel(path).startswith('raw/'):
            cites += 1
    if not special and fm.get('type') in ('concept', 'entity') and cites == 0:
        errors.append('%s: cites no source page' % r)
    if not special and '—' in body:
        warns.append('%s: contains an em dash (house style: none)' % r)

index_links = set()
if os.path.exists(index_path):
    for _, target in links(texts[index_path]):
        index_links.add(os.path.normpath(os.path.join(ROOT, target.split('#')[0])))
else:
    errors.append('index.md is missing')
for p in pages:
    r = rel(p)
    if r in ('index.md', 'log.md'):
        continue
    if p not in index_links:
        errors.append('%s: not listed in index.md' % r)
    if not [q for q in inbound[p] if rel(q) not in ('index.md', 'log.md')]:
        warns.append('%s: orphan (no other wiki page links to it)' % r)

man = os.path.join(RAW, 'MANIFEST.csv')
queued = ingested = 0
other, apps = {}, {}
if os.path.exists(man):
    with open(man, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            fp = os.path.join(ROOT, row['path'])
            if not os.path.exists(fp):
                errors.append('manifest names a raw file that is gone: ' + row['path'])
            elif sha256(fp) != row['sha256']:
                errors.append('raw file changed after it was recorded: ' + row['path'])
            ingested += row['status'] == 'ingested'
            queued += row['status'] == 'queued'
            other[row['status']] = other.get(row['status'], 0) + 1
            if row.get('app'):
                apps.setdefault(row['app'], []).append(row)
    for app, items in apps.items():
        if any(x['status'] == 'ingested' for x in items) and any(x['status'] == 'queued' for x in items):
            warns.append('app %s: a newer summary is queued while an older one is ingested; ingest it and mark the old source page superseded' % app)
    listed = set()
    with open(man, newline='', encoding='utf-8') as f:
        listed = {row['path'] for row in csv.DictReader(f)}
    for p in walk(RAW):
        if rel(p) != 'raw/MANIFEST.csv' and rel(p) not in listed:
            warns.append('raw file not in the manifest (run tools/manifest.py): ' + rel(p))
else:
    errors.append('raw/MANIFEST.csv is missing (run tools/manifest.py)')

oq = os.path.join(WIKI, 'open-questions.md')
open_q = len(re.findall(r'^- \[ \]', read(oq), re.M)) if os.path.exists(oq) else 0

types = {}
for p, t in texts.items():
    ty = front_matter(t)[0].get('type', 'special')
    types[ty] = types.get(ty, 0) + 1
print('pages:', ', '.join('%s %d' % kv for kv in sorted(types.items())))
print('raw files: %d ingested, %d queued' % (ingested, queued) + ''.join(', %d %s' % (v, k) for k, v in sorted(other.items()) if k not in ('ingested', 'queued')))
print('open questions: %d   pages not yet reviewed by Bob: %d' % (open_q, unreviewed))
if rereview:
    print('pages changed after Bob reviewed them: %d (%s)' % (len(rereview), ', '.join(os.path.basename(x)[:-3] for x in sorted(rereview))))
if partial:
    print('long documents read in part: %d (%s)' % (len(partial), ', '.join(os.path.basename(x)[:3] for x in partial)))
for w in warns:
    print('WARN ', w)
for e in errors:
    print('ERROR', e)
print('%d errors, %d warnings' % (len(errors), len(warns)))
sys.exit(1 if errors else 0)
