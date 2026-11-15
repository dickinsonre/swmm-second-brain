---
name: OpenSWMM Engine
file: open-swmm-core
version: 6.0.0-alpha.1
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://open-swmm-core.replit.app, repo: https://github.com/HydroCouple/OpenSWMMCore}
engines:
  - {name: OpenSWMMCore legacy SWMM solver (WebAssembly), version: "Legacy SWMM 5.x; app release 6.0.0-alpha.1", source: "HydroCouple/OpenSWMMCore, swmm6_rel branch", commit: not recorded, license: "MIT; original EPA SWMM material is stated as public domain"}
stack: TypeScript, React, Vite, WebAssembly, Tailwind CSS, Recharts, marked, highlight.js, Google Fonts; no database or API service
units: both
ai_use: No AI-tool authorship is recorded in the source or documentation
---

# OpenSWMM Engine: Explore and run SWMM stormwater models in a browser

## What it does

OpenSWMM Engine introduces the OpenSWMM project and provides a technical documentation view and an in-browser simulator. The simulator accepts SWMM input text or files, previews a network map, and runs the included legacy SWMM engine compiled to WebAssembly. It presents the run report as raw text, parsed tables, and time-series graphs. The displayed project release is 6.0.0-alpha.1, and the feature page identifies EPA SWMM 5.2.4 as its legacy baseline (features.tsx:106-110, 152-157).

## How it computes

1. The user uploads or pastes an `.inp` model, or selects a bundled sample (simulator.tsx:25-32, 52-80, 200-206).
2. `parseInpForMap` reads coordinates and model sections to construct node, link, and subcatchment geometry for the map. It does not calculate hydraulic results (inp-map-parser.ts:31-44, 51-69, 72-178).
3. `runSwmmSimulation` loads the compiled WebAssembly module and writes the input text to its virtual filesystem as `/input.inp` (swmm-wasm.ts:32-58, 86-125).
4. When the step API is available, `runWithSteps` calls `swmm_open`, `swmm_start`, repeatedly calls `swmm_step`, then calls `swmm_end`, `swmm_report`, and `swmm_close`. The SWMM engine performs the hydraulic and hydrologic calculations; this web app does not implement separate solver equations (swmm-wasm.ts:128-225).
5. The app reads the generated report. `parseRptSections` extracts tables and `extractTimeSeries` extracts values for graphs (rpt-parser.ts:16-40, 145-188; simulator.tsx:112-123, 283-390).

## Inputs and outputs

- Inputs: `.inp` or `.txt` files, pasted input text, and bundled `.inp` samples (simulator.tsx:25-32, 189-206).
- Outputs shown in the browser: network map, raw `.rpt` report, parsed tables, and graphs (simulator.tsx:252-280, 283-390).
- The engine creates `/output.rpt` and `/output.out` in its WebAssembly virtual filesystem, reads the report for display, then removes temporary files. The app does not offer a report or binary-output download (swmm-wasm.ts:141, 208-214, 262-266).
- No database or application API endpoint is used by this web artifact. Dark-mode preference is stored in browser `localStorage` (artifact.toml:12-23; use-dark-mode.ts:3-16).

## Contents

- 3 app views: Features, Documentation, and Simulator (App.tsx:6-19).
- 6 bundled sample models (simulator.tsx:25-32; files under `public/samples/`).
- 11 top-level documentation chapters, counted from the Markdown headings in `src/content/how-openswmm-works.ts` (headings at lines 9-448).
- No server-side model or user records are defined in this artifact (artifact.toml:12-23).

## Checks

- TypeScript check: passed with `pnpm --filter @workspace/openswmm-engine run typecheck`.
- Production build: passed with `PORT=18532 BASE_PATH=/ pnpm --filter @workspace/openswmm-engine run build`. Vite reported a main JavaScript chunk of 730.06 kB and an advisory threshold of 500 kB.
- Browser smoke check: loaded Features, Documentation, and Simulator in Chromium. All 3 views appeared, with 0 browser errors during the run.
- Simulation smoke check: the bundled User1 sample completed with a Success status in the browser.
- File requests: the app page and all 6 bundled sample files returned HTTP 200.
- Automated tests: no test script or app test suite was found, so no automated test count is available.
- Human review: none recorded.

## What this does not show

1. Only the User1 sample was run through the simulator. The other sample models were fetched successfully but not simulated, and results were not compared with an independent reference.
2. Mobile-browser behavior, accessibility, and performance on large models were not checked.
3. The WebAssembly build script clones the `swmm6_rel` branch without recording a source commit; the exact source revision used for the checked-in binary is not recorded (scripts/build-wasm.sh:10-17, 40).
4. The build emits a large-chunk advisory; its effect on real-world load times was not measured.
5. No person’s review of this summary or independent engineering review is recorded.

## How to reproduce

From the workspace root:

```sh
pnpm install
PORT=18532 BASE_PATH=/ pnpm --filter @workspace/openswmm-engine run dev
```

Run the checks:

```sh
pnpm --filter @workspace/openswmm-engine run typecheck
PORT=18532 BASE_PATH=/ pnpm --filter @workspace/openswmm-engine run build
```

There is no automated test command in this app package.

## Credits and licenses

- OpenSWMMCore and HydroCouple: the app identifies the project as MIT licensed. The original EPA SWMM material is stated to be public domain under 17 USC § 105 (features.tsx:303-307; how-openswmm-works.ts:660-664).
- EPA SWMM and Lewis A. Rossman: acknowledged as the originating project and author in the project documentation (how-openswmm-works.ts:660-664).
- React and React DOM (MIT), Vite (MIT), TypeScript (Apache-2.0), Recharts (MIT), marked (MIT), highlight.js (BSD-3-Clause), and Tailwind CSS (MIT). Package names are listed in `artifacts/openswmm-engine/package.json`; license identifiers were read from installed package metadata.
- Google Fonts supplies the Inter font used by the page (index.html:8-10).
- No license file is present in the app artifact directory.

## AI use

The source and documentation do not record which AI tools, if any, built the app, or what Robert Dickinson contributed. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Latest 10 entries from `git log`, newest first:

- 2026-03-27: Update simulation engine to use OpenSWMMCore for building the WebAssembly module
- 2026-03-27: Add information about SWMM 6 and update styling for progress bar
- 2026-03-26: Add progress monitor and improve simulation execution
- 2026-03-26: Published your App
- 2026-03-26: Add interactive network map to visualize simulation input files
- 2026-03-26: Add multiple sample models to the simulator
- 2026-03-26: Add in-browser SWMM simulator for running WASM models
- 2026-03-26: Published your App
- 2026-03-26: Introduce a new features landing page and improve navigation
- 2026-03-26: Add dark mode toggle to the documentation sidebar
