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
5. When the task touches INTEGRAL principles, one of the five systems,
   community technology, resource coordination or federation, also read the
   relevant parts of `editorial/INTEGRAL_IN_STORY.md`. It is a framework
   reference, not a replacement for story canon.
6. Ask the author what they want to work on if the next task is not explicit.
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
- Use `editorial/INTEGRAL_IN_STORY.md` when relevant to understand the framework; use `STORY.md` for what is already true in the novel. Do not silently make an early village arrangement equivalent to a complete INTEGRAL system.
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

The chapter-based source, chapter guide and AI task template are in `main`.
The current editorial framework reference is `editorial/INTEGRAL_IN_STORY.md`;
read it when a task involves the five systems, technology or federation. It is
based on the author's supplied plain-English guide and does not replace the
full technical paper or the story canon. Existing continuity review questions
remain review questions, not approved edits.

## 8. Multi-agent synchronisation

GitHub `main` is the source of truth for the shared story. A local checkout,
an agent's workspace and a downloaded ZIP are only copies; they may be behind.

### If the agent has repository access

1. Before editing, fetch the latest repository state and check open pull requests
   and recent commits.
2. Work on a dedicated feature branch, not directly on `main`.
3. Commit the agreed source changes and open or update a pull request against
   `main`.
4. Tell the author the branch and PR link, list the changed files, and mention
   whether the website build was run and verified.
5. Do not merge unless the author explicitly asks.

### If the agent does not have repository access

1. Ask it to work from the latest files supplied by the author—not from an
   assumed or remembered copy.
2. Request a Git patch where possible. Otherwise request the complete changed
   files with their exact repository paths, preferably in a ZIP.
3. The author should review the changes before adding them to the repository.
4. Apply them on a new local feature branch, run the build and checks, then
   commit and push the branch and open a pull request.
5. Never overwrite newer repository work with an older file. If the file has
   changed since the agent received its copy, compare and reconcile the edits.

### Updating the author's local checkout

After a pull request is merged, the author can update their local copy with:

```bash
git switch main
git pull origin main
```

If the author has not cloned the repository yet, clone it once:

```bash
git clone https://github.com/knottyman/lower-wobbling.git
```

A PR merge updates GitHub; it does not automatically update anyone's local
checkout. Each local copy must be pulled separately.

### Handover between agents

Every agent handing work to another agent should provide:
- The repository branch and latest commit it worked from.
- The exact files changed.
- A PR link, or the patch/ZIP and exact paths if it lacked repository access.
- Build/test results and anything not verified.
- Any decisions or questions that need the author's approval.

The next agent must check the current repository state before applying a patch
or continuing work. Treat external agent output as a proposal until reviewed
and reconciled with the latest `main`.
