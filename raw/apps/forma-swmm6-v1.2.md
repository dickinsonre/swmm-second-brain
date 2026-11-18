---
name: Forma × SWMM6
file: forma-swmm6.html
version: "1.2"
date: 2026-11-01
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://forma-swmm6.netlify.app", artifact: "https://claude.ai/artifact/Sjv8Vv75yuMsAobYVvWw8Y", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4, commit 7952ca8379", note: "Emscripten 3.1.51, -O2, single file, single thread"}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: "3c30f1e6c2 (2026-10-17)", license: Apache-2.0, note: "both builds copied byte for byte from Seven SWMM Engines 1.2"}
units: US customary (cfs, ft, ft3, ac, in)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude (Opus 5.5) from 30 October to 1 November 2026 at Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Sjv8Vv75yuMsAobYVvWw8Y, version 1793588262-0575 (index.html, 6,336,104 bytes, SHA-256 7c0b735f386b1589de5e251c89d66b560f197bb7b06c6c6a15585c07a9c4584d), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Forma × SWMM6: a SWMM6 model kept the way a common data environment keeps a drawing

## In three points
- **What:** A working answer to what Autodesk's Forma Data Management would do for a SWMM6 model, built after InfoDrainage 2027.2 learned to open and save models in Forma: one fictional subdivision (Cedar Run) kept as four versions, each run in EPA SWMM 5.2.4 and OpenSWMM 6 alpha 4 in the browser, compared line by line and result by result, with a SWMM version of the Static Volume Summary.
- **So what:** Because a .inp is plain text, versions diff with no vendor viewer, and the volume summary matched both engines' own .out to the printed 0.1 ft3 (36 checks, 224 on a census of all shapes). The checks also turned up engine observations: SWMM6's DYNAMIC_SLOT books slot water as storage (C1 of V3 reads 2,463.5 ft3 against 1,963.5 ft3 of pipe), and FV does not hold a pressurized still pool.
- **Now what:** Use the sample folder to see the bookkeeping, or the Netlify edition to open your own Forma project. The live connection has been tested only against a mock of Autodesk's endpoints; the first real sign-in is its first real test.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.2 · 2026-11-01"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Project, Run, Compare, Static Volume, Review, Background, About, Doc. The Project tab is either a simulated sample folder (versions, author, date, comment, container state) or, on the Netlify edition, your own Forma Data Management project: sign in with Autodesk (PKCE), open any .inp, read every version, save new ones. The Netlify edition carries a server of about forty lines that forwards the page's requests to Autodesk. Each run gets its own Web Worker and a fresh engine instance; SWMM6 options are added to [OPTIONS] at run time so the saved file stays readable by SWMM 5.2.4.

## The model (as the page states it)

Cedar Run: six lots of 4.13 ac, a street, a trunk sewer, later a detention pond; an alternating-block storm of 3.108 in.
- V1 predevelopment, 10% impervious: outfall peak 28.30 cfs in SWMM 5.2.4, 28.31 cfs in SWMM6.
- V2 lots built out to 60% impervious, 18 to 30 in pipes kept: J1 and J2 overflow, about 115,000 gallons; outfall peak 47.71 cfs.
- V3 trunk upsized to 30 to 48 in: nothing floods; outfall peak 74.91 cfs, two and a half times the baseline.
- V4 pond in front of the outfall: peak 31.35 cfs.

## Checks (as stated on the page)

- Storm: both engines report 3.108 in on all four versions.
- Runs: all four versions in SWMM 5.2.4, SWMM6 DW and SWMM6 FV in Node; runoff continuity -0.010 to -0.015%, routing within ±0.03%.
- Static Volume Summary on a level-pool twin of each version: 36 conduit and storage checks matched SWMM 5.2.4 and SWMM6 as written to within 0.1%; 0.00 ft3 at every junction. A census model with all 21 cross-section shapes and six storage shapes, with depth and with elevation offsets: 224 checks within 0.1%. EPA's Example1: 44 checks.
- Forma connection driven end to end in a headless browser against a mock of Autodesk's endpoints, every request body checked against Autodesk's aps-sdk-node.
- v1.2 regressions after an evaluation report of v1.1: 1,274 option-editing checks; token refresh under three concurrent requests; tabular storage; persistence by byte compare.

## Observations on the engines (as the page reports them, not yet reported upstream)

- O1: with SURCHARGE_METHOD DYNAMIC_SLOT a full pipe books slot water as stored volume (+25.5% on C1 of V3); on the still pool, routing continuity reads -1.035% (V4) and -32.064% (V1).
- O2: FLOW_ROUTING FV does not hold the pressurized still pool: link flows reach 74 cfs in V4 and routing continuity is -9.021%.
- O3: SWMM 5.2.4 and SWMM6 DW stop with ERROR 141 when an orifice and a weir both go straight to the outfall; SWMM6 FV ran it.
- O4 and O5 are inherited by 5.2.4 too: a still pool reads -3.713% routing continuity in V1; a TABULAR storage curve with no zero-depth row gives 50 ft3 at 1.00 ft and 1.005 ft3 at 1.01 ft.

## What this does not show

As the page lists it: the live Forma connection is tested against a mock, not a real hub; the sample folder's container states are simulated (the Data Management API does not expose ISO 19650 states); Forma keeps files, not results; nothing says InfoDrainage reads SWMM6 files or that Autodesk plans a SWMM6 connection; the site and storm are fictional.

## How to reproduce

Run tab: Run every version. Static Volume tab: Check runs the level-pool comparison live. The Review tab carries the v1.1 evaluation's items.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); OpenSWMM 6 (HydroCouple, Caleb Buahin and the OpenSWMM team, Apache-2.0); Autodesk's One Water Blog post of 14 September 2026 and aps-sdk-node. No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model (Claude Opus 5.5), on 30 October to 1 November 2026, at the direction of Robert (Bob) Dickinson, who asked for the app from the One Water Blog post, then for it to use Forma itself, then handed over an evaluation report of v1.1. Claude designed Cedar Run and its versions, wrote the model generator, the section diff, the Static Volume Summary and its check, the Forma client and pass-through function, the page, the Doc essay and the .docx, and ran every test. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.2 (2026-11-01): the version read; fixes from the v1.1 evaluation report.
