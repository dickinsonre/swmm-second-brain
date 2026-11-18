---
title: "Inside hydrocouple.platform (app)"
type: entity
updated: 2026-11-17
sources: [S205, S259]
tags: [apps, hydrocouple, swmm6, platform, findings]
reviewed: no
---
Bob's app Inside hydrocouple.platform: an explainer of the hydrocouple.platform repository (commit 3d7d3a1) read from source: its architecture, how a run moves through it, its rules, SWMM packaging and AI agents, with a numbered register of ten findings, each with its source lines. The platform itself was not run. Version 1.1, 2026-10-24 [S259](../sources/S259-inside-hydrocouple-platform-summary.md). Netlify address: https://inside-hydrocouple-platform.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S259](../sources/S259-inside-hydrocouple-platform-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S259](../sources/S259-inside-hydrocouple-platform-summary.md)
- The page's JavaScript ports of the platform's rules pass 64 of 64 checks against the platform's own tests; 0 of the platform's 78 tests were run.
- Findings by severity for a SWMM user: 2 Gap, 2 Design note, 3 Info, 3 Limit.
- F1: the packaging scanner does not see the detailed report file a [LID_USAGE] line can name (field 9), so that path is left as the author wrote it; EPA 5.2.4 opens the file and stops with ERROR 305 if it cannot. F2: the GUI scanner the platform copies has the same omission.
- F3: original file paths reach the control plane under every egress policy. F4: HydroCouple's run-1.0 schema cannot catalogue SWMM's .out and .rpt. F5: the engine's licence now differs by branch.
- The page reports that the platform keeps customer keys with the customer and serves private and on-premises sites with outbound traffic only, through one code path.

**What it does not show.** Every finding is read from source; none was run. Nothing after commit 3d7d3a1. [S259](../sources/S259-inside-hydrocouple-platform-summary.md)

**Noted at ingest.** 2 + 2 + 3 + 3 = 10 findings. F5, the licence by branch, is the matter of Q83.

See [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [OpenSWMM 6 and HydroCouple](openswmm-6-and-hydrocouple.md), [HydroCouple Interactive (app)](hydrocouple-interactive.md), [LID bio-retention layers](../concepts/lid-bioretention-layers.md).
