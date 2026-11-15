---
name: ICM Ruby to Nano Banana Prompt
file: icm-flow-visualizer-robertdickinson
version: 1.0.0
date: 2025-11-19
author: Robert Dickinson
links: {replit: https://swmm5toicmswmmworkflow.com, repo: none}
engines: none
stack: TypeScript, JavaScript, React, Vite, Express, in-memory storage, Google GenAI SDK and Gemini API, Google Fonts CDN; Drizzle ORM and Neon PostgreSQL packages are present but not used for app storage
units: not applicable
ai_use: Gemini generates code explanations at runtime; project records do not name an AI app builder
---

# ICM Ruby to Nano Banana Prompt: Analyze Ruby and SWMM5 files

## What it does

The app helps engineers inspect Ruby scripts used with ICM InfoWorks and SWMM5 input files. It answers questions about code structure, file sections, and workflow steps. Users can upload one Ruby file, a folder of Ruby files, or one `.inp` file. It displays a workflow view, code statistics, diagrams, and AI-generated explanations.

## How it computes

- `parseRubyFile` in `server/ruby-parser.ts:4-117` scans Ruby text for method definitions, skips selected helper names, creates one workflow node per matching method, and connects nodes in order. It creates a default node when it finds no methods. This is a text-pattern parser, not a Ruby interpreter.
- `analyzeRubyCode` in `client/src/components/MetadataPanel.tsx:31-64` finds class and method declarations with regular expressions and builds a short summary.
- `parseSWMM5File` in `client/src/components/MetadataPanel.tsx:66-85` reads section headers and counts nonblank, non-comment lines under each section.
- The `/api/mermaid-diagram` handler in `server/routes.ts:248-381` uses regular expressions to count code patterns and returns a text diagram. It does not execute Ruby.
- The `/api/ai-analyze`, `/api/nano-explain`, and `/api/ai/explain` handlers send prompts to Gemini using `gemini-2.5-flash` (`server/routes.ts:79-115,117-162,164-246`).
- `workflowToMarkdown` in `server/ruby-parser.ts:119-147` formats workflow nodes as Markdown.
- The app does not call an ICM or SWMM simulation engine. The default workflow is example data in `server/storage.ts:41-138`.

## Inputs and outputs

- Inputs: Ruby text from `.rb` uploads or folder uploads, and SWMM5 text from `.inp` uploads (`client/src/pages/WorkflowVisualization.tsx:169-191,87-123`).
- Browser routes: `/` displays the analyzer; other paths use the not-found route (`client/src/App.tsx:9-14`).
- API routes: `GET /api/workflow`, `GET /api/logs`, `POST /api/parse-ruby`, `POST /api/markdown/generate`, `POST /api/markdown/save`, `GET /api/markdown`, `POST /api/ai/explain`, `POST /api/ai-analyze`, `POST /api/nano-explain`, and `POST /api/mermaid-diagram` (`server/routes.ts:8-410`).
- Outputs include workflow JSON, code analysis, a text diagram, AI explanations, and generated or saved Markdown (`server/routes.ts:28-77,79-115,117-162,164-246,248-410`).
- Workflow data, logs, and Markdown are held in server memory by `MemStorage` (`server/storage.ts:11-39,161`). They are not stored in a database or server files by this implementation. The onboarding-seen flag is stored in browser `localStorage` (`client/src/components/OnboardingDialog.tsx:17-26`).

## Contents

- The app has one main routed page at `/` and a fallback page (`client/src/App.tsx:9-14`).
- The live `GET /api/workflow` response contained 23 nodes and 24 edges. Node types were 1 start, 15 process, 5 decision, 1 data, and 1 end. These counts came from a request to `/api/workflow`; the seed definition is in `server/storage.ts:41-115`.
- The same response contained 7 file configuration records (`GET /api/workflow`; seed records in `server/storage.ts:129-137`).
- The live `GET /api/logs` response contained 14 sample log records (`GET /api/logs`; seed records in `server/storage.ts:141-157`).
- The source names one Gemini model, `gemini-2.5-flash` (`server/routes.ts:103-105,150-152,234-236`).
- The version is `1.0.0` in `package.json:3`. Git history first records that package version on 2025-11-19 (`git log -S'"version"' -- package.json`), which is the date used above.

## Checks

- The `/` page loaded in the browser preview. No browser console errors appeared in the captured load.
- `GET /api/workflow`, `GET /api/logs`, and `GET /api/markdown` returned responses during a live development-server check (`server/routes.ts:8-26,69-77`).
- `npm run check` failed with 34 TypeScript diagnostics. The command is defined by `package.json:6-12`; the count is from the run made for this summary.
- Tests: 0 run, 0 passed, 0 failed. No test script is declared in `package.json:6-12`, and no project test files were found under `client`, `server`, or `shared`.
- Human review: none recorded.

## What this does not show

1. The POST APIs, file-upload flows, and Gemini responses were not exercised with uploaded user files.
2. The runtime workflow, log, and file configuration data are seeded examples. They do not verify an actual ICM import (`server/storage.ts:41-157`).
3. The app's production behavior was not tested. The browser check used the development app.
4. The TypeScript check currently fails with 34 diagnostics; the full check output was not copied into this summary.
5. The HTML page title and description still use SWMM5 workflow wording (`client/index.html:7-8`), unlike the app's displayed name (`client/src/pages/WorkflowVisualization.tsx:165-167`).
6. The reference dialog names Markdown files under `/reference/` (`client/src/components/ReferenceModal.tsx:24-30`). Those files were not present in the current `client/public` listing; loading each reference was not checked.
7. Individual licenses for third-party dependencies were not checked. The project has no tracked standalone license file; the package declares MIT (`package.json:5`).
8. No independent person reviewed this summary or recorded a review of the app.

## How to reproduce

- Start the development app with `npm run dev` (`package.json:6-7`).
- Run the available TypeScript check with `npm run check` (`package.json:10`). It currently reports 34 diagnostics.
- No test command is configured (`package.json:6-12`).

## Credits and licenses

- Robert Dickinson is the listed author. Git history attributes the recorded changes to `robertdickinson`.
- Project license: MIT (`package.json:5`). No standalone license file is tracked.
- Runtime libraries named in `package.json` include React, Express, Vite, `@google/genai`, Mermaid, Drizzle ORM, and the Neon PostgreSQL driver (`package.json:13-80`). Their individual licenses were not checked.
- Google Gemini is used for generated explanations (`server/routes.ts:79-115,117-162,164-246`). Google Fonts is loaded from Google Fonts (`client/index.html:9-11`).

## AI use

The project source records Gemini as a runtime tool for code explanations. It does not record which AI tools, if any, built the app. The Git log records Robert Dickinson's changes, including publication and interface updates, but does not describe his full role.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Source: `git log -10 --date=short --pretty=format:'%ad %s'`.

- 2026-02-07: Published your App
- 2025-12-06: Published your App
- 2025-12-06: Add a light blue background to the application interface
- 2025-12-06: Adopt a playful Nano Banana color theme for the application
- 2025-12-06: Update application colors to a vibrant blue theme
- 2025-11-22: Update application title to include "Prompt" for clarity
- 2025-11-22: Ensure Nano Banana tab shows for multiple files
- 2025-11-22: Update application title to ICM Ruby to Nano Banana
- 2025-11-22: Fix folder upload to correctly allow users to select directories
- 2025-11-22: Add ability to upload and analyze multiple Ruby files from a folder
