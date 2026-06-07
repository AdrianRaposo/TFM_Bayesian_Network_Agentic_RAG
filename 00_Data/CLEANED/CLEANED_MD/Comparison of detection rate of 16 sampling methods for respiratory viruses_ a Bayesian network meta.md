# BMJ Global Health 

## Comparison of detection rate of 16 sampling methods for respiratory viruses: a Bayesian network metaanalysis of clinical data and systematic review

Nianzong Hou, ${ }^{1}$ Kai Wang, ${ }^{2}$ Haiyang Zhang, ${ }^{1}$ Mingjian Bai, ${ }^{3}$ Hao Chen, ${ }^{4}$ Weidong Song, ${ }^{5}$ Fusen Jia, ${ }^{1}$ Yi Zhang, ${ }^{1}$ Shiliang Han, ${ }^{1}$ Bing Xie ${ }^{1}$

To cite: Hou N, Wang K, Zhang H, et al. Comparison of detection rate of 16 sampling methods for respiratory viruses: a Bayesian network meta-analysis of clinical data and systematic review. BMJ Global Health 2020;5:e003053. doi:10.1136/ bmjgh-2020-003053

Handling editor Alberto L Garcia-Basteiro

- Additional material is published online only. To view, please visit the journal online (http://dx.doi.org/10.1136/ bmjgh-2020-003053).

NH and KW contributed equally.
NH and KW are joint first authors.

Received 1 June 2020
Revised 18 September 2020
Accepted 14 October 2020
(A) Check for updates
(C) Author(s) (or their employer(s)) 2020. Re-use permitted under CC BY-NC. No commercial re-use. See rights and permissions. Published by BMJ.
For numbered affiliations see end of article.

## Correspondence to

Professor Bing Xie; xiebingshouzuwaike@163.com, Dr Kai Wang; wangkaiicu@163.com and Dr Nianzong Hou; hounianzong@163.com

## ABSTRACT

Background Respiratory viruses (RVs) is a common cause of illness in people of all ages, at present, different types of sampling methods are available for respiratory viral diagnosis. However, the diversity of available sampling methods and the limited direct comparisons in randomised controlled trials (RCTs) make decision-making difficult. We did a network meta-analysis, which accounted for both direct and indirect comparisons, to determine the detection rate of different sampling methods for RVs.
Methods Relevant articles were retrieved comprehensively by searching the online databases of PubMed, Embase and Cochrane published before 25 March 2020. With the help of R V.3.6.3 software and 'GeMTC V.0.8.2' package, network meta-analysis was performed within a Bayesian framework. Node-splitting method and $I^{2}$ test combined leverage graphs and Gelman-Rubin-Brooks plots were conducted to evaluate the model's accuracy. The rank probabilities in direct and cumulative rank plots were also incorporated to rank the corresponding sampling methods for overall and specific virus.
Results 16 sampling methods with 54438 samples from 57 literatures were ultimately involved in this study. The model indicated good consistency and convergence but high heterogeneity, hence, random-effect analysis was applied. The top three sampling methods for RVs were nasopharyngeal wash (NPW), mid-turbinate swab (MTS) and nasopharyngeal swab (NPS). Despite certain differences, the results of virus-specific subanalysis were basically consistent with RVs: MTS, NPW and NPS for influenza; MTS, NPS and NPW for influenza-a and b; saliva, NPW and NPS for rhinovirus and parainfluenza; NPW, MTS and nasopharyngeal aspirate for respiratory syncytial virus; saliva, NPW and MTS for adenovirus and sputum; MTS and NPS for coronavirus.
Conclusion This network meta-analysis provides supporting evidences that NPW, MTS and NPS have higher diagnostic value regarding RVs infection, moreover, particular preferred methods should be considered in terms of specific virus pandemic. Of course, subsequent RCTs with larger samples are required to validate our findings.

## Key questions

## What is already known?

- The identification of respiratory viruses (RVs) in patient samples is highly dependent on the sampling methods of the clinical specimen.
- The diversity of available sampling methods and the limited direct comparisons in randomised controlled trials make decision-making difficult.


## What are the new findings?

- Nasopharyngeal wash, mid-turbinate swab (MTS) and nasopharyngeal swabs had higher diagnostic value regarding RVs infection, but MTS showed its superiority at the positive rate, less discomfort and easy to operate.
- Particular preferred sampling methods should be considered in case of one specific virus outbreak.
- Sputum ranks the first in terms of common coronaviruses detection, which may demonstrate that the pathophysiology and pathogenic mechanisms of COVID-19 is similar to common coronaviruses and it was easily to infect via the sputum.


## What do the new findings imply?

- Every sampling method has their own advantages and disadvantages.
- Taking positive rate, less discomfort and cost into account, MTS might be the best choice for the diagnosis of RVs infection.
- Because of different pathophysiology and pathogenic mechanisms, particular sampling methods should be considered in case of one specific virus outbreak.
- For common coronaviruses, sputum resulted in significantly higher detection rates, which may be applied to COVID-19.


## INTRODUCTION

Respiratory viruses (RVs), account for approximately $80 \%$ of acute respiratory diseases, are among the most important human pathogens contributing to the significant mortality and

morbidity worldwide.1 Non-specific symptoms including fever, headache, cough or sore throat make it difficult to differentiate these viruses.2 Specimen collection before transported to laboratory/test is the first important pillar for the rapid and accurate diagnosis of respiratory viral infections. Indeed, the identification of RVs in patients' samples is highly dependent on the sampling methods of the clinical specimen.3

Currently, ciliated epithelial cells or cell-free viruses have been collected from nasal,4--6 throat,7 8 mid-turbinate,1 9 10 nose--throat,11 12 oropharyngeal13--16 and nasopharyngeal swabs17--19 (NS/TS/MTS/N--TS/OPS/NPS); nasal19 20 and nasopharyngeal aspirates12 21 22 (NA/NPA); nasal23 24 and nasopharyngeal wash25--27 (NW/NPW); nasal brush (NB)20 28and/or saliva,29--31 sputum,32--34 bronchoalveolar lavage (BAL),35 swab36 37 or aspirate38 39 with viral transport medium (VTM-S/VTM-A). Choosing the highest yield in a least invasive manner has always been central to the practice of medicine. The gold standard for RVs testing is the NPS collected by a healthcare worker.1 However, one of the shortcomings of the use of NPS is that it is obtained not as easily as other types of specimens, such as NS, MTS, saliva and sputum, which may result in a suboptimal specimen, particularly if obtained by the inexperienced personnel.30 Moreover, the procedure for obtaining an NPS could cause coughing in most patients which inevitably increases the risk of nosocomial spread of RVs.40 In addition, based on the results of several studies,1 4 13 14 30 35 41 42 other sampling methods with superior sensitivity have generally been considered as the specimen choices for RVs identification. NPS and other types of specimens, as samples for RVs detection, have been compared between some of them directly or indirectly in several studies,1 4 6 13 14 17 18 26 29 30 33 35 41--47 however, at present, there is still a lack of comprehensive researches as far as the actual evaluation for the RVs detection with different sampling methods. As a powerful and useful approach to combine both direct and indirect evidences,48 Bayesian network meta-analysis is conducted to provide a hierarchy for the detection with different types of specimen. The purpose of this study was anticipated to assess the comparability of these sampling methods for RVs and specific virus detection which combined with reverse transcription (RT)-PCR and/or virus culture/immunofluorescent antibody (IFA)/ELISA and so on. and provide a clinically useful summary that can guide clinical work.

## METHODS

Our meta-analysis was arranged in line with PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines49 and its extension statement for network meta-analyses.50

### Data source, search strategy and inclusion/exclusion criteria

Network meta-analysis was performed and relative data were searched by using the PubMed, Embase and the Cochrane. The publication date was set from the beginning of this investigation up until 25 March 2020, and the language was restricted to English. Through all fields of advanced, we used the following search terms or keywords alone or in combination: “Respiratory Viruses”, “Influenza”, “SARS”, “MERS”, “2019nCoV”, “Swab*”, “Sputum”, “Saliva”, “Aspirate”, “Wash”, “Brush”, “Serum”, “Blood”, “Plasma”, of which strategies were mainly divided into two parts (respiratory viral infection and different sampling methods).

We manually reviewed the titles and abstracts to select the potential articles systematically and comprehensively. Then we carefully read the full texts and selected suitable articles. Finally, we included all comparative trials or cohort studies comparing the detection of one sampling method with others for patients with respiratory illness. To minimise article omissions, the reference lists of relevant studies were also manually screened for additional publications, what is more, combination and short reports were also included. The samples were all from patients of all ages with a diagnosis of respiratory tract infection. Case reports, duplicated data, no control group, without or with wrong data analysis methods, inconsistent data, reviews, unpublished literature, conference papers, studies without adequate information were excluded in the present network meta-analysis. The PRISMA flow chart was shown in figure 1.

### Data extraction and study quality assessment

Two researchers independently screened the articles in accordance with the above-mentioned criteria. One reviewer checked the original data extraction of these studies and extracted additional data where necessary,

and then another reviewer checked all data. Any disagreements were resolved by discussion and, if necessary, with the involvement of a fifth reviewer. We extracted descriptive statistics of population characteristics across all eligible trials and studies, such as the following variables: author, date, country, age, gender, number of patients, number of positive samples, hospital, sampling time, target virus, sampling methods, diagnosis of enrolled patients, detective rates, sample ranking and references. The bias risk of eligible comparative trials (CTs) and cohort studies (CSs) were assessed by Newcastle-Ottawa Scale (NOS). ${ }^{51}$ The following terms were used in NOS for assessing risk of bias: patient selection, comparability between groups and objectivity of results. If scored $\geq 5$, the CTs and CSs were considered moderate or high quality. On the contrary, they were considered as low quality, if it scored $<5$ and subsequently excluded from our meta-analysis.

## Statistical analysis

We used R (V.3.6.3) and package of GeMTC (V.0.8.2) to perform our Bayesian network meta-analysis. The inconsistency of the model was assessed according to the nodesplitting method and the Bayesian p value, in which $p<0.5$ is considered as the existence of significant inconsistency. Heterogeneity variance parameter $I^{2}$ test was analysed to assess the heterogeneity of the model, in which the heterogeneity between studies was assessed as high if $I^{2}$ $>50 \%$ and the random-effects model was used, on the contrary, the heterogeneity between studies was assessed as low and the fixed effects mode was used. Furthermore, the model convergence was accessed by convergence plots (Gelman-Rubin-Brooks plots), ${ }^{52}$ and the model fitting effect was assessed by leverage graph. Afterwards, detection rate was analysed using the OR with its $95 \%$ credible interval (CrI), which were calculated by Markov chain Monte Carlo methods. Ultimately, the rank probabilities would be calculated to obtain the hierarchy of each sampling method. From the direct and cumulative rank plots based on the rank probabilities provided by the 'GeMTC' package, we could easily find the ranking of each sampling method and the proportion of each ranking, and make the choice which sampling methods could be best, second and so on. We also performed additional network meta-analyses in eight subgroups of studies: subgroup 1 with different sampling methods for influenza virus (INF), 2 for influenza-a (INFa), 3 for influenza-b (INFb), 4 for rhinovirus (RV), 5 for respiratory syncytial virus (RSV), 6 for parainfluenza virus (PIV), 7 for adenovirus (ADV) and 8 for coronavirus (COV).

## Patient and public involvement

This research was done without patient or public involvement.

## RESULTS

## Identification

We retrieved 37 439, 22313 and 13322 related studies through the PubMed, Embase and the Cochrane Library,
respectively. After excluding duplicate articles through EndNote software, we read titles, abstract and the full text, and then, excluded 47154 articles. A total of 57 eligible literatures, including 54438 samples and mentioning the comparison of different sampling methods for RVs detection, were finally screened. This study covered 16 sampling methods: NPS, MTS, OPS, NS, TS, N-TS, NPA, NPW, NA, NW, NB, saliva, sputum, BAL, VTM-S and VTM-A. The detailed characteristics of eligible studies were shown in online supplemental table 1.

## Quality assessment

All 57 CTs or CSs were performed the quality assessment using the NOS. All the studies included had obvious bias in the item of 'follow-up long enough for outcomes to occur', but were all scored $\geq 5$ and have considerable quality. There was a relative high risk of bias in the studies of Ngaosuwankul et al, ${ }^{5}$ Goyal et al, ${ }^{17}$ Masters et al, ${ }^{25}$ Yoshii et al, ${ }^{32}$ Miró-Cañés et al ${ }^{24}$ and Walsh et al, ${ }^{38}$ which were scored 5; in other words, most of the studies were considered to be of high quality. The summary and figures of risk of bias about the eligible studies were shown in online supplemental tables 1 and 2.

## Evidence network

In terms of detection rate of viruses, we can make the indication that different sampling methods were used by a relatively large number of patients. The network structure diagrams, presenting the direct association between different sampling methods, were displayed in figure 2.

## Inconsistency and heterogeneity test

The OR with $95 \% \mathrm{CrI}$ and p value (indirect) of consistency test based on detection rate for RVs and specific viruses proved the consistency of the network to be satisfactory, and we found no significant inconsistency or qualitative difference available in the outcomes (online supplemental table 3). In addition, the Gelman-RubinBrooks plots (online supplemental figure 1) showed the analyses achieve good convergence efficiency, and the leverage graphs (figure 3) reflect well-fitted models, all of which mean that no inconsistency between direct and indirect evidences was significant and the data were steady.

The results of the heterogeneity test were shown in online supplemental table 4. As shown in this table, the tests of heterogeneity in this study were generally covering low, moderate and high degree, and then because the $I^{2}$ of more than half of the comparisons was $>50$, the heterogeneity between studies was assessed as high and the random-effects model was used within a Bayesian framework.

## Network meta-analyses

The results of these network meta-analyses were demonstrated in league table (online supplemental table 5). The results of lower left triangle were displayed as the ratio of the $X$ axis versus $Y$ axis and the upper right triangle as the ratio of the $Y$ axis versus $X$ axis. The results were

![img-0.jpeg](img-0.jpeg)

Figure 2 Network of the comparisons for the Bayesian network meta-analysis. Network of detection for respiratory viruses (a), influenza (b), influenza-a (c), influenza-b (d), rhinovirus (e), respiratory syncytial virus (f), parainfluenza virus (g), adenovirus (h) and coronavirus (i). A, nasopharyngeal swab; B, saliva; C, mid-turbinate swab; D, nasal swab; E, sputum; F, nasopharyngeal aspirate; G, bronchoalveolar lavage; H, oropharyngeal swab; I, nasopharyngeal wash; J, throat swab; K, nose-throat swab; L, nasopharyngeal wash; M, viral transport medium (VTM)-swab; N, VTM-aspirate; O, nasal aspirate; P, nasal brush.
deemed as statistical significant if it did not include value 1. As shown in this table, there were significant differences for RVs and specific viruses detection in nearly half of comparisons when these sampling methods were compared with each other.

## Rank probabilities

The detailed rankings of different sampling strategies were presented in ranking table (online supplemental table 6). Based on it, direct and cumulative rank plots of the probability for the detection of RVs and specific viruses (figure 4) were established, from which we could easily find the ranking and the proportion of each sampling strategy. At last, we summarised the detection rank in table 1, allowing a more intuitive way to understand the rank probabilities of different sampling methods for RVs and specific viruses.

## DISCUSSION

RVs are a common cause of respiratory infections each year during respiratory illness seasons, which lead to more poorer prognosis, especially the children, the elderly and those with compromised immune systems resulting from other diseases. ${ }^{33}$ Different sample collection techniques, including NPS, MTS, OPS, TS, N-TS, NPA, NPW, NA,

NW, NB, BAL, VTM-S, VTM-A, saliva and sputum specimens, are available for detecting RVs and help distinguish these viruses such as INF, RSV, ADV, PIV and so on, combining with RT-PCR, and/or viral culture/antigen test/enzyme immunoassay/ELISA and so on. Faced with so many sampling methods and a variety of conflicting conclusions of different CTs and CSs, both clinicians and patients felt confused and the ideal sampling method remained to be completely identified. Although there is an abundant of data available on the comparison of some of these sampling methods, it was observed that the literatures of direct comparisons are limited and there are no guidelines which usually attempted to rank the detection rate of these methods. As we knew, when direct comparisons were unavailable, the existence of a Bayesian network meta-analysis could allow the investigators to overcome the limitation of traditional meta-analysis and gain their efficiency or accuracy indirectly. ${ }^{48}$ Therefore, we conducted a Bayesian network meta-analysis to comprehensively evaluate the detection rate of different sampling methods for patients and want to provide some references for clinical work. A total of 54438 samples from 57 studies were ultimately involved in our study. As illustrated by the rank probabilities, NPW, MTS and NPS were among the three best sampling methods, whereas, NW, NS, NPA, NA, N-TS, OPS, sputum, VTM-S, TS, saliva, VTM-A, NB and BAL were among the relatively inferior specimens. As far as we know, this is the first and largest network meta-analysis considering the detection rate of different sampling methods with a large scale of samples involved in the analysis. According to the inconsistency test within node-splitting method, Gelman-Rubin-Brooks plots and the leverage graphs, there were little inconsistency and good convergence efficiency between direct and indirect evidence, all of which suggesting well-fitted models and y reliable results provided by us.

These sampling methods can be divided into invasive, less invasive and non-invasive specimens. There is a traditional concept that the more invasive the respiratory specimen, the more likely a positive result. ${ }^{12}$ However, with the development of specimen collection, less invasive methods may be acceptable in the era of molecular testing. ${ }^{6}$ The use of multiple sampling methods is necessarily beneficial for maximal detection of viral infections but inevitably increases cost and wastes medical resource, and there is not a clear-cut answer to evaluate the marginal effects. ${ }^{1454}$

Obviously, NPW, NW, NPA, NA and BAL belong to invasive specimens. It is not surprising that NPW ranks the first at the detection of RVs, because the volume of saline used in NPW collection procedures is usually sufficient. ${ }^{27}$ Nevertheless, NPW is difficult to perform and inevitably causes patients discomfort for the need of a small feeding tube and a syringe for suction, thus it is not routinely performed in some institutions. ${ }^{25} 42$ NW is akin to NPW, but has a lower detection rate and poses a risk of aspiration. ${ }^{45}$ NPA was generally thought to be the optimal specimen for some time, however, this

![img-1.jpeg](img-1.jpeg)

Figure 3 The leverage graphs reflect the model is well fitted with all the arms under the curve. The leverage graph for RVs (A), INF (B), INFa (C), INFb (D), RV (E), RSV (F), PIV (G), ADV (H) and COV (I). ADV, adenovirus; COV, coronavirus; INF, influenza virus; INFa, influenza-a; INFb, influenza-b; PIV, parainfluenza virus; RSV, respiratory syncytial virus; RV, rhinovirus; RVs, respiratory viruses.
may not be applicable for all medical establishments, because liquid aspirates are cumbersome, collections of NPA require suitable suction devices, highly trained personnel are needed and may present more infectious risk to healthcare workers. ${ }^{420} 40{ }^{53}$ NA has an advantage in collection of nasal secretions for viral testing and this technique performed similarly to NPA, but the unpleasant experience with lower sensitivity made it not a better choice. ${ }^{192927}$ BAL specimen is in essence both an upper and a lower airway mixed sample, yet, it was a more invasive procedure and unlikely to provide additional information if other sampling methods are positive. ${ }^{143653}$
MTS, NPS, NS, N-TS, OPS, VTM-S, TS and NB were considered to be the less invasive specimens. NPS collected by a healthcare worker has been considered as a gold standard technique for the diagnosis of RVs and shows excellent sensitivity in the study and other articles. Although NPS may be less invasive than NPW to some extent, it could cause a great amount of distress and coughing to patients, which may increase the risk of nosocomial spread of RVs. ${ }^{3040}$ MTS is recommended as
the most effective alternative to NPS for detection of RVs due to its ease of collection, possible self-collection by patients and higher diagnostic rate. ${ }^{18}$ Since the discomfort increased significantly with depth of swab sampling, the discomfort associated with the MTS was more similar to that of the superficial NS but less than to the deep NPS. ${ }^{4}$ NS collected in the nasal vestibules ranks at the fifth in the detection of RVs and causes little discomfort, however, the sensitivity of this specimen type was too low to reliably rule out infection in some situations. ${ }^{440}$ OPS, as a valuable clinical tool, is relatively easier to obtain but inferior to NPS and produces lower sensitivities as a specimen for RVs detection. ${ }^{1316}$ Obtaining a TS specimen is less likely to precipitate coughing, unfortunately, the incremental benefit for viral detection with the TS is modest, which suggests that it may have value as a supplementary test. ${ }^{81930}{ }^{31} \mathrm{~N}-\mathrm{TS}$ is minimally invasive and non-healthcare workers with simple training can collect this specimen. N-TS has been shown to have a sensitivity comparable to that of NS for RVs detection, however, N-TS alone would not be adequate for RVs

![img-2.jpeg](img-2.jpeg)

Figure 4 Direct and cumulative rank plots of the probability for the detection of RVs (A), INF (B), INFa (C), INFb (D), RV (E), RSV (F), PIV (G), ADV (H) and COV (I). ADV, adenovirus; BAL, bronchoalveolar lavage; COV, coronavirus; INF, influenza virus; INFa, influenza-a; INFb, influenza-b; MTS, mid-turbinate swab; NA, nasal aspirate; NB, nasal brush; NPA, nasopharyngeal aspirate; NPS, nasopharyngeal swab; NPW, nasopharyngeal wash; NS, nasal swab; N-TS, nose-throat swab; NW, nasal wash; OPS, oropharyngeal swab; PIV, parainfluenza virus; RSV, respiratory syncytial virus; RV, rhinovirus; RVs, respiratory viruses; TS, throat swab; VTM, viral transport medium.
surveillance according to some studies. ${ }^{1112} \mathrm{NB}$ is a useful supplement for RVs detection but produces a lower rate of viral detection and demonstrates a higher level of patient discomfort. ${ }^{14}$ VTM is used to preserve the collections when they are transported to the lab and testing,
which could increase the cost of consumables, storage requirements and risk of leakage during transportation, what is more, VTM-S and VTM-A did not seem to be related to high quality of specimen or improve the detection rate. ${ }^{363853}$

Table 1 Summary of the detection ranks for different viruses


ADV, adenovirus; BAL, bronchoalveolar lavage; COV, coronavirus; INF, influenza virus; INFa, influenza a; INFb, influenza b; MTS, mid-turbinate swab; NA, Nasal aspirate; NA, Not applicable; NB, nasal brush; NPA, nasopharyngeal aspirate; NPS, nasopharyngeal swabs; NPW, nasopharyngeal wash; NS, nasal swab; N-TS, nose-throat swab; OPS, oropharyngeal swab; PIV, parainfluenza virus; RSV, respiratory syncytial virus; RV, rhinovirus; RVs, respiratory viruses; TS, throat swab; VTM-A, aspirate with viral transport medium; VTM-S, swab with viral transport medium.

Sputum and saliva testings are non-invasive techniques and could dramatically reduce anxiety and discomfort, which may simplify the collection for monitoring RVs of populations over time. ${ }^{31}$ Sputum showed significantly higher detection rates for most types of viruses, and it might be one reliable specimen for RVs detection if other samples are not available. ${ }^{40}$ However, the use of sputum has some limitations. First, sputum is secreted from lower respiratory tract and good-quality sputum is often difficult to obtain which is easily contaminated by upper respiratory secretions. ${ }^{6}$ Second, because of the viscosity of sputum, it requires an additional pretreatment procedure and some young children or the elderly cannot produce sputum. ${ }^{40}$ It is very likely that RVs are secreted via the salivary glands, ${ }^{31}$ thus, saliva is worth testing in the airborne viral infections. Saliva is not widely accepted for the diagnosis of RVs infection for it may not be expected to have high viral concentrations and it is difficult to distinguish the difference between saliva and sputum. ${ }^{20}$

As far as the results of subgroups network meta-analysis, there were also several important findings. First, the results of virus-specific subanalyses were basically consistent with RVs: the top three sampling methods for INF were MTS, NPW and NPS; for INFa and b were MTS, NPS and NPW; for RV and PIV were saliva, NPW and NPS; for RSV were NPW, MTS and NPA; for ADV were saliva, NPW and MTS; and for COV were sputum, MTS and NPS. These differences of detection for sampling methods during RVs and specific viruses may be mainly attributed to that different viruses may have different viral loads in different respiratory mucosa. ${ }^{55}$ Second, the first three sampling methods were not in complete agreement between INF and INFa/b. This result may be explained by the fact that the three subgroups of INF confound several subtypes of INFa such as H1N1, H3N2, H5N1 and so on. ${ }^{518}$ The subtle differences in detection may indicate that the physiological and pathological characterisations are different among INF. ${ }^{56}$ Third, the detection rate of RV and PIV from saliva is higher than NPW and NPS. This brings an incredible result because RV and PIV infection begins in the nasopharynx and destructs the airway epithelial cells, but not many viruses survive in saliva. One possible explanation is the saliva specimen was dirtied by respiratory secretions caused by these two types of viruses and this procedure is analogous to NPW. Another explanation with more probability is that unknown confounding bias in statistical analysis distorts the ranks. Even so, as a source of markers for infectious disorders and viruses could survive in evaporated saliva microdroplets, ${ }^{57}$ the diagnostic value of saliva for RV/PIV should be paid close attention to. Fourth, NPA ranked third in detection of RSV, just after NPW and MTS. Although RSV usually causes lung infection, this demonstrated that NPA, conducted with deep nasal wall suction from one nostril, was most likely to collect adequate viruses from respiratory secretions for test. ${ }^{1222}$ Fifth, saliva is also the first choice to detect ADV, which may be used to confirm that one major replication site of ADV is salivary glands

but not the respiratory epithelium. ${ }^{18}$ Sixth, sputum ranks the first in terms of common COV detection. According to the current situation-the outbreak of the pandemic COVID-19 posing a major challenge to global health services and clinicians, ${ }^{58-65}$ this result in our study had its own rationality and practical significance. In view of one recent systematic review supporting that sputum is the most valuable method in COVID-19 diagnosis, ${ }^{64}$ our finding may cautiously demonstrate that the pathophysiology mechanism of COVID-19 is similar to common COV and it is easily to infect via the sputum.

Our findings are consistent with the most clinical trials included either in the outcome of the network metaanalysis or in the rank probabilities, especially the trials with a large sample size or high scores in NOS. Twenty-two ${ }^{145781214-161920232530-32435465-68}$ studies found that one sampling method is sensitive for the diagnosis of RVs than the other, of which these comparisons are in accordance to our rank possibilities. The study by Ye and Wang ${ }^{67}$ reported epidemiological data on the prevalence of RVs in a large tertiary care children's hospital with 34961 samples and summarised that the detection rate of sputum is higher than TS. The study by Frazee et al ${ }^{4}$ and Larios et al ${ }^{1}$ summarised MTS higher than NPS, the study by Lieberman et al ${ }^{14}$ reported NPW higher than NPS and the study by Yoshii et al ${ }^{52}$ showed NPS higher than sputum. Not exactly to the RVs detection ranks, but the results of Stensballe et al ${ }^{35}$ and Macfarlane et al ${ }^{68}$ showed consistence based on subgroup analysis of RSV. No significant differences for viruses detection when different sampling methods compared with the others were found in 21 studies, ${ }^{369} 9101718212224282933363739404244454769$ but nearly half of the actual detection rates supported our rank possibilities. ${ }^{369} 21242833464769$ Results of comparison in other $12^{21113273538414670-73}$ studies were inconsistent to our rank possibilities, however, some of these studies have small sample size ${ }^{7173}$ or focused on the discomfort associated with the sampling methods or a particular virus ${ }^{1127}$ or were partial consistent with the RVs detection ranks. ${ }^{22735}$ The last two studies belonged to CSs without clear result of comparison. ${ }^{6674}$

The strength of this study was mainly that it was the first time for us to put forward the hierarchy of different sampling methods, which could guide the clinical work. What is more, there are also some other particular advantages about our network meta-analysis. First, a wide range of search strategy was used to minimise the possibility of publication bias. Second, the model in our study owns the good homogeneity and convergence to ensure the accuracy of the results. Third, our study overcomes the constraint of conventional meta-analysis and distinguishes the differences among different sampling methods in the detection of RVs using direct and indirect results. Fourth, additional network meta-analyses about eight specific viruses were performed and would be useful in assisting clinical practice.

However, our present network meta-analyses had some limitations. First, all of the included articles were CTs or

CSs, which could not provide powerful statistical power that randomised controlled trials (RCTs) could do. Second, the studies regarding the comparisons of BAL, VTM-S and VTM-A were relatively small, which could result in some unclear bias. Last but not least, a variety of viral laboratory testing techniques (RT-PCR/IFA/ ELISA and so on), materials (nylon, rayon and cotton) and styles (flocked or conventional) of these sampling methods, in addition, more precise results (true positive, false positive, true negative and false negative) were not involved and distinguished in our study due to the absence of sufficient or high-quality data, thus, further stratified analyses based on a larger set of samples were recommended.

## CONCLUSION

In summary, the systematic review and meta-analyses shed light that NPW, MTS and NPS had higher diagnostic value regarding RVs infection and MTS showed its superiority at the positive rate, less discomfort and easy to operate; moreover, other preferred methods should be considered in case of a specific virus outbreak. Certainly, in consideration of the limitations of the study, conclusions should be interpreted with caution. Hopefully, this meta-analysis was able to provide some evidences for clinicians in the selection of appropriate sampling methods for patients with RVs infection. Strictly designed and upcoming prospective RCTs were required to provide more available data and validate our findings.

## Author affiliations

${ }^{1}$ Department of Hand and Foot Surgery, Zibo Central Hospital,Shandong First Medical University, Zibo, Shandong, China
${ }^{2}$ Department of Critical Care Medicine, Zibo central hospital, Zibo, Shandong, China
${ }^{3}$ Department of Clinical Laboratory, Aerospace Central Hospital, Beijing, China
${ }^{4}$ Department of spine Surgery, Renji Hospital, Shanghai, China
${ }^{5}$ Department of Orthopedic Surgery, Sun Yat-Sen Memorial Hospital, Guangzhou, Guangdong, China

Contributors NH, KW, MB, WS and BX conceptualised, designed and prepared the initial draft of the study, which was reviewed by HZ, HC, YZ and SH. FJ, HZ, KW, HC and BX contributed to the abstract, full article screening and data extraction. All the authors reviewed the draft and approved the final version of the manuscript.
Funding The authors have not declared a specific grant for this research from any funding agency in the public, commercial or not-for-profit sectors.
Competing interests None declared.
Patient consent for publication Not required.
Ethics approval Ethical approval for this study was not applicable because it was a review of existing literature and did not involve any handling of individual patient's data.
Provenance and peer review Not commissioned; externally peer reviewed.
Data availability statement All data relevant to the study are included in the article or uploaded as supplemental information. All the data analysed and reported in this paper were from published literature, which is already in the public domain.
Supplemental material This content has been supplied by the author(s). It has not been vetted by BMJ Publishing Group Limited (BMJ) and may not have been peer-reviewed. Any opinions or recommendations discussed are solely those of the author(s) and are not endorsed by BMJ. BMJ disclaims all liability and responsibility arising from any reliance placed on the content. Where the content includes any translated material, BMJ does not warrant the accuracy and reliability of the translations (including but not limited to local regulations, clinical guidelines,

terminology, drug names and drug dosages), and is not responsible for any error and/or omissions arising from translation and adaptation or otherwise.
Open access This is an open access article distributed in accordance with the Creative Commons Attribution Non Commercial (CC BY-NC 4.0) license, which permits others to distribute, remix, adapt, build upon this work non-commercially, and license their derivative works on different terms, provided the original work is properly cited, appropriate credit is given, any changes made indicated, and the use is non-commercial. See. http://creativecommons.org/licenses/by-nc/4.0/.
