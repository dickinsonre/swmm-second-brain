---
name: NetSTORM Explorer
file: netstorm-explorer.html
version: 1.0.0
date: 2026-11-18
author: Robert Dickinson
links: {netlify: none yet, artifact: private Claude artifact, repo: none}
engines: none (an index of a web page; no computational engine)
source_page: http://www.dynsystem.com/netstorm/ (owner: CDM Smith; read 2026-11-18)
units: not applicable
ai_use: built with Claude (Anthropic); see AI use
---

# NetSTORM Explorer: a searchable map of CDM Smith's NetSTORM web page

NetSTORM Explorer turns CDM Smith's one-page NetSTORM site into a searchable map of 79 SWMM class links in 10 categories and 138 release notes in 13 undated groups, each marked as scraped or supplied.

NetSTORM is CDM Smith's free Windows program for rainfall statistics, long-term storage and overflow accounting, and SWMM calibration reports. Its web page is one long scroll. This app read that page once, on November 18, 2026, and filed what it found into five views: a map, a link directory, a changelog, a module summary and a name index. Two separate reads of the page agreed on 79 link labels in 10 categories and on 13 release groups. They disagreed by one on the entry count, 138 against 137. The main limit is plain. The reader returned the link labels but not the addresses behind them, so 50 addresses were supplied by Claude and 29 links are search-only.

## What it does
- Presents the content of one web page, http://www.dynsystem.com/netstorm/, as structured data in five views: Map (tree), Resources (link directory), Changelog (release notes), Modules (notes by program part), Index (notes by name).
- NetSTORM is CDM Smith's free Windows program for storage-treatment-overflow modeling (after HEC-STORM), rainfall IDF analysis, time series aggregation and disaggregation, weather data import, and SWMM and MOUSE calibration reporting.
- Output: on-screen views, plus CSV and JSON export of the links and release notes.

## How it computes
- No engine and no numerical method. The app filters, counts and draws a fixed dataset embedded in the file as JSON.
- Scrape method: the page was read through a web text reader (page converted to text, then questioned), four passes: overall shape, link labels by category, version history entry by entry, and a count cross-check.
- Each page item became one short reworded index entry. Provenance letters in the app: P = read from the page; C = added by Claude from general knowledge, unverified.
- Release notes are tagged with one of 8 modules (CSReporter, IDF, STORM, Read, Transform, SWMM5 Simplification, CSInterfacer, Platform) and one of 6 kinds (Added, Changed, Fixed, Known issue, Dropped, Milestone). Tags are C.
- Import: a saved copy of the page (.html) dropped on the Resources tab is parsed with DOMParser; anchor text is normalized (lower case, parentheticals and punctuation removed) and matched exactly to the 79 labels; matched addresses replace Claude's and are marked P.

## Inputs and outputs
- Input: none required. Optional: a saved .html copy of the NetSTORM page, to restore real link addresses.
- Output: CSV of links (category, label, address, address_source, note); CSV of release notes (group, module, kind, entry); JSON of everything.
- Storage: theme choice and imported addresses in the browser's localStorage, when available.

## Data in this build
| Item | Count | Source |
|---|---|---|
| Link categories | 10 | page |
| Link labels | 79 (SWMM 8, Meteorological statistics 8, Meteorological data 11, Hydrology 9, Hydraulics 9, Guidance 6, Vendors 8, Open source 7, GIS 8, Videos 5) | page |
| Link addresses from the page | 0 | reader dropped them |
| Link addresses supplied by Claude | 50 | general knowledge, unverified |
| Search-only links | 29 | n/a |
| Release groups | 13 (entries, newest first: 2, 4, 12, 7, 12, 3, 19, 11, 11, 14, 17, 13, 13) | page |
| Release notes | 138 | page, reworded |
| Notes by module | CSReporter 36, IDF 22, STORM 18, Read 20, Transform 18, SWMM5 Simplification 6, CSInterfacer 2, Platform 16 | tags by Claude |
| Notes by kind | Added 64, Changed 43, Fixed 25, Known issue 3, Dropped 2, Milestone 1 | tags by Claude |
| Groups with a dating clue | 6 of 13 | inference by Claude |
| Index terms | 45 | chosen by Claude |

## Checks
- Mechanical, scrape: two separate reads of the page agree on 79 link labels, 10 categories and 13 release groups. Entry count: 138 (detailed read, used) vs 137 (counting read); the difference is bullet splitting on multi-bullet lines.
- Mechanical, app: 63 of 63 tests pass (headless Chromium): rendered counts equal data counts, filters, theme switch changes colour only, import of a synthetic saved page, export row counts, no console errors.
- Complexity: SWMM App Complexity Meter not run (analyzer not available to the build). Raw counts: 1634 source lines in 7 files; page script 139 functions, 186 decision points.
- Human review: none yet.

## What this does not show
1. The page's own link addresses. All 50 addresses are Claude's and unverified; 29 links are search-only.
2. Release dates or version numbers. The page gives none for the 13 groups; dating clues are inference.
3. The list of papers and reports citing NetSTORM (on a linked page, not retrieved).
4. The pages behind the older copy's footer menu (Online Help, Support, IDF Sample, Legal); not retrieved. The site's home page refuses automated readers.
5. The page's exact wording; every entry is reworded.
6. Any NetSTORM run. The STORM figure is a general sketch, not a simulation and not page content.
7. Open point from the page itself: the introduction credits NetSTORM with multi-structure STORM modeling, while the release note for the C# rewrite (group 7) says multi-structure modeling was omitted. The page does not say whether it returned.
8. A second copy of the page at http://dynsystem.com/netstorm/ (about 160 words, footer menu, note on IDF limits for unregistered users) differs from the one indexed.

## How to reproduce
1. Read http://www.dynsystem.com/netstorm/ and count the links per category and the bullets per release group.
2. Compare with the table above or with the app's Export output.
3. Rebuild: `node build.js && node test.js && node build.js` (source: data.js, essay.js, figs.js, client.js, style.css).

## Credits and licenses
- NetSTORM and its web page: CDM Smith. Contacts named on the page: Mitch Heineman, Ajay Prasad, Constantine Karos. CDM Smith had no part in this app.
- STORM method: US Army Corps of Engineers, Hydrologic Engineering Center.
- App: Robert Dickinson, SWMM Enablement.

## AI use
This app was built with Claude, Anthropic's AI model, in one session on November 18, 2026, at the request of Robert (Bob) Dickinson. He chose the page and asked for an interactive app with as much detail as possible. Responsibility for publishing it is his.

What Claude did. It read the NetSTORM page through a web text reader and wrote every index entry. It tagged each release note by module and by kind, supplied 50 web addresses and all the one-line notes from general knowledge, inferred the dating clues, and wrote the code, the figures, this essay, the .docx and the .md.

How it was checked. The checks are mechanical: two separate reads of the page for the counts, and 63 tests on the built file. No person has yet compared the entries with the page, and none of the 50 supplied addresses has been opened. NetSTORM and its web page belong to CDM Smith, which had no part in this app.

## Changes
`1.0.0 (2026-11-18)`: first build.
