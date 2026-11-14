---
title: "How to make the ICM InfoWorks UX look a bit like InfoSewer (for Manhole loads)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-make-icm-infoworks-ux-look-bit-like-infosewer-loads-dickinson-xfmge
created: "2024-02-25 20:53"
published: "2024-02-26 15:43"
words: 661
export_sha256: 9f202684061882298179d1a890049f7f33a21e3ad7a271cb5687e517afcb29c3
---
# How to make the ICM InfoWorks UX look a bit like InfoSewer (for Manhole loads)

![The user fields of ICM InfoWorks have the names of the Loads and Patterns from InfoSewer](https://media.licdn.com/mediaD4E12AQFN35wyilywnA "The user fields of ICM InfoWorks have the names of the Loads and Patterns from InfoSewer")

Bridging the gap between InfoWorks ICM and InfoSewer, this guide offers a hands-on approach to customizing the ICM InfoWorks UX, making it more familiar to users of InfoSewer, particularly for managing manhole loads. Starting with defining user fields to replicate InfoSewer load and pattern names (Figure 1), the guide walks you through saving ten loads and patterns to ICM's user fields for enhanced usability (Figure 2), detailing manhole loads definition in InfoSewer for Extended Period Simulation (EPS) (Figure 3), and incorporating Arc GIS or Arc Map insights as it matures in 2024 (Figure 4). It also covers using user fields to preserve InfoSewer model units within ICM InfoWorks (Figure 5), and concludes with integrating loads into the InfoSewer DB Table for seamless data and header transfer to InfoWorks ICM (Figure 6).

![](https://media.licdn.com/dms/image/v2/D4E12AQEGQOz8gkAWnA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708902109317?e=1795651200&v=beta&t=Nm4MriUcbVXXKOAM8ANQfu0c4vXuRakCX4FqMSBo8gA)

Figure 1 - Here is where you can define the user fields to mimic the InfoSewer load and pattern names in the user fields.

![](https://media.licdn.com/dms/image/v2/D4E12AQHwnSioj4jJVw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708902126560?e=1795651200&v=beta&t=tNOezoMCwo3Ht3unyt_4s6ne4Z5uiagYJNUq1pq06tQ)

**Figure 2. The ten loads and patterns are saved to the user fields of InfoWork ICM. For ease of use, you can change the field names to LOAD 1 to 1\`0 and Pattern 1 to 10 or the numbers and text, respectively.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFm_V5mCXD9dA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1708902195411?e=1795651200&v=beta&t=wvyr_14zoST-6WmgEPixqkHny23yk6M42x8-YBpYfi0)

**Figure 3. How manhole loads are defined at each node in InfoSewer (ten possible loads plus an extra loading table) for Extended Period Simulation (EPS)**

![](https://media.licdn.com/dms/image/v2/D4E12AQGNIHDNmivBnQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708902257139?e=1795651200&v=beta&t=nhWgdCt1VQ9x3nPgk9RMuxykrU-PjKpfeF_MfV9fQi4)

**Figure 4. Arc GIS or Arc Map, is shifting into mature stage in 2024**

![](https://media.licdn.com/dms/image/v2/D4E12AQFUU7nACPaocg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1708961459731?e=1795651200&v=beta&t=FRLTzys3phyzodlSdAC0vrDHy4mUP13I_y0TcMvJ4Ps)

Figure 5. How we can use the User fields to preserve the user units of the InfoSewer model in ICM InfoWorks.

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/). The next goal is 133 or 17\*19, in FY2025 (which is calendar year 2024 and the start of 2025 in Autodesk terms).

The articles form the backbone of the newsletter. Seven articles make up One Newsletter edition. There will be a summary edition once 19 editions are published, or approximately every 133 articles. The far reaching goal is 1729 articles, 247 editions, and 20 summary editions.

Why 1729: The number 1729 has **8 factors**, which are 1, 7, 13, 19, 91, 133, 247, and 1729 itself. A bit of history about 1729: It's famously known as the **Hardy-Ramanujan number** after a story involving two great mathematicians, G.H. Hardy and Srinivasa Ramanujan. According to the anecdote, Hardy visited Ramanujan in the hospital and mentioned that he arrived in a taxi numbered 1729, which he found to be a rather uninteresting number. Ramanujan immediately responded that 1729 is actually very interesting because it is the smallest number expressible as the sum of two cubes in two different ways: 1729=1^3+12^3=9^3+10^3. This property makes 1729 a significant figure in the world of mathematics, showcasing Ramanujan's extraordinary intuitive grasp of numbers.
