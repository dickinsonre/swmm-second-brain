---
title: "SWMM6 in Diagrams (design)"
type: entity
updated: 2026-11-18
sources: [S281]
tags: [diagrams, swmm6, openswmm, slot, anderson, virtual-junctions, finite-volume]
reviewed: no
---
Bob's set of diagrams SWMM6 in Diagrams: ten 1,600 px boards that set SWMM5 beside OpenSWMM 6.0.0-alpha.4 (the SWMM2D street mesh, the dynamic slot, semi-implicit node continuity, Anderson acceleration, virtual junctions, finite-volume routing, the 2D surface, gridded groundwater, the engine and its API), six of them with runs on small test chains. Version and date 2026-11-14 [S281](../sources/S281-swmm6-in-diagrams-summary.md). Its `links:` line names no live Netlify address [S281](../sources/S281-swmm6-in-diagrams-summary.md).

**A caution about its source.** The page ships no technical summary. [S281](../sources/S281-swmm6-in-diagrams-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S281](../sources/S281-swmm6-in-diagrams-summary.md)
- Chain A (eight 50 ft runs of 15 in pipe, ponded): EPA 5.2.4 / SWMM6 EXTRAN / SWMM6 DYNAMIC_SLOT give continuity 0.194 / 0.091 / 0.008%, steps not converging 9.43 / 2.99 / 0.00%, average step 9.91 / 6.51 / 1.28 s.
- SEMI_IMPLICIT stopped non-convergence (2.99 to 0.00%) and made continuity worse on both ponded chains (A 0.091 to -0.389%, B -0.316 to -2.998%); on an unponded 4-pipe chain it helped (-0.092 to -0.023%).
- Anderson acceleration: 2.51 trials per step with and without it on chain A (EPA 5.2.4: 3.00); the documented 25 to 50% fewer iterations was not reproduced; with a floor of 2 trials the most any accelerator could save was 20%.
- Virtual junctions on chain D: 4 continuity nodes to 2, depths and peaks unchanged; an earlier 15-model test (alpha.3) took one model's continuity from -0.07% to -24.9% when every eligible node was converted.
- FV routing on chain C: continuity 0.000% against -0.054%, run time 2.04 s against 0.29 s; with ALLOW_PONDING YES, FV reported -158% and -133%.
- Parity is not universal in alpha.4: on ponded chain A, EPA 5.2.4 peaked at 14.45 cfs and SWMM6's SWMM5 path at 11.67 cfs; on chain D the two agree on every number shown.

**What it does not show.** One small chain per measured board, not a field calibration; board 4's bars are a two-node toy; boards 7 and 8 show the documented design with no 2D or groundwater run; the MCP server and Gymnasium environment were not run. [S281](../sources/S281-swmm6-in-diagrams-summary.md)

**Noted at ingest.** 2.04 / 0.29 = 7.0 times; (2.51 - 2) / 2.51 = 20%; slot width 32.2 x 1.227 / 82^2 = 0.0059 ft, about 0.07 in, for a 15 in pipe; 25 m/s = 82 ft/s (our arithmetic).

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [Infiltration methods](../concepts/infiltration-methods.md).
