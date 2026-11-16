---
name: SWMM Second Brain
file: swmm-second-brain.html
version: 0.1.0
date: 2026-11-15
author: Robert Dickinson
links: {artifact: https://claude.ai/artifact/Y66NqQ856ExcQc1BuZt9gX, repo: https://github.com/dickinsonre/swmm-second-brain}
engines: none
units: not applicable
ai_use: built with Claude (Anthropic); see AI use
---

# SWMM Second Brain: a reader for Bob Dickinson's SWMM wiki

## What it does

One HTML page that holds every page of the wiki in `dickinsonre/swmm-second-brain` (the index, the log, and the source, concept, entity and synthesis pages), built from the repository after each ingest. It answers "what does the wiki say, and on what source?" without opening GitHub. Views: Read (index rail and page), Search, Open questions, To review, About, Doc. It runs no model and no engine.

## How it computes

1. `tools/build_app.py` reads the front matter of every page with `tools/common.py` (title, type, dates, `reviewed:`, `changed_after_review:`, `raw:`, `superseded_by:`).
2. It renders each page's markdown to HTML with Python-Markdown (extensions `tables`, `fenced_code`, `sane_lists`), after inserting the blank line that Python-Markdown needs before a list or table.
3. It rewrites every link: a wiki page becomes `#<page id>` inside the app; a file under `raw/` or any other repository file becomes its GitHub URL; an outside link opens in a new tab.
4. For a source page whose raw file is an app summary, it reads the `links:` line of that summary and makes buttons, Netlify first; an entity page takes the buttons of the first source cited in its text.
5. It reads `index.md` for the groups of the left rail, `wiki/open-questions.md` for the question list (open `- [ ]`, settled `- [x]`), `raw/MANIFEST.csv` for counts by status, and `log.md` for the last eight entries.
6. It writes one JSON block into `tools/app_template.html` and saves `build/swmm-second-brain.html` (full document, for Netlify) and `build/swmm-second-brain-artifact.html` (body only, for a Claude artifact).
7. Search in the browser: a page is a hit only if every typed word appears in its text or title; score = sum over words w of (n_w + 20 * T_w), where n_w is the number of times w appears in the page text and T_w is 1 if w is in the title.
8. The Doc tab is `tools/app_doc.md` with figures drawn by `tools/app_doc.py` from the log, the manifest and the pages, with numbers filled in at build time.

## Inputs and outputs

- Reads: `index.md`, `log.md`, `wiki/**/*.md`, `raw/MANIFEST.csv`, the front matter of `raw/apps/*.md`, this file (embedded in the page and shown in the About tab).
- Writes: `build/swmm-second-brain.html`, `build/swmm-second-brain-artifact.html`, `build/doc.md`, `build/figs/*.svg`. `build/` is not committed.
- In the browser: theme choice, the To review ticks and the last search are kept in `localStorage` only. The To review tab can copy the ticked list as text for Claude.

## Checks

On the build of 15 November 2026 (commit 37c380d and after):
- `tools/lint.py`: 0 errors, 1 warning (a newer St. Venant Rosetta Stone summary queued).
- 309 pages built (307 wiki pages, the index, the log); every one of the 307 pages listed in `index.md` resolved to a page; 0 links between wiki pages left pointing at a file.
- Headless Chromium at 1,366 x 900 and 390 x 844: home, a source page, an app page, open questions, review list, search and Doc, in the dark and light themes. No horizontal scroll; the only console errors were blocked web fonts on the test machine.
- A search for "Preissmann slot" returned the concept page "Preissmann slot and surcharge" first.
- SWMM App Complexity Meter (baseline HC-2026-11-01-e), four code files: index 38.1 (HydroCouple = 100; EPA SWMM 5.2.4 = 69.2 on the same meter); 13,346 code tokens on 730 code-bearing lines, 270 decision points, 127 callable units.
- Human review: none recorded.

## What this does not show

1. Most wiki pages have not been read by Bob: 119 of 307 say `reviewed: no` and 18 carry text added after his review.
2. The file is a snapshot of the repository at build time.
3. App buttons appear only where an app summary's `links:` line names an address; 9 summaries name a Netlify address, though most of Bob's apps are now on Netlify.
4. Search matches words, not meanings.
5. The raw files are not in the page; they open on GitHub.
6. No automated test suite; the checks are the linter, the link check and the screenshots above.

## How to reproduce

```sh
pip install markdown
python3 tools/manifest.py
python3 tools/lint.py
python3 tools/build_app.py
node tools/build_app_docx.js
```

## Credits and licenses

- Robert Dickinson: the wiki, its sources and the decisions on what is settled.
- The wiki pattern: Andrej Karpathy's LLM wiki (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- Python-Markdown (BSD-3-Clause), used at build time. Fonts from Google Fonts: Inter, Source Serif 4, JetBrains Mono (SIL Open Font License).
- The repository has no license set.

## AI use

Built with Claude, Anthropic's AI model, in a Claude session on 15 November 2026, at Robert Dickinson's direction; he decides what goes into the wiki and what is settled, and responsibility for the work is his. Claude wrote the build script, the page template, the Doc essay and its figures, the .docx and this file, and wrote or updated the wiki pages from the raw sources. Many app summaries in `raw/apps/` were written by Replit Agent and say so. Checks are mechanical (linter, link check, screenshots, complexity meter); no person has reviewed this summary.

## Changes

- 0.1.0 (2026-11-15): first version: Read, Search, Open questions, To review, About and Doc tabs; dark by default.
