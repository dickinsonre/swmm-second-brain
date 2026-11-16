# SWMM second brain

A knowledge base of what Robert (Bob) Dickinson has written and built about SWMM, ICM and the engines around them, kept in the form Andrej Karpathy described in his 2026 "LLM wiki" gist: raw sources that are never edited, a wiki of linked markdown pages that an AI agent writes and maintains from them, and a schema file that tells the agent how.

It is not a search index. Each source is read once and compiled into pages; a question is answered from the pages.

## Where things are

| Path | What |
|---|---|
| `raw/` | Sources. 422 files, about 1,330,000 words. Never edited. `raw/MANIFEST.csv` has a hash, a word count and a status for each |
| `wiki/` | 354 pages, about 176,000 words: 179 sources, 72 concepts, 101 entities, an overview and an open-questions list |
| `index.md` | Catalog of every page. Start here |
| `log.md` | What was done and when |
| `CLAUDE.md` | The schema: page rules and the three operations |
| `tools/` | `manifest.py`, `lint.py`, `search.py`, `li2md.py`; `build_app.py` and `build_app_docx.js`, which build the reader app (one HTML page of the whole wiki) into `build/`; `ontology.py`, which builds the typed relations into RDF |
| `ONTOLOGY.md`, `ontology/` | the draft vocabulary of typed relations, and what `tools/ontology.py` builds from the pages' Relations tables: TriG, JSON-LD, a CSV, a Mermaid graph and sample SPARQL queries |

## How to use it

Attach the repository to a Claude session (or open it in Claude Code) and say one of three things.

- **"Ingest the next batch"**, or "ingest raw/apps/one-swmm.md". The agent reads the source, writes its source page, updates every concept and entity page it touches, and reports any contradiction.
- **Ask a question.** "What do I have on conduit lengthening?" The agent answers from the wiki with citations, and files the answer as a page if it is worth keeping.
- **"Lint."** The agent runs `python3 tools/lint.py` and then reads for contradictions, stale claims and missing pages.

To add a source, drop the file in the right folder under `raw/` and say "ingest". For a new LinkedIn export, run `python3 tools/li2md.py PATH/TO/Articles/Articles` first.

To add an app, upload its technical summary, named `APPNAME-vVERSION.md`, to `raw/apps/` (on GitHub: https://github.com/dickinsonre/swmm-second-brain/upload/main/raw/apps) and say "ingest". One file per released version; never upload over an existing name. Older versions that were never ingested are marked `superseded` and skipped, and identical files are marked `duplicate`, so extra uploads do not pile up in the queue. The rules are in `CLAUDE.md` under "App summaries and versions".

To add an idea of your own, copy `raw/notes/_TEMPLATE.md` to a new file in `raw/notes/`, write one idea in it, and say "ingest". The template came from the earlier `swmm-brain` repository, which this one replaces; its contents are in `raw/swmm-brain/`.

To read the wiki yourself, open the folder in Obsidian (the graph view shows hubs and orphans) or browse it on GitHub; every link is a plain relative link and works in both.

## State on 16 November 2026

- 179 of 422 raw files ingested, one of them (the EPA hydraulics manual) in part. The queue is in `index.md`.
- 82 open questions in `wiki/open-questions.md`, and 8 settled. Several are contradictions between Bob's own articles.
- Bob reviewed every page on 11/16/2026. Since then, 37 new pages say `reviewed: no` (graph theory, the seventeen AI-written ICM notes and their pages, and two Curve Number articles) and 5 carry `changed_after_review:` (Infiltration methods, InfoWorks ICM, SWMM 5 versus ICM InfoWorks, the open questions and the overview).
- The ontology draft has Relations tables on 3 pages: 89 statements, each filed under the source it cites, with conditions and a `verification` status on the rows that need them. `ontology/queries/5-comparable-fields.txt` answers "which fields can I compare across InfoWorks and ICM SWMM networks, under what conditions, and on what evidence?" for the fields the wiki has so far.

## What is not here

The text of the OpenSWMM posts, the swmm5.org and swmmfive.com posts, the Ruby script library, the EPA manuals, and the technical summaries of apps built before November 2026. See "What is missing from raw" in `wiki/overview.md`.

## What a reader should know

Public at https://github.com/dickinsonre/swmm-second-brain since 14 November 2026, by Bob's decision. `raw/` holds his published articles and his working notes; the wiki holds professional facts only. Unpublished LinkedIn drafts were left out of `raw/` on purpose.

Treat it as a working notebook, not a reference:

- Bob read every wiki page on 11/16/2026. A page added since says `reviewed: no`; a page changed since carries `changed_after_review:`. `python3 tools/lint.py --review` lists both, in the order to read them.
- Many sources were drafted by an AI (ChatGPT, Claude, the GPT plugin for Autodesk) and say so under "How it was written". A claim resting on one is no stronger than that draft until a run or Bob checks it.
- Findings marked `unconfirmed` have not been rerun. They are notes, including the ones about other people's code.
- `wiki/open-questions.md` lists where the sources contradict each other. Until an item is ticked, neither side is settled.
- The OpenSWMM thread list names the people who started or joined each public forum thread, as openswmm.org shows them.

## Credits

- Robert (Bob) Dickinson: every source, the six themes, the decisions.
- Andrej Karpathy: the LLM wiki pattern, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- The people and projects named in the sources are credited on the pages that draw on them.

## AI use

This repository was set up on 14 November 2026 by Claude, Anthropic's AI model, at Bob's direction. Claude converted the LinkedIn export, copied the other sources in, wrote the schema, the tools and all 144 wiki pages across several sessions, computed the OpenSWMM counts, and found the 49 open questions. The mechanical checks are `tools/lint.py` (links, front matter, citations, raw-file hashes). The content checks were Claude rereading each page against its sources; no person has read any wiki page yet, and each page says so in its front matter. Many of the sources themselves contain AI-written passages; each source page records what is known about how it was written.

No license has been set.
