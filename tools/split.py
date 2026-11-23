#!/usr/bin/env python3
"""
split.py — derive chapters/*.md + manifest.json from the canonical index.html.

Usage: python3 tools/split.py
Reads:  index.html
Writes: chapters/*.md, manifest.json

The chapter files are the editable units. The canonical HTML is NOT touched.
Run tools/reassemble.py afterwards to push fragment edits back into index.html.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
CH_DIR = ROOT / "chapters"
MANIFEST = ROOT / "manifest.json"

# Section id -> output file. Order is the reading order.
SECTION_FILES = [
    ("prologue",  "00-prologue.md"),
    ("ch1",       "01-the-lettuce.md"),
    # noticeboard interlude is handled specially, after ch1
    ("ch2",       "02-the-money.md"),
    ("ch3",       "03-not-convinced.md"),
    ("ch4",       "04-the-greenhouse.md"),
    ("ch5",       "05-the-ledger.md"),
    ("ch6",       "06-first-winter.md"),
    ("ch7",       "07-the-ladders.md"),
    ("ch8",       "08-supply-chain.md"),
    ("ch9",       "09-the-visitors.md"),
    ("ch10",      "10-next-village.md"),
    ("ch11",      "11-delivery-note.md"),
    ("epilogue",  "12-epilogue.md"),
    ("appendix",  "13-appendix.md"),
]

SECTION_RE = re.compile(
    r'<section\s+id="(?P<id>[^"]+)"\s*>(?P<body>.*?)</section>',
    re.DOTALL,
)
KICKER_RE = re.compile(r'<p class="kicker">(?P<k>.*?)</p>', re.DOTALL)
H2_RE = re.compile(r'<h2>(?P<t>.*?)</h2>', re.DOTALL)
NOTICEBOARD_RE = re.compile(
    r'<div class="noticeboard">(?P<body>.*?)</div>\s*(?=<!--|$)',
    re.DOTALL,
)
TAG_RE = re.compile(r'<[^>]+>')
WS_RE = re.compile(r'[ \t]+')
BLANK_RE = re.compile(r'\n{3,}')


def strip_tags(s: str) -> str:
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</p\s*>', '\n\n', s)
    s = re.sub(r'</h[1-6]\s*>', '\n\n', s)
    s = re.sub(r'<li\b[^>]*>', '- ', s)
    s = TAG_RE.sub('', s)
    s = s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    s = s.replace('&mdash;', '—').replace('&ndash;', '–')
    s = s.replace('&rsquo;', '’').replace('&lsquo;', '‘')
    s = s.replace('&ldquo;', '“').replace('&rdquo;', '”')
    s = s.replace('&nbsp;', ' ')
    s = WS_RE.sub(' ', s)
    s = BLANK_RE.sub('\n\n', s)
    return s.strip()


def extract_figure(body: str) -> str:
    """Preserve <figure> blocks as HTML (they carry images and captions)."""
    return "\n\n".join(
        m.group(0) for m in re.finditer(r'<figure>.*?</figure>', body, re.DOTALL)
    )


def body_to_md(body: str) -> str:
    # Pull out figures first so they survive as HTML.
    figures = extract_figure(body)
    # Drop the figure blocks from the text extraction to avoid duplication.
    text_body = re.sub(r'<figure>.*?</figure>', '', body, flags=re.DOTALL)
    # Drop the kicker and h2 (they go into front-matter and are re-rendered).
    text_body = KICKER_RE.sub('', text_body)
    text_body = H2_RE.sub('', text_body)
    # Convert section breaks.
    text_body = re.sub(r'<hr class="star">', '\n\n---\n\n', text_body)
    text_body = re.sub(r'<hr class="star"\s*/>', '\n\n---\n\n', text_body)
    md = strip_tags(text_body)
    # Normalise the divider that came out of the hr replacement.
    md = re.sub(r'\n?---\n?', '\n\n---\n\n', md).strip()
    parts = [md]
    if figures:
        parts.append("\n\n<!-- figures from the canonical HTML; keep as-is -->\n" + figures)
    return "\n\n".join(p for p in parts if p).strip() + "\n"


def front_matter(sid: str, kicker: str | None, title: str) -> str:
    lines = ["---", f'id: "{sid}"']
    if kicker:
        lines.append(f'kicker: "{kicker}"')
    lines.append(f'title: "{title}"')
    lines.append('canonical: "index.html"')
    lines.append('edit_here: true')
    lines.append("---\n")
    return "\n".join(lines)


def main() -> int:
    if not INDEX.exists():
        print(f"error: {INDEX} not found", file=sys.stderr)
        return 1
    html = INDEX.read_text(encoding="utf-8")
    CH_DIR.mkdir(exist_ok=True)

    sections = {m.group("id"): m.group("body") for m in SECTION_RE.finditer(html)}
    # The noticeboard div sits outside any <section>.
    nb = NOTICEBOARD_RE.search(html)
    noticeboard_body = nb.group("body") if nb else None

    manifest_sections = []
    # Insert the noticeboard after ch1 in reading order.
    for sid, fname in SECTION_FILES:
        if sid == "ch2" and noticeboard_body is not None:
            write_noticeboard(noticeboard_body)
            manifest_sections.append({
                "id": "noticeboard",
                "num": None,
                "kicker": None,
                "title": "Ballywobble Noticeboard (interlude)",
                "file": "chapters/interlude-noticeboard.md",
                "words": count_words(noticeboard_body),
            })
        body = sections.get(sid)
        if body is None:
            print(f"warning: section #{sid} not found in index.html", file=sys.stderr)
            continue
        kicker = KICKER_RE.search(body)
        kicker_txt = strip_tags(kicker.group("k")) if kicker else None
        h2 = H2_RE.search(body)
        title = strip_tags(h2.group("t")) if h2 else sid
        md = front_matter(sid, kicker_txt, title) + body_to_md(body)
        out = CH_DIR / fname
        out.write_text(md, encoding="utf-8")
        # num comes from the TOC; we derive it from the filename prefix.
        num = None
        m = re.match(r'(\d+)-', fname)
        if m:
            num = m.group(1).lstrip("0") or "0"
        if sid in ("prologue", "epilogue"):
            num = "—"
        if sid == "appendix":
            num = "◆"
        manifest_sections.append({
            "id": sid,
            "num": num,
            "kicker": kicker_txt,
            "title": title,
            "file": f"chapters/{fname}",
            "words": count_words(body),
        })
        print(f"wrote {out.relative_to(ROOT)} ({count_words(body)} words)")

    manifest = {
        "title": "The Greenhouse at Ballywobble",
        "canonical": "index.html",
        "story_bible": "STORY.md",
        "generated_by": "tools/split.py",
        "sections": manifest_sections,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    print(f"wrote {MANIFEST.relative_to(ROOT)}")
    return 0


def write_noticeboard(body: str) -> None:
    md = strip_tags(body)
    # Keep the individual lines as block quotes so they read as a forum.
    lines = [ln.strip() for ln in md.splitlines() if ln.strip()]
    quoted = "\n".join(f"> {ln}" for ln in lines)
    out = CH_DIR / "interlude-noticeboard.md"
    out.write_text(
        "---\n"
        'id: "noticeboard"\n'
        'kicker: null\n'
        'title: "Ballywobble Noticeboard (interlude)"\n'
        'canonical: "index.html"\n'
        'edit_here: true\n'
        "---\n\n"
        "<!-- Forum interlude between ch1 and ch2. Keep the poster voice. -->\n\n"
        f"{quoted}\n",
        encoding="utf-8",
    )
    print(f"wrote {out.relative_to(ROOT)}")


def count_words(html: str) -> int:
    text = strip_tags(html)
    return len(re.findall(r"\b[\w’'-]+\b", text))


if __name__ == "__main__":
    sys.exit(main())
