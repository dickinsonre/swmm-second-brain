---
name: SWMM5+ Bench
file: swmm5plus-bench.html
version: "1.0"
date: 2026-10-24
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/F3RiZ6wq7cFxMJKiEZXiQ6", repo: none named in the page}
engines:
  - {name: SWMM5+, version: 1.0.3, source: "CIMM-ORG/SWMM5plus @ afd44de (2024-11-25) through Ehsan Madadi's swmm5plus-capi v0.2.1 (linux-x86_64, interface version 2, EPA SWMM 5.1.13 parser); recorded runs, and a Live bridge for a local library", license: "SWMM5+ public domain (Unlicense); swmm5plus-capi GPL-3.0-or-later"}
  - {name: EPA SWMM, version: 5.2.4, source: "tag v5.2.4 (7952ca8), src/solver compiled with wasi-sdk 25 to a wasm32-wasi reactor, one patch (mkstemp)", license: public domain}
units: the .inp's own; a US/SI toggle converts for display only
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/F3RiZ6wq7cFxMJKiEZXiQ6, version 1792869902-f990 (index.html, 2,375,794 bytes, SHA-256 20c93aaa6495e1adcfdb6131a0c44dc2ca41582edb8b3c8c37fdb65ddc536820), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# SWMM5+ Bench: SWMM5+ 1.0.3 and EPA SWMM 5.2.4 side by side on one model

## In three points
- **What:** Runs one SWMM model through two dynamic-wave engines and shows where they differ: CIMM's finite-volume SWMM5+ 1.0.3 through Ehsan Madadi's swmm5plus-capi C interface, and EPA SWMM 5.2.4 compiled into the page; 34 models recorded.
- **So what:** On EXTRAN4 EPA floods 178 ac-ft (15.0% of inflow) at two nodes that SWMM5+ treats as faces that cannot flood, a weir-crown setting explains another gap (peaks within 1.9% once both use the same formula), and SWMM5+ needs a mean step of 0.119 s and 241,021 steps for eight hours.
- **Now what:** Use it to see where the two engines part company and why before choosing one. The SWMM5+ runs are recorded (or loaded through the Live bridge on your own machine), and neither engine is checked against field data.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); the date is the recorded runs' (October 24 2026). The file name above is ours. Every number below is copied from the page. No model was run to write this file.

## What it does

SWMM5+ is about 88,000 lines of modern Fortran built around coarrays and HDF5, usually run in a container. swmm5plus-capi builds it as an ordinary shared library for Windows, macOS and Linux; the page uses Ehsan's release binaries unmodified. Tabs: Run, C API, Compare, Findings, Live bridge, About, Doc. Windows users can load the matching swmm5plus_capi.dll through the Live bridge (the kit's s5p_bridge.py).

## Results the page reports

- EXTRAN4 as shipped: EPA floods 178 ac-ft (21.9 ha-m), 15.0% of the inflow, at two nodes (an upstream end and a node with two links); in SWMM5+ both are faces and cannot flood.
- Weir control: changing one weir's Surcharge flag from NO to YES gives both engines the same equivalent-orifice formula above the crown, and the weir peaks come back within 1.9%.
- Example 1 at five-minute reporting: the SWMM5+ record shows 279,414 ft3 of lateral inflow and 294,105 ft3 of outflow (5.3% more out than in); subtracting the 14,421 ft3 that subcatchment 8 sends straight to outfall 18 closes the budget to 0.1%.
- SWMM5+ is explicit: on EXTRAN4 a mean step of 0.119 s and 241,021 steps for eight hours.

## Checks (as stated on the page)

- The four Linux files of the v0.2.1 release match the SHA-256 values in its SHA256SUMS.
- The page's EPA engine: .out byte-identical to native on 32 of 33 models.
- Byte comparison across builds and versions, determinism repeats, and one-flag control runs; findings D-1 and D-3 traced to the source lines quoted.
- 34 models recorded on Linux x86-64 (2 cores), October 24 2026, through s5p_run.py, the driver the bridge uses.

## What this does not show

- Which engine is right on a real system: no field data.
- SWMM5+ does not run in the browser; its results are recorded runs or the Live bridge on your machine.

## How to reproduce

Open the page; Run and Compare use the recorded runs and the in-page EPA engine. The kit's s5p_run.py and swmmc_run.py rerun them; the Live bridge runs SWMM5+ locally.

## Credits and licenses

swmm5plus-capi and Mirab, copyright 2026 Ehsan Madadi, GPL-3.0-or-later. SWMM5+ by CIMM (public domain, Unlicense). EPA SWMM (public domain). The bridge scripts (s5p_bridge.py, s5p_run.py, swmmc_run.py) are GPL-3.0-or-later to match the library they drive. Test models include Ehsan's catchments.inp and extran4.inp and SWMM5+'s test_cases/Example1.inp.

## AI use

The page says it was built with Claude, Anthropic's AI model, in a Claude session on October 24, 2026, at the request of Robert (Bob) Dickinson, who chose the subject, pointed at Ehsan Madadi's repositories, and set the standing rules (US units, dark default, Doc tab, disclosure, Corinne-type testing). Claude downloaded and checksum-checked the release libraries, wrote the Python driver and the local bridge, compiled EPA SWMM 5.2.4 natively and to WebAssembly, wrote the readiness checker, the .out reader, the comparison code, the page and its essay, ran every model in both engines, and traced the findings to source. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-10-24): first version.
