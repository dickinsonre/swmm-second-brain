---
title: "Advanced Calibration Graphs and Advanced Reference Graphical Comparisons in InfoSWMM 13, 14, 14.5"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/advanced-calibration-graphs-reference-graphical-13-robert-dickinson
created: "2015-07-27 13:07"
published: "2015-07-27 13:07"
words: 1286
export_sha256: de2c12d47e996ffa3a1f03a3255c3f55b0e1c8d1d3a51243ff35fb9ab07faf84
---
# Advanced Calibration Graphs and Advanced Reference Graphical Comparisons in InfoSWMM 13, 14, 14.5

### Advanced Calibration Graphs and Advanced Reference Graphical Comparisons in InfoSWMM 13, 14, 14.5

> One of the most valuable tools in any simulation program is the ability to compare monitored and predicted data. The new InfoSWMM v13 to InfoSWMM v14.5 excels in its ability to effectively compare monitored and predicted data, the results of different scenarios and in the making of mixed graphs comparing disparate elements in the network. The graphs can be viewed using Multiple Reference Panels or with multiple Reference Axes.

InfoSWMM v13+ allows the comparison of 15 types of monitored data for Nodes, Links and Subcatchments. The Calibration comparisons can be made for Node Depth, Node Head, Lateral Inflow, Flooding, Node Quality, Storage Volume, Link Flow, Link Depth, Link Head, Link Velocity, Runoff, Snow Depth, Groundwater Flow, Groundwater Elevation and Water Quality Washoff (Figure 1). The Calibration Reference graph in addition will show the Volume comparison between predicted and monitored data (Figure 2). InfoSWMM has the ability to plot up to 66 node, link, subcatchment, LID, 2D and System output variables which helps in understanding and interpreting the model output. The new InfoSWMM v13 greatly expands the ability to view and understand all of these model view variables in concise and clear graphs. The new graphics are also available in InfoSWMM for transects, curves, time series, DB tables, Report Manager output Tables and any graph in any dialog box of InfoSWMM. The new graphics are also a feature in H2OMap SWMM v13. InfoSWMM and H2OMap SWMM are based on the current version of [EPA SWMM 5 or 5.1.01](http://www2.epa.gov/water-research/storm-water-management-model-swmm)2.

Area, bar and line options for the System Results in InfoSWMM. The graphs can have reference panels, reference axes, custom markers, lines, and colors, compare calibration data and scenario output.

![](https://media.licdn.com/dms/image/v2/C5112AQErSSS2AOgTxA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1520214068315?e=1795651200&v=beta&t=x3zlmQthneGFawpS69heKiqyHAO4XSNton4Es8tYyaE)

**Figure 1.** InfoSWMM Calibration Files, 15 types

![](https://media.licdn.com/dms/image/v2/C5112AQGaZLDIY3PqEQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520143352934?e=1795651200&v=beta&t=1dB6EiQkz_qR2lyMHkQzBZuewal7sXV8f53uIOYjlLU)

![](https://media.licdn.com/dms/image/v2/C5112AQFkuT3KaHk6WQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1520192690991?e=1795651200&v=beta&t=AdPFgy40xDdMKrHVOdHv7lWzGJLeSk08rLNgyejcXMU)

Figure 2. InfoSWMM Calibration Plots show the Monitored and Predicted Volumes.

The Calibration Plots and any graph layer in InfoSWMM can be customized as either a line, bar or area. The color, markers, and thickness of each bar, area or line can be saved as a permanent setting for the model in the future. The graphs can be viewed in 3D or as a mixture of bar and area, bar and line, bar, area and line (Figure 3). There are 8 view variables for Subcatchments, 14 view variables for Nodes, 13 view variables for Links, 14 view variables for the System, 10 view variables for Low Impact Development (LID) and 7 view variables for 2D polygons, points and lines for a total of 66 view variables.

![](https://media.licdn.com/dms/image/v2/C5112AQFZgJy3Ev-paw/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520214595597?e=1795651200&v=beta&t=CxaBXRNHlryJrnaEZYlx71nxtCiN7wOzZc5-DI6wcMs)

Figure 3. InfoSWMM Calibration Plot with Additional Scenario Graphs and a Rainfall Reference Axes.

Figure 4. InfoSWMM Link Flow plots now have an automatic reference rainfall panel if you are simulating Subcatchments.

If you are modeling Runoff from a Subcatchment then the program will automatically create a reference panel for the rainfall from the nearest Subcatchment if you graph a Node or Link (Figure 4 and 5). The rainfall has a reverse Y axis and the default view is a bar but this can be changed by using the properties icon and converted to another color or a line and area.

![](https://media.licdn.com/dms/image/v2/C5112AQHmOtb0MJ5Vng/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520256000690?e=1795651200&v=beta&t=bU0UmhOyTTm6oG38VIQ0mF1DF7Ul9rUytl3fePqR_x0)

Figure 5. InfoSWMM Node Depth plots now have an automatic Reference rainfall Panel.

![](https://media.licdn.com/dms/image/v2/C5112AQF-LIwc8ATSkQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520192013124?e=1795651200&v=beta&t=td-dYmQjopdDw0GkuOVQmevejAMbiUunvCsnU_3KDdI)

Figure 6. You have had up to the limit of output variables reference panels for any plot.

![](https://media.licdn.com/dms/image/v2/C4E12AQE2DQuhHdXUEg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520477155001?e=1795651200&v=beta&t=BC6wwvlgUXIU9G0z9j1kXv3piWex-7jeLD5maRsTJ0M)

Figure 7. The Reference Graph Tool allows you to see many Scenarios on one graph.

Every single node, link, subcatchment, LID or 2D variable can be plotted on either one reference panel with multiple axes or multiple reference panels (Figure 6). The Reference sources can be either the Calibration data, other saved scenario output from the current model or a custom ASCII Text file (Figure 7). The Quick Multiple Graph Axes allows the modeler to see all 14 System variables on one graph with clear Axes for example(Figure 8). The Advanced Reference option allows you to mix and match custom reference axes and custom reference panels from the same element, another element or disparate elements (Figure 9). Figure 8 in particular shows how you can view all of the major flow sources and outlets of the whole network in one view. It allows you to view all of the Wet Weather Components, the Dry Weather Flow Components, Surface Flooding, Storage and Outflow as a holistic understandable graph in comparison to the rainfall This aids in model comprehension, model calibration and model verification.

![](https://media.licdn.com/dms/image/v2/C5112AQHGpHD7A9nzvQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520249963162?e=1795651200&v=beta&t=PAlngdaA2anB5NIZwYS_BkpGJ_W6etkxnARXRaDsU9s)

Figure 8. The Reference Axes tool allow you to see all of the System data in one graph.

![](https://media.licdn.com/dms/image/v2/C5112AQHL1AzTY-pj4w/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520145325667?e=1795651200&v=beta&t=A-qvEk1yicbqTCD2x0bUbynFkCMlC0RFipQTp-tXrbw)

Figure 9. The Advanced Reference and Reference page tool allows you to mix Calibration graphs with other element data in other panels or on the same graph with multiple axes.

![](https://media.licdn.com/dms/image/v2/C5112AQGs_GIj2QSSPg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520249903612?e=1795651200&v=beta&t=NK7uU0OrtpQs3Gk57lbHh9aVkvOB99ndLOPsaRM5D5o)

Figure 10. Reference Axes show the Time Lag between Rainfall and the Total Flow at the Outfalls

The ability to combine Reference Axes and Reference Panels for all model elements allows you to plot the rainfall at an upstream Subcatchment against the flow at all of the Outfall nodes (Figure 10). This is a surrogate estimate of the time of concentration for the modeled basin. All of the graphs can be customized as well and the customization saved to a ChartProperties.xml file for use in another InfoSWMM or H2OMAP SWMM Model.

![](https://media.licdn.com/dms/image/v2/C4E12AQGnLeTkTq3-sg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520477155137?e=1795651200&v=beta&t=0onPJUN-54cbUbd_6NZ44MufxQ6r6jZCDlEu_MgvQT4)

**InfoSWMM Introduction:** InfoSWMM v13 for ArcGIS 9.3, 10, 10.1, 10.2, 10.3, 10.4, 10.5 (Esri, Redlands, CA). InfoSWMM enables engineers to work more efficiently and reliably with very large and complex network models, thanks to improvements in such areas as built-in 64-bit simulation, enhanced water quality modeling, and batch run scenario management using many of the Arc Map tools developed for InfoWater and InfoSewer.. All operations of a typical sewer system — from analysis and design to management functions such as water quality assessment, pollution prediction, sediment transport and deposition, urban flooding, real-time control, and record keeping — are addressed in a single, fully integrated geoengineering environment. The program’s powerful hydraulic and water quality computational engine is based on the current SWMM 5 version, which is endorsed by the USEPA and certified by FEMA.
