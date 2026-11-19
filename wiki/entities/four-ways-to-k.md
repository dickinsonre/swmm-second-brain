---
title: "Four Ways to K (app)"
type: entity
updated: 2026-11-19
sources: [S205, S225, S386]
tags: [apps, swmm5, minor-losses, manholes, wasm]
reviewed: no
---
Bob's app Four Ways to K: four ways of putting a manhole loss into SWMM5 ([LOSSES], an equivalent Manning n, a side orifice and a HEC-22 calculation) plus a no-loss control, run on one two-pipe test line with EPA SWMM 5.2.4 in the page. Version 1.0.1, 2026-11-19 [S386](../sources/S386-four-ways-to-k-summary-v1-0-1.md); version 1.0 of 29 October 2026 is summarized in [S225](../sources/S225-four-ways-to-k-summary.md). Netlify address: https://four-ways-to-k.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S225](../sources/S225-four-ways-to-k-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S225](../sources/S225-four-ways-to-k-summary.md)
- Test line: J1 (invert 100.0 ft) to C1, 300 ft, to J2 (98.5 ft) to C2, 300 ft, to OF1 (97.0 ft); 24 in circular, n 0.013, slope 0.005; dynamic wave at a 2 s step. Four flow cases: 20 cfs surcharged, 8 cfs half full, 2 cfs shallow, and a 0 to 25 to 0 cfs storm.
- At 20 cfs surcharged, [LOSSES], equivalent n and the orifice each raise J1 by 0.944 ft; the hand value is 1.5 x 0.629 = 0.944. At the storm peak: 1.478, 1.450 and 1.468 ft.
- Under [LOSSES] and equivalent n the manhole rises 0.315 ft; under the orifice 0.944 ft, the whole loss parked at the manhole. HEC-22's straight-through manhole costs 40 percent as much.
- Equivalent n was tuned to the full-pipe hydraulic radius: at 2 cfs (water at 0.24 of the diameter) the formula predicts 2.15 times too much loss and the engine gave 1.94 times; it is right at half full and undercharges a nearly full pipe by about a fifth.
- The engine is Bob's EPA 5.2.4 WebAssembly build from Seven SWMM Engines 1.2, unchanged, checked against swmm-toolkit 0.17.0; results are read by the SWMM Results Kit 1.0.0.

**What it does not show.** One test line and four flow cases; no field data. [S225](../sources/S225-four-ways-to-k-summary.md)

**Noted at ingest.** 1.5 x 0.629 = 0.9435 ft. Using [LOSSES] or an orifice when the loss must hold at all depths is the page's advice, from these runs.

**Version 1.0.1.** The page followed the device's light setting on first paint, against the dark-first rule. `<html>` now carries `data-theme="dark"`, and the theme falls back to dark rather than to `prefers-color-scheme`; Light is used only when chosen. No engine run was repeated [S386](../sources/S386-four-ways-to-k-summary-v1-0-1.md).

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Seven SWMM Engines (app)](seven-swmm-engines.md), [SWMM Results Kit](swmm-results-kit.md), [Orifices](../concepts/orifices.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
