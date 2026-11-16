---
title: InfoWorks ICM
type: entity
updated: 2026-11-15
sources: [S03, S13, S14, S17, S20, S65, S125, S127]
tags: [icm, engine, comparison]
reviewed: 11/16/2026
---
The commercial integrated catchment model developed by Wallingford Software in England and now maintained by Autodesk [S20](../sources/S20-li-edition-54-two-solvers.md).

- **Two network types.** An InfoWorks network, solved by ICM's implicit St. Venant scheme, and a SWMM network ("ICM SWMM"), which runs the SWMM5 dynamic wave [S17](../sources/S17-li-routing-options.md).
- **Solver.** Preissmann four-point implicit finite differences, Newton-Raphson iterations, adaptive time stepping, with each conduit divided into segments [S20](../sources/S20-li-edition-54-two-solvers.md).
- **Surcharge.** Preissmann slot from the beginning [S20](../sources/S20-li-edition-54-two-solvers.md).
- **No steady-state or kinematic wave solver.** A quasi-steady state is made from a saved state [S17](../sources/S17-li-routing-options.md).
- **2D.** Mesh-based overland flow coupled to the 1D network [S20](../sources/S20-li-edition-54-two-solvers.md).
- **Hydrology carried over from SWMM.** Three runoff surfaces per SWMM subcatchment, tied by Land Use ID [S13](../sources/S13-li-three-runoff-surfaces.md); subarea routing as Direct, To pervious, To impervious since version 6.5, November 2015 [S14](../sources/S14-li-subarea-routing.md).
- **A recorded correction.** `hw_storage` and `hw_outfall` are "phantom tables" in the ICM results file: a register candidate, status corrected, no detail given [S03](../sources/S03-findings-register-format.md).
- **Rainfall in.** The [World Rainfall Pattern Painter (app)](world-rainfall-pattern-painter.md) writes ICM rainfall event files (CSV, type=RED) after Autodesk's "Events - CSV File Formats". Its tests check the exact text of the file; import into ICM itself has not been checked [S65](../sources/S65-world-rainfall-pattern-painter-app-md.md).

Full comparison: [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md).

**Not in the sources yet.** Ruby and SQL scripting, the results file, RDII and ground infiltration, sediment, the 12 runoff surfaces. Of the 213 queued LinkedIn articles, 139 name ICM or InfoWorks in the title and 70 name Ruby.

**Added 15 November 2026: two apps.** [ICM InfoWorks release history (app)](icm-release-history-app.md) holds 50 ICM release records and 822 feature records, from release 1.5 to 2027.2, in a file inside the project and not a live feed; none of it was checked against Autodesk's own sources [S127](../sources/S127-icm-infoworks-release-history-replit-summary.md). [Kinematic Wave Router (app)](kinematic-wave-router.md) has a module that imports from and exports to ICM through its Ruby API, which was not run [S125](../sources/S125-kinematic-wave-router-replit-summary.md). Replit Agent wrote both summaries and Bob has read neither (Q74).
