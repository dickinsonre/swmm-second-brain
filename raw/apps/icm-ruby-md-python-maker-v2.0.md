---
name: ICM Ruby MD Python Maker
file: icm-ruby-md-python-maker.html
version: "2.0"
date: 2026-10-24
written: 2026-11-18
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/K5imRonpAjeqPATTusECC7", original: "https://icm-ruby-md-python-maker.lovable.app (Lovable project icm-ruby-md-python-maker, MIT)", repo: none named in the page}
engines: none (a lexer, converter and summarizer written for the page; the Lovable app's own engines kept behind an As shipped switch)
units: not applicable
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude in October 2026 under Robert Dickinson's direction. Inside a Claude artifact its unit-test step asks Claude through the viewer's own account; elsewhere it gives a skeleton. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/K5imRonpAjeqPATTusECC7, version 1792900042-2f52 (index.html, 1,482,696 bytes, SHA-256 9509b3b909b6be2456d31587624b1682aa0010efe7448c8f7e4070a4018348c9), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file."
---

# ICM Ruby MD Python Maker: write up an InfoWorks ICM Ruby script, move it to Python, draft its tests

## In three points
- **What:** A single-file edition of Bob's Lovable app that summarizes a code file as Markdown, converts Ruby to Python, and drafts unit tests, with rebuilt engines, an ICM Script Card for InfoWorks ICM, InfoAsset Manager and WS Pro Ruby scripts, a batch mode and a Checks tab. The Lovable engines stay available unchanged behind an As shipped switch.
- **So what:** Of the 532 Ruby scripts in Innovyze/Open-Source-Support, converted and handed to Python's own parser, the shipped converter's output parses for 15 and the rebuilt one for 464. Run side by side in Ruby 3.3.6 and Python 3.13, the shipped converter matches 6 of 56 tuned programs and the rebuilt one 56.
- **Now what:** Use it to document an ICM Ruby script and get a Python starting point. No person has read the 464 converted scripts that parse or the Script Card findings, and no converted script has run inside ICM.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("v2.0 · 2026-10-24"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Tabs: Workbench, Batch, Checks, Source, About, Doc. The summarizer classifies lines by language (Ruby comments now count), counts from code only, lists dependencies per language and security notes with line numbers, with no 1,500-character cut. The converter protects strings and comments, tracks blocks on a stack, and applies a table of Ruby-to-Python rewrites for methods, blocks, operators and literals. Unit tests: inside Claude the page asks Claude through its own permission; elsewhere, Netlify included, you get a skeleton. One .zip holds every download. Samples: five scripts from Innovyze/Open-Source-Support used unchanged, pipe_report.rb written for the app, and the Lovable project's own rubyToPython.ts.

## Checks (as stated on the page)

- The Lovable project's 20 Vitest cases: the shipped engine passes 20, the new one 19; the one it fails expects output ending in an empty "else:", which is not legal Python, and the new engine writes "else:" followed by pass.
- Python's parser on 532 real scripts: 15 parse as shipped, 464 rebuilt.
- Ruby 3.3.6 and Python 3.13 run side by side on 77 programs, printed output compared byte for byte, ICM-style scripts against a fake WSApplication written once in each language: 56 of 56 tuned programs match, plus 21 programs written after tuning was finished, run once.
- Ruby's Ripper lexer on 531 scripts for the line counts.

## What this does not show

As the page lists it: no person has checked the 464 converted scripts that parse, the ICM Script Card findings, or any converted script inside ICM. A converted script that parses and matches on small programs can still differ inside ICM.

## Credits and licenses

Innovyze/Open-Source-Support scripts, MIT License, Copyright (c) 2026 Autodesk, Inc. and contributors, used unchanged; the Lovable app, MIT © 2026 Robert Dickinson.

## AI use

The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who wrote the original Lovable app, chose the task and is responsible for the result. Claude read the Lovable source, ported its engines unchanged for the As shipped mode, wrote the new lexer, converter and summarizer, the ICM Script Card checks, the test prompt and skeletons, the page, the Doc essay and the .docx, and wrote and ran every check on the Checks tab. This summary was written by Claude on 18 November 2026 from the published page.

## Changes

- 2.0 (2026-10-24): single-file edition with rebuilt engines (the version read).
- 1 (Lovable): the original app.
