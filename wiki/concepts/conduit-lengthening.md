---
title: Conduit lengthening
type: concept
updated: 2026-11-14
sources: [S04, S22]
tags: [hydraulics, swmm5, stability]
reviewed: 2026-11-15
---
`LENGTHENING_STEP` is one of the [dynamic wave](dynamic-wave-routing.md) stability options SWMM 5 carries from EXTRAN's history [S22](../sources/S22-li-ten-problems.md). Per F-0007, a lengthening step of 10 s stretches every conduit shorter than the distance a wave travels in that time [S04](../sources/S04-findings-register-seed.md).

**Finding F-0007 (status: unconfirmed until rerun).** Lengthening adds storage that does not exist, attenuates peaks and suppresses node flooding, and nothing in the run warns of it [S04](../sources/S04-findings-register-seed.md).

| Quantity | US customary (our conversion) | As the source gives it |
|---|---|---|
| Pipe size | 3.3 ft | 1 m |
| Wave speed c | about 10 ft/s | about 3.1 m/s |
| Lengthening step | 10 s | 10 s |
| Every conduit shorter than this is stretched | about 102 ft | about 31 m |
| A connector of this length | 20 ft | 6 m |
| becomes | 102 ft | 31 m |
| Storage added per connector | about 710 cu ft | about 20 m³ |
| 150 short stubs in a flat combined system | about 106,000 cu ft | about 3,000 m³ |

All rows are from [S04](../sources/S04-findings-register-seed.md). Continuity closes throughout, and travel time and water-column mass inflate by the same factor [S04](../sources/S04-findings-register-seed.md). In the demonstration, a fully lengthened stub reached only 5.1 s of a 10 s target [S04](../sources/S04-findings-register-seed.md).

**Why it matters.** It is a case for [Continuity is not validation](continuity-is-not-validation.md): the run reports a closed mass balance while the answer is wrong where flooding accuracy matters most [S04](../sources/S04-findings-register-seed.md).

**Not in the sources yet.** The formula SWMM 5 uses to lengthen a conduit, and which release introduced the option. Likely in the queued EXTRAN and "Inside SWMM5" material.
