# Dynamic Bayesian network for predicting physiological changes, organ dysfunctions and mortality risk in critical trauma patients 

Qi Chen ${ }^{1 \dagger}$, Bihan Tang ${ }^{3 \dagger}$, Jiaqi Song ${ }^{1 \dagger}$, Ying Jiang ${ }^{6 \dagger}$, Xinxin Zhao ${ }^{2}$, Yiming Ruan ${ }^{1}$, Fangjie Zhao ${ }^{3}$, Guosheng Wu ${ }^{5 *}$, Tao Chen ${ }^{4 *}$ and Jia $\mathrm{He}^{1,2 *}$


#### Abstract

Background: Critical trauma patients are particularly prone to increased mortality risk; hence, an accurate prediction of their conditions enables early identification of patients' mortality status. Thus, we aimed to develop and validate a real-time prediction model for physiological changes, organ dysfunctions and mortality risk in critical trauma patients.


Methods: We used Dynamic Bayesian Networks (DBNs) to model complicated relationships of physiological variables across time slices, accessing data of trauma patients from the Medical Information Mart for Intensive Care database (MIMIC-III) ( $n=2915$ ) and validated with patients' data from ICU admissions at the Changhai Hospital (ICU-CH) ( $n=1909$ ). The DBN model's evaluation included the predictive ability of physiological changes, organ dysfunctions and mortality risk.
Results: Our DBN model included two static variables (age and sex) and 18 dynamic physiological variables. The differences in ratios between the real values and the 24 - and 48 -h predicted values of most physiological variables were within $5 \%$ in the two datasets. The accuracy of our DBN model for predicting renal, hepatic, cardiovascular and hematologic dysfunctions was more than 0.8. The calculated area under the curve (AUC) from receiver operating characteristic curves and 95\% confidence interval for predicting the 24- and 48-h mortality risk were 0.977 (0.967-0.988) and 0.958 (0.945-0.971) in the MIMIC-III and 0.967 (0.947-0.987) and 0.946 (0.925-0.967) in ICU-CH.
Conclusions: A DBN is a promising method for predicting medical temporal data such as trauma patients' mortality risk, demonstrated by high AUC scores and validation by a real-life ICU scenario; thus, our DBN prediction model can be used as a real-time tool to predict physiological changes, organ dysfunctions and mortality risk during ICU admissions.
Keywords: Dynamic Bayesian network, Critical trauma patients, Prediction model

[^0]
## Background

Trauma is a universal health challenge that leads to numerous deaths and disabilities at any age [1]. The common causes of trauma include road injuries, falls, selfharm, interpersonal violence, and so on. In 2017, there were more than 4.4 million trauma deaths and 520 million trauma cases globally, which resulted in 3267 DALYs per 100,000 [2]. Critical trauma patients admitted to the intensive care unit (ICU) are particularly vulnerable and

## E BMC

[^1]
[^0]:    *Correspondence: wuguosheng_nmu@163.com; chentao301@126.com; hejia63@yeah.net
    ${ }^{\dagger}$ Qi Chen, Bihan Tang, Jiaqi Song and Ying Jiang have contributed equally and are co-first authors of this article
    ${ }^{\dagger}$ Department of Health Statistics, Naval Medical University, No. 800 Xiangyin Road, Shanghai 200433, China
    * Department of Cardiology, PLA General Hospital, No. 28 Fuxing Road, Beijing 100853, China
    ${ }^{\text {S }}$ Department of Burn Surgery, Changhai Hospital, Naval Medical University, No. 800 Xiangyin Road, Shanghai 200433, China Full list of author information is available at the end of the article

[^1]:    (c) The Author(s) 2022. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.

prone to increased mortality risk. Thus, accurate prediction of the complications and death probability of trauma patients in ICU could enable early identification and intervention for patients at high mortality risks [3].

Although some prognostic scoring systems such as the Simplified Acute Physiology Score (SAPS) [4] and Acute Physiology and Chronic Health Evaluation (APACHE) [5] exist and are used for risk stratification of ICU patients, and some trauma score instruments such as the Injury Severity Scale (ISS) [6] and Trauma and Injury Severity Score (TRISS) [7] are used for risk stratification of trauma patients, the predictive ability of these scoring systems for mortality trauma patients was still conflicting [8--10]. Besides, two other reasons might hinder the clinical application of these scoring systems. First, these scoring systems' items are too complex, and some of them need to be measured manually. Second, these scoring systems are based on the baseline information (usually admission) to predict an outcome. However, in clinical practice, patient status changes over time, and doctors adjust their prognostic prediction based on the latest status. Hence, a real-time prediction tool based on the latest data outperforms the tools based on baseline data in timeliness and accuracy and actualize precision-medicine-based decision making [11].

Advanced medical equipment can monitor the physiological status of ICU trauma patients in real-time and accumulate massive patient-level temporal data in electronic health record (EHR) systems [12]. In contrast, advanced machine learning techniques are suited to deal with this voluminous data and complex relationships among physiological variables [13]. Bayesian Networks (BNs) have been applied to solve the medical tasks due to their capability to model complex systems in which relationships between the variables were previously completely unknown [14]. Dynamic Bayesian Networks (DBNs) add to BNs the ability to process temporal relationships, and thereby, have become popular in offering an approach to detailed prognostic models that capture the relationships between variables at different time slices and predict the variables in the next time slice from the variables in the previous time slice [15, 16].

Therefore, we sought to develop and validate a real-time prediction model for physiological changes, organ dysfunctions and mortality risk in ICU trauma patients using DBNs based on the massive patient-level temporal data from two centers.

## Materials and methods

### Data collection

Our prediction model was developed in Medical Information Mart for Intensive Care database (MIMIC-III), an ICU database from the Beth Israel Deaconess Medical Center (Boston, MA) [17], and validated using patients at the Burn and Trauma ICU of the Changhai Hospital (ICU-CH) from January 2008 to December 2019, which is one of the major burn and trauma centers in East China [18]. Patients aged > 18 years who received trauma services in ICU were eligible for the study and included in our analysis. Trauma was defined as the injury caused by physical harm from an external source like traffic accident, fight, fall from height and so on. Our study was performed in accordance with the Declaration of Helsinki and the protocol was approved by the Ethics Committee of the Naval Medical University. The MIMIC-III is public de-identifed databases thus informed consent and approval of the Institutional Review Board was waived. Written informed consent was obtained from individual at ICU-CH.

Clinical data were obtained from the patients' electronic health records (EHR). Baseline patients' data at the time of ICU admission were extracted, including age, sex, ICU admission time, ICU discharge time, and in-hospital death time. The physiological items in SAPS II [19] and APACHE II [20] were used as temporal physiological variables in our study. They included temperature, respiratory rate, heart rate, systolic pressure, diastolic pressure, Glasgow coma scale, leukocyte count, platelet count, hematocrit, bilirubin, blood glucose, serum sodium, serum potassium, arterial pH value, serum creatinine, serum urea nitrogen levels, central venous pressure and PO_{2}/FIO_{2} Ratio.

### Data preparation

(1) Outliers' processing: We considered the influence of outliers in the model construction by setting a series of criteria based on clinical experience to filter out and delete the outliers in the database (Additional file 1: Table S1). (2) The length of time slice: The recording interval of vital signs data range from 15 min to 4 h, and the interval of laboratory tests was about 1 day. The length of the time slice in our DBNs was set to 4 h. If vital signs were measured multiple times in a one-time slice, the average value was used to avoid a fluctuation due to random errors (Fig. 1A). (3) Data collation: All temporal records were organized into longitudinal data by patient identification and time points; baseline data were replicated at each timepoint (Fig. 1B). (4) Normal transformation: Continuous variables should obey normal distribution in DBNs, so all variables were converted to logarithmic values. (5) Data imputation: Different variables were measured with different frequencies, which resulted in missing values of variables at some time points. The missing proportion of temporal physiological variables were shown in Additional file 1: Table S2. For these missing values, the common filling strategy was

![img-0.jpeg](img-0.jpeg)

C. Evaluation of prediction accuracy for physiological changes

![img-1.jpeg](img-1.jpeg)

D. Evaluation of prediction accuracy for organ dysfunctions

![img-2.jpeg](img-2.jpeg)

E. Evaluation of prediction accuracy for mortality risk

![img-3.jpeg](img-3.jpeg)

Fig. 1 The overview of data extraction, data collation and model evaluation

Table 1 Baseline characteristics of study population from MIMIC-III and ICU-CH


${ }^{a}$ Other included dislocation, sprains and strains of joints and adjacent muscles, open wound of trunk, open wound of limb, etc.
to impute with the last observation of that variable until the next measurement of the particular value was available or until the end of the time series, and we used this filling strategy in our study [21]. The remaining missing values were imputed with the expectation-maximization algorithm.

## Model development

The construction of a DBN consists of two steps: structure learning and parameter learning. In our study, structure learning of the network was data-driven with some logical constraints. We assumed that the state of physiological variables at time slice $t 1$ was only related to the state of the variables at previous time slice $t 0$. The DBN structure learning was performed using the PC algorithm, a prototypical constraint-based structure learning method. After building the network structure, we conducted parameter learning to estimate the conditional probabilities that quantify the arcs of the network.

Maximum likelihood parameter estimation was used to fit the parameters of DBN.

Our prediction model was built on the collated data derived from MIMIC-III using the DBN. The DBN was implemented using the R package bnlearn. In our study, a simple description of DBN and R codes are shown in the Additional file 1. A detailed description of DBN theory, structure, and parameter learning is provided in a book by Nagarajan et al. [14].

## Model evaluation

The evaluation of our prediction model included three parts: prediction ability of physiological changes, organ dysfunctions and mortality risk at the next 24 h and 48 h .

The DBN model evaluation was conducted in MIMICIII and ICU-CH, respectively. For patients in ICU stay of $>24 \mathrm{~h}$, we extracted true data in the final time slice (within 4 h before death or discharge) and the last 7th slice ( 24 h before death or discharge); then we computed the predicted data in a final time slice by DBN after six iteration imputations on data in the last 7th slice. For patients with ICU stay of $>48 \mathrm{~h}$, we extracted real data in the final time slice and the last 13th slice ( 48 h before death or discharge), and the predicted data in the final time slice were computed by a DBN after 12 iteration imputations on data in the last 13th slice. Then prediction ability of physiological changes, organ dysfunctions and mortality risk at the next 24 h and 48 h was tested in patients' ICU stay for $>24 \mathrm{~h}$ and $>48 \mathrm{~h}$, respectively.

For evaluating the prediction accuracy of physiological changes (Fig. 1C), we used the absolute difference and different ratios to measure the distinction between the true and predicted data, which reflected the prediction accuracy of physiological changes for our DBN. For the evaluation of organ dysfunctions risk prediction accuracy (Fig. 1D), the true state of organ dysfunctions was judged by the true physiological data, and the predicted state of organ dysfunctions was judged by the predicted physiological data. The criteria of organ dysfunctions were developed according to Multiple Organ Dysfunction Score (Additional file 1: Table S3). The prediction performance for organ dysfunctions was evaluated by sensitivity, specificity and accuracy. For the evaluation of mortality risk prediction accuracy (Fig. 1E), we used real data in the final time slice of MIMIC-III to build a mortality discrimination model by logistic regression with a restricted cubic spline function. Subsequently, this mortality discrimination model was used to calculate the predicted mortality risk based on the predicted data of the final time slice computed by the DBN. The prediction performance for mortality was evaluated by the areas under the curves (AUCs) of the receiver operating characteristic (ROC) and calibration curves. Moreover,

Table 2 Prediction accuracy of variables at 24th hour and 48th hour in development datasets (MIMIC-III)


[^0]we calculated mortality prediction performance using SAPS II and APACHE II based on the data at the last 7th or 13th slices to compare the prediction ability of mortality between our DBN model and SAPS II and APACHE II scores. The mortality discrimination model, ROC curves, and calibration curves were implemented using R package rms.

In practice, to display intuitively and facilitate the use of our DBN model, an interactive web-based calculator
was developed using the R "Shiny" package (https://www. shinyapps.io/).

## Results

In total, we included 2915 ICU admissions from MIMICIII and 1909 ICU admissions from ICU-CH in this study. The general characteristics of the study participants are shown in Table 1. Cause of injury and ISS from ICU-CH


[^0]:    ${ }^{a}$ Difference ratio $=($ True value - Predicted value $) \times 100 \% /$ True value

Table 3 Prediction accuracy of variables at 24th hour and 48th hour in testing dataset (ICU-CH)


are shown in Additional file 1: Table S4. The structure of our DBN model is shown in Additional file 1: Fig. S1, where the arrows represent the impact path from variables in $t 0$ to variables in $t 1$.

Table 2 shows the prediction accuracy of our DBN model for physiological changes at the 24th hour and 48th hour in MIMIC- III. The difference ratios between the real values and the 24-h predicted values of most physiological variables were within $5 \%$. The errors of
$48-\mathrm{h}$ predicted values were slightly larger than that of 24-h predicted values. In the ICU-CH, the different ratios between the real values and the $24-\mathrm{h}$ or $48-\mathrm{h}$ predicted values of all variables were within $15 \%$; indeed, most were within $5 \%$ (Table 3). Also, we assessed the prediction accuracy for physiological changes in patients whose outcome was death (Additional file 1: Tables S5, S6). Some physiological variables (like GCS) had large prediction errors in death patients.

Table 4 Prediction accuracy of organ dysfunctions risk at 24th hour and 48th hour


Sensitivity = (true positives)/(true positives + false negatives), specificity = (true negatives)/(true negatives + false positives), accuracy = (true positives + true negatives)/total

As Table 4 shown, our model had good predicting ability for predicting renal, hepatic, cardiovascular and hematologic dysfunctions with accuracy more than 0.8 in MIMIC- III and ICU-CH. For the 48-h neurological dysfunction in MIMIC- III and the respiratory dysfunction in ICU-CH, the prediction accuracy of our DBN model was less than 0.8 .

Figure 2 shows the prediction accuracy of our DBN model for mortality risk. In MIMIC-III, the AUC of the mortality discrimination model using the data predicted by DBN based on the 24th hour data before outcome was 0.977 ( $95 \% \mathrm{CI}, 0.967-0.988$ ). The AUCs of SAPSII and APACHE-II based on the 24th hour data before outcome were 0.954 ( $95 \% \mathrm{CI}, 0.942-0.966$ ) and 0.948 ( $95 \% \mathrm{CI}, 0.932-0.964$ ). In a similar scenario, the AUC of the model using data predicted by DBN was higher than that of other models, and appeared in the 48-h mortality prediction in MIMIC- III and 24-h and 48-h mortality prediction in ICU-CH. Calibration plots in Additional file 1: Fig. S2 showed that the predicted mortality from the model using data predicted by DBN closely approximated the actual outcomes.

We developed a web-based calculator based on our DBN model to predict physiological changes and mortality risk for new trauma patients available at the website https://jsong67.shinyapps.io/Prediction2/. This web-based calculator requires the input of the participant's baseline characteristics and physiological variables and then outputs the predicted results.

## Discussion

Our study built a DBN model for predicting physiological changes, organ dysfunctions and mortality risk in critical trauma patients and validated the model in an external dataset with good discrimination and calibration. The DBN model was based on the variables in SAPS-II and APACHE-II and is accessible online by a web application. Compared with other machine learning-based models, our model can be readily calculated with a web application that allows clinicians to use our model in practice and help to validate our model in their medical work.

In practice, a trauma patient's current physiological variables' values could be inputted in our DBN model to calculate and physiological changes, organ dysfunctions and the death risk in the future 24 and 48 h . As more physiological variables become available during ICU monitoring, our DBN model is able to update the predicted values dynamically. With the emergence of personalized medicine, our DBN model can not only predict the risk of death, but also predict physiological variables to predict the occurrence of organ dysfunctions. Then, our model can be used for clinical decision making, with a view of early interventions, thereby preventing a delay in the initiation of appropriate therapy that has been recognized as a risk factor for mortality among ICU patients [22, 23].

The relationship between ICU patients' physiological variables is highly complex (usually nonlinear and interactive), which is unlikely to be captured by common parametric methods (e.g., linear regression). Moreover, models designed to be intuitive for human experts'

![img-4.jpeg](img-4.jpeg)

# A. MIMIC- III

## 24th hour mortality



## 48th hour mortality



## B. ICU-CH

## 24th hour mortality



## 48th hour mortality



## Fig. 2 Comparison of prediction models by ROC analysis

Understanding may not be computationally efficient or accurate for probabilistic modeling [24]. Methods that consider the complex conditional inter-dependencies between variables would be more precise in probabilistic modeling. The DBN extends standard BNs with the concept of time and can handle arbitrary nonlinear and complicated time-dependent relationships, which can be used for a wide range of tasks, including prediction and decision making under uncertainty [25, 26]. Our study demonstrated that the DBN is a robust method, able to

predict physiological changes and improve the prediction accuracy of mortality compared with traditional tools like the SAPS-II and APACHE-II.

Compared with other studies that directly put outcome variables into the DBN [15, 16, 25, 26], our study did not use this approach for two reasons. First, there is about $10 \%$ of patients' death in our dataset (Table 1). If the mortality was included in the DBN model, it would lead to an imbalance in machine learning, causing overfitting and reducing the external accuracy [27]. Second, deaths are discrete data, while physiological variables are continuous data, and the combination of these data types yield mixed data. A simple way to learn DBN from mixed data is to convert all continuous variables to discrete ones [14]. However, there are many discretization methods; thus, it is difficult to determine the appropriate discretization mode; also, our study's purpose was to predict the specific value of physiological indicators. Therefore, death was not put into the DBN model, and the mortality risk was calculated based on the predicted physiological values.

There are four major limitations to our study. First, we included the variables in SAPS-II and APACHE-II, although more recent versions of SAPS and APACHE are available, partly because some variables in recent versions do not exist in our two databases, and partly because we wanted to keep our model as simple as possible. Second, some complications such as sepsis were not included in our model since the lack of the occurrence time of complications in our datasets. Third, although our DBN model performed well in external validation, our data were from two high-level hospitals with advanced medical conditions and rich medical experiences. The physiological changes are not only affected by trauma but also affected by medical conditions. So, our DBN model still needs extensive validation in various types of hospitals in the future. Finally, participants with the same input values had the same output values calculated using the DBN model, but each person is unique with individual characteristics. Therefore, although our DBN prediction model could support decision making, not all medical care decisions need to be made by a clinician.

## Conclusion

Our DBN model can be used as a real-time prediction tool to predict physiological changes, organ dysfunctions and mortality risk in ICU trauma patients and achieve better performance than conventional severity scores. Moreover, our study demonstrates that the DBN is a promising method for predicting of medical temporal data. In the future, we should validate our DBN model to verify its prediction accuracy and further improve the web calculator to increase the user convenience of the models by a physician.

Supplement tables show the definition of non-fault value, the missing proportion of variables in MIMICIII, the criteria of organ dysfunctions, cause of injury and Injury Severity Score from ICU-CH, and prediction accuracy of physiological variables at 24th hour and 48th hour in death population. Supplement figures show the structure of DBN model and calibration curves. Supplement texts show R codes of dynamic Bayesian network.

## Supplementary Information

The online version contains supplementary material available at https://doi. org/10.1186/s12911-022-01803-y.

Additional file 1: Table S1. The definition of non-fault value. Table S2. The missing proportion of temporal physiological variables in MIMIC-III. Table S3. The criteria of organ dysfunctions. Table S4. Cause of injury and Injury Severity Score from ICU-CH. Table S5. Prediction accuracy of variables at 24th hour and 48th hour in death population from development datasets (MIMICIII). Table S6. Prediction accuracy of variables at 24th hour and 48th hour in death population from testing dataset (ICU-CH). Figure S1. Prediction accuracy of variables at 24th hour and 48th hour in death population from testing dataset (ICU-CH). Figure S2. Calibration curves. Supplement texts. The description and R codes of dynamic Bayesian network.

Not applicable.

Q.C. G.S.W. T.C. and J.H. discussed and developed the study question for this report. Q.C. conducted the data extraction and statistical analysis, which was validated by B.H.T. J.Q.S. developed an interactive web-based calculator. All authors were involved in interpretation of the data and discussed the results. Q.C. wrote the first draft of this paper. Y.J. participated in the revision. All authors agreed on the final draft of this study. The Corresponding Author has the right to grant on behalf of all authors. All authors read and approved the final manuscript.

This work was supported by grants from National Natural Science Foundation[71804186, 82073671]; National Key R\&D Program [2017YFC0908005]; Military Key Discipline Construction Project (Health Service—Naval Health Service Organization and Command); Shanghai Key Disciplines of Public Health [GWV-10.1-XK05]; Special Clinical Research in Health Industry in Shanghai [20184Y0054]; Shanghai Sail Program[19YF1459200]; the Military Medical Science and Technology Youth Cultivation Project[21QNPY030, 21QNPY031]; the Sailing Talents Project of the Naval Military Medical University; Research and Development of Medical Protection Technology[19WLMS-13]; and Shanghai Industrial collaborative innovation project[2021-cyxt1-kj10].

The MIMIC-III analyzed during our study are available in the PhysioNet repository, [https://mimic.mit.edu/]. The ICU-CH are not publicly available due to privacy and ethical restrictions but are available from the corresponding author on reasonable request.

The protocol was approved by the Ethics Committee of the Naval Medical University. The MIMIC-III is public de-identified databases thus informed consent

and approval of the Institutional Review Board was waived. Written informed consent was obtained from individual at ICU-CH.

## Consent for publication

Not applicable.

## Competing interests

The authors have declared that there is no conflict of interest.

## Author details

${ }^{1}$ Department of Health Statistics, Naval Medical University, No. 800 Xiangyin Road, Shanghai 200433, China. ${ }^{2}$ School of Medicine, Tongji University, Shanghai, China. ${ }^{3}$ Institute of Military Health Management, Naval Medical University, Shanghai, China. ${ }^{4}$ Department of Cardiology, PLA General Hospital, No. 28 Fuxing Road, Beijing 100853, China. ${ }^{5}$ Department of Burn Surgery, Changhai Hospital, Naval Medical University, No. 800 Xiangyin Road, Shanghai 200433, China. ${ }^{6}$ Department of Pharmaceutical Administration and Regulation, Zhejiang Pharmaceutical College, Ningbo, China.

## Received: 2 September 2021 Accepted: 9 March 2022 Published online: 03 May 2022

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Ready to submit your research? Choose BMC and benefit from:

- fast, convenient online submission
- thorough peer review by experienced researchers in your field
- rapid publication on acceptance
- support for research data, including large and complex data types
- gold Open Access which fosters wider collaboration and increased citations
- maximum visibility for your research: over 100M website views per year

At BMC, research is always in progress.
Learn more biomedcentral.com/submissions