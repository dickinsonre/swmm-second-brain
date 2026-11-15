---
title: The SWMM findings register
type: concept
updated: 2026-11-15
sources: [S03, S04, S05, S59, S67, S71, S72, S74, S75, S79, S80, S82, S83]
tags: [findings, verification, method]
reviewed: 2026-11-15
changed_after_review: "2026-11-15: one paragraph added near the end, headed Added 15 November 2026"
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
