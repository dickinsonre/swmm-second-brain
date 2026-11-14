---
name: Control Section Lab
file: control-section-lab.html
version: 1.2
date: 2026-10-18
written: 2026-11-14
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/LQxgGtb6dRgCrKEPox5srx", netlify: "https://swmm-icm-control-section-lab.netlify.app (not read for this summary; it may serve another build)", repo: none recorded in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model, tag v5.2.4, unmodified", license: public domain, use: "runs in the page; clang to wasm32-wasi; 843,203 bytes; sha256 50346aaef8848143f42e082fdde36d741116ce5eff68f2680e6fcd1ac1fef17b"}
  - {name: OpenSWMM, version: 6.0.0-alpha.4, branch: swmm6_rel, commit: 64d517f1f238361e42488ac239078761ba74f81a, commit_date: 2026-10-16, license: Apache-2.0, use: "runs in the page as dynamic wave (DW) and finite volume (FV); wasi-sdk-34 (clang 23.1.0), wasm32-wasip1, -fwasm-exceptions; 3,868,436 bytes; sha256 f46bea530af76cdfe57d5de32118e305665b78f266c88e4ed7ac0960e5e41a07; five changed build files"}
  - {name: InfoWorks ICM, version: none, use: "no ICM engine runs in the page; an ICM-rule line is drawn from ICM's documented defaults"}
units: US customary (cfs, ft). ICM's documented space-step limits are quoted in meters as the page gives them.
ai_use: the app was built with Claude (Anthropic). This summary was written by Claude from the page's source. See AI use.
written_from: "the published artifact's page source, its embedded build record (script#build-data, built 2026-10-18, findings version 52004) and its Doc essay, read on 2026-11-14. No engine was run and no test was rerun to write this file."
---

# Control Section Lab: which section of a channel sets the water surface, and which engines find it

This summary was written after the fact. The page carries no technical summary of its own. Every number below is copied from the page's build record or its Doc essay. Stored depths are long decimals; they are shown here to four places. Nothing here was measured again.

## What it does

One channel reach, one steady flow. The user changes the discharge, the throat, the sill, the chute and the tailwater. A reference solver finds the control section and colors the water by the control that governs it. The page then runs EPA SWMM 5.2.4 and OpenSWMM 6 (dynamic wave and finite volume) on the same reach and compares node depths with the reference. An ICM rules tab applies InfoWorks ICM's documented solver settings. A Findings tab records nine measured results, F1 to F9, and a button reruns every case in the browser, about 70 engine runs in all.

The essay says the idea comes from the Control Section Lab at Vasslab, which this app rebuilds around a SWMM-style channel of eight conduits.

## The reach

Eight rectangular open conduits, 2,650 ft from node J1 to outfall OUT1. All are 30 ft wide and 20 ft deep except the throat. The bed slope is 0.001 except on the chute. The outfall invert is 100.00 ft and J1's is 110.25 ft.

| Conduit | Length, ft | Width, ft | Slope | Role |
|---|---|---|---|---|
| C1 | 400 | 30.0 | 0.0010 | approach |
| C2 | 300 | 30.0 | 0.0010 | rises to the sill at J3 |
| C3 | 300 | 30.0 | 0.0010 | falls from the sill |
| C4 | 150 | 14.0 | 0.0010 | the throat |
| C5 | 300 | 30.0 | 0.0010 | mild reach |
| C6 | 400 | 30.0 | 0.0200 | the chute, slope break at J6 |
| C7 | 400 | 30.0 | 0.0010 | mild reach |
| C8 | 400 | 30.0 | 0.0010 | tail reach to the outfall |

Defaults: Q 600 cfs, Manning n 0.022, throat 14 ft, no sill, chute slope 0.02, FREE outfall. Four features compete for control: the sill at J3, the throat C4, the chute crest at J6 and the outfall OUT1. Six presets are offered.

## How it computes

- **Reference.** A steady one-dimensional mixed-flow profile with jumps placed by specific force, written for the app. The essay names its method as the one in Chow's Open-Channel Hydraulics (1959) and in the mixed-flow option of the HEC-RAS Hydraulic Reference Manual, applied to rectangles. Constants: g = 32.2 ft/s² and the Manning constant 1.486. Each conduit is cut into steps no more than 2 ft long; at default settings the channel has 1,333 sections. Width changes are crossed by conserving energy with no friction and no contraction or expansion loss.
- **SWMM 5.2.4.** Driven through `swmm_open`, `swmm_start`, `swmm_step`, `swmm_end`, `swmm_close`, with depths and flows read by `swmm_getValue`. Two stand-ins only: `mkstemp` and `realpath`. Each case is a steady inflow run for 3 hours.
- **OpenSWMM 6.** Built with GeoPackage, HDF5, the 2D module and the GPU plugin off. Five files changed for a one-thread browser with no plug-ins: `src/engine/CMakeLists.txt`, `output/IOThread.cpp`, `plugins/PluginFactory.cpp`, `hydraulics/fv/NetworkSolverFactory.cpp`, `output/openswmm_output_impl.cpp`. The page says none touches the hydraulics.
- **ICM rule line.** The steady profile that ICM's documented rules imply: a free outfall at min(yn, yc), inertia phased out between the Lower Froude number (default 0.8) and the Upper (default 1.0), one water level per node. Other documented defaults shown: time weighting 0.65, space step 20 × min(width, height) limited to 0.5 to 100 m, minimum 5 nodes per conduit. The essay calls the line a prediction waiting for a test in ICM.

## Findings as stored

| ID | Finding | Stored numbers |
|---|---|---|
| F1 | When the tailwater controls everything, SWMM5 and the reference agree (prismatic reach) | Max difference 0.0003 ft with a FIXED 9 ft stage; 0.000005 ft with a NORMAL outfall |
| F2 | SWMM5 does not see the choke at the throat (defaults, NORMAL_FLOW_LIMITED BOTH, PARTIAL damping) | J1: reference 5.4682 ft, SWMM5 4.1179 ft. J2: 5.7128 and 4.0677. J3: 5.9098 and 4.0134. J4: 5.2475 and 3.9364. Largest shortfall 1.8964 ft, at J3. The engine's report classes C4 as supercritical for 98 % of the run |
| F3 | At the chute crest SWMM5 carries normal depth, not critical depth | J6: reference 2.3160 ft (critical depth), SWMM5 1.6232 ft (normal depth 1.6233 ft); 1.2522 ft with NORMAL_FLOW_LIMITED NONE. C6 is normal-flow limited for 97 % of the run |
| F4 | With the normal-flow limit off and the chute toe drowned (FIXED 9 ft), SWMM5 never settles | Last half hour of a 3 h, 600 cfs run. With NORMAL_FLOW_LIMITED NONE the flow in C6 swings 1,574.8 cfs, from -160.3 to 1,414.6. With BOTH, C6 holds within 6.6 cfs while C4 swings 142.6 cfs. Both verdicts are "not steady" |
| F5 | Shorter conduits do not converge here | Unsplit: steady, J1 4.1179 ft, 5,401 steps. Split in 2: not steady, J1 4.7548 ft. Split in 4: not steady, J1 4.5830 to 5.4310 ft. Split in 8: not steady, J1 4.6884 to 5.9995 ft, 17,089 steps. Reference 5.4682 ft |
| F6 | The damped momentum equation explains both misses | J6: damped profile 1.6233 ft, SWMM5 1.6232 ft, reference 2.3160 ft. J1: 4.2814, 4.1179 and 5.4682 ft |
| F7 | An entry loss on the throat can stand in for the choke at J1 | K found by bisection: 2.247 at 300 cfs, 2.675 at 600 cfs, 2.89 at 900 cfs. Using the 600 cfs K at 300 cfs gives 3.4479 ft against a target of 3.3177 ft; at 900 cfs, 7.0929 ft against 7.2846 ft |
| F8 | OpenSWMM 6 dynamic wave against SWMM 5.2.4 | Max node-depth difference 0 on the null control, the defaults and the split-in-4 case. 1.4249 ft on FIXED 9 ft with the limit NONE, where both engines are "not steady" |
| F9 | OpenSWMM 6 finite volume on the choke and the crest | Below |

F9, finite volume against the reference:

| Case | J1, FV and reference, ft | J6, FV and reference, ft | Max difference, ft | Settled | Continuity, % |
|---|---|---|---|---|---|
| Null control (prismatic, FIXED 9 ft) | 6.72 and 6.73 | 7.92 and 7.93 | 0.012 | steady | -0.003 |
| Defaults, default mesh (4 cells per conduit) | 5.47 and 5.47 | 2.59 and 2.32 | 1.038 | steady | -0.002 |
| Defaults, FV_CELL_LENGTH 25 ft | 5.64 and 5.47 | 2.55 and 2.32 | 1.237 | steady | -0.002 |
| FIXED 9 ft (jump in the chute) | 5.47 and 5.47 | 2.59 and 2.32 | 1.038 | steady | -0.002 |

The essay's reading of F9: on this channel the finite-volume solver is the only engine in the app that finds the choke and holds the crest near critical depth without a calibrated loss, and "that is one channel and one pre-release commit".

## Checks

From the essay's chapter 12. The three suites run against the shipped HTML file.

| Suite | Result | What it establishes |
|---|---|---|
| Physics (`test_core.js`) | 29 passed | An M2 drawdown agrees with an independent Runge-Kutta integration 1,000 ft upstream. An M1 backwater agrees with the continuous solution within 0.005 ft. With full inertia the damped integrator reproduces the standard step. σ(0.75) = 0.5 as in `dwflow.c` |
| SWMM5 engine (`test_engine.js`) | 33 passed | The browser 5.2.4 and a native gcc build run the same models; `.out` files are identical byte for byte and `.rpt` files identical apart from wall-clock lines |
| SWMM6 engine (`test_engine6.js`) | 24 passed | The browser OpenSWMM 6 and a native g++ build run six models, three DW and three FV. All six `.out` files are identical byte for byte. On two FV models the `.rpt` differs only in the clock time at which a steady node first reached its maximum |
| Browser pass (headless Chromium) | no errors | The built page loads, both engines run live, and the Findings rerun completes with the recorded wording |

Human review: none recorded.

## What this does not show

From the page's own list:

1. Unsteady flow. Every case is a steady inflow run to the end of three hours.
2. Three-dimensional, curved-streamline or air-entrained flow at the throat, the sill and the jumps.
3. Contraction and expansion losses in the reference, which crosses width changes with no loss.
4. The real length of a hydraulic jump. Jumps are placed at a single section.
5. ICM's own Preissmann discretization, base flow and conveyance handling.
6. SWMM models that use offsets, weirs or orifices to represent controls.
7. Depths inside conduits from the FV solver. The app reads node depths only.
8. Any OpenSWMM 6 build other than the one pinned.

Not checked, by the page's own account: no person has compared the ICM-rule line with an ICM run; the ICM descriptions rest on ICM's documentation, not its code; the OpenSWMM team has not reviewed the build changes; no person has checked the historical asides against the primary sources.

Added by this summary:

9. This file was written from the page, not from the build. No stored result was rerun.
10. F1 to F9 are the page's own IDs. This summary does not map them to any other register.

## How to reproduce

Open the artifact. The Findings tab's "Re-run all cases in this browser" button reruns every case and replaces the recorded numbers. Each finding has an "Open this case" button. The default `.inp` is printed in Appendix A of the essay and can be exported. To check this summary, view the page source and read `script#build-data`.

## Credits and licenses

- EPA SWMM 5.2.4: U.S. EPA, public domain.
- OpenSWMM 6: the OpenSWMM team at HydroCouple, Caleb Buahin (lead developer and maintainer) and Corinne Wiesner-Friedman (developer, documentation and technical review). Copyright 2026 HydroCouple Developers, Apache License 2.0 on the swmm6_rel branch. The page reproduces the upstream NOTICE and the Apache-2.0 text, opens with an attribution comment and marks the changed files. The USEPA and HydroCouple do not endorse the app.
- browser_wasi_shim 0.4.2 by bjorn3 and contributors (MIT or Apache-2.0). wasi-libc, and in OpenSWMM 6 LLVM's libc++, libc++abi and libunwind (Apache-2.0 with LLVM exception).

## AI use

From the essay's chapter 17: the app and both versions of its document were made with Claude, Anthropic's AI model, in a Claude session in October 2026, under the direction of Robert (Bob) Dickinson. He chose the subject and the Vasslab lab to follow, asked for InfoWorks ICM and the OpenSWMM 6 release engine to be added, asked for the first document and for its retelling in the manner of Isaac Asimov, and is responsible for the work. Claude read the SWMM 5.2.4 and OpenSWMM 6 sources and the ICM documentation; wrote the reference solver, the damped-equation integrator and the `.inp` builder; compiled both engines to WebAssembly and made the five-file build changes; ran the engine cases behind the findings; wrote the interface, the test suites and both documents. The checks are mechanical. No person has yet compared the ICM line with an ICM run, the OpenSWMM team has not reviewed the build changes, and no person has checked the historical asides against the primary sources.

This summary: written by Claude (model claude-fable-5-2) on 14 November 2026 at Bob's request, from the page source only. Bob has not yet read it.

## Changes

- `1.2 (2026-10-18)`: the build this summary describes. The page records no change history in the parts read.
