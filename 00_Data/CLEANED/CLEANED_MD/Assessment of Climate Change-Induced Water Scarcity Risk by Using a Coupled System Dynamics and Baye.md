# Assessment of Climate Change-Induced Water Scarcity Risk by Using a Coupled System Dynamics and Bayesian Network Modeling Approaches 

Sara Dehghani ${ }^{1} \cdot$ Alireza Massah Bavani ${ }^{1} \cdot$ Abbas Roozbahani ${ }^{2} \odot \cdot$ Oz Sahin $^{3}$<br>Received: 12 December 2023 / Accepted: 26 March 2024 / Published online: 10 April 2024<br>© The Author(s) 2024


#### Abstract

The water scarcity risk induced by climate change is contributing to a sequence of hydrological and socioeconomic impacts. Certain numbers of related impacts are locked in already and are expected to be much greater in the future. So, there is still a lack of understanding of its dynamics, origin, propagation, and the mutual interaction of its drivers. In recent years, several model-based approaches have been introduced to tackle the complexity, dynamics, and uncertainty of water scarcity specifically. However, the coupled modeling while addressing different aspects of the risk of water scarcity under the climate change scenarios has been rarely done. For bridging this gap, in this research, the combination of complementary System Dynamics modeling and Bayesian Network was applied to Qazvin Plain in Iran with five AOGCM models under two Shared Socioeconomic Pathways (SSP) scenarios (126 and 585). Key findings of this research show: 1) Baseline risk assessment indicates a low probability of water scarcity; however, in the future 30-year time horizon with continuous change in hazard, vulnerability, and exposure for SSP126, the risk fell in the extreme category with an average probability of $41 \%$. Under SSP585, the risk varies between extreme and high categories with an average probability of $47 \%$. 2) Economic development, particularly regional gross domestic product (RGDP) in 20452054 in SSP585 can diminish the negative projected consequences of climate change and therefore investments in adaptation policies could offset negative consequences, highlighting the role of economic growth in climate resilience. 3) It is projected that crop yield and income will receive the largest negative effects due to cutting back the agriculture area. 4) Considering the interplay of climate change, economic development, and water extraction policies is essential for the design, operation, and management of water-related activities. The proposed integrated methodology provides a comprehensive framework for understanding climate change-induced water scarcity risks, their drivers, and potential consequences. This approach facilitates adaptive decision-making to address the evolving challenges posed by climate change.


Keywords Integrated risk assessment $\cdot$ Water scarcity $\cdot$ Climate change $\cdot$ System dynamics $\cdot$ Bayesian network

[^0]
[^0]:    Extended author information available on the last page of the article

# 1 Introduction 

Food production, water insecurity, and reduced quality and quantity of crop yields in farmlands are among the major challenges driven by climate change today on the global and national levels (Abdelfattah 2021). Climate change influences water availability as well as water demand in many regions, through temperature rise and precipitation variation. These changes consequently affect the hydrologic cycle which in turn influences water availability (Stocker et al. 2013). In contrast, other issues such as population growth, water resource mismanagement, and economic development increase water demand significantly over the next two decades in all three components, industry, domestic, and agriculture (Boretti and Rosa 2019).

Although the direct impact of climate change-enforced risk is local, it can propagate through entire sectors as various parts of the water system are interrelated, which forms the secondary risk (Dolan et al. 2021). Measuring, monitoring, managing, and reporting this risk is crucial for a robust planning scheme.

In general, risk is referred to the potential for adverse consequences and is a function of three components: i.e., hazard, vulnerability, and exposure (Reisinger et al. 2020). This study addresses the risk of water scarcity defined here as a shortage in the availability of freshwater relative to demand (Taylor 2009). This risk is addressed by many researchers in the way that the whole system is exposed, broken down into smaller parts, and the risk assessed individually. The main focus of those research studies is on either physical, hydrological water scarcity on economic loss (Zhao et al. 2019; Dallison et al. 2021), social (Taylor 2009), environmental (Pittock and Lankforf 2010), or health issues (Terzi et al. 2021). However, they used the risk concept not as an integrated assessment.

The risk of water scarcity induced by climate change has a multidimensional context (Gain and Giupponi 2015) and hence, combining the representation of components with an integrated model emphasizing linkage is essential (Malmir et al. 2022). Thus, a method for simulating non-linear, dynamic, and complex systems with often time delays should be employed to provide users with the cause and, the context of the system's risk drivers (Bavandpour et al. 2021). Accordingly, System Dynamics modeling (SDM) is selected to simulate the water system in the region under study. This System Dynamics simulation amplifies understanding of the characteristics of risk problems except for the inherent uncertainty of future projections. The complexity and uncertainty challenge the importance of model-based decision making. Uncertainty lies in emissions of greenhouse scenarios, socioeconomic development and impact, and water management policies (Zare et al. 2019; Reisinger et al. 2020). To address the challenges of uncertainty, complexity and dynamic character of water scarcity risk and considering that this risk affects SDM coupled Bayesian Network (BN) implications, was analyzed.

For quantification of uncertainty and decision-making under uncertainty, BN has been used. BNs are probabilistic graphical models representing a set of random variables and their conditional interdependencies via a Directed Acyclic Graph (DAG) (Pearl 1988). BN is also a flexible framework with learning capability that increases the efficiency of analysis for policymakers or decision-makers, and is a powerful tool for demonstrating the probabilistic behavior between risk events that can quantify risks and correlate them (Bozorgi et al. 2021). However, the application of BNs for climate change faced some limitations; representing dynamics and feedback effects among the variables. The directed acyclic graph restriction of the BN is critical. No calculus has been developed for coping with feedback loops (Bertone et al. 2015; Sperotto et al. 2017; Punyamurthula 2018).

Moreover, hazards, exposure, and vulnerability may each be subject to uncertainty in terms of likelihood of occurrence and each may change over time due to socio-economic changes and human decision-making. BNs have been utilized in climate change adaptation and risk management studies, but their inability to represent feedback loops and dynamic complexities poses challenges (IPCC 2021). Conversely, SDM captures system dynamics holistically, considering interactions among interconnected subsystems (Sterman 2000). By combining different approaches, it is possible to leverage their strengths and overcome limitations. (Moallemi et al. 2018), this study aims to dynamically assess water scarcity risk, overcoming the limitations of each modeling tool and capturing the uncertainty, feedback, and dynamic aspects of climate change risk comprehensively and also provides an effective means of conceptualizing risk drivers and conducting probabilistic risk assessment (Punyamurthula 2018).

This article focuses on the coupling SDM-BN as an application of multi-model design for comprehensive perspective in decision making for dynamic complex systems with plausible futures. The coupled SDM-BN has not been discussed before. This study is a continuation of previous research (Dehghani et al. 2022). Here, we describe how climate change affects water supply and demand systems in terms of water scarcity risks. The risk of water scarcity is defined here in the agriculture sector and will be studied throughout the whole water system in detail here.

The proposed SDM-BN methodology is tested in the Qazvin Plain (QP) in Iran, which now suffers from water scarcity and groundwater depletion, mainly due to agricultural development.

# 2 Study Area 

QP is located in mid-northern Iran (latitude:36.269363, longitude: 50.0032) with an area of approximately $9550 \mathrm{~km}^{2}$ (Fig. 1). It has semi-arid climate with the precipitation about $256 \mathrm{~mm} /$ year and the annual average air temperature about $13^{\circ} \mathrm{C}$. Surface flows and floods originating from the surrounding mountains are the primary sources nourishing underground aquifers, rivers, and streams in the plain. Water for domestic, services, industry, and agricultural sections is supplied by surface water (rivers) and groundwater (wells, aquifers, and springs).

Surface water withdrawal is minimal compared to groundwater pumping in the Qazvin Plain, primarily because of the limited annual discharge of ephemeral streams. Surface water is exclusively allocated to irrigating croplands and orchards. There is also inter-basin water transfer from Taleghan Dam in Tehran, which supplies the water for agriculture.

Fig. 1 Schematic view of QP and its geographical location
![img-0.jpeg](img-0.jpeg)

Precipitation does not fall evenly over the plain but in highly localized spots. The main source of groundwater supply is the Qazvin aquifer with an area of $3592.4 \mathrm{~km}^{2}$ (Fig. 1).

Qazvin plain allocated 450,000 (ha) of agricultural area in Iran. The main consumer sector of water is agriculture. More than $90 \%$ of the total water withdrawal is used for the agriculture sector. However, due to unsustainable surface water storage, unauthorized wells and uncontrolled harvesting about $75 \%$ of water is extracted from groundwater storage. Owing to traditional irrigation methods, the irrigation efficiency varied between 15 and $31 \%$ from 2001 to 2016 (IWRMO 2014). Therefore, a high amount of water is lost in this sector. Climatic factors such as less precipitation and higher temperature affect water scarcity in QP and lead to average of 1.5 m yearly reduction in the groundwater's level. Continuing this trend depicts a serious water shortage with demand exceeding water availability, especially in the agriculture sector.

# 3 Materials and Methods 

As shown in Fig. 2, the study includes the following: a) System Dynamics Model development of the region using 2001-2016 period for calibration and the period 2025-2054 period for projection, b) downscaling and bias correcting of AOGCM (Atmosphere/Ocean General Circulation Model) output, c) preparing multi-dimensional uncertainty scenarios, d) defining risk drivers and extracting these indicators from SDM, e) developing BN based on risk indicators in every ten years of SDM modeling, and f) calculating isk in three 10-year time steps in the future.
![img-1.jpeg](img-1.jpeg)

Fig. 2 Research flowchart

# 3.1 SDM 

SDM in this study was constructed based on three interlinked sub-systems:

1. Hydrological: this subsystem includes hydrological cycle variables such as precipitation, runoff, and groundwater. This part constitutes the water supply for domestic, services, industry, and agriculture based on their water allocation priorities.
2. Socio-economic: his sub-system captures the social components such as employment in the QP, population, social welfare, and water demand for users in the domestic and services sector, as well as economic aspects such as income and regional growth domestic product.
3. Agricultural: this subsystem encompasses seven important crop types and orchards in the QP, namely cereals, forage, herb, vegetables, industrial, and two orchards of grapes and walnut, with their evapotranspiration, land area income, yield, and costs. Here, the term "delivery rate" is defined which is representative of the water scarcity in the QP and defined as the ratio of agricultural water demand to the available water for agriculture. The delivery rate also influences the actual land area, and depicts that the available water can determine the actual farmland area in the region (Fig. 3).

SDM construction was done as follows: (1) articulating the problem and defining the system boundary; (2) developing a conceptual model or causal loop diagram/s (CLD) of the system; and (3) developing a stock and flow diagram (SFD) to build a simulation model; After calibration of SDM, the risk indicators were extracted from the model to be introduced as input to BN.
![img-2.jpeg](img-2.jpeg)

Fig. 3 Contributed subsystems to SDM of QP

# 3.2 Future Scenarios 

### 3.2.1 Construction of Climate Change Scenarios in the Future

Global climate models, also known as atmosphere-ocean general circulation models (AOGCMs), numerically simulate climate variables under different greenhouse gas emission scenarios. AOGCMs contain significant uncertainties and the IPCC recommends that this uncertainty should be managed in climate change studies (IPCC 2021). Multi-model ensembles must consider both robustly quantified uncertainty and model's ability to reproduce observations (Brunner et al. 2019).

In this study the impact of climate change was evaluated on the monthly temporal scale for precipitation $(\mathrm{Pr})$, maximum and minimum temperature $\left(\mathrm{T}_{\max }\right.$ and $\left.\mathrm{T}_{\min }\right)$, respectively. Five AOGCM models, namely: GFDL, INM, IPSL, MPI-ESM1-2, and MRI.MRI-ESM2-0 (esgf-node.llnl.gov) used under two shared socioeconomic pathways (SSPs) of 126 and 585 (Riahi et al. 2017). The two scenarios have a significant difference in terms of CO2 emissions, with SSP126 representing a low emissions scenario based on sustainability, while SSP585 predicts a high emissions scenario that achieves strong economic growth in part through fossil fuels. These two scenarios capture a range of possible future states and better predictions of the future to highlight the uncertainty (Marchessaux et al. 2021).

Because of the coarse resolution of AOGCM output for regional assessment, the output of the models was downscaled and bias-corrected using the multivariate bias correction (MBC) for Qazvin Synoptic Station from 1985 to 2014. This method uses climate model simulations of multiple climate variables (Cannon 2016). It is a multivariate generalization of quantile mapping that transfers all aspects of an observed continuous multivariate distribution to the corresponding multivariate distribution of variables from a climate model (Cannon 2018). The bias correction was accomplished for precipitation and temperature using the MBC package in the R programming language.

Long-term average changes of precipitation and temperature in different AOGCMS in the future period in comparison to the historical period were calculated using, Eqs. (1) and (2) (Wilby and Harris 2006):

$$
\begin{gathered}
\Delta R_{i}=\left(\frac{\bar{R}_{A O G C M f u t}}{\bar{R}_{A O G C M h i s t}}\right) \\
\Delta T_{i}=\bar{T}_{O G C M f u t}-\bar{T}_{A O G C M h i s t}
\end{gathered}
$$

where $\Delta R_{i}$ is the ratio of precipitation in a future period $\left(\bar{R}_{A O G C M f u t}\right)$ to a historical period $\left(\bar{R}_{A O G C M h i s t}\right)$ in AOGCM models and $\Delta T_{i}$ is the difference between temperatures in the future period $\left(\bar{T}_{A O G C M f u t}\right)$ and the historical period $\left(\bar{T}_{A O G C M h i s t}\right)$ in AOGCM models.

### 3.2.2 Groundwater Management Scenarios and Economic Development

Water mismanagement, maladaptation strategies, and some other factors like economic development can exacerbate the water scarcity situation. To consider how groundwater withdrawal strategies will influence water scarcity, three groundwater withdrawal capacities (1400, 1200, and 1000 MCM) were applied in 10-year time steps of modeling using management strategies plans for QP. All these capacities depict a decrease in groundwater withdrawal in comparison to the baseline period (2001-2016) which

is approximately 1700 MCM , to see the effect of reducing groundwater withdrawal on water scarcity.

To represent the role of economic development on water scarcity, a change in RGDP was considered. The RGDP assumed $2.7 \%$ and $4.6 \%$ in the 2010- 2040 period for SSP126 and SSP585, respectively. For the 2040-2100 period, the RGDP assumed $4.1 \%$ and $3.5 \%$ for SSP126 and SSP585 respectively.

# 3.3 Risk Indicators 

Risk is assessed in the agriculture sector as being due to the high dependence on water, and risk receptors are the farmers' incomes.

The selected indicators represent physical, social, economic, institutional, and infrastructural dimensions. The process of indicator selection is guided by several criteria: 1) understanding of the water scarcity and propagating its influence in the water system; 2) consideration of mutual interaction and statistical correlations between engaging parts; 3) evaluation of data quality of the selected indicators and their drivers; and 4) input from experts and stakeholders within the region. These proxies should be the best representative of water scarcity risk in the region.

Table 1 provides an overview of the selected indicators, focusing specifically on the risk of water scarcity within the agriculture sector, which is primarily characterized by availability shortages. These indicators offer insights into the trends of key variables influencing water scarcity risk in agriculture. It is important to note that the datasets utilized may feature differing measurement units. However, employing ratios to define indicators can yield unitless metrics that facilitate aggregation and comparison across different datasets.

### 3.4 Bayesian Network

To model risk using the BN, risk components are considered a node, and complex relationships between the risk components are quantified using conditional probabilities (Fenton and Neil 2012). In a BN, the probabilistic relations among the nodes are determined by the product rule Eq. 3.) The product rule allows the calculation of any member of the joint distribution of a set of random variables (Nielsen and Jensen 2009):

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \operatorname{Parents}\left(X_{i}\right)\right)
$$

where $X_{i}$ : is the $i$ th variable in the network and nodes are representatives of variables in the network that connect using arcs. These arcs demonstrate the relationships between parent and child nodes. The relationships between nodes are also depicted through the conditional probability table (CPT).

BNs can be expressed in two types named discrete and continuous nodes. Discrete nodes are for non-numerical data, whereas times series data are expressed as continuous data. The third type of BN is called hybrid BN which models together in both discrete and continuous nodes. Since risk nodes were evaluated descriptively and the rest had numerical series, the hybrid BN was used in this study.

Table 1: Indicators representing the risk of water scarcity in the agriculture sector


# 3.4.1 Constructing BN 

For building up the BN, the quantification of the CPTs (conditional probability table) is based on learning from historical data between 2001 and 2016. Concerning the indicators extracted from SDM, the state values were based on historical data. Seventeen years of observation are available based on running the SDM.

The BN network includes seven parent nodes and three child nodes. The relation between child and parent nodes is described through the equation and weighted parent nodes resulted in child nodes. The weighting of parent nodes is done through the Shannon Entropy method (Shannon and Weaver 1949). After importing the data, the learning process is performed. The learning of the BN is done by given data in the form of training cases. Each case represents an object situated in the system and this case supplies value for a set of variables in BN. Each variable is a node in BN and the possible value for each node becomes a node state.

The learned net can be used to analyze a new case that comes from the same system as the training cases.

The steps for the posterior probability of BN proceeds are as follows:

1. Indicators are gained and state probabilities are calculated by historical data for the period 2001-2016.
2. The estimated Dirichlet distribution is transferred to BN with discretized variables with the associated states.
3. The generated CPTs are used for future risk evaluation and, by new findings from SDM in each time step, the BN updates the probabilities.

### 3.4.2 Weighting Calculations

Calculation of the weights affecting the nodes is done for the child nodes through Shannon Entropy (Shannon and Weaver 1949) (Eqs. 4-7). The main idea for this technique is that the more dispersed the amount of a criterion, the higher the impact would be (Curto and Martin 2019). Shannon Entropy could be used as an indicator to quantify the information of a system. To give the weight of each node, these steps are:

Step 1: Calculate $P_{i j}$ using the decision-making matrix entries $\left(a_{i j}\right)$

$$
P_{i j}=\frac{a_{i j}}{\sum_{i=1}^{m} a_{i j}}: i, j
$$

Step 2: Calculate Entropy $\left(\theta_{j}\right)$

$$
\begin{gathered}
\theta_{j}=-k \sum_{i=1}^{m}\left[P_{i j} \ln P_{i j}\right] ; j \\
K=\frac{1}{\ln (m)}
\end{gathered}
$$

Step 3: Calculate weight $W_{j}$

$$
W_{j}=\frac{1-\theta_{j}}{\sum_{j=1}^{n} 1-\theta_{j}}
$$

where $\boldsymbol{\theta}_{\boldsymbol{j}}$ is the amount of entropy that determines the information transmission.

# 3.4.3 Validation of BN 

Validation is key to ensuring that the BN model has high quality. It is done through crossvalidation, the most common of which is K-fold cross-validation (Xiong et al. 2020). This method is a popular procedure for estimating the performance of a classification algorithm or comparing two classifications on a dataset. A dataset is randomly divided into k folds of equal size. Each fold is then used to test the model derived from the other k folds by a classification algorithm. Based on the average of $k$ accuracies obtained from k -fold cross-validation, the performance of the classification algorithm is assessed at the fold level of average.

In this study, for every ten years of risk calculation, the datasets are randomly divided into four folds of the same size: one set is introduced to the network as the training set and the other three are introduced as the testing sets. The testing set results are then checked with the results obtained from the BN in the calibration period (2001-2016).

### 3.5 Risk Nodes

The BN risk structure for evaluating the risk of water scarcity in agriculture is illustrated in Fig. 4. The nodes consist of the aggregation of hazard, vulnerability, and exposure. Hazard is representative of physical water scarcity, and vulnerability encompasses the social susceptibility and infrastructural and institutional capacities to cope with the risk. Exposure includes the economic aspects of water scarcity's consequences on agricultural income.

The risk was assigned based on the division of the risk calculation into four categories representing low, mild, high, and extreme risk. This part is done using categorizing in Netica software where risk is divided into four categories: $0-0.075$ (low), $0.075-0.15$ (mild), $0.15-0.225$ (high) and $0.225-0.3$ (extreme).

### 3.6 Coupling the System Dynamic Model with BN

The SDM was calibrated for QP in the calibration period (2001-2016) and the risk indicators were extracted from SDM. After the validation of the BN for the calibration period, SDM was developed to interactively be adjusted to assess different future scenarios. The SDM was established in Vensim DSS software.

In the next step, the future time series was divided into 3-time steps (2025-2035), (2035-2044), and (2045-2054). In each of the time steps, the risk indicators were extracted from SDM and fed into the BN. The BN model was developed using Netica software from Norsys Software Corp. The relation between parent nodes was evaluated and imported into the software to calculate the numerical value of child nodes. The final output of BN is the risk of water scarcity in the agriculture sector in future periods.

![img-3.jpeg](img-3.jpeg)

Fig. 4 BN for risk evaluation in QP

# 4 Results and Discussion 

### 4.1 Climate Change Scenarios of QP

Figure 5 shows the downscaled and bias-corrected precipitation of different AOGCM models in future periods. The results show that different models project precipitation differently and these are the major sources of uncertainty. This figure illustrates the
![img-4.jpeg](img-4.jpeg)

Fig. 5 Bias corrected precipitation of QP in (2025-2054) for the SSP126 (a) and, SSP585 (b)

various models, based on the unique assumptions inherent in each model's formulation, that forecast the trajectory of rainfall fluctuations across different years.

Figure 6(a) illustrates the average precipitation in the future, for SSP126 and SSP585 in comparison to the historical period for QP. The results depict that, except for the GFDL model in SSP126 and MRI-ESM_2 in SSP585, the other models predict precipitation reduction in future periods. In SSP126, the models depict a $5 \%, 33 \%$, and $11 \%$ reduction in INM, IPSL, and MPI_ESM_1, respectively. However, in MRI_ESM_2, there is no significant change in precipitation compared to the historical period. In addition, GFDL projects a $4.4 \%$ increase in precipitation. For SSP585, the results are a bit different; $11 \%, 1 \%, 30 \%$, and $13 \%$ precipitation reduction in GFDL, INM, IPSL, and MPI_ESM_1 are projected, respectively, whereas, in the MRI_ESM_2_0 model, a 13\% increase in precipitation is expected.

For minimum temperature projections in the future, all AOGCM models in both SSP scenarios show an increasing amount in comparison to the historical period (Fig. 6b). For maximum temperature, the projections predict temperature increase; for instance, in GFDL, INM, and MRI_ESM_2, the maximum temperature increases by 1, 1.5, and about 2 Celsius degrees in SSP126 and 2, 1.5, and 2 Celsius degrees for SSP585 (Fig. 6c).
![img-5.jpeg](img-5.jpeg)

Fig. 6 a Precipitation changes of QP b The changes in minimum temperature and c maximum temperature for the future (2025-2054) in comparison to the baseline period (1985-2014)

# 4.2 BN Set Up for QP 

### 4.2.1 Conditional Probability Table (CPT) Construction

The conditional probability table (CPT) of risk is constructed in Netica.By importing the child node data, the CPTs were calculated with Netica software and illustrated Based on the historical data, the low risk had the highest probability and vice versa has been detected. The reason for that is that the groundwater withdrawal reduction has not been applied to the QP and the water delivery varied between 0.6 and 1 with the highest probability in $0.8-1$ which was about $84 \%$. Besides this, the modern irrigation infrastructure that was established in the range of 0 to 0.2 of potentially irrigated area and the low range of agriculture insurance made coping capacity to be in the range of 0 to 0.2 . The lowest coping capacity affects the vulnerability in reverse relation. The higher the coping capacity, the less the vulnerability would be.

### 4.2.2 Cross-Validation Results

For the accuracy of the BN using the k-fold cross-validation method, four datasets from 2001 to 2016 were used. The results of testing the model were then checked with the 'test with cases' tab in Netica (Table 2). The purpose of this feature is to grade a Bayes net using a set of real cases to check how well the predictions or diagnosis of the net match the actual cases. For this purpose, firstly the selected nodes were imported into Netica; then we called the unobserved nodes (parent nodes) afterward, the result of BN predictions for the child nodes was compared with the real data values. According to the results (Table 2), the nodes are well-trained in BN since there is a low relative error that represents the network's ability to calculate the risk. In the next step when the accuracy of BN was proven, the BN can be used for future risk prediction.

### 4.3 Risk Parameters in the Future Using BN

### 4.3.1 Hazard

Figure 7a shows the expected values of water scarcity risk indicators in the baseline period, SSP126, and SSP585 scenarios in three 10-year time steps (2025-2034, 2035-2044, 2045-2054). In comparison with the calibration period, all the results indicate a concerning trend wherein water demand surpasses available resources in agriculture. Notably, the likelihood of hazards appears lower in the SSP126 scenarios across all temporal horizons, contrasting with the heightened probabilities observed in the SSP585 projections. For instance, for the second ten years, the hazard probability was

Table 2 Relative error of crossvalidation results (RMSE)


![img-6.jpeg](img-6.jpeg)

Fig. 7 a Hazard assessment, b vulnerability assessment and $\mathbf{c}$ the exposure assessment of QP in two SSP scenarios for three future time-steps
about $42 \%$ in SSP126, whereas for SSP585, it was about 56\% (Fig. 7a). Over time, the hazard in both SSP scenarios would increase. It is because of the reduction of groundwater withdrawal through time which is 1400,1200 , and 1000 MCM , respectively. This reduction significantly impacts water availability for agricultural purposes, despite escalating irrigation demands. As the surface water also decreased over these years, the ratio of agriculture supply to demand would decrease about $25 \%$ and result in higher hazards

in the system in terms of water delivery. The hazard here considered both physical and socio-economic aspects through engaging the water supply and their effective factors like climate change and water demand which are influenced by social factors.

# 4.3.2 Vulnerability 

In this study, vulnerability is described as the aggregation of susceptibility and coping capacity. The drivers of coping capacity are insurance, modern irrigation infrastructure, water recycling facilities, and literacy representing positive trends. The increase in these proxies also contributes to higher coping capacity and less vulnerability. As is clear in Fig. 7b, susceptibility shows a decreasing trend over time. In general, because of more weight on coping capacity than susceptibility for obtaining vulnerability, vulnerability depicted a similar trend in 2025-2034 and 2035-2044. One reason for the slight difference in 2045-2054 was the increased RGDP which affected the development of modern irrigation infrastructure. Moreover, the proactive establishment of additional wastewater treatment facilities by water managers further contributes to the decline in vulnerability during this period (Fig. 7b).

### 4.3.3 Exposure

The term "exposure" in our context refers to "agricultural income". The agriculture sector produces less income than the other two sections, which is proven by SDM modeling in the 2001-2016 period. However, factors such as rising food production costs, dwindling land availability, and reduced access to water resources inevitably drive up the price of agricultural products. This, in turn, amplifies the vulnerability of agricultural income to fluctuations in water availability. The agricultural sector faces a dual exposure to water scarcity, manifesting as diminished crop yields and reduced income levels, both of which are reflected in the agricultural subsystem in SDM. For assessing the effect of water scarcity on agriculture income, the less income deducted by higher water scarcity leads to posing a higher risk to QP. The results show that; the agricultural income would decrease by a probability of $28.8 \%, 27.8 \%$, and $24.565 \%$ in SSP126 in three 10-year time steps respectively. However, the decreasing trend in SSP585 was more obvious with a probability of $26.4 \%, 22.74 \%$, and $14.37 \%$. Since the RGDP in SSP585 had a sharper increase than in SSP126, leading to more development in the industrial sector, this change caused the exposure to decrease (Fig. 7c).

### 4.4 Risk Level Assessment

### 4.4.1 Baseline Period

Considering risk definition, the multiplication of hazard, vulnerability, and exposure is analyzed. Figure 8a shows the risk levels in the baseline period by the probability of $62.4 \%$ belonging to Low risk. Therefore, the farmers' income is not affected by the negative effects of water scarcity.

![img-7.jpeg](img-7.jpeg)

Fig. 8 a The risk results in the baseline period, (b) in 2025-2034 for SSP126 and (c) SSP585, (d) in 20352044 for SSP126 and (e) SSP585, in 2045-2054 for SSP126 (f) and SSP585 (g)

# 4.4.2 Future Period (2025-2034) 

The hazard element in BN in both SSP scenarios for the 2025-2034 period depicts less ratio of water supply to water demand than in the baseline period. For SSP126, the state variable falls between 0.4 -and 0.8 ; however, for SSP585, this ratio falls between 0.4 and 0.6 with a higher probability. One reason for this change is that precipitation reduction in SSP585 is more and subsequently, less water recharges to the surface and groundwater.

By following the business as usual in the baseline period for 'water recycling facilities', 'literacy rate', and 'insurances', there is no significant change between the two SSP scenarios. However, for influencing the 'modern irrigation infrastructure' by RGDP and considering higher RGDP in SSP585, a higher 'coping capacity is expected in SSP585.

Susceptivity is driven by agricultural labor and, in both SSP scenarios; there is no significant change in labor variation in comparison to the two other subsystems. However, the ratio of susceptivity in SSP585 was lower than in SSP126, but it was still identified between 0.1 and 0.2 .

The 'exposure' node, which identified the agriculture income, shows a higher probability in SSP126 since the cultivated area was higher than SSP585 due to more water availability. The last node 'risk' depicts a higher probability in the 'low' risk class in SSP126 expected with a probability of $27 \%$ belonging to 'Low' and a probability of $10 \%$ in SSP126 and SSP585. For mild classification, the probability is $44 \%$ and $38.5 \%$ for SSP126 and SSP585, respectively. The high risk in SSP585 is higher than in SSP126 (Fig. 8b, c). Lastly, the extreme probability depicts more ratio in SSP585 than in SSP126. The risk results show that the hazard and exposure have inverse effects in the risk node. Of available water in agriculture, the more available water is, the less the risk will be. Similarly, in exposure which is representative of the economic condition of agriculture, by less land and water availability, the income will be reduced as less income brings higher risk to the system. Low agriculture income results in less labor demand in the QP, while there is rising unemployment in the basin increasing the risk in the agriculture sector of the QP. The results demonstrate that the allocated water in agriculture cannot support the cultivated area and reduction of farmlands is necessary.

### 4.4.3 Future Period (2035-2044)

Figure 8d, e shows the results of risk assessment in the 2035-2044 period under the two SSP scenarios. In this period, the groundwater withdrawal capacity reached 1200MCM. Therefore, the probability of water availability in SSP126 falls between $0.2-0.4,0.4-0.6$, and $0.6-0.8$ with the probabilities of $20 \%, 18.2 \%$, and $58 \%$. In the same state domain in SSP585, the probabilities are $34.5 \%, 60 \%$, and $1.82 \%$, respectively. This means that, in SSP126, more water availability in agriculture is found than in SSP585. Modern irrigation infrastructure also has very close probabilities; the reason is that under SSP585, despite more RGDP increments, the population also increased; so, the ratio is closer to the SSP126 scenario.

The ratio of vulnerability is close in both SSP scenarios; however, in SSP585 with a higher hazard and higher probability of exposure, the risk is expected to fall with a higher probability of $57 \%$ in the mild level in SSP585 and SSP126 with a probability of $37.4 \%$. The projected risk in the second time step shows more water scarcity in QP. The risk will rise with increasing the hazard. As the crop production is in direct link with the available

farmlands by cutting off the farmlands less crops could be cultivated and continuously the income gained from crop production will decrease as well.

# 4.4.4 Future Period (2045-2054) 

In the last ten years of simulation (2045-2054), the withdrawal capacity reached about 1000MCM. Due to less water for irrigation, agricultural net profit in comparison to other parts is relatively low. The Bayesian Network (BN) analysis indicates a downward trend in the agriculture income ratio, which steadily declined over the last decade, leading to a net income range between 0 and 0.2 . Another contributing factor to this decline is the increased RGDP in the QP, which increases industrial added value. Moreover, the added value in services and domestic sectors exhibited an upward trajectory relative to the baseline period.

An increase in QP coping capacity results in a steady decrease in vulnerability, the coping capacity and vulnerability depict an inverse relation. By decreasing the irrigated land, agricultural labor also changes. The amount of hired agriculture labor in comparison to the baseline period will decrease; however, through the years of future simulation, no significant difference is witnessed. Analysis of water availability probabilities for the 2045-2054 period revealed fluctuations ranging between $34.5 \%$ and $78.2 \%$ for SSP126 and SSP585 scenarios, respectively (Fig. 8f, g). Consequently, the projected risk index exhibited an overall increase over the 30-year simulation period. Diminished water and land availability directly impacted agricultural income and employment, leading to a notable reduction in the employed fraction of individuals in this sector. However, enhanced water delivery to the QP facilitated risk mitigation efforts and gradually elevated agricultural employment opportunities and income levels.

## 5 Discussion

This study introduces a novel framework aimed at quantifying, estimating, and assessing the probability of water scarcity risks under various scenarios including climate change, economic, and groundwater policies. Theoretically, agriculture will expose more to negative consequences of this risk because of more water dependency (Ahmadi et al. 2021). The results of the simulation depict risk characteristics that accumulate over time. Water availability is influenced by climate change, however, increasing water demand in agriculture due to higher evapotranspiration. Low irrigation efficiency may have a stronger effect on water scarcity since the amount of water availability to water demand is decreased gradually through the time frame.

However, the effects will not capture just in the agriculture sector alone and will propagate through the whole water system. Continuously, water scarcity endangers agriculture production and accordingly the income, investment for food production and workforce in this sector. As agriculture income is a concern as the exposure, due to farmers' attitude toward more valuable crops with less water consumption in the area, the diversity of crop types is endangered. Endangered crop types could influence food security in the region. Therefore, QP's managers should consider agricultural production's imports.

By providing more jobs in the industry and services, reasonable diversification from agriculture labor occurs. A decrease in income will put the farmers' life in substandard condition also increase the possibility of migration in the region due to crop failures. A

low per capita income, economic contraction, competition for resources, and other adverse social-economic factors can increase conflict risk (Field et al. 2014).Agriculture communities benefit from literacy, modern technological tools, insurances and socio-economic associated factors to enhance coping capacity toward climate change. These results are parallel to Li et al., published in 2021. Some other factors proposed by stakeholders to include such as inflation rate, subsidies, or poverty assessment. however, it makes the model more complicated and harder to interpret and some suggestions were hard to quantifiable.

The agriculture sector uses surface water, groundwater for irrigation and however there is a high potential of recycled water for irrigation, the amount of treating wastewater is low. As treated water is valuable fertilizer then could help farmers to reduce the expenses on agricultural supplements and increase the income which eventually reduce the risk.

The dynamic risk index calculated in this study can foster awareness of climate change adaptation strategies. Indicators used to assess risk should accurately represent regional stressors, which vary across regions. Results showed that there were several reasons for increasing the water scarcity risk in QP: 1) the decreasing trend in precipitation and, following that, the less recharged water to surface and groundwater; 2) decreasing the agricultural area due to less water availability; 3) less agriculture income which causes more agricultural risk. Findings were similar to the research results of (Naderi et al. 2021; Mueller et al. 2020; Akbari et al. 2022).

Based on the integrated risk assessment in this study, increasing risk through time scale indicates the QP will be unstable to climate change. In order to mitigate the risk of water scarcity in QP, it is necessary to have social, economic, and technological capacity. Therefore, more investment in the region could lead to stronger capacity building for risk mitigation. Policymakers can use the model to gain a better understanding of future risks, the severity of exposure, and the target point for exploring policy options to enhance resiliency. Its applicability extends to other regions, provided adaptations are made to account for regional nuances in hazard, vulnerability, and exposure.

# 6 Conclusion 

This article discussed the water scarcity assessment of QP due to climate change with a particular focus on the identification and quantification of risk drivers' interactions using coupled SDM-BN to benefit from the strengths of SDM and BN models.

First the integrated system was built for base time and after projections of climate change impacts in the future, water management options, and economic expansion, the risk of the agricultural subsystem was evaluated. The finding suggested that the water scarcity risk in QP is increasing in the future. Results of SDM-BN also revealed that the fluctuation in the amount of water delivery for agriculture will increase over time.

The proposed SDM-BN coupling in this article can deliver an extra benefit for decisionmakers with a probabilistic understanding of the water supply and water demand conditions, depicting the complexity and dynamic nature of risk drivers in the future and current situations. This framework can address different aspects of adaptive decision making and by emerging new probability in the future in each sector, they can choose between alternatives.

To reduce the risk, long-term planning adaptation options play a crucial role in increasing the ability to adapt and reducing vulnerability and exposure. As the region faces

increasing water demand, long-term sustainable planning is critical, and more contribution from social institutions and NGOs is needed.

However, there are still some limitations in the study, and still unknown drivers of risk which need to be further developed due to the complexity of risks induced by climate change and the limited understanding of risk propagation paths. Additionally, this study focuses on the agriculture sector, but evaluating risk in other sectors, which are not modeled in the BN, can be useful.

In future studies, in addition to using Shannon entropy to weight risk parameters, the risk parameters can be weighted through joint discussions with policymakers and regional water authorities to gain further insight into the risk drivers.

Authors Contributions Sara Dehghani: Investigation, Methodology, Software, Formal analysis, Writing -original draft. Alireza Massah Bavani: Conceptualization, Supervision, Validation, Writing—Review \& Editing. Abbas Roozbahani: Conceptualization, Supervision, Validation, Writing—Review \& Editing. Oz Sahin: Validation, Writing—Review \& Editing.

Funding Open access funding provided by Norwegian University of Life Sciences

# Declarations 

Ethical Approval Not applicable.
Consent to Participate Not applicable.
Consent to Publish Not applicable.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

# Authors and Affiliations 

## Sara Dehghani ${ }^{1} \cdot$ Alireza Massah Bavani ${ }^{1} \cdot$ Abbas Roozbahani ${ }^{2} \odot \cdot$ Oz Sahin $^{3}$

$\boxtimes$ Alireza Massah Bavani
armassah@ut.ac.ir
$\boxtimes$ Abbas Roozbahani
abbas.roozbahani@nmbu.no
1 Faculty of Agricultural Technology, College of Agriculture and Natural Resources, University of Tehran, Tehran, Iran
2 Faculty of Science and Technology, Norwegian University of Life Sciences (NMBU), Ås, Norway
3 School of Engineering and Built Environment, Griffith University, Southport, QLD 4222, Australia