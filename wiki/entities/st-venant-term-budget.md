---
title: "St. Venant Term Budget (app)"
type: entity
updated: 2026-11-18
sources: [S301]
tags: [apps, swmm5, swmm6, dynamic-wave, momentum, verification]
reviewed: no
---
Bob's app St. Venant Term Budget: does friction dominate? Per-link momentum terms, read from a SWMM .out file. Version 1.0, 2026-10-05 [S301](../sources/S301-st-venant-term-budget-summary.md). Its `links:` line names no live Netlify address [S301](../sources/S301-st-venant-term-budget-summary.md).

**A caution about its source.** The page ships no technical summary. [S301](../sources/S301-st-venant-term-budget-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S301](../sources/S301-st-venant-term-budget-summary.md)
- Load a SWMM model set (.inp, .out, .rpt) and the app splits each conduit's momentum equation into bed slope, pressure gradient, friction, the two inertia terms and local losses, each as a slope in ft/ft, rebuilt from what the .out file saved. It rolls them up into a Friction Dominance Index: the share of conveyed volume that moved with friction matching bed slope. A second run can be loaded to see where two engines or two option sets differ.
- Where friction equals bed slope, water is running downhill and any engine gives the same answer; where it does not, the engines' choices matter. On the 13-conduit demo the index is 49%, built low on purpose. The rebuild was checked against an instrumented EPA SWMM 5.2.4 that records the terms the solver used at every step: kinematic match agrees within 0.0006, and the index reads 0.4937 from the .out against 0.4940 from the engine.
- Instrumented EPA SWMM 5.2.4 against the rebuild on the demo: kinematic match within 0.0006, any term share within 0.0006, index 0.4937 against 0.4940. The recorder changed nothing: its .out is byte-identical to the stock build.
- Report steps from 5 s to 60 s: max |Δ match| 0.0006; at 300 s, 0.0032. Also checked with SURCHARGE_METHOD SLOT, INERTIAL_DAMPING NONE and FULL, and VARIABLE_STEP 0.75.
- Stock engine run twice: byte-identical. The .out reader against the .rpt time series: 2,880 values, 0 outside print rounding (largest difference 5.0e-4).
- EPA 5.2.4 against OpenSWMM 6.0.0-alpha.2 on the demo: every conduit within 0.30% of its own peak at every reporting period. The OpenSWMM 6 continuity line reads −29.401% against −0.211%, because its report counts almost none of the 0.404 acre-ft already in the system as initial storage (entered on the page's defect register as open, not reported).

**How to use it, as the summary puts it.** Use it to see which links in your model are kinematic, which are run from downstream, and where an engine's rules decide the flow. It has no field data, one purpose-built 13-conduit test network, analytic geometry for four section shapes only, and no engine outside the SWMM family. [S301](../sources/S301-st-venant-term-budget-summary.md)

**What it does not show.** As the page lists it: no field data; one 13-conduit network built for the purpose, so the rank correlations rest on 13 points and the p-values are optimistic; two of the three demo B runs are the same engine with options changed, and the OpenSWMM 6 run shares SWMM 5's scheme; nothing compares against ICM or HEC-RAS; only circular, rectangular, trapezoidal and triangular sections are handled, every other shape (force mains included) is skipped and counted; the rule share also absorbs report-step sampling error, so it is an upper bound. [S301](../sources/S301-st-venant-term-budget-summary.md)

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [St. Venant Solver Rosetta Stone (app)](st-venant-solver-rosetta-stone.md).
