---
title: SWMM 3 Runoff & Transport (app)
type: entity
updated: 2026-11-17
sources: [S193, S74]
tags: [apps, swmm3, history, runoff, transport, wasm]
reviewed: no
---
Bob's app that runs the Runoff and Transport blocks of SWMM Version III, the November 1981 release, in the browser from 1981 card formats. Published 23 October 2026, with no version number of its own [S193](../sources/S193-swmm3-runoff-transport-summary.md).

**A caution about its source.** The page ships no technical summary. [S193](../sources/S193-swmm3-runoff-transport-summary.md) was written by Claude on 16 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q99).

**A derivation, not a transcription.** The page says Version III went out on magnetic tape, about 25,000 Fortran statements, and no listing is known to survive; the listing of EXTRAN III, one block of Version III, does survive [S74](../sources/S74-extran3-workbench-app-md.md), so the page may mean the other blocks (Q102). So the engine was made by subtraction: the Version 4 additions were found from the 1988 manual's list of changes and dated comments and taken out of the SWMM 4.4 Fortran, and the 1981 input, output and limits restored from the 1981 manual. Where the sources disagree, the 1981 manual wins; the Runoff Newton-Raphson step is a single step, as in 1981, not wrapped in Version 4's Richardson extrapolation [S193](../sources/S193-swmm3-runoff-transport-summary.md).

**What runs** [S193](../sources/S193-swmm3-runoff-transport-summary.md)
- Runoff: Horton and Green-Ampt, the three-subarea nonlinear reservoir, snowmelt, buildup and washoff, continuous simulation.
- Transport: the kinematic-wave finite difference with Newton iteration, thirteen cross-sections, lift stations, dividers, storage, backwater elements, pollutant routing.
- The 1981 interface file between them. Converters punch SWMM 5 .inp files and SWMM 4 decks as 1981 cards.

**Three defects kept as shipped** [S193](../sources/S193-swmm3-runoff-transport-summary.md)

| ID | Effect |
|---|---|
| SNOW-1 | With partial snow cover (1 - ASC) of the melt is lost: 16 % of the initial pack on the snow1 deck |
| TRANS-1 | Continuity omits a lift station's initial wet-well volume: 2.9 % on the lift null test |
| TRANS-2 | Flow sent to an element that does not exist is dropped uncounted: -92 % on TRANS23 |

**Checks.** Native and WebAssembly builds give byte-identical printouts on eleven cases, after both were made to compile the same musl 1.2.6 math routines. All 47 Transport example decks of the January 2003 SWMM 4 set convert and run to the end [S193](../sources/S193-swmm3-runoff-transport-summary.md).

**What it does not show.** No 1981 output survives to score against. No person other than Claude has reviewed the subtraction decisions [S193](../sources/S193-swmm3-runoff-transport-summary.md).

**Related.** [SWMM version history](../concepts/swmm-version-history.md), [Block architecture and interface files](../concepts/block-architecture.md), [SWMM 1 (1971)](swmm-1.md), [SWMM 4 Twin Engines (app)](swmm4-twin-engines.md), [Wayne C. Huber](wayne-huber.md).
