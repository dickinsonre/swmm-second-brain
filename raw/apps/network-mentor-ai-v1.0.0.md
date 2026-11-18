---
name: Network Mentor AI
file: network-mentor-ai.html
version: 1.0.0
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/45htVKeNxZdQZW4mVZcnPk", original: "Lovable project network-mentor-ai (React, TanStack Start, Supabase; MIT)", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: "5.2.4 (swmm-toolkit 0.17.0, engine version 52004)", note: "the demo model was run once while building; the page embeds the report, the input file and the 5-minute series and replays them"}
units: US customary (ac, in, ft)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was rebuilt with Claude in October 2026 under Robert Dickinson's direction. Inside Claude it can ask Claude through the viewer's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/45htVKeNxZdQZW4mVZcnPk, version 1792949261-116d (index.html, 381,998 bytes, SHA-256 3e76840cb7fe7f31b59cd52ccfcc52dbe3bcbcb2372b2e7d2bd9e7a66bb5d000), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# Network Mentor AI: an onboarding studio for drainage modeling software

## In three points
- **What:** An onboarding studio for drainage and hydraulic modeling software: guided tours and templates that walk a new user through replicas of SWMM 5, InfoWorks ICM, InfoDrainage and Civil 3D workspaces, all showing the same demo network. Rebuilt as one HTML file from Bob's Lovable project.
- **So what:** The Lovable build's demo numbers were invented ("Completed in 1.4s · 0 errors · 2 warnings · Continuity 99.6%", and a plotted peak that changed on every page load). The rebuild's demo network is a real SWMM 5 model (35.4 ac in three subcatchments, four conduits of 30 to 60 in, a 5.00 in SCS Type II 24-hour storm) run in EPA SWMM 5.2.4, and its QA tab compares every engine number with the report each time it opens. The findings register lists D1 to D18, such as three SWMM 5 tour steps pointing at tree rows that never open.
- **Now what:** Use it to make tours for new modelers on one shared example. The template prose about ICM, InfoDrainage and Civil 3D behaviour has not been checked by a person, and the HydroCouple workflow is illustrative.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0.0 · 2026-10-25"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Studio, Templates, Library, QA, About, Doc. The demo model: rain gage RG1, subcatchments S1 to S3 (35.4 ac), junctions J1 to J4, outfall Out1 and conduits C1 to C4 (30, 54, 60 and 60 in), laid out from the Lovable map at 5 ft per map unit; the storm built from the TR-55 cumulative table. Clicking a node, conduit, subcatchment or tree row selects it and shows its input data and peak results. The demo .inp, the Status Report (.rpt) and the series (.csv) download. The tour overlay opens collapsed parents before measuring a target, and a step whose target is missing says so.

## Checks (as stated on the page)

- The demo model run with swmm-toolkit 0.17.0 (engine version 52004, "Build 5.2.4"); a second build, swmm-toolkit 0.16.2, gave an identical report apart from timestamps.
- The QA tab compares the engine numbers with the SWMM report each time it opens; every template target is looked up on its rendered screen; contrast measured; the page driven in a headless browser through every template in both themes.
- The findings register was read from the source zip; the Lovable build itself was not run.

## What this does not show

As the page lists it: the corrected template prose about ICM, InfoDrainage and Civil 3D behaviour is not checked by a person; the HydroCouple workflow is illustrative; the product workspaces are replicas, not the products.

## Credits and licenses

EPA SWMM 5.2.4 via swmm-toolkit; USDA TR-55; the Lovable network-mentor-ai (MIT, Robert Dickinson). Product names belong to their owners.

## AI use

The page says: rebuilt with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who wrote the original Lovable app, chose the rebuild and is responsible for it. Claude read the Lovable source and wrote the findings register, designed the demo network's SWMM input and ran it through EPA SWMM 5.2.4, and wrote all of the page's code, the corrected tour templates, the help articles, the Doc essay and the Word document. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.0 (2026-10-25): single-file rebuild with a real SWMM demo model (the version read).
