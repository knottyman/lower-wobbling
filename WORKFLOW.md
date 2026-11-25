# Working workflow — The Greenhouse at Ballywobble

This file is the shared handover for the author and any AI agent. Read it at the
start of every new working session, including when returning after a break.
It records how we work; it does not replace the story canon.

## 1. Start every session here

1. Read this file and `AGENTS.md`.
2. Check the current GitHub branch, open pull requests and recent commits before
   assuming what has or has not been done.
3. Read `CHAPTER_GUIDE.md` to find the relevant part of the story.
4. Read only the necessary headings in `STORY.md`, then the target chapter and
   any adjacent material needed for continuity.
5. Ask the author what they want to work on if the next task is not explicit.
   Do not assume an old suggestion has been approved.

## 2. How we collaborate

The author is the decision-maker. The AI is a writing partner, researcher and
careful editor—not the owner of the story.

For each task:

1. **Agree the task.** Define one clear chapter, scene, character or story
   question. Keep the scope small.
2. **Explore before changing.** For developmental work, identify what works,
   what feels weak and possible approaches. Offer options and explain trade-offs.
   Do not rewrite the story before the author agrees.
3. **Check continuity.** Compare the proposal with the relevant story-bible
   details, timeline, character motivations and unresolved threads.
4. **Make a focused change.** Edit only the agreed source fragment(s). Preserve
   the established voice and HTML structure.
5. **Review together.** Explain what changed, why, and any new continuity
   implications. Show a concise diff or the changed passage.
6. **Publish safely.** Build and verify the website, then use a feature branch
   and pull request for review. Do not push experimental prose straight to
   `main` without the author's agreement.

Use `AI_TASK_TEMPLATE.md` when preparing a focused prompt for another agent.

## 3. Writing principles

- Keep the voice dry, warm, understated and quietly funny.
- Use third-person past tense and en-GB / Hiberno-English.
- Prefer scenes, dialogue and practical consequences over speeches explaining
  the ideas.
- Let people have understandable pressures, interests and doubts. Avoid making
  opponents into caricatures or turning supporters into heroes.
- The village should feel like a real place with limited time, money, skills and
  energy—not a perfect demonstration project.
- Preserve ambiguity and unresolved endings where the story has left them.
- Do not invent a character's history, motivation or decision when canon is
  unclear. Flag the gap and ask.

## 4. Keep AI context and cost under control

- Never load the whole website or every chapter for an ordinary edit.
- Use `CHAPTER_GUIDE.md` for navigation, not as a substitute for canon.
- Read only relevant `STORY.md` headings and the target fragment.
- Read neighbouring chapters only when needed to check a hand-off or callback.
- Ask for an outline or critique before asking for a full new scene.
- Return summaries and diffs, not full copies of unchanged files.
- If a task genuinely needs a wider read, explain why before doing it.

## 5. Repository rules

- Canon: `STORY.md`.
- Chapter summaries/navigation: `CHAPTER_GUIDE.md`.
- Ordered source fragments: `story/manifest.json`.
- Editable prose: `story/chapters/`, `story/interludes/` and `story/structure/`.
- Website shell: `template.html`.
- Generated website: `index.html` — never edit it directly.
- After source edits, run `python3 tools/build.py` and verify the output.
- Do not use the legacy `tools/split.py` or `tools/reassemble.py` workflow.
- Keep each pull request focused and describe exactly what changed.

## 6. Session handover

At the end of a substantial session, give the author a short handover containing:

- What was decided.
- Which files changed.
- Which pull request or branch contains the work.
- What remains unresolved.
- The single most useful next step.

Update this file only when the agreed working process changes. Put story facts
and plot decisions in `STORY.md`, not here.

## 7. Current starting point

The chapter-based source and build workflow has been merged into `main`.
A follow-up pull request adds the chapter guide and AI task template; check its
status on GitHub at the start of a session. The first suggested editorial task
is a continuity review of the interlude inventory and the repeated Drumroe
reflection across chapters 10–11. These are review questions, not approved edits.
