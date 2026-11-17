---
name: SWMM 3 Runoff & Transport
file: swmm3-runoff-engine.html
version: 2026-10-23
date: 2026-10-23
written: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Fchy5RhShKep5b2bTw87fm", repo: none named in the page}
engines:
  - {name: "SWMM Version III Runoff and Transport blocks (November 1981 release), derived by subtraction from the SWMM 4.4 Fortran and hand-translated to C", source: "SWMM 4.4 Fortran, Oregon State University and CDM, July 2003 / 2004, in SWMMEnablement/SWMM_MD_Documents", license: not stated in the page, build: "wasi-sdk 24 (clang 18) for wasm32 and gcc natively; musl libc 1.2.6 (MIT) transcendental functions shared by both builds"}
units: "US customary as in the 1981 card formats (cfs, cu ft, in, ac)"
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page's own AI-use note says the app was built with Claude under Robert Dickinson's direction, a co-author of the 1981 manual. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Fchy5RhShKep5b2bTw87fm, version 1792729841-e249 (index.html, 8,995,754 bytes, SHA-256 97327e7eb5f335b93e061963c1446d30121091cd016c2be372663413920f6501), its About and Doc tabs read in headless Chromium on 2026-11-16. No deck was run to write this file."
---

# SWMM 3 Runoff & Transport: the 1981 Runoff and Transport blocks rebuilt for the browser

## In three points
- **What:** The 1981 SWMM Version III Runoff and Transport blocks, rebuilt in C by subtraction from the SWMM 4.4 Fortran and run in the browser from 1981 card formats.
- **So what:** The WebAssembly and native builds give byte-identical printouts and interface files on eleven cases, and all 47 Transport example decks of the January 2003 SWMM 4 set convert and run to the end.
- **Now what:** Treat it as a derivation, not a transcription: no 1981 output survives to score against, and no person other than Claude has reviewed the subtraction decisions.

This summary was written after the fact. The page ships no technical summary and no version number of its own, so the version above is the date of the published version read. The file name is the one the page's own GIF caption uses. Every number below is copied from the page's About tab or its Doc essay. No deck was run to write this file.

## What it does

The Runoff Block and the Transport Block of SWMM Version III, the November 1981 release documented in the Storm Water Management Model User's Manual, Version III (Huber, Heaney, Nix, Dickinson and Polmann, University of Florida, EPA-600/2-84-109a), rebuilt to run in the browser as WebAssembly, with the 1981 card formats as input, the 1981 interface file passed between them, and the 1981 limits and numerics. Tabs: Runoff, Transport, Printout, 1981 manual, Card formats, Doc, About.

## Provenance: a derivation, not a transcription

Version III was distributed on magnetic tape (about 25,000 Fortran statements) and the page says no listing of it is known to survive. The engine was made by subtraction from the SWMM 4.4 Fortran: each Version 4 addition was identified from the 1988 manual's list of changes and the dated comments and taken out, and the Version III input, output and limits were restored from the 1981 manual's Tables 4-28 and 6-6, their footnotes and Figure 2-3. Where the sources disagree about numerics, the 1981 manual wins: the 1988 manual says Version 4 wrapped the Runoff Newton-Raphson step in Richardson extrapolation "so that Subroutine Gutter no longer has convergence problems", so here the single step of 1981 (footnote 10) is used. Every such decision is an R3 note in the C source and listed on the Source tab, which the page says shows every SWMM 4.4 line colored by its fate.

## How it computes

- Runoff: Horton (integrated form with regeneration) and Green-Ampt infiltration; the three-subarea nonlinear reservoir; trapezoidal, circular and dummy channel/pipes with surcharge storage; single-event and continuous snowmelt; buildup and washoff of up to ten constituents on five land uses, street sweeping, catchbasins, USLE erosion; continuous simulation from NWS Card Deck 488 hourly precipitation (ICRAIN = 1).
- Transport: Table 6-6 cards A1 to R1; thirteen cross-sections plus two user shapes; manholes, lift stations, flow dividers, two storage units, backwater elements; the kinematic-wave finite difference with Newton iteration (ROUTE/NEWTON/PSI/DPSI); dry-weather flow from FILTH and infiltration from INFIL; complete-mixing pollutant routing with first-order decay for up to four constituents.
- Converters: SWMM 5 .inp and SWMM 4 $RUNOFF and $TRANSPORT decks are punched as 1981 cards; every change is listed in the converter report.
- Deliberate differences: REAL is IEEE single precision (1981 ran on an Amdahl 470 in IBM hexadecimal floating point); continuity summers are double; printout layouts are SWMM 4.4's with the Version 4 columns removed.
- Not here: the Storage/Treatment, Extran and Executive Blocks; ICRAIN = 2; the Version 4 additions by design.

## Defect register (faithful statements the engine keeps)

| No. | Where | Effect |
|---|---|---|
| SNOW-1 | WSHED.FOR 324, 338, 352, 369 | With partial snow cover, (1 - ASC) of the melt is lost: 16 % of the initial pack on the snow1 deck. Kept as shipped (dated 1977); a switch applies the correction. |
| TRANS-1 | TRANS.FOR 87-138; INITAL.FOR 207-214 | The continuity sum omits a lift station's initial wet-well volume: +1,000 cu ft, 2.9 %, on the lift null test; about 1 % of the 2.5 % on the Lancaster deck. Kept; reported. |
| TRANS-2 | TRANS.FOR 720-728 | Flow sent to an element that does not exist is dropped without being counted: -92 % on example TRANS23. Kept. |

## Checks (as stated on the page)

- Two builds, same bytes: the same C compiled by wasi-sdk clang to wasm32 and by gcc natively gives byte-identical printouts and interface files on eleven cases. They were not at first: the two host libraries disagree at the last bit of sinf, cosf, tanf, asinf, acosf, atanf, log10f, exp and pow, so both builds now compile the same musl 1.2.6 routines. The check is tests/wasm_vs_native.js in the source zip.
- Continuity, Runoff (surface / channel): test deck -0.36 % / 0.009 %; Lancaster -0.46 % / 0.15 %; Example 1 -0.05 % / 0.01 %.
- Continuity, Transport: Lancaster fed by the Runoff file 2.47 % flow (TRANS-1 accounts for about 1 %), 0.43 / 2.18 / -3.39 / -0.15 % for the four pollutants; one-pipe null test 0.18 %; divider 0.33 %; two pipes 0.30 %; rectangular 0.51 %; egg 0.27 %; trapezoid 1.07 %; surcharge 0.015 %; lift station 2.87 % (= TRANS-1).
- Census: all 47 Transport example decks of the January 2003 SWMM 4 set convert and run to the end (TRANS12-16 pipelines about 0.01 %; TRANS22 degenerate 0.01 cfs case -135 %; TRANS23 -92 % by TRANS-2; TRANS37 natural channel approximated as a trapezoid -13 %).
- A user shape loaded with the circular tables matches the built-in circular pipe to 0.01 cfs except at low flows.
- The Runoff interface file reads back with the record lengths Figure 2-3 implies; a Transport file read by a second Transport run routes on.

## What this does not show

- No 1981 output survives to score against.
- No person other than Claude has reviewed the subtraction decisions; the page says they are written out so that someone can.

## How to reproduce

Open the page and load a deck on the Runoff or Transport tab, or convert a SWMM 5 .inp or a SWMM 4 deck. The byte-identity test, tests/wasm_vs_native.js, is in the source zip the page names; the zip is not shipped inside the page.

## Credits and licenses

Huber, Heaney, Nix, Dickinson and Polmann (1981), SWMM User's Manual Version III, EPA-600/2-84-109a. Huber and Dickinson (1988), SWMM Version 4 User's Manual, EPA/600/3-88/001a. SWMM 4.4 Fortran, Oregon State University and Camp Dresser & McKee. SWMM 4 example decks, January 5, 2003 set, in SWMMBobSWMM6/1729-SWMM5-Models-2030. Metcalf & Eddy et al. (1971), SWMM Volume IV, Program Listing. musl libc 1.2.6 (MIT).

## AI use

The page says the app was built with Claude, Anthropic's AI model, in Claude sessions on 22-23 October 2026, under the direction of Robert (Bob) Dickinson, a co-author of the 1981 manual, who set the goal (recreate SWMM 3 by subtraction from the SWMM 4 code), asked for the snowmelt, quality and Transport cuts, supplied the Fortran, the scanned manuals and the example decks, chose hand-translation when the sandbox would not run a Fortran compiler, and reviews the result. Claude read the manuals and the Fortran, decided which lines are Version 4 and which Version III, wrote the five C files by hand with a Fortran-I/O runtime, wrote the converters, test decks, defect notes, app, essay and .docx. This summary was written by Claude on 16 November 2026 from the published page.

## Changes

- 2026-10-23: the version read. The page carries no change log.
