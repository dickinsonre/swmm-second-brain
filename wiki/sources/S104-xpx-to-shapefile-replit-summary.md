---
title: "S104: XPX to Shapefile Converter, summary written by Replit Agent (v0.1.0)"
type: source
raw: raw/apps/xps-to-shape--robertdickinson-v0.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, xpswmm, gis, migration]
reviewed: 11/16/2026
---
**What it is.** A technical summary of XPX to Shapefile Converter, version 0.1.0: a Flask app that reads an XPSWMM XPX file and writes its nodes, links and polygons as ESRI Shapefiles in a ZIP. It is one of Bob's Replit apps, at `xps-to-shape--robertdickinson.replit.app`. Raw file: [raw/apps/xps-to-shape--robertdickinson-v0.1.0.md](../../raw/apps/xps-to-shape--robertdickinson-v0.1.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says the project files do not identify an AI tool that built it. The copy here was read out of the editor of the Replit project named XpsToShape on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It accepts `.xpx` and `.txt` uploads up to `50 * 1024 * 1024` bytes.
- The parser handles lines beginning `NODE`, `LINK`, `CONDUIT`, `PIPE`, `POLYGON` or `SUBCATCHMENT`.
- Outputs are `nodes.shp`, `pipes.shp` and `catchments.shp`. It assigns a coordinate reference system, with a heuristic EPSG suggestion, and does not reproject coordinates or convert units.
- The bundled sample parsed as 3 nodes, 2 links and 2 polygons, and converted to a ZIP of 15 shapefile component files.
- The test command discovered 0 tests.
- It is meant to help move XPSWMM data into GIS tools such as InfoDrainage. It runs no hydraulic simulation.
- No license is stated for the app.

**Limits it states.** Other XPX variants, malformed uploads and the size limit were not checked. The geographic accuracy of the output was not verified. Only the root page of the deployed app was requested. No release date is recorded for 0.1.0.

**Checked at ingest.** Three layers of five component files each make the 15 (our arithmetic).

**Feeds:** [XPX to Shapefile Converter (app)](../entities/xpx-to-shapefile-converter.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [InfoDrainage Explorer (app)](../entities/infodrainage-explorer.md).
