---
name: Run SWMM6 in Ten Minutes
file: run-swmm6-ten-minutes.html
version: "2026-10-05"
date: 2026-10-05
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Qye3EfPzBhQWBq3raowNTf", repo: none named in the document}
engines:
  - {name: OpenSWMM, version: 6.0.0a4.dev1 (pip openswmm; the .rpt header reads 6.0.0-alpha.4), note: "run by the reader; the document's numbers come from Linux x86-64, Python 3.12.3, 5 Oct 2026"}
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4, note: "compiled from the USEPA repository for the comparison"}
  - {name: HydroCouple legacy solver, version: 5.3.0, note: "bundled in the openswmm package; close to EPA 5.2.4, not the same build"}
units: US customary (cfs, ft, acre-ft)
ai_use: "This summary was written by Claude (Anthropic) from the published document. The document carries no AI-use note; it is a Claude Docs document on Robert Dickinson's account. See AI use."
written_from: "the Claude Docs document https://claude.ai/artifact/Qye3EfPzBhQWBq3raowNTf, its one tab exported as HTML on 2026-11-17 (12,027 bytes, SHA-256 2d2a32aa0be99ce24da9de65b3a7ab453e360bc3a188702bb2745a0970c43e8b) and read in full. Nothing was run to write this file."
---

# Run SWMM6 in Ten Minutes: install OpenSWMM 6 with pip, run a three-pipe model, check it against EPA SWMM 5.2.4

## In three points
- **What:** A ten-minute walk-through dated 5 October 2026: install the openswmm package (6.0.0a4.dev1) with one pip command, save a three-conduit model printed on the page, run it from a short Python script and check the report against the page's numbers.
- **So what:** On this model SWMM6 alpha 4 matches EPA SWMM 5.2.4 bit for bit in node depths and link flows at all 360 reporting periods, yet four summary-report lines differ: alpha 4 says "No nodes were surcharged" while J1 reaches 5.36 ft over a 2 ft conduit. One added option, NODE_CONTINUITY SEMI_IMPLICIT, moves the J1 peak from 5.36 to 4.91 ft.
- **Now what:** Run a network you trust next, compare it with your SWMM5 results and report disagreements to the HydroCouple issue tracker. In this alpha, take the time series from SWMM6 and the surcharge tables from SWMM5. One model, one build, one machine.

This summary was written after the fact. The document ships no technical summary of its own and gives no version number; the version above is its date. The file name is ours. Every number below is copied from the document. Nothing was run to write this file.

## What it does

A Claude Docs document, not an app. It walks a reader through ten minutes: install (minute 1), the model (2 to 3), run it (4 to 5), what you should see (6), the same file in SWMM5 (7 to 8), one SWMM6 option (9 to 10), then where to go next and what the page does not show. The engine is Caleb Buahin's Open-Source SWMM 6.0 (SWMM2D), developed at HydroCouple.

## The test model (as printed in the document)

- tenmin.inp: three 24 in circular conduits in series, 400 ft each, n = 0.013, on a 0.125% slope; junctions J1, J2, J3 at inverts 100.0, 99.5 and 99.0 ft, 10 ft deep; a free outfall at 98.5 ft.
- DYNWAVE, 5 s routing step, fixed step, 1-minute reports, 6 hours; INERTIAL_DAMPING PARTIAL, NORMAL_FLOW_LIMITED BOTH, no ponding.
- Inflow at J1: 0 cfs at 0:00, 15 cfs at 1:00, 0 at 3:00. Manning full-flow capacity 8.0 cfs, so the line surcharges and nothing floods.
- A plain SWMM5 file with no SWMM6-only lines.

## Results the document reports

| Report item | Value |
|---|---|
| External inflow, external outflow (acre-ft) | 1.860, 1.861 |
| Flow routing continuity error (%) | -0.059 |
| Maximum depth at J1, J2, J3 (ft) | 5.36, 4.08, 2.81 |
| Maximum flow in C1, C2, C3 (cfs) | 15.00, 15.01, 15.00 |
| Max/Full Flow in C1 | 1.87 |
| Average iterations per step | 2.06 |
| Steps not converging (%) | 0.19 |

Where EPA SWMM 5.2.4 and SWMM6 alpha 4 differ on the same file (time series identical):

| Report item | EPA SWMM 5.2.4 | SWMM6 alpha 4 |
|---|---|---|
| Node Surcharge Summary | J1 1.08 h, J2 0.96 h, J3 0.69 h | "No nodes were surcharged" |
| Conduit Surcharge Summary, hours full at both ends | C1 0.96, C2 0.69, C3 0.01 | C1 0.00, C2 0.00, C3 missing |
| J1 reported max depth (ft) | 5.34 | 5.36 |
| J1 time of max depth | 01:00 | 00:59 |

One added line in [OPTIONS], four runs in SWMM6 alpha 4:

| Line added | J1 peak depth (ft) | C3 peak flow (cfs) | Continuity error (%) | Steps not converging (%) |
|---|---|---|---|---|
| None (EXTRAN, EXPLICIT) | 5.36 | 15.00 | -0.059 | 0.19 |
| SURCHARGE_METHOD SLOT | 5.31 | 14.95 | -0.003 | 0.00 |
| SURCHARGE_METHOD DYNAMIC_SLOT | 5.40 | 15.05 | -0.003 | 0.00 |
| NODE_CONTINUITY SEMI_IMPLICIT | 4.91 | 14.41 | -0.001 | 0.00 |

- Control run: with the inflow held at 15 cfs for three hours, EXPLICIT and SEMI_IMPLICIT both settle at 5.31 ft and 15.00 cfs. They agree at steady state and differ on the sharp peak.
- EPA SWMM 5.2.4 stops with ERROR 205 (invalid keyword) on NODE_CONTINUITY and on DYNAMIC_SLOT. SLOT runs in 5.2.4 and gives 5.22 ft at J1 against 5.31 ft in SWMM6. The bit-for-bit match holds for the default EXTRAN method only.

## Gotchas the document records

- The HydroCouple quickstart calls s.nodes.get_depth("J1") and s.links.get_flow("C1"); build 6.0.0a4.dev1 has neither and raises AttributeError. The document reads the NumPy arrays s.nodes.depths and s.links.flows instead.
- openswmm.legacy.engine.run_solver names its report after the input file and ignores the other two arguments, so the document copies tenmin.inp to tenmin5.inp first.

## Checks

- Arithmetic we checked (our arithmetic, not the document's): Manning full flow for a 24 in pipe at S = 0.00125, n = 0.013 is (1.486 / 0.013) x 3.1416 x 0.5^(2/3) x 0.00125^0.5 = 8.0 cfs; 15 / 8.0 = 1.875, reported as 1.87; the inflow triangle holds 0.5 x 15 cfs x 3 h = 81,000 ft3 = 1.860 acre-ft, the external inflow reported.
- The document states the platform of every number (Linux x86-64, Python 3.12.3, 5 October 2026) and that the 5.2.4 reference was compiled from the v5.2.4 tag.

## What this does not show

As the document lists it: one model of four nodes and three conduits; one build on one machine (Windows and macOS untested); dynamic wave routing in closed conduits only (no hydrology, water quality, 2D surface flow, finite volume solver or GUI); no field data; no verdict on which option's answer is right.

## How to reproduce

The document carries everything: the pip command (pin openswmm==6.0.0a4.dev1 to match), the full tenmin.inp, run6.py, and the legacy-solver snippet.

## Credits and licenses

Caleb Buahin's Open-Source SWMM 6.0 (SWMM2D) at HydroCouple; EPA SWMM 5.2.4 from the USEPA repository. The document links HydroCouple's install guide, quickstart, migration guide, testing article, LID storage node tutorial and the openswmm.engine issue tracker. No license is stated for the document.

## AI use

The document carries no AI-use note. It is a Claude Docs document on Robert Dickinson's account, written in a claude.ai session. The Netlify copy adds a paragraph at the foot saying it was written with Claude at his direction and that the copy was exported from the Docs document on 18 November 2026. The document does not say who ran the engines. This summary was written by Claude on 18 November 2026 from the exported document.

## Changes

- 2026-10-05: the version read (the document's date; it carries no version number).
