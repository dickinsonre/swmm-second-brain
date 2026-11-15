---
name: ICM PRN File Reader
file: icm-reader-robertdickinson
version: 1.0.0
date: 2025-08-05
author: Robert Dickinson
links: {replit: "https://icm-reader-robertdickinson.replit.app", repo: none}
engines: none
stack: "TypeScript, JavaScript, Node.js, Express, React, Vite, Tailwind CSS, Radix UI, TanStack Query, Wouter, Zod, Multer, Recharts, ExcelJS, PDFKit; in-memory storage; Replit hosting"
units: both
ai_use: "Git records Replit Agent contributions; no runtime AI integration identified in the inspected application paths."
---

# ICM PRN File Reader: Inspect hydraulic simulation summaries and export converted results

## What it does
The app helps civil engineers and water management professionals inspect InfoWorks ICM PRN output.
It extracts node, link, and mass-balance data and identifies flooding, surcharge, and capacity conditions.
Users can view tables and dashboard charts, convert units, and export CSV, Excel, or PDF files.
It reads existing simulation results; it does not run a hydraulic simulation.
Sources: `replit.md`, `server/prn-parser.ts`, `server/routes.ts`, and `client/src/components/results-display.tsx`.

## How it computes
- `server/prn-parser.ts:54`, `parsePrnFile`: split input into lines, identify sections, skip page furniture, and extract trailing numeric fields while preserving identifiers.
- Node rows contain 9 numeric fields. Link rows use 14 or 8 numeric fields. Sources: `server/prn-parser.ts:176-220`.
- `parsePrnFile` computes `surchargeDepth = max(0, maxLevel - groundLevel)` and `freeboard = groundLevel - maxLevel`, rounded to 3 decimal places. Source: `server/prn-parser.ts:20-22,204-205`.
- `nodeStatus` prioritizes data warnings, severe flooding, flooding, and surcharge. Severe flooding starts at about 353.147 ft³ (10 m³); flooding exceeds about 1.766 ft³ (0.05 m³); surcharge applies below about 1.640 ft (0.5 m) freeboard without flooding. Sources: `server/prn-parser.ts:4-9,35-40`; customary equivalents calculated from `server/routes.ts:53-63`.
- `parsePrnFile` chooses the signed upstream or downstream flow and velocity with the larger absolute magnitude. `capacityPercent = abs(maxFlow) / pipeFullFlow * 100`, rounded to 1 decimal place. Capacity is null when pipe-full flow is not positive. Source: `server/prn-parser.ts:249-251`.
- `classifyLinkType` uses identifier patterns and numeric-field counts. `linkStatus` classifies capacity above 100%, capacity at least 80%, reverse flow, or unavailable capacity, with data warnings taking priority. Source: `server/prn-parser.ts:24-51`.
- `parsePrnFile` reads summary totals. When reported total inflow or outflow equals zero, it substitutes component sums. `volumeError = totalInflow - totalOutflow`; when continuity error equals zero and inflow is positive, `continuityErrorPercent = volumeError / totalInflow * 100`. Both errors are rounded to 2 decimals. Source: `server/prn-parser.ts:123-134,292-304`.
- Mass-balance status is critical above 10% absolute error, warning above 5%, otherwise acceptable. Source: `server/prn-parser.ts:303-304`.
- `server/routes.ts:66-164`, `convertUnits` and `convertPrnData`: copy the stored data, apply conversion factors, and round numeric outputs to the selected precision. Status classifications remain those of the parsed source.
- Customary conversion equations: `cfs = m³/s * 35.3147`; `ft = m * 3.28084`; `ft³ = m³ * 35.3147`; `ft² = m² * 10.7639`; `in = mm / 25.4`. Reverse conversions use reciprocals. Source: `server/routes.ts:53-91`.
- Precision accepts 0 through 6 decimal places, defaulting to 2. Source: `shared/schema.ts:31-35`.
- `DashboardTab` counts status categories, finds maximum flood volume and absolute velocity, and ranks flooded nodes and capacity-limited links. `makeHistogram` places values into bins by comparing them with bucket edges. Source: `client/src/components/dashboard-tab.tsx:48-107`.
- No simulation engine is invoked. InfoWorks ICM is the upstream output format, not an embedded solver.

## Inputs and outputs
| Interface | Input or output |
| --- | --- |
| `GET /` | Upload, conversion settings, and results interface |
| `POST /api/prn/upload` | Multipart `file`; UTF-8 PRN/text input; parsed JSON and file identifier |
| `POST /api/prn/sample` | Bundled sample input; parsed JSON and file identifier |
| `POST /api/prn/convert` | File identifier and validated settings; converted JSON |
| `GET /api/prn/:fileId/export` | CSV; optional settings and all/nodes/links/massbalance section |
| `GET /api/prn/:fileId/export-report` | XLSX or PDF selected by `format`; optional settings |
| `GET /api/prn/files` | Stored file objects, including content and parsed data |

Sources: `client/src/App.tsx:10-16`; `server/routes.ts:256-466`.

- Upload limit: 50 MiB. The server accepts a plain-text MIME type or a filename ending in `.prn`. Source: `server/routes.ts:37-49`.
- Raw text and parsed objects reside in server-process memory, not an active database. Source: `server/storage.ts:19-25,64-94`.
- Expiration is checked on storage access after 3 hours. Cleanup targets 20 retained files, but insertion occurs after cleanup and can temporarily exceed that target. Source: `server/storage.ts:16-44,64-84`.
- Server restarts discard stored uploads. Browser theme preference uses local storage; current file and conversion state use React state. Sources: `server/storage.ts`; `client/src/hooks/use-theme.tsx:14-21`; `client/src/pages/home.tsx`.
- The sample is a server file at `server/data/sample.prn`. The sample route searches alternative deployment-relative locations. Source: `server/routes.ts:294-314`.
- PostgreSQL/Drizzle schema and dependencies exist, but `storage` is explicitly `MemStorage`. Older database/session statements in `replit.md` do not describe this active storage implementation.

## Contents
| Item | Count | Source |
| --- | ---: | --- |
| Main page | 1 | `client/src/App.tsx:13` |
| Fallback page | 1 | `client/src/App.tsx:14` |
| Results tabs | 5 | Dashboard, Node Data, Link Data, Mass Balance, Parsing Report; `client/src/components/results-display.tsx:174-203` |
| PRN API routes | 6 | Route declarations in `server/routes.ts:256-456` |
| Excel worksheets | 4 | Metadata, Nodes, Links, Mass Balance; `server/report-exports.ts:65,76,105,145` |
| Nodes in bundled sample | 37 | Direct parser run on `server/data/sample.prn` during this review |
| Links in bundled sample | 75 | Same parser run |
| Unparsed sample data lines | 0 | Same parser run, `parsingReport.unparsedLines` |
| Undefined sample capacities | 1 | Same parser run, `parsingReport.undefinedCapacities` |

Counts describe the current source and bundled sample, not user uploads or production usage.

## Checks
Checks were run on 2026-11-15 for this summary.

- `npx vitest run`: 24 tests passed, 0 failed; 2 test files passed, 0 failed. Source: this review's command output. The files are `server/__tests__/prn-parser.test.ts` and `server/__tests__/storage.test.ts`.
- `npm run check`: passed with exit status 0 and no TypeScript diagnostics. Source: this review's command output.
- Loaded `/` in the running development app. Upload and conversion controls rendered. No browser errors were reported.
- Loaded `/summary-route-check` to exercise the fallback page. The expected not-found screen rendered. No browser errors were reported.
- Parsed the bundled sample directly with `parsePrnFile`; resulting counts appear under Contents.
- Deployment metadata lookup returned the published URL used above. This was a metadata check, not a production-page test.
- Human review: none recorded in the inspected source, documentation, tests, or git commit messages.

## What this does not show
1. Production behavior: not checked. The deployed app was not loaded or exercised.
2. Interactive upload, sample loading, conversion controls, results tabs, and download behavior in the browser: not checked in this review. Page checks cover initial rendering only.
3. Current HTTP-level invalid-upload handling, conversion accuracy, and export integrity: not checked. The executed suite covers parser and storage code, not those complete API paths.
4. Large-file throughput, concurrent users, memory pressure, mobile layouts, accessibility, and cross-browser behavior: not checked.
5. Reverse conversion correctness for actual US-customary input: not checked. Conversion starts from stored data described by the code as original SI data, while reverse settings are accepted. Source: `server/routes.ts:94-108`; `shared/schema.ts:31-35`.
6. Classification thresholds differ across views. Parser mass balance uses warning above 5% and critical above 10%; dashboard tone uses good through 1%, warning through 5%, then critical. Sources: `server/prn-parser.ts:304`; `client/src/components/dashboard-tab.tsx:120-121`.
7. Capacity boundaries also differ: parser over-capacity status requires greater than 100%; dashboard overload counts include exactly 100%. Sources: `server/prn-parser.ts:46`; `client/src/components/dashboard-tab.tsx:67-68`.
8. Missing mass-balance components begin as zero. Dry-weather flow and flooding are not assigned extracted values in this parser. The summary is not an independent hydraulic mass-conservation audit. Source: `server/prn-parser.ts:76-88,123-134,292-304`.
9. The file-list route returns stored file objects without route-level authentication. Security and privacy testing: not checked. Source: `server/routes.ts:456-459`; `server/storage.ts:67-72,82-86`.
10. Engine accuracy, compatibility with other PRN variants, and engineering suitability have not been independently reviewed by a person in the inspected records.
11. A distinct release date is not recorded. The front-matter date is the earliest git record of package version 1.0.0, dated 2025-08-05. Source: `git log --reverse -- package.json` and that commit's `package.json:3`; later changes retained the version.
12. Public repository availability and the complete transitive dependency license inventory: not checked. Git records an internal Replit GitHub remote, not a verified public GitHub URL.
13. Dependency installation and a fresh production build/start: not checked in this review.

## How to reproduce
Use the existing dependency lockfile and the project's Node.js environment.

```sh
npm ci
npm run dev
```

Run checks separately:

```sh
npx vitest run
npm run check
```

Reproduce the sample count without uploading or changing stored data:

```sh
npx tsx -e 'import {readFileSync} from "fs"; import {parsePrnFile} from "./server/prn-parser"; const d=parsePrnFile(readFileSync("server/data/sample.prn","utf8")); console.log({nodes:d.nodeData.length,links:d.linkData.length,report:d.parsingReport});'
```

Production build/start commands are defined in `package.json:8-9`:

```sh
npm run build
npm start
```

## Credits and licenses
- Summary author: Robert Dickinson, as requested.
- Project license: MIT, declared in `package.json:5`.
- React, Express, Vite, Tailwind CSS, Radix UI, TanStack Query, Multer, Zod, ExcelJS, PDFKit, Recharts, and Vitest: MIT.
- TypeScript and Drizzle ORM: Apache-2.0.
- Wouter: Unlicense. Lucide React: ISC.
- Library license sources: the respective installed `node_modules/<package>/package.json` license fields, read during this review. These are package declarations, not a legal audit.
- Autodesk InfoWorks ICM is named by the parser and project documentation as the source format. No engine source, engine commit, or engine license is bundled or established by this review.

## AI use
Git commit authors record Replit Agent contributions to the app.
Agent-authored subjects include interface setup, dark mode, parsing improvements, and sample-file deployment fixes.
The git log also records `robertdickinson` on the workbook/PDF export commit. Commit attribution alone does not establish who wrote each line or performed engineering review.
No other AI tool was identified in the inspected application code and project documentation. Underlying models and a complete AI contribution history are not recorded.
No runtime AI service call was identified in the inspected parsing, conversion, or export paths.
This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes
Source: `git log -10 --format='%ad %s' --date=short`, newest first. Dates are commit dates, not independently verified release dates.

- 2026-07-22: Published the app.
- 2026-07-22: Updated sample-file lookup for production builds.
- 2026-07-22: Added Excel workbook and PDF report exports.
- 2026-07-22: Published the app.
- 2026-07-22: Fixed sample PRN loading in production.
- 2026-07-22: Published the app.
- 2026-07-22: Added QA dashboard, exports, and reliability work.
- 2026-07-22: Recorded additional QA dashboard, exports, and reliability work.
- 2026-07-22: Expanded parsing, node/link fields, types, validation, and parsing reports.
- 2026-07-22: Fixed units, labels, and misleading controls.
