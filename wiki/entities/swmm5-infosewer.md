---
title: swmm5-infosewer
type: entity
updated: 2026-11-17
sources: [S201, S70]
tags: [swmm5, infosewer, engine, pumps, force-mains]
reviewed: no
---
One of Bob's variants of [EPA SWMM 5](swmm-5.md): 5.2.4 with InfoSewer's routing rules, switched on by `FLOW_ROUTING INFOSEWER`. Repository SWMMBobSWMM6/swmm5-infosewer, private; the build described is commit 12492d6 [S201](../sources/S201-infosewer-2009-app-md.md). It is one of the engines on the extend road in [Wrap, translate or extend](../concepts/wrap-translate-or-extend.md) [S70](../sources/S70-swmm-engine-what-if-app-md.md).

**The method.** Write up the InfoSewer engine's rules with source file and line references, then match its output value for value. The reference is the InfoSewer engine (HeEngPkg) of MWH Soft and Innovyze, 1996 to 2011, built from its source, which Bob supplied; it is proprietary and not in the repository [S201](../sources/S201-infosewer-2009-app-md.md). See [InfoSWMM and InfoSewer](infoswmm-and-infosewer.md).

**The rules it copies** [S201](../sources/S201-infosewer-2009-app-md.md)
- Pump curve `H = H0 - a Q^b`.
- Force main loss by Hazen-Williams, `hL = 4.727 L Q^1.852 / (C^1.852 D^4.871)`, Q in cfs, L and D in ft.
- A station runs where pump head equals static lift plus force main loss. Steady state reports force main flow equal to station inflow, with head loss at the pump flow.
- Extended period: each wet well on a 1-minute pump step, pumps on at the maximum level and off at the minimum, reported hourly.

**How close.** On the 2009 network of [InfoSewer_2009 (app)](infosewer-2009.md), 58,487 of 58,487 steady-state values and 900,500 of 900,500 extended-period values identical in every bit. Over its whole test set, 11,894,156 values, all identical except the LPS and MLD models, within 4.2e-11 [S201](../sources/S201-infosewer-2009-app-md.md).

**What this does not show.** It is not a second opinion on InfoSewer: it copies InfoSewer's rules, oddities included. Two engine paths have no reference case, a bisection after Newton fails and a gravity pipe leaving a wet well [S201](../sources/S201-infosewer-2009-app-md.md).

**Related.** [Pumps and pump curves](../concepts/pumps-and-pump-curves.md), [Force main friction](../concepts/force-main-friction.md).
