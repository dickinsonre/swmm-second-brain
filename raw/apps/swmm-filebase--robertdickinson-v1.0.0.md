---
name: SWMM5 Network Miner
file: swmm-filebase--robertdickinson
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://swmm-filebase--robertdickinson.replit.app, repo: https://github.com/dickinsonre/SWMM-Filebase}
engines:
  - {name: "EPA SWMM through PySWMM and swmm-toolkit", version: "PySWMM 2.1.0; swmm-toolkit 0.17.0", source: "uv.lock:30-56", commit: "not stated", license: "PySWMM BSD-2-Clause; swmm-toolkit CC0-1.0 plus third-party terms"}
  - {name: "Bundled browser SWMM WebAssembly module", version: "not stated", source: "client/public/swmm/js.js and js.wasm", commit: "not stated", license: "not checked"}
stack: TypeScript, React, Vite, Express, PostgreSQL, Drizzle ORM, Replit Object Storage, GitHub API, PySWMM
units: both
ai_use: No model API call found in app source; static rule-based QA/QC. Details under AI use.
---

# SWMM5 Network Miner: Organize, inspect, compare, and run SWMM models

## What it does

SWMM5 Network Miner gives stormwater model users a browser interface for organizing, searching, inspecting, and exporting SWMM model files. It accepts `.inp` and `.xp` uploads and groups files into directories. Users can compare model text, view structural QA/QC findings, inspect database-wide summaries, and run simulations for supported `.inp` models. The app can attach simulation reports and output files and includes a conduit discretization tool. (README.md:9-19; client/src/components/Sidebar.tsx:76-82; server/routes.ts:668-719; server/routes.ts:1401-1519)

## How it computes

1. `parseInpFile` reads sectioned SWMM text and counts nodes, links, and subcatchments. `parseCoordinates` reads node coordinates, link vertices, polygons, and link endpoints. (server/inp-parser.ts:46-117)
2. `analyzeInpFile` checks expected sections, node and link references, conduit values, and connectivity. It starts the health score at 100, subtracts 15 per error, 5 per warning, and 1 per informational finding, applies missing-section and model-structure deductions, then clamps the score to 0–100. (client/src/lib/inpAnalyzer.ts:30-48, 245-258)
3. `parseInpSections` and `computeLineDiff` split model text into sections and compare their lines for the comparison view. (client/src/lib/diff.ts:21-59)
4. `accumulateInsightsFromContent` collects model dimensions, roughness, routing methods, and other values from the search index. `computeAndStoreInsights` bins those values for the database-insights page. Pipe diameter values below 10 are treated as feet and converted to inches; larger values are rounded as inches. Other dimensions are binned as read from the file. (server/indexing.ts:28-52, 73-80, 108-220)
5. `applyReswmm` selects a target conduit length from either a fixed interval or a diameter-to-length ratio. It computes `segment count = max(1, ceil(conduit length / target length))`, divides the conduit length evenly across those segments, and writes new model sections when a conduit is split. (server/reswmm.ts:315-346, 482-594)
6. The server simulation path writes a temporary `.inp` file and calls `python3 server/python/run_swmm.py`. That script runs `pyswmm.Simulation`; the server attaches nonempty `.rpt` and `.out` files and parses the report. (server/routes.ts:107-186; server/python/run_swmm.py:1-8)

## Inputs and outputs

- Inputs: `.inp` and `.xp` model files; optional `.rpt` and `.out` simulation results. Upload routes reject other model extensions. (client/src/components/Sidebar.tsx:76-82; server/routes.ts:501-509, 632-644)
- Outputs: CSV and JSON downloads from the model library, ZIP exports of selected files or a directory, and `.rpt` / `.out` simulation artifacts. (client/src/pages/Dashboard.tsx:493-530; server/routes.ts:1303-1345; server/routes.ts:163-185)
- API: `/api/inp-files`, `/api/directories`, `/api/stats`, comparison and search routes, upload/edit/delete routes, simulation and run-history routes, GitHub browse/import routes, results routes, and `/api/reswmm/apply`. (server/routes.ts:268-1551)
- Storage: PostgreSQL holds model metadata, result metadata, search-index text, simulation jobs, insights cache, and activity records. Model and result file contents are stored in Replit Object Storage; the database stores object paths. Theme settings and the admin token are stored in browser local storage. (shared/schema.ts:6-81; server/objectStorage.ts:50-78, 212-224; client/src/context/ThemeContext.tsx:23-36; client/src/lib/adminToken.ts:5-19)

## Contents

- The app package and sidebar show version 1.0.0. (package.json:3; client/src/components/Sidebar.tsx:481-482)
- The app defines seven main page routes: model library, compare, QA/QC, run history, insights, ReSWMM, and settings. (client/src/App.tsx:21-27)
- A read-only development database query on 2026-11-15 counted 2,001 `.inp` model records, 0 `.xp` records, 36 directories, 878 result-file records, and 2,001 search-index records. The same query counted 0 simulation-job records and 0 activity-log records. The query counted rows in the tables defined in `shared/schema.ts:12-80`.
- A file count run on 2026-11-15 found five bundled sample `.inp` files in `server/samples/`.

## Checks

- `npm run build`: passed on 2026-11-15. It built the client and server bundles.
- `npm run check`: failed on 2026-11-15 with 19 TypeScript `TS2802` diagnostics about iterating Set, Map, and iterator values with the configured compiler target.
- No test script is defined in `package.json:6-12`, and no project test/spec files were found in the source search. No automated tests were run.
- Browser preview checks on 2026-11-15 loaded `/`, `/compare`, `/ai-analysis`, `/runs`, `/insights`, `/reswmm`, and `/settings`. No JavaScript errors appeared. The settings page logged a browser warning that the password field is not inside a form. These checks used the development preview.
- Human review: none recorded.

## What this does not show

1. The database counts above are from the development database. Production database contents were not checked.
2. Simulation execution was not tested. The development database query found no simulation-job records.
3. Uploading `.xp` files was not tested. The current development database contains no `.xp` model records.
4. GitHub browsing/import, model edits, file deletion, exports, and interactive controls were not exercised.
5. The production UI was not loaded in a browser. The page checks used the development preview, even though deployment metadata reports a public URL and a successful current build.
6. Pipe diameters have a feet-to-inches conversion, but a consistent conversion layer for all model quantities was not found. Handling of every US customary and SI input was not checked.
7. The bundled browser WebAssembly engine's version, source revision, and license were not identified in the project.
8. No person review is recorded for this summary or in the project checks.

## How to reproduce

```bash
npm install
npm run dev
npm run build
npm run check
```

`npm run dev` starts the development server. `npm run build` creates the production build. `npm run check` runs TypeScript. The repository does not define an automated test command. (package.json:6-12)

## Credits and licenses

- Robert Dickinson is the named author of this summary and the app.
- The project declares MIT in `package.json:5`. No separate project license file was found.
- Core libraries and their package-lock metadata: React and React DOM use MIT (package-lock.json:8568, 8608); Express uses MIT (package-lock.json:6473); Drizzle ORM uses Apache-2.0 (package-lock.json:6065); the Google Cloud Storage client uses Apache-2.0 (package-lock.json:1365).
- PySWMM is BSD-2-Clause. (`.pythonlibs/lib/python3.11/site-packages/pyswmm-2.1.0.dist-info/licenses/LICENSE.txt`)
- swmm-toolkit is CC0-1.0 and notes that bundled third-party libraries have separate terms. (`.pythonlibs/lib/python3.11/site-packages/swmm_toolkit-0.17.0.dist-info/licenses/LICENSE.md`)
- This is a selected list of core dependencies, not a complete inventory of transitive dependency licenses.

## AI use

The QA/QC feature uses deterministic checks in `analyzeInpFile`; no AI model API call was found in the current client or server application source. Git history names Replit Agent on several implementation commits and Robert Dickinson on a viewer fallback change. No other AI builder is named in the project records reviewed. (client/src/lib/inpAnalyzer.ts:39-48, 245-258; Git log)

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-07-23: Added post-merge dependency setup.
- 2026-07-23: Kept viewer side panels available when WebGL is unavailable.
- 2026-07-20: Updated the website preview image.
- 2026-07-20: Polished labels, accessibility, and mobile layouts.
- 2026-07-20: Added engineering workflow improvements.
- 2026-07-20: Added engineering workflow improvements.
- 2026-07-20: Added search and pagination for the model library.
- 2026-07-20: Added search and pagination for the model library.
- 2026-07-20: Added search and pagination for the model library.
- 2026-07-20: Added admin passphrase authentication and API protection.

