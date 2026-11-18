---
name: Network Lift
file: network-lift.html
version: "1.2"
date: 2026-10-19
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/XTVVY9HmhXn46RVixbSNzN", repo: none named in the page}
engines: none (a DXF reader, network builder and checks in JavaScript)
units: US customary (ft, in) or SI (m, mm), with drawing units read from $INSUNITS
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/XTVVY9HmhXn46RVixbSNzN, version 1792451188-b271 (index.html, 1,756,033 bytes, SHA-256 e88a1badff62e357d6ccae6d026531f78d47cc9f1d80ac5a910eae59bc51c06b), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file; the date is the artifact's publish date."
---

# Network Lift: CAD drainage drawing to manholes, pipes and hydraulic checks, out to Excel, ICM, SewerGEMS and SWMM5

## In three points
- **What:** Reads a drainage drawing saved as DXF, finds the manholes and pipes, matches the text labels to them, works out flow direction, fills missing inverts and slopes, checks the network, and writes Excel, CSV, SWMM5 and DXF for InfoWorks ICM, SewerGEMS or SWMM.
- **So what:** In the US sample, 7 of 19 data labels were placed by evidence the drafter drew, 11 needed the distance rule, and one was too far from everything to place; a manhole with no label gets a calculated invert (815.68 ft) and is flagged.
- **Now what:** Use it to lift a network out of a drawing instead of retyping it, then read every flagged label and assumption. It does not read Civil 3D pipe-network objects (export them to plain lines first) and checks no design flows or capacity.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.2"); the date is the artifact's. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

The idea came from the NETWORK2EXCEL AutoLISP post, which gives three formulas (IL_US, IL_DS, L and slope S). The drawing is read in the browser and not uploaded; DWG must be saved as DXF first, and Civil 3D pipe networks need EXPORTTOAUTOCAD so pipes become plain lines. Two synthetic sample drawings with planted defects (US storm in ft, metric storm in m) are included. Tabs: Plan, Manholes, Pipes, Checks, Profile, Export, How it works, About, Doc.

## Results the page reports

- US sample (sample-us-storm.dxf, 68.6 KB, AC1032, $INSUNITS 2 = ft, 47 entities): 7 of 19 data labels placed by drawn evidence, 11 by the distance rule, 1 unplaced.
- UNK-1 has no label (no ID, rim or inverts); the pipe from SMH-301 reaches it with a calculated invert of 815.68 ft, and the outgoing pipe has a slope label but no invert; the app makes one stated assumption there.

## What this does not show

- Civil 3D pipe-network objects, design flows, or capacity against demand.
- Real drawings: the samples are synthetic.

## How to reproduce

Open the page, open a DXF or a sample, and export from Export (.xlsx and others).

## Credits and licenses

The NETWORK2EXCEL post (the idea and formulas). No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, in October 2026, under the direction of Robert (Bob) Dickinson, who chose the problem from the NETWORK2EXCEL post and asked for the documentation. Claude wrote all of the code (the DXF reader, label recognition, network building, the checks, the Excel, CSV, SWMM5 and DXF writers, the GIF encoder and the page) plus two test drawings. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.2: the version read.
