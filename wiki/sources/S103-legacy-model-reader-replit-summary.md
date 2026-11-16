---
title: "S103: InfoSewer and InfoSWMM Legacy Model Reader, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/data-importer-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-07-22
ingested: 2026-11-15
tags: [apps, replit, infosewer, infoswmm, legacy, icm, migration]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of InfoSewer and InfoSWMM Legacy Model Reader, version 1.0.0: an app that reads InfoSWMM `.ISDB` and InfoSewer `.IEDB` model files, turns their DBF tables into a network model, and prepares SWMM5 and ICM exports. It is one of Bob's Replit apps, at `data-importer-robertdickinson.replit.app`. Raw file: [raw/apps/data-importer-robertdickinson-v1.0.0.md](../../raw/apps/data-importer-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says the checked files do not name the AI tools used to build it. The copy here was read out of the editor of the Replit project named InfoSWMM-InfoSewer-Reader on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** The tests cover synthetic fixtures, not every real DBF variant. No hydraulic simulation was run. Uploading, editing and export downloads were not exercised. The production build was not tested.

**Checked at ingest.** This is the first source here that names tables inside an ISDB or IEDB model. [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md) had listed the file layout as not in the sources.

**Feeds:** [InfoSewer and InfoSWMM Legacy Model Reader (app)](../entities/infosewer-infoswmm-legacy-model-reader.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md), [InfoWorks ICM](../entities/infoworks-icm.md), [Camel_SWMM (app)](../entities/camel-swmm.md).
