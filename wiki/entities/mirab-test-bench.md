---
title: Mirab Test Bench (app)
type: entity
updated: 2026-11-15
sources: [S71, S82]
tags: [apps, mirab, swmm5plus, swmm5, engine-comparison, findings]
reviewed: no
---
Bob's test bench for Mirab, Ehsan Madadi's free desktop application that runs EPA SWMM 5.2 and SWMM5+ in one project. Version 1.0, 24 October 2026 [S82](../sources/S82-mirab-test-bench-summary.md).

**A caution about its source.** The page ships no technical summary. [S82](../sources/S82-mirab-test-bench-summary.md) was written by Claude on 14 November 2026 from the page's source and evidence record, with nothing rerun, and Bob has not yet read it (Q52).

**What it does.** It reads the `.anr` results files Mirab writes, reruns the same `.inp` through EPA SWMM 5.2.4 compiled into the page, and measures the gap. Where the engines should be identical it tests bit parity. Where they solve differently (SWMM5+) it reports each element's divergence as a share of that element's own peak. It does not run SWMM5+, which is Fortran with no known working path to WebAssembly [S82](../sources/S82-mirab-test-bench-summary.md).

**Versions tested** [S82](../sources/S82-mirab-test-bench-summary.md): Mirab 0.2.4; swmm5plus-capi 0.2.1; SWMM5+ 1.0.3 from CIMM-ORG/SWMM5plus; EPA SWMM 5.2.4.

**Result 1: Mirab's EPA engine is the EPA engine.** A native build, Mirab's library and the page's WebAssembly agree bit for bit on every `.anr` value of three samples: 7,200, 42,048 and 18,432 values [S82](../sources/S82-mirab-test-bench-summary.md).

**Result 2: a census that separated WebAssembly from the math library.** Of 449 `.inp` files, 59 gave different `.out` files in the page than in a native glibc build. All 59 matched a native build linked against musl. See [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).

**Result 3: SWMM5+ against EPA SWMM 5.2.4** [S82](../sources/S82-mirab-test-bench-summary.md)

| Sample | Link flow, median peak change |
|---|---|
| Urban | 0.42 % |
| Long Beach sewer | 27.81 % |
| Long Beach with a dummy first pattern | 0.34 % |
| Quality | 0.17 % |

**Its findings register** [S82](../sources/S82-mirab-test-bench-summary.md)

| ID | Status in the page | Finding |
|---|---|---|
| S-1 | Confirmed by experiment | SWMM5+ dry-weather inflow ignores the first pattern in `[PATTERNS]`: `interface/api.c:399` tests `if (jj > 0)` while EPA numbers patterns from 0. It explains the Long Beach row above |
| S-2 | Found by reading; not run | The weekend pattern multiplies the hourly one |
| S-3 | Measured | SWMM5+ interpolates inflow boundaries linearly |
| S-4, S-5 | Open: needs SWMM5+ review | An outfall face depth that disagrees with its own area; a node that reaches 7.65 ft (2.332 m) where EPA peaks at 0.95 ft (0.289 m); feet are a conversion made by the summary |
| C-1, C-2 | Confirmed | What the `.anr` node depth is, and a unit factor of 1.00011 |
| M-1 | Confirmed | Mirab's SWMM5+ output folder lands beside the work folder |
| P-1 | Confirmed | `realpath()` writes into a 260-byte buffer in EPA SWMM 5.2.4 |
| P-2 | Confirmed | EPA 5.2.4's answer depends on the math library on some models |

P-1 names the buffer that the translators of the engine found separately, as defect 3 of [SWMM Engines, Byte for Byte (app)](swmm-engines-byte-for-byte.md) [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md).

**What it does not show.** Three small circular-pipe dynamic-wave models. No observed flows, so nothing says which engine is more accurate. No person has reviewed the register against the SWMM5+, swmm5plus-capi and Mirab sources, and S-4 and S-5 have not been examined by anyone who works on SWMM5+ [S82](../sources/S82-mirab-test-bench-summary.md).

**Credits.** Mirab and swmm5plus-capi are by Ehsan Madadi, GPL-3.0-or-later; SWMM5+ is from CIMM at the University of Texas at Austin. The page says it includes none of Mirab's code and is not affiliated with those projects [S82](../sources/S82-mirab-test-bench-summary.md).

**Open.** The findings carry the page's own IDs, with no IDs in [The SWMM findings register](../concepts/findings-register.md) (Q47).
