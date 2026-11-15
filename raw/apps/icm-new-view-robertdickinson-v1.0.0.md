---
name: ICM InfoWorks
file: icm-new-view-robertdickinson
version: 1.0.0
date: 2025-11-13
author: Robert Dickinson
links: {replit: "https://icm-new-view-robertdickinson.replit.app", repo: none}
engines: none
stack: TypeScript, React, Vite, Express, Tailwind CSS, Radix UI, TanStack Query, p5.js, Recharts, Zod, in-memory storage, Anthropic, Google Gemini, OpenAI, OpenRouter
units: SI
ai_use: Hosted language models answer release-history questions; recorded development commits name Replit Agent.
---

# ICM InfoWorks: Explore InfoWorks ICM release history and upgrade changes

## What it does

The app answers questions about changes in Autodesk InfoWorks ICM for modelers and upgrade planners.
Users browse a release timeline, search descriptions, filter categories and release ranges, and compare versions.
Learning paths and interactive diagrams explain selected topics.
Outputs include feature details, charts, downloadable summaries, and AI answers with feature citation links.
Sources: `client/src/pages/home.tsx`, `client/src/components/Header.tsx:21`, and `server/routes.ts`.

The application version is `1.0.0`, from `package.json:3`, not the latest ICM release.
The front-matter date is the earliest recorded package occurrence, not a verified release date.
Source: `git log --diff-filter=A --format='%as %s' -- package.json` and inspection of that revision's package.
The deployment name and URL were verified through deployment metadata during this review.
No public GitHub URL was established. `git remote -v` records an internal repository host.

## How it computes

- `server/storage.ts`, `MemStorage`: loads `versionsData` into a map. `getAllVersions` sorts numeric major and minor version components in descending order.
- `client/src/pages/home.tsx`, `HomePage` / `filteredVersions`: performs case-insensitive substring search over title, description, and category. Category matches are combined with search and inclusive release-date bounds.
- My Stack compares release dates and marks newer releases. It does not remove older releases from the filtered array.
- `client/src/components/FilterPanel.tsx`, `matchesCategory`: groups content using category and keyword rules.
- `client/src/components/CompareVersionsDialog.tsx`, `computeUpgradePath`: selects releases after the older endpoint through the newer endpoint, then counts matching features.
- In that file, `computeCategoryShift` calculates category count / feature count near each endpoint, then subtracts the earlier proportion from the later proportion. Categories can overlap.
- `CompareVersionsDialog.tsx`, `jaccard` / `detectChainsInRange`, and `EvolutionChainsDialog.tsx`, `jaccard` / `detectChains`: tokenize titles and cluster similar features. The similarity threshold is 0.5 in the respective detection functions. These are heuristic links, not verified feature ancestry.
- `client/src/components/VersionCharts.tsx`, `VersionCharts`: aggregates feature counts and keyword-based heatmap categories. Cell intensity is count / reference maximum, using a global or row maximum.
- `client/src/components/diagrams/CapabilityRadarSketch.tsx`, `scoreDomains`: counts keyword matches. The component accumulates counts by release and normalizes by final domain totals. This measures documented mentions, not engineering capability.
- `server/routes.ts`, `buildSystemPrompt`: serializes the complete release dataset into the AI system prompt and requests feature citation markers.

The app also computes illustrative physical quantities in browser diagrams. It does not invoke an Autodesk ICM simulation engine.
US customary quantities would be rainfall depth in inches, intensity in inches per hour, flow in gallons per minute, and head in feet.
The inspected calculators do not implement those outputs. The equations below use their native SI units and must not be evaluated with unconverted US customary inputs.

| Calculation | Method and source |
|---|---|
| Rainfall | `DesignRainfallSketch.tsx:18-44`, `generateHyetograph`: depth = 25 * returnPeriod^0.45 * (durationMinutes / 60)^0.3. Gaussian-shaped weights are normalized to this depth. Intensity = stepDepth * 60 / stepMinutes. Depth is millimeters and intensity is millimeters per hour. |
| Runoff | `RunoffSketch.tsx:27-46`, `scsCumulative`: S = 25400 / CN - 254; Ia = 0.2 * S; Q = 0 when P <= Ia, otherwise Q = (P - Ia)^2 / (P - Ia + S). P, S, Ia, and Q are millimeters. `buildHyetograph` distributes rainfall using normalized weights. |
| Pump operating point | `PumpStationSketch.tsx:19-36`, `pumpHead`, `systemHead`, `findOperatingPoint`: Hp = max(0, shutoff - a * Q^2); Hs = staticHead + k * Q^2; Q = sqrt((shutoff - staticHead) / (a + k)). The no-head-margin branch returns zero flow. Native flow is liters per second; head is meters. |

Diagram paths in this table are under `client/src/components/diagrams/`.
These formulas were read, not numerically validated against engineering benchmarks.

## Inputs and outputs

| Interface | Inputs and outputs |
|---|---|
| Browser | Search text, category selections, version selections, chat text, and diagram controls. |
| `GET /api/versions` | Returns the release dataset as JSON. |
| `GET /api/versions/:id` | Returns a release or a not-found response. |
| `POST /api/chat/claude` | Validated message array; Anthropic response. |
| `POST /api/chat/gemini` | Validated message array; Google Gemini response. |
| `POST /api/chat/openai` | Validated message array; OpenAI response. |
| `POST /api/chat/deepseek` | Validated message array; DeepSeek through OpenRouter. |
| Export | Filtered features as CSV or Markdown; comparison Markdown. |

Sources: `server/routes.ts:43-224`, `shared/schema.ts`, `client/src/lib/exportFeatures.ts`, and `CompareVersionsDialog.tsx` / `exportMarkdown`.
CSV columns are Version, Release Date, Feature ID, Title, Category, Description, and Documentation URL.
The release source is `server/data/versions.ts`, not a live documentation feed.
Release records are held in server memory. Chat histories are React state in `ChatSidebar.tsx`.
My Stack and theme preferences use browser localStorage in `FilterPanel.tsx` and `ThemeToggle.tsx`.
Database schema and dependencies exist, but the registered release storage is `MemStorage`.
The inspected main workflow has no file-import control.

## Contents

| Content | Count and evidence |
|---|---|
| Release records | 50, counted by importing `versionsData` during this review. |
| Feature records | 822, counted by flattening that array during the same run. |
| Release endpoints | Latest 2027.2; earliest 1.5, from the same data run. These are ICM identifiers. |
| Main content route | 1 explicit route, `/`, plus a not-found fallback; `client/src/App.tsx:9-14`. |
| Main tabs | 5: Timeline, Interactive Diagrams, Learning Paths, AI Assistant, Version Compare; `home.tsx:297-316`. |
| Diagram entries | 9 entries marked available; `DiagramsPlaceholder.tsx:30-101`. |
| Learning paths | 9 path IDs; `LearningPathsDialog.tsx:45-150`. |
| Chat choices | 2 browser choices in `ChatSidebar.tsx:27`; 4 backend chat routes in `server/routes.ts`. |

## Checks

Checks below were rerun on 2026-11-15 for this refresh against the workspace, not the published deployment.

- `npm test -- --run`: could not start because `package.json` has no test script. No test pass/fail totals were produced.
- `npm run check -- --incremental false`: failed with 13 diagnostics. There were 12 drawing-context `setLineDash` type errors across the database, dependency, pump, and roughness diagrams, and 1 missing-version-ID error in `components/examples/TimelineView.tsx`.
- Data check using `node --import tsx --input-type=module`: 4 assertions passed, 0 failed. Checks covered schema validity, descending release dates, unique version IDs, and unique feature IDs in `server/data/versions.ts`.
- Browser captures loaded all 5 main tabs at 1280 by 720 pixels. All rendered. No browser error messages appeared in those captures.
- `/`, `/#tab=diagrams`, `/#tab=learning`, and `/#tab=chat`: no warnings in captured browser logs.
- `/#tab=compare`: rendered the automatically opened dialog. Its browser log warned that `DialogContent` lacked a description or explicit `aria-describedby` handling.
- Human review: none recorded in the inspected project documentation or recent git entries.

## What this does not show

1. AI responses, provider availability, answer accuracy, and citation navigation: not checked through live chat calls.
2. Export downloads, filter interactions, populated comparisons, diagram interactions, and learning-path actions: not checked end to end.
3. Mobile layouts, keyboard navigation, screen readers, and contrast compliance: not checked.
4. Production page behavior, production API responses, and equivalence between published and workspace builds: not checked. Only deployment metadata was obtained.
5. Release dates, feature wording, and documentation links against original Autodesk sources: not checked. The latest record explicitly labels its date as user-supplied.
6. Formula correctness, parameter ranges, dimensional consistency, and numerical agreement with engineering standards: not checked.
7. Rainfall labels do not establish implementation of the named official methods. The inspected generator uses generic shaped weights and an approximate depth expression.
8. Performance under load, AI costs, security vulnerabilities, and dependency advisories: not checked. Full-dataset AI prompting is visible in the source, but its runtime impact was not measured.
9. Full production build and database operations: not checked.
10. Detailed human contribution history and human technical approval: not checked. The summary has not been reviewed by Robert Dickinson.
11. A formal release date for the application package version: not checked or established. The front matter uses its earliest git occurrence.
12. Third-party content reuse rights and complete transitive-license compliance: not checked.
13. Type checking currently fails, and the comparison dialog emits the accessibility warning recorded above. No code was changed to address either.

## How to reproduce

Use the installed project dependencies:

```sh
npm run dev
# Development preview at the configured web port.
npm run check -- --incremental false
npm test -- --run
# The preceding test command currently fails: no test script.
```

Reproduce the data assertions:

```sh
node --import tsx --input-type=module <<'JS'
import { versionsData as v } from "./server/data/versions.ts";
import { versionSchema } from "./shared/schema.ts";
const f = v.flatMap(x => x.features);
const checks = {
  schema: v.every(x => versionSchema.safeParse(x).success),
  dates: v.every((x, i) => !i || v[i - 1].releaseDate > x.releaseDate),
  versionIds: new Set(v.map(x => x.id)).size === v.length,
  featureIds: new Set(f.map(x => x.id)).size === f.length
};
console.log({ versions: v.length, features: f.length, checks });
if (Object.values(checks).some(x => !x)) process.exitCode = 1;
JS
```

Load the root page and each tab hash listed under Checks.
Production commands declared in `package.json:8-9` are `npm run build` followed by `npm start`; these were not run for this summary.

## Credits and licenses

- Summary author: Robert Dickinson, as specified in the supplied instructions.
- Project license: MIT, declared in `package.json:5`.
- Autodesk InfoWorks ICM documentation supplies the subject matter and linked feature references in `server/data/versions.ts`. Content reuse rights were not verified.
- React, Express, Vite, Tailwind CSS, Recharts, and the Anthropic SDK: MIT.
- TypeScript, Google GenAI SDK, and OpenAI SDK: Apache-2.0.
- p5.js: LGPL-2.1.
- Library license declarations above were read from the installed packages' `package.json` files during this review. This is not a complete dependency license inventory.

## AI use

Recent git commits identify Replit Agent as author of release-note, chat-sidebar, and learning-path changes.
The inspected history does not establish Robert Dickinson's detailed implementation or review contributions.
At runtime, `server/routes.ts` configures Claude, Gemini, OpenAI, and DeepSeek through OpenRouter.
`ChatSidebar.tsx` exposes Claude and Gemini. Other providers have routes but no selector in that component.
The system prompt supplies the entire local release history and asks for feature citations.
This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: `git log -8 --format='%as %s'`, newest first. Dates are commit dates, not verified product release dates.

- 2026-11-15: Add agent asset metadata and new view documentation.
- 2026-09-15: Published your App.
- 2026-09-15: Update chat sidebar, learning paths dialog, and version data.
- 2026-09-15: Add release notes for current version.
- 2026-07-20: Published your App.
- 2026-07-20: Published your App.
- 2026-07-10: Published your App.
- 2026-07-10: Add new features and updates for the latest software release.
