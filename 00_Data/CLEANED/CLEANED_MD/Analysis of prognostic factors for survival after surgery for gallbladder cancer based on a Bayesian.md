# SCIENTIFIC REP ${ }^{\circledR R T S}$ 

## OPEN

Received: 24 August 2016
Accepted: 2 March 2017
Published online: 22 March 2017

## Analysis of prognostic factors for survival after surgery for gallbladder cancer based on a Bayesian network

Zhi-qiang Cai ${ }^{1}$, Peng Guo ${ }^{1}$, Shu-bin $\mathrm{Si}^{1}$, Zhi-min Geng ${ }^{2}$, Chen Chen ${ }^{2}$ \& Long-long Cong ${ }^{2}$


#### Abstract

The factors underlying prognosis for gallbladder cancer (GBC) remain unclear. This study combines the Bayesian network (BN) with importance measures to identify the key factors that influence GBC patient survival time. A dataset of 366 patients who underwent surgical treatment for GBC was employed to establish and test a BN model using BayesiaLab software. A tree-augmented naïve Bayes method was also used to mine relationships between factors. Composite importance measures were applied to rank the influence of factors on survival time. The accuracy of BN model was $81.15 \%$. For patients with long survival time ( $>6$ months), the true-positive rate of the model was $77.78 \%$ and the false-positive rate was $15.25 \%$. According to the built BN model, the sex, age, and pathological type were independent factors for survival of GBC patients. The N stage, liver infiltration, T stage, M stage, and surgical type were dependent variables for survival time prediction. Surgical type and TNM stages were identified as the most significant factors for the prognosis of GBC based on the analysis results of importance measures.


Gallbladder cancer (GBC) is the most common malignant tumour of the biliary tract worldwide ${ }^{1}$. It is also the most aggressive cancer of the biliary tract with the shortest median survival from the time of diagnosis ${ }^{2}$. The only option for a complete cure is surgical resection. However, currently only $10 \%$ of GBC patients are candidates for surgery with a curative intent. The current international guidelines may not suit for all regions as the difference of financial resources, cultural attitudes and environmental factors. Therefore, it is of vital importance to identify practical key factors that affect the survival of patients with GBC to support the prediction of survival time and decisions regarding therapy.

Data-based statistical methods have been extensively applied to the analysis of prognostic factors for GBC patient survival ${ }^{3,4}$. These studies have examined prognostic factors such as T stage, patient age, surgical type, and recurrence using statistical analyses of clinical data. However, these studies describe the separate impacts of single factors associated with prognosis and have neglected the joint influence of multiple factors. The roles of interactions or mutual influences among these factors are not yet clearly understood, so an effective modelling method is required to explore and represent the relationships among these factors.

Recent studies have analysed medical data using artificial intelligence to support specialists in the course of clinical stage, decision-making, and prognosis prediction. Wang et al. ${ }^{5}$ developed a nomogram based on a web browser using a parametric survival model from the Surveillance, Epidemiology and End Results-Medicare database to predict which gallbladder patients may benefit from adjuvant chemoradiotherapy. Additionally, Wang et al. ${ }^{6}$ put forward a multivariate Cox proportional hazards model to enable individualised predictions of the net survival benefit of adjuvant radiotherapy for GBC patients based on specific tumour and patient characteristics. Horgan et al. ${ }^{7}$ undertook a systematic review and meta-analysis to determine the impact of adjuvant therapy on survival in the treatment of biliary tract cancer. Udelnow et al. ${ }^{8}$ conducted a two-centre observational study of the accuracy of a Bayesian network (BN) for short-term outcome prediction in cholecystectomy patients. Chukwuka et al. ${ }^{9}$ built a simple regression model to assess the variability of gallbladder contraction indices and to obtain

[^0]
[^0]:    ${ }^{1}$ Department of Industrial Engineering, School of Mechanical Engineering, Northwestern Polytechnical University, Xi'an 710072, Shaanxi, China. ${ }^{2}$ Department of Hepatobiliary Surgery, First Affiliated Hospital, Xi'an Jiaotong University, Xi'an 710061, Shaanxi, China. Correspondence and requests for materials should be addressed to S.-b.S. (email: sisb@nwpu.edu.cn) or Z.-m.G. (email: gengzhimin@mail.xjtu.edu.cn)

![img-0.jpeg](img-0.jpeg)

**Figure 1. (A)** Overall survival of GBC patients after surgery. **(B)** Survival of GBC patients with different TNM stage. **(C)** Comparison of patient survival in GBC patients after radical resection or palliative resection.

The gastric emptying ratio, although some methods of data mining have been developed and applied to survival prediction for patients with GBC, most methods cannot represent variables under uncertainty and ignore the cause-and-effect relationships between prognostic factors.

The BN is specialized in its representation of nonlinear and variable interactions^{10}. Furthermore, importance measures are useful tools to deal with uncertainty in model prediction^{11}. We have used the BN and importance measures to identify the most significant predictors of survival time for patients who have undergone hepatectomy for treatment of hepatocellular carcinoma^{12}. In this paper, we used BN to construct a model that predicts prognosis for patients with GBC. Then the importance measures were used to sort these prognostic factors. The BN model, which was built based on practical medical data, could provide efficient individual prognosis and optimal treatment by considering regional health care conditions.

## **Results**

### **General characteristics of the study population**

Of the study patients, 260 (71.04%) were female and 106 (28.96%) were male. The median age at the time of surgery was 63 years. Eighty-three (22.79%) patients were positive for jaundice and 203 (55.46%) were positive for liver infiltration. Pathological analysis identified 311 (84.97%) patients with adenocarcinoma and 55 (15.03%) with non-adenocarcinoma lesions, including squamous cell carcinoma (9), neuroendocrine neoplasm (9), sarcoma (8), mucinous adenocarcinoma (11), and adenosquamous carcinoma (18). Protuberant tumors were present in 252 (68.90%) patients, while 114 (31.10%) had infiltrative lesions. The proportions of patients with lesions classified as pathological grades of well, moderate, and poor were 11.20%, 42.62%, and 46.17%, respectively. The proportions of patients with T stages of Tis, T1a, T1b, T2, T3, and T4 were 0.82%, 0.82%, 2.19%, 1.37%, 59.02%, and 35.79%, respectively. Meanwhile, proportions of patients with N stage lesions of grades N0, N1, and N2 were 28.96%, 37.16%, and 33.88%, respectively. Proportions of patients with M stage lesions of M0 and M1 were 72.40% and 27.60%, respectively. Proportions of patients requiring a total surgical time of ≤3 hours and >3 hours were 57.10% and 42.90%, respectively. Blood loss of >1000 mL occurred in 6.56% of patients.

The surgical approach used for 142 (38.80%) patients was radical surgery (R0), including 11 hepatopancreatoduodenectomy (HPD) procedures and 15 right hepatectomy or right trisegmentectomy procedures. Palliative surgical intervention was performed for the remaining cases, with 224 (61.20%) cases undergoing R1/2 resection: 72 underwent cholecystectomy, 107 cholecystectomy with biliary tract drainage, 19 biliary tract external drainage, 18 opening and closure of the abdomen, and 8 gastrointestinal anastomosis.

### **Survival analysis**

The survival curve is shown in Fig. 1. The median survival time was 5.7 months with a 95% CI of 4.9–7.0 months. The mean survival time was 24.6 months, and the 1-, 3-, and 5-year overall survival rates were 34.2%, 26.8%, and 25.4%, respectively. The median survival time of patients with GBC of TNM stages 0–II and IIIA was not reached during the course of this study, with more than half of the patient cohort still alive when the study was concluded. Meanwhile, the median survival times for stage IIIB, IVA, and IVB patients were 7 months, 4 months, and 2.5 months, respectively, and the differences were statistically significant (P < 0.001). The median survival time of GBC with R1/2 resection was 3 months (P < 0.001).

### **Assessment of model efficacy**

The BN model was established after obtaining values for the required variables from 244 patient records in the training dataset to obtain a survival time. The 122 records in the testing dataset are used to test the model. The reliability and accuracy of prognosis predictions are obtained (Table 1) using confusion matrix evaluation indices with default probability threshold of 0.5. A patient was classified as having a long survival time (>6 months) when the probability was more than the threshold, otherwise the patient was classified as having a short survival time (≤6 months). The actual number of patients surviving for >6 months was 63, with 49 correctly classified—yielding a true positive rate (TPR) of 77.78%. The number of patients identified by the model was 58, and 49 of these had a survival time of >6 months, conferring a reliability of 84.48%. The above values were the predicted rates of correct classification. In the aggregate, 50 patients (≤6 months) and 49 patients (>6 months) were correctly classified, conferring a model accuracy of 81.15% (calculated as per


Table 1. Confusion matrix and reliability and accuracy of the BN model of prognosis.


Table 2. LR on survival time $>6$ months.
![img-1.jpeg](img-1.jpeg)

Figure 2. (A) ROC curve of survival time $>6$ months for BN. (B) ROC curve of survival time $>6$ months for LR.

Equation [1]). As the probability threshold varied from 0 to 1 , the corresponding FPR and TPR formed the ROC curve (Fig. 2A). The area under the curve (AUC) of the receiver operating characteristics ROC for the BN model was $78.1 \%$.

Logistic regression (LR) analysis was implemented with the original 438 dataset in SPSS. The stepwise backward algorithm was applied with a significance threshold of 0.1 . After ten steps, the final predictive model with all significant terms was obtained (Table 2). Obviously, T stage, N stage, M stage and pathological type have a significant value ( $\mathrm{p}<0.1$ ), which can be used to generate the ROC curve (Fig. 2B). The corresponding AUC of the ROC for the LR was $87.4 \%$.

Prognostic factors ranked by importance. The importance of correlative prognostic factors was analysed according to the established BN prognostic model. First, we obtained the prior probability distribution of each factor (Table 3). The prior probability of survival time was $\left\{\mathrm{p}(\mathrm{S}=0)=0.5355, \mathrm{p}(\mathrm{S}=1)=0.4645\right\}$, and the prognostic factors that were attribute variables were described as $\{\mathrm{p}(\mathrm{V}=0), \mathrm{p}(\mathrm{V}=1), \ldots\}$. Next, states of the attribute variables were modified and the posterior probability distribution of a survival time of $\leq 6$ months was calculated. The posterior probability was determined using $\{\mathrm{p}(\mathrm{S}=0 \mid \mathrm{V}=0), \mathrm{p}(\mathrm{S}=0 \mid \mathrm{V}=1), \ldots\}$. Finally, the importance measure of each variable was calculated using equations (2) to (8) described in the Materials and Methods. Results are shown in Table 3.

Multivariate analysis for various risk factors. After univariate analysis for the listed 13 factors with Log-rank test, 9 factors, including jaundice, liver infiltration, surgical type, T stage, N stage, M stage, pathological grade, pathological type and shape, were identified as risk factors ( $\mathrm{P}<0.05$ ) for prognosis of GBC. Then, a multivariate analysis base on Cox regression was performed to determine which univariate prognostic relationships were independent predictive factors. The results showed that the surgical type, N stage, M stage and pathological grade were independent risk factors ( $\mathrm{p}<0.05$ ) for prognosis of GBC (Table 4).


Table 3. Importance of prognostic factors in survival time ranking.


Table 4. Results of Cox multivariate regression analysis.

# Discussion 

In this study, we used a BN in combination with importance theory to identify the key factors underlying GBC patient prognosis under uncertainty. The BN model was used to predict patient survival time using data gathered from patients treated at the First Affiliated Hospital of Xi'an Jiaotong University in China. BN models can detect and express the hidden relationships among prognostic factors and are widely used in medical research fields. Furthermore, Demichelis et al. ${ }^{13}$ proposed an extension of the well-known Naïve Bayes classifier-which accounts for biological heterogeneity in a probabilistic framework-that relies on Bayesian hierarchical models

to develop a model with an accuracy of 0.65 . Our model correctly classified 50 patients with survival time ≤6 months and 49 who survived $>6$ months, leading to a model accuracy of $81.15 \%$. Additionally, the AUC of the ROC for the BN model was $78.1 \%$. Therefore, we obtained a higher TPR with a given FPR, meaning that we obtained higher prediction accuracy with lower risk.

Table 2 lists the results of LR on survival time with the stepwise backward algorithm. The results showed that T stage, N stage, M stage and pathological type had a statistical significance of $\mathrm{P}<0.1$, which were used to establish ROC curve and the AUC was $87.4 \%$. The difference of the two ROC results may be caused by the used of stepwise backward algorithm on LR, while BN analysed the whole factors.

Table 3 lists prognostic factors ranked by importance measures calculated using seven kinds of CIM: MBM, MRAW, MFV, MRRW, MAD, MMAW, and MMFV. The Birnbaum importance defines the importance of a given component as the probability that this component is critical to the functioning of the system ${ }^{14}$. The MBM accounts for the absolute deviation of each component state from the actual value in a multi-state system. A high value for MBM indicates that the reliability is highly-sensitive to perturbations in the state of a component. From this perspective, the value obtained for surgical type was highest, meaning that surgery type was the most significant factor dictating the prognosis of GBC patients. Meanwhile, MBM values for sex and age factors were small, meaning that they had a slight influence on patient prognosis.

The RAW measure quantifies the maximum percentage increase in system reliability generated by a particular component and it can be extended to a multi-state case. The MRAW adopts the existing condition perspective, and indicates which component is likely to improve the system performance the most, after it has been replaced by a better performing component ${ }^{15}$. This approach identified the M stage as the most significant factor influencing the prognosis of patients with GBC.

The FV importance measure quantifies the maximum decrement in system reliability caused by a particular component, while the RRW measures the potential damage caused to the system by a particular component. Equations (4) and (5) show that mathematical calculations can transform MFV into MRRW, affording them the same importance ranks. This approach identified the value for T stage as the largest, implicating the T stage as the most important factor underlying the prognosis of patients with GBC.

MAD, MMAW, and MMFV are alternative CIMs that account for the impact a given component has on system reliability, the perturbation of system reliability when a component state changes, and the probability that such changes occur. In other words, the MAD, MMAW, and MMFV measures account for both prior and posterior probabilities. From this perspective, the N stage had the most significant effect on the prognosis of patients with GBC. Additionally, sex and age factors had the smallest influence on GBC prognosis regardless of the importance measures selected.

The BN model depicts the dynamic and static characteristics of the dataset and expresses all the information in it. According to our model, N stage, liver infiltration, T stage, M stage, and surgical type were all dependent variables in survival time prediction. Other previous studies have considered the stage of cancer as the most significant factor for survival time ${ }^{16}$. GBC discovered incidentally has a better prognosis compared with patients with preoperative suspicion of GBC because of an earlier stage at incidental discovery ${ }^{17}$. The median survival times of GBC patients with M stages of $\mathrm{M}_{0}$ and $\mathrm{M}_{1}$ were 9.33 months and 2 months, respectively, with this difference statistically significant. The median survival times of GBC patients with T stages of $\mathrm{T}_{3}$ and $\mathrm{T}_{4}$ were 8 months and 2.67 months, respectively. The median survival times of GBC patients with N stages of $\mathrm{N}_{0}, \mathrm{~N}_{1}$, and $\mathrm{N}_{2}$ were 39.3 months, 4 months, and 2.67 months, respectively, with these differences statistically significant. The median survival times of GBC with R0 resection and R1/2 resection were 25.0 months and 3 months, respectively, with this difference statistically significant.

Table 3 lists prognostic factors ranked by importance measures and shows that the surgical type and TNM stage are the most significant factors among these factors, consistent with previous studies ${ }^{16-18}$. Table 4 lists prognostic factors analysed by Cox regression. The results showed that the surgical type, N stage, M stage and pathological grade were all independent risk factors ( $\mathrm{p}<0.05$ ) for prognosis of GBC, which are almost same with the results of importance analysis. Maybe the lack of data for T0-2 causes the small diffidence between the two methods, but what we have confirmed is that the surgical type, NM stage are the most significant factors. And understandably, different surgical types-including radical surgery and palliative surgery-lead to different outcomes for GBC patients, with curative resection prolonging survival. The advent of GBC stage has facilitated an improvement in survival rates, with patients at different stages undergoing different therapies. Stages 0-III are potentially resectable with curative intent, while stage IV is not because of distant metastases ${ }^{19}$.

Briefly, we have used BN combined with importance measures to indentify the key prognostic factors influencing patient survival following surgery for GBC and compared with the Cox regression results. Our data support the use of BN as an effective tool for medical data mining and show that importance measures can be applied to analyse the influence of variables related to a target ${ }^{12}$. Surgical type and TNM stage are significant predictive factors of survival time for patients with GBC. However, sufficient patient data are needed to achieve a high predictive accuracy ${ }^{20}$. Our study employed only 13 attribute variables in the BN model, with 366 patient records in the dataset. Therefore, additional and complete clinical records of patients with GBC should be collected for future research.

## Materials and Methods

Patients and data collection. The original medical records of 438 patients (Supplementary Table S1) who had undergone surgical procedures for the treatment of GBC were collected from the First Affiliated Hospital of Xi'an Jiaotong University in China from January 2008 to December 2012, with follow-up data was available until October 2014.

The patient dataset was established with 15 categories: jaundice, liver infiltration, pathological type, shape, pathological grade, T stage, N stage, M stage, age, surgical type, blood loss, surgical time, sex, survival state and


Table 5. Standard description of data. Jaundice was defined by the serum bilirubin level exceeding 32.4 umol/L $(2 \mathrm{mg} / \mathrm{dL})$. Clinical end-points and measurements included imaging examination such as abdominal ultrasound, Computed Tomography (CT) and Magnetic Resonance (MR) scan, and assaying serological tumor markers, which included the determination of carbohydrate antigen 125 (CA-125), carbohydrate antigen 19-9 (CA19-9) and carcinoembryonic antigen (CEA).
survival time (Table 5). Patients were assessed for TNM stage according to the American Joint Committee on Cancer (7th edition) ${ }^{21}$.

Indications for surgery. Different surgical procedures were performed based on the results of exploratory surgery and intraoperative pathological examination. In patients with advanced GBC either without involvement of the liver or with minimal liver infiltration, wedge resection of the gallbladder bed/segment IVb/V resection and regional/extended lymph node dissection was performed. When massive invasion of the liver was diagnosed, major hepatectomy procedures-such as right hemihepatectomy or right trisectionectomy-were performed. When tumours involved the extrahepatic bile duct or bulky regional lymph node metastasis near the bile duct was found, common bile duct resection was performed. Peritoneal seeding, bulky lymph node involvement, or para-aortic lymph node involvement were regarded as contraindications for surgery. HPD was considered in patients with the following conditions: (1) lower bile duct involvement, (2) pancreatic infiltration, (3) duodenal infiltration, or (4) bulky retropancreatic lymph node metastasis. Gastric resection was performed in cases of macroscopic infiltration.

Palliative surgical interventions were performed when en bloc tumour removal could not be achieved because of distant metastasis, peritoneal seeding, positive para-aortal lymph node metastasis, widespread tumour invasion, or other patient complications precluded aggressive surgery. For palliative surgery cases, biliary tract drainage was performed once jaundice or biliary tract invasion occurred.

![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian network model for prognostic factors.

Follow-up. Survival time was calculated as time from surgery until patient death, when the patient was lost to follow-up, or to the end of the follow-up period for patients who remained alive when the study ended in October 2014. The follow-up interval was 6 months. Overall survival (OS) was calculated using all 438 cases within the dataset. Follow-up studies identified death in $61.9 \%$ of patients (271), while $16.4 \%$ of patients (72) were lost to follow-up. The remaining $21.7 \%$ of patients (95) remained in stable condition in October 2014.

Bayesian network. BN is recommended as a comprehensive method of indicating relationships between variables in medical domains when conditions of causality and conditional independence are involved ${ }^{22}$. Formally, a BN includes nodes, edges, and conditional probability. The nodes represent random variables. Each edge represents the cause-and-effect relationship between two nodes. The conditional probability table will quantitatively express the interdependence between nodes.

Through the application of the Bayes theorem, BN is used to obtain the probabilities of unknown variables from known evidence and probabilistic relationships. Duda and Hart put forward a form of Naïve Bayes classifier (NB) based on Bayes formula in 1973. In the NB model, all attributes are conditionally independent to the class variable. Friedman et al. ${ }^{23}$ proposed a tree augmented naïve Bayes (TAN) method which reduces the hypothesis of any attribute that is independent another in the NB classifier based on the dependent relationship of the attributes. Recently, Udelnowet al. ${ }^{24}$ introduced the BN for cancer to predict outcome following multi-organ resection. Si et al. ${ }^{25}$ established a breast cancer diagnosis model to identify tumour markers based on BN using a real-world database.

Prognostic model based on Bayesian network. A total of 366 individuals whose survival state was 0 or 1 , and these patients were used to establish and test the BN model. First, the survival state was excluded from 438 original dataset as survival time was the predictive variable. Next, because BN can only deal with discrete variables, continuous prognostic factors were converted into discrete values on the basis of data features and medical advice. Age was divided into three intervals of $29-50,51-70$, and $71-86$ years. Surgical time was divided into two intervals of $\leq 3$ and $>3$ hours based on medical suggestion. Survival time was divided into two intervals of $\leq 6$ and $>6$ months according to the median survival time of 5.7 months.

To establish the BN model and test its performance, the dataset of 366 patients with GBC was stochastically divided into two cohorts using the rand function in Microsoft Excel. Two-thirds (244) of the patients formed the training dataset (Supplementary Table S2) to establish the model and the remaining 122 individuals (Supplementary Table S3) were considered as the testing dataset to test the model.

In the datasets, survival time was set as the target variable to be predicted, while other factors were considered as attribute variables that affected the state of the target variable. Then the prognostic BN model was established using the TAN algorithm implemented automatically by BayesiaLab. The TAN algorithm ${ }^{23}$ includes four steps: (1) Compute the mutual information function between variables, (2) Build a complete undirected graph, (3) Build a maximum weighted spanning tree, (4) Transform the resulting undirected tree to a directed one by choosing a root variable and setting the direction of all edges to be outward from it. The cause-and-effect relationships among these attribute variables are shown in Fig. 3.

Confusion matrix and ROC curve. Confusion matrix is a tool used to evaluate the credibility of a prognostic classification model. The columns represent the actual condition, while the rows represent the predicted

results of the classifier. True positive (TP) and true negative (TN) values describe correctly-classified instances. Meanwhile, false positive (FP) totals the negative instances misclassified as positive, and false negative (FN) totals the quantity of positive instances misclassified as negative.

Model reliability is defined as the values along the major diagonal of the total instances. Meanwhile, partial reliabilities are calculated by $\mathrm{TP} /(\mathrm{TP}+\mathrm{FP}), \mathrm{FP} /(\mathrm{TP}+\mathrm{FP}), \mathrm{FN} /(\mathrm{TN}+\mathrm{FN})$, and $\mathrm{TN} /(\mathrm{TN}+\mathrm{FN})$.

Model accuracy is defined by the following equation.

$$
\text { Accuracy }=\frac{\mathrm{TP}+\mathrm{TN}}{\mathrm{TP}+\mathrm{FP}+\mathrm{TN}+\mathrm{FN}}
$$

However, accuracy may sometimes not be the appropriate measure when the number of negative and positive cases varies widely. Considering this condition, the ROC curve and the AUC were calculated to measure the overall performance of the classification model.

The TPR of the classifier is estimated as $\mathrm{TP} /(\mathrm{TP}+\mathrm{FN})$. The FPR of the classifier is estimated as $\mathrm{FP} /(\mathrm{TN}+\mathrm{FP})^{26}$. ROC graphs are two-dimensional graphs in which TPR is plotted on the $Y$ axis and FPR is plotted on the $X$ axis. For the ROC curve, if the curve approaches the counter-diagonal line, the attribute variables have few judgment values for the target variable. Contrastingly, if the curve is far from the line, the attribute variables will have great value for the target variable.

Importance measures. The concept of importance measures was first introduced by Birnbaum ${ }^{27}$ to quantify the contribution of individual components to total system performance. Nowadays, importance measures are widely used to identify the key factors within an engineering system ${ }^{14,28}$. So we applied some importance measures to evaluate the influence of covariates on survival from different aspects and compared the results with the traditional Cox regression analysis.

The composite importance measures (CIM) ${ }^{29}$ was applied to calculate the importance of factors affecting the survival time of patients with GBC. The CIM is extended from different aspects to comprehensively evaluate the roles of different factors.

The CIM generalization for Birnbaum importance (MBM) can be expressed as

$$
\mathrm{MBM}_{\mathrm{V}_{\mathrm{i}}}^{\mathrm{S}}=\frac{1}{\omega_{\mathrm{i}}-1} \sum_{\mathrm{j}=1}^{\omega_{\mathrm{i}}}\left|\mathrm{P}(\mathrm{~S}=0 \mid \mathrm{V}_{\mathrm{i}}=\mathrm{j})-\mathrm{P}(\mathrm{~S}=0)\right|
$$

where $S$ represents the survival time, $\mathrm{P}(\mathrm{S}=0)$ represents the prior probability of survival time, $\mathrm{V}_{\mathrm{i}}$ represents the covariates with $\omega_{\mathrm{i}}$ candidate states $\left\{1, \ldots, \mathrm{j}, \ldots, \omega_{\mathrm{i}}\right\}$ which is also called prognostic factors, the $\mathrm{p}(\mathrm{S}=0 \mid \mathrm{V}_{\mathrm{i}}=\mathrm{j})$ represents the posterior probability which reflect the change of survival time under the change of covariates $\mathrm{V}_{\mathrm{i}}$ state. So, the influence of prognostic factors on survival time is determined by this equation.

The CIM generalization for reliability achievement worth (MRAW) was calculated as follow:

$$
\mathrm{MRAW}_{\mathrm{i}}=1+\frac{1}{\omega_{\mathrm{i}}-1} \sum_{\mathrm{j}=1}^{\omega_{\mathrm{i}}} \max \left(0, \beta_{\mathrm{ij}}\right)=1+\frac{1}{\omega_{\mathrm{i}}-1} \sum_{\mathrm{j}=1}^{\omega_{\mathrm{i}}} \max \left(0, \frac{\mathrm{P}(S=0 \mid \mathrm{V}_{\mathrm{i}}=\mathrm{j})-\mathrm{P}(\mathrm{~S}=0)}{\mathrm{P}(\mathrm{~S}=0)}\right)
$$

The CIM generalization for Fussell-Vesely importance (MFV) was expressed as follows:

$$
\mathrm{MFV}_{\mathrm{i}}=\frac{1}{\omega_{\mathrm{i}}-1} \sum_{\mathrm{j}=1}^{\omega_{\mathrm{i}}} \max \left(0,-\beta_{\mathrm{ij}}\right)=\frac{1}{\omega_{\mathrm{i}}-1} \sum_{\mathrm{j}=1}^{\omega_{\mathrm{i}}} \max \left(0, \frac{\mathrm{P}(\mathrm{~S}=0)-\mathrm{P}(S=0 \mid V_{i}=\mathrm{j})}{\mathrm{P}(\mathrm{~S}=0)}\right)
$$

The CIM generalization for reliability reduction worth (MRRW) was calculated as follow:

$$
\mathrm{MRRW}_{\mathrm{i}}=\frac{1}{1-\mathrm{MFV}_{\mathrm{i}}}
$$

The CIM generalization for mean absolute deviation (MAD) was calculated as follow:

$$
\mathrm{MAD}_{\mathrm{i}}=\sum_{\mathrm{j}} \mathrm{P}_{\mathrm{ij}}\left|\mathrm{P}(\mathrm{~S}=0 \mid \mathrm{V}_{\mathrm{i}}=\mathrm{j})-\mathrm{P}(\mathrm{~S}=0)\right|
$$

The CIM generalization for mean multi-state reliability achievement worth (MMAW) was calculated as follow:

$$
\mathrm{MMAW}_{\mathrm{i}}=1+\sum_{\mathrm{j}} \mathrm{P}_{\mathrm{ij}} \max \left(0, \beta_{\mathrm{ij}}\right)
$$

The CIM generalization for mean multi-state Fussell-Vesely (MMFV) was calculated as follow:

$$
\mathrm{MMFV}_{\mathrm{i}}=\sum_{\mathrm{j}} \mathrm{P}_{\mathrm{ij}} \max \left(0,-\beta_{\mathrm{ij}}\right)
$$

Statistical analysis. SPSS 13.0 for Windows (SPSS Inc., Chicago, IL, USA) was used for statistical analyses. BayesiaLab (Bayesian Limited Company, France) was used to establish a BN. Microsoft Excel was used to prepare the training and testing datasets. All continuous variables were transformed into discrete variables. Survival rates were calculated according to the Kaplan-Meier method and differences were measured with the Log-rank test.

Moreover, prognostic multivariate analysis was analyzed by Cox regression and importance measures. Statistical significance was set at $\mathrm{P}<0.05$.

Ethics statement. This study was approved by the Ethics Committee of the First Affiliated Hospital of Xi'an Jiaotong University. All patients gave written informed consent to participate. The ethics committee approved this consent procedure. Data did not contain any information that could identify the patients. All methods were performed in accordance with the relevant guidelines and regulations.

## Acknowledgements

The authors gratefully acknowledge the financial supports for this research from the National Natural Science Foundation of China (Nos 71471147, 71271170, 81572420), the Basic Research Project of Natural Science in Shaanxi Province (No. 2015JQ7273), the Key Science and Technology Program of Shaanxi Province (No. 2014K11-03-03-12).

## Author Contributions

C.Z.Q., S.S.B. and G.Z.M. conceived and designed the experiments. G.P. and C.L.L. performed the experiments. G.Z.M., C.C. and C.L.L. analyzed the data. C.Z.Q., G.P., and S.S.B. contributed reagents materials analysis tools. C.Z.Q., S.S.B. and G.Z.M. wrote the paper. G.P., C.C. and C.L.L. reviewed the manuscript. C.C. and C.L.L. conducted statistical analysis.

## Additional Information

Supplementary information accompanies this paper at doi:10.1038/s41598-017-00491-3
Competing Interests: The authors declare that they have no competing interests.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/
(c) The Author(s) 2017