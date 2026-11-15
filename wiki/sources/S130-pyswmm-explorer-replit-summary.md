---
title: "S130: PySWMM Explorer, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/pyswmm-explorer-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-02-11
ingested: 2026-11-15
tags: [apps, replit, pyswmm, reference]
reviewed: no
---
**What it is.** A technical summary of PySWMM Explorer, version 1.0.0: a reference and learning app for PySWMM: API module notes, a phrasebook, cookbook examples, ecosystem references and a repository outline. It is one of Bob's Replit apps, at `pyswmm-explorer.replit.app`. Raw file: [raw/apps/pyswmm-explorer-v1.0.0.md](../../raw/apps/pyswmm-explorer-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the Git log attributes its recent commits to Robert Dickinson and that no AI tool is identified. The copy here was read out of the editor of the Replit project named Pyswmm Explorer on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It runs no SWMM or Python engine. The Playground prints sample console lines from a timer and a fixed depth pattern; it does not parse or execute the user's Python code, and its completion summary is hard-coded.
- The Parameter Explorer makes a synthetic hourly depth series, `depth_next = max(0, depth + rain - drain - pumpDrain + noise)`, which the file calls illustrative, not a calibrated model.
- Ten tab views. Eight API modules and fifty cookbook examples. Sixty phrasebook entries in eight categories. Five repository folders with thirty-six described files.
- No API endpoints are registered and no database connection is used.
- `npm run check` and `npm run build` passed. No test script exists.
- It links to https://github.com/SWMMEnablement/pyswmm and shows BSD-2-Clause for the PySWMM project. The app package declares MIT.

**Limits it states.** Real PySWMM execution and `.inp` loading were not checked. The individual tabs were not opened. External links were not followed. The license terms of swmm-toolkit and EPA SWMM5 are not stated in the source.

**Checked at ingest.** The `repo:` in the front matter, SWMMEnablement/pyswmm, is the repository the app links to for PySWMM; the file does not say it holds this app's source (Q79).

**Feeds:** [PySWMM Explorer (app)](../entities/pyswmm-explorer.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM5 Network Miner (app)](../entities/swmm5-network-miner.md), [SWMM5 Explorer (app)](../entities/swmm5-explorer.md).
