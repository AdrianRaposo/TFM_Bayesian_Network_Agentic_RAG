# Interpretable machine learning model for digital lung cancer prescreening in Chinese populations with missing data 

Shuaijie Zhang ${ }^{1,2}$, Qing Wang ${ }^{1,2}$, Xifeng $\mathrm{Hu}^{1,2}$, Botao Zhang ${ }^{1,2}$, Shuangshuang Sun ${ }^{1,2}$, Ying Yuan ${ }^{1,2}$, Xiaofeng Jia ${ }^{3}$, Yuanyuan Yu ${ }^{2,4} \boxtimes$ \& Fuzhong Xue ${ }^{1,2} \boxtimes$

We developed an interpretable model, BOUND (Bayesian netwOrk for large-scale IUng caNcer Digital prescreening), using a comprehensive EHR dataset from the China to improve lung cancer detection rates. BOUND employs Bayesian network uncertainty inference, allowing it to predict lung cancer risk even with missing data and identify high-risk factors. Developed using data from 905,194 individuals, BOUND achieved an AUC of 0.866 in internal validation, with time- and geography-based external validations yielding AUCs of 0.848 and 0.841 , respectively. In datasets with $10 \%-70 \%$ missing data, AUC ranged from $0.827-0.746$. The model demonstrates strong calibration, clinical utility, and robust performance in both balanced and imbalanced datasets. A risk scorecard was also created, improving detection rates up to 6.8 times, available free online (https://drzhang1.aiself.net/). BOUND enables non-radiative, cost-effective lung cancer prescreening, excels with missing data, and addresses treatment inequities in resource-limited primary healthcare settings.

Lung cancer is the most commonly occurring cancer ${ }^{1}$. Over a third of the world's newly diagnosed cases of lung cancer and related fatalities are reported in China ${ }^{2,3}$. The prevailing guidelines for lung cancer screening target individuals with significant risk factors, such as a history of lung cancer in the family or smoking, etc ${ }^{4,5}$. However, among the Chinese who don't meet lung cancer screening criteria, the detection rate is around $1.4 \%{ }^{6}$, with the rate of missed diagnoses reaching as high as $75.6 \%{ }^{7}$. Research shows that among populations with higher risk factors, the proportion of lung cancers detected at an advanced stage is higher than in populations typically considered to be at low risk ${ }^{8}$. In addition, low- and middle-income regions face a high risk of diagnostic delays due to relatively poor health awareness and limited clinical resources. Notably, the five-year survival rate for advanced lung cancer remains bleak, at about $20 \%{ }^{8,9}$, and the mortality rate of lung cancer in China continuing to escalate in recent years ${ }^{10}$. Therefore, it is crucial to broaden the scope of screening to enhance early detection and improve survival rates.

Low-dose computed tomography (LDCT) is widely employed for lung cancer screening. However, its application is constrained in economically underdeveloped regions, preventing its widespread adoption. For example, as of 2022, primary health-care institutions-which constitute about $96.36 \%$ of the total healthcare facilities in China ${ }^{11}$ -
often lack the necessary resources and expertise to diagnose serious illnesses. In addition, LDCT screening is focused on populations with higher risk factors ${ }^{12}$, yet its detection rate among these groups in China ranges from $0.35 \%$ to $2.34 \%{ }^{6,13,14}$. LDCT also carries certain risks, such as exposure to radiation ${ }^{15}$. Hence, a more cost-effective, broadly applicable and non-radiative prescreening method is needed to identify individuals highly likely to have lung cancer.

Certainly, researchers have developed numerous lung cancer screening models to address the aforementioned issues. Many of the models developed depend on questionnaires to collect information on lifestyle habits, such as smoking, along with laboratory tests and genetic data ${ }^{16-18}$. However, this data collection is notably time-consuming and requires substantial labor. Electronic Health Record (EHR) data offer an alternative, that can indirectly reflect the effects of these elementary factors through records of disease exposures. Nonetheless, the lack of specialization and inadequate equipment in primary health-care institutions can lead to overly conservative diagnoses, resulting in the omission of critical health information and missing data, rendering existing EHR-based models ineffective ${ }^{19-22}$. Moreover, existing models generally lack the capability to elucidate the pathways of lung cancer ${ }^{19-22}$, a limitation that hinders their application in decision-

[^0]
[^0]:    ${ }^{1}$ Department of Epidemiology and Health Statistics, School of Public Health, Cheeloo College of Medicine, Shandong University, Jinan, 250012, China. ${ }^{2}$ Institute for Medical Dataology, Cheeloo College of Medicine, Shandong University, Jinan, 250012, China. ${ }^{3}$ Health and Wellness Assurance Center Network Information Office of Boxing County, Shandong, 256500, China. ${ }^{4}$ Data Science Institute, Shandong University, Jinan, Shandong, 250100, China.
    e-mail: yu_yy_1993@163.com; xuefzh@sdu.edu.cn

making for doctors. Therefore, there is an urgent need to develop efficient models that can accommodate missing data and provide an insightful pathway-centric framework for understanding the inference of lung cancer risk, thereby enhancing the clinical utility.

In this study, we developed an interpretable machine learning-based model (known as BOUND) using EHR data from 4909 hospitals and primary health-care institutions. BOUND leverages Bayesian Network (BN) to elucidate the dependency relationships between variables. To address the challenges of sparse EHR data, we developed a novel parameter learning method of BOUND, i.e., BN-logistic. We assessed its performance by comparing it with traditional parametric learning methods, such as maximum likelihood estimation and Bayesian estimation, using both simulated and real-world data. By fully utilizing BN's capacity for uncertainty inference ${ }^{23,24}$, the model facilitates lung cancer prescreening even with incomplete data. To assess the model's generalizability, we performed both internal and external validations, considering temporal and geographical variations. We also assessed its performance on imbalanced data sets. Additionally, a risk scorecard of lung cancer was created to improve the model's convenience, accessible for free at https://drzhang1.aiself.net/.

## Results

## Description of the training and validation sets

The BOUND model training set ultimately included 905,194 participants, of which 5293 were diagnosed with lung cancer. In the internal validation set, out of 387,941 participants, 2172 were lung cancer patients. The time-based external validation encompassed 874,543 participants, with 10,833 diagnosed as lung cancer patients; while the geography-based external validation comprised 166,641 participants, with 994 diagnosed with lung cancer. The flowchart of dataset creation is clearly illustrated in Fig. 1. Between the training set and the two external validation sets, the majority of the variables analyzed showed significant statistical differences, detailed information can be found in Supplementary Table 1.

## Model structure and its performance

Following variable selection, the BOUND model ultimately incorporated 100 variables. The results of the logistic univariate analysis for these variables are detailed in Supplementary Table 2, with the outcomes of incremental feature selection showed in Supplementary Fig. 1. The workflow for constructing the BOUND model is illustrated in Fig. 2. BOUND was developed in three stages: network structure learning, parameter learning, and inferring lung cancer risk using BN's uncertainty reasoning under missing data conditions. In the parameter learning phase, we introduced BN-logistic to address sparse data challenges, and compared it with traditional parameter learning methods using both simulated and real-world datasets. More details can be found in the Methods section.

The network structure of BOUND can be viewed in Fig. 3 or enlarged on the webpage (https://drzhang2.aiself.net/) for a better view. The network structure revealed key variables directly related to lung cancer diagnosis, including age, gender, abnormal findings on diagnostic imaging and function studies (without diagnosis), diseases of the respiratory system, persons encountering health services for specific procedures and health care, and diseases of the pleura. We demonstrated the magnitude of effects of these variables in lung cancer diagnosis in Table 1.

BOUND demonstrated an AUC of 0.860 ( $95 \%$ CI: $0.855-0.867$ ) on the training set, as shown in Fig. 4. For the internal validation set, the AUC was 0.866 ( $95 \%$ CI: $0.857-0.875$ ) (Supplementary Fig. 2). External validations indicated that the BOUND model maintained commendable performance, with an AUC of 0.848 ( $95 \%$ CI: $0.844-0.852$ ) for time-external validation set and an AUC of 0.841 ( $95 \%$ CI: $0.827-0.855$ ) for geographic-external validation set (Supplementary Fig. 3 and Supplementary Fig. 4). The calibration curve exhibited good concordance. Decision curve analysis further validated the clinical utility of these models.

The AUCs of BN-logistic in the internal validation set, time-external validation set, and geographic-external validation set were higher than that of traditional BN parameter learning methods, showing statistically significant differences (see Table 2). In simulated data with different sparsity
![img-0.jpeg](img-0.jpeg)

Fig. 1 | Flowchart of model population enrollment. The figure illustrates the inclusion process for the training set, internal validation set, time-based external validation set, and geography-based external validation set. Samples from the Cheeloo LEAD database, spanning January 1, 2015, to October 31, 2017, were
included in the training and internal validation sets, while data from January 1, 2018, - October 31, 2020, were used for the time-based external validation set. The geography-based external validation set was sourced from the Boxing database.

![img-1.jpeg](img-1.jpeg)

**Fig. 2 | Overview of the BOUND model development and validation process.** The BOUND model is composed of three key components: Bayesian network structure learning, parameter learning, and uncertainty inference. To make the model more user-friendly, a lung cancer risk scorecard was developed based on BOUND, enabling the assessment of high and low lung cancer risk. The model was trained on the training set and validated through both internal and external evaluations. The figure is created with BioRender.com.

levels, BN-logistic demonstrated superior performance in terms of the calibration curve (intercept closer to 0, slope closer to 1), AUC, sensitivity, and Youden's index (Fig. 5).

We evaluated BOUND's predictive accuracy using PR curve on both balanced and imbalanced datasets. Figure 6 illustrates the dependency of precision on prevalence, which is thoroughly analyzed in Equation (4) of Supplementary Note 1. This analysis demonstrates how the PR curve adjusts to different levels of prevalence[25]. Despite initial impressions from Fig. 6 suggesting a strong dependency of BOUND's performance on dataset balance, the reality is quite the contrary. BOUND consistently maintains robust performance across both balanced and imbalanced test sets. Lower the area under the Precision-Recall curve (AUPR) values in imbalanced datasets primarily reflect the severity of dataset imbalance rather than a deficiency in the model's predictive capabilities. Figure 6 further demonstrates that when the PR curve is rescaled, the predictive outcomes for imbalanced datasets closely align with those from balanced datasets, as evidenced by the overlap of the blue and green curves. This confirms BOUND's effectiveness across both balanced and imbalanced datasets.

### Lung cancer risk scorecard

We established a one-to-one correspondence between BOUND and the lung cancer risk scorecard, mapping risk probabilities to a 0–100 scoring system (Fig. 7). The scorecard's AUC, both in the training and validation sets, matches that of BOUND (Supplementary Fig. 5). Based on the scorecard, we identified optimal cut-off value in the training set AUC to categorize risk levels as high or low, with scores below 72.663 classified as high risk. Additionally, we have developed an online lung cancer risk scoring tool, accessible for free at https://drzhang1.aisell.net/. The system generates comprehensive risk assessment reports that not only provide the lung cancer risk level but also identify high-risk factors based on the assessed risk level (detailed in the *Methods* section). This information serves as a reference for physicians to guide further medical action.

### Utilization of model-based customized screening approaches

Utilizing the lung cancer scorecard developed with BOUND, set at risk threshold values ranging from 72 to 50, demonstrated exceptional predictive performance. In the training set, PPV ranged between 4.77% and 15.67%, while NPV was between 99.80% and 99.53%, with specificity improving from 91.93% to 99.33%. Compared to the current screening guideline detection rate of 2.3% in the Chinese population[6,13,14], this scorecard could enhance the detection rate by 2.07 to 6.81 times. In the internal validation set, PPV varied from 4.56%–15.40%, with NPV at 99.81%–99.55% and specificity between 91.95% and 99.36%, achieving a detection rate increase of 1.98–6.69 times. For the time-based external validation, PPV ranged from 3.61% to 11.78%, with NPV between 99.70% and 99.09% and specificity from 72.34%–97.30%, culminating in a detection rate increase of 1.57–5.12 times. In the geography-based external validation set, PPV was between 4.26% and 13.11%, with NPV at 99.77%–99.51% and specificity from 91.31%–99.24%, enhancing the detection rate by 1.85–5.70 times. Details are available in Fig. 8 and Supplementary Table 3.

### Sensitivity analysis

We conducted a sensitivity analysis of BOUND on an external validation set from the Boxing dataset, taking into account different data missingness rates ranging from 10% to 70%. The analysis results revealed that, under various rates of missingness, the calibration curve of BOUND was very close to the ideal state (i.e., the perfectly calibrated diagonal line), demonstrating nearly zero intercept and a slope close to 1 (Fig. 9). Additionally, AUC values fluctuated between 0.827 (95% CI: 0.813 – 0.842) and 0.746 (95% CI: 0.730–0.763), and decision curve analysis further confirmed its good clinical

![img-2.jpeg](img-2.jpeg)

Fig. 3 | The network structure of BOUND. The figure can be enlarged on the webpage (https://drzhang2.aiself.net/) for a better view. To facilitate easier viewing, we categorized the predictor nodes into four layers (indicated by four different colors) from bottom to top, excluding the outcome node "Lung cancer" (considered the 0th layer). The first layer is made up of the parent nodes of "Lung Cancer." The second layer includes the parent nodes of those in the first layer, and this pattern continues until all nodes are organized into four distinct layers.

utility (Fig. 9). The detailed analysis results have been provided in the Supplementary Table 4. Moreover, we also explored the changes in PPV, NPV, sensitivity, specificity, Youden's index, and detection rate ratio within the score range of 72 – 50 under different missingness rates, with these data also included in the Supplementary Table 5. The findings indicate that the PPV ranged from 1.53% – 12.73%, and when the score was less than or equal to 70, the detection rate under missingness conditions from 10% to 70% was higher than the current screening guidelines' detection rate in the Chinese population (Supplementary Fig. 6).

The comparison between the BOUND model and the logistic model (combined with various imputation methods) is shown in Fig. 10. The results indicate that as the missing rate increases, the BOUND model consistently maintains stable calibration. Specifically, the calibration curves' intercepts remain close to 0 (Fig. 10a), and their slopes stay near 1 (Fig. 10b), indicating that the predicted probabilities align well with the actual event probabilities. In contrast, the logistic model, whether using multiple imputation or random forest imputation, shows a significant deviation in the calibration curve slopes from 1 as the missing rate increases, indicating a substantial discrepancy between predicted probabilities and actual event rates. Additionally, in terms of AUC, the BOUND model outperforms the logistic model at missing rates ranging from 10% to 70%, with its advantage becoming more pronounced as the missing rate increases.

#### Discussion

In this study, we developed BOUND, a highly interpretable machine learning model designed for lung cancer digital prescreening. BOUND serves as a low-cost, large-scale, radiation-free preliminary screening tool before LDCT scans. By incorporating BN's uncertainty inference, BOUND's applicability is further enhanced, particularly in scenarios with incomplete medical data, where it predicts lung cancer risk and identifies high-risk factors. This capability aids doctors in making timely intervention decisions. BOUND will hopefully be integrated into routine screening workflows at primary health-care institutions, generating initial risk assessment reports, and reducing the burden on physicians by automatically identifying high-risk patients.

Table 1 | Results from the BN-logistic on variables directly related to lung cancer


Abbreviations: OR Odds Ratio, CI Confidence Interval. ${ }^{*} P$-values reached a significance level of 0.05 . (a) Calibration Curve (b) ROC Curve (c) Decision Curve

![img-3.jpeg](img-3.jpeg)

Fig. 4 | Model evaluation of training set. a Calibration curve, with ' A ' as the intercept and ' B ' as the slope; b ROC curve, showcasing the AUC; c Decision curve, where the area under the green line signifies the net clinical benefit from universal

![img-4.jpeg](img-4.jpeg)


![img-5.jpeg](img-5.jpeg)

Table 2 | Comparative of AUC between BN-logistic and traditional Bayesian Network parameter learning (i.e., Maximum Likelihood Estimation and Bayesian estimation)


Abbreviations: MLE: Maximum Likelihood Estimation; CI: Confidence Interval. ${ }^{*} P$-values reached a significance level of 0.05 . Notes: The $P$-value in the third column represent the comparison between MLE and BN-logistic, while the $P$-value in the fifth column represent the comparison between Bayes estimation and BN-logistic.

To the best of our knowledge, BOUND is developed using EHR data from the largest number of medical institutions in China for digital prescreening of lung cancer to date. This EHR data is sourced from a unified database, the Cheeloo LEAD database, which connects 4909 medical facilities. The database provides each individual with comprehensive access to medical records from all these institutions through an encrypted unique ID. Therefore, BOUND is constructed on the substantial and complete dataset, which ensures its robustness. Our objective is to implement BOUND across healthcare organizations of varying levels. A significant advantage of BOUND lies in its flexibility regarding data requirements, which manifests in two main aspects. Firstly, BOUND does not require complete data, making it especially valuable for resource-constrained primary health-care institutions. These facilities often lack the necessary equipment and professional expertise to diagnose certain critical diseases, frequently resulting in incomplete patient information. Despite these limitations, they can still effectively utilize the BOUND model. However, traditional logistic models fail and require imputation methods for prediction in the missing data. In addition, as shown in the model comparison results (Fig. 10), BOUND outperforms the logistic model combined with imputation under these conditions. Secondly, BOUND only relies on existing information related to

![img-6.jpeg](img-6.jpeg)

**Fig. 5 | Comparative BN-logistic and traditional Bayesian Network parameter learning (i.e., Maximum Likelihood Estimation and Bayesian estimation) on simulated data using calibration curve intercept, calibration curve slope, AUC, sensitivity, specificity, and Youden's index. a** Calibration curve intercept, which is optimal when close to zero. The red dashed line represents the reference line at zero. **b** Calibration curve slope, with optimal values close to one, denoted by a red dashed line at one. **c** represents AUC; **d** indicates sensitivity; **e** represents specificity; and **f** denotes Youden's index. Higher values of AUC, sensitivity, specificity, and Youden's index are preferable. The figure displays the results of 1000 statistical simulations. Details on the simulation can be found in Supplementary Note 6. After verifying that each metric approximately follows a normal distribution, the paired *t*-test was employed to assess whether the BN-logistic model outperformed traditional methods. A *p*-value of <0.05 indicates superior performance of BN-logistic.

demographics, diagnoses, surgical interventions, and pharmacological treatments, without necessitating substantial additional time and resources to collect data on patients' lifestyle habits (such as smoking) or to conduct laboratory tests. Although factors like smoking habits and laboratory test results may influence disease outcomes, these effects can be indirectly reflected through the existing records of disease history and treatment conditions. This strategy, which depends on available medical records, significantly alleviates the burden of data collection, rendering the BOUND not only practical but also broadly applicable across various healthcare settings.

BOUND can effectively make predictions in the presence of missing data, thanks to its use of the uncertainty inference capabilities of BN. In this paper, we adopt the likelihood weighting method for uncertainty inference. Likelihood weighting proves effective in predicting outcomes with missing data because it enables estimation of the probabilities of outcomes based on available evidence. This method involves sampling informed by prior knowledge and adjusting the significance (weight) of these samples to reflect their congruence with observed data. This approach helps to avoid the biases and inaccuracies that can arise from attempts to impute or guess missing values. Additionally, likelihood weighting offers significant advantages in large-scale screening scenarios as it converges quickly with large networks[^1].

In supporting clinical decision-making, the BOUND model also effectively leverages BNs uncertainty inference, playing a pivotal role. Traditionally, clinical decisions have often relied on a physician's intuition and experience, overlooking the rich information hidden in the data. However, the BOUND model leverages the vast amount of information available in EHR data to support decisions in two key areas. First, it assists in the screening for lung cancer. Second, it aids in managing high-risk factors. Specifically, the BOUND model employs BN's uncertainty reasoning to generate risk scores and classifications for lung cancer (Equation (6)).

![img-7.jpeg](img-7.jpeg)

[^1]: Reference for the patient's intention to use the information hidden in the data.

![img-8.jpeg](img-8.jpeg)

**Fig. 6 | Evaluating the predictive performance of BOUND on balanced and imbalanced datasets using Precision-Recall curves. a–d** Four panels represent testing in the training set, an internal validation set, and two external validation sets, respectively. Imbalanced test sets are denoted by red lines, while balanced test sets are marked with blue lines. The prevalence are as follows: 0.58% in the training set, 0.56% in the internal validation set, 1.24% in the time-external validation set, and 0.60% in the geographic-external validation set. All balanced datasets have a prevalence of 50%. The precision for balanced datasets is calculated as the average precision across 100 datasets generated by matching positive and negative cases in a 1:1 ratio. All imbalanced scenarios (red lines) are rescaled to match the prevalence of the corresponding balanced scenarios (green lines) using Equation (4) in Supplementary Note 1. Upon doing so, it is observed that the green and blue lines almost completely overlap, confirming BOUND's capability to perform effectively under both balanced and imbalanced datasets.

**Fig. 7 | The relationship between lung cancer risk probability and the corresponding scorecard conversion.** The black dots represent the risk probability and corresponding risk score for each individual in the training set, the green curve illustrates the fitted function: *Riskscore* = 30.996 – 7.923*log(*RiskProbability*/(1 − *RiskProbability*)).

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

**Fig. 8 | Comparison of PPV and detection rate ratios at different scoring thresholds in the training set, internal validation set, and two external validation sets. a** Positive predictive values (PPV) at various high and low-risk score thresholds. Exploring a range of high to low-risk thresholds from 72 to 50 points, where a lower score indicates poorer health and a higher risk of lung cancer. **b** The detection rate of the BOUND model is compared to the higher detection rate of 2.3% observed in current lung cancer LDCT screening, with the detection rate ratio calculated as the BOUND model's detection rate divided by 2.3%.

Additionally, based on these risk levels and the patients' medical history, BOUND can backtrack to identify high-risk factors (Equation (8)), helping clinicians prioritize these in their decision-making process—something that traditional logistic regression models cannot achieve. For example, individuals identified as high-risk for lung cancer, especially those with previous abnormal imaging records, should prioritize preventive lung cancer screenings, such as LDCT. Moreover, physicians may recommend targeted preventive measures for high-risk factors. For those assessed as low-risk for lung cancer but with multiple known high-risk factors, it is advisable to focus on preventive strategies specifically addressing these risk factors. We have developed a free tool incorporating these capabilities, available at https://drzhang1.aiself.net/, allowing physicians to download risk reports and guide subsequent clinical actions.

BOUND employs the Directed Acyclic Graph (DAG) to visually represent the complex relationships between variables in lung cancer prescreening, with its clear network structure greatly enhancing the model's interpretability. During the BOUND structure learning phase, we employed the TABU search-based algorithm, widely recognized for its high accuracy[35]. The edges in the network capture the conditional dependencies between variables, clearly identifying which factors directly or indirectly influence lung cancer. This visual representation helps clinicians quickly grasp these intricate relationships. Drawing from the results, BOUND identifies key variables directly associated with lung cancer diagnosis, including age[27], gender[28], abnormal findings on diagnostic imaging and in function studies (without diagnosis)[29], respiratory diseases[30], persons encountering health services for specific procedures and health care[31], as well as pleural diseases[32]. Respiratory diseases include chronic lower respiratory diseases[33], influenza and pneumonia[34], and other diseases of the respiratory system[35]. Moreover, the edges in the network represent the pathways through which information propagates within the BOUND. For instance, when the status of "chronic lower respiratory diseases" or "other respiratory diseases" changes, this information is transmitted along the network edges to the "lung cancer" node, thereby influencing the probability distribution of lung cancer occurrence. This information propagation is achieved through BN's uncertainty reasoning (detailed in the *Methods* section). As a result, BOUND's transparent network structure ensures that the model's outputs are both understandable and traceable, further reinforcing the model's interpretability.

To address the issue of unlearnable parameters for certain variable combinations caused by data sparsity, we innovatively developed the BN logistic to learn the network parameters of BOUND. Compared to traditional parameter learning methods, BN logistic demonstrated superior performance on both internal and external validation sets as well as in simulated data across various levels of sparsity (Fig. 5 and Table 2). Thus, BN logistic has proven to be a robust and viable solution for real-world applications where data sparsity is a common challenge.

We conducted comprehensive internal and external validations to evaluate BOUND's performance. We assessed its calibration, discrimination, and clinical utility, testing its screening capability under both balanced and imbalanced data conditions using the rescaled PR curve[25]. External validations across different time periods and geographic locations demonstrated BOUND's excellent performance, with AUC values of 0.848 (95% CI: 0.844-0.852) and 0.841 (95% CI: 0.827-0.855) on two heterogeneous validation sets (Supplementary Table 1, Supplementary Fig. 3 and Supplementary Fig. 4). The rescaled PR curve (Fig. 6) further confirmed BOUND's consistently strong performance across both balanced and imbalanced datasets.

To further enhance the convenience and application scope of lung cancer risk assessment, we developed a lung cancer risk scorecard. After validation on the training set, internal validation set, and external validation sets, the AUC values of the scorecard were consistent with the risk probabilities outputted by BOUND (Supplementary Fig. 5), demonstrating that no information was lost during the conversion process. The scorecard offers governments and healthcare institutions a powerful tool for widespread lung cancer screenings. For broad-scale implementation, we recommend setting the threshold for distinguishing between high and low risk at 72 points in environments where resources are ample. This approach has the potential to double the detection rates of lung cancer compared to those achieved under current screening guidelines, as illustrated in Fig. 8. Conversely, in settings where resources are more constrained, our goal shifts towards maximizing the number of detected lung cancer cases. Here, opting for a lower threshold, such as 50 points, we can identify a smaller yet significantly higher-risk group for further LDCT screening. This method could elevate detection rates by 5.12 to 6.81-fold (Fig. 8), showcasing the scorecard's potential to make a substantial impact in lung cancer screening across various resource availability scenarios.

The BOUND model was trained on a dataset of nearly one million samples using a single-core CPU. The training process took 25.8 min and required 2.1 GB of memory, both well within acceptable limits.

Our study has a few limitations. Firstly, the development and validation of our model were conducted using a retrospective design, hence, prospective studies are needed in the future to more accurately assess the clinical efficacy of this model in early lung cancer detection. Secondly, our study population primarily consisted of individuals from China, and the effectiveness of the model in other countries needs to be validated and confirmed through more extensive research.

In summary, BOUND, as an interpretable digital prescreening tool, can be integrated into routine clinical workflows to provide large-scale, low-cost lung cancer screening. We also have developed a free, user-friendly

![img-11.jpeg](img-11.jpeg)

**Fig. 9 | Evaluation of the BOUND model's performance on the geography-based external validation under completely random missing rates of 10%–70%. a** The intercept of the calibration curve, with values closer to 0 being preferable. **b** The slope of the calibration curve, where values closer to 1 are optimal. **c** ROC curves, with the area under the curve representing the AUC. **d** Decision curves.

online platform (https://drzhang1.aiself.net/) that allows for convenient and intuitive assessment of lung cancer risk levels. The platform highlights high-risk factors and provides an initial health report for doctors to reference when considering further preventive interventions. We believe that AI-based prescreening is a pressing need that bridges interpretable machine learning models with professional medical expertise, reducing the workload for physicians while ensuring timely diagnoses. This approach will effectively address the diagnostic delays caused by unequal access to healthcare services, ultimately aiming to reduce lung cancer mortality rates.

# **Methods**

## **Data source and setting**

This is an observational retrospective study. The data was obtained from the Cheeloo Lifespan Electronic-Health Research Data-library (Cheeloo LEAD) and the Boxing database. The Cheeloo LEAD database integrates data from 5,152,597 individuals across 4909 hospitals and primary health-care institutions in 39 urban areas from Shandong Province, China. This collection includes 1214 secondary and tertiary hospitals as well as 3695 primary medical institutions. Each individual can be linked to their comprehensive data across all 4909 medical institutions through an encrypted unique ID. Additionally, the Cheeloo LEAD database retrospectively collected EHR data from 2009 to 2023, covering a follow-up period of around 14 years. The Boxing database, serving as one of the external validation sets, has compiled EHR data from three sub-district offices and nine towns in Boxing County, Shandong Province, China, for the period from 2018 to 2023. This dataset does not overlap with the Cheeloo LEAD database. Both datasets comprise demographic, diagnostic, medication, and surgery.

![img-12.jpeg](img-12.jpeg)

**Fig. 10 | The model comparison results.** The BOUND model was compared to the traditional logistic regression model across datasets with varying missing data rates. Since the traditional logistic regression model cannot be directly applied to missing data, we employed multiple imputation (MI) and random forest (RF) imputation to handle the missing values, allowing for its application in missing datasets. **a** Calibration curve intercept, the closer to 0 the better; (**b**) Calibrate the slope of the curve, the closer to 1 the better. **c** The performance of AUC. As the missing data rate increases, the advantage of the BOUND model becomes more pronounced.

information. We follow the common data model[57] to conduct data quality control and standardization on data from various sources and formats, thereby establishing a unified terminology.

### Study population

Participants for the training and internal validation sets were selected from the Cheeloo LEAD database, covering the period from Jan 1, 2015, to Oct 31, 2017. Inclusion criteria were individuals aged 40 years and above, with exclusions for those previously diagnosed with lung cancer before recruitment and individuals with abnormal lung cancer diagnosis dates. The lung cancer diagnosis code was determined based on the International Classification of Diseases, 10th edition (ICD-10), specifically code C34. Data were randomly divided into the training set and internal validation set using a 7:3 ratio.

For external validations, the study conducted both temporal and geographic validations. Temporal validation involved participants from the Cheeloo LEAD database between Jan 1, 2018, and Oct 31, 2020, adhering to the same inclusion and exclusion criteria as the training set. Geographic validation included individuals aged 40 years and above from the Boxing database, spanning Jan 1, 2019, to Dec 31, 2020, with similar exclusions for those with prior lung cancer diagnoses.

Figure 1 illustrates the flowchart of enrollment. The study adhered to the Transparent Reporting of a multivariable prediction model for Individual Prognosis or Diagnosis (TRIPOD).

### Variable selection

In this study, we collected 4148 potential predictors, including demographic variables, diagnoses, surgical interventions, and medication usage. Age was categorized into a five-level variable, while all other variables were dichotomized (see Supplementary Note 2 for detailed values of variables). All candidate variables were initially evaluated using a univariate logistic regression model. Given the multitude of variables, to control the overall risk of Type I error (false positive rate), *p*-values underwent Bonferroni correction, selecting variables with *p* < 0.05/4,148. To fully leverage the interrelationships among variables and enhance prescreening accuracy in the presence of missing data, we implemented Incremental Feature Selection (IFS), which selects an appropriate number of variables. For more details of the IFS, please see Supplementary Note 3. Definitions and coding formats of predictors for BOUND can be located in the Supplementary Table 6.

### Development of the BOUND model

We developed BOUND using the complete training set sourced from the Cheeloo LEAD database, which has the advantage of linking comprehensive data from 4909 hospitals and primary health-care institutions. Each individual's records across these institutions are indexed using an encrypted unique ID, ensuring a dataset with no missing entries.

The development of BOUND is divided into three steps: First, learning the BN structure; second, acquiring the BN parameters; and finally, conducting BN's uncertainty inference to get the lung cancer risk and reverse

inference of high-risk factors. BN's uncertainty inference can predict risk even when data is missing. Figure 2 illustrates the workflow involved in constructing the BOUND model.

Step 1: Learning the BN structure of BOUND. Firstly, we used the TABU search algorithm to learn the BN structure, allowing us to intuitively display the dependency relationships between variables ${ }^{30}$. The TABU search algorithm optimizes BN structures by iteratively modifying initial structures and evaluating them with a scoring function like BIC. The best-scoring structure that isn't on the TABU list, which prevents revisiting recent structures, is selected to continue the search. This process repeats until a stopping criterion is met, resulting in an optimized BN structure. The following formula represents the principle of the TABU algorithm:

The structure learning algorithm of BN explores the entire feasible structure space $\mathbb{G}$ using the given data $\boldsymbol{D}$ and identifies the optimal structure $\mathcal{G}$ by maximizing a defined objective score function (Equation (1)), which measures the fit between the structure and the data.

$$
\mathcal{G}=\arg \max _{\mathbb{G}^{*} \in \mathbb{G}} S\left(\mathbb{G}^{*}, \mathbf{D}\right)
$$

During the network structure learning, we integrated some prior knowledge to enhance the network's interpretability and accuracy (see Supplementary Note 4 for details).

Step 2: Learning the BN parameter of BOUND. Faced with the challenge of sparse data in EHR, the traditional BN parameter learning method, specifically the maximum likelihood estimation, often encounters limitations in prediction due to the generation of missing values. In Supplementary Note 5, we comprehensively explain the occurrence of missing values, detailed through formula derivation. To overcome this challenge, we developed a new parameter learning algorithm, BN-logistic. BN-logistic learns the effects $\boldsymbol{\beta}$ between variables and applies them across all possible combinations of variable values, generating conditional probability tables for all scenarios.

Here is an explanation of the principles behind BN-logistic:
The BOUND model is represented by $\mathcal{B}=\langle\mathcal{G}, \boldsymbol{\theta}\rangle$, where $\mathcal{G}$ denotes the network structure learned in Step 1, and $\boldsymbol{\theta}$ represents the network parameters. Assume the network contains $p$ discrete variables $\mathbf{X}=\left\{x_{1}, x_{2}, \cdots, x_{p}\right\}$. Each node $x_{i}$ in the network can take $r_{i}$ possible values, specifically $1,2, \cdots, r_{i}$. The value combinations of the parents $\mathbf{p a}_{i}^{\mathcal{B}}$ of $x_{i}$ amount to $q_{i}$, ranging from $1,2, \cdots, q_{i}$. If $x_{i}$ has no parents, then $q_{i}$ is 1 . Consequently, the parameters of BOUND are defined by the following conditional probability:

$$
\boldsymbol{\theta}_{x_{i} \mid \mathbf{p a}_{i}^{\mathcal{B}}}=P_{f i}\left(x_{i} \mid \mathbf{p a}_{i}^{\mathcal{B}}\right)
$$

Here, $\mathbf{p a}_{i}^{\mathcal{B}}$ denotes the set of parents of variable $x_{i}$ in $\mathcal{B}$. The formula can be expanded as:

$$
\theta_{i j k}=P\left(x_{i}=k \mid \mathbf{p a}_{i}^{\mathcal{B}}=j\right)
$$

where $x_{i}$ represents the $i$-th variable among the $p$ variables, $i$ ranges from 1 to $p . k$ denotes the $k$-th value of $x_{i}$, with a range from 1 to $r_{i} . j$ signifies the $j$-th value combination of the parents $\mathbf{p a}_{i}^{\mathcal{B}}$ of $x_{i}$, where $j$ ranges from 1 to $q_{i} . \boldsymbol{\theta}$ represents the vector comprising all $\theta_{i j k}$ combinations.

BN-logistic involves treating each child node as a dependent variable and its parent nodes as independent variables, fitting logistic models for each node in the network, as delineated in Equation (4).

$$
\log \left(\frac{P_{x_{i}=1}}{1-P_{x_{i}=1}}\right)=\beta_{i 0}+\sum_{m_{i}=1}^{M_{i}} \beta_{i m_{i}} \mathrm{pa}_{i m_{i}}
$$

where $x_{i}$ represents the $i$-th node. $M_{i}$ is the count of parent nodes associated with $x_{i}, \boldsymbol{\beta}_{i}=\left\{\beta_{i 0}, \beta_{i 1}, \ldots, \beta_{i M_{i}}\right\}^{T}$ is the coefficient of the parent nodes $\mathbf{p a}_{i}$ of
$x_{i}$ to $x_{i} . \mathrm{pa}_{i m_{i}}$ denotes the $m$-th parent node of $x_{i} . P_{x_{i}=1}$ is used to represent the probability when $x_{i}=1$.

Subsequently, we determine the conditional probability for each node by enumerating all possible parent node combinations for every node:

$$
P_{x_{i}=1}=P\left(x_{i}=1 \mid \mathbf{p a}_{i}\right)=\frac{1}{1+\exp \left(-\left[\beta_{i 0}+\sum_{m_{i}=1}^{M_{i}} \beta_{i m_{i}} \mathrm{pa}_{i m_{i}}\right]\right)}
$$

When $x_{i}=1$, the probability of that class is $P\left(x_{i}=1 \mid \mathbf{p a}_{i}\right)$; otherwise, the probability is $1-P\left(x_{i}=1 \mid \mathbf{p a}_{i}\right)$. Consequently, regardless of the values of new data, the corresponding conditional probability tables, which are the parameters of BN, can be derived based on the effects $\boldsymbol{\beta}$ learned. BN-logistic effectively addresses the issue of certain variable combinations remaining unlearned due to sparse data, which consequently cannot be predicted. We evaluated BN-logistic against traditional parameter learning methods using simulation data across various levels of sparsity and real-world data, including internal and external validation sets (see Supplementary Note 6 for details).

Step 3: BN's uncertainty inference for BOUND prediction with missing data. To ensure the BOUND model remains versatile and effective even with missing data, we utilize BN uncertainty inference capabilities. Specifically, we employ the likelihood weighting method within BN inference algorithms, which converges quickly and efficiently handles large networks ${ }^{33}$. This method generates a large number of samples from the network, where the known variables are fixed and the missing variables are sampled according to the network's conditional probabilities, i.e., the parameter of BOUND ${ }^{34}$. Each sample is assigned a weight that reflects the likelihood of the evidence variables given the sampled values. By aggregating these weighted samples, we can approximate the posterior distribution, providing the probability of lung cancer risk. The formula for likelihood weighting is as follows ${ }^{33,34}$ :

$$
P(Q=1 \mid \mathbf{E}=\mathbf{e}) \approx \frac{\sum_{i=1}^{S} I_{Q=1}\left(D_{e}\right) \omega\left(D_{e}\right)}{\sum_{i=1}^{S} \omega\left(D_{i}\right)}, \quad D_{e} \sim P^{\prime}(\mathbf{X})
$$

where, the observed variables are referred to as evidence variables, denoted as $\mathbf{E}=\mathbf{e} ; Q=1$ denotes a diagnosis of lung cancer; $P(Q=1 \mid \mathbf{E}=\mathbf{e})$ represents the posterior probability of lung cancer risk, calculated using existing known variables' data $\mathbf{E}=\mathbf{e} ; I_{Q=1}$ is the indicator function;

$$
\omega\left(D_{e}\right)=\left.\prod_{Y \in \mathbf{E}} P\left(Y \mid \mathbf{p a}_{Y}\right)\right|_{\mathbf{X}=D_{e}}
$$

Thus, the likelihood weighting method essentially assigns a likelihood rate weight, denoted as $\omega\left(D_{t}\right)$, to each sample $D_{e}$. In this paper, we calculate the lung cancer risk for each individual by performing 19,760 samplings (i.e., $S=19,760$ ) based on their known variables. The sample size is the default value in the R package bnlearn: $5000 * \log 10$ (nparams(fitted_model)).

Moreover, what's even more interesting is that BOUND can leverage BN's uncertainty reasoning to backtrack from predicted outcomes and known medical history to identify high-risk factors. This capability enables doctors to take timely preventive measures. The underlying principle is as follows:

According to the Markov property ${ }^{35}$, once the parent nodes of lung cancer are given, the lung cancer risk becomes conditionally independent of other risk factors. This allows us to directly control the risk factors associated with lung cancer, which correspond to the parent nodes of lung cancer in the network. Therefore, we use the predicted outcomes and existing medical history (i.e., the set of variables where $\mathbf{X}=1$ ) as evidence variables to infer high-risk factors that are directly related to lung cancer but have not yet been

clearly diagnosed. The calculation formula is as follows:

$$
P\left(\mathbf{Q}=1 \mid \mathbf{E}=\{\mathbf{X}=1, Y=y\}\right) \approx \frac{\sum_{s=1}^{S} I_{Q_{s+1}}\left(D_{s}\right) \omega\left(D_{s}\right)}{\sum_{s=1}^{S} \omega\left(D_{s}\right)}, \quad D_{s} \sim P^{\prime}(\mathbf{X})
$$

where, $\mathbf{Q}$ represents a vector set corresponding to risk factors that are directly related to lung cancer in the network but have not yet been clearly diagnosed. $\mathbf{E}=\{\mathbf{X}=1, Y=y\}$ denotes the set of evidence variables, which includes the confirmed variables in the network and the value of $Y$ (where $Y=1$ indicates a high predicted risk of lung cancer, and $Y=0$ indicates a low risk). $P(\mathbf{Q}=1 \mid \mathbf{E}=\{\mathbf{X}=1, Y=y\})$ represents the probability of risk factors taking values of 1 given the evidence variables. $\omega\left(D_{s}\right)$ represents the likelihood weight assigned to each $D_{s}$. We define variables with an output probability greater than 0.5 as high-risk factors.

In summary, the BOUND model's output, including lung cancer risk predictions and identified high-risk factors, serves as a reference for doctors, who can then take preventive measures based on the patient's specific circumstances.

## Validation of the BOUND model

We conducted both internal and external validations of the model, as described in the Study population section. The external validations assessed the model's performance from both temporal and geographical perspectives.

## Lung cancer risk scorecard

To enhance the convenience of lung cancer prescreening, we have developed a lung cancer risk scorecard based on the BOUND model:

$$
\text { Score }=A-B \log \left(\frac{p}{1-p}\right)
$$

where $p$ represents the probability of having lung cancer predicted by the BOUND model; $A$ and $B$, model parameters determined through training, are used to calibrate the scoring scale ${ }^{35}$. This scorecard maps the risk probability into a $0-100$ point scoring system, achieving a quantitative assessment of the patient's lung cancer risk, where a lower score indicates poorer health and a higher risk of lung cancer. Due to the BOUND's ability to effectively predict risk in the presence of missing data, our scorecard can also be applied to risk assessments with incomplete information, significantly enhancing its practicality and flexibility. Furthermore, by identifying the optimal Area Under the ROC Curve (AUC) cut-off value, lung cancer risk is categorized into high and low levels. To thoroughly evaluate the public health value of the scorecard, we analyzed the positive predictive value (PPV), negative predictive value (NPV), sensitivity, specificity, and Youden's index at different scores, comparing these with the current higher detection rate of $2.3 \%$ in lung cancer screening ${ }^{4,7,114}$, calculating the detection rate ratio at different scores.

## Model visualization and online software

We utilized Cytoscape.js for visualizing the BOUND model. We developed a model usage interface specifically designed for hospitals or governments to obtain lung cancer risk levels. This platform also allows for the identification of high-risk factors based on predicted outcomes and known medical history.

## Statistical analysis

In this study, the variables used were all categorical, described by frequency (n) and proportion (\%). For the baseline comparison between the training set and two external validation sets, the chi-square test was utilized for binary variables, while the Wilcoxon rank-sum test was applied for the ordered categorical variable of age.

We evaluated BN-logistic against traditional parameter learning methods (maximum likelihood and Bayesian estimation) on internal and external
validation sets, using the Delong test to assess whether BN-logistic achieved a higher AUC. We also compared these methods on simulated data at various sparsity levels $(0.005,0.015,0.025,0.035,0.045,0.055)$. For each sparsity level, 1000 data sets were generated to evaluate these methods. After confirming that each evaluation index approximated a normal distribution, we conducted a paired $t$-test to assess whether BN-logistic outperformed traditional methods. Sensitivity analysis of BOUND was conducted on the external validation set in Boxing, setting a missing data rate between $10 \%$ and $70 \%$ (notably, age and gender data were complete without missing values), aiming to evaluate the model's performance under various missing data conditions.

For comparison, we used the logistic regression model, which cannot directly handle missing data, was combined with different imputation methods to make predictions. The imputation techniques used were multiple imputation ${ }^{36}$ and random forest imputation ${ }^{37}$. As shown in Supplementary Fig. 1, the model's AUC stabilized after incorporating the top eight features. Therefore, these eight features were selected to construct the logistic model. Like BOUND, the logistic model was trained on the Cheeloo LEAD training set and then applied to the Boxing external validation set under different missing data conditions.

This study comprehensively assessed BOUND's performance in terms of discrimination, calibration, and clinical utility. The model's discriminative ability was evaluated using AUC, assessing the model's effectiveness in distinguishing between lung cancer patients and those non-lung cancer population. Calibration refers to the agreement between predicted risks and observed outcomes. Additionally, decision curve analysis was employed to evaluate the clinical utility of the model. Furthermore, the rescaled Precision-Recall (PR) curve was used to evaluate BOUND's prediction performance for imbalanced data. The detailed process of rescaled PR curve ${ }^{23}$ can be found in Supplementary Note 1. All analyses were performed in R, version 4.3.0, and PostgreSQL, version 15.0.

## Data approval

This study was approved by the Institutional Review Board of the Shandong University School of Public Health, China. No informed consent was required, because the EHR in this study were anonymized.

## Data availability

The datasets used and/or analyzed in the current study can be made accessible by the corresponding author upon a justified request. Prior to utilizing the data, proposals need to be approved by all partners and a data sharing agreement will need to be signed. Approval will depend on the scientific value of the proposal, compatibility with the original patient consent, and data protection legislation.

## Code availability

The analytical code used in this study are available from the corresponding authors on request.

Received: 16 June 2024; Accepted: 22 October 2024;
Published online: 19 November 2024

## Acknowledgements

The authors extend their gratitude to the patients and investigators who contributed to the Cheeloo LEAD and Boxing databases by providing the data. This study was supported by the Key Program of the National Natural Science Foundation of China (Grant No. 82330108); 2021 National Natural Science Foundation Project of China (Grant No. 82173625); Shandong Province Key R\&D Program (Science and Technology Demonstration Project) (Project number: 2021SFGC0504); China Postdoctoral Science Foundation (Grant No. 2022M721921); Shandong Youth Foundation (Grant No. ZR2023QH236).

## Author contributions

F.Z.X., S.J.Z., and Y.Y.Y. contributed to the conception and design of the study. F.Z.X., Y.Y.Y., S.J.Z., Q.W., X.F.J., and X.F.H. managed data collection. S.J.Z., Q.W., X.F.J., B.T.Z., S.S.S., and Y.Y. cleaned and verified the data. S.J.Z. conducted the analysis and prepared the tables and figures. S.J.Z. wrote the first draft of the manuscript. F.Z.X, Y.Y.Y. and S.J.Z. made further revisions to the content of the manuscript. X.F.J. and S.J.Z. developed an online tool. F.Z.X, Y.Y.Y., and S.J.Z. took charge of the decision to submit the manuscript for publication. All authors contributed to, reviewed, and approved the final version of the manuscript. All authors had full access to the data and take responsibility for the integrity of the data and accuracy of the analysis.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information The online version contains supplementary material available at
https://doi.org/10.1038/s41746-024-01309-z.
Correspondence and requests for materials should be addressed to Yuanyuan Yu or Fuzhong Xue.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.
(c) The Author(s) 2024