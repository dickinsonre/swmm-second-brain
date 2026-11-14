---
name: SWMM 1 Engine
file: swmm1-runoff-engine.html   # name kept from v1.4, when the page ran the Runoff Block only, so existing links still work
version: 3.6
date: 2026-11-13
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/3g5gzA2tPNLeCXzZyCzyHt", netlify: none, repo: none}
engines:
  - {name: SWMM Version 1 (full program), version: October 1971, source: "EPA 11024 DOC 10/71, Volume IV Program Listing, 248 pages", cards: 12200, units: 65, build: "f2c + Emscripten 3.1.6 (clang 15), libf2c 20140711", license: "US government report, public domain"}
  - {name: SWMM Version 1 with five repaired cards (optional), version: "October 1971 + 2026 repairs", source: "same listing; cards SROU 17, SROU 74, PLUG 21, PLUG192 changed, one COMMON card added to TRCHEK", build: "same as the full program", license: "public domain"}
  - {name: SWMM Version 1 Runoff Block (workbench), version: October 1971, source: "same listing, Section 2, 1,311 cards", build: "hand C translation, wasi-sdk 24", license: "public domain"}
units: US customary (cfs, ft, acres, in/hr), as in 1971
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM 1 Engine: the 1971 Storm Water Management Model, all five blocks, in the browser

**In one sentence.** This page runs the first Storm Water Management Model as it was printed in October 1971, all five blocks and 12,200 cards, and it reproduces a 1971 tide table within 0.004 foot and the 1971 flows of a San Francisco storm to the printed digit.

**In one paragraph.** SWMM Version 1 was a relay of five Fortran programs: an Executive Block that reads block names from cards, and Runoff, Transport, Storage and Receiving Water Blocks that pass hydrographs to each other on tape. All 248 pages of its listing were typed back into Fortran and compiled to WebAssembly, so this page reads 1971 card decks and prints the 1971 report. Three runs printed in 1971 check the work. The estuary example matches 52 printed stage values within 0.004 foot. The sewer example matches except where one card changed between May 1970 and October 1971. A real storm on Baker Street, San Francisco, matches 88 of 95 printed flow and cost numbers to the digit, and shows that the pollutant loads printed for it in August 1971 were about sixty times too heavy. A second real deck, for Philadelphia, reproduces the dry-weather flows printed for all 51 of its tracts.

## What it does
Runs the original SWMM Version 1 from its own Fortran, rebuilt from the scanned program listing. It reads 80-column card decks and writes the 1971 line-printer report and interface tapes. All five blocks run: Executive, Runoff, Transport, Storage, Receiving Water. It is for people who want to see what the first SWMM computed, and for anyone tracing a SWMM 4 or SWMM 5 method back to its first form.

## How it computes
- Source: every card of Volume IV, typed back into fixed-form Fortran with the identification field in columns 73-80.

| Block | Program units | Cards |
|---|---|---|
| Executive (MAIN, GRAPH, CURVE, PINE, PPLOT) | 5 | 389 |
| Runoff | 7 | 1,311 |
| Transport | 25 | 4,114 |
| Storage | 17 | 3,918 |
| Receiving Water | 11 | 2,468 |
| Total | 65 | 12,200 |

- Full-program engine: the listing, translated by f2c to C, compiled by Emscripten to WebAssembly (328 KB). A new module instance per run. Unit 5 is the deck, unit 6 the printout, other units are files `fort.N` in an in-memory file system.
- Build-time edits (temporary copy only, no arithmetic changed): `KILL` renamed `SKILL` (name clash); the two unnamed `BLOCK DATA` units named `TRBLK` and `STBLK`; in `INDATA`, `INQUAL`, `SWFLOW` one `DATA` card moved below the type cards (f2c statement order); `ARSIN(X) = ASIN(X)` supplied; COMMON blocks defined once at their largest declared size.
- Repaired engine (used only when "run with the 2026 repaired cards" is ticked): the same build after `tools/repair.py` changes five cards. `SROU 17` and `PLUG 21` (`DT=DT*60.0`) are removed and `SROU 74` and `PLUG192` (`9999 DT=DT/60.0`) become `9999 CONTINUE`, because STRAGE has already converted DT at `STRA 16`; `COMMON /TBLK/DT,NDT,KDT` is added to TRCHEK. The Run tab's first tile names the engine that made each run.
- Printer plots: the Plots tab finds every plot page in the printout (pages drawn by CURVE, PINE and PPLOT, 101 by 51 print positions) and draws each one as printed. A `GRAPH` block card plots any interface tape: cards `NTAPE,NPCV,NQP,NPLOT` (16I5), optional element list, title, horizontal label, `NQP+1` vertical labels (20A4).
- Runoff workbench engine: statement-for-statement C translation of the seven Runoff routines (version 1 of the app), used for Runoff-only decks and for the SWMM 5 `.inp` and SWMM 4 `.DAT` importers.
- Deck routing: a deck containing a block card (`WATERSHED`, `TRANSPORT`, `STORAGE`, `RECEIVING`, `ENDPROGRAM`) goes to the full program; any other deck goes to the workbench.
- Methods, as coded in 1971: Runoff, nonlinear reservoir on three planes per subarea with Horton infiltration (WSHED), gutter and pipe routing (GUTTER), surface quality (SFQUAL). Transport, elements sequenced upstream to downstream, kinematic wave by Newton iteration on normalized flow-area tables for 12 conduit shapes (ROUTE, NEWTON), dry-weather flow (FILTH), infiltration (INFIL), quality routing (QUAL). Storage, basin routing (STRAGE, SROUTE, PLUGS), a string of treatment units (TREAT), cost (TRCOST). Receiving Water, link-node explicit hydrodynamics (SWFLOW) and quality (SWQUAL, LOOPQL).

## Inputs and outputs
- Companion files: `pdf/SWMM1_Volume_I_Final_Report.pdf` (338 PDF pages), `pdf/SWMM1_Volume_II_Verification_and_Testing.pdf` (173 PDF pages), `pdf/SWMM1_Volume_III_Users_Manual.pdf` (359 PDF pages), read by the PDF tab; Volume IV (248 pages) is embedded in the HTML.
- Input: card decks (text, 80 columns). Executive header: title (10A4); `NSERYS,ACRES,ADDWF,NDESYR,DESFLO,NSTRMS,QTRUNK` (I5,F10.1,F10.2,I5,F10.1,I5,F10.1); `NSTRMS` storm cards (4A4,4A4); tape pairs `JIN,JOUT` (20I4); `NSCRAT(5)` (20I4); then block name cards, each followed by that block's cards; `ENDPROGRAM`.
- Interface tape (unformatted, 4-byte record markers): title (40 words); `NSTEP,NPOINTS,NQUAL,DT,TZERO,TAREA`; element numbers; then per step time, flow per point, `NQUAL` loads per point. Storage always reads unit 10 and writes unit 11.
- C source: Fortran tab, "Download the C (.zip)" gives `swmm1-c-source.zip`: `c/` (65 program units translated by `f2c -w -E -Nn802 -Nx400`, plus `commons.c` and `arsin.c`), `fortran/` (the listing with the build-time edits), `wmain.c`, build scripts. Native compile: `gcc -O0 -w c/*.c -lf2c -lm`. Machine-translated; as-printed cards only.
- Output: the printout (carriage control in column 1), every tape left on disk (charted and downloadable as CSV), and for Receiving Water the stage table parsed from the printout.
- Make a GIF (header button): records a 15-frame, 960 by 600 walkthrough inside the page and saves `swmm1_engine_walkthrough.gif` (about 675 KB, 40 s). It runs Runoff sample 1, then the Baker Street and Kingman Lake decks, draws each frame from the live page, and puts the user's deck back. html2canvas and gif.js are embedded, so it works offline and inside a claude.ai artifact.
- Importers (workbench only): SWMM 5 `.inp` and SWMM 4 `$RUNOFF` decks are converted to SWMM 1 Runoff cards. For a `.inp` the page shows a conversion inventory (every non-empty section marked Preserved, Converted, Approximated, Omitted or Unavailable; the label "Simplified SWMM 1 reconstruction" when a section that changes results has no translation) and a rainfall check (time span, depth, interval and peak in the file against the cards). Rainfall rule since 3.6: a record keeps its calendar date, lasts one gage interval or until the next record, and is spread over the SWMM 1 blocks by overlap, so depth is conserved inside the run. The snow catch factor is not applied. Green-Ampt: minimum rate = conductivity (second parameter), maximum rate = 3 times conductivity, a rule of thumb.
- Run status (since 3.6): four separate rows after every run. Execution (ENDPROGRAM reached, or an expected historical stop), Numerical validity (count of NaN and Inf values in the printout), Conservation (Runoff's printed continuity error, with the HYDR137 caution), Reference agreement (the live check against a printed 1971 table, when one is stored).
- Run record (since 3.6): "Run record (.json)" saves the exact deck, the input tapes (base64), the engine and repair mode, app version, statuses, conversion report, printout, and SHA-256 hashes. Editing the deck after a run shows "Inputs changed since this run" on the Run, Printout and Plots tabs.

## Checks

The six 1971 runs at a glance (details follow):

| 1971 run | Printed in | Blocks | Agreement | What does not agree, or what was found |
|---|---|---|---|---|
| Estuary example | Vol. III, Tables 6-3, 6-4 | Receiving Water | 52 stage values, largest difference 0.0041 ft, mean 0.0006 ft | The listing prints a different stability limit (`INDA314T`) from the manual's printout |
| Sewer example | Vol. III, Table 4-8 | Transport | Area and capacity table to the last digit; 6 of 10 hydrographs to 0.001 cfs | 4 hydrographs differ by up to 0.4 % in early steps, traced to card `INIT 55` |
| Baker Street, San Francisco | Vol. II, Tables 2-7, 2-8, 2-10, 2-11 | Runoff, Transport, Storage | 88 of 95 flow and cost numbers to the digit, 95 within 1 %; input volume 8.161 MG identical | Storm pollutant loads far above this listing's (card `TRAN346`, peak hours only) |
| Wingohocking, Philadelphia | Vol. II, Tables 5-1, 5-7 | Runoff, Transport, Storage sizing | 51 of 51 subarea dry-weather flows to two decimals; 150 of 153 flow, BOD and solids values | August 1967 storm has no printed Runoff cards; basin routing not scored |
| Bloody Run, Cincinnati | Vol. II, Table 3-1, Figure 3-9 | Runoff, Transport | Outfall dry-weather flow 13.940 cfs against 13.94 reported | Peak 1,821 cfs against about 1,770 drawn; `HYDR137` leaves `WAREA(J)` out of the continuity check |
| Kingman Lake, Washington, D.C. | Vol. II, Tables 4-1 to 4-3, Figure 4-15 | All five | 53 of 55 storage design numbers to the digit, 55 within 1 % | Pollutant totals 30 % and 17 % low; the basin fills (34.70 of 35 ft) and Storage stops in `INTERP` |

Mechanical checks of this build:
- Complexity (SWMM App Complexity Meter analyzer 1.7.0, baseline HC-2026-11-10-h, HydroCouple = 100; `tools/complexity.js` over 155 source files, generated C, libraries and scans left out): index 70.2; Size 62.4, Structure 76.8, Test evidence 32.3, SWMM vocabulary 86.5; the shipped .html alone 61.7. Counts: 260,146 code tokens, 851 routines, 4,100 decision points, 51 test markers, 8 outside libraries, 18 file formats, 65 of 226 SWMM 5.2.4 terms.
- Outside review of 3.5, acceptance tests (`app/test/t16.js`, headless Chromium): 23 of 23 pass (rainfall gap, dates, snow factor, Green-Ampt field, inventory, zero interval, escaped names, stale results, four statuses, run record, dropped deck).
- Receiving Water vs the 1971 User's Manual (Volume III, Table 6-3 deck, Table 6-4 output): 52 printed stage values (junctions 2 and 8, day 2), largest difference 0.0041 ft, mean 0.0006 ft, tide range 4.8 ft. Junction and channel tables match except the stability column (see limits). Channel flows agree to about 0.1 %.
- Transport vs the manual's example (Table 4-8 deck, 32 elements, 12 shapes, 50 steps of 240 s): full area and capacity table matches to the last printed digit; 6 of 10 printed outflow hydrographs match to 0.001 cfs; 4 differ by up to 0.4 % in early steps, traced to card `INIT 55` (starting dry-weather flow scaled by `DVDWF*HVDWF`). With that scaling removed as an experiment, element 203 gives 46.289, 78.932, 60.753, 65.903, 65.344, the manual's values exactly. Manual run dated May 1970; listing October 1971.
- Runoff + Transport + Storage vs Volume II (EPA 11024 DOC 08/71), Baker Street, San Francisco, storm of 19-20 December 1969: deck from Appendix A (printed pages 143-146), output Tables 2-7, 2-8, 2-10, 2-11. 95 printed numbers that depend on flow and cost only: 88 identical to the printed digit, 6 cost totals near $1.7 million differ by $4, 1 annual cost 134,048 vs 134,049. All 11 printed average flows identical (2.69, 3.63, 64.24, 61.83, 80.03, 29.38, 21.11, 6.48, 4.29, 3.54, 3.40 cfs); input volume 8.161 MG identical. `tools/mk_baker.py`, `tools/score_baker.py`; wasm and GNU Fortran give the same score.
- Same run, pollutant loads (do not agree): BOD to the plant 70,998 lb printed vs 2,164 lb here; suspended solids 1,300,754 vs 22,114; coliforms 2.46E15 vs 8.69E14. Experimental native build with card `TRAN346` (`PLUTO(ND,NJ)=PLUTO(ND,NJ)/60.`) made a CONTINUE (`tools/exper.py a`, not in the app): 74,642 lb, 1,254,030 lb, 2.37E15; percent removed at 1:25, 2:35, 3:45 = 35.96, 37.36, 28.90 (BOD) and 49.14, 51.05, 39.49 (SS), identical to the 1971 print; SS arriving at 2:35 and 3:45 = 23,725 and 11,772 mg/L vs 23,699 and 11,729 printed. Hours 0:15, 4:55 and 6:05 are not reproduced (for example SS 9,739 vs 1,618 mg/L at 4:55).
- Runoff + Transport vs Volume II, Wingohocking, Philadelphia (Appendix A printed pages 166-172; 5,434 ac, 57 subareas on 4 gages, 129 elements; `tools/wingo_data.py`, `tools/mk_wingo.py`, `tools/score_wingo.py`). FILTH table vs Table 5-1: 51 of 51 subarea flows identical to two decimals; subtotals 4.35, 5.83, 8.57, 14.77 and total 14.89 cfs identical; 150 of 153 flow/BOD/SS values identical (differences: tract 222 SS 0.08 vs 0.09, tract 429 BOD 0.16 vs 0.15, tract 510 BOD 0.30 vs a doubtful 0.23). Storm of 3 July 1967 at element 108: peak 2,599.1 cfs at step 27, second crest 1,705 cfs at step 42; 1971 Figure 5-4 (plot, read by eye) about 2,600 and 1,700. wasm and GNU Fortran agree (1 of 15,588 printed numbers differs by more than 0.1 %).
- Storage basin sizing, Wingohocking (`mk_wingo.py DIR aug --qdes`): with QDESYN = 632.34 cfs the basis of design equals Table 5-7 (696.15 cfs = 450.00 MGD, KMOD 18; storage 31,920 / 121,440 / 261,840 / 456,480 / 694,320 / 958,320 / 1,251,360 / 1,575,120 / 1,929,120 / 2,299,680 cu ft; 2.79 x QPUMP x DT; 36 microstrainers of 12.50 MGD, 217.01 sq ft; bar racks 348.08 vs 348.07 cfs per screen) and the storm-independent rows of Table 5-9 (microstrainers $10,306,800 vs $10,306,770 installed; outlet pumping $2,378,011 vs $2,378,008; land 8.03 ac).
- Runoff + Transport vs Volume II, Bloody Run, Cincinnati (Appendix A printed pages 147-151; 2,380 ac, 38 subareas, 71 surface-quality subareas, 117 elements, 36,705.5 ft, storm of 12 May 1970, 1.757 in., 50 steps of 5 min; `tools/cinci_data.py`, `tools/mk_cinci.py`, `tools/score_v2b.py cinci`). Outfall (element 107) dry-weather flow at step 1: 13.940 cfs; Table 3-1 "Reported" at location 6: 13.94 (its "Computed": 13.61, not reproduced). Storm peak 1,821.2 cfs at step 14 (8:40); computed curve of Figure 3-9, read from the drawing: about 1,770 cfs at 8:45; rise matches with a 10 min shift, recession slower here (940 cfs at 9:50 vs about 500 at 10:00). FILTH running totals 0.51, 0.90, 2.01, 8.23, 9.35 cfs vs Table 3-1 Computed 0.90, 0.50, 2.12, 12.58, 0.80, 13.61 (two agree). Pollutants not comparable (peak BOD 190 lb/min here vs about 1,100 drawn; the report's three dummy subareas are not on the cards). wasm and GNU Fortran agree.
- Runoff + Transport vs Volume II, Kingman Lake, Washington, D.C. (Appendix A printed pages 152-162; 4,060.1 ac, 53 subareas on 2 gages, 57 surface-quality subareas, 152 elements, 105,329 ft, storm of 22 July 1969, 95 steps of 5 min, KASE 1 dry-weather flow 27.8 cfs with CF2 = 1.22; `tools/king_data.py`, `tools/mk_king.py`, `tools/score_v2b.py king`). At outfall 149, wasm engine: BOD 3.9 to 225.7 mg/L, mean 49.2 (Table 4-1: 4 to 220, mean 47); SS 31.2 to 872.7, mean 259.6 (6 to 977, mean 267). BOD every 30 min from step 1: 226, 143, 78, 61, 38, 21, 4, 7, 13, 9, 17, 25, 34, 43, 49, 72 (Table 4-2: 220, 135, 79, 84, 49, 40, 14, 4, 6, 6, 10, 19, 27, 37, 42, 63). Totals 403,815 lb SS and 38,507 lb BOD (printed 581,000 and 46,500). Peaks: 5,091 cfs; second Transport run (156 elements, type 18 dividers at 45, 63, 69) 4,136 cfs at 149 and 2,007 at 156; Figure 4-15 printer plots about 4,800, 4,100, 2,000. GNU Fortran: 5,091, 4,025, 2,007 (up to 3 % apart from wasm for a few steps at the second peak). Surcharged elements, first run: 22, 38, 88, 96, 103, 109, 139. Element 139 (gothic, 23.5 ft, slope 0.001): QFULL 4,004, QMAX 4,264 cfs.
- Storage design vs Table 4-3, Kingman Lake (`deck_st.dat`, repaired engine, `score_v2b.py design`): 55 storm-independent numbers, 53 identical, 55 within 1 % (21,105,000 vs 21,104,990 cu ft at 31.5 ft; 38.68 vs 38.67 cfs per screen). Includes 77.35 cfs = 50.00 MGD (KMOD 8), 11 depth-storage pairs to 23,450,000 cu ft, 288.54 x QPUMP x DT, 4 filters of 434.13 sq ft, contact tank 69,615 cu ft. With the 22 July storm the basin reaches 34.70 of 35 ft at step 46 and Storage stops in INTERP. As printed, the engine stops at the filter check (`TRCH104`).
- Receiving Water, Kingman Lake (`deck_rw.dat`, 48 junctions, 50 channels, tide at junction 32, 2 tidal cycles of 25 h, 60 s step): runs to "RECEIVING SIMULATION COMPLETED" on wasm and GNU Fortran without the saved tape; nothing scored.
- Experimental native build with `WAREA(J)*` added to card `HYDR137` (`tools/exper.py c`, not in the app): Cincinnati continuity error 17.76170 % becomes 0.07075 %, surface storage 205,030 becomes 2,889,556 cu ft, rest of the printout identical; Wingohocking unchanged at 0.42110 %.
- Three builds, five test decks: wasm vs native f2c, printouts byte-identical (21,804 printed numbers). GNU Fortran 13.3 vs f2c, numbers differing by more than 0.1 %: Runoff 0 of 3,086; Transport 48 of 6,346 (max 0.5 %); Transport + Storage 114 of 9,213 (max 3 %); Receiving Water 152 of 3,159 (max 7.7 %).
- Fourteen added decks (2026, `tools/mk_variants.py`), each run on GNU Fortran and on the wasm engine. As printed, 11 run to the end and 3 stop (`st_filters`, `st_orifice`, `st_weir`); with the five repaired cards all 14 run. Numbers differing by more than 0.1 % between the two builds: 0 for the GRAPH deck, the infiltration deck and every Storage deck; Receiving Water weir deck 394 of 3,135; restart deck 152 of 3,337.
- Repaired engine vs as-printed engine on the pumped Transport + Storage deck: printouts identical. The as-printed engine's five-deck results are unchanged from version 2.
- Infiltration deck: INFIL prints a melt term of 15.8 gpm and apportions 0.100 and 0.113 cfs to the two pipes (base 30 gpm, rain-induced 50 gpm, storm on day 270).
- GRAPH deck: 8 printer plot pages (Runoff hyetograph and hydrographs, both inlets on one page from unit 8, Transport outfall flow, BOD, suspended solids, coliforms from unit 10).
- Runoff workbench engine vs native build of the listing: sample 1 interface tape byte-identical; sample 2, 14 values differ, largest relative difference 1.6e-6.
- Transcription: every card compared with its page image (by the AI), ink-per-column check of typed text against the scan, all 65 units compile with GNU Fortran and f2c.

## Bugs and quirks found in the October 1971 listing

Behavior of the cards as printed, found by running them. The as-printed engine keeps all of it; the optional repaired engine changes five cards (see the engines above).

- Storage with an orifice or weir outlet converts DT from minutes to seconds twice (`STRA 16`, then `SROU 17` and `PLUG 21`) and stops in `INTERP`; pumped outlets (`ISTOUT = 6`) work.
- TRCHEK tests DT with no COMMON card for it (`TRCH104`, `TRCH106`), so every deck with high-rate filters (`ITREAT(4) = 43`) is refused with "DT = 0.00 MIN. IS AN UNACCEPTABLE VALUE".
- STRAGE's cards marked TEMPORARY (`STRA 88` to `STRA 99`) drive the start depth negative when inflow exceeds the pump rate with the pump off, and the run stops (not repaired).
- SWQUAL rewinds the hydraulics file inside the restart-tape loop (`SWQU143`, `SWQU144`), so the tape holds NQCYC copies of the first quality cycle's flows.
- Transport reads `JPLOT` and never uses it.
- GRAPH reads a title card (`GRAP 30`) and then overwrites it with the tape's title (`GRAP 35`).
- HIGHRF keeps an ASSIGNed GO TO label across calls: f2c runs it, GNU Fortran stops.
- `TREA887` sets `KNTOF = 10**12` (integer overflow).
- `KILL` divides by inflow suspended solids (NaN when zero).
- Runoff's continuity check omits `WAREA(J)` on pervious storage (`HYDR137`; flows unaffected).
- Storage reads tape pollutants as `((POLL(KDT,K,J),J=1,NOUTS),K=1,NPOLL)` (`STOR103`-`104`) while Transport writes `((OUTTAP(J,KK),KK=2,NPOLS),J=1,NOUTS)` (`TRAN497T`-`498`), so with two or more outfalls on the tape Storage takes coliforms as suspended solids.
- A full basin has no spill: INTERP stops the run.
- `HYDR 26` sets `NRANVL = 200` and `HYDR 51` to `HYDR 55` clear 200 elements of `HGRAPH`, `HTIME` and `RAIN`, which are dimensioned 160. Checked in the f2c build: blank COMMON is one static block of 106,244 bytes (sized by GRAPH), of which HYDRO declares 45,120. `HGRAPH(161..200)` lands on `HTIME(1..40)`, cleared by the same loop; `RAIN(161..200,J)` lands on the next column of `RAIN` and, for J = 10, on `NHYET(1..40)`; `HTIME(161..200)` lands 160 bytes past HYDRO's declaration, on `X(1..40,1)` of HCURVE's plot arrays. All of it happens before `RHYDRO` reads a card (`HYDR 63`), and every word touched is read or computed again before it is used, so nothing is corrupted in the full-program engine. The hand-translated workbench engine was not examined for this.
- Receiving Water prints a stability limit `0.75*L/SQRT(32.2*(R+2))` (card `INDA314T`); the manual's printout used `L/SQRT(32.2*(R+5))`. The manual example's 300 s step exceeds the listing's limit in 9 channels.

## What this does not show
- Not done from the outside review of 3.5: conversion and engine runs still execute on the main thread (no worker, no cancel, no time limit); no mounted-tapes panel; no card-field inspector, guided experiments or network sketch; no accessibility pass (tab roles, focus handling, live region); no verification page; the downloadable archive now carries the scoring tools and reference values, but still lacks the hand-written Runoff C and a one-command rebuild; no autosave.
- The four status rows are screens, not proofs: Numerical validity only counts NaN and Inf tokens in the printout, Conservation only repeats what Runoff prints, and pollutant balances are not checked.
- The complexity index measures source footprint against HydroCouple = 100. It says nothing about correctness.
1. No person has compared the 10,889 cards of the Executive, Transport, Storage and Receiving Water Blocks with the page images. 17 doubtful readings are listed on the Fortran tab.
2. Storage is checked three ways: flow through a treatment plant and cost (Baker Street), and the storm-independent sizing of a basin and its plant (Wingohocking Table 5-7; Kingman Lake Table 4-3, 53 of 55 numbers identical). The routing of a storm through a storage basin is not scored anywhere: the manual's example needs an unpublished Transport tape, and Volume II's option 3 is refused by `TRCH 58`, `IF (ISTOR .EQ. 2 .AND. ITREAT(3) .NE. 35) GO TO 25`. Pollutant removals disagree with Volume II by a factor near 60 at the storm's height; the `TRAN346` explanation fits the peak hours only. Receiving Water quality has no check.
3. The Transport + Storage deck, the three-block deck and the fourteen added decks are 2026 test decks. None has a 1971 printout, so their numbers are checked against a second compiler and nothing else.
4. The five repaired cards are a 2026 judgement of what the authors meant. No person has reviewed them.
5. The Baker Street deck is in an older card format and was re-punched: one job, tapes 8/10/11; Transport control card ten fields to nine (NOUTS = 1, NNYN = 1, NNPE = 2 fixed by the three lists that follow the elements); element types 01 (inches), 02, 05 to 1 (feet), 16, 2; FILTH subarea data on one card and three HVCOLI cards of 1.0 added; GRAPH card for the listing. Type 05 as a rectangle is chosen by the printed flows (as an egg: 93 of 95 within 1 %, 6.39 vs 6.48 cfs). The 1971 values were typed from a 72 dpi scan; a few digits are ambiguous. Figure 2-5 of Volume II gives a calculated dry-weather flow of 2.70 cfs; this deck gives 2.51 cfs; not reconciled.
6. Wingohocking: typed from a rough scan (0, 3, 8, 9 often alike); sewer lengths sum to 72,565 ft vs 73,385 ft in the report; printed population subtotals differ by about 2 %. The August 3-4 storm (the one behind Tables 5-8 and 5-9) has no printed Runoff cards; rebuilt from Table 5-3 it gives 84.823 MG to the plant vs 78.091 MG printed and a second crest above the first, so the storage basin's routing is not scored. With the printed DESF = 0.50 that reconstruction stops in Storage (design flow above the largest module).
7. Cincinnati and Kingman Lake are close to Volume II, not digit matches: Table 3-1's Computed column, the SS/BOD totals of the Kingman storm (30 % and 17 % low here) and the later rows of Table 4-2 are not reproduced; figure values were read off a drawing and off printer plots (about 50 and 100 cfs). Tables 4-4 and 4-5 (plant performance, storm of 20 August 1969) and the Receiving Water profiles (Figures 4-11, 4-12) need a tape and cards that were not printed. The routing of a pumped storage basin through a storm is still unscored. Deck changes: Cincinnati tapes 8/10 and element 23 upstream 22, 24 (print: 25); Kingman GRAPH cards `9 1 3` to `9 1 0 0`, elements 36 and 82 left with blank type (manholes by `TRAN164X`), element 148 length 1.090 ft as printed, element 120 length read as 1370, BASEA 670,000 (first misread as 870,000), Receiving Water JIN = 0 and the line `QUALITY` after `ENDQUANT` dropped.
8. Volume I (Final Report) was not read. About 150 of Volume III's 359 pages were read.
9. REAL is IEEE single precision, not IBM System/360 hexadecimal. Expect three to four digits of agreement with 1971 printouts. System/360 single precision is base 16 with a 24-bit fraction, of which 21 to 24 bits are significant, and its arithmetic truncated where IEEE rounds, so long sums drift apart in the last digits; the 4 dollar differences in six Baker Street cost totals near 1.7 million dollars are of that size, though they were not traced to it.

## How to reproduce
- In the app: Run tab, press the "Receiving Water" example button (or pick "Receiving Water: User's Manual estuary" and Load sample). The check card recomputes the 52-value comparison. Samples "Transport" and "Transport → Storage" mount the constant-inflow tape (50, 40, 30 cfs at elements 101, 109, 107) on unit 8.
- Baker Street: Run tab, button "1971 city: Baker Street" (or the sample list group "A 1971 deck for a real storm"). The check card recounts the 95 numbers. `python3 tools/mk_baker.py DIR [egg]` writes the deck; `python3 tools/score_baker.py OUT.txt` scores a printout.
- Wingohocking, Philadelphia: Run tab, button "1971 city: Wingohocking" (or the sample list). The check card recounts Table 5-1. `python3 tools/mk_wingo.py DIR` writes the 3 July 1967 deck from `tools/wingo_data.py`; `python3 tools/score_wingo.py OUT.txt` scores a printout; `python3 tools/mk_wingo.py DIR aug --qdes` writes the August storm with the storage basin sized as in Table 5-7.
- Cincinnati and Kingman Lake: Run tab, buttons "1971 city: Cincinnati" and "1971 city: Washington", or the sample list. `python3 tools/mk_cinci.py DIR`, `python3 tools/mk_king.py DIR` write the decks; `python3 tools/score_v2b.py cinci|king|design OUT.txt` scores a printout. The Kingman storage sample needs "run with the 2026 repaired cards".
- Added decks: Run tab, sample list group "Parts of the program the first examples never reached", or the "Printer plots" button; then the Plots tab. Tick "run with the 2026 repaired cards" for the three decks that say they need it.
- The scripts named here are in `swmm1-c-source.zip` (Fortran tab, "Download the C") under `tools/`, with the 1971 reference values under `reference/`. They carry the build machine's paths. There is no public repository yet.
- From source: download the whole listing on the Fortran tab; apply the build-time edits above; `gfortran -std=legacy -fno-automatic -ffixed-line-length-72 -fallow-argument-mismatch -fno-range-check -finit-local-zero`, or `f2c -E` then any C compiler with libf2c.

## Credits and licenses
- SWMM Version 1: Metcalf & Eddy, Inc. (Palo Alto), University of Florida (Gainesville), Water Resources Engineers, Inc. (Walnut Creek), for the EPA Water Quality Office, 1969 to 1971. Reports 11024 DOC 07/71 (Vol. I), 08/71 (Vol. II), 09/71 (Vol. III), 10/71 (Vol. IV); this build used Vol. IV in full, Vol. II (all pages by OCR; the San Francisco section and Appendix A as images; Figures 5-4, 3-9 and 4-15 read by eye for Philadelphia, Cincinnati and Washington) and part of Vol. III. US government publications.
- f2c and libf2c: AT&T, Lucent Technologies and Bellcore; notice below. Emscripten (MIT / NCSA).
- Importer input formats: EPA SWMM 5, written by Lewis A. Rossman, U.S. EPA (first released 2004); SWMM 4, Huber and Dickinson (1988), EPA/600/3-88/001a. Neither program's code is used.
- SWMM 4 sample decks: SWMMEnablement/legacy-swmm-ai.
- GIF recorder: html2canvas 1.4.1, Copyright (c) 2022 Niklas von Hertzen, MIT License; gif.js 0.2.0, Johan Nordberg, MIT License. Both are embedded unmodified.
- App: Robert Dickinson.

```
Copyright 1990 - 1997 by AT&T, Lucent Technologies and Bellcore.

Permission to use, copy, modify, and distribute this software
and its documentation for any purpose and without fee is hereby
granted, provided that the above copyright notice appear in all
copies and that both that the copyright notice and this
permission notice and warranty disclaimer appear in supporting
documentation, and that the names of AT&T, Bell Laboratories,
Lucent or Bellcore or any of their entities not be used in
advertising or publicity pertaining to distribution of the
software without specific, written prior permission.

AT&T, Lucent and Bellcore disclaim all warranties with regard to
this software, including all implied warranties of
merchantability and fitness.  In no event shall AT&T, Lucent or
Bellcore be liable for any special, indirect or consequential
damages or any damages whatsoever resulting from loss of use,
data or profits, whether in an action of contract, negligence or
other tortious action, arising out of or in connection with the
use or performance of this software.
```

## AI use
Built with Claude, Anthropic's AI model, in Claude sessions in October and November 2026, directed by Robert (Bob) Dickinson, who supplied the scans and the manual, set the goal and reviews the result. Claude transcribed all 248 pages (training a character classifier on 154,000 labelled character images from the pages already typed, then comparing every drafted card with the page image), wrote the checking tools, built the program three ways, punched the test decks from the manual's tables, ran the comparisons, wrote fourteen more decks from the card descriptions for version 3.0, found the faults listed above by running them, chose the five repaired cards, read Volume II and typed and re-punched the Baker Street deck for version 3.1, ran the TRAN346 experiment, typed the Wingohocking deck for 3.2 and the Cincinnati and Kingman Lake decks for 3.3, read values off Figures 3-9 and 4-15, ran the HYDR137 experiment, and wrote the page, the Doc essay, the Word version and this file. The checks above are mechanical. No person has yet read the newly transcribed cards against the pages or reviewed the five repaired cards, the four Volume II decks, or the 1971 table values and figure readings taken from the scan.

## Changes
- `3.6 (2026-11-13)`: documentation pass after a second outside review (of this file and the Doc summaries): six 1971 runs named in the summaries, scorecard table above the checks, the 1971 bugs moved to their own section, the `HYDR 26` overrun traced through blank COMMON, Storage limits narrowed, Wingohocking added to How to reproduce, scoring tools added to the source archive. Also answers an outside review of 3.5 (ChatGPT, 85 of 100). Importer: rainfall dates kept, a rainfall value lasts one gage interval (was carried across gaps), snow catch factor no longer applied to rain, Green-Ampt conductivity read from the right field, zero gage interval rejected, conversion inventory and rainfall check, imported names escaped. Runs: four status rows, stale-result banner, run record with hashes, engine named before the run, a dropped deck no longer keeps a sample's tapes, the GIF recorder restores the session on failure. Doc: the factor of sixty stated with its limits (totals 33, 59 and 2.8 times), EXTRAN named as the SWMM 5.2 default surcharge method, a table of which checks are independent, and a complexity box (index against HydroCouple = 100). 23 acceptance tests (`app/test/t16.js`). No engine change.
- `3.5 (2026-11-13)`: Make a GIF repaired and brought up to date. It no longer fetches its encoder from a CDN (inside a claude.ai artifact that fetch was refused and the button produced a WebM video instead of a GIF); html2canvas and gif.js now ride in the file. The frames, last written for v1.4 (Runoff only), now show all five blocks and the San Francisco and Washington checks against Volume II. No engine change.
- `3.4 (2026-11-13)`: Fortran tab gains "Download the C (.zip)": the 67 C files (25,998 lines) that f2c makes from the listing, the Fortran they were made from, build scripts and a README. No engine change.
- `3.3 (2026-11-13)`: the last two Volume II decks added: Bloody Run, Cincinnati (12 May 1970) and Kingman Lake, Washington (22 July 1969: two Transport runs, the storage basin and plant, Receiving Water), each with a live check against Volume II. Findings: `HYDR137` (continuity check), `TRAN497T`/`STOR103` (tape order with two outfalls). No engine change.
- `3.2.1 (2026-11-12)`: PDF tab reads all four volumes (IV embedded; I, II, III from `pdf/` beside the page, or chosen from disk).
- `3.2 (2026-11-12)`: Wingohocking, Philadelphia added from Volume II: July 3, 1967 deck with a live check of Table 5-1, and a labelled reconstruction of the August storm with the storage basin. Plots tab no longer mistakes a long element table for a plot. No engine change.
- `3.1 (2026-11-12)`: Volume II read. Baker Street, San Francisco (storm of 19-20 December 1969) added as a sample with a live check against Tables 2-7, 2-8, 2-10, 2-11; Doc section on the factor of sixty in the 1971 pollutant loads (card TRAN346) and on card TRCH 58. No engine change.
- `3.0 (2026-11-12)`: fourteen decks for the parts never run (Transport infiltration, ten Storage options, Receiving Water weir and restart tape, the GRAPH block); a Plots tab that shows every 1971 printer plot page; an optional engine with five repaired cards so Storage gravity outlets and high-rate filters run; Sources corrected to say which volumes were read.
- `2.4 (2026-11-12)`: four questions near the top of the Doc tab and Word document, with their answers at the end. No engine change.
- `2.3 (2026-11-12)`: a row of buttons on the Run tab loads one example for each block; the full-program decks are listed first in the sample list. No engine change.
- `2.2 (2026-11-12)`: the one-page summary carries one image, the rebuilt code against the 1971 printed stage values. No engine change.
- `2.1 (2026-11-12)`: Doc tab and Word document open with the essay in one sentence, one paragraph and one page, and every section starts with a one-sentence summary. No engine change.
- `2.0 (2026-11-12)`: Executive, Transport, Storage and Receiving Water Blocks transcribed; full-program engine (f2c to wasm); five full-program sample decks; live check against the manual's Receiving Water printout; whole listing on the Fortran tab; Doc essay extended.
- `1.4 (2026-10-22)`: Runoff Block only (hand C translation), SWMM 5 and SWMM 4 importers.
