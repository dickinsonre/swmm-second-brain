---
title: "S299: O2 Tesseract, summary written from the page (v3.3)"
type: source
raw: raw/apps/o2-tesseract-v3.3.md
kind: app-md
author: Robert Dickinson
published: 2026-10-20
ingested: 2026-11-18
tags: [apps, puzzles, four-dimensions, counting]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app O2 Tesseract, version 3.3: the QiYi O2 puzzle carried from its 3D toy into four dimensions and on to seventeen: in 4D, eight balls in eight windows turned by six planes, with a cycle formula for the distance of any position. Raw file: [raw/apps/o2-tesseract-v3.3.md](../../raw/apps/o2-tesseract-v3.3.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/5dg4Y9uySBXb4U34A4MjTF, version 1792425917-d049 (index.html, 430,461 bytes, SHA-256 c151aeda6881859e588875d83f2edadb393f12c617050ecfd6930b0475009b20), its Play, Numbers, How it works and Doc tabs read in headless Chromium on 2026-11-18. Nothing was run to write this file." The page says Claude built the app in October 2026 under Bob's direction; he asked for each stage, rejected layouts that were not true projections and brought in an outside review.

**Claims worth keeping** (all copied from the file)
- In 4D there are 192 positions, never more than three moves from solved.
- Distance from solved is n - E - O/2 moves (n - E quarter turns) for E even and O odd cycles; every count and distance to 7D was computed twice by breadth-first search (Python and the page), 8D searched exhaustively, and above that the formula is used.

**Limits it states.** A model of what you can see, not a mechanism; the hidden pieces are not modelled; no person has checked the formula's case-by-case proof.

**Checked at ingest.** Not a water app. Nothing else to check by arithmetic. The `links:` line gives Netlify as https://o2-tesseract.netlify.app.

**Feeds:** [O2 Tesseract (app)](../entities/o2-tesseract.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Loopover (app)](../entities/loopover.md), [Cube as a Graph (app)](../entities/cube-as-a-graph.md).
