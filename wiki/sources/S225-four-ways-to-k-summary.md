---
title: "S225: Four Ways to K, summary written from the page (v1.0)"
type: source
raw: raw/apps/four-ways-to-k-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-29
ingested: 2026-11-17
tags: [apps, swmm5, minor-losses, manholes, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Four Ways to K, version 1.0: four ways of putting a manhole loss into SWMM5 ([LOSSES], an equivalent Manning n, a side orifice and a HEC-22 calculation) plus a no-loss control, run on one two-pipe test line with EPA SWMM 5.2.4 in the page. Raw file: [raw/apps/four-ways-to-k-v1.0.md](../../raw/apps/four-ways-to-k-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793323393-f15c, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude (Claude Opus 5.5) in a session on 29 October 2026 at Bob's direction: Bob asked whether SWMM5's fixed link losses could be done any other way and asked for the comparison to be engine-verified; Claude read the 5.2.4 loss code, designed the test line and cases and wrote the HEC-22 implementation.

**Claims worth keeping** (all copied from the file)
- Test line: J1 (invert 100.0 ft) to C1, 300 ft, to J2 (98.5 ft) to C2, 300 ft, to OF1 (97.0 ft); 24 in circular, n 0.013, slope 0.005; dynamic wave at a 2 s step. Four flow cases: 20 cfs surcharged, 8 cfs half full, 2 cfs shallow, and a 0 to 25 to 0 cfs storm.
- At 20 cfs surcharged, [LOSSES], equivalent n and the orifice each raise J1 by 0.944 ft; the hand value is 1.5 x 0.629 = 0.944. At the storm peak: 1.478, 1.450 and 1.468 ft.
- Under [LOSSES] and equivalent n the manhole rises 0.315 ft; under the orifice 0.944 ft, the whole loss parked at the manhole. HEC-22's straight-through manhole costs 40 percent as much.
- Equivalent n was tuned to the full-pipe hydraulic radius: at 2 cfs (water at 0.24 of the diameter) the formula predicts 2.15 times too much loss and the engine gave 1.94 times; it is right at half full and undercharges a nearly full pipe by about a fifth.
- The engine is Bob's EPA 5.2.4 WebAssembly build from Seven SWMM Engines 1.2, unchanged, checked against swmm-toolkit 0.17.0; results are read by the SWMM Results Kit 1.0.0.

**Limits it states.** One test line and four flow cases; no field data.

**Checked at ingest.** 1.5 x 0.629 = 0.9435 ft. Using [LOSSES] or an orifice when the loss must hold at all depths is the page's advice, from these runs. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://four-ways-to-k.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Four Ways to K (app)](../entities/four-ways-to-k.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Seven SWMM Engines (app)](../entities/seven-swmm-engines.md), [SWMM Results Kit](../entities/swmm-results-kit.md), [Orifices](../concepts/orifices.md), [SWMM 5 network objects, boundary and initial conditions](../concepts/swmm5-network-objects.md).
