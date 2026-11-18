---
title: "S267: BobSWMM App Catalog, summary written from the page (v1.0)"
type: source
raw: raw/apps/bobswmm-app-catalog-v1.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-21
ingested: 2026-11-17
tags: [apps, catalog, lovable, audit]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app BobSWMM App Catalog, version 1.0: Bob's catalog of his own small web apps (BobSWMM, also called the Multiverse Educational Lab), rebuilt from its Lovable source as one HTML file with the finder, toolkits, workflows, a map, a glossary and a Health sheet. The original lives at bobswmmapps.lovable.app. Raw file: [raw/apps/bobswmm-app-catalog-v1.0.md](../../raw/apps/bobswmm-app-catalog-v1.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1792631891-7879, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says it was built with Claude in a Claude Code session on 21 October 2026 at Bob's request; Bob supplied the source and owns the catalog and its contents. The original was built on Lovable, an AI app builder. Claude compiled the source data, wrote the audit and the node test and ported the finder.

**Claims worth keeping** (all copied from the file)
- 106 records and 364 wires: 88 apps on the main shelf, 6 math curiosities, and 12 older apps kept in the data but hidden.
- 18 records carry hidden: true; 6 still appear in the Math Curiosities drawer and 12 appear nowhere.
- Five hero tools show lines such as "Used 32 times this week", typed into the code under a comment reading "Simulated weekly usage counts".
- The finder expands words through a synonym table; for a conversion request, XP to SWMM Bridge, the tool built for the job, ranks 4th behind InfoSewer To ICM Guide.
- The original's single app review is marked in its source as AI-generated.
- Counts and findings are checked by a node test and an independent Python audit; every finding quotes its source lines.

**Limits it states.** No person has reviewed the findings against the live original site.

**Checked at ingest.** 88 + 6 + 12 = 106 records. The simulated usage counts are a fact about the original catalog's code that a visitor to it would not see. The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://bobswmm-app-catalog.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [BobSWMM App Catalog (app)](../entities/bobswmm-app-catalog.md), [Apps summarized on 17 November 2026: SWMM6, HydroCouple and AI](../concepts/apps-from-pages-swmm6-hydrocouple-ai.md), [Robert (Bob) Dickinson](../entities/robert-dickinson.md), [Bob Usefulness Index (app)](../entities/bob-usefulness-index.md).
