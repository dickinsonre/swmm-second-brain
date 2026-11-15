---
name: SWMM Ecosystem
file: swmm-history-robertdickinson
version: 1.0.0
date: 2025-08-29
author: Robert Dickinson
links: {replit: "https://swmm-history-robertdickinson.replit.app", repo: "https://github.com/dickinsonre/SwmmHistory"}
engines: none
stack: TypeScript, React, Vite, Express, Tailwind CSS, TanStack Query, Wouter, Canvas API, OpenAI; PostgreSQL and Drizzle scaffolding
units: not applicable
ai_use: Replit Agent development recorded in git; OpenAI chat integration; details below.
---

# SWMM Ecosystem: Explore SWMM history, software, and contributors

Metadata sources: display name in `client/src/pages/home.tsx:252`; version in `package.json:3`; deployment metadata read during this review; repository URL from `git config --get remote.origin.url`.
The date above is the earliest recorded introduction of the current package version, not a separately declared release date: `git log -1 -G '"version".*"1.0.0"' -- package.json` identifies commit `88aef49`, dated 2025-08-29.
Source inspection, counts, and checks below were performed on 2026-11-15, the date returned by `date -u +%F`.

## What it does

SWMM Ecosystem is a reference application for people exploring the history of the Storm Water Management Model and related software.
It presents software timelines, contributor profiles and editorial grades, commercial and open-source catalogs, comparisons, a glossary, diagrams, and change notes.
Readers can browse the reference material and ask an integrated chat assistant questions.
It does not execute drainage models or produce engineering simulation results.
Sources: `client/src/pages/home.tsx:73`, `client/src/App.tsx:14-27`, `server/routes.ts:6-29`.

## How it computes

- **Catalog statistics:** `MemStorage.getSwmmStats`, `server/storage.ts:1293-1338`, counts the catalog arrays. For EPA records, it splits developer labels on comma-space; for other categories, it counts each whole developer string. It computes `percentage = round(developer label count / total catalog records * 100)`, sorts by count, and retains the first ten labels. These are catalog-label frequencies, not market shares. Multiple labels on an EPA record can contribute separately.
- **Elapsed history:** the same function computes `current calendar year - 1969`. This is a calendar difference, not a measurement of uninterrupted maintenance (`server/storage.ts:1337`).
- **Comparison graphics:** `scoreVersion`, `client/src/components/compare-charts.tsx:29-36`, lowercases concatenated feature text and counts matching keywords for each dimension. Its formula is `min(matches / max(keyword count * 0.4, 1), 1)`. The dimensions and keyword lists are defined immediately above that function. Scores are text heuristics, not measured capabilities or hydraulic benchmarks.
- **Contributor profiles:** `reviewedProfile` and `reviewContributorList`, `client/src/lib/reviewed-contributors.ts:29-68`, normalize names, apply reviewed profile overrides, append designated additions, and remove duplicates by canonical name. Grades are stored editorial judgments. No formula derives a grade from repository activity.
- **Hydraulic illustration:** the `animate` callback in `client/src/components/preissmann-slot.tsx:172-193` advances a synthetic water level, reverses its direction at fixed bounds, and adds a sinusoidal disturbance above an era-specific threshold. The display uses normalized drawing coordinates, not a drainage-model solution. Its physical-looking labels do not establish engineering accuracy.
- **Chat:** the registered handler sends conversation history and a fixed system prompt to OpenAI, then streams the response. The configured model is `gpt-4o-mini` (`server/replit_integrations/chat/routes.ts:36-86`, model at line 58). This handler does not implement retrieval from the current catalog.
- **Engine boundary:** the active server registers catalog and chat routes, not a SWMM solver (`server/routes.ts:6-29`). Software versions described in the catalog are reference content, not installed simulation-engine versions.

## Inputs and outputs

| Interface | Input | Output or storage |
| --- | --- | --- |
| Browser pages | Navigation, search, filters, selections | Rendered reference material and Canvas illustrations |
| `/`, `/history`, `/source`, `/changes` | Browser requests | React pages; route definitions in `client/src/App.tsx:14-27` |
| `GET /api/swmm-data` | HTTP request | JSON catalog from server memory |
| `GET /api/swmm-stats` | HTTP request | JSON category counts and developer-label statistics |
| `POST /api/chat` | JSON message and optional session identifier | Server-sent events containing streamed assistant text |
| `DELETE /api/chat/:sessionId` | Session identifier | Deletes that process-local conversation |

API sources: `server/routes.ts:6-29` and `server/replit_integrations/chat/routes.ts:36-99`.
The catalog is embedded in TypeScript and validated against Zod schemas, rather than read from uploaded model files (`server/storage.ts`, `shared/schema.ts`).
Active catalog and chat storage is process memory, not PostgreSQL. PostgreSQL and Drizzle configuration does not establish that these paths persist data there.
Chat sessions are discarded on process restart. Cleanup removes sessions based on creation age after one hour, checked every ten minutes (`server/replit_integrations/chat/storage.ts:12-37`).
Theme and onboarding dismissal use browser local storage (`client/src/components/theme-provider.tsx:22-29`; `client/src/components/onboarding.tsx:89-104`).
No simulation input-file import or engineering result-file export is implemented by the active routes inspected.

## Contents

Counts below come from fresh inspection runs, not earlier documentation.

| Content | Count | Source and counting method |
| --- | ---: | --- |
| Main page routes | 4 | Route declarations, `client/src/App.tsx:17-25` |
| Home tab identifiers | 13 | Array counted in `client/src/pages/home.tsx:73` |
| EPA catalog records | 12 | `MemStorage.getSwmmData()` array length; confirmed by live `/api/swmm-stats` request |
| Commercial and third-party records | 26 | Same run, `Commercial_and_3rdParty` |
| Open-source and academic records | 13 | Same run, `OpenSource_and_Academic` |
| Total catalog records | 51 | Sum of the category lengths returned by that run |
| Home contributor cards | 87 | Fresh TypeScript AST extraction of the literal list at `client/src/pages/home.tsx:2198`, followed by `reviewContributorList` |
| History contributor cards | 45 | Same method for `client/src/pages/history.tsx:17` |
| Glossary entries | 285 | Fresh extraction and key count of the glossary object at `client/src/components/glossary-term.tsx:4` |

Contributor counts describe distinct views with overlapping membership. They must not be added to estimate unique people across the application.

## Checks

- **TypeScript:** `npm run check -- --incremental false` exited successfully with no diagnostics.
- **Automated tests:** the command below passed **15 tests**, failed **0**, skipped **0**, and cancelled **0**, as reported by the test runner.

```sh
npx tsx --test client/src/lib/reviewed-contributors.test.ts server/storage.test.ts server/replit_integrations/audio/storage.test.ts
```

- **Page loads:** fresh development-preview captures of `/`, `/history`, `/source`, and `/changes` rendered their initial views. No browser runtime errors appeared in the returned logs. Home initially showed its onboarding overlay; Source showed its mock viewer.
- **HTTP checks:** fresh requests to those same four development routes each returned HTTP 200. A fresh `GET /api/swmm-stats` request returned JSON with the category counts reported above.
- **Human review recorded in the project:** `client/src/components/list-review-panel.tsx:28-36` explicitly attributes affiliation, identity, and review-scope clarifications to the site owner. These concern Robert Dickinson's affiliation, Mirab's identity, and deferred EPA staffing review. They are not evidence of independent technical validation or approval of this summary.

## What this does not show

1. Historical claims, contributor grades, external commit totals, release schedules, and linked publications were **not checked** against their outside sources in this documentation run. Existing cards are editorial content, not independently verified findings here.
2. Hydraulic accuracy, mass conservation, numerical convergence, calibration, and engineering suitability were **not checked**. No simulation engine was run. Animated behavior and keyword-based comparisons are not evidence of these properties.
3. The Source page is a known limitation: it uses a hardcoded file tree and returns mock file text instead of fetching real source (`client/src/pages/source-code.tsx:29`, `209-217`). External repository and archive links were **not checked** by following them.
4. Live chat responses, streaming failure handling, session isolation under concurrent use, cleanup timing, and OpenAI service availability were **not checked**. Loading the chat interface is not an end-to-end chat test.
5. The production build, published-page behavior, deployment logs, and differences between the deployed revision and this workspace were **not checked**. Deployment metadata confirms a public deployment, not its equivalence to the source inspected.
6. Mobile rendering, keyboard and screen-reader behavior, all home tabs, filters, comparisons, diagrams, local-storage persistence, and onboarding dismissal were **not checked** interactively in this run. The screenshots establish initial page rendering only.
7. Security, authorization, rate limiting, load capacity, dependency vulnerabilities, and test coverage were **not checked**. No security or performance assurance follows from the passing tests.
8. Database connectivity, migrations, persistence, backups, full transitive dependency licensing, and provenance or reuse rights for every external image and linked resource were **not checked**.
9. Independent review of all technical and historical content is **not checked**. Robert Dickinson has not reviewed this summary.

## How to reproduce

Use the repository's Node environment and install dependencies from its lockfile. The install command below is a reproduction instruction, not an additional check performed for this summary.

```sh
npm ci
npm run dev
```

The development script starts the Express server with Vite integration (`package.json:7`; `server/index.ts:39-69`). Open the preview and visit the main routes listed above.
Run the same static check and tests:

```sh
npm run check -- --incremental false
npx tsx --test client/src/lib/reviewed-contributors.test.ts server/storage.test.ts server/replit_integrations/audio/storage.test.ts
```

To inspect the catalog counts against the development server:

```sh
curl -fsS "https://$REPLIT_DEV_DOMAIN/api/swmm-stats"
```

Configured production commands are `npm run build` followed by `npm run start` (`package.json:8-9`). They are documented here, not reported as executed checks.
Chat requires the configured OpenAI integration; no credentials are included in this document.

## Credits and licenses

- **Robert Dickinson:** credited for compilation in `client/src/pages/home.tsx:3750-3786`; owner-supplied corrections are identified in `client/src/components/list-review-panel.tsx:28-36`.
- **SWMM and related projects:** the catalog credits EPA and named developers and contributors. Those references do not mean their engines are bundled or executed by this application.
- **Application license:** MIT is declared in `package.json:5`. No standalone root license file was found during inspection.
- **React, Express, Vite, Tailwind CSS:** MIT, from installed manifests at `node_modules/react/package.json:10`, `node_modules/express/package.json:15`, `node_modules/vite/package.json:5`, and `node_modules/tailwindcss/package.json:5`.
- **TypeScript and the OpenAI SDK:** Apache-2.0, from `node_modules/typescript/package.json:6` and `node_modules/openai/package.json:10`.
- **Wouter:** Unlicense, `node_modules/wouter/package.json:66`.
- **Lucide React:** ISC, `node_modules/lucide-react/package.json:5`.
- **Other used libraries:** TanStack Query, Radix UI components, and Recharts appear in the package dependencies. This list is not a complete dependency-license audit.

## AI use

Git records Replit Agent as the author of recent development commits covering review logic, diagrams, layouts, and page configuration. Source: `git log -5 --format='%ad %an %s' --date=short`, inspected during this review.
The application credits Robert Dickinson for compiling its material and records specific clarifications supplied by him. The inspected evidence does not assign every code change or editorial judgment to a person or tool.
The application also uses OpenAI for its runtime chat assistant. That is separate from evidence about which tools built the application.
No additional AI development tool is established by the sources cited here.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: `git log -10 --format='%ad: %s' --date=short`, read during this review. These are recorded commit subjects, not fresh verification of every behavior.

- 2026-11-05: Published your App.
- 2026-11-05: Update review panel logic and add scope documentation.
- 2026-11-05: Refactor diagram components and update page layouts.
- 2026-11-05: Update page components and environment configuration.
- 2026-04-11: Published your App.
- 2026-04-11: Add detailed commercial software profiles to the ecosystem tab.
- 2026-03-31: Published your App.
- 2026-03-30: Add keyboard navigation and accessibility features to application tabs.
- 2026-03-30: Improve mobile responsiveness and user experience across the application.
- 2026-03-30: Published your App.
