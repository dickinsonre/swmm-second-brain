---
title: "WNTR Toolkit (app)"
type: entity
updated: 2026-11-18
sources: [S318]
tags: [apps, epanet, wntr, resilience, tanks]
reviewed: no
---
Bob's app WNTR Toolkit: resilience ensembles for EPANET networks, from real WNTR runs on Net3. Version 1.0.0, 2026-10-25 [S318](../sources/S318-wntr-toolkit-summary.md). Its `links:` line names no live Netlify address [S318](../sources/S318-wntr-toolkit-summary.md).

**A caution about its source.** The page ships no technical summary. [S318](../sources/S318-wntr-toolkit-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S318](../sources/S318-wntr-toolkit-summary.md)
- A single-file rebuild of Bob's Lovable WNTR Toolkit. The landing page is kept and corrected; the Explorer, which drew synthetic curves on an invented "Net3-like" network, now shows WNTR 1.5.0 results for the real Net3 model (92 junctions, 117 pipes, 2 pumps, 3 tanks, 2 reservoirs), with criticality, ensemble and timing studies and a fixed toolkit (runner, notebook and guide) to run on your own model.
- When WNTR's own simulator and EPANET 2.2 disagree over two days, the tanks' books settle it: WNTR's worst tank is off by 4.2% of its working volume, while EPANET 2.2's tanks are off by 119%, 122% and 53%, because an empty tank keeps flowing out (from hour 18 tank 1 sits at its minimum level and EPANET still draws from it). The page traces this to a 0.0005-ft dead band in EPANET 2.2's head comparison, which EPANET 2.3 replaces. The shipped runner, notebook and guide failed; each failure on the Defects tab is a recorded error message.
- The shipped runner executed for each scenario family, the shipped notebook cell by cell and the shipped guide block by block on WNTR 1.5.0 with Net3; the fixed versions executed end to end the same way: all 140 ensemble runs, 4 baselines, 234 sweep runs and 200 timing runs completed with no failures.
- Baseline agreement between the two simulators: largest pressure difference 0.0006 psi (0.0004 m) over all junctions and hours.
- Tank continuity and empty-tank discharge computed for every run; WNTR's empty-tank discharge was zero in all of them.
- The EPANET mechanism confirmed from the result tables (head drops of 1.3e-05 to 1.4e-04 ft across the tank links against an HTOL of 5e-4 ft), read alongside src/hydstatus.c at tag v2.2 and on the development branch.

**How to use it, as the summary puts it.** Use it to study resilience on Net3 and to run the fixed toolkit on your own network. Every number is one 92-junction network; the earthquake model is WNTR's tutorial recipe; EPANET 2.3 was not run. [S318](../sources/S318-wntr-toolkit-summary.md)

**What it does not show.** As the page lists it: one network (nothing run on a 10,000-pipe system, where WNTRSimulator is far slower); the page runs no hydraulics; hourly reporting, so controls and tank events inside an hour are not drawn and continuity errors of a few percent remain in healthy runs; pipe closures are idealized status changes; the earthquake model is WNTR's tutorial recipe with one fragility curve, uncorrelated damage, no tank damage and no repairs, and Net3's coordinates were multiplied by 1,000 to make meters; population is demand / 200 gal/person/day, not a census; EPANET 2.3 was not run (its empty-tank fix is taken from its source and release notes); water quality appears only in the fixed notebook. [S318](../sources/S318-wntr-toolkit-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [EPANET](epanet.md).
