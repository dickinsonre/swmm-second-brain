---
title: "S391: SWMM 1 Engine, technical summary (app .md, v3.15)"
type: source
raw: raw/apps/swmm1-runoff-engine (8).md
kind: app-md
author: Robert Dickinson
published: 2026-11-19
ingested: 2026-11-19
tags: [swmm-history, swmm1, verification, apps, wasm]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: no
---
**What it is.** The technical summary carried inside the SWMM 1 Engine page, version 3.15. It replaces [S73](S73-swmm1-engine-app-md-v3-13.md) (version 3.13) as the current source for the app. Version 3.14 had no summary of its own in `raw/`; this file carries its change entry. Raw file: [raw/apps/swmm1-runoff-engine (8).md](../../raw/apps/swmm1-runoff-engine%20%288%29.md).

**How it was written.** As for 3.13: by Claude (Anthropic) in sessions of October and November 2026, directed by Bob, "who supplied the scans and the manual, set the goal and reviews the result". For 3.15, "Bob gave the house rules and the Netlify addresses".

**Claims worth keeping** (all copied from the file)
- "As far as we know, this is the only copy of SWMM Version 1 that runs." All five blocks of the October 1971 listing, 12,200 cards, compiled from the cards and checked against 355 numbers printed in 1971.
- Netlify: https://swmm1-engine-imports-swmm5.netlify.app/.
- 3.14 (2026-11-14) answers an outside review of 3.13 (ChatGPT, 92 of 100); every finding was reproduced on the 3.13 page before any change. Five faults, with the code the file quotes:
  - PctZero was averaged by total area: `let pzSum=0,aSum=0; sub.forEach(s=>{ const a=sa[s.name]; if(a&&isFinite(a.pz)){ pzSum+=a.pz*s.area; aSum+=s.area; } });` in `convertInp`. PctZero 0 or 100 on 10 unpaved acres beside one paved acre punched PCTZER 2.273 or 93.18, and Runoff printed 180 or 345 cu ft of gutter flow. The mean is now weighted by paved area; two paved subcatchments with 0 on 5 paved acres and 100 on 1 give 16.7.
  - Rain not in the .inp passed: `const okR=Math.abs(eng-src)<=Math.max(0.01*src,1.0)&&!unres.length;` compared zero with zero for a gage that reads an external file, so Rainfall carried said OK on a dry run. Such a gage, and one that names an undefined series, now makes the row CHECK.
  - Barrels were never read: `xs[r[0]]={shape:r[1].toUpperCase(),g1:...,g4:parseFloat(r[5])||0}` stops at the sixth field, so one barrel and four gave the same cards. Inputs carried now names each conduit with more than one barrel and is CHECK; SWMM 1 has one barrel per element, so this is "Not emulated".
  - The run record read the run again after every hash, so a run finishing during hashing put its deck beside the first run's status. It now captures the run first and records `run_number`.
  - `doRun` began `showWB();` before running, so cancelling a workbench run hid the full-program results.
  - Test t24: 20 checks; 16 fail on the 3.13 page, the other four are controls.
- 3.15 (2026-11-19) follows the house rules of 16 and 18 November 2026, with "no engine, converter or test-model change": the "What is unique" section (114 words), a contents list of 34 sections, the Doc tab after About, a "Related apps on Netlify" section, no em dash in the prose, and the Netlify address in the front matter. Test t25: 25 checks; 20 fail on the 3.14 page, the other five are controls.
- Complexity 72.9 over 185 source files (Size 66.6, Structure 79.0, Test evidence 36.6, SWMM vocabulary 87.3; meter 1.7.0); the shipped .html alone 65.0. Version 3.13 gave 72.6 and 64.8.
- Related apps on Netlify, as the file lists them: EXTRAN III, Alive Again (https://extran3-alive-again.netlify.app/); SWMM 4.4H Engine (https://swmm44h-engine-swmm5-import.netlify.app/); The SWMM 1 Book (https://swmm1-book-based-on-app.netlify.app/); XP to SWMM5 (https://xp-to-swmm5.netlify.app/); Visual SWMM at CHI 1999 (https://visual-swmm-1999-chi-conference.netlify.app/); Water Modeling to the Year 3000 (https://water-modellng-in-year-3000.netlify.app/); and SWMM Second Brain (https://swmm-second-brain.netlify.app/), "a reader for Bob Dickinson's SWMM wiki".

**Limits it states.** Unchanged from 3.13 [S73](S73-swmm1-engine-app-md-v3-13.md): no person has read the newly transcribed cards against the pages or reviewed the five repaired cards, the four Volume II decks, or the 1971 table values and figure readings taken from the scan.

**Checked at ingest.** Compared line by line with 3.13: 36 lines differ; the rest is identical. The PctZero figures check (ours): 25 % of 1 paved acre over 11 acres is 2.273; (100 x 10 + 25 x 1) / 11 is 93.18; (0 x 5 + 100 x 1) / 6 is 16.7. Of the seven related-app addresses, six are projects on Bob's Netlify team as read through his connector at ingest; the seventh, water-modellng-in-year-3000, is not, and a project named water-modeling-in-year-3000 is (Q125). The raw file's name, `swmm1-runoff-engine (8).md`, does not follow the naming rule (it would be `swmm1-runoff-engine-v3.15.md`); the agent does not rename raw files.

**Feeds:** [SWMM 1 Engine (app)](../entities/swmm-1-engine-app.md), [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [SWMM 4.4H Workbench (app)](../entities/swmm44h-workbench.md), [Water Modeling to 3000 (app)](../entities/water-modeling-to-3000.md).
