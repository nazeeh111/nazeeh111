"""Offline integrity for this profile's inline Markdown and HTML references.

Checks local structure, not remote availability, scientific claims or rendering.
No third-party packages or network requests. Run from any working directory.
"""

import argparse
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
INLINE_START = re.compile(r'(!?)\[[^\]\n]*\]\(')
SVG = '{http://www.w3.org/2000/svg}'


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img' and not attrs.get('alt', '').strip():
            self.errors.append('HTML image needs nonempty alt text')
        for key in ('href', 'src'):
            if attrs.get(key):
                self.items.append((attrs[key], tag == 'img' and key == 'src'))
        if attrs.get('srcset'):
            for candidate in attrs['srcset'].split(','):
                parts = candidate.split()
                if parts:
                    self.items.append((parts[0], True))

    handle_startendtag = handle_starttag


def inline_references(text):
    """Read simple-label inline links, including balanced/angle destinations.

    This is a profile lint rule, not a Markdown renderer: reference-style links,
    autolinks and code-block interpretation are outside its declared syntax.
    """
    for match in INLINE_START.finditer(text):
        pos = match.end()
        while pos < len(text) and text[pos].isspace():
            pos += 1
        start = pos
        if pos < len(text) and text[pos] == '<':
            close = text.find('>', pos + 1)
            if close < 0 or '\n' in text[pos:close]:
                raise ValueError('unterminated angle link destination')
            destination, pos = text[pos + 1:close], close + 1
        else:
            depth = 0
            while pos < len(text):
                char = text[pos]
                if char == '\\':
                    pos += 2
                    continue
                if (char.isspace() or char == ')') and depth == 0:
                    break
                if char == '(':
                    depth += 1
                elif char == ')':
                    depth -= 1
                pos += 1
            destination = text[start:pos]
        whitespace = pos < len(text) and text[pos].isspace()
        while pos < len(text) and text[pos].isspace():
            pos += 1
        if pos < len(text) and text[pos] in ('"', "'", '('):
            if not whitespace:
                raise ValueError('inline link title needs separating whitespace')
            closer = ')' if text[pos] == '(' else text[pos]
            pos += 1
            while pos < len(text) and text[pos] != closer:
                pos += 2 if text[pos] == '\\' else 1
            if pos == len(text):
                raise ValueError('unterminated inline link title')
            pos += 1
            while pos < len(text) and text[pos].isspace():
                pos += 1
        if pos >= len(text) or text[pos] != ')':
            raise ValueError('unterminated or unsupported inline link')
        destination = unescape(re.sub(r'\\([!"#$%&\'()*+,\-./:;<=>?@\[\]\\^_`{|}~])', r'\1', destination))
        yield destination, bool(match.group(1))


def references(text):
    parser = References()
    parser.feed(text)
    parser.close()
    parser.items.extend(inline_references(text))
    return parser.items, parser.errors


def local_file(root, document, target):
    """Resolve within this repository; do not read an escaping symlink target."""
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        raise ValueError('expected repository-relative file')
    path = unquote(parsed.path)
    if not path or path.startswith('/') or '\\' in path:
        raise ValueError('expected repository-relative file')
    result = document.parent.joinpath(path).resolve()
    if not result.is_relative_to(root):
        raise ValueError('reference escapes repository')
    if not result.is_file():
        raise ValueError('referenced file is missing')
    return result


def immutable_source(url):
    parsed = urlsplit(url)
    parts = parsed.path.strip('/').split('/')
    if parsed.hostname == 'github.com' and len(parts) >= 3 and parts[2] in ('blob', 'raw'):
        return len(parts) >= 5 and re.fullmatch('[0-9a-fA-F]{40}', parts[3]) is not None
    if parsed.hostname == 'raw.githubusercontent.com':
        return len(parts) >= 4 and re.fullmatch('[0-9a-fA-F]{40}', parts[2]) is not None
    return True


def check_svg(path):
    root = ET.parse(path).getroot()
    if root.tag != SVG + 'svg':
        raise ValueError('root must be an SVG element')
    ids = {}
    for node in root.iter():
        key = node.get('id')
        if key:
            if key in ids:
                raise ValueError('duplicate SVG id: ' + key)
            ids[key] = node
    required = []
    for tag in ('title', 'desc'):
        node = root.find(SVG + tag)
        if node is None or not ''.join(node.itertext()).strip() or not node.get('id'):
            raise ValueError('SVG needs a nonempty root ' + tag + ' with id')
        required.append(node.get('id'))
    labels = root.get('aria-labelledby', '').split()
    if root.get('role') != 'img' or not set(required).issubset(labels):
        raise ValueError('SVG image label must include title and description')
    if any(key not in ids for key in labels):
        raise ValueError('SVG label references a missing id')


def check(root=ROOT):
    root = root.resolve()
    errors = []
    images = set()
    visited = set()
    pending = [root / 'README.md', root / 'START_HERE.md']
    try:
        mapping = json.loads((root / 'profile-assets.json').read_text(encoding='utf-8'))
        if set(mapping) != {'version', 'images'} or type(mapping['version']) is not int or mapping['version'] != 1:
            raise ValueError('expected asset-map version1')
        mapping = mapping['images']
        if not isinstance(mapping, dict) or not mapping:
            raise ValueError('asset map must be a nonempty object')
        for image, provenance in mapping.items():
            if not isinstance(provenance, str):
                raise ValueError('provenance path must be a string')
            source = local_file(root, root / 'README.md', image)
            note = local_file(root, root / 'README.md', provenance)
            if note.suffix != '.md':
                raise ValueError('provenance must be Markdown')
            text = note.read_text(encoding='utf-8')
            if source.name not in text:
                raise ValueError('provenance must identify image: ' + image)
            refs, _ = references(text)
            if not any(urlsplit(url).hostname == 'github.com' and '/blob/' in urlsplit(url).path
                       and immutable_source(url) for url, _ in refs):
                raise ValueError('provenance needs a fixed-revision source citation: ' + provenance)
            pending.append(note)
    except (OSError, ValueError, TypeError) as exc:
        return ['profile-assets.json: ' + str(exc)]
    while pending:
        document = pending.pop()
        if document in visited:
            continue
        visited.add(document)
        try:
            refs, markup_errors = references(document.read_text(encoding='utf-8'))
            errors.extend(f'{document.relative_to(root)}: {e}' for e in markup_errors)
            for url, image in refs:
                parsed = urlsplit(url)
                if parsed.scheme or parsed.netloc:
                    if image:
                        raise ValueError('profile images must be local and mapped: ' + url)
                    if not immutable_source(url):
                        raise ValueError('source citation needs a full40hex commit: ' + url)
                elif parsed.path:
                    path = local_file(root, document, url)
                    if image:
                        images.add(path.relative_to(root).as_posix())
                    elif path.suffix == '.md':
                        pending.append(path)
        except (OSError, ValueError) as exc:
            errors.append(f'{document.relative_to(root)}: {exc}')
    if images != set(mapping):
        errors.append('image/provenance map differs from rendered images: missing=' +
                      repr(sorted(images - set(mapping))) + ', unused=' + repr(sorted(set(mapping) - images)))
    for image in sorted(images):
        if image.endswith('.svg'):
            try:
                check_svg(root / image)
            except (OSError, ValueError, ET.ParseError) as exc:
                errors.append(image + ': ' + str(exc))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='profile checkout to check')
    args = parser.parse_args()
    errors = check(args.root)
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print('Profile integrity passed (offline structure and source-link syntax only).')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
