---
title: "ICM + InfoDrainage KCS Catalog (app)"
type: entity
updated: 2026-11-17
sources: [S205, S245]
tags: [apps, icm, infodrainage, support-articles, kcs]
reviewed: no
---
Bob's app ICM + InfoDrainage KCS Catalog: a finder for 183 Autodesk support articles on InfoWorks ICM (101) and InfoDrainage (82), plus an audit that grades 77 April 2024 ICM article titles against five KCS title gates and proposes 2026 titles. Neither data set is connected to the live knowledge base. Version 2026.5, 2026-11-06 [S245](../sources/S245-icm-kcs-catalog-2026-summary.md). Netlify address: https://icm-kcs-catalog.netlify.app [S205](../sources/S205-note-netlify-addresses.md).

**A caution about its source.** The page ships no technical summary. [S245](../sources/S245-icm-kcs-catalog-2026-summary.md) was written by Claude on 17 November 2026 from the page, with nothing rerun, and Bob has not yet read it (Q108).

**What the summary says** [S245](../sources/S245-icm-kcs-catalog-2026-summary.md)
- Five gates from the KCS field guide: at most 69 characters; names ICM; one of three patterns (exact error message, How to, plain problem statement); a How-to title names something the reader can do; clean.
- April 2024 titles: 38 of 77 were 70 characters or longer, the longest 153; 45 began "How to Understand". Grades: A 5, B 35, C 25, D 12. The list holds 66 published, 10 drafts and 1 archived duplicate.
- 71 proposals pass all five gates and cut the mean length over the 76 non-archived records from 80.1 to 58.2 characters.
- Search test, thirty seed questions, BM25 over 76 titles: the right article first 25 times with the 2026 titles and 28 with the 2024 titles. The worst case was the error "[RAINGAGES] or [TIMESERIES] should not be empty", whose 2026 title had cut the error words.
- Of the InfoSewer import steps, live pages were found for the Overview, Step 5 and Step 8, all carrying a legacy notice; none for Steps 1, 2, 3, 4, 6, 7 or 9.
- The finder's 183 summaries, topics and tags are ChatGPT's reading; four titles were checked against fetched pages and all four match.

**What it does not show.** Article bodies were not read, and none of the 183 summaries was checked against its article. The finder is a snapshot. View counts are April 2024's. The search test's questions were written by the same AI that wrote the proposals, and it searches titles only. The KCS field guide carries no date. [S245](../sources/S245-icm-kcs-catalog-2026-summary.md)

**Noted at ingest.** 5 + 35 + 25 + 12 = 77 and 66 + 10 + 1 = 77. A result against the app's own proposals: the shorter titles found the right article first less often than the old ones (25 against 28). Bob renamed the Netlify site from `icm-kcs` to `icm-kcs-catalog` on 17 November 2026 [S205](../sources/S205-note-netlify-addresses.md).

See [Apps summarized on 17 November 2026: ICM, data and the tools around models](../concepts/apps-from-pages-icm-and-data.md), [InfoWorks ICM](infoworks-icm.md), [InfoDrainage Explorer (app)](infodrainage-explorer.md), [InfoSewer to InfoWorks ICM (app)](infosewer-to-infoworks-icm-guide.md), [Negative results](../concepts/negative-results.md).
