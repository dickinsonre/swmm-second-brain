---
title: App build contract (four working principles)
type: concept
updated: 2026-11-14
sources: [S01, S02, S05, S58]
tags: [apps, method]
reviewed: no
---
The rules Bob set for building his single-file browser apps, as written in the instruction file of the old swmm-brain repository [S58](../sources/S58-swmm-brain-working-principles.md). The full contract lives in his swmm-vibe-coding-apps skill, which is not in `raw/` [S58](../sources/S58-swmm-brain-working-principles.md).

| Principle | In short |
|---|---|
| 1. State assumptions; don't pick silently | Name the units, the equation form, the boundary conditions and the defaults before writing code. Ask when a request has more than one reasonable reading |
| 2. Simplicity, beyond the contract, not below it | The minimum code above a fixed floor. No unrequested features, no abstractions for single use |
| 3. Surgical changes | Patch the named section only. Never regenerate the whole file to change one part |
| 4. Define success as a runnable check | See the list below |

Table from [S58](../sources/S58-swmm-brain-working-principles.md).

**The floor: what every app ships** [S58](../sources/S58-swmm-brain-working-principles.md)
- a "How to Use" welcome modal on first load, dismissable, reopened with `?`
- a step-by-step tour, or intro banners per tab
- a "Make a GIF" walkthrough button
- CSV export for tables
- `.inp` export where a model is generated

"If onboarding or export is missing, the app is incomplete, not lean" [S58](../sources/S58-swmm-brain-working-principles.md).

**Done means** [S58](../sources/S58-swmm-brain-working-principles.md)
- the displayed equation matches the computation exactly
- presets produce expected values, checked in a quick Node test before the interface is wired
- no console errors; responsive at 375 px; sliders with sane ranges, steps and units; chart axes labeled with units

**Seen in practice.** The SWMM 1 Engine has a Make a GIF button that records a 15-frame walkthrough [S01](../sources/S01-swmm1-engine-app-md.md), and the Complexity Meter writes a GIF walkthrough and CSV files [S02](../sources/S02-complexity-meter-app-md.md). The share of app-building conversations that report N of N test results rose from 7 % to 72 % between 2025Q4 and 2026Q3 [S05](../sources/S05-swmm5org-article-facts.md).

**Later additions not in this source.** [S58](../sources/S58-swmm-brain-working-principles.md) dates from August 2026. The Doc tab, the app .md and the complexity box are named in [S01](../sources/S01-swmm1-engine-app-md.md) as parts of a later app; the rules that require them are not in `raw/`.

See [Six quality markers for app-building work](app-quality-markers.md), [App complexity index (HydroCouple = 100)](app-complexity-index.md).
