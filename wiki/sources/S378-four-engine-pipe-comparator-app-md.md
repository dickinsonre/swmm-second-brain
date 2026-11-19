---
title: "S378: Four-Engine Pipe Comparator, app .md (v1.5.0)"
type: source
raw: raw/apps/four-engine-pipe-comparator.md
kind: app-md
author: Robert Dickinson
published: 2026-11-18
ingested: 2026-11-19
tags: [apps, hec-ras, icm, swmm5, swmm6, pressurization, verification]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** A technical summary of the app Four-Engine Pipe Comparator, version 1.5.0: what HEC-RAS Pipe Networks, InfoWorks ICM, EPA SWMM5 and OpenSWMM 6 each pay for pressurization, on one shared benchmark. Raw file: [raw/apps/four-engine-pipe-comparator.md](../../raw/apps/four-engine-pipe-comparator.md).

**How it was written.** The app ships this file. Its AI-use section: "Built with Claude (Anthropic). Claude wrote all page code, the four Node test suites, the build scripts, the Doc essay, every figure, and this file." Claude read the sources behind the engine claims; Bob set the brief, supplied the engine knowledge, said the SWMM6 column was wrong to be called roadmap when the finite volume solver was already shipping, and supplied an outside review whose five bug reports were all real. The file does not open with an In three points block.

**Claims worth keeping** (all copied from the file)
- The app compares how HEC-RAS Pipe Networks (7.0.1), InfoWorks ICM, EPA SWMM5 (5.2.x) and OpenSWMM 6 (6.0.0-alpha.3, branch `swmm6_rel`) route unsteady flow through closed conduits. It states each engine's scheme and capabilities with caveats, computes what pressurization costs each in stable timestep on a pipe the user specifies, generates a surcharge benchmark as a SWMM5 .inp (the one format all four read), and scores returned hydrographs. No engine runs inside the app.
- Formulas: open-channel celerity `c = sqrt(g*A/T)`; Preissmann slot celerity `c_slot = sqrt(g*A_full/(f*D))` for a slot of width `f*D`; Courant bound `dt = Cr*dx/(V + c)`.
- OpenSWMM's FV kernels, mirrored: mesh `n = max(FV_MIN_CELLS, ceil(L/FV_CELL_LENGTH))` with defaults 4 and 0 (no length target); a static slot `T_slot = g*A_full/c^2` capped at `0.05*w_max`; explicit substep `dt_sub = FV_CFL*dx_cell/(|V| + c)` with `FV_CFL` 0.5; local time stepping in power-of-two tiers.
- Anchored to OpenSWMM's own documented values: slot width 0.0228 ft on a 3 ft pipe at `FV_SLOT_CELERITY` 100, half-full celerity 6.16 ft/s, the ratio of 16.
- The numbers the build reports on a 3 ft pipe, 330 ft long, at 3 ft/s and Cr 0.75: SWMM5 SLOT 2.75 s, SWMM5 EXTRAN 14.72 s, ICM 5 to 60 s (accuracy choice), HEC-RAS 82.5 s, SWMM6 FV 0.400 s substep on an 82.5 ft cell. Half-full celerity 6.16 ft/s; 1 percent slot 87.07 ft/s.
- 204 checks in four suites (39 FV, 57 core, 47 theme, 61 smoke), all green at this build; each suite extracts its functions from the shipped HTML, so the tests exercise the shipped code.
- Comparison trap: SWMM6 reports conduit flow as the mean face mass flux over the reporting step, not the end-of-step momentum state. Upstream found a force main delivering 25 cfs whose cell momentum state held 18.4.
- Version 1.5.0 corrected SWMM6 FV facts superseded by the November rebuild: algebraic junctions return no timestep bound, the cost case turned over, and 22 FV_ keys parse as 20 live plus 2 retired. It also fixed a second gravity constant (32.2 against the file's `G_US = 32.174`).
- SWMM App Complexity Meter: index 52.9 across all hand-written source; the shipped .html alone reads 47.7 (HydroCouple = 100, analyzer 1.7.0).

**Limits it states.** No engine has ever run inside the page: all 128 capability cells are a reading of documentation, release notes, source and upstream measurements. The finite volume cost figures are quoted, not measured: the superseded August column (peak deviation 37.1 / 15.3 / 7.2 percent, wall clock about 7x to 34x dynamic wave) and the current one (about 3 percent at every resolution, wall clock at parity with dynamic wave or better, reference continuity 0.024 percent) are the upstream commit's own numbers. SWMM6's hydraulic parity with SWMM5 on the classic corpus is close but not exact: a wide metric sweep found a 0.84 percent worst-case flooding peak and one model disagreeing on the number of reporting periods. The lab computes a single-reach Courant bound only. The benchmark scoreboard ships empty, and B2 to B5 have no generators.

**Checked at ingest.** Our arithmetic from the file's formulas: a 1 percent slot on a 3 ft pipe gives sqrt(32.174 x 7.069 / 0.03) = 87.07 ft/s, and 0.75 x 330 / (3 + 87.07) = 2.75 s; the FV substep 0.5 x 82.5 / (3 + 100) = 0.40 s; HEC-RAS's 82.5 s is 0.75 x 330 / 3, a bound on velocity alone. The slot width at 100 ft/s is 0.0227 ft with g = 32.174 and 0.0228 ft with g = 32.2. The `links:` line names no Netlify address and no artifact address. The file name carries no version.

**Feeds:** [Four-Engine Pipe Comparator (app)](../entities/four-engine-pipe-comparator.md), [HEC-RAS](../entities/hec-ras.md), [InfoWorks ICM](../entities/infoworks-icm.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md).
