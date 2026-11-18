---
title: "S333: ICM Ruby MD Python Maker, summary written from the page (v2.0)"
type: source
raw: raw/apps/icm-ruby-md-python-maker-v2.0.md
kind: app-md
author: Robert Dickinson
published: 2026-10-24
ingested: 2026-11-18
tags: [apps, icm, ruby, python, conversion]
drafted_by: Claude (Anthropic), from the published page
reviewed: 2026-11-18
---
**What it is.** A technical summary of the app ICM Ruby MD Python Maker, version 2.0: write up an InfoWorks ICM Ruby script, move it to Python, draft its tests. Raw file: [raw/apps/icm-ruby-md-python-maker-v2.0.md](../../raw/apps/icm-ruby-md-python-maker-v2.0.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 18 November 2026 at Bob's request; nothing was run to write it, and Bob has not read it (Q116). Its `written_from:` line: "the published Claude artifact https://claude.ai/artifact/K5imRonpAjeqPATTusECC7, version 1792900042-2f52 (index.html, 1,482,696 bytes, SHA-256 9509b3b909b6be2456d31587624b1682aa0010efe7448c8f7e4070a4018348c9), its About and Doc tabs and every other tab read in headless Chromium on 2026-11-18, with its CDN libraries supplied from local npm copies of the same versions. Nothing was run to write this file." Its AI-use section: "The page says: built with Claude, Anthropic's AI model, in a Claude session in October 2026 under the direction of Robert (Bob) Dickinson, who wrote the original Lovable app, chose the task and is responsible for the result."

**Claims worth keeping** (all copied from the file)
- A single-file edition of Bob's Lovable app that summarizes a code file as Markdown, converts Ruby to Python, and drafts unit tests, with rebuilt engines, an ICM Script Card for InfoWorks ICM, InfoAsset Manager and WS Pro Ruby scripts, a batch mode and a Checks tab. The Lovable engines stay available unchanged behind an As shipped switch.
- Of the 532 Ruby scripts in Innovyze/Open-Source-Support, converted and handed to Python's own parser, the shipped converter's output parses for 15 and the rebuilt one for 464. Run side by side in Ruby 3.3.6 and Python 3.13, the shipped converter matches 6 of 56 tuned programs and the rebuilt one 56.
- The Lovable project's 20 Vitest cases: the shipped engine passes 20, the new one 19; the one it fails expects output ending in an empty "else:", which is not legal Python, and the new engine writes "else:" followed by pass.
- Python's parser on 532 real scripts: 15 parse as shipped, 464 rebuilt.
- Ruby 3.3.6 and Python 3.13 run side by side on 77 programs, printed output compared byte for byte, ICM-style scripts against a fake WSApplication written once in each language: 56 of 56 tuned programs match, plus 21 programs written after tuning was finished, run once.
- Ruby's Ripper lexer on 531 scripts for the line counts.

**Limits it states.** As the page lists it: no person has checked the 464 converted scripts that parse, the ICM Script Card findings, or any converted script inside ICM. A converted script that parses and matches on small programs can still differ inside ICM.

**Checked at ingest.** Read in full; nothing was rerun at ingest. The `links:` line gives Netlify as "not yet deployed".

**Feeds:** [ICM Ruby MD Python Maker (app)](../entities/icm-ruby-md-python-maker.md), [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [Thirty-One Rubies (app)](../entities/thirty-one-rubies.md).
