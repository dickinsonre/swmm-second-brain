---
name: Low-Spot Census
file: low-spot-census.html
version: "1.0"
date: 2026-11-05
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/7y4S869stBBkYXUGCU3xRC", repo: none named in the page}
engines:
  - {name: none in the page, note: "the exported SWMM input files were run outside the page in EPA SWMM 5.2.4 through swmm-toolkit 0.17.0"}
units: US customary (ft, in)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/7y4S869stBBkYXUGCU3xRC, version 1793909074-527b (index.html, 237,009 bytes, SHA-256 88120d084a8abafc45217d522c099f110b87906c7bfd73de58821654d165360e), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file; the date is the artifact's publish date."
---

# Low-Spot Census: every sink on a road surface, checked against an inlet and a mesh

## In three points
- **What:** Finds every place a surface (grid, LandXML TIN or GeoTIFF) can hold water, checks each low spot against the inlets in a SWMM model or CSV, and shows what a 2D mesh does to it.
- **So what:** On the sample road the last 55 ft of gutter before the low point climbs 2.1 inches, which no contour plot shows; 20 of 20 exact-answer checks pass, and planted defects were found 4 of 4 on the design surface with no false finds.
- **Now what:** Run your design surface and inlets through it before a storm finds the puddle. Every surface tested is synthetic, and it finds where water can stand, not how much an inlet captures.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); the date is the artifact's. The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

The problem came from a road designer's post about checking falls and dips by eye in Civil 3D. A 12 ft lane at 2 percent crossfall drops 0.24 ft, about 3 inches, and sag curves are flatter. On the sample road the last 55 ft of gutter before the low point climbs 2.1 inches. The app finds every sink, asks whether an inlet serves it and whether the model's mesh can still see it, and gives each a verdict:
- Orphan: no inlet in this low spot.
- Stranded: the inlet is there, but its rim sits above the low point.
- Cut off: an inlet serves this sag, but a high spot separates this dip from it.
- Noise: gone after a 3 by 3 median, so the surface cannot resolve it.
- Drained: the inlet sits at the low point.
Tabs: Census, Inlets, Mesh, Dstore, Verify, About, Doc.

## Inputs and outputs

- Surface: ESRI ASCII grid, LandXML TIN, GeoTIFF (its reader loads from a CDN when needed). Grids are capped at 6 million cells and coarsened above that, with a notice.
- Inlets: SWMM 5.2 .inp with [INLET_USAGE], any .inp with [JUNCTIONS] and [COORDINATES], or a CSV with id, x, y, rim and optional placement columns.
- Mesh: SMS .2dm or ASCII grid.
- Method source named: Barnes, Lehman and Mulla (2014), Priority-Flood, Computers & Geosciences 62.

## Checks (as stated on the page)

- 20 of 20 exact-answer checks pass and run live on the Verify tab: a tilted plane holds no water; a paraboloid bowl matches its exact volume to 0.003 percent; volume by cells equals the integral of area over depth; filling a filled surface changes nothing; raising the datum or turning the surface 90 degrees changes nothing; an inlet at the low point drains the bowl to zero, and a rim 3 in above it leaves the exact pool.
- Planted defects: 4 of 4 on the design surface with 0 false finds; 7 of 9 on the as-built scan with 1 false find; 0 of 9 on QL2 with 0. The two as-built misses: a pothole small enough for the filter to erase (reported as Noise), and shallow water that reads Cut off where the design surface says Stranded.
- A mesh as fine as the surface reproduces the census exactly.
- The exported input files run in EPA SWMM 5.2.4 with no errors (swmm-toolkit 0.17.0), with byte-identical controls for AUTOMATIC inlet placement in both directions and for a repeat run.
- The checks are mechanical. No person has reviewed the code or the essay.

## What this does not show

- No real road has been through the app; every surface is synthetic.
- The test noise is uncorrelated from cell to cell; real lidar noise is partly correlated, so the QL2 result is a worst case.
- Inlet capture, gutter spread, clogging, or anything finer than the grid.

## How to reproduce

Open the page, load the built-in synthetic sample road and its SWMM model or your own surface and inlets, and read the Census tab. Verify reruns the 20 checks.

## Credits and licenses

Priority-Flood: Barnes, Lehman and Mulla (2014). EPA's inlet.c was read for how AUTOMATIC placement resolves. No license is stated in the page.

## AI use

The page says the app was built with Claude, Anthropic's AI model, in a Claude session in November 2026, under the direction of Robert (Bob) Dickinson, who chose the problem from a road designer's post and set the requirements. Claude wrote all the code, the synthetic sample road and its SWMM model, the Doc essay and the Word document, chose the noise test and its thresholds by measurement, and read EPA's inlet.c. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.
