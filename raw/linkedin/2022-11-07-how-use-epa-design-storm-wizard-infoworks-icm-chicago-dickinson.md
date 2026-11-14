---
title: "How to use the EPA Design Storm Wizard with  InfoWorks ICM for Chicago, SCS, NOAA, and IDF Curves."
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-epa-design-storm-wizard-infoworks-icm-chicago-dickinson
created: "2022-11-06 17:05"
published: "2022-11-07 01:05"
words: 1008
export_sha256: de4d96b9338f94c72d8560e14c993482e7db6b3f8665414e8962ebde5d7d0f66
---
# How to use the EPA Design Storm Wizard with  InfoWorks ICM for Chicago, SCS, NOAA, and IDF Curves.

![](https://media.licdn.com/mediaD4E12AQGKw3DJILm_Ow)

  

The Design Storm Wizard install can be found on the openswmm thread at the following link: [https://www.openswmm.org/Topic/32275/dstorm-a-design-storm-wizard](https://www.openswmm.org/Topic/32275/dstorm-a-design-storm-wizard). This is a versatile tool for generating rainfall distributions in SWMM5, based on user-specified IDF or various standard distributions such as Triangular, SCS, NRCS Regional, and Huff. If IDF is not used, the user has the option to save custom distributions to an SWMM5 file. This file can then be imported into an InfoWorks or SWMM ICM network as a Rainfall event. The DSTORM program can be used in conjunction with ICM to create and import rainfall distributions for use in ICM SWMM or ICM InfoWorks Networks. To use DSTORM with SWMM5 and ICM, the user can generate the desired rainfall distribution in DSTORM, copy it, paste it to SWMM5, and then import the resulting Rain Gage into ICM.

Once imported, ALL of the time series are different rainfall columns in the rainfall event. We see Chicago, IDF, Huff, and NOAA. **The rainfall event can be used in ICM SWMM or ICM InfoWorks Networks.** Our goal is to generate the rainfall distribution in DSTORM, copy it, paste it to SWMM5 and then import the rain gages later to ICM. Inside SWMM5, create a new Time Series and paste the generated rainfall distribution from the clipboard. Next, assign the time series to an SWMM5 Rain Gage.

> DSTORM can export SI or USA units to the SWMM5 file.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQFupW3BID9ZEQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667773978502?e=1795651200&v=beta&t=Rb8E0R1RIoOHry5jzk6upEFsoGOnG6ajGHRVbWyrwTs)

DSTORM can export SI or USA units to the SWMM5 file.  
  
  
  

> IDF Curves from NOAS Atlas 14 or User-Defined IDF Table.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHVuF0U7I7wbw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774033557?e=1795651200&v=beta&t=1bbfa3mPqR_nQh4FRgLdZRQdmkehULV4lebvvq8AZos)

IDF Curves from NOAS Atlas 14 or User-Defined IDF Table.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHr4toxWxI3fQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774079833?e=1795651200&v=beta&t=9gK-EtnGT5Y40rgN8dsqgZYdt5oCyY24CVwCOdRbkZU)

If using NOAA Atas 14 for the IDF data then you as a user can pick the USA location.

Our goal is to generate the rainfall distribution in DSTORM, copy it, paste it to SWMM5 and then import the rain gages later to ICM. Inside SWMM5, create a new Time Series and paste the generated rainfall distribution from the clipboard. Next, assign the time series to an SWMM5 Rain Gage.

  

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHGiV36HE4m_w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774121143?e=1795651200&v=beta&t=h4fX_kiWKnkSoK1_J8wMlnHeA5fjzZZ2eq8qHEuy8mQ)

Table for User-Defined IDF Curve

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGH0xQmVDsHUg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774145588?e=1795651200&v=beta&t=JQBvwXJzYKTLuVqXJ3mI2L7dhi-y5fO3ZBrTQdRrbcY)

Chicago IDF Method

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHOoQ74U8i4TQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774175123?e=1795651200&v=beta&t=WgzjIepLV_DYILSchJiD7HIxTllxtBS3eab7-C44hxI)

If using any IDF Curve, you have the option of using Composite, Chicago or Nester Distributions.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQE19q59XjsCTA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774202060?e=1795651200&v=beta&t=og-nzlArrv37-P1b8Ul5BV_tPCrRV0G9ffokivW6iuQ)

Nested IDF Method.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHghH7NytoJng/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774265434?e=1795651200&v=beta&t=1mBjyC37YrX6mNpoolZ2mNAwQAMjYcYmj6g22NhO7UI)

SCS can use one of the four Regional SCS Distributions.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEdHUWlt4kPpA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774300102?e=1795651200&v=beta&t=3M1TlP8QpXwu-ou16q8J8zV5NH3XDp-pYm0wRZ7laTw)

Four types for NRCS

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGupC9D9Tp5Aw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774340081?e=1795651200&v=beta&t=p1ar7QxzQzUHmeEzjvaSoZpCCXBb50_Pfca8qTP_Bas)

Six NRSC Regions with 4 Types per Region

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQElqByVuyKsvw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774367642?e=1795651200&v=beta&t=dV-CQ3QY0Z0_wyZbXS5Hw_eDxBZjUqiEyp2foRFfqZc)

After Calculating the Rainfall Distribution Copy the data tot he Clipboard.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQHW4M0wN0FR3w/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774400597?e=1795651200&v=beta&t=_PDwVGMm0pNGb_mfejAqCByF4oUXtkK3HYKu6M-C3VU)

DSTORM allows typical parameters for defining the generated rainfall distribution

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGVH1gDcLI1HA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774426012?e=1795651200&v=beta&t=LrDGtwAYhzKCBXw6ftMQ9CUOfyahTxc1M5nVvtR2I1k)

Inside of SWMM5, create a new Time Series and paste the generated rainfall distribution from the clipboard. Next, assign the time series to an SWMM5 Rain Gage.

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQEzjossZaoO-A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667774624476?e=1795651200&v=beta&t=Mcm3QDcufbLPbR1_REr1_BlSZUHxjQZxS1LifxjiYGE)

Import of the saved SWMM5 file can be specific and not general. We will import to a Rainfall event, which will read in all of the rain gages and associated time series.

> Once imported, ALL of the time series are different rainfall columns in the rainfall event. We see Chicago, IDF, Huff, and NOAA. **The rainfall event can be used in ICM SWMM or ICM InfoWorks Networks.**

![No alt text provided for this image](https://media.licdn.com/dms/image/v2/D4E12AQGp5f8Qd6ZZ_Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1667778734781?e=1795651200&v=beta&t=lJYkO0fflx0Qy6HO3bX5GBrWwf8C4rus9hzwLFJkJXI)

Once imported, ALL of the time series are different rainfall columns in the rainfall event. We see Chicago, IDF, Huff, and NOAA. The rainfall event can be used in ICM SWMM or ICM InfoWorks Networks..
