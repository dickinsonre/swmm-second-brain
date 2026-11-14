---
title: "QA/QC Process for the Import of an XP-SWMM model to InfoWorks ICM  6 - ICM 7.5"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/qaqc-process-import-xp-swmm-model-infoworks-icm-6-robert-dickinson
created: "2015-07-15 00:25"
published: "2015-07-15 00:25"
words: 1355
export_sha256: 65bd2dbfc011c5326f8febd25d17c66c6de090e11f610abc5a1c52ae8bacfd0c
---
# QA/QC Process for the Import of an XP-SWMM model to InfoWorks ICM  6 - ICM 7.5

## QA/QC Process for the Import of an XP-SWMM model to InfoWorks ICM 5.5 or ICM 6, ICM 7, ICM 8+

> The following section shows how the XP-SWMM file (MyXP.XP) was converted to an ICM 6 model using the ICM SWMM 6 import tools.

The XP-SWMM model was converted to ICM 6 using a combination of the import process in ICM of a SWMM5 input file (MySWMM5File.INP ) and an Extensive QA/QC process using the .XP file of XP-SWMM (MyXP.XP). Figure 1 shows how the file MySWMM5File.INP looks inside of SWMM 5.1. Figure 2 shows the model summary of the file MySWMM5File.INP which was exported in SWMM 5 format from XP-SWMM. Figure 3 shows the Import process in ICM for any SWMM5 file. Figure 4 show how the file MySWMM5File.INP looks like ICM after the Import. Figure 5 shows the element summary in ICM of the imported file MyXP.XP. The number of links, nodes, Subcatchments and diversions match the input file and the summary shown in Figure 2. There are approximately 7000 nodes, links, diversions and Subcatchments in the model.

After import into ICM the imported data was checked using the Network Validation tool (Figure 6). If there were any import errors a log file would have been created. However, all data imported without errors and the log file was blank for ICM 6 import. ICM has many more node and link parameters than in XP-SWMM so there are some validation errors. The validation errors are shown in Figure 7 and are related to the node of ICM needing chamber, ground and flood levels. You can click on the warning message as shown in Figure 8 to bring up the node grid so that the few validation errors can be fixed. As a further check the .XP file was used to check any ICM Validation Messages as shown in Figure 9.

The import tool in ICM does not import the Rainfall or DWF patterns from the SWMM5 file. The hyetographs and DWF patterns have to be separately copied and pasted from the SWMM5 file to the Rainfall Event CSV file and Waste Water Patter CSV file in ICM. Figure 10 shows the DWF Patterns used in the file MySWMM5File.INP . Figure 11 shows the cumulative Rainfall Hyetographs used in the file MySWMM5File.INP . The Rainfall hyetograph have to be converted to rainfall intensity and multiplied by the storm event total as defined in the file MyXP.XP The rainfall totals for the 2, 5, 10, 25, 50 and 100 year storm events are shown in Figure 12. Figure’s 13 and 14 show the DWF Pattern and ICM Rainfall Event corresponding to the values shown in Figures 10 and 11, respectively. The connection between the Pattern and Rainfall CSV files and the imported network in ICM is illustrated in Figure 15.

The XP-SWMM model in SWMM 5 format has many irregular natural channels modeled as prismatic HEC-RAS transects. Figure 16 shows an example transect view. The imported network in ICM has these transects as channels with a shape named after the transect (Figure 17). The channels can be either used as channel in ICM or converted to a River Reach with 2D connection using the ICM Channel/River Reach conversion tool (Figure 18).

![](https://media.licdn.com/dms/image/v2/C5112AQEweekAETTXWg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520172011054?e=1795651200&v=beta&t=3aYRcWH2Skkcmx34RGzyK9BMBdSyuvLu8Rdb1zCh2mM)

Figure 1. How the MySWMM5File.INP looks inside of SWMM5

The three types of runoff surfaces in the XP-SWMM model are imported with the physical data on the Subcatchment Tab. Examples of the physical data are the slope, width, Subcatchment area and percent imperviousness for each Subcatchment (Figure 19). The Impervious surface with depression storage is imported as a Fixed Runoff Volume Type with a non-zero initial loss and the SWMM Routing Model. The Impervious surface without depression storage is imported as a Fixed Runoff Volume Type with a zero initial loss and the SWMM Routing Model. The pervious surface with depression storage is imported as a Green-Ampt Runoff Volume Type with a non-zero initial loss and the SWMM Routing Model. The three types of runoff surface can be seen on the Runoff Tab of the Subcatchment Grid.

![](https://media.licdn.com/dms/image/v2/C5112AQGXFGJ0ZUXIBw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520193784643?e=1795651200&v=beta&t=CZPMeX1rmEpb99KtMKyMOokIELH0jARlU0NRBAuIQQY)

Figure 2. MySWMM5File.INP File Summary

![](https://media.licdn.com/dms/image/v2/C5112AQG98j1WKKggkA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520142068347?e=1795651200&v=beta&t=psNpEbbwvIY87LflgyWKndG9Do3ZBpXUFjVbDSNP1Ew)

Figure 3. The tools use to import the file MySWMM5File.INP to ICM.

![](https://media.licdn.com/dms/image/v2/C5112AQEXYpNUoQ3rQg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520251389147?e=1795651200&v=beta&t=dD8xDSRN7Wq3iWeVek8bSWpju6LaDx5tQ4yh9HCZ2JM)

Figure 4. How the file MySWMM5File.INP looks like ICM after Import.

![](https://media.licdn.com/dms/image/v2/C4E12AQEnqxo9eViS5A/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520505913431?e=1795651200&v=beta&t=7RmELzT6DPQrx4nc8Gph-BXcXwV60vTx-jpnBufRAqY)

Figure 5. Summary of the file MySWMM5File.INP after import into ICM.

![](https://media.licdn.com/dms/image/v2/C5112AQHoEKNV8b3xow/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520250603108?e=1795651200&v=beta&t=QyUTIULsB74WOHBM2iecfMRpV0g-St2XtzzTf0s5Rxs)

Figure 6. The Network Validation Tool checks the imported file for data errors.

![](https://media.licdn.com/dms/image/v2/C4E12AQHgUDHcUMmhng/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520505913449?e=1795651200&v=beta&t=is8RWhc7ccZX2bkVRXJfhPr3h6cTTEHnMUkqp1Pg0z4)

Figure 7. Import Data Errors are shown in Output.

![](https://media.licdn.com/dms/image/v2/C5112AQGzClXu_SPOUw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520251222859?e=1795651200&v=beta&t=XGqUCpgiOdEBKPHnFdzgpcZOxb0hJjuYi8dGzh3jAig)

Figure 8. Click on Warning Message and the location is shown on the screen.

![](https://media.licdn.com/dms/image/v2/C5112AQF3zX9tkxgAzg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520174043308?e=1795651200&v=beta&t=YKV_udwXCTSxR5Zz05bUFQaw2DZwEB575pwH7nbOrhg)

Figure 9. The XP file was used to check any ICM Validation Messages.

![](https://media.licdn.com/dms/image/v2/C5112AQGkHJ1_Za3dfA/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520142975974?e=1795651200&v=beta&t=8OXhgss6UviClAua2SQdqbRX7bH8nErPbUrIIRGdpII)

Figure 10. The DWF Patterns from XP-SWMM as they look in SWMM5

![](https://media.licdn.com/dms/image/v2/C5112AQHc-1orDoN_1Q/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520042129329?e=1795651200&v=beta&t=WQh-sEsb7LsV7z15Ecci_tJEFEm8OkXz5C_WOv6pY9Y)

Figure 11. The Rainfall Hyetograph in XP-SWMM.

![](https://media.licdn.com/dms/image/v2/C5112AQHVd-y57TegVQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520241317097?e=1795651200&v=beta&t=oYlK_G-abpgQoUB53hpB8T906L1McqsbmDpwzoZSnIk)

Figure 12. The 2, 5, 10, 25, 50 and 100 year Storm Totals used In XP-SWMM.

![](https://media.licdn.com/dms/image/v2/C4E12AQF8eGxD8I779g/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520505913619?e=1795651200&v=beta&t=FvlkQ0V68KME3sXIbwxNnAE8dKXGa_-ILSVvmovFows)

Figure 13. The Copied DWF Patterns from XP-SWMM in ICM.

![](https://media.licdn.com/dms/image/v2/C5112AQHkJM6kDzgC8g/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520211792068?e=1795651200&v=beta&t=CR7doJ2eLkNAY50xqSBMvkWDI0Hg5LhqI9kkaMkx9ig)

Figure 14. The Converted Hyetograph as it looks in the ICM Rainfall Event.

![](https://media.licdn.com/dms/image/v2/C5112AQHi3xA_4fL2Wg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520250823713?e=1795651200&v=beta&t=DlMXrtIMCW0t88oUQmPht6eNejCNN9kEKlbeE6o_86o)

Figure 15. Imported XP-SWMM Network, Rainfall and DWF Patterns in ICM.

![](https://media.licdn.com/dms/image/v2/C4E12AQErD9mAiqpFWg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520505913383?e=1795651200&v=beta&t=i4YoigYxdKackb4yzOyTV0izigCUWEBiZowtrsW5VMg)

Figure 16. Prismatic Channel Transects in XP-SWMM.

![](https://media.licdn.com/dms/image/v2/C5112AQHfqdDDyC5tjQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520207451851?e=1795651200&v=beta&t=pZK57d3Xus3cEFIpbg5Sk_c5_p8xoNv5u5p_pc_1isY)

Figure 17. Imported Transects from XP-SWMM are Channel Shapes in ICM.

![](https://media.licdn.com/dms/image/v2/C5112AQHXGPxMDgp6Zw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1520239873115?e=1795651200&v=beta&t=pLk8RXwHIg5ssXPmNVSisASVUTt9mpsOpxAE02L-dUc)

Figure 18. You can convert the Channels to River Reaches with Banks and 2D connections using the Channel to River Reach Tool.

![](https://media.licdn.com/dms/image/v2/C5112AQFyqG9F8yHgPQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1520238790727?e=1795651200&v=beta&t=t78ip7pOgKwSuIoUWN8p2GhfjQQTTfxStZv19_DuJko)

Figure 19. The XP-SWMM Hydrology is imported as Fixed or Green-Ampt for Impervious and Pervious Areas.
