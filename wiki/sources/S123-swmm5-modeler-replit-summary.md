---
title: "S123: SWMM5 Modeler, summary written by Replit Agent (v0.0.0)"
type: source
raw: raw/apps/mirofish-swmm-v0.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, wasm, engines, model-generation]
reviewed: no
---
**What it is.** A technical summary of SWMM5 Modeler, version 0.0.0: an app that generates, scales up or imports a drainage network, runs it in EPA SWMM5 compiled to WebAssembly, and reports results, errors, proposed fixes and a model grade, with six rule-based "agents" commenting on it. It is one of Bob's Replit apps, at `mirofish-swmm.replit.app`. Raw file: [raw/apps/mirofish-swmm-v0.0.0.md](../../raw/apps/mirofish-swmm-v0.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says Replit Agent is not named as a builder; Git has an initial commit by `agent` and later feature commits by Robert Dickinson. The copy here was read out of the editor of the Replit project named Mirofish SWMM on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Engine: EPA SWMM5 5.1.14 from Open Water Analytics, commit `7e7e6da`, run as WebAssembly through `swmm_run`. No SWMM engine license file or statement was found in the repository.
- If the engine fails, the API falls back to a simplified calculation: runoff from `C = 0.3 + 0.6 × imperviousPercent / 100` and `Q = C × rainfallIntensity × area`, and conduit flow from Manning with 1.49. The file says these formulas belong to the fallback, not the SWMM engine.
- When a parsed time series is missing, the runner makes a synthetic one: a quadratic rise, an exponential recession and random variation.
- The six agents are code-defined rules with fixed thresholds. No external language model is called.
- The USER1 sample has 58 subcatchments, 59 junctions, one outfall, 59 conduits and one raingage. Its project description says 22 subcatchments. The discrepancy was not resolved.
- An analysis run returned 60 node results, 59 link results and 58 subcatchment results, with 420 points in the first series of each group, and completed with EPA SWMM5 v5.1.14 (WASM).
- The sample `.inp` declares CMS units while the results page labels peak runoff in CFS. Units were not audited end to end.
- `pnpm run typecheck` failed, and the web package's typecheck failed with 14 TypeScript errors across eight files. No tests exist.
- MiroFish is named as the inspiration for the multi-agent idea; its license is not recorded. Project license MIT.

**Limits it states.** Import, generation, scale-up, save, auto-fix and calibration were not exercised one by one. The published pages were not checked. Engineering accuracy was not validated. The fallbacks are not equivalent to EPA SWMM output.

**Checked at ingest.** Version 0.0.0 comes from `package.json`, and the `date:` is the day of the summary (Q75). The site is mirofish-swmm and the app calls itself SWMM5 Modeler (Q77).

**Feeds:** [SWMM5 Modeler (app)](../entities/swmm5-modeler.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [EPA SWMM 5](../entities/swmm-5.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
