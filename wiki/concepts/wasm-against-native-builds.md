---
title: WebAssembly builds against native builds
type: concept
updated: 2026-11-15
sources: [S68, S73, S74, S76, S77, S78, S79, S80, S81, S82, S83]
tags: [wasm, verification, swmm5, math-library, apps]
reviewed: no
---
Most of Bob's engine apps run EPA SWMM 5.2.4 compiled to WebAssembly inside the page. Does that build give the same answers as a native build of the same C? Several apps tested it, and they do not all report the same thing. One of them found the cause [S82](../sources/S82-mirab-test-bench-summary.md).

**What each app measured**

| App | Compared | Result |
|---|---|---|
| [Mirab Test Bench (app)](../entities/mirab-test-bench.md) | 449 `.inp` files, native glibc against the page | 380 byte-identical, 59 differ, 10 rejected by both [S82](../sources/S82-mirab-test-bench-summary.md) |
| [Under Load (app)](../entities/under-load.md) | 72 EPA regression models, native gcc against wasm | 63 identical; largest difference 16.19 of 168.73 cfs in one link [S77](../sources/S77-under-load-app-md.md) |
| [SWMM5 Code House (app)](../entities/swmm5-code-house.md) | 78 corpus models against stored native output | 75 identical to the last stored digit; why three differ "was not traced" [S68](../sources/S68-swmm5-code-house-app-md.md) |
| [Teacher-Forced SWMM (app)](../entities/teacher-forced-swmm.md) | 15 runs | 15 byte-identical [S79](../sources/S79-teacher-forced-swmm-summary.md) |
| [Control Section Lab (app)](../entities/control-section-lab.md) | Its SWMM 5 and SWMM6 test models | `.out` files byte-identical [S80](../sources/S80-control-section-lab-summary.md) |
| [Inside the Network (app)](../entities/inside-the-network-cfd.md) | 3 twin models and 4 EXTRAN examples | Identical on every record both wrote [S76](../sources/S76-inside-the-network-cfd-app-md.md) |
| [EXTRAN III Workbench (app)](../entities/extran-iii-workbench.md) | EXTRAN III, seven decks | Reports byte-identical to the same C built natively [S74](../sources/S74-extran3-workbench-app-md.md) |

**The cause, where one was found: the math library.** The Mirab bench reran all 59 differing files with a native build linked against musl instead of glibc, and 59 of 59 then matched the page byte for byte. Its register concludes the cause is the math library, glibc against musl, "which wasi-libc inherits", and not WebAssembly. Across the 59 the median worst relative difference is 6.44e-08, but 15 are above 1 % and 11 above 10 % [S82](../sources/S82-mirab-test-bench-summary.md).

**The same thing at the scale of one function.** In the SWMM 1 Engine's Runoff workbench, a native glibc build differed from the browser on 2 of 9 decks. Logs of 180,246 math-library calls showed `powf`, `expf` and `sqrtf` never differing, and `sinf` and `cosf` differing by one unit in the last place in 572 of 69,342 calls, all in circular-pipe geometry. In all 194 distinct cases the browser's (musl) value was the correctly rounded one. A small header that computes sine and cosine in double and rounds once makes a native build match the browser bit for bit [S73](../sources/S73-swmm1-engine-app-md-v3-13.md).

**A candidate explanation, not yet tested.** The SWMM5 Code House's three untraced models and Under Load's nine may be the same effect. Neither app reran with musl, so this is a guess from the Mirab result, and it is recorded as Q55.

**At least ten builds of one engine.** The apps do not share one WebAssembly build of EPA SWMM 5.2.4. The ones whose summaries are ingested here:

| App | Toolchain | Bytes or hash prefix |
|---|---|---|
| SWMM5 Code House | Emscripten 3.1.51 | `e371a849` [S68](../sources/S68-swmm5-code-house-app-md.md) |
| [Bellinge (app)](../entities/bellinge-app.md) | Emscripten 3.1.51 | 678,177 bytes, `4602e507` [S81](../sources/S81-bellinge-summary.md) |
| Control Section Lab | clang, wasm32-wasi | 843,203 bytes, `50346aae` [S80](../sources/S80-control-section-lab-summary.md) |
| Teacher-Forced SWMM | not recorded; four patches | 843,845 bytes, `2eeb51fd` [S79](../sources/S79-teacher-forced-swmm-summary.md) |
| Mirab Test Bench | clang 18, `-O2 -ffp-contract=off` | not recorded [S82](../sources/S82-mirab-test-bench-summary.md) |
| [People as Pollutants (app)](../entities/people-as-pollutants.md) | clang 18, reactor | `0225fd30` [S83](../sources/S83-people-as-pollutants-summary.md) |
| [Fractal SWMM5/SWMM6 Network Generator (app)](../entities/fractal-swmm-generator.md) | clang 18, reactor | `edf4f4ee` [S78](../sources/S78-fractal-swmm-generator-app-md.md) |
| Under Load | zig 0.17.0 cc, `-O2` | `661fc2b6` patched, `5847388b` unpatched [S77](../sources/S77-under-load-app-md.md) |
| EXTRAN III Workbench | not recorded | 529,581 bytes, `6f2e7d58` [S74](../sources/S74-extran3-workbench-app-md.md) |
| Inside the Network | wasm32-wasi reactor, KW/SF patch | 853,130 bytes, `e62aa569` [S76](../sources/S76-inside-the-network-cfd-app-md.md) |

The Code House and Bellinge builds name the same compiler and carry different hashes. Under Load counts its patched and unpatched builds as one row here.

**What follows for a claim of "engine-verified".** A result from a browser build of 5.2.4 is a result from that build's compiler and math library. For most models the difference from a glibc build is in the eighth digit; for a minority it is not small [S82](../sources/S82-mirab-test-bench-summary.md).

See [Matching glibc math in a translation](glibc-math-in-translation.md), where the translations of the engine meet the same problem from the other side, and [Byte-for-byte gate](byte-for-byte-gate.md).
