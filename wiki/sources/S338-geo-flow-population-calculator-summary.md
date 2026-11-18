---
title: "S338: Geo Flow Population Calculator, summary written from the page (v2)"
type: source
raw: raw/apps/geo-flow-population-calculator-v2.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, dry-weather-flow, population, gis, swmm5]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Geo Flow Population Calculator, version 2: households to subcatchments to dry weather flow in SWMM5. Raw file: [raw/apps/geo-flow-population-calculator-v2.md](../../raw/apps/geo-flow-population-calculator-v2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/La5qqP7RUfXa3xvLwzCPbe, version 1792937621-cbc3 (index.html, 1,380,088 bytes, SHA-256 8a67e5f6b2f1f33bc285fa2b809de6a4ea9b2c8fbfdb766459fc7499916bf50c), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in two Claude sessions in October 2026 under the direction of Robert (Bob) Dickinson, who supplied the geo-flow-ruby source, asked for an HTML app, chose the four version 2 improvements and owns the result."

**Claims worth keeping** (all copied from the file)
- A single-file rebuild of Bob's geo-flow-ruby project: it assigns household points to SWMM5 subcatchments with a point-in-polygon ray cast (PNPOLY), totals persons per subcatchment, and writes that population into the model as dry weather flow at each subcatchment's outlet node, then runs the export in EPA SWMM 5.2.4 inside the page.
- On the real-data check, 1,782 households fall inside a subcatchment for 3,140.1 persons, an independent Shapely overlay agrees point for point, and the exported model runs in EPA SWMM 5.2.4 with no errors; mean system DWF equals Σ persons x q to 3.8 x 10^-8. Version 2 fixed what driving version 1 through every workflow found, such as an unassigned-household fix that used the median stray distance (191 ft on the sample, which rescues half of any strays) and now uses a fixed 30 ft (9 m).
- Version 1: 43 core tests on parsing, allocation, validation, merge, unit conversion and export, including runs of the exported files in native EPA SWMM 5.2.4 (zero errors; mean system DWF equals Σ persons x q to 3.8 x 10^-8; every one of 672 report periods checked).
- Version 2: 37 core tests holding version 2 to version 1 (allocation, nearest distance and validation identical household by household on the sample, on 6,000 random households in 108 polygons with holes, and on 60,000 households in 1,600 polygons).
- The real-data allocation checked against Shapely; the overlap area checked against Shapely's make_valid (both 195.5 sq ft); the registration search checked against a control it had to find.
- The original's defects (GF-2, GF-3, GF-4 among them) reproduced by running its utilities unchanged, with the code shown on the Defects tab.

**Limits it states.** As the page lists it: that the populations are right, which depends on the data; the biggest risk is position, since a geocoding error can move a household across a boundary (on the sample, 0% of assigned households lie within 15 ft of a boundary, 9% within 30 ft, 30% within 50 ft; the synthetic lots were set back).

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Geo Flow Population Calculator (app)](../entities/geo-flow-population-calculator.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [Geo Flow Ruby (app)](../entities/geo-flow-ruby.md).
