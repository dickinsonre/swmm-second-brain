---
title: "Using Ruby to add Nodes to Subcatchments and Polygons in ICM InfoWorks and SWMM Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-add-nodes-subcatchments-polygons-icm-swmm-robert-dickinson-czxle
created: "2024-01-27 17:53"
published: "2024-01-31 23:11"
words: 859
export_sha256: 08bf0d06893dc7d17d5eeafe21120ff7762fa3318b7a42511388354f79bd5a43
---
# Using Ruby to add Nodes to Subcatchments and Polygons in ICM InfoWorks and SWMM Networks

![Using Ruby to add Nodes to ICM InfoWorks and SWMM Networks](https://media.licdn.com/mediaD4E12AQEl4fawif_dfQ "Using Ruby to add Nodes to ICM InfoWorks and SWMM Networks")

This Ruby code to add nodes to selected polygons could be important and useful to InfoWorks ICM and SWMM modelers for a few reasons:

1.  Allows automated subdivision of large subcatchments or polygons: By adding a centroid node and vertex nodes, this code provides a way to easily subdivide large subcatchments or polygons into smaller areas. This can help improve model accuracy. **I like it for making test models to show how a feature works in ICM or SWMM**.

2.  Facilitates parameter assignment: The added nodes allow modelers to easily assign different parameters (roughness, infiltration rate, etc) to different sections of a large subcatchment based on land use, soil type etc. **Micro catchments.**

3.  Enables detailed modeling: Adding nodes to polygons enables users to model each sub-section explicitly as a subcatchment with its own parameters. This allows for more detailed modeling.

4.  Supports result mapping and visualization: The added nodes provide additional points where results can be mapped or visualized, allowing users to see the spatial distribution.

5.  Aid in model calibration: Comparing results at vertex nodes with observed data can guide subcatchement parameter calibration to match real-world measurements.

> Section 1: How does it Work?

The Ruby script reads the polygon boundary of a subcatchment or polygon, finds the vertex points and centroid, and makes a new node.

Here is the network before: no nodes in the polygon and only an outlet node for the subcatchment.

After running the script for hw_polygons, the new nodes at the polygon points and the centroid of the shape area are added.

After running the script for hw_subcatchment, the new nodes at the subcatchment vertices and the centroid of the subcatchment area are added.

![](https://media.licdn.com/dms/image/v2/D4E12AQFLVmv3piFIJA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1706453266243?e=1795651200&v=beta&t=vU4966Cb-DE93c-mIfkDM638yf9yLKdtJ8QxVcHLTig)

The small model before the new nodes are added by Ruby. The red shapes are polygons. The other colored shapes are subcatchments.

1.  

![](https://media.licdn.com/dms/image/v2/D4E12AQHiHMyfHz7X1A/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1706453311348?e=1795651200&v=beta&t=aNhAMMWomBuslIJnRw17MeY-f5g_t_e7JfI8mukjmSM)

After running the script for hw_polygons, the new nodes at the polygon points and the centroid of the shape area are added.

![](https://media.licdn.com/dms/image/v2/D4E12AQEjzqwWSeXqhA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1706453182866?e=1795651200&v=beta&t=WgNulY3OGedyOeNo8Ov0cVuJRnLDS2ctGWlHZwOO_QI)

After running the script for hw_subcatchment, the new nodes at the subcatchment vertices and the centroid of the subcatchment area are added.

> Section 2: InfoWorks SIM and SWMM SWMMSim Engines

![](https://media.licdn.com/dms/image/v2/D4E12AQFIqfPVr2P7uA/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1706378028000?e=1795651200&v=beta&t=5H3y28y78whzU2-IfWxs3RLD4UNoRiiQz5FjMyY79Xw)

InfoWorks SIM and SWMM SWMMSim Engines and Table Names

![](https://media.licdn.com/dms/image/v2/D4E12AQFF6Rvnp5Emmg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1706394885277?e=1795651200&v=beta&t=m6QdIzmNZ6sskwgfCuRaJWlIEvLQMGdVnIHYpTsm6jA)

This script creates new nodes at the centroid and periphery of each selected polygon or subcatchment in an InfoWorks network.

> Section 2: [Readme.md](http://Readme.md) file for the Ruby Code

> **Section 3:** Where do I find this code for ICM InfoWorks and SWMM Networks**?**

You can find the Ruby code for both the ICM InfoWorks and SWMM Networks from the InfoWorks [ICM Technical Information Hub for InfoWorks and SWMM Networks](https://boards.autodesk.com/4bf242?token=a671af9e76) in the subfolder 01 InfoWorks ICM\01 Ruby\02 SWMM**0021 - Create nodes from polygon, subcatchment boundary**

> **Section 4: Copy of Code for ICM SWMM and InfoWorks Networks**

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).

> **Extra Poem**

In the world of water, so vast and so wide, A Ruby script's journey, a tech-savvy guide. 🔺 To subcatchments large, it brings a new node, Subdividing areas, a helpful new code.

🌍 For land of different uses, a parameter's tune, Roughness and infiltration, under sun and moon. 🌱 In soil type's embrace, each section's own trait, Micro catchments it forms, with detail so great.

🌐 In modeling's realm, where data's king, Nodes in polygons, such clarity they bring. Each sub-section modeled, with care and with might, Detailing the water's flow, both day and night.

🔍 For results to be seen, in maps so vivid, Visualization's key, in this domain vivid. 📍 At each node, results take a stand, Mapping the journey, across the watered land.

🔄 Calibration's aid, a tool so profound, Matching reality, where truth is found. 📊 At vertex nodes, observations align, For models so real, like stars that shine.

In this world of water, where Ruby code plays, Accuracy and insight, in so many ways. 🌊 For modelers of ICM, and SWMM's deep dive, This script's a beacon, making models come alive.
