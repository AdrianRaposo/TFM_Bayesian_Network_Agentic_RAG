# HHS Public Access 

Author manuscript<br>JACC Heart Fail. Author manuscript; available in PMC 2017 September 01.

Published in final edited form as:
JACC Heart Fail. 2016 September ; 4(9): 711-721. doi:10.1016/j.jchf.2016.04.004.

## A Bayesian Model to Predict Right Ventricular Failure following Left Ventricular Assist Device Therapy

Natasha A. Loghmanpour, PhD ${ }^{1}$, Robert L. Kormos, MD ${ }^{2}$, Manreet K. Kanwar, MD ${ }^{3}$, Jeffrey J. Teuteberg, MD ${ }^{2}$, Srinivas Murali, MD ${ }^{3}$, and James F. Antaki, PhD ${ }^{1}$<br>${ }^{1}$ Department of Biomedical Engineering, Carnegie Mellon University, Pittsburgh, PA<br>${ }^{2}$ Heart and Vascular Institute, University of Pittsburgh Medical Center, Pittsburgh, PA<br>${ }^{3}$ Cardiovascular Institute, Allegheny Health Network, Pittsburgh, PA


#### Abstract

Background—Right ventricular failure (RVF) continues to be a major adverse event following left ventricular assist device (LVAD) implantation. This study investigates the use of a Bayesian statistical model to address the limited predictive capacity of existing risk scores derived from multivariate analyses. This is based on the hypothesis that it is necessary to consider the interrelationships and conditional probabilities amongst independent variables to achieve sufficient statistical accuracy.


Methods-The data used for this study was derived from 10,909 adult patients from INTERMACS who had a primary LVAD from December 2006 - March 2014. An initial set of 176 pre-implant variables were considered. RVF post-implant was categorized as acute ( $<48$ hours), early ( 48 hours-14 days) and late ( $>14$ days) in onset. For each of these endpoints, a separate treeaugmented Naïve Bayes model was constructed using the most predictive variables using an open source Bayesian inference engine (SMILE.)

Results-The acute $R V F$ model consisted of 33 variables, including: systolic pulmonary artery pressure (PAP), white blood cell count, left ventricular ejection fraction, cardiac index, sodium levels, and lymphocyte percentage. The early $R V F$ model consisted of 34 variables, including systolic PAP, pre-albumin, LDH, INTERMACS profile, right ventricular ejection fraction, pro-Btype natriuretic peptide, age, heart rate, tricuspid regurgitation and BMI. The late RVF model included 33 variables and was mostly predicted by peripheral vascular resistance, MELD score, albumin, lymphocyte percentage, mean PAP and diastolic PAP. The accuracies of all the Bayesian models were between $91-97 \%$, AUC between $0.83-0.90$ sensitivity of $90 \%$ and specificity between $98-99 \%$, significantly outperforming previously published risk scores.

[^0]
[^0]:    Corresponding Author: James F. Antaki, Department of Biomedical Engineering, 700 Technology Drive, Carnegie Mellon University, Pittsburgh, PA, 15219, Tel: 412-268-9857, Fax: 412-268-9807, antaki@cmu.edu.
    Publisher's Disclaimer: This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

    ## Disclosure

    None of the authors have any financial relationship with any commercial entities that have an interest in the subject of the presented manuscript or other conflicts of interest to disclose.

Conclusion—A Bayesian prognostic model of RVF, based on the large, multi-center INTERMACS registry provided highly accurate predictions of acute, early, and late RVF based on preoperative variables. These models may facilitate clinical decision-making while screening candidates for LVAD therapy.

## Keywords

Left Ventricular Assist Device; Right Ventricular Failure; Bayesian; Risk Stratification

## Introduction

Left ventricular assist devices (LVADs) are increasingly used for management of patients with end-stage heart failure, both as bridge to cardiac transplantation and as destination therapy (DT). Post-operative right ventricular failure (RVF) is known to contribute significantly to post-LVAD morbidity and mortality. The risk of development of RVF after LVAD implantation is multifactorial and dependent on hemodynamic variables such as RV preload and afterload as well as clinical variables such as hepatic and renal function, amongst others. There have been numerous publications examining risk factors associated with RVF over the past decade that have led to the development of several risk scores for RVF (1--13). These scores are comprised of weighted sums of 4--7 risk factors, which do not contribute much sensitivity or specificity. Furthermore, the accurate prediction of patients at risk to develop RVF after implantation of a continuous flow LVAD depends on the complex and dynamic interplay of multiple pre-operative variables which cannot be adequately captured by traditional multivariate modeling. In contradistinction, Bayesian Network (BN) algorithms can account for nonlinear interactions between variables by identifying groups of risk factors and their conditional inter-dependency.

## Methods

We sought to develop a Bayesian-based prognostic model of RVF following implantation of a continuous flow LVAD, utilizing the Interagency Registry for Mechanically Assisted Circulatory Support (INTERMACS).

## Patient Cohort

The study described in this submission was approved by the INTERMACS Data, Access, Analysis, and Publication Committee (DAAP). The Data Coordinating Center at University of Alabama at Birmingham provided us with de-identified patient data for implants between December 2006 and June 2014 (n=10,909). (See Supplemental Table 1.) The inclusion criterion for this study was the use of a continuous flow LVAD as the primary implant and age ≥ 18. Patients who received a right ventricular assist device (RVAD) were included as long as the initial implant was an LVAD. Total Artificial Heart recipients were excluded from this study.

## RVF Definition

The definition for RVF was based on the INTERMACS definition prior to 2014. (See Appendix A, available online: www.intermacs.com.) We studied three RVF end points: <48

hours (acute onset), 48 hours - 14 days (early onset), and >14 days (late onset). These end points were chosen to stress upon the fact that different clinical variables affect the risk of RVF at different time points. Therefore, we considered how the model might be used in clinical practice and highlight the differences in the associated set of risk factors, which in turn may provide insights towards the mitigation of the risk. The first end point (acute) refers to the immediate intra-operative and post-operative period (<48 hours) in which the surgical team might use the information to consider whether or not to implant a temporary or permanent right-ventricular assist device (RVAD). The next period (early: 48 hours-14 days) generally considers the duration ICU to initial discharge from hospital. The clinical response to this risk might involve pharmacological management of RV function or PVR; or possibly the use of a temporary RVAD. Late (>14 days) would be used to alert the follow-up care provider to be vigilant about the risk of RVF, and to be prepared to intervene if necessary. Also, chronic or late RVF (>14 days) is being increasingly recognized as an adverse event and may occur in patients who do not develop acute or early RVF.

# Missing Data 

The data entries in the INTERMACS registry exhibited varying degrees of missing-ness. (See Supplemental Table 2.) Data elements with excessive missing data ( $>90 \%$ ) were excluded from the analysis. Of the pre-implant variables remaining, both numeric and categorical missing data elements were imputed ( 5 iterations) using the Random Forest Multiple Imputation by Chained Equation (rfMICE) method using the open source R statistical environment (14). The average of all 5 iterations were used for the final imputed value.

## Discretization

The Bayesian methodology requires the discretization of continuous variables. (See Supplemental Table 3.) This was performed by assuming a normal, Gaussian distribution and defining breakpoints at one standard deviation above and below the mean, thereby creating three ranges, or classes (below average, average and above average). Lower bounds were truncated if the breakpoint was less than zero. In some cases, a fourth range was defined (well above average: if the distribution had a negative, left-sided skew). Examples of discretized intervals include BMI ( $\leq 22.0,22.0-28.7,28.7-35.3, \geq 35.3$ ), INR ( $\leq 0.89$, $0.90-1.34,1.35-1.80, \geq 1.81)$ and CVP $(\leq 7.6,7.7-11.4,11.5-15.2, \geq 15.3)$. The above discretization was performed using commercial statistical software (IBM SPSS Statistics, 2013, Version 22.0).

## Bayesian Networks

BNs (15) incorporate informational relationships and processes individual patient data to predict probable outcomes for survival and adverse events. These networks can encode both qualitative and quantitative knowledge and provides a rigorous framework to perform inference on predictive variables that are readily interpreted. These are often represented diagrammatically, in which nodes represent independent variables and directed edges (arrows between nodes) represent influences between those variables. Absence of an arrow between a pair of nodes implies independence between those variables. This adds to the practicality of BNs for this application. BNs are equipped with conditional probability tables

(CPTs) associated with each node, that describe both the direction and magnitude of influence between variables. The methods used for the present study evolved from our prior experience with machine learning for decision support applied to various VAD cohorts (6--8,16--22). For this study, we utilized the Tree-Augmented Naïve Bayes (TAN) architecture, which adds one level of complexity to the Naïve Bayes network. TAN allows independent variables to both directly, and indirectly impact the outcome through their influence on other variables. All Bayesian models were graphed using GeNIe 2.0 (23) developed at the University of Pittsburgh in the School of Information Science.

## Selection of Variables

After eliminating sparse variables with excessive missing data, eliminating redundancies by the clinical authors (e.g. age and contraindication for VAD due to age) and eliminating irrelevant variables (e.g. education level) further variables were eliminated that would cause over-fitting the model to the data. In the present study, this was measured by information gain (24), which is based on the same principle as decision trees. This process provides ranking of variables based on their influence on outcome.

## Derivation of Model Structure

All BN classifiers were derived on an independent dataset comprised of a training set of approximately 90% of the data records and a testing set from the remaining approximate 10%, also known as ten-fold cross validation. This same process was repeated for evaluating the performance of the models. The reduced datasets for each of the three RVF time points were reviewed by the clinical authors to further refine the variables to be included and remove redundancies that may have been included in the registry data (e.g. representing Hemoglobin and Hematocrit as separate variables). The interested reader is referred to our previously published study (17) for further details of the procedure.

## RVF Score Comparison

We compared the performance of our models with that of the RVF risk score (RVFRS) published by Matthews et al (5) and the Drakos score (3) as these were the two most cited and widely used scores for RVF in an LVAD population. The RVFRS was calculated by summing points awarded for the presence of a vasopressor (4 points), AST ≥80 IU/L (2 points), bilirubin ≥2.0 mg/dl (2.5 points) and creatinine ≥2.3 mg/dl (3 points). The resulting score is stratified as low risk (RVFRS ≤3.0, 0.49 likelihood ratio of RVF), medium risk (RVFRS 4.0--5.0, 2.8 likelihood ratio) and high risk (RVFRS ≥5.5, 7.6 likelihood ratio). The Drakos score was calculated as the sum of points assigned for existence of each of the 8 perioperative variables: destination therapy patients (3.5 points), intra-aortic balloon pump (4 points), pulmonary vascular resistance (PVR) ≤1.7 WU (1 point), PVR 1.8--2.7 (2 points), PVR 2.8--4.2 (3 points), PVR ≥4.3 (4 points), inotrope dependency (2.5 points), obesity defined as BMI ≥30 kg/m^{3} (2 points), angiotensin-converting enzyme inhibitor and/or angiotensin II receptor blocker (-2.5 points) and β-blocker (2 points). The resulting risk score are stratified as: low risk (score ≤5.0, 11% risk RVF), medium risk (score 5.5--8.0, 37% risk RVF), high risk (score 8.5--12, 56% risk RVF) and very high risk (≥12.5, 83% risk RVF). When applied to INTERMACS data, missing values for either score were imputed using the same rfMICE methods described previously. (See Table 1.)

Performance Metrics

To compare the performance and results of the Bayesian models, RVFRS and Drakos score, we used the area under the receiver operator characteristics curve (AUC). The ROC curves were plotted using SPSS (IBM SPSS Statistics, 2013, Version 22.0). For the Bayesian models, we also report the accuracy, sensitivity and specificity computed in GeNIe (32). These metrics cannot be calculated for the risk scores, as they do not provide an actual prediction of RVF, but instead stratifies the patients into risk levels associated with certain percentages of RVF prevalence.

## Results

There were a total of 10,909 patients who met the inclusion criteria. The majority were between the age of 50--69 years (n=6,568; 60%), 78% (n=8606) were male, 3,811 (35%) patients received the LVAD as destination therapy (DT) and 6,901 (63%) patients were listed as bridge to transplantation (BTT). Ischemia was listed as the cause for cardiomyopathy in 4,466 (41%) patients. At the time of implantation, 17% (n=1,900) were designated as INTERMACS profile 1, 38% (n=4,169) of the patients were categorized as INTERMACS profile 2, and 26% (n=2,875) as INTERMACS profile 3. Overall 18.5% of the patients (n=2,024) were diagnosed with RVF, 2.7% (n=293) with acute RVF, 9.5% (n=1,036) with early RVF and 6.4% (n=695) with late onset RVF.

The accuracy, area under the ROC curve (AUC), sensitivity and specificity are summarized in Figure 1 and Table 2, respectively. The accuracies of all three models ranged between 91--97%, and their AUC ranged between 0.83--0.90, significantly outperforming all previously published risk scores. The Bayesian models for acute (<48 hours), early (between 48 hours and 14 days) and late (>14 days) RVF are illustrated in Figures 2--4. The variables are color-coded according to four categories: hemodynamics, medications, laboratories or demographics.

### Acute RVF model (< 48 hours)

The acute RVF model contained 33 variables with 65 direct relationships among the variables and directly to the outcome (Figure 2). Although the order of influence changes as variables are observed or specific (i.e. while calculating the risk for a specific patient), the variables most predictive of RVF given the population distribution included systolic pulmonary artery pressure (PAP), white blood cell (WBC) count, left ventricular ejection fraction (LVEF), cardiac index (CI), sodium levels, lymphocyte percentage, hemoglobin, and heart rate (HR).

### Early RVF model (48 hours -- 14 days)

The early RVF model contains 34 variables with 67 direct relationships (Figure 3). The top 10 variables most predictive of RVF given the population distribution were: systolic PAP, pre-albumin, lactate dehydrogenase (LDH), INTERMACS profile, right ventricular ejection fraction (RVEF), pro-B-type natriuretic peptide (pro-BNP), age, HR, tricuspid regurgitation and body mass index (BMI).

Late RVF model (> 14 days)

The late RVF model also contains a different subset of 34 variables with 67 direct relationships. (See Figure 4.) The variables most predictive of RVF given the population distribution include peripheral vascular resistance (PVR), model for end-stage liver disease (MELD) score, device strategy (destination therapy versus bridge to transplantation), use of inotropes, primary diagnosis (HF etiology), albumin, lymphocyte percentage, mean PAP and diastolic PAP.

## Drakos Risk Score and RVFRS

For benchmark comparison, we computed the RVFRS as well as Drakos Risk Score with the INTERMACS registry data. The corresponding AUCs were 54.7% and 49.8% for the RVFRS and Drakos scores, respectively. It can be seen in Figure 1 that these curves closely approximate the line of unity, with the Drakos Risk score performing worse than random chance. These were considerably lower than reported in their originally published studies (74% and 73%, respectively.) (3,5).

When first introduced, the Drakos score compared the survival among the 4 different categories (<5.0, 5.5 to 8, 8.5 to 12, and > 12.5 points). The corresponding 30-day survival rates after LVAD were reported as 97%, 92%, 85%, and 83% (log-rank for linear trend p < 0.029), and the 180-day survival was reported as 94%, 85%, 75%, and 72% (p < 0.009). When applied to the INTERMACS data the Drakos score did not significantly differentiate survival amongst the four categories. However, it is important to notice the relatively even distribution of RV failure across the different groups: low (n=2573, 16% RVF), medium (n=3670, 17% RVF), and high (n=3737, 20% RVF), and very high (n=929, 24% RVF) in the INTERMACS data compared to the original derivation cohort (Supplemental Table 4).

When first published, RVFRS was shown to significantly stratify survival at 180 days: 66 ± 9%, 80 ± 8%, and 90 ± 3% for the high, medium, and low RVFRS strata, respectively, and a log rank for linear trend p < 0.0045, showing an increased risk of mortality with greater RVFRS. Although the risk strata of the RVFRS had significantly different survival when applied to the INTERMACS cohort it did so to a lesser degree. The high-risk stratum had a distinctly lower survival rate, but the medium and low risk strata overlay each other by approximately 9 months. Unlike the Drakos score, the RVFRS was highly skewed towards the low risk stratum (n=9623, 19% RVF), with relatively few identified as medium risk (n=856, 15.8% RVF) and high risk (n=430, 17.2% RVF) patients.

## Discussion

Despite improving VAD technology and increasing focus on pre-emptive strategies to medically optimize the patient's physiology pre-operatively, adverse events are common and significantly impacts survival and quality of life after LVAD implantation. This is partly due to the heterogeneous and complex nature of these patients, rendering generalized recommendations for patient selection or those derived from small patient cohorts only partly helpful. Specifically, for RVF it is critical to identify the patients who will successfully tolerate isolated LVAD implant without RV failure at the time of surgical

decision making. Recent studies, using the INTERMACS registry, have been performed to identify individual clinical variables, such as INTERMACS profile and elevated PVR, that might be predictive of RVF (25).

These analyses reveal a wide variety of risk factors from disparate categories (e.g. nutrition, hemodynamics, laboratories, history, etc.). These data, in turn, can inform clinical decisionmaking. However, in clinical practice, evaluation for risk for RVF is a dynamic process that incorporates many pathways of information including physical examination findings, laboratory results, imaging and hemodynamic data. Existing risk scores attempt to combine a multiplicity of factors by using a weighted summation. But, in reality some (most) risk factors are inter-related; i.e. they will affect dissimilar patients differently. Depending on prevailing conditions, some factors may increase the risk in one patient, yet reduce the risk in another. For example, the AST ≥ 80 IU/L allows for 2 points in the RVFRS, which may elevate an otherwise medium risk patient to a high risk category. Elevated AST is usually a reflection of liver congestion and aggressive optimization within days preceding an LVAD could result in lowering this value to < 80 IU/L transiently. This would then re-categorize the patient from a higher to lower risk group. But in clinical practice we all realize the dynamic interplay between cardiac output, RV failure, elevated transaminases and renal dysfunction. Even though a lower AST level implied a lower pre-operative risk, the fact that it was achieved using inotropes, aggressive diuresis and possibly temporary balloon pump support days before LVAD placement may only imply a more subtle improvement in the risk of RVF in this patient than represented by RVFRS. In the current study we found that the accuracy of both RVFRS and the Drakos score in predicting RVF in the INTERMACS registry was virtually equivalent to a flip of a coin. We acknowledge that these scores might have performed better if calibrated to the same training set as used for our Bayesian models, however it would be mathematically impossible to outperform the Bayesian models when using a weighted summation of variables with fixed coefficients.

We previously endeavored to model the complexity of determining the risk of RVF (based on the need for an RVAD) using a Decision Tree classifier (6--8). This provided promising results, but was limited to a single center and a combination of pulsatile and continuous flow LVADs. The Bayesian models reported here are particularly suited for combining large sets of risk factors because they are based on conditional probabilities of the likelihood of RVF for a given combination of inter-related variables. In this way, these algorithms better reflect human logic in prioritizing dynamic clinical information, yet benefiting from the corpus of evidence provided by the INTERMACS registry. To the best knowledge of the authors, this is the first report of a prognostic model of RVF following continuous flow LVAD utilizing the INTERMACS database and to adopt machine learning methods for statistical analysis.

In the current study, each of the three independent models for RVF consisted of 33--34 pre-operative variables from several categories: demographics, laboratory values medications, and hemodynamics. This allowed for inclusion of variables such as measures of nutrition (pre-albumin, cholesterol, lymphocyte count), functional class (6 minute walk distance), re-hospitalizations (recent cardiac hospitalization) in addition to the more apparent hemodynamic (PAP), laboratory (BNP, sodium) and imaging (LV end diastolic diameter) factors in the calculation of risk assessment. Because the selection of variables, and their

inter-dependence was determined automatically by the computer algorithm, not all variables appear intuitive. And some of the inter-relationships are difficult to interpret biologically. While biologic plausibility is not always necessary for an accurate predictive model, it does lend credibility to the associations. Fortunately, the structure of the Bayesian tree is relatively "flexible" inasmuch as inter-connections can be changed, removed or added manually without necessarily impairing the accuracy of the model. Therefore, the clinician has the freedom to modify the structure (within bounds) to correspond more logically with his/her reasoning and understanding of the underlying physiology/pathology.

# Limitations 

Limitations of this study include: missing data, skewedness towards absence of RVF (which reduces the sensitivity), and the variety of aberrations that are intrinsic to a retrospective study using a registry data set. Multiple imputation methods were investigated to address the missing data entries. The choice to exclude data with $>90 \%$ was determined by trial-anderror, but we acknowledge was somewhat arbitrary. However most of the variables included in the three models had less than $5 \%$ missing data and only a few variables had missing data exceeding $50 \%$. Choosing a lower cutoff would reduce the errors associated with imputation, but at the cost of eliminating potentially important variables. An unfortunate consequence of lack of data was our inability to include the severity of RVF in the model. Also, we acknowledge that patients who were deemed too great a risk for RVF and who therefore never received an LVAD were excluded from the registry. Additional variables that may impact the risk of RVF in clinical practice, such as bypass time, blood products used and dose of inotropes were not available in the INTERMACS registry and thereby for our analysis. We also recognize errors due to the variability of timing of data entry into the registry, particularly those variables that are most dynamically changing in practice. Finally we acknowledge that the criteria for diagnosing RVF in the INTERMACS dataset is heterogeneous. Not all patients who were declaring having RVF received an RVAD. (Surprisingly, there are cases in the INTERMACS registry of patients who did receive and RVAD who were NOT identified as having RVF.)

Many of the aforementioned limitations will be addressed in an ongoing multi-site prospective study.

## Conclusions

This is the first application of Bayesian analysis to predict the risk of RVF in a large, multicenter LVAD cohort. Three separate Bayesian models for acute, early and late RVF substantially outperformed the existing risk scores in their ability to predict the risk of RV failure. These models show great promise as a reliable and accurate risk stratification tool for clinical decision making.

## Clinical Perspective

When implementing the BN model with a particular patient, it can accept numerous combinations of input variables to compute the risk of RVF. In other words, the model can

predict the likelihood of RVF even with a limited, incomplete set of data. But if additional data points are added (as they become available), the predictive ability of the algorithm improves incrementally. To illustrate, we consider a VAD patient for whom, initially, no additional data is known. Based on the current INTERMACS registry report, the baseline probability for late RVF is $12 \%$. Now if we add the observation of high systolic PAP ( $=65$ mmHg ) this increases this risk to $62 \%$. If we then include the observation of $\mathrm{CI}=2.5$, the risk of RVF risk increases to $77 \%$, and then to $92.4 \%$ if the patient has an elevated WBC count of $10 \times 10^{9} / \mathrm{L}$. The latter sequence of steps is depicted in Figure 5. In a second hypothetical high-risk patient scenario with the same baseline risk and systolic PAP, entering a condition of hypotension with a systolic blood pressure of $86-102 \mathrm{mmHg}$ increases the calculated risk of RVF to $66 \%$. Further observation that the patient has a moderately reduced pre-operative RVEF, the model now calculates the risk to be $83 \%$. In a third scenario, addition of high lymphocyte count increases the $12 \%$ baseline risk to $27 \%$, and further observing the mean PAP $\geq 36 \mathrm{mmHg}$ increases the risk to $49 \%$. These scenarios exemplify the dynamic interdependency of various risk factors on the final clinical outcome, which is unique to Bayesian analysis. This provides the possibility to examine the changes in risk over time, as well as explore hypothetical "what if" scenarios by entering variables manually. One could even envision entering variables inter-operatively, thereby acknowledging recent reports of the importance of intra operative events to the occurrence of post-operative RV failure.

# Translational Outlook 

We recognize that the utility of these Bayesian models, containing over 30 variables, will depend greatly on the ease/difficulty by which it can be calculated. For this reason, our ongoing work aims to provide an accessible and easy-to-use decision support tool for physicians and patients engaged in LVAD discussion. Titled CORA (Cardiac Outcomes Risk Assessment), this application will be provided in the form of an interactive, graphic interface accessible on smartphones and other devices that would be integrated with commonly available electronic medical records (such as Epic). A prototype screen is depicted in Figure 5 .

It will provide the user access to all the Bayesian models derived for predicting adverse events (including RVF) and mortality in a patient being evaluated for an LVAD. ${ }^{1}$

## Supplementary Material

Refer to Web version on PubMed Central for supplementary material.

## Acknowledgments

We would like to thank the Data Access, Analysis, and Publications Committee of INTERMACS for allowing us to use their registry for the study, and specifically thank Dr. James Kirklin, Dr. Francis Pagani and Dr. David Naftel. We would also like to thank Susan Meyers and Grant Studdard for their administrative, database, and statistical assistance with INTERMACS. We are grateful for the contributions of Dr. Marek Druzdzel and the Decision Systems Laboratory at the University of Pittsburgh.

[^0]
[^0]:    ${ }^{1}$ The reader is invited to contact the corresponding author for access to the beta version of the web based application.

# Funding Source 

Funding for this work was provided by the National Institute of Health (NIH) Division of National Heart, Lung, and Blood Institute (NHLBI) grants: R41 HL120428 STTR Phase I Cardiac Health Risk Stratification System, R01 HL122639 CORA ${ }^{\text {TM }}$ : a Personalized Cardiac Counselor for Optimal Therapy, R01 HL086918 Identification and Optimization of Ventricular Recovery of Patients on Ventricular Assistance.

## Abbreviations

