---
title: The SWMM findings register
type: concept
updated: 2026-11-18
sources: [S03, S04, S05, S59, S67, S71, S72, S74, S75, S79, S80, S82, S83, S192, S193, S194, S195, S196, S197, S203, S216, S220, S209, S212, S240, S236, S229, S242, S255, S261, S262, S259, S285, S286, S282, S271, S287]
tags: [findings, verification, method]
reviewed: 2026-11-15
changed_after_review: "2026-11-17 (S192 to S202 ingest): one paragraph added at the end listing more app-local findings (S192 to S197); 2026-11-17 (S203 ingest): one paragraph added at the end on the SOIL2 misread; 2026-11-17 (S205 to S223 ingest): a paragraph added near the end, headed Added 17 November 2026 (S216, S220, S209, S212); 2026-11-17 (S224 to S242 ingest): a paragraph added near the end, headed Added 17 November 2026 (S240, S236, S229, S242); 2026-11-17 (S243 to S255 ingest): a paragraph added near the end, headed Added 17 November 2026 (S255); 2026-11-17 (S256 to S267 ingest): a paragraph added near the end, headed Added 17 November 2026 (S261, S262, S259); 2026-11-18 (S268 to S299 ingest): a paragraph added near the end, headed Added 18 November 2026 (S285, S286, S282, S271, S287)"
---
A numbered, dated record of what was checked and what came back, proposed in October 2026 because Bob's apps are safe on Netlify and GitHub while the findings exist only inside chat transcripts [S03](../sources/S03-findings-register-format.md).

**Rules** [S03](../sources/S03-findings-register-format.md)
1. Negative results are entries.
2. No claim without a procedure.
3. Numbers, not adjectives.
4. Status can change; the entry does not. Supersede with a new entry that cites the old ID.

**Seed entries.** Status is the source's own. "Unconfirmed" means not rerun since it was read out of the archive [S04](../sources/S04-findings-register-seed.md).

| ID | Claim | Key numbers | Status |
|---|---|---|---|
| F-0001 | Slot and EXTRAN reach different steady states | 5.2475 against 5.0586 cfs | unconfirmed |
| F-0002 | One bad shape spelling hid two more error layers in the OWA corpus | 20 files ERROR 205, then 10 ERROR 211, then 3 ERROR 209, of 151 | unconfirmed |
| F-0003 | Audusse sign error survives mass conservation | 39 of 39 after the fix | fixed |
| F-0004 | A benchmark harness undercounts its corpus | 57 uppercase `.INP` files missed | unconfirmed |
| F-0005 | SWMM6 keywords: fatal in 5.2.4, silent in legacy 5.3 | ERROR 205 | partly unconfirmed |
| F-0006 | Own accuracy claim for Fourier cross sections was wrong | conveyance 0.5 to 1.5 % at N = 6; local width 4 to 14 % | corrected |
| F-0007 | Lengthening invents storage | see [Conduit lengthening](conduit-lengthening.md) | unconfirmed |
| F-0008 | Twelve source-level defects in a third-party Rust rewrite (neeraip/hydra) | 12 of 12 claims confirmed against source | unconfirmed |
| F-0009 to F-0013 | Five negative results | see [Negative results](negative-results.md) | disproven (two with a stated scope) |
| F-0014 | Two claims by an outside reviewer did not hold | checked against source | confirmed against source |

**Not yet in the register.** [S03](../sources/S03-findings-register-format.md) lists twenty candidates. [S05](../sources/S05-swmm5org-article-facts.md) lists five named engine findings from Bob's notes, among them a `dt`-rounding bug and 23 documented deviations from SWMM5 in the Rust `hydra` engine. The 14 faults found in the 1971 SWMM 1 listing (see [SWMM 1 (1971)](../entities/swmm-1.md)) have no register IDs. [S59](../sources/S59-topsoil-recovery-check-app-md.md) numbers its own defects D1 (Modified Horton with MaxInfil, see [Infiltration methods](infiltration-methods.md)) and D2 (a drain with no storage layer, see [LID bio-retention layers](lid-bioretention-layers.md)); D1 matches the `MODIFIED_HORTON` candidate in [S03](../sources/S03-findings-register-format.md). Neither has a register ID (Q33 in [Open questions](../open-questions.md)). [S04](../sources/S04-findings-register-seed.md) expects 30 to 40 more entries from the archive before June 2026.

**A new candidate.** [Green-Ampt Newton test order](green-ampt-newton-test-order.md): a note of 14 November 2026 that asks for a register ID; status in the note "working", runs not rerun [S67](../sources/S67-note-green-ampt-newton-test-order.md).

**More candidates from the apps.** Five numbered defects in EPA 5.2.4 found by translating it [S71](../sources/S71-swmm-engines-byte-for-byte-summary.md); a possible `culvert.c` defect and 20 reading notes on OpenSWMM 6, all from source reading and JavaScript copies [S72](../sources/S72-li-swmm6-code-house-article.md). None has a register ID (Q47).

**Linked pages.** [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md) (F-0001), [Continuity is not validation](continuity-is-not-validation.md) (F-0003, F-0007), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md) (F-0005).

**Disagreements**
- Q08. F-0008 counts 12 defects in hydra; [S05](../sources/S05-swmm5org-article-facts.md) counts 23 deviations. One review or two?

**Added 15 November 2026.** The app summaries ingested today add more unregistered findings, each under its app's own IDs: thirty register items on the SWMM 4.4H, SWMM 5.2.4 and OpenSWMM 6 solvers, marked measured or read [S75](../sources/S75-st-venant-rosetta-stone-app-md.md); five pieces of hot start state, R-1 to R-5, and a run-duration defect, D-1 [S79](../sources/S79-teacher-forced-swmm-summary.md); nine channel findings, F1 to F9 [S80](../sources/S80-control-section-lab-summary.md); ten findings on SWMM5+, Mirab and EPA 5.2.4, S-1 to P-2 [S82](../sources/S82-mirab-test-bench-summary.md); two SWMM defaults and a file-system fault, D-1 to D-3 [S83](../sources/S83-people-as-pollutants-summary.md); and ten faults fixed in the 1981 EXTRAN listing [S74](../sources/S74-extran3-workbench-app-md.md). The labels collide: D-1 means three different things in three apps, and F1 to F9 look like this register's F-0001 series. None has a register ID (Q47). Pages that carry them: [The crown cap at mid-pipe](crown-cap-at-mid-pipe.md), [Hot start: what a restart loses](hot-start-restart-state.md), [Run duration floored to whole seconds](run-duration-floor.md), [WebAssembly builds against native builds](wasm-against-native-builds.md).

**Added 17 November 2026: more findings under the apps' own labels.** None of these has a register ID (Q47).
- [SWMM QA Report Bench](../entities/swmm-qa-report-bench.md): E1, EPA's 2006 report prints Figures 4.18 and 4.19 under each other's captions; B1, `swmm5.c:1593` passes a 260-byte buffer to `realpath`, and fortified glibc builds abort (no effect on results); O1, an observation on the weir surcharge flag; A1, the app's own first version drew synthetic curves [S192](../sources/S192-swmm-qa-report-bench-app-md.md).
- [SWMM5 Engine Race](../entities/swmm5-engine-race.md): F-1, `gage.c` casts a huge initial `dxMin` to int for a one-point time series, undefined in C [S197](../sources/S197-swmm5-engine-race-app-md.md). The label has the form of this register's F-0001 series.
- [SWMM 3 Runoff & Transport](../entities/swmm3-runoff-transport-app.md): SNOW-1, TRANS-1 and TRANS-2, three defects in the Version III code kept as shipped; TRANS-2 drops flow sent to an element that does not exist, -92 % on example TRANS23 [S193](../sources/S193-swmm3-runoff-transport-summary.md).
- [SWMM 4 Twin Engines](../entities/swmm4-twin-engines.md): the SWMM 4.4 Transport cap reads a storage unit's capacity from QO1 instead of QO2; on one deck the printed continuity error goes from 56.180 % to 0.003 % with the fix [S194](../sources/S194-swmm4-twin-engines-summary.md).
- [swmm5-kw](../entities/swmm5-kw.md) 1.1 fixed two defects of its own, a 64-outlet flag array and a HEAD rule that could hand out 1.5e-6 cfs more than arrived [S195](../sources/S195-swmm5-kw-summary.md).
- [SWMM5 RASPIPE](../entities/swmm5-raspipe.md) calls one stock behavior a bookkeeping gap: a fixed outfall that feeds the network is never booked as inflow [S196](../sources/S196-swmm5-raspipe-summary.md).

**Added 2026-11-17 (S203).** The Topsoil Recovery Check summary adds a third app-local finding beside D1 and D2: EPA 5.2.4 reads a SOIL2 line as a second SOIL line, with no error or warning [S203](../sources/S203-topsoil-recovery-check-v2026-11-17.md). It has no register ID (Q33 in [Open questions](../open-questions.md)).

**Added 17 November 2026.** More findings reported by app pages, not rerun here and not yet checked by a person: EPA's report prints "All links are stable." when the least stable link is the first in the file, report.c line 994 [S216](../sources/S216-swmm-rhythm-detector-summary.md); gage.c:251 converts 8.64 x 10^14 s to a C int, which C leaves undefined, so gcc and Rust write different reports on one-point rain series [S220](../sources/S220-swmm5-rs-side-by-side-summary.md); the stock dynamic slot runs 1.414 fast on an exact pressurised transient [S209](../sources/S209-rigid-column-test-summary.md); a short last link at a free outfall gives -11,199 % continuity with no error [S212](../sources/S212-swmm5-residual-walk-summary.md). The summaries use no status words; read them as unconfirmed.

**Added 17 November 2026, second batch.** From the second batch, again at the pages' word: a tapered channel under NORMAL_FLOW_LIMITED BOTH oscillates between 359.53 and 570.70 cfs, identical on two engine copies [S240](../sources/S240-non-prismatic-channel-lab-summary.md); the HEC-22 spread round trip in inlet.c gives 8.021 ft back from 8 ft, and the Maximum Spread SWMM reports comes from the street transect, not Eq. 4-2 [S236](../sources/S236-water-on-the-road-summary.md); a native Linux build of 5.2.4 aborts with "buffer overflow detected" unless built with -D_FORTIFY_SOURCE=0 [S229](../sources/S229-rule110-swmm5-summary.md) [S236](../sources/S236-water-on-the-road-summary.md); the obvious quasi-2D mesh stores twice the water, so waves arrive 1.414 times late [S242](../sources/S242-walk-the-mesh-summary.md).

**Added 17 November 2026, third batch.** From the third batch, at the page's word: SWMM 5.2.4's climate.c evening and pre-dawn temperature branches do not meet at midnight [S255](../sources/S255-ifs-analysis-explorer-summary.md).

**Added 17 November 2026, fourth batch.** From the fourth batch: OpenSWMM 6 at 137e65e kept a dry conduit's last evaporation rate, -34,178 % routing continuity on an all-snow storm, fixed upstream on 12 September 2026 (status as the page gives it) [S261](../sources/S261-swmm6-hands-on-watershed-summary.md); the cross-section tables make a Gothic sewer ring in dry weather [S262](../sources/S262-swmm5-swmm6-curve-sections-summary.md); the HydroCouple platform's packaging scanner misses the [LID_USAGE] report file [S259](../sources/S259-inside-hydrocouple-platform-summary.md).

**Added 18 November 2026.** From the 18 November batch, at the pages' word: alpha.4 Green-Ampt (ED-1, fixed upstream) and flooding summary (ED-2) [S285](../sources/S285-swmm6-shoebox-summary.md); storage nodes written as dividers (DR-1) and an FV junction at 103.4 ft (DR-2, undiagnosed) [S286](../sources/S286-exam-first-swmm-harness-summary.md); slot water booked as storage and still-pool continuity in every dynamic-wave run (O1 to O5) [S282](../sources/S282-forma-swmm6-summary.md); a 121-change corrected SWMM 4.4H with 26 faults left alone and listed [S271](../sources/S271-swmm44h-workbench-summary.md); a benchmark scorer that a forged results file beats [S287](../sources/S287-openhydro-bench-review-summary.md).
