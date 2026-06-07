## (3) Check for updates

## OPEN ACCESS

EDITED BY
Mathieu Gruet,
Université de Toulon, France
REVIEWED BY
Georges Jabbour,
Qatar University, Qatar
Robin Souron,
Université de Nantes, France
*CORRESPONDENCE
Hongli Jiang,
j92106@sina.com
SPECIALTY SECTION
This article was submitted to Exercise Physiology,
a section of the journal
Frontiers in Physiology
RECEIVED 16 May 2022
ACCEPTED 29 August 2022
PUBLISHED 19 September 2022

## CITATION

Song Y, Chen L, Wang M, He Q, Xue J and Jiang H (2022), The optimal exercise modality and intensity for hemodialysis patients incorporating Bayesian network meta-analysis and systematic review.
Front. Physiol. 13:945465.
doi: 10.3389/fphys.2022.945465
COPYRIGHT
(c) 2022 Song, Chen, Wang, He, Xue and Jiang. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## The optimal exercise modality and intensity for hemodialysis patients incorporating Bayesian network meta-analysis and systematic review

Yangyang Song, Lei Chen, Meng Wang, Quan He, Jinhong Xue and Hongli Jiang*

Dialysis Department of Nephrology Hospital, The First Affiliated Hospital of Xi'an Jiaotong University, Xi'an, China

Background: Physical inactivity is highly prevalent in patients with hemodialysis, and a large body of evidence reported the positive effect of different exercise modalities on their health outcomes. However, the effective dosage of exercise for hemodialysis patients still requires verification.

Objective: We aimed to determine the most effective exercise intensity and modality for improvements in physical function, blood pressure control, dialysis adequacy, and health-related quality of life for hemodialysis patients.

Design: Systematic review with network meta-analysis of randomized trials.
Data sources: Five electronic databases (PubMed, EMBASE, Web of Science, Cochrane CENTRAL, and Scopus) were searched for randomized controlled trials. Data extraction and quality appraisal were conducted by two authors independently. Data were analyzed by the R (version.3.6.2) and the Stata (version.15.0).

Result: We included 1893 patients involving four exercise modalities and six exercise intensities. Combined training (aerobic exercise plus resistance exercise) has been the top-ranking exercise modality for improving the 6min walk test (6MWT) (surface under the cumulative ranking curve analysis (SUCRA) score, 90.63), systolic blood pressure control (SUCRA score, 77.35), and diastolic pressure control (SUCRA score, 90.56). Moreover, the top-ranking exercise intensity was moderate-vigorous for 6MWT (SUCRA score, 82.36), systolic blood pressure (SUCRA score, 77.43), and diastolic blood pressure (SUCRA score, 83.75). Regarding dialysis adequacy and health-related quality of life, we found no exercise modality or intensity superior to the placebo.

[^0]
[^0]:    Abbreviations: ACSM, American College of Sports Medicine; RCT, randomized clinical trial; 6MWT, 6min walk test; AT, aerobic training; RT, resistance training; CT, combined training; EMS, electrostimulation; CN, control group; BP, blood pressure; L, light intensity; LM, light-moderate; M, moderate; MV, moderate-vigorous; V, vigorous; A, according to the patient's needs; MH, mental health; PH, physical health; MD, mean difference.

Conclusion: This network meta-analysis indicated that combined training and moderate--vigorous intensity might be the most effective interventions to improve 6MWT and blood pressure control. This finding helps further guide clinical exercise prescriptions for hemodialysis patients.

Systematic Review Registration: [<https://www.crd.york.ac.uk/PROSPERO/>], identifier [CRD42021268535].

## Keywords

hemodialysis, blood pressure control, network meta-analysis, dialysis efficiency, exercise dosage

## 1 Introduction

Chronic kidney disease (CKD) is one of the most prevalent global health problems (Collaboration, 2020). The number of CKD patients transitioning to maintenance hemodialysis (HD) has increased in recent years (Yang et al. 2021). Nearly 25 million patients required dialysis therapy in 2020, which is expected to double by 2030 (Liyanage et al. 2015). Hemodialysis has been considered a standard alternative treatment for patients with kidney failure (O'Hare et al. 2003), but it comes along with a higher prevalence of cardiovascular diseases (Ahmadmehrabi and Tang, 2018) and mortality (Robinson et al. 2014). Regular exercise among HD patients was associated with lower mortality risk (Tentori et al. 2010). However, HD patients usually choose a sedentary lifestyle (Stack and Murthy, 2008). The Dialysis Outcomes and Practice Patterns Study (DOPPS), which consisted of 20,920 HD participants in 12 countries, showed that 43.9% never exercised and only 5.7% exercised four to five times per week (Tentori et al. 2010).

Many physiological factors contribute to physical inactivity in HD patients. First, over 80% of HD patients had chronic obstructive pulmonary diseases (Plissier et al. 2016), and cardiovascular diseases (CVDs) exist in nearly 50% of HD patients (Ahmadmehrabi and Tang, 2018). Since cardiac and pulmonary dysfunction significantly reduces absolute ventilation, HD patients can hardly increase ventilation in response to activity (Fedeli et al. 2017; Rangaswami et al. 2019; McGuire et al. 2020). Second, the prevalence of sarcopenia among HD patients was up to 65% (D'alessandro et al. 2018). HD-related sarcopenia was associated with reduced exercise capacity (Hirai et al. 2016; Kirkman et al. 2021). Third, malnutrition, anemia, and iron deficiencies were common complications of HD patients, lowering the oxygen-carrying and aerobic capacity (Hannan and Bronas, 2017; Macdougall, 2017). Other factors related to HD patients' exercise intolerance include fear of injuries, symptoms of debilitation, and fatigue (Delgado and Johansen, 2012; Wang et al. 2020).

Previous evidence demonstrated that exercise could improve cardiovascular function, physical function, and quality of life and relieve restless legs syndrome, muscle cramping, and fatigue for HD patients (Ferrari et al. 2020; Hargrove et al. 2021). Most systematic reviews have compared the control group with different exercise modalities (e.g. aerobic training, resistance training, and aerobic exercise plus resistance training) on physical function, cardiovascular health, and hemodialysis efficiency (Sheng et al. 2014; Ferreira et al. 2019; Ferrari et al. 2020). Some systematic reviews showed that resistance training (RT) and electrostimulation (EMS) could improve the 6-min walk distance (Ferrari et al. 2020). The 6MWT was one of the most commonly used tools for evaluating exercise capacity and endurance (Vogiatzaki et al. 2022). The change of 6MWT was also considered a sensitive indicator for assessing the effectiveness of an exercise intervention on hemodialysis patients (Kono et al. 2014). Aerobic training (AT) can improve HD efficiency (Ferreira et al. 2019). Another systematic review demonstrated that RT and combined training (CT: aerobic exercise plus resistance training) has no effect on 6MWT, only AT can improve 6MWT, and exercise has no effect on blood pressure control (Huang et al. 2019). Although these results have verified the effectiveness of exercise among HD patients, they are controversial. Few studies have compared the effect of different modalities on HD patients. Only one network meta-analysis (Scapini et al. 2019) compared the effect of three exercise modalities simultaneously, but the heterogeneity was high in this systematic review. As an attractive strategy, EMS was less investigated. We have no idea which specific exercise modality is appropriate for patients.

There is also a dose--response relationship between exercise intensity and health outcomes for HD patients. First, some trials showed that compared to those with low exercise intensity, higher intensity could contribute to improvements in cardiovascular outcomes among hemodialysis patients (Tzvetanov et al. 2014; Greenwood et al. 2015; Chan et al. 2018). Some trials showed that moderate and vigorous exercise could improve aerobic capacity and health-related quality of life and lower blood pressure (Reboredo et al. 2011). On the other hand, “morphologic muscle threshold” might explain the phenomenon that exercise does not affect hemodialysis efficiency (Parsons et al. 2006; Pellizzaro et al. 2013). Exercise must exceed a certain threshold to increase enough

muscle blood flow and enlarge the capillary surface and then contribute to circulating toxins transferred to the intravascular compartment and removed by dialysis (Brown et al. 2018; Andrade et al. 2019). However, no systematic review or meta-analysis is available to compare the effect of various training intensities on HD patients' health outcomes.

Due to variations in evidence and limited guidelines, it was an ongoing challenge for dialysis clinicians to support structured exercise programs as routine care (Salhab et al. 2019). Most dialysis physicians (85%) and nurses (83.3%) had no experience with interventional exercise programs for HD patients (Michou et al. 2019). The development of exercise programs has been largely overlooked for HD patients (Regolisti et al. 2018; Lambert et al. 2022) and falls far behind that of other chronic diseases (obesity, diabetes, stroke, and hypertension), for which the consensus for exercise prescription or guideline had already been established (Hansen et al. 2018; Kim et al. 2019; Teich et al. 2019; Alpsoy, 2020).

To our knowledge, there was little evidence about the optimal exercise modality and intensity for HD patients. Specific exercise prescriptions for hemodialysis patients should be designed by physical therapists and facilitate physical exercise for HD patients. To address the knowledge gap, we conducted a Bayesian network meta-analysis combining all available direct and indirect evidence across trials to compare the effect of various exercise modalities and intensities. Our research question for this systematic review was as follows: which specific exercise modality and intensity is the optimal exercise intervention to improve physical capacity, dialysis efficiency, blood pressure control, and health-related quality of life?

## 2 Methods

### 2.1 Literature search and selection criteria

The network meta-analysis was conducted in agreement with the PRISMA network meta-analysis (PRISMA-NMA) (Hutton et al. 2016), and it has been registered in the PROSPERO database (registration number ID: CRD42021268535).

We searched PubMed, EMBASE, Web of Science, Cochrane CENTRAL, and Scopus (from their inception date to 12 June 2022). The following keywords or combinations were used: exercise, aerobic exercise, resistance exercise, electrostimulation, hemodialysis, and chronic kidney disease. The complete search strategy used in PubMed is shown in Supplementary Appendix S1. Trials were also included by manually searching the reference lists of relevant reviews. We have no restrictions on the language of the publications.

We screened all included RCTs according to the criteria of the PICOS (participants, interventions, comparators, outcomes, and study design). The population group of interest was adults (≥18 years) with a chronic renal disease requiring hemodialysis. Interventions are exercise training such as aerobic training (AT), resistance training (RT), combined training (CT), and electrostimulation (EMS). The control group means the nonexercise training group. We included studies that have at least one of the outcome measures: physical function (6-min walk distance) and blood pressure (systolic blood pressure and diastolic blood pressure). The 6MWT is inexpensive, safe, and easier to perform and repeat, even though it is less sensitive to detect physical performance changes than the cardiopulmonary exercise test (Galie et al. 2016). The American Thoracic Society guideline advised that (Uszko-Lencer et al. 2017) the 6MWT was the gold standard tool to assess functional exercise capacity and activities of daily living, and moreover, it is better tolerated for chronic diseases than other walk tests (such as some tests needed to reach a speed). The 6MWT has been widely validated to assess exercise capacity in kidney diseases, including end-stage kidney disease (Shi et al. 2017), kidney transplant candidates (Cheng et al. 2020), and non-kidney solid organ transplantation (Kobashigawa et al. 2019). A long cohort also showed that compared to other physical performance assessment tools, only 6MWT was a significant predictor of severe mortality for hemodialysis patients (Vanden Wyngaert et al. 2022). Blood pressures were measured when patients were at rest. HD efficiency was measured using single-pool Kt/V (Churchill and Patri, 2021), the most common measurement for dialysis adequacy worldwide. “K” represents dialyzer urea clearance, “t” means the duration time of a single dialysis session, and “V” is the volume of urea distribution that is equal to total body water (Gotch et al. 2000). The Kidney Disease Outcomes Quality Initiative (KDOQI) guidelines recommended that single-pool Kt/V should be 1.2 or higher (Daugirdas et al. 2015). Moreover, mental- or physical health-related quality of life was measured by the short-form 36 health questionnaire (SF-36), which consisted of physical and mental component dimensions (Kraus et al. 2016). Physical health consisted of four scales (physical function, role physical, bodily pain, and general health), and mental health included four scales (vitality, social functioning, role-emotional, and mental health), and higher scores mean better health status (Turkmen et al. 2012).

### 2.2 Data abstraction

Two authors extracted data from the included trials (Yangyang Song and Lei Chen). The following information was extracted: year of publication, basic characteristics of patients, and details of intervention (exercise modality, intensity, frequency, and duration). The same two authors independently used the Cochrane Collaboration tool (Sterne et al. 2019) to assess the quality of each included trial and included randomized sequence generation, allocation concealment, performance bias, detection bias, incomplete outcome data, selective reporting, and other biases. Any

disagreements were resolved by discussion with the third author (Hongli Jiang).

The trials with AT, RT, and CT were summarized into five intensities: light, light--moderate, moderate, moderate--vigorous, and vigorous, according to ACSM recommendations (Garber et al. 2011; Scharhag-Rosenberger et al. 2015). The indicators of exercise intensity are HR (heart rate), HRR (heart rate reserve), and VO_{2max} or some subjective parameters such as the rating of perceived exertion (RPE). The resistance exercise was classified by repetition maximum (RM). We added an intensity according to the patient's need, which means there was no specific exercise velocity or target heart rate for patients to achieve (Molsted et al. 2004; Pomidori et al. 2016). The classification details of the intensity of each exercise are shown in Supplementary Appendix S2 eTable1. The summarization process was performed by two authors independently. We contacted the authors when the data were unavailable.

### 2.3 Synthesis analysis

We performed a pairwise meta-analysis using a randomeffect model. The mean difference (MD) and a 95% confidence interval (CI) were used as effect estimates among different studies. Heterogeneity was assessed by I^{2} statistics, 0--40%, 40%--60%, 60%--75%, and 75--100%, which indicated low, moderate, substantial, and considerable heterogeneity, respectively (Hutton et al. 2016). The unit-of-analysis error may exist in studies with two or more experimental groups. To overcome this error, we split these trials into two or more groups, with one control group in the pairwise meta-analysis (Andreato et al. 2019).

We performed NMA using a Bayesian framework noninformatively prior to distributions and the Markov chain Monte Carlo method (MCMC). The Bayesian network metaanalysis can provide evidence from direct and indirect comparisons. The model allows comparisons of the different treatments simultaneously. The network plot was generated to represent the connection between each treatment. The lines in the plot represented direct comparisons between two treatments, the width of the lines represented the number of trials, and the size of each node represented the number of participants (Salanti et al. 2011). We ranked the treatments using the surface under the cumulative ranking curve (SUCRA). SUCRA reported the cumulative ranking probabilities and considered the more precise estimation of ranking probabilities (Mbuagbaw et al. 2017). The value of SUCRA close to 1 represented the best intervention (Salanti et al. 2011). We presented the treatment effect and the corresponding 95% CI by league tables.

For each outcome, heterogeneity was evaluated using the I^{2} statistic. The node-splitting approach was used to examine whether there exists any inconsistency between direct and indirect evidence, and the p-value was higher than 0.05, which indicated no significant inconsistency. We would analyze using clinical factors if there does exist statistical inconsistency and heterogeneity. Sensitive analysis was performed by excluding the high risk of trials. We also judged publication bias by inspecting the asymmetry of a comparison-adjusted funnel plot and the p-value of Egger's test. Serial analyses were performed in STATA (Stata version 15.0), R language, and the “RJAGS” package.

Our analyses were based on previously published trials, and there is no need for ethical approval and patient consent.

## 3 Results

### 3.1 Flow of studies through the review

The flow diagram of the included studies is presented in Figure 1. The initial search yielded 4,179 records, and 12 studies were included in the reference lists of published systematic reviews. A total of 780 duplicates were excluded, and 3,411 studies were excluded after abstract screening. A total of 182 studies were retrieved in full text for further consideration. In total, 46 trials were finally included in the qualitative analysis.

### 3.2 Study characteristics and risk of bias assessment

The 46 studies comprised 1893 participants, and the study duration ranged from 8 to 40 weeks. Among the studies included, 1,011 were allocated to exercise training interventions, and 882 were allocated to the non-exercise group. Exercise training interventions included aerobic (n = 417), resistance (n = 282), and combined aerobic and resistance exercise (n = 252), EMS (n = 60).

Nineteen studies compared the effects of AT and the control group (Painter et al. 2002; Tsuyuki et al. 2003; Sakkas et al. 2008; Toussaint et al. 2008; Koh et al. 2010; Reboredo Mde et al. 2010; Wilund et al. 2010; Giannaki et al. 2013; Mohseni et al. 2013; Wu et al. 2014; Groussard et al. 2015; Liao et al. 2016; Pomidori et al. 2016; Cooke et al. 2018; Fernandes et al. 2019; Lin et al. 2021; Perez-Dominguez et al. 2021; Kim et al. 2022; Vogiatzaki et al. 2022). Nine studies evaluated RT and the control group. (Cheema et al. 2007; Pellizzaro et al. 2013; Kirkman et al. 2014; Abreu et al. 2017; Rosa et al. 2018; Dong et al. 2019; Martins do Valle et al. 2020; Gadelha et al. 2021).

Ten studies evaluated CT (DePaul et al. 2002; Molsted et al. 2004; van Vilsteren et al. 2005; Ouzouni et al. 2009; Frih et al. 2017; Huang et al. 2019; Hatef et al. 2020; Yeh et al. 2020; Assawasaksakul et al. 2021; Myers et al. 2021), and three studies evaluated EMS (Roxo et al. 2016; Schardong et al. 2017; Suzuki et al. 2018). In total, 35 studies were two-arm studies, three were three-arm studies (Afshar et al. 2010; Dobsak et al. 2012; McGregor et al. 2018), and two trials were four-arm studies (Kopple et al.

![img-0.jpeg](img-0.jpeg)

FIGURE 1
Flow of studies through the review.

2007; Thompson et al., 2016). The duration of most trials ranged from 8 weeks to 12 months. The exercise duration was 8–12 weeks in 26 trials, 12–24 weeks in 11 trials, and ≥24 weeks in nine trials. The frequency of exercise training per week ranged from 2 to 4 times except for one study, which was performed once per day (Myers et al., 2021). The exercise duration for most trials per session was 30–90 min. The detailed characteristics of included trials are presented in Supplementary Appendix S3 eTable2.

The risk of bias assessment for each study is shown in Supplementary Appendix S4. Most trials are not of high methodological quality. As the included studies involved exercise interventions, it may be difficult to blind patients and investigators, and most trials tend to have unclear risks of performance bias, and eight studies have high risks of detection bias. Random sequence generation was reported in only 20 studies (43.48%), and 26 studies (56.52%) had unclear risks. Allocation concealment in 13 studies (28.26%) was reported, while 32 studies had unclear bias (69.57%). Nearly half of the studies did not report incomplete outcome data (50%). Only ten trials exhibited a low risk of selective outcome reporting (21.73%), and 33 studies (71.74%) had an unclear bias. Twenty studies (43.48%) were judged high or unclear in the domain risk of other bias since they did not report the sample size calculation. It was challenging to explain the result, especially in some studies with small sample sizes.

### 3.3 Pairwise meta-analysis

The detailed results of the pairwise meta-analysis are shown in Supplementary Appendix S5 eTable3. For 6MWT, CT (MD = 4.9, 95% CI = 3.1 to 6.7, I² = 0%), AT (MD = 3.3, 95% CI = 0.7 to 6.0, I² = 0%), and RT (MD = 2.5, 95% CI = 0.56 to 4.5, I² = 0%) reached statistical significance than the control group. However, EMS had limited effect on 6MWT (MD = 2.3, 95% CI = −2.1 to 6.6, I² = 0%). Moderate–vigorous intensity (MD = 4.5, 95% CI = 1.9 to 7.1, I² = 4.8%) is superior in the control group. Moderate (MD = 5.0, 95% CI = 1.80 to 7.7, I² = 0%) and moderate–vigorous intensity (MD = 4.6, 95% CI = 0.80 to 8.4, I² = 0%) are more efficient than light intensity. Regarding Kt/V, no exercise modality and intensity has got statistical significance improvement than the control group.

As for systolic and diastolic blood pressure, no exercise modality significantly reduced systolic or diastolic blood pressure more than the control group. Moderate–vigorous exercise significantly reduced systolic blood pressure (MD = −8.7, 95% CI = −17 to −1.6, I² = 70.8%) and diastolic blood pressure (MD = −4.9, 95% CI = −9.9 to −0.35, I² = 74.2%) than the control group.

For mental health-related quality of life, CT (MD = 3.6, 95% CI = −4.1 to 11.0, I² = 58.8%), AT (MD = 3.8, 95% CI = −2.2 to 10.0, I² = 60.0%), and RT (MD = 5.7, 95% CI = −5.4 to 17.0, I² = 70.3%) did not reach statistical significance than the control

![img-1.jpeg](img-1.jpeg)

group. Moderate (MD = 3.6, 95%CI = −7.6 to 16.0, I² = 84.0%) and moderate-vigorous intensity (MD = 2.4, 95% CI = −4.6 to 9.4, I² = 66.6%) is not superior to that in the control group. For physical health-related quality of life, CT (MD = 3.6, 95% CI = −5.9 to 13.0, I² = 0%), AT (MD = 6.9, 95% CI = −23.0 to 11.0, I² = 77.4%), and RT (MD = 8.7, 95% CI = −3.0 to 21.0, I² = 70.3%) did not reach statistical significance than the control group. Moderate (MD = −0.52, 95% CI = −12.0 to 11.0, I² = 0%) and moderate-vigorous intensity (MD = 5.8, 95% CI = −1.2 to 13.0, I² = 82.9%) is not superior to that in the control group. However, only one trial (Dobsak et al., 2012) compared the effect of intra-dialytic EMS (20 weeks) on health-related quality of life among HD patients, and significant improvement was observed in the mental function (p = 0.001) and physical function (p = 0.006) compared to that in the control group.

### 3.4 Synthesis results of network meta-analysis

Our network analysis of exercise modality was conducted among the four treatments. EMS was difficult to classify based on intensity. Only the studies on AT, RT, or CT were included to estimate the effect of different intensities. The visual network plot was performed to display evidence among different exercise modalities and exercise intensities. All network plots are presented in Figure 2. Each node represented a unique intervention or control group. The lines showed a direct relationship between interventions, and the width was weighted according to the number of trials between them. Figure 3 presents the interventions of mean difference and the 95% credible interval (CrI) in accordance with the control group. Supplementary Appendix S6 illustrates the effect sizes (MD) for all exercise modalities or intensities. Figure 4 shows the corresponding surface under the cumulative ranking curve analysis (SUCRA) in terms of different outcomes.

### 3.4.1 Assessment of heterogeneity and inconsistency for each outcome

There was no significant statistical heterogeneity (I² < 10%) for each exercise modality and intensity; more details are shown in Supplementary Appendix S7 eTable4. The assessment of incoherence global results for each outcome is presented in Supplementary Appendix S8 eTable5. The node split model results indicated no difference between direct and indirect outcomes (p values >0.05). The node-splitting results are presented in Supplementary Appendix S8 eTable6.

### 3.4.2 Network meta-analysis results for 6MWT

Twenty studies that assessed the effect of different exercise modalities on 6MWT were eligible for network analysis. A total of five unique treatments were included in the network plot (Figure 2A). CT (MD = 4.89; 95% CI, 3.02–6.60), RT (MD = 2.50;

![img-2.jpeg](img-2.jpeg)

FIGURE 3

Forest plots for each outcome category represent the comparisons of the active intervention with no intervention (control group). (A): 6MWT-exercise modalities and (B): 6MWT-exercise intensities. (C) Kt/V-exercise modalities. (D): Kt/V-exercise intensities. (E) Systolic blood pressure-exercise modalities. (F): Systolic blood pressure-exercise intensities. (G): Diastolic blood pressure-exercise modalities. (H): Diastolic blood pressure-exercise intensities. (I): Mental health-exercise modalities. (J): Physical health-exercise modalities.

![img-3.jpeg](img-3.jpeg)

FIGURE 4

Schematic details of the treatments according to the surface under the cumulative ranking curve analysis (SUCRA).

95% CI, 0.61–4.48), and AT (MD = 3.53; 95% CI, 1.09–6.01) were more effective than those of the control group (Figure 3A). EMS (MD = 2.23; 95% CI, −2.15–6.61) had no significant effect on 6MWT than in the control group. The result showed that CT is the best treatment with the highest probability (SUCRA score, 90.63).

A total of six unique exercise intensities were included in the network plot (Figure 2B). The light intensity (MD = 2.55; 95% CI, −0.52–5.39), light–moderate intensity (MD = 4.30; 95% CI, −0.53–9.01), and "A" (the intensity was according to the patient's need) had no significant effect on 6MWT than in the control group. The moderate–vigorous intensity (MD = 5.36;

95% CI, 2.99--7.73) showed significantly superior efficacy over the control group (Figure 3B). The moderate--vigorous intensity was more efficient than the light intensity (MD = 2.82; 95% CI, 0.02--5.80) and the vigorous intensity (MD = 3.82; 95% CI, 0.39--7.44). The top-ranked interventions for 6MWT were moderate--vigorous intensity (SUCRA score, 82.36).

### 3.4.3 Network meta-analysis results for hemodialysis efficiency

As for Kt/V, the network plot (Figure 2C) consisted of 21 studies with five different exercise modalities. No difference has been found between the intervention and control groups (Figure 3C). CT had the highest probability (SUCRA score, 90.56) of being the best treatment for this outcome. Twenty studies assessed the effect of seven different exercise intensities for Kt/V. The network plot is shown in Figure 2D. All intensities had a 95% CrI including the zero effect (Figure 3D). Light-intensity exercise was the most effective treatment (SUCRA score, 83.92).

To evaluate the effect of intradialytic exercise on improving Kt/V, we also conducted an analysis that only included studies in which the intervention was intra-dialytic exercise. Twenty studies were included in the analysis. The results showed that even intradialytic exercise exhibited no significant effect on improving Kt/V. The details of forest plots are presented in Supplementary Appendix S9. AT had the highest probability (SUCRA score, 74.14) and was the best treatment for this outcome. Light-intensity exercise was the most effective treatment (SUCRA score, 83.93).

### 3.4.4 Network meta-analysis results for blood pressure

In the network meta-analysis of blood pressure, 21 studies on exercise modality's effects and nineteen studies on different exercise intensities were included. Only two network plots of exercise modality (Figure 2E) and exercise intensity (Figure 2F) were presented for blood pressure because all studies simultaneously measured both systolic and diastolic blood pressure.

In the network meta-analysis of systolic blood pressure, none of the exercise training modalities was more effective than the control group (Figure 3E). Moderate--vigorous exercise intensity (MD = -7.33, 95% CI, -14.08, 1.25) was more effective in reducing systolic blood pressure than in the control group (Figure 3F). CT had the highest probability (SUCRA score, 77.35) and was the best treatment for systolic pressure control. Moderate--vigorous exercise intensity (SUCRA score, 77.43) has the best intensity for systolic pressure control.

In the network meta-analysis of diastolic blood pressure, all exercise modalities were statistically equivalent to the control group (Figure 3G). CT had the probability (SUCRA score, 69.15) to be the best treatment. Moderate--vigorous exercise intensity (MD = -4.13, 95% CI, -7.93, -0.64) was more effective in reducing systolic blood pressure than in the control group. The other exercise intensities had a 95% CrI, including the zero effect (Figure 3H). The moderate--vigorous intensity (SUCRA score, 83.75) was the best for diastolic blood pressure control.

### 3.4.5 Network meta-analysis results for health-related quality of life

In the network meta-analysis of health-related quality of life, nineteen studies on the effect of exercise modalities and sixteen studies on different exercise intensities were included. The network plots of exercise modality (Figure 2G; Figure 2H) were presented for mental- and physical health-related quality of life.

We did not conduct a network analysis about the effect of different exercise intensities on health-related quality of life. All the included studies compared the effect of different exercise intensities with that of the control group, and no study compared the effect of various training intensities on health-related quality of life. Therefore, it was unable to form a connected network and cannot satisfy the connectivity assumption of network analysis (Higgins et al. 2012; Watt et al. 2019).

In the network meta-analysis of mental health-related quality of life, none of the exercise training modalities was more effective than those of the control group (Figure 3I). CT (MD = 4.46; 95% CI, -2.29--11.51), RT (MD = 5.62; 95% CI,-3.57--15.18), and AT (MD = 3.95; 95% CI, -1.49--10.00) were not effective compared with those in the control group (Figure 3I). EMS (MD = 6.32; 95% CI, -6.08--19.04) had no significant effect on mental health quality than in the control group. EMS had the highest probability (SUCRA score, 67.48) and was the best treatment for mental health-related quality of life.

In the network meta-analysis of physical health quality, all exercise modalities, except AT, were statistically equivalent to the control group (Figure 3J). CT (MD = 4.33; 95% CI, -4.21--13.02), RT (MD = 9.13; 95% CI, 1.12 to -19.59) had no statistical effect than the control group. AT (MD = 7.26; 95% CI, 0.33--13.8) was more effective than the control group (Figure 3J). EMS (MD = -4.95; 95% CI, -20.73 to 10.91) had no significant effect on physical health quality than the control group. RT had the probability (SUCRA score, 76.79) to be the best treatment.

### 3.4.6 Publication bias and sensitivity analysis for each outcome

The comparison-adjusted funnel plots were symmetrically distributed and showed no publication bias. Egger's test revealed no publication bias, and the p-value was higher than 0.05 for all outcomes, except for the exercise modality of 6MWT. There was evidence of publication bias (p = 0.02). The results are shown in Supplementary Appendix S10. We conducted a sensitivity analysis for all outcomes, and the results did not change when

we excluded the high-risk studies. The result is presented in Supplementary Appendix S11.

## 4 Discussion

The network meta-analysis method has been used to explore the optimal exercise modality or intensity in some chronic diseases, such as obesity (Chang et al., 2021) and diabetes (Schwingshackl et al., 2014). Only a network meta-analysis (Scapini et al., 2019) has compared the effectiveness of different exercise modalities (AT, RT, and CT) with placebo on physical function, blood pressure, and hemodialysis efficiency among HD patients. That review needs to be updated, and it took no account of exercise intensity. Our research provided more comparisons and trials to comprehensively assess the effect of different exercise modalities. We also added a new outcome indicator, quality of life, in the current study. More importantly, our study is the first network meta-analysis to compare the effectiveness of different exercise intensities for HD patients.

In the current study, we compared the effect of various exercise modalities and intensities on different outcomes for hemodialysis patients. Most included trials last 4-6 months (3 sessions/weeks) and $30-50 \mathrm{~min}$ per session. The result showed some interesting findings, and we recommended that combined training (CT) and moderate-vigorous intensity are the optimal exercise modality and intensity for improving physical function and controlling blood pressure in HD patients.

Although the method of evaluating exercise intensity (light, moderate, and vigorous) has been widely used in the previous literature (Garber et al., 2011; Scharhag-Rosenberger et al., 2015), there are no standard definitions and descriptions of moderate-vigorous or light-moderate intensity exercise. However, physical activity of moderate-vigorous intensity is commonly recommended for health benefits in health guidelines (Tremblay et al., 2011). This ambiguity also makes it difficult for practitioners to offer accurate exercise advice. In order to improve the generalization of MV, a recent review by Brian (MacIntosh et al., 2021) suggested that the rating of perceived exertion might be a practical and effective measurement to define moderate-vigorous exercise. Therefore, the current study defined the moderate-vigorous intensity as RPE at 12-16 and the light-moderate intensity as RPE at 11-13. Meanwhile, based on the previous literature (Yoshioka et al., 2021a; Yoshioka et al., 2021b), which conducted exercises on chronic kidney diseases, we defined the MV intensity as higher than 3.0 metabolic equivalents.

Evidence has shown that moderate-vigorous intensity of exercise might benefit kidney function and physical function for patients with chronic diseases. A cross-sectional study (Hara et al., 2021) of 66,603 Japanese patients demonstrated that replacing 1 h of sedentary behavior with moderate-vigorous physical activity ( $\geq 3.0$ metabolic equivalents) could reduce the incidence of chronic kidney diseases by $3-4 \%$. Some studies (Yoshioka et al., 2021a; Yoshioka et al., 2021b) demonstrated that a slight increase ( $10 \mathrm{~min} /$ day) in the time of moderate-vigorous intensity exercise ( $\geq 3.0$ metabolic equivalents) contributes to maintaining skeletal muscle strength and isometric knee extension strength in patients with chronic kidney disease, especially attenuating bone density decline. It is to be noted that the amount of moderate-vigorous intensity of exercise might exert different effects. A 10-year cohort (Wang et al., 2021) of 403,681 individuals suggested that participants who performed exercise at moderate-vigorous intensity and those with $50-75 \%$ vigorous intensity exercise had $17 \%$ lower allcause mortality than those with no vigorous exercise. Future work should focus on the amount of moderate-vigorous intensity exercise and whether the proportion of moderate or vigorous intensity exerts different impacts on individuals.

Our results indicated that exercise could positively affect 6MWT regardless of modality and intensity. The most remarkable improvement was observed in exercise mortality with combined exercise and moderate-vigorous intensity. This finding was in agreement with that of another traditional metaanalysis that showed that exercise could increase at least 60 m for 6MWT (Ferrari et al., 2020). The 6MWT could reflect the ability to perform daily life activities and assess the global exercise responses. The previous meta-analysis suggested that 6MWT was sensitive as $\mathrm{VO}_{2}$ to evaluate exercise capacity and the effect of exercise among hemodialysis patients (Huang et al., 2019). Another meta-analysis (Gomes Neto et al., 2018) showed that all types of exercise improved the 6MWT distance among hemodialysis patients. It is critical to improving physical function for HD patients, characterized as 6MWT, which has been an independent mortality predictor of increased cardiovascular events (Sietsema et al., 2004). A 3-year followup showed that an increase of 20 walked meters in 6MWT among HD patients can reduce all-cause death by $12 \%$, all-cause hospitalizations by $4 \%$, and fatal and non-fatal cardiovascular events by $7 \%$ (Torino et al., 2014).

Our result showed that exercise had a limited effect on $\mathrm{Kt} / \mathrm{V}$. The result was consistent with that of previous systematic reviews (Salhab et al., 2019; Scapini et al., 2019). This might mean that exercises, regardless of modality or intensity, might not be able to improve hemodialysis efficiency or $\mathrm{Kt} / \mathrm{V}$ was not the optimal measurement to evaluate the effect of exercise on hemodialysis efficiency. $\mathrm{Kt} / \mathrm{V}$ represents the clearance of urea, a small solute distributed across plasma membranes (Vanholder et al., 2019). Some studies used the removal of serum potassium, creatinine, $\beta 2-$ microglobulin, or phosphate rather than urea to evaluate HD efficiency (Sampaio et al., 2012; Orcy et al., 2014). A meta-analysis (Ferreira et al., 2019) of three to five studies revealed that aerobic exercise could decrease creatinine levels for HD patients. Another study also found that exercise has no effect on $\mathrm{Kt} / \mathrm{V}$ but had a

significant decrease in serum phosphorus, creatinine, and potassium (Pellizzaro et al. 2013). It is to be noted that a recent review demonstrated that exercise had limited effects on improved small-molecule clearance for HD patients (Kirkman et al. 2019). Since Kt/V has been used in most previous studies, we still choose Kt/V as the measurement for hemodialysis efficiency. Future trials could assess the effect of exercise on the clearance of middle molecules and protein-bound uremic toxins.

The prevalence of hypertension among HD patients was up to 70--90% (Bikos et al. 2018), and uncontrolled hypertension was strongly associated with cardiovascular diseases (Loutradis et al. 2017). Our result found that exercise modalities did not affect blood pressure control, similar to a recent meta-analysis (Huang et al. 2019), which showed that the effect size of exercise on SBP and DBP was -0.18 (-0.42, 0.07) and -0.23 (-0.69, 0.24), respectively. In contrast with our results, another meta-analysis showed that CT could significantly reduce diastolic BP, and AT can improve systolic BP (Ferrari et al. 2020). However, their research showed moderate heterogeneity (44%). Our analysis has low heterogeneity and yields more reliable results.

It is to be noted that our results showed that moderate--vigorous intensity exercise could significantly reduce systolic blood pressure (8 mmHg) and diastolic blood pressure (4 mmHg). Consistent with our results, an 8-year cohort (Diaz et al. 2015) study consisting of 1,311 participants with moderate--vigorous physical activity (≥3.5 metabolic equivalents) had lower hypertension incidence for African--Americans (hazard ratio 0.76; 95% CI 0.58--0.99) compared to those who do not perform exercise. Another research showed that a 2 mmHg decrease in systolic blood pressure could reduce coronary heart disease and stroke in adults with hypertension (Hetwe and Jacobson, 2014). These results might be helpful in management of HD patients.

Our result found that exercise did not affect the mental or physical quality of life among HD patients. Contrary to our results, a systematic review (Huang et al. 2019) suggested that an 8-week exercise regimen could reverse the reduction of physical and mental health-related quality of life (SMD = 0.34, 95% CI: 0.09--0.59 and SMD = 0.27, 95% CI: 0.02--0.51, respectively) among HD patients. However, the metaanalysis only included seven trials (139 participants), and the limited sample size might exist bias. Nevertheless, a review conducted by Gomes Neto et al. (2018) demonstrated that AT could not improve the whole quality of life for HD patients. Previous studies (Sheng et al. 2014; Chung et al. 2017) also showed that AT and RT did not have a significant difference in the mental health-related quality of life. The baseline quality of life scores might cause the discrepancy. Painter et al. (2000)showed that HD patients with baseline physical quality of life (SF-36) scores less than 34 were associated with more remarkable improvement but not found in those with scores higher than 34. We should focus on HD patients with lower baseline quality of life scores who might more easily be affected by exercise.

## 5 Strengths and limitations

The strength of our network meta-analysis is that it provided evidence to guide the exercise of clinical practice for HD patients, which integrated direct and indirect comparisons to compare various modalities and intensities. A significant strength is that we comprehensively estimated the effectiveness of exercise intensities for HD patients. The validated measurement was used to classify the exercise intensities. Moreover, we provided the ranking of different exercise training modalities and intensities based on health outcomes for HD patients. Our evidence can help clinicians to choose the optimal exercise modality and intensity for HD patients. Furthermore, we found no heterogeneity and inconsistency in global and local analysis.

However, there were also some limitations. Most included studies were performed in a single medical center with limited number of patients. Future trials are required to be performed in multiple centers. The included trials did not compare the duration and session of exercise, contributing to difficulty in ascertaining the optimal exercise dose within the current literature. Since most of the included studies failed to report adverse events, this study does not pay attention to the adverse effects of exercise. A meta-analysis with limited trials showed that exercises would not increase the rate of adverse events for HD patients (Chung et al. 2017). Few trials have reported the adherence of patients after the intervention. We failed to explore exercise adherence after the intervention. Clinicians should help patients develop long-term exercise habits.

## 6 Conclusion

The present network analysis included four exercise modalities and six exercise intensities. In conclusion, combined training was the most effective intervention among current exercise interventions, and moderate--vigorous intensity was the most effective intensity in improving 6MWT and blood pressure control. In addition, exercise might not affect Kt/V and quality of life. Clinicians could give the optimal exercise prescription even for hemodialysis patients at home. Supervision was also needed to ensure the right exercise intensity. Future research can be conducted to estimate the clinical effect of exercise duration for HD patients and provide more evidence for clinical practice.

## Author contributions

All authors contributed equally to the development of the manuscript. With regard to specific roles, HJ, MW, and QH supported conceptualization of the manuscript. LC, MW, YS, and JX supported data extraction and data analysis. JX and YS

wrote the manuscript. HJ supported all phases of the manuscript's development.

## Funding

This study was supported by the National Natural Science Foundation of China (No. 82170755).

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors, and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphys. 2022.945465/full#supplementary-material

Chung, Y. C., Yeh, M. L., and Liu, Y. M. (2017). Effects of intradialytic exercise on the physical function, depression and quality of life for haemodialysis patients: A systematic review and meta-analysis of randomised controlled trials. J. Clin. Nurs. 26 (13-14), 1801-1813. doi:10.1111/jocn. 13514

Churchill, B. M., and Patri, P. (2021). The nitty-gritties of kt/vurea calculations in hemodialysis and peritoneal dialysis. Indian J. Nephrol. 31 (2), 97-110. doi:10.4103/ ijn.JJN_245_19

Collaboration, G. B. D. C. K. D. (2020). Global, regional, and national burden of chronic kidney disease, 1990-2017: A systematic analysis for the global burden of disease study 2017. Lancet 395 (10225), 709-733. doi:10.1016/S0140-6736(20) 30045-3

Cooke, A. B., Ta, V., Iqbal, S., Gomez, Y. H., Mavrakanas, T., Barre, P., et al. (2018). The impact of intradialytic pedaling exercise on arterial stiffness: A pilot randomized controlled trial in a hemodialysis population. Am. J. Hypertens. 31 (4), 458-466. doi:10.1093/ajh/hpx191

D'alessandro, C., Piccoli, G. B., Barsotti, M., Tassi, S., Giannese, D., Morganti, R., et al. (2018). Prevalence and correlates of sarcopenia among elderly CKD outpatients on tertiary care. Nutrition 10 (12), 1951. doi:10.3390/nu10121951

Daugirdas, J. T., Depner, T. A., Inrig, J., Mehrotra, R., Rocco, M. V., Suri, R. S., et al. (2015). Kdoqi clinical practice guideline for hemodialysis adequacy: 2015 update. Am. J. Kidney Dis. 66 (5), 884-930. doi:10.1053/j.ajkd.2015.07.015

Delgado, C., and Johansen, K. L. (2012). Barriers to exercise participation among dialysis patients. Nephrol. Dial. Transpl. 27 (3), 1152-1157. doi:10.1093/ndt/gfx402

DePaul, V., Moreland, J., Eager, T., and Clase, C. M. (2002). The effectiveness of aerobic and muscle strength training in patients receiving hemodialysis and EPO: A randomized controlled trial. Am. J. Kidney Dis. 40 (6), 1219-1229. doi:10.1053/ajkd. 2002.36887

Dias, K. M., Veerabhadrappa, P., Brown, M. D., Whited, M. C., Dubbert, P. M., and Hickson, D. A. (2015). Prevalence, determinants, and clinical significance of masked hypertension in a population-based sample of african Americans: The jackson heart study. Am. J. Hypertens. 28 (7), 900-908. doi:10.1093/ajh/hpu241

Dobsak, P., Homolka, P., Svojanovsky, J., Reichertova, A., Soscek, M., Novakova, M., et al. (2012). Intra-dialytic electrostimulation of leg extensors may improve exercise tolerance and quality of life in hemodialyzed patients. Artif. Organs 36 (1), 71-78. doi:10.1111/j.1525-1594.2011.01302.x

Dong, Z. J., Zhang, H. L., and Yin, L. X. (2019). Effects of intradialytic resistance exercise on systemic inflammation in maintenance hemodialysis patients with sarcopenia: A randomized controlled trial. Int. Urol. Nephrol. 51 (8), 1415-1424. doi:10.1007/s11255-019-02200-7

Fedeli, U., De Giorgi, A., Gennaro, N., Ferroni, E., Gallerani, M., Mikhaifidis, D. P., et al. (2017). Lung and kidney: A dangerous liaison? A population-based cohort study in copd patients in Italy. Int. J. Chron. Obstruct. Pulmon. Dis. 12, 443-450. doi:10.2147/COPD.S119390

Fernandes, A. O., Sens, Y., Xavier, V. B., Miorin, L. A., and Alves, V. (2019). Functional and respiratory capacity of patients with chronic kidney disease undergoing cycle ergometer training during hemodialysis sessions: A randomized clinical trial. Int. J. Nephrol. 2019, 7857824. doi:10.1155/2019/7857824

Ferrari, F. J, Helal, L., Dipp, T., Soares, D., Soldatelli, A., Mills, A. L., et al. (2020). Intradialytic training in patients with end-stage renal disease: A systematic review and meta-analysis of randomized clinical trials assessing the effects of five different training interventions. J. Nephrol. 33 (2), 251--266. doi:10.1007/s40620-019-00687-y

Ferreira, G. D., Bohlke, M., Correa, C. M., Dias, E. C., Orcy, R. B., and rehabilitation (2019). Does intradialytic exercise improve removal of solutes by hemodialysis? A systematic review and meta-analysis. Arch. Phys. Med. Rehabil. 100 (12), 2371--2380. doi:10.1016/j.apmr.2019.02.009

Frih, B., Jaafar, H., Mkacher, W., Roe Salah, Z., Hammami, M., and Frih, A. (2017). The effect of interdialytic combined resistance and aerobic exercise training on health related outcomes in chronic hemodialysis patients: The Tunisian randomized controlled study. Front. Physiol. 8, 288. doi:10.3389/fphys.2017.00288

Gadelha, A. B., Cesari, M., Correa, H. L., Neves, R. V. P., Sousa, C. V., Deus, L. A., et al. (2021). Effects of pre-dialysis resistance training on sarcopenia, inflammatory profile, and anemia biomarkers in older community-dwelling patients with chronic kidney disease: A randomized controlled trial. Int. Urol. Nephrol. 53 (10), 2137--2147. doi:10.1007/s11255-021-02799-6

Galie, N., Humbert, M., Vachiery, J. L., Gibbs, S., Lang, I., Torbicki, A., et al. (2016). 2015 ESC/ERS guidelines for the diagnosis and treatment of pulmonary hypertension: The joint task force for the diagnosis and treatment of pulmonary hypertension of the European society of cardiology (ESC) and the European respiratory society (ERS): Endorsed by: Association for European paediatric and congenital cardiology (AEPC), international society for heart and lung transplantation (ISHLT). Eur. Heart J. 37 (1), 67--119. doi:10.1093/eurheartj/ehv317

Garber, C. E., Blissmer, B., Deschenes, M. R., Franklin, B. A., Lamonte, M. J., Lee, I. M., et al. (2011). American College of Sports medicine position stand. Quantity and quality of exercise for developing and maintaining cardiorespiratory, musculoskeletal, and neuromotor fitness in apparently healthy adults: Guidance for prescribing exercise. Med. Sci. Sports Exerc. 43 (7), 1334--1359. doi:10.1249/MSS. 0b013e318213fefb

Giannaki, C. D., Hadjigeorgiou, G. M., Karatzaferi, C., Maridaki, M. D., Koutedakis, Y., Founta, P., et al. (2013). A single-blind randomized controlled trial to evaluate the effect of 6 months of progressive aerobic exercise training in patients with uraemic restless legs syndrome. Nephrol. Dial. Transpl. 28 (11), 2834--2840. doi:10.1093/ndt/glt288

Gomes Neto, M., de Lacerda, F. F. R., Lopes, A. A., Martinez, B. P., and Saquetto, M. B. (2018). Intradialytic exercise training modalities on physical functioning and health-related quality of life in patients undergoing maintenance hemodialysis: Systematic review and meta-analysis. Clin. Rehabil. 32 (9), 1189--1202. doi:10.1177/0269215518760380

Gotch, F. A., Sargent, J. A., and Keen, M. L. (2000). Whither goest Kt/V? Kidney Int. Suppl. 76, S3--S18. doi:10.1046/j.1523-1755.2000.07602.x

Greenwood, S. A., Koulaki, P., Mercer, T. H., Raab, R., O'Connor, E., Tuffnell, R., et al. (2015). Aerobic or resistance training and pulse wave velocity in kidney transplant recipients: A 12-week pilot randomized controlled trial (the exercise in renal transplant [ExeRT] trial). Am. J. Kidney Dis. 66 (4), 689--698. doi:10.1053/j. ajkd.2015.06.016

Groussard, C., Rouchon-Jesard, M., Coutard, C., Romain, F., Malarde, L., Lemoine-Morel, S., et al. (2015). Beneficial effects of an intradialytic cycling training program in patients with end-stage kidney disease. Appl. Physiol. Nutr. Metab. 40 (6), 550--556. doi:10.1139/apnm-2014-0357

Hannan, M., and Bronas, U. G. (2017). Barriers to exercise for patients with renal disease: An integrative review. J. Nephrol. 30 (6), 729--741. doi:10.1007/s40620-017-0420-z

Hansen, D., Niebauer, J., Cornelissen, V., Barna, O., Neunhauserer, D., Stettler, C., et al. (2018). Exercise prescription in patients with different combinations of cardiovascular disease risk factors: A consensus statement from the expert working group. Sports Med. 48 (8), 1781--1797. doi:10.1007/s40279-018-0930-4

Hara, M., Nishida, Y., Tanaka, K., Shimaswa, C., Koga, K., Furukawa, T., et al. (2021). Moderate-to-vigorous physical activity and sedentary behavior are independently associated with renal function: A cross-sectional study. J. Epidemiol. 10 (16), JE20210155. doi:10.2188/jee. JE20210155

Hargrove, N., El Tobgy, N., Zhou, O., Pinder, M., Plant, B., Askin, N., et al. (2021). Effect of aerobic exercise on dialysis-related symptoms in individuals undergoing maintenance hemodialysis: A systematic review and meta-analysis of clinical trials. Clin. J. Am. Soc. Nephrol. 16 (4), 560--574. doi:10.2215/CJN.15080920

Hatef, M., Mousavinasab, N., Esmaeili, R., Kamali, M., Madani, Z., Spabbodi, F., et al. (2020). The effects of exercise training on physical performance and self-efficacy in hemodialysis patients: A randomized controlled clinical trial. Iran. J. Nurs. Midwifery Res. 25 (6), 520--526. doi:10.4103/ijnmr. IJNMR_28_19

Heiwe, S., and Jacobson, S. H. (2014). Exercise training in adults with CKD: A systematic review and meta-analysis. Am. J. Kidney Dis. 64 (3), 383--393. doi:10. 1053/j.ajkd.2014.03.020

Higgins, J. P., Jackson, D., Barrett, J. K., Lu, G., Ades, A. E., and White, I. R. (2012). Consistency and inconsistency in network meta-analysis: Concepts and models for multi-arm studies. Res. Synth. Methods 3 (2), 98--110. doi:10.1002/jnsm.1044

Hirai, K., Ookawara, S., and Morishita, Y. (2016). Sarcopenia and physical inactivity in patients with chronic kidney disease. Nephrourol. Mon. 8 (3), e37443. doi:10.5812/numonthly.37443

Huang, M., Lv, A., Wang, J., Xu, N., Ma, G., Zhai, Z., et al. (2019). Exercise training and outcomes in hemodialysis patients: Systematic review and metaanalysis. Am. J. Nephrol. 50 (4), 240--254. doi:10.1159/000502447

Hutton, B., Catala-Lopez, F., and Mober, D. (2016). The PRISMA statement extension for systematic reviews incorporating network meta-analysis: PRISMA-NMA. Med. Clin. 147 (6), 262--266. doi:10.1016/j.medch.2016.02.025

Kim, S., Park, H. J., and Yang, D. H. (2022). An intradialytic aerobic exercise program ameliorates frailty and improves dialysis adequacy and quality of life among hemodialysis patients: A randomized controlled trial. Kidney Res. Clin. Pract. 41 (4), 462--472. doi:10.23876/j.krcp.21.284

Kim, T., Lai, B., Mehta, T., Thirumalai, M., Padalabalanarayanan, S., Rimmer, J. H., et al. (2019). Exercise training guidelines for multiple sclerosis, stroke, and Parkinson disease: Rapid review and synthesis. Am. J. Phys. Med. Rehabil. 98 (7), 613--621. doi:10.1097/PHM.0000000000001174

Kirkman, D. L., Bohnke, N., Carbone, S., Garten, R. S., Rodriguez-Miguelez, P., Franco, R. L., et al. (2021). Exercise intolerance in kidney diseases: Physiological contributors and therapeutic strategies. Am. J. Physiol. Ren. Physiol. 520 (2), F161--F173. doi:10.1152/ajprenal.00437.2020

Kirkman, D. L., Mullins, P., Junglee, N. A., Kumwenda, M., Jibani, M. M., and Macdonald, J. H. (2014). Anabolic exercise in haemodialysis patients: A randomised controlled pilot study. J. Cachexia Sarcopenia Muscle 5 (3), 199--207. doi:10.1007/s13539-014-0140-3

Kirkman, D. L., Scott, M., Kidd, J., and Macdonald, J. H. (2019). The effects of intradialytic exercise on hemodialysis adequacy: A systematic review. Semin. Dial. 32 (4), 368--378. doi:10.1111/sdi.12785

Kobashigawa, J., Dadbania, D., Bhorade, S., Ader, D., Berger, J., Bhat, G., et al. (2019). Report from the American Society of Transplantation on frailty in solid organ transplantation. Am. J. Transpl. 19 (4), 984--994. doi:10.1111/ajt.15198

Koh, K. P., Fassett, R. G., Sharman, J. E., Coombes, J. S., and Williams, A. D. (2010). Effect of intradialytic versus home-based aerobic exercise training on physical function and vascular parameters in hemodialysis patients: A randomized pilot study. Am. J. Kidney Dis. 55 (1), 88--99. doi:10.1053/j.ajkd.2009.09.025

Kono, K., Nishida, Y., Moriyama, Y., Yabe, H., Taoka, M., and Sato, T. (2014). Investigation of factors affecting the six-minute walk test results in hemodialysis patients. Ther. Apher. Dial. 18 (6), 623--627. doi:10.1111/1744-9987.12177

Kopple, J. D., Wang, H., Casaburi, R., Fournier, M., Lewis, M. I., Taylor, W., et al. (2007). Exercise in maintenance hemodialysis patients induces transcriptional changes in genes favoring anabolic muscle. J. Am. Soc. Nephrol. 18 (11), 2975--2986. doi:10.1681/ASN.2006070794

Kraus, M. A., Fluck, R. J., Weinhandl, E. D., Kansal, S., Copland, M., Komenda, P., et al. (2016). Intensive hemodialysis and health-related quality of life. Am. J. Kidney Dis. 68 (5S1), S33--S42. doi:10.1053/j.ajkd.2016.05.023

Lambert, K., Lightfoot, C. J., Jegatheesan, D. K., Gabrys, I., and Bennett, P. N. (2022). Physical activity and exercise recommendations for people receiving dialysis: A scoping review. PLoS One 17 (4), e0267290. doi:10.1371/journal.pone. 0267290

Liao, M. T., Liu, W. C., Lin, F. H., Huang, C. F., Chen, S. Y., Liu, C. C., et al. (2016). Intradialytic aerobic cycling exercise alleviates inflammation and improves endothelial progenitor cell count and bone density in hemodialysis patients. Med. Baltim. 95 (27), e4134. doi:10.1097/MD.0000000000004134

Lin, C. H., Hsu, Y. J., Hsu, P. H., Lee, Y. L., Lin, C. H., Lee, M. S., et al. (2021). Effects of intradialytic exercise on dialysis parameters, health-related quality of life, and depression status in hemodialysis patients: A randomized controlled trial. Int. J. Environ. Res. Public Health 18 (17), 9205. doi:10.3390/ijenph18179205

Liyanage, T., Ninomiya, T., Jha, V., Neal, B., Patrice, H. M., Okpechi, I., et al. (2015). Worldwide access to treatment for end-stage kidney disease: A systematic review. Lancet 385 (9981), 1975--1982. doi:10.1016/S0140-6736(14)61601-9

Loutradio, C. N., Tsioufio, C., and Sandidis, P. A. (2017). The clinical problems of hypertension treatment in hemodialysis patients. Curr. Vasc. Pharmacol. 16 (1), 54--60. doi:10.2174/1570161115666170414120921

Macdougall, I. C. (2017). Intravenous iron therapy in patients with chronic kidney disease: Recent evidence and future directions. Clin. Kidney J. 10 (1), i16-i24. doi:10.1093/ckj/sfz043

MacIntosh, B. R., Marias, J. M., Keir, D. A., and Weir, J. M. (2021). What is moderate to vigorous exercise intensity? Front. Physiol. 12, 682233. doi:10.3389/fphys.2021.682233

Martins do Valle, F., Valle Pinheiro, B., Almeida Barros, A. A., Ferreira Mendonca, W., de Oliveira, A. C., de Oliveira Werneck, G., et al. (2020). Effects of intradialytic resistance training on physical activity in daily life, muscle strength, physical capacity and quality of life in hemodialysis patients: A randomized clinical trial. Disabil. Rehabil. 42 (25), 3638-3644. doi:10.1080/09638288.2019.1606857

Mbuaghew, L., Rochwerg, B., Janschke, R., Henb-Andsell, D., Albuzzani, W., Thabane, L., et al. (2017). Approaches to interpreting and choosing the best treatments in network meta-analyses. Syst. Rev. 6 (1), 79. doi:10.1186/s13643-017-0473-z

McGregor, G., Ennis, S., Powell, R., Hamborg, T., Raymond, N. T., Owen, W., et al. (2018). Feasibility and effects of intra-dialytic low-frequency electrical muscle stimulation and cycle training: A pilot randomized controlled trial. PLoS One 13 (7), e0200354. doi:10.1371/journal.pone. 0200354

McGuire, S., Horton, E. J., Renshaw, D., Chan, K., Krishnan, N., and McGregor, G. (2020). Ventilatory and chronotropic incompetence during incremental and constant load exercise in end-stage renal disease: A comparative physiology study. Am. J. Physiol. Ren. Physiol. 319 (3), F515-F522. doi:10.1152/ajprenal.00258.2020

Michou, V., Kouidi, E., Liabopoulos, V., Doumousi, E., and Deligiannis, A. (2019). Attitudes of hemodialysis patients, medical and nursing staff towards patients' physical activity. Int. Urol. Nephrol. 51 (7), 1249-1260. doi:10.1007/s11255-019-02179-1

Mohseni, R., Emami Zeydi, A., Ilali, E., Adib-Hajbaghery, M., and Makhlough, A. (2013). The effect of intradialytic aerobic exercise on dialysis efficacy in hemodialysis patients: A randomized controlled trial. Oman Med. J. 28 (5), 345-349. doi:10.5001/omj.2013.99

Molsted, S., Eidemak, I., Sorensen, H. T., and Kristensen, J. H. (2004). Five months of physical exercise in hemodialysis patients: Effects on aerobic capacity, physical function and self-rated health. Nephron. Clin. Pract. 96 (3), c76-81. doi:10. 1159/000076744

Myers, J., Chan, K., Chen, Y., Lit, Y., Patti, A., Massaband, P., et al. (2021). Effect of a home-based exercise program on indices of physical function and quality of life in elderly maintenance hemodialysis patients. Kidney Blood Press. Res. 46 (2), 196-206. doi:10.1159/000514269

O'Hare, A. M., Tawney, K., Bacchetti, P., and Johansen, K. L. (2003). Decreased survival among sedentary patients undergoing dialysis: Results from the dialysis morbidity and mortality study wave 2. Am. J. Kidney Dis. 41 (2), 447-454. doi:10. 1053/ajkd.2003.50055

Orcy, R., Antunes, M. F., Schiller, T., Seus, T., and Bohlke, M. (2014). Aerobic exercise increases phosphate removal during hemodialysis: A controlled trial. Hemodial. Int. 18 (2), 450-458. doi:10.1111/hdi.12123

Ouzouni, S., Kouidi, E., Sioulis, A., Grekas, D., and Deligiannis, A. (2009). Effects of intradialytic exercise training on health-related quality of life indices in haemodialysis patients. Clin. Rehabil. 23 (1), 53-63. doi:10.1177/ 0269215508096760

Painter, P., Carlson, L., Carey, S., Paul, S. M., and Myll, J. (2000). Low-functioning hemodialysis patients improve with exercise training. Am. J. Kidney Dis. 36 (3), 600-608. doi:10.1053/ajkd.2000.16200

Painter, P., Moore, G., Carlson, L., Paul, S., Myll, J., Phillips, W., et al. (2002). Effects of exercise training plus normalization of hematocrit on exercise capacity and health-related quality of life. Am. J. Kidney Dis. 39 (2), 257-265. doi:10.1053/ ajkd.2002.30544

Parsons, T. L., Toffelmiire, E. B., and King-VanVlack, C. E. (2006). Exercise training during hemodialysis improves dialysis efficacy and physical performance. Arch. Phys. Med. Rehabil. 87 (5), 680-687. doi:10.1016/j. apmr.2005.12.044

Pellizzaro, C. O., Thome, F. S., and Veronese, F. V. (2013). Effect of peripheral and respiratory muscle training on the functional capacity of hemodialysis patients. Ren. Fail. 35 (2), 189-197. doi:10.3109/0886022X.2012.745727

Perez-Dominguez, B., Casana-Granell, J., Garcia-Maset, R., Garcia-Testal, A., Melendez-Oliva, E., and Segura-Orti, E. (2021). Effects of exercise programs on physical function and activity levels in patients undergoing hemodialysis: A randomized controlled trial. Eur. J. Phys. Rehabil. Med. 57 (6), 994-1001. doi:10.23736/S1973-9087.21.06694-6

Plesner, L. L., Warming, P. E., Nielsen, T. L., Dalsgaard, M., Schou, M., Host, U., et al. (2016). Chronic obstructive pulmonary disease in patients with end-stage kidney disease on hemodialysis. Hemodial. Int. 20 (1), 68-77. doi:10.1111/hdi. 12342

Pomidori, L., Lamberti, N., Malagoni, A. M., Manfredini, F., Pozzato, E., Felisatti, M., et al. (2016). Respiratory muscle impairment in dialysis patients: Can minimal dose of exercise limit the damage? A preliminary study in a sample of patients enrolled in the excite trial. J. Nephrol. 29 (6), 863-869. doi:10.1007/s40620-016-0325-2

Rangaswami, J., Bhalla, V., Blair, J. E. A., Chang, T. I., Costa, S., Lentine, K. L., et al. (2019). Cardiorenal syndrome: Classification, pathophysiology, diagnosis, and treatment strategies: A scientific statement from the American heart association. Circulation 139 (16), e840-e878. doi:10.1161/CIR.0000000000000664

Reboredo Mde, M., Pinheiro Bdo, V., Neder, J. A., Avila, M. P., Araujo, E. B. M. L., de Mendonca, A. F., et al. (2010). Efeito de exercício aeróbico durante as sessões de hemodiálise na variabilidade da frequência cardíaca e na função ventricular esquerda em pacientes com doença renal crônica. J. Bras. Nefrol. 32 (4), 372-379. doi:10.1590/S0101-28002010000400006

Reboredo, M. M., Neder, J. A., Pinheiro, B. V., Henrique, D. M., Faria, R. S., and Paula, R. B. (2011). Constant work-rate test to assess the effects of intradialytic aerobic training in mildly impaired patients with end-stage renal disease: A randomized controlled trial. Arch. Phys. Med. Rehabil. 92 (12), 2018-2024. doi:10.1016/j.apmr.2011.07.190

Regolisti, G., Maggiore, U., Sabatino, A., Gandolfini, I., Pieli, S., Torino, C., et al. (2018). Interaction of healthcare staff's attitude with barriers to physical activity in hemodialysis patients: A quantitative assessment. PLoS One 13 (4), e0196313. doi:10.1371/journal.pone. 0196313

Robinson, B. M., Zhang, J. Y., Morgenstern, H., Bradbury, B. D., Ng, L. J., McCullough, K. P., et al. (2014). Worldwide, mortality risk is high soon after initiation of hemodialysis. Kidney Int. 85 (1), 158-165. doi:10.1038/ki.2013.252

Rosa, C., Nishimoto, D. Y., Souza, G. D. E., Ramirez, A. P., Carletti, C. O., Daibem, C. G. L., et al. (2018). Effect of continuous progressive resistance training during hemodialysis on body composition, physical function and quality of life in endstage renal disease patients: A randomized controlled trial. Clin. Rehabil. 32 (7), 899-908. doi:10.1177/0269215518760696

Roux, R. S., Xavier, V. B., Miorin, L. A., Magalhaes, A. O., Sens, Y. A., and Alves, V. L. (2016). Impact of neuromuscular electrical stimulation on functional capacity of patients with chronic kidney disease on hemodialysis. J. Bras. Nefrol. 38 (3), 344-350. doi:10.5935/0101-2800.20160052

Sakkas, G. K., Hadjigeorgiou, G. M., Karatafeti, C., Maridaki, M. D., Giannaki, C. D., Mertens, P. R., et al. (2008). Intradialytic aerobic exercise training ameliorates symptoms of restless legs syndrome and improves functional capacity in patients on hemodialysis: A pilot study. ASAIO J. 54 (2), 185-190. doi:10.1097/MAT.0b013e3181641b07

Salanti, G., Ades, A. E., and Ioannidis, J. P. (2011). Graphical methods and numerical summaries for presenting results from multiple-treatment meta-analysis: An overview and tutorial. J. Clin. Epidemiol. 64 (2), 163-171. doi:10.1016/j.jclinepi. 2010.03.016

Salliah, N., Karavetian, M., Kooman, J., Fisccadori, E., and El Kloury, C. F. (2019). Effects of intradialytic aerobic exercise on hemodialysis patients: A systematic review and meta-analysis. J. Nephrol. 32 (4), 549-566. doi:10.1007/ s40620-018-00565-z

Sampaio, M. S., Ruzany, F., Dorigo, D. M., and Suassuna, J. H. (2012). Phosphate mass removal during hemodialysis: A comparison between eKT/V-matched conventional and extended dialysis. Am. J. Nephrol. 36 (2), 121-126. doi:10. 1159/000338675

Scapini, K. B., Bohlke, M., Moraes, O. A., Rodrigues, C. G., Inacio, J. F. S., Shruzzi, G., et al. (2019). Combined training is the most effective training modality to improve aerobic capacity and blood pressure control in people requiring haemodialysis for end-stage renal disease: Systematic review and network metaanalysis. J. Physiother. 65 (1), 4-15. doi:10.1016/j.jphys.2018.11.008

Schardong, J., Hipp, T., Bozzeto, C. B., de Silva, M. G., Baldissera, G. L., Ribeiro, R. C., et al. (2017). Effects of intradialytic neuromuscular electrical stimulation on strength and muscle architecture in patients with chronic kidney failure: Randomized clinical trial. Arch. Organs 41 (11), 1049-1058. doi:10.1111/aor.12886

Scharhag-Rosenberger, F., Kuehl, R., Klassen, O., Schommer, K., Schmidt, M. E., Ulrich, C. M., et al. (2015). Exercise training intensity prescription in breast cancer survivors: Validity of current practice and specific recommendations. J. Cancer Surviv. 9 (4), 612-619. doi:10.1007/s11764-015-0437-z

Schwingshackl, L., Missbach, B., Dias, S., Konig, J., and Hoffmann, G. (2014). Impact of different training modalities on glycaemic control and blood lipids in patients with type 2 diabetes: A systematic review and network meta-analysis. Diabetologia 57 (9), 1789-1797. doi:10.1007/s00125-014-3303-z

Sheng, K., Zhang, P., Chen, L., Cheng, J., Wu, C., and Chen, J. (2014). Intradialytic exercise in hemodialysis patients: A systematic review and meta-analysis. Am. J. Nephrol. 40 (5), 478-490. doi:10.1159/000368722

Shi, Y., Zheng, D., Zhang, L., Yu, Z., Yan, H., Ni, Z., et al. (2017). Six-minute walk test predicts all-cause mortality and technique failure in ambulatory peritoneal dialysis patients. Nephrol. Gerb. 22 (2), 118-124. doi:10.1111/nep. 12726

Sietsema, K. E., Amato, A., Adler, S. G., and Brass, E. P. (2004). Exercise capacity as a predictor of survival among ambulatory patients with end-stage renal disease. Kidney Int. 65 (2), 719-724. doi:10.1111/j.1523-1755.2004.00411.x

Stack, A. G., and Murthy, R. (2008). Exercise and limitations in physical activity levels among new dialysis patients in the United States: An epidemiologic study. Ann. Epidemiol. 18 (12), 880-888. doi:10.1016/j.annepidem.2008.09.008

Sterne, J. A. C., Savovic, J., Page, M. J., Elbers, R. G., Blencowe, N. S., Boutron, I., et al. (2019). RoB 2: A revised tool for assessing risk of bias in randomised trials. BMJ 366, 16898. doi:10.1136/bmj. 16898

Suzuki, T., Ikeda, M., Minami, M., Matayoshi, Y., Nakao, M., Nakamura, T., et al. (2018). Beneficial effect of intradialytic electrical muscle stimulation in hemodialysis patients: A randomized controlled trial. Artif. Organs 42 (9), 899-910. doi:10.1111/aor. 13161

Teich, T., Zaharieva, D. P., and Riddell, M. C. (2019). Advances in exercise, physical activity, and diabetes mellitus. Diabetes Technol. Ther. 21 (S1), S112. doi:10.1089/dla.2019.2509

Tentori, F., Elder, S. J., Thumma, J., Pisoni, R. L., Bommer, J., Fissell, R. B., et al. (2010). Physical exercise among participants in the dialysis outcomes and practice Patterns study (DOPPS): Correlates and associated outcomes. Nephrol. Dial. Transpl. 25 (9), 3050-3062. doi:10.1093/ndt/glq138

Thompson, S., Klarenbach, S., Molzahn, A., Lloyd, A., Gabrys, I., Haykowsky, M., et al. (2016). Randomised factorial mixed method pilot study of aerobic and resistance exercise in haemodialysis patients: DIALE-SIZE. BMJ Open 6 (9), e012085. doi:10.1136/bmjopen-2016-012085

Torino, C., Manfredini, F., Bolignano, D., Aucella, F., Baggetta, R., Barilla, A., et al. (2014). Physical performance and clinical outcomes in dialysis patients: A secondary analysis of the EXCITE trial. Kidney Blood Press. Res. 39 (2-3), 205-211. doi:10.1159/000355798

Toussaint, N. D., Polkinghorne, K. B., and Kerr, P. G. (2008). Impact of intradialytic exercise on arterial compliance and B-type natriuretic peptide levels in hemodialysis patients. Hemodial. Int. 12 (2), 254-263. doi:10.1111/j.1542-4758. 2008.00262.x

Tremblay, M., Warburton, D., Janssen, I., Paterson, D., Latimer, A., Rhodes, R., et al. (2011). New Canadian physical activity guidelines. Appl. Physiol. Nutr. Metab. 36 (1), 36-46. doi:10.1139/H11-009

Tsoyuki, K., Kimura, Y., Chiachi, K., Matsushita, T., Ninomiya, T., Choh, T., et al. (2003). Oxygen uptake efficiency slope as monitoring tool for physical training in chronic hemodialysis patients. Ther. Apher. Dial. 7 (4), 461-467. doi:10.1046/j. 1526-0968.2003.00084.x

Turkmen, K., Yazici, B., Solak, Y., Guney, I., Altintepe, L., Yeksan, M., et al. (2012). Health-related quality of life, sleep quality, and depression in peritoneal dialysis and hemodialysis patients. Hemodial. Int. 16 (2), 198-206. doi:10.1111/j. 1542-4758.2011.00648.x

Tevetanov, I., West-Thielke, P., D'Amico, G., Johnsen, M., Ladik, A., Hachaj, G., et al. (2014). A novel and personalized rehabilitation program for obese kidney transplant recipients. Transpl. Proc. 46 (10), 3431-3437. doi:10.1016/j.transproceed. 2014.05.085

Uziko-Lencer, N., Mesquita, R., Janssen, E., Werter, C., Brunner-La Rocca, H. P., Pitta, F., et al. (2017). Reliability, construct validity and determinants of 6-minute walk test performance in patients with chronic heart failure. Int. J. Cardiol. 1 (240), 285-290. doi:10.1016/j.ijcard.2017.02.109

van Vliiteren, M. C., de Groef, M. H., and Huisman, R. M. (2005). The effects of a low-to-moderate intensity pre-conditioning exercise programme linked with exercise counselling for sedentary haemodialysis patients in The Netherlands: Results of a randomized clinical trial. Nephrol. Dial. Transpl. 20 (1), 141-146. doi:10.1093/ndt/gfh560

Vanden Wyngaert, K., Van Biesen, W., Eloot, S., Van Craenenbroeck, A. H., Calders, P., and Holvoet, E. (2022). The importance of physical performance in the assessment of patients on haemodialysis: A survival analysis. PLoS One 17 (5), e0268115. doi:10.1371/journal.pone.0268115

Vanholder, B., Van Biesen, W., and Lametre, N. (2019). A swan song for Kt/ Vurea. Semin. Dial. 32 (5), 424-437. doi:10.1111/sdi.12811

Vogiatzaki, E., Michou, V., Liakopoulos, V., Roumeliotis, A., Roumeliotis, S., Kouidi, E., et al. (2022). The effect of a 6-month intradialytic exercise program on hemodialysis adequacy and body composition: A randomized controlled trial. Int. Urol. Nephrol. 5 (23), 1573-2584. doi:10.1007/s11255-022-03238-w

Wang, X. X., Lin, Z. H., Wang, Y., Xu, M. C., Kang, Z. M., Zeng, W., et al. (2020). Motivators for and barriers to exercise rehabilitation in hemodialysis centers: A multicenter cross-sectional survey. Am. J. Phys. Med. Rehabil. 99 (5), 424-429. doi:10.1097/PHM.0000000000001360

Wang, Y., Nie, J., Ferrari, G., Rey-Lopez, J. P., and Rezende, L. F. M. (2021). Association of physical activity intensity with mortality: A national cohort study of 403681 us adults. JAMA Intern. Med. 181 (2), 203-211. doi:10.1001/ jamainternmed.2020.6331

Watt, J., Tricco, A. C., Straus, S., Veroniki, A. A., Naglie, G., and Drucker, A. M. (2019). Research techniques made simple: Network meta-analysis. J. Invest. Dermatol. 139 (1), 4-12. doi:10.1016/j.jid.2018.10.028

Wilund, K. R., Tomayko, E. J., Wu, P. T., Ryong Chung, H., Vallurupalli, S., Lakshminarayanan, B., et al. (2010). Intradialytic exercise training reduces oxidative stress and epicardial fat: A pilot study. Nephrol. Dial. Transpl. 25 (8), 2695-2701. doi:10.1093/ndt/glq106

Wu, Y., He, Q., Yin, X., He, Q., Cao, S., and Ying, G. (2014). Effect of individualized exercise during maintenance haemodialysis on exercise capacity and health-related quality of life in patients with uraemia. J. Int. Med. Res. 42 (3), 718-727. doi:10.1177/0300060513509037

Yang, C., Yang, Z., Wang, J., Wang, H. Y., Su, Z., Chen, R., et al. (2021). Estimation of prevalence of kidney disease treated with dialysis in China: A study of insurance claims data. Am. J. Kidney Dis. 77 (6), 889-897. doi:10.1053/j.ajkd.2020. 11.021

Yeh, M. L., Wang, M. H., Hsu, C. C., and Liu, Y. M. (2020). Twelve-week intradialytic cycling exercise improves physical functional performance with gain in muscle strength and endurance: A randomized controlled trial. Clin. Rehabil. 34 (7), 916-926. doi:10.1177/0269215520921923

Yoshioka, M., Kosaki, K., Matsui, M., Shibata, A., Oka, K., Kuro, O. M., et al. (2021a). Replacing sedentary time for physical activity on bone density in patients with chronic kidney disease. J. Bone Min. Metab. 39 (6), 1091-1100. doi:10.1007/ s00774-021-01255-w

Yoshioka, M., Kosaki, K., Matsui, M., Takahashi, K., Shibata, A., Oka, K., et al. (2021b). Physical activity, sedentary behavior, and skeletal muscle strength in patients with chronic kidney disease: An isotemporal substitution approach. Phys. Ther. 101 (7), pzab101. doi:10.1093/ptj/pzab101)