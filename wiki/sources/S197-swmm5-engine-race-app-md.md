---
title: "S197: SWMM5 Engine Race, technical summary (app .md, v1.0.0)"
type: source
raw: raw/apps/swmm5-engine-race-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-11
ingested: 2026-11-17
tags: [apps, swmm5, wasm, speed, byte-for-byte, corpus, findings]
drafted_by: Claude (Anthropic), at Bob's direction
reviewed: no
---
**What it is.** The technical summary that ships with SWMM5 Engine Race, version 1.0.0 (11 November 2026). The page runs one .inp on two WebAssembly builds of EPA SWMM 5.2.4, stock and fast, times each phase, and checks that both write the same .out and .rpt bytes. Raw file: [raw/apps/swmm5-engine-race-v1.0.0.md](../../raw/apps/swmm5-engine-race-v1.0.0.md).

**How it was written.** By Claude (Anthropic) in two sessions on 10 and 11 November 2026, at Bob's direction; Bob set the goal (speed up the WebAssembly engine, starting from a poster of compiler stages), supplied the corpus and asked for the race app. Claude wrote the patch, the build and benchmark scripts, the self-test and the page, and ran every measurement. The checks are mechanical. No person has reviewed the patch line by line, run the page in Firefox or Safari, or repeated the timings on another machine.

**Claims worth keeping**
- Two builds from tag v5.2.4, Emscripten 3.1.51, clang/LLVM 18.1.3, Binaryen 116. Stock: `-O2`, wasm SHA-256 `fbbfb0a2...`. Fast: the tag plus `swmm524-fast-io.patch`, `-O3 -flto -fno-math-errno -msimd128 -mbulk-memory -DSWMM_FAST_IO`, wasm SHA-256 `35767fbb...`. Not used: `-ffast-math`, `-mnontrapping-fptoint`, threads, WASMFS.
- The patch, 659 lines over six files, all behind `#ifdef SWMM_FAST_IO`: `output.c` reads results back with one `pread()`; `report.c` caches each period's date stamp (up to 64 MB) and prints numbers with `fast_fmtFixed` (exact, integer arithmetic, half to even), one `fwrite` per line; `input.c` and `rain.c` parse plain decimals as integer over a power of ten with one IEEE division and fall back to `strtod` or `sscanf` otherwise; `project.c` and `output.c` get 64 KB stdio buffers. A post-link script makes MEMFS files grow by doubling up to 256 MB (stock: x1.125 past 1 MB).
- Speed-up, Node 22.23.4 on 2 cores, step API with report tables, median of interleaved pairs: Greenville (all SWMM5 features) 1.31x; 490 H&H elements 1.19x; Bellinge 5 hours 1.57x; 4,569 nodes, 6 hours 1.60x; 1000-year case, first 50 years 2.24x; Bellinge full 2 days 1.29x (2 pairs). One-shot, no `swmm_report`: 1.16x, 1.12x, 1.59x, 1.12x and 1.72x.
- All 104 of those runs wrote identical .out and .rpt between builds and between repeats.
- Compiler flags alone, stock source: routing phase 1.06x to 1.19x, but the whole-run pair ranges reach 0.99 or lower, so not resolved.
- Corpus sweep, 1,156 distinct .inp files from 23 folders of 1729-SWMM5-Models-2030: 728 identical, 352 same error and same report, 76 skipped (baseline over 12 s), 0 different; 1.08 GB of .out compared. 187 of the 352 stop at ERROR 205 and 28 at ERROR 317.
- `fastio_selftest.c`: 12,847,544 fast-path cases against the C library, 0 mismatches; with the tie rule or the float boundary guard removed it reports mismatches.
- Calls from wasm into JavaScript during `swmm_report` on Cycling_pumps.inp (345,480 table lines): stock 4.00 per line and 2,076 bytes read per line; fast 1.01 and 52.
- In headless Chrome on the same machine: Cycling pumps 2.15x; Greenville 1.03x; Bellinge 5 hours with its 26 MB rain file 1.59x; EPA site drainage example, one-shot, 0.84x (0.281 s against 0.334 s). The fast module is 90,141 bytes larger.
- The stock wasm build is not byte-identical to a native gcc build of 5.2.4 (a different libm `pow`): on Greenville 4.3 % of conduits differ by more than 1 % of their own peak at the worst instant, peaks unchanged. The fast build inherits this.
- Finding F-1, open in SWMM itself: `gage.c` casts `Tseries[k].dxMin*SECperDAY` to int while `dxMin` is still at its huge initial value for a one-point series. The result is undefined in C; `-mnontrapping-fptoint` changes it, and WARNING 09 appears on 25 of the first 287 corpus models. The flag is not used; the cast is unchanged.

**Limits it states.** One 2-core machine, with 4 to 17 percent run-to-run spread. Parity is shown only for models that ran in under 12 s plus the benchmark runs; the 76 skipped were not compared. The "same error" models exercise parsing, not routing. Hot start, interface and RDII file paths were not stress-tested. Saving inside the claude.ai viewer was not exercised.

**Checked at ingest.** 728 + 352 + 76 = 1,156. 27 step-API pairs + 25 one-shot pairs = 52 pairs, or 104 runs. The speed-up column is the median of per-pair ratios, so it need not equal the ratio of the printed times (2.67 / 2.13 = 1.25 against 1.31x for Greenville). The finding label F-1 has the form of the findings register's F-0001 series (Q47).

**Feeds:** [SWMM5 Engine Race (app)](../entities/swmm5-engine-race.md), [Engine speed, 1988 to 2024](../concepts/engine-speed-1988-2024.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md), [Byte-for-byte gate](../concepts/byte-for-byte-gate.md), [The SWMM findings register](../concepts/findings-register.md), [1729-SWMM5-Models-2030 (the corpus)](../entities/corpus-1729.md), [Open questions](../open-questions.md).
