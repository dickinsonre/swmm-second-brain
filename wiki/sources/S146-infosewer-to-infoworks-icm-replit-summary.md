---
title: "S146: InfoSewer to InfoWorks ICM, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/data-sewer-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-02-12
ingested: 2026-11-15
tags: [apps, replit, infosewer, icm, migration]
reviewed: no
---
**What it is.** A technical summary of InfoSewer to InfoWorks ICM, version 1.0.0: a guide to moving InfoSewer model data into InfoWorks ICM, pointing to a Ruby import tool as the preferred route and a manual ODIC workflow as the alternative, with browser tools to check IDs and CSV headers and to compose SQL; it converts nothing itself. It is one of Bob's Replit apps, at `infosewericminfoworksimport.com`. Raw file: [raw/apps/data-sewer-robertdickinson-v1.0.0.md](../../raw/apps/data-sewer-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the checked project code and documentation do not name an AI tool that built it. The copy here was read out of the editor of the Replit project named InfoSewerToICMSteps on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It does not itself convert or import a model. The preferred Ruby importer and the other conversion resources are linked, not executed. `engines: none`.
- A comparison calculator sums hard-coded time estimates: 182 minutes for the older workflow and 28 minutes for the newer, a difference of 154 minutes, or 2 hours 34 minutes. These are estimates in the code, not measured runs.
- The ID checker splits IDs on commas or newlines, checks naming rules with a length check of 40 characters, proposes corrected IDs and builds SQL update text, which it shows or copies but does not execute.
- The CSV validator reads pasted headers or the first line of an uploaded CSV, normalizes them to uppercase and computes `present fields / required fields * 100`. It does not inspect the data rows, and the file is not sent to the server.
- The SQL builder joins fixed snippets and does not connect to a database. The readiness checklist computes `checked items / total items * 100`.
- Nine manual conversion-step records, four browser tools, nine step-specific required-field sets, seven preset SQL scripts, a checklist of 14 items, 19 error records and eight color themes.
- Progress, theme and checklist state are kept in browser localStorage. The Express server registers no API endpoints.
- `npm run check` passed. No `test` script. The browser console recorded an Invalid hook call warning and invalid `React.Fragment` prop warnings; the guide stayed visible.
- Linked Innovyze Open-Source-Support conversion resources are referenced; their licenses were not checked. The project declares MIT. `units: US customary`.

**Limits it states.** The linked Ruby conversion tool was not downloaded or run, and no real InfoSewer model was converted or validated. No production build was run and the published page was not checked. The cause of the console warnings was not investigated.

**Checked at ingest.** The difference checks: 182 - 28 = 154 minutes, which is 2 hours 34 minutes (our arithmetic). The `date:` is the newest commit date, 12 February 2026; the change list starts on 16 August 2025 (Q75). Its `file:`, data-sewer, does not say what it is (Q77). The models it helps move are the ones the [InfoSewer and InfoSWMM Legacy Model Reader (app)](../entities/infosewer-infoswmm-legacy-model-reader.md) reads [S103](S103-legacy-model-reader-replit-summary.md); see also [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md).

**Feeds:** [InfoSewer to InfoWorks ICM (app)](../entities/infosewer-to-infoworks-icm-guide.md), [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [InfoSewer and InfoSWMM Legacy Model Reader (app)](../entities/infosewer-infoswmm-legacy-model-reader.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md).
