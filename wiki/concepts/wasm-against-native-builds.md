---
title: WebAssembly builds against native builds
type: concept
updated: 2026-11-19
sources: [S68, S73, S74, S76, S77, S78, S79, S80, S81, S82, S83, S157, S193, S194, S195, S196, S197, S199, S206, S210, S211, S212, S214, S222, S224, S229, S228, S242, S231, S227, S270, S274, S275, S283, S291, S285, S271, S377]
tags: [wasm, verification, swmm5, math-library, apps]
reviewed: 11/16/2026
changed_after_review: "2026-11-17 (S192 to S202 ingest): one paragraph and a table added at the end on five more apps (S193 to S199); 2026-11-17 (S205 to S223 ingest): a paragraph added near the end, headed Added 17 November 2026 (S206, S210, S211, S212, S214, S222); 2026-11-17 (S224 to S242 ingest): a paragraph added near the end, headed Added 17 November 2026 (S224, S229, S228, S242, S231, S227); 2026-11-18 (S268 to S299 ingest): a paragraph added near the end, headed Added 18 November 2026 (S270, S274, S275, S283, S291, S285, S271); 2026-11-19 (S377 to S382 ingest): a paragraph added at the end, headed Added 19 November 2026 (S377)"
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

**Added 16 November 2026.** Another app, [LSTM + SWMM5](../entities/lstm-swmm5-app.md), built its engine with clang 18 for wasm32-wasi (`-O2`, `-ffp-contract=off`, wasi-libc). Its six probe models gave byte-identical .out files in the browser and natively. Its calibration demo did not: 56 of 4,032 periods differ, at most 0.102 cfs (0.41 % of peak), NSE 0.999996 between the two. The native build disagrees with itself on 4 periods (at most 0.047 cfs) when glibc's FMA code paths are switched off [S157](../sources/S157-lstm-swmm5-summary.md). The source is a summary Claude wrote from the page (Q84). It bears on Q55.

**Added 17 November 2026: five more apps, and the math library named twice more.**

| App | Compared | Result |
|---|---|---|
| [SWMM5 Engine Race](../entities/swmm5-engine-race.md) | stock wasm against a native gcc build of 5.2.4 | Not byte-identical, because of a different libm `pow`; on Greenville 4.3 % of conduits differ by more than 1 % of their own peak at the worst instant, peaks unchanged [S197](../sources/S197-swmm5-engine-race-app-md.md) |
| [SWMM 3 Runoff & Transport](../entities/swmm3-runoff-transport-app.md) | the same C, wasm32 and gcc | Byte-identical on eleven cases, but only after both builds compiled the same musl 1.2.6 routines; the host libraries differed at the last bit of sinf, cosf, tanf, asinf, acosf, atanf, log10f, exp and pow [S193](../sources/S193-swmm3-runoff-transport-summary.md) |
| [SWMM 4 Twin Engines](../entities/swmm4-twin-engines.md) | gfortran, f2c + gcc, f2c + wasm | The same printed continuity error on five decks; the Runoff interface file byte-identical [S194](../sources/S194-swmm4-twin-engines-summary.md) |
| [SWMM5 RASPIPE](../entities/swmm5-raspipe.md) | 16 test decks | 15 byte-identical; the other off by at most 0.01 cfs on an 8 cfs link [S196](../sources/S196-swmm5-raspipe-summary.md) |
| [swmm5-kw](../entities/swmm5-kw.md) | its wasm engines against native builds (GCC 13 with musl 1.2.4) | "checked"; no count given [S195](../sources/S195-swmm5-kw-summary.md) |

Two more builds: Engine Race's stock and fast builds, Emscripten 3.1.51, wasm SHA-256 `fbbfb0a2` and `35767fbb` [S197](../sources/S197-swmm5-engine-race-app-md.md); [Seven SWMM Engines](../entities/seven-swmm-engines.md), Emscripten 3.1.51, 0.65 MB [S199](../sources/S199-seven-swmm-engines-summary.md). The Engine Race and SWMM 3 results point at the math library, as the Mirab bench did; they bear on Q55.

**Added 17 November 2026.** Six more app summaries report a browser build of EPA SWMM 5.2.4 against a native one: 36 of 36 inputs byte-identical [S206](../sources/S206-runoff-block-summary.md); 16 of 16 against a musl build, with a glibc build within 7e-7 ft [S210](../sources/S210-swmm5-implicit-box-bench-summary.md); 46 of 60 corpus models [S211](../sources/S211-swmm5-self-regeneration-summary.md); 89 of 100, where on one of the other 11 a last-bit change moved a pump switch and changed a flow by 100 % of peak [S212](../sources/S212-swmm5-residual-walk-summary.md); 32 of 33 [S222](../sources/S222-swmm5plus-bench-summary.md); one model of 2,661,597 bytes [S214](../sources/S214-lead-pump-pointer-summary.md). All are summaries Claude wrote from the pages (Q108).

**Added 17 November 2026, second batch.** From the second batch: 16 of 16 on the OpenSWMM legacy 5.3 engine [S224](../sources/S224-conformal-swmm-app-md.md); every case of eight automata [S229](../sources/S229-rule110-swmm5-summary.md); three of three default designs, 275,760 bytes each [S228](../sources/S228-logic-based-generative-swmm5-summary.md); fixed-step surges, with the variable-step flood envelope within 0.0007 ft [S242](../sources/S242-walk-the-mesh-summary.md); 13 of 13 [S231](../sources/S231-swmmcraft-ultimate-app-md.md); two of two at p = 5 and 7 [S227](../sources/S227-kleinian-swmm-summary.md).

**Added 18 November 2026.** More apps compare a browser build with a native one:
- A wasm build of EPA 5.2.4, run in Node, changed 1 of 437 corpus runs against a native musl build; its math matched musl bit for bit and differed from glibc on 2.9% of calls [S270](../sources/S270-how-many-languages-swmm5-summary.md).
- The Tri-Pyramid engine writes a 319,329-byte .out byte-for-byte identical to a native gcc build's [S274](../sources/S274-tri-pyramid-summary.md); Des Moines' sanitary sample gives byte-identical .out files, and its storm sample differs by at most 0.06% of a peak [S275](../sources/S275-des-moines-sewer-swmm5-summary.md).
- Cymatic Synapse's browser and native 5.2.4 agree byte for byte on six of ten presets and within 0.059 ft on the rest [S283](../sources/S283-cymatic-synapse-generator-summary.md).
- A prebuilt wasm 5.2.2 matched native 5.2.4 on 17 small models with a largest difference of 0 [S291](../sources/S291-seven-studies-swmm-app-md.md); SWMM6 Shoebox's 16 compared numbers matched exactly between Chromium and Node [S285](../sources/S285-swmm6-shoebox-summary.md).
- SWMM 4.4H through f2c in the browser against native gfortran: of 1,643 numbers that differ on the Extran example, 1,250 differ in the last digit [S271](../sources/S271-swmm44h-workbench-summary.md).

**Added 19 November 2026.** [FV Link Lab](../entities/fv-link-lab.md) compared its two WebAssembly engines with native over the 73 EPA regression models. Stock and finite-volume builds each gave 65 identical, 1 `.rpt` with round-off only, 6 `.out` files that differ and 1 with the same error; the largest difference is 16.2 cfs in 1,962 cfs (0.83 %, user5), and the source says it follows the math library, musl against glibc [S377](../sources/S377-fv-link-lab-app-md.md). The null effect of the `[FV_LINKS]` patch still holds exactly inside WebAssembly on all 73 [S377](../sources/S377-fv-link-lab-app-md.md). In the page, 9 samples run through its own engines and native gave 18 `.out` files byte-identical [S377](../sources/S377-fv-link-lab-app-md.md).
