---
title: "Brick City Water Cycle (app)"
type: entity
updated: 2026-11-18
sources: [S276]
tags: [apps, teaching, water-cycle, lid, detention, swmm5, 3d]
reviewed: no
---
Bob's app Brick City Water Cycle: a toy-brick 3D board of a small town's supply, wastewater and storm water in sixteen stages, with the storm drains, pond and green infrastructure a real EPA SWMM 5.2.4 model whose results the page replays. Version 1.0, 2026-10-24 [S276](../sources/S276-brick-city-water-cycle-summary.md). Netlify address, from its `links:` line: https://brick-city-water-cycle.netlify.app [S276](../sources/S276-brick-city-water-cycle-summary.md).

**A caution about its source.** The page ships no technical summary. [S276](../sources/S276-brick-city-water-cycle-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S276](../sources/S276-brick-city-water-cycle-summary.md)
- Storm: 2.5 in in 2 hours on 33.7 ac. The pond cuts the peak by 86 percent and does not reduce the volume.
- With a green roof, 18 rain gardens and 40,000 ft2 of pavers: runoff 1.84 to 1.43 in, infiltration 0.64 to 0.86 in, peak inflow to the pond 100 to 77 cfs, peak pond depth 2.44 to 1.88 ft, release to the river 14.4 to 12.6 cfs.
- The release falls only 12% because the outlet orifice, not the rain, sets it; the page's lesson is that the pond and the gardens are designed together.
- Continuity: runoff -0.021% and routing -0.016% as built; -0.029% and -0.014% with green infrastructure; seven subcatchment polygons overlap by 0 ft2.

**What it does not show.** Supply and sewer flows are drawn, not computed; heights not to scale; one design storm, no dry-weather flow or quality; stage design values from published standards, not computed; LID parameters textbook values; no person has reviewed it. [S276](../sources/S276-brick-city-water-cycle-summary.md)

**Noted at ingest.** Two printed hand checks do not multiply out as printed (our arithmetic): 2.5 x 33.7 / 12 = 7.021, where the page writes 7.018 (SWMM's value, which implies 33.69 ac); 70,000 x 2.44 = 170,800 ft3, where the page writes 171,100 (Q113).

See [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [LID bio-retention layers](../concepts/lid-bioretention-layers.md), [Weirs and outlets](../concepts/weirs-and-outlets.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md).
