---
name: Historical Water Inventions
file: historical-mystery-robertdickinson
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://historical-mystery-robertdickinson.replit.app, repo: https://github.com/dickinsonre/HistoricalWaterInventions}
engines: none
stack: TypeScript, React, Vite, Express, Tailwind CSS, Zustand, TanStack Query, Anthropic SDK, OpenAI SDK
units: SI
ai_use: Anthropic Claude chatbot; project files do not record AI authorship.
---

# Historical Water Inventions: Explore historical water engineering through interactive maps and calculators

## What it does

The app lets users explore water engineering inventions by civilization, historical site, and period. It presents map and timeline navigation, invention detail pages, quizzes, interactive hydraulic calculators, and a chatbot for water-engineering questions. Users can adjust calculator inputs, inspect historical descriptions and diagrams, and download prepared SWMM5 model files. It is an educational reference and visualization app, not a general-purpose hydraulic design package.

## How it computes

Historical entries are read from structured TypeScript data in `client/src/data/gameData.ts`; the app does not calculate historical dates or claims. The `WaterFlowSimulation` component calculates channel area as `A = width × depth`, wetted perimeter as `P = width + 2 × depth`, and hydraulic radius as `R = A / P`. It then uses Manning's equation, `V = (1/n) × R^(2/3) × S^(1/2)`, and calculates discharge as `Q = V × A` (`client/src/components/game/WaterFlowSimulation.tsx:286-330`; equation and SI velocity units are shown in `client/src/components/game/ManningsNSection.tsx:244-265`). `IrrigationCanalSimulator` applies the same method to its adjustable canal dimensions and roughness (`client/src/components/game/simulators/IrrigationCanalSimulator.tsx:20-27`).

The app does not run EPA SWMM5 or another external hydraulic solver. It stores prepared SWMM5 input text and offers it for download (`client/src/data/swmm5CustomINP.ts:1`; `client/src/lib/swmm5Export.ts:4992`).

## Inputs and outputs

- Browser routes include `/`, `/simulators`, `/mannings-n`, `/vr`, `/minigames`, `/:civilizationId`, and invention detail routes (`client/src/App.tsx:40-49`).
- Users provide navigation, search, quiz choices, calculator settings, and chatbot text. The chatbot endpoint is `POST /api/chat`; it streams generated text from Anthropic (`server/routes.ts:91-139`).
- Progress uses `GET /api/progress` and `POST /api/progress`. The browser store persists progress with Zustand's local-storage middleware and also sends it to the server (`client/src/lib/stores/useProgress.tsx:28-30,84-119`).
- The server's progress store is an in-memory map, not a persistent database (`server/storage.ts:29-38,57-68`). Language and quest preferences also use browser local storage (`client/src/lib/stores/useLanguage.tsx:41-48`; `client/src/components/game/QuestSystem.tsx:473-482`).
- Output includes rendered pages, streamed chatbot text, and downloadable `.inp` model files. No user file-import flow was checked.

## Contents

Counts below were recalculated by importing the current data modules with `npx tsx` on 2026-11-15.

- 221 civilization/region records, 404 historical sites, and 1,286 invention records (`client/src/data/gameData.ts:57`).
- 20 interactive simulator entries (`client/src/components/game/simulators/index.ts:22`).
- 12 custom SWMM5 input templates (`client/src/data/swmm5CustomINP.ts:1`).

## Checks

- `npm run check` failed with 11 TypeScript diagnostics across 6 files in the run made on 2026-11-15. The reported issues include a missing `Confetti` module, type errors in `client/src/components/ui/interface.tsx`, `p-retry` errors in `server/replit_integrations/batch/utils.ts`, missing database/schema imports in `server/replit_integrations/chat/storage.ts`, optional image-response data in `server/replit_integrations/image/client.ts` and `server/replit_integrations/image/routes.ts`, and a Vite `allowedHosts` type error in `server/vite.ts`.
- Browser captures rendered `/`, `/simulators`, `/mannings-n`, `/minigames`, `/malaysia`, `/malaysia/lombong`, and `/malaysia/lombong/details/diagram`. Captured browser logs showed no runtime exceptions and included 2 React Router future-flag warnings (browser check run on 2026-11-15).
- `GET /vr` returned HTTP 200, but the browser screenshot timed out on both capture attempts (local route check on 2026-11-15).
- Human review: none recorded in the checked project files.

## What this does not show

1. No automated test command is defined in `package.json`; automated tests were not checked.
2. The visual appearance and interactive states of `/vr` were not checked because screenshot capture timed out. Captures of other routes showed only their initial view.
3. The prepared SWMM5 files were not opened or run in EPA SWMM5 or InfoWorks ICM.
4. Historical and engineering claims were not independently fact-checked. No human review is recorded.
5. Individual dependency license terms were not checked. The production build command was not run.

## How to reproduce

```bash
npm install
npm run dev
npm run check
```

`npm run dev` starts the development server (`package.json:6-11`; `.replit:1-3`). The TypeScript check currently reports the errors listed above. The package also defines `npm run build` and `npm run start`; those commands were not run for this summary (`package.json:6-11`).

## Credits and licenses

- Robert Dickinson is credited as the project creator in `README.md:75-80`, as a curator in `client/src/data/expertInventions.ts:43`, and in model records in `client/src/data/waterSimModels.ts`.
- The project declares the MIT License (`LICENSE`; `package.json:5`).
- Libraries named in the manifest include React, React Router, Vite, Express, Tailwind CSS, Zustand, TanStack Query, Drizzle ORM, `@anthropic-ai/sdk`, and `openai` (`package.json:13-129`). Their individual licenses were not checked.
- EPA SWMM5 and InfoWorks ICM are named as model compatibility targets in `replit.md:111-113`. Their license terms and compatibility of the supplied files were not checked.

## AI use

The project files do not document which AI tools contributed to building the app or divide the work between AI and Robert Dickinson. The active `/api/chat` route uses Anthropic's Claude Haiku model (`server/routes.ts:4-9,121-125`). The Replit config names Anthropic and OpenAI AI integrations (`.replit:18-19`). OpenAI integration modules exist in the source, but the current server startup registers only `registerRoutes` (`server/index.ts:1-3,39-40`); their use as active routes was not verified. Project files credit Robert Dickinson as creator and curator, but do not itemize his software contributions.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

From `git log -10`, newest first, checked on 2026-11-15:

- 2026-11-15: Add four custom SWMM5 model downloads
- 2026-11-15: Git commit prior to merge
- 2026-07-23: Published your App
- 2026-07-22: Published your App
- 2026-07-22: Add interactive labeled hotspots to the six new modern diagrams
- 2026-07-22: Add historical sites and custom image for Malaysia
- 2026-07-22: Fix 12 duplicate artifact IDs so invention links always open the right page
- 2026-07-22: Post-merge setup completed successfully
- 2026-07-22: Give the 59 new modern inventions diagrams and SWMM5 models like older entries
- 2026-07-22: Complete Kazakhstan's civilization page with new imagery and details
