---
title: "S108: SWMM5 Runoff and Infiltration App, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/horton-model--robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, hydrology, infiltration, horton, green-ampt, curve-number, lid]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 Runoff and Infiltration App, version 1.0.0: an interactive app for exploring infiltration and surface runoff of a storm with five infiltration models, soil and LID settings, and rainfall fetched from a weather service. It is one of Bob's Replit apps, at `horton-model--robertdickinson.replit.app`. Raw file: [raw/apps/horton-model--robertdickinson-v1.0.0.md](../../raw/apps/horton-model--robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q67). Of the app itself it says AI use in development is not recorded in the project. The copy here was read out of the editor of the Replit project named SWMM5RunoffInfiltration on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- Five model choices: Horton, modified Horton, Green-Ampt, modified Green-Ampt and SCS Curve Number.
- Horton advances in 0.1-hour increments; capacity decays toward `fc` in rain and recovers toward `f0` when dry.
- Green-Ampt uses `f = Ks * (1 + psi * thetaD / F)` with a constant rainfall intensity over a six-hour calculation.
- Curve Number uses `Ia = 0.2 * S`.
- Presets: five storm scenarios; five Horton soils, six Green-Ampt soils, seven Curve Number land uses and four subcatchments; eight LID control types.
- It can fetch historical hourly precipitation from Open-Meteo.
- It downloads results as CSV, JSON, PDF, SWMM `.INP` and LandXML. No EPA SWMM engine is called, and importing the `.INP` into EPA SWMM was not checked.
- Peak runoff is converted to CFS by what the source code labels a rational-method approximation.
- `npm run check` passed. No test script is configured.

**Limits it states.** The live deployment was not loaded. Outputs were not compared with independent calculations. The downloads were not opened in other applications. No release date is recorded for 1.0.0.

**Checked at ingest.** The project is named SWMM5RunoffInfiltration and the site horton-model (Q70). It overlaps [S107](S107-green-ampt-calculator-replit-summary.md) in four of its five methods.

**Feeds:** [SWMM5 Runoff and Infiltration (app)](../entities/swmm5-runoff-and-infiltration.md), [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [Infiltration methods](../concepts/infiltration-methods.md), [Green-Ampt Infiltration Calculator (app)](../entities/green-ampt-infiltration-calculator.md).
