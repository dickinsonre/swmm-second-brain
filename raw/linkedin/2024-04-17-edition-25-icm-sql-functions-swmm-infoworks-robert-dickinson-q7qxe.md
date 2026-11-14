---
title: "Edition 25 - ICM SQL Functions in ICM SWMM and ICM InfoWorks Networks"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/edition-25-icm-sql-functions-swmm-infoworks-robert-dickinson-q7qxe
created: "2024-03-23 20:51"
published: "2024-04-17 13:19"
words: 931
export_sha256: 49500c1a3977a545abe7522e1999a0f60d9ed2e3ab36e75977e02e3eb2449e05
---
# Edition 25 - ICM SQL Functions in ICM SWMM and ICM InfoWorks Networks

![](https://media.licdn.com/dms/image/v2/D4E12AQHBow7-cAKBmw/series-logo_image-shrink_300_300/series-logo_image-shrink_300_300/0/1707065394509?e=1795651200&v=beta&t=tN-hhC1z9uquar5xA2f4iKHMUJauOcieSynf04B5KXc)

### EPASWMM5 Related Software Five decades with SWMM, still shipping code. SWMM5/6, ICM with Ruby, browser apps that teach the engines — and the art

![ICM SQL Functions in ICM SWMM and ICM InfoWorks Networks](https://media.licdn.com/mediaD4E12AQEvkAEMUchYoQ "ICM SQL Functions in ICM SWMM and ICM InfoWorks Networks")

This newsletter edition covers several SQL-related topics for working with ICM InfoWorks and ICM SWMM networks. The first section provides SQL code to create a usage table for the Sustainable Drainage Systems (SUDS) or Low Impact Development (LID) features on subcatchments. The second sections cover SQL for working with buckets and the RINDEX in ICM InfoWorks network data, as well as using aggregate functions for ICM InfoWorks links. Following are sections on SQL for ICM SWMM options and how to delete all SUDS or LIDs from an ICM network. Finally, the newsletter includes SQL code for retrieving upstream and downstream results for time series reporting (TSR) in ICM InfoWorks networks, as well as a similar SQL query for ICM SWMM network link TSR results.

> **1/ SQL for make a Usage Table for the SUDS or LIDS on the Subcatchments**

\[embedded item\]

> **2/ SQL Buckets and RINDEX for ICM InfoWorks Network Data**

\[embedded item\]

> **3/ SQL Aggregate Functions for ICM InfoWorks Links**

\[embedded item\]

> **4/ SQL for ICM SWMM Options**

\[embedded item\]

> **5/ How to Delete all SUDS or LIDS from your Network**

ICM InfoWorks and ICM SWMM Networks do not have easy-to-use grids for viewing all of the SuDS or LID data.  You need to use Ruby to view or edit the data globally. Here is how you can delete all of the SuDS data.   

This Ruby script is designed to reset Sustainable Drainage Systems (SUDS) controls in a network of subcatchments. Here's a summary of what it does:

1.  It starts by importing the necessary libraries: CSV for handling CSV files and date for handling dates.

2.  It retrieves the current network using the WSApplication.current_network method.

3.  It records the start time of the operation for tracking purposes.

4.  It begins a transaction on the network. Transactions ensure that changes to the network are done atomically, meaning all changes are applied, or none are.

5.  It initializes a counter to keep track of the number of SUDS controls that get reset.

6.  It iterates over each subcatchment in the network. For each subcatchment, it checks if there are any SUDS controls. If there are, it resets them by setting the size of the suds_controls array to 0, writes the changes back to the suds_controls and the subcatchment, and increments the reset counter.

7.  After iterating over all subcatchments, it commits the transaction, making all changes to the network permanent.

8.  Finally, it outputs the number of reset SUDS controls to the console.

&nbsp;

> **6/ SQL for ICM InfoWorks Network Link Upstream and Downstream results**

Here is what the code does for TSR or time series report data - The SQL code is performing a series of aggregate operations on a dataset, grouped by the field. Here's a summary of what it does:

- **Object**: The script operates on a model run that was dragged to the ICM GeoPlan

- **Group By**: The script groups the data by the field.

- **Select**: The script selects the following aggregate operations for each : , , , , and of

![](https://media.licdn.com/dms/image/v2/D4E12AQGPd1ioS2ZcNQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713356704143?e=1795651200&v=beta&t=1o424pQrcx8jYVflP5Iy9cvgkwq3cgF5we3RjD9GRWA)

SQL Table Result - You can copy and paste all of the rows and columns

> **7/ SQL for ICM SWMM Network Link TSR Results**

Almost the same SQL can be used for ICM SWMM networks but since SWMM5 has only ONE flow per link the use of US and DS are not needed and some parameters have a different name.

![](https://media.licdn.com/dms/image/v2/D4E12AQEKhssU3b1fRw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713357882805?e=1795651200&v=beta&t=ZX_QcUeNEkWPLom-hnJRaMCyxQ-oD6iMS0pU9n0_Gyk)

SQL Table Result - You can copy and paste all of the rows and columns

![](https://media.licdn.com/dms/image/v2/D4E12AQEKiL5k9K4Otw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1713359669832?e=1795651200&v=beta&t=NsaYG4U8-84jS_LC1aw342Nc57jUxBL9FB0NxPOC0SY)

**SQL for Green Infrastructur**e

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is the calendar year 2024 and the start of 2025 in Autodesk terms).

Why 1729: The factors of 1729 are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
