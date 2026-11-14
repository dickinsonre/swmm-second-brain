---
title: "S17: Steady State, EPS, Kinematic and Dynamic Wave Options in InfoSewer, SWMM5, InfoSWMM, ICM SWMM and ICM InfoWorks (LinkedIn, 2024)"
type: source
raw: raw/linkedin/2024-07-28-steady-state-eps-kinematic-dynamic-wave-options-swmm5-dickinson-x3uhe.md
kind: linkedin-article
author: Robert Dickinson
published: 2024-07-28
ingested: 2026-11-14
tags: [hydraulics, routing, swmm5, icm, infosewer]
reviewed: no
---
**What it is.** A comparison of which routing methods five products offer. Raw file: [raw/linkedin/2024-07-28-steady-state-eps-kinematic-dynamic-wave-options-swmm5-dickinson-x3uhe.md](../../raw/linkedin/2024-07-28-steady-state-eps-kinematic-dynamic-wave-options-swmm5-dickinson-x3uhe.md).

**How it was written.** By Bob; the definitions are generic (AI-style) and the three SWMM5 routing descriptions follow the EPA SWMM5 help text. The bold sentences are his.

**Claims worth keeping**
- SWMM5, InfoSWMM and InfoSewer have a steady-state option. Bob's opinion: InfoSewer's is the best because of its flow loading and flow splitting options.
- ICM SWMM and ICM InfoWorks have no steady-state solver; a quasi-steady state is made by saving a state from a previous run and running for a few minutes.
- All five do extended-period simulation.
- Only SWMM5 and InfoSWMM have kinematic wave routing.
- SWMM5 steady flow and kinematic wave routing work only on dendritic networks, where each node has one outflow link (two for a divider).
- Kinematic wave is stable with time steps of 1 to 5 minutes; dynamic wave needs steps of thirty seconds or less.
- ICM SWMM defaults to the SWMM5 dynamic wave; ICM InfoWorks to its implicit St. Venant solution.

**Feeds:** [Kinematic wave and steady flow routing](../concepts/kinematic-wave-and-steady-flow.md), [Dynamic wave routing](../concepts/dynamic-wave-routing.md), [SWMM 5 versus ICM InfoWorks](../concepts/swmm5-versus-icm-infoworks.md), [InfoSWMM and InfoSewer](../entities/infoswmm-and-infosewer.md), [InfoWorks ICM](../entities/infoworks-icm.md).
