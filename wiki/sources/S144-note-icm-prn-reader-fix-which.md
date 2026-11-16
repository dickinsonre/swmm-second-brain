---
title: "S144: Note, the PRN problem Bob fixed was the open file list (2026-11-15)"
type: source
raw: raw/notes/icm-prn-reader-fix-which-2026-11-15.md
kind: note
author: Robert Dickinson
published: 2026-11-15
ingested: 2026-11-15
tags: [apps, replit, icm, results]
reviewed: 11/16/2026
---
**What it is.** Bob's answer to which problem he fixed in his Replit app the ICM PRN File Reader. Raw file: [raw/notes/icm-prn-reader-fix-which-2026-11-15.md](../../raw/notes/icm-prn-reader-fix-which-2026-11-15.md).

**How it was written.** Bob typed the answer in a Claude session on 15 November 2026 at 17:28 Eastern time, one minute after the sentence in [S143](S143-note-icm-prn-reader-fix.md). Claude (Anthropic) copied it into a note on the template, in his words. Bob has not read the note.

**Claims worth keeping**
- The problem Bob fixed is "the file that anyone can read": the route `GET /api/prn/files`, which the summary of version 1.0.0 says returned stored files, with their content, without route-level authentication [S142](S142-icm-prn-file-reader-replit-summary.md). Status: fixed, on Bob's word.

**What is the note's reading and not Bob's words.** That his phrase names that route. That the second problem, the differing thresholds, is not yet fixed, since his answer does not mention it.

**Checked at ingest.** No new summary, rerun or change list came with the answer. The fixed version is not described here; its summary would come as a new file in `raw/apps/` under a new version number.

**Feeds:** [ICM PRN File Reader (app)](../entities/icm-prn-file-reader.md), [Open questions](../open-questions.md).
