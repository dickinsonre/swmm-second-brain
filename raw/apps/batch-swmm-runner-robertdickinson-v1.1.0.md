---
name: BatchSWMM56
file: batch-swmm-runner-robertdickinson
version: 1.1.0
date: 2026-09-12
author: Robert Dickinson
links: {replit: "https://batch-swmm-runner-robertdickinson.replit.app", repo: none}
engines:
  - {name: EPA SWMM native executable/API, version: 5.2.4, source: USEPA/Stormwater-Management-Model, commit: unknown, license: "EPA public-domain basis; bundled glibc notices"}
  - {name: SWMM5 WASM, version: 5.2.4, source: "vendored EPA source; exact archive provenance uncertain", commit: unknown, license: "EPA public-domain basis; full binary audit not established"}
  - {name: SWMM5 Extended, version: "5.2.4 KW/SF extension", source: "EPA plus supplied source patch", commit: "7952ca837988b1c32f791812eccc9fd64547e093 (base)", license: "modified binary license inventory incomplete"}
  - {name: OWA SWMM, version: "5.1 lineage; build unknown", source: OpenWaterAnalytics/Stormwater-Management-Model, commit: unknown, license: MIT}
  - {name: SWMM6 stable, version: 6.0.0-alpha.4, source: HydroCouple/openswmm.engine, commit: 9976efc815d5242e52a07a9d7c799e535b65fcaa, license: Apache-2.0}
  - {name: SWMM6 develop, version: 6.0.0-alpha.3, source: HydroCouple/openswmm.engine, commit: 19a1bc42074eac8cdf46e2edafe6fc5849adf6da, license: MIT}
  - {name: Hydra, version: 12.1.0, source: neeraip/hydra, commit: 2a75372531b981c3a8f6668cbb846a0366cf062d, license: AGPL-3.0}
stack: "TypeScript, JavaScript, C/C++, Rust engine artifacts, React, Vite, Tailwind CSS, Express, Node.js, Drizzle ORM, PostgreSQL, Neon driver, WebAssembly, Replit, GitHub, OpenAI"
units: both
ai_use: "OpenAI report assistant; implementation-tool attribution is not fully recorded"
---

# BatchSWMM56: Run drainage models and compare simulation results

## What it does
BatchSWMM56 runs SWMM input models individually or in batches for drainage modelers.
It compares engine status, continuity, flooding, flows, timing, and time series.
It provides QA/QC, coherence screening, and conduit discretization tools.
Outputs include result tables, plots, reports, modified inputs, and downloadable run artifacts.
Sources: `client/src/App.tsx:19-26`, `client/src/components/EngineComparisonView.tsx`, and `client/src/pages/ReswmmPage.tsx`.

## How it computes
- Input preparation: `shared/inpOptions.ts`, `resolveEngineOverrides` and `applyInpOverrides`, apply routing and simulation settings to model text.
- Experimental routing: `resolveEngineOverrides` applies the Extended-only routing choice without changing the other engines. Inherit preserves the shared or model setting.
- Native executable: `server/routes.ts`, `processSingleFile`, launches the engine and parses its report and output files.
- Native API: `server/routes.ts`, `processSingleFileApi`, calls `server/swmm5api.ts`, `runWithApi`, through Koffi.
- Browser execution: `client/src/lib/swmmWasmEngine.ts` dispatches work to workers. `client/public/wasm/swmm-worker.js` loads the selected module, opens the input, steps the solver, and reads outputs.
- Extended and Hydra use dedicated workers in `client/public/wasm-extended/` and `client/public/wasmhydra/`.
- Hydraulic calculations come from the chosen engine. Report parsing is not an independent hydraulic solution.
- Binary results: `server/swmmOutParser.ts`, `parseSwmmOutputBinary`, wraps the shared binary parser.
- Coherence screening: `client/src/lib/coherenceDiagnostic.ts`, `parseDiagnosticReport` and `indicators`, combine report evidence and model information. Screening is not proof of physical correctness.
- ReSWMM: `client/src/lib/reswmmEngine.ts`, `hydraulicDiameter`, `computeCflAnalysis`, and `discretizeConduits`, estimate wave celerity and split conduits.
- Its celerity equation is `c = sqrt(g * hydraulicDiameter)`. Gravity is 32.174 ft/s² for US models, or 9.81 m/s² for SI models. Segment count is `max(1, ceil(length / targetLength))`. Source: `client/src/lib/reswmmEngine.ts:129-224`.
- Comparison statistics: `client/src/lib/comparisonIdeas.ts`, `blandAltman`, uses `mean = (a+b)/2`, `difference = b-a`, `bias = average(difference)`, and agreement limits `bias +/- 1.96 * sampleSD`. Values must have compatible units. Source: lines 251-280.
- Timing: the workers and `server/swmm5api.ts` record initialization, simulation, and output phases. The comparison view explains differing boundaries and unavailable native executable phases.
- Optional warm browser runs reuse loaded engine resources. They are not equivalent to controlled hardware benchmarks.

## Inputs and outputs
- Inputs include SWMM `.inp` models, engine options, and supported auxiliary inputs. ReSWMM writes modified `.inp` files.
- Outputs include `.rpt`, binary `.out`, CSV, report documents, and ZIP downloads. Export implementations are in `client/src/lib/zipExport.ts` and `client/src/lib/pairedEngineExport.ts`.
- Server routes include `/api/swmm-status`, `/api/samples`, `/api/samples/:filename`, and `/api/github-models/tree`.
- Batch routes include `/api/upload`, `/api/batch/:jobId/files`, `/api/batch/:jobId/start`, `/api/batch/:jobId/cancel`, and `/api/batch/:jobId`.
- Result routes expose retained content and native artifacts. `/api/chat-report` streams AI responses. Source: `server/routes.ts:444-958,1694-1747`.
- PostgreSQL stores batch jobs and results through Drizzle. Sources: `shared/schema.ts:107-121`, `server/storage.ts`, and `server/db.ts:20-35`.
- Native runs use server files. Browser runs use worker virtual filesystems. Browser settings and regression baselines use local storage. Sources: `server/routes.ts`, `client/public/wasm/swmm-worker.js`, `client/src/lib/browserEngineSelection.ts:38-44`, and `client/src/lib/regressionBaseline.ts:170-193`.

## Contents
Counts below were taken from the current checkout on 2026-11-15.
- Eight explicit page routes, plus a not-found fallback. Source: `client/src/App.tsx:19-27`.
- Six browser engine records and one native bundle record. Source: counted entries in `client/public/engines.json`; also confirmed by the manifest validator run.
- The native bundle supports executable and API modes. Source: `server/routes.ts`, `processSingleFile` and `processSingleFileApi`.
- 113 `.inp` files directly inside `public/samples`. Source: Node filesystem count, filtering case-insensitive `.inp` suffixes.
- 58 test files directly inside `tests`. Source: Node filesystem count of `.test.ts` suffixes.
- Display name source: `client/src/components/AppHeader.tsx:50`. Version source: `package.json:3`.
- Front-matter date is the latest package-file commit date from `git log -1 --format='%cs' -- package.json`, not a verified release date.
- Engine versions, base commits, and license descriptors come from `client/public/engines.json`; Extended's base version is also documented in `tools/swmm5-kw-extension/references/integration.md`.
- Deployment name and URL were returned by the deployment metadata query during this inspection. No public GitHub repository URL was established; `git remote -v` records an internal GitHub proxy.

## Checks
Mechanical checks run on 2026-11-15:
- Command: `timeout 240 npm test`. Exit status: 1.
- Manifest and engine checks passed.
- Vitest: 549 tests passed, 1 failed, 550 total; 57 test files passed and 1 failed, 58 total.
- Failure: `tests/hydraEngine.test.ts:110`, classic-worker initialization. Error: `ReferenceError: performance is not defined` in the worker's VM test context.
- Evidence: current test output captured in `/tmp/summary-tests.log`. This temporary log is not a retained project deliverable.
- HTTP page checks: `curl` against the running development preview returned HTTP 200 for `/`, `/pitch`, `/folder`, `/dashboard`, `/docs`, `/reswmm`, `/qaqc`, and `/coherence`.
- These requests checked server responses, not browser rendering or interaction.
- Human review: none recorded.

## What this does not show
1. Browser rendering, console errors, and interactive workflows on every main page: not checked in this inspection.
2. Production page behavior, production data, and equivalence of deployed code to this checkout: not checked.
3. Independent hydraulic validation against measured drainage data: not checked.
4. Every sample model, parameter combination, and large-model workload: not checked.
5. Source-to-binary reproducibility of every engine and a complete third-party license audit: not checked. The manifest records provenance gaps.
6. Fresh TypeScript and production-build checks: not checked in this inspection.
7. AI service responses, correctness, cost, and external GitHub library contents: not checked.
8. Database row counts and stored user records: not checked.
9. The test suite is not fully passing. The Hydra VM failure does not by itself establish a browser-engine failure.
10. Extended KW/SF allocation and loop iteration do not provide Dynamic Wave backwater or pressure physics. Source: `tools/swmm5-kw-extension/references/design.md`.
11. Timing comparisons have different engine and machine boundaries. No universal speed ranking follows.
12. Human hydraulic review and Robert Dickinson's review of this summary are not recorded.

## How to reproduce
Use the configured project environment and its required database configuration. Do not commit credentials.
Commands are declared in `package.json:6-18`.
```sh
npm run dev
npm test
npm run check
npm run build
npm run start
```
To reproduce the bounded test invocation used here:
```sh
timeout 240 npm test
```
The timeout value is an inspection limit, not an application setting.

## Credits and licenses
- Author: Robert Dickinson, as specified for this document.
- Application license: MIT, declared in `package.json:5`.
- EPA SWMM, OpenWaterAnalytics SWMM, HydroCouple OpenSWMM, and neeraip Hydra supply the engine implementations.
- Engine license records are listed in the front matter and `client/public/engines.json`. Native glibc notices are under `swmm-engine/licenses/`.
- OpenSWMM attribution and runtime notices are under `client/public/licenses/openswmm/`.
- React, Express, Vite, Recharts, and Koffi declare MIT licenses.
- Drizzle ORM and the OpenAI SDK declare Apache-2.0 licenses.
- JSZip declares MIT or GPL-3.0-or-later.
- Library license source: each installed library's `node_modules/<package>/package.json`, read during this inspection. This is not an exhaustive dependency audit.
- ReSWMM background is credited in `docs/linkedin_reswmm_article.md` to the ecotecnologias/ReSWMM project.

## AI use
The application calls OpenAI's `gpt-4o` model for report discussion and streams the response. Source: `server/routes.ts:1694-1747`.
The prompt includes provided model and report content, with truncation notices. AI output is separate from the hydraulic engine computation.
The inspected code and documentation do not establish a complete tool-by-tool implementation history or Robert Dickinson's detailed implementation contributions.
Replit Agent inspected current source, ran the checks above, and wrote this summary. No other AI implementation attribution is asserted.
This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes
Source: `git log -10 --format='%cs: %s'`, newest first.
- 2026-10-23: Published your App.
- 2026-10-05: Update OpenSWMM WASM build configuration and dependency documentation.
- 2026-09-30: Implement experimental routing features and update associated tests.
- 2026-09-30: Update simulation engine workers and integrate engine comparison view.
- 2026-09-29: Published your App.
- 2026-09-29: Add dark mode dropdown styles and reference screenshots.
- 2026-09-29: Published your App.
- 2026-09-29: Add SWMM test models and update engine documentation.
- 2026-09-29: Add browser engine support and update export functionality.
- 2026-09-29: Add comparison summary to documentation.
