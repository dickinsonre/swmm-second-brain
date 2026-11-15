---
name: InfoSewer to InfoWorks ICM
file: data-sewer-robertdickinson
version: 1.0.0
date: 2026-02-12
author: Robert Dickinson
links: {replit: https://infosewericminfoworksimport.com, repo: none}
engines: none
stack: TypeScript, React, Wouter, Tailwind CSS, Vite, Express, Node.js 20, Replit hosting, Google Fonts, Font Awesome CDN
units: US customary
ai_use: No AI tool attribution is recorded in the checked project sources.
---

# InfoSewer to InfoWorks ICM: Guides and checks a network conversion workflow

## What it does

The app explains how to move InfoSewer model data into InfoWorks ICM for sewer modelers. It presents a linked Ruby import tool as the preferred conversion method and documents a manual ODIC workflow as an alternative. The app provides browser tools for checking IDs and CSV headers, composing SQL text, tracking setup readiness, and looking up common errors. It does not itself convert or import a model. (client/src/data/app-data.json:45-101,117-129; client/src/components/step-content.tsx:283-309,414-543,545-689,691-835,837-857)
Package metadata lists version 1.0.0. (package.json:3)

## How it computes

- The guide content is static data and page components. The preferred Ruby importer and external conversion resources are linked, not executed by this app. No simulation or conversion engine is included. (client/src/data/app-data.json:45-101, client/src/components/step-content.tsx:16-26,957-1018)
- `ComparisonCalculator` sums hard-coded time estimates. The older workflow totals 182 minutes, the newer workflow totals 28 minutes, and the displayed difference is 154 minutes, or 2 hours 34 minutes. These are estimates in the code, not measured runs. (client/src/components/step-content.tsx:197-219)
- `NodeIdChecker.analyze` splits entered IDs on commas or newlines, checks naming rules, proposes corrected IDs, and builds SQL update text. The length check is 40 characters. The SQL is displayed or copied; the app does not execute it. (client/src/components/step-content.tsx:283-309)
- `CsvFieldValidator` reads pasted headers or the first line of an uploaded CSV file. It normalizes headers to uppercase, checks them against the selected step's required fields, and computes `present fields / required fields * 100`. It does not inspect the CSV's data rows. (client/src/components/step-content.tsx:414-453)
- `SqlScriptBuilder` joins selected fixed SQL snippets into one script. It does not connect to or execute against a database. (client/src/components/step-content.tsx:545-689)
- `ReadinessChecklist` computes `checked items / total items * 100`. Conversion completion is counted across the nine manual steps. The checklist and conversion progress are stored in browser localStorage. (client/src/components/step-content.tsx:691-762; client/src/hooks/use-conversion-progress.tsx:17-24,63-92)

## Inputs and outputs

- Users enter IDs and CSV headers as text. The CSV validator also reads a `.csv` file in the browser and uses its first line. The file is not sent to the server. (client/src/components/step-content.tsx:283-309,414-453)
- The app displays validation results, proposed SQL, guide content, and checklist status. The ID checker and SQL builder offer clipboard copying. No model file or report is written by the app. (client/src/components/step-content.tsx:307-314,630-635,674-685)
- Browser localStorage holds the current guide section, completed conversion steps, theme, dark-mode preference, and checklist state. (client/src/hooks/use-conversion-progress.tsx:31-77; client/src/hooks/use-theme.tsx:101-117,141-157; client/src/components/step-content.tsx:692-757)
- The client route is `/`; other client paths render the not-found page. The Express route registration contains no API endpoints. The server has an in-memory user-store template and a Drizzle user schema, but the registered routes do not use them. (client/src/App.tsx:11-16; server/routes.ts:5-14; server/storage.ts:7-38; shared/schema.ts:6-18)
- The app does not store user data in a database. No database connection is used by the registered routes. (server/routes.ts:5-14; server/storage.ts:13-38)

## Contents

- Nine manual conversion-step records are in the app data. (client/src/data/app-data.json:137-147,511-571)
- The interface provides four browser tools: ID checker, CSV validator, SQL builder, and readiness checklist. (client/src/components/step-content.tsx:976-979)
- The CSV validator has nine step-specific required-field sets. (client/src/components/step-content.tsx:419-429)
- The SQL builder contains seven preset scripts. (client/src/components/step-content.tsx:549-627)
- The readiness checklist contains 14 items. (client/src/components/step-content.tsx:694-738)
- The error lookup contains 19 records. (client/src/components/step-content.tsx:837-857)
- The theme data lists eight color themes. (client/src/data/app-data.json:24-35)

## Checks

- `npm run check`: passed. (command run during this summary; script is package.json:10)
- `npm test`: unavailable. The command exited because package.json has no `test` script; zero tests ran. (package.json:6-11; command run during this summary)
- Loaded `/` in the development preview. The conversion guide rendered. The HTTP response was 200.
- Loaded an unknown path in the development preview. The not-found page rendered. The development server returned the client application shell with HTTP 200.
- The browser console recorded an “Invalid hook call” warning and invalid `React.Fragment` prop warnings associated with `Sidebar` and `WorkflowMapper`. The guide remained visible. (browser console captured during this summary)
- Human review: none recorded.

## What this does not show

1. There is no configured automated test suite. Interactions such as CSV file selection, clipboard copying, saved-state restoration, and keyboard navigation were not exercised.
2. A production build was not run. Production-only behavior and the published page were not checked in this run.
3. The cause and effect of the browser-console warnings were not investigated.
4. The linked Ruby conversion tool was not downloaded or run. No real InfoSewer model was converted or validated.
5. The project records no formal release date. The front matter date is the newest source commit date shown by `git log`, not a tagged release date.
6. The checked project files do not record which AI tools assisted with app development or which work Robert Dickinson performed beyond commits attributed to him. No person has recorded a review of this summary.

## How to reproduce

```sh
npm install
npm run dev
npm run check
```

The Replit workflow also starts the app with `npm run dev`. For a production build and start, package scripts are `npm run build` and `npm start`. No test command is configured. (package.json:6-11; .replit:1-3)

## Credits and licenses

- Robert Dickinson is the author named for this summary. The recent Git commits are attributed to `robertdickinson`. (git log)
- The project declares MIT in package.json. No root-level license file was found. (package.json:5)
- React and React DOM: MIT. Wouter: Unlicense. TanStack Query: MIT. Express: MIT. Vite: MIT. Tailwind CSS: MIT. Radix UI: MIT. Zod: MIT. (installed package metadata under node_modules)
- Drizzle ORM and drizzle-zod: Apache-2.0. Class Variance Authority: Apache-2.0. Lucide React: ISC. (installed package metadata under node_modules)
- Google Fonts, Font Awesome, and the linked Innovyze Open-Source-Support conversion resources are referenced by the project. Their applicable licenses were not checked. (client/src/index.html:6-8; client/src/index.css:1-2; client/src/data/app-data.json:100-101)

## AI use

The checked project code and documentation do not name an AI tool that built the app. Git history attributes the inspected commits to Robert Dickinson, but does not identify AI assistance or divide the work by author. The project files do not provide a more detailed account of Robert Dickinson's contributions.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-02-12: Added the interactive conversion toolkit. (git log)
- 2026-02-12: Added a recommended import path and identified the manual process as a fallback. (git log)
- 2026-02-12: Enhanced the conversion guide. (git log)
- 2026-02-11: Published the app. (git log)
- 2026-02-11: Updated the guide to feature the new import tool and historical methods. (git log)
- 2026-02-11: Added a last-updated date to the overview. (git log)
- 2025-08-23: Adjusted the page layout for screen sizes. (git log)
- 2025-08-16: Added the interactive web guide. (git log)
