---
name: Modeling Confluence Mograph
file: modeling-confluence-mograph.html
version: 1.0
date: 2026-11-18
author: Robert Dickinson
links: {netlify: none yet, artifact: https://claude.ai/artifact/TWCK37t5UnwWevhs65cyqn, repo: none}
engines: none (a drawing; no SWMM or other engine)
units: time in seconds; film coordinates in pixels on a 1920 by 1080 frame
ai_use: built with Claude (Anthropic); see AI use
---

# Modeling Confluence Mograph: a 44-second film of the EWRI Modeling Confluence Conference 2027 call for abstracts

**In one sentence.** A 44-second, six-scene motion graphic of the call for abstracts for the EWRI Modeling Confluence Conference 2027, drawn in code from the conference's own pages, with abstracts due December 9, 2026, not 2027 as the post said.

**In one paragraph.** The Modeling Confluence Mograph is a 44-second, six-scene motion graphic of the call for abstracts for the EWRI Modeling Confluence Conference, August 8 to 11, 2027, in Reston, Virginia. A single function draws each of its 1,320 frames from a time and a small file of facts read from the conference's own pages, so the player in the page and the MP4 are the same film. A checking program drew every frame in two themes, found no text outside the frame, and traced all 99 strings on screen to their source. The post that prompted it gave the deadline as December 9, 2027. The site says December 9, 2026, and the film follows the site. It is unofficial and no person has reviewed it yet.

## What it does
Plays a six-scene motion graphic (44 s, 30 fps, 1,320 frames, 1920 by 1080, silent) built from a LinkedIn post Bob supplied and the conference's own pages. Scenes: The question (0 to 5.5 s); The conference (5.5 to 12.5 s); Four tracks (12.5 to 23.5 s); What to send (23.5 to 30.5 s); Key dates (30.5 to 38 s); The deadline (38 to 44 s). The page also lists every fact with its source and carries the Doc essay. Audience: modelers deciding whether to submit an abstract.

## How it computes
- One function, `render(t, ctx)` in `src/film.js`, draws the whole frame for time t. No state between frames, no wall clock, no unseeded random numbers (the 250 word bars use a fixed-seed generator).
- Player: t advances with requestAnimationFrame. Renderer: t = f / 30 for f = 0 to 1,319, in headless Chromium; JPEG frames (quality 0.92) piped to ffmpeg, libx264, CRF 18, yuv420p; one file per scene, joined with the concat demuxer and `-c copy`.
- Stream curve, before the confluence at Xc = 1010 px: y(x) = y0 + (Yc - y0) * S(x / Xc), S(u) = 6u^5 - 15u^4 + 10u^3, plus a small sine wobble that fades to zero at Xc. After Xc the four strands run 11 px apart.
- Key dates are placed by day count from December 9, 2026 over a 245-day span. Mid-January is placed at January 15 with a hollow marker.
- All conference text comes from `src/facts.json`.

## Inputs and outputs
- In: `src/facts.json` (read from the sources below on November 18, 2026).
- Out: `modeling-confluence-mograph.html` (single file), `modeling-confluence-mograph.mp4` (7,769,590 bytes, h264, yuv420p), `modeling-confluence-mograph.docx`, `modeling-confluence-mograph.md`.

## Facts shown
- EWRI Modeling Confluence Conference 2027; Water Modeling Together! At the confluence of water systems, technology, and community; August 8–11, 2027; ASCE World Headquarters, Reston, Virginia.
- Dates: Abstracts due: December 9, 2026 (11:59 pm EST); Speaker notifications: Mid-January 2027; Paper deadline: February 17, 2027 (optional); Speaker registration: March 3, 2027; Conference: August 8–11, 2027 (Reston, Virginia).
- Tracks and topics:
  - Collection Systems: Asset Management, Rehabilitation, & Resilience; Combined and Sanitary Sewer Overflows, and Inflow & Infiltration; Hydraulics & Hydrology; Real-Time Control & Optimization
  - Cross-Cutting Innovation, Technology, & Practice: AI, Machine Learning, & Digital Twins; Model Development, Calibration, & Validation; Uncertainty Analysis & Risk-Based Decision-Making; Data Readiness, Quality, & GIS Integration
  - Environmental Systems: Coastal Systems & Storm Surge; Compound Flooding & Climate Impacts; Green Infrastructure & Nature-Based Solutions; Sediment Transport & Water Quality
  - Water Distribution Systems: Hydraulics & Water Quality; Leakage, Water Loss, & Pressure Management; Lead Service Line Replacement & Water Main Renewal; Pumping & Energy Efficiency
- Abstract: One paragraph, about 250 words; Your own work (No lists, tables, figures, equations, footnotes or references); Up to 2 abstracts per presenter; Oral presentations only (There is no poster hall); A full paper is optional (5 to 15 pages, due February 17, 2027).
- Submission address: https://modelingcon.asce.org/call-abstracts
- The post gave the deadline as December 9, 2027. The conference site gives December 9, 2026. The film uses the site's date.

## Checks
Mechanical, by `tools/check.js` on 2026-11-18:
- Frames drawn, each theme: 1,320
- Pieces of text drawn, both themes: 50,546
- Pieces of text outside the safe margin: 0
- Smallest type, pixels on a 1080 frame: 19
- Distinct strings on screen: 99
- Copied whole from the facts file: 46
- Pieces of facts-file values: 40
- The film's own words: 13
- Frames identical when drawn twice: 6 of 6
- Lowest color contrast, to 1: 4.58
- Calendar offsets recomputed and equal: 5 of 5
- MP4 frames, seconds, MB: 1,320, 44, 7.8
- December 9, 2027 is 120 days after the conference closes; December 9, 2026 is 242 days before it opens.

By AI review: Claude looked at nine still frames at full size and two frames taken back out of the MP4. By human review: none yet.

Complexity: no index against HydroCouple = 100; the Meter's analyzer could not be run in this build. Raw counts: 12 hand-written source files, 1,028 lines, 198 functions.

## What this does not show
- Unofficial; not reviewed or endorsed by ASCE or EWRI.
- The source pages were read through a web reader, not seen by a person. The short link in the post could not be opened.
- Track numbers are not shown; the order on the page and in an earlier committee draft differ.
- Not shown: fees, registration price dates, cancellation deadlines, hotel, program.
- Dates can change after November 18, 2026.
- The checks compare the film with the facts file, not the facts file with the conference pages. No person has done that yet, or watched the whole film.
- The streams are a drawing. No hydraulics, no flow, no model.

## How to reproduce
`node tools/check.js`, then `node tools/render.js`, then `node tools/build.js`, then `node tools/docx.js`. Needs Node, Playwright with Chromium, ffmpeg and the Inter typeface.

## Credits and licenses
- Conference, tracks, topics, dates: ASCE Environmental & Water Resources Institute and the conference committee (https://modelingcon.asce.org/, https://modelingcon.asce.org/call-abstracts, https://www.asce.org/education-and-events/events/call-for-submissions).
- Film and page: Robert (Bob) Dickinson, SWMM Enablement, swmm5.org.
- Typeface: Inter (SIL Open Font License).

## AI use
This film, this page, the technical summary and this essay were made with Claude, Anthropic's AI model, in one session on November 18, 2026, at the request and under the direction of Robert (Bob) Dickinson. He chose the post and asked for the film. Responsibility for publishing it is his.

What Claude did: read the conference pages through a web reader; noticed that the deadline in the post could not be right and reported it; wrote the facts file, the film code, the checking and rendering scripts, this page and its figures; rendered the MP4; and wrote this text.

How it was checked: by the mechanical checks listed under What was verified, and by Claude looking at nine still frames at full size and two frames taken back out of the MP4. What no person has checked yet: the facts file against the conference pages, and the film watched from start to finish.

## Changes
`1.0 (2026-11-18)`: first build.
