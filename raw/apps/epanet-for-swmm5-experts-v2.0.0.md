---
name: EPANET for SWMM5 Experts
file: epanet-for-swmm5-experts.html
version: 2.0.0
date: 2026-11-12
author: Robert Dickinson
links: {repo: https://github.com/SWMMEnablement/EPANET-SWMM-Experts, site: https://www.swmm5.org}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: USEPA/Stormwater-Management-Model, commit: 07c371f8a0d477da1d9d4e7c0d75719664f62fec, license: public domain}
  - {name: EPANET, version: 2.2, source: OpenWaterAnalytics/EPANET tag v2.2, commit: 4d8d82ddc260fce216af9321fc3d9a4646ac6827, license: MIT}
  - {name: EPANET, version: 2.3.5, source: OpenWaterAnalytics/EPANET tag v2.3.5, commit: 444725fbf16ab28b0470ef0ed281dc4849d49583, license: MIT}
units: US customary (ft, cfs, gpm, psi) by default; SI display behind a switch
ai_use: built with Claude (Anthropic); see AI use
---

# EPANET for SWMM5 Experts: EPANET explained in SWMM5 terms, checked against both engines

## In three points
- **What:** A single HTML file of 35 tabs that explains the EPANET water distribution engine to engineers who already know SWMM5: objects, demands, head loss formulas, solvers, pumps, valves, water quality and file formats, mapped from one program to the other, with calculators. Version 2.0 adds a Verify tab (engine comparisons and a corrections register), an About tab and a Doc tab.
- **So what:** Version 2.0 ran the central claim through EPA SWMM 5.2.4, EPANET 2.2 and EPANET 2.3.5, all built from source. For one 12-in pipe, 1,000 ft long, Hazen-Williams C of 130, at six flows from 100 to 2,000 gpm, SWMM 5.2.4's FORCE_MAIN matched the formula within 0.001 ft and EPANET 2.2 matched to its 0.01 ft print resolution. The same work found 15 errors in version 1, among them printed source code that is not in SWMM5; all 15 are corrected and listed. 47 in-page tests compare the page's formulas with the stored engine numbers at every load.
- **Now what:** Use it to read or build EPANET models from what you know of SWMM5. Check before relying on the 19 of the original 32 tabs that were not audited beyond a source scan, since they were written by the same process that produced the 15 errors. The engine comparison is one pipe in steady flow, and no person has yet reviewed version 2.0.

In one sentence: EPANET for SWMM5 Experts explains EPANET in SWMM5 terms. Version 2.0 ran its central claim through both engines: for one 12-inch pipe at six flows, SWMM 5.2.4 and EPANET 2.2 report the same head loss.

In one paragraph: EPANET for SWMM5 Experts is a single-file guide of 35 tabs that explains the EPANET water distribution engine to people who already know SWMM5. Version 2.0 checked the app against the engines themselves. EPA SWMM 5.2.4, EPANET 2.2 and EPANET 2.3.5 were built from source and given one pipe: 12 inches, 1000 ft, Hazen-Williams C of 130, at six flows from 100 to 2000 gpm. The engines agreed with each other and with the formula at every flow. The same work found 15 errors in version 1 of the app, among them printed source code that is not in SWMM5. All 15 are corrected and listed. Most of the other tabs have not been audited line by line.

## What it does

A single HTML file of 35 tabs for engineers who know SWMM5 and need to read or build EPANET models. It maps objects, demands, head loss formulas, solvers, pumps, valves, water quality and file formats from one program to the other, with calculators. It does not run either engine in the browser. Engine results shown in the page were produced ahead of time by engines built from source and are stored in the page with the input files that made them. Version 2.0 adds a Verify tab (engine comparisons and a corrections register), an About tab and a Doc tab (the essay).

## How it computes

All internal arithmetic for the checks is in feet, cfs and ft/s.

- Hazen-Williams friction slope, full pipe: `Sf = V^1.852 / ((1.318 C)^1.852 R^1.1667)`, R = D/4. Source: SWMM 5.2.4 `src/solver/forcmain.c:78` (`r = 1.318*xsect.rBot*pow(lengthFactor, 0.54)`) and `forcmain.c:106` (`return xsect.sBot * pow(v, 0.852) / pow(hrad, 1.1667);`). EPANET 2.2 resistance form: `src/hydcoeffs.c:95` (`4.727 * L / pow(e, hyd->Hexp) / pow(d, 4.871)`).
- Equivalent Manning n for a force main: `n = 1.067 / C * (D / S0)^0.04`, D in ft, S0 = conduit slope. Source: `forcmain.c:54`. Called once from `link.c:1094` (conduit_validate). Used only when the pipe is not full: `dwflow.c:212` (`if ( xsect->type == FORCE_MAIN && isFull )` selects the Hazen-Williams or Darcy-Weisbach slope).
- Where C is entered: Geom2 of the FORCE_MAIN line in [XSECTIONS] (stored as `xsect.rBot`). Darcy-Weisbach roughness height goes in the same field, in inches (US) or mm (SI).
- Minimum conduit drop: `link.c:63` `MIN_DELTA_Z = 0.001` ft, with WARNING 04.
- Manning: `Sf = (V n / (1.486 R^(2/3)))^2`. `consts.h:46` `PHI 1.486`. EPANET Chezy-Manning uses 1.49: `hydcoeffs.c:101`.
- Darcy-Weisbach friction factor: logic of `forcemain_getFricFactor` in forcmain.c (64/Re to Re 2000, interpolation to 4000, Swamee-Jain above), kinematic viscosity 1.1e-5 ft2/s, g = 32.2.
- SWMM5 dynamic wave defaults: `dynwave.c:61` `OMEGA = 0.5`, `dynwave.c:63` `DEFAULT_HEADTOL = 0.005` ft, `dynwave.c:66` `DEFAULT_MAXTRIALS = 8`; `project.c:846` `SurchargeMethod = EXTRAN`, `project.c:854` `CourantFactor = 0.75`, `project.c:867` `RouteStep = 20`, `project.c:868` `MinRouteStep = 0.5`. Optional slot width: `dwflow.c:587` `xsect->wMax * 0.5423 * exp(-pow(yNorm, 2.4))`.
- EPANET defaults: `input1.c:25` `MAXITER 200`, `input1.c:26` `HACC 0.001`.
- EPANET 2.3 pipe leakage (FAVAD): `Q = 0.6 sqrt(2g) (Ao + m H) sqrt(H)`, Ao in mm2 per 100 length units. Source: EPANET 2.3.5 `src/leakage.c:153` (`c_orif = 4.8149766 * 1.e-6`) and lines 153 to 190. A pipe between two junctions puts half its leak coefficient on each end; a pipe with one junction end puts all of it there.
- SWMM5 pump curve types: `enums.h:419` to `423`, TYPE1 to TYPE5, plus IDEAL. A PUMP3 curve is entered head first, then flow.

## Inputs and outputs

No file input. The page offers seven input files as text (download where the browser allows, otherwise copy): one_pipe_epanet.inp, one_pipe_swmm_forcemain.inp, one_pipe_swmm_circular_equiv_n.inp, one_pipe_swmm_partial_flow.inp, fm_station.inp, dead_end_zero_demand.inp, favad_leak_epanet23.inp. Calculator state can be shared through the URL hash. The Reference tab can open a printable equations document.

## Checks

Mechanical checks, all run 2026-11-12. Test pipe: 12 in diameter, 1000 ft, C = 130, slope 0.001, boundary head 10 ft. Head loss = reported upstream head minus 10 ft.

| Flow, gpm | H-W formula, ft | SWMM 5.2.4 FORCE_MAIN | EPANET 2.2 | EPANET 2.3.5 | SWMM 5.2.4 CIRCULAR n = 0.01082 | Manning vs H-W |
|---|---|---|---|---|---|---|
| 100 | 0.036 | 0.036 | 0.04 | 0.04 | 0.027 | -24.0% |
| 250 | 0.195 | 0.195 | 0.19 | 0.19 | 0.169 | -13.0% |
| 500 | 0.702 | 0.702 | 0.70 | 0.70 | 0.677 | -3.5% |
| 605 | 0.999 | 0.999 | 1.00 | 1.00 | 0.992 | -0.8% |
| 1000 | 2.535 | 2.535 | 2.53 | 2.53 | 2.709 | +6.9% |
| 2000 | 9.151 | 9.151 | 9.15 | 9.15 | 10.836 | +18.4% |

- V1. SWMM 5.2.4 FORCE_MAIN matched the formula within 0.001 ft at 6 of 6 flows. EPANET 2.2 matched to its 0.01 ft print resolution.
- V2. Partly full (free outfall, 0.2, 0.5, 1.0 cfs): FORCE_MAIN and CIRCULAR with n = 0.01082 ran at depths 0.250, 0.397, 0.589 ft, identical to 0.001 ft. CIRCULAR with n = 0.013: 0.275, 0.440, 0.650 ft.
- V3. Manning with the equivalent n equals Hazen-Williams at 605 gpm (friction slope = pipe slope). It reads -24.0% at 100 gpm and +18.4% at 2000 gpm.
- V4. Flat main: WARNING 04, slope 1e-6, equivalent n 0.014263. Full-flow head loss unchanged (0.702 ft at 500 gpm). Partly full at 0.3 cfs: FORCE_MAIN depth 0.462 ft = CIRCULAR with n = 0.014263 (0.462 ft); CIRCULAR with n = 0.01082 gives 0.421 ft.
- V5. Adverse main (rises 5 ft), 500 gpm: no error or warning, head 15.702 ft against a 15 ft outfall.
- V6. Darcy-Weisbach, roughness 0.01 in, head loss in ft:

| Flow, gpm | SWMM 5.2.4 | EPANET 2.2 |
|---|---|---|
| 250 | 0.179 | 0.18 |
| 500 | 0.663 | 0.66 |
| 1000 | 2.523 | 2.52 |
| 2000 | 9.783 | 9.78 |

- V7. EPANET Chezy-Manning, n = 0.013: 0.24, 0.97, 3.89 ft at 250, 500, 1000 gpm, matching the formula with 1.49 (not 1.486; 0.54% apart in head loss).
- V8. fm_station.inp (wet well, Type 3 pump, 2000 ft of 18 in force main, gravity outlet, 6 h, 2 cfs inflow): no errors or warnings, 8 pump start-ups, 6.67 cfs average while on, wet well peak 6.0 ft, routing continuity -0.777%. Same file with the pump curve typed flow then head: no errors or warnings, 0 start-ups, 0 cfs, wet well at 12.0 ft, 0.263 million gallons flooded.
- V9. EPANET dead end with two zero-demand junctions: balanced after 2 trials, heads 149.96 ft at all three junctions.
- V10. The version 1.x force main example as printed: ERROR 203 (five-field [CONDUITS] line), ERROR 119 (Geom2 = 0), ERROR 205 ([END]).
- V11. Defaults read from report files: SWMM 5.2.4 Surcharge Method EXTRAN, Maximum Trials 8, Head Tolerance 0.005000 ft; EPANET 2.2 Hydraulic Accuracy 0.001, Maximum Trials 200, demand model DDA.
- V12. EPANET 2.3.5 heads equal EPANET 2.2 heads at 6 of 6 flows. `[LEAKAGE] P1 10 0.0` on a 1000 ft pipe at 149.94 ft of head: 28.485 gpm in the engine, 28.484 gpm from the formula with the head rounded to 149.94 ft. EPANET 2.2 stops on that file with Error 201.
- V13. Null-effect control: one SWMM5 input file run twice gave identical reports apart from time stamps.
- In-page tests: 47 assertions recompute the page's formulas and compare them with the stored engine numbers at every load (47 of 47 pass). Tolerances: 0.002 ft against SWMM5, 0.006 ft against EPANET.
- Headless browser run (Chromium, Playwright): all 35 tabs open with no script errors, in the dark and light themes, with and without Chart.js available.
- Source scan: every passage that names a SWMM5 or EPANET source file or shows a C function definition was compared with the source trees.
- Human review: none yet for version 2.0.

## What this does not show

- One pipe, one diameter, one C, one slope, steady flow. No loops, tanks, valves or pumps in the engine-to-engine comparison.
- No field data. Agreement between engines is not agreement with a real main.
- No test of the SWMM5 unsteady solution. Neither engine models water hammer.
- 13 of the original 32 tabs had passages corrected. 19 were not changed and were not audited beyond the source scan. A wrong number in a table that names no source would not have been caught.
- SI mode was exercised in a browser, not against an SI engine run.
- One machine, gcc 13.3 on Linux. No timing claims.
- Legacy diagrams and code blocks keep a dark background in the light theme.
- Corrections register for version 1.x, numbered in the Verify tab:
  - C-1 invented `forcemain_getEquivN()` shown as SWMM5 source
  - C-2 claim that SWMM5 drops the slope term, with a 20 to 40% error
  - C-3 C placed in [CONDUITS] instead of [XSECTIONS] Geom2
  - C-4 example .inp that the engine rejects
  - C-5 file name forcemain.c (it is forcmain.c)
  - C-6 Preissmann slot given as the default surcharge method (default is EXTRAN)
  - C-7 dynamic wave described as single-pass explicit (it uses Picard iterations)
  - C-8 EPANET TRIALS 40 and ACCURACY 0.01 given as defaults (200 and 0.001)
  - C-9 zero-demand dead ends said to need a tiny demand
  - C-10 wrong SWMM5 pump type table
  - C-11 Manning constant 1.49 in SWMM5 calculations (1.486)
  - C-12 [END] said to be required in EPANET
  - C-13 SI mode of the force main converter mixed units
  - C-14 a console test that failed on every load
  - C-15 four invented source functions in the Leakage tab, and FAVAD pipe leakage credited to EPANET 2.2

## How to reproduce

1. Build EPA SWMM 5.2.4 from the commit above. With gcc at -O2 or higher on Ubuntu 24 the command line stops with "buffer overflow detected" at "Retrieving project data" (a glibc fortify false positive on `realpath` in `swmm_open`); build with `-U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0`.
2. Build EPANET from tags v2.2 and v2.3.5.
3. Download the input files from the Verify tab. `runepanet one_pipe_epanet.inp out.rpt` and read the head at J1. `runswmm one_pipe_swmm_forcemain.inp out.rpt` and read the last head at J1. Name no .out file on the SWMM5 command line if you want the time series printed in the report.
4. Change the flow (the negative demand at J1 in EPANET, the [INFLOWS] baseline in SWMM5) to 100, 250, 500, 605, 1000 and 2000 gpm.
5. Open the page and read the test count on the Verify tab, or the browser console.

## Credits and licenses

- Lewis A. Rossman (US EPA): author of EPANET and the author named in the SWMM5 source files quoted. Michael Tryby (US EPA) and Robert Dickinson are named with him in the header of dynwave.c.
- EPA SWMM 5.2.4, US Environmental Protection Agency, public domain. Source excerpts are copied from that repository.
- EPANET 2.2 and 2.3.5, US EPA and the Open Water Analytics community, MIT license.
- Chart.js 4.4.1, MIT license. Fonts Outfit and JetBrains Mono, SIL Open Font License.
- This app: MIT license, Copyright (c) 2026 Robert Dickinson.

## AI use

This app was built with AI, and so were its errors. Robert Dickinson chose the subject, supplied the source material and the reviews, set the standard that numbers must come from the engines, and is responsible for the work.

**Versions 1.0 and 1.1 (March 2026).** Claude, the AI model made by Anthropic, wrote the first build in a chat session, from his direction and attachments. The expansion to 32 tabs was done in Replit: 17 of the 20 commits in the repository come from the Replit account. The repository does not record which AI tools were used there, beyond a pasted review that names Claude. The errors listed above were written by AI in those versions. AI-written reviews then graded the equations and the source code display A and A+ without running an engine.

**Version 2.0 (November 2026).** Claude built EPA SWMM 5.2.4, EPANET 2.2 and EPANET 2.3.5 from source, wrote and ran the test input files, read the source files cited, found and corrected the 15 errors, and wrote the Verify, About and Doc tabs, the light theme, this essay, its Word copy and the technical summary.

**How it was checked.** The checks are mechanical. 47 comparisons of page formulas against engine output run at every load, and a headless browser opened all 35 tabs in both themes with no script errors. They are not the judgment of the AI about its own work.

**What no person has checked.** No person has yet reviewed the version 2.0 changes. Nineteen of the original 32 tabs were not audited, and they were written by the same process that produced the errors found.

## Changes

- `2.0.0 (2026-11-12)`: 15 corrections from source and engine checks; Verify, About and Doc tabs; 47 engine-pinned tests; verified force main station example; EPANET 2.3 leakage note; verbatim source excerpts in the Leakage tab; light and Auto themes; Reference sections 15 and 16 no longer show under every tab; Chart.js pinned to 4.4.1 with an offline guard.
- `1.1 (2026-03)`: expanded to 32 tabs in Replit.
- `1.0 (2026-03-15)`: first release, 11 tabs.
