---
title: The missing specification
type: concept
updated: 2026-11-14
sources: [S04, S10, S11, S22]
tags: [documentation, swmm5, swmm6]
reviewed: 2026-11-15
---
Four of the ten problems in [S22](../sources/S22-li-ten-problems.md) are one problem: there has never been a written, testable statement of what the engine does and how to read what it prints [S22](../sources/S22-li-ten-problems.md).

| Problem in [S22](../sources/S22-li-ten-problems.md) | What it says |
|---|---|
| 1. The code was the specification | For most of SWMM5's life the only exact statement of what it computed was the C source. The reference manuals came out between 2015 and 2017, more than ten years after SWMM 5.0 |
| 2. Results moved between releases with no public yardstick | Release notes said what changed in the code, not how much results changed. Public regression testing came late in the 5.1 line |
| 8. Reports invite the wrong comparison | See [Reading SWMM output](reading-swmm-output.md) |
| 9. The real teaching lived in forums and people's heads | Between the source and the GUI help sat the useful middle, held on SWMM-USERS, OpenSWMM.org and SWMM5.org, searchable but not organized |

**Evidence from the forum.** "Where is the theory?" tags 86 of Bob's 2,879 thread titles and "Version churn and release bugs" 152 [S10](../sources/S10-openswmm-top25-problems.md).

**Bob's qualification.** He has "always said" that the EPA manuals by Lew Rossman were "fantastic and almost a work of engineering art" [S22](../sources/S22-li-ten-problems.md), and in 2017 called them the best software documentation in the world [S11](../sources/S11-li-my-history-with-swmm.md).

**What would close it, per [S22](../sources/S22-li-ten-problems.md).** A specification; a shared model set; a certify step. "A specification, a shared model set like your 1,729-model corpus, and a certify step would fix more of this list than any new solver." Bob's comment: "One can hope."

**Shared model sets have their own defects.** In the OWA corpus, 20 of 151 files failed on shape spellings that hid two further layers of errors (F-0002), and one benchmark harness silently skipped 57 uppercase `.INP` files (F-0004); both are unconfirmed until rerun [S04](../sources/S04-findings-register-seed.md).

**Relation to this wiki.** Problem 9 describes the forum and blog material as "searchable but not organized" [S22](../sources/S22-li-ten-problems.md). Organizing it is what this repository is for.

See [The top 25 problems in 31 years of forum threads](forum-problems-top-25.md), [Lewis A. (Lew) Rossman](../entities/lew-rossman.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md).
