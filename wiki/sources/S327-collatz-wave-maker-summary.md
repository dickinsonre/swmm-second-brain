---
title: "S327: Collatz Wave Maker, summary written from the page (v2.0)"
type: source
raw: raw/apps/collatz-wave-maker-v2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, swmm5, generators, trees, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Collatz Wave Maker, version 2.0: the Collatz tree as a branching sewer, run in EPA SWMM 5.2.4. Raw file: [raw/apps/collatz-wave-maker-v2.0.md](../../raw/apps/collatz-wave-maker-v2.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/2JaLQCeuvWaqSSPYvzBDmF, version 1792949717-9747 (index.html, 1,009,724 bytes, SHA-256 7ff0bf51c52ce383adf80588c723fcda545a90c9184bf7eef82c5854dfc8d527), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude Code session on 25 October 2026 under the direction of Robert (Bob) Dickinson, who wrote the Lovable original, supplied its source zip and asked for a single-file HTML app; responsibility is his."

**Claims worth keeping** (all copied from the file)
- Every whole number from 2 to N, halved when even and tripled plus one when odd, drains to 1, so the numbers form a tree with one outlet per node, like a branching sewer. The page turns that tree into an EPA SWMM5 input file, runs it in EPA SWMM 5.2.4 compiled to WebAssembly, and plays the flood wave back over the tree in eleven layouts.
- The Lovable original ran EPA SWMM 5.2.2, not 5.2.4: every report header read "VERSION 5.2 (Build 5.2.2)", and the same .inp gives 198 against 197 flooded nodes and 0.059 against 0.060% continuity on 5.2.2 and 5.2.4. Twelve defects are listed on the Audit tab with the original lines, among them flooding and surcharge tables that read the node ID as the first number.
- 337 Node checks of the ported generator: tree facts (27 takes 111 steps; N = 100 gives 251 nodes; every conduit drops exactly one step), storm depth conserved to 10^-9 for all three hyetographs, ten engine configurations returning code 0 with the .out parser agreeing with the .rpt continuity line, first report period at 5 min, no overlapping subcatchment polygons in any of the eleven layouts.
- Each Audit item reproduced by running the original TypeScript (bundled with esbuild) against the original engine.
- Headless Chromium: boots dark, runs N = 100 to completion in the worker, fills every tab, switches theme, no page errors.

**Limits it states.** As the page lists it: not a real drainage system; the network, elevations, inflows and catchments are generated from a number-theory rule.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Collatz Wave Maker (app)](../entities/collatz-wave-maker.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md), [Cycles and trees](../concepts/graph-cycles-and-trees.md).
