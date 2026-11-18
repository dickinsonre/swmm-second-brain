---
title: "Finite difference vs ML for flood modeling (dashboard)"
type: entity
updated: 2026-11-18
sources: [S279]
tags: [dashboards, surrogates, machine-learning, saint-venant, extrapolation]
reviewed: no
---
Bob's dashboard Finite difference vs ML for flood modeling: a dashboard of one synthetic experiment: a 1D Saint-Venant finite difference solver on an 8-mile reach and two scikit-learn surrogates (a neural network and a random forest) trained on 200 of its runs, scored against ten reasons, each with a test. Version and date 2026-10-09 [S279](../sources/S279-finite-difference-vs-ml-summary.md). Its `links:` line names no live Netlify address [S279](../sources/S279-finite-difference-vs-ml-summary.md).

**A caution about its source.** The page ships no technical summary. [S279](../sources/S279-finite-difference-vs-ml-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S279](../sources/S279-finite-difference-vs-ml-summary.md)
- Inside the record (peaks 200 to 1,200 cfs, all in bank) the network matches the solver's peak depth at mile 4 to 0.007 ft RMSE and answers 4,200 times faster (1,700 ms against 0.40 ms per flood).
- At a 3,000 cfs design flood, ten trainings of the network give 5.90 to 9.75 ft against the solver's 8.40 ft; the forest gives 5.50 ft; the first network training loses 18% (251 ac-ft) of the 1,397 ac-ft inflow and the forest 56%.
- Solver continuity is at worst 4 x 10^-12 % over 265 runs; steady depth matches Manning normal depth within 2 x 10^-13 ft.
- A surrogate trained on a teacher solver with n off by 0.005 is 0.33 ft from the reference but 0.008 ft from its teacher.
- A grid test caught a centered convective term that ran clean on five grids and broke on the 66 ft grid (2,324 rising steps on the recession); the upwind term fixed it.

**What it does not show.** The reference is the solver itself; one synthetic reach, no rainfall, gauges or calibration; two small off-the-shelf surrogates with two inputs; rows 3, 4, 5 and 8 of the scorecard true by construction; a hydraulics test, not rainfall-runoff forecasting. [S279](../sources/S279-finite-difference-vs-ml-summary.md)

**Noted at ingest.** 3,000 / 1,200 = 2.5; 1,699.8 / 0.404 = 4,206 (given as 4,200); 251 / 1,397 = 18% (our arithmetic).

See [Apps summarized on 17 and 18 November 2026: SWMM5, EPANET and the checks on them](../concepts/apps-from-pages-swmm5-epanet-checks.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md), [Where a surrogate of SWMM breaks: hidden state and missing forcing](../concepts/surrogates-hidden-state-missing-forcing.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md).
