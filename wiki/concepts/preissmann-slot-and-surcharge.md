---
title: Preissmann slot and surcharge
type: concept
updated: 2026-11-14
sources: [S01, S04, S05, S08, S20, S21, S22]
tags: [hydraulics, swmm5, icm, surcharge]
reviewed: no
---
When a closed pipe fills, the free-surface equations stop applying. The Preissmann slot keeps them valid by putting a narrow virtual slot above the crown: the water level rises into the slot, and the slot width sets the wave speed. A narrower slot gives a faster wave, closer to real pressurized behavior, and needs a smaller time step [S20](../sources/S20-li-edition-54-two-solvers.md).

**Wave speeds, as the source gives them.** A pressure wave in a full pipe travels at roughly 3,300 ft/s (the source says 1,000 m/s; conversion ours), against 3 to 16 ft/s (1 to 5 m/s) for a gravity wave in a partly full pipe [S20](../sources/S20-li-edition-54-two-solvers.md).

**In the two programs**
- [InfoWorks ICM](../entities/infoworks-icm.md) has used the slot as its surcharge method from the beginning [S20](../sources/S20-li-edition-54-two-solvers.md).
- [EPA SWMM 5](../entities/swmm-5.md) inherited a separate surcharge algorithm from [EXTRAN](../entities/extran.md) that switches between open-channel and pressurized equations [S20](../sources/S20-li-edition-54-two-solvers.md). EXTRAN is still the default surcharge method in SWMM 5.2 [S01](../sources/S01-swmm1-engine-app-md.md).
- The SLOT option was added in build 5.1.013, which EPA's update notes date to 10 May 2018 [S22](../sources/S22-li-ten-problems.md).

**The two methods do not give the same steady state.** Register entry F-0001: a pump feeding a pressurized 1 ft pipe against a fixed 8 ft tailwater in EPA SWMM 5.2.4 settles at 5.0586 cfs under EXTRAN and 5.2475 cfs under SLOT, 3.7 % higher. The entry cites USEPA issue 231 and is marked unconfirmed until rerun [S04](../sources/S04-findings-register-seed.md). Bob's notes also record a SLOT-versus-EXTRAN difference between SWMM5 builds, found with the Four-Engine Pipe Comparator [S05](../sources/S05-swmm5org-article-facts.md).

**Other approaches in Bob's work.** A Slot-Free Pressurization app, and a Preissmann box branch in his fork of EPA SWMM [S08](../sources/S08-swmm5org-topic-inside-swmm5.md).

**Disagreements**
- [S20](../sources/S20-li-edition-54-two-solvers.md) says 5.1.013 was "released around 2012". [S22](../sources/S22-li-ten-problems.md), which cites EPA's update notes, and [S21](../sources/S21-li-edition-56-swmm-history.md)'s table both say 2018. Open question Q01 in [Open questions](../open-questions.md).
