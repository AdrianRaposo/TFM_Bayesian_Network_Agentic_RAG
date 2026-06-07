# Disabling and reoperation in patients with Crohn's disease subject to early surgery or immunosuppression: a Bayesian network prognostic model 

Cláudia Camila Dias<br>CIDES \& CINTESIS<br>Faculty of Medicine, University of Porto<br>Porto, Portugal<br>camila@med.up.pt

Fernando Magro
MedInUP
Institute of Pharmacology \& Therapeutics
Faculty of Medicine, University of Porto
Porto, Portugal
fm@med.up.pt

Pedro Pereira Rodrigues<br>CINTESIS \& LIAAD - INESC TEC<br>Faculty of Medicine, University of Porto<br>Porto, Portugal<br>pprodrigues@med.up.pt

Abstract- Crohn's disease is one type of inflammatory bowel disease whose incidence is currently increasing, subject to relapse and disabling, with unknown etiology, and usually diagnosed between the second and third decade of life. The aim of this work is to develop a Bayesian network tool to predict disabling and reoperation in patients with Crohn's disease subject to early surgery or immunosuppressors intake. Multi-centric study data from patients with surgery or immunosuppression in the first six months after diagnosis was used, focusing on the prognosis and the analysis of factors' interaction. Patients were grouped by the index episode: immunosuppressors intake, and surgery (stratified considering the use or not of immunosuppressors 6 months after surgery). Patient group was associated with disease behavior, upper gastrointestinal tract location (L4) and age at diagnosis, while disease extent was associated to perianal disease. For disabling, association between perianal disease and gender and location was also found. Association between gender and L4 was also found for reoperation. The cross-validated discriminative power of the models were high for both disabling (above 70\%) and reoperation (above 80\%). The generated models presented interesting insights on factor interaction and predictive ability for the prognosis, supporting their use in future clinical decision support systems.

Keywords: prognosis; Crohn's disease; clinic decision support; Bayesian network models

## I. INTRODUCTION

Crohn's disease is a chronic illness with unknown etiology usually diagnosed during the second and third decade of life. The interaction between genetic and environment factors had a important role in the etiology of the disease [1].

The disease could had along periods of remission but the more aggressive cases requires more aggressive interventions like surgery [2] but, being a chronic disease, neither treatment nor surgery actually heals the patients, yielding frequent medical visits and hospitalizations, which in turn creates uncertainty about the professional and social future of patients and their families [3].

The treatment of Crohn's disease has changed in the last decades. Strategies like step-up or top down treatments have been more frequently chosen. The top-down strategy is based on the very early use of intensive therapy (immunosuppressive and/or biologics) to maintain a good quality of life from the first flare-up of the disease and prevent any irreversible consequences [4].

In our day the principal focus of treatment has been the improvement of quality of life, reduction of surgeries or hospitalization, besides the sole control of symptoms. Since the treatment plan clearly affects the disease course, focus has been given to identifying good prognostic models based on clinical/demographic factors since they are more easily included in daily clinical practice [5], [6].

However, prognostic studies show heterogeneous results, likely as a result of using different methodologies and/or applying different criteria for selection and evaluation. In addition, predicting the prognosis is a considerably uncertain task, so the development of predictive models also requires research. Also, traditional biostatistics is no longer enough to cope with the real-world biomedical data and it is necessary to look to other techniques [7]. Bayesian networks are a good choice since they deal well with prior knowledge, collected in published evidence included in quality literature or in primary or secondary data sources, and transform the data analyses in a process of updating the prior knowledge with available evidence at inference time [9], dealing better than other models with the uncertainty in the data. Bayesian networks are represented by a qualitative model (which describes the relations among variables) and a quantitative model (which gives the joint probability of all variables) which allows the inspection of marginal probabilities for each variable's state, and their use in the computation of a posteriori probabilities for single patients at inference time [10].

A preliminary study on the problem constituted a proof-of-concept for the use of Bayesian network classifiers as prognostic predictor model for disabling of prognostic prediction of disabling [15]. However, a thorough follow-up clinical appraisal of those results revealed that the analysis of immunosuppressive therapy prior to six months after surgery was misleading, so a new definition of groups should be

considered. Also, an additional important outcome should be modelled, as clinicians usually consider the risk for reoperation as a decisive factor for defining the best intervention for those patients.

The aim of this work is to develop Bayesian networks for the predictive prognosis of patients with Crohn's disease subject to early surgery or immunosuppression, namely targeting disabling disease and reoperation.

## II. MATERIAL AND METHODS

Multi-centric study data of Crohn's patients with surgery or immunosuppression in the first six months after diagnosis with more than 18 years old and at least 3 years of follow were included. A total of 489 patients were included (out of 668 patients collected). Hundred and seventy-nine patients were excluded because of missing values.

## A. Studied variables and outcomes

This study was a retrospective study and the collected variables included: characterization of patients (gender), disease (data of diagnosis and intervention (surgery and/or immunosuppressors, location with or not upper gastrointestinal tract, behavior and perianal disease), and follow up data (namely number of surgery and hospitalizations, treatments and adverse events). Patients were grouped by the index episode: immunosuppressors intake, and surgery (stratified considering the use or not of immunosuppressors 6 months after surgery).

The two main outcomes were disabling (defined by the presence of at least one of the following criteria: more than one surgery, excluding the first; more than two hospitalizations, excluding the first; two steroids course requirements per year, steroids dependency, steroids refractory; need to switch immunosuppressors or Anti-TNF therapy; adverse events) and reoperation (defined by the deed of second surgery).

## B. Model building and evaluation

Following the preliminary study presented previously [15], Tree Augmented Naïve Bayes (TAN) models were derived using all studied variables to predict disabling and reoperation. To assess the general structure and accuracy of learned models, stratified 10 -fold cross-validation was repeated 10 times, estimating accuracy and the area under the ROC curve.

WEKA software [12] was used to learn the Bayesian network structure. gRain [13] and pROC [14] R packages were also used to estimate de parameters of the networks and ROC curves, respectively.

## III. RESULTS

The main characteristics of patients are shown in Tab. I. Forty-eight percent of patients took immunosuppressors in the first 6 months after diagnosis and $36 \%$ had surgery with immunosuppressors 6 months after surgery. Forty-six percent were male and $21 \%$ had more than 40 years old at diagnosis.

Concerning location $47 \%$ had ileal disease and $32 \%$ had penetrating disease. We observed that $64 \%$ of patients had disabling during the course of the disease and $18 \%$ needed a second surgery.

TABLE I. MAIN CHARACTERISTICS OF PATIENTS WITH CROHN'S DISEASE INCLUDED IN THE STUDY ( $N=489$ ).


## A. Bayesian network model qualitative analysis

The qualitative models were show in Fig 1 and 2. Patient group was associated with disease behavior, upper gastrointestinal tract location (L4) and age at diagnosis, while disease extent was associated to perianal disease.

For disabling, association between perianal disease and gender and location was also found. Association between gender and L4 was also found for reoperation.

## B. Bayesian network model validation

Fig. 3 presents the in sample, leave-one-out and 10 times 10 -fold cross validation ROC curves for disabling and reoperation models, respectively. Resulting validation AUC were between $72 \%$ and $73 \%$. (for disabling) and between $79 \%$ and $80 \%$ (for reoperation).

## IV. DISCUSSION

The main contribution of this work was the development of prognostic models for disabling disease and reoperation. This models were developed after a preliminary study [15] done for the adequacy of these techniques into this problem, where comparison with other methods, namely logistic regression, has been assessed. Other clinical problems were also already addressed in the past with good performance, easy interpretation and friendly representations [7], [8], [11].

From models presented in Fig. 1 and 2 it was possible to infer some known clinical associations. In both outcomes, patient group was associated with disease behavior (whether it is penetrating or presenting stenosis or neither), upper gastrointestinal tract location (L4) and age at diagnosis, while disease extent was associated to perianal disease. These global dependencies show a common thread for knowledge representation in Crohn's disease management, specifically tune for each outcome considering the added associations between perianal disease and gender and location (found for disabling) and the association between gender and L4 (found for reoperation).

This knowledge representation allows an easy visualization of the model, supporting the experts' decision beyond the use of risk factors and discriminative cut points, into a support on the interdependences of studied variables and their induced causality.

From the quantitative analysis, and following the discussion from previous preliminary study - which showed that no significant decrease in predictive accuracy rises (beyond the naïve Bayes approach) with the enhancement of graphical analysis of variables' dependences - the Tree Augmented Naïve Bayes proved to be an accurate prognostic model, usable in clinical settings, even though it might (as expected) slightly over fit the training cohort (i.e. higher insample AUC), losing some generalization ability (i.e. lower quality on cross-validation). Further analysis shall confirm such suspicions using independent cohorts.

## V. CONCLUSIONS

The cross-validated evaluation of the Bayesian network classifiers derived in this study resulted in high accuracy and discriminative power for both disabling (above 70\%) and reoperation (above $80 \%$ ) outcomes in Crohn's disease patients subject to early surgery or immunosuppression. The generated models presented interesting insights on factor interaction and predictive ability for the prognosis, supporting their use in future clinical decision support systems.

Current path of research includes the definition of clinically usable decision support tools, based on the hereby derived Bayesian network classifiers and temporal Bayesian networks for the modeling of temporal interdependences useful for mid- and long-term prognosis of Crohn's disease course, taking into account the specific modeling of immunosuppressors intake.

## ACKNOWLEDGMENT

The authors thank the investigators of all hospitals who included data for this study, to GEDII - Grupo de Estudo da Doença Intestinal Inflamatória - for all the support, and project NanoStima ${ }^{\text {® }}$ NORTE-01-0145-FEDER-000016 ${ }^{\circ}$ which is financed by the North Portugal Regional Operational Programme (NORTE 2020), under the PORTUGAL 2020 Partnership Agreement, and through the European Regional Development Fund (ERDF).
