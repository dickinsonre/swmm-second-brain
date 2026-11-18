---
title: "Tri-Pyramid (app)"
type: entity
updated: 2026-11-18
sources: [S87, S274]
tags: [apps, results, visualization, swmm5, wasm, report-step]
reviewed: no
---
Bob's app Tri-Pyramid: a demographic-profile chart for a sewer: every node and link binned by fullness, flooding and conduit Froude number, mirrored nodes against links and animated through the run, with EPA SWMM 5.2.4 in the browser. Version 3.0, 2026-10-20 [S274](../sources/S274-tri-pyramid-summary.md). Netlify address, from its `links:` line: https://tri-pyrimid-swmm5-swmm6.netlify.app [S274](../sources/S274-tri-pyramid-summary.md).

**A caution about its source.** The page ships no technical summary. [S274](../sources/S274-tri-pyramid-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S274](../sources/S274-tri-pyramid-summary.md)
- The embedded wasm engine, checked by SHA-256, writes a 319,329-byte .out byte-for-byte identical to the one from a native gcc build of 5.2.4.
- 29 of 29 node maximum depths from the .out agree with the .rpt within 0.006 ft (largest 0.0045 ft).
- Share of time each of 27 conduits spent supercritical, from the page's rebuilt geometry against SWMM's Flow Classification Summary: 0.03 percentage points on average, 0.50 at worst.
- Report-step sampling: with a 120 s report step and 5 s routing, the samples caught 31% of link CB1's routing-step peak; 2 of 28 links fall under the app's 80% threshold and 13 more under 99%.

**What it does not show.** No topology by design (a screening view); geometry compared with the engine on one 27-conduit network, not read against xsect.c; parsers not run on the full 3,813-model corpus; large models and other browsers unmeasured. [S274](../sources/S274-tri-pyramid-summary.md)

**Noted at ingest.** The summary says the parsers have not been run on "the full 3,813-model corpus the page can reach"; the corpus README counts 4,540 .inp files as file counts, not distinct networks ([S87](../sources/S87-corpus-1729-readme.md) via [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md)).

See [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md).
