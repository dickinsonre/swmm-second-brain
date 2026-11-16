---
title: SWMM and ICM St. Venant comparison (app)
type: entity
updated: 2026-11-15
sources: [S20, S118]
tags: [apps, comparison, hydraulics]
reviewed: 11/16/2026
---
Bob's Replit app that sets SWMM 5's and ICM's solutions of the St. Venant equations side by side, at `swmm-icm-st-venant--robertdickinson.replit.app` [S20](../sources/S20-li-edition-54-two-solvers.md).

**What it contains** [S20](../sources/S20-li-edition-54-two-solvers.md)
- Twelve tabs: solver mechanics, solver options, dynamic wave options, temporal dynamics, operational controls, advanced analysis, hydrologic methods, climate and infiltration, ICM simulation specifics, surface to sewer coupling, green infrastructure, code architecture.
- 117 animations, among them a flow pulse moving through a one-element SWMM 5 conduit and a segmented ICM conduit.
- A slot-width calculator, a Manning geometry comparison and a force main friction comparison. See [Force main friction](../concepts/force-main-friction.md).
- A live five-node network comparison.
- A nine-question solver recommendation tool. The recommendation is always contextual, never that one solver is better everywhere.

**What kind of evidence it is.** The article cites no run of either engine. The side-by-side hydrographs and typical error ranges come from the app's own calculations [S20](../sources/S20-li-edition-54-two-solvers.md). Until a source shows the app runs the real engines, its numbers on [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md) are illustrations, not measurements.

**Not to be confused with** the [St. Venant Solver Rosetta Stone (app)](st-venant-solver-rosetta-stone.md), a different app that compares SWMM 4, SWMM 5 and SWMM6 solvers by engine runs and does have a summary.

**Not in the sources.** An app .md, a version number, a date built, test results. Adding the .md to `raw/apps/` would settle the question above.

**Added 15 November 2026: the app now has a summary.** Replit Agent wrote one from the app's source on 15 November 2026 [S118](../sources/S118-swmm5-vs-icm-infoworks-networks-replit-summary.md); Bob has not read it (Q74). It gives the name SWMM5 vs ICM InfoWorks Networks, package version 1.0.0 and 22 July 2026 as the latest publication in Git. It answers the question above: the app does not call or embed the EPA SWMM 5 or InfoWorks ICM engines, so its outputs are authored data and illustrations [S118](../sources/S118-swmm5-vs-icm-infoworks-networks-replit-summary.md). It counts 13 comparison topics, 16 diagram categories and 118 diagram registry entries, where the article above gives twelve tabs and 117 animations (Q78). `npm run check` passed, no test script exists, and the formulas were not validated against either engine [S118](../sources/S118-swmm5-vs-icm-infoworks-networks-replit-summary.md). The paragraph headed "Not in the sources" is overtaken to that extent.
