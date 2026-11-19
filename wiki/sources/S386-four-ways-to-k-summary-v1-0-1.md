---
title: "S386: Four Ways to K, summary written from the page (v1.0.1)"
type: source
raw: raw/apps/four-ways-to-k-v1.0.1.md
kind: app-md
author: Robert Dickinson
published: 2026-11-19
ingested: 2026-11-19
tags: [apps, swmm5, minor-losses, manholes, wasm]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** The technical summary of Four Ways to K, version 1.0.1. It is the summary of version 1.0 [S225](S225-four-ways-to-k-summary.md) with one patch added, and it replaces S225 as the current source for the app. Raw file: [raw/apps/four-ways-to-k-v1.0.1.md](../../raw/apps/four-ways-to-k-v1.0.1.md).

**How it was written. A summary written from the page, then patched.** Claude (Anthropic) wrote the text of 1.0 on 17 November 2026 from the published page, with no model run [S225](S225-four-ways-to-k-summary.md). In a later session on 19 November 2026 Claude made the 1.0.1 patch, added a line to the page's own AI-use note, and added to the file its Changes line, a sentence in the AI-use section and the deployed Netlify address. Bob has not read it (Q108).

**Claims worth keeping** (all copied from the file)
- 1.0.1 (2026-11-19): "the page followed the device's light setting on first paint, against the dark-first rule."
- `<html>` now carries `data-theme="dark"`, and the theme function falls back to dark rather than to `prefers-color-scheme`; Light is used only when chosen. "Nothing else changed; no engine run was repeated."
- The engine numbers are those of 1.0: with the pipes full, [LOSSES], equivalent n and the orifice each raise J1 by 0.944 ft; at 2 cfs equivalent n charges 1.94 times too much loss.
- Netlify: https://four-ways-to-k.netlify.app.

**Limits it states.** As in 1.0: one test line and four flow cases; no field data.

**Checked at ingest.** Compared line by line with 1.0: 15 lines differ, all in the front matter, the version sentence, the AI-use section and the Changes list. The file describes the theme change in words and does not quote the code it replaced.

**Feeds:** [Four Ways to K (app)](../entities/four-ways-to-k.md), [Apps summarized on 17 November 2026: generators, rain and surfaces for SWMM5](../concepts/apps-from-pages-generators-rain-surfaces.md).
