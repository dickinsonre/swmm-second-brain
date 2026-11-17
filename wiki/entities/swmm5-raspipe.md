---
title: SWMM5 RASPIPE
type: entity
updated: 2026-11-17
sources: [S196]
tags: [swmm5, swmm6, engine, dynamic-wave, finite-volume, hec-ras]
reviewed: no
---
One of Bob's variants of [EPA SWMM 5](swmm-5.md): 5.2.4 with a semi-implicit finite-volume pipe solver written from HEC's public manuals, switched on by `FLOW_ROUTING RASPIPE`. Version 1.3; a page runs it beside EPA 5.2.4 and OpenSWMM 6.0.0-alpha.4 [S196](../sources/S196-swmm5-raspipe-summary.md).

**A caution about its source.** [S196](../sources/S196-swmm5-raspipe-summary.md) was written by Claude on 16 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q99). The page itself says Bob has not reviewed this build.

**What it is and is not.** One new file, `raspipe.c`, about 2,500 lines, that replaces dynamic wave's explicit link and node update with a semi-implicit solve over a mesh of pipe cells. Hydrology, controls, statistics and the .out format are EPA's. Without the option line it is EPA 5.2.4 byte for byte. The page states: "Not HEC-RAS. ... It contains no HEC-RAS code, and it has not been compared with a run of HEC-RAS." [S196](../sources/S196-swmm5-raspipe-summary.md)

**The options** [S196](../sources/S196-swmm5-raspipe-summary.md): diffusion wave or full shallow-water equations; cell length (100 by default) and at most 20 cells per conduit; implicit weighting theta from 0.5 to 1.0; a residence-time Courant target of 0.9, HEC's default; start-up stages and warm-up steps. A manhole is a real tank up to its MaxDepth.

**What the corpus sweep showed** (1,163 models that finished in both engines) [S196](../sources/S196-swmm5-raspipe-summary.md)

| | EPA 5.2.4 | RASPIPE |
|---|---|---|
| Median routing continuity error | 0.795 % | 0.005 % |
| Models past 1 % | 552 | 2 |
| Median run time, against EPA | (the reference) | 2.6 times |
| Models at the 60 s limit | 26 | 124 |

A smaller continuity error is not a better answer; see [Continuity is not validation](../concepts/continuity-is-not-validation.md).

**Beside SWMM6.** On 87 corpus models, SWMM6's modified dynamic wave had a median continuity error of 0.701 % against EPA's 0.941 %. On one deck it sent none of the 0.26 ac-ft out the outfall where EPA sent 0.24 [S196](../sources/S196-swmm5-raspipe-summary.md). See [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).

**What it does not show.** No field data. Not run against HEC-RAS. Where the engines disagree in the corpus, nobody has sorted out which is right. Hot-start files carry no cell states. No person has reviewed the code [S196](../sources/S196-swmm5-raspipe-summary.md).

**Related.** [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Wrap, translate or extend](../concepts/wrap-translate-or-extend.md).
