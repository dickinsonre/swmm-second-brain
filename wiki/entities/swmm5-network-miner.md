---
title: SWMM5 Network Miner (app)
type: entity
updated: 2026-11-18
sources: [S97, S326]
tags: [apps, replit, swmm5, model-library, pyswmm]
reviewed: 11/16/2026
changed_after_review: "2026-11-18 (S300 to S375 ingest): a paragraph added near the end, headed Added 18 November 2026 (S326, S97)"
---
Bob's Replit app SWMM5 Network Miner: an app for organizing, searching, inspecting, comparing and running a library of SWMM model files. Version 1.0.0, at `swmm-filebase--robertdickinson.replit.app` [S97](../sources/S97-swmm5-network-miner-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S97](../sources/S97-swmm5-network-miner-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S97](../sources/S97-swmm5-network-miner-replit-summary.md)
- It accepts `.inp` and `.xp` uploads, with optional `.rpt` and `.out` results.
- A health score starts at 100, loses 15 per error, 5 per warning and 1 per informational finding, and is clamped to 0 to 100.
- Pipe diameter values below 10 are treated as feet and converted to inches.
- Its ReSWMM tool splits a conduit into `max(1, ceil(conduit length / target length))` equal segments.
- The server runs a model with `pyswmm.Simulation`. The front matter gives PySWMM 2.1.0 and swmm-toolkit 0.17.0. A bundled browser WebAssembly SWMM module has no stated version and its license was not checked.
- The development database on 15 November 2026 held 2,001 `.inp` records, 0 `.xp` records, 36 directories, 878 result-file records and 0 simulation-job records.
- `npm run build` passed. `npm run check` failed with 19 TypeScript `TS2802` diagnostics. No test script is defined.
- No AI model API call was found; the QA/QC feature is rule-based.
- Repository: https://github.com/dickinsonre/SWMM-Filebase.

**What it does not show.** The production database and the production page were not checked. Running a simulation and uploading an `.xp` file were not tested. A consistent unit conversion for all quantities was not found. [S97](../sources/S97-swmm5-network-miner-replit-summary.md)

**Noted at ingest.** The pages it loaded include one at `/ai-analysis`, and it found no AI call in the app. The display name, the project name and the site name are three different names (Q70).

**Added 18 November 2026.** A single-file edition, version 2.0 [S326](../sources/S326-swmm5-network-miner-summary.md), carries EPA SWMM 5.2.4 in the page. Its audit lists ReSWMM defects R1 to R11 (junction rows, cross-sections, offsets, rims and references written wrongly), now fixed, with unit conversion for SI models and a CFL time-step preview; "AI Analysis" is renamed Health Check because it is a rule list [S326](../sources/S326-swmm5-network-miner-summary.md). The edition is a separate file from the Replit app summarized in [S97](../sources/S97-swmm5-network-miner-replit-summary.md), not a later version of it.

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [SWMM5 INP MAKER (app)](swmm5-inp-maker.md), [EPA SWMM 5](swmm-5.md).
