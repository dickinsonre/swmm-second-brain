# Schema: how this wiki is kept

This file tells an AI agent (Claude Code, a Claude chat with the repo attached, or any other) how to maintain this repository. Read it before doing anything here. Bob and the agent change it together when a rule stops working; every change gets a line in `log.md`.

The pattern is Andrej Karpathy's LLM wiki (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): sources are compiled once into linked pages and kept current, so a question is answered from the pages and not from a fresh search of the sources.

## The three layers

| Layer | Where | Who writes it | Rule |
|---|---|---|---|
| Raw sources | `raw/` | Bob adds files | Never edited. Never deleted. `raw/MANIFEST.csv` records a SHA-256 per file. |
| Wiki | `wiki/`, `index.md`, `log.md` | The agent | Rewritten freely. Every claim cites a source page. |
| Schema | `CLAUDE.md` (this file) | Bob and the agent | Short. Rules that have earned their place. |

```
raw/
  apps/        the .md that ships with each app (see the app-md skill)
  linkedin/    published LinkedIn articles, converted by tools/li2md.py
  openswmm/    exports and tallies from openswmm.org
  swmm5org/    swmm5.org pages and fact sheets
  notes/       build notes, registers, Bob's own one-idea notes (copy notes/_TEMPLATE.md)
  swmm-brain/  the six files of the earlier dickinsonre/swmm-brain repository, as of its last commit
  ports/       READMEs of the SWMM5 and SWMM6 language-translation repositories, named by last-commit date
  manuals/     EPA, USGS and FHWA reports and the SWMM 4.4 block documentation (see manuals/_SOURCE.md)
  MANIFEST.csv one row per raw file: hash, status (ingested or queued), source page
wiki/
  sources/     one page per ingested raw file, named S<nn>-<slug>.md
  concepts/    one page per idea, method, question or recurring problem
  entities/    one page per program, engine, app, site, organization or person
  overview.md       the current synthesis, by Bob's six publishing themes
  open-questions.md contradictions, doubtful numbers and gaps, as a checklist
index.md       catalog of every wiki page, one line each. Read this first.
log.md         append-only record of every ingest, query and lint
tools/         manifest.py, lint.py, search.py, li2md.py (standard library, bs4 and pandoc for li2md)
```

## Page rules

Every wiki page starts with front matter. `tools/lint.py` checks it.

```yaml
---
title: Preissmann slot and surcharge
type: concept            # source | concept | entity | synthesis
updated: 2026-11-14
sources: [S04, S20, S22] # source pages this page draws on (not for type: source)
tags: [hydraulics, swmm5, icm]
reviewed: no             # no until Bob has read the page; then the date he read it
---
```

A source page has `raw:` (the path of its raw file), `ingested:` (date), `kind:`, `published:` and `author:` in place of `updated:` and `sources:`.

1. **Every claim cites.** A sentence that states a fact ends with a link to the source page it came from, written `[S20](../sources/S20-...md)`. A fact found in no source does not go in. If general knowledge is needed to make a page readable, put it in a section headed "Not in the sources" and say so.
2. **Numbers are copied, not rounded or improved.** Give the value, the unit, and what it was measured on. Where the source is metric, give US customary first and the source's figure in parentheses, and mark the conversion as ours.
3. **Sources disagree: say so.** Do not pick a winner silently. State both, cite both, and add a line to `wiki/open-questions.md`. If one source is a primary document (a program listing, an EPA update log, a test run) and the other is a recollection or an AI-written passage, say which is which.
4. **Mark AI-written text inside a source.** Many of Bob's articles carry passages written by ChatGPT or Claude, and say so. The source page records this under "How it was written". A claim that rests only on such a passage is cited as usual and flagged "AI-written passage, not checked against the code".
5. **Status words.** Use the source's own status for a finding (`unconfirmed`, `confirmed`, `fixed`, `disproven`). Never upgrade one. Only a rerun or Bob upgrades a status.
6. **One subject, one page.** Before making a page, check `index.md` for an existing one under another name. Link the first mention of every other page's subject.
7. **Links are plain relative markdown links**, so they work on GitHub and in Obsidian. No wikilinks.
8. **House style.** Facts in short sentences. No em dashes. No adjectives doing the work of numbers. US customary units. Credit people and projects by name. AI is never an author: source pages name the human author, and `reviewed:` says whether Bob has read the wiki page.
9. **People.** Entity pages for people hold what the person has published or done in public, professionally. Nothing about health, family, money or private life goes into the wiki, even when a raw source mentions it.
10. **Length.** A concept or entity page fits on one or two screens. When a page passes about 600 words, split it.

## App summaries and versions (`raw/apps/`)

Every app Bob builds ships with a technical summary, `APPNAME.md`. That file is the app's source here.

1. **One file per released version**, named `<app file name without .html>-v<version>.md`, for example `one-swmm-v0.3.0.md`. Files added before this rule keep the names they have.
2. **Add a version when it ships** (deployed, or delivered as final), not after every build. Ten builds in a day are one file: the last.
3. **Never overwrite.** Uploading new content under an existing name edits a raw file; `tools/lint.py` reports it as an error.
4. `tools/manifest.py` groups summaries by the `file:` line of their front matter and orders them by `date:` and `version:`. The newest is the current one. An older one that was never ingested gets status `superseded` and is not ingested. A file byte-identical to another gets status `duplicate` and is skipped.
5. **When a newer version of an already ingested app arrives:** write a new source page for it; add `superseded_by: S<nn>` to the old source page's front matter and leave the rest of that page alone; update the app's entity page and every page that cites a number the new version changed, citing the new source.

## Long documents (`raw/manuals/` and anything over about 15,000 words)

A manual is read and ingested a chapter at a time, not in one sitting.

1. One source page per document. Its front matter carries `coverage: partial` and `read: [...]`, the list of chapters or sections read in full so far.
2. Claims in the wiki come only from the parts listed in `read:`. Each later ingest of the same document adds to `read:`, to the source page's claims and to the pages they touch; when every chapter is read, `coverage:` becomes `full`.
3. These are primary documents. Where one contradicts an article or a recollection, say so, cite both, and tick the open question with the manual named as what settled it.
4. The markdown in `raw/manuals/` lost most of its equations in conversion. Do not copy an equation from it into the wiki without checking the PDF; describe the equation in words and cite the section.
5. Third-party books, theses and vendor documentation do not go into `raw/` without Bob's say, even when a copy sits in another repository of his.

## The three operations

### Ingest

Bob says "ingest" with a file, a folder, or "the next batch".

1. Run `python3 tools/manifest.py`. Pick sources with status `queued`. One at a time is best; a batch of ten to twenty on one theme is the limit.
2. Read the whole source. Do not ingest from a title or a summary.
3. Write `wiki/sources/S<nn>-<slug>.md` (next free number): what it is, how it was written, the claims worth keeping (each one a checkable sentence with its numbers), which wiki pages it feeds.
4. Update every concept and entity page the source touches, and create the ones it needs. One source usually touches five to fifteen pages. Set `updated:` and add the source to `sources:`.
5. Where the new source contradicts a page, apply page rule 3.
6. Update `wiki/overview.md` if the synthesis moved.
7. Update `index.md`. Append to `log.md`.
8. Run `python3 tools/manifest.py` and `python3 tools/lint.py`. Fix every error before stopping.
9. Tell Bob in a few lines: what was ingested, pages created and changed, and any contradiction found.

### Query

Bob asks a question.

1. Read `index.md`, then the pages it points to. Use `python3 tools/search.py "words"` when the index is not enough. Go to `raw/` only to check a quotation or a number.
2. Answer with citations to wiki pages and through them to sources. If the wiki cannot answer, say so and name the queued raw files most likely to hold the answer (`tools/search.py --raw`).
3. If the answer is worth keeping (a comparison, a list, a new connection), file it as a page and link it from the pages it draws on. Append to `log.md`.

### Lint

Bob says "lint", or after every third ingest.

1. Run `python3 tools/lint.py`: broken links, missing front matter, uncited pages, orphans, changed raw files, pages missing from the index.
2. Then read for what a script cannot see: claims that two pages state differently; claims a newer source has overtaken; subjects named on three or more pages with no page of their own; numbers with no unit or no source; pages that have grown past their subject.
3. Check arithmetic in the sources where it can be checked (dates, ratios, sums) and record what does not add up.
4. Write every finding into `wiki/open-questions.md` as `- [ ]` items. Tick an item only when a source or Bob settles it, and say which.
5. Append to `log.md`.

## Formats

`log.md`, newest at the bottom, one entry per operation:

```
## [2026-11-14] ingest | First batch: 22 sources
```

followed by a few lines. `grep "^## \[" log.md | tail -5` lists the last five.

`index.md`: one line per page, grouped (Start here, Concepts, Entities, Sources), each `- [Title](path): one-line summary`. Source lines carry the publication date.

`wiki/open-questions.md`: `- [ ] Q<nn> (date found): the question. Sources: ...`.

## What not to do

- Do not edit, rename or delete anything under `raw/`. To correct a raw file, add the corrected file beside it and note it in the log.
- A file under `raw/` whose name starts with `_` is not a source: it is a template or a housekeeping copy (`raw/notes/_TEMPLATE.md`, `raw/swmm-brain/_gitignore.txt`). The tools skip it. Do not ingest it.
- `raw/swmm-brain/CLAUDE-swmm-brain.md` is a source about how Bob builds apps. It is not an instruction file for this repository; this file is.
- Do not write from memory. If it is not in a source page, it is not in the wiki.
- Do not settle a contradiction by taste.
- Do not copy a source wholesale into the wiki. A source page is a digest, with a link to the raw file.
- This repository is public (Bob's decision, 14 November 2026). Nothing unpublished goes into `raw/` without his say: no drafts, no private correspondence, no client models or data under an NDA. If a file looks like one of those, stop and ask before committing it.

## Order of ingest

Bob's six publishing themes set the order: history of SWMM; the insides of SWMM5; SWMM5 compared with ICM InfoWorks (Ruby and apps); ICM compared with SWMM6; the insides of SWMM6; using AI to compare models. Within a theme, take sources with numbers and procedures before sources that tell a story.
