---
title: "S349: Network Mentor AI, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/network-mentor-ai-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, teaching, onboarding, swmm5]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Network Mentor AI, version 1.0.0: an onboarding studio for drainage modeling software. Raw file: [raw/apps/network-mentor-ai-v1.0.0.md](../../raw/apps/network-mentor-ai-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/45htVKeNxZdQZW4mVZcnPk, version 1792949261-116d (index.html, 381,998 bytes, SHA-256 3e76840cb7fe7f31b59cd52ccfcc52dbe3bcbcb2372b2e7d2bd9e7a66bb5d000), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says: rebuilt with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who wrote the original Lovable app, chose the rebuild and is responsible for it. Claude read the Lovable source and wrote the findings register, designed the demo network's SWMM input and ran it through EPA SWMM 5.2.4, and wrote all of the page's code, the corrected tour templates, the help articles, the Doc essay and the Word document."

**Claims worth keeping** (all copied from the file)
- An onboarding studio for drainage and hydraulic modeling software: guided tours and templates that walk a new user through replicas of SWMM 5, InfoWorks ICM, InfoDrainage and Civil 3D workspaces, all showing the same demo network. Rebuilt as one HTML file from Bob's Lovable project.
- The Lovable build's demo numbers were invented ("Completed in 1.4s · 0 errors · 2 warnings · Continuity 99.6%", and a plotted peak that changed on every page load). The rebuild's demo network is a real SWMM 5 model (35.4 ac in three subcatchments, four conduits of 30 to 60 in, a 5.00 in SCS Type II 24-hour storm) run in EPA SWMM 5.2.4, and its QA tab compares every engine number with the report each time it opens. The findings register lists D1 to D18, such as three SWMM 5 tour steps pointing at tree rows that never open.
- The demo model run with swmm-toolkit 0.17.0 (engine version 52004, "Build 5.2.4"); a second build, swmm-toolkit 0.16.2, gave an identical report apart from timestamps.
- The QA tab compares the engine numbers with the SWMM report each time it opens; every template target is looked up on its rendered screen; contrast measured; the page driven in a headless browser through every template in both themes.
- The findings register was read from the source zip; the Lovable build itself was not run.

**Limits it states.** As the page lists it: the corrected template prose about ICM, InfoDrainage and Civil 3D behaviour is not checked by a person; the HydroCouple workflow is illustrative; the product workspaces are replicas, not the products.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Network Mentor AI (app)](../entities/network-mentor-ai.md), [Apps summarized on 18 November 2026: papers, AI and films about the work](../concepts/apps-from-pages-papers-ai-and-films.md), [Six quality markers for app-building work](../concepts/app-quality-markers.md).
