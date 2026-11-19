---
title: "S384: Visual SWMM, summary written from the page (v0.1.1)"
type: source
raw: raw/apps/visual-swmm-v0.1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-19
ingested: 2026-11-19
tags: [apps, xpswmm, history, file-formats, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** The technical summary of Visual SWMM, version 0.1.1. It is the summary of version 0.1.0 [S207](S207-visual-swmm-summary.md) with one patch added, and it replaces S207 as the current source for the app. Raw file: [raw/apps/visual-swmm-v0.1.1.md](../../raw/apps/visual-swmm-v0.1.1.md).

**How it was written. A summary written from the page, then patched.** Claude (Anthropic) wrote the text of 0.1.0 on 17 November 2026 from the published page, with nothing rerun [S207](S207-visual-swmm-summary.md). In a later session on 19 November 2026 Claude made the 0.1.1 patch and added to the file its Changes line, a sentence in the AI-use section and the deployed Netlify address. The `written_from:` line now ends: "The 0.1.1 patch was made on 2026-11-19 by Claude and checked in headless Chromium at 390 px; its Changes line says what moved." Bob has not read it (Q108).

**Claims worth keeping** (all copied from the file)
- 0.1.1 (2026-11-19): at phone width the one-column grid kept its automatic minimum, so the Verify table pushed the page to 484 px on a 390 px screen.
- The fix is one CSS line in the 900 px media rule: `.grid,.grid.even{grid-template-columns:1fr}` became `minmax(0,1fr)`. Every view now fits at 390 px. Nothing else changed.
- "Nothing was rerun against the .xpx exports." The other numbers are those of 0.1.0: 18,219 of 18,296 input fields equal XP-SWMM's own .xpx exports for eleven models, and 30,612 of 51,144 records (60%) in 25 sample files sit on cards the dictionary decodes.
- Netlify: https://visual-swmm.netlify.app.

**Limits it states.** As in 0.1.0: it does not run a model; cards added after December 1999 show as raw records; 25 of more than 1,300 archive files were checked; the .xpx it writes has not been loaded back into XP-SWMM; no person has reviewed the reader line by line.

**Checked at ingest.** Compared line by line with 0.1.0: 15 lines differ, all in the front matter, the version sentence, the AI-use section and the Changes list. The page's code lines are quoted in the file itself; nothing was rerun at ingest.

**Feeds:** [Visual SWMM (app)](../entities/visual-swmm.md), [Apps summarized on 17 November 2026: SWMM history and the insides of SWMM5](../concepts/apps-from-pages-history-and-swmm5.md).
