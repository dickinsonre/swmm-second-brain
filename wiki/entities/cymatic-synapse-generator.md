---
title: "Cymatic Synapse Generator (app)"
type: entity
updated: 2026-11-18
sources: [S283]
tags: [apps, generators, swmm5, swmm6, storage, wasm]
reviewed: no
---
Bob's app Cymatic Synapse Generator: a generator that turns a Grok Imagine render into an EPA SWMM 5.2.4 model (a twin-rail trunk, storage hubs with throttled outlets, contours and Voronoi subcatchments) and runs it in EPA 5.2.4 and OpenSWMM 6 DW and FV in the browser. Version 1.15, 2026-10-31 [S283](../sources/S283-cymatic-synapse-generator-summary.md). Netlify address, from its `links:` line: https://cymatic-synapse-swmm5-swmm6.netlify.app [S283](../sources/S283-cymatic-synapse-generator-summary.md).

**A caution about its source.** The page ships no technical summary. [S283](../sources/S283-cymatic-synapse-generator-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S283](../sources/S283-cymatic-synapse-generator-summary.md)
- 28 native EPA 5.2.4 runs (swmm-toolkit 0.17.0) over 23 models finished with 0 errors and 0 warnings; runoff continuity -0.003 to -0.004%, routing within 0.118%.
- Seed 7 default: OF1 peak 717.1 cfs; basins removed, pipes kept 798.6 cfs; redesigned without storage 812.1 cfs; all about 31.08 to 31.09 MG.
- The default storm drops 130.29 ac-ft on 521.19 ac, which is 3.00 in.
- The browser and native builds of 5.2.4 agree byte for byte on six of ten presets and within 0.059 ft on the rest.

**What it does not show.** Before a run the picture shows design numbers; playback interpolates between report times; the glow is decoration; OpenSWMM 6 FV runs with four cells per conduit by default, which its own manual calls not converged. [S283](../sources/S283-cymatic-synapse-generator-summary.md)

**Noted at ingest.** 130.29 ac-ft / 521.19 ac = 0.25 ft = 3.00 in (our arithmetic).

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [Seven SWMM Engines (app)](seven-swmm-engines.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).
