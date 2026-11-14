---
title: InfoWorks ICM
type: entity
updated: 2026-11-14
sources: [S03, S13, S14, S17, S20]
tags: [icm, engine, comparison]
reviewed: no
---
The commercial integrated catchment model developed by Wallingford Software in England and now maintained by Autodesk [S20](../sources/S20-li-edition-54-two-solvers.md).

- **Two network types.** An InfoWorks network, solved by ICM's implicit St. Venant scheme, and a SWMM network ("ICM SWMM"), which runs the SWMM5 dynamic wave [S17](../sources/S17-li-routing-options.md).
- **Solver.** Preissmann four-point implicit finite differences, Newton-Raphson iterations, adaptive time stepping, with each conduit divided into segments [S20](../sources/S20-li-edition-54-two-solvers.md).
- **Surcharge.** Preissmann slot from the beginning [S20](../sources/S20-li-edition-54-two-solvers.md).
- **No steady-state or kinematic wave solver.** A quasi-steady state is made from a saved state [S17](../sources/S17-li-routing-options.md).
- **2D.** Mesh-based overland flow coupled to the 1D network [S20](../sources/S20-li-edition-54-two-solvers.md).
- **Hydrology carried over from SWMM.** Three runoff surfaces per SWMM subcatchment, tied by Land Use ID [S13](../sources/S13-li-three-runoff-surfaces.md); subarea routing as Direct, To pervious, To impervious since version 6.5, November 2015 [S14](../sources/S14-li-subarea-routing.md).
- **A recorded correction.** `hw_storage` and `hw_outfall` are "phantom tables" in the ICM results file: a register candidate, status corrected, no detail given [S03](../sources/S03-findings-register-format.md).

Full comparison: [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).

**Not in the sources yet.** Ruby and SQL scripting, the results file, RDII and ground infiltration, sediment, the 12 runoff surfaces. Of the 216 queued LinkedIn articles, 139 name ICM or InfoWorks in the title and 70 name Ruby.
