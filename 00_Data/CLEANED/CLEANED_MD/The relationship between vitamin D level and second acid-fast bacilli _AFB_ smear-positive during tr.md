# The relationship between vitamin D level and second acid-fast bacilli (AFB) smear-positive during treatment for TB patients was inferred by Bayesian network 

Xiaoxu Zhang ${ }^{1}$, Yan Zhang ${ }^{1 *}$, Wenjun Xia ${ }^{1 *}$, Yajie Liu ${ }^{2}$, Hongkai Mao ${ }^{1}$, Liangliang Bao ${ }^{1}$, MingQin Cao ${ }^{1 *}$<br>1 Department of Epidemiology and Health Statistics, School of Public Health, Xinjiang Medical University, Urumqi, Xinjiang Uygur Autonomous Region, China, 2 Medical Record Room, Third Affiliated Hospital of Xinjiang Medical University, Urumqi, Xinjiang Uygur Autonomous Region, China<br>$\cdot$ These authors contributed equally to this work.<br>* 602941846@qq.com

## $\triangle$

## OPEN ACCESS

Citation: Zhang X, Zhang Y, Xia W, Liu Y, Mao H, Bao L, et al. (2022) The relationship between vitamin D level and second acid-fast bacilli (AFB) smear-positive during treatment for TB patients was inferred by Bayesian network. PLoS ONE 17(5): e0267917. https://doi.org/10.1371/journal. pone. 0267917

Editor: Frederick Quinn, The University of Georgia, UNITED STATES

Received: December 16, 2021
Accepted: April 18, 2022
Published: May 4, 2022
Copyright: © 2022 Zhang et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: All relevant data are within the manuscript and its Supporting Information files.

Funding: The study was supported by the National Natural Science Foundation of China (Grant number 82060622). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing interests: The authors have declared that no competing interests exist.

## Abstract

## Background

Vitamin D is related to human immunity, so we used Bayesian network model to analyze and infer the relationship between vitamin D level and the acid-fast bacilli (AFB) smear-positive after two months treatment among pulmonary tuberculosis (TB) patients.

## Methods

This is a cross-sectional study. 731 TB patients whose vitamin D level were detected and medical records were collected from December 2019 to December 2020 in XinJiang of China. Logistic regression was used to analyze the influencing factors of second AFB smear-positive. Bayesian network was used to further analyze the causal relationship among vitamin D level and the second AFB smear-positive.

## Results

Baseline AFB smear-positive ( $O R=6.481,95 \% C I: 1.604-26.184$ ), combined cavity ( $O R=$ $3.204,95 \% C I: 1.586-6.472$ ), full supervision ( $O R=8.173,95 \% C I: 1.536-43.492$ ) and full management ( $O R=6.231,95 \% C I: 1.031-37.636$ ) were not only the risk factors and can also be considered as the reasons for second AFB smear-positive in TB patients (Ensemnle $>0.5$ ). There was no causal relationship between vitamin D level and second AFB smearpositive (Ensemnle $=0.0709$ ).

## Conclusions

The risk factors of second AFB smear-positive were baseline AFB smear-positive, combined cavity, full supervision and full management. The vitamin D level in TB patients was not considered as one of the reasons for the AFB smear-positive.

# 1 Background 

Tuberculosis (TB) is still a major health problem in today's world, especially in the developing countries of Asia, Africa and Latin America [1]. In the past twenty years, China has made significant progress in the prevention and treatment of tuberculosis. However, 866,000 people were still suffering from TB and 37,000 died of TB in 2018 [2]. The negative rate of sputum bacteria in TB patients is an important part of TB control project. Studies have shown that sputum culture which is still not negative at the end of 2 months is a predictor of treatment failure and recurrence [3]. There is also evidence that sputum culture conversion rate (SCC) may be an early predictor of successful treatment for multidrug-resistant (MDR-TB) [4, 5]. The acid-fast bacilli (AFB) smear-test result after 2 months treatment (second AFB smear-test) is great significance for the prediction of treatment outcome and evaluation of treatment management [6, 7].

Vitamin $\mathrm{D}_{3}$, also known as cholecalciferol [8] whose main effect is to maintain the function of monocytes and macrophages that play an important role in the pathogenesis related to human innate immunity. Vitamin D works by binding to the nuclear receptors of the affected cells, So the level of vitamin D in the human body will have an impact on the immune status of mycobacterium tuberculosis [9]. At present, the treatment of active tuberculosis is mainly antibacterial treatment, that is, the need for long-term use of high-dose chemotherapy drugs. Patients do not only face risk of drugs toxicity, but also possible drug resistance and high economic cost [10]. Vitamin D has a unique effect on the immune system, which makes it necessary to become an immunomodulatory therapy based on antibacterial treatment to shorten the duration of disease transmission [11], and to prevent the occurrence of drug resistance by shortening the time of chemotherapy. However, the mechanisms involved in the effect of vita$\min \mathrm{D}$ on TB is still unclear. In this paper, the relationship between second AFB smear-positive and vitamin D in TB patients was analyzed and inferred by the Bayesian network which is more sensitive to causality [12].

Bayesian network is a probability graph model proposed by Judea Pearl in 1985, which is an uncertainty processing model that simulates causality in the human reasoning process, and its topological structure is a directed acyclic graph. Each node in the directed acyclic graph represents a random variable, and the directed edge represents the conditional dependence between random variables [13]. Bayesian network model can clearly and intuitively express the interdependence between variables, which is more convenient for us to identify the probability causal dependence and conditional probability independence. Compared with the logistic regression model controlling confounding, Bayesian network can regulate the network through a priori experience, so as to give the objective conditional establishment probability, which makes the judgment more reasonable and accurate [14]. In this study, Bayesian network was used to explore the relationship between vitamin D level and the second AFB smear-positive among TB patients.

## 2 Materials and methods

### 2.1 Study design and ethics

An epidemiological investigation by using a cross-sectional study design (Fig 1). The study plan was approved by the Ethics Committee of Xinjiang Medical University (No. K20191007), and all the participants provided their voluntarily written informed consent before the investigation (Minors obtained the informed consent from their guardians).

### 2.2 Participants

The subjects of this study had been registered with Directly Observed Treatment of Short Course Strategy (DOTS) in Urumqi Center for Disease Control and Prevention (CDC) among

![img-0.jpeg](img-0.jpeg)

Fig 1. Flow chart of implementation process.
https://doi.org/10.1371/journal.pone.0267917.g001

December 2019-December 2020. All the patients were diagnosed, registered and treated by the Urumqi TB prevention and treatment institution. Inclusion criteria: Patients who were on standard TB treatment plan for two months and have completed with informed consent. Exclusion criteria: The main medical records were incomplete. A total of 731 patients have participated in this study.

# 2.3 Basic information collection 

The inclusion and exclusion criteria were strictly observed during the data collection process. The basic medical record information of TB patients is derived from the TB special report information system. It includes basic demographic data such as gender, age, nationality, floating population and source of patients; Treatment related information of patients, such as treatment classification, diagnosis classification, baseline AFB smear-test results, patients with cavity, treatment management. The collected data were consistent with the patient's medical records and registration books. After 2 months of treatment, second AFB smear-test was performed and medical records were recorded.

### 2.4 Vitamin D data collection

After obtaining informed consent, 5 ml peripheral venous blood of patients was extracted by using disposable vacuum anticoagulant blood collection vessel when persons were diagnosed with TB. The serum plasma was separated, and the content of 25 hydroxy vitamin D which the active form of vitamin D that in patients' serum was detected by Enzyme-linked

immunosorbent assay (ELISA). 25-HVD3(25-Hydroxy Vitamin D3) ELISA Kit that Catalog No: E-EL-0015c; Intra-assay Precision (Coefficient of variation, CV):3.27\%; Inter-assay Precision (CV):4.75\%) was used in this study. In the detection of serum vitamin D level in TB patients, whose blood samples with severe hemolysis were excluded. In order to ensure the consistency of inspection results, the detection kit provided by the same company was used and the operation steps were strictly in accordance with the instructions.Serum-25-hydroxyvi-tamin-D of $0-29 \mathrm{ng} / \mathrm{ml}$ were considered as deficient, and $\geq 30 \mathrm{ng} / \mathrm{ml}$ as sufficient $[15,16]$.

# 2.5 Statistical analysis 

Excel was used to capture the data, SPSS version 25.0 (IBM USA) was used for statistical analysis. chi-square test was used for comparison and correlation analysis; non-conditional logistic regression was used for multivariate analysis. Using the backward stepwise regression method, the test level of the included model was 0.05 , and the exclusion standard was 0.10 . The "forestplot" package in R 4.0.3 was used to draw forest map. tetrad 6.9.0 (NIH Big Data to Knowledge (BD2K) Consortium, USA) was used to construct the Bayesian network model and carry out the analysis.

## 3 Results

### 3.1 Second AFB smear-positive status among different TB patients

According to the results of the data analysis (Table 1), 41 (5.6\%) of the 731 TB patients were second AFB smear-positive. Statistically significant differences were found in the detection rate of second AFB smear-positive among patients who differed in terms of their patient source, treatment classification, baseline sputum smear, combined cavity and treatment management $(P<0.05)$.

### 3.2 Logistic regression analysis of second AFB smear-positive

The dependent variable was the result of the second AFB smear-test, and the independent variable was the significant individual factor in the univariate analysis. The independent variables mainly included patient source, treatment classification, baseline sputum smear, cavity and treatment management (Table 2). The results showed that Baseline sputum smear, Cavity, Treatment management could affect the rate of second AFB smear-positive ( $P<0.05$ ). Among them, baseline AFB smear-positive, combined cavity, Full supervision mode and Full management mode were risk factors for second AFB smear-positive (Fig 2).

### 3.3 Second AFB smear-positive of TB patients with different vitamin D levels

There were 316(43.2\%) with vitamin D sufficient and 415 (56.8\%) with vitamin D deficiency among 731 patients. There was significant statistically difference in the rate of second AFB smear-positive among TB patients with different levels of vitamin $\mathrm{D}(P<0.05)$. The rate of second AFB smear-positive in vitamin D sufficient group ( $7.6 \%$ ) was higher than that in vita$\min$ D deficiency group (4.5\%) (Table 3).

### 3.4 Construction of a Bayesian network model for second AFB smearpositive

In this study, tetrad6.9.0 software was used to construct Bayesian network. The influencing factors $(P<0.05)$ of second AFB smear-positive were as follows: baseline sputum smear,

Table 1. Comparison of second AFB smear-positive status among different TB patients.


Patient source: TB patients are classified according to different sources; Track: Under the guidance of CDC, the primary medical institutions should follow up the TB patients who have not visited TB designated institutions or who have close contacts with suspicious symptoms, so that they can go to TB designated medical institutions for treatment; Referral: Refers to the suspected or confirmed TB patients at all levels of medical and health institutions transferred to TB designated medical institutions; Other: Including physical examination and who was close contact inspection. Treatment management: The management of TB patients in China is mainly based on non-hospitalization, including full supervision, intensive supervision, full management and self-medication; Intensive supervision: In the intensive period of treatment, patients were treated with direct supervision chemotherapy every time, and the full management was adopted in the continuous period; Full supervision: In the whole process of tuberculosis treatment, each time the patient takes anti-tuberculous drugs, they are under the direct supervision of medical staff or trained volunteer supervisors; Full management: In the whole process of patient treatment, urge patients to complete the whole course of treatment through various ways and channels. https://doi.org/10.1371/journal.pone.0267917.t001

Table 2. Assignment table of dependent variable and independent variables.


https://doi.org/10.1371/journal.pone.0267917.t002


Fig 2. The result of logistic regression.
https://doi.org/10.1371/journal.pone.0267917.g002
cavity, treatment management mode and vitamin D level of TB patients were used as network nodes to construct Bayesian network model. The definition and assignment of Bayesian network nodes were shown in Table 4. There were three steps to build Bayesian network structure (Fig 3). The data set of model construction was discrete data, PC variants algorithm was used in the whole calculation process, the test method was chi-square test, and the conditional independent test level was alpha $<0.05$.

As shown in Fig 3, Graph A was to explore the initial model from the original data. At this time, the graph had no arrow pointing, and the connection only indicated the correlation between the two variables, so it was necessary to further add constraints to the model; Graph B was the graph that constraints were imposed on the model according to the chronological order of independent variables and calculated the edge probability of each variable (Table 5), where the probability of "Baseline to VitD", "Cavity to VitD", "VitD to Second" three edges were all less than 0.5 , and the vitamin D level of TB patients was less likely to affect the second AFB smear-positive (Ensemnle $=0.0709$ ). It was not considered to be the interpretable cause of second AFB smear-positive; After eliminating the edges with edge probability less than 0.5 , reconstructed the model (Graph C) and calculated the conditional probability of positive in second AFB smear-positive (Fig 4). Baseline AFB smear-positive, combined cavity and different treatment management mode all had a direct impact on the second sputum smear, which was consistent with the logistic regression results, and the logistic regression results were supplemented in more detail through the conditional probability table (Fig 4).

Table 3. Second AFB smear-test results of TB patients with different vitamin D levels.


https://doi.org/10.1371/journal.pone.0267917.t003

Table 4. The definition and assignment table of Bayesian network nodes.


https://doi.org/10.1371/journal.pone.0267917.t004

# 4 Discussion 

Baseline AFB smear-positive patients were more likely to continue to be positive in the second AFB smear-test. The baseline AFB smear-positive patients who carry more Mycobacterium tuberculosis are due to the long delay of treatment time. A retrospective study of 330 patients with drug resistance from Yangon of Burma showed that delayed initiation of treatment was associated with poor treatment outcome. Median treatment-delay times were longer among TB patients with poor outcomes ( 144 days) than those with successful outcomes (102 days). Patients with long treatment delays were significantly different from those with short delays, in terms of having high sputum smear grade, resistance to more than two main drugs (isoniazid and rifampicin), and long culture conversion time [17]. On the other hand, patients with different constitution and related gene expression, such as the presence of susceptibility genes in patients is related to persistent positive sputum smear. A cohort study of Vitamin D
![img-1.jpeg](img-1.jpeg)

Fig 3. Bayesian network model for second AFB smear-positive in TB patients. A: Initial network structure. B: Bayesian network structure after adding constraints according to prior knowledge. C: Trimmed Bayesian network structure.
https://doi.org/10.1371/journal.pone.0267917.g003

Table 5. Edges and edge type probabilities of Bayesian network node.


https://doi.org/10.1371/journal.pone.0267917.t005
receptor (VDR) gene polymorphisms showed that the VDR gene polymorphisms were associated with rate of sputum culture conversion in MDR TB patients [18]. Research shows that patients with the TT TaqI genotype had significantly longer time to sputum culture conversion compared with $T t$ genotype (median 46 days for $T T$ genotype vs. 16 days for $T t$ genotype) [19]. And other report showed that a significantly lower proportion of patients with ApaI aa genotype had converted cultures by 2 months of TB treatment compared to patients with ApaI Aa genotype ( $26 \%$ vs. $51 \%, P=0.03$ ) [20]. In addition, it may be that the baseline AFB smearpositive patients are insensitivity to anti-tuberculosis drugs [21]. And two months of treatment can not completely turn most baseline sputum smear positive patients into negative.

TB patients with cavities are often more severe and have higher mycobacterial load, initial bacterial load is associated with sputum smear delayed conversion to negative at the end of TB
![img-2.jpeg](img-2.jpeg)

Fig 4. Conditional probability table of second AFB smear-positive.
https://doi.org/10.1371/journal.pone.0267917.g004

treatment [22]. A review published of LANCET INFECTIOUS DISEASES in 2020 pointed out: Phagocytes and granulocytes penetrate poorly went into these necrotic areas(cavity), thus creating an immune-sheltered zone of bacterial growth. High oxygen levels within the cavity also provided a rich environment for high rates of bacterial replication leading to a large bacillary burden at the inner edge of the cavity. During cavity formation, both the basement membrane and alveolar architecture were permanently destroyed. Even after successful TB treatment, TB cavities can persist, leading to lifelong pulmonary deficits and recurrent opportunistic infections. All the above reasons lead to the characteristics of cavitary tuberculosis, which is difficult to cure completely and easy to relapse [23]. Many studies have shown that the presence of cavities in chest X-ray films is a risk factor for tuberculosis recurrence. Patients with cavities are more likely to have adverse treatment outcomes than patients without cavities. It had negative implications not only for the patient-associated with poor treatment outcomes, including delayed sputum culture conversion, relapse after treatment, and development of drug resistance, but was also a public health threat, which since cavitation greatly increased the risk of person-to-person transmission [24, 25]. Therefore, it is necessary to improve the early detection rate of TB patients to avoid the deterioration of the disease and the formation of cavities [26]. At the same time, it should be ensured that the cavity disappears at the end of treatment, and regular follow-up should be conducted for patients who still have cavity at the end of treatment.

The different treatment management patterns also had different effects on second AFB smear-test results and treatment outcomes of TB patients [27]. Most countries gave some forms of TB patients support including various treatment supervision options and treatment adherence interventions such as health education, psycho-emotional and socio-economic support [28]. The full supervision mode is suitable for AFB smear-positive patients, new AFB smear-negative patients with miliary cavity and other serious complications. The disease situation of these patients is relatively serious, so the second AFB smear-positive rate is higher. However, the full management refers to the whole process of tuberculosis treatment for patients who have not reached the full supervision or intensive supervision. Through all the comprehensive management methods such as strengthening the propaganda and education of patients, regular outpatient medication, family visits, return visit medication situation, delayed recovery to ensure the regular medication of patients. For the TB patients, regular medication is an important condition to improve the disease and prognosis [29]. TB patients should complete the whole treatment process according to the medical advice and should not interrupt or shorten the medication time and need to take medicine for a long time. Only regular medication on time can ensure the effective dose of the drug concentration in the body and make the drug continue to play its role. However, some of the patients who received the full management stopped treatment by themselves after their symptoms improved significantly, or some of them stopped taking drugs by themselves because of adverse drug reactions and poor economic ability, resulting in a higher rate of the second AFB smear-positive [30, 31]. Patients who received two or more anti TB courses were significantly associated with multidrug-resistant tuberculosis compared with patients receiving an anti TB course. In some instances, individualizing treatment regimens may be necessary [32].

The results of this study do not believe that vitamin D deficiency in TB patients is the cause of AFB smear-positive after 2 months treatment, which is consistent with the results of a metaanalysis from China. The meta-analysis considered that vitamin D supplementation did not shorten the time to sputum culture and smear conversion and did not lead to an increase in the proportion of participants with negative sputum culture [33]. However, there is still no unified statement on the role of vitamin D level of TB patients in TB treatment, and there are many reasons for this situation. The first is the effect of chemotherapy drugs on their own

metabolism during treatment. Such as Rifampicin (RFP) limits the formation of active form of vitamin D in anti-tuberculosis treatment, and Isoniazid (INH) leads to the reduction of corresponding vitamin D metabolites, so that the vitamin D level of patients generally decreases during treatment [34, 35]. In addition, the relationship between vitamin D and the outcome of TB treatment was different in different study populations. A meta-analysis showed that the level of vitamin D had no significant effect on the time of sputum culture transformation in general TB patients, but it played an accelerating role in the sputum culture transformation of MDR-TB patients [36]. Finally, the vitamin D level of TB patients may be affected by genetic factors, such as black Americans had low levels of vitamin D compared with whites [37]. And different combinations of vitamin D levels and genotypes of vitamin D receptor gene polymorphisms have different sputum culture conversion rates in TB patients [38].

# 5 Conclusion 

The risk factors of second AFB smear-positive were baseline AFB smear-positive, combined cavity, full supervision and full management. Inference results based on Bayesian network, the vitamin D level in TB patients was not considered as one of the reasons for the AFB smear-positive. Baseline AFB smear-positive as well as cavity caused by delayed treatment should be avoided and the medication compliance education of patients in the full management should be strengthen in the process of TB prevention and control.

## 6 Limitation

First, the research object of this study is only from tuberculosis patients in Urumqi, so it is not clear whether the research results are applicable to other regions and countries. Secondly, AFB smear-test can be classified data. Due to the limitation of conditions, it is regarded as secondary classification data in this study. In the follow-up research, we should try to ensure the originality and comprehensiveness of AFB-test result. Third, this study adopts cross-sectional design, which can only use statistical techniques to infer the preliminary etiological clues from the probability rather than identify a clear causal relationship. It is suggested that the follow-up study can design community intervention trials, and further clarify the role of vitamin D in the treatment of tuberculosis.

## Supporting information

## S1 Data.

(XLS)

## Acknowledgments

We thank all the CDC doctors, researchers, nurses help in conducting survey. We also thank all patients who participated in this study.

## Author Contributions

Conceptualization: Xiaoxu Zhang, MingQin Cao.
Data curation: Yajie Liu, Hongkai Mao, Liangliang Bao.
Formal analysis: Xiaoxu Zhang, Yan Zhang, Wenjun Xia.
Funding acquisition: MingQin Cao.
Investigation: Yajie Liu, Hongkai Mao, Liangliang Bao.

Methodology: Xiaoxu Zhang, MingQin Cao.
Project administration: MingQin Cao.
Resources: MingQin Cao.
Software: Xiaoxu Zhang, Yan Zhang, Wenjun Xia.
Supervision: MingQin Cao.
Validation: Xiaoxu Zhang, MingQin Cao.
Visualization: Xiaoxu Zhang.
Writing - original draft: Xiaoxu Zhang.
Writing - review \& editing: Xiaoxu Zhang, MingQin Cao.
