---
name: ICM Exchange 2026
file: icm-exchange-2026.html
version: "2026.2"
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/At1xHF4er17JHbYtf949de", repo: none named in the page}
engines:
  - {name: none (a reference and checker), note: "Ruby checks ran on Ruby 2.4.10, 3.3.6 and 3.4.1 (WebAssembly), not inside ICM"}
sources_used: {old_manual: "ICM Exchange / InfoAsset Exchange / WS Pro Exchange, Version 2021.8, October 2021 (supplied by Bob)", current_help: "ruby_icm_help.md in innovyze/Open-Source-Support at commit c580601ecb6fabb00ce4363ab8443febb594cd27 (2026-10-20), MIT"}
units: none (methods, files, lines)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app and document were built with Claude at Robert Dickinson's request. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/At1xHF4er17JHbYtf949de, version 1793657728-75cb (index.html, 1,344,591 bytes, SHA-256 f77c6d9eca708fedab766c2579eed6bc979802af569085f2f2ae0728936e0789), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# ICM Exchange 2026: the 2021.8 ICM Exchange manual brought forward to ICM 2027.2 and Ruby 3.4

## In three points
- **What:** A reference and Ruby migration guide that takes the October 2021 ICM Exchange manual (Version 2021.8) and reconciles it with Autodesk's current Ruby help, with the network tables, run parameters, short codes, an ICMExchange command builder and a Ruby 3.4 checker.
- **So what:** Of 335 methods in the current help, 268 match the 2021.8 manual by name, 13 were renamed and 54 appear only in the current reference; a sweep of Autodesk's 532 public example scripts found six with calls that fail under Ruby 3.4.
- **Now what:** Check your scripts before moving to ICM 2027.0, which runs Ruby 3.4.6 instead of 2.4.0. Nothing here ran inside ICM or through ICMExchange.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v2026.2", "November 2026 edition"); the date is the build session's. Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

Through the 2026 releases ICM ran scripts on an embedded Ruby 2.4.0; from 2027.0 it runs Ruby 3.4.6 and can load gems. In 2025.0 the capitalised method names (run_SQL, GIS_export, export_IDs and others) were lowercased; the old spellings still answer. The page marks each of the current help's 335 methods in 24 classes as present in both references, renamed, or only in the current one, with the reason and the source line, and adds the tables, run parameters, short codes, a command builder, a Ruby 3.4 checker with an installation check, an audit of Autodesk's example scripts, and a defect register. Tabs: Reference, Object Model, Run It, 2021 to 2026, Ruby 3.4 Check, Tables, Run Params, Short Codes, Defects, About, Doc. Scope: InfoWorks ICM through 2027.2, with InfoAsset Manager and WS Pro where the ICM help covers them.

## Results the page reports

- The 2021.8 reference holds 308 entries, 16 in classes that belong to WS Pro alone. From the 2021.8 side: 267 match by name, 13 by rename, 28 not in the current reference (267 + 13 + 28 = 308). From the current side: 268 + 13 + 54 = 335; the extra match is open, documented once on WSModelObject in 2021.8.
- Sweep: Autodesk's public example repository at commit c580601 (2026-10-20) holds 532 .rb files, 96,652 lines. Six files contain calls that fail under Ruby 3.4: four archived InfoSewer scenario-import tools and two InfoAsset scripts.

## Checks (as stated on the page)

- Both references were parsed by script; the current help's 335 methods each matched to section and line; the 2021.8 inventory from headings matched to usage lines, plus 21 headings added by hand, each with its page. The reconciliation is asserted in code.
- Removed Ruby calls and three of the defects were run on Ruby 2.4.10, 3.3.6 and 3.4.1; the messages shown are the interpreters' own.
- Each swept file got ruby -c on 2.4.10 and 3.3.6, a compile on 3.4.1, and 16 rules (version 2026.11-r2); the manifest carries each file's git blob hash.
- The checker's lexer exists in JavaScript (the page) and Python (the sweep); both were compared with views built from Ruby's own lexer, Ripper; all three gave the same 282 findings, column for column.

## What this does not show

- Nothing ran inside ICM 2027 or through ICMExchange; Ruby checks used 2.4.10, 3.3.6 and 3.4.1 (WebAssembly), not ICM's 3.4.6.
- "Only in the current reference" is a comparison of two documents, not a statement of when a method was added.
- Field names in the examples are from the 2021.8 examples and were not run inside ICM.

## How to reproduce

Open the page; Ruby 3.4 Check takes pasted scripts; findings export to CSV.

## Credits and licenses

Autodesk's 2021.8 ICM Exchange manual (supplied by Bob) and Autodesk's public innovyze/Open-Source-Support repository (MIT). No license is stated for the page.

## AI use

The page says the app and document were built with Claude, Anthropic's AI model, in a chat session in November 2026, at the request of Robert (Bob) Dickinson, who supplied the October 2021 manual, asked for a 2026 edition with a Doc tab and a Word file, and then supplied an outside review of the first version, which this revision answers point by point. Claude searched Autodesk's blog and help pages, read the public repository, wrote the Python that parsed both references and built the ledger, the rule set, the lexers and the Ripper comparison, ran the 532-file sweep, built Ruby 2.4.10 from source, ran Ruby 3.4.1 in WebAssembly, and wrote the installation check, the defect register, the app, the figures and the essay. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2026.2: answers an outside review of the first version, point by point.
- First version: the first 2026 edition, from the 2021.8 manual (its number is not given in the sections read).
