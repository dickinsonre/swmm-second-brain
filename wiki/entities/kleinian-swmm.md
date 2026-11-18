---
title: "Kleinian SWMM (app)"
type: entity
updated: 2026-11-17
sources: [S205, S227]
tags: [apps, swmm5, generators, kinematic-wave, wasm]
reviewed: no
---
Bob's app Kleinian SWMM: a generator that grows a storm sewer from a Kleinian (Schottky) group, or in a second mode from a finite group mod p: tiles become subcatchments, orbit points junctions and arcs conduits, written as a SWMM5 .inp and run in the page on EPA SWMM 5.2.4 with Bob's KW/SF extension, compiled to WebAssembly. Version 1.6.1, 2026-11-03 [S227](../sources/S227-kleinian-swmm-summary.md). Netlify address: https://kleinian-swmm.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S227](../sources/S227-kleinian-swmm-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S227](../sources/S227-kleinian-swmm-summary.md)
- Default Pearl necklace, 1,553 ac and 324 subcatchments, a 2-hour storm of 1.97 in: dynamic wave peaked at 1,469 cfs 51 minutes in; kinematic wave 1,474 cfs; steady flow 1,480 cfs. The rational method gives 1,638 cfs; the routed peaks come in about 10 % under it.
- Conduits are sized by the rational method at one design intensity on the whole upstream area, with no time-of-concentration reduction, so trunk conduits come out larger than the routed peaks need.
- The KW/SF extension lets kinematic wave and steady flow handle multi-outlet junctions and loops; Schottky networks are trees, so on them results are stock 5.2.4's.
- Finite mode: 15 register rules pass at all five moduli; Euler's V - E + F = 2 - 2g is checked against the genus (-4 at p = 7).
- A separate Python script with shapely intersected every neighbouring pair of exported polygons (49, 415, 898, 9,373 and 27,213 pairs): zero area shared.
- Native EPA SWMM 5.2.4 ran all five finite-mode files with no warnings or errors, routing continuity -0.002 % to -0.016 %; the WebAssembly .out matched native byte for byte at p = 5 and 7.

**What it does not show.** Not a good design. No terrain, real rain or real soil. Two presets cross themselves, and the register says so. At p = 11 and 13 the maps are stretched (worst tile tip 129 to 1 and 358 to 1). The [Polygons] are cartography the engine never reads. [S227](../sources/S227-kleinian-swmm-summary.md)

**Noted at ingest.** (1,638 - 1,469) / 1,638 = 10.3 %, the "about 10 % under" of the page. The extension is [swmm5-kw](swmm5-kw.md).

See [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [swmm5-kw](swmm5-kw.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Planar graphs and Euler's formula](../concepts/planar-graphs.md), [Fractal SWMM5/SWMM6 Network Generator (app)](fractal-swmm-generator.md).
