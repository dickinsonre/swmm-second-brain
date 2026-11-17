---
title: InfoWorks ICM
type: entity
updated: 2026-11-16
sources: [S03, S13, S14, S17, S20, S65, S125, S127, S159, S160, S162, S163, S164, S166, S170, S172, S178, S179, S184, S188]
tags: [icm, engine, comparison]
reviewed: 11/16/2026
changed_after_review: "2026-11-16 (S159 to S165 ingest): one paragraph added at the end, headed Added 16 November 2026, on scripting, tables, result fields and conversion (S159, S160, S162, S163, S164); 2026-11-16 (S166 to S178 ingest): a second paragraph added at the end, headed Added 16 November 2026, later, on ICM 2D (S166, S170, S172, S178); 2026-11-16 (S179 ingest): the drafter of the seven ICM notes named as ChatGPT (S179); 2026-11-16 (S180 to S187 ingest): one paragraph added at the end on the shared 2D engine (S184); 2026-11-16 (S188 to S190 ingest): one paragraph added at the end on the 2021 Water Talks webinar (S188)"
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

**Added 16 November 2026: scripting and data.** Seven notes Bob supplied, drafted by ChatGPT from Autodesk Help [S179](../sources/S179-note-icm-notes-drafted-by-chatgpt.md) and not run (Q90), give the scripting side. Autodesk documents Ruby 3.4.6 for UI and Exchange scripting from ICM 2027.0, replacing Ruby 2.4.0 [S160](../sources/S160-note-icm-ruby-version-compatibility.md), and ICM Exchange for Ultimate licenses [S159](../sources/S159-note-icm-ruby-ui-vs-exchange.md). The two network types keep their objects in different tables, `hw_node` and `sw_node` for nodes [S162](../sources/S162-note-icm-network-tables-and-fields.md), and report node level as `DEPNOD` (InfoWorks) and `HEAD` (ICM SWMM) [S163](../sources/S163-note-icm-results-field-crosswalk.md). Autodesk's 2027 conversion pages list `.inp` import support through EPA SWMM 5.1.015 [S164](../sources/S164-note-swmm-inp-conversion-qa.md). See [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md) and [Checking a SWMM5 model's conversion into ICM](../concepts/swmm5-to-icm-conversion-checks.md).

**Added 16 November 2026, later: 2D.** Ten more notes from the GPT plugin for Autodesk [S166](../sources/S166-note-icm-notes-from-gpt-plugin.md), AI-written and not run (Q90), cover ICM's 2D side: a manhole's flood type sets its exchange with the mesh (a weir on ground level and shaft circumference for flood type 2D) [S170](../sources/S170-note-icm-1d-2d-node-exchange.md), and subgrid sampling, a Tech Preview in the 2027 help, builds volume-level tables inside elements [S172](../sources/S172-note-icm-2d-subgrid-sampling.md). From Bob's own articles: CNSWMM infiltration came to the 2D mesh in ICM 2025.1 [S178](../sources/S178-li-cnswmm-on-the-icm-2d-mesh.md). See the five ICM 2D pages, starting at [ICM 2D: terrain, mesh and subgrid sampling](../concepts/icm-2d-mesh-and-subgrid.md).

**Added 16 November 2026, from the EXTRAN and QA ingest.** ICM InfoWorks and ICM SWMM networks share one 2D engine, based on the Mulet and Alcrudo unstructured flood solver (MULFLOOD), but not a 1D engine: in 2023 ICM SWMM ran the SWMM 5.2.3 engine and InfoWorks a proprietary one [S184](../sources/S184-li-unified-2d-engine-icm.md).

**Added 16 November 2026, from Bob's 2021 webinar** [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). As he gave it then:
- Lineage "going back at least to the late '70s": WALLRUS, SPIDA, HydroWorks CS, "a few RS versions", then ICM "I guess since 2009".
- ICM networks hold SWMM parts: SWMM 5 water quality, SWMM 5 LIDs (called SUDS), SWMM 5 and SWMM 4 RDII, SWMM hydrology, and Green-Ampt and modified Horton infiltration from SWMM (Q13).
- ICM SWMM networks run the One SWMM engine, Innovyze's build of SWMM 5, which InfoSWMM and InfoDrainage share; it was tested every night on at least 500 files against EPA SWMM 5.1.015. ICM 2021.3 had 2D in ICM SWMM networks.
- Three 1D solutions (conduit, pressure, force main), at least five computational points per link, six node head-loss types, a slot set by celerity ratio, time-step halving, and an initialization to steady state before every run. See [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md) and [Time stepping in ICM and SWMM 5](../concepts/time-stepping-icm-and-swmm5.md).
