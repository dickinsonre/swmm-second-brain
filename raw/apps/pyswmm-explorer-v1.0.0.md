---
name: PySWMM Explorer
file: pyswmm-explorer
version: 1.0.0
date: 2026-02-11
author: Robert Dickinson
links: {replit: https://pyswmm-explorer.replit.app, repo: https://github.com/SWMMEnablement/pyswmm}
engines: none
stack: "TypeScript, React, Vite, Express, Tailwind CSS, Wouter, CodeMirror; in-memory server scaffold; Replit deployment; Google Fonts; no active database"
units: SI
ai_use: "No AI use for app development is recorded in the inspected project files."
---

# PySWMM Explorer: Interactive PySWMM reference and learning app

## What it does

The app helps Python and stormwater users look up PySWMM concepts, code examples, and project architecture. It presents API module notes, a searchable phrasebook, cookbook examples, ecosystem references, and a repository outline. The Playground and Parameter Explorer display illustrative results. They do not run the SWMM engine.

## How it computes

Most content is stored as TypeScript data in `client/src/lib/data.ts`. The application displays this content and does not calculate hydraulic model results.

`ParameterExplorer` in `client/src/pages/explorer.tsx` makes a synthetic hourly depth series. Its recurrence is `depth_next = max(0, depth + rain - drain - pumpDrain + noise)`. Rain is `0.4 * sin(((hour - 3) / 5) * pi)` for hours `3` through `8`; drainage is `0.08` when depth is positive; pump drainage is `0.15` above the pump-on threshold; random noise ranges from `-0.01` to `0.01`. Pump state uses the on and off thresholds and the previous state. These values are illustrative, not a calibrated model (`client/src/pages/explorer.tsx:150-173`).

`PlaygroundTab.simulateRun()` in `client/src/components/playground.tsx` uses a timer, a fixed depth pattern, and random variation to print sample console lines. It does not parse or execute the user's Python code. Its completion summary is hard-coded (`client/src/components/playground.tsx:236-288`).

No SWMM or Python simulation engine is bundled or called by this app (`client/src/components/playground.tsx:236-288`; `package.json:13-115`).

## Inputs and outputs

- The browser route `/` serves the explorer. Other paths use the not-found component (`client/src/App.tsx:10-16`).
- Users can edit sample Python text, adjust Parameter Explorer controls, search content, and change the theme (`client/src/components/playground.tsx`; `client/src/pages/explorer.tsx`; `client/src/components/theme-provider.tsx:13-32`).
- The app does not upload or read user model files, and it does not export files. It displays code and synthetic results.
- The theme is stored in browser `localStorage`. The Playground can copy code to the clipboard (`client/src/components/theme-provider.tsx:13-32`; `client/src/components/playground.tsx:304-313`).
- No API endpoints are registered (`server/routes.ts:5-15`). No database connection is used by the app. The server has an in-memory user storage scaffold, but the routes do not call it (`server/storage.ts:7-38`; `server/routes.ts:5-15`).
- External links point to the project repository, PySWMM documentation, JOSS, and PyPI (`client/src/pages/explorer.tsx:2403-2410`).

## Contents

Counts below were obtained by importing the current arrays in `client/src/lib/data.ts` with `npx tsx`.

- Ten tab views: Overview, API Modules, Architecture, Repository, Capabilities, Ecosystem, Phrasebook, Cookbook, Roadmap, and Playground (`client/src/pages/explorer.tsx:2435-2508`).
- Eight API modules and fifty cookbook examples (`client/src/lib/data.ts:23-1414`).
- Eight capability entries, five architecture layers, and six ecosystem entries (`client/src/lib/data.ts:1510-1555`).
- Sixty phrasebook entries in eight categories (`client/src/lib/data.ts:1557-1636`).
- Eight deep-dive entries (`client/src/lib/data.ts:1638-1791`).
- Five repository folders with thirty-six described files (`client/src/lib/data.ts:1416-1500`).
- Six header tags (`client/src/lib/data.ts:1784-1791`).

## Checks

- `npm run check`: passed. TypeScript reported no errors.
- `npm run build`: passed. The build emitted warnings about stale Browserslist data, a PostCSS plugin option, and a JavaScript chunk larger than the configured warning threshold.
- The root route `/` loaded in the app preview. The browser console showed Vite connection messages and a React DevTools information message, with no browser errors in the captured log.
- Human review: none recorded.

## What this does not show

1. Project tests are not checked. `package.json:6-12` has no test script, so no project test suite was run.
2. Individual tabs, their interactions, mobile layouts, and accessibility are not checked.
3. Real PySWMM code execution, `.inp` model loading, and model-specific results are not checked. The source shows synthetic output, not engine execution (`client/src/components/playground.tsx:236-288`).
4. External link destinations and their current content are not checked.
5. The app's source does not record a human review.
6. License terms for swmm-toolkit and EPA SWMM5 are not stated in the inspected project source.

## How to reproduce

- Install dependencies with `npm install`.
- Start the development app with `npm run dev` (`package.json:6-10`).
- Run the TypeScript check with `npm run check`.
- Build the app with `npm run build`.
- The configured deployment builds with `npm run build` and starts `node ./dist/index.cjs` (`.replit:15-18`).

## Credits and licenses

- Robert Dickinson is the requested author. The Git log attributes its listed recent commits to Robert Dickinson (`git log -10`).
- The app package declares MIT (`package.json:1-5`).
- The app displays BSD-2-Clause for the PySWMM project. Its repository browser describes a `LICENSE.txt` as BSD-2-Clause (`client/src/lib/data.ts:1490-1500,1784-1791`). The app links to `https://github.com/SWMMEnablement/pyswmm` (`client/src/pages/explorer.tsx:2403-2410`).
- The app names swmm-toolkit and EPA SWMM5 as parts of PySWMM's architecture; their license terms are not stated in the inspected source (`client/src/lib/data.ts:1527-1550`).
- Direct package licenses below were read from installed package manifests. `package.json` lists the project dependencies (`package.json:13-115`).
- MIT: `@codemirror/lang-python`, `@codemirror/state`, `@codemirror/theme-one-dark`, `@codemirror/view`, `@hookform/resolvers`, `@jridgewell/trace-mapping`, `@radix-ui/react-accordion`, `@radix-ui/react-alert-dialog`, `@radix-ui/react-aspect-ratio`, `@radix-ui/react-avatar`, `@radix-ui/react-checkbox`, `@radix-ui/react-collapsible`, `@radix-ui/react-context-menu`, `@radix-ui/react-dialog`, `@radix-ui/react-dropdown-menu`, `@radix-ui/react-hover-card`, `@radix-ui/react-label`, `@radix-ui/react-menubar`, `@radix-ui/react-navigation-menu`, `@radix-ui/react-popover`, `@radix-ui/react-progress`, `@radix-ui/react-radio-group`, `@radix-ui/react-scroll-area`, `@radix-ui/react-select`, `@radix-ui/react-separator`, `@radix-ui/react-slider`, `@radix-ui/react-slot`, `@radix-ui/react-switch`, `@radix-ui/react-tabs`, `@radix-ui/react-toast`, `@radix-ui/react-toggle`, `@radix-ui/react-toggle-group`, `@radix-ui/react-tooltip`, `@tanstack/react-query`, `clsx`, `cmdk`, `codemirror`, `connect-pg-simple`, `date-fns`, `embla-carousel-react`, `express`, `express-session`, `framer-motion`, `input-otp`, `memorystore`, `next-themes`, `passport`, `pg`, `react`, `react-day-picker`, `react-dom`, `react-hook-form`, `react-icons`, `react-resizable-panels`, `recharts`, `tailwind-merge`, `tailwindcss-animate`, `tw-animate-css`, `vaul`, `ws`, `zod`, `zod-validation-error`, `@tailwindcss/typography`, `@tailwindcss/vite`, `@types/connect-pg-simple`, `@types/express`, `@types/express-session`, `@types/node`, `@types/passport`, `@types/passport-local`, `@types/react`, `@types/react-dom`, `@types/ws`, `@vitejs/plugin-react`, `autoprefixer`, `drizzle-kit`, `esbuild`, `postcss`, `tailwindcss`, `tsx`, `vite`, and `bufferutil`.
- Apache-2.0: `class-variance-authority`, `drizzle-orm`, `drizzle-zod`, and `typescript`.
- ISC: `lucide-react`.
- Unlicense: `wouter`.
- License not stated in the installed package manifest: `passport-local`, `@replit/vite-plugin-cartographer`, `@replit/vite-plugin-dev-banner`, and `@replit/vite-plugin-runtime-error-modal`.
- Google Fonts is loaded by the page. Font-specific license terms were not checked (`client/index.html:9-10`).

## AI use

The inspected app source and project documentation do not identify AI tools used to build the app. The Git log attributes its listed recent changes to Robert Dickinson. Those entries include Playground work, publication, roadmap, and documentation updates (`git log -10`). The project record does not establish whether Robert used other tools.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

From `git log -10 --date=short`, newest first:

- 2026-03-08: Added improvement ideas and roadmap to the handover document.
- 2026-03-08: Added a detailed handover document.
- 2026-03-08: Updated project documentation.
- 2026-03-08: Updated the handover document.
- 2026-03-06: Published the app.
- 2026-03-06: Improved Playground interactions and code loading.
- 2026-03-06: Added the interactive Playground.
- 2026-03-05: Published the app.
- 2026-03-05: Added a roadmap tab.
- 2026-02-11: Published the app.
