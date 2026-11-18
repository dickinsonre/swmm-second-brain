---
title: "S214: Lead Pump Pointer, summary written from the page (v1.1)"
type: source
raw: raw/apps/lead-pump-pointer-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-03
ingested: 2026-11-17
tags: [apps, swmm5, pumps, controls, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Lead Pump Pointer, version 1.1: a three-pump lift station run through EPA SWMM 5.2.4 in the browser under six control rules (five through SWMM's step API, one in plain [CONTROLS] text), with pumps knocked out at bad moments, to test whether a lead-pump pointer changes the result. Raw file: [raw/apps/lead-pump-pointer-v1.1.md](../../raw/apps/lead-pump-pointer-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793665898-26b1, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app and its document were built with Claude in one session in November 2026 under Bob's direction: Bob supplied the graphic (Modular Residue Recurrence Generating Pairs), asked for the pump use to be built and supplied the outside review behind 1.1, which was itself AI-assisted (its links point to ChatGPT). Claude compiled the engine without changing the solver, designed the test station and wrote the controller and tests.

**Claims worth keeping** (all copied from the file)
- The plain station: Pump 1 starts at 6 ft, Pump 2 at 7 ft, Pump 3 at 8 ft, all stop at 3 ft; a week of sewage with one storm. SWMM 5.2.4 reports Pump 1 starting 704 times and running 53.7 hours, Pump 2 18 times, Pump 3 3 times.
- The pointer barely changes how high the water gets but decides who collects the starts: fixed lead puts 679 starts on P1 and none on P3; the ring gives 254/255/183, with P3 out for 36 hours.
- With P3 cut to 70 % of its curve, rotation by cycle gives 223/223/221 starts but 20.2/19.3/29.3 run hours: equal starts leave the weak pump running most.
- The rule that starts the pump idle longest, readable in SWMM rules since Build 5.1.010, and the ring rule give byte-identical .out files in dry weather: rotation with no register in any SWMM 5 copy.
- Eleven checks, of repeatability, implementation agreement and logic, none physical. The WebAssembly .out matches a native gcc build byte for byte (2,661,597 bytes); with no outage the three pointer rules give byte-identical .out files.
- Engine: the USEPA v5.2.4 tag, commit 7952ca837988b1c32f791812eccc9fd64547e093, no solver changes, clang 18.1.3 and wasi-libc plus two small stubs.
- Version 1.1 answers an outside review of 1.0 (77 of 100): the dry-weather pattern averaged 0.965 in 1.0, so 0.6 cfs was really 0.579 cfs; it now averages 1.0 and all stored results were rerun.

**Limits it states.** One synthetic station with no field data. Pumps start instantly. Starts and hours are counts, not a measure of wear.

**Checked at ingest.** 0.6 x 0.965 = 0.579 cfs. The engine commit is the v5.2.4 tag commit given for the swmm5-ruby reference copy in [S204](S204-note-two-pipe-benchmark-step1-run.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://lead-pump-pointer.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Lead Pump Pointer (app)](../entities/lead-pump-pointer.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
