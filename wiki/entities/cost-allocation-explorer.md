---
title: Cost Allocation Game Theory Explorer (app)
type: entity
updated: 2026-11-14
sources: [S61, S64]
tags: [apps, cost-allocation, game-theory, lovable, verification]
reviewed: 2026-11-15
---
Bob's app version of the 1982 paper he wrote with [James P. (Jim) Heaney](james-heaney.md), built with Lovable and served at https://heaneywrr1982.lovable.app [S61](../sources/S61-cost-allocation-explorer-app-md.md) [S64](../sources/S64-li-heaney-1982-paper-cost-allocation-app.md). Version 1.0.1, 14 November 2026, MIT license [S61](../sources/S61-cost-allocation-explorer-app-md.md). The methods are on [Cost allocation by cooperative game theory](../concepts/cost-allocation-methods.md). It has no hydraulics in it: no rainfall, flow or depth file is read or written [S61](../sources/S61-cost-allocation-explorer-app-md.md).

**What it does.** A user enters stand-alone and coalition costs for 3 or 4 partners, in million dollars. The app returns five allocations (SCRB, MCRS, Shapley value, Nucleolus, Equal Split), a plot of the core, step-by-step calculations and an audit of which coalitions an allocation overcharges [S61](../sources/S61-cost-allocation-explorer-app-md.md).

**Two dated descriptions**

| | March 2026 [S64](../sources/S64-li-heaney-1982-paper-cost-allocation-app.md) | Version 1.0.1, November 2026 [S61](../sources/S61-cost-allocation-explorer-app-md.md) |
|---|---|---|
| Methods in the calculator | Four: SCRB, Shapley value, Nucleolus, Equal Split | Five: the same four and MCRS |
| Partners | 3 or 4 | 3 or 4 |
| Teaching parts | First-time walkthrough, onboarding tour, Story Mode, quizzes, glossary, five chart modes | Onboarding, quizzes, core plots, method comparisons |
| Scenarios | Three Towns, airport runway, factory pollution, an empty-core game | Scenario JSON export and import |
| Tests reported | none | 101 of 101 |

The March column comes from a passage that reads as AI-drafted and was not checked against the code [S64](../sources/S64-li-heaney-1982-paper-cost-allocation-app.md). The change list for 1.0.0 (14 November 2026) names "exact MCRS and Nucleolus" among the additions [S61](../sources/S61-cost-allocation-explorer-app-md.md).

**Checks** [S61](../sources/S61-cost-allocation-explorer-app-md.md)
- Vitest, 14 November 2026: 101 of 101 tests in 11 files, 18.14 seconds.
- 47 numeric comparisons against the 1982 paper (Three Towns, Table 1, the two-person and empty-core examples): largest absolute difference 0.00421052631579 $M, against the paper's rounded empty-core figures.
- 8 of the tests cover interface crashes and mode switching; 1 is a placeholder.
- Two review grades are on record, 76/100 (C) and A-/A (about 90/100). The summary cannot say who or what gave them (Q38).

**The AI inside it.** Optional text explains a failed audit line. It is sent the computed figures only, and an explanation that quotes a number not among them is dropped. It computes no allocation [S61](../sources/S61-cost-allocation-explorer-app-md.md).

**Limits** [S61](../sources/S61-cost-allocation-explorer-app-md.md)
- 4 partners at most.
- Its linear-program solver is sized for these games and is not a general solver.
- No person has recalculated the 47 comparisons or rerun the tests.

**Who did what.** Lovable built the interface, the methods and the tests. Bob co-authored the paper, directed the work, and reviewed the interface and the mathematics [S61](../sources/S61-cost-allocation-explorer-app-md.md).

**Open.** The summary's front matter carries the identifier of another app, the [World Rainfall Pattern Painter (app)](world-rainfall-pattern-painter.md) (Q35), and one difference in its table is larger than the largest it reports (Q36). See [Open questions](../open-questions.md).
