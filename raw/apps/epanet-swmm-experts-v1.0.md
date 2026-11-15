---
name: EPANET for SWMM5 Experts - The Rosetta Stone
file: epanet-swmm-experts
version: 1.0
date: 2026-03-15
author: Robert Dickinson
links: {replit: https://epanet-swmm-experts.replit.app, repo: https://github.com/SWMMEnablement/EPANET-SWMM-Experts}
engines: none
stack: HTML, CSS, JavaScript, Vite; Chart.js from jsDelivr; Google Fonts; separate Express API and PostgreSQL/Drizzle scaffold
units: both
ai_use: No prior AI development attribution was found in the source; Replit Agent wrote this summary.
---

# EPANET for SWMM5 Experts: Translate SWMM5 concepts into EPANET terms

## What it does

This browser app explains how SWMM5 concepts correspond to EPANET concepts for people familiar with SWMM5. It combines reference material, comparison diagrams, and interactive hydraulic calculators in one page. It displays calculated flow and head-loss values, and can generate a reference document and a CSV export. The app identifies its version as 1.0 in the source header and footer (`artifacts/epanet-swmm/index.html:5,8612`).

## How it computes

The app runs its calculations in browser JavaScript. No EPANET or SWMM simulation engine invocation appears in the app source.

1. `updateCalc()` converts the entered diameter, length, and flow into internal US customary units, then calculates pipe area, velocity, hydraulic radius, Reynolds number, Manning head loss, and Hazen-Williams head loss. It displays head loss per 1,000 feet and converts displayed results for SI mode (`artifacts/epanet-swmm/index.html:9922-10032`).
2. `cToN_swmm()`, `cToN_alt()`, and `nToC()` convert between Hazen-Williams C and Manning n using either the SWMM5 source-code method or the reference-manual method. `sfManning()` and `sfHW()` calculate friction slope (`artifacts/epanet-swmm/index.html:10696-10740`).
3. `updateDW()` calculates a Darcy-Weisbach friction factor and an equivalent Manning n from roughness height and pipe diameter (`artifacts/epanet-swmm/index.html:11040-11088`).
4. `updateCFL()` calculates a maximum timestep and Courant number from pipe length, velocity, wave celerity, and timestep inputs (`artifacts/epanet-swmm/index.html:8706-8735`).
5. `generateDocs()` assembles the equations and code reference as an HTML document. The force-main batch tool assembles CSV output in `fm_downloadCSV()` (`artifacts/epanet-swmm/index.html:11089-11593,13369-13379`).

Representative equations below describe the implementation, not independent verification. All functions are in `artifacts/epanet-swmm/index.html`.

| Function and source lines | Implemented calculation |
|---|---|
| `updateCalc()`, 9954-9967 | A = pi * D^2 / 4; V = Q / A; R = D / 4; Re = V * D / nu. Manning Sf = (n * Q / (1.49 * A * R^(2/3)))^2. Hazen-Williams hf = 4.727 * L * Q^1.852 / (C^1.852 * D^4.87). D and L are feet; Q is cubic feet per second. |
| `cToN_swmm()`, 10696-10702 | n = (phi / cf) * (D / 4)^(2/3 - 0.63) / C. US coefficients are phi = 1.486 and cf = 1.318. The function switches coefficients in SI mode. |
| `cToN_alt()`, 10705-10707 | n = 1.067 * (D / S0)^0.04 / C, with D in feet. |
| `updateDW()`, 11066-11073 | f = 0.25 / log10(epsilon / (3.7 * D))^2; n = sqrt(f / 185) * D^(1/6). |
| `updateCFL()`, 8706-8723 | dtMax = L / (V + c); Courant = (V + c) * dt / L. |
| `lkCalcEmitter()`, 11603-11610 | Q = Ce * P^gamma when P is positive; otherwise Q = 0. The chart uses GPM and psi. |
| `lkCalcGW()`, 11648-11667 | net = A1 * dgw^B1 - A2 * dsw^B2 + A3 * dgw * dsw, using fixed demonstration coefficients. |
| `TX.evalTreatment()` and `TX.simulate()`, 11768-11853 | Validate and evaluate an entered expression across residence times. For percent removal R, C_out = C_in * (1 - R / 100). This is an expression sweep, not SWMM routing. |
| `updateValveSim()`, 12383-12434 | Uses valve-specific pressure rules. Throttle head loss is K * V^2 / (2 * g). |
| `updateFireFlow()`, 12445-12465 | Q_available = Q_test * ((P_static - P_min) / (P_static - P_residual))^0.54, using GPM and psi. |
| `updatePumpEnergy()`, 12538-12575 | Q_adjusted = Q * speed; H_adjusted = H * speed^2; water hp = Q_adjusted * H_adjusted * 8.34 / 33000. Pump and motor efficiencies give input power and energy cost. |
| `dmUpdatePDA()`, 12599-12609 | Demand percentage follows sqrt(P / P_normal), bounded by zero and full demand. |
| `skelUpdate()`, 12722-12731 | Estimates remaining pipes with a fixed diameter-based percentage rule. It does not simplify an imported network. |
| `agingUpdate()`, 12753-12800 | Applies an exponential age fraction to stored roughness endpoints and plots the trend. |
| `trUpdate()`, 12801-12831 | Calculates illustrative transient quantities; it does not call a transient simulation engine. |
| `fm_updateCalculation()`, 13143-13235 | Converts source roughness to n, with optional flow and temperature inputs. `fm_getKinematicViscosity()` and `fm_getFrictionFactor()` supply local viscosity and friction-factor approximations at lines 13132-13141. |

## Inputs and outputs

- Inputs are values entered through page controls, including calculator values and formula selections. The unit selector offers US and SI modes (`artifacts/epanet-swmm/index.html:1256-1259,9918-9946`).
- The page stores shareable interface state in the URL hash, including theme, units, selected tab, and calculator values. No database or browser storage writes were found in the app source (`artifacts/epanet-swmm/index.html:12857-12944`).
- The generated files are an HTML equations reference and a CSV named `swmm5_conversion.csv` (`artifacts/epanet-swmm/index.html:11585-11593,13369-13379`).
- No application API endpoint or user-file import was found in the web app source. Chart.js loads from jsDelivr, and fonts load from Google Fonts (`artifacts/epanet-swmm/index.html:45,61`).
- The separate Express service exposes `GET /api/healthz`. The web page does not call it (`artifacts/api-server/src/app.ts:11`; `artifacts/api-server/src/routes/health.ts:6-8`).
- The treatment editor produces a copyable `[TREATMENT]` text block (`artifacts/epanet-swmm/index.html:12150-12157`).

## Contents

- One HTML entry page (`artifacts/epanet-swmm/index.html`).
- 32 navigation tabs and 32 matching content panels, counted from the current source (`artifacts/epanet-swmm/index.html:1280-1337`, section IDs through line 8002).
- 11 selectable themes, counted from `VALID_THEMES` (`artifacts/epanet-swmm/index.html:8624`).
- The page is organized into Start Here, Hydraulics, Components, Quality, Modeling, Data & Tools, and Reference navigation groups (`artifacts/epanet-swmm/index.html:1281-1333`).

## Checks

- `pnpm run typecheck`: passed for the workspace.
- Main preview page at `/`: loaded and rendered in the browser preview.
- Browser equation checks: 9 of 10 passed on page load. The failing assertion is `cToN_swmm(130, 2.0)`, which returned `0.00846` while the embedded check expects approximately `0.0109` (`artifacts/epanet-swmm/index.html:12951-13009`; browser console run on 2026-11-15).
- No separate test script is configured in the EPANET artifact package (`artifacts/epanet-swmm/package.json:6-10`).
- Vite workflow logs reported HTML parse warnings at `artifacts/epanet-swmm/index.html:2511,5701`. The page still rendered during the preview load.
- Human review: none recorded in the source and documentation inspected.

## What this does not show

1. Root cause of the failed equation assertion: not checked. No code was changed to resolve it.
2. Identity and impact of the browser's unidentified 404 resource: not checked.
3. Production build, published-page rendering, and published-page interactions: not checked. The browser check used the development preview.
4. Other tabs, input ranges, mobile behavior, keyboard accessibility, CSV downloads, and HTML document downloads: not checked interactively.
5. Numerical agreement with EPANET, SWMM, field measurements, or independent reference calculations: not checked.
6. Full dependency license compliance: not checked. The root package declares MIT. No separate license file was found in the root or first-level directories.
7. The app source names Robert E. Dickinson as author. It does not record detailed individual contributions or prior AI development use. No human review of this summary has been recorded.
8. The app footer says version 1.0, the artifact configuration says 1.0.0, and the artifact package says 0.0.0 (`artifacts/epanet-swmm/index.html:5,8612`; `artifacts/epanet-swmm/.replit-artifact/artifact.toml`; `artifacts/epanet-swmm/package.json:2-4`).
9. The typecheck does not validate embedded HTML calculator logic. The app package invokes TypeScript, while calculations reside in inline JavaScript (`artifacts/epanet-swmm/package.json:10`; `artifacts/epanet-swmm/index.html:8620`).
10. HTML parse warning impact: not checked beyond the initial preview rendering.
11. SI correctness: not checked. Source inspection found the dimensionless head-loss ratio multiplied by a length conversion before display as an SI ratio (`artifacts/epanet-swmm/index.html:9974-9976`). This needs independent verification.
12. Security of the treatment-expression evaluator and separate force-main unit-test suite: not checked (`artifacts/epanet-swmm/index.html:11768-11807,13311-13335`).

## How to reproduce

- Run the app: `pnpm --filter @workspace/epanet-swmm run dev`
- Run the workspace typecheck: `pnpm run typecheck`
- No separate test command is configured. The page runs its embedded equation checks on load.
- Use the configured app workflow to supply the required `PORT` and `BASE_PATH` settings. The Vite config rejects missing settings (`artifacts/epanet-swmm/vite.config.ts:4-23`).
- To reproduce the equation-check result, open `/` in the preview and inspect the browser console. A typecheck alone does not run those assertions.

## Credits and licenses

- Robert Dickinson is named as the app author (`artifacts/epanet-swmm/index.html:6,35`).
- The footer dedicates the app to Dr. Lewis A. Rossman (`artifacts/epanet-swmm/index.html:8614-8615`).
- The workspace root package declares MIT (`package.json:1-4`). No separate license file was found in the root or first-level directories.
- The app loads Chart.js from jsDelivr and the Outfit and JetBrains Mono fonts from Google Fonts (`artifacts/epanet-swmm/index.html:45,61`). Their license terms are not stated in the project files.
- Vite is the app's build and development tool (`artifacts/epanet-swmm/package.json:6-10`). Its installed package declares MIT (`artifacts/epanet-swmm/node_modules/vite/package.json:5`).

## AI use

No prior AI development tool or role is identified in the app source or package metadata checked for this summary. Robert Dickinson is named as the author. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

The following are the 10 newest entries from `git log --date=short`:

- 2026-04-13: Updated documentation to reflect new features and project scale.
- 2026-03-31: Added the Autodesk theme and EPANET modeling guide tab.
- 2026-03-31: Defined CSS variables for EPANET and accent yellow across themes.
- 2026-03-31: Published the app.
- 2026-03-30: Added a Tom Walski history anecdote.
- 2026-03-25: Defined missing CSS variables and fixed display logic.
- 2026-03-25: Published the app.
- 2026-03-25: Added a guide to SWMM5 and EPANET modeling differences.
- 2026-03-24: Published the app.
- 2026-03-24: Added explanations of water-flow models and seasonal variations.
