---
title: "S186: St. Venant Solver Rosetta Stone, technical summary (app .md, v2.6.2)"
type: source
raw: raw/apps/st-venant-solver-rosetta-stone-v2.6.2.md
kind: app-md
author: Robert Dickinson
published: 2026-11-14
ingested: 2026-11-16
coverage: partial
read: [front matter and summaries, What it does, How it computes, Inputs and outputs, "Checks (the opening count and Examples 2 to 7 with Register 23 and 31 to 33)", What this does not show, Complexity, Changes]
tags: [hydraulics, extran, swmm4, swmm5, swmm6, dynamic-wave, pumps, findings, verification, apps]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: no
---
**What it is.** The technical summary of the St. Venant Solver Rosetta Stone, version 2.6.2, which supersedes version 2.4.0 ([S75](S75-st-venant-rosetta-stone-app-md.md)). It adds the EXTRAN manual's Examples 2 to 7 on all six solvers and three findings about pumps and tailwater. Raw file: [raw/apps/st-venant-solver-rosetta-stone-v2.6.2.md](../../raw/apps/st-venant-solver-rosetta-stone-v2.6.2.md), about 16,000 words.

**How it was written.** By Claude (Anthropic) under Bob's direction, from the build's own runs. "All mechanical. No human review yet." Versions 2.4 to 2.6.2 each answer an outside review. Over 15,000 words, so it is read in parts: the Example 1 checks of the 2.4.0 page are not re-read here, and S75 stays the source for them.

**Coverage: partial.** Read: the parts listed in `read:`. Not yet read: the Example 1 sweeps, the ZROUTE deep dive and the 53-deck tables of the Checks section, and How to reproduce.

**Claims worth keeping**
- 1,342 engine runs: 321 on Example 1, 899 on 52 other example decks on SWMM 4.4H builds, 80 on Examples 2 to 7 in versions 2.6 and 2.6.2, 11 on two decks made from Example 3, 20 on a single pipe and 11 on a pump test deck. A register of thirty-three findings, 28 measured and 5 read. 50 changed build copies: 48 of SWMM 4.4H, 1 of SWMM 5.2.4 and 1 of OpenSWMM 6.
- Examples 2 to 7, each Example 1 with one device, were run on ten configurations at a 20-second step. SWMM 4.4H ran the manual's decks; for SWMM 5.2.4 and SWMM 6 each device was written by hand into the Example 1 input. The Example 6 wet well (a 100 sq ft storage node with its floor 12 ft below the pipe) is "a choice made here, not in the deck".
- Example 2, tide gate: flooding 113,565 ft3 in XROUTE, 114,868 in SWMM 5.2.4 EXTRAN, 78,582 in SWMM 5.2.4 SLOT and 0 in ZROUTE; printed continuity -8.88 percent in XROUTE and -4.05 in SWMM 5.2.4.
- Example 5, storage and side orifice: flooding 219,550 ft3 in XROUTE, 203,425 in SWMM 5.2.4 EXTRAN, 176,984 in SLOT and 108,750 in ZROUTE.
- Example 6, Register 23: ZROUTE pumps 66.2 cfs through a station whose largest rate is 20 cfs and holds 82309 at 115.15 ft, where XROUTE holds 129.40. The other solvers pump 20 cfs.
- Example 7, Register 31: XROUTE and YROUTE pump from a dry junction. Continuity -6.87 and -5.28 percent as in the manual; 0.10 and 0.13 with the first pump rate set to zero. After 4:22 XROUTE pumps 5 cfs on 330 of 654 steps, 320 of them with 82309 printed at its invert. 19,538 ft3 of XROUTE's surplus is not placed. SWMM 5.2.4 EXTRAN prints 0.05 percent.
- Example 2, Register 32: a fixed outfall stage is booked as stored water at the end of the run and not at the start. With the stage lowered to the outfall invert, XROUTE prints 0.06 percent and SWMM 5.2.4 0.01. SWMM 4.4H's printed total outflow of 1,445,000 ft3 includes 113,565 ft3 of flooding.
- Register 33: OpenSWMM 6 finite volume pumps 39.00 cfs on Example 7 through a curve that ends at 20, and 28.87 cfs on a one-junction test deck where the curve gives 5.00; SWMM 6 dynamic wave with DYNAMIC_SLOT alone pumps 30.00 cfs on the test deck with 11.84 percent continuity error. The cause is `q = std::max(nodes.inflow[un1], 0.0);` at HydStructures.cpp:539. A copy with `q = std::min(q, std::max(nodes.inflow[un1], 0.0));` pumps 5.00 on the test deck and 10.00 on Example 7, where finite volume at 25 ft cells then floods 5,881 ft3 instead of none.
- On the pump test deck the stock finite volume run holds 0.05 ft of water at the junction while pumping 28.8 cfs; SWMM 5.2.4 holds 7.40 ft and pumps 5.00.
- EPA SWMM 5.2.4 has the same dry-node rule, `if ( y <= 0.0 ) return Node[j].inflow;` in getModPumpFlow, dynwave.c, and pumped at the curve on both decks.
- SWMM 5.2.4 and SWMM 6 dynamic wave iterate up to MaxTrials = 8 with OMEGA = 0.5 (dynwave.c:61, 66; Constants.hpp:124).
- Complexity index 53.6 (SWMM App Complexity Meter v1.9.1, baseline HC-2026-11-10-h).
- Limits it adds: no person has reviewed any of the thirty-three Register items or rerun the engines; Examples 2 to 7 ran at one time step only; no person has checked the hand conversions.

**Checked at ingest.** 24 + 67 + 94 + 973 + 184 = 1,342 and 321 + 899 + 80 + 11 + 20 + 11 = 1,342; 48 + 1 + 1 = 50; 28 + 5 = 33; 1,445,000 - 113,565 = 1,331,435. XROUTE's -6.87 percent on Example 7 is SWMM 4's figure in the 2006 QA report [S185](S185-epa-swmm5-qa-report-dynamic-wave-2006.md). That report also says both SWMM 4 and SWMM 5 limit a pump to its inflow when the curve would pump the node dry; Register 31 measures XROUTE pumping 5 cfs from a dry junction (Q95). The report's SWMM 5 is version 5.0.006 with four trials; this file's 5.2.4 has eight.

**Feeds:** [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md), [The EXTRAN manual test models](../concepts/extran-manual-test-models.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE](../concepts/extran-solvers-xroute-yroute-zroute.md), [Open questions](../open-questions.md).
