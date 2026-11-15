---
name: BobSWMM Writer
file: snagit-video-article--robertdickinson
version: 2.1.0
date: 2026-02-11
author: Robert Dickinson
links: {replit: https://snagit-video-article--robertdickinson.replit.app, repo: none}
engines: none
stack: TypeScript, React, Vite, Express, PostgreSQL on Neon, Drizzle ORM, Anthropic Claude API, Google Gemini API, Google Fonts
units: not applicable
ai_use: Anthropic Claude generates content; Google Gemini transcribes audio. No app-builder attribution is recorded.
---

# BobSWMM Writer: Prepare water-management content for publication

## What it does

BobSWMM Writer helps water-management and civil-engineering professionals turn technical notes, transcripts, and recordings into social and professional content. The article composer produces and edits drafts, headlines, hashtags, summaries, and alternate formats. Video and browser recordings can be submitted for audio transcription. The app stores article, transcript, prompt, and capture metadata in PostgreSQL; it does not run a water-management simulation. [client/src/App.tsx:20-26] [server/routes.ts:87-175] [server/routes.ts:370-481] [shared/schema.ts:12-47]

## How it computes

- There is no simulation engine or engineering calculation in the application code. Article work is prompt-based text generation, not a hydraulic model run.
- The article composer sends requests for topics, article text, content analysis, hashtags, headline variants, transcript formatting, and alternate formats to the Express API. `generateContent` in `server/ai.ts` maps model labels to Anthropic model IDs and calls the Anthropic Messages API. The UI also offers Gemini as a content-model choice, but the generation map routes that label to Claude. [client/src/components/LinkedInEditor.tsx:475-485] [client/src/components/LinkedInEditor.tsx:1463-1504] [server/ai.ts:29-58] [server/routes.ts:87-175] [server/routes.ts:192-485]
- Video uploads are held in Multer memory storage. `transcribeAudio` in `server/ai.ts` extracts audio from video with FFmpeg, splits audio above 7 MiB into chunks, and calls Gemini 2.5 Flash to return timestamped transcript entries. The API saves those entries in the transcript table. [server/routes.ts:593-612] [server/ai.ts:122-147] [server/ai.ts:149-189] [server/ai.ts:199-235] [server/ai.ts:238-300]
- Video processing does not extract frames or create image files. It writes 3 fixed prompt records and 5 fixed capture-metadata records for each processed upload. The captures page uses a bundled sample image when a capture has no image URL. [server/routes.ts:614-660] [client/src/components/ScreenCaptures.tsx:1-6] [client/src/components/ScreenCaptures.tsx:110-115]
- Article quality indicators are string-presence checks in `checkQualityItem` in `client/src/components/LinkedInEditor.tsx`, not an independent technical-accuracy review. [client/src/components/LinkedInEditor.tsx:211-221]

## Inputs and outputs

- The input page accepts files matching `video/*`. It also uses browser screen capture, microphone, and `MediaRecorder` APIs. Uploaded video is sent as multipart form data to `POST /api/process-video`. [client/src/components/VideoInput.tsx:61-62] [client/src/components/VideoInput.tsx:137-164] [client/src/components/VideoInput.tsx:260-265]
- The application stores articles, prompts, transcripts, and captures in PostgreSQL through Drizzle. The database schema also defines users. Transcript content is JSONB. The original video is kept in memory during the request; extracted audio uses temporary files that the code removes after processing. [shared/schema.ts:6-47] [db/index.ts:1-11] [server/storage.ts:34-115] [server/ai.ts:125-147]
- The browser stores the most recently processed transcript ID in `localStorage`. Transcript export downloads a `.txt` file. Articles can be downloaded as `.md`, `.html`, or `.txt`; rich-copy writes HTML and plain text to the clipboard. [client/src/components/VideoInput.tsx:116-120] [client/src/components/TranscriptView.tsx:120-135] [client/src/components/LinkedInEditor.tsx:421-473] [client/src/components/LinkedInEditor.tsx:1351-1408]
- Routes:
  - Articles: `GET /api/articles`, `GET /api/articles/:id`, `POST /api/articles`, `PATCH /api/articles/:id`, `DELETE /api/articles/:id`. [server/routes.ts:17-80]
  - Generation: `POST /api/generate/article`, `/api/generate/refine`, `/api/generate/prompts`, `/api/generate/summary`, `/api/generate/format-transcript`, `/api/generate/topics`, `/api/generate/analyze`, `/api/generate/hashtags`, `/api/generate/headlines`, and `/api/generate/multi-format`. [server/routes.ts:87-481]
  - Prompts: `GET /api/prompts`, `POST /api/prompts`. Transcripts: `GET /api/transcripts`, `GET /api/transcripts/:id`, `POST /api/transcripts`. Captures: `GET /api/captures`, `GET /api/captures/transcript/:transcriptId`, `POST /api/captures`. Video: `POST /api/process-video`. [server/routes.ts:486-674]

## Contents

- The router defines 6 main pages: article composer, input, transcript, captures, prompts, and documentation. [client/src/App.tsx:20-26]
- The database schema defines 5 tables: users, articles, prompts, transcripts, and captures. Live record totals were not queried. [shared/schema.ts:6-47]
- The composer contains 8 article styles, 8 target audiences, 9 output formats, 3 target lengths, 6 quality checks, 6 templates, and 1 sample article. [client/src/components/LinkedInEditor.tsx:38-70] [client/src/components/LinkedInEditor.tsx:93-100] [client/src/components/LinkedInEditor.tsx:102-143] [client/src/components/LinkedInEditor.tsx:145-149] [client/src/components/LinkedInEditor.tsx:172-209]
- The prompts page contains 3 hard-coded prompt cards. Video processing inserts 3 fixed prompts and 5 fixed capture records per processed upload. [client/src/components/NanoBananaPrompts.tsx:10-29] [server/routes.ts:614-660]
- The composer displays 4 model choices. Content-generation calls use Anthropic Claude model IDs; transcription calls use Gemini 2.5 Flash. [client/src/components/LinkedInEditor.tsx:1463-1504] [server/ai.ts:29-55] [server/ai.ts:238-244]

## Checks

- TypeScript check, `npm run check`: 0 passed, 1 failed diagnostic, TS2353, at `client/src/components/VideoInput.tsx:144`. The `cursor` property is not accepted in the declared `MediaTrackConstraints` type. [run: `npm run check`]
- Project tests: no test script is configured in `package.json`, and no `*.test.*` or `*.spec.*` files are tracked. [package.json:6-12] [tracked-file inventory]
- Preview: opened all 6 routes listed in `client/src/App.tsx`. All rendered on initial load. No browser errors were captured. [client/src/App.tsx:20-26] [preview run, 2026-11-15]
- Human review: none recorded.

## What this does not show

1. The UI labels version `2.1.0` as current, while `package.json` declares `1.0.0`. No release-date field was found. The front-matter date is the newest Git commit date, not a verified release date. [client/src/components/DocumentationView.tsx:333-341] [package.json:1-5] [git log, newest commit dated 2026-02-11]
2. Database record totals were not checked. Schema counts describe table definitions, not current database contents.
3. The production build command `npm run build` was not run. The TypeScript check fails as reported above.
4. Video uploads, browser recording, FFmpeg processing, Gemini transcription, Anthropic generation, and database writes were not exercised in this check.
5. The preview check loaded pages but did not test their interactive controls or verify the published pages.
6. The code's claim of capture extraction is not verified because the server creates fixed metadata instead of extracting video frames. [server/routes.ts:614-660]
7. The repository does not document which AI tools built the application or describe Robert Dickinson's individual contributions. The inspected Git commits are attributed to `robertdickinson`.
8. Licenses for every transitive dependency and FFmpeg were not checked.
9. No GitHub repository URL is configured. The only Git remote is an internal backup remote. [git remote -v]
10. The composer saves an article with `published` status, but no LinkedIn posting integration was found in the inspected source. [client/src/components/LinkedInEditor.tsx:758-793]

## How to reproduce

- Install dependencies with `npm install`, then run the development server with `npm run dev`.
- Run the configured TypeScript check with `npm run check`.
- Build for production with `npm run build`; start the built server with `npm run start`.
- These scripts are declared in `package.json`. There is no configured test command. [package.json:6-12]

## Credits and licenses

- Robert Dickinson: author named in this summary request and Git commit author shown in the inspected history. Recorded changes include Markdown rendering, headline generation, alternate content formats, AI model updates, and branding/navigation updates. No other contributor attribution is recorded. [git log, inspected commits dated 2026-02-04 through 2026-02-11]
- Project license: MIT. [package.json:1-5]
- License identifiers below are those declared in the installed package metadata for the named libraries:

| Library | License |
| --- | --- |
| React and React DOM | MIT |
| Express | MIT |
| Vite | MIT |
| TanStack Query | MIT |
| Drizzle ORM | Apache-2.0 |
| Neon serverless driver | MIT |
| Anthropic SDK | MIT |
| Google GenAI SDK | Apache-2.0 |
| TypeScript | Apache-2.0 |
| Tailwind CSS | MIT |
| Radix Dialog | MIT |
| Wouter | Unlicense |
| Lucide React | ISC |
| Multer and React Dropzone | MIT |
| Framer Motion | MIT |
| Zod | MIT |

## AI use

The source identifies Anthropic Claude for content generation and Google Gemini for transcription. The content-generation model mapping sends the listed non-Claude labels to Claude. The source does not identify Replit Agent or another AI tool as a builder. Git history attributes the inspected commits to `robertdickinson`; recorded change subjects include Markdown rendering, headline generation, alternate formats, AI model updates, and branding. [server/ai.ts:29-55] [server/ai.ts:238-244] [git log, latest 10 commits]

This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

- 2026-02-11: Saved progress at the end of the loop.
- 2026-02-11: Improved Markdown rendering and added headline generation features.
- 2026-02-11: Published the app.
- 2026-02-07: Published the app.
- 2026-02-04: Saved progress at the end of the loop.
- 2026-02-04: Added content formats and optimized interface elements.
- 2026-02-04: Published the app.
- 2026-02-04: Published the app.
- 2026-02-04: Upgraded AI models and updated interface branding.
- 2026-02-04: Updated branding and navigation labels.
