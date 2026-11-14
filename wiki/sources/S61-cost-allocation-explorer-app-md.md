---
title: "S61: Cost Allocation Game Theory Explorer, technical summary (app .md, v1.0.1)"
type: source
raw: raw/apps/cost-allocation-explorer-v1.0.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-14
tags: [apps, cost-allocation, game-theory, verification, lovable]
reviewed: no
---
**What it is.** The technical summary that ships with the Cost Allocation Game Theory Explorer, version 1.0.1, a Lovable app at https://heaneywrr1982.lovable.app. The app compares five ways of sharing the cost of a joint water project among 3 or 4 partners. Raw file: [raw/apps/cost-allocation-explorer-v1.0.1.md](../../raw/apps/cost-allocation-explorer-v1.0.1.md).

**How it was written.** By Lovable (the AI app builder): its change list says version 1.0.1 was rewritten "from current source and a fresh 101-test run" on 14 November 2026. Its AI-use section says Lovable built the interface, implemented the five methods, added the validation, audit, scenario files, tests, dark mode and the summary; Bob co-authored the 1982 paper, directed the work and reviewed UX and mathematics. It says no person has independently recalculated the 47 reference comparisons or rerun the 101 tests.

**A fault in its front matter.** `file: rain-canvas-studio` is not this app's identifier. [S62](S62-rules-for-responsible-modeling-app-md.md) carries the same line. `tools/manifest.py` now groups the two by `name:`. See Q35 in [Open questions](../open-questions.md).

**Claims worth keeping**
- Five methods: SCRB (Separable Costs, Remaining Benefits), MCRS (Minimum Costs, Remaining Savings), Shapley value, Nucleolus, Equal Split. 3 or 4 partners only; scenario files accept `playerMode` 3 or 4.
- Default game, Three Towns: stand-alone costs $2M, $4M and $6M, joint cost $7M, saving $5M, 41.66666666667 % of the $12M separate total.
- Checks: `npx vitest run --reporter=verbose`, started 2026-11-14 20:51:25 UTC, 11 files, 101 of 101 tests passed, 18.14 seconds.
- Against the 1982 paper (Three Towns, Table 1, two-person and empty-core examples): 47 numeric comparisons, largest absolute difference 0.00421052631579 $M, which the summary puts down to comparing with the paper's rounded empty-core allocation.
- Per test file: paper-examples 18, calculations 20, steps-helpers 20, mcrs 7, deployment-check 12, core-geometry 6, validation 6, explain-audit 3, CostCalculator 2, CoreVisualization 6, example 1 (a placeholder boolean test).
- The reference: James P. Heaney and Robert E. Dickinson, "Methods for Apportioning the Cost of a Water Resource Project", Water Resources Research 18(3), 476-482, 1982, bundled in the app as a PDF.
- Method credits as the summary gives them: SCRB, Federal Inter-Agency River Basin Committee, 1950; MCRS, Heaney and Dickinson, 1982; Shapley value, Lloyd S. Shapley, 1953; Nucleolus, David Schmeidler, 1969.
- MCRS: the lowest and highest charge each partner can have inside the core are found by linear programs; each partner pays the lowest charge plus a share of what is left, in proportion to the partner's range. With an empty core the costs of coalitions of two or more are raised by a common factor (1 + theta) and the program minimizes theta.
- Shapley: every one of the n! orderings is enumerated; no sampling.
- Nucleolus: sequential linear programs that maximize the smallest excess; a coalition is fixed when its largest possible excess is within 1e-6 of the optimum.
- The linear-program solver is the app's own, by vertex enumeration (`src/lib/lp.ts`), pivot tolerance 1e-9, feasibility tolerance 1e-6, designed for at most 5 variables and about 31 constraints.
- Audit: a coalition is overcharged when it pays more than its own cost by more than 1e-6.
- Optional AI text explains failed audit constraints through the Lovable AI Gateway, model identifier `openai/gpt-6-astra`; any explanation quoting a decimal that does not match the supplied figures at 2 decimals is dropped. The AI does not compute an allocation.
- Review records in the project: 76/100 (C) and A-/A (about 90/100), tool and dates "not checked"; the summary says the project cannot say whether either was a human or an AI review.
- Changes: 1.0.0 (2026-11-14) added the summary, dark mode, AI audit explanations, scenario export and import, exact MCRS and Nucleolus, and 101 tests; 1.0.1 (same day) rewrote the summary from current source and a fresh run.
- License: MIT, copyright 2026 Robert Dickinson. No new license is claimed for the paper.

**Limits it states.** No games with more than 4 partners (0 tests with 5 or more). The solver is not a general LP solver. No screen-reader audit by a person. 0 live AI explanation requests in the test run. 0 research links newly checked against Crossref.

**Checked at ingest.** The test counts sum to 101. 2 + 4 + 6 = 12, 12 - 7 = 5, 5 / 12 = 41.67 %. The table also lists a difference of 0.00428571428571 $M in `deployment-check.test.ts` "against 2-decimal displays", larger than the 0.00421052631579 $M given as the largest of the 47 (Q36).

**Feeds:** [Cost Allocation Game Theory Explorer (app)](../entities/cost-allocation-explorer.md), [Cost allocation by cooperative game theory](../concepts/cost-allocation-methods.md), [James P. (Jim) Heaney](../entities/james-heaney.md), [Robert (Bob) Dickinson](../entities/robert-dickinson.md).
