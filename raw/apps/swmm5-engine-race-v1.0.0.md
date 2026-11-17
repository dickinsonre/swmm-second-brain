---
name: SWMM5 Engine Race
file: swmm5-engine-race.html
version: 1.0.0
date: 2026-11-11
author: Robert Dickinson
links: {netlify: not deployed yet, artifact: private claude.ai artifact, repo: none}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4, build: stock, flags: "-O2", license: public domain, wasm_sha256: fbbfb0a2e0f3e6242316017511341a91cacd4a4a9a9b295c309f4aa031d79d75}
  - {name: EPA SWMM, version: 5.2.4, source: tag v5.2.4 + swmm524-fast-io.patch, build: fast, flags: "-O3 -flto -fno-math-errno -msimd128 -mbulk-memory -DSWMM_FAST_IO", license: public domain, wasm_sha256: 35767fbb8a42ccdac2f0e2d38bf158985728cb9c1b55df66a20944dae8e0c0a1}
toolchain: Emscripten 3.1.51, clang/LLVM 18.1.3, Binaryen 116
units: seconds and bytes; model units are whatever the .inp sets and are not touched
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM5 Engine Race: run one .inp on the stock and fast WebAssembly builds of EPA SWMM 5.2.4 and compare time and bytes

## In three points
- **What:** Runs one .inp on the stock and fast WebAssembly builds of EPA SWMM 5.2.4, times each phase, and checks that both write the same .out and .rpt bytes.
- **So what:** In Node the fast build ran 1.12x to 2.24x faster on the benchmark models, all 104 benchmark runs wrote identical files, and the corpus sweep of 1156 .inp files found 0 different.
- **Now what:** Race your own models on the Race tab. The timings so far come from one 2-core machine, and a short run can be slower on the fast build (0.84x on the 0.3 s site drainage sample).

## What it does

The page embeds two WebAssembly builds of EPA SWMM 5.2.4 and runs a user's model on both, in turn, for 1 to 7 rounds. It reports each run's time by phase, the median speed-up with the range of the per-round ratios, and whether the two builds wrote the same .out and .rpt bytes. It is for anyone who ships SWMM5 in a browser and wants to know what the fast build buys on their own models and machine. It also carries the measurements made while the fast build was developed.

## How it computes

1. Each run starts a new Web Worker from a blob holding the Emscripten glue (wasm inlined) plus the runner. New worker means new module and new in-memory file system. If workers cannot start, the same runner executes on the page thread in slices and only the slices are timed.
2. Files are written to MEMFS: `/m/model.inp`, each extra file at `/m/<name>`, and again at the path the .inp names for it when the base names match (`../DataFiles/x.dat`, or a Windows path as one odd file name).
3. Calls, each timed with `performance.now()` inside the worker: module factory (load), `swmm_open`, `swmm_start(1)`, a `swmm_step` loop until elapsed time is 0 or an error, `swmm_end`, `swmm_report` (step mode only), `swmm_close`.
4. `total = load + open + start + routing + end + report + close`.
5. Rounds alternate order: stock first on odd rounds, fast first on even rounds.
6. `speed-up = median over rounds of (stock total / fast total)`. Verdict: resolved if every round's ratio is above 1 (or every one below 1); not resolved if the range straddles 1; one round is reported as a single ratio.
7. Parity: SHA-256 (Web Crypto) of the whole .out, and of the .rpt up to the line "Analysis begun on" (the three closing wall-clock lines differ run to run). Same hash and same compared length in every run of both builds is reported as "same bytes out". FNV-1a is used only if Web Crypto is missing, and the page says so.
8. One-shot mode skips `swmm_report`, which is what `swmm_run` does when the .out file is named (swmm5.c calls `swmm_report` only for a scratch output file).

What the fast build changes (all behind `#ifdef SWMM_FAST_IO`, patch of 659 lines over six files):

- `output.c`: results are read back with one `pread()` in place of `fseek()` + `fread()`.
- `report.c`: the date and time stamp of each reporting period is formatted once and cached (up to 64 MB); numbers are printed by `fast_fmtFixed` (exact, integer arithmetic, half to even); one `fwrite` per line.
- `input.c`, `rain.c`: plain decimals are parsed as integer / power of ten with one IEEE division (`fast_parseDecimal`, `fast_parseDecimalF`); anything else falls back to `strtod` / `sscanf`.
- `project.c`, `output.c`: 64 KB stdio buffers on .rpt and .out.
- `swmm5_fast_post.js`: MEMFS file growth doubles up to 256 MB (stock: x1.125 past 1 MB) and sets `Module.swmmBuild`.
- Not used: `-ffast-math`, `-mnontrapping-fptoint`, threads, WASMFS.

## Inputs and outputs

- Reads: one .inp, plus any data files it names (.dat, .txt, .rin, .prn, .csv, .hsf, .rff). Three samples are embedded: the EPA site drainage example (29 KB), Cycling_pumps.inp (44 KB), Greenville_all_SWMM5_Features.inp (798 KB).
- The .inp is passed to both engines unchanged. Nothing is added or stripped.
- Writes (on request): the results CSV (one row per run, with phase times, sizes and hashes), the fast build's .rpt (saved as .rpt.txt, up to 64 MB), the bench tables CSV, this .md, and a GIF or WebM walkthrough.
- Nothing is uploaded. No network request is made by the page.

## Checks

Mechanical checks, with the numbers.

Engine parity and speed, Node 22.23.4 (V8), 2 cores, fresh process per run, builds interleaved (step API, with report tables):

| Model | Stock s | Fast s | Speed-up | Pair range | Pairs |
|---|---|---|---|---|---|
| Greenville, all SWMM5 features | 2.67 | 2.13 | 1.31x | 1.14 to 1.34 | 5 |
| 490 H&H elements | 2.20 | 1.65 | 1.19x | 1.18 to 1.43 | 5 |
| Bellinge, 5 hours | 7.25 | 4.71 | 1.57x | 1.36 to 1.65 | 5 |
| 4,569 nodes, 6 hours | 18.49 | 11.36 | 1.60x | 1.56 to 1.78 | 5 |
| 1000-year case, first 50 years | 7.80 | 3.48 | 2.24x | 2.08 to 2.43 | 5 |
| Bellinge, full 2 days | 139.49 | 108.35 | 1.29x | 1.29 to 1.29 | 2 |

One-shot (no `swmm_report`):

| Model | Stock s | Fast s | Speed-up | Pair range | Pairs |
|---|---|---|---|---|---|
| Greenville, all SWMM5 features | 2.33 | 2.02 | 1.16x | 1.13 to 1.35 | 5 |
| 490 H&H elements | 1.84 | 1.61 | 1.12x | 1.07 to 1.18 | 5 |
| Bellinge, 5 hours | 6.79 | 4.27 | 1.59x | 1.38 to 1.65 | 5 |
| 4,569 nodes, 6 hours | 11.91 | 10.45 | 1.12x | 1.09 to 1.20 | 5 |
| 1000-year case, first 50 years | 3.83 | 2.31 | 1.72x | 1.44 to 1.91 | 5 |

- All 104 of those runs: .out and .rpt identical between builds and between repeats.
- Compiler flags alone (stock source): routing phase 1.06x to 1.19x; whole-run pair ranges all reach 0.99 or lower, so not resolved.
- Corpus sweep, 1156 distinct .inp files from 23 folders of SWMMBobSWMM6/1729-SWMM5-Models-2030: 728 identical, 352 same error and same report, 76 skipped (baseline over 12 s), 0 different. 1.08 GB of .out compared.
- `fastio_selftest.c`: 12,847,544 fast-path cases against the C library, 0 mismatches; with the tie rule or the float boundary guard removed the same test reports mismatches.
- Calls from WebAssembly into JavaScript during `swmm_report` on Cycling_pumps.inp (345,480 table lines): stock 4.00 per line and 2,076 bytes read per line; fast 1.01 per line and 52 bytes.
- MEMFS growth replayed for a 200 MB file: stock rule 49 copies and 1595 MB moved; patched rule 12 copies and 256 MB. Computed, not timed.
- The embedded wasm modules are byte-identical to the benchmarked ones (SHA-256 in the front matter).

This page in headless Chrome 153.0.8010.12, 1280 x 900, same machine:

| Model | Mode | Rounds | Stock s | Fast s | Speed-up | Pair range | Verdict | Output |
|---|---|---|---|---|---|---|---|---|
| Cycling pumps | step API | 3 | 1.097 | 0.482 | 2.15x | 2.13 to 2.77 | resolved | identical |
| Greenville | step API | 3 | 2.578 | 2.365 | 1.03x | 1.02 to 1.14 | resolved | identical |
| Bellinge 5 hours, uploaded with its 26 MB rain file | step API | 3 | 7.364 | 4.633 | 1.59x | 1.50 to 1.63 | resolved | identical |
| EPA site drainage example | one-shot | 1 | 0.281 | 0.334 | 0.84x | 0.84 to 0.84 | single pair | identical |
| Cycling pumps, workers disabled (page-thread fallback) | step API | 1 | 1.067 | 0.463 | 2.30x | 2.30 to 2.30 | single pair | identical |

- Bellinge uploaded without its rain file: both builds stop at ERROR 317 with identical reports, and the page says the comparison covers the error path only.
- Greenville .out SHA-256 begins 6509627b20bb909e in Chrome and in Node.
- Welcome modal on load, 7-step tour, dark on first paint, theme toggle leaves every result string unchanged, no horizontal overflow at 375 px on the Race and Doc tabs, CSV saved, 8 figures in the Doc tab, GIF recorded (1.1 MB), 0 console errors.
- Contrast: 32 token pairs pass in both themes (lowest 3.26:1, faint labels, light); chart series at least 4.83:1 against the card.

Human review: none yet.

## What this does not show

1. No timing in desktop Chrome on other hardware, Firefox or Safari. The Race tab exists to produce those.
2. One 2-core machine with 4 to 17 percent run-to-run spread. The 2-day Bellinge figure rests on 2 pairs.
3. Parity is shown for corpus models that ran in under 12 s plus the benchmark runs. The 76 skipped models were not compared.
4. 187 of the 352 "same error" models stop at ERROR 205 and 28 at ERROR 317, so they exercise parsing, not routing.
5. Short runs: on the 0.3 s site drainage sample single pairs ranged 0.84 to 1.04. The fast module is 90,141 bytes larger.
6. The stock WebAssembly build is not byte-identical to a native gcc build of 5.2.4 (different libm `pow`). On Greenville 4.3 percent of conduits differ by more than 1 percent of their own peak at the worst instant, peaks unchanged. The fast build inherits this.
7. Hot start, interface and RDII text file paths were not changed and not separately stress-tested.
8. In the claude.ai artifact viewer saving goes through the viewer's download prompt, which was not exercised; only the standalone file's download path was tested.
9. Finding F-1 (open in SWMM itself): `gage.c` casts `Tseries[k].dxMin*SECperDAY` to int while `dxMin` is still at its huge initial value for a one-point series. The result is undefined in C; `-mnontrapping-fptoint` changes it and WARNING 09 appears on 25 of the first 287 corpus models. The flag is not used; the cast is unchanged.
10. No person has reviewed the patch line by line.

## How to reproduce

- Engines: `swmm5-fast-wasm.zip`, `build/build.sh` (clones tag v5.2.4, applies `src/swmm524-fast-io.patch`, builds stock, fast and single-file). It reproduced both wasm hashes above from a clean clone.
- Timings: `bench/ab.js` (interleaved pairs), parity sweep: `bench/sweep.js`, number test: `tests/fastio_selftest.c`. Raw results are in `results/`.
- Browser numbers: open the page, pick the sample, step API, 3 rounds. Models: Cycling_pumps.inp (Hydraulics folder), Greenville_all_SWMM5_Features.inp (Greenville folder), BellingeSWMM_v021_nopervious.inp with END_TIME 05:00:00 on 06/29/2012 (Special folder) and rg_bellinge_Jun2010_Aug2021.dat.

## Credits and licenses

- EPA SWMM 5.2.4, US EPA, public domain. Lewis Rossman and the EPA SWMM team wrote the engine.
- Emscripten (MIT / University of Illinois NCSA) generated the glue. LLVM and Binaryen did the compiling.
- Bellinge model and rain data: the Bellinge open data set (Pedersen and co-authors, DTU), used only for the measurements; it is not embedded.
- html2canvas 1.4.1 (Niklas von Hertzen, MIT) and gif.js 0.2.0 (Johan Nordberg, MIT) are embedded for the GIF button.
- Sample and corpus models: Robert Dickinson, SWMMBobSWMM6/1729-SWMM5-Models-2030.
- App and patch: Robert Dickinson, SWMM Enablement. No restriction beyond those above.

## AI use

This app, the fast engine inside it and this write-up were built with Claude, Anthropic's AI model, in two sessions on 10 and 11 November 2026, at the direction of Robert (Bob) Dickinson. He set the goal (speed up the WebAssembly SWMM5 engine, starting from a poster of compiler stages), supplied the model corpus and asked for the race app. Responsibility for publishing and using it is his.

What Claude did: it assembled the Emscripten toolchain, chose the benchmark models from his 1729 corpus, profiled the engine, wrote the source patch (fastio.h and changes to five SWMM source files), the post-link script, the build and benchmark scripts, the number self-test, this page, its figures and this text, and ran every measurement quoted here.

How the results were checked: the checks are mechanical. They are byte comparison of .out and .rpt files on 1,156 models, a differential test of the number routines against the C library, interleaved timings, and a headless Chrome run of this page. No person has yet reviewed the patch line by line, run this page in Firefox or Safari, or repeated the timings on another machine.

## Changes

- 1.0.0 (2026-11-11): first version. Race, My Bench, About and Doc tabs; three samples; fast engine build of 2026-11-10.
