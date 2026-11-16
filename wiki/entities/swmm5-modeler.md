---
title: SWMM5 Modeler (app)
type: entity
updated: 2026-11-15
sources: [S123]
tags: [apps, replit, swmm5, wasm, engines, model-generation]
reviewed: 11/16/2026
---
Bob's Replit app SWMM5 Modeler: an app that generates, scales up or imports a drainage network, runs it in EPA SWMM5 compiled to WebAssembly, and reports results, errors, proposed fixes and a model grade, with six rule-based "agents" commenting on it. Version 0.0.0, at `mirofish-swmm.replit.app` [S123](../sources/S123-swmm5-modeler-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S123](../sources/S123-swmm5-modeler-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S123](../sources/S123-swmm5-modeler-replit-summary.md)
- Engine: EPA SWMM5 5.1.14 from Open Water Analytics, commit `7e7e6da`, run as WebAssembly through `swmm_run`. No SWMM engine license file or statement was found in the repository.
- If the engine fails, the API falls back to a simplified calculation: runoff from `C = 0.3 + 0.6 × imperviousPercent / 100` and `Q = C × rainfallIntensity × area`, and conduit flow from Manning with 1.49. The file says these formulas belong to the fallback, not the SWMM engine.
- When a parsed time series is missing, the runner makes a synthetic one: a quadratic rise, an exponential recession and random variation.
- The six agents are code-defined rules with fixed thresholds. No external language model is called.
- The USER1 sample has 58 subcatchments, 59 junctions, one outfall, 59 conduits and one raingage. Its project description says 22 subcatchments. The discrepancy was not resolved.
- An analysis run returned 60 node results, 59 link results and 58 subcatchment results, with 420 points in the first series of each group, and completed with EPA SWMM5 v5.1.14 (WASM).
- The sample `.inp` declares CMS units while the results page labels peak runoff in CFS. Units were not audited end to end.
- `pnpm run typecheck` failed, and the web package's typecheck failed with 14 TypeScript errors across eight files. No tests exist.
- MiroFish is named as the inspiration for the multi-agent idea; its license is not recorded. Project license MIT.

**What it does not show.** Import, generation, scale-up, save, auto-fix and calibration were not exercised one by one. The published pages were not checked. Engineering accuracy was not validated. The fallbacks are not equivalent to EPA SWMM output. [S123](../sources/S123-swmm5-modeler-replit-summary.md)

**Noted at ingest.** Version 0.0.0 comes from `package.json`, and the `date:` is the day of the summary (Q75). The site is mirofish-swmm and the app calls itself SWMM5 Modeler (Q77).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [EPA SWMM 5](swmm-5.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
