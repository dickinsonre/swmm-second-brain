---
name: ICM River Reach Modeler
file: icm-river-reach-modeler.html
version: 1.1.0
date: 2026-11-12
author: Robert Dickinson
links: {artifact: published Claude artifact (private until shared), netlify: not yet, repo: none}
source: Lovable app "ICM River Reach Modeler", data export of 2026-10-25 (45 files)
engines:
  - {name: hydro.js, version: 1.1.0, language: JavaScript, units: SI internally, license: same as the app}
  - {name: EPA SWMM, version: 5.2.4, use: offline check of the benchmark reach only (pyswmm 2.2.0, swmm-toolkit 0.17.0), license: public domain}
units: US customary by default (ft, cfs); SI on a header toggle; arithmetic in SI
ai_use: built with Claude (Anthropic) under Bob Dickinson's direction; see AI use
---

# ICM River Reach Modeler: steady 1D river reach hydraulics for SWMM5 and InfoWorks ICM modellers

## In three points
- **What:** A single-file teaching and checking tool for one-dimensional river reaches, from Bob's Lovable app: it walks through building a reach the way InfoWorks ICM does and gives seven steady-flow calculators (Froude and regime, hydraulic jump, gradually varied flow, culverts by FHWA HDS-5, weirs and orifices, compound channels by the Divided Channel Method, rating curves with SWMM5 .inp import), plus an ICM benchmark reach with the expected water level at every section.
- **So what:** The benchmark reach's gradually varied flow matches EPA SWMM 5.2.4 within 0.0001 ft over 17 sections for the M1 case (outfall 8.0 ft, upstream depth 6.784 ft) and 0.0006 ft for the M2 case (outfall 4.2 ft); 55 of 55 checks in tests.js pass, and an outside review checked all 36 HDS-5 inlet values against Table A.1.
- **Now what:** Use it to learn ICM's river-reach objects and to have an expected answer before building the reach in ICM. Steady, prismatic flow only; no ICM run of the benchmark or of the four Ruby scripts has been made yet.

## What it does
A single-file teaching and checking tool for one-dimensional river reaches. It walks through building a reach the way ICM does (GeoPlan link, Cross Section Lines, panels, bank spill, Inflow and Level events), and gives seven steady-flow calculators: Froude and regime, hydraulic jump, gradually varied flow (GVF), culverts by FHWA HDS-5, weirs and orifices, compound channels by the Divided Channel Method, and rating curves with SWMM5 .inp import. An ICM benchmark tab gives one reach to build in ICM, with the expected water level at every section, already checked against EPA SWMM 5.2.4. Reference tabs cover SWMM5 open and closed shapes, LID, ICM 2D coupling objects and four ICM Ruby scripts.

## How it computes
All in `hydro.js`, SI units, g = 9.80665 m/s². Display converts with 1 ft = 0.3048 m, 1 cfs = 0.0283168 m³/s.
- Normal depth: bisection on (1/n)·A·R^(2/3)·S^(1/2) = Q. Critical depth: bisection on Q²T/(gA³) = 1.
- GVF: dy/dx = (S0 − Sf)/(1 − Fr²), fourth-order Runge–Kutta from the control end (downstream if the boundary depth is above yc, upstream if below), sub-stepped so no stage moves more than 1% of yc. Stops at critical depth and reports the stations it reached (`r.first`, `r.last`, `hasUp`, `hasDn`).
- Jump: momentum function M = Q²/(gA) + b·y²/2 + z·y³/3, sequent depth by bisection; Chow jump classes; USBR EM-25 basin types.
- Culvert, HDS-5 (2012) Appendix A form 1: X = Ku·Q/(A·D^0.5), Ku = 1.811 SI. Unsubmerged (X ≤ 3.5) HW/D = Hc/D + K·X^M + Ks·S; submerged (X ≥ 4.0) HW/D = c·X² + Y + Ks·S. For 3.5 < X < 4.0, a cubic Hermite meeting each curve with its own value and slope (HDS-5 says to draw a curve between and tangent to both; this is an approximation). Outlet control HW = h0 + (1 + Ke)·V²/2g + hf − L·S, h0 = max(TW, (dc + D)/2). Nine K, M, c, Y, Ke sets.
- Culvert capacity at the allowable headwater: bisection only when HW(Q → 0) < HWa (`findRoot` requires a sign change); otherwise "No feasible forward discharge at the allowable headwater".
- Weirs: sharp Q = Cd(2/3)√(2g)LH^1.5; broad Q = Cd√g·L·H^1.5 (ideal Cd 0.544); ogee and Cipoletti Q = CLH^1.5; V-notch Q = Cd(8/15)√(2g)tan(θ/2)H^2.5. Approach velocity Q/(width·(P + H)). Orifice Q = Cd·A·√(2gH).
- Compound channel: DCM with vertical interfaces, main channel keeps the water column above the banks, sloped floodplains wet only h/s; α, β, Lotter and Horton–Einstein n.
- Rating curve: Manning for a trapezoid; best-fit n by least squares on Q (closed form, 1/n = ΣQi·ki/Σki²).
- ICM benchmark: `H.benchmark` runs the GVF with one station per section, builds four-vertex trapezoidal sections (height = 1.5 × max depth, rounded up to whole feet), a 21-row conveyance table K = A·R^(2/3)/n, and an inverse-slot estimate (0.1 m × 1 m, n = 0.01, per ICM Help). `H.benchInp` writes the same reach as a SWMM5 file: a junction per section, FIXED outfall, DYNWAVE, 5 s step, 6 h, inflow as an [INFLOWS] baseline.

## Inputs and outputs
- Reads: SWMM5 .inp (OPTIONS FLOW_UNITS, LINK_OFFSETS DEPTH or ELEVATION; JUNCTIONS, OUTFALLS, STORAGE, DIVIDERS inverts; CONDUITS; XSECTIONS TRAPEZOIDAL, RECT_OPEN, TRIANGULAR). '*' offsets and ends below the node invert follow SWMM5 (at the invert). Flat, adverse or missing slopes are flagged, never taken.
- Writes: CSV per calculator, HTML report per calculator, A/B scenario CSV matched by result name and unit, GIF or WebM of the current view, the Doc essay as .docx. Benchmark: sections grid CSV (key, X, Y, Z, roughness_Manning, new_panel), Cross Section Lines CSV (line_id, vertex, X, Y, Z), conveyance CSV, SWMM5 .inp, benchmark sheet .html, levels CSV with pasted ICM results.
- Keeps in browser storage only: theme, units, scenarios, pasted ICM benchmark results.

## Checks
Mechanical: 55 of 55 checks in `tests.js` pass on the shipped `hydro.js`. Groups: closed forms (critical depth, Bélanger, wide-channel normal depth), conservation (jump momentum, zone sums, Lotter K), independent re-derivation (standard-step backwater, HDS-5 in English units), the original Lovable formulas measured, and 17 added in v1.1:
- culvert: no capacity when HW(Q→0) ≥ allowable (TW 10 ft, HWa 8 ft): HW0 9.000 ft, Qcap NaN
- culvert: default case still bisects to HW = allowable: Qcap 145.58 cfs
- root(): NaN without a sign change
- inlet transition continuous at X = 3.5 and 4.0 for all 9 inlets: largest jump 8.85e-8 D
- inlet transition never decreases with X
- inp ELEVATION: slope 0.010, not 0.020: S 0.01
- inp ELEVATION: '*' puts the end at the node invert
- inp: adverse and flat slopes are flagged: adverse, flat
- inp DEPTH: offsets are heights above the inverts
- M3 preset stops short of the downstream end: last station 47.9 ft of 1600
- S1 preset stops short of the upstream end: first station 1570.5 ft
- M1 reaches both ends
- benchmark: 17 sections, profile reaches both ends, outfall depth held: M1, upstream 6.784 ft
- benchmark .inp: 16 junctions, 16 conduits, FIXED outfall at 108 ft
- slot estimate: 0.1 m², about 1.5 cfs at S = 0.001: 1.467 cfs
- GVF matches EPA SWMM 5.2.4 on the benchmark reach (M1, outfall 8 ft): largest difference 0.0001 ft over 17 sections
- GVF matches EPA SWMM 5.2.4 on the benchmark reach (M2, outfall 4.2 ft): largest difference 0.0006 ft over 17 sections

Against EPA SWMM 5.2.4 (benchmark reach, run for this build, dry start, 6 h): largest depth difference over 17 sections 0.0001 ft for the M1 case (outfall 8.0 ft, upstream depth 6.784 ft) and 0.0006 ft for the M2 case (outfall 4.2 ft). Steady by the first hour. Flow routing continuity error 0.141% (M1 run, .rpt).

Defaults for reference: culvert (4 ft RCP, square edge, 175 cfs, 100 ft, S 0.01, TW 2.5 ft) capacity 145.6 cfs at 8 ft; with TW 10 ft, HW at zero flow 9.00 ft and no feasible capacity. M3 preset stops at station 47.9 ft of 1,600. Slot estimate 1.47 cfs (0.29% of 500 cfs).

By hand: the nine HDS-5 inlet sets match a published reproduction of Table A.1; an outside review (Nov 2026) checked all 36 values against Table A.1 itself and found them right. ICM field names (roughness_Manning, new_panel, left_2d_zone_id, zone_id) checked against Autodesk ICM Help 2027 and the Innovyze help. Ruby scripts: Ruby 3.3 syntax check and a run against a mock ICM network (branching reach, three-panel sections).

## What this does not show
1. Steady flow only; no unsteady routing and nothing that tests a Saint-Venant solver.
2. Prismatic sections; no surveyed sections, bridges, expansions or contractions.
3. The Froude tab joins two end depths with a straight line; it is not a profile.
4. Culverts: nine HDS-5 inlet sets, no roadway overtopping, tapered inlets or HY-8 profile types. The 3.5 < X < 4.0 transition is an approximation of a hand-drawn curve.
5. DCM without interface shear over-predicts just above bankfull.
6. No comparison with an ICM run yet. The benchmark tab exists for that.
7. ICM Ruby scripts not run in ICM. WSTableInfo#results_fields is assumed; the scripts stop with a message if it is missing.
8. ICM's free-outfall calculation is not described; the help pages read for this build do not cover it.
9. ICM 2D cards and knowledge-base entries not marked "checked" were carried over from the original app unchecked.
10. Not done by a person: an ICM run of the benchmark, an ICM run of the Ruby scripts, a check of the corrections against the printed HDS-5.

## How to reproduce
- `node tests.js` in the app folder: the 55 checks, including the two frozen SWMM 5.2.4 runs (`doc/swmm524_m1.json`, `doc/swmm524_m2.json`).
- SWMM5 runs: download "SWMM5 (.inp)" from the ICM benchmark tab (defaults, then outfall depth 4.2 ft), run in EPA SWMM 5.2.4, read node depths J000 to OUT at 06:00.
- ICM: follow the benchmark sheet; paste the levels at the 17 sections into the tab.
- Review scenarios in the page: culvert TW 10 ft; weir saved as A and orifice as B, then Comparison CSV; GVF M3 preset then Report; rating import of an .inp with LINK_OFFSETS ELEVATION.

## Credits and licenses
- Original app and direction: Robert Dickinson (Lovable app "ICM River Reach Modeler").
- FHWA HDS-5, Hydraulic Design of Highway Culverts, 3rd ed. (FHWA-HIF-12-026, 2012). Kitsap County Stormwater Design Manual, Appendix F (HDS-5 transition wording, Table F.3). tbn2net reproduction of Table A.1.
- US EPA SWMM 5.2 User's Manual; EPA SWMM 5.2.4 via pyswmm and swmm-toolkit.
- Autodesk InfoWorks ICM Help 2027: River Reach Data Fields, Build sections from lines, Running simulations on the river model, inverse Preissmann slot, Conveyance Data Editor. Innovyze ICM help: Inline Bank, Inline Bank Data Fields, Inflow and Level Events.
- Ven Te Chow, Open-Channel Hydraulics (1959); USBR Engineering Monograph 25; Bodhaine, USGS TWRI 3-A3 (1968).
- Libraries loaded at run time: html2canvas 1.4.1, gif.js 0.2.0 (MIT).

## AI use
Built with Claude (Anthropic). v1.0 (2026-10-25): Claude read the Lovable export, wrote hydro.js and its checks, rebuilt the calculators, corrected the quiz and reference errors, rewrote the Ruby scripts, and wrote the app, the Doc essay and the .docx. v1.1 (2026-11-12): from an outside review Bob supplied, Claude reproduced each calculation finding, fixed it and added checks, read the Autodesk and Innovyze help pages cited and rewrote the ICM guidance and Ruby scripts, built the benchmark and ran it in EPA SWMM 5.2.4, and updated the About tab, the Doc, the .docx and this file. Bob Dickinson directed the work and is responsible for it.

## Changes
- 1.1.0 (2026-11-12): 9 v1.0 defects fixed (culvert capacity bracket, LINK_OFFSETS ELEVATION slope, import carry-over, scenario matching by name and unit, GVF end labels, HDS-5 tangent transition, roughness_Manning, results_fields checks, ICM guidance); ICM benchmark tab with SWMM5 twin; 17 new checks; Doc sections "A second pair of eyes" and "A reach you can build and check".
- 1.0.0 update (2026-11-05): Make a GIF sweeps the current view's main input with axes held steady.
- 1.0.0 (2026-10-25): rebuilt from the Lovable export; 44 corrections listed on the About tab.
