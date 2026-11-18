---
title: "S322: Legacy SWMM Converter, summary written from the page (v1.0.0)"
type: source
raw: raw/apps/legacy-swmm-converter-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10
ingested: 2026-11-18
tags: [apps, swmm4, swmm5, conversion, history]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Legacy SWMM Converter, version 1.0.0: SWMM4 card decks to SWMM5, with both engines in the page. Raw file: [raw/apps/legacy-swmm-converter-v1.0.0.md](../../raw/apps/legacy-swmm-converter-v1.0.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/QBiLynVKTENeBm97jRhPmZ, version 1792899207-88b8 (index.html, 4,590,449 bytes, SHA-256 69d71810dc37a8a7eb288c266715061ab251a300b7b0b6bdb77d5552173119a5), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who wrote the Lovable original, chose the job, supplied the source and sets what counts as right; responsibility is his."

**Claims worth keeping** (all copied from the file)
- A single-file rebuild of Bob's Lovable app Legacy SWMM AI, which converted SWMM4 .DAT decks to SWMM5 .INP files by sending them to Google Gemini. A language model's conversion changes from run to run, so this edition converts deterministically (swmm4to5.js, from the EXTRAN, RUNOFF, TRANSPORT and STRT card layouts), keeps a ledger of every value as DIRECT, ESTIMATED or ASSUMED, and runs the original deck in SWMM 4.4H and the conversion in EPA SWMM 5.2.4 side by side.
- 11 of 12 converted sample models run in SWMM 5.2.4 with no error (SWDAT4 needs NWS climate files its deck only names). On the six EXTRAN models where SWMM 4.4H recorded maxima, the median difference in peak conduit flow is 0.5% to 4.8%; on SWDAT1 the 29 subcatchment peaks agree within 0.11% (median 0.03%). The outliers are one pipe, 8060, where 4.4H records a short surge 0:25 into the storm.
- Every sample deck converted and run in EPA SWMM 5.2.4: 11 of 12 ran with no error.
- Every original deck run in SWMM 4.4H, and peaks compared element by element: EXTRAN medians 0.5% to 4.8%; EXAM3, the orifice example, 0.6% with maximum HGLs within a median 0.07 ft; the second SWDAT5 run 0.5%; SWDAT1 subcatchments within 0.11%.
- Conduit 8060: in EXAM1 and EXAM2, 4.4H records its peak 0:25 into the storm (65.4 and 67.6 cfs); in SWDAT5, where NSTART starts keeping maxima after the surge, 4.4H reports 43.6 and 44.5 cfs and the engines agree within 4%.
- Card meanings checked against the 4.4H Fortran (INDAT1, INDAT2, INTRAN, GUTNR, ROUTE, TRANSX).

**Limits it states.** As the page lists it: water quality, erosion, snowmelt, Transport's dry-weather flow and infiltration estimates, storage-treatment removal and cost, STATISTICS and EXTRAN bridges are not converted (each drop is a note with deck line numbers); inflows read from interface files outside the deck are absent, so the model runs with less water; Transport inverts and coordinates in decks without XLOC/YLOC are made up by stated rules; the Transport network is checked only through the runoff that feeds it; two engines agreeing shows the conversion kept the model, not that the model is right.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Legacy SWMM Converter (app)](../entities/legacy-swmm-converter.md), [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [SWMM 4.4H Workbench (app)](../entities/swmm44h-workbench.md), [SWMM 4 against SWMM 5: the 2006 quality assurance tests](../concepts/swmm4-versus-swmm5-qa-2006.md).
