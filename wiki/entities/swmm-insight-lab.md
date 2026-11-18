---
title: "SWMM Insight Lab (app)"
type: entity
updated: 2026-11-18
sources: [S311]
tags: [apps, swmm5plus, fortran, dependency-graph, audits]
reviewed: no
---
Bob's app SWMM Insight Lab: a map of the SWMM5+ engine and its relation to EPA SWMM 5.1.13. Version 1.0.0, 2026-10-25 [S311](../sources/S311-swmm-insight-lab-summary.md). Its `links:` line names no live Netlify address [S311](../sources/S311-swmm-insight-lab-summary.md).

**A caution about its source.** The page ships no technical summary. [S311](../sources/S311-swmm-insight-lab-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S311](../sources/S311-swmm-insight-lab-summary.md)
- Maps CIMM's SWMM5+ hydraulics engine at commit afd44de: its folder tree, its Fortran module graph, the papers behind it, its relation to the EPA SWMM 5.1.13 C code it links, a C-port scaffold, and the seven query tools of the original Lovable build (subtitle: SWMM5+ Repo Explorer). The Lovable README described a different app, a Mars settlement model; the code was this explorer.
- Re-running the module extraction matched the Lovable data on 71 of 71 module declarations and 534 of 534 edges, and found 4 repeated use statements it had dropped. But 27 of the curated dependency edges do not exist in the source. The audit register holds 24 entries (broken, wrong, missing, unverified, improvement).
- Cloned CIMM-ORG/SWMM5plus at afd44de and confirmed CIMM-ORG/SWMM5plus-1 points at the same commit.
- Module extraction re-run with the same regular expressions: 71 of 71 declarations and 534 of 534 edges match; 4 dropped use statements found.
- All 23 EPA counterpart files exist in both v5.1.13 and master; every named EPA function grepped in the 5.1.13 tree.
- Curated dependency edges checked against the source: 27 do not exist.

**How to use it, as the summary puts it.** Use it to find your way around SWMM5+ and its EPA counterparts. It shows what static reading can measure: there is no call graph, no speed on N processors, and no accuracy against EPA SWMM; the module summaries and relation labels are a person's reading, unchecked. [S311](../sources/S311-swmm-insight-lab-summary.md)

**What it does not show.** As the page lays out: judgment, not checked (relation labels, unflagged module summaries, paper-to-module links, the subsystem of each folder, which EPA file is "nearest"); and outside what static reading can do (the call graph, speed on N processors, accuracy against EPA SWMM). [S311](../sources/S311-swmm-insight-lab-summary.md)

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [SWMM5+ (CIMM finite-volume engine)](swmm5plus.md), [SWMM5+ Repo Explorer (app)](swmm5plus-repo-explorer.md).
