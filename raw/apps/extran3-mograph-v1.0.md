---
name: EXTRAN III Mograph
file: extran3-mograph.html
version: 1.0
date: 2026-11-16
author: Robert Dickinson
links: {netlify: not deployed yet, artifact: private claude.ai artifact, repo: none, subject: https://extran3-alive-again.netlify.app/}
engines: none. No engine runs in the film. It describes EXTRAN III Workbench v1.6.0.
units: US customary (ft)
ai_use: made with Claude (Anthropic); see AI use
---

# EXTRAN III Mograph: a 60-second film of the wonders of the EXTRAN III Workbench

## In three points
- **What:** A 60-second film, drawn by one function of time, showing five wonders of the EXTRAN III Workbench, the 1981 CDM program rebuilt from 2,998 scanned lines and scored against its own printed output.
- **So what:** Every number on screen is traced: 8 settled frames hold 66 distinct numbers, all in the film's facts file; the three repair grades (1,289, 133 and 3) add to 1,425 and the four corpus counts to 257.
- **Now what:** Use it as a one-minute introduction to the EXTRAN III Workbench; the Record button saves it as a WebM where the browser allows. No engine runs and no person has reviewed the film; its numbers came from a text reader's account of the live page, not from its source. It inherits the Workbench's limits: the score covers only the code paths of the seven 1981 examples.

## In one sentence
A 60-second film, drawn by one function of time, shows five wonders of the EXTRAN III Workbench, the 1981 CDM program rebuilt from 2,998 scanned lines and scored against its own printed output.

## In one paragraph
The EXTRAN III Mograph is a 60-second motion graphic about the EXTRAN III Workbench, the browser app that runs Camp Dresser & McKee's 1981 Extended Transport program from its printed listing. The film is one JavaScript function that draws a 1920 by 1080 frame for any time t, so the page, the scrubber and the MP4 show the same pictures. Seven scenes cover the scanned listing and its repairs, the four engines, the score against the 1981 printout, the ten bugs, and 257 SWMM 5 models converted back to 1981. Every number on screen comes from the app's page. The listing lines and the surcharge wave are drawings. No engine runs in the film, and it proves nothing about the engine.

## What is unique
As software this is not unique. It is the same kit as the SWMM 1 Engine Mograph made the same day: a canvas, a clock and seven scenes. What it carries is the EXTRAN III Workbench's own evidence, 66 numbers read from its live page and shown as counted. The film puts the engine's two faces side by side: the listing as printed, which gives 0.53 ft at one outfall, and the listing with ten bugs fixed, which gives 2.51 ft. It closes on what the app does not claim. No engine runs in the film. For that, open the app.

## What it does
- Plays a 60-second motion graphic, 1920 x 1080, 30 frames a second, in 7 scenes.
- Subject: EXTRAN III Workbench v1.6.0 (https://extran3-alive-again.netlify.app/), Camp Dresser & McKee's 1981 Extended Transport program rebuilt from its printed listing and run as WebAssembly.
- Outputs: the page (extran3-mograph.html), an MP4 (extran3-mograph.mp4, 1800 frames), a Word essay (EXTRAN3-Mograph.docx), this file.

| Scene | Seconds | Says |
|---|---|---|
| Opening | 0 to 6 | The compiler stamp, a sheet of listing paper, and the app's name. |
| Wonder 1: a scan with errors in nearly half its lines | 6 to 15 | 1,425 of 2,998 lines repaired, graded 1,289 sure, 133 likely and 3 guesses. |
| Wonder 2: four engines in one browser tab | 15 to 23 | Listing to f2c to C to clang to WebAssembly; as printed, fixed, enlarged, and SWMM 5.2.4. |
| Wonder 3: scored against the 1981 printout | 23 to 32 | 2,253 of 2,424 printed values exact, and the share for each of the seven examples. |
| Wonder 4: ten bugs, 45 years old | 32 to 43 | The ten bug labels, the 0.677 exponent, and outfall 10208 three ways. |
| Wonder 5: SWMM 5 models go back to 1981 | 43 to 53 | 257 models as dots, how each fared, and the median depth difference before and after the fixes. |
| Closing: what it does not claim, and credits | 53 to 60 | The 139 doubtful lines, the 1981 and 2026 credits, and where to run it. |

## How it computes
- One pure function: `Film.draw(ctx, t, theme, facts)` (kit core.js + this film's src/scenes.js). Same t, same pixels. No clock, no random numbers, no state between calls.
- Scene lookup: the last scene whose start <= t; local time u = t - start.
- Easing: E(x) = 4x^3 for x < 0.5, else 1 - (2 - 2x)^3 / 2. One rolling counter = 1,425 * E((u - 1.2) / 5.2). Every other number appears whole.
- Scene fades: 0.35 s in, 0.3 s out; the closing scene holds.
- Illustrative surcharge wave (not engine output): depth in manhole i = 16 + 170 e^(-q^2 / 0.9) px, q = ((1.1u - i) mod 5) - 1.2.
- Illustrative OCR lines: seven made-up FORTRAN lines whose look-alike characters flip every 0.3 s.
- MP4: the same function called for t = k / 30, k = 0..1799, frames piped to ffmpeg (libx264, yuv420p).

## Inputs and outputs
- Input: src/facts.json only. It holds every number shown. No model files are read. No .inp is written.
- Numbers carried (all from the live page, read 2026-11-16):
  - Listing: 2,998 lines, 15 program units, 62 pages (167 to 228), compiler stamp 20-MAY-81, DEC-20.
  - Repairs: 1,425 lines; 1,289 sure, 133 likely, 3 guesses; 27 further port edits; 139 doubtful lines unchecked.
  - Score against 1981 print: 2,253 of 2,424 exact (92.9%); 98.4% allowing last-digit and OCR-type differences; 39 mismatches, 20 of them peak times.
  - By example, exact: Basic pipe system 93.7% of 1,356; Tide gate 95.1% of 164; Sump orifice 91.1% of 180; Weir diversion 89.4% of 188; Storage + side orifice 89.2% of 176; Off-line pump 94.1% of 188; In-line pump 93.0% of 172.
  - Ten bugs: DEPTHX 95, DEPTHX 96-97, DEPTHX 56, HEAD 86, HYDRAD 45, TRANSX 340, TRANSX 459, BOUND 229, BOUND 234, OUTPUT 62. Manning exponent 0.677 where 2/3 belongs.
  - Example 1 outfall 10208 peak depth: 0.53 ft as printed, 2.51 ft fixed, 2.53 ft in SWMM 5.2.4.
  - Corpus: 257 SWMM 5 models; 207 ran both engines, 34 too large (1981 limit 187 junctions; 16 run in the 5,000-junction build), 10 SWMM 5.2.4 could not run, 6 not converted.
  - Median peak-depth difference from SWMM 5.2.4 over 203 models: 0.48 ft as printed, 0.11 ft fixed.

## Checks
Mechanical, run on this build (kit check.js, check_browser.py):
- The three repair grades in `facts.json` (1,289, 133 and 3) add to 1,425, and the four corpus counts (207, 34, 10 and 6) add to 257.
- Scene lengths add to 60 s = 1800 frames; MP4 frame count after render: 1,800.
- Trace: 8 settled frames hold 66 distinct numbers; all 66 are in facts.json or the film's own short list.
- Determinism: 18 frames drawn twice in Chromium, identical pixel for pixel.
- Theme: dark and light show the same 140 strings.
- Fit: 601 frames sampled every 0.1 s, no text outside the 140 to 1780 px margins.
- Contrast: 34 pairs in both themes, lowest 3.26 to 1.
- Source size (plain pattern counts, not the Complexity Meter): 13 files, 967 lines, 215 functions, 214 decision points, most of it the kit shared by the mographs of the same day. No Meter index was computed (the analyzer could not be loaded in this session).
AI review: Claude looked at 12 rendered frames in both themes. Human review: none yet.

## What this does not show
1. No engine runs. The FORTRAN lines and the surcharge wave are drawings.
2. The film inherits the app's limits: the score covers only the code paths of the seven 1981 examples; 139 doubtful lines are unconfirmed; SWMM 5 is a different program, not ground truth; comparisons test routing, not hydrology.
3. Not affiliated with or endorsed by the 1981 authors, their firm or the U.S. EPA.
4. Numbers came from a text reader's account of the live page (read twice), not from its source. An error on the page or in the reading is repeated here.
5. The page's own layout is not shown; Claude never saw it.
6. Record button: not exercised for this film. The same Record code produced a 60-second, 1920 by 1080 WebM in headless Chromium for the SWMM 1 Engine Mograph. It has not been tried in a person's browser or inside the claude.ai viewer.

## How to reproduce
```
node ../mgkit/build.js --draft && node ../mgkit/check.js && python3 ../mgkit/check_browser.py
python3 ../mgkit/render.py && node ../mgkit/stats.js && node ../mgkit/build.js && node ../mgkit/docx.js
```

## Credits and licenses
- EXTRAN III (1981): Camp Dresser & McKee; Larry A. Roesner, Robert P. Shubinski, John A. Aldrich. Original San Francisco model: Water Resources Engineers. SWMM and EXTRAN: U.S. EPA.
- EXTRAN III Workbench v1.6.0: directed by Robert (Bob) Dickinson, built with Claude (Anthropic).
- Fonts: Latin Modern (GUST Font License), Inter (SIL OFL 1.1), embedded as subsets.
- More of Bob's SWMM work: https://swmm5.ai

## AI use
This film and its page were made with Claude Fable 5.2, Anthropic's AI model, in one session on November 16, 2026, at the request of Robert (Bob) Dickinson. He chose the subject and directed the EXTRAN III Workbench that the film describes. Responsibility for publishing the film is his. Claude is not an author of it.

What Claude did. It read the live page with a text reader, chose the seven scenes, and wrote the film code, the page, this essay, the technical summary and the Word file. It rendered the MP4 frame by frame, wrote and ran the checks, and looked at 12 rendered frames.

How it was checked. The checks are mechanical: the repair grades add to 1,425 and the corpus counts add to 257; all 66 numbers on screen trace to the facts file; 18 frames drawn twice were identical; both themes show the same 140 strings; no text crosses the margins in 601 sampled frames.

What no person has checked. Nobody has yet watched the film or compared its numbers with the live page by eye. The numbers came from a text reader's account of the page, read twice. Bob should check each one against the page before posting.

## Changes
`1.0 (2026-11-16)`: first version. Seven scenes, Doc and About tabs, MP4, .docx, .md.
