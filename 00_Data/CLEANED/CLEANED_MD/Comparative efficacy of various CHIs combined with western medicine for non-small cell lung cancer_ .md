## Check for updates

## OPEN ACCESS

EDITED BY
Eswar Shankar,
The Ohio State University, United States
REVIEWED BY
Prem P. Kushwaha,
Case Western Reserve University,
United States
Deena Snoke,
University of Vermont, United States
Kate Ormiston,
The Ohio State University, United States
*CORRESPONDENCE
Liubao Peng,
pengliubao@csu.edu.cn
SPECIALTY SECTION
This article was submitted to
Pharmacology of Anti-Cancer Drugs,
a section of the journal
Frontiers in Pharmacology
RECEIVED 06 September 2022
ACCEPTED 20 October 2022
PUBLISHED 10 November 2022

## CITATION

Peng C, Chen J, Cui W, Li S, Li J and Peng L (2022), Comparative efficacy of various CHIs combined with western medicine for non-small cell lung cancer: A bayesian network metaanalysis of randomized controlled trials. Front. Pharmacol. 13:1037620. doi: 10.3389/fphar.2022.1037620

COPYRIGHT
(c) 2022 Peng, Chen, Cui, Li, Li and Peng. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## Comparative efficacy of various CHIs combined with western medicine for non-small cell lung cancer: A bayesian network meta-analysis of randomized controlled trials

Ciyan Peng ${ }^{1}$, Jing Chen ${ }^{2}$, Wei Cui ${ }^{1}$, Sini Li ${ }^{1}$, Jianhe Li ${ }^{1}$ and Liubao Peng ${ }^{1 *}$<br>${ }^{1}$ Department of Pharmacy, The Second Xiangya Hospital of Central South University, Changsha, China, ${ }^{2}$ Department of Pharmacy, The First Affiliated Hospital of Hunan University of Chinese Medicine, Changsha, China

Background: Given the limitations of Western medicine (WM) for the treatment of non-small cell lung cancer (NSCLC) and the wide exploration of Chinese herbal injections (CHIs), systematically evaluate the efficacy of Various CHIs Combined with WM for Non-small Cell Lung Cancer. In this study, we performed a network meta-analysis to evaluate the comparative efficacy of 16 CHIs combined with WM regimens for the treatment of NSCLC.

Methods: Literature databases were searched from their inception to November 2021, and all randomized control trials (RCTs) involving NSCLC patients treated with a combination of Chinese and WM were retrieved. Outcomes, including disease control rate, survival quality score, incidence of gastrointestinal adverse reactions, incidence of leukopenia, and incidence of thrombocytopenia, were analyzed using RevMan (5.3), Stata17, and R software. Surface under the cumulative ranking curve (SUCRA) probability values were calculated to rank the treatments examined, and clustering analysis was used to compare the effects of CHIs on different outcomes.

Results: A total of 389 studies involving 31,263 patients and 16 CHIs were included. The 16 CHIs were: Aidi injection (ADI), Huachansu injection (HCSI), oil

[^0]
[^0]:    Abbreviations: 95\% CI, 95\% confidence interval; ADI, Aidi injection; CHIs, Chinese herbal injections; CM, Chinese medicine; CSI, Chansu injection; DCI, disodium cantharidinate and vitamin B6 injection; DCR, disease control rate; DLSI, Delisheng injection; FFKSI, Fufang Kushen injection; GI, gastrointestinal; HCSI, Huachansu injection; HQI, Huangqi injection; INPLASY, International platform of registered systematic review and meta-analysis protocols; KAI, Kangai injection; KLTI, Kanglaite injection; KPS, Karnofsky performance scale; NSCLC, non-small cell lung cancer; NMA, network meta-analysis; OOMI, oil of Ophiopogon injection; OR, odds ratio; RCT, randomized controlled trial; SFI, Shenfu injection; SI, Shengmai injection; SMI, Shenmai injection; SGFZI, Shenqi Fuzheng injection; SUCRA, surface under the cumulative ranking curve area; WM, western medicine; XAPI, Xiaoaping injection; XGDTI, Xianggu Duotang injection.

of Ophiopogon injection (OOMI), disodium cantharidinate and vitamin B6 injection (DCI), Shenfu injection (SFI), Shenmai injection (SMI), Shenqi Fuzheng injection (SQFZI), Chansu injection (CSI), Delisheng injection (DLSI), Fufang Kushen injection (FFKSI), Huangqi injection (HQI), Kangai injection (KAI), Kanglaite injection (KLTI), Shengmai injection (SI), Xiangguduotang injection (XGDTI), and Xiaoaiping injection (XAPI). The results of the network metaanalysis showed that, with WM treatment as a co-intervention, CSI was most likely to improve the disease control rate (SUCRA $=80.90 \%$ ), HQI had the highest probability of being the best option for improving the survival quality score (SUCRA $=82.60 \%$ ), DCI had the highest probability of reducing the incidence of gastrointestinal adverse reactions (SUCRA $=85.50 \%$ ), HCSI + WM had the highest probability of reducing the incidence of thrombocytopenia (SUCRA $=91.30 \%$ ), while SMI had the highest probability of reducing the incidence of leukopenia (SUCRA $=79.10 \%$ ).

Conclusion: CHIs combined with WM is proved to be more effective than WM alone, which may be beneficial to NSCLC patients. SMI + WM and DCI + WM are most likely the optimal CHI to improve disease control rates, survival quality score, and reduce adverse effects. This study has limitations; therefore, higher quality RCTs and real-world evidence are required to support our conclusions.

## KEYWORDS

network meta-analysis, bayesian model, Chinese herbal injections, non-small cell lung cancer, combined therapy, Chinese medicine

## 1 Introduction

Lung cancer is the malignancy with the highest mortality and incidence rates, both worldwide and in China (Bray et al., 2018; Sung et al., 2021; Siegel et al., 2021; Alexander et al., 2020). Lung cancer brings a tremendous economic and social burden on both developing and developed countries (Minguet et al., 2016; Sung et al., 2021; Bray et al., 2018; Molina et al., 2008). Based on histology, Lung cancer can be classified as non-small cell lung cancer (NSCLC) and small cell lung cancer. Non-small cell lung cancer (NSCLC) accounts for approximately $80 \%-85 \%$ of all lung cancers (Miller et al., 2020; Miller et al., 2016; Miller et al., 2022).

Currently, platinum based chemotherapy is still the firstline treatment for lung cancer (Ettinger et al., 2017; Ettinger et al., 2022). However, some patients are unable to complete the recommended cycles of chemotherapy due to serious adverse events, greatly limiting its clinical application (Quoix et al., 2011; Shojaee and Nana-sinkam, 2017; Ettinger et al., 2022). With the development of modern treatment methods and biotechnology, lung cancer has entered the era of precision therapy (Soo et al., 2017; Hirsch et al., 2017; Yoneda et al., 2018). Molecular targeted drugs and immunotherapy have substantially improved the clinical efficacy of mid-to late-stage lung cancer treatment (Lemjabbar-Alaoui et al., 2015; Cho, 2017; Zhang et al., 2018; Jiang et al., 2019; Li et al., 2021). Although Immunotherapy
increasing the 5-year survival rate of patients with advanced NSCLC from 5\% to approximately 23\% (Reck et al., 2022; Ren et al., 2021; Yoneda et al., 2018; Garon et al., 2019; Breimer et al., 2020), it is often accompanied by low antigenicity, side effects, and drug resistance for lung cancer has limitations in clinical practice (Khunger et al., 2018; Zhang et al., 2018; Xia et al., 2019; Wang et al., 2021; Stock-Martineau et al., 2021; Zhou and Zhou., 2021). Therefore, how to actively identify effective drug treatment options to reduce postoperative recurrence and metastasis, prolong the survival time of patients with advanced disease, reduce adverse effects, and improve patient quality of life remains a key challenge in the treatment of advanced lung cancer.

Chinese medicine injections (CHIs) are widely used by clinicians in China as an important component of complementary and alternative medicine for the adjuvant treatment of NSCLC (Jiao et al., 2017; Jiang et al., 2019; Xu et al., 2021; Han et al., 2016; Wu et al., 2016; He et al., 2016; Cao et al., 2017; Cao et al., 2021; Wang B et al., 2018). Many studies have documented the efficacy of Various CHIsCombined with Western Medicine for Non-small Cell Lung Cancer (Li et al., 2021; Zhang et al., 2018; Yao et al., 2020; Jiang et al., 2016; Jiang et al., 2019; Tan and Wang., 2016; Liu et al., 2017; Ma and Xu., 2017; Zheng et al., 2017; Wang G et al., 2018; Li et al., 2020; Liu et al., 2021; Xie et al., 2021). However, there are various types of CHIs, and the optimal strategy for combining CHIs with WM for treating

NSCLC remains inconclusive, which may cause difficulty for clinicians in clinical treatment. Bayesian network metaanalysis (NMA) has the advantage of combining direct and indirect evidence to compare multiple interventions (Schwingshackl et al. 2019; Watt et al. 2019; Ahn and Kang. 2021; González-Xuriguera et al. 2021; Watt and Del Giovne, 2022). Therefore, in this study, we used Bayesian network meta-analysis (NMA) method to systematically evaluate the efficacy of Various CHIs Combined with WM for Non-small Cell Lung Cancer. The objective of this NMA was to supplement the optimal strategy of NSCLC treatment and to strengthen additional insights for clinical practice in the future.

## Methods

This study is reported in strict accordance with the standard format specifications detailed in the Preferred Reporting Items for Systematic Reviews and Meta-Analysis: PRISMA Extension Statement (Cornell, 2015; Hutton et al. 2015; Rethlefsen et al. 2021). A completed PRISMA checklist is included as an additional file (Supplementary File). The study protocol was registered and approved on the International Platform of Registered Systematic Review and Meta-Analysis Protocols (INPLASY) on 17 November 2021 (registration number: INPLASY2021110068), and the study was conducted strictly in accordance with the registered study protocol. This NMA did not require ethical approval, because the study only collected clinical data from each randomized controlled trial (RCT) and did not disclose patient information.

### Search strategy

In this NMA, a comprehensive data search of the following electronic databases for RCTs of CHIs combined with WM for NSCLC was conducted from their inception to November 2021: Chinese Biological Medicine Literature, China National Knowledge Infrastructure, Wanfang, PubMed, Cochrane Library, and Embase. In addition, pharmaceutical companies that manufacture proprietary CMI were contacted to provide unpublished information regarding premarket and postmarket studies. Further, study authors were contacted to supplement incomplete reports of original papers or to provide data from unpublished studies. The search strategy was divided into three parts: CHIs, NSCLC, and RCTs. A search strategy was developed, as illustrated in Table 1 using PubMed as an example. A total of 16 CHIs that met the national standards of the Chinese Food and Drug Administration were included (https://db.yaozh.com and https://www.nmpa.gov.cn/). Detailed drug information is provided in (Table 1 and Supplementary Table S1).

### Inclusion criteria

### Study types

RCTs that reported the efficacy of the 16 CHIs combined with WM for treating NSCLC were eligible. There were no language restrictions. When outcome information was available for multiple time points, the data for the longest follow-up time point were selected.

### Participants

All patients were pathologically and histologically diagnosed with NSCLC. There were no limitations on sex, age, race, region or nationality.

### Interventions

Patients in control groups received only WM regimens, including DP, TP, GP, NP, and GE, where D indicates docetaxel, P cisplatin, T paclitaxel, G gemcitabine, N vinorelbine, and E gefitinib. Patients in the treatment group received CHIs together with WM therapy. To facilitate our analyses, we collapsed all agents regardless of dose. If patients had complications during the treatment, then some appropriate mitigation measures could be taken.

### Outcome measures

The primary outcome indicator was DCR, where DCR was defined as complete remission + partial remission + stable. Survival quality was assessed using the Karnofsky performance scale (KPS), with improvement defined as an increase of ≥10 points in the KPS score after treatment, stability as an increase or decrease of <10 points, and a decline as a decrease of ≥10 points in the KPS score. Secondary outcome indicators were the incidence of adverse reactions, including gastrointestinal (GI) adverse reactions, leukopenia, and thrombocytopenia. Data were extracted according to the predefined definitions described in the protocol, with priority given to the earliest published report when data appeared in more than one report. RCTs were eligible if they reported one of the aforementioned outcomes.

### Exclusion criteria

The exclusion criteria were as follows: 1) Other western medical treatment options (Radiotherapy, Surgical and Local interventional therapy); 2) Other traditional Chinese Medicine treatment options (Decoction for oral and external use, emotional therapy, static breathing control, acupuncture); 3) repeat publications; and 4) Studies with incomplete or incorrect data.

TABLE 1 Specific terms used to search PubMed.

```
#1 Non-small cell lung
cancer (MeSH terms),
#2 carcinoma, Non-small cell
lung (title/Abstract), #3 carcinomas,
Non-small-cell lung (title/Abstract),
#4 lung carcinoma, Non-small-cell
(title/Abstract), #5 lung carcinomas,
Non-small-cell (title/Abstract), #6 Non-small-cell
lung carcinoma (title/Abstract),
#7 Non-small-cell lung carcinomas
(title/Abstract)
```

```
#8, #1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7
#9 Aidi Injection (Title/Abstract), #10 Huachansu Injection (Title/Abstract),
#11 Oil of Ophiopogon Injection (Title/Abstract), #12 Disodium Cambaridinate
and Vitamin B6 Injection (Title/Abstract), #13 Shenfu Injection (Title/Abstract),
#14 Shenmai Injection (Title/Abstract)
#15 Shenqifuzheng Injection (Title/Abstract), #16 Chansu Injection (Title/
Abstract), #17 Dehsheng Injection (Title/Abstract), #18 Fufangkushen Injection
(Title/Abstract), #19 Huangqi Injection (Title/Abstract)
#20 Kangai Injection (Title/Abstract), #21 Kanglete Injection (Title/Abstract),
#22 Shengmai (Title/Abstract), #23 Xiangguduotang Injection (Title/Abstract),
#24 Xiaoxiping Injection (Title/Abstract)
#25 #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR
#19 OR #20 OR #21 OR #22 OR #23, OR #24
#26 randomized controlled trial (Publication type)
#27 controlled clinical trial (Publication type)
#28 #26 OR # 27
#28 #8 AND #25 AND #28
```


### 2.5 Data extraction and quality assessment

All retrieved studies were managed using EndNote software. After excluding duplicate studies, two researchers (Jing Chen and Sini Li) independently screened the retrieved studies according to the inclusion and exclusion criteria, and after excluding unrelated literature, such as reviews, evaluations, animal studies, and uncontrolled studies, the full text of each report was read to finalize the texts for inclusion in the study and to extract the data. Subsequently, a review team consisting of two researchers (Jianhe Li and Wei Cui) checked the accuracy of the data and assessed the quality of the included studies. Information extracted from included studies comprised: study name, study date, number of patients, sex ratio, treatment strategy, treatment procedure, and outcomes.

Two researchers (Jianhe Li and Wei Cui) independently assessed the risk of bias in included RCTs according to the risk of bias tool provided in the Cochrane Handbook for Systematic Reviews of Interventions. The following were assessed: 1) selection bias associated with random sequence generation; 2) selection bias associated with allocation concealment; 3) performance bias: blinding of participants and personnel; 4) detection bias: blinding of outcome assessments; 5) attrition bias: completeness of
outcome data; 6) reporting bias: selective reporting; and 7) other sources of bias. Each factor was categorized as "low risk", "high risk", or "unclear". All discrepancies that emerged from this study were discussed by a review panel.

### 2.6 Data analysis

All meta-analyses were performed within a Bayesian framework using R4.11 software for statistical analysis of data and research, and a Markov chain Monte Carlo method for Bayesian inference. The parameters set in R4.11 software were as follows: number of chains, 4 ; tuning iterations, 50,000 ; simulation iterations, 100,000 ; thinning interval, 1 ; settings of tuning iterations and simulation iterations were adjusted according to the actual situation. Potential scale reduction factors were used to evaluate the convergence of Markov chains. Models were compared using the deviance information criterion, which is equal to the sum of the posterior mean of the residual deviations and the number of valid parameters. Results for comparisons of dichotomous variables were calculated as odds ratios (OR). Differences between groups were considered statistically significant when the $95 \%$ confidence interval (CI) of OR values did not contain 1. Network diagrams showing indirect comparative relationships among different interventions were generated, where the nodal areas for each intervention represent the number of patients, and the thickness of lines between different interventions represented the number of RCTs. R4.11 and Stata17 software were used to plot cumulative probability ranking, and to generate mesh and funnel plots for each intervention. A surface under the cumulative ranking area (SUCRA) curve is used to estimate the probability of ranking each intervention; the larger the area under the curve, the higher the ranking and the higher the probability that the CHIs are the best interventions (Salanti et al., 2011). Clustering analysis was used to synthesize and compare interventions with two different outcome indicators, to obtain the best choice of injection for both outcome indicators: the farther away from the origin in the clustering plot, the better the outcome indicator. Acomparisonadjusted funnel plot was used to assess potential publication bias. If points on both sides of the midline in the funnel diagram were symmetric, which meant the correction guideline was at right angles to the midline, it was considered indicative of no significant publication bias.

## 3 Results

### 3.1 Search results

A total of 2004 studies were retrieved, and 389 RCTs (Supplementary Table S2) were finally included for NMA

Table 2 Detailed information on Chinese herbal injections.

Note: ADI, Aidi injection; CSI, Chansu injection; DCI, disodium cantharidinate and vitamin B6 injection; DLSI, Delisheng injection; FFKSI, Fufang Kushen injection; HCSI, Huachansu injection; HQI, Huangqi injection; KAI, Kangai injection; KLTI, Kanglaite injection; OOMI, oil of Ophiopogon injection; SFI, Shenfu injection; SI, Shengmai injection; SMI, Shenmai injection; SQFZI, Shenqi Fuzheng injection; XAPI, Xiaoxiping injection; XGDTI, Xianggu Duotang injection.

![img-0.jpeg](img-0.jpeg)

FIGURE 1 PRISMA flow diagram.

According to the pre-defined inclusion and exclusion criteria, further details of the literature screening process are shown in Figure 1. The 389 RCTs reported 16 herbal injections used as interventions in combination with conventional WM, as follows: Aidi injection (ADI, 66 RCTs), Huachansu injection (HCSI, 10 RCTs), oil of *Ophiopogon* injection (OOMI, 23 RCTs), disodium cantharidinate and vitamin B6 injection (DCI, 14 RCTs), Shenfu injection (SFI, 14 RCTs), Shenmai injection (SMI, 21 RCTs), Shenqi Fuzheng injection (SQFZI, 39 RCTs), Chansu injection (CSI, 4 RCTs), Delisheng injection (DLSI, 8 RCTs), Fufang Kushen injection (FFKSI, 55 RCTs), Huangqi injection (HQI, 8 RCTs), Kangai injection (KAI, 37 RCTs), Kanglaite injection (KLTI, 39 RCTs), Shengmai injection (SI, 11 RCTs), Xiangguduotang injection (XGDTI, 18 RCTs), and Xiaoaiping injection (XAPI, 22 RCTs) (Table 2). Of the 389 RCTs reported, 306 reported DCR, 198 reported Survival Quality Score, 222 reported Incidence of GI Adverse Reactions, 198 reported Incidence of Leukopenia, and 113 reported Incidence of Thrombocytopenia. All included studies were published in Chinese, and the publication years were from 2003 to 2021.

### 3.2 Characteristics and quality of included studies

A total of 31,263 patients (15,854 in intervention groups and 15,409 in control groups) were enrolled in the 389 included studies, all of whom were diagnosed with NSCLC in hospital, based on clear diagnostic criteria. The number of people is (males: 18,588, females: 12,675), and patients had a mean age of 58 years. A total of 3,094 patients received ADI, 499 HCSI, 929 OOMI, 498 DCI, 462 SFI, 788 SMI, 1461 SQFZI, 142 CSI, 284 DLSI, 2373 FFKSI, 244 HQI, 1450 KAI, 1722 KLTI, 370 SI, 702 XGDTI, and 786 XAPI combined with WM therapies. Basic data about the studies analyzed in this paper are listed in (Table 2 and Supplementary Table S2). We assessed the quality of included studies according to the Cochrane Risk of Bias tool. Each evaluation principle was classified as "high risk", "low risk", or "unclear". Of the 389 studies included, 59 RCTs used random number tables for group assignment, 2 used random sampling methods, and 1 applied random assignment by lottery; selection bias associated with random sequence generation in the studies was rated as "low risk". All included studies reported complete outcome indicators, and their attrition bias was assessed as "low

![img-1.jpeg](img-1.jpeg)

**FIGURE 2** Assessment of risk of bias.

risk". Detailed results of the risk of bias assessment are shown in Figure 2.

### 3.3 Primary outcomes

#### 3.3.1 DCR

DCR directly reflects the curative effect of treatments on patients and served as the main outcome index in this study. A total of 16 CHIs assessed in 306 RCTs including 25,783 patients, were included in the DCR analysis. Studies of ADI (*n* = 58), CSI (*n* = 3), DCI (*n* = 11), DLSI (*n* = 6), FFKSI (*n* = 42), HCSI (*n* = 6), HQI (*n* = 3), KAI (*n* = 32), KLTI (*n* = 35), OOMI (*n* = 18), SFI (*n* = 12), SI (*n* = 4), SMI (*n* = 16), SQFZI (*n* = 30), XAPI (*n* = 11), and XGDTI (*n* = 19), each combined with WM, were included. A network diagram is shown in Figure 3A. OR values generated by NMA are shown in Supplementary Table S1. DCR values were significantly higher in patients with NSCLC treated with ADI, CSI, DCI, DLSI, FFKSI, HCSI, KAI, KLTI, OOMI, SFI, SMI, SQFZI, XAPI, or XGDTI combined with WM than in those treated with WM alone. There was no significant difference between DCR in patients treated with HQI or SI combined with WM and those receiving WM treatment alone.

The results of the SUCRA rankings and probability values (Table 3 and Figure 4A), after ranking the effects of the interventions, indicated that CSI was most likely to improve DCR in patients with NSCLC relative to WM treatment alone (probability, 80.90%).

#### 3.3.2 Survival quality score

Improvement in quality of survival was assessed for a total of 16 CHIs, 198 RCTs, and 14,700 patients, including studies of ADI (*n* = 40), CSI (*n* = 3), DCI (*n* = 11), DLSI (*n* = 5), FFKSI (*n* = 25), HCSI (*n* = 2), HQI (*n* = 1), KAI (*n* = 16), KLTI (*n* = 18), OOMI (*n* = 9), SFI (*n* = 7), SI (*n* = 6), SMI (*n* = 8), SQFZI (*n* = 21), XAPI (*n* = 12), and XGDTI (*n* = 14), each combined with WM. A network diagram is shown in Figure 3B. OR values generated by NMA are shown in Supplementary Table S2. Compared with the control group treated with WM alone, survival quality scores of patients with NSCLC treated with WM combined with all CHIs were significantly improved.

After ranking the effects of each intervention, the results of the SUCRA ranking and probability values (Table 3 and Figure 4B) indicated that HQI was most likely to improve survival quality score in patients with NSCLC, compared with controls treated with WM alone (probability, 82.60%).

### 3.4 Secondary outcomes

#### 3.4.1 Incidence of GI adverse reactions

A total of 16 CHIs, 222 RCTs, and 18,720 patients were included in analysis of GI adverse reactions, comprising studies of ADI (*n* = 45), CSI (*n* = 1), DCI (*n* = 8), DLSI (*n* = 5), FFKSI (*n* = 30), HCSI (*n* = 4), HQI (*n* = 1), KAI (*n* = 22), KLTI (*n* = 22), OOMI (*n* = 16), SFI (*n* = 9), SI (*n* = 6), SMI (*n* = 10), SQFZI (*n* = 21), XAPI (*n* = 8), and XGDTI (*n* = 14), each combined with WM. A network diagram is shown in Figure 3C. The OR values generated by NMA are presented in Supplementary Table S3. The rate of GI adverse reactions in patients with NSCLC treated with WM combined with ADI, DCI, CSI, DLSI, FFKSI, HCSI, KAI, KLTI, HQI, SFI, SMI, SQFZI, XAPI, or XGDTI was significantly lower than that in patients treated with WM alone. There was no significant difference in GI adverse events between patients receiving OOMI or SI combined with WM and those treated with WM alone.

After ranking the effects of each intervention, the results of the SUCRA rankings and probability values (Table 3 and Figure 4C) indicated that DCI was most likely to reduce the incidence of leukopenia in patients with NSCLC relative to WM treatment alone (probability, 85.50%).

#### 3.4.2 Incidence of leukopenia

Incidence of leukopenia was analyzed for a total of 16 CHIs, in 198 RCTs, and 16,187 patients, comprising studies on ADI (*n* = 37), CSI (*n* = 1), DCI (*n* = 10), DLSI (*n* = 2), FFKSI (*n* = 27),

![img-2.jpeg](img-2.jpeg)

FIGURE 3

Network graphs for different outcomes. (A) Disease control rate. (B) Survival quality score. (C) Incidence of gastrointestinal adverse reactions. (D) Incidence of leukopenia. (E) Incidence of thrombocytopenia.

HCSI (*n* = 4), HQI (*n* = 3), KAI (*n* = 16), KLTI (*n* = 16), OOMI (*n* = 13), SFI (*n* = 10), SI (*n* = 7), SMI (*n* = 11), SQFZI (*n* = 23), XAPI (*n* = 6), and XGDTI (*n* = 12), each combined with WM. A network diagram is shown in Figure 3D. The OR values generated by NMA are presented in Supplementary Table S4. The incidence of leukopenia in patients with NSCLC treated with a combination of WM and ADI, DCI, OOMI, DLSI, FFKSI, HCSI, KAI, KLTI, SFI, SI, SMI, SQFZI, XAPI, or XGDTI was significantly lower than that in patients treated with WM alone. HQI or CSI combined with WM did not significantly alter the incidence of leukopenia relative to WM treatment alone.

After ranking the effects of each intervention, the results of the SUCRA rankings and probability values (Table 3 and Figure 4D) indicated that SMI was most likely to reduce leukopenia incidence in patients with NSCLC compared with WM alone, with a probability of 79.10%.

### 3.5 Incidence of thrombocytopenia

Analysis of the incidence of thrombocytopenia included a total of 14 CHIs, 113 RCTs, and 12,648 patients in studies of ADI (*n* =

Table 3: Surface under the cumulative ranking probabilities analysis (SUCRA) results for five outcome measures.


21), DCI (n = 3), DLSI (n = 1), FFKSI (n = 17), HCSI (n = 3), KAI (n = 7), KLTI (n = 10), OOMI (n = 1), SFI (n = 6), SI (n = 4), SMI (n = 9), SQFZI (n = 17), XAPI (n = 5), and XGDTI (n = 6), each combined with WM. A network diagram is shown in Figure 3E. OR values generated by NMA are presented in Supplementary Table S5. The incidence of leukocytopenia in patients with NSCLC treated with a combination of WM and ADI, DCI, HQI, DLSI, CSI, FFKSI, HCSI, KAI, KLTI, SFI, SMI, SQFZI, XAPI, or XGDTI was significantly lower than that in patients treated with WM alone; there was no significant difference between patients treated with OOMI or SI combined with WM and those receiving WM alone.

After ranking the effects of each intervention, the results of the SUCRA rankings and probability values (Table 3 and Figure 4E) indicated that HCSI was most likely to reduce the incidence of thrombocytopenia in patients with NSCLC compared with WM alone (probability, 91.30%).

### 3.6 Cluster analysis

Cluster analysis based on SUCRA is illustrated in Figure 5. First, cluster analysis was conducted on DCR and survival quality score. Among eligible treatments, SMI + WM and CSI + WM achieved superior effects over the others in improving DCR and survival quality score, while WM alone ranked toward the bottom. Next, cluster analyses were performed on DCR, survival quality score, and other outcomes. The results revealed that SMI + WM, DCI + WM, and HQI + WM were the highest ranked among the eligible interventions.

### 3.7 Publication bias

To assess whether the primary results of this study were affected by reporting bias, we generated Acomparison-adjusted funnel plot. The points on both sides of the center line of the funnel plot were basically symmetrical from left to right; therefore, we assumed that there was no small sample effect. There was an angle between the correction guideline and the centerline, suggesting that our findings may have been influenced by publication bias to some extent (Figure 6).

## 4 Discussion

The severity of NSCLC has been widely recognized due to its high mortality rates and heavy economic burden (Bray et al. 2018; Miller et al. 2022). Currently, a combination of CHIs and WM is widely adopted in China and has achieved the desired efficacy (Cao et al. 2017; Chen, 2018; Duan et al. 2018; Wang J et al. 2018; Cao et al. 2019; Wang et al. 2019; Feng et al. 2020; Zhu et al. 2022). As aim of this study was to supplement the optimal strategy of NSCLC treatment and to strengthen additional insights for clinical practice in the future, this NMA incorporated 389 RCTs, which included 31,263 patients, comparing the efficacy of Sixteen CHIs combined

![img-3.jpeg](img-3.jpeg)

FIGURE 4 (Continued)
higher the ranking and the higher the probability that the CHIs are the best interventions). (A) Disease control rate. (B) Survival quality score. (C) Incidence of gastrointestinal adverse reactions. (D) Incidence of leukopenia. (E) Incidence of thrombocytopenia.
with WM versus WM alone. According to the results of the cluster analysis and the SUCRA, all eligible CHIs combined with WM were associated with a more beneficial effect than WM alone. Moreover, SMI + WM and DCI + WM are most likely the optimal CHIs to improve disease control rates, survival quality score, and reduce adverse effects. Hence, the efficacy of SMI + WM and DCI + WM should be considered for patients with NSCLC. However, according to the results of the ORs, there was no significant difference between DCR in patients treated with HQI or SI combined with WM and those receiving WM treatment alone. It is worth noting that there are major differences in the numbers of males and females analyzed in this current NMA. Therefore, clinical treatment decisions should be cautious guided by the specific situation and the clinicians experience. The OR and SUCRA values for some treatment strategies generated in this study were very close; therefore, despite clear advantages over other treatment strategies, they do not represent definitive treatment strategy choices in clinical care.

Shenmai injection (SMI), is derived from a well-known traditional Chinese formula, Shendong Yin, in which the primary pharmacological activity constituents are ginsenosides and Ophiopogon (Liu et al. 2018; Xu et al. 2019; Nag et al. 2012; Chen et al. 2021). Several pharmacological studies reported that SMI has antitumor efficacy and is effective in regulating immune function, enhancing body immunity, and reducing the side effects of chemotherapy (Sun et al. 2020; Li S. Y. 2019; Fang et al. 2018). Ginsenoside Rg3 (the preparation named SMI), a principal pharmacological component of Ginseng, has the potential to reverse drug resistance, inhibit the proliferation of NSCLC cells, and protect DNA integrity (Jiang et al. 2017; Liu L et al. 2019). The underlying mechanism may be that they can attenuate the resistance of cisplatin in lung cancer by inhibiting Akt and NFKB, resuming immunity, and regulating DNA damage in NSCLC cells by activating the VRK1/P53BP1 pathway (Jiang et al. 2017; Liu T et al. 2019). These findings reveal the impact of ginsenoside Rg3 on DNA damage and downregulating PD-L1, and it opens a new window for developing new drugs based on ginsenoside Rg3 and presents a foundation for developing new therapeutic strategies for cancers. Sodium cantharidinate (SCA), a semi-synthetic derivative of cantharidin, is chemically synthesized from cantharidin and sodium hydroxide (molecular formula, $\mathrm{C}_{10} \mathrm{H}_{12} \mathrm{Na}_{2} \mathrm{O}_{5}$ ). SCA (the preparation named DCI) has the potential to enhance immune function and inhibit the adhesion, invasion, and metastasis of tumor cells (Wang G et al. 2018; Tao et al. 2017; Wen et al. 2013; Wu et al. 2021). Their an mechanism may be that they can promote the proliferation of T lymphocytes, secrete the cytokine interleukin-2, inhibits the secretion

![img-4.jpeg](img-4.jpeg)

FIGURE 5
Cluster analysis plots for outcomes. Cluster analysis plot of: (A) disease control rate (DCR) and survival quality score, (B) DCR and incidence of gastrointestinal adverse reactions, (C) DCR and incidence of leukopenia, (D) DCR and incidence of thrombocytopenia, (E) survival quality score and incidence of gastrointestinal adverse reactions, (F) survival quality score and incidence of leukopenia, and (G) survival quality score and incidence of thrombocytopenia. Interventions located in the upper right corner indicate optimal therapies for two different outcomes, as follows: A, adi + wm; B, csi + wm; C, dci + wm; D, dIsi + wm; E, f&si + wm; F, hcsi + wm; G, hqi + wm; H, kai + wm; I, kIti + wm; J, oomi + wm; K, sfI4-wm; L, si + wtn; M, smi + win; N, sqfzi + wm; 0, wm; P, xapi + wm; Q, xgdti + wm.

![img-5.jpeg](img-5.jpeg)

FIGURE 6

Funnel plots (A comparison-adjusted funnel plot was used to assess potential publication bias. If points on both sides of the midline in the funnel diagram were symmetric, which meant the correction guideline was at right angles to the midline, it was considered indicative of no significant publication bias). (A) Disease control rate. (B) Survival quality score. (C) Incidence of gastrointestinal adverse reactions. (D) Incidence of leukopenia. (E) Incidence of thrombocytopenia. A, adi + wm; B, csi + wm; C, dci + wm; D, dlsi + wm; E, fflcsi + wm; F, hcsi + wm; G, hqi + wm; H, kai + wm; I, kiti + wm; J, oomi + wm; K, sfi + wm; L, si + wm; M, smi + wm; N, sqfzi + wm; 0, win; P, xapi + wm; Q, xgdti + wm.

of interleukin-8, downregulates the protein expression of VEGF and MMP-9, restrain the formation of new blood vessels, and control tumor cell adhesion (Tao et al., 2017; Wen et al., 2013; Wu et al., 2021). In addition, SCA could reduce the hematopoietic system toxicity of chemoradiotherapy by shortening the bone marrow maturation, releasing leukocytes' time, and promoting the differentiation of hematopoietic stem cells into granulocyte/monocyte progenitor cells, as well as increasing white blood cell counts (Wu et al., 2021). Chansu injection (CSI) combined with WM is considered as the best intervention for improving the Disease Control Rate (DCR). Pharmacological studies have revealed that it has good anti-tumor and anti-inflammatory effects, possibly due to its main active ingredient-Toad (Su et al., 2001). The antitumor mechanism of this combination strategy may be that they can induce apoptosis of A549 cells, suppress the survivin mRNA and protein, and increase caspase-3 activity (Morishita et al., 1992; Wang et al., 2009; Wang et al., 2012).

The safety of CHIs should also be evaluated alongside their effectiveness. Although the incidences of ADRs/ADEs were low in this NMA, approximately two-thirds of eligible RCTs did not report ADRs/ADEs, implying that these analyses did not take the safety issue seriously. While describing ADRs/ADEs, this NMA observed that an appropriate course of treatment is essential in treatment. Moreover, appropriate dosage, solution, and syndrome differentiation should also be emphasized.

The present study has some limitations that should be considered when interpreting the findings: 1) The methodological quality of the included studies was not very high. Only 62 of the 389 RCTs described the correct generation of random sequences and no studies mentioned allocation concealment or blinding. 2) The included studies spanned a relatively long period of time and were published in Chinese journals, and their findings may not be fully generalizable to other locations. 3) Most included RCTs compared CHIs combined with WM for treatment of NSCLC, and there was a lack of direct comparisons of two or more CHIs. 4) The sample sizes included in the RCTs varied in size and significant differences may not be detected by studies with small sample sizes. If the sample size is increased, to balance the number of RCTs targeting different types of CHI could improve the statistical power of the data and the credibility of the NMA. 5) Most relevant RCTs did not report the CHIs dosage and ADRs/ADEs, In terms of the above limitations, more rigorous RCTs with high quality are needed to verify the value of CHIs combined with WM for patients with NSCLC.

Although this study has some limitations, it is the first to comprehensively assess the efficacy and safety of CHIs in combination with WM for treatment of NSCLC, using a NMA to rank DCR, survival quality scores, incidence of GI adverse events, incidence of leukopenia, and incidence of thrombocytopenia. This NMA provides clinicians with a detailed comparison of common treatment strategies and may provide a reference for clinical application.

## 5 Conclusion

Overall, this NMA provides a comprehensive and integrated evaluation and summary of the findings using CHIs for treatment of NSCLC. The current evidence indicates that CHIs combined with WM might have a more beneficial effect on NSCLC patients than WM alone, particularly SMI + WM and DCI + WM. It is imperative for clinicians to consider the efficacy of CHIs when diagnosing and treating patients. Future studies should include high quality RCTs, and real-world data are needed to confirm and support the findings of this NMA.

## Data availability statement

The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding author.

## Author contributions

CP and SL conceived and designed the network metaanalysis. CP, JC, WC, SL, JL, and LP performed the network meta-analysis. JL and WC assessed the quality of the network meta-analysis. CP, JC, WC, SL, JL, and LP analyzed study data, CP and JC wrote the paper. All authors read and approved the final version of the manuscript.

## Funding

This study was supported by the Scientific Foundation of Hunan Provincial Health and Health Commission (No. 202213052746).

## Acknowledgments

We thank the Hunan Province Evidence-Based Medicine Center for their support.

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphar. 2022.1037620/full#supplementary-material

[^0][^1]
[^0]:    Ahn, E. and Kang, H. (2021). Concepts and emerging issues of network meta-analysis. Korean J. Anesthesiol. 74 (5), 371--382. doi:10.4097/kja. 21358

Alexander, M., Kim, S. Y., and Cheng, H. (2020). Update 2020: Management of non-small cell lung cancer. Lung 198 (6), 897-907. doi:10.1007/s00408-020-00407-5

Bray, F., Ferlay, J., Soerjomataram, I., Siegel, R. L., Torre, L. A., and Jemal, A. (2018). Global cancer statistics 2018: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. Ca. Cancer J. Clin. 68 (6), 394-424. doi:10.3322/caac. 21492

Breimer, L. H., Nousios, P., Olsson, L., and Brunnstrom, H. (2020). Immune checkpoint inhibitors of the PD-1/PD-L1-axis in non-small cell lung cancer: Promise, controversies and ambiguities in the novel treatment paradigm. Scand. J. Clin. Lab. Invest. 80 (5), 360-369. doi:10.1080/00365513.2020.1742369

Cao, A., He, H., Jing, M., Yu, B., and Zhou, X. (2017). Shenfu injection adjunct with platinum-based chemotherapy for the treatment of advanced non-small-cell lung cancer: A meta-analysis and systematic review. Evidence-based complementary Altern. Med. 2017, 1068751. doi:10.1155/2017/1068751

Cao, A., He, H., Wang, Q., Li, L., An, Y., and Zhou, X. (2019). Evidence of Astragalus injection combined platinum-based chemotherapy in advanced nonsmall cell lung cancer patients: A systematic review and meta-analysis. Medicine 98 (11), e14798. doi:10.1097/MD.0000000000014798

Cao, W., Chen, H. D., Yu, Y. W., and Li, N. (2021). Changing profiles of cancer burden worldwide and in China: A secondary analysis of the global cancer statistics 2020. Chin. Med. J. 134 (7), 783-791. doi:10.1097/CM9.000000000001474

Chen, G. (2018). Effects of Shenfu injection on chemotherapy-induced adverse effects and quality of life in patients with advanced nonsmall cell lung cancer: A systematic review and meta-analysis. J. Cancer Res. Ther. 14, S549-S555. doi:10. 4103/0973-1482.187299

Chen, Y., Sun, Y., Zhao, Q., Liu, C., and Wang, C. (2021). Shenmai injection enhances cisplatin-induced apoptosis through regulation of Mfs2-dependent mitochondrial dynamics in lung adenocarcinoma A549/DDP cells. Cancer Drug resist. 4 (4), 1047-1060. doi:10.20517/cdr. 2021.94

Cheng, L., Liu, W., Zhong, C., Ni, P., Ni, S., Wang, Q., et al. (2021). Remodeling the homeostasis of pro-and anti-angiogenic factors by Shenmai injection to normalize tumor vasculature for enhanced cancer chemotherapy. J. Ethnopharmacol. 270, 113770. doi:10.1016/j.jep.2020.113770

Cho, J. H. (2017). Immunotherapy for non-small-cell lung cancer: Current status and future obstacles. Immune Netw. 17 (6), 378-391. doi:10.4110/in.2017.17.6.378

Cichello, S. A., Yao, Q., Dowell, A., Leury, B., and He, X. Q. (2015). Proliferative and inhibitory activity of siberian ginseng (situitheroscccos senticosus) extract on cancer cell lines; A-549, XWLC-05, HCT-116, CNS and beas-2b. Asian pso. J. Cancer Prev. 16 (11), 4781-4786. doi:10.7314/apjcp.2015.16.11.4781

Cornell, J. E. (2015). The PRISMA extension for network meta-analysis: Bringing clarity and guidance to the reporting of systematic reviews incorporating network meta-analyses. Ann. Intern. Med. 162 (11), 797-798. doi:10.7326/M15-0930

Dong, X. L., Gong, Y., Chen, Z. Z., and Wang, Y. J. (2014). Delisheng Injection, a Chinese medicinal compound, enhanced the effect of cis-platinum on lung carcinoma cell line PGCL3. Chin. J. Integr. Med. 20 (4), 286-291. doi:10.1007/ s11655-013-1335-0

Duan, B., Xie, J., Rui, Q., Zhang, W., and Xi, Z. (2018). Effects of Shengmai injection add-on therapy to chemotherapy in patients with non-small cell lung cancer: A meta-analysis. Support. Care Cancer 26 (7), 2103-2111. doi:10.1007/ s00520-018-4167-4

Efferth, T., Davey, M., Olbrich, A., Rucker, G., Gebhart, E., and Davey, R. (2002). Activity of drugs from traditional Chinese medicine toward sensitive and MDR1- or MRP1-overexpressing multidrug-resistant human CCRF-CEM leukemia cells. Blood Cells Mol. Dis. 28 (2), 160-168. doi:10.1006/bcmd.2002.0492

Ettinger, D. S., Wood, D. E., Aisner, D. L., Akerley, W., Bauman, J., Chirieac, L. R., et al. (2017). Non-small cell lung cancer, version 5.2017, NCCN clinical practice guidelines in oncology. J. Natl. Compr. Canc. Netw. 15 (4), 504-535. doi:10.6004/ jnccn. 2017.0050

Ettinger, D. S., Wood, D. E., Aisner, D. L., Akerley, W., Bauman, J. R., Bharat, A., et al. (2022). Non-small cell lung cancer, version 3.2022, NCCN clinical practice guidelines in oncology. J. Natl. Compr. Canc. Netw. 20 (5), 497-530. doi:10.6004/ jnccn. 2022.0025

Fang, T., Li, J., and Wu, X. (2018). Shenmai injection improves the postoperative immune function of papillary thyroid carcinoma patients by inhibiting differentiation into Treg cells via miR-103/GPER1 axis. Drug Dev. Res. 79 (7), 324-331. doi:10.1002/ddr. 21459

Feng, F., Huang, J., Wang, Z., Zhang, J., Han, D., Wu, Q., et al. (2020). Xiao-ai-ping injection adjunct with platinum-based chemotherapy for advanced non-smallcell lung cancer: A systematic review and meta-analysis. BMC Complement. Med. Ther. 20 (1), 3. doi:10.1186/s12906-019-2795-y

Garon, E. B., Hellmann, M. D., Rizvi, N. A., Carcereny, E., Leighl, N. B., Ahn, M. J., et al. (2019). Five-year overall survival for patients with advanced non-small-cell lung cancer treated with pembrolizumab: Results from the phase I KEYNOTE-001 study. J. Clin. Oncol. 37 (28), 2518-2527. doi:10.1200/JCO.19.00934

González-Xuriguera, C. G., Vergara-Merino, L., Garognani, L., Ortiz-Munoz, L., and Meza, N. (2021). Introduction to network meta-analysis for evidence synthesis. Medwave 21 (6), e8315. doi:10.5867/medwave.2021.06.8315

Gui, X. M., Dai, L., Yuan, Q. W., and Fan, X. M. (2020). Effect of Kangluite injection in the treatment of advanced non-small cell lung cancer with chemotherapy drugs and its effect on CD-+, 3, CD-+, 4, NK, CD-+, 4/ CD-+, 4. Effect of level. Chin. J. Traditional Chin. Med. 38 (5), 147-150. doi:10. 13193/j.issn.1673-7717.2020.05.034

Han, Y., Wang, H., Xu, W., Cao, B., Han, L., Jia, L., et al. (2016). Chinese herbal medicine as maintenance therapy for improving the quality of life for advanced non-small cell lung cancer patients. Complement. Ther. Med. 24, 81-89. doi:10.1016/j.ctim.2015.12.008

He, X. R., Han, S. Y., and Li, P. P. (2016). Injectable Chinese herbal formula Kang'ai for nonsmall cell lung cancer: Trial sequential analysis of 2, 259 participants from 31 randomized controlled trials. J. Cancer Res. Ther. 12 (2), 735-743. doi:10. 4103/0973-1482.150411

Hu, J. D., and Wang, Y. (2022). Research progress on the anti-tumor mechanism of matrine Chinese. J. Traditional Chin. Med. 40 (5), 171-175. doi:10.13193/j.issn. 1673-7717.2022.05.040

Hutton, B., Salanti, G., Caldwell, D. M., Chaimani, A., Schmid, C. H., Cameron, C., et al. (2015). The PRISMA extension statement for reporting of systematic reviews incorporating network meta-analyses of health care interventions: Checklist and explanations. Ann. Intern. Med. 162 (11), 777-784. doi:10.7326/M14-2385

Jiang, Y., Liu, L. S., Shen, L. P., Han, Z. F., Jian, H., Liu, J. X., et al. (2016). Traditional Chinese medicine treatment as maintenance therapy in advanced non-small-cell lung cancer: A randomized controlled trial. Complement. Ther. Med. 24, 55-62. doi:10.1016/j.ctim.2015.12.006

Jiang, Y., Liu, L. S., Shen, L. P., Liu, J. X., Jiang, G. N., Gu, A. Q., et al. (2019). Traditional Chinese medicine treatment as adjuvant therapy in completely resected stage IB-iiia non-small-cell lung cancer: Study protocol for a multicenter, doubleblind, randomized, placebo-controlled trial. Clin. Lung Cancer 20 (5), e541-e547. doi:10.1016/j.cllc.2019.05.011

Jiang, Z., Yang, Y., Yang, Y., Zhang, Y., Yue, Z., Pan, Z., et al. (2017). Ginsenoside Rg3 attenuates cisplatin resistance in lung cancer by downregulating PD-L1 and resuming immune. Biomed. Pharmacother. = Biomedicine Pharmacother. 96, 378-383. doi:10.1016/j.biopha.2017.09.129

Jiao, L., Dong, C., Liu, J., Chen, Z., Zhang, L., Xu, J., et al. (2017). Effects of Chinese medicine as adjunct medication for adjuvant chemotherapy treatments of nonsmall cell lung cancer patients. Int. Rep. 7, 46524. doi:10.1038/ierp46524

Jiao, Y. N., Wu, L. N., Xue, D., Liu, X. J., Tian, Z. H., Jiang, S. T., et al. (2018). Marsdenia tenacissima extract induces apoptosis and suppresses autophagy through ERK activation in lung cancer cells. Cancer Cell Int. 18, 149. doi:10. 1186/s12935-018-0646-4

Khunger, M., Jain, P., Rakshit, S., Pasupuleti, V., Hernandez, A. V., Stevenson, J., et al. (2018). Safety and efficacy of PD-1/PD-L1 inhibitors in treatment-naive and chemotherapy-refractory patients with non-small-cell lung cancer: A systematic review and meta-analysis. Clin. Lung Cancer 19 (3), e335-e348. doi:10.1016/j.cllc. 2018.01.002

Lemjabbar-Alaoui, H., Hassan, O. U., Yang, Y. W., and Buchanan, P. (2015). Lung cancer: Biology and treatment options. Biochim. Biophys. Acta 1856 (2), 189-210. doi:10.1016/j.bbcav.2015.08.002

Li, L., Shu, Z., Wang, Y., Yang, D., Li, J., Duan, Z., et al. (2019). Pre-treatment with a combination of Shenmai and Danshen injection protects cardiomyocytes against hypoxia/reoxygenation- and H2O2-induced injury by inhibiting mitochondrial permeability transition pore opening. Exp. Ther. Med. 17 (6), 4643-4652. doi:10. 3892/etm.2019.7462

Li, S. Y., Q, X. M., and Li, Ke. (2019). Research progress on immunoregulatory effect and mechanism of astragalus polysaccharides. J. China Med. Univ. (05), 685-689. doi:10.13753/j.issn.1007-6611.2019.05.030

Li, T., Song, S. L., and Huang, G. (2020). Research progress of immune mechanism and treatment status of Chinese medicine for lung cancer. J. Tradit. Chin. Med. 48, 62-66. doi:10.19664/j.cnki.1002-2392.200016

Li, W., Xu, Q., He, Y. F., Liu, Y., Yang, S. B., Wang, Z., et al. (2015). Anti-tumor effect of steamed codonopsis lanceolata in H22 tumor-bearing mice and its possible mechanism. Nutrients 7 (10), 8294-8307. doi:10.3390/nu7105395

Li, Z., Feiyue, Z., and Gaofeng, L. (2021). Traditional Chinese medicine and lung cancer--From theory to practice. Biomed. pharmacotherapy=Biomedecine Pharmacother. 137, 111381. doi:10.1016/j.biopha.2021.111381

Liu, L., Liu, Q., and Fang, Z. (2017). Research progress of Chinese medicine treatment for non-small cell lung cancer. J. Shandong Univ. Tradit. Chin. Med. 41, 386-388. doi:10.16294/j.cnki.1007-659x.2017.04.027

Liu, Q., Wu, H., Wang, J., and Li, X. M. (2018). Effects of Shenmai injection on the values of CO, SV, and ef in patients undergoing off-pump coronary artery bypass graft: A randomized, clinical trial. Medicine 97 (10), e0085. doi:10.1097/MD. 0000000000010085

Liu, S. X., He, H. H., Jia, R., Du, J., Lin, S., and Li, Y. (2021). Research progress on mechanism of traditional Chinese medicine in treating lung cancer. Clin. Res. Tradit. Chin. Med. (5), 132-134.

Liu, T., Zuo, L., Guo, D., Chai, X., Xu, J., Cui, Z., et al. (2019). Ginsenoside Rg3 regulates DNA damage in non-small cell lung cancer cells by activating VRK1/ P53BP1 pathway. Biomed. Pharmacother. = Biomedecine Pharmacother. 120, 109483. doi:10.1016/j.biopha.2019.109483

Lu, X. (2011). Effect of Shengmai injection combined with chemotherapy on quality of life and immune function of advanced non-small cell lung cancer. Shaanxi Tradit. Chin. Med. 32 (04), 389-391.

Luo, L. H., Song, Z. H., Yang, J. J., Li, H. J., Kang, G. Q., and Shi, X. (2019). Effect of Brucea javanica oil emulsion combined with TP chemotherapy on immune function of patients with advanced non-small cell lung cancer. World Tradit. Chin. Med. 14 (8), 2087-2091.

Lv, L., Deng, M. H., and Guo, L. Y. (2021). Effect of lentinan as adjuvant therapy on immune function of patients with non-small cell lung cancer. China Health Stand. Manag. 12 (14), 101-104.

Ma, C., and Xu, L. (2017). Research progress of Chinese medicine in the treatment of lung cancer. Chin. J. Tradit. Chin. Med. 35, 1100-1103. doi:10.13193/j.issn.16737717.2017.05.013

Meng, Q., Pan, J., Liu, Y., Chen, L., and Ren, Y. (2018). Anti-tumour effects of polysaccharide extracted from Acanthopanax senticosus and cell-mediated immunity. Exp. Ther. Med. 15 (2), 1694-1701. doi:10.3892/etm.2017.5568

Miller, K. D., Fidler-Benaoudia, M., Keegan, T. H., Hipp, H. S., Jemal, A., and Siegel, R. L. (2020). Cancer statistics for adolescents and young adults, 2020. Ca. Cancer J. Clin. 70 (6), 443-459. doi:10.3322/caac. 21637

Miller, K. D., Nogueira, L., Devasia, T., Mariotto, A. B., Yabroff, K. R., Jemal, A., et al. (2022). Cancer treatment and survivorship statistics, 2022. Ca. Cancer J. Clin. 72 (5), 409-436. doi:10.3322/caac. 21731

Miller, K. D., Siegel, R. L., Lin, C. C., Mariotto, A. B., Kramer, J. L., Rowland, J. H., et al. (2016). Cancer treatment and survivorship statistics, 2016. Ca. Cancer J. Clin. 66 (4), 271-289. doi:10.3322/caac. 21349

Minguet, J., Smith, K. H., and Bramlage, P. (2016). Targeted therapies for treatment of non-small cell lung cancer--Recent advances and future perspectives. Int. J. Cancer 138 (11), 2549-2561. doi:10.1002/ijc. 29915

Mo, S. X. (2010). Effect of Brucea javanica oil emulsion combined with chemotherapy on immune function of patients with non-small cell lung cancer after surgery. J. Med. Integr. Chin. West. Med. 19 (9), 1098-1099.

Molina, J. R., Yang, P., Cassivi, S. D., Schild, S. E., and Adjei, A. A. (2008). Nonsmall cell lung cancer: Epidemiology, risk factors, treatment, and survivorship. Mayo Clin. Proc. 83 (5), 584-594. doi:10.4065/83.5.584

Morishita, S., Shoji, M., Oguni, Y., Jin, C., HiguchiM.and SakanashiM. (1992). Pharmacological actions of "kyushin, " a drug containing toad venom: Cardiotonic and arrhythmogenic effects, and excitatory effect on respiration. Am. J. Chin. Med. 20, 243-256. doi:10.1142/S0192413X92000254

Nag, S. A., Qin, J. J., Wang, W., Wang, M. H., Wang, H., and Zhang, R. (2012). Ginsenosides as anticancer agents: In vitro and in vivo activities, structure-activity relationships, and molecular mechanisms of action. Front. Pharmacol. 3, 25. doi:10. 3389/fphar.2012.00025

Quoix, E., Zalcman, G., Oster, J. P., Westeel, V., Pichon, E., Lavole, A., et al. (2011). Carboplatin and weekly paclitaxel doublet chemotherapy compared with monotherapy in elderly patients with advanced non-small-cell lung cancer: DCT0501 randomised, phase 3 trial. Lancet (London, Engl. 378 (9796), 1079-1088. doi:10.1016/S0140-6736(11)60780-0

Reck, M., Remon, J., and Hellmann, M. D. (2022). First-line immunotherapy for non-small-cell lung cancer. J. Clin. Oncol. 40 (6), 586-597. doi:10.1200/JCO.21. 01497

Ren, S., Xiong, X., You, H., Shen, J., and Zhou, P. (2021). The combination of immune checkpoint blockade and angiogenesis inhibitors in the treatment of advanced non-small cell lung cancer. Front. Immunol. 12, 689132. doi:10.3389/ fimmu.2021.689132

Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., et al. (2021). PRISMA-S: An extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst. Rev. 10 (1), 39. doi:10.1186/s13643-020-01542-x

Salanti, G., Ades, A. E., and Ioannidis, J. P. (2011). Graphical methods and numerical summaries for presenting results from multiple-treatment meta-analysis: An overview and tutorial. J. Clin. Epidemiol. 64 (2), 163-171. doi:10.1016/j.jclinepi. 2010.03.016

Sang, G. Y., Wei, S., and Liu, C. (2008). Research progress on anti-tumor mechanism and clinical application of Astragalus membranaceus. Shizhen Tradit. Chin. Med. 19 (12), 3032-3034.

Schwingshackl, L., Schwarzer, G., Rücker, G., and Meerpohl, J. J. (2019). Perspective: Network meta-analysis reaches nutrition research: Current status, scientific concepts, and future directions. Adv. Nutr. 10 (5), 739-754. doi:10. 1093/advances/nnut016

Shojaee, S., and Nana-Sinkam, P. (2017). Recent advances in the management of non-small cell lung cancer. F1000Res. 6, 2110. doi:10.12688/f1000research.11471.1

Siegel, R. L., Miller, K. D., Fuchs, H. E., and Jemal, A. (2021). Cancer statistics, 2021. Ca. Cancer J. Clin. 71 (1), 7-33. doi:10.3322/caac. 21654

Stock-Martineau, S., Magner, K., Jao, K., and Wheatley-Price, P. (2021). Challenges of immunotherapy in stage IV non-small-cell lung cancer. JCO Oncol. Pract. 17 (8), 465-471. doi:10.1200/OP.20.00949

Su, Y. H., and Niu, X. (2001). Review on the pharmacodynamic effect of bulonis preparation. J. Beijing Univ. Traditional Chin. Med. 2001 (2), 51-54.

Sun, Y., Chen, Y., Xu, M., Liu, C., Shang, H., and Wang, C. (2020). Shenmai injection supresses glycolysis and enhances cisplatin cytotoxicity in cisplatinresistant A549/DEP cells via the AKT-mTOR-c-myc signaling pathway. Biomed. Res. Int. 2020, 9243681. doi:10.1155/2020/9243681

Sung, H., Ferlay, J., Siegel, R. L., Laversanne, M., Soerjomataram, I., Jemal, A., et al. (2021). Global cancer statistics 2020: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. Ca. Cancer J. Clin. 71 (3), 209-249. doi:10.3322/caac. 21660

Tan, X., Liang, X., Xi, J., Guo, S., Meng, M., Chen, X., et al. (2021). Clinical efficacy and safety of Huachansu injection combination with platinum-based chemotherapy for advanced non-small cell lung cancer: A systematic review and meta-analysis of randomized controlled trials. Medicine 100 (36), e27161. doi:10.1097/MD. 0000000000027161

Tan, Y., and Wang, Y. (2016). Research progress in Chinese medicine for nonsmall cell lung cancer. J. Liaoning Univ. Tradit. ChinMed. 18, 128-130. doi:10. 13194/j.issn.1673-842x

Tao, R., Sun, W. Y., Yu, D. H., Qiu, W., Yan, W. Q., Ding, Y. H., et al. (2017). Sodium cantharidinate induces HepG2 cell apoptosis through LC3 autophagy pathway. Oncol. Rep. 38 (2), 1233-1239. doi:10.3892/or.2017.5779

Wang, B., Wang, X., and Li, Z. (2018). Research progress of Chinese medicine in the treatment of lung cancer. J. Tradit. Chin. Med. 33, 371-374. doi:10.16368/j.issn. 1674-8999.2018.03.090

Wang, G., Dong, J., and Deng, L. (2018). Overview of cantharidin and its analogues. Curr. Med. Chem. 25 (17), 2034-2044. doi:10.2174/ 0929867324666170414165253

Wang, J., Jin, Y., Xu, Z., Zheng, Z., and Wan, S. (2009). Involvement of caspase-3 activity and survivin downregulation in cinobufocini-induced apoptosis in A 549 cells. Exp. Biol. Med. 234 (5), 566-572. doi:10.3181/ 0811-RM-326

Wang, J., Li, G., Yu, L., Mo, T., Wu, Q., and Zhou, Z. (2018). Aidi injection plus platinum-based chemotherapy for stage IIIB/IV non-small cell lung cancer: A metaanalysis of 42 RCTs following the PRISMA guidelines. J. Ethnopharmacol. 221, 137-150. doi:10.1016/j.jep.2018.04.013

Wang, J. Y., Chen, L., Zheng, Z., Wang, Q., Guo, J., and Xu, L. (2012). Cinobufocini inhibits NF- $\alpha$ B and COX-2 activation induced by TNF- $\alpha$ in lung adenocarcinoma cells. Oncol. Rep. 27 (5), 1619-1624. doi:10.3892/or.2012.1647

Wang, M., Herbst, R. S., and Boshoff, C. (2021). Toward personalized treatment approaches for non-small-cell lung cancer. Nat. Med. 27 (8), 1345-1356. doi:10. 1038/s41591-021-01450-2

Wang, Z., Feng, F., Wu, Q., Jin, Y., Gu, J., Xu, Y., et al. (2019). Disodium cantharidinate and vitamin B6 injection adjunct with platinum-based chemotherapy for the treatment of advanced non-small-cell lung cancer: A meta-analysis. Evidence-based complementary Altern. Med. 2019, 9386273. doi:10.1155/2019/9386273

Watt, J., and Del Giovane, C. (2022). Network meta-analysis. Methods Mol. Biol. 2345, 187-201. doi:10.1007/978-1-0716-1566-9_12

Watt, J., Tricco, A. C., Straus, S., Veroniki, A. A., Naglie, G., and Drucker, A. M. (2019). Research techniques made simple: Network meta-analysis. J. Invest. Dermatol. 139 (1), 4-12. e1. doi:10.1016/j.jid.2018.10.028

Wen, S. Q., Chen, Q., and Hu, M. (2013). Experimental study on the inhibitory effect of sodium cantharidinate on human hepatoma HepG2 cells. Afr. J. Tradit. Complement. Altern. Med. 11 (1), 131-134. doi:10.4314/ajri.arn.v11i1.20

Wu, L., Deng, C., Zhang, H., Weng, J., Wu, Y., Zeng, S., et al. (2021). Efficacy and safety of docetaxel and sodium cantharidinate combination vs. Either agent alone as second-line treatment for advanced/metastatic NSCLC with wild-type or unknown EGFR status: An open-label, randomized controlled, prospective, multi-center phase III trial (Cando-L1). Front. Oncol. 11, 769037. doi:10.3389/fonc.2021.769037

Wu, X., Chung, V., Lu, P., Poon, S. K., Hui, E. P., Lau, A. Y. L., et al. (2016). Chinese herbal medicine for improving quality of life among nonsmall cell lung cancer patients: Overview of systematic reviews and network meta-analysis. Medicine 95 (1), e2410. doi:10.1097/MD.0000000000002410

Xia, L., Liu, Y., and Wang, Y. (2019). PD-1/PD-L1 blockade therapy in advanced non-small-cell lung cancer: Current status and future directions. Oncologist 24, S31-S41. doi:10.1634/theoncologist.2019-IO-S1-s05

Xie, Y. A. G., Shen, K. P., and Lu, Y. L. (2021). Research progress in Chinese medicine for non-small cell lung cancer. Chin. J. Traditional Chin. Med. 36, 2846-2851.

Xiong, Y., Zhao, Q., Gu, L., Liu, C., and Wang, C. (2018). Shenqi Fuzheng injection reverses cisplatin resistance through mitofusin-2-mediated cell cycle arrest and apoptosis in A549/DDP cells. Evidence-based complementary Altern. Med. 2018, 8258246. doi:10.1155/2018/8258246

Xu, H., Liu, Y., Wang, D., and Zhang, Z. (2019). Shenmai injection maintains blood-brain barrier integrity following focal cerebral ischemia via modulating the expression and trafficking of occludin in lipid rafts. J. Ethnopharmacol. 237, 55-63. doi:10.1016/j.jep.2019.03.034

Xu, L. L., Zhang, S. F., Wang, Y. L., Luo, Y. B., Fang, Z. H., Fang, Y., et al. (2021). The efficacy of long-term Chinese herbal medicine use on lung cancer survival time: A retrospective two-center cohort study with propensity score matching. Evid. Based. Complement. Altern. Med. 2021, 5522934. doi:10.1155/2021/5522934

Xu, S., Zhao, S. K., Ren, F., Ren, D., Wang, Y. Y., and Song, Z. Q. (2020). Progress and prospect of new adjuvant targeting and immunotherapy for non-small cell lung cancer. Chin. Clin. Oncol. 47 (6), 299-303.

Yao, C., Su, L., Zhang, F., Zhu, X., Zhu, Y., Wei, L., et al. (2020). Thevebioside, the active ingredient of traditional Chinese medicine, promotes ubiquitin-mediated SRC-3 degradation to induce NSCLC cells apoptosis. Cancer Lett. 493, 167-177. doi:10.1016/j.canlet.2020.08.011

Yomeda, K., Imanishi, N., Ichiki, Y., and Tanaka, F. (2018). Immune checkpoint inhibitors (ICIs) in non-small cell lung cancer (NSCLC). J. LOEH 40 (2), 173-189. doi:10.7888/juoeh.40.173

Zhang, B. B., Song, Z. H., He, C. X., Yu, X. M., Lou, G. Y., Hong, D., et al. (2013). Clinical efficacy of different doses of gemcitabine combined with carboplatin in first-line treatment of advanced non-small cell lung cancer. J. Oncol. (12), 977-980.

Zhang, X. W., Liu, W., Jiang, H. L., and Mao, B. (2018). Chinese herbal medicine for advanced non-small-cell lung cancer: A systematic review and meta-analysis. Am. J. Chin. Med. 46 (5), 923-952. doi:10.1142/S0192415X18500490

Zhao, R., and Gao, Y. X. (2012). Research progress on immune regulation of astragalus polysaccharides. Clin. Res. Traditional Chin. Med. 4 (5), 4-6.

Zheng, J. B., Li, B. X., Cheng, Q. W., Li, D., and Lin, H. S. (2017). Research progress in post-operative treatment of non-small cell lung cancer patients with traditional Chinese medicine China. Cancer Clin. Rehabil. (1), 125-128. doi:10.13455/j.cnkicjcor.2017.01.36

Zhong, C., Jiang, C., Ni, S., Wang, Q., Cheng, L., Wang, H., et al. (2020). Identification of bioactive anti-angiogenic components targeting tumor endothelial cells in Shenmai injection using multidimensional pharmacokinetics. Acta Pharm. Sin. B 10 (9), 1694-1708. doi:10.1016/j.apsb.2019.12.011

Zhou, F., and Zhou, C. C. (2021). Immunotherapy in non-small cell lung cancer: Advancements and challenges. Chin. Med. J. 134 (10), 1135-1137. doi:10.1097/ CM9.0000000000001338

Zhu, D., Xu, Y., Feng, F., Wang, Z., Han, D., and Zhou, X. (2022). Effect of kangai injection combined with platinum-based chemotherapy on the immune function of patients with advanced non-small-cell lung cancer: A meta-analysis. Phytomedicine. 100, 154088. doi:10.1016/j.phymed.2022.154088