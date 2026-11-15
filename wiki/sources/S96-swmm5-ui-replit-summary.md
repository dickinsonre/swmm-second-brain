---
title: "S96: SWMM5-UI, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-ui-engine-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, swmm6, engines, wasm, lid]
reviewed: no
---
**What it is.** A technical summary of SWMM5-UI, version 1.0.0: an app that opens and edits SWMM model files, runs them in browser, server or remote engines, and shows maps, time series, tables, reports and comparisons between runs. It is one of Bob's Replit apps, at `swmm-ui-engine.replit.app`. Raw file: [raw/apps/swmm-ui-engine-v1.0.0.md](../../raw/apps/swmm-ui-engine-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says the README records iterative development with Replit Agent. The copy here was read out of the editor of the Replit project named Swmm UI Engine on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Six engine modes, counting a mock: EPA SWMM in the browser, labelled 5.2.4-lid1 (v5.2.4 with local LID changes); OpenSWMM 6.0.0-alpha.3 built from `swmm6_rel` (Apache-2.0); OpenSWMM 6.0.0-alpha.3 built from `develop` (MIT); a local EPA SWMM 5.2.4; a remote SWMM service; and a mock that makes synthetic data.
- The upstream commits of the three browser engines are unrecorded in `engines.json`.
- Checks were run on the workspace, not on the published build. `npm run check` passed. `npm test` reported 34 groups passed and 0 failed; its Vitest part passed 58 tests in 8 files.
- 36 bundled `.inp` sample files and 3 MCP tool registrations.
- Its diagnostic equations use a gravity of 32.174 ft/s² and a Manning phi of 1.4859 in US customary units.
- Long binary outputs are sampled with a nominal limit of 5,000 periods; unsampled peaks were not checked.
- The README marks SWMM6 LID results as untrustworthy.
- Credits: USEPA for the SWMM engine and HydroCouple for OpenSWMM. Caleb Buahin, Corinne Wiesner-Friedman and Scott Jeffers are named as OpenSWMM contributors, as attribution and not as reviewers of this app.
- Repository: https://github.com/dickinsonre/Swmm5-UI-Engine. Application source is MIT.

**Limits it states.** The published app was not checked. The end-to-end browser suite was not run. The remote engine, engine parity and field accuracy were not checked. No release date is recorded for 1.0.0, so the front matter carries the summary date.

**Checked at ingest.** The newest change it lists is dated 21 September 2026. [S80](S80-control-section-lab-summary.md) built OpenSWMM 6.0.0-alpha.4 on 16 October 2026, so the alpha.3 named here is the older build.

**Feeds:** [SWMM5-UI (app)](../entities/swmm5-ui.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [EPA SWMM 5](../entities/swmm-5.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
