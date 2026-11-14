---
title: Cost allocation by cooperative game theory
type: concept
updated: 2026-11-14
sources: [S61, S64]
tags: [cost-allocation, game-theory, method]
reviewed: no
---
How to split the cost of a joint water project so that no partner, and no group of partners, would do better alone. The subject of the 1982 paper by [James P. (Jim) Heaney](../entities/james-heaney.md) and Bob, and of the [Cost Allocation Game Theory Explorer (app)](../entities/cost-allocation-explorer.md) [S64](../sources/S64-li-heaney-1982-paper-cost-allocation-app.md).

**The worked example.** Three towns share a reservoir. Alone they would pay $2M, $4M and $6M, $12M in all; together, $7M. The saving is $5M, 41.66666666667 % of the separate total [S61](../sources/S61-cost-allocation-explorer-app-md.md). The question is who pays what share of the $7M [S64](../sources/S64-li-heaney-1982-paper-cost-allocation-app.md).

**Terms** [S61](../sources/S61-cost-allocation-explorer-app-md.md)
- c(S) is what a group S would pay on its own. x(i) is what partner i is charged.
- The core is the set of allocations that recover the whole cost and charge no group more than it would pay alone.
- A game is subadditive when joining two separate groups never costs more than the two apart.
- A core can be empty: then every allocation overcharges some group.

**Five methods, as the app computes them** [S61](../sources/S61-cost-allocation-explorer-app-md.md)

| Method | Credit and year in the source | Rule in words |
|---|---|---|
| SCRB, Separable Costs, Remaining Benefits | Federal Inter-Agency River Basin Committee, 1950 | Each partner pays its separable cost (the joint cost less the cost of the project without that partner), plus a share of the remainder in proportion to its stand-alone cost less its separable cost |
| MCRS, Minimum Costs, Remaining Savings | Heaney and Dickinson, 1982 | Each partner pays the lowest charge it can have inside the core, plus a share of the remainder in proportion to the width of its range inside the core |
| Shapley value | Lloyd S. Shapley, 1953 | The partner's added cost, averaged over every order in which the partners could join |
| Nucleolus | David Schmeidler, 1969 | The allocation that makes the worst-off group as well off as possible, then the next worst, in turn |
| Equal Split | Listed as an option by the same 1950 committee; no individual credited | The joint cost divided by the number of partners |

**What MCRS changed.** SCRB uses nominal bounds. MCRS uses the actual bounds of the core, found by linear programs, so its answer lies in the stable region [S64](../sources/S64-li-heaney-1982-paper-cost-allocation-app.md). When the core is empty, the app raises the cost of every intermediate group (two or more partners) by a common factor until a core exists, and takes the smallest such factor; stand-alone costs are left as they are [S61](../sources/S61-cost-allocation-explorer-app-md.md).

**Numbers the app is held to.** 47 values from the paper, largest difference 0.00421052631579 $M; 101 of 101 tests on 14 November 2026 [S61](../sources/S61-cost-allocation-explorer-app-md.md).

**The Shapley value elsewhere.** The article says the same average-over-orderings is the basis of SHAP, a method for explaining machine-learning predictions by Scott Lundberg and Su-In Lee. AI-written passage, not checked [S64](../sources/S64-li-heaney-1982-paper-cost-allocation-app.md).

**Limits of what is here.** The app handles 3 or 4 partners [S61](../sources/S61-cost-allocation-explorer-app-md.md). The equations are in the app summary, with file and line for each; they are not copied here.

**Not in the sources yet.** The 1982 paper itself, its Table 1, and any use of these methods on a real project.
