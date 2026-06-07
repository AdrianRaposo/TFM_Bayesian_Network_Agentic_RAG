# Article 

## The Situation Assessment of UAVs Based on an Improved Whale Optimization Bayesian Network ParameterLearning Algorithm

Weinan Li ${ }^{1, * *}$, Weiguo Zhang ${ }^{1}$, Baoning Liu ${ }^{2}$ and Yicong Guo ${ }^{1 *}$


#### Abstract

check for updates Citation: Li, W.; Zhang, W.; Liu, B.; Guo, Y. The Situation Assessment of UAVs Based on an Improved Whale Optimization Bayesian Network Parameter-Learning Algorithm. Drones 2023, 7, 655. https:// doi.org/10.3390/drones7110655

Academic Editors: Shuang Li, Chengchao Bai and Jinzhen Mu

Received: 6 October 2023
Revised: 28 October 2023
Accepted: 30 October 2023
Published: 1 November 2023


## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Automation, Northwestern Polytechnical University, Xi'an 710129, China; zhangwg@nwpu.edu.cn (W.Z.); guoyicong@mail.nwpu.edu.cn (Y.G.)
2 The Institute of Xi'an Aerospace Solid Propulsion Technology, Xi'an 710025, China

* Correspondence: liweinan@mail.nwpu.edu.cn


#### Abstract

To realize unmanned aerial vehicle (UAV) situation assessment, a Bayesian network (BN) for situation assessment is established. Aimed at the problem that the parameters of the BN are difficult to obtain, an improved whale optimization algorithm based on prior parameter intervals (IWOA-PPI) for parameter learning is proposed. Firstly, according to the dependencies between the situation and its related factors, the structure of the BN is established. Secondly, in order to fully mine the prior knowledge of parameters, the parameter constraints are transformed into parameter prior intervals using Monte Carlo sampling and interval transformation formulas. Thirdly, a variable encircling factor and a nonlinear convergence factor are proposed. The former and the latter enhance the local and global search capabilities of the whale optimization algorithm (WOA), respectively. Finally, a simulated annealing strategy incorporating Levy flight is introduced to enable the WOA to jump out of the local optimum. In the experiment for the standard BNs, five parameter-learning algorithms are applied, and the results prove that the IWOA-PPI is not only effective but also the most accurate. In the experiment for the situation BN, the situations of the assumed mission scenario are evaluated, and the results show that the situation assessment method proposed in this article is correct and feasible.


Keywords: situation assessment; Bayesian network; parameter learning; constraints; whale optimization algorithm

## 1. Introduction

The modern working environments for UAVs are extremely complex and filled with a wide variety and a large number of entities, and these bring difficulties and challenges for UAV situation assessment. Situation assessment is the process of perceiving the attributes, states, and behaviors of entities in an environment, understanding an environment's information, inferring entities' intentions, and finally predicting entities' future short-term actions [1]. Intention inference is the core of situation assessment, and the mission is the expression of the intention. Therefore, the situation is embodied as the entities' mission in this article. The general methods of situation assessment include the analytic hierarchy process (AHP) [2,3], the technique for order preference by similarity to ideal solution (TOPSIS) [4,5], neural networks [6,7], fuzzy logic [8,9], Bayesian networks [10,11], etc.

All the above methods, except for Bayesian networks, achieve situation assessment to a certain degree, but each of them has some shortcomings. The AHP relies on the human subjective experience too much, and inaccurate experiences lead to a large deviation in situation assessment results. The TOPSIS is unable to solve the problem of single-target situation assessment. In the case of multiple targets, the distance from the optimal solution to the positive ideal solution may approximate the distance to the negative ideal solution, which makes it possible to obtain the opposite assessed results. Neural networks have

black box characteristics that make it hard to accurately determine the effect on the output when certain inputs change. It is difficult to determine the logic operations and inferring methods of fuzzy logic. In addition, both neural networks and fuzzy logic have only a single output for known inputs and cannot provide other feasible solutions.

A Bayesian network (BN) is a probabilistic graphical model that combines the abilities to express and infer uncertain knowledge and is capable of handling multivariate information. BNs consist of a structure and parameters [12]. The former abstracts the dependencies between the situations and its associated elements into a visual network, and the latter transforms the degree of association between the elements into a conditional probability table (CPT). The construction process of BNs is consistent with the human cognitive habits of situations, which is more conducive to commanders' inference and application. Compared to the AHP, thanks to structure and parameter learning, BNs alleviate the influence of human subjective experiences. In comparison with the TOPSIS, BNs solve the problem of single-target and multi-target situation assessment. Speaking of neural networks and fuzzy logic, BNs not only have a clear structure with white box characteristics, but also follow mature Bayesian criteria in probability calculation and inference. In addition, BNs output the probabilities of different states of multiple nodes and provide decision-makers with multiple choices.

Despite the many advantages of BNs, the network parameters are sometimes difficult or even impossible to obtain. Combined with expert knowledge and sample data, the parameters are acquired via parameter learning. The main parameter-learning methods include constrained optimization methods and Bayesian estimation methods.

The constrained optimization methods represent expert knowledge as constraints and then treat parameter learning as an optimization problem. Niculescu [13], Campos [14], and Hou [15] transform parameter learning into an optimization problem with constraints. They use the logarithmic or entropy function as the objective function and optimize the objective function convexly in the feasible domain, limited by constraints. Altendorf [16] and Liao [17] transformed parameter learning into an optimization problem without constraints. They constructed a penalty function with constraints and then summed the logarithmic likelihood function and the penalty function to obtain the augmented objective function to be optimized.

The Bayesian estimation methods transform expert knowledge into the ranges of the values of the parameters, calculate the hyper-parameters of the prior distribution of the parameters within these ranges, and finally combine the hyper-parameters and the sample data to compute the Bayesian maximum a posteriori (MAP) to obtain the BN parameters. Ren [18] and Di [19] assume that the parameters obey a uniform distribution in the feasible domain, and Chai [20] proposes to represent the approximate equality constraints based on the normal distribution. They use Beta distribution to approximate the uniform and normal distributions, respectively. Since the Beta distribution is the marginal distribution of the Dirichlet distribution, the hyper-parameters of the Dirichlet distribution are derived from the Beta distribution parameters. In the end, the BN parameters are obtained using the MAP formula. Gao [21] proposes a constrained Bayesian estimation (CBE) algorithm that enhances learning accuracy by introducing expert criteria. Di [22] proposes a constrained adjusted MAP (CaMAP) algorithm by choosing a reasonable equivalent sample size. The qualitative maximum a posteriori estimation (QMAP) algorithm proposed by Chang [23] performs Monte Carlo (MC) sampling on the feasible domain of the parameters determined based on constraints. The pseudo prior counts obtained are functionally equivalent to the hyper-parameters of the Dirichlet distribution, and then the parameters are computed using the MAP formula. Guo [24] made an improvement to the QMAP algorithm and proposes a further constrained QMAP algorithm.

The above two methods have the following defects: firstly, the learning results of the convex optimization algorithm in the studies [13,14,15] are often located at the boundary of the feasible domain of the parameters [25], which leads to the degradation of inequality constraints into equality constraints. This indicates a failure to fully utilize expert knowl-

edge. In addition, directly optimizing within the limited range of ordinary constraints often fails to fully utilize prior knowledge in the constraints. Secondly, the penalty function method in studies [16,17] needs to design specific penalty functions for different constraints, and the penalty factor is manually determined, which is sometimes inaccurate. Thirdly, for some sample data, the learning results of QMAP [23] may violate some parameter constraints. This means a failure to make full use of the sample data. In addition, study [19] only applies to monotonic constraints, and study [20] only applies to approximate equality constraints. The prior distribution of [21] is set to be the BDeu priors rather than the transferred priors, which are more meaningful. When no parameter constraints are available, the CaMAP [22] is inferior to the MAP. The FC-QMAP algorithm [24] only outperforms QMAP when dealing with small datasets.

In order to overcome the shortcomings of the above algorithms, in this article, an improved whale optimization algorithm based on parameter prior intervals (IWOA-PPI) for parameter learning is proposed, and the parameters learned by the IWOA-PPI are substituted into the situation assessment BN to evaluate the situation. In this algorithm, expert knowledge is transformed into parameter qualitative constraints; then, parameter prior intervals (PPIs) are calculated depending on the qualitative constraints, and finally, the improved WOA is used to optimize within the PPIs to obtain the optimal parameters. Due to the integration of the advantages of the constrained optimization methods and Bayesian estimation methods, the new algorithm proposed in this article can not only mine the information in the expert knowledge as much as possible, but can also fully utilize sample data. The main contributions of this article are that (1) the concept of PPIs is proposed. The PPIs not only contain the prior knowledge of the parameters but also narrow the feasible domain of the parameters, thus improving the search accuracy of subsequent IWOA. (2) A new variable encircling factor for the WOA is proposed. The variable encircling factor can properly shrink the local search area with the operation of the algorithm, and the local search ability of the WOA is enhanced.

The rest of the article is organized as follows: Section 2 introduces the preliminary knowledge, including BN parameter learning, parameter constraints, and the WOA. Section 3 establishes the structure of the BN for situation assessment. Section 4 proposes the improved whale optimization algorithm based on parameter prior intervals. Section 5 designs the simulation experiments. The parameters of four BNs are learned by five algorithms in the experiment for standard BNs, and the results prove that the IWOA-PPI proposed in this article is of the highest accuracy. The situation of the assumed mission scenario is evaluated in the experiment for the situation assessment BN, and the results verify that the BN established in this article can correctly infer the target intention. Finally, conclusions are drawn in Section 6.

# 2. Preliminaries 

### 2.1. BN Parameter Learning

A BN is a direct acyclic graph with probabilities, which is generally denoted as $B=(G, \Theta) . G=(V, E)$ is the graph structure, the set of nodes $(V)$ denotes the set of random variables, and the set of directed arcs $(E)$ denotes the dependencies between the random variables. $\Theta$ is the set of network parameters denoting the conditional probability distributions between states of nodes. $\Theta$ is also denoted as $P\left(X_{i} \mid p a\left(X_{i}\right)\right)$, where $p a\left(X_{i}\right)$ denotes the set of parents of node $X_{i}$. When the parents are given, node $X_{i}$ is conditionally independent of its non-descendant nodes. According to the Markov condition, the joint probability distribution of a BN can be represented in Equation (1):

$$
P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

When the structure $G$ is known, the parameter learning of a BN refers to the estimation of the true parameters of the BN from a given sample dataset, $D$, according to a certain criterion. The BN parameter $\theta_{i j k}$ is denoted in Equation (2):

$$
\begin{gathered}
\theta_{i j k}=P\left(X_{i}=k \mid p a\left(X_{i}\right)=j\right) \\
1 \leq i \leq n, 1 \leq j \leq q_{i}, 1 \leq k \leq r_{i}
\end{gathered}
$$

where $i$ denotes the serial number of $X_{i}, j$ denotes the state of $p a\left(X_{i}\right)$, and $k$ denotes the state of $X_{i}$.

There are two basic methods for BN parameter learning: maximum likelihood estimation (MLE) and Bayesian estimation. MLE is usually used for a sample set with a sufficient sample size and no missing data. The logarithmic likelihood function for BNs is defined in Equation (3):

$$
L(\theta \mid D)=\log P(D \mid \theta)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \log \theta_{i j k}
$$

where $N_{i j k}$ denotes the number of samples that satisfy $X_{i}=k$ and $p a\left(X_{i}\right)=j$. The $\theta_{i j k}$ that maximizes $L(\theta \mid D)$ is called MLE, and is shown in Equation (4):

$$
\theta_{i j k}=\frac{N_{i j k}}{\sum_{k=1}^{r_{i}} N_{i j k}}=\frac{N_{i j k}}{N_{i j}}
$$

where $N_{i j}$ denotes the number of samples that satisfy $p a\left(X_{i}\right)=j$.
MAP is usually used for a sample set with an insufficient sample size and no missing data. Assuming that the prior distribution, $P(\theta)$, of the BN parameter satisfies the Dirichlet distribution $D\left(\alpha_{i j 1}, \alpha_{i j 1}, \cdots \alpha_{i j r_{j}}\right)$, and since the Dirichlet distribution is a conjugate family of polynomial distributions, the posterior distribution $P(\theta \mid D)$ also satisfies the Dirichlet distribution, which is expressed in Equation (5):

$$
P(\theta \mid D) \propto \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \prod_{k=1}^{r_{i}} \theta^{N_{i j k}+\alpha_{i j k}-1}
$$

At this point, the logarithmic likelihood function for the BN is defined in Equation (6):

$$
\log P(\theta \mid D)=\log P(\theta) P(D \mid \theta)-c
$$

where $c$ is a constant. The $\theta_{i j k}$ that maximizes $P(\theta \mid D)$ is called MAP, and is shown in Equation (7):

$$
\theta_{i j k}=\frac{N_{i j k}+\alpha_{i j k}}{\sum_{k=1}^{r_{i}} N_{i j k}+\alpha_{i j k}}
$$

where $\alpha_{i j k}$ is the hyperparameter of the Dirichlet distribution.

# 2.2. Parameter Constraints 

Parameter constraints refer to the constraint relationships between the conditional probabilities of a BN given by domain experts. There are generally five types of parameter constraints.

1. Axiomatic constraint.

This constraint defines a special sum-of-parameters relationship and is given in Equation (8). The sum of the probabilities of the various states of the child nodes with constant parent combinations is 1 .

$$
\sum_{k=1}^{r_{i}} \theta_{i j k}=1,0 \leq \theta_{i j k} \leq 1, \forall i, j, k
$$

2. Range constraint.

This constraint defines the upper and lower bounds of the parameter and is given in Equation (9).

$$
0 \leq \alpha_{i j k} \leq \theta_{i j k} \leq \beta_{i j k} \leq 1
$$

where $\alpha_{i j k}$ and $\beta_{i j k}$ are the bounds of the parameter.
3. Approximate equality constraint.

This constraint defines the approximate equality relationship between the parameters and is given in Equation (10).

$$
\theta_{i j k} \approx \theta_{i^{\prime} j^{\prime} k^{\prime}}, \forall i j k \neq i^{\prime} j^{\prime} k^{\prime}
$$

Equation (10) is not easy to apply, so the form of Equation (11) is usually adopted:

$$
\left|\theta_{i j k}-\theta_{i^{\prime} j^{\prime} k^{\prime}}\right|<\varepsilon, \forall i \neq i^{\prime}, j \neq j^{\prime}, k \neq k^{\prime}
$$

where $\varepsilon$ is a very small positive rational number.
4. Inequality constraint.

This constraint defines the inequality relationship between the parameters and includes three types that are given in Equations (12)-(14):

- Intra-distribution constraint:

$$
\theta_{i j k} \leq \theta_{i j k^{\prime}}, \forall k \neq k^{\prime}
$$

- Cross-distribution constraint:

$$
\theta_{i j k} \leq \theta_{i j^{\prime} k}, \forall j \neq j^{\prime}
$$

- Inter-distribution constraint:

$$
\theta_{i j k} \leq \theta_{i^{\prime} j^{\prime} k^{\prime}}, \forall i \neq i^{\prime}, j \neq j^{\prime}, k \neq k^{\prime}
$$

5. Synergy constraint.

This constraint defines the inequality relationship between the sum or product of multiple parameters and includes two types that are given in Equations (15) and (16):

- Additive synergy constraint:

$$
\theta_{i j_{1} k}+\theta_{i j_{2} k} \leq \theta_{i j_{3} k}+\theta_{i j_{4} k}, \forall j_{1} \neq j_{2} \neq j_{3} \neq j_{4}
$$

- Product synergy constraint:

$$
\theta_{i j_{1} k} \cdot \theta_{i j_{2} k} \leq \theta_{i j_{3} k} \cdot \theta_{i j_{4} k}, \forall j_{1} \neq j_{2} \neq j_{3} \neq j_{4}
$$

# 2.3. Whale Optimization Algorithm 

The whale optimization algorithm (WOA) is a meta-heuristic intelligent optimization algorithm proposed by Mirjalili [26], inspired by the natural phenomenon of the predatory behavior of humpback whales. This algorithm has the advantages of a high optimization accuracy and few control factors, and has been applied in many fields such as photovoltaic power generation [27], resource scheduling [28], and path planning [29]. In addition, some scholars have made improvements to the whale algorithm [30-32].

The WOA is divided into three parts, namely encircling prey, bubble-net attacking (exploitation phase), and the search for prey (exploration phase).

1. Encircling prey:

The WOA assumes that the position of the individual that reaches the optimal solution in the current population is the prey position, and then other whales will move towards that position for the purpose of encirclement. The mathematical model for encircling prey is expressed in Equations (17)-(20):

$$
\begin{gathered}
\vec{D}=\left|\vec{C} \cdot \vec{X}^{*}(t)-\vec{X}(t)\right| \\
\vec{X}(t+1)=\vec{X}^{*}(t)-\vec{A} \cdot \vec{D} \\
\vec{A}=2 \vec{a} \vec{r}_{1}-\vec{a} \\
\vec{C}=2 \vec{r}_{2}
\end{gathered}
$$

where $t$ is the iteration number, $\vec{X}^{*}(t)$ is the optimal position, and $\vec{X}(t)$ is the individual position. $\vec{A}$ and $\vec{C}$ are the coefficient vectors determined by $\vec{a}, \vec{r}_{1}$, and $\vec{r}_{2} . \vec{a}$ decreases linearly from 2 to 0 with each iteration. $\vec{r}_{1}$ and $\vec{r}_{2}$ are random vectors in $[0,1]$.
2. Bubble-net attacking (exploitation phase)

Bubble-net attacking consists of two parts: shrinking the encircling mechanism and the spiral updating position. When $|\vec{A}| \leq 1$, the former is realized in Equations (17) and (18). The mathematical model of the latter is expressed in Equations (21) and (22):

$$
\begin{gathered}
\vec{D}^{\prime}=\left|\vec{X}^{*}(t)-\vec{X}(t)\right| \\
\vec{X}(t+1)=\vec{X}^{*}(t)+\vec{D}^{\prime} \cdot e^{b l} \cdot \cos (2 \pi l)
\end{gathered}
$$

where $b$ defines the shape of the logarithmic helix, and $l$ is a random number in $[-1,1]$.
When the whales implement bubble-net attacking, the shrinking of the encirclement and the spiral update occur simultaneously. To model simultaneity, it is assumed that there is a $50 \%$ probability of selecting one of the behaviors each time, as shown in Equation (23):

$$
\vec{X}(t+1)=\left\{\begin{array}{cc}
\vec{X}^{*}(t)-\vec{A} \cdot \vec{D} & \text { if } p<0.5 \\
\vec{X}^{*}(t)+\vec{D}^{\prime} \cdot e^{b l} \cdot \cos (2 \pi l) & \text { if } p \geq 0.5
\end{array}\right.
$$

where $p$ is a random number in $[0,1]$.
3. Search for prey (exploration phase)

When $|\vec{A}|>1$, whales search randomly according to each other's position. The mathematical model is expressed in Equations (24) and (25):

$$
\begin{gathered}
\vec{D}=\left|\vec{C} \cdot X_{\text {rand }}^{-1}(t)-\vec{X}(t)\right| \\
\vec{X}(t+1)=X_{\text {rand }}^{-1}(t)-\vec{A} \cdot \vec{D}
\end{gathered}
$$

where $X_{\text {rand }}^{-1}(t)$ is the position vector of a random individual in the current population.

## 3. Structure Establishment of Situation Assessment BN

In this section, the influencing factors of the target intention are enumerated, and the structure of the situation assessment BN is established based on their dependencies.

When a target performs a mission, its intention can be reflected by its attributes and state to a certain extent. Firstly, by restricting the range of missions that the target can perform, the target type is an important attribute to infer the intention. Secondly, relative motion is the movement trend of the target relative to our UAVs, which can indicate that the target is approaching or leaving our UAVs. Finally, the relative velocity and relative height between the target and our UAVs are able to serve as an auxiliary basis for inferring the target intention. Therefore, the BN for intention inference is shown in Figure 1.

![img-0.jpeg](img-0.jpeg)

**Figure 1.** Intention inference BN.

Similar to target intention inference, target type recognition requires obtaining target information, which generally includes the velocity, height, radar cross-section (RCS), and radar frequency band variability (RFV) of the target. Therefore, the BN for type recognition is shown in Figure 2.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Type recognition BN.

The relative motion trend of the target is determined based on the distance and bearing relative of the target to our UAVs. Therefore, the BN for relative motion determination is shown in Figure 3.

![img-2.jpeg](img-2.jpeg)

**Figure 3.** Relative motion determination BN.

By connecting the three sub-networks in Figures 1-3 into a multi-layer BN, the structure of the situation assessment BN is established, as shown in Figure 4. Among them, the light-colored nodes such as velocity, height, etc., are the base nodes, and their states can be obtained via observation. The three dark-colored nodes, namely target intention, target type, and relative motion, are the hidden nodes that use base nodes as their child nodes. In conjunction with the CPTs and the states of the child nodes, the probabilities of each state of the hidden nodes are calculated and acquired. The relevant information on each node in the network is shown in Table 1.
![img-3.jpeg](img-3.jpeg)

Figure 4. Situation assessment BN.
Table 1. Relevant information on the nodes.


${ }^{1}$ Air-borne early warning. ${ }^{2}$ Electronic jamming aircraft. ${ }^{3}$ Reconnaissance plane.

# 4. IWOA-PPI for Parameter Learning 

The establishment of the structure for a situation assessment BN is introduced in Section 3, and the IWOA-PPI for parameter learning is discussed in detail in this section. The parameter learning problem is treated as an unconstrained optimization problem in the PPIs, and the objective function can be acquired using Equation (3). The idea of the IWOA-PPI is to transform parameter constraints into PPIs, and then use the improved WOA to search for the optimal parameters. In this way, the algorithm has the advantages of Bayesian estimation, which fully utilizes prior information, and constrained optimization, which fully utilizes sample data. Therefore, the key to the algorithm is the PPIs and the improvements to the WOA. The former has the ability to mine the parameter prior information embedded in the expert knowledge, thereby improving the accuracy of the parameter learning. For the latter, since the original WOA has the shortcomings of a slow convergence speed, an inability to jump out of the local optima, and difficulty in reaching the global optima, it is necessary to make appropriate improvements to accelerate the search speed and enhance the global optimization ability. In this section, the establishment

of the PPIs is described in Section 4.1, and the improvements to the WOA are explained in Sections 4.2-4.4.

# 4.1. Parameter Prior Interval 

Expert knowledge is defined as the qualitative parameter relationships that are summarized by domain experts based on physical phenomena or objective laws. The knowledge contains prior information of the parameters and is typically represented as parameter constraints. In order to make full use of prior knowledge, the concept of PPIs is proposed.

PPIs are essentially the intervals bounded by the upper and lower bounds of the parameters, formally equivalent to the range constraint of Equation (9), but fundamentally different from general parameter constraints. Firstly, the PPI is a concise upper and lower bound form, but the parameter constraints are embodied in a variety of more complex forms. Secondly, the PPI is transformed by extracting the prior information of the parameters in the parameter constraints, so the prior knowledge can be fully utilized. Finally, compared to parameter constraints, PPIs narrow the parameters' feasible domain to a more precise region, which accelerates the subsequent IWOA speed and improves its accuracy.

PPIs are obtained in three steps:

1. By performing MC sampling on the parameter space delimited by the parameter constraints, the parameters without samples are obtained using Equation (26):

$$
\theta_{i j k}^{M C}=P\left(X_{i}=k, p a\left(X_{i}\right)=j \mid \Omega\right)=\frac{\sum_{i=1}^{S} P_{l}\left(X_{i}=k, p a\left(X_{i}\right)=j \mid \Omega\right)}{S}
$$

where $\Omega$ denotes the parameters constraints, $S$ denotes the number of samples of MC sampling, $P_{l}\left(X_{i}=k, p a\left(X_{i}\right)=j \mid \Omega\right)$ denotes the value of $\theta_{i j k}^{l}$ for a single sample, and $\theta_{i j k}^{M C}$ denotes the mean value of all $\theta_{i j k}^{l}$ for $S$ samples. $\theta_{i j k}^{M C}$ is the parameter obtained via MC sampling without considering the samples. Its numerical value is close to the true parameter to some extent, and the degree of closeness is positively related to the number of constraints.
2. Using the interval transform formulas, the uncorrected PPIs are obtained. $\theta_{i j k}^{M C}$ $\left(k=1,2, \ldots, r_{i}\right)$ are denoted from small to large, as shown in Equation (27):

$$
\theta_{i j k_{1}}^{M C} \leq \theta_{i j k_{2}}^{M C} \leq \ldots \leq \theta_{i j k_{m}}^{M C} \leq \ldots \leq \theta_{i j k_{r_{i}}}^{M C}
$$

where $k_{m} \in\left\{1,2, \ldots, r_{i}\right\} . d_{k_{m}}^{\text {low }}$ is defined as the lower bound interval of $\theta_{i j k_{m}}^{M C}, d_{k_{m}}^{\text {up }}$ is defined as the upper bound interval of $\theta_{i j k_{m}}^{M C}$, and $\left[\theta_{i j k_{m}}^{M C}-d_{k_{m}}^{\text {low }}, \theta_{i j k_{m}}^{M C}+d_{k_{m}}^{\text {up }}\right]$ is the uncorrected PPI of $\theta_{i j k_{m}}^{M C}$. The determination of $d_{k_{m}}^{\text {low }}$ and $d_{k_{m}}^{\text {up }}$ needs to be categorized into two cases:

- When $\theta_{i j k_{1}}^{M C}<\theta_{i j k_{2}}^{M C}<\ldots<\theta_{i j k_{m}}^{M C}<\ldots<\theta_{i j k_{r_{i}}}^{M C}$, the interval transform formulas of $\theta_{i j k_{m}}^{M C}$ are implemented as Equations (28) and (29):

$$
\begin{aligned}
& d_{k_{m}}^{\text {low }}=\frac{\theta_{i j k_{m}}^{M C}-\theta_{i j k_{m-1}}^{M C}}{\theta_{i j k_{m}}^{M C} / \theta_{i j k_{m-1}}^{M C}} \\
& d_{k_{m}}^{\text {up }}=\frac{\theta_{i j k_{m+1}}^{M C}-\theta_{i j k_{m}}^{M C}}{\theta_{i j k_{m+1}}^{M C} / \theta_{i j k_{m}}^{M C}}
\end{aligned}
$$

For $\theta_{i j k_{1}}^{M C}, d_{k_{1}}^{\text {up }}$ is calculated first, and then $d_{k_{1}}^{\text {low }}=d_{k_{1}}^{\text {up }}$. For $\theta_{i j k_{r_{i}}}^{M C}, d_{k_{r_{i}}}^{\text {low }}$ is calculated first, and then $d_{k_{r_{i}}}^{\text {up }}=d_{k_{r_{i}}}^{\text {low }}$.

- When $\theta_{i j k_{p}}^{M C}=\theta_{i j k_{p+1}}^{M C}=\ldots=\theta_{i j k_{p+q}}^{M C}$, the interval transform formulas of $\theta_{i j k_{m}}^{M C}$ are implemented as Equation (30):

$$
d_{k_{m}}^{i n w}=d_{k_{m}}^{n p}=\frac{\omega \cdot\left(\theta_{i j k_{p}}^{M C}+\theta_{i j k_{p+1}}^{M C}+\ldots+\theta_{i j k_{p+q}}^{M C}\right)}{q}
$$

where $\omega$ is the weight coefficient that takes a small value.
3. Combining the parameter constraints, the PPIs are obtained. The uncorrected PPIs may violate some parameter constraints, so the intersection of the parameter constraints and the uncorrected PPIs is sought to obtain the PPIs. For example, in order to satisfy the axiomatic constraint, the lower bound interval, $d_{k_{1}}^{i n w}$, of $\theta_{i j k_{1}}^{M C}$ is $\max \left(0, \theta_{i j k_{1}}^{M C}-d_{k_{1}}^{i n w}\right)$ and the upper bound interval, $d_{k_{1}}^{n p}$, of $\theta_{i j k_{1}}^{M C}$ is $\min \left(\theta_{i j k_{1}}^{M C}+d_{k_{1}}^{n p}, 1\right)$.

# 4.2. Variable Encircling Factor 

Aimed at the encircling prey behavior, a variable encircling factor is proposed to enhance the local search ability of the WOA.

The value range of $\vec{C} \cdot \vec{X}^{*}(t)$ in Equation (17) is $\left[\overrightarrow{0}, 2 \vec{X}^{*}(t)\right]$. The physical meaning of $\left[\overrightarrow{0}, 2 \vec{X}^{*}(t)\right]$ refers to a high-dimensional neighborhood. This neighborhood is centered on the current optimal position, $\vec{X}^{*}(t)$, and the range of each dimension is $\left[0,2 X_{i}^{*}(t)\right]$. This neighborhood is embodied as a rectangle in two dimensions, a rectangular body in three dimensions, and a hyper-cuboid in high dimensions. The encircling prey behavior of Equations (17) and (18) is a random selection of a point, $\vec{C} \cdot \vec{X}^{*}(t)$, within the neighborhood, $\left[\overrightarrow{0}, 2 \vec{X}^{*}(t)\right]$, and then all whale individuals shrink and move from their current position, $\vec{X}(t)$, to $\vec{C} \cdot \vec{X}^{*}(t)$.
$\vec{C}$ is defined as the encircling factor, and its value range determines the size of $\left[0,2 X_{i}^{*}(t)\right]$. In the original WOA, all dimensional variables of $\vec{r}_{2}$ in Equation (20) obey the uniform distribution, $U(0,1)$; i.e., all dimensional variables of $\vec{C}$ obey the uniform distribution, $U(0,2)$. As the algorithm runs, $\vec{X}^{*}(t)$ gradually approaches the optimal position. Since the neighborhood $\left[\overrightarrow{0}, 2 \vec{X}^{*}(t)\right]$ is too large, this leads to a large number of invalid local searches. Therefore, a variable encircling factor, $\vec{C}^{V}$, obeying the normal distribution, is proposed as Equation (31):

$$
p\left(C_{i}^{V}\right)=\frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{\left(C_{i}^{V}-1\right)^{2}}{2 \sigma^{2}}}
$$

where $C_{i}^{V}$ is a one-dimensional variable of $\vec{C}^{V}$.
The variability of the variable encircling factor, $\vec{C}^{V}$, is reflected in $\sigma$ : firstly, the value of $\sigma$ is very large at the beginning of the algorithm. At this moment, the distribution of $C_{i}^{V}$ degenerates from the normal distribution, $N\left(1, \sigma^{2}\right)$, to the uniform distribution, $U(0,2)$, and it means a degeneration towards the original WOA. Secondly, after certain iterations, make $3 \sigma$ equal to 1 , and then $C_{i}^{V}$ obeys the normal distribution, $N(1,1 / 3)$. Then, the $3 \sigma$ area of $C_{i}^{V}$ is $[0,2]$, which significantly increases the probability of $\vec{C} \cdot \vec{X}^{*}(t)$ approaching $\vec{X}^{*}(t)$. Finally, $3 \sigma$ decreases gradually to 0.1 at the later stage of the algorithm, and the $3 \sigma$ area of $C_{i}^{V}$ becomes $[0.9,1.1]$ in the end. The process of changing $\sigma$ shrinks the local search area to accelerate the local search speed.

4.3. Nonlinear Convergence Factor

The WOA performs a global search in the exploration phase and a local search in the exploitation phase, and switches between the two phases based on control coefficient $\vec{A}$, determined as $a$. As $a$ decreases linearly, both global and local searches are performed in the early stages $(a>1)$, and only a local search is performed in the later stages $(a \leq 1)$. However, when dealing with certain optimization problems, the linear convergence factor $a$ makes the algorithm enter the later phase so early that a sufficient global search has not been performed in the early stage. Therefore, the global optimal solution cannot be found. To overcome this problem, a nonlinear convergence factor, $a_{n l}$, is proposed as Equation (32):

$$
a_{n l}=2 \cdot \cos \left(\frac{\pi}{2} \cdot \frac{t}{t_{\max }}\right)
$$

where $t$ is the iteration number and $t_{\max }$ is the maximum iteration number.
The curves of $a$ and $a_{n l}$ with iterations are shown in Figure 5. As shown in Figure 5, $a_{n l}$ has two characteristics: firstly, from the perspective of the number of iterations, the number of iterations where $a>1$ is 250 , while the number of iterations where $a_{n l}>1$ is extended to about 330. This indicates that $a_{n l}$ increases the number of iterations where $\left|\vec{A}_{n l}\right|>1$. Secondly, from the perspective of the value, when $a>1$ and $a_{n l}>1, a_{n l}$ is always greater than $a$, except for the beginning iteration, where $a=a_{n l}$. This indicates that $a_{n l}$ makes it easier for $\left|\vec{A}_{n l}\right|$ to exceed 1 compared to $|\vec{A}|$. The above two characteristics mean that $a_{n l}$ increases the probability of the global search. In addition, the decreasing trend of $a_{n l}$ is gentle in the early stage and sharp in the later stage, which means that the algorithm performs more global searches in the early stage and faster local searches in the later stage. The above indicates that $a_{n l}$ has the ability to balance the global and local search of the algorithm better. In a word, the performance of WOA is improved by $a_{n l}$.
![img-4.jpeg](img-4.jpeg)

Figure 5. Curves of two convergence factors. The blue curve refers to $a$ and the black curve refers to $a_{n l}$.

# 4.4. Simulated Annealing Strategy Incorporating Levy Flight 

Simulated annealing [33] has the ability to jump out of local optima through the Metropolis criterion, and Levy flight [34] has the ability to enhance the randomness of the search. Therefore, a simulated annealing strategy incorporating Levy flight is proposed. This strategy utilizes Levy flight for position updating and the Metropolis criterion to jump out of local optima, thereby enhancing the global search ability of the WOA.

Levy flight refers to random walks with step sizes that satisfy the heavy-tailed distribution. Due to the alternating characteristics of a short-distance search and occasional long-distance wander, the random walks are used to simulate animal foraging in nature. The Levy distribution is usually realized with the Mantegna algorithm, and the step length, $s$, is defined in Equation (33):

$$
s=\frac{u}{|v|^{1 / \beta}}
$$

where $\operatorname{Levy}(\beta) \sim s^{-1-\beta}, 0<\beta \leq 2$, and the general value of $\beta$ is 1.5. $u \sim N\left(0, \sigma_{u}^{2}\right)$; $v \sim N(0,1) \cdot \sigma_{u}^{2}$ is defined in Equation (34):

$$
\sigma_{u}=\left\{\frac{\Gamma(1+\beta) \sin \left(\frac{\pi \beta}{2}\right)}{\Gamma\left(\frac{1+\beta}{2}\right) \beta 2^{(\beta-1) / 2}}\right\}^{1 / \beta}
$$

The position updating of Levy flight is shown in Equation (35):

$$
X_{i}(t+1)=X_{i}(t)+\alpha \otimes \operatorname{Levy}(\beta)
$$

where $\alpha$ is the step size control factor and $\operatorname{Levy}(\beta)$ is the step length of the Levy flight.
Simulated annealing comes from the simulation of the solid annealing cooling process. The core idea is to accept inferior solutions with a certain probability using the Metropolis function, thereby achieving the goal of jumping out of local optima. The Metropolis function is defined in Equation (36):

$$
p=\left\{\begin{array}{cl}
1 & \Delta f>0 \\
\exp (-\Delta f / T) & \Delta f \leq 0
\end{array}\right.
$$

where $p$ is the probability of accepting inferior solutions, $\Delta f$ is the increment of the objective function, and $T$ is the current temperature. $T \in\left[T_{\text {end }}, T_{0}\right], T_{0}$ and $T_{\text {end }}$ refer to the initial temperature and the end temperature, respectively.

Assuming that population 1 is obtained via an iteration of the WOA, and population 2 is obtained after using Equation (35) to update the positions of the individuals in population 1, comparing the fitness of the individuals in the two populations, if the fitness of an individual in population 2 is better than that in population 1, the corresponding individual in population 1 is replaced; otherwise, the corresponding individual in population 1 is replaced with the probability $(p)$ of Equation (36). The population obtained through the Metropolis function is population 3, which serves as the initial population for the next iteration of the WOA.

In summary, the pseudo-code of the IWOA-PPI is shown in Algorithms 1.

```
Algorithms 1 Pseudo-code of the IWOA-PPI
    01 : Initialize the whales population \(X_{l}(l=1,2, \ldots, m)\) in the parameter prior internals
    02 : Calculate the fitness of each search agent
    \(03: T=T_{0}, X^{*}=\) the best search agent
    04 : While \((t<\) maximum number of iterations)
    05: for each search agent
    06: Update \(a_{n l}, A_{n l}, C^{V}, l\), and \(p\)
    07: if1 \((p<0.5)\)
    08: if2 \((|A|<1)\)
    09: Update the position \(X_{l}\) of the current search agent by the Equation (18)
    10: else if2 \((|A| \geq 1)\)
    11: Select a random search agent \(\left(X_{\text {rand }}\right)\)
    12: Update the position \(X_{l}\) of the current search agent by the Equation (25)
    13: else if2
    14: else if1 \((p \geq 0.5)\)
    15: Update the position \(X_{l}\) of the current search agent by the Equation (22)
    16: else if1
    17: Update the position \(X_{l}^{L e r y}\) of the current search agent by the Equation (35)
    18: Check if \(X_{l}\) or \(X_{l}^{L e r y}\) goes beyond the search space and amend it
    19: Calculate the fitness of \(X_{l}\) and \(X_{l}^{L e r y}\)
    20: \(\Delta f=f\left(X_{l}^{L e r y}\right)-f\left(X_{l}\right)\)
    21: if3 \((\Delta f>0)\) or random \((0,1) \leq p(\Delta f, T)\)
    22: \(\quad X_{l} \leftarrow X_{l}^{L e r y}\)
    23: end if3
    24: end for
    25: Update \(X\) * if there is a better solution
    26: Update \(T\)
    27: \(\quad t=t+1\)
    28 : end while
    29 : return \(X^{*}\)
```


# 5. Experiment and Discussion 

In the experiment for the standard BNs, including MLE, MAP, QMAP, WOA, and the IWOA-PPI proposed in this article, five algorithms are used to learn the parameters of four standard BNs. In the experiment for the situation assessment BN, the parameters of the situation assessment BN in Figure 4 are learned by the IWOA-PPI, and then the learned parameters are used to evaluate the target's situation.

Both the two experiments are simulated in MATLAB 2018b. The construction and inference of the BNs, the collection of the sample data, and the MLE and MAP algorithms are achieved with the BNT toolbox. The QMAP, WOA, and IWOA-PPI are validated with the assistance of the BNT toolbox.

### 5.1. Experiment for the Standard BNs

The KL divergence [35] is used to measure the accuracy of the parameter learning results, which is defined in Equation (37):

$$
K L(\theta \mid \hat{\theta})=\frac{1}{\sum_{i=1}^{n} r_{i} q_{i}} \sum_{i=1}^{n} \sum_{j=1}^{q_{j}} \sum_{k=1}^{r_{i}} \theta_{i j k} \log \frac{\theta_{i j k}}{\hat{\theta}_{i j k}}
$$

where $\theta_{i j k}$ denotes the true parameter, and $\hat{\theta}_{i j k}$ denotes the learned parameter. The smaller the KL divergence is, the more accurate the learned parameters are.

To verify the universality and effectiveness of the IWOA-PPI, four different sizes of BNs are adopted as learning objects, and the basic information of the four BNs is shown in Table 2. According to the number of nodes, arcs, and parameters, the standard BNs are categorized into four scales, namely small, medium, large, and very large.

Table 2. Information of 4 BNs.


The sample sizes are set to $40,80,120,160$, and 200 , and the training samples are generated with the BNT toolbox. Except for synergy constraints, all kinds of constraints in Section 2 are considered and randomly selected. For example, the structure and CPTs of the Asia BN are shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. Structure and conditional probability tables of the Asia BN.
According to the CPTs of the Asia BN, three typical constraints are as follows:

- Range constraint. For example, $0.8 \leq P(\operatorname{tub}=0 \mid \operatorname{asia}=0) \leq 0.1$;
- Approximate equality constraint. For example, $P($ either $=0 \mid$ tub $=0$, lung $=0) \approx P$ $($ either $=1 \mid$ tub $=0$, lung $=1)$;
- Inequality constraint. For example, $P($ bronc $=0 \mid$ smoke $=0)>P($ bronc $=1 \mid$ smoke $=1)$.

After the samples and constraints are prepared, the five algorithms are used to learn the parameters of each network 20 times at different sample sizes, and the expectation and variance of the KL divergences are calculated. The KL divergences are represented as expectation $\pm$ standard deviation in Table 3. The comparisons of the KL divergences of the five algorithms are shown in Figures 7-10. The horizontal axis represents the number of the sample, and the vertical axis represents the value of the KL divergence. Due to the significant differences in the KL divergences of the various algorithms, there are four graphs for each network. Graph (a) shows the KL divergences of the five algorithms, Graph (b) shows those of MLE, Graph (c) shows those of MAP and the WOA, and Graph (d) shows those of QMAP and the IWOA-PPI.

![img-6.jpeg](img-6.jpeg)

Figure 7. (a) KL divergences of 5 algorithms for the Asia BN. (b-d) KL divergences with error bars.
Table 3. KL divergences of five algorithms.


Table 3. Cont.


![img-7.jpeg](img-7.jpeg)

Figure 8. (a) KL divergences of 5 algorithms for the Alarm BN. (b-d) KL divergences with error bars.

![img-8.jpeg](img-8.jpeg)

**Figure 9.** (**a**) KL divergences of 5 algorithms for the Win95pts BN. (**b–d**) KL divergences with error bars.

From Table 3 and Figures 6–9, the following is clear:

1. The accuracy ranking of the five algorithms is **IWOA-PPI > QMAP > WOA > MAP > MLE**. There are roughly three levels of accuracy, the lowest level for **MLE**, the medium level for the **WOA** and **MAP**, and the highest level for the **IWOA-PPI** and **QMAP**.
2. For all networks and sample sizes, the **IWOA-PPI** proposed in this article has the smallest KL divergence among the five parameter-learning algorithms, which means that the learning results are the most accurate. The highest accuracy of the **IWOA-PPI** indicates that, in contrast to the **QMAP** and **WOA**, the **IWOA-PPI** absorbs the advantages of the Bayesian estimation and constrained optimization methods, and fully extracts information from both parameter constraints and sample data.
3. Comparing the **WOA** and the **IWOA-PPI**, the KL divergence of the former is about three times that of the latter. This indicates that the improvements in Section 4 significantly enhance the optimization ability of the **WOA**.

![img-9.jpeg](img-9.jpeg)

**Figure 10.** (**a**) KL divergences of 5 algorithms for the Andes BN. (**b**–**d**) KL divergences with error bars.

### 5.2. Experiment for the Situation Assessment BN

The experiment for the situation assessment BN includes two parts:

- Use the IWOA-PPI to learn the parameters of the situation assessment BN in Figure 4;
- For the assumed mission scenario, substitute the learned parameters into the situation assessment BN, and use this BN to evaluate the operational intentions of the opposing targets, i.e., the opposing situation.

### 5.2.1. Parameter Learning of the Situation Assessment BN

The parameter-learning process of the situation assessment BN is the same as that of the standard BNs. Using the function "sample_bnet" of the BNT toolbox, the samples are generated in the same way. However, the constraints of the situation assessment BN cannot be randomly generated because of the realistic physical meanings. The corresponding relationship between the parameters and the CPTs of nodes is introduced first, and then some examples of the constraints are listed.

The true parameters of the situation assessment BN are shown in Table 4, and the CPTs of the node intention, target type, and relative motion are displayed. Taking the target type node as an example, when the intention is patrol, the probability that the target type is AEW is 0.6, and this probability is denoted as the parameter *θ*_{211} = 0.6. According

to Table 1, the number of the target type node is two. Corresponding the state notation $\{p, r, e, a\}$ of the intention to $\{1,2,3,4\}$ and the state notation $\{a, r, e, f\}$ of the target type to $\{1,2,3,4\}$, the whole CPT between the target type and the intention is denoted as the parameters $\theta_{2 j k}$, in which $j, k \in\{1,2,3,4\}$.

Table 4. True parameters in the form of conditional probability tables.


After discussing the corresponding relation between the CPT and the parameters, some typical constraints of the situation assessment BN are shown below with the explanation of their physical meanings.

- Range constraint. $\theta_{233}=P($ target type $=3 \mid$ intention $=3), 0.6 \leq \theta_{233} \leq 1$. When the intention is jamming and the target type is EJA, the range of the conditional probability, $P($ target type $\mid$ intention), is $[0.6,1]$. This indicates that if the target is performing the jamming mission, it has at least a $60 \%$ chance of being the EJA. Since the probability cannot be greater than one, the range is $[0.6,1]$.

- Approximate equality constraint. $\theta_{411}=P($ relative motion $=1 \mid$ intention $=1)$, $\theta_{412}=P($ relative motion $=2 \mid$ intention $=1), \theta_{411} \approx \theta_{412}$. The conditional probability when the intention is patrol and the relative motion is approach is approximately equal to the one when the intention is patrol and the relative motion is leave. When performing the patrol mission, in order to ensure comprehensive air surveillance of the defense focus, the AEW sets the defense focus as the center of the circle and flies around it according to a certain patrol radius and patrol speed. Since the target makes a circular flight in a fixed area, the approach and leave of the target have no influence on our UAVs. Therefore, when the intention is patrol, the probabilities of approach and leave are approximately equal.
- Inequality constraint. $\theta_{721}=P($ height $=1 \mid$ target type $=2), \theta_{722}=P($ height $=2 \mid$ target type $=2), \theta_{723}=P($ height $=3 \mid$ target type $=2), \theta_{721}<\theta_{723}, \theta_{722}<\theta_{723}$. The conditional probability when the target type is RP and the height is low altitude is smaller than the one when the target type is RP and the height is high altitude. So is the one when the target type is RP and the height is medium altitude. Because the RP is often at high altitude when conducting reconnaissance, the conditional probability, $P($ height $=3 \mid$ target type $=2)$, is the highest.
With the structure of the situation assessment BN, the samples, and the constraints, the parameters learned by the IWOA-PPI are shown in Table 5. The KL divergence between the true parameters and the learned parameters is 0.1123 , and it indicates that they are close enough that the former can be completely replaced by the latter to evaluate the situation.

Table 5. Learned parameters in the form of conditional probability tables.


Table 5. Cont.


# 5.2.2. Result of Situation Assessment 

To assess the situations of the targets, there are three contents to be completed. Firstly, an assumed mission scenario is constructed. Secondly, the observed evidence of the targets is collected. At last, the situation assessment BN is used on all the targets to acquire the results.

1. The description of the assumed mission scenario. The existing entities in the environment are several UAVs perceiving the situation and a ground radar belonging to us. An AEW, an RP, an EJA, and a fighter belong to the other side. The assumed missions of the opposing targets are: in the beginning, the AEW is patrolling with a fighter, the RP is conducting reconnaissance and the EJA has no clear mission. After a while, the ground radar is discovered by the RP. Then, the EJA starts to fly towards the radar and implement electronic jamming, and the fighter stops escorting the AEW and assaults the radar after the electronic jamming takes effect.
2. The acquisition of the observed evidence. The observed evidences are necessary for situation assessment and are transferred from the attributes and states of the targets. Since the attributes and states are continuous variables, and the evidences in the form of probabilities are discrete variables. Then, fuzzy discretization is used to acquire the evidences. Taking the height node as an example, the process to acquire the observed evidence is as below.

- The construction of the membership function. The fuzzy membership function of the height node is defined as Equation (38) and shown in Figure 11.

$$
\begin{aligned}
& \mu_{H, 1}=\left\{\begin{array}{cc}
1 & 0 \leq H<5000 \\
-H / 2000+7 / 2 & 5000 \leq H<7000 \\
0 & \text { other }
\end{array}\right. \\
& \mu_{H, 2}=\left\{\begin{array}{cc}
H / 3000-5 / 3 & 5000 \leq H<8000 \\
1 & 8000 \leq H<9000 \\
-H / 3000+4 & 9000 \leq H<12,000 \\
0 & \text { other }
\end{array}\right. \\
& \mu_{H, 3}=\left\{\begin{array}{cc}
H / 4000-5 / 2 & 10,000 \leq H<14,000 \\
1 & H \geq 14,000 \\
0 & \text { other }
\end{array}\right.
\end{aligned}
$$

where $\mu_{H, 1}$ denotes the membership of low altitude, $\mu_{H, 2}$ denotes that of medium altitude, and $\mu_{H, 3}$ denotes that of high altitude.

![img-10.jpeg](img-10.jpeg)

Figure 11. The membership function of height.
The unit of height is meters. The green area is $\mu_{H, 1}$, the red area is $\mu_{H, 2}$, and the blue area is $\mu_{H, 3}$. The brown area is the overlap between $\mu_{H, 1}$ and $\mu_{H, 2}$, and the grey area is the overlap between $\mu_{H, 2}$ and $\mu_{H, 3}$.

- The transform from the fuzzy membership to the probability. The probability-possibility transformation formula [36] is defined in Equation (39):

$$
p_{i}(u)=\frac{\mu_{i}(u)^{1 / \alpha}}{\sum_{i=1}^{u} \mu_{i}(u)^{1 / \alpha}}, 0<\alpha<1
$$

where $u$ denotes the attribute or state, $\mu_{i}$ denotes the membership function, and $p_{i}(u)$ denotes the probability. $\alpha$ is 0.5 in this article.

For example, if the height of the target is 6000 m , the fuzzy memberships are according to Equation (38), and the probabilities are [0.6923, 0.3077, 0] according to Equation (39). In this way, the evidences of other attributes or states are acquired. The evidences at a certain moment are shown in Table 6.

Table 6. Observed evidences.


3. The application of the situation assessment BN.

Substituting the learned parameters and the evidences into the situation assessment BN, the results are inferred by the BNT toolbox according to the Bayesian formula. At each moment, the situation assessment BN is used for each target, and the situations at all times constitute the situation of the target for a period of time. The results of the situation assessment for all the targets are shown in Figure 12. The $X$-axis represents the time, the $Y$-axis represents the intention, and the $Z$-axis represents the probability. The height of the bars means the probability value, and the color of the bars means a certain moment like t1.

![img-11.jpeg](img-11.jpeg)

**Figure 12.** (**a**) Situation assessment results of the AEW. (**b**) Situation assessment results of the RP. (**c**) Situation assessment results of the EJA. (**d**) Situation assessment results of the fighter.

In Figure 12a, the probability of patrol is always the highest, which means that the AEW is patrolling all the time. It is discovered that the probability of the patrol before t5 is lower than that after t5, and the reason is that the AEW is approaching before t5 and leaving after t5 when the aircraft is in circular flight. The approaching behavior reduces the probability of patrolling. In Figure 12b, the probability of reconnaissance becomes the highest after t3, which means that the RP is conducting reconnaissance. In the beginning, since the RP is climbing and the heights are low and medium altitude, the true intention is not recognized. In Figure 12c, the probability of jamming becomes the highest after t3. Because the EJA does not have a clear mission in the beginning, the probabilities of patrol and jamming are close before t4. After the EJA starts to perform electronic jamming, the probability of jamming becomes the highest. In Figure 12d, the probability of patrol is the highest before t4, and the probability of assault becomes the highest starting from t4. This indicates a trend that the fighter performs the patrol at first and turns into an assault later, and the trend is the same as the fighter in the assumed mission scenario. According to Figure 12, all the situation assessment results are consistent with the description of the assumed mission scenario, and this proves that the situation assessment method proposed in this article is correct and feasible.

# 6. Conclusions 

In this article, the situation assessment BN is established to evaluate the situation of the targets, and an improved whale optimization algorithm based on parameter prior intervals (IWOA-PPI) is proposed for parameter learning. In the IWOA-PPI, the prior knowledge embedded in the parameter constraint is maximally mined based on the PPIs, and the performance of the original WOA is enhanced by a variable encircling factor, a nonlinear convergence factor, and a simulated annealing strategy incorporating Levy flight. The experiment for the standard BNs proves that the parameter-learning algorithm proposed in this article is able to effectively learn parameters with optimal learning accuracy. The experiment for the situation assessment BN shows that the situation assessment BN established in this article has the ability to infer the correct intention and understand the situation.

In future research, the algorithm proposed in this article will be explored for application in other fields such as disaster area search and rescue, plant protection, and so on. In addition, work on applying the algorithm of this paper to real UAVs like quad-copters will be carried out.

Author Contributions: Conceptualization, W.L. and W.Z.; methodology, W.L.; software, W.L.; validation, W.L.; formal analysis, W.L.; investigation, W.L. and B.L.; resources, W.L. and W.Z.; data curation, W.L. and B.L.; writing-original draft preparation, W.L.; writing-review and editing, W.L.; visualization, W.L.; supervision, W.L., W.Z., B.L. and Y.G.; project administration, W.Z. and Y.G.; funding acquisition, W.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the National Natural Science Foundation of China, grant No. 62173277 and grant No. 62373301.

Data Availability Statement: Not applicable.
Acknowledgments: The authors are grateful to the Shaanxi Province Key Laboratory of Flight Control and Simulation Technology.

Conflicts of Interest: The authors declare no conflict of interest.

## Abbreviations

The following abbreviations are used in this article:

