---
title: PySWMM Explorer (app)
type: entity
updated: 2026-11-15
sources: [S130]
tags: [apps, replit, pyswmm, reference]
reviewed: no
---
Bob's Replit app PySWMM Explorer: a reference and learning app for PySWMM: API module notes, a phrasebook, cookbook examples, ecosystem references and a repository outline. Version 1.0.0, at `pyswmm-explorer.replit.app` [S130](../sources/S130-pyswmm-explorer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S130](../sources/S130-pyswmm-explorer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S130](../sources/S130-pyswmm-explorer-replit-summary.md)
- It runs no SWMM or Python engine. The Playground prints sample console lines from a timer and a fixed depth pattern; it does not parse or execute the user's Python code, and its completion summary is hard-coded.
- The Parameter Explorer makes a synthetic hourly depth series, `depth_next = max(0, depth + rain - drain - pumpDrain + noise)`, which the file calls illustrative, not a calibrated model.
- Ten tab views. Eight API modules and fifty cookbook examples. Sixty phrasebook entries in eight categories. Five repository folders with thirty-six described files.
- No API endpoints are registered and no database connection is used.
- `npm run check` and `npm run build` passed. No test script exists.
- It links to https://github.com/SWMMEnablement/pyswmm and shows BSD-2-Clause for the PySWMM project. The app package declares MIT.

**What it does not show.** Real PySWMM execution and `.inp` loading were not checked. The individual tabs were not opened. External links were not followed. The license terms of swmm-toolkit and EPA SWMM5 are not stated in the source. [S130](../sources/S130-pyswmm-explorer-replit-summary.md)

**Noted at ingest.** The `repo:` in the front matter, SWMMEnablement/pyswmm, is the repository the app links to for PySWMM; the file does not say it holds this app's source (Q79).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM5 Network Miner (app)](swmm5-network-miner.md), [SWMM5 Explorer (app)](swmm5-explorer.md).
