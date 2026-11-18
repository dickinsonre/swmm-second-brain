---
name: NA Rain Grid
file: na-rain-grid.html
version: 2.0.0
date: 2026-10-25
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/UJJTb2Cr6vtwRMZaZHNyDo", original: "Lovable app na-rain-grid (React, Supabase, Mapbox)", repo: none named in the page}
engines: none (design-storm builders written for the page; exported SWMM 5 input was run in EPA SWMM 5.2.4 while building)
units: US customary (in, hours) by default, SI behind a toggle
data: "NOAA Atlas 14 snapshot of 598 stations taken 25 October 2026 from the Precipitation Frequency Data Server"
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session on 24 and 25 October 2026 under Robert Dickinson's direction, with two sub-agents reviewing the larger components. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/UJJTb2Cr6vtwRMZaZHNyDo, version 1792896390-9a1a (index.html, 638,641 bytes, SHA-256 e4bbd3ec6f4083253efa48016da545b999f2ddcb3c67991f7d82eee585547c4a), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# NA Rain Grid: NOAA Atlas 14 rainfall frequency into IDF curves, design storms and SWMM 5 input

## In three points
- **What:** Turns NOAA Atlas 14 precipitation-frequency estimates into what a stormwater modeler needs: IDF curves, design storms (NRCS Types I, IA, II, III, alternating block, Huff and others) and SWMM 5 input. One HTML file with no server or keys, rebuilt from Bob's Lovable app so that every rainfall number on screen comes from a 598-station Atlas 14 snapshot.
- **So what:** The Lovable version asked NOAA for data and then threw the answer away (see its Audit tab); features that only showed invented numbers (annual totals, 30-year trends, drought, ENSO, forecasts, climate scenarios) are not carried over. In the rebuild every storm method returns exactly the Atlas 14 depth (to 10^-9 in), and an exported Tampa 24-hour, 100-year Type II storm reads 11.300 in of total precipitation in EPA SWMM 5.2.4's report.
- **Now what:** Use it to make design storms for a SWMM model at an Atlas 14 station. Atlas 14 is frequency, not climate (it does not read Atlas 15); depths are points, not areas; Washington, Oregon and Canada have no values unless you paste a table.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v2.0.0 · HTML edition"); the date is the end of the build session the page names. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Atlas (station map), IDF, Design Storm, Compare, Data, Temperature (carried over because it used real data), Audit, About, Doc. Storms export as SWMM 5 [TIMESERIES] and [RAINGAGES] input. Between stations a hosted copy can fetch live from NOAA's server; inside the Claude viewer only the snapshot is available.

## Checks (as stated on the page)

- Snapshot integrity: 624 station queries; 598 returned Atlas 14 values and 26 fell outside coverage; every 25-station block matched an FNV-1a hash computed on NOAA's page before it was written (whole-file hash 7694c941). One station, Vatia in American Samoa, sat offshore; it was moved onto land and re-queried.
- NRCS tables: Types I, II and III at 0.1 hour and IA at 0.5 hour, each matched to a hash of the published file and monotone from 0 to 1.
- Storm totals: a Node test suite checks the sum of increments against the Atlas 14 depth to 10^-9 in; the alternating block holds the IDF depth in every window (worst shortfall zero).
- SWMM round trip in EPA SWMM 5.2.4: Tampa 24-hour, 100-year, Type II at 6-minute steps, 11.300 in; the 3-day alternating block 15.100 in; the SI version 287.020 mm.
- Station coordinates corrected against the GeoNames gazetteer (299 corrections).

## What this does not show

As the page lists it: frequency, not climate (NOAA's February 2026 progress report expected Atlas 15 as a preliminary release on water.noaa.gov, which this app does not read); point depths, so an areal reduction factor is the user's job; no Atlas 14 volume for Washington and Oregon, and Canada is outside NOAA's remit; six hundred points, not a map. Not yet checked by a person: the Huff table, read from a text extraction of Circular 173; the 299 coordinate corrections; the Keifer-Chu fits.

## Credits and licenses

NOAA National Weather Service, Hydrometeorological Design Studies Center, NOAA Atlas 14 Volumes 1 to 12 via PFDS (snapshot 25 October 2026); USDA Soil Conservation Service (1986), TR-55; NRCS 24-hour tables from HydroCAD's published file; Huff, ISWS Circular 173; Keifer and Chu; GeoNames gazetteer via github.com/lutangar/cities.json. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session on 24 and 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for an HTML app; responsibility is his. Claude audited the Lovable source (with two sub-agents reviewing the larger components), wrote every line of the file, collected the Atlas 14 snapshot through the desktop app's browser pane on NOAA's own site, corrected the station coordinates, and pulled the NRCS tables. The checks are mechanical. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.0.0 (2026-10-25): HTML edition from a verified Atlas 14 snapshot (the version read).
- 1 (Lovable): na-rain-grid.
