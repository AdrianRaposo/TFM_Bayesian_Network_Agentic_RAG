# Developing a Risk Management Framework for Agricultural Water Systems Using Fuzzy Dynamic Bayesian Networks and Decision-Making Models 

Atiyeh Bozorgi ${ }^{1} \cdot$ Abbas Roozbahani ${ }^{2} \odot$ Seied Mehdy Hashemy Shahdany ${ }^{3} \cdot$ Rouzbeh Abbassi ${ }^{1}$

Received: 2 July 2024 / Accepted: 28 August 2024 / Published online: 25 September 2024
(c) The Author(s) 2024


#### Abstract

Given the various natural and human-caused hazards that threaten the agricultural water distribution process from the main source to farms, establishing a framework to analyze these risks is crucial. This study aims to develop an intelligent risk management framework to help stakeholders devise long-term and sustainable solutions for managing agricultural water systems. First, we developed a Fuzzy Dynamic Bayesian Network (FDBN) model for multi-hazard risk assessment, taking into account the temporal causal interactions between parameters and incorporating fuzzy theory. Next, we defined several risk management scenarios across structural, non-structural, automated control, and integrated methods. These scenarios were implemented in the FDBN model to mitigate the risks associated with the system. Various economic, social, environmental, and technical criteria were considered, and scenarios were ranked using the WASPAS, TOPSIS, and MultiMoora methods. The Copeland approach was used to combine the ranking results. The results showed that automated scenarios, specifically Model Predictive Control (MPC) and Proportional-Integral (PI) controllers, could reduce the system's risk by $11.4 \%$ and $9.8 \%$, respectively, and were ranked the highest. The findings of this study and the proposed framework can assist operators in the sustainable planning and management of water systems in light of anticipated threats.


Keywords Sustainable water management $\cdot$ Multi-hazard risk modelling $\cdot$ Fuzzy dynamic bayesian network $\cdot$ Multi-criteria decision making $\cdot$ Risk management

## 1 Introduction

Persistent droughts and climate change in recent decades have created significant challenges in maintaining an adequate water supply to meet agricultural demand in arid regions (Hashemy Shahdany et al. 2018). Water supply and distribution systems are increasingly

[^0]
[^0]:    This paper is submitted for the WARM S.I. "Managing Water-Energy-Land-Food under Climatic Environmental and Social Instability".

    Extended author information available on the last page of the article

vulnerable to various hazards, raising the likelihood of system failures. Therefore, conducting risk assessments is essential to enhance the efficiency of these systems.

Risk assessment is crucial for mitigating potential accidents by identifying hazards, their likelihood, system tolerance, and consequences (Rausand and Haugen 2020; Abedzadeh et al. 2020; Shafiee Neyestanak and Roozbahani 2021; Roozbahani and Ghanian 2024). While various methods have been used for risk assessment, this paper focuses on the effectiveness of the Fuzzy Dynamic Bayesian Network (FDBN). FDBN accounts for temporal relations and uncertainties, making it suitable for complex systems like agriculture. Compared to traditional Bayesian Networks (BNs), FDBNs are more flexible and interpretable (Ren et al. 2009; Guo et al. 2021) and can more effectively manage uncertainty and describe complex relationships between risk events.

Research on FDBN spans various fields, demonstrating its effectiveness in handling uncertainty and improving risk assessment accuracy. It has been used for decision support in critical situations (Naderpour et al. 2013), error detection and reliability prediction (Yao et al. 2015), and marine hazard assessment (Jinyong et al. 2017). Liu et al. (2020) showed that an improved FDBN model enhances the reliability of face recognition systems. Despite these advancements, FDBN has not yet been applied to assess risk in agricultural water systems, which are significant consumers of water resources. Although Bayesian Network methods have been used for risk evaluation in water systems, the multi-hazard risk in agricultural supply and distribution remains unexplored.

Risk assessment is a key part of any risk management project, aiming to reduce the likelihood and impact of hazards (Popov et al. 2016). Risk management involves the efficient use of resources to maximize opportunities. Le et al. (2024) analyzed drought risk assessments for agriculture, finding that most studies lack methodological validation and often do not link risk identification to practical adaptation strategies. Shelar et al. (2023) developed a framework to assess climate change-related water scarcity risks in Puglia, Italy, identifying vulnerable areas and enabling tailored adaptation strategies for agriculture and irrigation. Orojloo et al. (2018) developed a fuzzy hierarchical risk management framework for canal networks, while Ghandi and Roozbahani (2020) ranked water risk management alternatives using fuzzy and non-fuzzy MCDM methods. Ronco et al. (2017) focused on nanoagrochemicals for seed treatments, highlighting the need for effective risk management to address safety concerns and maximize their potential in sustainable agriculture.

Based on previous studies, there is a gap in assessing the multi-hazard risk of agricultural supply and distribution systems. This gap impacts the ability to provide accurate information about the risk status of these systems, which are threatened by various hazards over time. A risk assessment model is needed to improve agricultural water systems, allowing for efficient water use and demand management. In this context, the FDBN is utilized to model causal relations between system components and address the uncertainty of parameters for risk assessment in agricultural water systems.

Risk management is essential for mitigating hazards' consequences, yet agricultural water supply and distribution systems have received less attention compared to other systems. Despite studies on risk reduction measures, their effects and predicted scenarios often remain unassessed. Evaluating the effectiveness of risk reduction scenarios using methods like FDBN is necessary. Additionally, the application and integration of new MCDM methods in risk management, such as MultiMoora and WASPAS, have been overlooked. This research addresses these gaps by discussing less commonly used methods in water resources management. Effective risk management scenarios are identified through various MCDM methods, with the Copeland method used for integrated ranking. Using three different MCDM methods ensures confidence in selecting the best scenarios.

Bozorgi et al. (2021) developed HBN to evaluate the risk of agricultural water systems. This research extends this model by incorporating the capabilities of the FDBN model, including temporal relations and parameter fuzzification. For the first time, this research evaluates risk mitigation scenarios in multiple aspects, including economic, social, environmental, and technical factors.

The research aims to develop an innovative, comprehensive multi-hazard risk assessment framework tailored specifically for agricultural water systems, using advanced probabilistic techniques, including a fuzzy dynamic Bayesian network. This framework is designed to handle data uncertainty and incorporate temporal dynamics, providing a more accurate and detailed analysis of risks. The study also introduces a user-friendly model that automates the risk assessment process, making it more efficient and accessible. Through a real-world case study, the framework's practicality and effectiveness are evaluated, addressing critical questions such as whether the fuzzy dynamic Bayesian network can assess overall risk with limited data, the system's risk level based on various hazards, the components and sub-components most at risk, and the best management strategies for mitigating these risks. Additionally, the research evaluates different risk management scenarios, providing decision-makers with comprehensive insights to enhance water distribution and reduce risks across economic, social, technical, and environmental dimensions.

The article begins by explaining the risk assessment structure and modeling with FDBN, then defines scenarios and their implementation in the FDBN model. It investigates the capabilities of these scenarios and determines the best risk management strategies using MCDM methods. The effectiveness of the scenarios is demonstrated by their ability to reduce system risk and improve conditions in environmental, social, and economic areas. The best alternatives are presented to the network operator.

# 2 Methodology 

This research follows steps outlined in Fig. 1. First, a risk assessment structure is designed by defining system components and identifying threats based on a case study. Risk assessment evaluates hazard likelihood, system vulnerability, and hazard consequences using indexes, modeled with FDBN. Next, scenarios-structural, non-structural, automated, and integrated are defined to manage system risk and assessed economically, environmentally, socially, and technically. MCDM approaches then rank the scenarios by criteria success, with Copeland merging the results to propose alternatives. Methodology details are provided in the following sections.

### 2.1 Risk Assessment Structure

Risk has three main parts: the probability of hazard occurrences $\left(P_{i, j}\right)$, systems' vulnerability against the hazard $\left(V_{i, j}\right)$, and hazards' consequences $\left(C_{i, j} ; i\right.$ th hazard, $j$ th component) (Torres et al. 2009). This equation is presented as follows:

$$
\text { Risk }=P_{i, j} \times V_{i, j} \times C_{i, j}
$$

The various system components should be identified before evaluating the risk associated with the system. The next step is to identify the hazards that each component is exposed to. These hazards can be created by humans, nature, or operations. The relevant indices should consider how vulnerable each system component is when threats arise. These indices show

![img-0.jpeg](img-0.jpeg)

Fig. 1 Developed Methodology for Risk assessment and management of agricultural water system
how resistant each system component is to hazards. Another component of risk is the consequences brought on by the hazard, which can be classified in terms of economic, social, environmental, or technical factors.

# 2.2 Fuzzy Dynamic Bayesian Modeling 

In this study, a Fuzzy Dynamic Bayesian Network (FDBN) was used to model the risks in agricultural water supply and distribution systems. The Bayesian network shows how nodes are related using edges in a directed acyclic graph. This method relies on probabilities first introduced by Bayes in 1763, where the posterior probability is calculated from the prior probability (Eq. 2). Equation 3 in the network determines the probability distribution for a set of variables (Jensen and Nielsen 2007):

$$
P\left(X_{1} \mid X_{2}\right)=\frac{P\left(X_{2} \mid X_{1}\right) P\left(X_{1}\right)}{P\left(X_{2}\right)}
$$

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \operatorname{Parents}\left(X_{i}\right)\right)
$$

In which, $P\left(X_{1}\right)$ and $P\left(X_{2}\right)$ are two events, the probability of each occurring is zero; $X_{i}=$ is the $i$-th variable in the network.

Each variable is shown as a node, with arcs indicating their connections. The Conditional Probability Table (CPT) gives the probability of each node based on its immediate parents. FDBN combine Dynamic Bayesian networks with fuzzy theory to model systems that change over time (Mihajlovic and Petkovic 2001). A DBN has two parts: an initial Bayesian Network (BN) for the first time slice and a series of BNs for later time slices, showing how nodes relate over time. Equation (4) describes a DBN using a probability distribution function for a sequence of T hidden-state variables X and observation variables Y .

$$
P(X, Y)=\prod_{t=1}^{T-1} P\left(x_{t} \mid x_{t-1}\right) \prod_{t=0}^{T-1} P\left(y_{t} \mid x_{t}\right) P\left(X_{0}\right)
$$

The fuzzy set theory was introduced by Zadeh (1965). Fuzziness is used when the boundary of elements is unclear, and there is uncertainty or vagueness. If $X$ is a space of fuzzy data points and it defines as $X=\{x\}$. A fuzzy set $\widetilde{A}$ can be represented by a membership degree in the range of $[0,1] . \mu_{\widetilde{A}}=0$ means $x$ does not belong to $\widetilde{A}$ and the value between $0-1$ represents the partial membership. There are different membership function shapes like triangular, trapezoidal, and gaussian. Trapezoidal and triangular are mostly used for the linguistic variable (Ren et al. 2009); in this study, the simple triangular function has been used. Triangular membership function $\left(\widetilde{A}=\left(a_{1}, a_{2}, a_{3}\right)\right)$ is presented in Eq. (5) (Ramzali et al. 2015). The parameters are divided into three classes low, medium, and high the diagram is shown in Fig. 2.

$$
V_{i}(x)=\left\{\begin{array}{cc}
0 & x<a_{1} \\
\frac{x-a_{1}}{a_{2}-a_{1}} & a_{1} \leq x \leq a_{2} \\
\frac{a_{2}-x}{a_{3}-a_{2}} & a_{2} \leq x \leq a_{3} \\
0 & x>a_{3}
\end{array}\right.
$$

FDBN combines DBN with fuzzy set theory, allowing for the quantification of uncertainty in dynamic processes (Guo et al. 2021). Observational variables are represented using fuzzy membership functions, a method introduced by Brignoli et al. (2015). Bayesian network learning involves structural and parametric training. Structural training determines the relationships and linkages between nodes using algorithms like constraint-based and score-based learning. Since the network's structure (nodes and causal links) is known

Fig. 2 Fuzzy regions and membership function
![img-1.jpeg](img-1.jpeg)

in this study, only parametric learning is needed. The Expectation-Maximization (EM) algorithm, introduced by Dempster in 1977, is used to create conditional probability tables (Reed and Mengshoel 2012; Sharma and Goyal 2016). The EM algorithm refines parameter estimates by adjusting initial values based on observed data until they converge (Reed and Mengshoel 2012).

BayesFusion software, featuring GeNIe for interactive model building and SMILE for reasoning and learning, supports various programming languages, including Python, used in this study. GeNIe has been previously used for simulating BN, DBN, and FDBN (Sienkiewicz and Łaska 2022).

After completing structural and parametric learning, the FDBN model must be calibrated and validated. One common validation technique is K-fold cross-validation, where the dataset is split into k equal parts. In each iteration, $\mathrm{k}-1$ parts are used for training, and one part for testing (Xiong et al. 2020).

# 2.3 Risk Management Scenarios 

Risk management scenarios are determined at this stage. Expert opinions and historical case study research are used to identify these scenarios. Risk management scenarios are classified into four types: non-structural, structural, automatic control, and combination.

- Non-Structural Scenarios

Non-structural approaches improve network operation in water scarcity situations by using operational experience. The focus is to enhance the traditional way of manually or automatically adjusting water level structures. The following are some techniques.

Scheduled Water Delivery (Scenario 1)
This method divides the main canal's intakes into upstream and downstream sections. Water is delivered in turn. Upstream intakes receive water half time, while downstream intakes receive water in the other half of the scheduled time (Khiabani et al. 2020; Tork et al. 2021; Khaeez and Hashemy Shahdany 2021).

Operation Method to Reduce Dewatering Time (Scenario 2)
The flow rate to the off-takes of the main canal is reduced when the inflow water to the head source of the canal is reduced. This strategy aims to achieve water distribution equity. As a result of the reduced available discharge, delivery time to off-takes is reduced rather than the delivered flow being reduced.

Inflow Fluctuation Prediction (Scenario 3)
The inflow fluctuation in the canal's head source was detected by hydrometry stations. The discharge to off-takes has changed from the beginning of the fluctuations. The discharges are then readjusted to match the initial demand need, and the procedure continues (Khiabani et al. 2020).

Increasing the Intake Recharge and Reducing the Flow Time in the Irrigation Canal (Scenario 4)

When the volume of water entering the network is less than the demand, the inflow to the canal increases and the length of dewatering reduces. In practise, this strategy shortens the delay time by improving the canal's intake recharge and lowering evaporation and leakage losses (Tork et al. 2021).

- Structural Scenario (Scenario 5)

The application of structural solutions was investigated in modernization and rehabilitation projects aimed at improving irrigation canal operation (Burt 2013; Hashemy Shahdany et al. 2013; Guan et al. 2011). Replacement of hydraulic structures (water level adjustment structures, catchment structures) is the most common structural scenario in modernization projects. The kind of catchment of the surface water distribution system is changed from Neyrpic to slide gates in this method. Specific flows can be passed through Neyrpic structures. However, depending on the openings, slide gates can pass any volume of water. As a result, the flow rate can be adjusted several times each day to the desired level, making its control easy (Khiabani et al. 2020; Tork et al. 2021).

# - Automated Control 

The use of automatic control systems in the distribution of surface water in a network of open canals is being done to reduce uncertainty (Maestre et al. 2014). Hydrodynamic flow simulators calculate all calculations linked to the amount and duration of opening/closing hydraulic structures, and each structure is adjusted by the motors connected to it. In other words, the operator's job is limited to monitoring the manner of operation. In this study, two selected scenarios in this category are the Model Predictive Control (MPC) system and the second one is decentralized automatic control system-Proportional-Integral Controller (PI). (Hashemy Shahdany et al. 2013; Kamrani et al. 2020).

## Model Predictive Control (Scenario 6)

To compute the controller output variable (water level figure in irrigation canal intervals), this method employs an optimization algorithm. The controller's role is to regulate the water level control structure above each canal interval to bring the water level downstream of each main canal to the target level. The MPC controller adjusts water level control structures by using a simplified mathematical model of the hydraulic flow (the internal model of the control system). The control directives for each time step are determined by the hydraulic condition prediction and the canal's current measurements (Kamrani et al. 2020).

## Proportional-Integral Controller (Scenario 7)

The PI controller is designed to measure the controlled variable (water level) upstream of the adjustment structure using feedback control (closed-loop control). In this method, the regulated variable (water level upstream of the regulating structure) is returned to the control algorithm to measure the corrective action, which is the rate of opening of the ditch (Hashemy Shahdany et al. 2013; Kamrani et al. 2020).

- Integrated Scenarios

Integrated scenarios are made up of two structural and non-structural strategies. All necessary activities in non-structural scenarios ( 4 scenarios stated) are performed in integrated scenarios, along with the required changes in catchment structures. In other words, non-structural procedures are used in each scenario after structural adjustments to the agricultural water distribution network.

# 2.4 Defining Criteria to Evaluate Risk Management Scenarios 

After selecting the scenarios, criteria for evaluating risk management performance should be established, including technical, economic, social, and environmental factors, aiming to enhance the surface water distribution process. Details are provided below. One research assumption is the inability to change the area under cultivation. Moreover, implementing risk management scenarios reduces operational losses in the agricultural water distribution system, with a new source replacing these reduced losses.

- Technical Criteria

The created FDBN risk assessment model incorporates risk management scenarios. The technical criterion is the potential of each scenario to reduce the risk of the system. This criterion is the difference between the average risk of the system in baseline (current situation) and the application of each scenario.

- Economic Criteria

The economic criterion includes two sub-criteria. (a) the cost of implementing each scenario, and (b) the agricultural benefits of modernizing the surface water distribution system. The agricultural profit from expanding the area under cultivation irrigated by surface water and lowering the area under cultivation irrigated by groundwater is calculated in the second sub-criterion. In other words, this sub-criterion is based on the profit of surface water-based agricultural production, which is computed as gross profit minus production costs and pumping station operating and maintenance costs (Hashemy Shahdany and Roozbahani 2016; Tork et al. 2021).

- Social Criteria

The next criterion is the social criterion, which is divided into two sub-criteria. (a) Increased employment is considered by increasing the area under surface water irrigated (assuming a fixed area under cultivation). This sub-criterion is based on an increase in the number of seasonal daily pay workers per hectare of the network as a result of risk management scenarios being implemented. (b) The equity of water delivery is a metric that measures the proportion between the amounts delivered and the amounts required over time. Molden and Gates (1990) introduced this index (Eq. (6)).

$$
P_{E}=\frac{1}{T} \sum_{i} C V_{R}\left(\frac{Q_{d}}{Q_{r}}\right)
$$

where $Q_{r}$ and $Q_{d}=$ the amount of water required and delivered, respectively, and $\frac{1}{T} \sum_{T}$ $=$ average time and $C V_{R}=$ coefficient of spatial variation. When the index reaches 0 , the equity of water delivery is achieved. According to Molden and Gates (1990), 0-10 percent is good, $10-20$ percent is moderate, and more than 20 percent is weak. Each category's numbers are also interpreted. Even if the numbers are one percent closer to zero, that situation is preferable.

# - Environmental Criteria 

The environmental criterion consists of two sub-criteria: (a) Reduction of groundwater withdrawal: Hydrodynamic models developed for the case study apply risk management scenarios, simulating hydraulic flow in open canals to determine water delivery volumes. These models calculate water delivered to the 2nd-degree canal by simulating water loss along the 1st-degree canal. The delivered water quantities are used to compute the adequacy index, which forms a GIS layer. Reduction in groundwater withdrawal is then calculated using GIS, incorporating the adequacy and well map layers.
(b) Energy conservation through reduced groundwater withdrawal: Energy savings resulting from reduced groundwater withdrawal are determined using Eq. (7) (Karimi et al. 2012), based on the extent of reduction in groundwater withdrawal.

$$
E c=\frac{2.73 * D * V}{O P E *(1-T l) * 1000}
$$

In which, $E c=$ total energy consumption ( Kwh ); $D=$ depth of groundwater relative to ground level; $V=$ volume of water withdrawn; $O P E=$ pump efficiency and $T l=$ transmission losses.

### 2.5 Analytic Hierarchy Process (AHP)

The AHP method is a comprehensive process for multi-criteria decision-making, allowing hierarchical problem formulation. The process involves breaking down the problem into hierarchical levels. A questionnaire, containing pairwise comparisons of criteria, is distributed to experts who rate the importance of criteria on a scale of 1 to 9 . A rating of 1 indicates equal importance, while 2 to 9 indicate increasing levels of importance.

Following the collection of data from questionaries, the consistency of the data should be examined. The initial step should be calculating the weighted sum and consistency vectors. The consistency index is then calculated using the formula (Eq. (8)) (Taherdoost 2017).

$$
C I=\frac{\lambda_{\max }-n}{n-1}
$$

In which, $\lambda_{\max }=$ the average elements of the consistency vector and $n=$ the number of options.

The consistency ratio is then calculated from the division of the consistency index to the random index (Golden and wang 1990). The comparison results are acceptable if the consistency ratio is less than 0.1 (Taherdoost 2017).

# 2.6 Multi Criteria Decision Making (MCDM) 

When choosing the best option among various alternatives with different criteria, MCDM methods are essential. These methods, based on diverse logics and calculations, identify the optimal choice for decision-makers. Various risk management scenarios have been defined and assessed using different criteria, so MCDM methods such as TOPSIS, WASPAS, and MULTIMOORA are employed here.

TOPSIS (Technique for Order of Preference by Similarity to the Ideal Solution) ranks alternatives based on their distance from the ideal and worst solutions (Dai et al. 2010). WASPAS (Weighted Aggregated Sum Product Assessment) combines WSM (Weighted Sum Model) and WPM (Weighted Product Model), offering more accuracy than using either method alone (Zavadskas et al. 2012). MULTIMOORA uses a ratio system, reference point, and full multiplicative form for multidimensional optimization (Brauers and Zavadskas 2006).

To consolidate rankings from multiple MCDM methods, an aggregation method like Copeland is used, where a matrix compares alternatives based on preference (Dey et al. 2016).

### 2.7 Case Study

The developed risk assessment framework is implemented in the Roodasht irrigation district as an agricultural water supply and distribution system. It is located in the center of Iran, Isfahan province. The transmission canal can handle 48 cubic metres per second of flow. This system covers about 45,000 hectares of agricultural land, which is cultivated with wheat, barley, fodder corn, alfalfa. The Roodasht irrigation district's plan is visualized in Fig. 3.

The Roodasht irrigation network in Isfahan province's Zayandehrood basin faces upstream fluctuations in agricultural, network, and industrial water use. This instability affects water supply across all ditches of the main canal, especially midstream and downstream, often leading to shortages or overflow. Roodasht was selected as a case study due to its unreliable water supply, causing social tensions. Upstream river inflow fluctuations exacerbate shortages in the main canal. Poor design and varied water-regulating structures further exacerbate water level issues along the canal.

- Risk Assessment Structure of Roodasht Irrigation District

It is necessary to identify hazards that threaten distinct components of the system. The agricultural water system is made up of two parts: supply and distribution. Upstream, middle stream, and downstream are the three subcomponents of the distribution component. According to historical data and expert opinions, drought is an important hazard that threatens the supply component. Additionally, each distribution component is threatened by Improper Performance of the Ditch-Riders (IPDRs) and Operational Losses (OL).

Risk assessment components (hazard occurrences, systems' vulnerability, and hazards' consequences) are calculated using hydraulic and hydrological indices based on the nature of the system and hazards (Bozorgi et al. 2021). Each component has an individual index that is shown in Table 1.

![img-2.jpeg](img-2.jpeg)

Fig. 3 The plan of the Roodasht irrigation district

These indices are streamflow drought index, deficiency compensated by groundwater, reliability for supply component and delay time, the discharge sensitivity to water depth variation index, structural adequacy, dependability, adequacy, and efficiency for distribution component. The input parameters used include river inflow, water delivered, groundwater withdrawal, cultivation area, and the net irrigation requirements of cropping patterns. These parameters were collected from the Isfahan Regional Water Company.

As explained in Sects. 2-3, the FDBN risk assessment structure should be modeled. GeNIe and SMILE were used to model the Roodasht irrigation network risk assessment. Figure 4 illustrates the FDBN scheme.

- Implementation of Scenarios

Hydrodynamic models are used to apply the scenarios described in the Roodasht irrigation district's risk assessment model. These hydrodynamic models simulate the distribution and delivery of water in the main irrigation canal. These models have been constructed, calibrated, and validated previously by this research group. They have also been employed in previous studies (Khiabani et al. 2020; Khaeez and Hashemy Shahdany 2021; Tork et al. 2021; Barkhordari and Hashemy Shahdany 2021; Kaghazchi et al. 2021). The developed models of this irrigation network include the ICSS simulator model, Hec-Ras, and a simplified Integrator Delay (ID) mathematical model written in MATLAB. Previous research has described how this mathematical model works and the basics of performance in modeling irrigation canal operations (Shahverdi and Monem 2015). The ID model is employed in this study. The ID model is a hydrodynamic model that predicts how much water will be supplied to each catchment over time based on changes in the hydrograph.

Table 1 Risk assessment structure


Where, $Q_{i, j}$ river streamflow for $j$-th month in the $i$-th hydrological year, $V_{i, k}$ cumulative streamflow from the first month to $k$-th period at $i$-th year, $\bar{y}_{k}$ and $s_{y, k}$ the average and standard deviations of cumulative streamflow volumes as these are estimated over a long period, SDI streamflow drought index, $P_{d}$ the hazard probability by using SDI, $C m$ the ratio of deficiency compensated by groundwater, $G w$ the volume of groundwater withdrawal, $D e$ agricultural demand, $R e$ water delivered to the catchments, $R e l$ reliability, $S$ the discarge sensitivity to water depth variation index, $\Delta Q / Q$ the ratio of the relative variation of discharge through the structure, $\Delta \mathrm{H}$ upstream water depth deviation, $A q_{s}$ structural adequacy, $\frac{1}{T} \sum$ and $\frac{1}{R} \sum$ indicate the time and spatial average, respectively, $Q_{d}$ the amount of water that could be delivered by the system considering the perfect operation according to the given schedule, $Q_{s}$ Water-delivery schedules that specify the amount scheduled, $D_{s}$ deviation of the value of the inflow from its normal value, $R e_{n}$ the value of the normal inflow, $P_{d}$ dependability, $C V_{T}\left(\frac{Q_{D}}{Q_{R}}\right)$ temporal coefficient of variation (ratio of the standard deviation to mean) of the ratio $Q_{D} / Q_{R}$ over the period $T, Q_{R}$ the amount of water required for consumption use, $Q_{D}$ the actual amount delivered by the system, $Q f_{n}$ normalized values off the adequacy/effiency parameter, $C l$ the consequence of OL. Finally, the risk is calculated by multiplying the probability $(P)$, vulnerability $(V)$, and consequences $(C)$ (Torres et al. 2009)

![img-3.jpeg](img-3.jpeg)

Fig. 4 Schematic of the Roodasht irrigation network risk assessment model based on FDBN model

The hydrodynamic model is run according to instructions in the non-structural technique. These instructions specify the time and amount of flow for opening and closing intakes. The structural method altered the catchment structures from Neyrpic gates to adjustable sliding gates. The slide gates can modify the water flow in different flows, making flow adjustment easier. Neyrpic gate structures only have an on/off mode and pass certain flows.

The ID simulator model is linked to the controller code of the proportional-integral model in MATLAB for the automatic control approach. The adjusting structures in this method are the slide gates connected to the motor, and the motor attached to the controller determines how much each of the 26 adjusting structures can be opened or closed. The MPC control approach is similar, except instead of a controller core, a centralized controller is used. Each of the 26 adjustment structures is controlled by a single controller.

# 3 Results and Discussion 

This study developed a structure to assess the integrated risk of agricultural water supply and distribution systems. The North Roodasht irrigation district was selected to evaluate this risk assessment model. Studies indicate that drought hazards, improper operator performance, and operating losses are the most critical threats to the irrigation network in this area. The base period selected is from 2011 to 2017.

To manage the system's risk, structural, non-structural, automatic control, and combined scenarios were defined. The most efficient scenarios were determined based on technical, economic, social, and environmental evaluation criteria. Finally, scenarios were ranked using MCDM methods, including TOPSIS, WASPAS, and MultiMoora, and the results were integrated with the Copeland method.

### 3.1 The Results of Risk Assessment and FDBN Model

The risk assessment results of the different components of the system (supply and distribution) are shown in Fig. 5. The risk of the distribution part of the system is in the range of 0.5 to 46.4 percent, and on average this amount is equal to 14.0 percent. The average risk

![img-4.jpeg](img-4.jpeg)

Fig. 5 Risk of supply, distribution, and system of Roodasht irrigation district
of the supply component is equal to 11.5 percent. The risk values of the distribution part are greater than the supply. The distribution system is influenced by the water conditions supplied by the surface water source and by threatening hazards. In other words, although a hazard such as a drought can considerably impact system performance, other hazards such as operational losses or improper performance of the ditch-riders can cause the system to fail if even sufficient water is available. All system components and indexes are effective in assessing the risk of the system. The amount of risk of the system is 0.3 to 51.8 percent, with an average of $12.7 \%$.

In arid regions where drought is a major concern, this risk assessment model shows that even with sufficient water, the system may still fail to distribute it properly. Thus, other hazards should be addressed as well. After developing the risk assessment model, it is implemented using the FDBN model in GeNIe and Python (Fig. 6). The model's structure, nodes, and causal and temporal relationships are defined, and fuzzified parameters are input. The output is then retrieved, with accuracy calculated for each run. The model is trained and tested using ten-fold cross-validation, as shown in Table 2. The final accuracy, averaging $90 \%$, is used for assessing risk management scenarios.

After modeling and reviewing the results, the FDBN model evaluates the impact of risk management scenarios on system risk reduction. These scenarios are applied across all time steps, primarily focusing on root nodes. While parameters like area under cultivation and river discharge remain constant, groundwater withdrawal and intake water volume vary with each scenario. The discrete output of the FDBN model is evaluated using the expected
![img-5.jpeg](img-5.jpeg)

Fig. 6 FDBN model

Table 2 The accuracy of FDBN model


value method. Risk values are classified into three classes, and the effects of risk reduction scenarios on each class and the system as a whole are examined. The results of applying these scenarios are depicted in Fig. 7.
![img-6.jpeg](img-6.jpeg)
(a)
![img-7.jpeg](img-7.jpeg)
(b)

Fig. 7 Results of risk reduction scenarios (a) average risk of the system and (b) cumulative risk of the system in three classes $(\mathrm{L})$ low, $(\mathrm{M})$ medium and $(\mathrm{H})$ high

Automated and combined control scenarios outperformed structural and non-structural ones. Automated scenarios reduced the system's average risk by over $10 \%$, while scenario 10 (inflow fluctuation prediction and structural actions) reduced it by $7.8 \%$. Non-structural scenarios decreased risk by an average of $5.5 \%$, and the structural scenario (scenario 5) reduced it by $4.7 \%$. Average high-risk values decreased by $13.36 \%$ from 46.7 with scenario implementation.

Overall, all scenarios reduced the average risk across low, medium, and high classes by $1.5 \%, 11.5 \%$, and $13.4 \%$, respectively (Fig. 7a). Scenarios 6, 7, and 10 were particularly effective, reducing cumulative high-risk by up to $67.5 \%$ during the base period (Fig. 7b). With the scenarios identified and their risk reduction capabilities assessed, it's now essential to evaluate them from other criteria perspectives.

# 3.2 The Results of the Evaluation Criteria 

Multiple criteria are defined to assess the performance of risk management scenarios, including technical, economic, social, and environmental factors. Under the economic criterion, the cost of implementing modernization scenarios and the profit from modernizing the surface water distribution system are specified as sub-criteria (Fig. 8). Reducing losses in surface water transmission and distribution systems boosts profits from agricultural production. For the Roodasht network's cultivation pattern (wheat, barley, alfalfa, beet, and safflower), the average monthly profit per hectare is approximately $\$ 1384$ (based on collected data from Isfahan Regional Water Company). This profit is the gross profit minus production costs and the expenses of operating and maintaining the pumping station. Figure 8 illustrates the results for various scenarios in this section.

This figure shows that the cost of implementing Scenario 6 (MPC) is higher than all other scenarios, and the lowest cost of implementing scenarios is related to non-structural scenarios. This index is defined as a negative indicator. The equipment used for automatic control scenarios is higher than other scenarios, so it has a lower rank than lower cost scenarios such as non-structural ones. PI and MPC scenarios, then combined scenarios, have the best performance in the profit index from the modernization of the surface water distribution system.
![img-8.jpeg](img-8.jpeg)

Fig. 8 Results of economic criteria of risk management scenarios

![img-9.jpeg](img-9.jpeg)

Fig. 9 Results of social criteria of risk management scenarios

The social criterion is divided into two sub-criteria: 1- The equity of water delivery, 2Employment. The result of these criteria is shown in Fig. 9.

In the Roodasht irrigation district, water delivery equity is only $16 \%$, with automated control scenarios proving most effective. Reduced groundwater usage also lowers withdrawal costs, allowing farmers to hire more workers, typically 3-4 per hectare. Scenarios 6 and 7 require the most labor, followed by combined ( 8 to 11 ) and non-structural ( 1 to 4) scenarios. The environmental criterion includes reducing groundwater withdrawal and energy savings. Groundwater reduction is derived from hydrodynamic models, while energy savings stem from decreased withdrawal. Economic criteria results are depicted in Fig. 10.

Sub-criteria for reducing groundwater withdrawal and saving energy are defined as positive criteria, mutually influencing each other. Results indicate that Scenarios 6 and 7 most effectively reduce groundwater withdrawal, followed by Scenarios 8 (structural and scheduled water delivery) and 11 (structural and increased inlet recharge, reduced flow time). The weakest performance is observed in Scenarios 2 and 5 (reducing dewatering time and structural).
![img-10.jpeg](img-10.jpeg)

Fig. 10 Results of environmental criteria of risk management scenarios

![img-11.jpeg](img-11.jpeg)

Fig. 11 Results of technical criteria of risk management scenarios

The scenarios' impact on reducing the system's average risk is evaluated using the FDBN model of the Roodasht irrigation district, considered a technical criterion. Figure 11 illustrates the reduction in the system's average risk in each scenario. The top three scenarios are automated control, and the combined scenario of structural changes and inflow fluctuation prediction.

# 3.3 Weighting Criteria and Ranking Results 

The criteria values for each risk management scenario formed the decision matrix (Table 3). They need to be weighted through the AHP method to rank different scenarios using MCDM tools.

In this step, experts evaluate the importance of criteria. AHP method is used as a proper method in comparing two by two criteria and estimating their weighting coefficients. Determining the coefficients is based on the AHP method and using questionnaires. A sample questionnaire is shown in the appendix, and the survey results and values of coefficients are presented below.

This questionnaire has been filled out from different perspectives by university professors, regional water experts, experts from the irrigation network operation office, and experts from the region's environmental organization. The results of the criteria weight are shown in Table 3 for the four main criteria and sub-criteria.

The risk management scenarios in the Roodasht irrigation district were ranked using TOPSIS, MultiMoora, and WASPAS methods (Table 4). Each method employs different logic for ranking scenarios, yet all produce consistent and robust results. The top three scenarios are consistently selected by all methods, indicating their superiority. Additionally, the Copeland method is used to integrate these results, with Table 4 presenting the combined rankings.

The table reveals that rankings from MCDM methods are largely similar, with final rankings determined by the Copeland method. Scenario 7 (PI) emerges as the top choice, followed by Scenario 6 (MPC), both associated with automated control methods.

Automated control methods excel due to their equipment precision, eliminating operator error, managing water efficiently, and meeting network demand. Despite higher costs, they

Table 3 Decision matrix


Table 4 Results of multi-criteria decision ranking methods


outperform other scenarios in reducing groundwater withdrawal (environmental criterion) and increasing labor (social criterion).

Next in performance are scenarios 8,10 , and 11, which combine structural methods with scheduled water delivery, inflow fluctuation prediction, increased inlet recharge, and reduced irrigation canal flow time, integrating structural and non-structural actions for better system performance. The results suggest two solutions for network managers: a shortterm and a long-term approach. The short-term solution involves quickly implementing a combined scenario, which includes setting up a simple telemetry system, increasing daily operation shifts, and improving inspections. If effective, this will create the conditions for a long-term solution with an automated distribution system.

Scenarios 1, 4, and 3, focused on scheduled water delivery and flow time reduction, follow and align with the combined scenarios, making scenario 1 a strong non-structural option. The lowest rankings go to scenarios 9, 2, and 5. Scenario 9 combines scenario 2 (reducing dewatering time) and scenario 5 (structural). While scenarios 2 and 5 individually reduce risk well, they perform poorly on economic and social criteria.

# 4 Conclusion 

In this study, the risk assessment structure is modeled by FDBN, evaluating risk management scenarios across various criteria. MCDM methods determine the best scenarios. The results show that the FDBN model's accuracy is 0.90 . Risk management scenarios are ranked based on economic, social, environmental, and technical criteria using MCDM methods (TOPSIS, WASPAS, MultiMoora, and Copeland). The top scenarios are PI and MPC as automated control scenarios, followed by combined scenarios (structural and scheduled water delivery, inflow fluctuation prediction, increasing inlet recharge, and reducing flow time in the irrigation canal). These top scenarios offer short-term and long-term solutions, with the combined scenario proposed for quick implementation in the short term. Decision-makers and network operators can utilize this model to make informed decisions in risky situations, predicting risks and providing solutions. The FDBN model can predict risks from individual components to the entire system with minimal input parameters. This model can be adapted for other systems facing multiple threats by defining parameters and logical relationships. It can

enhance the operation of agricultural water systems, designing risk management alternatives based on budget and available resources, and evaluating their effects. The model can also be applied in further studies to assess risk under climate change conditions, integrating spatial and temporal analysis methods for comprehensive control of connected networks.

Authors Contributions Atiyeh Bozorgi: Investigation, Methodology, Software, Formal analysis, Writing -original draft Abbas Roozbahani: Conceptualization, Supervision, Validation, Writing—Review \& Editing. Seied Mehdy Hashemy Shahdany: Supervision, Validation, Writing—Review \& Editing. Rouzbeh Abbassi: Validation, Writing—Review \& Editing.

Funding Open access funding provided by Norwegian University of Life Sciences

# Declarations 

Ethical Approval Not applicable.
Consent to Participate Not applicable.
Consent to Publish Not applicable.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

# Authors and Affiliations 

## Atiyeh Bozorgi ${ }^{1} \cdot$ Abbas Roozbahani ${ }^{2} \odot \cdot$ Seied Mehdy Hashemy Shahdany ${ }^{3}$. Rouzbeh Abbassi ${ }^{1}$

$\boxtimes$ Abbas Roozbahani
abbas.roozbahani@nmbu.no
$\boxtimes$ Seied Mehdy Hashemy Shahdany
mehdi.hashemy@ut.ac.ir
Atiyeh Bozorgi
atiyeh.bozorgi@hdr.mq.edu.au
Rouzbeh Abbassi
rouzbeh.abbassi@mq.edu.au
1 School of Engineering, Faculty of Science and Engineering, Macquarie University, Sydney, NSW, Australia
2 Faculty of Science and Technology, Norwegian University of Life Sciences (NMBU), Ås, Norway
3 Faculty of Agricultural Technology, College of Agriculture and Natural Resources, University of Tehran, Tehran, Iran