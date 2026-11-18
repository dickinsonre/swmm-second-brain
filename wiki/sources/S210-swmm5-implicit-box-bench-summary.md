---
title: "S210: SWMM5 Implicit Box Solver Test Bench, summary written from the page (v2026-10-02)"
type: source
raw: raw/apps/swmm5-implicit-box-bench-v2026-10-02.md
kind: app-md
author: Robert Dickinson
published: 2026-10-30
ingested: 2026-11-17
tags: [apps, swmm5, icm, solvers, preissmann, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM5 Implicit Box Solver Test Bench, version 2026-10-02: one .inp run twice in the browser, with stock EPA SWMM 5.2.4 dynamic wave and with an implicit Preissmann four-point box scheme (pbox.c) built into the same engine, the published method InfoWorks ICM's 1D engine is documented as using. It is not InfoWorks code. Raw file: [raw/apps/swmm5-implicit-box-bench-v2026-10-02.md](../../raw/apps/swmm5-implicit-box-bench-v2026-10-02.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793394709-117e, reading its page text in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the bench and the solver were built with Claude in a claude.ai session in October 2026 under Bob's direction: Bob asked for the solver, chose to put it in 5.2.4 and is running the ICM comparison himself; Claude wrote pbox.c and its hooks, compiled the engine, wrote the sixteen test models and found and fixed the convergence faults. The page has no About or Doc tab.

**Claims worth keeping** (all copied from the file)
- Sixteen built-in test models, from chains at 5 s and 60 s steps to a braided network, a relief loop and a storage unit, each with 3 to 8 conduits; or the user's own DYNWAVE .inp.
- The implicit run uses the ROUTING_STEP as a fixed step and halves it only when Newton fails. Theta runs from 0.5 to 1; theta below 1 failed on two of the sixteen models.
- With the extension off, the .out is byte-identical to pristine EPA SWMM 5.2.4 on all 16 models.
- The WebAssembly engine is byte-identical to a native musl build of the same source on all 16 models, extension off and on; a glibc build on four models differs by at most 7e-7 ft and 3e-8 cfs.
- Against stock on the 16 models: conduit peaks within 5.5 %, node peak depths within 9.8 %, routing continuity within 0.11 %, no step accepted unconverged.
- Cost: 16 times stock on the chain model at the same 5 s step (15.0 to 16.4 over seven interleaved pairs), 8.7 times on the pump model.
- Every conduit keeps a base depth of 5 % of its height; link flows and volumes are net of the base flow.

**Limits it states.** No comparison with InfoWorks ICM and no field data: agreement with stock says the two schemes solve the same equations, not that either is right. Flap gates, culvert inlet control, force-main equations, conduit seepage and evaporation and conduit flow limits are not modelled.

**Checked at ingest.** The repository is named only as a branch, dev-pbox-implicit-wasm, on a SWMMBob GitHub repository whose name was cut off in the text read. Bob's wish to test the ICM 1D solution inside SWMM5 is on [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md); the time-step side is on [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://swmm5-implicit-box-bench.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [SWMM5 Implicit Box Solver Test Bench (app)](../entities/swmm5-implicit-box-bench.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
