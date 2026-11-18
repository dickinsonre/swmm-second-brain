---
title: Seven SWMM Engines (app)
type: entity
updated: 2026-11-17
sources: [S199, S200, S81, S22, S225, S234, S240]
tags: [apps, swmm5, swmm6, swmm4, extran, wasm, comparison]
reviewed: no
---
Bob's app that runs one SWMM 5 input file through seven engines compiled to WebAssembly and compares what they report. Version 1.2, built 28 October 2026 [S199](../sources/S199-seven-swmm-engines-summary.md). Its engines are the ones the [Bellinge (app)](bellinge-app.md) runs [S81](../sources/S81-bellinge-summary.md), and [One SWMM (app)](one-swmm.md) is built on it [S200](../sources/S200-one-swmm-summary.md).

**A caution about its source.** The page ships no technical summary. [S199](../sources/S199-seven-swmm-engines-summary.md) was written by Claude on 16 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q99).

**The seven** [S199](../sources/S199-seven-swmm-engines-summary.md)

| Engine | Source | Size |
|---|---|---|
| [EPA SWMM 5](swmm-5.md) 5.2.4 | tag v5.2.4, 7952ca8379 | 0.65 MB |
| [OpenSWMM 6](openswmm-6-and-hydrocouple.md) alpha.1 | 74ef6e27aa, 2026-05-26 | 1.45 MB |
| OpenSWMM 6 alpha.2 | 0df29948a4, 2026-07-07 | 1.74 MB |
| OpenSWMM 6 alpha.3 (finite volume arrives) | 86c28a886e, 2026-08-11 | 1.97 MB |
| OpenSWMM 6 swmm6_rel, reports alpha.4 | 3c30f1e6c2, 2026-10-17 | 5.00 MB |
| SWMM 4.4H, Runoff into Extran | the 2004 Fortran, a converted deck | 1.99 MB |
| [EXTRAN](extran.md) III, April 1981 | as printed, or with ten fixes | 0.54 MB |

The OpenSWMM builds also run with their own solver options (SWMM6 DW) and, from alpha.3 on, finite volume (FV).

**On EPA's Example 1** [S199](../sources/S199-seven-swmm-engines-summary.md)
- Outfall peak from 71.69 to 75.94 cfs across the runs; EPA 5.2.4 reports 73.9 cfs. Flow routing continuity within 0.03 percent in every run.
- TSS continuity error is where they part: -1.96 % in EPA 5.2.4, -58.54 %, -53.43 % and -53.20 % in the SWMM6 DW runs of alpha.1 to alpha.3, -1.65 % in alpha.4; -85.40 % in alpha.3 FV and -3.70 % in alpha.4 FV.

The 73.9 cfs is also conduit C11's peak in EPA 5.2.4's Link Flow Summary, where the .out at 5-minute reporting gives 71.18 cfs [S22](../sources/S22-li-ten-problems.md); the Bellinge app gives the outfall peak as 71.18 cfs [S81](../sources/S81-bellinge-summary.md). Which measure each engine's figure is, the summaries do not say (Q100).

**What 1.2 changed.** Every .rpt and .out is now read by the [SWMM Results Kit](swmm-results-kit.md). On Bellinge, the old reader read 1,037 of 1,044 links; the kit reads all 1,044 [S199](../sources/S199-seven-swmm-engines-summary.md).

**What it does not show.** "Agreement between engines is not correctness." No field data, and seven engines that share most of their ancestry can agree while all wrong. The Fortran engines run a converted deck and report from printed tables [S199](../sources/S199-seven-swmm-engines-summary.md).

**Added 17 November 2026, second batch.** Its EPA 5.2.4 WebAssembly build is reused unchanged by three later apps: [Four Ways to K (app)](four-ways-to-k.md) [S225](../sources/S225-four-ways-to-k-summary.md), [SWMM Inlet Library (app)](swmm-inlet-library.md), which also carries its OpenSWMM 6.0.0-alpha.4 build [S234](../sources/S234-swmm-inlet-library-summary.md), and [Non-Prismatic Channel Lab (app)](non-prismatic-channel-lab.md) [S240](../sources/S240-non-prismatic-channel-lab-summary.md).

**Related.** [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [EXTRAN III Workbench (app)](extran-iii-workbench.md).
