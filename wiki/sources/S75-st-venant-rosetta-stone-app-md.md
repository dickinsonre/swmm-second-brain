---
title: "S75: St. Venant Solver Rosetta Stone, technical summary (app .md, v2.4.0)"
type: source
raw: raw/apps/st-venant-solver-rosetta-stone (1).md
kind: app-md
author: Robert Dickinson
published: 2026-11-13
ingested: 2026-11-15
tags: [hydraulics, extran, swmm4, swmm5, swmm6, dynamic-wave, findings, verification, apps]
reviewed: no
---
**What it is.** The technical summary that ships with the St. Venant Solver Rosetta Stone, version 2.4.0: six dynamic-wave solvers from SWMM 4.4H, EPA SWMM 5.2.4 and OpenSWMM 6, set side by side by source line and by 1,157 engine runs. Raw file: [raw/apps/st-venant-solver-rosetta-stone (1).md](../../raw/apps/st-venant-solver-rosetta-stone%20%281%29.md). Bob uploaded it on 14 November 2026.

**How it was written.** By Claude (Anthropic) in November 2026 under Bob's direction. The file says the source findings "are the AI's reading of the code at the lines cited" and that no person has rerun the engines, checked the thirty Register items against the source, or reviewed the SWMM 5 conversion of Example 1. Version 2.4.0 answers a written review of 2.3 that, "going by the link it carries", was produced with ChatGPT. "Neither the OpenSWMM authors nor EPA have seen these results."

**Engines.** SWMM 4.4H Extran block (XROUTE, YROUTE, ZROUTE), WCH_2004_SWMM44H commit 9dd9f6c, gfortran 13.3.0; 45 changed build copies of it; EPA SWMM 5.2.4 commit 07c371f and one build copy with a switch in `dwflow.c`; OpenSWMM 6.0.0-alpha.4, branch swmm6_rel, commit 0071c5f.

**Claims worth keeping**
- 1,157 runs: 290 on Example 1 of the EXTRAN manual, 847 on 52 other example decks, 20 on a single pipe.
- Example 1 at a 20-second step, water lost to flooding of 1,458,000 ft³ inflow: XROUTE 114,714 ft³, YROUTE 114,644, SWMM 5.2.4 EXTRAN 114,824, ZROUTE as distributed 0, ZROUTE with the slot freed 84,349, SWMM 5.2.4 SLOT 78,582, SWMM6 dynamic wave expanded 90,866, SWMM6 finite volume at 25 ft cells 80,673, SWMM6 finite volume at the default mesh 0.
- SWMM 5.2.4 and SWMM6 still carry XROUTE's momentum terms: `dq3 = 2 v (aMid - aOld) sigma` and `dq4 = dt v^2 (a2 - a1)/L sigma` at `dwflow.c:213-240`, against XROUTE.FOR:332-338.
- SWMM6 dynamic wave with SURCHARGE_METHOD EXTRAN matches EPA SWMM 5.2.4 on 30 of 30 values at six time steps.
- Register 20: the crown cap (NHEAD.FOR:95, 98, 348; `dwflow.c:125-129, 150`) gives a conduit surcharged at one end a partly full mid-section. Worth 17,497 ft³ in XROUTE and 20,560 in SWMM 5.2.4.
- Register 1 and 21 account for ZROUTE's missing flooding: 0, then 60,433, then 108,445 ft³ as the two are lifted, against XROUTE's 114,714.
- Eleven kept changes ("ZROUTE improved") cut the median absolute continuity error on 50 non-steep decks from 1.42 to 0.38 percent. Three steep-drop decks defeat every form of ZROUTE.
- Register 13: ZROUTE's work arrays have no SAVE; compiled without `-fno-automatic` it floods 1,477,890 ft³ of a 1,458,000 ft³ inflow.
- SLOT differs by design between EPA 5.2.4 (78,582 ft³) and OpenSWMM (89,559): in OpenSWMM the slot area does not convey flow.
- SWMM6 EXTRAN + SEMI_IMPLICIT floods 6,534 ft³ against 114,824; the cause was read, not isolated.
- Finite volume flooding against cell length: 0 at 4 cells per conduit and at 500 ft; 58,980 at 200 ft; 72,832 at 100 ft; 78,147 at 50 ft; 80,673 at 25 ft. Still rising at 25 ft.
- An independent mass balance agrees with each engine's printed continuity within 0.03 point in 55 of the 59 Example 1 runs that print one.
- Complexity index 51.5 (meter 1.9.1); the page carries no tests of its own, so test markers score 0.

**Limits it states.** "It is not a validation of any engine." No measured flood volume. The findings rest largely on one small network near capacity; Register 20 on one conduit, 1602. No changed build copy is claimed to be a safe fix. The 53-deck extension is SWMM 4.4H only. Nothing has been reported to EPA or to the OpenSWMM authors.

**Checked at ingest.** 973 + 184 = 1,157; 290 + 847 + 20 = 1,157; 114,714 - 84,349 = 30,365 = 17,497 + 12,868. The limits list numbers two items 23 and two items 24. The file gives EPA SWMM 5.2.4 as commit 07c371f; other sources give tag v5.2.4 as 7952ca8. A lookup in the USEPA repository on 15 November 2026 found 07c371f to be the head of its develop branch and the tag to be 7952ca8 (Q50).

**Feeds:** [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md), [EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE](../concepts/extran-solvers-xroute-yroute-zroute.md), [The crown cap at mid-pipe](../concepts/crown-cap-at-mid-pipe.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [EXTRAN](../entities/extran.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Continuity is not validation](../concepts/continuity-is-not-validation.md), [The SWMM findings register](../concepts/findings-register.md), [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md).
