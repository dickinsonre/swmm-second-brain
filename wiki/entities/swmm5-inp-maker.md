---
title: SWMM5 INP MAKER (app)
type: entity
updated: 2026-11-15
sources: [S97, S98]
tags: [apps, replit, swmm5, generators, test-models]
reviewed: 11/16/2026
---
Bob's Replit app SWMM5 INP MAKER: an app that generates SWMM5 `.inp` model files from network, terrain, hydrology and unit settings, and can validate, transform, discretize and run them. Version 1.0.0, at `swmm-inp-maker.replit.app` [S98](../sources/S98-swmm5-inp-maker-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S98](../sources/S98-swmm5-inp-maker-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S98](../sources/S98-swmm5-inp-maker-replit-summary.md)
- Generation is seeded: a Mulberry32 random-number generator, with `force_directed` as the default layout method.
- Element counts come from the requested junction count and ratios, for example `conduits = max(N, round(N * conduitRatio))`.
- Counted from the running API: 38 example presets, 276 rainfall patterns and 56 INP sections.
- Simulation calls a local `swmm5` executable identified as EPA SWMM 5.2.4. Time limits are 120 seconds for full mode and 60 seconds for quick mode; quick mode patches the dates for a one-minute structural run.
- A smoke run with seed `321` (generate, validate, transform, quick simulate) returned HTTP 200 at each step.
- The TypeScript check failed with 30 errors. There is no test command: 0 tests run.
- `ReSWMM.md` credits Robert Dickinson for porting ReSWMM and names Robson Leo Pachaly as its original author.

**What it does not show.** Production pages and API were not checked. The SWMM executable's upstream source, commit and license are not recorded. No human engineering review is recorded. [S98](../sources/S98-swmm5-inp-maker-replit-summary.md)

**Noted at ingest.** Both this app and [S97](../sources/S97-swmm5-network-miner-replit-summary.md) carry a ReSWMM discretization tool.

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [SWMM5 Network Miner (app)](swmm5-network-miner.md), [SWMM5 Topology Sandbox (app)](swmm5-topology-sandbox.md), [Fractal SWMM5/SWMM6 Network Generator (app)](fractal-swmm-generator.md).
