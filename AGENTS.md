# AGENTS.md — how to edit this story

## Read order (mandatory)

1. `STORY.md` — the whole-arc context. **Read this first, every time.**
2. `manifest.json` — the fragment index. Use it to find the chapter you
   need; do not read every fragment.
3. The specific `chapters/*.md` fragment(s) you are editing.
4. Only if you need the full text: `index.html` (canonical, large).

## Source of truth

`index.html` is canonical. `chapters/*.md` are **derived**. The normal
workflow is:

- **Edit a fragment** (`chapters/NN-*.md`), then run `tools/reassemble.py`
  to regenerate `index.html`. Never hand-edit `index.html` and expect the
  fragments to update — they won't.
- If you must hand-edit `index.html` (e.g. CSS, `<head>`, the noticeboard
  interlude), run `tools/split.py` afterwards to re-derive the fragments.

## What you may edit

- Prose inside a chapter fragment. Keep the YAML front-matter intact.
- The noticeboard interlude — but keep the forum-poster voice (Barry G.,
  Sheila P., Mabel B.) and the `(OFFICIAL) (NO POLITICS)` header.
- The appendix table — but keep it consistent with `STORY.md`.

## What you may **not** edit without explicit author approval

- The one-way valve rule (credits ≠ money).
- Hob signing before ch9, or any change to his arc.
- Pennyfeather's finding ("It is a shed.").
- The open threads listed in `STORY.md`.
- The prologue frame or the epilogue frame.
- Character names, ages, or roles in `STORY.md`.
- The `id` attributes of sections (they are anchors; changing them breaks
  links and the manifest).

## Style

Follow the "Style rules for editors" in `STORY.md`. In particular:

- en-GB / Hiberno-English spelling and idiom.
- Dry, understated, third-person past.
- No explaining the system; show it in use.
- No new exclamation marks in narration.
- Preserve `<hr class="star">` section breaks where they exist.

## Continuity checks before you commit

Run through this list:

- [ ] Does the edit contradict `STORY.md`'s timeline?
- [ ] Does it contradict a character's arc (esp. Hob, Gerard, O'Driscoll)?
- [ ] Does it introduce a concept not in the appendix or `STORY.md`?
  If so, add it to both.
- [ ] Does it let credits convert to euros, or vice versa? (If yes: stop.)
- [ ] Does it make Pennyfeather a villain, or Hob a spokesman? (If yes: stop.)
- [ ] Does it explain the Rota, the Board, or the Ledger rather than show
  them? (If yes: rewrite.)
- [ ] Have you run `tools/reassemble.py` and confirmed `index.html` still
  opens in a browser?

## Changelog

If you make a substantive change (new scene, new character beat, changed
arc), add a line to `CHANGELOG.md` describing what changed and why. Keep
it to one line per change.
