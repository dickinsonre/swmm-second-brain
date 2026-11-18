---
title: "S291: Seven Studies for SWMM, app .md (v1.0.0)"
type: source
raw: raw/apps/seven-studies-swmm-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-17
ingested: 2026-11-18
tags: [apps, teaching, judgment, swmm5, wasm, uncertainty]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app Seven Studies for SWMM, version 1.0.0: seven habits of thought, from metacognition to intellectual humility, each given one lab on the same four-pipe SWMM model run by EPA SWMM 5.2.2 compiled to WebAssembly in the page. Raw file: [raw/apps/seven-studies-swmm-v1.0.0.md](../../raw/apps/seven-studies-swmm-v1.0.0.md).

**How it was written.** The app ships this file. The file says it was built with Claude (Anthropic) at Bob's request; the engine is the prebuilt 5.2.2 because the Emscripten toolchain could not be downloaded in the build session.

**Claims worth keeping** (all copied from the file)
- Upsizing the pipe below a flooded manhole cut total flooding by only 2.2 percent, because the flood moved downstream.
- The model: three towns, four pipes, one 2.37 in storm that floods 0.727 million gallons.
- The wasm 5.2.2 engine matched a native EPA SWMM 5.2.4 build on 17 models, 216,840 values, largest difference 0.
- A null-effect control (pervious parameters on a 100% impervious plane) gives byte-identical .out files; a hand nonlinear reservoir matches the engine's runoff peak within 0.18% on 4 cases.
- 22 of 22 mechanical checks pass over 958 engine runs.

**Limits it states.** One synthetic network and storm; illustrative cost curve and uncertainty ranges; parity with 5.2.4 on 17 small models only; the .out reader is local; no person has reviewed the text or numbers.

**Checked at ingest.** Nothing in the summary can be checked by arithmetic beyond its own tables. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Seven Studies for SWMM (app)](../entities/seven-studies-swmm.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [App build contract (four working principles)](../concepts/app-build-contract.md).
