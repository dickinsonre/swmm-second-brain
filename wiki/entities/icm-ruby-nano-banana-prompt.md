---
title: "ICM Ruby to Nano Banana Prompt (app)"
type: entity
updated: 2026-11-15
sources: [S145, S150]
tags: [apps, replit, icm, ruby, ai-agents]
reviewed: 11/16/2026
---
Bob's Replit app ICM Ruby to Nano Banana Prompt: an app that reads ICM Ruby scripts and SWMM5 input files, draws a workflow from the Ruby methods, counts sections and code patterns, and asks Gemini to explain the code; it runs no engine and does not execute Ruby. Version 1.0.0, at `swmm5toicmswmmworkflow.com` [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md)
- Users upload one Ruby file, a folder of Ruby files or one `.inp` file. The app does not call an ICM or SWMM simulation engine. `engines: none`.
- `parseRubyFile` scans Ruby text for method definitions and creates one workflow node per matching method, connected in order. This is a text-pattern parser, not a Ruby interpreter.
- `parseSWMM5File` reads section headers and counts nonblank, non-comment lines under each section.
- The `/api/mermaid-diagram` handler counts code patterns with regular expressions and returns a text diagram. It does not execute Ruby.
- Three handlers send prompts to Gemini using `gemini-2.5-flash`.
- The default workflow is example data: 23 nodes and 24 edges (1 start, 15 process, 5 decision, 1 data and 1 end), 7 file configuration records and 14 sample log records. They do not verify an actual ICM import.
- Workflow data, logs and Markdown are held in server memory.
- `npm run check` failed with 34 TypeScript diagnostics. No test script is declared and no test files were found.
- The HTML page title and description still use SWMM5 workflow wording, unlike the app's displayed name.
- The reference dialog names Markdown files under `/reference/` that were not present in the current `client/public` listing.
- The package declares MIT; no standalone license file is tracked.

**What it does not show.** The POST APIs, file uploads and Gemini responses were not exercised with uploaded files. Production behavior was not tested. [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md)

**Noted at ingest.** The app goes by three names: ICM Ruby to Nano Banana Prompt in the file, icm-flow-visualizer in its `file:` and swmm5toicmswmmworkflow.com as its address (Q77). The `date:`, 19 November 2025, is the first Git record of version 1.0.0; the change list runs to 7 February 2026 (Q75). It is one of two apps for ICM Ruby scripts ingested together, with the [InfoWorks ICM Ruby Script Runner (app)](icm-ruby-script-runner.md) [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md).

See [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [InfoWorks ICM Ruby Script Runner (app)](icm-ruby-script-runner.md), [InfoWorks ICM](infoworks-icm.md).
