---
name: SWMM5 Modeler
file: mirofish-swmm # Taken from the current deployed URL.
version: "0.0.0" # artifacts/swmm5-modeler/package.json:3
date: 2026-11-15 # Current date; used as the summary date.
author: Robert Dickinson
links: {replit: "https://mirofish-swmm.replit.app", repo: none}
engines:
  - {name: EPA SWMM5, version: "5.1.14", source: Open Water Analytics, commit: "7e7e6da", license: not stated in repository}
stack: TypeScript, React, Vite, Tailwind CSS, Express, PostgreSQL, Drizzle ORM, SWMM5 compiled to WebAssembly, Replit hosting
units: both
ai_use: Engineering findings use hard-coded rules; no external LLM calls were found.
---

# SWMM5 Modeler: builds and analyzes stormwater drainage networks

## What it does

The app lets stormwater engineers create or import drainage networks and inspect simulated runoff, node depth, conduit flow, flooding, errors, and model grades. It can generate a network from parameters, scale up an existing network, or parse a SWMM `.inp` file. Results include charts, an EPA SWMM-style report, proposed model fixes, and calibration data downloads. The app has dashboard, editor, agents, and results routes (`artifacts/swmm5-modeler/src/App.tsx:22-30`).

## How it computes

- `generateModel`, `scaleUpModel`, and `parseInpFile` create, replicate, or parse network data (`artifacts/swmm5-modeler/src/lib/model-generator.ts:31,207,366`).
- `runSwmmWasm` passes an input file to EPA SWMM5 compiled to WebAssembly. It calls `swmm_run`, reads the generated report, and parses summary tables and per-element time series (`artifacts/api-server/src/lib/swmm-wasm-runner.ts:428-437,479-534`).
- For imported USER1 projects, the server supplies the original `.inp` content. Other projects are converted from stored model data to `.inp` text (`artifacts/api-server/src/routes/projects.ts:27-32,153-160,175-183`; `artifacts/api-server/src/lib/swmm-wasm-runner.ts:431-438`).
- If the engine fails, the API uses `runSwmmSimulation`. Its runoff estimate uses `C = 0.3 + 0.6 × imperviousPercent / 100` and `Q = C × rainfallIntensity × area`. Its circular-conduit flow uses `Q = (1.49 / n) × area × hydraulicRadius^(2/3) × sqrt(slope / 100)` (`artifacts/api-server/src/lib/swmm-simulator.ts:146-159`). These formulas belong to the simplified fallback, not the SWMM engine.
- When a parsed per-element time series is missing, the WASM runner also creates a synthetic series: a quadratic rise to a peak, exponential recession, and random variation (`artifacts/api-server/src/lib/swmm-wasm-runner.ts:264-280,542-582`).
- `detectModelErrors`, `generateAutoFixes`, and `gradeModelResults` check connectivity and hydraulic conditions, propose selected repairs, and score model results (`artifacts/api-server/src/lib/report-generator.ts:296,502,660`; `artifacts/api-server/src/routes/projects.ts:184-186`).
- `generateSwarmPrediction` applies fixed thresholds and estimates for runoff, capacity, flooding, water quality, climate, and infrastructure. The six displayed agents are code-defined specialists; the source does not call an external language model (`artifacts/swmm5-modeler/src/lib/agents.ts:14-87,114-126,141-176,180-220,232-270`).

## Inputs and outputs

- Reads EPA SWMM `.inp` text through `parseInpFile`; creates generated or scaled model data in the editor (`artifacts/swmm5-modeler/src/lib/model-generator.ts:31,207,366`).
- Project records store a name, description, model JSON, and timestamps in PostgreSQL (`lib/db/src/schema/projects.ts:5-11`).
- API routes include `GET` and `POST /api/projects`; `GET`, `PUT`, and `DELETE /api/projects/:id`; `POST /api/projects/:id/simulate`, `/analyze`, `/fix`, `/calibration`, and `/calibration/preview`; `GET /api/projects/:id/export`; and `GET /api/healthz` (`artifacts/api-server/src/routes/projects.ts:34-127,130-215,217-260,262-346,348-371`; `artifacts/api-server/src/routes/health.ts`).
- Simulation and analysis return JSON. Analysis also returns report text, errors, a grade, and proposed fixes. Export downloads `.inp` text. Calibration export downloads a ZIP containing `.dat` files (`artifacts/api-server/src/routes/projects.ts:168-215,262-297,348-370`; `artifacts/api-server/src/lib/calibration-export.ts:303-440`).

## Contents

- The app defines four main page routes (`artifacts/swmm5-modeler/src/App.tsx:22-30`).
- The current development API returned two project records: `USER1 - Test Problem` and `Test Generated Network` (`GET /api/projects`, run on 2026-11-15).
- The USER1 model in the current API response has 58 subcatchments, 59 junctions, one outfall, 59 conduits, and one raingage (`GET /api/projects/4`, run on 2026-11-15). The same counts were read from the input file sections at `artifacts/api-server/src/data/user1.inp:51-371`.
- The analysis run returned 60 node results, 59 link results, and 58 subcatchment results. The first result series in each group contained 420 points (`POST /api/projects/4/analyze`, run on 2026-11-15).
- The code defines six specialist agents (`artifacts/swmm5-modeler/src/lib/agents.ts:14-87`).

## Checks

- `pnpm run typecheck` failed. The API package reported missing `x` and `y` properties in `swmm-simulator.ts` and a `ModelData` type conversion error in `routes/projects.ts` (`artifacts/api-server/src/lib/swmm-simulator.ts:420,423,427`; `artifacts/api-server/src/routes/projects.ts:233`).
- `pnpm --filter @workspace/swmm5-modeler run typecheck` failed with 14 TypeScript errors across eight files. Errors include unresolved generated schema imports and query option type errors (command output from the run on 2026-11-15).
- No automated test script or project test files were found. Automated test cases run: 0 passed, 0 failed. No test command is configured (`package.json:5-10`; frontend and API scripts in their package manifests).
- `GET /api/healthz`, `GET /api/projects`, and `GET /api/projects/4` returned HTTP 200. `POST /api/projects/4/analyze` returned HTTP 200, completed with EPA SWMM5 v5.1.14 (WASM), and returned the counts above (runs on 2026-11-15).
- The dashboard, editor, agents, and results routes loaded in the browser. The dashboard logged a missing favicon; `GET /favicon.ico` returned HTTP 404. No browser errors were reported on the other three pages (browser checks on 2026-11-15).
- Human review: none recorded in the project.

## What this does not show

1. The USER1 project description says it has 22 subcatchments, while the stored model and `.inp` file each contain 58. This discrepancy was not resolved (`GET /api/projects/4`, run on 2026-11-15; `artifacts/api-server/src/data/user1.inp:56-116`).
2. The sample `.inp` declares CMS units, while the results UI labels peak runoff in CFS. Unit conversions and labels were not audited end to end (`artifacts/api-server/src/data/user1.inp:7`; `artifacts/swmm5-modeler/src/pages/Results.tsx:316`).
3. Import, generation, scale-up, save, auto-fix, and calibration interactions were not individually exercised. The page checks only confirmed that the main routes loaded.
4. The app can fall back to simplified calculations if WASM fails and to generated time series when parsed series are absent. These fallbacks are not equivalent to EPA SWMM output (`artifacts/api-server/src/routes/projects.ts:155-165,197-214`; `artifacts/api-server/src/lib/swmm-wasm-runner.ts:542-582`).
5. Engineering accuracy has not been independently validated. No human review is recorded.
6. The dashboard's missing favicon response was not fixed or investigated further (`GET /favicon.ico`, run on 2026-11-15).
7. Typechecking is currently failing, as described under Checks. Automated tests are not configured.
8. The published production pages were not checked; browser checks used the running development preview.

## How to reproduce

- Start the API: `pnpm --filter @workspace/api-server run dev` (`artifacts/api-server/.replit-artifact/artifact.toml:7-13`).
- Start the web app: `pnpm --filter @workspace/swmm5-modeler run dev` (`artifacts/swmm5-modeler/.replit-artifact/artifact.toml:12-19`).
- Run the configured typecheck: `pnpm run typecheck` (`package.json:5-10`). No automated test command is configured.

## Credits and licenses

- Project license: MIT, as declared in the root package manifest (`package.json:1-4`).
- EPA SWMM5 source headers name L. Rossman and the U.S. EPA. Build metadata names Open Water Analytics and records version 5.1.14 and commit `7e7e6da` (`lib/swmm-wasm/src/solver/swmm5.c:1-12`; `lib/swmm-wasm/src/solver/version.h:4-16`). No SWMM engine license file or license statement was found in this repository.
- MiroFish is named as inspiration for the multi-agent concept (`replit.md:40-64`). Its license is not recorded here.
- Key package licenses, checked from installed package metadata: React, React DOM, React Query, Express, `pg`, Zod, Recharts, Radix UI, Framer Motion, Tailwind CSS, and most listed UI packages use MIT; Drizzle ORM, drizzle-zod, and class-variance-authority use Apache-2.0; lucide-react uses ISC; Wouter uses Unlicense. Package names are declared in `artifacts/swmm5-modeler/package.json:12-66`, `artifacts/api-server/package.json:11-19`, and `lib/db/package.json:14-19`. This is not a complete transitive dependency inventory.

## AI use

- Replit Agent is not named as a builder in the project source or documentation. Git history has an initial commit by `agent`, but does not identify a tool or map its work to features. No other AI tool or external language-model API is named in the source.
- The app's specialist-agent findings are generated by code-defined rules and estimates (`artifacts/swmm5-modeler/src/lib/agents.ts:114-126,141-176,209-270`).
- Git history attributes the later feature commits to Robert Dickinson. Those commits cover the modeler, multi-agent analysis, grading and fixes, the USER1 sample, and SWMM5 WASM integration (`git log`, 2026-03-12 through 2026-03-14).
- This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-03-14: Integrated the EPA SWMM5 WebAssembly engine (`git log`).
- 2026-03-14: Added the USER1 SWMM5 model as the default project (`git log`).
- 2026-03-14: Added analysis, auto-fixing, and model grading (`git log`).
- 2026-03-14: Published the app (`git log`).
- 2026-03-13: Added the multi-agent prediction engine (`git log`).
- 2026-03-13: Added the SWMM5 modeler with project management and simulation (`git log`).
- 2026-03-12: Created the initial project commit (`git log`).
