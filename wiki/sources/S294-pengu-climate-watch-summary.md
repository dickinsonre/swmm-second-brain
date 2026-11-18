---
title: "S294: Pengu Climate Watch, summary written from the page (v1.1)"
type: source
raw: raw/apps/pengu-cllimate-watch-v1.1.md
kind: app-md
author: Robert Dickinson
published: 2026-10-25
ingested: 2026-11-18
tags: [apps, climate, antarctica, teaching, lovable]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app Pengu Climate Watch, version 1.1: Bob's Lovable app on Antarctic weather, ice and penguin habitat (four React pages) rebuilt as one HTML file and fact-checked, treating the ice sheet as a reservoir and a glacier's flux gate like a culvert. Raw file: [raw/apps/pengu-cllimate-watch-v1.1.md](../../raw/apps/pengu-cllimate-watch-v1.1.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q111). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/F3gS5aqDFjLA4fbxafNcLv, version 1792959766-8223 (index.html, 491,290 bytes, SHA-256 91f57f55f4974f598b00087eae2a2609f42ad8be0f0ada4fa418dc15d742aff0), every tab read in headless Chromium on 2026-11-18, with d3 7.9.0 supplied from a local copy because cdnjs was not reachable from the reading machine. Nothing was run to write this file." The page says this edition was produced with Claude on 25 October 2026 at Bob's request; he wrote the original Lovable app (project pengu-climate-watch, repository pudgy-water-flow).

**Claims worth keeping** (all copied from the file)
- GRACE and GRACE-FO: about 135 Gt (about 149 billion US tons) of ice lost a year from 2002 to 2025; IMBIE's 2026 assessment: 4,780 Gt lost from 1979 to 2023, 13.3 mm (0.52 in, the summary's conversion) of sea level.
- The Fixes tab lists 23 code defects and 26 numbers that did not match their sources in the Lovable project, and 30 defects in the port fixed in 1.1, each with the code as it was.
- Weather requests fell from about 27 on page load to five.
- The simulator's melt factor is f = 1.15^(T + 2) above -2 °C, else 1; scaling the net loss rather than the gross discharge gives about 84 mm (3.3 in) of sea level by 2100 at the slider's far end where a strict mass balance would give about a metre (3.3 ft).

**Limits it states.** Air temperature does not melt most Antarctic ice; the habitat tolerances and warmings are the original app's assumptions; Open-Meteo is model output; the ten colony counts are unchecked, at least one about ten times too low.

**Checked at ingest.** The summary was written with d3 supplied from a local copy, because cdnjs was not reachable from the reading machine, so it does not say how the page behaves when d3 cannot load (Q112). The `links:` line gives Netlify as https://pengu-cllimate-watch.netlify.app.

**Feeds:** [Pengu Climate Watch (app)](../entities/pengu-climate-watch.md), [Apps summarized on 17 and 18 November 2026: AI workflows, tools and puzzles](../concepts/apps-from-pages-tools-and-puzzles.md), [Negative results](../concepts/negative-results.md).
