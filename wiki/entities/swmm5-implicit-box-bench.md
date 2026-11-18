---
title: "SWMM5 Implicit Box Solver Test Bench (app)"
type: entity
updated: 2026-11-17
sources: [S205, S210]
tags: [apps, swmm5, icm, solvers, preissmann, wasm]
reviewed: no
---
Bob's app SWMM5 Implicit Box Solver Test Bench: one .inp run twice in the browser, with stock EPA SWMM 5.2.4 dynamic wave and with an implicit Preissmann four-point box scheme (pbox.c) built into the same engine, the published method InfoWorks ICM's 1D engine is documented as using. It is not InfoWorks code. Version 2026-10-02, 2026-10-30 [S210](../sources/S210-swmm5-implicit-box-bench-summary.md). Netlify address: https://swmm5-implicit-box-bench.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S210](../sources/S210-swmm5-implicit-box-bench-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S210](../sources/S210-swmm5-implicit-box-bench-summary.md)
- Sixteen built-in test models, from chains at 5 s and 60 s steps to a braided network, a relief loop and a storage unit, each with 3 to 8 conduits; or the user's own DYNWAVE .inp.
- The implicit run uses the ROUTING_STEP as a fixed step and halves it only when Newton fails. Theta runs from 0.5 to 1; theta below 1 failed on two of the sixteen models.
- With the extension off, the .out is byte-identical to pristine EPA SWMM 5.2.4 on all 16 models.
- The WebAssembly engine is byte-identical to a native musl build of the same source on all 16 models, extension off and on; a glibc build on four models differs by at most 7e-7 ft and 3e-8 cfs.
- Against stock on the 16 models: conduit peaks within 5.5 %, node peak depths within 9.8 %, routing continuity within 0.11 %, no step accepted unconverged.
- Cost: 16 times stock on the chain model at the same 5 s step (15.0 to 16.4 over seven interleaved pairs), 8.7 times on the pump model.
- Every conduit keeps a base depth of 5 % of its height; link flows and volumes are net of the base flow.

**What it does not show.** No comparison with InfoWorks ICM and no field data: agreement with stock says the two schemes solve the same equations, not that either is right. Flap gates, culvert inlet control, force-main equations, conduit seepage and evaporation and conduit flow limits are not modelled. [S210](../sources/S210-swmm5-implicit-box-bench-summary.md)

**Noted at ingest.** The repository is named only as a branch, dev-pbox-implicit-wasm, on a SWMMBob GitHub repository whose name was cut off in the text read. Bob's wish to test the ICM 1D solution inside SWMM5 is on [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md); the time-step side is on [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
