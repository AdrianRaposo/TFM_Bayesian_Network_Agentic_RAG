Carolina A. M. Schurink Stefan Visscher Peter J. F. Lucas Henk J. van Leeuwen Erik Buskens Reinier G. Hoff Andy I. M. Hoepelman Marc J. M. Bonten

## A Bayesian decision-support system for diagnosing ventilator-associated pneumonia

Received: 10 November 2006
Accepted: 8 May 2007
Published online: 16 June 2007
(c) Springer-Verlag 2007

Electronic supplementary material
The online version of this article (doi:10.1007/s00134-007-0728-6) contains supplementary material, which is available to authorized users.
C. A. M. Schurink $\cdot$ S. Visscher $\cdot$
H. J. van Leeuwen $\cdot$ A. I. M. Hoepelman $\cdot$ M. J. M. Bonten ( $\triangle$ )

University Medical Center Utrecht, Division of Internal Medicine, Geriatrics and Infectious Diseases, Heidelberglaan 100, HP F.02.126, 3584 CX Utrecht, The Netherlands
e-mail: mbonten@umcutrecht.nl
Tel.: +31-30-2507676
Fax: +31-30-2523741
P. J. F. Lucas

Radboud University, Institute for Computing and Information Sciences, Nijmegen, The Netherlands
H. J. van Leeuwen $\cdot$ A. I. M. Hoepelman $\cdot$ M. J. M. Bonten

University Medical Center Utrecht, Eijkman-Winkler Laboratory for Microbiology,
Heidelberglaan 100, HP F.02.126, 3584 CX Utrecht, The Netherlands

E. Buskens $\cdot$ M. J. M. Bonten University Medical Center Utrecht, Julius Center for Health Sciences and Primary Health Care,
Heidelberglaan 100, HP F.02.126, 3584 CX Utrecht, The Netherlands
R. G. Hoff

University Medical Center Utrecht, Division of Perioperative and Emergency Care, Heidelberglaan 100, HP F.02.126, 3584 CX Utrecht, The Netherlands

Abstract Objective: To determine the diagnostic performance of a Bayesian Decision-Support System (BDSS) for ventilator-associated pneumonia (VAP). Design: A previously developed BDSS, automatically obtaining patient data from patient information systems, provides likelihood predictions of VAP. In a prospectively studied cohort of 872 ICU patients, VAP was diagnosed by two infectious-disease specialists using a decision tree (reference diagnosis). After internal validation daily BDSS predictions were compared with the reference diagnosis. For data analysis two approaches were pursued: using BDSS predictions (a) for all 9422 patient days, and (b) only for the 238 days with presumed respiratory tract infections (RTI) according to the responsible physicians.

Measurements and results: 157 (66\%) of 238 days with presumed RTI fulfilled criteria for VAP. In approach (a), median daily BDSS likelihood predictions for days with and without VAP were $77 \%$ [Interquartile range (IQR) $=56-91 \%$ ] and $14 \%$ [IQR $5-42 \%, p<0.001$, Mann-Whitney U-test (MWU)], respectively. In receiver operating characteristics (ROC) analysis, optimal BDSS cutoff point for VAP was $46 \%$, and with this cut-off point positive predictive value (PPV) and negative predictive value (NPV) were 6.1 and $99.6 \%$, respectively [AUC $=0.857$ ( $95 \%$ CI $0.827-0.888$ )]. In approach (b), optimal cut-off for VAP was $78 \%$, and with this cut-off point PPV and NPV were 86 and $66 \%$, respectively [AUC $=0.846(95 \%$ CI $0.794-0.899)]$. Conclusions: As compared with the reference diagnosis, the BDSS had good test characteristics for diagnosing VAP, and might become a useful tool for assisting ICU physicians, both for routinely daily assessment and in patients clinically suspected of having VAP. Empirical validation of its performance is now warranted.

Keywords Ventilator-associated pneumonia $\cdot$ Decision-support system $\cdot$ Bayesian network

## Introduction

Ventilator-associated pneumonia (VAP) is the most frequently occurring nosocomial infection among mechanically ventilated patients in intensive care units (ICUs). Reported incidence rates of VAP have ranged from 5 to $67 \%$, depending on the selection of patients and the criteria used to establish its diagnosis [1].

In the absence of a clinically available gold standard, VAP is usually diagnosed according to a combination of criteria, such as systemic signs of infection, abnormalities on chest radiograph, and microbiological identification of pathogens; however, each of these criterion combines high sensitivity with low specificity. In an attempt to raise diagnostic accuracy, algorithms, such as the Centers for Disease Control definition for nosocomial pneumonia, and the Clinical Pulmonary Infection Score (CPIS), have been developed [2, 3]. Furthermore, invasive diagnostic techniques, such as bronchoalveolar lavage (BAL) and protected specimen brush (PSB), and quantitative analysis of microbiological cultures, have been proposed to better distinguish between colonization and infection of the respiratory tract [4-6]. Nevertheless, bronchoscopy includes a certain, though probably small, risk for complications and quantitative culturing is expensive and labor intensive. As a result, these techniques have not yet become common practice in most ICUs.

Presently, patient records have become fully computerized and linked to hospital information systems in many ICUs. These systems contain all relevant variables on which intensive care physicians base their clinical decision. In such a setting, computerized decision-support systems may assist in diagnosing VAP. For these purposes, a Bayesian approach seems most attractive, because these models are able to deal with uncertainties, such as missing values, can be improved by "self-learning," and can be linked to computerized patient record systems [7]. We developed such a Bayesian Decision-Support System (BDSS) for diagnosing VAP [8]. The aim of the present study was to compare the diagnostic properties of the BDSS with a reference diagnosis in two cohorts of mechanically ventilated patients. Firstly, in 872 consecutively admitted patients (and on each day of ventilation), and secondly, in a nested subgroup of 238 patients with a clinical suspicion of VAP (on the day of clinical suspicion only).

## Materials and methods

Setting
All patients admitted to two ICUs (a ten-bed medical ICU and an eight-bed neurosurgical ICU) of the University Medical Center Utrecht (UMCU) between 1 January 2000 and 1 January 2003 were included in this prospective cohort study. The UMCU is a 1062-bed tertiary care
hospital. As both ICUs are equipped with patient data management systems, all relevant clinical, laboratory, and microbiological variables are registered on a daily basis. Indications for antibiotic use, as judged by the attending physicians, and interpretation of chest radiographs by radiologists were manually added to the database. Patients receiving home mechanical ventilation were excluded. As no intervention was evaluated and daily care was not influenced by the study, the institutional review board waived the necessity of informed consent.

## Bayesian decision-support system

A Bayesian network (BN) is a graphical representation of a process (in our case VAP) involving a set of variables based on probability theory. A BN consists of nodes representing variables (containing tables with probabilities) and arrows, where the direction of an arrow indicates the relationship between the parent node and the child node. The qualitative part of a relationship between nodes is characterized by conditional probabilities. For each variable in the BN there exists an a priori probability distribution, representing what is known about a variable without any evidence. When there is evidence, for example clinical signs, the a posteriori distribution can be calculated based on these clinical signs. Bayesian networks are often used in fields where decision-making occurs under uncertainty, such as in healthcare. The BDSS for diagnosing VAP incorporates (conditional) probability distributions that were initially assessed subjectively, that is, either estimated (by C.A.M.S. and M.J.M.B.) or obtained from scientific literature. Fig. 1a shows the global structure of the model. Subsequently, the estimated probabilities (being the qualitative part of the model) were updated where needed using machine learning techniques [9]. This learning process was performed as follows:

1. A randomly selected subset ( $50 \%$ of the cases) of the data was used for learning the probability distributions on the basis of the models' original estimated probabilities.
2. The diagnostic performance of the new model was assessed by testing it on the remainder number of cases, i.e., the other half of the data set, and calculating the area under the receiver operating characteristics (ROC) curve.

This process was repeated ten times to rule out chance and to prevent for overfitting. The performance (measured in area under the ROC curve) of all ten potential models were compared, and the model with the median performance was considered our new model. (The results of these internal learning steps are not presented but are available upon request.)

![img-0.jpeg](img-0.jpeg)

Fig. 1 a Representation of the global architecture of the BDSS for VAP. b Diagnostic part of the BDSS for VAP in detail. (See ESM for additional information)

The diagnostic part (shown in detail in Fig. 1b) of the BDSS uses the variables body temperature, antipyretic drugs, blood leukocyte count, infiltrative abnormalities on chest X-ray (radiological signs), $\mathrm{PaO}_{2} / \mathrm{FiO}_{2}$ ratio, sputum production, sputum color, and duration of mechanical ventilation. The definitions of these variables are summarized in Table 1. One of the advantages of a Bayesian network is that, unlike other statistical models, such as, for example, logistic regression, it can handle missing values in such a way that when, for example, a patient's body temperature is unknown, still the posterior probability of having VAP can be calculated. On the basis of these variables and probability distributions, the BDSS calculates the likelihood, i.e., the posterior probability, of having VAP that ranges from 0 to $100 \%$. With the exception of information regarding chest radiographs and tracheal aspirate cultures, which had to be added manually, all information required for the BDSS network was automatically retrieved from patient information systems.

## Reference definition of VAP

In the absence of a gold standard for diagnosing VAP, a diagnostic decision tree was developed to categorize all clinically suspected episodes of VAP (Fig. 2). In this diagnostic decision tree aspects of different proposed diagnostic algorithms were combined [2, 3, 11]. Categorization was performed through independent adjudication by two reviewers (C.A.M.S. and M.J.M.B.) taking all relevant clinical, microbiological, and radiological criteria. Episodes of clinical suspicion of VAP (defined as days on which clinicians had prescribed antibiotics for presumed respiratory infections or infections without evident focus) were evaluated at the time of clinical suspicion as well as in the subsequent 3 days. Disagreement in categorization between both reviewers was resolved through discussion and consensus was achieved on all cases.

On the day of prescription of antibiotics fulfillment of criteria of clinical suspicion was determined (Fig. 2). The criteria of possible VAP, probable VAP, definite VAP, or definite absence of VAP were verified at day 3 in all patients with clinical suspicion of VAP. All episodes with "clinical suspicion," as well as "possible," "probable," and "definite" VAP were considered VAP. All analyses were performed for the categories "VAP" vs. "non-VAP," as well as for the different categories of severity of VAP ("clinical suspicion," "possible," "probable," and "definite" VAP vs. non-VAP).

## Statistical analysis

For data analysis two approaches were pursued. Test characteristics of the BDSS were determined for a situation in which all "VAP positive" and all "VAP negative" patient days $(n=9422)$ were included, as well as for the situation in which only the days that antibiotics were prescribed because of presumed respiratory tract infection $(n=238)$ were included. In the latter analysis, VAP diagnosis was confirmed, according to our reference test, in 157 days.

Daily predictions of the likelihood of VAP by the BDSS were retrospectively compared with the reference diagnosis of VAP. Data were expressed as absolute numbers with percentages and as means or medians with standard deviation or range. Subsequently, since VAP is considered a sub-acutely developing disease [12, 13], BDSS' predictions around the time of diagnosis for patients diagnosed with VAP were compared with BDSS' predictions for control patients not diagnosed with VAP during their stay in ICU. Controls were matched on gender, ICU ward, and number of mechanically ventilated days at the time of analysis.

Independent variables were compared by Mann-Whitney U-test or $t$-test, when appropriate, and Wilcoxon signed-rank test was used for non-independent variables.

Table 1 Definitions of variables used in the Bayesian Decision-Support System. Each variable relates to the period within 24 h before time of ventilator-associated pneumonia likelihood prediction


Table 2 Patient characteristics


A $p$-value less than 0.05 was considered statistically significant. Test characteristics of the BDSS were analyzed using ROC curves and by calculation of the likelihood ratio (LR) [14]. The SPSS statistical software (version 12, SPSS, Chicago, Ill.) for Windows was used to perform these analyses.

Hugin Professional software (http://www.hugin.com) was used to construct the Bayesian network model and to calculate all probabilities needed for our analyses.

## Results

In all, 872 patients ( 909 admissions) were included with a total of 9422 patient days (Table 2). Antibiotics were prescribed for presumed respiratory tract infection on day 238 (Fig. 2). Based on the diagnostic decision tree, 157 episodes ( $66 \%$ ) of VAP were diagnosed, subdivided into "clinical suspicion only" $(n=58)$, "possible" $(n=78)$, and "probable" $(n=21)$. There were no cases of definite

![img-1.jpeg](img-1.jpeg)

Fig. 2 Decision tree for diagnosing VAP: number of episodes of presumed respiratory tract infections (RTI) and number of episodes according to the definitions of VAP. (See ESM for additional information)

VAP. The overall incidence of VAP was $18 \%$ with an average incidence per patient-day of $1.7 \%$.

The BDSS correctly identified the days that VAP was diagnosed. Median likelihood prediction of VAP for these 157 days was $77 \%$ [Interquartile range (IQR) $=56-91 \%$ ],
as compared with $14 \%$ [IQR 5-42\%] for the 9265 days with absence of VAP ( $p<0.001$ ). Median likelihood predictions were $72 \%$ [IQR 39-90\%] for "clinical suspicion only," $89 \%$ [IQR 66-92\%] for "possible," and $88 \%$ [IQR $47-96 \%$ ] for "probable" VAP (Fig. 3).

In the days before VAP diagnosis, median BDSS posterior probabilities increased from $28 \%$ on day -3 , to $35 \%$ on day -2 and day -1 , to $77 \%$ on the day of VAP. In contrast, only small changes in posterior probabilities were observed in control patients (median values ranging from 16 to $20 \%$ ) during the three successive days. After diagnosing VAP, median posterior probabilities decreased from 77 to $30 \%$ on day $+1,28 \%$ on day +2 , and $29 \%$ on day +3 .

The ROC curve for BDSS predictions and VAP (yes or no, 157 episodes) had an area under the curve (AUC) of $0.857[95 \%$ CI $0.827-0.888]$, with an optimal cut-off point (optimal trade-off between sensitivity and specificity, as identified by SPSS) for diagnosing VAP of $46 \%$ (i.e., a prediction $>46 \%$ would be considered VAP). This cutoff point had a sensitivity and specificity of $80 \%$, with a positive predictive value (PPV) of $6.1 \%$ and a negative predictive value (NPV) of $99.6 \%$. For this cut-off point the likelihood ratio for a positive test (LR+) was 4.0. The AUC was somewhat higher for episodes fulfilling criteria of "possible" [AUC $=0.884$ ( $95 \%$ CI $0.842-0.925$, opti-

Fig. 3 Box plots for the different definitions of VAP. Statistical significant differences were determined between median predictions for Only clinical suspicion and Possible VAP ( $p<0.05$ ), and between Only clinical suspicion and Probable VAP $(p=0.05)$. (See ESM for additional information)

Distributions of the posterior probabilities for different definitions of VAP
![img-2.jpeg](img-2.jpeg)

mal cut-off $=52.6 \%$ )] and "probable" VAP [AUC $=0.875$ ( $95 \%$ CI $0.804-0.945$, optimal cut-off $=53.0 \%$ )], respectively. For episodes fulfilling criteria of "clinical suspicion only" the AUC was 0.818 ( $95 \%$ CI $0.765-0.871$ ), with an optimal cut-off point of $40.6 \%$.

In the second approach, the diagnostic performance of the BDSS was evaluated in the cohort of 238 patient-days on which antibiotics were prescribed for presumed respiratory tract infection (of which 157 episodes were considered VAP). Here, the optimal cut-off point for VAP was $78 \%$, with sensitivity and specificity of $79 \%$, PPV of $87 \%$, and NPV of $66 \%$. In this analysis the AUC was 0.846 ( $95 \%$ CI $0.794-0.899$ ), which hardly changed when using only episodes of "possible" [0.853 ( $95 \%$ CI $0.791-0.91695 \%$ CI)] or "probable" VAP [0.875 ( $95 \%$ CI $0.804-0.945$ )]. The LR for a positive test in this approach was 3.8.

## Discussion

A Bayesian Decision-Support System, linked to computerized patient record systems in the ICU, accurately predicted absence and presence of VAP. Two approaches for application were analyzed. When used on a daily basis, BDSS predictions had extremely high negative predictive values, but low positive predictive values. When restricted to the days that physicians prescribed antibiotics for presumed respiratory tract infections, BDSS predictions had excellent test characteristics and a positive predictive value of $87 \%$. Computerized decision-support systems might become accurate, relatively cheap, patient friendly, and safe adjuncts for intensive care medicine.

The goal of this study was to determine the diagnostic performance of the BDSS when compared with a reference diagnosis. For a more detailed introduction to Bayesians networks, a detailed description of the full model and an example of computing posterior probabilities given evidence, we refer to previously published work [7, 8]. Neither did we aim to compare classification performance of the BDSS with other statistical methods or to determine the impact of the BDSS on clinical practice; for the latter, a randomized trial comparing two diagnostic strategies for relevant outcome parameters is warranted.

The construction of our model has been based, as much as possible, on the available scientific evidence on the pathophysiology of VAP, and the conditional probabilities were subsequently tuned by machine learning techniques. Duration of exposure (ICU stay and mechanical ventilation) and colonization of the upper respiratory tract were considered the most important risk factors for VAP [15, 16]. In contrast, gastric colonization and contamination of ventilatory circuits were not included in the model, as there is cumulating evidence that gastric colonization is less relevant than colonization of the upper respiratory tract $[17,18]$ and that frequently changing ventilatory circuits, in attempt to minimize the risks of
contaminated equipment, has not been demonstrated to prevent VAP [19].

To the best of our knowledge, other BDSSs to diagnose VAP have not been described or evaluated before; however, other approaches for decision-making have previously been described. A well-known approach is the Clinical Pulmonary Infection Score (CPIS), proposed by Pugin et al. [3], taking into account the same clinical signs and symptoms as the BDSS described in this paper; however, one major difference between the CPIS score and our BDSS is the possibility for likelihood prediction with missing data. Moreover, the approach as proposed by Singh et al [20] includes reevaluation of the clinical situation at day 3 , after all patients have started with antibiotics at day 1 .

Previously described BDSSs for infectious diseases other than VAP considered choosing empirical therapy for bacterial infections [21], predicting the pathogens of bacteraemia originating from the urinary tract and from other sites [22-24], and diagnosing community-acquired pneumonia (CAP) [25]. This BDSS for diagnosing CAP was retrospectively evaluated in 41,371 patients that had visited an emergency department and for which a discharge diagnosis was known. Five hundred fifty-three patients were diagnosed with CAP. The BDSS had a sensitivity for diagnosing CAP of $95 \%$, with a specificity of $96.5 \%$, an area under the ROC curve of 0.98 , and a positive predictive value of $26.8 \%$. This model is now being used in the emergency room to identify patients with CAP [26], but prospective data on performance, effects on patient care, and outcome or cost-benefit analyses have not been reported to date.

The development and evaluation of our BDSS deserves some comments and one important limitation must be discussed. As all diagnostic studies for VAP, this study suffers from the absence of an available gold standard. An attractive alternative for the only true gold standard (i.e., histology) would be bronchoscopy with quantitative cultures. Yet, as this procedure was not common practice in our ICU, it could not be used for all patients; therefore, we defined a decision tree (Fig. 2) and prospectively categorized all patients with a clinical suspicion of VAP according to this scheme. It is noteworthy that this was performed before the BDSS model was used for calculation of likelihood predictions for VAP. Still, this does not exclude the possibility of misclassification. Another potential insufficiency is that we only included the days of initiation of antibiotic prescription for presumed respiratory tract infection or for infection without obvious focus in the decision tree. In this way we could have missed cases of VAP that were not treated with antibiotics. Yet, it is generally assumed that unnecessary treatment of presumed VAP occurs much more frequently than unnecessarily withholding treatment in patients with true VAP; therefore, our definition of patient inclusion probably had a high sensitivity to capture all episodes of true VAP. Nevertheless, in the ab-

sence of a gold standard, a prospective randomized trial is needed to determine the clinical benefits, expressed in patient outcome, antibiotic use, and costs of a new diagnostic test.

When used on a daily basis, BDSS predictions had a PPV of $6.1 \%$, which might seem low. Yet, with an overall incidence of $18 \%$ and average daily risk of $1.7 \%$, a diagnostic test with sensitivity and specificity of $95 \%$ would still have a PPV of only $25 \%$; therefore, even good diagnostic tests can have poor PPV in low-prevalence settings [27]. The incidence rates as observed in our study are fully comparable to incidences reported in other studies [1, 15], and this problem, therefore, seems unavoidable when using a diagnostic test in daily practice. The use of a BDSS in the daily assessment of patients might lead physicians to withhold antibiotics on days that the likelihood for VAP is low, and could thus be helpful in reducing unnecessary antibiotic use. The problem of low PPV is avoided when restricting the diagnostic test to those days on which the physician has a clinical suspicion of VAP. In such an approach BDSS predictions had excellent test characteristics (AUC $=0.846$ ), but, again, as compared with our reference standard.

The specificity of the BDSS for VAP was high, but not $100 \%$. There are several explanations for false-positive test results. Because of the complex disease presentations in critically ill patients, there is always the possibility of other infections, also associated with systemic signs of infection. In our cohort, though, a comparison of the days with clinical suspicions of VAP with all other days on which
no antibiotics were prescribed, reflecting absence of clinical suspicion of any infection, revealed similar sensitivity and specificity (data not given here). Another potential diagnostic problem is the sub-acute development of VAP, which may lead to false-positive predictions around the time of diagnosis. We therefore investigated whether patients developing VAP already had higher prediction likelihoods in the days before diagnosis, in a matched-cohort analysis. Indeed, in the days before VAP was diagnosed, median BDSS posterior probabilities increased from the days before VAP until the day VAP was diagnosed.

## Conclusion

We have presented the first attempt to use a fully automated Bayesian Decision-Support System for diagnosing and ruling out VAP. In two approaches (using it on a daily basis for all patients or only in cases of clinical suspicion of VAP) the system performed reasonably well. The next steps will be incorporation of pathogen prediction and antimicrobial therapy advice. The diagnostic properties of this model should be investigated further in other ICU populations and, preferably, compared with usual care in a randomized study design.
Acknowledgements. This study was supported by a grant from ZonMw (project number 2100.0035), and NWO (project number 634.000.026) for the TimeBayes project. We are thankful to P. van der Werken and J. van Wolffelaar for developing the user interface and their help with retrieving data from the clinical database server, and to A. Hoes for helpful comments.
