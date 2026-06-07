# Risk analysis of new oral anticoagulants for gastrointestinal bleeding and intracranial hemorrhage in atrial fibrillation patients: a systematic review and network meta-analysis* ${ }^{*}$ 

Wei-wei $\mathrm{XU}^{\dagger}$, Shen-jiang HU , Tao $\mathrm{WU}^{\dagger \ddagger}$<br>(Department of Cardiology, the First Affiliated Hospital, School of Medicine, Zhejiang University, Hangzhou 310003, China)<br>${ }^{\dagger}$ E-mail: xuweiweijuly@163.com; taowu001@yeah.net<br>Received Mar. 31, 2016; Revision accepted Oct. 23, 2016; Crosschecked June 16, 2017


#### Abstract

Background: Antithrombotic therapy using new oral anticoagulants (NOACs) in patients with atrial fibrillation (AF) has been generally shown to have a favorable risk-benefit profile. Since there has been dispute about the risks of gastrointestinal bleeding (GIB) and intracranial hemorrhage (ICH), we sought to conduct a systematic review and network meta-analysis using Bayesian inference to analyze the risks of GIB and ICH in AF patients taking NOACs. Methods: We analyzed data from 20 randomized controlled trials of 91671 AF patients receiving anticoagulants, antiplatelet drugs, or placebo. Bayesian network meta-analysis of two different evidence networks was performed using a binomial likelihood model, based on a network in which different agents (and doses) were treated as separate nodes. Odds ratios (ORs) and 95\% confidence intervals (CIs) were modeled using Markov chain Monte Carlo methods. Results: Indirect comparisons with the Bayesian model confirmed that aspirin+clopidogrel significantly increased the risk of GIB in AF patients compared to the placebo (OR 0.33, 95\% CI 0.01-0.92). Warfarin was identified as greatly increasing the risk of ICH compared to edoxaban 30 mg (OR 3.42, 95\% CI 1.22-7.24) and dabigatran 110 mg (OR $3.56,95 \%$ CI $1.10-8.45$ ). We further ranked the NOACs for the lowest risk of GIB (apixaban 5 mg ) and ICH (apixaban 5 mg , dabigatran 110 mg , and edoxaban 30 mg ). Conclusions: Bayesian network meta-analysis of treatment of nonvalvular AF patients with anticoagulants suggested that NOACs do not increase risks of GIB and/or ICH, compared to each other.


Key words: Anticoagulation; New oral anticoagulant; Atrial fibrillation; Meta-analysis; Gastrointestinal bleeding; Intracranial hemorrhage
http://dx.doi.org/10.1631/jzus.B1600143

## 1 Introduction

Atrial fibrillation (AF) is a leading cause of ischemic stroke and systemic embolism (Giorda et al., 2014), affecting $0.5 \%$ of the population aged 50 59 years and almost $10 \%$ of those aged $80-89$ years

[^0]CLC number: R541.7+5
(Candel et al., 2004). As an independent factor, AF also causes significant morbidity and mortality, and increases in the cost of healthcare compared to stroke patients without AF (Dulli et al., 2003; LuengoFernandez et al., 2006; Slot et al., 2008). Substantial evidence suggests that most thromboembolic complications of AF could be prevented with adequate pharmacological anticoagulation therapy (Gersh et al., 2004; Fuster et al., 2006; Sacco et al., 2006; Zhang, 2012). Therefore, for AF patients, the American College of Cardiology/American Heart Association (ACC/AHA) 2006 Guidelines recommended warfarin alone for patients with more than one moderate-risk factor for stroke, such as, being older than 75 years,


[^0]:    ${ }^{\ddagger}$ Corresponding author

    * Project supported by the National Natural Science Foundation of China (No. 30800999)
    ${ }^{+}$Electronic supplementary materials: The online version of this article (http://dx.doi.org/10.1631/jzus.B1600143) contains supplementary materials, which are available to authorized users
    (C) ORCID: Wei-wei XU, http://orcid.org/0000-0001-8310-2632; Tao WU, http://orcid.org/0000-0003-3789-7854
    (C) Zhejiang University and Springer-Verlag Berlin Heidelberg 2017

hypertension, heart failure, impaired left ventricular systolic function (ejection fraction $35 \%$ or less or fractional shortening less than $25 \%$ ), or diabetes (Fuster et al., 2006; Sacco et al., 2006). However, vitamin K antagonists (VKAs) have a narrow therapeutic window and regular monitoring of the international normalized ratio (INR) is required. Many reasons exist that can prevent patients from being treated with VKAs correctly, including drug interactions, increased risk of hemorrhage, inadequate compliance with INR monitoring, and a desire by the patient to avoid VKA therapy. Asians seem to do poorly on VKAs, which is associated with lower efficacy, less safety, and more events of major bleeding such as gastrointestinal bleeding (GIB) (Chen et al., 2014). Asians also seem to have poorer anticoagulation control, as reflected by low time in therapeutic ranges (TTRs), than non-Asians. As a second choice, many of those patients are treated with aspirin and/or clopidogrel instead, which could be potentially problematic, particularly in those with co-morbidities (Camm et al., 2012; January et al., 2014).

Therefore, over the past several years, new oral anticoagulants (NOACs) have been developed and approved for stroke prevention in AF patients. Unlike warfarin, which inhibits vitamin K-dependent synthesis of clotting factors II, VII, IX, and X, NOACs inhibit coagulation by directly and specifically binding to the active site of either thrombin (dabigatran) or factor Xa (rivaroxaban, apixaban, and edoxaban). Relative to warfarin, NOACs have rapid onset of action, and in patients with normal renal and hepatic function, rapid offset of action. This obviates the need for bridging therapy with a rapidly-acting parenteral anticoagulant. Moreover, unlike warfarin, these agents do not interact with dietary constituents or alcohol, have few reported drug interactions, and monitoring of their anticoagulant intensity is not routinely required due to their predictable anticoagulant effects. Thus, these NOACs provide important clinical advantages over traditional anticoagulation agents and have been proven to be either superior to or equal to warfarin for the prevention of stroke and systemic embolus (Granger et al., 2011; Levi et al., 2011; Patel et al., 2011).

Since 2012, the European Society of Cardiology (ESC) Guidelines for AF recommend that patients with AF be managed with NOACs alone for the remainder of their lives (Camm et al., 2012). The 2014

American Heart Association (AHA)/American College of Cardiology (ACC)/Heart Rhythm Society (HRS) AF Treatment Guidelines state that the NOACs (dabigatran, rivaroxaban, and apixaban) be used alongside warfarin as preferred therapy (January et al., 2014). Although the above-mentioned management with NOACs improves outcomes and shows a favorable risk-benefit profile for AF patients, some randomized controlled trials (RCTs) (Alexander et al., 2011; Mega et al., 2012) and recent meta-analyses suggested potentially increased or uncertain risks of GIB and intracranial hemorrhage (ICH) (Granger et al., 2011; Patel et al., 2011; Chatterjee et al., 2013; Gomez-Outes et al., 2013; Holster et al., 2013; Ruff et al., 2014). As a consequence, the management of patients taking NOACs still remains a clinical challenge in terms of efficacy and safety. Due to the lack of direct head-to-head trials comparing the NOACs, a careful review of updated literature regarding GIB and ICH risks attributable to NOACs is warranted and particularly relevant because AF patients taking NOACs often have other co-morbidities and concomitantly use other drugs, which may substantially increase risks of GIB and ICH. Furthermore, in contrast with traditional coagulants, no clinically tested antidote is currently available for NOACs, thereby hampering therapeutic options in the event of GIB and ICH (Granger et al., 2011; Levi et al., 2011; Patel et al., 2011). Thus, we aimed to perform a systematic review and pair-wise (direct) and warfarin-adjusted network (indirect) meta-analyses focusing on the risks of GIB and ICH of all currently used anticoagulants in the AF population.

## 2 Materials and methods

### 2.1 Data sources and search strategy

A comprehensive literature search was conducted to identify RCTs reporting GIB or ICH in patients receiving NOACs compared with standard warfarin treatment. Two independent reviewers (WX and TW) searched MEDLINE, EMBASE, and the Cochrane databases of systematic reviews through April 2014 with no language restrictions using medical subject heading terms and key words to identify RCTs including "apixaban" OR "rivaroxaban" OR "dabigatran" OR "edoxaban" AND "atrial fibrillation" AND "humans" AND "randomized controlled

trial". We also reviewed the reference lists of published meta-analyses of anticoagulant and antiplatelet therapies and GIB and ICH events in patients with AF. The electronic search strategy was complemented by a manual review of reference lists of included articles.

### 2.2 Study selection

Search results were combined and duplicates were removed. Studies were first screened based on title and abstract for relevance, after which the full text was reviewed. Studies had to meet the following inclusion criteria: (a) randomized controlled phase II or III trials of VKAs, aspirin, clopidogrel, and novel oral anticoagulants in patients with non-valvular AF; (b) randomized treatment allocation; and (c) intention-to-treat analysis. To reflect current practice patterns, we excluded studies or study arms in which VKAs were administered at non-standard doses (e.g. low fixed doses) or where antiplatelet agents other than aspirin or clopidogrel were tested.

### 2.3 Data abstraction and quality assessment

The outcome of this systematic review was the risks of GIB and ICH. GIB was considered as at least one episode of clinically apparent hematemesis (frank blood or coffee-ground material that tested positive for blood), melena, or spontaneous rectal bleeding (if more than a few spots) or endoscopically confirmed bleeding, and was judged as either major or clinically relevant non-major depending upon the severity (Gibson et al., 2011). ICH was defined as bleeding within the skull, including hemorrhages in the brain and the three meningeal membranes and was diagnosed with clinical symptoms or a computed tomography (CT) scan. The quality of included studies was assessed according to the Cochrane Reviewers' Handbook (Higgins and Green, 2006). Both manuscript and protocol, if available online, were scanned for relevant information on quality.

### 2.4 Statistical analysis

Outcomes were allocated according to the intention-to-treat principle. Only outcomes occurring during the time period that patients received study drugs, placebo, or observation were included within the analyses. Bayesian network meta-analyses and direct, frequentist, pairwise meta-analyses were conducted for all outcomes. Bayesian network meta-
analyses were performed with a binomial likelihood model. Bayesian methods have been widely used in recent years after first being introduced to metaanalysis in 2011 (Dias et al., 2011). They can borrow strength from indirect evidence to gain certainty about all treatment comparisons and allow for estimation of comparative effects that have not been investigated head-to-head in randomized clinical trials. Bayesian methods also allow the straightforward calculation of rank probabilities of a set of alternative treatments. The network meta-analysis was based on a network in which different agents (and doses) were treated as separate nodes (aspirin 100 mg daily, aspirin+clopidogrel, VKA, apixaban 5 mg twice daily, rivaroxaban 20 mg daily, and dabigatran 110 mg and 150 mg twice daily).

Odds ratios (ORs) and 95\% confidence intervals (CIs) were modeled using Markov chain Monte Carlo methods. We obtained the corresponding $95 \% \mathrm{CI}$ using the 2.5 th and 97.5 th percentiles of the posterior distribution, which could be interpreted in a way similar to conventional $95 \%$ CIs. We used adjusted continuity corrections of 0.5 to account for studies with no events (Sweeting et al., 2004). We calculated the probability that each drug was the most efficacious regimen by counting the proportion of iterations of the Markov chain in which each drug had the highest OR (Dias et al., 2011). To ensure convergence, we assessed trace plots and the Brooks-GelmanRubin statistic (Spiegelhalter et al., 2004) (Figs. S1 and S2). Analyses were performed using R 3.0.2 (R Language and Environment for Statistical Computing) and WinBUGS software (MRC Biostatistics Unit).

A network meta-analysis also required that studies were sufficiently similar to pool their results (Dias et al., 2013; Jansen and Naci, 2013). We assessed available study and patient characteristics to ensure similarity and to investigate the potential effect of heterogeneity on effect estimates. We used the node splitting method to calculate the inconsistency of the model. We then evaluated the agreement between the direct and indirect evidence and reported its Bayesian $P$-value (Lumley, 2002). Inconsistency analyses were performed using R 3.0.2.

Additionally, results from our network metaanalysis were qualitatively compared with direct, frequentist, and pairwise estimates. Pairwise metaanalyses were performed using R 3.0.2.

## 3 Results

Of the 518 studies identified, 498 were excluded due to nonrandomized design, registry data, case series, subgroup analysis, post-hoc analysis, low-dose warfarin, or use of antiplatelet agents other than aspirin or clopidogrel. The detailed flow-chart showing study selection is shown in Fig. 1. Twenty studies (Petersen et al., 1989; Connolly et al., 1991; 2006; 2009a; 2009b; 2011; The Boston Area Anticoagulation Trial for Atrial Fibrillation Investigators, 1991; Ezekowitz et al., 1992; Gullov et al., 1998; Hellemons et al., 1999; Hu et al., 2006; Sato et al., 2006; Mant et al., 2007; Chung et al., 2011; Levi et al., 2011; Ogawa et al., 2011; Hori et al., 2012; Mega et al., 2012; Yamashita et al., 2012; Giugliano et al., 2013) with 91671 AF patients met our inclusion criteria and were included in the analysis. Ten different strategies were identified: aspirin, aspirin+clopidogrel, dabigatran 150 mg twice daily, dabigatran 110 mg twice daily, adjusted dose of VKAs, rivaroxaban, apixaban, edoxaban 30 mg daily, edoxaban 60 mg
daily, and placebo/control. Table S1 depicts baseline characteristics of the included studies. Table S2 depicts quality assessments. Overall, a low risk of bias was identified. All studies provided adequate sequence generation, reported outcomes completely, and were free of selective reporting bias. All 20 studies were designed as RCTs.

### 3.1 Gastrointestinal bleeding

Indirect comparisons of GIB among the abovementioned 10 strategies including placebo treatment revealed that only aspirin+clopidogrel increased the risk of GIB compared to placebo (OR $0.33,95 \% \mathrm{CI}$ $0.01-0.92$ ). No significant statistical differences were found in AF patients treated with aspirin, aspirin+ clopidogrel, warfarin, or NOACs (dabigatran, edoxaban, rivaroxaban, apixaban) compared to placebo or to each other (Table 1). Furthermore, no single drug or drug combination was identified as conferring significantly lower or higher risk of GIB. The detailed ORs and 95\% CIs defining GIB risks in AF patients treated with different anticoagulation strategies are listed in Table 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Flow chart of study selection

### 3.2 Intracranial hemorrhage

Although no significant differences in ICH were found between any anticoagulant and placebo, warfarin conferred a significantly greater risk of ICH compared to edoxaban 30 mg (OR $3.42,95 \% \mathrm{CI}$ $1.22-7.24$ ) and dabigatran 110 mg (OR $3.56,95 \% \mathrm{CI}$ $1.10-8.45$ ). No NOACs increased the risk of ICH compared to standard care or placebo treatment. A detailed comparison of ORs and $95 \%$ CIs between anti-coagulation strategies is given in Table 2.

### 3.3 Treatment ranking

We ranked the risks of GIB and ICH in AF patients taking anti-coagulants. We defined the probability for the highest and second highest rate of GIB/ICH as a basis for ranking since it shows a larger degree of dispersion compared to other statistics (e.g. the probability of highest rate of GIB/ICH, or surface under the cumulative ranking curve). As a result, aspirin+clopidogrel, edoxaban 60 mg , and placebo were identified as having the greatest risk of GIB, and

Table 1 Odds ratios (ORs) and 95\% confidence intervals (CIs) for network meta-analyses of GIB


OR ( $95 \%$ CI) of drug named in row versus column. Interventions are reported in alphabetical order. Results are ORs in the row-defining treatment compared with ORs in the column-defining treatment. For efficacy, ORs $<1$ favor row-defining treatment. To obtain ORs for comparisons in the opposite direction, reciprocals should be taken. Significant results are in bold. Edo, edoxaban; Riva, rivaroxaban; Dab, dabigatran; Api, apixaban; Asp, aspirin; Clo, clopidogrel

Table 2 Odds ratios (ORs) and 95\% confidence intervals (CIs) for network meta-analyses of ICH


OR ( $95 \%$ CI) of drug named in row versus column. Interventions are reported in alphabetical order. Results are ORs in the row-defining treatment compared with ORs in the column-defining treatment. For efficacy, ORs $<1$ favor row-defining treatment. To obtain ORs for comparisons in the opposite direction, reciprocals should be taken. Significant results are in bold. Edo, edoxaban; Riva, rivaroxaban; Dab, dabigatran; Api, apixaban; Asp, aspirin; Clo, clopidogrel

apixaban 5 mg , warfarin, and aspirin had the lowest risk. Warfarin, aspirin+clopidogrel, and rivaroxaban had the greatest risk of ICH , and apixaban 5 mg , dabigatran 110 mg , and edoxaban 30 mg had the lowest risk. A detailed ranking is reported in Table 3.

Table 3 Treatment ranking based on simulations


* Probability for the highest and second highest risks. Edo, edoxaban; Riva, rivaroxaban; Dab, dabigatran; Api, apixaban; Asp, aspirin; Clo, clopidogrel


### 3.4 Network model consistency and heterogeneity

No major inconsistencies or qualitative differences (e.g. change in directionality of the estimate) were observed when we compared the effect estimates based on direct versus indirect evidence from the comparisons (Tables S3 and S4), supporting the robustness of the model. Connected treatment networks were evaluated to identify heterogeneity and consistency within closed loop evidence structures. All comparisons had little or no heterogeneity. As a secondary endpoint, GIB is defined differently in the initial studies, which indeed influenced the accuracy of this study. After excluding data of Stroke Prevention in Atrial Fibrillation (SPAF-I), Canadian Atrial Fibrillation Anticoagulation (CAFA), Boston Area Anticoagulation Trial for Atrial Fibrillation (BAATAF), and Japan Atrial fibrillation and Stroke Trial (JAST), there were no substantial changes in the overall results. Sensitivity assessment for GIB is performed in Table S5.

## 4 Discussion

AF increases the risk of stroke, a leading cause of death and disability worldwide. The use of oral anticoagulation in patients with AF for stroke pre-
vention, estimated by established criteria, improves outcomes. Although vitamin K antagonism and aspirin (or aspirin with clopidogrel) have been the firstline treatments, NOACs with novel mechanisms of action are now available. These NOACs (direct thrombin inhibitors or factor Xa inhibitors) obviate many of warfarin's shortcomings, and they have demonstrated safety and efficacy in large randomized trials of patients with non-valvular AF. However, major bleeding, such as GIB and ICH, appeared to be limitations of the NOACs. For example, in pivotal stroke prevention in AF trials, NOACs have been associated with an increased risk of major GIB compared with warfarin (Gomez-Outes et al., 2013).

However, differences in pivotal trials among study populations, definitions of major bleeding events, study protocol design, and the absence of parallel trials may limit the conclusiveness of such comparisons. Moreover, it is uncertain why NOACs such as dabigatran 150 mg twice daily and rivaroxaban are associated with a higher rate of major GIB than warfarin, but have simultaneously lower rates of ICH and similar rates of all-site major bleeding events. Therefore, we sought to review the current literature and analyze qualified datasets by performing a systematic review and pair-wise (direct) and warfarinadjusted network (indirect) meta-analyses, to better understand safety data of treatments frequently used in the prevention of stroke and systemic embolism in AF patients. We first focused on separate risks of GIB and ICH in AF patients treated with warfarin, aspirin (or aspirin with clopidogrel), and four NOACs from 20 strictly selected qualified studies without study selection bias to increase our statistical power and reach a reliable conclusion. We found highly focused and extended study designs which were unlike much of the previously published literature. For example, Biondi-Zoccai et al. (2013) and Dogliotti et al. (2014) focused on major bleeding risks of NOACs in AF patients without clarifying the bleeding type. From comprehensive study strategies, meta-analysis revealed aspirin+clopidogrel conferred increased risk of GIB compared to placebo (OR $0.33,95 \%$ CI $0.01-$ 0.92 ), which is consistent with current knowledge of these two treatments based on clinical trials and published meta-analyses.

Our analysis also revealed increased risks of ICH in AF patients taking warfarin compared to edoxaban 30 mg (OR 3.42, 95\% CI 1.22-7.24) and

dabigatran 110 mg (OR 3.56; 95\% CI 1.1-8.45), which favors the above-mentioned NOACs over warfarin. Chatterjee et al. (2013) enrolled 57491 patients from 6 studies, and administered three NOACs (dabigatran, rivaroxaban, and apixaban), and reported that all NOACs studied reduced the risk of ICH, but Bayesian indirect comparison analysis did not reveal a significant difference between the specific medications. However, the fact that this study enrolled and pooled datasets without stratifying the study conditions (e.g. dosage of the NOACs) may reduce the statistical power of the meta-analysis.

Our meta-analysis also revealed no increased or decreased risks of GIB in AF patients taking NOACs compared to traditional coagulants and placebo, which differs from data from previously published meta-analyses and from indirect estimates of risk associated with the coagulants in this study. For example, Holster et al. (2013) studied the risks of NOACs in patients with different diseases (AF, acute coronary syndrome (ACS), orthopedic surgery, intensive care, and deep vein thrombosis/pulmonary embolism), and concluded that patients treated with NOACs have an increased risk of GIB, compared with those who receive standard care. However, this conclusion may be questionable with respect to specialized diseases. A possible underlying pathophysiological basis for NOAC-related GIB was the disruption of GI mucosa, an event distinct from the actual disease/condition each patient had. Apparently, for some diseases listed above, GI mucosa was impaired more severely than in AF alone. Also, oral anti-coagulants may theoretically cause GIB via: (1) systemic anticoagulation; (2) topical anticoagulation; (3) topical direct mucosal stimulation (inhibition of impaired mucosal healing). These mechanisms may occur in combination so that the degree of existing mucosal impairment, NOAC dose, topical drug concentrations, and drug absorption rates in the GI tract play an important role in GIB formation. Therefore, without evaluating inherent GI mucosal damage before NOAC management in different diseases, conclusions about NOACs of GIB in AF management are suspect.

In conclusion, based on a large pooled patient group, we report that AF management with NOACs does not change the risks of GIB and ICH compared with each other. Our network meta-analysis is by far
the most comprehensive study focusing on this aspect. However, caution is required when interpreting the results of the present study. Firstly, the heterogeneity among included trials with respect to the characteristics of the patients, the length of follow-up period, differential loss to follow-up, and concomitant interventions allowed by protocols, might reduce the statistical power to find differences. Some studies with less rigor, which were conducted 10-20 years ago, might further affect the precision of the results. Secondly, it is important not to over-interpret differences in the ranking of tested therapeutic interventions generated by Bayesian inference, since small differences in data generation could lead to significant differences in ranking (Begg and Mazumdar, 1994). We recommend treatment strategies for NOACs in AF patients, specifically. Patients should be screened for GI mucosal damage or current/past bleeding history before NOAC administration. Patients should be counseled for increased risk of GIB in the setting of certain diseases, and the appropriate type and dosage of NOACs should be considered for all AF patients. Long-term follow-up data from real-world studies are still required to confirm the current published evidence and to help define the efficacy and safety of the NOACs in clinical practice.

## Acknowledgements

We sincerely thank Dr. Alek CHOO (Eastern Cereal and Oilseed Research Centre, Agriculture and Agri-Food Canada, Ottawa, Canada) for providing valuable barley varieties for this study.

## Compliance with ethics guidelines

Wei-wei XU, Shen-jiang HU, and Tao WU declare that they have no conflict of interest.

This article does not contain any studies with human or animal subjects performed by any of the authors.

## List of electronic supplementary materials

Fig. S1 Trace plot of the Brooks-Gelman-Rubin statistics of Bayesian network meta-analysis on GIB in patients receiving NOACs compared with standard warfarin treatment
Fig. S2 Trace plot of the Brooks-Gelman-Rubin statistics of Bayesian network meta-analysis on ICH in patients receiving NOACs compared with standard warfarin treatment
Table S1 Characteristics of the included studies
Table S2 Quality assessment of included studies
Table S3 Effect estimates from multiple treatment meta-analysis compared with direct and indirect estimates, based on node-splitting and pair-wise meta-analyses of GIB
Table S4 Effect estimates from multiple treatment meta-analysis compared with direct and indirect estimates, based on node-splitting and pair-wise meta-analyses of ICH
Table S5 Odds ratios (ORs) and 95\% confidence intervals (CIs) for network meta-analyses of GIB for sensitivity test

## 中文概要

题 目：新型口服抗凝血剂在心房颤动患者中胃肠道出血和颅内出血的风险分析：系统回顾和网络 meta分析
目的：评估新型口服抗凝药物在心房颤动患者中胃肠道出血和颅内出血的风险。
创新点：首次用网络 meta 分析的方法评估新型口服抗凝血剂在心房颤动患者中胃肠道出血和颅内出血的风险。
方法：我们搜集了 20 个随机控制试验共 91671 位使用抗凝、抗血小板药物或安慰剂的房颤患者。采用贝叶斯网络 meta 分析，使用马尔可夫链蒙特卡罗方法模拟了比值比（OR）和 $95 \%$ 置信区间（CI）。
结 论：通过与贝叶斯模型的间接比较证实，阿司匹林+氯吡格雷相比安慰剂大大增加房颤患者胃肠道出血的风险（OR 0.33 ， $95 \%$ CI $0.01 \sim 0.92$ ）。华法林与新型口服抗凝药物相比，大大增加了颅内出血风险，其中与依度沙班 30 mg 相比 OR 3.42 ， $95 \%$ CI 1.22 7.24 ，与达比加群 11 mg 相比 OR 3.56 ， $95 \%$ CI $1.10 \sim 8.45$ 。我们进一步排名发现胃肠道出血风险最低的新型口服抗凝血剂是阿哌沙班 5 mg ，颅内出血最低的是阿哌沙班 5 mg 、达比加群 110 mg 和依度沙班 30 mg 。
关键词：抗凝；新型口服抗凝药物；心房颤动；Meta 分析；消化道出血；颅内出血