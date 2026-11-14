---
name: Topsoil Recovery Check
file: index.html (Netlify folder topsoil-recovery-site/)
version: 2026-11-12
date: 2026-11-12
author: Robert Dickinson
links: {netlify: Bob's deploy of topsoil-recovery-site/ (URL not recorded here), artifact: none, repo: https://github.com/SWMMBobSWMM6/swmm524-perched (branch van-genuchten)}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: USEPA/Stormwater-Management-Model tag v5.2.4, commit: 7952ca83, license: public domain, wasm_sha256: d001434e}
  - {name: EPA SWMM 5.2.4 + MaxInfil fix, version: 5.2.4, source: same + modhorton-maxinfil-fix.patch (OpenSWMM 5.3.0's fix), license: public domain, wasm_sha256: 034bc710}
  - {name: swmm524-perched, version: 5.2.4 + SOIL2/STRUCT/VG, source: SWMMBobSWMM6/swmm524-perched, branch: van-genuchten, commit: 548e5fbf (engine source unchanged since f8932013), license: none stated in repo (EPA base is public domain), wasm_sha256: 2bca9e49}
  - {name: OpenSWMM legacy, version: 5.3.0-beta.3, branch: swmm6_rel, commit: 13746831, license: Apache-2.0, wasm_sha256: c87b5626}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: 13746831, license: Apache-2.0, wasm_sha256: d80bb560}
units: US customary (in, in/hr, in/day, acres, cfs)
ai_use: built with Claude (Anthropic); see AI use
---

# Topsoil Recovery Check: how SWMM credits decompacted topsoil over compacted clay

## What it does

Answers one question with engine runs: how much of a storm does 4 in of decompacted, amended topsoil over 24 in of compacted sandy clay capture in SWMM, winter and summer, and how much does that depend on which SWMM setup describes the soil? It compares Modified and Standard Horton, three LID bio-retention setups, and swmm524-perched (a second soil layer with a Green-Ampt interface, plus an optional van Genuchten rule) on single storms, synthetic seasons and an 8 in design storm. Five engines run in the page as WebAssembly, so a reader can change the soils and rerun. Written for the people discussing Chesapeake Bay soil-restoration credits and for SWMM modelers.

## How it computes

Site: 1 acre, 100 % pervious, 2 % slope, 0.05 in depression storage. Monthly PET (in/day, Jan to Dec): 0.02 0.03 0.06 0.10 0.14 0.17 0.18 0.16 0.12 0.07 0.04 0.02.

Soils (study assumptions, not measured):

| Layer | Thick (in) | Porosity | FC | WP | Ksat (in/hr) | Suction (in) |
|---|---|---|---|---|---|---|
| Decompacted, amended topsoil | 4 | 0.50 | 0.30 | 0.15 | 1.0 | 3.5 |
| Compacted sandy clay (Rawls, Ksat halved) | 24 | 0.430 | 0.321 | 0.221 | 0.01 | 9.45 |

Setups (keys used in the scripts):

- H0: Modified Horton, f0 3 in/hr, fmin 0.01, Kd set so 0.80 in is infiltrated above fmin, 7-day drying. Recovery: Fe <- Fe exp(-kr dt), kr = -ln(0.02)/DryTime.
- HS: Standard Horton with MaxInfil 0.80 in. Hmax: Modified Horton with MaxInfil 0.80 in (5.2.4 defect D1). Hmaxf: same with the fix.
- L0 / L1: LID with the clay as the 24 in storage layer, void ratio from total (0.43) or drainable (0.109) porosity; seepage 0.01 in/hr.
- L2: LID with no storage layer, seepage = clay Ksat 0.01 in/hr (the clay throttles topsoil drainage).
- P1: swmm524-perched, SOIL2 = the clay; topsoil-to-clay flow capped by the clay's Green-Ampt capacity with the perched head added.
- P1vg: P1 + `VG` lines. Head from van Genuchten curves (theta_s = porosity), drive = (h1 - h2)/dz + 1 with dz = 14 in; downward flow = K1 min(drive, 1), capped by Green-Ampt; upward flow = -K2 min(-drive, GMAX = 10); SOIL2 drains at K2(theta2) with no field-capacity cutoff. Curves: topsoil (0.1018, 0.04633 1/in, 1.3764), clay (0.2053, 0.02377 1/in, 1.5383).
- `VG OPTION TOPFC | FCDRAIN | SOIL2ET | FCHEAD | STEP` each restores one perched rule (ablation).

Synthetic seasons: storms every 6 days from Nov 1 (dormant) and May 1 (growing), 61-day spin-up, 90-day scoring window, intensity 1/6 in/hr; "big storms" are those of 0.75 in and larger. Capture = 1 - runoff / rain over the scored storms, runoff from each storm's start to the next storm's start, integrated from the .out at a 1-minute report step.

## Results (this build, 12 Nov 2026)

Big-storm capture, % (dormant / growing), from results_B.json:

| Setup | Dormant | Growing |
|---|---|---|
| H0 Modified Horton | 76.6 | 77.9 |
| Hz Modified Horton, impermeable clay | 70.8 | 72.7 |
| Hmax Modified Horton + MaxInfil (defect) | 6.7 | 11.0 |
| HS Standard Horton + MaxInfil 0.8 in | 70.8 | 72.7 |
| L0 LID, clay as storage layer | 100.0 | 100.0 |
| L2 LID, no storage layer | 79.3 | 95.0 |
| P1 perched engine | 83.0 | 97.1 |
| P1vg perched + van Genuchten | 67.1 | 96.9 |
| P1vgm perched + vG, Mualem K | 60.5 | 96.6 |
| P1s / P1svg, clay 5x tighter | 53.7 / 44.4 | 95.2 / 94.5 |

VG ablation, dormant big-storm capture (vg_ablation.json): full VG 67.1; + TOPFC 67.1; + FCDRAIN 67.0; + SOIL2ET 67.1; no upward flow 71.1; + FCHEAD 68.3; + STEP 59.4; all five perched rules 72.3.

8 in storm, 10 ac Denver HSG B Horton, SCS Type II stand-in (storm8_results.json): Standard Horton with 3 in cap infiltrates 3.00 in; Modified Horton with 3 in cap infiltrates 0.001 in in EPA 5.2.4 (defect D1) and 3.00 in with the fix; perched engine keeps 3.81 in.

Experiment H, ideas from the SWMM-USERS list (forum_ideas.json):

- DRY_ONLY YES changes big-storm capture by at most 1.3 points (HS growing 72.7 -> 71.4) and the LID/perched setups by at most 0.4. Reason: `lidproc.c getEvapRates()` already sets SoilEvap = 0 whenever SurfaceInfil > 0 (same rule in OpenSWMM 6 `LID.cpp` line 907). Horton summer evaporation falls 24 to 40 % and scaled dry-hour PET does not restore it (H0: 0.49 -> 0.29 -> 0.30 in).
- Depression storage as the topsoil bowl (Horton f0 = fmin = 0.01 in/hr): dormant big-storm capture 27.6 % at 0.2 in, 75.2 % at 0.8 in, 95.5 % at 1.4 in; it equals P1's 83.0 % at 0.99 in and P1vg's 67.1 % at 0.68 in.
- 3 in/hr test on the two-layer profile: surface rate falls below 0.1 in/hr after 20 (L2, near FC) to 82 minutes (P1, dry); mean rate in hours 4 to 6 is 0.010 in/hr (L2) and 0.035 to 0.048 in/hr (P1, P1vg).
- DRAIN line as a curb cut: see defect D2. The perched engine ignores DRAIN lines (`StorageDrain = 0.0` in its flux routine).

## Inputs and outputs

- Reads: nothing from the user's disk. The Run tab writes a SWMM 5.2.4 .inp from the form ([OPTIONS], [EVAPORATION] MONTHLY + DRY_ONLY NO, [INFILTRATION], [LID_CONTROLS] with optional SOIL2, STRUCT, VG lines, [LID_USAGE], one outfall).
- Writes: "Export completed run (.zip)" with each engine's .inp and .rpt, results.csv (with provenance lines), manifest.json (engine and input SHA-256), README.txt. "Download .inp (current inputs)".
- Download soil-recovery-study.zip: Python scripts, result JSON/CSV, example .inp per setup, verify.py + tests_manifest.json, BUILD.md, wasm-build/ (WASI patches, compat headers), patches, the OpenSWMM issue draft.

## Checks

Mechanical (verify.py, 12 Nov 2026, 1,181 of 1,181 passed, 94 s on two cores; exit 1 on a missing engine, failed run, missing file, count mismatch or moved number):

| Group | Cases | What |
|---|---|---|
| season | 46 | 23 setups x 2 seasons vs results_B.json |
| ablation | 18 | 9 VG cases x 2 seasons |
| vg_checks | 4 | closed column (EXP, Mualem), drying column, no upward flow |
| storm8 | 7 | 8 in storm cases |
| thread | 54 | Experiment H |
| parity | 930 | perched vs EPA 5.2.4 with no SOIL2/VG/STRUCT line: .out and LID report byte-identical |
| openswmm | 122 | stock, fix, OpenSWMM 5.3.0-beta.3 and 6.0.0-alpha.4 on season, 8 in, SOIL2 and drain inputs |

Other checks:

- Options build vs pre-VG build, inputs without VG lines: 1,346 of 1,346 .out byte-identical. VG inputs without OPTION lines vs first VG build: 27 of 27.
- WebAssembly vs native, VG inputs including OPTION cases: 38 of 38 .out byte-identical.
- All five .wasm files rebuilt from the pinned sources with Zig 0.17.0: byte-identical (SHA-256 above; scripts in wasm-build/).
- RECOVERY pattern of all 1.0 vs none: 66 of 66 .out pairs byte-identical. Worst runoff continuity in the study runs: 0.017 %. .out runoff matches .rpt totals within 0.033 in.
- Browser runs: test_review.py 24 of 24 (run locking, stale state, export contents, validation, accessibility).

Human review: Bob Dickinson reviews conclusions. An outside AI-assisted review (3 Nov 2026) graded the 30 Oct release 82/100; its findings are answered on the Limits tab.

## What this does not show

- No calibration to a site; one soil pair; synthetic storm trains (rain in 3.5 % of hours).
- No matched HYDRUS comparison. The binned Rv runs use stand-in rain and profiles; the questioner's West Allis rain, HYDRUS profiles and Python test are needed.
- Each layer is one moisture bucket; a wetting front inside the clay is represented only by the Green-Ampt cap. GMAX = 10 is a supplied, fitted value.
- Soil structure is static except the experimental STRUCT Ksat decay (illustrative rates).
- The study clay's porosity 0.43 implies a bulk density of 1.51 g/cc (94 lb/ft3) at a particle density of 2.65; compacted urban soils near 1.9 g/cc would be tighter.
- Known defects:
  - D1. Modified Horton with MaxInfil > 0 in EPA 5.2.4: `infil.c` line 545 uses MAX where MIN is meant (`infil->Fe = MAX(infil->Fe, infil->Fmax)`); 4.0 in of rain infiltrates 0.002 in. Fixed in OpenSWMM 5.3.0; the fix is ported in the "MaxInfil fix" engine.
  - D2. DRAIN line on a bio-retention LID with no storage layer: `lidproc.c biocellFluxRates()` computes StorageDrain, the `storageThickness == 0.0` branch never limits it, and `f[STOR] = 0.0` never removes it. Winter season, coefficient 0.1: 232.85 in of drain flow from 20.55 in of rain, runoff continuity -1,100.9 %, in EPA 5.2.4, OpenSWMM 5.3.0-beta.3 and 6.0.0-alpha.4. Proportional to the coefficient (2.3 in at 0.001). Not fixed in any engine here.
  - OpenSWMM 6.0.0-alpha.4 ignores an unknown LID layer keyword (SOIL2) instead of reporting it; issue drafted with a tested patch (openswmm-issue/).

## How to reproduce

```
export SWMM_ENGINE=/path/to/swmm524/build/bin/Release/runswmm
export SWMM_MHFIX_ENGINE=/path/to/swmm524-mhfix/build/bin/Release/runswmm
export SWMM_PERCHED_ENGINE=/path/to/swmm524-perched/build/bin/Release/runswmm
export OPENSWMM_BIN=/path/to/openswmm.engine/build-native/bin/Release
python3 verify.py                 # or --skip-openswmm
```

Builds and pinned revisions: BUILD.md in the download. Study scripts: run_season.py, run_recovery.py, storm8_test.py, vg_checks.py, vg_ablation.py, rv_bins.py, forum_ideas.py, compare_engines_a4.py.

## Credits and licenses

- The question: a soil scientist working on Chesapeake Bay soil-restoration credits ("the questioner"), with comments from a second reviewer; replies on the SWMM-USERS list at OpenSWMM.org (Experiment H). Names withheld on the public page.
- EPA SWMM 5.2.4: USEPA, public domain (17 USC 105).
- OpenSWMM Engine: Copyright 2026 HydroCouple Developers, Apache License 2.0, https://github.com/HydroCouple/openswmm.engine (swmm6_rel @ 13746831). The page ships LICENSE-OpenSWMM.txt and NOTICE-OpenSWMM.txt and reproduces the NOTICE in its About tab. OpenSWMM sources were modified for a wasm32-wasi build; changed files carry dated notices. The USEPA does not endorse this product.
- Page, scripts and swmm524-perched changes: Robert Dickinson, SWMM Enablement.

## AI use

Claude (Anthropic) did most of the work behind this page at Bob Dickinson's request: compiled the engines (native and WebAssembly, including the WASI patches for SWMM6), read the infiltration and LID source, wrote the swmm524-perched change and its van Genuchten option, ported OpenSWMM's MaxInfil fix, made the fixes from the outside review, ran the list-thread ideas as Experiment H and found the no-storage-layer drain defect, designed and ran the simulations, controls and verify script, and wrote the page, its Doc essay, the Word file and this summary. Bob set the question and reviews the conclusions.

## Changes

- 2026-11-12: Experiment H (From the list tab): DRY_ONLY, depression-storage bowl, infiltration-test duration, curb-cut drain; defect D2; verify.py thread group (54 cases) and two OpenSWMM drain runs; Doc tab and .docx one-sentence, one-paragraph and one-page summaries with questions and answers; this file.
- 2026-11-03: outside-review fixes: frozen run records and bound exports, verify.py with expected counts, BUILD.md, VG OPTION lines and ablation, accessibility, wording pass.
- 2026-11-02: van Genuchten option in swmm524-perched; binned Rv with stand-in inputs.
- 2026-10-31: both OpenSWMM engines moved to the swmm6_rel release branch (6.0.0-alpha.4).
- 2026-10-30: 8 in storm test, MaxInfil fix engine, OpenSWMM legacy 5.3.0 and 6.0.0-alpha.3 (native and WebAssembly), Engines tab.
- 2026-10-29: first release: recovery test, seasons, soil structure tab, perched engine, Run it yourself (EPA 5.2.4 and swmm524-perched in WebAssembly).
