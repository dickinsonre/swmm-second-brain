---
title: "S178: Curve Number or CNSWMM infiltration model for 2D simulations is now in ICM 2025.1 (LinkedIn, 2024)"
type: source
raw: raw/linkedin/2024-05-28-curve-number-cnswmm-infiltration-model-2d-simulations-dickinson-bqsne.md
kind: linkedin-article
author: Robert Dickinson
published: 2024-05-28
ingested: 2026-11-16
tags: [icm, 2d, infiltration, curve-number]
reviewed: no
---
**What it is.** Bob's short article announcing CNSWMM infiltration on the ICM 2D mesh in ICM 2025.1. Raw file: [raw/linkedin/2024-05-28-curve-number-cnswmm-infiltration-model-2d-simulations-dickinson-bqsne.md](../../raw/linkedin/2024-05-28-curve-number-cnswmm-infiltration-model-2d-simulations-dickinson-bqsne.md).

**How it was written.** Bob's article; most of it is quoted from Autodesk's ICM 2025 online help, as the article says ("The following is from the online help file"). The closing list of key points reads as a summary of that help. It states no AI use.

**Claims worth keeping**
- ICM 2025.1 added CNSWMM as an infiltration model for InfoWorks networks on the 2D mesh, an often-requested feature.
- CNSWMM combines the CNSWMM curve number model with initial losses. It is a new option of the Infiltration type property of Infiltration Surface (2D) objects, with new properties Initial abstraction factor (the initial loss), Curve number and Drying time.
- 2D initial conditions gained a property, CNSWMM antecedent moisture condition, for the soil moisture before a rainfall event.
- Infiltration Surface (2D) data is stored in the `hw_2d_infil_surface` table.
- The infiltration types listed: Fixed, Horton, ConstInf, Green-Ampt, DefConLoss and CNSWMM, each with its own parameters (Fixed runoff coefficient for Fixed and ConstInf; Horton initial, limiting, decay and recovery; Green-Ampt suction, conductivity and deficit; infiltration loss coefficient and maximum deficit for Deficit and Constant Loss; curve number, initial abstraction factor and drying time for CNSWMM).

**Against the 2023 article.** [S177](S177-li-curve-number-approximations-icm-2d.md) lists four 2D infiltration types in 2023; this lists six in 2025.1, adding DefConLoss and CNSWMM. A change in ICM over time, not a disagreement.

**Feeds:** [ICM 2D: rainfall and infiltration on the mesh](../concepts/icm-2d-rainfall-and-infiltration.md), [Infiltration methods](../concepts/infiltration-methods.md), [ICM network tables and result fields](../concepts/icm-tables-and-result-fields.md).
