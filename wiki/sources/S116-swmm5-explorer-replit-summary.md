---
title: "S116: SWMM5 Explorer, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-explorer--robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-01-29
ingested: 2026-11-15
tags: [apps, replit, swmm5, source-code, ai]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM5 Explorer, version 1.0.0: an app for studying the SWMM source code: a code browser, preset Sankey diagrams of module relationships, an input-file form, an engine page and AI explanations of selected source text. It is one of Bob's Replit apps, at `swmm-explorer--robertdickinson.replit.app`. Raw file: [raw/apps/swmm-explorer--robertdickinson-v1.0.0.md](../../raw/apps/swmm-explorer--robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the repository records agent-authored workflows but does not establish which assistant wrote each feature. The copy here was read out of the editor of the Replit project named SWMM Explorer on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- The browser engine asset is a no-op stub. A direct probe reported version `0.0.0`, success `true`, error code `0` and empty report text. No hydraulic simulation takes place.
- When the module is missing, a fallback waits through scripted phases and returns fixed report quantities, not values calculated from rainfall or geometry.
- It bundles 75 source records: 54 C implementation files and 21 headers, in 5 categories. The archived solver is EPA SWMM 5.2.4, public domain, upstream commit not recorded.
- Engine version labels conflict: the sidebar and About page show `5.1.015`, the fallback string `5.2.1`, the archived header `5.2.4` and the stub `0.0.0`.
- The symbol index uses a regular expression, not a C parser. Sankey link values are preset data, not measured flows.
- 7 named routes. 6 rendered behind an onboarding dialog; `/code` failed with the error "`Tooltip` must be used within `TooltipProvider`".
- The input generator interpolates form strings into a template with a fixed subcatchment row and does no calculation. Replit Agent notes that it references rainfall and outlet objects without complete definitions.
- `npm run check` and `npm run build` passed. `npm test` failed to start: no test script.
- At run time it sends prompts and selected code to OpenRouter, selecting DeepSeek V3.2 and Claude Sonnet 4.5. No paid AI call was made in the checks.

**Limits it states.** Real hydraulic accuracy was not checked, because the asset is a stub and not the archived solver compiled to WebAssembly. AI responses, file handling, downloads and the published site were not checked. The welcome overlay stayed open, so the page loads do not verify the interactions under it.

**Checked at ingest.** The file's own `engines:` line calls its entry "EPA SWMM source archive, not an executable browser solver". Not to be confused with [PySWMM Explorer (app)](../entities/pyswmm-explorer.md) or [SWMManywhere Explorer (app)](../entities/swmmanywhere-explorer.md).

**Feeds:** [SWMM5 Explorer (app)](../entities/swmm5-explorer.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [EPA SWMM 5](../entities/swmm-5.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
