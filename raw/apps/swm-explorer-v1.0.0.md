---
name: SWMManywhere Explorer
file: swm-explorer
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://swm-explorer.replit.app, repo: none}
engines:
  - {name: SWMManywhere, version: 0.1.17, source: installed Python package, commit: not recorded, license: BSD License classifier}
  - {name: EPA SWMM5 WebAssembly, version: not checked, source: wasm/swmm5.js and wasm/swmm5.wasm, commit: not recorded, license: not stated}
stack: Python, FastAPI, SWMManywhere, React, TypeScript, Vite, Express, SQLite, OpenStreetMap, Overpass API, AWS elevation tiles
units: SI
ai_use: No AI tool used to build the app is identified in the project records.
---

# SWMManywhere Explorer: Explore and generate urban drainage models

## What it does

The app explains the SWMManywhere workflow for building urban drainage models from a selected area. Users can browse preloaded city examples and technical panels, or submit a bounding box to the Python backend for model generation. The app displays network geometry and summary metrics and can provide an EPA SWMM `.inp` file. A browser-based SWMM5 simulator accepts uploaded or generated `.inp` text and displays parsed simulation results. [client/src/App.tsx:10-16; client/src/pages/explorer.tsx:780-835, 3462-3468, 3606-3685; backend/main.py:73-85]

## How it computes

1. The backend accepts a bounding box in `[west, south, east, north]` order. It estimates width as `abs(east - west) * 111 * abs(cos(mid-latitude))` kilometers and height as `abs(north - south) * 111` kilometers. It rejects invalid coordinates and boxes wider or taller than 10 km. [backend/pipeline.py:173-210]
2. Rainfall depth in millimeters is converted to precipitation in meters per hour as `depth_mm / 1000 / (duration_min / 60)`, unless an explicit precipitation override is supplied. Rainfall time series can use uniform, triangular, Chicago, or SCS Type II distributions. [backend/pipeline.py:11-76, 260-272]
3. Quick Mode writes a constant-value raster with elevation `100.0` and sets a default slope of `0.005`; it is a flat DEM, not terrain sampled for the selected area. Normal generation delegates the configured bounding box and overrides to `swmmanywhere(config)`. [backend/pipeline.py:274-313, 394]
4. The backend reads generated edge and node layers, converts geometries to GeoJSON, and derives counts and summary statistics from those layers. If those layers cannot be read, it attempts to derive some counts and pipe geometry from the `.inp` file. [backend/pipeline.py:430-544, 577-643]
5. The frontend's network quality score is a heuristic. It totals five checks, each scored out of 20: connectivity, slope, pipe-size consistency, outfalls, and network density. It is not an independent hydraulic validation. [client/src/pages/explorer.tsx:96-175]
6. The browser simulator loads `wasm/swmm5.js`, calls SWMM5 open, start, step, end, report, and close functions, then parses the report into node and link summaries. The simulator's runtime-reported SWMM5 version was not checked in this run. [client/src/lib/swmm5-engine.ts:60-99, 111-170, 189-216]
7. The what-if analysis scales the base rainfall series and runs six scenarios with depth multipliers `0.54`, `0.75`, `1.00`, `1.25`, `1.50`, and `1.79`. These are the UI's configured scenario factors, not return-period estimates verified here. [client/src/pages/explorer.tsx:862-900]

The app's data catalog describes OpenStreetMap streets and waterways, NASADEM elevation data, and Google-Microsoft Open Buildings. The running code also requests road data from the Overpass API and uses OpenStreetMap and AWS elevation tile URLs for maps. [client/src/data/swmmanywhere-data.ts:252-275; client/src/pages/explorer.tsx:584-620, 1042-1055]

## Inputs and outputs

- Generation input: a geographic bounding box and optional generation, rainfall, and hydraulic-design options. The backend validates the box before starting the pipeline. [client/src/pages/explorer.tsx:665-686; backend/main.py:30-39, 73-85]
- Simulation input: generated `.inp` content or a user-selected text file read in the browser. [client/src/pages/explorer.tsx:780-835]
- API routes: `GET /api/swm/health`, `POST /api/swm/bbox-info`, `POST /api/swm/generate`, `GET /api/swm/status/{job_id}`, `GET /api/swm/result/{job_id}`, `GET /api/swm/stream/{job_id}`, `GET /api/swm/download/{job_id}`, `GET /api/swm/dem/{job_id}`, and `GET /api/swm/dem-info/{job_id}`. [backend/main.py:46-255]
- Outputs: GeoJSON network features and statistics, a downloadable `.inp` file when generation produces one, optional DEM GeoTIFF data and metadata, and browser-parsed SWMM report results. [backend/main.py:103-118, 167-255; backend/pipeline.py:541-553; client/src/lib/swmm5-engine.ts:189-203]
- Storage: job metadata and serialized results go to `backend/cache/jobs.db` (SQLite). Generated project files are stored under `backend/cache/results`. Old job records and result directories are removed when the store initializes if they exceed 24 hours. Uploaded `.inp` text is held in browser state. [backend/jobs.py:13-15, 38-67, 123-149; client/src/pages/explorer.tsx:822-835]

## Contents

Counts below were read from the current source data. The repository tree is the app's bundled reference data, not a scan of this project's filesystem.

- App routes: one content route, `/`, plus a not-found fallback. The content route has eight tab views. [client/src/App.tsx:10-16; client/src/pages/explorer.tsx:3606-3685]
- Bundled reference repository tree: 5 directories and 43 listed files. [client/src/data/swmmanywhere-data.ts:54-139]
- City presets: 247. [client/src/data/swmmanywhere-extended-data.ts:107-3998]
- Pipeline stages: 8. [client/src/data/swmmanywhere-data.ts:140-217]
- Graph-function catalog entries: 19. [client/src/data/swmmanywhere-data.ts:219-239]
- Graph-function dependency records: 19. [client/src/data/swmmanywhere-extended-data.ts:4123-4391]
- Data-source entries: 3; key parameters: 9; metric tiers: 4. [client/src/data/swmmanywhere-data.ts:252-289, 338-363]
- Parameter sensitivity records: 6. [client/src/data/swmmanywhere-extended-data.ts:4392-4509]
- Validation city records: 4; ecosystem tools: 5. [client/src/data/swmmanywhere-extended-data.ts:4510-4787]
- Limitation entries: 6; FAQ entries: 8. [client/src/data/swmmanywhere-extended-data.ts:4788-4862]

## Checks

- `npm run build`: passed. The build emitted warnings about stale browser data, a PostCSS source option, and a large JavaScript chunk.
- `npm run check`: failed with one TypeScript error at `server/index.ts:25`. The declared `IncomingMessage` extension in `server/index.ts:10-14` does not include `originalUrl`.
- Automated tests: no test script is configured in `package.json`; no project test suite was run. [package.json:1-12]
- Loaded the local app route `/`: HTTP 200. The browser preview showed the app, and its console had no application errors.
- Loaded `GET /api/swm/health`: HTTP 200 with `{"status":"ok","engine":"swmmanywhere"}`. [backend/main.py:46-48]
- Human review: none recorded.

## What this does not show

1. No model-generation job or SWMM simulation was run. The build and page-load checks do not establish hydraulic validity.
2. The tab views were not opened one by one. Only the root route was loaded in the browser preview.
3. External data downloads, model file downloads, DEM responses, and failure cases were not checked.
4. The public deployment URL was confirmed from deployment metadata, but the production app was not loaded or tested.
5. The WASM engine's runtime version was not checked.
6. No separate release date for package version `1.0.0` was found. The front matter date is the date this summary was written.
7. The source does not identify a GitHub repository for this app. The GitHub link in the UI points to the upstream SWMManywhere project.

## How to reproduce

- Start the web app: `npm run dev`
- Start the Python backend: `cd backend && python3 main.py`
- Run the TypeScript check: `npm run check`
- Build the app: `npm run build`
- No automated test command is configured. [package.json:1-12; .replit:1-2]

## Credits and licenses

- Robert Dickinson is named as the author of this summary. The local Git history records Robert Dickinson as the author of its commits.
- The app cites Dobson, Jovanovic, Alonso-Álvarez, and Chegini's 2025 SWMManywhere paper. [client/src/pages/explorer.tsx:3692-3701]
- The Python package metadata reports SWMManywhere version `0.1.17` and a BSD license classifier. The app's UI displays a BSD-3-Clause badge for the upstream project. [pyproject.toml:1-10; client/src/pages/explorer.tsx:3593-3603]
- `package.json` declares MIT for this Node package. No top-level license file was found in the project. [package.json:5]
- Installed package metadata identifies React, React DOM, Vite, and Express as MIT; Leaflet as BSD-2-Clause; React Leaflet as Hippocratic-2.1; Wouter as Unlicense; and TypeScript as Apache-2.0.
- The map displays OpenStreetMap contributor attribution. The project source does not state a separate license for its bundled map or reference data. [client/src/pages/explorer.tsx:1042-1055]

## AI use

The project source and documentation do not record which AI tools, if any, were used to build the app. The Git history attributes 37 commits to Robert Dickinson, but does not describe whether AI assistance was used. The project does not record a division of work between Robert Dickinson and any AI tools.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-03-08: Published the app.
- 2026-03-08: Added network quality scoring and comparison tools.
- 2026-03-08: Updated project documentation with feature ideas and implementation details.
- 2026-03-06: Added terrain data and a hillshade layer.
- 2026-03-06: Added terrain elevation data to map and download features.
- 2026-03-06: Added 93 city presets and associated data.
- 2026-03-06: Updated the SWMManywhere citation and corrected rainfall calculations.
