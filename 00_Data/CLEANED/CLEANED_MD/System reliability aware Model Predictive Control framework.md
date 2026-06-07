# System Reliability Aware Model Predictive Control Framework 

Jean C. Salazar ${ }^{\mathrm{a}, *}$, Philippe Weber ${ }^{\mathrm{b}}$, Fatiha Nejjari ${ }^{\mathrm{a}}$, Ramon Sarrate ${ }^{\mathrm{a}}$, Didier Theilliol ${ }^{\mathrm{b}}$<br>${ }^{a}$ Universitat Politècnica de Catalunya, Research Center for Supervision, Safety and Automatic Control (CS2AC), 10 Rambla Sant Nebridi, Terrassa, Spain<br>${ }^{\text {b }}$ Université de Lorraine, Centre de Recherche en Automatique de Nancy (CRAN), FST - B.P. 70239 54506 Vandoeuvre-lès-Nancy, France


#### Abstract

This work presents a Model Predictive Control (MPC) framework taking into account the usage of the actuators to preserve system reliability while maximizing control performance. Two approaches are proposed to preserve system reliability: a global approach that integrates in the control algorithm a representation of system reliability, and a local approach that integrates a representation of component reliability. The trade-off between the system reliability and the control performance should be taken into account. A methodology for MPC tuning is proposed to handle this trade-off. System and component reliability are computed based on Dynamic Bayesian Network. The effectiveness and benefits of the proposed control framework are discussed through its application to an over-actuated system.


Keywords: Reliability, Dynamic Bayesian Networks, Model Predictive Control, Reliability Importance Measures

## 1. Introduction

The degradation of physical components in engineering systems is generally inevitable. In particular, the degradation of actuators in a closed-loop control system can lead to poor performance and sometimes in a loss of controllability. Therefore, actuator health is of great importance for the safety and reliability of the controlled system. Thus, to avoid failures it is important to enhance system safety by taking into consideration the reliability of components in the controller design [12].

If the design objective is still to maintain the original system performance, this may force the remaining actuators to work beyond their normal duty to compensate the handicaps caused by the fault. Therefore, the tradeoff between achievable performance and available actuator capability should be carefully considered in all control designs.

Considerable research has been carried out in order to enhance the system reliability from the manufacturing and system structure point of view. Recently, system reliability has been taken into account in the system control process through a Prognosis and Health Management (PHM) framework. Mainly because reliability is as a measure of how long the system will perform its function correctly [7] and can be used to predict future failures in the system given the state of its components.

In some cases the control effort can be redistributed among the available actuators to relieve the work load and the stress factors on assets with worst conditions avoiding in this manner their deterioration. For this purpose,

[^0]an appropriate policy should be developed to redistribute the control effort until maintenance actions can be taken. In this work, the actuator and system reliability are integrated in the control design and used as a policy which serves to redistribute the control effort among the actuators $[23,24]$.

This paper presents a method to manage the system reliability while performing the control of the system within a framework based on Model Predictive Control (MPC). For this purpose, the paper presents two approaches, the local approach, based on the components reliability and the global approach focused on the system reliability. As a result, a trade-off between system reliability and control performance arises.

The growing importance of maintenance has generated an increasing interest in the development and implementation of optimal maintenance strategies for improving system reliability, preventing the occurrence of system failures, and reducing maintenance costs of deteriorating systems [9].

MPC is an efficient technique to manage this kind of objectives. It allows the incorporation of several criteria in the optimization problem. By instance, in [8] the authors present an application of MPC to a Drinking Water Network (DWN) which includes in the optimization problem several criteria such as a criteria for economic cost, level of service and level of components degradation.

In [21] and [22], the MPC formulation includes the actuator usage as constraints, whose objective is to maintain the accumulated usage under a safety level at the end of the mission.

Reliability can be modelled as an exponential function $[6,33]$, as a Weibull function $[2,11]$ or a Gamma function


[^0]:    *Corresponding author

    Email address: jean.salazar@upc.edu (Jean C. Salazar)

# List of acronyms and notation 


$\bar{u}_{i} \quad$ Upper bound of the control input for the $i$ actuator
$H_{r} \quad$ Control horizon
$H_{p} \quad$ Prediction horizon
$\rho \quad$ Energy weighting parameter
$\varepsilon \quad$ Weighting parameter of cost function objectives
$\lambda_{i} \quad$ Failure rate of the $i$ th component
$\lambda_{i}^{0} \quad$ Baseline failure rate of the $i$ th component
$C_{k} \quad k$ th minimal cut set
$P_{s} \quad s$ th minimal path set
$\mathrm{P}(\mathrm{A}) \quad$ Probability of event A
$\mathrm{P}(\mathrm{A} \mid \mathrm{B})$ Probability of event A given B
$R_{i} \quad$ Reliability of the $i$ th component
$R \quad$ Reliability of the system
$T_{s} \quad$ Sampling time
$\Phi(\cdot) \quad$ Structure function
$e_{i} \quad$ Random variable representing the state of the $i$ th component
$S \quad$ Random variable representing the state of the system
$X_{i} \quad$ Random variable representing the state of the $i$ th component of the system
$\mathbf{X} \quad$ System state vector composed of $X_{i}$ elements
$T_{M} \quad$ Mission time
$[17,18,26]$, among others. It can also be expressed as a stochastic process [20], using a Markov chain (MC) to model the reliability of the components with the drawback that in practice and depending on the complexity of the system this can lead to a combinatorial explosion of states $[32]$.

The use of Bayesian Networks (BN) to model and computing the reliability of the system, taking into account observations (evidences) about the state of the components has been considered recently in some works [1, 2, 27, 30]. In [25] the authors present the advantages of BNs in comparison with reliability block diagrams. In [4], a fault tree is modelled using a BN. A comparison between MC and Dynamic Bayesian Networks (DBN) applied to reliability is presented in [31]. DBNs are interesting because they allow to model the system reliability with a factorization of the MC states leading to a compact model representation.

The purpose of this paper is to present the benefit of taking into account system and component reliability as criteria in the MPC algorithm through an illustration dedicated to DWN as a part of a PHM strategy.

The paper presents a study on local and global approaches to manage the system reliability, using Reliability Importance Measures (RIMs). The global system reliability is modelled using a DBN.

The rest of the work is organized as follows: Section 2 deals with the components and system reliability mod-
elling. Section 3 presents the RIM used in the global approach. In Section 4 a description of the MPC framework is presented. Section 5 presents the application of the MPC framework on a DWN system and some results of the control application are discussed. Finally in Section 6 some conclusions are given.

## 2. Reliability Modelling

### 2.1. Reliability concept

Before introducing the concept of reliability, let us first define the concept of failure rate. The general definition of failure rate, denoted as $\lambda$, is stated as the fraction of the density of the random lifetime to the survival function (i.e. conditional probability).

From this definition, the failure rate can be interpreted as the probability that a component will fail at the next instant time $(k+\Delta t)$ given that it has survive until the current instant time $(k)$.

In this work, the definition given by [5] is used, where the failure rate for the $i$ th item is modelled as:

$$
\lambda_{i}(k)=\lambda_{i}^{0} \times g(\ell, \vartheta)
$$

where $\lambda_{i}^{0}$ represents the baseline failure rate or nominal failure rate and $g(\ell, \vartheta)$ is a load function also known as

covariate, that represents the effect of stress on the component failure rate. $\ell$ represents an image of the applied load and $\vartheta$ is a component parameter.

Different definitions of function $g(\ell, \vartheta)$ exists in the literature. However, the exponential form is the most commonly used. In [13, 14] the authors propose a load function based on the root-mean-square of the applied control input $\left(u_{i}\right)$ until the end of the mission $\left(T_{M}\right)$, and an actuator parameter defined from the upper and lower bounds of control input.

Moreover, the operating conditions and environmental factors, such as stress, load, temperature, pressure, etc., under which device operates must be taken into account. In this work, it is assumed that the failure rate is provided by:

$$
\lambda_{i}(k)=\lambda_{i}^{0} g_{i}\left(u_{i}(k)\right)
$$

In (2) $g_{i}\left(u_{i}(k)\right)$ represents the amount of load on the actuator and corresponds to the following normalized control action:

$$
g_{i}\left(u_{i}(k)\right)=\frac{u_{i}(k)-\underline{u}_{i}}{\bar{u}_{i}-\underline{u}_{i}}
$$

where $u_{i}(k)$ is the control effort at time $k, \underline{u}_{i}$ and $\bar{u}_{i}$ are the minimum and maximum control efforts allowed for the $i$ th actuator. The major actuator load corresponds to $u_{i}(k)=$ $\bar{u}_{i}$, which leads to the worst failure rate $\lambda_{i}=\lambda_{i}^{0}$.

Accordingly to the failure rate definition, reliability is the probability that a system will perform its functioning satisfactorily for a given period of time and under stated operating conditions.

In this paper an exponential model for the component reliability is used:

$$
R_{i}(t)=e^{-\int_{0}^{t} \lambda_{i}(v) d v}
$$

and in discrete time it follows:

$$
R_{i}(k+1)=e^{\left(-T_{s} \sum_{v=0}^{k+1} \lambda_{i}(v)\right)}
$$

where $\lambda_{i}(v)$ is the failure rate that is obtained from the $i$ th component under different levels of load and $T_{s}$ is the sampling time.

For analysis simplification but without loss of generality, it is assumed that all the components are mutually independent. This means that the joint distribution of the system state vector $\left(\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)\right)$ is determined by the reliability of its components.

The dependence of the state of the system regards to the state of the components can be determined by means of its structure function $(\Phi(\mathbf{X}))$. This function indicates the status of the system (success or failure) given the states of each component.

For instance, the structure function can be computed using either the minimal path sets $\left(P_{s}\right)$ which are the minimal sets of elements of the system whose functioning (i.e., being up -Up-) ensures that the system is up (6), or the minimal cut sets $\left(C_{k}\right)$ which are the minimal sets of elements of the system whose failure (i.e. being down -Dn-) causes the failure of the system (7).

$$
\begin{aligned}
& \Phi_{p}(\mathbf{X})=1-\prod_{j=1}^{s}\left(1-\prod_{i \in P_{j}} X_{i}\right) \\
& \Phi_{c}(\mathbf{X})=\prod_{j=1}^{k}\left(1-\prod_{i \in C_{j}}\left(1-X_{i}\right)\right)
\end{aligned}
$$

where $X_{i}$ is a random binary variable that represents the state of the component: $X_{i}=1$ the component is $U p$, $X_{i}=0$ the component is $D n$.

As both of methods are equivalent in this work the minimal path set approach is used.

Hence, the reliability of the system is defined as the expectation of the structure function, this is:

$$
R=E[\Phi(\mathbf{X})]
$$

which can be expressed in probability terms as:

$$
R=\mathrm{P}(\Phi(\mathbf{X})=1)
$$

Therefore, if $\Phi(\mathbf{X})=1$ the system is up $(U p)$, and if $\Phi(\mathbf{X})=0$ the system is down $(D n)$. Generally, the reliability is determined by the way the components are interconnected in the system, i.e., serial or parallel or a combination of them.

### 2.2. Bayesian Networks 8 Dynamic Bayesian Networks

Basically, Bayesian Networks compute the probability distribution in a set of variables according to the prior knowledge of some variables and the observation of others [10]. BNs can be considered as a subset of Directed Acyclic Graph (DAG).

To illustrate this concept, let $\mathbf{A}$ and $\mathbf{B}$ be two nodes with two possible states $\left(\mathbf{S}_{1}\right.$ and $\left.\mathbf{S}_{2}\right)$ (Figure 1). A probability is associated to each state of the node $\mathbf{A}$ and this probability is defined a priori for a root node and computed by inference for the others. The a priori probabilities of node $\mathbf{A}$ are $\mathrm{P}\left(\mathbf{A}=\mathbf{S}_{A 1}\right)$ and $\mathrm{P}\left(\mathbf{A}=\mathbf{S}_{A 2}\right)$.
![img-0.jpeg](img-0.jpeg)

Figure 1: Basic Bayesian Network.
A Conditional Probability Table (CPT) is associated with node $\mathbf{B}$ and defines the conditional probability of the state of $\mathbf{B}$ given the state of $\mathbf{A}(\mathrm{P}(\mathbf{B} \mid \mathbf{A}))$.

Thus, the BN inference computes the marginal distribution e.g. $\mathrm{P}\left(\mathbf{B}=\mathbf{S}_{B 1}\right)$ as:

$$
\begin{aligned}
\mathrm{P}\left(\mathbf{B}=\mathbf{S}_{B 1}\right)= & \mathrm{P}\left(\mathbf{B}=\mathbf{S}_{B 1} \mid \mathbf{A}=\mathbf{S}_{A 1}\right) \mathrm{P}\left(\mathbf{A}=\mathbf{S}_{A 1}\right) \\
& +\mathrm{P}\left(\mathbf{B}=\mathbf{S}_{B 1} \mid \mathbf{A}=S_{A 2}\right) \mathrm{P}\left(\mathbf{A}=\mathbf{S}_{A 2}\right)
\end{aligned}
$$

A special case of Bayesian Network called Dynamic Bayesian Network (DBN) is used to model the time dependency of a process. In a DBN the random variables are time indexed, so the process state $S_{A}:\left\{s_{1}^{A}, \ldots, s_{M}^{A}\right\}$ is represented by nodes $\mathbf{A}_{k}$ and $\mathbf{A}_{k+\Delta t}$ at time instants $k$ and $k+\Delta t$, respectively. The time dependence is represented by an arc and the temporal evolution of the variables is represented by successive time slices as shows Figure 2 (for simplicity let $\Delta t$ be equal to 1 ).

The transition probability between the states of the variable at time instant $k$ to $k+1$ is defined by a CPT intertime slices. Given the probability distribution $\mathrm{P}\left(\mathbf{A}_{k}\right)$ at time instant $k$, the network leads by inference to a unique distribution $\mathrm{P}\left(\mathbf{A}_{k+1}\right)$ at time instant $k+1$. The computation over time of $\mathrm{P}\left(\mathbf{A}_{T}\right)$ is performed by iterative inferences starting from $k=0$ and $\mathrm{P}\left(\mathbf{A}_{0}\right)$ [1].
![img-1.jpeg](img-1.jpeg)

Figure 2: DBN model for the $i$ th component.

### 2.3. Components reliability modelling

The decay of the components reliability can be modelled using a Markov chain process. This type of process is very useful in system reliability modelling due to its memoryless property, which means, that the state transitions only depend on the current and next state, and it does not depend on the previous state or the amount of time that the process has stayed in the current state, making it an effective tool for system reliability analysis [28].

Let $e_{i}$ be a discrete random variable in the Markov process representing the state of the $i$ th component with two possible mutually exclusive states $\{U p, D n\}$. The probabilistic state transition between the states is defined by:

$$
\mathbf{P}_{\mathrm{MC}}=\left[\begin{array}{cc}
1-p_{12} & p_{12} \\
0 & 1
\end{array}\right]
$$

where $p_{12} \cong \lambda \Delta t: \lambda$ represents a constant failure rate and $\Delta t$ the time interval, and $p_{12}$ can be interpreted as the probability that the component goes from state $U p$ to $D n$ after $\Delta t$.

In the case of components whose failure rate depends on time, their reliability decay can be modeled by a semiMarkov chain (Figure 3).

The MC is homogeneous if the transition probabilities of the states are independent on time. In a semi-Markov chain, the memoryless property is relaxed, which means that the state transition depends on the current state and the transition time. Therefore, the probability matrix (11) becomes dependent on time:

$$
\mathbf{P}_{\mathrm{MC}}\left(e_{i^{k}+1} \mid e_{i^{k}}\right)=\left[\begin{array}{cc}
1-p_{12}(k) & p_{12}(k) \\
0 & 1
\end{array}\right]
$$

![img-2.jpeg](img-2.jpeg)

Figure 3: Semi-Markov chain for the component reliability.
From (12) it is clear that the failure rate is the probability of component state to be $D n$ at instant time $k+1$ given that its state was $U p$ at time $k$, this is:

$$
\lambda_{i}(k)=\mathrm{P}\left(e_{i}(k+1)=D n \mid e_{i}(k)=U p\right)
$$

The semi-Markov chain is modelled by a Dynamic Bayesian Network with CPT evolving according to time. In this case the evolution is represented in two time slides (Figure 4) $[1]$.
![img-3.jpeg](img-3.jpeg)

Figure 4: DBN model for the $i$ th component.
Therefore, DBN computes the component reliability using:

$$
R_{i}(k+1)=\mathrm{P}\left(e_{i}(k+1)=U p\right)
$$

which follows expression (5).

### 2.4. System reliability modelling

A system is defined as a set of $i$ components whose states are described by the random variable $e_{i}$, as:

$$
\mathrm{P}\left(X_{i}=1\right)=\mathrm{P}\left(e_{i}=U p\right) ; \mathrm{P}\left(X_{i}=0\right)=\mathrm{P}\left(e_{i}=D n\right)
$$

where $X_{i}: X_{i}=1$ if the $i$ th component is up, $X_{i}=0$ if the $i$ th component is down.

Assume that the state of the components are known. Therefore, in this work the system reliability is computed from its components reliability using a DBN.

For instance, once the minimal path sets of the system are identified, its states (i.e., if the minimal path set is up or down) are represented by a random variable as a node in the DBN. The state of the components of the system are also represented as nodes in the DBN and are connected to their respective minimal path set node. Note that the probabilities of the component states are computed by inferences in the DBN modelling of the semi Markov chain described in Section 2.3.

Finally, the state of the system (i.e., system reliability) is given by the top node of the BN which is connected to the minimal path set nodes.

For example, consider the reliability block diagram (RBD) of Figure 5, which shows the contribution of component reliability to the success or failure of a three components system. It is clear that with a minimum of two components the system can performs its function satisfactorily, being $\{1,3\}$ and $\{2,3\}$ the minimal path sets of the system. Although, in this example a RBD is used to define the structure of the BN, the minimal path sets can also be obtained by other methods or directly from the system. This will be illustrated in the case study in Section 5.
![img-4.jpeg](img-4.jpeg)

Figure 5: RBD of a three components system example.
Then, it is possible to build a BN of the system reliability from its minimal path sets see Figure 6, being $e_{i}$ the probability of the $i$ th component state, $P_{i}$ the probability of the state of the $i$ th minimal path set and $S$ the probability of the system state [27].
![img-5.jpeg](img-5.jpeg)

Figure 6: Bayesian Network of system reliability.
Tables 1 and 2 present the CPTs of nodes $P_{1}$ and $S$, respectively. $P_{1}$ depends on the states of the components $e_{1}$ and $e_{3}$ and its behaviour corresponds to an AND gate, i.e., all the components in a success path should be available for the system to be available. $S$ depends on the state of success path nodes $P_{1}$ and $P_{2}$ and has the behaviour of an OR gate, i.e., if there is at least one success path available, then the system will be available.

Table 1: CPT for node $P_{1}$.




It is possible then to compute the probability distribution for each variable conditioned by the values of the other
variables in the graph. This feature is particularly important in case a control system must work in real-time, because in that case evidences acquired about a state variable must be propagated to update the state of the rest of the domain. Therefore, the reliability of the system $(R)$ is computed using the BN as:

$$
R(k+1)=\mathrm{P}(S(k+1)=U p)
$$

In the case of complex structure systems with high amount of components the compute of the structure function becomes non trivial. The use of BNs to reliability modelling allows several modelling structures based on minimal path sets, or logical combination of components states (using AND or OR gates) [15].

## 3. Reliability Importance Measures

One of the objectives of system reliability analysis is to identify the weakness in a system and to quantify the impact of components failures over system functioning. Several indicators of reliability importance exist, each expressing the importance from a slightly different point of view.

Importance Measures (IMs) were first introduced by [3] and are classified in two groups: Reliability Importance Measures (RIMs) and Structural Importance Measures (SIMs). The RIMs evaluate the relative importance of a component taking into account its contribution to the system reliability and the SIMs provide the relative importance of a component taking into account its position into the system structure.

These metrics can be defined according to their functional aspect, leading to their modelling by the minimal path sets, and according to their dysfunctional aspect, leading to their modelling by the minimal cut sets. As both are equivalent, in this study only the functional aspect is used.

The aim is to quantify the importance of the $i$ th component for the reliability of the total system and how the changes in the component reliability impact in the system reliability.

One of the most used RIMs is the Birnbaum's importance measure [3] also known as Marginal Importance Factor (MIF). MIF is related to the probability that a component is critical for the system.

Definition 1. The Birnbaum's importance measure of the $i$ th component for the functioning of the system, denoted as $\mathrm{I}_{\mathrm{B} i}(i ; \mathbf{p})$, for a coherent system with independent components it is defined as:

$$
\begin{aligned}
\mathrm{I}_{\mathrm{B}}(i, \mathbf{p}) & =\frac{\partial R(\mathbf{p})}{\partial p_{i}} \\
& =\mathrm{P}\left(S=U p \mid e_{i}=U p\right)-\mathrm{P}\left(S=U p \mid e_{i}=D n\right)
\end{aligned}
$$

This measure is well known from classical sensitivity analysis. It represents the probability that the failure and functioning of the $i$ th component coincide with the failure

and functioning of the system. This can be interpreted as the maximum decrease of system reliability when the $i$ th component changes from the condition of perfect functioning to failed condition.

Note that the Birnbaum's importance measure of the $i$ th component only depends on the structure of the system and the reliabilities of the other components, and that it is independent of the actual reliability of the $i$ th component.

The Birnbaum's importance measure of component $i$ can be computed by inference using the DBN system model by introducing evidences about the states of each component (i.e., being $U p$ or $D n$ ) and computing the difference between the system reliabilities in both cases.

## 4. Reliability aware MPC Framework

### 4.1. MPC formulation

Consider the following linear discrete-time dynamic model of a system described in the state-space form as:

$$
\begin{aligned}
x(k+1) & =A x(k)+B u(k) \\
y(k) & =C x(k)
\end{aligned}
$$

where for each $k \in \mathbb{Z}^{+}, x(k) \in \mathbb{R}^{n}$ is the state, $u(k) \in \mathbb{R}^{p}$ is the control input, $y(k) \in \mathbb{R}^{q}$ is the measured output, $A \in \mathbb{R}^{n \times n}$ is the state matrix, $B \in \mathbb{R}^{q \times p}$ is the input matrix and $C \in \mathbb{R}^{q \times n}$ is the output matrix.

Model-based predictive control (MPC) is a discrete time technique where an explicit dynamic model of the plant is considered to predict the system outputs by applying (20) recursively along the prediction horizon, obtaining (18) $\left(H_{p}\right)$ where $\hat{u}(k+i \mid k)$ is the control input corresponding to $k+i$ calculated at time instant $k$, and the hat notation represents a predicted value.

The control actions are manipulated throughout a finite control horizon $\left(H_{c}\right)$ in order to minimize a given cost function, with $H_{c}<H_{p}$. This methodology is represented in Figure 7, where the past outputs and control input sequences (showed in the left side) are used to compute the future output sequence over $H_{p}$ and future control inputs
![img-6.jpeg](img-6.jpeg)

Figure 7: Model Predictive Control basic concept
sequences over $H_{c}$. Such that the cost function is minimized.

The cost function generally includes a term for the tracking error, minimizing the square difference between the predicted output $(\hat{Y})$ and the set-point $\left(Y_{\text {ref }}\right)$, and a term for the minimization of the square of the energy $(\hat{U})$ and its variation $(\Delta \hat{U})$ according to (18) and (19).

In this work, the cost function $J$ is defined as:

$$
\begin{aligned}
& J=\varepsilon\left[\hat{Y}-Y_{\text {ref }}\right]^{\top}\left[\hat{Y}-Y_{\text {ref }}\right] \\
& \min \\
& \text { ( } \hat{U}(k \mid k), \ldots, \\
& \hat{U}(k+H c-1 \mid k), \\
& \Delta \hat{U}(k \mid k), \ldots, \\
& \Delta \hat{U}(k+H_{c}-1 \mid k)) \\
& \text { subject to } \quad \underline{U} \leq \hat{U} \leq \bar{U} \\
& \underline{X} \leq \bar{X} \leq \bar{X}
\end{aligned}
$$

where: $Y_{\text {ref }}=\left[y_{\text {ref }}(k+1), \ldots, y_{\text {ref }}\left(k+H_{p}\right)\right]^{\top}$ is the output reference, $\boldsymbol{\rho}=\operatorname{diag}(\rho, \rho, \ldots, \rho)$ of size $H_{c} \times H_{c}$ and $\rho=\operatorname{diag}\left(\rho_{1}, \rho_{2}, \ldots, \rho_{p}\right)$ is the weighting for the energy and $\varepsilon$ is a weighting parameter between tracking and energy objectives, $\underline{U}, \bar{U}, \underline{X}$ and $\bar{X}$, are the lower and upper bounds of the control effort and system states, respectively.

The resulting control action $\hat{u}(k \mid k)$ is injected to the system while $\hat{u}(k+i \mid k) \forall i=1, \ldots, H_{c}-1$ are discarded. At
![img-7.jpeg](img-7.jpeg)

next instant time $k+1, y(k+1)$ is measured and the optimization problem is solved again. Thus, $\hat{u}(k+1 \mid k+1)$ is calculated moving the prediction horizon using the concept of sliding window.

### 4.2. MPC tuning methodology

MPC tuning involves finding the appropriate values for the weighting parameters in the cost function, as well as the prediction and control horizons that depend on the application and the amount of data that can be handled.

This work focuses on proposing a methodology to find $\rho$ and $\varepsilon$ in (21) as follows:

Step 1:
Select $\varepsilon=0$ and through simulations find the optimal value of $\rho$ in which the reliability of the system at the end of the mission time is the highest.
The comparison and selection of the best approach is performed based on the following criteria. Let the Joint Component Reliability index (JCR) be a measure of the remained overall reliability of the system components at the end of the mission time:

$$
\mathrm{JCR}=\prod_{i=1}^{p} R_{i}
$$

and, let the Cumulative Actuator Usage (CAU) be a measure of the actuator energy consumption defined as:

$$
\mathrm{CAU}=T_{s} \sum_{k=0}^{T_{M} / T_{s}} U(k)^{\top} U(k)
$$

where $T_{M}$ is the mission time.
Step 2:
Having selected $\rho$ as mentioned in the previous step, find the optimal value of $\varepsilon$ through simulations, starting from $\varepsilon=0$ to 1 .
The idea is to study the effect produced by the variation of parameter $\varepsilon$ in the system reliability or in other words, the impact of the tracking error in the reliability. To measure this impact, an index called the integral square error (ISE) is defined:

$$
\mathrm{ISE}=T_{s} \sum_{k=0}^{T_{M} / T_{s}}\left[\hat{Y}(k)-Y_{r e f}(k)\right]^{\top}\left[\hat{Y}(k)-Y_{r e f}(k)\right]
$$

Therefore, the $\varepsilon$ value which corresponds to the highest system reliability and the lowest ISE.

### 4.3. Control action redistribution

The weights $\rho$ in the cost function (21) redistribute the control effort among the actuators [23].

In this work, a global and a local approach are proposed to handle the reliability in the optimization problem. The
global approach consists in considering the Birnbaum's importance measure viewed in Section 3 (computed using the DBN reliability model) by setting:

$$
\rho(k)=\operatorname{diag}\left(\mathrm{I}_{\mathrm{B} i}(k)\right) \forall i=1,2, \ldots, p
$$

in this case, it is expected that components with a greater contribution to the system reliability are used less than the others.

On the other hand, the local approach tries to preserve system reliability by preserving component reliability by setting the weight as:

$$
\rho(k)=\operatorname{diag}\left(1-R_{i}(k)\right) \forall i=1,2, \ldots, p
$$

This criteria aims at finding the optimal control actions and distribute it among the available actuators in such a way that actuators with lower reliability level are relieved. Hence, the use of highly reliable components is prioritized.

The local approach assumes an equivalent contribution of component reliability to system reliability. However, this is hardly ever true. In fact, the DBN reliability model can intrinsically explain this relation.

The control strategy scheme is presented in Figure 8. On the one hand, the MPC computes the control inputs according to: the cost function, a set of bounds, the current system state and the weight $\rho$. Then, the control input is injected to the system and used to compute the component failure rates.
![img-8.jpeg](img-8.jpeg)

Figure 8: Block diagram of the approach
On the other hand, those failure rates are used in the DBN to compute: the components reliability, the overall system reliability and the Birnbaum's importance measure. This data is used then to update the weight $\rho$, which is used in the MPC algorithm, closing in this way the loop.

## 5. Application: Drinking Water Network

### 5.1. System description

A DWN is composed by sources (water supplies), sinks (water demand sectors) and pipelines that link sources to sinks. It also contains active elements like pumps, valves.

![img-9.jpeg](img-9.jpeg)

Figure 9: Drinking water network diagram.

The considered DWN corresponds to a subsystem of the Barcelona water transport network [30] (Figure 9).

The network consists of 5 sources and 1 sink. It is assumed that the demand forecast at the sink (d_{m}(k)) is known (Figure 10), and that any single source can satisfy this required water demand. It is also assumed that the volume of the tanks should follow a given set point (Figure 11).

![img-10.jpeg](img-10.jpeg)

Figure 10: Drinking water demand.

The DWN is modelled by applying mass balance to each tank and the following linear discrete-time model is obtained:

$$
\beginaligned}
x(k+1) & =Ax(k)+Bu(k)+B_d d_m(k) \\
y(k) & =Cx(k)
\endaligned
\tag{27}
$$

where x(k) ∈ R^{n} are tanks volume, u(k) ∈ R^{p} are the control inputs (pump commands) with u(k) ≥ 0 ∀ k, y(k) ∈ R^{q} are the measured tanks volume, d_{m}(k) ∈ R^{m} is the water demand, A ∈ R^{n×n} is the state matrix, B ∈ R^{q×p} input matrix, B_{d} ∈ R^{n×m} is the disturbance matrix, and C ∈ R^{q×n} is the output matrix.

![img-11.jpeg](img-11.jpeg)

Figure 11: Volume reference for the 4 reservoirs

### 5.2. Dynamic Bayesian Network modelling

The DWN reliability is modelled using a DBN following the methodology explained in Section 2.4. Firstly, system components must be identified. In this case there are 10 pumps, 5 sources, 4 tanks and several pipes.

Secondly, the minimal path sets should be determined. A minimal path set is composed of those components which allow a flow path between sources and sinks, such as pipes, tanks and pumps. A list of the components that correspond to each minimal path set is presented in Table 3. There are nine minimal path sets in the system of Figure 9. Each minimal path set is available depending on the reliability of its components. Pipes and tanks are considered perfectly reliable so they do not provide significant information to the network. Nevertheless, sources are included in the minimal path sets merely for illustrating the procedure.

Table 3: Components and minimal path sets relationship.


![img-12.jpeg](img-12.jpeg)

Figure 12: Dynamic Bayesian network model of the DWN.

At each sampling time, the reliability $R_{i}$ of each pump is computed according to its failure rate using a MC (Figure 12). Its behaviour follows an exponential distribution as stated in (4).

Note that it is independent of the previous states of the component. It only depends on its present state. In the DBN, this corresponds to the CPT shown in Table 4.

Table 4: Inter-time slices CPT for node $e_{i^{k+1}}$.


Remark 1. The failure rate is computed according to $g_{i}\left(u_{i}(k)\right)$. The CPT shown in Table 4 defines the discretized stochastic process of using (2) and (3) in (4).

The CPT of node $P_{1}$ is shown in Table 5. This CPT depends on the states of the source $1\left(A_{1}\right)$ and pumps 1 and $5\left(e_{1}, e_{5}\right)$. Its behaviour corresponds to an AND gate.

Table 5: CPTs for nodes $P_{1}$.


It is assumed that with one source it is possible to satisfy the water demand. Thus, the availability of the system can be assured as long as at least one of paths $P_{i}$ is available, which corresponds to the CPT of node $S$ shown in Table 6. It depends on the state of nodes $P_{1}$ to $P_{9}$ and has the behaviour of an OR gate.

Table 6: CPT for node $S$.


The system reliability of the DWN is computed by implementing the DBN presented in the Figure 12 using the BNT toolbox for Matlab [19].

### 5.3. MPC with reliability optimization

The control of the DWN system is performed applying the MPC formulation of Section 4. Table 7 provides the simulation parameters used. A hierarchical control structure is assumed, where the MPC layer produces a set of set-points for the lower level flow controllers. Hence, a 1 hour sampling time is assumed for the upper level MPC. Since the water demand (Figure 10) exhibits a daily profile, a 24 h prediction horizon has been chosen and the initial tank volumes have been set to $X_{0}$.

Table 7: Simulation parameters


To find the appropriate values for the weighting parameters the procedure presented in Section 4 is followed.

First, Step 1 is applied and the following simulation scenarios are considered: $\rho_{i}=1-R_{i}, \rho_{i}=\mathrm{I}_{\mathrm{Bi}}$ and $\rho_{i}=1$ where no dependency on system reliability is assumed.

Figure 13 displays the $\rho_{i}=1-R_{i}$ weights evolution, where the smaller reliability profile (i.e., higher weight) corresponds to pumps $1,2,3$ and 7 .
![img-13.jpeg](img-13.jpeg)

Figure 13: MPC weights for the case $\rho_{i}=1-R_{i}$.
Figure 14, provides the $\rho_{i}=\mathrm{I}_{\mathrm{B} i}$ weights evolution, where the highest weight corresponds to pump 6 (in the figure it goes off of the plot). In this scenario, the system reliability is highly sensitive to pump 6 reliability, so MPC tries to preserve the system reliability by preventing its use.
![img-14.jpeg](img-14.jpeg)

Figure 14: MPC weights for the case $\rho_{i}=\mathrm{I}_{\mathrm{B} i}$.
Table 8 presents the indexes values for each scenario. For $\rho_{i}=1-R_{i}$ system reliability is improved with respect to the nominal case. However, the best system reliability results are achieved when $\rho_{i}=\mathrm{I}_{\mathrm{B} i}$.

Table 8: Indexes of the RIMs in control loop at $T_{M}$.


Instead, the case $\rho_{i}=1-R_{i}$ provides the best joint component reliability. In this case, these results show that the global approach improves more slightly the overall system reliability than the local approach. This is explained by the fact that in the local approach, individual component reliabilities are not incremented all at once, and that the failure rate of the components is not the same. Then, in the global approach, the components use is penalized depending on their impact in the overall reliability system.

In both cases (local and global), improving system reliability leads to an increase in the cumulative actuator usage which indicates that the improvement of system reliability can lead to an increase of energy consumption.

Concerning the case $\rho_{i}=\mathrm{I}_{\mathrm{B} i}$, note that those pumps that do not belong to minimal path sets $P_{5}$ and $P_{8}$ (i.e., pumps $1,2,3,6,8$ and 9 ) are greatly penalized. This is mainly due to the criticality of pump 6 from a system reliability point of view. Remark from Table 3 that pump 6 belongs to 7 out of 9 minimal path sets.

Figure 15 provides the evolution of the input commands $\left(u_{i}\right)$ produced by the MPC layer for each pump in the three different cases. Remark that, when $\rho_{i}=1-R_{i}$, the usage of the pumps with a greater baseline failure rate are diminished.
![img-15.jpeg](img-15.jpeg)

Figure 15: Pump commands corresponding to $\rho_{i}=1$ (blue), $\rho_{i}=$ $1-R_{i}$ (green) and $\rho_{i}=\mathrm{I}_{\mathrm{B} i}$ (red).

Once selected $\rho=\mathrm{I}_{\mathrm{B} i}$ as the optimal setting to obtain the best system reliability, the optimal value of $\varepsilon$ will be chosen following Step 2 of the procedure presented in Section 4.

To this purpose several simulations were done for $\varepsilon$ in the range of 0 to 1 . Figure 16 presents the reliability ob-

tained at the end of the simulation time, where the main system reliability behaviour is, as expected, decreasing as $\varepsilon$ increases. Nevertheless, for some specific values of $\varepsilon$, the system reliability tends to stay steady or even increases when $\varepsilon=10^{0}$, perhaps it is due to numerical issues in the optimization solver.
![img-16.jpeg](img-16.jpeg)

Figure 16: Overall system reliability evolution for the 4 reservoirs
Figure 17 shows the tracking error obtained at the end of the mission. These results show that as $\varepsilon$ approaches to 1 , less ISE is obtained, as it can be expected from (21), since the tracking error is less penalized.
![img-17.jpeg](img-17.jpeg)

Figure 17: Tracking error for the 4 reservoirs in semilog scale
Therefore according to these results, $\rho$ should be selected as $\rho=\mathrm{I}_{\mathrm{Br}}$, and the value of $\varepsilon$ which has the highest system reliability and lowest ISE is around $10^{-10}$. Figure 18 presents the tracking response of the control algorithm.

## 6. Conclusions

An MPC framework that takes into account the usage of the actuators to preserve system reliability while maximizing control performance has been proposed in this work. A methodology has been proposed to tune the MPC cost function weights that provide best system reliability and control performance. To handle the reliability in the optimization problem of the MPC controller, a global approach considering the Birnbaum's importance measure
![img-18.jpeg](img-18.jpeg)

Figure 18: Tracking references of tanks
and a local approach, considering an equivalent contribution of component reliability to system reliability, have been studied.

The reliability assessment is computed on-line using a Dynamic Bayesian Network (DBN).

Results show that a reliability importance measure provides better system reliability. In this work the Birnbaum's importance measure has been studied, but other reliability importance measures exist [16].

Future research will focus on the study of these other importance measures for reliability preservation through MPC tuning.

The methodology presented in this paper is based in determining the minimal path sets, which is known to be an NP-hard problem when applied to complex system with high amount of components. Nevertheless, the DBN model may be build from other methods based on a top down analysis avoiding the specification of all path sets [29].

## Acknowledgements

This paper is an extension of a paper presented at the 9th IFAC Symposium on Fault Detection, Supervision and Safety for Technical Processes SAFEPROCESS'15, September 2-4, 2015. It has been selected for the special section of Reliability Engineering and System Safety (Elsevier) on "Applications of Probabilistic Graphical Models in Dependability, Diagnosis and Prognosis". Guest editors: Philippe Weber and Luigi Portinale.

The authors would like to thank all the anonymous reviewers for their valuable comments and suggestions, as these comments led us to an improvement of the work quality.

This work was supported by Spanish Government (Ministerio de Economía y Competitividad) and FEDER under project DPI2014-58104-R (HARCRICS).
