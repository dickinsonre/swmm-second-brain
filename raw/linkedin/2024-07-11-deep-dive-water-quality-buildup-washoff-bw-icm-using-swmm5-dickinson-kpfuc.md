---
title: "Deep Dive into Water Quality Buildup Washoff (BW) in ICM InfoWorks using the SWMM5 BW Options"
kind: linkedin-article
author: Robert Dickinson
url: https://www.linkedin.com/pulse/deep-dive-water-quality-buildup-washoff-bw-icm-using-swmm5-dickinson-kpfuc
created: "2024-07-11 04:01"
published: "2024-07-11 10:35"
words: 1261
export_sha256: ca3a581161cba266132460869378799ed0ca9bc8a269c86c51bbe06420619ca7
---
# Deep Dive into Water Quality Buildup Washoff (BW) in ICM InfoWorks using the SWMM5 BW Options

![Deep Dive into Water Quality Buildup Washoff (BW) in ICM InfoWorks using the SWMM5 BW Options ](https://media.licdn.com/mediaD4E12AQEa3in0HJM1lA "Deep Dive into Water Quality Buildup Washoff (BW) in ICM InfoWorks using the SWMM5 BW Options ")

Using nine separate scenarios, this paper investigates water quality modeling in ICM InfoWorks with all of the SWMM5 buildup washoff choices for runoff, the addition of RDII, and the use of pollutants pl1, pl2, and sf1:

1.  Runoff Only with PL1: Basic scenario without buildup/washoff or rain concentration

2.  RDII Only with PL1: Focusing on Rainfall-Derived Infiltration and Inflow

3.  Runoff Only with PL1 and Rain Concentration: Examining the impact of rainfall on pollutant concentration

4.  Runoff Only with PL1 and Buildup/Washoff: Introducing BW concepts with a single pollutant

5.  Runoff Only with PL1 and PL2: Exploring multiple pollutants with different potency factors

6.  RDII and Runoff with PL1 and PL2: Combining multiple sources and pollutants

7.  Runoff with PL1 and PL2 using Rating Curve BW: Demonstrating the rating curve approach

8.  Runoff with PL1 and PL2 using Exponential Washoff and Buildup: Illustrating more complex BW dynamics

9.  Comprehensive Results Analysis: Examining all output fields for nodes and links

> **1: Runoff Only, PL1, no BW or Rain Concentration no BW or Rain Concentration - no mass flow or PL1 Concentration**

![](https://media.licdn.com/dms/image/v2/D5612AQExmLGSrqLRRg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1720693623038?e=1795651200&v=beta&t=6gggyIelkH3XmghicrDvJ-r7tslM_axJrssXqb3VEhc)

> **2: RDII Only, PL1, no BW or Rain Concentration - mass flow or PL1 Concentration only from RDII and it matches the SWMM5 RDII Concentration**

![](https://media.licdn.com/dms/image/v2/D5612AQGkOk5sAAnD3A/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1720693623418?e=1795651200&v=beta&t=KaV5P8W1I6QRnNQD9xTuvgb-W0KijHCLzvGe4_9MvY8)

> **3: Runoff Only, PL1, no BW just Rain Concentration - mass flow or PL1 Concentration only from Rainfall , it does not equal 1 mg/l**

![](https://media.licdn.com/dms/image/v2/D5612AQGNG0QgbhH80Q/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1720693623468?e=1795651200&v=beta&t=X3qbz8tPnt-Lt_c4soRg779eZ_HnQRId4UuYhP09Jg8)

> **4: Runoff Only, PL1, BW - mass flow or PL1 Concentration only from BW it does equal 10 mg/l , need to use Potency Factors and SF1**

![](https://media.licdn.com/dms/image/v2/D5612AQFWCm9GXJFKFA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720693623013?e=1795651200&v=beta&t=xmZ6IENVVDj4GGxTlrAUnRCm2FqMLo_S7Pw_Q07l8RM)

> **5: Runoff Only, PL1, PL2, BW - mass flow or PL1 and PL2 Concentration only from BW equals 10 mg/l and 5 mg/l need to use Potency Factors and SF1. PL2 has a potency factor of 0.5**

![](https://media.licdn.com/dms/image/v2/D5612AQHh1bh90EDa6Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720693623184?e=1795651200&v=beta&t=d-o-ksivC21YO3OnEmSb01iHI_STCx3fWCF_yqs4ff8)

> **6: RDII + Runoff, PL1, PL2, BW - mass flow or PL1 and PL2 Concentration from RDII + EMC. Concentration is mixed due to Runoff + RDII**

![](https://media.licdn.com/dms/image/v2/D5612AQFgTObTTXNbFA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720693623954?e=1795651200&v=beta&t=qWqetXY1C-1Vd6agBjjdcEU3vsUsx8Qpz0eZE-fXR04)

> **7: Runoff, PL1, PL2, Rating Curve BW - mass flow or PL1 and PL2 Concentration from Rating Curve. Concentration is constant.**

![](https://media.licdn.com/dms/image/v2/D5612AQFXz8lD5-nSIw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720693623356?e=1795651200&v=beta&t=iGlrU-iy691eaMsRBiCfGuKk_-UNCmJWZmv3UIOWLVc)

> **8: Runoff, PL1, PL2, Exponential Washoff with Buildup BW - mass flow for PL1 and PL2 drops off when the buildup limit is reached.**

![](https://media.licdn.com/dms/image/v2/D5612AQHIq2udmJdXvw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720693623731?e=1795651200&v=beta&t=I8BbNqeCKF76T1fBBL09Z8ivkLLOoMCZDjfz_E31uQA)

> **9: All of the results fields for nodes and links in this water quality simulationoff Only, PL1, no BW or Rain Concentration no BW or Rain Concentration - no mass flow or PL1 Concentration**

![](https://media.licdn.com/dms/image/v2/D4E12AQE4KHbwWoE_Bg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720671272954?e=1795651200&v=beta&t=bJ6ojQ18L60orY1x3ZjywSUW9Vk1YAVslaiPIR7hJDU)

Runoff Only, PL1, no BW or Rain Concentration, no BW or Rain Concentration - no mass flow or PL1 Concentration

> **2: RDII Only, PL1, no BW or Rain Concentration - mass flow or PL1 Concentration only from RDII and it matches the SWMM5 RDII Concentration**

![](https://media.licdn.com/dms/image/v2/D4E12AQFq4_p-ThABXg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720674676450?e=1795651200&v=beta&t=lgHqJk1xcLwcRQ9O-QBZss0z4nka9Y3ri9UYvQkh2vQ)

RDII Only, PL1, no BW or Rain Concentration - mass flow or PL1 Concentration only from RDII and it matches the SWMM5 RDII Concentration

> **3: Runoff Only, PL1, no BW just Rain Concentration - mass flow or PL1 Concentration only from Rainfall , it does not equal 1 mg/l**

![](https://media.licdn.com/dms/image/v2/D4E12AQHDCm9EovxeNg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720675309966?e=1795651200&v=beta&t=MoEtgDxvGkqBS2Hm2VrVBOuu_pPsNikOuUimwDx4Olk)

Runoff Only, PL1, no BW just Rain Concentration - mass flow or PL1 Concentration only from Rainfall , it does not equal 1 mg/l

> **4: Runoff Only, PL1, BW - mass flow or PL1 Concentration only from BW it does equal 10 mg/l , need to use Potency Factors and SF1**

![](https://media.licdn.com/dms/image/v2/D5612AQGGuJxuLFO4UQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720681057660?e=1795651200&v=beta&t=h3Impl57HKyxio63DvplQ_HjWSlZVI6ZYnbhSQ1b5uw)

**Runoff Only, PL1, BW - mass flow or PL1 Concentration only from BW it does equal 10 mg/l , need to use Potency Factors and SF1**

> **5: Runoff Only, PL1, PL2, BW - mass flow or PL1 and PL2 Concentration only from BW equals 10 mg/l and 5 mg/l need to use Potency Factors and SF1. PL2 has a potency factor of 0.5**

![](https://media.licdn.com/dms/image/v2/D5612AQEOB7Xqny65Cg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720685559659?e=1795651200&v=beta&t=navX_fQiYmdSlyGI-NmGleanRrA7wCwVP7Sp4SM4jSQ)

**Runoff Only, PL1, PL2, BW - mass flow or PL1 and PL2 Concentration only from BW equals 10 mg/l and 5 mg/l need to use Potency Factors and SF1. PL2 has a potency factor of 0.5**

> **6: RDII + Runoff, PL1, PL2, BW - mass flow or PL1 and PL2 Concentration from RDII + EMC. Concentration is mixed due to Runoff + RDII**

![](https://media.licdn.com/dms/image/v2/D5612AQH8KZPb-rFFGw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720686370316?e=1795651200&v=beta&t=Vq_HmCcvizzVy73dbvk8hEiijjTSVff-2K1aTpbSu_M)

**RDII + Runoff, PL1, PL2, BW - mass flow or PL1 and PL2 Concentration from RDII + EMC. Concentration is mixed due to Runoff + RDII**

> **7: Runoff, PL1, PL2, Rating Curve BW - mass flow or PL1 and PL2 Concentration from Rating Curve. Concentration is constant.**

![](https://media.licdn.com/dms/image/v2/D5612AQFQ2ymkc3oL6w/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720688196333?e=1795651200&v=beta&t=o0Pmy-KQ5iELloeGh2P8a0AlYmxNDobMdpyswl9SRGA)

**Runoff, PL1, PL2, Rating Curve BW - mass flow or PL1 and PL2 Concentration from Rating Curve. Concentration is constant.**

> **8: Runoff, PL1, PL2, Exponential Washoff with Buildup BW - mass flow for PL1 and PL2 drops off when the buildup limit is reached.**

![](https://media.licdn.com/dms/image/v2/D5612AQGAHrs6lKArwA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1720692540792?e=1795651200&v=beta&t=C-jW9DtgZH2xbAoBMhIFpBOpSTFz2PtZ7SCVXPLgjaM)

**Runoff, PL1, PL2, Exponential Washoff with Buildup BW - mass flow for PL1 and PL2 drops off when the buildup limit is reached.**

> **9: All of the results fields for nodes and links in this simulation**

> **Closing Note:**

**Thank you for reading these articles. I appreciate your engagement and support. Thank you again, and I hope you'll join me on this ongoing journey of learning and discovery. Until next time!**

*The articles in this newsletter highlight temporal asymmetries. They discuss topics that, while not universally relevant at all times, become crucial for those in need. These pieces are resources, and they are ready to let you know and help when specific circumstances arise.*
