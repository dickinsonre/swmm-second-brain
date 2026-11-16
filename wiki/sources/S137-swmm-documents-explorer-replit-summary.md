---
title: "S137: SWMM Documents Explorer, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/swmm-documents-explorer-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2026-02-11
ingested: 2026-11-15
tags: [apps, replit, documentation, swmm-history]
reviewed: 11/16/2026
---
**What it is.** A technical summary of SWMM Documents Explorer, version 1.0.0: a guide to the SWMM documentation archive, with eras, a timeline, explanatory pages on SWMM processes and a filtered list of files; it runs no simulation. It is one of Bob's Replit apps, at `swmm-documents-explorer.replit.app`. Raw file: [raw/apps/swmm-documents-explorer-v1.0.0.md](../../raw/apps/swmm-documents-explorer-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the checked source, project documentation and Git commit messages do not name an AI tool used to build it. The copy here was read out of the editor of the Replit project named SWMM-Documents-Explorer on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- It presents a curated guide to the SWMM documentation archive and does not run stormwater simulations. `engines: none`.
- The archive entries are hard-coded TypeScript objects. The app does not load the archive documents at run time or write document files.
- Counted from its data: 8 era records, 13 timeline entries, 7 explanatory process steps, 29 document metadata entries (11 PDF, 17 Markdown, 1 DOC) and 4 subfolder entries, 33 entries in all.
- The overview shows the labels `30+` documents, `8` eras, `6` folders and `55` years. The document and folder labels do not match the counts from the records.
- The Saint-Venant equations are rendered as explanatory text; the app does not evaluate them.
- The server registers no API endpoints. A PostgreSQL schema and an in-memory user storage class exist, but the archive pages read their content from client constants.
- The page links to the SWMM document archive, the SWMMEnablement GitHub organization and SWMM5.org. The `repo:` in the front matter is `SWMMEnablement/SWMM_MD_Documents`, the archive repository the app links, not a verified repository for the app's own source.
- `npm run check` passed. No `test` script is defined. The main page `/` loaded with no browser console errors.
- The app's license is MIT. The overview labels the archive license MIT.
- The project describes its Markdown archive as AI-readable; the file says that does not establish that AI tools built the app.

**Limits it states.** Only the first view of `/` was checked; tab changes, era selection, file filters and the theme toggle were not. The historical claims, equations, archive documents, external links and the licenses of the source documents were not independently validated. The `date:` is the date of the latest Git commit, whose message is "Published your App".

**Checked at ingest.** The archive it guides is the repository the EPA hydraulics manual here was converted from: [S60](S60-epa-swmm5-reference-manual-vol2-hydraulics.md) names `SWMMEnablement/SWMM_MD_Documents` as the place its markdown is kept. The app's 29 document entries and the files in `raw/manuals/` were not compared. The `date:`, 11 February 2026, is a commit date, and every change in its list is from that day (Q75). Its `repo:` is the archive, not the app (Q79).

**Feeds:** [SWMM Documents Explorer (app)](../entities/swmm-documents-explorer.md), [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [Master SWMM PDF (app)](../entities/master-swmm-pdf.md), [Bob's GitHub repositories (where the rest of the material lives)](../entities/bobs-github-repositories.md).
