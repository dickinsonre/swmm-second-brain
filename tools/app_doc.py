"""The Doc tab of the reader app: the essay in tools/app_doc.md with its figures.

Every figure is drawn here from numbers in the repository (the log, the manifest, the pages), once with
theme variables for the app and once with fixed light colours for the .docx. Used by build_app.py.
"""
import csv, json, os, re
from common import ROOT, RAW, read

APP = {'ink': 'var(--ink)', 'dim': 'var(--ink-dim)', 'faint': 'var(--ink-faint)', 'line': 'var(--line)',
       'card': 'var(--card)', 'field': 'var(--field)', 'head': 'var(--head)', 'accent': 'var(--accent)',
       'ok': 'var(--ok-ink)', 'okbg': 'var(--ok-bg)', 'hi': 'var(--hi-ink)', 'hibg': 'var(--hi-bg)',
       'warn': 'var(--warn-ink)', 'warnbg': 'var(--warn-bg)', 'panel': 'var(--panel)', 'panelline': 'var(--panel-line)',
       'font': 'Inter, system-ui, sans-serif', 'mono': 'JetBrains Mono, ui-monospace, monospace'}
DOCX = {'ink': '#1f2937', 'dim': '#4b5563', 'faint': '#6b7280', 'line': '#d1d5db', 'card': '#ffffff', 'field': '#f9fafb',
        'head': '#1e3a5f', 'accent': '#2563eb', 'ok': '#166534', 'okbg': '#f0fdf4', 'hi': '#c2410c', 'hibg': '#fff7ed',
        'warn': '#991b1b', 'warnbg': '#fef2f2', 'panel': '#eff6ff', 'panelline': '#bfdbfe',
        'font': 'Liberation Sans, Arial, sans-serif', 'mono': 'Liberation Mono, Courier New, monospace'}


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def svg(w, h, body, title, C):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-label="%s" '
            'style="max-width:100%%;height:auto;font-family:%s">%s</svg>') % (w, h, w, h, esc(title), C['font'], body)


def rect(x, y, w, h, C, fill='field', stroke='line', r=8, sw=1.2, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ''
    return '<rect x="%g" y="%g" width="%g" height="%g" rx="%g" style="fill:%s;stroke:%s;stroke-width:%g"%s/>' % (
        x, y, w, h, r, C[fill], C[stroke], sw, d)


def text(x, y, s, C, size=13, color='ink', weight=400, anchor='start', mono=False):
    fam = C['mono'] if mono else C['font']
    return '<text x="%g" y="%g" style="fill:%s;font-size:%gpx;font-weight:%d;font-family:%s" text-anchor="%s">%s</text>' % (
        x, y, C[color], size, weight, fam, anchor, esc(s))


def lines(x, y, rows, C, size=12.5, color='dim', gap=17, **k):
    return ''.join(text(x, y + i * gap, r, C, size, color, **k) for i, r in enumerate(rows))


def arrow(x1, y1, x2, y2, C, color='dim', label=None, dash=None):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 9 * math.cos(a), y2 - 9 * math.sin(a)
    p1 = (hx + 5 * math.sin(a), hy - 5 * math.cos(a))
    p2 = (hx - 5 * math.sin(a), hy + 5 * math.cos(a))
    d = ' stroke-dasharray="%s"' % dash if dash else ''
    s = '<line x1="%g" y1="%g" x2="%g" y2="%g" style="stroke:%s;stroke-width:1.6"%s/>' % (x1, y1, hx, hy, C[color], d)
    s += '<polygon points="%g,%g %g,%g %g,%g" style="fill:%s"/>' % (x2, y2, p1[0], p1[1], p2[0], p2[1], C[color])
    if label:
        s += text((x1 + x2) / 2, (y1 + y2) / 2 - 7, label, C, 11.5, color, 600, 'middle')
    return s


# ---------- figures ----------

def fig_layers(C, k):
    b = ''
    b += rect(250, 14, 260, 54, C, 'panel', 'panelline')
    b += text(380, 36, 'CLAUDE.md: the schema', C, 14, 'head', 700, 'middle')
    b += text(380, 55, 'how sources are read, cited and checked', C, 12, 'dim', 400, 'middle')
    b += rect(20, 110, 250, 170, C)
    b += text(36, 136, 'raw/', C, 16, 'head', 700, mono=True)
    b += lines(36, 160, ['sources, never edited', 'articles, app summaries, notes,', 'manuals, READMEs',
                         'MANIFEST.csv: a SHA-256 per file', '%s files, %s ingested' % (k['raw'], k['ingested'])], C)
    b += rect(490, 110, 250, 170, C)
    b += text(506, 136, 'wiki/', C, 16, 'head', 700, mono=True)
    b += lines(506, 160, ['%s source pages' % k['sources'], '%s concept pages, %s entity pages' % (k['concepts'], k['entities']),
                          'overview, open questions', 'index.md and log.md', 'every claim cites a source page'], C)
    b += arrow(272, 168, 486, 168, C, 'accent', 'ingest (the agent)')
    b += arrow(486, 226, 272, 226, C, 'faint', 'citations lead back', dash='5 4')
    b += arrow(330, 70, 160, 106, C, 'faint', dash='4 4') + arrow(430, 70, 610, 106, C, 'faint', dash='4 4')
    b += rect(490, 312, 250, 58, C, 'okbg', 'ok')
    b += text(506, 336, 'Bob reads a page', C, 13.5, 'ok', 700)
    b += text(506, 356, 'reviewed: no  becomes a date', C, 12, 'ok', 400, mono=True)
    b += arrow(615, 282, 615, 308, C, 'ok')
    b += rect(20, 312, 250, 58, C, 'hibg', 'hi')
    b += text(36, 336, 'This app', C, 13.5, 'hi', 700)
    b += text(36, 356, 'one HTML file built from wiki/', C, 12, 'hi', 400)
    b += arrow(488, 340, 274, 340, C, 'hi', 'build_app.py')
    return svg(760, 384, b, 'The three layers of the repository and the app', C)


def fig_ingest(C, k):
    steps = [('1', 'Read the whole source', ['never a title or', 'a summary']),
             ('2', 'Write the source page', ['S + number; the claims', 'worth keeping, with numbers']),
             ('3', 'Update other pages', ['usually five to fifteen;', 'dates and sources: lists']),
             ('4', 'Record disagreements', ['both sides cited; an', 'unticked open question']),
             ('5', 'Index and log', ['one line per page;', 'one entry per operation']),
             ('6', 'Manifest and lint', ['hashes checked;', 'zero errors to stop'])]
    b, w, h = '', 228, 96
    for i, (n, t, sub) in enumerate(steps):
        col, row = i % 3, i // 3
        x, y = 16 + col * 248, 16 + row * 130
        b += rect(x, y, w, h, C)
        b += '<circle cx="%g" cy="%g" r="13" style="fill:%s"/>' % (x + 24, y + 26, C['accent'])
        b += text(x + 24, y + 31, n, C, 13, 'card', 700, 'middle')
        b += text(x + 46, y + 31, t, C, 13.5, 'head', 700)
        b += lines(x + 16, y + 58, sub, C, 12)
        if col < 2:
            b += arrow(x + w + 2, y + h / 2, x + 246, y + h / 2, C, 'faint')
    b += arrow(16 + 2 * 248 + w / 2, 16 + h + 2, 16 + w / 2, 146 - 2, C, 'faint', dash='4 4')
    b += text(380, 268, 'A reply from Bob goes into raw/notes/ in his words first, then through the same six steps.', C, 12, 'dim', 400, 'middle')
    return svg(760, 280, b, 'The six steps of an ingest', C)


def fig_build(C, k):
    b = ''
    src = ['index.md', 'log.md', 'wiki/**/*.md', 'open-questions.md', 'raw/MANIFEST.csv', 'app summaries: links:']
    b += rect(14, 14, 190, 236, C)
    b += text(28, 38, 'The repository', C, 13.5, 'head', 700)
    b += lines(28, 64, src, C, 12, mono=True, gap=28)
    steps = ['front matter: title, type, dates', 'Markdown to HTML', 'rewrite every link', 'index groups for the rail',
             'open questions as a list', 'counts by status']
    b += rect(250, 14, 250, 236, C, 'panel', 'panelline')
    b += text(264, 38, 'tools/build_app.py', C, 13.5, 'head', 700, mono=True)
    b += lines(264, 64, steps, C, 12, gap=28)
    b += arrow(206, 132, 246, 132, C, 'accent')
    b += rect(546, 14, 200, 104, C, 'hibg', 'hi')
    b += text(560, 38, 'One HTML file', C, 13.5, 'hi', 700)
    b += lines(560, 62, ['template + one JSON block', '%s MB, no server' % k['mb'], 'Netlify copy and artifact copy'], C, 12, 'hi')
    b += arrow(502, 66, 542, 66, C, 'accent')
    views = ['Read', 'Search', 'Open questions', 'To review', 'About', 'Doc']
    for i, v in enumerate(views):
        x, y = 546 + (i % 2) * 102, 136 + (i // 2) * 38
        b += rect(x, y, 96, 30, C, 'field', 'line', 6)
        b += text(x + 48, y + 20, v, C, 12, 'ink', 600, 'middle')
    b += arrow(646, 120, 646, 132, C, 'faint')
    return svg(760, 264, b, 'What the build reads, what it does, and what comes out', C)


def fig_links(C, k):
    b = ''
    b += text(16, 24, 'Links: one rule for each kind', C, 13.5, 'head', 700)
    rows = [('../sources/S20-li-edition-54-two-solvers.md', '#S20-li-edition-54-two-solvers', 'a jump inside the app'),
            ('../../raw/apps/one-swmm.md', 'github.com/.../blob/main/raw/apps/one-swmm.md', 'opens the raw file on GitHub'),
            ('https://openswmm.org/...', 'unchanged', 'opens in a new tab')]
    for i, (a, z, why) in enumerate(rows):
        y = 44 + i * 46
        b += rect(16, y, 330, 34, C, 'field', 'line', 6)
        b += text(26, y + 22, a, C, 11.5, 'ink', 400, mono=True)
        b += arrow(350, y + 17, 384, y + 17, C, 'accent')
        b += rect(388, y, 356, 34, C, 'field', 'line', 6)
        b += text(398, y + 15, z, C, 11.5, 'ink', 400, mono=True)
        b += text(398, y + 29, why, C, 11, 'dim')
    y0 = 200
    b += text(16, y0, 'Search: how a page is scored', C, 13.5, 'head', 700)
    b += rect(16, y0 + 12, 728, 64, C, 'panel', 'panelline')
    b += text(380, y0 + 52, 'score  =  Σ over words w  of  ( nₑ + 20 · Tₑ )'.replace('ₑ', '_w'), C, 20, 'head', 700, 'middle', mono=True)
    b += text(110, y0 + 104, 'n_w : times the word appears in the page text', C, 12, 'dim')
    b += text(110, y0 + 122, 'T_w : 1 if the word is in the title, else 0', C, 12, 'dim')
    b += text(110, y0 + 140, 'a page counts only if every word has n_w + T_w > 0', C, 12, 'dim')
    return svg(760, 352, b, 'How links are rewritten and how search scores a page', C)


def growth_series():
    log = read(os.path.join(ROOT, 'log.md'))
    pts = []
    for m in re.finditer(r'^## \[([\d-]+)\][^\n]*\n(.*?)(?=^## \[|\Z)', log, re.M | re.S):
        body = m.group(2)
        g = (re.search(r'(\d+) raw files, (\d+) ingested', body) or re.search(r'Counts?: (\d+) of (\d+) raw files ingested', body))
        if not g:
            continue
        if 'raw files, ' in g.group(0):
            raw_, ing = int(g.group(1)), int(g.group(2))
        else:
            ing, raw_ = int(g.group(1)), int(g.group(2))
        pts.append((m.group(1), ing, raw_))
    return pts


def fig_growth(C, k):
    pts = growth_series()
    if len(pts) < 2:
        return ''
    W, H, L, R, T, B = 760, 300, 56, 20, 24, 50
    ymax = max(p[2] for p in pts)
    ymax = (ymax // 100 + 1) * 100
    n = len(pts)
    X = lambda i: L + (W - L - R) * i / (n - 1)
    Y = lambda v: T + (H - T - B) * (1 - v / ymax)
    b = rect(0.5, 0.5, W - 1, H - 1, C, 'card', 'line', 8)
    for v in range(0, ymax + 1, 100):
        b += '<line x1="%g" x2="%g" y1="%g" y2="%g" style="stroke:%s;stroke-width:1"/>' % (L, W - R, Y(v), Y(v), C['line'])
        b += text(L - 8, Y(v) + 4, v, C, 11, 'faint', 400, 'end')
    for name, idx, color in (('raw files', 2, 'faint'), ('ingested', 1, 'accent')):
        path = ' '.join('%s%.1f,%.1f' % ('M' if i == 0 else 'L', X(i), Y(p[idx])) for i, p in enumerate(pts))
        b += '<path d="%s" style="fill:none;stroke:%s;stroke-width:%s"/>' % (path, C[color], 2.6 if idx == 1 else 1.8)
        b += '<circle cx="%.1f" cy="%.1f" r="4" style="fill:%s"/>' % (X(n - 1), Y(pts[-1][idx]), C[color])
        b += text(X(n - 1) - 6, Y(pts[-1][idx]) - 9, '%s %d' % (name, pts[-1][idx]), C, 12, color, 700, 'end')
    first14 = [i for i, p in enumerate(pts) if p[0] == '2026-11-14']
    b += text(X(0), H - 28, '%d' % pts[0][1], C, 11, 'accent', 600, 'middle')
    b += text(L, H - 12, 'first logged count, %s' % pts[0][0], C, 11, 'faint')
    b += text(W - R, H - 12, 'log entries with counts: %d, newest at right' % n, C, 11, 'faint', 400, 'end')
    if first14:
        x = X(first14[-1])
        b += '<line x1="%g" x2="%g" y1="%g" y2="%g" style="stroke:%s;stroke-dasharray:3 4"/>' % (x, x, T, H - B, C['faint'])
        b += text(x + 4, T + 12, 'end of 14 Nov', C, 11, 'faint')
    return svg(W, H, b, 'Sources ingested and raw files held, entry by entry in the log', C)


def folder_counts():
    c = {}
    with open(os.path.join(RAW, 'MANIFEST.csv'), encoding='utf-8') as f:
        for r in csv.DictReader(f):
            fo = r['path'].split('/')[1]
            st = r['status'] if r['status'] in ('ingested', 'queued') else 'other'
            c.setdefault(fo, {'ingested': 0, 'queued': 0, 'other': 0})[st] += 1
    return sorted(c.items(), key=lambda x: -sum(x[1].values()))


def fig_folders(C, k):
    rows = folder_counts()
    W, L, R, rowh = 760, 120, 70, 30
    H = 40 + rowh * len(rows) + 30
    mx = max(sum(v.values()) for _, v in rows)
    sc = (W - L - R) / mx
    b = rect(0.5, 0.5, W - 1, H - 1, C, 'card', 'line', 8)
    for i, (fo, v) in enumerate(rows):
        y = 30 + i * rowh
        b += text(L - 10, y + 15, fo + '/', C, 12, 'ink', 600, 'end', mono=True)
        x = L
        for st, col in (('ingested', 'accent'), ('queued', 'hi'), ('other', 'faint')):
            if v[st]:
                w = v[st] * sc
                b += '<rect x="%g" y="%g" width="%g" height="18" style="fill:%s"/>' % (x, y + 2, max(w, 1.5), C[col])
                x += w
        b += text(x + 6, y + 15, '%d of %d' % (v['ingested'], sum(v.values())), C, 11.5, 'dim')
    y = H - 16
    for j, (lab, col) in enumerate((('ingested', 'accent'), ('queued', 'hi'), ('duplicate or superseded', 'faint'))):
        b += '<rect x="%g" y="%g" width="12" height="12" style="fill:%s"/>' % (L + j * 150, y - 10, C[col])
        b += text(L + j * 150 + 18, y, lab, C, 11.5, 'dim')
    return svg(W, H, b, 'Raw files by folder: ingested and queued', C)


def fig_review(C, k, pages):
    order = ['synthesis', 'concept', 'entity', 'source']
    c = {t: {'read': 0, 'changed': 0, 'unread': 0} for t in order}
    for p in pages.values():
        t = p.get('type')
        if t not in c:
            continue
        if p.get('reviewed') == 'no':
            c[t]['unread'] += 1
        elif p.get('changed_after_review'):
            c[t]['changed'] += 1
        else:
            c[t]['read'] += 1
    W, L, R, rowh = 760, 110, 230, 40
    H = 40 + rowh * len(order) + 34
    mx = max(sum(v.values()) for v in c.values())
    sc = (W - L - R) / mx
    b = rect(0.5, 0.5, W - 1, H - 1, C, 'card', 'line', 8)
    for i, t in enumerate(order):
        v = c[t]
        y = 30 + i * rowh
        b += text(L - 10, y + 18, t, C, 12.5, 'ink', 600, 'end')
        x = L
        for st, col in (('read', 'ok'), ('changed', 'warn'), ('unread', 'hi')):
            if v[st]:
                w = v[st] * sc
                b += '<rect x="%g" y="%g" width="%g" height="24" style="fill:%s"/>' % (x, y, max(w, 2), C[col])
                x += w
        b += text(x + 6, y + 17, '%d read, %d changed, %d unread' % (v['read'], v['changed'], v['unread']), C, 11.5, 'dim')
    y = H - 16
    for j, (lab, col) in enumerate((('read by Bob', 'ok'), ('changed after he read it', 'warn'), ('not yet read', 'hi'))):
        b += '<rect x="%g" y="%g" width="12" height="12" style="fill:%s"/>' % (L + j * 190, y - 10, C[col])
        b += text(L + j * 190 + 18, y, lab, C, 11.5, 'dim')
    return svg(W, H, b, 'Pages by type and whether Bob has read them', C)


CAPTIONS = {
    'layers': 'Sources go in once; the agent compiles them into cited pages; Bob reading a page is what turns it from a draft into the record.',
    'ingest': 'An ingest is the same six steps every time, and it does not stop until the linter reports zero errors.',
    'build': 'The build reads only what the repository holds and writes one file; nothing is fetched when the page opens.',
    'links': 'Every link is rewritten by kind, and search ranks a page first when the words are in its title.',
    'growth': 'Counts as the log recorded them after each operation. The raw files grow when Bob sends sources; the ingested line catches up in steps.',
    'folders': 'Measured from raw/MANIFEST.csv at build time. The app summaries are nearly all in; the LinkedIn articles and the EPA manuals wait.',
    'review': 'Counted from the reviewed: line of every page at build time. Most of the wiki is still the agent\'s reading.',
}


def figures(C, k, pages):
    return {'layers': fig_layers(C, k), 'ingest': fig_ingest(C, k), 'build': fig_build(C, k), 'links': fig_links(C, k),
            'growth': fig_growth(C, k), 'folders': fig_folders(C, k), 'review': fig_review(C, k, pages)}


def complexity_text():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app_complexity.json')
    if not os.path.exists(p):
        return 'Not measured yet with the SWMM App Complexity Meter.'
    d = json.loads(read(p))
    return d['text']


def build_doc(render, counts, pages, built, outdir):
    """Return (html for the Doc tab, markdown with numbers filled in). Writes light SVGs for the .docx to outdir/figs."""
    md = read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app_doc.md'))
    md = re.sub(r'\{\{c:(\w+)\}\}', lambda m: str(counts[m.group(1)]), md)
    md = md.replace('{{built}}', built).replace('{{complexity}}', complexity_text())
    figs_app = figures(APP, counts, pages)
    figs_doc = figures(DOCX, counts, pages)
    os.makedirs(os.path.join(outdir, 'figs'), exist_ok=True)
    for n, s in figs_doc.items():
        with open(os.path.join(outdir, 'figs', n + '.svg'), 'w', encoding='utf-8') as f:
            f.write(s)
    num = {}
    def sub_md(m):
        n = m.group(1)
        num[n] = len(num) + 1
        return '[[FIG %s]]' % n
    md_marked = re.sub(r'^\{\{fig:(\w+)\}\}$', sub_md, md, flags=re.M)
    with open(os.path.join(outdir, 'doc.md'), 'w', encoding='utf-8') as f:
        f.write(md_marked)
    with open(os.path.join(outdir, 'doc-captions.json'), 'w', encoding='utf-8') as f:
        json.dump({n: 'Figure %d. %s' % (i, CAPTIONS[n]) for n, i in num.items()}, f)
    h = render(md_marked)
    h = re.sub(r'<p>\[\[FIG (\w+)\]\]</p>', lambda m: '<figure class="fig">%s<figcaption>Figure %d. %s</figcaption></figure>' % (
        figs_app[m.group(1)], num[m.group(1)], esc(CAPTIONS[m.group(1)])), h)
    return h, md_marked
