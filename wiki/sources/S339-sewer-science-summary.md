---
title: "S339: Sewer Science, summary written from the page (v1.0)"
type: source
raw: raw/apps/sewer-science-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-22
ingested: 2026-11-18
tags: [apps, vacuum-sewers, gravity-sewers, icm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Sewer Science, version 1.0: vacuum against gravity sewers, and how to represent a vacuum system in InfoWorks ICM. Raw file: [raw/apps/sewer-science-v1.0.md](../../raw/apps/sewer-science-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/1o8sbvMc5kujy2hqEdy4Sg, version 1792638568-fd21 (index.html, 1,437,295 bytes, SHA-256 14980dc4b182d0c15a2739f520231d2770174bdd5d1da29253de35c92ddd930e), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says it was built with Claude (Anthropic) under Robert Dickinson's direction, ported from SWMMEnablement/sewer-science (Lovable); the About tab lists what changed from the Lovable source with the original lines, and the Doc names the checks above as mechanical. This summary was written by Claude on 18 November 2026 from the published page."

**Claims worth keeping** (all copied from the file)
- Compares vacuum and gravity sewer collection and shows how to represent a vacuum system in InfoWorks ICM, a solver built for gravity flow, through an orifice analog and real-time control logic. A single-file port of Bob's Lovable monograph, with US units, a partial-flow depth solution for the gravity pipe, a head budget for the vacuum main, and checks against published US design rules.
- The original drew the gravity pipe's water depth from the flow ratio: its typical SI preset read 74% full where Manning puts the water at 64% of the diameter, and an overloaded pipe was clamped at 95% with no surcharge warning. It also converted bar to head by multiplying by ten, so every printed head ran 2% low (0.60 bar showed as 6.0 m instead of 6.12 m). The port solves the depth and flags surcharge above 1.076 Qfull.
- 30 node tests on the physics core, all passing: the half-depth checkpoints (Q/Qfull = 0.5, V/Vfull = 1.0), maximum flow 1.076 at y/D 0.938, maximum velocity 1.140 at y/D 0.813, the depth inversion round-tripped to 1e-9 from 0.5% to 107.5% of full, SI Manning (k = 1) against US Manning (k = 1.486) to 0.01% on four pipes, and the original's own capacity function reproduced.
- Headless Chromium screenshots of every tab in both themes and at 375 px; a contrast gate on both palettes; a theme-invariance check.
- Design rules read from the Florida DEP vacuum sewer checklist, 30 TAC §217.98 (Texas), and a PDH course that excerpts WEF Manual of Practice FD-12 and the AIRVAC design manual.

**Limits it states.** As the page lists it: two-phase flow (slug speed, film flow and pooling come from the design literature); friction in the vacuum main (a 5-ft allowance); terrain (lift heights assume flat ground); vacuum main capacity (the gpm-by-size table is a Florida rule of thumb tied to no design flow); ICM behaviour (no ICM model built or run); the four field implementations in the original carry no citations and are labelled illustrative; gravity hydraulics at constant n. Nobody has checked the vacuum rules against the AIRVAC manual itself.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Sewer Science (app)](../entities/sewer-science.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [Vacuum Sewer Toolkit (app)](../entities/vacuum-sewer-toolkit.md), [InfoWorks ICM](../entities/infoworks-icm.md).
