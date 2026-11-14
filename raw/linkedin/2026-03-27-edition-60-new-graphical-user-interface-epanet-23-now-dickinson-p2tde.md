---
title: "Edition 60: New Graphical User Interface for EPANET 2.3 Now Available - Lew Rossman on GitHub"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-60-new-graphical-user-interface-epanet-23-now-dickinson-p2tde
created: "2026-03-27 07:46"
published: "2026-03-27 08:24"
words: 400
export_sha256: 786f8828fc15ca53182630889aec9873e3b4c9c3b513ba625cdbeb395c11e79a
---
# Edition 60: New Graphical User Interface for EPANET 2.3 Now Available - Lew Rossman on GitHub

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![New Graphical User Interface for EPANET Now Available - Lew Rossman on GitHub](https://media.licdn.com/mediaD4E12AQHdlWVh7qi8NQ "New Graphical User Interface for EPANET Now Available - Lew Rossman on GitHub")

The new UX looks great and even has GIS features. The code is on GitHub, and the UX here: [https://sites.google.com/view/epanet-ui](https://sites.google.com/view/epanet-ui)

[EPANET-UI](https://sites.google.com/view/epanet-ui) allows users to visually design a pipe network, edit its properties, run a simulation, and view the results in a variety of formats. The user interface:

- offers a modern and simple design

- runs on Windows, Linux and MacOS

- has full support for EPANET's multi-species water quality (MSX) extension

- can import data from GIS shapefiles and DXF CAD files

- can use web mapping services to provide background basemaps

- It includes multiple reporting options for simulation results.

> **From Lew Rossman on GitHub**

The source code has been posted to [https://github.com/OpenWaterAnalytics/EPANET-UI](https://github.com/OpenWaterAnalytics/EPANET-UI) and executable binaries for both Windows and Linux can be downloaded from [here](https://sites.google.com/view/epanet-ui). If you encounter any issues when testing the UI, it's best to raise them on the EPANET-UI site rather than here.

> **From the Lew Rossman Help File**

A unique feature of EPANET-UI is that it uses the EPANET Toolkit to store and retrieve project data from the engine itself as users interact with the UI, thus avoiding the need to have one copy of a project's data reside inside the UI and another exported to the engine when an analysis is requested. Also, the same code can be compiled to run on Windows, Linux, and macOS with just some minor edits to a configuration file (is anyone willing to volunteer to produce a Mac executable?).

The EPANET-UI repository is forked from the US EPA's [EPANET repository](https://github.com/USEPA/EPANET) and the two will be kept in sync with one another so that the new UI can potentially become an official EPA release.
