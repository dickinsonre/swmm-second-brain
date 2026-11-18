---
name: Legacy SWMM Converter
file: legacy-swmm-converter.html
version: 1.0.0
date: 2026-10
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/QBiLynVKTENeBm97jRhPmZ", original: "https://legacy-swmm-ai.lovable.app (Legacy SWMM AI, which sent SWMM4 decks to Google Gemini through a Supabase edge function)", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, build: "Emscripten single-file build (commit 7952ca8, 2023-10-10), 678,177 bytes, carried over byte for byte from Seven SWMM Engines", license: public domain}
  - {name: SWMM 4.4H, version: "Huber/CDM 2004 Fortran", build: "f2c to Emscripten, from the SWMM 4.4H Workbench via Seven SWMM Engines; 2,085,703 bytes"}
  - {name: swmm4to5.js, version: 1.0.0, note: "the deterministic converter written for this app"}
units: US customary, as the SWMM4 decks are
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction, and that it replaces the original's AI conversion with a deterministic one. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/QBiLynVKTENeBm97jRhPmZ, version 1792899207-88b8 (index.html, 4,590,449 bytes, SHA-256 69d71810dc37a8a7eb288c266715061ab251a300b7b0b6bdb77d5552173119a5), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# Legacy SWMM Converter: SWMM4 card decks to SWMM5, with both engines in the page

## In three points
- **What:** A single-file rebuild of Bob's Lovable app Legacy SWMM AI, which converted SWMM4 .DAT decks to SWMM5 .INP files by sending them to Google Gemini. A language model's conversion changes from run to run, so this edition converts deterministically (swmm4to5.js, from the EXTRAN, RUNOFF, TRANSPORT and STRT card layouts), keeps a ledger of every value as DIRECT, ESTIMATED or ASSUMED, and runs the original deck in SWMM 4.4H and the conversion in EPA SWMM 5.2.4 side by side.
- **So what:** 11 of 12 converted sample models run in SWMM 5.2.4 with no error (SWDAT4 needs NWS climate files its deck only names). On the six EXTRAN models where SWMM 4.4H recorded maxima, the median difference in peak conduit flow is 0.5% to 4.8%; on SWDAT1 the 29 subcatchment peaks agree within 0.11% (median 0.03%). The outliers are one pipe, 8060, where 4.4H records a short surge 0:25 into the storm.
- **Now what:** Use it to bring an old SWMM4 deck into SWMM5 with every assumption written down. Water quality, snowmelt, Transport's dry-weather flow and infiltration, storage-treatment and STATISTICS are not converted, inflows from interface files are missing, and coordinates are made up by stated rules where the deck has none.

This summary was written after the fact. The page ships no technical summary of its own. It gives the converter's version (swmm4to5.js 1.0.0) and the build month (October 2026); the version above is that. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Convert, Trace, Network, Run SWMM5, SWMM4 vs SWMM5, Checks, Card reference, Ask, Findings, About, Doc. Every data line of the deck ends in one of four states (used, print control, dropped with a reason, unread); on the ten sample decks the unread count is zero. Checks replace the Lovable app's AI anomaly call with structural checks and engineering screens, each with its arithmetic (for example an adverse slope of -0.160% on conduit 1600, and conduit 1630 at 300 ft, shorter than one Courant step of 340 ft). The Ask tab answers from the engines through a dry-run diff. Samples: EXAM1 to 4 and SWDAT1 to 6, public-domain EPA SWMM 4 examples bundled in the Lovable app.

## Checks (as stated on the page)

- Every sample deck converted and run in EPA SWMM 5.2.4: 11 of 12 ran with no error.
- Every original deck run in SWMM 4.4H, and peaks compared element by element: EXTRAN medians 0.5% to 4.8%; EXAM3, the orifice example, 0.6% with maximum HGLs within a median 0.07 ft; the second SWDAT5 run 0.5%; SWDAT1 subcatchments within 0.11%.
- Conduit 8060: in EXAM1 and EXAM2, 4.4H records its peak 0:25 into the storm (65.4 and 67.6 cfs); in SWDAT5, where NSTART starts keeping maxima after the surge, 4.4H reports 43.6 and 44.5 cfs and the engines agree within 4%.
- Card meanings checked against the 4.4H Fortran (INDAT1, INDAT2, INTRAN, GUTNR, ROUTE, TRANSX).

## What this does not show

As the page lists it: water quality, erosion, snowmelt, Transport's dry-weather flow and infiltration estimates, storage-treatment removal and cost, STATISTICS and EXTRAN bridges are not converted (each drop is a note with deck line numbers); inflows read from interface files outside the deck are absent, so the model runs with less water; Transport inverts and coordinates in decks without XLOC/YLOC are made up by stated rules; the Transport network is checked only through the runoff that feeds it; two engines agreeing shows the conversion kept the model, not that the model is right.

## Credits and licenses

EPA SWMM 5.2.4 (public domain); SWMM 4.4H, Wayne Huber's 2004 Fortran from SWMMEnablement/SWMM_MD_Documents and the CDM/OSU 2001 to 2004 card documentation in SWMMEnablement/WCH_2004_SWMM44H; swmmio readers, the GIF encoder and the engine-chat kernel from Seven SWMM Engines and the socratic-engine-chat skill; the EPA SWMM 4 example decks (public domain).

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who wrote the Lovable original, chose the job, supplied the source and sets what counts as right; responsibility is his. Claude read the Lovable source and the 4.4H documentation and Fortran, wrote the converter (all of swmm4to5.js), the page, its chat tools, the checks, the findings and the Doc essay with its Word version and figures, carried the two engines and readers over from earlier apps, and ran the verification. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 1.0.0 (2026-10): deterministic converter with both engines (the version read).
- Lovable: Legacy SWMM AI, conversion by Google Gemini.
