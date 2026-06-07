# Article 

## Risk Assessment of Port Congestion Risk during the COVID-19 Pandemic

Dongping Gui ${ }^{1}$, Haiyan Wang ${ }^{1,2}$ (D) and Meng Yu ${ }^{1, *}$


#### Abstract

check for updates Citation: Gui, D.; Wang, H.; Yu, M. Risk Assessment of Port Congestion Risk during the COVID-19 Pandemic. J. Mar. Sci. Eng. 2022, 10, 150. https://doi.org/10.3390/ jmse10020150

Academic Editor: Claudio Ferrari

Received: 6 December 2021
Accepted: 19 January 2022
Published: 24 January 2022


Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Transportation and Logistic Engineering, Wuhan University of Technology, Wuhan 430063, China; 249002@whut.edu.cn (D.G.); hywang777@whut.edu.cn (H.W.)
2 National Engineering Research Center for Water Transport Safety, Wuhan University of Technology, Wuhan 430063, China

* Correspondence: ymmona@whut.edu.cn


#### Abstract

With the COVID-19 outbreak hitting the world, the frequency and severity of port congestion caused by various factors are increasing, challenging the stability of international supply chains. Thus, it is necessary to conduct an in-depth study on congestion risks to reduce their adverse impacts on congestion. Although traditional criticality analysis techniques may be capable of ranking port congestion risk in common scenarios, new risk analysis methods are urgently required to tackle uncertainty along with the COVID-19 pandemic. This paper develops a methodology designed for the identification and prioritization of port congestion risk during the pandemic. First, a novel congestion risk assessment model is established by extending the risk prioritization index (RPI) suggested by failure mode and effects analysis (FMEA). Next, the combination of fuzzy Bayesian reasoning, AHP and the variation coefficient method is incorporated into the model in a complementary way to facilitate the treatment of uncertainty and quantitative analysis of the congestion under the different influence of risk factors in ports. Finally, the mode introduces a set of risk utility values for calculating the RPI for prioritization. A real case study and a sensitivity analysis were carried out to illustrate and validate the proposed model. The results proved that the applied method is feasible and functional. In the illustrative example, the top three risk factors are "Interruption of railways/barges services", "Skilled labor shortage" and "Shortage of truck-drivers/drayage truck". The findings obtained from this paper could provide useful insights for risk prevention and mitigation.


Keywords: the COVID-19 pandemic; port congestion risk; risk parameter structure-based FMEA; fuzzy belief rule-based Bayesian network (FBRB-BN); AHP; the variation coefficient method

## 1. Introduction

Accounting for approximately $90 \%$ of goods transportation between countries [1,2], maritime transportation is regarded as an important means to keep global trade flowing and ensure the stability of supply chains. Since ports are an accelerator of high-quality development, the business continuity of ports is vital for the modern world economy and trade. However, the COVID-19 pandemic hit the world and triggered an unprecedented health and economic crisis, upending the landscape for maritime transport and trade [3]. Against this background, the frequency and severity of port congestion, stimulated by a variety of factors are rising, severely challenging the continuity of shipping services. Thus, all the stakeholders in the maritime industry must step up to the congestion challenge.

Port congestion not only leads to longer waiting times and lower service levels before berthing, but also brings long-term effects such as reduced income, increased risk of debt and bankruptcy and declined competitiveness. Therefore, it is an important problem both from the perspective of efficiency and economy [4]. Implementing necessary management to mitigate even avoid congestion has become more widely known in recent years. Normally, strategies proposed by researchers for port congestion management can be divided into reactive strategies and proactive strategies. The former are applied after congestion

emerged, and typical examples of these are evolution analysis of port congestion [5,6], and congestion governance modes [4,7] or measures [8,9]. The latter refers to the identification and assessment of congestion or congestion risk before it occurs. Many techniques have been developed and applied to forecast and evaluate port congestion, such as simulation technology [10], algorithms based on AIS Data [11,12], and Markov chain analysis [13]. Moreover, the use of risk assessment as the solution to decision-making of operation management and port investment has been recognized by researchers with various backgrounds and verified effectively by real examples. These studies could be classified into networkbased cascading congestion risk models [14] and traditional risk models [15,16] where risk was defined as the combination of probability and impact. Possible limitations of such traditional risk models would be that, for one thing, they failed to address the uncertainty existing in common responses from interviewees; for another, it described risk based on only two types of risk parameters. This may neglect or underestimate the likelihood of a disruption of the type and scale of the COVID-19 outbreak, thus providing insufficient information for decision making. Frequent congestion during the pandemic implied that the maritime transport of the future needs to be calibrated according to risk exposure and risk management, anticipating further enhancement. Last but not least, there are some studies [17,18] focused on robustness and recovery planning for ports, in which both the proactive and reactive disruption management for ports were taken into account.

Undoubtably, an adequate risk management procedure is of importance to prevent and reduce congestion risk as well as strengthen resilience-building of maritime transport. On the one hand, the identification and analysis of relevant risk exposures, vulnerabilities and potential losses are essential for risk prevention/mitigation [19]. On the other hand, the disruption caused by the COVID-19 pandemic will exert a lasting impact on shipping and trade. Additionally, port congestion will change with time and external conditions, resulting in fuzzy and incomplete data for estimating and managing risks. This requires a flexible and effective quantitative risk analysis model, which can not only provide insight into the congestion risk status of ports with incomplete evidence, but also update the existing information when new data are available [20]. This paper aims to answer the following three research questions:
RQ1: What are the risk factors contributing to port congestion during the pandemic?
RQ2: What risk parameters should be considered in port congestion risk assessment?
RQ3: How to realize flexible and accurate congestion risk assessment?
The rest of this paper is organized as follows: Section 2 reviews the research work related to port congestion and the application of Fuzzy Rule-Based Bayesian Network (FRBN) in risk assessment. Section 3 is the methodology for establishing a generic port congestion risk assessment framework, including congestion risk identification, a novel congestion risk assessment model and model validation. A real case of the congestion risk of the Los Angeles-Long Beach ports and sensibility analysis are used to demonstrate and validate the methodology in Section 4. Finally, Section 5 concludes the work.

# 2. Literature Review 

In this section, the prior research relating to port congestion management is first reviewed, followed by the introduction of the quantitative analysis of port congestion concerned, the application of Fuzzy Rule-Based Bayesian Networks (FRBN), and finally the summary of research gaps that remain to be addressed appropriately. It lays emphasis on the lessons learnt and the inadequacies in the literature, thereby paving the way forward in our study.

### 2.1. Previous Research on Port Congestion Management

Port congestion is a phenomenon which is relevant to delays, queuing, extra voyage and dwell time of ships and cargo at the port [21]. Most scholars [6,13,22] deemed that congestion occurs when maritime participants clash with others in the utilization of port resources. In other words, port congestion is significantly associated with the entire

maritime supply chain (MSC) [23]. Considering the impact of congestion on time and costs, such as excessive waiting times and high demurrage or additional congestion surcharges, port congestion management has received increased attention in recent years.

There is some research aiming to reduce local congestion at ports. For example, Zhen [24] studied the yard template planning problem in the context of yard truck interruptions. In their study, a mixed-integer programming model and a Squeaky Wheel Optimization based meta-heuristic were developed for minimizing the total expected travel time of moving containers around the yard. Concentrating on berth congestion reduction, Iris et al. [25] proposed novel Generalized Set Partitioning (GSPP) formulations for solving the integrated Berth Allocation and quay Crane Assignment Problem (BACAP). Iris et al. [26] formulated and solved a mathematical model for the flexible containership loading problem for seaport container terminals. Instead, Saeed, Song and Andersen [4] and Xu, Li, Liu and Yang [9] discussed the measures for mitigating port congestion with considering other stakeholders' engagement. Compared to after-the-fact management, the identification, assessment and forecasting of congestion are preferred by academic research. For instance, Oyatoye et al. [27] utilized queuing theory to detect that congestion in the Nigeria port is majorly caused by the operational inefficiency of the port managers and operators coupled with long years of infrastructural developmental neglect. Stergiopoulos, Valvis, Mitrodimas, Lekkas and Gritzalis [14] developed a risk-based interdependency analysis method that can identify the large-scale traffic congestion between interrelated ports and routes in the shipping network. Yeo, Roe and Soak [10] used the AWE-SIM simulation program to forecast the potential of congestion at the Busan port owing to the increased cargo volume. By applying Markov Analysis, Pruyn, Kana and Groeneveld [13] developed a probabilistic prediction model for days of waiting time due to port congestion, which could provide a decision-making basis for shippers and carriers to choose cargo loading and unloading ports. Based on AIS data, Li [12] and AbuAlhaol, Falcon, Abielmona, Petriu and Ieee [11] developed different algorithms for evaluating congestion and predicting the behaviors of ports in future months, respectively. According to results from the above research, factors caused congestion could be listed in general headings as follows: socio-economic factors, adjustments in the market strategies of maritime participants, low productivity in port, adverse weather and accidents. The existence of such factors increases the uncertainty of port operation. Additionally, such uncertainty has been intensified by the COVID-19 pandemic [28].

The sudden outbreak of COVID-19 pandemic has rapidly affected all elements of the maritime supply chain roughly at the same time, and unprecedented chaos has consequently been brought about in global ports and the shipping industry. Millefiori et al. [29] proposed a maritime mobility index for analyzing the short-term effects that the COVID-19 pandemic and its containment measures had on the shipping industry. The result from their research shows that an unprecedented drop in maritime mobility across all categories of commercial shipping in the early days of the COVID-19. According to the evidence from 14 ports in China, Xu et al. [30] detected that the traditional peak season for shipping of import throughput is still maintained, while export throughput no longer has a clear difference between low and peak seasons. After the temporal surges driven by the large increase in trade of medical pharmaceuticals and mode substitution from air to maritime [31], the global shipping industry is confronted with another demand peak brought about by the economic recovery. For the shake of strengthening the supply chain, some North American countries have witnessed a clear trend toward restocking inventories at distribution centers and stores since September 2020 despite the pandemic still accelerating there [32]. During the epidemic, the imbalance of port productivity and shipping demand, as well as the instability of shipping routes, were further highlighted, and consequently the trend of goods and ships arriving at the port in the same time becomes more and more obvious. However, the operational capacity of most ports is lower than their theoretical capacity [6]. The impact of the pandemic on the economy, society, and port industry far exceeds that of "SARS" in 2003. Chen et al. [18] emphasized the importance of the robustness and sustainability of the

port logistics system. By formula derivation and analysis, they obtain an optimized and robust system which can minimize the economic loss caused by the outbreak. The duration and severity of the epidemic in the future is still a matter of uncertainty, which outlines the importance of effectively managing the risk of port congestion.

# 2.2. Quantitative Analysis of Port Congestion Risk 

Port congestion has been regarded as one of the most prominent risks in the shipping industry [15]; therefore, some research pays more attention to the assessment of risk factors which have a noteworthy impact on the efficiency of port operation.

Park et al. [33] discussed how the operations of an excursion ship, i.e., an increase in harbor traffic volume, affected the Busan North Port's marine traffic status by applying the marine traffic assessment indexes and IWRAP MkIImodel. Based on the relative importance, Bolat, Kayisoglu, Gunes, Kızılay and Ozsogut [16] ranked a list of factors contributing to port congestion by AHP. Potgieter, Goedhals-Gerber and Havenga [15] proposed that the risk severity of port congestion should be measured using two measurements, namely risk frequency (L), and risk impact (C). In their study, the risk impact is defined as the number of hours delayed (scheduling impact) and forms a risk matrix with the risk frequency to evaluate the risk level of weather- and system-related port congestion at Cape Town container terminal. The combination of $L$ and $C$ has been proved a simple and effective way to represent risk, which could be found in other aspects of port risk studies, such as safety and security analysis [34], operational risk [20] and disruption risk [1]. However, risk is a complex and interdisciplinary concept involving many parameters such as probability, consequence, uncertainty and scenario [35]. Only considering the parameters $L$ and $C$ will lead to the loss of useful information in risk analysis. Moreover, port congestion will not only lead to more and more queues, but also more or less hidden congestion costs even decline in competitiveness [5]. Putting all aspects under the umbrella of 'consequence' might add the difficulty of risk assessment and encourage the behavior of careless assessment [36,37].

With the deepening of risk management in the shipping industry, visibility has become another issue of maritime transportation. Good visibility plays a vital role in the operational efficiency, productivity and effective planning of the transportation system [38]. Improving visibility is the inevitable trend of future development. For example, Maersk and IBM jointly developed a blockchain project, Trade Lens, which can connect all the partners in a maritime supply chain, thereby bring end-to-end supply chain visibility for shippers and consignee. AIS systems, the Internet of things (IOT) and blockchain technology promote information sharing among maritime supply chain participants, making it possible to monitor the status of ship motion and cargo shipment and facilitate the evacuation and delivery of cargo out of the port. This is of great significance for improving the transparency and stability of the maritime transportation system, as well as preventing and alleviating port congestion. However, according to the literature collected by the author, visibility has not been considered in risk assessment of port congestion yet.

### 2.3. Fuzzy Rule-Based Bayesian Networks Used in Maritime Risk Assessment

Owing to its transparency and easiness, failure modes and effect analysis (FMEA) has been widely applied in risk analysis. However, it still shows limitation in addressing cognitive uncertainty in risk assessment. Furthermore, it may occur that different combinations of three risk parameters (i.e., likelihood of occurrence L, the severity of consequence C, and the probability of the failure being undetected P ) share the same value of risk priority number (RPN). As a coupled method, Fuzzy Rule-Based Bayesian Networks were usually introduced into FMEA for their unique superiorities in fully expressing experts' subjective judgement and modeling the non-linear relationship between different variables.

Yang et al. [39] innovatively developed a fuzzy rule-based Bayesian Reasoning (FuRBaR) approach for supporting safety-based decision making during tandem offloading operation in port. The results from their study indicated that FuRBaR can effectively manage the uncertainty stemming from human knowledge in risk assessment. However,

the application of FuRBaR was affected by the rationality of belief rule base (BRB). Thus, different improvement mechanisms were put forward by some scholars. For example, Alyami, Lee, Yang, Riahi, Bonsall and Wang [34] proposed a Fuzzy Rule-Based Bayesian Network (FRBN) for evaluating the criticality of hazard events (HEs) in a container terminal, where a more rigorous and explicit proportion method was used to construct a reasonable structure of BRB. Wan et al. [40] suggested that considering the relative importance of the risk attributes when developing a rule representation will be helpful to improve the robustness of BRB in FRBN. In their research, a fuzzy belief rule-based Bayesian network (FBRB-BN) approach was proposed, where AHP was employed to determine all the degree of beliefs (DoBs) of rules rationally in a BRB. However, AHP has a certain subjectivity which inevitably generates weight deviation, consequently showing drawbacks in scientifically reflecting the real state of the risk. One realistic way to solve this problem is the comprehensive weight method where AHP and the variation coefficient method are integrated in a complementary manner [41].

# 2.4. Research Gap 

Though the above studies have provided useful insights into the quantitative analysis of port congestion, as well as in maritime risk assessment, there are still some research gaps which need to be filled:
(1) From the above literature review, there is no research on port congestion risk assessment under the COVID-19 pandemic despite it being very important.
(2) For one thing, traditional risk assessment methods employed in previous studies; for example, the risk matrix cannot deal with the epistemic uncertainty caused by inaccurate congestion risk data. For another, the application of Fuzzy Rule-Based Bayesian Networks (FRBN) for congestion risk assessment is still in its infancy.
(3) Problems of congestion in ports are multi-dimensional or rather complex [21]; however, previous quantitative analysis studies on port congestion risk only concentrated on the likelihood or the severity of consequences, leaving the other features of risk not being fully explored.
Given the existing gaps as well as advantages of prior studies, this paper takes the port congestion risk under the COVID-19 pandemic as the research object and proposes a novel congestion risk assessment model. This is achieved by (1) determining the research boundary of port congestion risk, thereby identifying all congestion risk factors assisted by congestion cases and available information in the literature review; (2) constructing a risk parameter structure for measuring the risk status of port congestion risk based on FMEA; and (3) using the combination of AHP and the variation coefficient method to assign subjective belief degrees to the subsequent parts of fuzzy rules in FRBN.

## 3. Methodology for Modeling Port Congestion Risk during the COVID-19 Pandemic

Generally, the choice of methods for risk assessment should be driven by the nature of the research problem, such as data availability (exact or incomplete data), the degree of interrelationship complexity, etc. [40]. Given no detailed list of/exact data pertaining to port congestion risk during the pandemic exists, congestion risk factors need to be identified and most of the risk attributes (e.g., severity and likelihood) amount have to be estimated. However, highly subjective judgments could be vague and uncertain [36]. In addition, port congestion will change with time and external conditions [12], especially considering the prevalence of a highly transmissible strain. Thus, the results obtained from risk assessment should be real-time and be upgraded with new information.

In view of these, we start by identifying congestion risk factors using the definition of port congestion risk, literature review and typical congestion cases. Then, a novel congestion risk assessment model is developed, in which the RPI suggested by FMEA is extended first, following the utilization of a fuzzy belief rule-based Bayesian network (FBRB-BN) for tackling vagueness in expert judgment and modeling the relationship between different variables and achieving risk inference. Inspired by [41-43], AHP and the

variation coefficient method are employed to further reduce the uncertainty from subjective judgements when establishing FBRB. Additionally, the RPI values for risk ranking could be computed from utility values and the marginal probability obtained from FBRB-BN. The detailed steps of the proposed methodology are depicted as Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. The main steps for port congestion risk assessment.

# 3.1. Identify Risk Factors of Port Congestion under the COVID-19 Pandemic 

To acquire more accurate and inclusive risk identification results, the concept of congestion risk should be defined first. Normally, risk is regarded as the combination of hazard, consequence and uncertainty in most studies related to port or maritime risk. In addition, many ports around the world have been suffering from congestion caused by external or internal disruption after the COVID-19 outbreak hit the world; see Table 1. Inspired by the work of [44], this paper defines the port congestion risk as potential risk factors that may lead to congestion or worsen the current situation of port congestion during the pandemic.

Table 1. Examples and their reasons for port congestion.


From Table 1, the risk factors of port congestion can be divided into external factors (EFs) and internal factors (IFs) here. External factors refer to the risk sources of congestion from members of the maritime supply chain or the external environment of port operation. Additionally, internal factors originate from the bottlenecks at various sections of the port, which are mainly associated with manpower, equipment, facilities, procedure, etc. Based on the above discussion and the available information presented in Section 2, a list of congestion risks could be identified-see Table 2.

Table 2. Risk Factors of port congestion during the COVID-19 pandemic.


# 3.1.1. External Factors Contributing to Port Congestion 

External factors contributing to port congestion, firstly, are the continuous growth of freight volumes associated with the transformation of consumption patterns and the economic recovery in post-pandemic. A continuing surge of freight volume results in the number of ships calling at ports exceeding the port's capacity level permits, where congestion arises [4]. Secondly, the pandemic disrupts the normal shipping schedule; vessels consequently arrive in port at the same time, which leads to further congestion and delays [45]. Thirdly, the ratio of lager vessels in the deployed container vessels continues to increase despite the pandemic [32]. The large-scale ships, especially Ultra Large Container Vessels (ULCVs), reduce the frequency of ships calling at the port while container volume surges significantly accompanied by this decline in port calls. Thus, the peak times of berths, yards and gates in the port are increasing, which further reduces the port's revenue and accentuates the degree of congestion.

Another source of congestion is directional imbalance of container trades due to the COVID-19 pandemic, especially in the Transpacific and Asia-Europe-Asia trade lanes [28]. Containers are not available in export-oriented areas; consequently, goods have been stockpiled at ports, terminals, and elsewhere for several weeks, while in import-oriented areas, an overrun of empty containers is eating up valuable yard space. Port congestion is also relevant to the inefficiency of the inland transportation system. Capacity "tightness" or congestion in railways and highways from the port to the inland, or the temporary suspension of rail and barge services, could slow down the evacuation and delivery of cargo out of the port [21]. Moreover, shortage of drayage truck or truck-drivers or chassis may further worsen the fluent flow of cargo through the port [5,46]. In addition, the reluctance of consignees to collect cargoes may occur because of additional fees (e.g., Container Excess Dwell Fees) and the complex cross-border crossing [32]. Alongside these

factors, network security (e.g., hacker intrusion or network fraud) seems an additional factor of congestion. Finally, port congestion can also happen due to external factors more or less beyond the control of the actors, namely industrial action or strikes, bad weather, and accidents [4]. On the one hand, industrial action or strikes may disrupt the normal operation of port business and shut down the port [1]. On the other hand, adverse weather (e.g., typhoon and thick fog) or traffic accidents may temporarily close the port, resulting in vessels lining up outside.

# 3.1.2. Internal Factors of Port Congestion 

During the pandemic, the internal bottlenecks at various sections of the port used for berthing, cargo unloading/loading, storage, and transfer [6], were underscored. For one thing, fewer workers could be on shift at a given time due to the social distancing mandates or continuous infection, which created a bottleneck at the docks or warehouses, resulting in a direct decline in port productivity. For another, insufficient or poorly maintained infrastructure/port handling equipment capacity contributed to delays in the loading/unloading of containers [15]. Limited yard or stockpiling space also impedes the process of cargoes discharging from ships. In addition, poor management on container stacks means unexpected shifting and sorting of containers, which may cause a certain degree of delay. For instance, when truckers come to pick up import containers as the container yard congestion builds, there could be multiple movements/sorts within the terminal before the containers are received [46].

In addition, with the increasing health risk of international goods, ports had to implement more stricter declaration, quarantine and disinfection measures for goods and ships arriving at or passing by the ports in high-risk regions. Cumbersome licensing or documentation procedures prolong the time each vessel spends at the port and the time cargo takes to move through the port, thereby aggravating congestion intangibly [16]. Finally, congestion can happen at the gate systems where cargo enters or leaves the port in the case of truck use. Inconsistent hours across terminals may take up the majority of the truck fleet, which adds to congestion [46].

### 3.2. Establishment of an FBRB for Modeling Port Congestion Risk

### 3.2.1. Risk Parameter Set Based on FMEA

Given the difficulty for experts of giving reliable judgements when the target object is excessively general or complicated [35], the extensions of the C (the severity of consequence) and $P$ (the probability of the failure being undetected) parameters in FMEA are considered in this paper when constructing the FBRB for port congestion risk assessment.

Besides time loss and thus a higher generalized cost, congestion implies increasing difficulty in the port's operation management and the decline in the port's competitive power. On the one hand, when congestion occurs, the port authority has to maximize the organization of terminal operation machinery and personnel for implementing an emergency response plan, which adds evitable total cost and operational difficulty. On the other hand, port congestion may exert a long-term impact on market power, thereby resulting in the loss of goods or vessel calls to the port [47]. Therefore, this study subdivided consequences into time impact (CT), additional cost (CC) and competitive impact (CI). Time impact usually refers to the amount of additional time or delays experienced by ocean carriers or cargo owners [15], i.e., the average waiting time of ships or the average dwell time of goods in port. Additional costs could be understood as costs associated with port operation and management when congestion occurs, for instance, fees spent in extra manpower or equipment to handle the same amount of goods in a more intensive time frame. According to Yeo, Roe and Soak [10], congestion on the port lanes can severely affect a user's loyalty to the port. Thus, competitive impact here expresses the damages of congestion risks on the port image, which could be further observed through complaints from the port's clients, the loss of cargo or the increasing number of vessel calls canceled. Normally, the P parameter, also called the level of detection (D) in this paper, refers to the

ability of managers to detect the existence of one specific risk factor. A more visible risk factor is a less dangerous one.

By doing this, a two-level parameter structure for experts to evaluate each congestion risk factor is developed, in which likelihood(L), D and C are on the first-level, and CT, CC, CI are on the second-level.

# 3.2.2. Definition of Input and Output Variables via Fuzzy Linguistic Terms 

Utilizing the fuzzy belief rule base (FBRB) in [39], we constructed IF-THEN rules where IF represents five risk parameters(L,D,CT,CC,CI) in Section 3.2.1 and THEN signifies the risk status $(R)$.

Considering subjective judgements are somewhat ambiguous and inexact in many cases, it is better to use linguistic terms rather than numerical values when collecting experts' estimates of risk [20]. Following recent studies related to maritime risk [19,40], this paper defined three linguistic variables for five risk parameters (L, D, CT, CC and CI), respectively-see Table 3. Similarly, the risk status (R) could be described by three grades, namely 'Low', 'Medium', and 'High'.

Table 3. Corresponding linguistic variables of parameters and their meaning.


### 3.2.3. Degree of Belief of Risk Status Based on AHP and the Variation Coefficient Method

As a multi-input and single-output structure, it is expected that there are $243(3 \times 3$ $\times 3 \times 3 \times 3$ ) rules in FBRB. Take one of rules Rule $_{t=i+j+k+l+m}$ as an example, the IF-THEN rule can be generally denoted as Equation (1).

$$
\begin{gathered}
\text { Rule }_{t=i+j+k+l+m}: \\
\text { IF } L_{i} \text { and } D_{j} \text { and } C T_{k} \text { and } C C_{l} \text { and } C I_{m} \\
\text { THEN }\left\{\left(\beta_{1}^{t}, R_{1}^{t}\right),\left(\beta_{2}^{t}, R_{2}^{t}\right),\left(\beta_{3}^{t}, R_{3}^{t}\right)\right\} \times\left(\sum_{n=1}^{3} \beta_{n}^{t}=1\right)
\end{gathered}
$$

where $L_{i}, D_{j}, C T_{k}, C C_{l}, C I_{m}(i, j, k, l, m=1,2,3)$ represented experts' subjective judgements of five risk parameters, respectively, and $\beta_{n}^{t}$ denoted the Degree of Belief (DoB) to which $R_{n}^{t}$ is believed to occur.

As discussed earlier, $\beta_{n}^{t}$ can be calculated based on distributing contribution in terms of weights of parameters in the IF part. That being said, the relative importance of each level parameter needs to be determined. Here, we used the linear combination (i.e., the comprehensive weight) of subjective and objective weight as the weight of the parameter. An expert investigation based on AHP was conducted to acquire estimations of the relative importance of the first-level parameter ( $\mathrm{L}, \mathrm{D}, \mathrm{C}$ ) and the second-level parameter (CT, $\mathrm{CC}, \mathrm{CI})$. Five domain experts (detailed experts' information refers to Section 4.1) were

interviewed who were dedicated to ensuring the safe and efficient operations of the port logistics system. The outputs are as shown in Equations (2) and (3) and were checked by the consistency ratio $(\mathrm{CR} 1=0.073<0.1, \mathrm{CR} 2=0.093<0.1)$,

$$
\begin{aligned}
& u_{1}=(0.082,0.670,0.248) \\
& u_{2}=(0.649,0.123,0.229)
\end{aligned}
$$

By calculating the weight of the information contained in the parameter directly, the coefficient of variation $\left(V_{i}\right)$ could avoid the interference of subjectivity, thus obtaining the objective weight [41]. Take the first-level parameter as an example, the calculation formula of coefficient of variation was as follows:

$$
V_{i}=\frac{\sigma_{i}}{\bar{x}_{i}}
$$

where $\sigma_{i}$ represented the standard deviation of parameter $i, \bar{x}_{i}$ denoted the average of parameter $i$.

The weight of variation coefficient formula of each index was as follows:

$$
v_{1}=\frac{V_{i}}{\sum_{i=1}^{n} V_{i}}
$$

Based on the data of experts, as well as the Equation (5), the objective weights for each parameter of the first level (with three decimal places reserved) were as follows:

$$
v_{1}=(0.159,0.422,0.419)
$$

The comprehensive weight model calculating adopted the following formula was as follows:

$$
\omega_{i}=\theta \times u_{i}+(1-\theta) \times v_{i}
$$

where $\omega_{i}$ denoted the comprehensive weight, $\theta$ was the proportion of subjective weight in the comprehensive weight.

To achieve the best combination of the two kinds of weights, one realistic way is to establish an objective function where the sum of the squares of deviations is minimized, denoted as $z[43]$ :

$$
\min z=\sum_{i=1}^{n}\left[\left(w_{i}-u_{i}\right)^{2}+\left(w_{i}-v_{i}\right)^{2}\right]
$$

The first derivative was found with respect to $\theta$ and set to 0 , thereby obtaining the optimal value of $\theta$ of 0.5 . Therefore, Equation (6) could further be represented as:

$$
\omega_{i}=0.5 \times u_{i}+0.5 \times v_{i}
$$

Then, synthesizing the data, the comprehensive weights of the parameters at the first level were obtained (with three decimal places reserved):

$$
w_{1}=(0.121,0.546,0.333)
$$

Similarly, the objective and comprehensive weights of the second-level parameter could be obtained which were as follows:

$$
\begin{aligned}
& v_{2}=(0.435,0.203,0.362) \\
& w_{2}=(0.542,0.163,0.295)
\end{aligned}
$$

Finally, the final comprehensive weights of risk parameters at each level were shown in Table 4.

Table 4. Weight of each risk parameter in the FBRB.


With the above information, we could determine $\beta_{n}^{l}(n=1,2,3)$ which are the sum of the final comprehensive weights of all risk parameters with the "same" grade [34,40]. For instance, the Rule $_{3=1 * 1 * 1 * 1 * 3}$ can be described as follows:

Rule $_{3=1 * 1 * 1 * 1 * 3}$ :

$$
\begin{aligned}
& \text { IF } L \text { is Unlikely, } D \text { is Good, CT is Low, CC is Low, CI is Critical } \\
& \left.\left.T H E N \begin{array}{l}
\left(\begin{array}{l}
R=\text { Low, } \beta_{R 1}^{3}=w_{L}+w_{D}+w_{C T}+w_{C C}=0.901
\end{array}\right), \\
\left(\begin{array}{l}
R=\text { Medium, } \beta_{R 2}^{3}=0
\end{array}\right), \\
\left(\begin{array}{l}
R=\text { High, } \beta_{R 3}^{3}=w_{C I}=0.099
\end{array}\right)
\end{array}\right\}
\end{aligned}
$$

In a similar way, the DoBs of the rest rules could be obtained. Therefore, the FBRB for modeling congestion risk was established and is partially presented in Table 5.

Table 5. The partial FBRB for congestion risk assessment.


# 3.3. Risk Ranking Based on the BN Technique and Utility Functions 

Since the outputs still were distributed in FBRB, a BN technique with strong reasoning ability was hence employed to aggregate all rules and simplify calculation. First, the Directed Acyclic Graph (DAG) in BN was used to convert the fuzzy rule into a Bayesian network diagram (see Figure 2), in which the risk status (R) was termed the child node NR while five parameters were defined as parent nodes, NL, ND, NCT, NCC, NCI, respectively. First, a fuzzy belief rule in FBRB was transformed and represented in the form of conditional probabilities, denoted as [40]:

$$
p\left(R h \mid L_{i}, D_{j}, C T_{k}, C C_{l}, C I_{m}\right)\left(h, i, j, k, l, m=1,2,3\right)
$$

where " $\mid$ " shows conditional probability. Specifically, Rule 3 can be further displayed as follows:

$$
p\left(R h \mid L_{1}, D_{1}, C T_{1}, C C_{1}, C I_{3}\right)=(0.901,0,0.099)
$$

Then, the rule-based risk inference can be simplified as the calculation of the marginal probability of the node $\mathrm{N}_{\mathrm{R}}$, denoted as:

$$
p(R h)=\sum_{i=1}^{3} \sum_{j=1}^{3} \sum_{k=1}^{3} \sum_{l=1}^{3} \sum_{m=1}^{3} p\left(R h \mid L_{i}, D_{j}, C T_{k}, C C_{l}, C I_{m}\right) p\left(L_{i}\right) p\left(D_{j}\right) p\left(C T_{k}\right) p\left(C C_{l}\right) p\left(C I_{m}\right)
$$

in which $p\left(L_{i}\right), p\left(D_{j}\right), p\left(C T_{k}\right), p\left(C C_{l}\right)$, and $p\left(C C_{m}\right)$ were the priori probabilities of five parent nodes, respectively.

Finally, to rank congestion risk, Risk Priority index (RPI) could be developed by Equation (17):

$$
R P I=\sum_{h=1}^{3} p(R h) \times U V_{R h}
$$

where $U V_{R h}$ was the risk utility value. This study employed $U V_{R 1}=1\left(1^{5}\right) ; U V_{R 2}=32\left(2^{5}\right)$; $U V_{R 3}=243\left(3^{5}\right)[40]$.
![img-1.jpeg](img-1.jpeg)

Figure 2. The Bayesian network structure for port congestion risk.

# 3.4. Model Validation 

For the sake of validating and demonstrating the application of the proposed method, a real case study and sensitivity analysis is carried out in this paper. The former provided a pragmatic basis for examining the feasibility of the model, while the latter proved the theoretical robustness of the constructed model. The following three axioms shall be satisfied if the proposed model is reasonable and robust [19,34,39,40,48]:

Axiom 1. The slight increase/decrease in the priori probability of each parent node shall inevitably lead to the raise/drop in the posteriori probability of the child node and in RPI value.

Axiom 2. The impact magnitudes of the subjective probability changes on RPI shall be in accordance with their weight, i.e., a higher weight indicating more obvious changes.

Axiom 3. The influence created on the RPI through the variation of the probabilities of evidence set shall be greater than that of any of its subsets.

## 4. Result and Discussion

### 4.1. Illustrative Case Study

To illustrate how the methodology can be implemented in actual risk situations, this paper carried out a real case study on Los Angeles-Long Beach ports (LA-LB ports) in the USA. With no less than 12 marine terminals, relatively completed infrastructural facilities as well as a convenient inland connection, the LA-LB ports are the busiest container trade gateways, which handle almost all the commodities from Asia to the United States, accounting for more than one third of the container import volume of the country. However, such concentration also makes the freight system in the USA more vulnerable to the sort of congestion and delays the ports experienced in the COVID-19 pandemic. According to the statistical data from the Southern California Shipping Exchange, as of 18 October 2021, the total number of ships waiting to enter the two ports to unload was 100, a record high. The congestion in the LA-LB ports has seriously aggregated the operation limits of the global shipping industry and consequently hindered the efficiency of the overall supply chain. Therefore, the LA-LB ports are regarded as a representative case by the author.

To acquire specific input information of risk factors listed in Table 2, we designed a questionnaire and consulted five relevant experts who have more than ten years of background experience in maritime research. In the questionnaire, experts were asked to use the subjective probability distribution of the linguistic variables of each parameter because their evaluation was not backed by objective data. Next, the arithmetic mean of these primary evaluation values were input into the Bayesian network structure (Figure 2) to calculate the necessary marginal probability through Equations (14) and (16) for risk ranking. Additionally, Netica software was utilized to facilitate BN computation due to its

ease of use. An example of EF_6 (“Interruption of railways/barges services”) is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Risk status of EF_6 calculated by Netica software.
According to Figure 3, it can be easily observed that any risk input with reference to the L, D, CT, CC and CI parameters can trigger a change in the output result, which facilitates achievement of an instant congestion risk assessment. Moreover, the expression of the risk status of EF_6 can be ((Low, 0.165), (Medium, 0.361), (High, 0.474)). Therefore, the RPI of "Interruption of railways/barges services" is calculated by Equation (17):

$$
R P I_{E F _6}=\sum_{h=1}^{3} p(R h) \times U V_{R h}=0.165 \times 1+0.361 \times 32+0.474 \times 243=126.899
$$

The RPI of the rest of the congestion risk factors can be calculated in a similar way. Based on the computed RPI values, we can rank all congestion risk factors, as shown in Table 6.

Table 6. Prioritization of congestion risk factors in the LA-LB ports.


Note: Gray: internal congestion risk factors; no color: external congestion risk factors.

# 4.2. Sensitivity Analysis 

To examine the robustness of the proposed model, we employed the consecutive method and cumulative method used by Nguyen and Wang [19] to conduct a sensitivity analysis, respectively. First, we reassigned absolute DoB in the worst grade (i.e., frequent occurrence, poor detection, time delay, highest additional cost and critical impact in port competition) to $100 \%$ in the input nodes and reset after each time. Next, we raised the DoB

of the worst grade to $100 \%$ without such a reset. All records regarding changes in DoB of "High" grade in risk status as well as in RPI value are shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Sensitivity analysis of different input nodes.
Here, we still take EF_6 as an example. From Figure 4, it can be clearly observed that the posterior probability of " $R=$ High" increased from $47.4 \%$ to $75.8 \%$ and the PRI rose from 126.899 to 189.18 after the DoB of "Poor" in node D was assigned to $100 \%$. Moreover, the impact magnitudes of the subjective probability changes in node D on the RPI (from 126.899 to 189.18) is larger than in other nodes (e.g., from 126.899 to 141.62). Therefore, it could be concluded that the proposed model satisfies Axiom 1 and Axiom 2. In cumulative adjustments, both the continuous growth in the DoB of "High" state and in RPI indicate that the Axiom 3 is satisfied.

# 4.3. Discussion 

This paper aims to fill the research gaps in the quantitative assessment and prioritization of port congestion risk factors during the COVID-19 pandemic. Therefore, there are three aspects of this problem which are addressed.

First, 19 risk factors causing port congestion were identified. Second, to precisely measure those risk factors and meet different decision-making requirements, we investigated more risk parameters according to the features of port congestion during the pandemic. Third, combining a fuzzy belief rule-based Bayesian network (FBRB-BN) with AHP and the variation coefficient method provided a powerful tool to incorporate subjective judgments to evaluate and prioritize congestion risk factors under uncertainty from incomplete risk records. None of the 19 identified port congestion risks had the same ranking value (see Table 6), and thus the applied method is considered feasible and functional. Meanwhile, the proposed method made it possible to consider other congestion risk features instead of just relying on likelihood and the severity of consequence. While results from sensitivity analysis validated the robustness of the developed model, they also illustrated the effectiveness of the five selected risk parameters in evaluating port congestion risk, i.e., any changes in the estimations of each risk parameter directly led to the relative variation in RPI. As a result, the port authority or government can easily obtain real-time congestion risk evaluation and dynamic risk-based decision support after inputting or updating information, thereby allocating limited resources to the most impactful risks.

The results of this study also contribute to managerial practices in the realms of LA-LB ports. According to Table 6, the most significant factor for port congestion in the investigated ports was "Interruption of railways/barges services", followed by "Skilled

labor shortage", "Shortage of truck-drivers/drayage truck", "Inefficient and insufficient port infrastructure/equipment", "Undeveloped ground access system" and "Industrial action or strikes". These prioritization results, on the one hand, were consistent with the related congestion analysis regarding this port complex by Fan, Wilson and Dahl [6] to a large extent, in which rail corridor constraints were considered more constraining than port restrictions. On the other hand, it suggested that congestion in LA-LB ports was largely associated with the landside system and the platform itself rather than external shocks from the seaside interface, such as unanticipated surges in import cargo volumes or vessel bunching. In other words, the bottleneck of port operations has been transferred to the yard side [24] and the inland transportation system rather than exiting on the quay side as was usual situation decades ago. This is consistent with the current situation of the container port systems in the USA. Furthermore, compared with the conclusion obtained from Bolat, Kayisoglu, Gunes, Kızılay and Ozsogut [16], the rankings of "Skilled labor shortage" and "Shortage of truck-drivers/drayage truck" rise. This is because of the extent of the workforce shortage during the pandemic is higher than in any other period, while the movement of goods to keep supply chains running still depends on human labor. Therefore, if some specific and radical decisions such as vaccination campaigns for protecting the workforce are added, the identified congestion risks may be mitigated or prevented. Since risk mitigation/control strategies are not included in this paper, this part is omitted and can be further discussed in the future research.

A major limitation of this paper is that all these values (including final comprehensive weights of each risk parameter and risk prioritization) are obtained from the synthesis of experts' judgements. Consequently, the usefulness of the result is still heavily hindered by the subjectivity. For instance, during the research, it was found that the worse the detection, the higher the ranking. This is probably a consequence of the comprehensive weight of parameter D being the highest, which was calculated based on the experts' opinions. The experts interviewed stressed the importance of visibility in the port congestion risk assessment. However, these problems could be solved if we consider objective statistic data to calculate the weights. In addition, it is also noteworthy that the weights of each risk parameter shown in Table 4 only represent the case of LA-LB ports. In fact, the value of the weight might be changed for each case study, its context and respondents. Therefore, the developed fuzzy belief rule base (FBRB) in this paper needs to be reconstructed accordingly and appropriately verified when the proposed methodology is applied to a new investigated scenario, so as to ensure practical and non-biased belief functions which fit the newly investigated ports. Additionally, it is noteworthy that the developed model is unable to analyze the link between internal and external risks. When one risk factor is solved, whether other risks are sorted or not could also be an interesting direction for future research.

# 5. Conclusions 

Affected by the COVID-19 pandemic, for the whole maritime system, especially the port logistics system, there exist various types of uncertainties. The frequency and severity of port congestion are increasing, due to various risk sources. Therefore, it is necessary to study congestion in ports and create a flexible and effective method for assessing port congestion risks.

The main theoretical contribution of this paper lies in the innovative analysis of the risk of port congestion during the pandemic. In view of the lack of related research and objective data, a clear and well-reasoned congestion risk concept was defined and coupled with congestion cases to identify existing risk factors contributing to port congestion. Then, we developed a novel congestion risk model with a coupled method (i.e., FMEA, a Fuzzy Belief Rule-Based Bayes Network, AHP and the variation coefficient method), in which the extended RPI provided a basis for obtaining input information and risk prioritization; FBRBBN allowed to expression and tackling of vagueness and uncertainty in expert judgments, thereby achieving risk inference. Additionally, AHP and the variation coefficient method

were utilized to establish a reasonable and robust FBRB. The proposed method provides the possibility of comparing the congestion risk factors of different perspectives in one single framework.

The illustrative example and a scientific process using the sensitivity analysis proved the feasibility and reliability of the newly proposed model. As far as the practical contributions are concerned, for LA-LB ports, "Interruption of railways/barges services" is the most significant one, followed by "Skilled labor shortage", "Shortage of truck-drivers/drayage truck", "Inefficient and insufficient port infrastructure/equipment", "Inefficiency of inland transportation system" and "Industrial action or strikes". The results could also help the managerial practices in the realms of the investigated ports.

To overcome the limitations of the paper analyzed in the discussion part above, on the one hand, collecting objective statistic data for calculating the weights of each parameter will facilitate the accuracy and usefulness of the model. On the other hand, in future research, the proposed method can be applied to and adapted to other ports or scenarios to test its feasibility in a wider context. Additionally, a risk mitigation/control strategy or the analysis of the link between internal and external risks may be other prospective research directions.

Author Contributions: Conceptualization, H.W. and M.Y.; methodology, D.G. and H.W.; software, D.G.; validation, D.G., H.W. and M.Y.; formal analysis, D.G.; data curation, D.G.; writing—original draft preparation, D.G.; writing-review and editing, H.W. and M.Y.; funding acquisition, M.Y. All authors have read and agreed to the published version of the manuscript.
Funding: This paper has been funded by the National Key R\&D Program of China [2020YFB1712400 and 2019YFB1600400] and the National Natural Science Foundation of China [71672137].
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to thank the five experts who participated for their valuable input in the case study.

Conflicts of Interest: The authors declare no conflict of interest.
