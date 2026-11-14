
---
name: SWMM App Complexity Meter
file: swmm-app-complexity-meter.html
version: 1.9.1
date: 2026-11-11
author: Robert Dickinson
links: {artifact: "https://claude.ai/artifact/LkChM9gVnmhNpZcX5Lo55m", netlify: none recorded, repo: none}
engines: none (the page runs no hydraulic engine; it reads source code)
analyzer: {name: meter-core.js, version: 1.7.0, content_hash: "f90db29a:d77073c4:144842"}
baseline: {id: HC-2026-11-10-h, measured: 2026-11-10, repositories: 43, organization: github.com/HydroCouple}
units: counts of source code; no physical units
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM App Complexity Meter: how big and how tangled is a modeling app, with HydroCouple = 100

## What it does

Reads a program's source (one .html, a folder, a .zip, or a GitHub repository) in the browser and grades it on eight counted dimensions against the HydroCouple GitHub organization, which is fixed at 100. An app can score above 100; most score below. The index measures source footprint, not quality and not capability. Beside the index it reports what size alone would score, a score against one HydroCouple peer, 36 separate metrics, a map of which SWMM processes the code names, nine software-sustainability indicators, and (from a git log) 12 months of history. Nothing is uploaded; the same analyzer file runs in Node and in the page.

## How it computes

1. Sieve. Files are classified by extension and content. Third-party folders, generated files, Doxygen output, duplicates (by content hash) and files over 3 MB are set aside and listed with the reason.
2. Lex. Comments, string contents and encoded data are blanked per language family, so formatting cannot change a count.
3. Count eight dimensions (weights sum to 1):

| Dimension | Unit | Weight | HydroCouple anchor |
|---|---|---|---|
| Bulk | code tokens | 0.15 | 6,607,205 |
| Decisions | estimated decision points | 0.2 | 123,080 |
| Routines | callable units | 0.1 | 38,818 |
| Test markers | test and assertion markers | 0.1 | 27,339 |
| Stack | languages + technology signals | 0.1 | 31.573 |
| Dependencies | outside libraries | 0.1 | 77 |
| Formats | file formats | 0.1 | 43 |
| SWMM vocabulary | SWMM 5.2.4 terms in code | 0.15 | 226 |

4. Score each dimension on a log scale, 25 points per factor of ten, with a soft floor:

   `score = 100 * log10(1 + x/x0) / log10(1 + H/x0)`, `x0 = H * 10^(-100/25)`

   where x is the program's count and H is HydroCouple's. One tenth of HydroCouple reads about 75; equal reads 100.
5. Index = weighted mean of the eight scores. Sub-indexes: Size (Bulk, Routines), Structure (Decisions, Stack, Dependencies, Formats), Test evidence, SWMM vocabulary.

Beside the index (none of these feeds it):

- From size alone = the Bulk score by itself. Beyond size = index minus that.
- Against one peer = the same eight dimensions with one HydroCouple repository as the anchor: openswmm.engine (index 90.1), openepanet.engine (index 67.1), openswmm.gui (index 89.1), SWMMComponent (index 48.0).
- Among those measured = share of the 55 measured repositories of 2,000 code tokens or more that score lower.
- Tracks size = Spearman rank correlation of a metric with code tokens across those 55.
- Comment density = lines carrying comment text / lines carrying anything (Python docstrings count). Modularity = share of source files with 10 to 1,000 non-blank lines.
- Sustainability = the nine indicators of Nyenah, Doell, Katz and Reinecke (2024); each is met, not met, or cannot tell.
- SWMM processes = the 226 SWMM 5.2.4 dictionary terms sorted into 16 processes, each term in exactly one (`PROCESSES` in meter-core.js).
- History = parsed from `git log --numstat --no-merges --date=short --format="@@%h|%ad|%an"`. Churn = lines added + deleted in source files outside third-party folders; relative churn = churn / today's code-bearing lines; a coupled pair = two files changed together in 5 or more commits and in at least half the commits of the quieter file. Counts only; no names are kept.

## Inputs and outputs

- Reads: source code in the languages the analyzer classifies (C, C++, C#, Fortran, Python, JavaScript, TypeScript, Rust, Go, Java, Pascal, R, Julia, shell and others), HTML with embedded scripts, .zip archives (stored and deflate), GitHub repositories pinned to a commit SHA (up to 2,500 files; hosted copy only, the Claude viewer blocks network calls), a saved report (.json), a git log (.txt).
- Writes: scorecard CSV, metrics CSV, task CSV, batch CSV, a JSON report (analyzer hash, baseline, acquisition record, per-file table with content hashes, evidence, overrides, project signs, history counts), a GIF walkthrough.
- A saved report is scored against the baseline it was measured under.

## Checks

Mechanical, all run on this build (1.9.1, analyzer 1.7.0):

| Check | Result |
|---|---|
| Lexer cases, counts worked by hand | 13 of 13 pass |
| Regression cases (five outside reviews, the metrics work, the v1.9 rulers) | 83 of 83 pass |
| Fixtures with expected counts, also live on the Verify tab | 66 of 66 pass |
| Browser cases, headless Chromium, standalone file | 109 of 109 pass |
| Eight counts of all 62 repositories versus baseline g | 0 differences |
| Second full measurement from the packaged scripts (`node verify.js`) | every count, indicator and history figure reproduced |

Measured facts of this baseline:

- Anchor: 6,607,205 code tokens on 792,668 code-bearing lines, 123,080 decisions, 38,818 routines, 27,339 test markers, 77 outside libraries, 43 file formats, 226 of 226 SWMM terms.
- Other scopes: all 47 repositories = 106.4; without forks = 97.0.
- Size study (55 repositories, 40 of HydroCouple's, 15 references): rank correlation of the index with a tokens-only score 0.87; median gap 5.3 points, largest 17.1; first principal component of the eight dimensions 66.6% of variance. Rank correlation with code tokens: Halstead volume 1.00, decisions 0.98, routines 0.87, 95th-percentile cyclomatic 0.34, deepest nesting 0.33, duplication 0.04.
- HydroCouple upkeep: comment density 27.5%; 94% of source files between 10 and 1,000 lines. Of 37 repositories with code: documentation 37 of 37, open-source license file 35 of 37, tests 16 of 37, container recipe 0 of 37, every file in range 5 of 37.
- HydroCouple history (default branches, 12 months to 2026-11-01, 43 repositories): 1,019 commits by 13 people; relative churn 189.8%.

| Reference | Index | Size alone | Decisions per 1,000 tokens | SWMM processes | Indicators met | Commits, 12 months |
|---|---|---|---|---|---|---|
| Stormwater-Management-Model | 69.2 | 63.8 | 26.2 | 16 of 16 | 5 of 8 | 0 |
| EPANET | 70.2 | 61.9 | 22.3 | 8 of 16 | 6 of 8 | 46 |
| pyswmm | 61.5 | 44.9 | 12.6 | 13 of 16 | 6 of 8 | 31 |
| swmm5-rust | 80.3 | 81.1 | 11.1 | 16 of 16 | 4 of 8 | 37 |
| swmm5-cplus | 74.2 | 67.5 | 23.5 | 16 of 16 | 5 of 8 | 14 |
| SWMM-Explorer | 74.6 | 65.5 | 23.3 | 16 of 16 | 5 of 8 | 28 |

## What this does not show

- Complexity is not quality. A high index can be a sprawling program; a low one can be a focused one.
- The index is source footprint. What works is covered only by the Tasks tab, where passes are attested by a person and not run by the page.
- Routine counts come from per-language pattern rules, not parsers. Halstead, cyclomatic, cognitive and maintainability figures are approximations and have not been checked against a full parser.
- The size study describes these 55 repositories, 40 of them HydroCouple's own, not software in general.
- Project signs are file names. A README counts as documentation whatever it says; a Dockerfile counts whether or not it builds. Coding-standard compliance is never judged (needs Pylint).
- History depends on the log supplied. For the references it is the default branch up to 2026-11-01; for EPA SWMM the code measured is tag v5.2.4. Churn counts every source file in the log, so relative churn can pass 100%.
- Propagation cost was tried and not adopted: from the import graph EPA SWMM's solver read 12.3% and its Rust translation 3.1%, because Rust `use` paths and C calls are not seen. Not comparable across languages.
- Not checked by a person: the choice of dimensions and weights, routine counts in large files, the anchor's evidence item by item, the purpose tags, the acceptance-task sets, the grouping of terms into processes, the license patterns, the choice of peers, and the cut-offs for coupled files.
- Known: Python's standard-library `webbrowser` counts as an outside library in one reference (Swmm5AppEngine).

## How to reproduce

From the source package (swmm-app-complexity-meter-v1.9.1-source.zip):

```bash
while read r; do tools/sparse-clone.sh hc/src $r; done < hc/repos.txt     # code-only clones at the recorded commits
tools/history-clone.sh hc/src hist/hc                                      # full histories for the history ruler
SACM_ASOF=2026-11-01 SACM_HIST=hist/hc node measure.js meter-core.js hc/src hc-measure.json "$DEFS"
node verify.js expected/expected-aggregates.json hc-measure.json           # every count, indicator and history figure
node tests/lex-test.js meter-core.js && node tests/regress-test.js meter-core.js
node tests/fixtures-test.js meter-core.js fixtures.js anchor-data.json
python3 tests/browser-suite.py .
```

README.md in the package gives the scope definitions (`$DEFS`) and the commit list.

## Credits and licenses

- Robert (Bob) Dickinson, SWMM Enablement: the idea, the rule that HydroCouple = 100, the choice of metric families, the decision to build each version.
- HydroCouple (github.com/HydroCouple), Caleb Buahin and the OpenSWMM team: the anchor. Their repositories are measured, not redistributed.
- References measured: USEPA Stormwater-Management-Model v5.2.4, OpenWaterAnalytics EPANET, pyswmm, and Bob's own repositories.
- Methods: M. H. Halstead (1977); T. J. McCabe (1976); P. Oman and J. Hagemeister (1992); G. A. Campbell (2017); D. Landman, A. Serebrenik, E. Bouwers and J. J. Vinju (2016); A. van Deursen (2014); E. Nyenah, P. Doell, D. S. Katz and R. Reinecke (2024); N. Nagappan and T. Ball (2005); C. Baldwin, A. MacCormack and J. Rusnak (2014). Five outside reviews were produced with ChatGPT (OpenAI) and supplied by Bob.
- Fonts: IBM Plex Sans and IBM Plex Mono (SIL Open Font License). No license has been set for the meter itself.

## AI use

Built with Claude, Anthropic's AI model, in October and November 2026, at the request of Robert (Bob) Dickinson, who set the anchor and its rule. Responsibility for the work is his. Claude chose the eight dimensions and their weights, wrote the analyzer, the page, the tests, the essay and this file, measured HydroCouple and the references, and answered five ChatGPT reviews that Bob supplied by reproducing each finding as a failing test before fixing it. For version 1.9 Claude read the papers credited above, ran the size study, proposed seven changes, and built the six Bob approved. The checks listed under Checks are mechanical. What no person has checked is listed under What this does not show. The About tab carries the version-by-version account.

## Changes

- `1.9.1 (2026-11-11)`: the dial starts at the top of its box instead of the vertical middle of a column that 1.9.0 made taller; tiles sit two by two unless four fit; this file added.
- `1.9.0 (2026-11-10)`: size, peer and percentile readings; Metrics tab reordered to 36 metrics in six families; SWMM process map; nine sustainability indicators; history ruler; analyzer 1.7.0, baseline h.
- `1.8.0 (2026-11-01)`: fifth review. Scope rules, attested task coverage, EPANET task set, comparability check; baseline g.
- `1.7.0 (2026-11-01)`: Metrics tab, 23 metrics in four families; baseline f.
- `1.6.0 (2026-11-01)`: fourth review. Keywords used as names, Tasks tab, scopes, structure panel; baseline e.
- `1.5.0 (2026-11-01)`: third review. SWMM word collisions, JSX text, soft floor; baseline d.
- `1.4.0 (2026-10-31)`: second review. Bulk in tokens, sub-indexes, Verify tab; baseline c.
- `1.3.0 (2026-10-31)`: first review. Evidence per count, acquisition record, reports, Compare and Batch; baseline b.
- `1.0.0 (2026-10-31)`: first build; baseline a.
