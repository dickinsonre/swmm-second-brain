---
title: "InfoSewer to InfoWorks ICM (app)"
type: entity
updated: 2026-11-15
sources: [S103, S146]
tags: [apps, replit, infosewer, icm, migration]
reviewed: no
---
Bob's Replit app InfoSewer to InfoWorks ICM: a guide to moving InfoSewer model data into InfoWorks ICM, pointing to a Ruby import tool as the preferred route and a manual ODIC workflow as the alternative, with browser tools to check IDs and CSV headers and to compose SQL; it converts nothing itself. Version 1.0.0, at `infosewericminfoworksimport.com` [S146](../sources/S146-infosewer-to-infoworks-icm-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S146](../sources/S146-infosewer-to-infoworks-icm-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S146](../sources/S146-infosewer-to-infoworks-icm-replit-summary.md)
- It does not itself convert or import a model. The preferred Ruby importer and the other conversion resources are linked, not executed. `engines: none`.
- A comparison calculator sums hard-coded time estimates: 182 minutes for the older workflow and 28 minutes for the newer, a difference of 154 minutes, or 2 hours 34 minutes. These are estimates in the code, not measured runs.
- The ID checker splits IDs on commas or newlines, checks naming rules with a length check of 40 characters, proposes corrected IDs and builds SQL update text, which it shows or copies but does not execute.
- The CSV validator reads pasted headers or the first line of an uploaded CSV, normalizes them to uppercase and computes `present fields / required fields * 100`. It does not inspect the data rows, and the file is not sent to the server.
- The SQL builder joins fixed snippets and does not connect to a database. The readiness checklist computes `checked items / total items * 100`.
- Nine manual conversion-step records, four browser tools, nine step-specific required-field sets, seven preset SQL scripts, a checklist of 14 items, 19 error records and eight color themes.
- Progress, theme and checklist state are kept in browser localStorage. The Express server registers no API endpoints.
- `npm run check` passed. No `test` script. The browser console recorded an Invalid hook call warning and invalid `React.Fragment` prop warnings; the guide stayed visible.
- Linked Innovyze Open-Source-Support conversion resources are referenced; their licenses were not checked. The project declares MIT. `units: US customary`.

**What it does not show.** The linked Ruby conversion tool was not downloaded or run, and no real InfoSewer model was converted or validated. No production build was run and the published page was not checked. The cause of the console warnings was not investigated. [S146](../sources/S146-infosewer-to-infoworks-icm-replit-summary.md)

**Noted at ingest.** The difference checks: 182 - 28 = 154 minutes, which is 2 hours 34 minutes (our arithmetic). The `date:` is the newest commit date, 12 February 2026; the change list starts on 16 August 2025 (Q75). Its `file:`, data-sewer, does not say what it is (Q77). The models it helps move are the ones the [InfoSewer and InfoSWMM Legacy Model Reader (app)](infosewer-infoswmm-legacy-model-reader.md) reads [S103](../sources/S103-legacy-model-reader-replit-summary.md); see also [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md).

See [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [InfoSewer and InfoSWMM Legacy Model Reader (app)](infosewer-infoswmm-legacy-model-reader.md), [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md).
