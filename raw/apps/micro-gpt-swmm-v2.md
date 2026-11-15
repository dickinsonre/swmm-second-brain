---
name: SWMM5 MicroGPT v2
file: micro-gpt-swmm
version: 2
date: 2026-02-16
author: Robert Dickinson
links: {replit: https://micro-gpt-swmm.replit.app, repo: none}
engines: none
stack: React, TypeScript, Vite, Tailwind CSS, Recharts, Express, Node.js, PostgreSQL/Drizzle scaffold, Replit hosting, Google Fonts
units: SI
ai_use: The app trains a small character-level GPT in the browser; project sources do not name a coding AI.
---

# SWMM5 MicroGPT: Explore SWMM5 text with a small character-level GPT

## What it does

The app parses SWMM5 `.INP` text into identifiers, keywords, section names, and short parameter lines (`client/src/lib/inp-parser.ts:12-103`). Users can train a small character-level GPT on built-in or parsed text, inspect its training loss, and generate SWMM-like names. It can also assemble and download a sample `.INP` file using generated identifiers and fixed example data (`client/src/pages/swmm5-microgpt.tsx:112-120, 1132-1195`). It does not run a SWMM5 hydraulic or hydrologic simulation (`client/src/pages/swmm5-microgpt.tsx:1597-1599`).

## How it computes

1. `handleFileUpload` reads a selected text file in the browser. `handleParseINP` passes its text to `parseINP` (`client/src/pages/swmm5-microgpt.tsx:555-564, 540-548`).
2. `parseINP` tracks section headers, extracts node, link, and subcatchment identifiers, collects keywords and short parameter lines, removes duplicates, and builds `allTokens` (`client/src/lib/inp-parser.ts:12-103`).
3. `generateManningTriplets` generates training strings using circular full-pipe geometry: `A = πD²/4`, `R = D/4`, and `Q = (1/n) × A × R^(2/3) × S^(1/2)` (`client/src/lib/inp-parser.ts:105-131`). The app's sample and generated `.INP` settings use SI units, including `FLOW_UNITS CMS` and map units in meters (`client/src/pages/swmm5-microgpt.tsx:71-76, 552`; generated map settings in `client/src/pages/swmm5-microgpt.tsx:201-205`). No US-customary calculation path is present in the inspected code.
4. `runTrainingAsync` builds a character vocabulary, trains the GPT, calculates next-character loss, and updates model parameters with Adam-style moment estimates and a linearly reduced learning rate (`client/src/lib/gpt-engine.ts:181-247`). `gptFwd` implements the model's attention and feed-forward pass (`client/src/lib/gpt-engine.ts:75-98`).
5. `generateSamples` samples characters from the trained model (`client/src/lib/gpt-engine.ts:113-133`). `generateINPFile` combines model-generated names with fixed template sections and example values (`client/src/pages/swmm5-microgpt.tsx:1-205`).

## Inputs and outputs

- Reads pasted `.INP` text and uploaded `.inp`, `.txt`, or `.dat` files as browser text (`client/src/pages/swmm5-microgpt.tsx:555-564, 798-810`).
- Includes one imported Greenville `.INP` sample (`client/src/lib/inp-parser.ts:160`).
- Displays parsed data, training loss, generated terms, comparison results, and a generated `.INP` preview in the browser (`client/src/pages/swmm5-microgpt.tsx:789-830, 920-1128, 1202-1210, 1300-1370`).
- Downloads generated `.INP` content as `microgpt_generated.inp` (`client/src/pages/swmm5-microgpt.tsx:1179-1195`).
- The client app is served at `/`. No API endpoints are registered in `server/routes.ts`. App working data is held in page state; the theme and onboarding choice use browser `localStorage` (`client/src/App.tsx:5-15`; `client/src/components/theme-toggle.tsx:5-23`; `client/src/pages/swmm5-microgpt.tsx:486-501`).
- The repository contains PostgreSQL and Drizzle schema/configuration, but the app routes do not connect its user store to these page flows (`shared/schema.ts:1-18`; `drizzle.config.ts:1-14`; `server/routes.ts:1-17`).

## Contents

- One client application with five tab panels: Data, Train, Generate, Compare, and Help (`client/src/App.tsx:5-15`; `client/src/pages/swmm5-microgpt.tsx:763-790`).
- Two fixed vocabulary datasets: 92 SWMM keyword strings and 40 node-name strings, 132 entries total. Counts were read from the array literals in `client/src/lib/inp-parser.ts:134-158` using a TypeScript AST count during this summary.
- One Manning dataset option generates 500 triplets when selected (`client/src/pages/swmm5-microgpt.tsx:570-572`; `client/src/lib/inp-parser.ts:105-131`).
- Five onboarding steps (`client/src/pages/swmm5-microgpt.tsx:356-382`; counted from the source array during this summary).
- Six FAQ entries (`client/src/pages/swmm5-microgpt.tsx:1591-1615`; counted from the source entries during this summary).

## Checks

- Tests: `npm test` was run. It exited with an error because `package.json` defines no `test` script. No tests ran: zero passed and zero failed (`package.json:6-11`; command run during this summary).
- TypeScript: `npm run check` was run and reported six TS2802 errors in `client/src/lib/gpt-engine.ts` and `client/src/lib/inp-parser.ts` (four and two errors, respectively). The command did not pass.
- Page load: the Replit preview loaded `/` and displayed the app with its onboarding dialog. Browser logs showed Vite connection messages and a React DevTools notice, with no app error. The five tab panels are part of this single page (`client/src/pages/swmm5-microgpt.tsx:763-790`).
- Human review: none recorded.

## What this does not show

1. The training, file upload, comparison, generation, and download interactions were not exercised in this run.
2. The individual tab panels were not opened in the preview. Only the root page was captured.
3. The production build command, `npm run build`, was not run. The preview check used the development server.
4. No test suite is configured, and no person’s review is recorded in the inspected project files or Git history.
5. Generated `.INP` output was not checked with a SWMM engine. The app does not run a SWMM simulation.
6. Licenses for the external projects cited by the app are not stated in the project sources.
7. No formal release date is recorded. The frontmatter date uses the newest date in the inspected Git history (`git log -10`).

## How to reproduce

- Start the development app: `npm run dev` (`package.json:6-11`).
- Run the TypeScript check: `npm run check` (`package.json:6-11`). It currently reports the errors listed under Checks.
- Build and start the production app: `npm run build` followed by `npm start` (`package.json:6-11`; deployment configuration in `.replit:15-19`).
- No test command is defined in `package.json`.

## Credits and licenses

- Robert Dickinson is the requested author. The project files do not describe his specific implementation work.
- The project declares the MIT license (`package.json:1-5`).
- React, React DOM, Vite, Tailwind CSS, Recharts, and Express declare MIT licenses in their installed package manifests. TypeScript declares Apache-2.0. Lucide React declares ISC. These licenses were read from the installed package manifests during this summary.
- The app credits Andrej Karpathy's `micrograd`, Xenova's `microgpt.js`, and SWMM5.org (`client/src/pages/swmm5-microgpt.tsx:1532-1547`). Their licenses are not stated in the project files.
- The app references Google Fonts from `client/index.html:11-13`. Font licenses were not checked.

## AI use

The app implements a small GPT and autograd engine in TypeScript (`client/src/lib/gpt-engine.ts:13-34, 75-98`). The project says it is based on Karpathy's `micrograd` and Xenova's `microgpt.js` (`replit.md:4-6`). The inspected code, configuration, and project documentation do not identify a coding AI or describe which tool built the app. Robert Dickinson is named as author, but the project does not record his specific development contributions.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: `git log -10`, newest first.

- 2026-02-16: Saved progress at the end of the loop.
- 2026-02-16: Add a new data generator for Manning's equation triplets.
- 2026-02-15: Published your App.
- 2026-02-15: Published your App.
- 2026-02-15: Expand model training options for deeper analysis.
- 2026-02-15: Add detailed explanation about training loss to the FAQ section.
- 2026-02-15: Published your App.
- 2026-02-15: Add training tips to the help section for better model generation.
- 2026-02-15: Add trending up icon to improve application documentation.
- 2026-02-15: Add interactive scenarios to guide users through tool functionalities.
