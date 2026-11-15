---
name: SWMM5-UI
file: swmm-ui-engine
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: "https://swmm-ui-engine.replit.app", repo: "https://github.com/dickinsonre/Swmm5-UI-Engine"}
engines:
  - {name: "EPA SWMM browser", version: "5.2.4-lid1", source: "USEPA/Stormwater-Management-Model, v5.2.4 with local LID changes", commit: "unrecorded", license: "EPA public domain; local contributions separately attributed"}
  - {name: "OpenSWMM release browser", version: "6.0.0-alpha.3", source: "HydroCouple/openswmm.engine, swmm6_rel with Emscripten changes", commit: "unrecorded", license: "Apache-2.0"}
  - {name: "OpenSWMM develop browser", version: "6.0.0-alpha.3", source: "HydroCouple/openswmm.engine, develop with Emscripten changes", commit: "unrecorded", license: "MIT"}
  - {name: "EPA SWMM local", version: "5.2.4 as documented", source: "swmm-engine/runswmm", commit: "not checked", license: "EPA public domain; modifications not independently audited"}
  - {name: "Remote SWMM service", version: "5.2.4 as labeled; remote binary not checked", source: "Cloud batch runner", commit: "not checked", license: "remote distribution not checked"}
  - {name: "Mock", version: "not separately versioned", source: "client/src/lib/swmm-engine.ts", commit: "not separately recorded", license: "MIT"}
stack: "TypeScript, JavaScript, C, C++, React, Vite, Tailwind CSS, Radix UI, TanStack Query, Recharts, wouter, Node.js, Express, WebAssembly, Emscripten; no application database; GitHub, remote SWMM batch runner, Replit hosting"
units: both
ai_use: "Replit Agent assisted development; in-app AI Assist is documented as local rule-based review."
---

# SWMM5-UI: Edit stormwater models, run simulation engines, and inspect results

## What it does

The app helps stormwater modelers inspect how rainfall, runoff, drainage networks, and LID controls behave in a SWMM model.
It opens and edits model files and runs browser, server, or remote simulation engines.
It displays maps, time series, tables, reports, diagnostics, and comparisons between selected runs.
Outputs include model files and engine reports, binary results, and detailed LID reports.
Sources: `README.md:44-70`, `client/src/lib/swmm-engine.ts`, and `server/routes.ts:553-789`.

## How it computes

1. `parseInpFile` in `client/src/lib/inp-parser.ts` converts INP sections into the project object. `projectToInp` writes the edited model. The round-trip audit in `client/src/lib/roundtrip-audit.ts` compares parsed representations.
2. `createWasmEngine` in `client/src/lib/swmm-engine.ts:231-288` writes model and companion files into the engine filesystem and calls `swmm_run` through Emscripten.
3. `createWasm6Engine` in the same file calls `swmm_engine_run` with input, report, and output filenames (`:477-510`). `runWasmEngineInWorker` dispatches browser engine work (`:659`).
4. Native execution spawns the configured executable with INP, RPT, and OUT paths in a temporary working directory (`server/routes.ts:284`). Remote execution uses `createRemoteEngine` and the server proxy, rather than a local JavaScript hydraulic solver.
5. `parseSwmmOut` reads binary reporting periods (`client/src/lib/swmm-out-parser.ts:63`). `parseRptToResults` handles report-derived results (`client/src/lib/swmm-engine.ts:1045`). A report-only result is not equivalent to native time series.
6. `computeExtendedVariables` adds diagnostic calculations to results (`client/src/lib/swmm-engine.ts:1069`). These are application calculations, not proof that the engine used the same intermediate values.

Selected diagnostic equations:

- Hydraulic radius: R = A / wetted perimeter.
- Manning capacity: Q = barrels * (phi / n) * A * R^(2/3) * sqrt(abs(slope)).
- Wave celerity: c = sqrt(g * A / top width).
- Froude number: Fr = abs(velocity) / c.
- US customary gravity is 32.174 ft/s²; SI gravity is 9.81 m/s². Manning phi is 1.4859 for US customary and 1.0 for SI.
- Sources: `computeExtendedVariables`, `client/src/lib/swmm-engine.ts:1070-1073,1187-1213,1354-1359`. The code includes minimum-value guards and substitutes; the equations above summarize the central expressions.

The separate planning calculation `computeCflAnalysis` uses c = sqrt(g * diameter), stableDt = length / c, and Courant = c * routingStep / length.
It also reports conservativeDt = stableDt * 0.10 and skips DUMMY and IRREGULAR shapes.
This is a simplified screening calculation, not the engine's actual adaptive timestep.
Source: `client/src/lib/cfl-analysis.ts:80-115`.

`generateMockResults` and `createMockEngine` generate synthetic demonstration data.
The mock path marks fidelity as `synthetic-mock`; it is not a physical simulation (`client/src/lib/swmm-engine.ts:1681-1793`).

## Inputs and outputs

- Reads SWMM `.inp`, engine `.out` and `.rpt`, detailed `.lid` data, and companion input files.
- Documented interchange includes CSV, DXF, and GeoJSON input, plus CSV and DXF output (`README.md:46-59`). Interchange round trips were not checked in this summary.
- Local model saves and report downloads use browser file/download mechanisms. Folder-aware saving is implemented in `client/src/lib/fs-access.ts`.
- Autosave snapshots and acknowledged recovery state use browser localStorage (`client/src/lib/autosave.ts:17-87`). Regression snapshots also use localStorage (`client/src/lib/regression-storage.ts:19-31`).
- Server result indexes are process-local maps (`server/routes.ts:45-46`). Native execution uses temporary server files (`:284`).
- `server/storage.ts` implements an in-memory user map. It does not implement persistent database storage.

API groups:

| Endpoint | Purpose | Source |
|---|---|---|
| `GET /api/swmm/status` | Native engine availability | `server/routes.ts:553` |
| `POST /api/swmm/run` | Native simulation | `server/routes.ts:628` |
| `POST /api/swmm/run-or-proxy` | Native execution or proxy fallback | `server/routes.ts:660` |
| `GET /api/swmm/out/:id` | Download parked binary results | `server/routes.ts:561` |
| `GET /api/swmm/lid/:id` | Download parked LID results | `server/routes.ts:597` |
| `/api/swmm-proxy/*` | Remote status, upload, batch start, status, results | `server/routes.ts:690-789` |
| `GET /api/github-browse`, `GET /api/fetch-github` | Browse and retrieve repository files | `server/routes.ts:465,509` |
| `POST /mcp` | Programmatic simulation and report tools | `README.md:72-82`, `server/mcp.ts` |

## Contents

| Item | Count | Evidence collected for this summary |
|---|---:|---|
| Main routed workbench | 1 | `client/src/App.tsx:8-15`; `/` and the fallback render the same component |
| Standalone viewer page examined | 1 | `client/public/3d-viewer.html`; browser load recorded below |
| Bundled INP sample files | 36 | Current run: `find client/public/samples -type f -iname '*.inp' \| wc -l` |
| Documented engine modes, including Mock | 6 | `README.md:31-38`; implementations in `client/src/lib/swmm-engine.ts` |
| MCP tool registrations | 3 | Current search of `server/mcp.ts`; registrations at lines 109, 151, 208 |

These counts describe files and registrations, not independent hydraulic validation cases.
The README sample and test counts are outdated relative to the current file census and test run.

## Checks

Checks were executed for this summary against the current workspace, not the published build.

| Command or action | Result |
|---|---|
| `npm run check` | Exit 0; TypeScript check passed |
| `npm test` | Exit 0; runner reported 34 groups passed, 0 failed |
| Vitest invocation within `npm test` | 8 test files passed; 58 tests passed; no failed tests reported |
| Chromium load of `/` through the development proxy | HTTP 200; 0 captured page exceptions or console errors |
| Chromium load of `/3d-viewer.html` through the development proxy | HTTP 200; 0 captured page exceptions or console errors |
| Workbench screenshot | Map, toolbar, and project explorer rendered; this was an initial-page check |

Test evidence: current execution of `npm run check` and `npm test`; runner definition is `tests/run-all.sh`.
The runner's group total includes its Vitest invocation as a group, so it is not an individual-assertion count.
Browser evidence: fresh Playwright Chromium run with `pageerror` and error-level console listeners on the listed pages.
The viewer check did not transfer a model or exercise animation.

Human review: none recorded for this summary.

## What this does not show

1. Full browser interaction suite: not checked. `npm run test:e2e` was not run for this summary.
2. Published application behavior and published/source equality: not checked. Deployment metadata supplied the site name and URL, not a functional production audit.
3. Remote engine availability, binary identity, commit, and license distribution: not checked.
4. Exact upstream commits for the browser engines are unrecorded in `engines.json`. Full reproducibility from upstream source is not established.
5. Native engine commit identity: not checked. The local version in front matter is the documented label, not an independently established source revision.
6. Field accuracy, calibration against observations, and universal engine parity: not checked. Passing repository tests is not certification of predictive accuracy.
7. SWMM6 LID results are explicitly marked untrustworthy in `README.md:42`. Their numerical correctness was not established here.
8. Long binary outputs are sampled using a nominal 5,000-period limit (`client/src/lib/swmm-out-parser.ts:61,196-201`). Unsampled peaks and every-period agreement were not checked.
9. Horizontal-scaling result retention: not checked. Process-local result maps do not establish cross-instance availability.
10. Import/export fidelity across every supported format, all dialog states, mobile layouts, and accessibility: not checked.
11. Security, authentication configuration, and dependency vulnerability audit: not checked. No credentials were read for this summary.
12. A release date specifically attached to package version 1.0.0 is not recorded in the inspected metadata. Front matter uses the summary date, not a claimed release date. Version source: `package.json:3`.
13. Individual human approval of the computations and this summary: not checked. Project credits do not establish review of every implementation.
14. Native file picker behavior and browser-specific filesystem permissions: not checked.

## How to reproduce

Use the existing dependencies, or install them in a separate checkout.
The scripts below are defined in `package.json:6-16`.

```bash
npm install
npm run dev
npm run check
npm test
npm run test:e2e
npm run test:lid-engine
npm run engines:check
```

Browser suites require the application to be running.
Native engine tests require the native executable expected by the project.
The commands listed for reproduction are not all claimed as executed above.

## Credits and licenses

- Robert Dickinson: application copyright holder; application source uses MIT (`LICENSE:1-8`).
- USEPA: original SWMM engine; public-domain government material (`NOTICE:11-31`).
- HydroCouple/OpenSWMM: release branch uses Apache-2.0; develop branch uses MIT (`NOTICE:60-98`).
- OpenSWMM contributors credited by the project include Caleb Buahin, Corinne Wiesner-Friedman, and Scott Jeffers (`README.md:150`). This is attribution, not a statement that they reviewed this app.
- React, Express, Vite, Tailwind CSS, Recharts, Radix UI, and TanStack Query: MIT, as read from their installed package manifests.
- TypeScript: Apache-2.0; wouter: Unlicense, as read from their installed package manifests.
- This is a selected dependency license inventory, not a complete redistribution audit.
- Engine versions and missing commit provenance above come from `engines.json:14-47,88-120,136-176`. Local and remote labels come from `README.md:36-38`.
- Display name source: `client/src/components/swmm/AboutDialog.tsx:60`. Repository link source: `README.md:112`. Deployment URL source: deployment metadata queried for this summary.

## AI use

`README.md:144` records iterative development with Replit Agent.
The git history records implemented features but does not allocate every line of code between Robert Dickinson and the agent.
`LICENSE:3` credits Robert Dickinson as copyright holder; `engines.json:41` attributes LID-consolidation changes to him.
His detailed manual implementation and review actions were not checked.
The local AI Assist feature is described as rule-based review with no external service (`README.md:70`).
MCP permits external programmatic or AI access; that does not establish use of any particular external AI tool.
No other development AI tool was established from the inspected records.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: current `git log -10 --format='%ad: %s' --date=short`. Dates are commit dates, not independently verified releases.

- 2026-09-21: Implement SWMM parser updates and document modifications.
- 2026-09-21: Published your App.
- 2026-09-21: Published your App.
- 2026-09-19: Expose native pollutant concentrations with units and provenance across maps, graphs, and tables.
- 2026-09-19: Reject self-loop virtual junction candidates before SWMM6 export.
- 2026-09-19: Extend Engine Inspector geometry with EPA shape tables and validated US/SI custom and transect calculations.
- 2026-09-19: Deliver native Local LID reports to animated viewer, preserving valid dry and optional-field models.
- 2026-09-19: Strengthen CFL regression coverage for regulator cross-sections and losses.
- 2026-09-19: Add detailed LID downloads to report dialog and project output saving, with browser regression coverage.
- 2026-09-19: Automate live SWMM5 LID parity validation and byte-exact Extran1 regression control.
