---
title: "S326: SWMM5 Network Miner, summary written from the page (v2.0)"
type: source
raw: raw/apps/swmm5-network-miner-v2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10
ingested: 2026-11-18
tags: [apps, swmm5, model-library, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app SWMM5 Network Miner, version 2.0: a library tool for SWMM5 models with EPA SWMM 5.2.4 in the page. Raw file: [raw/apps/swmm5-network-miner-v2.0.md](../../raw/apps/swmm5-network-miner-v2.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/GZspfddPZFMUQx9NWAg3Dv, version 1792949039-0c6d (index.html, 1,591,279 bytes, SHA-256 1723acf9258eb51055a568ebe69c28ad8087209f285755d7d71b44b8cf04b8d6), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who wrote and ran the original Replit app, supplied its source, and asked for this single-file edition; responsibility is his."

**Claims worth keeping** (all copied from the file)
- Load a pile of .inp files, see what is in them, check them, compare them, cut long conduits with ReSWMM, and run any of them in EPA SWMM 5.2.4, all in one HTML file with nothing leaving the browser. A single-file edition of Bob's Replit app SWMM5 Network Miner, which kept models in PostgreSQL and Replit Object Storage behind an Express server and whose browser engine was 5.1.015.
- The Audit lists ReSWMM defects R1 to R11 (junction rows, cross-sections, offsets, rims and references written wrongly), now fixed, with unit conversion for SI models and a CFL time-step preview. "AI Analysis" is renamed Health Check because it is a rule list; a new rule catches the rain-gage interval mistake in all five samples. The page hashes the wasm it decodes and shows that it matches the build (e448f692...).
- A Node suite, engine runs and a headless-browser test (described in the Doc).
- Every run's .rpt header reads "VERSION 5.2 (Build 5.2.4)"; the page computes the SHA-256 of the wasm it decodes and shows it next to the build hash (matching hashes show the bytes are the bytes built; they are not a signature).
- The Replit source read line by line for the Audit findings.

**Limits it states.** As the page lists it: a clean run is not a correct model (nothing here knows where the city put its pipes, whether roughness was calibrated, or whether the storm is the one the permit asked for); XP files are kept, shown and searched but not parsed; EPA SWMM 5.2.4 only, not SWMM 5.1, OpenSWMM 6 or InfoWorks ICM; ReSWMM's interior junctions are computational points. No person has run this edition against Bob's full thousand-model library, and the 0.10 conservative time-step factor in the ReSWMM spec has not been checked against the paper it cites.

**Checked at ingest.** A single-file edition of the Replit app summarized in [S97](S97-swmm5-network-miner-replit-summary.md); the file's name carries "(single-file edition)" so the two are not grouped as versions of one app. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [SWMM5 Network Miner (app)](../entities/swmm5-network-miner.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Reading SWMM output](../concepts/reading-swmm-output.md).
