---
title: "How to import the Scenarios from InfoSewer or InfoSWMM to ICM SWMM or ICM InfoWorks using Ruby"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-import-scenarios-from-infosewer-infoswmm-icm-swmm-dickinson-4m7ke
created: "2024-02-03 17:12"
published: "2024-02-03 17:48"
words: 367
export_sha256: ba1d033917ddd86b78fc1e151d2e30a315b6eada74dec13892cf458fdc1fd864
---
# How to import the Scenarios from InfoSewer or InfoSWMM to ICM SWMM or ICM InfoWorks using Ruby

![InfoSWMM Scenarios Imported to ICM InfoWorks or ICM SWMM](https://media.licdn.com/mediaD4E12AQFpDGjmJgm9Xg "InfoSWMM Scenarios Imported to ICM InfoWorks or ICM SWMM")

> Introduction. Why do we have to do this?

The [direct import of InfoSWMM to ICM SWMM](https://www.linkedin.com/pulse/how-import-swmm5-file-from-pcswmm-andor-model-group-icm-dickinson/?trackingId=V2yEEgsbQNSb%2Fw%2FbW1ARgQ%3D%3D) only imports one scenario at a time. If we want to import all of the scenarios, we end up with a lot of networks and ancillary data for those networks. Duplicates of rainfall, inflow and patterns are examples. The Ruby code (it is the same for both SWMM and InfoWorks networks) is called Step25_User_123_ICM_Scenario_csv.rb and is in the subfolder 0100 - ODIC and SQL, Ruby Scripts for Importing InfoSewer to ICM under 02 SWMM.

> Step 1. Import the Base InfoSWMM or InfoSewer Network

![](https://media.licdn.com/dms/image/v2/D4E12AQFjRsPlH8-nng/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1706981384250?e=1795651200&v=beta&t=y5-lTp21FMZWLsFTWjbQ731pEsYZRk-qFmK-rxMsAUM)

Only the Base Scenario has been imported

> Step 2. Import the file SCENARIO.CSV - it is the same name in InfoSWMM and InfoSewer

You must first convert scenario.dbf to scenario.csv

![](https://media.licdn.com/dms/image/v2/D4E12AQFZzfXsMBWXmQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1706981534189?e=1795651200&v=beta&t=dGa-V0zm5-uMmOFZP7Uas5dtJgtl-g3EGhjMtzXeH08)

Use a folder picker and select either the ISDB or IEDB Folder

> Step 3. A successful import shows you a log file

A successful import shows you a log file that you can copy to the scenario notes.

![](https://media.licdn.com/dms/image/v2/D4E12AQG9069hKf-5Hg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1706982026701?e=1795651200&v=beta&t=wwDyWKzadEdpBShJbEuA3FIBIYhLagHCafPZok5NNUs)

A successful import shows you a log file that you can copy to the scenario notes.

> Section 4. The Ruby Code

> Section 5 The Readme File

**Closing Note**: Thank you so much for journeying with me through this content. This space is reserved for future updates and insights. Your engagement and time are truly appreciated. Until next time! You can also see my past articles on [LinkedIn (91 in 2023)](https://www.linkedin.com/in/robertdickinson/recent-activity/articles/).
