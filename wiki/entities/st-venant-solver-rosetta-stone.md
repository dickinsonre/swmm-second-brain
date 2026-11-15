---
title: St. Venant Solver Rosetta Stone (app)
type: entity
updated: 2026-11-15
sources: [S20, S75]
tags: [apps, hydraulics, extran, swmm4, swmm5, swmm6, dynamic-wave, findings]
reviewed: no
---
Bob's app that sets six dynamic-wave solvers side by side, by source line and by engine run: XROUTE, YROUTE and ZROUTE from SWMM 4.4H, the one solver of EPA SWMM 5.2.4, and the dynamic wave and finite volume solvers of OpenSWMM 6. Version 2.4.0, 13 November 2026 [S75](../sources/S75-st-venant-rosetta-stone-app-md.md). It is not the [SWMM and ICM St. Venant comparison (app)](swmm-icm-st-venant-app.md) of [S20](../sources/S20-li-edition-54-two-solvers.md), which compares SWMM 5 with ICM and runs no engine.

**What it holds** [S75](../sources/S75-st-venant-rosetta-stone-app-md.md)
- The momentum and surcharge lines of each solver, with file and line numbers.
- The results of 1,157 engine runs. Nothing is simulated in the browser except a one-pipe calculator.
- A register of thirty findings, each marked measured in a run or read in the source.

**The four questions it answers** [S75](../sources/S75-st-venant-rosetta-stone-app-md.md)
1. How do the three SWMM 4 solvers differ, and what did SWMM 5 keep? See [EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE](../concepts/extran-solvers-xroute-yroute-zroute.md).
2. What do the two OpenSWMM 6 solvers do on the same network? See [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).
3. Are there more bugs in YROUTE and ZROUTE?
4. Why is ZROUTE different? See [The crown cap at mid-pipe](../concepts/crown-cap-at-mid-pipe.md).

**The runs** [S75](../sources/S75-st-venant-rosetta-stone-app-md.md)

| Group | Runs |
|---|---|
| ZROUTE deep dive: 16 builds at six time steps, 16 configurations on 53 decks, 29 supporting | 973 |
| Sweep of 9 configurations at 6 time steps | 54 |
| Why-ZROUTE one-change build copies | 48 |
| Bug-hunt build copies of SWMM 4.4H | 21 |
| All others (10-second output, SWMM6 parity, option sets, meshes, single pipe) | 61 |
| Total | 1,157 |

To make them, Claude built 45 changed copies of SWMM 4.4H and one of SWMM 5.2.4, each with one change or a named combination. A reproduction bundle holds the scripts, decks and a manifest of 1,365 retained raw reports [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**Version history** [S75](../sources/S75-st-venant-rosetta-stone-app-md.md)

| Version | Date | What |
|---|---|---|
| 1.0 | 2026 | A React component with a made-up transient |
| 2.0.0 | 2026-11-12 | The invented transient replaced by 48 runs of compiled engines |
| 2.1.0 | 2026-11-12 | The two OpenSWMM 6 solvers; runs 48 to 136 |
| 2.2.0 | 2026-11-13 | Why ZROUTE differs; runs 136 to 184 |
| 2.3.0 | 2026-11-13 | ZROUTE deep dive; runs 184 to 1,157 |
| 2.4.0 | 2026-11-13 | Corrections after an outside review; no new runs |

Version 2.0 withdrew two claims of version 1: that ZROUTE has no surcharge treatment, and that YROUTE's denominator damps the flow [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**What it is not.** "It is not a validation of any engine." There is no measured flood volume, and 290 of the runs are one small network near capacity. No person has checked the thirty register items against the source or rerun the engines. Nothing has been reported to EPA or to the OpenSWMM authors [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**Complexity index.** 51.5 on the [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md) [S75](../sources/S75-st-venant-rosetta-stone-app-md.md).

**Open.** Its thirty register items have no IDs in [The SWMM findings register](../concepts/findings-register.md) (Q47). Its "EPA SWMM 5.2.4" is commit 07c371f, which is the head of the USEPA repository's develop branch and not the v5.2.4 tag (Q50). See [Open questions](../open-questions.md).
