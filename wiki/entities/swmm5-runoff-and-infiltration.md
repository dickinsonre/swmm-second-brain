---
title: SWMM5 Runoff and Infiltration (app)
type: entity
updated: 2026-11-15
sources: [S107, S108, S139]
tags: [apps, replit, hydrology, infiltration, horton, green-ampt, curve-number, lid]
reviewed: no
---
Bob's Replit app SWMM5 Runoff and Infiltration App: an interactive app for exploring infiltration and surface runoff of a storm with five infiltration models, soil and LID settings, and rainfall fetched from a weather service. Version 1.0.0, at `horton-model--robertdickinson.replit.app` [S108](../sources/S108-runoff-and-infiltration-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S108](../sources/S108-runoff-and-infiltration-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q67).

**What the summary says** [S108](../sources/S108-runoff-and-infiltration-replit-summary.md)
- Five model choices: Horton, modified Horton, Green-Ampt, modified Green-Ampt and SCS Curve Number.
- Horton advances in 0.1-hour increments; capacity decays toward `fc` in rain and recovers toward `f0` when dry.
- Green-Ampt uses `f = Ks * (1 + psi * thetaD / F)` with a constant rainfall intensity over a six-hour calculation.
- Curve Number uses `Ia = 0.2 * S`.
- Presets: five storm scenarios; five Horton soils, six Green-Ampt soils, seven Curve Number land uses and four subcatchments; eight LID control types.
- It can fetch historical hourly precipitation from Open-Meteo.
- It downloads results as CSV, JSON, PDF, SWMM `.INP` and LandXML. No EPA SWMM engine is called, and importing the `.INP` into EPA SWMM was not checked.
- Peak runoff is converted to CFS by what the source code labels a rational-method approximation.
- `npm run check` passed. No test script is configured.

**What it does not show.** The live deployment was not loaded. Outputs were not compared with independent calculations. The downloads were not opened in other applications. No release date is recorded for 1.0.0. [S108](../sources/S108-runoff-and-infiltration-replit-summary.md)

**Noted at ingest.** The project is named SWMM5RunoffInfiltration and the site horton-model (Q70). It overlaps [S107](../sources/S107-green-ampt-calculator-replit-summary.md) in four of its five methods.

**Added 15 November 2026: a third infiltration app.** [SWMMCRAFT, infiltration simulator (app)](swmmcraft-infiltration-simulator.md) computes Horton, Green-Ampt and Curve Number infiltration for one storm in its own server code [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md).

See [Replit apps and the summaries Replit Agent wrote](../concepts/replit-app-summaries.md), [Infiltration methods](../concepts/infiltration-methods.md), [Green-Ampt Infiltration Calculator (app)](green-ampt-infiltration-calculator.md).
