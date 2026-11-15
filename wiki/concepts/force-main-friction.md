---
title: Force main friction
type: concept
updated: 2026-11-14
sources: [S10, S20]
tags: [hydraulics, swmm5, icm, force-mains]
reviewed: 2026-11-15
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
