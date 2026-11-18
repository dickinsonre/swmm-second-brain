---
name: SWMM 1 Engine Mograph
file: swmm1-engine-mograph.html
version: 1.0
date: 2026-11-16
author: Robert Dickinson
links: {netlify: not deployed yet, artifact: https://claude.ai/artifact/RQKqrrHDTQBgzPcfGgQsCH, repo: none, subject_app: https://swmm1-engine-imports-swmm5.netlify.app/}
engines: none. No engine runs in the film. It describes SWMM 1 Engine v3.13.
units: US customary (cfs, ft, lb, minutes)
ai_use: made with Claude (Anthropic); see AI use
---

# SWMM 1 Engine Mograph: a 60-second film of the wonders of the SWMM 1 Engine

## In three points
- **What:** A 60-second film, drawn by one function of time, showing five wonders of the SWMM 1 Engine, the 1971 program rebuilt from 12,200 printed cards, using only numbers taken from the app's own pages.
- **So what:** Every number on screen is traced: 9 settled frames hold 43 distinct numbers, all in the film's facts file, and the block counts add to the app's 12,200. The Record button produced a 60-second, 1920 by 1080 WebM of 16.9 MB in headless Chromium.
- **Now what:** Use it as a one-minute introduction to the SWMM 1 Engine; the Record button saves it as a WebM where the browser allows. No engine runs and no person has reviewed the film; its numbers came from a text reader's account of the live page, not from its source. Cards, printout and hydrograph are drawings.

## In one sentence
A 60-second film, drawn by one function of time, shows five wonders of the SWMM 1 Engine, the 1971 program rebuilt from 12,200 printed cards, using only numbers taken from the app's own pages.

## In one paragraph
The SWMM 1 Engine Mograph is a 60-second motion graphic about the SWMM 1 Engine, the browser app that runs the 1971 Storm Water Management Model from a retyped listing. The film is one JavaScript function that draws a 1920 by 1080 frame for any time t, so the page, the scrubber and the MP4 all show the same pictures. Seven scenes cover the paper listing, the five blocks, the WebAssembly build, the SWMM 5 import and the score against the numbers printed in 1971. Every number on screen comes from the app's pages. The cards, the printout and the one hydrograph are drawings. No engine runs in the film, and it proves nothing about the engine.

## What is unique
As software this is not unique. A motion graphic of a web app is a common thing, and this one is a canvas, a clock and seven scenes, the same pattern as the two earlier mographs in this series (SWMM5 / SWMM6 and hydrocouple.org). What it carries is less common. All 43 numbers on screen are read from the SWMM 1 Engine's own pages, none is rounded for effect, and the film spends its last scene on what the app does not claim. It is also the first film in the series about a reconstructed engine. No engine runs in it. For that, open the app.

## What it does
- Plays a 60-second motion graphic, 1920 x 1080, 30 frames a second, in 7 scenes.
- Subject: SWMM 1 Engine v3.13 (https://swmm1-engine-imports-swmm5.netlify.app/), the 1971 Storm Water Management Model (EPA 11024 DOC 10/71) rebuilt from the printed listing and run as WebAssembly.
- Outputs: the page (swmm1-engine-mograph.html), an MP4 (swmm1-engine-mograph.mp4, 1800 frames), a Word essay (SWMM1-Engine-Mograph.docx), this file.

| Scene | Seconds | Says |
|---|---|---|
| Opening | 0 to 6 | The report number, a punch card carrying the film's title, and the app's name. |
| Wonder 1: it survived only on paper | 6 to 15 | 248 pages became 12,200 card images; 10,889 were typed again from the scan by a trained reader. |
| Wonder 2: five blocks, one tape | 15 to 24 | Card counts for Executive, Runoff, Transport, Storage and Receiving Water, and the tape that links them. |
| Wonder 3: it runs in your browser | 24 to 32 | Listing to f2c to C to WebAssembly; three engines; a run in a few milliseconds. |
| Wonder 4: a SWMM 5 file becomes a 1971 deck | 32 to 41 | A SWMM 5 file becomes a 1971 deck, with three checks on every import. |
| Wonder 5: scored against 1971, and one mystery | 41 to 53 | Six scores against 1971, then the Baker Street BOD gap and card TRAN346. |
| Closing: what it does not claim, and credits | 53 to 60 | What no person has checked, the 1971 and 2026 credits, and where to run it. |

## How it computes
- One pure function: `Film.draw(ctx, t, theme, facts)` in src/film.js. Same t, same pixels. No clock, no random numbers, no state between calls.
- Scene lookup: the last scene whose start <= t; local time u = t - start.
- Easing: E(x) = 4x^3 for x < 0.5, else 1 - (2 - 2x)^3 / 2. Card counter = 12,200 * E((u - 1.2) / 5.2).
- Scene fades: 0.35 s in, 0.3 s out; the closing scene holds.
- Illustrative hydrograph (not engine output): q = 30 x^2 e^(2(1 - x)) cfs, x = t / 25 min; peak 30 cfs at 25 min.
- MP4: the same function called for t = k / 30, k = 0..1799, frames piped to ffmpeg (libx264, yuv420p).

## Inputs and outputs
- Input: src/facts.json only. It holds every number shown. No model files are read. No .inp is written.
- Numbers carried (all from the app's pages, read 2026-11-16):
  - 248 pages, 235 of listing; 12,200 card images; 65 program units; 5 blocks.
  - Cards per block: Executive 66 cards, plus 323 for plotting; Runoff 1,311; Transport 4,114; Storage 3,918; Receiving Water 2,468.
  - 10,889 cards retyped from the scan; 154,000 training characters; 98 to 99.9% character accuracy on held-out pages.
  - Checks: Receiving Water estuary stages 52 of 52 (within 0.004 ft on a 4.8 ft tide); Wingohocking dry-weather flows 51 of 51 (every subarea flow identical); Kingman Lake design numbers 53 of 55 (identical, storm-independent numbers); Baker Street flows and costs 88 of 95 (identical; six cost totals off by $4, one cost by $1); Transport example hydrographs 6 of 10 (to 0.001 cfs; the other 4 within 0.4%); Native build against WebAssembly 21,804 of 21,804 (printed numbers, byte-identical).
  - Baker Street BOD: printed 70,998 lb, engine 2,164 lb; card TRAN346 divides by 60 (the app's hypothesis, supported only at the storm peak).
  - 17 doubtful readings; 5 repaired cards (off by default in the app).

## Checks
Mechanical, run on this build (tools/check.js, tools/check_browser.py):
- Block counts add to 12,200 = the app's total.
- Scene lengths add to 60 s = 1800 frames; MP4 frame count after render: 1,800.
- Trace: 9 settled frames hold 43 distinct numbers; all 43 are in facts.json or the film's own short list.
- Determinism: 18 frames drawn twice in Chromium, identical pixel for pixel.
- Theme: dark and light show the same 158 strings.
- Fit: 601 frames sampled every 0.1 s, no text outside the 140 to 1780 px margins.
- Contrast: 34 pairs in both themes, lowest 3.26 to 1.
- Source size (plain pattern counts, not the Complexity Meter): 11 files, 1,006 lines, 200 functions, 209 decision points. No Meter index was computed (the analyzer could not be loaded in this session).
AI review: Claude looked at 28 rendered frames in both themes. Human review: none yet.

## What this does not show
1. No engine runs. Cards, printout and hydrograph are drawings; the hydrograph is a formula.
2. Numbers came from a text reader's account of the live page (read twice), not from the app's source. An error on the page or in the reading is repeated here.
3. The app's screen layout is not shown; Claude never saw it.
4. The film inherits the app's limits: 10,889 retyped cards not read by a person, 17 doubtful readings, single precision (3 to 4 digits, not 6).
5. Record button: exercised once in headless Chromium, where it produced a 60-second, 1920 by 1080 WebM of 16.9 MB. It has not been tried in a person's browser or inside the claude.ai viewer, where a save needs the viewer's permission.
6. Not affiliated with or endorsed by the U.S. EPA or the 1971 authors.

## How to reproduce
```
node tools/build.js --draft && node tools/check.js && python3 tools/check_browser.py
python3 tools/render.py && node tools/build.js && node tools/docx.js
```

## Credits and licenses
- SWMM 1 (1971): Metcalf & Eddy, University of Florida, Water Resources Engineers, for the U.S. EPA (report EPA 11024 DOC 10/71).
- SWMM 1 Engine v3.13: directed by Robert (Bob) Dickinson, built with Claude (Anthropic).
- Fonts: Latin Modern (GUST Font License), Inter (SIL OFL 1.1), embedded as subsets.
- More of Bob's SWMM work: https://swmm5.ai

## AI use
This film and its page were made with Claude Fable 5.2, Anthropic's AI model, in one session on November 16, 2026, at the request of Robert (Bob) Dickinson. He chose the subject and directed the SWMM 1 Engine that the film describes. Responsibility for publishing the film is his. Claude is not an author of it.

What Claude did. It read the app's live page with a text reader, chose the seven scenes, and wrote the film code, the page, this essay, the technical summary and the Word file. It rendered the MP4 frame by frame, wrote and ran the checks, and looked at 28 rendered frames.

How it was checked. The checks are mechanical: the block counts add to 12,200; all 43 numbers on screen trace to the facts file; 18 frames drawn twice were identical; both themes show the same 158 strings; no text crosses the margins in 601 sampled frames.

What no person has checked. Nobody has yet watched the film or compared its numbers with the app by eye. The numbers came from a text reader's account of the page, read twice. Bob should check each one against the app before posting.

## Changes
`1.0 (2026-11-16)`: first version. Seven scenes, Doc and About tabs, MP4, .docx, .md.
