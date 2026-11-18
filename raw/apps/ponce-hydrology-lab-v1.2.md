---
name: Ponce Hydrology Lab
file: ponce-hydrology-lab.html
version: "1.2"
date: 2026-10-22
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/68sBRNXNG46AvRq1NscxMQ", original: "Lovable project aquifer-quest-zone (React 18, TypeScript, Vite; MIT)", repo: none named in the page}
engines: none (thirty-six calculators written for the page from Prof. Ponce's published methods)
units: US customary by default, SI behind a switch
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the original was built in Lovable, an AI app builder, and that this edition was made with Claude in Claude Code sessions on 21 and 22 October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/68sBRNXNG46AvRq1NscxMQ, version 1792675605-04c4 (index.html, 3,539,623 bytes, SHA-256 df2047d8c726534595017834d7e6da186bc6faa73e2bff46af8c5c6747784199), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Ponce Hydrology Lab: thirty-six hydrology and hydraulics modules after Victor Miguel Ponce's web library

## In three points
- **What:** Thirty-six hands-on hydrology and hydraulics modules in one file, built on the web hydrology library of Prof. Victor Miguel Ponce at San Diego State University: move a slider and the equation, the numbers and the chart answer at once. An independent adaptation, from Bob's Lovable project aquifer-quest-zone, and a teaching instrument, not a design code.
- **So what:** Fifty-seven calculation defects were fixed across three versions (nineteen in v1.0, seven in v1.1, thirty-one in v1.2), each with the original code quoted in the Doc register. The page passes 208 unit tests and 26 formulation checks against Prof. Ponce's own calculator pages; in v1.2 the theory and reference text got 32 corrections and 13 dead links fixed.
- **Now what:** Use it to teach hydrology methods with live numbers. Each method has a range where it stops working (the Doc maps the curve number method's: runoff under 0.5 in is the least reliable), and no person has checked the modules against Ponce's textbook.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Single-file HTML, v1.2 · 22 October 2026"). The page's title reads "Ponce Lab". The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Modules, Reference, About, Doc, with a Source view. Module pages have addresses like #/modules/theis-well. US customary units everywhere with an SI switch; every chart and table exports CSV in the units shown. v1.1: the gradually varied flow module integrates the real profile equation, the routing module derives K and X from the channel (Muskingum-Cunge), and the inlet module handles sags. v1.2: the physics inside eighteen screen components moved into library files (evapotranspiration, flood frequency, environmental flow, culverts, sediment transport, weirs), and the Workflow Builder computes its chain for real.

## Checks (as stated on the page)

- 208 unit tests; 26 formulation checks against Prof. Ponce's calculator pages.
- Every one of the 36 module pages, plus the home, About and Doc pages, opened in headless Chromium in both themes, both unit systems and at 375 px: no console errors, no sideways scroll, and in US mode no SI unit left on any page.
- 57 defects fixed, listed with the original code.

## What this does not show

As the page lists it, starting with the curve number method: no runoff below the initial abstraction, and runoff under 0.5 in is the least reliable region (TR-55). It is a teaching instrument, not a design code. The page lists further limits by module in the Doc.

## Credits and licenses

Scientific content: Prof. Victor Miguel Ponce, ponce.sdsu.edu (Engineering Hydrology, 1989; online edition 2014). The original aquifer-quest-zone is MIT License © 2026 Robert Dickinson. The page states it is an independent adaptation.

## AI use

The page says: the original React project (aquifer-quest-zone) was built in Lovable, an AI app builder, under the direction of Robert (Bob) Dickinson, from Prof. Ponce's published material. This single-file edition was made with Claude, Anthropic's AI model, in Claude Code sessions on 21 and 22 October 2026. Claude compiled the project into one HTML file with address-bar routing, made dark the default, wrote the welcome card, tour and GIF recorder, added US customary units, audited the calculation libraries and fixed the defects, and wrote the About and Doc pages and the Word document. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.2 (2026-10-22): eighteen components' physics moved into libraries; Workflow Builder computes; text audit; 31 defects fixed (the version read).
- 1.1: GVF, Muskingum-Cunge and inlet sags; 7 defects fixed.
- 1.0: single-file edition; 19 defects fixed.
