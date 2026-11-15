---
name: SWMM Manual Search
file: video-search
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://video-search.replit.app, repo: none}
engines: none
stack: TypeScript, React, Vite, Express, Tailwind CSS, Node.js; PostgreSQL and Drizzle scaffolding; Google Fonts
units: not applicable
ai_use: Replit Agent wrote this summary; the project does not record implementation AI attribution.
---

# SWMM Manual Search: Promotional landing page for a separate manual-search site

## What it does

This project serves a promotional landing page for SWMM Manual Search. It describes a separate search service for finding equations, parameters, and INP syntax in the SWMM manual (`client/src/pages/Home.tsx:84-96`). The page links to `https://sjswmm5manualsearch.com` and shows a demo video with an audio control (`client/src/pages/Home.tsx:107-126`). This project does not implement manual search or display search results.

## How it computes

The landing page performs no search or simulation calculations. The `Home` component renders the page, animates its sections, and controls local audio playback (`client/src/pages/Home.tsx:6-26, 63-67, 107-126`). The server registers no application API routes (`server/routes.ts:5-15`). The footer renders the current year with `new Date().getFullYear()` (`client/src/pages/Home.tsx:179-182`).

## Inputs and outputs

- Inputs are browser navigation and clicks on page controls. The source has no file-upload input.
- The browser renders the home route and a not-found page for unmatched routes (`client/src/App.tsx:9-15`).
- The page loads `swmm-video.mp4` and `carmen.mp3` (`client/src/pages/Home.tsx:107-116`). `client/index.html:17` references `favicon.png`. `opengraph.jpg` is present in `client/public/` but is not referenced by the current HTML.
- The navigation and search calls-to-action link to `https://sjswmm5manualsearch.com` (`client/src/pages/Home.tsx:39-49, 88-96`).
- No search queries or user files are written by this landing page. Backend scaffolding includes an in-memory user store and a Drizzle `users` schema, but no application route uses that store (`server/storage.ts:13-38`, `shared/schema.ts:6-18`, `server/routes.ts:5-15`).
- Google Fonts is loaded by the HTML page (`client/index.html:18-20`). No API service is called by the landing page source.

## Contents

- One explicitly routed home page and one not-found fallback are configured in `client/src/App.tsx:11-14`.
- Three feature cards are rendered in `client/src/pages/Home.tsx:156-175`.
- Public media and image files are `carmen.mp3`, `swmm-video.mp4`, `favicon.png`, and `opengraph.jpg` in `client/public/`.
- No manual corpus, search records, or simulation models are included in the repository source files.
- The page copy states that it covers 53 documents, 621 sections, and 248,407 words (`client/src/pages/Home.tsx:151-153`). These displayed figures are not counted from a local corpus.

## Checks

- Tests: no test script is defined in `package.json:6-12`, and `git ls-files | grep -E '(^|/)(test|tests|__tests__)(/|$)|\.(test|spec)\.[^/]+$'` found no tracked test files. Test command: none. Tests run: 0. Passed: 0. Failed: 0.
- TypeScript check: `npm run check -- --incremental false` completed successfully. The `check` script runs `tsc` (`package.json:6-12`).
- The home page loaded in the preview. A request to `/` returned HTTP 200. The video and audio assets returned HTTP 200.
- The unmatched-route preview rendered the not-found page. Browser logs showed Vite connection and React DevTools informational messages; no browser errors were shown.
- Human review: none recorded.

## What this does not show

1. The separate search service at `https://sjswmm5manualsearch.com` was not tested. Its search behavior and the figures shown in the landing-page copy are not verified here.
2. The audio control and outbound links were not manually clicked during these checks.
3. Licenses and attribution for the bundled video, audio recording, and Google Fonts were not verified; their licenses are not stated in this repository.
4. Automated behavior tests were not checked because the repository has no test script or tracked test suite.
5. The repository does not record a release date for version 1.0.0. The front-matter date is the date this summary was prepared.
6. No human review of this summary or the app is recorded in the project.

## How to reproduce

```sh
npm install
npm run dev
```

Run the available TypeScript check with:

```sh
npm run check
```

No automated test command is defined in `package.json:6-12`.

## Credits and licenses

- Robert Dickinson is the named author. Git history records commits under `robertdickinson`.
- The project declares MIT in `package.json:5`.
- React, React DOM, Vite, Express, Framer Motion, Tailwind CSS, TanStack Query, and Radix Tooltip declare MIT licenses in their installed package manifests.
- Lucide React declares ISC. Wouter declares Unlicense.
- The page references SWMM, EPA, and InfoWorks ICM (`client/src/pages/Home.tsx:84-86, 134-136, 171-173`). Their licenses are not stated in this project.
- Google Fonts supplies Inter and Space Grotesk (`client/index.html:18-20`). Their license terms were not checked.
- The video and audio asset files do not have license or attribution details recorded in the source.

## AI use

The project source and Git history do not identify an AI tool used to implement the app. Git history attributes the initial project, landing page/video, and audio-control commits to `robertdickinson`, but does not separate work by person or tool. Replit Agent wrote this summary.

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

2026-02-19: Published your App
2026-02-19: Saved progress at the end of the loop
2026-02-19: Published your App
2026-02-19: Add operatic music and audio controls to the promotional video
2026-02-19: Published your App
2026-02-19: Update landing page with a modern dark mode aesthetic and animated video
2026-02-19: Extracted stack files
2026-02-19: Initial commit
