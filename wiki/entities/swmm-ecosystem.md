---
title: SWMM Ecosystem (app)
type: entity
updated: 2026-11-15
sources: [S126, S132]
tags: [apps, replit, swmm-history, reference]
reviewed: 11/16/2026
---
Bob's Replit app SWMM Ecosystem: a reference app on the history of SWMM and the software around it: timelines, contributor profiles with editorial grades, catalogs of commercial and open-source programs, comparisons, a glossary and a chat assistant. Version 1.0.0, at `swmm-history-robertdickinson.replit.app` [S126](../sources/S126-swmm-ecosystem-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S126](../sources/S126-swmm-ecosystem-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S126](../sources/S126-swmm-ecosystem-replit-summary.md)
- It runs no drainage model. `engines: none`.
- The catalog holds 51 records: 12 EPA, 26 commercial and third-party, and 13 open-source and academic.
- 87 contributor cards on the home page and 45 on the history page; the two views overlap and must not be added. 285 glossary entries. 13 home tab identifiers.
- Contributor grades are stored editorial judgments. No formula derives a grade from repository activity.
- Comparison scores count keyword matches in feature text, `min(matches / max(keyword count * 0.4, 1), 1)`. The file calls them text heuristics, not measured capabilities.
- Elapsed history is computed as `current calendar year - 1969`.
- The Preissmann slot animation advances a synthetic water level; it is not a drainage-model solution.
- The Source page uses a hardcoded file tree and returns mock file text.
- Chat sends the conversation to OpenAI `gpt-4o-mini` with a fixed system prompt and does not retrieve from the catalog.
- `npm run check` passed, and 15 tests passed with 0 failed.
- A review panel in the app records clarifications from the site owner on Robert Dickinson's affiliation, Mirab's identity and a deferred EPA staffing review. The file says these are not approval of the summary.
- Repository: https://github.com/dickinsonre/SwmmHistory. License MIT.

**What it does not show.** Historical claims, contributor grades, commit totals and linked publications were not checked against outside sources. Live chat, the production build and the published pages were not checked. [S126](../sources/S126-swmm-ecosystem-replit-summary.md)

**Noted at ingest.** The `date:` is the first appearance of package version 1.0.0 in Git, commit `88aef49`, 29 August 2025 (Q75). None of the app's history or grades is copied into this wiki.

**Added 15 November 2026: embedded in another app.** The Docs page of [SWMM5 & EPANET INP Explorer (app)](swmm5-epanet-inp-explorer.md) embeds this app's site [S132](../sources/S132-swmm5-epanet-inp-explorer-replit-summary.md).

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md), [Mirab Test Bench (app)](mirab-test-bench.md), [Historical Water Inventions (app)](historical-water-inventions.md).
