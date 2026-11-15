---
name: SWMM5 Topology Sandbox
file: fractal-swmm-gen--robertdickinson
version: 1.0.0
date: 2026-01-19
author: Robert Dickinson
links: {replit: https://fractal-swmm-gen--robertdickinson.replit.app, repo: none}
engines: none
stack: TypeScript, React 18 (package.json:62-64), Express 5 (package.json:52), Vite 7 (package.json:101), Tailwind CSS 3 (package.json:98), Drizzle ORM (package.json:49), PostgreSQL configured but not used by active storage (server/storage.ts:14-21), Google Fonts (client/index.html:12-14), Replit deployment (.replit:15-18)
units: US customary (client/src/components/NetworkMetrics.tsx:61-75)
ai_use: Project records do not identify AI contributions; see AI use.
---

# SWMM5 Topology Sandbox: Explore drainage network geometry

## What it does

The app lets learners explore how stormwater network layouts differ. Users select a network pattern and hydraulic parameters, then view the generated nodes, links, and subcatchments on an interactive canvas. The app shows topology-based hydrograph estimates and exports a SWMM5-format INP file or network statistics as CSV. It is an educational sandbox, not a hydraulic simulation engine.

## How it computes

- `generateFractalNetwork` in `client/src/lib/fractal.ts` selects a pattern-specific generator and returns nodes, links, and subcatchments. The pattern enum contains 22 choices (`shared/schema.ts:6-33`).
- `applyHydraulicParameters` in `client/src/lib/fractal.ts` adds random variation to imperviousness, slope, and area. The formulas are `base + (random - 0.5) * 20`, `base + (random - 0.5)`, and `base + (random - 0.5) * baseArea * 0.5`. Link diameter is scaled from its normalized generated size, and roughness is set from the configured value (`client/src/lib/fractal.ts:3599-3638`).
- `generateHydrographData` in `client/src/components/SimulationPanel.tsx` uses topology-specific parameters to form a rising power curve and an exponential recession curve (`client/src/components/SimulationPanel.tsx:14-84`). `getHydrographParams` and `generateHydrographCurve` in `client/src/components/HydrographComparisonPanel.tsx` create similar comparison curves (`client/src/components/HydrographComparisonPanel.tsx:35-80`).
- These charts are theoretical estimates. The interface labels them educational and says to export the INP file for real EPA SWMM5 simulation (`client/src/components/SimulationPanel.tsx:251-261`).
- The client-side `runSimulation` produces an estimate from node count, link count, and topology, with random flooded-node output. The server `POST /api/networks/:id/simulate` route also creates random result values after a delay. Neither calls an external hydraulic engine (`client/src/components/SimulationPanel.tsx:174-227`; `server/routes.ts:77-108`).
- `generateINPFile` formats network data as an INP text file (`client/src/lib/inp-generator.ts:3-327`; `server/inp-generator.ts:3-260`). `NetworkMetrics` sums link lengths and subcatchment areas and averages imperviousness and pipe size for display and CSV export (`client/src/components/NetworkMetrics.tsx:19-30,78-130`).

## Inputs and outputs

- Inputs are UI configuration values for pattern, iterations, node and subcatchment counts, link type, branching, scale, spread angle, imperviousness, slope, area, pipe diameter, and roughness (`shared/schema.ts:82-96`; `client/src/components/ConfigPanel.tsx:185-203`).
- The browser generates networks into React state. The theme preference is stored in browser `localStorage` (`client/src/pages/Home.tsx:24-55`; `client/src/components/ThemeToggle.tsx:13-26`).
- The browser downloads `.inp` and `.csv` files. INP contents can also be previewed or copied to the clipboard (`client/src/components/ExportPanel.tsx:32-66,112-189`; `client/src/components/NetworkMetrics.tsx:78-135`).
- The server exposes JSON API routes for listing, reading, creating, and deleting networks; downloading INP; starting and reading simulation results; and generating INP from submitted network data (`server/routes.ts:13-156`).
- Server-side network and simulation records are held in process memory maps and are not written to PostgreSQL (`server/storage.ts:14-21,33-68,71`). The Replit configuration includes PostgreSQL and Drizzle setup, but the active storage implementation is `MemStorage` (`.replit:1`; `drizzle.config.ts:7-13`; `server/storage.ts:14-21`).

## Contents

- Browser route cases: 2, the home page and the not-found page (`client/src/App.tsx:9-15`).
- Network pattern choices: 22 (`shared/schema.ts:6-33`).
- Link types: 5 (`shared/schema.ts:3`).
- API route handlers: 8 (`server/routes.ts:13-156`).
- Initial development API data: 0 saved networks observed in the current run (`GET /api/networks` returned `[]`).
- Package version: 1.0.0 (`package.json:3`). Git first recorded `package.json` on 2026-01-19 (`git log --follow --date=short -- package.json`); that date is used in the front matter.

## Checks

- `npm run check`: passed. This runs TypeScript (`package.json:6-10`).
- `npm test`: no test script is configured (`package.json:6-11`). The command reported a missing script; 0 tests ran, 0 passed, and 0 failed.
- `npm run build`: passed. The build reported a stale Browserslist database, a PostCSS warning, and a client bundle-size warning above 500 kB (build run: `npm run build`).
- Development page `/`: HTTP 200 and rendered. Browser logs showed Vite connecting and an informational React DevTools message, with no reported browser errors (development run and screenshot).
- Unmatched development path: the server returned the app shell with HTTP 200, and the client rendered its expected 404 page. Browser logs showed no reported browser errors (development run and screenshot; `client/src/App.tsx:11-14`; `client/src/pages/not-found.tsx:4-16`).
- Human review: none recorded in project files.

## What this does not show

1. No SWMM engine was run against an exported INP file. Compatibility with an actual SWMM run was not checked.
2. The hydrograph charts and simulation results are estimates, not outputs from hydraulic calculations (`client/src/components/SimulationPanel.tsx:14-84,174-227`; `server/routes.ts:77-108`).
3. No automated test suite is configured. `npm test` could not execute tests (`package.json:6-11`; command run above).
4. Only the development home page and not-found route were loaded. Other interactions, API error cases, and the production page were not checked.
5. Mobile layout, accessibility, and performance were not comprehensively tested. The build did report a client bundle larger than 500 kB (build run: `npm run build`).
6. Server-side records are in memory; persistence across a server restart was not checked (`server/storage.ts:14-21`).
7. No human review is recorded in the project.
8. Git remote configuration did not provide a GitHub repository URL. The individual licenses of every dependency were not audited.

## How to reproduce

- Install dependencies with `npm install`.
- Start the development app with `npm run dev` (`package.json:6-9`; `.replit:1-2`).
- Run the TypeScript check with `npm run check` (`package.json:10`).
- Build production files with `npm run build` and run them with `npm start` (`package.json:8-10`).
- No test command is configured (`package.json:6-11`).

## Credits and licenses

- Author: Robert Dickinson.
- Project license: MIT (`package.json:5`).
- Checked dependency licenses: React, Express, Vite, Tailwind CSS, Zod, TanStack Query, and Radix UI Accordion use MIT; Drizzle ORM uses Apache-2.0; Lucide React uses ISC; Wouter uses Unlicense (installed package metadata).
- EPA SWMM is linked as a reference (`client/src/App.tsx:85-90`). This project does not state a license for EPA SWMM.

## AI use

The reviewed project files and Git history do not identify AI tools used to build the app or record which work Robert Dickinson completed. The Git history lists project changes but does not provide that attribution.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: the 10 newest entries from `git log --date=short`.

- 2026-07-22: Published your App
- 2026-07-22: Published your App
- 2026-07-22: Published your App
- 2026-02-04: Saved progress at the end of the loop
- 2026-02-04: Add ability to toggle node labels and improve presets with icons
- 2026-02-04: Add suggestions for improving the fractal network generation tool
- 2026-02-04: Published your App
- 2026-02-04: Published your App
- 2026-02-04: Saved progress at the end of the loop
- 2026-02-04: Add stream order calculation and CSV export for network statistics
