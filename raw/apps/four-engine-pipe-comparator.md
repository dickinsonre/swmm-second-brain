---
name: Four-Engine Pipe Comparator
file: four-engine-pipe-comparator.html
version: 1.5.0
date: 2026-11-18
author: Robert Dickinson
links: {netlify: none recorded, artifact: see delivery message, repo: none}
engines:
  - {name: HEC-RAS Pipe Networks, version: "7.0.1", source: USACE HEC release, license: public release, run_here: false}
  - {name: InfoWorks ICM, version: current, source: Autodesk, license: commercial, run_here: false}
  - {name: EPA SWMM, version: 5.2.x, source: US EPA, license: public domain, run_here: false}
  - {name: OpenSWMM, version: 6.0.0-alpha.3, branch: swmm6_rel, license: Apache-2.0, run_here: false}
units: US customary by default (CFS, ft); SI behind a toggle that converts slider values
ai_use: built with Claude (Anthropic); see AI use
---

# Four-Engine Pipe Comparator: what each solver pays for pressurization, on one shared benchmark

## What it does

Compares how HEC-RAS Pipe Networks, InfoWorks ICM, EPA SWMM5 and OpenSWMM 6 route unsteady flow through
closed conduits. It does three things: states each engine's scheme and capabilities with caveats attached;
computes live what pressurization costs each of them in stable timestep on a pipe you specify; and generates
a surcharge benchmark as a SWMM5 .inp file, the one format all four read, then scores returned hydrographs.
No engine runs inside the app. Everything stays in the browser.

## How it computes

Wave celerity, open channel: `c = sqrt(g*A/T)` with A and T from circular geometry at relative depth y/D.
Preissmann slot celerity: `c_slot = sqrt(g*A_full/(f*D))` for a slot of width `f*D`.
Courant bound: `dt = Cr*dx/(V + c)`.
Manning full-pipe capacity: `Q_full = (k/n)*A*R^(2/3)*sqrt(S)`, `k = 1.49` US, `1.0` SI, `A = pi*D^2/4`, `R = D/4`.
Gravity: one constant per file, `G_US = 32.174`, `G_SI = 9.81`.

OpenSWMM finite volume kernels, mirroring the engine:
- mesh: `n = max(FV_MIN_CELLS, ceil(L/FV_CELL_LENGTH))`, defaults 4 and 0 (no length target)
- static slot folded into the closure: `T_slot = g*A_full/c^2`, capped at `0.05*w_max`, from `FV_SLOT_CELERITY`
- explicit substep: `dt_sub = FV_CFL*dx_cell/(|V| + c)`, `FV_CFL` 0.5
- local time stepping: power-of-two tiers, macro cycle `2^(K-1)` base substeps

Hydrograph metrics, computed over the overlap window only, on a common resampled grid:
- NSE `= 1 - sum((cand-ref)^2)/sum((ref-mean(ref))^2)`
- KGE `= 1 - sqrt((r-1)^2 + (sd_c/sd_r - 1)^2 + (mu_c/mu_r - 1)^2)` (Gupta et al. 2009)
- volume by trapezoid on raw points; peak and time-to-peak are the exact piecewise-linear maxima,
  evaluated at raw interior points and at both clipped window endpoints
- a flat reference returns null for NSE, KGE and r rather than dividing by zero

Options the generator writes into the .inp: `FLOW_ROUTING DYNWAVE`, `SURCHARGE_METHOD` (SLOT or EXTRAN,
selectable), `VARIABLE_STEP 0.75`, `ROUTING_STEP 1`, `LINK_OFFSETS DEPTH`, `FORCE_MAIN_EQUATION H-W`,
`MIN_SURFAREA` and `HEAD_TOLERANCE` set per unit system. Manhole depth comes from one rule used by both
artifacts: `max(3*D, 10 ft US / 3 m SI)`.

## Inputs and outputs

Reads: two pasted `time, value` time series (comma, semicolon or tab; headers and hour/minute/second units
tolerated). Writes: a SWMM5 `.inp` (B1 surcharge ladder), an engine-neutral canonical model JSON always in SI,
a feature-matrix CSV, a terminology CSV, a benchmark scoreboard CSV, a hydrograph-metrics CSV, and an
optional animated GIF or WebM of a session.

## Checks

All four suites run against functions extracted from the shipped HTML, so there is one source and no drift.

- `verify-fv.js`, **39 checks**. Anchored to OpenSWMM's own documented values: slot width 0.0228 ft on a 3 ft
  pipe at `FV_SLOT_CELERITY` 100, half-full celerity 6.16 ft/s, the ratio of 16. Plus the mesh rule, the
  5 percent width cap, the inverse-square celerity relation, LTS tiers and macro cycles, and the three
  explicit-engine timesteps.
- `verify-core.js`, **57 checks**. Manning in both unit systems against hand arithmetic; the .inp and the
  canonical JSON generated from the same parameters and cross-checked on end time, every timeseries
  timestamp, unit-converted peak, all four inverts, manhole depth and freeboard, across three parameter sets;
  metrics against analytic anchors (identity NSE and KGE exactly 1, constant offset RMSE equal to the offset,
  doubled series KGE exactly `1 - sqrt(2)`, triangle volume `0.5*b*h`); the sparse-paste peak guard.
- `verify-theme.js`, **47 checks**. Both palettes parsed from the stylesheet, the duplicated dark block
  asserted byte-identical to its `data-theme` twin, and WCAG contrast measured on every shipped pair in both
  themes: 4.5:1 for text, 3:1 for figure inks.
- `smoke.js`, **61 checks**. Headless boot, every tab, every control, theme flip, unit round trip,
  deep links, and the whole Doc-essay contract (word counts, one image in the one-page size, four questions,
  six or more figures, a one-line summary under every heading, complexity box last).

Total **204 checks**, all green at this build.

Measured numbers this build reports, on a 3 ft pipe, 330 ft, 3 ft/s, Cr 0.75:
SWMM5 SLOT 2.75 s, SWMM5 EXTRAN 14.72 s, ICM 5 to 60 s (accuracy choice), HEC-RAS 82.5 s,
SWMM6 FV 0.400 s substep on an 82.5 ft cell. Half-full celerity 6.16 ft/s; 1 percent slot 87.07 ft/s.
Q_full 21.15 cfs, generated peak 42.30 cfs. Sample hydrograph pair: NSE 0.847, KGE 0.864, Pearson r 0.924,
peak error -8.00 percent, volume error -8.00 percent, lag +10.0 min, RMSE 1.302.

## Complexity

SWMM App Complexity Meter, analyzer 1.7.0, baseline HC-2026-11-10-h, HydroCouple = 100.
**Index 52.9** across all hand-written source; the shipped .html alone reads 47.7.
Size 42.5, Structure 61.8, Test evidence 6.0, SWMM vocabulary 71.9.
Measured, not estimated. Generated and third-party code excluded.

## What this does not show

1. **No engine has ever run inside this page.** All 128 capability cells are a reading of documentation,
   release notes, source and upstream measurements. Every one is a claim to re-verify in your own build.
2. **The finite volume cost figures are quoted, not measured here.** Both the superseded August column
   (peak deviation 37.1 / 15.3 / 7.2 percent, wall clock about 7x to 34x dynamic wave) and the current one
   (about 3 percent at every resolution, wall clock at parity with dynamic wave or better, reference
   continuity 0.024 percent) are the upstream commit's own numbers.
3. **Shock and dam-break accuracy figures are quoted** from the OpenSWMM test suite, not reproduced.
4. **SWMM6 inherited hydrology is marked as lineage, not verified.** LID, snowmelt and groundwater rows say
   so. Hydraulic parity with SWMM5 on the classic corpus is close but not exact: a wide metric sweep found a
   0.84 percent worst-case flooding peak and one model disagreeing on the number of reporting periods.
5. **The lab computes a single-reach Courant bound.** A real network's step is set by its worst link under
   whatever variable-step control is running, which this page does not model.
6. **The benchmark scoreboard ships empty.** Filling it would mean publishing runs that were never made.
7. **B2 to B5 have no generators yet.** Only B1 generates; the others carry expected-behaviour notes and
   recording grids.
8. **Comparison trap, worth repeating:** SWMM6 reports conduit flow as the mean face mass flux over the
   reporting step, not the end-of-step momentum state. Upstream found a force main delivering 25 cfs whose
   cell momentum state held 18.4. Record which quantity you pulled before calling a difference physical.

## How to reproduce

```
node verify-fv.js        # 39
node verify-core.js      # 57
node verify-theme.js     # 47
node smoke.js            # 61   (requires jsdom)
```
Each suite extracts its functions from `four-engine-pipe-comparator.html` by name, so the tests
exercise the shipped code rather than a copy. The B1 model is regenerated from the sliders;
the default US state is D = 3 ft, n = 0.013, S = 0.001, L = 400 ft, peak multiplier 2.

## Credits and licenses

EPA SWMM5: United States Environmental Protection Agency, public domain.
OpenSWMM 6: Caleb Buahin and the OpenSWMM team at HydroCouple; the finite volume solver is the work of
Caleb Buahin and Corinne Wiesner-Friedman. Apache-2.0 on the `swmm6_rel` branch.
HEC-RAS: US Army Corps of Engineers, Hydrologic Engineering Center.
InfoWorks ICM: Autodesk. SWMM5+ coordination: CIMM.org.
Page by Robert Dickinson, SWMM Enablement.

## AI use

Built with Claude (Anthropic). Claude wrote all page code, the four Node test suites, the build scripts,
the Doc essay, every figure, and this file. Claude did the source reading behind the engine claims:
HEC-RAS 7.0 release notes, the OpenSWMM source tree and Chapter 8 of its hydraulics manual, the commit
history around the junction change, and the PyPI release record. Bob Dickinson set the brief, supplied the
engine knowledge, identified that the SWMM6 column was wrong to be called roadmap when the finite volume
solver was already shipping, supplied an outside review whose five bug reports were all real, and decided
what to claim and what to mark unverified. Two corrections were made by Claude against its own earlier
work in this build: version 1.4 shipped finite volume cost figures already superseded by the junction
change, and a reported dark-mode fault turned out on measurement to be a stale build being force-darkened
by the browser rather than a defect in the page.

## Changes

`1.5.0 (2026-11-18)`: Doc tab and About tab added with the full essay, .docx and this .md. US customary
is now the default unit system. Corrected the SWMM6 finite volume facts superseded by the November
rebuild: algebraic junctions return no timestep bound, the cost case turned over, 22 FV_ keys parse as
20 live plus 2 retired, reported conduit flow is the mean face mass flux. Fixed two defects found by the
suites: a second gravity constant (32.2 against the file's G_US = 32.174), and `--ink-faint` at 2.43:1 on
the figure background in light mode.
`1.4.0`: SWMM6 column rewritten for `FLOW_ROUTING FV`; FV mesh controls and a computed substep added to
the Numerics Lab; 24 matrix rows, 3 Rosetta concepts, 5 benchmark notes and 3 advisor requirements updated.
`1.3.0`: Five reported bugs fixed; hydrograph plot, KGE, deep-linkable tabs, must-have advisor weighting,
modal accessibility, print stylesheet.
`1.2.0`: Hydrograph Compare, canonical JSON export, results-extraction guidance; HEC-RAS data corrected
to 7.0.1.
`1.1.0`: Dark mode with a `prefers-color-scheme` fallback; engine palette corrected for WCAG contrast.
`1.0.0`: Six tabs, numerics lab, feature matrix, rosetta, B1 generator, decision advisor.
