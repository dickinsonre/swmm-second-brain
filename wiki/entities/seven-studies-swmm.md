---
title: "Seven Studies for SWMM (app)"
type: entity
updated: 2026-11-18
sources: [S291]
tags: [apps, teaching, judgment, swmm5, wasm, uncertainty]
reviewed: no
---
Bob's app Seven Studies for SWMM: seven habits of thought, from metacognition to intellectual humility, each given one lab on the same four-pipe SWMM model run by EPA SWMM 5.2.2 compiled to WebAssembly in the page. Version 1.0.0, 2026-11-17 [S291](../sources/S291-seven-studies-swmm-app-md.md). Its `links:` line names no live Netlify address [S291](../sources/S291-seven-studies-swmm-app-md.md).

**Its source.** [S291](../sources/S291-seven-studies-swmm-app-md.md) is the technical summary the app ships with. Bob has not read this page.

**What the summary says** [S291](../sources/S291-seven-studies-swmm-app-md.md)
- Upsizing the pipe below a flooded manhole cut total flooding by only 2.2 percent, because the flood moved downstream.
- The model: three towns, four pipes, one 2.37 in storm that floods 0.727 million gallons.
- The wasm 5.2.2 engine matched a native EPA SWMM 5.2.4 build on 17 models, 216,840 values, largest difference 0.
- A null-effect control (pervious parameters on a 100% impervious plane) gives byte-identical .out files; a hand nonlinear reservoir matches the engine's runoff peak within 0.18% on 4 cases.
- 22 of 22 mechanical checks pass over 958 engine runs.

**What it does not show.** One synthetic network and storm; illustrative cost curve and uncertainty ranges; parity with 5.2.4 on 17 small models only; the .out reader is local; no person has reviewed the text or numbers. [S291](../sources/S291-seven-studies-swmm-app-md.md)

**Noted at ingest.** Nothing in the summary can be checked by arithmetic beyond its own tables.

See [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Calibration, validation and uncertainty](../concepts/calibration-validation-uncertainty.md), [App build contract (four working principles)](../concepts/app-build-contract.md).
