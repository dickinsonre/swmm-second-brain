---
name: Agreement Is the Null
file: engine-ageement-is-the-null.html
version: 1.1.0
date: 2026-10-04
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://engine-ageement-is-the-null.netlify.app", artifact: "https://claude.ai/artifact/TEHw1e5WwvAuzsVfoBLQXg", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, note: "as bundled in the PyPI package swmm-toolkit (solver reports 52004), one thread, Linux; 328 runs made while building, embedded as results"}
units: US customary (percent differences of US-unit models)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/TEHw1e5WwvAuzsVfoBLQXg, version 1791082767-18b1 (index.html, 998,363 bytes, SHA-256 e6d0936791265279b15201ef4176669fd8d849a984bb0ccb761807b960d35fa3), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Agreement Is the Null: engine comparisons rethought, as robustness, solution difference and what refinement can resolve

## In three points
- **What:** A rethink of how hydraulic engines are compared, measured on 16 public test models (864 conduits, 328 runs of EPA SWMM 5.2.4). Every difference comes from changing one option in that one engine (time step, inertial damping, surcharge method, Manning's n) and is put on one scale: the uniform change in n that would move the result as far.
- **So what:** When the physics forces two engines to the same answer, their agreement describes the network; the finding is where they part. On EXTRAN example 1, switching the inertial terms off moves the median conduit by 0.177%, less than raising n by 2% (0.509%), while SLOT against EXTRAN surcharge moves it 1.06%, about what raising n by 5% does (1.25%); the step sensitivity is 0.030%.
- **Now what:** Keep two scorecards (robustness and solution difference), refine each engine against itself before comparing, and read agreement between engines that share code as regression testing, not corroboration. No ICM, HEC-RAS or SWMM6 run is in the app, and no observed data.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.1.0 · 2026-10-04"). The file name above is the Netlify site's, including its spelling. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Rethink, Census, Two gaps, Price in n, Your runs, Lineage, Limits. Rethink opens with a predict-before-you-look question and a one-model, eight-differences chart (EXTRAN example 1, nine conduits, three pressurizing; medians of the time-averaged difference as a share of each conduit's peak, log scale): same run twice byte-identical; finest two steps 0.030%; shipped against refined step 0.122%; inertial terms off against on 0.177%; SLOT against EXTRAN surcharge 1.06%; n raised 2%, 5% and 10%: 0.509%, 1.25%, 2.43%. Lineage sorts engine pairs (SWMM3/4 EXTRAN, XPSWMM, EPA SWMM5, a vendor build, OpenSWMM 6 legacy path, SWMM5+, ICM InfoWorks, HEC-RAS 1D, MIKE+) into repeatability, regression test, lineage test and independent corroboration.

## Checks

The page states its reproduction: EPA SWMM 5.2.4 from swmm-toolkit; models from OpenWaterAnalytics/swmm-nrtestsuite (EXTRAN manual examples 1 to 10 without 8b, Example3, user1 to user5), cloned 2026-10-03; REPORT_STEP set to 60 s or the routing step if larger; all nodes and links reported.

## What this does not show

As the page lists it: the option switches stand in for cross-engine differences and are not cross-engine differences; no observed flow or depth, so no number is an accuracy; only the time step was refined; step sensitivity is empirical, not an error bound, and no convergence order is claimed; medians are not additive; 16 small models, close cousins, not the larger corpus; fixed routing steps only; medians hide worst instants (one conduit moved 80%); regime classes inherit the engine's own errors; pricing in n scales all roughness by one factor; the ladder stops at one eighth of the shipped step; no profiles inside long pipes; the Lineage tab's scheme summaries are recalled from published documentation and were not run or re-verified.

## How to reproduce

Limits tab, Reproduction: the engine, the models, what was changed, and how the runs were made. Your runs accepts the user's own run pairs.

## Credits and licenses

EPA SWMM 5.2.4 (public domain) via swmm-toolkit; OpenWaterAnalytics swmm-nrtestsuite models. No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session; the page does not say which parts Claude wrote. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.1.0 (2026-10-04): the version read.
