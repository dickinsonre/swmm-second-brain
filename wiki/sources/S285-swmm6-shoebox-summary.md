---
title: "S285: SWMM6 Shoebox, summary written from the page (v1.1)"
type: source
raw: raw/apps/swmm6-shoebox-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, swmm6, openswmm, detention, infiltration, green-ampt, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM6 Shoebox, version 1.1: a one-site stormwater desk (a catchment, a pond with a two-stage outlet, a pipe) where 18 console controls write a .inp that OpenSWMM 6 alpha.4 and EPA SWMM 5.2.4 solve in the tab, with design storms, a rain year, a 144-design survey and a water-balance rail. Raw file: [raw/apps/swmm6-shoebox-v1.1.md](../../raw/apps/swmm6-shoebox-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/1p8Bgs9HXPV9N2n7dTyxrb, version 1792853011-1fd3 (index.html, 2,777,294 bytes, SHA-256 ebd05d02fc131907c2f2b1703cc7d3160dba51992b9212ba07683d856547d7e1), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says it was built with Claude (Opus 5.5) on 23 October 2026, version 1.1 on 24 October, under Bob's direction; he supplied the two engine builds from BatchSWMMRunner. Claude found ED-1 and ED-2 and did not modify either engine.

**Claims worth keeping** (all copied from the file)
- With Curve Number infiltration the two engines agree on 32 of 32 quantities within tolerance plus 1% (worst 0.18%); their year-long outflow series differ by at most 0.0003 cfs.
- ED-1: with Green-Ampt on a 4 in storm over loam, alpha.4 gave a pre-development peak of 0.99 cfs against 19.54 cfs in 5.2.4 (pervious runoff 0.00 against 1.70 in), both with continuity under 0.1%; traced to two lines of alpha.4 source and fixed on swmm6_rel.
- ED-2: alpha.4's Node Flooding Summary lists both outfalls as flooded (47.48 hours and 1.300 million gallons at the site outfall) while its routing ledger says flooding loss 0.000; 5.2.4 prints "No nodes were flooded."
- Version 1.1 adds 66 NCEI Hourly Precipitation Data gauges (63 inside an Atlas 14 volume) with three years of record each.
- A year at 15-minute reporting (35,136 output steps) solves in 3.5 s; the 144-design survey through the 100-year storm in 3.0 s.

**Limits it states.** One catchment, one prismatic pond, one pipe; example storm depths until a station is picked; generic standards; three years of station record at most; kinematic wave is the default; peaks read at one-minute steps; no person had reviewed the code, essay or defect diagnosis.

**Checked at ingest.** The defect statuses are the page's: ED-1 fixed upstream on swmm6_rel, ED-2 as reported. The `links:` line gives Netlify as https://swmm6-shoebox.netlify.app.

**Feeds:** [SWMM6 Shoebox (app)](../entities/swmm6-shoebox.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Infiltration methods](../concepts/infiltration-methods.md), [Green-Ampt Newton test order](../concepts/green-ampt-newton-test-order.md), [BatchSWMM56 (app)](../entities/batchswmm56.md), [The SWMM findings register](../concepts/findings-register.md).
