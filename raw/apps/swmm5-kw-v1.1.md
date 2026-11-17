---
name: swmm5-kw
file: swmm5-kw.html
version: "1.1"
date: 2026-11-10
written: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/QaFtX92xbzLnarHpToK5UC", repo: "https://github.com/SWMMBobSWMM6/swmm5-kw"}
engines:
  - {name: EPA SWMM, version: 5.2.4, source: "USEPA/Stormwater-Management-Model tag v5.2.4 (commit 7952ca8)", license: public domain}
  - {name: swmm5-kw, version: "1.1", source: "SWMMBobSWMM6/swmm5-kw (kwmod.c plus changes to flowrout.c, toposort.c, node.c and swmm5.c)", license: not stated in the page}
units: "model units; the page's results are in cfs and ft"
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page's own AI-use note says the extension, the page, its tests and the Doc essay were made with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/QaFtX92xbzLnarHpToK5UC, version 1794347262-6e96 (index.html, 2,525,018 bytes, SHA-256 6cf90a37f79075e52f30d9ff093682fb58f7527f7813023e4c062fd4bf07edbb), its About and Doc tabs read in headless Chromium on 2026-11-16. No model was run to write this file."
---

# swmm5-kw: kinematic wave and steady flow that split a junction and run a loop

## In three points
- **What:** EPA SWMM 5.2.4 whose kinematic wave and steady flow routing split a junction among several outlets (instead of ERROR 133) and run directed loops (instead of ERROR 131).
- **So what:** On split.inp the HEAD rule sends 73.8% of the flow down the big pipe against 71.3% under dynamic wave, and 352 of the 357 corpus KINWAVE or STEADY models gave .out files identical to stock byte for byte in all four runs.
- **Now what:** Use it to route splits and loops where stock stops. It cannot represent backwater, surcharge or reverse flow, and a loop pipe that would run backwards is wrong in direction.

This summary was written after the fact. The page ships no technical summary of its own. The version, 1.1, is the page's own ("What changed in 1.1"); the date is the date of the published version read. Every number below is copied from the page's About tab or its Doc essay. No engine was run to write this file.

## What it does

swmm5-kw is EPA SWMM 5.2.4 with one change in purpose: kinematic wave and steady flow routing no longer stop at a junction with several outlets (ERROR 133) or at a directed loop (ERROR 131). A split junction shares its outflow among its outlets by one of three rules (HEAD, AREA, CAPACITY); a loop is iterated within each routing step until the flow coming back around settles. Dynamic wave is untouched, and with both options off the engine is stock 5.2.4. The page runs two engines compiled to WebAssembly from the same source tree: stock EPA SWMM 5.2.4 from the official v5.2.4 tag, and the same tree with the extension.

The page warns: results from swmm5-kw with either option on are not stock EPA SWMM results. Its report says so in a KW/SF extension block.

## How it computes

- HEAD, the default rule, finds the one junction water level y at which the outlets together carry exactly what came in: each outlet sees y less its own offset, carries the Manning flow at that normal depth, and is capped at its full-flow capacity; y is found by bisection, in 22 to 31 halvings on average in the test runs. Water beyond the sum of the capacities stays in the junction and ponds or floods. The page calls HEAD "an allocation at normal depth." CAPACITY shares by what each pipe could carry flowing full; the page names AREA as the third rule. The page does not give the AREA formula in the sections read.
- A loop is iterated within each routing step until the returning flow settles.
- Open decisions listed on the page: a runtime switch (today) or an [OPTIONS] keyword such as NODE_SPLIT NONE|HEAD|AREA|CAPACITY; a version stamp such as 5.2.4-kw; HEAD or AREA as the default rule (the first ask was AREA); whether apps start with the extension on while the engine defaults to off.

## Results the page reports

- split.inp (one 3 ft pipe carrying 20 cfs into a junction with a 3.0 ft and a 1.5 ft outlet, both 400 ft): HEAD sends 73.8% down the big pipe; dynamic wave sends 71.3%. Dynamic wave drives 5.73 cfs through the 1.5 ft pipe, about 9% beyond the 5.25 cfs it carries flowing full by gravity. CAPACITY sends 86.4% down the big pipe.
- diamond.inp and braid.inp: every pipe's peak flow within 1.8% of dynamic wave; within 4.3% on split.inp.
- Steady flow with HEAD: routing continuity error 0.000% on split.inp; kinematic wave 0.131%, against 0.124% for stock kinematic wave on a plain three-pipe chain at 30 cfs.

## Checks (as stated on the page)

- Corpus gate (1729-SWMM5-Models-2030, commit 9ee63bd): 3,759 models through stock 5.2.4 and swmm5-kw. The 357 KINWAVE or STEADY models ran four times (extension off, then each split rule with loops on); 352 gave a .out identical to stock byte for byte, and a report identical apart from its three clock lines, in all four runs. 3,239 dynamic-wave models ran with the extension on and were identical in 3,226 cases. Interface-file models: 159 of 163 identical. The page says not one model differed; 10 decks crash stock 5.2.4 and crash swmm5-kw at the same point; 11 could not be compared because stock never finished.
- The extension changed 1 corpus model: NCIMM_ROUTING/water.inp, which stock refuses with ERROR 131.
- What-if pass: 3,218 dynamic-wave models copied with routing switched to KINWAVE. Stock refused 925 with ERROR 133 or 131; swmm5-kw ran 234 of those to the end. The other 691 stopped on checks the extension leaves alone (ERROR 115 in 583, ERROR 139 in 357, a fork with a pump or regulator among its outlets in 323). Of the 1,412 stock could run, every one gave identical bytes from swmm5-kw; 874 stopped on an input check in both. Among the 234: median 1 split junction and 0 loop-closing links, largest 15 and 8; median continuity error magnitude 0.17%, 60 of 234 past 1%.
- The wasm engines were checked against native builds and the patch against a fresh checkout. The checks are mechanical.

## What this does not show

- That kinematic wave can represent backwater, surcharge or flow reversal. It cannot, in a split or a loop or anywhere else.
- That loop results are fit for design. Where a pipe in a loop would run backwards, the answer is wrong in direction, not just in size.
- How the three split rules compare across real networks: five small test networks were compared with dynamic wave, and the corpus contains one model the extension changes.
- That every continuity error in the what-if pass is stock behavior: the 30 largest were traced, the long tail was not.
- That the 1.1 fixes are right for every network: checked on the shipped networks, every corpus network the what-if pass routes, and junctions of up to 130 outlets.
- A Windows build: built and gated on Linux (GCC 13, musl 1.2.4) and as WebAssembly (Clang 18, wasi-libc).
- A person's line-by-line review of the C changes.

## How to reproduce

The source, the patch, the test networks (split.inp, diamond.inp, braid.inp, loop.inp, loopactive.inp and others), the gates and their logs are in SWMMBobSWMM6/swmm5-kw, with the Doc essay as dist/swmm5-kw-doc.docx. The corpus gates need SWMMBobSWMM6/1729-SWMM5-Models-2030 at commit 9ee63bd.

## Credits and licenses

The EPA Storm Water Management Model is a work of the U.S. Environmental Protection Agency, in the public domain; version 5.2.4's engine is Lewis Rossman's design. The page runs its engines with @bjorn3/browser_wasi_shim 0.4.2.

## AI use

The page says the extension, the page, its tests and the Doc essay were made with Claude, Anthropic's AI model, under the direction of Robert (Bob) Dickinson: the engine on 28 and 29 September 2026, the repository, page and essay on 29 October 2026, and engine v1.1 and the page's fixes on 31 October 2026 after an outside review. Bob asked for kinematic wave and steady flow that run loops and bifurcations, chose to keep the work in its own repository, and supplied the model corpus. This summary was written by Claude on 16 November 2026 from the published page.

## Changes

- 1.1 (2026-10-31): after an outside review of v1.0. Engine: CAPACITY and AREA kept their "outlet is full" flags in char done[64], so an outlet past the 64th was never set aside and the junction flooded; now one flag per outlet. HEAD could hand out up to 1.5e-6 cfs more than arrived; fixed. Page: results carry the run that made them; a stopped run gets a "Stopped" verdict and no export; missing values export blank, never -Infinity; peaks keep their sign; each point sits at the time stamped on it in the .out.
- 1.0: engine (28 and 29 September 2026); page and repository (29 October 2026).
