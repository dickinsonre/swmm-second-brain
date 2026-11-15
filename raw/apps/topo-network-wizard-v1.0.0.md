---
name: SWMM5 Topo Network Wizard
file: topo-network-wizard
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://topo-network-wizard.replit.app, repo: none}
engines:
  - {name: Topology network generator, version: not separately versioned, source: client/src/lib/topology-generators.ts, commit: not separately versioned, license: project package declares MIT}
  - {name: Lenia particle simulator, version: not separately versioned, source: client/src/lib/lenia-engine.ts, commit: not separately versioned, license: project package declares MIT}
  - {name: Hydraulic analysis calculator, version: not separately versioned, source: client/src/lib/hydraulic-engine.ts, commit: not separately versioned, license: project package declares MIT}
stack: TypeScript, React, Vite, Express, PostgreSQL, Drizzle ORM, Zustand, d3-delaunay
units: both
ai_use: Project records do not identify AI tools used to build the app.
---

# SWMM5 Topo Network Wizard: Browser-based stormwater network generation and export

## What it does

The app lets users generate and inspect stormwater drainage network layouts from topology methods and configurable node and pipe parameters. It animates particle layouts, assigns elevations, estimates catchments and hydraulic values, and reports network statistics. It exports SWMM5 input files and several geometry or image formats. The project source does not show an external EPA SWMM executable or service being run.

## How it computes

1. The topology selector chooses a method-specific generator. An optional seed initializes a deterministic pseudorandom function; the selected generator returns particles (client/src/lib/topology-generators.ts:3-20, 2418-2479).
2. The particle engine evaluates pairwise distance, a Gaussian interaction kernel, a growth function, and short-range repulsion. It updates positions from velocity and the time step, reflecting particles from canvas boundaries (client/src/lib/lenia-engine.ts:47-80, 82-126, 127-156).
3. Link generation groups particles in a spatial hash, checks nearby candidates within the configured connection radius, sorts by distance, and selects up to three neighbors per particle. Link direction follows elevation, and duplicate links are discarded (client/src/lib/lenia-engine.ts:158-240).
4. Freezing the layout assigns elevations by traversing link distances from an outfall. Delaunay triangulation creates clipped Voronoi cells for subcatchments; their areas are computed from polygon vertices (client/src/lib/hydraulic-engine.ts:32-78, 80-168; client/src/pages/home.tsx:179-200).
5. The hydraulic calculator estimates runoff as runoff coefficient times rainfall intensity times catchment area, accumulates flow along a shortest-distance tree, and estimates conduit capacity from area, hydraulic radius, roughness, and slope. It reports peak outlet flow, pipe utilization, flooding nodes, runoff volume, and time of concentration (client/src/lib/hydraulic-engine.ts:170-320).
6. The export dialog assembles SWMM sections for nodes, conduits, subcatchments, rainfall, and related data. It creates files in the browser; it does not run those files through SWMM (client/src/components/lenia-export-dialog.tsx:136-290; client/src/lib/hydraulic-engine.ts:336-469).

## Inputs and outputs

- Inputs: topology method, node count, seed, connection and particle parameters, project name, and USA or SI units. The node slider accepts 3 to 1,000 nodes (client/src/components/lenia-controls.tsx:785-797). Permalinks encode the method, node count, seed, selected parameters, and units in the URL query (client/src/components/lenia-controls.tsx:357-399).
- Units: USA mode uses feet, square feet, cubic feet per second, and feet per second. SI mode uses meters, square meters, cubic meters per second, and meters per second (client/src/lib/lenia-store.ts:6-27).
- Downloads: SWMM `.inp`, GeoJSON, DXF, SVG, and PNG. The INP can also be copied to the clipboard (client/src/components/lenia-export-dialog.tsx:452-470, 536-590).
- HTTP API: `GET /api/projects`, `GET /api/projects/:id`, `POST /api/projects`, `PATCH /api/projects/:id`, and `DELETE /api/projects/:id` (server/routes.ts:12-77).
- Saved projects are stored in PostgreSQL. Project rows contain a name, description, node data, link data, and timestamps (server/db.ts:1-13; shared/schema.ts:80-100).
- The browser stores up to five recent network-history entries under `topo-swmm-history`; current simulation state is held in the client store (client/src/lib/lenia-store.ts:47-73, 99-116, 118-133, 171-194).

## Contents

- One application page is routed at `/`, with a not-found fallback for other paths (client/src/App.tsx:10-15).
- The source defines 49 topology method identifiers and 8 categories (client/src/lib/topology-generators.ts:23-82, 132-141).
- The source defines 10 scenario presets (client/src/lib/topology-generators.ts:112-123).
- Five export formats are exposed in the download menu (client/src/components/lenia-export-dialog.tsx:550-590).
- Five project API operations are registered (server/routes.ts:12-77).
- The version is `1.0.0` in package.json:1-5. The app version is not recorded separately for its engines.

## Checks

- `npm run build`: passed on 2026-11-15. Vite built the client and esbuild built the server. The build emitted dependency-age, PostCSS, and bundle-size warnings.
- `npm run check`: failed with 4 TypeScript errors in 2 files. Both files report missing declarations for `d3-delaunay`; the hydraulic file also has 2 implicit-`any` errors for Voronoi vertex coordinates (client/src/components/lenia-canvas.tsx:2; client/src/lib/hydraulic-engine.ts:1, 60).
- Browser preview: `/` loaded. No app errors were captured in the browser console; the captured messages were Vite connection and React DevTools information.
- Automated tests: no test script is configured in package.json, and no first-party test or spec files were found in `client`, `server`, `shared`, or `script`.
- Human review: none recorded.

## What this does not show

1. The generated INP was not opened or run in EPA SWMM, so SWMM compatibility and simulation results were not independently verified.
2. Hydraulic estimates, rainfall assumptions, unit conversions, and exported engineering values were not compared with an authoritative model or hand calculation.
3. Project API operations and database persistence were not exercised. Production database contents were not checked.
4. The browser check covered the main page only. Dialogs, downloads, parameter interactions, and the not-found route were not tested.
5. The published URL was obtained from deployment metadata, but its live page was not tested during this summary.
6. The schema includes a users table, but the storage methods for users return placeholders; user management was not tested (shared/schema.ts:102-113; server/storage.ts:18-30).
7. The project files do not record which AI tools built the app or what work Robert Dickinson performed.

## How to reproduce

```bash
npm ci
npm run dev
npm run build
npm start
npm run check
```

`npm start` serves the production build after `npm run build`. No test command is defined (package.json:6-12).

## Credits and licenses

- Robert Dickinson is the named author for this summary.
- The project package metadata declares MIT. No root `LICENSE` file was present.
- Runtime and development dependency names are listed in package.json. Installed package metadata reports these licenses:
  - MIT: `@hookform/resolvers`, `@jridgewell/trace-mapping`, `@radix-ui/react-accordion`, `@radix-ui/react-alert-dialog`, `@radix-ui/react-aspect-ratio`, `@radix-ui/react-avatar`, `@radix-ui/react-checkbox`, `@radix-ui/react-collapsible`, `@radix-ui/react-context-menu`, `@radix-ui/react-dialog`, `@radix-ui/react-dropdown-menu`, `@radix-ui/react-hover-card`, `@radix-ui/react-label`, `@radix-ui/react-menubar`, `@radix-ui/react-navigation-menu`, `@radix-ui/react-popover`, `@radix-ui/react-progress`, `@radix-ui/react-radio-group`, `@radix-ui/react-scroll-area`, `@radix-ui/react-select`, `@radix-ui/react-separator`, `@radix-ui/react-slider`, `@radix-ui/react-slot`, `@radix-ui/react-switch`, `@radix-ui/react-tabs`, `@radix-ui/react-toast`, `@radix-ui/react-toggle`, `@radix-ui/react-toggle-group`, `@radix-ui/react-tooltip`, `@tanstack/react-query`, `clsx`, `cmdk`, `connect-pg-simple`, `date-fns`, `embla-carousel-react`, `express`, `express-session`, `framer-motion`, `input-otp`, `memorystore`, `next-themes`, `passport`, `pg`, `react`, `react-day-picker`, `react-dom`, `react-hook-form`, `react-icons`, `react-resizable-panels`, `recharts`, `tailwind-merge`, `tailwindcss-animate`, `tw-animate-css`, `vaul`, `ws`, `zod`, `zod-validation-error`, `zustand`, `@tailwindcss/typography`, `@tailwindcss/vite`, `@types/connect-pg-simple`, `@types/express`, `@types/express-session`, `@types/node`, `@types/passport`, `@types/passport-local`, `@types/react`, `@types/react-dom`, `@types/ws`, `@vitejs/plugin-react`, `autoprefixer`, `drizzle-kit`, `esbuild`, `postcss`, `tailwindcss`, `tsx`, `vite`, `bufferutil`.
  - Apache-2.0: `class-variance-authority`, `drizzle-orm`, `drizzle-zod`, `typescript`.
  - ISC: `d3-delaunay`, `lucide-react`.
  - Unlicense: `wouter`.
  - License not declared in installed package metadata: `passport-local`, `@replit/vite-plugin-cartographer`, `@replit/vite-plugin-dev-banner`, `@replit/vite-plugin-runtime-error-modal`.
- Space Grotesk and JetBrains Mono are loaded from Google Fonts (client/index.html:11-13). Their licenses were not checked in this project.

## AI use

No AI tools used to build the app are recorded in the project files inspected. The project files do not describe Robert Dickinson's contributions. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-03-16: Update documentation on network generation and hydraulic analysis features
- 2026-03-16: Improve network generation and analysis capabilities
- 2026-03-16: Create comprehensive documentation for the topology network generator tool
- 2026-02-07: Improve network visualization and add export validation checks
- 2026-02-07: Add reproducible network generation and improved hydraulic analysis
- 2026-02-07: Add hydraulic analysis and enhanced export capabilities

Source: `git log`, newest relevant changes first. The current uncommitted summary is not represented in the log.
