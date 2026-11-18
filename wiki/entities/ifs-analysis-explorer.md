---
title: "IFS Analysis Explorer (app)"
type: entity
updated: 2026-11-17
sources: [S205, S255]
tags: [apps, climate, evaporation, swmm5, data]
reviewed: no
---
Bob's app IFS Analysis Explorer: an app that computes the layout of Beyond Weather's repackaging of ECMWF's 6-hourly operational analysis (January 2011 to September 2026) as one Icechunk/Zarr repository on AWS, and bridges it to SWMM5 with a climate-file converter and a generated Python script. It never reads the data itself. Version 1.0, 2026-10-16 [S255](../sources/S255-ifs-analysis-explorer-summary.md). Netlify address: https://ifs-analysis-explorer.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S255](../sources/S255-ifs-analysis-explorer-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S255](../sources/S255-ifs-analysis-explorer-summary.md)
- The archive holds 23,008 analyses at 00, 06, 12 and 18 UTC of 542,080 points on the N320 reduced Gaussian grid (640 rows, about 19 mi spacing) and 32 variables, 6.69 TB as float32; 72,638,720 values and 290.6 MB raw per analysis.
- The AWS registry page says the archive ends 2024-12-31; the README runs to 2026-09-30.
- Near 3,280 ft the stored surface elevation moves in 171 ft steps (up to plus or minus 86 ft, 0.31 F on a lapse-rate shift); take site elevation from a DEM.
- From the 6-hourly data, a climate file's Tmax averages -3.5 F and Tmin +0.9 F off the true extremes, and a year's Hargreaves PET comes out at 84 % of the true value (30.5 against 36.1 in).
- SWMM 5.2.4's climate.c evening and pre-dawn temperature branches do not meet at midnight; the port was checked hour by hour against the engine.
- The generated Python, run with icechunk 2.3.0 on a local mock with the same names, dimensions and chunking, wrote a climate file byte-identical to the page's converter over 58 days.

**What it does not show.** It never reads an IFS value. The Python has not been run against the real bucket, and no person has reviewed the text. [S255](../sources/S255-ifs-analysis-explorer-summary.md)

**Noted at ingest.** 542,080 x 134 fields (6 x 18 + 22 + 4) = 72,638,720 values; x 4 bytes = 290.6 MB; x 23,008 = 6.69 TB. 30.5 / 36.1 = 84 %. The midnight step in climate.c is a finding at the page's word.

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [Evaporation during rain (DRY_ONLY)](../concepts/evaporation-during-rain.md), [The SWMM findings register](../concepts/findings-register.md).
