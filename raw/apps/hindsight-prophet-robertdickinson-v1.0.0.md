---
name: Hindsight Prophet
file: hindsight-prophet-robertdickinson
version: 1.0.0
date: 2025-11-22
author: Robert Dickinson
links: {replit: "https://hindsight-prophet-robertdickinson.replit.app", repo: none}
engines: none
stack: TypeScript, JavaScript, React, Vite, Tailwind CSS, Express, Node.js, Drizzle ORM, PostgreSQL, Neon, OpenAI SDK, OpenRouter, Google Gemini, Google Fonts
units: not applicable
ai_use: Gemini generates advisory text; Replit Agent development is recorded in git.
---

# Hindsight Prophet: AI-assisted advice for legacy stormwater modeling decisions

## What it does
Hindsight Prophet answers technical and strategic questions about stormwater models and engineering ideas.
Its interface targets people maintaining legacy stormwater models.
Users can submit an idea, compare alternatives, and supply model context.
The app returns persona analyses, confidence labels, references, a consensus, and an implementation roadmap.
Sources: `client/src/components/prophet/WelcomeScreen.tsx:418-422`, `server/routes.ts:194-255,285-451`.

## How it computes
- `InputSection.tsx`, `detectPlatform` and `parseModelPaste`, recognize SWMM or InfoWorks ICM terminology and extract text fields using regular expressions. They do not solve hydraulic equations (`client/src/components/prophet/InputSection.tsx:48-120`).
- `server/routes.ts`, `buildUserPrompt`, assembles the question, comparison labels, and application context into text (`194-255`).
- `getRecentSessionContext` adds summaries from the latest 3 database consultations. This is shared database history, not history filtered by user (`server/routes.ts:257-283`; `server/storage.ts:48-54`).
- `runCouncil` sends persona requests concurrently through the OpenAI SDK to OpenRouter's `google/gemini-2.5-pro`. Standard mode uses 4 personas; full mode adds 2 (`server/routes.ts:50-168,285-321`).
- Persona requests use temperature 0.7 and a 4,000-token output limit. The synthesis request uses temperature 0.7 and an 8,000-token limit (`server/routes.ts:298-306,417-425`).
- `parseConfidenceAndSources` extracts confidence tags and a trailing sources list. Missing confidence defaults to MEDIUM (`server/routes.ts:170-191`).
- Failed persona requests become LOW-confidence unavailable messages. Synthesis uses successful responses; the code does not require a minimum successful council size (`server/routes.ts:321-338,349-355,386-391`).
- Synthesis text is split at CONSENSUS and IMPLEMENTATION ROADMAP headings. Missing or short sections trigger text fallbacks (`server/routes.ts:427-451`).
- `ResultsView.tsx`, `computeVerdict`, calculates a display score: HIGH = 90, MEDIUM or missing = 60, LOW = 30; score = round(sum(scores) / max(number of responses, 1)). This is a heuristic, not a calibrated probability (`115-137`).
- That function counts matching negative, conditional, and positive phrases. It selects RECONSIDER, CONDITIONAL, or otherwise PROCEED (`client/src/components/prophet/ResultsView.tsx:123-137`).
- `ResultsView`, `verdictTally`, counts parsed A, B, and DEPENDS comparison labels (`client/src/components/prophet/ResultsView.tsx:93-103,167-177`).
- `registerRoutes` builds journey previews and concatenates saved roadmap entries. It does not recompute a unified engineering plan (`server/routes.ts:622-680`).
- No simulation engine is invoked in the inspected request path. SWMM and ICM are advisory context, not executable solvers.

## Inputs and outputs
Inputs are form text, pasted model summaries, and JSON request bodies. Model summaries are parsed as text, not loaded as executable model files.

| Route | Purpose |
| --- | --- |
| `GET /` | Main client application |
| `POST /api/prophecy` | Accept idea, councilMode, and queryMode; generate and save advice |
| `POST /api/oracle/ask` | Accept question, optional context, and councilMode; return structured advice |
| `GET /api/oracle/health` | Report configuration status and API metadata |
| `GET /api/stats` | Return stored consultation count |
| `GET /api/prophecies` | Return recent consultations |
| `GET /api/journey` | Return chronological session previews and saved roadmaps |
| `GET /api/prophecy/:id` | Find a saved consultation among the recent records |

Sources: `client/src/App.tsx:9-15`; `server/routes.ts:454-698`.

- PostgreSQL stores original questions, persona JSON, consensus, roadmap text, and timestamps. A users table also exists (`shared/schema.ts:6-33`; `server/storage.ts:35-58`).
- Neon supplies the PostgreSQL connection through Drizzle (`server/db.ts:1-15`).
- Browser localStorage holds up to 20 recent question summaries under `prophet_history` (`client/src/components/prophet/ResultsView.tsx:181-190`).
- Reports download as `.txt` files. Clipboard copying and browser sharing are available (`client/src/components/prophet/ResultsView.tsx:140-149,192-246`).
- Report files are generated in the browser, not persisted as server files by `downloadReport`.
- Questions, context, and recent-session summaries are sent to the model provider (`server/routes.ts:294-306`).

## Contents
Counts below are source counts or observations from the development app on 2026-11-15.

| Item | Count | Source |
| --- | ---: | --- |
| Explicit application page routes | 1 | `client/src/App.tsx:12`; separate unmatched-route fallback at line 13 |
| Main view states | 4 | welcome, input, processing, results; `client/src/pages/ProphetPage.tsx:9` |
| Council personas | 6 | `server/routes.ts:52,71,90,109,131,150` |
| Distinct configured generative model identifiers | 1 | Same identifier at `server/routes.ts:299,418` |
| Declared database tables | 2 | `shared/schema.ts:6,20` |
| Stored consultations reported by development API | 12 | Current `GET /api/stats` returned `totalQueries: 12` |
| Journey sessions and roadmap entries | 12 each | Current `GET /api/journey`: totalSessions, sessions.length, strategicRoadmap.length |

Database counts describe the current development API response, not a production database audit.
Version 1.0.0 comes from `package.json:3`.
The version date is its first observed occurrence in git, 2025-11-22, not a verified release date.
Evidence: `git log --diff-filter=A -1 --format='%ad' --date=short -- package.json`, followed by reading that commit's `package.json:3`.
The deployed name and URL were retrieved from current deployment metadata on 2026-11-15.
No public GitHub repository URL was recorded by `git remote -v`; the recorded origin is an internal Replit host.

## Checks
Checks performed on 2026-11-15:

- `npm test`: failed to start because the project has no test script. Test cases executed: 0; passed: 0; failed: 0. This is a missing test runner command, not a passing suite. Source: command output and `package.json:6-13`.
- `npm run check -- --incremental false`: passed, exit status 0, with no TypeScript diagnostics. This checks types, not runtime behavior.
- Development HTTP reads using Node fetch against the workspace preview domain: `/`, `/api/oracle/health`, `/api/stats`, and `/api/journey` each returned HTTP 200. Requests passed: 4; failed: 0.
- A browser screenshot loaded `/` at 1280 by 720 pixels. The welcome page and journey summary rendered. The capture's browser log contained Vite connection messages and the React DevTools notice, with no errors reported.
- Human review: none recorded in the inspected project material.

## What this does not show
1. Live AI generation, model availability, output quality, citation accuracy, and provider billing were not checked. No consultation was submitted.
2. Input, processing, results, comparison interactions, saved-session reopening, exports, clipboard sharing, mobile layout, and the unmatched-route screen were not checked in the browser. They are not covered by the welcome-page screenshot.
3. Production pages, production records, and parity between deployed code and workspace code were not checked.
4. Database writes, migrations, authentication, authorization, rate-limit enforcement, security, accessibility, load, and timeout behavior were not checked.
5. A production build was not checked. No automated test cases ran because the test command is absent.
6. Engineering correctness and professional review of generated advice were not checked. No human review of this summary or generated advice is recorded.
7. Dependency license metadata was read for the libraries credited below. A complete transitive dependency, font, icon-content, and service-terms audit was not checked.
8. Current route and storage code does not scope consultations or recent-session context to a user (`server/routes.ts:257-283,611-698`; `server/storage.ts:48-58`). The implications for multiple users were not checked at runtime.
9. Confidence percentages are arbitrary display mappings. References are generated by the language model and are not independently verified (`server/routes.ts:565`; `ResultsView.tsx:115-137`).
10. Journey and single-session lookup inspect only the latest 100 records (`server/routes.ts:624,691`). Older records may not be reachable through those endpoints.
11. The stats endpoint returns a zero count if storage fails, which can conceal a database error (`server/routes.ts:601-608`).
12. The exported report contains a hardcoded site address different from the deployment address retrieved for this summary (`client/src/components/prophet/ResultsView.tsx:225`). Its destination was not checked.

## How to reproduce
Use an environment with Node.js and npm. Provision the PostgreSQL and OpenRouter configuration required by `server/db.ts:8-15` and `server/routes.ts:8-13` without putting credentials in source files.

```sh
npm ci
npm run dev
npm run check -- --incremental false
npm test
```

The final command currently fails because no test script exists.
For production build and startup, the configured commands are:

```sh
npm run build
npm start
```

These production commands were not checked during this summary.
`npm run db:push` is the configured schema command; it changes the connected database and was not run.
Command sources: `package.json:6-12`.
The server binds all interfaces using the configured port or default 5000 (`server/app.ts:78-88`).
Read-only HTTP checks can be repeated against the running workspace:

```sh
curl -f "https://${REPLIT_DEV_DOMAIN}/"
curl -f "https://${REPLIT_DEV_DOMAIN}/api/oracle/health"
curl -f "https://${REPLIT_DEV_DOMAIN}/api/stats"
curl -f "https://${REPLIT_DEV_DOMAIN}/api/journey"
```

## Credits and licenses
- Robert Dickinson is the author credited for this summary, as requested.
- The project's package declares MIT (`package.json:5`).
- React, Express, Vite, Tailwind CSS, Neon serverless driver, Framer Motion, TanStack React Query, Radix Dialog, and Zod declare MIT.
- TypeScript, Drizzle ORM, and the OpenAI SDK declare Apache-2.0.
- Lucide React declares ISC. Wouter declares Unlicense.
- Library license evidence: the `license` field read from each named package's installed `node_modules/<package>/package.json`.
- OpenRouter and Google Gemini provide inference services. Google Fonts supplies fonts. Their service terms and font licenses were not checked.
- SWMM and InfoWorks ICM are discussed model platforms, not bundled simulation engines in the inspected computation path.

## AI use
Git records Replit Agent as the author of the report redesign, journey navigation, and reliability changes.
Evidence: `git log -5 --format='%ad | %an | %s' --date=short`.
The same log records `robertdickinson` on a publication commit dated 2026-02-08.
Specific manual coding, validation, or engineering review by Robert Dickinson is not established by those records.
No other app-building AI tool was identified in the inspected code, project notes, or recent git history.
At runtime, Google Gemini through OpenRouter generates persona responses and synthesis; these are model roles, not independent human reviewers (`server/routes.ts:285-451`).

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes
Source: `git log -10 --format='%ad %s' --date=short`, newest first. Dates are commit dates, not version releases.

- 2026-07-25: Redesigned results view with new fonts and visual elements.
- 2026-07-25: Enabled journey opening and automatic scrolling.
- 2026-07-24: Recorded app publication.
- 2026-07-24: Improved application reliability and user experience with AI.
- 2026-02-08: Recorded app publication.
- 2026-02-07: Saved progress at the end of the loop.
- 2026-02-07: Added persistent journey and strategic roadmap tracking.
- 2026-02-07: Saved progress at the end of the loop.
- 2026-02-07: Added side-by-side comparison mode.
- 2026-02-07: Added model-aware stormwater analysis mode.
