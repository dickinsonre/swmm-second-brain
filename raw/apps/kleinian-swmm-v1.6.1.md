---
name: Kleinian SWMM
file: kleinian-swmm.html
version: 1.6.1
date: 2026-11-03
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/SrvQ5KtPf4Rwx6N7L8Kom1", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "compiled to WebAssembly with the KW/SF v1.1 extension from github.com/SWMMBobSWMM6/swmm5-kw", license: public domain}
units: US customary (ac, in, cfs, ft)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app, its engine extension and its essay were made with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/SrvQ5KtPf4Rwx6N7L8Kom1, version 1793713941-5b65 (index.html, 8,519,283 bytes, SHA-256 3f89f49563c1c37a6dda7388e24e2714956fbcfd3a7224ad37e3c1db069ed11a), its Doc tab read in headless Chromium on 2026-11-17 (the page has no About tab). No model was run to write this file; the date is the artifact's publish date."
---

# Kleinian SWMM: two Mobius maps and their inverses, drawn as a runnable SWMM5 network

## In three points
- **What:** Grows a storm sewer from a Kleinian (Schottky) group, or in a second mode from a finite group mod p: tiles become subcatchments, orbit points junctions and arcs conduits, written as a SWMM5 .inp and run in the page on EPA SWMM 5.2.4 compiled to WebAssembly.
- **So what:** The default necklace (1,553 ac, 324 subcatchments, a 1.97 in 2-hour storm) peaks at 1,469 cfs under dynamic wave, 1,474 under kinematic wave and 1,480 under steady flow, against 1,638 cfs by the rational method; a separate shapely check found zero shared area between neighbouring outlines.
- **Now what:** Use it for valid test networks with exact areas, sizes that grow downstream and no crossings. They are not designs: sizing is rational-method on uniform synthetic rain, and elevations come from slopes, not terrain.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.6.1"); the date is the artifact's. Every number below is copied from the page's Doc essay. No model was run to write this file.

## What it does

Bob asked on 28 September 2026 whether the nesting circles of Indra's Pearls (Mumford, Series and Wright, 2002) could be a storm sewer: a real network the engine runs to the end. The app answers yes under three rules: the areas add up, pipes get bigger downstream, and no two pipes cross. IDs spell A as x and B as y because SWMM IDs are case-blind. Tabs: Design, Network (a register of rules rerun on every change), Run SWMM, Your model (load your own network), Export, Doc.

## How it computes (as the page describes it)

- Two Mobius maps a, b and their inverses build a word tree, largest disk first, stopping at a radius rho; tiles w(F), orbit points w(p0) and arcs w(edge) become subcatchments, junctions and conduits; the limit set below rho is folded into the last tiles.
- Conduits are sized by the rational method at one design intensity on the whole upstream area, with no time-of-concentration reduction.
- Elevations come from the conduit slopes; each junction's rim is its invert plus the largest connected conduit plus the cover.
- The engine's KW/SF extension lets kinematic wave and steady flow handle multi-outlet junctions and loops; Schottky networks are trees, so on them results are stock 5.2.4's.
- Finite mode (added 2 November 2026) builds the group mod p on a hyperbolic surface; Euler's V - E + F = 2 - 2g is checked against the genus (-4 at p = 7).

## Results the page reports

- Default Pearl necklace, 1,553 ac and 324 subcatchments, 2-hour design storm of 1.97 in, run on 31 October 2026: dynamic wave peaked at 1,469 cfs 51 minutes in; kinematic wave 1,474 cfs; steady flow 1,480 cfs. The rational method (whole area at the worst 5-minute intensity) gives 1,638 cfs; the routed peaks come in about 10% under it.

## Checks (as stated on the page)

- Finite mode: 15 register rules (closure, the relations, three pipes at every junction, Euler characteristic, telescoping area, downhill pipes, matched crowns, sizes, IDs, outlines, crossings, the written file) pass at all five moduli.
- A separate Python script with shapely intersected every neighbouring pair of exported polygons: 49, 415, 898, 9,373 and 27,213 pairs, zero area shared.
- Native EPA SWMM 5.2.4 ran all five files with no warnings or errors; routing continuity between -0.002% and -0.016%.
- The WebAssembly engine wrote a .out byte-identical to native at p = 5 and 7.
- The Schottky mode did not move: the default necklace exports 31,781 lines.

## What this does not show

- That the network is a good design; trunk conduits come out larger than the routed peaks need.
- Terrain, real rain or real soil.
- The limit set itself.
- The [Polygons] are cartography; the engine never reads them.
- That every twist embeds: two presets cross themselves, and the register says so.
- At p = 11 and 13 the models are sound but the maps are stretched (worst tile tip 129 to 1 and 358 to 1; 5 to 1 at p = 7).

## How to reproduce

Open the page, pick a preset on Design, and run it on Run SWMM; Export writes the .inp. Your model loads a network of your own.

## Credits and licenses

EPA SWMM 5.2.4 (public domain) with Bob's swmm5-kw extension. Mumford, Series and Wright (2002), Indra's Pearls. No license is stated for the page.

## AI use

The page says the app, its engine extension and the essay were made with Claude, Anthropic's AI model, under the direction of Robert (Bob) Dickinson, who asked on 28 September 2026 for SWMM networks grown from a Kleinian group, then for non-overlapping outlines, tooltips, the modified engine, loading his own models, fixes from reviews, a rotating map, the Doc tab, the finite-group mode (2 November 2026) and an outside review of it (3 November 2026). Claude wrote all of the code. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.6.1: current version as published. The page records versions 1.1 to 1.6 in its text; the finite mod p mode was added on 2 November 2026 and an outside review of it on 3 November 2026.
