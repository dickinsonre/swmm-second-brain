---
name: SWMM Rhythm Detector
file: swmm-rhythm-detector.html
version: "1.0"
date: 2026-11-06
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/Fz5hNw3kvCxbW9HC6RtxsZ", repo: none named in the page}
engines:
  - {name: EPA SWMM, version: 5.2.4, role: "reference engine whose .out, .rpt and .inp the app reads; the page's experiments ran it through swmm-toolkit 0.17.0; no engine runs in the page", license: public domain}
units: US customary (cfs, ft, in); thresholds also given in SI
ai_use: "This summary was written by Claude (Anthropic) from the published page. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/Fz5hNw3kvCxbW9HC6RtxsZ, version 1794001004-a9f3 (index.html, 2,781,655 bytes, SHA-256 be5e1ab16478075eb0b328f15aaff37d7784e52b229431ee869de2a39d31bcd5), its About and Doc tabs read in headless Chromium on 2026-11-17. No model was run to write this file."
---

# SWMM Rhythm Detector: find the steady beats in a SWMM 5.2.4 run and name their cause

## In three points
- **What:** Reads an EPA SWMM 5.2.4 .out and looks in every link flow and node depth for a steady beat, then names its cause from the .rpt and .inp (pump cycle, control rule, daily pattern, rain interval) or flags it as unexplained.
- **So what:** Of 138 corpus runs, 22 show at least one strong rhythm and 89 report every 15 minutes or longer, too coarse to see anything faster than half an hour; it also found that EPA's report prints "All links are stable." when the least stable link is the first in the file.
- **Now what:** Run it on a model with pumps or controls, and rerun with the fine-step copy it writes when the report step is too coarse. A rhythm is a pattern, not a diagnosis, and the thresholds were set on test models, not fitted.

This summary was written after the fact. The page ships no technical summary of its own. Its version and build date are the page's own ("VERSION 1.0", "BUILT Nov 6, 2026"). The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. No model was run to write this file.

## What it does

The idea came from an infographic on monotone, repetitive rhythm that Mike sent Bob; Bob asked whether any of it applied to SWMM. In a model a steady beat is either built (a pump cycle, a daily sewage pattern, a gate on a control rule) or made by the arithmetic without asking. The app finds the beats, names the built ones, and flags the rest. When the reporting step is too coarse to see a fast rhythm, it writes a copy of the .inp that reports every routing step. Everything runs in the browser. Tabs: Detect, Pumps, Fine-step copy, Evidence, About, Doc.

## How it computes

- Period: the time between repeats. Score: autocorrelation of the step-to-step change at that period (1.0 a perfect beat, 0 none). Swing: half the 5th-to-95th percentile range after a one-period moving average removes the storm, as a fraction of peak.
- Listed at a score of 0.6 and a swing of 2% of peak over at least three cycles; strong at 0.8 and 5%. Flows below 0.035 cfs (1 L/s) and depths below 0.04 in (1 mm) are not analysed.
- Flow instability index and pump start-ups by the rules in EPA's stats.c: a turn is a change in sign of the step-to-step flow change bigger than 0.001 cfs; index = turns x 100 / (2/3 x (periods - 2)); a start-up is pump flow rising above 0.001 cfs.
- Causes are matched by period: within 15%, or twice or half a pump's start-up interval.

## Results the page reports

- Cycling_pumps.inp from the 1729 corpus: lead and lag pumps on a 25 ft2 wet well (lead on at 2.0 ft, off at 1.0 ft; lag on at 4.0 ft, off at 2.0 ft).
- Start-up counts: with every routing step saved and the step fixed, the .out count equals EPA's for 36 of 37 links across eight test runs; the exception (E1580ZDG link 254) is off by a fraction because the .out stores 32-bit flows.
- Aliasing: a looped force main from the NCIMM training models (Session 52) has a pump that EPA counted starting 237 times in four hours; the .out reported every five minutes shows 11 and a false 25-minute beat.
- EPA report defect: report.c line 994 tests the worst link's index rather than whether the list is empty, so when the least stable link is the first in the file (index 0) the report says "All links are stable." Reproduced in Cycling_pumps with its orifice moved to the top (index 106.5), Driveway.inp (6.2) and treatment.INP (3.0); the control E1580ZDG.inp lists 5 links as it should. The same test guards the nonconverging-node list.
- Corpus: 138 runs analysed as saved; 22 with at least one strong rhythm; 83 report every 15 minutes and 89 every 15 minutes or longer; only 2 report every routing step with the step fixed. Unexplained leads the kinds; 12 of those 14 runs report less often than every second routing step.

## Checks (as stated on the page)

- 14 unit tests pass.
- Two calm models (Saving_Runoff_File.inp and a two-orifice model), each run three ways: six runs, no strong rhythms. Every test run analysed twice gave the same answer.
- Start-up and turn counts compared with EPA's printed Pumping Summary and flow instability index, as above.

## What this does not show

- "Unexplained" does not prove a numerical fault, and "explained" does not prove a pump cycle is acceptable.
- Nothing faster than two reporting steps can be seen, and a coarse .out can show the alias of a faster beat.
- A rhythm at three times a pump's interval is left unexplained.
- The thresholds were set by trying them on these test models; there is no labelled set of good and bad models.
- Subcatchment results, water quality and system totals are not analysed.
- Counts match EPA SWMM 5.2.4 only; other engines and versions may count differently.
- No person has reviewed the 14 corpus runs filed as unexplained.

## How to reproduce

Run a model in EPA SWMM 5.2.4 and load its .out, .rpt and .inp on the Detect tab. Use Fine-step copy to write an .inp that reports every routing step, run it, and load the new .out.

## Credits and licenses

EPA SWMM 5.2.4 (US EPA, public domain); its stats.c and report.c rules are followed and cited. Test models from the 1729-SWMM5-Models-2030 corpus and the NCIMM training models. No license is stated in the page.

## AI use

The page says the app was built with Claude, Anthropic's AI model, in a Claude Code session in November 2026, under the direction of Robert (Bob) Dickinson, who supplied the starting idea, asked whether it had a use in SWMM, and told Claude to build the detector it had suggested, tested against short-cycling pump models such as Cycling_pumps.inp. Claude read the EPA SWMM 5.2.4 C source (stats.c, report.c, output.c), wrote the readers, the period detector, the classifier, the fine-step copy, the page, its charts and tests; ran every engine experiment in EPA SWMM 5.2.4 (swmm-toolkit 0.17.0), including the corpus census; found and reproduced the "All links are stable" defect in report.c; and wrote the Doc essay and the .docx. The thresholds were chosen by Claude on the test models. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0 (2026-11-06): first version.
