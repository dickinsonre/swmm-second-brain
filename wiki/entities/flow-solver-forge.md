---
title: "Flow Solver Forge (app)"
type: entity
updated: 2026-11-18
sources: [S313]
tags: [apps, swmm5, saint-venant, numerics, verification]
reviewed: no
---
Bob's app Flow Solver Forge: build a 1D Saint-Venant solver from parts and run it beside EPA SWMM 5.2.4. Version 1.0, 2026-10-25 [S313](../sources/S313-flow-solver-forge-summary.md). Its `links:` line names no live Netlify address [S313](../sources/S313-flow-solver-forge-summary.md).

**A caution about its source.** The page ships no technical summary. [S313](../sources/S313-flow-solver-forge-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S313](../sources/S313-flow-solver-forge-summary.md)
- A workbench for the engine inside a 1D sewer or channel model: one prismatic reach, one storm, and an unsteady flow solver you assemble from five switchable parts, compared with EPA SWMM 5.2.4 (compiled into the page) and with four problems whose answers are known exactly. The Lovable export of this name held only a blank template, so at Bob's direction the page was designed from the name.
- On a surcharging storm the native and wasm SWMM builds agree to the last printed digit (39.366 cfs); the JavaScript port gives 39.370 cfs, Nash-Sutcliffe 1.00000 against native SWMM, the same 2.07 iterations per step and the same -0.215% continuity error. Against exact answers, SWMM's link-node method fails Stoker's dam break (L1 depth error 0.942 ft, front -27.0%), and only Godunov HLL passes all four tests.
- The link-node part checked three ways against EPA SWMM 5.2.4: the EPA source built natively with gcc, the same source built to WebAssembly, and the JavaScript port, run by run (numbers above).
- Every scheme scored against the four exact answers; a grid-refinement study run. All Verify numbers come from those runs.

**How to use it, as the summary puts it.** Use it to see why schemes differ and what an exact test can show that an engine comparison cannot. One reach, no network, no structures, no wet-dry fronts, and no person has reviewed the solver code line by line. [S313](../sources/S313-flow-solver-forge-summary.md)

**What it does not show.** As the page lists it: one reach, no network; no junction losses, no manhole storage beyond SWMM's minimum surface area, no pumps, weirs or orifices, no rainfall-runoff; wet-dry fronts not handled (every run keeps a small base flow); the Preissmann box uses equal space weighting (ψ = 0.5) only. These are limits of the page, not of the methods. No person has yet reviewed the solver code line by line. [S313](../sources/S313-flow-solver-forge-summary.md)

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [St. Venant Solver Rosetta Stone (app)](st-venant-solver-rosetta-stone.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
