---
name: SingaPourApps
file: singa-pour-site
version: 1.0.0
date: 2025-12-24
author: Robert Dickinson
links: {replit: https://singa-pour-site--robertdickinson.replit.app, repo: none}
engines: none
stack: TypeScript, JavaScript, React, Vite, Express, Node.js, PostgreSQL, Drizzle ORM, Replit hosting, Google Fonts, Twitter share link
units: not applicable
ai_use: No AI tool use for the app is recorded in the inspected source or documentation.
---

# SingaPourApps: Parses SWMM input files into rainfall, runoff-parameter, and discharge summaries

## What it does

The app accepts text input in SWMM `.inp` format and presents three analysis views for rainfall time series, subcatchment parameters, and drainage nodes and conduits. A user can upload a model, select it for an analysis, and view summary values, tables, and simple visualizations. The app stores uploaded model text and analysis results in PostgreSQL. The current published site serves its home page, but its model API endpoint returned HTTP 404 during this check.

## How it computes

- `parseSwmmFile` in `server/swmm-parser.ts` separates bracketed sections, uppercases section names, and ignores blank lines and lines beginning with `;` (`server/swmm-parser.ts:10-27`).
- `analyzeRainfall` reads `RAINGAGES` and `TIMESERIES`. It adds the parsed values for total depth, takes the largest sample (or zero) as `peakIntensity`, counts samples for duration, groups zero values into gaps, and groups adjacent positive values into storm events (`server/swmm-parser.ts:29-97`). It reads the displayed unit from the third field of the first rain-gage line, or defaults to `in` (`server/swmm-parser.ts:99-115`). It does not calculate intensity from elapsed time.
- `analyzeRunoff` reads `SUBCATCHMENTS`, `SUBAREAS`, `INFILTRATION`, and `OPTIONS`. It sums subcatchment area and computes the arithmetic mean of impervious percentages (`server/swmm-parser.ts:119-166`). It reads the infiltration method from `OPTIONS`, defaulting to `HORTON` (`server/swmm-parser.ts:168-181`). It reports parsed parameters; it does not run a runoff simulation.
- `analyzeDischarge` reads junction, outfall, storage, conduit, and cross-section rows. It calculates circular cross-section area as pi times radius squared, rectangular cross-section area as the product of the first two geometry values, and otherwise uses the first geometry value (`server/swmm-parser.ts:184-283`). It flags nodes with positive surcharge depth and nodes whose parsed maximum depth is greater than zero and less than `2` (`server/swmm-parser.ts:285-300`). It does not calculate hydraulic flow or run a SWMM engine.
- No unit conversion or app-wide unit setting was found. The parser uses model values as written, except for the rainfall display-unit behavior above.

## Inputs and outputs

- The upload form accepts `.inp` and `.txt` files, reads them as text in the browser, and sends a model name and content to the server (`client/src/pages/Tools.tsx:91-112`, `client/src/pages/Tools.tsx:153-160`).
- Models are stored in the PostgreSQL `swmm_models` table. Analysis results are stored as JSON in `analysis_results` (`shared/schema.ts:20-49`; `server/storage.ts:41-70`).
- The API accepts and returns JSON. Routes are `POST /api/models`, `GET /api/models`, `GET /api/models/:id`, `DELETE /api/models/:id`, `POST /api/analyze/rainfall/:modelId`, `POST /api/analyze/runoff/:modelId`, `POST /api/analyze/discharge/:modelId`, and `GET /api/results/:modelId` (`server/routes.ts:12-134`).
- No model or analysis export-to-file behavior was found. The client renders returned results in the page.

## Contents

| What | Count or status | Source |
| --- | --- | --- |
| Browser routes | 5 | `client/src/App.tsx:13-22` |
| Analysis tools | 3 | `client/src/pages/Tools.tsx:13-40` |
| Database tables | 3: users, models, analysis results | `shared/schema.ts:6-49` |
| API routes | 8 | `server/routes.ts:12-134` |
| Development model records | 0; `GET /api/models` returned `[]` with HTTP 200 during this run | Development API request made for this summary |
| Sample SWMM input files in the inspected project tree | 0 found | File search run for `.inp` files |

## Checks

- `npm run check`: passed; TypeScript compiler exited with status `0`.
- `npm test`: no test cases ran. The command exited with status `1` because `package.json` has no `test` script. No tracked test files were found.
- Browser preview: `/`, `/tools`, `/tools/rainfall`, `/tools/runoff`, and `/tools/discharge` loaded. The browser logs showed Vite connection messages and an informational React DevTools notice, with no browser errors.
- Published site: the home page returned HTTP `200`. `GET /api/models` on the published site returned HTTP `404`. The Replit deployment metadata reports a successful build and a `static` deployment; `.replit` currently specifies `autoscale` for the next deployment.
- Human review: none recorded.

## What this does not show

1. Version `1.0.0` comes from `package.json:4`. No release date for that version is recorded. The front-matter date is the latest date in the inspected Git history, not a verified release date.
2. No public GitHub repository URL was found. The configured Git remote is an internal Replit URL, so the repository link is listed as `none`.
3. No tests exercise model uploads, analysis calculations, malformed input, or database persistence. The browser check loaded pages but did not submit a model or run an analysis.
4. The analysis-result row count was not checked. No API route lists all results independently of a model. The development model list was empty, and the published model API returned HTTP `404`, so no production model count was obtained.
5. The published API response means the model-upload and analysis flow was not verified on the live site. This summary does not establish why the published API route is unavailable.
6. No person has recorded a review of the app or this summary.

## How to reproduce

- Start the development app: `npm run dev`.
- Run the available TypeScript check: `npm run check`.
- A new database needs `DATABASE_URL` configured and the schema applied with `npm run db:push` (`server/db.ts:7-14`, `package.json` scripts).
- There is no `npm test` script in `package.json`.

## Credits and licenses

- App author recorded in the checked Git history: Robert Dickinson. The project declares MIT in `package.json`; no separate tracked `LICENSE` file was found.
- Direct dependency licenses below are from the installed package manifests. The project records no simulation-engine dependency.
- MIT: `@hookform/resolvers`, `@jridgewell/trace-mapping`, `@radix-ui/react-accordion`, `@radix-ui/react-alert-dialog`, `@radix-ui/react-aspect-ratio`, `@radix-ui/react-avatar`, `@radix-ui/react-checkbox`, `@radix-ui/react-collapsible`, `@radix-ui/react-context-menu`, `@radix-ui/react-dialog`, `@radix-ui/react-dropdown-menu`, `@radix-ui/react-hover-card`, `@radix-ui/react-label`, `@radix-ui/react-menubar`, `@radix-ui/react-navigation-menu`, `@radix-ui/react-popover`, `@radix-ui/react-progress`, `@radix-ui/react-radio-group`, `@radix-ui/react-scroll-area`, `@radix-ui/react-select`, `@radix-ui/react-separator`, `@radix-ui/react-slider`, `@radix-ui/react-slot`, `@radix-ui/react-switch`, `@radix-ui/react-tabs`, `@radix-ui/react-toast`, `@radix-ui/react-toggle`, `@radix-ui/react-toggle-group`, `@radix-ui/react-tooltip`, `@tanstack/react-query`, `clsx`, `cmdk`, `connect-pg-simple`, `date-fns`, `embla-carousel-react`, `express`, `express-session`, `framer-motion`, `input-otp`, `memorystore`, `next-themes`, `passport`, `passport-local`, `pg`, `react`, `react-day-picker`, `react-dom`, `react-hook-form`, `react-resizable-panels`, `recharts`, `sonner`, `tailwind-merge`, `tailwindcss-animate`, `tw-animate-css`, `vaul`, `ws`, `zod`, `zod-validation-error`, `@tailwindcss/vite`, `@types/connect-pg-simple`, `@types/express`, `@types/express-session`, `@types/node`, `@types/passport`, `@types/passport-local`, `@types/react`, `@types/react-dom`, `@types/ws`, `@vitejs/plugin-react`, `autoprefixer`, `drizzle-kit`, `esbuild`, `postcss`, `tailwindcss`, `tsx`, and `vite`.
- Apache-2.0: `drizzle-orm`, `drizzle-zod`, `class-variance-authority`, and `typescript`.
- ISC: `lucide-react`.
- Unlicense: `wouter`.
- License not declared in installed package manifest: `@replit/vite-plugin-cartographer`, `@replit/vite-plugin-dev-banner`, and `@replit/vite-plugin-runtime-error-modal`.
- External services named in the project: Replit hosting and PostgreSQL, Google Fonts, and a Twitter share link (`client/index.html:22-24`, `client/src/components/layout/Footer.tsx:5-8`). The project does not state separate licenses for these services or the font files.

## AI use

The inspected source and documentation do not identify an AI tool used to build the app. The checked Git history lists Robert Dickinson as author but does not record which work he performed or whether he used AI. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2025-12-24: Add new simulation tools for rainfall, runoff, and discharge analysis
- 2025-12-24: Saved progress at the end of the loop
- 2025-12-24: Add a Twitter share button to the website footer
- 2025-12-22: Published your App
- 2025-12-21: Published your App
- 2025-12-21: Published your App
- 2025-12-21: Update hero section title for hydrology and hydraulics tutorials
- 2025-12-21: Update About section with a new concept diagram
- 2025-12-21: Published your App
- 2025-12-21: Update website to showcase water engineering applications
