---
title: "S73: SWMM 1 Engine, technical summary (app .md, v3.13)"
type: source
raw: raw/apps/swmm1-runoff-engine-v3.13.md
kind: app-md
author: Robert Dickinson
published: 2026-11-13
ingested: 2026-11-15
tags: [swmm-history, swmm1, verification, apps, wasm]
reviewed: no
---
**What it is.** The technical summary carried inside the SWMM 1 Engine page, version 3.13. It replaces [S01](S01-swmm1-engine-app-md.md) (version 3.6) as the current source for the app. Raw file: [raw/apps/swmm1-runoff-engine-v3.13.md](../../raw/apps/swmm1-runoff-engine-v3.13.md). Versions 3.7 to 3.12 were never ingested; 3.12 is marked `superseded`.

**How it was written.** By Claude (Anthropic) in sessions of October and November 2026, directed by Bob, who "supplied the scans and the manual, set the goal and reviews the result". Versions 3.6 to 3.9 and 3.11 to 3.13 each answer an outside review made with ChatGPT (grades 85, 89, 91, 90, 93, 91 and 93 of 100; the last is a second review of 3.10). The file says every review finding was reproduced on the earlier page before any change.

**What is unchanged from 3.6.** The listing (65 units, 12,200 cards), the three engines, the six 1971 runs and their scores, the three-build comparison (21,804 printed numbers), the as-printed and repaired engines. The change list says "No engine change" for each version from 3.1 to 3.10; the entries for 3.11 to 3.13 describe importer, status-row and page changes and name no change to the engines' arithmetic.

**Claims new since 3.6**
- Of the 248 pages of Volume IV, 235 are listing pages; 115 were typed by reading and 120 drafted by a character classifier trained on 154,000 labelled character images.
- Both full-program engines rebuilt from the project kit are byte-identical to the shipped ones (Ubuntu 24.04, gfortran 13.3, f2c 20200916, Emscripten 3.1.6).
- The Runoff workbench's hand-written C of 22 October 2026 was recovered and is in the kit. Rebuilt with Emscripten 3.1.6 it matches the shipped wasm bit for bit on 9 decks.
- A native glibc 2.39 build of that C differs from the browser in tape 8 on 2 of 9 decks. Logs of 180,246 math-library calls trace it to `sinf` (292 of 46,228 calls) and `cosf` (280 of 23,114), one unit in the last place, at cards `GUTT 94` to `GUTT 101`. In all 194 distinct cases the wasm (musl) value is the correctly rounded one; glibc is off by up to 0.559 ULP.
- The importer from SWMM 5 `.inp` now carries: a rain interval made a whole number of steps, because WSHED reads the rain histogram once per step at its middle (`WSHE 24`); EPA's cumulative-rain reset rule; WET_STEP as the runoff step; ELEVATION offsets; the per-line infiltration method; and zeros punched as the smallest value a field holds.
- Run status has rows for execution, numerical validity, conservation, time axis, rainfall carried, routing carried, inputs carried, geometry carried, effective parameters, output tapes, second engine and reference agreement. Since 3.13 each effective parameter has one of five outcomes: preserved, approximated, historical default applied, mismatch, not checked.
- A converted one-acre lot with slope 0 is punched `.001` ft/ft and 3,368 of 3,630 cu ft run off in SWMM 1; the file says a zero slope "cannot be expressed on a SWMM 1 card at all".
- Since 3.13 the engines run in a Web Worker with Cancel: identical printouts, tapes and COMMON snapshots on both workbench decks and all 54 full-program runs.
- Complexity index 72.6 (analyzer 1.7.0, baseline HC-2026-11-10-h, 182 source files); the shipped .html alone 64.8.
- The front matter is dated 2026-11-13; the change list dates 3.11, 3.12 and 3.13 to 2026-11-14.

**Limits it states.** No EPA SWMM 5 run was made for the importer checks: "the solver could not be installed or compiled" in the session, so the four models in `app/test/epa/` are unrun. The importer's hydrographs are not compared with SWMM 5's. No person has compared the 10,889 cards of four blocks with the page images, or reviewed the five repaired cards, the four Volume II decks, or the values read from the scans. Volume I was not read.

**Checked at ingest.** The six-run table and the bug list match [S01](S01-swmm1-engine-app-md.md) card for card. The bug list has 15 entries, one of them called "a method, not a fault" (`WSHE 24`); [S01](S01-swmm1-engine-app-md.md) counted fourteen faults.

**Feeds:** [SWMM 1 Engine (app)](../entities/swmm-1-engine-app.md), [SWMM 1 (1971)](../entities/swmm-1.md), [Verification against printed runs](../concepts/verification-against-printed-runs.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md).
