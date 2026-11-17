---
title: EPANET
type: entity
updated: 2026-11-17
sources: [S21, S11, S198, S115, S120]
tags: [epanet, engine, water-distribution]
reviewed: no
---
EPA's program for pressurized water distribution networks. [Lewis A. (Lew) Rossman](lew-rossman.md) is its author [S21](../sources/S21-li-edition-56-swmm-history.md). Bob calls him "a brilliant programmer, developer and explainer of EPANET and SWMM for decades" [S11](../sources/S11-li-my-history-with-swmm.md).

**Versions run in Bob's apps.** OpenWaterAnalytics EPANET, tag v2.3.5, through owa-epanet 2.3.5 (engine 20305); WNTR 1.5.0 with its bundled EPANET 2.2; EPyT 2.3.5.3; epanet-js 0.9.0 [S198](../sources/S198-two-engines-one-town-summary.md). The ForceMain comparison app runs EPANET through WNTR 1.5.0 and does not report the native engine version [S120](../sources/S120-forcemain-swmm5-epanet-comparison-replit-summary.md).

**Facts the apps rely on** [S198](../sources/S198-two-engines-one-town-summary.md)
- Pressure-dependent demand (PDA) came with EPANET 2.2. Below a minimum pressure a junction gets nothing, above a required pressure everything, and in between a share that rises with the square root of pressure.
- EPANET converts head to pressure at 0.4333 psi per foot (`PSIperFT` in `types.h`).
- Net1, the example network: nine junctions, a source reservoir, one pump and an elevated tank, demands in GPM, a two-hour pattern peaking at 1.6 times average.

**Six routes to one answer.** On Net1's 225 hourly pressures, epanet-js, EPyT, WNTR with EPANET 2.2, the runepanet console program and WNTR's own Python solver all agree with owa-epanet to within 9.6e-05 psi [S198](../sources/S198-two-engines-one-town-summary.md).

**Apps here that use or explain it.** [Two Engines, One Town](two-engines-one-town.md), which couples it to SWMM [S198](../sources/S198-two-engines-one-town-summary.md); [ForceMain SWMM5 EPANET Comparison](forcemain-swmm5-epanet-comparison.md) [S120](../sources/S120-forcemain-swmm5-epanet-comparison-replit-summary.md); [EPANET for SWMM5 Experts](epanet-for-swmm5-experts.md), which explains it to SWMM users and runs no engine [S115](../sources/S115-epanet-for-swmm5-experts-replit-summary.md); [EPANET Quizzer](epanet-quizzer.md).

**Related.** [Force main friction](../concepts/force-main-friction.md), where SWMM's and EPANET's friction formulas meet.
