---
title: "S153: OpenSWMM Engine, summary written by Replit Agent (v6.0.0-alpha.2)"
type: source
raw: raw/apps/open-swmm-core-v6.0.0-alpha.2.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, openswmm, swmm6, wasm, licensing]
reviewed: 11/16/2026
---
**What it is.** A technical summary of OpenSWMM Engine, version 6.0.0-alpha.2: a browser app that introduces the OpenSWMM project, documents it and runs `.inp` models in the legacy SWMM engine of HydroCouple/OpenSWMMCore compiled to WebAssembly. It is one of Bob's Replit apps, at `open-swmm-core.replit.app`. Raw file: [raw/apps/open-swmm-core-v6.0.0-alpha.2.md](../../raw/apps/open-swmm-core-v6.0.0-alpha.2.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, after Bob had the app's license statement fixed, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the source and documentation do not record which AI tools, if any, built it. The copy here was read out of the editor of the Replit project named Open-SWMM-Core on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** The other five samples were not run, and no result was compared with an independent reference. The public deployment was not checked, because it had not been republished. No independent legal or engineering review is recorded.

**Checked at ingest.** It supersedes [S148](S148-openswmm-engine-app-replit-summary.md), version 6.0.0-alpha.1. The license statement changed from MIT to Apache-2.0, as Bob had said it should [S151](S151-note-openswmm-license-not-mit.md) (Q83). Bob wrote at 19:16 that it is published, and the live home page then showed alpha.2, the commit and the Apache-2.0 statement [S154](S154-note-openswmm-engine-alpha2-published.md). The engine commit is now recorded (Q79). The engine version label changed from Legacy SWMM 5.x, with EPA SWMM 5.2.4 named as the legacy baseline [S148](S148-openswmm-engine-app-replit-summary.md), to Legacy SWMM 5.3.0. The [Topsoil Recovery Check (app)](../entities/topsoil-recovery-check.md) [S59](S59-topsoil-recovery-check-app-md.md) names an OpenSWMM legacy engine 5.3.0-beta.3, at another commit of the repository named openswmm.engine; whether the two are the same engine is not said. The `date:` is the day of the summary (Q75).

**Feeds:** [OpenSWMM Engine (app)](../entities/openswmm-engine-app.md), [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
