---
title: SWMM 1 Engine (app)
type: entity
updated: 2026-11-18
sources: [S01, S06, S07, S73, S324]
tags: [apps, swmm-history, swmm1]
reviewed: 2026-11-15
changed_after_review: "2026-11-18 (S300 to S375 ingest): a paragraph added near the end, headed Added 18 November 2026 (S324)"
---
Bob's browser app that runs [SWMM 1 (1971)](swmm-1.md) from its own Fortran. File `swmm1-runoff-engine.html`; the name is kept from version 1.4, when the page ran the Runoff Block only [S73](../sources/S73-swmm1-engine-app-md-v3-13.md). Version 3.13; the summary's front matter is dated 13 November 2026 and its change list dates 3.13 to 14 November [S73](../sources/S73-swmm1-engine-app-md-v3-13.md). The earlier source page, for version 3.6, is [S01](../sources/S01-swmm1-engine-app-md.md).

**Three engines in one page** [S73](../sources/S73-swmm1-engine-app-md-v3-13.md)

| Engine | Source | Build |
|---|---|---|
| Full program, as printed | All 12,200 cards of the October 1971 listing | f2c, then Emscripten 3.1.6 to WebAssembly, 328 KB |
| Full program with five repaired cards (optional) | `SROU 17`, `SROU 74`, `PLUG 21`, `PLUG192` changed; one COMMON card added to TRCHEK | Same |
| Runoff workbench | The 1,311 Runoff cards | Hand translation to C of 22 October 2026, wasi-sdk 24 |

A deck with a block card goes to the full program; any other deck goes to the workbench. Since 3.13 the engines run in a Web Worker with a Cancel button [S73](../sources/S73-swmm1-engine-app-md-v3-13.md).

**What it reads and writes.** 80-column card decks in; the 1971 line-printer report, printer plots and interface tapes out. Importers turn SWMM 5 `.inp` and SWMM 4 `$RUNOFF` decks into SWMM 1 Runoff cards [S73](../sources/S73-swmm1-engine-app-md-v3-13.md). What the importer keeps and loses is on [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md).

**Run status and run record.** After every run the page shows separate rows, among them execution, numerical validity, conservation, time axis, rainfall carried, routing carried, inputs carried, effective parameters, second engine and reference agreement. Only printed 1971 results count toward reference agreement. A run record, frozen when the run finishes, saves the exact deck, tapes, statuses and SHA-256 hashes [S73](../sources/S73-swmm1-engine-app-md-v3-13.md).

**Version milestones** [S73](../sources/S73-swmm1-engine-app-md-v3-13.md)

| Version | Date | Change |
|---|---|---|
| 1.4 | 2026-10-22 | Runoff Block only, with the SWMM 5 and SWMM 4 importers |
| 2.0 | 2026-11-12 | All five blocks; full-program engine |
| 3.0 | 2026-11-12 | Fourteen more decks, Plots tab, optional repaired engine |
| 3.1 to 3.3 | 2026-11-12 to 13 | The four Volume II cities |
| 3.6 to 3.9 | 2026-11-13 | Importer and run-status fixes after outside reviews graded 85, 89, 91 and 90 of 100 |
| 3.10 | 2026-11-13 | The workbench's C recovered, rebuilt and matched bit for bit on 9 decks |
| 3.11 to 3.13 | 2026-11-14 | Zero substitutes graded; outlet and name lookups fixed; Web Worker with Cancel |

The change list says "No engine change" for each version from 3.1 to 3.10 [S73](../sources/S73-swmm1-engine-app-md-v3-13.md).

**Checks.** The six 1971 runs are on [Verification against printed runs](../concepts/verification-against-printed-runs.md). The native-against-browser difference in the workbench, traced to `sinf` and `cosf`, is on [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md). Complexity index 72.6 at 3.13, up from 70.2 at 3.6 [S73](../sources/S73-swmm1-engine-app-md-v3-13.md), [S01](../sources/S01-swmm1-engine-app-md.md).

**What no run has checked.** The importer is checked against the `.inp`'s meaning and against a second engine, not against EPA SWMM 5: the solver could not be installed in the session, and four test models wait unrun [S73](../sources/S73-swmm1-engine-app-md-v3-13.md).

**Where it lives.** The swmm5.org topic pages link `swmm1-engine-imports-swmm5.netlify.app` [S06](../sources/S06-swmm5org-topics-index.md), [S07](../sources/S07-swmm5org-topic-swmm-history.md). The app's own summary records `netlify: none` and no public repository [S73](../sources/S73-swmm1-engine-app-md-v3-13.md).

**Stale text elsewhere.** [S07](../sources/S07-swmm5org-topic-swmm-history.md) still describes it as "the 1971 SWMM 1 Runoff engine". Open question Q09 in [Open questions](../open-questions.md).

**Added 18 November 2026.** A 60-second film of the app, SWMM 1 Engine Mograph, holds 43 distinct numbers in 9 settled frames, all in its facts file; its block counts add to the app's 12,200 [S324](../sources/S324-swmm1-engine-mograph-app-md.md).
