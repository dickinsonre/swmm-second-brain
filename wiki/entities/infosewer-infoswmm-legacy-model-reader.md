---
title: InfoSewer and InfoSWMM Legacy Model Reader (app)
type: entity
updated: 2026-11-15
sources: [S103, S146]
tags: [apps, replit, infosewer, infoswmm, legacy, icm, migration]
reviewed: 11/16/2026
---
Bob's Replit app InfoSewer and InfoSWMM Legacy Model Reader: an app that reads InfoSWMM `.ISDB` and InfoSewer `.IEDB` model files, turns their DBF tables into a network model, and prepares SWMM5 and ICM exports. Version 1.0.0, at `data-importer-robertdickinson.replit.app` [S103](../sources/S103-legacy-model-reader-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S103](../sources/S103-legacy-model-reader-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S103](../sources/S103-legacy-model-reader-replit-summary.md)
- It accepts DBF, ZIP and MXD uploads. It can view MXD bytes but does not parse ArcMap geometry.
- Scenarios are built from the `SCENARIO` table's parent references; active and inactive elements are counted from the ANODE/ALINK and CBNODE/CBLINK tables.
- Connectivity and export grades each start at 100, subtract issue weights and are clamped to 0 through 100.
- Exports: SWMM5 `.inp`, an ICM bundle ZIP, a CSV inventory, GeoJSON, an HTML dossier, a reading report as JSON and PDF, and a complete ZIP. No SWMM executable is invoked.
- For the ICM bundle, US subcatchment area is converted with hectares = acres × 0.404686.
- Counts: 19 main navigation tabs, 38 bundled demonstration ZIP archives, 79 field explainers, 53 API endpoint entries.
- The conversion regression suite completed with 100 passed and 0 failed, over 11 synthetic fixture cases.
- On the main page the browser log reported a 404 for `GET /api/table/JUNCTION.DBF`; the cause was not investigated.
- The README describes a browser-only reader with no upload; the current server code accepts uploads and processes files on the server.
- An optional "SWMM Pilot handoff" sends a URL for the exported model to a separate service; the UI warns against using it for confidential models.
- Repository: https://github.com/dickinsonre/InfoSWMM-InfoSewer-Reader.

**What it does not show.** The tests cover synthetic fixtures, not every real DBF variant. No hydraulic simulation was run. Uploading, editing and export downloads were not exercised. The production build was not tested. [S103](../sources/S103-legacy-model-reader-replit-summary.md)

**Noted at ingest.** This is the first source here that names tables inside an ISDB or IEDB model. [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md) had listed the file layout as not in the sources.

**Added 15 November 2026: a guide to the next step.** [InfoSewer to InfoWorks ICM (app)](infosewer-to-infoworks-icm-guide.md) is a guide to moving InfoSewer data into InfoWorks ICM, with ID, CSV and SQL checkers; it converts nothing itself [S146](../sources/S146-infosewer-to-infoworks-icm-replit-summary.md).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md), [InfoWorks ICM](infoworks-icm.md), [Camel_SWMM (app)](camel-swmm.md).
