---
title: "S227: Kleinian SWMM, summary written from the page (v1.6.1)"
type: source
raw: raw/apps/kleinian-swmm-v1.6.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-03
ingested: 2026-11-17
tags: [apps, swmm5, generators, kinematic-wave, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Kleinian SWMM, version 1.6.1: a generator that grows a storm sewer from a Kleinian (Schottky) group, or in a second mode from a finite group mod p: tiles become subcatchments, orbit points junctions and arcs conduits, written as a SWMM5 .inp and run in the page on EPA SWMM 5.2.4 with Bob's KW/SF extension, compiled to WebAssembly. Raw file: [raw/apps/kleinian-swmm-v1.6.1.md](../../raw/apps/kleinian-swmm-v1.6.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793713941-5b65, reading its Doc tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app, its engine extension and the essay were made with Claude under Bob's direction: Bob asked on 28 September 2026 whether the circles of Indra's Pearls (Mumford, Series and Wright, 2002) could be a storm sewer, then for non-overlapping outlines, the modified engine, the finite-group mode (2 November 2026) and an outside review of it (3 November 2026). Claude wrote all of the code. The page has no About tab; only its Doc tab was read.

**Claims worth keeping** (all copied from the file)
- Default Pearl necklace, 1,553 ac and 324 subcatchments, a 2-hour storm of 1.97 in: dynamic wave peaked at 1,469 cfs 51 minutes in; kinematic wave 1,474 cfs; steady flow 1,480 cfs. The rational method gives 1,638 cfs; the routed peaks come in about 10 % under it.
- Conduits are sized by the rational method at one design intensity on the whole upstream area, with no time-of-concentration reduction, so trunk conduits come out larger than the routed peaks need.
- The KW/SF extension lets kinematic wave and steady flow handle multi-outlet junctions and loops; Schottky networks are trees, so on them results are stock 5.2.4's.
- Finite mode: 15 register rules pass at all five moduli; Euler's V - E + F = 2 - 2g is checked against the genus (-4 at p = 7).
- A separate Python script with shapely intersected every neighbouring pair of exported polygons (49, 415, 898, 9,373 and 27,213 pairs): zero area shared.
- Native EPA SWMM 5.2.4 ran all five finite-mode files with no warnings or errors, routing continuity -0.002 % to -0.016 %; the WebAssembly .out matched native byte for byte at p = 5 and 7.

**Limits it states.** Not a good design. No terrain, real rain or real soil. Two presets cross themselves, and the register says so. At p = 11 and 13 the maps are stretched (worst tile tip 129 to 1 and 358 to 1). The [Polygons] are cartography the engine never reads.

**Checked at ingest.** (1,638 - 1,469) / 1,638 = 10.3 %, the "about 10 % under" of the page. The extension is [swmm5-kw](../entities/swmm5-kw.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://kleinian-swmm.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Kleinian SWMM (app)](../entities/kleinian-swmm.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [swmm5-kw](../entities/swmm5-kw.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Planar graphs and Euler's formula](../concepts/planar-graphs.md), [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md).
