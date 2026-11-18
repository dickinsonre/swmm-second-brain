---
title: "S242: Walk the Mesh, summary written from the page (v1.0)"
type: source
raw: raw/apps/walk-the-mesh-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-19
ingested: 2026-11-17
tags: [apps, swmm5, quasi-2d, waves, mesh, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Walk the Mesh, version 1.0: an app adapted from a Perplexity "Clairaut" app about walking on a 4D surface: you stand inside a SWMM quasi-2D mesh (a grid of junctions, storage and conduits) and see where a surge launched from you would be after each second, then run EPA SWMM 5.2.4 in the browser on the same mesh for surge and flood runs. Raw file: [raw/apps/walk-the-mesh-v1.0.md](../../raw/apps/walk-the-mesh-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792425948-1977, reading every tab in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built, tested and written with Claude under Bob's direction; its Notes tab says what Claude did, how it was checked and what has not been checked. The page has Notes and Essay tabs, no About or Doc.

**Claims worth keeping** (all copied from the file)
- A point surge reaches each cell at the wave-ray travel time (slope 0.99 to 1.02 over five still-water worlds) only on a mesh that stores the right water. The obvious quasi-2D mesh in SWMM 5.2.4 stores twice as much, so waves arrive a factor of the square root of 2 (1.414) too late; the fix multiplies Manning's n by 2^(-1/4) = 0.841. The page quotes the code lines behind it from tag v5.2.4.
- Meshes from 30 x 30 to 80 x 80 cells on a 600 x 600 ft domain (8.26 ac); at 60 x 60 cells of 10 ft, 3,600 junctions and storage and 7,080 conduits.
- Lake at rest for 120 s on four beds: max |Q| = 0.000 cfs on all four.
- Every [COORDINATES] entry scrambled: the .out stays byte-identical (9.18 MB).
- Steady sheet flow on a 1 % plane against Manning normal depth: area-true mesh +2.9 to +4.1 %, plain mesh +2.2 to +3.9 %.
- WebAssembly against a native gcc build: byte-identical .out for fixed-step surges; the variable-step flood depth envelope within 0.0007 ft.
- Flood hazard uses the combined H1 to H6 classes of AIDR Guideline 7-3, as used by ARR 2019, converted from SI.

**Limits it states.** No current-carried waves, infiltration, buildings, pipes, or any mesh tool other than the page's own generator.

**Checked at ingest.** 600 x 600 ft = 360,000 ft2 = 8.26 ac. 2^(-1/4) = 0.8409. [Quasi-2D Mesh Maker for SWMM5 (app)](../entities/quasi-2d-mesh-maker.md) reports the same doubling and fixes it with half-width links instead [S241](S241-quasi-2d-mesh-maker-summary.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://walk-the-mesh.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Walk the Mesh (app)](../entities/walk-the-mesh.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md), [Quasi-2D Mesh Maker for SWMM5 (app)](../entities/quasi-2d-mesh-maker.md), [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md), [The SWMM findings register](../concepts/findings-register.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
