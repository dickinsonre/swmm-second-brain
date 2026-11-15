---
name: MapSWMMSewer - Code Repository
file: sewer-code-search
version: 1.0.0
date: 2026-03-09
author: Robert Dickinson
links: {replit: https://sewer-code-search.replit.app, repo: none}
engines: none
stack: TypeScript, JavaScript, React, Vite, Node.js, Express, PostgreSQL, Drizzle ORM, Tailwind CSS, TanStack Query, Google Fonts
units: not applicable
ai_use: Build-time AI use is not documented; Replit Agent wrote this summary.
---

# MapSWMMSewer: Search and manage stored engineering code files

## What it does

The app answers which saved code files match a text search or category. It is a private repository for code associated with SWMM, sewer analysis, and h2oCalc. Users can search and filter records, view code, and add, edit, or delete records. The app returns matching records and simple repository counts. It does not run the stored engineering code.

## How it computes

The app runs no SWMM, sewer, or h2oCalc simulation engine. It stores code as text in PostgreSQL. The `Home` component calculates record totals by category, distinct language count, and a line count using `code.split("\n").length` (`client/src/pages/home.tsx:82-94`). Search and category filtering are applied to loaded records in `Home` (`client/src/pages/home.tsx:58-80`). The server also implements search and category queries in `DatabaseStorage.searchCodeFiles` and `DatabaseStorage.getCodeFilesByCategory` (`server/storage.ts:27-43`). No simulation engine is called.

## Inputs and outputs

- Users enter a title, filename, description, source text, language, category, subcategory, tags, and source in the add/edit form (`client/src/components/add-snippet-dialog.tsx:32-45`).
- The app accepts code as text in a form. It has no source-file upload or download route.
- `GET /api/code` returns records and accepts `category` or `search` query parameters. `GET /api/code/:id` returns one record. `POST /api/code` creates a record. `PATCH /api/code/:id` updates a record. `DELETE /api/code/:id` deletes a record. `GET /api/categories` and `GET /api/tags` return category and tag lists (`server/routes.ts:10-100`).
- Records are stored in the PostgreSQL `code_snippets` table. The schema includes title, filename, description, code, language, category, subcategory, tags, source, and creation time (`shared/schema.ts:6-18`).
- The browser displays code cards, repository counts, and a code viewer. API responses are JSON.

## Contents

- The router defines one main page at `/` and a not-found fallback (`client/src/App.tsx:13-18`).
- The development database contained 16 records: 6 SWMM, 3 Sewer, and 7 h2oCalc. It contained 3 categories, 4 distinct language values, and 2,759 code lines. These counts came from a read-only query of `code_snippets` on 2026-11-15. The line count uses the same newline split as `Home` (`client/src/pages/home.tsx:85`).
- The development API returned 84 distinct tags and 16 records on 2026-11-15 (`GET /api/tags` and `GET /api/code`).
- The app display name is from `client/index.html:6`. Version `1.0.0` is from `package.json:3`. Git records the package version in a commit dated 2026-03-09 (`git log -- package.json`).

## Checks

- `npm run check`: passed. TypeScript reported no errors.
- `npm test`: could not run because `package.json` defines no `test` script. Zero tests executed, zero passed, and zero test cases failed.
- The main development page at `/` loaded. The browser console showed no errors; it logged Vite connection messages and a React DevTools informational message.
- Development API checks returned HTTP 200 for `GET /api/code`, `GET /api/categories`, and `GET /api/tags`.
- Human review: none recorded.

## What this does not show

1. The record and tag counts are from the development database. The production database was not queried.
2. Deployment metadata reports a private deployment, but does not report a successful current build. The production page was not loaded or checked.
3. No automated test suite is configured, so create, update, delete, search, and category-filter behavior were not covered by automated tests in this run.
4. The project files name EPA SWMM 5.2, ICM SWMM, InfoSWMM, InfoSewer, InfoAsset, and h2oCalc as content sources. Their license terms and the correctness of the stored source code were not independently checked.
5. No person has recorded a review of this summary.

## How to reproduce

Run the development app with `npm run dev`. Run the TypeScript check with `npm run check`. Build with `npm run build` and run the built app with `npm start`. These commands are defined in `package.json:6-11`. The project has no configured test command.

## Credits and licenses

- Robert Dickinson is the author named for this summary and the author recorded in the project Git history. The project license is MIT (`package.json:5`).
- Content source names in `server/seed.ts` include EPA SWMM 5.2, ICM SWMM, InfoSWMM, InfoSewer, InfoAsset, and h2oCalc. The source file does not state their licenses.
- Direct dependency license labels below are from installed package metadata. They are not a review of the full license terms or transitive dependencies.

| License label | Direct packages |
| --- | --- |
| MIT | `@hookform/resolvers`, `@jridgewell/trace-mapping`, `@radix-ui/react-accordion`, `@radix-ui/react-alert-dialog`, `@radix-ui/react-aspect-ratio`, `@radix-ui/react-avatar`, `@radix-ui/react-checkbox`, `@radix-ui/react-collapsible`, `@radix-ui/react-context-menu`, `@radix-ui/react-dialog`, `@radix-ui/react-dropdown-menu`, `@radix-ui/react-hover-card`, `@radix-ui/react-label`, `@radix-ui/react-menubar`, `@radix-ui/react-navigation-menu`, `@radix-ui/react-popover`, `@radix-ui/react-progress`, `@radix-ui/react-radio-group`, `@radix-ui/react-scroll-area`, `@radix-ui/react-select`, `@radix-ui/react-separator`, `@radix-ui/react-slider`, `@radix-ui/react-slot`, `@radix-ui/react-switch`, `@radix-ui/react-tabs`, `@radix-ui/react-toast`, `@radix-ui/react-toggle`, `@radix-ui/react-toggle-group`, `@radix-ui/react-tooltip`, `@tanstack/react-query`, `@tailwindcss/typography`, `@tailwindcss/vite`, `@types/connect-pg-simple`, `@types/express`, `@types/express-session`, `@types/node`, `@types/passport`, `@types/passport-local`, `@types/react`, `@types/react-dom`, `@types/ws`, `@vitejs/plugin-react`, `autoprefixer`, `clsx`, `cmdk`, `connect-pg-simple`, `date-fns`, `drizzle-kit`, `embla-carousel-react`, `esbuild`, `express`, `express-session`, `framer-motion`, `input-otp`, `memorystore`, `next-themes`, `passport`, `pg`, `postcss`, `react`, `react-day-picker`, `react-dom`, `react-hook-form`, `react-icons`, `react-resizable-panels`, `recharts`, `tailwind-merge`, `tailwindcss`, `tailwindcss-animate`, `tsx`, `tw-animate-css`, `vite`, `ws`, `zod`, `zod-validation-error` |
| Apache-2.0 | `class-variance-authority`, `drizzle-orm`, `drizzle-zod`, `typescript` |
| ISC | `lucide-react` |
| Unlicense | `wouter` |
| Not declared in installed package metadata | `passport-local`, `@replit/vite-plugin-cartographer`, `@replit/vite-plugin-dev-banner`, `@replit/vite-plugin-runtime-error-modal` |

## AI use

The project source, configuration, and `replit.md` do not name AI tools used to build the app. Git history attributes the recorded application changes to Robert Dickinson, including the repository, code-file terminology, and h2oCalc category changes. This does not establish whether AI tools were used. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

2026-03-09: Added h2oCalc as a code-file category and updated related counts.
2026-03-09: Changed the app from storing snippets to storing code files.
2026-03-09: Added the SWMM and sewer code repository.
2026-03-09: Extracted stack files.
2026-03-09: Created the initial commit.
