---
name: SWMM5 Manual Search
file: swmm-manual-search-robertdickinson
version: "5.2"
date: "2026-07-20"
author: Robert Dickinson
links: {replit: https://swmm-manual-search-robertdickinson.replit.app, repo: https://github.com/dickinsonre/SJ-SWMM5-ManualSearch}
engines:
  - {name: EPA SWMM, version: "5.2.4", source: "swmm-toolkit solver.swmm_version_info(), app.py:540-548", commit: not recorded, license: "repository states public domain, README.md:369"}
stack: Python, FastAPI, Uvicorn, Jinja2, Whoosh, browser JavaScript and SVG, JSON Lines files, PySWMM, swmm-toolkit, Anthropic
units: both
ai_use: "Anthropic Claude model for chatbot and search-result summaries; development-tool attribution is described under AI use."
---

# SWMM5 Manual Search: Search the SWMM manual and examine model inputs

## What it does

The app answers where the SWMM manual discusses a search topic and returns matching sections, related concepts, and relevant INP references. Engineers can browse the manual, inspect engineering diagrams and calculators, check input files, and submit an INP model to the SWMM simulation engine. It also provides an HTTP API, an Anthropic-powered assistant, and manual exports. The app identifies Robert Dickinson as its creator (README.md:365-371; app.py:1603-1607).

## How it computes

1. `crawler.py` fetches the manual site and splits page content into records using headings where available. Each record contains a page URL, title, section, and text (crawler.py:14-16, 45-85).
2. `indexer.py:10-43` reads `data/docs.jsonl` and builds a Whoosh index over titles, sections, and content. The fields use stemming, and a section URL is used to update its index record.
3. `app.py:110-122, 279-287, 309-430` expands some queries with SWMM synonyms, supports fuzzy terms, searches the index, applies optional chapter filtering, and returns ranked results and excerpts.
4. `static/app.js:7982` defines calculator inputs, formulas, and computations. For example, circular-pipe flow uses the Manning equation, `V = (1.486/n) × R^(2/3) × sqrt(S)` and `Q = V × A` (static/app.js:7994-8003). The calculator suite supports US customary and SI units (README.md:38).
5. The INP quality endpoint parses submitted text and checks model structure (app.py:1076-1100). Validation opens an INP file with PySWMM but does not step the model (app.py:1034-1073). Simulation creates temporary INP, report, and output files, iterates the SWMM engine, and parses the report for continuity values, warnings, and errors (app.py:995-1031, 1361-1410).
6. The chatbot searches for up to eight manual results and sends the messages and retrieved context to Anthropic for a streamed answer (app.py:24-29, 1950-1975). The summary endpoint also sends search-result context to Anthropic (app.py:1870-1908).

## Inputs and outputs

- Search accepts text, a result limit, and an optional chapter filter through `GET /search` or `GET /api/v1/search` (app.py:476-477, 1610-1652).
- The public API also provides lookup, chapters, statistics, INP-reference, and health endpoints under `/api/v1` (README.md:197-209).
- INP text is accepted by `POST /api/validate-inp`, `POST /api/inp-quality`, and `POST /api/run-inp`. The run endpoint returns the generated SWMM report and analysis; its temporary model files are created inside a temporary directory (app.py:1034-1047, 1100-1112, 1361-1398).
- The app serves search results, manual references, CSV and PDF exports, and a downloadable project archive (README.md:48, 182-193).
- Server-side manual data is in `data/docs.jsonl`; the Whoosh search index is in `index/`. The repository describes storage as file-based and says it has no database (README.md:85-87).
- Learning-path progress is stored in browser `localStorage` (README.md:45). Chat and summarization requests send content to Anthropic. The repository does not establish the provider's data-retention policy (app.py:24-29, 1878-1908, 1963-1975).

## Contents

- The current `/stats` run returned 53 chapters, 621 indexed sections, and 248,407 words. The service calculates these fields from the local documents and index (app.py:522-557; `data/docs.jsonl` was also counted during this check).
- The rendered homepage contains 43 interactive diagram controls and 19 chat-language controls. The calculator registry contains 30 entries (templates/index.html:3338-3414, 3752-3770; static/app.js:7787-7797, 7982; counts checked against the rendered homepage).
- `data/swmm_version_history.json` contains 41 version records (counted from the file; app.py:793-821 reads the history).

## Checks

- Tests: 25 passed, 0 failed. Command: `python -m pytest tests/test_app.py -q`.
- Local page/API smoke check: `/`, `/intro`, `/presentation`, `/source`, and `/api/v1` each returned HTTP 200.
- A local homepage screenshot showed the main interface and its system-status panel. No browser-console entries were reported during that capture.
- Human review: none recorded.

## What this does not show

1. The front matter version `5.2` is the app's reported SWMM version, not a separately defined software release number (app.py:550-557). The front matter date is the date of the latest relevant Git change. The repository does not specify a separate release date for software version `5.2` (Git log checked; app.py:550-557).
2. The `/stats` run reported an index date of May 22, 2026. A fresh crawl was not run, and the stored index was not compared with the live manual (app.py:522-557; local homepage run).
3. User-supplied INP simulations, their engineering results, and live Anthropic responses were not tested during this check.
4. Interactive states, every calculator result, and keyboard or screen-reader operation were not checked during this run.
5. The production homepage was not loaded. The page checks and screenshot used the local app; deployment metadata reported the production URL and a successful build.
6. The README says the calculator suite contains nine calculators, while the current JavaScript registry and homepage run show 30. The README count is out of date (README.md:38; static/app.js:7982; local homepage run).
7. No record of a human review of this summary or the current app was found in the checked project sources.

## How to reproduce

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python main.py
```

Run the tests:

```bash
python -m pytest tests/test_app.py -q
```

The Replit workflow also starts the app with `python main.py` (.replit:25-29). The deployment configuration runs Uvicorn with `app:app` (.replit:37-39).

## Credits and licenses

- Robert Dickinson is credited as app creator (README.md:365-367; app.py:1603-1607).
- Scott Jeffers is credited for domain expertise and stewardship of the manual collection. The project identifies the U.S. EPA as the source of the SWMM manual and engine (README.md:367-371).
- The project describes the EPA manual and engine as public domain (README.md:369). This summary does not independently verify that licensing statement.
- The app's source code has no stated open-source license. The README says it is provided as-is and that no preferred OSS license has been added (README.md:375-377).
- Runtime package metadata identifies PySWMM as BSD-2-Clause, Whoosh as a two-clause BSD license, Anthropic's Python SDK as MIT, and the OpenAI SDK as Apache-2.0. The repository lists OpenAI as a fallback or for older endpoints (README.md:341, 344; installed package metadata checked during this run).
- The repository's requirements list FastAPI, Uvicorn, Jinja2, HTTPX, Beautiful Soup, Playwright, and swmm-toolkit but do not state their licenses (requirements.txt).

## AI use

The running chatbot and search-result summarizer use Anthropic's `claude-sonnet-4-5` model (app.py:24-29, 1870-1908, 1950-1975; README.md:46-47). The README lists the OpenAI SDK as a fallback or for older endpoints but does not name an OpenAI model (README.md:344). Project attribution names Robert Dickinson as app creator but does not describe a task-by-task authoring split (README.md:365-371). The checked source and Git history do not identify Replit Agent or another AI as an app developer. This summary was written by Replit Agent on 2026-11-15 from the project's source. Robert Dickinson has not yet reviewed it.

## Changes

Recent application changes, newest first, from `git log`:

- 2026-07-20: Updated the app's trust and consistency details.
- 2026-07-20: Improved reindex status handling and token security.
- 2026-05-29: Improved search clearing and interface synchronization.
- 2026-05-28: Added the GitHub repository link.
- 2026-05-28: Improved navigation and added diagram filtering and URL hash support.
- 2026-05-28: Added a downloadable application archive.
- 2026-05-28: Added calculators and corrected calculation behavior.
- 2026-05-28: Added advanced search and diagram export features.
- 2026-05-28: Added hydraulic calculators and corrected calculation issues.
- 2026-05-28: Added search-result bookmarks and multi-select export.
