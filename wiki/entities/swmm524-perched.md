---
title: swmm524-perched
type: entity
updated: 2026-11-17
sources: [S08, S55, S59, S70, S203]
tags: [swmm5, engine, lid, infiltration]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S203 ingest): one paragraph added at the end: drain correction, Windows builds, SOIL2 misread"
---
One of Bob's variants of [EPA SWMM 5](swmm-5.md) [S08](../sources/S08-swmm5org-topic-inside-swmm5.md). Repository SWMMBobSWMM6/swmm524-perched, branch van-genuchten, commit 548e5fbf; the source says no license is stated in the repo and that the EPA base is public domain [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**What it adds to 5.2.4** [S59](../sources/S59-topsoil-recovery-check-app-md.md)
- A `SOIL2` layer under the bio-retention soil. Flow from topsoil to SOIL2 is capped by SOIL2's Green-Ampt capacity with the perched head added.
- Optional `VG` lines. Head comes from van Genuchten curves (theta_s = porosity); drive = (h1 - h2)/dz + 1 with dz = 14 in; downward flow = K1 min(drive, 1), capped by Green-Ampt; upward flow = -K2 min(-drive, GMAX = 10); SOIL2 drains at K2(theta2) with no field-capacity cutoff. Curves: topsoil (0.1018, 0.04633 1/in, 1.3764), clay (0.2053, 0.02377 1/in, 1.5383).
- `VG OPTION TOPFC | FCDRAIN | SOIL2ET | FCHEAD | STEP`, each restoring one perched rule, for ablation.
- An experimental `STRUCT` Ksat decay, with illustrative rates.

**Relation to the SOIL2 proposal.** The README of the old swmm-brain repository describes a two-layer design with `SOIL2` and a `UseAsInfil` flag [S55](../sources/S55-swmm-brain-readme.md). This engine has the `SOIL2` keyword with a different flow rule. See [Two-layer soil infiltration (SOIL2)](../concepts/two-layer-infiltration.md).

**Checks** [S59](../sources/S59-topsoil-recovery-check-app-md.md)
- With no SOIL2, VG or STRUCT line it writes the same `.out` and LID report as EPA 5.2.4, byte for byte, on 930 of 930 inputs.
- The build with OPTION support matches the build before VG on 1,346 of 1,346 inputs without VG lines, and the first VG build on 27 of 27 VG inputs without OPTION lines.
- WebAssembly and native `.out` byte-identical on 38 of 38 VG inputs, OPTION cases included.

**A later count.** At commit 6f253a4 the change is 310 lines added and 2 changed in `lid.c`, `lid.h` and `lidproc.c`; with no SOIL2 line 598 of 598 test inputs write the same `.out` bytes as EPA 5.2.4; and with a subsoil conductivity of 1,000 in/hr runoff equals the stock result to 0.000 in across 64 recovery cases [S70](../sources/S70-swmm-engine-what-if-app-md.md). It is one of four engines on the extend road: see [Wrap, translate or extend](../concepts/wrap-translate-or-extend.md).

**Results on one soil pair** are on [Topsoil over compacted clay](../concepts/topsoil-over-compacted-clay.md): 83.0 % of big winter storms captured, 67.1 % with van Genuchten [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**Limits** [S59](../sources/S59-topsoil-recovery-check-app-md.md)
- Each layer is one moisture bucket; a wetting front inside the clay is represented only by the Green-Ampt cap. GMAX = 10 is a supplied, fitted value.
- Its flux routine sets `StorageDrain = 0.0`, so a DRAIN line has no effect (see [LID bio-retention layers](../concepts/lid-bioretention-layers.md)).

**Added 2026-11-17.** The last Limits bullet holds only for a model with a SOIL2 line; without one the engine runs 5.2.4's routine and shares defect D2 (232.848 in of drain flow from 20.550 in of rain) [S203](../sources/S203-topsoil-recovery-check-v2026-11-17.md). Windows x64 builds of this engine and of unchanged EPA 5.2.4, with a compare script, are in the repository's `windows/` folder, https://github.com/SWMMBobSWMM6/swmm524-perched/tree/van-genuchten/windows. Under Wine 9.0 their `.out` files are byte-identical to Linux builds made the same way on 8 example runs; they have not yet been run on a Windows machine [S203](../sources/S203-topsoil-recovery-check-v2026-11-17.md). A SOIL2 input must not go to stock 5.2.4 as written: 5.2.4 reads SOIL2 as a second SOIL line (see [LID bio-retention layers](../concepts/lid-bioretention-layers.md)) [S203](../sources/S203-topsoil-recovery-check-v2026-11-17.md).
