---
name: Collatz Wave Maker
file: collatz-wave-maker.html
version: "2.0"
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/2JaLQCeuvWaqSSPYvzBDmF", original: "Lovable app collatz-wave-maker (SWMMEnablement collection, MIT)", repo: none named for this edition}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4, commit 7952ca8379", build: "Emscripten 3.1.51, -O2, single-file; 678,177 bytes, SHA-256 pinned and checked in the page; the same build as Seven SWMM Engines", license: public domain}
units: US customary (ft, cfs)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session on 25 October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/2JaLQCeuvWaqSSPYvzBDmF, version 1792949717-9747 (index.html, 1,009,724 bytes, SHA-256 7ff0bf51c52ce383adf80588c723fcda545a90c9184bf7eef82c5854dfc8d527), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Collatz Wave Maker: the Collatz tree as a branching sewer, run in EPA SWMM 5.2.4

## In three points
- **What:** Every whole number from 2 to N, halved when even and tripled plus one when odd, drains to 1, so the numbers form a tree with one outlet per node, like a branching sewer. The page turns that tree into an EPA SWMM5 input file, runs it in EPA SWMM 5.2.4 compiled to WebAssembly, and plays the flood wave back over the tree in eleven layouts.
- **So what:** The Lovable original ran EPA SWMM 5.2.2, not 5.2.4: every report header read "VERSION 5.2 (Build 5.2.2)", and the same .inp gives 198 against 197 flooded nodes and 0.059 against 0.060% continuity on 5.2.2 and 5.2.4. Twelve defects are listed on the Audit tab with the original lines, among them flooding and surcharge tables that read the node ID as the first number.
- **Now what:** Use it as a stress test and a teaching toy for tree networks (N up to 5,000). The network, elevations, inflows and catchments come from a number-theory rule, not from any place.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v2.0"); the date is the build session the page names. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Presets N = 10, 27, 100, 1000 and a 5,000 stress run; Run SWMM5 in a worker. Tabs: Tree, Wave, Profile, Results, INP, Sizing, Lab, History, Audit, About, Doc. Inputs: layout (symmetric bloom, radial rings, Reingold-Tilford, dendrogram, sunburst, force-directed, Sugiyama, Ulam spiral, arc diagram, stopping-time isochrone, parity grid; map only, no effect on hydraulics), diameter, Manning's n, conduit length, invert drop per step, manhole depth, outfall invert, progressive sizing D x √(upstream nodes), and a trapezoidal inflow on chosen nodes. Everything the Lovable app did is kept: generator, validator, engine runner, HGL and profile views, sizing, batch, regression lab, history and comparison.

## Checks (as stated on the page)

- 337 Node checks of the ported generator: tree facts (27 takes 111 steps; N = 100 gives 251 nodes; every conduit drops exactly one step), storm depth conserved to 10^-9 for all three hyetographs, ten engine configurations returning code 0 with the .out parser agreeing with the .rpt continuity line, first report period at 5 min, no overlapping subcatchment polygons in any of the eleven layouts.
- Each Audit item reproduced by running the original TypeScript (bundled with esbuild) against the original engine.
- Headless Chromium: boots dark, runs N = 100 to completion in the worker, fills every tab, switches theme, no page errors.

## What this does not show

As the page lists it: not a real drainage system; the network, elevations, inflows and catchments are generated from a number-theory rule.

## Credits and licenses

EPA SWMM 5.2.4, U.S. EPA (public domain), tag v5.2.4; the Lovable collatz-wave-maker (MIT, © Robert Dickinson). No separate license is stated for this edition.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who wrote the Lovable original, supplied its source zip and asked for a single-file HTML app; responsibility is his. Claude read the Lovable source, ran the original generator and engine in Node to find the Audit defects, ported the generator to plain JavaScript and fixed them, embedded the 5.2.4 WebAssembly build from Bob's Seven SWMM Engines page, and wrote every view, the GIF encoder, the tests, the Doc essay and the .docx. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.0 (2026-10-25): single-file edition with a verified 5.2.4 engine and twelve Audit fixes (the version read).
- 1 (Lovable): the original collatz-wave-maker.
