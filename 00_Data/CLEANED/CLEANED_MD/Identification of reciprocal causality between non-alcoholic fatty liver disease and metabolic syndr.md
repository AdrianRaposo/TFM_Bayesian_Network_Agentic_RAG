# BMJ Open Identification of reciprocal causality between non-alcoholic fatty liver disease and metabolic syndrome by a simplified Bayesian network in a Chinese population 

To cite: Zhang Y, Zhang T, Zhang C, et al. Identification of reciprocal causality between non-alcoholic fatty liver disease and metabolic syndrome by a simplified Bayesian network in a Chinese population. BMJ Open 2015;5:e008204. doi:10.1136/bmjopen-2015008204

- Prepublication history and additional material is available online. To files please visit the journal (http://dx.doi.org/ 10.1136/bmjopen-2015008204).

YZ and TZ contributed equally.

Received 16 March 2015
Revised 25 August 2015
Accepted 28 August 2015

## Abstract

Objectives: It remains unclear whether non-alcoholic fatty liver disease (NAFLD) is a cause or a consequence of metabolic syndrome (MetS). We proposed a simplified Bayesian network (BN) and attempted to confirm their reciprocal causality.
Setting: Bidirectional longitudinal cohorts (subcohorts A and B) were designed and followed up from 2005 to 2011 based on a large-scale health check-up in a Chinese population.
Participants: Subcohort A (from NAFLD to MetS, $\mathrm{n}=8426$ ) included the participants with or without NAFLD at baseline to follow-up the incidence of MetS, while subcohort B (from MetS to NAFLD, n=16 110) included the participants with or without MetS at baseline to follow-up the incidence of NAFLD.
Results: Incidence densities were 2.47 and 17.39 per 100 person-years in subcohorts A and B, respectively. Generalised estimating equation analyses demonstrated that NAFLD was a potential causal factor for MetS (relative risk, RR, 95\% CI 5.23, 3.50 to 7.81), while MetS was also a factor for NAFLD (2.55, 2.23 to 2.92). A BN with 5 simplification strategies was used for the reciprocal causal inference. The BN's causal inference illustrated that the total effect of NAFLD on MetS (attributable risks, AR\%) was $2.49 \%$, while it was $19.92 \%$ for MetS on NAFLD. The total effect of NAFLD on MetS components was different, with dyslipidemia having the greatest (AR\%, 10.15\%), followed by obesity ( $7.63 \%$ ), diabetes ( $3.90 \%$ ) and hypertension (3.51\%). Similar patterns were inferred for MetS components on NAFLD, with obesity having the greatest ( $16.37 \%$ ) effect, followed by diabetes (10.85\%), dyslipidemia (10.74\%) and hypertension (7.36\%). Furthermore, the most important causal pathway from NAFLD to MetS was that NAFLD led to elevated GGT, then to MetS components, while the dominant causal pathway from MetS to NAFLD began with dyslipidaemia.
Conclusions: The findings suggest a reciprocal causality between NAFLD and MetS, and the effect of MetS on NAFLD is significantly greater than that of NAFLD on MetS.


## Strengths and limitations of this study

- This is the first bidirectional longitudinal study designed to verify the reciprocal causality between NAFLD and MetS in a cohort within the same population.
- Bayesian network with five simplification strategies is proposed for the reciprocal causal inference between NAFLD and MetS.
- This study indicates a reciprocal causality between NAFLD and MetS, and the effect of MetS on NAFLD is significantly greater than that of NAFLD on MetS.
- The presence of NAFLD is assessed by experienced radiologists using abdominal ultrasonography, and we have no information on the intraobserver or interobserver reliability of the ultrasonographic examinations.
- The diagnostic criteria of MetS is based on the Chinese medical association diabetes branch rather than the international standard criteria, owing to the absence of waist circumference measurement in the health check-up programme.


## INTRODUCTION

Metabolic syndrome (MetS) is a constellation of metabolic and cardiovascular disease (CVD) risk factors, including obesity, hypertension, hyperglycaemia, dyslipidemia and insulin resistance. ${ }^{1}$ Non-alcoholic fatty liver disease (NAFLD) is defined as a disorder with excess fat in the liver due to nonalcoholic causes. ${ }^{2}$ In recent years, due to lifestyle and economic changes in Chinese populations, the prevalence of NAFLD and MetS has been rapidly increasing, and has become a major public-health challenge. ${ }^{3-7}$ Both disorders predict type 2 diabetes, cardiovascular disease, non-alcoholic steatohepatitis (NASH) and hepatocellular carcinoma.

Insulin resistance (IR) plays a critical role in the development of both NAFLD and MetS.8 9 Patients with MetS frequently have an increase in fat accumulation in the liver and hepatic insulin resistance. In patients with NAFLD, glucose and triglycerides are overproduced by the fatty liver due to the impaired ability of insulin. Furthermore, a growing number of epidemiological studies support an association between NAFLD and MetS.10--21 From the conventional viewpoint, NAFLD is regarded as the hepatic manifestation of MetS. Nevertheless, a series of longitudinal studies have reported that NAFLD might be a precursor to MetS, suggesting NAFLD as a risk factor for MetS rather than merely its hepatic manifestation.15 16 22--29 Meanwhile, other longitudinal studies have also confirmed that MetS precedes the future development of NAFLD.29--34 Therefore, it remains unclear whether NAFLD is a cause or consequence of MetS, and a ‘chicken or egg' scientific debate has arisen recently and gained intense new interest.35 36

Previous studies partially confirmed the complicated and bidirectional relationship between NAFLD and MetS in single-directed longitudinal cohorts, by focusing on the temporal sequence of NAFLD to MetS or MetS to NAFLDs separately. Up to now, to the best of our knowledge, there has been no bidirectional longitudinal cohort study in the same population to clarify their reciprocal relationship. In addition, the previous studies usually utilised regression models, such as the Cox and the generalised estimating equation (GEE) models,37 to analyse the temporal association between NAFLD and MetS. The specified statistical technique for causal inference, such as the Bayesian network (BN),38 39 has not been used to analyse their reciprocal causality.

In this study, we proposed an assumption of reciprocal causality between NAFLD and MetS. To identify this reciprocal causality, a bidirectional longitudinal cohort study (from NAFLD to MetS, and from MetS to NAFLD) was conducted based on a large-scale health check-up in an urban Han Chinese population. A BN with five simplification strategies was used for reciprocal causal inference. Additionally, the relative importance of the pathogenesis and the public health significance of a specific pathway were evaluated.

## MATERIALS AND METHODS

### Design of bidirectional subcohort

On the basis of the routine health check-up system at the Center for Health Management of Shandong Provincial Qianfoshan Hospital and Shandong Provincial Hospital, we set up a large-scale longitudinal cohort and conducted a follow-up from 2005 to 2011 in an urban Han Chinese population. Within this large-scale longitudinal cohort, the bidirectional longitudinal cohorts (subcohorts A and B, shown in figure 1) were designed to identify the reciprocal causality between NAFLD and MetS.

Generally, participants who had a health check-up at least twice between 2005 and 2011 were recruited in this study, with the first health check-up data as baseline and the end of follow-up as end point. Subcohort A (n=8426) included the participants with or without NAFLD at baseline to follow-up the incidence of MetS (shown in figure 1A). The exclusion criteria were: presence of any MetS components (obesity, dyslipidemia, hyperglycaemia or hypertension) at baseline; regular alcohol intake; positive serological marker for hepatitis B surface antigen (HBsAg) or hepatitis C virus antibody (HCVAb) at baseline; and the development of MetS before the development of NAFLD during the follow-up period. The inclusion/exclusion criteria for subcohort B (n=16 110) were similar to subcohort A, except that subcohort B participants were free from NAFLD at baseline and the group excluded those with NAFLD occurring before MetS (shown in figure 1B).

### Measurements

The health check-up examinations were performed after an overnight fasting period of at least 12 h, and all the participants underwent routine anthropometric, clinical and laboratory testing. The anthropometric measurements included height, weight and blood pressure.

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

**Figure 1** Diagram of bidirectional longitudinal cohorts. (A) Subcohort A (from NAFLD to MetS, n=8426) includes participants with or without NAFLD at baseline to follow-up the incidence of MetS and (B) Subcohort B (from MetS to NAFLD, n=16 110) includes participants with or without MetS at baseline to follow-up the incidence of NAFLD.

Height and weight were measured with participants wearing light clothing and no shoes. Body mass index (BMI) was calculated as weight ( kg ) divided by the square of height (m), and was used to estimate obesity. Blood pressure, including systolic blood pressure (SBP) and diastolic blood pressure (DBP), was measured from the right arm after 5 min of rest in a sitting position.

Blood biochemical analysis was performed using a fully automatic blood analyser (E9000, Sysmex Corporation, Japan); the abbreviations of variables and value assignments are shown in table 1. All the participants consented to and underwent an abdominal B-ultrasonography examination performed by experienced radiologists using a 3.5 MHz transducer (Logic Q700 MR, GE, Milwaukee, Wisconsin, USA). Additionally, lifestyle behaviours, including diet, smoking, alcohol intake, sleeping quality and physical activity, were surveyed by a general health questionnaire. Questions about alcohol intake included the type of alcohol consumed, the frequency of alcohol consumption per week and the usual amount per day ( $\geq 20 \mathrm{~g} /$ day). Based on these questions, alcohol intake was coded as an ordered categorical variable as follows: 0 , never; 1 , seldom; 2, often, wine; 3, often, beer; 4, often, Chinese spirits; and 5, often, mixed/all types. Persons with a value $>1$ were considered regular alcohol users.

## Definitions of NAFLD and MetS

According to the revised definition and treatment guidelines laid down by the Chinese Hepatology Association in February 2006, ${ }^{40}$ NAFLD was diagnosed by abdominal ultrasonography based on evidence of liver brightness and a diffusely echogenic change in the liver parenchyma, with exclusion of participants who had a prior diagnosis of NAFLD, hepatitis virus infection (HBsAg or HCVAb positive) or other known causes of steatosis.

The diagnostic criteria for MetS were classified according to the Chinese Medical Association diabetes branch (CDS), ${ }^{41}$ which defines MetS as meeting three or more of the following four categories: (1) overweight or obesity (BMI $\geq 25.0 \mathrm{~kg} / \mathrm{m}^{2}$ ); (2) hypertension (SBP $\geq 140 \mathrm{~mm} \mathrm{Hg}, \mathrm{DBP} \geq 90 \mathrm{~mm} \mathrm{Hg}$ or prior diagnosis); (3) hyperglycaemia (FPG $\geq 6.1 \mathrm{mmol} / \mathrm{L}$ or 2 h postprandial glucose (PG) $\geq 7.8 \mathrm{mmol} / \mathrm{L}$, or prior diagnosis); (4) dyslipidemia (TG $\geq 1.7 \mathrm{mmol} / \mathrm{L}$, or HDL $\leq 0.9 \mathrm{mmol} / \mathrm{L}$ in males and $\leq 1.0 \mathrm{mmol} / \mathrm{L}$ in females).

## Missing data imputation

As missing values existed in our longitudinal cohort data, multiple imputation had to be performed before the GEE analysis and causal network construction. Because the imputation method was dependent on the patterns of the missing data and the types of imputed variables, without loss of generality, the Markov chain Monte Carlo (MCMC) method was chosen according to the Multiple Imputation (MI) Procedure of SAS V.9.1.3. ${ }^{42}$ Most variables had $<2 \%$ missing observations before imputation except smoking and exercise, having $<10 \%$ missing values.

Table 1 Variable abbreviations and assignments


## Statistical analysis

Quantitative variables were summarised by mean $\pm \mathrm{SD}$ for normal distributed variables, median (25th, 75th centile) for non-normal distributed variables and categorical variables by percentages (\%). The p values between the two groups were calculated by $t$ test for normal distributed quantitative variables, with nonparametric test for skew distributed quantitative variables and $\chi^{2}$ test for categorical variables. The number of

person-years was calculated as the sum of the follow-up times from the baseline to the occurrence of NAFLD (or MetS) or the last health check-up. The potential causality of the temporal sequence from NAFLD to MetS (or from MetS to NAFLD) was detected by GEE models. Simple GEE analyses were first performed to select the potential risk factors for MetS in subcohort A and NAFLD in subcohort B, separately. The variables with p value less than the significance level 0.05 were then included in the multiple GEE models. Statistical analyses were performed using SAS V.9.1.3 (SAS Institute, Inc, Cary, North Carolina, USA). A two-sided p value $<0.05$ was considered statistically significant.

## Causal inference by simplified BN

$\mathrm{BN}^{43-45}$ was used to construct the reciprocal causality pathway of NAFLD and MetS (see online supplementary text 1 for details). The primary network was usually too complex to identify the causal effect pathways efficiently. Thus, network simplification was essential before causal inference. We proposed the following simplification criteria: (1) keep the direct and indirect effect pathway; (2) keep the confounding pathway; (3) drop the nodes with irrationality on temporal logic; (4) drop the independent causal factors; (5) drop the collider nodes and collider edges (see online supplementary text 2 for details). ${ }^{38}$
To find the relative importance of the pathogenesis of a specific pathway on the simplified causal network, it is necessary to rank its effect by conditional distribution with all the variables set to the highest level. Taking the causal inference of NAFLD on MetS as an example, suppose we have a pathway $\operatorname{NAFLD}(0,1), \mathrm{A}(0,1), \mathrm{B}(0,1)$, $\mathrm{C}(0,1), \operatorname{MetS}(0,1)$ : its relative importance in pathogenesis can be assessed by

$$
\mathrm{P}(\operatorname{MetS}=1 \mid \text { NAFLD }=1, \mathrm{~A}=1, \mathrm{~B}=1, \mathrm{C}=1)
$$

Furthermore, the joint probability distribution was calculated to evaluate public health significance of the specific pathway. As for the above pathway, the joint probability was calculated by

$$
\begin{aligned}
& \mathrm{P}(\operatorname{MetS}=1, \text { NAFLD }=1, \mathrm{~A}=1, \mathrm{~B}=1, \mathrm{C}=1) \\
& =\mathrm{P}(\operatorname{MetS}=1 \mid \text { NAFLD }=1, \mathrm{~A}=1, \mathrm{~B}=1, \mathrm{C}=1) \\
& \quad P_{c}(\text { NAFLD }=1, \mathrm{~A}=1, \mathrm{~B}=1, \mathrm{C}=1)
\end{aligned}
$$

where the $P_{c}(\operatorname{NAFLD}=1, \mathrm{~A}=1, \mathrm{~B}=1, \mathrm{C}=1)$ was the co-exposure rate of these risk factors (NAFLD, A, B, C) in the population. Usually, since the joint probability could be quite small due to the quite lower exposure rate, public health significance of the pathway might be limited. The natural causal effect of the specific pathway (including direct and indirect pathway) was calculated by the theorem of causal effects identification (see online supplementary text 3 for further information). ${ }^{46-49}$ The BN construction and causal inference were performed on Hugin 7.0. ${ }^{5051}$

## RESULTS

## Characteristics of subcohorts

The baseline characteristics of participants in subcohorts A and B are shown in table 2 and online supplementary table S1. In subcohort A, among 8426 participants, 1243 ( $14.75 \%$ ) participants suffered from NAFLD at baseline. During the follow-up from 2005 to 2011, 93 incidences of MetS were diagnosed in patients with NAFLD, with an incidence density of 2.47 per 100 person-years (93/3767 person-years), while 103 were diagnosed in the non-NAFLD group, with an incidence density of 0.54 per 100 person-years (103/19 040 person-years). In subcohort B, among 16110 participants, 2170 (13.47\%) suffered from MetS at baseline. The incidence density of NAFLD in patients with MetS ( 17.39 per 100 personyears, 1089/6264) was significantly higher than that in the non-MetS group ( 6.81 per 100 person-years, 2558/ 37572 ).

## Bidirectional associations between NAFLD and MetS analysed by GEE models

The multiple GEE analyses for subcohorts A and B, adjusting for the potential confounding factors selected by simple GEE models, are presented in figure 2, online supplementary tables S2 and S3. They revealed that NAFLD was a strong potential risk factor for MetS (relative risks (RRs) and $95 \%$ CI $5.23,3.50$ to 7.81 ) and its components (obesity, diabetes, hypertension and dyslipidemia), while MetS and its components were also potential predictors for NAFLD, with obesity the largest effect (shown in figure 2).

## Reciprocal causal inference by BN

Based on the proposed simplification criteria in the Materials and methods section, the simplified BN from NAFLD to MetS retained 14 nodes, 33 edges and 36 pathways (shown in figure 3) from the primary network (see online supplementary figure S1). The total effects of NAFLD on MetS or its components are summarised in table 3, indicating that the total effect was greatest on dyslipidemia, followed by obesity, diabetes, hypertension and MetS.

The relative importance from the viewpoints of pathogenesis for the pathway from NAFLD to MetS is shown in online supplementary table S4, with their ranking effects by conditional distribution with all the variables set to the highest level. Generally, the most important pathway was that NAFLD led to elevated GGT, then to dyslipidaemia, followed by hypertension and, finally, the incidence of MetS. The second important pathway was that persistent NAFLD led to obesity, then to diabetes, or dyslipidaemia or hypertension and, finally, to MetS. The elevated CHOL level in the pathway would result in a decrease in the incidence of MetS.

However, a single-causal pathway had less public health significance due to the relatively lower exposure rate of the risk factors through each pathway in the population. Take the typical pathway of NAFLD, GGT1,

Table 2 Baseline characteristics of participants in subcohorts A and B


*Non-normal distributed variables were presented as median (25th, 75th centile), and the p values were calculated using non-parametric test.

![img-2.jpeg](img-2.jpeg)

Figure 2 Relative risks (RRs) and 95\% CIs of developing MetS or its components having NAFLD at baseline (hollow diamond, subcohort A), and developing NAFLD having MetS or its components at baseline (solid diamond, subcohort B). The RRs were calculated from the multiple generalised estimating equation (GEE) analyses, adjusting for the potential confounding factors selected by simple GEE model.

GGT2, dyslipidemia, hypertension and MetS as an example, which was a local structure extracted from a simplified network. The conditional probability was calculated to arrive at the indirect effect of this specific pathway (as shown in figure 4). In this pathway, GGT and dyslipidemia were key factors for the development of MetS in pathogenesis, but its effect was very small $(0.025 \%)$ in the population, with less public health significance.

The simplified causal BN from MetS to NAFLD retained 17 nodes and 98 pathways (shown in figure 5).

The total effect of MetS and its component on NAFLD are shown in table 3; it revealed that MetS had the largest effect, followed by obesity, diabetes, dyslipidemia and hypertension. The relative importance of these pathways is shown in online supplementary table S5, and indicates that the dominant causal pathway is that dyslipidaemia leads to other MetS components and finally results in NAFLD.

## DISCUSSION

To the best of our knowledge, this has been the first large-scale bidirectional longitudinal cohort study to clarify the reciprocal causality between NAFLD and MetS within the same study population. We confirmed that NAFLD could be both a cause and consequence of MetS in this bidirectional longitudinal cohort from a section of the Chinese population. As for the results of the longitudinal association between NAFLD and MetS, similar results have been found in other national and regional populations for the temporal sequence of NAFLD to MetS ${ }^{15} 1622-29$ and MetS to NAFLD. ${ }^{29-34}$ Furthermore, we found that the effect of MetS on NAFLD was higher than that of NAFLD on MetS in reciprocal causality between NAFLD and MetS.

The simplified BN was constructed to infer the reciprocal causality between NAFLD and MetS. The total effect of NAFLD on MetS was $2.49 \%$, while it was $19.92 \%$ for MetS on NAFLD, in the framework of causal network, indicating that the effect of MetS on NAFLD
![img-3.jpeg](img-3.jpeg)

Figure 3 Simplified Bayesian network from NAFLD to MetS retained 14 nodes, 33 edges and 36 pathways. The numbers ' 1 ' and ' 2 ' associated with the variables denote the status at baseline and at the end of follow-up, respectively.

Table 3 Total effects of NAFLD to MetS or MetS to NAFLD


was higher than that of NAFLD on MetS. This unbalanced causal effect was consistent with unbalanced incidence densities observed in the bidirectional subcohort. However, the effect of NAFLD on MetS and its components was different, with the effect on dyslipidemia the largest ( $\mathrm{AR} \%=10.15 \%$ ), followed by that on obesity ( $7.63 \%$ ), diabetes ( $3.90 \%$ ) and hypertension ( $3.51 \%$ ). Similar patterns were inferred for the effect of MetS components on NAFLD. The result of the BN was similar to the above GEE analysis results. The above results demonstrated that obesity and dyslipidemia were key factors linking NAFLD and MetS. Several studies suggested that obesity was associated with an increased risk of $\mathrm{NAFLD}^{52} 53$ and might also be important in determining the development of MetS. ${ }^{54}$ These viewpoints were confirmed in this study.

Among the 36 causal pathways from NAFLD to MetS, the most important was that NAFLD led to elevated GGT, then to dyslipidaemia, hypertension and, finally, to MetS. GGT hosted the key node in this causal pathway, and participants with elevated GGT levels would have an increased risk for MetS by increasing oxidative stress, insulin resistance and hepatic steatosis. ${ }^{55-60}$ The second
![img-4.jpeg](img-4.jpeg)

Figure 4 Conditional probability and local structure extracted from the simplified network, for calculating the indirect effect of this specific pathway (NAFLD, GGT1, GGT2, dyslipidemia, hypertension and MetS). The numbers ' 1 ' and ' 2 ' associated with the variables denote the status at baseline and at the end of follow-up, respectively.
important causal pathway was that NAFLD led to obesity, then to the other components, and finally resulted in MetS. This was concordant with previous reports, which considered NAFLD and MetS may be linked by fat ectopic accumulation and insulin resistance. ${ }^{89} 2054$

Among the 98 causal pathways from MetS or its components to NAFLD, the dominant causal pathways begin by leading to dyslipidaemia, and finally resulted in NAFLD. In these pathways, dyslipidaemia might cause the increased triglyceride synthesis in liver cells and triglyceride accumulation in the liver, and then block the low-density lipoprotein synthesis, finally resulting in NAFLD. ${ }^{61}$ Although the cause-effect pathogenesis still needs to be clarified in further investigation, the association between haematocrit and NAFLD has been detected in another Chinese population, ${ }^{62}$ and haemoglobin has been identified as a biomarker of NAFLD in some studies. ${ }^{63-65}$

The association between cholesterol and NAFLD (or the metabolic syndrome) has been fairly well established through long-term studies of high levels of serum cholesterol and the incidence of NAFLD, MetS and coronary heart diseases. Surprisingly, in this study, we found that the elevated total cholesterol appearing in the above pathways would result in a lower probability of MetS and NAFLD. This may not be in accordance with the conventional viewpoint. Nevertheless, a meta-analysis reported that serum total cholesterol levels were significantly lower in non-alcoholic steatohepatitis (NASH) than in simple steatosis. ${ }^{66}$ This study concluded that lower cholesterol levels were independently associated with NASH, in addition to the well-known association with MS and IR. However, the mechanistic explanations linking a lower cholesterol level with NAFLD and MetS still need further investigation.

Our study has several limitations. First, the presence of NAFLD was assessed by experienced radiologists using abdominal ultrasonography, and we have no information on the intraobserver or interobserver reliability of ultrasonographic examinations. The diagnosis of NAFLD was not subjected to any semiquantitative indices. ${ }^{67} 68$ Second, owing to the absence of waist circumference

![img-5.jpeg](img-5.jpeg)

Figure 5 Simplified causal Bayesian network from MetS to NAFLD (17 nodes and 98 pathways). The numbers ' 1 ' and ' 2 ' associated with the variables denote the status at baseline and at the end of follow-up, respectively.
measurement in the health check-up programme, the diagnostic criteria of MetS were based on the Chinese medical association diabetes branch, rather than the international standard criteria. Third, because the present study was based on a routine health check-up system in an urban Han Chinese population of Shandong province, generalisability to the general population was uncertain. Further investigation needs to be carried out to confirm the reciprocal causality between NAFLD and MetS in a larger sample of the general population.

## Author affiliations

${ }^{1}$ Department of Biostatistics, School of Public Health, Shandong University, Jinan, Shandong, China
${ }^{2}$ Medical Department, Qilu Hospital of Shandong University, Jinan, Shandong, China
${ }^{3}$ Health Management Center, Shandong Provincial QianFoShan Hospital, Jinan, Shandong, China

Acknowledgements The authors would like to thank all the participants who participated in the study, and the staff working at the Center for Health Management of Shandong Provincial Qianfoshan Hospital and Center for Health Management of Shandong Provincial Hospital.
Contributors FX, CZ and YL designed the study and directed its implementation. XS, HaL and FT performed the clinical examinations and collected the data. YZ, TZ, NZ and HoL analysed the data. YZ and TZ participated in much of the above work and led the writing of the paper.
Funding This work was supported by grants from the National Natural Science Foundation of China (Numbers 81573259, 81273177 and 81273082) and the Natural Science Foundation of Shandong Province (Number ZR2013HQ056).
Competing interests None declared.

Patient consent Obtained.
Ethics approval Ethics Committee of School of Public Health, Shandong University.
Provenance and peer review Not commissioned; externally peer reviewed.
Data sharing statement No additional data are available.
Open Access This is an Open Access article distributed in accordance with the Creative Commons Attribution Non Commercial (CC BY-NC 4.0) license, which permits others to distribute, remix, adapt, build upon this work noncommercially, and license their derivative works on different terms, provided the original work is properly cited and the use is non-commercial. See: http:// creativecommons.org/licenses/by-nc/4.0/
