---
title: XPX to Shapefile Converter (app)
type: entity
updated: 2026-11-15
sources: [S104]
tags: [apps, replit, xpswmm, gis, migration]
reviewed: 11/16/2026
---
Bob's Replit app XPX to Shapefile Converter: a Flask app that reads an XPSWMM XPX file and writes its nodes, links and polygons as ESRI Shapefiles in a ZIP. Version 0.1.0, at `xps-to-shape--robertdickinson.replit.app` [S104](../sources/S104-xpx-to-shapefile-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S104](../sources/S104-xpx-to-shapefile-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S104](../sources/S104-xpx-to-shapefile-replit-summary.md)
- It accepts `.xpx` and `.txt` uploads up to `50 * 1024 * 1024` bytes.
- The parser handles lines beginning `NODE`, `LINK`, `CONDUIT`, `PIPE`, `POLYGON` or `SUBCATCHMENT`.
- Outputs are `nodes.shp`, `pipes.shp` and `catchments.shp`. It assigns a coordinate reference system, with a heuristic EPSG suggestion, and does not reproject coordinates or convert units.
- The bundled sample parsed as 3 nodes, 2 links and 2 polygons, and converted to a ZIP of 15 shapefile component files.
- The test command discovered 0 tests.
- It is meant to help move XPSWMM data into GIS tools such as InfoDrainage. It runs no hydraulic simulation.
- No license is stated for the app.

**What it does not show.** Other XPX variants, malformed uploads and the size limit were not checked. The geographic accuracy of the output was not verified. Only the root page of the deployed app was requested. No release date is recorded for 0.1.0. [S104](../sources/S104-xpx-to-shapefile-replit-summary.md)

**Noted at ingest.** Three layers of five component files each make the 15 (our arithmetic).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [InfoDrainage Explorer (app)](infodrainage-explorer.md).
