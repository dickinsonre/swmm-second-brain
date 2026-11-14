---
title: The SWMM findings register
type: concept
updated: 2026-11-14
sources: [S03, S04, S05, S23]
tags: [findings, verification, method]
reviewed: no
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

**Not yet in the register.** [S03](../sources/S03-findings-register-format.md) lists twenty candidates. [S05](../sources/S05-swmm5org-article-facts.md) lists five named engine findings from Bob's notes, among them a `dt`-rounding bug and 23 documented deviations from SWMM5 in the Rust `hydra` engine. The 14 faults found in the 1971 SWMM 1 listing (see [SWMM 1 (1971)](../entities/swmm-1.md)) have no register IDs. [S23](../sources/S23-topsoil-recovery-check-app-md.md) numbers its own defects D1 (Modified Horton with MaxInfil, see [Infiltration methods](infiltration-methods.md)) and D2 (a drain with no storage layer, see [LID bio-retention layers](lid-bioretention-layers.md)); D1 matches the `MODIFIED_HORTON` candidate in [S03](../sources/S03-findings-register-format.md). Neither has a register ID (Q20 in [Open questions](../open-questions.md)). [S04](../sources/S04-findings-register-seed.md) expects 30 to 40 more entries from the archive before June 2026.

**Linked pages.** [Preissmann slot and surcharge](preissmann-slot-and-surcharge.md) (F-0001), [Continuity is not validation](continuity-is-not-validation.md) (F-0003, F-0007), [OpenSWMM 6 and HydroCouple](../entities/openswmm-6-and-hydrocouple.md) (F-0005).

**Disagreements**
- Q08. F-0008 counts 12 defects in hydra; [S05](../sources/S05-swmm5org-article-facts.md) counts 23 deviations. One review or two?
