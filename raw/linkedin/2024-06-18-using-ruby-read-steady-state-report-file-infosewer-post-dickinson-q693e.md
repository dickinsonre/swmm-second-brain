---
title: "Using Ruby to Read the Steady State Report file of InfoSewer post 2025+"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/using-ruby-read-steady-state-report-file-infosewer-post-dickinson-q693e
created: "2024-06-18 12:14"
published: "2024-06-18 12:45"
words: 841
export_sha256: a749203721f248b2ec0178b47d8c79506c2927dd040366f409b18c42e44596ab
---
# Using Ruby to Read the Steady State Report file of InfoSewer post 2025+

![Using Ruby to Read the Steady State Report file of InfoSewer post 2025+](https://media.licdn.com/mediaD4E12AQGHH23C9p7rxw "Using Ruby to Read the Steady State Report file of InfoSewer post 2025+")

**New note** - see the extra section at the bottom of this note for the links to the improved Ruby code on our GitHub

The year is 2030, and we need to update an old InfoSewer model, but InfoSewer has been retired since 2025, and ArcMap is also a distant memory. We cannot use ArcMap or InfoSewer. We've got tools to import the InfoSewer DBF files into ICM InfoWorks, as the model data is not hidden, but that only gets us the network data. How do we know the HGL and flows that were simulated in InfoSewer?

In this article, we'll show you how to use Ruby's powers to read ancient texts (i.e., text report files of InfoSewer from 2010 to 2030) and compare them to ICM. Please remember that this can only be done if someone in the past had the foresight to save the OUT folder for you! **The components of InfoSewer are the MXD file (ArcMap), the IEDB folder (DBF Files), and the OUT folder (the simulation).** Next up is the Ruby code for EPS InfoSewer and InfoSWMM.

> **What does the Steady State Report file RPT look like?**

![](https://media.licdn.com/dms/image/v2/D4E12AQGGHPi5pZhrGg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718713047031?e=1795651200&v=beta&t=kvnJACfL-2MY57t05iTxouuKTJPrw8QCzvBw3Vfb9Ao)

What does the Steady State Report file RPT look like?

> **Where do you find the InfoSewer RPT File?**

If it exists, it will be in the Scenario folder in the InfoSewer OUT folder.

![](https://media.licdn.com/dms/image/v2/D4E12AQEcQ0rr3bHveA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718713081062?e=1795651200&v=beta&t=MwZacx-pduv936u0HRD3m5ZQZjZkjR6x2k_u4KCjRlw)

Where do you find the InfoSewer RPT file?

> **Ruby Code Subfolder - 0152 - Read InfoSewer Steady State Report File**

[01 InfoWorks ICM/01 Ruby/02 SWMM/0152 - Read InfoSewer Steady State Report File](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/02%20SWMM/0152%20-%20Read%20InfoSewer%20Steady%20State%20Report%20File)

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

> Extra - see also this link to our GitHub site and new Ruby code

**The conversion process has been significantly streamlined thanks to more structured and straightforward Ruby code.** The code can be located and tracked by accessing the links provided in Section 1.

> **1: Location of the Ruby, SQL and ODIC CFG Files**

[01 InfoWorks ICM/01 Ruby/01 InfoWorks/0060 - ODIC and SQL, Ruby Scripts for Importing InfoSewer to ICM](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/01%20Ruby/01%20InfoWorks/0060%20%20-%20ODIC%20and%20SQL%2C%20Ruby%20%20Scripts%20for%20Importing%20InfoSewer%20to%20ICM)

GitHub has excellent readme files, and in addition, the internal Autodesk has more information in the [ICM Online help file](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Knowledge-Importing-InfoSewer-to-InfoWorks-ICM-Overview-of-all-Import-Steps.html)

> **2: Run the Ruby Script and use the converted CSV, Shapefiles and ODIC files Import your InfoSewer Model**

![](https://media.licdn.com/dms/image/v2/D4E12AQEv72y595kHVQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721192385049?e=1795651200&v=beta&t=sgpYZ8FDB3vqfU2bMAzmbfIPOe6YgzmW1_3RlWFA2mw)

> **3: The import process reads all of the needed files and makes an infoWorks Network very fast.**

![](https://media.licdn.com/dms/image/v2/D4E12AQFPyNnHcltHSA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721192385228?e=1795651200&v=beta&t=Xz7sIEoELgKglTnY7llJWHB2LDRhaZqm01FrhoVYUXQ)

> **4: Validate and commit the imported network - no validation errors in the case of this InfoSewer Training model**

![](https://media.licdn.com/dms/image/v2/D4E12AQFLrhN7EtZfaw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721192385586?e=1795651200&v=beta&t=A0BbVfvks7A5PU8oB8hZovcFQVoK77rVthYDulpReoo)

> **5: Run the validated model using a design trade flow pattern.**

With only one unpeakable load (Infosewer term) and a few diurnal patterns, this was a basic Infosewer loading model. In the subcatchment grid, user number one was given the load, and user text one was given the pattern. The trade pattern is created from an InfoSewer CSV file using an Excel macro (see the Innovyze GitHub). The user load-to-trade flow is copied using SQL, and the pattern name is changed to a number for the design trade pattern.

![](https://media.licdn.com/dms/image/v2/D4E12AQGSnMUSIixNPQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721192385868?e=1795651200&v=beta&t=hDZwi57ouJvuM9pcIPR23Hab5PeNWiHJR5Hlc4Lumgc)

> **6: As discussed elsewhere on LinkedIn, you can make observed predicted csv file for depth, flow and velocity to compare InfoSewer to ICM InfoWorks**

![](https://media.licdn.com/dms/image/v2/D4E12AQF-tTFHSQ-xBA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721192386670?e=1795651200&v=beta&t=stsyIMXdH8R1_FqttE2ZaUxCqkaFCpnmkMvtVLV0oqo)

![](https://media.licdn.com/dms/image/v2/D4E12AQFTnsuVoSkRoQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721192386569?e=1795651200&v=beta&t=NdHGFY6DdWve4ZvhXUi0HU90INHIQYkXn629z_fQiVQ)
