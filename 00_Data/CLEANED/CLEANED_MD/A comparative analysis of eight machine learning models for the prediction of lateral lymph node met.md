## OPEN ACCESS

EDITED BY
Terry Francis Davies,
Icahn School of Medicine at Mount Sinai, United States

REVIEWED BY
An-Cheng Qin,
Suzhou Municipal Hospital, China
Bao-qiang Wu,
Changzhou No. 2 People's Hospital, China
Jian-jun Tang,
Changzhou Wujin People's Hospital, China
Qungang Chang,
First Affiliated Hospital of Zhengzhou University, China
Luca Pio,
St. Jude Children's Research Hospital, United States
Yin Detao,
First Affiliated Hospital of Zhengzhou University, China
*CORRESPONDENCE
Yong Jiang
yjiang8888@hotmail.com
SPECIALTY SECTION
This article was submitted to
Thyroid Endocrinology,
a section of the journal
Frontiers in Endocrinology
RECEIVED 27 July 2022
ACCEPTED 14 October 2022
PUBLISHED 28 October 2022
CITATION
Feng J-W, Ye J, Qi G-F,
Hong L-Z, Wang F, Liu S-Y
and Jiang Y (2022) A comparative analysis of eight machine learning models for the prediction of lateral lymph node metastasis in patients with papillary thyroid carcinoma. Front. Endocrinol. 13:1004913. doi: 10.3389/fendo.2022.1004913

COPYRIGHT
(c) 2022 Feng, Ye, Qi, Hong, Wang, Liu and Jiang. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## A comparative analysis of eight machine learning models for the prediction of lateral lymph node metastasis in patients with papillary thyroid carcinoma

Jia-Wei Feng, Jing Ye, Gao-Feng Qi, Li-Zhao Hong, Fei Wang, Sheng-Yong Liu and Yong Jiang*

The Third Affiliated Hospital of Soochow University, Changzhou First People's Hospital, Changzhou, Jiangsu, China

Background: Lateral lymph node metastasis (LLNM) is a contributor for poor prognosis in papillary thyroid cancer (PTC). We aimed to develop and validate machine learning (ML) algorithms-based models for predicting the risk of LLNM in these patients.

Methods: This is retrospective study comprising 1236 patients who underwent initial thyroid resection at our institution between January 2019 and March 2022. All patients were randomly split into the training dataset ( $70 \%$ ) and the validation dataset (30\%). Eight ML algorithms, including the Logistic Regression, Gradient Boosting Machine, Extreme Gradient Boosting, Random Forest (RF), Decision Tree, Neural Network, Support Vector Machine and Bayesian Network were used to evaluate the risk of LLNM. The performance of ML models was evaluated by the area under curve (AUC), sensitivity, specificity, and decision curve analysis.

Results: Among the eight ML algorithms, RF had the highest AUC (0.975), with sensitivity and specificity of 0.903 and 0.959 , respectively. It was therefore used to develop as prediction model. The diagnostic performance of RF algorithm was dependent on the following nine top-rank variables: central lymph node ratio, size, central lymph node metastasis, number of foci, location, body mass index, aspect ratio, sex and extrathyroidal extension

Conclusion: By combining clinical and sonographic characteristics, ML algorithms can achieve acceptable prediction of LLNM, of which the RF model performs best. ML algorithms can help clinicians to identify the risk probability of LLNM in PTC patients.

## REYWORDS

Lateral lymph node metastasis, machine learning, prediction model, random forest, papillary thyroid carcinoma

Introduction

Thyroid cancer is one of the most common malignant endocrine carcinomas with a rapidly increasing incidence. Papillary thyroid carcinoma (PTC) is the most common histological type of thyroid cancer (1). The incidence of lymph node metastasis (LNM) is high, ranging from 49% to 90% (2, 3). PTC patients with lateral lymph node metastasis (LLNM) are reported to have higher rates of disease persistence, recurrence and distant metastasis than patients with or without central lymph node metastasis (CLNM) (4).

Current methods for assessing preoperative lymphatic status mainly include ultrasound and fine needle aspiration cytology (FNAC). However, the diagnostic sensitivity of ultrasound to cervical LNM is only about 20% to 40% (5, 6). And the false negative rate of FNAC can be as high as 16.7% (7). Hence, occult LLNM has been reported to occur in up to 55% of PTC patients with clinically negative (cN0) lateral neck (8). Prophylactic lateral neck dissection (LND) is not recommended for patients with cN0 lateral neck (9--11). Considering the existence of occult LLNM that is not easily detected preoperatively, some patients undergoing thyroidectomy may have some metastatic lymph nodes in the lateral compartment (12). Therefore, accurate assessment of lateral cervical lymph node status in PTC patients has a guiding role in clinical decision-making.

At present, studies have reported several risk factors of LLNM, and established predictive models. However, these results are inconsistent. Due to the complexity of medical data, there are significant connections between the various factors of predictive models, Therefore, there are also significant differences in the calculation methods of the model. Machine learning (ML) is a new type of artificial intelligence and is widely used in healthcare data analysis (13--17). By using the ML algorithms, data can be accurately processed, connections among important data can be analyzed, and accurate decisions can be made. Through the powerful predictive capabilities of ML algorithms, predictive tools that are better than traditional statistical modeling can be developed in some cases. Unfortunately, there are currently no studies training ML algorithms to predict LLNM of PTC patients.

We aimed to develop models based on eight ML algorithms using clinical and sonographical features. By selecting one model that performs best in predicting the risk of LLNM among PTC patients, individual strategies could be proposed to help clinicians to make therapeutic decisions.

## Materials and methods

### Patients population

This retrospective study was approved by the Ethics Committee of Changzhou First People's Hospital, and written informed consent was obtained from all patients. Consecutive patients who underwent initial thyroid resection at our institution between January 2019 and March 2022 were reviewed. The exclusion criteria were as follows: (1) non-PTCs or other subtypes than classic PTC; (2) history of prior treatment for head and neck cancer; (3) history of cervical radiation exposure in childhood; (4) family history of thyroid cancer; (5) history with other malignancy; (6) incomplete clinical data; (7) loss to follow-up; (8) patients who underwent non-curative surgery (residual tumor or lymph node detected within 6 months of initial surgery). A total of 1236 patients were enrolled in this study.

### Surgical strategy

All patients were confirmed as Bethesda Categories V or VI according to ultrasound-guided FNAC. Cervical lymph nodes with the following characteristics were suspected of metastases: hyperechoic changes, roundness or necrosis, loss of the fatty hilum, microcalcification or peripheral vascularity (18). FNAC was performed preoperatively to confirm the histopathological diagnosis of suspicious lateral lymph nodes.

All patients underwent total thyroidectomy or thyroid lobectomy. According to the Chinese guidelines for diagnosis and treatment of differentiated thyroid carcinoma, central neck dissection (CND) was routinely performed for PTC patients. According to the American Thyroid Association guidelines (9) and Chinese guidelines, LND was performed only in patients with high suspicion of LLNM based on preoperative imaging data and FNAC. CND referred to the removal of prelaryngeal, pretracheal and paratracheal lymph nodes. LND included the removal of the lateral lymph nodes, including level II to V, while preserving the spinal accessory nerve, internal jugular vein, or sternocleidomastoid muscle.

### Clinicopathological and sonographical features

We included a total of 18 variables in this study. Clinicopathological features included sex, age, body mass index (BMI), diabetes, BRAF V600E mutation, chronic lymphocytic thyroiditis (CLT), maximum tumor size, the number of foci, bilaterality, location, CLNM and central lymph node ratio (CLNR). BMI (kg/m^{2}) was defined as weight (kg) divided by height (m) squared. According to the World Health Organization-BMI standard, enrolled PTC patients were divided into normal (BMI < 25 kg/m^{2}), overweight (25 kg/m^{2} ≤ BMI). The diagnosis of CLT included any of the following: (i) antibodies to thyroid peroxidase level >50 IU/mL, (ii) diffuse heterogeneity on ultrasound, (iii) diffuse lymphocytic thyroiditis on histopathology (19). CLNR was defined as the ratio of

metastatic lymph nodes in the central compartment out of the number of dissected lymph nodes in the central compartment.

Specific evaluation parameters of malignant thyroid lesions included: nodular composition, echogenicity, calcification, aspect ratio and margin, including irregular shape and extrathyroidal extension (ETE). More than two radiologists with 10 years of experience in thyroid cancer ultrasound diagnosis evaluated images.

The surgeon dissected all lymph node specimens according to the level of the neck and sent them to the department of pathology for examination. Each lymph node was fixed in 20% buffered formalin, embedded in paraffin, sectioned, and stained with hematoxylin and eosin. Lymph nodes with suspected cancer involvement were further investigated by using immunohistochemical staining. All pathological specimens were reviewed and cross-checked by two or more experienced pathologists microscopically.

## Development of ML-based models

We split all patients randomly into two groups, the training dataset (70%) and the validation dataset (30%). Based on the presence or absence of LLNM, We also divided the overall study population into two groups and compared baseline information. Logistic Regression (LR) was conducted to assess independent predictors associating with LLNM.

Eight types of ML algorithms were applied in this study, including LR, Gradient Boosting Machine (GBM), Extreme Gradient Boosting (XGB), Random Forest (RF), Decision Tree (DT), Neural Network (NNET), Support Vector Machine (SVM) and Bayesian Network (BN) (16, 17, 20--22). Only LR is considered as conventional method among all eight algorithms, and the others are representative supervised ML-based algorithms. Only DT and LR are explainable, where the users are able to identify the function between variables and predicted outcomes. The other algorithms are inexplicable, where function between variables and the outcome is invisible to the user. In order to construct more reliable ML-based predictive models, we used the z- score normalization to preprocess all continuous variables (23).

## Validation strategy and feature selection

Overfitting, meaning the model becomes too specific to fit to another dataset, is a common risk, especially when the number of variables is large (24). In order to minimize the adverse effect of overfitting, we adopted 5-fold cross-validation in the training set. The relative importance ranking of each input variable was analyzed in each model. We compared all variables to determine their predictive importance for LLNM. The predictive performance of these models was assessed by the area under the receiver operating characteristic (ROC) curve (AUC). In the comparison of ML algorithms, the closer the AUC was to 1, the better the performance of the model. However, ROC curve is a traditional diagnostic method that focuses only on sensitivity and specificity. In this case, we employed decision curve analysis (DCA) to assess the clinical utility of these models (25).

## Statistical analysis

All statistical analysis was performed by using SPSS Version 25.0 software (Chicago, IL, USA), and R software Version 3.5.3 (The R Foundation for Statistical Computing). Pearson Chi-square test or Fisher's exact test was used for categorical data. Normally distributed quantitative parameters were compared by Student's t-test, while non- normally distributed parameters were compared by the Mann-Whitney U test. We considered P value <0.05 to be statistically significant. For independent risk factors for LLNM, odds ratios (ORs) with 95% confidence intervals (CIs) were calculated by using multivariate logistic regression analysis with backward stepwise selection. R software (Version 3.5.3) was used to develop ML-based models and DCA.

## Results

## Demographics and sonographic features

The 1236 patients were divided into two groups randomly: approximately 866 (70%) cases were conducted as the training dataset, and the remaining around 370 (30%) cases were used as the validation dataset. No significant differences were observed in clinicopathological and sonographic features of thyroid nodules (P >0.05 for all comparisons), which justified their use as training and validation cohorts (Table 1).

Among the 866 patients in the training cohort, 257 were males and 609 were females. The average age was 45.1 ± 10.5 years (range 18--82 years). Four hundred and eighty-one (55.5%) patients developed CLNM, and 176 (20.3%) patients developed LLNM. The validation cohort consisted of 370 patients (mean age, 46.3 ± 11.2 years), including 93 males and 277 females. CLNM were positive in 190 (51.4%) cases, and LLNM were positive in 64 (17.3%) cases. Baseline epidemiological and sonographic characteristics of the two cohorts are shown in Table 1.

## Univariate and multivariate analysis of potential factors for LLNM

In univariable analysis, gender, diabetes, tumor size, number of foci, bilaterality, location, aspect ratio, irregular shape, ETE, microcalcification, CLNM and CLNR were all significantly related with LLNM in all patients (all P < 0.05).

TABLE 1 Comparison of clinical and ultrasonic characteristics of the PTC patients in the training and validation dataset.


TABLE 1 Continued


PTC, papillary thyroid carcinoma; Y, year; BMI, body mass index; CLT, chronic lymphocytic thyroiditis; A/T, aspect ratio (height divided by width on transverse views); ETE, extrathyroidal extension; CLNM, central lymph node metastasis; CLNR, central lymph node ratio; LLNM, lateral lymph node metastasis.

All above parameters were included in the LR. The results showed that male (OR: 1.521, 95\% CI: 1.077-2.149, $P=0.017$ ), tumor size ranges between 1.0 to 2.0 cm (OR: $1.753,95 \% \mathrm{CI}$ : $1.206-2.548, P=0.003$ ), tumor size ranges between 2.0 to 4.0 cm (OR: $3.381,95 \%$ CI: $2.075-5.507, P<0.001$ ), tumor size > 4.0 cm (OR: $2.167,95 \%$ CI: $1.015-5.625, P=0.012$ ), three or more tumor foci (OR: $3.254,95 \%$ CI: $2.014-5.257, P<0.001$ ), tumors located in the upper pole (OR: $2.368,95 \%$ CI: 1.6913.317, $P<0.001$ ), presence of ETE (OR: $9.145,95 \%$ CI: 4.09220.439, $P<0.001$ ), presence of CLNM (OR: $4.261,95 \%$ CI: $2.637-6.887, P<0.001$ ), and CLNR $\geq 0.5$ (OR: $2.379,95 \%$ CI: $1.642-3.449, P<0.001$ ) were independent predictors of LLNM (Table 2).

## Predictive performance and clinical usefulness of ML-based models

We used 18 variables to develop predictive models for LLNM based on eight algorithms. Figure 1 and Table 3 show the predictive performance of these models. In the training cohort, the best performance was observed in the RF model, whose AUC was 0.975 (Figure 1A). It was followed by XGB and GBM with AUCs of 0.924 and 0.899 , respectively. All ML-based models except DT (AUC $=0.777$ ) and SVM (AUC $=0.824$ ) were better than the conventional method-LR (AUC $=0.837$ ). In the training cohort, the RF model performed the best with an AUC as high as 0.853 (Figure 1B). And the sensitivity and specificity of

TABLE 2 Univariate analysis and multivariate analysis of factors associated with LLNM in whole cohort.


(Continued)

TABLE 2 Continued


PTC, papillary thyroid carcinoma; Y, year; BMI, body mass index; CLT, chronic lymphocytic thyroiditis; A/T, aspect ratio (height divided by width on transverse views); ETE, extrathyroidal extension; CLNM, central lymph node metastasis; CLNR, central lymph node ratio; LLNM, lateral lymph node metastasis.

the RF model in the training cohort were 0.903 and 0.959, respectively. The sensitivity and specificity of the RF model in the validation cohort were 0.891 and 0.775, respectively (Table 3). Above results proved the best diagnostic performance of RF model.

Moreover, we applied the mixed Lift curves of the eight ML models in the training cohort. The drawing process of the Lift curve is similar to the ROC curve, the difference is that the Lift value and the robust plane pose change in opposite directions, forming the opposite form of the Lift curve and the ROC curve. Furthermore, the Lift curve considers the accuracy of the classifier: the ratio of the number of positive classes obtained with the classifier to the number of positive classes obtained randomly without the classifier. RF model also has the best diagnostic performance among the current mix Lift curves (Figure 2).

Furthermore, we used the DCA to evaluate the clinical values of these models (Figure 3). Assuming that all patients do not have positive lymph nodes in the latter compartment, the solid black line (negative line) indicates that when no patient accepts LND, net benefit is zero. On the contrary, the solid grey line (positive line) indicates the net benefits when all patients have LLNM and receive LND. According to the incidence of LLNM among patients with PTC, the reasonable range of thresholds was set from 0.3 to 0.9. Almost at the entire range, all ML-based models showed higher net benefits than the two extreme lines (negative line and positive line) except DT. It was noteworthy that RF, XGB and GBM performed significantly better than the others at most of threshold points. Within a threshold range of 0 to 0.7, XGB had a higher net benefit than GBM. But within the threshold range of 0.8 to 0.9, the net benefit of GBM was higher than that of XGB. In almost the entire threshold probability range, the RF model had the highest net benefit, much higher than XGB and GBM.

### Relative importance of variables in ML-based models

Considering favorable AUCs and clinical benefits based on the DCA, we selected RF, XGB and GBM as the models with the most potential for predicting LLNM in PTC patients. The relative importance of variables in RF, XGB and GBM for predicting LLNM is shown in Figure 4. Although the importance of variables in these ML algorithms were slightly different among these three models. It was obvious that CLNR, CLNM, size, number of foci and location ranked in the top five. In contrast, solid, hypoechogenicity, BRFA, and diabetes did not contribute much to the prediction of the risk of LLNM in PTC patients.

The relationship between the number of variables and the AUCs of models is shown in Figure 5. The AUC of the RF model plateaued when 9 variables were introduced, while the AUCs of XGB and GBM started to decrease when they reached the highest point (10 variables).

Accordingly, we chose the RF model as the best predictive model according to its best performance in ROC curve, Lift curve and DCA. We further performed the collinearity test for nine top-rank variables in RF model. In general, the variance inflation factor (VIF) and tolerance are most commonly used to detect collinearity. Tolerance and VIF are reciprocal of each other. When the VIF is less than 3, there is no collinearity problem; when the VIF value is greater than 3 and less than 10, there is a moderate degree of collinearity; when the VIF is greater than 10, there is a serious collinearity problem. Likewise, tolerance values greater than 0.1 indicate no collinearity. In our study, the VIF for CLNR, size, CLNM, number of foci, location, BMI, aspect ratio, sex and ETE were 1.493, 1.160, 1.513, 1.042, 1.031, 1.055, 1.049, 1.113 and 1.021, respectively. Moreover, the tolerance value for CLNR, size, CLNM, number

![img-0.jpeg](img-0.jpeg)

FIGURE 5 The mixed ROC curves of the eight machine learning models for prediction of LLNM. (A) The mixed ROC curves in the training cohort; (B) The mixed ROC curves in the validation cohort. ROC receiver operating characteristic; LLNM Lateral lymph node metastasis; LR Logistic Regression; GBM Gradient Boosting Machine; XGB Extreme Gradient Boosting; RF Random Forest; DT Decision Tree; NNET Neural Network, SVM Support Vector Machine; BN Bayesian Network.

TABLE 3 Predictive performance comparison of the eight types of machine learning algorithms in the training and validation dataset.


AUC, the area under the curve; LR, logistic regression; GBM, gradient boosting machine; XGB, extreme gradient boosting; RF, random forest; DT, decision tree; NNET, neural network; SVM, support vector machine; BN, Bayesian network. of foci, location, BMI, aspect ratio, sex and ETE were 0.670 , $0.862,0.661,0.960,0.970,0.948,0.953,0.898$ and 0.979 , respectively. The above results indicate that there is no collinearity between the above variables.

At last, The nine top-rank variables were identified to construct the best predictive model, including CLNR, size, CLNM, number of foci, location, BMI, aspect ratio, sex and ETE.

## Discussion

Although lateral neck is the second most common compartment for LNM, prophylactic LND was not recommended by most clinical guidelines, including National Comprehensive Cancer Network (11), American Thyroid Association guidelines (9), the Japanese Association of

Figure 2 The mixed Lift curves of the eight machine learning models in the training cohort. LR Logistic Regression; GBM Gradient Boosting Machine; XGB Extreme Gradient Boosting; RF Random Forest; DT Decision Tree; NNET Neural Network, SVM Support Vector Machine; BN Bayesian Network.

![img-1.jpeg](img-1.jpeg)

FIGURE 3 Decision curve for predictive models based on machine learning models in the training cohort. LR Logistic Regression; GBM Gradient Boosting Machine; XGB Extreme Gradient Boosting; RF Random Forest; DT Decision Tree; NNET Neural Network, SVM Support Vector Machine; BN Bayesian Network.

Endocrine Surgeons and the Japanese Society of Thyroid Surgeons (10). And the indication for prophylactic LND remained controversial (26). Moreover, due to the low metastasis rate in this region as well as the high incidence of postoperative complications, LND is performed only for those with clinically positive LLNM in most medical institutions.

ML algorithms have the advantage of automatically learning from input data and identifying patterns and trends in these data. There are many studies using ML for the differential diagnosis of benign and malignant thyroid nodules (27, 28). However, there are few studies on the application of ML models to predict LNM in PTC patients, especially LLNM. Lee et al. (29) applied a deep learning-based computer-aided diagnosis system to locate and diagnose metastatic lymph nodes in patients with thyroid cancer. But they used only one ML model and did not compare the performance of multiple ML models in distinguishing metastatic lymph nodes in patients with thyroid cancer.

We aimed to predict the risk of LLNM more accurately and filter the best prediction model. In this study, by combining the clinical and imaging characteristics of patients, we developed eight models using the ML algorithm to predict the LLNM of

![img-2.jpeg](img-2.jpeg)

FIGURE 4 Relative importance ranking of each input variable for prediction of LLNM in the machine learning models. (A) Random Forest; (B) Gradient Boosting Machine; (C) Extreme Gradient Boosting.

![img-3.jpeg](img-3.jpeg)

**FIGURE 5** Predictive performance of the RF, XGB and GBM model with different numbers of variables. *RF* Random Forest; *XGB* Extreme Gradient Boosting; *GBM* Gradient Boosting Machine.

PTC patients. We first used ROC analysis and mixed Lift curves to evaluate the predictive performance of these models. Most of the eight models maintained high AUCs. Except for DT and SVM, all ML-based models performed better than LR model using a traditional statistical method in predicting LLNM (Figures 1, 2 and Table 3). The clinical value of these models was then assessed using DCA. DCA has enormous clinical utility and has been used in many medical studies. According to DCA, most of these models outperformed the positive line and negative line, indicating that the overall net benefit of performing LND for patients with high risk of LLNM identified by the model was higher than in all patients or no patient undergoing the same surgical procedure. Three models (RF, XGB and GBM) performed better than the others at most of threshold points. At last, combined with the results of ROC, mixed Lift curves and DCA, the RF model performed best in distinguishing between LLNM and non-LLNM. Besides, the validation set confirmed that the RF model was the best predictive model for LLNM of PTC (AUC=0.853).

The RF structure is simple, easy to understand, and more efficient than similar methods. From a computational point of view, RF is a more advanced algorithm based on DT, which can be used for both regression and classification. In addition, RF can be directly used for high-dimensional problems. From a statistical point of view, RF has the following characteristics, that is, the priority of characteristics, different weight coefficients fall into different categories, and illustration and unsupervised learning ability. Moreover, RF is a well-known ML algorithm for classification tasks and is inherently capable of resisting overfitting. According to previous meta-analysis of metastatic lymph node studies (30), computed tomography demonstrated a sensitivity of 81.1% and a specificity of 84.0% in detecting LLNM, and ultrasound demonstrated a sensitivity of 75.8% and a specificity of 88.0%. When we compared the diagnostic performance of the RF model with that in the meta-analysis, our RF model achieved better sensitivity (90.3%) and specificity (95.9%).

Although the link between variables and outcomes in most ML-based models is invisible, the predicted importance of variables in each model could be obtained by using a classifierspecific estimator (Figure 4). Therefore, the nine top-rank variables were considered to be the most important risk factors for LLNM in the RF model: CLNR, size, CLNM, number of foci, location, BMI, aspect ratio, sex and ETE. We also tested the collinearity of these variables and found that there was no collinearity between the above variables. Tumor size is the most important preoperative predictor of LLNM in PTC patients, and CLNR is the most important postoperative predictor of LLNM in PTC patients. Diameter was also reported in previous studies to be an independent risk factor for LLNM in PTC patients (31, 32). This may be attributed to the more extensive the tumors, the more aggressive and proliferative. Lymph node ratio is considered a variable reflecting tumor burden in PTC and other solid tumors (33). It is important to note that LNR is not only affected by disease burden, but also by the extent of neck dissection and pathological examination. This requires the surgeon to remove the central lymph nodes as much as possible and the pathologist to carefully check the status of the removed lymph nodes ensuring the accuracy of the model. According to RF model, for patients with several preoperative risk factors of LLNM, detailed preoperative examinations (such as high-resolution ultrasound by experienced sonographers) should be performed to detect small metastatic lymph nodes early. Moreover, experienced surgeons are recommended to perform detailed operations for these patients, and carbon nanoparticles suspension injection can be used during the operation to prevent the miss of small metastatic lymph nodes.

Furthermore, for patients with high CLNR, heightened vigilance for occult LLNM may be warranted for these patients postoperatively. More closely follow-up should be applied for these patients after surgery. For suspicious lymph nodes detected in the lateral compartment postoperatively, FNAC should be actively conducted to confirm the histopathologic diagnosis, and LND should be considered if necessary.

To our surprise, BMI had no significant significance in univariate analysis (P=0.077), but was ranked sixth in the top. In addition, although the seventh-ranked shape (A/T) was statistically significant in univariate variables, it had no significant significance in multivariate analysis. This may be attributed to the amazing advantages of ML-based models in data mining, which can find more relationships between variables and results than traditional methods. Because LR is used to analyze prognostic factors based on linear combinations between variables, if the degree of correlation between variables is high, the analysis is limited by overfitting results. ML models, on the other hand, do not assume a linear combination of variables used, thus reducing the effect of correlations between variables. Therefore, factors including BMI and aspect ratio were important constituent variables of RF models and were used in other ML models at high frequencies. Thus, the AUC of the LR model based on the above factors was significantly lower than the most ML-based models.

The advantage of this research lies in the innovation of technology and method. By using eight ML methods, we outperformed other methods on clinical data and its application. However, there also has limitations. First, because this was a retrospective study, potential selection bias might exist. Second, ML model we built was based on the data from a single institution, which may limit its generality. Moreover, patients enrolled in our study were all native Chinese population, most of whom were female. Residual confounding variables of unmeasured factors such as race and region cannot be ruled out. Last, the AUCs of the training set were higher than that of the validation set, indicating the overfitting in ML algorithms-based models. This may be related to the fact that our models are complicated and the description data is too accurate. We will conduct prospective multicenter institutional trials to achieve more objective conclusions by increasing the amount of data, reducing the number of data characteristics (dimension), and reducing the complexity of the models to reduce overfitting.

In summary, we proved that ML algorithms are feasible to incorporate clinicopathological and sonographic features to predict LLNM in patients with PTC. We used the ML algorithms to construct and compare the performance of eight predictive models, of which the RF model is the best. In the future, we will integrate imaging, molecular, and genetic data to improve the performance of our models, thus providing more accurate methods for clinical and surgical decisions and postoperative follow-up.

## Data availability statement

The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation.

## Ethics statement

Written informed consent was obtained from the individual(s) for the publication of any potentially identifiable images or data included in this article.

## Author contributions

J-WF and L-ZH: writing - original draft, software, and data curation. S-YL: validation, formal analysis, and data curation. FW: conceptualization. JY and G-FQ: validation and investigation. YJ: writing - review \& editing, visualization, and supervision. All authors contributed to the article and approved the submitted version.

## Acknowledgments

Lei Qin, the English language editor, was responsible for correcting language and grammar issues.

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.
