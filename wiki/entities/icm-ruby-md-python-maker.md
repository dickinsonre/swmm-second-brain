---
title: "ICM Ruby MD Python Maker (app)"
type: entity
updated: 2026-11-18
sources: [S333]
tags: [apps, icm, ruby, python, conversion]
reviewed: no
---
Bob's app ICM Ruby MD Python Maker: write up an InfoWorks ICM Ruby script, move it to Python, draft its tests. Version 2.0, 2026-10-24 [S333](../sources/S333-icm-ruby-md-python-maker-summary.md). Its `links:` line names no live Netlify address [S333](../sources/S333-icm-ruby-md-python-maker-summary.md).

**A caution about its source.** The page ships no technical summary. [S333](../sources/S333-icm-ruby-md-python-maker-summary.md) was written by Claude on 18 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q116).

**What the summary says** [S333](../sources/S333-icm-ruby-md-python-maker-summary.md)
- A single-file edition of Bob's Lovable app that summarizes a code file as Markdown, converts Ruby to Python, and drafts unit tests, with rebuilt engines, an ICM Script Card for InfoWorks ICM, InfoAsset Manager and WS Pro Ruby scripts, a batch mode and a Checks tab. The Lovable engines stay available unchanged behind an As shipped switch.
- Of the 532 Ruby scripts in Innovyze/Open-Source-Support, converted and handed to Python's own parser, the shipped converter's output parses for 15 and the rebuilt one for 464. Run side by side in Ruby 3.3.6 and Python 3.13, the shipped converter matches 6 of 56 tuned programs and the rebuilt one 56.
- The Lovable project's 20 Vitest cases: the shipped engine passes 20, the new one 19; the one it fails expects output ending in an empty "else:", which is not legal Python, and the new engine writes "else:" followed by pass.
- Python's parser on 532 real scripts: 15 parse as shipped, 464 rebuilt.
- Ruby 3.3.6 and Python 3.13 run side by side on 77 programs, printed output compared byte for byte, ICM-style scripts against a fake WSApplication written once in each language: 56 of 56 tuned programs match, plus 21 programs written after tuning was finished, run once.
- Ruby's Ripper lexer on 531 scripts for the line counts.

**How to use it, as the summary puts it.** Use it to document an ICM Ruby script and get a Python starting point. No person has read the 464 converted scripts that parse or the Script Card findings, and no converted script has run inside ICM. [S333](../sources/S333-icm-ruby-md-python-maker-summary.md)

**What it does not show.** As the page lists it: no person has checked the 464 converted scripts that parse, the ICM Script Card findings, or any converted script inside ICM. A converted script that parses and matches on small programs can still differ inside ICM. [S333](../sources/S333-icm-ruby-md-python-maker-summary.md)

See [Apps summarized on 18 November 2026: ICM, InfoSewer and sanitary flow](../concepts/apps-from-pages-icm-infosewer-and-sanitary-flow.md), [ICM Ruby: UI scripts and Exchange scripts](../concepts/icm-ruby-ui-and-exchange.md), [Thirty-One Rubies (app)](thirty-one-rubies.md).
