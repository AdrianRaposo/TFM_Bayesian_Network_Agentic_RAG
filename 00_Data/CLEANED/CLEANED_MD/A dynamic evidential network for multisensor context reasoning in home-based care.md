# A Dynamic Evidential Network for Multisensor Context Reasoning in Home-based Care 

Hyun Lee<br>Computer Science and Engineering<br>University of Texas at Arlington<br>Arlington, TX, 76019, USA<br>hlee@mavs.uta.edu

Jae Sung Choi<br>Computer Science and Engineering<br>University of Texas at Arlington<br>Arlington, TX, 76019, USA<br>jschoi@uta.edu

Ramez Elmasri<br>Computer Science and Engineering<br>University of Texas at Arlington<br>Arlington, TX, 76019, USA<br>elmasri@uta.edu


#### Abstract

In home-based care, reliable contextual information of remotely monitored patients should be generated to recognize activities and to identify hazardous situations of the patient. This is difficult for several reasons. First, low level data obtained from multisensor have different degrees of uncertainty. Second, generated contexts can be conflicting even if they are acquired by simultaneous operations. And last, context reasoning over time is difficult for temporal changes in sensory information. In this paper, we propose the dynamic evidential fusion approach as a context reasoning method in home-based care. The proposed approach processes the generated contexts with Dynamic Evidential Network (DEN), which is composed of the combination of DezertSmarandache Theory (DSmT) and Markov Chain (MC). The DSmT reduces ambiguous or conflicting contextual information and the MC processes the association and correlation of sensory information that may change based on time series. Finally, we compare the dynamic evidential fusion approach with the static evidential fusion approach for analyzing the improvement of the dynamic evidential fusion approach.


Index Terms-Sensor data fusion, Dynamic Evidential Network, Context Reasoning, DSmT, Markov Chain

## I. INTRODUCTION

A Pervasive Healthcare Monitoring System (PHMS) enables continuous healthcare monitoring [7] with the help of heterogeneous multisensor. A key approach of the PHMS is that reliable contextual information should be generated to recognize correct activities and to identify hazardous situations of the patient [15], [11]. However, a higher confidence level in the generated contexts is difficult to produce. First, inaccurate sensor readings, which have different degrees of uncertainty, can produce misunderstandings for recognizing activities that lead to incorrect services to the patient. Second, contextual information is more ambiguous if data obtained from multisensor are corrupted or conflicted. And last, context reasoning over time is difficult for temporal changes in sensory information. To solve these problems, we proposed the static evidential fusion approach based on Dezert-Smarandache Theory (DSmT) as a context reasoning method in [8]. The DSmT reduces ambiguous or conflicting contextual information using a consensus method such as Proportional Conflict Redistribution No. 5 (PCR5) combination rule [12] and static weighting factors. However, the [8] did not consider the temporal changes in sensory information, which have the association and correlation of contextual information collected from multisensor. Not only
considering the state of contextual information based on time stamp but also considering the association and correlation of sensory information based on time series, which can make a better decision, are necessary for context reasoning. Therefore, we propose the dynamic evidential fusion approach based on time series. The proposed approach processes the generated contexts with Dynamic Evidential Network (DEN), which is composed of the combination of DSmT and Markov Chain (MC) [19]. The DSmT calculates the state-space dependency and the MC calculates the temporal dependency [9] with DEN. Thus, the DEN reasons over time then obtains a higher confidence level of contextual information. Finally, we compare the dynamic evidential fusion approach with the static evidential fusion approach for analyzing the improvement of the dynamic evidential fusion approach.

There are a number of methods available for sensor data fusion. Among sensor data fusion techniques, Bayesian methods (Bm) [1], [4], and Dempster-Shafer Theory (DST) [10], [22] are commonly used to handle the degree of uncertainty. As a generalized probabilistic approach, DST, which represents the ignorance [20] caused by the lack of information and aggregates the belief when new evidence is accumulated, have some distinct features when compared with Bm. However, the DST also has some limitations and weaknesses. When conflict becomes important between sources, the results of Dempsters combination rule has low confidences. Thus, we use the PCR5 combination rule [12], which overcomes drawbacks of Dempsters combination rule. To handle the temporal changes in sensory information, Hidden Markov Models (HMM) [2], [16], [21], Kalman Filtering Models (KFM) [5], [17], and Dynamic Bayesian Networks (DBN) [13], [23], [18] are used as a fusion technique. In terms of probabilistic networks, the DBN, which was proposed as a generalization of HMM, have some distinct features when compared with HMM or KFM, since it allows much more general graph structures. The DBN represents the hidden state in terms of a set of random variables when compared with HMM. The DBN allows general hybrid, nonlinear conditional probability densities (CPD) when compared with KFM. This is a useful feature to manage the causality between random variables as well as time series data. However, the DBN model is composed of interconnected two time slices of a static Bayesian network. We use the MC, which

![img-0.jpeg](img-0.jpeg)

Fig. 1. An example of a $1^{\text {st }}$ order MC
represents temporal and state links between two consecutive time slices.

The rest of the paper is organized as follow. In section II, the basics of evidence theories are introduced. We explain the static evidential fusion approach in section III. We propose the dynamic evidential fusion approach as a context reasoning in section IV. A case study is performed to compare two evidential fusion approaches in section V. We then conclude the paper in section VI.

## II. Basics on DSMT and Markov Chain

## A. Basis of $D S m T$

An evidential theory allows us to better quantify uncertainty. The set, denoted by $\Theta$, is called the frame of discernment of the sensor. The basic idea of DSmT is to consider all elements of $\Theta$ as not precisely defined and separated, so that no refinement of $\Theta$ into a new finer set $\Theta^{* r f}$ of disjoint hypotheses is possible in general, unless some integrity constraints are truly known and in such case they will be included in the DSm model of the frame. Shafer's model [6] assumes $\Theta$ to be truly exclusive and appears only as a special case of DSm hybrid model in DSmT. The hyper-power set, denoted $D^{\Theta}$, is defined by the rules 1,2 , and 3 without additional assumption on $\Theta$ but the exhaustivity of its elements in DSmT.

1) $\emptyset, \theta_{1}, \cdots, \theta_{n} \in D^{\Theta}$.
2) If $\theta_{1}, \theta_{2} \in D^{\Theta}$, then $\theta_{1} \cap \theta_{2}$ and $\theta_{1} \cup \theta_{2}$ belong to $D^{\Theta}$.
3) No other elements belong to $D^{\Theta}$, except those obtained by using rules 1) or 2).

In evidential theory, a range of probability rather than a single probabilistic number is used to represent uncertainty of the sensor. The lower and upper bounds of the probability are called the Belief (Bel) and Plausibility (Pl) respectively. Thus, Bel and $P l$ of any proposition $X \in G^{\Theta}$ are defined as:

$$
\operatorname{Bel}(X) \triangleq \sum_{\substack{Y \subseteq X \\ Y \in G^{\Theta}}} m(Y) \quad \text { and } \quad P l(X) \triangleq \sum_{\substack{Y \cap X=\emptyset \\ Y \in G^{\Theta}}} m(Y)
$$

Based on eq. (1), Bel shows the degree of belief to which the evidence supports $X$. Whereas $P l$ shows the degree of belief to which the evidence fails to refute $X$.

For inferring actities along evidential networks, evidential operations [8] are performed then belief distributions on frame can be combined by several independent sources of evidence using PCR5 rule. This rule is mainly based on the conjunctive consensus operator defined for two-sources cases by:

$$
m_{12}(X)=\sum_{\substack{X_{1}, X_{2} \in G^{\Theta} \\ X_{1} \cap X_{2}=X}} m_{1}\left(X_{1}\right) m_{2}\left(X_{2}\right)
$$

The total conflicting mass drawn from two sources, denoted $k_{12}$, is defined as:

$$
k_{12}=\sum_{\substack{X_{1}, X_{2} \in G^{\Theta} \\ X_{1} \cap X_{2}=\emptyset}} m_{1}\left(X_{1}\right) m_{2}\left(X_{2}\right)=\sum_{\substack{X_{1}, X_{2} \in G^{\Theta} \\ X_{1} \cap X_{2}=\emptyset}} m\left(X_{1} \cap X_{2}\right)
$$

Based on eq. (3), we know that the total conflicting mass is the sum of partial conflicting masses. If $k_{12}$ is close to 1 , two sources are almost in total conflict. Whereas if $k_{12}$ is close to 0 , two sources are not in conflict.

## B. PCR5 Combination Rule

In DSmT, PCR5 redistributes the partial conflicting mass only to the elements involved in that partial conflict. First, it calculates the conjunctive rule of the belief masses of sources. Second, it calculates the total or partial conflicting masses. And last, it redistributes the conflicting masses proportionally to non-empty sets involved in the model according to all integrity constraints.

PCR5 combination rule for two sources is defined in [3]: $m_{P C R 5}(\emptyset)=0$ and $\forall(X \neq \emptyset) \in G^{\Theta}$

$$
\begin{aligned}
& m_{P C R 5}(X)=m_{12}(X)+ \\
& \quad \sum_{\substack{Y \in G^{\Theta} \backslash\{X\} \\
c(X \cap Y)=\emptyset}}\left[\frac{m_{1}(X)^{2} m_{2}(Y)}{m_{1}(X)+m_{2}(Y)}+\frac{m_{2}(X)^{2} m_{1}(Y)}{m_{2}(X)+m_{1}(Y)}\right]
\end{aligned}
$$

where $m_{12}$ is defined by eq. (2) and all denominators such as $m_{1}(X)+m_{2}(Y)$ and $m_{2}(X)+m_{1}(Y)$ differ from zero (0).

## C. Markov Chain (MC)

The MC is a mathematical model for stochastic systems whose states (discrete or continuous) are governed by a transition probability. This is a sequence of random variables $X_{1}, X_{2}, X_{3}, \ldots$ with the Markov property, given the present state, the future and past states are independent. The possible values of $X_{i}$ form a countable set $S$ called the state space of the chain. The MC is often described by a directed graph, where the edges are labeled by the probabilities of going from one state to the other states. Formally, Fig. 1 shows an example of a $1^{\text {st }}$ order MC. In this paper, a finite state machine [14] can be used as a representation of a MC as shown in Fig. 3.

## III. Static Evidential Fusion Approach

## A. Characteristics of Sensors

Multisensor such as medical body sensors, RFID devices, environmental sensors and actuators, and location sensors are used in a PHMS [7]. These sensors are operated by pre-defined rules or learning processes of the expert systems, and often have thresholds to represent the emergency situation of the patient or to operate actuators. Each sensor can be represented by an evidential form such as 1 (active) and 0 (inactive) based on the pre-defined threshold. Whenever the state of a certain context associated with a sensor is changed, the value of a sensor can change from 0 to 1 or from 1 to 0 . Hence we simply express the status of each sensor as a frame:
$\Theta=\left\{\right.$ Threshold $_{\text {over }}$, Threshold $_{\text {not-over }}\}=\{1,0\}$.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Static Evidential Network

## B. Context Reasoning based on Static Evidential Network

We utilize context concepts defined in [8] to make a statespace based context modeling with an evidential form. We define the quality of data to represent static weighting factors of the selected data within the given time and location. It consists of a hierarchical relationship between sensors, related context (attribute and state), and relevant activities within a region of the patient as shown in Fig. 2.

All possible values and their combination values of sensors can be represented by evidential forms which are either active (1) or inactive (0). This evidential form can make an evidential network. Context reasoning is performed to achieve a high confidence level of contextual information using a static evidential network. A context attribute consists of binary values of multisensor. The binary values are determined by the predefined threshold controlled by the expert system. Each context attribute has a discounting factor (error rate) depending on the technical limitations of sensors or noise. A context state consists of context attributes having an active (1) value. We apply a multi-valued mapping into the related context state to calculate the relationships among context attributes. Each context state has different static weighting factors. These static weighting factors help to make an activity using an evidential mapping among context states. Finally, we obtain a consensus using a combination rule then infer the situation of the patient by calculating the belief and uncertainty levels.

## IV. Dynamic Evidential Fusion Approach

## A. State-Markov Model

As mentioned in section I, the contextual information of the patient has the association or correlation based on time series. To deal with context reasoning over time, each contextual information of the patient is defined as one of the four states: 1) Initial State (Empty), 2) Recognition State (Identification), 3) Uncertain State (Ambiguity), and 4) Hazardous State (Emergency) as shown in Fig. 3.

The transition probabilities (the association and correlation) between each state, which utilizes environmental (E) sensors and medical body sensors (M), are defined as:
![img-2.jpeg](img-2.jpeg)

Fig. 3. Four State-Markov Model to represent current contextual information
$a_{00}$ : No sensor activation
$a_{01}$ : Only E-sensors activation
$a_{02}$ : Some E- and M-sensors activation
$a_{03}$ : All E- and M-sensors activation
$a_{10}$ : All E-sensors deactivation
$a_{11}$ : Only E-sensors activation continuously
$a_{12}$ : Some E-sensors deactivation and M-sensors activation
$a_{13}$ : All M-sensors activation
$a_{20}$ : All E- and M-sensors deactivation
$a_{21}$ : All M-sensors deactivation
$a_{22}$ : Some E- and M-sensors activation continuously
$a_{23}$ : All M-sensors activation
$a_{30}$ : All E- and M-sensors deactivation
$a_{31}$ : Only M-sensors deactivation
$a_{32}$ : Some E- and M-sensors deactivation
$a_{33}$ : All E- and M-sensors activation continuously

## B. Dynamic Evidential Network

The DEN is a Static Evidential Network (SEN) including a temporal dimension as shown in Fig. 4. This new dimension is managed by time-indexed states. The state, denoted by $X_{t}$, is represented at time step $t$ by a state $X$ with the aggregation of the belief mass assigned to a finite number of focal elements $X_{t}:\left\{m\left(S_{0}^{t}\right), m S\left({ }_{1}^{t}\right), m\left(S_{2}^{t}\right), m\left(S_{3}^{t}\right)\right\}$. In this case, $m\left(S_{0}^{t}\right)$ denotes the belief mass assigned to the focal element $S_{0}$ at time step $t$. Several time-indexed states are represented by the belief mass distribution of four states relative to the time slice $t$. An arc linking two states belonging to different time slices represents a temporal change of the belief mass and models the dependence between these states. Thus, the DEN allows to model random states as shown in Fig. 5. Defining these impacts as transition-belief masses between the focal elements of the state at time step $t$ and those at time step $t+1$ leads to the definition of the association and correlation of the state relative to inter-time slices, as it is defined as:

$$
\begin{aligned}
M( & \left.\left.X_{t+1} \mid X_{t}\right)=\right. \\
& \left.\left(\left\{m\left(S_{0}^{t+1}\right), m\left(S_{1}^{t+1}\right), m\left(S_{2}^{t+1}\right), m\left(S_{3}^{t+1}\right)\right\}\right)\right] \\
& \left(\left\{m\left(S_{0}^{t}\right), m\left(S_{1}^{t}\right), m\left(S_{2}^{t}\right), m\left(S_{3}^{t}\right)\right\}\right)
\end{aligned}
$$

The state in the first time slice do not have any parameters associated conditional probability distribution in Fig. 5. It is possible to compute the belief mass distribution of any state

![img-3.jpeg](img-3.jpeg)

Fig. 4. A Dynamic Evidential Network, which is a Static Evidential Network including temporal dimension
$X_{i}$ at time step $t$ corresponding to the activated sensors at time step $t$. The belief mass distribution at time step $t+1$ is computed using the activated sensors at time step $t+1$. So, the DEN with only two time slices and arcs between two states is defined. Two states are such rotated that the old state is dropped and the new state is used as time progresses. The arcs between two states are from left to right, reflecting the temporal link (the association and correlation) between two consecutive time slices. We only consider discrete-time stochastic processes, so we increase the index $t$ by one every time a new observation (sensory information) arrives.

## C. Context Reasoning based on Dynamic Evidential Network

To make a context reasoning over time based on DEN, we first apply a static evidential fusion process then calculate the association and correlation of two states based on consecutive time slices using the MC as shown in Fig. 3. Ideally, four states: $\left\{S_{0}, S_{1}, S_{2}, S_{3}\right\}$ can be recognized directly by the belief mass distribution of the activated sensors. However, in practice, four states have different belief mass distributions based on time series. We should compare two consecutive time slices, which indicates two cases: 1) same belief mass distribution between time step $t$ and time step $t+1$ and 2) different belief mass distribution between time step $t$ and time step $t+1$.

In 1) case, we estimate that the time-indexed states have no sensor reading errors. We can easily make a decision based on the static fusion process. However, in 2) case, we can estimate that one of time-indexed states between two consecutive states $\left(\left(X_{t}\right)\right.$ or $\left.\left(X_{t+1}\right)\right)$ has sensor reading errors or new sensor activation occurs in time step $t+1$. Thus, we calculate the belief mass distribution at time step $t+2$ then compare it with that at time step $t+1$. If the result of the state at time step $t+2$ is equal to that at time step $t+1$, this case is same as 1) case. Whereas this case is same as 2) case, recursively. After all, we can make a decision based on the dynamic fusion process.
![img-4.jpeg](img-4.jpeg)

Fig. 5. A DEN made of two consecutive random states $X$

## V. A CASE Study

## A. Applied Scenario and Assumptions

Many ambiguous situations can happen in home-based care. However, we simply assume that the state of the patient with two hypotheses. One hypothesis is the "Identification (I)" and the other is the "Emergency (E)". The corresponding frame of discernment is then described by: $\Theta=\{(I),(E)\}$. The set of focal elements is defined by:

$$
\begin{aligned}
D^{\Theta} & =\{\{(I)\},\{(E)\},\{(I \cap E)\},\{(I \cup E)\}\} \\
& =\left\{\left\{S_{1}\right\},\left\{S_{3}\right\},\left\{S_{0}\right\},\left\{S_{2}\right\}\right\}, \text { respectively }
\end{aligned}
$$

In DSmT, the constraint $m\left(S_{0}\right)=0$ is assumed and the role of $S_{2}$ is to characterize the ignorance [20], which is an epistemic uncertainty, on the real probability distribution over the state. When $\underline{P}_{E}$ is the lower probability of the hypothesis $S_{3}(E)$ and $\bar{P}_{E}$ is the corresponding upper probability, the lower and upper bounds of the reliability $\left(\underline{P}_{E}, \bar{P}_{E}\right)$ are easily translated to define the belief mass assignment of $S_{3}(E)$ :

$$
\begin{aligned}
& m\left(S_{3}\right)=\underline{P}_{E} \\
& m\left(S_{1}\right)=1-\bar{P}_{E} \\
& m\left(S_{2}\right)=\bar{P}_{E}-\underline{P}_{E}
\end{aligned}
$$

To make this scenario, we utilize environmental sensors (the lighting sensor and the heating sensor of the living room), location sensors (the pressure sensor attached on the sofa), and medical body sensors (i.e., blood pressure, body temperature, and respiratory rate). Multisensor have thresholds and their operations can be represented by evidential forms. Based on this simplified scenario, we can derive a static evidential fusion process based on SEN as shown in Fig. 6. We can then calculate the belief and uncertainty levels. To calculate the belief and uncertainty levels, we assume that a discounting rate (error rate) and a static weighting factor of each sensor are fixed. For example, a discounting rate of the environmental sensors, the location sensors, and the medical body sensors are $0.3,0.2$, and 0.1 , respectively. A static weighting factor of the pressure sensor, the location sensor, the motion sensor, the blood pressure sensor, the body temperature sensor, and the respiratory rate sensor are $0.7,0.2,0.1,0.2,0.3$, and 0.5 , respectively.

![img-5.jpeg](img-5.jpeg)

Fig. 6. An example of the Static Evidential Network (SEN) for inferring the contextual Information $\left(S_{0}, S_{1}, S_{2}, S_{3}\right)$ of the patient

## B. Static Evidential Fusion Process

As described in [8], we can make a context reasoning based on SEN using a static evidential fusion process. First, we represent the evidence on each sensor as a mass function. Second, we apply a discounting factor (error rate) to each sensor to obtain sensor's credibility. Third, we apply multivalued mappings, which represent the relationships between sensors and associated objects by translating mass functions, for making context attributes. Fourth, context attributes are aggregated then translated to the related context states using multi-valued mappings. Fifth, we apply different static weighting factors to each context state then sum up context states using evidential mappings. Sixth, we apply the PCR5 rule to achieve the conjunctive consensus with the conflict mass then redistribute the partial conflicting mass. Finally, we calculate the belief and uncertainty levels (ignorance) using the belief mass. The results are shown in Fig. 7.

According to Fig. 7, the belief level $\left(m\left(S_{3}\right)\right)$ of the (E) situation are increased based on the number of the activated sensors. However, the belief level of (A) (i.e., the activation of the location sensor and the respiratory sensor) is bigger than that of (B) (i.e., the activation of the environmental sensors and the body temperature sensor) even if the number of the activated sensors of (A) is smaller than that of (B), since the applied weighting factor of (A) is bigger than that of (B). Thus, we can know that the number of the activated sensors and the weighting factor are concurrently important factors for inferring the correct situation of the patient. However, it is difficult to find sensor reading errors. So, we consider the dynamic evidential fusion process based on time series.

## C. Dynamic Evidential Fusion Process

As mentioned in section IV. (B and C), we can make a context reasoning over time based on DEN using a dynamic evidential fusion process. First, we measure the belief mass
![img-6.jpeg](img-6.jpeg)

Fig. 7. An example of the belief and uncertainty levels of "Emergency (E)" situation of the patient
distribution of the time-indexed state at time step $t$ and time step $t+1$ using the proposed static evidential fusion process. Second, we compare the belief mass distribution of two consecutive states at time step $t$ and $t+1$. And last, if the belief mass distribution of two consecutive states have different values, we compare the belief mass distribution of the next state at time step $t+2$ recursively until we make a decision based on the proposed rules: 1) No errors, 2) Sensor errors, and 3) New sensor activation.

According to Fig. 8, the temporal changes of the belief mass distribution between two consecutive random states $X$ occur based on time series, since new sensors may activate or sensor reading errors may happen. For example, in $A$ case, the degrees of the temporal change are a few and the time interval of the temporal change is bigger than that of the $B$ case. In this case, we can estimate that sensor reading errors may happen, since a few temporal change happens in sensory information. By the way, in $B$ case, the degrees of the temporal change is frequently happened and the temporal variation interval is smaller than that of the $A$ case. In this case, we can estimate that new sensors may activate then the situation of the patient will be changed or many sensors have wrong activations. This is a useful method to find sensor reading errors.

## D. Comparison and Analysis

Now, we can compare the DEN based on time series with the SEN based on time stamp. According to Fig. 9, the belief levels of the (E) situation based on time series have variations depending on the number of the activated sensors. We can make a context reasoning that the situation of the patient is the $\left(S_{1}\right)$ state at $C$ time intervals and the $\left(S_{3}\right)$ state at $E$ time intervals by comparing the belief mass distribution of two timeindexed states. In addition, we can estimate that sensor reading errors happen at $A, B$, and $F$ temporal point by comparing the belief mass distribution of three time-indexed states. This uncertainty can not be founded whenever we use the SEN. Moreover, the situation of the patient is the $\left(S_{2}\right)$ state at $D$ time intervals, since the temporal changes occurs frequently.

![img-7.jpeg](img-7.jpeg)

Fig. 8. An example of the temporal changes of the belief mass distribution between two consecutive random states $X$ based on time series

In this paper, we represent the belief levels of the patient's situation as the belief mass distribution $m\left(S_{3}\right)$. At $D$ time intervals, the belief levels $\left(m\left(S_{3}\right)\right)$ are increased depending on the time spent. Thus, we can make a context reasoning that the situation of the patient is close to the the $\left(S_{3}\right)$ state corresponding to the time spent. Therefore, we can say that some kinds of uncertainty, which are not solved with SEN, can be solved with DEN by considering the association and correlation of two consecutive random states based on time series. The DEN is a useful method to reason contexts over time when compared with the SEN.

## VI. CONCLUSION

In this paper, we utilize a dynamic evidential fusion approach as a context reasoning method to reduce the different degrees of uncertainty in sensed data and in generated contexts based on time series. The dynamic evidential fusion process consists of two parts: (1) DSmT and (2) MC. The DSmT resolves the conflicting contexts then the MC obtains a higher belief levels of contextual information with time variations based on DEN. Finally, we compare the DEN with the SEN to show the improvement of the reliability of contextual information in DEN.
