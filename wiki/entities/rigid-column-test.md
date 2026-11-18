---
title: "The Rigid Column Test (app)"
type: entity
updated: 2026-11-17
sources: [S29, S205, S209]
tags: [apps, swmm5, swmm6, surcharge, preissmann-slot, verification]
reviewed: no
---
Bob's app The Rigid Column Test: a full horizontal pipe between two fixed heads, started from rest, which has an exact answer, V(t) = V_inf tanh(t/tau), put to EPA SWMM 5.2.4 and OpenSWMM 6.0.0-alpha.4, varying the surcharge method, node storage and virtual junctions one at a time. The page works in SI units; the US figures here are conversions, ours or the summary's. Version and date 2026-09-30 [S209](../sources/S209-rigid-column-test-summary.md). Netlify address: https://rigid-column-test.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S209](../sources/S209-rigid-column-test-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S209](../sources/S209-rigid-column-test-summary.md)
- The pipe: 3,281 ft (1,000 m) long, 3.28 ft (1 m) across, n 0.013, horizontal, full at rest, from a reservoir at 16.4 ft (5 m) to a fixed outfall at 9.84 ft (3 m), a head difference of 6.56 ft (2 m). A chain version splits it into 20 pieces of 164 ft (50 m) with 19 junctions.
- Exact answer: V_inf = 4.48 ft/s (1.3652 m/s), Q_inf = 37.9 cfs (1.0722 m3/s), tau = 69.6 s; 76 % of V_inf at 70 s and 99 % at 184 s.
- Thirteen of fifteen runs share one number set with the single pipe: EXTRAN and every slot variant, both engines, both unit systems. EXTRAN in both engines lands on the exact curve within 1 %.
- Wave test, the outfall dropped from 16.4 to 9.84 ft (5 to 3 m) over one second: EXTRAN behaves as the incompressible limit; the SWMM 5.2.4 SLOT (Sjoberg 1 % slot, celerity 91.2 ft/s, 27.8 m/s) measured 87.6 to 93.5 ft/s (26.7 to 28.5 m/s) and carried +3.814 % on V_inf in both unit systems.
- The stock dynamic slot runs a factor of the square root of 2 (1.414) fast.
- The two virtual-junction runs fail on initial conditions, not on the slot.
- A junction's storage is the larger of the slot's contribution and MIN_SURFAREA.

**What it does not show.** One pipe geometry and its chain version; engine builds of 30 September 2026 only. [S209](../sources/S209-rigid-column-test-summary.md)

**Noted at ingest.** The exact values follow from Manning on a full 1 m pipe at a slope of 2/1000: V = (1/0.013) x 0.25^(2/3) x 0.002^0.5 = 1.365 m/s, and tau = L V_inf / (g Delta H) = 69.6 s; tanh(70/69.6) = 0.76 (our arithmetic). The conversions of 16.4 ft, 9.84 ft, 164 ft and the celerities are ours. The summary does not name the engine of the "stock dynamic slot"; DYNAMIC_SLOT is a surcharge method of OpenSWMM 6 [S29](../sources/S29-swmm6-rust-readme.md). The summary's version is the page's build date, as it has none of its own.

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).
