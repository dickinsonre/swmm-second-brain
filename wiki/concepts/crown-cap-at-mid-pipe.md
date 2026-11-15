---
title: The crown cap at mid-pipe
type: concept
updated: 2026-11-15
sources: [S75]
tags: [hydraulics, extran, swmm4, swmm5, swmm6, surcharge, findings]
reviewed: 2026-11-15
---
In the EXTRAN line of solvers, the depth at each end of a conduit is capped at the pipe's full depth before the mid-length section is worked out. A conduit surcharged at one end only is therefore given a partly full section at mid-length, and that section's area and hydraulic radius are the ones the momentum equation uses [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). The finding is Register item 20 of the [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md), marked measured.

**Where the cap is** [S75](../sources/S75-st-venant-rosetta-stone-app-md.md)

| Program | Lines | What they do |
|---|---|---|
| SWMM 4.4H | NHEAD.FOR:95, 98, then 348 | Cap each end depth at DEEP + 2 FUDGE, then interpolate the mid depth |
| EPA SWMM 5.2.4 | `dwflow.c:125-129`, then 150 | `y1 = MIN(y1, yFull)`, `y2 = MIN(y2, yFull)` when the surcharge method is not SLOT, then `yMid = 0.5 (y1 + y2)` |
| OpenSWMM 6 | DynamicWave.cpp:1937-1941 | The same cap; read, not changed |

**One conduit, measured.** Conduit 1602 of EXTRAN Example 1 (5 ft, 5,000 ft long, n 0.034) at 2:00, from instrumented builds [S75](../sources/S75-st-venant-rosetta-stone-app-md.md):

| | End depths, ft | Mid depth, ft | Flow, cfs |
|---|---|---|---|
| XROUTE (capped) | 5.000 and 2.969 | 3.985 | 72.03 |
| ZROUTE, slot freed (uncapped) | 21.186 and 3.020 | 12.103 | 74.38 |

The head at the upstream junction is 133.63 ft and the crown 117.3 ft; a straight grade line stands 7.1 ft above the crown at mid-length [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**What it is worth.** With the mid section taken from the uncapped heads, flooding on Example 1 falls by 17,497 ft³ in XROUTE (114,714 to 97,217) and by 20,560 ft³ in SWMM 5.2.4 with EXTRAN surcharge (114,824 to 94,264) [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**How it explains ZROUTE's missing flooding.** ZROUTE as distributed reports 0 ft³ of flooding where XROUTE reports 114,714. Two things combine [S75](../sources/S75-st-venant-rosetta-stone-app-md.md):
1. The same cap holds ZROUTE's Preissmann slot at its crown width, 0.3919 of the diameter for a circular pipe (Register 1).
2. ZROUTE credits the capped mid-section's free surface to the surcharged junction as storage (Register 21).

| Build, one change at a time | Flooding, ft³ |
|---|---|
| ZROUTE as distributed | 0 |
| Crown slot narrowed from 0.3919 D to 0.005 D | 60,433 |
| Plus the mid-section surface width at the uncapped depth | 108,445 |
| XROUTE | 114,714 |

**The slot-freed ZROUTE** lifts the cap when the slot is on, by prefixing NHEAD.FOR lines 95 and 98 with `IF(JSLOT.EQ.0)`. It floods 84,349 ft³. Of the 30,365 ft³ between it and XROUTE, 17,497 is the mid-pipe section, measured; the remaining 12,868 is split by arithmetic, not by a run [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**"ZROUTE improved."** Eleven further changes, tested alone and together, bring Example 1's continuity error to between +0.10 and +0.16 percent at six time steps, and the median over 50 non-steep decks from 1.42 to 0.38 percent. Four of the eleven changed nothing on any deck and rest on reading. Three steep-drop decks defeat it [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**What is not shown** [S75](../sources/S75-st-venant-rosetta-stone-app-md.md)
- Which mid-pipe description is right. "A straight grade line favors the full section; nothing was compared with a measurement."
- More than one conduit in one network.
- That any changed build is a safe fix.
- Nothing has been reported to EPA or to the OpenSWMM authors, and no person has checked the reading of the code.

See [EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE](extran-solvers-xroute-yroute-zroute.md), [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md), [Dynamic wave routing](dynamic-wave-routing.md).
