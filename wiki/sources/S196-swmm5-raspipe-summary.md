---
title: "S196: SWMM5 RASPIPE, summary written from the page (v1.3)"
type: source
raw: raw/apps/swmm5-raspipe-v1.3.md
kind: app-md
author: Robert Dickinson
published: 2026-11-05
ingested: 2026-11-17
tags: [apps, swmm5, swmm6, engine, dynamic-wave, finite-volume, hec-ras, continuity, corpus]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of SWMM5 RASPIPE version 1.3: EPA SWMM 5.2.4 with a semi-implicit finite-volume pipe solver written from HEC's public manuals, switched on by `FLOW_ROUTING RASPIPE`. Version 1.3 adds OpenSWMM 6.0.0-alpha.4's modified dynamic wave and finite volume as comparison lines. Raw file: [raw/apps/swmm5-raspipe-v1.3.md](../../raw/apps/swmm5-raspipe-v1.3.md).

**How it was written. A summary written from the page.** The page ships no technical summary of its own. Claude (Anthropic) wrote this file on 16 November 2026, at Bob's request, from the published artifact (version 1793916058-2c2b) and its About and Doc tabs. No model was run. Bob has not read it (Q99). The page says Claude designed the solver, wrote `raspipe.c`, the reference solver and every test, and ran the corpus sweeps; Bob pointed it to the HEC-RAS time step and start-up options, supplied the outside review behind 1.2, and asked for the SWMM6 lines in 1.3. The page says Bob has not yet reviewed this build.

**Claims worth keeping** (all copied from the page)
- "Not HEC-RAS. This is an independent implementation written from HEC's public manuals and the journal papers they cite. It contains no HEC-RAS code, and it has not been compared with a run of HEC-RAS."
- One new file, `raspipe.c`, about 2,500 lines. It replaces the explicit link and node update of dynamic wave with a semi-implicit finite-volume solve over a mesh of pipe cells. Hydrology, controls, statistics and the .out format are EPA's. Without the option line the engine is EPA 5.2.4 byte for byte.
- Options: `RASPIPE_EQUATIONS DW` (diffusion wave) or `SWE` (full shallow-water equations with HEC's Eulerian-Lagrangian advection); `RASPIPE_CELL_LENGTH 100`; `RASPIPE_MAX_CELLS 20`; `RASPIPE_THETA 1.0` (0.5 to 1.0; 0.6 keeps sharp fronts better, 1.0 is what the corpus ran); `RASPIPE_COURANT 0.9`, the residence-time Courant target C = dt x outflow / volume, HEC's default; `RASPIPE_INITIAL_STAGE`; `RASPIPE_WARMUP` (HEC asks for 30 or more steps). Plain Newton with a nested-Newton fallback at theta = 1. A manhole is a real tank up to its MaxDepth.
- Bore benchmark: version 1.1 ran the bore 13.2 % slow; with the face area from upstream -5.6 %; the mean of the two sides -3.3 % at theta = 1 and +0.2 % at theta = 0.6; -1.0 % at a 0.02 s step.
- Corpus sweep (version 1.1 build, diffusion wave): 1,600 models drawn at random from the 1729 corpus, stratified by file size, 60 s limit; 134 had no conduits; 1,466 through both engines; 1,163 finished in both. Median routing continuity error 0.795 % on EPA 5.2.4 and 0.005 % on RASPIPE; 552 models past 1 % on stock, 2 on RASPIPE. The worst RASPIPE entry, NUM-19_outfall-inflow.inp at 1,341 %, is called a stock bookkeeping gap (a fixed outfall that feeds the network is never booked as inflow).
- The solver's own volume ledger closes to 3.8e-06 ft3 on 304,200 ft3 of inflow on the mixed test model. 14 models finished with a step left unsolved.
- Run time: median 2.6 times stock, 12 times at the 90th percentile; 124 models hit the 60 s limit on RASPIPE (76 in version 1.0) against 26 on stock. Three models in five interleaved pairs: 2.5, 0.86 and 33 times stock.
- Quality, 46 sample models with pollutants: median quality continuity error 1.73 % on stock and 0.07 % on RASPIPE; worst cases 99.5 % and 950.0 %.
- SWMM6 on the 87 corpus models every engine finished: modified DW median continuity error 0.701 % against EPA's 0.941 %; past 10 %: 22 against 22; better than EPA by at least five points on 8 models, worse on 9. On the deck "Peter", EPA and SWMM6's EXTRAN each send 0.24 of the 0.26 ac-ft out the outfall; the modified DW sends 0.000.
- SWMM6 options one at a time (median continuity error over the sample): EXTRAN alone 0.763 %; DYNAMIC_SLOT 0.734 %; ANDERSON_ACCEL 0.696 %; both 0.619 %; SEMI_IMPLICIT 0.909 %; all three (the modified DW) 0.516 %.
- Checks: closed forms (Manning, normal depth, a pump curve, Stoker's dam break, the U-tube period); .out byte comparison with the feature off and of diffusion wave against 1.1, identical on 23 of 23 test decks and 60 of 60 corpus models; a separately written Saint-Venant reference solver; WebAssembly against native, byte for byte on 15 of 16 test decks, the other off by at most 0.01 cfs on an 8 cfs link.

**Limits it states.** No field data. Not run against HEC-RAS. Where the engines disagree in the corpus, nobody has sorted out which is right. A conduit holds one concentration while its flow varies along the cells. Hot-start files carry node and link states, not cell states. No water hammer. Timing from one machine. No person has reviewed the code, figures or text; two cited papers were not read directly.

**Checked at ingest.** 1,600 - 134 = 1,466. The SWMM6 figures come from two samples: 0.701 % and 0.941 % on 87 models, and 0.516 % for the same modified DW "over the sample" in the one-at-a-time list; the page does not say whether the sample is the same 87. 0.24 / 0.26 = 0.92.

**Feeds:** [SWMM5 RASPIPE](../entities/swmm5-raspipe.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Engine speed, 1988 to 2024](../concepts/engine-speed-1988-2024.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Hot start: what a restart loses](../concepts/hot-start-restart-state.md), [Open questions](../open-questions.md).
