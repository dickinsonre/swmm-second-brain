---
title: InfoSWMM and InfoSewer
type: entity
updated: 2026-11-15
sources: [S11, S17, S103]
tags: [innovyze, legacy, engine]
reviewed: 2026-11-15
changed_after_review: "2026-11-15 (Replit ingest): one paragraph added near the end, headed Added 15 November 2026, on the Legacy Model Reader app (S103)"
---
Two Innovyze products. Bob was their Product Sector Leader from January 2008, along with H2OMAP SWMM and H2OMap Sewer [S11](../sources/S11-li-my-history-with-swmm.md).

**InfoSWMM**
- An ArcGIS extension that works in ArcMap and uses the EPA SWMM 5 C code as its engine, with import and export to SWMM 5 [S11](../sources/S11-li-my-history-with-swmm.md).
- Has the same three routing options as SWMM 5: steady flow, kinematic wave, dynamic wave [S17](../sources/S17-li-routing-options.md).

**InfoSewer**
- Two routing options: steady state and extended-period simulation [S17](../sources/S17-li-routing-options.md).
- Bob's opinion: its steady state is the best of the five products compared, "as it has good flow loading and flow splitting options" [S17](../sources/S17-li-routing-options.md).

**Company history, as [S11](../sources/S11-li-my-history-with-swmm.md) tells it.** MWH Soft became Innovyze. In 2017 EQT owned both Innovyze (bought from Stantec, via MWH) and XP Solutions (bought from Cardno), which sells XP-SWMM [S11](../sources/S11-li-my-history-with-swmm.md).

**Not in the sources yet.** The ISDB file layout, the InfoSewer engine, manhole loads, and the migration to ICM. Queued: 50 LinkedIn articles name InfoSewer or InfoSWMM in the title, among them "From Legacy to Future: Recalling the Engine of InfoSewer" (2024).

**Added 15 November 2026: a reader for the old model files.** [InfoSewer and InfoSWMM Legacy Model Reader (app)](infosewer-infoswmm-legacy-model-reader.md) reads InfoSWMM `.ISDB` and InfoSewer `.IEDB` models as sets of DBF tables. Its summary names a `SCENARIO` table with parent references and the ANODE/ALINK and CBNODE/CBLINK tables from which active elements are counted, and it writes SWMM5 and ICM exports without running either engine [S103](../sources/S103-legacy-model-reader-replit-summary.md). Replit Agent wrote that summary and Bob has not read it (Q67).

See [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [InfoWorks ICM](infoworks-icm.md).
