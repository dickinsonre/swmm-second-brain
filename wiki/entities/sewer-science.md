---
title: "Sewer Science (app)"
type: entity
updated: 2026-11-18
sources: [S339]
tags: [apps, vacuum-sewers, gravity-sewers, icm]
reviewed: no
---
Bob's app Sewer Science: vacuum against gravity sewers, and how to represent a vacuum system in InfoWorks ICM. Version 1.0, 2026-10-22 [S339](../sources/S339-sewer-science-summary.md). Its `links:` line names no live Netlify address [S339](../sources/S339-sewer-science-summary.md).

**A caution about its source.** The page ships no technical summary. [S339](../sources/S339-sewer-science-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S339](../sources/S339-sewer-science-summary.md)
- Compares vacuum and gravity sewer collection and shows how to represent a vacuum system in InfoWorks ICM, a solver built for gravity flow, through an orifice analog and real-time control logic. A single-file port of Bob's Lovable monograph, with US units, a partial-flow depth solution for the gravity pipe, a head budget for the vacuum main, and checks against published US design rules.
- The original drew the gravity pipe's water depth from the flow ratio: its typical SI preset read 74% full where Manning puts the water at 64% of the diameter, and an overloaded pipe was clamped at 95% with no surcharge warning. It also converted bar to head by multiplying by ten, so every printed head ran 2% low (0.60 bar showed as 6.0 m instead of 6.12 m). The port solves the depth and flags surcharge above 1.076 Qfull.
- 30 node tests on the physics core, all passing: the half-depth checkpoints (Q/Qfull = 0.5, V/Vfull = 1.0), maximum flow 1.076 at y/D 0.938, maximum velocity 1.140 at y/D 0.813, the depth inversion round-tripped to 1e-9 from 0.5% to 107.5% of full, SI Manning (k = 1) against US Manning (k = 1.486) to 0.01% on four pipes, and the original's own capacity function reproduced.
- Headless Chromium screenshots of every tab in both themes and at 375 px; a contrast gate on both palettes; a theme-invariance check.
- Design rules read from the Florida DEP vacuum sewer checklist, 30 TAC §217.98 (Texas), and a PDH course that excerpts WEF Manual of Practice FD-12 and the AIRVAC design manual.

**How to use it, as the summary puts it.** Use it to understand when vacuum collection pays and how to fake it in ICM. Nothing here solves two-phase flow, the vacuum main's friction is a 5-ft allowance, terrain is flat, and no ICM model was built or run. [S339](../sources/S339-sewer-science-summary.md)

**What it does not show.** As the page lists it: two-phase flow (slug speed, film flow and pooling come from the design literature); friction in the vacuum main (a 5-ft allowance); terrain (lift heights assume flat ground); vacuum main capacity (the gpm-by-size table is a Florida rule of thumb tied to no design flow); ICM behaviour (no ICM model built or run); the four field implementations in the original carry no citations and are labelled illustrative; gravity hydraulics at constant n. Nobody has checked the vacuum rules against the AIRVAC manual itself. [S339](../sources/S339-sewer-science-summary.md)

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [Vacuum Sewer Toolkit (app)](vacuum-sewer-toolkit.md), [InfoWorks ICM](infoworks-icm.md).
