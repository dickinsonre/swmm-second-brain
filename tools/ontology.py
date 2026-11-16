"""Build the wiki's typed relations into RDF.

Reads the vocabulary (prefixes, relations with what they may connect, classes, qualifiers)
from ONTOLOGY.md and the **Relations** table of every wiki page, checks them, and writes into ontology/:
  second-brain.trig    RDF in TriG: vocabulary and labels in the default graph,
                       one named graph per source page holding the statements that cite it
  second-brain.jsonld  the same as JSON-LD
  relations.csv        one row per statement, with its qualifiers (condition, tested_on, as_of, verification)
  graph.md             the statements as a Mermaid diagram (GitHub draws it)

  python3 tools/ontology.py           # build (standard library only)
  python3 tools/ontology.py --check   # also parse the output with rdflib and run ontology/queries/*.rq

tools/lint.py imports collect() and reports its errors.
"""
import csv, io, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, WIKI, front_matter, read, rel, walk, ai_drafted

OUT = os.path.join(ROOT, 'ontology')
PAGE_BASE = 'https://github.com/dickinsonre/swmm-second-brain/blob/main/'
STD = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'owl': 'http://www.w3.org/2002/07/owl#',
    'xsd': 'http://www.w3.org/2001/XMLSchema#',
    'skos': 'http://www.w3.org/2004/02/skos/core#',
    'prov': 'http://www.w3.org/ns/prov#',
    'dcterms': 'http://purl.org/dc/terms/',
}
ID = re.compile(r'^([a-z][a-z0-9-]*):([A-Za-z0-9_.\-]+)$')
CODE = re.compile(r'`([^`]+)`')
QUAL = re.compile(r'`([a-z_]+): ([^`]*)`')   # a qualifier: a space after the colon tells it from a term ID
MDLINK = re.compile(r'\[([^\]]*)\]\(([^)\s]+)\)')


def table_rows(text, after):
    """Rows (lists of cells) of the first markdown table that follows the line `after`."""
    lines = text.split('\n')
    try:
        i = next(k for k, l in enumerate(lines) if l.strip() == after)
    except StopIteration:
        return None
    rows, started = [], False
    for l in lines[i + 1:]:
        s = l.strip()
        if s.startswith('|'):
            started = True
            cells = [c.strip() for c in s.strip('|').split('|')]
            if all(re.fullmatch(r':?-{3,}:?', c) for c in cells if c):
                continue
            rows.append(cells)
        elif started:
            break
        elif s and not s.startswith('#'):
            continue
    return rows


def vocabulary():
    """Prefixes, relations, classes, qualifiers and verification values, from ONTOLOGY.md."""
    text = read(os.path.join(ROOT, 'ONTOLOGY.md'))
    sections, cur, fence = {}, None, False
    for l in text.split('\n'):
        if l.startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        if l.startswith('## '):
            cur = l[3:].strip()
            sections[cur] = []
        elif cur:
            sections[cur].append(l)

    def tables(start):
        """Every table in the first section whose title starts with `start`, header rows dropped."""
        name = next((k for k in sections if k.startswith(start)), None)
        out, t = [], None
        for l in sections.get(name, []):
            st = l.strip()
            if st.startswith('|'):
                if t is None:
                    t = []
                    out.append(t)
                if not re.fullmatch(r'\|[\s|:-]+\|', st):
                    t.append([c.strip() for c in st.strip('|').split('|')])
            else:
                t = None
        return [x[1:] for x in out]

    def rows(start, k=0):
        t = tables(start)
        return t[k] if len(t) > k else []

    def must(cell):
        """A class the term must be declared, 'same', or None for anything."""
        c = CODE.findall(cell)
        if c:
            return c[0]
        return 'same' if cell.strip().lower() == 'same' else None

    prefixes = {}
    for r in rows('Prefixes'):
        p = CODE.findall(r[0])
        if p:
            prefixes[p[0]] = r[1]
    relations = {}
    for r in rows('Relations'):
        name = CODE.findall(r[0])
        std = CODE.findall(r[2]) if len(r) > 2 else []
        if name:
            relations[name[0]] = {'means': r[1], 'std': std[0] if std else None,
                                  'domain': must(r[3]) if len(r) > 3 else None,
                                  'range': must(r[4]) if len(r) > 4 else None}
    classes = {}
    for r in rows('Classes'):
        c = CODE.findall(r[0])
        if c:
            classes[c[0]] = r[1]
    qualifiers = {}
    for r in rows('Qualifiers'):
        k, prop = CODE.findall(r[0]), CODE.findall(r[1])
        if k and prop:
            qualifiers[k[0]] = {'prop': prop[0], 'holds': r[2]}
    verification = {}
    for r in rows('Qualifiers', 1):
        v = CODE.findall(r[0])
        if v:
            verification[v[0]] = r[1]
    return prefixes, relations, classes, qualifiers, verification


def page_id(path):
    return os.path.splitext(os.path.basename(path))[0]


def collect():
    """Return (statements, vocabulary, sources_meta, errors)."""
    vocab = vocabulary()
    prefixes, relations, classes, qualifiers, verification = vocab
    statements, errors, sources_meta = [], [], {}
    pages = walk(WIKI, ('.md',))
    by_id = {page_id(p): p for p in pages}
    for p in pages:
        fm, body = front_matter(read(p))
        if fm.get('type') == 'source':
            sources_meta[page_id(p).split('-')[0]] = {'path': rel(p), 'fm': fm}
    for p in pages:
        text = read(p)
        rows = table_rows(text, '**Relations**')
        if rows is None:
            continue
        r = rel(p)
        if not rows or [c.lower() for c in rows[0][:5]] != ['subject', 'relation', 'object', 'note', 'source']:
            errors.append('%s: the Relations table must have the columns Subject | Relation | Object | Note | Source' % r)
            continue
        for n, cells in enumerate(rows[1:], 2):
            where = '%s: Relations row %d' % (r, n)
            if len(cells) != 5:
                errors.append(where + ': needs 5 cells')
                continue
            subj, relc, obj, note, src = cells
            rname = CODE.findall(relc)
            if len(rname) != 1 or rname[0] not in relations:
                errors.append(where + ': unknown relation %r (see ONTOLOGY.md)' % relc)
                continue
            rname = rname[0]

            def terms(cell, side):
                out = []
                for code in CODE.findall(cell):
                    m = ID.match(code)
                    if not m:
                        errors.append('%s: %s %r is not prefix:Name' % (where, side, code))
                    elif m.group(1) not in prefixes:
                        errors.append('%s: %s %r has an unknown prefix' % (where, side, code))
                    else:
                        out.append(('term', code))
                for _, target in MDLINK.findall(cell):
                    t = os.path.normpath(os.path.join(os.path.dirname(p), target.split('#')[0]))
                    if not t.startswith(WIKI) or not os.path.exists(t):
                        errors.append('%s: %s link %s is not a wiki page' % (where, side, target))
                    else:
                        out.append(('page', rel(t)))
                if not out:
                    errors.append('%s: %s is empty' % (where, side))
                return out

            ss, oo = terms(subj, 'subject'), terms(obj, 'object')
            quals = {}
            for k, v in QUAL.findall(note):
                if k not in qualifiers:
                    errors.append('%s: unknown qualifier %r (see ONTOLOGY.md, Qualifiers)' % (where, k))
                elif k in quals:
                    errors.append('%s: qualifier %r given twice' % (where, k))
                else:
                    quals[k] = v.strip()
            for code in CODE.findall(note):
                m = ID.match(code)
                if m and m.group(1) in qualifiers:
                    errors.append('%s: write the qualifier as `%s: %s`, with a space after the colon' % (where, m.group(1), m.group(2)))
            if 'verification' in quals and quals['verification'] not in verification:
                errors.append('%s: verification %r is not one of %s' % (where, quals['verification'], ', '.join(verification)))
            comment = re.sub(r'\s+', ' ', QUAL.sub('', note)).strip()
            cites = sorted({os.path.basename(t).split('-')[0] for _, t in MDLINK.findall(src) if re.match(r'S\d+', os.path.basename(t))})
            cites = [c for c in cites if c in sources_meta]
            if not cites:
                errors.append(where + ': cites no source page')
                continue
            if rname == 'is_a':
                for kind, o in oo:
                    if kind != 'term' or o not in classes:
                        errors.append('%s: is_a object %r is not a class in ONTOLOGY.md' % (where, o))
            for s in ss:
                for o in oo:
                    statements.append({'s': s, 'p': rname, 'o': o, 'note': note, 'comment': comment,
                                       'quals': quals, 'sources': cites, 'page': r, 'where': where})
    errors.extend(check_classes(statements, relations))
    return statements, vocab, sources_meta, errors


def check_classes(statements, relations):
    """What each relation can connect: the Subject must be / Object must be columns of ONTOLOGY.md."""
    cls, errors = {}, []
    for st in statements:
        if st['p'] == 'is_a' and st['o'][0] == 'term':
            cls.setdefault(st['s'][1], set()).add(st['o'][1])
    have = lambda n: cls.get(n[1], set()) if n[0] == 'term' else set()
    said = lambda h: 'is ' + ', '.join('`%s`' % c for c in sorted(h)) if h else 'has no is_a row'
    for st in statements:
        d = relations[st['p']]
        rel_ = '`%s`' % st['p']
        for side, role, need in (('s', 'a subject', d['domain']), ('o', 'an object', d['range'])):
            if need and need != 'same' and need not in have(st[side]):
                errors.append('%s: %s needs %s of class `%s`; `%s` %s' % (
                    st['where'], rel_, role, need, st[side][1], said(have(st[side]))))
        if 'same' in (d['domain'], d['range']):
            hs, ho = have(st['s']), have(st['o'])
            if not hs or not ho:
                errors.append('%s: %s connects terms of the same class, and `%s` needs an is_a row' % (
                    st['where'], rel_, (st['s'] if not hs else st['o'])[1]))
            elif not hs & ho:
                errors.append('%s: %s connects terms of the same class; `%s` is %s and `%s` is %s' % (
                    st['where'], rel_, st['s'][1], ', '.join('`%s`' % c for c in sorted(hs)), st['o'][1], ', '.join('`%s`' % c for c in sorted(ho))))
    return errors


def iri(node, prefixes):
    kind, v = node
    if kind == 'page':
        return PAGE_BASE + v
    pre, local = v.split(':', 1)
    if pre in STD:
        return STD[pre] + local
    return prefixes[pre] + local


def label(node):
    kind, v = node
    if kind == 'page':
        return None
    local = v.split(':', 1)[1]
    if v.startswith(('qty:', 'sb:')):
        return re.sub(r'(?<=[a-z0-9])(?=[A-Z])', ' ', local).capitalize()
    if v.startswith('ruby:'):
        return 'Ruby ' + local
    if v.startswith('icm:') and re.match(r'\d', local):
        return 'ICM ' + local
    return local


def esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')


def build(statements, vocab, sources_meta):
    prefixes, relations, classes, qualifiers, verification = vocab
    SB = prefixes['sb']
    P = lambda name: STD['rdf'] + 'type' if name == 'is_a' else SB + name
    terms = {}
    for st in statements:
        for side in ('s', 'o'):
            n = st[side]
            if n[0] == 'term':
                terms.setdefault(n[1], set()).add(st['page'])
    # default graph: vocabulary, classes, term labels, source metadata
    default = []
    default.append((SB, STD['rdf'] + 'type', ('iri', STD['owl'] + 'Ontology')))
    default.append((SB, STD['rdfs'] + 'label', ('lit', 'SWMM Second Brain ontology (draft)')))
    default.append((SB, STD['rdfs'] + 'seeAlso', ('iri', PAGE_BASE + 'ONTOLOGY.md')))
    for name, d in relations.items():
        if name == 'is_a':
            continue
        default.append((SB + name, STD['rdf'] + 'type', ('iri', STD['rdf'] + 'Property')))
        default.append((SB + name, STD['rdfs'] + 'label', ('lit', name.replace('_', ' '))))
        default.append((SB + name, STD['rdfs'] + 'comment', ('lit', d['means'])))
        if d['std']:
            pre, local = d['std'].split(':', 1)
            default.append((SB + name, STD['rdfs'] + 'subPropertyOf', ('iri', STD[pre] + local)))
    for k, q in qualifiers.items():
        qi = iri(('term', q['prop']), prefixes)
        default.append((qi, STD['rdf'] + 'type', ('iri', STD['rdf'] + 'Property')))
        default.append((qi, STD['rdfs'] + 'label', ('lit', k.replace('_', ' '))))
        holds = q['holds'] + ('; one of: ' + ', '.join('%s (%s)' % kv for kv in verification.items()) if k == 'verification' else '')
        default.append((qi, STD['rdfs'] + 'comment', ('lit', holds)))
        default.append((qi, STD['rdfs'] + 'domain', ('iri', STD['rdf'] + 'Statement')))
    for c, means in classes.items():
        ci = iri(('term', c), prefixes)
        default.append((ci, STD['rdf'] + 'type', ('iri', STD['rdfs'] + 'Class')))
        default.append((ci, STD['rdfs'] + 'label', ('lit', label(('term', c)))))
        default.append((ci, STD['rdfs'] + 'comment', ('lit', means)))
    for t, pages in sorted(terms.items()):
        if t in classes:
            continue
        ti = iri(('term', t), prefixes)
        default.append((ti, STD['rdfs'] + 'label', ('lit', label(('term', t)))))
        for pg in sorted(pages):
            default.append((ti, STD['rdfs'] + 'isDefinedBy', ('iri', PAGE_BASE + pg)))
    used = sorted({s for st in statements for s in st['sources']}, key=lambda x: int(x[1:]))
    for sid in used:
        m = sources_meta[sid]
        g = PAGE_BASE + m['path']
        fm = m['fm']
        default.append((g, STD['rdf'] + 'type', ('iri', STD['prov'] + 'Entity')))
        default.append((g, STD['dcterms'] + 'identifier', ('lit', sid)))
        for key, pred in (('title', STD['dcterms'] + 'title'), ('published', STD['dcterms'] + 'date'),
                          ('author', STD['dcterms'] + 'creator'), ('kind', SB + 'sourceKind')):
            if fm.get(key):
                default.append((g, pred, ('lit', str(fm[key]))))
        # always present, so a query never has to guess what a missing line means
        default.append((g, SB + 'draftedBy', ('lit', str(fm.get('drafted_by') or 'unknown'))))
        default.append((g, SB + 'aiDrafted', ('lit', ai_drafted(fm.get('drafted_by')))))
        default.append((g, SB + 'reviewed', ('lit', str(fm.get('reviewed') or 'unknown'))))
    # named graphs: one per source
    graphs = {}
    for st in statements:
        s_iri, o_iri = iri(st['s'], prefixes), iri(st['o'], prefixes)
        for sid in st['sources']:
            g = PAGE_BASE + sources_meta[sid]['path']
            graphs.setdefault(g, [])
            trip = (s_iri, P(st['p']), ('iri', o_iri))
            if trip not in graphs[g]:
                graphs[g].append(trip)
            if st['comment'] or st['quals']:
                quals = tuple((iri(('term', qualifiers[k]['prop']), prefixes), st['quals'][k])
                              for k in qualifiers if k in st['quals'])
                bnode = ('note', s_iri, P(st['p']), o_iri, st['comment'], quals)
                if bnode not in graphs[g]:
                    graphs[g].append(bnode)
    return default, graphs


def term_ttl(x):
    return '<%s>' % x


def obj_ttl(o):
    kind, v = o
    return '<%s>' % v if kind == 'iri' else '"%s"' % esc(v)


def write_trig(default, graphs):
    out = io.StringIO()
    out.write('# SWMM Second Brain ontology (draft). Built by tools/ontology.py from ONTOLOGY.md and the Relations tables of the wiki pages.\n')
    out.write('# Default graph: vocabulary, classes, labels, source metadata. Each named graph is one source page and holds the statements that cite it.\n\n')
    for s, p, o in default:
        out.write('%s %s %s .\n' % (term_ttl(s), term_ttl(p), obj_ttl(o)))
    for g in sorted(graphs):
        out.write('\n%s {\n' % term_ttl(g))
        for item in graphs[g]:
            if item[0] == 'note':
                _, s, p, o, note, quals = item
                parts = ['<%stype> <%sStatement>' % (STD['rdf'], STD['rdf']), '<%ssubject> <%s>' % (STD['rdf'], s),
                         '<%spredicate> <%s>' % (STD['rdf'], p), '<%sobject> <%s>' % (STD['rdf'], o)]
                parts += ['<%s> "%s"' % (qp, esc(qv)) for qp, qv in quals]
                if note:
                    parts.append('<%scomment> "%s"' % (STD['rdfs'], esc(note)))
                out.write('  [] ' + ' ;\n     '.join(parts) + ' .\n')
            else:
                s, p, o = item
                out.write('  %s %s %s .\n' % (term_ttl(s), term_ttl(p), obj_ttl(o)))
        out.write('}\n')
    return out.getvalue()


def write_jsonld(default, graphs):
    def node_list(triples):
        nodes, notes = {}, []
        for item in triples:
            if item[0] == 'note':
                _, s, p, o, note, quals = item
                n = {'@type': STD['rdf'] + 'Statement', STD['rdf'] + 'subject': {'@id': s},
                     STD['rdf'] + 'predicate': {'@id': p}, STD['rdf'] + 'object': {'@id': o}}
                for qp, qv in quals:
                    n[qp] = qv
                if note:
                    n[STD['rdfs'] + 'comment'] = note
                notes.append(n)
                continue
            s, p, o = item
            n = nodes.setdefault(s, {'@id': s})
            val = {'@id': o[1]} if o[0] == 'iri' else o[1]
            if p == STD['rdf'] + 'type':
                n.setdefault('@type', []).append(o[1])
            else:
                n.setdefault(p, []).append(val)
        return list(nodes.values()) + notes
    doc = {'@graph': node_list(default) + [{'@id': g, '@graph': node_list(t)} for g, t in sorted(graphs.items())]}
    return json.dumps(doc, indent=1, ensure_ascii=False) + '\n'


def write_csv(statements, qualifiers):
    out = io.StringIO()
    w = csv.writer(out, lineterminator='\n')
    w.writerow(['subject', 'relation', 'object'] + list(qualifiers) + ['note', 'sources', 'page'])
    for st in statements:
        w.writerow([st['s'][1], st['p'], st['o'][1]] + [st['quals'].get(k, '') for k in qualifiers]
                   + [st['comment'], ' '.join(st['sources']), st['page']])
    return out.getvalue()


def write_mermaid(statements, classes):
    kinds = {}
    for st in statements:
        if st['p'] == 'is_a':
            kinds.setdefault(st['s'][1], []).append(label(st['o']))
    ids, lines = {}, []

    def nid(n):
        key = n[1]
        if key not in ids:
            ids[key] = 'n%d' % len(ids)
            text = key if n[0] == 'term' else os.path.basename(key)[:-3]
            if key in kinds:
                text += '<br/><i>' + ', '.join(sorted(set(kinds[key]))) + '</i>'
            lines.append('  %s["%s"]' % (ids[key], text.replace('"', "'")))
        return ids[key]
    by_page = {}
    for st in statements:
        if st['p'] != 'is_a':
            by_page.setdefault(st['page'], []).append(st)
    out = ['# Ontology graph (built)', '',
           'Built by `tools/ontology.py` from the Relations tables; do not edit by hand. Classes from `is_a` are shown in italics inside each box; a relation with a `verification` qualifier shows it in parentheses (run, pending or documented). See [ONTOLOGY.md](../ONTOLOGY.md).', '']
    for page, sts in sorted(by_page.items()):
        ids.clear()
        lines.clear()
        edges = []
        for st in sts:
            a, b = nid(st['s']), nid(st['o'])
            text = st['p'].replace('_', ' ')
            if st['quals'].get('verification'):
                text += ' (%s)' % st['quals']['verification']
            e = '  %s -->|"%s"| %s' % (a, text, b)
            if e not in edges:
                edges.append(e)
        out += ['## ' + page, '', '```mermaid', 'flowchart LR'] + lines + edges + ['```', '']
    return '\n'.join(out)


def check():
    import rdflib
    g = rdflib.Dataset(default_union=True)
    g.parse(os.path.join(OUT, 'second-brain.trig'), format='trig')
    quads = len(list(g.quads()))
    g2 = rdflib.Dataset(default_union=True)
    g2.parse(os.path.join(OUT, 'second-brain.jsonld'), format='json-ld')
    print('rdflib %s: TriG %d quads in %d graphs; JSON-LD %d quads' % (
        rdflib.__version__, quads, len(list(g.graphs())), len(list(g2.quads()))))
    qdir = os.path.join(OUT, 'queries')
    for fn in sorted(os.listdir(qdir)) if os.path.isdir(qdir) else []:
        if not fn.endswith('.rq'):
            continue
        q = read(os.path.join(qdir, fn))
        res = g.query(q)
        rows = [[str(v) if v is not None else '' for v in r] for r in res]
        head = [str(v) for v in res.vars]
        short = lambda x: re.sub(r'^https://github.com/dickinsonre/swmm-second-brain/(ontology/|ontology#|blob/main/)', '', x)
        lines = [l for l in q.strip().split('\n') if l.startswith('#')]
        lines.append('\t'.join(head))
        lines += ['\t'.join(short(c) for c in r) for r in rows]
        with open(os.path.join(qdir, fn[:-3] + '.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
        print('query %s: %d rows' % (fn, len(rows)))


def main():
    statements, vocab, sources_meta, errors = collect()
    for e in errors:
        print('ERROR', e)
    if errors:
        sys.exit(1)
    default, graphs = build(statements, vocab, sources_meta)
    os.makedirs(OUT, exist_ok=True)
    files = {'second-brain.trig': write_trig(default, graphs), 'second-brain.jsonld': write_jsonld(default, graphs),
             'relations.csv': write_csv(statements, vocab[3]), 'graph.md': write_mermaid(statements, vocab[2])}
    for fn, text in files.items():
        with open(os.path.join(OUT, fn), 'w', encoding='utf-8') as f:
            f.write(text)
    pages = sorted({st['page'] for st in statements})
    print('ontology: %d statements from %d pages, %d terms, %d source graphs -> ontology/' % (
        len(statements), len(pages), len({st[k][1] for st in statements for k in ('s', 'o')}), len(graphs)))
    if '--check' in sys.argv:
        check()


if __name__ == '__main__':
    main()
