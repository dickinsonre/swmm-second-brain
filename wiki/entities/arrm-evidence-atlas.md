---
title: "Automatic Rainfall-Runoff Models: Evidence Atlas (app)"
type: entity
updated: 2026-11-16
sources: [S156]
tags: [apps, modpods, surrogates, machine-learning, benchmarks, netlify]
reviewed: no
---
Bob's app that puts every fit in the [modpods](modpods.md) replication package, `dantzert/automatic-rainfall-runoff-models`, on one page: 2,476 fitted models across 415 sites. It is on Netlify at automatic-rainfall-runoff-models.netlify.app, deployed 21 August 2026, with no version number on the page. "Nothing is quoted from the paper text" [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**A caution about its source.** The page ships no technical summary. [S156](../sources/S156-arrm-evidence-atlas-summary.md) was written by Claude on 16 November 2026 from the live page, and Bob has not yet read it (Q84). The page has no AI-use note, but one sentence on it is in the first person of the program that wrote it.

**Eight tabs** [S156](../sources/S156-arrm-evidence-atlas-summary.md): Overview, CAMELS scoreboard, SWMM surrogate, Live model, Complexity & cost, Selection defect, Atlas (2,476 fits, filterable, every table with a CSV button), Repo & method.

**The headline, in the page's words:** "As a rainfall-runoff model for real catchments it loses to everything; as an emulator of a SWMM model's own output it works" [S156](../sources/S156-arrm-evidence-atlas-summary.md).

| Dataset | Sites | Median evaluation NSE | NSE ≤ 0 | Best |
|---|---|---|---|---|
| SWMM, Ann Arbor junction depth | 181 | 0.7406 | 22 | 0.9935 |
| CAMELS basins | 201 | 0.1938 | 42 | 0.8799 |
| USGS gauges | 27 | -0.0060 | 14 | 0.7382 |

On the 365 CAMELS basins all fourteen models share, modpods' median is 0.1358 against 0.7619 for the LSTM ensemble [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**Overfitting, measured.** On the SWMM set, median training NSE climbs from 0.7874 to 0.8950 across six configurations while evaluation NSE zigzags between 0.3473 and 0.5869. Junction 91-51480 trains at 0.8232 and evaluates at -6.173 [S156](../sources/S156-arrm-evidence-atlas-summary.md). The page's advice: hold out storms, not timesteps [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**The junction filters.** The SWMM driver dropped a junction if its depth range was under 0.5 ft, its first-step derivative over 50, its initial depth not zero, or its ending wet above 20 % of the peak; 181 survive [S156](../sources/S156-arrm-evidence-atlas-summary.md). Which signals such a model cannot carry is on [Where a surrogate of SWMM breaks](../concepts/surrogates-hidden-state-missing-forcing.md).

**Live model.** Eleven stored models re-run in the browser from the pickled parameters, with sliders on the kernel parameters, ranged by the repository's own search bounds. For junction 93-80315 the re-run matches the stored simulation to 0.154 % of range [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**Selection defect.** Two defects in the package's summary scripts, shown with the lines and reproduced on 177 of 180 SWMM sites; the intended rule raises the SWMM median from 0.6909 to 0.7406 [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**Cost.** 869 h of fitting in all; worst single fit 59.8 h [S156](../sources/S156-arrm-evidence-atlas-summary.md).

**Open.** One of its tables does not add up (Q85), and it names a different worst junction from [modpods, for a SWMM person](modpods-explainer-app.md) (Q86).
