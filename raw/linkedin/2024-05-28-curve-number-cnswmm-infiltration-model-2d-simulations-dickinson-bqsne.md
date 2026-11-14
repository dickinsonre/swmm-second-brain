---
title: "Curve Number or CNSWMM infiltration model for 2D simulations is now in ICM 2025.1"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/curve-number-cnswmm-infiltration-model-2d-simulations-dickinson-bqsne
created: "2024-05-28 17:38"
published: "2024-05-28 17:49"
words: 394
export_sha256: 6e4a38921341a7ff3baf9f80c689619780508442e24fd6471d7a644c59b00a82
---
# Curve Number or CNSWMM infiltration model for 2D simulations is now in ICM 2025.1

![New in 2025.1 is an often-requested feature - using a CN value or curve number on the ICM 2D mesh for infiltration. ](https://media.licdn.com/mediaD4E12AQFAb9msBgdx5g "New in 2025.1 is an often-requested feature - using a CN value or curve number on the ICM 2D mesh for infiltration. ")

New in 2025.1 is an often-requested feature - using a CN value or curve number on the ICM 2D mesh for infiltration. The following is from the online help file.

> **Curve Number or CNSWMM infiltration model for 2D Simulations**

### CNSWMM infiltration model for 2D simulations

A new infiltration model, CNSWMM, is now available for InfoWorks networks. This model combines the [CNSWMM](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-2B5418EF-21E4-4E7D-8187-6E51BD35C2AA) curve number model with initial losses. To use the model, a new CNSWMM option has been added to the Infiltration type property for [Infiltration Surface (2D)](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-104AF009-702A-4349-904C-FB3F34ECC7A6) objects. In addition, an Initial abstraction factor, which defines the initial loss, and the Curve number and Drying time used by CNSWMM infiltration have also been added as Infiltration Surface (2D) properties.

[Initial conditions in 2D have also been modified to enable the mode](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-3F7AA44B-F870-4144-B613-9D1A4A84E1EB)ling of CNSWMM infiltration. A new property, CNSWMM antecedent moisture condition, which represents the initial soil moisture condition before a rainfall event, has been added to the grid window. You can look at the 2D Infiltration Models for more information about the new model.

> **The various data fields and parameters to define an Infiltration Surface (2D) object ICM**

The key points are:

1.  Infiltration Surface (2D) data can be edited in the Infiltration Surface (2D) Grid Window or Property Sheet.

2.  The data is stored in the "hw_2d_infil_surface" database table.

3.  The main data fields include: ID: The name of the surface Infiltration type: Fixed, Horton, ConstInf, Green-Ampt, DefConLoss, or CNSWMM Parameters specific to each infiltration type, such as Fixed runoff coefficient (for Fixed and ConstInf) Horton initial, limiting, decay, and recovery factors (for Horton) Green-Ampt suction, conductivity, and deficit (for Green-Ampt) Infiltration loss coefficient and maximum deficit (for Deficit and Constant Loss) Curve number, initial abstraction factor, and drying time (for CNSWMM)
