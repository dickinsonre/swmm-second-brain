---
name: InfoSewer and InfoSWMM Legacy Model Reader
file: data-importer-robertdickinson
version: 1.0.0
date: 2026-07-22
author: Robert Dickinson
links: {replit: https://data-importer-robertdickinson.replit.app, repo: https://github.com/dickinsonre/InfoSWMM-InfoSewer-Reader}
engines: none
stack: TypeScript, React, Vite, Express, Tailwind CSS, in-memory sessions, Replit hosting, Google Fonts, optional SWMM Pilot handoff
units: both
ai_use: AI tools used to build the app are not identified in the checked project files; this summary was written by Replit Agent.
---

# InfoSewer and InfoSWMM Legacy Model Reader: inspect legacy model databases and prepare exports

## What it does

The app reads InfoSWMM `.ISDB` and InfoSewer `.IEDB` model files and turns their DBF tables into a network model. It is for engineers and modelers who need to inspect inherited legacy data, understand scenario structure, and find data-quality or export issues. It provides network, table, scenario, health, comparison, and export views. It can prepare SWMM5 input and ICM migration files, but it does not run a hydraulic simulation. [README.md:1-24; client/src/pages/home.tsx:47-52; server/routes.ts:1104-1115, 1583-1609]

## How it computes

1. The server accepts DBF, ZIP, and MXD uploads. ZIP extraction keeps DBF and MXD files, then `readAllDbfFilesWithFolders` walks the extracted folder tree and parses DBF records with `readDbfFile`. The parser checks field and record budgets before reading records. [server/routes.ts:101-104, 138-153, 351-392; server/dbfReader.ts:6-39, 68-175]
2. `buildModel` creates a structured network from the parsed tables. It joins related records by trimmed element IDs and fills node, link, and subcatchment properties from product-specific tables. [server/modelBuilder.ts:9-58, 82-98, 151-168]
3. `ScenarioBuilder.buildTree` reads `SCENARIO` parent references and joins each child to its parent. It counts active and inactive elements from scenario or base ANODE/ALINK and CBNODE/CBLINK tables. [server/scenarioBuilder.ts:245-295, 354-430]
4. Health and connectivity checks count missing elevations, zero-length links, dangling links, disconnected components, and other structural conditions. Connectivity starts at 100, subtracts issue weights, and clamps the result to 0 through 100. Export grading also starts at 100, subtracts issue weights, clamps the result, and applies caps for blockers and selected unit or roughness warnings. [server/healthReport.ts:4-82; server/connectivityCheck.ts:265-300; server/exportGrader.ts:453-470]
5. `SWMM5Exporter.export` writes a SWMM5 `.inp` text file for the selected scenario; no SWMM executable is invoked. For dry-weather flow, the conversion is `exported flow = source flow × TO_CFS(source unit) / TO_CFS(target unit)`. `exportIcmBundle` converts US subcatchment area with `area in hectares = area in acres × 0.404686`; SI area passes through. [server/swmm5Exporter.ts:81, 1161-1201; server/icmExporter.ts:65, 171-197; README.md:20-24]

## Inputs and outputs

- Inputs: uploaded `.dbf`, `.zip`, and `.mxd` files; bundled demonstration ZIPs; and server-side folders when permitted by configuration. The ZIP reader extracts DBF and MXD entries. The app can view MXD bytes, but does not parse ArcMap geometry from the MXD. [server/routes.ts:101-104, 138-153, 266-310, 351-392, 638-680]
- API: the endpoint registry describes model loading, model and table inspection, scenarios, comparison, quality checks, edits, diagnostics, and exports. It lists 53 endpoint entries, counted from the registry array. [server/routes.ts:1668-1727; count run against that array]
- Outputs: SWMM5 `.inp`, ICM bundle ZIP, CSV inventory, GeoJSON, HTML dossier, reading report JSON and PDF, and a complete ZIP archive. [server/routes.ts:768-799, 1104-1115, 1550-1609, 1629-1655]
- Storage: parsed records, models, comparison state, and edit history are held in the Express process's in-memory session map. Uploads and extracted files use temporary server directories. Session cleanup clears those directories on reset, expiration, or eviction. No persistent database write was found in the model-loading path checked. [server/sessionStore.ts:13-32, 70-92, 99-177; server/routes.ts:101-105, 351-392]
- External services: Replit hosts the app. The HTML loads fonts from Google Fonts. The optional SWMM Pilot handoff sends a URL for the exported model to that separate service; the UI warns users not to use it for confidential models. [client/index.html:17-19; client/src/components/export-panel.tsx:316-329]

## Contents

- Page modules: 2, `home.tsx` and `not-found.tsx`, counted from `client/src/pages/`.
- Main navigation tabs: 19, counted from the `VALID_TABS` set in `client/src/pages/home.tsx:47-52`.
- Bundled demonstration models: 38 ZIP archives, counted from `server/demo-data/`.
- Plain-language field explainers: 79 entries, counted from `D({ ... })` definitions in `shared/fieldDictionary.ts:34-138`.
- API descriptions: 53 entries, counted from the endpoint registry in `server/routes.ts:1673-1727`.
- Conversion regression fixtures: 11 fixture cases, listed in `tests/conversion/runConversionTests.ts` in the test run.
- Fixed model, user, or question records: none identified. Models are loaded at runtime into sessions; this is not a fixed content catalog. [server/sessionStore.ts:13-32; server/routes.ts:351-392, 564-621]

## Checks

- Conversion regression suite: `npx tsx tests/conversion/runConversionTests.ts` completed with 100 passed and 0 failed. The run exercised 11 synthetic fixture cases. [test run on 2026-11-15; tests/conversion/runConversionTests.ts]
- Main page `/`: the preview rendered the app shell and an already loaded ISDB model. Its browser log reported `GET /api/table/JUNCTION.DBF` as 404; the cause was not investigated. [app preview run on 2026-11-15]
- Not-found page `/not-a-real-page`: the preview rendered the 404 page; no browser error was reported for that capture. [app preview run on 2026-11-15]
- Human review: none recorded.

## What this does not show

1. The main-page 404 request is unresolved. [app preview run on 2026-11-15]
2. The preview checked only the visible first viewport. Uploading a new model, editing, export downloads, and the other in-app tabs were not exercised in this check.
3. The test suite covers synthetic conversion fixtures. It does not establish correctness for every real-world DBF variant, ZIP, model, scenario, or export.
4. No hydraulic or water-quality simulation was run. The app creates and checks model data; it does not invoke SWMM5 or the InfoSewer solver. [README.md:20-24]
5. The README describes a browser-only, no-upload reader, but the current server code accepts uploads and processes model files on the server. This summary follows the current code. [README.md:3, 18, 86, 128-130; server/routes.ts:351-392]
6. The production build command, deployment behavior, browser compatibility, and security properties were not tested for this summary.
7. Package metadata gives version `1.0.0`, but there is no separate release tag or release date checked. The front-matter date is the last commit date that changed `package.json`, not a verified release date. [package.json:3; `git log -1 -- package.json` run on 2026-11-15]
8. The checked project files do not record a human review of this summary or identify which AI tools contributed to building the application.

## How to reproduce

- Development server: `npm run dev`. [package.json:6-9; .replit:1-3]
- Conversion tests: `npx tsx tests/conversion/runConversionTests.ts`. [tests/conversion/README.md:1-14; .replit:49-55]
- Production build: `npm run build`, followed by `npm start`. The build was not run for this summary. [package.json:6-10; .replit:19-22]

## Credits and licenses

- Robert Dickinson is named as the project author. [README.md:163-165]
- The project declares MIT in `package.json`; no standalone root license file was found. [package.json:1-5; license-file search run on 2026-11-15]
- Core libraries and manifest licenses checked in installed package metadata: React and React DOM (MIT), Express (MIT), Vite (MIT), TypeScript (Apache-2.0), `dbffile` (MIT), Multer (MIT), `adm-zip` (MIT), PDFKit (MIT), Drizzle ORM (Apache-2.0), TanStack Query (MIT), Wouter (Unlicense), Recharts (MIT), Lucide React (ISC), Tailwind CSS (MIT), Zod (MIT), `pg` (MIT), and `tsx` (MIT). [package.json:13-108; installed package manifests read on 2026-11-15]
- EPA SWMM5 is an output format target and optional simulation destination, not an engine bundled or invoked by this app. [README.md:20-24; server/routes.ts:1104-1115]

## AI use

The checked README, project notes, source, configuration, and recent Git history do not name AI tools used to build the app. `.replit` labels a workflow author as `agent`, but does not identify a specific AI tool. Robert Dickinson is named as project author in the README; the checked files do not assign his work to particular modules. [README.md:163-165; .replit:24-30]

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-07-29: Added an InfoSWMM documentation asset and updated metadata.
- 2026-07-22: Updated the model summary dashboard and navigation.
- 2026-07-22: Added a conversion regression test suite.
- 2026-07-22: Hardened security and stability.
- 2026-07-22: Corrected hydraulic export behavior.

Dates and descriptions are from the newest entries in `git log`, read on 2026-11-15.
