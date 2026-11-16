---
title: SWMM5 MicroGPT (app)
type: entity
updated: 2026-11-15
sources: [S114]
tags: [apps, replit, swmm5, ai, inp-files]
reviewed: 11/16/2026
---
Bob's Replit app SWMM5 MicroGPT v2: an app that parses SWMM5 `.INP` text, trains a small character-level GPT on it in the browser and generates SWMM-like names. Version 2, at `micro-gpt-swmm.replit.app` [S114](../sources/S114-swmm5-microgpt-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S114](../sources/S114-swmm5-microgpt-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S114](../sources/S114-swmm5-microgpt-replit-summary.md)
- It runs no SWMM5 hydraulic or hydrologic simulation. `engines: none`.
- The parser tracks section headers and extracts node, link and subcatchment identifiers, keywords and short parameter lines.
- Training builds a character vocabulary, calculates next-character loss and updates parameters with Adam-style moment estimates and a linearly reduced learning rate.
- One training set is 500 Manning triplets from circular full-pipe geometry: `A = πD²/4`, `R = D/4`, `Q = (1/n) × A × R^(2/3) × S^(1/2)`.
- The sample and generated `.INP` settings are SI, with `FLOW_UNITS CMS` and map units in meters. No US customary calculation path is present.
- Two fixed vocabulary sets: 92 SWMM keyword strings and 40 node-name strings, 132 entries in all. One imported Greenville `.INP` sample.
- Five tab panels: Data, Train, Generate, Compare and Help.
- It can assemble and download a sample file, `microgpt_generated.inp`, from generated identifiers and fixed example data. That output was not checked with a SWMM engine.
- `npm run check` reported six TS2802 errors. `npm test` ran no tests because no test script is defined.
- The app credits Andrej Karpathy's `micrograd`, Xenova's `microgpt.js` and SWMM5.org. The project declares MIT.

**What it does not show.** Training, upload, comparison, generation and download were not exercised. Only the root page was loaded. The production build was not run. No formal release date is recorded; the `date:` is the newest date in the Git history. [S114](../sources/S114-swmm5-microgpt-replit-summary.md)

**Noted at ingest.** The `version:` is the bare number 2, and the app name carries "v2" (Q75).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [EPA SWMM 5](swmm-5.md), [SWMM5 Rosetta Stone, also called Code Rosetta Stone (app)](code-rosetta-stone.md).
