---
title: "S68: SWMM5 Code House, technical summary (app .md, v1.15.1)"
type: source
raw: raw/apps/swmm5-code-house-v1.15.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-11
ingested: 2026-11-14
tags: [apps, swmm5, source-code, wasm, verification]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: 2026-11-15
---
**What it is.** The technical summary carried inside the SWMM5 Code House page, version 1.15.1: a walkable 3D map of the EPA SWMM 5.2.4 source with the engine running in the page. Raw file: [raw/apps/swmm5-code-house-v1.15.1.md](../../raw/apps/swmm5-code-house-v1.15.1.md).

**How it got here.** Extracted byte for byte on 14 November 2026 from the `script#app-md` block of Bob's published artifact, after he gave the app's Netlify address. The public Netlify page was not the source: its page source shows a v1.0.0 badge (Q45).

**How it was written.** By Claude (Anthropic) in Claude Code sessions in November 2026; versions to 1.14.0 with model claude-opus-5-5, versions 1.15.0 and 1.15.1 with claude-fable-5-2. Bob asked for the app and steers it through outside reviews. It says Bob "has not yet reviewed this build".

**Claims worth keeping**
- The house: 58 rooms on 5 floors, 51,080 lines, 54 files, 969 functions, 160 doorways. The guide is Froude, a water drop.
- Engine in the page: `swmm524.wasm`, SHA-256 `e371a84962a38b760a5ef76eebe993bd961fe9a97537a04e89db2e277239efa7`, built from USEPA commit 7952ca8 with Emscripten 3.1.51, `-O2 -D_FORTIFY_SOURCE=0`, per the build record in the Seven SWMM Engines app v1.2. The build was not repeated.
- WebAssembly against stored native EPA 5.2.4 output, 78 models from the 1729 corpus: 78 ran, 78 inside the limits, 801,567 of 805,991 stored values exactly equal, 75 models identical to the last stored digit, largest gap 2.4 % of one series' range. The limits (3 % of range, 0.003 percentage point on continuity) were set after the first comparison.
- 59 engine checks and 97 verification rows are required. 344 of 344 deliberately forced engine failures gave a failed check, a failed command and a named model.
- 28 test scripts run by `node test/run_all.js` on the delivered file.
- The ? on code: 8,745 of 8,745 struct field uses resolve to their owner.
- Doors to the SWMM6 house: 454 of 962 SWMM 5 function names appear in the OpenSWMM 6.0.0-alpha.4 text (commit 9648837), at 1,266 places; 147 places are OpenSWMM functions with the same name.
- Diagrams are JavaScript transcriptions of the C in each room. Reported values are labelled as interpolated, computed from interpolated values (conduit velocity) or averaged.
- Froude's Hunt has 9 clues. Follow a run has three paths.
- Credits: EPA SWMM 5.2.4, USEPA, public domain, "Lewis Rossman is its principal developer"; three.js r128.
- Changes: 1.13.0 (2026-11-03), 1.14.0 (2026-11-04), 1.15.0 (2026-11-11), 1.15.1 (2026-11-12).

**Limits it states.** The engine build was not repeated and its record lacks the full command line. The native reference files were not rerun and the native program has no recorded hash. Three models differ from native and the cause was not traced. A door to the SWMM6 house is a name match, not shown to be the same logic. No person has read the diagrams against the C line by line. No learner was observed; no real phone or screen reader was tried.

**Checked at ingest.** The script list has 28 entries. The summary gives 969 functions for the house and 962 for the door census (Q46). Its front matter is dated 2026-11-11 and its change list dates 1.15.1 to 2026-11-12.

**Feeds:** [SWMM5 Code House (app)](../entities/swmm5-code-house.md), [SWMM6 Code House (app)](../entities/swmm6-code-house.md), [EPA SWMM 5](../entities/swmm-5.md), [Lewis A. (Lew) Rossman](../entities/lew-rossman.md).
