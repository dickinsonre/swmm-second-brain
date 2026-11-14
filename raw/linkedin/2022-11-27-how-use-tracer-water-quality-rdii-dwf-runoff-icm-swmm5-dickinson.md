---
title: "How to Use Tracer Water Quality for RDII, DWF, and Runoff in an InfoWorks ICM Network - Use SWMM5 Washoff"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-tracer-water-quality-rdii-dwf-runoff-icm-swmm5-dickinson
created: "2022-11-07 04:21"
published: "2022-11-27 20:48"
words: 685
export_sha256: 01a620481e1cfe299ad0ed6735bd3f6e8d2f82e2c61fbfe217d7736df2ff067b
---
# How to Use Tracer Water Quality for RDII, DWF, and Runoff in an InfoWorks ICM Network - Use SWMM5 Washoff

![You are looking at the SWMM5 Buildup Washoff Options in an InfoWorks ICM Network](https://media.licdn.com/mediaD4E12AQHmKHpyrccvyA "You are looking at the SWMM5 Buildup Washoff Options in an InfoWorks ICM Network")

The hydrology of combined sewer systems is extremely complex. Runoff, dry weather flow, or rainfall-dependent infiltration and inflow can all contribute to the flow to a WWTP or an outfall (RDII from leaky sanitary sewers). All inflows are mixed in the 1D ICM pipes, and it is difficult to determine how much RDII flow gets to a WWTP or an outfall.

If you utilize SWMM5 washoff in an ICM InfoWorks network, you can use tracer concentrations for DWF, Runoff, and RDII to calculate the percentage or fractional contribution from any source in the link flow.

### How do you define the tracers?

It is a simple four-step process: (1) Use an InfoWorks Network, (2) Use the Water Quality and Sediment Parameters dialog, (3) Use the SWMM Buildup / Washoff Model, and (4) define rainfall and RDII concentrations. The output of ICM lists the concentration as kg/m3, so we enter the tracer as 100,000, so the link water quality percentage is 0 to 100. BOD will be the RDII tracer, and COD will be the tracer for runoff. The tracer for runoff is actually the rainfall concentration.

![](https://media.licdn.com/dms/image/v2/D4E12AQHu5Vd-qg1AAA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1669576249706?e=1795651200&v=beta&t=TuQBlTxVdk4nN5vokkO3FlElKx36hh6PDNA9FJjBlvw)

How do you define the tracers?

### How do we tell if the RDII Tracer is working?

We will define a subcatchment with only RDII or an RTK UH. We run the model and see that the concentration of BOD or our RDII tracer, is 100 and the COD concentration is zero, as there is no runoff and no rainfall tracer contribution to the runoff water quality.

![](https://media.licdn.com/dms/image/v2/D4E12AQF7h7Jx-QkunA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1669579981681?e=1795651200&v=beta&t=EFPpqGer4E50xITd-xMHKTdfez1eR-695JgPzNxCS8Q)

BOD is 100 as we have no Runoff and only RDII flow from the Subcatchment.

### How do we tell if the Rainfall or Runoff Tracer is working?

We will define a subcatchment without an RDII or an RTK UH. We run the model and see that the concentration of BOD or our RDII tracer, is 0 and the COD concentration is 100, as there is runoff and a rainfall tracer contribution to the runoff water quality.

![](https://media.licdn.com/dms/image/v2/D4E12AQEcetlH9ozdUg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1669580317371?e=1795651200&v=beta&t=muviQh_s_DvIal9Zhklg631-3ufeFFaFvnLnqnhropo)

COD is 100 as we only have Runoff and no RDII flow.

### What do we see if RDII and Runoff sources are mixed in the Link?

When the concentration in a link with upstream sources for runoff and RDII is examined, COD and BOD are not zero. BOD concentration is expressed as a percentage of RDII flow, while COD concentration is expressed as a percentage of runoff. Because the RDII peak is usually later than the runoff peak flow, the BOD concentration is after the COD peak.

![](https://media.licdn.com/dms/image/v2/D4E12AQGHqzFOVNEeSQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1669580485298?e=1795651200&v=beta&t=vQrTZsVsRkjYnSF6muQ8TAZLbR49CPxzgDE1XuHSohk)

If we look at the concentration in a link with upstream sources for Runoff and RDII then both COD and BOD are not zero

### Use SQL to define the RDII UH or RTK UH Quickly.

![](https://media.licdn.com/dms/image/v2/D4E12AQFxq8x-UTK10w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1669581076280?e=1795651200&v=beta&t=hqGRt-fTebcZEOjzhx-rYrhp5l0Ra8Rvvbb9e6GKCQs)

Use SQL to define the RDII UH or RTK UH Quickly.

There are nine used RTK UH parameters in our testing. You can also use the grid output to see the concentrations in a table at a particular time step for both the upstream and downstream ends of the link.

![](https://media.licdn.com/dms/image/v2/D4E12AQEonDTBxM91sw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1669581411937?e=1795651200&v=beta&t=EoI6mos7_F1oyqqYch2a56Axg7Hw8IGbfc5QCaR8sMo)

There are nine used RTK UH parameters in our testing
