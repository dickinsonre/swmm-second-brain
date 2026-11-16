---
title: "BobSWMM Writer (app)"
type: entity
updated: 2026-11-15
sources: [S135, S141]
tags: [apps, replit, writing, ai-agents]
reviewed: 11/16/2026
---
Bob's Replit app BobSWMM Writer: an app that turns technical notes, transcripts and recordings into posts and articles by calling Anthropic Claude, with audio transcribed by Google Gemini; it runs no water-management simulation. Version 2.1.0, at `snagit-video-article--robertdickinson.replit.app` [S141](../sources/S141-bobswmm-writer-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S141](../sources/S141-bobswmm-writer-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S141](../sources/S141-bobswmm-writer-replit-summary.md)
- There is no simulation engine or engineering calculation in the code. Article work is prompt-based text generation. `engines: none`.
- `generateContent` maps model labels to Anthropic model IDs and calls the Anthropic Messages API. The composer displays 4 model choices; it offers Gemini for content, but the generation map routes that label to Claude.
- Uploaded video is held in memory. FFmpeg extracts the audio, audio above 7 MiB is split into chunks, and Gemini 2.5 Flash returns timestamped transcript entries.
- Video processing does not extract frames or create image files. It writes 3 fixed prompt records and 5 fixed capture-metadata records for each processed upload.
- Article quality indicators are string-presence checks, not an independent technical-accuracy review.
- Six main pages and five database tables (users, articles, prompts, transcripts and captures) in PostgreSQL on Neon.
- The composer contains 8 article styles, 8 target audiences, 9 output formats, 3 target lengths, 6 quality checks, 6 templates and 1 sample article.
- Articles can be downloaded as `.md`, `.html` or `.txt`. The composer saves an article with `published` status, but no LinkedIn posting integration was found.
- The screens label version `2.1.0` as current, while `package.json` declares `1.0.0`.
- `npm run check` failed with one diagnostic, TS2353. No test script or test files. All 6 routes rendered on initial load.
- Project license: MIT.

**What it does not show.** Video uploads, browser recording, FFmpeg processing, Gemini transcription, Claude generation and database writes were not exercised. `npm run build` was not run. No GitHub repository URL is configured. [S141](../sources/S141-bobswmm-writer-replit-summary.md)

**Noted at ingest.** It is a writing tool, not a modeling app. Its file name, snagit-video-article, does not say what it is (Q77). The `date:` is the newest commit date, 11 February 2026 (Q75). The file does not say which of Bob's posts, if any, were drafted in it; how fifty of his posts were received is on [LinkedIn posts that were well received](../concepts/linkedin-post-reception.md) [S135](../sources/S135-li-fifty-posts-with-counts.md).

See [Replit apps: six more summaries](../concepts/replit-app-summaries-third-batch.md), [LinkedIn posts that were well received](../concepts/linkedin-post-reception.md).
