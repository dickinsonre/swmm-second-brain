---
title: "SWMM Rhythm Detector (app)"
type: entity
updated: 2026-11-17
sources: [S205, S216]
tags: [apps, swmm5, pumps, output, findings, aliasing]
reviewed: no
---
Bob's app SWMM Rhythm Detector: an app that reads an EPA SWMM 5.2.4 .out and looks in every link flow and node depth for a steady beat, then names its cause from the .rpt and .inp (pump cycle, control rule, daily pattern, rain interval) or flags it as unexplained; no engine runs in the page. Version 1.0, 2026-11-06 [S216](../sources/S216-swmm-rhythm-detector-summary.md). Netlify address: https://swmm-rhythm-detector.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S216](../sources/S216-swmm-rhythm-detector-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S216](../sources/S216-swmm-rhythm-detector-summary.md)
- A beat is listed at an autocorrelation score of 0.6 and a swing of 2 % of peak over at least three cycles, and called strong at 0.8 and 5 %. Flows below 0.035 cfs (1 L/s) and depths below 0.04 in (1 mm) are not analysed.
- Pump start-ups and the flow instability index follow EPA's stats.c: index = turns x 100 / (2/3 x (periods - 2)); a start-up is pump flow rising above 0.001 cfs.
- With every routing step saved and the step fixed, the .out count of start-ups equals EPA's for 36 of 37 links across eight runs; the exception is off by a fraction because the .out stores 32-bit flows.
- Aliasing: a looped force main from the NCIMM training models (Session 52) has a pump EPA counted starting 237 times in four hours; the .out reported every five minutes shows 11 and a false 25-minute beat.
- EPA report defect: report.c line 994 tests the worst link's index rather than whether the list is empty, so when the least stable link is the first in the file (index 0) the report says "All links are stable." Reproduced in Cycling_pumps with its orifice moved to the top (index 106.5), Driveway.inp (6.2) and treatment.INP (3.0); the same test guards the nonconverging-node list.
- Corpus: 138 runs analysed as saved; 22 with at least one strong rhythm; 89 report every 15 minutes or longer, too coarse to see anything faster than half an hour; only 2 report every routing step with the step fixed. Of the 14 runs with an unexplained rhythm, 12 report less often than every second routing step.
- 14 unit tests pass; two calm models run three ways gave no strong rhythms.

**What it does not show.** "Unexplained" does not prove a numerical fault and "explained" does not prove a pump cycle is acceptable. Nothing faster than two reporting steps can be seen. The thresholds were set by trying them on these models; there is no labelled set. Counts match EPA SWMM 5.2.4 only. No person has reviewed the 14 unexplained runs. [S216](../sources/S216-swmm-rhythm-detector-summary.md)

**Noted at ingest.** The report.c defect is a new entry for [The SWMM findings register](../concepts/findings-register.md), at the page's word: Claude found it and reproduced it on three models; no person has checked it against the code, and it is not reported to EPA in the summary.

See [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md), [The SWMM findings register](../concepts/findings-register.md), [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [Reading SWMM output](../concepts/reading-swmm-output.md), [1729-SWMM5-Models-2030 (the corpus)](corpus-1729.md).
