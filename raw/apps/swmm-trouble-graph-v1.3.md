---
name: SWMM Trouble Graph
file: swmm-trouble-graph.html
version: "1.3"
date: 2026-11-04
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/2N5Yrfv5VN3kdGQv7T83dr", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, role: "the app reads its .inp, .rpt and optional .out and runs no engine; the page's seeded tests used the swmm-toolkit 0.17.0 build", license: public domain}
units: the model's own (peaks are converted to one unit before ranking)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app and essay were built with Claude under Robert Dickinson's direction, with outside reviews setting the fixes in 1.1 to 1.3. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/2N5Yrfv5VN3kdGQv7T83dr, version 1793798092-4bc5 (index.html, 4,255,086 bytes, SHA-256 b77fe621c40f275156f0561adc011b8b2e54d6d56ed60db3210ebd04ea1ef7dd), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file; the date is the artifact's publish date."
---

# SWMM Trouble Graph: connect what the report tables say about one place in the network

## In three points
- **What:** Reads a SWMM5 .inp with the .rpt from a run of it, pins each flagged report record to its element, joins records that sit close together, and ranks the places where separate tables testify against the same few elements; it also lists records connected to nothing.
- **So what:** Its reader parsed 3,558 corpus .inp and .rpt pairs with no failures, but in 296 seeded-error runs the graph did not beat the right single list: for a pipe length typed too short the time-step list's first entry landed within 2 hops 40% of the time against 23% for the graph.
- **Now what:** Use a neighborhood as a place to look, alongside the report lists, not as a diagnosis. The cause can sit outside the neighborhood, and nothing has been compared with field data.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("Version 1.3"); the date is the artifact's publish date. The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

The idea came from Ken Phuc Le's November 2026 post about a knowledge graph on Autodesk Forma data, where one floor slab carried 7 issues and 84 clashes that no single list showed. A SWMM report is a stack of separate lists (Highest Continuity Errors, Time-Step Critical Elements, Highest Flow Instability Indexes, Most Frequent Nonconverging Nodes and the summary tables). The app builds the network, ties each record to its element, and ranks neighborhoods by how many separate tables flag them, with a shuffle test for chance. It reads files in the browser, does not run the engine and does not change the model. Tabs: Neighborhoods, Table Meetings, Missing Links, Compare, Report Lists, Verify, About, Doc. Sample models include 450_Nodes.inp (447 nodes, pump stations), a manifold-pumps model, a healthy model, and one with a planted error (a 208 ft pipe typed as 10 ft).

## Checks (as stated on the page)

- Reader against the corpus: 3,558 .inp and .rpt pairs from the 1729 corpus parsed with no failures; 2,883 reports held summary tables; their 661,218 node and link rows named no element missing from the .inp, and all 469 printed element counts matched.
- Reader against the binary: on 12 models, .out peaks matched names one for one across 1,912 links and 1,951 nodes; median .out to .rpt peak ratio 0.992 (the .out samples at the report step); 1 of 803 ran high by more than 1%.
- Null control: 12 models rerun with an inert comment gave identical reports (time stamps removed) and identical analysis.
- Shuffle calibration: 1,620 draws over 540 models at Numerics; any neighborhood under 0.05 in 14 draws (0.9%), first-ranked in 12; at 0.10, 26 (1.6%). On the real reports any neighborhood passed in 39 of 540 models (7.2%), the first-ranked in 37.
- Engine parity of the seeded runs' engine (swmm-toolkit 0.17.0) with the corpus reports on 64 models: 14,293 of 15,493 peak flows exact, 15,380 within 2%.
- Footprints: across 2,883 reports and 80,921 neighborhoods, 80,916 match version 1.2 exactly.

## The planted-error test (as stated on the page)

39 models, one typing error planted in a quiet conduit more than 3 hops from any flag (length divided by 50, diameter divided by 4, roughness times 10, upstream invert raised by 1.5 diameters); 296 runs counted (3 ran past the 60 s limit). A hit means the method's first pick lands within 2 hops; a random element hits 2.0%.
- Length too short (70 runs): Graph Numerics 23%, Graph Capacity 4%, Graph All 10%, time-step list 40%, instability list 7%, flooding table 9%, surcharge table 6%.
- Diameter too small (78 runs): Graph Numerics 0%, Graph Capacity 26%, Graph All 12%, time-step list 1%, flooding table 26%, surcharge table 21%.
- Roughness x10 (78 runs): best were the surcharge table 15% and flooding table 13%; Graph All 8%.
- Invert raised (70 runs): all methods 0% to 7%.
- The page's own reading: the graph did not beat the right list.

## What this does not show

- A neighborhood is a place to look, not a diagnosis; the tables say where trouble surfaced, and the cause can sit outside it.
- Nothing has been compared with field data.

## How to reproduce

Open the page, load a sample model or drop an .inp with its .rpt (and optionally .out), or a folder; files pair by folder and file stem. Verify reruns the page's checks.

## Credits and licenses

EPA SWMM 5.2.4 (public domain), its report layout and xsect.dat sizes. The 1729-SWMM5-Models-2030 corpus. The idea: Ken Phuc Le's post. No license is stated in the page.

## AI use

The page says the app and essay were built with Claude, Anthropic's AI model, in a Claude session in November 2026, under the direction of Robert (Bob) Dickinson, who chose the problem from Ken Phuc Le's post, set the standards, and owns the corpus it was tested on. Claude wrote the readers, the graph analysis, the shuffle test, the seeded-defect test, the comparison, the app, the figures and the text. For version 1.1 Bob supplied a review of version 1.0 written by an OpenAI model, and for 1.2 and 1.3 two more reviews. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.3: every name field compared as a name (inside control rules and twenty other places); peaks converted to one unit first; capped velocities kept as lower bounds; large neighborhoods keep their connecting pipes; shuffle calibrated through the live code; run condition strip and a peak table with units.
- 1.2 and 1.1: fixes from outside reviews, including drawing each table's flags from its own eligible elements.
- 1.0: first version.
