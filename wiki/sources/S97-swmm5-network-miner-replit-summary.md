---
title: "S97: SWMM5 Network Miner, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-filebase--robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, model-library, pyswmm]
reviewed: no
---
**What it is.** A technical summary of SWMM5 Network Miner, version 1.0.0: an app for organizing, searching, inspecting, comparing and running a library of SWMM model files. It is one of Bob's Replit apps, at `swmm-filebase--robertdickinson.replit.app`. Raw file: [raw/apps/swmm-filebase--robertdickinson-v1.0.0.md](../../raw/apps/swmm-filebase--robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says Git history names Replit Agent on several commits. The copy here was read out of the editor of the Replit project named SWMM Filebase on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It accepts `.inp` and `.xp` uploads, with optional `.rpt` and `.out` results.
- A health score starts at 100, loses 15 per error, 5 per warning and 1 per informational finding, and is clamped to 0 to 100.
- Pipe diameter values below 10 are treated as feet and converted to inches.
- Its ReSWMM tool splits a conduit into `max(1, ceil(conduit length / target length))` equal segments.
- The server runs a model with `pyswmm.Simulation`. The front matter gives PySWMM 2.1.0 and swmm-toolkit 0.17.0. A bundled browser WebAssembly SWMM module has no stated version and its license was not checked.
- The development database on 15 November 2026 held 2,001 `.inp` records, 0 `.xp` records, 36 directories, 878 result-file records and 0 simulation-job records.
- `npm run build` passed. `npm run check` failed with 19 TypeScript `TS2802` diagnostics. No test script is defined.
- No AI model API call was found; the QA/QC feature is rule-based.
- Repository: https://github.com/dickinsonre/SWMM-Filebase.

**Limits it states.** The production database and the production page were not checked. Running a simulation and uploading an `.xp` file were not tested. A consistent unit conversion for all quantities was not found.

**Checked at ingest.** The pages it loaded include one at `/ai-analysis`, and it found no AI call in the app. The display name, the project name and the site name are three different names (Q70).

**Feeds:** [SWMM5 Network Miner (app)](../entities/swmm5-network-miner.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [SWMM5 INP MAKER (app)](../entities/swmm5-inp-maker.md), [EPA SWMM 5](../entities/swmm-5.md).
