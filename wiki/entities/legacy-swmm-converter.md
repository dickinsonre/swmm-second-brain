---
title: "Legacy SWMM Converter (app)"
type: entity
updated: 2026-11-18
sources: [S322]
tags: [apps, swmm4, swmm5, conversion, history]
reviewed: no
---
Bob's app Legacy SWMM Converter: SWMM4 card decks to SWMM5, with both engines in the page. Version 1.0.0, 2026-10 [S322](../sources/S322-legacy-swmm-converter-summary.md). Its `links:` line names no live Netlify address [S322](../sources/S322-legacy-swmm-converter-summary.md).

**A caution about its source.** The page ships no technical summary. [S322](../sources/S322-legacy-swmm-converter-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S322](../sources/S322-legacy-swmm-converter-summary.md)
- A single-file rebuild of Bob's Lovable app Legacy SWMM AI, which converted SWMM4 .DAT decks to SWMM5 .INP files by sending them to Google Gemini. A language model's conversion changes from run to run, so this edition converts deterministically (swmm4to5.js, from the EXTRAN, RUNOFF, TRANSPORT and STRT card layouts), keeps a ledger of every value as DIRECT, ESTIMATED or ASSUMED, and runs the original deck in SWMM 4.4H and the conversion in EPA SWMM 5.2.4 side by side.
- 11 of 12 converted sample models run in SWMM 5.2.4 with no error (SWDAT4 needs NWS climate files its deck only names). On the six EXTRAN models where SWMM 4.4H recorded maxima, the median difference in peak conduit flow is 0.5% to 4.8%; on SWDAT1 the 29 subcatchment peaks agree within 0.11% (median 0.03%). The outliers are one pipe, 8060, where 4.4H records a short surge 0:25 into the storm.
- Every sample deck converted and run in EPA SWMM 5.2.4: 11 of 12 ran with no error.
- Every original deck run in SWMM 4.4H, and peaks compared element by element: EXTRAN medians 0.5% to 4.8%; EXAM3, the orifice example, 0.6% with maximum HGLs within a median 0.07 ft; the second SWDAT5 run 0.5%; SWDAT1 subcatchments within 0.11%.
- Conduit 8060: in EXAM1 and EXAM2, 4.4H records its peak 0:25 into the storm (65.4 and 67.6 cfs); in SWDAT5, where NSTART starts keeping maxima after the surge, 4.4H reports 43.6 and 44.5 cfs and the engines agree within 4%.
- Card meanings checked against the 4.4H Fortran (INDAT1, INDAT2, INTRAN, GUTNR, ROUTE, TRANSX).

**How to use it, as the summary puts it.** Use it to bring an old SWMM4 deck into SWMM5 with every assumption written down. Water quality, snowmelt, Transport's dry-weather flow and infiltration, storage-treatment and STATISTICS are not converted, inflows from interface files are missing, and coordinates are made up by stated rules where the deck has none. [S322](../sources/S322-legacy-swmm-converter-summary.md)

**What it does not show.** As the page lists it: water quality, erosion, snowmelt, Transport's dry-weather flow and infiltration estimates, storage-treatment removal and cost, STATISTICS and EXTRAN bridges are not converted (each drop is a note with deck line numbers); inflows read from interface files outside the deck are absent, so the model runs with less water; Transport inverts and coordinates in decks without XLOC/YLOC are made up by stated rules; the Transport network is checked only through the runoff that feeds it; two engines agreeing shows the conversion kept the model, not that the model is right. [S322](../sources/S322-legacy-swmm-converter-summary.md)

See [Apps summarized on 18 November 2026: EPANET, converters and SWMM5 tools](../concepts/apps-from-pages-epanet-converters-and-swmm5-tools.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [SWMM 4.4H Workbench (app)](swmm44h-workbench.md), [SWMM 4 against SWMM 5: the 2006 quality assurance tests](../concepts/swmm4-versus-swmm5-qa-2006.md).
