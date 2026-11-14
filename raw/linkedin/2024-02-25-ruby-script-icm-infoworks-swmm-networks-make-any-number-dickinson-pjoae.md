---
title: "Ruby Script for ICM InfoWorks and SWMM Networks to make any number of sides Polygons for Subcatchments"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/ruby-script-icm-infoworks-swmm-networks-make-any-number-dickinson-pjoae
created: "2024-02-25 13:36"
published: "2024-02-25 14:18"
words: 754
export_sha256: 4c712b9ceea875d3fb5203269c6279d9648a98312235b04fb9ffc4c4bf7f3b13
---
# Ruby Script for ICM InfoWorks and SWMM Networks to make any number of sides Polygons for Subcatchments

![Ruby Script for ICM InfoWorks and SWMM Networks to make any side Polygon for Subcatchments (sans the actual Subcatchment boundary)](https://media.licdn.com/mediaD4E12AQFWO-egPMts9Q "Ruby Script for ICM InfoWorks and SWMM Networks to make any side Polygon for Subcatchments (sans the actual Subcatchment boundary)")

ICM offers a Subcatchment tool that is designed to generate dummy, circular Subcatchment boundaries tailored to specific regions, as illustrated in Figure 1. This functionality is particularly crucial when importing data from InfoSewer, InfoSWMM, and SWMM5. It ensures that flow elements, including dry weather flow, RDII flow, and base flow are seamlessly transferred from SWMM nodes to ICM Infoworks subcatchments.

To enhance this process and for demonstrative as well as visual purposes, a concise Ruby script has been developed. This script enables users to create custom polygonal Subcatchment boundaries in place of the default circular ones, as shown in Figure 2, providing a more tailored and visually appealing representation of subcatchment areas.

![](https://media.licdn.com/dms/image/v2/D4E12AQGRzjpdnHV9fg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708869565548?e=1795651200&v=beta&t=26S8KRD054BjPs9IHYiQcEz0MPOjKUN75gRQMYzO3xk)

Figure 1. The defaults in ICM for dummy polygon subcatchments is a small circular polygon based on the area of the subcatchment.

![](https://media.licdn.com/dms/image/v2/D4E12AQFKijjmHVlYhw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1708869584072?e=1795651200&v=beta&t=sP0xrljjHruj_XRtYquCSBxn3lDpLoApWswrMgqYMLA)

Figure 2. A simple ruby scripts will take the existing dummy polygons boundaries and make a polygon with a user defined number of sides

> What does the Ruby Script do to make an arbitrary sided polygon?

Filename: UI_Generic_Sides.rb via Visual Studio Code GitHub CoPilot

Summary:

The script modifies the boundaries of selected polygons in a network to have a specified number of sides. The polygons are part of a 'hw_subcatchment' collection in the network.

Details:

1\. The script starts by getting the current network object and beginning a transaction. This allows all changes to be made at once at the end of the script.

2\. A function named 'generate_polygon_boundary' is defined. This function takes a boundary array and a number of sides as arguments. It calculates the minimum and maximum x and y coordinates from the boundary array, and uses these to calculate the width and height of the polygon. It then calculates the points of the new polygon with the specified number of sides, and returns the new boundary array.

3\. The script then iterates over all polygons in the 'hw_subcatchment' collection in the network. For each polygon, it checks if the polygon is selected. If it is, it gets the boundary array of the polygon and sets a new boundary array with a specified number of sides using the 'generate_polygon_boundary' function. The polygon is then written back to the network.

4\. Finally, the script commits the transaction, making all changes permanent.

Note:

The number of sides for the new polygons is currently set to 7. This can be changed by modifying the 'sides' variable in the loop that iterates over the polygons.

> The Ruby Script

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

Why 1729: The number 1729 has **8 factors**, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
