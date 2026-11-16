---
title: "ICM 2D: three benchmark cases"
type: concept
updated: 2026-11-16
sources: [S166, S176]
tags: [icm, 2d, benchmark, verification]
reviewed: no
---
Three small InfoWorks ICM 2D cases, each with one question and a check that can be read from numbers. The note names them for the ICM Lab Canon [S176](../sources/S176-note-icm-2d-benchmark-cases.md). These pages rest on notes written by the GPT plugin for Autodesk [S166](../sources/S166-note-icm-notes-from-gpt-plugin.md): AI-written text whose facts about ICM are reported from Autodesk's 2027 help and were not checked against ICM, and whose tests have not been run (Q90).

**1. Closed rainfall box** [S176](../sources/S176-note-icm-2d-benchmark-cases.md)
- A flat, dry zone 100 ft by 100 ft, Vertical Wall on every edge.
- 1.00 in of direct rain over one hour at 100 percent; no other input, no infiltration, no evaporation; `Ignore rain falling on dry elements` unchecked.
- Expected: 833.33 cu ft stored on exactly 10,000 sq ft, a mean depth of 1.00 in. Record the residual against the area actually meshed.

Our check of the arithmetic: 10,000 sq ft × 1.00 in ÷ 12 in/ft = 833.33 cu ft.

**2. Reversing manhole** [S176](../sources/S176-note-icm-2d-benchmark-cases.md). One 1D node and a small surface depression. Raise the sewer head above the opening, then lower it while water remains on the surface, and read the signed exchange hydrograph and the levels on both sides. The exchange relations are on [ICM 2D: boundaries and 1D-2D exchange](icm-2d-boundaries-and-exchange.md).

**3. Embankment with a gap** [S176](../sources/S176-note-icm-2d-benchmark-cases.md). One opening in a raised feature and a short pulse on one side, run in the mesh configurations of the subgrid comparison. Read a transect through the gap and one across intact crest, and record arrival on the far side, volume along each route and when overtopping begins. See [ICM 2D: terrain, mesh and subgrid sampling](icm-2d-mesh-and-subgrid.md).

**Rules for all three** [S176](../sources/S176-note-icm-2d-benchmark-cases.md): record the ICM build, network commit, terrain, mesh, event, controls and outputs; set the acceptance criteria before running.

**Status.** Designs, not results. None has been run.

**Related.** [ICM 2D: timestep, volume balance and results](icm-2d-runs-and-checks.md); the SWMM and ICM two-pipe design on [Checking a SWMM5 model's conversion into ICM](swmm5-to-icm-conversion-checks.md).
