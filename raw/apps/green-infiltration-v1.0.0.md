---
name: Green-Ampt Infiltration Calculator
file: green-infiltration
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://green-infiltration--robertdickinson.replit.app, repo: none}
engines: none
stack: TypeScript 5.6.3, React 19.2, Vite 7.1, Express 4.21, Wouter 3.3, Recharts 2.15, Tailwind CSS 4, TanStack Query 5, Drizzle ORM 0.39, PostgreSQL client pg 8.16, Replit hosting, Google Fonts
units: both
ai_use: No AI tool used to build the app is identified in the inspected project records; details below.
---

# Green-Ampt Infiltration Calculator: estimates infiltration and runoff

## What it does

The app calculates infiltration estimates from user-entered soil, rainfall, and storm-duration parameters. It offers Green-Ampt, Modified Green-Ampt, Horton, and SCS Curve Number methods, plus charts, summary values, and a water-balance display where supported (`client/src/pages/green-ampt.tsx:163-209, 321-420, 1937-1995`). Users can compare scenarios and save parameter presets in their browser (`client/src/pages/green-ampt.tsx:530-579`). The app describes its methods as SWMM5 methods, but the calculations run in the app's own TypeScript code rather than an invoked SWMM engine (`client/src/pages/green-ampt.tsx:321-420`; `server/routes.ts:5-15`).

## How it computes

All four methods run in `calculateInfiltration` in `client/src/pages/green-ampt.tsx`, using a default timestep of `0.1` hours (`:321`).

- Green-Ampt: starts cumulative infiltration `F` at `0.001`, calculates capacity as `f = K * (1 + suctionHead * initialDeficit / F)`, limits actual infiltration to rainfall when rainfall is present, and accumulates excess rainfall as runoff (`:327-355`).
- Modified Green-Ampt: adjusts the moisture deficit by `effectiveDeficit = initialDeficit * (1 - exp(-time / max(redistributionTime, 0.1)) * 0.3)`, applies the Green-Ampt capacity equation, then calculates rainfall-limited infiltration and runoff (`:356-386`).
- Horton: calculates `f = minRate + (maxRate - minRate) * exp(-decayConstant * time)` and sums `f * timestep` for cumulative infiltration (`:387-395`).
- SCS Curve Number: calculates `S = 1000 / CN - 10`, `Ia = initialAbstraction * S`, cumulative rainfall `P`, runoff `Q = (P - Ia)^2 / (P - Ia + S)` when `P > Ia`, and infiltration `F = P - Q` (`:396-416`).

Green-Ampt and Modified Green-Ampt get rainfall intensity from `getRainfallAtTime`, which contains the selectable distribution profiles (`:423-490`). Outputs are formatted for the selected unit system in the page; conversion factors and labels are defined at `:220-234`.

## Inputs and outputs

- Inputs are entered in the browser: duration and method-specific parameters for soil, rainfall, and runoff. The page does not read input files (`client/src/pages/green-ampt.tsx:881-1140`).
- The main client route is `/`. It serves the calculator and its documentation tab. There are no application API endpoints in `server/routes.ts` (`client/src/App.tsx:9-14`; `server/routes.ts:5-15`).
- Outputs include infiltration charts, calculation tables, summaries, and a mass-balance table (`client/src/pages/green-ampt.tsx:1717-1790, 1937-1995`).
- CSV data and text reports are copied to the browser clipboard; chart images are downloaded as PNG; printing uses the browser print dialog (`client/src/pages/green-ampt.tsx:648-720, 828-836, 703-705`).
- Saved presets are stored in browser `localStorage` under `infiltration-calculator-presets` (`client/src/pages/green-ampt.tsx:218, 519-560`). Calculations run client-side. The server's storage implementation is in-memory and is not used by the calculator (`server/storage.ts:13-38`).
- No user-uploaded files or persistent calculation records are stored by the app. PostgreSQL and Drizzle packages are present, but the calculator does not use a database (`package.json:14-110`; `server/routes.ts:5-15`).

## Contents

- Main route: 1 (`/`), with Calculator and Docs views; an unmatched path renders a not-found page (`client/src/App.tsx:9-14`; `client/src/pages/green-ampt.tsx:1201-1218, 1261-1269`).
- Infiltration methods: 4 (`client/src/pages/green-ampt.tsx:163, 296-301`).
- Built-in scenarios: 8 (`client/src/pages/green-ampt.tsx:246-287`).
- Soil presets: 6 (`client/src/pages/green-ampt.tsx:237-244`).
- Rainfall distributions: 13 (`client/src/pages/green-ampt.tsx:172, 423-490`; selectable options at `:964-978`).
- Database records or question sets used by the calculator: none found (`server/routes.ts:5-15`; `client/src/pages/green-ampt.tsx`).

## Checks

- `npm run check`: passed. This runs the TypeScript compiler (`package.json:11`).
- `npm test`: unavailable. The command exited with “Missing script: test”; 0 tests ran, 0 passed, and 0 failed (`package.json:6-12`; command run on 2026-11-15).
- Main page `/`: local request returned HTTP 200. The published page loaded at `https://green-infiltration--robertdickinson.replit.app` on 2026-11-15. The local browser capture showed no browser errors; it logged an informational React DevTools message. The workflow log showed the server listening on port 5000.
- Human review: none recorded in the inspected project files or Git history.

## What this does not show

1. The package version is `1.0.0` (`package.json:1-5`), but the project does not record when that version was assigned. The front-matter date is the inspection date, 2026-11-15, not a verified release date.
2. The metric selector changes unit labels and some displayed outputs, but Green-Ampt and Horton inputs are bound directly to stored numeric values. The input values are not converted when the unit selection changes (`client/src/pages/green-ampt.tsx:220-234, 509, 881-952, 1055-1104`). Metric-mode input correctness was not checked.
3. The Modified Green-Ampt branch records cumulative infiltration before adding that timestep's infiltration (`client/src/pages/green-ampt.tsx:374-384`). Its reported cumulative series may lag the calculation by one timestep; this was not independently tested.
4. The simulation loops include the duration boundary and add a full timestep in each iteration (`client/src/pages/green-ampt.tsx:331-354, 360-385, 390-395, 402-414`). Boundary behavior was not independently tested.
5. The Curve Number branch calculates rainfall from `params.rainfall`, but does not add it to `cumulativeRainfall`; the returned `totalRainfall` is taken from that separate accumulator (`client/src/pages/green-ampt.tsx:321-325, 396-420`). The effect on all displayed outputs was not tested.
6. Horton inputs contain no rainfall parameter, and its calculation writes zero runoff (`client/src/pages/green-ampt.tsx:195-200, 387-395`). Rainfall-coupled Horton behavior is not shown.
7. Interactive controls, the Docs tab, exports, printing, preset persistence, and comparison scenarios were not exercised in this check. Only the initial main page view and page load were checked.
8. A test suite was not run because the project has no `test` script. Production build behavior and numerical agreement with EPA SWMM were not checked. The app's documentation cites SWMM5 references, but no SWMM engine is invoked (`client/src/pages/green-ampt.tsx:1275-1281`; `server/routes.ts:5-15`).
9. The inspected project records do not document who reviewed the app or which AI tools built it. The Google Fonts font licenses were not checked.

## How to reproduce

- Start the development app: `npm run dev` (`package.json:6-12`).
- Run the available type check: `npm run check` (`package.json:11`).
- Run tests: no test command is configured (`package.json:6-12`).
- Build for deployment: `npm run build`; start the production server with `npm start` (`package.json:9-10`). These commands were not run for this summary.

## Credits and licenses

- Author: Robert Dickinson, as specified for this summary. The inspected Git history records `robertdickinson` as author of the most recent commits.
- Project license: MIT, declared in `package.json:5`. No standalone license file was found.
- Selected application libraries and licenses from their installed package manifests: React (MIT), TypeScript (Apache-2.0), Vite (MIT), Express (MIT), Wouter (Unlicense), TanStack Query (MIT), Recharts (MIT), Tailwind CSS (MIT), Drizzle ORM (Apache-2.0), `pg` (MIT), Lucide React (ISC), and html2canvas (MIT).
- The app's documentation cites Green and Ampt, Horton, USDA Soil Conservation Service, Huff, Rossman, Huber, Rawls, Brakensiek, and Miller (`client/src/pages/green-ampt.tsx:1452-1470`). These are listed as method references, not as software engines.
- Inter and JetBrains Mono are requested from Google Fonts (`client/index.html:18-20`). Their font licenses were not checked.

## AI use

The inspected source, project documentation, and Git history do not identify an AI tool that built the app. The most recent Git entries attribute work to `robertdickinson`; they do not specify which tools were used or the author's full contribution. The project does not record a human technical review.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

The following are the 10 newest entries from `git log -10 --date=short --pretty=format:'%ad %s'`, read on 2026-11-15:

- 2026-01-21: Published your App
- 2026-01-21: Make the method reference section collapsible for better user experience
- 2026-01-21: Improve chart readability by capping infiltration rates and adjusting axis scaling
- 2026-01-21: Saved progress at the end of the loop
- 2026-01-21: Add functionality to generate and copy detailed analysis reports
- 2026-01-21: Published your App
- 2026-01-21: Saved progress at the end of the loop
- 2026-01-21: Add example scenarios to the infiltration model interface
- 2026-01-21: Published your App
- 2026-01-21: Add continuity error percentage to mass balance table
