---
title: "Collatz Wave Maker (app)"
type: entity
updated: 2026-11-18
sources: [S327]
tags: [apps, swmm5, generators, trees, wasm]
reviewed: no
---
Bob's app Collatz Wave Maker: the Collatz tree as a branching sewer, run in EPA SWMM 5.2.4. Version 2.0, 2026-10-25 [S327](../sources/S327-collatz-wave-maker-summary.md). Its `links:` line names no live Netlify address [S327](../sources/S327-collatz-wave-maker-summary.md).

**A caution about its source.** The page ships no technical summary. [S327](../sources/S327-collatz-wave-maker-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S327](../sources/S327-collatz-wave-maker-summary.md)
- Every whole number from 2 to N, halved when even and tripled plus one when odd, drains to 1, so the numbers form a tree with one outlet per node, like a branching sewer. The page turns that tree into an EPA SWMM5 input file, runs it in EPA SWMM 5.2.4 compiled to WebAssembly, and plays the flood wave back over the tree in eleven layouts.
- The Lovable original ran EPA SWMM 5.2.2, not 5.2.4: every report header read "VERSION 5.2 (Build 5.2.2)", and the same .inp gives 198 against 197 flooded nodes and 0.059 against 0.060% continuity on 5.2.2 and 5.2.4. Twelve defects are listed on the Audit tab with the original lines, among them flooding and surcharge tables that read the node ID as the first number.
- 337 Node checks of the ported generator: tree facts (27 takes 111 steps; N = 100 gives 251 nodes; every conduit drops exactly one step), storm depth conserved to 10^-9 for all three hyetographs, ten engine configurations returning code 0 with the .out parser agreeing with the .rpt continuity line, first report period at 5 min, no overlapping subcatchment polygons in any of the eleven layouts.
- Each Audit item reproduced by running the original TypeScript (bundled with esbuild) against the original engine.
- Headless Chromium: boots dark, runs N = 100 to completion in the worker, fills every tab, switches theme, no page errors.

**How to use it, as the summary puts it.** Use it as a stress test and a teaching toy for tree networks (N up to 5,000). The network, elevations, inflows and catchments come from a number-theory rule, not from any place. [S327](../sources/S327-collatz-wave-maker-summary.md)

**What it does not show.** As the page lists it: not a real drainage system; the network, elevations, inflows and catchments are generated from a number-theory rule. [S327](../sources/S327-collatz-wave-maker-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Fractal SWMM5/SWMM6 Network Generator (app)](fractal-swmm-generator.md), [Cycles and trees](../concepts/graph-cycles-and-trees.md).
