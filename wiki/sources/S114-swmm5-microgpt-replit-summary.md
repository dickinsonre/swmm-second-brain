---
title: "S114: SWMM5 MicroGPT v2, summary written by Replit Agent (v2)"
type: source
raw: raw/apps/micro-gpt-swmm-v2.md
kind: app-md
author: Robert Dickinson
published: 2026-02-16
ingested: 2026-11-15
tags: [apps, replit, swmm5, ai, inp-files]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 MicroGPT v2, version 2: an app that parses SWMM5 `.INP` text, trains a small character-level GPT on it in the browser and generates SWMM-like names. It is one of Bob's Replit apps, at `micro-gpt-swmm.replit.app`. Raw file: [raw/apps/micro-gpt-swmm-v2.md](../../raw/apps/micro-gpt-swmm-v2.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the inspected code and documentation do not identify a coding AI. The copy here was read out of the editor of the Replit project named MicroGPT SWMM on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** Training, upload, comparison, generation and download were not exercised. Only the root page was loaded. The production build was not run. No formal release date is recorded; the `date:` is the newest date in the Git history.

**Checked at ingest.** The `version:` is the bare number 2, and the app name carries "v2" (Q75).

**Feeds:** [SWMM5 MicroGPT (app)](../entities/swmm5-microgpt.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [EPA SWMM 5](../entities/swmm-5.md), [SWMM5 Rosetta Stone, also called Code Rosetta Stone (app)](../entities/code-rosetta-stone.md).
