#!/usr/bin/env python3
"""Validate links, anchors, and pipe-bearing syntax in generated book HTML."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.rows, self.code = set(), [], [], []
        self.cells = None
        self.code_text = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        key = 'href' if tag in ('a', 'link') else 'src'
        if attrs.get(key):
            self.links.append(attrs[key])
        if tag == 'tr':
            self.cells = 0
        elif tag in ('th', 'td') and self.cells is not None:
            self.cells += 1
        elif tag == 'code':
            self.code_text = ''

    def handle_data(self, data):
        if self.code_text is not None:
            self.code_text += data

    def handle_endtag(self, tag):
        if tag == 'tr' and self.cells is not None:
            self.rows.append(self.cells)
            self.cells = None
        elif tag == 'code' and self.code_text is not None:
            self.code.append(self.code_text)
            self.code_text = None


def check(root):
    root = root.resolve()
    pages = {p.resolve(): Page(p.read_text()) for p in root.rglob('*.html')}
    errors = []
    for path, page in pages.items():
        for raw in page.links:
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target = target / 'index.html'
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f'{path.relative_to(root)}: missing local target {raw}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(root)}: missing anchor {raw}')
        if path.name == 'current-language.html':
            if not page.rows or any(n != 3 for n in page.rows):
                errors.append(f'{path.relative_to(root)}: quick-reference table must have 3 cells per row')
            for form in ('<| expr', '?(cond) => { ... } | { ... }'):
                if form not in page.code:
                    errors.append(f'{path.relative_to(root)}: damaged syntax {form}')
    for lang in ('cn', 'en'):
        for rel in ('index.html', 'current-language.html', 'cookbook/chaining-and-composition.html', 'contributing.html'):
            if root / lang / rel not in pages:
                errors.append(f'missing required rendered page: {lang}/{rel}')
    return pages, errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    args = parser.parse_args()
    pages, errors = check(args.root)
    print('\n'.join(errors) if errors else f'PASS: {len(pages)} rendered pages, local links/anchors, and syntax tables')
    raise SystemExit(bool(errors))
