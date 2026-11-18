---
name: ICM 2D Table Atlas
file: icm-2d-table-atlas.html
version: "1.1"
date: 2026-11-02
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/BaLPii9jvtEFyfz1FuKP1q", repo: none named in the page}
engines: none (a reference built from an ICM Ruby schema dump and Autodesk help pages)
data: {baseline: "Ruby schema dump pasted as text, 7,300 lines, 91 tables, 6,823 fields, 385 blob sub-fields, ICM version not recorded, SHA-256 f8c32ae888cfe6aa032924cd7721b4bb5fbec338cd2a130d1bddb8ed178bfff0", help: "ICMLive 2026 edition where it could be opened, ICM 2027 otherwise, read 2026-11-02"}
units: US customary display units, as Autodesk's help gives them
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says it was built with Claude under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/BaLPii9jvtEFyfz1FuKP1q, version 1793656582-99ad (index.html, 2,430,434 bytes, SHA-256 6db268cc014f96981a07b939c6b4423b89ec144cd3e45da28ae75a5edfa74475), its About and Doc tabs read in headless Chromium on 2026-11-17. Nothing was run to write this file."
---

# ICM 2D Table Atlas: the 21 hw_2d tables of InfoWorks ICM, field by field, with the evidence behind each row

## In three points
- **What:** A reference to the 21 hw_2d network tables of InfoWorks ICM: every field from a Ruby schema dump set beside the types, US display units, defaults, limits and meanings in Autodesk's help, each row labelled by its evidence.
- **So what:** A JavaScript and a separate Python parser agree on 91 tables, 6,823 fields and 385 blob sub-fields, and the diff of dump against help found eight names only in the help and seven only in the dump.
- **Now what:** Use it when scripting or checking ICM 2D data, and read each row's evidence label. The dump's ICM version was not recorded, and the defaults and limits copied from help pages have not been checked by a person.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("Version 1.1, November 2, 2026"). The file name above is ours. Every number below is copied from the page. Nothing was run to write this file.

## What it does

Nine lines of Ruby walk every ICM table and print every column; the run behind this atlas printed 7,300 lines. Twenty-one tables start with hw_2d: the 2D zones, boundary lines, walls, gates, starting conditions and result probes. The atlas sets the dump (exact names, order, flags) beside Autodesk's help (types, units, defaults, limits, meaning). Tabs: Atlas, Fields, Versions, Tasks, Links, Ruby (three scripts), About, Doc.

## Checks (as stated on the page)

- Parser test cases: 14 of 14 pass in the browser.
- Two independent parsers (JavaScript and Python) agree on 91 tables, 6,823 fields and 385 blob sub-fields.
- Writing the parsed schema back reproduces the 7,300-line paste line for line (Windows line endings normalized, one trailing blank ignored).
- A second reading of every help page, made to copy defaults and limits, found the same field names for 21 of 21 tables.
- Dump against help: eight names only in the help, seven only in the dump (five of those seven coordinate arrays).
- Where the page text lost empty cells, the cell was left blank and the row marked; this affects many rows on the linear structures and the infiltration surface.
- The three Ruby scripts were checked with ruby -c and run under Ruby 3.3.6 against a stub.

## What this does not show

- Which ICM version produced the dump (not recorded).
- The ICM 2026 help pages themselves could not be opened; rows name the edition used.
- Four open questions need a stamped dump from a live ICM install.
- Defaults and limits copied from help pages have not been checked by a person.

## How to reproduce

Open the page; the parser tests run in the browser. Export CSV of the fields.

## Credits and licenses

Autodesk InfoWorks ICM help (ICMLive 2026 and ICM 2027 editions). No license is stated for the page.

## AI use

The page says it was built with Claude, Anthropic's AI model, on 2 November 2026, under the direction of Robert (Bob) Dickinson, who supplied the table dump, chose the scope, asked for the update, Doc tab and Word file, and passed on an outside review of version 1.0. Claude parsed the dump and wrote the app, its parser tests, figures, Ruby scripts, the essay and the .docx; Claude research agents read Autodesk's help pages, release blogs and the ICM Ruby reference. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 1.1 (2026-11-02): corrections from an outside review of 1.0; every row evidence-labelled.
- 1.0: first version.
