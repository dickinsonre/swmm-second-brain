---
title: "ICM 2D: timestep, volume balance and results"
type: concept
updated: 2026-11-16
sources: [S166, S173, S174, S175]
tags: [icm, 2d, timestep, continuity, results, hazard]
reviewed: no
---
How to check an InfoWorks ICM 2D run once it is built: its time stepping, its volumes and the results taken from it. These pages rest on notes written by the GPT plugin for Autodesk [S166](../sources/S166-note-icm-notes-from-gpt-plugin.md): AI-written text whose facts about ICM are reported from Autodesk's 2027 help and were not checked against ICM, and whose tests have not been run (Q90).

**Time steps** [S173](../sources/S173-note-icm-2d-timestep-and-stability.md). Keep four settings apart in the run record: the run timestep, the 1D-2D coupling options, the 2D stability control and the reporting interval. In the 2D Parameters dialog, Timestep Stability Control sets the CFL bound the 2D engine uses for its internal steps; the same dialog can link 1D and 2D calculations at minor timesteps, and holds depth and momentum thresholds. To test, change one thing at a time with the mesh and event fixed: a smaller run timestep at the same reporting interval; then minor-timestep coupling; then, separately, the mesh. Record whether the result and the warning changed together.

**Volume balance** [S174](../sources/S174-note-icm-2d-volume-balance.md). For each control volume over the same interval, residual = starting storage + inputs - outputs - ending storage.
- The 2D mesh alone: direct rain, boundary flows, the signed transfer with 1D, losses, change in surface volume.
- 1D and 2D together: the transfer between them is internal and cancels; count external inflows, delivered runoff, direct mesh rain, external discharges and losses, and the change in combined storage.
- Infiltration routed into 1D through a permeable zone is a transfer in the combined balance.

Use the PRN volume summary with local checks near the important exchanges; if reported and independent volumes disagree, compare time window, units, boundary sign and the results used before touching solver controls [S174](../sources/S174-note-icm-2d-volume-balance.md). The same point for SWMM is on [Continuity is not validation](continuity-is-not-validation.md).

**Results** [S175](../sources/S175-note-icm-2d-results-and-hazard.md). Depth, level, speed, time to first inundation and hazard answer different questions, so record the quantity and its time basis with every export: units and datum, timestep or maximum, the wet/dry threshold, the first-inundation depth threshold, and for a transect its line and sign. InfoWorks reports `Depth at first max hazard` and `Speed at first max hazard`, a matched pair that explains a hazard map at a point. Network Results objects at fixed points and a transect, kept through a remesh, let map and hydrograph be checked together.

**Related.** [ICM 2D: three benchmark cases](icm-2d-benchmark-cases.md), [ICM 2D: boundaries and 1D-2D exchange](icm-2d-boundaries-and-exchange.md), [ICM network tables and result fields](icm-tables-and-result-fields.md).
