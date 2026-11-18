---
name: SWMM Second Brain Mograph
file: swmm-second-brain-mograph.html
version: 1.0
date: 2026-11-16
author: Robert Dickinson
links: {netlify: not deployed yet, artifact: private claude.ai artifact, repo: none, subject: https://swmm-second-brain.netlify.app/}
engines: none. No engine runs in the film. It describes a wiki, not an engine.
units: not applicable (counts of files, pages and words)
ai_use: made with Claude (Anthropic); see AI use
---

# SWMM Second Brain Mograph: a 60-second film of the wonders of the SWMM Second Brain

## In three points
- **What:** A 60-second film, drawn by one function of time, showing five wonders of the SWMM Second Brain, a wiki of 366 pages compiled by an AI from 423 raw files that lists 87 questions it has not settled.
- **So what:** Every number on screen is traced: 8 settled frames hold 20 distinct numbers, all in the film's facts file; the page kinds (187 source pages, 101 entities, 76 concepts, 2 others) add to 366. The wiki has grown since: the README it read carried two counts from different moments (366 and 354).
- **Now what:** Use it as a one-minute introduction to the SWMM Second Brain; the Record button saves it as a WebM where the browser allows. No engine runs and no person has reviewed the film; its numbers came from a text reader's account of the live page, not from its source. The field of dots is a drawing, not the link graph.

## In one sentence
A 60-second film, drawn by one function of time, shows five wonders of the SWMM Second Brain, a wiki of 366 pages that an AI compiled from 423 raw files and that lists 87 questions it has not settled.

## In one paragraph
The SWMM Second Brain Mograph is a 60-second motion graphic about the SWMM Second Brain, Bob Dickinson's wiki of SWMM, ICM and his apps. The wiki is kept by Claude from raw sources under one schema file. The film is one JavaScript function that draws a 1920 by 1080 frame for any time t, so the page, the scrubber and the MP4 show the same pictures. Seven scenes cover the raw sources, the compiled pages, the three ways to use the repo, the list of open questions, and the site and its licenses. Every count comes from the public README. The field of linked dots is a drawing. The film shows no wiki content and does not vouch for any page.

## What is unique
As software this is not unique. It is the same kit as the SWMM 1 Engine and EXTRAN III mographs made the same day: a canvas, a clock and seven scenes. The subject is less common: a public wiki of one engineer's SWMM and ICM work, compiled by an AI from 423 raw files that are never edited, which publishes its own doubts, 87 open questions and 49 unreviewed pages. All 20 numbers on screen are from the repo's README. The film shows none of the wiki's content. For that, open the site.

## What it does
- Plays a 60-second motion graphic, 1920 x 1080, 30 frames a second, in 7 scenes.
- Subject: SWMM Second Brain (https://swmm-second-brain.netlify.app/; repo https://github.com/dickinsonre/swmm-second-brain), a wiki of Bob Dickinson's SWMM and ICM writing and apps, compiled by Claude from raw sources under a schema file.
- Outputs: the page (swmm-second-brain-mograph.html), an MP4 (swmm-second-brain-mograph.mp4, 1800 frames), a Word essay (SWMM-Second-Brain-Mograph.docx), this file.

| Scene | Seconds | Says |
|---|---|---|
| Opening | 0 to 6 | The site's name and its one-line description, over a made-up field of linked dots. |
| Wonder 1: raw sources go in and are never edited | 6 to 15 | About 1,330,000 words in 423 raw files; 187 ingested and 3 partly; hashes checked. |
| Wonder 2: an AI compiles them into 366 pages | 15 to 24 | 187 source pages, 101 entities, 76 concepts and 2 more; about 189,000 words. |
| Wonder 3: one schema file, three verbs | 24 to 32 | CLAUDE.md, and the three ways to use the repo: ingest, ask and lint. |
| Wonder 4: it keeps a list of what it does not know | 32 to 42 | 87 open questions, 8 settled, 49 pages unreviewed and 18 changed after review. |
| Wonder 5: read it, search it, check its work | 42 to 53 | The five tabs, 212 commits, 89 ontology statements and the two licenses. |
| Closing: what it does not claim, and credits | 53 to 60 | A notebook, not a reference; what was left out; credits; where to find it. |

## How it computes
- One pure function: `Film.draw(ctx, t, theme, facts)` (kit core.js + this film's src/scenes.js). Same t, same pixels. No clock, no random numbers, no state between calls.
- Scene lookup: the last scene whose start <= t; local time u = t - start.
- Easing: E(x) = 4x^3 for x < 0.5, else 1 - (2 - 2x)^3 / 2. One rolling counter = 1,330,000 * E((u - 1.2) / 5.2). Every other number appears whole.
- Scene fades: 0.35 s in, 0.3 s out; the closing scene holds.
- Illustrative field of dots (not the wiki's link graph): dot i at radius 46 sqrt(i + 0.5), angle 2.39996 i + 0.04u; links i to i + 8 and i + 13.
- Unit charts: one mark per raw file (423) and one ring per question (95), drawn to count.
- MP4: the same function called for t = k / 30, k = 0..1799, frames piped to ffmpeg (libx264, yuv420p).

## Inputs and outputs
- Input: src/facts.json only. It holds every number shown. No model files are read. No .inp is written.
- Numbers carried (all from the live page, read 2026-11-16):
  - Raw: 423 files, about 1,330,000 words; 187 ingested, 3 partly.
  - Wiki: 366 pages, about 189,000 words: 187 source pages, 101 entities, 76 concepts, an overview and an open-questions page. The README's AI-use section gives 354 pages as of 16 November 2026, an earlier count.
  - Open questions: 87 open, 8 settled. Review: 49 new pages marked reviewed: no; 18 changed after review.
  - Ontology draft: 89 statements in Relations tables on 3 pages. 212 commits on main.
  - Licenses: MIT for tools/; CC BY 4.0 for the wiki, the ontology and Bob's own writing in raw/.
  - Site tabs: Read, Search, Open questions, To review, About.

## Checks
Mechanical, run on this build (kit check.js, check_browser.py):
- The page kinds in `facts.json` (187 source pages, 101 entities, 76 concepts and 2 others) add to 366, and the 187 source pages equal the 187 ingested raw files.
- Scene lengths add to 60 s = 1800 frames; MP4 frame count after render: 1,800.
- Trace: 8 settled frames hold 20 distinct numbers; all 20 are in facts.json or the film's own short list.
- Determinism: 18 frames drawn twice in Chromium, identical pixel for pixel.
- Theme: dark and light show the same 108 strings.
- Fit: 601 frames sampled every 0.1 s, no text outside the 140 to 1780 px margins.
- Contrast: 34 pairs in both themes, lowest 3.26 to 1.
- Source size (plain pattern counts, not the Complexity Meter): 13 files, 938 lines, 206 functions, 217 decision points, most of it the kit shared by the mographs of the same day. No Meter index was computed (the analyzer could not be loaded in this session).
AI review: Claude looked at 12 rendered frames in both themes. Human review: none yet.

## What this does not show
1. No engine and no wiki content is in the film. The field of dots is a drawing, not the link graph.
2. Counts are from the repo README, not the Netlify site, whose pages the reader could not see. The README does not mention the site, so the two may differ.
3. The README carries two page counts from different moments (366 and 354); the wiki is moving.
4. The film inherits the wiki's own caution: a working notebook, not a reference; contradictions between sources stay open.
5. Numbers came from a text reader's account of the live page (read twice), not from its source. An error on the page or in the reading is repeated here.
6. The page's own layout is not shown; Claude never saw it.
7. Record button: not exercised for this film. The same Record code produced a 60-second, 1920 by 1080 WebM in headless Chromium for the SWMM 1 Engine Mograph. It has not been tried in a person's browser or inside the claude.ai viewer.

## How to reproduce
```
node ../mgkit/build.js --draft && node ../mgkit/check.js && python3 ../mgkit/check_browser.py
python3 ../mgkit/render.py && node ../mgkit/stats.js && node ../mgkit/build.js && node ../mgkit/docx.js
```

## Credits and licenses
- The LLM wiki pattern: Andrej Karpathy (credited in the repo README).
- SWMM Second Brain: every source and the decisions by Robert (Bob) Dickinson; schema, tools and wiki pages written by Claude (Anthropic) at his direction; ChatGPT and Grok suggested changes to the tools.
- Fonts: Latin Modern (GUST Font License), Inter (SIL OFL 1.1), embedded as subsets.
- More of Bob's SWMM work: https://swmm5.ai

## AI use
This film and its page were made with Claude Fable 5.2, Anthropic's AI model, in one session on November 16, 2026, at the request of Robert (Bob) Dickinson. He chose the subject and directed the SWMM Second Brain that the film describes. Responsibility for publishing the film is his. Claude is not an author of it.

What Claude did. It read the live page with a text reader, chose the seven scenes, and wrote the film code, the page, this essay, the technical summary and the Word file. It rendered the MP4 frame by frame, wrote and ran the checks, and looked at 12 rendered frames.

How it was checked. The checks are mechanical: the page kinds add to 366 and the source pages equal the 187 ingested files; all 20 numbers on screen trace to the facts file; 18 frames drawn twice were identical; both themes show the same 108 strings; no text crosses the margins in 601 sampled frames.

What no person has checked. Nobody has yet watched the film or compared its numbers with the live page by eye. The numbers came from a text reader's account of the page, read twice. Bob should check each one against the page before posting.

## Changes
`1.0 (2026-11-16)`: first version. Seven scenes, Doc and About tabs, MP4, .docx, .md.
