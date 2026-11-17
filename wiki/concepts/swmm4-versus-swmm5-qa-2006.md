---
title: "SWMM 4 against SWMM 5: the 2006 quality assurance tests"
type: concept
updated: 2026-11-17
sources: [S185, S186, S192]
tags: [swmm4, swmm5, dynamic-wave, verification, comparison, primary-document]
reviewed: no
---
Before SWMM 5 replaced SWMM 4, EPA ran both on the same twenty networks and compared the answers. This page is that report, Lewis Rossman's quality assurance report of 2006, a primary document, in digest [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md).

**What was compared** [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md)
- SWMM 4.4h (July 4, 2005) against SWMM 5.0.006 (September 2005), dynamic wave routing only, with equivalent options.
- Twenty examples: the ten [EXTRAN manual test models](extran-manual-test-models.md); five Challenge Test Cases "compiled by Robert E. Dickinson of CDM" (circular conduits in series with flat slopes, pipe constrictions, steep drops, adverse slopes and inlet offsets); and five real systems from users, 59 to 273 conduits.
- Judged on flow balances, scatter plots of peak conduit flows, and time series at outfalls, devices and places where the peaks differed.

**How the two solve a step** [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md)

| | SWMM 4.4h | SWMM 5.0.006 |
|---|---|---|
| Time stepping | Explicit: a half step, then a full step | Successive approximation, relaxation 0.5, head tolerance 0.005 ft, at most four trials |
| Surcharged nodes | Extra iterations at both half and full step, tolerance on fractional flow change | Folded into the ordinary iterations, no under-relaxation of the head |
| Orifice | An equivalent pipe | The orifice equation, or a modified weir equation when partly submerged |
| Shared | Velocity capped at 50 ft/s; free-fall end depth is the smaller of critical and normal depth; pumps limited to the inflow when the curve would pump the node dry | the same |

SWMM 5.2.4 iterates up to eight trials, not four [S186](../sources/S186-st-venant-rosetta-stone-app-md-v2-6-2.md); see [Dynamic wave routing](dynamic-wave-routing.md).

**What was found** [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md)
- Most time histories of flow and depth matched closely. EXTRAN1 gave "essentially identical results" and EXTRAN8 "perfect agreement".
- Two differences came from different assumptions. Bottom orifices; and Type 1 pump wet wells, where SWMM 4 holds back the inflow so the well never floods and SWMM 5 lets it flood, losing exactly the flooded volume from the outflow.
- EXTRAN7: SWMM 4's continuity error was -6.87 percent against SWMM 5's 0.24, with flow instability when the pump's inlet ran dry.
- EXTRAN10: at 40 minutes three identical pumps gave 25.7 cfs each in SWMM 5 and 23.0, 22.5 and 21.0 cfs in SWMM 4.
- In the user systems SWMM 4 went unstable "even with as low a time step as 0.5 seconds", worst with odd-shaped storage and oscillating inertial flow. SWMM 5 ran stably at a much larger step in 50 percent of the Challenge and user examples.
- Run times on the five user systems, SWMM 4 then SWMM 5, in seconds: 4 and 2, 17 and 10, 52 and 34, 30 and 22, 56 and 75.
- The verdict: SWMM 5.0 "performs dynamic wave flow routing as good as or better than SWMM 4.4".

**Twenty years on.** The [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md) reran Example 7 on SWMM 4.4H's XROUTE and printed the same -6.87 percent. It traces the error to a pump drawing from a dry junction, which disagrees with the report's statement that SWMM 4 limits the pump to the inflow when the node would run dry (Q95) [S186](../sources/S186-st-venant-rosetta-stone-app-md-v2-6-2.md), [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md).

**Not read yet.** Chapters 5 and 6 of the report, with the Challenge and user cases one by one [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md).

**Added 17 November 2026: the figures as data.** The [SWMM QA Report Bench (app)](../entities/swmm-qa-report-bench.md) measured the report's figures off the PDF and ran EPA SWMM 5.2.4 on the same twenty input files: 100 of 111 peaks are within 5 % of the 2006 SWMM 5 figure. The six largest differences and the large-step continuity errors are on its page [S192](../sources/S192-swmm-qa-report-bench-app-md.md).
