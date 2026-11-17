---
name: SWMM5 RASPIPE
file: swmm5-raspipe.html
version: "1.3"
date: 2026-11-05
written: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/3zBb9jAAvucjovoDtCFcCo", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model, v5.2.4", license: public domain}
  - {name: SWMM5 RASPIPE, version: "1.3", source: "EPA SWMM 5.2.4 plus raspipe.c (about 2,500 lines) and small patches to EPA's files", license: not stated in the page}
  - {name: OpenSWMM 6, version: 6.0.0-alpha.4, source: "HydroCouple/openswmm.engine swmm6_rel at 3c30f1e (2026-10-17), the same build as Seven SWMM Engines", license: Apache-2.0}
units: "model units; RASPIPE_CELL_LENGTH in ft or m; results in the page in US customary (cfs, ft, ft3, ac-ft)"
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page's own AI-use note says SWMM5 RASPIPE was built with Claude at Robert Dickinson's request and that he has not yet reviewed this build. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/3zBb9jAAvucjovoDtCFcCo, version 1793916058-2c2b (index.html, 8,106,825 bytes, SHA-256 325ae3bd5bd2289c70b2809d49b572773530f288dbcbf9dcd7dc8ce4bfdd0eec), its About and Doc tabs read in headless Chromium on 2026-11-16. No model was run to write this file."
---

# SWMM5 RASPIPE: EPA SWMM 5.2.4 with a semi-implicit finite-volume pipe solver after HEC-RAS

## In three points
- **What:** EPA SWMM 5.2.4 with a semi-implicit finite-volume pipe solver written from HEC's public manuals, switched on by FLOW_ROUTING RASPIPE; without that line the engine is EPA 5.2.4 byte for byte.
- **So what:** On the 1,163 corpus models that finished in both engines, the median routing continuity error fell from 0.795% on EPA 5.2.4 to 0.005%, and models past 1% fell from 552 to 2.
- **Now what:** Treat it as a test bed, not a replacement: it has not been run against HEC-RAS, no field data backs it, and its median run time is 2.6 times stock.

This summary was written after the fact. The page ships no technical summary of its own. Its version, 1.3, comes from the page's code (VERSION='1.3') and its About tab. Every number below is copied from the page's About tab or its Doc essay. No engine was run to write this file.

## What it does

RASPIPE is a fork of EPA SWMM 5.2.4 with one new source file, raspipe.c, about 2,500 lines. It replaces the explicit link and node update of dynamic wave routing with a semi-implicit finite-volume solve over a mesh of pipe cells. Hydrology, controls, statistics and the .out format are EPA's. Quality routing is EPA's with one change: it is told the flow at each end of a conduit. Version 1.3 adds SWMM6 modified DW and SWMM6 FV as their own lines on the Run and Profile tabs and a shared table on Verify.

The page states: "Not HEC-RAS. This is an independent implementation written from HEC's public manuals and the journal papers they cite. It contains no HEC-RAS code, and it has not been compared with a run of HEC-RAS."

## How it computes

Turned on with one word in [OPTIONS]; without it the engine is EPA 5.2.4, byte for byte.

```
FLOW_ROUTING          RASPIPE
RASPIPE_EQUATIONS     DW      ; DW or SWE
RASPIPE_CELL_LENGTH   100     ; ft or m
RASPIPE_MAX_CELLS     20
RASPIPE_THETA         1.0     ; 0.5 to 1.0
RASPIPE_COURANT       0.9     ; 0 = off
RASPIPE_INITIAL_STAGE YES
RASPIPE_WARMUP        0       ; steps, 30 or more
RASPIPE_NESTED_ONLY   NO      ; for testing
```

- RASPIPE_EQUATIONS: DW is diffusion wave; SWE is the full shallow-water equations with HEC's Eulerian-Lagrangian advection.
- RASPIPE_COURANT 0.9: target residence-time Courant number for the pipe steps, HEC's default. For each cell, C = dt x outflow / volume; the largest C in the network is held at the target, and a SWMM routing step runs as many pipe steps inside it as the target needs. Mean flows go back to SWMM at the end of the step.
- RASPIPE_THETA: implicit weighting, 0.5 to 1. The page says 0.6 keeps sharp fronts better; 1.0 is what the corpus ran.
- RASPIPE_INITIAL_STAGE: projects FIXED, TIDAL and TIMESERIES outfall stages up the conduits at the start. RASPIPE_WARMUP: warm-up steps, inflows ramped over the first 2/3; HEC asks for 30 or more.
- Plain Newton with a nested-Newton fallback (the fallback always uses theta = 1). A manhole is a real tank up to its MaxDepth.

## Results the page reports

- Bore benchmark: version 1.1 ran the bore 13.2% slow. HEC's formula with the face area taken from upstream gave -5.6%; the mean of the two sides gave -3.3% at theta = 1 and +0.2% at theta = 0.6; the lag closes to -1.0% at a 0.02 s step.
- Corpus sweep (version 1.1 build, diffusion wave): 1,600 models drawn at random from the 1729 corpus, stratified by file size, 60 s limit per run. 134 had no conduits; 1,466 went through both engines; 1,163 finished in both with a continuity figure. Median routing continuity error 0.795% on EPA 5.2.4 and 0.005% on RASPIPE. 552 models past 1% on stock, 2 on RASPIPE. The worst RASPIPE entry, NUM-19_outfall-inflow.inp at 1,341%, is called a stock bookkeeping gap (a fixed outfall that feeds the network is never booked as inflow).
- The solver's own volume ledger closes to 3.8e-06 ft3 on 304,200 ft3 of inflow on the mixed test model. 14 models finished with any step left unsolved.
- Run time: median 2.6 times stock, 12 times at the 90th percentile; 124 models hit the 60 s limit on RASPIPE (76 in version 1.0) against 26 on stock. Three models timed in five interleaved pairs: 2.5 times stock, 0.86 times, and 33 times.
- Quality: across 46 sample models with pollutants, median quality continuity error 1.73% on stock and 0.07% on RASPIPE; worst cases 99.5% and 950.0%.
- SWMM6 (version 1.3): on the 87 corpus models every engine finished, SWMM6 modified DW had a median continuity error of 0.701% against EPA's 0.941%; models past 10% were 22 against 22; it beat EPA by at least five points on 8 models and lost by at least five on 9. On the deck "Peter", EPA and SWMM6's EXTRAN each send 0.24 of the 0.26 ac-ft out the outfall; with the modified DW the outflow is 0.000.
- SWMM6 options one at a time over the sample (median continuity error): EXTRAN with nothing added 0.763%; DYNAMIC_SLOT alone 0.734%; ANDERSON_ACCEL alone 0.696%; both 0.619%; SEMI_IMPLICIT alone 0.909%; all three (the modified DW) 0.516%.

## Checks (as stated on the page)

- Closed-form answers: Manning, normal depth, a pump curve, Stoker's dam break, the U-tube period.
- Byte comparison of the .out with the feature off, and of diffusion wave against version 1.1: identical on 23 of 23 test decks and 60 of 60 corpus models (16 more skipped for time or error).
- A separately written Saint-Venant reference solver, the solver's own volume ledger, the 1,600-model corpus sweep, and a Playwright run of the page.
- The WebAssembly build matched the native .out byte for byte on 15 of 16 test decks; on the other the largest difference was 0.01 cfs on an 8 cfs link.
- The page calls these checks mechanical, not the AI's judgment.

## What this does not show

- No field data. Agreement with Manning, a pump curve and another solver shows the arithmetic, not whether a model predicts a real sewer.
- It has not been run against HEC-RAS and may differ from HEC's code in any detail the manuals leave out.
- Where the two engines disagree in the corpus, nobody has yet sorted out which is right, model by model.
- A manhole is a real tank up to its MaxDepth; EXTRAN stores nothing above the crown.
- A conduit holds one concentration while its flow varies along the cells; nothing tests concentrations against a reference.
- Hot-start files carry node and link states, not cell states. Water hammer is not modeled.
- Timing is from one machine.
- No person has reviewed the code, the figures or the text. Casulli and Stelling (2013) and Stelling and Duinmeijer (2003) were not read directly.

## How to reproduce

Add FLOW_ROUTING RASPIPE to a SWMM 5.2.4 .inp and run it on the Run tab. The page names its test decks (long_pipe_wave.inp, u_tube.inp, pump_full_pipe.inp, startup_spike.inp, stage_on_dry_network.inp); the corpus sweep needs the 1729 corpus and is not in the page.

## Credits and licenses

EPA SWMM 5.2.4: USEPA, public domain. OpenSWMM Engine, Copyright 2026 HydroCouple Developers, Apache License 2.0, with public domain EPA SWMM material; the page states the USEPA does not endorse the product. Methods from the HEC-RAS 1D Technical Reference Manual 7.0 and the HEC-RAS User's Manual 6.6 and 7.0; the Hydrologic Engineering Center and the U.S. Army Corps of Engineers did not make, review or endorse it. Other sources named: CivilGEO (Advanced Time Step Control), Stoker (1957), EPA SWMM issue 231, Brutto et al. (2023), Fuamba (2002), the 1729 SWMM5 Models corpus.

## AI use

The page says SWMM5 RASPIPE was built with Claude, Anthropic's AI model, in a Claude session in November 2026, at the request of Robert (Bob) Dickinson, who pointed it to the HEC-RAS time step and start-up options used in version 1.1, supplied the outside review that drove version 1.2, asked for SWMM6 FV and the SWMM6 modified dynamic wave to be compared in version 1.3, and set the standing requirements for testing, documentation and units. Claude designed the solver, wrote raspipe.c, the reference solver, every test and the app, and ran the corpus sweeps. The page says Bob has not yet reviewed this build. This summary was written by Claude on 16 November 2026 from the published page.

## Changes

- 1.3: SWMM6 modified DW and SWMM6 FV (OpenSWMM 6.0.0-alpha.4) added to the Run, Profile and Verify tabs.
- 1.2: HEC's Eulerian-Lagrangian advection for the full equations; momentum across a junction of two conduits; Stoker's dam break, a U-tube and a one-cause-at-a-time wave benchmark; a run record; a Profile tab; evidence labels. Diffusion wave unchanged byte for byte.
- 1.1: HEC-RAS adaptive pipe time step (residence-time Courant) and start-up options.
- 1.0: first version.
