---
title: "S244: ICM Exchange 2026, summary written from the page (v2026.2)"
type: source
raw: raw/apps/icm-exchange-2026-v2026.2.md
kind: app-md
author: Robert Dickinson
published: 2026-11-02
ingested: 2026-11-17
tags: [apps, icm, ruby, exchange, migration]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app ICM Exchange 2026, version 2026.2: a reference and Ruby migration guide that takes the October 2021 ICM Exchange manual (Version 2021.8, supplied by Bob) and reconciles it with Autodesk's current Ruby help, with the network tables, run parameters, short codes, an ICMExchange command builder and a Ruby 3.4 checker. Nothing ran inside ICM. Raw file: [raw/apps/icm-exchange-2026-v2026.2.md](../../raw/apps/icm-exchange-2026-v2026.2.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1793657728-75cb, reading its About and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app and document were built with Claude in a chat session in November 2026 at Bob's request; Bob supplied the manual and an outside review of the first version, which 2026.2 answers point by point. Claude read Autodesk's public repository, wrote the parsers, ledger, rule set and lexers, ran the 532-file sweep and built Ruby 2.4.10 from source.

**Claims worth keeping** (all copied from the file)
- Through the 2026 releases ICM ran scripts on an embedded Ruby 2.4.0; from 2027.0 it runs Ruby 3.4.6 and can load gems. In 2025.0 the capitalised method names (run_SQL, GIS_export, export_IDs and others) were lowercased; the old spellings still answer.
- Of the current help's 335 methods in 24 classes, 268 match the 2021.8 manual by name, 13 were renamed and 54 appear only in the current reference. From the 2021.8 side, 267 + 13 + 28 = 308 entries, 16 of them in classes that belong to WS Pro alone; the extra match is open, documented once on WSModelObject in 2021.8.
- Autodesk's public example repository, innovyze/Open-Source-Support at commit c580601 (2026-10-20), holds 532 .rb files, 96,652 lines; six files contain calls that fail under Ruby 3.4, four archived InfoSewer scenario-import tools and two InfoAsset scripts.
- The checker's lexer exists in JavaScript and Python; both were compared with views built from Ruby's own lexer, Ripper, and all three gave the same 282 findings, column for column.
- Removed Ruby calls and three of the defects were run on Ruby 2.4.10, 3.3.6 and 3.4.1 (WebAssembly); the messages shown are the interpreters' own.

**Limits it states.** Nothing ran inside ICM 2027 or through ICMExchange, and none of the Ruby versions used is ICM's 3.4.6. "Only in the current reference" compares two documents; it does not date when a method was added.

**Checked at ingest.** 267 + 13 + 28 = 308 and 268 + 13 + 54 = 335, as the page asserts in code. The Ruby version change bears on every script on [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://icm-exchange-2026.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [ICM Exchange 2026 (app)](../entities/icm-exchange-2026.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoWorks ICM](../entities/infoworks-icm.md), [InfoWorks ICM Ruby Script Runner (app)](../entities/icm-ruby-script-runner.md), [ICM InfoWorks release history (app)](../entities/icm-release-history-app.md).
