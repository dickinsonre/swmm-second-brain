---
title: "Run SWMM6 in Ten Minutes (document)"
type: entity
updated: 2026-11-18
sources: [S280]
tags: [documents, swmm6, openswmm, python, parity, tutorial]
reviewed: no
---
Bob's document Run SWMM6 in Ten Minutes: a Claude Docs document that walks a reader through installing OpenSWMM 6 (pip openswmm 6.0.0a4.dev1), running a three-conduit model from Python, and comparing it with EPA SWMM 5.2.4. Version and date 2026-10-05 [S280](../sources/S280-run-swmm6-ten-minutes-summary.md). Its `links:` line names no live Netlify address [S280](../sources/S280-run-swmm6-ten-minutes-summary.md).

**A caution about its source.** The page ships no technical summary. [S280](../sources/S280-run-swmm6-ten-minutes-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q111).

**What the summary says** [S280](../sources/S280-run-swmm6-ten-minutes-summary.md)
- Model: three 24 in conduits in series, 400 ft each, on a 0.125% slope; full-flow capacity 8.0 cfs; inflow peaking at 15 cfs; a plain SWMM5 file that also runs in EPA SWMM 5.2.4.
- SWMM6 alpha 4 matches EPA SWMM 5.2.4 bit for bit in node depths and link flows at all 360 reporting periods, but four summary-report lines differ: alpha 4 prints "No nodes were surcharged" (EPA: J1 1.08 h, J2 0.96 h, J3 0.69 h) while J1 reaches 5.36 ft over a 2 ft conduit.
- One added option moves the J1 peak: EXTRAN 5.36 ft, SLOT 5.31, DYNAMIC_SLOT 5.40, NODE_CONTINUITY SEMI_IMPLICIT 4.91; with the inflow held at 15 cfs both EXPLICIT and SEMI_IMPLICIT settle at 5.31 ft and 15.00 cfs.
- EPA SWMM 5.2.4 stops with ERROR 205 on NODE_CONTINUITY and on DYNAMIC_SLOT; SLOT runs there and gives 5.22 ft at J1.
- Build 6.0.0a4.dev1 has no s.nodes.get_depth or s.links.get_flow (the HydroCouple quickstart calls them); openswmm.legacy.engine.run_solver names its report after the input file and ignores its other two arguments; the bundled legacy solver reports 5.3.0.

**What it does not show.** One model of four nodes and three conduits; one build on Linux x86-64 with Python 3.12.3 on 5 October 2026; dynamic wave in closed conduits only; no field data; no verdict on which option is right. [S280](../sources/S280-run-swmm6-ten-minutes-summary.md)

**Noted at ingest.** Manning full flow for a 24 in pipe at S = 0.00125 and n = 0.013 is 8.0 cfs; 15 / 8.0 = 1.875, printed 1.87; the inflow triangle holds 0.5 x 15 cfs x 3 h = 81,000 ft3 = 1.860 ac-ft, the external inflow printed (our arithmetic).

See [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md).
