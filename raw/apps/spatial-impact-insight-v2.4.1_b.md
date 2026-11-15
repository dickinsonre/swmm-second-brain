---
name: GeoAI Flood Impact
file: spatial-impact-insight
version: 2.4.1_b
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://spatial-impact-insight.replit.app, repo: none}
engines: none
stack: TypeScript, React, Vite, Express, PostgreSQL, Drizzle ORM, Zod, TanStack Query, Recharts, Orval, Replit hosting, Google Fonts
units: SI
ai_use: No AI model calls found in the inspected runtime code; Git history attributes app and documentation commits to Replit Agent.
---

# GeoAI Flood Impact: flood exposure decision support

## What it does

GeoAI Flood Impact presents stored community and infrastructure flood-exposure information for response planning. It shows communities by exposure and response status, summarizes district and infrastructure risk, and displays the stored GeoAI workflow descriptions. The community detail view provides recorded component scores, coordinates, and nearby infrastructure. The app reads and updates PostgreSQL records through its API; it does not run a satellite-processing or flood-simulation engine in the inspected application code. (Routes: `artifacts/flood-impact/src/App.tsx:20-25`; data mapping and handlers: `artifacts/api-server/src/routes/flood.ts:30-68,70-115,205-254`; database connection: `lib/db/src/index.ts:7-14`.)

## How it computes

- Community exposure scores, impact categories, and component scores are stored values. The app returns these values; the database schema does not define a formula for deriving them. (`lib/db/src/schema/communities.ts:17-28`; `artifacts/api-server/src/routes/flood.ts:30-49,242-254`.)
- The dashboard classifies communities marked `high` or `moderate` as at risk, and infrastructure with `high` or `moderate` status as vulnerable. Average exposure is the sum of community exposure scores divided by the number of communities, rounded to one decimal place. Analyzed area is the sum of district `areaKm2` values. (`artifacts/api-server/src/routes/flood.ts:70-113`.)
- Priority areas exclude communities with response status `complete`, sort the remainder by exposure score descending, and return the first eight. (`artifacts/api-server/src/routes/flood.ts:191-203`.)
- Community detail selects infrastructure in the same district, sorts it using `(asset latitude - community latitude)^2 + (asset longitude - community longitude)^2`, and returns the first five. This is a coordinate-space ordering, not a geodesic distance calculation. (`artifacts/api-server/src/routes/flood.ts:225-240`.)
- The map linearly scales latitude and longitude to the map bounds. Marker radius is `clamp(sqrt(population) / 10, 3, 12)` pixels. These are display calculations, not flood-model calculations. (`artifacts/flood-impact/src/components/spatial-map.tsx:20-57`.)
- Physical quantities use stored metric values. Area remains in square kilometers, and elevation and river distance remain in meters; the app does not convert them to US customary units. (`lib/db/src/schema/districts.ts:11-13`; `lib/db/src/schema/communities.ts:19-23`; `artifacts/api-server/src/routes/flood.ts:89-101`.)

## Inputs and outputs

- The browser requests JSON from the API under `/api`. The API reads the `districts`, `communities`, `infrastructure`, and `workflow_steps` PostgreSQL tables. (`artifacts/api-server/src/app.ts:28-33`; `artifacts/api-server/src/routes/flood.ts`; `artifacts/api-server/src/routes/health.ts`; `lib/db/src/schema/index.ts`.)
- `PATCH /api/communities/{id}` updates a community's `responseStatus` in PostgreSQL. (`artifacts/api-server/src/routes/flood.ts:257-299`; `lib/api-spec/openapi.yaml:142-176`.)
- The app has no file import or export flow in the inspected routes. Its rendered outputs are the browser views and JSON API responses.
- API operations are `GET /api/healthz`, `/api/dashboard/summary`, `/api/districts`, `/api/communities`, `/api/communities/{id}`, `/api/infrastructure`, `/api/priority-areas`, `/api/analytics/impact-distribution`, `/api/analytics/district-breakdown`, and `/api/workflow-steps`, plus the community `PATCH` route. (`lib/api-spec/openapi.yaml:26-263`.)

## Contents

- Browser views: 6 routes, including the community detail route. (`artifacts/flood-impact/src/App.tsx:20-26`.)
- Current development database: 5 districts, 30 communities, 22 infrastructure records, and 8 workflow-step records. Source: read-only `COUNT(*)` query on the development PostgreSQL database, run 2026-11-15; table definitions are in `lib/db/src/schema/{districts,communities,infrastructure,workflowSteps}.ts`.

## Checks

- `pnpm run typecheck`: passed on 2026-11-15.
- Local API check: each `GET` endpoint listed above returned HTTP 200 on 2026-11-15.
- Browser check: `/`, `/communities`, `/communities/1`, `/infrastructure`, `/analytics`, and `/workflow` loaded on 2026-11-15. No browser errors appeared; the console showed an informational React DevTools message.
- Human review: none recorded.

## What this does not show

1. Automated test execution was not checked or run. No test script was found in the inspected package manifests.
2. The development database counts do not establish production database contents. Production records were not checked.
3. Data provenance, the validity of the stored scores, coordinate accuracy, and agreement with observed flood outcomes were not checked.
4. No live satellite, geospatial, or simulation service integration was found in the inspected application code. The workflow view displays database descriptions; it does not demonstrate that those stages execute.
5. The community response-status `PATCH` was not exercised in this verification run.
6. The complete dependency license set was not audited, and no standalone `LICENSE` file was found at the project root.
7. The production URL was confirmed from deployment metadata, but its pages and API were not tested.

## How to reproduce

Configure `DATABASE_URL` for PostgreSQL, then run these commands from the project root:

```bash
pnpm install
pnpm --filter @workspace/db run push
pnpm --filter @workspace/api-server run dev
pnpm --filter @workspace/flood-impact run dev
pnpm run typecheck
```

The API and frontend development commands run as separate processes. The schema push command changes the configured development database. (`replit.md:5-13`; package scripts in `package.json`, `artifacts/api-server/package.json`, `artifacts/flood-impact/package.json`, and `lib/db/package.json`.)

## Credits and licenses

- Robert Dickinson: author named for this summary.
- Replit Agent: Git history attributes the application implementation and documentation commits to this author.
- The root package metadata declares MIT for this project (`package.json:4`). No standalone license text was found at the root.
- Primary library license metadata checked from installed package manifests: React and React DOM, MIT; Vite and `@vitejs/plugin-react`, MIT; Express, MIT; Drizzle ORM, Apache-2.0; TanStack Query, MIT; Recharts, MIT; Wouter, Unlicense; Lucide React, ISC; Tailwind CSS, MIT; TypeScript, Apache-2.0; Orval, MIT.
- The deployed app is hosted on Replit. Google Fonts is referenced by the web page (`artifacts/flood-impact/index.html:16-24`).

## AI use

The Git history attributes the application implementation commit and the documentation commit to Replit Agent. The inspected code and project documentation do not name another AI tool. Git history does not specify Robert Dickinson's individual implementation work. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-06-10: Added the README, getting-started guide, and tutorial. (`git log`, commit dated 2026-06-10.)
- 2026-05-31: Added the flood-impact application implementation. (`git log`, commit dated 2026-05-31.)
- 2026-05-31: Recorded an app publication. (`git log`, commit dated 2026-05-31.)
- 2026-05-28: Added the initial workspace scaffold. (`git log`, commit dated 2026-05-28.)
