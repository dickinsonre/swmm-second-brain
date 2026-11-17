---
title: SWMM5 Engine Race (app)
type: entity
updated: 2026-11-17
sources: [S197]
tags: [apps, swmm5, wasm, speed, byte-for-byte]
reviewed: no
---
Bob's app that runs one .inp on two WebAssembly builds of [EPA SWMM 5](swmm-5.md) 5.2.4, stock and fast, times each phase, and checks that both write the same .out and .rpt bytes. Version 1.0.0, 11 November 2026 [S197](../sources/S197-swmm5-engine-race-app-md.md).

**The fast build.** A patch of 659 lines over six files, all behind `#ifdef SWMM_FAST_IO`, plus `-O3 -flto` and SIMD flags. It changes how the engine reads and writes, not how it computes: one `pread()` for results, cached date stamps and an exact integer formatter for the report, a fast decimal parser for input and rain files, 64 KB file buffers, and file growth by doubling in the browser's in-memory file system. `-ffast-math` is not used [S197](../sources/S197-swmm5-engine-race-app-md.md).

**Speed-up in Node on 2 cores, with report tables** [S197](../sources/S197-swmm5-engine-race-app-md.md)

| Model | Speed-up |
|---|---|
| Greenville, all SWMM5 features | 1.31x |
| 490 H&H elements | 1.19x |
| Bellinge, 5 hours | 1.57x |
| 4,569 nodes, 6 hours | 1.60x |
| 1000-year case, first 50 years | 2.24x |
| Bellinge, full 2 days (2 pairs) | 1.29x |

Without the report step the range is 1.12x to 1.72x. A short run can be slower: 0.84x on the 0.3 s EPA site drainage example. Compiler flags alone did not give a resolved speed-up [S197](../sources/S197-swmm5-engine-race-app-md.md).

**Same bytes.** All 104 benchmark runs wrote identical .out and .rpt files. Across 1,156 corpus models, 728 were identical, 352 stopped at the same error with the same report, 76 were skipped as too slow, and 0 differed. A self-test ran 12,847,544 number cases against the C library with 0 mismatches [S197](../sources/S197-swmm5-engine-race-app-md.md). See [Byte-for-byte gate](../concepts/byte-for-byte-gate.md).

**Two findings on the way** [S197](../sources/S197-swmm5-engine-race-app-md.md)
- The stock wasm build is not byte-identical to a native gcc build of 5.2.4, because of a different math library `pow`. See [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
- F-1: `gage.c` casts a huge initial `dxMin` times seconds per day to int for a one-point series, which is undefined in C. One compiler flag changes the result and makes WARNING 09 appear on 25 of 287 corpus models. The flag is not used.

**What it does not show.** Timings from one 2-core machine, with 4 to 17 percent spread. No Firefox, Safari or other hardware. No person has reviewed the patch line by line [S197](../sources/S197-swmm5-engine-race-app-md.md).

**Related.** [Engine speed, 1988 to 2024](../concepts/engine-speed-1988-2024.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md).
