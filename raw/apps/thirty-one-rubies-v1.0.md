---
name: Thirty-One Rubies
file: thirty-one-rubies.html
version: "1.0"
date: 2026-11-03
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/TYfiMHPdPQRzDEReWUte7y", repo: none named in the page}
engines:
  - {name: CRuby, version: 3.4.1, note: "compiled to WebAssembly, running 44 scripts against a stand-in for the ICM Ruby API"}
data: {icm_api_rules: "Autodesk Open-Source-Support repository (MIT): 136 tables and 2,644 fields in hw_parameters.rb and sw_parameters.rb, 336 methods in ruby_icm_help.md"}
units: US customary (the made-up demo network)
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the app was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/TYfiMHPdPQRzDEReWUte7y, version 1793713065-d89a (index.html, 13,221,055 bytes, SHA-256 f800fac92e697d1ef57d6d1e2010585e643b70b476e1c91650718ff9e6c4fcde), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file; the date is the artifact's publish date."
---

# Thirty-One Rubies: 31 ICM Ruby apps on one real Ruby interpreter in the browser

## In three points
- **What:** One file that runs 44 ICM Ruby scripts from 31 of Bob's apps on CRuby 3.4.1 compiled to WebAssembly, against a strict stand-in for the ICM Ruby API built from Autodesk's public table, field and method lists.
- **So what:** All 43 compared scripts gave character-for-character identical output on native Ruby 3.3.6 and browser Ruby 3.4.1, and a volume check caught an RTK script reading 24.0000 ac-in where 6.0000 was right.
- **Now what:** Use it to check that a script parses, runs and names real tables and fields before you open ICM. No script has run in real ICM, and Ruby 2.4.0 (ICM before 2027.0) was not tested.

This summary was written after the fact. The page ships no technical summary of its own. Its version is the page's own ("v1.0"); the date is the artifact's. The file name above is ours. Every number below is copied from the page's About tab or its Doc essay. Nothing was run to write this file.

## What it does

The 31 apps from Bob's archive review each carried Ruby written for InfoWorks ICM, which a browser cannot reach. A June chat said ICM Ruby cannot run in a browser; Ruby can, and what it lacks is ICM, so the page builds a stand-in that is as strict as possible. Press Run and a real interpreter executes the script against a made-up sewer network, writes CSV files into an in-memory scratch folder, and the page draws them; the same text can be copied into ICM. ICM 2027.0 and later run Ruby 3.4.6. Tabs: Map, Workbench, Alongside (16), About Ruby (8), Ports (7), Register, About, Doc.

## Checks (as stated on the page)

- Every one of the 44 scripts ran under native Ruby 3.3.6 and Ruby 3.4.1 in headless Chromium; all 43 compared runs matched character for character (the Set timing script was left out because its output is a stopwatch). The comparison first showed 37 of 43; most of the gap was JavaScript rewriting 500.0 as 500, so the page now passes the network as raw text.
- The checker passes all 44 scripts with no hard flags; table and field rules come from Autodesk's lists.
- The stand-in's refusals were tested: a wrong field, a wrong table, map on a custom collection, an undocumented method, a real method it does not implement, and a change without .write.
- Hand checks: Harmon at 1 MGD and 100 gpcd gives 2.955; RTK volume 6.0000 ac-in against R x rain x area (the first run read 24.0000, four times high, because a Delta-t was missing from the convolution).
- Both themes and phone width, no console errors.

## What this does not show

- That any script works in real ICM: none has run there. A pass means the Ruby runs and the names are on Autodesk's lists.
- That a script runs on Ruby 2.4.0, for ICM before 2027.0.
- Bob has not yet reviewed the 46 corrections, and the Federov choice is his to make (as the About tab puts it).

## How to reproduce

Open the page, pick a script on Workbench and press Run; "Check this build" on the About tab runs every script. The page is about 13 MB.

## Credits and licenses

CRuby 3.4.1, compiled to WebAssembly. The stand-in's rules come from Autodesk's public Open-Source-Support repository, MIT. No license is stated for the page.

## AI use

The page says the app was built with Claude, Anthropic's AI model, in a Claude session in November 2026, under the direction of Robert (Bob) Dickinson, who chose the 31 apps and asked for the combination. Claude read the past chats for the 31 apps with three delegated readers, and wrote the mock, the checker, all 44 scripts, the demo network and inputs, the page, its charts and the Doc essay. Many scripts are new or heavily rewritten, not copies of the originals. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.0: first version.
