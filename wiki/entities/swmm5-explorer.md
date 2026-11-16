---
title: SWMM5 Explorer (app)
type: entity
updated: 2026-11-15
sources: [S116]
tags: [apps, replit, swmm5, source-code, ai]
reviewed: 11/16/2026
---
Bob's Replit app SWMM5 Explorer: an app for studying the SWMM source code: a code browser, preset Sankey diagrams of module relationships, an input-file form, an engine page and AI explanations of selected source text. Version 1.0.0, at `swmm-explorer--robertdickinson.replit.app` [S116](../sources/S116-swmm5-explorer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S116](../sources/S116-swmm5-explorer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S116](../sources/S116-swmm5-explorer-replit-summary.md)
- The browser engine asset is a no-op stub. A direct probe reported version `0.0.0`, success `true`, error code `0` and empty report text. No hydraulic simulation takes place.
- When the module is missing, a fallback waits through scripted phases and returns fixed report quantities, not values calculated from rainfall or geometry.
- It bundles 75 source records: 54 C implementation files and 21 headers, in 5 categories. The archived solver is EPA SWMM 5.2.4, public domain, upstream commit not recorded.
- Engine version labels conflict: the sidebar and About page show `5.1.015`, the fallback string `5.2.1`, the archived header `5.2.4` and the stub `0.0.0`.
- The symbol index uses a regular expression, not a C parser. Sankey link values are preset data, not measured flows.
- 7 named routes. 6 rendered behind an onboarding dialog; `/code` failed with the error "`Tooltip` must be used within `TooltipProvider`".
- The input generator interpolates form strings into a template with a fixed subcatchment row and does no calculation. Replit Agent notes that it references rainfall and outlet objects without complete definitions.
- `npm run check` and `npm run build` passed. `npm test` failed to start: no test script.
- At run time it sends prompts and selected code to OpenRouter, selecting DeepSeek V3.2 and Claude Sonnet 4.5. No paid AI call was made in the checks.

**What it does not show.** Real hydraulic accuracy was not checked, because the asset is a stub and not the archived solver compiled to WebAssembly. AI responses, file handling, downloads and the published site were not checked. The welcome overlay stayed open, so the page loads do not verify the interactions under it. [S116](../sources/S116-swmm5-explorer-replit-summary.md)

**Noted at ingest.** The file's own `engines:` line calls its entry "EPA SWMM source archive, not an executable browser solver". Not to be confused with [PySWMM Explorer (app)](pyswmm-explorer.md) or [SWMManywhere Explorer (app)](swmmanywhere-explorer.md).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [EPA SWMM 5](swmm-5.md), [WebAssembly builds against native builds](../concepts/wasm-against-native-builds.md).
