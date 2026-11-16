---
title: "S148: OpenSWMM Engine, summary written by Replit Agent (v6.0.0-alpha.1)"
type: source
raw: raw/apps/open-swmm-core-v6.0.0-alpha.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, openswmm, swmm6, wasm]
reviewed: no
---
**What it is.** A technical summary of OpenSWMM Engine, version 6.0.0-alpha.1: a browser app that introduces the OpenSWMM project, documents it and runs `.inp` models in the legacy SWMM engine of HydroCouple/OpenSWMMCore compiled to WebAssembly. It is one of Bob's Replit apps, at `open-swmm-core.replit.app`. Raw file: [raw/apps/open-swmm-core-v6.0.0-alpha.1.md](../../raw/apps/open-swmm-core-v6.0.0-alpha.1.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the source and documentation do not record which AI tools, if any, built it. The copy here was read out of the editor of the Replit project named Open-SWMM-Core on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- One `engines:` entry: the OpenSWMMCore legacy SWMM solver in WebAssembly, version given as Legacy SWMM 5.x with app release 6.0.0-alpha.1, from the `swmm6_rel` branch of HydroCouple/OpenSWMMCore. Commit: not recorded.
- The feature page identifies EPA SWMM 5.2.4 as its legacy baseline.
- The app calls `swmm_open`, `swmm_start`, `swmm_step` repeatedly, then `swmm_end`, `swmm_report` and `swmm_close`. The SWMM engine performs the hydraulic and hydrologic calculations; the app implements no solver equations of its own.
- It parses the report into tables and time series. The `.rpt` and `.out` files stay in the WebAssembly virtual filesystem and are removed; the app offers no download of them.
- 3 views, 6 bundled sample models and 11 top-level documentation chapters. No database or API service.
- The TypeScript check passed. The production build passed, with a main JavaScript chunk of 730.06 kB against an advisory threshold of 500 kB.
- The bundled User1 sample completed with a Success status in the browser. The other samples were fetched but not run, and no result was compared with an independent reference.
- The build script clones the `swmm6_rel` branch without recording a commit, so the source revision of the checked-in binary is not recorded.
- The app identifies OpenSWMMCore and HydroCouple as MIT licensed and states that the original EPA SWMM material is public domain under 17 USC § 105. It acknowledges EPA SWMM and Lewis A. Rossman. No license file is in the app directory.
- No automated test suite. `units: both`.

**Limits it states.** Only User1 was run through the simulator. Mobile behavior, accessibility and large models were not checked. The engine's source commit is not recorded.

**Checked at ingest.** License. The file says MIT. Bob wrote the same day that the OpenSWMM license has moved away from MIT [S151](S151-note-openswmm-license-not-mit.md). Other sources here give Apache-2.0 for the `swmm6_rel` branch of HydroCouple/openswmm.engine, a repository with a different name: [S59](S59-topsoil-recovery-check-app-md.md) [S69](S69-swmm6-code-house-app-md.md) [S96](S96-swmm5-ui-replit-summary.md) (Q83). The engine's version is given as Legacy SWMM 5.x; 6.0.0-alpha.1 is the app's release label (Q79). The `date:` is the day of the summary; the change list is from 26 and 27 March 2026 (Q75).

**Feeds:** [OpenSWMM Engine (app)](../entities/openswmm-engine-app.md), [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
