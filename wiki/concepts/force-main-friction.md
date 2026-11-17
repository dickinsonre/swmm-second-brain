---
title: Force main friction
type: concept
updated: 2026-11-17
sources: [S10, S20, S115, S120, S201]
tags: [hydraulics, swmm5, icm, force-mains]
reviewed: 11/16/2026
changed_after_review: "2026-11-17 (S192 to S202 ingest): one paragraph added at the end on InfoSewer's Hazen-Williams form (S201)"
---
SWMM 5 offers three friction equations for a pipe under pressure, and the choice can move the answer by a factor of two [S20](../sources/S20-li-edition-54-two-solvers.md).

| Equation | Flow, 12 in pipe with 5 ft of head above the crown | Note from the source |
|---|---|---|
| Manning | 2.53 cfs | Made for open channels; widely used under pressure anyway |
| Hazen-Williams | 3.21 cfs | Empirical, developed for pressurized pipe flow |
| Darcy-Weisbach | 1.58 cfs | Most rigorous; needs absolute wall roughness |

Source for the table: [S20](../sources/S20-li-edition-54-two-solvers.md). The figures come from the calculator in the [SWMM and ICM St. Venant comparison (app)](../entities/swmm-icm-st-venant-app.md); the article does not give the roughness values or the pipe length behind them, so the comparison cannot be reproduced from the article alone. The highest value is 2.03 times the lowest (our arithmetic).

**ICM.** Force mains are a dedicated link type with pressurized flow built into the solver. The user is not offered a choice of friction formula in the same way [S20](../sources/S20-li-edition-54-two-solvers.md).

**How often it is asked.** "Pumps and force mains" tags 74 of Bob's 2,879 OpenSWMM thread titles [S10](../sources/S10-openswmm-top25-problems.md).

**Added 15 November 2026: two calculators.** [EPANET for SWMM5 Experts (app)](../entities/epanet-for-swmm5-experts.md) computes Hazen-Williams head loss as `hf = 4.727 * L * Q^1.852 / (C^1.852 * D^4.87)`, with D and L in feet and Q in cubic feet per second, and converts C to Manning n by `n = (phi / cf) * (D / 4)^(2/3 - 0.63) / C` with phi = 1.486 and cf = 1.318. One of its ten built-in checks fails: `cToN_swmm(130, 2.0)` returned `0.00846` where about `0.0109` is expected, and the cause was not looked for [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md). [ForceMain SWMM5 EPANET Comparison (app)](../entities/forcemain-swmm5-epanet-comparison.md) writes paired SWMM5 and EPANET models of a force main, runs both through PySWMM 2.1.0 and WNTR 1.5.0, and flags differences of 5% and 10% [S120](../sources/S120-forcemain-swmm5-epanet-comparison-replit-summary.md). Replit Agent wrote both summaries, nobody reran either, and Bob has read neither (Q74, Q76).

**Added 17 November 2026: InfoSewer's form.** [swmm5-infosewer](../entities/swmm5-infosewer.md) writes InfoSewer's force main loss as `hL = 4.727 L Q^1.852 / (C^1.852 D^4.871)`, Q in cfs, L and D in ft [S201](../sources/S201-infosewer-2009-app-md.md). The calculator above uses D^4.87 [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md); the two sources print the exponent to different places.
