---
title: "S276: Brick City Water Cycle, summary written from the page (v1.0)"
type: source
raw: raw/apps/brick-city-water-cycle-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, teaching, water-cycle, lid, detention, swmm5, 3d]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Brick City Water Cycle, version 1.0: a toy-brick 3D board of a small town's supply, wastewater and storm water in sixteen stages, with the storm drains, pond and green infrastructure a real EPA SWMM 5.2.4 model whose results the page replays. Raw file: [raw/apps/brick-city-water-cycle-v1.0.md](../../raw/apps/brick-city-water-cycle-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/EpyKacUscNdqfMxdvEsA6Z, version 1792849940-43e0 (index.html, 181,361 bytes, SHA-256 f996e84794f8865610904763fa84218593350745974cc52270cc3a94fcebb04c), its About and Doc tabs read in headless Chromium on 2026-11-18 with three.js r128 supplied from a local copy. Nothing was run to write this file." The page says it was built with Claude in October 2026 under Bob's direction, from a reference photo he supplied; the board is an original layout.

**Claims worth keeping** (all copied from the file)
- Storm: 2.5 in in 2 hours on 33.7 ac. The pond cuts the peak by 86 percent and does not reduce the volume.
- With a green roof, 18 rain gardens and 40,000 ft2 of pavers: runoff 1.84 to 1.43 in, infiltration 0.64 to 0.86 in, peak inflow to the pond 100 to 77 cfs, peak pond depth 2.44 to 1.88 ft, release to the river 14.4 to 12.6 cfs.
- The release falls only 12% because the outlet orifice, not the rain, sets it; the page's lesson is that the pond and the gardens are designed together.
- Continuity: runoff -0.021% and routing -0.016% as built; -0.029% and -0.014% with green infrastructure; seven subcatchment polygons overlap by 0 ft2.

**Limits it states.** Supply and sewer flows are drawn, not computed; heights not to scale; one design storm, no dry-weather flow or quality; stage design values from published standards, not computed; LID parameters textbook values; no person has reviewed it.

**Checked at ingest.** Two printed hand checks do not multiply out as printed (our arithmetic): 2.5 x 33.7 / 12 = 7.021, where the page writes 7.018 (SWMM's value, which implies 33.69 ac); 70,000 x 2.44 = 170,800 ft3, where the page writes 171,100 (Q113). The `links:` line gives Netlify as https://brick-city-water-cycle.netlify.app.

**Feeds:** [Brick City Water Cycle (app)](../entities/brick-city-water-cycle.md), [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [LID bio-retention layers](../concepts/lid-bioretention-layers.md), [Weirs and outlets](../concepts/weirs-and-outlets.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md).
