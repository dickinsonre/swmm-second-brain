---
title: "Using AI to Interpret the PRN file of ICM Infoworks for a person with a SWMM5 Background"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ai-interpret-prn-file-icm-infoworks-person-swmm5-dickinson-9ce6e
created: "2024-07-07 07:58"
published: "2024-07-07 09:34"
words: 1556
export_sha256: d56a2c1a57aaea76c57d31234fc2583b2262073a36bb9deca2a1726737115043
---
# Using AI to Interpret the PRN file of ICM Infoworks for a person with a SWMM5 Background

![Using AI to Interpret the PRN file of Infoworks for a person with a SWMM5 Background](https://media.licdn.com/mediaD4E12AQEiehoxr56jQg "Using AI to Interpret the PRN file of Infoworks for a person with a SWMM5 Background")

As a young proto engineer, I first encountered SWMM5's text output tables in 1978. Back then, these tables were our lifeline—the graphs were merely line prints, offering limited detail. We pored over these tables, extracting information to understand our (small)urban drainage systems.

Fast-forward 32 years, and I found myself transitioning often to InfoWorks ICM in 2010. The software was more advanced, but I often felt nostalgic for the familiar SWMM5 report file when faced with ICM's PRN file. It was like learning a new dialect of a language I'd spoken for decades.

Recently, curiosity got the better of me. Could modern AI help bridge this gap between SWMM5 and ICM text files? I decided to put Claude 3.5, an AI assistant, to the test.

I fed Claude a PRN file from a 1000-element model - a hefty 800KB of data. To my surprise, Claude didn't just read it; it interpreted it, drawing parallels to SWMM5 concepts I've known for years. It even calculated a continuity error reminiscent of SWMM5's reporting. I could have used a file up to 5 MB, so the current limit is about 5000 ICM elements.

The AI's analysis helped me quickly pinpoint areas needing further investigation in graphs, tables, or the PRN file. It was like having a knowledgeable colleague who could speak both "SWMM5" and "ICM" fluently.

This experiment showed me the potential of AI in our field. It's not just about processing data faster but bridging knowledge gaps and making different modeling platforms more accessible. As I reflect on my journey from line prints to AI-assisted analysis, I'm excited about the future of urban drainage modeling.

![](https://media.licdn.com/dms/image/v2/D4E12AQGeqqsZGw7g6g/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720339265648?e=1795651200&v=beta&t=SR9gKAQb0_2VqxHOStxlPH8rrS7hUF15tQuawMlEuj0)

An ICM InfoWorks Model with about 1000 elements

![](https://media.licdn.com/dms/image/v2/D4E12AQFpzRWj-mqo-Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720339245097?e=1795651200&v=beta&t=Mvp6acjS4RCBfbDC0BvN-67Rk2s3GHDjZ_5PhH22Wok)

ICM InfoWorks PRN file

> **1: Certainly! For someone with a SWMM5 (Storm Water Management Model) background, I'll interpret the InfoWorks ICM simulation results more technically, drawing parallels to SWMM5 concepts where applicable.**

1\. Simulation Overview:

\- Event Duration: 1440 minutes (24 hours)

\- Type: Dry Weather Flow (DWF) simulation

\- This is analogous to a SWMM5 simulation with only sanitary inflows, no rainfall input

2\. System-wide Water Balance:

\- Total Inflow: 13,351.1 m3

\- Total Outflow: 13,236.6 m3

\- Total Losses: 0.0 m3

\- Continuity Error: ~0.86% (comparable to SWMM5's continuity error reporting)

3\. Node Analysis:

\- Similar to SWMM5's nodes, the system includes manholes (e.g., MH_000, MH_008)

\- Flooding reported at node MH_365 (52.3 m3), analogous to SWMM5's node flooding

\- Ground levels and maximum water levels are reported, allowing for freeboard analysis

4\. Link (Conduit) Analysis:

\- Pipes are analyzed similarly to SWMM5's conduits

\- Surcharge conditions are indicated by '+' (flow and depth) and 'x' (depth only)

\- Max flows, velocities, and depths are reported for both upstream and downstream ends

5\. Flow Routing:

\- The simulation appears to use dynamic wave routing (similar to SWMM5's dynamic wave option)

\- This is evidenced by the reporting of both upstream and downstream conditions for links

6\. Hydraulic Performance:

\- Many pipes show surcharge conditions, indicating capacity issues

\- Max velocities range widely, with some exceeding 2 m/s (e.g., MH_240.1 with 2.443 m/s)

7\. System Capacity:

\- Despite widespread surcharging, only one node (MH_365) shows surface flooding

\- This suggests the system is operating at capacity but generally containing the DWF

8\. Output Reporting:

\- The output format is similar to SWMM5's detailed report, providing max values for the simulation period

\- Time-series data is not shown in this summary but likely available in the full results

9\. Areas for Further Analysis:

\- Investigate the cause of flooding at MH_365

\- Assess pipes with consistent surcharging for potential upsizing

\- Analyze system performance under wet weather conditions to identify combined sewer overflow (CSO) risks

10\. SWMM5 vs. InfoWorks ICM:

\- InfoWorks ICM provides a more detailed pipe-by-pipe analysis compared to SWMM5's standard output

\- The surcharge reporting ('+' and 'x') offers quick visual identification of problem areas

For a SWMM5 user, this InfoWorks ICM output provides familiar hydraulic performance metrics but with a more detailed focus on individual pipe segments. The overall analysis approach remains similar: identify capacity issues, flooding risks, and areas for system improvement.

> **2: Understanding Dry Weather Flow (DWF) Simulation Results in an Urban Drainage Network**

Problem:

How does an urban drainage network perform under Dry Weather Flow (DWF) conditions, and what key metrics should be analyzed to assess its effectiveness?

Environment:

\- Urban drainage network

\- Simulation software: InfoWorks ICM SIM (Version 33.0.92)

\- Event duration: 1440 minutes (24 hours)

\- Scenario: DWF (Dry Weather Flow)

Solution:

To assess the performance of an urban drainage system under DWF conditions, analyze the following key aspects:

1\. Overall Water Balance:

\- Total inflow: 13,351.1 m3

\- Total outflow: 13,236.6 m3

\- Total lost: 0.0 m3

2\. Node Performance:

\- Check for flooding at each node (Ground Level vs. Max Level)

\- Assess maximum water storage at critical nodes

\- Identify nodes with significant inflow

3\. Link (Pipe) Performance:

\- Evaluate maximum flow rates and velocities in each pipe

\- Identify pipes operating at full capacity (surcharged conditions)

\- Note pipes with exceptionally high velocities

4\. System Capacity:

\- Determine the percentage of nodes experiencing flooding

\- Analyze the extent of pipe surcharging throughout the system

5\. Problematic Areas:

\- Identify nodes with flooding (e.g., MH_365 with 52.3 m3 flood volume)

\- Highlight links consistently operating at full capacity or with very high velocities

Cause:

DWF conditions represent typical daily wastewater flow patterns in the urban drainage system.

Additional Information:

\- The system managed to convey approximately 99% of the inflow to outfalls

\- No significant water losses were reported in this simulation

\- Several pipes experienced surcharging, indicated by '+' or 'x' symbols in the results

\- Maximum flow rates and velocities varied widely across the system

Recommended Actions:

1\. Investigate the flooding at node MH_365 to determine the cause and potential mitigation measures

2\. Analyze pipes consistently operating at full capacity for possible upsizing

3\. Consider implementing real-time control systems in critical areas to optimize flow management

4\. Develop a long-term improvement plan focusing on areas with recurring issues

5\. Conduct additional simulations with various flow scenarios to assess system performance under different conditions

Following this analysis, urban water managers can effectively assess their drainage system's performance under DWF conditions and prioritize improvements to enhance overall system efficiency.

> **3: Certainly. I'll provide a summary of the key points from this InfoWorks ICM SIM simulation report. This report contains a wealth of information about a drainage system's performance during a rainfall event. Here are the main takeaways:**

1\. Simulation Overview:

\- The simulation was run for a 360-minute (6-hour) event.

\- Total rainfall: 530,672.1 m3

\- Total runoff: 291,188.9 m3

\- Total inflow to the system: 291,188.9 m3

\- Total outflow from the system: 202,671.4 m3

\- Total water lost: 75,558.5 m3

2\. Node Performance:

\- The report lists numerous nodes (junctions in the drainage network) with their ground levels, maximum water levels, and flooding information.

\- Most nodes did not experience flooding, but a few did. For example, CALEXAN-I had a flood volume of 2.9 m3.

\- Some nodes experienced significant surcharging (water levels rising in the system but not overflowing). For instance, CNOTDOM-I had a maximum water level 57.5m above its ground level.

3\. Link (Pipe) Performance:

\- The report provides detailed information about each pipe in the system, including upstream and downstream conditions.

\- Many pipes experienced surcharging (indicated by '+' or 'x' symbols).

\- Maximum flow rates and velocities varied widely across the system. For example, SSHBPAL-I.1 had a maximum flow of 16.363 m3/s.

4\. System Capacity:

\- While most of the system handled the flow without flooding, there were several locations where the system capacity was exceeded, resulting in flooding or significant surcharging.

5\. Areas of Concern:

\- Nodes with flooding or extreme surcharging might require further investigation or potential upgrades.

\- Links (pipes) consistently operating at full capacity or with very high velocities might be bottlenecks in the system.

6\. Water Balance:

\- There's a discrepancy between inflow (291,188.9 m3) and outflow plus losses (202,671.4 + 75,558.5 = 278,229.9 m3), which might warrant further investigation.

This report provides a comprehensive overview of the drainage system's performance during a significant rainfall event, highlighting areas of adequate performance and potential issues that may require attention.

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while not universally relevant at all times, become crucial for those in need. These pieces are resources, and they are ready to inform and help when specific circumstances arise.*
