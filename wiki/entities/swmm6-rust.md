---
title: swmm6-rust
type: entity
updated: 2026-11-14
sources: [S29]
tags: [swmm6, translation, verification, 2d, rust]
reviewed: 2026-11-15
---
The OpenSWMM 6 engine translated from C++ into safe Rust (`#![forbid(unsafe_code)]`), 1D first and then 2D surface flow with 1D-2D coupling, each piece checked byte for byte against OpenSWMM 6 built from the same source [S29](../sources/S29-swmm6-rust-readme.md). Upstream is HydroCouple/openswmm.engine, branch `swmm6_rel`, commit 88329d6, 6.0.0-alpha.4 [S29](../sources/S29-swmm6-rust-readme.md).

**What makes it different from the other ports.** It is translated from the C++, not from the C# the other [SWMM6 language translations](swmm6-language-ports.md) start from, and it is the only one with 2D. It also checks more than the output files: the state of the engine after every step [S29](../sources/S29-swmm6-rust-readme.md).

**The four gates** [S29](../sources/S29-swmm6-rust-readme.md)

| Gate | What must hold |
|---|---|
| G1 | `.out` byte-identical to the C++ engine on every gate deck |
| G2 | `.rpt` identical except the wall-clock lines |
| G3 | State after every routing step bit-identical |
| G4 | Leaf functions identical to upstream's own code, compiled from upstream source |

G3 exists because a float32 `.out` can hide differences: both engines dump every member of the context as hex bits after each stage and the dumps are compared [S29](../sources/S29-swmm6-rust-readme.md).

**Where it stands** [S29](../sources/S29-swmm6-rust-readme.md)
- 1D: all 932 gate decks identical end to end (480 corpus, 336 upstream test decks, 116 synthetic).
- 2D (phase 2a): 1,315 of 1,415 gate decks identical through the command-line program, including every 2D deck that runs to completion (425); the other 100 stop at features not yet translated.
- Paths no gate deck reaches are left untranslated on purpose. A deck that needs one stops before anything changes and exits with status 3. Examples: DYNAMIC_SLOT and TPA surcharge, FV_PRESSURIZED_IMPLICIT, USE and SAVE RUNOFF.
- Not started: 2D aquifer and subsurface flow, surface quality, heat and snow on the mesh, the GPU backend, the HDF5 2D writer.

**Upstream oddities.** Where upstream does something odd, the Rust does the same and UPSTREAM_NOTES.md records it with the code quoted. Where upstream crashes, the Rust returns an error at the same point with the same message [S29](../sources/S29-swmm6-rust-readme.md). The notes themselves are not yet a raw source here.

**People.** Upstream's lead developer is Caleb Buahin, with Corinne Wiesner-Friedman on development and documentation. Claude wrote the translation; Bob set the goal and the approach [S29](../sources/S29-swmm6-rust-readme.md).

See [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md).
