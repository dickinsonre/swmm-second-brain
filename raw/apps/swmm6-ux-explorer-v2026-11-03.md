---
name: SWMM6 UX Explorer
file: swmm6-ux-explorer.html
version: "2026-11-03"
date: 2026-11-03
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://swmm6-ux-explorer.netlify.app", artifact: "https://claude.ai/artifact/L9wrbfR7L97GDMYwWXZNvB", repo: none named in the page}
engines:
  - {name: teaching demo engine, note: "a small engine in the page that steps every 10 minutes; the page labels it 'Teaching demo engine, not SWMM'"}
  - {name: EPA SWMM, version: 5.2.4, note: "run on the exported .inp files for the storm comparison; not in the page"}
units: US customary (cfs, ft, ac, in)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was made with Claude in sessions on 31 October and 2 and 3 November 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/L9wrbfR7L97GDMYwWXZNvB, version 1793763272-a53c (index.html, 1,046,093 bytes, SHA-256 d69ce79d29109a519690c7dc96d81a00fe4899ac21615f583526fbfbe532b755), every tab read in headless Chromium on 2026-11-18. The page gives no version number; the version above is the date of its last revision as the Doc states it. Nothing was run to write this file."
---

# SWMM6 UX Explorer: the SWMMVis alpha.4 workspace in one HTML file, with public data and the storm you finally apply

## In three points
- **What:** A single-file browser copy of the SWMMVis desktop workspace for OpenSWMM 6 alpha.4, wrapped around a small live model (59 junctions, one outfall, 59 conduits, 58 subcatchments on 222 ac, one rain gage), with the alpha.4 Data tools rebuilt: NOAA Atlas 14 depths, USGS daily flows, a 3DEP elevation sample, and three candidate design storms. From 2 November it also reads your own SWMM5 file and writes it back.
- **So what:** It shows a design number keeping its pedigree: Atlas 14 gives 4.82 in for the 10-year, 24-hour storm at 38.9 N, 77.0 W (the 122 mm in the alpha.4 release graphic). Three storms of the same 4.82 in give very different peaks: SCS Type II 315.7 cfs, the alternating block 296.9, a triangle 47.1 in the demo engine; EPA SWMM 5.2.4 on the exported files gives 373.4, 357.9 and 49.6, in the same order.
- **Now what:** Use it to see the alpha.4 workflow without installing anything, and use the .inp export with a real engine for numbers that matter. It is not SWMMVis, and its engine is not SWMM.

This summary was written after the fact. The page ships no technical summary of its own and gives no version number. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

A ribbon (Home, Model, Features, Analysis, Animation, Data), an Object Browser, layers, a Properties panel, an Attribute Table, Summary, USGS, 3D, Atlas 14 and Message Log panels, with About and Doc. It extends Bob's August app; the 80,702-byte August original was rebuilt and matches the copy on his computer by MD5. Rounds of work: a revision after an outside review (31 October), a SWMM5 reader (2 November), the SWMMVis look and a revision after a second outside review (3 November). A replayed .out is drawn as SWMM wrote it.

## Results the page reports

- Storm candidates: all three total 4.8200 in. SCS Type II puts about 31% of the day's rain into the fifteen minutes before noon. The alternating block matches Atlas 14 at 9 of 10 durations up to 24 hours and runs 1.7% high at 3 hours.
- All three storms deliver the same 2,080,214 ft3 of runoff in the demo engine; only the timing differs. Its ranking of storms matched SWMM's on this network.
- Subcatchment outlines: all 58 match their modeled areas (largest relative error 9 x 10^-13); all 1,653 pairs intersect with zero overlap area. Of the old outlines the page says only that they "held 74.1 percent".

## Checks (as stated on the page)

- Seven data snapshots (three Atlas 14 tables, three daily-flow records, the elevation grid) hashed in the fetching browser and again inside the file: all seven match; the grid matches row by row, 40 by 40.
- The USGS Water Data API path, asked for water year 2026 at three gages: all 888 daily values, their dates, the 18 ice days and the two peaks match the older WaterServices snapshot.
- Five bugs from the outside review fixed and tested both ways: run against the file the reviewer graded, 14 of 17 bug checks fail.

## What this does not show

As the page lists it: no SWMMVis code runs here; the look follows the SWMMVis manual's screenshots (a Mac, light theme) and nobody has set it beside SWMMVis on Windows; the demo engine is not SWMM, and on a network with large storage its storm ranking might differ; the storm experiment speaks for this network at this location; the outlines are true in area and invented in shape on a synthetic network placed at a real location; the elevation layer is a 40 x 40 sample of 3DEP, about 295 ft per cell.

## How to reproduce

Data tab: fetch Atlas 14 and compare storms; Model: export the .inp and run it in EPA SWMM 5.2.4.

## Credits and licenses

SWMMVis and OpenSWMM 6 (HydroCouple); NOAA Atlas 14 (Precipitation Frequency Data Server); USGS Water Data API and WaterServices; USGS 3DEP; NRCS TR-55. No license is stated for the page.

## AI use

The page says: made with Claude, Anthropic's AI model, in sessions on 31 October and 2 and 3 November 2026 under the direction of Robert (Bob) Dickinson, who asked for it, whose August app it extends, and who supplied the two outside reviews. Claude rebuilt the August file, fetched the USGS, 3DEP and NOAA data through the built-in browser on his computer, wrote all of the new code, reproduced and fixed the five reported bugs, and wrote the SWMM5 reader and writer. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2026-11-03: SWMMVis look; revised after a second outside review (the version read).
- 2026-11-02: reads SWMM5 input files.
- 2026-10-31: revised after an outside review.
