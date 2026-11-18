---
name: Water on the Road
file: water-on-the-road.html
version: "1.1"
date: 2026-10-15
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/EMjexv1kQMRqRvPXNt5qGt", repo: none named in the page}
engines:
  - {name: "HEC-22 inlet chain", source: "line-for-line port of EPA SWMM 5.2.4 src/solver/inlet.c (L. Rossman), HEC-22 3rd ed.", note: "parity measured with SWMM 5.2.4 built from USEPA source on 2026-10-14; no engine runs in the page"}
units: US customary (ft, in, ac, cfs, ft/s)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The published page carries no AI-use note; it is a Claude artifact on Robert Dickinson's account. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/EMjexv1kQMRqRvPXNt5qGt, version 1792029478-9152 (index.html, 155,253 bytes, SHA-256 7ffdf6b3eb21c5b152326836871850d085de6f9a690b86d188d4bac68cc455fb), every tab read in headless Chromium on 2026-11-17. Nothing was run to write this file; the date is the artifact's publish date."
---

# Water on the Road: Nhat Tien Vo's six-step Civil 3D HEC-22 workflow, rebuilt in the browser

## In three points
- **What:** Rebuilds the six-step road-drainage workflow of Nhat Tien Vo's VNTool Civil 3D plugin (October 10, 2026 post) in one page: pipe network from a polyline, structures by spacing, fit to the road, catchments from the corridor surface, HEC-22 hydraulics, and water on the road.
- **So what:** Its HEC-22 code is a line-for-line port of EPA SWMM 5.2.4's inlet.c, and the exported steady .inp run through SWMM 5.2.4's own street and inlet code reproduces the page's chain on 11 inlets in 4 scenarios (approach flow within 0.17%, capture within 0.02 points).
- **Now what:** Use it to see inlet spread, capture, bypass and sag ponding on a road before modeling in SWMM. It is not his code or Civil 3D, the IDF curves are illustrative, and it is not a design tool of record.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.1"); the date is the artifact's. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Plan (the six steps), Background, Drainage Table, Long Section, How He Built It, Verify. The sample: 6 inlets (3 on each of 2 gutters), 1.64 ac drained, peak runoff 7.34 cfs, 0.27 cfs bypass carried on, maximum spread 4.8 ft against a 10.0 ft limit. Exports: SWMM5 .inp (design storm, dual drainage), a steady parity .inp, drainage table and pipe schedule CSV, and a recorded walkthrough.

## Results the page reports

- On a 1.20% grade with a 2.0% cross slope and a 2.0 in gutter depression, the example flow spreads 4.58 ft; a 2 ft x 2 ft P_BAR-50 grate catches 94.0% of it (0.969 cfs); gutter velocity 2.74 ft/s against 8.16 ft/s splash-over.
- The sag inlet S4R at station 7+84 must take 1.714 cfs and ponds 1.8 in deep at the curb, 1.4 ft wide.

## Checks and findings (as stated on the page)

- Engine parity: the exported steady .inp through SWMM 5.2.4's [STREETS] and [INLETS] dual-drainage code reproduces the page's HEC-22 chain on 11 inlets in 4 scenarios: approach flow within 0.17%, capture within 0.02 percentage points, sag depth equal.
- D-1: the HEC-22 round trip is not the identity (Eq. 4-2 forward uses T^2.67, the inverse in inlet.c uses 0.375); T = 8 ft gives Q = 1.905 cfs gives T = 8.021 ft, 0.26%.
- D-2: SWMM's "Maximum Spread" comes from the street transect at the conduit's maximum depth, not Eq. 4-2 (the HEC-22 line is commented out in writeStreetStats).
- D-3: the longitudinal slope at each inlet is the approach chord, chosen for parity.
- D-5: SWMM 5.2.4 built with gcc -O2 on Ubuntu aborts on input ("buffer overflow detected") unless built with -D_FORTIFY_SOURCE=0.

## What this does not show

- His code, or Civil 3D itself; a 3D water surface (spread is drawn in plan); HEC-22 4th-edition changes.
- Pipe hydraulics beyond full-flow Manning (no HGL, no junction losses); timing in the pipe system (rational peaks are added).
- The IDF curves are illustrative. Not a design tool of record.

## How to reproduce

Open the page, set the road and rules in Plan, and export the steady parity .inp to run in SWMM 5.2.4.

## Credits and licenses

Workflow from Nhat Tien Vo's LinkedIn post on VNTool. HEC-22 3rd edition (FHWA-NHI-10-009) as coded in EPA SWMM 5.2.4 inlet.c (public domain). No license is stated for the page.

## AI use

The published page carries no AI-use note. It is a Claude artifact on Robert Dickinson's account, built in a claude.ai session. The Netlify copy in this batch adds a one-line AI-use note at the foot of the page. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1: the version read.
