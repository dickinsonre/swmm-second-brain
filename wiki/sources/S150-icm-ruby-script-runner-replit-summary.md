---
title: "S150: InfoWorks ICM Ruby Script Runner, summary written by Replit Agent (v0.1.0)"
type: source
raw: raw/apps/ruby-script-ai-v0.1.0.md
kind: app-md
author: Robert Dickinson
published: 2025-11-07
ingested: 2026-11-15
tags: [apps, replit, icm, ruby, ai-agents, security]
reviewed: no
---
**What it is.** A technical summary of InfoWorks ICM Ruby Script Runner, version 0.1.0: an app with a web editor that ran Ruby scripts for InfoWorks ICM on the server and returned their output, with AI explanations through gpt-5, templates, an API reference page and GitHub browsing. It is one of Bob's Replit apps, at `ruby-script-ai.replit.app`. Raw file: [raw/apps/ruby-script-ai-v0.1.0.md](../../raw/apps/ruby-script-ai-v0.1.0.md).

**How it was written. This one is different.** The app ships no summary of its own making. Replit Agent wrote the file on 15 November 2026 from the project's source, and the file says Bob has not yet reviewed it (Q74). Of the app itself it says Git metadata records both `robertdickinson` and agent-authored commits, labelled `Agent`, and names no other app-building AI tool. When it runs, the app calls model `gpt-5` through the OpenAI Python client via Replit AI Integrations. The copy here was read out of the editor of the Replit project named RubyScriptAI on 15 November 2026 and matched a SHA-256 computed there (see the log).

**Claims worth keeping** (all copied from the file)
- `run_script` checks submitted Ruby for emptiness, length and a list of blocked strings, writes it to a temporary `.rb` file and runs the `ruby` executable, with a 50,000-character limit and a 30-second timeout.
- The Ruby script filter is not a security sandbox. The README warns against exposing the app publicly without authentication and additional sandboxing, and the code executes user-submitted Ruby on the server.
- Explanations, answers and Markdown documentation come through the OpenAI Python client; the model name is `gpt-5`.
- It includes no InfoWorks ICM engine. The ICM-specific examples require the InfoWorks ICM environment for those APIs. `engines: none`.
- Uploaded `.rb` files are saved under `uploaded_scripts/`; the request-size limit is 5 MB. No database.
- 2 HTML pages and 14 API routes, 16 in all; 8 Ruby example files and 6 templates.
- Python 3.11 and Ruby 3.2 runtimes. CodeMirror `5.65.2` is loaded from a CDN.
- `python -m unittest discover -v` found 0 tests. `ruby examples/01_hello_world.rb` passed. The production `GET /` and `GET /docs` returned HTTP 200 on 2026-11-15.
- The project has no license file or license statement.

**Limits it states.** The test suite contains no tests. AI requests, GitHub access and browser behavior were not checked. ICM-specific scripts were not run inside InfoWorks ICM.

**Checked at ingest.** Retired. Bob deleted the app on the evening of 15 November 2026 and wrote that it is better to use ICM Exchange anyway [S152](S152-note-ruby-script-runner-deleted.md). Before that, in the same session, Replit Agent had reported that the Replit runtime offered no usable operating-system sandbox; that report is in the note, not in this file. The `date:`, 7 November 2025, is the first Git record of version 0.1.0; the change list shows the app published on 21 July 2026 (Q75). It and [ICM Ruby to Nano Banana Prompt (app)](../entities/icm-ruby-nano-banana-prompt.md) [S145](S145-icm-ruby-nano-banana-prompt-replit-summary.md) were both tools for ICM Ruby scripts.

**Feeds:** [InfoWorks ICM Ruby Script Runner (app)](../entities/icm-ruby-script-runner.md), [Replit apps: a fourth set of six summaries](../concepts/replit-app-summaries-fourth-batch.md), [ICM Ruby to Nano Banana Prompt (app)](../entities/icm-ruby-nano-banana-prompt.md), [InfoWorks ICM](../entities/infoworks-icm.md).
