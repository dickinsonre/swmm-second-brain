---
name: Bob Usefulness Index
file: bob-usefulness-index.html
version: 2.2
date: 2026-11-11
author: Robert Dickinson
links: {artifact: private Claude artifact, v1: https://bob-usefulness-index.dickinsonre.chatgpt.site/, evidence: https://claude.ai/artifact/DnRTUhUVgV2dU4YJipzV95 (private), repo: none}
engines: none (a scorecard; it runs no simulation engine)
units: not applicable (points, 0 to 100)
ai_use: baseline scores, evidence lines and the page were written by Claude (Anthropic); see AI use
---

# Bob Usefulness Index: a 100-point scorecard for Robert Dickinson's usefulness to water modelers, scored against the record in his Knowledge Library

## What it does
Answers one question: did someone become better able to model, decide, learn or help because of what Robert shared? Four pillars, five criteria each, every criterion scored 0 to 5, total 0 to 100. Version 2.2 replaces the v1.0 example score (92, no evidence) with a baseline of 66 read criterion by criterion from the SWMM & ICM Knowledge Library (v63, 11 Nov 2026, 9,955 records). Each criterion carries an evidence line (what the library records) and a gap line (what would raise it). Robert edits the scores and lines, saves dated reviews, and compares them over time.

## How it computes
- Rubric per criterion: 0 no contribution yet; 1 a useful start; 2 delivered; 3 in service; 4 confirmed useful; 5 lasting or repeatable value.
- Claimed index: BUI = sum of the 20 criterion scores s, each 0 to 5. Pillar score = sum of its 5 criteria, 0 to 25. Equal weights.
- Evidenced index: E = sum of e, where e = s if the criterion's evidence line is not empty, else min(s, 2). A score above 2 with no evidence line is shown as a claim.
- Next step: the 20 criteria are sorted by score, then by pillar score, then by card order; the lowest three are shown with their gap lines.
- Baseline: 16 + 16 + 16 + 18 = 66 (Solve, Reuse, Teach, Help). v1.0 example: 23 + 22 + 23 + 24 = 92.
- State: one JSON object (schema bob-usefulness-index, version 2) in localStorage key bob-usefulness-index-v2: mode, label, values[4][5], ev[4][5], notes[4], links[4], reviews[].

## Baseline scores and their evidence

### Solve real modeling problems: 16 of 25

| Criterion | Score | Evidence on file | To raise it |
|---|---:|---|---|
| Validate the result | 3 | Model Testing is one of the library’s standing topics, so checks have been published more than once. | The count of records under that topic was not read for this index, and nothing on file shows a check someone else relied on. Add a “checked against” note to ten records in Robert’s workspace: the engine, the version, the model, the number. |
| Unblock a modeler | 4 | 2,744 threads answered and 135 started on openswmm.org, February 1995 to 2026, with 291 in the peak year, 2019. A 1981 Florida thesis thanks him by name for pulling its author out of trouble. | The thread list holds dates, titles and names, not what was written or whether the fix worked. Open one thread for each of the 25 problems and record whether the asker confirmed it. |
| Make the next step practical | 3 | 45 tools, 18 reusable code components and 4 learning paths. A 25-problem filter covers the forum threads; 2,190 of 2,879 titles carry a problem tag. | Every tool card is labeled a code excerpt, a usage example or an outline. None is labeled a working tool. Promote three to working tools, each with an input file and its expected output, and note one person who ran one. |
| Explain uncertainty | 3 | The library lists 7 things it does not show. Paper records say Checked or Not checked, every Timeline date names its source, and tool cards say excerpt, example or outline. | The limits describe the library, not the articles and posts inside it. Add a “when this fails” line to five articles and ask one reader whether it changed what they did. |
| Follow through | 3 | 670 of 4,398 LinkedIn comments are replies inside a thread, so he came back to the conversation. A review of 10 Nov 2026 was acted on by 11 Nov and the fixes were re-checked: 66 newsletter dates, 163 article dates, 15 broken links and 37 duplicate articles. | No record shows a forum answer confirmed by the person who asked. Follow up on five 2026 threads and note what happened. |

### Build things others can use: 16 of 25

| Criterion | Score | Evidence on file | To raise it |
|---|---:|---|---|
| Provide a working example | 3 | 276 app entries (171 on Netlify, 85 on Replit, 5 on Lovable, 15 featured), 239 GitHub repositories and 64 gists. | 15 SWMMBobSWMM6 repositories were still empty on 9 Nov 2026 (3 SWMM5 ports and 12 OpenSWMM 6), and no run, download, star or fork counts were read for this index. One note from a person who ran an app or script makes this a 4. |
| Make it reproducible | 2 | Repository descriptions were written from their READMEs, and the library lists its own rebuild commands. | No tool or app record carries inputs, versions and expected outputs. Start with three Ruby scripts: a small model, the command, the numbers that should come out. |
| Explain how to use it | 3 | A Doc essay with 12 operating steps and 11 figures, 4 learning paths, 66 newsletter editions and 163 LinkedIn articles. The Ruby topic alone finds 19 editions. | Most summaries are AI-written and 38 articles carry only their opening lines. Summarize the 38, then ask one modeler to follow an edition cold and say where they got stuck. |
| Make it findable | 4 | One searchable file: 9,955 records, 2,954 distinct links, 19 tabs. An outside review found that search could not find a repository by its exact name. After the fix, 2,601 of 2,601 titled records came back when searched by exact name. | The library is a private artifact with no repository and no stated license, and links other than newsletter and article links have not been re-checked. Publish it, state a license, run the link check. |
| Keep it useful | 4 | The library was updated on 11 separate days between 24 Oct and 11 Nov 2026 and stands at v63. The deductions in the review of 10 Nov were worked within a day and re-checked. | swmm5.org shows 19 posts so far in 2026 against 46 in 2025. Put each new app on swmm5.org as it ships. |

### Make difficult ideas clear: 16 of 25

| Criterion | Score | Evidence on file | To raise it |
|---|---:|---|---|
| Explain the mechanism | 5 | 68 publications from 1980 to 2025, among them the SWMM III and SWMM 4 user’s manuals and the EXTRAN addendum. 6 papers by other people cite them. 1,327 swmm5.org posts since 2009. | Hold it. 29 of the 77 paper records are not yet confirmed at source. |
| Let someone try it | 3 | 276 app entries, 30 quiz questions and 4 learning paths. | No record of anyone finishing a path or a quiz; the quiz high score stays in one browser. Two learners who run a path and report back make this a 4. |
| Give context and limits | 3 | Newsletters and articles are grouped by level, each record keeps its topic tags, and the library states what it does not show. | Individual posts rarely say when a method stops applying. Add that line to five articles. |
| Make the idea understandable | 3 | 139 cover images, a Doc essay with 11 figures and 163 dated articles. | Most summaries are AI-written and no person has reviewed them. Review the summaries of the 66 newsletter editions and record one reader’s reaction. |
| Check understanding | 2 | A 30-question quiz exists. The one outside review on file, 80 out of 100 from ChatGPT, graded the library, not a learner. | No reader or learner feedback is recorded anywhere in the library. Ask three readers what they did after reading one edition, and write it down. |

### Help people move forward: 18 of 25

| Criterion | Score | Evidence on file | To raise it |
|---|---:|---|---|
| Give direct help | 5 | 4,398 LinkedIn comments on other people’s posts since September 2016 and 2,744 forum answers since 1995. With the 135 threads he started, they are 73 percent of the library’s records. | Hold it. The record shows the answers, not the outcomes. |
| Connect useful people or resources | 3 | 88 reposts of other people’s work, each with a comment, 22 Open-Source SWMM group posts kept, and 2,954 distinct links. | No record of an introduction that led somewhere. Note one in the workspace when it happens. |
| Share credit | 3 | Records keep credit for the people named in them, Caleb Buahin and Corinne Wiesner-Friedman among them. Thread partners are counted by name: Lew Rossman 213, Mitchell Heineman 201, Michael Gregory 187. Google Scholar is linked as searches so that another Robert Dickinson’s citations are not borrowed. | The content carries no license, so others cannot reuse it with credit. State one, and note one case where a credited person’s work was found through the library. |
| Listen and improve | 4 | ChatGPT reviewed the library on 10 Nov 2026 and gave it 80 out of 100. Four of its five deductions have a recorded fix: the dates, exact-name search, the Quiz topic and the tool labels. | The fifth deduction, a summary looser than its edition, has no recorded fix. And one AI review is not a reader. Ask a person. |
| Build independence | 3 | 4 learning paths, 30 quiz questions and a problem filter that lets a modeler find an old answer alone. | No record of someone solving the next problem without help. Ask the next person you help what they can now do alone. |

## Inputs and outputs
- Reads: nothing at run time; the baseline is embedded. Optional: a JSON backup (v1.0 or v2.0 schema) through Import backup. A v1.0 backup gains empty evidence lines; its saved reviews keep their totals.
- Writes: a JSON backup, a scorecard SVG, this .md. In the Claude artifact viewer these go through the viewer's downloads capability; elsewhere through a normal download.

## Checks
Mechanical, on this build (verify.mjs, check.mjs):
- Sum: the 20 baseline scores add to 66; pillars 16, 16, 16, 18.
- Records: 18 collection counts (7,277 + 1,901 + 642 + 110) plus 25 problem definitions add to 9,955, the library's own total. Answers are 73.1 percent of records, shown as 73.
- Blog: 18 yearly counts plus 1 undated post add to 1,327.
- Chart numbers: 61 of 61 numbers in the three library charts were found in the library's Doc text.
- Line numbers: the 40 evidence and gap lines hold 58 distinct numbers; 57 were found in the library's Doc text. Of the 28 with three or more digits, 27 were found. Not found by machine: 2,601 (read from the library's technical summary, section Checks, and typed in).
- Page: opened in headless Chromium at 1,360 px and 375 px wide. 6 of 6 tabs render, console errors: 0, sideways scroll at 375 px: none. The score reads 66 in the dark theme and 66 in the light theme.
- Behaviour: raising one slider by 1 raised the total by 1; clearing one evidence line on a score of 5 dropped the evidenced total by 3; Reset returned 66; a saved review survived a reload.
- Old backups: a v1.0 backup with 1 saved review imported and kept its total of 92.
- Colour: the dark-mode contrast gate passed 34 checks with 0 below target; lowest pair 3.26:1 (faint labels on card (light)).

Read from the library and typed in, small numbers the matcher cannot distinguish from coincidence: 11 update days (counted from the dated AI-use log, 24 Oct to 11 Nov 2026); 15 empty repositories (3 + 12, AI-use log entries of 8 and 9 Nov); 12 operating steps and 11 figures (counted in the Doc essay); 19 Ruby editions and 7 limits (technical summary); 29 unconfirmed paper records (77 - 48); four of five review deductions with a recorded fix (Doc essay, "A second reader's report card").

Human review: Robert set the meaning of level 3. He has not yet reviewed the 20 scores or the 40 lines.

## What this does not show
1. The 20 baseline scores are Claude's reading of the rubric against the library's summary of itself. Another reader could move several by one level.
2. Claude read the library's Doc essay, technical summary (.md) and build stamp. It did not read the 9,955 individual records; that data block exceeded what its artifact-reading tool serves.
3. Library counts measure activity, not outcome. 2,744 forum answers is not a count of problems solved.
4. Level 3 is easy on purpose (changed in 2.1 at Robert's direction): it counts volume and upkeep, not use. Evidence that the work helped someone starts at level 4.
5. Equal pillar weights are a choice carried over from v1.0, not a finding.
6. No peer comparison or ranking.
7. Drafts and reviews stay in one browser unless exported.
8. The evidence is a snapshot of the library at v63; it does not update itself. The 25-problem ranking was made in a separate Claude chat on 6 Nov 2026 and is carried as the library reports it.
9. The evidenced total checks that an evidence line exists, not that it is true.

## How to reproduce
From the build folder: `node verify.mjs <library Doc text>`, `node build.mjs`, `node check.mjs`, `node build.mjs` (embeds the page-check numbers), `node doc.mjs`. `build/verify.json` and `build/page-check.json` hold the numbers above. Sources: `src/data.mjs` (facts, scores, lines), `src/figs.mjs` (10 figures), `src/essay.mjs` (the Doc essay), `src/template.html` (the page).

## Credits and licenses
- Framework (four pillars, 20 criteria, 0 to 5 rubric, equal weights, review history): Bob Usefulness Index v1.0, made for Robert Dickinson on a ChatGPT site.
- Evidence: SWMM & ICM Knowledge Library, Robert Dickinson. People named in its records keep credit there, among them Caleb Buahin and Corinne Wiesner-Friedman (SWMM6, HydroCouple), Lew Rossman, Mitchell Heineman, Michael Gregory, Bill James and Wayne Huber.
- Switchboard text: supplied by Robert Dickinson; its source was not stated. The diagram is a metaphor and makes no physiological claim.
- No external libraries or fonts are loaded. No license is stated for the content; ask Robert before reuse.

## AI use
Version 1.0 of this index was published from a ChatGPT site (bob-usefulness-index.dickinsonre.chatgpt.site). Its four pillars, twenty criteria and equal weights are kept here unchanged. Rung 3 of its rubric was reworded at Robert's direction, from Used to In service. Version 2.2 was built with Claude, Anthropic's AI model, in a Claude session in November 2026, under the direction of Robert (Bob) Dickinson. He supplied the v1.0 page, pointed Claude at his SWMM & ICM Knowledge Library and asked for the index to be improved from it. Responsibility for the index, and for every score on it, is his.

What Claude did. It read the v1.0 page and the library's Doc essay, its technical summary and its build stamp (artifact v63, 11 Nov 2026). It proposed the 20 baseline scores, wrote the 20 evidence lines and the 20 gap lines, rebuilt the page with a dark theme, the Evidence, About and Doc tabs and the evidenced total, drew the ten figures, among them a switchboard diagram made from a short text Robert supplied, and wrote this essay, the technical summary (.md) and the Word copy.

How the results were checked. Mechanically, by the build's own scripts: the 20 scores add to 66; the collection counts add to the library's 9,955; the yearly post counts add to 1,327; the numbers in the evidence and gap lines were matched against the library's text, with the unmatched ones listed in the technical summary; and the page was opened in headless Chromium at two widths in both themes.

What no person has checked. The 20 scores, the 40 evidence and gap lines, and this essay. Claude did not open the library's 9,955 individual records; the data block was larger than its reading tool would serve. Robert set the meaning of rung 3. He has not yet reviewed the 20 individual scores.

## Changes
- 2.2 (2026-11-11): switchboard diagram added to the Overview tab and the Doc essay (unplug from fear, plug into vision and creation), drawn from a short text Robert supplied. No score or formula changed.
- 2.1 (2026-11-11): level 3 reworded from "Used: there is evidence that someone put it to use" to "In service: delivered more than once, in a public place, and kept up"; baseline rescored from 55 to 66.
- 2.0 (2026-11-11): baseline of 55 scored from the Knowledge Library v63 in place of the 92 example, with level 3 read as use by someone else; evidence and gap line per criterion; claimed and evidenced totals; three lowest criteria on the front page; Evidence, About and Doc tabs; dark default with Light and Auto; v1.0 backup import; host widget and extension residue removed.
- 1.0: four pillars, 20 criteria, illustrative 92, one note per pillar.
