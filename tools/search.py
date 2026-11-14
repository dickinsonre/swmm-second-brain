#!/usr/bin/env python3
"""Rank wiki pages and raw files against a query (BM25, standard library).

  python3 tools/search.py "preissmann slot"          wiki first, then raw
  python3 tools/search.py --wiki "subcatchment width"
  python3 tools/search.py --raw -n 20 "manhole loads infosewer"

Read index.md first; use this when the index is not enough.
"""
import math, os, re, sys
from common import RAW, WIKI, read, walk, rel, front_matter

args = sys.argv[1:]
n = 10
if '-n' in args:
    i = args.index('-n'); n = int(args[i + 1]); del args[i:i + 2]
scope = [x for x in ('--wiki', '--raw') if x in args] or ['--wiki', '--raw']
query = ' '.join(a for a in args if not a.startswith('--'))
if not query:
    sys.exit(__doc__)
tok = lambda s: re.findall(r'[a-z0-9_]+', s.lower())
q = tok(query)


def rank(files):
    docs = []
    for p in files:
        t = read(p)
        fm, body = front_matter(t)
        h = re.search(r'^#\s+(.+)$', body, re.M)
        title = fm.get('title') or fm.get('name') or (h.group(1) if h else os.path.basename(p))
        words = tok(title) * 5 + tok(body)
        docs.append((p, title, body, words))
    if not docs:
        return []
    N = len(docs)
    avg = sum(len(d[3]) for d in docs) / N
    df = {w: sum(1 for d in docs if w in set(d[3])) for w in set(q)}
    out = []
    for p, title, body, words in docs:
        s = 0.0
        for w in q:
            f = words.count(w)
            if not f:
                continue
            idf = math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5))
            s += idf * f * 2.2 / (f + 1.2 * (0.25 + 0.75 * len(words) / avg))
        if s > 0:
            m = re.search('|'.join(re.escape(w) for w in q), body, re.I)
            a = max(0, (m.start() if m else 0) - 70)
            out.append((s, p, title, ' '.join(body[a:a + 200].split())))
    return sorted(out, reverse=True)[:n]


for flag, top, exts in (('--wiki', WIKI, ('.md',)), ('--raw', RAW, ('.md', '.txt', '.json'))):
    if flag not in scope:
        continue
    print('==', flag[2:], '==')
    for s, p, title, snip in rank(walk(top, exts)):
        print('%6.2f  %s\n        %s\n        ...%s...' % (s, rel(p), title[:100], snip))
