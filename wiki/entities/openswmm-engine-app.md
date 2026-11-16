---
title: "OpenSWMM Engine (app)"
type: entity
updated: 2026-11-15
sources: [S59, S148, S151, S153, S154]
tags: [apps, replit, openswmm, swmm6, wasm, licensing]
reviewed: no
---
Bob's Replit app OpenSWMM Engine: a browser app that introduces the OpenSWMM project, documents it and runs `.inp` models in the legacy SWMM engine of HydroCouple/OpenSWMMCore compiled to WebAssembly. Version 6.0.0-alpha.2, at `open-swmm-core.replit.app` [S153](../sources/S153-openswmm-engine-app-alpha2-replit-summary.md). It replaced version 6.0.0-alpha.1 [S148](../sources/S148-openswmm-engine-app-replit-summary.md) on 15 November 2026.

**A caution about its source.** This page rests on [S153](../sources/S153-openswmm-engine-app-alpha2-replit-summary.md) and [S148](../sources/S148-openswmm-engine-app-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source, and on Bob's notes [S151](../sources/S151-note-openswmm-license-not-mit.md) and [S154](../sources/S154-note-openswmm-engine-alpha2-published.md). Nothing here has been read by Bob (Q74).

**What the alpha.2 summary says** [S153](../sources/S153-openswmm-engine-app-alpha2-replit-summary.md)
- One `engines:` entry: the OpenSWMMCore legacy SWMM solver in WebAssembly, version given as Legacy SWMM 5.3.0 with app release 6.0.0-alpha.2, from HydroCouple/OpenSWMMCore at commit `87664bf518104e618f0537340b9500a1fdfe797c`.
- Engine license: Apache-2.0 for OpenSWMM contributions; the USEPA SWMM portions are public domain. This app's code: MIT, Copyright 2026 Robert Dickinson.
- The credits read: OpenSWMM Engine, Copyright 2026 HydroCouple Developers, licensed under the Apache License, Version 2.0; portions derive from USEPA SWMM, which is in the public domain under 17 USC 105; the USEPA does not endorse this product.
- `ENGINE_SOURCE.txt` records the commit, and `git rev-parse HEAD` in the fetched source checkout matched it. The app links to that commit.
- Root `LICENSE` and `NOTICE` are unchanged copies from that commit and matched it byte-for-byte; their SHA-256 checksums are `94fcde3f05aad351a969a65f5c87b25ee3893ee7297549d6a3217bf29ccbc3aa` and `83a3c0524ba9dd6929a5d5e110f959d318ce142ffbc2cce74616bf5866b1d5cb`. The complete NOTICE is displayed on the Features page.
- The WebAssembly build passed from the pinned commit with a fresh Emscripten cache. The compiler emitted two ignored `#pragma float_control` warnings from upstream `mathexpr.c`. No upstream engine C source files were modified.
- The bundled User1 sample completed in the rebuilt engine with exit code 0 and a 66,945-character report. The other five samples were not run.
- The TypeScript check and the production build passed; the main JavaScript chunk is 734.08 kB against an advisory 500 kB.
- OpenSWMM credits Caleb Buahin (lead developer) and Corinne Wiesner-Friedman (developer, documentation); EPA SWMM and Lewis A. Rossman are credited for the foundational model.
- 3 views, 6 bundled sample models, 11 top-level documentation chapters. No database or API service, and no automated test suite.
- When the summary was written the app had not yet been republished.

**What changed from alpha.1** [S148](../sources/S148-openswmm-engine-app-replit-summary.md). The license statement: alpha.1 called OpenSWMMCore and HydroCouple MIT; Bob said the OpenSWMM license has moved away from MIT [S151](../sources/S151-note-openswmm-license-not-mit.md) (Q83); alpha.2 states Apache-2.0 for the engine and MIT for the app's own code. The engine commit: not recorded in alpha.1, pinned in alpha.2. The engine version label: Legacy SWMM 5.x with EPA SWMM 5.2.4 as the legacy baseline in alpha.1, Legacy SWMM 5.3.0 in alpha.2. Bob wrote that alpha.2 is published, and the live home page showed it [S154](../sources/S154-note-openswmm-engine-alpha2-published.md).

**What it does not show.** The other five samples were not run, and no result was compared with an independent reference. The public deployment was not checked, because it had not been republished. No independent legal or engineering review is recorded. [S153](../sources/S153-openswmm-engine-app-alpha2-replit-summary.md)

**Noted at ingest.** The [Topsoil Recovery Check (app)](topsoil-recovery-check.md) [S59](../sources/S59-topsoil-recovery-check-app-md.md) names an OpenSWMM legacy engine 5.3.0-beta.3 at another commit of the repository named openswmm.engine; whether it is the same engine as this one is not said (Q79).

See [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).
