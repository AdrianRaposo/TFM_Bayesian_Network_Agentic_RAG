# Article 

## Probability-Based Wildfire Risk Measure for Decision-Making

Adán Rodríguez-Martínez * and Begoña Vitoriano (D)<br>Interdisciplinary Mathematics Institute, Complutense University of Madrid (UCM), 28040 Madrid, Spain; bvitoriano@mat.ucm.es<br>* Correspondence: adanro01@ucm.es

Received: 6 March 2020; Accepted: 5 April 2020; Published: 10 April 2020


#### Abstract

Wildfire is a natural element of many ecosystems as well as a natural disaster to be prevented. Climate and land usage changes have increased the number and size of wildfires in the last few decades. In this situation, governments must be able to manage wildfire, and a risk measure can be crucial to evaluate any preventive action and to support decision-making. In this paper, a risk measure based on ignition and spread probabilities is developed modeling a forest landscape as an interconnected system of homogeneous sectors. The measure is defined as the expected value of losses due to fire, based on the probabilities of each sector burning. An efficient method based on Bayesian networks to compute the probability of fire in each sector is provided. The risk measure is suitable to support decision-making to compare preventive actions and to choose the best alternatives reducing the risk of a network. The paper is divided into three parts. First, we present the theoretical framework on which the risk measure is based, outlining some necessary properties of the fire probabilistic model as well as discussing the definition of the event 'fire'. In the second part, we show how to avoid topological restrictions in the network and produce a computable and comprehensible wildfire risk measure. Finally, an illustrative case example is included.


Keywords: wildfire management; risk measure; probability; Bayesian networks; decision-making; prescribed burns; firebreak location

## 1. Introduction

Forest fires are an annual occurrence in many parts of the world, affecting the population and environment of the adjacent areas with significant economic and ecological losses, and often, human casualties. The number and size of forest fires have increased over time, exceeding the firefighters' response capacity [1]. In the last few years, big fires have taken a global relevance: Portugal (2017) 44,969 ha and 66 fatalities, California (2018) 101,287 ha and 124 fatalities, and Australia (2019) 18,600,000 ha approx. and 34 fatalities (until 6 March 2020).

From the firefighters' perspective, Ref. [2] suggests that the abandonment of farmland and reduced grazing have led to an increase in wildland areas, and they address the issue of how extinguishing small fires can increase the size of future fires.

A considerable amount of literature has been published on the use of applied mathematics to tackle the problem of wildfires. Many of these studies are focusing on subjects such as behavior and spread of fire [3], fire suppression [4], evacuation in case of risk [5-7], and location of firebreaks [8,9], for example. For this work, we focus on those articles that deal with the issue of prevention and mitigation of forest fires. In this sense, Ref. [10] is an analysis of operational research challenges in forestry where 33 open problems are formulated, being Problem 20 formulated as follows:
'How can we develop tractable models that can be used to help determine when and where to implement fuel treatments on large flammable forest and wildland landscapes?'

Fuel treatments include mainly fuel management and location of firebreaks. Fuel management is one of the most important measures for preventing large scale fires. This practice consists of reducing the amount of fuel through the application of treatments such as prescribed fire or mechanical thinning [8,11]. Ref. [12] addresses the question of how fuel management should be used over time to reduce wildfire impact. The problem with spatial and temporal dimensions is solved by using a mixed-integer linear programming model. In a later study, Ref. [13] take additional considerations into account for preserving habitat quality. Finally, to obtain robust models against uncertainty, as can be seen for instance in [14] for other fields, stochasticity is included in the model. The complete study can be found in [15].

Firebreak location is a very extended activity to provide safe and accessible places to fight against fires. Effectiveness of firebreaks has been studied extensively in many territories [9,16]. The right position where those firebreaks should be located is a very complex problem. Ref. [8] shows how different configurations of firebreaks affect fire propagation.

The purpose of this paper is to obtain a spatial probabilistic measure for wildfire risk, suitable to compare different landscape configurations after applying fuel treatments. Paper [17] entitled 'Probability-based models for estimation of wildfire risk', presents a statistical perspective to solve this problem. They use a partition of the landscape for estimating the probability of fire in each $1 \mathrm{~km}^{2}$ pixel. For every pixel, two different events are defined: ignition or small fire (between 0.04 ha and 40.5 ha ) and large fire (greater than 40.5 ha). Finally, Ref. [17] proposes estimating the probability of ignition and the probability that a small fire will become a large fire using a logistic regression based on several fire indicators. The aim of that work is to estimate the number of large fires to support tactical decisions to reduce this number.

We propose a network representation of the landscape considering fire as a phenomenon that can be spread out through the land instead of considering it as a one-off event. In a recent study, Ref. [18] presents a methodology used by Catalan Fire and Rescue Service based on modelling landscape with a network. A case study of Odena (Spain) is shown where the landscape is divided into 23 sectors (Figure 1). Considering two wind scenarios, they define main connections between sectors as 'extreme fire behavior', 'intense fire behavior' or 'low fire behavior'. The resulting scheme is the starting point to plan tactical actions on the landscape.

The aim of this work is to establish a mathematical basis to be able to compute fire risk and to be optimized into decision-making models. We focus on the definition of fire risk as well as its calculations in realistic dimensions.

Ref. [19] models wildfires and [20] models fire spread in buildings; both develop mathematical tools for computing fire probabilities in a network. However, the theoretical analysis presented in this paper shows some non-trivial properties of the probabilistic space that were not taken into account.

The second section of this paper is a theoretical discussion about the definition of fire in a probabilistic model and the issue of computing the probability of fire. In Section 2.1, the working space is defined as the product probabilistic space, and the problem of defining 'fire' in this space is addressed. In Section 2.2, it is shown that under some conditions, the probabilistic behavior of fire conforms to a Bayesian network. In the second part, Section 3, a methodology to generalize the previous theoretical results to be applied in a real case is presented. Finally, we use a simulated case study provided by [21] to illustrate the application of the proposed method for decision-making.

# 2. Fire Probability 

A tool measuring the risk that takes into account fire connectivity can be helpful to decide which changes on the landscape are more efficient to reduce fire risk. Also, an estimation of the effectiveness of every action as an expected value can be used to justify the investment in preparedness.

Risk is a broad concept that can be defined in different ways. In our context, we will define fire risk as the expected losses due to bush fires in a determined landscape for a limited period of time. Computing this value implies being able to compute probabilities of burning, which will be done

through a representation of the landscape as a network. Nodes represent homogeneous sectors in which we divide the territory and arcs represent the probability of fire spread among those parts. The first issue is to compute the probability of a node burns, assumed known the ignition probabilities in the nodes and the spread probabilities through the arcs.

1st assumption: Landscape can be divided into homogeneous areas: sectors. A sector is a portion of land where in case of a fire, the only possible way of extinguishing it will be within its boundaries (Figure 1).

This assumption is the cornerstone of the methodology presented. It is a usual simplification taken both by researchers and firefighters [12,13,17-19,22]. Although fire and landscape are naturally seen as a continuous phenomenon, preventive actions used to be taken within finite set of possible places and a network is an appropriate framework for these decisions.
![img-0.jpeg](img-0.jpeg)

Figure 1. Segmentation of the area of interest to identify tactical objectives [18].

# 2.1. Probabilistic Network Model 

1st assumption allows us to work with a network representing the landscape. We denote the network as $G=(N, A)$, with

$$
\begin{aligned}
& N=\left\{n_{1}, \ldots, n_{m}\right\} \\
& A=\left\{a_{i j}=\left(n_{i}, n_{j}\right): n_{i}, n_{j} \in N\right\}, \quad \text { with }|A|=p
\end{aligned}
$$

being $N$ the set of all nodes representing sectors of the landscape and $A$ the set of directed edges connecting adjacent sectors.

Random experiments on nodes will be related to fire ignition (Fire ignition is defined as a fire greater than 0.04 ha [17]). Elementary events for each node will be 'there is ignition' and 'there is not ignition', defining the following probability spaces:

$$
\begin{array}{lll}
\square_{n_{i}}=\left\{i g_{i}, i g_{i}^{c}\right\}, & i=1, \ldots, m \\
i g_{i}: \text { ignition in node } n_{i}, & i=1, \ldots, m \\
\mathscr{A}_{n_{i}}=\mathscr{P}\left(\square_{n_{i}}\right), & i=1, \ldots, m \\
p_{n_{i}}: \quad \mathscr{A}_{n_{i}} & \longrightarrow \mathbb{R}, & i=1, \ldots, m \\
\varnothing & \longrightarrow 0 & & \\
\left\{i g_{i}\right\} & \longrightarrow & p_{n_{i}}\left(\left\{i g_{i}\right\}\right) \\
\left\{i g_{i}^{c}\right\} & \longrightarrow & 1-p_{n_{i}}\left(\left\{i g_{i}\right\}\right) \\
\square_{n_{i}} & \longrightarrow & 1 &
\end{array}
$$

In the same way, elementary events for each edge will be ' $a_{i j}$ is able to spread fire' and ' $a_{i j}$ is not able to spread fire':

$$
\begin{aligned}
& \Omega_{a_{i j}}=\left\{s p_{i j}, s p_{i j}^{c}\right\}, \quad a_{i j} \in A \\
& s p_{i j}: a_{i j} \text { is able to spread fire, } \\
& a_{i j} \in A \\
& a_{a_{i j}}=\mathscr{P}\left(\Omega_{a_{i j}}\right), \\
& p_{a_{i j}}: \quad \mathscr{A}_{a_{i j}} \quad \longrightarrow \mathbb{R}, \quad a_{i j} \in A \\
& \varnothing \quad \longrightarrow 0 \\
& \left\{s p_{i j}\right\} \quad \longrightarrow \quad p_{a_{i j}}\left(\left\{s p_{i j}\right\}\right) \\
& \left\{s p_{i j}^{c}\right\} \quad \longrightarrow \quad 1-p_{a_{i j}}\left(\left\{s p_{i j}\right\}\right) \\
& \Omega_{a_{i j}} \quad \longrightarrow \quad 1
\end{aligned}
$$

With this definition, if $n_{i}$ burns and $a_{i j}$ 'is able to spread fire', then $n_{j}$ also burns. Arc spread capability is related mainly with topographical and meteorological conditions (especially those related with wind directions). Estimation of $i g_{i}$ and $s p_{i j}$ probabilities will be discussed in Section 3 but it is not part of the current work.

Time period considered will be long enough for characterizing a global risk measure, but short enough so that a cell does not burns twice during the period (no regeneration).

Next assumption is, at this point, a technical necessity to work with the probabilistic space. The compatibility of this assumption with reality will be discussed in Section 3.

2nd assumption: independence between nodes ignitions and arc spread capabilities.
Hence, with this assumption, the probabilistic space on the network model is the product space:

$$
\begin{aligned}
& \Omega=\Omega_{n_{1}} \times \cdots \times \Omega_{n_{m}} \times \Omega_{a_{i_{1} j_{1}}} \times \cdots \times \Omega_{a_{i_{p} j_{p}}} \approx\{0,1\}^{m+p} \\
& a=a_{n_{1}} \times \cdots \times a_{n_{m}} \times a_{a_{i_{1} j_{1}}} \times \cdots \times a_{a_{i_{p} j_{p}}} \\
& p: \quad \text { a } \frac{\mathbb{R}}{\left(w_{1}, \ldots, w_{m}, t_{i_{1} j_{1}}, \ldots, t_{i_{p} j_{p}}\right) \quad \mapsto \quad \prod_{n_{i} \in N} p_{n_{i}}\left(w_{i}\right) \cdot \prod_{a_{i j} \in A} p_{a_{i j}}\left(t_{i j}\right), \quad \forall w_{i} \in a_{n_{i}}, t_{i j} \in a_{a_{i j}}}
\end{aligned}
$$

For notational simplicity, we will denote, in the following, the next (non-elementary) events:

$$
\begin{array}{llll}
\Omega_{n_{1}} \times \cdots \times\left\{i g_{i}\right\} \times \cdots \times \Omega_{n_{m}} \times \Omega_{a_{i_{1} j_{1}}} \times \cdots \times \Omega_{a_{i_{p} j_{p}}} & \subset & \Omega & \text { as } & i g_{i}, \quad \text { and } \\
\Omega_{n_{1}} \times \cdots \times \Omega_{n_{m}} \times \Omega_{a_{i_{1} j_{1}}} \times \cdots \times\left\{s p_{i_{p} j_{k}}\right\} \times \cdots \times \Omega_{a_{i_{p} j_{p}}} & \subset & \Omega & \text { as } & s p_{i_{k} j_{k}}
\end{array}
$$

Also, $c_{i j}=\left\{a_{i l_{1}}, a_{l_{1} l_{2}}, \ldots, a_{l_{p} j}\right\} \subset A$ will be a 'path from $n_{i}$ to $n_{j}$ ' and we denote the set of all paths from $n_{i}$ to $n_{j}$ with $C_{i j}$.

Ones the probability basis for the model has been established, in the following part we will focus on how to define fire event and how to compute its probability. In both cases, we have two options: one simple but computationally intractable and another one non-trivial but computable for real size networks.

Definition 1. The event $F_{i}$ : ' $n_{i}$ burns', can be defined as
' $n_{i}$ burns if there is ignition there or if fire is coming from another node where there is ignition through a path connecting it with $n_{i}$ '.

In terms of elementary events, this is

$$
F_{i}=i g_{i} \cup \bigcup_{\substack{j=1 \\ j \neq i}}^{m}\left(i g_{j} \cap \bigcup_{c_{j i} \in C_{j i}}\left(\bigcap_{a_{k l} \in c_{j i}} s p_{k l}\right)\right)
$$

Please note that paths may not be disjoint, especially in a topography network. From this definition is possible to compute $p\left(F_{i}\right)$ with a method based on the Law of total probability. We consider the partition over $\left(\Omega_{a_{i j j_{1}}} \times \cdots \times \Omega_{a_{i p / j}}\right)$, i.e.,

$$
\begin{aligned}
& \Omega^{k}=\Omega_{a_{1}} \times \cdots \times \Omega_{a_{m}} \times\left(\Phi\left(s p_{a_{i j j_{1}}}\right), \ldots, \Phi\left(s p_{a_{i j j}}\right)\right), \text { where } \Phi\left(s p_{a_{i j}}\right)= \begin{cases}\left\{s p_{a_{i j}}\right\}, a_{i j} \in A^{k} \\
\left\{s p_{a_{i j}}^{c}\right\}, a_{i j} \notin A^{k} & , A^{k} \in \mathscr{P}(A)\end{cases} \\
& \Omega^{k} \cap \Omega^{k^{\prime}}=\varnothing \forall k \neq k^{\prime} \text { and } \bigcup_{k=1}^{2^{p}} \Omega^{k}=\Omega
\end{aligned}
$$

Clearly $\left\{\Omega^{k}: k=1, \ldots, 2^{p}\right\}$ is a partition of $\Omega$ and probability of every $\Omega^{k}$ is:

$$
p\left(\Omega^{k}\right)=p\left(\left\{s p_{i j}: a_{i j} \in A^{k}\right\} \wedge\left\{s p_{i j}^{c}: a_{i j} \in A \backslash A^{k}\right\}\right)=\prod_{a_{i j} \in A^{k}} p\left(s p_{i j}\right) \cdot \prod_{a_{i j} \in A \backslash A^{k}}\left(1-p\left(s p_{i j}\right)\right)
$$

Then, conditional probability of fire in $n_{i}$ given $\Omega^{k}$ is the probability that there is some ignition in any of its ancestors in $A^{k}$, that is

$$
\begin{aligned}
p\left(F_{i} \mid \Omega^{k}\right) & =p\left(i g_{i} \cup \bigcup_{j \in\left\{j: \exists c_{j i} \subset A^{k}\right\}} i g_{j}\right)=1-p\left(i g_{i}^{c} \cap \bigcap_{j \in\left\{j: \exists c_{j i} \subset A^{k}\right\}} i g_{j}^{c}\right)= \\
& =1-\left(1-p\left(i g_{i}\right)\right) \cdot\left(\prod_{j \in\left\{j: \exists c_{j i} \subset A^{k}\right\}}\left(1-p\left(i g_{j}\right)\right)\right)
\end{aligned}
$$

Finally, applying the Law of total probability

$$
p\left(F_{i}\right)=\sum_{k=1}^{2^{p}} p\left(\Omega^{k}\right) \cdot p\left(F_{i} \mid \Omega^{k}\right)
$$

This algorithm has its weak point in the partition of the probabilistic space in $2^{p}$ parts. This partition implies an exponential computing time with respect to $|A|$.

To explore alternative algorithms, we propose the following recursive definition of the event fire.
Definition 2. The event $F_{i}$ : ' $n_{i}$ burns' can be expressed in a recursive way as
' $n_{i}$ burns if there is ignition there or if a neighbor burns and fire spreads to $n_{i}$ '.
Or expressed in terms of elementary events,

$$
F_{i}=i g_{i} \cup \bigcup_{\substack{j=1 \\ j \neq i}}^{m}\left(F_{j} \cap s p_{j i}\right)
$$

However, the next example proves that this recursive definition is not always consistent.
Example 1. Consider the graph

$$
\begin{aligned}
G= & \left(N=\left\{n_{1}, n_{2}\right\}\right. \\
& \left.A=\left\{a_{12}=\left(n_{1}, n_{2}\right), a_{21}=\left(n_{2}, n_{1}\right)\right\}\right)
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Then, Definition 2 would be:

$$
\begin{aligned}
& F_{1}=i g_{1} \cup\left(s p_{21} \cap F_{2}\right) \\
& F_{2}=i g_{2} \cup\left(s p_{12} \cap F_{1}\right)
\end{aligned}
$$

Solving the system (13) by substitution

$$
F_{1}=i g_{1} \cup\left(s p_{21} \cap\left(i g_{2} \cup\left(s p_{12} \cap F_{1}\right)\right)\right)
$$

Using intersection and union sets' properties we obtain

$$
F_{1}=\left(i g_{1} \cup s p_{21}\right) \cap\left(i g_{1} \cup i g_{2} \cup s p_{12}\right) \cap\left(i g_{1} \cup i g_{2} \cup F_{1}\right)
$$

And, finally, taking into account that, from definition of $F_{1}, i g_{1} \subset F_{1}$

$$
F_{1}=\left(i g_{1} \cup s p_{21}\right) \cap\left(i g_{1} \cup i g_{2} \cup s p_{12}\right) \cap\left(i g_{2} \cup F_{1}\right)
$$

This Boolean implicit equation can be solved following [23] work. First, we need to consider the characteristic function of every event:

$$
A \rightarrow \mathcal{X}^{A}(\omega)=\left\{\begin{array}{l}
1, \text { if } \omega \in A \\
0, \text { if } \omega \notin A
\end{array} \quad(\omega \in \Omega)\right.
$$

for simplicity we just write $\mathcal{X}^{A}$.

$$
\mathcal{X}^{F_{1}}=\left(\mathcal{X}^{i g_{1}} \vee \mathcal{X}^{\alpha p_{21}}\right) \wedge\left(\mathcal{X}^{i g_{1}} \vee \mathcal{X}^{i g_{2}} \vee \mathcal{X}^{\alpha p_{12}}\right) \wedge\left(\mathcal{X}^{i g_{2}} \vee \mathcal{X}^{F_{1}}\right)
$$

Using the resolution method exposed on [23]

$$
\left(\mathcal{X}^{i g_{1}} \vee \mathcal{X}^{\alpha p_{21}}\right) \wedge\left(\mathcal{X}^{i g_{1}} \vee \mathcal{X}^{i g_{2}} \vee \mathcal{X}^{\alpha p_{12}}\right) \wedge \mathcal{X}^{i g_{2}} \leq \mathcal{X}^{F_{1}} \leq\left(\mathcal{X}^{i g_{1}} \vee \mathcal{X}^{\alpha p_{21}}\right) \wedge\left(\mathcal{X}^{i g_{1}} \vee \mathcal{X}^{i g_{2}} \vee \mathcal{X}^{\alpha p_{12}}\right)
$$

and grouping terms and expressing it again in sets language, we obtain

$$
F_{1}^{m}=\left(i g_{1} \cap i g_{2}\right) \cup\left(s p_{12} \cap s p_{21} \cap i g_{2}\right) \subseteq F_{1} \subseteq i g_{1} \cup\left(s p_{21} \cap\left(i g_{2} \cup s p_{12}\right)\right)=F_{1}^{M}
$$

Each set $F_{1}$ included in $F_{1}^{M}$ (Figure 2a) and containing $F_{1}^{m}$ (Figure 2b) is solution of (14).

![img-2.jpeg](img-2.jpeg)

Figure 2. (a) Venn diagram for maximal set event solution $F_{1}^{M}$. (b) Venn diagram for minimum set event solution $F_{1}^{m}$.

Therefore, there are multiple solution for $F_{1}$, specifically there are $2^{6}=64$ different set satisfying inequality (20). If one of them is chosen, $F_{2}$ is determined from the second equation of system (13), obtaining so a different solution for each of the solutions of $F_{1}$.

Following explicit Definition 1, $F_{1}=i g_{1} \cup\left(s p_{21} \cap i g_{2}\right)$ (Figure 3).
![img-3.jpeg](img-3.jpeg)

Figure 3. Venn representation of $F_{1}$ following explicit Definition 1.
It can be concluded that Definition (2) is not consistent since it does not guarantee unicity. Moreover, regarding the 'maximal solution'

$$
\begin{aligned}
& F_{1}^{M}=i g_{1} \cup\left(s p_{21} \cap\left(i g_{2} \cup s p_{12}\right)\right) \\
& F_{2}^{M}=i g_{2} \cup\left(s p_{12} \cap\left(i g_{1} \cup s p_{21}\right)\right)
\end{aligned}
$$

it would imply that if arcs $a_{12}$ and $a_{21}$ are able to spread $\left(s p_{1} \cap s p_{2}\right)$ then $n_{1}$ and $n_{2}$ burn without any ignition.

This example shows that Definition 1 is not consistent for the general case. In the following, it will be proven that this definition is consistent for acyclic networks, proving that Definitions 2 and 1 are equivalent in that case. Next proposition will be used later to prove the result.

Proposition 1. If $F_{1}, \ldots, F_{i-1}, F_{i+1}, \ldots, F_{m}$ are defined by Definition 1 and $F_{i}$ by Definition 2, then Definitions 2 and 1 are equivalent in $F_{i}$ :

$$
F_{i}=i g_{i} \cup \bigcup_{\substack{j=1 \\ j \neq i}}^{m}\left(F_{j} \cap s p_{j i}\right)=i g_{i} \cup \bigcup_{\substack{j=1 \\ j \neq i}}^{m}\left(i g_{j} \cap \bigcup_{c_{j i} \in C_{j i}}\left(\bigcap_{a_{k l} \in c_{j i}} s p_{k l}\right)\right)
$$

Proof. This proposition is mainly proved using arithmetic set properties. It has been included the case $m=1$, which is trivial since both formulas state that $F_{i}=i g_{i}$ when there is only one node $(m=1)$. Assume without loss of generality that $i=1$ and $m>1$. So, we want to proof that

$$
\begin{gathered}
F_{1}=i g_{1} \cup \bigcup_{j=2}^{m}\left(F_{j} \cap s p_{j 1}\right)=i g_{1} \cup \bigcup_{j=2}^{m}\left(i g_{j} \cap \bigcup_{c_{j 1} \in C_{j 1}} \bigcap_{a_{k l} \in c_{j 1}} s p_{k l}\right) \\
F_{1}=i g_{1} \cup \bigcup_{j=2}^{m}\left(F_{j} \cap s p_{j 1}\right)= \\
=i g_{1} \cup \bigcup_{j=2}^{m}\left(\left(i g_{j} \cap s p_{j 1}\right) \cup \bigcup_{j=1}^{m}\left(i g_{i} \cap s p_{j 1} \cap\left(\bigcup_{c_{i j} \in C_{i j}} \cap_{a_{k l} \in c_{i j}} s p_{k l}\right)\right)\right)= \\
=i g_{1} \cup\left(\bigcup_{j=2}^{m}\left(i g_{j} \cap s p_{j 1}\right)\right) \cup\left(\bigcup_{j=2}^{m} \bigcup_{i=1}^{m}\left(i g_{i} \cap s p_{j 1} \cap\left(\bigcup_{c_{i j} \in C_{i j}} \cap_{a_{k l} \in c_{i j}} s p_{k l}\right)\right)\right)= \\
=i g_{1} \cup\left(\bigcup_{j=2}^{m}\left(i g_{j} \cap s p_{j 1}\right)\right) \cup\left(\bigcup_{j=2}^{m}\left(i g_{1} \cap s p_{j 1} \cap\left(\bigcup_{c_{1 j} \in C_{1 j}} \cap_{a_{k l} \in c_{1 j}} s p_{k l}\right)\right)\right) \cup \\
\cup\left(\bigcup_{j=2}^{m} \bigcup_{i=2}^{m}\left(i g_{i} \cap s p_{j 1} \cap\left(\bigcup_{c_{i j} \in C_{i j}} \cap_{a_{k l} \in c_{i j}} s p_{k l}\right)\right)\right)
\end{gathered}
$$

and using $\bigcup_{j=2}^{m}\left(i g_{1} \cap s p_{j 1} \cap \bigcup_{c_{1 j} \in C_{1 j}}\left(\cap_{a_{k l} \in c_{1 j}} s p_{k l}\right)\right) \subset i g_{1}$

$$
\begin{aligned}
F_{1} & =i g_{1} \cup\left(\bigcup_{j=2}^{m}\left(i g_{i} \cap s p_{i 1}\right)\right) \cup\left(\bigcup_{j=2}^{m} \bigcup_{i=2}^{m}\left(i g_{i} \cap s p_{j 1} \cap\left(\bigcup_{c_{i j} \in C_{i j}} \cap_{a_{k l} \in c_{i j}} s p_{k l}\right)\right)\right)= \\
& =i g_{1} \cup\left(\bigcup_{j=2}^{m}\left(i g_{i} \cap s p_{i 1}\right)\right) \cup\left(\bigcup_{i=2}^{m} \bigcup_{j=2}^{m}\left(i g_{i} \cap s p_{j 1} \cap\left(\bigcup_{c_{i j} \in C_{i j}} \cap_{a_{k l} \in c_{i j}} s p_{k l}\right)\right)\right)=
\end{aligned}
$$

Last two equations just differ in the index union order. In both cases, the union is defined over the index set $\{(i, j) \in\{2, \ldots, m\}^{2}: i \neq j\}$. This change will be useful for finishing the proof.

$$
\begin{aligned}
F_{1} & =i g_{1} \cup\left(\bigcup_{j=2}^{m}\left(i g_{i} \cap s p_{i 1}\right)\right) \cup\left(\bigcup_{i=2}^{m} i g_{i} \cap \bigcup_{j=2}^{m} \bigcup_{c_{i j} \in C_{i j}} \cap_{a_{k l} \in c_{i j}} s p_{k l} \cap s p_{j 1}\right)= \\
& =i g_{1} \cup \bigcup_{i=2}^{m} i g_{i} \cap\left(\left(\bigcup_{c_{i 1}=\left\{s p_{i 1}\right\}} s p_{i 1}\right) \cup\left(\bigcup_{j=2}^{m} \bigcup_{c_{i j} \in C_{i j}} \cap_{a_{k l} \in c_{i j}} s p_{k l} \cap s p_{j 1}\right)\right)= \\
& =i g_{1} \cup \bigcup_{i=2}^{m}\left(i g_{i} \cap \bigcup_{c_{i 1} \in C_{i 1}} \cap_{a_{k l} \in c_{i 1}} s p_{k l}\right)
\end{aligned}
$$

For the last step, note that $\left\{s p_{i 1}\right\}$ is the set of all paths from $n_{i}$ to $n_{1}$ with length 1 , and

$$
\left\{s p_{k l} \cap s p_{j 1}: i \neq j=2, \ldots, m, c_{i j} \in C_{i j}, a_{k l} \in c_{i j}\right\}
$$

is the set of all paths from $n_{i}$ to $n_{1}$ with length $\geq 2$.
Following result is directly derived from Proposition 1. It will complete discussion about fire event definition.

Corollary 1. If $(N, A)$ is a directed acyclic graph (DAG), then Definitions 2 and 1 are equivalent.
Proof. In a DAG, there exists a partial order $<_{G}$ defined as

$$
n_{i}<_{G} n_{j} \Leftrightarrow \text { exists a directed path from } n_{i} \text { to } n_{j}
$$

Assuming $N$ is a finite set, we can say that a subgroup of nodes exists $N_{0} \subset N$ with no-parents, or in other words

$$
\exists \varnothing \neq N_{0} \subset N \text { such as } n_{i} \nless_{G} n_{j} \quad \forall n_{i} \in N, n_{j} \in N_{0}
$$

Now, considering $N \backslash N_{0}$ we can repeat same reasoning and denote this set of minimal elements as $N_{1}$. This process can be repeated until $\left(N \backslash N_{0}\right) \backslash \ldots) \backslash N_{u}=\varnothing$, so $N$ can be split on $u$ disjoint sets of nodes, satisfying

$$
k \leq k^{\prime} \Rightarrow n^{k^{\prime}} \nless_{G} n^{k} \quad \forall n^{k} \in N_{k} \text { and } \forall n^{k^{\prime}} \in N_{k^{\prime}}
$$

This is there is no path from any node of $N_{k^{\prime}}$ to any node of $N_{k}$ if $k \leq k^{\prime}$ (see Figure 4).
![img-4.jpeg](img-4.jpeg)

Figure 4. Nodes structure in DAG.
Finally, note that every node of $N_{k+1}$ has its parents on $\bigcup_{k=1}^{k} N_{k}$, then assuming that nodes of this union are defined by (6) and nodes of $N_{k+1}$ are defined by (11), then all the conditions of Proposition 1 are satisfied and Definitions 1 and 2 are equivalent in $N_{k+1}$. Moreover, for nodes in $N_{0}$, equivalence of (11) and (6) is trivial. Therefore, using complete induction and Proposition 1 we can conclude Definitions 1 and 2 are equivalent for all $N$.

# 2.2. Bayesian Network 

In this section, we will prove that random (binary) variables $x_{F}=\left\{x_{F_{1}}, \ldots, x_{F_{m}}\right\}$ associated with fire events conform a Bayesian network, as long as $G$ is a DAG. This result will allow us to use specific algorithms for computing fire probabilities.

Next result it is a technical property related with mutually independent sets. It will be necessary in the proof of the main result of this section, Proposition 2.

Lemma 1. Let $C_{1}$ and $C_{2}$ two mutually independent sets of events, this is

$$
p(A \cap B)=p(A) \cdot p(B), \quad \forall A \in C_{1}, B \in C_{2}
$$

then $\sigma$-algebras

$$
\sigma\left(C_{1}\right) \text { and } \sigma\left(C_{2}\right)
$$

are mutually independent, i.e.,

$$
p(A \cap B)=p(A) \cdot p(B) \quad \forall A \in \sigma\left(C_{1}\right), B \in \sigma\left(C_{2}\right)
$$

Proof. This is a particular case of Corollary 10.1 (b) collected in ([24], pp. 284-285).

Proposition 2. Random (binary) variables $x_{F}=\left\{x_{F_{1}}, \ldots, x_{F_{m}}\right\}$ associate with fire events defined as Definition 1 or 2 conform a Bayesian network over a directed acyclic graph $G$.

Proof. There are a few ways to define Bayesian networks, we will use the Local Markov property [25]. Given a DAG, there is a natural partial order defined in its nodes:

$$
n_{i}<_{G} n_{j} \text { if exists a directed path from } n_{i} \text { to } n_{j}
$$

With this notation, the Local Markov property consist on

$$
\begin{gathered}
p\left(x_{F_{i}}=f_{i} \mid x_{F_{j}}=f_{j}: n_{j} \ngtr_{G} n_{i}\right)= \\
p\left(x_{F_{i}}=f_{i} \mid x_{F_{j}}=f_{j}: n_{j}<_{G} n_{i}\right), \quad f_{i}, f_{j} \in\{0,1\}
\end{gathered}
$$

Using binary random variables instead of events, we can express (11) as

$$
x_{F_{i}}=x_{n_{i}} \vee \bigvee_{\substack{j=1 \\ j \neq i}}^{\infty}\left(x_{F_{j}} \wedge x_{a_{j j}}\right)=x_{n_{i}} \vee \bigvee_{j \in\left\{j: a_{j j} \in A\right\}}\left(x_{F_{j}} \wedge x_{a_{j j}}\right)
$$

and

$$
\begin{aligned}
p\left(x_{F_{i}}=f_{i}\right) & =f_{i} \cdot p\left(x_{F_{i}}=1\right)+\left(1-f_{i}\right) \cdot p\left(x_{F_{i}}=0\right)= \\
& =f_{i} \cdot p\left(x_{F_{i}}=1\right)+\left(1-f_{i}\right) \cdot\left(1-p\left(x_{F_{i}}=1\right)\right)= \\
& =\left(2 f_{i}-1\right) \cdot p\left(x_{F_{i}}=1\right)+\left(1-f_{i}\right)= \\
& =\left(2 f_{i}-1\right) \cdot p\left(x_{n_{i}}=1 \vee \bigvee_{j \in\left\{j: a_{j j} \in A\right\}}\left(x_{F_{j}}=1 \wedge x_{a_{j i}}=1\right)\right)+\left(1-f_{i}\right)
\end{aligned}
$$

Then,

$$
\begin{aligned}
& p\left(x_{n_{i}}=1 \vee \bigvee_{j \in\left\{j: a_{j j} \in A\right\}}\left(x_{F_{j}}=1 \wedge x_{a_{j i}}=1\right) \mid x_{F_{j}}=f_{j}: n_{j} \ngtr_{G} n_{i}\right)= \\
& p\left(x_{n_{i}}=1 \vee \bigvee_{j \in\left\{j: a_{j j} \in A\right\}}\left(x_{F_{j}}=1 \wedge x_{a_{j i}}=1\right) \mid x_{F_{j}}=f_{j}: n_{j}<_{G} n_{i}\right)
\end{aligned}
$$

For the first conditional probability we have

$$
\begin{aligned}
& p\left(x_{n_{i}}=1 \vee \bigvee_{j \in\left\{j: a_{j j} \in A\right\}}\left(x_{F_{j}}=1 \wedge x_{a_{j i}}=1\right) \mid x_{F_{j}}=f_{j}: n_{j} \ngtr_{G} n_{i}\right)= \\
& p\left(x_{n_{i}}=1 \vee \bigvee_{j \in\left\{j: a_{j j} \in A \wedge f_{j}=1\right\}}\left(x_{a_{j j}}=1\right) \mid x_{F_{j}}=f_{j}: n_{j} \ngtr_{G} n_{i}\right)
\end{aligned}
$$

and following same reasoning for second conditional probability

$$
\begin{aligned}
& p\left(x_{n_{i}}=1 \vee \bigvee_{j \in\left\{j: a_{j j} \in A\right\}}\left(x_{F_{j}}=1 \wedge x_{a_{j i}}=1\right) \mid x_{F_{j}}=f_{j}: n_{j}<_{G} n_{i}\right)= \\
& p\left(x_{n_{i}}=1 \vee \bigvee_{j \in\left\{j: a_{j j} \in A \wedge f_{j}=1\right\}}\left(x_{a_{j j}}=1\right) \mid x_{F_{j}}=f_{j}: n_{j}<_{G} n_{i}\right)
\end{aligned}
$$

Finally, with Lemma 1 we can see that $F_{k}$ is independent to

$$
i g_{i} \cup \bigcup_{j \in\left\{j: a_{j i} \in A \wedge f_{j}=1\right\}} i g_{j}
$$

for any $k$ such as $n_{k} \ngtr_{G} n_{i}$. It is enough to see that $F_{k} \in \sigma\left(\left\{i g_{i}, s p_{j i}: n_{i} \leq_{G} n_{k}\right\}\right)$ and $\left(i g_{i} \cup \bigcup_{j \in\left\{j: a_{j j} \in A \wedge f_{j}=1\right\}} i g_{j}\right) \in \sigma\left(\left\{i g_{i}, s p_{j i}: n_{i} \not \leq_{G} n_{k}\right\}\right)$ to obtain the result.

Therefore, we can use plenty of specific Bayesian Networks algorithms that take profit of this structure of $(\Omega, \mathscr{A}, p)$ in order to compute $p\left(F_{i}\right)$ efficiently.

# 3. Risk Measure Proposed: Losses Expected Value 

Definition 3 (Fire Risk Measure). Given a probabilistic space $(\Omega, \mathcal{A}, p)$ over a network $(N, A)$, and defined the event fire $F_{i}$, we define the Fire Risk Measure (FRM) as the losses expected value due to forest fire

$$
F R M=\sum_{i=1}^{m} v\left(n_{i}\right) p\left(F_{i}\right)
$$

where $v\left(n_{i}\right)$ is the value associated with $n_{i}$ sector that may depends on human, economic and ecological factors.
This definition needs 1st assumption to consider a probabilistic space over a network . 2nd assumption is needed to be able to compute $p\left(F_{i}\right)$ (Equation (10)).

Previous section is intended to explore under which conditions it is possible to tackle the fire probability problem from a Bayesian perspective. In this section, a methodology suitable for computing it in real cases is shown.

Network resulting from representing a landscape will rarely be a Bayesian network. In a general case, we can assume wind scenarios under which the associated graph is a DAG.

3rd assumption: A finite set of meteorological scenarios of disjoint events can be considered and, under each one of them, the network representing landscape is a DAG.

Formally, this assumption means that a set $\mathcal{S}$ and a probabilistic space $\left(\mathcal{S}, \mathscr{P}(\mathcal{S}), p_{\mathcal{S}}\right)$ exists, such as

$$
\begin{aligned}
& \mathcal{S}=\left\{\omega_{1}, \ldots, \omega_{s}\right\}, \\
& \omega_{i}: \text { meteorological scenario, } \\
& \mathcal{A}_{\mathcal{S}}=\mathscr{P}(\mathcal{S}), \\
& p_{\mathcal{S}}: \quad \mathcal{A}_{\mathcal{S}} \quad \longrightarrow \mathbb{R}, \\
& \varnothing \quad \longrightarrow \quad 0 \\
& \left\{\omega_{i}\right\} \quad \longrightarrow \quad p_{\mathcal{S}}\left(\left\{\omega_{i}\right\}\right), \\
& \sum_{i=1}^{s} p_{\mathcal{S}}\left(\left\{\omega_{i}\right\}\right)=1 \text { and } p_{\mathcal{S}}\left(\left\{\omega_{i}\right\} \cap\left\{\omega_{j}\right\}\right)=0, \forall i \neq j
\end{aligned}
$$

and

$$
\begin{aligned}
& \tilde{\Omega}=\mathcal{S} \times \Omega_{n_{1}} \times \cdots \times \Omega_{n_{m}} \times \Omega_{a_{i j j}} \times \cdots \times \Omega_{a_{i j j j}}
\end{aligned}
$$

$$
\begin{aligned}
& \tilde{p}: \quad \mathcal{A} \xrightarrow[\left(\omega, w_{1}, \ldots, w_{m}, t_{i_{1} j_{1}}, \ldots, t_{i_{p} j_{p}}\right) \quad \mapsto \quad p_{\mathcal{S}}(\omega) \cdot \prod_{n_{i} \in N} p_{n_{i}}\left(w_{i}\right) \cdot \prod_{a_{i j} \in A} p_{a_{i j}}\left(t_{i j}\right), \\
& \forall w \in \mathscr{P}(\mathcal{S}) w_{i} \in \mathcal{A}_{n_{i}}, t_{i j} \in \mathcal{A}_{a_{i j}}
\end{aligned}
$$

Finally,

$$
G^{\omega}=\left(N, A^{\omega}=\left\{a_{i j}: \tilde{p}\left(s p_{i j} \mid \omega\right) \neq 0\right\}\right) \text { is DAG, } \forall \omega \in \mathcal{S}
$$

Definition 3 can be applied with extended probability $\tilde{p}$ :

$$
\operatorname{FRM}=\sum_{i=1}^{m} v\left(n_{i}\right) \tilde{p}\left(F_{i}\right)=\sum_{\omega \in \mathcal{S}} \tilde{p}(\omega) \sum_{i=1}^{m} v\left(n_{i}\right) \tilde{p}\left(F_{i} \mid \omega\right)
$$

The consideration of scenarios has the purpose of being able to apply Bayesian algorithms to compute FRM in real cases. However, 2nd assumption, independence between ignition and spreads, is more realistic under a particular scenario. Also, estimations of $p\left(i g_{i}\right)$ and $p\left(s p_{i j}\right)$ are

usually dependent of meteorological variables, therefore, fixing a meteorological state we can estimate Bayesian network parameters.

Even in a dominant wind scenario, loops are possible. In such cases, a more efficient partition where each $G_{k}$ is a DAG is possible (see Example 2), being possible computing fire probabilities within a reasonable time.

A relaxation of 3rd assumption can be considered instead of the original one:
3rd relaxed assumption: A finite set of meteorological scenarios of disjoint events can be considered and, under each one of them, the network representing landscape is a quasi-DAG.

Next example shows how to work with quasi-DAG.
Example 2. Suppose we are interested in studying the non-DAG network represented in Figure 5, $G=(N, A)$.
![img-5.jpeg](img-5.jpeg)

Figure 5. Network with a loop.
Edges $\left\{a_{34}, a_{47}, a_{73}\right\}$ conform the only loop of the graph. With a similar argument of methodology showed in Equation (10), we only need to split the probabilistic model over $\left(\Omega_{a_{34}} \times \Omega_{a_{47}} \times \Omega_{a_{73}}\right)$. All $8\left(=2^{3}\right)$ resulted models represented with 8 different graphs in Figure 6 can be seen as Bayesian networks. For the last model, we can see nodes $n_{3}, n_{4}$ and $n_{7}$ as a unique node since connectivity between all then has probability 1 .

![img-6.jpeg](img-6.jpeg)

Figure 6. Representation of partition of the probabilistic space.
Consideration of scenarios and partition over some possible loops may complicate the methodology for computing an FRM. Table 1 of computational times comparing partition algorithm and Bayes-based algorithm shows the necessity of the Bayes-based algorithms in networks with more than 20 arcs.

Table 1. Computational time comparative between inference Bayes algorithm and naive algorithm (Equation (10)) with different network size $(m=|N|, p=|A|)$. Algorithms has been executed on a computer with an Intel Core i7 processor and 8gb RAM.


# 4. Case Example 

Forests authorities need to evaluate risk of fire of the territory to decide and prioritize preventive actions as prescribed burns and firebreak location. A study of fuel, dominant winds, and orography of sectors allows the obtaining of an estimation of fire's behavior. To obtain accurate results, many types of information must be taken into account.

This section has an illustrative purpose trying to avoid many of the technical issues presented in a real case. It has been simulated an island (Figure 7a) using [21] to apply the methodology exposed in the previous sections. For this example, we suppose that the fire affecting the island is always wind-driven [2] and dominant winds are in the vertical line, it means, two wind direction scenarios $\{\uparrow, \downarrow\}$ referred to South and North wind, respectively. Partition of this example is done considering this assumption (Figure 7b).

![img-7.jpeg](img-7.jpeg)

Figure 7. (a) Fictional island. (b) Sectors considered for a wind-driven fire type.

Ignition probability is considered proportionally to its area fixing the probability of there being any ignition on the island over a year to $0.5\left(p\left(\mathrm{U} i g_{i}\right)=0.5\right.$, Table 2). In a real case, this number should be estimated with historical data. Probability of spread follows wind direction which depends on the scenario. Figure 8 is the network resulting from scenario ' $\downarrow$ '. The network for scenario ' $\uparrow$ ' will include the same arcs but with opposite direction with the same probabilities that can be seen in Figure 8. Now, it is possible to compute fire probability of each sector and consequently, to obtain the expected burned area. In this case, $v\left(n_{i}\right)$ is proportional to the area of the sector and is measured in terms of Monetary Unit [MU]. In a general case, $v$ should be estimated taking into account several factors, as for instance, the assets located in the sector, including the forest itself.

Table 2. Ignition probability and area considered for each sector.


The network has 43 arcs and with this size, the partition algorithm is untraceable: there are more than $8 \times 10^{12}$ of subgraphs $G_{k}$. Using Bayesian algorithms provided by [26], we calculate FRM: 2453 MU. $13.44 \%$ of the landscape is expected to burn, from which $35.59 \%$ is due to ignitions.

With the aim of showing how the defined measure can support decision-making, we will compare two different preventive actions: prescribed burns and firebreaks. Prescribed burns usually do not affect trees; controlled fire burns bush and small plants. Thus, we will assume in this example that prescribed burns affect the value of a sector reducing it by $20 \%$ and ignition and spread probabilities by $50 \%$. We compare the results of the risk measure considering that prescribed burn can be performed in only one sector, resulting sector 9 the optimal selection (Table 3). In this case, a controlled fire in this sector increases FRM by $0.2 \cdot v\left(n_{9}\right)\left(1-\bar{p}\left(F_{9}\right)\right)=167 \mathrm{MU}$, but the expected value of losses due to fire in the landscape decreases until 509 MU .

Prescribed burns is not the only option, and even sometimes it is not possible perform it. Land ownership or the protection of natural spaces restrict location and techniques for prescribed burns, being firebreaks an alternative option. A firebreak is a safe place where firefighters can stop fires from spreading out. Considering that only it is allowed locating one firebreak, in our example, the connection that produces the greatest reduction in the risk measure is $(4,9)$ (and $(9,4)$ ). A firebreak

located there, assuming $100 \%$ of effectiveness $\left(p\left(s p_{49}\right)=p\left(s p_{94}\right)=0\right)$ reduces the value of FRM to 2100 MU (Table 4).
![img-8.jpeg](img-8.jpeg)

Figure 8. Network representation for scenario ' $\downarrow$ '. Network associated with scenario ' $\uparrow$ ' is equivalent but with arrows inverted.

Table 3. FRM after performing prescribed burns in each sector. Minimum value is highlighted in bold.


Table 4. FRM after locating a firebreak between two sectors. Minimum value is highlighted in bold.


A hypothetical decision-maker could prefer a more detailed output. The analysis computes the fire probability of each sector showing the effect of the preventive actions on the fire probabilities of each sector. This information is plotted in greyscale differentiating risk under different wind scenarios in Table 5.

Table 5. FRM with different scenario set and forestry treatments: no treatment, prescribed burn in sector 9 , location of firebreak between sector 4 and 9.


# 5. Conclusions and Future Work 

The aim of this work is to develop a methodology to support decision-making in the fight against wildfires. Focused on preventive actions on fuel management, a theoretical framework for a risk measure in a wildfire context has been studied without diverting attention from the main purpose.

A risk measure has been defined through the representation of the landscape as a network and based on the ignition and spread probabilities on it. The measure, defined as the expected value of fire losses, requires an efficient way to compute probabilities of each node burning. Under several assumptions and for a specific wind direction scenario, it has been proved that the network can be conformed to a Bayesian Network. Therefore, efficient algorithms developed for Bayesian Networks can compute the probabilities. The proposed methodology has been applied to an example to illustrate its usefulness for decision-making to minimize the risk of the network, comparing different landscape configurations after fuel management treatments. Moreover, with an accurate estimation of the sectors values, the proposed risk measure can also be used to justify prevention investments.

The limitations of the study are given by the assumptions made:
1st assumption considers that landscape can be divided in homogeneous areas. Researchers and firefighters often make this assumption when working with big scales territories. Usually watersheds are considered to section the landscape, but other methodologies may be explored.
2nd assumption relates to the independence between ignitions and spread capabilities. Correlations between spread and ignition events could arise mainly due to a mutual meteorological scenario affecting them. Consideration of scenarios in the analysis makes this 2nd assumption more acceptable.
3rd assumption, related to acyclic graphs, in its relaxed version, is accomplished considering wind direction scenarios and assuming no spread against wind direction.

Other limitations come from basic input data estimation. Ignition probabilities can be estimated from historical data and a study of influential factors. Fire simulators can be used to estimate spread probabilities. Wind direction scenarios can be obtained from historical data, although scenario

generation is a research area under development. Nevertheless, in real cases, expert opinion will remain decisive. Future work will be devoted to obtaining accurate estimations of these input data.

The aim of this paper is to provide the measure to be optimized into decision-making models. Therefore, future research will be devoted to the development of an optimization model to support decisions on the best actions to be implemented to minimize this fire risk measure with limited resources. These limited resources usually will be related to costs and budget, or to time for developing the activities. It must be taken into account that there is limited time window for developing some preventive activities as prescribed burns determined mainly by weather conditions.

Finally, note that tactical planning is crucial in the fight against forest fires. Firefighters and forest guards dedicate effort, time and resources to these tasks. A model to measure the effects of their preventive actions on the landscape will increase their capacity of decision-making and their effectiveness.

Author Contributions: Conceptualization, A.R.-M. and B.V.; data curation, A.R.-M.; formal analysis, A.R.-M. and B.V.; funding acquisition, B.V.; investigation, A.R.-M.; methodology, A.R.-M. and B.V.; project administration, B.V.; resources, B.V.; software, A.R.-M.; validation, A.R.-M.; visualization, A.R.-M.; writing-original draft, A.R.-M. and B.V.; writing-review and editing, A.R.-M. and B.V. All authors have read and agreed to the published version of the manuscript.
Funding: This research has been supported by the H2020 Marie Skłodowska-Curie RISE Action GEO-SAFE 691161, the Government of Spain grant project MTM2015-65803-R and the Complutense University grant CT17/17-CT18/17.
Conflicts of Interest: The authors declare no conflict of interest.
