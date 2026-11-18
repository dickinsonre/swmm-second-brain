---
name: Rule 110 in SWMM5
file: rule110-swmm5.html
version: 1.0.0
date: 2026-11-09
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/6XhL4jerEu7WQmPcYnFPZu", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4 (stock), source: "SWMMBobSWMM6/swmm5-kw build, wasm/swmm524.wasm, 840,503 bytes, SHA-256 9714657c0306f5673e287dbd1f71f371f8f3285fa8ad5542f0285db33f7f455f", license: public domain}
units: US customary (ft, ft2, cfs); the model uses FLOW_UNITS CFS
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app and its essay were built with Claude at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/6XhL4jerEu7WQmPcYnFPZu, version 1794321164-8899 (index.html, 3,337,610 bytes, SHA-256 46c150d475aaad48f2582d505bc44b0ede75786886e3cf953a480155847113f9), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# Rule 110 in SWMM5: an elementary cellular automaton computed by EPA SWMM 5.2.4 with water

## In three points
- **What:** The app writes an unmodified EPA SWMM 5.2.4 model whose storage nodes are the cells of any of the 256 elementary cellular automata, runs it in the browser, and checks every cell against the automaton.
- **So what:** In the default run (Rule 110, 48 cells, 40 generations) all 1,968 cells read from the .out match, and eight automata from seven rules matched in 10,700 of 10,700 cells in both native and browser engines.
- **Now what:** Use it to see SWMM's control rules, storage nodes and orifices doing exact work, and where they break. It exercises no conduits or dynamic wave, and the finite tape runs Rule 110 without proving anything about it.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v1.0.0, 9 November 2026"). Every number below is copied from the page's About tab or its Doc essay. No model was run to write this file.

## What it does

It writes a SWMM5 input file for any elementary rule, on a tape of 8 to 96 cells, for up to 80 generations, runs it in the browser with a WebAssembly build of EPA SWMM 5.2.4, reads every cell back from the binary .out, and compares each one with the automaton computed directly. Nothing in SWMM is patched. The idea came from an infographic that claimed eight bits of rule make a universal machine and printed them as 0 1 1 0 1 1 0 0, which is Rule 108, not Rule 110. Tabs: Machine, Inside, Rules, Predict, Verify, About, Doc.

## How it computes

- Cell: a storage node of 1,000 ft2 plan area, floor at 20 ft, 6 ft deep. It reads 1 when its depth is above a 2 ft read line.
- Write: a pump from a common tank to the cell, Type 3 curve, flat at 0.5 cfs; a rule stops it at 4 ft. Write time t = h A / Q = 4 ft x 1,000 ft2 / 0.5 cfs = 8,000 s, about 133 minutes.
- Erase: a 6 in orifice, Cd 0.65, at the cell floor, draining freely to the tank; about 166 minutes from 4 ft to below 0.04 ft.
- Tank: 25 times the plan area of all cells, with a spillway weir at 11 ft that a correct run never uses.
- Clock: SIMULATION CLOCKTIME. A day holds two generations in four 6-hour phases (write B from A, erase A, write A from B, erase B). Generation k is read at elapsed hour 12k + 3.
- Logic: one fill rule per cell per bank, written as a product of sums of the neighbours' states.

## Results the page reports

- Default run: Rule 110, 48 cells, 40 generations from a single cell at the right end; 20.25 simulated days at a 60 s routing step, 29,160 steps; native EPA SWMM 5.2.4 about 2 s, the browser about 3 s. 1,968 cells read, 0 disagreements.
- Noise margin in the default run: every 1 stood at 4.020 ft or more at its read hour, every 0 at 0.0043 ft or less.
- Mass: initial and final stored volume both 165.375 ac-ft; routing continuity error 0.000%; spillway flow zero.
- Rule 108 (the infographic's bits) from a single cell does nothing; from a random row it locks into a period-two cycle by generation 2. Rule 110 never repeats. Both match their automata in every cell.
- Pump sweep: the write pump must lift at least 2 ft x 1,000 ft2 / 21,600 s = 0.0926 cfs. At 0.1 cfs written cells reach 2.16 ft and every cell is right; at 0.09 cfs 513 of 1,968 cells are wrong; at 0.095 cfs none.
- Orifice sweep: at 0.15 ft diameter every cell is right (worst 0 cell held 1.06 ft); at 0.1 ft 342 cells are wrong. Routing steps of 30, 60 and 120 s all give every cell right with zero continuity error.

## Checks (as stated on the page)

- Logic: 773 checks pass, including all 256 rules against an independent table lookup, Rule 90 against Pascal's triangle mod 2, Rule 30's centre column against OEIS A051023, and the rule text parsed back and evaluated in SWMM's order in all 36,864 cell-and-neighbourhood cases.
- Engine: eight automata from seven rules (110, 30, 90, 108, 54, 150, 184) ran in native EPA SWMM 5.2.4 from the v5.2.4 tag and in the browser build; all 10,700 cells matched in both, and the two engines' results were byte-identical in every case.
- Readers: the .out and .rpt readers are translations of swmmrr/outfile.py and swmmrr/rptfile.py; on four runs they agree with the Python originals bit for bit across 1,944 report periods.
- Two side findings: the bundled @bjorn3/browser_wasi_shim 0.4.2 grows files to their exact size on every write; a twelve-line patch that doubles the buffer cut the default run from 14.4 s to 3.5 s with a byte-identical .out. Native Linux EPA SWMM 5.2.4 aborts with "buffer overflow detected" on a relative input path when fortify checks are on (getAbsolutePath in swmm5.c, realpath into a 260-byte buffer).
- The checks are mechanical. No person had reviewed the essay or the hydraulic design when this version was published.

## What this does not show

- It is not a universal computer: the tape has at most 96 cells with fixed or wrapped edges.
- SWMM is not a sensible way to compute: a generation takes 12 simulated hours, about 700 cells a second in the browser.
- One hydraulic design; other designs would have other edges.
- No conduits, dynamic-wave momentum, surcharge or ponding: every link is a pump, an orifice or the one weir.
- Only EPA SWMM 5.2.4 was run.

## How to reproduce

Open the page, pick a rule on the Machine tab, set the tape, and press Run in SWMM. Export gives the .inp, .rpt, .out and CSV files. The Verify tab reruns the logic checks in the browser. The default model is rule 110, 48 cells, 40 generations, .inp SHA-256 739207e9b5fe... as printed in the page's citation block.

## Credits and licenses

EPA SWMM 5.2.4 (US EPA, public domain), run by kwengine.js from SWMMBobSWMM6/swmm5-kw. @bjorn3/browser_wasi_shim 0.4.2 (MIT OR Apache-2.0). Readers translated from SWMMBobSWMM6/swmm-run-record-repo. Sources named: Cook (2004), Universality in Elementary Cellular Automata, Complex Systems 15(1); Lukyanov's water integrator (1936); Phillips's MONIAC (1949).

## AI use

The page says the app and its essay were built with Claude, Anthropic's AI model, in a Claude session on 9 November 2026, at the request of Robert (Bob) Dickinson, who asked whether the infographic was of use, chose the idea of running Rule 110 inside a SWMM5 model, and asked for it to be built. Claude designed the hydraulic machine, wrote the generator, the readers, the page, its tests, the figures and the text, and found the two side issues. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0.0 (2026-11-09): first version.
