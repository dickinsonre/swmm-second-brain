---
title: "S126: SWMM Ecosystem, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-history-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2025-08-29
ingested: 2026-11-15
tags: [apps, replit, swmm-history, reference]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM Ecosystem, version 1.0.0: a reference app on the history of SWMM and the software around it: timelines, contributor profiles with editorial grades, catalogs of commercial and open-source programs, comparisons, a glossary and a chat assistant. It is one of Bob's Replit apps, at `swmm-history-robertdickinson.replit.app`. Raw file: [raw/apps/swmm-history-robertdickinson-v1.0.0.md](../../raw/apps/swmm-history-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says Git records Replit Agent as the author of recent development commits. The copy here was read out of the editor of the Replit project named SwmmHistory on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** Historical claims, contributor grades, commit totals and linked publications were not checked against outside sources. Live chat, the production build and the published pages were not checked.

**Checked at ingest.** The `date:` is the first appearance of package version 1.0.0 in Git, commit `88aef49`, 29 August 2025 (Q75). None of the app's history or grades is copied into this wiki.

**Feeds:** [SWMM Ecosystem (app)](../entities/swmm-ecosystem.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM version history, 1969 to 2026](../concepts/swmm-version-history.md), [Mirab Test Bench (app)](../entities/mirab-test-bench.md), [Historical Water Inventions (app)](../entities/historical-water-inventions.md).
