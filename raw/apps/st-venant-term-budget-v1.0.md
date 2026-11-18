---
name: St. Venant Term Budget
file: st-venant-term-budget.html
version: "1.0"
date: 2026-10-05
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/QN5FG2DKm24VeW4SsL6XhU", repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "demo results computed ahead of time (v5.2.4 tag, gcc -O2 -ffp-contract=off -D_FORTIFY_SOURCE=0, single thread); no engine runs in the page", license: public domain}
  - {name: OpenSWMM 6, version: 6.0.0-alpha.2, note: "demo run B from the LocalSWMM prebuilt wasm, commit 164beb8d", license: Apache-2.0}
units: the .out file's own units; the demo is CFS
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page carries no AI-use note."
written_from: "the published Claude artifact https://claude.ai/artifact/QN5FG2DKm24VeW4SsL6XhU, version 1791203604-671c (index.html, 784,497 bytes, SHA-256 e9e034d88f70ef2523adbfd1f798af0d49e54cdd303e2818537447ec5ce76824), its Budget, Links, Compare, Verify and Learn tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# St. Venant Term Budget: does friction dominate? Per-link momentum terms, read from a SWMM .out file

## In three points
- **What:** Load a SWMM model set (.inp, .out, .rpt) and the app splits each conduit's momentum equation into bed slope, pressure gradient, friction, the two inertia terms and local losses, each as a slope in ft/ft, rebuilt from what the .out file saved. It rolls them up into a Friction Dominance Index: the share of conveyed volume that moved with friction matching bed slope. A second run can be loaded to see where two engines or two option sets differ.
- **So what:** Where friction equals bed slope, water is running downhill and any engine gives the same answer; where it does not, the engines' choices matter. On the 13-conduit demo the index is 49%, built low on purpose. The rebuild was checked against an instrumented EPA SWMM 5.2.4 that records the terms the solver used at every step: kinematic match agrees within 0.0006, and the index reads 0.4937 from the .out against 0.4940 from the engine.
- **Now what:** Use it to see which links in your model are kinematic, which are run from downstream, and where an engine's rules decide the flow. It has no field data, one purpose-built 13-conduit test network, analytic geometry for four section shapes only, and no engine outside the SWMM family.

This summary was written after the fact. The app ships no technical summary of its own. Its version and date are the page's own ("v1.0, built 2026-10-05"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Budget, Links, Compare, Verify, Learn. Load model set, Load folder, or the demo (budget13.inp, .out, .rpt, plus run B budget13_swmm6.out). Budget shows the index, the median link match, links at 0.90 or more, the pressure and inertia shares, and term shares by link. Links sorts every conduit by slope, kinematic match, shares, backwater ratio, rule share, Froude peak, peak flow, rise time, memory ratio, Ponce kinematic and diffusion numbers and the Woolhiser–Liggett number, with a screen of kinematic, diffusion or dynamic. Compare measures where run B differs link by link and tests whether the budget predicted it (Spearman ρ with a permutation p). Learn gives the equations in the order of SWMM's dwflow.c and the metric definitions. Export CSV and Make a GIF are in the header.

## How it computes

From dwflow_findConduitFlow(): Q = (Qold − dq2 + dq3 + dq4) / (1 + dq1 + dq5). Each term divided by g·Awtd·Δt becomes a slope: S0 (bed), Sp (pressure), Sf = (n/φ)² · |v| · Q / (Awtd · Rwtd^(4/3)), Sconv, Sloc, Sloss, with S0 + Sp + Sconv = Sf + Sloss + Sloc; φ = 1.486 in US units; σ is the inertial damping factor. Kinematic match = 1 − Σw|Sf − S0| / Σw(|Sf| + |S0|), weighted by w = |Q|·Δt. The rule share is the residual: the engine's normal-flow limit, iteration blending, inlet control and flow limits.

## Checks (as stated on the page)

- Instrumented EPA SWMM 5.2.4 against the rebuild on the demo: kinematic match within 0.0006, any term share within 0.0006, index 0.4937 against 0.4940. The recorder changed nothing: its .out is byte-identical to the stock build.
- Report steps from 5 s to 60 s: max |Δ match| 0.0006; at 300 s, 0.0032. Also checked with SURCHARGE_METHOD SLOT, INERTIAL_DAMPING NONE and FULL, and VARIABLE_STEP 0.75.
- Stock engine run twice: byte-identical. The .out reader against the .rpt time series: 2,880 values, 0 outside print rounding (largest difference 5.0e-4).
- EPA 5.2.4 against OpenSWMM 6.0.0-alpha.2 on the demo: every conduit within 0.30% of its own peak at every reporting period. The OpenSWMM 6 continuity line reads −29.401% against −0.211%, because its report counts almost none of the 0.404 acre-ft already in the system as initial storage (entered on the page's defect register as open, not reported).

## What this does not show

As the page lists it: no field data; one 13-conduit network built for the purpose, so the rank correlations rest on 13 points and the p-values are optimistic; two of the three demo B runs are the same engine with options changed, and the OpenSWMM 6 run shares SWMM 5's scheme; nothing compares against ICM or HEC-RAS; only circular, rectangular, trapezoidal and triangular sections are handled, every other shape (force mains included) is skipped and counted; the rule share also absorbs report-step sampling error, so it is an upper bound.

## Credits and licenses

Ponce, Li and Simons (1978), J. Hydraulics Div. ASCE 104(HY3); Woolhiser and Liggett (1967), Water Resources Research 3(3). EPA SWMM 5.2.4 (public domain); OpenSWMM 6.0.0-alpha.2 through LocalSWMM's prebuilt wasm (used for a run whose .out the page carries; no OpenSWMM code is in the page). The defect register also notes a bug in corinne-testing/scripts/out-diff.js (link type codes read as floats). No license is stated for the page.

## AI use

The page carries no AI-use note. This summary was written by Claude (Anthropic) on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-05): first version (the version read).
