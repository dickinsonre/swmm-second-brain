---
title: EPANET for SWMM5 Experts (app)
type: entity
updated: 2026-11-18
sources: [S115, S315]
tags: [apps, replit, epanet, swmm5, force-mains, hydraulics]
reviewed: 11/16/2026
changed_after_review: "2026-11-18 (S300 to S375 ingest): a paragraph added near the end, headed Added 18 November 2026 (S315, S115)"
---
Bob's Replit app EPANET for SWMM5 Experts - The Rosetta Stone: a one-page reference that explains EPANET to people who know SWMM5, with comparison diagrams and hydraulic calculators run in browser JavaScript. Version 1.0, at `epanet-swmm-experts.replit.app` [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md)
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

**What it does not show.** No number was compared with EPANET, SWMM, field measurements or an independent calculation. The published page, the other tabs and the downloads were not checked. HTML parse warnings at two lines were not followed up. [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md)

**Noted at ingest.** The file names this app "The Rosetta Stone"; it is one of three of Bob's apps with Rosetta Stone in the name (Q77). The failed check and the SI doubt are in Q76.

**Added 18 November 2026.** Version 2.0.0 of 12 November 2026 [S315](../sources/S315-epanet-for-swmm5-experts-app-md.md) is a later version of the app summarized above; [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md) now carries `superseded_by: S315`. Version 2.0 built EPA SWMM 5.2.4, EPANET 2.2 and EPANET 2.3.5 from source and ran one 12-in, 1,000 ft pipe with C = 130 at six flows from 100 to 2,000 gpm: SWMM's FORCE_MAIN matched the Hazen-Williams formula within 0.001 ft, EPANET 2.2 matched to its 0.01 ft print resolution, and Manning with the equivalent n equals Hazen-Williams at 605 gpm, reading -24.0% at 100 gpm and +18.4% at 2,000 gpm [S315](../sources/S315-epanet-for-swmm5-experts-app-md.md). The same work lists 15 corrections to versions 1.0 and 1.1, among them an invented `forcemain_getEquivN()` shown as SWMM5 source (C-1), the Preissmann slot given as the default surcharge method where the default is EXTRAN (C-6), EPANET defaults given as TRIALS 40 and ACCURACY 0.01 where they are 200 and 0.001 (C-8), and the Manning constant 1.49 in SWMM5 calculations where SWMM5 uses 1.486 (C-11) [S315](../sources/S315-epanet-for-swmm5-experts-app-md.md). The page now has 35 tabs and 47 in-page tests; 19 of the original 32 tabs were not audited beyond a source scan, and no person has reviewed version 2.0 [S315](../sources/S315-epanet-for-swmm5-experts-app-md.md). The two summaries name different `file:` lines, so the manifest counts them as two apps (Q117).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [Force main friction](../concepts/force-main-friction.md), [Lewis A. (Lew) Rossman](lew-rossman.md), [EPA SWMM 5](swmm-5.md).
