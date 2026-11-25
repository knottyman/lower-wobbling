# lower-wobbling

**The Greenhouse at Ballywobble** — a story about an ordinary village doing something rather extraordinary.

## Where to edit
- `STORY.md` — story bible and canon.
- `story/chapters/` — one HTML file per chapter.
- `story/interludes/` — noticeboard and forum/thread interludes.
- `story/manifest.json` — reading order.
- `template.html` — website shell, styling and behaviour.
- `index.html` — generated website; do not edit by hand.

## Build
Requires Python 3; no third-party packages:
```bash
python3 tools/build.py
```
The build joins the original HTML fragments into `index.html`. Original markup is retained, including emphasis, figures, tables and interlude formatting.

## AI editing workflow
For a chapter edit, give your agent `AGENTS.md`, only the relevant part of `STORY.md`, the target file under `story/chapters/`, and adjacent chapters only when needed. Avoid sending `index.html` to prose-editing agents.
