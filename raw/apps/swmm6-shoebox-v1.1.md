---
name: SWMM6 Shoebox
file: swmm6-shoebox.html
version: "1.1"
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://swmm6-shoebox.netlify.app", artifact: "https://claude.ai/artifact/1p8Bgs9HXPV9N2n7dTyxrb", repo: none named in the page}
engines:
  - {name: OpenSWMM, version: 6.0.0-alpha.4, license: Apache-2.0, note: "WebAssembly build from dickinsonre/BatchSWMMRunner, Emscripten 3.1.51; pinned by SHA-256"}
  - {name: EPA SWMM, version: 5.2.4, license: public domain, note: "WebAssembly build from the same repository; pinned by SHA-256"}
units: US customary (cfs, in, ft, ac, MG)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Opus 5.5) on 23 October 2026, version 1.1 on 24 October, under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/1p8Bgs9HXPV9N2n7dTyxrb, version 1792853011-1fd3 (index.html, 2,777,294 bytes, SHA-256 ebd05d02fc131907c2f2b1703cc7d3160dba51992b9212ba07683d856547d7e1), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM6 Shoebox: a one-site stormwater desk solved by OpenSWMM 6 and EPA SWMM 5.2.4 in the browser

## In three points
- **What:** A one-site desk (a catchment, a detention pond with a two-stage outlet, a pipe to an outfall) where 18 console controls write a real .inp and OpenSWMM 6.0.0-alpha.4 and EPA SWMM 5.2.4, compiled to WebAssembly, solve it in the tab: design storms, a year of rain, a 144-design survey, and a water-balance rail. Its shape comes from Samuel Letellier-Duchesne's Shoebox, which runs EnergyPlus in a browser.
- **So what:** With Curve Number infiltration the two engines agree on 32 of 32 quantities within tolerance plus 1% (worst 0.18%), and their year-long outflow series differ by at most 0.0003 cfs. Checking them against each other found two alpha.4 defects: with Green-Ampt on a 4 in storm over loam alpha.4 gave a pre-development peak of 0.99 cfs against 19.54 cfs (ED-1, traced to two lines of source and fixed on today's swmm6_rel), and its Node Flooding Summary lists both outfalls as flooded where its ledger says 0.000 (ED-2).
- **Now what:** Use it to see what a small site design does across storms, a year and a survey, and to see why Curve Number is the default. One catchment, one prismatic pond and one pipe; agreement between two engines is evidence, not proof.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own (version 1.1, 24 October 2026). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Desk, Year, Survey, Engines, About, Doc. The console's 18 channels follow the water: rain, land, soil, pond, outlet, pipe; seven are rail terms of the water balance that sum at the foot. Two subcatchments share the rain: S_POST drains to the pond, S_PRE is the same land before building and drains to its own outfall, so one run gives both worlds. Version 1.1 adds a rain-station panel: NOAA Atlas 14 depths and three years of hourly record at 66 NCEI Hourly Precipitation Data gauges (63 inside an Atlas 14 volume), with PFDS and HPD file loaders.

## Results the page reports

- Timing in the browser: a full year at 15-minute reporting (35,136 output steps) takes 3.5 s; the survey of 144 designs through the 100-year storm takes 3.0 s.
- ED-1: on the 4 in storm over loam, pervious runoff 0.00 in (alpha.4) against 1.70 in (5.2.4), both with continuity errors under 0.1%; reproduced over twelve values of Ks.
- ED-2: alpha.4 lists 47.48 hours and 1.300 million gallons of flooding at the site's outfall, every drop that left through it; 5.2.4 prints "No nodes were flooded."

## Checks (as stated on the page)

- Browser equals Node: 16 compared numbers matched exactly.
- Both engines are pinned by SHA-256 and refused on mismatch.
- Under a policy that blocks worker threads, storms, year and survey re-ran on the page thread with the same numbers.
- The rail: across 4 designs, every storm and both engines (28 pairs), the site run without its pre-development twin gave the same outflow peak (worst 0.0000 cfs), and recomputed continuity errors matched SWMM's printed ones in 28 of 28.
- Station rain: every station-year's wet-hour count, total and wettest hour checked against NCEI's files; no rainfall value was altered.

## What this does not show

As the page lists it: one catchment, one prismatic pond and one pipe; example storm depths until a station is picked; generic standards, not any jurisdiction's code; a synthetic year has a year's shape, not a city's statistics, and station records cover three years at most; hourly records smooth the bursts that set small-site peaks; kinematic wave is the default and the timings are for it; peaks read at one-minute steps; no person had reviewed the code, the essay or the defect diagnosis at publication.

## How to reproduce

Engines tab: the ED-1 Ks sweep reruns on demand and each engine prints its version line.

## Credits and licenses

OpenSWMM 6.0.0-alpha.4 (HydroCouple/openswmm.engine, Apache-2.0; musl and Emscripten notices apply); EPA SWMM 5.2.4 (public domain); NOAA Atlas 14 and NCEI Hourly Precipitation Data; NRCS TR-55; Samuel Letellier-Duchesne's Shoebox for the idea.

## AI use

The page says: built with Claude, Anthropic's AI model (Claude Opus 5.5), in a single session on 23 October 2026 at the request and under the direction of Robert (Bob) Dickinson, who chose the project, set the scope and supplied the two engine builds. Claude wrote all of the page's code, text and figures, chose the opening design by grid search, and found and traced ED-1 and ED-2. For 1.1 it chose the 66 gauges and read the NCEI and NOAA files through the built-in browser in Bob's desktop app. It did not build or modify either engine. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.1 (2026-10-24): rain stations, Atlas 14 alternating block, PFDS and HPD loaders, the water-balance rail, ED-2 (the version read).
- 1.0 (2026-10-23): first version.
