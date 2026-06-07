# HHS Public Access 

Author manuscript
Int J Med Inform. Author manuscript; available in PMC 2017 June 06.
Published in final edited form as:
Int J Med Inform. 2014 November ; 83(11): 805-813. doi:10.1016/j.ijmedinf.2014.07.008.

## Implementation and Evaluation of an Integrated Computerized Asthma Management System in a Pediatric Emergency Department: A Randomized Clinical Trial

Judith W Dexheimer, PhD ${ }^{1,2}$, Thomas J Abramo, MD ${ }^{3}$, Donald H Arnold, MD, MPH ${ }^{4,5}$, Kevin Johnson, MD, MS ${ }^{6}$, Yu Shyr, PhD ${ }^{7}$, Fei Ye, PhD ${ }^{7}$, Kang-Hsien Fan ${ }^{7}$, Neal Patel, MD, MS ${ }^{6}$, and Dominik Aronsky, MD, PhD ${ }^{4,6}$<br>${ }^{1}$ Division of Emergency Medicine, Cincinnati Children's<br>${ }^{2}$ Division of Biomedical Informatics, Cincinnati Children's<br>${ }^{3}$ Department of Pediatrics, University of Arkansas for Medical Sciences<br>${ }^{4}$ Department of Emergency Medicine, Vanderbilt University<br>${ }^{5}$ Center for Asthma Research and Environmental Health, Vanderbilt University<br>${ }^{6}$ Department of Biomedical Informatics, Vanderbilt University<br>${ }^{7}$ Department of Biostatistics, Vanderbilt University


#### Abstract

Objective-The use of evidence-based guidelines can improve the care for asthma patients. We implemented a computerized asthma management system in a pediatric emergency department (ED) to integrate national guidelines. Our objective was to determine whether patient eligibility identification by a probabilistic disease detection system (Bayesian network) combined with an asthma management system embedded in the workflow decreases time to disposition decision.


Methods-We performed a prospective, randomized controlled trial in an urban, tertiary care pediatric ED. All patients 2-18 years of age presenting to the ED between October 2010 and

[^0]
[^0]:    Correspondence: Judith Dexheimer, PhD, Division of Emergency Medicine, Cincinnati Children's Hospital Medical Center, MLC 2008, 3333 Burnet Avenue, Cincinnati, OH 45229-3039, Judith.Dexheimer@cchmc.org, Phone: 001-513-803-2962, Fax: 001-513-803-2581.
    Publisher's Disclaimer: This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

    AUTHOR CONTRIBUTIONS
    All authors contributed materially to the creation of the manuscript.
    Judith W Dexheimer: design, acquisition of data, drafting of the manuscript, critical revision, and technical, and material support. Thomas Abramo: design, implementation, and material support.
    Donald Arnold: design, implementation, and revisions.
    Kevin Johnson: design and critical revisions.
    Yu Shyr: design, statistical support and revisions.
    Fei Ye: statistical support and design.
    Kang-Hsien Fan: statistical and technical support.
    Neal Patel: design and critical revisions.
    Dominik Aronsky: conception, design, and critical revisions.

February 2011 were screened for inclusion by the disease detection system. Patients identified to have an asthma exacerbation were randomized to intervention or control. For intervention patients, asthma management was computer-driven and workflow-integrated including computer-based asthma scoring in triage, and time-driven display of asthma-related reminders for re-scoring on the electronic patient status board combined with guideline-compliant order sets. Control patients received standard asthma management. The primary outcome measure was the time from triage to disposition decision.

## Results

The Bayesian network identified 1,339 patients with asthma exacerbations, of which 788 had an asthma diagnosis determined by an ED physician-established reference standard (positive predictive value 69.9%). The median time to disposition decision did not differ among the intervention (228 minutes; IQR=(141, 326)) and control group (223 minutes; IQR= (129, 316));(p=0.362). The hospital admission rate was unchanged between intervention (25%) and control groups (26%); (p=0.867). ED length of stay did not differ among intervention (262 minutes; IQR=(165, 410)) and control group (247 minutes; IQR=(163, 379));(p=0.818).

## Conclusions

The control and intervention groups were similar in regards to time to disposition; the computerized management system did not add additional wait time. The time to disposition decision did not change; however the management system integrated several different information systems to support clinicians' communication.

## Keywords

Asthma, Emergency Medicine, Medical Informatics, pediatrics, clinical decision support

## 1. INTRODUCTION

In the United States, approximately 4 million children experience an asthma exacerbation annually leading to more than 1.8 million emergency department (ED) visits [1]. Patients presenting to the ED with an asthma exacerbation often require treatment and observation over several hours. This care can be complex and involves a coordinated care team. Ideally, upon arrival, patients are given an initial asthma severity rating using either an asthma scoring metric [2] or peak flow measurement. According to national recommendations [3] the patient's asthma severity and response to treatment should be reevaluated every 1--2 hours. With each assessment treatment, decisions should be adjusted to the new severity level, ideally leading to a disposition decision within 4--6 hours. Treating asthma exacerbations involves a temporal and multi-disciplinary evaluation element, including patient reevaluation, treatment adjustments and timely disposition decisions. The challenge is to provide standardized, multi-faceted care in a fast-paced, interruption-driven and often overcrowded environment like the ED.

Clinical guidelines and pathways exist to help guide asthma care and positive effects on patient outcomes have been demonstrated [4, 5]. The asthma guideline from the National Heart Lung and Blood Institute (NHLBI)[3] focuses mainly on the outpatient environment, but includes information on care for emergency exacerbations. The most frequent approach to implementing guidelines in a clinical environment is still paper-based [6], but computer-based implementations are also used [7, 8]. Researchers have examined the benefits of

paper-based and computer-based guideline implementations, but sustainable computer-based approaches in a clinical environment remain infrequent. An automatic, informaticssupported management system could assist clinicians in delivering more homogeneous and better coordinated care for asthmatic patients.

Automating disease detection can help prompt clinicians to initiate treatments earlier and remove the burden of guideline initiation. We hypothesized that the integration of an asthma management system will decrease time to patient disposition decision. We designed and implemented a computerized disease detection and management system for asthma care in the pediatric ED embedded in the clinicians' workflow. The goal of this project was to determine whether patient eligibility identification by a probabilistic disease detection system (Bayesian network) combined with an asthma management system embedded in the workflow decreases time to disposition decision.

## 2. MATERIALS AND METHODS

### 2.1 Setting

This study was conducted at an urban, pediatric ED that provides care for 55,000 patient visits annually with approximately 7--10% of patients presenting with an asthma exacerbation [9]. The ED has 68 attending and resident physicians, 95 nurses, and 16 respiratory therapists. The pediatric ED has a fully computerized information technology infrastructure involving an electronic medical record (EMR) [10], electronic triage application [11], computerized provider order entry (CPOE) [12], and a computerized patient status board [13]. All four of the systems in the electronic infrastructure are entirely home-grown and integrated. The EMR is a web-based medical record system for clinical communication including inpatient and outpatient visit information. The electronic triage application is used to collect all relevant information about the patient's current ED visit; this information is automatically sent to the EMR. All orders are entered in the CPOE system which provides decision support for medication orders. Finally, the computerized patient status board integrates and displays information relevant to the current visit from the previous three systems. Prior to the start of the study, an 8-page, paper-based guideline including a validated asthma severity metric [2] has been available for guiding asthma care including reassessment and treatment suggestions; however, the guideline was used in only 7--10% of asthma cases [9].

### 2.2 Asthma Management System

A computerized asthma management system was developed by the investigators. The asthma system includes two components: 1) the automatic disease detection system, and 2) a computerized management system that has been reported previously [14]. The automatic disease detection system was based on a Bayesian network [9, 15, 16] developed in the same pediatric ED as the study. The Bayesian network uses electronic information available at the time of triage including age, respiratory rate, chief complaint, oxygen saturation, and acuity level and historical data from the patient's electronic medical record including past medical history, medications, and billing codes. It required no additional data entry by clinical staff and ran seamlessly during each encounter.

The pediatric ED clinical team identified optimization of asthma treatment as a high priority for quality improvement. A multidisciplinary respiratory distress committee was formed approximately 2 years prior to implementation, including pediatric ED faculty and fellows, nursing staff, respiratory therapy, pharmacy, and informatics personnel. The committee iteratively developed and refined an evidence-based practice guideline, which was combined with an asthma care flow sheet and severity-based order sets. The flow sheet and paper-based guideline have been described previously [17]. The paper-based guideline is a local adaptation of the NHLBI guidelines for the emergency treatment of asthma exacerbations. The severity-based order sets for use in the CPOE system were created using the paper-based guideline and the NHLBI guidelines. The two guidelines were combined to create 3 severity-based order sets for mild, moderate, and severe asthma. The computerized order sets were available as both text-based order sets accessible by all physicians and as an automatic prompt for intervention patients after the physician assigned an asthma score.

For intervention patients identified by the detection system, the electronic triage summary page required the nurse to perform an initial asthma score on the patient. When complete, a computer-generated page was sent to respiratory therapy containing the patient's information and asthma score, and the reminders were turned on in the electronic patient status board and CPOE systems. The electronic patient status board [13] acted as a communication point among the clinical care team. A new column was added for displaying the asthma scores and related information. Each time a respiratory distress score was recorded electronically, the patient status board column updated with the new score and a trend arrow. The trend arrow looked only at the last two scores and displayed whether the patient was worsening (down arrow), improving (up arrow), or remaining stable (equals sign). By hovering-over the column with the mouse, a graph of the patient's asthma severity scores was displayed. This graph was updated each time a new score was recorded. The electronic patient status board provided prompts for when a patient was due for reassessment.

The electronic patient status board prompts were passive reminders for the respiratory therapist and physician. The respiratory therapists were given a new column for patient sign-in. Respiratory therapy scoring was required hourly per protocol. For intervention patients, the column background would turn yellow when a new respiratory distress score was due within 15 minutes. The background of the column would turn red when a new respiratory distress score was due or past due. Entering a new score into the respiratory therapy charting system would clear the column and restart the timer.

Physicians were required to reassess and rescore their patients every 2 hours. Similar to the respiratory therapists' reminder, if an assessment and score were due within 15 minutes, the background of the column was yellow. If an assessment was due or past due, the background of the column was red. If the patient met the criteria for making a disposition decision, the column would flash dark blue. Patients were considered eligible for a disposition decision when they had been in the ED at least four hours, with two scores either in the same category, indicating that treatment effect does not result in further changes, or the scores are improving (e.g. moderate to mild categorization). When the physician clicked on the column, a pop-up box would inform them that it was time to make a disposition decision on

the patients. The physicians could defer this decision for 2 hours. When a discharge or bed request for hospital admission was entered in for the patient, the column turned green, indicating that a disposition decision had been made and the patient's care in the ED had reached stabilization for either admission or discharge.

When the physician opened the CPOE session on the patient, a pop-up required asthma scoring for the patient (figure 1). This pop-up displayed the asthma scoring matrix along with the most recent asthma score recorded and time. The physician had the option of turning off all asthma-related prompts. If the patient was presenting with an asthma exacerbation, the physician carried through with scoring. Based upon this score, a severity-based order set was provided to the clinician. The order sets were mild, moderate, or severe and had pre-selected items the pediatric ED recommended for asthma care. By selecting boxes, the physicians could order the asthma treatments. Once ordering was complete, a summary page was displayed to elucidate the new orders, continuing orders, and discontinued orders. All prompts remained on through the patient's stay in the ED regardless of disposition decision unless turned off in the CPOE system.

In automatically detected eligible patients, either the computerized management system alerts were turned on or the paper-based asthma protocol was automatically printed out and placed with the triage document in the patient's chart. A multidisciplinary respiratory distress committee created guideline-adapted severity-based order-sets that were available on paper and in the CPOE system. After the automatic disease detection system identifies patients, scoring reminders and the order sets are displayed to help maintain guideline compliance. Table 1 shows a brief description of the key parts of the asthma management system and when these parts were available.

### 2.3 Educational Effort

In the two months prior to the study a considerable educational effort was completed: a) physicians were informed about the study in the operational emergency management, faculty, and monthly resident meetings; b) an email from the ED director (division chair) describing and supporting the study was sent out to the ED staff; c) respiratory therapists were informed during their monthly management meetings; and d) for a week prior to the study the nurse leadership informed the nursing staff through the twice-daily meetings before the start of each shift. At all of these meetings, an investigator explained the study and answered any questions that arose.

### 2.4 Follow-up Survey

After study completion a one-page, a 10-question follow-up survey was administered to the respiratory therapists, nurses, and attending and resident physicians, and who worked shifts in the ED during the study period. The survey evaluated the use of the paper-based flow diagram and electronic management system and protocol during the study period.

### 2.5 Study Design

We conducted a prospective, randomized controlled trial to evaluate a computerized disease detection and management system for asthma care. The study period took place over five

months: October 1, 2010-February 28, 2011, three weeks of which was excluded due to an informatics error. Patients identified by the Bayesian network [9, 15, 16] were randomized. The control group received the paper-based protocol at the end of triage when the nurse automatically printed the triage summary page. The electronic triage summary page displayed a required click-box reminder to acknowledge that the patient presented with symptoms compatible with an asthma exacerbation and that the protocol would print. The intervention group was enrolled in the computerized management system. The unit of randomization was the patient with an automated, computerized 6-patient block randomization schema. Clinicians were blinded to patient's randomization assignment, although prompts were visible on the electronic patient status board.

### 2.6 Selection of Participants

All patients presenting to the pediatric ED during the study period were screened for inclusion using the Bayesian network system [9, 15, 16]. The computerized disease detection system screens all patients for inclusion using a probabilistic algorithm (Bayesian network). The detection system's algorithm includes past medical history from the EMR, and the computerized triage application for details relating to the current visit [9, 16]. The detection system requires no additional data entry and operates in real-time. All patients presenting to the ED were screened for an asthma exacerbation during triage and the Bayesian network detection threshold was set to reduce alert fatigue. Patients identified through the Bayesian network were eligible and randomized for the study.

Patients were included if they were 2--18 years of age and were identified by the Bayesian network. Patients were excluded if they a) had an Emergency Severity Index = 1 (most severe, life-threatening condition), b) had no electronic triage, or c) eloped or left the ED prior to being seen by a physician. A sample size of 313 patients per group was needed to detect a difference in throughput time of 10% with a power of 0.8 and α= 0.05. The study was approved by the institutional review board and registered on clinicaltrials.gov.

### 2.7 Outcomes

The primary outcome measure was the time from ED triage to disposition decision. Either a discharge or hospital admission order (bed request order) in the patient tracking board was considered a disposition decision. Secondary outcomes were guideline adherence measures such as asthma education ordered, protocol found on chart, asthma scoring performed, ED length of stay, and hospital admission rate.

Data on each visit were collected from the available ED information system including the electronic medical record [10], electronic triage application [11] and ED patient status board [13]. A sensitivity of 85% was chosen for the Bayesian network to minimize alert fatigue while still capturing the maximum number of asthma patients. Based on historical data this would result in a specificity of 93.6%, positive predictive value of 65.3%, and negative predictive value of 98.7% [14]. To establish a reference standard for the diagnosis of an asthma exacerbation, a pediatric emergency medicine board-certified physician examined each patient visit within 7 days of the visit and determined whether an asthma exacerbation was present. To collect study data, a pediatric ED charge nurse performed chart reviews on

all patient visits. To ascertain data quality, a second, independent pediatric emergency medicine board-certified physician established a diagnosis for 20% of randomly selected patients' charts (k=0.8837; 95% CI: 0.817, 0.950).

### 2.8 Analysis

Primary analysis focused on detecting the associations between the use of an integrated electronic asthma management system (intervention) and time from ED triage to disposition decision, with comparison to the standard care system (control). The visit was the unit of analysis. Descriptive statistics, including means, standard deviations, and ranges for continuous variables such as time to disposition decision, length of stay, and age, as well as percentages and frequencies for categorical variables such as race, gender, insurance type, were provided to describe the study sample. Differences between group means for continuous variables were examined using ANOVA or Wilcoxon rank-sum test. Pearson chisquare tests were used to assess the categorical variables. All tests of significance were based on two-sided probabilities, at P values less than .05. Logistic regression was used to estimate the odds ratios (ORs) and 95% confidence intervals (CIs) for patient's disposition status, representing the overall odds of being admitted associated with the management system, and to adjust for potential confounding variables, including age, gender, race, insurance, language, acuity, and mode of arrival in the multivariate analysis. Kaplan-Meier curves were presented with log-rank test results to determine whether there were differences in the observed time to disposition decision as well as length of stay. Cox proportional hazards models were used for time to decision and length of stay separately, to determine whether there is a significant difference in the outcome variables between intervention and control, adjusting for the potential confounding variables. The adjusted p-values and the corresponding 95% confidence intervals were reported for multivariate analyses. All data analyses were carried out using statistical software R (Version 2.12.2).

## 3. RESULTS

### 3.1 Characteristics of study subjects

Among all the 19,559 pediatric ED patients during the study period, 13,896 were within the eligible age range (2--18 years) and screened by the asthma detection system. The Bayesian Network identified 1,339 patients having an asthma exacerbation (figure 2). As determined by the reference standard, 788 had a final diagnosis of asthma, yielding a positive predictive value of 69.9%. In the management system, the physician responded that the patient was not presenting with an asthma exacerbation 288 times; these patients are still included in the analysis. Patient demographics are shown in table 2.

Intervention and control patients did not differ significantly in time to disposition; intervention patients had a median time of 228 minutes (SD: 161 minutes, 95% CI: (208, 251)) and control patients a median time of 223 minutes (SD: 146 minutes, 95% CI: (208, 234)); p = 0.362). Intervention patients had a median length of stay 262 minutes (SD: 352 minutes, 95% CI: (241, 209)) and control of 247 minutes (SD: 354 minutes, 95% CI: (234, 272); p = 0.9863). Admission rates were similar between the two groups (intervention=25%, control=26%, p=0.867). Primary findings are shown in table 3.

The time to disposition decision for inpatients was 211 minutes (figure 3) and the time to disposition decision for outpatients was 330 minutes (figure 4).

Response rates for the clinician follow-up survey were (96%) for respiratory therapy, (51%) for nurses, and (67%) for physicians. Respiratory therapists who saw the protocol were not any more likely to use it than those who never reported seeing it (p=1.0). Nurses who saw the protocol were not any more likely to use it than those who never reported seeing it (p=0.41). Physicians who saw the paper-based protocol were not any more likely to use it compared to those who did not see the protocol (p=0.166). Clinician survey results are shown in table 4.

## 4. DISCUSSION

The study examined the automatic detection of eligible patients and the implementation of a fully computerized asthma management system to guide care compared to printing out the existing paper-based asthma protocol and attaching it to the chart. The goal of the study was to decrease time to disposition decision, and examine length of stay and guideline adherence measures such as asthma education, the protocol found on the chart, asthma scoring, and hospital admission rate. The study did not find a significant difference between the computerized management system and the paper-based system in time to disposition decision, length of stay, or the rate of hospital admission. There was no difference between the two groups in any of the guideline adherence measures. Despite a thorough educational element and support from the ED clinicians, the management system did not show a significant effect.

The average time to disposition decision was 3.8 hours, below the NHLBI guideline goal of 4--6 hours. This is a marked decrease from our previous study, in which the time to disposition decision was 4.8 hours and also within the recommended range [17]. The patient's time to disposition decision may be determined by the disease progression and response to treatment. It is possible that even with earlier scoring and treatment initiation, the disease progression would not be significantly changed. However, the triage score was automatically paged to the respiratory therapist and the therapist was able to start aerosol treatment via standing order before physician assessment. This standing order applied to all patients and respiratory therapists may have taken initiative to help start all patient treatments earlier regardless of the paged reminder.

The system did not provide an “intent to admit” option for the physicians. If a patient needed to be admitted but it was known that there were no beds open in the hospital, it is possible that a bed request was not placed. Therefore, these patients would benefit from an “intent to admit” option indicating the clinician has made a disposition decision but is unable to act on it yet. We did not provide disposition reminders until the patient's length of stay was at least 4 hours. It is possible that earlier and more frequent reminders would have helped encourage the physicians to make a disposition decision quicker, the rules were created to prompt the physicians only when a disposition decision should have already been made.

The guideline adherence measures were also not different between intervention and control groups. It is possible that the clinical staff are already providing care that adheres to the NHLBI guidelines. We examined charts for some of the guideline measures that may help to decrease ED re-visits: asthma education and a prescription for an inhaled corticosteroid [18]. Asthma education was already at 95% in the pediatric ED and remained high throughout the study. Take-home prescriptions of inhaled corticosteroids were charted in 82--84% of the asthma patients. The paper-based protocol was rarely found in the patient's chart. This is similar to the phase 1 study [17]. If the paper-based protocol was not written on, it may not have made it into the medical record. As elucidated in the first study, the protocols were frequently used as a guideline to reference and not a means of documentation.

This study was phase 2 in a two phase study design [14], where phase 1 compared the printed paper-based protocol to the standard of care [17]. Given an assumption that the system may be effective but have cross contamination, we compared phase 1 and phase 2 using phase 1 as a historical control. Neither study had a statistically significance difference in time to disposition decision (average = 288 minutes in phase 1, average = 224 minutes in phase 2) or ED length of stay (average = 331 minutes in phase 1, average = 255 minutes in phase 2). However, the operational characteristics of the ED during the two study periods including occupancy rate, average patient acuity, number of boarding patients, and average length of stay of boarding patients was significantly different (p<0.001) so no direct comparison can be made.

Clinician follow-up interviews revealed that most clinicians used the computerized management system in some form. More than half of the clinicians reported using the computerized patient status board portion of the asthma management system. The computerized patient status board scores were available for all clinicians to see, regardless of patient intervention. This may have contributed to a Hawthorne effect [19, 20] suggesting that the clinical staff were aware of being studied due to the unblinded nature of the computerized patient status board display, and therefore reducing the possible intervention differences between the two groups.

In the CPOE system, we removed the “cancel” button for patient scoring. This required all physicians to provide an asthma score for a patient if they were eligible. This screen is also where the prompts could be turned off. However, once the physician has scored the patient, they were free to cancel and leave the order sets if desired. Unfortunately, due to the nature of the display, we do not have data to confirm that asthma orders were placed using the order sets.

The study has several limitations. First, this is a single center study and the pediatric ED is highly integrated with using several information systems for patient care, which is not typical for many pediatric EDs and may limit the generalizability of the findings. However, more hospitals are installing electronic medical records and CPOE systems. The system uses commonly collected data elements to determine patient eligibility, and extensive analysis was performed to make use of the clinicians' existing workflow. Second, the Bayesian network only detected two-thirds of eligible patients and we do not have information about patients not detected. Due to the large number of patients screened by the system, it was not

feasible to find missed patients. However, the order sets were available to all physicians regardless of randomization and were not used during the study period.

When the system was originally prospectively evaluated [16], the negative predictive value was $69.8 \%$ and the positive predictive value was $79.3 \%$. Our test characteristics were chosen to suggest a negative predictive value of $98.7 \%$. Unfortunately, without the gold standard physician reviewing all 13,896 charts, we cannot create an accurate negative predictive value.

The pediatric ED treats a large number of asthma exacerbations; therefore, because the clinicians are very adept at treating asthma exacerbations, small changes in outcomes may be detected in EDs where clinicians are less familiar with diagnosis and treatment of asthma. The applicability of the asthma management system may be beneficial in smaller and lessexperienced EDs.

The control and intervention groups were similar in regards to time to disposition; therefore the computerized management system did not add additional waiting time. The system helped to increase communication and documentation for all patients.

The system integrated patient and clinician data to help the care team communicate more effectively. Based on this information, the patient's asthma scores could be more easily followed throughout the visit by the clinical care team. The computerized asthma management system represents a workflow oriented, sustainable approach in a challenging environment.

In summary, although the system did not influence time to disposition decision, we believe this management system to be a sustainable computerized management system to help standardize asthma care. We integrated the computerized management system with the existing workflow and were able to automatically identify and alert providers about patients presenting with an asthma exacerbation. While the automatic identification had good sensitivity, the system did not make an measurable impact on outcome measures relating to the timing of patient care for asthma in our ED.

# Acknowledgments 

This work was supported by NIH LM 009747-01 (Dr Dexheimer, Dr Aronsky) and NHLBI K23 HL80005 (Dr Arnold). The first author was supported by a Training Grant from the NLM (T15 LM 007450-03).

## Abbreviations

CPOE Computerized Provider Order Entry
ED Emergency Department
EMR Electronic Medical Record
NHLBI National Hearth Lung and Blood Institute

1. Akinbami LJ, Moorman JE, Liu X. Asthma prevalence, health care use, and mortality: United States, 2005--2009. Natl Health Stat Report. 2011 Jan; 12(32):1--14.
2. Qureshi F, Pestian J, Davis P, Zaritsky A. Effect of nebulized ipratropium on the hospitalization rates of children with asthma. N Engl J Med. 1998 Oct 8; 339(15):1030--5. [PubMed: 9761804]
3. National Heart Lung and Blood Institute (NHLBI), National Asthma Education and Prevention Program. Expert Panel Report 3 (EPR-3): Guidelines for the Diagnosis and Management of Asthma-Summary Report 2007. J Allergy Clin Immunol. 2007; 120(5, Supplement):S94--S138. [PubMed: 17983880]
4. Grimshaw JM, Eccles MP, Walker AE, Thomas RE. Changing physicians' behavior: what works and thoughts on getting more things to work. J Contin Educ Health Prof. 2002 Fall;22(4):237--43. [PubMed: 12613059]
5. Scribano PV, Lerer T, Kennedy D, Cloutier MM. Provider adherence to a clinical practice guideline for acute asthma in a pediatric emergency department. Acad Emerg Med. 2001 Dec; 8(12):1147--52. [PubMed: 11733292]
6. Dexheimer JW, Talbot TR, Sanders DL, Rosenbloom ST, Aronsky D. Prompting clinicians about preventive care measures: a systematic review of randomized controlled trials. J Am Med Inform Assoc. 2008 May-Jun;15(3):311--20. [PubMed: 18308989]
7. Hoeksema LJ, Bazzy-Asaad A, Lomotan EA, Edmonds DE, Ramirez-Garnica G, Shiffman RN, et al. Accuracy of a computerized clinical decision-support system for asthma assessment and management. J Am Med Inform Assoc. 2011 May 1; 18(3):243--50. [PubMed: 21486882]
8. Lomotan EA, Hoeksema LJ, Edmonds DE, Ramirez-Garnica G, Shiffman RN, Horwitz LI. Evaluating the use of a computerized clinical decision support system for asthma by pediatric pulmonologists. Int J Med Inform. 2012 Mar; 81(3):157--65. [PubMed: 22204897]
9. Sanders DL, Aronsky D. Detecting asthma exacerbations in a pediatric emergency department using a Bayesian network. AMIA Annu Symp Proc. 2006:684--8. [PubMed: 17238428]
10. Giuse DA. Supporting communication in an integrated patient record system. AMIA Annu Symp Proc. 2003:1065. [PubMed: 14728568]
11. Levin S, France D, Mayberry RS, Stonemetz S, Jones I, Aronsky D. The effects of computerized triage on nurse work behavior. AMIA Annu Symp Proc. 2006:1005. [PubMed: 17238624]
12. Miller RA, Waitman LR, Chen S, Rosenbloom ST. The anatomy of decision support during inpatient care provider order entry (CPOE): empirical observations from a decade of CPOE experience at Vanderbilt. Journal of biomedical informatics. 2005 Dec; 38(6):469--85. [PubMed: 16290243]
13. Aronsky D, Jones I, Lanaghan K, Slovis CM. Supporting patient care in the emergency department with a computerized whiteboard system. J Am Med Inform Assoc. 2008 Mar-Apr;15(2):184--94. [PubMed: 18096913]
14. Dexheimer JW, Arnold DH, Abramo TJ, Aronsky D. Development of an asthma management system in a pediatric emergency department. AMIA Annu Symp Proc. 2009; 2009:142--6. [PubMed: 20351838]
15. Sanders DL, Aronsky D. Prospective evaluation of a Bayesian Network for detecting asthma exacerbations in a Pediatric Emergency Department. AMIA Annu Symp Proc. 2006:1085. [PubMed: 17238704]
16. Sanders DL, Gregg W, Aronsky D. Identifying asthma exacerbations in a pediatric emergency department: a feasibility study. Int J Med Inform. 2007 Jul; 76(7):557--64. [PubMed: 16647876]
17. Dexheimer JW, Abramo TJ, Arnold DH, Johnson KB, Shyr Y, Ye F, et al. An asthma management system in a pediatric emergency department. Int J Med Inform. 2013 Apr; 82(4):230--8. [PubMed: 23218449]
18. Sin DD, Man SF. Low-dose inhaled corticosteroid therapy and risk of emergency department visits for asthma. Arch Intern Med. 2002 Jul 22; 162(14):1591--5. [PubMed: 12123402]
19. Mayo, E. The human problems of an industrial civilization London. New York: Routledge; 2003.

20. Roethlisberger, FJ., Dickson, WJ., Wright, HA., Pforzheimer, CH. Western Electric Company Management and the worker: an account of a research program conducted by the Western Electric Company, Hawthorne Works, Chicago. Cambridge, Mass: Harvard University Press; 1939.

# Highlights 

National asthma guidelines can improve care.
Automatic patient identification can be used to drive guideline initiation.
Despite integration with the EMR, a computerized asthma management system did not significantly improve time to disposition.

# SUMMARY POINTS 

## WHAT'S KNOWN

Asthma guidelines can improve patient care. Guideline implementation approaches benefit from an increased level of workflow integration, early initiation is integral to beginning severity-adjusted treatments promptly. The NHLBI guidelines emphasize early recognition and treatment of asthma exacerbations, as well as appropriate treatment stratified by severity.

## WHAT'S NEW

The goal of this study was to implement and evaluate a fully computerized asthma management system in a pediatric emergency department to help standardize care and reduce time to disposition decision.

This patient may be presenting with an asthma exacerbation. Please modify and confirm the pediatric asthma score shown below. $\square$ Check this box if the patient is not presenting with an asthma exacerbation (no further asthma prompts will be displayed in the order-entry system or on the whiteboard).


Last available asthma score: 2010-04-12 14:30 PAS: 10 (Mild/Moderate/Severe)

Figure 1. Computerized provider order entry pediatric asthma respiratory distress scoring screen.

![img-0.jpeg](img-0.jpeg)

Figure 2.
Consort Diagram.

# Time to Disposition Decision by Intervention

!![img-1.jpeg](img-1.jpeg)

**Figure 3.** Time to disposition decision for inpatients.

*Int J Med Inform.* Author manuscript; available in PMC 2017 June 06.

# Time to Disposition Decision by Intervention 

![img-2.jpeg](img-2.jpeg)

Time to Disposition Decision (mins)

Figure 4.
Time to disposition decision for outpatients.

# Table 1 

Asthma management system key components and availability.


Table 2
Patient demographics.


* LQ - lower quartile, UQ - upper quartile

Table 3
Primary findings.


* LQ - lower quartile, UQ - upper quartile

Table 4
Results from clinician follow-up survey.
