---
title: "How to use SWMM5 Buildup/Washoff in an ICM InfoWorks Network for Event Mean Concentrations (EMC)"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/how-use-swmm5-buildupwashoff-icm-infoworks-network-event-dickinson-tliqe
created: "2024-06-13 06:57"
published: "2024-06-13 09:06"
words: 602
export_sha256: 4a43d556b3cd1dc0bcaf189605958c3fbd96f01f0c0790cc848191afa31ae1e5
---
# How to use SWMM5 Buildup/Washoff in an ICM InfoWorks Network for Event Mean Concentrations (EMC)

![How to use SWMM5 Buildup/Washoff in an ICM InfoWorks Network for Event Mean Concentrations (EMC)](https://media.licdn.com/mediaD4E12AQGI0w4FLs8g7g "How to use SWMM5 Buildup/Washoff in an ICM InfoWorks Network for Event Mean Concentrations (EMC)")

How to use SWMM5 Buildup/Washoff in an ICM InfoWorks Network for Event Mean Concentrations (EMC). Ten steps to use EMC in an InfoWorks Network in ICM.

> **1: Use SWMM Buildup Washoff in the Water Quality and Sediment Parameters**

![](https://media.licdn.com/dms/image/v2/D4E12AQG0noDaYzARGg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718262109128?e=1795651200&v=beta&t=a-52WrnmAX654ib54PMujdlsGylArUWTKNaW48stXJc)

**Use SWMM Buildup Washoff in the Water Quality and Sediment Parameters**

> **2: Define the Non-Attached Pollutants**

We will use only BOD for the first iteration.

![](https://media.licdn.com/dms/image/v2/D4E12AQGL7xpg14IV_A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718269024651?e=1795651200&v=beta&t=p7l3Ye-xeaMN5iDgOVMgCdcQ_72DDmr159Jl1vES-QA)

**Define the Non-Attached Pollutants**

> **3: Decide whether to use Sediments (The Potency factor)**

We will not use the sediment fraction parameters SF1 or SF2 for this example.

![](https://media.licdn.com/dms/image/v2/D4E12AQErTTlSGZuQRQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1718263575195?e=1795651200&v=beta&t=Ja1l4vI_kfeC3OZC_5zGV2YWX1rfDg-TWqRdaiWcbww)

**Decide whether to use Sediments (The Potency factor)**

> **4: On the Subcatchment Grid use the Tab Buildup / Washoff Land Use for SWMM BW**

![](https://media.licdn.com/dms/image/v2/D4E12AQGGH-hZtM3Zsg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718263971081?e=1795651200&v=beta&t=-DL1ZYErLHuHbr3RwxgsCks2_UQaGPEEEWTRBu2yAwM)

**On the Subcatchment Grid, use the Tab Buildup / Washoff Land Use for SWMM BW.**

> **5: Do not use Buildup for EMC Washoff**

![](https://media.licdn.com/dms/image/v2/D4E12AQHHNIZ3EsZLEQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718264575321?e=1795651200&v=beta&t=R7pqElwWvf6O1_MwdWxZsEUwQ3wObkSbG9Oa-dQgwN4)

**Do not use Buildup for EMC Washoff.**

> **6: Use EMC Washoff in the Washoff Dialog for the Determinant BOD**

The event mean concentration runoff coefficient used in the EMC (Event mean concentration) washoff type. Depending on the pollutant, this is specified in mg/m3 or 1/m3.

![](https://media.licdn.com/dms/image/v2/D4E12AQEDWu_lYamakg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718269093839?e=1795651200&v=beta&t=A7y9bCCv7fgQJiPKRjHQFnyOejXFJAU10lKuexfDrHY)

**Use EMC Washoff in the Washoff Dialog for the Determinant BOD**

> **7: Define the BW Land Use for the Subcatchment**

![](https://media.licdn.com/dms/image/v2/D4E12AQGgX4aeLWQg6Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718265498237?e=1795651200&v=beta&t=4Cinf0eSHwlOJLXbO2GGulPfknaBfYoOS4xgvvGgJU8)

**Define the BW Land Use for the Subcatchment**

> **8: In the Run Dialog, use only BOD as the QM parameter for Water Quality**

![](https://media.licdn.com/dms/image/v2/D4E12AQGfE7FkLMfKOQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718263815963?e=1795651200&v=beta&t=HsjVbiNOHrfRywgU-bLCH8Yr6uW2ZoHcI5Wa_IM4Hi0)

**In the Run Dialog, only use BOD as the Water Quality QM parameter.**

> **9: Validate, run the model, and then graph the results. The concentration of BOD is 100 mg/l**

![](https://media.licdn.com/dms/image/v2/D4E12AQHiK_nVEr6PLw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718268837028?e=1795651200&v=beta&t=fpUQwGH8GO-5UZ0TcLBwaWS0ZLamb4feVpCSo9hV3lI)

Validate, run the model, and then graph the results. The concentration of BOD is 100 mg/l

> **10: In Tools / Options use mg/l as the output units for Concentration**

![](https://media.licdn.com/dms/image/v2/D4E12AQE2Bzcgcl-SpQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1718269362131?e=1795651200&v=beta&t=eLxxfuainTY3a4GYxaRO9nsJz01Wh64wccljgIuDgdY)

**In Tools / Options use mg/l as the output units for Concentration**

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**
