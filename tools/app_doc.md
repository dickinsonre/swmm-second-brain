# How the SWMM Second Brain works

## What is unique about this app

As software, not much. It is one HTML file that shows markdown pages with an index, links and a search box, as many wiki readers do. What sets it apart is what it holds: Bob's SWMM and ICM sources compiled into pages where every fact cites a source page, disagreements between sources kept as numbered open questions, and typed relations (`ONTOLOGY.md`) that let a query ask which result fields can be compared across ICM's two network types, under what conditions and on what evidence. The model comparisons and the runs behind them are the point; this page is the way to read them.

## In one sentence

The SWMM Second Brain is one web page that holds every page of Bob Dickinson's wiki, rebuilt from the repository after each ingest, so you can read, search and check the wiki without opening GitHub.

## In one paragraph

Bob's wiki keeps three layers in one repository: raw sources that are never edited, wiki pages that an AI agent writes from those sources, and a schema that says how the work is done. The pages are plain markdown, which suits an agent and tires a person. This app is the person's view. A Python script reads the index, the log and every wiki page, turns the markdown into HTML, rewrites each link so it works inside the page, and packs the lot into one HTML file with no server behind it. In the browser you get the index on the left and the page on the right, a search box, the open questions as a checklist, and a list of the pages Bob has not yet read. The file is a snapshot. It shows the repository as it stood when it was built, and it says when that was.

## Four questions to carry with you

1. Why must every fact on a wiki page come from a source page?
2. What does "not yet read by Bob" tell you about a page?
3. Why is the app rebuilt after each ingest instead of reading the repository live?
4. When two sources disagree, what does the wiki do?

The answers are at the end. Try them first.

## On one page

{{fig:layers}}

The repository runs like a filing office with a strict clerk. Bob puts a source into `raw/`: an article, an app summary, a note in his own words. The source is never edited after that, and `raw/MANIFEST.csv` records a SHA-256 hash of every file so a change would show. When Bob says "ingest", the agent reads the whole source, writes one source page that lists the claims worth keeping with their numbers, and then updates every concept and entity page the source touches. A sentence that states a fact ends with a link to the source page it came from. Where two sources disagree, both are stated and the disagreement goes into the open questions; nobody picks a winner by taste. The index and the log are updated on every pass, and `tools/lint.py` must report zero errors before the work stops. A page carries `reviewed: no` until Bob has read it.

This app is how you look at all of that. `tools/build_app.py` turns the repository into one HTML file, which runs as a Claude artifact and as a plain page on Netlify. Today it holds {{c:pages}} wiki pages built from {{c:ingested}} ingested sources, with {{c:open}} open questions and {{c:unreviewed}} pages Bob has not yet read.

## A question with three answers

When did SWMM 5 get the Preissmann slot? One of Bob's articles says build 5.1.013 came out around 2012. Another quotes EPA's own update notes, which date 5.1.013 to 10 May 2018 and say it added the SLOT option. A third lists it under 2018 too. A notebook would keep whichever answer was written last. This wiki keeps all three, cites each one, and files the disagreement as question Q01, with a note that the primary document supports 2018.

That one example carries the whole method. Nothing goes in without a source. When sources disagree, the disagreement goes on the record, and a primary document (an EPA update log, a program listing, a test run) outranks a recollection or an AI-written passage. Bob or a better source settles it, and the page says which.

## What it is

The app is a reader for that record. It is not the wiki itself; the wiki is the folder of markdown files in the repository. The app is a printed copy that you can search, made fresh after each ingest, with the date on the cover.

## How it works

### The ingest

{{fig:ingest}}

Everything in the app comes out of the ingest, so start there. The schema in `CLAUDE.md` sets the steps. The agent reads the whole source, never just its title. It writes a source page named `S` plus a number. It updates five to fifteen other pages, sets each one's `updated:` date and adds the source to its `sources:` list. It copies numbers as the source gives them, with the unit and what they were measured on, and where the source is metric it gives US customary first. It writes a contradiction into `wiki/open-questions.md` as an unticked item. It updates `index.md`, appends to `log.md`, and runs the manifest and the linter. When Bob answers a question in a session, the answer goes into `raw/notes/` in his words first and is ingested like any other source, so even his word has a citation.

### The build

{{fig:build}}

`tools/build_app.py` does five jobs. It reads the front matter of every page: title, type, dates, the `reviewed:` line and, for a source page, the raw file it digests. It renders the markdown to HTML with Python-Markdown. It rewrites every link. It reads the index to get the groups for the left rail, and the open questions page to get the checklist. It counts the raw files by status from `raw/MANIFEST.csv`. Then it writes everything as one block of JSON into an HTML template and saves two copies: a full document for Netlify and a body-only copy for a Claude artifact. Today's file is {{c:mb}} MB.

### Links and search

{{fig:links}}

The wiki's links are relative paths written for GitHub and Obsidian. Inside a single page those paths lead nowhere, so the build resolves each one. A link to another wiki page becomes a jump inside the app. A link to a raw file becomes a link to that file on GitHub, because the raw files are not inside the app. A link to anywhere else opens in a new tab. For a page about an app, the build reads the `links:` line of the app's own summary and puts buttons at the top of the page, Netlify first.

Search is plain arithmetic. A page is a hit only if every word you typed appears in it. Its score is the number of times the words appear in the text, plus 20 for each word that appears in the title. The title bonus is large on purpose: if you type the name of a thing, the page about that thing should come first, not the page that mentions it most.

## What the numbers say

{{fig:growth}}

The log records the counts after every operation, so the growth of the wiki can be read straight from it. The wiki began on 14 November 2026. It passed one hundred ingested sources the next day, when eighteen summaries of Bob's Replit apps went in at once.

{{fig:folders}}

The raw folders are not equally done. The app summaries are nearly all ingested. The LinkedIn articles are mostly still queued, and so are the EPA manuals, which are read a chapter at a time. The index lists the suggested order for the next batches.

## What was checked

These checks were run on the build of {{built}}. The linter reported zero errors. Every page listed in the index resolved to a page in the app, and no link between wiki pages was left pointing at a file. The page was opened in a headless Chromium at 1,366 by 900 pixels and at 390 by 844: the home page, a source page, an app page, the open questions, the review list, a search and this Doc tab, some in the dark theme and some in the light. Nothing scrolled sideways, and the only console errors were the web fonts, which the test machine could not reach. A search for "Preissmann slot" returned the concept page first.

## What this does not show

{{fig:review}}

Most of what you read here has not been read by a person. Of {{c:pages}} pages, {{c:unreviewed}} say `reviewed: no` and {{c:changed}} more carry text added after Bob read them. Until he reads a page, it is the agent's reading of the sources, checked by machine and not by judgment.

The app is a snapshot. Anything ingested after the build date is not in it until it is built again.

Most of Bob's apps now live on Netlify, but a Netlify address appears in the sources for only {{c:netlify}} of them, so most app pages still point to Replit or to a Claude artifact. The fix is a source that names the addresses, not a guess in the app.

The ticks on the To review tab stay in the browser that made them. They reach the repository only when you copy the list and give it to Claude.

Search matches words, not meanings. A search for "slot" finds the slot; a search for "pressurized flow" finds only pages that use those words.

The app does not hold the raw files and does not answer questions. For a question, ask Claude, which reads the index and the pages and answers with citations.

## How to use it

1. Start on the Read tab. The index on the left follows `index.md`; type in the filter box to narrow it.
2. Click any `S` number in a page to open the source page behind a claim. The raw file is one more click, on GitHub.
3. Use Search when you know a word but not the page. Every word must appear.
4. Use Open questions to see what is still in dispute. Filter by section or by a word.
5. Use To review to work through the pages you have not read. Tick each one, then copy the list and paste it to Claude, and the pages get their `reviewed:` date.
6. After an ingest, ask Claude to rebuild the app. The same artifact link updates in place; the `.html` file goes to Netlify.

## AI use

This app was built with Claude, Anthropic's AI model, in a Claude session on 15 November 2026, at Robert Dickinson's direction. He chose to have a reader for the wiki and decides what goes into the wiki and what is settled; responsibility for the work is his. Claude wrote `tools/build_app.py`, the page template, this essay and its figures, and the `.docx` made from it, and it wrote or updated every wiki page from the raw sources. Many app summaries in `raw/apps/` were written by Replit Agent inside each Replit project and say so. The checks are mechanical: the linter, the link check in the build, and the browser screenshots listed above. No person has yet read most of the wiki pages; the To review tab lists them.

## Answers

1. **Why must every fact come from a source page?** So that it can be checked. A cited sentence leads in two clicks to the raw file it came from, and the raw file cannot have changed because its hash is in the manifest. A fact with no source would be the agent's memory, and the agent's memory is exactly what the wiki is built to replace.
2. **What does "not yet read by Bob" tell you?** That the page is the agent's reading of the sources, checked by machine but not by the person whose work it describes. Treat it as a careful first draft. When Bob reads it, the line becomes the date he read it.
3. **Why rebuild instead of reading the repository live?** A Claude artifact may not fetch from GitHub, and one file with everything inside works anywhere, Netlify included, with no server. The price is that the file is a snapshot, which is why it shows the date it was built.
4. **When two sources disagree?** The wiki states both, cites both, says which is the primary document, and adds an unticked item to the open questions. Only a source that settles it, or Bob, ticks the item, and the item then says which.

## How complex is it?

{{complexity}}
