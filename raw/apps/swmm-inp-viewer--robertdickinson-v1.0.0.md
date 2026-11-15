---
name: SWMM5 & EPANET INP Explorer
file: swmm-inp-viewer--robertdickinson # generated deployment name
version: 1.0.0 # package.json:3
date: 2026-11-15 # no release date is declared; current date used
author: Robert Dickinson
links: {replit: https://swmm5epanetinpviewer.com, repo: none}
engines: none
stack: TypeScript, React, Wouter, Vite, Express, Tailwind CSS, Drizzle ORM (schema only), PostgreSQL module configured but no app runtime connection, in-memory server storage, Replit-hosted tracking endpoint, Google Fonts
units: both
ai_use: Git metadata identifies a Replit Agent commit; details below
---

# SWMM5 & EPANET INP Explorer: Browse and work with model input formats

## What it does

This app explains the structure of SWMM and EPANET input files for people learning, reading, or preparing hydraulic models. It provides searchable section references, field definitions, examples, and related-section links. It also provides guided lessons, sample input files, a section builder, and a paste-in parser. It documents formats but does not run either simulation engine.

## How it computes

- `SwmmExplorer` in `client/src/pages/SwmmExplorer.tsx` filters the in-memory section arrays by a lowercased search string in `filteredSections` and displays the matching records. It does not compute a hydraulic simulation.
- `INPBuilder` in `client/src/components/INPBuilder.tsx` validates required fields and numeric fields in `validateRow`. It formats entered rows under a section header in `generateINP`, then copies the text or creates a browser download.
- `INPParser` in `client/src/components/INPParser.tsx` reads pasted text in a `useMemo`: it finds the requested section, skips blank and comment lines, splits data lines on whitespace, and maps tokens to the section's field definitions. It reports missing required fields and invalid numeric values. For numeric fields with parsed values, it reports minimum, maximum, and arithmetic mean.
- No simulation engine is invoked by the client or server source. `server/routes.ts` registers no API endpoints.
- Field documentation covers US Customary and SI units. The app does not convert physical quantities or produce simulated results.

## Inputs and outputs

- Users search and select built-in section records, enter builder fields, or paste INP text into the parser. The parser does not read an uploaded file.
- The builder and sample-model controls create `.inp` text downloads. The section browser can export field metadata as CSV. The parser can copy valid parsed rows.
- Historical documents are static PDFs under `client/public/pdfs/`. The Docs page also embeds the external SWMM History site at `https://swmm-history-robertdickinson.replit.app`.
- The app routes are `/` and `/docs` (`client/src/App.tsx:13-17`). `server/routes.ts:5-15` defines no application API endpoints.
- Section and lesson data are TypeScript arrays. PDFs are static server files. Builder, parser, and navigation state is held in the browser. Theme, font weight, and onboarding state use `localStorage` (`client/src/lib/theme.tsx:17-47`; `client/src/components/OnboardingModal.tsx:125-153`).
- The server has a `MemStorage` user map (`server/storage.ts`), but the app routes do not expose it. No user records are saved to a database by the current routes.
- `client/index.html:29-57` sends pageview events, a browser-generated visitor identifier, the current path, referrer, and user-agent metadata to a Replit-hosted tracking endpoint. No credentials are included here.

## Contents

- SWMM section definitions: 50 (`client/src/data/swmm-schema.ts:48`; counted from the exported array).
- EPANET section definitions: 24 (`client/src/data/epanet-schema.ts:4`; counted from the exported array).
- Sample models: 4 (`client/src/data/sample-models.ts:11`; counted from the exported array).
- Learning pathways: 7; quiz questions: 12 (`client/src/pages/Docs.tsx:46-219`; counted from the pathway data).
- SWMM5 reference top-level sections: 17 (`client/src/data/swmm5-reference.ts:8`; counted from the exported array).
- SWMM4 format top-level sections: 14 (`client/src/data/swmm4-format.ts:8`; counted from the exported array).
- SWMM3 format top-level sections: 17 (`client/src/data/swmm3-format.ts:8`; counted from the exported array).
- Historical PDF files: 7 (`client/public/pdfs/`; counted from the directory).

## Checks

- `npm run build`: passed during this run. Vite built the client and esbuild built the server.
- `npm run check`: failed during this run with 22 TypeScript diagnostics in `client/src/pages/Docs.tsx`. The diagnostics include Set iteration target errors and implicit `any` errors in Markdown renderers.
- `npm test`: no test script is defined in `package.json`; the command reported “Missing script: test.” No test case pass/fail count is available.
- Preview load: `/` and `/docs` both rendered during this run. The browser console on both pages reported a failed cross-origin request to the tracking endpoint. No other page-load error was captured.
- Human review: none recorded.

## What this does not show

1. The release date for package version `1.0.0` is not declared in the project. The front-matter date is the current summary date, not a verified release date.
2. No automated test suite is configured. Parser and builder interactions were not exercised as part of this run.
3. The production pages were not loaded in a browser. The page check used the Replit preview.
4. The external tracking service and its stored data were not inspected. The preview request failed because of a cross-origin error.
5. The history iframe was present in source but its external content and availability were not checked.
6. No person has reviewed this summary. Human review of the application is not recorded in the project.
7. The full licenses of every direct and development dependency were not checked. The libraries listed under Credits are the checked subset.
8. The code does not establish whether every part of the app was written by a person or an AI tool.

## How to reproduce

- Install declared dependencies with `npm install`.
- Start the development app with `npm run dev`.
- Create a production build with `npm run build`.
- Run the TypeScript check with `npm run check`.
- There is no test command; `npm test` fails because `package.json` has no `test` script.

## Credits and licenses

- Robert Dickinson is the named author in this summary. The recent Git history records commits under `robertdickinson`.
- SWMM is described as public domain in `client/src/data/swmm5-reference.ts:19`. No SWMM engine code is included in the app. The project does not state an EPANET license.
- The app's `package.json:5` declares MIT. No separate license text is summarized here.
- Checked installed package manifests list these licenses: React and React DOM, MIT; Wouter, Unlicense; Vite, MIT; Express, MIT; Tailwind CSS, MIT; Drizzle ORM, Apache-2.0; Zod, MIT; Framer Motion, MIT; Lucide React, ISC; React Markdown, MIT; Next Themes, MIT.
- Outside services named in source include Google Fonts, the Replit-hosted tracking endpoint, and the SWMM History site.

## AI use

- Git metadata marks a Replit Agent commit dated 2026-02-07. Its recorded change adds SWMM history and input-format documentation and the Markdown-rendering dependencies. The commit does not identify a model or itemize generated code.
- Git history records Robert Dickinson as author of recent changes, including the SWMM History tab and interactive learning content. The history does not establish which portions he authored beyond those commit records.
- This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Newest first, from `git log -10 --date=short`:

- 2026-03-16: Add SWMM history timeline and a detailed project handover document.
- 2026-02-12: Published your App.
- 2026-02-09: Add a new tab for SWMM history documentation.
- 2026-02-08: Saved progress at the end of the loop.
- 2026-02-08: Add interactive learning steps with quizzes and examples to the documentation.
- 2026-02-08: Saved progress at the end of the loop.
- 2026-02-08: Apply distinct colors to categorize model sections and their cross-references.
- 2026-02-08: Published your App.
- 2026-02-08: Make the SWMM Explorer tab bar horizontally scrollable for better visibility.
- 2026-02-08: Add ability to view PDF documents directly within the application.
