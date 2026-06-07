# Replacement policies for a complex system with unobservable components using dynamic Bayesian networks 

Demet Özgür-Ünlüakın ${ }^{1}$ ', Taner Bilgiç ${ }^{2}$<br>${ }^{1}$ Industrial Engineering Department, Bahçeşehir University, 34353, Beşiktaş, İstanbul, Turkey<br>E-mail: demet.unluakin@bahcesehir.edu.tr<br>${ }^{2}$ Industrial Engineering Department, Boğaziçi University, 34342, Bebek, İstanbul, Turkey<br>E-mail: taner@boun.edu.tr<br>Received 15 December 2012<br>Accepted 8 July 2013


#### Abstract

We study maintenance of a complex dynamic system consisting of ageing and unobservable components under a predetermined threshold reliability level. Our aim is to construct an optimum replacement policy for the components of the system by minimizing total number of replacements or total replacement cost. We represent the problem with dynamic Bayesian networks (DBNs). We prove that under the existence of a predetermined threshold reliability, performing replacements at periods when the system reliability just falls below the threshold assures optimum replacement times. Four component selection approaches and their cost focused versions are proposed to choose the component to replace and are tested on a complex dynamic problem. Their performances are analyzed under various threshold and cost levels.


Keywords: Maintenace, replacement policy, DBNs, uncertainty modelling, optimization and heuristics.

## 1. Introduction

Maintenance is becoming an increasingly difficult task with the increasing complexity of the systems. One can be either proactive or reactive in maintaining a complex system. If the system breaks down and then the maintenance (repair) is performed, this is reactive. On the other hand, proactive maintenance can either be performed on a fixed schedule or it can be adaptively applied. ${ }^{1}$ We consider the reliability-centered preventive maintenance activities of a complex dynamic system comprised of ageing components. It is not possible to directly ob-

[^0]serve the states of components and that of the system (possibly because the system is far away). However system reliability can be estimated from the interactions of its components. The aim is to optimize component replacement schedules in a given planning horizon such that the (estimated) system reliability is always kept over a predetermined threshold value. The complex nature of the problem does not allow us to show that a threshold policy is optimal for this problem. But we argue that a constant threshold policy is an effective heuristic for complex systems with unobservable components.

We propose a methodology to effectively pre-


[^0]:    ${ }^{1}$ Corresponding author

pare a proactive maintenance plan using dynamic Bayesian networks (DBNs). A DBN is an extended Bayesian network (BN) which includes a temporal dimension. DBN representation allows monitoring the system reliability in a given planning horizon and predicting the system state under different replacement plans. We propose to use DBNs to represent the problem and to do fast inference. We presume that the reliability of the system should be kept over a predetermined threshold value in all periods. This is a reasonable policy in mission critical systems where the failure of the system is a very low probability event due to built in redundancy and other structural properties.

Our approach to maintenance is close to the decision-theoretic troubleshooting problems (DTTP) ${ }^{2}$ in handling complex system structures. DTTPs study a broken system and the aim is to identify and eliminate the underlying fault(s) in the least costly manner. DTTPs are extended to the context of Bayesian networks to handle the complex system structure. ${ }^{3}$ Although DTTPs are characterized by their complex system structures, they have always been studied as a static problem. ${ }^{4,5,6,7,8}$ Naturally, there are some problems for which a static troubleshooting can not be applied. These can be working systems which are under continuous or discrete time monitoring and produce undesirable faulty messages while they are working or systems which are not even observable. For such systems, it may be better to perform troubleshooting/maintenance actions while the system is in process. Furthermore, the system components may be subject to ageing in time which requires a dynamic version of DTTP. This is one of the main motivations for this study.

Recently BNs and DBNs have been applied in the literature frequently to reliability, dependability, risk analysis and maintenance due to their capability to model complex systems. ${ }^{9}$ Although there are some challenges while using BNs, ${ }^{10}$ such as the quantification of the network and inference in hybrid BNs, they are still very convenient in complex real life system domains. BNs and DBNs allow additional power in representing, modelling and analyzing complex dependable systems ${ }^{11,12,13}$ which
are difficult with conventional analysis techniques such as fault trees, Markov chains and stochastic petri networks. ${ }^{14}$ Moreover BNs can handle parameter uncertainty, coverage factors, multi state nodes and sensitivity analysis. ${ }^{15}$

Previous studies related to reliability analysis using DBNs are generally descriptive. ${ }^{16,17}$ The dynamic problem is represented with DBNs and the outcome of the analysis is how system or component reliability behaves in time. ${ }^{18,19}$ The impact of maintenance of an element at a specific time on this behavior is also reported in some of them. ${ }^{20,21}$ However optimization of maintenance activities (i.e., finding a minimum cost plan) ${ }^{22}$ using DBNs is rarely considered which is another main motivation for this study.

In the maintenance problem we tackle, we assume that there exists a predetermined threshold reliability strategy. If such a strategy (control policy) was not set beforehand, the problem could be modelled with dynamic decision networks such as partially observable Markov decision processes (POMDP). A POMDP ${ }^{23,24}$ is a generalization of a Markov decision process (MDP) which permits uncertainty regarding the state of a Markov process. However the generalization of MDPs to POMDPs results in additional computational difficulties. ${ }^{25,26}$ Furthermore, it is very hard to obtain the optimal policy in this setting.

The proposed proactive maintenance methodology described in this paper is an extension of the methodology presented in a previous study. ${ }^{27}$ The major difference of the current paper is on the computational study section where we extend it comprehensively analyzing the performances of the proposed methodologies with two different objectives under various threshold and cost levels. Another major difference is that, in this paper, we give the proof of the proposition in Section 3.2 in details. We propose and test several maintenance policies to maintain the reliability of a system over time above a threshold. In all of the proposals, DBNs are used as the main representation and computational model to predict system reliability. DBNs can be considered to be a generalization of Markov decision models that allow fast inference. Although both exact and

approximate inference in (static) belief networks are computationally hard problems, ${ }^{28,29}$ we insist on exact inference to predict system reliability.

We first show that it is unnecessary to do a replacement if the system reliability is above the threshold and then using this result we propose a series of procedures that differ in their orientation (cost vs. number of repairs) and information use (myopic vs look ahead ${ }^{22}$ or fault vs reliability effect). We analyze performance of these procedures under various threshold and cost levels. Since we do not have any other algorithms from the literature to compare our results to, we test our procedures against a random policy and make available our test problem and procedures for other researchers to work on. ${ }^{30}$

The rest of the paper is organized as follows: We define the maintenance problem in Section 2. The proposed solution is presented in Section 3 where we represent the problem with DBNs and develop an algorithm within the DBN framework. Numerical illustrations are given in Section 4. Finally Section 5 concludes the study.

## 2. Problem definition

The problem we take up can be described as follows: There is a system which consists of several components that are subject to failure. It is not possible to observe the states of components and the system due to the following reasons: The system may be far away or strictly hidden to the decision maker, i.e. it may be in space or inside a nuclear tank. Observing the system may be very expensive or time costly which may be the case in machines having long setup times. The system itself has a very low probability of failure most probably due to built in redundancy. However system reliability can be estimated from the interactions of its components. This is the only way to have an idea about the system which evolves in a discrete-time planning horizon. We presume that the estimated reliability of the system should be kept over a predetermined threshold value in all periods. By this, the system is in an acceptable working situation in all periods. This is reasonable in mission critical systems where the failure of the system is a very low probability event due to
built in redundancy and other structural properties. Components age with a constant transition probability of failure. It is possible to replace components in any period even if they are far away from the decision maker, i.e. by changing software configuration of components. Once replaced, the components will work at their full capacity. Our aim is to determine a replacement policy for the components of a system minimizing either the total number of replacements or the total maintenance cost in a discrete time planning horizon such that reliability of the system never falls below the threshold. Furthermore the following assumptions are made:
(i) All conditional probability distributions are discrete. (ii) All components and the system have two states ("w": working, "nw": failure). (iii) Components can only fail at the beginning of a time period. Once they fail they will be in state "nw" unless they are repaired. (iv) Components can only be replaced at the beginning of each period. Once they are replaced, their working state probability (i.e., their reliability) becomes 1 in that period. (v) If all components are replaced in a period, system reliability becomes 1 in that period. The first two assumptions are required for computational purposes. The third and fourth assumptions are standard in reliability.

## 3. Proposed solution

In this section, we propose dynamic Bayesian Networks (DBNs) ${ }^{31}$ to represent the problem. A DBN is an extended Bayesian network (BN) which includes a temporal dimension. BNs are a widely used formalism for representing uncertain knowledge. The main features of the formalism are a graphical encoding of a set of conditional independence relations and a compact way of representing a joint probability distribution between random variables. ${ }^{32} \mathrm{BNs}$ have the power to represent causal relations between components and the system using conditional probability distributions. ${ }^{33}$

The problem can be formally modelled using dynamic decision networks. However, even with limited information, evaluating such networks are computationally intensive. ${ }^{34}$ Furthermore, it is very dif-

ficult to show the structure of the optimal policy in this setting. Hence we presuppose the existence of a (constant) threshold policy and use DBNs to compute system reliability. This computation is exact under the given assumptions on component ageing and dependency.

We give the details of DBN formulation in Section 3.1. We decouple the decisions of when and what to replace under the existence of a predetermined threshold reliability and perform replacements at periods when the system reliability just falls below the threshold value in Section 3.2. This policy assures optimum replacement times when the objective is either to minimize total number of replacements or to minimize total cost when replacement costs are stationary along the planning horizon. We, then propose component selection approaches in Section 3.3 to select the component to be replaced at a planned replacement time.

### 3.1. DBN formulation

In DBNs there are no formally defined action nodes as in influence diagrams or decision networks. ${ }^{33}$ Nevertheless, replacing or not replacing decisions of each component can be handled with DBNs by modelling actions as chance nodes. For this purpose, an action node for each replaceable component at each period is introduced in the DBN representation of the problem. Such a system is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. DBN representation with action nodes.
In Figure 1, there are three components A, B
and C ; and the state of B depends on the state of A. Let $s_{t}$ denote the system state in period $t$ and $c_{i t}$ denote the state of component $i$ in period $t$ where $i \in\{A, B, C\}$. Solid arcs represent the causal relations among the components and the system node. They constitute the conditional probabilities $P\left(c_{B t} \mid c_{A t}\right)$ and $P\left(s_{t} \mid c_{B t}, c_{C t}\right)$ for all $t=1 . . T$. It is assumed that this probability is the same for all $t=1 . . T$. The dashed arcs represent temporal relations of the components between two consecutive time periods. They constitute the conditional probabilities $P\left(c_{i t} \mid c_{i, t-1}, a_{i t}\right)$. Temporal relations are the transition probabilities of components due to ageing.

Let $a_{i t}$ be the action node of component $i$ at time $t$. All $a_{i t}$ 's have two states which are " $d n$ " standing for doing nothing and " $r c$ " standing for replacing the related component. Initially all $a_{i t}$ 's are given hard evidence of " $d n$ ". Replacement of a component $i$ at $t$ is executed by entering hard evidence to its action node $a_{i t}$, i.e., $\left\{a_{i t} \leftarrow r c\right\}$. This evidence does not affect the working probability of any other conditionally independent components at any periods. Because $a_{i t}$ 's are independent of each other. So every kind of system, especially when there are dependent components as in Figure 1, can be formulated with these action nodes.

Since actions are explicitly represented as probabilistic nodes in the DBN, the transition probability table for an independent component $i$ (in the example given in Figure $1, i \in\{A, C\}$ ) will have values of conditional probabilities $P\left(c_{i t} \mid c_{i, t-1}, a_{i t}\right)$ and is presented in Table 1.

Table 1. Transition probability table for an independent component i.


When the decision maker decides not to replace component $i$ in decision epoch $t$ and component $i$ is working in period $t-1, P\left(c_{i t}=w \mid c_{i, t-1}=w, a_{i t}=\right.$ $d n)=p_{i}$ where $0<p_{i}<1$ and $1-p_{i}$ is the stationary transition probability of failure for a working

component $i$. When $a_{t}=d n$ and component $i$ is nonworking in period $t-1$, it will still be non-working in the subsequent period $t$. So $P\left(c_{i t}=n w \mid c_{i, t-1}=\right.$ $\left.n w, a_{i t}=d n\right)=1$. When a component is decided to be replaced at $t$, i.e, $a_{i t}=r c, P\left(c_{i t}=w \mid c_{i, t-1}, a_{i t}=\right.$ $r c)=1$ no matter whether the component is working or not at $t-1$.

The transition probability table for the conditionally dependent component B will have values for $P\left(c_{B t} \mid c_{A t}, c_{B, t-1}, a_{B t}\right)$. These conditional probabilities will be constituted by also its parent components, in this case component A , in addition to ageing of the component itself and the replacement decision at $t$.

DBN representation allows inferring the reliability of the system and components in a given planning horizon and predicting the state of the system and components under different replacement schedules. In principle, our procedures can also work with other (possibly approximate) means of estimating the system reliability. However, since the computed system reliability is compared against a predetermined threshold, this needs to be performed with extra care. We insist on DBNs for exact inference on the system reliability. Furthermore, since all components and the system in the problem have discrete probability distributions, exact inference is possible. ${ }^{31}$

In the DBN formulation, replacements are performed by entering evidence to the actions. Let $\varepsilon$ denote the evidence list which is initially empty. Then all $a_{i t}$ 's are given hard evidence of " $d n$ ". When a component $i$ is chosen to be replaced in period $t$, this decision is executed by entering hard evidence to its action node and this information is added to the evidence list, i.e., $\varepsilon \leftarrow \varepsilon \cup\left\{a_{i t} \leftarrow r c\right\}$.

Reliability, ${ }^{35}$ in general, is defined as the probability that an item will perform its purpose adequately under given conditions for a given time interval. Let $R_{i t}$ be the estimated reliability of component $i$ in period $t$, so $R_{i t}=P\left(c_{i t}=w \mid \varepsilon\right)$ and let $R_{0 t}$ be the estimated reliability of system in period $t$, so $R_{0 t}=P\left(s_{i t}=w \mid \varepsilon\right)$.

There exists an ageing function $g_{i}$ for each component $i$ at each period given that the component is not replaced at that period. This function is constructed by the transition probability function of the
component. For the independent components given in Figure 1, $R_{i t}=g_{i}\left(R_{i, t-1}\right)$ and is computed as

$$
\begin{aligned}
R_{i t}= & P\left(c_{i t}=w \mid \varepsilon\right) \\
= & \sum_{c_{i, t-1}} P\left(c_{i t}=w \mid c_{i, t-1}, a_{i t}=d n, \varepsilon\right) P\left(c_{i, t-1} \mid \varepsilon\right) \\
= & P\left(c_{i t}=w \mid c_{i, t-1}=w, a_{i t}=d n, \varepsilon\right) R_{i, t-1}+ \\
& P\left(c_{i t}=w \mid c_{i, t-1}=n w, a_{i t}=d n, \varepsilon\right)\left(1-R_{i, t-1}\right)
\end{aligned}
$$

which is further simplified according to Table 1 as

$$
R_{i t}=p_{i} R_{i, t-1}
$$

Furthermore, there exists a function $f$ mapping component reliabilities $R_{i t}$ to system reliability $R_{0 t}$. This function expresses the causal relations between the components and the system. For the example given in Figure 1, system reliability can be expressed directly by the reliability of components $C$ and $B$, and indirectly by the reliability of component $A$. So $R_{0 t}=f\left(R_{C t}, R_{B t}\right)$ and this function can be constructed by the direct causal relations as follows:

$$
\begin{aligned}
R_{0 t}= & P\left(s_{t}=w \mid \varepsilon\right) \\
= & \sum_{c_{B t}} \sum_{c_{C t}} P\left(s_{t}=w \mid c_{C t}, c_{B t}, \varepsilon\right) P\left(c_{C t} \mid \varepsilon\right) P\left(c_{B t} \mid \varepsilon\right) \\
= & P\left(s_{t}=w \mid c_{C t}=w, c_{B t}=w, \varepsilon\right) R_{C t} R_{B t}+ \\
& P\left(s_{t}=w \mid c_{C t}=n w, c_{B t}=w, \varepsilon\right)\left(1-R_{C t}\right) R_{B t}+ \\
& P\left(s_{t}=w \mid c_{C t}=w, c_{B t}=n w, \varepsilon\right) R_{C t}\left(1-R_{B t}\right)+ \\
& P\left(s_{t}=w \mid c_{C t}=n w, c_{B t}=n w, \varepsilon\right)\left(1-R_{C t}\right)\left(1-R_{B t}\right)
\end{aligned}
$$

As the number of components in the system increases and the causal relations between the components and the system become more complex, the functions $g_{i}$ and $f$ become more difficult even to represent. That is why we use DBNs to formulate these transition probabilities and causal relations in the problem.

### 3.2. Threshold algorithm

In the maintenance problem, two important decisions are to be made: One is the time of replacement. The other is the decision of which component(s) to be replaced in that period. These two decisions should be made such that system reliability is

always guaranteed to be over a threshold value and the total number of replacements or total replacement cost is minimized. Our methodology is based on decoupling these decisions under the assumption of a predetermined threshold reliability. The decision of the replacement times is made sequentially by monitoring the next period when the estimated system reliability just falls below the given threshold. In other words, we defer a replacement decision as far as the threshold permits. This method leads to optimum replacement times for the maintenance problem of minimizing the total number of replacements under the following conditions:
(i) Estimated system reliability is an increasing function $f$ of the reliability of all components. That is, as $R_{it increases} R_{0 t}=f\left(R_{1 t}, R_{2 t}, \cdots, R_{i t}, \cdots\right)$ also increases.This is valid in all coherent systems.
(ii) Components age with a decaying function $g_{i t}$ unless they are replaced where $g_{i t}$ is the transition probability function of component $i$ at period $t$ which may be stationary or nonstationary. That is $R_{i t}=g_{i, t-1}\left(R_{i, t-1}\right)$ and $R_{i t}<R_{i, t-1}$ for all $1<t \leqslant T$.

Furthermore, this method also leads to optimum replacement times for the maintenance problem of minimizing the total replacement cost in a given planning horizon provided that replacement costs of components are stationary.

The following proposition states that given a component replacement schedule, by keeping to the component sequence and realizing the replacements when the estimated system reliability just falls below the given threshold, one finds at least the same number of replacements. The proposition is valid in all systems whether there are conditionally dependent components or not, provided that the above conditions are satisfied. The proof is given subsequently.

Proposition 1. For a given finite horizon $T$, assume there exists an optimal replacement schedule $R S$ such that it makes at least one replacement when the estimated system reliability is above the threshold. Let RS' be another replacement schedule which is constructed from RS such that all replacements are performed when the estimated system reliability just falls below the threshold and it has the same replacement sequence of components with RS. Both
schedules are feasible with respect to the threshold constraint. Under the above conditions, RS' is at least as good as RS in minimizing total number of replacements or total replacement cost when costs are stationary.

Proof. It is required to show that in the worst case RS' will have the same number of replacements as with RS in a given planning horizon. In the best case it will have less number of replacements by discarding the last one(s). In this way total cost can also be improved by reducing the number of replacements.
![img-1.jpeg](img-1.jpeg)

Fig. 2. An example for RS and RS'.

Figure 2 shows an example of RS and RS' where, in the graph, $L$ is the predetermined threshold reliability that the system should never fall below and $T$ is the planning horizon. The peak points in the graph are the epochs where replacement decisions are made. When a component is replaced, its effect on the system reliability is seen immediately at that period because of assumption (iv) stated in Section 2. Let's assume only one replacement of RS, $m^{\text {th }}$ replacement, is performed when the estimated system reliability is above the threshold value $L$ whereas others are made exactly at periods when the estimated system reliability falls just below the threshold.

Let $l \in\{1, \cdots, Z\}$ denote the replacement sequence index where $Z$ is the number of total replacements of RS. $t_{l}$ and $t_{l}^{\prime}$ are the periods of the $l^{\text {th }}$ replacement of RS and RS' respectively. Eq. (4) shows how replacement periods of RS' are derived consec-

utively given the evidence $\varepsilon$ :

$$
t_{l}^{\prime}=\min _{t_{l-1}^{\prime} \leqslant t \leqslant T}\left\{t: P\left(s_{t}=w \mid \varepsilon\right)<L\right\}
$$

Given a planning horizon $T$, the last replacement epoch of RS is $t_{Z}$ and $t_{Z} \leqslant T$. However, $t_{Z}^{\prime}$ of RS' may be outside of $T$, as in this example, because $t_{Z} \leqslant t_{Z}^{\prime}$. In this case, there is no need to do the replacements $l$ such that $t_{l}^{\prime}>T$. Hence total replacement number of RS' reduces. Let $Z^{\prime}$ be the replacement number of RS', it can be computed as follows:

$$
Z^{\prime}=\max _{1 \leqslant l \leqslant Z}\left\{l: t_{l}^{\prime} \leqslant T\right\}
$$

Eq. (5) reveals that $Z^{\prime} \leqslant Z$. So when the objective is to minimize total number of replacements or total replacement cost when costs are stationary along the planning horizon, given any replacement schedule, the objective function can always be improved or at least remains the same by deferring all the replacements to the periods computed as in Eq. (4).

The result of Proposition 1 motivates the following "Threshold Algorithm" within the framework of DBN formulation described in Section 3.1. In the algorithm, $e f_{i k}$ is an efficiency measure of component $i$ in period $t$ used to determine the most effective component to replace when a replacement is planned.
(i) Initialize $t=1$
(ii) Infer system reliability $P\left(s_{t^{\prime}}=w \mid \varepsilon\right) t \leqslant t^{\prime} \leqslant T$
(iii) If $P\left(s_{t^{\prime}}=w \mid \varepsilon\right) \geqslant L \forall t^{\prime}$, then stop.
(iv) Else find the replacement period, $k=\min _{t \leqslant t^{\prime} \leqslant T}\left\{t^{\prime}: P\left(s_{t^{\prime}}=w \mid \varepsilon\right)<L\right\}$
(v) Do replacement(s) for period $k$
(a) Initialize remaining components list, $I^{\prime} \leftarrow I$
(b) Calculate $e f_{i k} \forall i \in I^{\prime}$
(c) Select the component to replace, $i^{*}=\arg \max \left\{e f_{i k}, i: i \in I^{\prime}\right\}$
(d) Update evidence list, $\varepsilon \leftarrow \varepsilon \cup\left\{a_{i^{*} k} \leftarrow r c\right\}$
(e) Update remaining components list, $I^{\prime} \leftarrow I^{\prime} \backslash\left\{i^{*}\right\}$
(f) If $P\left(s_{k}=w \mid \varepsilon\right)<L$ then continue with (v.b)
(g) Else update $t=k+1$
(vi) If $t>T$, then stop.
(vii) Else continue with step (ii)

In step (v.b) of the Threshold Algorithm, one of the component selection approaches to be described
in Section 3.3 is performed to calculate $e f_{i k}$. Each approach uses a different way to compute efficiency scores of components.

### 3.3. Component selection approaches

In Section 3.2, by Proposition 1, we prove that the decisions of when and what to replace can be decoupled under the existence of a predetermined threshold reliability and that performing replacements at periods when the system reliability just falls below the threshold value assures optimum replacement times when the objective is to minimize total number of replacements. Furthermore, this policy minimizes total replacement cost if components have stationary replacement costs along the planning horizon.

So the next step is to decide what to replace at a replacement epoch. At the time of replacement, the decision of which component(s) to be replaced is an important issue since it affects future system reliability and consequently the next time to do a replacement. After a component is replaced, if this is not enough to increase the system reliability above the threshold, another component is selected, among the remaining components, to be replaced at that period. This process continues until the threshold constraint is satisfied at that period. We assume that in the worst case all components are replaced at a replacement epoch to keep the estimated system reliability above the threshold at that period. Hence if one determines the component(s) to replace optimally at a replacement epoch, then the whole problem can be solved optimally.

We propose four efficient heuristic approaches to select the component to be replaced to minimize the total number of replacements in a given planning horizon. The first two of them are based on fault diagnosis techniques whereas the next two focus on the improvement of system reliability. We, then propose the cost focused versions of these four approaches to minimize the total cost of replacements in a given planning horizon.

### 3.3.1. Fault effect myopic approach (FEM)

Criticality of the system components with respect to current possible system failure is analyzed. Like in

decision-theoretic troubleshooting, ${ }^{2}$ posterior probabilities of components given the system state are used as efficiency measures of components in each period when a replacement is planned. Efficiency measure is calculated as in Eq. (6). It is the probability of the component being faulty given the system is faulty in a period. This posterior probability is calculated by entering evidence that the system has failed and employing an inference algorithm only once. Note that it is not known whether the system is really faulty in that period. All we know that its reliability has fallen under the threshold value. So we assume as if it has failed and use this information to determine the component which explains this failure best.

$$
e f_{i t}^{F E M}=P\left(c_{i t}=n w \mid \varepsilon \cup\left\{s_{t}=n w\right\}\right)
$$

### 3.3.2. Fault effect look-ahead approach (FEL)

Criticality of the system components with respect to future possible system failures is analyzed. Hence it is similar to FEM, but FEL takes into account future information which can be transmitted by the transition probabilities of components. This is done by entering evidence to the system node from $t+1$ to $T$ as $s_{t+1: T}=n w$. In other words, we assume the system will fail in all periods after the period $t$.

$$
e f_{i t}^{F E L}=P\left(c_{i t}=n w \mid \varepsilon \cup\left\{s_{t+1: T}=n w\right\}\right)
$$

where $s_{t+1: T}$ denotes $s_{t+1}, \ldots, s_{T}$.

### 3.3.3. Replacement effect myopic approach (REM)

The effect of single component replacement to system reliability is analyzed for each component. At a replacement time, the component whose replacement increases system reliability most is chosen to be replaced. For each component selection process, this approach employs inference as much as the number of remaining components (those that have not been replaced at that period).

$$
e f_{i t}^{R E M}=P\left(s_{t}=w \mid \varepsilon \cup\left\{a_{i t} \leftarrow r c\right\}\right)-P\left(s_{t}=w \mid \varepsilon\right)
$$

### 3.3.4. Replacement effect look-ahead approach (REL)

The effect of single component replacement to the next replacement time is analyzed for each component. At a replacement time, the component whose replacement holds system reliability above the threshold most is chosen to be replaced. By this way, the next replacement time is deferred as much as possible. In case of tie, the component whose replacement makes the system reliability highest in the next replacement time is chosen. Like in REM, for each component selection process, this approach also employs inference as much as the number of remaining components. Let $t^{\prime}$ be the periods where the system reliability is less than the threshold.
$e f_{i t}^{R E L}=\min _{t \leqslant t^{\prime} \leqslant T}\left\{t^{\prime}: P\left(s_{t^{\prime}}=w \mid \varepsilon \cup\left\{a_{i t} \leftarrow r c\right\}\right)<L\right\}$.

### 3.3.5. Cost focused versions of the approaches

The previous proposed component selection methods consider minimizing the total number of replacements in a given planning horizon. To account for minimizing the total replacement cost in a given horizon, slight modifications of the methods are proposed. Let FEMc, FELc, REMc and RELc be the cost included versions of the component selection approaches FEM, FEL, REM and REL respectively. Let $\pi_{i}$ denote the replacement cost of component $i$. Efficiency of FEMc, FELc and REMc are computed as in Eq. (10-12) respectively.

$$
\begin{gathered}
e f_{i t}^{F E M c}=\frac{P\left(c_{i t}=n w \mid \varepsilon \cup\left\{s_{t}=n w\right\}\right)}{\pi_{i}} \\
e f_{i t}^{F E L c}=\frac{P\left(c_{i t}=n w \mid \varepsilon \cup\left\{s_{t+1: T}=n w\right\}\right)}{\pi_{i}} \\
e f_{i t}^{R E M c}=\frac{P\left(s_{t}=w \mid \varepsilon \cup\left\{c_{i t} \leftarrow w\right\}\right)-P\left(s_{t}=w \mid \varepsilon\right)}{\pi_{i}}
\end{gathered}
$$

RELc uses the same efficiency measure as with REL which is given in Eq. (9). However, in case of tie, the component with the smallest replacement cost is chosen. By this slight modification, we improve the REL method to account for also the replacement costs of components while preserving the

effort to keep the total number of replacements as small as possible.

## 4. Computational study

The example given in Figure 1 is of a simple system consisting of three components. A more complex dynamic test problem is generated from the well known static auto diagnosis problem ${ }^{3}$ in decision theoretic troubleshooting environment. We call this test problem "Dynamic Auto Problem".

The Threshold Algorithm is coded in Matlab and uses the Bayes Net Toolbox (BNT) ${ }^{36,37}$ to represent the causal and temporal relations, and to perform inference. There are a few exact DBN inference algorithms available in the literature. ${ }^{31}$ In this study, we use dynamic junction tree inference algorithm ${ }^{37}$ which applies the static junction tree algorithm ${ }^{33}$ to pairs of neighbouring slices at a time.

We compare the performances of the four component selection approaches and their cost focused versions on the Dynamic Auto Problem (DAP). All procedures and the test problem are available online. ${ }^{30}$ Statistical analysis are performed in Minitab.

### 4.1. DBN representation of DAP

In the BN representation of the static auto diagnosis problem, Engine-St is the problem defining node meaning Engine Start. In DAP however we make this node more generic and denote it with $s$ representing the system node. The auto diagnosis problem is made dynamic by making the components ageing in time under the following assumptions: The automobile is assumed to be never out of gas. That is why Gas and Gas Gauge are excluded in the dynamic model. It is presumed that the decision maker cannot get any observations. So Radio and Lights are also excluded. Since the model is dynamic, battery age is already handled by the temporal variable Battery which is subject to ageing like the other components. So Battery age is also excluded. Starter, Fan Belt, Alternator, Battery, Distributor, Spark Plugs, Fuel Pump and Fuel Line are taken as the ageing components that are assumed to have constant transition probabilities. The resulting DBN is
shown in Figure 3 for two time slices $t$ and $t+1$.
![img-2.jpeg](img-2.jpeg)

Fig. 3. DBN representation of DAP.
The constant transition probabilities of working $\left(p_{i}\right)$ and replacement cost values $\left(\pi_{i}\right)$ of the components are consulted to an authorized service of an automobile company for a moderate car type and are given in Table 2. Planning horizon and threshold reliability are taken as 100 months and 0.50 respectively.

Table 2. DAP data.


DAP is solved for two cases: to minimize total number of replacements (DAP-TR) and to minimize total cost of replacements (DAP-TC). The Threshold Algorithm described in Section 3.2 is used to solve both cases with the component selection approaches proposed in Section 3.3. Performances of the approaches are analyzed regardless of the value of the threshold reliability and the replacement cost of Spark Plugs for both cases.

Table 3. DAP-TR results when threshold is 0.50 .


Table 4. DAP-TR results when threshold is 0.75 .


### 4.2. Solution of DAP-TR

We solve DAP-TR using the Threshold Algorithm proposed in Section 3.2 with FEM, FEL, REM and REL component selection approaches one by one. In order to compare the performances of the approaches with a baseline method, we also solve the problem again with the Threshold Algorithm, but select the component to replace randomly and call this method "Random" approach.

Table 3 shows the results of DAP-TR with FEM, FEL, REM, REL and random component selection methods. "TCost" and "TRep" stand for total cost and total number of replacements of the solution. ' $\mathrm{T}(\mathrm{sec})$ " shows the solution time in seconds. The remaining columns belong to the components of DAPTR and show the number of replacements of each. Although this table belongs to the results of DAP where the objective is to minimize total number of replacements, we also report the total replacement cost calculated according to the replacement plans of components and their costs given in Table 2 to compare with the results of DAP-TC in Section 4.3.

As its name implies, the random method selects the component to be replaced randomly at a replacement time. 50 replications are performed for the random method and the average solution with its standard deviation and the average solution time are reported in the table. Since the objective is to minimize total number of replacements, REL finds the
best solution although its solution time is the highest. This is because REM and REL perform more inferences than FEM and FEL to determine the component to be replaced. FEM and REM results are nearly the same except the number of replacements of Spark Plug. Replacement decisions of FEM and REM are similar to the results of REL. Although the total number of replacements found by FEL is not so different than the ones found by FEM, REM and REL, its distribution among components is significantly different. The solution of the random method is the worst and its total number of replacements is significantly very far from the solution of others. In addition to this, computation time of FEM and FEL is very close to the average computation time of the random method.

We analyze the sensitivity of the results of DAPTR to the threshold reliability. In Section 4.1, threshold is decided to be taken as 0.50 whereas now it is increased to 0.75 arbitrarily. Table 4 shows the results of DAP-TR when the threshold is increased to 0.75 for the four component selection approaches and the random method. To keep the estimated system reliability above a higher threshold, total number of replacements in all approaches increase as expected. Note that TRep values are all greater than 100 , because there are some replacement epochs where more than one component are selected to replace to satisfy the threshold constraint. Among all

methods, REL finds the minimum total number of replacements. Again random method is the worst with respect to total number of replacements and its solution is significantly far from the solution of FEM, FEL, REM and REL.

In order to see whether there exists significant difference among the performance of the methods proposed for DAP-TR or not, we perform complete block design to eliminate the effect of threshold on the statistical comparisons among the performance of the methods. The response variable is TRep and different levels of threshold are the blocks in the experiment. The block experimental design is given in Table 5 and the resulting analysis of variance (ANOVA) is presented in Table 6. Since P-Value of the methods is 0.102 , at the 0.05 level of significance, there exists no strong evidence that the performance of the methods differ on minimizing the total number of replacements.

Table 5. Block design for DAP-TR (threshold is block).


Table 6. ANOVA for DAP-TR (threshold is block).


### 4.3. Solution of DAP-TC

We solve DAP-TC using the Threshold Algorithm proposed in Section 3.2 with FEMc, FELc, REMc and RELc component selection approaches one by one. In order to compare the performances of the approaches with a baseline method, we use the results of the Random method introduced in Section 4.2 which selects the component to replace randomly at periods where replacements are decided to be performed.

Table 7 shows the results of DAP-TC with FEMc, FELc, REMc, RELc and random compo-
nent selection methods. When total cost is tried to be minimized, there is a significant increase in the number of replacements of Spark Plug since it is the cheapest component and it has the smallest $p_{i}$ value. FELc, REMc and RELc improve total cost while FEMc does not when compared with the total cost of their corresponding results of DAP-TR given in Table 3. Although FELc and REMc improve total cost, they cause a significant increase in the total number of replacements. RELc finds the best result with respect to total cost and in addition this result has the least total number of replacements. In fact, RELc is a slight modification of REL improving the component selection procedure to account for also component replacement costs. That is why the total number of replacements it finds is still reasonable. Like in the DAP-TR, the solution of the random method is the worst and its total cost is significantly very far from the solution of others.

### 4.3.1. Sensitivity of DAP-TC to threshold

We analyze the sensitivity of the results of DAP-TC to the threshold reliability. In Section 4.1, threshold is decided to be taken as 0.50 whereas now it is increased to 0.75 arbitrarily as in Section 4.2. Table 8 shows the results of DAP-TC when the threshold is increased to 0.75 for the four component selection approaches and the random method. To keep the estimated system reliability above a higher threshold, total cost of replacements also increase as expected. All methods find less cost when compared with the results of their respective efficiency measures in DAP-TR given in Table 4. RELc is the best approach when component costs are concerned and in addition it has the least number of replacements. All cost included methods plan to replace Spark Plug more frequently than the other components as in the case when the threshold is 0.50 . Furthermore, the solution of the random method is again the worst with respect to total cost of replacements and its total cost is significantly far from the solution of FEMc, FELc, REMc and RELc.

In order to see whether the performance of the methods proposed for DAP-TC significantly differ or not, we perform complete block design to eliminate the effect of threshold on the statistical com-

Table 7. DAP-TC results when threshold is 0.50 .


Table 8. DAP-TC results when threshold is 0.75 .


parisons among the performance of the methods. The response variable is TCost and different levels of threshold are the blocks in the experiment. The block experimental design is given in Table 9 and the resulting ANOVA output is shown in Table 10. Since P-Value of the methods is 0.000 , at the 0.05 level of significance, there is strong evidence that the performance of the methods differ on minimizing the total cost.

Table 9. Block design for DAP-TC (threshold is block).


Table 10. ANOVA for DAP-TC (threshold is block).


Since we reject the null hypothesis that the performance of the methods are indifferent by the ANOVA result given in Table 10, the next step is to determine the methods which really differ with a post-hoc analysis. Tukey's test ${ }^{38}$ is used to test all pairwise mean comparisons. The Tukey proce-
dure controls the overall family error rate (of all pairwise mean comparisons) at the selected significance level.

Results of Tukey simultaneous tests for comparing pairwise means of method performances on DAP-TC are given in Table 11. The first column illustrates the direction of the pairwise test. The second column gives the difference of the means of the methods that are tested in the direction stated in the first column. Finally the last column gives the adjusted P-value of the tests. At the 0.05 level of overall significance, tests having adjusted P -value $<0.05$ are rejected concluding that there exists significant difference between pairs. In this case, if the difference of means has positive sign, then the method stated first in the test, has significantly greater cost than the second method that is subtracted in the pairwise test.
Table 11. Tukey Test Results for DAP-TC (threshold is block).


Hence, according to Table 11, performance of FEMc, FELc and REMc are indifferent whereas per-

Table 12. Results of DAP when $\pi_{S P}$ increases to 5.


formance of RELc is significantly different from the performance of others. As a result, we can conclude that whatever the threshold value is, RELc gives significantly less total replacement cost than the other methods under the current replacement cost structure of components at a 0.05 level of overall significance.

### 4.3.2. Sensitivity of DAP-TC to cost

Replacement costs of components are also other factors that may affect the performance of the component selection methods. According to Table 2, Spark Plug is the cheapest component and it has the minimum $p_{i}$ among all components. That is why, in Table 7 all methods except the random one plan to replace Spark Plug more frequently than the other components. In order to see the sensitivity of the approaches to the costs of components, we increase $\pi_{S P}$ from 1 to 5 .

Table 12 shows the results of DAP when $\pi_{S P}$ increases to 5 and threshold is kept at 0.50 for the four component selection approaches and their cost included versions. Results of FEM, FEL, REM and REL are the same as in Table 3 except TCost value. In the solutions of FEMc, FELc, REMc and RELc, number of replacements of Spark Plug decreases sharply when compared with the results in Table 7, and all methods prefer to replace Battery instead. This is because Battery becomes the cheapest component with a small $p_{i}$ after increasing $\pi_{S P}$ to 5 . RELc is the only method which improves the total cost of DAP-TC when $\pi_{S P}=5$.

To eliminate the effect of the cost of Spark Plug on the statistical comparisons among the performance of the methods on DAP-TC, we perform
complete block design experiment where different values of costs that Spark Plug can take are considered as blocks. The response variable is TCost and the block experimental design with the observed TCost values is given in Table 13. The resulting ANOVA output is shown in Table 14. P-Value of the methods is 0.000 . So, at the 0.05 level of significance, there is strong evidence that the performance of the methods differ on minimizing the total cost.

Table 13. Block design for DAP-TC ( $\pi_{S P}$ is block).


Table 14. ANOVA for DAP-TC ( $\pi_{S P}$ is block).


Since we reject the null hypothesis that the performance of the methods are indifferent by the ANOVA result given in Table 14, we perform Tukey's test as a post-hoc procedure to test all pairwise mean comparisons so that we determine the methods which really differ. Results of Tukey simultaneous tests for comparing pairwise means of method performances on DAP-TC are given in Table 15 which has a similar structure with Table 11. At the 0.05 level of overall significance, tests having adjusted P-value $<0.05$ are rejected concluding that there exists significant difference between pairs.

According to Table 15, when the threshold is 0.50 , whatever the replacement cost of Spark Plug is, performance of REMc and RELc are indifferent, and they are significantly better than performances of FEMc and FELc which are pairwise indifferent at a 0.05 level of overall significance.

Table 15. Tukey Test Results for DAP-TC ( $\pi_{S P}$ is block).


## 5. Conclusion

We develop an algorithm for determining replacement policies of a complex dynamic system with unobservable components within the framework of DBN representation. First, the next replacement period is determined and then the components to be replaced at that period are determined sequentially. We propose to perform replacements at periods when the system reliability just falls below the threshold. We prove that under the existence of a predetermined threshold, this method assures optimum replacement times in minimizing total number of replacements. Furthermore, this policy minimizes total replacement costs if components have stationary replacement costs along the planning horizon.

Using this policy, we propose four alternative procedures that differ in their orientation and information use to select the components to be replaced at a replacement epoch to minimize total number of replacements. When the objective is to minimize total replacement cost, these approaches are slightly modified by taking into account also the replacement costs of components.

All component selection methods are tested on a relatively complex problem which is generated from the auto diagnosis problem in the literature. The results of proposed algorithms are also compared against the solution of a random method. All four component selection measures and their cost fo-
cused versions perform significantly better than the random method both in terms of total number of replacements and total cost. This is some evidence that the proposed methods perform reasonably well. However, since a comparison against an optimal replacement policy or other heuristic approaches are not available, we provide our example problem and algorithms on-line for other researchers to perform tests on them.

Performance of the methods under various threshold and cost levels are also analyzed. Results show that whatever the threshold value is, there exists no significant difference among the four methods in minimizing total number of replacements. However when the objective is to minimize total replacement cost, the cost focused versions of the four methods do differ. Under the given threshold value, whatever the cost of the most sensitive component is, the reliability based efficiency measures RELc and REMc perform significantly better than the failure based ones FELc and FEMc in minimizing total replacement cost. Furthermore, under the given cost structure whatever the threshold value is, RELc performs significantly better than the others in minimizing total replacement cost.
