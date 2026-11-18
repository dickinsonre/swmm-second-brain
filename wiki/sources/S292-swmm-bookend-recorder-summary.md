---
title: "S292: SWMM Enablement Bookend Recorder, summary written from the page (v1.1.0)"
type: source
raw: raw/apps/swmm-bookend-recorder-v1.1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-27
ingested: 2026-11-18
tags: [apps, tools, video, gif, provenance]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app SWMM Enablement Bookend Recorder, version 1.1.0: a browser screen recorder for app videos and GIFs that shows the maker's face full size only at the start and end, keeps it small or hidden in between, and cuts GIFs from a screen-only track; 1.1.0 adds narration over an existing MP4, pinned comments and backdrops. Raw file: [raw/apps/swmm-bookend-recorder-v1.1.0.md](../../raw/apps/swmm-bookend-recorder-v1.1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/1y1Hy7jtVYzC7cAH3ehCxy, version 1793124803-dad6 (index.html, 313,935 bytes, SHA-256 bcf7150e818b2e8d2715c238b4a887bc1b009d1009cde6c459f32572816788ba), every tab read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says it was built with Claude in a claude.ai session on 27 October 2026 at Bob's request; he chose the problem (proof of presence without too much face) and named the app.

**Claims worth keeping** (all copied from the file)
- Decoding the finished MP4 and counting the stand-in face's pixels agrees with the compositor's own log: median ratio 0.964 at full frame, 0.89 for the tiny box.
- A rehearsal take: 13.71 s, file plays 13.69 s, 1.28 MB; 30.3 fps, 416 frames, 0 dropped.
- The Doc reports 23 of 23 checks passed; the About tab says Claude wrote 40 automated checks (Q114).

**Limits it states.** Not a cryptographic proof of humanity and no C2PA Content Credentials; a deepfake webcam is a webcam to the browser; no real face, webcam or desktop tested; Safari, Firefox and Edge not run; no real Snagit or Camtasia file tried.

**Checked at ingest.** The two check counts in the page differ (23 and 40); the summary reports both. The `links:` line gives Netlify as https://swmm-bookend-recorder.netlify.app.

**Feeds:** [SWMM Enablement Bookend Recorder (app)](../entities/swmm-bookend-recorder.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [App build contract (four working principles)](../concepts/app-build-contract.md).
