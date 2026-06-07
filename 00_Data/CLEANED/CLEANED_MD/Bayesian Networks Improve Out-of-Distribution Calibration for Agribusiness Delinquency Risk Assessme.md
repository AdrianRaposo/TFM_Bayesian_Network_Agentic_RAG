# Bayesian Networks Improve Out-of-Distribution Calibration for Agribusiness Delinquency Risk Assessment 

Ana Clara Teixeira ${ }^{\dagger *}$<br>ana.teixeira@traivefinance.com<br>Traive Inc.<br>Brookline, Massachusetts, USA

## Aline Pezente <br> aline.oliveira@traivefinance.com <br> Traive Inc. <br> Brookline, Massachusetts, USA

## ABSTRACT

Automated credit risk assessment plays an important role in agricultural lending. However, credit risk assessment in the agricultural domain has unique challenges due to the impact of weather, pest outbreaks, commodities market dynamics, and other volatile forces that drive risk. Training a model to account for these factors requires immense data assets that are challenging to obtain. Indeed, even the best credit risk assessment models in this domain are trained using data from single-institutions that often focus on dedicated geographical regions, or singular commodities. Hence, most agricultural credit risk models exhibit poor out-of-domain performance. In this paper, we use a novel dataset describing nearly 100 thousand historical loans, sourced from 9 large agricultural lenders to train a Bayesian network model for loan delinquency classification. The proposed model exhibited improved calibration (relative improvement in Expected Calibration Error) in out-of-domain performance tests when compared to three state-of-the-art credit risk scoring approaches: Logistic regression ( $81 \pm 15 \%$ improvement), XGBoost ( $80 \pm 14 \%$ improvement), and an Artificial Neural Networks ( $7 \pm$ $2 \%$ improvement). We conclude that Bayesian networks provide better modeling of agricultural credit risk by combining (limited) data assets with expert domain knowledge. Our approach is likely to generalize to any credit risk assessment task where small sample sizes is of concern.

## CCS CONCEPTS

- Computing methodologies $\rightarrow$ Bayesian network models; Supervised learning by classification.

[^0]Hamed Yazdanpanah ${ }^{\dagger}$ hamed.yazdanpanah@traivefinance.com

Traive Inc.
Brookline, Massachusetts, USA
Mohammad Ghassemi
mohammad.ghassemi@traivefinance.com
Traive Inc.
Brookline, Massachusetts, USA


## KEYWORDS

Bayesian network model, out-of-distribution generalization, probability of delinquency, credit risk assessment, agricultural loan

## ACM Reference Format:

Ana Clara Teixeira, Hamed Yazdanpanah, Aline Pezente, and Mohammad Ghassemi. 2023. Bayesian Networks Improve Out-of-Distribution Calibration for Agribusiness Delinquency Risk Assessment. In 4th ACM International Conference on AI in Finance (ICAIF '23), November 27-29, 2023, Brooklyn, NY, USA. ACM, New York, NY, USA, 9 pages. https://doi.org/10. 1145/3604237.3626897

## 1 INTRODUCTION

Agriculture is critical to food security, and thus, global stability and propriety. There is an increasing investment by public and private financial institutions, such as commercial banks, development banks, investment funds, and industry suppliers, on food production and agriculture industry [8]. The consequences of an incorrect investments are not only problematic for the lender, but also the global food supply, and especially vulnerable populations (which are more sensitive to fluctuations in commodities prices).

Given it's importance, the private sources that finance agricultural activity need robust ways to assess the risk of their investments. The current method are the use of human analysts that leverage a combination of strong domain knowledge, with some data (e.g. from credit bureaus) to assess the credit worthiness of farmers and agricultural businesses seeking loans. However, despite the expertise of many credit analysts, the current method is prone to errors because (1) there are no global standards for how agricultural credit risk assessment aught to be performed and (2) existing analytic tools to support the analysts (such as consumer credit risk scores) are not appropriate because they were not purpose-built for the agriculture; it's not reasonable to assume that a consumer credit risk score can provide a comprehensive assessment of risk because many of the factors that impact agricultural risk are completely beyond the control of the farmer (weather, global conflicts, etc.).

Clearly, there is a need for access to better data and, if this data could be collected, machine learning can enable more efficient and robust risk assessment in the agricultural domain. However, the intricacies of data in the Agriculture industry pose considerable challenges to collect, at scale. Agriculture, by its nature, is a sector heavily influenced by a multitude of uncontrollable and hard to


[^0]:    *Corresponding author
    ${ }^{\dagger}$ These authors contributed equally.

predict factors, such as weather patterns, pest outbreaks, macroeconomic events, geopolitical conflicts, and commodity price volatility. These factors introduce high variance and irregularities into the data that traditional models struggle to capture effectively. Additionally, the vast temporal and spatial differences in agricultural practices across regions, coupled with infrequent and inconsistent data collection methods, result in a high degree of data sparsity and lack of homogeneity. The temporal aspect of agricultural data also introduces seasonality effects that are difficult to account for. Moreover, the industry is impacted by intricate policy changes and market dynamics, furthering the already high dimensional and complex nature of the data. These complexities result in data assets that are small, incomplete, which leads to machine learning models that fail to generalize effectively, which then reinforces the need for the involvement of human experts. Breaking this cycle will require the application of methods that can use a combination of limited data and expert knowledge, to provide robust assessments of risk in situations beyond their original scope of learning.

### 1.1 Related Works

Automated credit risk assessment using machine learning presents a promising approach to resolving unique credit risk complexities within the agricultural ecosystem. Widespread applications of AI and machine learning in finance, underscored by an extensive body of literature on these methods in credit risk assessment [1, 6, 23, 26], support that these methodologies can be effectively adapted to the nuances of agricultural credit. Within agricultural finance, there has been an increasing interest in harnessing the power of machine learning to address credit risk, indicating the willingness of the field to adopt innovative, data-driven strategies [2, 5, 11, 22, 28]. Despite these strides, a review of related work reveals that no existing studies have examined the out-of-distribution generalization capabilities of their proposed models for estimating credit risk. Hence, while the existing work provides crucial groundwork, there is a clear opportunity to advance the field by developing models with reliable out-of-distribution performance.

Frequentist machine learning models, despite their extensive use in credit risk assessment, struggle with accounting for uncertainty and generalizing to new data [25]. On the other hand, previous research has highlighted Bayesian networks as a promising alternative in credit risk assessment, specifically for their capacity to encapsulate inherent uncertainty in the data through the use of prior distributions [15, 16, 20]. These networks offer more than point predictions, extending to quantify the uncertainty or confidence around these predictions. This attribute becomes particularly advantageous when dealing with data not represented in the training set. Furthermore, the Bayesian networks' graphical representation enables experts to understand and validate the model's learning process. The capabilities of Bayesian networks can potentially enhance the model's robustness to out-of-distribution generalization, when the model development process is thoughtfully designed. Our research provides a contribution to the field by demonstrating that Bayesian networks achieve enhanced out-of-distribution performance on credit risk assessment in agricultural finance.

Bayesian networks serve as a suitable framework for implementing methods aimed at improving out-of-distribution generalization,
a major challenge in artificial intelligence systems [21, 27]. Bayesian networks, by facilitating causal representation learning, are at the forefront of methods that effectively counter spurious correlations by accounting for latent variables. Additionally, they can address data shift, given their structural capacity to integrate shift axes as features. Consequently, the impact of these shifts on the target variable can be reflected in the prior distribution, a crucial step toward model robustness against underlying distribution changes. These capabilities position Bayesian networks as a core instrument for principled model design when targeting out-of-distribution generalization. Our work, building on this theoretical foundation, offers empirical substantiation for the efficacy of this approach.

In the quest for robust credit risk models, the emphasis on calibration is paramount. Indeed, in the application of AI to finance, well-calibrated classification models are arguably of greater relevance to credit risk assessment than those with excellent classification performance alone [3, 4, 24]. Calibration is important for risk assessment because it measures the reliability of the model's predictions [7, 18]. Hence, by accurately measuring uncertainty, well-calibrated models contribute to efficient portfolio management and improved financial performance.

In summary, while machine learning techniques, particularly Bayesian networks, hold great promise in credit risk assessment, their full potential is yet to be explored. Addressing out-of-distribution generalization, as measured by calibration, will lead to more robust and reliable credit risk models. Our research represents a relevant step in this direction.

### 1.2 Contributions

This paper introduces a novel application of a Bayesian network to overcome challenges in credit risk assessment in agricultural finance, especially in out-of-distribution scenarios. Notably, Bayesian networks incorporate prior knowledge, a valuable trait when data is limited or of low quality, as is frequently the case in the agricultural credit risk domain [16]. They serve as robust mechanisms against overfitting, with their capacity to assimilate domain expertise contributing significantly to model resilience when tackling out-of-distribution inferences.

A key contribution of our work is the demonstration of the Bayesian network's superior out-of-distribution performance, as gauged by calibration - the most relevant metric in this context. We adopted the Bayesian network to predict agricultural loan delinquency, considering the sector's characteristics such as small datasets, low-quality data, and the necessity to incorporate domain knowledge. This approach was shaped through collaboration with domain experts, resulting in a model that effectively encapsulates the complexities of agricultural credit risk knowledge and provides calibrated estimates for robust out-of-distribution predictions.

The paper is organized as follows: Section 2.1 details the dataset, feature definitions, strategy for handling missing values, and the discretization of continuous variables. The specifics of the proposed Bayesian network are discussed in Section 2.4. The results, including the calibration-based performance comparison with other frequentist models, are presented in Section 3. The discussion is presented in Section 4. Finally, Section 5 provides conclusions and potential directions for future research.

## 2 METHODS

### 2.1 Dataset

In this study, we utilize a dataset comprised of 97,235 agricultural loans granted to 31,900 , Brazilian farmers sourced from nine of the largest financial and supply chain institutions in Brazil; the nine institutions are anonymized and shown by capital letters from A to I in this study. Due to differing credit policies, the characteristics of the data was significantly different across the nine institutions. The loans were typically issued at the onset of the farming season and repayment was expected to be fully executed by the end of the crop season, upon harvest and sales. The target variable in this dataset is a dichotomous variable indicating if the loan was unsuccessfully repaid within 90 days of the loan's due date (i.e., a delinquency event was coded as 1). Detailed characteristics of each institution, including the number of loans issued, the count of unique borrowers, the data time range, and the respective delinquency rates, are presented in Table 1. Notably, the number of loans sources across across the institutions varied significantly, ranging from a minimum of 1,019 loans (see row I, Table 1) to a maximum of 31,095 loans (see row A, Table 1). More importantly, there is a significant variation in delinquency rates among these institutions, ranging from as low as $1.05 \%$ (Institution A) to as high as $22.27 \%$ (Institution F). This variability highlights the disparate credit policies across these institutions emphasizing the the need for a modeling framework that can effectively generalize out-of-distribution.

### 2.2 Features

Each loan in our dataset was characterized by a total of nine features; four of the features were the output of separate models ("Scores" with values ranging from 0 to 1000) designed to characterize key contributors to risk, while the remaining five features are descriptive of the farmer and their farm. We provide additional details about the nine features below.

### 2.2.1 Scores $(n=4)$ :

(1) Agronomic Score: the Agronomic Score is the output of an ML Model that uses historical agronomic and weather patterns to predict the expected crop yield for a given farmer, at a given location, in a given season. A higher yield results in a higher agronomic score. We expect this feature to be useful because of the correlation between yield and the farmer's income - which will be the source for loan repayment.
(2) Market Score: The market score is the output of an ML model that uses historical commodities sales price, the crop portfolio, production/logistics costs, and expected yield to predict the farmer's operational profits. A higher farmer income results in a higher market score. We expect this features to be useful because a higher operational margin allows for more cash available to facilitate loan repayment.
(3) Financial Score: The financial score is the ratio of the farmer's outstanding indebtedness relative to his/her expected profit. A higher ratio results in a lower financial score. We expect this feature to be useful because it reflects the proceeds available for the repayment of the loan; when this feature is closer to zero, it means that a more significant part of the farmer's
profit is used to pay current debts, and less profit will remain to repay the requested loan on the due date.
(4) Behavior Score: The behavior score is a consumer credit risk score sourced from a credit bureau that is fine-tuned for use in agricultural finance. A higher consumer credit score results in a higher behavior score. Although most of the farming activity signals and farmers' financial life are not captured by credit bureau data, they have valuable information about farmers' consumer behavior, such as paying bills. A good credit bureau score shows that the farmer has good behavior regarding paying bills, even if not related to his/her business. Delays on the payment of consumer loans and bills is an early alarm of financial stress or irresponsibility that will likely to impact the farming business.

### 2.2.2 Farm and Farmer Characteristics ( $n=5$ ):

(1) Ratio of Short-Term Debt to Total Planted Area: This feature represents the ratio of the farmer's outstanding short-term debt, to their total planted area (RSTDTPA). Short-term debt is defined as all debts that must be paid in the next twelve months. Note that, as mentioned earlier, all loans in the dataset have a duration of crop season. Thus, short-term debt includes all debts that the farmer should pay before the due date of the loan.
(2) Ratio of Long-Term Debt to the Farm Area: This feature represents the ratio of the farmer's long-term debt over their total farm area (RLTDFA). Long-term debt is all debts that must be paid in a period longer than one crop season. Longterm debts are generally used for investments in the farm, such as machinery renewal, installing irrigation systems, etc.
(3) Land Lease Costs: This feature represents the cumulative costs paid by the farmer in the crop season to rent the land from a third party; if the farmer owned their land, this value would be 0 .
(4) Credit History: This feature represents the credit history of the farmer with the institution from which they are requesting the loan; the feature may take one of three categories reflecting if the farmer's last loan was: successfully paid,

Table 1: Dataset description; our dataset comprised of 97,235 agricultural loans granted to 31,900, Brazilian farmers sourced from nine of the largest financial and supply chain entities in Brazil (rows A - I).


delinquent, or if the farmer was a new client in the institution's portfolio.
(5) Main Crop: This features represents the main crop grown by the farmer; it has eight categories: soybean, summer corn, winter corn, wheat, rice, Arabic coffee, robusta coffee, sugarcane. Note that the farmer may plant various crops during the loan's life cycle, whereas the one with the most significant area is considered as the main crop.

The first, second, and third quartiles (Q1, Q2, Q3), and the percentage of data that were missing for each continuous feature is described in Table 2. As can be seen, many of the features were missing for a significant fraction of the loans (e.g. the behavior score was missing for $95.9 \%$ of loans). This is consistent with our expectations when dealing with agricultural loans, sourced from multiple institutions. For a given loan, we addressed missing values by assigning the median value for any missing features.

Regarding the categorical variables, there were no missing values. For the credit history feature: 73,621 samples paid their last loan successfully, 1,954 samples were delinquent on the last loan, and 21,660 samples were new farmers in the intuition's portfolio. For the main cropt feature: $66.3 \%$ of the samples were soybean, $21.3 \%$ were sugarcane, and the remaining were summer corn, Arabic coffee, rice, wheat, robusta coffee, and winter corn in decreasing order of sample size.

### 2.3 Assessment of Concept Drift

We assessed the data for concept drift (change in the distribution of the data) across four axes: institutions, crop, state, and year. Concept drift was assessed using the Jensen-Shannon Divergence (JSD) test.

Suppose that $\mathcal{A}=\{$ Institution, State, Crop, Year $\}$. Then, for a given feature $f$, define the following set of JSDs,

$$
\mathcal{J}_{f}=\bigcup_{a \in \mathcal{A}}\left\{J S D_{1 \leq i<j \leq \# a}\left(\mathbf{f}_{a_{i}}, \mathbf{f}_{a_{j}}\right)\right\}
$$

where $\mathbf{f}_{a_{i}}$ is the vector of feature values $f$ for all samples belong to axis $a_{i}$, and $\# a$ denotes the number of unique values in the axis $a$. Then, the $90^{\text {th }}$ percentile of $\mathcal{J}_{f}$ is computed by

$$
P_{90}(f)=\operatorname{percentile}\left(\mathcal{J}_{f}, 90\right)
$$

Table 2: The first, second, and third quartiles of the continuous features in our data, and their missing value percentages. See 2.2 for a description of features.


Table 3: Analysis of concept drift across various features using Jensen-Shannon divergence. The table quantifies how much the distribution changes when samples' characteristics vary along four axes: institution, crop, state, and year. Each cell indicates the number of Jensen-Shannon divergence values above the 90th percentile corresponding to each axisfeature pair. Most data drift occurs in the onstitution axis, suggesting significant shifts in data distribution of samples across institutions.


Subsequently, we determine the total number of JSD values above the $90^{\text {th }}$ percentile are associated with each axis; the count is denoted by

$$
\operatorname{Count}(f, a)=\sum_{j \in \mathcal{J}_{f, a}} \mathbb{1}\left(j, P_{90}(f)\right)
$$

where $\mathbb{1}$ stands for the indicator function, and $\mathcal{J}_{f, a}$ is the subset of $\mathcal{J}_{f}$ in which their axis is $a$. These values for all features and axes are reported in Table 3. As can be seen, most data drift happened along the institution axis. In other words, the greatest shifts in the data distribution occurred when the institution was changed.

Since most data drift is observed when the institution is changed among the samples; thus, the label shift is also analyzed inside each institution. To this end, the Mann-Whitney U test is employed. For all samples inside each institution, they are divided into two subsets of successful and unsuccessful loan payments. Then, the Mann-Whitney $U$ test is computed for all continuous features in these two subsets, and their p-values are reported in Table 4. It can be seen in this table that, for all institutions, there are evident label shifts when analyzing RSTDTPA and financial score features. When an entry is denoted by NA in this table, it means that for the corresponding feature and institution, all samples in the payment and delinquency subsets were identical, and the Mann-Whitney $U$ test cannot be computed; this was true for institutions D, G, H, and I, where the land lease cost was zero.

Also, since the Mann-Whitney $U$ test is only calculable for numerical variables, the $\chi^{2}$ test is adopted for analyzing the label shift in categorical variables. The results are summarized in Table 5. As can be observed, the label shift is noticeable for all institutions when evaluating credit history and main crop features.

Table 4: Inter-institutional label shift analysis using Mann-Whitney U test: significant changes detected in continuous features.


Table 5: Categorical feature label shift analysis by institution using Chi-Squared test: notable differences in 'Credit History' and 'Main Crop' across institutions.


### 2.4 Proposed Approach

In this section, we describe the method used to assess delinquency risk in agricultural loans. As demonstrated in the previous section, the data in the agricultural finance sector suffers from several quality issues: sample sizes are relatively small (see Table 1), many features are missing values (Table 2) and the data distributions between different institutions change significantly (Table 3). To account for these data quality issues, human credit analysts will rely heavily on "experts" to provide apriori beliefs about the importance of the features. These limitations of the data, and the existence of strong priors from experts position Bayesian networks an excellent fit for modeling risk in this domain.

A Bayesian network is a probabilistic graph model which illustrates a set of variables (nodes) and their conditional relationship and dependencies through a directed acyclic graph (DAG) [9, 10]. Each node in the DAG stands for a feature, and the edges between them define probabilistic relationships linking the corresponding features. Dependencies between features have different strengths, and they are measured by conditional probability distributions. Bayesian networks are capable of integrating observed data with prior knowledge to improve predictions under uncertainty. They bring forth an explicit and natural perception of the dependencies among features; thus, they permit comprehensible interpretation and causal reasoning.

The Bayesian network employed in this study is represented in Figure 1, where the credit performance node is the model target. Expert knowledge in the agricultural credit risk domain is extensively utilized in constructing the network to imitate credit analysts' structure of thinking when assessing an agricultural loan. This expertise helps in defining the nodes (variables) of the network and their relationships based on a deep understanding of the actual conditions influencing credit delinquency in agribusiness. Therefore, the proposed network structure is a close representation of the real-world intricacies of credit delinquency scenarios in agricultural loans.
![img-0.jpeg](img-0.jpeg)

Figure 1: The proposed Bayesian network for agricultural loan credit risk assessment.

In the agricultural loan evaluation, the crop type is the origin of the assessment. It has an immediate impact on the agronomic score (expected crop yield production), market score (expected operational profit), financial score (the ratio between the debts and profit), and credit performance. Thus, there are edges between the main crop node and the nodes corresponding to the mentioned features in the network. Also, there is a direct edge between the agronomic score and market score because higher (lower) expected crop yield production implies higher (lower) expected operational profit. Furthermore, there is an edge connecting the agronomic score and credit performance nodes. The market score is linked

to the credit performance as well since the farmer's operational profit amount is directly related to the loan repayment capacity. Additionally, it is connected to the financial score, as the financial score is the ratio between the farmer's debt and profit.

The RLTDPA node is linked to the RSTDTPA and credit performance nodes. Particularly, it is connected to the RSTDTPA because some installments of the long-term debts must be paid within the following twelve months of the loan request date, and they should be considered short-term debts. Note that it does not need to be directly connected to the financial score since it impacts this score indirectly via the RSTDTPA. Besides the main crop node that impacts four nodes directly, the credit history is another important node that impacts three nodes immediately. It is connected to the RSTDTPA because if the farmer did not pay the last loan, he/she is carrying the debts of the previous season to the current season, which should be paid in the following twelve months. Also, it is linked to the behavior score since this score is a measure of the farmer's behavior on consumer loans and daily bill payments. Indeed, when the last season loan has not been paid successfully, it is expected that some consumer loans or bills have defaulted because they were less critical from the farmer's perspective and not related to his/her business. In addition, this node is directly connected to the model target since the last loan performance is an excellent indicator of the subsequent loan output, as observed in the label shift analysis in Table 5.

There is an edge between the RSTDTPA and financial score nodes because the short-term debt is used in the financial score computation. Moreover, the RSTDTPA is directly connected to the credit performance, and it can be seen in Table 4 that this feature has a different distribution between successfully paid and delinquency samples in all institutions. The land lease costs node is only linked to the financial score node since the land lease costs is similar to the short-term debt (it should be paid during the season) and is employed in the financial score computation. The financial score node is connected to the behavior score and credit performance nodes. This feature is a measure of the farmer's indebtedness and describes the farmer's capacity for successful payments. Therefore, besides the credit performance, it impacts the credit bureau data and, consequently, the behavior score. Finally, the behavior score node is only linked to the credit performance node since negative records in the consumer loan and bill payments are early alarms of financial stress, which will impact the farmer's business.
2.4.1 Discretization Approach. To prepare the data for use in a discrete Baysian Network, all continuous features were first discretized. the bins used for the discritization were selected by two credit analysts with over 20 years of collective experience in agribusiness. The thresholds were defined so that when a feature shifted from one category to another, a significant change in the downsteam risk attributable to that feature was expected by the expert. Finally, the prior conditional probability distribution of the credit performance node was defined and validated by the experts. The priors were used to manage the heterogeneity of data drawn from population-wide information and expert assumptions about agricultural credit risk. These priors enabled us to incorporate additional knowledge into the model, filling in the gaps introduced by heterogeneous data. This integration was intended to improve the model's robustness and overall performance in the out-of-distribution generalization.

### 2.5 Baselines

Following a review of the literature, three baseline models were selected: eXtreme Gradient Boosting (XGBoost) [14], L2 penalized Logistic Regression (LR) [13] and Artificial Neural Networks (ANN) [23]. The baselines represent the best-performing modeling frameworks reported in the systematic review by Shi et al. [23].

For the ANN baseline, the architecture consists of an input layer featuring 16 neurons and an output layer with a single neuron. The activation functions chosen for the input and output layers are the rectified linear unit (ReLU) and the Sigmoid function, respectively. This model employs a binary cross-entropy loss function and is optimized using the Adam optimizer. The training process is defined with a batch size of 200 and is run for a total of 100 epochs. For the XGBoost and LR models, hyperparameters were fine-tuned using Bayesian optimization to ensure optimal performance.
2.5.1 Metrics for the Comparison. To compare the models in this work, calibration metrics, such as Expected Calibration Error (ECE) [12, 19], Average Calibration Error (ACE) [12, 17], Maximum Calibration Error (MCE) [12, 19], and Brier score, are reported.

## 3 RESULTS

In this section, the dataset described in Section 2.1 is utilized to predict delinquency events (unsuccessfully repayment within 90 days of the loan's due date). Thus, the target for the model was a dichotomous variable where the delinquency was coded as 1 and repayment as 0 . The model's input has nine features, as explained in Section 2.1. First, the missing values in the dataset are imputed by assigning the median value for any missing features. Then, the continuous features are converted to discrete variables. Various methods can be employed in feature discretization, such as Jenks natural breaks optimization, percentiles, and expert-based discretization. In this study, expert knowledge is used to discretize the feature values, as described in Section 2.4.1. Thus, the bin thresholds for each feature are defined according to expert recommendations. Furthermore, the prior conditional probability distribution of the delinquency event (credit performance) node of the Bayesian network is provided by experts in agricultural loans.

After the imputation and discretization, the Bayesian network described in Section 2.4 is employed to train the model. Among four possible axes of data drift (Institution, Crop, State, and Year), it is observed in Table 3 that the most data drift happened when the institution changed in the dataset. Since the purpose of this study is to show the out-of-distribution generalizability of the proposed Bayesian network, this model is trained on all institutions except one and is tested on the held-out institution. This experiment is repeated so that all institutions are used one time as the test set. Table 6 reports the ECE, ACE, MCE, Brier score values for the Bayesian Network (BN), ANN, XGBoost, and LR models when each institution held out as the test set. Note that all metric values vary between 0 and 1 , and a value closer to zero means that the model is more calibrated.

According to each metric, the number of institutions in which the each model has a superior performance to other models is reported in Table 7. It can be observed that, according to all metrics, the Bayesian networks attained the highest performance on the most number of institutions. After the Bayesian network, on the second

Table 6: ECE, ACE, MCE, and Brier metric values of the Bayesian network, ANN, XGBoost, and LR models on the different held-out institutions.


place, the ANN obtained the best performance on some institutions. For no metric and no institution the XGBoost obtained the best performance, and it is the worst model regarding the calibration metrics. The LR model only achieved the highest MCE on one institution. Furthermore, for each metric in this table, it is shown what percentage of the total population in the dataset is composed by the institutions that each model attains the best performance. As can be seen, regarding all metrics, the Bayesian network outperformed other models on at least $62 \%$ of the total population. On the second place is the ANN, and it showed better performance on almost $30 \%$ of the total population regarding all metrics, except the MCE. In summary, this table showed that in more institutions and a more significant percentage of the dataset, the Bayesian network has superior capability in out-of-domain calibration compared to other employed models for agribusiness delinquency risk assessment.

Table 7: Comparison between the Bayesian network, ANN, XGBoost, and LR models regarding the number of institutions and the percentage of the total population in which they obtained higher ECE, ACE, MCE, and Brier values.


## 4 DISCUSSION

Our analysis revealed that the most pronounced data drift was observed during changes in institutions, followed by state-level changes, albeit with a considerably smaller variation magnitude as detailed in Table 3. The fact that institutional changes encapsulate regional variances suggests that institutional dynamics, rather than merely regional factors, are the primary drivers of this shift. This aligns with the reality of the agribusiness, where different institutions often employ varying business rules and lack standardized practices. Such a finding underscores the importance of ensuring calibration across various distributions.

To address these market realities, a robust modeling approach that can account for market inconsistencies is paramount. We have adopted a Bayesian network model, which allows the design of the model structure and the update with data of the model initially informed with priors. Thus, the Bayesian network can handle different institutional practices and regional variances. This approach ensures that our model remains robust and accurate even when subjected to the inconsistent realities of the market environment.

Given the data drift analysis, we implemented a Bayesian network developed for agricultural loan assessments using our dataset. From the data presented in Table 1, we can draw several key conclusions regarding the performance of the Bayesian network compared to the baseline models across multiple metrics and institutions.

Superior Calibration: The Bayesian network outperforms the other models in calibration, measured by the ACE and ECE metrics. With lower ACE values in $67.86 \%$ of the institutions, this proposed model demonstrates better alignment between the predicted probabilities and observed frequencies on average. Additionally, the Bayesian network's ECE values being lower in $71.71 \%$ of the institutions suggests that, especially in regions of the prediction space with more data, the model's predicted probabilities align closely

with the actual outcomes, providing a more realistic picture of the model's calibration.

Resilience to Drastic Errors: The Bayesian network also stands out in terms of robustness to drastic prediction errors. As revealed by the MCE, the Bayesian network model exhibited the smallest maximum deviation in $62.73 \%$ of the institutions, surpassing the ANN, XGBoost, and LR models.

Overall Predictive Accuracy: The Bayesian network model also achieves superior results in terms of predictive accuracy, as denoted by the Brier Score. With the lowest mean squared difference between predicted probabilities and actual outcomes in $62.0 \%$ of the institutions, the Bayesian network model demonstrates greater overall prediction accuracy.

These findings reaffirm the robustness of the Bayesian network. Despite the diverse institutional practices and regional variances, the Bayesian network model consistently outperforms the ANN, XGBoost, and LR models in calibration, resilience to drastic prediction errors, and overall prediction accuracy across a majority of the institutions. Thus, it validates the effectiveness of our modeling approach in dealing with the market's inconsistent realities.

### 4.1 Future Research Direction

In the domain of credit risk assessment and banking services, the interpretability of model outputs is crucial, serving as a key driver of transparent and informed decision-making. As we chart our future research, our focus will be on expanding the interpretability of the Bayesian network model and assess how variations in feature importance impact model performance. Owing to the graphical structure of the Bayesian network, it has inherent potential for delivering clear interpretations. An essential part of our investigation will be examining the variability of feature importance across institutions to gain insights into unique institutional influences on credit risk.

We also plan to evaluate various network structure learning methods, aiming to optimize the capture of intricate dataset relationships. Furthermore, we will scrutinize the out-of-domain generalization capabilities of our Bayesian network model concerning data drift in terms of latent variables. Importantly, our research efforts will not only enhance our model's predictive accuracy and interpretability but will also contribute to private investment decision-making in agricultural finance. By identifying the factors that may impact credit risk performance, we can enable more informed and effective investment decisions and thereby contribute to the stability and growth of agricultural finance.

## 5 CONCLUSION

Our research presents compelling evidence for the superiority of the Bayesian network model in agricultural loan assessments. Notably, this model exhibits superior calibration, resilience to drastic prediction errors, and overall predictive accuracy, as compared to other benchmark models like the Artificial Neural Network (ANN), extreme Gradient Boosting (XGBoost), and Logistic Regression (LR). The ability of the Bayesian network to handle different institutional practices and regional variances, despite the lack of standardization and the presence of data drift, is noteworthy. The network
outperforms its counterparts across most institutions, affirming its robustness and efficacy.

As we plan our future research, we aim further to research the interpretability of the Bayesian network model and how variations in feature importance impact model performance. Indeed, unique institutional influences on credit risk could offer valuable insights. Additionally, we plan to assess out-of-domain generalization capabilities of our model, while exploring various network structure learning methods. Our overarching goal is to enhance our model's predictive accuracy and interpretability. The resulting insights will contribute to improved decision-making in agricultural finance and bolster its stability and growth.

## ACKNOWLEDGMENTS

The authors thank Traive Inc. for funding this research. We thank Traive's agricultural credit risk experts, Luis Lapo, Antonio Hildenberg, and Rafael Arruda, for their collaboration and insights. We also thank the data engineering team on this project: Abhay Sarda, Arthur Yuan, Alan Martins, Juscelena Lopes, and Luis Campos.
