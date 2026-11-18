---
title: "Network Mentor AI (app)"
type: entity
updated: 2026-11-18
sources: [S349]
tags: [apps, teaching, onboarding, swmm5]
reviewed: no
---
Bob's app Network Mentor AI: an onboarding studio for drainage modeling software. Version 1.0.0, 2026-10-25 [S349](../sources/S349-network-mentor-ai-summary.md). Its `links:` line names no live Netlify address [S349](../sources/S349-network-mentor-ai-summary.md).

**A caution about its source.** The page ships no technical summary. [S349](../sources/S349-network-mentor-ai-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S349](../sources/S349-network-mentor-ai-summary.md)
- An onboarding studio for drainage and hydraulic modeling software: guided tours and templates that walk a new user through replicas of SWMM 5, InfoWorks ICM, InfoDrainage and Civil 3D workspaces, all showing the same demo network. Rebuilt as one HTML file from Bob's Lovable project.
- The Lovable build's demo numbers were invented ("Completed in 1.4s · 0 errors · 2 warnings · Continuity 99.6%", and a plotted peak that changed on every page load). The rebuild's demo network is a real SWMM 5 model (35.4 ac in three subcatchments, four conduits of 30 to 60 in, a 5.00 in SCS Type II 24-hour storm) run in EPA SWMM 5.2.4, and its QA tab compares every engine number with the report each time it opens. The findings register lists D1 to D18, such as three SWMM 5 tour steps pointing at tree rows that never open.
- The demo model run with swmm-toolkit 0.17.0 (engine version 52004, "Build 5.2.4"); a second build, swmm-toolkit 0.16.2, gave an identical report apart from timestamps.
- The QA tab compares the engine numbers with the SWMM report each time it opens; every template target is looked up on its rendered screen; contrast measured; the page driven in a headless browser through every template in both themes.
- The findings register was read from the source zip; the Lovable build itself was not run.

**How to use it, as the summary puts it.** Use it to make tours for new modelers on one shared example. The template prose about ICM, InfoDrainage and Civil 3D behaviour has not been checked by a person, and the HydroCouple workflow is illustrative. [S349](../sources/S349-network-mentor-ai-summary.md)

**What it does not show.** As the page lists it: the corrected template prose about ICM, InfoDrainage and Civil 3D behaviour is not checked by a person; the HydroCouple workflow is illustrative; the product workspaces are replicas, not the products. [S349](../sources/S349-network-mentor-ai-summary.md)

See [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Six quality markers for app-building work](../concepts/app-quality-markers.md).
