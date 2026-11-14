---
name: Mirab Test Bench
file: mirab-test-bench.html
version: 1.0
date: 2026-10-24
written: 2026-11-14
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/Mmdfj6RVuBY7zEYHrWTBDX", netlify: "https://mirab-testing-companion.netlify.app (not read for this summary; it may serve another build)", repo: none recorded in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model @ 7952ca8 (tag v5.2.4)", license: public domain, use: "runs in the page as wasm32-wasi; the reference"}
  - {name: SWMM5+, version: 1.0.3, source: "CIMM-ORG/SWMM5plus @ afd44de, with EPA SWMM 5.1.13 for input and hydrology", license: Unlicense, use: "not run in the page; its results arrive as Mirab .anr files"}
  - {name: Mirab, version: 0.2.4, source: "ehsanMa86/Mirab @ c9029ef (2026-10-24), headless build (mirab-cli)", license: GPL-3.0-or-later, use: "wrote the .anr files; none of its code is in the page"}
  - {name: swmm5plus-capi, version: 0.2.1, source: "ehsanMa86/swmm5plus-capi @ eb05b4d (2026-10-23), gfortran 13.3, interface v2", license: GPL-3.0-or-later, use: "the interface Mirab runs SWMM5+ through"}
units: each model's own flow units (two samples in CMS, one in CFS). Differences are shares of each element's own peak. Where the page gives a depth in meters, feet are given first and the conversion is this summary's.
ai_use: the app was built with Claude (Anthropic). This summary was written by Claude from the page's source. See AI use.
written_from: "the published artifact's page source, its About tab, its findings register and its embedded evidence record (generated 2026-10-24T19:17:45Z), read on 2026-11-14. No engine was run and no test was rerun to write this file."
---

# Mirab Test Bench: Mirab's .anr results against EPA SWMM 5.2.4 running in the page

This summary was written after the fact. The page carries no technical summary of its own. Every number below is copied from the page's embedded evidence record (`script#evidence`), its findings register or its About tab. Nothing here was measured again. The page records no file name; `mirab-test-bench.html` is taken from its title.

## What it does

It is a test bench for Mirab, Ehsan Madadi's free desktop application that runs EPA SWMM 5.2 and SWMM5+ (and the EPANET engines) in one project. The bench reads the `.anr` results files Mirab writes, reruns the same `.inp` through EPA SWMM 5.2.4 compiled into the page, and measures the gap. Where the engines should be identical it tests bit parity. Where they solve differently (SWMM5+) it reports per-element divergence as a share of each element's own peak, with the worst instant and the change in peak kept apart.

It does not run SWMM5+. The About tab says SWMM5+ is Fortran built on coarrays, HDF5 and json-fortran, with no known working path to WebAssembly.

Tabs named in the page: Bench, Findings, Files, About, Doc.

## How it computes

- The page's engine: EPA SWMM 5.2.4 built with clang 18, `--target=wasm32-wasi -O2 -ffp-contract=off`, as a reactor. Two libc stand-ins (`mkstemp`, `realpath`). An in-memory WASI file system written for the bench.
- All seven upstream source archives reproduced the SHA-256 values pinned in Mirab's and swmm5plus-capi's CMake files.
- For an EPA `.anr`: every stored value is compared with the page's own run, bit for bit.
- For a SWMM5+ `.anr`: only the common report times are compared (the SWMM5+ file has one more period than EPA's in each sample). For each element the page computes the worst instant, the average and the peak change, each divided by that element's peak. Elements whose peak is under a floor are dropped.

## Results as stored

**Parity, EPA engine (native build = Mirab's library = this page's wasm).**

| Sample | `.out` bytes | `.anr` values bit-equal |
|---|---|---|
| mirab-urban | 29,908 | 7,200 of 7,200 |
| mirab-longbeach-sewer | 170,875 | 42,048 of 42,048 |
| mirab-quality | 75,459 | 18,432 of 18,432 |

**Census of 449 `.inp` files from the SWMM5+ repository's test folders, native glibc build against the page's engine.** 380 gave byte-identical `.out` files. 59 differed. 10 were rejected by both. All 59 were rerun with a native build linked against musl, and 59 of 59 matched the page byte for byte. The register concludes the cause is the math library (glibc against musl, which wasi-libc inherits), not WebAssembly. Across the 59, the median worst relative difference in link flow or node depth is 6.44e-08, 15 are above 1 % and 11 above 10 %. The largest stored is 2.3141 (relative), on `test_notSync/user3/user3_tallManholes_noStorage.inp`.

**SWMM5+ against EPA SWMM 5.2.4.** Stored as fractions of each element's peak; shown here as percent to two decimals.

| Sample | Units, common periods | Links compared | Link flow, worst instant: median | max | Link flow, peak change: median | max | Node depth, worst instant: median |
|---|---|---|---|---|---|---|---|
| Urban | CMS, 72 | 5 | 2.27 % | 3.03 % | 0.42 % | 0.71 % | 52.46 % |
| Long Beach sewer | CFS, 192 | 16 (2 under the floor) | 38.30 % | 38.81 % | 27.81 % | 28.52 % | 26.83 % |
| Long Beach, dummy first pattern | CFS, 192 | 16 (2 under the floor) | 19.95 % | 21.09 % | 0.34 % | 1.07 % | 13.88 % |
| Quality | CMS, 144 | 5 | 2.49 % | 4.22 % | 0.17 % | 2.36 % | 56.82 % |

The sample models: urban has 5 circular conduits and 3 subcatchments; Long Beach has 18 circular conduits, 9 dry-weather inflows and one pattern (`WW_PAT1`); quality has 5 circular conduits, 3 subcatchments, 1 dry-weather inflow and one pattern (`Hourly1`). All three use dynamic wave routing and have no storage and no other link types.

## Findings register, as stored

| ID | Kind, severity | Status in the page | Finding |
|---|---|---|---|
| S-1 | defect, high | Confirmed by experiment | SWMM5+ dry-weather inflow ignores the first pattern in `[PATTERNS]`. `interface/api.c:399` tests `if (jj > 0)`, while EPA numbers patterns from 0 and uses -1 for none. On Long Beach every conduit's SWMM5+ peak is 25 to 29 % low and the outlet sits at 1.2476 cfs for 48 h, the sum of the nine baselines. With an all-ones dummy pattern placed first, EPA's `.out` is byte-identical to before and the SWMM5+ peak change falls to a median of 0.34 % (max 1.07 %). |
| S-2 | defect, medium | Found by reading; not run | The weekend DWF pattern multiplies the hourly one instead of replacing it. No sample model has a weekend pattern. |
| S-3 | behaviour, info | Measured; documented in source | SWMM5+ interpolates inflow boundaries linearly, so hourly steps become ramps. With S-1 worked around, the worst-instant difference stays near 20 % of peak. |
| S-4 | open, medium | Open: needs SWMM5+ review | At outfall O1 of the urban model at 1:00, the SWMM5+ face depth disagrees with its own area: depth 0.741 ft (0.225877 m) with area 0.271978 m², where EPA reports 1.437 ft (0.438 m). |
| S-5 | open, medium | Open: needs SWMM5+ review | In the quality model the upstream end J1 reaches 7.65 ft (2.332 m) above invert in SWMM5+ and peaks at 0.95 ft (0.289 m) in EPA. |
| C-1 | docs, low | Confirmed | The `.anr` node depth is the junction-main element; SWMM5+'s own node CSV is a different number, up to 4.4 % (urban) and 6.6 % (quality) of peak away. |
| C-2 | note, info | Confirmed; correct as designed | In SI models the `.anr` flow and volume are EPA's CMS, about 0.011 % above SWMM5+'s own SI files. EPA converts with 0.02832 m³/ft³; SWMM5+ and the C interface use 0.0283168466. The page's ledger gives the factor as 1.00011. |
| M-1 | defect, low | Confirmed | The SWMM5+ output folder lands beside the work folder, not inside it (`Mirab src/cli/main.cpp:815` with `SWMM5+ utility/utility_files.f90:660`). Results are not affected. |
| P-1 | defect, low | Confirmed | In EPA SWMM 5.2.4 `swmm5.c`, `realpath()` writes into a 260-byte buffer. The register notes that Mirab already works around it. |
| P-2 | note, info | Confirmed | On some models EPA 5.2.4's answer depends on which math library rounds it (the census above). |

The fix the register proposes for S-1 is to change `jj > 0` to `jj >= 0`.

## Checks

Mechanical, from the page's ledger and About tab:

- Byte comparison of `.out` files across three builds (native, Mirab's library, wasm) on the three samples.
- Bit comparison of every `.anr` value (table above).
- Repeat runs: the page's engine wrote byte-identical `.out` files on repeat runs of every sample.
- Null control on Mirab's input edits: EPA 5.2.4 on Mirab's prepared file, with INERTIAL_DAMPING put back, gives hydraulics identical to the original, bit for bit.
- The page's JavaScript comparison code against an independent Python reader: 3 models by 2 variables, every distribution number identical.
- `.anr` structural audit: 7 Mirab `.anr` files, all checks pass.

Human review: none recorded.

## What this does not show

From the page:

1. No observed flows, so nothing says which engine is more accurate.
2. Three small circular-pipe dynamic-wave models. No storage, pumps, weirs, orifices or other shapes were compared.
3. SWMM5+ is not run in the browser.
4. No speed claims.
5. S-2 was found by reading and has not been run.
6. No person has reviewed the findings register against the SWMM5+, swmm5plus-capi and Mirab sources. S-4 and S-5 have not been examined by anyone who works on SWMM5+.

Added by this summary:

7. This file was written from the page, not from the build. No stored result was rerun.
8. The page records no file name and no repository of its own.
9. The findings have the page's own IDs (S, C, M, P). This summary does not map them to any other register.

## How to reproduce

Open the artifact. On the Bench tab pick a sample (each is one of Mirab's own SWMM examples with the `.anr` files Mirab 0.2.4 wrote), let the reference run, and choose the Mirab result and variable. For S-1: "Long Beach sewer (US, DWF)", compare SWMM5+, then "Long Beach, dummy first pattern". To check this summary, view the page source and read the `evidence` script element and the `findings` function.

## Credits and licenses

- Mirab and swmm5plus-capi: Copyright 2026 Ehsan Madadi, GPL-3.0-or-later. The bench reads Mirab's documented file format and includes none of Mirab's code.
- SWMM5+: CIMM, University of Texas at Austin (Unlicense).
- EPA SWMM: U.S. EPA, public domain. The engine in the page is built from the unmodified EPA sources.
- The page says it is not affiliated with or endorsed by the U.S. EPA, CIMM or the Mirab project.

## AI use

From the page's About tab: the bench was built with Claude, Anthropic's AI model, in a Claude session in October 2026, under the direction of Robert (Bob) Dickinson, who asked for a test bench for Mirab, chose EPA SWMM 5.2.4 and SWMM5+ as its engines and is responsible for the work. Claude built Mirab and swmm5plus-capi from source, ran Mirab's three SWMM examples through both engines, compiled EPA SWMM 5.2.4 to WebAssembly, wrote the readers and the comparison code, traced S-1 to its line and ran the dummy-pattern experiment, wrote the findings register, drew the figures and wrote the Doc essay and the page. The checks are mechanical. Not yet checked by a person: the findings register against the sources, and S-4 and S-5.

This summary: written by Claude (model claude-fable-5-2) on 14 November 2026 at Bob's request, from the page source only. Bob has not yet read it.

## Changes

- `1.0 (2026-10-24)`: the build this summary describes. The page records no change history.
