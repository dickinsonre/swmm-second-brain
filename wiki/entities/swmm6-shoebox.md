---
title: "SWMM6 Shoebox (app)"
type: entity
updated: 2026-11-18
sources: [S285]
tags: [apps, swmm6, openswmm, detention, infiltration, green-ampt, wasm]
reviewed: no
---
Bob's app SWMM6 Shoebox: a one-site stormwater desk (a catchment, a pond with a two-stage outlet, a pipe) where 18 console controls write a .inp that OpenSWMM 6 alpha.4 and EPA SWMM 5.2.4 solve in the tab, with design storms, a rain year, a 144-design survey and a water-balance rail. Version 1.1, 2026-10-24 [S285](../sources/S285-swmm6-shoebox-summary.md). Netlify address, from its `links:` line: https://swmm6-shoebox.netlify.app [S285](../sources/S285-swmm6-shoebox-summary.md).

**A caution about its source.** The page ships no technical summary. [S285](../sources/S285-swmm6-shoebox-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S285](../sources/S285-swmm6-shoebox-summary.md)
- With Curve Number infiltration the two engines agree on 32 of 32 quantities within tolerance plus 1% (worst 0.18%); their year-long outflow series differ by at most 0.0003 cfs.
- ED-1: with Green-Ampt on a 4 in storm over loam, alpha.4 gave a pre-development peak of 0.99 cfs against 19.54 cfs in 5.2.4 (pervious runoff 0.00 against 1.70 in), both with continuity under 0.1%; traced to two lines of alpha.4 source and fixed on swmm6_rel.
- ED-2: alpha.4's Node Flooding Summary lists both outfalls as flooded (47.48 hours and 1.300 million gallons at the site outfall) while its routing ledger says flooding loss 0.000; 5.2.4 prints "No nodes were flooded."
- Version 1.1 adds 66 NCEI Hourly Precipitation Data gauges (63 inside an Atlas 14 volume) with three years of record each.
- A year at 15-minute reporting (35,136 output steps) solves in 3.5 s; the 144-design survey through the 100-year storm in 3.0 s.

**What it does not show.** One catchment, one prismatic pond, one pipe; example storm depths until a station is picked; generic standards; three years of station record at most; kinematic wave is the default; peaks read at one-minute steps; no person had reviewed the code, essay or defect diagnosis. [S285](../sources/S285-swmm6-shoebox-summary.md)

**Noted at ingest.** The defect statuses are the page's: ED-1 fixed upstream on swmm6_rel, ED-2 as reported.

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [Infiltration methods](../concepts/infiltration-methods.md), [Green-Ampt Newton test order](../concepts/green-ampt-newton-test-order.md), [BatchSWMM56 (app)](batchswmm56.md), [The SWMM findings register](../concepts/findings-register.md).
