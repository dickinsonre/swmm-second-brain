---
name: SWMM5 Lego Model
file: swmm-lego-model
version: 0.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://swmm-lego-model.replit.app, repo: none}
engines:
  - {name: Quick Sim, version: project 0.0.0; engine version not stated, source: artifacts/swmm5-lego/src/lib/hydraulics.js, commit: not recorded, license: MIT declared by project; engine-specific terms not stated}
  - {name: EPA SWMM5 WASM, version: 5.2.4, source: https://github.com/OpenWaterAnalytics/Stormwater-Management-Model, commit: not recorded, license: not recorded}
stack: JavaScript, TypeScript, React, Vite, Recharts, EPA SWMM5 WebAssembly, browser localStorage, Express health endpoint, Google Fonts
units: both
ai_use: No project record names AI tools used to build the app; see AI use.
---

# SWMM5 Lego Model: Build and simulate stormwater drainage models

## What it does

The app lets a user assemble a stormwater drainage layout on a grid and select a rainfall profile. It answers how the entered layout responds in either a simplified JavaScript simulation or the EPA SWMM5 solver compiled to WebAssembly. Results include runoff and network time series, charts, and parsed SWMM reports. Models can be imported, saved in the browser, and exported for use outside the app.

## How it computes

1. The Quick Sim reads grid cells and their properties to assemble surface areas, drainage nodes, and connected links. Adjacent surface cells become subcatchments; area is calculated from cell count and the configured cell spacing. Link cells are traced between nodes. (`artifacts/swmm5-lego/src/lib/hydraulics.js:30-110,113-190`)
2. For pervious surfaces, the app applies a Curve Number runoff equation. It calculates `S = 1000/CN - 10` and `Ia = 0.2 × S`; cumulative rainfall at or below `Ia` produces no excess, otherwise excess is `(P - Ia)² / (P - Ia + S)`. Impervious runoff subtracts depression storage. (`artifacts/swmm5-lego/src/lib/hydraulics.js:5-11,215-237`)
3. The Quick Sim estimates overland and circular-pipe flow with Manning-based equations, then updates link flows and node depths using a simplified routing loop. Its route timestep is 15 seconds. This is not the EPA engine's dynamic-wave calculation. (`artifacts/swmm5-lego/src/lib/hydraulics.js:3,13-27,197-320`)
4. The EPA path converts the grid and selected storm to a SWMM `.INP` file, calls `swmm_run` in the browser's WebAssembly module, and reads its text `.RPT` and binary `.OUT` results. The app parses those outputs for display. The project documentation identifies the bundled engine as EPA SWMM5 5.2.4. (`artifacts/swmm5-lego/src/components/SWMM5LegoBuilder.jsx:451-479`; `artifacts/swmm5-lego/src/lib/swmmWasm.js:26-79`; `replit.md:62`; `artifacts/swmm5-lego/public/docs/SWMM5_Lego_Builder_Handover.md:443-448`)

## Inputs and outputs

- The user paints surfaces, nodes, and links, edits model properties, and chooses a storm in the browser. (`artifacts/swmm5-lego/src/components/SWMM5LegoBuilder.jsx`)
- The app reads SWMM `.INP` and `.TXT` files and model `.JSON` files. (`artifacts/swmm5-lego/src/components/SWMM5LegoBuilder.jsx:753-760`; `artifacts/swmm5-lego/src/lib/importInp.js:3-22`; `artifacts/swmm5-lego/src/lib/persistence.js:192-205`)
- It downloads SWMM `.INP`, model `.JSON`, results `.CSV`, a standalone `.HTML` graph report, and the EPA engine's `.RPT` report. The binary `.OUT` file is parsed in memory. (`artifacts/swmm5-lego/src/lib/exportInp.js:5-20`; `artifacts/swmm5-lego/src/lib/persistence.js:179-189`; `artifacts/swmm5-lego/src/lib/exportCsv.js:1-49`; `artifacts/swmm5-lego/src/lib/exportHtmlReport.js:1-20`; `artifacts/swmm5-lego/src/components/SWMM5LegoBuilder.jsx:1528-1535`; `artifacts/swmm5-lego/src/lib/swmmWasm.js:63-72`)
- Autosaves and named model slots are stored in browser `localStorage`; the app does not need a database for model persistence. The source limits named slots to 5. (`artifacts/swmm5-lego/src/lib/persistence.js:1-4,84-103,142-169`)
- The editor supports US customary units and SI. US customary units include feet, acres, inches per hour, and cubic feet per second; SI includes meters, hectares, millimeters per hour, and cubic meters per second. (`artifacts/swmm5-lego/src/lib/units.js:1-16`)
- The separate Express API service exposes `GET /api/healthz`; it returns `{"status":"ok"}` when healthy. No model API route is present in the inspected route files. (`artifacts/api-server/src/app.ts:11`; `artifacts/api-server/src/routes/health.ts:6-9`)
- The app loads fonts from Google Fonts. (`artifacts/swmm5-lego/index.html:8-10`; `artifacts/swmm5-lego/src/components/SWMM5LegoBuilder.jsx:521`)

## Contents

- 1 main React app entry renders the SWMM5 builder. (`artifacts/swmm5-lego/src/App.tsx:3-5`)
- 54 built-in storm profiles, including 5 marked continuous; counted from the exported `STORMS` array in the current source. (`artifacts/swmm5-lego/src/lib/storms.js:32-137`; counted by importing the array during this run)
- 13 demo models; counted from the exported `DEMOS` array in the current source. (`artifacts/swmm5-lego/src/lib/demos.js:5-365`; counted by importing the array during this run)
- 1 API route, the health check; counted from the inspected router and handler. (`artifacts/api-server/src/routes/index.ts:1-8`; `artifacts/api-server/src/routes/health.ts:1-11`)
- 6 unit-test files; the current test run reports 79 passing tests. (`artifacts/swmm5-lego/src/__tests__/`; test command below)

## Checks

- Tests: 79 passed, 0 failed. Command: `pnpm --filter @workspace/swmm5-lego test`.
- Main app page `/`: loaded in the preview. The initial tutorial screen appeared. Browser logs contained Vite connection and React DevTools informational messages, with no browser errors.
- API health route `/api/healthz`: returned HTTP 200 and `{"status":"ok"}`.
- Human review: none recorded.

## What this does not show

1. The Quick Sim is an approximation. This run did not compare its results against EPA SWMM5 or an independently validated model.
2. The EPA SWMM5 binary's upstream commit and license are not recorded in the checked-in project documentation or source. Emscripten and Google Fonts license terms were not checked.
3. The tests and page load did not run an end-to-end simulation or exercise file import, export, save, or load in the browser.
4. Only the app's initial tutorial screen was visually loaded. Other interactive states and mobile layouts were not checked.
5. The project declares MIT in the root `package.json`, but no project license file was found. The core installed package manifests list React 19.1.0 (MIT), Recharts 2.15.4 (MIT), Vite 7.3.1 (MIT), Vitest 4.1.1 (MIT), and TypeScript 5.9.3 (Apache-2.0). A complete third-party and transitive license inventory was not checked.
6. No project source or documentation checked here records which AI tools built the app or what work Robert Dickinson personally performed. The ten newest Git log entries credit the `robertdickinson` account, but do not specify personal contributions.

## How to reproduce

- Run the web app: `pnpm --filter @workspace/swmm5-lego run dev`
- Run the tests: `pnpm --filter @workspace/swmm5-lego test`
- Run the API service: `pnpm --filter @workspace/api-server run dev`

## Credits and licenses

- Robert Dickinson: the ten newest Git log entries are credited to the `robertdickinson` account. The log does not describe his individual contributions.
- SWMM5 Lego Model project: MIT is declared in the root `package.json`.
- EPA SWMM5 5.2.4: the handover document points to OpenWaterAnalytics' Stormwater-Management-Model repository. The bundled binary's specific license and commit are not stated in the checked project files.
- React 19.1.0, Recharts 2.15.4, Vite 7.3.1, and Vitest 4.1.1: MIT, according to their installed package manifests.
- TypeScript 5.9.3: Apache-2.0, according to its installed package manifest.
- Google Fonts: Inter, Fredoka, and Nunito are referenced by the app. Their specific license terms were not checked.

## AI use

No project source or documentation checked for this summary names an AI tool used to build the app. Git history credits the `robertdickinson` account for the recent changes, but does not state what Robert Dickinson personally did. The project does not record other AI use.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-03-25: Published your App
- 2026-03-25: Improve model import and export functionality and add user feedback
- 2026-03-25: Enhance model building and testing capabilities with new features and improvements
- 2026-03-22: Add water quality modeling and continuous simulation capabilities
- 2026-03-22: Add a detailed technical handover document for the SWMM5 Lego Builder application
- 2026-03-22: Published your App
- 2026-03-22: Add ability to parse and display detailed simulation results from binary output files
- 2026-03-22: Published your App
- 2026-03-22: Add downloadable HTML report with simulation graphs and statistics
- 2026-03-22: Published your App
