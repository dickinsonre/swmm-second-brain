---
title: "ICM SWMM and InfoDrainage share the same swmmsim.exe Engine SWMM 5.2.4, InfoSWMM uses an older version of the EPA SWMM5 Engine based on SWMM 5.1.015"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/icm-swmm-infodrainage-share-same-swmmsimexe-engine-524-dickinson-qph1e
created: "2024-06-15 21:57"
published: "2024-06-15 22:23"
words: 2534
export_sha256: 50b5ec61da360f1fe9a224e7cd00301273a942adf9e44fef94fd492f8a4c7753
---
# ICM SWMM and InfoDrainage share the same swmmsim.exe Engine SWMM 5.2.4, InfoSWMM uses an older version of the EPA SWMM5 Engine based on SWMM 5.1.015

![ICM SWMM and InfoDrainage share the same swmmsim.exe Engine SWMM 5.2.4, InfoSWMM uses an older version of the EPA SWMM5 Engine based on SWMM 5.1.015](https://media.licdn.com/mediaD4E12AQFAoGqI0oVXJw "ICM SWMM and InfoDrainage share the same swmmsim.exe Engine SWMM 5.2.4, InfoSWMM uses an older version of the EPA SWMM5 Engine based on SWMM 5.1.015")

This article explains the differences between the SWMM engines used in various Innovyze and now Autodesk Water modeling products. It is noted that the ICM SWMM and InfoDrainage platforms share the same swmmsim.exe engine, which is based on a more recent version of the EPA SWMM5 software or SWMM 5.2.4. They both share the same swmmsim engine with the main difference being InfoDrainge has SWMM5 Inlets and InfoSWMM does not. In contrast, the older InfoSWMM product (soon to move to mature status) utilizes an earlier version of the EPA SWMM5 engine. The article also highlights the differences between SWMM5 versions 5.1.015 and 5.2.4, available on the EPA website, allowing users to understand better the evolution and differences between InfoSWMM and ICM SWMM. You can see the updated history for SWMM5 between 2020 and 2024 at the bottom of the article from the EPA SWMM5 download website.

> 1: EPA SMMM5 Download Page - Click on the image to go to the URL

[![](https://media.licdn.com/dms/image/v2/D4E12AQEz56PpuzwvSg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718488787078?e=1795651200&v=beta&t=YuQs22jQV-4Nd9Rot3nE_KCw56IooaBvRiTlIkol1nw)](https://www.epa.gov/water-research/storm-water-management-model-swmm)

EPA SMMM5 Download Page - Click on the image to go to the URL

> **2: ICM SWMM and InfoDrainage share the same swmmsim.exe Engine based on SWMM 5.2.4; InfoSWMM uses an older version of the EPA SWMM5 Engine based on SWMM 5.1.015**

![](https://media.licdn.com/dms/image/v2/D4E12AQECUycn54OGQQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718489012640?e=1795651200&v=beta&t=W-IXQInKaHJwcYcQr_0_aUbVbvYtb317rVjupwL9vok)

ICM SWMM and InfoDrainage share the same swmmsim.exe Engine; InfoSWMM uses an older version of the EPA SWMM5 Engine

![](https://media.licdn.com/dms/image/v2/D4E12AQGT_rSDg61vtw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718490122133?e=1795651200&v=beta&t=feD-dt35FkNuVYBje0kHf74_Qrohn8bHiI7bAltOadk)

ICM SWMM and InfoDrainage share the same swmmsim.exe Engine SWMM 5.2.4, InfoSWMM uses an older version of the EPA SWMM5 Engine based on SWMM 5.1.015

> **3: Differences in the EPA SWMM5 engine between 5.1.015 and 5.2.4 from the EPA Web Site**

## SWMM 5 Update History

------------------------------------------------------------------------

### Build 5.2.4 (07/15/2023)

Engine Updates:

1.  A potential mismatch between reported pollutant Surface Runoff mass and conveyance system Wet Weather Inflow mass in a run's Status Report was fixed.

2.  The test for invalid input data for an LID unit with an underdrain was fixed.

3.  Improvements and corrections were made to the calculation of water flux rates between layers in Bio-Retention, Permeable Pavement, and Infiltration Trench LID units.

4.  The hydraulic head seen by a storage layer underdrain in a Permeable Pavement LID unit with a soil layer above it was corrected.

5.  A bug in retrieving the backing parameters for a street cross-section was fixed.

6.  The generation of transect points for a street cross-section with a depressed gutter was corrected.

7.  The calculation of gutter slope for street links with depressed gutters was corrected.

8.  The calculation of the effective hydraulic head seen within a curb inlet with an inclined throat opening was corrected.

9.  Conduit evaporation and seepage loss over a time step are now limited to the conduit's current volume instead of its flow rate under dynamic wave flow routing.

10. A conduit's evaporation and seepage loss are now split evenly between its end nodes instead of just at the upstream node.

11. The default values for the Inertial Damping and Variable Time Step options were made compatible with those used by the GUI.

GUI Updates:

1.  Flickering of the study area map when panning has been fixed.

2.  An Access Violation error message will no longer appear when trying to edit the vertices of a Storage Unit polygon.

3.  When the Welcome Screen is re-opened from the Help menu and a new file is selected, the program now prompts the user to save the current project they were working on.

4.  The possibility of the centroid symbol for subcatchments and storage nodes being outside their bounding polygon was fixed.

5.  The Max/Full Depth value for orifices and weirs now appears in the correct column of the Summary Results Link Flow table.

6.  A "Scrollbar property out of range" error should no longer appear after running a model with an extremely long duration.

------------------------------------------------------------------------

### Build 5.2.3 (02/12/2023)

Engine Updates:

1.  Double counting of initial moisture volume in the drainage mat layer of a green roof LID unit was fixed.

GUI Updates:

1.  A failure to load a project's backdrop image when first opened in v.5.2.2 was fixed.

2.  A failure in v5.2.2 to update the position of a Storage Unit's centroid symbol after its vertices are edited was fixed.

------------------------------------------------------------------------

### Build 5.2.2 (12/01/2022)

Engine Updates:

1.  Long-run times occurring when the simulation duration exceeded the end of an externally applied time series were eliminated.

2.  A bug introduced in 5.2.0 causing the math expression evaluator to compute a*b^c as (a*b)^c instead of a\*(b^c) was fixed.

3.  A check was added to the dimensions supplied for the Modified basket handle and Round-Rectangular cross sections to insure that the computed height of the rounded portion does not exceed the total height.

4.  Additional performance statistics were added to the Street Flow Summary table in the project's report file.

5.  The warning messages removed in release 5.2.1 about raising a node's maximum depth and adjusting a conduit's elevation drop were restored.

6.  The values reported for storage unit evaporation and exfiltration loss as a percentage of total storage volume were corrected.

7.  The default number of threads used for dynamic wave flow routing was changed to 1 to be consistent with the User's Manual and with the GUI.

GUI Updates:

1.  The display of the Street Flow Summary table was updated to accommodate the additional results added to the table.

2.  Storage units can now be drawn as polygons in a similar fashion as subcatchments.

3.  The dashed line between inlet conduits and their receptor nodes is always drawn from the conduit node at lower invert elevation.

4.  An option to view a backdrop image in grayscale was added to the View \| Backdrop menu.

5.  The Copy As Data option was removed from the preview plots of Curves, Time Series, and Transects in their respective editors since it was not functioning correctly.

6.  The display of a progress indicator in the program's task bar icon was removed as it caused problems in some computing environments (such as Citrix).

------------------------------------------------------------------------

### Build 5.2.1 (8/01/2022)

Engine Updates:

1.  Use of the Normal Flow Limited feature for dynamic wave flow routing is now optional.

2.  A refactoring bug causing excessive execution times for projects with control rules has been fixed.

3.  For kinematic wave storage routing, after convergence is obtained, the reported depth is based on the last volume value rather than the next trial depth.

4.  Corrections were made to the geometry tables for the egg-shaped cross section at the two lowest relative depth levels.

5.  The practice of setting a dry node's pollutant concentration to 0 even when it receives non-zero pollutant inflow (as introduced in release 5.2.0) has been dropped.

6.  When there is no inflow to a non-storage node, its water quality concentration now remains unchanged rather than being set to 0.

7.  The definition of F_OFF in output.c was corrected for non-MS C/C++ compilers.

8.  To eliminate having an excessive number of warning messages appear in the Status Report:

GUI Updates:

1.  The Dynamic Wave page of the Simulation Options dialog had �NONE� added to the choice for Normal Flow Criteria.

2.  The program's task bar icon now displays a progress indicator while a simulation is running.

3.  A more accurate method is now used to detect the number of cores available on the Dynamic Wave options dialog.

4.  Issues with how the Welcome Screen behaved when there were no recent projects to display were fixed.

5.  Subcatchment outlines are now included when the Study Area Map is exported to a DXF file and a problem with the sizing of the node symbols was fixed.

6.  Some issues with restoring the state of the program after an Add-In tool returned control to it were fixed.

7.  The annoying Access Violation message when using the Storage Shape editor was eliminated.

8.  Some refactoring was done to make the code compatible with Delphi 10.4.

------------------------------------------------------------------------

### Build 5.2.0 (11/01/21)

Engine Updates:

1.  Support has been added for modeling street runoff capture by inlet drains:

2.  A Type 5 variable-speed pump that obeys the pump affinity laws relating head and flow to pump speed was added.

3.  Storage Curve options now include several pre-defined shapes (cylinders, paraboloids, cones and pyramids) whose geometry is based on analytical formulas

4.  Several new quantities, including past n-hour rainfall, were added to the properties that can appear in control rule condition clauses.

5.  Control rule condition clauses were expanded to include named variables and math expressions.

6.  A listing of the nodes with the highest flow routing non-convergence frequency was added to the Status Report.

7.  Support was added for the latest version of NOAA's Climate Data Online service, where GHCN climate files can be retrieved in either US or SI units.

8.  An additional validation check was added to the user-supplied Initial Deficit value for Green-Ampt infiltration.

9.  The conversion of runon flow into an equivalent ponded depth for Curve Number infiltration was fixed.

10. A new parameter was added to Rain Barrel LIDs, indicating whether the rain barrel is covered or not.

11. The effect that the Impervious Surface Fraction parameter for Permeable Pavement LID has on the pavement layer's effective permeability is now accounted for.

12. The values of water depth in a Permeable Pavement LID written to the detailed LID report file are now expressed as inches (or mm) instead of feet.

13. The math expression parser was modified to allow exponents to be expressions instead of just constant numerical values.

14. The way in which average flow is computed was changed for the time-step-average reporting option.

15. The total reporting time value used to compute several statistics in the summary results tables was corrected.

16. Shell sort replaces insertion sort for sorting event periods.

17. The number of open files that SWMM can access was increased to

18. The command-line executable now supports binary output files larger than 2 GB.

19. A number of new functions were added to the SWMM 5 API.

GUI Updates:

1.  An optional Welcome page has been added to the program.

2.  The map-related speed buttons on the main toolbar have been moved into a separate Map toolbar on the Study Area Map window.

3.  A set of keyboard shortcuts for common menu commands has been added with a Help menu item that lists them.

4.  A subset of results appearing in the Summary Results tables can now be viewed as themes on the Study Area Map.

5.  Use of the F1 key to bring up context-sensitive Help has been extended to all dialog forms.

6 . Support for relative path names for files appearing in an input file has been added, making these files more portable.

1.  New dialog forms were created for editing the properties of Street cross-sections and Inlet structures.

2.  A new Inlet Usage dialog form was created for assigning an Inlet structure to a street conduit and the node that receives its captured flow.

3.  A new dialog form has been added for entering a storage unit's shape data.

4.  A new dialog form has been added that helps a user select a Culvert Code number for conduits based on the culvert's shape and inlet design.

5.  A Type5 pump type has been added to the choice of pump types in the Pump Curve Editor.

6.  Void ratios greater than 1 for LID storage layers are now accepted by the LID Control Editor.

7.  Pump startup and shutoff depths are now included in the properties that can be copied to another pump.

8.  A problem with the Property Editor not appearing after a session using a multi-monitor setup was fixed.

9.  The Move Up and Move Down buttons on the Data Browser now work correctly.

10. The input file reader now strips off any BOM character it detects at the beginning of the file.

11. A warning message is now shown if no data can be read from an opened file, such as when it is not a true SWMM project file.

12. Potential problems with determining the map extents from a SWMM input file were fixed.

------------------------------------------------------------------------

### Build 5.1.015 (05/01/20)

Engine Updates:

1.  A mix of infiltration methods can now be used within a project.

2.  The Status Report now includes a grouped frequency table of the variable routing time steps used during a simulation.

3.  An error in the average summary statistics reported for projects with a reporting start date later than the simulation start date was fixed.

4.  A pollutant mass balance error occurred when very shallow storage units lost all inflow to flooding.

5.  A fatal error is now issued if a storage node's area curve produces a negative volume when extrapolated to the node's full depth.

GUI Updates:

1.  The mouse wheel can now be used to zoom in or out of the Study Area Map without having to select a speed button or menu option.

2.  The Subcatchment Infiltration Dialog was modified to accept a choice of infiltration method.

3.  The Group Editor dialog was modified to allow a choice of infiltration method and its parameters to be assigned to a group of subcatchments.

4.  Some problems with the Graph Options dialog for the Statistics Report plots were fixed.

5.  Better support for 4K ultra-HD monitors was added.

6.  The latter update required that the three toolbars on the main window be combined into one to avoid resizing issues.

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

![](https://media.licdn.com/dms/image/v2/D4E12AQEDlU2ZRn4rGQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718489131914?e=1795651200&v=beta&t=uI-TtqePXvIO3MKWe_JYfs9pEjj-r912FvCcH2qRzeg)

Mid-Journey AI image for Color
