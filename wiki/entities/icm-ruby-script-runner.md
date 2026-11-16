---
title: "InfoWorks ICM Ruby Script Runner (app)"
type: entity
updated: 2026-11-15
sources: [S145, S150, S152]
tags: [apps, replit, icm, ruby, ai-agents, security]
reviewed: no
---
Bob's Replit app InfoWorks ICM Ruby Script Runner: an app with a web editor that ran Ruby scripts for InfoWorks ICM on the server and returned their output, with AI explanations through gpt-5, templates, an API reference page and GitHub browsing. Version 0.1.0, at `ruby-script-ai.replit.app` [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md).

**A caution about its source.** Everything on this page rests on [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md), which Replit Agent wrote on 15 November 2026 from the project's source. Nothing here has been read by Bob (Q74).

**What the summary says** [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md)
- `run_script` checks submitted Ruby for emptiness, length and a list of blocked strings, writes it to a temporary `.rb` file and runs the `ruby` executable, with a 50,000-character limit and a 30-second timeout.
- The Ruby script filter is not a security sandbox. The README warns against exposing the app publicly without authentication and additional sandboxing, and the code executes user-submitted Ruby on the server.
- Explanations, answers and Markdown documentation come through the OpenAI Python client; the model name is `gpt-5`.
- It includes no InfoWorks ICM engine. The ICM-specific examples require the InfoWorks ICM environment for those APIs. `engines: none`.
- Uploaded `.rb` files are saved under `uploaded_scripts/`; the request-size limit is 5 MB. No database.
- 2 HTML pages and 14 API routes, 16 in all; 8 Ruby example files and 6 templates.
- Python 3.11 and Ruby 3.2 runtimes. CodeMirror `5.65.2` is loaded from a CDN.
- `python -m unittest discover -v` found 0 tests. `ruby examples/01_hello_world.rb` passed. The production `GET /` and `GET /docs` returned HTTP 200 on 2026-11-15.
- The project has no license file or license statement.

**What it does not show.** The test suite contains no tests. AI requests, GitHub access and browser behavior were not checked. ICM-specific scripts were not run inside InfoWorks ICM. [S150](../sources/S150-icm-ruby-script-runner-replit-summary.md)

**Noted at ingest.** Retired. Bob deleted the app on the evening of 15 November 2026 and wrote that it is better to use ICM Exchange anyway [S152](../sources/S152-note-ruby-script-runner-deleted.md). Before that, in the same session, Replit Agent had reported that the Replit runtime offered no usable operating-system sandbox; that report is in the note, not in this file. The `date:`, 7 November 2025, is the first Git record of version 0.1.0; the change list shows the app published on 21 July 2026 (Q75). It and [ICM Ruby to Nano Banana Prompt (app)](icm-ruby-nano-banana-prompt.md) [S145](../sources/S145-icm-ruby-nano-banana-prompt-replit-summary.md) were both tools for ICM Ruby scripts.

See [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [ICM Ruby to Nano Banana Prompt (app)](icm-ruby-nano-banana-prompt.md), [InfoWorks ICM](infoworks-icm.md).
