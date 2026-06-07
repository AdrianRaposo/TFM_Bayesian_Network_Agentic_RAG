# NIH Public Access 

## Author Manuscript

Int J Med Inform. Author manuscript; available in PMC 2014 April 01.
Published in final edited form as:
Int J Med Inform. 2013 April ; 82(4): 230-238. doi:10.1016/j.ijmedinf.2012.11.006.

## An asthma management system in a pediatric emergency department

Judith W. Dexheimer ${ }^{\text {a,b,* }}$, Thomas J. Abramo ${ }^{\text {c }}$, Donald H. Arnold ${ }^{\text {c,d }}$, Kevin B. Johnson ${ }^{\text {e }}$, Yu Shyr ${ }^{\mathrm{f}}$, Fei Ye ${ }^{\mathrm{f}}$, Kang-Hsien Fan ${ }^{\mathrm{f}}$, Neal Patel ${ }^{\mathrm{e}}$, and Dominik Aronsky ${ }^{\mathrm{c}, \mathrm{e}}$<br>Judith W. Dexheimer: Judith.Dexheimer@cchmc.org<br>${ }^{a}$ Division of Emergency Medicine, Cincinnati Children's Hospital Medical Center, United States<br>${ }^{\text {b }}$ Division of Biomedical Informatics, Cincinnati Children's Hospital Medical Center, United States<br>${ }^{\text {c }}$ Dept of Emergency Medicine, Vanderbilt University, United States<br>${ }^{\text {d }}$ Center for Asthma Research and Environmental Health, Vanderbilt University, United States<br>${ }^{\text {e }}$ Dept of Biomedical Informatics, Vanderbilt University, United States<br>${ }^{\mathrm{f}}$ Dept of Biostatistics, Vanderbilt University, United States


#### Abstract

Introduction—Pediatric asthma exacerbations account for $>1.8$ million emergency department (ED) visits annually. Asthma guidelines are intended to guide time-dependent treatment decisions that improve clinical outcomes; however, guideline adherence is inadequate. We examined whether an automatic disease detection system increases clinicians' use of paper-based guidelines and decreases time to a disposition decision.


Methods-We evaluated a computerized asthma detection system that triggered NHLBIadopted, evidence-based practice to improve care in an urban, tertiary care pediatric ED in a 3month (7/09-9/09) prospective, randomized controlled trial. A probabilistic system screened all ED patients for acute asthma. For intervention patients, the system generated the asthma protocol at triage for intervention patients to guide early treatment initiation, while clinicians followed standard processes for control patients. The primary outcome measures included time to patient disposition.

Results-The system identified 1100 patients with asthma exacerbations, of which 704 had a final asthma diagnosis determined by a physician-established reference standard. The positive predictive value for the probabilistic system was $65 \%$. The median time to disposition decision did not differ among the intervention ( $289 \mathrm{~min} ; \mathrm{IQR}=(184,375)$ ) and control group ( $288 \mathrm{~min} ; \mathrm{IQR}=$ $(185,375))(p=0.21)$. The hospital admission rate was unchanged between intervention ( $37 \%$ ) and control groups ( $35 \%$ ) ( $p=0.545$ ). ED length of stay did not differ among the intervention ( 331 $\min ; \operatorname{IQR}=(226,581))$ and control group $(331 \min ; \operatorname{IQR}=(222,516))(p=0.568)$.
Conclusion-Despite a high level of support from the ED leadership and staff, a focused education effort, and implementation of an automated disease detection, the use of the paper-based asthma protocol remained low and time to patient disposition did not change.

[^0]
[^0]:    (c) 2012 Elsevier Ireland Ltd. All rights reserved.
    ${ }^{\mathrm{f}}$ Corresponding author at: Division of Emergency Medicine, Cincinnati Children's Hospital Medical Center, MLC 2008,3333 Burnet Avenue, Cincinnati, OH 45229-3039, United States. Tel: +1 513803 2962; fax: +1 5138032581.
    Authors contributions: All authors contributed materially to the production of this manuscript.
    Conflict of interest: The authors declare that they have no competing interests.

# Keywords

Asthma; Medical informatics; Bayesian network; Decision support

## 1. Introduction

Asthma is the leading chronic childhood disease, affecting 6.8 million children (9.4%) [1]. Asthma exacerbations account for >1.8 million emergency department (ED) visits annually [2]. Asthma disproportionately affects minority populations. Adverse outcomes, including ED visits, are higher for African-American children [3]. Because asthma is a chronic disease, it carries a considerable economic burden and accounts for >60% of asthma-related costs [4]. Uncontrolled asthma can lead to exacerbations requiring the patient to seek immediate care, frequently in an ED setting.

Treatment of an asthma exacerbation is complex, involving a temporal and multidisciplinary evaluation and reevaluation to adjust asthma medications and make a disposition decision. It is challenging to provide standardized care in a fast-paced, interruption-driven and often overcrowded environment like the ED. An automatic, informatics-supported guideline delivery system could assist clinicians in delivering more homogeneous care for asthma patients. The goal of this study was to implement and evaluate a fully computerized asthma detection system combined with a paper-based asthma care protocol in the pediatric ED to help standardize care and reduce time to disposition decision.

## 2. Background

### 2.1. Guidelines

Early initiation and adherence of asthma guideline-directed care improves patients' care [4,5]. The asthma guideline from the National Heart Lung and Blood Institute (NHLBI) [6] focuses on outpatient care and chronic control but includes limited information on treating emergency exacerbations. The guidelines are general rules to follow for optimal care. The emergency management guidelines recommend treatment decisions be guided through peak flow readings, forced expiratory volume, and oxygen saturation. The NHLBI flow diagram provides general direction but requires local customization to account for individual ED resources and practice variability, including available medications and asthma severity scoring. With such opportunity for variability, clinicians' adherence to guidelines remains suboptimal. Current guideline implementation approaches could benefit from an increased level of workflow integration, particularly through the application of information technology. Despite the benefits of computerized guidelines, a major barrier remains in the daily clinical or daily ED routine clinicians need to remember to initiate the guideline process, either by retrieving paper-based guidelines or initiating the process in a computerized system.

### 2.2. Guideline initiation

Guideline initiation is integral to initiating treatment that is calibrated to severity. The NHLBI guidelines [6] recommend that (a) asthma treatment is initiated quickly; (b) response to initial treatment is reevaluated in 1-2 h intervals; and (c) treatments that are appropriate for the patient's severity level are readjusted within a specific time. Patient disposition decisions, e.g., whether a patient needs to be admitted to the hospital, should occur within a few hours of ED presentation. At triage an automatic reminder mechanism might be implemented, which can start the evidence-based asthma protocol and mark the starting time for reevaluation intervals.

However, identification of patients presenting with an asthma exacerbation is often delayed, leading to unnecessary delay in starting treatments, furthermore, variations in timely reevaluation of a patient's treatment response can lead to further delays, resulting in unduly long ED visits.

Because early recognition of asthma is crucial, some studies [7,8] have explored ways to identify asthma patients in the ED setting. One ED-based study implemented a computerized kiosk to obtain patient information from parents [7]. Another used a Neural Network, but the data were from a mailed questionnaire and not real-time identification during the patient's visit [8]. However, neither utilized an integrated information system infrastructure.

### 2.3. Motivation and framework

An automatic asthma detection system might prompt providers to initiate treatments earlier and remove the burden of guideline initiation from the triage nurse. Ideally the system would detect asthma patients during the triage process, which is most often the earliest time of a clinician interacting with a patient. Our primary objective was to examine whether a workflow-embedded, informatics-supported framework including automatic disease detection system and a locally adapted protocol based on the NHLBI guideline can decrease the time to disposition decision.

## 3. Methods

### 3.1. Setting

The Vanderbilt Children's Hospital ED is an urban, tertiary care teaching facility with approximately 55,000 annual admissions, 2800 of which are for acute asthma exacerbations. The ED has 68 attending and resident physicians, 95 nurses, and 16 respiratory therapists. Approximately 7--10% of pediatric ED patients present with an asthma exacerbation [9].

The pediatric ED has an 8-page paper-based guideline available for use including a validated asthma severity metric [10], and is available for guiding asthma care including reassessment and treatment suggestions. The guideline is available at both triage and in the physician area of the ED. In a prospective chart audit of asthmatic patients, the guideline was used in only 7--10% of asthma cases presenting to the pediatric ED [9].

### 3.2. Asthma informatics reminder system

We developed an asthma informatics system that includes 2 components: (1) an automatic detection system, and (2) a disease management system. The two-phase study design of the integrated asthma system has been reported previously [11]. To examine the effects of the detection and management system, we designed a two-phase evaluation allowing us to separately measure the effects of the automatic detection and the computerized management component. This study reports the first phase examining the individual impact of the asthma detection component.

The computerized disease detection system [9,12] automatically screened all patients presenting to the pediatric ED for inclusion using a probabilistic algorithm (Bayesian network). The detection system algorithm includes information from the electronic medical record for past medical history and medications, the billing system for previous asthmarelated encounters, and the computerized triage application for details relating to the current visit. The detection system requires no additional data entry and operates in real-time providing automatic identification and subsequent initiation of asthma guidelines. All patients presenting to the ED are screened for an asthma exacerbation and the Bayesian

network threshold is used to distinguish between patients with and without asthma. The threshold can be adjusted and was set to reduce alert fatigue.

For patients detected by the algorithm as potentially having an asthma exacerbation, the asthma protocol was automatically printed out and placed with the triage document in the patient's chart. This allowed the clinical team immediate access to the asthma management protocol at the bedside. The goal was to add asthma protocols consistently and automatically to the charts of patients who had an increased likelihood of an asthma exacerbation. A pediatric emergency medicine board-certified physician examined each patient identified by the system to determine whether asthma exacerbation was present; patients without a positive asthma diagnosis were not included in the analysis.

### 3.3. Study design

We evaluated the asthma informatics reminder system in a prospective, randomized controlled trial. The study period was 3 months: July 1--September 30, 2009. All patients presenting to the pediatric ED during the study period were screened for inclusion using the Bayesian network system [9,11,12]. Patients were included if they were 2--18 years of age and were identified as presenting with an asthma exacerbation by the disease detection system. Patients were excluded if they (a) had an Emergency Severity Index = 1 (most severe, life-threatening condition), (b) had no electronic triage, or (c) eloped or left the ED prior to being seen by a physician. The patient visit was the unit of analysis and patients were randomized with a 6-block randomization schema. Repeat patient visits were not excluded and were considered independent events. All patients presenting to the ED were randomized prior to asthma determination and were automatically assigned to either intervention or control. A sample size of 286 patients per group was needed to detect a 10% difference with a β = 0.9 and α = 0.05, with the control group receiving usual care. The study was approved by the institutional review board and registered on clinicaltrials.gov (NCT01070147).

### 3.4. Intervention

The pediatric ED clinical team identified optimization of asthma treatment as a high priority for quality improvement. A multidisciplinary respiratory distress committee including pediatric ED faculty and fellows, nursing staff, respiratory therapy, pharmacy, and informatics personnel iteratively developed and refined an evidence based practice protocol, which was combined with an asthma care flow sheet. The flow sheet (Fig. 1) is a best practice based adaptation of the NHLBI guidelines for acute asthma care that also includes treatments not addressed in the guidelines and is based on an asthma severity score. The flow sheet is a one-page, graphical algorithm which was the title page of the protocol and allowed for annotations. More detailed protocol information was available in an appended 8-page asthma protocol developed by the physicians and respiratory therapists to guide asthma care based on patient severity. The asthma protocol contains suggested drugs and dosing stratified by patient severity. It includes rules and recommendations for therapies resistant to standard asthma therapies and noninvasive positive pressure ventilation and intubation and mechanical ventilation. The asthma protocol encourages re-scoring the patient and after the additional evaluation offers disposition suggestions based on patient severity.

The asthma detection system and paper-based protocol included 8 of the 15 important features found in successful clinician decision support systems [13]. The identification system was integrated with the information systems and a multidisciplinary team was involved in the entire development process. Because it was a paper-based protocol, it included additional data entry and provided the suggested order set for each patient severity rating.

If the asthma detection system identified a patient presenting with signs and symptoms consistent with an asthma exacerbation [9,12,14], the patient was randomized to the intervention or control group. The clinicians were blinded to the randomization. The intervention group received the flow diagram and protocol which printed automatically at the end of the triage session when the nurse printed the triage summary page. The electronic triage summary page displayed a reminder which required the nurse to acknowledge that the patient presented with symptoms compatible with an asthma exacerbation and that the protocol would print. The paper-based protocol printed automatically at the end of the triage session when the patient triage summary was printed. The paper-based protocol was placed in the folder where clinicians access other paper forms for documentation and review during the patient's visit. The control group received usual care, i.e. no reminders or automatic printout was provided. The paper-based protocol was available in the ED at triage and in the physician area.

In the 2 months prior to the study an educational program was implemented: (a) physicians were informed about the study in the operational emergency management, faculty, and monthly resident meetings; (b) an email from the ED director (division chair) describing and supporting the study was sent out to the ED staff; (c) respiratory therapists were informed during their monthly management meetings; and (d) for a week prior to the study the nursing leadership informed the nursing staff through twice-daily meetings before the start of each shift. At each of these meetings an investigator explained the study and answered any questions that arose. Posters with the one-page flow diagram were mounted as reminders in all of the triage locations and the physician work areas.

### 3.5. Data collection

Data on each visit were collected from the available ED information system including the electronic medical record [15], electronic triage application [16] and ED patient status board [17]. A sensitivity of 85% was chosen for the Bayesian network to minimize alert fatigue but capture the maximum number of asthma patients. Based on historical data this resulted in the network having a specificity of 93.6%, positive predictive value of 65.3%, and negative predictive value of 98.7% [9]. To establish a reference standard for the diagnosis of an asthma exacerbation, a pediatric emergency medicine board-certified physician examined each patient visit within 3 days of the visit to determine whether asthma exacerbation was present. A pediatric ED charge nurse performed chart reviews on all patient visits. To ascertain data quality an independent pediatric emergency medicine board-certified physician established a diagnosis for 20% of randomly selected patients' charts (k = 0.89; 95% CI: 0.82-0.95).

### 3.6. Outcome measures

The primary outcome measure was the time from ED triage to disposition decision. A discharge or hospital admission order (bed request order) in the patient tracking board was considered a disposition decision. Secondary outcomes were guideline adherence measures including asthma education ordered, protocol found on chart, any asthma scoring performed, and hospital admission rate.

### 3.7. Clinician follow-up survey

After study completion a one-page, 10-question follow-up survey was administered to the respiratory therapists, nurses, and attending and resident physicians who worked shifts in the ED during the study period. The survey evaluated the use of the paper-based flow diagram and protocol during the study period.

3.8. Statistical analysis

Primary analysis of this study focused on detecting the associations between the use of an electronic asthma management system (intervention) and time from ED triage to disposition decision, with comparison to the usual care (control). Descriptive statistics, including means with standard deviations or medians with interquartile ranges for continuous variables such as time to disposition decision, length of stay, and age, as well as percentages and frequencies for categorical variables such as race, gender, insurance type, were provided to describe the study sample. Differences between groups for continuous variables were examined using ANOVA or Wilcoxon rank-sum test as appropriate. Differences between group means for continuous variables were examined using ANOVA or Wilcoxon rank-sum test. Pearson chi-square tests were used to assess the categorical variables. All tests of significance were based on two-sided probabilities, at P values less than 0.05. Logistic regression was used to estimate the odds ratios (ORs) and their 95% confidence intervals (CIs) for patient's admission status, representing the overall odds of being admitted associated with the management system, and to adjust for potential confounding variables, including age, gender, race, insurance, language, acute asthma severity, and mode of arrival in the multivariate analysis. Kaplan–Meier curves were presented with log-rank test results to determine whether there were differences in the observed time to disposition decision as well as length of stay by management system. Cox proportional hazards models were used separately for time to decision and length of stay, to determine whether there is a significant difference in the outcome variables between the intervention and control, adjusting for the potential confounding variables. The adjusted p-values and the corresponding 95% confidence interval were reported for multivariate analyses. All data analyses were carried out using statistical software R (Version 2.12.2).

## 4. Results

Among all the 15,163 ED patients screened during the study period, 9624 were within the eligible age range (2–18 years) and screened by the asthma detection system (Fig. 2). Two patients were excluded due to registration errors. The detection system (Bayesian network) identified 1100 patients having an asthma exacerbation. As determined by the reference standard, 704 had a final diagnosis of asthma, yielding a positive predictive value of 64%. Among the 394 determined not to present with asthma, 178 had a respiratory complaint, 75 had flu or flu like symptoms, 31 had fever [9], and 110 had other complaints.

There were 54 repeat visits from 51 unique patients during the study period. The average number of days between visits was 25 (0, 79). Nine treat-and-release patients had repeat visits within 72 h that classified as a relapse. Of the 9 patients, 5 were treated and released in their second visit, 1 left against medical advice and returned to be admitted, and 3 patients were treated and released and returned to be admitted.

From the 704 patients with a reference diagnosis of asthma, patients did not differ significantly in race (p = 0.439, df = 2) or mode of arrival (p = 0.529, df = 2). Patient demographics are shown in Table 1.

For all study patients, intervention and control patients did not differ significantly in time to disposition; intervention patients had a median time of 289 min (SD: 259 min) and control patients a median time of 288 min (SD: 307 min; p = 0.212). Intervention patients had a median ED length of stay of 331 min (SD: 517 min) and control of 331 min (SD: 565 min; p = 0.414). Admission rates were similar between the two groups (intervention = 36.6%, control = 34.4%, p = 0.271). Primary findings are shown in Table 2.

For study patients with a paper-based protocol on the chart, intervention and control patients did not differ significantly in time to disposition. Protocol patients had a median time of 288 min ( $95 \%$ CI: $270-314 \mathrm{~min}$ ) and no-protocol patients a median time of $290 \mathrm{~min}(95 \% \mathrm{CI}$ : $266-302 \mathrm{~min} ; p=0.291$ ). Protocol patients had a median ED length of stay of $332 \mathrm{~min}(95 \%$ CI: $310-360 \mathrm{~min}$ ) and no protocol of $331 \mathrm{~min}(95 \%$ CI: $318-358 \mathrm{~min} ; p=0.848$ ). Admission rates were not similar between the two groups (protocol $=14 \%$, no protocol $=38 \%, p<$ 0.01 ).

The median time to ED disposition decision for hospital admitted patients was 348 min for hospital-admitted patients (Fig. 3) and 257 min (Fig. 4) for treat-and-release patients. The median ED length of stay was 754 min for hospital-admitted patients and 268 min for treat-and-release patients.

The response rates for the clinician survey were $81 \%$ for respiratory therapy, $99 \%$ for nurses, and $75 \%$ for physicians. Clinician survey results are shown in Table 3. Nurses who saw the protocol were not any more likely to use it than those who never reported seeing it ( $p=0.094$ ). Physicians who saw the protocol were more likely to use it compared to those who did not see the protocol $(p<0.001)$.

# 5. Discussion 

The study examined the effect of a computerized asthma disease detection system combined with a paper-based asthma care protocol in the pediatric ED compared to the usual care. We did not find a difference in time to disposition decision, hospital admission rate or ED length of stay between intervention and control patients. Combining the automatic detection system with printing the paper-based protocol did not change clinician care for the patients. Paperbased protocols were found in $18 \%$ of the intervention patients' charts, which was less than expected, and protocols were found in $1 \%$ of the control patients' charts. The time to disposition decision was chosen as the primary outcome measure because asthma guideline compliance has been shown to decrease the time to emergency department disposition [18]. The time to disposition decision was chosen as the primary outcome measure instead of the ED length of stay because the length of stay can be influenced by factors outside the control of the patient's current care such as hospital beds available. Intervention patients with a paper-based protocol in their chart had a lower admission rate ( $14 \%$ ) than intervention patients without a paper-based protocol ( $38 \%$ ); while it can be hypothesized that the protocols may have helped to reduce admission, the small sample size and alternate explanations, e.g., faster protocol use and less documentation requirement for asthma patients with lower severity, prevent a conclusive interpretation of the findings.

None of the primary and secondary outcomes showed a difference between intervention and control. Additional analysis was performed to compare admitted and treat-and-release patients. No significant difference was found in time to disposition decision or length of stay; this may indicate that there is truly no difference between the groups. However, the median time to disposition was under 6 h for both groups and within the national guideline's recommendations. We did not perform a strict intention to treat analysis because randomization occurred after identification by the Bayesian network and all identified patients were included in the study; this produces an additional bias against the null hypothesis suggesting that there is no real difference between the intervention and control groups.

Despite a high level support from ED management and clinicians, substantial education effort, and automated decision support, paper-based asthma protocol utilization remained at very low levels and may indicate that such multi-disciplinary protocols are difficult to implement in a busy emergency care environment that is driven by information-intense work

patterns, multi-tasking, crowding, and frequent interruptions. Although the protocol was already in available in the ED, the protocol is 8 pages, which may inhibit use in the fastpaced ED environment. The first page of the protocol is a flow sheet describing best practice adaptation of the NHLBI guidelines. The study occurred during the H1N1 season, which may have impacted the performance characteristic of the disease detection system and ED workload. There was no additional staff for managing potential eligible patients presenting during the study period, however, at least one respiratory therapist is on staff and present at all times in the ED and more are available if needed from the hospital.

The paper-based protocols were available in the ED and in use for several years prior to study implementation; the printed asthma protocol and one-page flow diagram was available in triage and in the physician area. The only change was the addition of the one-page flow diagram on the first page. The disease detection system was successfully integrated with the ED information systems, however it did not influence the clinicians' behavior despite providing a reminder and the convenience of automatic guideline printing. The triage nurse was required to acknowledge that the patient may be presenting with an asthma exacerbation for the protocol to print. This protocol did not, however, get added to the patient's medical record. Because of this, there are several places for the protocol to get "lost" either from a lack of printer or from the protocol not being separated and set aside for the study team. Since the protocol was found on $18 \%$ of the available charts, the providers took note of this protocol during a patient's management and that it may have influenced patient management. However, in spite of education about the existence and availability of the paper-based protocol, the protocol was not adopted and used by many clinicians in a significantly higher number than the control group.

The disease detection system was successfully integrated with the ED information systems and used to identify possible asthma exacerbations in triage. After discussion with ED leadership and staff, we chose the Bayesian network sensitivity of $85 \%$ to produce an anticipated positive predictive value of approximately $66 \%$ which allowed approximately 1 of 3 prompts to be for a patient not presenting with an asthma exacerbation, a rate we felt was low enough to reduce alert fatigue and minimize the total number of patients misclassified. Existing data from the development of the Bayesian network in the same setting (12, 14) was used and discussed to settle on the ideal sensitivity for our ED. Paper-based asthma care protocols were found on fewer charts than expected with the automatic printing. Several possible causes could have reduced the number of paper-based asthma care protocols seen. Automatic printing of the asthma care protocol was linked to the process of printing the triage summary. Because the protocol was a research study, it was separated from the patient's chart at the end of the visit, set aside for the study team, and not made part of the permanent medical record. Although education was provided to save the protocol sheets, some may have been discarded if there was no writing on the paper. However, some protocols may not have been separated from the chart and if empty, would have been discarded.

While the protocol was more frequently found in the chart for intervention patients, this may not be helpful in delivering multi-disciplinary coordinated care.

Because of the low level of protocol utilization, we conducted a follow-up survey with clinical staff to determine some of the reasons for non-use of the paper protocol. The aim was to elucidate some of the potential work-flow issues that may have inhibited protocol use. The nurses saw the protocol in the chart; and despite considerable educational efforts from nurse management prior to the study the nurses frequently were not sure what to do with the protocol. The physicians saw the protocol in the charts but reported using it infrequently. However, physicians who saw the protocol in the chart reported being more

likely to use it to make care decisions. While we designed the protocol to be filled-out and written on, all of the medication orders in our system are electronic. It is possible that the medication guidelines were used but no writing was performed on the paper sheet.

For patients in whom the protocol was identified in the chart, clinicians did not utilize the protocol for annotations (decision logic or severity assessment). The low use of the paperbased protocol may bias the study toward the null hypothesis. However, the sample size analysis showed adequate power to detect a difference. In a similar prospective study [19] the kiosk-generated care recommendations were presented on paper to the clinicians treating the patients. The study had only marginal effects on patient care, which was primarily due to physicians' nonuse of the provided paper-based information. The measurements used to measure guideline compliance may not have been the correct proxies, or the actual guideline compliant care occurred whether or not the paper-based guideline was physically present. The study only examined process measures such as the time to disposition decision and the patient's length of stay. However, it did not attempt to evaluate changes in the patient's clinical care. The time to disposition decision maybe determined by the natural history of the illness; a failure to shorten this time may not be a direct result of the intervention and the acuity and admission rates were not statistically significant between groups.

The study has several limitations. The pediatric ED utilizes several information systems for patient care. Also, this environment may not be typical, limiting the generalizability of the findings. However, the disease detection system uses only common data elements that other locations could easily obtain. Clinician use could not be measured by annotation on the paper-based protocol because clinicians may have applied the algorithm from the paper without annotating on the protocol. It is possible that a Hawthorne effect influenced the study because blinding was not possible; as clinicians used the protocol in the ED for several years, the potential bias would likely be small. The clinicians may have already used the algorithm in daily practice which would bias the study toward the null hypothesis. Although the study did not find differences between the intervention and control group, this may not be interpreted as a lack of effectiveness of clinical prompts.

The paper-based protocol was available to be picked up at the triage stations and in the ED. Despite the educational efforts only one control patient had a protocol placed on their chart without a computerized prompt. Due to the nature of providing a paper form, blinding was not possible.

Our study represents a prospective randomized control trial of an automatic disease detection system and a paper-based asthma care protocol. The disease detection system implementation represented the feasibility of using a fully-integrated informatics system to detect patients in real-time. The paper-based protocol use was equivalent to previous research in the field.

In addition to an integrated asthma management system, phase II will contain the automatic disease detection system and a computer-based management system including the evidencebased order-sets will replace the paper-based protocol approach. It is expected that an integrated approach may alleviate some of the issues that the paper-based protocol presented.

The prospective randomized controlled trial represents an automatic disease detection step to help alleviate the burden on clinicians initiating guidelines. While the automatic asthma detection system demonstrated good levels of identifying asthma patients among an unselected ED population, the system was not effective at influencing outcome measures that relate to the timing of asthma care in the pediatric ED.

# Acknowledgments 

This work was supported by LM 009747-01 (Dr Dexheimer, Dr Aronsky) and NHLBI K23 HL80005 (Dr Arnold). The first author was supported by a Training Grant from the NLM (T15 LM 007450-03).

# Summary points 

What was known before the study?

- Asthma guidelines can improve patient care.
- Guideline implementation approaches benefit from an increased level of workflow integration, early initiation is integral to beginning severity-adjusted treatments promptly.
- The NHLBI guidelines emphasize early recognition and treatment of asthma exacerbations, as well as appropriate treatment stratified by severity.

What the study has added to the body of knowledge?

- The disease detection system implementation represented the feasibility of using a fully-integrated informatics system to detect patients in real-time.
- The paper-based protocol use was equivalent to previous research in the field.

![img-0.jpeg](img-0.jpeg)

Fig. 1.
The locally adapted flow-sheet for emergency pediatric asthma care.

![img-1.jpeg](img-1.jpeg)

Fig. 2.
Consort diagram for patient randomization.

Time to Disposition Decision by Intervention (Inpatient)
![img-2.jpeg](img-2.jpeg)

Fig. 3.
Time to inpatient disposition decision by intervention vs control.

Time to Disposition Decision by Intervention (Outpatient)
![img-3.jpeg](img-3.jpeg)

Fig. 4.
Time to outpatient disposition decision by intervention vs control.

Table 1
Patient demographics.


${ }^{a}$ LQ - lower quartile; UQ - upper quartile.

Table 2
Primary findings.


${ }^{a}$ LQ - lower quartile; UQ - upper quartile.

Table 3
Results from clinician survey.
