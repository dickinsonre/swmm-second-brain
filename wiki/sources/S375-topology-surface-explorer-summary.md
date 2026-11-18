---
title: "S375: Topology Surface Explorer, summary written from the page (v2026-10-28)"
type: source
raw: raw/apps/topology-surface-explorer-v2026-10-28.md
kind: app-md
author: Robert Dickinson
published: 2026-10-28
ingested: 2026-11-18
tags: [apps, topology, mathematics, not-water]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Topology Surface Explorer, version 2026-10-28: surfaces built by gluing the edges of a polygon. Raw file: [raw/apps/topology-surface-explorer-v2026-10-28.md](../../raw/apps/topology-surface-explorer-v2026-10-28.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/LbcjojQQ5EWzsAecUWvXnZ, version 1793230423-cf1e (index.html, 286,517 bytes, SHA-256 c9d2186aaafce1c5f0c1839d6377ef1199c1c7b9540770ad78cc373d03bf6408), its markup read on 2026-11-18 (its 3D module did not load in headless Chromium without the network). Nothing was run to write this file." Its AI-use section: "The page says: this edition was made with Claude, Anthropic's AI model (Claude Opus 5.5), on 28 October 2026 at the request of Robert (Bob) Dickinson, who supplied the app file and asked for it to be imported; responsibility for publishing it is his."

**Claims worth keeping** (all copied from the file)
- An interactive explorer for surfaces built by gluing the edges of a polygon. Type a gluing word such as aba'b' and the app names the surface, computes its Euler characteristic, orientability and boundary count, reduces the word to normal form step by step, and shows the surface as a polygon, a 3D model, a hyperbolic tiling, a walk and a kart race. Not a water-modeling app.
- An independent surface classifier written for the check agrees with the app on 21 of 21 words; all 25 invariant checks printed during six step-by-step reductions read "Surface unchanged"; straight-walk crossing counts match hand predictions on all five flat surfaces. One known issue: on a curved surface the Walk tab's "straight-line distance from start" loses accuracy after about 25 units of walking and is off by up to 0.28 at 36 units (the walking itself is unaffected).
- The supplied file run unmodified in a headless browser to collect every number in the Doc.
- An independent surface classifier against the app on 21 words: 21 agree.
- 25 invariant checks during six reductions; crossing counts on five flat surfaces against hand predictions; a control test of the hyperbolic drawing.
- The same data collection re-run on the edited file returned identical numbers.

**Limits it states.** As the page lists it: the Walk distance readout error on curved surfaces (measurements, cause and the responsible line of code are in the Doc); no person has checked the essay text and its history, the figures, the 3D models, the hyperbolic drawings or the kart physics.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Topology Surface Explorer (app)](../entities/topology-surface-explorer.md), [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Planar graphs and Euler's formula](../concepts/planar-graphs.md).
