---
title: "S132: SWMM5 & EPANET INP Explorer, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-inp-viewer--robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, swmm5, epanet, inp-files, reference]
reviewed: no
---
**What it is.** A technical summary of SWMM5 & EPANET INP Explorer, version 1.0.0: a reference to the SWMM and EPANET input-file formats: searchable section references with field definitions and examples, guided lessons, sample input files, a section builder and a paste-in parser. It is one of Bob's Replit apps, at `swmm5epanetinpviewer.com`. Raw file: [raw/apps/swmm-inp-viewer--robertdickinson-v1.0.0.md](../../raw/apps/swmm-inp-viewer--robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the code does not establish whether every part was written by a person or an AI tool. The copy here was read out of the editor of the Replit project named SwmmInpViewer on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It documents formats and does not run either simulation engine. `engines: none`.
- Contents: 50 SWMM section definitions and 24 EPANET section definitions, 4 sample models, 7 learning pathways with 12 quiz questions, and 7 historical PDF files.
- It also holds format references by generation: 17 top-level sections for SWMM5, 14 for SWMM4 and 17 for SWMM3.
- The section builder validates required and numeric fields and writes the entered rows under a section header as `.inp` text.
- The parser reads pasted INP text, maps tokens to the section's field definitions and reports missing required fields and invalid numeric values. For numeric fields it reports minimum, maximum, and arithmetic mean. It does not read an uploaded file.
- Field documentation covers US Customary and SI units. The app does not convert physical quantities.
- The Docs page embeds the external SWMM History site at `https://swmm-history-robertdickinson.replit.app`.
- The app routes are `/` and `/docs`. The server registers no API endpoints.
- The page sends pageview events, a browser-generated visitor identifier, the current path, referrer, and user-agent metadata to a Replit-hosted tracking endpoint.
- `npm run build` passed. `npm run check` failed with 22 TypeScript diagnostics in `client/src/pages/Docs.tsx`. No test script is defined.
- Git metadata marks a Replit Agent commit dated 2026-02-07 that adds SWMM history and input-format documentation. Git records Robert Dickinson as author of recent changes.
- The app declares MIT. No SWMM engine code is included. The project does not state an EPANET license.

**Limits it states.** Parser and builder interactions were not exercised. The production pages were not loaded; the page check used the Replit preview. The tracking service and its stored data were not inspected. The embedded history site was not checked.

**Checked at ingest.** The site address in the file is `swmm5epanetinpviewer.com`; its `file:` is swmm-inp-viewer--robertdickinson and the Replit project is SwmmInpViewer (Q77). It is not the [SWMM5 .inp File Viewer (app)](../entities/swmm5-inp-file-viewer.md) of [S105](S105-swmm5-inp-file-viewer-replit-summary.md), whose file is swmm-5-inp-reader. The `date:` is the day of the summary (Q75). The history site it embeds is the [SWMM Ecosystem (app)](../entities/swmm-ecosystem.md) [S126](S126-swmm-ecosystem-replit-summary.md). It was brought over after the seventeen on the concept page and is added there as a nineteenth row.

**Feeds:** [SWMM5 & EPANET INP Explorer (app)](../entities/swmm5-epanet-inp-explorer.md), [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM5 .inp File Viewer (app)](../entities/swmm5-inp-file-viewer.md), [SWMM5 INP MAKER (app)](../entities/swmm5-inp-maker.md), [SWMM Ecosystem (app)](../entities/swmm-ecosystem.md).
