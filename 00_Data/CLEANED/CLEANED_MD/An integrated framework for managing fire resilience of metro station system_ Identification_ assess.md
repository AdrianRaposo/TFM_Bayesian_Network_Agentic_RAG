# International Journal of Disaster Risk Reduction

## An integrated framework for managing fire resilience of metro station system: identification, assessment and optimization

--Manuscript Draft--

Southeast University
Nanjing, Jiangsu Province CHINA  |

Dear Editors,

We would like to submit the enclosed manuscript entitled "An integrated framework for managing fire resilience of metro station system: identification, assessment and optimization", which we wish to be considered for publication in "International Journal of Disaster Risk Reduction". We claim that there is no conflict of interest in the manuscript and concerned materials have never been published or under consideration elsewhere. The approval by all the listed authors, including Yuchun Tang, Wei Bi, Liz Varga, Tom Dolan, and Qiming Li, for publication has been confirmed.

As a sociotechnical infrastructure system composed of equipment and facilities, operational staff, and passengers, metro station systems (MSSs) manage threats of high-frequency fires in the city, but scant attention is drawn to how MSSs in operation systematically cope with fires. To improve the existing MSSs' poor performance across the fire lifecycle, the concept of fire resilience is proposed based on the system resilience theory. The disaster scene analysis, TOSE approach, and modified TOPSIS method are combined to identify critical fire resilience indexes. Then, a Bayesian network is developed to assess fire resilience and reveal critical causal chains in fire scenes. Furthermore, sensitivity analysis and dynamic Bayesian network with critical importance analysis are adopted to formulate optimization strategies for MSSs in different periods of operating life. The resulting integrated framework for managing fire resilience is applied to Nanjing MSS, providing operational staff and decision makers with practical tools to engage in long-term resilient operation of MSS against fires within a clear manageable scope. The results indicate that passengers' safety knowledge and behaviors, effectiveness of security screening operations, and skills of staff in emergency response team are the prime factors resulting in low fire resilience; meanwhile, economic resource allocation should be prioritized for optimization initially, but optimization priorities should be transferred to the less controllable passengers' escape skills and aging firefighting equipment as operating life increases. The integration of identification, assessment, and optimization methods can also be flexibly embedded into various infrastructure systems' operation management processes to optimize disaster resilience continuously.

We would appreciate it that you can consider our manuscript and we are looking forward for any comments and suggestions from the reviewers. Should you need to contact me, please find my contact information as follows:

Postal address: Department of Construction Management and Real Estate, School of Civil Engineering, Southeast University, Nanjing 211189, China
E-mail address: cmre_lqming@163.com
Tel: $+86-13505186838$

Thank you very much for consideration.

Yours sincerely,
Dr. Qiming Li (corresponding author)
School of Civil Engineering, Southeast University, China

# Highlights 

- Propose a model to identify fire resilience indexes for metro station system.
- Construct a Bayesian network to simulate formation and emergence of fire resilience.
- Perform critical importance analysis for dynamic optimization of fire resilience.
- The proposed methods are applied in a real-world case through investigating experts.

1 Title page
1
2 An integrated framework for managing fire resilience of metro station system: identification,
3 assessment and optimization

4 Yuchun Tang ${ }^{\text {a }}$, Wei Bi ${ }^{\text {b }}$, Liz Varga ${ }^{\text {c }}$, Tom Dolan ${ }^{\text {c }}$, Qiming Li ${ }^{\text {a, } *}$

5 a Department of Construction Management and Real Estate, School of Civil Engineering, Southeast

6 University, Nanjing 211189, China
$7{ }^{\text {b }}$ Department of Engineering, University of Cambridge, Cambridge CB2 1PZ, UK
$8{ }^{c}$ Department of Civil, Environmental and Geomatic Engineering, University College London, London,
9 WC1E 6BT, UK

10 *Corresponding author
11 E-mail address: cmre_lqming@163.com
12 Postal address: Department of Construction Management and Real Estate, School of Civil Engineering,

13 Southeast University, Nanjing 211189, China
14 Tel: $+86-13505186838$

15 An integrated framework for managing fire resilience of metro station system: identification,
16 assessment and optimization

## Abstract

18 As a sociotechnical infrastructure system composed of equipment and facilities, operational staff, and
19 passengers, metro station systems (MSSs) manage threats of high-frequency fires in the city, but scant
20 attention is drawn to how MSSs in operation systematically cope with fires. To improve the existing MSSs'
21 poor performance across the fire lifecycle, the concept of fire resilience is proposed based on the system
22 resilience theory. The disaster scene analysis, TOSE approach, and modified TOPSIS method are combined
23 to identify critical fire resilience indexes. Then, a Bayesian network is developed to assess fire resilience and
24 reveal critical causal chains in fire scenes. Furthermore, sensitivity analysis and dynamic Bayesian network
25 with critical importance analysis are adopted to formulate optimization strategies for MSSs in different
26 periods of operating life. The resulting integrated framework for managing fire resilience is applied to
27 Nanjing MSS, providing operational staff and decision makers with practical tools to engage in long-term
28 resilient operation of MSS against fires within a clear manageable scope. The results indicate that passengers'
29 safety knowledge and behaviors, effectiveness of security screening operations, and skills of staff in
30 emergency response team are the prime factors resulting in low fire resilience; meanwhile, economic resource
31 allocation should be prioritized for optimization initially, but optimization priorities should be transferred to
32 the less controllable passengers' escape skills and aging firefighting equipment as operating life increases.
33 The integration of identification, assessment, and optimization methods can also be flexibly embedded into
34 various infrastructure systems' operation management processes to optimize disaster resilience continuously.

35 Keywords: Metro station system; Fire resilience; Resilience capacities; Disaster scenes; Dynamic Bayesian
36 network

# 1 Introduction 

By the end of 2020, 538 cities worldwide had operational metros with a total length reaching 33346
kilometers [1]. As an urban lifeline infrastructure, metros provide cities with daily transportation services
and disaster relief functions, such as emergency evacuation and emergency supply transportation, which guarantees cities' public safety. Furthermore, most metros are located in urban underground spaces and have complex structures and dense passenger flows, which dramatically increases various disaster risks [2].

According to incomplete statistics of metro operation accidents, metro stations have the highest accident rates
in an entire metro system [3]; meanwhile, fire disasters are the accident type with the highest occurrence probability and the most severe consequences among all operation accidents [4]. Therefore, it is urgent to identify, assess and optimize metro stations' capacities to address fire disasters to minimize catastrophic economic losses and negative social impacts.

Current research on metro station fires mainly focuses on risk management with the goal of efficient fire prevention and emergency management with the goal of robust fire resistance, which emphasizes structural response to fires, but ignores the participation of operational staff and passengers during the fire recovery and adaptation [5]. Although fire resilience has gradually attracted attention, most related research aims only to address the functional continuity of equipment and facilities from structural perspective [6, 7], which ignores the role of operators and users in disaster resilience management of infrastructure systems. To fill the above gaps, this research applies system resilience theory to define the fire resilience of a metro station system (MSS) as the comprehensive capacities to absorb and resist negative impacts of fires, return to normal operations, and adapt to potential fires. Meanwhile, considering that the causality between the formation and emergence of fire resilience is usually neglected in existing resilience assessment tools [8, 9], this research integrates the disaster scene analysis and the technical, organizational, social, and economic (TOSE) approach to establish a standardized D-TOSE model to identify fire resilience indexes including assessment

indicators and influential factors. In this model, assessment indicators reflecting fire resilience formation are identified as resilience capacities in the fire lifecycle scenes, and influential factors reflecting fire resilience emergence are identified from the TOSE dimensions. Then, the impacts of the emergence process of the influential factors on the formation process of resilience capacities are quantified by integrating resilience capacities with their influential factors and fire scene status into a Bayesian network (BN). Moreover, given that static BN model cannot be updated quickly according to the development or degradation characteristics of the system [10], dynamic Bayesian network (DBN) model is applied to capture the changing law of the failure probability of various influential factors as the MSS operating life increases. Finally, sensitivity analysis and critical importance analysis are combined to provide decision makers with current, short-term, and long-term optimization strategies of fire resilience. The above methods are integrated into a systemic framework for operational staff and decision makers to manage fire resilience of MSSs through scene-based identification, causality-based assessment, and time-based optimization. Such integration is applied in Nanjing MSS and advances comprehensive understanding of the system's existing fire resilience level and optimization strategy preferences, helping MSSs respond to fires with minor occurrence, less consequence, and faster recovery.

# 2 Literature review 

### 2.1 Fire safety management for metro stations

Metro stations are characterized by complex fire compartmentation, limited evacuation paths, narrow emergency rescue space, etc. Once fires occur in metro stations, they quickly cause severe casualties and public property losses [11]. Therefore, studies on the fire safety management of metro stations have been extensively conducted with the following three aspects: (1) As for the existing studies on fire risk prevention for metro stations, they mainly propose targeted prevention measures of high-frequency hazards through statistical analysis and risk assessment [12, 13]. Many studies have found that fires breaking out in metro


facilities, the interruption consequences caused by technical faults of trains, tracks, and cables are often identified as resilience metrics [25-27]. From the perspective of topological networks, a metro system is usually modeled as a complex network loaded with various attack strategies, including node, edge, and space destruction. And changes in the topological attributes of a metro network are usually identified as resilience metrics [28, 29]. (2) Metro system resilience assessment is realized by quantifying system performance or resilience capacities [30, 31], in which the performance-based method assesses resilience by the geometric solution of the change curve of the system performance over time [32], and the capacity-based method assesses resilience by inferring the resilience capacity level [33]. Because of the limited data on damage to infrastructures, many studies support the capacity-based method and indicate that resilience capacities as assessment indicators can be adjusted more flexibly according to different types of systems and disasters, which makes it easier to collect basic data [34]. However, the existing capacity-based assessment indicators usually do not address all the resilience capacities formed throughout the disaster lifecycle, which causes final assessment results reflecting reliability, robustness, and vulnerability, instead of resilience [35]. Meanwhile, almost all indicators are static and cannot be automatically updated as operating life increases [36]. Hence, corresponding resilience assessment results cannot assist in decision-making for long-term system operations.

In conclusion, the shortcomings of existing research are as follows: (1) Most research objects focus on metro systems' physical hardware and topological network, but there is a lack of attention to metro stations that are simultaneously equipped with service function and topological function [37]. In addition, metro system resilience is mainly assessed by simulating generalized attacks on metro networks without a characteristic analysis of specific disasters. Hence, the formation and emergence of various system resilience capacities against specific disasters are still black-box issues. (2) Most resilience optimization strategies fail to consider complex time-varying characteristics of metro system components' functional states and their

gain or loss effects on resilience capacities over time [38]. To address the above deficiencies, this research
selects metro station as the system and fire disaster as the disturbance, and then proposes the concept of fire resilience based on system resilience theory. Furthermore, resilience capacities with their dynamic influential
factors are considered in BN model and DBN model to assess and optimize fire resilience of the MSS.

# 3 Methodology 

### 3.1 Three-phase integrated framework

System resilience theory indicates that resilience is an inherent property of a system in operation; meanwhile, assessing and optimizing system resilience are premised on the basis of identifying the system, disturbance, time period when the system experiences the disturbance, required capacities of the system to handle the disturbance, and influential factors of required capacities [39]. It is worth noting that system resilience should be built not only in the technical and physical elements as in traditional engineering practices, but also in the social and organizational elements. Therefore, in this research, the MSS is defined as a sociotechnical system composed of "hard" parts including equipment and facilities as well as "soft" parts including operational staff and passengers [40-42]; the disturbance is fire disaster; the time period refers to the fire lifecycle, namely, prior-disaster, in-disaster, post-disaster and after resuming operation stages; the remaining two elements are resilience capacities as assessment indicators of fire resilience and their influential factors, reflecting the formation and emergence process of fire resilience, respectively. A three-phase integrated framework is proposed as shown in Fig. 1 to fulfill scene-based identification, causality-based assessment, and time-based optimization of fire resilience.

![img-0.jpeg](img-0.jpeg)

Fig. 1. A three-phase integrated framework for managing fire resilience

# 3.2 Identification methods in Phase 1 

Phase 1 aims to identify fire resilience of the MSS based on fire lifecycle scenes. The disaster scene analysis
and TOSE approach are integrated to construct the D-TOSE model for identifying fire resilience indexes, including assessment indicators and influential factors. Then, the modified technique for order preference by similarity to ideal solution (TOPSIS) is used to calculate influential factors' contributions on fire resilience for screening critical influential factors tailored to different MSSs. The identification methods in Phase 1 help operational staff and decision makers fully understand specific resilience capacities and influential factors involved in the fire lifecycle, which encourages them to engage in resilient operation of MSS within a clear manageable scope.

### 3.2.1 Disaster scene analysis to identify assessment indicators

To date, many studies have reached a basic consensus that the resilience capacities are effective assessment indicators to quantify disaster resilience of infrastructure systems [43], and they include absorption capacity

to prevent disturbances, resistance capacity to minimize consequences, recovery capacity to return to normal operations, and adaptation capacity to learn from undesirable situations [44, 45]. However, the connotation of resilience capacities is still very abstract for front-line operational staff and decision makers, which easily causes inefficient resilience management due to significant understanding bias when assessing resilience capacities. Because the basis of analyzing the antecedents and consequences of disasters is to determine specific scenes (or scenarios), the scene analysis has been increasingly applied to infrastructure disaster management [46, 47]. It is worth noting that the scene analysis emphasizes that one scene should contain both "hard" and "soft" elements including physical space, awareness, and behaviors [48], which coincides with the system boundaries defined in system resilience theory. Hence, combing with specific disaster characteristics, one fire scene can be divided into reaction components, reaction time, reaction causes, reaction behaviors, and scene statuses to capture resilience capacity and its corresponding efficacy [49], which facilitates understanding and assessing resilience capacities through observing scene status of the MSS under its different reaction components' reaction behaviors. The fire lifecycle is divided into the following four fire scenes as shown in Table 1:
(1) the prevention scene, where the absorption capacity forms, is characterized by the prevention status of unsafe passenger behaviors and unsafe equipment and facilities;
(2) the response scene, where the resistance capacity forms, is characterized by the response status of fire detection, evacuation, and extinguishment;
(3) the restoration scene, where the recovery capacity forms, is characterized by the reuse status of equipment, facilities and operation services;
(4) the learning scene, where the adaptation capacity forms, is characterized by the feedback status from the operation organization.

184 Table 1 Fire scene analysis of an MSS


# 3.2.2 TOSE approach to identify preliminary influential factors 

It should be acknowledged that identifying influential factors of fire resilience not only emphasizes the disaster lifecycle, but also needs to focus on the whole system and systematically subdivide the influential factors to reflect different types of reaction components' contribution to resilience in fire scenes. In this research, the TOSE approach is applied to further subdivide all the influential factors into technical, organizational, social, and economic dimensions, which respectively represent physical hardware operation related to equipment working status and facility design features; operational management implementation related to all the internal work teams including inspection team, training team, emergency response team, maintenance team, customer service team, technical service team and data and analytics team; social organization interaction related to passengers and external organization access; and resource allocation related to decision makers' input of investments, equipment, and manpower [34, 50]. Then, four dimensions from the TOSE approach and four fire scenes from the disaster scene analysis are combined to establish the D-TOSE model, which provides a systematic classification matrix to identify influential factors. Moreover, the relevance of each influential factor to the 4 R attributes of system resilience (namely, robustness,

redundancy, resourcefulness, and rapidity [51]) should also be judged to guarantee that all identified influential factors are closely related to fire resilience, which can confirm when influential factors come into play, whether the MSS better resist various negative impacts of fire, possess more replaceable redundancy components, schedule resources more reasonably, and recover operational services faster.

# 3.2.3 Modified TOPSIS method to screen critical influential factors 

The limited investment should be optimized the most critical influential factors of fire resilience; in addition, different operational management schemes and philosophies of metro stations in various cities lead to different preferences for critical influential factors. Therefore, it is essential to screen critical influential factors before the formal assessment and optimization of fire resilience of an MSS. The TOPSIS method has been gradually applied to screen the influential factors of engineered system resilience [52], and this research modifies traditional TOPSIS method by constructing the "degree of contribution" as the screening threshold for each influential factor and quantifying it by combining the "degree of importance" and the "degree of differentiation", where the "degree of importance" aims to find which influential factor is no longer important with technological development, and the "degree of differentiation" aims to find which influential factors are not differentiated for most metro stations. The steps of applying the modified TOPSIS method to screen the critical influential factors are illustrated as follows [53, 54].
(5) Step1: Construct the initial decision matrix $X$

Each influential factor has three attributes: likelihood of occurrence $(p)$, severity of consequence $(c)$, controllability of uncertainty $(\alpha)$, and they can be marked through questionnaire survey on a 5-point Likerttype scale as "Unlikely=1, Seldom=2, Occasional=3, Likely=4, Frequent=5", "Negligible=1, Minor=2, Moderate=3, Major=4, Catastrophic=5", and "Very difficult =1, Difficult =2, Neutral=3, Easy=4, Very easy $=5$ " respectively. Meanwhile, $p$ and $c$ are positive, and $\alpha$ is negative; namely, the larger the value of $p$ and $c$, the smaller the value of $\alpha$, the more important this influential factor is [55]. The initial decision matrix

$$
X=\left[\begin{array}{cccc}
X_{11} & X_{12} & X_{13} \\
X_{21} & X_{22} & X_{23} \\
\vdots & \vdots & \vdots \\
X_{m, 1} & X_{m, 2} & X_{m, 3}
\end{array}\right]=\left[\begin{array}{cccc}
\frac{\sum_{1}^{K} x_{11}}{K} & \frac{\sum_{1}^{K} x_{12}}{K} & \frac{\sum_{1}^{K} x_{13}}{K} \\
\frac{\sum_{1}^{K} x_{21}}{K} & \frac{\sum_{1}^{K} x_{22}}{K} & \frac{\sum_{1}^{K} x_{23}}{K} \\
\vdots & \vdots & \vdots \\
\frac{\sum_{1}^{K} x_{m, 1}}{K} & \frac{\sum_{1}^{K} x_{m, 2}}{K} & \frac{\sum_{1}^{K} x_{m, 3}}{K}
\end{array}\right]
$$

Where $i$ is the $i^{t h}$ preliminary influential factor $(i=1,2, \cdots, m) ; j$ is the $j^{\text {th }}$ influential factor attribute $(j=1,2,3) ; X_{i j}$ is the value of $j^{\text {th }}$ attribute of $i^{\text {th }}$ influential factor, which is obtained by questionnaire survey with $K$ experts.
(6) Step2: Calculate the weighted sum of squares of the distance between positive and negative ideal solutions $f_{i}(\omega)$

The questionnaire data $X_{i j}$ is normalized to $r_{i j}$ with Equation (2)-(3) for positive attributes $(p, c)$ and negative attribute $(\alpha)$. The weights of $p, c$, and $\alpha$ are $\omega_{1}, \omega_{2}$, and $\omega_{3}$ respectively, and the total weight is 1 . Then, $f_{i}(\omega)$ is calculated with Equation (4):

$$
\begin{gathered}
r_{i j}=\frac{x_{i j}-\min \left(X_{i j}\right)}{\max \left(X_{i j}\right)-\min \left(X_{i j}\right)}, \text { where } j=1,2 \\
r_{i j}=\frac{\max \left(x_{i j}\right)-x_{i j}}{\max \left(x_{i j}\right)-\min \left(x_{i j}\right)}, \text { where } j=3 \\
f_{i}(\omega)=f_{i}\left(\omega_{1}, \omega_{2}, \omega_{3}\right)=\sum_{j=1}^{3} \omega_{j}^{2}\left(1-r_{i j}\right)^{2}+\sum_{j=1}^{3} \omega_{j}^{2} r_{i j}^{2}
\end{gathered}
$$

When the distance is used as a limiting condition, a smaller value of $f_{i}(\omega)$ is better. To achieve this goal, the goal programming model is established as Equation (5), then Lagrange function is constructed as Equation (6) to calculate the optimal solution as Equation (7)

$$
\begin{gathered}
\min f(\omega)=\sum_{i=1}^{3} f_{i}(\omega), \text { where } \sum_{j=1}^{3} \omega_{j}=1, \omega_{j} \geq 0, j=1,2,3 \\
F(\omega, \lambda)=\sum_{i=1}^{m} \sum_{j=1}^{3} \omega_{j}^{2}\left[\left(1-r_{i j}\right)^{2}+r_{i j}^{2}\right]-\lambda\left(1-\sum_{j=1}^{3} \omega_{j}\right) \\
\omega_{j}=\frac{\mu_{j}}{\sum_{j=1}^{3} \mu_{j}}, \text { where } \mu_{j}=\frac{1}{\sum_{i=1}^{m}\left[\left(1-r_{i j}\right)^{2}+r_{i j}{ }^{2}\right]}, j=1,2,3
\end{gathered}
$$

(7) Step3: Calculate the degree of importance $I_{i}$

Based on the weights calculated in Step 2, $I_{i}$ is calculated with Equation (8):

$$
I_{i}=\omega_{1} x_{i 1}+\omega_{2} x_{i 2}+\omega_{3}\left(6-x_{i 3}\right), \text { where } i=1,2, \cdots, m
$$

The threshold value of $I_{i}$ is set to delete influential factors that are unlikely to occur, have negligible consequences, and are very easy to control. Hence, it is calculated as follows: $I_{0}=\omega_{1} \times 2+\omega_{2} \times 2+\omega_{3} \times$ $(6-4)=2$. When $I_{i}<I_{0}$, this influential factor is judged to be unimportant.
(8) Step4: Calculate the degree of differentiation $D_{i}$

The influencing proportion of $i^{\text {th }}$ influential factor to the whole influential factor system is defined as $k_{i}$ in Equation (9). Taking into account the differences in the relative importance of each attribute of $i^{\text {th }}$ influential factor, the influential proportion of attribute $j$ of $i^{\text {th }}$ influential factor is defined as $p_{i j}$ in Equation (10).

$$
\begin{gathered}
k_{i}=\frac{f_{i}(\omega)}{\sum_{i=1}^{m} f_{i}(\omega)}, \text { where } i=1,2, \cdots, m \\
p_{i j}=\frac{r_{i j} k_{i}}{\sum\left(r_{i j} k_{i}\right)}, \text { where } i=1,2, \cdots, m ; j=1,2,3
\end{gathered}
$$

Based on the entropy theory, entropy value $H_{i}$ and entropy weight $e_{i}$ can be combined to determine each influential factor's $D_{i}$ with Equations (11)-(13):

$$
\begin{gathered}
H_{i}=-k \sum_{j=1}^{3} p_{i j} \ln p_{i j}, \text { where } k=\frac{2}{i n m} \text { to make sure that } H_{i} \epsilon[0,1] \\
e_{i}=\frac{1-H_{i}}{m-\sum_{i=1}^{m} H_{i}}, \text { where } i=1,2, \cdots, m \\
D_{i}=\frac{e_{i}}{H_{i}}=\frac{1-H_{i}}{\left(m-\sum_{i=1}^{m} H_{i}\right) H_{i}}, \text { where } i=1,2, \cdots, m
\end{gathered}
$$

The larger the value of $D_{i}$ means that $i$ is more beneficial for decision making. However, when $H_{i}$ is infinitely close to 1 , the contribution of each attribute is consistent, resulting in the influential factor $i$ not having a substantial role compared with the other influential factors. Therefore, the maximum value of $H_{i}$ is generally set to 0.8 as the threshold, and $D_{i}$ 's threshold value $D_{0}$ can be calculated accordingly [56]. When $D_{i}<D_{0}$, this influential factor is judged to be undifferentiated.
(9) Step5: Calculate the degree of contribution $C_{i}$

To ensure that influential factor $i$ is important and differentiated to MSS fire resilience at the same time,

$I_{i}$ and $D_{i}$ are combined to calculate $C_{i}$ with Equation (14):

$$
C_{i}=\frac{I_{i} D_{i}}{\sum_{i=1}^{m} I_{i} D_{i}}, \text { where } i=1,2, \cdots, m
$$

According to the threshold values of $I_{i}$ and $D_{i}, C_{i}$ 's threshold value $C_{0}$ can be calculated to screen critical influential factors. When $C_{i}<C_{0}$, this influential factor is deleted.

# 3.3 Assessment methods in Phase 2 

Phase 2 aims to assess fire resilience of the MSS based on causality inference. The BN model is applied to simulate complex causality between fire resilience capacities and their influential factors. Then fuzzy comprehensive evaluation method (FCEM) and Leaky Noisy-OR model are respectively applied to calculate the prior probabilities and conditional probabilities of nodes in the model according to questionnaire survey on causality among nodes. Finally, fire resilience is assessed through BN inference including forward and backward propagation analysis. The assessment methods in Phase 2 help operational staff and decision makers understand how fire resilience forms and emerges under complex causality, grasp MSS's current fire resilience level, and reveal the weakest chains in the fire resilience operation process.

### 3.3.1 Bayes theorem to construct the BN model

Considering the uncertainties of the fire lifecycle, this research applies the BN model and its inference rules to assess fire resilience. The BN model is a directed acyclic graph consisting of nodes and directed arcs, where the nodes represent various random variables and the directed arcs directing from the parent node to the child node quantify the conditional dependencies between nodes [57]. Additionally, a node not linked to any parent node is a root node, and a node not linked to any child node is a leaf node. In this research, fire resilience is regarded as the leaf node. Based on fire scene analysis of the MSS, fire resilience, four resilience capacities identified as assessment indicators, and influential factors identified from TOSE perspectives can be connected into one BN model with clear causality structure through fire scene status. The BN model can reveal how influential factors affect the emergence process of resilience capacities and how resilience


$$
\text { Noisy OR: } P\left(Y \mid X_{Y}\right)=1-\prod_{i=1}^{q}\left(1-P\left(Y \mid X_{i}\right)\right)
$$

More importantly, considering that the fires occurring in MSSs are sometimes caused by unpredictable and accidental influential factors, a leaky node $X_{L}$ is introduced to supplement possible factors that may be neglected. The basic assumption of the Leaky Noisy-OR model is that when all the parent nodes of a child node $Y$ are in a non-failure state, it is possible that $Y$ is in a failure state due to the existence of the leaky node [63]. The model is explained in Equation (17):

$$
\text { Leaky Noisy OR: } P(Y \mid X)=1-\left(1-P\left(Y \mid X_{L}\right)\right) \prod_{i=1}^{q} \frac{1-P\left(Y \mid X_{i}\right)}{1-P\left(Y \mid X_{L}\right)}
$$

where $P\left(Y \mid X_{L}\right)$ represents the probability of the occurrence of $Y$ in the absence of other causes listed in the BN structure. Considering the uncertainty of other unpredicted factors, it is assumed that $P\left(Y \mid X_{L}\right)$ is normally distributed with a confidence interval of 0.9 ; namely, $P\left(Y \mid X_{L}\right)=0.1$ [64].

Finally, the complete NPT of each node in the BN model can be obtained by experts only judging the failure probability of each root node and the probability that each parent node failure will cause its child node failure. Moreover, considering that the causality judgment should be more meticulous than the importance judgment of influential factors in Section 3.2.3, the failure likelihood of each root node and their causality with child nodes are measured through questionnaire survey on a scale of 1-7 points [65]. Then, all questionnaire data representing expert judgment are transformed into node probabilities through FCEM, and the specific data transformation process is shown in Table 2.

Table 2 Data transformation process of expert questionnaire data


Extremely unlikely (EU) $(0,0,0.1,0.2)$
Very unlikely (VU) $\quad(0.1,0.2,0.2,0.3)$
Unlikely (U) $\quad(0.2,0.3,0.4,0.5)$
More or less (ML) $\quad(0.4,0.5,0.5,0.6)$
Likely (L) $\quad(0.5,0.6,0.7,0.8)$
Very likely (VL) $\quad(0.7,0.8,0.8,0.9)$
Extremely likely (EL) $\quad(0.8,0.9,1,1)$

![img-1.jpeg](img-1.jpeg)


# 3.4 Optimization methods in Phase 3 

314 Phase 3 aims to optimize fire resilience of the MSS. Considering the impacts of influential factors' timevarying characteristics on fire resilience, the DBN model is established through setting probability distribution functions for the state transition of different influential factors. Then, sensitivity analysis is conducted to formulate static optimization strategies based on diagnostic perspective, and critical importance (CI) analysis is applied to formulate dynamic optimization strategies based on predicted perspective. The optimization methods in Phase 3 incorporate the degradation and strength characteristics of various influential factors of fire resilience over time into the optimization strategy, which makes BN model be automatically updated to determine optimization priorities from both static and dynamic aspects.

### 3.4.1 DBN model to capture system state transitions

323 In the practice of resilience management through the BN model, decision makers have frequently ignored the change characteristics of system component states over time, which makes optimization strategies not

appropriate for long-term system operations [67]. Therefore, to incorporate influential factors' state change
rules into the decisions on optimization priorities, the Markov law is introduced into the traditional BN model
to generate the DBN model with the following two assumptions [68]:
(1) The BN structure does not change over time, and the conditional probability remains the same;
(2) The probability distribution of the next state depends only on the current state and not on the sequence
of events that preceded it.

A DBN model has two types of arcs, including normal arcs linking nodes at the same time slice and temporal arcs linking nodes at different time slices. The joint probability of $X=\left(X_{1}, X_{2}, \ldots, X_{i}, \ldots, X_{n}\right)$ at the $t+\Delta t$ time slice can be mathematically expressed as Equation (24):

$$
P\left(X^{t+\Delta t}\right)=\prod_{i=1}^{n} P\left(X_{i}^{t+\Delta t} \mid X_{i}^{t}, P a\left(X_{i}^{t}\right), P a\left(X_{i}^{t+\Delta t}\right)\right)
$$

where $P a\left(X_{i}^{t}\right)$ and $P a\left(X_{i}^{t+\Delta t}\right)$ represent parent nodes of $X_{i}^{t}$ and $X_{i}^{t+\Delta t}$.
334335
335
32
336
337
38
39
40
41
rank of nonfailure probabilities, hence, the prior probability of each root node is increased step by step with
43
a $5 \%$ step length from the original probability to $100 \%$, which simulates decision makers gradually increasing optimization inputs for this root node until it does not fail completely, and then the increments of four fire resilience capacities are observed as optimization effects. Furthermore, the optimization effects of four resilience capacity increments on fire resilience are also observed. Finally, the optimization priority of influential factors and resilience capacities can be ranked by calculating the average sensitivity coefficient (i.e., the percentage change in the nonfailure probability of the root note to the percentage change in the target nodes [70]).

347 Compared with static sensitivity coefficient, CI indicator, which is defined as the ratio of the change
348 rate of the root node's failure probability to the leaf node's failure probability, can better grasp the dynamic
349 influence of root node failure on leaf node failure from both perspectives of sensitivity and the failure
350 probability itself. Meanwhile, CI reflects that optimizing a root node with a high failure probability is easier
351 than a root node with a low failure probability [71, 72]. In this research, the rank changes in the CI of the
352 influential factors are observed to determine dynamic changes in the optimization priorities, helping
353 operational staff predict the contribution changes of different influential factors on fire resilience over
354 increasing operating life, and make scientific decisions on breakdown maintenance and safety investments.
355 The CI of the root node $i$ at a specific time slice is calculated as Equation (25) [73]:

$$
I_{i}=\frac{P\left(X_{i}=1\right) *\left(P\left(R=1 \mid X_{i}=1\right)-P\left(R=1 \mid X_{i}=0\right)\right)}{P(R=1)}
$$

356 where $X_{i}$ is a binary variable which represents the state of root node $i$ (i.e., 1 and 0 represents failure state
357 and reliable state, respectively); $R$ represents the state of leaf node; $P(R=1 \mid \cdot)$ represents the conditional
358 probability of the leaf node failure; $P(R=1)$ represents the failure probability of the leaf node.

# 4 Case study results and discussion 

### 4.1 Study case and data collection

361 Nanjing MSS has served about 3.5 million passengers daily since it opened in 2005, and it has real historical
362 experience in coping with fire accidents. Therefore, Nanjing MSS was chosen as a real-life case application
363 to demonstrate how the developed D-TOSE model, BN model, and DBN model assist operational staff and
364 decision makers to identify, assess and optimize MSS fire resilience at city level, which can provide valuable
365 references to other cities' MSS facing challenges of fire resilience management. Given that the number of
366 participants who can make professional judgment on influential factors' importance and causality with
367 sufficient relevant knowledge and practical experience is minimal, most case studies tend to choose 5-30
368 experienced experts to guarantee the validity of the questionnaire data [74-76].

To collect data for screening critical influential factors of fire resilience, a one-day facilitated workshop
with Questionnaire survey A (see Section Supplementary material) that investigates the contribution degree
of each influential factor was conducted in Nanjing with 51 participants, including front-line operational staff
for station operation, line operation, and company management from the Nanjing metro operating company.
And the selection of participants is strictly abided by the criteria suggested by Witkin and Altschuld to guarantee that all participants have a deep understanding of metro station fire in the operation phase [77].

The workshop started with a detailed presentation to introduce the preliminary influential factors and their corresponding failure modes identified through the D-TOSE model, then followed by a panel discussion for the 51 participants to supplement and revise the factors. Immediately after the facilitated workshop, the updated Questionnaire $A$ was conducted among 51 participants independently to rate $p, c$, and $\alpha$ of each influential factor on a scale of 1 to 5 points. Among the 51 returned questionnaires, 15 invalid questionnaires were removed due to the participants' insufficient rating duration and lack of working experience (i.e., less than 3-year working periods). Finally, 36 valid questionnaires were collected, with a response rate of $70.6 \%$.

To collect data for calculating the NPTs, an online Questionnaire survey B (see Section Supplementary material) was conducted to investigate the causality among the influential factors on a scale of 1 to 7 points.

In this survey, the participant quality is more important than its quantity because the accuracy of causality judgment depends heavily on the participants' experience [78]. Hence, 25 out of 36 valid respondents to the Questionnaire $A$ were selected to conduct Questionnaire $B$ due to their post-fire treatment experience in Nanjing MSS. Participants need to individually judge the causality for each pair of nodes in the BN model.

Finally, 7 invalid questionnaires were removed due to participants' carelessness for failing one attention test item set in Questionnaire B. Thus, 18 valid questionnaires were collected for further analysis, with a response rate of $72 \%$. And the demographic information of valid respondents to the Questionnaire $A$ and Questionnaire $B$ is listed in Table 3.

Table 3 Demographic information of valid respondents to the Questionnaire A and Questionnaire B


# 4.2 Scene-based identification of fire resilience for Nanjing MSS 

### 4.2.1 Preliminary influential factors

Based on the D-TOSE model, a total of 36 influential factors of fire resilience for Nanjing MSS are preliminarily identified from national codes issued by the Chinese Ministry of Transport, enterprise standards issued by the Chinese metro operating companies, and metro fire accidents reported by official news. Furthermore, 3 out of 36 influential factors were supplemented by participants through the facilitated workshop, i.e., $\mathrm{AbsT}_{3}, \mathrm{ResO}_{6}$, and $\mathrm{AdaO}_{3}$. All influential factors' relationship with the 4 R attributes of system resilience, and specific failure modes are illustrated in Table 4.

Table 4 Preliminary influential factors of fire resilience for the Nanjing MSS






Notes: T, O, S, and E refer to technical, organizational, social, and economic aspects, respectively; R1, R2, R3, and R4 represent robustness, redundancy, resourcefulness, and rapidity, respectively.

# 4.2.2 Critical influential factors 

Based on the scores of three attributes $p, c$, and $\alpha$ of each influential factor from the 36 valid questionnaires collected, all preliminary influential factors' degree of importance, differentiation, and contribution were obtained as shown in Fig. 2. Then, 5 influential factors including $\mathrm{AbsT}_{2}, \mathrm{AbsO}_{6}, \mathrm{AbsS}_{2}$, $\mathrm{RecO}_{2}$, and $\mathrm{AdaO}_{4}$ were deleted according to the thresholds of importance, differentiation, and contribution calculated $I_{0}=2, D_{0}=0.0271, C_{0}=0.0118$ based on Section 3.2.3. Notably, these five influential factors were deleted due to low degree of differentiation, which indicates that these influential factors have been implemented with unified standardized operation by the whole Nanjing MSS. Finally, 31 critical influential factors applicable to Nanjing MSS were obtained.
![img-2.jpeg](img-2.jpeg)

Fig.2. Degrees of importance, differentiation, and contribution of all preliminary influential factors

### 4.3 Causality-based assessment of fire resilience for Nanjing MSS

### 4.3.1 Constructed BN model

A BN model with 44 nodes integrating assessment indicators, fire scene status variables, and influential factors is constructed as shown in Fig. 3, and each node has two state parameters: fail (State 1) and not fail (State 0).

![img-3.jpeg](img-3.jpeg)

Fig. 3. BN model for assessing fire resilience of Nanjing MSS

All the participants agreed with the nodes and their causality established in this model. Meanwhile, all
items rated by participants in the Questionnaire $B$ reached the required level (inter-rater agreement $\left(R_{w g}\right)>$
0.7) proposed by James et al. [79], which confirms the validity of constructed BN structure. The meanings of various nodes in the BN model are as follows:
(1) 4 nodes represent fire resilience capacities, including absorption capacity (Abs), resistance capacity (Res), recovery capacity (Rec), and adaptation capacity (Ada); and the leaf node represents fire resilience (R);
(2) 8 auxiliary nodes represent fire scene status variables, including unsafe behavior prevention status $\left(\mathrm{SV}_{1}\right)$,
unsafe equipment and facilities prevention status $\left(\mathrm{SV}_{2}\right)$, fire detection status $\left(\mathrm{SV}_{3}\right)$, fire evacuation status
$\left(\mathrm{SV}_{4}\right)$, fire extinguishment status $\left(\mathrm{SV}_{5}\right)$, equipment and facilities reuse status $\left(\mathrm{SV}_{6}\right)$, operation service


# 4.3.3 Backward propagation analysis 

Backward propagation is a typical effect-to-cause analysis to observe the leaf node, and the marginal probabilities of unobserved parent nodes are calculated by propagating the impact of the observed child node through the BN model in a backward fashion. In this research, the leaf node (i.e., fire resilience) is set to a complete failure state (i.e., $P(R=1)=1$ ) to identify the influential factors with high posterior probabilities in the BN model. According to the posterior probability results shown in Fig. 5, when the fire resilience of Nanjing MSS fails completely, the resilience capacity failure risks gradually increase in the order of adaptation, recovery, absorption, and resistance capacity, and their failure probabilities are $27.5 \%, 37.3 \%$, $42.8 \%$, and $50.6 \%$, respectively. Moreover, the critical cause chain with the biggest contribution to the fire resilience failure was revealed, namely, "escape skills of passengers $\left(\operatorname{ResS}_{1}\right) \rightarrow$ fire evacuation status $\left(\mathrm{SV}_{4}\right)$ $\rightarrow$ resistance capacity (Res) $\rightarrow$ fire resilience (R)". Hence, the resistance capacity was the most important guarantee for fire resilience formation in the Nanjing MSS, and the timely evacuation of passengers is the most effective measure to reduce casualties. Considering that fire evacuation efficiency is greatly affected by escape skills of passengers, it is also necessary to strengthen the publicity of fire knowledge and arrange professional command staff to help passengers evacuate quickly, which can avoid the cascading failure of the critical cause chain.

![img-4.jpeg](img-4.jpeg)

Fig. 4. Forward propagation analysis for assessing fire resilience
![img-5.jpeg](img-5.jpeg)

Fig. 5. Backward propagation analysis for revealing the critical cause chain

# 4.4 Time-based optimization strategies of fire resilience for Nanjing MSS 

### 4.4.1 Static optimization strategies

To maximize fire resilience with limited resources, it is necessary to observe the effects of optimizing different root nodes on four resilience capacities [83]. The optimization priorities of rooted influential factors
and resilience capacities can be ranked according to average sensitivity coefficients as shown in Fig. 6.


Fig. 6. Sensitivity coefficients of the 28 root nodes and 4 resilience capacities

The simulation results show that the four resilience capacities' optimization priorities are the absorption,
resistance, adaptation, and recovery capacities in descending order of the sensitivity to fire resilience, which reflects that Nanjing MSS has great optimization potential of effective fire prevention and rapid fire prevention response to fires. In addition, fire resilience capacities are the most sensitive to economic influential factors ( $\mathrm{AbsE}_{1}, \mathrm{ResE}_{1}, \mathrm{RecE}_{1}, \mathrm{AdaE}_{1}$ ), which proves that increasing the investment, equipment and manpower in fire lifecycle scenes can directly reduce the consequences of fires because sufficient resource input can provide essential economic support to optimize technical, organizational and social influential factors [84]. Except for optimizing the resource allocation, the remaining static optimization strategies are as follows:
(1) The absorption capacity is the most sensitive to $\mathrm{AbsO}_{3}$, which indicates that strengthening real-time

monitoring, regular inspection and maintenance of mechanical and electrical devices can optimize fire
prevention effect to the maximum extent;
(2) The resistance capacity is the most sensitive to $\mathrm{ResT}_{5}$, which indicates that adjusting and updating firefighting equipment types, quantities, and installation locations according to the lessons from historical fires and the latest fire safety requirements can maximize the efficiency of fire spread control;
(3) The recovery capacity is the most sensitive to $\mathrm{RecO}_{1}$, which indicates that the timely arrival and efficient coordination of repair and rescue teams can avoid secondary accidents to the greatest extent and guarantee the rapid reopening of the MSS to the public;
(4) The sensitivity coefficient of the root node affecting adaptation capacity tends to be zero, indicating that the MSS has mature fire accident investigation and rectification process with little room for improvement.

# 4.4.2 Dynamic optimization strategies 

Dynamic optimization strategies are proposed based on DBN simulation results considering system component states' change characteristics over time. The DBN model with three kinds of temporal arcs linking each root node from the current time slice $t$ to the next time slice $t+\Delta t$ is shown in Fig. 7, in which 28 root nodes of fire resilience are divided into the following three categories [85]:
(1) Equipment and facility factors, including MSS internal equipment and facilities (all the technical root nodes: $\mathrm{AbsT}_{1}, \mathrm{AbsT}_{3}, \mathrm{ResT}_{1}, \mathrm{ResT}_{2}, \mathrm{ResT}_{3}, \mathrm{ResT}_{4}, \mathrm{ResT}_{5}$, and $\mathrm{ResT}_{6}$ ) and external equipment ( $\mathrm{ResS}_{2}$ );
(2) Individual behavior factors, including operational staff's regulated behaviors for daily work and emergency work $\left(\mathrm{AbsO}_{1}, \mathrm{AbsO}_{3}, \mathrm{AbsO}_{4}, \mathrm{AbsO}_{5}, \mathrm{ResO}_{1}, \mathrm{ResO}_{6}, \mathrm{RecO}_{1}\right.$, and $\left.\mathrm{RecO}_{3}\right)$ and passengers' behavior under current knowledge and skills ( $\mathrm{AbsS}_{1}$ and $\mathrm{ResS}_{1}$ );
(3) Management experience factors, including operational organization's emergency management capabilities $\left(\mathrm{AbsO}_{2}, \mathrm{ResO}_{2}, \mathrm{ResO}_{3}, \mathrm{ResO}_{4}\right.$, and $\left.\mathrm{AdaO}_{1}\right)$ and resource investment decision-making capabilities $\left(\mathrm{AbsE}_{1}, \mathrm{ResE}_{1}, \mathrm{RecE}_{1}\right.$, and $\left.\mathrm{AdaE}_{1}\right)$.

![img-6.jpeg](img-6.jpeg)

Fig. 7. DBN model for optimizing fire resilience of Nanjing MSS

511 In addition, considering that each root node's state transition in the DBN model complies with the
hidden Markov model [86], the transition probabilities of three types of root nodes are defined as shown in
Table 5 based on the following assumptions:
(1) For equipment and facility factors, all equipment and facilities work in one of two states: normal operation (State 0) or failure (State 1). As the MSS's operating life increases, equipment and facilities
will age to a certain extent so that operational staff has to maintain all equipment and facilities regularly. It is assumed that the equipment and facility factor's failure rate due to aging is $\lambda_{1}$, and the repair rate due to regular maintenance is $\mu$. Moreover, the failure rate and repair rate of the equipment and facilities are assumed to meet the exponential distribution [87].
(2) For individual behavior factors, all individuals execute tasks or instructions in one of two states: normative (State 0) or non-normative (State 1). Considering that human errors due to non-normative behavior belong to random events, it is assumed that such a random event is a counting process, in which the average number of human errors per unit time is $\lambda_{2}$ meeting the Poisson distribution [88].
(3) For management experience factors, all teams or organizations invoke management experience to make decisions, implement plans, and allocate resources in one of two states: rational (State 0 ) or irrational (State 1). Considering that as the establishment years of operational organizations increase, the management experience will become increasingly affluent through accumulation; the experience enhancement coefficient $c$ is introduced to reflect the improvement in the decision-making level, implementation ability, and resource allocation rationality due to the enhancement of operational management experiences [89].

Table 5. Three types of root nodes' state transition probabilities


Notes: (1) $\Delta t=1$ represents 1 year; (2) $\lambda_{1}=12 / 365$ represents that equipment and facilities will breakdown 12 times a year, $\mu=0.1$; (3) $\lambda_{2}=12$ represents that human errors will occur 12 times a year;
(4) $c=0.1$ represents that management experience enhancement can reduce the related influential factors'
failure probability by $10 \%$.

In this case study, the original static BN model is transferred ten times to form the DBN model with ten time slices, and then the CI of 28 root nodes from $T_{0}$ to $T_{10}$ is obtained. Based on the numerical range of the CI, the optimization priorities are determined as follows: when $l_{i}>0.03$, the corresponding root nodes are optimized with the first priority; when $0.015<l_{i} \leq 0.03$, the corresponding root nodes are optimized with the second priority; and when $l_{i} \leq 0.03$, the corresponding root nodes are optimized with the third priority. According to the CI results of all the root nodes during ten time slices, the CI of root nodes ranked $11^{\text {th }}$ to $28^{\text {th }}$ at $T_{0}$ is lower than 0.015 in all the time slices. Therefore, the root nodes with the top 10 CI at $T_{0}$ are selected for dynamic CI analysis to help decision makers prioritize the critical influential factors at different stages of MSS operation. The dynamic optimization priorities of the critical influential factors from $T_{0}$ to $T_{10}$ are shown in Fig. 8.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Dynamic optimization priorities of the critical influential factors for Nanjing MSS

From the perspective of the influential factor type, the top 10 root nodes' dynamic optimization priorities are as follows:
(1) The CI of management experience factors ( $\mathrm{AbsE}_{1}, \mathrm{ResE}_{1}, \mathrm{RecE}_{1}$, and $\mathrm{AdaE}_{1}$ ) decreases significantly.
(2) The CI of individual behavior factors ( $\operatorname{ResS}_{1}, \operatorname{ResO}_{6}, \mathrm{AbsS}_{1}, \operatorname{RecO}_{1}$, and $\mathrm{AbsO}_{1}$ ) increases slightly.
(3) The CI of equipment and facility factor $\left(\operatorname{Res} \mathrm{T}_{5}\right)$ increases significantly.

The above predicted trend is consistent with the actual operation practice of Nanjing MSS, which reflects that as the operating life increases, the resource allocation becomes increasingly scientific with little room for further optimization; the failure probability of firefighting equipment and facilities increases due to aging; and human error occurrence increases, but human errors still belong to small probability events compared with technical failure.

From the perspective of the execution time of optimization strategies, the top 10 root nodes' dynamic

optimization strategies are as follows:
(1) In the present moment $T_{0}$, it is necessary to increase the resource allocation strength ( $\mathrm{AbsE}_{1}, \mathrm{ResE}_{1}$, $\mathrm{RecE}_{1}$, and AdaE ${ }_{1}$ ) with the first priority, facilitating rapidly building the absorption, resistance, recovery, and adaptation capacities. Then, less controllable passengers' escape skills $\left(\operatorname{ResS}_{1}\right)$ and easily overlooked fire and rescue service access $\left(\operatorname{ResO}_{6}\right)$ should be optimized with the second priority.
(2) In the short term, from $T_{1}$ to $T_{3}$, only the optimization priority of rectification resource allocation
$\left(\mathrm{AdaE}_{1}\right)$ is degraded, mainly because rectification resources involve fewer investment items than the prevention, resistance, and recovery resources and are easier to optimize within the short term.
(3) In the long term since $T_{4}$, the optimization priorities of all resource allocations are degraded, which indicates that the resource allocation level of an MSS will be optimized to a relatively ideal state without further improvement potential after many years of MSS operation. Meanwhile, long-term optimization priorities should transfer to passengers' escape skills $\left(\operatorname{ResS}_{1}\right)$ that need to be continuously cultivated by playing various videos of escape skills in various media channels of the MSS, and firefighting equipment
$\left(\operatorname{ResT}_{5}\right)$ that needs to be regularly maintained by establishing strict supervision process for monitoring, maintaining and updating firefighting equipment.

# 5 Conclusions and future work 

### 5.1 Theoretical contribution

This study establishes an integrated framework for managing MSS fire resilience, which enriches the connotation of system resilience through disaster scene analysis and provides resilience management strategies with dynamic and long-term insights through combining BN and DBN. More importantly, this systemic integration of identification, assessment, and optimization methods can be extended to various infrastructures at asset, city, and national levels.
(1) For scene-based identification methods: system resilience theory, disaster scene analysis, and TOSE

582
583
584
585
586
11
12
13587
14
15
16588
17
18589
19
20
21590
22
23
24591
25
26
27592
28
29
30593
31
32594
33
34
35595
36
37
38596
39
40597
41
42
43598
44
45
46599
47
48
49600
50
51601
52
53
54
55
56602
57
58603
583
584
approach are combined to establish a standardized D-TOSE model for identifying resilience capacities
and their influential factors in the prevention, response, restoration, and learning scenes, which facilitates
understanding the manageable scope of fire resilience and then screen out critical influential factors
tailored to different cities.
(2) For capacity-based assessment methods: the formation and emergence process of fire resilience are simulated through the BN model linking resilience capacities with influential factors and fire scene status. This BN model reveals that the emergence level of influential factors affects fire scene status; then, fire scene status further affects resilience capacity formation; finally, the formation level of resilience capacities determines the fire resilience value. Moreover, considering that the BN model involves numerous conditional probability calculations and ignores the high uncertainty of influential factors, the Leaky Noisy-OR model is introduced to simplify the conditional probability calculation process and optimize the causality inference structure.
(3) For time-based optimization methods: from diagnostic perspective, static optimization strategies conforming to the MSS's current operation situation are formulated based on the sensitivity analysis; from predictive perspective, dynamic optimization strategies for short-term and long-term operations are formulated based on the DBN model with critical importance analysis, which addresses the impact of influential factors' time-varying characteristics on MSS fire resilience. The time-based optimization method delivers static and dynamic optimization strategies by ranking the optimization priorities of various influential factors, which helps decision makers flexibly adjust optimization strategies at different stages of operating life to maximize fire resilience.

# 5.2 Practical implication 

The developed integrated framework is a practical management tool for the MSS's operational staff and decision makers. It can also flexibly adapt to the operation conditions of different metro stations in different

cities by collecting questionnaire data on the influential factors' importance and causalities with fire resilience.

Based on the case study of Nanjing MSS, the following results can be applied in practice.
(1) For identification results: 36 preliminary influential factors were identified based on the D-TOSE model, and among them, 3 influential factors including "cigarette extinguishers", "fire and rescue service access", and "implementation and supervision of the rectification" were supplemented in the facilitated workshop. However, 5 influential factors including "integrated supervision and control system", "stability control of the environment", "safe operation of underground commercial areas", "supplementary supply of emergency equipment", and "archive of fire history data" were deleted because their implementation status differed little in the current operational practice. Finally, 31 influential factors were selected to assess fire resilience of Nanjing MSS.
(2) For assessment results: the nonfailure probabilities of absorption capacity, resistance capacity, recovery capacity, adaptation capacity, and fire resilience were $75.5 \%, 70 \%, 76.9 \%, 84.8 \%$, and $68.8 \%$, respectively. These results reflect that the low fire resilience of Nanjing MSS resulted from poor system performance in the prevention and response scenes, where "passengers' safety knowledge and behaviors", "effectiveness of security screening operations", and "skills of staff on the emergency response team" had high failure probabilities. Meanwhile, the critical cause chain, "escape skills of passengers $\rightarrow$ fire evacuation status $\rightarrow$ resistance capacity $\rightarrow$ fire resilience" contributed the most to the failure of fire resilience. The above assessment results not only quantify Nanjing MSS's fire resilience value but also help operational staff confirm influential factors with the highest failure probabilities and the bottleneck existing in the fire resilience emergence process.
(3) For optimization results: from the perspective of resilience capacities, the optimization priority ranking is absorption, resistance, adaptation, and recovery capacities; from the perspective of influential factors, in addition to increasing resource allocation strength in four fire scenes, assigning the optimization

priorities to the remaining top 10 influential factors for the sensitivity to fire resilience, namely,
"firefighting equipment" from the technical dimension, "fire and rescue service access", "coordination
of repairs and rescue teams", and "inspection and maintenance of electrical equipment" from the organizational dimension, and "escape skills of passengers" and "passengers' safety knowledge and behaviors" from the social dimension, can maximize the optimization effect. More importantly, incorporating dynamic impacts of aging equipment and facilities, human error randomness, and the reinforcement of operational management experience, dynamic optimization priorities applicable to the long-term Nanjing MSS operation conditions should transfer from resource allocation to passengers' escape skills that need to be continuously cultivated and firefighting equipment that needs to be maintained regularly.

# 5.3 Limitations and future work 

This study aims to improve the understanding and optimization effect of fire resilience for operational staff and decision makers of the MSS, but the proposed integrated framework still has the following limitations:
(1) For identification methods: the interactions between the MSS and other systems (such as tunnel systems and bus systems) are not discussed in the influential factor analysis because fire resilience is regarded as the inherent capacity of an MSS.
(2) For assessment methods: considering that the causalities among resilience capacities, influential factors, and scene status are quantified by questionnaires data which is dependent on the accuracy of the fire handling experience invoked by experts, the states of all nodes in the BN model have to be set with binary parameters to match the experts' memory characteristics of historical fire disasters.
(3) For optimization methods: the existing probability distribution functions are used to simulate the state transition process of the equipment and facility factors, individual behavior factors, and management experience factors, which does not accurately describe a specific MSS's status change rules of various

influential factors as the operating life increases.

Our future research will focus on addressing the above limitations. First, influential factors representing the interdependencies of other systems interacting with an MSS will be introduced into the BN model. Second, one pilot study will be conducted by installing sensors and cameras in a specific metro station to accumulate operation and maintenance data of equipment and facilities as well as behavior data of operational staff and passengers. Finally, each influential factor's practical state distribution and transition rules will be fitted based on real-time data for precise assessment and efficient optimization of fire resilience, realizing automatic decision-making and resilient operation.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China [Grant No. 51978164], the National Construction of High Level Colleges for Postgraduate Study Abroad Project, China Scholarship Council [Grant No. 202006090370], the Postgraduate Research \& Practice Innovation Program of Jiangsu Province, China [Grant No. KYCX20_0115] and the Fundamental Research Funds for the Central Universities [Grant No. 3205002105D]. The authors are grateful to all the individuals who participated in this research and provided their expertise.

## Supplementary material

(1) Questionnaire A: Investigation on influential factors of fire resilience of metro station system
(2) Questionnaire B: Investigation on causality among influential factors of fire resilience of metro station system

# Declaration of interests 

$\boxtimes$ The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
$\square$ The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

# Click here to access/download 

## Supplementary Material

## Supplementary material Questionnaire A and

Questionnaire B.docx