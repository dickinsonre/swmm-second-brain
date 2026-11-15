---
title: "SWMMCRAFT, infiltration simulator (app)"
type: entity
updated: 2026-11-15
sources: [S107, S108, S139]
tags: [apps, replit, infiltration, hydrology]
reviewed: no
---
Bob's Replit app SWMMCRAFT: a calculator of infiltration and runoff for one storm by the Horton, Green-Ampt or Curve Number method, in its own server code; it calls no SWMM engine. Version 1.0.0, at `swmm-infiltration--robertdickinson.replit.app` [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md)
- Users enter storm duration, time step, rainfall intensity and method parameters in hours and inches. `units: US customary`. `engines: none`.
- The server computes `steps = ceil(duration / timeStep)`, then loops from `i = 0` through `steps`, with constant rainfall intensity at each step.
- Horton: potential rate = `minRate + (maxRate - minRate) * exp(-decay * time)`, capped at rainfall intensity.
- Green-Ampt: potential rate = `conductivity * (1 + suction * initialDeficit / F)`, with `F` initialized to `0.0001` when it is zero, capped at rainfall intensity.
- Curve Number: `S = 1000 / CN - 10`; `Ia = 0.2 * S`; for `P > Ia`, `Q = (P - Ia)^2 / (P + 0.8 * S)`. Cumulative infiltration is set to `P - Q`.
- Runoff rate is the nonnegative difference between rainfall and infiltration rate. The method-comparison chart computes all three curves in the browser, separately from the server calculation. No external SWMM simulation engine is called.
- A Horton request with duration 1 hour, time step 0.5 hour and rainfall intensity 1 inch/hour returned 3 rows and totals of 1.5 inches rainfall, 1.1921 inches infiltration and 0.3079 inches runoff.
- The inclusive loop processes `steps + 1` rainfall increments; that is how the 1-hour request above produced 1.5 inches of rainfall.
- The Horton code uses elapsed simulation time directly; its comment says it does not implement equivalent time for non-ponding periods.
- The Curve Number reference page displays `Q = (P - Ia)^2 / (P - Ia + S)`; the file reports this as differing from the server's denominator `P + 0.8 * S`.
- Three routed pages, three methods and three seed models. PostgreSQL stores names, methods and parameters; results are not saved. `npm run check` failed with 2 TypeScript errors. No test script is configured.
- The project declares MIT. The technical reference cites EPA SWMM 5.2, Horton, Green and Ampt, USDA-NRCS and Rawls et al.

**What it does not show.** Engineering accuracy and suitability for design are not established. Varying rainfall and surface ponding are not inputs. The production pages and the iPhone layout were not checked. The `date:` uses the newest date in the Git log. [S139](../sources/S139-swmmcraft-infiltration-replit-summary.md)

**Noted at ingest.** Arithmetic. The totals add up: 1.1921 + 0.3079 = 1.5000 inches. With steps = ceil(1 / 0.5) = 2 and i running from 0 through 2, the loop applies three half-hour increments at 1 inch/hour, 1.5 inches, where a 1-hour storm at that rate holds 1.0 inch (our arithmetic). The two Curve Number denominators are one expression: with `Ia = 0.2 * S`, `P - Ia + S` equals `P + 0.8 * S` (our algebra), so the difference the file reports is in how the formula is written, not in its value (Q82). The name SWMMCRAFT does not say the app computes infiltration; its Replit project is SWMM-Infiltration (Q77). It is the third infiltration calculator here with its own code, after the [Green-Ampt Infiltration Calculator (app)](green-ampt-infiltration-calculator.md) [S107](../sources/S107-green-ampt-calculator-replit-summary.md) and [SWMM5 Runoff and Infiltration (app)](swmm5-runoff-and-infiltration.md) [S108](../sources/S108-runoff-and-infiltration-replit-summary.md). Its whole change list is dated 25 December 2025 (Q75).

See [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [Green-Ampt Infiltration Calculator (app)](green-ampt-infiltration-calculator.md), [SWMM5 Runoff and Infiltration (app)](swmm5-runoff-and-infiltration.md), [Infiltration methods](../concepts/infiltration-methods.md).
