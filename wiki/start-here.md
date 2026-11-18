---
title: Start here
type: synthesis
updated: 2026-11-17
sources: [S187, S192, S45, S165, S87, S23, S204]
tags: [handoff, reading-path, reproduction]
reviewed: no
---
This wiki is a record of Bob Dickinson's work comparing SWMM5, SWMM6, ICM and the engines around them. In his words: "i am doing this to make model comparisons and not be a writer - the simulatons are the whole point" [S187](sources/S187-note-model-comparison-purpose-and-dogfooding.md). This page is for someone arriving without him. It says how to read a claim, gives four first tasks that each end in something you have done, and says where the working materials are.

## How to read a claim (not in the sources: the rules this repository keeps)

- Every fact ends in a link to a source page, and every source page links its raw file. Follow the chain back before you rely on a number.
- A finding carries its source's own status: `unconfirmed`, `confirmed`, `fixed` or `disproven`. Only a rerun or Bob changes it.
- A Relations row says `verification: run`, `pending` or `documented`: a run backs it, a test is planned, or only a document says so.
- `drafted_by:` on a source page names who drafted it, often an AI. That is disclosure, not a defect. What gives a claim weight is the run behind it.
- `reviewed:` is the date Bob read the page; `no` means he has not.
- [Open questions](open-questions.md) lists where sources disagree. Until an item is ticked, neither side is settled.

## Four first tasks

**1. Modeler: rerun one of EPA's 2006 test models and flip one flag.**
Read [Continuity is not validation](concepts/continuity-is-not-validation.md) and [Weirs and outlets](concepts/weirs-and-outlets.md). Then take EXTRAN4 from OpenWaterAnalytics/swmm-nrtestsuite, commit e609fdbb, and run it in EPA SWMM 5.2.4 with the 2006 report's options: `INERTIAL_DAMPING NONE`, `NORMAL_FLOW_LIMITED SLOPE`, `LENGTHENING_STEP 0`, `MIN_SURFAREA 0`, `MAX_TRIALS 4`, `VARIABLE_STEP 0.00`, `THREADS 1` [S192](sources/S192-swmm-qa-report-bench-app-md.md).
Done when node 82309 peaks at 12.03 ft with the weir's surcharge flag YES (the default), and at 20.28 ft with it NO. EPA's 2006 figure shows 14.21 ft [S192](sources/S192-swmm-qa-report-bench-app-md.md). The reference build was 5.2.4 from tag v5.2.4 with gcc 13.3.0 at `-O2`; another build can differ in the last digits (see [WebAssembly builds against native builds](concepts/wasm-against-native-builds.md)).

**2. Developer: check one translated engine against EPA, byte for byte.**
Read [Byte-for-byte gate](concepts/byte-for-byte-gate.md) and the README of SWMMBobSWMM6/swmm5-ruby [S45](sources/S45-swmm5-ruby-readme.md). Run one model with `ruby/runswmm model.inp model.rpt model.out` under Ruby 3.3.6 ([raw README](../raw/ports/2026-11-09-swmm5-ruby-README.md)), and the same model in EPA 5.2.4 built from the v5.2.4 tag with gcc 13.3 at `-O2` on x86-64 Linux [S45](sources/S45-swmm5-ruby-readme.md).
Done when the `.out` files are byte-identical and the `.rpt` files match except the "Analysis begun on", "Analysis ended on" and "Total elapsed time" lines, the pass rule of every port README [S45](sources/S45-swmm5-ruby-readme.md). The models are the gate set of [the corpus](entities/corpus-1729.md) [S23](sources/S23-swmm6-csharp-readme.md).

**3. ICM user: run the two-pipe benchmark in ICM.**
Read [ICM Ruby: UI and Exchange](concepts/icm-ruby-ui-and-exchange.md) and [Checking a SWMM5 model's conversion into ICM](concepts/swmm5-to-icm-conversion-checks.md). The benchmark is one small model: two junctions and a free outfall at inverts of 100, 99 and 98 ft, two 12 in conduits 200 ft long at n 0.013, an inflow at the first junction rising to 1.0 cfs at 20 minutes and back to 0 at 30, one hour, results every minute. Step 1 runs it in EPA 5.2.4 and swmm5-ruby; steps 2 and 3 in ICM SWMM and ICM InfoWorks [S165](sources/S165-note-epa-swmm-ruby-icm-benchmark.md).
Step 1 has been run: EPA 5.2.4 and swmm5-ruby wrote byte-identical results, with the outfall peaking at 0.9665 cfs at minute 21 and J1 at 0.4356 ft at minute 20, and the run record lists every minute [S204](sources/S204-note-two-pipe-benchmark-step1-run.md). It holds 59 records, minutes 1 to 59, because EPA's run is one second short ([Run duration floored to whole seconds](concepts/run-duration-floor.md)).
Done when your ICM SWMM and ICM InfoWorks results for the same model are filed as a note in `raw/notes/`, set beside that table. Nobody has run steps 2 and 3, and the design was drafted by ChatGPT from Autodesk Help, not checked against ICM (Q90).

**4. Maintainer: change one page and pass the checker (not in the sources).**
`CLAUDE.md` gives the three operations. Add or correct one page from a source, run `python3 tools/lint.py`, and finish at 0 errors. How someone other than Bob records a review is not decided yet (Q105).

## Where the working materials are

This repository holds no `.inp`, `.rpt`, `.out` or `.rb` files. The models live in the public corpus, https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030 [S23](sources/S23-swmm6-csharp-readme.md); its README is [S87](sources/S87-corpus-1729-readme.md). The repositories the sources name are mapped on [Bob's GitHub repositories](entities/bobs-github-repositories.md).

The apps are the weak link. Counted by Claude from the `links:` lines of the 94 ingested summaries in `raw/apps/` on 17 November 2026: 29 name a GitHub repository or a live Netlify address; 16 name only a Claude artifact, which opens for Bob and whoever he shares it with; 49 name neither. So from this repository alone a successor can reach 29 of the 94 apps (Q104).

## What Bob has not written down yet

Which findings he trusts most and why; which results are promising but unsettled; what he checks first when a model looks wrong; which project or version to start from; and a failure that taught him something the final result hides (Q106). Three pages say what they lack: [subcatchment width](concepts/subcatchment-width.md) a worked sensitivity and Bob's proposed alternative, [RDII](concepts/rdii-unit-hydrographs.md) how InfoSWMM and ICM treat it, and [calibration](concepts/calibration-validation-uncertainty.md) a calibration of a real catchment.
