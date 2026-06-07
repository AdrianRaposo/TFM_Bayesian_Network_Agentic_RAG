# Maintenance Evaluation and Optimization of a Multi-State System Based on a Dynamic Bayesian Network 

Zakaria Dahia ${ }^{1}$, Ahmed Bellaouar ${ }^{1}$, Jean-Paul Dron ${ }^{2}$<br>${ }^{1}$ Transport engineering and environment laboratory, University of Constantine 1, Constantine, Algeria<br>${ }^{2}$ University of Reims Champagne Ardenne, Reims, France

Received: 20 May 2020
Accepted: 27 May 2021


#### Abstract

Nowadays, the main challenge in maintenance is to establish a dynamic maintenance strategy to significantly track and improve the performance measures of multi-state systems in terms of production, quality, security and even the environment. This paper presents a quantitative approach based on Dynamic Bayesian Network (DBN) to model and evaluate the maintenance of multi-state system and their functional dependencies. According to transition relationships between the system states modeled by the Markov process, a DBN model is established. The objective is to evaluate the reliability and the availability of the system with taking into account the impact of maintenance strategies (perfect repair and imperfect repair). Using the proposed approach, the dynamic probabilities of system states can be determined and the subsystems contributing to system failure can also be identified. A practical application is demonstrated by a case study of a blower system. Through the result of the diagnostic inference, to improve the performances of the blower, the critical components C, F, W, and P should be given more attention. The results indicate also that the perfect repair strategy can improve significantly the performances of the blower, while the imperfect repair strategy cannot degrade the performances in comparison to the perfect repair strategy. These results show the effectiveness of this approach in the context of a predictive evaluation process and in providing the opportunity to evaluate the impact of the choices made on the future measurement of systems performances. Finally, through diagnostic analysis, intervention management and maintenance planning are managed efficiently and optimally.


## Keywords

multi-state system, dynamic Bayesian network, reliability, availability, maintenance optimization.

## Introduction

Traditional analysis methods, such as failure modes and effects analysis (FMEA), failure tree analysis (FTA) are used to assess systems reliability. When applying these methods, it is assumed that the system operates in two states, namely, perfect operating state and total failure state; also referred to as a binary state system. However, in addition to perfect functionality and complete failure, a system can have several intermediate states (Li and Peng, 2014; Sheu et al., 2015). Degraded systems are function-

[^0]ing systems whose condition degrades over time and this degradation can lead to a decrease in their performance and efficiency (Yuan and Xu, 2012). When defining a maintenance strategy, the main problem is to establish a dynamic strategy that is adapted to the evolution of the systems states. Maintenance has a major impact on the evolution of system performance measures, including dynamic parameters such as reliability and availability.

In the literature, several models for multi-state systems are used to assess these parameters and control its evolution. (Soro et al., 2010) proposed a model for assessing reliability indices and production rate of a degradable multi-state system subject to minimal and imperfect repairs. To predict the reliability of a power-generating unit in a short time-periods, a multi-state Markov model is presented by (Lisnianski et al., 2012). Liu and Huang (2010) proposed an optimal replacement policy based on the combination between the Markov model and the Universal Gen-


[^0]:    Corresponding author: Zakaria Dahia, Transport engineering and environment laboratory, University of Constantine 1, Constantine, Algeria, phone: +213 665254 094, e-mail: zahi.dahia@umc.edu.dz
    (C) 2021 The Author(s). This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/)

erating Function (UGF), they used a quasi-renewal process to evaluate the probability of system states and describe the behavior of the system after imperfect maintenance.

Today, Bayesian Network (BN) represents another area of research. It is widely used in many applications for system performance evaluation, risk analysis, diagnosis and prediction analysis, and maintenance (Weber et al., 2012; Chang et al.,2019). Reasoning from probabilistic graphical models facilitates dealing with both diagnosis and prediction problems. In addition, the graphical models which were developed by various tools, participate and facilitate the construction and model representation for many problems (Lakehal et al., 2019). Moreover, a methodology for applying BN to assess the reliability of structural systems was developed by (Mahadevan et al., 2001). Neil and Marquez (2012) presented a hybrid Bayesian network (HBN) framework to model the availability of renewable systems.

The Dynamic Bayesian Network (DBN) is an extension of BN which allows modelling the dynamic behaviour of systems. Also in DBN, a new type of nodes called 'temporal nodes' which allows the modeling of random variables over time. The description of cause and effect relationships is permitted by probability distributions (Iung et al., 2005; Weber and Jouffe, 2006). In several studies, DBN represents an appropriate solution for predictive and diagnostic analysis, as well as for expressing uncertain causal relationships (Wilson and Huzurbazar, 2007).

By translating the Failure Tree (FT) into DBN, (Cai, et al., 2013) proposed a model based on DBN to analyze and evaluate reliability and availability for a subsea BOP system. In another study, (Wang, et al., 2017) established a stochastic deterioration model for multi-element systems under a conditional maintenance strategy (CBM). A quantitative risk assessment approach based on DBN that dynamically predicts the risk of riser recoil control failure during production test of marine natural gas hydrate was presented by (Chang et al., 2019).

A combination of the Markov process and a DBN is proposed by (Li et al., 2018) to model and analyze the reliability of a multi-state system. Different types of maintenance were taking into account including, perfect repair, imperfect repair, and condition-based maintenance. (Adjerid et al., 2012) evaluated the performance of an industrial system and studied the effect of different maintenance strategies on reliability performance.

This paper aims to model a multi-state industrial system based on the Markov process and the DBN.
By using the proposed approach, the reliability and availability with respect to perfect repair and imperfect repair are evaluated. This paper is structured as follows: Section 2 presents a Bayesian approach for modelling multi-state systems. Section 3 analyzes the blower as study case, results and discussions are presented in Section 4 and Section 5 summarizes this paper.

## Bayesian approach for modelling a multi-state system

## Dynamic Bayesian network

A Bayesian Network is a probabilistic causal network that allows to graphically represent variables and their probabilistic dependencies. The BN is composed of nodes that are connected by direct arcs, the arcs indicate a causal relationship or dependency between the linked nodes, and conditional probability tables (CPTs) that determine how the linked nodes depend on each other. It can describe a multi-state element with a single node, cause and effect relationships can be designated by conditional probability distributions. Using static or dynamic logical gates, the (CPTs) can be obtained (Li et al., 2018). A DBN is an extension parallel to the ordinary BN, it allows to explicitly model the temporal evolution of variables over time (Weber and Jouffe, 2006). Each step of time is called a time slice, the probability of transition between two successive slices $P(X t \mid X t-1)$ is expressed by

$$
P\left(X_{t} \mid X_{t-1}\right)=\prod_{i=1}^{N} P\left(X_{t}^{i} \mid p a\left(X_{t}^{i}\right)\right)
$$

where $X_{t}^{i}$ represents the $i$-th node at time $t$, and $p a\left(X_{t}^{i}\right)$ represents its parent nodes.

1. A Dynamic Bayesian network expanded from time slice 0 to 1

Figure 1 represents an expanded DBN, the intraslice arcs represent the relationships between nodes (variables A and B) and the relationships between nodes at successive time intervals $t 0-t 1$ are represented by arcs between slices. By unrolling the time slices, the probability of joint distribution can be obtained by the following expression:

$$
P\left(X_{1: T}\right)=\prod_{t=1}^{T} \prod_{i=1}^{N} P\left(X_{t}^{i} \mid p a\left(X_{t}^{i}\right)\right)
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. A Dynamic Bayesian network expanded from time slice 0 to 1

### Imperfect repair modeling

In DBN modeling, it is assumed that each parent node is a degraded multi-state system, four assumptions are made (Soro et al., 2010):

1. The system might fail randomly from any operational state.
2. The component may have many levels of degradation corresponding to discrete performance rates, which vary from perfect function to complete failure.
3. All transition rates are constant and exponentially distributed.
4. The current degradation state is observable through some system parameters and the time needed for inspection is negligible.

In DBN, each parent node has four states: perfect state (Perfect), degraded state1 (DS1), degraded state2 (DS2), and fault state (Fault). The perfect state refers to perfect operation and the fault state represents a total failure. The DS1 and DS2 represent the first and second degraded states, respectively. At first, each parent node of DBN is in perfect condition, as time passes, the DBN either passes to the DS1 or DS2 states or proceed directly to the fault state. When a failure occurs, a repair is needed: the DBN can either return to perfect condition, which is considered a perfect repair or return to the first or second degraded state, which is considered as an imperfect repair. The state transition diagram for the four-state component is shown in Figure 2.

By consulting maintenance engineers of Pepsi Company and their opinions, which is mainly based on the historical data and their feedback experience, the assumptions for the failure rates between states, for each component (parent node), can be classified into two classes: minor failures class (λ3, λ4 and λ6) and major failures class (λ1, λ2 and λ5). Two classes are distinguished also for repair rates between states: Imperfect repair (μ1 and μ2) and Perfect repair (μ3). The following equations show how failure and repair rates are calculated:

![img-1.jpeg](img-1.jpeg)

Fig. 2. Transition state diagram for four-state component

$$
\begin{aligned}
\lambda 1 + \lambda 4 + \lambda 5 &= \lambda s, \\
\lambda 4 &= \lambda 6 = \lambda 3, \\
\lambda 2 &= \lambda 5, \\
\lambda 1 : \lambda 4 : \lambda 5 &= 1 : 4 : 5, \\
\mu 1 + \mu 2 + \mu 3 &= \mu s, \\
\mu 1 : \mu 2 : \mu 3 &= 1 : 3 : 6.
\end{aligned}
\tag{3}
$$

Suppose that at any time t, the interval between two consecutive time slices is Δt. Then, the transition relationships between nodes of the network without repair, with perfect repair, and imperfect repair are present in Tables 1–3, respectively, (Kohda and Cui, 2007).

Conditional dependencies between variables will be assigned to conditional probability tables (CPTs). In a DBN having n parents and m states, to determine the CPT for each parent node, it is necessary to define n<sup>m</sup> independent parameters. When n is large, traditional models of OR-gate and AND-gate are used to quantify relationships in series and parallel systems. Suppose that for node A, there are n parent nodes X1, X2, Xn, and the degradation probability of node i is P<sub>i</sub>. The unreliability of an AND-gate can therefore be calculated by the expression as follows (Cai et al., 2013):

$$P\left(A \mid X_1, X_1, \dots, X_1\right) = \prod_{1 < i < n} P_i.\tag{9}$$

In the case where the parent nodes are in parallel, the unreliability of an OR-gate can be calculated by the expression as follows (Cai et al., 2013):

$$P\left(A \mid X_1, X_1, \dots, X_1\right) = 1 - \prod_{1 < i < n} \left(1 - P_i\right).\tag{10}$$

Table 1
Transition relations between states without repair


Table 2
Transition relations between states with perfect repair


Table 3
Transition relations between states with imperfect repair


## Industrial application

## System description

Figure 3 illustrates the production line of soft drinks of Atlas Bottling Corporation (Pepsi) company in Algeria. The production process begins with the dumping of preforms into a large bin that will put them one by one on an air conveyor and then transferred to the blower machine. This latter, through a feeding system, will blow the predisposed preforms in different molds to give them bottle shape. The new bottles go to the filling machine for rinsing, filling the finished product (soft drinks) and capping. The soft drinks preparation is done at the pre-mixer level. To check the poorly filled bottles, at the exit of the filling machine, we found a light checking system. After capping and checking the production, the bottles through a belt conveyor will be transferred to the labeller, then to the dater, the packing machine followed by the palletizer to be labelled, dated, packaged, put on the pallets and finally stocked.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Production process of soft drink manufacturing (Adjerid et al., 2012)

In this work, we are interested in the blower which is a complex system, it is mainly composed of different subsystems with functional dependencies as shown in (Figure 4). This machine requires precise conditions to provide a quality product. Changing a single parameter can cause a high discard rate and delay the production rate of the entire line.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Decomposition of the blower

In many research areas, DBN receive considerably increased attention in the reliability assessment and analysis field. The results obtained by applying this method show its effectiveness and its use in the context of a performance evaluation, forward, and backward analysis (Cai et al., 2013; Li et al., 2018; Adjerid et al., 2012). Compared with conventional methods, DBN reduces the calculations and provides more impressive results (Li et al., 2018). Referring to (Adjerid et al., 2012), a DBN approach was used to evaluate the reliability of the blower and studied the effect of different maintenance strategies. Usually, the behaviour of any degraded system is related to the multistate of their subsystems and any degradation can lead to a decrease in system performances. In this work, to study and analysis more accurately the blower performances, a quantitative method based on DBN is proposed. The objective is to model and evaluate the reliability and the availability of a blower system as a multistate system, identify the subsystems most contributing to the blower's failure and measure the impact of different maintenance strategies during future missions.

Each subsystem has four states: a perfect operating state, two degraded operating states ( $D S 1, D S 2$ ) and a failure state. In this study, two modes of repair are taken into account: perfect and imperfect reparations.

Table 4
Parameters of the Blower subsystems (per hour)


By exploiting the blower data obtained from the historical failure/maintenance database in the period of (2018-2020) and using the experience feedback of maintenance engineers, the failure rates, repair rates, and the degradation probabilities (\%) of blower subsystems are presented in Table 4. For each subsystem, the failure and repair rates are calculated using the following equations:

$$
\begin{aligned}
& \lambda=\frac{1}{M T B F} \\
& \mu=\frac{1}{M T T R}
\end{aligned}
$$

where the $M T B F$ and $M T T R$ are the mean time between failure and mean time to repair, respectively. The selection of values of the degradation states 1 and 2 of the system is estimated by using the historical results of the fault diagnostic, and analysis as well as the experience feedback.

The degradation state $D S 1=5 \%$ for the component furnace means that when the furnace is at the degraded state1, the failure probability of the dependent subsystems (which is the chucks subsystem) because of furnace failure is 0.05 .

The architecture of Figure 6 represents the evolution of each subsystem with time, the black arc represents the temporal evolution, whereas the functional dependence is represented by an orange arc. The evolution of the degradation model of the blowing wheel subsystem is conditioned by the degradation function of their functional dependencies which are the Cooling System (CS) and the Compression Air System (CA).

The architecture of the equivalent DBN model was developed using the GeNIe graphical interface software, taking into account the different states of each node and their functional dependence as illustrated in (Figure 7).

## Reliability and availability

Over time, failures can occur at any time either minor or major. Take the example of the chucks element (Figure 5), failure rates and repair rates between the states of each node can be calculated using equations (3)-(8). Subsequently, the transition relationships between consecutive nodes in all three cases can be calculated using tables 1-3. The reliability and availability of the chucks subsystem node are determined, as shown in (Figure 8).
![img-4.jpeg](img-4.jpeg)

Fig. 5. DBN of the chucks subsystem

By using the equation (11) and (12), the CPT for series and parallel system can be calculated. From Table 4, the degradation probability of the Furnace and the Chucks are:

$$
\begin{aligned}
& P(\text { chucks subsystem }=\text { fault } \mid \text { Chucks }=\text { DS1 })=4 \%, \\
& P(\text { chucks subsystem }=\text { fault } \mid \text { Chucks }=\text { DS2 })=7.5 \%, \\
& P(\text { chucks subsystem }=\text { fault } \mid \text { Furnace }=\text { DS1 })=5 \%, \\
& P(\text { chucks subsystem }=\text { fault } \mid \text { Furnace }=\text { DS2 })=8 \%
\end{aligned}
$$

![img-5.jpeg](img-5.jpeg)

Fig. 6. Proposed model of the global system with functional dependencies from $t$ to $t+\Delta t$
![img-6.jpeg](img-6.jpeg)

Fig. 7. DBN of global system
![img-7.jpeg](img-7.jpeg)

Fig. 8. The Reliability and Availability of the "chucks" subsystem

One of chucks and furnace can cause the failure of chucks subsystem, which means that there are $n=2$ nodes and each node has $m=4$ states, therefor, the CPT have $m^{n}=16$ nodes.

For example, using equation (10), the degradation probability

$$
\begin{aligned}
P\left(\text { chucks subsystem }=\text { fault } \left\lvert\, \begin{aligned}
\text { Chucks } & =\text { DS1, } \\
\text { Furnace } & =\text { DS1 } \\
& =0.088 .
\end{aligned}\right.\right.
\end{aligned}
$$

The CPT of this subsystem is shown in Table 5.
As Figure 8 indicates, it is obvious that as time progresses, the dynamic reliability decreases to almost 0 in about 550 hours. With repair, the availability of chucks decreases, in the case of a perfect repair, it reaches a value of about $71.13 \%$ in 450 hours. When imperfect repair is considered, it reaches a value of $70 \%$ in about 450 hours. It can be seen that perfect and imperfect repair can improve the performances of the Chucks subsystem, but the imperfect repair does not significantly affect availability compared to perfect repair.

## Results and discussion

## DBN for the global system

In the same way, we can build the overall system network, study the influence of subsystems on the blower's state and measure the impact of both repair strategies on overall performances. Figure 9 shows the global DBN extended over time without repair. Each node initially is in a perfect functioning state (perfect $=100 \%$ ), over time, the degradation begins. According to the failure rate, repair rate, and functional dependencies, the probabilities of each subsystem evolve differently from the other. For the blower, two modalities are chosen, namely, Normal and Fault.

The performance evaluation of the blower is examined using DBN, the evolution of reliability and availability with respect to a perfect and imperfect repair are represented in Figure 10. As mentioned, over time, reliability and availability decrease. The reliability drops to about 0 in 400 hours and the availability reaches the values of 0.42 and 0.37 in 650 h with per-

Table 5
CPT of chucks


![img-8.jpeg](img-8.jpeg)

Fig. 9. Extended DBN of Blower over time

![img-9.jpeg](img-9.jpeg)

Fig. 10. Reliability and Availability of Blower

fect repair and imperfect repair, respectively. Clearly, the availability with perfect and imperfect repairs is evolving almost identically. Based on these results, it has been noted that perfect and imperfect repairs can significantly improve the Blower performances, while imperfect repair compared to perfect repair does not degrade performance significantly.

### Diagnostic inference

The application of the diagnostic inference method (backward analysis) is used to determine the causes that have a significant impact on the failure of the top event (Kohda and Cui, 2007). By adopting this method in the inference of the DBN model. The new belief over the entire network will be reflected, as a result, critical subsystems are quickly identified and the posterior probabilities of each event at different time slices can be calculated. So, it can provide a useful information about the necessary preventive measures that could be taken to prevent the risk of blower failure.

The prior and posterior probabilities of the basic events at T = 100 h are determined, as shown in Figure 11. It is noted that the subsystems: "Chucks (C)", "Furnace (F)", "Blowing Wheel (B)" and "PLC" are the most influential factors leading to blower failure because they have the highest increasing probability.

ties and significant posterior probabilities. Therefore, based on diagnosis results, more attention should be paid to these subsystems to further reduce the risk of failure.

![img-10.jpeg](img-10.jpeg)

Fig. 11. Comparison between posterior and prior probabilities for basic events at T = 100 h

### Sensitivity analysis

In this study, a sensitivity analysis must be carried out to ensure its robustness and to prove that this model is a reasonable representation. If the obtained result sensitive i.e. it will not show abrupt variations in case of a minor change in input parameters, then the model is robust (Li et al., 2019), (Cai et al., 2013). It is assumed that the failure rates of critical subsystems are subject to a variation of ±10%. The effects of these variations on the probability of system failure are shown in (Figure 12).

In this figure, when the failure rate of the Chucks subsystem is increased to 110%, the probability of blower failure increased from 42.36% to 43.55%.

When increasing the failure rate of both subsystems Chucks and Furnace to 110%, the probability of blower failure increased from 43.55% to 44.06%. When the failure rates of critical subsystems Chucks, Furnace and Wheels were increased to 110%, the probability of blower failure increased from 44.06% to 44.39%. In addition, by increasing the failure rate of subsystems Chucks, Furnace, Wheels, and PLC to 110%, the probability of blower failure increased from 44.39% to 44.65%.

Reducing failure rates of critical subsystems will reduce the failure probability of the top event in the same way. As expected, in this case, a slight modification in the failure rate for critical subsystems induces the probability of blower failure logically and reasonably, thus giving a validation of this model.

![img-11.jpeg](img-11.jpeg)

Fig. 12. The effect of changes in failure rate of critical subsystem on the probability of blower failure

### Conclusion

In this article, unlike previous studies in maintenance evaluation and optimization field, a methodology based on DBN was proposed to model and evaluate the performance measurements (reliability and availability) of a multi-state system, different repair strategies are taken into account. A real case of a blower is analyzed to show how this approach can be effectively manipulated to resolve several problems concerning: the identification of influencing factors (diagnosis), the analysis of the relationship between system components, predictive evaluation of the dynamic failure probabilities, and measuring the effect of maintenance strategies on system reliability and availability. The main conclusions of this study can be summarized as follows:

- Dynamic analysis indicates that the repair improves the performance of the blower, while an imperfect repair does not significantly degrade performance compared to the perfect repair.

- Diagnostic inference of blower's critical subsystems including Chucks, Furnace, Wheels, and PLC are identified as contributors leading to blower failure. Based on diagnosis, we should pay more attention to these subsystems to further reduce the risk of system failure.
- In order to improve the performance of the system, preventive measures are necessary to reduce as much as possible the failure rate of critical events. As a recommendation, some measures could be taken, which are; a systematic overhaul for the chucks accessories and the loading/unloading wheels is necessary, develop a detailed maintenance plan for the Furnace subsystem to maintain the correct temperature.
- The analysis results obtained in this study can be provided as a decision support tool and a very useful information base. Moreover, this model can serve engineers to plan maintenance interventions optimally.
- Sensitivity analysis allows us to validate and show that the model is correct and rational.

