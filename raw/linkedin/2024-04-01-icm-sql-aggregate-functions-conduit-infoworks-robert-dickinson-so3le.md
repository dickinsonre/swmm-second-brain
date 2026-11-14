---
title: "How do I find the min, max, and peak timings of hydraulic conduit results using SQL aggregate functions in ICM InfoWorks?"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/icm-sql-aggregate-functions-conduit-infoworks-robert-dickinson-so3le
created: "2024-03-28 02:47"
published: "2024-04-01 13:23"
words: 754
export_sha256: 1c61de87491993f03edd648e195b5a0d84f4af96585555761dcb71280dc70eed
---
# How do I find the min, max, and peak timings of hydraulic conduit results using SQL aggregate functions in ICM InfoWorks?

![ICM SQL to find the min, max, sum , count of various us and ds parameters in ICM InfoWorks](https://media.licdn.com/mediaD4E12AQHfkSt6RllSSA "ICM SQL to find the min, max, sum , count of various us and ds parameters in ICM InfoWorks")

A non-ruby article that employs ICM SQL to determine the minimum, maximum, count, sum, and peak timings of hydraulic conduit results at the upstream and downstream ends of the link. **Simple** to use: simply drag a model run to the Geoplan, indicate the conduits you need information on, and copy and paste the SQL code - it will create SQL tables for all selected links and parameters.

![](https://media.licdn.com/dms/image/v2/D4E12AQGcL4-lpP3pUQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711977604645?e=1795651200&v=beta&t=BDmLZHiYOE2a0vx8Cy3ol3WWnQY284S1BOuf6ixuJw4)

ICM SQL Aggregate Functions for a Conduit in ICM InfoWorks

> **Summary of ICM SQL Aggregate Functions (see online help for ICM as Well):**

1\. ANY: Returns true if the expression is true for any row of the array field.

2\. ALL: Returns true if the expression is true for all rows, related objects, or timesteps.

3\. COUNT: Counts the number of rows, related objects, or timesteps for which the expression is true.

4\. MAX: Returns the maximum value (number, date, or string) for all rows, related objects, or timesteps.

5\. MIN: Returns the minimum value (number, date, or string) for all rows, related objects, or timesteps.

6\. AVG: Returns the mean of all non-null values of the expression (numerical only) for all rows or related objects. For time series results, it returns the time-weighted average.

7\. FIRST: Returns the value of the expression for the first row, related object, or timestep.

8\. LAST: Returns the value of the expression for the last row, related object, or timestep.

9\. SUM: Applicable to time series results. Returns the sum of all values at all time steps.

10\. DURATION: Applicable to time series results. Returns the time in minutes for which the expression is true for the timesteps under consideration. Timesteps need not be contiguous.

11\. EARLIEST: Applicable to time series results. Returns the first non-null value of an expression. It is often used with the IIF function to find the first time a condition is met.

12\. LATEST: Applicable to time series results. Returns the last non-null value of an expression.

13\. INTEGRAL: Applicable to time series results. Returns the sum of the value of the expression at each timestep multiplied by the length of the timestep in minutes.

14\. WHENEARLIEST: Applicable to time series results. Returns the earliest time for which the expression is true.

15\. WHENLATEST: Applicable to time series results. Returns the latest time for which the expression is true.

These aggregate functions allow for powerful calculations and analysis of data across array fields, related objects, and time series results within ICM SQL queries.

> **SQL Code**

> **Summary of SQL Code**

![](https://media.licdn.com/dms/image/v2/D4E12AQHYLHIrm7aUBw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1711977651466?e=1795651200&v=beta&t=pjstiHfHatVvBnG-ljgooMvqgQPOcp4gjSl_1kUbHMc)

ICM SQL Aggregate Functions for a Conduit in ICM InfoWorks

![](https://media.licdn.com/dms/image/v2/D4E12AQFE4ZeC4Ynl0g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1711977730643?e=1795651200&v=beta&t=HxVs42yxBit7DXsBkUzDcc-1w8XVPNom8F218OP68Io)

1729 in other Cultures

**Closing Note:** Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

**Why 1729:** The number 1729 has 8 factors, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the Hardy-Ramanujan number after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
