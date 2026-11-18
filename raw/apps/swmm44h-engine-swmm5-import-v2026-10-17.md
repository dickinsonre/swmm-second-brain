---
name: SWMM 4.4H Workbench
file: swmm44h-engine-swmm5-import.html
version: "2026-10-17"
date: 2026-10-17
written: 2026-11-18
author: Robert Dickinson
links: {netlify: "https://swmm44h-engine-swmm5-import.netlify.app", artifact: "https://claude.ai/artifact/FnWcKvgsHhJX3ikBL1Qz9i", repo: "Fortran source from SWMMEnablement/SWMM_MD_Documents"}
engines:
  - {name: EPA SWMM 4.4H, version: "CDM/OSU release of 23 July 2004 (Moore, Dickinson, Huber)", note: "Fortran via f2c and Emscripten 3.1.6 to WebAssembly, 33 compile patches, built 2026-10-17; carried twice: as distributed, and corrected with 121 marked changes"}
  - {name: EPA SWMM, version: 5.2.4, note: "compiled from the EPA source the same way; runs each imported model for the SWMM5 vs SWMM4 tab"}
units: US customary (cfs, ft, in)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in Claude Code sessions in October 2026 under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/FnWcKvgsHhJX3ikBL1Qz9i, version 1792424858-74c2 (index.html, 14,110,965 bytes, SHA-256 355b89a17d44d59e3bafc1eb3b9479ac87330381a8543ed94b99da13f06a49f4), its start view and Doc essay read in headless Chromium on 2026-11-18. Nothing was run to write this file."
---

# SWMM 4.4H Workbench: the 2004 Fortran engine, as distributed and corrected, beside EPA SWMM 5.2.4 in the browser

## In three points
- **What:** The 2004 SWMM 4.4H Fortran source (the CDM/OSU release by Moore, Dickinson and Huber) translated by f2c and compiled to WebAssembly, carried twice (as distributed, and with 121 marked corrections from a 95-entry source audit), with a SWMM5-to-SWMM4 deck converter and EPA SWMM 5.2.4 beside it. Every block has a tab: Executive, Rain, Temp, Runoff, Transport, Extran, Storage/Treatment, Statistics, Combine, Graph.
- **So what:** On 300 SWMM5 models from the 1729 corpus, converted and run in both generations, 252 finished in both and 211 had pipes to compare: the middle model's median difference in conduit peak flow is 8.3%, 114 agree within 10% and 53 differ by more than half. The 121 fixes leave 218 of 286 converted models with the same report apart from two removed print lines, and where they move a peak it is mostly by less than 1%.
- **Now what:** Use it to run old SWMM4 decks again, see what a fix changes, and compare a SWMM5 model with its SWMM4 translation. The differences mix the engines with the translation; nothing is compared with measured flows, and no person has read the 121 changes line by line.

This summary was written after the fact. The page ships no technical summary of its own. Its date is the page's own ("4.4H · 2 engines + SWMM5 · 2026-10-17"); it gives no other version. The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Run a working deck (exam1.dat is loaded at start) or drop a SWMM5 .inp: the converter writes the nearest SWMM 4.4H deck ($RUNOFF for subcatchments, $EXTRAN for the network) and lists in a ledger everything it could not carry (quality, LID, RDII, groundwater, snow, control rules and outlets are dropped). An engine switch chooses as distributed or corrected; Compare engines runs one deck through both and lists every differing line; Evidence holds the census and the audit register. The page asks no server for anything.

## Checks (as stated on the page)

- Browser against a native gfortran build, Extran example: 8,394 report lines, 7,297 identical; of 1,643 numbers that differ, 1,250 differ in the last digit only, and no printed depth or flow of 1 or more differs by more than 1%. The page attributes this to f2c carrying some single-precision expressions in double precision.
- Corrections: nearly every one tested with a small deck before and after; after merging, 395 of 435 test decks reproduced their stored reports exactly and the other 40 differed only where a second fix touched the same deck.
- On 300 converted census models through both 4.4H engines: 218 same report, 68 reports differ, 5 stop in the corrected engine only, 9 finish in neither.
- 26 faults were left alone, each listed, because the right behavior was a design decision or the correction could not be shown safe.

## Census (as stated on the page)

300 SWMM5 models (127 with pipe networks, 173 hydrology only), not filtered for what SWMM4 can represent. 38 stopped with errors in SWMM5 itself; nine translated decks did not finish in SWMM4. Of 211 with pipes to compare: 114 within 10%, 24 from 10 to 25%, 20 from 25 to 50%, 53 over 50%; a quarter agree within 2.5% and a quarter differ by more than 56%.

## What this does not show

As the page lists it: which engine is right (no measurements); differences mix the engines and the translation, which keeps hydrology and hydraulics only; Extran is explicit with a fixed step, so steep short pipes are slow; four items of the defect register remain open; tested in Chromium only; the 121 changes and the translator are checked by machine, not read by a person.

## How to reproduce

Evidence tab: the census and audit tables. Compare engines: any deck through both 4.4H builds. The Fortran source is linked from the header.

## Credits and licenses

SWMM 4.4H (CDM and Oregon State University, 2004; Moore, Dickinson, Huber); EPA SWMM 5.2.4 (public domain); f2c; Emscripten 3.1.6; IBM Plex Sans and Mono (SIL OFL 1.1); html2canvas 1.4.1 (MIT). No license is stated for the page.

## AI use

The page says: built with Claude, Anthropic's AI model, in Claude Code sessions in October 2026 under Robert Dickinson's direction; Claude wrote the patches, the audit, the corrected source, the converter, the page and its text. The Doc essay, in the manner of an Isaac Asimov science essay with Claude as narrator, says a few historical remarks come from Claude's general knowledge and were not checked, and that no person has reviewed the essay or its figures. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2026-10-17: the build read.
