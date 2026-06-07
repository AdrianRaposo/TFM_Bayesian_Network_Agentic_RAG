# FLOOD DAMAGE ASSESSMENT: A REVIEW OF MULTIVARIATE FLOOD DAMAGE MODELS 

Sumiliana Sulong and and *Noor Suraya Romali<br>Faculty of Civil Engineering Technology, Universiti Malaysia Pahang, Gambang, Pahang, Malaysia.

*Corresponding Author, Received: 24 Aug. 2021, Revised: 11 Feb. 2022, Accepted: 27 March 2022


#### Abstract

Nowadays, more emphasis is given to flood risk management for dealing with flood disasters. To assess flood risk, damage from a flood is a crucial component to be considered. Flood damage function is a commonly accepted approach for the estimation of flood damages worldwide, where it combines the element of hazard, vulnerability, and exposure. However, this method usually considers only the flood depth and the type of buildings at risk. The effect of other flooding conditions (impact parameters) and the resistance parameters to the degree of flood damages are normally neglected. Flood risk assessment should cover all damage dimensions to obtain an extensive description of flood damages. Multivariate damage modeling can be applied to examine the relationship between flood damages and other flood influencing factors. This paper presents a review of methods applied to generate multivariate flood damage models, which includes the Multiple Linear Regression (MLR), Bayesian Network (BN), Artificial Neural Network (ANN), and the Random Forest (RF) analysis. Moreover, the multivariate models are also found capable of generating synthetic data to counter the problems of flood damage data scarcity experienced by developing countries. Identifying damage influencing factors, especially resistance parameters is important as a comprehensive flood damage model based on the local conditions and property characteristics of the study area can assist in the future damage assessment works, as well as offer decision-makers with an indispensable tool for managing strategies related to flood risk.


Keywords: Flood risk, Flood damage assessment, Flood damage influencing factors, Multivariate analysis

## 1. INTRODUCTION

Floods are the most prevalent natural catastrophes that may endanger lives, destroy property, disrupt social and economic activities, and the environment and ecology in both rural and urban regions. Global climate change and rapid urbanization are explicitly identified as major catastrophe hazard drivers in the Sendai Framework 2015 - 2030 [1]. Although the boundless focus is positioned in executing structural flood mitigation approaches, non-structural measures including flood risk assessment still need to be extensively managed, since comprehension of the damage evaluation remains inadequate [2]. Flood risk assessment is concerned with the combination of the hazard and its vulnerability. Estimation of flood hazard combining two essential flood characteristics, namely flood extent and flood depth while the vulnerability is a notion that includes exposure and refers to the impacts of floods. The primary tools in visualizing flood risk assessment are the flood hazard map, flood damage assessment, and flood vulnerability map [2] - [4].
Flood vulnerability assessments have become increasingly relevant all around the world. Meanwhile, flood damage assessment is one of the main tools of flood vulnerability assessment. Its framework serves as a decision support tool for
decision-makers who must prioritize and execute best practices in flood risk reduction. Flood damage refers to all varieties of damages produced by floods and is categorized into two groups: tangible and intangible damages [3]-[7], as summarized in Table 1. Tangible damages may be quantified in monetary terms, while intangible damages are often measured using non-monetary metrics such as the ecosystem, the environment, health, and psychological impacts. Furthermore, each group of damage is classified further as either direct or indirect damages [9].

Penning-Rowsell and Chatterton [10] in the United Kingdom and Smith [11] from Australia, were among the pioneer researchers on flood damage assessment. Although flood vulnerability assessment studies have begun over 40 years ago, it is still new in developing countries. Many works are to be done, which relate to several issues, such as limited knowledge on the factors influencing vulnerabilities, damage data scarcity, and uncertainties in flood damage analysis [4], [12]. Past studies on flood damage assessment typically deliberated on the relationship between flood damage and hydrological impacts parameters, such as flood depth, which has been regularly chosen as the most appropriate flood damage variable [10]. The variation of flood damages to properties could not be explained based on flood depth alone [6]. The outcomes were uncertain and did not

significantly affect the total damage cost predictions. Therefore, proper estimation of flood damage is challenging and requires careful consideration of some effects on the socioeconomic and the property characteristics to the degree of flood damage, especially for loss estimation in monetary terms.

Many studies have shown that the influence of various resistance parameters should be given more attention as it affects the accuracy of flood damage and makes the outcomes adaptable for other areas and times [13]. Apart from that, with appropriate modifications, flood damage assessment can also be made on other assets and properties such as building contents in residential, commercial, and industrial buildings [11]. Therefore, the study on the relationship between socio-economic conditions and property characteristics that may affect the extent of flood damage should prioritize.

Table 1 Categories of flood damage


This paper intends to deliver a concise review of the multivariate flood damage models that may aid in establishing a framework for assessing the
flood damage by considering the effects of damage factors from multiple dimensions. To this end, a review of the multivariate flood damage assessment framework is provided to improve the understanding of flood damage estimation.

## 2. FLOOD DAMAGE ASSESSMENT

Throughout recent decades, risk-based methods have been progressively acknowledged and utilized in managing flood risk. Flood damage assessments are an important component of flood risk assessment, and the outcomes offer decisionmakers essential tools for preparing more effective approaches to reducing risk [12]. Consequently, the current understanding of flood impacts and their outcomes can be improved towards developing a more reliable damage estimation, and efficiently reducing flood risk. The effectiveness of flood damage assessment depends on its framework, which encompasses hazard, vulnerability, and exposure [12]. The flood damage assessment concept has been summarized in Figure 1. It has been adapted by numerous studies in both developed and developing countries and has progressively obtained global reception as the standard approach for assessing urban flood damages in urban areas. The key differences among the existing methodological frameworks for damage assessment are involved to the types of flood damage to be considered, spatial scale approach, analysis of exposures and risk elements, parameters influencing flood damage, and methods of the flood damage model [5], [15], [16], [17].

Three main ways of assessing the flood damage are the unit loss, the flood damage function curve, and the multivariate modeling approach [5], [15], [16]. The unit loss method refers to the direct computation of loss to individual properties, which is then combined to create a total loss number for the event under consideration [2]. The damage function curve approach is the more accepted approach for flood loss assessment due to its simplicity [18], [19]. In the curve method, direct damage is based on water depth with either the percentage of the total damage of the affected element at risk (relative damage curve) or loss in monetary terms (absolute damage curve) [7], [17]. Recently, due to the consideration that the flood damage could not be explained by the hydrological impact alone, the establishment of a multivariate model is an increasingly popular method in modeling flood damage assessment. The multivariate flood damage model has utilized the relationship among the hydrological characteristics (magnitude of the hazard), property characteristics and socio-economic elements (exposure), and flood damages (vulnerability) [12], [17]. In this approach, several techniques were applied to build flood

damage models using statistical techniques such as Multiple Linear Regression (MLR), Bayesian Network, Artificial Neural Network (ANN), and Random Forest (RF) [15], [20], [21], [24]-[27]. The outcome of the models allows the confidently determining which factors are significant most and how they influence each other. However, multivariate flood damage models that consider various damage influencing parameters rather than the ones considered in flood depth damage functions can only be effectively developed if a sufficient and detailed empirical dataset is available [22].
![img-0.jpeg](img-0.jpeg)

Fig. 1 The concept of flood damage assessment

## 3. MULTIVARIATE FLOOD DAMAGE MODEL

### 3.1 Flood Damage Influencing Variables

Malgwi [14] asserted the necessity to identify patterns and interactions among multi-parameters that impact various damage categories to develop reliable flood damage models that represent the relationship between flood damage and resistance parameters such as socioeconomic and property characteristics. The influencing factors of flood damage may be divided into two categories: impact (hazard) parameters; and resistance (vulnerability) parameters. Impact parameters that influence flood damage include the hydrological impact such as flood depth and flood duration. Meanwhile, the resistance parameters include property characteristics, precautionary measures, socioeconomic circumstances, flood warning, and disaster preparedness as shown in Table 2. These damage influencing parameters must be included in the construction of reliable flood damage modeling. The multivariate flood damage model has demonstrated an improved forecast accuracy, allowing for validity with any flood occurrence and
diverse locations in flood damage assessments [13], [21].

Table 2 Flood damage influencing factors


### 3.2 Multivariate Regression Analysis

Flood damage models have been established with a multivariate regression analysis approach relating more than one influencing flood variable to the magnitude of flood damages such as the impact parameters and the resistance parameters [15], [20], [21], [24]-[27]. Table 3 shows the description of the techniques used by the researchers in developing the multivariate flood damage models, while the damage influencing factors involved in the modeling are shown in Table 4. The MLR, BN, ANN, and RF techniques have been used in establishing the multivariate flood damage assessment model to identify the importance of flood damage influencing parameters and calculating the flood damage estimation. The description of the techniques is further elaborated in the following sections.

The development of multivariate regression flood damage models required large amounts of observed data, and the characteristics of the model empirically approach and site-specific [17], [21], [24], [26]. Furthermore, the robustness of the results became increasingly improved for the larger empirical data sets used for model training because of being less prone to outlier-induced aberrations [27]. Although applying these statistical multivariate regression techniques in flood damage assessment models can create more reliability and improve the established flood damage model, it remains challenging with the data scarcity problems [24]. A framework of multivariate flood damage model as shown in Figure 2. The framework starts with the identification of flood damage influencing parameters before the development of the

multivariate flood damage model and finally the estimation of flood damage [13], [14].
To train the models, the flood damage influencing variables are structured into dependent and independent variables which include flood damage data, flood impact variables, and resistance variables. The regression analysis will be carried out using the selected regression techniques. Generally, the outcomes of the model are the relative predictive value (damage factor or damage value) and important flood damage influencing parameters. The model performance and validation are then carried out to confirm the estimation's reliability to be accepted for decision making [12].

### 3.2.1 Multiple Linear Regression

MLR has been commonly employed to aid in flood damage assessment. Win Zin [17] established a flood loss estimation model of direct damages to residential buildings in Bago, Myanmar, using the multiple linear regression with an extension of Ordinary Least Square (OLS) to determine the most influencing factors to the flood damage. This model incorporates more than one factor of hazard and resistance variables that affect damage, such as the depth of floodwater, the duration of flooding,
building material, age of the building, building condition, number of stories, and flood level. The linear regression analysis techniques consider the linearity independence, homoscedasticity, and normality of the input data. These procedures were applied to estimate flood damage with a linear functional form equation based on the coefficient value of each input variable from the regression result. The coefficient of determination ( R squared) value and p -value ( $5 \%$ significance level) were used to measure the factors influencing measures the significant influencing factors. Yu (25) also created a flood damage assessment model with MLR techniques using an extension of the Ordinary Least Square (OLS) approach to residential, commercial, and agricultural sectors for the 2012 flood event in Gunsan City, Korea. OLS is a process in which is a linear line is used to estimate the relationship between the multivariables. On the other hand, Wagenaar (24) applied MLR techniques to compare with the other Statistical regression techniques to develop a reliable flood damage assessment model.

Table 3 Summary of multivariate regression techniques


Table 4 Multivariate flood damage models techniques and variables.


### 3.2.2 Bayesian Network (BN)

Wagenaar [24] adapted the BN technique in estimating flood damage. The BN technique is a probabilistic graphical model that represents a set of random variables and provisional dependencies in a Directed Acyclic Graph (DAG) structure. Every variable in the network may be perceived as a preceding probability distribution, and dependencies between variables are represented with edges representing joint probability distributions. The edges in the BN are focused on the influence of one variable that flows to the other. From this network, extrapolation can be performed to apply knowledge of one variable for predicting other variables. It demonstrates the versatility and value of combining multi-parameters to predict system behavior for multiple data output. The ability of the BN technique to assimilate data allows them to integrate several multi-parameter simulations from developed models for a combined assessment of many scenarios and characteristics. One of the most significant advantages of employing BN is due to its ability to analyze correlations between variables using data contained in conditional probability tables. Because conditional probability tables are designed with the connected relationships between variables, the BN may also be used to answer queries regarding sector behavior [28]. By means, BN may quantify the distribution obtained in resistance parameters and assess the flood damage with the induced hazard characteristics. However, the disadvantage of the BN technique is its poor performance in cases with a limited data set and poor data quality [24].

### 3.2.3 Artificial Neural Network (ANN)

Rumelhart [29] pioneered the ANN approach, which was inspired by the way the human brain analyses information. and discover the connections between variables in a data collection. The model constructed using ANNs is composed of numerous (hidden) layers of neuron-like processing units coupled in a network-like model. Each neuron is linked to every other neuron in the layer immediately before and following it. Coefficients are applied to measure every value passing through the neuron. The coefficients of the neurons are computed by an optimization approach that reduces error on the training data set. Amadio [26] applied the ANN techniques to evaluate flood damage to estimate the potential economic costs of flood events to residential buildings in Italy. In the study, apart from considering the flood depth, the contribution of multi-variables is considered, such as the detailed hazard data and comprehensive vulnerability data involved in building characteristics. ANN models are excellent for a probabilistic analysis, i.e., a procedure in which the variation in input variables may be explicitly represented in a model and may include the quantitative analysis of enormous quantities of data. Another benefit is ANN of the model is not restricted to the range of normalized values.

### 3.2.4 Random Forest (RF)

RF technique is widely used in multivariate flood damage estimation. Regression analysis is mainly used in understanding the relationship between dependent variables (hazard) and independent variables (vulnerability). Malawi [20], Carisi [21], Wagenaar [24], Amadio [26] and Sieg [27] adapted RF techniques to relate multi-variables for estimating damage. This regression tree-based approach generates data for each tree using a bootstrapping resampling method [24]. In each tree, branches are formed by splitting the dataset based on binary recursive partitioning. The input data sample corresponds to the root node of a single tree and is split into subsamples that form the tree's nodes. The RF algorithm does not use all

explanatory variables for each tree, but it seeks the best splits within a limited number of sampled explanatory variables. The number of sampled features is the square root of the data set, a total number of features. The best splits refer to regression trees that split the training data to slight variation within the resulting leaves. The mean value of the predictions from each regression tree is the anticipated value for the entire RF model. Thus, the more decision tree an RF model includes, the more robust and accurate its result becomes. The correlations coefficients matrix is used to support the interpretation of the variable importance. In the study by Wagenaar [24] and Amadio [36], the RF model performed well in estimating the flood damage due to its capability to evaluate the relative importance of each independent variable in the bagging tree building procedure.
![img-1.jpeg](img-1.jpeg)

Fig. 2 The proposed framework for the multivariate flood damage model

### 3.3 Model Performance and Validation

Flood damage model performance and validation are two essential phases in developing
flood damage estimation [13]. The robustness performance of the model ensures the completeness
and correctness of the estimation. At the same time, validation establishes its credibility to determine the degree to which it can reasonably represent the assessment [13]. The validations are crucial for testing the reliability of the models' predictions for evaluating damage and ensuring the predictive outcome's precision [13], [21]. The validation methods discussed by researchers include empirical data validity (using historical data), comparison with alternative models (or cross-validation), and predictive validation using error estimation analysis (or internal validation). These methods are summarized in Table 5. The review of methods to validate the flood the multivariate flood damage model revealed that most of the researchers used the validation using empirical data from another flood event or a subset of the training data and compared their error estimation indicators to evaluate the performance of the models [13], [17], [20], [21],[24], [26], [27].

The precision of the model is tested by Mean Absolute Error (MAE) and Mean Bias Error (MBE) and the residual variation of the model is checked by the Root Mean Square Error (RMSE) and Coefficient of Variation (CV).

Table 5 Validation method


On the other hand, the bi-variate model (function curve) was also developed to compare with the multivariate flood damage model as done by Nafari [13], Malgwi [20], Carisi [21]. The MAE, MBE, RMSE, CV, and HR are calculated for the validation dataset as shown in Table 6.

## 4. CONCLUSIONS

Nowadays, flood vulnerability assessment has become increasingly important around the world. Several previous studies had utilized the damage function approach in estimating flood damage.

Table 6 Model performance metrics


est - predicted value, obs - observed value, $\boldsymbol{n}$-population, $\boldsymbol{\sigma}$ standard deviation, $\boldsymbol{\mu}=$ mean value of the model residual, $\boldsymbol{h}$ number of hit value, $\infty$ - infinity, LV- Lower value, UV - Upper value and

PP - Perfect prediction value.
Source : Nafari [13], Malgwi [20] and Sieg [27]

However, such a method relies only on a deterministic relationship between the type or use of properties at risk and the depth of the floodwater. The effects of other flood influencing parameters such as the natural/socio-economic conditions and the resistance parameters to the degree of flood damages are usually neglected. From the literature, it was discovered that the recent estimation method which applies multivariate flood damage models, has effectively related flood damage with other influencing factors such as impact variables (e.g., flood depth velocity, frequency, water contamination, and velocity) and resistance variables inclusive of permanent resistance (e.g., emergency measures, precautionary measures, building characteristics - age of the building, building material, and building size) and temporal situation (e.g., preparedness and socio-economic status - ownership status, household income, and educational level). Furthermore, the multivariate models are also capable of generating appropriate new data points to counter the problem of insufficient or missing data. This would be beneficial to develop countries that experience issues of data scarcity in performing damage assessment works.

## 5. ACKNOWLEDGMENTS

The authors would like to thank the Ministry of

Education of Malaysia (MOE) for providing financial support under fundamental research grant No. FRGS/1/2019/TK01/UMP/02/2 (University reference RDU1901155) and Universiti Malaysia Pahang for technical support and encouragement.
