---
title: "OpenSWMM Gymnasium (app)"
type: entity
updated: 2026-11-18
sources: [S306]
tags: [apps, swmm6, openswmm, reinforcement-learning, control]
reviewed: no
---
Bob's app OpenSWMM Gymnasium: a reinforcement-learning framework for the SWMM engine, explained and run. Version 1.0, 2026-10-25 [S306](../sources/S306-openswmm-gymnasium-summary.md). Its `links:` line names no live Netlify address [S306](../sources/S306-openswmm-gymnasium-summary.md).

**A caution about its source.** The page ships no technical summary. [S306](../sources/S306-openswmm-gymnasium-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S306](../sources/S306-openswmm-gymnasium-summary.md)
- An explainer of HydroCouple's openswmm.gymnasium, a reinforcement-learning framework for the SWMM engine: how the loop, spaces and rewards work, what the package really ships, and its b01 TwinTank benchmark run on EPA SWMM 5.2.4 compiled to WebAssembly in the page. A single-file edition of Bob's Lovable app, which added a real learner (the cross-entropy method) on its pond model.
- The shipped TwinTank benchmark delivers 0.667 in of rain instead of 4.0: the first tank peaks at 1.99 ft of its 12, flooding is zero for every policy, and the do-nothing policy (orifice shut) scores a perfect normalized hypervolume of 1.000. The learner settles on doing nothing within six generations. The page repairs the storm and reruns. PyPI holds only a reserved 0.0.0 package with a 57-byte __init__.py.
- Pond parity: pond, storm, controllers and reward ported verbatim and compared with a separate port of the original on 24 storm and seed combinations (144 comparisons), all equal within 1e-9.
- The original's claims at a 247.2 cfs storm peak re-run, and again with the episode stretched to 120 and 240 minutes; the 60-minute horizon was not hiding a later spill.
- The learner is seeded, so the Doc's numbers reproduce with the default seed.
- The engine reports version 52004 in every run; flow routing continuity stayed within 0.2% in the reports read; the same policy run twice gives the same result.

**How to use it, as the summary puts it.** Use it to see what an RL benchmark for SWMM needs before training on it. The benchmark ran on EPA SWMM 5.2.4, not on openswmm.engine version 6, which the package targets and which the page does not claim to have run. [S306](../sources/S306-openswmm-gymnasium-summary.md)

**What it does not show.** As the page lists it: openswmm.engine version 6 was not run (version 6 descends from the same code and is expected to read a rain gage the same way, unverified); the pond is the Lovable app's model; the learner's levels and the scripted curve's are not comparable. [S306](../sources/S306-openswmm-gymnasium-summary.md)

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).
