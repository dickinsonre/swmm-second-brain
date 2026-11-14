---
title: Open questions
type: synthesis
updated: 2026-11-14
sources: [S01, S04, S05, S07, S08, S11, S12, S14, S19, S20, S21, S22, S23]
tags: [lint, contradictions]
reviewed: no
---
Contradictions, doubtful numbers and gaps found while ingesting and linting. An item is ticked only when a source or Bob settles it, with a note saying which. Newest at the bottom of each section.

## Sources that disagree

- [ ] Q01 (2026-11-14): When did SWMM 5 get the Preissmann slot? [S20](sources/S20-li-edition-54-two-solvers.md) says build 5.1.013 was "released around 2012". [S22](sources/S22-li-ten-problems.md) cites EPA's update notes: 5.1.013 is dated 10 May 2018 and added the SLOT option. [S21](sources/S21-li-edition-56-swmm-history.md) also lists 5.1.013 under 2018. The primary document supports 2018; [S20](sources/S20-li-edition-54-two-solvers.md) looks like the error. A queued article of 1 March 2019, [New Engine and GUI Features in InfoSWMM 14.7 which is based on EPA SWMM 5.1.013](../raw/linkedin/2019-03-01-new-engine-gui-features-infoswmm-147-which-based-epa-swmm-dickinson.md), shows the Slot option and fits 2018.
- [ ] Q02 (2026-11-14): Who built SWMM 1? [S21](sources/S21-li-edition-56-swmm-history.md): the University of Florida, Camp Dresser & McKee and Metcalf & Eddy. [S01](sources/S01-swmm1-engine-app-md.md), from the 1971 report itself, and [S07](sources/S07-swmm5org-topic-swmm-history.md): Metcalf & Eddy, the University of Florida and Water Resources Engineers. The report supports the second.
- [ ] Q05 (2026-11-14): Who led the SWMM 5 CRADA work? [S21](sources/S21-li-edition-56-swmm-history.md) says both that Bob was "leading the CRADA that produced SWMM 5" and that "the CDM Smith CRADA team was led by Ted Burgess and had Robert E. Dickinson". The 2008 announcement quoted in [S11](sources/S11-li-my-history-with-swmm.md) calls Bob "the principal developer" of SWMM5, while [S21](sources/S21-li-edition-56-swmm-history.md) and [S22](sources/S22-li-ten-problems.md) name Lew Rossman as architect and author of the engine. Bob to supply the wording he wants used.
- [ ] Q06 (2026-11-14): Bob's start dates. [S21](sources/S21-li-edition-56-swmm-history.md): "inside this story since 1980" and "working with EPA SWMM since 1978". [S07](sources/S07-swmm5org-topic-swmm-history.md): went to Florida in 1973, on SWMM itself since 1978. [S19](sources/S19-li-edition-29-engine-speed.md): punch cards from 1977 to 1980; an undergraduate at Black Hall in 1974. The anniversary counts in [S11](sources/S11-li-my-history-with-swmm.md) were updated in 2013, 2018 and 2023 and do not share one base year. One dated list from Bob would replace all of these.
- [ ] Q08 (2026-11-14): The review of the Rust engine `hydra`. Register entry F-0008 in [S04](sources/S04-findings-register-seed.md) counts twelve source-level defects, all confirmed. [S05](sources/S05-swmm5org-article-facts.md) lists "23 documented deviations from SWMM5 in the Rust hydra engine". One review counted two ways, or two reviews?
- [ ] Q12 (2026-11-14): Is SWMM 5's dynamic wave solution implicit or explicit? [S20](sources/S20-li-edition-54-two-solvers.md) calls the EXTRAN lineage "implicit backward Euler time integration" with successive relaxation. [S08](sources/S08-swmm5org-topic-inside-swmm5.md) lists an app on "why SWMM5's explicit dynamic wave solution stays robust" and a 2013 post on successive under-relaxation. The 2013 post and the 2006 QA report, both listed in [S08](sources/S08-swmm5org-topic-inside-swmm5.md) but not in raw, should settle the wording.
- [ ] Q13 (2026-11-14): [S20](sources/S20-li-edition-54-two-solvers.md) calls SWMM 5 "the only platform with built in LID and water quality modeling". Queued articles by Bob have titles on SUDS and LID usage in ICM InfoWorks, and on buildup and washoff in ICM InfoWorks. Ingest those and correct the comparison table.
- [ ] Q14 (2026-11-14): When did EXTRAN enter SWMM? [S21](sources/S21-li-edition-56-swmm-history.md) says SWMM 2 (1975) added it. [S20](sources/S20-li-edition-54-two-solvers.md) calls it a module "of the original EPA Storm Water Management Model". The October 1971 listing has no EXTRAN block [S01](sources/S01-swmm1-engine-app-md.md). [S21](sources/S21-li-edition-56-swmm-history.md) is the only dated statement and its history rests on AI searching by its own account.

## Arithmetic and wording to check

- [ ] Q03 (2026-11-14): [S19](sources/S19-li-edition-29-engine-speed.md) gives 1 January 1988 to 1 January 2024 as 324,360 hours and the speed ratio as 54,060. That span is 13,149 days, or 315,576 hours, which gives 52,596. The article's figure equals 37 years of 8,760 hours plus 240 hours.
- [ ] Q04 (2026-11-14): [S19](sources/S19-li-edition-29-engine-speed.md) says "ICM AT" in five places and "IBM PC AT" in section 6; [S22](sources/S22-li-ten-problems.md) repeats "ICM AT". Presumably the IBM PC AT throughout.
- [ ] Q07 (2026-11-14): [S14](sources/S14-li-subarea-routing.md), section 5, is captioned "Impervious in SWMM, Impervious to Pervious in InfoWorks". Section 1 of the same article defines IMPERV as pervious runoff draining to the impervious area. Which pairing did the test networks use? The screenshots that would show it are not in the export.
- [ ] Q15 (2026-11-14): [S21](sources/S21-li-edition-56-swmm-history.md) says SWMM 5 "has evolved through eight significant releases" and its table has seven dated rows; it also says "four universities" without naming them.
- [ ] Q09 (2026-11-14): [S07](sources/S07-swmm5org-topic-swmm-history.md) describes the SWMM 1 Engine app as "the 1971 SWMM 1 Runoff engine"; since version 2.0 it runs all five blocks [S01](sources/S01-swmm1-engine-app-md.md). [S07](sources/S07-swmm5org-topic-swmm-history.md) links the app on Netlify, while [S01](sources/S01-swmm1-engine-app-md.md) records `netlify: none`. One of the two needs updating.

## Open inside a single source

- [ ] Q10 (2026-11-14): Baker Street pollutant loads. The 1971 print is far above the listing's result, and removing the division at card `TRAN346` explains the peak hours only; hours 0:15, 4:55 and 6:05 are not reproduced [S01](sources/S01-swmm1-engine-app-md.md).
- [ ] Q11 (2026-11-14): Baker Street dry-weather flow. Figure 2-5 of Volume II gives 2.70 cfs; the rebuilt deck gives 2.51 cfs; not reconciled [S01](sources/S01-swmm1-engine-app-md.md).
- [ ] Q16 (2026-11-14): Do the SWMM and ICM comparison numbers in [S20](sources/S20-li-edition-54-two-solvers.md) (peaks within 2 to 3 %, the two continuity bands, the force main flows) come from runs of the two engines or from the app's own calculators? The article cites no run.
- [ ] Q17 (2026-11-14): [S12](sources/S12-li-diamond-village.md) says SWMM was developed at Black Hall "between 1969 and 1992". What ended in 1992? The SWMM 4 manual is dated 1988 [S19](sources/S19-li-edition-29-engine-speed.md).

## Gaps to decide

- [ ] Q18 (2026-11-14): The 14 faults found in the 1971 SWMM 1 listing [S01](sources/S01-swmm1-engine-app-md.md) have no findings-register IDs. The seed's next free number is F-0015 [S04](sources/S04-findings-register-seed.md). Bob to say whether they get numbers.
- [ ] Q19 (2026-11-14): Several source pages could not say which AI tool wrote which passages ([S11](sources/S11-li-my-history-with-swmm.md), [S12](sources/S12-li-diamond-village.md), [S16](sources/S16-li-rdii-in-swmm5.md), [S20](sources/S20-li-edition-54-two-solvers.md)). If Bob remembers, a line on each source page would replace "reads as".
- [ ] Q20 (2026-11-14): [S23](sources/S23-topsoil-recovery-check-app-md.md) numbers two engine defects D1 (Modified Horton with MaxInfil, EPA 5.2.4 `infil.c` line 545) and D2 (a drain on a bio-retention cell with no storage layer makes water, in EPA 5.2.4 and both OpenSWMM engines). D1 matches the confirmed `MODIFIED_HORTON` candidate in [S03](sources/S03-findings-register-format.md). Bob to say whether they get register IDs from F-0015 on (see Q18).
- [ ] Q21 (2026-11-14): [S23](sources/S23-topsoil-recovery-check-app-md.md) says the swmm524-perched repository states no license, while the engine it changes is public domain. Bob to decide the license.
