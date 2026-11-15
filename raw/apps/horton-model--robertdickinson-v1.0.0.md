---
name: SWMM5 Runoff and Infiltration App
file: horton-model--robertdickinson
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: "https://horton-model--robertdickinson.replit.app", repo: none}
engines: none
stack: TypeScript, React, Vite, Express, Wouter, Recharts, Tailwind CSS, Drizzle ORM, PostgreSQL configuration, Open-Meteo, Google Fonts
units: both
ai_use: App development AI use is not recorded in the project; this summary was written by Replit Agent.
---

# SWMM5 Runoff and Infiltration App: interactive stormwater infiltration modeling

## What it does

The app lets users explore infiltration and surface runoff for storms using Horton, modified Horton, Green-Ampt, modified Green-Ampt, and SCS Curve Number calculations (`client/src/pages/home.tsx:62,1036-1118`). Users adjust soil, rainfall, watershed, and Low Impact Development (LID) parameters, then view time series, runoff summaries, and water-balance values (`client/src/pages/home.tsx:83-206,444-505,1851-1874,4232-4310`). The app can fetch historical precipitation from Open-Meteo and turn detected events into storm inputs (`client/src/pages/home.tsx:729-829`). It exports results and model data, including SWMM `.INP` text, but does not call an EPA SWMM simulation engine (`client/src/pages/home.tsx:1259-1312,1314-1592`).

## How it computes

- The Horton calculation advances in 0.1-hour increments. During rain, infiltration capacity decays exponentially toward `fc`; during dry periods, it recovers toward `f0`. Actual infiltration is the lesser of capacity and rainfall, and runoff is the nonnegative difference (`calculateSWMM5Horton`, `client/src/pages/home.tsx:1036-1098`).
- Modified Horton additionally scales capacity by remaining `Fmax` storage and reduces accumulated infiltration during dry periods using a fixed evapotranspiration rate (`client/src/pages/home.tsx:1050-1065`).
- Green-Ampt uses `f = Ks * (1 + psi * thetaD / F)` and a constant rainfall intensity over a six-hour calculation, with a 0.1-hour step. The modified variant adjusts effective cumulative infiltration with a redistribution factor and limits capacity at its configured storage (`calculateGreenAmpt` and `calculateModifiedGreenAmpt`, `client/src/pages/home.tsx:846-974`).
- The Curve Number method computes `S = 1000 / CN - 10`, `Ia = 0.2 * S`, then `Q = (P - Ia)^2 / (P - Ia + S)` when cumulative rainfall exceeds initial abstraction. Rainfall is distributed in a triangle across the selected duration, and changes in cumulative runoff produce runoff rates (`calculateCurveNumber`, `client/src/pages/home.tsx:976-1034`).
- The engineering summary sums precipitation, infiltration, and runoff. It converts peak runoff to CFS and total runoff to acre-feet using watershed area; the source labels the peak-flow conversion a rational-method approximation (`client/src/pages/home.tsx:1851-1874`).

## Inputs and outputs

- Inputs are entered through the browser interface. The app requests geocoding and hourly historical precipitation as JSON from Open-Meteo (`client/src/pages/home.tsx:729-829`).
- The client has no file-upload or file-reading handler. It creates browser downloads for result CSV, parameter CSV, field-test JSON, PDF, SWMM `.INP`, and LandXML XML files (`client/src/pages/home.tsx:720-727,1259-1312,1314-1592,1594-1708,1710-1845`).
- The client route is `/`; other paths use the not-found page (`client/src/App.tsx:9-14`). The Express route registration adds no API endpoints (`server/routes.ts:5-16`).
- Simulation parameters and results live in React component state. The server defines an in-memory user map and a Drizzle user schema, but the app routes do not connect them to the simulation (`client/src/pages/home.tsx:444-505`, `server/storage.ts:7-38`, `shared/schema.ts:6-18`, `server/routes.ts:5-16`).

## Contents

- One client page route, `/`, plus a not-found fallback (`client/src/App.tsx:9-14`).
- Five infiltration model choices (`client/src/pages/home.tsx:62`).
- Five built-in storm scenarios (`client/src/pages/home.tsx:273-348`).
- Five Horton soil presets, six Green-Ampt soil presets, seven Curve Number land-use presets, and four subcatchment presets (`client/src/pages/home.tsx:44-81`).
- Eight LID control types (`client/src/pages/home.tsx:83-84`).

## Checks

- `npm test`: no test script is configured. No tests ran, so 0 passed and 0 failed (`package.json:6-13`; command run on 2026-11-15).
- `npm run check`: passed. This runs the TypeScript compiler (`package.json:11`; command run on 2026-11-15).
- Browser check: `/` rendered. The browser log contained Vite connection and React DevTools informational messages, with no errors.
- Browser check: an unknown path rendered the not-found page. The browser log contained the same informational messages, with no errors.
- Human review: none recorded.

## What this does not show

1. The live deployment UI was not loaded. Deployment metadata confirms the public URL, but the browser checks used the development preview.
2. No EPA SWMM engine was run. Importing the generated `.INP` file into EPA SWMM was not checked.
3. Simulation outputs were not compared against independent engineering calculations or reference cases.
4. Generated CSV, PDF, JSON, XML, and `.INP` downloads were not opened in other applications.
5. The production build command was not run, and the project has no configured automated test suite.
6. Open-Meteo response behavior and Google Fonts availability were not tested beyond reading their source references.
7. The project files do not record prior human review or which AI tools, if any, were used to build the app.
8. The remote Git URL is an internal Replit GitHub host, not a public GitHub URL. No public repository URL is listed here.
9. Licenses for every package in the dependency manifest and for outside services were not audited.

## How to reproduce

- Install dependencies: `npm install`
- Start the development app: `npm run dev`
- Run the TypeScript check: `npm run check`
- Build for production: `npm run build`
- Automated tests: no `test` script is defined in `package.json`.

## Credits and licenses

- Author: Robert Dickinson.
- Project license: MIT, declared in `package.json:5`.
- Selected libraries and licenses from installed package metadata: React and React DOM, MIT (`node_modules/react/package.json:10`; `node_modules/react-dom/package.json:14`); Vite, Express, Tailwind CSS, Recharts, and jsPDF, MIT (`node_modules/vite/package.json:5`; `node_modules/express/package.json:15`; `node_modules/tailwindcss/package.json:5`; `node_modules/recharts/package.json:160`; `node_modules/jspdf/package.json:29`); Drizzle ORM and TypeScript, Apache-2.0 (`node_modules/drizzle-orm/package.json:43`; `node_modules/typescript/package.json:6`); Wouter, Unlicense (`node_modules/wouter/package.json:66`); Lucide React, ISC (`node_modules/lucide-react/package.json:5`).
- Outside service: Open-Meteo. The app requests its geocoding and archive APIs (`client/src/pages/home.tsx:741-759`).

## AI use

The project files do not identify AI tools used to build the app or record Robert Dickinson's implementation contributions. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

From `git log`, newest first:

- 2026-07-23: Published your App.
- 2026-07-23: Improved simulation export and playback timing accuracy.
- 2026-07-23: Published your App.
- 2026-02-05: Added real rainfall data import from weather services.
- 2026-02-05: Added mobile field mode for infiltration testing and parameter fitting.
- 2026-02-04: Added an animated soil cross-section.
- 2026-02-04: Added links to related hydrology tools.
- 2026-02-04: Added SI and US unit selection.
- 2026-02-04: Added color themes and theme selection.
- 2026-02-04: Published your App.
