---
title: The EXTRAN manual test models
type: concept
updated: 2026-11-16
sources: [S75, S180, S181, S182, S183, S185, S186]
tags: [extran, test-models, verification, swmm4, swmm5, swmm6, icm]
reviewed: no
---
The example networks of the EXTRAN manual are the oldest test models still run against every new SWMM engine. Most are one small network, Example 1, with one device added, so a difference in results points at the device.

**Where they come from and where they run**
- Bob's articles trace them to the 1981 EXTRAN 3 manual of CDM, which printed the input files and the output [S180](../sources/S180-li-extran1-extran2-test-files.md). A caption calls them "Seven Classic SWMM5 Hydraulics Test Files" [S180](../sources/S180-li-extran1-extran2-test-files.md).
- EPA's 2006 quality assurance report used ten of them, the Extran examples of the last SWMM 4.4 Users Manual (Roesner and others, 1992) [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md).
- They ship in the SWMM5 download and in EPA's GitHub test suite, and Bob says they are part of ICM SWMM network daily build validation and are used in InfoDrainage [S180](../sources/S180-li-extran1-extran2-test-files.md).
- The [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md) runs Examples 1 to 7 on six solvers [S186](../sources/S186-st-venant-rosetta-stone-app-md-v2-6-2.md).

**The examples** [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md), [S186](../sources/S186-st-venant-rosetta-stone-app-md-v2-6-2.md)

| Example | What it adds | What it tests |
|---|---|---|
| 1 | Seven circular conduits in two branches, two trapezoidal channels, free outfall; inflows of 45, 50 and 40 cfs | Surcharge in conduits 8040, 8060 and 1602 and flooding at node 80608 |
| 2 | Fixed outfall stage of 94.4 ft with a tide gate at node 10208 | Backwater from a fixed tailwater |
| 3 | Bottom (sump) orifice at junction 82309, 2.0 ft, coefficient 0.85 | Bottom orifices |
| 4 | Transverse weir at junction 82309, crest 3.0 ft, coefficient 0.80 | Weirs |
| 5 | Storage unit at 82309, 40.5 ft high, 800 sq ft, drained by a side orifice to a new node 82308 | Storage and side orifices |
| 6 | Off-line wet well 82310 and a Type 1 pump, 20 cfs at 1,200 ft3 | Pumping on wet-well volume |
| 7 | In-line Type 2 pump from 82309 to 15009 | Pumping on inlet depth |
| 8 | Several cross-section shapes, two irregular channels, a hot start | Shapes and natural channels |
| 9 | Variable-area storage with a side orifice, peak inflow 42.4 cfs (1.2 m3/s; conversion ours) | Storage geometry |
| 10 | Five Type 3 pumps lifting water up a 50-foot hill between two storage units | Pump switching by depth |

Examples 3 and 4 are described from the Rosetta Stone's conversion, because their pages in the QA report are not in the raw file (Q92) [S186](../sources/S186-st-venant-rosetta-stone-app-md-v2-6-2.md).

**What they have shown**
- 2006: SWMM 4.4h and SWMM 5.0.006 agree closely on the ten, with two differences of assumption (bottom orifices and Type 1 wet wells) and two places where the report doubts SWMM 4 (Example 7 pumping, Example 10 pump flows). See [SWMM 4 against SWMM 5: the 2006 quality assurance tests](swmm4-versus-swmm5-qa-2006.md) [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md).
- 2026: on Example 7, XROUTE's continuity error is -6.87 percent, the same figure as SWMM 4 in 2006; the cause traced is a pump drawing from a dry junction (Register 31). On Example 2, a fixed tailwater is booked as stored water at the end of a run but not at the start, which explains printed errors of -8.88 and -4.05 percent (Register 32) [S186](../sources/S186-st-venant-rosetta-stone-app-md-v2-6-2.md), [S185](../sources/S185-epa-swmm5-qa-report-dynamic-wave-2006.md).
- On Example 1, flooding lost from the network runs from 0 ft3 (ZROUTE as distributed) to 114,824 ft3 (SWMM 5.2.4 with the EXTRAN surcharge rule), depending on the solver and its surcharge rule [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**The AI summaries in the 2025 articles.** Each article carries a summary of the .inp "created with AI Help". Where checked, the storage and orifice of Example 5 agree with the QA report and the Rosetta Stone; the Example 6 summary calls the pump curve's volumes "ft head" [S181](../sources/S181-li-extran5-storage-side-orifice.md), [S182](../sources/S182-li-extran-example-6-type-1-pump.md).

**Related.** [EXTRAN](../entities/extran.md); [Pumps and pump curves](pumps-and-pump-curves.md); [Orifices](orifices.md).
