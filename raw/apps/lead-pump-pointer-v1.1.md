---
name: Lead Pump Pointer
file: lead-pump-pointer.html
version: "1.1"
date: 2026-11-03
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/J2hKHtscj4FPvVaNCpRRGH", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA v5.2.4 tag, commit 7952ca837988b1c32f791812eccc9fd64547e093, no solver changes, compiled to WebAssembly with Ubuntu clang 18.1.3 and wasi-libc plus two small stubs", license: public domain}
units: US customary (ft, cfs, MG, hours)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app and its document were built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/J2hKHtscj4FPvVaNCpRRGH, version 1793665898-26b1 (index.html, 3,120,406 bytes, SHA-256 e51fe89aab70fef63f7fad73d95ef29684e46185060ad7999227237ffd118370), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file; the date is the artifact's publish date."
---

# Lead Pump Pointer: lead-pump rotation through an outage, in the real SWMM 5.2.4 engine

## In three points
- **What:** A three-pump lift station run through EPA SWMM 5.2.4 in the browser under six control rules (five through SWMM's step API, one in plain [CONTROLS] text), with pumps knocked out at bad moments, to test whether a lead-pump pointer changes the result.
- **So what:** The pointer barely changes how high the water gets but decides who collects the starts: fixed lead puts 679 starts on P1 and none on P3, the ring gives 254/255/183, and with P3 at 70% capacity equal starts (223/223/221) still leave the weak pump running most (20.2/19.3/29.3 hours).
- **Now what:** Rotate by hours, not cycles, if you want equal run time; the plain-text rule that starts the pump idle longest gives rotation with no register in any SWMM 5 copy. One synthetic station, no field data, and pumps start instantly.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.1"); the date is the artifact's. The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. No model was run to write this file.

## What it does

The idea came from a graphic titled Modular Residue Recurrence Generating Pairs: a pointer stepping around a list whose length changes. Here the list is the pumps in service and the pointer picks the lead pump. The plain station: Pump 1 starts at 6 ft, Pump 2 at 7 ft, Pump 3 at 8 ft, all stop at 3 ft, a week of sewage with one storm; SWMM 5.2.4 reports Pump 1 starting 704 times and running 53.7 hours, Pump 2 18 times, Pump 3 3 times. The app reports peak depth, flood volume, starts, run hours, pumped volume and longest run for each pump under each rule. Tabs: Station, Replay, Pointer, Sweep, Verify, About, Doc.

## Results the page reports

- Fixed lead: 679 starts on P1, none on P3. Ring: 254/255/183 (P3 was out for 36 hours).
- P3 cut to 70% of its curve: rotation by cycle gives 223/223/221 starts but 20.2/19.3/29.3 run hours.
- Least hours rule: counts each pump's run time in whole routing steps; the available pump with the fewest goes next, ties to the lowest number.
- The idle-time rule (readable in SWMM rules since Build 5.1.010) and the ring rule give byte-identical .out files in dry weather.

## Checks (as stated on the page)

Eleven checks, by kind (repeatability, implementation agreement, logic; no physical validation). Among them:
- V1: the WebAssembly .out matches a native gcc build byte for byte (2,661,597 bytes).
- V2: the same input twice gives the same .out.
- V3: with no outage the three pointer rules give byte-identical .out files.
- V4: the step loop changes nothing the stock rules would not (238/237/237 starts).
- V5: two counts of the same pump agree: starts within 1, hours within 0.01 h, volume within 0.001 MG.
- V6: every window of the graphic checked: 2 of 8 windows dropped; 2 of 30 printed transitions leave p >= m, 0 after the repair.
- V7: the repaired rules hold under random abuse (no out-of-range pointer, no invalid lead, no pump running while out of service).

## What this does not show

- One synthetic station with no field data.
- Pumps start instantly.
- Starts and hours are counts, not a measure of wear.

## How to reproduce

Open the page, set the station and outage on Station, run each rule, and compare on Pointer and Sweep; Replay shows the reason for each controller action. The PySWMM script and a bundle are written from the scenario for 2, 3 or 4 pumps.

## Credits and licenses

EPA SWMM 5.2.4 (public domain). No license is stated for the page.

## AI use

The page says the app and its document were built with Claude, Anthropic's AI model, in one session in November 2026, under the direction of Robert (Bob) Dickinson, who supplied the graphic, asked for the pump use to be built, and supplied the outside review behind v1.1. Claude compiled the engine without changing the solver, designed the test station, and wrote the controller, the page, the PySWMM script, the tests and all the text. The outside review was itself AI-assisted (its links point to ChatGPT); Claude checked its findings against the code and the engine. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1: answers an outside review of v1.0 (77 of 100): every result owns its scenario; one engine job at a time; the dry-weather pattern now averages 1.0 (in v1.0 it averaged 0.965, so 0.6 cfs was really 0.579 cfs; all stored results rerun); Replay tab; Least hours rule; scenario save and load.
- 1.0: first version.
