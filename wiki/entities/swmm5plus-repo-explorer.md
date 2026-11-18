---
title: "SWMM5+ Repo Explorer (app)"
type: entity
updated: 2026-11-18
sources: [S310]
tags: [apps, swmm5plus, fortran, repositories]
reviewed: no
---
Bob's app SWMM5+ Repo Explorer: the SWMM5+ source at afd44de, with its links to EPA SWMM 5.1.13 checked. Version 1.0.0, 2026-10-25 [S310](../sources/S310-swmm5plus-repo-explorer-summary.md). Its `links:` line names no live Netlify address [S310](../sources/S310-swmm5plus-repo-explorer-summary.md).

**A caution about its source.** The page ships no technical summary. [S310](../sources/S310-swmm5plus-repo-explorer-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob marked it reviewed on 18 November 2026 (Q116, settled).

**What the summary says** [S310](../sources/S310-swmm5plus-repo-explorer-summary.md)
- The explorer from Bob's Lovable project swmm-insight-lab, rebuilt as one HTML file that runs offline, with every count re-extracted from the SWMM5+ source at commit afd44de. It adds the main program as a source unit, use, intrinsic statements, the Fortran source itself (all 85 files in the eight source folders, embedded and searchable), procedure counts, links pinned to a commit, corrected C paths and function names, a checked paper list and a findings register. (SWMM Insight Lab is a second single-file edition of the same Lovable project.)
- None of the Lovable build's runtime links to the EPA C code resolved. SWMM5+ downloads EPA SWMM v5.1.13 (CMakeLists.txt lines 82 to 85), whose engine sits in src/; EPA moved it to src/solver/ after 5.1.13, and the Lovable table wrote every C path in the new layout while pinning the link to the old tag. Also, 27 of 130 curated edges have no use statement behind them; the edition keeps them, drawn dashed.
- Module and use extraction re-run with a corrected pattern; procedures counted.
- Every cited C path listed in both EPA trees and every cited function grepped in v5.1.13.
- Paper citations checked against publisher pages by a Claude sub-agent.
- Lovable build against this edition on four measures: Fortran source units, use statements recorded, C links resolving at v5.1.13, curated edges backed by a use.

**How to use it, as the summary puts it.** Use it to browse SWMM5+ and its EPA counterparts offline. The graph is the use graph (which module may see which), not a call graph; nothing runs SWMM5+ or EPA SWMM; the C scaffold's stubs compile because they are empty. [S310](../sources/S310-swmm5plus-repo-explorer-summary.md)

**What it does not show.** As the page lists it: the use graph is not a call graph, and shows no coarray traffic between images or calls into the C engine; nothing runs SWMM5+ or EPA SWMM, so no claim about accuracy, speed or stability is tested; the C scaffold translates nothing; module summaries and C relation labels come from the Lovable build, and only the Findings items were checked line by line; the source is one commit. [S310](../sources/S310-swmm5plus-repo-explorer-summary.md)

**Noted at ingest.** It is a second single-file edition of the Lovable project swmm-insight-lab, the same project as [SWMM Insight Lab (app)](swmm-insight-lab.md); the two editions are kept as two pages because they hold different apps.

See [Apps summarized on 18 November 2026: SWMM6, SWMM5+ and solvers](../concepts/apps-from-pages-swmm6-solvers-and-swmm5plus.md), [SWMM5+ (CIMM finite-volume engine)](swmm5plus.md), [SWMM5+ Explorer (app)](swmm5plus-explorer.md).
