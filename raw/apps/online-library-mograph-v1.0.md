---
name: Online Library Mograph
file: online-library-mograph.html
version: 1.0
date: 2026-11-16
author: Robert Dickinson
links: {netlify: not deployed yet, artifact: private claude.ai artifact, repo: none, subject: https://robert-dickinson-online-library.netlify.app/}
engines: none. No engine runs in the film. It describes a catalog, not an engine.
units: not applicable (counts of records, links and megabytes)
ai_use: made with Claude (Anthropic); see AI use
---

# Online Library Mograph: a 60-second film of the wonders of the SWMM & ICM Knowledge Library

## In three points
- **What:** A 60-second film, drawn by one function of time, showing five wonders of Robert Dickinson's SWMM & ICM Knowledge Library: one HTML file of 9,889 catalog records and 2,909 links that reaches back to 1980.
- **So what:** Every number on screen is traced: 8 settled frames hold 39 distinct numbers, all found in the film's facts file; the 25 kinds of record add to 9,889, and the 135 threads started and 2,744 answered add to the 2,879 OpenSWMM.org threads. 18 frames drawn twice are identical pixel for pixel.
- **Now what:** Use it as a one-minute introduction to the Knowledge Library; the Record button saves it as a WebM where the browser allows. No engine runs and no person has reviewed the film; its numbers came from a text reader's account of the live page, not from its source. Its counts are from the library's chart of 20 October 2026.

## In one sentence
A 60-second film, drawn by one function of time, shows five wonders of Robert Dickinson's SWMM & ICM Knowledge Library, one HTML file of 9,889 catalog records and 2,909 links that reaches back to 1980.

## In one paragraph
The Online Library Mograph is a 60-second motion graphic about Robert Dickinson's SWMM & ICM Knowledge Library, a catalog of his writing, apps and code that runs as one HTML file with no server. The film is one JavaScript function that draws a 1920 by 1080 frame for any time t, so the page, the scrubber and the MP4 show the same pictures. Seven scenes cover the 9,889 records, the kinds they fall into, the years they span, the search, and how 185 MB of images became 2.9 MB. Every number on screen comes from the library's page. The shelf and the cards are drawings. The film shows no record and does not check any link.

## What is unique
As software this is not unique. It is the same kit as the three other mographs made the same day: a canvas, a clock and seven scenes. What it does differently is draw its subject to count. The first wonder puts 9,889 small squares on screen, one for each record in Robert Dickinson's SWMM & ICM Knowledge Library, coloured by kind, so the proportions cannot be dressed up. All 39 numbers on screen are read from the library's own page. No record of the library is shown. For that, open the library.

## What it does
- Plays a 60-second motion graphic, 1920 x 1080, 30 frames a second, in 7 scenes.
- Subject: Robert Dickinson's SWMM & ICM Knowledge Library (https://robert-dickinson-online-library.netlify.app/), a single HTML file of about 8.5 MB rebuilt from his Replit app's export of 20 October 2026.
- Outputs: the page (online-library-mograph.html), an MP4 (online-library-mograph.mp4, 1800 frames), a Word essay (Online-Library-Mograph.docx), this file.

| Scene | Seconds | Says |
|---|---|---|
| Opening | 0 to 6 | The library's name over a shelf of cards drawn for the film. |
| Wonder 1: 9,889 records in one file | 6 to 15 | One square per record, 2,909 distinct links, about 8.5 MB, 18 tabs. |
| Wonder 2: mostly answers to other people | 15 to 24 | The eight largest kinds of record and the 17 others, to one scale. |
| Wonder 3: it reaches back to 1980 | 24 to 33 | A time line from 1980 to 2026, and 2,744 forum threads answered against 135 started. |
| Wonder 4: one search box, and cards that suggest more | 33 to 42 | Search across ten kinds, filters, related items and an assistant that cites records. |
| Wonder 5: small enough to carry | 42 to 53 | 139 images at 185 MB as PNG and 2.9 MB as WebP; 42 of 73 papers confirmed; no server. |
| Closing: what it does not claim, and credits | 53 to 60 | Links not rechecked, records not full text, credits, and where to open it. |

## How it computes
- One pure function: `Film.draw(ctx, t, theme, facts)` (kit core.js + this film's src/scenes.js). Same t, same pixels. No clock, no random numbers, no state between calls.
- Scene lookup: the last scene whose start <= t; local time u = t - start.
- Easing: E(x) = 4x^3 for x < 0.5, else 1 - (2 - 2x)^3 / 2. One rolling counter = 9,889 * E((u - 1.2) / 5.2). Every other number appears whole.
- Scene fades: 0.35 s in, 0.3 s out; the closing scene holds.
- Unit chart: one 4 px square per record, 132 to a row, 9,889 in all, revealed in step with the rolling counter.
- Illustrative shelf, cards and search query (not library content).
- MP4: the same function called for t = k / 30, k = 0..1799, frames piped to ffmpeg (libx264, yuv420p).

## Inputs and outputs
- Input: src/facts.json only. It holds every number shown. No model files are read. No .inp is written.
- Numbers carried (all from the live page, read 2026-11-16):
  - 9,889 records, 2,909 distinct links, 18 tabs, about 8.5 MB, no server; export of 20 October 2026.
  - Records by kind: LinkedIn comments 4,398; OpenSWMM.org threads 2,879; swmm5.org posts 1,327; Netlify apps 171; LinkedIn articles 162; MyBlogspot posts 145; SWMMEnablement repos 89; Replit apps 85; Reposts 82; External papers 73; Newsletters 65; LinkedIn posts 65; Gists 64; dickinsonre repos 57; Tools 45; SWMMBobSWMM6 repos 35; Quiz questions 30; NS Apps repos 29; SWMM group posts 22; Documents 20; Components 18; Featured apps 15; Lovable apps 5; CIMM-ORG repos 4; Learning paths 4.
  - OpenSWMM.org: 135 threads started, 2,744 answered; his oldest thread is from February 1995.
  - Reach: papers 1980 to 2025; swmm5.org posts from 2009, 406 of them in 2013; LinkedIn comments from September 2016.
  - Papers: 42 of 73 confirmed on a publisher, CHI, EPA or archive page or in a CV. Images: 139, 185 MB as PNG, 2.9 MB as WebP.
  - Derived in the film: 17 kinds after the eight largest hold 9,889 - 9,256 = 633 records; 22 kinds after the three largest.

## Checks
Mechanical, run on this build (kit check.js, check_browser.py):
- The 25 kinds of record in `facts.json` add to 9,889; the threads started and answered (135 and 2,744) add to the 2,879 OpenSWMM.org threads; and the 17 smaller kinds add to the 633 shown as one bar.
- Scene lengths add to 60 s = 1800 frames; MP4 frame count after render: 1,800.
- Trace: 8 settled frames hold 39 distinct numbers; all 39 are in facts.json or the film's own short list.
- Determinism: 18 frames drawn twice in Chromium, identical pixel for pixel.
- Theme: dark and light show the same 117 strings.
- Fit: 601 frames sampled every 0.1 s, no text outside the 140 to 1780 px margins.
- Contrast: 34 pairs in both themes, lowest 3.26 to 1.
- Source size (plain pattern counts, not the Complexity Meter): 13 files, 932 lines, 214 functions, 209 decision points, most of it the kit shared by the mographs of the same day. No Meter index was computed (the analyzer could not be loaded in this session).
AI review: Claude looked at 12 rendered frames in both themes. Human review: none yet.

## What this does not show
1. No library record is shown. The shelf, cards and search query are drawings.
2. Counts are from the library's chart (export of 20 October 2026); its home page shows a slightly different snapshot from 1 November 2026.
3. The film inherits the library's limits: catalog records and links, not full text; 2,909 links not rechecked by a person; the assistant's answers unreviewed.
4. Numbers came from a text reader's account of the live page (read twice), not from its source. An error on the page or in the reading is repeated here.
5. The page's own layout is not shown; Claude never saw it.
6. Record button: not exercised for this film. The same Record code produced a 60-second, 1920 by 1080 WebM in headless Chromium for the SWMM 1 Engine Mograph. It has not been tried in a person's browser or inside the claude.ai viewer.

## How to reproduce
```
node ../mgkit/build.js --draft && node ../mgkit/check.js && python3 ../mgkit/check_browser.py
python3 ../mgkit/render.py && node ../mgkit/stats.js && node ../mgkit/build.js && node ../mgkit/docx.js
```

## Credits and licenses
- SWMM & ICM Knowledge Library: Robert (Bob) Dickinson built the original Replit app and directed the single-file copy; Claude (Anthropic) built the copy and wrote its essay.
- Fonts: Latin Modern (GUST Font License), Inter (SIL OFL 1.1), embedded as subsets.
- More of Bob's SWMM work: https://swmm5.ai

## AI use
This film and its page were made with Claude Fable 5.2, Anthropic's AI model, in one session on November 16, 2026, at the request of Robert (Bob) Dickinson. He chose the subject and directed the SWMM & ICM Knowledge Library that the film describes. Responsibility for publishing the film is his. Claude is not an author of it.

What Claude did. It read the live page with a text reader, chose the seven scenes, and wrote the film code, the page, this essay, the technical summary and the Word file. It rendered the MP4 frame by frame, wrote and ran the checks, and looked at 12 rendered frames.

How it was checked. The checks are mechanical: the 25 kinds add to 9,889 and the threads started and answered add to 2,879; all 39 numbers on screen trace to the facts file; 18 frames drawn twice were identical; both themes show the same 117 strings; no text crosses the margins in 601 sampled frames.

What no person has checked. Nobody has yet watched the film or compared its numbers with the live page by eye. The numbers came from a text reader's account of the page, read twice. Bob should check each one against the page before posting.

## Changes
`1.0 (2026-11-16)`: first version. Seven scenes, Doc and About tabs, MP4, .docx, .md.
