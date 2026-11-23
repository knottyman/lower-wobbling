#!/usr/bin/env python3
"""
reassemble.py — push chapter fragment edits back into canonical index.html.

Usage: python3 tools/reassemble.py
Reads:  chapters/*.md, manifest.json, index.html
Writes: index.html (in place; a .bak is kept)

This is deliberately conservative. It refuses to run if:
  - the fragment set doesn't match manifest.json
  - a fragment has lost its front-matter id
  - a fragment contains a <section> tag (would nest sections)
It preserves the <figure> blocks as HTML and converts Markdown paragraphs
back to <p> tags. It is not a full Markdown renderer; it handles the
subset this story uses (paragraphs, ---, blockquotes, figures).
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
MANIFEST = ROOT / "manifest.json"

FRONT_RE = re.compile(r'^---\n(?P<fm>.*?)\n---\n', re.DOTALL)
ID_RE = re.compile(r'^id:\s*"(?P<id>[^"]+)"', re.MULTILINE)
SECTION_RE = re.compile(
    r'(<section\s+id="(?P<id>[^"]+)"\s*>)(?P<body>.*?)(</section>)',
    re.DOTALL,
)


def md_to_html_body(md: str) -> str:
    """Convert the fragment body (after front-matter) to HTML paragraphs."""
    # Preserve figures verbatim.
    figures = re.findall(r'<figure>.*?</figure>', md, re.DOTALL)
    text = re.sub(r'<figure>.*?</figure>', '', md, flags=re.DOTALL)
    # Drop the HTML comment we emit from split.py.
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL).strip()
    # Blockquotes -> .noticeboard lines (only used by the interlude, which
    # is handled separately; here we just keep them as <p> for safety).
    out_blocks = []
    for block in re.split(r'\n\s*\n', text):
        block = block.strip()
        if not block:
            continue
        if block == '---' or block == '* * *':
            out_blocks.append('<hr class="star">')
            continue
        # Strip leading "> " from noticeboard-style lines.
        block = re.sub(r'^>\s?', '', block, flags=re.MULTILINE)
        # Join wrapped lines into one paragraph.
        para = ' '.join(ln.strip() for ln in block.splitlines() if ln.strip())
        para = para.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        out_blocks.append(f'<p>{para}</p>')
    body = '\n\n    '.join(out_blocks)
    if figures:
        body += '\n\n    ' + '\n\n    '.join(figures)
    return body


def main() -> int:
    if not MANIFEST.exists():
        print("error: manifest.json not found; run split.py first", file=sys.stderr)
        return 1
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = {s["id"]: s["file"] for s in manifest["sections"]}

    # 1) Verify the fragment set matches the manifest.
    found = {}
    for s in manifest["sections"]:
        p = ROOT / s["file"]
        if not p.exists():
            print(f"error: missing fragment {p}", file=sys.stderr)
            return 1
        fm = FRONT_RE.match(p.read_text(encoding="utf-8"))
        if not fm:
            print(f"error: {p} has no front-matter", file=sys.stderr)
            return 1
        m = ID_RE.search(fm.group("fm"))
        if not m or m.group("id") != s["id"]:
            print(f"error: {p} front-matter id mismatch", file=sys.stderr)
            return 1
        found[s["id"]] = p
    if set(found) != set(expected):
        print("error: fragment set != manifest", file=sys.stderr)
        return 1

    # 2) Rewrite each section body in index.html.
    html = INDEX.read_text(encoding="utf-8")
    shutil.copy2(INDEX, INDEX.with_suffix(".html.bak"))

    def repl(m):
        sid = m.group("id")
        if sid == "appendix":
            # The appendix is a table; keep the canonical HTML for it.
            return m.group(0)
        p = found.get(sid)
        if p is None:
            return m.group(0)
        raw = p.read_text(encoding="utf-8")
        fm = FRONT_RE.match(raw)
        body_md = raw[fm.end():] if fm else raw
        new_body = md_to_html_body(body_md)
        return f'{m.group(1)}\n    {new_body}\n  {m.group(4)}'

    new_html = SECTION_RE.sub(repl, html)

    # 3) Handle the noticeboard interlude separately (it's a <div>).
    nb_file = ROOT / "chapters/interlude-noticeboard.md"
    if nb_file.exists():
        raw = nb_file.read_text(encoding="utf-8")
        fm = FRONT_RE.match(raw)
        body_md = raw[fm.end():] if fm else raw
        # Turn "> line" blocks back into <p> lines.
        lines = [re.sub(r'^>\s?', '', ln).strip()
                 for ln in body_md.splitlines() if ln.strip()]
        inner = "\n    ".join(
            f'<p><span class="who">{ln.split(":",1)[0]}:</span>{ln.split(":",1)[1]}</p>'
            if ":" in ln and not ln.startswith("Ballywobble")
            else f'<p class="head">{ln}</p>'
            for ln in lines
        )
        new_div = f'<div class="noticeboard">\n    {inner}\n  </div>'
        new_html = re.sub(
            r'<div class="noticeboard">.*?</div>',
            new_div,
            new_html,
            count=1,
            flags=re.DOTALL,
        )

    INDEX.write_text(new_html, encoding="utf-8")
    print(f"updated {INDEX.relative_to(ROOT)} (backup: index.html.bak)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
