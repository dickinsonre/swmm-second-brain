---
title: "S115: EPANET for SWMM5 Experts - The Rosetta Stone, summary written by Replit Agent (v1.0)"
type: source
raw: raw/apps/epanet-swmm-experts-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-03-15
ingested: 2026-11-15
tags: [apps, replit, epanet, swmm5, force-mains, hydraulics]
drafted_by: Replit Agent (an AI), from the project's source
reviewed: 11/16/2026
---
**What it is.** A technical summary of EPANET for SWMM5 Experts - The Rosetta Stone, version 1.0: a one-page reference that explains EPANET to people who know SWMM5, with comparison diagrams and hydraulic calculators run in browser JavaScript. It is one of Bob's Replit apps, at `epanet-swmm-experts.replit.app`. Raw file: [raw/apps/epanet-swmm-experts-v1.0.md](../../raw/apps/epanet-swmm-experts-v1.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says no prior AI development tool is identified in the source. The copy here was read out of the editor of the Replit project named EPANET SWMM Experts on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- No EPANET or SWMM engine is called. `engines: none`.
- 32 navigation tabs with 32 matching content panels, and 11 selectable themes.
- The main calculator works internally in US customary units: Manning `Sf = (n * Q / (1.49 * A * R^(2/3)))^2` and Hazen-Williams `hf = 4.727 * L * Q^1.852 / (C^1.852 * D^4.87)`, with D and L in feet and Q in cubic feet per second.
- It converts Hazen-Williams C to Manning n two ways. The one it calls the SWMM5 source-code method is `n = (phi / cf) * (D / 4)^(2/3 - 0.63) / C`, with US coefficients phi = 1.486 and cf = 1.318. The reference-manual method is `n = 1.067 * (D / S0)^0.04 / C`, with D in feet.
- The page runs 10 embedded equation checks on load; 9 passed. The failing one is `cToN_swmm(130, 2.0)`, which returned `0.00846` where the check expects about `0.0109`. The cause was not looked for and no code was changed.
- Other calculators: a Darcy-Weisbach friction factor and equivalent n, a Courant number (`dtMax = L / (V + c)`), fire flow (`Q_available = Q_test * ((P_static - P_min) / (P_static - P_residual))^0.54`, in GPM and psi), pump energy, emitters, valves and a `[TREATMENT]` expression editor.
- The footer says version 1.0, the artifact configuration 1.0.0 and the artifact package 0.0.0.
- Replit Agent, reading the code, found the dimensionless head-loss ratio multiplied by a length conversion before display in SI mode. It marks this as needing independent verification.
- `pnpm run typecheck` passed, but it does not cover the calculator logic, which is inline JavaScript.
- The footer dedicates the app to Dr. Lewis A. Rossman. Repository: https://github.com/SWMMEnablement/EPANET-SWMM-Experts.

**Limits it states.** No number was compared with EPANET, SWMM, field measurements or an independent calculation. The published page, the other tabs and the downloads were not checked. HTML parse warnings at two lines were not followed up.

**Checked at ingest.** The file names this app "The Rosetta Stone"; it is one of three of Bob's apps with Rosetta Stone in the name (Q77). The failed check and the SI doubt are in Q76.

**Feeds:** [EPANET for SWMM5 Experts (app)](../entities/epanet-for-swmm5-experts.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Force main friction](../concepts/force-main-friction.md), [Lewis A. (Lew) Rossman](../entities/lew-rossman.md), [EPA SWMM 5](../entities/swmm-5.md).
