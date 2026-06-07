## Active and Dynamic Information Fusion for Multisensor Systems With Dynamic Bayesian Networks

Yongmian Zhang and Qiang Ji


#### Abstract

Many information fusion applications are often characterized by a high degree of complexity because: 1) data are often acquired from sensors of different modalities and with different degrees of uncertainty; 2) decisions must be made efficiently; and 3) the world situation evolves over time. To address these issues, we propose an information fusion framework based on dynamic Bayesian networks to provide active, dynamic, purposive and sufficing information fusion in order to arrive at a reliable conclusion with reasonable time and limited resources. The proposed framework is suited to applications where the decision must be made efficiently from dynamically available information of diverse and disparate sources.


Index Terms-Active sensing, Bayesian networks, information fusion.

## I. INTRODUCTION

There has been a great deal of interest in the development of systems capable of using many different sources of sensory information [1], [2]. Whatever the application may be, there is a need to systematically and efficiently interpret the large volume of information acquired from sensors of different modalities and with different degrees of uncertainty. Typically, many applications contain a large number of uncertain events interrelated by causes and effects. The question is how to systematically and efficiently represent and fuse uncertain information at different levels of abstraction.

The world situation is often dynamic and uncertain in nature and unfolds over time. To correctly assess and interpret the dynamic environment, a fusion system is needed that not only can systematically handle uncertain sensory data of different modalities but, more importantly, can reason over time. The inability of current sensor fusion systems to correlate and reason about a vast amount of information over time is an impediment to providing a coherent overview of the unfolding events. The question is, therefore, how to account for the temporal changes in sensory information.

Moreover, many applications are often constrained by limited time and resources. The usage of more sensors incurs more cost in acquiring information. It is important to avoid unnecessary or unproductive sensor actions and computations. Thus, we must select a subset of sensors that are the most decision-relevant. Now the question is how to determine a set of most informative information sources for the current goal with minimal cost at particular stage of information gathering to achieve an efficient and timely decision.

To address above issues, a fusion system therefore requires the capability which can not only represent the temporal changes of uncertain sensory information, but dynamically select the most relevant sensory data for a given goal at a given time as well. To achieve this, we propose to cast information fusion into a framework of dynamic Bayesian networks (DBNs) to account for the temporal aspect of decision making and uncertainty of knowledge, and to integrate and infer dynamic sensory information of different modalities. The fusion system is able to

Manuscript received December 21, 2004; revised April 17, 2005. This work was supported by a Grant from the U.S. Army Research Office under Grant DAAD19-01-1-0402. This paper was recommended by Associate Editor Isabelle Bloch.

The authors are with the Department of Electrical, Computer and System Engineering, Rensselaer Polytechnic Institute, Troy, NY 12180 USA (e-mail: jiqi@rpi.edu).

Digital Object Identifier 10.1109/TSMCB.2005.859081
actively select a subset of sensors to produce the most decision-relevant information with limited resources and in reasonable time. Additionally, DBNs enable sensor selection to dynamically adapt to varying situations.

Research in information fusion is getting wider and deeper nowadays. There are a number of methods available for sensor fusion including evidential reasoning [3], fuzzy theories [4]-[6], and neural networks [7], [8]. However, these methods lack the sufficient expressive power to handle uncertainties, dependencies and dynamics exhibited by sensory data in many applications. Bayesian networks (BNs), since their inception, have shown great promise in performing multisensor data fusion [1]. Recently, DBNs extend BNs for modeling dynamic events [9]-[13]. In the existing works, BNs and DBNs are primarily used for knowledge and uncertainty representation. DBNs were proposed as a generalization of hidden Markov models (HMMs) [14], but they allow much more general graph structures than an HMM does. It is therefore natural to consider a DBN as a basis of the general spatio-temporal sensor data analysis and interpretation.

Active sensing involves actively controlling sensors to optimize information gathering in a knowledge-based manner with an identifiable selection criterion rather than randomly selecting sensor parameters. A significant amount of research has been directed to the area of computer vision and robotics [15]-[19]. More recently, Oliver et al. [20] studied selective perception policies to purposively guide sensing and visual information processing to circumvent the computational burden associated with perceptual analysis. Pinz et al. [21] is the first to introduce active fusion in remote sensing image understanding. Paletta and Pinz proposed an active recognition system [22], where mutual information is used to quantify the ambiguity and to determine which view to select. Denzler and Brown [23] applied mutual information theory in the state estimation process for active camera parameter selection. Using HMMs and evidential reasoning to combine instantaneous and temporal visual information is recently studied in [24]. The notion of dynamically combining information provides useful hint to this work. A central problem of active information fusion is the sensor selection problem. There have been several attempts in sensor selection for target localization [25]-[28]. In theses works, they assumed that the system model is either a linear system or a standard stochastic model. Other works of interest for sensor selection can be found in the control literature. The work presented in [29] considers an Hidden Markov model with a number of sensors. The sensor sequence is determined via stochastic dynamic programming. The problem of optimal sensor selection for discrete-event systems under partial observation was studied in [30]. Since we use a DBN as an information fusion method, the above approaches of sensor selection can not directly be applied to our problem.

This paper aims to formalize a framework based on DBNs for active and dynamic information fusion, which is particularly suited to the applications where the decision must be made efficiently from dynamically available information of diverse and disparate sources. The remainder of this paper is organized as follows. We start with information fusion using DBNs in the next section. An active and dynamic information fusion framework is proposed in Section III. Section IV presents an example for a proof-of-concept. The final section is the conclusion.

## II. Information Fusion With BAYESIAN Networks

Information fusion is a process dealing with the association, correlation, and combination of information collected from various disparate sources into one coherent structure that can be used by a computer system to make a better decision than from single source only. In order

![img-0.jpeg](img-0.jpeg)

Fig. 1. Overview of a dynamic information fusion process in sequential decision-making for situation understanding. The figure shows that, if the certainty about the world situation is not sufficiently high, the additional information is requested by selecting a set of information sources. When knowing enough about the world situation, the decision-maker may make a decision about which course of action corresponding to that type of situation needs to be taken.
to accomplish this task, a fusion function $F$ must be used to combine these multiple sensor readings to a single output. Regardless of the fusion structure, the fusion process can be generally expressed as

$$
\Theta=F\left(S_{1}, S_{2}, \cdots, S_{n}\right)
$$

where $S_{i}$ denotes an individual sensor that gives a measurement; $\Theta$ is the output on which the decision-making is based. The choice of the fusion function $F$ depends on the chosen fusion methods. A review of information combination methods can be found in [31]. The fusion method in this effort is a dynamic probabilistic network; while the probabilistic inference is analogous to the fusion function $F$. The output $\Theta$ is the posterior probability of hypotheses that we want to infer. Fig. 1 outlines an active fusion process in sequential decision-making for situation understanding.

In terms of probabilistic networks, chain graphs have been explored to incorporate probabilistic reasoning for data analysis tools [32]-[34]. A chain graph is a probabilistic network model that mixes undirected and directed graphs to give a probabilistic representation. However, in order to represent the causality between random variables as well as time-series data, it is natural to use directed graphical models, which can capture the fact that one causes another as well as time flows forward. BNs or DBNs are ideal for representing directed graphs.

A Bayesian network is a graphical model representing probabilistic relationships among a set of variables to reflect an expert's understanding of the domain. A rigorous definition of Bayesian networks can be found in [35]. Here we develop the concept with just enough rigor and detail that will enable us to apply them to information fusion problems. A general definition of a BN, as shown in Fig. 2(a), is given as follows. Let $(\mathcal{E}, P)$ be a joint probability space with $\mathcal{E}=\mathcal{E}_{1} \times \cdots \times \mathcal{E}_{n}$, and joint probability $P$. Given a directed acyclic graph (DAG) of $G=(X, E)$ with $X=\left\{X_{1}, \cdots, X_{n}\right\}$ and arcs $E$, where $X_{i}$ is the projection onto $\mathcal{E}_{i}$. Let $\pi\left(X_{i}\right)$ be the parents of $X_{i}$ and $A\left(X_{i}\right)$ be the nondescendant of $\pi\left(X_{i}\right)$. Then $(G, P)$ is a Bayesian network if, for all $X_{i} \in X, X_{i}$ and $A\left(X_{i}\right)$ are independent given $\pi\left(X_{i}\right)$. The resulting joint probability over the random variables in the network can be expressed as

$$
P(X)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi\left(X_{i}\right)\right)
$$

Bayesian networks are valuable for several reasons. First, they enable to model the dependencies and uncertainties of the events and to handle incomplete data sets without difficulty because they discover dependencies among all variables. Second, domain knowledge can be described in a hierarchical graphical structure to represent different levels
![img-1.jpeg](img-1.jpeg)

Fig. 2. (a) Static Bayesian network (a directed acyclic graph), where $X_{1}-X_{6}$ are random variables. (b) A DBN is defined by "unrolling" the two-slice BN. Assume that the model is first-order Markov. The figure shows that $X_{1}, X_{2}$ and $X_{3}$ at current time $t$ are connected to their corresponding variables which determine the system at previous moment of time $t-1$.
of abstraction. Third, they provide a mathematically rigorous foundation for consistent, coherent and efficient reasoning.

BNs were initially not suited to modeling dynamic events. To circumvent this limitation, a new statistical approach from the perspective of BNs was proposed as a generalization of Kalman filtering models (KFMs) [36] and HMMs [37], namely, DBNs [14]. A DBN model is made up of interconnected two time slices of a static BN, and the transition of BN between the two consecutive time $t$ and $t+1$ satisfies the Markov process. Conventionally, it is assumed that a DBN is first-order Markov, and that temporal nodes ${ }^{1}$ at the current time $t$ are connected only to the corresponding nodes at the next time slice $t+1$. DBNs, however, can be extended by connecting a node at $t$ to any nodes at $t+1$ it may affect. However, such connections not only greatly complicate the network topology but also have limited utility since the impact of a node at $t$ on any nodes other than itself at $t+1$ are usually accounted for through the propagation of its influence on the corresponding node to the other nodes. Therefore, DBNs can be implemented by keeping in memory two slices at any one time, representing previous time slice and current time slice, respectively. The nodes in the first time slice do not have any parameters associated with them and they only determine the system at the previous moment of time; while each node from the second time slice has an associated conditional probability distribution. The two slices are such rotated that old slices are dropped and new slices are used as time progresses. The arcs between slices are from left to right, reflecting the temporal causality and they are parameterized by transitional probabilities. We only consider discrete-time stochastic processes, so we increase the index $t$ by one every time a new observation arrives. Fig. 2(b) shows an example of DBNs as given by the definition above. The joint distribution from the initial moment of time $(t=1)$ until the time boundary $(t=T)$ is then given by

$$
P\left(X_{1: T}\right)=\prod_{t=1}^{T} \prod_{i=1}^{n} P\left(X_{i}^{t} \mid \pi\left(X_{i}^{t}\right)\right)
$$

where $X_{i}^{t}$ is the $i^{\prime}$ th node at time $t ; \pi\left(X_{i}^{t}\right)$ stands for the parents of a node $X_{i}$ at time $t$, and they can either be in the same time slice or in the previous time slice. The difference between a DBN and an HMM is that a DBN represents the hidden state in terms of a set of random variables. By contrast, in an HMM, the state space consists of a single random variable. The difference between a DBN and a KFM is that a KFM requires all the conditional probability densities (CPDs) to be linearGaussian, whereas a DBN allows general hybrid, nonlinear CPDs. In addition, HMMs and KFMs have a restricted topology, whereas a DBN allows much more general graph structures. Therefore, it is natural to consider a DBN as a basis of the general spatio-temporal sensor data

[^0]
[^0]:    ${ }^{1}$ Temporal nodes represent variables that evolve over time.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Sensors are viewed as random variables and incorporated into a Bayesian network to form a coherent information fusion structure. For representing sensor uncertainties, a layer of information variables $\left\{I_{1}, \cdots, I_{m}\right\}$ is added into dynamic Bayesian networks to interface sensors and intermediate variables.
analysis and interpretation. A thorough work on DBN representation, inference and learning can be found in [13].

With the hypothesis and sensors, we can construct a coherent fusion structure with a Bayesian network as shown in Fig. 3. The root node of such a network would contain the hypothesis variable whose states corresponds to multiple hypotheses. The sensors occupy the lowest level nodes without any children. Sensors are the only observable variables in the model and evidences are gathered through sensors. In general a network will have a number of intermediate nodes that are interrelated by cause and effect. The hypothesis node is causally linked to the sensor nodes through these intermediate variables. The nodes and the links should reflect the causal structure and context independencies pertaining to the problem we are modeling.

In the real world, however, a fusion system may receive incorrect information from sensors for various reasons such as sensor noise, imprecise acquisition devices, and limitations of numerical reconstruction algorithms. If information is expert knowledge, experts also differ in their level of expertise. Therefore, sensor readings include uncertainties, which may diminish the reliability of a fusion system. There are a number of ways to represent uncertainty in sensory data [38]. Nevertheless, a probabilistic metric provides us with some consistency for information throughout the probabilistic graphical model. The uncertainty of sensor readings measures the degree of belief that the information provided by a sensor reflects the actual value. To be able to handle the uncertainty of sensor readings in the fusion structure with a probabilistic network, we may add an additional layer of variables which connects sensors to intermediate variables, namely information variables, as shown in Fig. 3. Conditional probabilities between information variables and sensors quantify the uncertainty of sensor measurements. Consequently, the uncertainty of sensor readings is incorporated into the fusion system to update the probability distribution over the hypothesis variable. Evidences regarding information variables are gathered through sensors and are fused through DBN inference. Temporal link between two consecutive time slices reflects the temporal causality. The time $t$ increases by one every time new sensor information arrives.

## III. Active and Dynamic Information Fusion

The objective of active information fusion is to selectively choose the most decision-relevant information while minimizing the cost associated with using the sensors for acquiring information. Overall efficiency can be achieved by aggregating only a subset of the most relevant sensor data to address the current goal. In other words, active fusion focuses on what is optimal rather than what is available.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Functional view of active information fusion, in which the fusion structure is a Bayesian network consisting of hypotheses $\Theta$, intermediate variables $X$, information variables $I$, and sensors $S$. The closed arrows represent the causality relations and the open arrows represent sensor activation control.

The problem of active fusion can be stated mathematically as follows. Assume that there are $m$ sensors $S_{i}, i=1, \cdots, m$ available that can be used to give measurements of the environment. Let $\Theta$ be a set of hypothesis $\theta_{k}, k=1, \cdots, K$. Let the sensors $\mathbf{S}=\left\{S_{1}, \cdots, S_{n}\right\}$ be a subset of sensors selected at time $t$, where $n \in\{1, \ldots, m\}$. The measurement of a sensor $S_{i}$ at time $t$ is denoted as $o_{t}\left(S_{i}\right)$, and $o_{t}\left(S_{i}\right)$ of the $i^{\prime}$ th sensor belongs to a known finite set of states $e_{1}^{(i)}, \ldots, e_{L}^{(i)}$. That is, the $i^{\prime}$ th sensor can yield one of $L$ possible measurements at a given time instant $t$. Let $O_{t}=\left\{o_{t}\left(S_{1}\right), \ldots, o_{t}\left(S_{n}\right)\right\}$ represent the information available at current time $t$ upon which the sensor selection is based at time $t+1$. The active information fusion generally proceeds in four stages at each time instant.
(1) Sensor Selection: based on the system state after receiving $O_{t}$, select an optimal subset of sensors $\mathbf{S}^{*}$ to be activated at the next time step $t+1$.
(2) Observation: get observation $o_{t+1}\left(S_{i}\right), i=1, \cdots, n$, to obtain new sensory information $O_{t+1}$, where $S_{i} \in \mathbf{S}^{*}$.
(3) State Estimation: compute the posterior probability $p\left(\Theta_{t+1} \mid O_{t+1}\right)$ by using DBN inference algorithms.
(4) Decision-making: make a decision if the certainty in the current solution is sufficiently high. Otherwise, start over and select sensors for further observations.
To determine a set of sensors to activate, it can only consider the probable outcomes of sensors. The actual outcomes of sensors can only be determined once the sensors are instantiated. Fig. 4 provides an architectural concept for the framework of active and dynamic information fusion. On the basis of this figure, the active control is to select a subset of sensors to be activated for the next time instant by only considering the probable outcomes of sensors (not physically invoked). The selected sensors have the greatest expected contribution to the uncertainty reduction (compared to their costs). The observed system is to physically invoke the selected sensors at time $t$, and generates sensory information $O_{t}$, the set of actual outcomes of selected sensors.

Acquiring information incurs cost such as operational cost, computational cost, etc. In a military context, the cost also includes the risk involved in information gathering. It is apparent that any quantitative analysis of information gain must account for the conflicting objective of sensor activation. Therefore, optimal sensor selection is to maximize a utility. In general, the utility function consists of two components: information gain $u_{1}$ and the cost $C(\mathbf{S})$ to activate sensors $\mathbf{S}$. We use $u_{2}=1-C(\mathbf{S})$ to convert the cost to the cost saving, which makes $u_{1}$ and $u_{2}$ in qualitative equivalence (both represents the benefit). Since

$u_{1}$ and $u_{2}$ are mutually utility independent [39], we can design a multilinear utility function as

$$
U\left(u_{1}, u_{2}\right)=\left(k_{1} u_{1}+1\right)\left(k_{2} u_{2}+1\right)
$$

where $k_{1}$ and $k_{2}$ are the preference parameters and $k_{1}+k_{2}=1 . u_{1}$ and $u_{2}$ need to be normalized in quantitative equivalence.

From the viewpoint of information theory, mutual information indeed measures the gain of an average amount of information before and after instantiating the selected sensors. Follow the notations in Fig. 4 and consider the process at certain time instant $t$. Notice that $t$ is dropped for notational clarity in the following equations. To obtain the mutual information, we shall start with the expected entropy of information. The expected entropy of hypothesis $\Theta$ with respect to all possible outcomes of a sensor $S_{i}$ measures how much uncertainty exists in $\Theta$ given $S_{i}$, is

$$
H(\Theta \mid S_{i})=-\sum_{S_{i}} \sum_{\Theta} P\left(\theta, s_{i}\right) \log P\left(\theta \mid s_{i}\right)
$$

where $s_{i}$ denotes the value taken by sensor $S_{i}$. If subtracting $H(\Theta \mid S_{i})$ from the original uncertainty in $\Theta$ prior to instantiating $S_{i}, H(\Theta)$, yield the amount of information about $\Theta$ that $S_{i}$ is capable of providing

$$
\begin{aligned}
I\left(\Theta ; S_{i}\right)= & H(\Theta)-H\left(\Theta \mid S_{i}\right) \\
= & -\sum_{\Theta} P(\theta) \log P(\theta) \\
& +\sum_{S_{i}}\left\{P\left(s_{i}\right) \sum_{\Theta} P\left(\theta \mid s_{i}\right) \log P\left(\theta \mid s_{i}\right)\right\} \\
= & \sum_{\Theta} \sum_{S_{i}} P\left(\theta, s_{i}\right) \log \frac{P\left(\theta \mid s_{i}\right)}{P(\theta)}
\end{aligned}
$$

where $I\left(\Theta ; S_{i}\right)$ also quantifies the total uncertainty-reducing potential of $S_{i}$ regarding $\Theta$. Then mutual information $I(\Theta ; \mathbf{S})$ for a sensor set $\mathbf{S}=\left\{S_{1}, \cdots, S_{n}\right\}$ may be written as

$$
\begin{aligned}
& I(\Theta ; \mathbf{S}) \\
& \quad=H(\Theta)-H(\Theta \mid \mathbf{S}) \\
& \quad=\sum_{\Theta} \sum_{S_{i} \cdots S_{n}}\left\{P\left(\theta, s_{1}, \cdots, s_{n}\right) \log \frac{P\left(\theta \mid s_{1}, \cdots, s_{n}\right)}{P(\theta)}\right\}
\end{aligned}
$$

where $P\left(\theta, s_{1}, \cdots, s_{n}\right)$ and $P\left(\theta \mid s_{1}, \cdots, s_{n}\right)$ at time $t$ can be directly obtained through DBN inference algorithms by considering the state of temporal variables at time $t-1$ and current sensor observations at time $t$.

Equation (7) provides a selection criterion in identifying the uncertainty reduction capability given a sensor set $\mathbf{S}$. Unfortunately, it is impractical to simply implement this criterion due to two difficulties when $n$ is large: 1) it requires time exponential in the number of summations to compute mutual information exactly and 2 ) it is infeasible to identify an optimal subset from a large number of information sources. This computational problem is beyond the scope of this present work as we focus on the principle and issues of active and dynamic information fusion. Now let $\mathcal{S}$ be entire space of sensor subsets and $\mathbf{S}^{*}$ be an optimal sensor subset. We then summarize a sequential decision process with the proposed framework as follows.

```
SEQUENTIAL-DECISION-PROCESS
    \(t \leftarrow 0\)
    \(2 \mathbf{S}^{*}=\arg \max _{\mathbf{S} \in \mathcal{S}} U(I(\Theta ; \mathbf{S}), C(\mathbf{S}))\)
    3 while \(t<T\)
4 Activate \(S_{i}\) for each \(S_{i} \in \mathbf{S}\) and get \(O_{t}\)
```

![img-4.jpeg](img-4.jpeg)

Fig. 5. DBN model for a conceptual IFF system to assist in the identification of aircraft. The transition between two neighboring time slices is modeled by first-order HMM. Assume that only the hypothesis nodes between two time slices are connected.

```
5 Perform DBN inference and obtain
\(P\left(\Theta \mid O_{t}\right)\)
6 if confidence is sufficiently high
7 make decision
8 else \(\mathbf{S}^{*}=\arg \max _{\mathbf{S} \in \mathcal{S}} U(I(\Theta ; \mathbf{S}), C(\mathbf{S}))\)
9 \(t \leftarrow t+1\)
```

A strategy of sensor selection needs to be implemented for lines 2 and 8 in the above procedure. Using the brute-force approach or greedy approach for sensor selection, we need to evaluate (7) when information theoretic criterion is used; this is feasible only for the problems with a small number of sensors and with a limited number of sensors being instantiated. To avoid the intractability of exact information computations, myopic is often used under the assumption that the decision maker will act after observing only one sensor. To correctly identify the cost-effective sensors, we should take into account the fact that the decision maker may instantiate more than one sensor before acting. One often used method for selecting multiple sensors at a time is the greedy approach, which greedily selects an ensemble of sensors iteratively until either the combined utility of the selected sensors peaks or when the maximum number of sensors is reached. While efficient, the greedy approach can not guarantee the optimality of the solution. A theoretic approach to the optimal and efficient sensor selection behind this framework is the focus of our current research. Our initial solution to efficiently compute (7) can be seen in [40]. Below, we use a brute-force approach to compute $I(\Theta ; \mathbf{S})$ and $U(\cdot)$ with a limited number of sensors being instantiated at each time.

## IV. EXAMPLE

To clarify the basic notions, we first experiment with a very simple example for a proof-of-concept. Suppose that a system of identification friend or foe (IFF) employs sensors including imaging sensors (e.g., FLIR, SAR), acoustic sensor, and radar sensor, etc., to identify characteristics of all known aircrafts. Fig. 5 presents a BN model for such a system. The most important identification features that best characterize a particular aircraft include length, span, wing and tail shape, speed, and engine sound, and they are provided by diverse sensors. For examples, to obtain the aircraft shape, we may activate the imaging sensors to determine the shape parameters of the aircraft; while we may

![img-5.jpeg](img-5.jpeg)

Fig. 6. (a) Comparison of entropy reduction between passive fusion and active fusion. Relative entropy = (H2 - H1)/H1, where H1 and H2 represent the entropy by active fusion and passive fusion, respectively. The error bar shows the lower and upper error ranges. (b) Comparison of utility between passive fusion and active fusion. The preference parameters k1 and k2 take 0.5 in (4). Relative utility = (C1 - C2)/C2, where C1 and C2 represent the utility by active fusion and passive fusion, respectively. The error bar shows the lower and upper error ranges.

**TABLE I**

**EXAMPLES OF SENSOR ACTION SEQUENCE WHERE SENSOR(S) ARE ACTIVELY SELECTED AT EACH TIME INSTANT**


The *Sensor Action Sequence Changes Due to the Change of Sensor Uncertainty*

utilize Sonar to obtain the aircraft speed. We assume that there are external modules which receive sensor data and make the data available as input evidence to the network. We shall select the most decision-relevant sensors in order to make a timely engagement decision.

We now specify the cost of individual sensors as [0.1667, 0.2667, 0.2000, 0.1333, 0.2333] for FLIR, SAR, Sonar, Radar, and Acoustic sensor, respectively. Fig. 6(b) shows the comparison result regarding the expected utility between active and passive fusion. For the convenience of comparison, we give the same sensors and sensor outcomes at the first time slice for both active fusion and passive fusion. Fig. 6(b) is the average relative utility of 20 sensor action sequences. As we initially expect, it shows that, on average, the sensors by active selection achieve greater utility than the sensors by passive selection.

Table I gives examples of different courses of sensor actions. In fact, we can see from Table I that the change of situation (here different sensor outcomes) results in different sensor action sequences. At each time instant, the number of sensors and which subset of sensors to be integrated are determined according to the state at that time as well as the evidence at previous time instant. Note that the certainty in Tables I and II is the information gain I(Θ; S). The larger the information gain, the more certainty there is.

The uncertainty of sensor readings also directly influences the sensor selection. To clarify this matter, we now change the uncertainty of sensor readings (probability distributions between information variables and sensors). Although, at the first time instant, the same sensor and sensor outcome in Table I are given, Table II shows that the course of sensor actions differs with that in Table I due to the change of the uncertainty of sensor readings.

**TABLE II**

**THE SENSOR ACTION SEQUENCE CHANGES DUE TO THE CHANGE OF SENSOR UNCERTAINTY**


In a dynamic environment, a decision is required across a fairly narrow space of time, and tasks are dependent on an ongoing, up-to-date analysis of the environment. If the same evidence is acquired sequentially, the evidence acquired at current time can reinforce the hypothesis made by the same information received at previous time. Although a static BN model can integrate all evidences available so far by sequentially propagating the impact of each evidence, the impact of previous evidence on subsequent integration can not be adjusted, and previous evidence can not be integrated into the same evidence currently received. DBNs, on the other hand, enable to correlate and associate the continual arriving evidences through temporal dependencies to perform reasoning over time. The information from previous time serves as prior information for current evidences, and they are combined with Bayesian statistics. Dempster-Shafer evidence theory [3] can also represent the uncertainty of information, but it lacks the ability to handle prior knowledge and temporal dependency.

### V. CONCLUSIONS

There are three important issues for a fusion system: 1) modeling uncertainties of sensory data; 2) modeling temporal change; and 3) active control and management of the fusion process. In this paper, we proposed a framework to simultaneously address the above three issues. Toward the first and the second issue, we adopt a dynamic Bayesian network as a fusion structure to provide a coherent and fully unified hierarchical probabilistic framework for representation, integration, and inference of uncertain sensory information of different modalities at different levels of abstraction, and to account for the temporal aspect of decision making. Toward the last issue, we need an efficient sensor selection method that allows a fusion system to actively select and invoke a subset of sensors that is the most decision-relevant.

It is impractical to simply implement information-theoretic criterion in (7) to identify an optimal sensor subset because (7) generally requires time exponential in the number of summations to compute mutual information exactly. In this paper, we mainly focus on the architectural concept and issues for active and dynamic information fusion rather than the efficient sensor selection methodology behind this framework. In many fusion applications, the relationships among the events are mostly unknown and they may vary as the world situation evolves. Therefore, a fusion system needs to incorporate a situation oriented learning mechanism. This is another issue that we will focus on in our future work.

### ACKNOWLEDGMENT

The authors gratefully acknowledge constructive comments from the anonymous reviewers that significantly improved the presentation of this paper.
