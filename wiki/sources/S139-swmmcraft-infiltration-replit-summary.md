---
title: "S139: SWMMCRAFT, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-infiltration--robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2025-12-25
ingested: 2026-11-15
tags: [apps, replit, infiltration, hydrology]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMMCRAFT, version 1.0.0: a calculator of infiltration and runoff for one storm by the Horton, Green-Ampt or Curve Number method, in its own server code; it calls no SWMM engine. It is one of Bob's Replit apps, at `swmm-infiltration--robertdickinson.replit.app`. Raw file: [raw/apps/swmm-infiltration--robertdickinson-v1.0.0.md](../../raw/apps/swmm-infiltration--robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the project records no AI contribution to the app source; the Replit workflow configuration uses `author = "agent"` but does not attribute code changes. The copy here was read out of the editor of the Replit project named SWMM-Infiltration on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** Engineering accuracy and suitability for design are not established. Varying rainfall and surface ponding are not inputs. The production pages and the iPhone layout were not checked. The `date:` uses the newest date in the Git log.

**Checked at ingest.** Arithmetic. The totals add up: 1.1921 + 0.3079 = 1.5000 inches. With steps = ceil(1 / 0.5) = 2 and i running from 0 through 2, the loop applies three half-hour increments at 1 inch/hour, 1.5 inches, where a 1-hour storm at that rate holds 1.0 inch (our arithmetic). The two Curve Number denominators are one expression: with `Ia = 0.2 * S`, `P - Ia + S` equals `P + 0.8 * S` (our algebra), so the difference the file reports is in how the formula is written, not in its value (Q82). The name SWMMCRAFT does not say the app computes infiltration; its Replit project is SWMM-Infiltration (Q77). It is the third infiltration calculator here with its own code, after the [Green-Ampt Infiltration Calculator (app)](../entities/green-ampt-infiltration-calculator.md) [S107](S107-green-ampt-calculator-replit-summary.md) and [SWMM5 Runoff and Infiltration (app)](../entities/swmm5-runoff-and-infiltration.md) [S108](S108-runoff-and-infiltration-replit-summary.md). Its whole change list is dated 25 December 2025 (Q75).

**Feeds:** [SWMMCRAFT, infiltration simulator (app)](../entities/swmmcraft-infiltration-simulator.md), [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [Green-Ampt Infiltration Calculator (app)](../entities/green-ampt-infiltration-calculator.md), [SWMM5 Runoff and Infiltration (app)](../entities/swmm5-runoff-and-infiltration.md), [Infiltration methods](../concepts/infiltration-methods.md).
