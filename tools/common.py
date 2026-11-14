"""Shared helpers for the wiki tools. Standard library only."""
import hashlib, os, re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
RAW = os.path.join(ROOT, 'raw')
WIKI = os.path.join(ROOT, 'wiki')


def read(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read()


def front_matter(text):
    """Return (dict, body). Only flat `key: value` lines and `key: [a, b]` lists are read."""
    if not text.startswith('---\n'):
        return {}, text
    end = text.find('\n---', 4)
    if end < 0:
        return {}, text
    fm = {}
    for line in text[4:end].split('\n'):
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if v.startswith('[') and v.endswith(']'):
            v = [x.strip().strip('"\'') for x in v[1:-1].split(',') if x.strip()]
        else:
            v = v.strip('"\'')
        fm[k] = v
    return fm, text[end + 4:].lstrip('\n')


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def walk(top, exts=None):
    out = []
    for d, _, files in os.walk(top):
        for fn in sorted(files):
            if fn.startswith('.'):
                continue
            if exts and not fn.lower().endswith(exts):
                continue
            out.append(os.path.join(d, fn))
    return sorted(out)


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, '/')


def wiki_pages():
    pages = walk(WIKI, ('.md',))
    for extra in ('index.md', 'log.md'):
        p = os.path.join(ROOT, extra)
        if os.path.exists(p):
            pages.append(p)
    return pages


LINK = re.compile(r'(?<!\!)\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')


def links(text):
    """Markdown links [text](target), code blocks and inline code removed first."""
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', '', text)
    return LINK.findall(text)
