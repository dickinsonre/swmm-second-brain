---
name: InfoDrainage Explorer
file: bob-swmm-info
version: 1.0.0
date: 2026-02-11
author: Robert Dickinson
links: {replit: "https://bob-swmm-info.replit.app", repo: none}
engines: none
stack: TypeScript, React, Vite, Express, Tailwind CSS; Autodesk Help links; swmm5.org link
units: not applicable
ai_use: App-generation AI use is not documented in checked project records.
---

# InfoDrainage Explorer: A personal reference and learning tool for InfoDrainage

## What it does

It organizes reference material about InfoDrainage product history, technical features, and help topics. Users can compare listed features, answer quiz questions, search a documentation index, and view technical facts. The app is presented as a personal learning tool by Bob Dickinson (bobSWMM), and provides a browser interface rather than running drainage simulations (`replit.md:4-10`; `client/src/pages/home.tsx:18-21,26-57`).

## How it computes

- `TimelineTab` in `client/src/components/timeline-tab.tsx:25-130` filters the static release list by category and major-feature flag. It totals the visible features, major features, and releases. The data comes from `APP_DATA.timeline` in `client/src/data/app-data.ts:76-374`.
- `ComparisonTab` in `client/src/components/comparison-tab.tsx:10-34,91-108` filters static comparison categories. It compares each row's values with `JSON.stringify` to count rows with differences and optionally hide matching rows. The source values are in `client/src/data/app-data.ts:375-454`.
- `QuizTab` in `client/src/components/quiz-tab.tsx:10-17,43-82` shuffles the filtered question list with a Fisher-Yates loop, checks selected answer indices against each question's `correct` index, and calculates the percentage as `round(correct answers / answered questions * 100)`. Quiz answers and score are held in component state.
- `NavigatorTab` in `client/src/components/navigator-tab.tsx:11-24,57-117` filters the embedded page titles by search text and loaded flags. It forms Autodesk Help links from the static base URL and page GUIDs (`client/src/data/app-data.ts:74,489-581`).
- `FactsTab` in `client/src/components/facts-tab.tsx:62-133` displays values and equation strings from `APP_DATA.facts` (`client/src/data/app-data.ts:582-600`). The app does not execute those hydraulic equations or call a simulation engine.

## Inputs and outputs

- The app does not read uploaded files or write exported files.
- The browser loads the single-page app at `/`. The client-side route is defined in `client/src/App.tsx:9-14`.
- No application API endpoints are registered (`server/routes.ts:5-15`). The Express server serves the client app (`server/index.ts:62-103`; `server/static.ts:5-18`).
- Static reference data is bundled in `client/src/data/app-data.ts`. Quiz selections and filters remain in React component state. The light/dark preference is stored in browser `localStorage` under `theme` (`client/src/components/theme-toggle.tsx:5-21`).
- The app links to Autodesk Help and swmm5.org (`client/src/data/app-data.ts:74`; `client/src/pages/home.tsx:63-66`). It does not fetch their page content into the app.

## Contents

Counts below were calculated from the current `APP_DATA` export on 2026-11-15 with a `tsx` runtime count. The corresponding arrays are in `client/src/data/app-data.ts`.

| Content | Count | Source |
|---|---:|---|
| Timeline releases | 31 | `client/src/data/app-data.ts:77-374` |
| Timeline features | 109 | `client/src/data/app-data.ts:77-374` |
| Timeline features marked major | 63 | `client/src/data/app-data.ts:77-374` |
| Comparison categories | 8 | `client/src/data/app-data.ts:375-454` |
| Comparison feature rows | 46 | `client/src/data/app-data.ts:375-454` |
| Quiz questions | 30 | `client/src/data/app-data.ts:456-487` |
| Help sections | 10 | `client/src/data/app-data.ts:489-581` |
| Help child entries | 56 | `client/src/data/app-data.ts:489-581` |
| Help entries marked loaded, including sections | 54 | `client/src/data/app-data.ts:489-581` |

The footer says “53 key pages” (`client/src/pages/home.tsx:66`). The count of loaded section and child entries in the current data is 54. These are different counts; the source does not explain the difference.

## Checks

- `npm run check`: passed. TypeScript exited successfully.
- `npm test`: no test suite ran. The command exited because `package.json` defines no `test` script. Zero test cases ran, zero passed, and zero failed (`package.json:6-11`).
- Metadata: `package.json` declares version 1.0.0 (`package.json:3`). The footer displays v1.0 and last updated February 11, 2026 (`client/src/pages/home.tsx:62`). The latest Git commit is dated 2026-02-11.
- Deployment metadata checked on 2026-11-15 returned the public URL `https://bob-swmm-info.replit.app`. The site name in the front matter is the subdomain before `.replit.app`.
- App route `/`: loaded from the running development app with HTTP 200 on 2026-11-15. A browser screenshot showed the default timeline view. No browser console errors appeared in that capture. The only client route is `/` (`client/src/App.tsx:9-14`).
- Human review: none recorded.

## What this does not show

1. The quiz, filters, theme toggle, and other tab interactions were not checked with browser automation. No project test suite is configured.
2. The Autodesk Help links were not checked; they were not opened to confirm that their destinations still work.
3. Technical statements in the embedded reference data were not independently checked against current Autodesk documentation.
4. The production build was not checked.
5. The development server logged warnings about outdated Browserslist data and a PostCSS `from` option. Their causes and effects were not checked.
6. A public GitHub repository URL was not found. The configured Git origin is internal, so the repository link is listed as none.

## How to reproduce

```sh
npm install
npm run dev
```

Run the available TypeScript check with:

```sh
npm run check
```

There is no `npm test` script in `package.json`.

## Credits and licenses

- Robert Dickinson is named in the project instructions and app footer (`replit.md:4`; `client/src/pages/home.tsx:62`).
- The root `package.json` declares the project license as MIT (`package.json:5`). No root `LICENSE` file is tracked.
- React and React DOM: MIT. Vite: MIT. Express: MIT. Tailwind CSS: MIT. TanStack React Query: MIT. Framer Motion: MIT. These licenses are recorded in their installed package metadata.
- Lucide React: ISC, as recorded in its installed package metadata.
- Autodesk InfoDrainage and Autodesk Help are named in the app's reference content. No license for that content was checked.
- Licenses for other dependencies were not audited.

## AI use

The checked source, project documentation, and Git history do not record which tools, if any, were used to build the app. Git commits are attributed to `robertdickinson`; the project instructions credit Robert Dickinson (`replit.md:4`; Git log checked on 2026-11-15). This does not establish whether AI tools were used during app development.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Git history, newest first, checked on 2026-11-15:

- 2026-02-11: Added the last update date to the application footer.
- 2026-02-11: Published the app.
- 2026-02-11: Reframed the site as a personal learning tool for Bob Dickinson.
- 2026-02-11: Published the app.
- 2026-02-10: Published the app.
- 2026-02-10: Saved progress at the end of the loop.
- 2026-02-10: Added the interactive InfoDrainage Explorer tabs.
- 2026-02-10: Extracted stack files.
- 2026-02-10: Created the initial commit.
