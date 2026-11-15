---
name: SWMMCRAFT
file: swmm-infiltration--robertdickinson
version: 1.0.0
date: 2025-12-25
author: Robert Dickinson
links: {replit: "https://swmm-infiltration--robertdickinson.replit.app", repo: none}
engines: none
stack: TypeScript, React, Wouter, TanStack React Query, Tailwind CSS, Radix UI, Recharts, Express, PostgreSQL, Drizzle ORM, Vite, Replit hosting, Google Fonts
units: US customary
ai_use: The project records no AI contribution to the app source; see AI use.
---

# SWMMCRAFT: Simulate storm infiltration and runoff

## What it does

SWMMCRAFT estimates infiltration and runoff for a storm using Horton, Green-Ampt, or Curve Number methods (`client/src/pages/Simulator.tsx:287-293`). Users enter storm duration, time step, rainfall intensity, and method parameters in hours and inches (`shared/schema.ts:26-51`). The app returns time-step values and summary depths, with charts and a soil animation (`shared/schema.ts:56-70`; `client/src/pages/Simulator.tsx:451-465,529-562`). Users can save parameter sets and read a technical reference (`client/src/pages/Simulator.tsx:117-130`; `client/src/pages/Documentation.tsx:6-16`).

## How it computes

The browser sends JSON to `POST /api/calculate`. The server validates it with `calculateRequestSchema` and calls `runSimulation` (`client/src/hooks/use-calculate.ts:13-27`; `server/routes.ts:42-46`; `shared/schema.ts:46-52`).

`runSimulation` computes `steps = ceil(duration / timeStep)`, then loops from `i = 0` through `steps`. It uses constant rainfall intensity at each step and accumulates rainfall (`server/routes.ts:86-104`).

- **Horton:** potential rate = `minRate + (maxRate - minRate) * exp(-decay * time)`. The applied rate is capped at rainfall intensity (`server/routes.ts:106-115`).
- **Green-Ampt:** potential rate = `conductivity * (1 + suction * initialDeficit / F)`. `F` is cumulative infiltration, initialized to `0.0001` when it is zero. The applied rate is capped at rainfall intensity (`server/routes.ts:117-130`).
- **Curve Number:** `S = 1000 / CN - 10`; `Ia = 0.2 * S`; for `P > Ia`, `Q = (P - Ia)^2 / (P + 0.8 * S)`. The implementation sets cumulative infiltration to `P - Q` and derives the step rate from its change (`server/routes.ts:131-163,175-186`).

For Horton and Green-Ampt, cumulative infiltration increases by rate times time step. Runoff rate is the nonnegative difference between rainfall and infiltration rate. The response contains time-step results and totals (`server/routes.ts:170-205`).

The method-comparison chart computes all three method curves in the browser with similar formulas; it is separate from the selected server calculation (`client/src/components/ComparisonChart.tsx:24-67`). No external SWMM simulation engine is called by the code inspected.

## Inputs and outputs

- **Inputs:** Browser form values and JSON request bodies. No uploaded-file input is implemented (`client/src/pages/Simulator.tsx:255-446`; `shared/routes.ts:45-50`).
- **Outputs:** JSON calculation responses, interactive charts, a summary, and a soil cross-section animation. No file export is implemented (`shared/routes.ts:51-64`; `client/src/pages/Simulator.tsx:451-465,529-562`).
- **Pages:** `/` simulator, `/saved` saved models, and `/docs` technical reference (`client/src/App.tsx:13-21`).
- **API:** `GET /api/simulations`, `POST /api/simulations`, `DELETE /api/simulations/:id`, and `POST /api/calculate` (`shared/routes.ts:18-68`).
- **Storage:** PostgreSQL stores simulation name, description, method, JSON parameters, and creation time. Calculation results are returned by the API and are not part of the saved-model schema (`shared/schema.ts:6-13,56-70`; `server/storage.ts:13-25`).
- **External services:** Replit hosts the app. The page imports fonts from Google Fonts (`client/index.html:7-9`; `client/src/index.css:1`). Database connection configuration uses an environment variable; its value is not included here (`server/db.ts:8-15`).

## Contents

- Routed pages: 3, counted in `client/src/App.tsx:16-20`.
- Simulation methods: 3, listed in `shared/schema.ts:46-52`.
- Seed model definitions: 3, created if the database is empty in `server/routes.ts:58-78`.
- Saved records in the development app during this check: 3, returned by `GET /api/simulations` during this run.

## Checks

- `npm test`: no test script is configured in `package.json:6-11`; the command reported “Missing script: test.” No tests ran: 0 passed, 0 failed.
- `npm run check`: failed with 2 TypeScript errors. `client/src/hooks/use-calculate.ts:2` imports a `CalculateRequest` type that `shared/routes.ts` does not export. `client/src/pages/SavedModels.tsx:46` uses unsupported button variant `link`.
- Development page loads: `/`, `/saved`, and `/docs` each returned HTTP 200 and rendered in the browser at 1280 × 900. Browser logs contained Vite connection messages and the React DevTools information message, with no console errors.
- Calculation request: `POST /api/calculate` returned HTTP 200 for a Horton request with duration 1 hour, time step 0.5 hour, and rainfall intensity 1 inch/hour. It returned 3 rows and totals of 1.5 inches rainfall, 1.1921 inches infiltration, and 0.3079 inches runoff. These are results of this request, not independent accuracy validation.
- Human review: none recorded.

## What this does not show

1. The report does not establish engineering accuracy or suitability for design decisions. No human review is recorded.
2. iPhone layout, assistive-technology use, and accessibility behavior were not checked on a mobile device.
3. Production page behavior and production database contents were not checked. The page and saved-record checks used the development preview.
4. Rainfall is constant within a simulation; varying rainfall profiles and surface ponding are not inputs to the implemented calculation (`server/routes.ts:97-104,117-130`; `shared/schema.ts:46-52`).
5. The Horton implementation uses elapsed simulation time directly. Its source comment says it does not implement equivalent time for non-ponding periods (`server/routes.ts:106-112`).
6. The inclusive loop processes `steps + 1` rainfall increments. In the request recorded under Checks, a 1-hour duration with a 0.5-hour time step produced 1.5 inches of rainfall (`server/routes.ts:86-104`; calculation request recorded above).
7. The Curve Number reference page displays `Q = (P - Ia)^2 / (P - Ia + S)`, while the server uses denominator `P + 0.8 * S`. The displayed reference and implementation therefore differ (`client/src/pages/Documentation.tsx:238-242`; `server/routes.ts:145-147`).
8. The project does not record a release date for version 1.0.0. The front matter date uses the newest date in the inspected git log.

## How to reproduce

Run the development app with `npm run dev`. Run the available TypeScript check with `npm run check`. `npm test` is currently unconfigured. These scripts are listed in `package.json:6-11`; the app listens on the configured development port in `.replit:8-14`.

## Credits and licenses

- Robert Dickinson is the requested author. The inspected git history identifies `robertdickinson` as commit author.
- The project declares MIT in `package.json:5`; no separate root license file was present.
- EPA SWMM 5.2 and publications by EPA, Horton, Green and Ampt, USDA-NRCS, and Rawls et al. are cited in the technical reference. Their licenses are not stated in the project (`client/src/pages/Documentation.tsx:111,214,322,338-342`). These are references, not a bundled simulation engine.
- Direct package licenses below come from installed package metadata. Package names are declared in `package.json:13-110`. Transitive package licenses are not listed.
- **MIT:** `@hookform/resolvers`, `@jridgewell/trace-mapping`, all declared `@radix-ui/react-*` packages, `@tailwindcss/typography`, `@tailwindcss/vite`, `@tanstack/react-query`, all declared `@types/*` packages, `@vitejs/plugin-react`, `autoprefixer`, `bufferutil`, `clsx`, `cmdk`, `connect-pg-simple`, `date-fns`, `drizzle-kit`, `embla-carousel-react`, `esbuild`, `express`, `express-session`, `framer-motion`, `input-otp`, `memorystore`, `next-themes`, `passport`, `pg`, `postcss`, `react`, `react-day-picker`, `react-dom`, `react-hook-form`, `react-icons`, `react-resizable-panels`, `recharts`, `tailwind-merge`, `tailwindcss`, `tailwindcss-animate`, `tsx`, `tw-animate-css`, `vaul`, `vite`, `ws`, `zod`, and `zod-validation-error`.
- **Apache-2.0:** `class-variance-authority`, `drizzle-orm`, `drizzle-zod`, `typescript`.
- **ISC:** `lucide-react`.
- **Unlicense:** `wouter`.
- **License not stated in installed package metadata:** `@replit/vite-plugin-cartographer`, `@replit/vite-plugin-dev-banner`, `@replit/vite-plugin-runtime-error-modal`, and `passport-local`.
- Google Fonts is loaded remotely; its license is not stated in this project.

## AI use

The inspected source, configuration, documentation, and recent git history do not document an AI tool contributing to the app source. The Replit workflow configuration uses `author = "agent"` but does not attribute code changes (`.replit:23-38`). The inspected git history identifies Robert Dickinson as author but does not describe his individual contributions. No other AI tool is named in those records.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: the 10 newest entries from `git log`, newest first.

- 2025-12-25: Improve mobile responsiveness by collapsing the sidebar
- 2025-12-25: Improve the appearance and layout of the app on iPhones
- 2025-12-25: Published your App
- 2025-12-25: Saved progress at the end of the loop
- 2025-12-25: Optimize app layout and components for mobile viewing
- 2025-12-25: Published your App
- 2025-12-25: Update documentation with simulation details and system architecture
- 2025-12-25: Update app theme and add interactive infiltration simulation features
- 2025-12-25: Add interactive SWMM5 infiltration simulator with saved models
- 2025-12-25: Extracted stack files
