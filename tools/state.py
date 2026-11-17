#!/usr/bin/env python3
"""Keep the counts in README.md and index.md current. Standard library only.

  python3 tools/state.py           # rewrite every <!-- state:KEY -->...<!-- /state:KEY --> span
  python3 tools/state.py --check   # print the stale spans and exit 1; change nothing

The counts come from raw/MANIFEST.csv, the wiki pages' front matter and
wiki/open-questions.md, so they say what the files say on the day it runs.
The date is the date of the newest entry in log.md.
"""
import csv, os, re, sys
from common import ROOT, WIKI, read, front_matter, rel, wiki_pages

TARGETS = [os.path.join(ROOT, 'README.md'), os.path.join(ROOT, 'index.md')]
SPAN = re.compile(r'<!-- state:([a-z_]+) -->(.*?)<!-- /state:\1 -->', re.S)


def n(x):
    return '{:,}'.format(x)


def counts():
    rows = list(csv.DictReader(open(os.path.join(ROOT, 'raw', 'MANIFEST.csv'), encoding='utf-8')))
    status = {}
    for r in rows:
        status[r['status']] = status.get(r['status'], 0) + 1
    raw_words = sum(int(r['words'] or 0) for r in rows)
    by_type, wiki_words, unreviewed, changed, partial = {}, 0, 0, 0, []
    for p in wiki_pages():
        if rel(p) in ('index.md', 'log.md'):
            continue
        t = read(p)
        fm, body = front_matter(t)
        ty = fm.get('type', '?')
        by_type[ty] = by_type.get(ty, 0) + 1
        wiki_words += len(body.split())
        if fm.get('reviewed', 'no') == 'no':
            unreviewed += 1
        elif fm.get('changed_after_review'):
            changed += 1
        if ty == 'source' and fm.get('coverage') == 'partial':
            partial.append(fm.get('title', rel(p)))
    concepts = len([p for p in wiki_pages() if rel(p).startswith('wiki/concepts/')])
    entities = len([p for p in wiki_pages() if rel(p).startswith('wiki/entities/')])
    oq = read(os.path.join(WIKI, 'open-questions.md'))
    q_open = len(re.findall(r'^- \[ \] Q\d+', oq, re.M))
    q_done = len(re.findall(r'^- \[x\] Q\d+', oq, re.M))
    dates = re.findall(r'^## \[(\d{4}-\d{2}-\d{2})\]', read(os.path.join(ROOT, 'log.md')), re.M)
    return dict(raw=len(rows), raw_words=raw_words, ingested=status.get('ingested', 0),
                queued=status.get('queued', 0), skipped=len(rows) - status.get('ingested', 0) - status.get('queued', 0),
                pages=sum(by_type.values()), sources=by_type.get('source', 0), concepts=concepts,
                entities=entities, synth=by_type.get('synthesis', 0), wiki_words=wiki_words,
                unreviewed=unreviewed, changed=changed, partial=len(partial),
                q_open=q_open, q_done=q_done, date=max(dates) if dates else '')


def render(c):
    def about(w):
        return 'about ' + n(int(round(w, -3)))
    return {
        'raw_files': '%s files, %s words' % (n(c['raw']), about(c['raw_words'])),
        'wiki_pages': '%s pages, %s words: %s sources, %s concepts, %s entities and %s synthesis pages (the overview, the open-questions list and the start-here guide)' % (
            n(c['pages']), about(c['wiki_words']), n(c['sources']), n(c['concepts']), n(c['entities']), n(c['synth'])),
        'date': c['date'],
        'ingested': '%s of %s raw files ingested, %s of them in part; %s queued; %s superseded or duplicate' % (
            n(c['ingested']), n(c['raw']), c['partial'], n(c['queued']), n(c['skipped'])),
        'oq': '%s open and %s settled' % (c['q_open'], c['q_done']),
        'review': '%s pages say `reviewed: no` and %s carry `changed_after_review:`' % (c['unreviewed'], c['changed']),
    }


def main():
    vals = render(counts())
    stale = []
    for path in TARGETS:
        t = read(path)
        def sub(m):
            key, old = m.group(1), m.group(2)
            if key not in vals:
                sys.exit('%s: unknown state key %s' % (rel(path), key))
            if old != vals[key]:
                stale.append('%s: %s says "%s", the files say "%s"' % (rel(path), key, old, vals[key]))
            return '<!-- state:%s -->%s<!-- /state:%s -->' % (key, vals[key], key)
        new = SPAN.sub(sub, t)
        if '--check' not in sys.argv and new != t:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new)
    if '--check' in sys.argv:
        for s in stale:
            print(s)
        sys.exit(1 if stale else 0)
    print('state: %d span(s) updated' % len(stale) if stale else 'state: all counts current')


if __name__ == '__main__':
    main()
