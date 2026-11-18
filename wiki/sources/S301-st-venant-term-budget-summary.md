---
title: "S301: St. Venant Term Budget, summary written from the page (v1.0)"
type: source
raw: raw/apps/st-venant-term-budget-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-05
ingested: 2026-11-18
tags: [apps, swmm5, swmm6, dynamic-wave, momentum, verification]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app St. Venant Term Budget, version 1.0: does friction dominate? Per-link momentum terms, read from a SWMM .out file. Raw file: [raw/apps/st-venant-term-budget-v1.0.md](../../raw/apps/st-venant-term-budget-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/QN5FG2DKm24VeW4SsL6XhU, version 1791203604-671c (index.html, 784,497 bytes, SHA-256 e9e034d88f70ef2523adbfd1f798af0d49e54cdd303e2818537447ec5ce76824), its Budget, Links, Compare, Verify and Learn tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page carries no AI-use note. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page."

**Claims worth keeping** (all copied from the file)
- Load a SWMM model set (.inp, .out, .rpt) and the app splits each conduit's momentum equation into bed slope, pressure gradient, friction, the two inertia terms and local losses, each as a slope in ft/ft, rebuilt from what the .out file saved. It rolls them up into a Friction Dominance Index: the share of conveyed volume that moved with friction matching bed slope. A second run can be loaded to see where two engines or two option sets differ.
- Where friction equals bed slope, water is running downhill and any engine gives the same answer; where it does not, the engines' choices matter. On the 13-conduit demo the index is 49%, built low on purpose. The rebuild was checked against an instrumented EPA SWMM 5.2.4 that records the terms the solver used at every step: kinematic match agrees within 0.0006, and the index reads 0.4937 from the .out against 0.4940 from the engine.
- Instrumented EPA SWMM 5.2.4 against the rebuild on the demo: kinematic match within 0.0006, any term share within 0.0006, index 0.4937 against 0.4940. The recorder changed nothing: its .out is byte-identical to the stock build.
- Report steps from 5 s to 60 s: max |Δ match| 0.0006; at 300 s, 0.0032. Also checked with SURCHARGE_METHOD SLOT, INERTIAL_DAMPING NONE and FULL, and VARIABLE_STEP 0.75.
- Stock engine run twice: byte-identical. The .out reader against the .rpt time series: 2,880 values, 0 outside print rounding (largest difference 5.0e-4).
- EPA 5.2.4 against OpenSWMM 6.0.0-alpha.2 on the demo: every conduit within 0.30% of its own peak at every reporting period. The OpenSWMM 6 continuity line reads −29.401% against −0.211%, because its report counts almost none of the 0.404 acre-ft already in the system as initial storage (entered on the page's defect register as open, not reported).

**Limits it states.** As the page lists it: no field data; one 13-conduit network built for the purpose, so the rank correlations rest on 13 points and the p-values are optimistic; two of the three demo B runs are the same engine with options changed, and the OpenSWMM 6 run shares SWMM 5's scheme; nothing compares against ICM or HEC-RAS; only circular, rectangular, trapezoidal and triangular sections are handled, every other shape (force mains included) is skipped and counted; the rule share also absorbs report-step sampling error, so it is an upper bound.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [St. Venant Term Budget (app)](../entities/st-venant-term-budget.md), [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md).
