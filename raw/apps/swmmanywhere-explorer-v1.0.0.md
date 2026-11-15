---
name: SWMManywhere Explorer
file: swmmanywhere-explorer
version: 1.0.0
date: 2026-05-13
author: Robert Dickinson
links: {replit: https://swmmanywhere-explorer.replit.app, repo: none}
engines: none
stack: TypeScript, React, Vite, Express, Tailwind CSS, Wouter, TanStack Query, Drizzle ORM, PostgreSQL schema tooling, Google Fonts
units: SI
ai_use: No AI use is documented in the project source.
---

# SWMManywhere Explorer: Reference guide to an urban drainage model generator

## What it does

SWMManywhere Explorer is a browser-based guide to the separate SWMManywhere Python project. It explains how that project describes generating urban drainage network models from a geographic area and global datasets. It presents a repository tree, a pipeline walkthrough, graph functions, data sources, parameters, and validation metrics for people learning about or evaluating that project. This app itself does not generate or simulate a drainage model. [client/index.html:6-9; client/src/pages/explorer.tsx:498-610; replit.md:3-9]

## How it computes

The app does not run scientific calculations or a simulation engine. It displays static TypeScript data from `client/src/lib/data.ts`. The described upstream workflow covers configuration, data acquisition, preprocessing, graph transformations, topology derivation, hydraulic design, SWMM model generation, and validation. The displayed equation `Q = C·i·A` is explanatory text; this app does not evaluate it. [client/src/lib/data.ts:56-329]

The UI performs display and selection operations:

- `FileTreeSection` searches and expands the static repository entries.
- `PipelineSection` displays a selected stage and moves between stages.
- `GraphFunctionsSection` filters the listed functions by category.
- The data source, parameter, and metrics sections render their respective static arrays.
- `ThemeProvider` reads and saves the `theme` preference in browser `localStorage`.

These components are in `client/src/pages/explorer.tsx`; theme persistence is in `client/src/components/theme-provider.tsx:10-27`. No SWMM or PySWMM engine is called by this app.

## Inputs and outputs

- The app reads bundled HTML, CSS, JavaScript, and static TypeScript data. It has no user file-upload flow.
- The client route `/` displays the explorer. Wouter displays a not-found page for unmatched client routes. [client/src/App.tsx:10-15]
- The server registers no application API endpoints. The current page renders the bundled data without requesting model or user data from an API. [server/routes.ts:5-16]
- The visible output is the explorer page. The selected light or dark theme is stored in browser `localStorage`; the app does not write model files or user content to server files.
- PostgreSQL schema and storage scaffolding exist, but the explorer does not use them to store its content. The storage implementation is in-memory. [shared/schema.ts:1-18; server/storage.ts:13-38; drizzle.config.ts:1-14]
- The page requests font files from Google Fonts. [client/index.html:11-13]

## Contents

Counts below are from the static arrays in `client/src/lib/data.ts`.

| Content | Count | Source |
| --- | ---: | --- |
| Repository sections | 5 | `client/src/lib/data.ts:56-140` |
| Listed repository entries | 43 | `client/src/lib/data.ts:56-140` |
| Pipeline stages | 8 | `client/src/lib/data.ts:142-227` |
| Graph functions | 19 | `client/src/lib/data.ts:229-249` |
| Data sources | 3 | `client/src/lib/data.ts:262-290` |
| Key parameters | 9 | `client/src/lib/data.ts:292-302` |
| Metric tiers | 4 | `client/src/lib/data.ts:304-329` |
| Metric labels across those tiers | 18 | `client/src/lib/data.ts:304-329` |

## Checks

- `npm run check`: passed. TypeScript reported no errors.
- `npm run build`: passed. The build emitted a stale Browserslist data warning and a PostCSS `from` option warning.
- Main page: development request to `/` returned HTTP 200. The page rendered in the browser preview. The browser log contained Vite connection and React DevTools informational messages, with no browser errors.
- Human review: none recorded.

## What this does not show

1. A formal release date for version `1.0.0` is not recorded. The front matter uses the newest date in Git history, whose entry says “Published your App.” It is not verified as the formal version date. [package.json:1-5; Git history]
2. Automated tests were not checked. `npm test` could not run because `package.json` defines no test script; zero tests were executed. Tab navigation, search, theme persistence, and other interactions were not checked. [package.json:6-11]
3. The upstream workflow, equation, dataset descriptions, and simulation claims are static reference content. This app does not independently validate them by running SWMManywhere.
4. The app's public repository URL was not checked. The app links to the separate upstream SWMManywhere repository, not a verified public repository for this explorer. [client/src/pages/explorer.tsx:518-520]
5. Google Fonts font licenses were not checked. The page requests fonts from Google Fonts. [client/index.html:11-13]
6. The project source does not record AI tools used to build the app or Robert Dickinson's specific development contributions; those details were not checked outside the project files.
7. No person has recorded a review of this summary in the project.

## How to reproduce

- Run the development app: `npm run dev`
- Run the TypeScript check: `npm run check`
- Build the app: `npm run build`

The commands are defined in `package.json:6-11`.

## Credits and licenses

- Robert Dickinson is the author named for this summary. The project files reviewed do not describe his specific development contributions.
- The explorer links to SWMManywhere by Imperial College London. The page identifies that separate project as BSD-3-Clause licensed. [client/src/pages/explorer.tsx:518-520,543-547,605-608]
- This app's `package.json` declares MIT. [package.json:1-5]
- Selected direct libraries and their installed package license fields: React and React DOM (MIT), Vite (MIT), Express (MIT), Tailwind CSS (MIT), TanStack Query (MIT), Radix Tabs (MIT), date-fns (MIT), Framer Motion (MIT), Recharts (MIT), Drizzle ORM (Apache-2.0), TypeScript (Apache-2.0), Lucide React (ISC), and Wouter (Unlicense). License fields were read from each package's `node_modules/<package>/package.json`.
- The page requests fonts from Google Fonts. [client/index.html:11-13]

## AI use

The project source and documentation reviewed do not record which AI tools, if any, helped build the app. They do not describe Robert Dickinson's development work. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Newest first, from `git log --date=short`:

- 2026-05-13: Published your App
- 2026-05-12: Published your App
- 2026-02-11: Saved progress at the end of the loop
- 2026-02-11: Add theme switching and improve exploration page layout
- 2026-02-11: Extracted stack files
- 2026-02-11: Initial commit
