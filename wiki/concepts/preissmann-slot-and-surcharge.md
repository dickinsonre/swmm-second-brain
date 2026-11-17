---
title: Preissmann slot and surcharge
type: concept
updated: 2026-11-16
sources: [S01, S04, S05, S08, S20, S21, S22, S55, S60, S75, S79, S188]
tags: [hydraulics, swmm5, icm, surcharge]
reviewed: 2026-11-15
changed_after_review: "2026-11-16 (S188 to S190 ingest): one paragraph added at the end on the 2021 Water Talks webinar (S188)"
---
When a closed pipe fills, the free-surface equations stop applying. The Preissmann slot keeps them valid by putting a narrow virtual slot above the crown: the water level rises into the slot, and the slot width sets the wave speed. A narrower slot gives a faster wave, closer to real pressurized behavior, and needs a smaller time step [S20](../sources/S20-li-edition-54-two-solvers.md).

**Wave speeds, as the source gives them.** A pressure wave in a full pipe travels at roughly 3,300 ft/s (the source says 1,000 m/s; conversion ours), against 3 to 16 ft/s (1 to 5 m/s) for a gravity wave in a partly full pipe [S20](../sources/S20-li-edition-54-two-solvers.md).

**In the two programs**
- [InfoWorks ICM](../entities/infoworks-icm.md) has used the slot as its surcharge method from the beginning [S20](../sources/S20-li-edition-54-two-solvers.md).
- [EPA SWMM 5](../entities/swmm-5.md) inherited a separate surcharge algorithm from [EXTRAN](../entities/extran.md) that switches between open-channel and pressurized equations [S20](../sources/S20-li-edition-54-two-solvers.md). EXTRAN is still the default surcharge method in SWMM 5.2 [S01](../sources/S01-swmm1-engine-app-md.md).
- The SLOT option was added in build 5.1.013, which EPA's update notes date to 10 May 2018 [S22](../sources/S22-li-ten-problems.md).

**The two methods do not give the same steady state.** Register entry F-0001: a pump feeding a pressurized 1 ft pipe against a fixed 8 ft tailwater in EPA SWMM 5.2.4 settles at 5.0586 cfs under EXTRAN and 5.2475 cfs under SLOT, 3.7 % higher. The entry cites USEPA issue 231 and is marked unconfirmed until rerun [S04](../sources/S04-findings-register-seed.md). Bob's notes also record a SLOT-versus-EXTRAN difference between SWMM5 builds, found with the Four-Engine Pipe Comparator [S05](../sources/S05-swmm5org-article-facts.md).

**How the EXTRAN-method surcharge works in SWMM 5** [S60](../sources/S60-epa-swmm5-reference-manual-vol2-hydraulics.md)
- A node is surcharged when every conduit connected to it is full, or its water level is above the crown of the highest connected conduit.
- A surcharged node has no free volume left, so its head cannot come from the ordinary surface-area formula. It is updated by a perturbation equation that drives the sum of flows at the node to zero.
- A blending factor eases the switch: by the time the water is 25 % above the highest conduit, the update is 98 % pure surcharge.
- Under-relaxation is not applied to the head of a surcharged node.
- The manual as read (May 2017) describes this method only; the SLOT option came a year later.

**Other approaches in Bob's work.** A Slot-Free Pressurization app, and a Preissmann box branch in his fork of EPA SWMM [S08](../sources/S08-swmm5org-topic-inside-swmm5.md). A planned fix: SWMM 5's slot has a fixed width of about 1 % of the pipe diameter, and the proposal is to narrow it as pressure stabilizes [S55](../sources/S55-swmm-brain-readme.md).

**Disagreements**
- [S20](../sources/S20-li-edition-54-two-solvers.md) says 5.1.013 was "released around 2012". [S22](../sources/S22-li-ten-problems.md), which cites EPA's update notes, and [S21](../sources/S21-li-edition-56-swmm-history.md)'s table both say 2018. Open question Q01 in [Open questions](../open-questions.md).

**Added 15 November 2026.** Measurements from the [St. Venant Solver Rosetta Stone (app)](../entities/st-venant-solver-rosetta-stone.md), on Example 1 of the EXTRAN manual at a 20-second step [S75](../sources/S75-st-venant-rosetta-stone-app-md.md): EPA SWMM 5.2.4 loses 114,824 ft³ to flooding with SURCHARGE_METHOD EXTRAN and 78,582 ft³ with SLOT. The same input in OpenSWMM gives 114,824 and 89,559, because there the slot area does not convey flow. Formulas as the summary reads them: SWMM 5.2.4's slot width is 0.5423 wMax exp(-(y/yFull)^2.4), and 0.01 wMax above 1.78, at `dwflow.c:584-587`; the head spike of the EXTRAN method grows as the time step shrinks, to 153.61 ft at a 5-second step against 134.62 ft at 20 seconds. These add a second case to F-0001 above, on a different network. See [The crown cap at mid-pipe](crown-cap-at-mid-pipe.md) for why a pipe surcharged at one end is treated as partly full, [OpenSWMM 6 solvers, measured](openswmm6-solvers-measured.md), and [Teacher-Forced SWMM (app)](../entities/teacher-forced-swmm.md), which tests three slot momentum variants written from EPA issue 231 [S79](../sources/S79-teacher-forced-swmm-summary.md).

**Added 16 November 2026, from Bob's 2021 webinar** [S188](../sources/S188-talk-water-talks-icm-sim-vs-icm-swmm-2021.md). Spoken claims:
- SWMM 5's slot width is 1 %, with the Sjöberg formula as the pipe nears full. ICM sets its slot width from a celerity ratio: 14.4 gives 1 %, 20 gives 2 %, or the user enters a width.
- A SWMM 5 force main still uses the slot; an ICM force main does not.
- For a comparison with ICM, use SLOT in SWMM 5: it "matches better what ICM does". On his inverted siphon, SWMM 5 ran better with SLOT than with EXTRAN.
- He says Lew Rossman added the slot "two years ago". In a talk of 2021 that points to about 2019, a third date beside Q01's 2012 and 2018; EPA's update notes, cited by [S22](../sources/S22-li-ten-problems.md), give 10 May 2018.
