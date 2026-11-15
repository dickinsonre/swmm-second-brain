

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
