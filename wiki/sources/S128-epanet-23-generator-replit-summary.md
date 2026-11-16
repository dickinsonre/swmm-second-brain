---
title: "S128: EPANET 2.3 Generator, summary written by Replit Agent (v4.6)"
type: source
raw: raw/apps/epanet-swmm-5-generate-v4.6.md
kind: app-md
author: Robert Dickinson
published: 2026-07-20
ingested: 2026-11-15
tags: [apps, replit, epanet, swmm5, model-generation, wasm]
reviewed: 11/16/2026
---
**What it is.** A technical summary of EPANET 2.3 Generator, version 4.6: an app that builds synthetic pressurized-water and stormwater networks from settings and a seed, runs them in EPANET and SWMM in the browser, and exports the model files. It is one of Bob's Replit apps, at `epanet-swmm-5-generate.replit.app`. Raw file: [raw/apps/epanet-swmm-5-generate-v4.6.md](../../raw/apps/epanet-swmm-5-generate-v4.6.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the inspected records do not establish a complete development-tool history; the app calls itself a "vibe coding" educational tool. The copy here was read out of the editor of the Replit project named EPANET SWMM5 Generate on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Engines: EPANET through epanet-js with `@model-create/epanet-engine`, labelled 2.3 by the app; SWMM 5.1.015 through ikegdivs/swmm-js. Neither commit was checked, and the SWMM wrapper's license was not checked.
- Generation is repeatable from a seed (`mulberry32`) together with the settings.
- Pipe sizing rejects velocity above 5 ft/s and headloss per length above 0.01 ft/ft, penalizes velocity below 2 ft/s and scores distance from 3.5 ft/s. Velocity is `(flow_gpm / 449) / area_ft2`.
- A pressure screen uses low and high thresholds of 20 psi and 100 psi. The file says the screen is not design certification.
- SWMM nodes get `invert = ground - cover - random_offset`; outfall candidates are perimeter nodes sorted by ground elevation.
- 24 starter models: 4 EPANET and 20 SWMM. The SWMM set is 10 case rows, each in US and SI, with 7 LID control types among them.
- Tests: 9 passed, 0 failed, 0 skipped. One runs 18 SWMM cases and asserts a zero return code and a report containing `5.1.015`. The typecheck passed.
- The preview console showed an HTTP 404 for one resource and EPANET Warning 5: "Valves cannot deliver enough flow."
- Running the models in native EPA SWMM 5.2.4 was not checked; the file warns that the bundled report version must not be confused with the app's export target.
- Optional explanations call Anthropic Claude, model `claude-opus-4-7`.
- Repository: https://github.com/dickinsonre/EPANET-SWMM5-Generate. The generator is MIT.

**Limits it states.** Engine commits were not checked. US and SI runoff equivalence, severe storms and drain-down were not checked. Not every starter file was rerun. Downloads, AI answers and the published client were not checked.

**Checked at ingest.** The app version is 4.6 and its name says EPANET 2.3, which is the engine label (Q77). The `date:`, 20 July 2026, is the app's build date. It is a third generator of test networks, after [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md) and [SWMM5 Topology Sandbox (app)](../entities/swmm5-topology-sandbox.md).

**Feeds:** [EPANET 2.3 Generator (app)](../entities/epanet-23-generator.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md), [SWMM5 Topology Sandbox (app)](../entities/swmm5-topology-sandbox.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
