---
title: "SWMM5 & EPANET INP Explorer (app)"
type: entity
updated: 2026-11-15
sources: [S105, S126, S132]
tags: [apps, replit, swmm5, epanet, inp-files, reference]
reviewed: no
---
Bob's Replit app SWMM5 & EPANET INP Explorer: a reference to the SWMM and EPANET input-file formats: searchable section references with field definitions and examples, guided lessons, sample input files, a section builder and a paste-in parser. Version 1.0.0, at `swmm5epanetinpviewer.com` [S132](../sources/S132-swmm5-epanet-inp-explorer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S132](../sources/S132-swmm5-epanet-inp-explorer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S132](../sources/S132-swmm5-epanet-inp-explorer-replit-summary.md)
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

**What it does not show.** Parser and builder interactions were not exercised. The production pages were not loaded; the page check used the Replit preview. The tracking service and its stored data were not inspected. The embedded history site was not checked. [S132](../sources/S132-swmm5-epanet-inp-explorer-replit-summary.md)

**Noted at ingest.** The site address in the file is `swmm5epanetinpviewer.com`; its `file:` is swmm-inp-viewer--robertdickinson and the Replit project is SwmmInpViewer (Q77). It is not the [SWMM5 .inp File Viewer (app)](swmm5-inp-file-viewer.md) of [S105](../sources/S105-swmm5-inp-file-viewer-replit-summary.md), whose file is swmm-5-inp-reader. The `date:` is the day of the summary (Q75). The history site it embeds is the [SWMM Ecosystem (app)](swmm-ecosystem.md) [S126](../sources/S126-swmm-ecosystem-replit-summary.md). It was brought over after the seventeen on the concept page and is added there as a nineteenth row.

See [Replit apps: the second seventeen summaries](../concepts/replit-app-summaries-second-batch.md), [SWMM5 .inp File Viewer (app)](swmm5-inp-file-viewer.md), [SWMM5 INP MAKER (app)](swmm5-inp-maker.md), [SWMM Ecosystem (app)](swmm-ecosystem.md).
