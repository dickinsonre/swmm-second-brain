---
title: "How to use Ruby for Subcatchments Statistics using the Current and Background Networks in ICM"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-ruby-subcatchments-statistics-using-current-icm-dickinson-rm2ve
created: "2024-03-28 02:46"
published: "2024-04-26 00:43"
words: 1602
export_sha256: 2bcd6a13ccae888bcd6fcebbbbc8a0eeea0a73e1c8419daf266ccf1cbcf255f2
---
# How to use Ruby for Subcatchments Statistics using the Current and Background Networks in ICM

![How to use Ruby for Subcatchments Statistics using Current and Background Networks in ICM](https://media.licdn.com/mediaD4E12AQFTgL_6Ig9WlQ "How to use Ruby for Subcatchments Statistics using Current and Background Networks in ICM")

This blog and many future and past blogs are centered around a few key objectives. The first is explaining the integration of **InfoSewer**, **InfoSWMM**, and **XPSWMM** into **ICM InfoWorks** and **ICM SWMM**. This will allow us to consolidate data and functionality from these systems into a unified platform, or Autodesk ICM. We are utilizing two powerful engines, **InfoWorks SIM** and the **SWMM5 SWMMSIM**, to drive our system. These engines will provide the computational power to process and analyze the imported data sets. We also have the capability to convert **ICM InfoWorks** to **ICM SWMM** and vice versa. This will provide greater flexibility and ensure that our system can adapt to a wide range of user needs.

A common user experience (UX) is used for both types of networks. This will ensure a seamless interaction for the users, regardless of the network they are working with, InfoWorks or SWMM. We also have a **Ruby scripting language** that applies to both types of networks. This will provide users with a flexible and powerful tool for customizing their data analysis and manipulation. Many of these blogs cover Ruby and how to use it.

One of our unique features is the ability to have a current and background network on the geoplan. This allows us to use Ruby on both and compare them, providing a unique perspective and deeper understanding of the data. In line with our commitment to transparency and collaboration, we aim for our models to be open source or open information. **We believe that sharing knowledge and resources is key to advancing the SSF field.**

Finally, all these elements contribute to a rigorous **Quality Assurance/Quality Control (QA/QC) process**. This ensures that our system is reliable, accurate, and meets the highest standards of excellence.

> **What does the Code Do? It reads both ICM SWMM and ICM InfoWorks and makes Similar Subcatchment Statistics**

![](https://media.licdn.com/dms/image/v2/D4E12AQG-zO-7T7zy0g/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1714089171161?e=1795651200&v=beta&t=6x6IOWzmYP8UR4A_vvuD-vLWcj4rRgdEIruRJh_R3jM)

ICM InfoWorks Top and ICM SWMM Bottom for a QA/QC Test

The code does the following:

1.  The code starts by initializing the current_network object (cn) and the background_network object (bn) using the WSApplication class. These objects represent the ICM InfoWorks network and the ICM SWMM network, respectively.

2.  The code clears any existing selection in both networks using the clear_selection method to ensure a clean slate.

3.  An empty array called subcatchment_areas is initialized to store the subcatchment areas.

4.  The code then iterates over each subcatchment in the network using the row_objects method with the argument 'hw_subcatchment' for the InfoWorks network and 'sw_subcatchment' for the SWMM network. For each subcatchment, it retrieves the total_area (InfoWorks) or area (SWMM) and adds it to the subcatchment_areas array if it exists.

5.  The code calculates the threshold area for the lowest 10% of subcatchments. It does this by finding the minimum area in the subcatchment_areas array and adding 10% of the range (maximum area - minimum area) to it. This threshold is stored in the threshold_area variable.

6.  The code also calculates the median area (50th percentile) by sorting the subcatchment_areas array and selecting the middle value. This median area is stored in the median_area variable.

7.  An empty array called selected_subcatchments is initialized to store the subcatchments that meet the selection criteria.

8.  The code iterates over each subcatchment in the network again. For each subcatchment, it checks if the total_area (InfoWorks) or area (SWMM) is below either the threshold_area or the median_area. If either condition is true, the subcatchment is marked as selected using ro.selected = true and added to the selected_subcatchments array.

9.  The code calculates the total number of subcatchments by getting the length of the subcatchment_areas array and stores it in the total_subcatchments variable.

10. Finally, the code checks if any subcatchments were selected by checking if the selected_subcatchments array is not empty. If subcatchments were selected, it prints out the subcatchment parameter statistics, including the minimum and maximum subcatchment areas, the threshold area for the lowest 10%, the median subcatchment area, the number of subcatchments below the threshold, and the total number of subcatchments. If no subcatchments were selected, it prints a message indicating that no subcatchments were selected.

This code performs a similar analysis for both the ICM InfoWorks network and the ICM SWMM network. It selects subcatchments based on their area, either below the threshold area for the lowest 10% or below the median area. The selected subcatchments are then stored, and the relevant statistics are printed.

The code uses the Ruby programming language and interacts with the ICM InfoWorks and SWMM APIs to retrieve subcatchment information and perform the selection and analysis.

> **The Ruby Code**

![](https://media.licdn.com/dms/image/v2/D4E12AQHkClnnfbReCQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1714088843483?e=1795651200&v=beta&t=M2WcC-oRh5ePGewEm8XrnbGlbzqDRGds3Juyk5KRcmk)

Give a mouse a cookie, and it will want to compare ICM InfoWorks to ICM SWMM using Ruby code and the ability to have both current and background networks.

> **An imaginary dialog about the meaning of Ruby code from Star Trek - stardate 41153.7**

Here's a dialog between Jim (Captain Kirk), Spock, and Bones (Dr. McCoy) from Star Trek, explaining the Ruby code:

Jim: Spock, Bones, I need your help understanding this code. It seems to be analyzing subcatchment areas in ICM InfoWorks and ICM SWMM networks.

Spock: Indeed, Captain. The code is performing a comparative analysis of subcatchment areas in both networks. It starts by initializing the current network and background network objects.

Bones: Jim, why are we even looking at this code? Shouldn't we be focusing on more pressing matters, like exploring new worlds?

Jim: Understanding the infrastructure of a civilization is crucial. This code could provide valuable insights.

Spock: Dr. McCoy, the code is quite logical. It iterates over each subcatchment in the networks, retrieves the areas, and stores them in an array.

Jim: What's the purpose of calculating the threshold area and median area, Spock?

Spock: The threshold area represents the lowest 10% of subcatchment areas, calculated by adding 10% of the range to the minimum area. By sorting the areas and selecting the middle value, the median area is the 50th percentile.

Bones: So, it's basically finding the smaller subcatchments?

Spock: Precisely, Doctor. The code then iterates over the subcatchments again and selects those with areas below either the threshold or the median.

Jim: And what does it do with the selected subcatchments?

Spock: The selected subcatchments are marked as selected and stored in a separate array. The code also calculates the total number of subcatchments in each network.

Bones: Why would anyone need to know the number of subcatchments below a certain threshold?

Jim: This information could be useful for urban planning, infrastructure management, or even identifying areas prone to flooding.

Spock: Indeed, Captain. The code provides valuable statistics, such as the minimum and maximum subcatchment areas, the threshold area, the median area, the number of selected subcatchments, and the total number of subcatchments.

Bones: I suppose that could be helpful for those who deal with these networks regularly.

Jim: Absolutely, Bones. This code demonstrates the power of data analysis in understanding complex systems.

Spock: The code is well-structured, using clear variable names and comments to explain its functionality. It also handles cases where no subcatchment are selected, providing appropriate feedback.

Jim: Thank you, Spock, for the explanation. And Bones, while this may not be as exciting as exploring new worlds, it's still an important aspect of understanding the civilizations we encounter.

Bones: I guess you're right, Jim. As long as it doesn't interfere with my medical duties, I can appreciate the value of this analysis.

Jim: Excellent. Let's keep this code in mind as we continue our mission. It may come in handy when we encounter similar infrastructure challenges in the future.

Spock: Agreed, Captain. The code provides a logical approach to analyzing subcatchment areas and can be adapted to various scenarios.

Jim: Thank you, both, for your insights. Now, let's continue our mission to boldly go where no one has gone before!

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
