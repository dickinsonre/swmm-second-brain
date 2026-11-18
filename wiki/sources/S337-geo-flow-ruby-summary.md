---
title: "S337: Geo Flow Ruby, summary written from the page (v2026-10-21)"
type: source
raw: raw/apps/geo-flow-ruby-v2026-10-21.md
kind: app-md
author: Robert Dickinson
published: 2026-10-21
ingested: 2026-11-18
tags: [apps, dry-weather-flow, population, gis, swmm5]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app Geo Flow Ruby, version 2026-10-21: household points to subcatchment population to SWMM dry-weather flow. Raw file: [raw/apps/geo-flow-ruby-v2026-10-21.md](../../raw/apps/geo-flow-ruby-v2026-10-21.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/Vig2igKDHQjNbNNMSYtCxX, version 1792637435-70b9 (index.html, 255,535 bytes, SHA-256 ba78d64fca27e206f3a74cdc2a50f1e0c58bc2fe33f2f72f8dbf6eaacffe965b), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the original source and asked for the app; responsibility is his. Claude read and reproduced the original's defects by running its code, compiled EPA SWMM 5.2.4 to test exports, and wrote the sample data, engine, interface, checks, figures and documentation."

**Claims worth keeping** (all copied from the file)
- An earlier single-file rebuild of SWMMEnablement/geo-flow-ruby (see also Geo Flow Population Calculator, a later and larger rebuild of the same project). It assigns household points to SWMM subcatchments with the ray-crossing test, sums persons, routes them to the node each subcatchment drains to, and writes dry-weather FLOW baselines into [DWF]. Files never leave the page.
- The original's own utilities, run unchanged in Node on the sample, read 0 of 12 polygons from an EPA-written .inp (its header test accepted only capitals), assigned 0 of 329 households (polygons rescaled to an 800 x 600 canvas, households left in model coordinates), wrote CFS baselines 100.0001 times too large (1.547 cfs for 100 persons at 100 gal/cap/day, against 0.01547 cfs), and produced 22 ERROR 209 lines in EPA SWMM 5.2.4 by writing [DWF] against subcatchments and inventing a pollutant called Population. The rebuild reads 12 of 12 and assigns 325 of 329.
- The original's TypeScript utilities bundled and run unchanged in Node against the sample model and households; every defect reproduced, nothing inferred from reading code alone.
- The new engine checked against Shapely 2.2.0 (GEOS) on all 329 households. Two households planted exactly on shared boundaries go to S06 and S03, one owner each, where GEOS reports each as touching two subcatchments.

**Limits it states.** As the page lists it: a household is a point, so a building that straddles a line goes to whichever side its geocode falls on; a snap radius can miss an edge and leave a household uncounted; census block centroids are not homes; the output is a baseline, with no RDII and no peaking factor.

**Checked at ingest.** Geo Flow Ruby and [Geo Flow Population Calculator (app)](../entities/geo-flow-population-calculator.md) are two single-file editions of the same Lovable project, SWMMEnablement/geo-flow-ruby, built in different sessions; they are kept as two pages. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Geo Flow Ruby (app)](../entities/geo-flow-ruby.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [Geo Flow Population Calculator (app)](../entities/geo-flow-population-calculator.md).
