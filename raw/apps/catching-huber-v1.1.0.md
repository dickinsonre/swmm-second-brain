---
name: Catching Huber
file: catching-huber.html
version: 1.1.0
date: 2026-11-16
author: Robert Dickinson
links: {netlify: not yet deployed, artifact: private claude.ai artifact, repo: none}
engines: none (bibliometric arithmetic only; no hydraulic engine)
units: counts of works and citations; years
ai_use: built and written with Claude Fable 5.2 (v1.0) and Claude Opus 5.5 (v1.1), Anthropic; see AI use
complexity: {meter: SWMM App Complexity Meter, analyzer: meter-core.js 1.7.0, baseline: HC-2026-11-10-h}
---

# Catching Huber: a publication ledger and h-index simulator for a SWMM developer

## In three points
- **What:** A ledger and simulator that grades Bob Dickinson's publication record against Wayne Huber's and runs his Google Scholar profile forward year by year, with a named plan of 26 papers and without it.
- **So what:** From 5,683 citations, an h-index of 33 and an i10-index of 76, the h-index reaches about 37 by 2031 with or without new papers; the two runs first differ in 2033, and in 2036 only four new papers, all reference papers, are in the h-core. The stand-in list of 130 counts holds only seven real counts, and the growth rule overshoots the measured since-2021 h by 3, so the gain is an upper estimate.
- **Now what:** Use it to choose which papers to write, not to forecast. Bob's real per-work counts were not used, Huber's Google Scholar figures were not found, and every new-paper citation rate is an assumption.

**In one sentence.** Catching Huber is a ledger and simulator showing that Bob Dickinson's Google Scholar h-index of 33 reaches about 37 by 2031 with or without new papers, and that only four reference papers change it after that.

**In one paragraph.** Catching Huber grades Bob Dickinson's publication record against Wayne Huber's and tests a paper plan before any paper is written. It starts from the three numbers on Bob's Google Scholar profile: 5,683 citations, an h-index of 33 and an i10-index of 76. It fits a stand-in list of 130 citation counts to those numbers, then steps the list forward one year at a time under a plan of 26 papers. The growth rule was checked against the profile's own since-2021 column, where it matches the i10-index within 1 and overshoots the h-index by 3. The main limit is Huber himself. He has no public Scholar profile, so his only measured figure is from OpenAlex: 48 papers, 631 citations, h-index 13.

**What is unique about this app.** Not much of the software is unique. Google Scholar, Publish or Perish and OpenAlex all report an h-index, and Acuna, Allesina and Kording published an h-index predictor in Nature in 2012. What this app adds is a comparison those tools do not make: one profile run forward twice, with a named paper plan and without it, so you can see which papers move the index and when. The content is also specific to SWMM. It carries Bob's cleaned profile, Huber's OpenAlex record, and the gap of about 50 times between the two indexes on one SWMM manual.

## What it does

Answers one question: how many papers, of what kind, move a 48-year SWMM developer's citation indices, and by when. It gives a corrected scorecard, a year-by-year projection of item count, total citations, h-index and i10-index with and without a paper plan, and a list of 16 proposed papers that feed the projection. It is for Bob Dickinson. Nothing in it is specific to him except the data file.

## How it computes

Source files: `src/sim.js` (pure functions), `src/data.js` (every number), `src/figs.js` (figures), `test.js` (checks).

- h-index: sort counts descending; h is the largest rank r with count[r] >= r. `sim.js hIndex`.
- i10-index: number of works with count >= 10. `sim.js i10`.
- Existing works, end of year t: `c_i(t) = floor(c_i(2026) + G * (t - 2026) * c_i(2026) / sum(c))`, with G = 325 citations per year by default.
- New paper of class rate r published in year y, end of year t: `c = floor(r * ((t - y) - 0.5))` for t > y, else 0.
- Years for one paper to hold N citations: `N / r + 0.5`.
- Each year: build the full list, then report items, total, h, i10, and the number of new papers with count >= h.
- Two runs are always made: with the plan, and with no new papers.
- Byline switch: removes the 290 and 248 entries (the two SWMM5 reference manuals, bylined Rossman and Huber) and scales G by the remaining share of citations.

Defaults (all adjustable in the app): G = 325; rates 10 (Reference), 3 (Method), 0.8 (Note) citations per year; 2 notes per year for 2027 to 2031; horizon 2031; target h 40 (placeholder); target items 120.

Stand-in list: 130 counts. Seven are real, read from the screenshots: 859, 290, 283, 248, 80, 10, 5. The other 123 are a geometric and power-law fill tuned so the list gives total 5,683, h 33, i10 76. The item count of 130 is an assumption.

## Inputs and outputs

Inputs: the constants in `data.js`; optionally a pasted column of citation counts (any integers, one per line), which replaces the stand-in list. Outputs: on-screen tables and SVG figures; a CSV of the run through Export (copy to clipboard). Settings persist in localStorage on the viewer's own browser only.

Measured inputs:

| Quantity | Value | Source |
|---|---|---|
| Scholar, before cleanup | 21,635 citations, h 61, i10 123 | screenshot 1, 2026-04-14 |
| Scholar, after cleanup | 5,683 citations, h 33, i10 76 | screenshot 2, 2026-04-14 |
| Scholar, since 2021 | 1,738 citations, h 19, i10 34 | screenshot 2 |
| Citations per year 2019 to 2026 | ~290, 255, 325, 340, 330, 328, 322, 100 (2026 to April) | bar heights read off screenshot 2, about +/-10 |
| SWMM4 manual (Huber and Dickinson 1988) | 859 on Scholar; 17 indexed on OpenAlex | screenshot 2; rankless.org |
| Huber on OpenAlex | 48 papers, 631 indexed citations, h 13 | rankless.org/authors/wayne-c-huber, read 2026-11-12 |
| Huber top-20 OpenAlex counts | 58 57 46 45 44 42 37 36 32 22 20 17 16 13 11 11 9 9 8 8 | same page |
| Huber output, own count | over 120 reports and technical papers | author note, Hydrology and Floodplain Analysis, 4th ed. |
| JWMM | $0 to publish, open access, CiteScore 1.5, impact factor 0.9 | chijournal.org |
| JWMM on OpenAlex | 492 papers, about 2,400 indexed citations (4.9 per paper) | alpha.rankless.org/sources/jwmm |

## Checks

All mechanical, run by `node test.js` on this build. Nine pass.

1. h-index on four hand-worked lists: 4, 3, 0, 0.
2. Huber's top-20 OpenAlex list: h = 13, equal to OpenAlex's stated 13.
3. Stand-in list: 130 entries, total 5,683, h 33, i10 76.
4. Null control (G = 0, no papers): every year 5,683 / 33 / 76 / 130 items.
5. New-paper rule at 10 per year: 0, 5, 35 citations at ages 0, 1, 4 years.
6. Per-year bar readings 2021 to 2026 sum to 1,745; Scholar states 1,738.
7. Byline switch on the stand-in list: 5,145 citations, h 32, i10 74.
8. Thirty notes and nothing else: h and i10 equal to the no-papers run in 2031 and 2036.
9. Backcast: sharing the 1,738 since-2021 citations by the growth rule gives since-2021 h 22 and i10 33; Scholar shows 19 and 34.

Default-plan results (stand-in list, asserted in `test.js`):

| End of year | Case | Items | Citations | h | i10 |
|---|---|---|---|---|---|
| 2026 | today | 130 | 5,683 | 33 | 76 |
| 2031 | no new papers | 130 | 7,252 | 37 | 82 |
| 2031 | default plan | 156 | 7,438 | 37 | 88 |
| 2036 | no new papers | 130 | 8,875 | 41 | 86 |
| 2036 | default plan | 156 | 9,477 | 43 | 102 |

Default plan: 26 papers (4 Reference, 12 Method, 10 Note); by year 6, 7, 5, 5, 3. The two h lines first differ in 2033. Four new papers are in the h-core in 2036, all Reference. Years to 34 citations: 3.9, 11.8, 43.0. Years to 10 citations: 1.5, 3.8, 13.0.

Complexity, measured with the SWMM App Complexity Meter analyzer 1.7.0 against baseline HC-2026-11-10-h (HydroCouple GitHub org = 100), on 11 hand-written source files: index 38.7; Size 41.4, Structure 56.8, Test evidence 0.0, SWMM vocabulary 0.0. Shipped .html alone: 34.7. Test evidence is 0 because the nine checks are assert calls in one script.

Human review: none yet.

## What this does not show

1. Huber's Google Scholar citations or h-index. None found. Target h 40 is a placeholder.
2. Bob's OpenAlex or Scopus record. Not looked up.
3. Bob's real per-work counts. The list and the 130-item count are stand-ins.
4. How many of the 76 works are peer-reviewed journal papers.
5. Acceptance, publication date or real citation rate of any planned paper. The three rates are assumptions.
6. The growth rule overshoots the measured since-2021 h by 3 (check 9), so the existing-works h gain (33 to 37 by 2031) is an upper estimate.
7. Self-citation, unmerged duplicates, or changes in Scholar's rules.
8. Whether the model corpus can be released; licenses are unchecked.
9. The 16 paper titles were drafted by Claude and are not approved by Bob.
10. No person has checked the bar readings, the rates, or the completeness of Huber's OpenAlex record.

## How to reproduce

`node test.js` (checks and default-plan table), `node build.js` (app, artifact fragment, .md, and dist/complexity.json from `tools/complexity.js`), `node build-docx.js` (essay as .docx). `tools/meter-core.js` and `tools/meter-baseline.json` are copied verbatim from the SWMM App Complexity Meter artifact. To rerun with real data: paste the Scholar Cited by column into the Simulator tab, or replace `standIn` in `src/data.js`.

## Credits and licenses

Wayne C. Huber (the yardstick, and co-author of the SWMM4 manual). Jorge E. Hirsch (h-index, 2005). D. E. Acuna, S. Allesina and K. P. Kording (h-index predictor, Nature, 2012). SWMM App Complexity Meter (analyzer and HydroCouple baseline, Bob Dickinson's app). OpenAlex and rankless.org (open citation data). CHI (Journal of Water Management Modeling). Fonts: IBM Plex Sans and IBM Plex Mono (SIL Open Font License), loaded from Google Fonts. App license: not yet set by Bob.

## AI use

This app and this essay were built with Claude, Anthropic's AI model, at the request of Robert (Bob) Dickinson. Claude Fable 5.2 built version 1.0 on 12 November 2026. Claude Opus 5.5 made version 1.1 on 16 November 2026. Bob asked the question, supplied the two profile screenshots, cleaned the profile himself and set the goal. Responsibility for anything published from this is his.

What Claude did in version 1.0: read the numbers off the screenshots, looked up Huber's OpenAlex record on rankless.org and the journal facts on chijournal.org, wrote the simulator and its tests, fitted the stand-in list, drew the figures, drafted the paper plan and its titles, and wrote every word here, including the earlier grades this essay corrects. In version 1.1 it wrote the section on what is unique about the app and the sentence on the 2012 h-index predictor. It also copied the analyzer and baseline from Bob's SWMM App Complexity Meter, ran them on this app's source, and wrote the closing complexity box from that run.

How it was checked: the nine mechanical checks above run in a test script, and the complexity numbers come from the Meter's own analyzer, not from judgment. What no person has checked: the bar heights read off the chart, the three assumed rates, the plan titles and whether Bob wants to write them, and the completeness of Huber's OpenAlex record. A journal will want its own AI disclosure for each paper in the plan. Follow that journal's rule. The AI does not go on the author line.

## Changes

`1.1.0 (2026-11-16)`: added What is unique about this app (Doc, About, .md) and the closing complexity box measured with the Meter's analyzer; one sentence on the 2012 predictor; AI use updated.
`1.0.0 (2026-11-12)`: first build. Replaces the earlier chat-only grade and 70-paper plan.
