---
title: "S29: swmm6-rust, OpenSWMM 6 in safe Rust, 1D and 2D (README)"
type: source
raw: raw/ports/2026-11-12-swmm6-rust-README.md
kind: repo-readme
author: Robert Dickinson
published: 2026-11-12
ingested: 2026-11-14
tags: [swmm6, translation, verification, 2d]
reviewed: no
---
**What it is.** The README of the public repository SWMMBobSWMM6/swmm6-rust, as published on 2026-11-12: the OpenSWMM 6 engine's 1D path and its 2D surface flow with 1D-2D coupling, translated from C++ into safe Rust and checked byte for byte against OpenSWMM 6 itself. Unlike the other SWMM6 ports it is translated from the C++, not from the C#. Raw file: [raw/ports/2026-11-12-swmm6-rust-README.md](../../raw/ports/2026-11-12-swmm6-rust-README.md).

**How it was written.** By Claude (Anthropic's AI model, in Claude Code), which "wrote the translation, the gate harnesses, the generators and these documents". Bob "set the goal, chose the approach (1D first, byte for byte against OpenSWMM 6), and directed the work." The counts below rest on this AI-written text and on the gate tables in the repository's PLAN.md; no person has rechecked them.

**Claims worth keeping**
- Goal: the same `.out`, bit for bit, as the C++ engine on the same deck. "It is not a rewrite or a new solver." Every floating-point operation keeps upstream's order. Where upstream does something odd, the translation does the same and records it in UPSTREAM_NOTES.md, quoting the code.
- Upstream: HydroCouple/openswmm.engine, branch `swmm6_rel`, commit `88329d6df2f8dd63fe7e7c601954ec2bde3573e6`, which the README calls 6.0.0-alpha.4. Lead developer Caleb Buahin; developer and documentation Corinne Wiesner-Friedman.
- The library is `#![forbid(unsafe_code)]`.
- Phase 1 (1D): on all 932 gate decks (480 corpus decks, 336 of upstream's test decks, 116 synthetic decks) the `.out` is byte-identical to the C++ engine's, the `.rpt` identical but its three clock lines, and the exit code the same.
- Four gates: G1 `.out` byte-identical; G2 `.rpt` identical except the wall-clock lines; G3 state after every routing step bit-identical (every member of the engine's context dumped as hex bits and compared); G4 leaf functions identical to upstream's own code compiled from upstream source.
- What 1D covers: input reading, initialization, runoff (every infiltration method, snow, groundwater, RDII, LID, buildup and washoff, the SWMM6 snow, heat, water-age and reaction-species hooks), routing (STEADY, KINWAVE, DYNWAVE with EXTRAN and SLOT surcharge and virtual junctions), the FV router on its CPU explicit backend (HLL/HLLC with MUSCL-Hancock reconstruction), water quality under the legacy solver and the EULERIAN_ARD and LAGRANGIAN engines, and the `.out` and `.rpt` writers.
- The FV quality solve uses a `long double` dot product in upstream; the translation emulates it exactly (`core/ext80.rs`).
- Not translated, because no gate deck reaches them: among others DYNAMIC_SLOT and TPA surcharge, the reaction solvers ROS2 and BDF2, FV_PRESSURIZED_IMPLICIT, control-rule expression premises, USE and SAVE RUNOFF, and native hotstart files. A deck that needs one stops before anything changes and `openswmm` exits with status 3.
- Where upstream crashes (an exception escaping a `noexcept` function), the Rust function returns `Err(Terminated)` at the same point with the same exception type and message.
- Phase 2a (2D surface flow and 1D-2D coupling, cargo feature `twod`): `open()` leaves the context and 2D router identical to OpenSWMM 6's 2D build on 1,223 gate decks; `initialize()` and `start()` identical on 1,125 of them (228 with an active mesh); 298 uncoupled 2D decks (182 synthetic) and 122 coupled decks stay identical after every step to the end of the run.
- Built with `twod`, `openswmm` gives the same `.out`, `.rpt` (but its clock lines), exit code and stderr as OpenSWMM 6's 2D build on 1,315 of 1,415 gate decks, including every 2D deck that runs to completion (425). The other 100 stop where the translation refuses.
- Not started: the 2D aquifer and subsurface flow, surface quality and species transport, heat and snow on the mesh, the GPU backend, the HDF5 2D writer, checkpoint files and the swmm_2d_* C API.
- `census/` holds a comparison of OpenSWMM 6 against EPA SWMM 5.2.4 on a corpus of SWMM5 models.

**Feeds:** [swmm6-rust](../entities/swmm6-rust.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [SWMM6 language translations](../entities/swmm6-language-ports.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md).
