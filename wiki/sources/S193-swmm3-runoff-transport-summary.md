---
title: "S193: SWMM 3 Runoff & Transport, summary written from the page (version of 2026-10-23)"
type: source
raw: raw/apps/swmm3-runoff-engine-v2026-10-23.md
kind: app-md
author: Robert Dickinson
published: 2026-10-23
ingested: 2026-11-17
tags: [apps, swmm3, swmm4, history, runoff, transport, wasm, findings]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM 3 Runoff & Transport: the Runoff and Transport blocks of SWMM Version III (the November 1981 release) rebuilt in C and run in the browser as WebAssembly, from 1981 card formats. Raw file: [raw/apps/swmm3-runoff-engine-v2026-10-23.md](../../raw/apps/swmm3-runoff-engine-v2026-10-23.md).

**How it was written. A summary written from the page.** The page ships no technical summary and no version number. Claude (Anthropic) wrote this file on 16 November 2026, at Bob's request, from the published artifact (version 1792729841-e249) and its About and Doc tabs. No deck was run. The version is the publish date. Bob has not read it (Q99). The page says the app was built with Claude on 22 and 23 October 2026 under Bob's direction; Claude decided which Fortran lines are Version 4 and which Version III, and wrote the five C files by hand.

**Claims worth keeping** (all copied from the page)
- The page says Version III was distributed on magnetic tape, about 25,000 Fortran statements, and no listing of it is known to survive.
- The engine was made by subtraction from the SWMM 4.4 Fortran (Oregon State University and CDM, July 2003 / 2004): each Version 4 addition was identified from the 1988 manual's list of changes and the dated comments and removed, and the Version III input, output and limits were restored from the 1981 manual's Tables 4-28 and 6-6, their footnotes and Figure 2-3. Every decision is an "R3 note" in the C source.
- Where sources disagree on numerics, the 1981 manual wins. The 1988 manual says Version 4 wrapped the Runoff Newton-Raphson step in Richardson extrapolation "so that Subroutine Gutter no longer has convergence problems"; this engine keeps the single step of 1981.
- Runoff: Horton and Green-Ampt infiltration, the three-subarea nonlinear reservoir, channels and pipes with surcharge storage, snowmelt, buildup and washoff of up to ten constituents on five land uses, continuous simulation from NWS Card Deck 488. Transport: thirteen cross-sections plus two user shapes, manholes, lift stations, dividers, two storage units, backwater elements, the kinematic-wave finite difference with Newton iteration, FILTH and INFIL, complete-mixing pollutant routing for up to four constituents.
- Deliberate differences: REAL is IEEE single precision (1981 ran on an Amdahl 470 in IBM hexadecimal floating point); continuity sums are double. Not here: Storage/Treatment, Extran and Executive Blocks.
- Defects kept as shipped: SNOW-1 (WSHED.FOR 324, 338, 352, 369), with partial snow cover (1 - ASC) of the melt is lost, 16 % of the initial pack on the snow1 deck; a switch applies the correction. TRANS-1 (TRANS.FOR 87-138, INITAL.FOR 207-214), the continuity sum omits a lift station's initial wet-well volume, +1,000 cu ft, 2.9 %, on the lift null test. TRANS-2 (TRANS.FOR 720-728), flow sent to an element that does not exist is dropped uncounted, -92 % on example TRANS23.
- Two builds, same bytes: the same C built by wasi-sdk clang to wasm32 and by gcc natively gives byte-identical printouts and interface files on eleven cases. At first they did not: the two host libraries disagree at the last bit of sinf, cosf, tanf, asinf, acosf, atanf, log10f, exp and pow, so both builds now compile the same musl 1.2.6 routines.
- Continuity, Runoff (surface / channel): test deck -0.36 % / 0.009 %; Lancaster -0.46 % / 0.15 %; Example 1 -0.05 % / 0.01 %. Transport: Lancaster 2.47 % flow (TRANS-1 about 1 %), lift station 2.87 % (= TRANS-1), one-pipe null test 0.18 %.
- Census: all 47 Transport example decks of the January 2003 SWMM 4 set convert and run to the end (TRANS22, a degenerate 0.01 cfs case, -135 %; TRANS23 -92 % by TRANS-2; TRANS37, a natural channel approximated as a trapezoid, -13 %).

**Limits it states.** No 1981 output survives to score against. No person other than Claude has reviewed the subtraction decisions; the page says they are written out so that someone can.

**Checked at ingest.** "No listing known to survive" sits beside the EXTRAN III Workbench, which runs EXTRAN III, a block of Version III, from the listing printed in its April 1981 manual [S74](S74-extran3-workbench-app-md.md) (Q102). The page credits "Huber and Dickinson (1988), SWMM Version 4 User's Manual, EPA/600/3-88/001a". EPA's 2006 report dates the same number October 1992 [S185](S185-epa-swmm5-qa-report-dynamic-wave-2006.md); see Q94. The page names the 1981 manual's authors as Huber, Heaney, Nix, Dickinson and Polmann (University of Florida, EPA-600/2-84-109a); the November 1981 release date is the page's.

**Feeds:** [SWMM 3 Runoff & Transport (app)](../entities/swmm3-runoff-transport-app.md), [SWMM version history](../concepts/swmm-version-history.md), [Block architecture and interface files](../concepts/block-architecture.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md), [The SWMM findings register](../concepts/findings-register.md), [Open questions](../open-questions.md).
