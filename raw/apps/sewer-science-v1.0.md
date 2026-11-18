---
name: Sewer Science
file: sewer-science.html
version: "1.0"
date: 2026-10-22
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/1o8sbvMc5kujy2hqEdy4Sg", original: "Lovable/TanStack monograph in SWMMEnablement/sewer-science", repo: none named for this edition}
engines: none (closed-form gravity and vacuum sewer calculations written for the page; nobody ran ICM or SWMM for it)
units: US customary by default (in, ft, inHg, gpm), SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/1o8sbvMc5kujy2hqEdy4Sg, version 1792638568-fd21 (index.html, 1,437,295 bytes, SHA-256 14980dc4b182d0c15a2739f520231d2770174bdd5d1da29253de35c92ddd930e), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Sewer Science: vacuum against gravity sewers, and how to represent a vacuum system in InfoWorks ICM

## In three points
- **What:** Compares vacuum and gravity sewer collection and shows how to represent a vacuum system in InfoWorks ICM, a solver built for gravity flow, through an orifice analog and real-time control logic. A single-file port of Bob's Lovable monograph, with US units, a partial-flow depth solution for the gravity pipe, a head budget for the vacuum main, and checks against published US design rules.
- **So what:** The original drew the gravity pipe's water depth from the flow ratio: its typical SI preset read 74% full where Manning puts the water at 64% of the diameter, and an overloaded pipe was clamped at 95% with no surcharge warning. It also converted bar to head by multiplying by ten, so every printed head ran 2% low (0.60 bar showed as 6.0 m instead of 6.12 m). The port solves the depth and flags surcharge above 1.076 Qfull.
- **Now what:** Use it to understand when vacuum collection pays and how to fake it in ICM. Nothing here solves two-phase flow, the vacuum main's friction is a 5-ft allowance, terrain is flat, and no ICM model was built or run.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-22"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Scenario, Principles, ICM Mapping, RTC Logic, Field Notes, About, Doc. Presets (Typical, Heavy), single or compare view, gravity or vacuum. Vacuum inputs in the typical US preset: 4.0 in main, 18.0 inHg station vacuum at cut-out (20.4 ft of water), 2,000 ft to the farthest valve, lifts every 250 ft, a 14.0 in sump trigger, valve Cd 0.62 and a 6 s pulse. Head = Δp/(ρg) with ρ = 1,000 kg/m3 and g = 9.80665 m/s2; inHg converts at 1.133 ft of water per inch. The audit lists each change from the Lovable source with the original lines (src/routes/index.tsx). CSV, text, HTML and Word exports; GIF capture.

## Checks (as stated on the page)

- 30 node tests on the physics core, all passing: the half-depth checkpoints (Q/Qfull = 0.5, V/Vfull = 1.0), maximum flow 1.076 at y/D 0.938, maximum velocity 1.140 at y/D 0.813, the depth inversion round-tripped to 1e-9 from 0.5% to 107.5% of full, SI Manning (k = 1) against US Manning (k = 1.486) to 0.01% on four pipes, and the original's own capacity function reproduced.
- Headless Chromium screenshots of every tab in both themes and at 375 px; a contrast gate on both palettes; a theme-invariance check.
- Design rules read from the Florida DEP vacuum sewer checklist, 30 TAC §217.98 (Texas), and a PDH course that excerpts WEF Manual of Practice FD-12 and the AIRVAC design manual.

## What this does not show

As the page lists it: two-phase flow (slug speed, film flow and pooling come from the design literature); friction in the vacuum main (a 5-ft allowance); terrain (lift heights assume flat ground); vacuum main capacity (the gpm-by-size table is a Florida rule of thumb tied to no design flow); ICM behaviour (no ICM model built or run); the four field implementations in the original carry no citations and are labelled illustrative; gravity hydraulics at constant n. Nobody has checked the vacuum rules against the AIRVAC manual itself.

## Credits and licenses

Florida DEP vacuum sewer checklist; Texas 30 TAC §217.98; WEF MOP FD-12; the AIRVAC design manual (through excerpts); Charles Liernur's nineteenth-century negative-pressure drainage. Bore Shell 1.0.0. MIT License, © 2026 Robert Dickinson.

## AI use

The page says it was built with Claude (Anthropic) under Robert Dickinson's direction, ported from SWMMEnablement/sewer-science (Lovable); the About tab lists what changed from the Lovable source with the original lines, and the Doc names the checks above as mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-22): first single-file port (the version read).
