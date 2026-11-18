---
title: "S280: Run SWMM6 in Ten Minutes, summary written from the page (v2026-10-05)"
type: source
raw: raw/apps/run-swmm6-ten-minutes-v2026-10-05.md
kind: app-md
author: Robert Dickinson
published: 2026-10-05
ingested: 2026-11-18
tags: [documents, swmm6, openswmm, python, parity, tutorial]
drafted_by: Claude (Anthropic), from the published document
reviewed: no
---
**What it is.** A technical summary of the document Run SWMM6 in Ten Minutes, version 2026-10-05: a Claude Docs document that walks a reader through installing OpenSWMM 6 (pip openswmm 6.0.0a4.dev1), running a three-conduit model from Python, and comparing it with EPA SWMM 5.2.4. Raw file: [raw/apps/run-swmm6-ten-minutes-v2026-10-05.md](../../raw/apps/run-swmm6-ten-minutes-v2026-10-05.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the Claude Docs document https://claude.ai/artifact/Qye3EfPzBhQWBq3raowNTf, its one tab exported as HTML on 2026-11-17 (12,027 bytes, SHA-256 2d2a32aa0be99ce24da9de65b3a7ab453e360bc3a188702bb2745a0970c43e8b) and read in full. Nothing was run to write this file." The document carries no AI-use note; it is a Claude Docs document on Bob's account, written in a claude.ai session. The Netlify copy adds a foot note saying it was written with Claude at his direction.

**Claims worth keeping** (all copied from the file)
- Model: three 24 in conduits in series, 400 ft each, on a 0.125% slope; full-flow capacity 8.0 cfs; inflow peaking at 15 cfs; a plain SWMM5 file that also runs in EPA SWMM 5.2.4.
- SWMM6 alpha 4 matches EPA SWMM 5.2.4 bit for bit in node depths and link flows at all 360 reporting periods, but four summary-report lines differ: alpha 4 prints "No nodes were surcharged" (EPA: J1 1.08 h, J2 0.96 h, J3 0.69 h) while J1 reaches 5.36 ft over a 2 ft conduit.
- One added option moves the J1 peak: EXTRAN 5.36 ft, SLOT 5.31, DYNAMIC_SLOT 5.40, NODE_CONTINUITY SEMI_IMPLICIT 4.91; with the inflow held at 15 cfs both EXPLICIT and SEMI_IMPLICIT settle at 5.31 ft and 15.00 cfs.
- EPA SWMM 5.2.4 stops with ERROR 205 on NODE_CONTINUITY and on DYNAMIC_SLOT; SLOT runs there and gives 5.22 ft at J1.
- Build 6.0.0a4.dev1 has no s.nodes.get_depth or s.links.get_flow (the HydroCouple quickstart calls them); openswmm.legacy.engine.run_solver names its report after the input file and ignores its other two arguments; the bundled legacy solver reports 5.3.0.

**Limits it states.** One model of four nodes and three conduits; one build on Linux x86-64 with Python 3.12.3 on 5 October 2026; dynamic wave in closed conduits only; no field data; no verdict on which option is right.

**Checked at ingest.** Manning full flow for a 24 in pipe at S = 0.00125 and n = 0.013 is 8.0 cfs; 15 / 8.0 = 1.875, printed 1.87; the inflow triangle holds 0.5 x 15 cfs x 3 h = 81,000 ft3 = 1.860 ac-ft, the external inflow printed (our arithmetic). The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [Run SWMM6 in Ten Minutes (document)](../entities/run-swmm6-ten-minutes.md), [Apps summarized on 17 and 18 November 2026: SWMM6, benchmarks and ICM results](../concepts/apps-from-pages-swmm6-and-benchmarks.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md).
