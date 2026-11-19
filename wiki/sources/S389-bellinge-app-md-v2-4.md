---
title: "S389: Bellinge, app .md (v2.4)"
type: source
raw: raw/apps/bellinge-v2.4.md
kind: app-md
author: Robert Dickinson
published: 2026-11-19
ingested: 2026-11-19
tags: [apps, swmm5, swmm6, swmm4, extran, engine-comparison, bellinge, wasm]
drafted_by: Claude (Anthropic), with the app
reviewed: no
---
**What it is.** The technical summary that now ships with the Bellinge app, version 2.4 (19 November 2026). It replaces [S81](S81-bellinge-summary.md), the summary of version 2.0 written from the page, as the current source for the app. Raw file: [raw/apps/bellinge-v2.4.md](../../raw/apps/bellinge-v2.4.md).

**How it was written.** By Claude (Anthropic), in the session of 19 November 2026 that revised the app, under Bob's direction. The AI-use section: the app was built with Claude in Claude Code sessions on 17 and 18 October 2026 and revised on 19 November; Bob "chose the project, the engines, the dataset and the scenario families" and is responsible for the work. "The October source tree was lost with its sandbox and recovered by Claude from the published page; no person has yet reviewed the November revision."

**Claims worth keeping** (all copied from the file)
- The same seven engines as 2.0, now with their commits: EPA SWMM 5.2.4 at 7952ca83; OpenSWMM 6.0.0-alpha.1 at 74ef6e27, alpha.2 at 0df29948, alpha.3 at 86c28a88, and swmm6_rel at 3c30f1e6 (2026-10-17); SWMM 4.4H (2004); EXTRAN III (April 1981), as printed and with bugs fixed.
- 42 scenarios, 33 of them pre-run; a catalogue of 30 model changes in 5 families.
- SWMM6 DW mode forces DYNWAVE and adds SURCHARGE_METHOD DYNAMIC_SLOT, NODE_CONTINUITY SEMI_IMPLICIT and ANDERSON_ACCEL. alpha.1 skips DYNAMIC_SLOT because it initialises the dynamic-wave solver before setting the surcharge method (Routing.cpp lines 243 to 249 of the tag). FV mode is for alpha.3 and later. EPA SWMM 5.2.4 rejects all three keywords (ERROR 205) and runs only as written.
- EXTRAN III's 1981 limits: 187 junctions and links, and 99,999 steps (NTCYC read with FORMAT I5). A longer run is cut to a window around its largest runoff peak, and a larger network is cut to one outfall's branch for every engine in the comparison.
- The 29 June 2012 storm on the G60K220 branch, unchanged from 2.0: flooding nodes 127 / 18 / 111 / 130 and outfall peak 42.6 / 42.6 / 36.5 / 40.0 cfs for SWMM 5.2.4 as written / swmm6_rel SWMM6 DW / SWMM 4.4H / EXTRAN III bugs fixed; routing continuity -0.61 / 0.14 / -9.2 / -3.3 per cent.
- The 48-hour base run on the whole model: flooding nodes 466 (5.2.4), 643 (alpha.1 DW, runoff continuity -43.9 per cent), 62 (alpha.2 DW), 62 (alpha.3 DW), 61 (swmm6_rel DW) and 520 (swmm6_rel FV); routing continuity 0.35 / -0.38 / 2.79 / 1.64 / 0.09 / -0.79 per cent; wall time 2.5 / 25.8 / 12.8 / 11.6 / 14.4 / 99 min.
- EXTRAN III's window on the 48-hour run: 03:46 to 17:36 on 29 June, 76 per cent of the runoff, continuity -4.6 per cent, 143 flooding manholes against 126.
- The 29 June 2012 event carries 0.764 and 0.929 in of rain at the two gauges (19.4 and 23.6 mm; conversion ours).
- The comparison takes peaks from the engines' own .rpt summaries where present, else from the .out.
- Tests: the October tree and its 51 checks were lost; this build has 16 Node checks and 19 headless-Chromium checks, the latter rerunning the 29 June 2012 branch storm through four engines and reproducing the October numbers. The pre-run results and the recorded base run are the October files, unchanged.
- Four defects worked around, not fixed: D1, alpha.1's slot allocated after the solver starts; D2, alpha.1's 43.9 per cent runoff loss; D3, EXTRAN III as printed never lets a closed rectangle run full (HYDRAD label 180); D4, EXTRAN III as printed lets a free-surface junction head rise above ground (TRANSX lines 199 to 200).
- Complexity 70.3 on the HydroCouple = 100 scale (Size 63.1, Structure 75.1, Test evidence 28.5, SWMM vocabulary 94.5; meter 1.7.0); the shipped page alone 66.5.
- 2.4 restructured the Doc tab and .docx to Bob's documentation rules, wrote and embedded this .md, and made the byline "the author alone (AI use stated in its own section)".

**Limits it states.** "Agreement between engines is not correctness": the dataset's 13 level meters and its flow meter are not in the page. The Fortran engines run conversions of the file. The recorded base run keeps time series as 10-minute frames quantised to a byte. OpenSWMM 6 is alpha. "The comparison metric decides the answer." No person has reviewed the November revision or compared any run with a desktop SWMM run of the same file.

**Checked at ingest.** 19 + 12 + 20 = 51, the October test count S81 gave (ours). The 48-hour figures that S81 gave (466, 62, 62, 61 and 520 flooding nodes, 99 min for finite volume, 2.79, 1.64 and 0.09 per cent) agree; alpha.1's 643 nodes and -0.38 per cent, 5.2.4's 0.35 per cent, finite volume's -0.79 per cent and the other wall times are new here. The `links:` line gives Netlify as "none yet"; a project named bellinge-swmm5-swmm6 was on Bob's Netlify team when it was read through his connector at ingest, and the file does not name it (Q127). The file's byline change answers part of Q53.

**Feeds:** [Bellinge (app)](../entities/bellinge-app.md), [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md), [App complexity index (HydroCouple = 100)](../concepts/app-complexity-index.md), [EXTRAN](../entities/extran.md).
