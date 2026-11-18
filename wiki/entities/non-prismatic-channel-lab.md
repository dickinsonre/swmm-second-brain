---
title: "Non-Prismatic Channel Lab (app)"
type: entity
updated: 2026-11-17
sources: [S205, S240]
tags: [apps, swmm5, open-channels, losses, normal-flow-limit, wasm]
reviewed: no
---
Bob's app Non-Prismatic Channel Lab: a 2,000 ft channel whose width you shape, solved by EPA SWMM 5.2.4 in the browser on an .inp the page writes and by a standard-step energy solution of the same channel; the gap between the two water surfaces is the cost of cutting a non-prismatic channel into prismatic links. Version 1.0, 2026-11-02 [S240](../sources/S240-non-prismatic-channel-lab-summary.md). Netlify address: https://non-prismatic-channel-lab.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S240](../sources/S240-non-prismatic-channel-lab-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S240](../sources/S240-non-prismatic-channel-lab-summary.md)
- Abrupt constriction with no losses: SWMM rises 0.279 ft against the energy method's 0.640 ft, 44 %. With converted [LOSSES]: 0.586 ft, 92 %. Tapers: 77 % with 50 ft links and 78 % with 10 ft links.
- A tapered channel under NORMAL_FLOW_LIMITED BOTH oscillates between 359.53 and 570.70 cfs at 10 s reports, on the page's engine and on swmm-toolkit 0.17.0 / PySWMM 2.2.0 alike, identical to the hundredth.
- Five test channels on the two engine copies: largest head difference at any node 0.00001 ft.
- The energy method matches an independent Python standard-step solution of all five channels to 0.0000 ft; the prismatic control agrees with it within 0.004 ft along the reach.
- The page's converted K equals the hand-built decks' 0.45 and 0.60.

**What it does not show.** Five test channels, no field data. ICM is discussed in the Doc but not run. [S240](../sources/S240-non-prismatic-channel-lab-summary.md)

**Noted at ingest.** 0.279 / 0.640 = 44 % and 0.586 / 0.640 = 92 %. The oscillation is a finding for [The SWMM findings register](../concepts/findings-register.md), at the page's word.

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Conduit cross-sections: the built-in shapes](../concepts/conduit-cross-sections.md), [Shape curves, transects and storage curves](../concepts/shape-curves-transects-storage-curves.md), [The SWMM findings register](../concepts/findings-register.md), [SWMM Results Kit](swmm-results-kit.md).
