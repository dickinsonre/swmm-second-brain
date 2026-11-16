#!/usr/bin/env python3
"""Build the wiki reader: one self-contained HTML page from index.md, log.md and wiki/.

    python3 tools/build_app.py            # writes build/swmm-second-brain.html and build/swmm-second-brain-artifact.html

The standalone file is a full HTML document (for Netlify). The artifact file is the same page
without <html>/<head>/<body>, for publishing as a Claude artifact. Needs the `markdown` package
(pip install markdown); everything else is the standard library. Run it after every ingest.
"""
import csv, datetime, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, RAW, WIKI, read, front_matter, walk, rel, wiki_pages
import markdown
import app_doc

REPO = 'https://github.com/dickinsonre/swmm-second-brain'
BLOB = REPO + '/blob/main/'
OUT = os.path.join(ROOT, 'build')
VIEWS = {'search', 'questions', 'review', 'about', 'doc', 'home'}


def page_id(path):
    r = rel(path)
    if r == 'index.md':
        return 'home'
    if r == 'log.md':
        return 'log'
    return os.path.splitext(os.path.basename(path))[0]


LIST = re.compile(r'^\s{0,3}([-*+]|\d+\.)\s')


def prepare(md):
    """Python-Markdown wants a blank line before a list or a table; the wiki often has none."""
    out, fence, prev = [], False, ''
    for line in md.split('\n'):
        if line.startswith('```'):
            fence = not fence
        if not fence and prev.strip() and (
                (LIST.match(line) and not LIST.match(prev) and not prev.startswith('    ')) or
                (line.startswith('|') and not prev.startswith('|'))):
            out.append('')
        out.append(line)
        prev = line
    return '\n'.join(out)


MD = markdown.Markdown(extensions=['tables', 'fenced_code', 'sane_lists'])


def render(md):
    MD.reset()
    return MD.convert(prepare(md))


def app_links(raw_path):
    """URLs on the `links:` line of an app summary's front matter, Netlify first."""
    try:
        fm_text = read(os.path.join(ROOT, raw_path)).split('\n---', 1)[0]
    except OSError:
        return []
    m = re.search(r'^links:\s*(.*)$', fm_text, re.M)
    if not m:
        return []
    urls = re.findall(r'https?://[^\s,}"\']+', m.group(1))
    urls = [u.rstrip('/') for u in urls if 'replit.internal' not in u]
    def rank(u):
        return (0 if 'netlify' in u else 1 if 'github.io' in u else 3 if 'github.com' in u else 2, u)
    seen, out = set(), []
    for u in sorted(urls, key=rank):
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def label(u):
    host = re.sub(r'^https?://', '', u).split('/')[0]
    if host.endswith('netlify.app'):
        return 'Netlify'
    if host.endswith('replit.app'):
        return 'Replit'
    if host == 'github.com':
        return 'GitHub'
    if host.endswith('github.io'):
        return 'GitHub Pages'
    if host == 'claude.ai':
        return 'Claude artifact'
    return host


def main():
    paths = wiki_pages()
    ids = {}
    for p in paths:
        i = page_id(p)
        assert i not in ids and i not in VIEWS - {'home'}, ('duplicate or reserved page id', i, p)
        ids[i] = p
    by_rel = {rel(p): page_id(p) for p in paths}

    pages, raw_of = {}, {}
    for p in paths:
        i = page_id(p)
        fm, body = front_matter(read(p))
        if i == 'home':
            fm, title = {'type': 'index'}, 'Index'
        elif i == 'log':
            fm, title = {'type': 'log'}, 'Log'
        else:
            title = fm.get('title', i)
        h = render(body)
        here = os.path.dirname(rel(p))

        def fix(m):
            href = html.unescape(m.group(1))
            if re.match(r'^(https?:|mailto:)', href):
                return '<a href="%s" target="_blank" rel="noopener">' % html.escape(href, True)
            if href.startswith('#'):
                return '<a href="%s">' % html.escape(href, True)
            target = os.path.normpath(os.path.join(here, href.split('#')[0])).replace(os.sep, '/')
            if target in by_rel:
                return '<a href="#%s" data-page="%s">' % (by_rel[target], by_rel[target])
            return '<a href="%s" target="_blank" rel="noopener">' % html.escape(BLOB + target, True)
        h = re.sub(r'<a href="([^"]*)">', fix, h)
        pg = {'id': i, 'title': title, 'type': fm.get('type', ''), 'path': rel(p), 'html': h,
              'out': sorted(set(re.findall(r'data-page="([^"]+)"', h)) - {i})}
        for k in ('updated', 'reviewed', 'changed_after_review', 'published', 'ingested', 'kind',
                  'author', 'raw', 'superseded_by', 'coverage'):
            if fm.get(k):
                pg[k] = fm[k]
        for k in ('sources', 'tags'):
            if isinstance(fm.get(k), list):
                pg[k] = fm[k]
        if pg.get('raw'):
            raw_of[i] = pg['raw']
            if pg['raw'].startswith('raw/apps/'):
                pg['apps'] = [[label(u), u] for u in app_links(pg['raw'])]
        pages[i] = pg

    # app links on entity pages: the source cited first in the page's opening paragraph
    sid = {re.match(r'(S\d+)-', i).group(1): i for i in pages if re.match(r'S\d+-', i)}
    for i, pg in pages.items():
        if pg['type'] == 'entity':
            m = re.search(r'data-page="(S\d+-[^"]+)"', pg['html'])
            if m and pages[m.group(1)].get('apps'):
                pg['apps'] = pages[m.group(1)]['apps']
                pg['appsFrom'] = m.group(1)
    back = {}
    for i, pg in pages.items():
        for o in pg['out']:
            back.setdefault(o, []).append(i)
    for i, pg in pages.items():
        pg['back'] = sorted(back.get(i, []))

    # index groups, in index.md order
    groups, cur, sub = [], None, None
    for line in read(os.path.join(ROOT, 'index.md')).split('\n'):
        if line.startswith('## '):
            cur = line[3:].strip()
            sub = None
            continue
        m = re.match(r'^- \[([^\]]+)\]\(([^)]+)\)(.*)$', line)
        if m and cur and cur != 'Queue':
            target = os.path.normpath(m.group(2)).replace(os.sep, '/')
            if target in by_rel:
                pid = by_rel[target]
                name = cur + (' / ' + sub if sub else '')
                if not groups or groups[-1][0] != name:
                    groups.append([name, []])
                label_ = pages[pid]['title'] if re.match(r'^S\d+$', m.group(1)) else m.group(1)
                groups[-1][1].append([pid, label_, m.group(3).lstrip(' :')])
        elif line.strip() and not line.startswith(('-', '#', '|')) and cur and len(line) < 60 and not line.endswith('.'):
            sub = line.strip()

    # open questions
    questions, section = [], ''
    oq = front_matter(read(os.path.join(WIKI, 'open-questions.md')))[1]
    for line in oq.split('\n'):
        if line.startswith('## '):
            section = line[3:].strip()
        m = re.match(r'^- \[( |x)\] (Q\d+) \(([\d-]+)\):\s*(.*)$', line)
        if m:
            h = render(m.group(4))

            def qfix(mm):
                href = html.unescape(mm.group(1))
                if re.match(r'^https?:', href):
                    return '<a href="%s" target="_blank" rel="noopener">' % html.escape(href, True)
                target = os.path.normpath(os.path.join('wiki', href.split('#')[0])).replace(os.sep, '/')
                if target in by_rel:
                    return '<a href="#%s" data-page="%s">' % (by_rel[target], by_rel[target])
                return '<a href="%s" target="_blank" rel="noopener">' % html.escape(BLOB + target, True)
            h = re.sub(r'<a href="([^"]*)">', qfix, h)
            questions.append({'id': m.group(2), 'done': m.group(1) == 'x', 'date': m.group(3), 'section': section, 'html': h})

    # counts from the manifest
    status = {}
    with open(os.path.join(RAW, 'MANIFEST.csv'), encoding='utf-8') as f:
        for row in csv.DictReader(f):
            status[row.get('status', '')] = status.get(row.get('status', ''), 0) + 1
    counts = {'raw': sum(status.values()), 'ingested': status.get('ingested', 0), 'queued': status.get('queued', 0),
              'pages': len(pages) - 2, 'sources': sum(1 for p in pages.values() if p['type'] == 'source'),
              'concepts': sum(1 for p in pages.values() if p['type'] == 'concept'),
              'entities': sum(1 for p in pages.values() if p['type'] == 'entity'),
              'open': sum(1 for q in questions if not q['done']), 'settled': sum(1 for q in questions if q['done']),
              'unreviewed': sum(1 for p in pages.values() if p.get('reviewed') == 'no'),
              'changed': sum(1 for p in pages.values() if p.get('changed_after_review'))}
    counts['questions'] = len(questions)
    counts['netlify'] = sum(1 for p in pages.values() if p['type'] == 'source' and any(l == 'Netlify' for l, _ in p.get('apps', [])))
    last = re.findall(r'^## \[([\d-]+)\] (\w+) \| (.*)$', read(os.path.join(ROOT, 'log.md')), re.M)
    built = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    here = os.path.dirname(os.path.abspath(__file__))
    tpl = read(os.path.join(here, 'app_template.html'))
    appmd_path = os.path.join(OUT, 'swmm-second-brain.md')
    appmd = read(appmd_path) if os.path.exists(appmd_path) else ''
    os.makedirs(OUT, exist_ok=True)
    counts['mb'] = '2.0'
    for _ in range(2):  # the second pass puts the real file size into the essay
        doc_html, _md = app_doc.build_doc(render, counts, pages, built, OUT)
        data = {'pages': pages, 'groups': groups, 'questions': questions, 'counts': counts, 'repo': REPO,
                'built': built, 'lastLog': [list(x) for x in last[-8:]][::-1], 'doc': doc_html}
        blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
        body = tpl.replace('/*__DATA__*/', blob).replace('/*__APPMD__*/', appmd.replace('</', '<\\/'))
        counts['mb'] = '%.1f' % (len(body.encode()) / 1e6)
    with open(os.path.join(OUT, 'swmm-second-brain-artifact.html'), 'w', encoding='utf-8') as f:
        f.write(body)
    full = ('<!doctype html>\n<html lang="en" data-theme="dark">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            '<meta name="color-scheme" content="dark light">\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
    with open(os.path.join(OUT, 'swmm-second-brain.html'), 'w', encoding='utf-8') as f:
        f.write(full)
    print('pages %d, questions %d, groups %d, %.1f MB' % (len(pages), len(questions), len(groups), len(full.encode()) / 1e6))


if __name__ == '__main__':
    main()
