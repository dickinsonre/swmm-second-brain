---
name: SWMM5 vs ICM InfoWorks Networks
file: swmm-icm-st-venant--robertdickinson
version: 1.0.0 # package.json:3
date: 2026-07-22 # Latest publication entry in git log; package version date is not stated.
author: Robert Dickinson
links: {replit: https://swmm-icm-st-venant--robertdickinson.replit.app, repo: none}
engines: none
stack: TypeScript, React, Vite, Express, Node.js, Tailwind CSS, Drizzle ORM, PostgreSQL schema, Google Fonts, Replit hosting
units: both
ai_use: Git history attributes changes to Replit Agent and Robert Dickinson; details are under AI use.
---

# SWMM5 vs ICM InfoWorks Networks: Technical solver comparison and learning reference

## What it does

The app explains differences between EPA SWMM 5 and InfoWorks ICM for hydraulic modeling of unsteady flow. It is aimed at modelers and learners who need to compare solver concepts and related engineering behavior. The interface presents a comparison summary, topic-based material, tables, source snippets, diagrams, and interactive calculators. Users can export the comparison content as JSON or Markdown. (Sources: `client/src/pages/dashboard.tsx:237-240`; `client/src/data/comparison-data.ts:1-6`; `client/src/lib/exporters.ts:3-18,30-67`.)

## How it computes

The app does not call or embed the EPA SWMM 5 or InfoWorks ICM simulation engines. It renders authored comparison data and educational visualizations from TypeScript modules. The calculations below are in `client/src/components/visuals/CalculatorDiagrams.tsx`.

- `CFLStabilityCalculator`: computes Courant number as `Cr = (V + c) * Δt / Δx`, derives a maximum step as `Δx / (V + c)`, and labels values at or below one stable. (`:26-41,154-160`.)
- `PreissmannSlotCalculator`: computes slot width as `pipe diameter * width factor / 100`; estimates pressure-wave speed as `sqrt(g * full-pipe area / slot thickness)`, with a lower slot-thickness bound and an upper speed cap. (`:175-190`.)
- `ManningsFlowCalculator`: derives the partially full circular area and hydraulic radius, then applies Manning's equation, `Q = (1.49 / n) * A * Rh^(2/3) * sqrt(S)`. It displays a comparison value with a small code-defined adjustment; these are illustrative values, not outputs from the engines. (`:327-354,460-470`.)
- `TimeStepEfficiencyEstimator`: applies code-defined timestep bounds and storm/network-size factors to estimate step counts and runtime. The component itself warns that actual runtime depends on hardware, model complexity, and solver settings. (`:451-470,596-600`.)
- `FroudeNumberDiagram`: displays a Froude number and flow regime, with the equation `Fr = V / sqrt(gD)` shown in the component. (`:609-619,695-714`.)
- `ComputationalPointsDiagram`: estimates ICM segments as `max(2, ceil(conduit length / 200))`; the SWMM5 side is drawn as conduit endpoints. (`:710-718,795-807`.)
- `InertialTermsDiagram`: updates an equation-type label from enabled/disabled momentum-term controls; it does not solve the flow equations. (`:795-810,839-868`.)
- `SurchargeAlgorithmDiagram`: maps the user-controlled head-above-crown value to labeled flow regimes using fixed thresholds. (`:937-958`.)
- `SurfaceFloodingDiagram`: animates a display level by fixed increments. It does not calculate a hydraulic flood solution. (`:1043-1059`.)

Most comparison content is authored in `client/src/data/comparison-data.ts`. Unit labels default to U.S. customary units, with SI display conversions in `client/src/contexts/UnitsContext.tsx:41-95`. Favorites are saved in browser local storage. (`client/src/contexts/FavoritesContext.tsx:13-54`.)

## Inputs and outputs

- Inputs are user-entered values and controls in the browser, including sliders, numeric fields, tabs, search, and favorite toggles. The comparison data is bundled TypeScript, not user-uploaded input files. (`client/src/pages/dashboard.tsx`; `client/src/components/visuals/CalculatorDiagrams.tsx`.)
- The app route is `/`. The dashboard supports the `visuals`, `topic`, `table`, and `source` views and uses query parameters for shareable view/category/diagram state. (`client/src/App.tsx:12-17`; `client/src/pages/dashboard.tsx:123-157`.)
- There are no application API endpoints registered in `server/routes.ts`. That file contains route-registration scaffolding only. (`server/routes.ts:5-15`.)
- Favorites are stored in browser `localStorage`. The server also has an in-memory user-storage class, but no application route exposes it. (`client/src/contexts/FavoritesContext.tsx:17-54`; `server/storage.ts:13-38`.)
- The export controls download `comparison.json` or `comparison.md` in the browser. (`client/src/lib/exporters.ts:8-18,53-67`.)

## Contents

- 118 diagram registry entries across 16 distinct diagram categories, counted from `DIAGRAM_REGISTRY`. (`client/src/data/diagram-registry.tsx:10-129`; category count logic at `:135-141`.)
- 13 comparison topics, counted from `TOPIC_ORDER`. (`client/src/data/comparison-data.ts:898-912`.)
- Two comparison records: `swmm5` and `icm`. (`client/src/data/comparison-data.ts:860-895`.)
- Five guided-tour steps. (`client/src/data/tour-steps.ts:1-27`.)
- One dashboard route and one fallback route. (`client/src/App.tsx:12-17`.)
- The interface labels the reference engines SWMM5 v5.2.4 and ICM v2025.1, and displays “Last updated: Feb 2026.” These are app labels, not proof of installed engine versions. (`client/src/components/visuals/ReviewDiagrams.tsx:767-775`.)

## Checks

- `npm run check`: passed. This runs TypeScript checking from `package.json:11`.
- `npm test`: the command exited because `package.json` has no `test` script. No tests ran: 0 passed and 0 failed test cases.
- Loaded the four dashboard view states at `/` with `?view=visuals`, `?view=topic`, `?view=table`, and `?view=source` in the app preview. All rendered. The Topic view browser log reported an HTML error because a `button` appears inside another `button`; the other captured views showed only Vite connection and React DevTools informational messages.
- `GET /` and `GET /src/main.tsx` returned HTTP 200 in the local run. `server/routes.ts` registers no API endpoints.
- Human review: none recorded.

## What this does not show

1. The app's visual formulas and example outputs have not been validated against actual SWMM 5 or InfoWorks ICM engine runs.
2. The test suite is not present as an npm script. Interactive behavior for every diagram was not exercised.
3. The browser check covered the first viewport of the four dashboard views, not every diagram, interaction, device size, or full-page state.
4. The Topic view has a browser-console HTML nesting error involving nested buttons. Its effect on other browsers or assistive technology was not checked.
5. The timestep estimator is explicitly an estimate, not a measured benchmark. (`client/src/components/visuals/CalculatorDiagrams.tsx:596-600`.)
6. The package version is recorded, but its release date is not. The front-matter date uses the latest Git publication entry, not a verified version-release date.
7. A public repository URL was not verified. The configured Git remote is an internal Git host.
8. The configured PostgreSQL/Drizzle dependencies and schema do not establish that the running app uses a database. The inspected route and storage code uses no database-backed app endpoint.
9. The full dependency tree's licenses and the font licenses were not individually audited.

## How to reproduce

```sh
npm install
npm run dev
npm run check
npm test
```

`npm run dev` starts the application. `npm run check` runs TypeScript checking. `npm test` currently exits because no test script is defined. `npm run build` is the configured production build command, but it was not run for this summary to avoid changing generated project files. (`package.json:6-12`.)

## Credits and licenses

| Person, project, or library | License or recorded role | Source |
| --- | --- | --- |
| Robert Dickinson | Author named for this summary. Git history attributes earlier documentation, unit-display, and accessibility changes to `robertdickinson`. | Git log |
| Replit Agent | Git history attributes later app publication, review-document, refactor, and search/navigation changes to Replit Agent. | Git log |
| EPA SWMM 5 | The app describes it as public domain. | `client/src/pages/dashboard.tsx:452-455` |
| Autodesk InfoWorks ICM | The app describes it as commercial software. | `client/src/pages/dashboard.tsx:452-455` |
| React, React DOM, Express, Vite, Tailwind CSS, TanStack Query, Framer Motion, Zod, Radix UI | MIT, as declared in installed package metadata. | `node_modules/<package>/package.json` |
| TypeScript, Drizzle ORM, Drizzle Zod | Apache-2.0, as declared in installed package metadata. | `node_modules/<package>/package.json` |
| Wouter | Unlicense, as declared in installed package metadata. | `node_modules/wouter/package.json` |
| Lucide React | ISC, as declared in installed package metadata. | `node_modules/lucide-react/package.json` |
| This project | `package.json` declares MIT. No root `LICENSE` file was present. | `package.json:5` |
| Replit and Google Fonts | Hosting and font services are referenced by project configuration/source; their service terms are not stated in this project. | `.replit`; `client/index.html:18-20` |

## AI use

Git history names Replit Agent and Robert Dickinson as commit authors. Replit Agent is credited in that history for app publication and later review, refactor, and search/navigation changes. Robert Dickinson is credited for earlier documentation, unit-display, accessibility, and publishing changes. Git history does not establish which lines were AI-generated or the full extent of either person's work.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-07-22: Published the app.
- 2026-07-22: Updated the review document with feedback.
- 2026-07-22: Refactored performance, accessibility, and code structure.
- 2026-07-22: Added search, deep links, evidence badges, and learning modes.
- 2026-07-22: Applied fixes from a quality review.
- 2026-07-22: Switched the project from planning to implementation.
- 2026-03-25: Added accessibility and error handling to interactive diagrams.
- 2026-03-25: Improved unit-display consistency.
- 2026-03-24: Published the app.
- 2026-03-09: Updated project documentation.
