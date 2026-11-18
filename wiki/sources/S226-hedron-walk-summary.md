---
title: "S226: Hedron Walk, summary written from the page (v1.7.0)"
type: source
raw: raw/apps/hedron-walk-v1.7.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-31
ingested: 2026-11-17
tags: [apps, swmm5, generators, rule-30, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Hedron Walk, version 1.7.0: a generator that turns a picture of a winding path tiled with triangles (and a second picture, the Mobius gimbal) into a SWMM5 model, a ribbon about 3,600 ft by 300 ft with 1,408 subcatchments, 21 trunk pipes, a vortex chamber, a ring pond, an orifice, a weir and two outfalls, run on EPA SWMM 5.2.4 in the page. Rule 30 decides which triangles are paved. Raw file: [raw/apps/hedron-walk-v1.7.0.md](../../raw/apps/hedron-walk-v1.7.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793467105-9cfa, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude (Claude Opus 5.5) in a claude.ai session on 27 October 2026 under Bob's direction: Bob supplied the picture and its text and asked for a SWMM5 .inp generator that looks like it; Claude chose how to read the picture's numbers as geometry, discarding a first spiral reading, and wrote the generator and checks.

**Claims worth keeping** (all copied from the file)
- A hedron at level k has an edge 1/2^k of the base, and one base triangle holds 4^k of them; the centre child is the parent turned 180 degrees about its centroid and halved. The counts, addresses and parity were checked at every level; the half-turn holds to 9 x 10^-13 ft.
- Default ribbon: 4.115 ac-ft of rain on 24.69 ac, 2.526 ac-ft of runoff (about 61 percent); inflow to the ring pond peaks at 28.5 cfs about 1 h 05 min in; the pond rises to 3.84 ft of its 8.00 at about 1 h 50 min; its orifice peaks at 7.5 cfs.
- Three Rule 30 carpets pave 49.9, 49.8 and 49.6 percent, with runoff 2.526, 2.522 and 2.514 ac-ft.
- No overlap: every face and subcatchment keeps positive area, the outline never crosses itself, and the tightest bend, 284 ft, exceeds the 150 ft half-width. The subcatchments add to 24.69 ac, within 0.02 percent of the smooth outline.
- The storm: a triangular hyetograph, 2 in in 2 hours peaking at 2 in/hr at 45 minutes; trunk sized by Q = CiA and Manning full-pipe flow at n 0.013, never shrinking downstream.

**Limits it states.** Not a design: sizing is the rational method on a synthetic storm. The picture's text about quantum computing plays no part.

**Checked at ingest.** 2 in over 24.69 ac is 4.115 ac-ft, and 2.526 / 4.115 = 61 %. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://hedron-walk.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Hedron Walk (app)](../entities/hedron-walk.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md), [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md).
