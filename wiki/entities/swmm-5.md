---
title: EPA SWMM 5
type: entity
updated: 2026-11-15
sources: [S02, S04, S08, S11, S15, S17, S19, S20, S21, S22, S41, S55, S59, S62, S67, S68, S70, S71, S72, S75, S76, S79, S80, S82, S83]
tags: [swmm5, engine]
reviewed: no
---
The C rewrite of SWMM, first released as 5.0 build 001 on 29 October 2004 [S22](../sources/S22-li-ten-problems.md). Written and carried for about twenty years by Lewis A. Rossman of EPA [S22](../sources/S22-li-ten-problems.md), [S21](../sources/S21-li-edition-56-swmm-history.md). See [Lewis A. (Lew) Rossman](lew-rossman.md).

**How it came about.** EPA and CDM signed a Cooperative Research and Development Agreement in 2001 [S21](../sources/S21-li-edition-56-swmm-history.md). Bob joined CDM in late 2000 and worked on the upgrade with Lew Rossman and Trent Schade at EPA and CDM's Jim Smullen, Ted Burgess, Carl Chan, Charles Rowney and Khalid Khan [S11](../sources/S11-li-my-history-with-swmm.md). The team's paper is Rossman, Dickinson, Schade, Chan, Burgess, Lai and Sullivan, WEFTEC 2003 [S19](../sources/S19-li-edition-29-engine-speed.md).

**Releases.** 42 builds from 5.0.001 to 5.2.4 [S22](../sources/S22-li-ten-problems.md). Dated ones are in [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md). The current stable release is 5.2.4 [S21](../sources/S21-li-edition-56-swmm-history.md).

**Status.** Public domain, open source [S11](../sources/S11-li-my-history-with-swmm.md), [S20](../sources/S20-li-edition-54-two-solvers.md). The EPA repository's default branch shows 0 commits in the 12 months to 1 November 2026 [S02](../sources/S02-complexity-meter-app-md.md).

**What the wiki holds on its insides**
- Routing: [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Preissmann slot and surcharge](../concepts/preissmann-slot-and-surcharge.md), [Conduit lengthening](../concepts/conduit-lengthening.md), [Force main friction](../concepts/force-main-friction.md).
- Hydrology: [Runoff surfaces and subarea routing](../concepts/runoff-surfaces-and-subarea-routing.md), [Subcatchment width](../concepts/subcatchment-width.md), [Infiltration methods](../concepts/infiltration-methods.md), [RDII unit hydrographs (RTK)](../concepts/rdii-unit-hydrographs.md). Function names are from [S15](../sources/S15-li-hydrology-code-story.md).
- Output: [Reading SWMM output](../concepts/reading-swmm-output.md).
- Documentation: [The missing specification](../concepts/the-missing-specification.md).

**Size.** More than 40 C source files [S55](../sources/S55-swmm-brain-readme.md).

**In the browser.** Compiled to WebAssembly with Emscripten, exporting `swmm_run`, `swmm_open`, `swmm_start`, `swmm_step` and `swmm_end`; the model, report and output files live in the module's in-memory file system [S55](../sources/S55-swmm-brain-readme.md).

**Bob's variants.** A [two-layer infiltration](../concepts/two-layer-infiltration.md) proposal [S55](../sources/S55-swmm-brain-readme.md). A fork with branches for a staggered grid, a Preissmann box, node surface area and six Curve Number changes; swmm5-kw; [swmm524-perched](swmm524-perched.md); and versions in C++, Rust, Fortran, C#, Python, TypeScript, Java and Go [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

**Translations.** Nineteen translations of 5.2.4 by Bob, each byte-identical to EPA on every one of the 480 gate models it finished: see [SWMM5 language translations](swmm5-language-ports.md) [S41](../sources/S41-swmm5-go-readme.md). Over those models EPA makes 1,524,961,124 calls to glibc's math library, and its results change on 43 of 480 models when glibc uses its generic routines instead of the FMA ones [S41](../sources/S41-swmm5-go-readme.md).

**Inside other products.** InfoSWMM uses the SWMM 5 C code as its engine [S11](../sources/S11-li-my-history-with-swmm.md). ICM SWMM runs the SWMM5 dynamic wave [S17](../sources/S17-li-routing-options.md).

**In a browser page.** The [Rules for Responsible Modeling (app)](rules-for-responsible-modeling-app.md) runs a WebAssembly build declared as 5.2.4 in a web worker. Its summary gives the binary's SHA-256 but marks the source commit, compiler flags and license audit "not checked" (Q39) [S62](../sources/S62-rules-for-responsible-modeling-app-md.md). The [Topsoil Recovery Check (app)](topsoil-recovery-check.md) pins its 5.2.4 build to tag v5.2.4, commit 7952ca83 [S59](../sources/S59-topsoil-recovery-check-app-md.md).

**Defects in 5.2.4 found by one study.** D1, Modified Horton with MaxInfil (`infil.c` line 545; see [Infiltration methods](../concepts/infiltration-methods.md)), and D2, a drain on a bio-retention cell with no storage layer (see [LID bio-retention layers](../concepts/lid-bioretention-layers.md)) [S59](../sources/S59-topsoil-recovery-check-app-md.md). Five more, found by translating the engine and numbered in [SWMM Engines, Byte for Byte (app)](swmm-engines-byte-for-byte.md): `inlet.c:146`, `gage.c:251`, `swmm5.c:1593`, `output.c:523`, `project.c:421` [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md). A possible one in `culvert.c`, Form 1 culverts, seen only in a JavaScript copy [S72](../sources/S72-li-swmm6-code-house-article.md). A third candidate, not yet rerun: the Green-Ampt Newton loop in `infil.c` lines 847 to 856 tests its correction before applying it (see [Green-Ampt Newton test order](../concepts/green-ampt-newton-test-order.md)) [S67](../sources/S67-note-green-ampt-newton-test-order.md).

**Back-compatibility hazard.** SWMM 5.2.4 stops with ERROR 205 on SWMM6 `[OPTIONS]` keywords; legacy 5.3 silently ignores them (F-0005, partly unconfirmed) [S04](../sources/S04-findings-register-seed.md).

**The code as a place.** [SWMM5 Code House (app)](swmm5-code-house.md) puts all of it on walls: 51,080 lines, 54 files, 969 functions [S68](../sources/S68-swmm5-code-house-app-md.md). The engine keeps a model in 415 mutable file-scope and program-scope variables, which is why one process holds one model [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**Complexity index.** 69.2 with HydroCouple = 100 [S02](../sources/S02-complexity-meter-app-md.md).

**Measured by the apps, October and November 2026.** Six pages hold what Bob's apps found by running or reading 5.2.4: [Hot start: what a restart loses](../concepts/hot-start-restart-state.md) [S79](../sources/S79-teacher-forced-swmm-summary.md); [Run duration floored to whole seconds](../concepts/run-duration-floor.md) [S76](../sources/S76-inside-the-network-cfd-app-md.md); [The crown cap at mid-pipe](../concepts/crown-cap-at-mid-pipe.md) [S75](../sources/S75-st-venant-rosetta-stone-app-md.md); [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md) [S82](../sources/S82-mirab-test-bench-summary.md); the control-section findings of the [Control Section Lab (app)](control-section-lab.md) [S80](../sources/S80-control-section-lab-summary.md); and two defaults, a 1 mm zero-depth test in quality routing and the minimum surface area, on [People as Pollutants (app)](people-as-pollutants.md) [S83](../sources/S83-people-as-pollutants-summary.md). None has been reviewed by a person or given a register ID.
