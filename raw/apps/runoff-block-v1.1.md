---
name: The Runoff Block
file: runoff-block.html
version: "1.1"
date: 2026-11-03
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/NSa4US2249jgfYWbbtkt68", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "WebAssembly build from swmm524-perched (perched patch not used by this page's parity runs)", license: public domain}
  - {name: SWMM 4.4H, source: "the 2004 Fortran, from the earlier SWMM 4 reconstruction app"}
  - {name: SWMM 1 Runoff Block, source: "rebuilt from the October 1971 Volume IV program listing, from the earlier SWMM 1 app"}
units: US customary (ac, ft, in, in/hr, cfs, MG)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/NSa4US2249jgfYWbbtkt68, version 1793755149-2052 (index.html, 4,563,875 bytes, SHA-256 f2a4310b68b64dd02285faac4185c83fed23fa64f68f0e7584ffd73f1448de2c), its About, Block and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# The Runoff Block: 59 runoff chats folded onto one subcatchment and EPA SWMM 5.2.4 in the browser

## In three points
- **What:** One subcatchment run by EPA SWMM 5.2.4 compiled to WebAssembly, with tabs for surface, infiltration, LID, groundwater and snow, the SWMM 1 and SWMM 4.4H engines on the same block, and the 59 runoff chats it gathers.
- **So what:** 36 of 36 scenario inputs wrote a byte-identical .out in the browser and native builds, and on the default block SWMM 4.4 and 5.2.4 agree to 0.13 percent on volume while SWMM 1 is 17.6 percent high because its Horton curve decays on the storm clock.
- **Now what:** Use it to see what each runoff method does to one block, including that halving W and both n values gives the same .out. One subcatchment under synthetic storms says nothing about which method is right for a real catchment.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.1 · 2026-11-03"). The file name above is ours; the page names none. Every number below is copied from the page. No model was run to write this file.

## What it does

From November 2023 on, Bob asked an AI 59 sets of questions about the subcatchment: width, infiltration, curve numbers, green roofs, groundwater, snow, the old engines. Those answers became separate apps, each with its own small solver. This page keeps the questions and replaces the solvers with one engine. Tabs: Block (the subcatchment, the storm, the hydrograph), Surface, Infiltration, LID, Ground & Snow (one group of chats each, run live), Old Engines (the block through 1971, 2004 and 2023), Lessons (three short runs with checkable answers), ICM, Chats (the 59-row list), About (checks and the defect register), Doc.

## How it computes

- Default block: 10 ac, 40% impervious, W 800 ft, 2% slope, Horton infiltration, a 2 in Chicago (Keifer-Chu) storm over 3 hours (peak at r = 0.4, b = 10 min, c = 0.75; illustrative, not from a local IDF curve).
- SWMM's three surfaces per subcatchment (impervious without storage, impervious with storage, pervious) are each a nonlinear reservoir, dd/dt = i* - alpha (d - ds)^(5/3), alpha = 1.49 W sqrt(S) / (n x surface area). The page runs each surface as its own engine run so the curves keep their own alpha.
- Film depth above the depression lip is recovered by inverting Manning on each surface's run.
- The 1971 line in RHYDRO and the 5.2.4 line in subcatch.c are set side by side; the page notes a comment in subcatch.c, "Possible change to how sub-area width should be assigned."

## Results the page reports

- Default block: peak 20.80 cfs at 1.25 hr; runoff 0.93 in (0.25 MG); runoff coefficient 0.466; runoff continuity -0.40%. Ledger: rain 2.000 in; infiltration 1.058 in; surface runoff 0.932 in; storage at end 0.018 in; residual -0.008 in.
- Width: from W x 0.25 to W x 4, a sixteenfold change, the peak goes from 14.6 to 25.0 cfs (five engine runs).
- As coded, impervious water on the default block flows 218 ft and pervious water 327 ft; the commented-out change would give both 545 ft.
- Three engines: SWMM 4.4 and 5.2.4 agree to 0.13 percent on volume; SWMM 1 is 17.6 percent high; with Horton decay removed (f0 = fc) the gap closes to 0.8 percent.

## Checks (as stated on the page)

- Parity: 36 of 36 scenario inputs wrote a byte-identical .out in the wasm build and a native gcc build of stock 5.2.4 with the perched patch reversed; the page stores each native SHA-256 and rehashes the browser run. The repo's own count, 598 of 598, is carried and not rerun.
- Null effect: the same input twice gives the same .out; W/2 with n/2 gives the same .out.
- Block equals impervious plus pervious within 0.047 percent of peak (in the far tail at 4.42 hours); impervious equals A1 plus A2 to 5e-7 cfs.
- JavaScript port against the engine: 5-minute wet step 2.4e-7 cfs, 2-minute 1.1e-7 cfs, report step longer than the wet step 1.8e-7 cfs, over every report period.
- Version 1.0 passed nine checks and was graded 75 of 100 by an outside reviewer, who found a 0.92 cfs port-versus-engine gap labelled as rounding; the port now follows the engine's variable step and each reproduced defect has a regression test.
- Every tab opened in Chromium, dark and light, at 1280 and 375 px, with no console errors.

## What this does not show

- No observed flows, no network, no water quality.
- One subcatchment under synthetic storms: what each method does, not which one is right for a given catchment.

## How to reproduce

Open the page; change the block on the first tab and every other tab follows. The About tab's Check panel reruns the parity hashes in the browser. Blocks can be saved as JSON.

## Credits and licenses

EPA SWMM 5.2.4 (US EPA, public domain). SWMM 1 (1971) and SWMM 4.4H (2004) engines from Bob's earlier reconstruction apps. No license is stated for the page itself.

## AI use

The page says the app and its essay were made with Claude, Anthropic's AI model, in one session on 3 November 2026, under the direction of Robert (Bob) Dickinson, who chose the project, wrote the list of 59 chats, set the standing rules for his apps, and for version 1.1 supplied the outside review. Claude read the SWMM 5.2.4 source and his earlier apps, wrote the app and its tests, ported the runoff step to JavaScript, ran the experiments and wrote the text; a second Claude agent read the 59 chats back and wrote the one-line summaries on the Chats tab. The SCS tables were first typed from memory and corrected against web sources in 1.1. The SWMM 1 and SWMM 4 engines, the perched engine, the Results Kit and the converters came from his earlier apps. No person has reviewed version 1.1, the essay or the chat summaries. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1 (2026-11-03): answers an outside review of 1.0 (75 of 100): port follows the engine's variable step; Reset fixed; regression tests for each reproduced defect.
- 1.0: first version, nine checks.
