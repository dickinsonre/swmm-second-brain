---
name: EXTRAN III Workbench
file: extran3-workbench.html
version: 1.6.0
date: 2026-11-11
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/6Rw5soUJGWmTBxgV1QhwsF (private until shared)", netlify: none yet, repo: none yet, archive: extran3-1981.zip}
engines:
  - {name: EXTRAN III as printed, source: "CDM listing dated 20-MAY-81, manual pp. 167-228, transcribed from OCR", build: "f2c with libf2c 20140711 -> clang wasm32-wasi -O2", bytes: 193528, sha256: 651fc2a0aa2d4cb5b651a51706239eb5e83dc4091d728fa675d53c10a55cc929}
  - {name: EXTRAN III bugs fixed, source: same listing with ten fixes (port_fixed/FIXES.tsv), bytes: 194491, sha256: 34e36309f18e14a6a4c97cf2f7b0b4170cd1a641f103826d1ccd013cab5d72ad}
  - {name: EXTRAN III as printed with enlarged arrays, source: port/ after tools/enlarge.py, bytes: 193982, sha256: 56a0d9fe399470f0a8cf561bae8848eadac0b50778bf0dea1b5e5dcdee22683a}
  - {name: EXTRAN III bugs fixed with enlarged arrays, source: port_fixed/ after tools/enlarge.py, bytes: 194954, sha256: 88e044122cc422f76e29b3be79cd8a5f3f217afdc1c9ef2065efdc37dcbdcdf8}
  - {name: EPA SWMM, version: 5.2.4, source: USEPA/Stormwater-Management-Model tag v5.2.4, license: public domain, bytes: 529581, sha256: 6f2e7d58fe48c8ec2d33eaf7187e5aa16ff5f002c2d865e92a9db3a6b858029f}
units: US customary (ft, cfs, ft3). SI SWMM models are converted with 3.280839895 ft/m and 35.3146667 cfs per m3/s
ai_use: built with Claude (Anthropic) under Robert Dickinson's direction; see AI use
---

# EXTRAN III Workbench: the 1981 EXTRAN, run from its printed listing, beside SWMM 5

## What it does

The workbench runs EXTRAN III, the Extended Transport block of SWMM Version III (Camp Dresser & McKee, 1981), in a browser. The program was rebuilt from the FORTRAN listing printed in the 1981 user's manual, which survived only as OCR text. One HTML file holds four EXTRAN III engines (as printed and with ten 1981 bugs fixed, each at the 1981 array sizes and with enlarged arrays), EPA SWMM 5.2.4, the seven manual example decks with their printed 1981 results, 164 SWMM 4 EXTRAN decks from January 2003, and ten SWMM 5 sample models.

It answers three questions. Does the rebuilt program reproduce CDM's printed 1981 runs? What does the 1981 method give on a modern SWMM 5 model, next to SWMM 5 itself? What does SWMM 5 give on a 1981 deck?

Outputs: the EXTRAN III line-printer report, charts, a network map, hydraulic profiles, a value-by-value score against the 1981 printout, comparison statistics against SWMM 5, and exports (report, deck, .inp, CSV, GIF, markdown).

## How it computes

**Method (TRANSX).** Link-node explicit solution of the Saint-Venant equations. Continuity at junctions, momentum in conduits, modified Euler: a half step from conditions at t, then a full step using the half-step heads, areas and velocities. The conduit flow update, listing lines TRANSX 144-150:

```fortran
      DELQ4=+DELT2*V(N)**2*(ANH-ANL)/LEN(N)
      DELQ3=2.*V(N)*(A(N)-AT(N))
      DELQ2=-(DELT2*32.2*(H(N,2)-H(N,1))/LEN(N))*A(N)
      QNEW=QO(N)+DELQ2+DELQ3+DELQ4
      AKON=-DELT2*(ROUGH(N)/HRAD**1.33333)*ABS(V(N))
      DELQ1=AKON*QNEW/(1.-AKON)
      QT(N)=QNEW+DELQ1
```

ROUGH = 32.2 n^2 / 2.208. A junction above 0.96 of the depth to its highest crown is treated as surcharged: head is adjusted iteratively until inflow and outflow balance within SURTOL. Stability needs dt below the wave travel time of the shortest conduit, L / sqrt(g D); the program warns when the ratio exceeds 1.

**Run length.** TRANSX runs whole passes of MP = (NTCYC+99)/100 steps (TRANSX 105-108), so steps run = MP * ceil(NTCYC/MP): 1,080 on the card runs 1,089; 1,440 runs 1,440; 2,880 runs 2,900. Both builds keep this.

**Two builds.** As printed reproduces the 1981 runs. Bugs fixed changes ten places and nothing else:

| Where | As printed | Fixed |
|---|---|---|
| DEPTHX 95 | `HRAD=AREA/(WIDE(N)+DTEMP*SROOTS)` (DTEMP never set) | `...+YI*SROOTS` |
| DEPTHX 96-97 | `HRAD**0.677` | `HRAD**0.6667` |
| DEPTHX 56 | rectangle "radius" was its wetted perimeter | `HRAD=AREA/(WIDE(N)+...)` |
| HEAD 86 | `CALL HYDRAD(...,AMID,RMID)` | `...,AMID,BMID)` |
| HYDRAD 45 | `180 WIDTH=WIDE(N)` (closed rectangle never ran full) | `180 IF(DEPTH.GE.DEEP(N)) GO TO 160` |
| TRANSX 340 | `IF(IT-30)562,562,564` | card 3's ITMAX (30 if blank) |
| TRANSX 459 | `VLEFT=VLEFT+Y(J)*ASTORE(J)` | `...*ASTORE(I)` |
| BOUND 229 | `884 QOUT=QINJ` | `884 QOUT=AMIN1(QINJ,PRATE(I,1))` |
| BOUND 234 | `IF(YDEP(J2).GT.VRATE(I,2))` | `IF(YDEP(J1).GT.VRATE(I,2))` |
| OUTPUT 62 | `PCTERR = ((SUMQIN-SUMOUT-VLEFT)/SUMQIN)*100.` | starting volume measured and counted |

**Array sizes.** The 1981 listing holds 187 junctions, 187 links, 20 storage junctions, 60 orifices, 60 weirs, 20 pumps, 25 free and 25 gated outfalls, 65 inflow hydrographs. `tools/enlarge.py` writes a copy of the source in which only sizes change (92 of 2,998 lines, plus 25 continuation lines where a longer line passes column 72): COMMON and DIMENSION sizes, `NDIM=187` in three units, and the constant limits of seven card-reading loops in INDATA. Enlarged sizes: 5,000 junctions and links, 5,000 hydrographs, 1,000 orifices and weirs, 500 storage junctions, pumps and outfalls of each kind. Unchanged: 8 links at a junction, 20 printed junctions and 20 printed conduits, I5 and F5.0 fields, 99,999 steps. The cap is 5,000 because internal links are numbered 90000 + position in five columns. The page uses the 1981-size engine whenever the deck fits and the enlarged engine only when it does not (120 s run limit instead of 30 s).

**SWMM 5 model to EXTRAN III deck (convert.js).** EXTRAN III has no hydrology. SWMM 5.2.4 runs the model first, reporting at its routing step; each node's total lateral inflow from the .out, moved back one step, becomes hydrograph cards (groups 21-22). No time-series files are read. At 1981 sizes the 65 largest-volume inflow junctions keep hydrographs and the rest get their mean flow as constant inflow; the enlarged build keeps every hydrograph. Inflow at outfalls is dropped. Shapes map to EXTRAN's six classes; others become a rectangle or trapezoid of equal depth and full area; barrels become parallel conduits. Every approximation is listed with the run.

**EXTRAN III deck to SWMM 5 model (deck2inp.js).** Names are the deck's numbers; internal links are 90000 + position. Initial depths are kept and initial flows left at 0. An off-line pump becomes a storage wet well with a Pump1 curve, an in-line pump a Pump2 curve. Tide option 2 becomes FIXED, option 3 a TIMESERIES. Options: DYNWAVE, INERTIAL_DAMPING PARTIAL, NORMAL_FLOW_LIMITED BOTH, MIN_SURFAREA 12.566, fixed routing step equal to the deck's dt. Duration uses the steps EXTRAN actually runs.

**SWMM 4 EXTRAN deck to EXTRAN III cards (swmm4.js).** Free-format SWMM 4 lines are rewritten as 1981 fixed-column cards; options EXTRAN III lacks are noted.

**Network map (netmap.js).** A deck has no coordinates. Junctions are placed by distance upstream of the outfalls (multi-source Dijkstra, lengths compressed by the power 0.6), outfalls on the right. A SWMM model's own [COORDINATES] are used when present.

## Inputs and outputs

- Reads: EXTRAN III card decks (80-column text), SWMM 4 EXTRAN-block decks, SWMM 5 or SWMM 6 `.inp` files. SWMM's `.rpt` and `.out` are produced and read inside the page.
- Before running SWMM the converter replaces `[REPORT]` so every node and link is written at the routing step. Lines SWMM 5.2.4 rejects are commented out and listed (up to 30 runs).
- Writes: EXTRAN III report (.txt), deck (.txt), deck as SWMM 5 model (.inp), time series, junction and conduit summaries, the comparison with 1981 and the SWMM 5 comparison (.csv), conversion notes, a profile drawing, an animated GIF of the profile, the bug list (.md).
- Units: ft, cfs, ft3, seconds.

## Checks

Mechanical checks, all rerun on the v1.6.0 build:

| Check | Result |
|---|---|
| Against CDM's printed 1981 output, seven examples, 2,424 values | 2,253 exact with the browser engine (92.9 %); 98.4 % counting last-digit and OCR-confusion differences. Native gfortran build: 2,260 exact |
| Browser engine vs the same C built natively | reports byte-identical on all seven decks, both builds |
| Enlarged vs 1981-size engines, 171 decks (7 manual, 164 SWMM 4) | reports byte-identical, both builds, 10.7 MB each (`test/enlarged.js`, 7 passed) |
| Enlarged as-printed build vs the 1981 printout | the same 2,253 exact |
| 401-junction chain deck | refused by the 1981-size build, runs in the enlarged build |
| SWMM 5 corpus (SWMMEnablement/1729-SWMM5-Models), 257 models, 1981 sizes | 207 through both engines; 34 too big; 10 SWMM 5.2.4 cannot run; 6 cannot be converted. Cards hold SWMM's inflow volume within 1 % in 199 of 202 runs with inflow |
| The 34 too-big models, enlarged builds (`verify/swmm5_corpus_enlarged.tsv`) | 16 through both engines (largest 2,055 nodes, 2,096 links); 9 SWMM 5.2.4 cannot run; 5 over 5,000; 4 other rules (1 over 99,999 steps, 1 nine links at a junction, 2 ideal pumps) |
| Of those 16 | 13 carry inflow; inflow volume within 1 % in 9 and within 5 % in 12; EXTRAN III continuity within 5 % in 2 (each build); continuity prints asterisks in 5; median peak-depth difference from SWMM 5 at most 0.1 ft in 13 of 16 |
| Deck written as SWMM 5 model, 171 decks | all written and run; the manual decks' cards return through the SWMM 5 converter unchanged except for three known rules (outfall ground elevation, Example 6's wet well, Example 7's pump steps); inflow volumes within 0.5 % in all 146 decks with inflow; median peak-depth difference 0.16 ft as printed, 0.12 ft bugs fixed |
| SWMM 4 decks | 164 of 164 translate and finish in both builds; EXAM1 prints Example 1's report byte for byte apart from titles |
| Page tests | shipped.js 67, contrast.js 164 pairs, deck2inp.js 48, netmap.js 17, swmm4.js 101, enlarged.js 7, engines.mjs 22, docs.mjs 15, doc.mjs 48, swmm4tab.mjs 10, deck2inp-tab.mjs 36, netmap-tab.mjs 27, enlarged-tab.mjs 13: all pass |

Human review: Robert Dickinson reviewed results and directed the tests. See below for what no person has checked.

## What this does not show

1. A SWMM comparison tests routing, not hydrology: EXTRAN III receives the inflow SWMM computed.
2. SWMM 5 is a different program, not the truth. A difference is not always a mistake.
3. Agreement with 1981 covers the code paths of the seven examples: circular pipes, trapezoidal channels, free and gated outfalls, one orifice of each type, a weir, storage, both pump types. Rectangular, horseshoe, egg and basket-handle conduits, tide options 3 and 4, and interface files have no printed run to check against.
4. Larger arrays do not make the 1981 explicit method stable on large models; see the continuity counts above.
5. Models over 5,000 nodes or links, over 99,999 steps, with more than 8 links at a node, or with ideal pumps cannot run.
6. Control rules, minor losses, ponding and conduit flap gates have no EXTRAN III equivalent.
7. Open defects: storage-junction drift in SWMM 4 decks EXAM57 and EXAM59 is not explained.
8. Not checked by any person: the 139 doubtful listing lines (136 repairs marked likely or guess, 3 kept as read) against images of the manual pages; every statement of the essay against the code. The essay's Section 11 and its part on the enlarged builds have had no separate review pass.
9. The 257-model corpus statistics were not rerun after the run-length finding; converted models may run a few steps longer in EXTRAN than in SWMM.

## How to reproduce

From `extran3-1981.zip`:

```sh
tools/build.sh && tools/verify.sh                       # native builds, score the seven examples
PORT=port LIBF2C=<libf2c2-20140711> sh app/engine/build-engine.sh
python3 -I tools/defect_variants.py /tmp/v corrected
PORT=/tmp/v/corrected OUT=extran3_fixed.wasm LIBF2C=<...> sh app/engine/build-engine.sh
python3 -I tools/enlarge.py port /tmp/big && PORT=/tmp/big OUT=extran3_big.wasm LIBF2C=<...> sh app/engine/build-engine.sh
python3 -I tools/enlarge.py /tmp/v/corrected /tmp/bigf && PORT=/tmp/bigf OUT=extran3_fixed_big.wasm LIBF2C=<...> sh app/engine/build-engine.sh
node app/test/enlarged.js                               # 171 decks, both sizes of engine
node app/test/corpus-enlarged.js <models dir>           # the 34 too-big corpus models
node app/test/deck2inp-sweep.js                         # 171 decks against SWMM 5.2.4
python3 -I app/build.py                                 # assemble extran3-workbench.html
```

In the page: Run tab, pick an example, Score all seven. SWMM5 vs EXTRAN III tab, load an `.inp`. Card deck tab, Compare with SWMM5.

## Credits and licenses

- EXTRAN III: Larry A. Roesner, Robert P. Shubinski and John A. Aldrich, Camp Dresser & McKee, *Extended Transport Model (EXTRAN) User's Manual*, April 1981, for the U.S. EPA. The listing carries no license statement.
- EPA SWMM 5.2.4: U.S. Environmental Protection Agency, public domain.
- SWMM 4 example decks (January 2003): SWMMBobSWMM6/1729-SWMM5-Models-2030, january5_2003_examples. SWMM 4.4 source (2004): SWMMEnablement/SWMM_MD_Documents, WCH_2004_SWMM_Fortran_Code.
- SWMM 5 model corpus: SWMMEnablement/1729-SWMM5-Models.
- f2c and libf2c (AT&T Bell Laboratories, Lucent, Bellcore), under their permission notice; clang/LLVM and wasi-libc.
- Workbench code and text: Robert Dickinson. No license has been chosen yet.

## AI use

The workbench was built with Claude, Anthropic's AI model, in Claude Code sessions in October and November 2026, under the direction of Robert (Bob) Dickinson. He chose the project, supplied the manual, decided what to test, asked for a review of the finished app, the network map and larger arrays, and reviewed the results. Responsibility for the work is his.

What Claude did: cut the OCR text into its 15 program units and repaired it, logging each repair with a reason and a confidence; made the port edits; translated the Fortran with f2c and compiled the engines to WebAssembly; transcribed the seven example decks; wrote the SWMM 5 converter, the SWMM 4 translator, the deck-to-SWMM 5 writer, the network map, the array-enlarging program, the page, its tests, the essay and this file; ran every check.

How results were checked: mechanically, as listed under Checks. What no person has checked is listed under "What this does not show", item 8.

## Changes

- `1.6.0 (2026-11-11)`: enlarged-array builds (5,000 junctions and links) used automatically for decks and models over the 1981 sizes; 16 of the 34 formerly too-big corpus models run; flow-path finder and map adapted to large networks; this file.
- `1.5.0 (November 2026)`: network map on the Run tab and the SWMM5 vs EXTRAN III tab.
- `1.4.0 (November 2026)`: review fixes; Compare with SWMM5 (deck written as a SWMM 5 model); TRANSX run-length finding; essay Section 11.
- `Earlier (October 2026)`: transcription and port; as-printed and bugs-fixed engines; scoring against 1981; SWMM 5 converter and comparison; SWMM 4 deck import; Doc tab.
