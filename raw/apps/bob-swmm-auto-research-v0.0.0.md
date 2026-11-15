---
name: bobSWMM Auto Research
file: bob-swmm-auto-research
version: 0.0.0
date: 2026-03-12
author: Robert Dickinson
links: {replit: "https://bob-swmm-auto-research.replit.app", repo: "https://github.com/SWMMBobSWMM6/BobSWMM-Auto-Research"}
engines: none
stack: TypeScript, React, Vite, Tailwind CSS, Recharts, Node.js, Express, PostgreSQL, Drizzle ORM, Zod, Orval, OpenAI, Replit AI Integrations
units: both
ai_use: OpenAI generates streamed research reports and chat replies using curated reference text.
---

# bobSWMM Auto Research: Research and file inspection for stormwater modeling

## What it does
The app answers SWMM modeling questions for stormwater engineers and modelers.
It produces AI-generated reports, chat replies, calculator plots, and file diagnostics.
Users can inspect input files, compare model sections, and read report summaries.
The inspected implementation computes educational examples in the browser; it does not invoke a SWMM simulation engine.
Sources: `README.md:1-35`, `artifacts/bob-swmm/src/App.tsx:40-66`, and the calculation and API files cited below.

## How it computes
Paths below starting with `pages/` are relative to `artifacts/bob-swmm/src/`.

- Research: `artifacts/api-server/src/lib/rag-knowledge.ts`, `matchesKeyword` and `buildRAGContext`, match whole words or phrases against curated topics and append reference text. This is keyword retrieval, not a demonstrated live literature search (`:191-227`).
- Generation: `artifacts/api-server/src/routes/research.ts`, the `/research/start` handler, stores a session, constructs the prompt, calls OpenAI model `gpt-5.2`, streams text, extracts a Sources list, and stores the result (`:95-177`). The model identifier is from `:138`.
- Green-Ampt: `pages/calculators.tsx`, `GreenAmptCalculator`, uses `fp = Ks*(1 + psi*dTheta/F)`, limits infiltration to rainfall, and accumulates `F += infiltration*dt/60`. It initializes capacity with twice rainfall when cumulative infiltration is zero. Inputs use inches and inches/hour. This is an explicit browser approximation, not the engine's iterative solver (`:42-60`, `:72-75`).
- Horton: the same file, `HortonCalculator`, uses `fp = fc + (f0-fc)*exp(-k*tHours)` and `runoff = max(0, rainfall-infiltration)` (`:105-120`).
- Curve Number: the same file, `CurveNumberCalculator`, computes `S = 1000/CN - 10` inches, `Ia = lambda*S`, and `Q = (P-Ia)^2/(P-Ia+S)` when `P > Ia`; otherwise runoff is zero (`:434-450`).
- RTK/RDII: the same file, `RTKCalculator` and its `triangle` helper, sum finite triangular responses. `Tb = Tp*(1+K)` and `qp = 2*R/Tb`. Numerical area uses samples spaced by `0.1` hour. Plotting is capped at `72` hours. The area check compares integrated response against the sum of R, not a simulated sewer-network discharge (`:170-216`).
- Manning: the same file, `ManningCalculator` and `PipeSizingTable`, calculate circular area, wetted perimeter, hydraulic radius, `Q = (k/n)*A*R^(2/3)*sqrt(slope)`, and `V = Q/A`. US customary uses feet, cubic feet/second, and `k=1.49`; SI uses meters, cubic meters/second, and `k=1.0` (`:285-295`, `:327-365`).
- Surcharge: the same file, `SurchargeCalculator`, applies a synthetic Gaussian inflow to a fixed capacity of `10` cubic feet/second. `pondedVolume = max(0, pondedVolume + excess*dtSeconds)`; positive ponded area converts volume to depth. This is illustrative lumped storage, not dynamic-wave routing (`:505-535`).
- Storms: `pages/design-storms.tsx`, `DesignStormsPage`, scales stored cumulative rainfall fractions by total depth in inches. `intensity = changeInFraction*totalDepth/dtHours`; peak time comes from the interval with greatest intensity (`:51-114`).
- Parameters and units: `pages/parameter-wizard.tsx`, `ParameterWizardPage`, selects tabulated soil, land-use, and slope values (`:38-62`). `pages/unit-converter.tsx`, `UnitConverterPage`, applies the factors in `CONVERSION_GROUPS` for US customary and SI conversions.
- File analysis: `lib/inp-parser.ts`, `parseInpFile`, parses model sections. `pages/inp-diff.tsx`, `parseInpSections` and `diffSections`, compare sections and records. `pages/model-review.tsx`, `parseAndReview`, applies structural checks. These operations inspect text rather than run hydraulics.
- Reports: `pages/rpt-dashboard.tsx`, `parseRpt`, `numericCols`, and `splitSummaryRow`, parse summary tables and produce numerical-quality, hydraulic-performance, and completeness assessments (`:65-338`).

## Inputs and outputs
- Browser inputs include text questions, numeric controls, `.inp`/`.txt` model files, and `.rpt`/`.txt` reports. File readers populate component state.
- Report export creates a Markdown Blob and `.md` download; printing uses the browser print dialog (`pages/research-session.tsx:129-139`). Design storms generate downloadable plain-text time series (`pages/design-storms.tsx:94-129`).
- API prefix: `/api` (`artifacts/api-server/src/app.ts:11`).
- Research endpoints: GET `/research/presets`, GET `/research/sessions`, GET and DELETE `/research/sessions/:id`, POST `/research/start` (`artifacts/api-server/src/routes/research.ts`).
- Chat endpoints: GET and POST `/openai/conversations`, GET and DELETE `/openai/conversations/:id`, GET and POST `/openai/conversations/:id/messages` (`artifacts/api-server/src/routes/openai.ts`).
- Health endpoint: GET `/healthz` (`artifacts/api-server/src/routes/health.ts`).
- PostgreSQL stores research queries, depth, status, report text, sources, matched topics, conversations, and messages. Sources: `lib/db/src/schema/research-sessions.ts`, `conversations.ts`, and `messages.ts`.
- The inspected file-analysis handlers use browser memory, not a server-side model-file archive.

## Contents
Counts were computed from current source during this summary run, not copied from documentation.

| Content | Count | Source and counting method |
|---|---:|---|
| Explicit application routes | 23 | Count of `<Route path=` in `artifacts/bob-swmm/src/App.tsx:43-65`; excludes fallback |
| Static routes | 22 | Same route list, excluding `/research/:id` |
| Calculator tabs | 6 | Entries in `CALC_TABS`, `pages/calculators.tsx:10-17` |
| Research presets | 60 | Preset `id` entries in `artifacts/api-server/src/lib/swmm5-presets.ts` |
| Curated retrieval topics | 8 | Object entries in `RAG_KNOWLEDGE`, `artifacts/api-server/src/lib/rag-knowledge.ts:27-189` |
| Application database tables | 3 | Table declarations in the schema files listed above |

## Checks
All runs in this section were made on 2026-11-15, as reported by the environment date command.

- Test discovery found no `.test.*` or `.spec.*` files under application, library, or script directories outside dependencies and build outputs. Root, web, and API package scripts do not declare a test command.
- Attempted `pnpm --filter @workspace/bob-swmm run test` and `pnpm --filter @workspace/api-server run test`. Neither produced a test report. Executed unit-test cases: 0 passed, 0 failed. This is absence of an executable suite, not a passing suite.
- `pnpm --filter @workspace/bob-swmm exec tsc --noEmit --incremental false` failed. The run reported 7 TypeScript diagnostics: 5 missing `ragTopics` properties, 1 implicit-any parameter, and 1 required `queryKey` option. Locations: `learning-log.tsx:23,26,27,132,178` and `research-session.tsx:65`. Wrapper exit status was 1.
- Read-only browser run: 22/22 static pages and 1/1 existing research-detail page loaded with HTTP 200 and nonempty content. No uncaught page errors, failed requests, or captured HTTP error responses occurred.
- Audited paths: `/`, `/history`, `/chat`, `/presets`, `/calculators`, `/compare`, `/inp-analyzer`, `/source-code`, `/community`, `/knowledge-base`, `/learning-log`, `/error-codes`, `/parameter-wizard`, `/unit-converter`, `/design-storms`, `/inp-diff`, `/model-review`, `/rpt-dashboard`, `/icm-translator`, `/pyswmm-code`, `/timeline`, `/section-explainer`, and `/research/1`.
- The first home-page load logged 1 unattributed console resource error reporting HTTP 404. A home reload had 0 console errors. A separate favicon request returned HTTP 404, but its connection to the console error was not established.
- Human review: none recorded. Knowledge entries contain `reviewed: true` metadata, but the inspected records do not identify a human reviewer or provide a signed engineering review.

## What this does not show
1. Numerical agreement with EPA SWMM, benchmark models, conservation across all parameter ranges, and real-file parser coverage: not checked.
2. New AI report generation, chat generation, citation accuracy, and outside-service availability during generation: not checked.
3. Uploads, downloads, printing, deletion, and other interactive workflows: not checked. The browser run checked page loading only.
4. Detailed visual review of every page, mobile layout, accessibility, security, and performance: not checked.
5. A new production build and production browser behavior: not checked. Deployment metadata supplied the published URL; page checks used the development app.
6. Production database contents, backup restoration, and complete record counts: not checked.
7. Transitive dependency licenses and external manual/source licensing: not checked. Credits below cover inspected direct-package metadata only.
8. Public repository reachability and a release tag matching the package version: not checked. The repository URL comes from `README.md:174`.
9. The source still has the TypeScript defects reported above. No code corrections were made for this summary.
10. The source calculations do not establish that a calibrated or validated simulation engine runs here. The RTK horizon can truncate long responses, and surcharge uses a synthetic inflow and fixed capacity.
11. No person is recorded as having reviewed this summary or validated the calculations described here. Boolean review flags alone do not establish that review.

## How to reproduce
Use the existing managed web and API workflows with their configured environment. Do not copy credential values into commands or documents.

```sh
pnpm install
pnpm --filter @workspace/api-server run dev
pnpm --filter @workspace/bob-swmm run dev
pnpm --filter @workspace/bob-swmm run test
pnpm --filter @workspace/api-server run test
pnpm --filter @workspace/bob-swmm exec tsc --noEmit --incremental false
```

The dev commands come from the corresponding package scripts. The test commands currently have no declared suite. Installation and development startup are reproduction instructions, not fresh checks performed for this document.
Repeat the browser audit by loading the paths listed under Checks without generating reports or changing stored data.

## Credits and licenses
- Robert Dickinson is credited by the project `LICENSE`. The project license is MIT.
- EPA SWMM manuals and source are referenced by the curated knowledge file. They are reference material here, not evidence of an embedded engine.
- React, Vite, Recharts, Express, Tailwind CSS, and node-postgres declare MIT in their installed package metadata.
- Drizzle ORM and the OpenAI JavaScript library declare Apache-2.0 in their installed package metadata.
- License evidence was read from each named package's `node_modules/<package>/package.json`, under its consuming web, API, database, or AI-integration package.

## AI use
The application uses OpenAI through Replit AI Integrations to generate research reports and chat replies. Retrieved context is assembled locally from curated text.
The inspected project documents and git subjects do not establish which historical edits were made by Replit Agent or another AI builder. No other builder attribution is asserted.
Robert Dickinson is the copyright holder named in `LICENSE`. The inspected records do not establish his specific implementation or validation actions.
This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes
Version `0.0.0` comes from `artifacts/bob-swmm/package.json:3`. The front-matter date is the earliest package-history date observed, not a verified release date. Summary inspection date is 2026-11-15.
The entries below are git subjects, not independent confirmation of each claimed outcome.

- 2026-10-29: Initialize bobswmm-deck artifact and update project dependencies.
- 2026-10-29: Published your App.
- 2026-10-29: Update RAG knowledge handling and refine chat and research stream hooks.
- 2026-07-23: Add MIT License to the project.
- 2026-06-13: Create README.md.
- 2026-03-16: Improve application navigation and fix code review issues.
- 2026-03-16: Create detailed handover document for the AI-powered SWMM5 research tool.
- 2026-03-14: Published your App.
