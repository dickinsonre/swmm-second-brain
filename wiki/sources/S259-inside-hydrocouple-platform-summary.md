---
title: "S259: Inside hydrocouple.platform, summary written from the page (v1.1)"
type: source
raw: raw/apps/inside-hydrocouple-platform-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-17
tags: [apps, hydrocouple, swmm6, platform, findings]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Inside hydrocouple.platform, version 1.1: an explainer of the hydrocouple.platform repository (commit 3d7d3a1) read from source: its architecture, how a run moves through it, its rules, SWMM packaging and AI agents, with a numbered register of ten findings, each with its source lines. The platform itself was not run. Raw file: [raw/apps/inside-hydrocouple-platform-v1.1.md](../../raw/apps/inside-hydrocouple-platform-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792870243-3a22, reading its Findings and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude (Claude Opus 5.5) in October 2026 at Bob's request; Bob chose the subject and supplied the outside review that shaped 1.1. Claude read the repository and the related EPA SWMM 5.2.4, OpenSWMM engine and GUI sources and wrote JavaScript ports of the platform's rules. The page has no About tab.

**Claims worth keeping** (all copied from the file)
- The page's JavaScript ports of the platform's rules pass 64 of 64 checks against the platform's own tests; 0 of the platform's 78 tests were run.
- Findings by severity for a SWMM user: 2 Gap, 2 Design note, 3 Info, 3 Limit.
- F1: the packaging scanner does not see the detailed report file a [LID_USAGE] line can name (field 9), so that path is left as the author wrote it; EPA 5.2.4 opens the file and stops with ERROR 305 if it cannot. F2: the GUI scanner the platform copies has the same omission.
- F3: original file paths reach the control plane under every egress policy. F4: HydroCouple's run-1.0 schema cannot catalogue SWMM's .out and .rpt. F5: the engine's licence now differs by branch.
- The page reports that the platform keeps customer keys with the customer and serves private and on-premises sites with outbound traffic only, through one code path.

**Limits it states.** Every finding is read from source; none was run. Nothing after commit 3d7d3a1.

**Checked at ingest.** 2 + 2 + 3 + 3 = 10 findings. F5, the licence by branch, is the matter of Q83. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://inside-hydrocouple-platform.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [Inside hydrocouple.platform (app)](../entities/inside-hydrocouple-platform.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md), [HydroCouple Interactive (app)](../entities/hydrocouple-interactive.md), [LID bio-retention layers](../concepts/lid-bioretention-layers.md).
