---
name: SWMM5Wiki
file: gator-swmm-robertdickinson
version: 1.0.0
date: 2025-08-28
author: Robert Dickinson
links: {replit: "https://gatorbeaverswmm.com", repo: none}
engines: none
stack: TypeScript, React, Vite, Wouter, TanStack Query, Express, Node.js, Drizzle schema packages, in-memory storage, Google Fonts, Replit hosting
units: US customary
ai_use: The project's source and documentation do not record AI tools used to build the app.
---

# SWMM5Wiki: An educational guide and quiz about SWMM

## What it does

SWMM5Wiki presents educational material about the Storm Water Management Model, including its hydrology, hydraulics, history, conceptual model, and low impact development controls. Readers can browse sections, search content, view a glossary, and change the display theme. A separate game page presents stormwater modeling challenges in multiple-choice, written-response, and design-answer formats. The app returns educational content, answer feedback, and in-memory progress records; it does not run a stormwater simulation.

## How it computes

1. `MemStorage` initializes the section, glossary, and game scenario data when the server starts (`server/storage.ts:28-48, 179-180, 757-758, 1089-1091`).
2. Express routes return JSON from that storage. The React pages request it through TanStack Query (`server/routes.ts:6-144`, `client/src/pages/home.tsx:26-32`, `client/src/pages/game.tsx:59-65`).
3. In `submitAnswer`, multiple-choice answers are graded by the selected option's `correct` flag. Written responses are graded by case-insensitive substring matches against stored keywords; a response is marked correct when it matches at least two. Its score is the matched-keyword count divided by the stored keyword count, capped at 100 (`client/src/pages/game.tsx:87-106`).
4. Design answers are parsed as numbers and compared with `solution.minDiameter` using a 10% tolerance. Incorrect-answer scores decrease with the absolute difference (`client/src/pages/game.tsx:107-114`). The implementation falls back to a minimum diameter of 18 if that field is absent.
5. Progress updates are written to JavaScript maps in the running server process. No SWMM or other simulation engine is called (`server/storage.ts:28-48, 102-175`; `server/routes.ts:71-89, 122-140`).

## Inputs and outputs

- The app does not read or write user-uploaded files.
- The browser reads section, glossary, progress, and game data as JSON through the `/api` routes (`server/routes.ts:6-140`).
- The API supports section and glossary reads and creation, user progress reads and updates, scenario reads by ID or category, and game progress reads and updates (`server/routes.ts:8-140`).
- New content and progress are held in server memory. They are not persisted by the storage implementation and are lost when that process restarts (`server/storage.ts:28-48, 75-99, 102-175`).
- PostgreSQL table definitions exist in `shared/schema.ts:6-55`, and Drizzle configuration expects a database URL (`drizzle.config.ts:1-12`). The server imports `MemStorage`, not a database-backed storage implementation (`server/routes.ts:1-4`, `server/storage.ts:28-48, 1146`).

## Contents

- Main client pages: the learning page at `/` and the game page at `/game` (`client/src/App.tsx:11-17`).
- Educational sections: 5, confirmed by the development `/api/sections` response and defined in `server/storage.ts:758-1072`.
- Glossary terms: 8, confirmed by the development `/api/glossary` response and defined in `server/storage.ts:1089-1143`.
- Game scenarios: 16, confirmed by the development `/api/game/scenarios` response and defined in `server/storage.ts:180-740`.
- No simulation engine is bundled or called (`server/storage.ts:28-48`; `server/routes.ts:1-4`).

## Checks

- `npm run build`: passed. Vite and esbuild completed successfully on 2026-11-15.
- `npm run check`: failed with 1 TypeScript diagnostic at `server/storage.ts:97`. The `category` value may be `undefined` where the `GlossaryTerm` type requires `string | null`.
- `npm test`: no tests ran. The command failed because `package.json` defines no `test` script.
- Main page `/` and game page `/game`: both loaded in the development preview on 2026-11-15. No browser console errors were observed.
- Human review: none recorded.

## What this does not show

1. Individual quiz submissions, all challenge types, API write validation, and progress behavior after a server restart were not tested.
2. The published pages and mobile layouts were not checked during this run. The page checks used the development preview.
3. No human review is recorded in the project.
4. The game page currently displays “SWMM5 and ICM,” and a stored scenario still compares ICM and SWMM routing (`client/src/pages/game.tsx:219-225`, `server/storage.ts:613-616`).
5. The design-answer grader always reads `solution.minDiameter` and shows a pipe-diameter input. A storage-node scenario stores `orificeDiameter` instead, so that scenario is not graded against its stored solution (`client/src/pages/game.tsx:107-114, 355-383`, `server/storage.ts:361-379`).
6. `package.json` has no release date for version 1.0.0. The front-matter date uses the newest date present in the inspected Git log, 2025-08-28 (`git log -10`).

## How to reproduce

```sh
npm install
npm run dev
npm run build
npm run start
npm run check
npm test
```

`npm run dev` starts the development server. `npm run start` serves the production build after `npm run build`. The project has no test command configured, so `npm test` reports a missing script.

## Credits and licenses

- Robert Dickinson is the author named for this summary. Git history records commits by `robertdickinson`.
- The app content names the U.S. Environmental Protection Agency's SWMM. The app does not bundle or call the SWMM engine (`server/storage.ts:765-770`; `server/routes.ts:1-4`).
- Key libraries and their installed package metadata licenses: React, MIT; Express, MIT; Vite, MIT; Wouter, Unlicense; TanStack Query, MIT; Drizzle ORM, Apache-2.0; Zod, MIT; Lucide React, ISC.
- `package.json` declares the project license as MIT. No separate license file was found.
- The client loads typefaces from Google Fonts (`client/index.html:6-8`).

## AI use

The project source and documentation do not identify AI tools used to build the app. Git history attributes its recorded changes to `robertdickinson`, but does not document his specific work beyond commit subjects.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2025-08-28: Update quiz content to consistently refer to SWMM
- 2025-08-28: Make SWMM questions more challenging with advanced hydraulics
- 2025-08-28: Add detailed content on conceptual models and LID development
- 2025-08-28: Add new questions and images to enhance learning content
- 2025-08-28: Add expert-level questions comparing hydraulic modeling implementations
- 2025-08-28: Update page title to reflect SWMM5Wiki only
- 2025-08-28: Add link to the ICM Hub for external resource access
- 2025-08-28: Update website title and description to include ICM
- 2025-08-28: Add advanced questions on SWMM5 and InfoWorks ICM integration and control
- 2025-08-28: Update title to reflect SWMM5 and ICM challenge options
