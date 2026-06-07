# Article 

## Bayesian Network Structure Learning Using Improved A* with Constraints from Potential Optimal Parent Sets

Chuchao $\mathrm{He}^{1}$, Ruohai $\mathrm{Di}^{1, *}$ and Xiangyuan Tan ${ }^{2}$

## check for updates

Citation: He, C.; Di, R.; Tan, X. Bayesian Network Structure Learning Using Improved A* with Constraints from Potential Optimal Parent Sets. Mathematics 2023, 11, 3344. https:// doi.org/10.3390/math11153344

Academic Editors: Zexun Chen and Bo Wang

Received: 4 July 2023
Revised: 27 July 2023
Accepted: 29 July 2023
Published: 30 July 2023

## 0

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Electronics and Information Engineering, Xi'an Technological University, Xi'an 710021, China; hechuchao@xatu.edu.cn
2 School of Electronic Information, Northwestern Polytechnical University, Xi'an 710192, China; tanxy2017@mail.nwpu.edu.cn

* Correspondence: diruohai@xatu.edu.cn or xfwtdrh@163.com; Tel.: +86-13-72-0450874

Abstract: Learning the structure of a Bayesian network and considering the efficiency and accuracy of learning has always been a hot topic for researchers. This paper proposes two constraints to solve the problem that the A* algorithm, an exact learning algorithm, is not efficient enough to search larger networks. On the one hand, the parent-child set constraints reduce the number of potential optimal parent sets. On the other hand, the path constraints are obtained from the potential optimal parent sets to constrain the search process of the A* algorithm. Both constraints are proposed based on the potential optimal parent sets. Experiments show that the time efficiency of the A* algorithm can be significantly improved, and the ability of the A* algorithm to search larger Bayesian networks can be improved by the two constraints. In addition, compared with the globally optimal Bayesian network learning using integer linear programming (GOBNILP) algorithm and the max-min hill-climbing (MMHC) algorithm, which are state of the art, the A* algorithm enhanced by constraints still performs well in most cases.

Keywords: Bayesian network; structural learning; A* search; constraint; potential optimal parent sets

MSC: 68 T30

## 1. Introduction

Artificial intelligence has been widely used in reality after decades of development. However, capturing and understanding causal relationships from data, known as causal discovery, remains a challenging task in artificial intelligence. Robust causal analysis is widely recognized as a key driver of techniques such as learning, prediction, diagnosis, and counterfactual reasoning, which can have significant implications for almost all fields of science.

A Bayesian network (BN) is a probabilistic graphical model of the combination of probability theory and graph theory, and a BN can support the representation and analysis of causal structure in the field of artificial intelligence. The structure of the BN is a directed acyclic graph (DAG), which represents the dependence relationship between nodes. These relationships are further quantified by a set of conditional probability distributions. In general, a Bayesian network represents the joint probability distribution of a set of random variables.

The number of possible structures increases exponentially with the number of nodes $n$. Determining the BN structure from data is an NP-hard problem [1,2], and it has been a hot topic in the research field of BN in recent decades. Existing BN structure learning algorithms can be divided into three categories: constraint-based, score-based, and hybrid search approaches [3].

Constraint-based approaches use statistical tests or information theory techniques to test conditional independence (CI), determine the relationship between variables, and ob-

tain the corresponding DAG. Widely adopted constraint-based approaches mainly include the Peter-Clark (PC) algorithm [4], inductive causality (IC) algorithm [5], and grow-shrink (GS) algorithm [6]. These algorithms can return equivalence classes if CI tests are correct. However, such assumptions are difficult to satisfy in practice. The CI test is often affected by statistical tests, and there will be a certain probability of error in the case of insufficient samples or noise. Perhaps even worse, because a series of steps in the algorithm relies on CI tests, these erroneous CI test results can further amplify errors in the subsequent learning process.

Score-based approaches are the most common BN structure learning approaches. Score-based approaches use a scoring function to measure the fitness between the BN structure and data, and return the BN structure with the optimal score. Therefore, scorebased approaches treat BN structure learning as a combinatorial optimization problem. From the perspective of combinatorial optimization, greedy search (GS) [7-9], simulated annealing (SA) [10], ordering-based search (OBS) [11], and other algorithms have developed rapidly in the early stage. In addition, the genetic algorithm (GA) [12], particle swarm optimization (PSO) [13], ant colony optimization (ACO) [14], and other swarm intelligence algorithms have also been widely used. However, these algorithms often obtain locally optimal network structures; in particular, swarm intelligence algorithms' convergence to the optimal solution in infinite time has no practical significance. Therefore, exact learning algorithms have begun to enter the field of vision of researchers. Research on exact learning algorithms began with a series of dynamic programming (DP) algorithms [15-17], which require exponential time and space complexity and can only be used for small-scale network structure learning. In recent years, other exact learning algorithms that are more competitive than DP algorithms have also been proposed, such as the A* [18,19], anytime window A* $\left(\mathrm{AWA}^{*}\right)$ [20], Bidirectional heuristic search (BiHS) [21], CPBayes [22], and Globally Optimal Bayesian Network learning using Integer Linear Programming (GOBNILP) algorithms [23,24]. The A*, AWA*, and BiHS algorithms regard the structure learning problem as the shortest path search problem and use different strategies to search, and $A^{*}$ is the more stable algorithm among them. CPBayes and GOBNILP use constraint programming and integer programming, respectively, to solve the structure learning problem. Later, CPBayes was enhanced by including linear programming techniques to provide more efficient acyclicity checking [25]. Compared with DP algorithms, these algorithms improve the scalability and efficiency of learning BNs, but their efficiency is still relatively low, and there is still room for improvement. Furthermore, algorithms based on continuous optimization have been developed in recent years. For example, the noncombinatorial optimization via trace exponential and augmented Lagrangian for structure learning (NOTEARS) algorithm [26] used the augmented Lagrangian method to address continuous optimization problems.

Hybrid search approaches try to combine the advantages of score-based and constraintbased algorithms. The most famous hybrid search approach is the max-min hill-climbing (MMHC) algorithm [27]. This algorithm is divided into two stages: in the first stage, the max-min parent and children (MMPC) algorithm [28] is used to learn the parent-child set of each node; in the second stage, the hill-climbing algorithm is conducted within the limited range of the parent-child set. The constrained optimal search (COS) algorithm [29] performs an optimal search through the DP algorithm under superstructure constraints. The edge-constrained optimal search (ECOS) algorithm [30] clusters the superstructure based on the COS algorithm, learns in each cluster, and finally merges to obtain the complete BN structure. The constrained hill-climbing (CHC) algorithm [31] improves algorithm efficiency and accuracy by dynamically limiting the hill-climbing algorithm process. The separation and reunion (SAR) algorithm [32] decomposes a large BN into learning some relatively small BNs through the CI test and builds the actual network structure by remerging these smaller network structures. Kuipers et al. [33] proposed a hybrid algorithm that creates a restricted search space using the PC algorithm followed by Markov Chain Monte Carlo (MCMC) sampling.

In this paper, we continue to study the structural learning problem from the perspective of the shortest path search problem. This paper proposes an improved $\mathrm{A}^{*}$ algorithm based on constraints from potential optimal parent sets (POPS), which is specifically improved in two aspects. On the one hand, the number of POPS is reduced through parent-child sets constraints; on the other hand, obtaining path constraints from POPS constrains the $\mathrm{A}^{*}$ algorithm. The search efficiency of $\mathrm{A}^{*}$ can be improved by the two aspects of constraints about POPS.

The remainder of this paper is organized as follows. In Section 2, the relevant theoretical basis of the problem is introduced and formulated. The details of the proposed algorithms are designed in Section 3. The proposed algorithms are demonstrated with experiments in Section 4, followed by conclusions in Section 5.

# 2. Preliminaries for Bayesian Networks 

This section will introduce BN and the structure learning problem based on the shortest path search perspective, providing the theoretical basis for the new algorithm.

### 2.1. Bayesian Networks

The Bayesian network $B N=(G, P)$ consists of two parts, DAG $G$ and probability distribution $P . G$ is called the structure of a BN, in which each node corresponds to the variables in variable set $\boldsymbol{V}=\left\{X_{1}, \ldots, X_{n}\right\}$ one by one, and the directed edges between nodes reflect the dependencies between nodes. The probability distribution $P$ is called the parameter of BN, specifically $P\left(X_{i} \mid P A_{i}\right)$, where $P A_{i}$ represents the parent set of $X_{i}$. The joint probability of all variables can be decomposed into the product of conditional probability distributions. Figure 1 shows an example of DAG, and $P A_{2}$ is formed by $\left\{X_{1}\right\}$ and $\}$.
![img-0.jpeg](img-0.jpeg)

Figure 1. The order graph of a 4-node BN.
Given the dataset $\boldsymbol{D}=\left\{D_{1}, \ldots, D_{N}\right\}$ ( $N$ is the sample size), the scoring function can give the fitness of network structure $\boldsymbol{G}$ and dataset $\boldsymbol{D}$. The goal of BN structure learning is to find a network structure $G^{*}$ so that the scoring function can obtain the optimal value. Many scoring functions can be used in the BN structure learning problem. Since this paper is based on the perspective of the shortest path search problem, the score of the minimum description length (MDL) [34] is selected. The smaller the MDL score is, the better the corresponding BN structure. Many scoring functions, including the MDL score, are decomposable, namely, the following:

$$
M D L(G)=\sum_{i=1}^{n} M D L\left(X_{i} \mid P A_{i}\right)
$$

where $M D L\left(X_{i} \mid P A_{i}\right)$ is called the local score.
Each local score $M D L\left(X_{i} \mid P A_{i}\right)$ is calculated as follows:

$$
M D L\left(X_{i} \mid P A_{i}\right)=H\left(X_{i} \mid P A_{i}\right)+\frac{\log N}{2} K\left(X_{i} \mid P A_{i}\right)
$$

$$
\begin{gathered}
H\left(X_{i} \mid P A_{i}\right)=-\sum_{x_{i}, p a_{i}} N_{x_{i}, p a_{i}} \log \frac{N_{x_{i}, p a_{i}}}{N_{p a_{i}}} \\
K\left(X_{i} \mid P A_{i}\right)=-\left(r_{i}-1\right) \prod_{X_{i} \in P A_{i}} r_{i}
\end{gathered}
$$

where $N_{x_{i}, p a_{i}}$ is the number of data points that satisfy $X_{i}=x_{i}$ and $P A_{i}=p a_{i}$ in the dataset $D, N_{p a_{i}}$ is the number of data points that satisfy $P A_{i}=p a_{i}$ in the dataset $D$, and $r_{i}$ is the number of states of $X_{i}$.

For any variable $X_{i}$, the other $n-1$ variables can be its parent nodes, and thus, each node can have $2^{n-1}$ parent sets. There are $n 2^{n-1}$ possible parent sets in total, and the corresponding $n 2^{n-1}$ local scores must be calculated theoretically. Obviously, it is impossible to calculate all local scores, and this number can be further reduced by some pruning rules. The following theorems, which have been proven in [19,35], provide a basis for ignoring some parent sets when searching for an optimal parent set for a variable with the MDL function.

Theorem 1 ([19,35]). In an optimal Bayesian network based on the MDL scoring function, each variable has at most $\lfloor\log (2 N / \log N)\rfloor$ parents.

Theorem 2 ([19]). Let $\boldsymbol{U}$ and $\boldsymbol{S}$ be two candidate parent sets for $X_{i}, \boldsymbol{U} \subset \boldsymbol{S}$, and $K\left(X_{i} \mid \boldsymbol{S}\right)-M D L\left(X_{i}, \boldsymbol{U}\right)>0$. Then, $\boldsymbol{S}$ and all supersets of $\boldsymbol{S}$ cannot possibly be optimal parent sets for $X_{i}$.

Theorem 3 ([19]). Let $\boldsymbol{U}$ and $\boldsymbol{S}$ be two candidate parent sets for $X_{i}$ such that $\boldsymbol{U} \subset \boldsymbol{S}$, and $M D L\left(X_{i}, \boldsymbol{U}\right) \leq M D L\left(X_{i}, \boldsymbol{S}\right)$. Then, $\boldsymbol{S}$ is not the optimal parent set of $X_{i}$ for any candidate set.

The pruning rules are lossless and can ensure that the optimal parent set of each node can be obtained in the remaining parent sets. The remaining parent sets are called the potential optimal parent sets, and the potential optimal parent sets of $X_{i}$ are denoted as $\boldsymbol{P O P S}_{i}$.

For exact learning algorithms, the local scores that correspond to the POPS are usually calculated in advance. Then, the local scores are used as the input to obtain the output optimal BN score. Therefore, for the exact learning algorithms, BN structure learning is regarded as a combinatorial optimization problem, as follows:

Input : A set $\boldsymbol{V}=\left\{X_{1}, \ldots, X_{n}\right\}$ and a set of $\boldsymbol{P O P S}_{i}$ for each $X_{i}$
Output : Find $a$ DAG $G^{*}$ such that
$G^{*} \in \underset{G}{\operatorname{argmin}} \sum_{i=1}^{n} M D L\left(X_{i} \mid P A_{i}\right)$
where $P A_{i} \in \boldsymbol{P O P S}_{i}$

# 2.2. Structure Learning in Order Graph 

A series of DP algorithms are proposed to solve the abovementioned combinatorial optimization problem. DP algorithms are mainly based on the following recursive formula:

$$
\begin{gathered}
M D L(\boldsymbol{V})=\min _{X_{i}}\left\{M D L\left(\boldsymbol{V} \backslash X_{i}\right)+\operatorname{BestMDL}\left(X_{i}, \boldsymbol{V} \backslash X_{i}\right)\right\} \\
\operatorname{BestMDL}\left(X_{i}, \boldsymbol{V} \backslash X_{i}\right)=\min _{P A_{i} \subseteq \boldsymbol{V} \backslash\left\{X_{i}\right\}, P A_{i} \in \boldsymbol{P O P S}_{i}} M D L\left(X_{i}, P A_{i}\right)
\end{gathered}
$$

According to the recursive relationship, the basic principle of DP algorithms is as follows. First, the optimal network structure is found for a single variable starting from the empty set. Then, nodes are gradually added to build the optimal subnetwork for an increasingly large set of variables until the optimal network corresponding to

$\boldsymbol{V}=\left\{X_{1}, \ldots, X_{n}\right\}$ is found. DP algorithms can find the optimal BN in the time and space complexity of $O\left(n 2^{n}\right)$, and the whole process can be graphically represented by the order graph. Figure 2 shows the order graph of a four-node BN.
![img-1.jpeg](img-1.jpeg)

Figure 2. The order graph of a four-node BN.
Yuan and Malone [18,19] further transformed the combinatorial optimization problem into the shortest path search problem. They regarded the top empty set $\boldsymbol{O}=\varnothing$ as the start state and the bottom $\boldsymbol{V}$ as the goal state. Therefore, a path from the start state to the goal state corresponds to the ordering of nodes, which is how the order graph obtains its name. In the order graph, state $\boldsymbol{U}$ to the next state $\boldsymbol{S}=\boldsymbol{U} \cup\left\{X_{i}\right\}\left(X_{i} \in \boldsymbol{V} \backslash \boldsymbol{U}\right)$ is equivalent to adding node $X_{i}$ based on subnetwork $\boldsymbol{U}$, and the path cost from state $\boldsymbol{U}$ to the next state $\boldsymbol{S}$ is

$$
\begin{aligned}
& \operatorname{cost}(\boldsymbol{U}, \boldsymbol{S})=\operatorname{BestMDL}\left(X_{i}, \boldsymbol{U}\right) \\
& =\min _{P A_{i} \subseteq \boldsymbol{U}, P A_{i} \in \boldsymbol{P O P S}_{i}} M D L\left(X_{i}, P A_{i}\right)
\end{aligned}
$$

where $\operatorname{BestMDL}\left(X_{i}, \boldsymbol{U}\right)$ is obtained by replacing $\boldsymbol{V} \backslash X_{i}$ in (7) by $\boldsymbol{U}$. The cost of the path is equal to the score of selecting an optimal parent set for $X_{i}$ out of $\boldsymbol{U}$, i.e., $\operatorname{BestMDL}\left(X_{i}, \boldsymbol{U}\right)$. For example, the path $\left\{X_{2}, X_{3}\right\} \rightarrow\left\{X_{1}, X_{2}, X_{3}\right\}$ has a cost equal to $\operatorname{BestMDL}\left(X_{1},\left\{X_{2}, X_{3}\right\}\right)$.

Then, the corresponding optimal ordering can be obtained in the order graph by finding the shortest path from the start state $\boldsymbol{O}$ to the goal state $\boldsymbol{V}$. In the process of finding the shortest path, the optimal parent sets corresponding to the path are recorded. The optimal BN can be built by combining the optimal node ordering with the optimal parent set of each node.

Yuan and Malone searched for the optimal BN structure using the classical A* algorithm based on the shortest path search. In the $\mathrm{A}^{*}$ algorithm, for each current state $\boldsymbol{U}$ in the order graph, the path cost $g(\boldsymbol{U})$ generated from start state $\boldsymbol{O}$ to $\boldsymbol{U}$ is calculated, and the heuristic function $h$ is used to estimate the $\operatorname{cost} h(\boldsymbol{U})$ from the current state $\boldsymbol{U}$ to the goal state $\boldsymbol{V}$. During the search, $f(\boldsymbol{U})=g(\boldsymbol{U})+h(\boldsymbol{U})$ is used to estimate the optimal cost of the path through state $\boldsymbol{U}$, the Open list is used to store the states that will be expanded, and the Closed list is used to store the states that have been expanded. In the Open list, the current state with the lowest $f$ value is expanded each time, and the current state is put into the Closed list, while the state expanded by the current state is put into the Open list. Until the goal state $\boldsymbol{V}$ is expanded, the shortest path from $\boldsymbol{O}$ to $\boldsymbol{V}$ is found, and the optimal node ordering is also found; thus, the corresponding optimal BN can also be built.
$\mathrm{AWA}^{*}$ and BiHS also search for the shortest path in the order graph, only their search strategies are different from $\mathrm{A}^{*}$. Although AWA* and BiHS have the ability to return more upper and lower bounds for the optimal score than $\mathrm{A}^{*}$, in most datasets, $\mathrm{A}^{*}$ expands fewer states and has better stability than AWA* and BiHS in the order graph.

# 3. Two Constraints for Improved A* Algorithm 

According to the introduction of BN structure learning theories and the $\mathrm{A}^{*}$ algorithm based on the order graph in Section 2, we can obtain two key factors that restrict the efficiency of the $\mathrm{A}^{*}$ algorithm:
(1) Potential optimal parent sets. According to the BN structure learning problem description and Formulas (3) and (4), it is necessary to find an optimal parent set from the POPS, of each node $X_{i}$. Obviously, the number of POPS limits the efficiency of the search. If the number of remaining POPS is very small, it is easy to find the parent sets that meet the requirements.
(2) Order graph. The total number of states in the order graph is $2^{n}$, and its scale increases exponentially with the increase in the nodes in BN. The size of the search space also limits the efficiency of the search.

Based on the above two points, this paper will propose solutions to improve the efficiency of the $\mathrm{A}^{*}$ algorithm.

### 3.1. Pruned Potential Optimal Parent Sets with MMPC

Although pruning rules can further reduce the number of POPS, the remaining number is still considerable. In the problem of BN structure learning, we ultimately need optimal parent sets. Therefore, other sets are relatively unnecessary. Given a target variable $T$, the MMPC algorithm can quickly return the parent-child set $C P C(T)$ of the target variable $T$ under the CI test. For the two variables $X, T$ and the set $\boldsymbol{Z}$, the CI $P_{I T}(X, T \mid \boldsymbol{Z})$ can be calculated by $G^{2}$ statistics under the null hypothesis of conditional independence. Let $N^{a b c}$ represent the occurrence times of $X=a, T=b$, and $\boldsymbol{Z}=\boldsymbol{c}$ in the dataset $\boldsymbol{D}$ (respectively, $a$, $b$, and $\boldsymbol{c}$ denote the values specifically taken by $X, T$, and $\boldsymbol{Z} . a$ and $b$ generally are integers, and $\boldsymbol{c}$ is a combination of the integers.); then, the statistical variable $G^{2}$ is defined as

$$
G^{2}=2 \sum_{a, b, c} N^{a b c} \ln \left(\frac{N^{a b c} N^{c}}{N^{a c} N^{b c}}\right)
$$

Under the null hypothesis, the $G^{2}$ statistic asymptotically obeys the distribution of $\chi^{2}$ statistics. Therefore, given the significance level $\alpha$, if the value $p$ calculated by the test, namely, $P_{I T}(X, T \mid \boldsymbol{Z})$, is less than $\alpha$, the hypothesis is rejected, and the variables $X$ and $T$ are considered to be conditionally dependent under a given $\boldsymbol{Z}$. Otherwise, $X$ and $T$ are considered to be conditionally independent under a given $\boldsymbol{Z}$. The pseudocode of the MMPC algorithm is shown in Algorithm 1. In Algorithm 1, $C P C(T)$ is the parent-child set of the target variable $T$.

```
Algorithm 1: MMPC
    Input: Target variable \(T\), variable set \(V\), and significance level \(\alpha\)
    Output: Parent-child set of the target variable \(T: C P C(T)\)
        Let parent-child set of the target variable \(T: C P C(T)=\varnothing, \boldsymbol{R}=\boldsymbol{V} \backslash\{T\} ;\)
        while \(\boldsymbol{R} \neq \varnothing\)
        for \(\forall X \in \boldsymbol{R}\) do
        if \(\max _{\boldsymbol{Z} \subseteq C P C(T)} P_{I T}(X, T \mid \boldsymbol{Z})>\alpha\) then \(\boldsymbol{R}=\boldsymbol{R} \backslash\{T\}\) end if
        end for
        \(Y=\operatorname{argmin}_{X \in R} \max _{\boldsymbol{Z} \subseteq C P C(T)} P_{I T}(X, T \mid \boldsymbol{Z})\) and \(C P C(T)=C P C(T) \cup\{Y\}\)
        for \(\forall X \in C P C(T) \backslash\{Y\}\) do
        if \(\max _{\mathbb{Z} \subseteq C P C(T) \backslash\{X\}} P_{I T}(X, T \mid \boldsymbol{Z})>\alpha\) then \(C P C(T)=C P C(T) \backslash\{X\}\) end if
        end for
    end while
```

Given a condition set $\boldsymbol{Z}$, the MMPC algorithm not only considers $P_{I T}(X, T \mid \boldsymbol{Z})$ to determine whether $X$ and $T$ are independent but also considers $\max _{\boldsymbol{Z}^{\prime} \subset \boldsymbol{Z}} P_{I T}\left(X, T \mid \boldsymbol{Z}^{\prime}\right)$, which has stronger robustness, to determine whether $X$ and $T$ are independent. Certainly, this approach requires more $\chi^{2}$ test calculations. Finally, we can use the MMPC algorithm to compute the parent-child set $C P C(T)$ for each variable $X_{i}$.

Through the constraint of the parent-child set $C P C(T)$, we can further prune the unnecessary sets and their corresponding MDL score calculations for the $\boldsymbol{P O P S}_{i}$. Taking a four-node BN as an example, for node $X_{4},\left\{X_{1}, X_{2}, X_{3}\right\}$ and all of its subsets could be the parent set of $X_{4}$. If the traditional pruning rules (Theorems 1-3) are not considered to be in effect, its POPS are still $\left\{X_{1}, X_{2}, X_{3}\right\}$ and all its subsets, which are represented as the parent graph of $X_{4}$, as shown in Figure 3. If the parent-child set of $X_{4}$ obtained by the MMPC algorithm is $C P C\left(X_{4}\right)=\left\{X_{2}, X_{3}\right\}$, then the parent graph of $X_{4}$ shown in Figure 3 can be pruned to the parent graph shown in Figure 4. For larger BNs, this pruning will be more significant in its score calculations. The constraints of the parent-child set calculated by the MMPC algorithm can greatly reduce unnecessary score calculations and storage. Limiting the number of corresponding POPS improves the search efficiency of the A* algorithm.
![img-2.jpeg](img-2.jpeg)

Figure 3. Parent graph of $X_{4}$ in a 4-node BN.
![img-3.jpeg](img-3.jpeg)

Figure 4. Parent graph of $X_{4}$ after pruning in a 4-node BN.

# 3.2. Pruned Order Graph with Path Constraints 

According to Section 2.2, the optimal BN structure learning actually searches for the shortest path from the order graph. Therefore, if the path constraints can be found in the order graph, it will greatly improve the efficiency of the $\mathrm{A}^{*}$ algorithm in searching for the shortest path in the order graph.

Before illustrating such path constraints, a simple example can be taken. Table 1 shows the POPS of each variable in a six-node BN. We assume that we have obtained the POPS of each variable by the score pruning rules or MMPC algorithm in Section 3.1. It can be seen from Table 1 that not all nodes can choose all other nodes as their parent nodes due to the

parent-child set constraints obtained from Section 3.1. For example, $X_{1}$ can only choose $X_{2}$ as its parent node or an empty set with no parent.

Table 1. The POPS of each variable in a 6-node BN.


A directed graph can be obtained by connecting each node $X_{i}$ and its potential optimal parent sets $\boldsymbol{P O P S}_{i}$. We connect from each node $X_{i}$ and its potential optimal parent sets $\boldsymbol{P O P S}_{i}$ from Table 1 to obtain the directed graph, as shown in Figure 5. In such a directed graph, if $X_{j}$ is a potential parent node of $X_{i}$, then the graph contains directed edges from $X_{j}$ to $X_{i}$.
![img-4.jpeg](img-4.jpeg)

Figure 5. A directed graph based on each variable in Table 1 and its POPS.
An interesting phenomenon can be observed in Figure 5: there are only directed edges from the node in $\left\{X_{1}, X_{2}\right\}$ to the node in $\left\{X_{3}, X_{4}, X_{5}, X_{6}\right\}$ but no directed edges from the node in $\left\{X_{3}, X_{4}, X_{5}, X_{6}\right\}$ to the node in $\left\{X_{1}, X_{2}\right\}$; in other words, the node in $\left\{X_{3}, X_{4}, X_{5}, X_{6}\right\}$ cannot be the parent node of the node in $\left\{X_{1}, X_{2}\right\}$, and thus, it can be split into two parts: $\left\{X_{1}, X_{2}\right\}$ and $\left\{X_{3}, X_{4}, X_{5}, X_{6}\right\}$. Thus, based on Figure 5, by contracting $\left\{X_{1}, X_{2}\right\}$ to one node and $\left\{X_{3}, X_{4}, X_{5}, X_{6}\right\}$ to another node, we can finally obtain the acyclic component graph, as shown in Figure 6. Based on the above splitting method, we can split the order graph of learning the six-node BN into two subgraphs, as shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. Acyclic component graph based on Figure 5.
Obviously, it can be seen from the above that the complete order graph of the six-variable BN should contain $2^{6}$ states. However, the order graph can be split into two subgraphs based on the constraints from Figure 5, in other words, $\left\{X_{1}, X_{2}\right\}$ and $\left\{X_{3}, X_{4}, X_{5}, X_{6}\right\}$. We refer to this splitting method as path constraints.

As the structure of the order graph changed, the entire process of searching the order graph also changed. First, we find the shortest path from $\boldsymbol{O}$ to $\left\{X_{1}, X_{2}\right\}$ in the first subgraph of Figure 7, and then find the shortest path from $\left\{X_{1}, X_{2}\right\}$ to $\boldsymbol{V}=\left\{X_{1}, X_{2}, X_{3}, X_{4}, X_{5}, X_{6}\right\}$ in

the second subgraph of Figure 7. The shortest path from $\boldsymbol{O}$ to $\boldsymbol{V}$ is obtained by concatenating the shortest paths in the two subgraphs. $\left\{X_{1}, X_{2}\right\}$ becomes the necessary state in the shortest searching process of the order graph. Therefore, the number of the states in the order graph search space of Figure 7 can be reduced to $2^{2}+2^{4}-1$.
![img-6.jpeg](img-6.jpeg)

Figure 7. Pruned order graph based on the constraints from Figure 5.
Compared with $2^{6}$ states in the complete order graph of the six-variable BN, path constraints can reduce the number of states in the order graph. As the number of nodes $n$ increases, the path constraint reduces the number of states in the order graph more significantly. We give Theorem 4 to generalize and quantify this reduction.

Theorem 4. In a Bayesian network with node set $\boldsymbol{V}=\left\{X_{1}, \ldots, X_{n}\right\}$, given path constraints, $\boldsymbol{V}$ can be split into subsets $\boldsymbol{P}_{1}, \boldsymbol{P}_{2}, \ldots, \boldsymbol{P}_{m}\left(\sum_{i=1}^{m} \boldsymbol{P}_{i}=\boldsymbol{V}\right)$. Then, the number of states in the order graph is reduced from $2^{n}$ to $\sum_{i=1}^{m} 2^{\left|P_{i}\right|}-m+1$.

Proof of Theorem 4. Obviously, the total $2^{n}$ states of the complete order graph correspond to the Bayesian network of $n$ nodes. For the ordered graph under path constraints, where the number of states of any subgraph split by $\boldsymbol{P}_{i}$ is $2^{\left|\boldsymbol{P}_{i}\right|}$, there are $m$ such subgraphs, and the total number of states is $\sum_{i=1}^{m} 2^{\left|\boldsymbol{P}_{i}\right|}$. However, this will double count $m-1$ states. Therefore, $m-1$ states are removed from the total number of computations. Finally, the total number of states is $\sum_{i=1}^{m} 2^{\left|P_{i}\right|}-m+1$.

This simple example shows that the directed graph built from each node $X_{i}$ and its potential optimal parent sets $\boldsymbol{P O P S}_{i}$ implies path constraints, which can be used to prune the order graph.

The internal principle is briefly described as follows, requiring the help of Theorem 5 (it is proved in the literature [19]).

Theorem 5. Let $\boldsymbol{U}$ and $\boldsymbol{S}$ be two candidate parent sets for $X_{i}$ such that $\boldsymbol{U} \subset \boldsymbol{S}$. We must have $\operatorname{BestMDL}\left(X_{i}, \boldsymbol{S}\right) \leq \operatorname{BestMDL}\left(X_{i}, \boldsymbol{U}\right)$.

In general, if there is only a directed path from $X_{j}$ to $X_{i}$ in the directed graph but no directed path from $X_{i}$ to $X_{j}$, then the order graph does not need to generate states containing $X_{i}$ but excluding $X_{j}$. One way to think about this phenomenon is the following. For a current state $\boldsymbol{U}$ in the order graph that does not include $X_{i}$ and $X_{j}$, if we expand $X_{j}$ first and then $X_{i}$, then the path cost from state $\boldsymbol{U}$ to state $\boldsymbol{U} \cup\left\{X_{i}, X_{j}\right\}$ is $\operatorname{BestMDL}\left(X_{j}, \boldsymbol{U}\right)+$ $\operatorname{BestMDL}\left(X_{i}, \boldsymbol{U} \cup\left\{X_{j}\right\}\right)$. On the other hand, if we expand $X_{i}$ first and then $X_{j}$, the path cost from state $\boldsymbol{U}$ to state $\boldsymbol{U} \cup\left\{X_{i}, X_{j}\right\}$ is $\operatorname{BestMDL}\left(X_{i}, \boldsymbol{U}\right)+\operatorname{BestMDL}\left(X_{j}, \boldsymbol{U} \cup\left\{X_{i}\right\}\right)$. However, since only a directed path from $X_{j}$ to $X_{i}$ can exist, $\operatorname{BestMDL}\left(X_{j}, \boldsymbol{U} \cup\left\{X_{i}\right\}\right)=$ $\operatorname{BestMDL}\left(X_{j}, \boldsymbol{U}\right)$. For these two path expansion plans, we should continue to compare the values of $\operatorname{BestMDL}\left(X_{i}, \boldsymbol{U} \cup\left\{X_{j}\right\}\right)$ and $\operatorname{BestMDL}\left(X_{i}, \boldsymbol{U}\right)$. According to Theorem 5 and $\boldsymbol{U} \subseteq \boldsymbol{U} \cup\left\{X_{j}\right\}$, it is more likely to obtain a better value that makes this path smaller in a larger set, and thus, $\operatorname{BestMDL}\left(X_{i}, \boldsymbol{U} \cup\left\{X_{j}\right\}\right) \leq \operatorname{BestMDL}\left(X_{i}, \boldsymbol{U}\right)$. Therefore, the plan that expands $X_{j}$ first and then $X_{i}$ is more likely to achieve the shortest path from $\boldsymbol{U}$ to $\boldsymbol{U} \cup\left\{X_{i}, X_{j}\right\}$. Thus, there is no need to generate states that contain $X_{i}$ but exclude $X_{j}$.

Based on the previous simple example, we discuss the general method of obtaining path constraints in order to prune the order graph.

A new concept, the strongly connected component (SCC), is actually involved in the process of splitting the directed graph built from each node $X_{i}$ and its potential optimal parent sets $\boldsymbol{P O P S}_{i}$. In a directed graph, if there is a directed path from $V_{i}$ to $V_{j}$ between two nodes and a directed path from $V_{j}$ to $V_{i}$, the two nodes are said to be strongly connected. A directed graph is a strongly connected graph if any two nodes are strongly connected. The extremely strongly connected subgraph of a directed graph is called a strongly connected component. The strongly connected components of a directed graph form an acyclic component graph, which is also a DAG. Each node $C_{i}$ in the acyclic component graph corresponds to a strongly connected component $\boldsymbol{S C C}_{i}$ and to a subset of the node set $\boldsymbol{V}=\left\{X_{1}, \ldots, X_{n}\right\}$ in a BN. The acyclic component graph gives more intuitive path constraints. In the acyclic component graph, if there are directed paths from $C_{i}$ to $C_{j}$, the variable in $\boldsymbol{S C C}_{j}$ cannot be the parent node of the variable in $\boldsymbol{S C C}_{i}$.

Based on the above concept, we try to obtain path constraints by extracting SCCs to prune the order graph. At present, there are mature algorithms for SCC extraction, among which the Kosaraju algorithm is the most commonly used. The pseudocode of the algorithm that obtains path constraints by extracting SCCs is shown in Algorithm 2.

In this algorithm, the potential optimal parent sets $\boldsymbol{P O P S}_{i}$ of each node $X_{i}$ are used to build the directed graph $G^{0}$, and the SCC $\left\{\boldsymbol{S C C}_{1}, \ldots \boldsymbol{S C C}_{i}, \ldots \boldsymbol{S C C}_{m}\right\}$ of the directed graph $G^{0}$ is extracted by the Kosaraju algorithm. It is worth noting that if the size of the SCC is too large, it is still not conducive to improving the efficiency of the algorithm and to searching for a larger network. For example, the original $\mathrm{A}^{*}$ algorithm itself cannot search the network of over 50 nodes. If, in the operation of building a directed graph $G^{0}$ and extracting SCCs through the POPS, two SCCs with $\left|\boldsymbol{S C C}_{1}\right|=1$ and $\left|\boldsymbol{S C C}_{2}\right|=49$ are obtained, and the path constraints are determined, such a method is still meaningless. Because the $\mathrm{A}^{*}$ algorithm still cannot search a network of 49 nodes. Thus, we limit the size of the SCC with the parameter $t$. If the size of the maximum SCC exceeds the parameter $t$, a part of the set of potential optimal parent sets $\boldsymbol{P O P S}_{i}$ is selected to rebuild the directed graph $G^{0}$. We prefer to select the sets that correspond to the local scores of the top $k$ in $P O P S_{i}$. The parameter $t$ will gradually decrease from the maximum number of POPS until the SCC that meets the conditions can be extracted from the built directed graph. Then, Algorithm 2 breaks out of the loop and returns the extracted SCCs under the constraints of the parameter $t$. However, this method is greedy because only part of POPS is used to build the directed graph, and the extracted SCCs lose some information. The pruned order graph formed according to the path constraints of SCCs has certain problems, which will affect the shortest path search and affect the accuracy of the final BN. This effect will be analyzed in detail in the experimental section.

```
Algorithm 2: Obtain path constraints algorithm
Input: Potential optimal parent sets of each node \(X_{i}\) POPS \(_{i}\), maximum size \(t\)
Output: Path constraints \(\boldsymbol{P}_{1}, \ldots, \boldsymbol{P}_{i}, \ldots, \boldsymbol{P}_{m}\)
    \(p \leftarrow \max \left\{\left|\boldsymbol{P O P S _ { 1 } \| , \ldots \| P O P S _ { i } \|, \ldots \| P O P S _ { m } \|}\right.\right.\)
    build graph \(G^{0}\) according to all \(P O P S_{j}\) of \(X_{i}\)
    \(\left\{\boldsymbol{S C C _ { 1 } , \ldots, S C C _ { i } , \ldots, S C C _ { m }}\right\} \leftarrow\) Kosaraju \(\left\{G^{0}\right\} ;\)
    \(q \leftarrow \max \left\{\left|\boldsymbol{S C C _ { 1 } \| , \ldots \| S C C _ { i } \|, \ldots \| S C C _ { m } \|}\right.\right.\);
    if \(q>t\) then
    for \(k=p \rightarrow 1\) do
    build graph \(G^{0}\) according to the best \(k\) POPS \(_{i}\) of \(X_{i}\)
    \(\left\{\boldsymbol{S C C _ { 1 } , \ldots, S C C _ { i } , \ldots, S C C _ { m }}\right\} \leftarrow\) Kosaraju \(\left\{G^{0}\right\} ;\)
    \(q \leftarrow \max \left\{\left|\boldsymbol{S C C _ { 1 } \| , \ldots \| S C C _ { i } \|, \ldots \| S C C _ { m } \|}\right.\right.\);
    if \(q \leq t\) then break; endif
    end for
    end if
    \(\boldsymbol{P}_{1}, \ldots, \boldsymbol{P}_{i}, \ldots, \boldsymbol{P}_{m} \leftarrow \boldsymbol{S C C _ { 1 } , \ldots, S C C _ { i } , \ldots, S C C _ { m }}\)
```

Finally, we discuss the search complexity in the pruned order graph. $\left\{\boldsymbol{S C C _ { 1 } , \ldots, S C C _ { i } , \ldots, S C C _ { m }}\right\}$ obtained by Algorithm 2 can split the original order graph into $m$ subgraphs, where the connection state between each subgraph is $\boldsymbol{F}_{i}=\cup_{k=1}^{i} \boldsymbol{S C C _ { k }}$, and $\boldsymbol{F}_{m}=\cup_{k=1}^{m} \boldsymbol{S C C _ { k }}=\boldsymbol{V}, \boldsymbol{F}_{0}=\{ \}=\boldsymbol{O}$. Thus, for each subgraph, the start state is $\boldsymbol{F}_{i-1}$ and the goal state is $\boldsymbol{F}_{i}$. For the entire order graph, it is equivalent to searching the shortest paths from $\boldsymbol{F}_{0}$ to $\boldsymbol{F}_{1}$, then from $\boldsymbol{F}_{1}$ to $\boldsymbol{F}_{2}$, all the way to $\boldsymbol{F}_{m-1}$ to $\boldsymbol{F}_{m}$. Still taking Figure 7 as an example, because there are $\boldsymbol{S C C _ { 1 }}=\left\{X_{1}, X_{2}\right\}$ and $\boldsymbol{S C C _ { 2 }}=\left\{X_{3}, X_{4}, X_{5}, X_{6}\right\}$, there are $\boldsymbol{F}_{1}=\left\{X_{1}, X_{2}\right\}$ and $\boldsymbol{F}_{2}=\left\{X_{1}, X_{2}, X_{3}, X_{4}, X_{5}, X_{6}\right\}$. Therefore, we search the shortest path from $\boldsymbol{F}_{0}=\varnothing$ to $\boldsymbol{F}_{1}=\left\{X_{1}, X_{2}\right\}$ and then search the shortest path from $\boldsymbol{F}_{1}=\left\{X_{1}, X_{2}\right\}$ to $\boldsymbol{F}_{2}=\left\{X_{1}, X_{2}, X_{3}, X_{4}, X_{5}, X_{6}\right\}$. Finally, it only remains to connect each shortest path to obtain the entire shortest path on the order graph. For each subgraph, the maximum complexity of the $\mathrm{A}^{*}$ search is $O\left(2^{\left|\mathrm{SCC}_{i}\right|}\right)$. This case is the worst case, which is almost impossible because $\mathrm{A}^{*}$ uses heuristic functions. Therefore, in the pruned order graph, which is split into $m$ subgraphs using $\left\{\boldsymbol{S C C _ { 1 } , \ldots, S C C _ { i } , \ldots, S C C _ { m }}\right\}$, the maximum complexity of the $\mathrm{A}^{*}$ search is

$$
O\left(2^{\left|\boldsymbol{S C C _ { 1 } \|}+\ldots+2^{\left|\boldsymbol{S C C _ { i } \|} \ldots+2^{\left|\boldsymbol{S C C _ { m } \|}\right.}\right.}\right)=O\left(m \max _{i} 2^{\left|\boldsymbol{S C C _ { i } \|}\right.}\right)\right.
$$

This conclusion also corroborates Theorem 4. This finding shows that the maximum complexity depends on the size of the maximum SCC. Therefore, it is necessary for Algorithm 2 to use the parameter $t$ to limit the size of the maximum SCC, which effectively limits the maximum complexity of the $\mathrm{A}^{*}$ search of the pruned order graph.

# 4. Experiments 

To evaluate the effect of $\mathrm{A}^{*}$ under MMPC constraints (Section 3.1) and path constraints (Section 3.2), experiments will be performed on some common benchmark BNs and UCI datasets. The $\mathrm{A}^{*}$ algorithm using only MMPC constraints is named $\mathrm{A}^{*}$-MMPC, the $\mathrm{A}^{*}$ algorithm using only path constraints is named $\mathrm{A}^{*}-\mathrm{PC}$, and the algorithm using both constraints is named $\mathrm{A}^{*}$-MM2PC. Experiments are mainly divided into two parts. First, the improvement effect of the two constraints on $\mathrm{A}^{*}$ is tested; in other words, the various indices between the $\mathrm{A}^{*}, \mathrm{~A}^{*}-\mathrm{MMPC}, \mathrm{A}^{*}-\mathrm{PC}$, and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ algorithms are tested. Then, the $\mathrm{A}^{*}$-MM2PC with two constraints is compared with the typical GOBNILP and MMHC algorithms.

First, the comparison experiment will compare $\mathrm{A}^{*}, \mathrm{~A}^{*}-\mathrm{MMPC}, \mathrm{A}^{*}-\mathrm{PC}$, and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ from the following three aspects:

1. Time: Time recorded the running time of the algorithm (OT means out of time);

2. States: The number of expanded states in the order graph;
3. Error: The percentage error $\left(M D L\left(G_{\text {obtained }}\right) / M D L\left(G_{\text {exact }}\right)-1\right) \times 100 \%$ where $M D L\left(G_{\text {obtained }}\right)$ is the MDL score of the BN obtained by the performing algorithm after learning the data, and $M D L\left(G_{\text {exact }}\right)$ is the exact MDL score of the BN obtained by the original $\mathrm{A}^{*}$ or GOBNILP algorithms.
4. Both the original $\mathrm{A}^{*}$ and GOBNILP algorithms are exact learning algorithms. If scoring values can be obtained, they are both optimal and equal. Therefore, these two algorithms do not need to calculate the percentage error, and they are both $0 \%$. On the one hand, the MMPC algorithm uses a CI test, and there will be a certain probability of error in the case of insufficient or noisy samples. On the other hand, path constraints adopt a greedy strategy when extracted SCCs do not meet parameter $t$. Therefore, $\mathrm{A}^{*}-\mathrm{MMPC}, \mathrm{A}^{*}-\mathrm{PC}$, and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ should all consider the influence of the accuracy, namely, the percentage error. The smaller the percentage error is, the higher the accuracy of the corresponding algorithm. Two decimal places are retained for each index, and scientific notation is used for numbers that are too large or too small.
The benchmark BNs are selected for the comparison experiment, and the sampled data are obtained from the sample sizes of $1000,3000,5000,7000$, and 10,000 . Then, BN is learned from the sampled data. Table 2 records the performances of the $\mathrm{A}^{*}, \mathrm{~A}^{*}-\mathrm{MMPC}$, $\mathrm{A}^{*}-\mathrm{PC}$, and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ algorithms on benchmark BNs. By adding path constraints, the scale of BNs that the $\mathrm{A}^{*}$ algorithm can search is expanded, and Water and Alarm networks that cannot be searched before can be searched.

Table 2. Performances of the $\mathrm{A}^{*}, \mathrm{~A}^{*}-\mathrm{MMPC}, \mathrm{A}^{*}-\mathrm{PC}$, and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ algorithms on benchmark BNs. The best-performing results (including minimum time, minimum number of expanded states and minimum percentage error) are highlighted in bold in the Table 2 and the following tables.


In terms of the number of expanded states in the order graph, using either MMPC or path constraints can significantly reduce the number of states, and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ using both

constraints has the lowest number of expanded states. Similarly, in general, the trend of the corresponding time consumption follows the trend of the number of expanded nodes, except for the Sachs network. In the Sachs network, although $\mathrm{A}^{*}-\mathrm{PC}$ and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ have fewer expanded states than $\mathrm{A}^{*}$ and $\mathrm{A}^{*}$-MMPC, their corresponding time consumption is higher. The time consumption for structure learning in the Sachs network is already low; however, it takes a certain amount of time to generate heuristic functions every time the $\mathrm{A}^{*}$ program is executed. Therefore, in the Sachs network, $\mathrm{A}^{*}-\mathrm{PC}$ and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ divide the complete order graph into several subgraphs using path constraints, and each subgraph increases the generation time of the heuristic function accordingly. In conclusion, $\mathrm{A}^{*}-\mathrm{PC}$ and $\mathrm{A}^{*}$-MM2PC use path constraints to reduce the number of expanded states in the order graph, and thus reduce the search time, which is far less than the generation time of the increased heuristic function, resulting in higher time consumption in a smaller network. However, in larger networks, the reduction in more states is the more dominant factor, and thus, their time consumption is significantly reduced. In the Alarm network, the size of the maximum SCC obtained by Algorithm 2 is 18, while the sizes of other SCCs are mostly 2 and 3. Therefore, the experimental results regarding the time consumption and the number of expanded states are similar to the Child network with 20 nodes. In Hailfinder and Win95pts, the size of the maximum SCC obtained by Algorithm 2 is relatively small, so their total time consumption and the number of expanded states are both even smaller than the corresponding results for smaller networks. This phenomenon shows that the maximum complexity of the algorithm depends on the size of the maximum SCC, which is consistent with the conclusion in Section 3.2.

In terms of the accuracy of these algorithms, it is easier to lose accuracy using MMPC constraints. The accuracy loss is more significant in the case of a small sample size, and the accuracy is higher in the case of a large sample size. Since MMPC uses the CI test, it is sensitive to the sample size and can only obtain good results under the condition of sufficient samples; as a result, this drawback is also inherited into the new algorithm. In addition, path constraints lead to accuracy loss in the Alarm network. For calculating path constraints in a large-scale network, Algorithm 2 will attempt to generate a directed graph using the sets that corresponds to the local scores of the top $k$ in $P O P S_{i}$. However, this approach is greedy, which reduces the accuracy of the final BN. Fortunately, path constraints using the greedy approach lead to a lower accuracy loss than MMPC constraints. Furthermore, it can be concluded from the experimental results that the accuracy loss of the $\mathrm{A}^{*}$-MM2PC algorithm using MMPC constraints and path constraints comes more from the accuracy loss caused by MMPC constraints.

Table 3 records the performances of the $\mathrm{A}^{*}, \mathrm{~A}^{*}-\mathrm{MMPC}, \mathrm{A}^{*}-\mathrm{PC}$, and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ algorithms on 13 common UCI datasets. By adding MMPC constraints and path constraints, the size of BNs that can be searched by the $\mathrm{A}^{*}$ algorithm is expanded, and the performance of adding path constraints is more significant than that of adding MMPC constraints. In terms of the number of expanded states in the order graph, MMPC or path constraints can significantly reduce the number of expanded states, and adding both can reduce the number of expanded states even further. The variation trend of time consumption is similar to that of the number of expanded states. In terms of the accuracy of these algorithms, since most UCI datasets have small sample sizes, and the CI test used in MMPC constraints requires a sufficient sample size, it is easier to lose accuracy by using MMPC constraints. Comparatively, the accuracy loss of path constraints appears only in Flag, Soybean, Bands, and Spectf. The accuracy loss of the A*-MM2PC algorithm using both MMPC constraints and path constraints mainly comes from MMPC constraints.

Table 3. Performances of the $\mathrm{A}^{*}, \mathrm{~A}^{*}-\mathrm{MMPC}, \mathrm{A}^{*}-\mathrm{PC}$, and $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ algorithms on UCI datasets.


On the whole, MMPC and path constraints can effectively and significantly improve the overall efficiency of the $\mathrm{A}^{*}$ algorithm and reduce time consumption and the number of expanded states in the order graph, at the cost of only a slight loss in accuracy. $\mathrm{A}^{*}$-MM2PC with MMPC constraints and path constraints is compared with other classical algorithms. The GOBNILP algorithm is considered to be the state-of-the-art algorithm among the exact learning algorithms, while the MMHC algorithm is the most well-known algorithm among the hybrid algorithms, which also uses MMPC constraints. In addition, the Insert Neighborhood Ordering-Based Search (INOBS) [36] algorithm is a state-of-the-art improved variant of OBS. The comparison experiment will compare GOBNILP, MMHC, INOBS, and A*-MM2PC from the following two aspects:

1. Time: time recorded the running time of the algorithm (OT means out of time);
2. Error: the percentage error $\left(M D L\left(G_{\text {obtained }}\right) / M D L\left(G_{\text {exact }}\right)-1\right) \times 100 \%$.

The percentage error is calculated in the same way as before, and since the GOBNILP algorithm is an exact learning algorithm, it is always $0 \%$ and is not recorded. In addition, since GOBNILP, MMHC, and INOBS have different search spaces and do not use the order graph as the search space, the number of expanded states in the order graph is also not recorded.

Table 4 records the performances of the GOBNILP, MMHC, INOBS, and A*-MM2PC algorithms on benchmark BNs. Compared with the GOBNILP algorithm, A*-MM2PC consumes less time in the Sachs, Child, Alarm, Hailfinder, and Win95pts networks. Although the accuracy of $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ is not as good as GOBNILP, the overall accuracy loss of $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ is less than $3 \%$, mainly concentrated within $0.5 \%$. Compared with the MMHC algorithm, A*-MM2PC has less time consumption on the Sachs, Child, Alarm, Hailfinder, and Win95pts networks and always has less accuracy loss than the MMHC algorithm. Although both the MMHC and A*-MM2PC algorithms adopt MMPC constraints, MMHC uses greedy search to further search in the second stage, while $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ is based on the $\mathrm{A}^{*}$ algorithm, an exact learning algorithm, to further search; thus, $\mathrm{A}^{*}-\mathrm{MM} 2 \mathrm{PC}$ will achieve higher accuracy than MMHC. The accuracy of the MMHC algorithm also roughly conforms to the trend of low accuracy when the sample size is small and high accuracy when the sample size is large. The reason is the fact that CI tests rely on sufficient samples. Compared with the INOBS algorithm, A*-MM2PC mostly has less time consumption on the Sachs, Child, Alarm, Hailfinder, and Win95pts networks than the INOBS algorithm, and has less accuracy loss than the INOBS algorithm, in most cases.

Table 4. Performances of GOBNILP, MMHC, and A*-MM2PC algorithms on benchmark BNs.


Table 5 records the performances of the GOBNILP, MMHC, and A*-MM2PC algorithms on UCI datasets. Compared with the GOBNILP algorithm, the A*-MM2PC algorithm has less time consumption on most datasets. Compared with the MMHC algorithm, it has less time consumption on most datasets and has less accuracy loss. Compared with the INOBS algorithm, A*-MM2PC has less time consumption and has less accuracy loss than the INOBS algorithm on more datasets. Due to the small sample size in the UCI dataset, the accuracy of the A*-MM2PC algorithm and the MMHC algorithm in the UCI dataset is lower than that of benchmark BNs, and the overall accuracy of the A*-MM2PC algorithm is higher than that of the MMHC algorithm. The A*-MM2PC algorithm has more advantages in time and accuracy than the MMHC algorithm. For the Mushroom dataset, due to having a large number of states of each variable and a large number of POPS, the time consumption of GOBNILP and MMHC increases significantly when learning its structure, and the accuracy of the MMHC algorithm decreases significantly. However, the search space of A*-MM2PC is an order graph, which does not increase as the number of variable states and POPS

increases. In contrast, it decreases with appropriate path constraints. Therefore, $\mathrm{A}^{*}$-MM2PC has higher time efficiency than GOBNILP and MMHC on Mushroom.

Table 5. Performances of GOBNILP, MMHC, and A*-MM2PC algorithms on UCI datasets.


# 5. Conclusions

Based on the $\mathrm{A}^{*}$ algorithm and POPS, this paper proposes an improved $\mathrm{A}^{*}$ algorithm, which is specifically divided into two aspects. On the one hand, it is called MMPC constraints, and POPS can be reduced through parent-child set constraints calculated by the MMPC algorithm. On the other hand, it is called path constraints and uses a directed graph built from POPS, and SCCs are extracted to obtain the path constraints in the order graph. The two constraints based on POPS can improve the search efficiency of $\mathrm{A}^{*}$. A large number of experiments were conducted to test the performance of the constraints. The A*-MMPC algorithm with MMPC constraints and the A*-PC algorithm with path constraints have less time consumption and fewer expanded states in the order graph and search larger networks than the original A* algorithm. Meanwhile, the A*-MM2PC algorithm with two constraints has better performance. The only drawback of both constraints is a slight loss of accuracy, most of which is no more than $0.5 \%$. Compared with the MMPC constraints, the path constraints bring a lower loss of accuracy, and the scale of the Bayesian network that can be searched is larger. Compared with the state-of-the-art GOBNILP algorithm, A*MM2PC has higher time efficiency in some experiments. Compared with the well-known MMHC algorithm of the hybrid algorithms, A*-MM2PC has more time efficiency and accuracy advantages in most cases. Compared with the state-of-the-art improved variant of OBS, namely, INOBS, A*-MM2PC has less time consumption and has less accuracy loss on more datasets.

Of course, the constraints we propose can not only be applied to the $\mathrm{A}^{*}$ algorithm. DP, AWA*, and BiHS have the same search space as $\mathrm{A}^{*}$, only the specific search method is different. Thus, our proposed constraints can also be applied to these algorithms. The method of application is similar to adding the constraints proposed in this paper into $\mathrm{A}^{*}$. First, the number of potential optimal parent sets for DP, AWA*, and BiHS is reduced by parent-child set constraints from the MMPC algorithm. After that, path constraints are obtained from their pruned potential optimal parent sets to limit the search process of these algorithms.

However, further research questions remain. In Algorithm 2, if the size of the maximum SCC exceeds the parameter $t$, we prefer to select the sets that correspond to the local scores of the top $k$ in $P O P S_{i}$, which is a greedy strategy, leading to a slight loss in accuracy. Perhaps this can be mitigated by more reasonable rules that filter out better POPS.

In practice, we try to obtain complete and sufficient data. On this basis, local scores and POPS are calculated, POPS are pruned by the MMPC algorithm, and then path constraints files are obtained from Algorithm 2 by the POPS. The $\mathrm{A}^{*}$ algorithm is modified to provide the ability to search after reading the path constraints files. Finally, the $\mathrm{A}^{*}$ algorithm is invoked through a script to enable it to search for sub-networks under different path constraint files and merge the sub-networks.

In future work, we seek to obtain more useful constraints from POPS to further restrict the learning process of the BN structure to improve the performance of the BN exact structure learning algorithm on larger networks. In addition, determining whether further constraints can be obtained directly from the data is also a direction for new thinking in producing new research.

Author Contributions: Conceptualization, Methodology, C.H.; Software, R.D.; Writing—original draft, X.T. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported by the National Natural Science Foundation of China (61573285, 62171360), and the Natural Science Foundation of Shaanxi Province of China (2022JQ-590).

Data Availability Statement: The benchmark Bayesian networks are known, and they are publicly available (http://www.bnlearn.com/bnrepository (accessed on 20 November 2022)). The UCI datasets are publicly available (https://archive.ics.uci.edu/ml/index.php (accessed on 20 November 2022)).

Conflicts of Interest: The authors declare no conflict of interest.
