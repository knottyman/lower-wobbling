# AI writing task template

Copy this prompt into your coding/writing agent and fill in the square-bracketed
parts. Give the agent only the files it needs.

---

You are helping edit **The Greenhouse at Ballywobble**.

## Task
[Describe one specific change or question. Name the chapter and the desired outcome.]

## Files to read
- `AGENTS.md`
- `CHAPTER_GUIDE.md`
- `editorial/INTEGRAL_IN_STORY.md` when the task involves INTEGRAL systems, technology, resource coordination or federation
- Only the relevant headings from `STORY.md`: [list headings]
- Target fragment: [path, e.g. `story/chapters/06-first-winter.html`]
- Adjacent fragment(s), only if needed: [paths]

Do not read `index.html` for a prose task. It is generated output.

## Rules
- Treat `STORY.md` as canon. If the request appears to conflict with it, stop
  and explain the conflict before editing.
- Preserve the established voice: dry, warm, understated, third-person past,
  en-GB / Hiberno-English.
- Do not turn the story into a manifesto, explain its ideas in lectures, or
  make the village into a collection of caricatures.
- When using INTEGRAL concepts, distinguish the framework described in
  `editorial/INTEGRAL_IN_STORY.md` from the village's existing partial
  arrangements. `STORY.md` remains canon; do not silently retrofit the full
  CDS, OAD, ITC, COS or FRS onto an established story mechanism.
- Preserve unresolved threads. Do not invent a resolution without asking.
- Change only the requested fragment. Do not rewrite neighbouring chapters
  for convenience.
- Preserve the existing HTML structure, IDs, classes, figures, links and
  emphasis unless the task specifically asks for a structural change.

## Before editing
1. Briefly state your understanding of the requested change.
2. Identify any canon or continuity risks.
3. If an essential detail is missing, ask one focused question. Otherwise proceed.

## After editing
1. Summarise what changed and why.
2. List any continuity implications or open questions.
3. Show the diff or the changed passage; do not paste the entire chapter unless asked.
4. Do not edit `index.html` by hand. Rebuild it with `python3 tools/build.py`
   after the source edit, then check the generated page and chapter IDs.
5. Report exactly which files changed.

## Suggested task shapes
- **Development:** “Find the weakest point in chapter [N]. Suggest three possible
  improvements, but do not edit yet.”
- **Line edit:** “Tighten this passage while preserving its meaning, voice and
  characterisation. Make the smallest useful changes.”
- **Continuity check:** “Check chapter [N] against the relevant canon and adjacent
  chapters. Report contradictions; do not fix them.”
- **New scene:** “Propose a scene that advances [character/plot function]. Give
  me an outline first; do not draft until I approve it.”
