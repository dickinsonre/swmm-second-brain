---
title: EPANET
type: entity
updated: 2026-11-18
sources: [S21, S11, S198, S115, S120, S277, S315, S316, S318, S317]
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

**Added 18 November 2026.** The [EPANET Total Head Explorer (app)](../entities/epanet-total-head-explorer.md) carries a JavaScript port of the EPANET 2.2 hydraulic solver that agrees with compiled EPANET 2.2 and OWA-EPANET 2.3.5 to 4.4 x 10^-12 ft on the manual's tutorial network; its first edition used 2.31 ft per psi where EPANET uses 0.4333 psi per ft and put node 2 at 386.66 psi instead of 387.02 [S277](../sources/S277-epanet-total-head-explorer-summary.md).

**Added 18 November 2026.** From the 18 November uploads: EPANET for SWMM5 Experts 2.0 compares EPANET 2.2 and 2.3.5 with EPA SWMM 5.2.4 on one pipe at six flows; 2.3.5's heads equal 2.2's at 6 of 6, and a 2.3.5 [LEAKAGE] line gives 28.485 gpm against 28.484 gpm from the formula [S315](../sources/S315-epanet-for-swmm5-experts-app-md.md). EPANET Web runs OWA EPANET 2.3.5 in a Web Worker, bit-identical on 2,751 of 2,781 Net1 hydraulic values [S316](../sources/S316-epanet-web-summary.md). WNTR Toolkit traces EPANET 2.2's tank errors on Net3 to a 0.0005-ft dead band in its head comparison, which EPANET 2.3 replaces [S318](../sources/S318-wntr-toolkit-summary.md). SWMM vs EPANET runs one pressurized network in both engines [S317](../sources/S317-swmm-vs-epanet-summary.md).

**Related.** [Force main friction](../concepts/force-main-friction.md), where SWMM's and EPANET's friction formulas meet.
