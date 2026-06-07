# A network meta-analysis of efficacy and safety for first-line and second/further-line therapies in postmenopausal women with hormone receptor-positive, HER2-negative, advanced breast cancer 

Hanqiao Shao ${ }^{1,2 \dagger}$, Mingye Zhao ${ }^{1,2 \dagger}$, Ai-Jia Guan ${ }^{3}$, Taihang Shao ${ }^{1,2}$, Dachuang Zhou ${ }^{1,2}$, Guo Yu ${ }^{4 *}$ and Wenxi Tang ${ }^{1,2 *}$


#### Abstract

Background Hormone receptor-positive/human epidermal growth factor receptor 2-negative (HR + /HER2 - ) advanced breast cancer is a prevalent subtype among postmenopausal women. Despite the growing number of randomized clinical trials (RCTs) exploring this topic, the efficacy and safety of first-line and second/further-line treatments remain uncertain. Accordingly, our aim was to conduct a comprehensive evaluation of the efficacy and safety of these therapies through network meta-analysis.


Methods RCTs were identified by searching Pubmed, Embase, and major cancer conferences. The efficacy of interventions was assessed using the hazard ratios (HRs) of progression-free survival (PFS) and overall survival (OS), while safety was indicated by the incidence of any grade adverse events (AEs), grade 3-5 AEs, AEs leading to treatment discontinuation, and AEs leading to death. Both time-variant HRs fractional polynomial models and time-invariant HRs Cox-proportional hazards models were considered for handling time-to-event data. Safety indicators were analyzed using Bayesian network meta-analysis. Additionally, subgroup analyses were conducted based on patient characteristics.
Results A total of 41 RCTs (first-line 17, second/further-lines 27) were included in the analysis. For first-line treatment, the addition of Cyclin-dependent kinase 4 and 6 (CDK4/6) inhibitors to endocrine therapy significantly improved therapeutic efficacy in terms of both PFS and OS, demonstrating the best performance across all mechanisms. Specifically, the combination of Abemaciclib and Letrozole demonstrated the most favorable performance in terms of PFS, while Ribociclib plus Fulvestrant yielded the best outcomes in OS. Incorporating the immune checkpoint inhibitor Avelumab into the regimen with CDK4/6 inhibitors and selective estrogen receptor degraders significantly enhanced both PFS and OS in second-line or later treatments. Regarding safety, endocrine monotherapy performed well.

[^0]
[^0]:    ${ }^{1}$ Hanqiao Shao and Mingye Zhao contributed equally to this work.
    *Correspondence:

    Guo Yu
    guoyu@cpu.edu.cn
    Wenxi Tang
    tokammy@cpu.edu.cn
    Full list of author information is available at the end of the article

Regarding safety, endocrine monotherapy performed well. There is mounting evidence suggesting that most CDK4/6 inhibitors may demonstrate poorer performance with respect to hematologic AEs. However, additional evidence is required to further substantiate these findings.

Conclusions CDK4/6 inhibitors, combined with endocrine therapy, are pivotal in first-line treatment due to their superior efficacy and manageable AEs. For second/further-line treatment, adding immune checkpoint inhibitors to CDK4/6 inhibitors plus endocrine therapy may produce promising results. However, to reduce the results' uncertainty, further trials comparing these novel treatments are warranted.

Trial registration Registration number: PROSPERO (CRD42022377431).

Keywords HR-positive/HER2-negative, Advanced breast cancer, Efficacy, Safety, Network meta-analysis

## Background

Breast cancer is a prevalent malignancy and the primary cause of cancer-related death among women globally. It constitutes 15.5% of all female cancer fatalities [1], with around 2.3 million new breast cancer cases recorded worldwide in 2020 and approximately 685,000 deaths [2]. According to the Surveillance, Epidemiology, and End Results database of the National Cancer Institute in the USA, it is estimated that there will be about 297,790 new cases of breast cancer and 43,170 breast cancer-related deaths in 2023. These account for 15.2% of all new cancer cases and 7.1% of all cancer-related deaths, respectively [3]. Most breast cancer cases occur in females (approximately 99%), but there are approximately 2500 new cases of breast cancer diagnosed in males annually in the USA [4]. In clinical practice, breast cancer is commonly subtyped by hormone receptor (HR) and human epidermal growth factor receptor 2 (HER2). The subtype of HR-positive/HER2-negative represents the most prevalent among all racial groups, accounting for approximately 68% of cases across all ethnicities [5]. Historically, the estrogen receptor signaling pathway primarily drives cancer cell growth and survival in these tumors, these tumors were treated with endocrine therapy (ET) [6, 7]. However, due to limitations in single-agent endocrine therapy efficacy and the presence of primary or secondary drug resistance, endocrine monotherapy is increasingly insufficient for clinical treatment. The development of targeted therapies including Cyclin-dependent kinase 4 and 6 inhibitors (CDK4/6i) and immune checkpoint inhibitor (ICI), particularly in combination with ET, has revolutionized the management of these tumors [8]. Nonetheless, the comparative efficacy and safety of most first-line and second/further-line treatments remain uncertain. While some randomized controlled trials (RCTs) have verified the safety and efficacy of targeted therapies or combined targeted endocrine therapy for patients with HR+/HER2-advanced breast cancer, the absence of head-to-head comparisons prevents us from determining which treatment offers the greatest survival advantage.

Furthermore, existing network meta-analyses (NMA) have only evaluated a limited range of treatment options for efficacy and safety [9--12], without delving into the mechanisms of targeted therapies [13]. Notably, nearly all these studies were executed using the proportional hazards (PH) model, without verifying the PH assumption. Nonetheless, it is important to note that the hazard ratios (HRs) represent the efficacy ratio within a specific time frame between treatments, calculated using a semiparametric Cox-proportional hazards (Cox-PH) model [14]. In most studies, the PH assumption was not valid, indicating that the relative efficacy between treatments varied over time. This potential limitation may compromise the reliability and accuracy of the results [15]. Consequently, our study aimed to compare the efficacy and safety of first-line and second/further-line therapies in treating postmenopausal female patients with HR+/HER2-advanced breast cancer, using an adjusted indirect comparison under a Bayesian framework that assumes non-PH.

## Methods

## Protocol

This study was conducted according to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension statement for network meta-analyses of healthcare interventions [16] (Additional file 1: Table S1). The research plan for this project has been registered in PROSPERO (CRD42022377431).

## Data sources

A systematic search was conducted across various databases and websites such as PubMed, Embase, the European Society for Medical Oncology, the American Society of Clinical Oncology, the San Antonio Breast Cancer Symposium conference, and the Chinese Society of Clinical Oncology. Our focus was on studies published between November 2007 and November 2022, specifically those concerning the treatment of HR+/HER2-advanced postmenopausal women with breast cancer. Considering that in 2007, the US Food and Drug

Administration (FDA) updated the guidance for clinical trials in oncology, leading to more consistent choices of endpoints [17]. The following keywords were mainly used: "hormone receptor-positive", "human epidermal factor receptor 2 negative", "advanced/metastatic breast cancer", and "randomized controlled trials". Details of the search strategies are given in Additional file 1: Table S2.

## Inclusion and exclusion criteria

Studies that met the following inclusion criteria and provided a clear description of patient characteristics were included in the NMA:(1) Population: Women with HR+/HER2 - postmenopausal advanced breast cancer.(2) Interventions and comparisons: Single-agent chemotherapy, endocrine therapy monotherapy, targeted therapy, and combinations of endocrine therapy with targeted therapy were considered.(3) Outcome: The HRs of overall survival (OS), progression-free survival (PFS), and the objective response rate were examined. Adverse events (AEs) incidences were categorized into multiple groups: AEs of any grade, grade 3--5 AEs, AEs leading to discontinuation, and AEs leading to death. Attention was also given to the incidence rates of the three most common specific AEs, which included both hematologic and non-hematologic types, across any grade and specifically within grades 3--5. The presence of at least one Kaplan--Meier curve for either OS or PFS was a requirement. If specific data related to postmenopausal women were provided in any RCTs, those trials were included in this study.(4) Study design: phase II or phase III RCTs.

Some articles were excluded based on the following criteria:(1) Papers published before 2007.(2) Non-RCTs or single-arm RCTs.(3) Trials with unclear clinical outcomes.(4) RCTs that included only premenopausal patients and HER2-positive or triple-negative breast cancer patients alone.

All retrieved articles were imported into Note Express (version 3.2.0.7535). The literature was reviewed by two researchers (HS and MZ). Disagreements among the reviewers were settled through discussion. A third reviewer (GY) was consulted if necessary. Titles and abstracts were first screened. The full text of the literature selected for inclusion was then evaluated. Finally, the included literature was reviewed for the inclusion of the most recent data from the relevant studies.

## Data extraction

Baseline characteristics and clinical outcomes were extracted independently by two investigators for participants in each treatment group in the following study designs: RCTs' names, sample size, median age, and follow-up time. Clinical outcomes extracted included HRs of OS and PFS, any grade AEs, grade 3--5 AEs, AEs leading to discontinuation of treatment, and AEs leading to death. Additionally, we considered the three most common AEs, encompassing both hematologic and nonhematologic types, across all grades and specifically within grades 3--5. Survival data from the independent review committee were prioritized. For trials where independent review committee data were not available, investigator-assessed outcomes were extracted.

## Quality assessment

RCTs were assessed using the Cochrane risk of bias tool measure [18]. We used Egger regression tests with funnel plots to assess publication bias and which were considered significantly asymmetric and publication biased if $p<0.1$.

## Statistical analysis

Interventions identified in the RCTs were extracted and categorized according to their mechanisms of action, utilizing resources from PubChem [19]. Furthermore, the FDA approval status of the drugs was ascertained by referencing the National Cancer Institute [20]. The Engauge Digitizer (version 4.1) was utilized to extract survival data from PFS and OS Kaplan--Meier curves [21]. Guyot's method was used to reconstruct individual patient data and then fit the survival data [22]. This is one of the most accurate data-reconstruction methods for cases where individual patient data are not available [23]. Through visual inspection, the reconstructed curves were consistent with the original curves.

The assumption of PH for each trial was first evaluated for time-to-event data, acknowledging that HRs between different treatments often vary over time. Logcumulative hazard plots and Schoenfeld residual tests were used for this analysis [24, 25]. Clear violations of the PH assumption were detected in several firstline and second/further-lines trials (Additional file 1: Table S3). Therefore, relying solely on the HR derived from the Cox-PH model as the effect measure for NMA is not sufficient. Instead, we fitted a series of first-order fractional polynomial (FP) models with power parameters $-2,-1,-0.5,0.5,1,2$, and 3 . Akaike information

criterion was used to assess goodness-of-fit [26, 27]. Frequency models were utilized for time-to-event data outcomes.

When the PH assumption did not hold, FP models were employed. To compare the effects of all treatments, life years for each treatment were calculated within 10 years. This horizon was selected as it is a more representative survival duration for the treatment of advanced breast cancer. When the PH assumption was held, the Cox-PH model was applied using the “netmeta” package in R, version 4.2.2. Additionally, given that some studies did not include Kaplan--Meier curves, we conducted a Cox-PH analysis to establish a comprehensive network and present conservative findings [28]. In the subgroup analysis, factors such as patient age, presence of visceral metastasis, ethnicity, and the occurrence of pivotal gene mutations were considered.

Bayesian NMA was used for safety, which could be realized by the R package "BUGSnet" [29]. The analysis was conducted through four parallel Markov chains comprising 50,000 samples after a 10,000-sample burn-in. We used the "gemtc" package in R, version 4.2.2. Log odds ratios with 95% credible intervals were used as effect sizes. Heterogeneity between studies was assessed using Cochran's Q test and I^{2} statistic within a visual forest plot, I^{2} statistic > 50%, or the P value < 0.1 for the Q test was considered as indicating significant heterogeneity, the inconsistency of this model was evaluated using the edge-splitting method, which took into account all direct and indirect evidence [30, 31]. The fixed effect model was only considered when the conditions I^{2} < 50% or P value of the Q test < 0.1 were met, and all points in the leverage plot were within the purple area. In all other circumstances, a random effects model was used [32]. The convergence of Markov chains was checked using trace plots and Gelman-Rubin diagnostic statistics [26].

## Results

### Study selection and characteristics of included studies

A total of 1291 records were retrieved from the database. After excluding 163 duplicates, 41 RCTs were retained following the primary screening of titles, abstracts, and full-text re-screening based on the PICOS principles. These consisted of 52 full-text articles and 9 abstracts [33--93]. The flow chart of the literature search process is shown in Fig. 1. All included studies exhibited high overall quality. Seventeen RCTs with 7062 patients were included in the first-line analysis, and 27 RCTs with 10,211 patients were included in the second/further-lines analysis (Additional file 1: Table S4-Table S5). The FDA approval status of the drugs is shown in Additional file 1: Table S6.

### Risk of bias

The risk of bias assessment was presented in Additional file 2: Figure S1. Overall, the risk of bias was generally low across all RCTs. However, some included RCTs were open-label, elevating the risk of bias in participant and personnel blinding as well as allocation concealment. The results of the risk of bias assessment were shown in Additional file 2: Figure S2, and Egger regression tests were used to determine publication bias, with p-values of 0.69 for first-line PFS and 0.21 for first-line OS, respectively, and 0.14 for second/further-lines PFS and 0.36 for second/further-lines OS. Consequently, there was no publication bias in our network.

### Efficacy outcomes

### Progression-free survival for first-line treatments

The NMA encompassed 15 therapies and 7 mechanisms, respectively (Fig. 2A,B). The PH assumption was invalidated in this network, resulting in the selection of the FP model, which fit the data at power parameters = - 1 (Additional file 1: Table S7). In terms of 10-year PFS of the therapies (Fig. 3A and Additional file 2: Figure S3A), Abemaciclib/Letrozole demonstrated the best PFS benefit, providing a life-year gain over 10 years of 3.39 years. Dalpiciclib/Letrozole and Palbociclib/Letrozole were found to be comparable to Abemaciclib/Letrozole, with life-years gained over 10 years of 3.37 and 3.13 years, respectively. Bayesian NMA provided consistent treatment rankings for Cox-PH model (Additional file 1: Table S8). Concerning the 10-year PFS of the mechanisms (Fig. 5A and Fig. 5C), CDK4/6i in combination with ET performed the best, with CDK4/6i plus selective estrogen receptor degrader (SERD) (3.48 life years) slightly outperforming CDK4/6i plus aromatase inhibitor (AI) (3.30 life years). A similar trend was observed in the results from the Cox-PH model (Additional file 2: Figure S4).

### Overall survival for first-line treatments

The NMA respectively incorporated 11 therapies and 6 mechanisms (Fig. 2C,D). The PH assumption was validated in this network, leading to the choice of the Cox-PH model. The results of the Cox-PH model (Fig. 3B) showed that compared with the Letrozole, several treatments, including Abemaciclib/Fulvestrant (HR, 0.60 [95% CI, 0.38 ~ 0.93]), Abemaciclib/Letrozole (0.76 [0.59 ~ 0.99]), Fulvestrant (0.70 [0.50 ~ 0.98]), Ribociclib/Fulvestrant (0.45 [0.28 ~ 0.71]), Ribociclib/Letrozole (0.76 [0.63 ~ 0.92]), and Fulvestrant/Anastrozole (0.82 [0.69 ~ 0.98]) all significantly improved OS in first-line patients to varying extents. Additionally, for first-line mechanisms, whether considering the Cox-PH model

![img-0.jpeg](img-0.jpeg)

Fig. 1 Flow diagram of literature search and study identification

(Additional file 2: Figure S4) or the FP model (Fig. 5B,C), the results consistently indicated superior performance of CDK4/6i combined with SERD or AI.

### Progression-free survival for second/further-line treatments

In the NMA of second/further-lines PFS, a total of 28 therapies and 14 mechanisms were incorporated (Fig. 2E,F). The PH assumption was invalidated in this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7). Regarding to 10-year PFS for various therapies (Fig. 4 and Additional file 2: Figure S3B), the combination of Palbociclib, Fulvestrant, and Avelumab emerged as the most effective, contributing to a life-year gain of 2.58 years over a decade. Dalpiciclib/Fulvestrant and Everolimus/Exemestane followed this network, leading to the selection of the FP model, which fit the data at power parameters = - 2 (Additional file 1: Table S7).

![img-1.jpeg](img-1.jpeg)

Fig. 2 (See legend on previous page.)

![img-2.jpeg](img-2.jpeg)

Fig. 3 Summary results of efficacy outcomes for the first-line treatment. (A Life-year results within 10 years for first-line therapies' PFS. B Cox-PH model result for first-line therapies' OS). Abbreviations: Aberna, Abemaciclib; ANA, Anastrozole; BEV, Bevacizumab; EXE, Exemestane; FUL, Fulvestrant; LET, Letrozole; Palbo, Palbociclib; Ribo, Ribociclib. Note: The direction of the reported relative effects in each cell is defined as treatment on the right vs. treatment on the left. Values < 1 favor the intervention on the right. Values in parenthesis are 95% credible intervals (95% CIs). Bold cells correspond to statistically significant relative effects for the respective treatment categories

closely, yielding life-year gains of 2.35 and 2.32 years respectively over the same period. Contrarily, results from the Cox-PH model (Additional file 1: Table S9) suggested that single-agent chemotherapy (Eribulin, Gemcitabine, or Capecitabine) outperformed others, with Everolimus/Exemestane ranking second. When examining 10-year PFS for different mechanisms (Fig. 5D and F), the combination of CDK4/6i, SERD, and ICI (2.76 life years) demonstrated the greatest benefit, followed by single-agent chemotherapy (2.49 life years). The Cox-PH model exhibited a similar trend (Additional file 2: Figure S5).

## Overall survival for second/further-line treatments

In this portion, the NMA incorporated 16 therapies and 12 mechanisms (Fig. 2G,H). The PH assumption was not sustained in this network, prompting the use of the FP model with power parameters set at - 1 (Additional file 1: Table S7). In terms of 10-year OS for therapies (Fig. 4 and Additional file 2: Figure S3C), the combination of Palbociclib, Fulvestrant, and Avelumab exhibited the best OS benefit, contributing to a life-year gain of 4.84 years over a decade. This was followed by Ribociclib/Fulvestrant (3.58 life years) and Palbociclib/Fulvestrant (3.53 life years). However, the results derived from

![img-3.jpeg](img-3.jpeg)

**Fig. 4** Life-year results within 10 years for second/further-line therapies' PFS and OS. Abbreviations: Abema, Abemaciclib; ALP, Alpelisib; CAP, Capivasertib; ENT, Entinostat; EVE, Everolimus; EXE, Exemestane; FUL, Fulvestrant; Palbo, Palbociclib; Ribo, Ribociclib

The Cox-PH model (Additional file 1: Table S9) suggested superior performance by Abemaciclib/Fulvestrant. For the mechanisms' 10-year OS (Fig. 5E,F), the combination of CDK4/6i, SERD, and ICI (5.20 life years) showed the best outcome, followed by CDK4/6i/SERD (3.58 life years), and single-agent chemotherapy (3.56 life years). The Cox-PH model displayed similar results (Additional file 2: Figure S5).

### Safety outcomes

Within the scope of first-line therapies, Letrozole consistently exhibits the lowest incidence rate for any grade AEs, grade 3–5 AEs, and AEs resulting in discontinuation. The only exception is the occurrence of AEs leading to death, where Fulvestrant has the lowest incidence rate. The highest incidence rates are observed with Palbociclib/Fulvestrant for any grade AEs, Sapitinib 40mg/Anastrozole for grade 3–5 AEs, Ribociclib/Fulvestrant for AEs leading to discontinuation, and Bevacizumab/Letrozole for AEs leading to death. Additional detailed information is available in the Additional file 1: Table S10. Regarding the mechanisms of first-line treatment strategies, AI persistently displays the lowest incidence rates for any AEs, grade 3–5 AEs, AEs leading to treatment cessation, and AEs resulting in death. The highest incidence rates for any grade AEs, grade 3–5 AEs, and AEs resulting in discontinuation are associated with CDK4/6i/SERD. However, for AEs leading to death, the highest incidence rate was observed with the combination of anti-vascular endothelial growth factor and AI. Additional detailed information is available in Fig. 6.

In terms of safety outcomes for second/further-line treatments, Everolimus presents the lowest incidence rate for any grade AEs, Fulvestrant exhibits the best performance in terms of grade 3–5 AEs, Palbociclib/Fulvestrant is optimal in minimizing AEs resulting in treatment discontinuation, and Exemestane shows the lowest rate of AEs leading to death. Conversely, Fulvestrant/Sapanisertib 4mg/day manifests the worst performance in any grade AEs, Buparlisib/Fulvestrant ranks highest in grade 3–5 AEs, Fulvestrant/Sapanisertib 30mg/week leads in AEs causing discontinuation, and Fulvestrant/Everolimus has the highest incidence rate of AEs leading to death. Additional detailed information is available in the Additional file 1: Table S11. In the context of second/further-line mechanisms, SERD demonstrates the lowest incidence rates for any grade AEs, grade 3–5 AEs, and AEs leading to treatment discontinuation. AI is associated with the lowest rate of AEs leading to death. Conversely, a combination of SERD and mammalian target of rapamycin inhibitor (mTORi) demonstrated the highest incidence rate of any grade AEs. CDK4/6i/

![img-4.jpeg](img-4.jpeg)

**Fig. 5** Life-year results within 10 years for first-line and second/further-line mechanisms' PFS and OS (**A** Extrapolation results of first-line mechanisms' PFS survival curves based on the Fractional polynomial model. **B** Extrapolation results of first-line mechanisms' OS survival curves based on the Fractional polynomial model. **C** Fractional polynomial model result for first-line mechanisms' PFS and OS. **D** Extrapolation results of second/further-lines mechanisms' PFS survival curves based on the Fractional polynomial model. **E** Extrapolation results of second/further-lines mechanisms' OS survival curves based on the Fractional polynomial model. **F** Fractional polynomial model result for second/further-line mechanisms' PFS and OS). Abbreviations: Al, Aromatase inhibitor; AKTi, AKT inhibitor; Anti-VEGF, Anti-vascular endothelial growth factor; CDK4/6i, Cyclin-dependent kinase 4 and 6 inhibitors; EGFRi: Epidermal growth factor receptor inhibitor; HDACi, Histone deacetylase inhibitor; ICI, Immune checkpoint inhibitors; mTORi, Mammalian target of rapamycin inhibitor; Pi, Protease inhibitor; PI3Ki, Phosphatidylinositol 3-kinase inhibitor; SERD, Selective estrogen receptor degrader

SERD accounted for the highest occurrence of grade 3–5 AEs. Single-agent chemotherapy was most associated with AEs leading to treatment cessation, while mTORi presented the highest incidence of AEs that resulted in death. More information is available in Fig. 6.

Additionally, it was observed that the incidence of both hematologic and non-hematologic AEs was relatively low with endocrine monotherapy. While most of CDK4/6 inhibitors were associated with an increased incidence of hematologic AEs such as neutropenia and

![img-5.jpeg](img-5.jpeg)


**Fig. 6** Safety outcomes for first-line and second/further-lines mechanisms (any grade AEs; grade 3–5 AEs; AEs leading to discontinuation; AEs leading to death). Abbreviations: AI, Aromatase inhibitor; AKTi, AKT inhibitor; Anti-VEGF, Anti-vascular endothelial growth factor; CDK4/6i, Cyclin-dependent kinase 4 and 6 inhibitors; EGFRi: Epidermal growth factor receptor inhibitor; HDACi, Histone deacetylase inhibitor; ICI, Immune checkpoint inhibitor; mTORi, Mammalian target of rapamycin inhibitor; PI, Protease inhibitor; PI3Ki, Phosphatidylinositol 3-kinase inhibitor; SERD, Selective estrogen receptor degrader

leukopenia, our analysis indicates a more varied profile for non-hematologic AEs, such as Abemaciclib showing a notable increase in events like diarrhea (Additional file 1: Table S12).

## Subgroup analysis results

The subgroup analysis revealed that in the first-line treatment, Palbociclib/Letrozole yielded the greatest PFS benefit for patients aged over 65; conversely, Abemaciclib/ Letrozole provided the most significant PFS benefit for patients under 65. For patients with visceral metastasis, the treatment yielding the best PFS benefit in the firstline setting was Abemaciclib/Letrozole, while in the second-line or further-line settings, the best PFS benefit was seen with Abemaciclib/Fulvestrant. In patients harboring mutations in Phosphatidylinositol-4,5-Bisphosphate 3-Kinase Catalytic Subunit Alpha (PIK3CA), both Capivasertib/Fulvestrant and Alpelisib/Fulvestrant regimens substantially improved the PFS. Similarly, for those with Estrogen Receptor 1 (ESR1) mutations, novel oral SERD such as Camizestrant and Elacestrant demonstrated superior PFS benefits compared to traditional SERD (Additional file 2: Figure S6). Furthermore, the incorporation of CDK4/6i into endocrine therapy appeared to yield a more substantial PFS benefit for Asian patients compared to White patients, both in the first-line and subsequent lines of treatment. Additionally, we compared the HRs for PFS and OS of FDA-approved drugs used in the first-line and second/further-line treatment of HR+/HER2-advanced breast cancer (Additional file 2: Figure S7-Figure S8). The results indicated that among FDA-approved first-line therapies, Ribociclib/Fulvestrant demonstrates the greatest patient benefit in both PFS and OS. In second/further-line treatment, Abemaciclib/Fulvestrant demonstrates superior performance in terms of OS, while single-agent chemotherapy may hold certain advantages in PFS.

Moreover, for the RCTs related to second/further-line treatments, we gathered HRs for PFS and OS from individual second and third-line treatments (Additional file 1: Table S13). Moreover, we performed an analysis using the Cox-PH model for individual second-line PFS and OS, as well as for third-line PFS. More details can be found in Additional file 1: Table S14. Limited data results demonstrate that, within the scope of second-line and subsequent treatments, the integration of various CDK4/6i with Fulvestrant significantly enhances patients' PFS and OS to diverse degrees.

## Convergence, heterogeneity, and transitivity assessment

The Gelman-Rubin method showed that the three Markov chains were stable and the inferential iterations were reproducible in all models. Overall, the results of the Q test, the I^{2} statistic, and the forest plots all indicated low heterogeneity across the specific arm. Further details are provided in Additional file 1: Table S15-Table S16. The transitivity assessment for patient baseline age, Eastern Cooperative Oncology Group score, and the proportion of the white race also demonstrated significant consistency and transitivity across the included studies (Additional file 2: Figure S9).

## Discussion

In this research, we identified 41 qualifying trials that constructed scant networks. Most of the treatments within these networks were not subjected to head-tohead trials, underscoring the value of our investigation. We compared the efficacy and safety of therapies and mechanisms in first-line and second/further-line treatment of HR+/HER2-advanced breast cancer in postmenopausal women.

Our primary findings suggest that combining CDK4/6i with ET (AI or SERD) has solidified its position in firstline treatment due to superior efficacy. Although the incidence of AEs is higher when combining CDK4/6i with endocrine therapy than with endocrine monotherapy, common CDK4/6i-related AEs like neutropenia and leukopenia are well-managed in clinical practice [94], not undermining their first-line treatment status. Subgroup analysis of first-line treatments revealed that patients under 65 years old derived more benefit from CDK4/6i combined with endocrine therapy than those over 65. Patients with visceral metastasis seemed to benefit less than the overall target population. Across different studies, the improvement trend was consistent in terms of race, with the Asian population benefiting more than the white population.

For second/further-line treatment, based on FP results, the addition of ICI to CDK4/6i combined with endocrine therapy performs well though the Cox-PH results do not align, potentially due to the inherent uncertainty in FP model extrapolation leading to unstable results. Regarding safety, endocrine monotherapy performed well. Despite PFS benefits provided by several drugs such as Sapanisertib and Buparlisib, their severe toxicity has precluded further development of these treatment plans. Subgroup analysis reveals varying degrees of PFS improvement in PIK3CA mutation patients treated with Capivasertib and Alpelisib, respectively, in combination with Fulvestrant. For ESR1 mutation patients, significant PFS improvement is observed with Camizestrant and Elacestrant monotherapy, which have been recommended in multiple guidelines and could become the new cornerstone of endocrine therapy for HR+/HER2 - breast cancer patients. The benefits for patients

with visceral metastasis are also less than the overall target population.

Clinical practice and the National Comprehensive Cancer Network (NCCN) guidelines [95] both highlight the efficacy of first-line therapies incorporating CDK4/6i. Among these, Abemaciclib/Letrozole offers the most significant enhancement in PFS for first-line patients, while Ribociclib/Fulvestrant optimizes OS. In subsequent line treatment based on CDK4/6i, Abemaciclib/Fulvestrant and Ribociclib/Fulvestrant lead in improving PFS and OS, respectively. When considering safety, Abemaciclib and Palbociclib, when added to first-line endocrine therapy, outshine other CDK4/6 inhibitors. In the subsequent line treatment, Palbociclib takes precedence. Moreover, among the recommended subsequent line treatments incorporating Everolimus with endocrine therapy, the combination of Everolimus and Exemestane exhibits marked superiority in both efficacy and safety compared to other endocrine therapy regimens.

The novel oral SERD Elacestrant has demonstrated promising results in treating breast cancer patients with resistance to endocrine therapy due to ESR1 gene mutations. Its outstanding trial outcomes have culminated in approvals from both the FDA and the European Medicines Agency [96, 97], as well as a recommendation in the most recent NCCN guidelines. Interestingly, in subgroup analysis, Camizestrant seems to surpass Elacestrant in terms of PFS. However, the evidence base for Camizestrant is limited, with only one phase II study included in the evaluation, indicating a need for further research. As for another important breast cancer mutant genotype, the PIK3CA mutation, Alpelisib/Fulvestrant is the recommended treatment according to NCCN guidelines. Alpelisib carries the distinction of being the first FDA-approved Phosphatidylinositol 3-kinase inhibitor. Significantly, Capivasertib/Fulvestrant has also shown encouraging PFS improvements and, intriguingly, Capivasertib has recently become the first FDA-approved AKT pathway inhibitor [98]. This highlights the potential of focusing on the targeted inhibition of the PI3K/AKT/ mammalian target of rapamycin signaling pathway as a promising avenue for advancing future breast cancer therapies.

Numerous systematic reviews and NMA of HR+/HER2 - advanced breast cancer have been published in recent years. Laura A. Huppert [4] provided a comprehensive analysis of systemic treatments for both early and metastatic HR+/HER2 - breast cancer, summarizing critical clinical data and exploring its influence on clinical practice. In May 2023, ESMO introduced an online guideline for metastatic breast cancer [99], incorporating all eligible HR+/HER2 - advanced patients into the first-line treatment scope with CDK4/6i. Upon CDK4/6i progression, alternative treatments, including Everolimus/Exemestane, CDK4/6i combinations with endocrine therapy, single-agent Fulvestrant, alpelisib for patients with PIK3CA mutations, Elacestrant for those with ESR1 mutations, are considered. Concurrently, a multitude of meta-analyses assessing the safety and efficacy of HR+/HER2 - advanced breast cancer treatment regimens have been published. All showing that the addition of CDK4/6i to endocrine therapy improves patient prognosis [9, 10, 13, 100-103]. In addition, sacituzumab govitecanhziy has been approved by the FDA for the treatment of HR+/HER2 - advanced breast cancer patients who have previously undergone endocrine-based treatments and at least two other therapeutic regimens [104]. Additionally, emerging targeted therapies such as ICI and Antibodydrug Conjugates offer potential new choices for future breast cancer treatment strategies [105, 106].

Initially, we considered both PH and Non-PH model with time-varying HRs and used life years gain as a measure of efficacy. This approach allowed for a clearer comparison of the survival benefits offered by different interventions. Furthermore, we extrapolated survival curves for different interventions based on their mechanisms, to predict long-term outcomes. This significant aspect, overlooked in previous network metaanalysis studies, augments the comprehensiveness of our research. Finally, we also classified the mechanisms of the interventions and compared the efficacy and safety of the different mechanisms, providing a reference for clinical use and new drug development.

To our knowledge, this research is the first to compare the outcomes of currently available first-line and second/ further-line treatments for patients with advanced HR+/HER2 - postmenopausal women with advanced breast cancer. As a timely network meta-analysis, we used the most updated data and addressed the study's relevant significance by making recommendations on treatment choices based on our analysis and the clinical point of view. We used FP models to model the long-term treatment effects of treatment options. In RCTs, it is not possible to accurately estimate the benefit of OS due to the limited follow-up time. The approach used in our study can address this data gap. The results of our study will enable clinicians and patients to determine the survival benefits of emerging treatments and select the best treatment. The results of our subgroup analysis can also help physicians tailor precise treatment regimens for patients of different ages and with different tumor metastatic statuses. Our robust methodology and aggregation mean that our results are reliable and relevant to clinical practice.

However, our research also has certain limitations. First, the biases of different baselines in clinical trials

cannot be ignored, and different baseline characteristics and clinical staging may lead to a lack of comparability of data. Second, indirect comparisons increase variance, which may lead to non-significant treatment effects or even eliminate differences between studies. In this network meta-analysis, we did not include clinical trials that were outmoded (such as trials with patients of unknown status such as HER2 and HR). We separately extracted first-line and second/further-lines metrics (such as HRs of PFS and OS) from the trials. Furthermore, when a subset of postmenopausal patients was included in larger RCTs (peri-menopausal or premenopausal patients accounted for less than 20%), data for HR+/HER2- patients were separately extracted. Sensitivity analysis was conducted excluding these RCTs to ensure result stability. Despite slight variations in the FP model results (Additional file 2: Figure S10), the overall mechanism ranking remained fundamentally consistent, thereby validating the reliability of the study outcomes. Additionally, in the execution of network meta-analysis, frequency models were utilized for time-to-event data outcomes, while Bayesian models were employed for binary outcomes [14, 107]. No significant differences were discerned in the statistical analysis results between these two approaches. However, this inevitably introduces some heterogeneity and bias into the results. Finally, we did not take into account the frontline treatment status of patients undergoing second/further-line therapy, as patients exhibit variability in their resistance or treatment uptake, which could lead to potential survival bias. Therefore, comparisons of treatment regimens after first-line progression may be subject to certain biases due to the inconsistent baseline medication used by frontline patients. RCTs that devise sequential treatment regimens, such as the SONIA study [108], are worth our attention.

## Conclusions

In conclusion, our NMA demonstrated that the combination of CDK4/6i and ET exhibits superior efficacy in first-line treatment, albeit at the expense of increased adverse events. Notably, enhanced benefits were observed in patients under 65 and within the Asian demographic. The combination of CDK4/6i and SERD displayed remarkable efficacy in second/further-line treatment, and the addition of ICI might enhance this efficacy, notwithstanding discrepancies in the Cox-PH model results. Furthermore, while there are PFS benefits associated with drugs such as Sapanisertib and Buparlisib, their development is hindered by toxicity. Noteworthy PFS improvements were observed in PIK3CA and ESR1 mutation patients treated with Capivasertib, Alpelisib, Camizestrant, and Elacestrant. Further research is necessary to determine the most effective treatment strategies in the HR+/HER2- advanced breast cancer, and sequencing of these therapies is crucial. Additionally, more trials comparing these novel treatments are warranted to reduce uncertainty in these results.

## Abbreviations

AEs Adverse events
AI Aromatase inhibitor
CDK4/6i Cyclin-dependent kinase 4 and 6 inhibitor
Cox-PH Cox's proportional hazards
ESR1 Estrogen receptor 1
ET Endocrine therapy
FDA Food and Drug Administration
FP Fractional polynomial
HER2 Human epidermal growth factor receptor 2
HR Hormone receptor
HRs Hazard ratios
ICI Immune checkpoint inhibitor
mTORi Mammalian target of rapamycin inhibitor
NCCN National Comprehensive Cancer Network
NMA Network meta-analysis
OS Overall survival
PFS Progression-free survival
PH Proportional hazards
PIK3CA Phosphatidylinositol-4,5-Bisphosphate 3-Kinase Catalytic Subunit Alpha
RCTs Randomized clinical trials
SERD Selective estrogen receptor degrader

## Supplementary Information

The online version contains supplementary material available at https://doi. org/10.1186/s12916-023-03238-2.

Additional file 1: Table S1. PRISMA checklist. Table S2. Search strategies. Table S3. Constant proportional risk test (probability) for Kaplan-Meier curves. Table S4. Baseline characteristics of included studies. Table S5. Summary of adverse events in RCTs across various dimensions. Table S6. List of drugs approved by the Food and Drug Administration. Table S7. Akaike Information Criterion value for survival curves from Fractional Polynomial models. Table S8. Cox-PH model analysis: Hazard ratios for PFS in first-line therapies. Table S9. Hazard ratios for PFS and OS in second/ further-lines therapies: Cox-PH model analysis. Table S10. Comparison of adverse events for first-line therapies. Table S11. Comparison of adverse events for second/further-lines therapies. Table S12. Summary of hematologic and non-hematologic adverse events in RCTs. Table S13. Summary of Hazard ratios for post-line RCTs' PFS and OS. Table S14. Hazard ratios for second-line OS and PFS, and third-line PFS from Cox-PH model analysis. Table S15. Convergence and heterogeneity assessment. Table S16. Heterogeneity assessment information.
Additional file 2: Figure S1. Methodology quality of the included studies. Figure S2. Funnel plots to detect the publication bias of included studies. Figure S3. Extrapolation results of therapies' survival curves based on the Fractional Polynomial model. Figure S4. Hazard ratios for PFS and OS from Cox-PH model analysis of first-line mechanisms. Figure S5. Hazard ratios for PFS and OS from Cox-PH model analysis of second/ further-lines mechanisms. Figure S6. Subgroup analysis of Cox-PH model results in first-line and second/further-lines therapies. Figure S7. Hazard ratios for PFS and OS from Cox-PH model analysis of FDA-approved first-line therapies. Figure S8. Hazard Ratios for PFS and OS from Cox-PH model analysis of FDA-approved second/further-lines therapies. Figure S9. Transitivity assessment. Figure S10. Sensitivity analysis of patients with full menopause.

## Acknowledgements

Not applicable.

## Authors' contributions

All authors contributed to this manuscript. WT, HS, and MZ had full access to all data in the study and took responsibility for the integrity of the data and the accuracy of the data analysis. HS and MZ contributed equally to this work. Conceptualization and design were carried out by WT, HS, and MZ; data acquisition was done by HS and MZ; HS and MZ also handled the analysis and interpretation of data. The manuscript was initially drafted by HS, and critically revised by WT, with insightful intellectual contributions from GY, A-JG, and DZ. Statistical analysis was conducted by SH and MZ. Funding was obtained by WT and GY. WT and GY provided administrative and technical support, as well as the study's supervision. All authors have read and given their approval to the final version of the manuscript.

## Funding

This work was supported by the General Program of National Natural Science Foundation of China (grant no. 72174207) and Jiangsu Provincial Natural Science Fund for Distinguished Young Scholars (BK20200005).

## Availability of data and materials

The data used in this study are derived from published studies, and the original datasets can be accessed by reviewing the relevant literature. Furthermore, the datasets supporting the outcomes of this research and the R software code can be obtained from the corresponding author via email.

## Declarations

## Ethics approval and consent to participate

Not applicable.

## Consent for publication

All authors agreed to the publication of this manuscript.

## Competing interests

The authors declare that they have no competing interests.

## Author details

${ }^{1}$ School of International Pharmaceutical Business, China Pharmaceutical University, Nanjing, Jiangsu, China. ${ }^{2}$ Center for Pharmacoeconomics and Outcomes Research \& Department of Public Affairs Management, School of International Pharmaceutical Business, China Pharmaceutical University, Nanjing, Jiangsu, China. ${ }^{3}$ Department of Rehabilitation Medicine, West China Hospital, Sichuan University, Sichuan, China. ${ }^{4}$ School of Basic Medicine and Clinical Pharmacy, China Pharmaceutical University, Nanjing, Jiangsu, China.

## Received: 18 May 2023 Accepted: 19 December 2023 Published online: 12 January 2024

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Ready to submit your research? Choose BMC and benefit from:

- fast, convenient online submission
- thorough peer review by experienced researchers in your field
- rapid publication on acceptance
- support for research data, including large and complex data types
- gold Open Access which fosters wider collaboration and increased citations
- maximum visibility for your research: over 100M website views per year

At BMC, research is always in progress.
Learn more biomedcentral.com/submissions