# AGENTS.md — working on The Greenhouse at Ballywobble

## Source of truth
- `STORY.md` is canon for plot, characters, timeline, themes and open decisions.
- `story/manifest.json` defines reading order.
- `story/chapters/*.html` and `story/interludes/*.html` are editable story source.
- `template.html` contains website shell, CSS, JavaScript, title block and table of contents.
- `index.html` is generated output. Never edit it directly.

## Token-efficient reading workflow
1. Read this file.
2. Read only relevant headings in `STORY.md`; do not load the whole bible by default.
3. Read `story/manifest.json` to identify the target fragment and neighbours.
4. Read the target chapter and only adjacent material needed for continuity.
5. Do not read `index.html` for prose-editing tasks.

## Editing rules
- Work on one chapter or interlude per task unless asked otherwise.
- Edit only the requested fragment; do not rewrite or summarise other chapters.
- Fragments are HTML, not Markdown. Preserve valid HTML, classes, IDs, figures, links and semantic structure.
- Preserve inline `<strong>`, `<em>`, paragraph boundaries and `<hr class="star">` dividers.
- Do not change section IDs or manifest order unless asked.
- Never invent canon to resolve an open thread. Ask the author first.
- Keep en-GB / Hiberno-English, dry and understated, third-person past.
- No new exclamation marks in narration. Show the system in use; do not explain it at length.

## Protected canon
Do not alter without explicit author approval:
- The one-way valve rule: credits are not money and cannot convert to euros.
- Hob signing before chapter nine, or his established arc.
- Pennyfeather's finding: "It is a shed."
- The prologue and epilogue framing.
- Open threads and unresolved decisions recorded in `STORY.md`.

## Build and verification
After editing story content, run:
```bash
python3 tools/build.py
```
This rebuilds `index.html` from `template.html` and the ordered fragments.
For prose-only tasks, do not modify the template, CSS or JavaScript.
For website tasks, edit `template.html`, then rebuild.
Do not run old `tools/split.py` or `tools/reassemble.py`; they belong to the previous lossy Markdown workflow.

## Before finishing
- Confirm only requested source fragments changed.
- Run the build.
- Check generated HTML contains all chapter section IDs.
- Report changed files and continuity implications.
- Add a concise `CHANGELOG.md` entry for substantive story changes.
