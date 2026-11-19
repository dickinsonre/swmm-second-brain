---
title: "SWMM6 Hands-On Watershed (app)"
type: entity
updated: 2026-11-19
sources: [S205, S261, S385]
tags: [apps, swmm6, snow, groundwater, emulator, wasm]
reviewed: no
---
Bob's app SWMM6 Hands-On Watershed: one page that carries the OpenSWMM 6 engine compiled to WebAssembly (swmm6_rel at 137e65e of 10 September 2026, reporting 6.0.0-alpha.4), a 179.06 ac synthetic catchment with snow and groundwater, eight knobs moved by hand gestures through the webcam, and a neural-network emulator that answers while the hand moves. The idea follows Alireza Razeghi Haghighi's Riverlight post; none of Riverlight's code is used. Version 1.1.1, 2026-11-19 [S385](../sources/S385-swmm6-hands-on-watershed-summary-v1-1-1.md); version 1.1.0 of 8 November 2026 is summarized in [S261](../sources/S261-swmm6-hands-on-watershed-summary.md). Netlify address: https://swmm6-hands-on-watershed.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S261](../sources/S261-swmm6-hands-on-watershed-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S261](../sources/S261-swmm6-hands-on-watershed-summary.md)
- Every term of P - ET - Q - Flood - DeepPerc = Delta S is read from the engine's continuity tables; the balance closed within 0.049 in on all 3,500 test runs, with 0 ERROR lines and a worst runoff continuity error of 0.50 %.
- Default storm, 2.50 in in six hours: 1.442 in infiltrated, 1.018 in ran off and left at the outfall within 72 hours, 0.104 in returned to the air; 2.500 - 0.104 - 1.018 = 1.379 in against Delta S 1.380 in.
- Emulator: two hidden layers of 32 units, trained on 3,300 SWMM6 runs, scored on 200 held out: peak R2 0.952; for peaks above 5 cfs a median error of 9.4 %, 90th percentile 37.4 %; worst time-to-peak miss 19.8 hours. Without snow (1.0) the median peak error was 3.4 %.
- Version 1.0 ran LocalSWMM's 6.0.0-alpha.2 build, which never melts snow. On 125 test models with peaks above 5 cfs the two builds' peaks match within a median 0.04 % (largest 0.75 %).
- Snow against EPA SWMM 5.2.4: six scenarios agree within 0.3 % except near freezing; rain on a 2 in pack at 38 F gives a peak 4.5 % off, and at 34 F outflow volume is 9.4 % off.
- Known defect in this build: a conduit that goes dry keeps its last evaporation rate (DynamicWave.cpp at 137e65e, recomputeConduitLossOne returns early for DRY conduits). On a storm that fell entirely as snow the report shows 0.022 ac-ft evaporated and a routing continuity error of -34,178 %; EPA SWMM 5.2.4 reports zero. Fixed upstream on 12 September 2026 (commit b051d270).
- 30 of 30 synthetic hand poses were classified correctly.

**What it does not show.** No real place: the catchment is synthetic and uncalibrated. The snow comes from a September build; OpenSWMM reworked snowmelt after 10 September 2026. The emulator knows one catchment. Live hand tracking was not tested, for want of a camera where it was built. The Doc's limits list still says six knobs and alpha.2. [S261](../sources/S261-swmm6-hands-on-watershed-summary.md)

**Noted at ingest.** 2.500 - 0.104 - 1.018 = 1.378 in, against the 1.379 printed; the difference is rounding in the three terms. The page says the camera is blocked in sandboxed previews; Netlify reported a finished deploy on 17 November 2026 [S205](../sources/S205-note-netlify-addresses.md), which is where the page says the camera works.

**Version 1.1.1.** Six tables (`table.t`) had no sideways scroller: after one engine run the session log made the Emulator tab 445 px wide on a 390 px screen, and the About table was 601 px. Each is now wrapped in `<div class="tw">` with `overflow-x:auto`, and both tabs fit at 390 px. No engine run was repeated [S385](../sources/S385-swmm6-hands-on-watershed-summary-v1-1-1.md).

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md), [The SWMM findings register](../concepts/findings-register.md).
