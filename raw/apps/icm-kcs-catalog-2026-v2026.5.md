---
name: ICM + InfoDrainage KCS Catalog
file: icm-kcs-catalog-2026.html
version: "2026.5"
date: 2026-11-06
written: 2026-11-17
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: "https://claude.ai/artifact/RS9ketwL7qog5N3S4binNc", repo: none named in the page}
engines: none (title scoring, BM25 search test and a flow-unit converter, in JavaScript)
data:
  - {name: April 2024 Salesforce list view, records: 77, copied: 2024-04-01}
  - {name: ChatGPT's Autodesk support-article snapshot, records: 183, gathered: 2026-11-06}
units: characters; the Field Guide's flow-unit converter is not described further in the sections read
ai_use: "This summary was written by Claude (Anthropic) from the published page. The page says the audit and essay were built with Claude and the 183-article finder was added with ChatGPT (OpenAI), both under Robert Dickinson's direction. See AI use."
written_from: "the published Claude artifact https://claude.ai/artifact/RS9ketwL7qog5N3S4binNc, version 1794013526-b46e (index.html, 432,817 bytes, SHA-256 36bd97ea49403bc20fd36d4e18f76cc2575470a0a0c6e765dfa205e42c34a557), its About & sources and Doc tabs read in headless Chromium on 2026-11-17. Nothing was rerun to write this file."
---

# ICM + InfoDrainage KCS Catalog: 183 Autodesk support articles to search, plus a 77-title KCS audit

## In three points
- **What:** A finder for 183 Autodesk support articles on InfoWorks ICM and InfoDrainage, plus an audit that grades 77 April 2024 ICM article titles against five KCS title gates and proposes 2026 titles.
- **So what:** All 71 proposed titles pass all five gates and cut the mean length from 80.1 to 58.2 characters, yet on thirty seed questions the 2024 titles found the right article first 28 times and the 2026 titles 25.
- **Now what:** Use the finder and the proposals as a starting point. Keep exact error text in error titles; the finder's summaries are ChatGPT's and unchecked, and neither data set is connected to the live knowledge base.

This summary was written after the fact. The page ships no technical summary of its own. Its version and date are the page's own ("What changed in 2026.5 (6 November 2026)"). Every number below is copied from the page's About & sources tab or its Doc essay. Nothing was rerun to write this file.

## What it does

Seven tabs. Find articles searches 183 Autodesk support articles (101 InfoWorks ICM, 82 InfoDrainage) by product and topic, with saved articles, notes, review states and exports. 2024 archive shows the April 2024 list of 77 articles. Review shows each title three ways where evidence exists (2024, Autodesk's current title, a proposed 2026 title you can edit) with a row of states: title-style grade, content match, workflow (current or legacy), error text preserved, and your decision. Search test ranks titles for support questions with BM25. Field Guide holds the rules, sixteen rule tests and a flow-unit converter. About & sources and Doc.

## How it computes

- Five gates from the KCS field guide Bob supplied: (1) length, 69 characters at most ("fewer than 70"); (2) names ICM; (3) one of three patterns (exact error message, How to, plain problem statement); (4) a How-to title must name something the reader can do; (5) clean: no typo, repeat, trailing period or question without a question mark ("How do I..." counts as a question).
- Grade: all five A, four B, three C, two or fewer D. Gates 1 to 4 are code that runs in the browser; gate 5 is part code, part reading. The proposals are judgment.
- Parser: the April 2024 list arrives as blocks of eight or nine lines; a published article carries a published date and a created date, a draft only a created date. Result: 66 published, 10 drafts (5 not validated), 1 archived duplicate.
- Naming: proposals use ICM and the ICM SWMM shorthand, because spelling out InfoWorks ICM pushes 37 of the 71 proposals to 70 characters or more.

## Results the page reports

- April 2024 titles: 38 of 77 were 70 characters or longer; the longest 153; 45 began "How to Understand". Gate failures: length 38, product 2, pattern 16, action 45. Grades: A 5, B 35, C 25, D 12.
- 71 proposals, all passing all five gates. Over the 76 non-archived records, mean length 80.1 to 58.2 characters; over the 71 rewritten, 81.6 to 58.1; longest proposal 69. Twenty proposals were revised after meaning flags.
- Search test, thirty seed questions, BM25 over 76 titles: right article first 25 times with 2026 titles, 28 with 2024 titles; within the top three, 29 against 30. The worst case was the error "[RAINGAGES] or [TIMESERIES] should not be empty", whose 2026 title had cut the error words.
- Live pages read by hand: the import Overview and Step 5 (2 and 6 November 2026) and Step 8 (6 November), all carrying a legacy notice; Step 8's live title is "Importing InfoSewer to InfoWorks ICM - Step 8: Import Wet Well Hydraulics". No live page was found for Steps 1, 2, 3, 4, 6, 7 or 9.
- Finder snapshot: 16 searches through Autodesk Product Help; 10 articles carry a legacy flag, all in the InfoSewer import series; four titles were checked against fetched pages and all four match.

## Checks (as stated on the page)

- Sixteen rule tests in the Field Guide; the gates' code is the same code the browser runs on an edited title.
- An outside review (written with ChatGPT, per its markup) recomputed every length in version 1.0's appendix and found all 77 right, then found four grade errors, which were confirmed in the code; a fifth fault was found and fixed in 2026.2.
- 2026.5 fixed the question test flagging "Where to find..." titles; no audit grade changed.

## What this does not show

- Article bodies, and whether the 183 summaries match their articles (summaries, topics, purposes and tags are ChatGPT's reading; none was checked).
- The full Autodesk index: the finder is a snapshot with no live connection.
- Views since April 2024: view counts are the April 2024 numbers.
- The search test's questions were written by the same AI that wrote the proposals, and it searches titles only.
- The KCS field guide carries no date; the page reads it as Autodesk's internal standard because it mentions the AKN, Salesforce and Jira.

## How to reproduce

Open the page. Find articles and Review work on the embedded data; Search test reruns BM25 on the seed questions; editing a proposed title reruns the gates. Export CSV, Export JSON and Backup notes also show the text to copy.

## Credits and licenses

Titles and links of the 183 articles are Autodesk's. The April 2024 list is from Autodesk's Salesforce knowledge base, supplied by Bob. No license is stated in the page.

## AI use

The page says the app and its essay were built with Claude, Anthropic's AI model, on 2 November 2026 and refreshed on 6 November, under the direction of Robert (Bob) Dickinson, who supplied the April 2024 list, the KCS field guidance, the request to bring the 2024 review up to 2026, and the outside review. Claude parsed the list, turned the guidance into five gates, sorted the articles into seven categories, wrote all 71 proposals, the rule tests and the thirty seed questions, built the app and wrote the essay; the 2024 review it corrects was also Claude's. Version 2026.4 (the 183-article finder) was built with ChatGPT (OpenAI); 2026.5 brought it into this app's source. This summary was written by Claude on 17 November 2026 from the published page.

## Changes

- 2026.5 (2026-11-06): the finder brought into this app's source and checked; question test fixed; exports also show text to copy; two rule tests added, sixteen in all.
- 2026.4 (2026-11-06, ChatGPT): Find articles tab with 183 articles.
- 2026.3 (2026-11-06): live pages re-checked; Step 8 verified.
- 2026.2: fixes from the outside review; title-style grade separated from other states; Search test tab and fourteen rule tests.
