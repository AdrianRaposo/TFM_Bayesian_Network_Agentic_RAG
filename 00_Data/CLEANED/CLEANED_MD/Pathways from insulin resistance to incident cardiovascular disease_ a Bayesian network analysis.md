# Pathways from insulin resistance to incident cardiovascular disease: a Bayesian network analysis 

Xue Tian ${ }^{1,2,3,4}$, Shuohua Chen ${ }^{5}$, Xue Xia ${ }^{1,2,3}$, Qin Xu ${ }^{1,2,3}$, Yijun Zhang ${ }^{1,2,3,4}$, Chenhao Zheng ${ }^{6}$, Shouling $\mathrm{Wu}^{5 *}$ and Anxin Wang ${ }^{1,2,3 *}$


#### Abstract

Background Insulin resistance coexist with many metabolic disorders, whether these disorders were promotors or pathway-factors for the association of insulin resistance and cardiovascular disease (CVD) remained unclear. We aimed to investigate the pathways related to elevated the triglyceride-glucose (TyG) index and pathways through elevated TyG index to the occurrence of CVD in Chinese adults.


Methods A total of 96,506 participants were enrolled from the Kailuan study. Bayesian network model with the maxmin hill climbing algorithm and maximum likelihood estimation was applied to identify factors and pathways related to the TyG index, and quantitatively infer the impact of associated factors on elevated TyG index and the occurrence of CVD by computing conditional probabilities.
Results A final Bayesian network was constructed with 14 nodes and 25 arcs, creating 28 pathways related to elevated TyG index and 8 pathways from elevated TyG index to CVD. Elevated TyG index was causally associated with CVD, the condition probability was $11.9 \%$. Pathways to elevated TyG index were mainly through unhealthy lifestyles and the subsequent increase in lipid profiles, especially smoking and low-density lipoprotein cholesterol. The most important pathway from elevated TyG index to CVD was through overweight/obesity, hypertension, and chronic kidney disease, with a condition probability of $18.5 \%$. The maximum relative change rate related to elevated TyG index was observed for overweight/obesity (64.3\%).
Conclusions Elevated TyG index was causally associated with the risk of CVD, a combined control of lifestyles and metabolic factors may contribute to the reduction of TyG index and the prevention of CVD.
Keywords Triglyceride-glucose index, Cardiovascular disease, Bayesian network analysis, Causal association

[^0][^1]
[^0]:    *Correspondence:

    Shouling Wu
    drwusl@163.com
    Anxin Wang
    wanganxin@bjth.org
    ${ }^{1}$ Department of Epidemiology, Beijing Neurosurgical Institute, Beijing Tiantan Hospital, Capital Medical University, No. 119 South 4th Ring West Road, Fengtai District, Beijing 100070, China
    ${ }^{2}$ China National Clinical Research Center for Neurological Diseases,, Beijing Tiantan Hospital, Capital Medical University, Beijing, China

[^1]:    ${ }^{3}$ Department of Clinical Epidemiology and Clinical Trial, Capital Medical University, Beijing, China
    ${ }^{4}$ Department of Epidemiology and Health Statistics, School of Public Health, Capital Medical University, Beijing, China
    ${ }^{5}$ Department of Cardiology, Kailuan Hospital, North China University of Science and Technology, 57 Xinhua East Rd, Tangshan 063000, China
    ${ }^{6}$ Statistics-Mathematics, Rutgers University, New Brunswick, NewBrunswick, NJ, USA

## Introduction

Insulin resistance, which refers to the diminished or impaired insulin sensitivity of target organs or tissues shown as impairments in absorbing and oxidizing the glucose, has been reported to be an important risk factor in the pathogenesis of cardiovascular disease (CVD) [1--3]. Therefore, an early detection and control of insulin resistance may contribute to the prevention of CVD. A simple and reliable surrogate marker of insulin resistance is the triglyceride-glucose (TyG) index, which merely derives from the levels of triglyceride (TG) and fasting blood glucose (FBG) [4--6]. The TyG index has shown a strong correlation with the hyperinsulinemiceuglycemic clamp, which has been considered as the gold-standard method for the assessing insulin resistance [7--9]. The high accessibility and cost-effectiveness make the TyG index be an attractive option for assessing insulin resistance in large population-based studies. Numerous studies have reported that the TyG index performed excellently in predicting the risk of CVD [4, 10--15].

However, it is noteworthy that most of the current studies on the role of TyG index in the development of CVD are associative and do not establish a causal relationship, and the underlying pathways through modified risk factors behind the association remains unknown. The identification of modifiable contributing factors can assist in designing individualized interventions that focused on decline the TyG index and preventing the development of CVD in early stages. The traditional statistical models in these studies only focused on displaying correlations between dependent variables and various independent variables without reflecting the overall linkage effect. To address these knowledge gaps and methodological limitations, Bayesian network analysis was performed in the current study. Compared with the traditional methods, Bayesian network analysis could intuitively describe the correlations of the TyG index, modified risk factors, and the occurrence of CVD by constructing directed acyclic graphs, and also allow us to obtain the correlation strength by calculating the conditional probabilities [16, 17]. Moreover, Bayesian network could also make inferences of unknown nodes according to the state of a known node, so as to be applied in the risk assessment of elevated TyG index and the occurrence of CVD.

Therefore, using data from a large community-based cohort, we sought to investigate the casual relationship between the TyG index and the risk of CVD, and explore the potential factors and pathways associated with elevated TyG index and the occurrence of CVD. The results were expected to guide the clinical decision making for CVD risk assessment and strategies establishment through controlling the levels of the TyG index.

## Methods

## Study population

This study originated from the Kailuan study, which was a large prospective cohort study conducted in Tangshan City, Northern China. The design of the study has been fully described previously [18, 19]. In brief, a total of 101,510 participants aged 18--98 years were recruited during 2006--2007, and were followed up every two 2 years until December 2021. The current study excluded 3,726 individuals with a history of CVD, and 1,278 individuals with missing data on FBG or TG, leaving 96,506 participants in the current analysis (Figure S1). The study was conducted according to the principles of the Declaration of Helsinki and was approved by the Ethics Committee of Kailuan Hospital. All participants gave written informed consent.

## Data collection

Information on demographic characteristics (age, sex, education, income), lifestyle (smoking, drinking, physical activity, perceived salt intake), medical history and medication information was collected through face-to-face interview via a standardized questionnaires by trained staff. Height and weight were measured Height was measured to the nearest 0.1 cm using a tape rule, and weight was measured to the nearest 0.1 kg using calibrated platform scales by trained field workers during the survey, and body mass index (BMI) was calculated as weight (kg)/height (m^{2}). Blood pressure was measured twice from the seated position using a mercury sphygmomanometer, and the mean of the two readings was used for the analysis. All blood samples were analyzed using an auto-analyzer (Hitachi 747, Tokyo, Japan) at the central laboratory platform, including FBG, lipid profiles, serum creatinine, serum uric acid (SUA) and high sensitivity C reactive protein (hs-CRP). Non-high density lipoprotein cholesterol (Non-HDL) was calculated as total cholesterol (TC) minus high density lipoprotein cholesterol (HDL). Estimated glomerular filtration rate (eGFR) was calculated used Chronic Kidney Disease Epidemiology Collaboration 2009 creatinine equation [20].

Current smoking or drinking was defined according to self-reported cigarette or alcohol consumption during the past 12 months. Individuals who exercised more than four times per week (≥ 20 min/time) were classified as active physical activity. High salt intake was defined as salt intake > 10 g/d [21]. Overweight or obesity was defined as BMI ≥ 24 kg/m^{2} according to Working Group on Obesity in China criteria [22]. High systolic blood pressure (SBP) was defined as SBP ≥ 140mmHg. High diastolic blood pressure (DBP) was defined as DBP ≥ 90mmHg. Elevated FBG was defined as FBG ≥ 5.6 mmol/L. High level of TC was defined as TC ≥ 5.2 mmol/L [23]. High level of TG was defined as TG ≥ 1.7 mmol/L [23]. High level of

low-density lipoprotein cholesterol (LDL) was defined as LDL ≥ 3.4 mmol/ L [23]. Low level of HDL was defined as HDL ≤ 1.0 mmol/ L [23]. High level of non-HDL was defined as non-HDL ≥ 3.4 mmol/ L [23]. Hyperuricemia was defined as SUA ≥ 420 μmol/ L [24].Inflammation status was defined as hs-CRP ≥ 3.0 mg/dL. Chronic kidney disease was defined as eGFR < 60 ml/min/1.73m^{2}.

## Calculation of TyG index

The TyG index was calculated as ln [(fasting TG (mg/dl)×FBG (mg/dl)/2] [14, 15] Since the threshold of TyG index that predict the risk of CVD has varied in different regions and population, and no common-recommended cutoff has been found in previous studies. Thus, the optimal cutoff point for TyG index associated with the risk of CVD was determined using an outcome-oriented method to maximized log-rank statistics, as previously done [3, 25].

## Assessment of outcome

The outcome in our study was incident CVD during the follow-up period until the date of death or the latest visit in December 2021, including stroke and myocardial infarction. Ascertainment of incident CVD was described previously [18, 26]. All participants were linked to the Municipal Social Insurance Institution and the Hospital Discharge Register for incidence of CVD, which cover all the Kailuan study participants. To further identify potential CVD events, we reviewed the discharge lists from the 11 hospitals and asked for a history of CVD via a questionnaire during the biennial interview. For all suspected CVD events, 3 experienced physician adjudicators who were blinded to the study design reviewed the medical records.

## Statistical analysis

Participants were divided into low and high TyG index group according to the cutoff determined by outcome-oriented method to maximized log-rank statistics method. Baselined characteristics were described as mean ± standard deviation (SD) for normally distributed variables, or median with interquartile range (IQR) for skewed distributed variables, or frequency with proportion for categorical variables. Differences between groups were compared with student t test, Wilcoxon, or chi-square test, as appropriate. Missing data was dealt with multiple imputation by chained equation with estimates combined 5 imputation sets using Ruben's rule, under the missing at random assumption. The correlation of the TyG index with other common cardiovascular risk factors weas examined with Peason or Spearman correlation analysis.

Subsequently, the Bayesian network analysis was performed to create and evaluate plausible causal relationships between the TyG index, modified risk factors with a P value < 0.05 in the correlation analysis, and the occurrence of CVD. The Bayesian network is an acyclic directed graph combined with a conditional probability table, in which each node represents a random variable and the arcs linking the nodes represent relationships between variables [27]. The construction of a Bayesian network included Bayesian learning and Bayesian inference. The Max-Min Hill Climbing (MMHC) algorithm was used for the structure learning [28, 29]. By learning 100 networks from the data, an averaged Bayesian network was constructed with arcs appearing in more than 85% of bootstrapped networks. Then maximum likelihood estimation was applied to estimate the conditional probability of each node. In the current study, only pathways through TyG index were preserved in the final structure. The Bayesian inference involves finding the posterior probability distribution of elevated TyG index and the occurrence of CVD given the observed random variables by marginalizing the joint probability distribution. Both the absolute and relative change of conditional probabilities were calculated in the current analysis. Age- (< 60 vs. ≥ 60 years) and sex-specific analyses were performed to explore the association in different populations.

The structure was learned with the “bnlearn” package in R version 4.3.1 (www.r-project.org), and the parameters were obtained with Netica software. All other analyses were performed using SAS version 9.4 (SAS Institute, Cary, NC, USA). All the statistical tests were 2-sided, and P < 0.05 was considered statistical significance.

## Results

## Baseline characters

Among 96,506 enrolled, the median age was 51.59 (IQR, 43.46--58.81) years and 76,755 (79.53%) individuals were men. The median level of the TyG index was 8.57 (IQR, 8.18--9.05). Using an outcome-oriented method to maximize log-rank statistics, the optimal cutoff point of the TyG index associated with incident CVD was 8.81 (Figure S2). A total of 34,953 (36.22%) participants had a high TyG index. Baseline characteristics between participants with low and high TyG index are summarized in Table 1. Participants with a high level of TyG index were more likely to be older, men, less educated, had a higher proportion of current smoker, current drinker, high salt intake, a higher prevalence of hypertension, diabetes, and dyslipidemia, and had more cardiometabolic risk factors, compared with those with a low level of TyG index (Table 2).

## Correlation between TyG index and other risk factors

Correlation analyses showed that there was a significantly positive relationship of the TyG index with TG,

Table 1 Baseline characteristics of the participants

Abbreviations: eGFR, estimated glomerular filtration rate; LDL, low density lipoprotein; HDL, high density lipoprotein; nonHDL, on-high density lipoprotein; hs-CRP, high-sensitivity C-reactive protein; SUA, serum uric acid; TyG index, triglyceride-glucose index

Table 2 The conditional probabilities for the pathways from TyG index to the occurrence of CVD


Abbreviations: BMI, body mass index; CVD, cardiovascular disease; eGFR, estimated glomerular filtration rate; hs-CRP, high-sensitivity C-reactive protein; SBP, systolic blood pressure; TyG index, triglyceride-glucose index

FBG, BMI, DBP, SBP, SUA, NONHDL, TC, LDL, smoking, drinking, salt intake, and hs-CRP, the correlation coefficient ranged from 0.84 to 0.01 (Fig. 1). Additionally, HDL-C and eGFR levels were negatively associated with the level of TyG index. There was no significant correlation between physical activity with the level of TyG index.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Correlation of TyG index with common risk factors of cardiovascular disease

## Bayesian network learning

The original Bayesian network was conducted among 19 nodes (Figure S3). After excluding nodes that were not related to the TyG index and pathways without TyG index, a final Bayesian network with 14 nodes and 25 arcs were constructed (Fig. 2). Conditional independence tests showed that all the arcs were significant ( $P<0.0001$, Table S1). A total of 28 pathways associated with elevated TyG index, 8 pathways from TyG index to the occurrence of CVD, and 224 pathways associated with elevated TyG index and the occurrence of CVD were finally identified (Fig. 2).

The Bayesian network model could be used to quantitatively analyze the impact of associated factors on elevated TyG index and the occurrence of CVD by computing conditional probabilities (Fig. 2). For instance, if an individual was current drinker, then probability of developing elevated TyG index was $36.5 \%$; if the individual also had a high level of LDL, the probability increased to $40.4 \%$; if the individual also had a high level of FBG, the probability reached to $62.1 \%$. Similarly, if an individual was without the above-mentioned risk factors, the probability of elevated is $26.5 \%$. In the pathways to elevated TyG index, changes in lifestyle could firstly lead to the increase in the levels of lipid profiles and FBG, then lead to the elevation of the TyG index (Table S2). Among the 28 pathways, 24 pathways ( $86 \%$ ) included elevated LDL, and the pathways included elevated FBG and TG yielded the maximum condition probability of elevated TyG index, almost $100 \%$. Pathways through the sole role of elevated TG yielded a greater probability ( $93.8 \%$ ) of elevated TyG index than through the sole role of elevated FBG (ranged from 62.0 to $63.5 \%$ ). Additionally, the probability for the
pathways though LDL, TC, and nonHDL to elevated TyG index was approximately $40 \%$.

Among 8 pathways from TyG index to the occurrence of CVD, the probability through the direct pathway from elevated TyG index to the occurrence of CVD was $11.9 \%$. The indirect pathways from elevated TyG index to the occurrence of CVD included leading to overweight or obesity (BMI), hypertension (SBP), inflammation (hs-CRP), and chronic kidney disease (eGFR) (Fig. 3 and Table S3). The maximum probability among these pathways was through (BMI), SBP, and eGFR, reaching $18.5 \%$; followed by through (BMI) and SBP, reaching $17.4 \%$; through BMI, hs-CRP, eGFR, reaching $14.3 \%$; and through hs-CRP, eGFR, reaching $14.0 \%$.

Among 224 pathways associated with elevated TyG index and the occurrence of CVD, 56 pathways (25\%) through elevated SBP and declined eGFR yielded the maximum probability of the occurrence of CVD, reaching $18.5 \% ; 56$ pathways ( $25 \%$ ) through elevated SBP yielded a probability of $17.4 \% ; 28$ pathways ( $12.5 \%$ ) pathways through elevated hs-CRP and declined eGFR yielded a probability of $14.3 \% ; 56$ pathways ( $25 \%$ ) through declined eGFR yielded a probability of $14.0 \%$; and 28 pathways ( $12.5 \%$ ) direct through TyG index yielded a probability of $11.9 \%$.

## Bayesian network inference

The probability of elevated TyG index was influenced by the lipid profiles, FBG levels and lifestyles (Fig. 4A). Changes in TG levels yielded the maximum relative changes in the probability of elevated TyG index. If the TG levels of an individual changed from a low to high level, the probability of elevated TyG index increased
![img-1.jpeg](img-1.jpeg)

Fig. 2 Bayesin network analysis for the pathways through elevated TyG index to the occurrence of CVD

![img-2.jpeg](img-2.jpeg)

Fig. 3 The maximum conditional probability for the pathways through elevated TyG index to the occurrence of CVD

from 9.9 to 94.0%, with a relative increase rate of 848.5%. Similarly, the probability of elevated TyG index increased from 26.6 to 59.9% (relative increase rate, 125.2%) with changes in FBG levels; 33.5--39.5% (relative increase rate, 17.3%) with changes in nonHDL levels; 35.9--40.5% (relative increase rate, 12.8%) with changes in LDL levels; 34.7--39.0% (relative increase rate, 12.4%) with changes in TC levels. Among lifestyles, changes in smoking status yielded a greater increase in the probability of elevated TyG index, from 35.2 to 38.8% (relative increase rate, 10.2%); followed by changes in drinking status, from 36.3 to 36.5% (relative increase rate, 0.6%), and changes in salt intake, from 36.4 to 36.6% (relative increase rate, 0.5%).

A transition from a low to a high level of the TyG index could also lead to the changes in the probability of other cardiometabolic risk factors and the occurrence of CVD (Fig. 4B). The maximum relative changes in the probability was observed for overweight or obesity, from 38.7 to 63.6% (relative change rate, 64.3%); followed by hypertension, from 21.4 to 32.2% (relative change rate, 50.5%), chronic kidney disease (relative change rate, 37.6%), and inflammation, from 17.9 to 21.4% (relative change rate, 19.6%). Additionally, the probability of CVD changed from 7.9 to 11.9%, with a relative change rate of 50.6%. The results indicated that elevated TyG index could casually increase the risk of CVD, and the pathways mainly through increasing BMI, SBP and declining eGFR.

### Age- and sex- specific analyses

Changes in lipids and lifestyles tended to contribute more to the probability of elevated TyG index in young adults and women (Fig. 5A and D). Additionally, the impact of TyG index on cardiometabolic risk factors and the occurrence of CVD tended to be greater in young adults and women (Fig. 5E and F). The relative increase rate of the occurrence of CVD was 63.9% versus 30.6% in young and old adults, and 151.5% versus 36.3% in women and men, respectively. In terms of the relative increase rate of cardiometabolic risk factors, the top factors associated with elevated TyG index was SBP (72.0% and 133.6%) in young adults and women, which was BMI (57.6% and 59.8%) in old adults and men, indicating the pathways from TyG index to CVD differed by age and sex.

### Discussion

Based on Bayesian network analysis, our study found a causal association of TyG index with the risk of CVD. Changes in lifestyle and increase in lipid profiles played important roles in the pathways to elevated TyG index, especially smoking and elevated LDL. Elevated TyG index was directly related to overweight/obesity, hypertension, chronic kidney disease, and inflammation, which further contributed to the occurrence of CVD. The pathways from elevated TyG index to CVD differed by age and sex, hypertension contributed more in young adults and women, and overweight/obesity contributed more in older adults and men. The findings may improve our understanding of the mechanisms of elevated TyG index and the development of incident CVD.

Previous studies mainly focused on the correlation between TyG index with other risk factors, and yielded inconsistent conclusions. For instance, one retrospective cohort study showed that the TyG index was positively correlated with FBG, BMI, TG, TC, and eGFR, but not with LDL-C [30]. While one cross-sectional study and other cohort study showed that the TyG index was

A. Change in the porportion of elevated TyG index

![img-3.jpeg](img-3.jpeg)

B. Change in the porportion of cardiometabolic factors and CVD

![img-4.jpeg](img-4.jpeg)

**Fig. 4** Bayesian inference for the changes in the probabilities of elevated TyG index and the occurrence of CVD

significantly associated with all the above factors [31, 32]. However, whether these factors were contributor or product of elevated TyG index was not explored in these studies. Our study found that unhealthy lifestyles, including smoking, drinking, and salty diet could increase the levels of lipids, and then increase the level of FBG or TG, which eventually lead to elevated TyG index. In other words, the finding indicated that unhealthy lifestyles, lipids, and FBG were the contributors, rather than the product of elevated TyG index. The results indicated the

![img-5.jpeg](img-5.jpeg)

**Fig. 5** Age- and sex-specific bayesian inference for the changes in the probabilities of elevated TyG index and the occurrence of CVD

importance of keeping a healthy lifestyle in controlling the levels of TyG index and the prevention of CVD.

Among the lifestyles, smoking contributed the most to elevated TyG index, which could direct lead to the increase in the levels of TG and indirect increase the levels of FBG through elevated LDL. The finding was supported by mechanical studies, showing that nicotine stimulates the sympathetic adrenal system, resulting in the increased secretion of catecholamines that results in increased lipolysis and increased concentrations of plasma free fatty acids, which further promote the secretion of hepatic free fatty acids and TG into the blood stream [33, 34]. In addition, drinking could indirectly increase the levels of FBG through LDL, TC, and nonHDL. Mechanically, alcohol consumption could lead to liver injury and fat metabolism, which then affect insulin signaling and cellular function, and increase insulin resistance [35]. Among the lipid profiles, LDL was the most common factor associated with unhealthy lifestyles, indicating strategies on LDL levels control could also be benefit in reducing insulin resistance.

In terms of the pathways from elevated TyG index to CVD, elevated TyG index could direct lead to the occurrence of CVD, indicating a causal relationship between the TyG index and the risk of CVD. Actually, the evidence on the causal relationship between TyG index and CVD was limited. A two-sample Mendelian randomization (MR) of published genome-wide association study data supported that a higher TyG index is a causal risk factor for incident heart failure in the general population [36]. Another MR study used data from the UK Biobank also found a causal effect of the TyG index on the risk of extensive cardio-cerebrovascular metabolic outcomes [37]. The application of MR was relied on three key assumptions. In contract, Bayesian network analysis without relying on genes cold handle more complex causal relationships and conditional dependencies, provide comprehensive inference models, and have strong scalability and flexibility. Our study provided not only a causal relationship between TyG index and CVD among Chinese adults, but also extent the application of Bayesian analysis to a large population-based study.

Additionally, the Bayesian network analysis could also present the pathways among multiple variables. Our study showed that elevated the TyG index could directly increase the levels of BMI, SBP, hsCRP, and decline the levels of eGFR, which then increase the occurrence of CVD. And the most pathway from elevated TyG index to CVD was through overweight/obesity, hypertension, and chronic kidney disease. In insulin-resistance individuals, hormone-sensitive lipase activity is decreased, leading to an increase in fat storage and obesity [38]. Meta-analysis showed that suppression of insulin secretion alone is sufficient to treat obesity [39]. These provided evidence for the finding that BMI was the most important contributor in the pathway. Insulin resistance could lead to endothelial dysfunction and the increase of sympathetic nerve tension, and may accelerate the reabsorption of sodium and water by renal tubules at the same time, eventually leading to the occurrence and development of hypertension [40, 41]. Insulin resistance induce adaptive pathological changes in the renal glomerulus, such as thickening of the glomerular basement membrane, hypertrophy and proliferation of mesangial cells, and deposition of mesangial matrix, all of which lead to impaired glomerular filtration function [42]. Insulin resistance could also promote the production of inflammatory factors, which then aggravate the hazard of insulin resistance on the organs. The findings of pathway analysis provided an insightful suggestion on the mechanisms underlying the link between elevated TyG index and the risk of CVD, and emphasized the important role of considering the combined contribution of multiple metabolic factors in the prevention of CVD.

Additionally, our study found that the most important contributor for the pathway from elevated TyG index and CVD differed by age and sex. Hypertension contributed more in young adults and women, and overweight/obesity contributed more in older adults and men. The findings were consistent with previous associative studies. Data from the Cardiorespiratory Fitness and Health in Eastern Armed Forces showed that the association of TyG index and hypertension was observed in young adults, rather than middle adults [43]. Data from the Korean Genome and Epidemiology Study showed that the TyG index was significantly associated with new-onset hypertension only in women [44]. Insulin resistance often coexist with obesity, there were differences in metabolic and physiological characteristics between men and women, young and older adults, such as lipid-metabolism patterns, fat distribution, and hormone levels, which lead to the different pathways from elevated TyG index and CVD. The results indicated that age and sex differences may be considered when implementing strategies on the prevention of CVD through controlling TyG index levels and its relative cardiometabolic risk factors.

## Strengths and limitations

Our study has several strengths. We conducted this study in a large prospective community cohort and put great emphasis on data quality, following standard protocols during the data collection process and the ascertainment of the events. The use of Bayesian network analysis allowed the associated variables and outcomes to be modeled simultaneously and the interactions between variables to be studies thoroughly, which supplemented the existing knowledge of the factors associated with

elevated TyG index and pathways from elevated TyG index to CVD.

However, this study also has several limitations. First, we established a discrete Bayesian network that involve discretization for the continuous variables, which may lead to a loss of information. However, discretization is a common practice in risk prediction due to its higher clinical applicability and explainability. Second, CVD cases in our study included myocardial infarction and stroke, and we may underestimate the incidence rate of CVD, which has broader subtypes. Third, the definition of chronic kidney disease was based on eGFR, since the data of albuminuria was unavailable in the study, which may underestimate the rate of participants with chronic kidney disease. Fourth, we did not assess inter observer correlation, however, the survey of our study included standardized questionnaires physical examinations by trained staff, and laboratory tests from blood samples were analyzed at the central laboratory, which could guarantee the quality of data. Finally, the participants were Han Chinese adults from the Kailuan community, which might limit the generalization of our findings to other ethnic or socioeconomic groups. However, the homogeneity of socioeconomic status in the study population may help reduce residual confounding factors related to socioeconomic factors.

## Conclusions

In this large community-based study, we found that the TyG index was causally related to the risk of CVD. Unhealthy lifestyles, lipids and FBG were promotors for elevated TyG index, in addition, overweight/obesity, hypertension, chronic kidney disease, and inflammation were important contributors for the pathways from elevated TyG index to CVD. The findings provided evidence on the mechanisms for the association of TyG index and CVD, and emphasized the important role of considering the combined contribution of multiple metabolic factors in controlling of TyG index levels and the prevention of CVD.

## Supplementary Information

The online version contains supplementary material available at https://doi.or g/10.1186/s12933-024-02510-w.

## Supplementary Material 1

## Acknowledgements

We thank all study participants, their relatives, the members of the survey teams at the 11 regional hospitals of the Kailuan Medical Group, and the project development and management teams at the Beijing Tiantan Hospital and the Kailuan Group.

## Author contributions

SW, AW contributed to the conception and design of the study; XT contributed to manuscript drafting; XT, SC, XX, QX, YZ, CZ contributed to the
statistics analysis and the acquisition of data; all authors contributed to critical revisions of the manuscript.

## Funding

This work was supported by the National Key Research and Development Program of China (2022YFC3600600) and the high-level public health talents (xuekegugan-02-47).

## Data availability

No datasets were generated or analysed during the current study.

## Declarations

## Ethics approval and consent to participate

The study was performed according to the guidelines of the Helsinki Declaration and was approved by the Ethics Committee of Kailuan General Hospital (approval number: 2006-05). All participants were agreed to take part in the study and provided informed written consent.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.

## Disclosure

None.

Received: 13 September 2024 / Accepted: 13 November 2024
Published online: 21 November 2024

## Publisher's note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.