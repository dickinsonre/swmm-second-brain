---
title: "Using Ruby to Add More Results Points to a Link in ICM InfoWorks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-add-more-results-points-link-icm-infoworks-dickinson-jkpye
created: "2024-02-19 00:16"
published: "2024-02-19 01:11"
words: 750
export_sha256: 1c7b18e6e86dfd573b7822a21aea12e82f55d7718cef272c521a493ed8cb7435
---
# Using Ruby to Add More Results Points to a Link in ICM InfoWorks

![ICM InfoWorks Computational Points (Top) and SWMM5 (bottom)](https://media.licdn.com/mediaD4E12AQHVzskrHaAbnw "ICM InfoWorks Computational Points (Top) and SWMM5 (bottom)")

ICM InfoWorks provides two result points at the upstream and downstream ends of each conduit, however, it supports more than just the minimum five computational nodes for enhanced hydraulic detail. The addition of 1D result points beyond the default or minimum configuration, as facilitated by the **Ruby** script, enriches the simulation's detail further. Specifically, the script introduces nine extra result points at intervals of 10 percent along the length of the conduit. This enhancement allows users to observe a more nuanced flow profile within the conduit, offering insights into the hydraulic conditions at intermediate points between the conduit's upstream and downstream ends. This capability is particularly valuable for detailed hydraulic studies, enabling precise analyses and informed decision-making in water management and engineering projects.

In the simulation options, "Minimum Number of Computational Nodes" refers to the least number of points within a conduit where calculations are performed in hydraulic modeling software. By default, every conduit is ensured to have a minimum of five computational nodes. This ensures that the software can simulate the hydraulic behavior within each conduit with a basic level of detail. However, the software is designed to increase this number if other parameters specifying the spatial resolution of the model (space step parameters) suggest that a higher resolution (i.e., more computational nodes) is necessary for accurate simulations.

![](https://media.licdn.com/dms/image/v2/D4E12AQE2ND8j_NzQgg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708301899934?e=1795651200&v=beta&t=4kcrhiZ8GdForVyY4-qXakbTwZ6ylr5u9o3YxXIL4_o)

**Once the Ruby code is run, the new data points are added to the links.**

![](https://media.licdn.com/dms/image/v2/D4E12AQGjRbpI-GLfxQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1708301918146?e=1795651200&v=beta&t=Q-yzNuDzCjpNpJyvRqgcnQntvPlkqQh4ZJ8J_sj3zgc)

Now that 9 extra result points are added to the links, we can see how the depth varies along the link. The flow is about the same at any point.

> How does the Code Work?

This script is designed to interact with a hydraulic modeling software's API, specifically targeting the manipulation of network data for the purpose of generating result points along selected hydraulic conduits. Here's a step-by-step summary:

1.  **Access the Current Network**: The script starts by accessing the currently loaded hydraulic network within the software. It raises an error if no network is currently loaded.

2.  **Access Row Objects**: It then attempts to access various types of row objects (data representations within the software), such as nodes, links, and subcatchments. For each type, it checks if these objects are found; if not, an error is raised.

3.  **Transaction Begin**: initiates a transaction, which allows for batch processing of changes to the network data. This is a critical feature for ensuring data integrity and for rolling back changes if an error occurs.

4.  **Define Result Point Percentages**: The script defines a set of percentages that determine where along each selected conduit result points will be added. These percentages represent the positions along the conduit's length.

5.  **Iterate Through Selected Links**: For each selected conduit (identified as 'hw_conduit'), the script performs the following steps:

    Retrieves the upstream and downstream nodes of the conduit.Calculates the x, y coordinates for these nodes.For each defined percentage, calculates the intermediate position along the conduit where a result point will be added.Creates a new result point object ('hw_1d_results_point') at each calculated position, setting its properties based on the current conduit and the calculated position.Writes the new result point object to the database.

6.  **Commit Transaction**: Once all result points have been added, the script commits the transaction, finalizing the changes to the network data.

7.  **Clear Selection**: Clears any selections made during the process to clean up the session.

8.  **Error Handling**: Includes basic error handling to catch and report errors during the script's execution.

This script automates the process of adding detailed result points along selected conduits, enhancing the granularity of hydraulic analysis by allowing for more precise observation of flow characteristics at specified intervals along a conduit.

> Ruby Code for adding 1D Results Points

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
