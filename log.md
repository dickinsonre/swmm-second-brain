

## [2026-11-15] ingest | S90, SWMM anecdotes from the comments on a LinkedIn post

Bob pasted the comment thread under one of his LinkedIn posts and said it might be good to add as anecdotes of SWMM. Claude typed `raw/notes/swmm-anecdotes-linkedin-comments-2026-11.md` from the paste: Bob's four comments, and the sentences of seven other people that recall SWMM or their own modeling work, word for word under the names they were posted under. Left out because the repository is public: comments that only congratulate, remarks about anyone's family or private life, job titles, reaction counts. The post itself was not in the paste.

Pages created (2, `reviewed: no`): S90; Anecdotes of SWMM, a concept page under History meant to collect more of these. Pages changed: Robert (Bob) Dickinson (one added paragraph; already marked changed after review), the overview (one bullet, counts), open questions, `index.md`, `README.md`.

Found:
- Q06, extended: the LinkedIn headline says "SWMM since the 1977", one more start date.
- Q64, new: the note waits for Bob's read; the post, the year of the Australian stay for the XP-EXTRAN update, and what the "double pipes" were are not in the sources; and whether other people's quoted comments should stay is his to decide.
- No contradiction with an existing page. The wiki had nothing on John Haestad, Jack Cook, Canberra, the Prime mainframe, the phosphate plant or DUFLOW before this note.

After this ingest: 333 raw files, 90 ingested, 239 queued, 1 superseded, 3 duplicate. 188 wiki pages: 90 sources, 50 concepts, 46 entities, overview, open questions. 61 questions open, 3 settled. 6 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-swmm-anecdotes`.

## [2026-11-15] setup | Branch `ingest-swmm-anecdotes` merged into main

Bob said "merge". Main had not moved since `5b20417`, so the merge is a fast-forward. It brings in S90, the Anecdotes of SWMM page, the addition to the Robert Dickinson page, the extension of Q06 and the new Q64. Nothing else changed. Q64 stays open: the post's text, date and link, the year of the Australian stay, and what the "double pipes" were.

## [2026-11-15] ingest | S91, Bob's answers to Q64

Bob answered the three gaps of Q64 in a Claude session. Claude copied his answers into `raw/notes/q64-answers-canberra-barrels-post-link.md` in his words and ingested the note. The post is https://lnkd.in/p/e8TVNFQZ, "from yesterday" (14 November 2026). The stay in Canberra ran "from november 1991 to december 1992". "double pipes are called barrels in swmm5 - i guess i added them to swmm4".

Page created (1, `reviewed: no`): S91. Pages changed: Anecdotes of SWMM, Robert (Bob) Dickinson (the paragraph added earlier today extended; its wording "to SWMM 3" corrected, because S90 does not say which version the double pipes went into), S90 (one pointer to S91), the overview (one bullet extended, counts; its stale count of open items corrected from fifty-nine to sixty-two), open questions, `index.md`, `README.md`.

Found:
- Q64, settled in part, not ticked. Still open: the text of the post (LinkedIn refused an automated fetch), whether "XSWMM" is XP-SWMM, and Bob's read of both notes.
- Q65, new, under "Sources that disagree": Weaver's comment places the double pipes in the SWMM 3 years; Bob guesses SWMM 4. A text search of the queued manuals finds a BARREL field in the Transport Block card data of the SWMM 3 manual and in SWMM 4.4 TRANS.doc, and no "barrel" in EXTRAN44.doc. Those files are not ingested, so the search is recorded in Q65 as a pointer and not as a wiki claim.
- Checked: November 1991 to December 1992 is 13 to 14 months, against "one year" in S90. Not a conflict.

After this ingest: 334 raw files, 91 ingested, 239 queued, 1 superseded, 3 duplicate. 189 wiki pages: 91 sources, 50 concepts, 46 entities, overview, open questions. 62 questions open, 3 settled. 7 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] ingest | S92, Bob's answer to Q65

Shown what the text search of the queued manuals had found, Bob answered: "transport is not extran so barrels were added later =- not a big matter". Claude copied it into `raw/notes/barrels-transport-is-not-extran.md` in his words and ingested the note.

Page created (1, `reviewed: no`): S92. Pages changed: Anecdotes of SWMM, open questions, the overview (counts), `index.md`, `README.md`.

Q65 ticked, on Bob's word: the BARREL field of the SWMM 3 Transport block is not the double pipes of the anecdote; those were barrels in Extran, added later. The version stays his guess of SWMM 4 (page rule 5: a guess is not upgraded).

After this ingest: 335 raw files, 92 ingested, 239 queued, 1 superseded, 3 duplicate. 190 wiki pages: 92 sources, 50 concepts, 46 entities, overview, open questions. 61 questions open, 4 settled. 8 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] ingest | S93, the name XP-SWMM and its change to XPSWMM in 1993

Bob typed: "xp-swmm was the original and we changed it to xpswmm in 1993". Claude copied it into `raw/notes/xp-swmm-renamed-xpswmm-1993.md` in his words and ingested the note.

Page created (1, `reviewed: no`): S93. Pages changed: Anecdotes of SWMM (one sentence; two sentences cut to keep the page under 600 words), Robert (Bob) Dickinson (one sentence in the paragraph added today), open questions (Q64 extended), the overview (counts), `index.md`, `README.md`.

Q64 stays open for two things: the text of the LinkedIn post, and Bob's read of the four notes Claude typed today (S90 to S93). That "XSWMM" in his comment is this program is Claude's reading of his answer, and is marked so.

Checked: his 2016 article (S11) writes both "XP-SWMM" and "XPSWMM"; no other source dates the change.

After this ingest: 336 raw files, 93 ingested, 239 queued, 1 superseded, 3 duplicate. 191 wiki pages: 93 sources, 50 concepts, 46 entities, overview, open questions. 61 questions open, 4 settled. 9 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] ingest | S94, Bob's LinkedIn post of 14 November 2026

Bob pasted the text of the post that the comments in S90 answer. It is a post, not an article, so it was not in the LinkedIn export. Claude copied the paste into `raw/linkedin/2026-11-14-post-my-earlier-history-with-swmm.md` without changing a word and ingested it. The file holds the post as Bob published it. By page rule 9 the wiki carries only what bears on SWMM: he learned about SWMM at 17, started working on it at 22, and "SWMM 2.5 was 20,000 punch cards".

Page created (1, `reviewed: no`): S94. Pages changed: Anecdotes of SWMM (one anecdote added, five sentences cut to keep the page near 600 words), Robert (Bob) Dickinson (one sentence in the paragraph added today), open questions, the overview (one bullet, counts), `index.md`, `README.md`.

Found:
- Q64 ticked, on Bob's answers and the post itself. His read of S90 to S94 is tracked by `reviewed: no`.
- Q06 extended: age 22, with "75 in 2030" from S89, puts his start on SWMM between 1976 and 1978.
- Q66, new: 20,000 cards for SWMM 2.5 (S94) against ten boxes for SWMM 2.5 and SWMM 3 together (S19). No source gives cards per box.

After this ingest: 337 raw files, 94 ingested, 239 queued, 1 superseded, 3 duplicate. 192 wiki pages: 94 sources, 50 concepts, 46 entities, overview, open questions. 61 questions open, 5 settled. 10 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] ingest | The post corrected ("Since"), and S95, a box held 2,000 cards

Two answers from Bob.

"ince should be since". Raw files are never edited, so the corrected text went in beside the first file as `raw/linkedin/2026-11-14-post-my-earlier-history-with-swmm-corrected.md`, with that one letter restored and its own account of how it was made. S94 now names the corrected file as its raw file. The as-pasted file stays, is listed as queued, and is not to be ingested; `index.md` says so.

"i remember it was 2000 - i remember as it was importat", on how many cards a box held. Claude copied it into `raw/notes/punch-card-box-held-2000-cards.md` in his words and ingested it.

Page created (1, `reviewed: no`): S95. Pages changed: S94, Anecdotes of SWMM, open questions, the overview (counts), `index.md`, `README.md`.

Found:
- Q66 ticked, on Bob's word: ten boxes of 2,000 cards are 20,000 cards, so his post (S94) and his 2024 article (S19) agree.
- A slip of Claude's corrected: S94 and Q66 had the article saying the two programs "together filled" ten boxes. The article's words are "SWMM 2.5 and SWMM 3 were in ten boxes".

After this ingest: 339 raw files, 95 ingested, 240 queued (one of them the as-pasted post, kept on purpose), 1 superseded, 3 duplicate. 193 wiki pages: 95 sources, 50 concepts, 46 entities, overview, open questions. 60 questions open, 6 settled. 11 pages not yet reviewed; 27 changed since Bob's review. Work is on branch `ingest-q64-answers`.

## [2026-11-15] setup | Bob's decision on the post in `raw/`

Asked whether the full text of his post of 14 November 2026, including what it says about his family, should sit in this public repository's `raw/` folder, Bob answered: "all public". The post stays in `raw/` as he published it. Page rule 9 is unchanged: the wiki still carries only what bears on SWMM.

## [2026-11-15] setup | Branch `ingest-q64-answers` merged into main

Bob said "merge". Main had moved: between 8:27 and 8:30 that morning Bob marked six pages reviewed (Orifices, Pumps and pump curves, Weirs and outlets, SWMM 5 network objects, Anecdotes of SWMM, S90) and cleared the `changed_after_review:` line on 27 pages. His commits were merged into the branch first, then main was fast-forwarded.

Three conflicts, all in front matter, all resolved the same way: his `reviewed:` dates kept, and a new `changed_after_review:` line listing only what the branch changed after his review. Five reviewed pages carry such a line: Anecdotes of SWMM, S90, Robert (Bob) Dickinson, open questions, the overview. On the Anecdotes page the changes are in place, not in a separate "Added" paragraph, because the page was `reviewed: no` when they were written; the line lists each one.

The merge brings in S91 to S95, the corrected copy of the post beside the as-pasted one, and the ticks on Q64, Q65 and Q66.

After the merge: 339 raw files, 95 ingested, 240 queued (one of them the as-pasted post, kept on purpose), 1 superseded, 3 duplicate. 193 wiki pages. 60 questions open, 6 settled. 5 pages not yet reviewed (S91 to S95); 5 changed since Bob's review.

## [2026-11-15] raw | 17 app summaries brought over from Bob's Replit workspace

Bob ran the summary prompt in Replit Agent on his projects and could not download the files. At his request the agent read each file out of the Replit editor through his browser and wrote it to `raw/apps/`. Each copy was checked against a SHA-256 computed inside Replit on the editor's text: all 17 match, and those hashes are the ones in `raw/MANIFEST.csv`.
Files: bob-swmm-info-v1.0.0, data-importer-robertdickinson-v1.0.0, fractal-swmm-gen--robertdickinson-v1.0.0, green-infiltration-v1.0.0, horton-model--robertdickinson-v1.0.0, singa-pour-site-v1.0.0, spatial-impact-insight-v2.4.1_b, swmm-5-inp-reader-robertdickinson-v0.1.0, swmm-filebase--robertdickinson-v1.0.0, swmm-inp-maker-v1.0.0, swmm-lego-model-v0.0.0, swmm-manual-search-robertdickinson-v5.2, swmm-pilot-robertdickinson-v1.0.0, swmm-ui-engine-v1.0.0, temp-monitor-1-v1.0.0, video-search-v1.0.0, xps-to-shape--robertdickinson-v0.1.0.
Every one says in its body that Replit Agent wrote it on 15 November 2026 and that Bob has not reviewed it. None is ingested yet; all are queued.
Held back, not committed: sewer-code-search-v1.0.0 (the app is a private deployment; waiting for Bob's say before it goes into a public repository).
No summary found in two projects, where Replit Agent stopped and asked to switch to its paid Power mode: EPANET SWMM Experts and SWMM Explorer.
