---
name: SWMM5 INP MAKER
file: swmm-inp-maker
version: 1.0.0
date: 2026-07-20
author: Robert Dickinson
links: {replit: https://swmm-inp-maker.replit.app, repo: none}
engines:
  - {name: "EPA SWMM5", version: "5.2.4", source: "local compiled binary; upstream URL not recorded", commit: "not recorded", license: "not stated"}
stack: TypeScript, React, Vite, Tailwind CSS, Node.js, Express, JSZip, in-memory storage, Replit hosting, Google Fonts
units: both
ai_use: Replit Agent is named in recent Git history; details under AI use
---

# SWMM5 INP MAKER: Generate and inspect SWMM5 input models

## What it does

The app creates SWMM5 `.inp` model files from network, terrain, hydrology, and unit settings. It is for people who need a configurable starting model or want to inspect an existing input file. It displays model statistics and network/profile views, and includes static validation, file transformation, discretization, and simulation features. The generated input can be downloaded or passed to the API.

## How it computes

1. `compute(config)` in `client/src/lib/swmm-engine.ts:669-689` calculates element counts from the requested junction count and type-specific ratios. For example: `conduits = max(N, round(N * conduitRatio))`.
2. `getSections(elems, config)` in `client/src/lib/swmm-engine.ts:691-711` selects required INP sections and adds optional sections according to configuration flags.
3. `generateModel(config)` in `client/src/lib/swmm-engine.ts:1087-1094` chooses the supplied seed or generates one, then initializes the Mulberry32 random-number generator in `client/src/lib/prng.ts:1-14`. The default generation method is `force_directed`; other methods are defined in `client/src/lib/generators.ts`. The generator assigns model properties and writes the INP sections in `client/src/lib/swmm-engine.ts`.
4. `validateInp(inpContent, autoFix)` in `client/src/lib/inp-validator.ts:55-109` performs static checks and can repair supported issues. Its engine-validation stage is skipped; it is not a SWMM simulation.
5. Server simulation routes call the local `swmm5` executable with temporary `.inp`, `.rpt`, and `.out` paths using `execFile` in `server/routes.ts:427-492`. Full mode uses the INP event dates; quick mode patches the dates for a one-minute structural run (`server/routes.ts:28-88`). The configured time limits are 120 seconds for full mode and 60 seconds for quick mode (`server/routes.ts:28-30`).

## Inputs and outputs

- The browser accepts SWMM `.inp` files for viewing and validation with `FileReader` (`client/src/components/inp-viewer.tsx:1048-1061`). Generation settings include network type, terrain, US or SI units, seed, hydrology, and optional SWMM sections (`client/src/lib/swmm-engine.ts:93-122`).
- The API accepts JSON configuration or INP text. Routes include `/api/generate`, `/api/generate-and-simulate`, `/api/simulate`, `/api/validate`, `/api/transform`, `/api/bulk-generate`, `/api/presets`, `/api/rainfall-patterns`, `/api/sections`, `/api/config-schema`, `/api/info`, and `/api/docs` (`server/routes.ts:234-267,311-343,345-425,427-568,569-764`).
- Outputs include `.inp` text or downloads; simulation reports; and, for bulk generation, a ZIP containing INP files and `summary.csv`, with reports when simulations produce them (`server/routes.ts:322-337,385-421,663-757`).
- Generated content is held in browser or request memory. Simulation files are created in temporary directories and removed after processing (`server/routes.ts:358-366,413-418,439-447`). Theme and onboarding preferences use browser storage (`client/src/components/theme-provider.tsx`, `client/src/components/onboarding.tsx`). The model data is not stored in a database. `server/storage.ts:13-38` defines an in-memory user store.
- Google Fonts are requested by `client/index.html:14-16`. No external API credentials are included here.

## Contents

- Main React route: `/`, with a not-found fallback (`client/src/App.tsx:10-16`). API documentation is served at `/api/docs` (`server/routes.ts:234-236`).
- Example presets: 38, counted from the running `GET /api/presets` response and defined in `client/src/lib/swmm-engine.ts:340-587`.
- Rainfall patterns: 276, from the running `GET /api/rainfall-patterns` response (`server/routes.ts:627-643`).
- INP sections: 56, from the running `GET /api/sections` response and the `ALL_SECTIONS` list (`client/src/lib/swmm-engine.ts:291-302`, `server/routes.ts:646-660`).

## Checks

- `GET /` and `GET /api/docs` each returned HTTP 200 on the local development server. The root browser capture showed the onboarding screen. Available browser output contained Vite connection and React DevTools informational messages, with no reported browser errors.
- API smoke run: generation with seed `321`, validation, transformation, and quick simulation each returned HTTP 200. Generation returned an INP model, validation reported valid with no errors, and quick simulation reported success. These were one-off requests to the local development server, not a test suite.
- Automated tests: no project test command or test files were found in the application directories. Test suite: 0 passed, 0 failed, 0 run. No test command is available to reproduce.
- TypeScript check: `npm run check -- --pretty false` failed with 30 TypeScript errors, including target-related errors for `Set` iteration and regular-expression flags.
- Human review: none recorded.

## What this does not show

1. Production pages and API: not checked. These page and API checks used the local development server.
2. Browser interactions beyond the initial onboarding screen: not checked.
3. Automated tests: not checked because the project has no test command or test files in the checked application directories.
4. The SWMM executable's upstream source URL, commit, and license are not recorded in the project and were not checked independently. The version is identified as 5.2.4 in `server/routes.ts:238-243` and by the binary's embedded version string.
5. Human engineering review or certification: not checked; none was recorded in the project.
6. Package license expressions below come from installed package metadata. License texts and transitive dependency licenses were not independently audited.

## How to reproduce

- Start the development app: `npm run dev` (`package.json:6-11`).
- Run the TypeScript check: `npm run check -- --pretty false` (`package.json:6-11`).
- No automated test command is defined in `package.json`.
- The deployment configuration builds with `npm run build` and starts with `node ./dist/index.cjs` (`.replit:17-23`).

## Credits and licenses

- `ReSWMM.md` credits Robert Dickinson for porting ReSWMM and names Robson Leo Pachaly as ReSWMM's original author. ReSWMM's license is not stated there.
- The app package declares MIT (`package.json:1-5`). No root `LICENSE` file was found.
- EPA SWMM5 is identified by the project as version 5.2.4. Its upstream source, commit, and license are not stated in the project.
- Runtime dependencies, by package metadata license:
  - MIT: `@hookform/resolvers`, `@jridgewell/trace-mapping`, `@radix-ui/react-accordion`, `@radix-ui/react-alert-dialog`, `@radix-ui/react-aspect-ratio`, `@radix-ui/react-avatar`, `@radix-ui/react-checkbox`, `@radix-ui/react-collapsible`, `@radix-ui/react-context-menu`, `@radix-ui/react-dialog`, `@radix-ui/react-dropdown-menu`, `@radix-ui/react-hover-card`, `@radix-ui/react-label`, `@radix-ui/react-menubar`, `@radix-ui/react-navigation-menu`, `@radix-ui/react-popover`, `@radix-ui/react-progress`, `@radix-ui/react-radio-group`, `@radix-ui/react-scroll-area`, `@radix-ui/react-select`, `@radix-ui/react-separator`, `@radix-ui/react-slider`, `@radix-ui/react-slot`, `@radix-ui/react-switch`, `@radix-ui/react-tabs`, `@radix-ui/react-toast`, `@radix-ui/react-toggle`, `@radix-ui/react-toggle-group`, `@radix-ui/react-tooltip`, `@tanstack/react-query`, `clsx`, `cmdk`, `connect-pg-simple`, `date-fns`, `embla-carousel-react`, `express`, `express-session`, `framer-motion`, `input-otp`, `memorystore`, `next-themes`, `passport`, `pg`, `react`, `react-day-picker`, `react-dom`, `react-hook-form`, `react-icons`, `react-resizable-panels`, `recharts`, `tailwind-merge`, `tailwindcss-animate`, `tw-animate-css`, `vaul`, `ws`, `zod`, and `zod-validation-error`.
  - Apache-2.0: `class-variance-authority`, `drizzle-orm`, and `drizzle-zod`.
  - ISC: `lucide-react`.
  - Unlicense: `wouter`.
  - MIT or GPL-3.0-or-later: `jszip`.
  - No license field in the installed package metadata: `passport-local`.
- Build and development dependencies, by package metadata license:
  - MIT: `@tailwindcss/typography`, `@tailwindcss/vite`, `@types/connect-pg-simple`, `@types/express`, `@types/express-session`, `@types/node`, `@types/passport`, `@types/passport-local`, `@types/react`, `@types/react-dom`, `@types/ws`, `@vitejs/plugin-react`, `autoprefixer`, `drizzle-kit`, `esbuild`, `postcss`, `tailwindcss`, `tsx`, and `vite`.
  - Apache-2.0: `typescript`.
  - No license field in the installed package metadata: `@replit/vite-plugin-cartographer`, `@replit/vite-plugin-dev-banner`, and `@replit/vite-plugin-runtime-error-modal`.

## AI use

The recent Git history names Replit Agent as the author of the listed commits. Those entries do not identify which implementation details were AI-generated. The checked project files do not name other AI tools or record a task-by-task division of work. `ReSWMM.md` credits Robert Dickinson with the ReSWMM port.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-07-20: Correctness pass for Release 1.
- 2026-07-20: Transitioned from planning to build.
- 2026-07-20: Published the app.
- 2026-07-19: Published the app.
- 2026-07-19: Updated workflow step indicators.
- 2026-07-18: Added step letters to the workflow.
