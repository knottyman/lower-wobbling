#!/usr/bin/env python3
"""Build index.html from template.html and ordered HTML story fragments."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "story" / "manifest.json"
MARKER = "<!-- GENERATED_STORY_CONTENT -->"

def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    template = (ROOT / manifest["template"]).read_text(encoding="utf-8")
    if template.count(MARKER) != 1:
        raise SystemExit(f"Expected exactly one {MARKER!r} marker in template.html")
    rendered, seen = [], set()
    for item in manifest["content"]:
        rel = Path(item["path"])
        if rel.is_absolute() or ".." in rel.parts:
            raise SystemExit(f"Unsafe fragment path: {rel}")
        if rel.as_posix() in seen:
            raise SystemExit(f"Duplicate fragment: {rel}")
        seen.add(rel.as_posix())
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"Missing story fragment: {path}")
        rendered.append(path.read_text(encoding="utf-8").rstrip())
    output = template.replace(MARKER, "\n\n".join(rendered))
    (ROOT / manifest["output"]).write_text(output, encoding="utf-8")
    print(f"Built {manifest['output']} from {len(rendered)} fragments.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
