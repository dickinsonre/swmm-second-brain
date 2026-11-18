---
title: "St. Venant Water Flow for Grandkids (app)"
type: entity
updated: 2026-11-18
sources: [S362]
tags: [apps, teaching, children, saint-venant]
reviewed: no
---
Bob's app St. Venant Water Flow for Grandkids: how water moves, for children under ten, with a grown-up mode. Version 2.1, 2026-10-22 [S362](../sources/S362-st-venant-water-flow-summary.md). Its `links:` line names no live Netlify address [S362](../sources/S362-st-venant-water-flow-summary.md).

**A caution about its source.** The page ships no technical summary. [S362](../sources/S362-st-venant-water-flow-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S362](../sources/S362-st-venant-water-flow-summary.md)
- A teaching app that explains how water moves (the Saint-Venant equations, Manning's roughness, the water cycle, SWMM5, and how Singapore and Dubai keep their streets dry) to children under ten, with a grown-up mode that shows the real equations. Simulators, a water race, a gallery of real channels, a question-answering "Dr. St. Venant", an 18-question quiz and a glossary. Built by Bob in Lovable, here as one HTML file.
- The original said SWMM5 uses the Preissmann four-point implicit scheme; the edition corrects it (SWMM5 iterates between conduit flows and node heads each step; the Preissmann box belongs to InfoWorks ICM and HEC-RAS 1D, and SWMM5's Preissmann slot is a surcharge option). Version 2.1 adds the SWMM family (SWMM4 1988, SWMM5 2004 to 2005, SWMM6 2026 alpha) with a "how many lifeguards does a pipe get?" explorer built on SWMM6's own finite-volume cell rule. The physics formulas themselves were not changed.
- Facts looked up and corrected against primary sources, each change listed with the source text as it was.
- SWMM4 described from the 1988 EPA User's Manual (Huber and Dickinson, EPA/600/3-88/001a) and the 4.4/4.5 block documentation; SWMM6 from openswmm.engine, branch swmm6_rel, commit 306f847 (22 October 2026, engine 6.0.0-alpha.4), with the cell rule and the authors' measurement quoted verbatim.

**How to use it, as the summary puts it.** Use it with a child at a window during a downpour. It is a teaching toy: the simulators are simple, and SWMM4 and SWMM6 are described from their manuals and source code, not run. [S362](../sources/S362-st-venant-water-flow-summary.md)

**What it does not show.** The page is for children, with simplified simulators; the physics formulas from the Lovable source were not changed, and no engine runs. Singapore's rain (about 94 in a year) and the other figures in the stories are illustrative of the lesson. [S362](../sources/S362-st-venant-water-flow-summary.md)

See [Apps summarized on 18 November 2026: calculators, toys and apps that are not about water](../concepts/apps-from-pages-calculators-toys-and-not-water.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md).
