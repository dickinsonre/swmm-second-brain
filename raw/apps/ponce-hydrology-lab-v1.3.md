---
name: Ponce Hydrology Lab
file: ponce-hydrology-lab.html
version: 1.3
date: 2026-11-19
author: Robert Dickinson
links: {netlify: https://ponce-hydrology-lab.netlify.app, artifact: https://claude.ai/artifact/68sBRNXNG46AvRq1NscxMQ, repo: none (Lovable project aquifer-quest-zone, source zip supplied by the author)}
engines:
  - {name: Ponce Hydrology Lab libraries, version: 1.3, source: src/lib/hydrology (19 TypeScript files, written for this app), license: MIT}
  - {name: scientific content, source: "Prof. Victor M. Ponce, SDSU: Engineering Hydrology (1989; online 2014) and onlinecalc.sdsu.edu", license: educational adaptation, not affiliated}
units: US customary by default (ft, cfs, in, °F); SI by the header switch; all arithmetic in SI
ai_use: built with Claude (Anthropic) from a Lovable project; see AI use
---

# Ponce Hydrology Lab: thirty-six hydrology and hydraulics calculators in one HTML file

**In one sentence.** Thirty-six of Prof. Ponce's hydrology and hydraulics calculators in one HTML file, in US or SI units, with 216 tests, 57 fixed defects quoted line by line, and a 26-point check against his published formulations that agrees to 0.03 percent.

**In one paragraph.** The Ponce Hydrology Lab is one HTML file that runs from a disk or a link, with no server. Its 36 module pages are built on Prof. Victor M. Ponce's teaching material at San Diego State University and cover runoff, routing, channel hydraulics, structures, groundwater, evapotranspiration and sediment, each a slider-driven instrument that answers with the equation, the numbers and a chart. The screens call nineteen library files that compute in SI and display in US or SI units. Three audits found and fixed 57 calculation defects, each quoted in the register; 216 tests pin the libraries to published tables; 26 formulation checks against his calculator pages agree to 0.03 percent. It is a teaching instrument, not a design code, and nobody has yet compared it with his live calculators.

**What is unique.** Not the calculators. Prof. Ponce's portal at onlinecalc.sdsu.edu has had a web calculator for every method here since 2004, and HEC-HMS, PCSWMM or a spreadsheet give the same numbers. What this file adds, as far as we know, is three things nobody has put together: thirty-six of those methods in one file with no server, in US or SI units, with a builder that chains runoff, unit hydrograph, routing and channel steps; a register of 57 calculation defects found in the source project, each with the offending line quoted and the numbers before and after; and a 26-point comparison with the formulations printed on his own calculator pages. The software is ordinary. The audit trail is new.

## What it does

One self-contained HTML page with 36 module pages (31 calculators and simulators, 5 learning tools) built on Prof. Ponce's SDSU teaching material: curve number runoff and infiltration comparison (Green-Ampt, Philip, Horton), rational method, unit hydrographs, Muskingum-Cunge routing, baseflow recession, flood frequency (Gumbel, log-normal, log-Pearson III), Theis drawdown, aquifer balance and recharge, catchment water balance, five evapotranspiration methods, energy balance, normal and critical depth, specific energy and the hydraulic jump, GVF profiles, wave celerity and the Vedernikov number, weirs and orifices, culverts (FHWA HDS-5), ogee spillways and USBR stilling basins, inlets and gutters (HEC-22), pump curves, sediment transport (Meyer-Peter and Müller, Engelund-Hansen, Yang), tractive force and regime channels, Rosgen classification, environmental flows, and a Workflow Builder that chains the methods. Each module answers a slider move with the equation, the numbers and a chart; every chart and table exports CSV in the units shown. For students of hydrology and engineers who want to push on a method, not for design.

## How it computes

- The screens call library functions in `src/lib/hydrology/` (19 files); the libraries compute in SI and `src/lib/units.tsx` converts for display. The US | SI switch changes nothing but the display.
- Curve number: S = 1000/CN − 10 in (25400/CN − 254 mm), Ia = 0.2 S, Q = (P − Ia)²/(P − Ia + S); AMC I and III by the NEH-630 formulas (`cn-method.ts`).
- Unit hydrograph: NRCS triangular (qp = 0.208 A/tp per mm, tb = 2.67 tp) and curvilinear (gamma, m = 3.7), convolved with rainfall-excess blocks (`unit-hydrograph.ts`).
- Muskingum-Cunge: K = Δx/c, X = ½(1 − q/(S₀ c Δx)) at a reference flow of ⅔ the peak, with c = dQ/dA from the Manning rating; C₀, C₁, C₂ from K, X, Δt; Courant C and cell Reynolds D reported with the C + D ≥ 1 (≥ 2 for accuracy, Ponce & Theurer 1982) check (`muskingum.ts`).
- Open channel: Manning for rectangular, trapezoidal, triangular, circular and parabolic sections; normal depth by bisection; critical depth from Q²T/(gA³) = 1; GVF profiles integrated by RK4 from the control (`open-channel.ts`).
- Structures: Kindsvater-Shen V-notch, broad-crested C = (2/3)^1.5 √g, Villemonte submergence; FHWA HDS-5 inlet (Form 1) and outlet control for circular concrete culverts; WES ogee crest x^1.85 = 2 Hd^0.85 y with C = 2.2 (He/Hd)^0.12 m^½/s; USBR basin types from Fr₁ and V₁ (`swmm.ts`, `culvert.ts`, `hydraulic-structures.ts`).
- Groundwater: Theis W(u) by series, aquifer step with linear-reservoir discharge R·h/h₀, recharge by the catchment-wetting budget W = P − Q, R = W − AET (`groundwater.ts`).
- Evapotranspiration: FAO-56 Penman-Monteith (Eq. 6, Rn from Eq. 38–40), Priestley-Taylor with Δ/(Δ+γ), Hargreaves (Eq. 52) with Ra from latitude and day, Blaney-Criddle with p = 100 N/4380, Thornthwaite (`evapotranspiration.ts`).
- Flood frequency: Gumbel and normal factors (Chow Table 12.3.1), log-normal by moments, log-Pearson III with the full Wilson-Hilferty expansion on ln Q (`flood-frequency.ts`).
- Sediment: Meyer-Peter and Müller 8(τ* − 0.047)^1.5, Engelund-Hansen f·Φ = 0.1 τ*^2.5, Yang (1973) with Ferguson & Church (2004) fall velocity (`sediment-transport.ts`).
- Workflow Builder: `workflow.ts` runs the same functions in a chain; values travel downstream in SI, any setting can be overridden, a routed hydrograph feeds the next reach.

## Inputs and outputs

- Reads nothing from disk. All inputs are sliders, selects and number boxes; the theory editor stores edits in the browser's localStorage only.
- Writes CSV (per chart and table, in the displayed units), a captioned GIF of a session (Make a GIF), the Doc as .docx, and this .md.
- Module pages have hash addresses (`#/modules/theis-well`); inside a preview iframe the router falls back to memory routing.
- No network use after load except Google Fonts (falls back to system fonts offline).

## Checks

Mechanical, this build:

- 216 unit tests in 23 files pass (`npx vitest run -c vitest.local.config.ts`): Theis W(u) against published table values; Bulletin 17B frequency factors at five skews (Cs 2, T 100: K = 3.605); FAO-56 Examples 18 and 20 (Rn 13.28, ETo 3.88; Hargreaves ETo 5.0); FAO-24 daylight fractions at 0°, 35°N, 40°N, 60°N; HEC-22 SI coefficients derived from the US ones; GVF profiles monotone and landing on yc or yn; routing coefficients summing to 1; hand values for infiltration, jump, culvert, spillway and sediment cases.
- 26 formulation checks against the formulas printed on Prof. Ponce's calculator pages (onlinechannel01/11/12/14, onlinerouting04/05, onlinefroude, onlinevedernikov, rational.php) and his culvert sample (yc = 4.037 ft, yn = 3.284 ft): worst relative difference 0.027 % (`npx vite-node verify/ponce-crosscheck.ts`, results in `src/doc/crosscheck.json`).
- 41 routes rendered headless in US and SI, dark and light: 0 errors, 0 NaN, no horizontal overflow at 1280 or 375 px; tour, GIF recorder, .docx download and sandboxed-iframe preview exercised.
- Complexity (SWMM App Complexity Meter core 1.7.0, baseline HC-2026-11-10-h, HydroCouple = 100): index 76.1 on the source (140 files); Size 65.6, Structure 77.2, Test evidence 60.6, SWMM vocabulary 100.0; shipped .html alone 61.0 (`node tools/complexity.cjs`).

Human review: Bob Dickinson directed the work and read the register; no hydrologist outside the project has reviewed the numbers.

Defect register: 57 defects fixed across v1.0 to v1.2 (22 high, 26 medium, 9 low), each with the original line quoted and the before and after values, in the Doc tab section 5. Text audit: 32 corrections in the theory, reference and lecture text and 13 dead ponce.sdsu.edu links replaced.

## What this does not show

- Every method is lumped or one-dimensional and most are steady; this is a teaching instrument, not a design code.
- The Ponce comparison is against his published formulations and one worked sample, not against his calculators' live output for arbitrary inputs; his servers refuse automated requests. A person should still type the same inputs into onlinecalc.sdsu.edu and a module.
- The curve number method predicts zero runoff below Ia and is least accurate below 0.5 in of runoff (TR-55).
- US slider stops were chosen by hand per module; a few US ranges are wider or coarser than the SI originals. Sediment sizes stay in mm in both systems.
- Spillway C does not vary with P/Hd; the culvert has one inlet type (concrete, square-edge headwall); Yang (1973) is a sand formula though the D50 slider reaches 100 mm; the Vedernikov module uses R = depth for every shape; the hydro-ecology indices and the form-friction n_form are illustrative, not named methods.
- The theory panels' pedagogical choices, the eight land-cover wetness fractions, and the routing reference flow of ⅔ peak have not been reviewed by anyone outside the project.
- Known open items: the Thornthwaite option is the unadjusted 12-hour-day form; FAO-56 Rn assumes sea level; Ponce's cascade of linear reservoirs has no counterpart here.

## How to reproduce

```
npm install --ignore-scripts
npx vitest run -c vitest.local.config.ts          # 216 tests
npx vite-node verify/ponce-crosscheck.ts          # 26 Ponce formulation checks → src/doc/crosscheck.json
node tools/complexity.cjs                         # Meter index → src/doc/complexity.json
npx vite-node tools/app-md.ts                     # this file
npx vite-node tools/build-docx.ts                 # Doc as .docx (figures rasterised with sharp)
npx vite build -c vite.single.config.ts           # dist-single/index.html, the shipped file
```

The register's before values come from the untouched source copy (`src.orig/`) run through the same inputs; the audit scripts are in the session scratchpad (`audit2/phys1`, `audit2/phys2`).

## Credits and licenses

- Scientific content: Prof. Victor Miguel Ponce, San Diego State University (Engineering Hydrology, 1989; online edition 2014; onlinecalc.sdsu.edu). This lab is an independent educational adaptation and is not affiliated with SDSU.
- References: NRCS NEH-630 and TR-55; FHWA HEC-22 (2009) and HDS-5 (2012); USBR Design of Small Dams and Peterka EM-25; USACE EM 1110-2-1603; FAO-56 (Allen et al. 1998); Chow (1959), Chow, Maidment and Mays (1988); Bulletin 17B; Theis (1935); Cunge (1969); Ponce and Theurer (1982); Rosgen (1994); Rawls et al. (1983); Villemonte (1947); Kindsvater and Shen (USBR Water Measurement Manual); Ferguson and Church (2004); Yang (1973); Engelund and Hansen (1967).
- Software: React 18, TypeScript, Vite, Tailwind, shadcn/ui, Recharts, html2canvas, gifenc, docx-js, sharp. Original project aquifer-quest-zone built in Lovable.
- License: MIT, © 2026 Robert Dickinson.

## AI use

The original React project (aquifer-quest-zone) was built in Lovable, an AI app builder, under the direction of Robert (Bob) Dickinson, from Prof. Ponce's published material; its files carry Lovable's scaffolding. This single-file edition was made with Claude, Anthropic's AI model, in Claude Code sessions on 21 and 22 October 2026, at Bob's request; v1.0 and v1.1 on the first day, v1.2 on the second. Responsibility for the work is his.

What Claude did. It compiled the project into one self-contained HTML file and switched it to address-bar routing; made dark the default and added the Dark/Light/Auto switch; wrote the welcome card, the tour and the GIF recorder; added US customary units to the stormwater suite; audited the twelve calculation libraries (one pass itself, one by a second Claude agent), fixed the nineteen defects in the register and wrote fifteen new tests; and wrote this essay, its figures, the About page and the Word version. For v1.1 it fixed the seven items it had flagged (the GVF integrator, the Cunge parameters, the sag-inlet equations, the Priestley-Taylor form, the USBR basin rules, the parabolic section and the gamma unit hydrographs) with seven more tests; extended the unit layer to every module, with three further Claude agents converting the modules in parallel under a written brief and a shared checker; added the CSV export; and revised this essay. For v1.2 it ran three more agents under written briefs: two audited the physics that lived inside the eighteen screen components the library audits had not reached (D27–D53 in the register, with the arithmetic moved into six new library files and 49 new tests), and one audited the theory, reference and lecture text (T1–T15 and the dead links). Itself, it rebuilt the Workflow Builder on the libraries, re-implemented the formulations published on Prof. Ponce's calculator pages for the 26-point cross-check, fixed the routing-coefficient rounding that the cross-check exposed, and revised this essay and its figures. For v1.3 (19 November 2026) it changed no calculation: it reshaped this Doc to Bob's current rules (the uniqueness note, the three sizes of summary, the opening questions and their answers, the related apps, the measured complexity box), wrote the technical summary file ponce-hydrology-lab.md and embedded it in the page, and ran the SWMM App Complexity Meter's analyzer over the source.

How the results were checked. The checks are mechanical: 216 unit tests, each fix re-run against the original and corrected code, the HEC-22 coefficients derived by dimensional conversion, the Theis function and the Bulletin 17B frequency factors compared with published table values, FAO-56's worked examples reproduced, the GVF integrator checked for monotonic profiles that land on yc or yn, 26 formulation checks against Prof. Ponce's calculator pages, and every page rendered in a headless browser in both themes and both unit systems with a scan for leftover SI strings. What no person has checked yet: the module outputs against the live output of Prof. Ponce's calculators (only their published formulations and one worked sample were available to a program), the wetness fractions chosen for the eight land covers, the hand-picked US slider ranges, and the judgement calls the text audit left to the author.

## Changes

- `1.3 (2026-11-19)`: Doc reshaped to the current rules (uniqueness note, three sizes of summary with one image, four opening questions answered at the end, related Netlify apps, measured complexity box); this .md written and embedded in the page; SWMM App Complexity Meter run (index 76.1). No calculation changed.
- `1.2 (2026-10-22)`: inline physics of 18 modules audited and moved into libraries (31 defects D27–D57); Workflow Builder rewired to the libraries; theory text audited (32 corrections); 26-point Ponce formulation cross-check; 208 tests.
- `1.1 (2026-10-22)`: US customary units on every module with an SI switch; seven flagged defects fixed (D20–D26); CSV export; GVF integrator; Muskingum-Cunge K and X from the channel.
- `1.0 (2026-10-21)`: single-file build; dark default; welcome card, tour, GIF recorder; 19 defects fixed; Doc tab and .docx.
