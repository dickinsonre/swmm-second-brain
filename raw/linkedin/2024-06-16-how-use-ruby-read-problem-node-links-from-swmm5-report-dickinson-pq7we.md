---
title: "How to Use Ruby to Read Problem Node and Links from the SWMM5 Report File and Add them as Selected Elements in ICM SWMM"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-ruby-read-problem-node-links-from-swmm5-report-dickinson-pq7we
created: "2024-06-16 01:08"
published: "2024-06-16 09:44"
words: 855
export_sha256: 72cf4d49cc0db32f37aec74f950df5a30fb534ec02de6775a0f0caa53175da7b
---
# How to Use Ruby to Read Problem Node and Links from the SWMM5 Report File and Add them as Selected Elements in ICM SWMM

![How to Use Ruby to Read Problem Node and Links from the SWMM5 Report File and Add them as Selected Elements in ICM SWMM](https://media.licdn.com/mediaD4E12AQHNBST8Wxo9-Q "How to Use Ruby to Read Problem Node and Links from the SWMM5 Report File and Add them as Selected Elements in ICM SWMM")

Utilizing the Tools in the InfoWorks Geoplan in ICM SWMM can greatly enhance understanding and optimization of the SWMM5 model. Here's how integrating specific data sections into the Geoplan interface can improve model comprehension and performance. The Ruby code extracts Each List from the report file and adds them as selected elements.

### Highest Continuity Errors List

**Explanation:** Continuity errors in SWMM5 indicate discrepancies between inflows, outflows, and stored volumes in the model. High continuity errors suggest potential issues in the model configuration or data inaccuracies.

**Benefits of Geoplan Selection:**

- **Visual Identification:** Displaying the highest continuity errors on the Geoplan allows for quick identification of problematic areas in the network.

- **Targeted Investigation:** These elements can be selected and investigated to determine the cause of the errors, facilitating corrections and refinements.

### Time-Step Critical Elements List

**Explanation:** The Courant–Friedrichs–Lewy (CFL) condition is crucial for numerical stability in SWMM5. Elements with small time-step requirements can significantly slow down the simulation. Knowing where they are on the GeoPlan is helpful.

**Benefits of Geoplan Selection:**

- **Highlighting Short Pipes:** By identifying short pipes or critical elements that dictate the time step, you can apply the conduit lengthening option or other adjustments to improve model efficiency.

- **Optimized Performance:** This ensures a more stable and faster-running model without sacrificing accuracy.

### Highest Flow Instability Indexes List

**Explanation:** Flow instability in model elements can lead to oscillations and unreliable results. The flow instability index measures the extent of these oscillations.

**Benefits of Geoplan Selection:**

- **Spotting Instabilities:** Displaying the highest instability indexes on the Geoplan helps pinpoint where flow oscillations are most severe.

- **Focused Analysis:** Engineers can graph these elements to analyze instability patterns and implement stabilization measures, such as adjusting parameters or adding damping. Graph those links with the highest instability - if those look okay, then the rest of your model, which may be large, should be better. You are looking at the worst-case scenario.

### Most Frequent Nonconverging Nodes List

**Explanation:** Nonconverging nodes indicate areas where the iterative solution process fails to converge within the set tolerance, often due to complex hydraulic conditions.

**Benefits of Geoplan Selection:**

- **Identification of Problem Nodes:** Visualizing the most frequent nonconverging nodes allows you to quickly identify and investigate nodes that need attention.

- **Improving Convergence:** Adjusting model parameters at these nodes, such as modifying time steps or area or revising boundary conditions, can enhance overall model stability.

### Routing Time Step Summary List

**Explanation:** The routing time step summary provides an overview of the time steps used throughout the simulation, influenced by the variable CFL condition and other factors.

**Benefits of Geoplan:**

- **Overall Time Step Analysis:** By adding this summary to the Geoplan, you can monitor time-step variations across the model.

- **Adjustment and Optimization:** This allows adjustments to be made where necessary, ensuring that the model runs efficiently while maintaining stability.

### Implementation and Investigation

**How to Implement:**

1.  **Import Data:** Integrate the specific sections (Highest Continuity Errors, Time-Step Critical Elements, etc.) into InfoWorks's Geoplan interface using ICM SWMM Networks (Figure 1).

2.  **Visualization:** Using the Geoplan to visualize these elements makes them easy to identify and select.

3.  **Analysis:** Select and graph the elements to investigate their behavior, analyze the causes of errors or instabilities, and make informed adjustments.

4.  **Optimization:** Apply appropriate options, such as conduit lengthening, parameter adjustments, or other corrective measures, to optimize model performance.

By leveraging the Geoplan interface to visualize and investigate these critical aspects, you can gain deeper insights into the SWMM5 model, identify and resolve issues more effectively, and ensure a stable and efficient simulation (Figure 2).

![](https://media.licdn.com/dms/image/v2/D4E12AQFqxI9Lv4q9Vg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718500317078?e=1795651200&v=beta&t=5sdVxOaIo-ZjchWrF0UEzywAWxfcFxbFhrZ_Z8J1YKk)

Figure 1. Dialog to Decide which SWMM5 Sections from the Import File you want to import to ICM and add as selected Elements on the GeoPlan and Grid.

![](https://media.licdn.com/dms/image/v2/D4E12AQE-qxh3IBry4A/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718529638971?e=1795651200&v=beta&t=XwvKaqV95Dbceft7Ucb0Ugc39Ihjm4MsNBOREJGF4XM)

Figure 2. How to Use Ruby to Read Problem Node and Links from the SWMM5 Report File and add them as Selected Elements in ICM SWMM

> **Ruby Code for Reading the SWMM5 File**

[01 InfoWorks ICM/01 Ruby/02 SWMM/0151 - Read SWMM5 RPT File](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0151%20-%20Read%20SWMM5%20RPT%20File)

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

![](https://media.licdn.com/dms/image/v2/D4E12AQFS-4By3ucukg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718500183551?e=1795651200&v=beta&t=lOkykOsxvXwvex0oYfr-qZq18BGI4yucONB7qdGhUMg)

**Obligatory AI Midjourney Image**
