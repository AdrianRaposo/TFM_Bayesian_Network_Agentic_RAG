# Predicting outcomes of gastric endoscopic submucosal dissection using a Bayesian approach: a step for individualized risk assessment 

## ○(1)○○

Authors
Diogo Libânio ${ }^{1,3}$, Mário Dinis-Ribeiro ${ }^{1,3}$, Pedro Pimentel-Nunes ${ }^{1,3}$, Cláudia Camila Dias ${ }^{2,3}$, Pedro Pereira Rodrigues ${ }^{2,3}$

## Institutions

1 Gastroenterology Department, Instituto Português de Oncologia do Porto, Porto, Portugal
2 CINTESIS - Center for Health Technology and Services Research, Faculty of Medicine of the University of Porto, Porto, Portugal
3 MEDCIDES - Community Medicine, Information and Health Decision Sciences, Faculty of Medicine of the University of Porto, Porto, Portugal
submitted 18.7.2016
accepted after revision 2.3.2017

## Bibliography

DOI https://doi.org/10.1055/s-0043-106576 |
Endoscopy International Open 2017; 05: E563-E572
(c) Georg Thieme Verlag KG Stuttgart $\cdot$ New York

ISSN 2364-3722

## Corresponding author

Diogo Libânio, MD, Gastroenterology Department, Portuguese Oncology Institute of Porto, 4200-072 Porto, Portugal
Fax: +351-225084001
diogolibaniomonteiro@gmail.com

## ABSTRACT

Background and study aims Efficacy and adverse events probabilities influence decisions regarding the best options to manage patients with gastric superficial lesions. We
aimed at developing a Bayesian model to individualize the prediction of outcomes after gastric endoscopic submucosal dissection (ESD).
Patients and methods Data from 245 gastric ESD were collected, including patient and lesion factors. The two endpoints were curative resection and post-procedural bleeding (PPB). Logistic regression and Bayesian networks were built for each outcome; their predictive value was evaluated in-sample and validated through leave-one-out and cross-validation. Clinical decision support was enhanced by the definition of risk matrices, direct use of Bayesian inference software and by a developed online platform. Results ESD was curative in $85.3 \%$ and PPB occurred in $7.7 \%$ of patients. In univariate analysis, male sex, ASA status, carcinoma histology, polypoid or depressed morphology, and lesion size $\geq 20 \mathrm{~mm}$ were associated with non-curative resection, while ASA status, antithrombotics and lesion size $\geq 20 \mathrm{~mm}$ were associated with PPB. Naïve Bayesian models presented AUROCs of $\sim 80 \%$ in the derivation cohort and $\geq 74 \%$ in cross-validation for both outcomes. Risk matrices were computed, showing that lesions with cancer at biopsies, $\geq 20 \mathrm{~mm}$, proximal or in the middle third, and polypoid are more prone to non-curative resection. PPB risk was $<5 \%$ in lesions $<20 \mathrm{~mm}$ in the absence of antithrombotics.
Conclusions The derived Bayesian model presented good discriminative power in the prediction of ESD outcomes and can be used to predict individualized probabilities, improving patient information and supporting clinical and management decisions.

## Introduction

Gastric superficial neoplasms can be treated by endoscopic or surgical resection and recently European guidelines recommended endoscopic treatment as a first-line treatment [1]. Increasing expertise with endoscopic resection techniques, namely with endoscopic submucosal dissection (ESD), make possible the resection of lesions of increasingly greater sizes and in every localization. Thus, it is expected that the incidence
of non-curative resections and adverse events (AEs) also increase as greater and more advanced lesions are submitted to gastric ESD.

Gastric ESD can resect en bloc $92 \%$ of gastric superficial neoplasms [2-4] although it is considered curative in only $80 \%$ to $82 \%[4,5]$. Adverse events like procedure-related bleeding and perforation occur in $4 \%$ to $9 \%$ and $4 %$ to $5 \%$, respectively [2-4].

Patient- and lesion-specific factors can influence the probability of achieving a curative resection and of AEs. Larger le-

sion size, longer procedure time, endoscopist inexperience, ulcerative findings and localization in the upper stomach have been associated with treatment failure [6, 7]. Several risk factors were also identified as risk factors for post-procedural bleeding (namely lesion size, localization and antithrombotic therapy) although the results are controversial in literature.

Generally, these general data from the literature and previous endoscopist experience are used to inform patients about the probabilities of success and the risk of adverse events associated with endoscopic treatment and this information is also used in the decision process regarding treatment allocation. However, the knowledge of risk factors alone is not readily and completely usable by patients and clinicians in the decision process since it is difficult to predict the addictive effect of risk factors in the outcome, in a given patient.

Bayesian networks are increasingly being used for clinical decision support because Bayesian statistical methods take into account prior knowledge when analyzing data and can aid in capturing and reasoning with uncertainty in medicine and healthcare [8]. On a general basis, Bayesian networks represent a joint distribution of 1 set of variables, specifying the assumption of independence between them, yielding a qualitative interpretation of associations and a formal (probability-based) representation of uncertainty, providing readily human-interpretable evidence (e.g. a priori risk, a posteriori risk, relative risk).

We postulated that a priori patient- and lesion-specific factors could be used to predict individual post intervention probability of curative resection and post-procedural bleeding (PPB). Thus, the aim of this study was to develop a Bayesian model that can be used in clinical practice to predict outcomes after ESD and aid in the decision-making process.

## Patients and methods

## Studied variables and outcomes

Data from consecutive gastric ESDs performed in our institution from October 2005 until June 2015 were retrospectively collected from a prospectively maintained database. Collected data included patient (age, sex, ASA status, antithrombotic medication) and lesion factors (lesion type, tumor size, localization, morphology and biopsies histology) available at the pre-resection stage. The 2 main endpoints were curative resection and post-procedural bleeding. Lesions were submitted to ESD if they met standard or expanded indications for endoscopic resection [9]. We defined curative resection as a resection meeting the standard or expanded criteria of the Japanese Gastric Cancer Association guidelines [9]. Post-procedural bleeding was defined as the occurrence of melena or hematochezia, unstable vital signs or a hemoglobin drop $>2.0 \mathrm{~g} / \mathrm{dL}$ after ESD. Regarding morphology, lesions were classified according to the Paris classification of gastrointestinal superficial neoplasms [10]. Lesions were also categorized as primary, recurrent, metachronous or synchronous. For the analysis and model construction, morphology was recoded into polypoid (0-Isp, 0-Isp, 0-Ip), depressed (0-IIa+IIc, 0-IIc+IIa, 0-IIc and 0 III) and non-polypoid non-depressed (all remaining; e.g. 0-IIa,

0-IIb, 0-IIa+IIb). Tumor size was dichotomized using the 20mm threshold. ASA status (American Society of Anaesthesiologists' physical status classification system) was recoded into three groups: I, II and III/IV. Antithrombotic use was defined as the usage of either antiplatelets or anticoagulants in the periprocedural period. Low-dose aspirin was withheld for 7 days unless the thrombotic risk was high; thienopyridines were withheld for 5 days before and 2 to 3 days after; oral vitamin K antagonists were replaced for low molecular weight heparin according to guidelines in the 5 days and oral anticoagulants were restarted in the day after the procedure. Patients that were antithrombotic users but withheld for a longer period were not included in the antithrombotic use group.

## Model building and evaluation

Crude associations between all pre-treatment factors and both endpoints were evaluated using chi-square tests and independent samples t-test, and p-values $<0.05$ were considered significant.

Naïve Bayesian networks and logistic regression were built from the derivation cohort, with model parameters being validated by comparing the Areas Under Receiver Operating Characteristic (AUROCs) in the derivation cohort (optimistic), using leave-one-out validation (less optimistic), and applying 30 times 2-fold cross-validation (for variability assessment with independent training and testing).

Variables were included in the Bayesian networks, logistic regression models and risk matrices if they were statistically significant from univariate analyses (chi-square tests described above) and recursive partitioning, fine-tuned by expert's interpretation of useful variables at decision time. Each cell of the matrix presents the marginal posterior outcome probability for that subgroup of patients. Additionally, a $95 \%$ credible interval (CI; a highest posterior density interval around the marginal) is presented, computed from a Monte Carlo simulation of one million samples from the derived conditional probability model (i.e. the Bayesian network) [11].

All analyses were done using R statistical software (version 3.2.2) [12]. Logistic regression and chi-square testing was applied with R package stats [12], crude odds ratio inference was done with R package epitools [13], Bayesian network models were built using R package bnlearn [14] while network parameters were estimated with R package gRain [15], with the exact inference following the Lauritzen-Spiegelhalter algorithm [16], and ROC curves were computed with R package pROC [17].

Clinical decision support was then enabled by the interpretation of the risk matrices, direct use of Bayesian inference software [18] and through the use of an online platform where the endoscopist can select the appropriate pre-treatment factor and the calculated probability of curative resection and PPB is shown ( $\boldsymbol{\sim}$ Fig. 1).

Written informed consent was obtained from all patients. This study was conducted according with the ethical principles of the Declaration of Helsinki.

![img-0.jpeg](img-0.jpeg)

- Fig. 1 Example of an online platform that can readily usable in clinical practice (http://servicesforms.gim.med.up.pt/form_test/esdbayes. html). This example shows the posterior probability of curative resection (97\%) in a ASA II patient, with a non-polypoid non-depressed < 20 mm lesion located in the lower third of the stomach, with high-grade dysplasia on pre-resection biopsies, as well as the posterior probability of PPB ( $2 \%$ without antithrombotics). The predicted probability should be interpreted along with those predicted from risk matrixes, taking into account credibility intervals.


## Results

In our sample of 245 gastric ESDs, there were $14.7 \%$ non-curative resections ( $n=36$ ), and post-procedural bleeding (PPB) occurred in $7.7 \%(n=19)$. The resection was en-bloc in $95.1 \%$ and complete (R0) in $94.3 \%$. Age was not statistically significantly different between groups, for either outcome. Patient- and le-sion-specific factors and their association with non-curative resection and post-procedural bleeding in univariate analyses are summarized in Table 1 and Table 2, respectively. Male sex,

ASA III/IV, carcinoma histology on pre-resection biopsies, polypoid or depressed morphology and lesion size $\geq 20 \mathrm{~mm}$ were associated with non-curative resection. The majority of noncurative resections were due to deep submucosal invasion and/or lymphovascular invasion ( Table 1). ASA status III/IV, antithrombotic therapy and lesion size $\geq 20 \mathrm{~mm}$ were significantly associated with PPB. Procedure duration was similar in patients with and without PPB ( 116.6 vs 127.7 minutes, $P=$ 0.796). Treatment outcomes were stable across time ( $\downarrow$ Supplementary Table 1).

Table 1 Univariate analysis of risk factors for non-curative resection.

Male
Female | $\begin{aligned} & 106 / 132(80.3) \ & 103 / 113(91.1) \end{aligned}$ | (ref)
$0.40[0.18,0.85]$ | 0.03  |
|  ASA
I
II
III/IV | $\begin{aligned} & 59 / 62(95.2) \ & 112 / 132(84.8) \ & 38 / 51(74.5) \end{aligned}$ | (ref)
$3.35[1.08,15.31]$
$6.39[1.88,30.69]$ | 0.01  |
|  Antithrombotics
No
Yes | $\begin{aligned} & 170 / 196(86.7) \ & 39 / 49(79.6) \end{aligned}$ | (ref)
$1.68[0.72,3.72]$ | 0.30  |
|  Lesion type
Primary
Recurrent
Metachronous
Synchronous | $\begin{aligned} & 168 / 202(83.2) \ & 9 / 10(90.0) \ & 18 / 19(94.7) \ & 14 / 14(100) \end{aligned}$ | (ref)
$0.48[0.13,4.49]$
$0.25[0.07,2.18]$
- | 0.19  |
|  Location
Upper
Middle
Lower | $\begin{aligned} & 44 / 51(86.3) \ & 55 / 70(78.6) \ & 110 / 124(88.7) \end{aligned}$ | $\begin{aligned} & 1.26[0.45,3.28] \ & 2.13[0.95,4.81] \ & \text { (ref) } \end{aligned}$ | 0.16  |
|  Lesion size
$<20 \mathrm{~mm}$
$>=20 \mathrm{~mm}$ | $\begin{aligned} & 130 / 143(90.9) \ & 79 / 102(77.5) \end{aligned}$ | (ref)
$2.91(1.40 ; 6.07)$ | $<0.01$  |
|  Morphology
Polypoid
Non-polypoid non-depressed
Depressed | $\begin{aligned} & 12 / 18(66.7) \ & 94 / 103(91.3) \ & 103 / 124(83.1) \end{aligned}$ | $\begin{aligned} & 5.22[1.58 ; 17.25] \ & \text { (ref) } \ & 2.13[0.93 ; 4.88] \end{aligned}$ | 0.01  |
|  Histology
LGD
HGD
IMC | $\begin{aligned} & 77 / 82(93.9) \ & 97 / 110(88.2) \ & 35 / 53(66.0) \end{aligned}$ | (ref)
$2.02[0.72,6.68]$
$7.64[2.77,25.21]$ | $<0.01$  |
Lymphovascular invasion
HMx/HM1
Poor differentiation $\geq 20 \mathrm{~mm}$
VMx/VM1 | $\begin{aligned} & 20 \ & 13 \ & 6 \ & 4 \ & 2 \end{aligned}$ |  |   |

ASA, American Society of Anaesthesiologists Physical Status System; LGD, low-grade dysplasia; HGD, high-grade dysplasia; IMC, intramucosal carcinoma; PPB, postprocedural bleeding; OR, odds ratio; ${ }^{1}$ chi-square test. at a significance level of 0.05 ${ }^{2}$ more than one unfavorable prognostic factor was present in some cases

## Bayesian network models and models evaluation

The constructed model for curative resection is shown in - Fig. 2, where dependencies between variables are shown. In the derivation cohort, the AUROCs of the Bayesian models were $78 \%$ and $83 \%$ for the prediction of curative resection and PPB, respectively (versus $79 \%$ and $84 \%$ with logistic regression models). In leave-one-out and cross-validation, the Bayesian model achieved AUROCs $\geq 74 \%$ for the prediction of both outcomes ( Fig.3). There were no statistically significant differences in the AUROCs of the Bayesian model and the logistic regression model, despite they were slightly higher with the Bayesian model. We did not compute confidence interval for AUROC es- timated with leave-one-out and cross-validation since these approaches are built from multiple models built from different sub-samples and therefore the frequentist confidence interval approach is not valid for this assessment.

## Risk matrices

Risk matrices were constructed for both outcomes based on Naïve Bayesian model. Posterior probabilities of achieving a curative resection ( Fig.4) ranged from $20 \%$ (for $\geq 20 \mathrm{~mm}$ polypoid lesions located in the middle third of the stomach with intramucosal carcinoma in pre-resection biopsies) to $98 \%$ (for non-polypoid non-depressed lesions located in the lower

Table 2 Univariate analysis of risk factors for post-procedural bleeding.


ASA, American Society of Anaesthesiologists Physical Status System; LGD, low-grade dysplasia; HGD, high-grade dysplasia; IMC, intramucosal carcinoma; OR, odds ratio; $\mathrm{HMx} / \mathrm{HM} 1$, indeterminate/positive horizontal margins; $\mathrm{VMx} / \mathrm{VM} 1$, indeterminate/positive vertical margins ${ }^{1}$ at a significance level of 0.05 third with low-grade dysplasia on pre-resection biopsies). The probability of non-curative resection was expected to be lower than $50 \%$ in polypoid lesions $\geq 20 \mathrm{~mm}$ with intramucosal carcinoma (IMC) on pre-resection biopsies, polypoid IMC lesions $<20 \mathrm{~mm}$ located in the middle third, and depressed lesions $\geq 20 \mathrm{~mm}$ with IMC located in the middle or lower third. The proportion of curative resections in our sample approached the probability predicted by the model.

Two risk matrices for PPB were also defined separately for patients under antithrombotic therapy and patients without antithrombotic use ( Fig. 5). The predicted probability of PPB in polypoid lesions was $0 \%$ ( $95 \%$ credibility interval 0,0 ). In nonpolypoid non-depressed and in depressed lesions, the posterior probability of PPB ranged from $1 \%$ to $13 \%$ in the absence of antithrombotic therapy and from $8 \%$ to $51 \%$ with antithrombotics ( Fig. 5). In general, size $\geq 20 \mathrm{~mm}$, localization in the upper and middle third and non-polypoid non-depressed morphology were associated with a higher bleeding risk. Lesions $<20 \mathrm{~mm}$ in the absence of antithrombotic therapy yielded posterior probabilities of post-procedural bleeding of less than $5 \%$.

## Clinical decision supporting tools

Research-oriented Bayesian inference software can be used in clinical practice to predict individualized probabilities of curability and post-procedural bleeding ( $\boldsymbol{\sim}$ Fig. 2). Additionally, an online platform ( $\boldsymbol{\sim}$ Fig. 1) was also developed to ease clinical decision support (http://servicosforms.gim.med.up.pt/form_test/esdbayes.html).

## Discussion

Treatment allocation when two or more alternatives are available is one of the most common dilemmas in clinical practice, making the decision process one of the most difficult tasks for both clinicians and patients, since uncertainty has to be dealt with at the time in which the decision is taken.

Regarding the treatment of gastric superficial neoplasms, 2 alternatives are possible: endoscopic and surgical treatment. Advances in endoscopic resection make possible the resection of superficial neoplasms of increasing size and in difficult loca-

![img-1.jpeg](img-1.jpeg)

- Fig. 2 Example of Bayesian inference software that can be used in clinical decision support and information. This example shows the posterior probability of curative resection ( $83 \%$ ) in a patient with a non-polypoid non-depressed lesion greater than 20 mm located in the middle third of the stomach, with high-grade dysplasia on pre-resection biopsies.
![img-2.jpeg](img-2.jpeg)
- Fig. 3 AUROC curves of the Bayesian and logistic regression models. AUROC curves (derivation cohort; leave-one-out and cross-validation) of Naïve Bayesian models and logistic regression for prediction of curative resection and post-procedural bleeding (PPB).

(ls, lp, Isp) | Middle | $85[74,95]$ | $74[58,90]$ | $42[27,51]$ | $66[50,87]$ | $49[33,76]$ | $20[11,46]$  |
(IIc, lla+c, llc+a, III) | Middle | $93[88,98]$ | $88[78,96]$ | $64[47,86]$ | $83[71,94]$ | $70[54,89]$ | $38[24,67]$  |
non-depressed
(lla, llb, lla+b) | Middle | $97[94,99]$ | $94[88,98]$ | $79[66,93]$ | $91[84,97]$ | $83[72,94]$ | $86[67,100]$  |

Each cell presents the marginal posterior outcome probability and $95 \%$ credibility intervals. LGD, low-grade dysplasia; HGD, high-grade dysplasia; IMC, intramucosal carcinoma. Green: $90 \%-100 \%$; Blue: $80 \%-89.9 \%$; Orange: $70 \%-79.9 \%$; Red: $50-69.9 \%$; Gray: $<50 \%$

- Fig. 4 Risk (posterior probabilities) matrix for curative resection based on morphology, localization, size and pre-resection histology, using a Bayesian model.

(IIc, lla+c, llc+a, III) | Middle | $3[0,5]$ | $2[0,4]$ | $3[0,6]$ | $9[0,16]$ | $7[0,12]$ | $10[0,18]$  |
(IIc, lla+c, llc+a, III) | Middle | $17[0,28]$ | $13[0,22]$ | $19[0,30]$ | $41[0,56]$ | $33[0,49]$ | $43[0,59]$  |

Each cell presents the marginal posterior outcome probability and $95 \%$ credibility intervals (upper part, in bold) and the proportion of cases in our series expressing the outcome (bottom part). LGD, low-grade dysplasia; HGD, high-grade dysplasia; IMC, intramucosal carcinoma. Green: $<5 \%$; Blue: $5-10 \%$; Orange: $10-20 \%$; Red: $20-30 \%$; Gray: $\geq 30 \%$

- Fig. 5 Risk (posterior probabilities) matrix for post procedural bleeding based on morphology, localization, size, pre-resection histology and antithrombotic therapy, using a Bayesian model. tions and this may increase the absolute number of non-curative resections and adverse events. Treatment failure can therefore be problematic for gastroenterologists, patients and healthcare systems: gastroenterologists and patients have the expectation of cure and being cured by endoscopic treatment; and the resources allocation of a time-consuming technique to a treatment that fails in approximately $20 \%$ of the cases.

Endoscopic evaluation of lesion features (margins, extensive ulceration, surrounding folds, irregular surface pattern) by an experienced endoscopist is considered the best method to pre-

dict submucosal invasion and is more accurate than ultrasonography [19, 20]. However, that evaluation is operator-dependent and data about its reproducibility is lacking.

Thus, clinicians must weigh the benefits and risks of the 2 treatments in order to choose the most appropriate for each patient, to optimize expectations and resources. However, it is difficult to integrate literature data in everyday practice, to individual patients. Bayesian models offer a versatile approach to capturing and reasoning with uncertainty in medicine and can aid in the decision process [8].

In this study we developed a Bayesian model using exclusively characteristics available at the pre-resection stage in order to predict the probabilities of success and of AEs before the procedure, when patients have to be informed and the decision taken. The derived model presented good discriminative power (AUROC ~ 80% in the derivation cohort and ≥ 74% in cross-validation). Although Bayesian models were not statistically significantly different from logistic regression, the information provided by Bayesian models is more usable in clinical practice and can aid clinicians in decision-making and patient information.

The derived risk matrices are a way to promptly assess posterior probabilities of curative resection and PPB based on 4 readily available variables. Generally, we see that the likelihood of a curative resection decreases with size ≥ 20 mm, more advanced histology in pre-resection biopsies, localization in the middle third and polypoid morphology. These findings are in line with Hirasawa et al. that found that lesion size, ulceration and localization in the upper third are associated with treatment failure [7]. In this study, a risk chart was also constructed based on the odds ratio of multivariate analysis, although the goodness of fit of the model was not reported. Our model also includes lesion morphology (that also affects the likelihood of submucosal invasion [10]) and pre-resection histology. Our results show that pre-resection biopsies can influence the probability of a curative resection and that this information can be used in risk prediction.

For PPB, to our knowledge this is the first risk matrix created to predict this adverse event. Antithrombotic therapy is the variable that greatly increases the likelihood of PPB, although size ≥ 20 mm, localization in the middle third and depressed and non-depressed non-polypoid morphology also contributes to a higher bleeding risk. However, although localization was found to influence PPB in our series, a recent meta-analysis found similar bleeding rates for lesions located in the upper, middle or lower third of the stomach [21]. This risk matrix can contribute to better patient information about individual bleeding risk and can also guide management after ESD, namely the period of in-hospital surveillance.

The Bayesian networks can also be interactively used in daily clinical practice either through the use of the research-oriented Bayesian inference software (Fig. 2) or through the use of a purposely developed online calculator (Fig. 1). Bayesian inference software allows users to select the corresponding option in each pre-resection variable, with the posterior probability of curative resection and PPB being computed as a percentage. Both the Bayesian inference software and the online calculator are intuitive and easy to use since clinicians only have to check the corresponding patient data and the individual probability of the outcome is shown.

To our knowledge, this study was the first that used Bayesian methods in the prediction of outcomes of endoscopic treatment. The risk factors found for non-curative resection and PPB are in line with data from other studies and this was translated in two risk matrices and in the development of one tool that can be useful in everyday clinical practice. Moreover, this study may encourage the application of Bayesian models in other areas of gastroenterology where they can be of great value in decision support.

This study has some limitations. First, although this is the largest Western series of gastric ESD, the endpoints (non-curative resection and post-procedural bleeding) occur infrequently and so the credibility intervals of risk matrices are wide in some cells and should be carefully interpreted in those cases. Also, the predicted probabilities of the online calculator should take into account this aspect. Generalization of our findings and its routine use before endoscopic resection is dependent on further validation and/or derivation of a more robust model in the future. However, we assessed overfitting by presenting 2 validation approaches – leave-one-out and 2-fold cross-validation – which suffice to expose the amount of overfit that we might expected from the models. As we can see in the ROC figures, the validation curves are less optimal than the derived ones but we present validated estimates of AUC above 70% for both outcomes, which supports our opinion that the models are generalizable to independent cohorts.

Second, our model was designed using only variables available at the pre-resection stage. Procedural variables like operator experience may also affect curability although the majority of non-curative resections are due to lesion-related factors such as submucosal invasion and lymphovascular invasion. Indeed, en-bloc and complete resections occur in almost 95% of the cases and incomplete resection is rarely the reason for treatment failure, reinforcing the need of prediction models to improve patient selection based on patients' and lesions' characteristics. Additionally, other lesion features (such as colour and hardness) may also affect the probability of curative resection but are less objective than size, morphology and localization and were not included in our model. Procedural duration and technical factors such as coagulation of visible vessels may also influence PPB and should be taken into account although in our series procedural time did not affect bleeding rates.

## Conclusion

In conclusion, the derived models presented good discriminative power in the prediction of curative resection and PPB. Bayesian models, risk matrices and computerized tools can be used to predict individualized probabilities, which can improve the information transmitted to patient regarding posterior probabilities and can aid in the decision process regarding allocation for endoscopic or surgical treatment. Additionally, posterior probabilities of adverse events can guide management

after gastric ESD, namely regarding the timing of discharge from hospital.

## Acknowledgements

This work was partially developed under the scope of project NanoStima (NORTE-01-0145-FEDER-000016) which is financed by the North Portugal Regional Operational Programme (NORTE 2020), under the PORTUGAL 2020 Partnership Agreement, and through the European Regional Development Fund (ERDF). The authors also acknowledge the help of Raphael Oliveira in the development of the online inference tool.

## Competing interests

None
