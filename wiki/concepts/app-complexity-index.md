---
title: App complexity index (HydroCouple = 100)
type: concept
updated: 2026-11-15
sources: [S01, S02, S73, S75]
tags: [apps, measurement]
reviewed: 2026-11-15
---
A number for how big and how tangled a modeling program's source is, on a scale where the HydroCouple GitHub organization is fixed at 100 [S02](../sources/S02-complexity-meter-app-md.md). Computed by the [SWMM App Complexity Meter (app)](../entities/swmm-app-complexity-meter.md).

**Formula.** Each of eight dimensions is scored on a log scale, 25 points per factor of ten:

`score = 100 * log10(1 + x/x0) / log10(1 + H/x0)`, with `x0 = H * 10^(-100/25)`

where x is the program's count and H is HydroCouple's. The index is the weighted mean of the eight scores [S02](../sources/S02-complexity-meter-app-md.md).

| Dimension | Weight | HydroCouple's count |
|---|---|---|
| Bulk (code tokens) | 0.15 | 6,607,205 |
| Decisions | 0.2 | 123,080 |
| Routines | 0.1 | 38,818 |
| Test markers | 0.1 | 27,339 |
| Stack (languages and technology signals) | 0.1 | 31.573 |
| Dependencies (outside libraries) | 0.1 | 77 |
| Formats | 0.1 | 43 |
| SWMM vocabulary (SWMM 5.2.4 terms in code) | 0.15 | 226 |

Table from [S02](../sources/S02-complexity-meter-app-md.md).

**Scores on record**

| Program | Index | Source |
|---|---|---|
| HydroCouple, all 47 repositories | 106.4 | [S02](../sources/S02-complexity-meter-app-md.md) |
| openswmm.engine | 90.1 | [S02](../sources/S02-complexity-meter-app-md.md) |
| swmm5-rust | 80.3 | [S02](../sources/S02-complexity-meter-app-md.md) |
| SWMM-Explorer | 74.6 | [S02](../sources/S02-complexity-meter-app-md.md) |
| swmm5-cplus | 74.2 | [S02](../sources/S02-complexity-meter-app-md.md) |
| EPANET | 70.2 | [S02](../sources/S02-complexity-meter-app-md.md) |
| SWMM 1 Engine app, v3.6 (155 source files) | 70.2 | [S01](../sources/S01-swmm1-engine-app-md.md) |
| EPA Stormwater-Management-Model v5.2.4 | 69.2 | [S02](../sources/S02-complexity-meter-app-md.md) |
| pyswmm | 61.5 | [S02](../sources/S02-complexity-meter-app-md.md) |

**What it does not mean.** The index is source footprint, not quality and not capability. It tracks size closely: rank correlation 0.87 with a tokens-only score across 55 repositories. No person has checked the choice of dimensions or weights [S02](../sources/S02-complexity-meter-app-md.md).

**In use.** The SWMM 1 Engine's Doc has carried the index in a complexity box since version 3.6 [S01](../sources/S01-swmm1-engine-app-md.md).

**Added 15 November 2026.** Two more scores are on record. The SWMM 1 Engine app at v3.13 scores 72.6 over 182 source files, with the shipped .html alone at 64.8 [S73](../sources/S73-swmm1-engine-app-md-v3-13.md); the 70.2 in the table above is its v3.6 figure. The [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md) page scores 51.5, with 0.0 for test markers because the page carries no tests of its own [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). Both name the baseline HC-2026-11-10-h. [S75](../sources/S75-st-venant-rosetta-stone-app-md.md) describes the anchor as "the 43 repositories of github.com/HydroCouple"; the table above has a row for all 47 repositories at 106.4 from [S02](../sources/S02-complexity-meter-app-md.md).
