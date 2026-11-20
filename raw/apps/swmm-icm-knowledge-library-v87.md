---
name: SWMM & ICM Knowledge Library
file: swmm-icm-knowledge-library.html
version: artifact v87
date: 2026-11-20
author: Robert Dickinson
links: {artifact: https://claude.ai/artifact/DnRTUhUVgV2dU4YJipzV95 (private), original: https://newsletter-gallery-robertdickinson.replit.app/, repo: none}
engines: none (a content library; it runs no simulation engine)
units: not applicable
ai_use: rebuilt and maintained with Claude (Anthropic); see AI use
---

# SWMM & ICM Knowledge Library: one searchable page of Robert Dickinson's SWMM, ICM and SWMM6 work since 1973

**In one sentence.** This page is a one-file catalog of 10,151 records of Robert Dickinson's SWMM and ICM work, and its search and related-item arithmetic match the original Replit app in all 229 related-item and 30 ranking comparisons.

**In one paragraph.** The library gathers 66 newsletter editions, 163 LinkedIn articles, 1,327 swmm5.org posts, 454 app entries, 243 GitHub repositories, Robert's LinkedIn comments and his OpenSWMM.org threads into one HTML file of about 9.1 megabytes that needs no server. Search scores every record by its words, and each card offers related items chosen by the words they share, with rare words counting for more. The copy was checked by running the original Replit code and the page's code on the same data: 229 of 229 related-item lists, 30 of 30 rankings and 4,032 of 4,032 search scores agreed. Every newsletter and article date was read from LinkedIn. The main limit is freshness: most links are only as good as the export they came from.

**What is unique.**
- The contents. It holds one SWMM developer's public record in one file: newsletters, articles, posts, blogs, apps, repositories, papers, comments and forum threads. 7,277 of the 10,151 records (72 percent) are his 4,398 LinkedIn comments and 2,879 OpenSWMM.org threads, the places where he answers other people. A list of publications would leave those out.
- The proof. The copy is tested against the program it copies. The Replit code and this page ran on the same data and agreed on 229 of 229 related-item lists, 30 of 30 rankings and 4,032 of 4,032 search scores, and the test found a fault in the original.
- Not unique. A searchable list of links is an old idea. Counting rare words for more is textbook retrieval, from Karen Spärck Jones in 1972. One-file pages and AI assistants on a catalog are common now.

## What it does
A single HTML file that holds Robert Dickinson's published work on SWMM3 through SWMM6, InfoWorks ICM, InfoSWMM, InfoSewer and XPSWMM: newsletter editions, LinkedIn articles, posts and reposts, apps, tools, GitHub repositories, gists, blog posts, papers, OpenSWMM.org threads and LinkedIn comments. It answers "has Robert written or built something on X, and where is it?" for engineers and for AI tools. It runs offline from one file; links lead to the original sources. It is a copy of his Replit app (NewsletterGallery), extended.

Related: the SWMM second brain, https://github.com/dickinsonre/swmm-second-brain, an AI-kept wiki compiled from Robert's published writing and apps. Attach it to a Claude session and ask it a question; the library links to it rather than copying it.

## Contents (this build)
| Collection | Records | Notes |
|---|---:|---|
| Newsletter editions | 66 | 66 dates read from their LinkedIn pages |
| LinkedIn articles | 163 | 163 distinct articles; 163 dates read from LinkedIn; 38 added from LinkedIn's list, not yet summarized |
| LinkedIn posts | 74 | the date field holds the year (74 of them); the Timeline dates them by the ID in the link |
| Reposts | 97 | LinkedIn reshares with Robert's comment; dated by the ID in the link |
| Documents | 20 |  |
| App entries | 454 | 15 featured, the rest gallery entries (Replit 85, Lovable 5, Netlify 349) |
| Tools | 45 | each labeled code excerpt, usage example or outline |
| GitHub repositories | 243 | five organizations; dates are last updates, not creation |
| Gists | 64 |  |
| Blog posts (Blogspot) | 145 |  |
| swmm5.org posts | 1,327 |  |
| Open-Source SWMM group posts | 22 |  |

Total records counted by the build: 10,151.

## How it computes
- **Data.** Records are extracted from the Replit app's TypeScript export (`client/src/lib/data.ts` and `data-content/*.json`) into one embedded JSON block. Entries added after the export are written into the same data file first, so the page and the source never disagree.
- **Search.** `searchAll(query)` tokenizes the query and scores every record in every collection on title, description, categories and keywords, the scoring ported from the Replit server. Results sort by score; the panel shows up to 100. A featured app also matches the name it was published under.
- **Related content and catalog ranking.** Ported from the Replit code and checked against it (see Checks).
- **Topics.** Each record keeps its original categories. Title rules add derived topics (for example Quiz, Ruby, SQL) shown with a dashed tag, kept separate so the original tags are never altered.
- **Tool labels.** Each tool card states what its preview holds: a code excerpt, a usage example that calls a library it does not include, or an outline. None is labeled a working tool.
- **Timeline.** Every dated record, newest first, each with the source of its date: a LinkedIn page that was read, the ID inside a LinkedIn link (`id >> 22` gives milliseconds since 1970), a blog post's URL, or a year only. 5 suggested connections between works are listed for confirmation.
- **Robert's workspace.** Dated notes, corrections, pins and revisit flags on any record, stored in this browser only (localStorage key `rd-record-notes-v1`), with export to a file.

## Inputs and outputs
- Reads: nothing at run time; all data is embedded. Optional: the research assistant calls Claude through the artifact runtime when that capability is available.
- Writes: CSV per tab, an animated GIF of the page, the Doc as .docx, this .md, and an export of workspace notes.

## Checks
Mechanical, on this build:
- Parity: the page's search, related-content and catalog functions, run on this build's data, give the same results as the original Replit code on the same data: identical. Record counts equal between source and page: yes.
- Search by exact name: 2,797 of 2,797 titled records came back when their exact title or repository name was searched; the lowest rank among them was 10.
- Dates: 66 of 66 newsletter dates and 163 of 163 article dates were read from LinkedIn on 10 Nov 2026 (rendered pages for newsletters; each article page's publish timestamp, matching the rendered date in every spot check).
- Topics: the Quiz topic on the Newsletters tab finds 2 editions; Ruby finds 19 (3 by original tag).
- Timeline renders 9,550 dated items with 5 connections. A workspace note saved, pinned and survived a reload.
- Phone width 390 px: page width 390 px, no sideways scroll. Light mode applies. Page errors in all test runs: 0.
- Complexity, on the SWMM App Complexity Meter's scale (HydroCouple organization = 100), measured with its analyzer meter-core.js 1.7.0 and baseline HC-2026-11-10-h on the 44 hand-written source files (page code plus build and test scripts; data, images and outside libraries left out): index 57.8; Size 58.9, Structure 70.2, Test evidence 0.0, SWMM vocabulary 53.2. The Doc's last section gives the counts.

Human review: none recorded for this build beyond Robert's own use of the page.

## What this does not show
1. Most summaries came from the Replit build and are AI-written; 38 articles added in Nov 2026 carry only their opening lines.
2. Links other than newsletter and article links have not been re-checked by a person; some may have moved.
3. Post and repost dates come from the ID in the LinkedIn link (when LinkedIn created the item), not from a date read off the page.
4. Repository and gist dates are last updates, not creation dates.
5. The 5 Timeline connections are suggestions from titles and names, not confirmed by Robert.
6. Workspace notes stay in the browser where they were written; they do not sync between devices or viewers.
7. Search finds words, not meaning; a record that never names a term will not match it.

## How to reproduce
From the build folder: `node extract.mjs <source> build/data.json`, `node build.mjs`, `node parity.mjs`, `node doc.mjs`, `node build.mjs`, then `node smoke.mjs`, `node check3.mjs` and `node gpt-check.mjs` (Playwright, Chromium). `build/verify.json` and `build/gpt-check.out` hold the numbers above. Then `node appmd.mjs` writes this file and a last `node build.mjs` embeds it.

## Credits and licenses
- Content and the original Replit app: Robert Dickinson. No license is stated for the content; ask before reuse.
- People named in records keep credit in those records (for example Caleb Buahin and Corinne Wiesner-Friedman for SWMM6/HydroCouple).
- Libraries loaded by the page: html2canvas 1.4.1 (MIT), gif.js 0.2.0 (MIT). Fonts: Playfair Display and Inter (SIL Open Font License), from Google Fonts.

## AI use
This one-file copy was built with Claude, Anthropic's AI model, under the direction of Robert (Bob) Dickinson, who built the original Replit app and supplied its source export and images. Claude extracted the records, rewrote the app as one HTML file, ported search, related content and catalog ranking, replaced the server's gpt-4o assistant with Claude, added the dark theme, exports, Doc tab and this file, and adds each LinkedIn item Robert sends after reading it in his browser. In Nov 2026 it read newsletter and article dates and links from LinkedIn, added 38 missing articles and the first newsletter issue, merged 37 articles listed twice, and added full-catalog search, title-rule topics, tool labels, the Timeline and record notes. Summaries of added items are Claude's. The About tab holds the full dated log. Responsibility for the library is Robert's.

## Changes
- v87 (2026-11-20): added a post (asking Gemini for the best source of SWMM6 information; it named the Australian Water School's Diving into Open-Source SWMM) and a repost (Toby Stoff's Manhole Force Workbench: manhole losses and forces from physics).
- v86 (2026-11-19): Netlify gallery checked against the account again: Walk the Mesh back at walk-the-swmm6-2d-mesh, and gilded-lamington-31be10 renamed swmm5-swmm6-options-updater; 349 apps in Netlify order.
- v85 (2026-11-19): added a post (an 80-second mograph of Mel Meng's InfoWorks ICM Ruby script finder).
- v84 (2026-11-19): added a repost (Mel Meng's AI-built search app for the InfoWorks ICM script library in Autodesk Water's Open Source Support repo).
- v83 (2026-11-19): Netlify gallery checked against the account again: added Mesh Bridge (pyramids-mesh formats into SWMM6 2D input) and the EXTRAN Features Upgrader at its new Netlify-assigned address; removed 6 sites deleted from the account (walk-the-mesh and five duplicates); the surviving copies of the duplicates now carry the descriptions; 348 apps in Netlify order.
- v82 (2026-11-18): added a repost (Mostafa Farrag on the pyramids plugin ecosystem: mesh, Earth observation, city models, point clouds); synced the Netlify gallery to the Nov 18 project grades spreadsheet: 72 apps added, 15 corrected addresses, inside-swmm (deleted) and four now-private sites removed; 352 apps in Netlify order.
- v81 (2026-11-18): added one Netlify app (FV Link Lab: swmm524-fvlink, finite volume on chosen conduits beside stock EPA SWMM 5.2.4).
- v80 (2026-11-18): added one Netlify app (Modeling Confluence Mograph), found by checking the Netlify account against the library.
- v79 (2026-11-18): added a repost (Ruth Ayn Hocker's call for abstracts for EWRI's Modeling Confluence Conference).
- v78 (2026-11-18): added a repost (William Katzenmeyer on Terrio, a pure-Rust replacement for GDAL in many workflows).
- v77 (2026-11-17): added 97 Netlify apps (73 published 17 Nov and 24 older ones), each described from its live page; 10 empty Netlify projects left out and one deleted site removed; the Netlify list follows the account's order.
- v76 (2026-11-17): added 14 Netlify apps (the 12 published 17 Nov, SWMM Second Brain and SWMM5 Walks Downhill), descriptions written from each live page; the Netlify list now follows the account's order; Robert's 2026 photo is now the page's picture of him, with the 1981 portrait kept in About.
- v75 (2026-11-16): added a repost (Mikki Seidenschnur-Lund on the Flow Systems Ontology, with Robert's note on a neutral object set for SWMM5, SWMM6 and ICM).
- v74 (2026-11-16): added a post (the SWMM 1 engine mograph, a 60-second film about the 1971 program rebuilt from paper).
- v73 (2026-11-16): the Doc, its .docx and this summary open with what is unique about the library (and what is not); added a repost (Fatemeh Arab Sadeghabadi's GEV vs MEVD tool for a 200-year rainfall from 30 years of data).
- v72 (2026-11-16): the Doc and .docx open with the essay in one sentence, one paragraph and one page (one figure), four questions answered at the end, a one-line lead under every section, and a closing complexity box measured with the Complexity Meter's analyzer; this summary carries the first two sizes and the complexity line; a dated copy goes to the second brain's raw/apps.
- v71 (2026-11-16): added a repost (Aparajit Koirala's HydroBOA Assistant, offline multi-engine modeling on a phone).
- v70 (2026-11-14): a one-line link to the SWMM second brain under the title on the home page.
- v69 (2026-11-14): GitHub repositories updated from all five organizations: swmm5-r, swmm5-infosewer and swmm6-r added; 8 language ports filled in (swmm5-hy, swmm5-mojo, swmm6-fsharp, swmm6-javascript, swmm6-groovy, swmm6-kotlin, swmm6-hy, swmm6-ruby); swmm6-rust and swmm5-cplus updated; 12 dates refreshed.
- v68 (2026-11-14): added the swmm-second-brain repository (Karpathy-style LLM wiki of Robert's SWMM and ICM writing).
- v67 (2026-11-13): added a repost (Sofia Lazar's Saudi Wadi Pulse, wadi flows and sediment).
- v66 (2026-11-13): added a post (Robert's early history with SWMM and his wife's part in it).
- v65 (2026-11-12): added a post (documentation features in Robert's Claude apps, shown on a CFD vs SWMM5 app).
- v64 (2026-11-11): Netlify gallery updated from the 50 newest dashboard projects: added Bob Usefulness Index and Next-Generation SWMM Day in Motion; EXTRAN III Workbench and the online library moved to the top; three descriptions written from the live pages.
- v63 (2026-11-11): added a repost (Xilin Xia's preprint on catchment-scale hydrological laws, shared by Nigel Wright).
- v62 (2026-11-11): added a repost (Vida Atashi and Reza Barati, reverse flood routing) and a post (sharing apps with humans and AIs); merged 37 articles listed twice, so 163 article records match the 163 on LinkedIn; added this technical summary (embedded, linked in the head and the About tab).
- v61 (2026-11-10): newsletter and article dates and links read from LinkedIn; first issue and 38 articles added; search over every collection; title-rule topics; tool labels; Timeline tab; Robert's workspace notes.
