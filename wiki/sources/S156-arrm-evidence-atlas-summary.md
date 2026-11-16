---
title: "S156: Automatic Rainfall-Runoff Models: Evidence Atlas, summary written from the page (deploy of 2026-08-21)"
type: source
raw: raw/apps/automatic-rainfall-runoff-models-v2026-08-21.md
kind: app-md
author: Robert Dickinson
published: 2026-08-21
ingested: 2026-11-16
tags: [apps, modpods, surrogates, machine-learning, benchmarks, netlify]
reviewed: 11/16/2026
---
**What it is.** A technical summary of the app "Automatic Rainfall-Runoff Models: Evidence Atlas", the page served at automatic-rainfall-runoff-models.netlify.app, deployed 21 August 2026. The app re-aggregates every fit in `dantzert/automatic-rainfall-runoff-models`, the replication package of the modpods paper, in eight tabs. Raw file: [raw/apps/automatic-rainfall-runoff-models-v2026-08-21.md](../../raw/apps/automatic-rainfall-runoff-models-v2026-08-21.md).

**How it was written. This one is different.** The page ships no summary and no version number. Claude (Anthropic) wrote the file on 16 November 2026, at Bob's request, from the live page, read tab by tab in a browser. Nothing was rerun on purpose; the Live model tab re-runs one stored model when it opens, and those live numbers were left out. Bob has not read it (Q84). The page carries no AI-use note; one sentence on its Repo & method tab is in the first person of the program that wrote it ("I do not have search or a bibliographic database here"), which marks at least that passage as AI-written. The page's tables are its evidence; its commentary is not checked against the repository here.

**Claims worth keeping** (all copied from the page)
- 2,476 fitted models across 415 sites: SWMM (Ann Arbor junction invert depth) 181 sites, 1,082 fits, median evaluation NSE 0.7406, 22 at NSE ≤ 0, best 0.9935; CAMELS 201 sites, 1,206 fits, 0.1938, 42, 0.8799; USGS 27 sites, 188 fits, -0.0060, 14, 0.7382. Selection on best training NSE among six configurations.
- CAMELS scoreboard, 365 basins, median evaluation NSE: LSTM ensemble 0.7619 down to VIC (CONUS calibrated) 0.3116 and modpods 0.1358; modpods beats EA-LSTM in 4 basins (1.1 %) and VIC (CONUS) in 108 (29.6 %). Benchmarks from the repository's `all_metrics.p` (Kratzert et al.).
- The SWMM driver: about 1,200 junctions, depth not flow, one shared rainfall series; junctions dropped for range under 0.5 ft, a first-step derivative over 50, a non-zero initial depth, or a wet ending above 20 % of the peak.
- The widest generalization gap: junction 91-51480, training NSE 0.8232, evaluation -6.173. Junction 91-51076: training 0.9954, evaluation -4.535.
- Complexity: on SWMM, median training NSE rises from 0.7874 (p1t1) to 0.8950 (p3t2) without a reversal while evaluation NSE goes 0.4922, 0.3577, 0.5782, 0.3473, 0.3882, 0.5869.
- Cost: median 19.2 minutes per site per order; worst single fit 59.8 h; 340 h for SWMM; 869 h in all.
- Selection defect: emulating two script defects reproduces the shipped `ensemble.csv` on 177/180 SWMM sites. As published 0.6909 (45/180 at NSE ≤ 0); intended rule 0.7406 (22/181); oracle 0.7956 (7/181, an upper bound that uses evaluation data).
- Re-running the stored model of junction 93-80315 agrees with the stored simulation to 0.154 % of range (0.164 % in an independent Python check); the gap is put down to cubic against linear forcing interpolation.

**Limits it states.** None in a list. This summary adds: the folder counts in one table do not add up (Q85); no version, author, About tab, Doc tab or AI-use note; the page asks that its DOI and the Kratzert citation be verified before they are quoted, and they were not.

**Feeds:** [Automatic Rainfall-Runoff Models: Evidence Atlas (app)](../entities/arrm-evidence-atlas.md), [modpods (Dantzer's method)](../entities/modpods.md), [Where a surrogate of SWMM breaks](../concepts/surrogates-hidden-state-missing-forcing.md), [A surrogate distilled from SWMM](../concepts/surrogate-distilled-from-swmm.md).
