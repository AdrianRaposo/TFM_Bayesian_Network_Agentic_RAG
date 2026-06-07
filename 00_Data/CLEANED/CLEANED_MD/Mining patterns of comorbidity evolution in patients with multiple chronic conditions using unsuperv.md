# Mining patterns of comorbidity evolution in patients with multiple chronic conditions using unsupervised multi-level temporal Bayesian network 

Syed Hasib Akhter Faruqui ${ }^{1}$, Adel Alaeddini ${ }^{1 *}$, Carlos A. Jaramillo ${ }^{2}$, Jennifer S. Potter ${ }^{3}$, Mary Jo Pugh*<br>1 Department of Mechanical Engineering, The University of Texas at San Antonio, San Antonio, TX, United States of America, 2 South Texas Veterans Health Care System, San Antonio, TX, United States of America, 3 Department of Psychiatry, University of Texas Health Science Center at San Antonio, San Antonio, TX, United States of America, 4 VA Salt Lake City Health Care System, Salt Lake City, UT, United States of America<br>* adel.alaeddini@utsa.edu

## $\triangle$ OPEN ACCESS

Citation: Faruqui SHA, Alaeddini A, Jaramillo CA, Potter JS, Pugh MJ (2018) Mining patterns of comorbidity evolution in patients with multiple chronic conditions using unsupervised multi-level temporal Bayesian network. PLoS ONE 13(7): e0199768. https://doi.org/10.1371/journal. pone. 0199768

Editor: Mark Webber Miller, Boston University \& VA Boston Healthcare System, UNITED STATES

Received: January 25, 2018
Accepted: June 13, 2018
Published: July 12, 2018
Copyright: © 2018 Faruqui et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: The dataset underlying our study is a third-party dataset from VA, which is not owned or collected by the authors. The dataset was provided to our team after approval by the South Texas Veterans Health Care System Research and Development committee in accordance with VA data security regulations. For others to access these data, the same process is required based on VA Data Security and privacy regulations. The authors did not have any special access privileges that others would not have. To

## Abstract

Over the past few decades, the rise of multiple chronic conditions has become a major concern for clinicians. However, it is still not known precisely how multiple chronic conditions emerge among patients. We propose an unsupervised multi-level temporal Bayesian network to provide a compact representation of the relationship among emergence of multiple chronic conditions and patient level risk factors over time. To improve the efficiency of the learning process, we use an extension of maximum weight spanning tree algorithm and greedy search algorithm to study the structure of the proposed network in three stages, starting with learning the inter-relationship of comorbidities within each year, followed by learning the intra-relationship of comorbidity emergence between consecutive years, and finally learning the hierarchical relationship of comorbidities and patient level risk factors. We also use a longest path algorithm to identify the most likely sequence of comorbidities emerging from and/or leading to specific chronic conditions. Using a de-identified dataset of more than 250,000 patients receiving care from the U.S. Department of Veterans Affairs for a period of five years, we compare the performance of the proposed unsupervised Bayesian network in comparison with those of Bayesian networks developed based on supervised and semisupervised learning approaches, as well as multivariate probit regression, multinomial logistic regression, and latent regression Markov mixture clustering focusing on traumatic brain injury (TBI), post-traumatic stress disorder (PTSD), depression (Depr), substance abuse (SuAb), and back pain (BaPa). Our findings show that the unsupervised approach has noticeably accurate predictive performance that is comparable to the best performing semi-supervised and the second-best performing supervised approaches. These findings also revealed that the unsupervised approach has improved performance over multivariate probit regression, multinomial logistic regression, and latent regression Markov mixture clustering.

inquire about and initiate the process of accessing the date, a request should be sent to the following point of contact: VA Information Resource Center (VIReC) Email: vireciliva.gov Building 18 Hines VA Hospital (151V) 5000 S. 5th Avenue Hines, IL 60141-3030 708-202-2413 708-202-2415 (fax).

Funding: This work was supported by National Institutes of Health (NIH/NIGMA), Grant number: 15C2GM118266-01, Grant Title: A Novel Probabilistic Methodology for Prediction of Emerging Diseases in Patients with Multiple Chronic Conditions, PI: Alaeddini; VA Health Services Research and Development Service, Grant Number: 101 HX000329-05, Grant Title: Identifying and Validating Complex Comorbidity Clusters in OEF-OIF Veterans, PI: Pugh; VA Clinical Services Research and Development Service, Grant Number: 101 CX001246, Grant Title: Chronic Effects of Neurotrauma Epidemiology Study, Investigator: Pugh; and National Institutes of Health (NIH/NIDA), Grant Number: 5UG1DA020024-13, Grant Title: Clinical trials network Texas node, Investigator: Potter. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing interests: The authors have declared that no competing interests exist.

## Introduction

For nearly a decade, clinicians caring for Veterans with traumatic brain injury (TBI) have described multimorbidity among those with persistent post-concussion symptoms and other commonly occurring comorbidities. This constellation was first described as the Polytrauma Clinical Triad (PCT), and included TBI, post-traumatic stress disorder (PTSD) and pain [1]. At the national level, approximately six percent of Post-9/11 Veterans were diagnosed with TBI, PTSD and pain in 2009 [2]. The number of Veterans receiving care for PCT were increased by a total of $144 \%$ over the triennium, and the health care cost that was four times higher than similar Post-9/11 Veterans without TBI [3]. PCT were also associated with sleep disturbance [4], suicide [5]. Miller et al. [6] showed that service members with mild TBI are at increased risk for addiction-related disorders including alcohol and nicotine. They also observed that mild TBI is distinguished from moderate to severe TBI in terms of timing of the risk, indicating a need for rigorous TBI clinical screening. Corrigan et al. [7] identified seven clusters of lifetime history of TBI for substance abuse problem. These clusters were characterized by injury severity, age of injury occurrence, and periods of repeated TBI. The clusters differed in their contribution to predict future consequences, which suggests an underlying complexity of the medical history that results in substance abuse. Adams et al. [8] conducted a path based analysis to examine the association of binge alcohol drinking with TBI and PTSD. The study sample included 6,824 military personnel and revealed that PTSD and a prior history of TBI both had a direct effect on binge drinking.

Lippa et al. [9] used factor analysis to identify patterns of comorbidity in a sample of 255 previously deployed Post-9/11 service members and veterans who participated in a structured clinical interview. They found that over $90 \%$ of the patients had psychiatric conditions, and approximately half had three or more conditions. They also identified four clinically relevant psychiatric and behavioral factors, including deployment trauma factor, somatic factor, anxiety factor, and substance abuse factor, that account for $76.9 \%$ of the variance in the data. They concluded that depression, PTSD, and a history of military mild TBI can comprise a harmful combination associated with high risk for substantial disability. Using a broader range of comorbid conditions, Pugh, et al. [10] used latent class analysis (LCA) to identify longitudinal comorbidity phenotypes in previously deployed Post-9/11 Veterans based on diagnoses received during the first three years of care in the Veterans Health Administration (VA). In analyses stratified by sex, they found five phenotypes that were consistent in men and women: Healthy, Chronic Disease, Pain, Mental Health, and Polytrauma Clinical Triad (Mental Health, TBI and Pain). These subgroups demonstrated increasing likelihood of having relevant diagnoses over time. Pugh et al. [11] showed that these comorbidity phenotypes are associated with measures of community reintegration, with individuals in the PCT and Mental Health groups being significantly more likely to report difficulty in the transition from military to civilian life, lower levels of social support, and higher rates of unemployment. Alaeddini, et al. [12] developed a Latent Regression Markov Mixture Clustering (LRMCL) algorithm to identify major transitions of four MCC that include hypertension (HTN), depression, PTSD, and back pain in a cohort of 601,805 Iraq and Afghanistan war Veterans (IAVs). The LRMCL algorithm was also able to predict the exact status of comorbidities about $48 \%$ of the time.

Zador et al. [13] used logistic regression to predict TBI outcome in the dataset of the corticosteroid randomization after significant head injury (CRASH), where they utilized a Bayesian network to assess the dependencies between predictors of the model. This gave a strong insight in formalizing clinical intuition for the demographic predictors being used. Zador et al. [14]

employed a similar approach based on Bayesian networks to visualize the probabilistic associations between outcome predictors of acute aneurysmal subarachnoid hemorrhage. Cai et al. [15] also established a Bayesian network using a tree-augmented naïve Bayes algorithm to mine relationships between factors influencing hepatocellular carcinoma after hepatectomy. While Bayesian networks can be used to predict disease prevalence, it is also, feasible to use them for providing accurate personalized survival estimates and treatment selection for patient specific variables. Sesen et al. [16] used such a Bayesian network model to create a decision support system for lung cancer care. Forsberg et al. [17] developed and trained a machinelearned Bayesian belief network model to estimate survival time in patients with operable skeletal metastases using candidate features based on historical data. Stojadinovic et al. [18] also used a machine-learned Bayesian belief network to provide clinical decision support in estimating overall survival among colon cancer patients based on a set of prognostic factors at 12-, 24-, 36-, and 60-month post-treatment follow-up. Moreover, Bayesian Networks can be used to study the evolutionary course of multiple disorders. Lappenschaar et al. [19] used a large dataset to develop a multilevel temporal Bayesian networks to model the progression of six chronic cardiovascular conditions.

While interesting, most of these studies have been cross-sectional or focus on a relatively short period of time. Moreover, while these methods describe general comorbidity phenotypes, they do not provide insight into the impact of TBI and comorbid conditions on specific adverse outcomes. In this paper, we develop an unsupervised Multi-level Temporal Bayesian Network (MTBN) from big data to identify the relationships among emergence of five deployment related conditions (TBI, PTSD, Depr, SuAb, and BaPa), and patient level risk factors (race, gender, age, education and marital status) over time. We also use a Longest Path Algorithm (LPA) to identify the most probable sequence of comorbidities emerging from and/or leading to specific chronic conditions. Moreover, we demonstrate the performance of the proposed unsupervised MTBN in comparison with the semi-supervised and supervised MTBNs, as well three baseline methods in the literature, including multivariate probit regression [20], multinomial logistic regression [21], and Latent Regression Markov Mixture Clustering (LRMCL) [12].

# Methods 

## Study population

The proposed study uses de-identified data from a large national cohort of patients $(\mathrm{N}=608,503)$ who were deployed in support of the wars in Afghanistan and Iraq and who entered care in the Department of Veterans Affairs between 2002 and 2011 and who received care at least once a year in three different years between 2002-2015. For the purpose of this analysis, only patients with care each year for the first five consecutive years after entering VA care were included $(\mathrm{n}=257,633)$. Dropout may result from not requiring care, dropping out of VA care, or death.

Individuals in the cohort were identified using the roster of veterans who had been previously deployed in support of Operations Enduring Freedom, Iraqi Freedom, and New Dawn (OEF/OIF/OND roster). The inpatient and outpatient data were then obtained from the VA national databases in Austin Texas. Data included ICD-9-CM diagnosis codes documented during the course of VA care, during each inpatient or outpatient encounter.

This study received institutional review board approval from the University of Texas Health Science Center at San Antonio and the Bedford VA Hospital with a waiver of informed consent.

# Measures 

Diagnosed health conditions. We used ICD-9-CM codes from inpatient and outpatient data (excluding ancillary and telephone care) to identify Traumatic brain injury (TBI), Post Traumatic Disorder (PTSD), Depression (Depr), substance abuse (SuAb), Back pain (BaPa) using validated published algorithms [22]. PTSD, SA, and BP required two diagnoses at least seven days apart, while TBI, which is an acute injury required only a single diagnosis. Each condition was coded as " 0 " or " 1 " for each year of care, with 1 indicating a diagnosis for that condition regardless of the number of instances for which each condition was diagnosed (See S1 Table for ICD-9 Codes for the considered conditions in this manuscript). Table 1 illustrates the prevalence of the five comorbidities in the final dataset based on the first five years of care in the VA.

Demographic characteristics. Sociodemographic characteristics included age at VA entry, sex, race/ethnicity and education. Age was identified during the first year of VA care. Based on our prior work, we categorized age as 18-30, 31-40, 41-50, and 51 and older. Sex, race/ethnicity (White, African American, Hispanic, Asian/Pacific Islander, Native American, unknown) and education (less than high school, high school graduate, some college, college graduate, post-college education) at the time of leaving the military were obtained from the OEF/OIF/OND Roster; missing values for race and sex were supplemented from VA data. Marital status was obtained from VA data (Table 2).

## Bayesian networks

In this section, we describe the proposed unsupervised approach along with the supervised and semi-supervised approaches for structure learning in Bayesian networks to mine patterns of comorbidity evolution in patients with Multiple Chronic Conditions (MCC). We also present a longest path algorithm to identify the most likely path to evolution of a chronic condition. This is one of the first studies to demonstrate the inherent association among chronic conditions and demographics for evolution of new conditions. Fig 1 shows the general scheme of the proposed approach.

Bayesian network [23-27] is a probabilistic graphical model that represents a set of variables and their conditional dependencies via a directed acyclic graph (DAG). In this study two sets of low-level and high-level variables are considered: (1) low level binary variables representing having or not having a chronic condition, namely TBI, PTSD, BaPa, Depr, and SuAb, and (2) high-level discrete variables representing demographic factors, namely, race, gender, marital status, age group and education. When the structure of a Bayesian network (DAG) in known, the joint probability distribution over the random variables can be derived according to the dependencies represented in the graph:

$$
P\left(X_{1}, \ldots . ., X_{n}\right)=\prod_{i=1}^{n} P\left(X=x_{k}^{t} \mid P a\left(X=x_{k}^{t}\right)\right)
$$

Eq (1) can be used to calculate the likelihood and estimate the conditional probabilities of the Bayesian network [27-31], having a dataset of variable observations, i.e. MCC occurrences.

Structural learning. In most real-world cases, such as multiple chronic condition studies, the Bayesian network structure (DAG) is partially or completely unknown and should be learned along with the conditional probabilities. Generally, the Bayesian network structure can be learned using: (1) Unsupervised learning algorithms, including score-based and constraintbased algorithms, (2) Supervised learning algorithms, where expert knowledge provides the

Table 1. The prevalence of the five comorbidities in the final dataset based on the five years of care.


(Continued)

Table 1. (Continued)


https://doi.org/10.1371/journal.pone.0199768.t001

Table 2. Demographics of the patients included in the study.

Rest | Unknown | $<$ High
School | High
School | Some
College | College
Graduate  |

https://doi.org/10.1371/journal.pone.0199768.t002

DAG, and (3) semi-supervised methods, which combine unsupervised and supervised learning algorithms.

Unsupervised learning algorithm One efficient way of unsupervised structure learning algorithm begins with finding the Maximum Weight Spanning Tree (MWST) for the given data using the mutual information to provides an initial variables (node) ordering in $O\left(n^{2}\right)$ steps [32]. Next, a greedy search method such as K2 Algorithm [33] is used to incrementally form the DAG structure based on maximum likelihood in $O\left(n^{3}\right)$ steps.

![img-0.jpeg](img-0.jpeg)

Fig 1. Framework. General Scheme of the proposed method.
https://doi.org/10.1371/journal.pone.0199768.g001

Temporal learning Unsupervised learning algorithm can be applied to temporal dataset as well. However, when the number of time slices and consequently variables increase, as in MCC evolution over time, the computational complexity of MWST algorithm degrades considerably. Therefore, to improve the efficiency of the learning process, we apply the MWST algorithm to each time slice separately, and then integrate the result into a single topological ordering based on their time slice (See Fig 2).

Supervised learning algorithm (expert knowledge) It uses the expert opinion, i.e. physicians input, and/or earlier related studies to identify the complete network structure
![img-1.jpeg](img-1.jpeg)

Fig 2. Unsupervised method. Implementation of the Proposed Algorithm (Unsupervised).
https://doi.org/10.1371/journal.pone.0199768.g002

![img-2.jpeg](img-2.jpeg)

Fig 3. Supervised method. The network structure inferred from literature review.
https://doi.org/10.1371/journal.pone.0199768.g003
(e.g. Fig 3). Then the joint probability distributions can be calculated using either Maximum Likelihood Estimation (MLE) [27], Bayesian Estimation [28], or Expectation Maximization (EM) Algorithm (for incomplete data) [30]. In our study we use the literature review to identify the complete network structure, which is assumed to be consistent across different time slices. We also used Maximum Likelihood Parameter Estimation algorithm to calculate the conditional probabilities based in the study dataset.

Semi-supervised method It's the mixture of the previous two methods. First, the initial ordering of MCC nodes are derived from the expert opinion and/or literature reviews. Next, the ordered nodes are passed through K2 algorithm to get the final structure of the network and conditional probabilities.

Inclusion of hierarchical level To improve the predictive performance of the Bayesian network, demographic variable such as race, sex, age group and education can be added to the DAG as higher-level variables. For this purpose, we simply connect all demographic variables to all the condition with the direction of the connections is constrained to be from demographics to chronic conditions. Meanwhile, we assume no dependence among demographic variables themselves and therefore avoiding any connection between demographics. The probability of the conditional dependencies between the demographic variables and the chronic conditions can be learned in the same we as the other conditional dependencies in the network.

Longest path algorithm (LPA). Having the Bayesian network structure and probability of conditional dependencies estimated, various queries can be answered to support better decision making for practitioners to slow down or stop the progression of targeted conditions. Among the most important ones is identifying the most likely sequence of comorbidities emerging from and/or leading to specific chronic conditions, i.e. the most likely path between TBI in year 1 and substance abuse in year 5 . Such query can be effectively answered by treating the preexisting condition, i.e. TBI, as the source node, and the target condition, i.e. SuAb, as

![img-3.jpeg](img-3.jpeg)

Fig 4. Unsupervised network. Learned BN structure from the proposed method (Unsupervised Method).
https://doi.org/10.1371/journal.pone.0199768.g004
the sink node, and finding the longest path between them on the graph. When only the initial chronic condition (source node), or the terminal chronic condition (sink node) is of interest, i.e. finding the most likely path (from any comorbidity) to substance abuse in year 5, we can introduce a dummy source node to the MTBN and connect it to all of the conditions in the first year, and find the longest path between the dummy source node and the sink node, i.e. SuAb in year 5, on the graph.

All the algorithms discussed in this section are included in S1 File.

# Results 

## Learned bayesian structure

Fig 4 illustrates the proposed unsupervised Multi-level Temporal Bayesian network (MTBN). The illustrated MTBN is consisted of five-time slices, one for each year of care, five demographic variables which enable the practitioners to customize the network to specific patients, and the probabilistic dependencies among five prevalent chronic conditions in the dataset (See S1 Fig for the supervised and semi-supervised MTBNs).

Comparing the unsupervised MTBN (Fig 4) with the supervised and semi-supervised MTBN networks, we found a significant degree of similarity among the conditional dependencies as shown in Table 3.

## Performance comparisons

We use the Area Under the Curve (AUC) of the Receiver Operating Characteristic (ROC) function [34] based on 10 -fold cross validation to compare the performance of the unsupervised MTBN with the semi-supervised and supervised methods, as well as three baseline methods in the literature, including multivariate probit regression [20], multinomial logistic regression [21], and Latent Regression Markov Mixture Clustering (LRMCL) [12].

Table 3. Similarity between the learned matrices.


https://doi.org/10.1371/journal.pone.0199768.t003

Table 4 illustrates the AUC performance of the competing methods for predicting future comorbidities, given comorbidity information of past years. For example, the first block of rows in Table 4 shows the prediction accuracy of year-2 to year 5 comorbidities, given year-1 comorbidities. Likewise, the second block of rows in Table 4 illustrates the prediction accuracy of year-3 to year 5 comorbidities, given year-1 and year-2 comorbidities. Except for the LRMCL method, which can only incorporate the comorbidity information of the immediate preceding year [12] (See first block of rows in Table 4), for all other competing methods, we collect the information of AUC performance for various years of given comorbidities, namely year 1 to year 4 . As shown in Table 4, the MTBNs provides the best performance across all competing methods, followed by the probit and logistic regression and finally LRMCL. Among MTBNs, the semi-supervised learning method demonstrates the overall best performance followed by supervised learning, and unsupervised learning. Meanwhile, the unsupervised learning method which uses no expert information or supervision for structure learning, provides a comparable performance to the best performing methods. Moreover, for all of the comparing methods, as the amount of provided information (comorbidity information of past years) increases, the accuracy of the predictions increases.

To demonstrate the predicted frequency of each comorbid condition, given the information of the past years, Table 5 illustrates an example of the unsupervised, semi-supervised, and supervised MTBNs' conditional probabilities of the comorbidities in year two, given year one data, for a sample patients with the following risk factors, gender (male), marital status (unmarried), education (less than high school), race (white), and age (18-30). For the economy of space, we use the following coding system to represent the comorbidities in the table: nocomorbidity (" 0 "), TBI (" 1 "), PTSD (" 2 "), BaPa (" 3 "), SuAb (" 4 "), and Depr (" 5 ") (See S2 Table for the detail description). Also, to highlight the significance of the transition probabilities among comorbidities, higher probabilities are highlighted with darker color. To interpret the table, the numbers on the main diagonal show the probabilities of retaining the conditions, the numbers above the main diagonal present the probabilities of adding new conditions, and the numbers below the diagonal represent the probabilities of remission from one or more of the existing conditions from year one to year two. As illustrated in the table, there is a considerable similarity between the conditional probabilities and patterns of high transition probabilities of the unsupervised, semi-supervised, and supervised methods. Meanwhile, the most significant pattern of the transition probabilities across all three MTBNs is retention of the existing comorbidities, which is intuitive. The other major pattern is remission from existing conditions (numbers below the main diagonal) which is more likely to happen for small number of comorbidities, i.e. one of two.

Also to demonstrate the clinical utility of the proposed method, Table 6 provides the confusion matrices of the unsupervised, semi-supervised, and supervised MTBNs for predicting the individual comorbid conditions that may occur in year 5, given years 1 to 4 data, based on a $50 \%$ threshold. As expected from earlier results, all three structure learning methods show comparable confusion matrices, while the semi-supervised methods provides the most competitive performance. Meanwhile, the true negative rate (specificity) of all MTBNs are

Table 4. The Area Under the Curve (AUC) performance of the competing methods for predicting future comorbidities, given comorbidity information of past years.


Table 5. Conditional probabilities of the comorbidities in year two, given year one data, for a sample patients with the following risk factors, gender (male), marital status (unmarried), education (less than high school), race (white), and age (18-30).


(Continued)

# Table 5. (Continued)


(Continued)

PLOS ONE | https://doi.org/10.1371/journal.pone.0199768 July 12, 2018 14/22


https://doi.org/10.1371/journal.pone.0199768.t005

Table 6. The confusion matrices of the unsupervised, semi-supervised, and supervised MTBNs for prediction of comorbidities of year 5, given year 1, 2, 3, 4 data, based on a 50% threshold.





Table 6. (Continued)
![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

Fig 5. Longest path. The longest paths in the MTBNs. From left (a) Unsupervised Network (b) Semi-supervised Network and (c) Supervised Network.
https://doi.org/10.1371/journal.pone.0199768.g005
acceptably high, and consistent across the five comorbid conditions. But, the true positive rate (recall) of the MTBNs fluctuates in predicting new cases of TBI.

# Longest path algorithm (LPA) 

Here, we use the longest path algorithm, a variation of the shortest path algorithm, to find the most likely path between the emergence of substance abuse (SuAb) in year 1, and the SUD in year 5 for the unsupervised, semi-supervised, and supervised MTBNs (Fig 5). The analysis of the longest path shows the sequence of conditions that are caused by and/or correlated with substance abuse problem at the base year and leading to diagnosis of SuAb in year 5. From the Figure, it can be seen that the most likely paths from all MTBNs, include recurrent SuAb across different years, which shows the previous history of SuAb is a major predictor of SuAb in the future. Our follow up analysis verifies the suggested sequence of SuAb in the longest path, by showing $10 \%$ of the patients with SuAb in year 5 going through it. Meanwhile, The semisupervised and supervised Bayesian networks show additional conditions on their longest path, suggesting possible correlations between PTSD and Depr, and the continuation of substance abuse problem.

## Discussion

Clinical data are often stored as a hierarchical time series in typically large and extensive datasets. Analysis of these raw datasets may give an insight into the evolution of diseases and information about the co-occurrence of chronic conditions. This study describes an unsupervised structure learning approach for constructing Multilevel Temporal Bayesian Networks (MTBN) for mining patterns of comorbidity evolution in a large population of patients in the VA over time. Comparing the learned structure from the proposed approach with those of semi-supervised, and supervised structure learning approaches, demonstrates a significant degree of similarity between the unsupervised approach and the other learning approaches that utilize expert input. The results also show that the unsupervised approach has considerable predictive performance, which is comparable to the supervised and semi-supervised approaches, and better than multivariate probit regression, multinomial logistic regression, and Latent Regression Markov Mixture Clustering (LRMCL). Thus, in the absence of a medical expert, or sufficient literature, the unsupervised model can perform close to that of a semi or fully supervised model. The unsupervised model can also be used to generate strong

hypotheses for the dependencies among chronic conditions to be tested by other approaches including clinical investigation.

We also present a Longest Path Algorithm (LPA) to mine major trajectories of comorbidities emerging from and/or leading to specific chronic conditions. We applied the LPA to mine the most probable sequence of comorbidities between the emergence of substance abuse in year 1, and substance abuse in year 5, and identified the major trajectory contains recurrent substance abuse across different years. This trajectory that includes $10 \%$ of all patients, who end up with substance abuse in year 5, suggests that the history of substance abuse is the major predictor of future substance abuse problems. Such finding from LPA might be best understood in both the context of the health care system where the diagnoses are made and the clinical associations between the diagnoses themselves. Given that substance abuse is also implicated in other adverse outcomes such as suicidality, homelessness and mortality, this usecase analysis will provide prognostic insight for clinicians caring for Veterans who sustained SuAb. In addition to that, it can be used in demonstrating utility of a method that may be used to identify and mitigate risk in individuals at greatest risk for adverse outcomes of interest such as suicide, homelessness, and early mortality.

Our findings highlight unique strengths and insights that can be gained from our algorithm and LPA and in this context, we have identified several new lines of clinical inquiry. Can early intervention of substance abuse problem prevents it in the future? Are patients with PTSD and/or Depression self-medicating with agents that predispose them to substance abuse problems, i.e., alcohol and illicit drugs? Were the treatments for these conditions suboptimal and did they include medications that predisposed patients to increased risk of substance abuse, i.e., benzodiazepines and opioids? This may be particularly relevant if back-pain is present, but not a clinical priority.

# Study limitations 

In this work, patients whose data was not maintained over the focused years were omitted. Aside from death, drop out can result from not requiring care or receiving care from other health providers, which typically happens to healthier patients and those who have health insurance. Consequently, the restricted population whose incomplete data are omitted, can be biased toward healthier patients and those with health insurance, which affect the predictability of the conditions. In addition, omitting the patients with missing data and dropout considerably reduces the number of available records for estimation and validation. The validity of this study was largely dependent on the accuracy of the diagnosis and record keeping. The data used to train the model has been attained from the VA and the data set has partial bias towards conditions related to military affairs. For instance, the Veteran population with TBI is weighted toward mild TBI, and a large number with blast exposure, which is not common in the civilian population. In addition, while military service members are required to have a higher level of fitness than the general population, Veterans who receive VA care tend to be of lower socioeconomic status and have more comorbidities than Veterans who do not receive VA care. Thus, the model cannot be used for general-purpose medical analysis, and findings may not generalize beyond the study cohort. However, the model can be retrained and extended for general-purpose analysis if the model data can be extended using the public health registries with similar diagnostic factors.

## Conclusion

In this paper, we proposed an unsupervised Multi-level Temporal Bayesian Network (MTBN) for revealing the hidden patterns of interaction among multiple chronic conditions and patient

levels risk factors, that can support medical decisions in absence of an medical expert or existing literature. The proposed approach develops a heuristic node ordering algorithm that reduces the computational complexity of the structure learning algorithm in temporal Bayesian networks. It also proposes a multi-level structure to model the hierarchal structure of patient level risk factors and co-morbidity. Additionally, it incorporates a Longest Path Algorithm (LPA) for identifying the most probable trajectories of comorbidities emerging from and/or leading to specific chronic conditions. We validated the performance of the proposed unsupervised approach against semi-supervised, and supervised learning Bayesian networks, as well as multivariate probit regression, multinomial logistic regression, and Latent Regression Markov Mixture Clustering (LRMCL) using a large dataset of more than 250,000 patients being monitored for 5 years. This approach has clinical implications for predicting how complex comorbid conditions may evolve. Importantly, this methodology can be used with large medical information datasets to develop predictive models for a wide variety and large number of clinical conditions including those that do not have previously demonstrated physiological or epidemiological associations.

# Supporting information 

S1 Fig. Semi-supervised and supervised networks. Learned BN structure from: (a) the semisupervised method and (b) the supervised method.
(PDF)
S1 File. Algorithms. The algorithms used to learn the BN structures mentioned in the manuscript.
(PDF)
S1 Table. ICD-9 codes. The ICD-9 codes for the disease conditions considered in the manuscript.
(PDF)
S2 Table. Disease codes in Table 5. The list of disease codes used in Table 5 of the manuscript.
(PDF)

## Author Contributions

Conceptualization: Syed Hasib Akhter Faruqui, Adel Alaeddini.
Data curation: Syed Hasib Akhter Faruqui, Mary Jo Pugh.
Formal analysis: Syed Hasib Akhter Faruqui, Adel Alaeddini, Mary Jo Pugh.
Funding acquisition: Adel Alaeddini, Carlos A. Jaramillo, Jennifer S. Potter, Mary Jo Pugh.
Investigation: Syed Hasib Akhter Faruqui, Adel Alaeddini, Carlos A. Jaramillo, Mary Jo Pugh.
Methodology: Syed Hasib Akhter Faruqui, Adel Alaeddini, Carlos A. Jaramillo, Mary Jo Pugh.
Project administration: Adel Alaeddini, Mary Jo Pugh.
Resources: Adel Alaeddini, Mary Jo Pugh.
Software: Syed Hasib Akhter Faruqui.
Supervision: Adel Alaeddini, Carlos A. Jaramillo, Mary Jo Pugh.

Validation: Syed Hasib Akhter Faruqui, Adel Alaeddini, Carlos A. Jaramillo, Jennifer S. Potter, Mary Jo Pugh.
Visualization: Syed Hasib Akhter Faruqui, Adel Alaeddini.
Writing - original draft: Syed Hasib Akhter Faruqui, Adel Alaeddini.
Writing - review \& editing: Syed Hasib Akhter Faruqui, Adel Alaeddini, Carlos A. Jaramillo, Mary Jo Pugh.
