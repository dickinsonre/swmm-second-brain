---
title: "S145: ICM Ruby to Nano Banana Prompt, summary written by Replit Agent (v1.0.0)"
type: source
raw: raw/apps/icm-flow-visualizer-robertdickinson-v1.0.0.md
kind: app-md
author: Robert Dickinson
published: 2025-11-19
ingested: 2026-11-15
tags: [apps, replit, icm, ruby, ai-agents]
reviewed: no
---
**What it is.** A technical summary of ICM Ruby to Nano Banana Prompt, version 1.0.0: an app that reads ICM Ruby scripts and SWMM5 input files, draws a workflow from the Ruby methods, counts sections and code patterns, and asks Gemini to explain the code; it runs no engine and does not execute Ruby. It is one of Bob's Replit apps, at `swmm5toicmswmmworkflow.com`. Raw file: [raw/apps/icm-flow-visualizer-robertdickinson-v1.0.0.md](../../raw/apps/icm-flow-visualizer-robertdickinson-v1.0.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says the project records do not name an AI app builder. When it runs, the app sends prompts to Gemini, `gemini-2.5-flash`. The copy here was read out of the editor of the Replit project named ICMFlowVisualizer on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
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

**Limits it states.** The POST APIs, file uploads and Gemini responses were not exercised with uploaded files. Production behavior was not tested.

**Checked at ingest.** The app goes by three names: ICM Ruby to Nano Banana Prompt in the file, icm-flow-visualizer in its `file:` and swmm5toicmswmmworkflow.com as its address (Q77). The `date:`, 19 November 2025, is the first Git record of version 1.0.0; the change list runs to 7 February 2026 (Q75). It is one of two apps for ICM Ruby scripts ingested together, with the [InfoWorks ICM Ruby Script Runner (app)](../entities/icm-ruby-script-runner.md) [S150](S150-icm-ruby-script-runner-replit-summary.md).

**Feeds:** [ICM Ruby to Nano Banana Prompt (app)](../entities/icm-ruby-nano-banana-prompt.md), [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [InfoWorks ICM Ruby Script Runner (app)](../entities/icm-ruby-script-runner.md), [InfoWorks ICM](../entities/infoworks-icm.md).
