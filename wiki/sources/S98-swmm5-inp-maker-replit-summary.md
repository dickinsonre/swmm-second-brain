---
title: "S98: SWMM5 INP MAKER, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-inp-maker-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-07-20
ingested: 2026-11-15
tags: [apps, replit, swmm5, generators, test-models]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 INP MAKER, version 1.0.0: an app that generates SWMM5 `.inp` model files from network, terrain, hydrology and unit settings, and can validate, transform, discretize and run them. It is one of Bob's Replit apps, at `swmm-inp-maker.replit.app`. Raw file: [raw/apps/swmm-inp-maker-v1.0.0.md](../../raw/apps/swmm-inp-maker-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says the recent Git history names Replit Agent as the author of the listed commits. The copy here was read out of the editor of the Replit project named SWMM INP Maker on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Generation is seeded: a Mulberry32 random-number generator, with `force_directed` as the default layout method.
- Element counts come from the requested junction count and ratios, for example `conduits = max(N, round(N * conduitRatio))`.
- Counted from the running API: 38 example presets, 276 rainfall patterns and 56 INP sections.
- Simulation calls a local `swmm5` executable identified as EPA SWMM 5.2.4. Time limits are 120 seconds for full mode and 60 seconds for quick mode; quick mode patches the dates for a one-minute structural run.
- A smoke run with seed `321` (generate, validate, transform, quick simulate) returned HTTP 200 at each step.
- The TypeScript check failed with 30 errors. There is no test command: 0 tests run.
- `ReSWMM.md` credits Robert Dickinson for porting ReSWMM and names Robson Leo Pachaly as its original author.

**Limits it states.** Production pages and API were not checked. The SWMM executable's upstream source, commit and license are not recorded. No human engineering review is recorded.

**Checked at ingest.** Both this app and [S97](S97-swmm5-network-miner-replit-summary.md) carry a ReSWMM discretization tool.

**Feeds:** [SWMM5 INP MAKER (app)](../entities/swmm5-inp-maker.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [SWMM5 Network Miner (app)](../entities/swmm5-network-miner.md), [SWMM5 Topology Sandbox (app)](../entities/swmm5-topology-sandbox.md), [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md).
