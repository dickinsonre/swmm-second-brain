---
title: "S330: NA Rain Grid, summary written from the page (v2.0.0)"
type: source
raw: raw/apps/na-rain-grid-v2.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, rainfall, noaa-atlas-14, design-storms]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app NA Rain Grid, version 2.0.0: NOAA Atlas 14 rainfall frequency into IDF curves, design storms and SWMM 5 input. Raw file: [raw/apps/na-rain-grid-v2.0.0.md](../../raw/apps/na-rain-grid-v2.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/UJJTb2Cr6vtwRMZaZHNyDo, version 1792896390-9a1a (index.html, 638,641 bytes, SHA-256 e4bbd3ec6f4083253efa48016da545b999f2ddcb3c67991f7d82eee585547c4a), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude Code session on 24 and 25 October 2026 under the direction of Robert (Bob) Dickinson, who supplied the Lovable source and asked for an HTML app; responsibility is his."

**Claims worth keeping** (all copied from the file)
- Turns NOAA Atlas 14 precipitation-frequency estimates into what a stormwater modeler needs: IDF curves, design storms (NRCS Types I, IA, II, III, alternating block, Huff and others) and SWMM 5 input. One HTML file with no server or keys, rebuilt from Bob's Lovable app so that every rainfall number on screen comes from a 598-station Atlas 14 snapshot.
- The Lovable version asked NOAA for data and then threw the answer away (see its Audit tab); features that only showed invented numbers (annual totals, 30-year trends, drought, ENSO, forecasts, climate scenarios) are not carried over. In the rebuild every storm method returns exactly the Atlas 14 depth (to 10^-9 in), and an exported Tampa 24-hour, 100-year Type II storm reads 11.300 in of total precipitation in EPA SWMM 5.2.4's report.
- Snapshot integrity: 624 station queries; 598 returned Atlas 14 values and 26 fell outside coverage; every 25-station block matched an FNV-1a hash computed on NOAA's page before it was written (whole-file hash 7694c941). One station, Vatia in American Samoa, sat offshore; it was moved onto land and re-queried.
- NRCS tables: Types I, II and III at 0.1 hour and IA at 0.5 hour, each matched to a hash of the published file and monotone from 0 to 1.
- Storm totals: a Node test suite checks the sum of increments against the Atlas 14 depth to 10^-9 in; the alternating block holds the IDF depth in every window (worst shortfall zero).
- SWMM round trip in EPA SWMM 5.2.4: Tampa 24-hour, 100-year, Type II at 6-minute steps, 11.300 in; the 3-day alternating block 15.100 in; the SI version 287.020 mm.

**Limits it states.** As the page lists it: frequency, not climate (NOAA's February 2026 progress report expected Atlas 15 as a preliminary release on water.noaa.gov, which this app does not read); point depths, so an areal reduction factor is the user's job; no Atlas 14 volume for Washington and Oregon, and Canada is outside NOAA's remit; six hundred points, not a map. Not yet checked by a person: the Huff table, read from a text extraction of Circular 173; the 299 coordinate corrections; the Keifer-Chu fits.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [NA Rain Grid (app)](../entities/na-rain-grid.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Design storms and temporal patterns](../concepts/design-storm-patterns.md).
