---
name: OpenSWMM Engine
file: open-swmm-core
version: 6.0.0-alpha.2
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://open-swmm-core.replit.app, repo: https://github.com/HydroCouple/OpenSWMMCore}
engines:
  - {name: OpenSWMMCore legacy SWMM solver (WebAssembly), version: "Legacy SWMM 5.3.0; app release 6.0.0-alpha.2", source: "HydroCouple/OpenSWMMCore", commit: "87664bf518104e618f0537340b9500a1fdfe797c", license: "Apache-2.0 for OpenSWMM contributions; USEPA SWMM portions are public domain"}
stack: TypeScript, React, Vite, WebAssembly, Tailwind CSS, Recharts, marked, highlight.js, Google Fonts; no database or API service
units: both
ai_use: No AI-tool authorship is recorded in the source or documentation
---

# OpenSWMM Engine: Explore and run SWMM stormwater models in a browser

## What it does

OpenSWMM Engine introduces the OpenSWMM project and provides a technical documentation view and an in-browser simulator. The simulator accepts SWMM input text or files, previews a network map, and runs the included legacy SWMM engine compiled to WebAssembly. It presents the run report as raw text, parsed tables, and time-series graphs. The app release shown in the interface is 6.0.0-alpha.2.

## How it computes

1. The user uploads or pastes a `.inp` model, or selects a bundled sample (`src/pages/simulator.tsx`).
2. `parseInpForMap` reads coordinates and model sections to construct node, link, and subcatchment geometry for the map. It does not calculate hydraulic results (`src/lib/inp-map-parser.ts`).
3. `runSwmmSimulation` loads the compiled WebAssembly module and writes the input text to its virtual filesystem as `/input.inp` (`src/lib/swmm-wasm.ts`).
4. When the step API is available, `runWithSteps` calls `swmm_open`, `swmm_start`, repeatedly calls `swmm_step`, then calls `swmm_end`, `swmm_report`, and `swmm_close`. The SWMM engine performs the hydraulic and hydrologic calculations; this web app does not implement separate solver equations.
5. The app reads the generated report. `parseRptSections` extracts tables and `extractTimeSeries` extracts values for graphs (`src/lib/rpt-parser.ts`).

## Inputs and outputs

- Inputs: `.inp` or `.txt` files, pasted input text, and bundled `.inp` samples.
- Outputs shown in the browser: network map, raw `.rpt` report, parsed tables, and graphs.
- The engine creates `/output.rpt` and `/output.out` in its WebAssembly virtual filesystem, reads the report for display, then removes temporary files. The app does not offer a report or binary-output download.
- No database or application API endpoint is used by this web artifact. Dark-mode preference is stored in browser `localStorage`.

## Contents

- 3 app views: Features, Documentation, and Simulator.
- 6 bundled sample models.
- 11 top-level documentation chapters in `src/content/how-openswmm-works.ts`.
- No server-side model or user records are defined in this artifact.

## Checks

- Source provenance: `git rev-parse HEAD` in the fetched source checkout matched `ENGINE_SOURCE.txt`.
- Legal files: `LICENSE` and `NOTICE` matched the corresponding files at the pinned commit byte-for-byte; the same was checked for the app copies.
- WebAssembly build: `bash artifacts/openswmm-engine/scripts/build-wasm.sh` passed using a fresh Emscripten cache and the pinned source commit. The compiler emitted two ignored `#pragma float_control` warnings from upstream `mathexpr.c`.
- Simulation smoke check: the bundled User1 sample completed in the rebuilt WebAssembly engine with exit code 0 and a 66,945-character report.
- TypeScript check: passed with `pnpm --filter @workspace/openswmm-engine run typecheck`.
- Production build: passed with `PORT=18532 BASE_PATH=/ pnpm --filter @workspace/openswmm-engine run build`. Vite reported a 734.08 kB main JavaScript chunk and its advisory 500 kB threshold.
- Browser preview: the Features page rendered the alpha.2 badge, pinned commit, distinct engine/app license statements, attribution names, license links, and full NOTICE. No browser errors were reported.
- HTTP checks: the preview page, local Apache license, and WebAssembly loader returned HTTP 200.
- Automated test suite: no app test script was found; no suite was run.
- Publication: the app has not yet been republished. Publishing is waiting for the user's action.

## What this does not show

1. The other five bundled sample models were not run, and results were not compared with an independent reference.
2. The newly prepared build has not been checked at the public deployment URL because it has not yet been republished.
3. Mobile-browser behavior, accessibility, and performance on large models were not checked.
4. No independent legal or engineering review is recorded.

## How to reproduce

From the workspace root:

```sh
pnpm install
PORT=18532 BASE_PATH=/ pnpm --filter @workspace/openswmm-engine run dev
```

To rebuild the WebAssembly engine from the pinned source:

```sh
bash artifacts/openswmm-engine/scripts/build-wasm.sh
```

Run the app checks:

```sh
pnpm --filter @workspace/openswmm-engine run typecheck
PORT=18532 BASE_PATH=/ pnpm --filter @workspace/openswmm-engine run build
```

There is no automated test command in this app package.

## Credits and licenses

- OpenSWMM Engine: “OpenSWMM Engine, Copyright 2026 HydroCouple Developers, licensed under the Apache License, Version 2.0. Portions derive from USEPA SWMM, which is in the public domain under 17 USC 105. The USEPA does not endorse this product.”
- The bundled engine source is pinned to commit `87664bf518104e618f0537340b9500a1fdfe797c` of `HydroCouple/OpenSWMMCore`; the app displays a link to that commit. `artifacts/openswmm-engine/ENGINE_SOURCE.txt` records the SHA.
- Root `LICENSE` and `NOTICE` are unchanged copies from that commit. Their SHA-256 checksums are `94fcde3f05aad351a969a65f5c87b25ee3893ee7297549d6a3217bf29ccbc3aa` and `83a3c0524ba9dd6929a5d5e110f959d318ce142ffbc2cce74616bf5866b1d5cb`. The app's copies match the root files, and the complete NOTICE is displayed in the Features page.
- The full Apache-2.0 license is linked from the Credits & Licenses section.
- OpenSWMM credits Caleb Buahin (lead developer) and Corinne Wiesner-Friedman (developer, documentation). EPA SWMM and Lewis A. Rossman are also credited for the foundational model.
- This app's code: MIT, Copyright 2026 Robert Dickinson.
- No upstream engine C source files were modified during the WebAssembly build.

## AI use

The source and documentation do not record which AI tools, if any, built the app, or what Robert Dickinson contributed. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Latest 10 entries from `git log`, newest first:

- 2026-11-15: Add agent metadata and version documentation
- 2026-03-27: Update simulation engine to use OpenSWMMCore for building the WebAssembly module
- 2026-03-27: Add information about SWMM 6 and update styling for progress bar
- 2026-03-26: Add progress monitor and improve simulation execution
- 2026-03-26: Published your App
- 2026-03-26: Add interactive network map to visualize simulation input files
- 2026-03-26: Add multiple sample models to the simulator
- 2026-03-26: Add in-browser SWMM simulator for running WASM models
- 2026-03-26: Published your App
- 2026-03-26: Introduce a new features landing page and improve navigation
