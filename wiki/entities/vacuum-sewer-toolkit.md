---
title: "Vacuum Sewer Toolkit (app)"
type: entity
updated: 2026-11-18
sources: [S340]
tags: [apps, vacuum-sewers, epa-1991, icm, ruby]
reviewed: no
---
Bob's app Vacuum Sewer Toolkit: EPA 1991 vacuum sewer design and InfoWorks ICM Ruby, corrected. Version 1.0, 2026-10-25 [S340](../sources/S340-vacuum-sewer-toolkit-summary.md). Its `links:` line names no live Netlify address [S340](../sources/S340-vacuum-sewer-toolkit-summary.md).

**A caution about its source.** The page ships no technical summary. [S340](../sources/S340-vacuum-sewer-toolkit-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S340](../sources/S340-vacuum-sewer-toolkit-summary.md)
- A single-file rebuild of Bob's Lovable app vcruby (126 files, 27 feature screens, 19,586 lines of TypeScript and 508 of Ruby by its own count): vacuum sewer design after the EPA 1991 manual and published state criteria, calculators, diagrams, components, comparisons with gravity, costs, and InfoWorks ICM Ruby scripts. The three ICM scripts are replaced by four corrected ones.
- The corrections register lists 35 entries (code 9, method 2, contradiction 4, number 6, practice 1, table 1, removed 5, physics 3, label 3, unsupported 1). The worst (C1): for a 320 m to 330 m guide the original sawtooth generator made inverts of 320, 319, 332, 329 and 330, one 13 m lift and 14 m of rise from a single pipe, three times the whole 13 ft (3.96 m) static budget. The engine passes 86 of 86 checks, the corrected Ruby 15 of 15 in a stand-in ICM, and both exported .inp files run clean in SWMM 5.2.
- Engine vac.js: 86 of 86 checks pass.
- Corrected ICM Ruby: 15 of 15 in a stand-in ICM harness; the original scripts were also run in that harness.
- SWMM 5.2 (pyswmm 2.2.0, toolkit 0.17.0) ran both exported .inp files with no errors or warnings; continuity error 1.60% (demo) and 0.15% (sawtooth).
- Published criteria looked up: WEF (via PDHengineer), Florida DEP, Texas 217.98, EPA 1991; the Innovyze examples.

**How to use it, as the summary puts it.** Use it to lay out a vacuum main and its lifts, and to take the design into ICM. Friction is single-phase Hazen-Williams (the AIRVAC two-phase charts are not reproduced), no script has run inside ICM, and costs are the original's 1990 unit costs times an inflation factor. [S340](../sources/S340-vacuum-sewer-toolkit-summary.md)

**What it does not show.** As the page lists it: friction is single-phase; the two-phase correction uses a correlation built for steady separated flow in straight pipe, while a vacuum main runs in slugs and the multiplier depends heavily on the air assumed; no script has run inside ICM; costs are 1990 unit costs times an inflation factor. The demo network is synthetic. [S340](../sources/S340-vacuum-sewer-toolkit-summary.md)

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [Sewer Science (app)](sewer-science.md), [InfoWorks ICM](infoworks-icm.md).
