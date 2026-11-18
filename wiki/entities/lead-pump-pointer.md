---
title: "Lead Pump Pointer (app)"
type: entity
updated: 2026-11-17
sources: [S204, S205, S214]
tags: [apps, swmm5, pumps, controls, wasm]
reviewed: no
---
Bob's app Lead Pump Pointer: a three-pump lift station run through EPA SWMM 5.2.4 in the browser under six control rules (five through SWMM's step API, one in plain [CONTROLS] text), with pumps knocked out at bad moments, to test whether a lead-pump pointer changes the result. Version 1.1, 2026-11-03 [S214](../sources/S214-lead-pump-pointer-summary.md). Netlify address: https://lead-pump-pointer.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S214](../sources/S214-lead-pump-pointer-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S214](../sources/S214-lead-pump-pointer-summary.md)
- The plain station: Pump 1 starts at 6 ft, Pump 2 at 7 ft, Pump 3 at 8 ft, all stop at 3 ft; a week of sewage with one storm. SWMM 5.2.4 reports Pump 1 starting 704 times and running 53.7 hours, Pump 2 18 times, Pump 3 3 times.
- The pointer barely changes how high the water gets but decides who collects the starts: fixed lead puts 679 starts on P1 and none on P3; the ring gives 254/255/183, with P3 out for 36 hours.
- With P3 cut to 70 % of its curve, rotation by cycle gives 223/223/221 starts but 20.2/19.3/29.3 run hours: equal starts leave the weak pump running most.
- The rule that starts the pump idle longest, readable in SWMM rules since Build 5.1.010, and the ring rule give byte-identical .out files in dry weather: rotation with no register in any SWMM 5 copy.
- Eleven checks, of repeatability, implementation agreement and logic, none physical. The WebAssembly .out matches a native gcc build byte for byte (2,661,597 bytes); with no outage the three pointer rules give byte-identical .out files.
- Engine: the USEPA v5.2.4 tag, commit 7952ca837988b1c32f791812eccc9fd64547e093, no solver changes, clang 18.1.3 and wasi-libc plus two small stubs.
- Version 1.1 answers an outside review of 1.0 (77 of 100): the dry-weather pattern averaged 0.965 in 1.0, so 0.6 cfs was really 0.579 cfs; it now averages 1.0 and all stored results were rerun.

**What it does not show.** One synthetic station with no field data. Pumps start instantly. Starts and hours are counts, not a measure of wear. [S214](../sources/S214-lead-pump-pointer-summary.md)

**Noted at ingest.** 0.6 x 0.965 = 0.579 cfs. The engine commit is the v5.2.4 tag commit given for the swmm5-ruby reference copy in [S204](../sources/S204-note-two-pipe-benchmark-step1-run.md).

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
