# Doubtful readings (page is the authority; these could not be settled from the scan alone)
| # | Card | Reading used | Alternative | Why doubtful / how to settle |
|---|---|---|---|---|
| 1 | PRIN 49 | IF(IP.EQ.2)WRITE(6,967) | IF(IP.EQ.3) | digit has an arc on top and a flat bar below (2-like); PRIN 81 (same logic for outflows) reads EQ.3. Settle from Vol III sample output: are inlet coliforms printed? |
| 2 | TRAN 44+ KINGTEMP id | KINGTEMP | KINSTEMP | ID field of the inserted Kingman Lake comment cards |
| 3 | FILT 229 | CPI=109.0) (comment) | 109.9 | comment only; code uses 109.9 |
| 4 | DATA 193 (DN1 row for ANORM=.14) | 0.18558,0.0,0.22500,0.16701,0.19280,0.15000,0.12056 | several digits | card is badly faded on the page; cols 1,3,5,6 read by shape, low confidence |
| 5 | DATA 205 | 0.25892 (type 6) | 0.25872 / 0.25832 | one smudged digit; SWMM 4.4H has 0.25892 |
| 6 | DATA 111 | 0.29568 (type 7) | 0.29560 | last digit |
| 7 | MAIN 8 | `2 , 4HAGE , 4HH   /` | no closing slash visible | the slash that ends the DATA list does not show on the page; it must have been there for the card to compile |
- TRTD 77 (p131): scan shows `GO TO (1,2,3,4,5.6,7), L` with a period-like mark between 5 and 6; typed as a comma (7 labels needed).
- TRTD 71: 'CHARACTISTICS' is spelled that way on the page (kept).
- Storage blank COMMON names still to settle from other copies: HPFD/HRFD, ALUMUT/ALJMUT, KNTDF/KNTOF, UPRAMA/OPRAMA, QCMAX/QOMAX (/STBK/).
- TRCH 74 (p141): NOECON(5) last digit smudged; typed 5242 (5243 is already an illegal pair in NOCOMB).
- TRCO209 (p193): comment card 'C??   IF (ICHEM ¬GT¬ ))' prints odd glyphs around GT; typed '.GT.'. TRCO197: EXP(2.3026/(0.2075+...)) has '/' where TRCO199 has '*' (as printed).
- INDA 55 (pdf p201): `DATA ASTERK,BLANK /4H****,4H    /` closing slash not visible on the scan (typed; needed to compile).
- INDA134 (pdf p203): smudged 'WRITE(N6,114) N?CYC' typed NQCYC (format 114 = water quality cycles per day). INDA148C prints as 146C. Three cards after INDA206 carry no ID (A1,A2,A3 read/write/format).
- INQU 14 (pdf p207) faint: typed REAER(6),DECAY(6),XR(6),XRE(6),XNF(6),XMEO(6) -- settle against LOOPQL/QPRINT/SWQUAL copies. INQU 35 TEO(6) vs TEU(6).
- PRTO 74 (pdf p221) faint: typed 'HOUR,11X,101H HEAD(FEET)...' (101 forced by the character count; 11X is the classifier's best reading).
- TIDC134 (pdf p243) very faint: typed 'SUM = SUM -AA(J)*SXX(K,J)' (Gauss-Seidel on the normal equations; classifier cannot tell SXX from SXY, layout fits).
