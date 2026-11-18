---
name: SWMM Guide Buddy
file: swmm-guide-buddy.html
version: "1.0"
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/JrtpowoQUHnJJ5J7YT62Cp", original: "Lovable project swmm-guide-buddy (React, Vite, shadcn/ui, Recharts, React Three Fiber)", repo: none named in the page}
engines: none (hand-method calculators; a port of EPA SWMM 5.2's culvert.c was used in Python to check them while building)
units: US customary by default, SI behind a switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the original was generated with Lovable, an AI app builder, and that this edition was built with Claude in October 2026 at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/JrtpowoQUHnJJ5J7YT62Cp, version 1792896871-5240 (index.html, 3,403,171 bytes, SHA-256 8a6f5b99a6f28c6a475fee360438a90cbafb4122828ae47ab2f33722f08ab56a), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM Guide Buddy: a companion to the EPA SWMM Applications Manual, with checked calculators

## In three points
- **What:** A companion to the EPA Storm Water Management Model Applications Manual (EPA/600/R-09/000, 2009) as adapted for InfoSWMM: nine worked-example pages and a bench of hydraulic calculators (normal and critical depth, pipe capacity, culverts by FHWA HDS-5, a 3D profile viewer, a routing advisor). A single-file edition of Bob's Lovable project.
- **So what:** The Lovable calculators reported a surcharged pipe as 99% full, drew the profile from a formula instead of solving the energy equation, and did not use the real HDS-5 equations; the edition fixes these and seventeen defects are listed with their original code. 447 mechanical comparisons against independent Python re-computations pass, for example normal and critical depth against scipy's brentq to 2.5 x 10^-10. Examples 1 and 3 now quote the manual's tables; invented numbers elsewhere are tagged amber.
- **Now what:** Use it beside the manual to work its examples and check hand calculations. No SWMM run happens in the page; the calculators are single-section, steady-flow hand methods, and the culvert tool covers HDS-5 inlet and full-flow outlet control only.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · HTML edition built 2026-10-24"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Home, Examples, Tools, About, Doc. CSV export on every tool. Reference tables corrected (permissible velocities after Fortier and Scobey) or labelled where their source could not be confirmed. Removed: a download form that collected a name and email and delivered nothing.

## Checks (as stated on the page)

A Node script dumps the app's answers; a separate Python script recomputes each by a different route:
- Normal and critical depth, 49 checks over rectangular, trapezoidal, triangular and circular sections, against scipy.optimize.brentq (circular geometry from the chord): worst relative difference 2.5 x 10^-10.
- Pipe capacity: Qfull and the 0.938·D hump by brute-force scan, 12 cases, worst 3.5 x 10^-8.
- Culvert inlet control, 170 cases: the app computes headwater from flow; a Python port of SWMM 5.2's culvert.c computes flow from that headwater; the round trip returns the starting flow to 3 x 10^-13 for every case across all ten inlet codes.
- Culvert outlet control, 170 cases, worst 2.4 x 10^-11; a sweep shows headwater rising monotonically with flow for every inlet code.
- The profile viewer against an adaptive Runge-Kutta integrator. Every page loaded headless in both themes with no console errors.

## What this does not show

As the page lists it: no SWMM run (the examples quote published results; the manual's hydrographs, its Example 3 pond design and with-pond peaks, and its Example 9 statistics are not in the app); single-section, steady-flow hand methods, with one rectangular reach and one control in the profile viewer, and no network model; HDS-5 inlet and full-flow outlet control only, with no partly full backwater, multiple barrels, overtopping or improved inlets (SWMM applies its culvert codes only under dynamic wave and switches to its transition zone at 0.95·D).

## Credits and licenses

US EPA, SWMM Applications Manual (EPA/600/R-09/000, 2009); FHWA HDS-5; EPA SWMM 5.2 culvert.c; Fortier and Scobey. MIT License © 2026 Robert Dickinson.

## AI use

The page says: the original app was generated with Lovable, an AI app builder, under Bob Dickinson's direction. This edition was built with Claude, Anthropic's AI model, in October 2026 at his request; he chose the project and supplied the source, and responsibility is his. Claude read the Lovable source and found the defects, wrote the shared calculation module and rewrote the depth, culvert and profile calculators and the routing advisor's limits, corrected the example pages against the EPA manual, and built the page, theme, units switch, tour, GIF recorder, CSV exports and the Doc. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10-24): first single-file edition (the version read).
