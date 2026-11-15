---
title: SWMM version history, 1969 to 2026
type: concept
updated: 2026-11-15
sources: [S01, S07, S11, S12, S19, S20, S21, S22, S55, S60, S63, S86, S126]
tags: [swmm-history, timeline]
reviewed: 2026-11-15
changed_after_review: "2026-11-15 (second Replit ingest): one paragraph added at the end, headed Added 15 November 2026, on the SWMM Ecosystem app (S126)"
---
The timeline as the ingested sources give it. Where two sources differ, both are shown.

| When | What | Source |
|---|---|---|
| 1969 to 1971 | SWMM begins as an EPA project with Metcalf & Eddy, the University of Florida and Water Resources Engineers | [S07](../sources/S07-swmm5org-topic-swmm-history.md), [S01](../sources/S01-swmm1-engine-app-md.md) |
| 1969 | First version cost $350,000 | [S21](../sources/S21-li-edition-56-swmm-history.md) |
| July to October 1971 | Four report volumes, EPA 11024 DOC 07/71 to 10/71; Volume IV is the program listing | [S01](../sources/S01-swmm1-engine-app-md.md) |
| 1975 | SWMM 2 | [S21](../sources/S21-li-edition-56-swmm-history.md) |
| 1977 to 1980 | Bob runs SWMM on punch cards; SWMM 2.5 and SWMM 3 fill ten boxes | [S19](../sources/S19-li-edition-29-engine-speed.md) |
| 1978 | [William (Bill) James](../entities/william-james.md) and Mark Robinson teach a SWMM 2 class at the University of Florida; thirty students run it on a Boeing mainframe in Seattle through one modem | [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md) |
| 1978 | Bob begins work on SWMM itself, starting with SWMM 2.5 | [S07](../sources/S07-swmm5org-topic-swmm-history.md) |
| November 1981 | SWMM 3 User's Manual (Huber, Heaney, Nix, Dickinson, Polmann) | [S19](../sources/S19-li-edition-29-engine-speed.md) |
| 1981 | EXTRAN 3 test model, later SWMM 5's Extran1.INP | [S19](../sources/S19-li-edition-29-engine-speed.md) |
| 1981 | CDM publishes the Extran manual, with 7 test files | [S55](../sources/S55-swmm-brain-readme.md) |
| 1983 | PCSWMM becomes available; Bob is one of its first users (see Q31) | [S63](../sources/S63-li-edition-53-measure-of-honest-numbers.md) |
| August 1988 | SWMM 4 User's Manual (Huber and Dickinson) and EXTRAN Addendum (Roesner, Aldrich, Dickinson) | [S19](../sources/S19-li-edition-29-engine-speed.md) |
| 1988 to 2004 | No major version for sixteen years | [S21](../sources/S21-li-edition-56-swmm-history.md) |
| 1969 to 1992 | Years the article gives for SWMM development at Black Hall, University of Florida | [S12](../sources/S12-li-diamond-village.md) |
| Late 2000 | Bob joins CDM | [S11](../sources/S11-li-my-history-with-swmm.md) |
| 2001 | EPA and CDM sign the CRADA to rewrite SWMM | [S21](../sources/S21-li-edition-56-swmm-history.md) |
| October 2003 | WEFTEC paper, "Redevelopment of the US EPA Stormwater Management Model" | [S19](../sources/S19-li-edition-29-engine-speed.md) |
| 2004 | SWMM 4.4H Fortran source, kept at SWMMEnablement/WCH_2004_SWMM44H | [S07](../sources/S07-swmm5org-topic-swmm-history.md) |
| 29 October 2004 | SWMM 5.0 build 001, in C | [S22](../sources/S22-li-ten-problems.md), [S21](../sources/S21-li-edition-56-swmm-history.md) |
| 2005 | 5.0.005, first FEMA-approved version | [S21](../sources/S21-li-edition-56-swmm-history.md) |
| 2010 | 5.0.019, LID controls | [S21](../sources/S21-li-edition-56-swmm-history.md) |
| 21 April 2011 | 5.0.022 | [S22](../sources/S22-li-ten-problems.md) |
| 24 March 2014 | 5.1.001 | [S22](../sources/S22-li-ten-problems.md) |
| 2015 to 2017 | Reference manuals for hydrology, water quality and hydraulics; hydraulics in May 2017 | [S22](../sources/S22-li-ten-problems.md) |
| 10 May 2018 | 5.1.013, adds the SLOT surcharge option | [S22](../sources/S22-li-ten-problems.md) |
| 1 February 2022 | 5.2.0 | [S22](../sources/S22-li-ten-problems.md) |
| 2023 | 5.2.4, the current stable release | [S21](../sources/S21-li-edition-56-swmm-history.md) |

There were 42 builds of SWMM 5 from 5.0.001 to 5.2.4 [S22](../sources/S22-li-ten-problems.md).

**EPA's own summary** (Table 1-1 of the hydraulics reference manual) [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)

| Version | Year | Contributors | What it added |
|---|---|---|---|
| SWMM I | 1971 | Metcalf & Eddy, Water Resources Engineers, University of Florida | First version; focus on combined sewer overflows |
| SWMM II | 1975 | University of Florida | First widely distributed version |
| SWMM 3 | 1981 | University of Florida, Camp Dresser & McKee | Full dynamic wave routine, Green-Ampt infiltration, snow melt, continuous simulation |
| SWMM 3.3 | 1983 | US EPA | First PC version |
| SWMM 4 | 1988 | Oregon State University, Camp Dresser & McKee | Groundwater, RDII, irregular channel cross-sections, over a series of updates through the 1990s |
| SWMM 5 | 2005 | US EPA, CDM-Smith | Complete rewrite in C, graphical interface, LID |

**After SWMM 5.** Four lines move forward separately: SWMM5+ at CIMM, OpenSWMM 6 at HydroCouple, EPA's 5.2 line and the vendor engines. They share no common test models and no shared definition of "agrees with SWMM5" [S22](../sources/S22-li-ten-problems.md).

**Disagreements** (all in [Open questions](../open-questions.md))
- Q02, settled: EPA's table gives Water Resources Engineers, not Camp Dresser & McKee, for SWMM I [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md).
- Q14, settled: EXTRAN and the dynamic wave routine arrived with SWMM 3 in 1981 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md), not with SWMM 2 as [S21](../sources/S21-li-edition-56-swmm-history.md) says.
- Q31 and Q32, new: EPA's table dates the first PC version to SWMM 3.3 in 1983 and SWMM 5 to 2005 [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md); other sources say 1988 and October 2004.
- Q01. [S20](../sources/S20-li-edition-54-two-solvers.md) dates 5.1.013 to "around 2012".
- Q06. Bob's own start dates differ between articles: first model run in 1974 [S55](../sources/S55-swmm-brain-readme.md), punch cards from 1977 [S19](../sources/S19-li-edition-29-engine-speed.md), on SWMM itself since 1978 [S07](../sources/S07-swmm5org-topic-swmm-history.md).
- Q29. Bob's years at Innovyze: from 2005 [S55](../sources/S55-swmm-brain-readme.md) or from January 2008 [S11](../sources/S11-li-my-history-with-swmm.md).

Pages for the versions: [SWMM 1 (1971)](../entities/swmm-1.md), [EXTRAN](../entities/extran.md), [EPA SWMM 5](../entities/swmm-5.md), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md). Cited once here: [S20](../sources/S20-li-edition-54-two-solvers.md).

**Added 15 November 2026.** On the manuals themselves, from the [Master SWMM PDF (app)](../entities/master-swmm-pdf.md) essay [S86](../sources/S86-master-swmm-pdf-page-text.md): SWMM's EPA user's manuals are dated 1971, 1975, 1981 and 1988, each an edited descendant of the one before. The 1988 manual was printed twice; the October 1992 second printing changed the title page, the disclaimer, the preface and pages 23, 28 to 32, 124, 220 to 221 and 375 to 377a, and its new preface sends readers to `.DOC` files on the distribution disks for options the book never described. This is the first source here with something dated 1992, which bears on Q17. The essay is AI-written and its citations have not been checked by a person. On SWMM 4.4H's three hydraulic solvers see [EXTRAN's three solvers: XROUTE, YROUTE, ZROUTE](extran-solvers-xroute-yroute-zroute.md).

**Added 15 November 2026: an app on this subject.** [SWMM Ecosystem (app)](../entities/swmm-ecosystem.md) catalogs 51 programs. Its summary says its historical claims were not checked against outside sources, and nothing from it is used above [S126](../sources/S126-swmm-ecosystem-replit-summary.md).
