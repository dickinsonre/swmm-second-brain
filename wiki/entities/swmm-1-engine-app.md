---
title: SWMM 1 Engine (app)
type: entity
updated: 2026-11-14
sources: [S01, S06, S07]
tags: [apps, swmm-history, swmm1]
reviewed: 2026-11-15
---
Bob's browser app that runs [SWMM 1 (1971)](swmm-1.md) from its own Fortran. File `swmm1-runoff-engine.html`; the name is kept from version 1.4, when the page ran the Runoff Block only [S01](../sources/S01-swmm1-engine-app-md.md). Version 3.6, 13 November 2026 [S01](../sources/S01-swmm1-engine-app-md.md).

**Three engines in one page** [S01](../sources/S01-swmm1-engine-app-md.md)

| Engine | Source | Build |
|---|---|---|
| Full program, as printed | All 12,200 cards of the October 1971 listing | f2c, then Emscripten 3.1.6 to WebAssembly, 328 KB |
| Full program with five repaired cards (optional) | `SROU 17`, `SROU 74`, `PLUG 21`, `PLUG192` changed; one COMMON card added to TRCHEK | Same |
| Runoff workbench | The 1,311 Runoff cards | Hand translation to C, wasi-sdk 24 |

A deck with a block card goes to the full program; any other deck goes to the workbench [S01](../sources/S01-swmm1-engine-app-md.md).

**What it reads and writes.** 80-column card decks in; the 1971 line-printer report, printer plots and interface tapes out. Importers convert SWMM 5 `.inp` and SWMM 4 `$RUNOFF` decks to SWMM 1 Runoff cards, with a conversion inventory and a rainfall check [S01](../sources/S01-swmm1-engine-app-md.md).

**Version milestones** [S01](../sources/S01-swmm1-engine-app-md.md)

| Version | Date | Change |
|---|---|---|
| 1.4 | 2026-10-22 | Runoff Block only, with the SWMM 5 and SWMM 4 importers |
| 2.0 | 2026-11-12 | All five blocks; full-program engine |
| 3.0 | 2026-11-12 | Fourteen more decks, Plots tab, optional repaired engine |
| 3.1 to 3.3 | 2026-11-12 to 13 | The four Volume II cities |
| 3.6 | 2026-11-13 | Importer fixes and four run-status rows after an outside review graded 3.5 at 85 of 100 |

**Checks.** See [Verification against printed runs](../concepts/verification-against-printed-runs.md). Complexity index 70.2; see [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md).

**Where it lives.** The swmm5.org topic pages link `swmm1-engine-imports-swmm5.netlify.app` [S06](../sources/S06-swmm5org-topics-index.md), [S07](../sources/S07-swmm5org-topic-swmm-history.md). The app's own summary records `netlify: none` and no public repository [S01](../sources/S01-swmm1-engine-app-md.md).

**Stale text elsewhere.** [S07](../sources/S07-swmm5org-topic-swmm-history.md) still describes it as "the 1971 SWMM 1 Runoff engine". Open question Q09 in [Open questions](../open-questions.md).
