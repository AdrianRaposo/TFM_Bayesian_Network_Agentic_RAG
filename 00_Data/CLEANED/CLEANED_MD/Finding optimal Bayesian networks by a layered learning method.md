# Finding optimal Bayesian networks by a layered learning method 

YANG Yu, GAO Xiaoguang*, and GUO Zhigao<br>School of Electronics and Information, Northwestern Polytechnical University, Xi'an 710129, China


#### Abstract

It is unpractical to learn the optimal structure of a big Bayesian network (BN) by exhausting the feasible structures, since the number of feasible structures is super exponential on the number of nodes. This paper proposes an approach to layer nodes of a BN by using the conditional independence testing. The parents of a node layer only belong to the layer, or layers who have priority over the layer. When a set of nodes has been layered, the number of feasible structures over the nodes can be remarkably reduced, which makes it possible to learn optimal BN structures for bigger sizes of nodes by accurate algorithms. Integrating the dynamic programming (DP) algorithm with the layering approach, we propose a hybrid algorithm - layered optimal learning (LOL) to learn BN structures. Benefitted by the layering approach, the complexity of the DP algorithm reduces to $O\left(\rho 2^{n-1}\right)$ from $O\left(n 2^{n-1}\right)$, where $\rho<n$. Meanwhile, the memory requirements for storing intermediate results are limited to $O\left(C_{k^{\frac{1}{n}}}^{\frac{k^{2}}{k}}\right)$ from $O\left(C_{k}^{\frac{n}{k}}\right)$, where $k^{\#}<n$. A case study on learning a standard BN with 50 nodes is conducted. The results demonstrate the superiority of the LOL algorithm, with respect to the Bayesian information criterion (BIC) score criterion, over the hill-climbing, max-min hill-climbing, PC, and three-phrase dependency analysis algorithms.


Keywords: Bayesian network (BN), structure learning, layered optimal learning (LOL).

DOI: 10.21629/JSEE.2019.05.12

## 1. Introduction

The Bayesian network (BN) [1] is a graphical tool [2,3] that can efficiently encode and infer uncertain knowledge [4]. A discrete BN consists of a structure and related conditional probability table (CPT) parameters. The structure is a directed acyclic graph (DAG) that represents independence relationships among nodes by directed connections; however, the CPTs are conditional probability distributions that qualify parents-child relationships in the DAG. The number of feasible BN structures for a set of nodes is

[^0]known to be super exponential on the number $n$ of the nodes [5]; that is, $O\left(n!2^{C_{n}^{2}}\right)$. Hence, it is unpractical to learn the optimal structure by exhausting the feasible structures for a largish $n$. Instead, structure learning requires either sub-optimal heuristic search algorithms or algorithms that are optimal under certain assumptions [6].

One popular approach for learning structure is search-and-score (S\&S). For an S\&S algorithm, the fitness of a structure to given data is measured by a score function. And a learning task is modeled as an optimization problem, which is to find the structure that maximizes (or minimizes) the score function. Typical score functions include Bayesian Dirichlet (BD) [7,8], Bayesian information criterion (BIC) [9], mutual information tests (MIT) [4], factorized normalized maximum likelihood (fNML) [10], and factorized conditional log-likelihood (fCLL) [11]. For a not large $n$ (around or smaller than 30), accurate algorithms, like dynamic programming (DP) [12-17], can achieve the optimal structures. However, in other cases, the computing complexity and memory requirements are usually unacceptable. Hence, a number of heuristic search algorithms, like greedy search [18,19], evolutionary algorithm [20-22], simulated annealing algorithm [23], particle swarm optimization [24-26], and ant colony optimization [27-29], are applied to finding local optimal solutions. As the search space is multimodal, heuristic search algorithms have a small probability of finding the global optimal solution. For classification, it is important to note that a structure having better score cannot guarantee higher classification accuracy [6].

Constraint-based (CB) is another well-known approach for revealing structures from data. The CB algorithms are relatively fast and have a well-defined stop criterion. They are based on conditional independence (CI) testing and generally asymptotically correct [6]. It may be unreliable in performing CI tests using large condition sets and limited data sizes. Meanwhile, an incorrect structure may be obtained for a sequence of errors caused by a CI testing


[^0]:    Manuscript received November 06, 2018.
    *Corresponding author.

    This work was supported by the National Natural Science Foundation of China (61573285).

error. Typical CB algorithms include recursive autonomy identification (RAI) [6], inductive causation (IC) [30], PC [31], and three phase dependency analysis (TPDA) [32].

In addition, hybrid algorithms have been developed to combine S\&S and CB approaches. In the I-map restart (IMAPR) algorithm [33], a DAG is firstly found by a heuristic algorithm, and then addition/deletion operations on edges of the DAG are performed by using CI testing. However, the sparse candidate (SC) algorithm [34] firstly removes impossible parent candidates by CI testing results, so the search space of the following procedures is relatively limited. Based on this idea, the maxmin hill-climbing (MMHC) algorithm [35] was proposed, where parent candidates are determined by the max-min parents and children (MMPC) algorithm and edges are orientated by the hill-climbing algorithm. The MMHC algorithm is so far the most efficient technique to learn thousands nodes in reasonable time. The constrained optimal search (COS) algorithm [5] can find the optimal structure by reducing the complexity and memory requirements with a super-structure $(n \leqslant 50)$. In addition, the nodes can be divided into strongly connected clusters based on a superstructure [36]. Then the clusters are respectively learned and merged. This algorithm can accurately learn hundreds of nodes.

In this work, we theoretically prove that the nodes of a BN can be layered by conditional independence relationships. For a layer of nodes, its parents belong to the layer, or layers who have priority over the layer. To be specific, for nodes have m-independence (referring to Definition 5 in this paper) relationships conditioned on $\boldsymbol{Z}$, their (include nodes in $\boldsymbol{Z}$ ) parents belong to themselves, or the nodes who have m-independence relationships conditioned on proper subsets of $\boldsymbol{Z}$. For example, let $\boldsymbol{X}, \boldsymbol{Y}$ and $\boldsymbol{Z}$ be disjoint subsets of nodes and $\boldsymbol{X}$ and $\boldsymbol{Y}$ be m-independent conditioned on $\boldsymbol{Z}$. For $\forall X \in \boldsymbol{X} \cup \boldsymbol{Y} \cup \boldsymbol{Z}$, parents of $X$ belong to $\boldsymbol{X} \cup \boldsymbol{Y} \cup \boldsymbol{Z}$ or nodes have m -independence relationships conditioned on corresponding proper subsets of $\boldsymbol{Z}$. Thus $\boldsymbol{X} \cup \boldsymbol{Y} \cup \boldsymbol{Z}$ can be regarded as a node layer, and layers who have priority over $\boldsymbol{X} \cup \boldsymbol{Y} \cup \boldsymbol{Z}$ are determined by all $\boldsymbol{Z}^{\prime} \subseteq \boldsymbol{Z}$. When nodes of a BN have been layered, we can orderly learn each layer alone according to the priority among layers. In this way, the number of feasible structures over a set of nodes can be remarkably reduced, which makes it possible to learn optimal BN structures for bigger sizes of nodes by an accurate algorithm. Therefore, combining the layer approach and ancestrally constrained dynamic programming, we propose a layered optimal learning (LOL) algorithm. The LOL algorithm is a constrained accurate algorithm, which can reduce computing complexity and memory requirements.

The remainder of this paper is organized as follows. Sec-
tion 2 introduces necessary information about BNs. Section 3 outlines the DP algorithms, which are one of the accurate algorithms. Section 4 describes the layering approach and layered optimal learning algorithm. Section 5 demonstrates a case study on a standard BN. Section 6 concludes this work and suggests the future work.

## 2. Preliminaries

A BN $\boldsymbol{B}(\boldsymbol{G}, \boldsymbol{\Theta})$ is a graphical model for decomposing the joint probability distribution for a set of variables (nodes) $\boldsymbol{V}=\left\{X_{1}, \ldots, X_{n}\right\}$. The structure $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$ is a DAG representing dependence relationships among the variables. If variables $X_{i}, X_{j} \in \boldsymbol{V}$ and an arc $X_{j} \rightarrow X_{i} \in$ $\boldsymbol{E}, X_{j}$ is called a parent of $X_{i}$. We define $\boldsymbol{\Pi}_{X_{i}}$ (or $\boldsymbol{\Pi}_{i}$ ) as the parent set for $X_{i}$. The parameter $\boldsymbol{\Theta}$ is the set of CPTs, and a CPT $P\left(X_{i} \mid \boldsymbol{\Pi}_{i}\right)$ quantifies the family (local structure) $\boldsymbol{\Pi} \rightarrow X_{i}$.

Definition 1 Conditional independency [35] Variables $X$ and $Y$ are conditionally independent given $\boldsymbol{Z}$, denoted by $\operatorname{Ind}_{p}(X, Y \mid \boldsymbol{Z})$, with respect to a probability distribution $P$ if $P(X, Y \mid \boldsymbol{Z})=P(X \mid \boldsymbol{Z}) P(Y \mid \boldsymbol{Z})$.

It is easy to prove that $\operatorname{Ind}_{P}(X, Y \mid \boldsymbol{Z}) \Leftrightarrow I(X ; Y \mid \boldsymbol{Z})=$ 0 , where $I(X ; Y \mid \boldsymbol{Z})$ represents the conditional mutual information between $X$ and $Y$ given $\boldsymbol{Z}$.

Definition 2 Markov condition [35] We call a BN satisfies the Markov condition if every variable is independent of any subset of its non-descendant variables conditioned on its parent set.

According to the Markov condition, given $\boldsymbol{\Pi}_{i}, X_{i}$ is independent of all the other ancestral nodes. Thus the joint probability distribution over $\boldsymbol{X}$ can be decomposed as

$$
P(\boldsymbol{V})=\prod_{i=1}^{n} P\left(X_{i} \mid \boldsymbol{\Pi}_{i}\right)
$$

A graphical criterion for representing the conditional independency is d-separation. Before defining d-separation, we introduce another two necessary notions.

Definition 3 Active trail [37] For a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, let $X_{i} \rightleftharpoons \cdots \rightleftharpoons X_{j}$ be a trail in $\boldsymbol{G}$ and $\boldsymbol{Z} \subset \boldsymbol{V}$ be a subset of observed variables. We say the trail $X_{i} \rightleftharpoons \cdots \rightleftharpoons X_{j}$ is active given $\boldsymbol{Z}$ if
(i) whenever we have a $v$-structure $X_{l} \rightarrow X_{t} \leftarrow X_{m}$ (convergent connection), where $X_{t}$ is called a collider, then $X_{T}$ or at least one of its descendants is in $\boldsymbol{Z}$;
(ii) no other node along the trail is in $\boldsymbol{Z}$.

If there are active trails between two nodes given $\boldsymbol{Z}$ in $\boldsymbol{G}$, they are not conditional independent as one can influence another through the active trails. From the contrary of Definition 3, we say a trail is blocked if (i) whenever we have a $v$-structure, the collider and its descendants are not in $\boldsymbol{Z}$; (ii) part of other nodes along the trail are in $\boldsymbol{Z}$.

Once all trails between two nodes are blocked, one cannot influence another. Based on Definition 3, we can obtain the notion of d-separation.

Definition 4 d-separation [37] Let $\boldsymbol{X}, \boldsymbol{Y}$ and $\boldsymbol{Z}$ be three disjoint subsets of nodes in a DAG $\boldsymbol{G}$. We say that $\boldsymbol{X}$ and $\boldsymbol{Y}$ are d-separation given $\boldsymbol{Z}$, denoted $\operatorname{Dsep}_{G}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z})$, if there is no active trail between two nodes of $\forall X \in \boldsymbol{X}, \forall Y \in \boldsymbol{Y}$ given $\boldsymbol{Z}$.

Lemma 1 [38] For any three disjoint subsets $\boldsymbol{X}, \boldsymbol{Y}$, and $\boldsymbol{Z}$ of nodes in a DAG $\boldsymbol{G}$, and for all joint probability distribution $P$, we have
(i) $\operatorname{Dsep}_{\boldsymbol{G}}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z}) \Rightarrow \operatorname{Ind}_{P}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z})$ whenever $\boldsymbol{G}$ and $P$ are compatible;
(ii) if $\operatorname{Ind}_{P}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z})$ holds in all distributions compatible with $\boldsymbol{G}$, then $\operatorname{Dsep}_{G}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z})$.

Lemma 1 shows the connection between $d$-separation and conditional independency. It can help us in building a BN from given data. If all conditional independencies in the joint probability distribution $P$ are entailed by applying local directed Markov condition to $\boldsymbol{G}$, we say that $P$ and $\boldsymbol{G}$ are faithful to each other [38].

Lemma 2 [38] Letting $\boldsymbol{X}, \boldsymbol{Y}$ and $\boldsymbol{Z}$ be three disjoint subsets of nodes in a DAG $\boldsymbol{G}$, we say that $\boldsymbol{B}(\boldsymbol{G}, \boldsymbol{\Theta})$ is faithful if $\operatorname{Ind}_{p}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z})$ holds if and only if $\operatorname{Dsep}_{\boldsymbol{G}}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z})$ holds.

In this paper we assume that the BNs always satisfy the faithfulness condition, and use the notion $\boldsymbol{X} \perp \boldsymbol{Y} \mid \boldsymbol{Z}$ for both $\operatorname{Ind}_{P}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z})$ and $\operatorname{Dsep}_{\boldsymbol{G}}(\boldsymbol{X}, \boldsymbol{Y} \mid \boldsymbol{Z})$. In addition, if a number of disjoint sets $\boldsymbol{M}=\left\{\boldsymbol{X}_{l} \mid l=1,2, \ldots, L\right\}$ are pairwise independent given $\boldsymbol{Z}$, it is denoted by $\perp(\boldsymbol{M} \mid \boldsymbol{Z})$.

## 3. DP

Given data $\boldsymbol{D}=\left\{D_{1}, \ldots, D_{N}\right\}$, learning the BN structure by an S\&S algorithm consists of searching for a DAG that maximizes (or minimizes) a score function from the related domain. The fitness of a structure to the data $\boldsymbol{D}$ is measured by the score function, such as BIC. Let $r_{i}$ be the number of states of node $X_{i}, q_{i}$ be the number of configurations of $\boldsymbol{\Pi}_{i}, N_{X_{i}, \boldsymbol{H}_{i}}$ be the number of data records consistent with the configuration of $\left\{X_{i}\right\} \cup \boldsymbol{\Pi}_{i}$, and $N_{\left\{X_{i}\right\} \cup \boldsymbol{\Pi}_{i}}$ be the number of data records related to the configuration of $\left\{X_{i}\right\} \cup \boldsymbol{\Pi}_{i}$. As the BIC score is decomposable, the score for a DAG $\boldsymbol{G}$ is given by

$$
\operatorname{BIC}(\boldsymbol{G})=\sum_{i=1}^{n} \operatorname{BIC}\left(X_{i} \mid \boldsymbol{\Pi}_{i}\right)
$$

where

$$
\begin{gathered}
\operatorname{BIC}\left(X_{i} \mid \boldsymbol{\Pi}_{i}\right)=-H\left(X_{i} \mid \boldsymbol{\Pi}_{i}\right)-\frac{\ln N}{2} \operatorname{dim}\left(X_{i} \mid \boldsymbol{\Pi}_{i}\right) \\
H\left(X_{i} \mid \boldsymbol{\Pi}_{i}\right)=-\sum_{X_{i}, \boldsymbol{\Pi}_{i}} N_{X_{i}, \boldsymbol{\Pi}_{i}} \ln \frac{N_{X_{i}, \boldsymbol{\Pi}_{i}}}{N_{\boldsymbol{\Pi}_{i}}} \\
\operatorname{dim}\left(X_{i} \mid \boldsymbol{\Pi}_{i}\right)=\left(r_{i}-1\right) q_{i}
\end{gathered}
$$

The BIC score function over feasible DAGs given $\boldsymbol{D}$ is multimodal, so heuristic algorithms have a small probability of achieving the optimal solution. As the DAG domain is discrete and finite, methods of exhaustion are theoretically feasible to learn an optimal structure for small $n$. The optimal BN structure can be found by the DP algorithms in $O\left(n 2^{n}\right)$ time and memories. The memory requirements are reduced to $O\left(C_{n}^{\frac{n}{2}}\right)$ by the memory-efficient DP (MEDP) algorithm [17].

For any $\boldsymbol{X} \subseteq \boldsymbol{V}$, the best BIC score for the rest nodes $\boldsymbol{V} \backslash \boldsymbol{X}$ can be recursively defined as

$$
\begin{gathered}
\operatorname{BestBIC}(\boldsymbol{V} \backslash \boldsymbol{X} \mid \boldsymbol{X})= \\
\max _{\boldsymbol{Y} \subseteq \boldsymbol{V} \backslash \boldsymbol{X},\|\boldsymbol{Y}\|=c} \operatorname{BestBIC}(\boldsymbol{Y} \mid \boldsymbol{X})+ \\
\operatorname{BestBIC}(\boldsymbol{V} \backslash(\boldsymbol{X} \cup \boldsymbol{Y}) \mid \boldsymbol{X} \cup \boldsymbol{Y})
\end{gathered}
$$

where $c \in\{0,1, \ldots,|\boldsymbol{V} \backslash \boldsymbol{X}|\}$ is a constant, $\operatorname{BestBIC}(\boldsymbol{V} \backslash \boldsymbol{X} \mid \boldsymbol{X})$ represents that nodes in $\boldsymbol{X}$ are also parent candidates for nodes in $\boldsymbol{V} \backslash \boldsymbol{X}$, and $\backslash$ represents the difference set operator. A DAG must be consistent with some full orders, which are full permutations on $\boldsymbol{V}$ where parents have priority over children. Thus for the node set $\boldsymbol{V}$, all full orders can cover all feasible DAGs. In other words, letting $\operatorname{BestBIC}(\prec(\boldsymbol{V}))$ be the best BIC score of $\boldsymbol{V}$ restricted by the full order $\prec(\boldsymbol{V})$, we have

$$
\operatorname{BestBIC}(\boldsymbol{V})=\max _{\prec(\boldsymbol{V})} \operatorname{BestBIC}(\prec(\boldsymbol{V}))
$$

Let $\boldsymbol{X}=\varnothing$ and $c \in\{1,|\boldsymbol{V} \backslash \boldsymbol{X}|-1\}$ in (4), it is easy to find that the recursive definition covers all full orders. Thus the algorithm implied in (4) can find the optimal BN structure. If $c=1$, the algorithm goes along the topdown direction; in other words, root nodes are firstly determined, and then children are iteratively added. However, if $c=|\boldsymbol{V} \backslash \boldsymbol{X}|-1$, the algorithm goes along the bottom-up direction, which means leaf nodes are firstly identified and parents are iteratively added. The computing complexities of two algorithms are both $O\left(n 2^{n-1}\right)$, but the memory requirements are different. Along the top-down direction, the size of potential parents for each node gradually increases from zero. Then, to avoid repetitive computation of family scores, in the worst cases, we need to store $O\left(n C_{n-1}^{\frac{n-1}{2}}\right)$ scores. Nevertheless, along the bottom-up direction, the size of potential parents for each node gradually decreases from $n-1$. Thus, to avoid repetitive computation, we have to store all of $O\left(n 2^{n-1}\right)$ family scores at the first step. A learning task probably fails at the beginning because such a mass of scores may be out of memory.

Memory requirements for storing intermediate results (partially learned DAGs and their scores) of two learning strategies are both $O\left(C_{n-1}^{\frac{n-1}{2}}\right)$. Algorithm 1 shows an ancestrally constrained top-down algorithm to compute $\operatorname{BestBIC}(\boldsymbol{Y} \mid \boldsymbol{X})$, where $\boldsymbol{X}$ is the set of learned nodes.

Algorithm 1 Ancestrally constrained DP (ACDP)
Function $[\boldsymbol{G}, s]=\operatorname{AncConstrDP}\left(\boldsymbol{G}_{0}, s_{0}, \boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{D}\right)$ :
$\%$
Input: partially learned DAG $\boldsymbol{G}_{0}$ : $\boldsymbol{G}_{0}$ 's score $s_{0}$; learned nodes $\boldsymbol{X}$; learning nodes $\boldsymbol{Y}$; data $\boldsymbol{D}$.

Output: DAG $\boldsymbol{G}$ and its score $s$.
Initializing learned DAG layer: $\boldsymbol{L}_{\mathrm{DAG}}=\left\{\boldsymbol{G}_{0}\right\}$;
$\%$ indexed by learned nodes
Initializing score layer for $\boldsymbol{L}_{\mathrm{DAG}}: \boldsymbol{S}_{\mathrm{BIC}}=\left\{s_{0}\right\}$;
$\%$ indexed by learned nodes

## Repeat

Let $\widetilde{\boldsymbol{L}}_{\mathrm{DAG}}=\varnothing, \widetilde{\boldsymbol{S}}_{\mathrm{BIC}}=\varnothing$
for each $\boldsymbol{G} \in \boldsymbol{L}_{\mathrm{DAG}}$
$\boldsymbol{T}=$ FindLearnedNodes $(\boldsymbol{G})$;
$\%$ Find learned nodes in $\boldsymbol{G}$
Let $\boldsymbol{R}=\boldsymbol{Y} \backslash \boldsymbol{T}$;
for each node $X \in \boldsymbol{R}$
$\boldsymbol{\Pi}_{X}=\arg \max _{\boldsymbol{U} \subset \boldsymbol{T}} \operatorname{BIC}(X \mid \boldsymbol{U})$
$\tilde{\boldsymbol{G}}=$ AddFamToDAG $\left(\boldsymbol{G}, X, \boldsymbol{\Pi}_{X}\right)$;
$\%$ Add family $\left\{X, \boldsymbol{\Pi}_{X}\right\}$ to $\boldsymbol{G}$.
Let $\boldsymbol{T}^{\prime}=\boldsymbol{T} \cup\{X\}$
if $\widetilde{\boldsymbol{L}}_{\mathrm{DAG}}\left(\boldsymbol{T}^{\prime}\right)=\varnothing$
$\%$ There is no such a DAG in $\widetilde{\boldsymbol{L}}_{\text {DAG }}$
whose learned nodes are $\boldsymbol{T}^{\prime}$.
$\widetilde{\boldsymbol{L}}_{\mathrm{DAG}}=\widetilde{\boldsymbol{L}}_{\mathrm{DAG}} \cup\{\widetilde{\boldsymbol{G}}\}$
$\widetilde{\boldsymbol{S}}_{\mathrm{BIC}}=\widetilde{\boldsymbol{S}}_{\mathrm{BIC}} \cup\left\{\boldsymbol{S}_{\mathrm{BIC}}(\boldsymbol{G})+\operatorname{BIC}\left(X \mid \boldsymbol{\Pi}_{X}\right)\right\}$
else
if $\widetilde{\boldsymbol{S}}_{\mathrm{BIC}}\left(\boldsymbol{T}^{\prime}\right)<\boldsymbol{S}_{\mathrm{BIC}}(\boldsymbol{T})+\operatorname{BIC}\left(X \mid \boldsymbol{H}_{X}\right)$
Let $\widetilde{\boldsymbol{L}}_{\mathrm{DAG}}\left(\boldsymbol{T}^{\prime}\right)=\widetilde{\boldsymbol{G}}$;
$\widetilde{\boldsymbol{S}}_{\mathrm{BIC}}\left(\boldsymbol{T}^{\prime}\right)=\boldsymbol{S}_{\mathrm{BIC}}(\boldsymbol{T})+\operatorname{BIC}\left(X \mid \boldsymbol{\Pi}_{X}\right)$
endif
endif
endfor
endfor
$\boldsymbol{L}_{\mathrm{DAG}}=\widetilde{\boldsymbol{L}}_{\mathrm{DAG}} ;$
$\boldsymbol{S}_{\mathrm{BIC}}=\widetilde{\boldsymbol{S}}_{\mathrm{BIC}} ;$
until $\boldsymbol{R}=\varnothing$;
Here, we have $\boldsymbol{L}_{\mathrm{DAG}}=\{\boldsymbol{G}\}, \boldsymbol{S}_{\mathrm{BIC}}=\{s\}$.
return $\boldsymbol{G}, s ;$

## 4. Layered learning method

For the EMDP algorithm with $O\left(n 2^{n}\right)$ computing complexity, we need $O\left(C_{n}^{\frac{n}{2}}\right)$ memories for storing intermediate results and $O\left(n C_{n-1}^{\frac{n-1}{2}}\right)$ memories for storing necessary family scores. Nevertheless, the complexity and memory requirements still sharply expand as $n$ increases. It limits
the application of EMDP algorithms to learn slightly bigger BNs. Manually defining full or partial orders on nodes is an efficient measure to reduce the complexity and memory requirements. However, in practice, we often have no such prior information. Therefore, in this section we propose an approach to layer nodes of a BN based on CI testing. For a node layer, the parents of the layer can only belong to the layer, or layers who have priority over the layer. Then a BN structure can be learned layer by layer via the ACDP (see Algorithm 1).

### 4.1 Theoretically layering Bayesian networks

In this subsection, for a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, we focus on layering nodes $\boldsymbol{V}$ to make parents of a layer only belong to the layer or previous layers. In this way, the computing complexity and memory requirements can both decrease.

Definition 5 (m-independency). In a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, let $\boldsymbol{Z}$ be a subset of $\boldsymbol{V}$ and $X, Y \in \boldsymbol{V} \backslash \boldsymbol{Z}$. We say $X$ and $Y$ are m-independent conditioned on $\boldsymbol{Z}$, denoted by $X \perp \perp Y \mid \boldsymbol{Z}$, if $X \perp Y \mid \boldsymbol{Z}$ and $X \perp Y \mid(\boldsymbol{Z} \backslash \boldsymbol{U})$ for any non-empty set $\boldsymbol{U} \subset \boldsymbol{Z}$.

For $X \perp \perp Y \mid \boldsymbol{Z}, \boldsymbol{Z}$ is a minimum condition set that blocks all active trails between $X$ and $Y$. In other words, some of active trails cannot be blocked if removing any node from $\boldsymbol{Z}$. For example, in Fig. 1, there are two active trails between node 1 and node 5, which are $1 \rightarrow 3 \rightarrow 5$ and $1 \rightarrow 2 \rightarrow 4 \rightarrow 5$. Sets $\{2,3\},\{3,4\}$, and $\{2,3,4\}$ can block both of the two active trails. However, $\{2,3\}$ and $\{3,4\}$ are minimum but $\{2,3,4\}$ is not, because $\{2,3\}$ and $\{3,4\}$ are subsets of $\{2,3,4\}$, which implies the two active trails can still be blocked if node 2 or node 4 is removed from $\{2,3,4\}$.
![img-0.jpeg](img-0.jpeg)

Fig. 1 A simple BN with five nodes
Lemma 3 In a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, for $\boldsymbol{Z} \subseteq \boldsymbol{V}$ and $X, Y \in$ $\boldsymbol{V} \backslash \boldsymbol{Z}$, let $X \perp \perp Y \mid \boldsymbol{Z}$ hold. Then for $\forall Z \in \boldsymbol{Z}$, there must be such an active trail $X \rightleftharpoons \cdots \rightleftharpoons Z \rightleftharpoons \cdots \rightleftharpoons Y$, where $Z$ is not a collider (convergent connection node) along this trail.

Proof If there do not exist an active trail $X \rightleftharpoons \cdots \rightleftharpoons$ $Z \rightleftharpoons \cdots \rightleftharpoons Y$ where $Z$ is not a collider given $\boldsymbol{Z}$, according to Definitions 3 and 4 and $X \perp Y \mid \boldsymbol{Z}$, we have $X \perp Y \mid \boldsymbol{Z} \backslash\{Z\}$. In other words, $\boldsymbol{Z}$ is not a minimum independent condition set for $X$ and $Y$, which is in contra-

diction with $X \perp \perp Y \mid \boldsymbol{Z}$ (Definition 5). Therefore, the conclusion in the lemma is obtained.

Definition 6 In a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, for $L+1$ disjoint subsets $\boldsymbol{M}=\left\{\boldsymbol{X}_{l} \mid l=1,2, \ldots, L\right\}$ and $\boldsymbol{Z}$ of nodes $\boldsymbol{V}$, let $\perp(\boldsymbol{M} \mid \boldsymbol{Z})$ hold. We say subsets in $\boldsymbol{M}$ are m-independent given $\boldsymbol{Z}$, denoted as $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$, if
(i) for nodes $\forall X \in \boldsymbol{X} \in \boldsymbol{M}, \forall X^{\prime} \in \boldsymbol{X}^{\prime} \in \boldsymbol{M}$, $X \perp \perp X^{\prime} \mid \boldsymbol{Z}$ holds;
(ii) $\operatorname{li} \boldsymbol{U}, \boldsymbol{T} \subset \boldsymbol{X} \in \boldsymbol{M}, \boldsymbol{U} \cup \boldsymbol{T}=\boldsymbol{X}, \boldsymbol{U} \cap \boldsymbol{T}=\varnothing$ make $\boldsymbol{U} \perp \boldsymbol{T} \mid \boldsymbol{Z}$ hold;
(iii) for any m-independence relationship $X \perp \perp X^{\prime} \mid \boldsymbol{Z}$ in $\boldsymbol{G}, \exists \boldsymbol{X}, \boldsymbol{X}^{\prime} \in \boldsymbol{M}$, satisfy $X \in \boldsymbol{X}$ and $X^{\prime} \in \boldsymbol{X}^{\prime}$.

Lemma 4 In a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, for $L+1$ disjoint subsets $\boldsymbol{M}=\left\{\boldsymbol{X}_{l} \mid l=1,2, \ldots, L\right\}$ and $\boldsymbol{Z}$ of nodes $\boldsymbol{V}$, let $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$ hold. Then for $\forall Z \in \boldsymbol{Z}, \mathbb{A} X \in \boldsymbol{X}, X^{\prime} \in \boldsymbol{X}^{\prime}$ make $X \rightarrow Z \leftarrow X^{\prime}$ hold, where $\boldsymbol{X}, \boldsymbol{X}^{\prime} \in \boldsymbol{M}$ and $\boldsymbol{X} \neq \boldsymbol{X}^{\prime}$.

Proof From $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$, we have $X \perp \perp X^{\prime} \mid \boldsymbol{Z}$. Thus $\forall Z \in \boldsymbol{Z}$ cannot be a shared child of $X$ and $X^{\prime}$; otherwise, the trail $X \rightarrow Z \leftarrow X^{\prime}$ is active given $Z$, which is in contradiction with $X \perp \perp X^{\prime} \mid \boldsymbol{Z}$.

Definition 6 , which is stricter than $\perp(\boldsymbol{M} \mid \boldsymbol{Z})$, ensures that all duals, satisfying the m-independent relationship conditioned on $\boldsymbol{Z}$, are included in $\boldsymbol{M}$ and the size of $\boldsymbol{Z}$ is minimal. For a specific $\boldsymbol{Z}$, according to the condition (iii) of Definition 6, there is no more than one m-independence relationship among subsets of $\boldsymbol{V}$. According to Lemma 4, a node in $\boldsymbol{Z}$ cannot be the shared child of nodes coming from different sets in $\boldsymbol{M}$; otherwise, $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$ does not hold. For example, let us have a BN shown in Fig. 1, we thus have $\{1,3\} \perp \perp\{4\} \mid\{2\}$. Although we have $\{1\} \perp\{4\} \mid\{2,3,5\},\{1\} \perp \perp\{4\} \mid\{2,3,5\}$ does not hold considering $\{1\} \perp\{4\} \mid\{2\}$. In addition, $\{1\} \perp \perp\{4\} \mid\{2\}$ does not hold, because $3 \perp \perp 4 \mid\{2\}$ is not included.

Lemma 5 In a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, for $L+1$ disjoint subsets $\boldsymbol{M}=\left\{\boldsymbol{X}_{l} \mid l=1,2, \ldots, L\right\}$ and $\boldsymbol{Z}$ of nodes $\boldsymbol{V}$, let $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$ hold. Then
(i) if $\boldsymbol{Z}=\varnothing, \forall T \notin \bigcup_{l} \boldsymbol{X}_{l}$ respectively have active trails to each set in $\boldsymbol{M}$;
(ii) if $\boldsymbol{Z} \neq \varnothing$, for $\forall T \notin\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$, given $\boldsymbol{Z}, T$ has active trails to no more than one of the sets in $\boldsymbol{M}$; or $T$ has active trails to more than one of sets in $\boldsymbol{M}$, but $T$ is the collider or one descendant of the collider for these trails, and the collider and its descendants are not in $\boldsymbol{Z}$.

Proof For $\boldsymbol{Z} \neq \varnothing$, if $T$ has no active trail to a set in $\boldsymbol{M}, T$ is independent to the set, which is contrary with the condition (iii) of Definition 6. Therefore, $\forall T \notin\left(\bigcup_{l} \boldsymbol{X}_{l}\right)$ has active trails to all sets in $\boldsymbol{M}$.

For $\boldsymbol{Z} \neq \varnothing$, if $T$ is independent of all sets in $\boldsymbol{M}$ conditioned on related proper subsets of $\boldsymbol{Z}$, it is possible that $T$ has no active trail to any set in $\boldsymbol{M}$. If $T$ is independent of the other sets (in addition to $\boldsymbol{X}$ ) in $\boldsymbol{M}$ conditioned on related proper subset of $\boldsymbol{Z}$, it is possible that $T$ only has active trails to the set $\boldsymbol{X} \in \boldsymbol{M}$. If $T$ has active trails to more than one of the sets in $\boldsymbol{M}$, without loss of generality, let $\boldsymbol{X}, \boldsymbol{X}^{\prime} \in \boldsymbol{M}$ and $T$ respectively have active trails $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}$ and $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ to them. From $T$ to $\boldsymbol{X}$ and $\boldsymbol{X}^{\prime}$, let the two active trails finally branch at $T^{*}$. Then to make $\boldsymbol{X} \perp \boldsymbol{X}^{\prime} \boldsymbol{Z}$ hold, the trail $\boldsymbol{X} \rightleftharpoons \cdots \rightleftharpoons T^{*} \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ should be blocked by some nodes on the trail. If the blocking node is not $T^{*}$, active trail $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}$ or $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ is also blocked, which is in contradiction with the assumption. Hence, below we focus on discussing whether $T^{*}$ is the blocking node. (i) Assume $T^{*}$ is a serial connection node (i.e., $\rightarrow T^{*} \rightarrow$ or $\leftarrow T^{*} \leftarrow$ ) along the trail $\boldsymbol{X} \rightleftharpoons \cdots \rightleftharpoons$ $T^{*} \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$. If $T^{*}$ is the blocking node, active trail $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}$ or $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ is still blocked. That is, to keep $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}$ and $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$, active, we cannot block the trail $\boldsymbol{X} \rightleftharpoons \cdots \rightleftharpoons T^{*} \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ when $T^{*}$ is a serial connection node. Here, a contradiction occurs. Therefore, $T^{*}$ is not a serial connection node. (ii) Assume $T^{*}$ be a divergent connection node (i.e.; $\leftarrow T^{*} \rightarrow$ ) along the trail $\boldsymbol{X} \rightleftharpoons \cdots \rightleftharpoons T^{*} \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$. If $T^{*}$ is the blocking node, active trails $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}$ and $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ are still blocked. Hence, $T^{*}$ is not a divergent connection node. (iii) Assume $T^{*}$ is a convergent connection node (i.e., $\rightarrow T^{*} \leftarrow$ ) along the trail $\boldsymbol{X} \rightleftharpoons \cdots \rightleftharpoons$ $T^{*} \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$. If $T^{*}$ or at least one of its descendants belong to $\boldsymbol{Z}, \boldsymbol{X} \rightleftharpoons \cdots \rightleftharpoons T^{*} \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ is an active trail and a contradiction occurs. Thus we have $T^{*}$ and its descendants cannot belong to $\boldsymbol{Z}$. To make $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}$ and $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ active, we have $T^{*} \rightarrow \cdots \rightleftharpoons T$. If there is a collider $T^{\prime}$ along $T^{*} \rightarrow \cdots \rightleftharpoons T$, to keep $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}$ and $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ active, $T^{\prime}$ must belong to $\boldsymbol{Z}$. However, $T^{\prime}$ must be a descendant of $T^{*}$, so $T^{\prime} \notin \boldsymbol{Z}$. Here, a contradiction occurs. Therefore, there is no collider along $T^{*} \rightarrow \cdots \rightleftharpoons T$. Thus $T$ is a descendants of $T^{*}$ or $T=T^{*}$. To sum up, we obtain the result (ii) of Lemma 5.

For the BN shown in Fig. 2, we have $\{1,3\} \perp \perp$ $\{4,6\} \mid\{2\}$. However, node 7 has no active trail to $\{1,3\}$ and $\{4,6\}$; node 5 and node 8 have active trails to $\{1,3\}$ and $\{4,6\}$, and node 5 is the collider and node 8 is a child of the collider. We also have $\{1,2\} \perp \perp\{5,8\} \mid\{3,4\}$; however, node 6 and node 7 only have active trails to $\{5,8\}$.

Theorem 1 For a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, let $\boldsymbol{M}=\left\{\boldsymbol{X}_{l} \mid l=\right.$ $1,2, \ldots, L\}$ be $L$ disjoint subsets of nodes $\boldsymbol{V}$ and $\perp \perp$

$(\boldsymbol{M} \mid \boldsymbol{Z}=\varnothing)$ hold. Then for $\forall X \in \forall \boldsymbol{X} \in \boldsymbol{M}$, we have $\Pi_{X} \subseteq \boldsymbol{X}$.
![img-1.jpeg](img-1.jpeg)

Fig. 2 Simple BN with eight nodes for illustrating Lemma 5
Proof It is easy to find that the parents of $X$ cannot be in the other sets (except $\boldsymbol{X}$ ) in $\boldsymbol{M}$. Let $T \notin\left(\bigcup_{l} \boldsymbol{X}_{l}\right)$ be one parent of $X$. According to Lemma 5 (i), there exists one active trail between $T$ and another set $\boldsymbol{X}^{\prime} \in \boldsymbol{M}$, and let it be $T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$. We can thus find an active trail between $X$ and $\boldsymbol{X}^{\prime}$ as $X \leftarrow T \rightleftharpoons \cdots \rightleftharpoons \boldsymbol{X}$, which is in contradiction with $\boldsymbol{X} \perp \boldsymbol{X}^{\prime}$. Then, $\forall T \notin\left(\bigcup_{i} \boldsymbol{X}_{l}\right)$ cannot be a parent of $X$. Thus we have $\Pi_{X} \subseteq \boldsymbol{X}$.

For the BN shown in Fig. 2, we have $\{1,2,3,4,6\} \perp \perp$ $\{7\}$. It is easy to find the parents of $\{1,2,3,4,6\}$ and $\{7\}$ from themselves. Theorem 1 provides an approach to find the first layer, where the parents of each node in the layer belong to the layer, of a total layering strategy on $\boldsymbol{V}$. The first layer consists of all nodes who have 0-degree $(\boldsymbol{Z}=\varnothing)$ independence relationships in $\boldsymbol{G}$. In other words, we can identify the first layer by finding out all 0-degree independence relationships with CI testing. In addition, according to Theorem 1, when $\boldsymbol{Z}=\varnothing, \forall \boldsymbol{X} \in \boldsymbol{M}$ can be learned alone since for $\forall X \in \boldsymbol{X}$ we have $\Pi_{X} \subseteq \boldsymbol{X}$.

If $\boldsymbol{Z} \neq \varnothing$ and $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z} \neq \varnothing)$ holds, the parents of $\left(\bigcup_{i} \boldsymbol{X}_{i}\right) \cup \boldsymbol{Z}$ are not limited to itself. Nevertheless, subsets of $\boldsymbol{V}$, who satisfy $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z} \neq \varnothing)$, also holds an interesting property that applies to finding subsequent layers one by one, starting from the first layer given by the Theorem 1.

Theorem 2 For a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, let $\boldsymbol{M}=\left\{\boldsymbol{X}_{l} \mid l=\right.$ $1,2, \ldots, L\}$ and $\boldsymbol{Z}$ be $L+1$ disjoint subsets of $\boldsymbol{V}$ and $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$ hold. Then
(i) for $\forall X \in \boldsymbol{X}_{l^{*}} \in \boldsymbol{M}, \boldsymbol{\Pi}_{X} \subset \boldsymbol{X}_{l^{*}} \cup \boldsymbol{X}_{l^{*}}^{\mathrm{Csub}(\boldsymbol{Z})} \cup \boldsymbol{Z}$. Here, $\boldsymbol{X}_{l^{*}}^{\mathrm{Csub}(\boldsymbol{Z})}$ is the set of such nodes $T$ that satisfies $T \notin\left(\bigcup_{i} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z},\{T\} 3_{\llcorner } \boldsymbol{X}_{l^{*}} \mid \boldsymbol{Z}$, and for $\forall Y \in \bigcup_{l \neq l^{*}} \boldsymbol{X}_{l}$, $\exists \boldsymbol{Z}^{\prime} \subseteq \boldsymbol{Z}$, makes $T \perp \perp Y \mid \boldsymbol{Z}^{\prime}$ hold; that is, $\boldsymbol{X}_{l^{*}}^{\mathrm{Csub}(\boldsymbol{Z})}$
is the set of nodes that are m-dependent of all nodes from the other sets (in addition to $\boldsymbol{X}_{l^{*}}$ ) in $\boldsymbol{M}$ conditioned on corresponding proper subsets of $\boldsymbol{Z}$.
(ii) for $\forall Z \in \boldsymbol{Z}, \boldsymbol{\Pi}_{z} \subset \boldsymbol{X} \cup \boldsymbol{X}^{\mathrm{Csub}(\boldsymbol{Z})} \cup \boldsymbol{Z} \cup \varnothing^{\mathrm{Csub}(\boldsymbol{Z})}$ ( $\boldsymbol{X}$ can only be one of the sets in $\boldsymbol{M}$ ). Here, $\varnothing^{\mathrm{Csub}(\boldsymbol{Z})}$ is the set of such nodes $T$ that satisfies $T \notin\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$, and for $\forall Y \in \bigcup_{l} \boldsymbol{X}_{l}, \exists \boldsymbol{Z}^{\prime} \subseteq \boldsymbol{Z}$, makes $T \perp \perp Y \mid \boldsymbol{Z}^{\prime}$ hold; that is, $\varnothing^{\mathrm{Csub}(\boldsymbol{Z})}$ is the set of nodes that are m-independent of the nodes from all sets in $\boldsymbol{M}$ conditioned on corresponding proper subsets of $\boldsymbol{Z}$.

Proof According to Lemmas 3 and 4, it is easy to verify that for $\forall X \in \boldsymbol{X}_{l^{*}} \in \boldsymbol{M}$, the parents of $X$ can belong to $\boldsymbol{X}_{l^{*}} \cup \boldsymbol{Z}$ but must be not in the other sets (in addition to $\boldsymbol{X}_{l^{*}}$ ) in $\boldsymbol{M}$. Let $T \notin\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$ be a parent of $X$, then $T$ is not a collider or one descendant of a collider about $X$ because we have $T \rightarrow X$. Hence, according to Lemma 5 (ii), $T$ can only have active trails to one set of $\boldsymbol{M}$, and the set must be $\boldsymbol{X}_{l^{*}}$. In other words, $T$ is independent to the other sets of $\boldsymbol{M}$ giving $\boldsymbol{Z}$. However, $\boxtimes X^{\prime} \in \bigcup_{l \neq l^{*}} \boldsymbol{X}_{l}$ makes $T \perp \perp X^{\prime} \mid \boldsymbol{Z}$ hold, because according to Definition 6 (iii), all m-independence relationships conditioned on $\boldsymbol{Z}$ are included in $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$ but $T \notin\left(\bigcup_{i} \boldsymbol{X}_{l}\right)$. Therefore, for $\forall Y \in \bigcup_{l \neq l^{*}} \boldsymbol{X}_{l}, \exists \boldsymbol{Z}^{\prime} \subseteq \boldsymbol{Z}$, makes $T \perp \perp$ $Y \mid \boldsymbol{Z}^{\prime}$ hold; noticing $\{T\} 3_{\llcorner } \boldsymbol{X}_{l^{*}} \mid \boldsymbol{Z}$, so $T \in \boldsymbol{X}_{l^{*}}^{\mathrm{Csub}(Z)}$. To sum up, $\boldsymbol{\Pi}_{X} \subset(\boldsymbol{X}+\boldsymbol{Z}) \cup \boldsymbol{X}^{\mathrm{Csub}(\boldsymbol{Z})}$.

For $\forall Z \in \boldsymbol{Z}$, it is easy to verify that $Z$ 's parents can belong to $\boldsymbol{Z}$. And according to Lemmas 3 and $4, Z$ is a serial or divergent connection node in the relationship of $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$, so $Z$ 's parents can belong to no more than one of sets in $\boldsymbol{M}$. Let $T \notin\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$ be a parent of $Z$. Assuming $T$ has active trails to two sets $\boldsymbol{X}, \boldsymbol{X}^{\prime} \in \boldsymbol{M}$ given $\boldsymbol{Z}$, we thus have two active trails $T \rightleftharpoons \ldots \rightleftharpoons \boldsymbol{X}$ and $T \rightleftharpoons \ldots \rightleftharpoons \boldsymbol{X}^{\prime}$. Then according to Lemma 5 (ii), we can construct a trail between $\boldsymbol{X}$ and $\boldsymbol{X}^{\prime}$ as $\boldsymbol{X} \rightleftharpoons$ $\cdots \rightarrow T^{*} \leftarrow \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$, where $T^{*}$ is an ancestor of $T$. As is a parent of $Z, T^{*}$ is also an ancestor of $Z$. Noticing that $Z$ is a condition node, according to Definition 3, $\boldsymbol{X} \rightleftharpoons \cdots \rightarrow T^{*} \leftarrow \cdots \rightleftharpoons \boldsymbol{X}^{\prime}$ is active, which is in contradiction with $\boldsymbol{X} \perp \boldsymbol{X}^{\prime} \mid \boldsymbol{Z}$. Therefore, $T$ has active trails to no more than one of sets in $\boldsymbol{M}$ given $\boldsymbol{Z}$. If $T$ has no active trail to each set of $\boldsymbol{Z}$, we have $T \in \varnothing^{\mathrm{Csub}(Z)}$. If $T$ has active trail to one set $\boldsymbol{X} \in \boldsymbol{M}$, we have $T \in \boldsymbol{X}^{\mathrm{Csub}(Z)}$. In addition, $\boldsymbol{X}$ must be the only set in $\boldsymbol{M}$ that can be the

parents for $Z$; otherwise, let $\boldsymbol{X}^{\prime}$ be the only set in $\boldsymbol{M}$ that can be the parents of $X$, and then we have an active trail $\boldsymbol{X} \rightleftharpoons \cdots \rightleftharpoons T \rightarrow Z \leftarrow \boldsymbol{X}^{\prime}$ given $\boldsymbol{Z}$, which is in contradiction with $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$. To sum up, $Z$ 's parents can belong to no more than one $\boldsymbol{X} \cup \boldsymbol{X}^{\operatorname{Csub}(\boldsymbol{Z})}(\boldsymbol{X} \in \boldsymbol{M})$, or $\boldsymbol{Z}$, or $\varnothing^{\operatorname{Csub}(Z)}$.

In fact, Theorem 1 is a particular case, where condition set $\boldsymbol{Z}=\varnothing$, of Theorem 2. For Theorem 2 with $\boldsymbol{Z}=\varnothing$, noticing that empty set $\varnothing$ has no proper subset, $\boldsymbol{X}^{\operatorname{Csub}(\boldsymbol{Z})}=\varnothing$. Then, the result (i) of Theorem 2 is exactly Theorem 1. Of course, the result (ii) is null for an empty condition set.

From Theorem 2 we can find that for $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z} \neq \varnothing)$ holding, the parents of $X \in\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$ must belong to $\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$, or nodes are m-independent conditioned on corresponding proper subsets of $\boldsymbol{Z}$; in other words, when all nodes that are m-independent conditioned on proper subsets of $\boldsymbol{Z}$ have been learned, the parents of $\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$ belong to themselves or previously learned nodes. Therefore, Theorem 2 provides an approach to find following layers of nodes after the first layer has been given by Theorem 1. That is, when the first layer has been obtained, the subsequent layers can orderly be added by using Theorem 2. In conclusion, we can also say that for $\forall \boldsymbol{Z}^{\prime} \subseteq \boldsymbol{Z}$, under the layering strategy provided by Theorems 1 and 2, the nodes holding m-independence relationships conditioned on $\boldsymbol{Z}^{\prime}$ always have priority over the nodes holding m-independence relationship conditioned on $\boldsymbol{Z}$, as shown in Fig. 3. For each arrow, the set at the starting point has priority over the set at the ending point. In addition, the priority possesses transitivity.
![img-2.jpeg](img-2.jpeg)

Fig. 3 Simple example for illustrating the priority among condition sets

When there is no 0-degree independence relationship in a BN, for $|\boldsymbol{Z}|=1$ we have $\varnothing^{\operatorname{Csub}(\boldsymbol{Z})}=\varnothing$ and $\boldsymbol{X}^{\operatorname{Csub}(\boldsymbol{Z})}=\varnothing(\boldsymbol{X} \in \boldsymbol{M})$. According to Theorem 2, the nodes who have 1-degree independence relationships can be taken as the first layer, because the parents of $\forall X \in\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$ must belong to $\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$. By
parity of reasoning, when there is no lower degree independence relationships in a BN, nodes who have the lowest degree independence relationships can be taken as the first layer. This is expressed in Corollary 1.

Corollary 1 For a DAG $\boldsymbol{G}(\boldsymbol{V}, \boldsymbol{E})$, let $\boldsymbol{M}=\left\{\boldsymbol{X}_{l} \mid l=\right.$ $1,2, \ldots, L\}$ and $\boldsymbol{Z}$ be $L+1$ disjoint subsets of $\boldsymbol{V}$ and $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$ hold. If $\boldsymbol{Z}$ is an independence condition with the lowest degree in $\boldsymbol{G}$, then
(i) for $\forall X \in \boldsymbol{X} \in \boldsymbol{M}, \boldsymbol{\Pi}_{X} \subset(\boldsymbol{X} \cup \boldsymbol{Z})$;
(ii) for $\forall Z \in \boldsymbol{Z}, \boldsymbol{\Pi}_{Z} \subset \boldsymbol{X} \cup \boldsymbol{Z}$ ( $\boldsymbol{X}$ can only be one of the sets in $\boldsymbol{M}$ ).

Proof Noticing that $\varnothing^{\operatorname{Csub}(\boldsymbol{Z})}=\varnothing$ and $\boldsymbol{X}^{\operatorname{Csub}(\boldsymbol{Z})}=$ $\varnothing(\boldsymbol{X} \in \boldsymbol{M})$ if $\boldsymbol{Z}$ is an independence condition with the lowest degree in $\boldsymbol{G}$, according to Theorem 2, we have Corollary 1.

The layering approach, implicated in Theorems 1 and 2, also provides a way to incorporating such prior information that a "subgraph" of the DAG is known. Here, the "subgraph" means the parents for each node are included in the "subgraph". Given a "subgraph", we can orderly add node layers according to Theorem 2.

### 4.2 LOL algorithm

Based on Theorems 1 and 2 discussed in the previous subsection, we can layer nodes of a DAG by CI testing. For two variables $X_{i}$ and $X_{j}$, it is possible to measure if they are independently conditioned on $\boldsymbol{Z}$ by using $G^{2}$ statistic, under the null hypothesis of conditional independency holding [39]. We denote $N_{X_{i}, X_{j}, \boldsymbol{Z}}$ for the number of data records consistent with the configuration of $\left\{X_{i}, X_{j}\right\} \cup \boldsymbol{Z}$, and similarly, $N_{X_{i}, \boldsymbol{Z}}$ for $\left\{X_{i}\right\} \cup \boldsymbol{Z}, N_{X_{j}, \boldsymbol{Z}}$ for $\left\{X_{j}\right\} \cup \boldsymbol{Z}$, and $N_{\boldsymbol{Z}}$ for $\boldsymbol{Z}$. Then we have

$$
G^{2}=2 \sum_{X_{i}, X_{j}, \boldsymbol{Z}} N_{X_{i}, X_{j}, \boldsymbol{Z}} \ln \frac{N_{X_{i}, X_{j}, \boldsymbol{Z}} N_{\boldsymbol{Z}}}{N_{X_{i}, \boldsymbol{Z}} N_{X_{j}, \boldsymbol{Z}}}
$$

The $G^{2}$ statistic is asymptotically distributed as $\chi^{2}(d f)$ under the null hypothesis, where $d f=\left(r_{i}-1\right)\left(r_{j}-\right.$ 1) $\prod_{X_{t} \in \boldsymbol{Z}_{t}} r_{t}$ and $r_{i}$ is the number of states for $X_{i}$. The $\chi^{2}$ test returns a $p$ value that corresponds to the probability of falsely rejecting the null hypothesis given it is true. For a threshold (significance level) $\alpha$, if $p \leqslant \alpha$ null hypothesis is rejected, that is $X_{i}$ and $X_{j}$ are considered as conditionally dependent conditioned on $\boldsymbol{Z}$.

When a layer has been found, the ACDP algorithm (illustrated in Algorithm 1) is recalled to learn this layer. The proposed algorithm LOL is shown in Algorithm 2.

Algorithm 2 LOL.
Input: data $D$, node set $\boldsymbol{V}$, threshold $K$.
Output: learned GAG $\boldsymbol{G}$ and its score $s$.
Initializing condition queue: $\boldsymbol{Q}=[\varnothing]$;
Initializing leaned nodes: $\boldsymbol{X}=\varnothing$;

Initializing unleaned nodes: $\boldsymbol{R}=\boldsymbol{V}$;
Initializing the degree for CI testing: $d=0$;
while $\boldsymbol{R} \neq \varnothing$
Initializing the node layer: $\boldsymbol{L}=\varnothing$;
$\%$ layering step
for each pair of nodes $\left\{X_{i}, X_{j}\right\}$ from $\boldsymbol{V} \backslash \boldsymbol{Q}(1)$
if $X_{i} \perp \perp X_{j} \mid \boldsymbol{Q}(1)$
$\boldsymbol{L}=\boldsymbol{L} \cup\left\{X_{i}, X_{j}\right\}$
endif
endfor
$\boldsymbol{L}=\boldsymbol{L} \backslash \boldsymbol{X}$
\% learning step, recall Algorithm 1
$[\boldsymbol{G}, s]=\operatorname{Anc} \operatorname{ConstrDP}(\boldsymbol{G}, s, \boldsymbol{X}, \boldsymbol{L}, \boldsymbol{D})$;
$[\boldsymbol{Q}, d]=\operatorname{Update} \boldsymbol{Q}(\boldsymbol{Q}, \boldsymbol{X}, \boldsymbol{L}, d)$;
$\%$ see the function in the end
$\boldsymbol{X}=\boldsymbol{X} \cup \boldsymbol{L} ; \boldsymbol{R}=\boldsymbol{R} \backslash \boldsymbol{L} ;$
if $|\boldsymbol{R}| \leqslant K$
$[\boldsymbol{G}, s]=\operatorname{Anc} \operatorname{ConstrDP}(\boldsymbol{G}, s, \boldsymbol{X}, \boldsymbol{R}, \boldsymbol{D})$;
$\boldsymbol{X}=\boldsymbol{X} \cup \boldsymbol{R} ; \boldsymbol{R}=\varnothing$;
endif
endwhile
return $\boldsymbol{G}, s$.
$\%$ function
Function $[\boldsymbol{Q}, d]=\operatorname{Update} \boldsymbol{Q}(\boldsymbol{Q}, \boldsymbol{X}, \boldsymbol{L}, d)$;
Removing $\boldsymbol{Q}(1)$ from $\boldsymbol{Q}$;
if $\boldsymbol{Q}=\varnothing$ and $\boldsymbol{L}=\varnothing$
$d=d+1$
Adding all $d$ subsets of $\boldsymbol{X}$ into $\boldsymbol{Q}$;
return;
end
for $t=1,2, \ldots, d$
Letting $\boldsymbol{Q}^{(t)}$ be the set of $\boldsymbol{T} \subset \boldsymbol{X} \cup \boldsymbol{L}$, where $\boldsymbol{T} \cap \boldsymbol{L} \neq \varnothing$ and $|\boldsymbol{T}|=t$;

Inserting sets of $\boldsymbol{Q}^{(t)}$ into $\boldsymbol{Q}$, before the first set in $\boldsymbol{Q}$ who has at least $t$ elements;
endfor
return $\boldsymbol{Q}, d$.
There are two typical steps in the LOL algorithmlayering step and learning step. At the layering step, a new layer of nodes is generated according to Theorem 2. There is a queue " $\boldsymbol{Q}$ " of condition sets coming from learned nodes in the LOL algorithm, which guarantees that for any condition set its each proper subset has priority over it. Based on the queue " $\boldsymbol{Q}$ ", a condition set can be applied to determining a new layer only if all of its proper subsets have been considered. According to Theorem 2, we have that the parents of a new layer must belong to the new layer or previously learned nodes (see Proposition 1). In the learning step, by using the ACDP algorithm,
a new layer is learned ancestrally constrained by previously leaned nodes. The layering step and learning step alternate until all nodes have been learned.

Proposition 1 Theoretically, Algorithm 2 can reveal the true DAG or its equivalence class.

Proof Reference [7] has proved that "choose the model for which BIC score is largest" is asymptotically correct. In the LOL algorithm, a node layer $\boldsymbol{L}$ 's potential parent set is $\boldsymbol{X} \cup \boldsymbol{L}$, where $\boldsymbol{X}$ is the learned nodes. For any node layer $\boldsymbol{L}$, if we can guarantee that $\boldsymbol{L}$ 's true parents belong to $\boldsymbol{X} \cup \boldsymbol{L}$, the ACDP algorithm can find out the optimal DAG, because ACDP is an accurate algorithm constrained by ancestral nodes. For $\boldsymbol{L}$ and its condition set $\boldsymbol{Z}$ (a certain $\boldsymbol{Q}(1)$ in Algorithm 2), according to Theorem 2, for $\forall X_{i} \perp \perp X_{j} \mid \boldsymbol{Z}^{\prime}$ and $\boldsymbol{Z}^{\prime} \subseteq \boldsymbol{Z}$, Algorithm 2 should guarantee that $\left\{X_{i}, X_{j}\right\} \subset \boldsymbol{X}$ holds; that is, $\left\{X_{i}, X_{j}\right\}$ should be learned before $\boldsymbol{L}$. In Algorithm 2, the function "Update $\boldsymbol{Q}$ " controls the queue of independent conditions. In the function "Update $\boldsymbol{Q}$ ", noticing the procedures between "for" and "endfor" can guarantee that $\forall \boldsymbol{Z}^{\prime} \subseteq \boldsymbol{Z}$ have priority over $\boldsymbol{Z}$. In addition, according to the function "Update $\boldsymbol{Q}$ ", we can find that each condition set $\boldsymbol{Z}$ consists of learned nodes; that is, $\boldsymbol{Z}$ 's parents have been determined when learning previous node layers. Therefore, for each node layer $\boldsymbol{L}$, we have $\left(\bigcup_{X \in \boldsymbol{L}} \boldsymbol{H}_{X}\right) \subset(\boldsymbol{L} \cup \boldsymbol{X})$. Then, tracing back to the beginning, Algorithm 2 can theoretically reveal the true DAG or its equivalence class.

### 4.3 Complexity analysis

Below we discuss the computing complexity and memory requirements of the proposed LOL algorithm. Let node set $\boldsymbol{V}$ be divided into $L$ disjointed layers $\left\{\boldsymbol{L}_{l} \mid l=1, \ldots, L\right\}$, where $\left|\boldsymbol{L}_{l}\right|=k_{l}$, and the structure is orderly learned according to the layers.

For the complexity, we mainly focus on the number of potential family scores, since the learning step is much more time-consuming than the layering step. For $\forall X \in$ $\boldsymbol{L}_{l}$, according to Algorithm 1 (learning step of Algorithm 2), its parent candidate set is $\left(\bigcup_{t \leqslant l} \boldsymbol{L}_{t}\right) \backslash\{X\}$, which totally has $-1+\sum_{t=1}^{l} k_{t}$ nodes. Hence, the number of family scores for $X$ is $2^{-1+\sum_{t=1}^{l} k_{t}}$. Then, the number of family scores for the node layer $\boldsymbol{L}_{l}$ is $k_{l} 2^{-1+\sum_{t=1}^{l} k_{t}}$. Thus we have that the total number of family scores for $\boldsymbol{V}$ is $\sum_{l} k_{l} 2^{-1+\sum_{t=1}^{l} k_{t}}$. Let $\sum_{l} k_{l} 2^{-1+\sum_{t=1}^{l} k_{t}}=\rho 2^{-1+\sum_{l} k_{l}}$,

where $\rho=\sum_{l} \frac{k_{l}}{\sum_{2^{l-1}+1} k_{l}}$. As $\sum_{l} k_{l}=n$ and $2^{\sum_{i=l+1}^{L} k_{l}} \geqslant 1$, $\rho<n$ holds. To sum up, the complexity for the LOL algorithm is $O\left(\rho 2^{n-1}\right)$ and $\rho<n$. In practice, $\rho$ is usually much smaller than $n$, since $k_{l} \ll 2^{\sum_{i=l+1}^{L} k_{l}}$ for $l<L$. For example, if a full order is given, it is easy to prove that $\rho<2$.

For the memory requirements, we mainly focus on the memories for storing family scores and the memories for storing intermediate results, including partially learned BNs and their scores. The maximal number of consumed memories is determined by the layer with most nodes. For $k^{\#}=\max \left\{k_{l} \mid l=1, \ldots, L\right\}$, the number of memories for storing family scores is $O\left(k^{\#} C_{k^{\#}-1}^{\frac{k^{\#}}{k}} \right)$, which is much smaller than $O\left(n C_{n-1}^{\frac{n-1}{2}}\right)$ of the EMDP algorithms; and
the number of memories for storing intermediate results is $O\left(C_{k^{\#}}^{\frac{k^{\#}}{k}}\right)$, which is much smaller than $O\left(C_{n}^{\frac{k}{k}}\right)$ of the EMDP algorithms. In conclusion, in the worst case, the LOL algorithm consumes $O\left(C_{k^{\#}}^{\frac{k^{\#}}{k}}\right)$ memories.

## 5. Case studies

To experimentally evaluate the proposed algorithm, a standard BN (illustrated in Fig. 4) is introduced to perform structure learning. There are 50 nodes in the BN, and each of them is binary. For comparison, we consider four competing algorithms, which are hill-climbing (HC) [35], MMHC [35], PC [31], and TPDA [32] algorithms. Since a DAG learned by the LOL is sometimes not a local optimum for the BIC score criterion, we apply the HC algorithm to search a local optimal structure starting from the result of LOL, and we refer to the improved LOL methods as LOL+.
![img-3.jpeg](img-3.jpeg)

Fig. 4 Bayesian network with 50 nodes

The experiments are implemented based on the Bayes net toolbox (BNT) [40] and BNT structure learning package (SLP) [41]. The HC, PC, and TPDA algorithms are obtained from the SLP, while the MMHC algorithm is written by us. The training data are randomly sampled from the true BN by the function "sample_bnet" provided by the BNT. The HC and MMHC algorithms start from empty DAGs $(\boldsymbol{E}=\varnothing)$. For the LOL, CI testing was implemented before learning within 2-degree. If $X \perp \perp Y \mid \boldsymbol{Z}$, for $\forall \boldsymbol{Z}^{\prime} \supseteq \boldsymbol{Z}, X \perp \perp Y \mid \boldsymbol{Z}^{\prime}$ does not holds. By using this property, we reduce the number of independence tests. The significance level for CI testing is 0.05 . In addition, the data sizes are fixed at $1000,2000$, and 5000 .

The learning results and running times are illustrated in Tables 1 and 2. The bold represents the best. We do not
only learn the whole network; however, we also learn part of the BN. And the " $n$ " in Tables $1-3$ expresses the number of considered nodes; that is, we only learn the first " $n$ " nodes of the BN in the related experiment. " - " in Tables 1 and 2 expresses an algorithm fails to obtain a DAG. We can notice that the PC and TPDA algorithms have failed to obtain DAGs in some cases. And the error, provided by the SLP package, is always "pdag_to_dag error : This pdag does not admit any extension", which means there are conflicts among CI tests and no DAG satisfies all testing results (conditional independences obtained from data). In addition to learning results, we also collect the node layers obtained from CI testing results by the LOL algorithm, which is demonstrated in Table 3.

Table 1 BIC scores for learned BNs


Table 2 Running time


Table 3 Layers of nodes obtained by the LOL algorithm


Table 1 shows that the LOL+ achieves the best BIC scores in all learning cases, while the LOL algorithm performs the best in ten learning cases. When the LOL and LOL+ algorithms simultaneously perform the best, the basic LOL algorithm has not been improved by the HC algorithm, which implies that the LOL algorithm reaches a local (or global) optimum. When the LOL+ obtains the best result alone, the basic LOL algorithm has been improved by the HC algorithm, which implies that the LOL algorithm does not reach a local (or global) optimum. These results suggest that the LOL algorithm cannot guarantee the local optimum. Meanwhile, the LOL algorithms outperform the competing algorithms in all learning cases. Comparing LOL with MMHC, which are both hybrid algorithms, the LOL algorithm has better performance with respect to the BIC score criterion.

According to Table 1, with $n$ increasing, it becomes more difficult to reach a local (or global) optimum for the basic LOL algorithm. In general, more node layers are needed for more nodes (referring to Table 3), which need more CI tests. Then, it has greater probability of occurring CI testing errors. As mentioned in Section 1, a CI testing error will cause a sequence of errors in other tests. The incorrect CI testing results will lead to incorrect node layers, which can reduce the learning accuracy of the LOL algorithm.

However, Table 1 also shows that with the data size increasing, in general the LOL algorithm has greater probability of reaching a local (or global) optimum (see $n=$ $35,40,45)$. More data are helpful to improving the accuracy of CI testing, which can reduce the probability of obtaining incorrect node layers. Then, the learning accuracy increases.

The learning results show that the PC and TPDA algorithms fail to obtain DAGs sometimes. It implies that CI testing is often unreliable, because a previous error will cause a sequence of errors. Sometimes the errors only lead to error arcs in a DAG; however, if the errors cause contradictions among CI testing results, there is even no DAGs satisfying all conflicting CI testing results. Hybrid algorithms, like MMHC or the proposed LOL, can mediate the trouble. For the LOL and MMHC algorithms, CI testing results are only applied to reducing search space, while they orient or lean edges by S\&S approaches.

Table 2 demonstrates that the LOL algorithm spends much more time than the MMHC, HC, TPDA, and PC algorithms under an identical condition. Noticing that the learning step of the LOL algorithm is based on an accurate algorithm (ACDP), its complexity cannot be too small. However, as the nodes of a BN are layered, the memory requirements reduce to $O\left(C_{k^{\#}}^{\frac{k^{\#}}{k}}\right)$ from $O\left(C_{d}^{\#}\right)\left(k^{\#}<\right.$ $n)$, which makes it possible to learn bigger BNs with accurate algorithms.

## 6. Conclusions and future work

In this work, we theoretically prove that a BN can be divided into layers by using CI testing. As we propose in Theorem 2, for $L+1$ disjoint subsets $\boldsymbol{M}=\left\{\boldsymbol{X}_{l} \mid l=\right.$ $1,2, \ldots, L\}$ and $\boldsymbol{Z}$, if $\perp \perp(\boldsymbol{M} \mid \boldsymbol{Z})$ holds, the parents of $\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$ belong to $\left(\bigcup_{l} \boldsymbol{X}_{l}\right) \cup \boldsymbol{Z}$, or the nodes that have m-independence relationships conditioned on corresponding proper subsets of $\boldsymbol{Z}$. An approach to layer nodes

of a BN is implied in Theorem 2; that is, for $\forall \boldsymbol{Z}^{\prime} \subseteq \boldsymbol{Z}$, the nodes that possess m-independence relationships conditioned on $\boldsymbol{Z}^{\prime}$ have priority over the nodes possessing mindependence relationships conditioned on $\boldsymbol{Z}$, because the former nodes can be potential parents for the latter nodes. Theorem 1 shows that nodes who have 0-degree (the condition set is empty) m-independence relationships can be taken as the first layer, where the parents of the layer belong to the layer, too. In fact, some BNs have no 0-degree m-independence relationships. In this scenario, Theorem 1 fails to work. However, Corollary 1, obtained from Theorem 2, illustrates that the nodes who have m-independence relationships with the lowest degree condition set can be the first layer.

Combining the above layering approach with the ACDP, an accurate algorithm shown in Algorithm 1, we propose an LOL algorithm (shown in Algorithm 2), which is a hybrid algorithm. There are two typical steps in the LOL algorithm - layering step and learning step. At the layering step, based on the layering approach, a new layer is found conditioned on the learned nodes; at the learning step, the ACDP algorithm is applied to learning the new layer constrained by previously learned nodes. Compared to the EMDP algorithm, the complexity of the LOL algorithm reduces to $O\left(\rho 2^{n-1}\right)$ from $O\left(n 2^{n-1}\right)(\rho<n)$, and the memory requirements reduce to $O\left(C_{k^{\#}}^{\frac{k^{\#}}{k}}\right)$ from $O\left(C_{n}^{\frac{n}{k}}\right)\left(k^{\#}<n\right)$. The LOL algorithm cannot guarantee that a local optimum is found with respect to the BIC score criterion. Thus it can be further improved by heuristic algorithms, including the HC algorithm.

In the case study, compared to the MMHC, HC, TPDA, and PC algorithms, we apply the proposed LOL algorithm to learning a standard BN with 1000,2000 , and 5000 data. In general, the LOL algorithm performs the best with respect to the BIC score criterion, because it achieves best results in all learning cases. However, as the learning step of the LOL algorithm is based on the accurate algorithm ACDP, the LOL is more time-consuming than MMHC, HC, TPDA, and PC algorithms. However, the layering approach proposed can reduce complexity and memory requirements, which makes it possible to learn bigger BNs with accurate algorithms.

It is easy to find that the LOL algorithm is compatible with ancestor constraints [42], which defines that some nodes are ancestors of other nodes. It is possible to judge whether a node layer violates ancestor constraints. For example, if a descendant node belongs to a new layer but its ancestor has not been learned, it is suspectable that some errors have occurred in CI testing; and then we can adopt
measures to mediate this conflict. Therefore, we think it is interesting to further improve the LOL algorithm by incorporating ancestor constraints.

## Biographies

![img-4.jpeg](img-4.jpeg)

YANG Yu was born in 1991. He received his B.S. degree from Northwestern Polytechnical University, Xi'an, China. He is now a Ph.D. candidate from the Department of System Engineering, Northwestern Polytechnical University. His areas of research include Bayesian networks, data mining, and image recognition.
E-mail: youngiv@126.com
![img-5.jpeg](img-5.jpeg)

GAO Xiaoguang received her Ph.D. degree from Northwestern Polytechnical University, Xi'an, China in 1989. She is currently a professor in the Department of System Engineering, Northwestern Polytechnical University. She now is the deputy director of Automatic Control Specialized Committee of China Ordnance Industry Association, and a specialized committee member of China Aviation Society of Weapon System and Photoelectric Technology of China Astronautical Society. Her research interests include probabilistic graphical models, deep learning, reinforcement learning, advanced control theory and its application in complex systems, attack defense confrontation and effectiveness evaluation of integrated avionics systems, and aviation fire control and operational effectiveness analysis.
E-mail: cxg2012@nwpu.edu.cn
![img-6.jpeg](img-6.jpeg)

GUO Zhigao is currently a Ph.D. candidate at the Department of System Engineering, Northwestern Polytechnical University. His research interests cover Bayesian networks, model optimization, knowledge and data mining. He has been the author of peer-reviewed publications on International Journal of Approximate Reasoning, Advanced Methodology for Bayesian Networks, and so on. E-mail: buckleyguo@mail.nwpu.edu.cn