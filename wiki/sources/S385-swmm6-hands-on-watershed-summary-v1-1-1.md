---
title: "S385: SWMM6 Hands-On Watershed, summary written from the page (v1.1.1)"
type: source
raw: raw/apps/swmm6-hands-on-watershed-v1.1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-19
ingested: 2026-11-19
tags: [apps, swmm6, snow, groundwater, emulator, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** The technical summary of SWMM6 Hands-On Watershed, version 1.1.1. It is the summary of version 1.1.0 [S261](S261-swmm6-hands-on-watershed-summary.md) with one patch added, and it replaces S261 as the current source for the app. Raw file: [raw/apps/swmm6-hands-on-watershed-v1.1.1.md](../../raw/apps/swmm6-hands-on-watershed-v1.1.1.md).

**How it was written. A summary written from the page, then patched.** Claude (Anthropic) wrote the text of 1.1.0 on 17 November 2026 from the published page, with no model run [S261](S261-swmm6-hands-on-watershed-summary.md). In a later session on 19 November 2026 Claude made the 1.1.1 patch, added a line to the page's own AI-use note, and added to the file its Changes line, a sentence in the AI-use section and the deployed Netlify address. Bob has not read it (Q108).

**Claims worth keeping** (all copied from the file)
- 1.1.1 (2026-11-19): six tables (`table.t`) had no sideways scroller. After one engine run the session log made the Emulator tab 445 px wide on a 390 px screen, and the About table was 601 px.
- Each table is now wrapped in `<div class="tw">` with `overflow-x:auto`; both tabs fit at 390 px. "Nothing else changed; no engine run was repeated."
- The other numbers are those of 1.1.0: the basin balance closed within 0.049 in on all 3,500 test runs, and the emulator's held-out peak R2 is 0.952 with a median error of 9.4%.
- Netlify: https://swmm6-hands-on-watershed.netlify.app.

**Limits it states.** As in 1.1.0: a synthetic, uncalibrated catchment; snow from a September engine build; the dry-conduit evaporation defect of that build (fixed upstream on 12 September 2026, commit b051d270); live hand tracking never tested.

**Checked at ingest.** Compared line by line with 1.1.0: 15 lines differ, all in the front matter, the version sentence, the AI-use section and the Changes list.

**Feeds:** [SWMM6 Hands-On Watershed (app)](../entities/swmm6-hands-on-watershed.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md).
