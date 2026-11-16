# Assign rainfall and infiltration explicitly where ICM domains overlap

**Status:** seed
**Date:** 2026-11-16

## The idea

InfoWorks can apply a rainfall event to subcatchments and directly to 2D mesh elements. Autodesk documents that overlapping areas can receive rainfall independently in both domains when direct mesh rainfall is enabled. Use the zone's application setting and rainfall percentages to implement the intended allocation. Document roofs or other surfaces that route directly to the drainage network.

## Proof / from scratch

1. Record the event, rainfall profile, area, and accumulated rain depth for the test. Start with one uniform profile and confirm the selected mesh receives it.
2. For any overlapping subcatchment, record its runoff destination and the 2D zone's setting for where rainfall applies. Autodesk gives `outside subcatchments` as the setting for excluding the overlap from direct mesh rainfall. Check rainfall percentages on both the 2D zone and assigned infiltration zones where relevant.
3. Assign an Infiltration Surface (2D) to the zone or to an Infiltration Zone (2D). Record the chosen method and its parameters with the run. For CNSWMM, capture Curve Number, initial abstraction factor, and drying time.
4. Run a closed flat zone with no infiltration first. Add one infiltration surface in the next run. With no boundary flow or evaporation, compare applied rain with final surface storage plus the infiltrated volume.

Use the two dated Curve Number articles together. The 2023 article explored approximations. The 2025.1 article records the addition of CNSWMM on the mesh, and the 2027 help lists the method and its parameters.

## Links

- [Autodesk 2D zone data fields for InfoWorks](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-111E1710-4BA5-4F49-8596-E5B00C4F6CE6.htm)
- [Autodesk Infiltration Zone (2D) data fields](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-10827E24-D0A4-4BA2-94C6-3640C0A08ECF.htm)
- [Autodesk 2D infiltration models](https://help.autodesk.com/cloudhelp/2027/ENU/ICM-Help/files/GUID-248537F7-C2E1-42C3-A1B3-E743A8385E5A.htm)
- [Bob's 2023 Curve Number approximation article](https://github.com/dickinsonre/swmm-second-brain/blob/main/raw/linkedin/2023-09-22-investigating-curve-number-approximations-icm-2d-robert-dickinson.md)
- [Bob's 2025.1 CNSWMM update](https://github.com/dickinsonre/swmm-second-brain/blob/main/raw/linkedin/2024-05-28-curve-number-cnswmm-infiltration-model-2d-simulations-dickinson-bqsne.md)
- [2D benchmark cases](./icm-2d-benchmark-cases.md)
