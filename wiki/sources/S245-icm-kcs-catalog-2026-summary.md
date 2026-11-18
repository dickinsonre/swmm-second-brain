---
title: "S245: ICM + InfoDrainage KCS Catalog, summary written from the page (v2026.5)"
type: source
raw: raw/apps/icm-kcs-catalog-2026-v2026.5.md
kind: app-md
author: Robert Dickinson
published: 2026-11-06
ingested: 2026-11-17
tags: [apps, icm, infodrainage, support-articles, kcs]
drafted_by: Claude (Anthropic), from the published page
reviewed: no
---
**What it is.** A technical summary of the app ICM + InfoDrainage KCS Catalog, version 2026.5: a finder for 183 Autodesk support articles on InfoWorks ICM (101) and InfoDrainage (82), plus an audit that grades 77 April 2024 ICM article titles against five KCS title gates and proposes 2026 titles. Neither data set is connected to the live knowledge base. Raw file: [raw/apps/icm-kcs-catalog-2026-v2026.5.md](../../raw/apps/icm-kcs-catalog-2026-v2026.5.md).

**How it was written. A summary written from the page.** The page ships no technical summary. Claude (Anthropic) wrote this file on 17 November 2026, at Bob's request, from the published Claude artifact, version 1794013526-b46e, reading its About & sources and Doc tabs in a headless browser; nothing was run to write it. Bob has not read it (Q108). The page says the app and essay were built with Claude on 2 November 2026 and refreshed on 6 November under Bob's direction; Bob supplied the April 2024 list, the KCS field guidance and an outside review written with ChatGPT. Claude wrote all 71 proposals, the rule tests and the thirty seed questions. Version 2026.4, the 183-article finder, was built with ChatGPT (OpenAI); 2026.5 brought it into this app's source.

**Claims worth keeping** (all copied from the file)
- Five gates from the KCS field guide: at most 69 characters; names ICM; one of three patterns (exact error message, How to, plain problem statement); a How-to title names something the reader can do; clean.
- April 2024 titles: 38 of 77 were 70 characters or longer, the longest 153; 45 began "How to Understand". Grades: A 5, B 35, C 25, D 12. The list holds 66 published, 10 drafts and 1 archived duplicate.
- 71 proposals pass all five gates and cut the mean length over the 76 non-archived records from 80.1 to 58.2 characters.
- Search test, thirty seed questions, BM25 over 76 titles: the right article first 25 times with the 2026 titles and 28 with the 2024 titles. The worst case was the error "[RAINGAGES] or [TIMESERIES] should not be empty", whose 2026 title had cut the error words.
- Of the InfoSewer import steps, live pages were found for the Overview, Step 5 and Step 8, all carrying a legacy notice; none for Steps 1, 2, 3, 4, 6, 7 or 9.
- The finder's 183 summaries, topics and tags are ChatGPT's reading; four titles were checked against fetched pages and all four match.

**Limits it states.** Article bodies were not read, and none of the 183 summaries was checked against its article. The finder is a snapshot. View counts are April 2024's. The search test's questions were written by the same AI that wrote the proposals, and it searches titles only. The KCS field guide carries no date.

**Checked at ingest.** 5 + 35 + 25 + 12 = 77 and 66 + 10 + 1 = 77. A result against the app's own proposals: the shorter titles found the right article first less often than the old ones (25 against 28). Bob renamed the Netlify site from `icm-kcs` to `icm-kcs-catalog` on 17 November 2026 [S205](S205-note-netlify-addresses.md). The `links:` line gives Netlify as "not yet deployed"; Netlify reported a finished deploy at https://icm-kcs-catalog.netlify.app on 17 November 2026 [S205](S205-note-netlify-addresses.md).

**Feeds:** [ICM + InfoDrainage KCS Catalog (app)](../entities/icm-kcs-catalog-2026.md), [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [InfoWorks ICM](../entities/infoworks-icm.md), [InfoDrainage Explorer (app)](../entities/infodrainage-explorer.md), [InfoSewer to InfoWorks ICM (app)](../entities/infosewer-to-infoworks-icm-guide.md), [Negative results](../concepts/negative-results.md).
