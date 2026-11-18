---
title: "ICM Exchange 2026 (app)"
type: entity
updated: 2026-11-17
sources: [S205, S244]
tags: [apps, icm, ruby, exchange, migration]
reviewed: no
---
Bob's app ICM Exchange 2026: a reference and Ruby migration guide that takes the October 2021 ICM Exchange manual (Version 2021.8, supplied by Bob) and reconciles it with Autodesk's current Ruby help, with the network tables, run parameters, short codes, an ICMExchange command builder and a Ruby 3.4 checker. Nothing ran inside ICM. Version 2026.2, 2026-11-02 [S244](../sources/S244-icm-exchange-2026-summary.md). Netlify address: https://icm-exchange-2026.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S244](../sources/S244-icm-exchange-2026-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S244](../sources/S244-icm-exchange-2026-summary.md)
- Through the 2026 releases ICM ran scripts on an embedded Ruby 2.4.0; from 2027.0 it runs Ruby 3.4.6 and can load gems. In 2025.0 the capitalised method names (run_SQL, GIS_export, export_IDs and others) were lowercased; the old spellings still answer.
- Of the current help's 335 methods in 24 classes, 268 match the 2021.8 manual by name, 13 were renamed and 54 appear only in the current reference. From the 2021.8 side, 267 + 13 + 28 = 308 entries, 16 of them in classes that belong to WS Pro alone; the extra match is open, documented once on WSModelObject in 2021.8.
- Autodesk's public example repository, innovyze/Open-Source-Support at commit c580601 (2026-10-20), holds 532 .rb files, 96,652 lines; six files contain calls that fail under Ruby 3.4, four archived InfoSewer scenario-import tools and two InfoAsset scripts.
- The checker's lexer exists in JavaScript and Python; both were compared with views built from Ruby's own lexer, Ripper, and all three gave the same 282 findings, column for column.
- Removed Ruby calls and three of the defects were run on Ruby 2.4.10, 3.3.6 and 3.4.1 (WebAssembly); the messages shown are the interpreters' own.

**What it does not show.** Nothing ran inside ICM 2027 or through ICMExchange, and none of the Ruby versions used is ICM's 3.4.6. "Only in the current reference" compares two documents; it does not date when a method was added. [S244](../sources/S244-icm-exchange-2026-summary.md)

**Noted at ingest.** 267 + 13 + 28 = 308 and 268 + 13 + 54 = 335, as the page asserts in code. The Ruby version change bears on every script on [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md).

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [InfoWorks ICM](infoworks-icm.md), [InfoWorks ICM Ruby Script Runner (app)](icm-ruby-script-runner.md), [ICM InfoWorks release history (app)](icm-release-history-app.md).
