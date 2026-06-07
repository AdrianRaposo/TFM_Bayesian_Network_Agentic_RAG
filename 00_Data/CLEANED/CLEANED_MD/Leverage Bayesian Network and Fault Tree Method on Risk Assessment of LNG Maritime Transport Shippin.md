# Article 

## Leverage Bayesian Network and Fault Tree Method on Risk Assessment of LNG Maritime Transport Shipping Routes: Application to the China-Australia Route

Zheng Chang ${ }^{1}$, Xuzhuo He ${ }^{1}$, Hanwen Fan ${ }^{1, * *}$, Wei Guan ${ }^{2 *}$ and Linsheng He ${ }^{3}$

## check for updates

Citation: Chang, Z.; He, X.; Fan, H.; Guan, W.; He, L. Leverage Bayesian Network and Fault Tree Method on Risk Assessment of LNG Maritime Transport Shipping Routes: Application to the China-Australia Route. J. Mar. Sci. Eng. 2023, 11, 1722. https://doi.org/10.3390/ jmse11091722

Academic Editor: Claudio Ferrari
Received: 7 August 2023
Revised: 21 August 2023
Accepted: 29 August 2023
Published: 1 September 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Transportation Engineering, Dalian Maritime University, Dalian 116026, China; chang_zheng@dlmu.edu.cn (Z.C.); hexvzhuo@163.com (X.H.)
2 Navigation College, Dalian Maritime University, Dalian 116026, China; gwwtxdy@163.com
3 Shandong Shipping Tanker Co., Qingdao 266000, China; tanker-safety@sdshipping.cn

* Correspondence: hwfan@dlmu.edu.cn

Abstract: The China-Australia Route, which serves as the southern economic corridor of the '21st Century Maritime Silk Road', bears great importance in safeguarding maritime transportation operations. This route plays a crucial role in ensuring the security and efficiency of such activities. To pre-assess the risks of this route, this paper presents a two-stage analytical framework that combines fault tree analysis and Bayesian network for evaluating the occurrence likelihood of risk of transporting liquefied natural gas (LNG) on the China-Australia Route. In the first stage, our study involved the identification of 22 risk influencing factors drawn from a comprehensive review of pertinent literature and an in-depth analysis of accident reports. These identified factors were then utilized as basic events to construct a fault tree. Later, we applied an expert comprehensive evaluation method and fuzzy set theory, and by introducing voting mechanism into expert opinions, the prior probability of basic events was calculated. In the second stage, a fault tree was transformed into a Bayesian network, which overcame the deficiency that the structure and conditional probability table of the Bayesian network find difficult to determine. Consequently, the employment of the Bayesian network architecture was applied to forecast the likelihood of LNG maritime transport along the China-Australia shipping pathway. The probability importance and critical importance of each basic event was calculated through an importance analysis. The development of a risk matrix was achieved by considering the two primary dimensions of frequency and impact, which were subsequently utilized to categorize all relevant risk factors into high, moderate, or low risk categories. This allowed for effective risk mitigation and prevention strategies to be implemented. Finally, assuming that the final risk occurs, we calculated the posterior probability of the basic event to diagnose the risk. The research findings indicate that the primary reasons for the risk of transporting LNG on the China-Australia Route are the impact of natural forces and epidemics, piracy and terrorist attacks, and the risk of LNG explosions. In the final section, we provide suggestions and risk control measures based on the research results to reduce the occurrence of risks.

Keywords: risk assessment; maritime transport; fault tree analysis; Bayesian network; Liquid Natural Gas (LNG)

## 1. Introduction

The rapid development of the shipping industry has significantly contributed to the growth of global trade, but it has also posed challenges to maritime safety [1]. The safety of routes has emerged as a critical domain of emphasis for the shipping sector and its associated enterprises. As the southward economic channel of the '21st Century Maritime Silk Road', the China-Australia and New Zealand route has gained significant attention for its transportation function and significance. However, according to a report by the International Maritime Organization, the safety situation of maritime transportation along

this route is not optimistic. Nevertheless, as per a report published by the International Maritime Organization, the safety status of maritime transportation along this course is not sanguine. How to scientifically and reasonably build the risk assessment model of the route is an important premise and calls for mastering the risk status of the route and identifying the influencing factors in the risk scenario.

From 2010 to 2023, very serious levels of maritime casualties and accidents accounted for $60-70 \%$ of the total number of accidents along the China-Australia and New Zealand route, highlighting the seriousness of safety risks along the route. For example, on 17 May 2023, a fishing vessel from China to Australia capsized in the Indian Ocean. The vessel with 39 crewmembers onboard is still missing. To ensure the sustainable development of the shipping industry, preventing maritime accidents and ensuring safety at sea should be the primary goal of the International Maritime Organization. Therefore, describing various risks and developing a quantitative evaluation model for the risk of LNG maritime transportation on this route to accurately predict and prevent risks that have not yet occurred can guide the safety of maritime transportation activities to a certain extent [2].

Previous studies have demonstrated that due to the numerous influencing factors involved in the indicator system, the diverse types and complex structures of indicators, as well as the participation of experts, maritime safety risk assessment problems have uncertainties brought about by the diverse types of indicators, structural uncertainties brought about by complex system structures, and cognitive uncertainties brought about by human cognitive limitations. Taking into account various uncertainties, risk factors including cargo characteristics, ship conditions, environmental conditions, human error, and management issues ensure that the safety of maritime transport is a complex task [3]. Addressing these challenges requires the collection and investigation of the latest data from recent maritime accidents, analysis of the causes of such accidents, identification of key risk influential factors (RIFs) under different scenarios, and the prediction of associated risks.

While classical risk analysis methods, including Failure Mode and Effects Analysis, Analytic Hierarchy Process, Markov Model, Human Factors Analysis and Classification System, and Fault Tree Analysis (FTA), have been widely used to identify critical factors for enhancing maritime safety, they are not practical for uncertain risk analysis with changing environmental conditions [4]. Among these models, Failure Mode and Effects Analysis with transparent and simple features [5] and Analytic Hierarchy Process with the ability to assign different weights to indicators [6] are widely used. However, both methods require experts to make evaluations in highly complex assessment environments [7]. Professional level, personality traits, and subjective judgment can all affect the ability to make accurate evaluations, leading to ambiguity and uncertainty in the final results, which cannot be used for risk assessment under multiple indicators. Human Factors Analysis and Classification System is designed to analyze different degrees of human factors in accidents. Celik M [8] introduced the Human Factors Analysis and Classification System model for water traffic accidents and identified the lowest level human factors in the model through a fuzzy analytic hierarchy process. However, its shortcomings are obvious. This method is only applicable to risk assessment caused by human factors in smaller models and cannot express other relevant factors. These limitations have necessitated the development of advanced risk analysis methods, such as Fuzzy Logic (FL) and the Bayesian Network.

Among the advanced methods used for maritime risk analysis, BN has gained significant attention due to its ability to explain the relationships among multiple variables under uncertainty, based on probabilistic information for risk assessment. Risk analysis using BN has become a promising technique in complex and uncertain shipping scenarios [9]. For example, Fan et al. [10] used the Naïve Bayesian Network (NBN) to model maritime accident risk analysis and identified 16 RIFs based on the analysis of 161 accident reports collected from 2012 to 2017. Similarly, Jiang and Lu [11] proposed a dynamic Bayesian network (DBN) model to assess dynamic contingencies in the Indian Ocean sea lanes based on incident data from 2007 to 2018.

However, the Bayesian network faces some challenges when capturing the conditional probability tables (CPTs) among the influencing factors and make it hard to determine a rations structure among the nodes: (1) when determining the CPT, the traditional method is expert scoring or data-driven, but these two methods require a high number of data samples, consuming time and energy; and (2) regarding structural learning, expert judgment is usually introduced, which can lead to strong subjectivity and bias, especially when multiple nodes are involved. Zhao [8] has shown that FTA can cleverly solve this problem, and combining FTA and BN can be used for maritime risk analysis under complex environmental impacts, which can be beneficial in compensating for their respective shortcomings. They use fuzzy fault tree analysis and noise or gate Bayesian network to estimate the probability of navigation accidents. The fault tree analysis is constructed from the navigation accident investigation report, and then the fault tree analysis is transformed into a Bayesian network using Noisy-OR gate. Finally, the model was applied to Qinzhou Port and reasonable conclusions were drawn by comparing it with the calculation results of other waterways.

This paper endeavors to rectify the aforementioned shortcomings by presenting the following measures. The primary objective of this paper is to propose a two-stage model framework for evaluating the risk of LNG maritime transport on the China-Australia route. The first stage involves constructing a fault tree based on the influencing factors identified from the related literature and accident reports, followed by calculating the prior probability of basic events using the expert comprehensive evaluation method and fuzzy set theory. In the second stage, the fault tree is transformed to a BN model, and the results of FTA in the first stage are input into the BN model in the second stage as initial values. After completing the BN model validation, the next step is to predict, prevent, and diagnose the risk of LNG maritime transport, and introduce a risk matrix to analyze the risks from the perspectives of importance and frequency. This paper offers three significant contributions: (1) the introduction of fuzzy set theory and expert voting mechanism addresses the challenges associated with handling conflicts in expert opinions and the inherent fuzziness in the expert scoring process and enriches the application of expert scoring methods in the field of risk assessment; (2) the probability importance degree and key importance degree obtained from the fault tree analysis are regarded as two inputs of the risk matrix. This enables decision-makers to clearly perceive the frequency and severity of risks, as well as their interrelationships, and assigns them priority levels, expanding the application and development of traditional risk management theory where risk is directly multiplied by frequency and importance; and (3) the richness of influencing factors in the LNG maritime transportation process leads to the complexity and uncertainty of the indicator system structure. Through the transformation of FTA to BN, a rational and scientific Bayesian risk assessment model has been constructed, expanding the application of LNG risk transportation under uncertain factors.

The remainder of this paper is organized as follows. Section 2 reviews the literature related to maritime accident research and the application of BN and FTA in maritime risk analysis and explores relevant research gaps. Section 3 proposes a risk assessment framework for LNG maritime transportation. This includes an illustration of the basic theory, identification of influencing factors in the risk assessment model, and explanation of the voting mechanism and risk matrix used in the subsequent analysis. In Section 4, the methodology is applied to evaluate the risk of LNG maritime transport on the China-Australia route. Section 5 proposes improvement measures for risks with a high impact on the model output.

# 2. Literature Review 

### 2.1. Risk Assessment of LNG Maritime Transport

LNG maritime transportation belongs to high-risk cargo transportation, and there is rich research in the academic community on the risks of LNG maritime transportation. Vanem et al. [12] conducted a high-risk assessment of the global navigation of LNG ships. The analysis collects and combines information from multiple sources and available infor-

mation from different sources has been structured in the form of event trees for different generic accident categories. Five different types of LNG-related risks have been identified, namely collision, grounding, contact, fire and explosion, and accidents that occur during loading and unloading at the dock. The results showed that the highest risk is collision. On the basis of traditional evaluation models, Martins [13] proposed a complete quantitative risk analysis method (QRA) for potential risk accidents that may occur during the offshore terminal loading and unloading processes of LNG ships. By comparing it to traditional models, the advantages and limitations of the new model are pointed out. Marroni et al. [14] developed a simplified method for the risk assessment of LNG ships in port areas. Based on the standard characteristics of the ship, a set of reference accident scenarios that need to be considered in risk assessment has been determined, providing specific guidance for determining hazards, estimating frequency of occurrence, and consequences. Finally, a customized risk matrix was adopted to support decisions on prevention and mitigation measures. Abdussamie et al. [15] proposed a fuzzy set method to deal with the uncertainty in expert opinions used in qualitative risk assessment research (such as a risk matrix). The risk parameters are modeled using fuzzy set, and the fuzzy risk values of several dangerous scenarios at different stages of the ship berthing operation are calculated.

Among the existing methods for quantitative risk analysis, fault tree analysis (FTA) and Bayesian network (BN) are conventional tools. For example, Zhou [16] took the loading and unloading process of a ship as an example, constructed a modified FTA for ship accident leakage, and introduced human reliability analysis (HRA) to predict human errors in the loading and unloading processes of LNG ships. Finally, the results of FTA and human reliability analysis are combined, and a Monte Carlo simulation (MCS) is used to evaluate the risk. Additionally, Zhao et al. [17] used Bayesian network to identify potential risks, calculate accident probability, and evaluate the severity of consequences for the safe anchoring system of LNG ships. Yeo [18] analyzed and identified potential hazardous events that may occur during the unloading process of LNG transport vessels at floating terminals. They use Bayesian networks to dynamically analyze the safety of LNG ships during loading and unloading to identify the most likely types of accidents. The result is similar to Vanem: collision is the most probable accident to occur during the offloading process of an LNG carrier at berth, which may have catastrophic consequences. Li et al. [19] proposed a process risk-based decision-making method for LNG ships colliding with Arctic Sea ice or obstacles based on the dynamic Bayesian network (DBN) risk assessment model, indicating that the decision-making process of ship navigation is dynamically related to time. Additionally, Melani et al. [20] combined the two methods, using FTA to analyze the failure of the unloading equipment of LNG ships. They combined it with pre-hazard analysis and causality diagram to calculate the probability of various accidents through Bayesian probability. Finally, they used the risk matrix for risk analysis and provided corresponding improvement measures and suggestions.

# 2.2. FTA and BN in Maritime Risk Analysis 

In this section, the advantages of FTA and BN in risk modelling are further demonstrated by a systematic review of its applications in maritime accident/risk analysis. FTA and BN models have been extensively applied in the field of maritime transport risk assessment and have yielded several notable results. FTA aims to determine the root cause by using a top-down method to build the accident chain and evaluate its impact on the accident. Fu et al. [21] proposed a fuzzy event tree method for Frank copula, which evaluated the risk of major ship accidents in Arctic waters under the consideration of uncertainty. Ugurlu [22] used FTA for qualitative and quantitative analysis to determine the root causes of ship-to-ship collisions statistically. Results show that the violation of the COLREG Rules is the most important and effective factor for collision accidents.

A Bayesian network model is used for quantitative assessment of risks under certain conditions. For instance, Wan et al. [23] develop a novel model to assess the risk factors of maritime supply chains by incorporating a fuzzy belief rule approach with Bayesian

networks. The new model, compared to traditional risk analysis methods, has the capability of improving result accuracy under a high uncertainty in risk data. In another study, Baksh et al. [24] employed BN to assess the transport risks during navigation in the Arctic Sea. The researchers first discussed the causes of maritime accidents and calculated the prior probability of Bayesian network nodes based on historical data and expert judgment. Subsequently, the possibility of accidents was determined through a sensitivity analysis of the model. The results revealed that sea ice was the main influencing factor of the accident, and appropriate management measures were proposed accordingly. Additionally, Chen et al. [25] proposed an evidence-based fuzzy Bayesian network method to build a maritime accident Statistical model. Using maritime accident reports, the Bayesian network was constructed from a systematic perspective and its reliability was verified by three axioms.

FTA can establish a linear or sequential relationship between events leading to an accident and provide a known conditional probability table and a clear model structure for the Bayesian network. For example, Sakar et al. [26] mapped FTA to BN to analyze the causes of grounding accidents and found that navigation factors had the most significant impact on grounding accidents. Sokukcu et al. [27] considered the limitations of Fault tree analysis in terms of conditional dependence and stationarity, proposed a Bayesian network mapping method based on Fault tree analysis to overcome this limitation, and conducted a probabilistic risk analysis on collision events. Kaushik et al. [28] proposed a comprehensive method based on intuitionistic fuzzy fault tree and Bayesian network to evaluate the fault probability of a system in cases of imprecise and insufficient fault data. The results indicate that when the statistical failure data of components are inaccurate, this method can be used as an alternative method for reliability probability assessment.

Based on the literature review presented above, two research gaps have been identified: (1) regarding structural learning, most studies use data-driven TAN or traditional BN models, which require expert guidance or data-driven development, leading to high energy and time consumption. Additionally, when multiple evaluation indicators are involved, determining the causal relationship between nodes and CPT in the network can be challenging. To address these issues, a FTA transformation method can be applied to remedy the structural defects of a traditional BN model and (2) when obtaining the quantitative value of the prior probability of the root nodes, most studies use the method of expert questionnaire. However, the possible deviations in the questionnaire results are not handled, resulting in a large deviation in the prior probability of some root nodes. By introducing an expert voting mechanism, we consider screening and retaining the expert opinions with significant deviations. Thus, the accurate prior probability value can be obtained.

In order to address the aforementioned gaps in the research, this study employs a comprehensive, multi-step framework. First, we identify risk factors that may lead to hazards in LNG maritime transport by reviewing relevant literature and develop a fault tree model accordingly. Next, the probability of failure of basic events is calculated according to the fuzzy set theory and expert scoring method. W also introduce a voting mechanism into expert scoring results to handle results with significant differences in opinions. For example, when experts have similar ratings for the frequency of events, their opinions are taken into consideration for subsequent analysis. However, when most experts give a relatively unified opinion on the frequency of an event, while very few experts have opposite opinions, the opinions of the very few experts are discarded, and the unified opinions of other experts are retained.

Then, the fault tree is transformed into a Bayesian network, and the risk prediction, prevention, and diagnosis are carried out in turn. The novelty of this research lies in integrating the fault tree with the Bayesian network, where FTA analyzes the causal relationship between risk factors, compensating for the challenge of determining the causal relationship of nodes in the Bayesian network model. After establishing the Bayesian network model, we can perform forward prediction and backward diagnosis, which overcome the limitation of the fault tree's inability to carry out probabilistic quantitative analysis.

# 3. Model Construction 

### 3.1. Establish a Maritime Risk Assessment Framework

FTA and BN are two widely used methods for risk assessment. However, using FTA for risk assessment requires calculating the top event state based on the probability of basic events, resulting in generating a large number of calculations when reasoning in the forward direction, and backward reasoning cannot be carried out in this model. These problems can be overcome in the BN model, which allows for both forward and backward reasoning. Additionally, fault tree transformation is the primary approach for constructing a Bayesian network.

Maritime risk analysis studies that use FTA-BN are typically conducted through several established steps, including data collection, variable identification, FTA structure transformation, BN model validation, and sensitivity analysis [29]. The methodology in this paper is no exception, and it consists of five parts: (1) identification of variables, (2) construction of the fault tree, (3) transformation of the fault tree into a Bayesian network, (4) calculation of the probability of root nodes, and (5) risk prediction, prevention, and diagnosis, as depicted in Figure 1.

### 3.2. Risk Factor Identification

RIFs, which stands for Risk Influencing Factors, are the variables that impact the security and safety of maritime transportation. Identifying risk influencing factors can provide support for subsequent survey questionnaires, concretizing and digitizing indicators. This can identify potential problems in the entire process of LNG maritime transportation and provide complete and scientific information for risk control measures. The widely used identification method currently is to identify RIFs based on the construction of a maritime accident database, utilizing relevant literature and the existing maritime accident record guidance from the IMO. After searching on the Web of Science, 16 typical journal papers were selected, which described the risk factors and were further analyzed against each of the retrieved results, as shown in Appendix A. Next, 22 RIFs were identified and are listed in Figure 2, with the frequency of occurrence of each risk factor. It is evident that the safety performance of LNG ships, high waves, heavy fog, strong sea breeze, unsafe behavior of personnel, piracy, and terrorist attacks are the top six RIFs identified in previous research. Once the RIFs were identified, previous studies in the field usually simplified the definition of their states to reduce the high data demand in quantifying their interdependencies, such as CPTs in BN. In this paper, all RIFs were set to two states: normal and fault. Experts scored the occurrence frequency of each RIF, and the fault probability was obtained through data processing, which was then input into the BN as prior probability.

### 3.3. Fault Tree Construction

FTA is a well-structured and widely used tool for the risk assessment and root cause analysis (RCA) of complex systems. In a fault tree there are top events, intermediate events, and basic events. The fault tree analysis begins with a final result, which is the top event, and decomposes layer by layer from top to bottom according to the causal relationship of logic gates until it cannot be decomposed any further. Finally, the basic events that caused the final failure are identified. This method can intuitively analyze various ways of system fault occurrence, effectively finding the fault source of the system. FTA produces graphical displays that show the logical connections between failure and the path toward the failure of a system. Due to the visualization and predictability of FTA, it has been widely used in the maritime field [21].

The event structure and relationship of the risks associated with the maritime transportation of liquefied natural gas (LNG) are illustrated in Table 1. This table outlines the specific factors that are represented by each event, and their relationship with intermediate events.

![img-0.jpeg](img-0.jpeg)

Figure 1. Developed framework for maritime transport risk assessment.

![img-1.jpeg](img-1.jpeg)

Figure 2. Frequency of RIFs in the retrieved literature and accident reports.
In view of the event design for the risk fault tree of LNG maritime transport in Table 1, this paper obtained the fault tree structure by drawing with Visio, as shown in Figure 3.

# 3.4. Introduce Fuzzy Set to Obtain Probability of Basic Events 

The fuzzy set theory (FST) was introduced by Zadeh [30] as a means of dealing with imprecision and vagueness. A fuzzy set on a given domain $U$ means that, for any $x \in U$, there is a number $u(x) \in[0,1]$ corresponding to it. The membership function $u(x)$ represents the membership value of $x$ in $U$. The triangular fuzzy number is a simple and widely used method for representing the membership function, where $a$ and $b$ are the lower and upper limits of the fuzzy number, respectively, and $m$ is the value with the highest possibility. In this paper, a triangular fuzzy number $U=(a, m, b)$ is utilized to represent the fuzzy failure probability of the nodes, and the membership function is given by Equation (1).

$$
u(x)=\left\{\begin{array}{l}
\frac{x-a}{m-a}, a<x \leq m \\
\frac{b-x}{b-m}, m<x \leq b \\
0, \text { otherwise }
\end{array}\right.
$$

The expert survey method has been widely used in risk research as an effective and feasible approach. However, this method solely focuses on the level of the expert judgment's ability, while ignoring the uncertainty in expert judgment. This can result in a certain degree of deviation in data reliability, which greatly impacts the subsequent evaluation. To address this issue, this paper proposes an expert survey method based on the confidence index, which takes into account the subjective reliability of the experts.

Table 1. Event structure relationship for risk of LNG maritime transport.


![img-2.jpeg](img-2.jpeg)

Figure 3. Fault tree diagram of LNG maritime transport risk assessment.
Firstly, the expert judgment ability, denoted as $\xi$, was categorized into five levels, represented by 'I, II, III, IV, and V' and corresponding to the values ' $0.6,0.7,0.8,0.9$, and $1.0^{\prime}$, respectively. A smaller $\xi$ value indicates less reliable expert judgment ability. The subjective reliability, represented by $\psi$, measures the degree of reliability of the expert

in their judgment and is divided into five levels, denoted as ' $0.6,0.7,0.8,0.9$, and $1.0^{\prime}$, respectively. A higher level of subjective reliability $\psi$ indicates a more reliable judgment. Assuming that $m$ experts participate in the survey, the confidence index $\delta_{n}$ of the nth expert can be calculated using Equation (2).

$$
\delta_{n}=\zeta_{n} \times \psi_{n}
$$

Secondly, in this paper, we adopt five fuzzy languages, namely 'very low (VL)', 'low (L)', 'medium (M)', 'high (H)', and 'very high (VH)', to describe the failure probability [31] of basic events. Table 2 illustrates the corresponding relationship between the linguistic variables and the failure probability intervals. The $i_{t h}$ interval is defined by its lower and upper bounds $\left[a_{i}, a_{i+1}\right]$, and its average value $c_{i}(1 \leq i \leq 5)$.

Table 2. Triangular fuzzy number assignment.


Multiple experts are selected to score the probability of failure of the basic event, usually the expert confidence level $\delta$ is less than 1 , which means that the remaining probability of the root node is $1-\delta$, distributed among other intervals. According to the Gaussian distribution pattern of random variables, the probability of failure tends to fluctuate around its expectation and gradually decreases as it moves away from the expectation. Therefore, a simplified formula for the distribution of residual probability $1-\delta$ in other intervals is proposed, as shown in Equations (3)-(5), where $a_{i}$ is the lower bound of the triangular fuzzy number in the $i_{t h}$ interval of failure probabilities.

$$
\begin{aligned}
P_{x_{n}}^{k} & =\left\{\begin{array}{l}
\delta, k=i(i=1) \\
\frac{\left(a_{5+2-k}-a_{1}\right)}{\sum_{n=2}^{i-1}\left(a_{n}-a_{1}\right)} \times(1-\delta), 2 \leq k \leq 5
\end{array}\right. \\
P_{x_{n}}^{k} & =\left\{\begin{array}{l}
\frac{\left(a_{i}-a_{i-k}\right)}{\sum_{n=1}^{i-1}\left(a_{i}-a_{n}\right)} \times \frac{1-\delta}{2}, 1 \leq k \leq i-1 \\
\delta, k=i \\
\frac{\left(a_{5+i-k}-a_{i}\right)}{\sum_{n=i+1}\left(a_{n}-a_{i}\right)} \times \frac{1-\delta}{2}, i+1 \leq k \leq 5
\end{array}\right. \\
P_{x_{n}}^{k} & =\left\{\begin{array}{l}
\frac{\left(a_{5}-a_{5-k}\right)}{\sum_{n=1}^{k}\left(a_{5}-a_{n}\right)} \times(1-\delta), 1 \leq k \leq 4 \\
\delta, k=i(i=5)
\end{array}\right.
\end{aligned}
$$

Thirdly, the failure probability evaluated by each expert on the root node $X_{n}$ can be obtained through Equation (6), where $\mathrm{c}_{\mathrm{k}}$ is the average value of the $K_{t h}$ failure probability interval, as shown in Table 2.

$$
P_{X_{n}}=\sum_{k=1}^{5}\left(c_{k} \times P_{x_{n}}^{k}\right)
$$

Fourthly, the fuzzy number $P^{*}$ of the failure probability of each basic event is obtained by calculating the mean value. Then, the failure probability $P$ of the basic event is calculated by solving the fuzzy, as shown in Equations (7) and (8) [25].

$$
\begin{gathered}
z=2.301\left(\frac{1-P^{*}}{P^{*}}\right)^{\frac{1}{3}} \\
P=\left\{\begin{array}{l}
\frac{1}{10^{*}}, P^{*} \neq 0 \\
0, P^{*}=0
\end{array}\right.
\end{gathered}
$$

# 3.5. Transforming the Fault Tree into Bayesian Network 

A Bayesian network is a directed acyclic graph (DAG) that encodes the joint probability distribution of a set of random variables [32]. As a tool for prediction, diagnosis, and reasoning, a BN can calculate the probability of risk occurrence. The Bayesian network has two types of reasoning: causal reasoning and diagnostic reasoning. Causal reasoning refers to predicting the probability of the failure of the target node based on the probability of the root node failure. Diagnostic reasoning involves assuming that the target node has a fault. Based on the degree of correlation between nodes, the possibility and importance of each root node can be obtained. This information can then be used to determine the specific reason for the occurrence of the target node.

The network diagram of BN can be observed as the qualitative part of the model, while the quantitative part of the model is composed of probability parameters. The joint probability of a set of random variables $\left(A_{1}, A_{2}, A_{3}, \ldots, A_{n}\right)$ based on the conditional independence and the chain rule can be obtained as follows:

$$
P\left(A_{1}, A_{2}, A_{3}, \ldots, A_{n}\right)=P\left(A_{1} \mid A_{2}, A_{3}, \ldots, A_{n}\right) P\left(A_{2} \mid A_{3}, \ldots, A_{n}\right) \ldots P\left(A_{n-1} \mid A_{n}\right) P\left(A_{n}\right)
$$

Bayes theorem [24] is used in the BN to update the failure probability (prior) of basic events given new observations to yield the consequence probability (posterior) using the following equation:

$$
P(A \mid B)=\frac{P(B \mid A) P(A)}{P(B)}
$$

where $P(A \mid B)$ is the posterior probability of $A$ if $B$ is true.
In addition to the posterior probability, the probability importance degree and the critical importance degree are also used to study the probability of the risk caused by the basic event.

Probability importance refers to the degree to which the change of probability of failure of basic events causes the change of probability of failure of top events. The specific calculation formula is as follows:

$$
I_{i}^{p r}=p\left(T=1 \mid a_{i}=1\right)-p\left(T=1 \mid a_{i}=0\right)
$$

Critical importance refers to the change rate of top event failure probability caused by the change rate of basic event failure probability, which essentially reflects the importance of basic events in the fault tree. The specific calculation formula is as follows:

$$
I_{i}^{c r}=p\left(A_{i}=1\right)\left[p\left(T=1 \mid a_{i}=1\right)-p\left(T=1 \mid a_{i}=0\right)\right] / p(T=1)
$$

where, $T$ is the top event; $P(T=1 \mid \cdot)$ is the conditional probability of the top event; $A_{i}=1,0$ indicates the status of occurrence or non-occurrence of basic event $i$; and $P\left(A_{i}\right)=1$ is the prior probability of the basic event $i$.

After establishing the relationships between events, logical relations, and symbols of the Bayesian network model in the fault tree, the fault tree was transformed into a Bayesian network, as shown in Figure 4. The top event in the fault tree is denoted by $T$, and the basic event is represented by $N=\left(x_{1}, x_{2}, \ldots \ldots, x_{n}\right)$. After transformation, the graphical

structure of the developed BN is shown in Figure 5. The colors of nodes represent the target node, intermediate node, and root node in order of depth to light.
![img-3.jpeg](img-3.jpeg)

Figure 4. Transformation diagram of AND-Gate and OR-Gate.
![img-4.jpeg](img-4.jpeg)

Figure 5. Bayesian network for risk assessment of LNG maritime transport.

# 4. Case Study 

### 4.1. Description of the China-Australia Route

The China-Australia route, starting from China, passes through Southeast Asian countries such as the Philippines and Indonesia, as well as the South China Sea, Banda Sea and other sea areas, and finally reaches Australia and South Pacific island countries. As China's offshore route, this route is a route channel with intensive and busy economic and trade exchanges with Australia and other countries, and it is also an important maritime transport channel for national strategic energy. China imports a large amount of energy and goods such as LNG and iron ore from Australia, which is the lifeline of China-Oceania import and export trade. Therefore, the shipping activities such as container transportation, LNG, iron ore, asphalt, and other bulk cargo transportation on the China-Australia route are active and frequent.

Due to the uncertainty of risks along the China-Australia route, there are certain impacts and losses along the route due to risks, providing a certain warning for the safe operation of the route. According to the statistics on maritime casualties and accidents released by the IMO, the statistics on maritime casualties and accidents along the route can be divided into three levels: very serious, serious, and not very serious. During 2006-2020 (the global shipping industry was impacted and affected by the global COVID-19 from 2020 to 2023, so there were fewer casualties and accidents at sea), the proportion of the very serious marine casualties and accidents along the line was basically $60-70 \%$. The proportion of serious maritime casualties and accidents is second, ranging from $20 \%$ to $30 \%$. The proportion of less serious maritime casualties and accidents is the smallest, around $10 \%$. This indicates that the consequences of maritime safety accidents caused by safety risks along the route are relatively serious. Therefore, the risk issues of the China-Australia route need to be taken seriously and security risk control along the route should be strengthened. In addition, according to a series of reports on Safety and Transportation Review issued by IMO, among the top ten loss areas in 2012-2019, southern China, Indonesia, and the Philippines have always been the key areas and focuses of ship losses. Among these key areas, the areas along the China-Australia route account for the vast majority, and the proportion of ship losses along the route remains around $20-30 \%$ globally. The significant safety risk losses indicate that the results caused by safety risks along the route are not optimistic and urgently need to be taken seriously by relevant parties.

# 4.2. Risk Prediction 

In the realm of risk analysis, the utilization of expert evaluation via questionnaires is widely regarded as a reliable approach to supplement the inadequacies inherent in incomplete data, thereby affording the opportunity to procure prior probabilities of greater precision. When selecting multiple experts to score the probability of failure of basic events, the judgment ability of each expert $(\xi)$ may be distinguished according to their working years.

The flowchart of the refinement stage of the voting mechanism is shown in step 3 of Figure 1. Firstly, each expert needs to choose a probability based on their own experience and research objectives. The five probabilities given by experts are all located in "very low (VL), low (L), medium (M), high (H), and very high (VH)". In the second step, expert opinions will be processed to further identify voting results with scores far below the average score for each factor. After discussion, it is believed that this situation was an accidental situation encountered by a certain expert and could not be symbolically summarized. Therefore, the excessive biased opinions in this situation are removed and the common opinions of the majority of experts are retained. The third step is to process and calculate the retained opinions into fuzzy set theory, converting them into probability values within the range of $(0,1)$. The prior probability of each basic event is obtained.

In this study, six experts were invited to conduct the expert judgements. Table 3 shows the allocation of experts according to their years of work experience, and the specific questionnaire survey results can be found in Appendix B.

Table 3. Expert assignment situation.


It can be observed from the questionnaire results that the scoring results of most basic events are relatively average. The Mean $c_{i}$ corresponding to each fuzzy language is averaged, and the error between the scoring results of six experts under 22 basic events and the average value is calculated, respectively. Five experts are involved, so a ratio of 0.2 is used for screening. We believe that scores exceeding the average value by $20 \%$ conflict with the opinions of most experts, so we have manually removed this situation to ensure consistency in expert judgment. If the error is within 0.2 , it is considered reasonable, and the scoring result error table is shown in Table 4. If the score error of four Basic events is higher than 0.2 , the expert opinion with a larger error in this case will be discarded and the other average expert opinions will be retained. In this way, the fairness of expert scoring opinions has been reasonably addressed. Meanwhile, the deviation of unequal information in the subjective judgment of experts is overcome, and the accuracy of the prior probability value of basic events is guaranteed.

Table 4. The scoring result deviation.


The prior probabilities of each basic event in LNG maritime transport risk can be calculated using Equations (3)-(8), and the calculation results are shown in Table 5.

Table 5. Probability transformation of expert language.


The probabilities of top event and intermediate events can be obtained after importing the prior probabilities of various basic events into the Bayesian network model. This step

becomes 'risk prediction'. By performing calculations using NETICA, the probability of the occurrence of risks during LNG maritime transport on the China-Australia route is 0.106, which is the predicted result. Due to the direct connection between the three intermediate events $\mathrm{I}_{1}, \mathrm{I}_{2}$, and $\mathrm{I}_{3}$ and the top event, they are considered as the direct cause of the risk occurrence. The direct causes of accidents are also evaluated, with a probability of 0.102 assigned to 'Shipping routes safety risks $\left(\mathrm{I}_{3}\right)^{\prime}, 4.53 \times 10^{-3}$ to 'LNG's own transport risks $\left(\mathrm{I}_{1}\right)^{\prime}$, and $9.82 \times 10^{-7}$ to 'Vessels and equipment risks $\left(\mathrm{I}_{2}\right)$ '. As a result, measures to reduce the risk of shipping routes should be prioritized over other risk-reduction measures.

# 4.3. Model Validation 

The validity of the BN model can be evaluated using the two axioms. The reliability of partial nodes in the network is verified by applying these axioms sequentially.

Axiom 1: The change of the failure probability of the target node is observed in the BN model by changing the prior probability value of the relevant intermediate node. This test determines whether the model meets the requirements of Axiom 1.

Axiom 2: The total impact of the combination of probability changes from 'evidence nodes' on the target value should always be greater than the combination of probability changes from 'secondary evidence nodes'.

The results of Axiom 1, depicted in Figure 6, show that the prior probability value of the target node and the intermediate node exhibit similar fluctuation trends. When the probability of the intermediate nodes being in the 'normal' state is $0 \%$, the probability of the target node being in the 'normal' state is also $0 \%$. This is because, in CPT, any abnormality in the three intermediate nodes leads to the occurrence of the final accident.
![img-5.jpeg](img-5.jpeg)

Figure 6. Test result of Axiom 1 under various prior probabilities.
To verify Axiom 2, it is necessary to first determine 'evidence nodes' and 'secondary evidence nodes'. The state of 'Safety of shipping routes $\left(\mathrm{I}_{3}\right)$ ' is related to 'Inherent risks of the airline itself $\left(\mathrm{I}_{4}\right)^{\prime}$, 'Influence of weather and sea state $\left(\mathrm{I}_{5}\right)^{\prime}$, 'Coastal ports risk $\left(\mathrm{I}_{6}\right)^{\prime}$, and 'Maritime security environment $\left(\mathrm{I}_{7}\right)$ '. Therefore, in this paper, 'Safety of shipping routes $\left(\mathrm{I}_{3}\right)^{\prime}$ is considered an 'evidence node', while 'inherent risks of the airline itself $\left(\mathrm{I}_{4}\right)^{\prime}$, 'Influence of weather and sea state $\left(\mathrm{I}_{5}\right)^{\prime}$, 'Coastal ports risk $\left(\mathrm{I}_{6}\right)^{\prime}$, and 'Maritime security environment $\left(\mathrm{I}_{7}\right)^{\prime}$ are regarded as 'secondary evidence nodes'.

When new evidence is introduced into the Bayesian network and the probability of four nodes being in the 'normal' state is $100 \%$, the probability of 'Risk of LNG maritime transport (T)' being in the 'normal' state is $89.4 \%, 93.5 \%, 90.9 \%$, and $93.5 \%$, respectively. When the probability of the four nodes being in the 'normal' state simultaneously is $100 \%$, the probability of 'Risk of LNG maritime transport (T)' being in the 'normal' state is $99.5 \%$. This value is greater than the probability value of 'Risk of LNG maritime transport (T)'

caused by the individual change probabilities of the four nodes, thereby satisfying the validation conditions of Axiom 2. In addition, tests were conducted on other corresponding secondary evidence nodes, which also met the validation criteria of Axiom 2.

# 4.4. Risk Prevention 

By calculating and ranking the critical importance and probability importance of basic events, it is possible to clarify the degree of influence of each event on the occurrence risk. Taking control measures for events with a high degree of impact and a relatively easy reduction in the failure probability can effectively prevent the occurrence of LNG maritime transport risk.

### 4.4.1. Calculation of Importance

The probability importance and critical importance of basic events can be calculated, and the results are shown in Table 6.

Table 6. Basic event significance calculation results.


### 4.4.2. Rank of Importance

The risk matrix is a qualitative analysis tool used to rank the likelihood and consequences and specify the level of risk. It mainly analyzes and evaluates risks from two dimensions: the likelihood of risk factors occurring, and the severity of damage caused. This evaluation method is a combination of qualitative and quantitative methods. The form of the risk matrix is represented by a two-dimensional table, and the basic risk matrix coordinate diagram is shown in Figure 7. By drawing a risk matrix diagram, multiple risks in the system can be more intuitively compared, and the corresponding order and methods of risk factors can be further determined based on the comparison results.

The basic risk matrix mainly divides the risk level into three regions: A, B, and C. If a risk factor is located in Region A, it is considered a high-level risk factor. Preventive measures should be taken well, and rules and regulations should be established to avoid such situations. If a risk factor is located in Region B, it is considered a moderate risk factor and reasonable control methods and solutions need to be developed. If a risk factor is in region C, it is considered a very low-level risk factor. Under the existing security management system, there is no need for additional control.

In order to comprehensively evaluate the risk of LNG maritime transport, the risk matrix analysis is introduced on the basis of the Bayesian network. Risk matrix is a qualitative analysis tool used to grade the possibility and consequence and specify the risk level. It can comprehensively represent the frequency and severity of risk accidents. According to the calculation results of probability importance and critical importance, they are standardized and presented in the table in the form of quadrants. By classifying the analyzed risks, we can obtain three different risk categories: 'high risk factor (HR)', 'medium risk factor (MR)', and 'low risk factor (LR)'. The specific division is shown in Figure 8.

![img-6.jpeg](img-6.jpeg)

Figure 7. Basic risk matrix.


Figure 8. Risk matrix.

### 4.4.3. Analysis of Importance Ranking Results

The high-risk factors are located at the intersection of the peaks of probability importance and critical importance, which means the events with a high risk of influencing top events and easily reduce the priori probability [33]. Taking measures to reduce the possibility of failure of these events will quickly and effectively reduce the risk of LNG maritime transport.

From the calculation results of probability importance, we find that there is no significant difference between the importance values of the top 14 basic events, which is much higher than the bottom 8. The order of critical importance of the top 14 is the same as probability importance, but the critical importance of the top 5 is far higher than that of others. Consequently, the fundamental occurrences associated with the uppermost five were scrutinized as perilous elements. Specifically, these comprise 'Non-traditional threat to security (I_{13})', 'Heavy fog (X_{10})', 'High frequency of strong winds (X_{13})', and 'Fewer LNG unloading ports (X_{14})'. First of all, non-traditional security threats along the China–Australia route are increasingly prominent. Piracy and terrorist attacks have

international characteristics, increasing the probability of transport risks. Moreover, the impact of the global epidemic has made maritime public health safety one of the important factors affecting transport risks. Therefore, we should include this factor in the assessment and response to transport risks and strengthen joint prevention and control measures to build a solid maritime security defense line. Secondly, 'Heavy fog $\left(\mathrm{X}_{10}\right)$ ' and 'High frequency of strong winds $\left(\mathrm{X}_{13}\right)$ ' fall under the category of 'Influence of weather and sea state $\left(\mathrm{I}_{5}\right)$ '. In case of severe weather, navigation ships need to take evasive measures such as entering the port or avoiding navigation. Finally, the small number of seaports on the China-Australia route has a high impact on LNG maritime transport risks, mainly because some ports along the route do not have facilities and equipment for LNG storage, loading, and unloading, resulting in poor connectivity with other ports, thereby increasing the risks in LNG transport.

Meanwhile, eight basic events with probability importance and critical importance close to zero are considered low-risk factors, namely 'Safety performance of LNG ships $\left(\mathrm{X}_{3}\right)^{\prime}$, 'Difficult handling of LNG ships $\left(\mathrm{X}_{4}\right)^{\prime}$, 'Long course distance $\left(\mathrm{X}_{5}\right)^{\prime}$, 'Deep channel $\left(\mathrm{X}_{6}\right)^{\prime}$, 'High ocean current velocity $\left(\mathrm{X}_{7}\right)^{\prime}$, 'Heavy traffic flow in the section $\left(\mathrm{X}_{8}\right)^{\prime}$, 'Unsafe behavior of personnel on LNG ships $\left(\mathrm{X}_{17}\right)^{\prime}$, and 'Poor organization $\left(\mathrm{X}_{18}\right)^{\prime}$. Reducing the occurrence probability of these events has less effect on improving the safety of LNG maritime transport and is more difficult to reduce [33]. We can summarize this as two intermediate events: 'Vessels and equipment risks $\left(\mathrm{I}_{2}\right)$ ' and 'Inherent risks of the route itself $\left(\mathrm{I}_{4}\right)$ '. In the case of limited resources, we can ignore these factors.

Moreover, medium-risk factors are events with high probability importance but low critical importance. Although such factors have a high risk of influencing the occurrence of top events, their own occurrence frequency is very low. Therefore, daily inspection and management should be strengthened for such factors, and potential symptoms should be found and handled in a timely manner.

# 4.5. Risk Diagnosis 

The cause of risk can be diagnosed by sorting the posterior probability of basic events, with the support of the ability of BN's binary risk diagnosis and risk prediction. The posterior probability of each basic event is calculated through NETICA, as shown in Table 7.

Table 7. Basic event posterior probability.


The posterior probability ranking results of basic events are as follows.

$$
\begin{aligned}
& P_{x 22}>P_{x 10}>P_{x 21}>P_{x 14}>P_{x 13}>P_{x 9}>P_{x 20}>P_{x 1}>P_{x 11}>P_{x 12}>P_{x 2} \\
& >P_{x 15}=P_{x 16}>P_{x 19}>P_{x 8}>P_{x 7}>P_{x 3}>P_{x 6}>P_{x 18}>P_{x 4}>P_{x 5}>P_{x 17}
\end{aligned}
$$

If there are risks in LNG maritime transport on the China-Australia route, the most likely reasons are 'The impact of epidemic $\left(\mathrm{X}_{22}\right)$ ', 'Piracy and terrorist attacks $\left(\mathrm{X}_{21}\right)$ ', 'Fewer LNG unloading ports $\left(\mathrm{X}_{14}\right)^{\prime}$, and 'Influence of weather and sea state $\left(\mathrm{I}_{5}\right)$ '. When accidents occur in maritime transport, priority can be given to checking whether these events occur, so as to save time and cost.

# 5. Suggestions and Discussion 

Based on the diagnosis of maritime transport risks on the China-Australia route, this paper puts forward suggestions and measures to reduce risks by reducing the probability of events with high posterior probability in Table 7.

As shown in Table 7, when accidents occur in LNG maritime transport, the posterior probability ranking of the top six basic events is significantly higher than others. To mitigate the risks associated with these events, the following suggestions and measures are proposed. From the perspective of risk control, these six events are divided into two categories for consideration: preventable and uncontrollable. Among them, the posterior probability ranking first and third are 'The impact of epidemic $\left(\mathrm{X}_{22}\right)$ ' and 'Piracy and terrorist attacks $\left(\mathrm{X}_{21}\right)^{\prime}$, which are considered as preventable events due to their low probability of failure. In response to the impact of the epidemic, shipping companies are predominantly affected, so it is crucial to establish a response mechanism for epidemic prevention and control for them; for piracy and terrorist attacks, the country should strengthen its domestic naval capacity building for defense. The rest are uncontrollable risks. The fourth-ranked event is 'Fewer LNG unloading ports $\left(\mathrm{X}_{14}\right)$ ', and as this situation cannot be improved in a short period of time, the establishment of alternative route mechanisms at ports can alleviate this impact to some extent. Finally, the second, fifth, and sixth-ranked events, namely 'Heavy fog $\left(\mathrm{X}_{10}\right)^{\prime}$, 'High frequency of strong winds $\left(\mathrm{X}_{13}\right)^{\prime}$, and 'High waves $\left(\mathrm{X}_{9}\right)^{\prime}$ can be summarized as the intermediate event 'Influence of weather and sea state $\left(\mathrm{I}_{5}\right)$ '. Given the unchangeable nature of these objective conditions, the only viable approach is to avoid LNG loading and unloading operations during adverse weather conditions.

The following are specific further discussions based on the above suggestions. For shipping enterprises, they should establish epidemic prevention and control response mechanisms. The outbreak of the global COVID-19 pandemic has increased the risk of shipping routes due to port suspensions in some relevant countries. To prevent similar situations from causing greater risks in the future, shipping enterprises should take targeted actions. For example, they should formulate comprehensive and feasible emergency plans for epidemic prevention and control under the leadership and guidance of the national government. This would help establish and improve relevant emergency response mechanisms to reduce the harm caused by public health emergencies at sea and prevent the spread of the epidemic [34]. Furthermore, strengthening the marine defense line for epidemic prevention and control is essential. Only by maintaining the normal order of maritime activities on the China-Australia route, and reducing the risk of the route, can we promote the recovery and normalization of shipping. Thus, it is crucial to take proactive measures to ensure the safety and security of shipping activities in the face of similar global accidents.

For the country, it is necessary to strengthen the capacity building of the domestic navy. The waters surrounding the South China Sea, Indonesia, and the Philippines are known for their high levels of pirate attacks and maritime terrorism, which create multiple uncertainties for shipping routes in the region. Therefore, it is crucial to enhance the construction of the domestic navy to improve route security. Specifically, China should focus on improving the navy's long-distance combat capability and defense capability, as well as enhancing the protection mechanism for LNG ships. Additionally, the ability to patrol dangerous waters and monitor the marine environment must be strengthened, and a well-established emergency plan system for piracy and terrorist attacks must be put in place. Increasing the frequency of naval convoys on the China-Australia route and cracking down on piracy are also important measures to consider.

For ports, a route substitution mechanism could be established to address the challenges posed by the restrictions of many islands, such as the Indonesian archipelago and the South Pacific islands, and the different passing capacities of key nodes, such as the Straits. Alternative routes should be actively sought to reduce the threat of emergencies to route safety. In the face of security threats, the route substitution mechanism could be implemented to reduce losses caused by port blockade and ensure the safety of the route.

Furthermore, loading and unloading operations should be avoided as far as possible during bad weather conditions. If environmental factors such as bad weather, strong winds, or waves affect the loading and unloading operation, it should be stopped immediately, and the corresponding connecting equipment should be disconnected to ensure the safety of the ship and the wharf.

# 6. Conclusions 

The main contribution of this paper is to build a fault tree analysis and Bayesian network model for the risk assessment of LNG maritime transport on the China-Australia routes. The proposed model combines the two methods to overcome the problem that conditional probabilities in the Bayesian network find difficult to determine. Specifically, due to the complexity of the maritime scenario, it is inappropriate for analysis to attribute accidents to a single cause or a few causes. This paper constructs accident causation networks from various perspectives of cargo, ships, route, and environment. The fault tree is established by investigating relevant literature and accident investigation reports, and expert opinions and fuzzy set are used to derive the prior probability, the fault tree is transformed into Bayesian network, and the conditional probability table in the Bayesian network is obtained through a relationship gate in fault tree analysis. From further analysis, the key influencing factors and sensitive factors can also be identified in this developed model.

In conclusion, the China-Australia route is an important maritime transport route for the trade activities between China and the Oceania region. However, the route is subject to multiple uncertainties, including piracy, terrorism, epidemic, port restrictions, and inclement weather conditions. These uncertainties pose significant risks to the safety of maritime transport activities and may result in economic losses and environmental damages. To reduce the risks and ensure the safety of maritime transport activities on this route, various measures should be taken, such as strengthening the construction of the domestic navy, establishing safety early warning systems for LNG storage and transportation, setting up appropriate meteorological monitoring departments, and avoiding LNG loading and unloading operations in bad weather conditions. By implementing these measures, we can promote the recovery and normalization of shipping on the China-Australia route and facilitate economic and trade cooperation between China and the Oceania region.

This paper analyzed the effect of risk factors from a systematic perspective based on real-world accidents. Although this paper takes LNG and the China-Australia route as an example, the proposed model can also be applied to other route to predict the probability of maritime accidents if the proposed route data have similar characteristics. Moreover, quantitative information assessed by experts due to limited data may be a biased representation of the exact real-world situation. Therefore, future work can model and analyze large amounts of data to provide additional and practical insights into enhancing marine safety.

Author Contributions: Conceptualization, X.H. and H.F.; methodology, H.F.; software, X.H.; validation, X.H., H.F. and Z.C.; formal analysis, H.F.; investigation, W.G.; resources, L.H.; data curation, X.H.; writing-original draft preparation, X.H.; writing-review and editing, H.F. and Z.C.; visualization, X.H.; supervision, W.G.; project administration, Z.C.; funding acquisition, Z.C. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by Dalian Maritime University grant number 2023JXA03.
Data Availability Statement: The data presented in this study are available on request from the corresponding author. The data are not publicly available due to privacy.
Conflicts of Interest: The authors declare no conflict of interest.

Appendix A. The Sources of RIFs Based on the Retrieved Results


Note: 'A' means this RIF is applied in the related reference.

# Appendix B. Questionnaire Results


Appendix C. Abbreviation and Full Name

