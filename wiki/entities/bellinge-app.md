---
title: Bellinge (app)
type: entity
updated: 2026-11-15
sources: [S74, S81]
tags: [apps, bellinge, swmm5, swmm6, swmm4, extran, engine-comparison]
reviewed: 2026-11-15
---
Bob's app that runs one open Danish sewer model, with its rain record and a set of scenarios, through seven SWMM engines in the browser. Version 2.0, 18 October 2026 [S81](../sources/S81-bellinge-summary.md).

**A caution about its source.** The page ships no technical summary. [S81](../sources/S81-bellinge-summary.md) was written by Claude on 14 November 2026 from the page's source, build record and essay, with nothing rerun, and Bob has not yet read it (Q52).

**The data.** The open Bellinge model, the combined sewer of a district of Odense, Denmark: 1,020 nodes, 1,044 links and 713 subcatchments, with rain from two gauges over June 2009 to August 2021. Published by Nedergaard Pedersen and others (2021) in Earth System Science Data 13, 4779-4798, under CC BY 4.0 [S81](../sources/S81-bellinge-summary.md).

**The seven engines** [S81](../sources/S81-bellinge-summary.md)

| Engine | Runs |
|---|---|
| EPA SWMM 5.2.4 | the scenario's `.inp` as written |
| OpenSWMM 6 at alpha.1, alpha.2, alpha.3 and swmm6_rel | the same file as written, or with SWMM 6 dynamic wave options, or (alpha.3 on) finite volume |
| SWMM 4.4H | a deck converted from the file, Runoff feeding Extran |
| EXTRAN III (1981), as printed or bugs fixed | a converted deck, fed the runoff 4.4H computed |

It joins two earlier apps, Bellinge Explorer and Seven SWMM Engines. One model of the user's own can be run in place of Bellinge [S81](../sources/S81-bellinge-summary.md).

**Scenarios.** 42 are offered: a 48-hour base run, the 29 June 2012 storm, six top storms, a custom window and 33 pre-run model changes from a catalogue (climate factor, a design storm from the record's own IDF, roughness, upsized pipes and others) [S81](../sources/S81-bellinge-summary.md).

**What the engines said: the 29 June 2012 storm on one branch** [S81](../sources/S81-bellinge-summary.md)

| Engine | Flooding nodes | Routing continuity | Peak at the outfall |
|---|---|---|---|
| EPA SWMM 5.2.4, as written | 127 | -0.61 % | 42.6 cfs |
| OpenSWMM swmm6_rel, SWMM 6 dynamic wave | 18 | 0.14 % | 42.6 cfs |
| SWMM 4.4H | 111 | -9.2 % | 36.5 cfs |
| EXTRAN III, bugs fixed | 130 | -3.3 % | 40.0 cfs |

The branch is used because EXTRAN III refuses the whole model: its 1981 limit is 187 junctions and links, and the branch has 159 nodes and 167 links. EXTRAN III as printed diverges on it; the essay traces that to the hydraulic-radius routine that never lets a closed rectangle run full, one of the ten faults listed on [EXTRAN III Workbench (app)](extran-iii-workbench.md) [S81](../sources/S81-bellinge-summary.md), [S74](../sources/S74-extran3-workbench-app-md.md).

**The whole model.** The 48-hour base run across four generations of OpenSWMM 6 is on [OpenSWMM 6 solvers, measured](../concepts/openswmm6-solvers-measured.md).

**What the essay concludes.** "The app does not tell you which to believe. It tells you how far apart they are" [S81](../sources/S81-bellinge-summary.md).

**What it does not show.** "Agreement between engines is not correctness." Thirteen level meters and a flow meter recorded Bellinge from 2010 to 2020; they are in the dataset and not in the page. The two Fortran engines run converted decks; see [Converting SWMM 5 models for older engines](../concepts/converting-swmm5-models-for-older-engines.md). No person has compared the runs with a desktop SWMM run node by node [S81](../sources/S81-bellinge-summary.md).

**Open.** Three small faults in the page's own text, among them an essay byline that reads "Robert Dickinson, with Claude" (Q53). See [Open questions](../open-questions.md).
