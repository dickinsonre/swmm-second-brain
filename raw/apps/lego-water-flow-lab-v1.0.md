---
name: LEGO Water Flow Lab
file: lego-water-flow-lab.html
version: "1.0"
date: 2026-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/L1QkxgaadXnwuKyqyzNuoQ", original: "Lovable project lego-water-flow (lego-water-flow-source.zip; Vite, React, TypeScript; MIT)", repo: none named in the page}
engines: none (a geometric fit model written for the page; the flow on screen is an animation)
units: US customary (in) by default, SI behind a toggle
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in a Claude Code session in October 2026 at Robert Dickinson's request, from his Lovable original. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/L1QkxgaadXnwuKyqyzNuoQ, version 1792897503-c98a (index.html, 514,628 bytes, SHA-256 449e9c5820df63c55cb9215b20094f4071d4ee814db89d76f9c05601b8839034), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# LEGO Water Flow Lab: will a molecule built from LEGO parts go down a pipe?

## In three points
- **What:** A playful lab that asks whether a molecule built from LEGO parts fits down a household pipe, with a Pipe Fit Tester, a Flow Simulator with Auto-Test, sound and reassembly, a parts list, an assembly guide and a specs table. A single-file edition of Bob's Lovable project; it adds an Engineer's switch with real pipe tables (Schedule 40 steel, copper Type L, PEX SDR 9) and three fit rules, and an Audit tab.
- **So what:** The audit of the Lovable source lists 12 findings (5 fixed, 2 with a switch added, 4 flagged, 1 changed). The worst: Auto-Test ran the starting pipe four times and recorded one row (D1); the fixed Auto-Test returns all four. Pipe tolerances are larger than several of the clearances shown, so a fit on paper can fail in the pipe.
- **Now what:** Use it to teach pipe bores and clearances with toy bricks. No water is modelled; the fit rules are for a straight pipe, so elbows, fittings and the faucet are not checked, and no person has checked the bores against the printed standards.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0 · October 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Lab, Audit, About, Doc. The Lab carries everything from the original (title block, Problem and Solution cards, Pipe Fit Tester, Flow Simulator, parts list, assembly guide, specs). Numbers and sources: Schedule 40 steel OD, wall and ID from Engineers Edge (ASME B36.10); copper Type L from the Copper Development Association's Copper Tube Handbook Table 2b; PEX SDR 9 from PexUniverse and Engineering ToolBox (ASTM F876), which disagree at 1/2 in (0.485 against 0.510 in ID; the page uses 0.485); steel tolerances (OD ±0.016 in, wall not more than 12.5% under nominal) from a Wheatland Tube ASTM A53 sheet; LEGO geometry (8 mm pitch, parts 8n - 0.2 mm long, 9.6 mm brick body; stud height taken as 1.8 mm) from BrickOwl and the Brighton Toy Museum.

## Checks (as stated on the page)

- Node assertions that the as-shipped table reproduces every verdict hard-coded in the original.
- Headless-browser runs of both builds; the fixed Auto-Test returns all four rows.
- A console-error and contrast check of the rendered page in both themes.
- Every file in the source zip read, the original built and run, and every number that decides a fit checked against a published table.

## What this does not show

As the page lists it: no water is modelled; the fit rules are for a straight pipe; pipe tables print nominal dimensions and the allowed tolerances are larger than several clearances shown; the stage draws the bore in proportion and the molecule as a fixed cartoon (the Pipe Fit Tester is the to-scale view). Not yet checked by a person: the edition as a whole, the bores against the printed standards, the faucet claim on the Problem card, and the parts list against a LEGO catalogue.

## Credits and licenses

The Lovable lego-water-flow, MIT © 2026 Robert Dickinson; Engineers Edge; Copper Development Association; PexUniverse; Engineering ToolBox; Wheatland Tube; BrickOwl; Brighton Toy Museum. LEGO is a trademark of the LEGO Group, which is not connected with the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude Code session in October 2026 at the request of Robert (Bob) Dickinson, who wrote the original on Lovable (an AI app-building platform), published it under the MIT licence and supplied its source; responsibility is his. Claude read the source, built and ran the original to reproduce the Auto-Test defect, looked up the pipe tables and LEGO dimensions, wrote the fit model and its Node assertions, rewrote the app as one HTML file, drew the Doc figures and wrote the Doc essay, the page and the Word document. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0 (2026-10): first single-file edition (the version read).
