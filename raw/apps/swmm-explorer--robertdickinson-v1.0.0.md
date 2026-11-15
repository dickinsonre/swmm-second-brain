---
name: SWMM5 Explorer
file: swmm-explorer--robertdickinson
version: 1.0.0
date: 2026-01-29
author: Robert Dickinson
links: {replit: "https://swmm-explorer--robertdickinson.replit.app", repo: none}
engines:
  - {name: "EPA SWMM source archive, not an executable browser solver", version: "5.2.4", source: "https://github.com/USEPA/Stormwater-Management-Model", commit: "not recorded", license: "Public Domain"}
stack: "TypeScript, JavaScript, C source content, React, Vite, Express, Tailwind CSS, Radix UI, Zustand, Wouter, D3, d3-sankey, Fuse.js, PostgreSQL and Drizzle scaffolding, OpenRouter through Replit AI Integrations"
units: both
ai_use: "Optional external code analysis and diagram-prompt generation; development attribution is limited by the repository record."
---

# SWMM5 Explorer: Browse SWMM source, inspect architecture diagrams, and prepare input text

## What it does

This app helps people studying stormwater-model source code find files, locate function-like symbols, and follow illustrated module relationships.
It presents source text, preset Sankey diagrams, an input-file form, and an engine interface (`client/src/App.tsx:21-27`).
Users can request external AI explanations of selected source text (`client/src/pages/AITools.tsx:110-140`).
The supplied browser engine asset is a no-op stub, so the interface does not establish that hydraulic simulation has occurred (`client/public/wasm/swmm5.js:1`).

Metadata evidence:
- The display name appears in `replit.md:1` and `client/index.html:7`.
- The summary uses package version `1.0.0` from `package.json:3`, rather than the inconsistent engine labels in the interface.
- The version date is the most recent package-file change date returned by `git log -1 --format='%ad %s' --date=short -- package.json`: `2026-01-29`. It is not a verified release date.
- The published URL and site name were returned by the deployment metadata lookup during this review. The lookup reported an active deployment with a successful build.
- `git remote -v` showed an internal repository mirror, not a verified public GitHub URL. Therefore `repo` is `none`.
- The archived solver version and date come from `swmm5_src/Stormwater-Management-Model-master/src/solver/consts.h:5-19`. Its upstream project URL and public-domain statement appear in the archive's `README.md:8-17`.

## How it computes

- **Source search:** `CodeBrowser` in `client/src/pages/CodeBrowser.tsx` builds Fuse.js indexes and filters by file category. `buildIndex` in `client/src/lib/store.ts:78-103` uses a regular expression to find function-like declarations. It computes the displayed line as the number of newline-separated segments before the match. This is not a C parser.
- **Diagram layout:** The effect in `SankeyDiagram`, `client/src/pages/SankeyDiagram.tsx:182-211`, copies a selected `FLOW_PRESETS` graph and passes its nodes and links to `sankeyGenerator`. Link values are preset data, not measured flows or simulation results. D3 computes the positions and widths.
- **Input generation:** `generateInp` in `client/src/pages/InpGenerator.tsx:36-66` interpolates form strings into an INP template. It performs no hydrologic or hydraulic calculation. The template includes a fixed subcatchment row.
- **Engine loading:** `SWMMEngine.loadScript` and `loadModule`, `client/src/lib/swmm-engine.ts:68-103`, load `/wasm/swmm5.js` and call `window.createSWMMModule`.
- **Intended solver call:** `SWMMEngine.run`, `client/src/lib/swmm-engine.ts:116-201`, writes input to a virtual filesystem, allocates filename strings, calls `ccall('swmm_run', ...)`, then reads report and output files.
- **Actual supplied engine:** `client/public/wasm/swmm5.js:1` makes the solver call return success and file reads return empty strings without computation. The direct engine probe below confirmed that behavior.
- **Missing-module fallback:** `simulateRun`, `client/src/lib/swmm-engine.ts:204-269`, waits through scripted phases. Progress = elapsed scripted duration / total scripted duration. `generateMockReport`, lines 272-316, returns fixed report quantities. These are not calculated from rainfall or drainage geometry.
- **Version formatting:** `getVersion`, `client/src/lib/swmm-engine.ts:323-333`, splits the integer returned by `swmm_getVersion` into major, minor, and patch components. The supplied stub returns zero, producing `0.0.0`, as observed in the direct probe and browser.
- **AI processing:** `registerRoutes`, `server/routes.ts:17-143`, sends prompts and optional code to OpenRouter. Code analysis streams text events; diagram-prompt generation returns JSON text. The latter does not create an image.
- **Units:** The generator offers CFS before SI choices (`client/src/pages/InpGenerator.tsx:130-135`). No unit-conversion calculation occurs in its template builder. The fallback report labels depths in inches and volumes in gallons (`client/src/lib/swmm-engine.ts:289-310`).

## Inputs and outputs

| Surface | Input | Output or storage |
|---|---|---|
| `/` and `/about` | Navigation | Introductory and attribution content |
| `/code` | File name, category, search text; optional `file` and `line` query parameters | Source display and symbol matches |
| `/sankey` | Diagram preset and node selection | SVG diagram; navigation to source |
| `/inp` | Project settings and rainfall-gage fields | INP preview; `project.inp` download; shared browser state |
| `/wasm` | Pasted INP text, embedded example, or generator state | Logs, progress, result state; report download as `swmm_report.rpt` when report text exists |
| `/ai` | Prompt, selected source text, analysis task, or diagram description | AI text displayed in browser memory |
| `POST /api/ai/deepseek` | JSON prompt, code, task | Streamed analysis through OpenRouter |
| `POST /api/ai/claude` | JSON prompt, code, task | Streamed analysis through OpenRouter |
| `POST /api/ai/diagram-prompt` | JSON description and diagram type | JSON prompt text generated through OpenRouter |

Route sources: `client/src/App.tsx:21-28`, `client/src/pages/CodeBrowser.tsx:32-57`, and `server/routes.ts:17-143`.
Download sources: `client/src/pages/InpGenerator.tsx:250-259` and `client/src/pages/WasmEngine.tsx:409-415`.

Model text, selected source, symbol indexes, and results live in Zustand memory, without persistence middleware (`client/src/lib/store.ts:30-59,80-115`).
Onboarding stores its seen flag in browser local storage (`client/src/components/Onboarding.tsx:63-70`).
The active AI endpoints do not write conversations or uploaded models to a database (`server/routes.ts`).
PostgreSQL schemas and chat storage exist, but `server/index.ts:62-81` does not register the separate `registerChatRoutes` function.
The schema and persistence scaffolding are in `shared/schema.ts`, `server/db.ts`, and `server/replit_integrations/chat/storage.ts`.
Source content is bundled from `client/src/lib/swmm-data.ts`; archived C sources also remain in server-side project files.

## Contents

Counts below were read or computed during this review, not copied from promotional labels.

| Content | Count | Source and counting method |
|---|---:|---|
| Named application routes | 7 | Count of explicit path routes in `client/src/App.tsx:21-27` |
| Fallback page | 1 | Unmatched route in `client/src/App.tsx:28` |
| Bundled source records | 75 | Imported `SWMM_FILES` and evaluated `.length` using Node with `--import tsx` |
| C implementation records | 54 | Filtered `SWMM_FILES` names ending in `.c` |
| C header records | 21 | Filtered `SWMM_FILES` names ending in `.h` |
| Source categories | 5 | Distinct `SWMM_FILES.category` values: Core, Hydrology, Hydraulics, Quality, Headers |
| Diagram presets | 4 | `client/src/pages/SankeyDiagram.tsx:297-302` |
| Embedded model menu entries | 4 | `EXAMPLE_MODELS` entries in `client/src/pages/WasmEngine.tsx:70-290` |
| AI tool tabs | 3 | `client/src/pages/AITools.tsx:28-95` |
| Registered AI endpoints | 3 | `server/routes.ts:17,65,111` |

The C and header counts come from the same direct import run. The interface's description of every source record as a C file is imprecise.

## Checks

Mechanical checks were run on 2026-11-15 against the workspace source, not the published build.
Commands and observations in this section are the sources for all run-result numbers.

| Check | Command or action | Result |
|---|---|---|
| Type checking | `npm run check` | Passed; command exited successfully with no TypeScript diagnostics |
| Production build | `npm run build` | Passed; client and server bundles were generated; Vite warned about large chunks |
| Project test runner | `npm test` | Failed to start: missing `test` script; 0 test cases passed, 0 test cases failed, 1 command failure |
| Direct engine probe | Node with `--import tsx`; supplied a minimal document shim, loaded the actual stub, then called `swmmEngine.init()` and `swmmEngine.run()` | Reported version `0.0.0`, success `true`, error code `0`, empty report text, and a string rather than a `Uint8Array` for output |
| Browser route loading | Screenshot/browser loads of every explicit path route | 6 routes rendered behind onboarding; `/code` failed with a Tooltip context error |

Per-route browser observations:

| Route | Observed result |
|---|---|
| `/` | Home content and welcome dialog rendered |
| `/code` | Blank application after a Tooltip exception; workflow log recorded "`Tooltip` must be used within `TooltipProvider`" |
| `/sankey` | Diagram and welcome dialog rendered after workflow restart |
| `/inp` | Input form, preview, and welcome dialog rendered after restart |
| `/wasm` | Engine page and welcome dialog rendered after restart; engine label showed `0.0.0` |
| `/ai` | AI tools and welcome dialog rendered after restart |
| `/about` | About content and welcome dialog rendered after restart |

The first page-load pass lost the development-server connection after the Code Browser exception.
The existing workflow was restarted without code edits; the remaining routes then loaded.
Every rendered welcome dialog logged a missing `DialogTitle` error and a missing description warning.
The welcome overlay remained open, so these loads do not verify underlying interactions.

Human review: none recorded in the source, project notes, or git history inspected for this summary.

## What this does not show

1. Real hydraulic or hydrologic accuracy: not checked. The browser asset is a stub, not the archived solver compiled to WebAssembly.
2. AI endpoint responses, streaming failures, model availability, provider retention, and response correctness: not checked. No paid AI calls were made.
3. Uploaded-file handling, model-menu interactions, generated-file downloads, cancellation, cross-page state transfer, and onboarding dismissal: not checked end to end.
4. Mobile layouts, keyboard navigation, and screen-reader behavior: not checked. The observed dialog accessibility errors remain.
5. Native solver compilation and the archived upstream C/C++ tests: not checked. The app has no npm test script (`package.json:6-13`).
6. Database connectivity, schema deployment, stored rows, and database-backed chat: not checked. The active route registration does not enable the chat scaffolding.
7. Published-site rendering, production performance, load capacity, authorization, and a security audit: not checked. Deployment metadata is not a production functional test.
8. Upstream source commit, a public project repository URL, exact release date, and the provenance of each embedded example: not checked or not recorded in the inspected materials.
9. Input-file validity against EPA SWMM: not checked by a real solver. `generateInp` emits standalone date sections and references rainfall and outlet objects without providing complete definitions (`client/src/pages/InpGenerator.tsx:36-66`).
10. Engine version labels conflict: the sidebar and About page show `5.1.015`, the fallback string shows `5.2.1`, the archived header identifies `5.2.4`, and the supplied stub reports `0.0.0` (`Layout.tsx:77`, `About.tsx:75`, `swmm-engine.ts:324`, archive `consts.h:6`, direct probe).
11. No person has reviewed this summary or validated its engineering conclusions in a record available to this review. Git author metadata does not prove manual code authorship or approval.

## How to reproduce

Use the existing Node.js project environment and configured Replit AI integration. Do not place credentials in source files.
The runtime selection and port mapping are in `.replit:1-14`; commands are defined in `package.json:6-13`.

```sh
npm ci
npm run dev
# In another terminal:
npm run check
npm run build
npm test
# npm test currently fails because no test script is defined.
# To run the generated production build instead of the dev server:
npm start
```

Visit the paths listed under Inputs and outputs. Expect onboarding in a fresh browser.
The production build writes generated bundles under `dist` (`script/build.ts:35-60`).
The direct engine probe used the actual `client/public/wasm/swmm5.js` asset with a minimal document-loading shim, then imported `client/src/lib/swmm-engine.ts`.
It called `init()`, `getVersion()`, and `run()` with a minimal title-only INP string.

## Credits and licenses

- Robert Dickinson is identified as creator in `client/src/pages/About.tsx:35-50`.
- EPA maintains the archived Stormwater Management Model source. Its README states Public Domain and includes a disclaimer (`swmm5_src/Stormwater-Management-Model-master/README.md:10-17`).
- L. Rossman is named in the archived solver header (`src/solver/consts.h:7` within that archive).
- The project's package declares MIT (`package.json:5`). No standalone project license file was found in the inspected root.
- Installed package metadata identifies React, Vite, Express, Tailwind CSS, Zustand, Radix UI, PostgreSQL's `pg` client, and react-syntax-highlighter as MIT.
- Installed package metadata identifies TypeScript, Fuse.js, the OpenAI SDK, and Drizzle ORM as Apache-2.0; D3 and Lucide React as ISC; d3-sankey as BSD-3-Clause; and Wouter as Unlicense.
- Those library licenses were read from each corresponding `node_modules/<package>/package.json` during this review. This is not a complete transitive-dependency license audit.

## AI use

The repository configuration records agent-authored workflows (`.replit:25-40`), and git history includes automated progress and publishing entries.
Those records do not establish which assistant wrote each feature. No additional named development assistant or complete development transcript was found in the inspected code and notes.
Robert Dickinson is credited as creator; recent git entries use his account name. His exact manual coding and review contributions are not established by those records.

At runtime, the code selects DeepSeek V3.2 and Claude Sonnet 4.5 through OpenRouter (`server/routes.ts:34-41,80-87`).
The Nano Banana prompt feature also calls DeepSeek; it writes text intended for image generation elsewhere (`server/routes.ts:110-138`).
The supplied active endpoints do not call an image-generation service or use AI to calculate hydraulic results.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: `git log -10 --date=short --pretty=format:'%ad %s'`, read during this review. Repeated publishing entries are retained as recorded.

- 2026-01-31: Published your App.
- 2026-01-31: Published your App.
- 2026-01-31: Saved progress at the end of the loop.
- 2026-01-31: Added interactive links and testing attributes to application pages.
- 2026-01-31: Added an About page and enhanced homepage module descriptions.
- 2026-01-31: Published your App.
- 2026-01-31: Published your App.
- 2026-01-29: Published your App.
- 2026-01-29: Added detailed explanations for Sankey visualizations.
- 2026-01-29: Added tooltips to interactive elements.
