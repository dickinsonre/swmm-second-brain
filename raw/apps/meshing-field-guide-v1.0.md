---
name: Meshing Field Guide
file: meshing-field-guide.html
version: "1.0"
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/2jyHLYsJGo844WmgyjAwuL", repo: none named in the page}
engines: none (a teaching mesher on cdt2d; ICM's mesher is not run)
units: US customary (ft, ft2)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/2jyHLYsJGo844WmgyjAwuL, version 1793635336-f222 (index.html, 1,643,742 bytes, SHA-256 0e5d001eb7c048b0f7737ca94de5a84c9f4ffc632e0bafe22f44a33c7e76269b), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# Meshing Field Guide: InfoWorks ICM 2D meshing tips, a 2014 note brought forward to 2026

## In three points
- **What:** A 2026 edition of Innovyze's January 2014 note Tips for a Good Meshing Experience for InfoWorks ICM: each tip summarized (not reproduced) with what has changed by November 2026, plus a browser mesher that shows the reason behind each tip.
- **So what:** ICM is now at 2027.2, ArcMap was retired on March 1, 2026, and ICM meshes with a newer default algorithm; the teaching mesher's area bookkeeping matches a hand-worked 87,012.9 ft2 exactly.
- **Now what:** Clean the data before you mesh, and check each 2026 update against your ICM release. The playground is a teaching mesher, not ICM's, and no ICM mesh was generated to compare.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0 · 2026-11-02"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

The 2014 note's message: the mesh can only be as clean as the data, so clean the data first. By November 2026 Innovyze belongs to Autodesk, ICM is at release 2027.2, Esri retired ArcMap on March 1, 2026, and ICM meshes with a newer default algorithm. Tabs: Guide (the tips, each with its 2026 change), Playground (constrained Delaunay via cdt2d, area splitting, merge across unconstrained edges), Workbench, Sensitivity, Automate (script generators), About, Doc.

## Checks (as stated on the page)

- Area bookkeeping: for every Playground state, element areas sum to the triangle areas and equal the zone area less building footprints. For the repaired block: 104,000 ft2 zone, a 407.4 ft2 facade bulge and a 20.4 ft2 lens give 87,012.9 ft2 by hand; the mesher's total is 87,012.9 ft2.
- Refusal: the bow-tie footprint produces exactly one edge crossing, at (330, 195); repairing the vertex order removes it.
- Swale: for element widths of 8 ft and more the deepest swale any alignment keeps equals 5.09 ft2 divided by the width; sampled over 80 alignments the code returns that bound at every width tested (0.637 ft at 8 ft, 0.509 ft at 10 ft).
- Unit conversions of the USGS quality levels and ICM default areas were done in code from published metric values; charts are drawn from the same core file the page embeds.
- Headless Chrome in both themes, no console errors, contrast measured.

## What this does not show

- The Playground does not reproduce ICM's Triangle settings, Clip or Classic meshing, terrain-sensitive meshing, Subgrid Sampling or any hydraulics; its timestep ratio is a width ratio, not a measured run time.
- No ICM mesh was generated for the test block, so the Playground has not been compared with ICM's mesher.
- The 2026 updates come from public Autodesk, Esri and USGS pages; check them against the release you use.

## How to reproduce

Open the page; the Playground, Workbench and Sensitivity tabs compute in the browser.

## Credits and licenses

Innovyze, Tips for a Good Meshing Experience (January 2014), summarized, not reproduced. cdt2d for the constrained Delaunay mesher. Autodesk, Esri and USGS public pages. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, in November 2026, under the direction of Robert (Bob) Dickinson, who supplied the 2014 note and the ICM Exchange reference and asked for the 2026 update, the app, the Doc tab and the .docx. Claude researched the changes and wrote the mesher on cdt2d, the merge and Courant arithmetic, the swale study, the GIF encoder, the calculators, the script generators, the interface and its tests. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-11-02): first version.
