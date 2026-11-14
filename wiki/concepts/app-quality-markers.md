---
title: Six quality markers for app-building work
type: concept
updated: 2026-11-14
sources: [S05]
tags: [apps, measurement, method]
reviewed: no
---
Six text patterns, each tested once per app-building conversation in the [Claude chat archive (app)](../entities/claude-chat-archive.md), that show whether checking happened in the transcript [S05](../sources/S05-swmm5org-article-facts.md).

Share of each quarter's app-building conversations showing the marker [S05](../sources/S05-swmm5org-article-facts.md):

| Marker | 2025Q4 | 2026Q1 | 2026Q2 | 2026Q3 |
|---|---|---|---|---|
| App conversations in the quarter | 14 | 149 | 234 | 115 |
| Runs a real engine | 29 % | 30 % | 31 % | 62 % |
| Verified against engine output | 29 % | 12 % | 28 % | 60 % |
| Reports N of N test results | 7 % | 13 % | 24 % | 72 % |
| Found a defect | 0 % | 7 % | 23 % | 47 % |
| Went through review rounds | 0 % | 16 % | 15 % | 27 % |
| Produced a negative result | 0 % | 11 % | 12 % | 15 % |

**What the sheet says the numbers support** [S05](../sources/S05-swmm5org-article-facts.md)
- Verification about doubled between 2026Q2 and 2026Q3 while the monthly app count fell by about two thirds from the May peak.
- N of N reporting moved most.
- Review rounds moved least, because few people are available to review the work.

**Cautions the sheet itself gives** [S05](../sources/S05-swmm5org-article-facts.md)
- A marker is evidence of discipline in the transcript. It does not show the app is correct.
- 2025Q4 holds only 14 conversations. The 2026Q1 dip in verification is small-sample noise; do not claim a steady rise.
- The patterns must be published with the numbers. A first "found a defect" pattern read 73 % for 2026Q3 and the tightened one 47 %; an older workbook's 65 % cannot be reproduced.
- A second channel matters: tool calls that ran an engine are invisible to a text search. That channel alone found 268 conversations; 87 compiled an engine and 142 ran a test script.

See [Negative results](negative-results.md), [Continuity is not validation](continuity-is-not-validation.md), [The SWMM findings register](findings-register.md), [App build contract (four working principles)](app-build-contract.md).
