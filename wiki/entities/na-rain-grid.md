---
title: "NA Rain Grid (app)"
type: entity
updated: 2026-11-18
sources: [S330]
tags: [apps, rainfall, noaa-atlas-14, design-storms]
reviewed: no
---
Bob's app NA Rain Grid: NOAA Atlas 14 rainfall frequency into IDF curves, design storms and SWMM 5 input. Version 2.0.0, 2026-10-25 [S330](../sources/S330-na-rain-grid-summary.md). Its `links:` line names no live Netlify address [S330](../sources/S330-na-rain-grid-summary.md).

**A caution about its source.** The page ships no technical summary. [S330](../sources/S330-na-rain-grid-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S330](../sources/S330-na-rain-grid-summary.md)
- Turns NOAA Atlas 14 precipitation-frequency estimates into what a stormwater modeler needs: IDF curves, design storms (NRCS Types I, IA, II, III, alternating block, Huff and others) and SWMM 5 input. One HTML file with no server or keys, rebuilt from Bob's Lovable app so that every rainfall number on screen comes from a 598-station Atlas 14 snapshot.
- The Lovable version asked NOAA for data and then threw the answer away (see its Audit tab); features that only showed invented numbers (annual totals, 30-year trends, drought, ENSO, forecasts, climate scenarios) are not carried over. In the rebuild every storm method returns exactly the Atlas 14 depth (to 10^-9 in), and an exported Tampa 24-hour, 100-year Type II storm reads 11.300 in of total precipitation in EPA SWMM 5.2.4's report.
- Snapshot integrity: 624 station queries; 598 returned Atlas 14 values and 26 fell outside coverage; every 25-station block matched an FNV-1a hash computed on NOAA's page before it was written (whole-file hash 7694c941). One station, Vatia in American Samoa, sat offshore; it was moved onto land and re-queried.
- NRCS tables: Types I, II and III at 0.1 hour and IA at 0.5 hour, each matched to a hash of the published file and monotone from 0 to 1.
- Storm totals: a Node test suite checks the sum of increments against the Atlas 14 depth to 10^-9 in; the alternating block holds the IDF depth in every window (worst shortfall zero).
- SWMM round trip in EPA SWMM 5.2.4: Tampa 24-hour, 100-year, Type II at 6-minute steps, 11.300 in; the 3-day alternating block 15.100 in; the SI version 287.020 mm.

**How to use it, as the summary puts it.** Use it to make design storms for a SWMM model at an Atlas 14 station. Atlas 14 is frequency, not climate (it does not read Atlas 15); depths are points, not areas; Washington, Oregon and Canada have no values unless you paste a table. [S330](../sources/S330-na-rain-grid-summary.md)

**What it does not show.** As the page lists it: frequency, not climate (NOAA's February 2026 progress report expected Atlas 15 as a preliminary release on water.noaa.gov, which this app does not read); point depths, so an areal reduction factor is the user's job; no Atlas 14 volume for Washington and Oregon, and Canada is outside NOAA's remit; six hundred points, not a map. Not yet checked by a person: the Huff table, read from a text extraction of Circular 173; the 299 coordinate corrections; the Keifer-Chu fits. [S330](../sources/S330-na-rain-grid-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md).
