---
name: IFS Analysis Explorer
file: ifs-analysis-explorer.html
version: "1.0"
date: 2026-10-16
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/TTC6wCLPb1yEtwkEyZBvsv", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, role: "climate.c ported and checked hour by hour; a starter .inp plus climate file run natively", license: public domain}
data: {name: "ECMWF operational analysis 2011-2026 repackaged by Beyond Weather", location: "s3://beyond-weather-ecmwf-ifs-analysis (us-east-2), Icechunk/Zarr v3", license: "CC BY 4.0, ECMWF copyright, modified by Beyond Weather"}
units: US customary with SI where the dataset is SI
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Opus 5.5) at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/TTC6wCLPb1yEtwkEyZBvsv, version 1792196679-d92e (index.html, 109,093 bytes, SHA-256 3d8cc82ec792a07a42843ba585a6a07923967e65e44197cb63f450c9a578deac), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# IFS Analysis Explorer: ECMWF's 2011 to 2026 operational analysis on AWS, read through a SWMM5 lens

## In three points
- **What:** Computes the layout of Beyond Weather's repackaging of ECMWF's 6-hourly operational analysis (January 2011 to September 2026) as one Icechunk/Zarr repository on AWS, and bridges it to SWMM5 with a climate-file converter and a generated Python script.
- **So what:** The archive holds 23,008 analyses of 542,080 N320 grid points and 32 variables (6.69 TB as float32); the page found the AWS registry lagging the README, and showed that daily-mean extremes put a year's Hargreaves PET at 84% of what true extremes give (30.5 against 36.1 in).
- **Now what:** Use the generated Python against the real bucket to build a SWMM climate file for a site. The app never reads the data itself, and no one has run the Python against the real bucket.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-10-16"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Dataset, N320 grid, Bit rounding, Chunk cost, SWMM bridge, Python, About. Every number is computed from the published layout: 23,008 analyses at 00/06/12/18 UTC; 542,080 grid points on the N320 reduced Gaussian grid (640 rows, 18 to 1,280 points per row, about 19 mi); 32 variables (6 upper-air on 18 levels, 22 surface, 4 static); 6.69 TB uncompressed as float32; 72,638,720 values and 290.6 MB raw per analysis; README about 6.7 TB raw and 1.3 TB stored. The bucket is anonymous; the marketplace listing is Earthmover beyond-weather/ecmwf-ifs-analysis.

## Results the page reports

- Docs check: the AWS registry page says the archive ends 2024-12-31; the README runs to 2026-09-30.
- Near 3,280 ft (1,000 m) the stored surface elevation moves in 171 ft steps (up to plus or minus 86 ft, or 0.31 F on a lapse-rate shift); take site elevation from a DEM.
- SWMM 5.2.4's climate.c evening and pre-dawn temperature branches do not meet at midnight; the step comes from the code, and the port was checked hour by hour against the engine.
- From the 6-hourly data, the file's Tmax averages -3.5 F and Tmin +0.9 F off the true extremes, and the year's Hargreaves PET comes out at 84% (30.5 against 36.1 in).

## Checks (as stated on the page)

- Nearest point: 8 named sites plus 3,000 random locations against eccodes codes_grib_find_nearest, 0 index mismatches.
- Bit rounding against numcodecs BitRound, keepbits 3 to 14, 7,009 values each: 0 mismatches.
- The generated Python, run with icechunk 2.3.0 on a local mock repository (same names, dimensions and chunking; 92,600 points, January to February 2020), wrote a climate file byte-identical to the page's converter, 58 days.
- Starter .inp plus climate file run in EPA SWMM 5.2.4 built from tag v5.2.4: no errors.

## What this does not show

- Any IFS value: the app never reads the bucket.
- The Python has not been run against the real bucket, and no person has reviewed the text.

## How to reproduce

Open the page; the Python tab gives the script; the SWMM bridge tab writes the climate file and starter .inp.

## Credits and licenses

ECMWF operational analysis, CC BY 4.0, ECMWF copyright, modified by Beyond Weather. EPA SWMM 5.2.4 (public domain). Checks against eccodes, numcodecs and Pillow. No license is stated for the page.

## AI use

The page says it was built with Claude (Opus 5.5), Anthropic's AI model, in a claude.ai session in October 2026, at the request of Robert (Bob) Dickinson, who supplied the Beyond Weather announcement and asked for the app. Claude read the dataset README and the AWS registry page, wrote all of the code and text, compiled EPA SWMM 5.2.4 from source, built the Icechunk mock and ran the checks. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-10-16): first version.
