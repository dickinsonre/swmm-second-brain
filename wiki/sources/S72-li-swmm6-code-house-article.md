---
title: "S72: SWMM6 Code House, Every Line of OpenSWMM 6 on a Wall (LinkedIn, 2026-11-04)"
type: source
raw: raw/linkedin/2026-11-04-swmm6-code-house-every-line-openswmm-6-wall-robert-dickinson-ubs3e.md
kind: linkedin-article
author: Robert Dickinson
published: 2026-11-04
ingested: 2026-11-14
tags: [apps, swmm6, swmm5, source-code, openswmm, findings]
drafted_by: Claude (Anthropic), first draft, in Claude Code; Bob reviews the results
reviewed: 2026-11-15
---
**What it is.** Bob's article on the SWMM6 Code House at version 1.1.0, with an appendix telling how both houses were built. Raw file: [raw/linkedin/2026-11-04-swmm6-code-house-every-line-openswmm-6-wall-robert-dickinson-ubs3e.md](../../raw/linkedin/2026-11-04-swmm6-code-house-every-line-openswmm-6-wall-robert-dickinson-ubs3e.md).

**How it was written.** It says so: Claude Code (Anthropic, model claude-opus-5-5) wrote the app, the tests and "the first draft of this article"; Bob chose the project, set the standards and reviews the results, and "has not checked every sentence or formula". Every claim below is an AI-written passage unless marked as Bob's account.

**Claims worth keeping**
- OpenSWMM 6 is C++20, 351,187 lines in 675 files, "about seven times the SWMM 5.2.4 solver".
- Nine floors: Weather Loft, Land Floor, Front of the House, Public Counter (the C API), Pipe Gallery, Water Lab, Surface Wing (2D), Underground, Cellar. The largest room, The Great Hall, has 13,652 lines.
- Where the data went: SWMM 5 keeps a struct per node and global arrays, so one run per process. OpenSWMM moves a run's state into one `SimulationContext`, and a node becomes an index into arrays (`ctx.nodes.depth[i]`).
- Output is written by a separate IO thread from a bounded queue, eight items by default.
- Four routing models; the new one, FV, is an explicit finite volume method with HLL or HLLC fluxes.
- New in OpenSWMM, by room: 2D overland flow, manhole exchange, soil columns and groundwater transport, a Richards column for LID soil, LARD and ARD water quality chosen by `QUALITY_SOLVER`, heat, plugins with an SDK.
- "Comments in its source name 61 of the 76 SWMM 5 files."
- 20 reading notes, each "a source-reading hypothesis" and not a bug until it has a model, an engine run and a repeatable difference. Four it names first: `NetworkMeshBuilder.cpp` line 456 (the finite volume path uses the power law for every culvert code: 25.7 cfs against 183 cfs in a JavaScript copy); `NodeCoupling.cpp` line 372 (exchange area doubles over the 5 cm above the crown); `InputReader.cpp` line 265 (a section header with a legacy abbreviation such as `[JUNC]` is dropped with no warning); `DynamicWave.cpp` line 4419 (SEMI_IMPLICIT: continuity -3.29 percent against +0.07 percent for EXPLICIT on a toy chain). Three of the 20 are the same in SWMM 5.2.4.
- A possible defect in EPA's `culvert.c`: for a Form 1 culvert the code runs the Ridder root finder and returns the flow from its last trial, a midpoint, not from the root. Flow can jump by up to 2.29 cfs across 0.005 ft of head. Of 228 runs, 221 sit on the jagged curve within 0.01 %. The fix "exists only as a JavaScript copy and has not been compiled or tested on a real build".
- Bob's account of the build: on 2 November 2026 he asked Claude for a 3D house of the SWMM5 C code; he steered it with nine ChatGPT reviews, attaching each and typing "add"; grades went from 88 at version 1.7 to 95 at 1.10, and a tougher grader gave 1.11 an 84. On the evening of 3 November he asked for the SWMM6 house as a separate app.
- The SWMM5 house engine "matches stored native 5.2.4 output digit for digit on 75 of 78 test models, though its build record (the source commit, compiler and flags) is still missing". [S68](S68-swmm5-code-house-app-md.md), a week later, records the commit, compiler and flags.
- Credits: Lew Rossman for the C on the SWMM5 walls; Caleb Buahin, Corinne Wiesner-Friedman and the OpenSWMM team for the C++.

**Limits it states.** No engine was compiled or run for the SWMM6 app. The call map is by name. No person has been tested with it.

**Checked at ingest.** 351,187 / 51,080 = 6.9, so "about seven times" holds against the line count in [S68](S68-swmm5-code-house-app-md.md) (our arithmetic). "76 SWMM 5 files" does not match the 54 files of S68 (Q46).

**Feeds:** [SWMM6 Code House (app)](../entities/swmm6-code-house.md), [SWMM5 Code House (app)](../entities/swmm5-code-house.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [EPA SWMM 5](../entities/swmm-5.md), [The SWMM findings register](../concepts/findings-register.md).
