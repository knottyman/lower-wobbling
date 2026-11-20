# Agent Workflow & Seasonal Editing Guide

This guide explains how to develop *The Greenhouse at Lower Wobbling* in small, repeatable passes across separate sessions without losing voice, continuity, or momentum.

## Repository Layout (Recommended)
- `story-bible.md` — Canonical characters, world mechanics, tone rules, and chapter map.
- `editorial/AGENT_WORKFLOW.md` — This file (session rules and VSM mapping).
- `editorial/LOOSE_ENDS.md` — Queue of open continuity items, unresolved hooks, and target chapters.
- `editorial/SEASON_LOG.md` — Short log of what changed in each session/season and why.
- `drafts/` — Working chapter files (`ch01.md` ... `ch08.md`, `epilogue.md`, `appendix.md`) prior to publishing to the site.

## How to Start Any Session
1. Tell the agent to read `story-bible.md`, `editorial/LOOSE_ENDS.md`, and the target chapter/file.
2. Pick **one** small task (one loose end, one scene pass, or one outline).
3. Require the agent to state **what it will not touch** (e.g., *"Do not rewrite jokes, do not change character ages, do not add ideological speeches"*).
4. After reviewing the output, update `editorial/LOOSE_ENDS.md` and append a 3–5 line entry to `editorial/SEASON_LOG.md`.

## Working in "Seasons"
A **Season** is a small batch of focused sessions around one theme:
- **Season 1 — Mechanics & Loose Ends:** Close continuity gaps (`LOOSE_ENDS.md`) so the internal rules hold water.
- **Season 2 — Friction & Character Arcs:** Deepen human stakes (especially Mr. Thwaite, Gerald Pocock, and Ines's scaling question) without softening the humor.
- **Season 3 — Voice, Pacing & Appendix:** Tighten prose rhythm, check noticeboard/Pennyfeather threads, and draft `A Note on the Concepts`.
- **Season 4 — Polish & Release:** Final copyedit, link/anchor check for the static site, and publish.

## Mapping Sessions to Stafford Beer’s Viable System Model (VSM)
Use VSM as a **diagnostic lens for your editing workflow** (and lightly as background inspiration for how the village self-organizes—never as jargon spoken by characters):

- **System 1 (Operations — The Writing & Scene Work):** Drafting scenes, fixing a specific chapter, or resolving one item in `LOOSE_ENDS.md`. Keep each System 1 task small and self-contained.
- **System 2 (Coordination — Continuity & Cross-Chapter Sync):** Checking that a change in Chapter 3 or 5 doesn't clash with Chapter 2 or the Epilogue; keeping `story-bible.md` and `LOOSE_ENDS.md` in sync.
- **System 3 (Control / Resource Allocation — Scope & Pacing):** Deciding where word count, scene attention, or editing effort goes right now so you don't over-polish minor bits while ignoring weak scenes.
- **System 4 (Intelligence / Future & Adaptation — New Angles & Appendix):** Exploring "what if" variations, testing how `A Note on the Concepts` connects to the narrative, or planning the next Season.
- **System 5 (Identity / Policy — Story Bible & Voice):** Guarding the soul of *Lower Wobbling*—dry humor, British village texture, non-preachy realism, and Mrs. Prewitt's practical guardrails. Whenever an AI suggestion violates System 5, System 5 wins.

## Copy-Paste Prompt Template for an Agent
> Read `story-bible.md`, `editorial/LOOSE_ENDS.md`, and `editorial/AGENT_WORKFLOW.md`.
> Mode: [System 1 / System 2 / System 3 / System 4 / System 5].
> Task: Work ONLY on **[ID from LOOSE_ENDS.md or specific chapter/section]**.
> Constraints: Keep dry/understated British village tone; no speeches or neat moralizing; change only what serves this task and show a diff or clear before/after.
