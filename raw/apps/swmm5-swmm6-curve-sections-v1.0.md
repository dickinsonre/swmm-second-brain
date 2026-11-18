---
name: SWMM5 · SWMM6 Curve Sections
file: swmm5-swmm6-curve-sections.html
version: "1.0"
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/EAViY2MZ5RZp8oFDGyXJNk", repo: none named in the page}
engines:
  - {name: swmm524-curves, source: "EPA SWMM 5.2.4 (tag v5.2.4) plus xcurve.c and small edits to read [OPTIONS] XSECT_GEOMETRY EXACT and POLYGON sections with XPOLYGON curves (OpenSWMM syntax), compiled to WebAssembly", wasm_sha256: 5d7f4bb97dcd701c582ef857fede539f6897009fd502a2418448e7a0ba1545ae, license: "public domain base"}
  - {name: OpenSWMM, role: "separate implementation of the same input, used as a check"}
units: US customary (ft, cfs)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/EAViY2MZ5RZp8oFDGyXJNk, version 1793630521-0451 (index.html, 932,519 bytes, SHA-256 a1a0649c58c53d60dbc64d50137cc151a4850aa727fcd86f4115d64cd207d0ee), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# SWMM5 · SWMM6 Curve Sections: a math curve where the cross-section lookup tables were

## In three points
- **What:** Replaces SWMM's cross-section lookup tables with one boundary curve of arcs and lines, gives the eleven tabulated shapes as curves plus seven families of new ones, runs them in a patched EPA SWMM 5.2.4 in the page, and writes input for three kinds of engine.
- **So what:** In a Gothic sewer in dry weather the tables make the last conduit ring between about 0.46 and 0.98 cfs and hand the outfall a peak 29 percent bigger than the 0.76 cfs that ever entered; with curves it climbs smoothly to 0.760.
- **Now what:** Try the curve geometry on shallow flows in large non-circular pipes, where tables are worst. Five shapes are fits, not confirmed definitions, and no field data says which model predicts better.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); the date is the artifact's. Every number below is copied from the page. No model was run to write this file.

## What it does

SWMM's xsect.dat holds up to five tables per rounded shape (180 numbers for an egg). In August 2026 Corinne Wiesner-Friedman showed for OpenSWMM that the tables disagree, worst at low depth, and her branch replaced the circle with exact geometry; rebuilding the other ten shapes from the width tables came out 2 to 8 percent short on area. This app gives all eleven as curves. Without the option its engine's .out matches stock 5.2.4 byte for byte. Tabs: Curve, Tables, Run, Export, Verify, About, Doc.

## Results the page reports

- Horseshoe: four of its five tables describe one outline and the width table another; at y/H = 0.08 they differ by about 12 percent.
- Basket-handle: its constant says 0.944 H wide, its area table about 0.99 H; the width table times 0.944 integrates 5.9 percent short of the stored area, times 1.0 0.3 percent short, which explains most of an 8.3 percent gap.
- Gothic, Catenary, Semi-elliptical, Basket-handle and Semi-circular have no confirmed definition; their fits (three or four arcs) land within 0.15 percent on area and radius and are labelled as fits.
- Dry-weather continuity: Gothic from -9.10 to -1.05 percent; Semi-elliptical from -8.74 to -1.26; every shape between -0.91 and -1.37 with curves. In wet weather the median worst-moment flow difference runs 0.4 to 2.2 percent.
- Gothic dry run: the most water that ever enters the network is 0.76 cfs; with tables the last conduit rings between about 0.46 and 0.98 cfs for more than an hour and hands the outfall a peak 29 percent bigger than any inflow; with curves it climbs smoothly to 0.760.

## Checks (as stated on the page)

- Byte comparison against stock 5.2.4 with the option off.
- The same input run on OpenSWMM's separate implementation.
- A derivative test of area against width on every shape.
- The reference out-diff and timing scripts.

## What this does not show

- That a model predicts better: no field data was used.
- No person has reviewed the fitted arcs, the defect register or the text.

## How to reproduce

Open the page, pick a shape on Curve, run it on Run, and export input files on Export; Verify reruns the page's checks.

## Credits and licenses

EPA SWMM 5.2.4 (public domain) with the xcurve.c patch. OpenSWMM's XSECT_GEOMETRY EXACT and XPOLYGON syntax and Corinne Wiesner-Friedman's August 2026 article. No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude session in November 2026, under the direction of Robert (Bob) Dickinson, who chose the idea and set the standards. Claude found the idea in earlier project notes, read the EPA and OpenSWMM source, tested the old section definitions against SWMM's tables, fitted arcs to the shapes with no known definition, wrote the C engine patch, the page and its JavaScript, ran the tests, and wrote the Doc and the Word document. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.
