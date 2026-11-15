---
name: EPANET Quizzer
file: epanet-quizzer-robertdickinson
version: 1.0.0
date: 2026-11-15
author: Robert Dickinson
links: {replit: https://epanetquizzer.com, repo: none}
engines: none
stack: TypeScript, React, Vite, Express, in-memory storage, Drizzle schema, KaTeX, Google Fonts
units: both
ai_use: No AI tools are identified in the checked project source, docs, or git log.
---

# EPANET Quizzer: quizzes on hydraulic modeling concepts

## What it does

EPANET Quizzer presents quizzes about hydraulic modeling and water distribution topics. Learners select a category, answer multiple-choice questions, and can use timed or practice mode. Questions can include worked explanations and mathematical notation. Results show a score, correct-answer count, elapsed time, and topic breakdown. The app teaches EPANET concepts; it does not run EPANET simulations. (client/src/pages/home.tsx:103-129; client/src/pages/quiz.tsx:23-35, 79-98; client/src/pages/results.tsx:47-71)

## How it computes

- Quiz questions, answer choices, correct-answer flags, explanations, difficulty, topics, and time limits are seeded in server memory. Some question records are generated from templates. (server/storage.ts:72-110, 116-855, 1045-1273)
- The quiz compares the selected choice with the stored correct choice. It counts correct answers and computes the score as `round(correct answers / total questions * 100)`. The quiz page does this in `completeQuiz`; `calculateScore` in the shared quiz utilities uses the same formula. (client/src/pages/quiz.tsx:111-163, 190-208; client/src/lib/quiz-data.ts:34-37)
- The results page groups questions by topic and calculates each topic percentage as `round(correct answers in topic / questions in topic * 100)`. (client/src/pages/results.tsx:60-71, 135-153)
- Timed mode counts down from each question's configured time limit. Practice mode does not run the countdown. (client/src/pages/quiz.tsx:23-30, 79-98)
- Missed-question storage schedules a first review after 1 day. When the user marks a missed question correct, the interval is multiplied by 2.5 and capped at 30 days. (server/storage.ts:1005-1039)
- The app does not call an EPANET engine or calculate hydraulic results. Hydraulic equations and worked calculations are stored as question and explanation text. (server/storage.ts:116-855, 1045-1273)

## Inputs and outputs

- The app does not read user-uploaded files or write downloadable files. Question content is embedded in `server/storage.ts`.
- The browser exchanges JSON with Express routes. The client routes are `/`, `/quiz/:categoryId`, and `/results/:sessionId`. (client/src/App.tsx:11-18)
- API routes provide categories and questions, anonymous-user data, quiz sessions, progress, and missed questions. They include `GET /api/categories`, `GET /api/categories/:categoryId/questions`, `GET /api/user`, `POST /api/quiz-sessions`, `GET` and `PATCH /api/quiz-sessions/:sessionId`, `GET /api/user/quiz-sessions`, `GET /api/user/progress`, `GET` and `POST /api/user/missed-questions`, and `POST /api/user/missed-questions/:questionId/correct`. (server/routes.ts:48-183)
- Users, categories, questions, sessions, progress, and missed-question records are held in JavaScript `Map` objects in server memory. A Drizzle schema describes database tables, but the active storage class is `MemStorage`. (server/storage.ts:27-70; shared/schema.ts:6-61)
- Anonymous user IDs are held in an `httpOnly`, `sameSite: "lax"` cookie with a one-year maximum age. (server/routes.ts:9-10, 25-45)
- A server restart clears in-memory user and quiz data. The seeded quiz questions are initialized when the storage object is created. (server/storage.ts:54-70)

## Contents

The category and question counts below were checked by requesting `/api/categories` and each category's question endpoint from the running app. The records are seeded in `server/storage.ts:72-110, 116-855, 1045-1273`.

| Category | Questions |
| --- | ---: |
| Hydraulic Fundamentals | 70 |
| Network Components | 70 |
| Water Quality Modeling | 60 |
| Advanced Analysis | 50 |
| Total | 250 |

The server returned four categories and 250 question records across those endpoints during the check.

## Checks

- `npm test`: failed before running tests because `package.json` defines no `test` script. No test files were found outside dependencies and tool directories.
- `npm run check`: failed with 2 TypeScript errors. One reports the regular-expression `s` flag requires an ES2018-or-newer target in `client/src/components/math-text.tsx:31`. One reports that `timeCompleted` is passed as a string where the storage update type expects a `Date` in `server/routes.ts:116`.
- Browser page check: `/` and `/quiz/hydraulic-fundamentals` rendered in the running preview without page errors. `/results/` rendered with a temporary completed in-memory session and no browser errors. An invalid result-session URL showed the expected not-found state and a 404 response.
- Human review: none recorded.

## What this does not show

1. The hydraulic facts and worked solutions have not been independently checked by a subject-matter reviewer.
2. Submitting answers through a full browser quiz and completing the entire quiz flow were not checked.
3. The production build command `npm run build` was not run.
4. Persistent storage across server restarts was not tested; the code uses in-memory maps.
5. The deployment service reported the app as deployed at `https://epanetquizzer.com`. This check did not test the deployed site's pages or API.
6. `package.json` identifies version `1.0.0`, but the project does not record that version's release date. The front-matter date is the date this summary was written, not a verified release date. (package.json:3; `git log -10`, run 2026-11-15)

## How to reproduce

- Start the app: `npm run dev`. (package.json:6-10)
- Run the declared type check: `npm run check`. It currently reports the errors listed under Checks.
- Run tests: no test command is configured. `npm test` reports a missing script.
- Production build command, not run for this summary: `npm run build`. (package.json:6-10)

## Credits and licenses

- Project license: MIT, as declared in `package.json:5`. No separate project license file was found.
- React, Vite, Express, Zod, Tailwind CSS, TanStack Query, and KaTeX: each package declares the MIT license in its installed package metadata.
- Wouter and Drizzle ORM are used by the project. Their installed package metadata was not available through the package metadata check, so their licenses were not checked.
- EPANET is named in quiz content and linked documentation. No EPANET engine is bundled or run, and the license of the linked reference materials was not checked.
- The home page links to the U.S. EPA EPANET page, EPANET documentation on Read the Docs, OpenWaterAnalytics/EPANET on GitHub, and Google Fonts. (client/src/pages/home.tsx:70-98, 161-167; client/index.html)

## AI use

The checked source, project documentation, and git log do not identify AI tools used to build the app or describe Robert Dickinson's individual coding contributions. The recent git commits are attributed to `robertdickinson`. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

From `git log -10`, newest first. The dates and entries below come from that command run on 2026-11-15.

- 2026-02-12: Published your App
- 2026-02-11: Saved progress at the end of the loop
- 2026-02-11: Enhance quiz application with math rendering and user session management
- 2026-02-11: Add detailed app review and grade to the home page
- 2026-02-11: Add a comprehensive app review section to the home page
- 2026-02-11: Published your App
- 2026-02-11: Update the home page to display prioritized improvement ideas
- 2026-02-11: Published your App
- 2026-02-11: Add last updated date to the application footer
- 2026-02-11: Published your App
