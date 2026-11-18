---
title: "SWMM5 / SWMM6 Mograph (film)"
type: entity
updated: 2026-11-18
sources: [S302]
tags: [films, swmm5, swmm6, wasm, mograph]
reviewed: no
---
Bob's film SWMM5 / SWMM6 Mograph: one storm, start to finish, in 60 seconds, on real engine output. Version 3.1, 2026-11-09 [S302](../sources/S302-swmm5-swmm6-mograph-summary.md). Its `links:` line names no live Netlify address [S302](../sources/S302-swmm5-swmm6-mograph-summary.md).

**A caution about its source.** The page ships no technical summary. [S302](../sources/S302-swmm5-swmm6-mograph-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S302](../sources/S302-swmm5-swmm6-mograph-summary.md)
- A 60-second motion graphic that follows one storm through the engine you pick, from the hyetograph through rain, runoff, routing and outfall to the continuity ledger. It runs on real output: EPA SWMM 5.2.4 and OpenSWMM 6 (dynamic wave and finite volume, through the swmm6-go translation) both run inside the page, so every bar, water level and curve is a number an engine wrote, and changing the model in the Model tab changes the film.
- The Compare tab runs the model through all three solvers, changing only the FLOW_ROUTING line between the two SWMM6 runs; the film picks the node with the widest gap in peak depth among the runs (J3 on the built-in model) and also counts how long each run holds it above the crown. The wasm EPA engine's results block is byte-identical to a native 5.2.4 build on the built-in model; on five pyswmm test models, three matched byte for byte and two agreed on outfall peak to 0.02% or better.
- The WebAssembly EPA engine and a native 5.2.4 build on the built-in model: results blocks byte-identical.
- The JavaScript readers compared with the Python originals on the same files; tank depths tested by mass balance against the report's final storage.
- Five public pyswmm example models against a native build: three byte for byte, two with outfall peak within 0.02%.
- Seventeen models (SI, kinematic wave, LID, pump and storage cases among them) run through every scene and the map with no drawing error; frames looked at for three. In a headless browser: three quick edits, a deliberate input error and three loaded files.

**How to use it, as the summary puts it.** Use it to show a storm moving through SWMM and to see where the SWMM6 solvers part from SWMM5. The built-in model is one synthetic storm on an invented catchment (3 subcatchments, 4 nodes, 3 links); the pipe surface is drawn straight between node and mid-pipe depths. [S302](../sources/S302-swmm5-swmm6-mograph-summary.md)

**What it does not show.** As the page lists it: a calibrated model of any real place; the real water profile inside a pipe; the separate depths inside a tank. [S302](../sources/S302-swmm5-swmm6-mograph-summary.md)

**Noted at ingest.** The page bundles swmm6-go, the Go translation of OpenSWMM 6 (Apache-2.0), without reproducing the upstream LICENSE and NOTICE, so its Netlify folder adds OPENSWMM-LICENSE and OPENSWMM-NOTICE (swmm6_rel at 2a98cbe).

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [SWMM6 language translations (swmm6-*)](swmm6-language-ports.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
