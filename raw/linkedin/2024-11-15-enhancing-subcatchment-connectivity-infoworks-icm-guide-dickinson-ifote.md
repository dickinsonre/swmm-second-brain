---
title: "Enhancing Subcatchment Connectivity in InfoWorks ICM: A Step-by-Step Guide Using Ruby Scripting"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/enhancing-subcatchment-connectivity-infoworks-icm-guide-dickinson-ifote
created: "2024-03-23 22:16"
published: "2024-11-15 01:35"
words: 1529
export_sha256: 6c5abad3b00625241a0a62af8d98e115a585015c3a14067ba6f3a521b083f835
---
# Enhancing Subcatchment Connectivity in InfoWorks ICM: A Step-by-Step Guide Using Ruby Scripting

![](https://media.licdn.com/mediaD4E12AQHWReJLmJTSrA)

## Enhancing Subcatchment Connectivity in InfoWorks ICM: A Step-by-Step Guide Using Ruby Scripting

This Ruby script is designed for use within InfoWorks ICM to associate subcatchments with the nearest node with the lowest ground level among five nodes. It performs several tasks to facilitate this connection between subcatchments and nodes in a stormwater or sewer model. Finding the correct receiving node for a subcatchment based on ground elevation is crucial for several important reasons:

> **\## Hydrological Accuracy**

**Natural Flow Patterns**

\- Water naturally flows downhill following topographical features

\- Natural drainage characteristics should not be altered to prevent system failures\[3\]

\- Incorrect node connections can lead to unrealistic flow patterns and model inaccuracies

**Critical Design Considerations**

\- Improper outlet selection can cause:

\- Ponding above road fills

\- Weakening/erosion of subgrades

\- Overloading of downstream systems\[3\]

> **\## Technical Requirements**

**Flow Direction Analysis**

\- Elevation and slope data help determine the likeliest manhole that would receive runoff from each subcatchment\[1\]

\- Topography impacts overall runoff volume and flow patterns

\- Slope shape (uniform, convex, concave) indicates surface and subsurface water concentration\[3\]

> **System Performance**

\- Incorrect connections can lead to:

\- Road surface erosion

\- Cut or fill failures

\- Mass failures due to inadequate drainage\[3\]

\- Proper node selection ensures the model accurately represents real-world conditions

The goal is to maintain natural drainage patterns while ensuring efficient stormwater management. Using elevation data helps identify the most appropriate receiving nodes that align with natural topography and flow paths.

Citations:

\[1\] [https://www.openswmm.org/Topic/33818/how-to-know-which-node-to-connect-the-sub-catchment-to](https://www.openswmm.org/Topic/33818/how-to-know-which-node-to-connect-the-sub-catchment-to)

> \### Step-by-Step Breakdown:

1\. **Initial Node Selection and Array Preparation**:

\- The script begins by accessing the current InfoWorks ICM network (\`net = WSApplication.current_network\`).

\- It iterates over all nodes (\`hw_node\` objects) and stores key attributes of each node that is currently selected. This includes the node ID, x and y coordinates, system type (e.g., stormwater, foul, etc.), and the ground level. The nodes' data is stored in an array called nodes, which will be used for further processing.

2\. **Start of Transaction**:

\- The script initiates a transaction (\`net.transaction_begin\`) to make changes to the network in a controlled way, ensuring all operations are performed as one atomic update.

3\. **Processing Selected Subcatchments**:

\- The script then moves on to the subcatchments (\`hw_subcatchment\` objects) in the network. It iterates over each subcatchment that is selected and aims to associate it with the nearest node with the lowest ground level.

For each selected subcatchment, it calculates its position (\`sx\` and sy) and initializes several variables to keep track of the distances to the nearest nodes of each system type.

![](https://media.licdn.com/dms/image/v2/D4E12AQG4V6POyHuWuA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1731630970053?e=1795651200&v=beta&t=QhoKxvlg5C3gLYW1_7WhPjM4fNZiogW5akLNUJx4jj8)

4\. **Distance Calculation for Nodes**:

\- The script calculates the squared Euclidean distance between the subcatchment and every node in the network (\`distance = ((sx - nx) *(sx - nx)) + ((sy - ny)* (sy - ny))\`). The distance value is squared to simplify the calculations, avoiding the computational overhead of square roots.

\- Each node’s ID, system type, and ground level are also stored in an array called nodes_with_distances, allowing easy reference later.

## A Smart Approach to Node Assignment

This Ruby script is designed for use within InfoWorks ICM to associate subcatchments with the nearest node that has the lowest ground level among a selection of nodes. It performs several tasks to facilitate this connection between subcatchments and nodes in a stormwater or sewer model.

\### Step-by-Step Breakdown:

1\. **Initial Node Selection and Array Preparation**:

\- The script begins by accessing the current InfoWorks ICM network (\`net = WSApplication.current_network\`).

\- It iterates over all nodes (\`hw_node\` objects) and stores key attributes of each node that is currently selected. This includes the node ID, x and y coordinates, system type (e.g., stormwater, foul, etc.), and the ground level. The nodes' data is stored in an array called nodes, which will be used for further processing.

2\. **Start of Transaction**:

\- The script initiates a transaction (\`net.transaction_begin\`) to make changes to the network in a controlled way, ensuring all operations are performed as one atomic update.

3\. **Processing Selected Subcatchments**:

\- The script then moves on to the subcatchments (\`hw_subcatchment\` objects) in the network. It iterates over each subcatchment that is selected and aims to associate it with the nearest node with the lowest ground level.

For each selected subcatchment, it calculates its position (\`sx\` and sy) and initializes several variables to keep track of the distances to the nearest nodes of each system type.

![](https://media.licdn.com/dms/image/v2/D4E12AQFV9dXwUCyXmw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1731630039040?e=1795651200&v=beta&t=po1XSBt7Ce7ff8KyEa2u-IvDMbTXVi7tGyyH2bzfNB0)

Processing Selected Subcatchments

4\. **Distance Calculation for Nodes**:

\- The script calculates the squared Euclidean distance between the subcatchment and every node in the network (\`distance = ((sx - nx) *(sx - nx)) + ((sy - ny)* (sy - ny))\`). The distance value is squared to simplify the calculations, avoiding the computational overhead of square roots.

\- Each node’s ID, system type, and ground level are also stored in an array called nodes_with_distances, allowing easy reference later.

![](https://media.licdn.com/dms/image/v2/D4E12AQGU1mTT1PYQbw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1731630173153?e=1795651200&v=beta&t=1KTN113pfj8fdmZsv7q_i4KhZXgTgHYVcjGb6xJwj_E)

Distance Calculation for Nodes:

5\. **Sorting and Selection of Nearest Nodes**:

\- Once all distances are computed, the script sorts the nodes by distance (\`sorted_nodes = nodes_with_distances.sort_by { \|node\| node\[:distance\] }\`).

\- It selects the **five closest nodes** (\`nearest_5_nodes = sorted_nodes.first(5)\`) and further analyzes these nodes to determine which one has the **lowest ground level** (\`lowest_ground_level_node = nearest_5_nodes.min_by { \|node\| node\[:ground_level\] }\`).

![](https://media.licdn.com/dms/image/v2/D4E12AQFFUYr8h13Qog/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1731630375368?e=1795651200&v=beta&t=LEsWTYqpdYDjWPvjeTX0qthDTHvY0ehrrYCLKUfpBeg)

Sorting and Selection of Nearest Nodes:

6\. **Updating Subcatchments**:

\- The subcatchment (\`s\`) is then updated with the ID of the nearest node that has the lowest ground level (\`s.node_id = lowest_ground_level_node\[:id\]\`).

\- If such a node is found, the script increments the changed_nodes_count counter and writes the changes (\`s.write\`).

7\. **Commit Changes**:

\- After all subcatchments are processed, the transaction is committed (\`net.transaction_commit\`), meaning all updates are saved to the network in InfoWorks ICM.

\- The script then prints out the total number of nodes that were checked and updated (\`puts "Number of nodes checked: \#{changed_nodes_count}"\`).

\### Summary of Purpose:

This script efficiently connects subcatchments to nodes in a network, prioritizing the nearest node with the lowest ground level, which is particularly useful for accurately modeling overland flow and runoff routing in a complex urban drainage system. By selecting the lowest ground-level node among the closest nodes, the script ensures that the subcatchment's connectivity is realistically represented, contributing to more accurate hydrodynamic simulation results.

For data integrity, the process is wrapped in a transaction, and using sorted nodes allows for a targeted association to ensure hydraulic consistency. This is especially important in modeling situations where the exact representation of subcatchment dynamics is needed.

![](https://media.licdn.com/dms/image/v2/D4E12AQEpscC0b91ECQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1726022502864?e=1795651200&v=beta&t=3mmls60p0qLmbe-YJxsmXxGlKzbJfiuhubrUq8JY-mk)

Enhancing Subcatchment Connectivity in InfoWorks ICM: A Step-by-Step Guide Using Ruby Scripting

> **Location of the Ruby Code on the Innovyze GitHub**

[01 InfoWorks ICM/01 Ruby/01 InfoWorks/0004 - Connect subcatchment to nearest node](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/01%20InfoWorks/0004%20-%20Connect%20subcatchment%20to%20nearest%20node)

### ICM Ruby Scripting & Drainage Quiz

1.  What is the primary reason for determining a subcatchment's receiving node based on ground elevation? A) To reduce computational time; B) To match natural flow patterns and topographical features C) To simplify the model structure; D) To meet software requirements Answer: B

2.  In a Ruby script for ICM, which of the following would be most important when writing code to find receiving nodes? A) Color coding of manholes B) Pipe material types C) Elevation and slope data comparison D) Manhole naming conventions Answer: C

3.  What potential system failure could occur from incorrect receiving node assignment?A) Software crashes B) Database corruption C) Ponding above road fills D) Network disconnection Answer: C

4.  When writing a Ruby script for receiving node analysis, which data structure would be most appropriate for storing elevation comparisons? A) Single-string variable B) Hash table with elevation keys C) Boolean array D) Text file Answer: B

5.  What critical design considerations should a Ruby script include for automated receiving node selection? A) Manhole depth only; B) Pipe diameter only; C) Surface slope shape (uniform, convex, concave); D) Manhole material type Answer: C

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while only universally relevant at some times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
