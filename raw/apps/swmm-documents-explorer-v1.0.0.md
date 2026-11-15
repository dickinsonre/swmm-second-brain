---
name: SWMM Documents Explorer
file: swmm-documents-explorer
version: 1.0.0
date: 2026-02-11
author: Robert Dickinson
links: {replit: https://swmm-documents-explorer.replit.app, repo: https://github.com/SWMMEnablement/SWMM_MD_Documents}
engines: none
stack: TypeScript, React, Vite, Tailwind CSS, Express, Node.js, Drizzle ORM, PostgreSQL schema, Google Fonts, Replit hosting
units: not applicable
ai_use: No AI tool use in building the app is recorded in the checked project sources.
---

# SWMM Documents Explorer: An interactive guide to SWMM documentation

## What it does

The app presents a curated guide to the SWMM documentation archive. It is for people looking for historical and technical context about SWMM documents. Visitors can browse overview information, eras, a timeline, explanatory material about SWMM processes, and a filtered file listing. The content describes documents and model history; the app does not run stormwater simulations.

## How it computes

- `client/src/lib/swmm-data.ts` defines the era records, document metadata, timeline entries, and explanatory process steps (lines 32-297).
- `AllFilesTab` in `client/src/components/allfiles-tab.tsx` combines each era's documents and subfolder entries, then filters the combined list by type (lines 14-45).
- `OverviewTab` in `client/src/components/overview-tab.tsx` displays the constants in `STATS` (lines 6-29). These are labels in the source, not all calculated from the document records.
- No SWMM simulation engine is called. The process descriptions and Saint-Venant equations are rendered as explanatory text in `HowItWorksTab` (`client/src/components/howitworks-tab.tsx`, lines 18-90); they are not evaluated by the app.
- The theme toggle in `ThemeProvider` stores the selected theme in browser `localStorage` (`client/src/components/theme-provider.tsx`, lines 15-33).

## Inputs and outputs

- The displayed archive entries are hard-coded TypeScript objects. Their metadata describes Markdown, PDF, and Word documents, plus folder entries (`client/src/lib/swmm-data.ts`, lines 1-23 and 32-229).
- The app does not load those archive documents as runtime input or write document files. The browser stores only the theme preference under the `theme` local-storage key (`client/src/components/theme-provider.tsx`, lines 15-33).
- The client route is `/`; other client paths render the not-found component (`client/src/App.tsx`, lines 10-15).
- The server registers no API endpoints in `server/routes.ts` (lines 5-16). It serves the client app through Vite in development or static files in production (`server/index.ts`, lines 78-102).
- A PostgreSQL schema and an in-memory user storage class exist (`shared/schema.ts`, lines 6-18; `server/storage.ts`, lines 13-38). The archive UI reads its content from client constants, not from that storage.
- The page links to the SWMM document archive, the SWMMEnablement GitHub organization, and SWMM5.org (`client/src/pages/explorer.tsx`, lines 104-120).

## Contents

Counts below were computed from the exported data in `client/src/lib/swmm-data.ts` during this summary run. The source arrays are at lines 32-245 and 247-297.

| Item | Count |
| --- | ---: |
| Era records | 8 |
| Timeline entries | 13 |
| Explanatory process steps | 7 |
| Document metadata entries | 29 |
| PDF entries | 11 |
| Markdown entries | 17 |
| DOC entries | 1 |
| Subfolder entries | 4 |
| Total document and subfolder entries | 33 |

The app also displays the source-defined overview labels `30+` documents, `8` eras, `6` folders, and `55` years (`client/src/lib/swmm-data.ts`, lines 299-303). The document and folder labels do not match the counts obtained from the actual `ERAS` records.

## Checks

- `npm run check`: passed. TypeScript exited with status zero.
- `npm test`: no test cases ran. The command exited with an error because `package.json` defines no `test` script. Test cases passed: 0. Test cases failed: 0.
- Main page: `/` loaded in the app preview. No browser console errors were captured. The development log included a stale Browserslist data warning and a PostCSS warning.
- Human review: none recorded.

## What this does not show

1. The file version date uses the latest Git commit date, whose message is “Published your App.” There is no separate release-date field in `package.json`.
2. The preview checked the initial `/` view only. Tab changes, era selection, file filters, and the theme toggle were not checked interactively.
3. The not-found route and server error cases were not checked.
4. The historical claims, equations, archive documents, external links, and actual licenses of the source documents were not independently validated.
5. The app's display counts for documents and folders differ from the counts in its data records, as described above.
6. Individual licenses for transitive and other unlisted dependencies were not checked.
7. The app's Git remote is an internal Replit URL. The GitHub URL in the front matter is the archive repository linked by the app, not a verified public repository for this app's source code.
8. No person is recorded as having reviewed this summary.

## How to reproduce

Run the app with `npm run dev`. Run the TypeScript check with `npm run check`. There is no configured test command. The package scripts also provide `npm run build` and `npm start` for the production build and server (`package.json`, lines 6-11).

## Credits and licenses

- Author: Robert Dickinson. The Git log attributes its recorded commits to `robertdickinson`; it does not describe individual contributions.
- The app's license is MIT (`package.json`, line 5).
- The app links to SWMMEnablement/SWMM_MD_Documents as its documentation source (`client/src/pages/explorer.tsx`, lines 104-120). The overview labels the archive license MIT (`client/src/components/overview-tab.tsx`, lines 46-70).
- Core libraries and declared package licenses: React, MIT; Vite, MIT; Express, MIT; Tailwind CSS, MIT; Drizzle ORM, Apache-2.0; Wouter, Unlicense; TanStack React Query, MIT; Radix UI, MIT; Lucide React, ISC; date-fns, MIT; Zod, MIT; TypeScript, Apache-2.0; esbuild, MIT. These licenses were read from the installed package manifests. Direct dependencies are listed in `package.json` (lines 13-101).
- Google Fonts is loaded from Google Fonts in `client/index.html` (lines 7-10). The font license terms were not checked.

## AI use

The checked source, project documentation, and Git commit messages do not name an AI tool used to build the app. The Git log attributes the recorded commits to `robertdickinson`, but does not describe Robert Dickinson's specific work. The project describes its Markdown archive as AI-readable (`client/src/components/overview-tab.tsx`, lines 32-42); that does not establish that AI tools built the app.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

From `git log -10`, newest first:

- 2026-02-11: Published your App
- 2026-02-11: Saved progress at the end of the loop
- 2026-02-11: Enhance website with interactive documentation explorer and theme support
- 2026-02-11: Extracted stack files
- 2026-02-11: Initial commit
