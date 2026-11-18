---
title: "Understand Anything for SWMM and ICM (app)"
type: entity
updated: 2026-11-17
sources: [S205, S251]
tags: [apps, swmm5, swmm6, icm, code-graphs, ruby]
reviewed: no
---
Bob's app Understand Anything for SWMM and ICM: a measurement of the file links and call graph of EPA SWMM 5.2.4 with the compiler and linker, a comparison with OpenSWMM 6, a census of 532 ICM Ruby scripts, and a scoring of code-graph tools (a June hand-drawn map and graphify) against that referee. It updates a June 2026 app that explained the Understand Anything plugin with a map drawn from memory. Version 2.0, 2026-11-05 [S251](../sources/S251-understand-anything-swmm-icm-summary.md). Netlify address: https://understand-anything-swmm-icm.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S251](../sources/S251-understand-anything-swmm-icm-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S251](../sources/S251-understand-anything-swmm-icm-summary.md)
- EPA SWMM 5.2.4: 365 file links, 324 with calls and 79 with data; 967 functions and 1,916 call edges, from all 54 objects compiled at tag v5.2.4 and read with nm.
- The June map found 60 of the 365 real links, drew 24 that do not exist and 4 backward, and left out 8 real files; it drew routing.c to dynwave.c, but routing.c never calls dynwave.c (routeFlow calls flowrout_execute, and line 167 of flowrout.c calls dynwave_execute).
- graphify's free pass found 322 links in 2.3 seconds, none invented, and 1,877 of the 1,916 call edges.
- The knot: 46 of 54 files form one strongly connected set; 8 are leaves; the best order still leaves 70 of 365 uses pointing backward, so no learning order can run one way.
- OpenSWMM 6.0.0-alpha.4 (swmm6_rel, 79bb4e1): 278 of 284 .cpp compiled, 6 needing HDF5, nothing executed; 1 public writable symbol against 332 in SWMM 5.2.4; a knot of 31 of 278 files.
- ICM Ruby census of 532 scripts: 288 contain no def; a regular expression finds 63 tables touched.

**What it does not show.** Understand Anything itself was read, not run: a safety check in the build session refused to build its downloaded code, and nobody worked around it. The reference is Linux gcc. A link says only that one file can reach another, not that a path runs in a given model. The ICM solver is closed source; only the Ruby layer is measured. [S251](../sources/S251-understand-anything-swmm-icm-summary.md)

**Noted at ingest.** 60 of 365 is 16 % of the real links, and 60 of the 88 lines drawn is 68 %, the two figures the page gives. Both the wrong map and the measurement are Claude's, months apart; the summary says so.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [How SWMM 5 is organized: objects, state and the time loop](../concepts/swmm5-objects-state-time-loop.md), [Cycles and trees](../concepts/graph-cycles-and-trees.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).
