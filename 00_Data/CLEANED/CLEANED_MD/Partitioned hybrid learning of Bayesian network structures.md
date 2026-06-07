# Partitioned hybrid learning of Bayesian network structures 

Jireh Huang ${ }^{1} \cdot$ Qing Zhou ${ }^{1}$ (D)<br>Received: 11 March 2021 / Revised: 18 November 2021 / Accepted: 23 January 2022 /<br>Published online: 16 March 2022<br>© The Author(s) 2022


#### Abstract

We develop a novel hybrid method for Bayesian network structure learning called partitioned hybrid greedy search ( pHGS ), composed of three distinct yet compatible new algorithms: Partitioned PC ( pPC ) accelerates skeleton learning via a divide-and-conquer strategy, $p$-value adjacency thresholding (PATH) effectively accomplishes parameter tuning with a single execution, and hybrid greedy initialization (HGI) maximally utilizes constraint-based information to obtain a high-scoring and well-performing initial graph for greedy search. We establish structure learning consistency of our algorithms in the largesample limit, and empirically validate our methods individually and collectively through extensive numerical comparisons. The combined merits of pPC and PATH achieve significant computational reductions compared to the PC algorithm without sacrificing the accuracy of estimated structures, and our generally applicable HGI strategy reliably improves the estimation structural accuracy of popular hybrid algorithms with negligible additional computational expense. Our empirical results demonstrate the competitive empirical performance of pHGS against many state-of-the-art structure learning algorithms.


Keywords Bayesian networks $\cdot$ Directed acyclic graphs $\cdot$ Structure learning $\cdot$ Greedy search $\cdot$ PC algorithm $\cdot$ Divide-and-conquer

## 1 Introduction

Bayesian networks are compact yet powerful graphical models that efficiently encode in their graphical structures probabilistic relationships amongst a large number of variables (Neapolitan 2004). Despite their utility for probabilistic inference, the problem of recovering from data the structure of the true underlying Bayesian network that governs a domain of variables is notoriously challenging (Chickering et al. 2004). The space of Bayesian network structures grows super-exponentially with the number of variables,

[^0]
[^0]:    Editor: Pradeep Ravikumar.
    Qing Zhou
    zhou@stat.ucla.edu
    Jireh Huang
    jirehhuang@ucla.edu
    1 Department of Statistics, University of California, Los Angeles, USA

severely limiting exhaustive evaluation of all structures and motivating decades of work in developing efficient algorithms for structure learning (Robinson 1977; Spirtes et al. 2000).

Generally, Bayesian network structure learning algorithms can be classified as one of the following three classes of algorithms. Constraint-based methods strategically test conditional independence relationships between pairs of variables, first determining the existence of edges before inferring orientations (Spirtes and Glymour 1991; Meek 1995). In the score-based approach, heuristics are designed to optimize some scoring criterion that evaluates the goodness-of-fit of a proposed structure to the available data (Heckerman et al. 1995; Chickering 2002b; Russell and Norvig 2009). Finally, hybrid methods combine the two strategies, optimizing a score over a reduced space of structures restricted through a constraint-based approach (Tsamardinos et al. 2006a; Gasse et al. 2014).

The PC algorithm, named after its authors, is often considered state-of-the-art amongst constraint-based methods for Bayesian network structure learning because of its polynomial complexity for sparse graphs and attractive theoretical properties (Spirtes and Glymour 1991; Kalisch and Bühlmann 2007). Even with its favorable scaling, PC can quickly become unwieldy for large networks, motivating various developments to structure learning speed. Several works have contributed to accelerating its execution with various parallelization strategies, resulting in speed-ups ranging from up to ten times to over three orders of magnitude (Kalisch et al. 2012; Le et al. 2016; Madsen et al. 2017; Scutari 2017; Zarebavani et al. 2020). However, these improvements are primarily feats of distributed processing implementation and are limited by the availability of required hardware. Gu and Zhou (2020) proposed a hybrid framework for partitioned estimation of Bayesian networks called partition, estimation, and fusion (PEF) in the interest of distributing learning by adopting a divide-and-conquer strategy. Unfortunately, its application to the PC algorithm does not in general retain the completeness of the PC algorithm and is limited in its capacity for parallel processing. Finally, none of these contributions tackle the practical problem that the performance of constraint-based algorithms can vary substantially with certain tuning parameters, potentially requiring multiple algorithm executions.

Prominent hybrid methods leverage the efficiency of constraint-based strategies to considerably reduce the space of Bayesian network models but sacrifice the asymptotic guarantees of constraint-based edge orientation for the generally superior empirical structural accuracy of restricted greedy search (Tsamardinos et al. 2006a). This is characteristic of members of what we call the generalized sparse candidate (GSC) framework, named after the sparse candidate algorithm (Friedman et al. 1999), in which a greedy search in the DAG space is executed from an empty graph (EG) restricted to a sparse set of candidate edges obtained through a constraint-based strategy. Hybrid algorithms belonging to GSC include max-min hill-climbing (MMHC) and hybrid hybrid parents and children (H2PC), which, despite being popular and widely regarded as well-performing, are well-known to be lacking in asymptotic guarantees (Tsamardinos et al. 2006a; Gasse et al. 2014). While the adaptively restricted greedy equivalence search (ARGES) stands out as a hybrid framework with established consistency (Nandy et al. 2018), our simulations suggest that ARGES can likewise empirically benefit from the developments in our work. In particular, both GSC and ARGES initialize their respective greedy searches with an EG and, to our knowledge, no principled and well-performing initialization strategy without assuming expert knowledge has been proposed.

We propose an answer to these challenges by the development of the partitioned hybrid greedy search (pHGS) algorithm, a hybrid structure learning algorithm that can be considered the composition of three independent contributions to the computational efficiency,

theoretical guarantees, and empirical performance of Bayesian network structure learning. In particular, pHGS accomplishes the following:

1. Restricts the search space with our proposed partitioned PC (pPC) algorithm that improves on the efficiency of the PC algorithm while retaining its soundness and completeness and capacity for parallel processing;
2. Mitigates the need for parameter tuning by automatically selecting the sparsity-controlling threshold of conditional independence tests with our $p$-value adjacency thresholding (PATH) algorithm that extends the accessibility of constraint-based consistency;
3. Initializes the restricted greedy search with our hybrid greedy initialization (HGI) algorithm that elevates the asymptotic guarantees of existing hybrid algorithms such as members of the GSC framework to that of sound and complete constraint-based methods while improving empirical performance.

After reviewing relevant preliminaries in Sect. 2, the novel components of pHGS are organized in the remainder of this paper as follows. In Sect. 3, we develop the pPC algorithm which employs a partitioned estimation strategy to reduce the number of statistical tests required for the exhaustive conditional independence investigation in PC-like CPDAG learning. We additionally detail the PATH thresholding algorithm, which efficiently generates and selects from a set of CPDAG estimates with varying sparsity from a single execution of pPC (or PC) and extends the accessibility of classical asymptotic consistency results to more flexible parameter specification. We begin Sect. 4 with a brief review of score-based structure learning before developing HGI, a greedy initialization strategy which endears constraint-based edge orientation to the empirical setting with desirable theoretical guarantees.

We empirically validate pPC, PATH, and HGI in Sect. 5, first independently and then collectively in the form of pHGS through an extensive simulation study. We show that pPC generally requires significantly fewer statistical calls as compared to PC, and that PATH effectively accomplishes the task of parameter tuning from a single algorithm execution with practically negligible additional computational expense. Compared to repeated executions of PC, the combined effect of pPC and PATH consistently achieves significant computational reductions without sacrificing (and indeed often improving on) estimation accuracy. We demonstrate the effectiveness of HGI on several instantiations of the GSC hybrid framework, and validate the holistic merits of pHGS against several popular structure learning algorithms. Though the focus of our paper is on the discrete case, we include succinct comments and results for our methods on high-dimensional Gaussian data in the discussion in Sect. 6 and the Supplementary Information.

# 2 Background 

A graph $\mathcal{G}=(\mathbf{V}, \mathbf{E})$ is a structure composed of a set of nodes $\mathbf{V}=\{1, \ldots, p\}$ and a set of edges $\mathbf{E}$. For a pair of distinct nodes $i, j \in \mathbf{V}$, we encode an undirected edge between $i$ and $j$ in $\mathcal{G}$ by an unordered connected pair $i-j \in \mathbf{E}$, and a directed edge from $i$ to $j$ in $\mathcal{G}$ by an ordered pair $i \rightarrow j \in \mathbf{E}$. A directed acyclic graph (DAG) has only directed edges and is oriented such that there are no directed cycles in $\mathcal{G}$. A DAG $\mathcal{G}$ defines the structure of a Bayesian network of a joint probability distribution $P$ of variables $\mathbf{X}$ corresponding to $\mathbf{V}$ if $P$ factorizes according to the structure of $\mathcal{G}$ :

$$
P(\mathbf{X})=\prod_{i=1}^{p} P\left(X_{i} \mid \boldsymbol{\Pi}_{i}^{\mathcal{G}}\right)
$$

where $\boldsymbol{\Pi}_{i}^{\mathcal{G}}=\left\{X_{j}: j \rightarrow i \in \mathbf{E}\right\}$ denotes the parents of $X_{i}$ according to $\mathcal{G}$. In this paper, we may refer to a node $i \in \mathbf{V}$ and its corresponding variable $X_{i} \in \mathbf{X}$ interchangeably. In a causal DAG, $i \rightarrow j$ asserts that $i$ is a direct cause of $j$, whereas more generally, a DAG encodes in its structure a set of conditional independence statements between distinct variables according to the above factorization. For ease of notation, we let $\mathbf{X}_{\mathbf{k}}=\left\{X_{k} \in \mathbf{X}: k \in \mathbf{k}\right\}$ for $\mathbf{k} \subseteq \mathbf{V}$.

This paper focuses on the setting in which $P$ is a discrete probability distribution, although the presented strategies are not limited to such a domain. Each variable $X_{i}$ probabilistically attains one of $r_{i} \geq 2$ states depending on the attained states of its parents $\boldsymbol{\Pi}_{i}^{\mathcal{G}}$. The conditional probability distributions of the variables given each of their parent configurations are multinomial distributions.

Let $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$ denote that $X_{i}$ and $X_{j}$ are independent given conditioning set $\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{X} \backslash\left\{X_{i}, X_{j}\right\}$ in $P$, and $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{\mathcal{G}}$ that $X_{i}$ and $X_{j}$ are $d$-separated by $\mathbf{X}_{\mathbf{k}}$ in $\mathcal{G}$. The factorization in Eq. (1) implies that $\mathcal{G}$ and $P$ satisfy the (global) Markov condition: for disjoint sets of variables $\mathbf{A}, \mathbf{B}, \mathbf{C} \subseteq \mathbf{X}$,

$$
(\mathbf{A} \perp \mathbf{B} \mid \mathbf{C})_{\mathcal{G}} \Rightarrow(\mathbf{A} \perp \mathbf{B} \mid \mathbf{C})_{P}
$$

# 2.1 Markov equivalence 

Multiple DAGs may encode the same set of $d$-separation statements and thus redundantly entail the same conditional independence statements. Such DAGs are said to be Markov equivalent. Formally, two DAGs $\mathcal{G}$ and $\mathcal{G}^{\prime}$ are Markov equivalent if $(\mathbf{A} \perp \mathbf{B} \mid \mathbf{C})_{\mathcal{G}} \Leftrightarrow(\mathbf{A} \perp \mathbf{B} \mid \mathbf{C})_{\mathcal{G}^{\prime}}$ for all mutually disjoint subsets $\mathbf{A}, \mathbf{B}, \mathbf{C} \subseteq \mathbf{X}$. We refer to Markov equivalent DAGs as simply equivalent and belonging to the same equivalence class. Given our distributional assumptions on $P$, equivalent DAGs are indistinguishable without background information or experimental data. As our interest lies in structure learning from observational data, the objective amounts to recovering the equivalence class of the underlying DAG.

The skeleton of a graph $\mathcal{G}=(\mathbf{V}, \mathbf{E})$ is the undirected graph obtained from replacing every adjacent (that is, connected) node pair in $\mathcal{G}$ with an undirected edge. A $v$-structure is a triplet $i, j, k \in \mathbf{V}$ oriented $i \rightarrow k \leftarrow j$ in $\mathcal{G}$ with $i$ and $j$ not adjacent. Let the pattern of $\mathcal{G}$ be the partially DAG (PDAG) obtained by orienting all and only the v-structures of $\mathcal{G}$ in its skeleton, leaving all remaining edges undirected. The following theorem was adapted from Verma and Pearl (1991) to characterize equivalent DAGs.

Theorem 1 (Meek (1995)) Two DAGs are equivalent if and only if they have the same patterns.

Implied by Theorem 1 is the existence of compelled and reversible edges. An edge $i \rightarrow j$ in a DAG $\mathcal{G}$ is compelled if it exists oriented as stated in every DAG in the equivalence class of $\mathcal{G}$, whereas it is reversible if it is directed $j \rightarrow i$ in at least one DAG in the equivalence class of $\mathcal{G}$. Meek (1995) detailed a set of sound and complete rules known as Meek's rules (R1, R2, R3, and R4) that deterministically extend the pattern of a graph $\mathcal{G}$ to its completed

PDAG (CPDAG), a PDAG featuring a directed edge for every compelled edge and an undirected edge for every reversible edge (Chickering 2002a). As the unique representation of its equivalence class, the CPDAG is the structure of interest for structure learning methods in the observational setting.

# 2.2 Faithfulness 

The global Markov property, as stated in Eq. (2), defines an avenue for inference regarding the conditional independence relationships in $P$ according to information encoded in its Bayesian network structure $\mathcal{G}$. As our interest is in recovering $\mathcal{G}$ from data generated from and thus sample estimates of probability distribution $P$, we require the assumption of faithfulness to infer the structure of $\mathcal{G}$ from $P$.

Definition 1 (Faithfulness) A distribution $P$ and a DAG $\mathcal{G}$ are said to be faithful to each other if all and only the conditional independence relations true in $P$ are entailed by the $d$-separation statements in $\mathcal{G}$, i.e.

$$
(\mathbf{A} \perp \mathbf{B} \mid \mathbf{C})_{\mathcal{G}} \Leftrightarrow(\mathbf{A} \perp \mathbf{B} \mid \mathbf{C})_{P}
$$

Under faithfulness, we may say in such a case that $\mathbf{A}$ and $\mathbf{B}$ are separated by $\mathbf{C}$, regardless of whether we are referring to $d$-separation or conditional independence. If $P$ is faithful to $\mathcal{G}$, then the existence of an edge between any distinct pair of nodes $i$ and $j$ can be necessarily and sufficiently determined by the nonexistence of a separation set of variables that render $i$ and $j$ conditionally independent in $P$. In particular,

$$
i, j \in \mathbf{V} \text { are not connected in } \mathcal{G} \Leftrightarrow \exists \mathbf{k} \subseteq \mathbf{V} \backslash\{i, j\} \text { such that }\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}
$$

Throughout the development of our methodology, in what we call the population versions of procedures, we assume possession of all conditional independence information in $P$ denoted $\left\{\perp_{P}\right\}$, thus having conditional independence oracles perfectly corresponding to $d$-separation. For inferring conditional independence from finite samples of discrete data $\mathcal{D}$ in the sample counterparts, we use the popular $G^{2}$ log-likelihood ratio test of independence for empirical estimation of conditional independence in $P$ with some significance level threshold $\alpha$, denoting the $G^{2}$ test statistic for testing $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$ as $G_{i j \mid \mathbf{k}}^{2}$ (Spirtes et al. 2000). We briefly discuss the basic notation for and evaluation of the $G^{2}$ test in Appendix C, referring details and examples to (Neapolitan 2004, Sect. 10.3.1)

### 2.3 The PC algorithm

The well-known PC algorithm (Spirtes and Glymour 1991), named after its authors, is widely considered the gold standard constraint-based structure learning method. The PC algorithm first efficiently estimates a skeleton, reducing the criterion stated in Eq. (3) by leveraging sparsity. Let $\mathbf{N}_{i}^{\mathcal{G}}=\left\{X_{i} \in \mathbf{X}: i\right.$ and $j$ are connected in $\left.\mathcal{G}\right\}$ be the neighbors, or adjacencies, of node $i$ in a graph $\mathcal{G}=(\mathbf{V}, \mathbf{E})$. If $\mathcal{G}$ is a DAG, the following is evident from the Markov condition:

$$
\begin{aligned}
i, j \in \mathbf{V} \text { are not connected in } \mathcal{G} \Leftrightarrow & \exists \mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{i}^{\mathcal{G}} \backslash\left\{X_{j}\right\} \text { or } \exists \mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{j}^{\mathcal{G}} \backslash\left\{X_{i}\right\} \\
& \text { such that }\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}
\end{aligned}
$$

```
Algorithm 1 PC-skeleton \(\left(\left\lceil\perp_{P}\right\rfloor\right)\) (PC-stable; population version)
input: conditional independence information \(\left\{\perp_{P}\right\}\)
output: undirected graph \(\mathcal{G}\)
    form the complete undirected graph \(\mathcal{G}=(\mathbf{V}, \mathbf{E})\) over nodes \(\mathbf{V}=\left\{k: X_{k} \in \mathbf{X}\right\}\)
    initialize \(\mathbf{S}=\emptyset\)
    initialize \(l=0\)
    repeat
        set \(\mathcal{G}^{\prime}=\mathcal{G}\) to fix adjacencies
        for all unordered node pairs \(i-j\) adjacent in \(\mathcal{G}^{\prime}\) with \(\left|\mathbf{N}_{i}^{\mathcal{G}^{\prime}}\right|-1\) or \(\left|\mathbf{N}_{j}^{\mathcal{G}^{\prime}}\right|-1 \geq l\)
    do
            for all unique subsets \(\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{i}^{\mathcal{G}^{\prime}} \backslash\left\{X_{j}\right\}\) and \(\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{j}^{\mathcal{G}^{\prime}} \backslash\left\{X_{i}\right\}\) of size
        \(|\mathbf{k}|=l\) do
            if \(\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}\) then
                store separation set \(\mathbf{S}(i, j)=\mathbf{S}(j, i)=\mathbf{k}\)
                disconnect \(i\) and \(j\) in \(\mathcal{G}\) and continue to the next pair of nodes
                end if
                end for
            end for
        \(l=l+1\)
until there is no node \(i\) with \(\left|\mathbf{N}_{i}^{\mathcal{G}}\right|-1 \geq l\), or \(l>m\) for some user-specified \(m\)
```

For easy reference in our algorithm description, we detail an implementation of the skeleton estimation step of the PC algorithm known as PC-stable in Algorithm 1 (Colombo and Maathuis 2014). Note that as discussed, in the population versions of procedures we assume possession of conditional independence oracles. For finite-sample execution, we replace $\left\{\perp_{P}\right\}$ with data samples $\mathcal{D}$ from which conditional independence relationships are inferred using a consistent test and some threshold $\alpha$. The key difference that distinguishes the PC-stable implementation from the original PC algorithm is that in line 5, the adjacencies are fixed in $\mathcal{G}^{\prime}$ such that the considerations of adjacent node pairs within the outermost loop (lines 4-15) become order-independent and thus executable in parallel. We further discuss parallel execution of the PC algorithm in Sect. 3.1.2. Note that for every node $i, \mathbf{N}_{i}^{\mathcal{G}} \subseteq \mathbf{N}_{i}^{\mathcal{G}^{\prime}}$ for $\mathbf{N}_{i}^{\mathcal{G}^{\prime}}$ in any stage in Algorithm 1, preserving the general design of the original PC skeleton learning method by ensuring the exhaustive investigation of Eq. (4) and thus retaining its theoretical properties. Hereafter, when we discuss the PC algorithm, we refer to the PC-stable implementation.

After determining the skeleton of a DAG $\mathcal{G}$, knowledge about the conditional independence relationships between variables (namely, the accrued separation sets $\mathbf{S}$ ) can be used to detect the existence of v-structures and orient the skeleton to the pattern of $\mathcal{G}$. Recovery of the CPDAG of $\mathcal{G}$ can then be achieved by repeated application of Meek's rules (Meek 1995). This process, which we refer to as skel-to-cpdag (Algorithm 6 in Appendix B), is guaranteed to orient the skeleton of a DAG $\mathcal{G}$ to its CPDAG given accurate conditional independence information entailed by $\mathcal{G}$. For details regarding constraint-based edge orientation, see Appendix B.

The complete PC(-stable) algorithm consists of skeleton estimation according to Algorithm 1 followed by edge orientation according to Algorithm 6, and is well-known to be sound and complete for CPDAG estimation (Kalisch and Bühlmann 2007; Colombo and Maathuis 2014).

# 3 The pPC and PATH algorithms 

In constraint-based methods, the computational expense of edge orientation has been noted to be generally insignificant compared to that of skeleton estimation (Chickering 2002a; Madsen et al. 2017). As such, we develop the pPC algorithm to reduce the computational expense of skeleton estimation by imposing a partitioned ordering to the conditional independence tests. Similarly, we propose the PATH algorithm that effectively accomplishes the task of parameter tuning by efficiently generating a solution path of estimates from a single execution of pPC or PC.

### 3.1 The partitioned PC algorithm

The pPC algorithm improves on the already desirable efficiency of the PC algorithm while retaining its attractive theoretical properties and empirical structure learning accuracy. The structure follows similarly to the PEF strategy applied to the PC algorithm in Gu and Zhou (2020). We develop improvements and computational exploits to further increase performance, formulate pPC to retain soundness and completeness, and propose adaptations to address the challenges of learning the structure of discrete Bayesian networks.

The intuition motivating a partitioned strategy is that any structure learning algorithm that scales worse than linearly with $p$ will be able to estimate $\kappa>1$ subgraphs for node clusters that partition the $p$ nodes faster than a single graph on all nodes. If the $p$ nodes can be reliably partitioned such that the connectivity between clusters is weak relative to within clusters, then we can expect that there will not be many false positive edges (as a result of causal insufficiency) within subgraphs. Consequently, the adjacencies are expected to be relatively well-estimated, providing a selective candidate set of neighbors to screen the edges between subgraphs. Coupled with the assumed weak connectivity between clusters, the process of determining the existence of edges amongst clusters is expected to be efficient.

The pPC algorithm estimation process proceeds as follows. We partition the $p$ nodes into $\kappa$ clusters using a version of the modified hierarchical clustering algorithm proposed in Gu and Zhou (2020) applied with a normalized discrete distance metric, additionally blacklisting marginally independent node pairs. We then apply the PC algorithm to estimate edges within clusters, and filter and refine edges between nodes in different clusters. Finally, we achieve completeness by applying a reduced PC algorithm before orienting the edges.

### 3.1.1 Clustering

As previously motivated, the task of obtaining an effective partition of the nodes is crucial for the success of the skeleton learning. A partition with many clusters $\kappa$ is desirable for greatest computational benefit in subgraph estimation, but each cluster must be substantive so as to minimally violate causal sufficiency. To accomplish this, the distances between nodes are measured by a normalized mutual information distance metric, and the target number of clusters and initial clusters are chosen adaptively.

Mutual information, denoted $I\left(X_{i}, X_{j}\right)$, serves as a similarity measure between discrete random variables $X_{i}$ and $X_{j}$ and may be interpreted as the Kullback-Leibler divergence between the joint probability distribution and the product of their marginals. We obtain a distance measure by inverting the pairwise mutual information after normalizing using the joint entropy $H\left(X_{i}, X_{j}\right)$. In particular, we formulate the distance between each pair of variables $X_{i}$ and $X_{j}$ as

$$
d_{i j}=1-\frac{I\left(X_{i}, X_{j}\right)}{H\left(X_{i}, X_{j}\right)} \in[0,1]
$$

The proposed distance $d_{i j}$ is a metric in the strict sense as shown by Kraskov et al. (2005), meaning it is symmetric, non-negative, bounded, and satisfies the triangle inequality. In practice, we compute the empirical quantities of the mutual information and joint entropy ( $\hat{I}$ and $\hat{H}$, respectively) between discrete variables (see Appendix C).

Given our distance matrix $D=\left(d_{i j}\right)_{p \times p}$, we apply Algorithm 1 in Gu and Zhou (2020) with average linkage to determine a cut $l$ for the agglomerative hierarchical clustering of the $p$ nodes. Succinctly described, we choose the highest cut such that the resulting cluster consists of the greatest number of large clusters, defined as node clusters of at least size $0.05 p$ according to a loose suggestion by Hartigan (1981). We then merge clusters of size less than $0.05 p$ with other small clusters or into large clusters sequentially, ordered by average linkage, until every cluster is a large cluster. For further details regarding the algorithm, we refer to the original paper. The clustering step partitions the $p$ nodes into $\kappa$ clusters, returning the cluster labels $\mathbf{c}=\left\{c_{1}, \ldots, c_{p}\right\}$, with $c_{i} \in\{1, \ldots, \kappa\}$ denoting the cluster label of node $i$.

While the pairwise computation of both the mutual information and the joint entropy may seem expensive for the purpose of obtaining a partition, we take advantage of two exploits to accomplish this economically. Observing that $I\left(X_{i}, X_{j}\right)=H\left(X_{i}\right)+H\left(X_{j}\right)-H\left(X_{i}, X_{j}\right)$, we need only compute the marginal entropies $H\left(X_{i}\right)=I\left(X_{i}, X_{i}\right)$ to derive the joint entropies from the pairwise mutual information, a reduction from $p(p-1)$ computations to $p(p+1) / 2$. Further noting that the discrete unconditional $G^{2}$ test statistic for investigating the marginal independence between $X_{i}$ and $X_{j}$ is computed as $G_{i j}^{2}=2 n \cdot \hat{I}\left(X_{i}, X_{j}\right)$ [see Eq. (23) in Appendix C], an initial edge screening can easily be obtained through the evaluation

$$
\begin{aligned}
\operatorname{Pr}\left(\chi_{f}^{2}>2 n \cdot \hat{I}\left(X_{i}, X_{j}\right)\right)>\alpha & \Rightarrow\left(X_{i} \perp X_{j}\right)_{P} \\
& \Rightarrow \text { blacklist the edge } i-j
\end{aligned}
$$

where $f$ is the degrees of freedom corresponding to the test of independence between $i$ and $j$ conditioned on $\mathbf{k}=\emptyset$ (see Appendix C). This effectively accomplishes the empty conditioning set $(l=0)$ testing step of the PC algorithm by separating all marginally independent pairs of variables (Algorithm 2 line 2).

Note that for continuous data, we recommend using correlation as a similarity measure, which Gu and Zhou (2020) found to lead to reasonable partitions of nodes for divide-and-conquer strategies for learning Gaussian Bayesian networks. This design may also take advantage of Eq. (6) by testing for zero correlation. After the clustering step, the pPC algorithm and other methods developed in this paper can be generalized to continuous cases with straightforward substitutions of conditional independence tests and score functions.

# 3.1.2 Partitioned skeleton estimation 

We now apply the PC algorithm skeleton learning phase to estimate $\kappa$ disconnected undirected subgraphs according to the partition obtained in the clustering step. Practically, independently applying the PC algorithm to each node cluster benefits from at most $\kappa$ processors if distributed as such for parallel processing. Furthermore, the speed-up is limited

by the longest estimation runtime, usually corresponding to the largest node cluster. In contrast, the design of the PC-stable implementation (Algorithm 1) by Colombo and Maathuis (2014) allows for parallel investigation of adjacent node pairs in lines 6-13, provided that updating the graph estimate is deferred to a synchronization step between iterations of $l$. Several contributions and implementations exist for this approach, referred to as vertical parallelization, which addresses the case where the number of variables $p$ is large (Kalisch et al. 2012; Le et al. 2016; Scutari 2017; Zarebavani et al. 2020). Alternatively, a horizontal parallelization approach parallelizes across data observations and is preferred when the sample size $n$ is large (Madsen et al. 2017). In these parallelization paradigms, due to the large number of distributed tasks, the number of utilizable computing processors is not practically limited, and the computational load is reasonably expected to be evenly distributed. To take advantage of these developments in parallelizing the PC algorithm, we estimate subgraphs within the node clusters by executing Algorithm 1 with the following modifications: (i) form the initial complete undirected graph by only connecting nodes within clusters, (ii) delete edges according to Eq. (6), and (iii) begin investigating candidate conditioning sets of size $l=1$. The result is an undirected graph $\mathcal{G}$ on $\mathbf{V}$ consisting of $\kappa$ disconnected subgraphs.

At this stage, given a good partition, we expect the node adjacencies to be relatively well-estimated, with the exception of extraneous edge connections within clusters due to the violation of causal sufficiency and missing edge connections between clusters that are disconnected by the partition. Recall from Sect. 3.1.1 that many pairs, including those between clusters, were removed from consideration via the initial marginal independence filtering according to Eq. (6). We further refine the pairs between clusters through a twostep screening process, our strategy being similar to Algorithm 2 designed by Gu and Zhou (2020), with modifications made to accommodate discrete structure learning. Note that this is where we anticipate to derive the most computational advantage over the PC algorithm. Assuming a block structure was successfully detected, we aim to circumvent the lower order conditional independence tests in our investigation of Eq. (4) by separating as many between cluster pairs as possible with the currently estimated adjacencies.

The proposed between cluster screening process is summarized in the following operations to the currently estimated skeleton $\mathcal{G}=(\mathbf{V}, \mathbf{E})$ :

$$
\begin{gathered}
\mathbf{E} \leftarrow \mathbf{E} \cup\left\{i-j: c_{i} \neq c_{j},\left(X_{i} \nmid X_{j}\right)_{P}, \text { and }\left(X_{i} \nmid X_{j} \mid \mathbf{N}_{i}^{\mathcal{G}} \cup \mathbf{N}_{j}^{\mathcal{G}}\right)_{P}\right\} \\
\mathbf{E} \leftarrow \mathbf{E} \backslash\left\{i-j \in \mathbf{E}: c_{i} \neq c_{j}, \text { and }\left(X_{i} \perp X_{j} \mid \mathbf{N}_{i}^{\mathcal{G}} \backslash\left\{X_{j}\right\}\right)_{P}\right. \\
\text { or }\left(X_{i} \perp X_{j} \mid \mathbf{N}_{j}^{\mathcal{G}} \backslash\left\{X_{i}\right\}\right)_{P}\right\}
\end{gathered}
$$

where $c_{i}$ is the cluster label of $X_{i}$. The first screen in Eq. (7) constructively connects the between cluster edges that are dependent marginally, as assessed according to Eq. (6), as well as conditioned on the union of the neighbor sets. With the addition of edges between clusters, the second screen in Eq. (8) disconnects pairs that are separated by the newly updated adjacencies. As in Algorithm 1, we fix adjacencies to retain the capacity for parallel investigation of the considered node pairs. Note that every between-cluster edge that is present in the underlying DAG will be connected by Eq. (7), and Eq. (8) can only prune false positives. Thus, after this step every node pair will have been considered and, in the population setting, every truly connected edge in the underlying DAG will be connected in $\mathcal{G}$.

```
Algorithm \(2 \mathrm{pPC}\left(\left\{\mathbb{IL}_{P}\right\}\right)\) (population version)
input: conditional independence information \(\left\{\mathbb{IL}_{P}\right\}\)
output: CPDAG estimate \(\mathcal{G}\)
    partitioning
    assign cluster labels c by partitioning all nodes into \(\kappa\) clusters as in Sect. 3.1.1
    within cluster edge estimation
    execute \(\mathcal{G} \leftarrow\) PC-skeleton \(\left(\left\{\mathbb{L}_{P}\right\}\right)\) (Algorithm 1), with the following modifica-
    tions:
        line 1: form undirected graph by only connecting node pairs \(i, j \in \mathbf{V}\) with
        \(c_{i}=c_{j}\)
        line 3: delete marginally independent pairs from \(\mathcal{G}\) according to Eq. (6) and
        initialize \(l=1\)
    between cluster edge screening
    initialize \(\mathcal{G}^{\prime}=\mathcal{G}\) to fix adjacencies
    for all unordered node pairs \(i, j\) such that \(c_{i} \neq c_{j}\) and \(\left(X_{i} \nsubseteq X_{j}\right)_{P}\) do
        if \(\left(X_{i} \nsubseteq X_{j} \mid \mathbf{N}_{i}^{\mathcal{G}^{\prime}} \cup \mathbf{N}_{j}^{\mathcal{G}^{\prime}}\right)_{P}\) then
            connect \(i\) and \(j\) in \(\mathcal{G}\)
        else
            store separation set in \(\mathbf{S}(i, j)=\mathbf{S}(j, i)\)
        end if
    end for
    set \(\mathcal{G}^{\prime}=\mathcal{G}\) to update fixed adjacencies
    for all unordered node pairs \(i, j\) adjacent in \(\mathcal{G}\) with \(c_{i} \neq c_{j}\) do
        if \(\left(X_{i} \mathbb{IL}_{j} \mid \mathbf{N}_{i}^{\mathcal{G}^{\prime}} \backslash\left\{X_{j}\right\}\right)_{P}\) or \(\left(X_{i} \mathbb{IL}_{j} \mid \mathbf{N}_{j}^{\mathcal{G}^{\prime}} \backslash\left\{X_{i}\right\}\right)_{P}\) then
            store separation set in \(\mathbf{S}(i, j)=\mathbf{S}(j, i)\)
            disconnect \(i\) and \(j\) in \(\mathcal{G}\)
        end if
    end for
    complete edge estimation
    execute \(\mathcal{G} \leftarrow\) PC-skeleton \(\left(\left\{\mathbb{L}_{P}\right\}\right)\) (Algorithm 1), continuing from \(\mathcal{G}\) and
    restricting to Eq. (9) with the following replacements:
        line 1: initialize undirected graph with current estimate \(\mathcal{G}\)
        line 2: omit this line
        line 3: initialize \(l=1\)
        line 7: for all unique subsets \(\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{i}^{\mathcal{G}^{\prime}} \backslash\left\{X_{j}\right\}\) and \(\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{j}^{\mathcal{G}^{\prime}} \backslash\left\{X_{i}\right\}\) satisfying
        \(|\mathbf{k}|=l\) and criteria Eq. (9) do
    edge orientation
    execute \(\mathcal{G} \leftarrow \operatorname{skel-to-cpdag}(\mathcal{G}, \mathbf{S})\) (Algorithm 6) to orient \(\mathcal{G}\)
```

Remark 1 The formulation of the discrete $G^{2}$ tests of independence require enumerating and counting across all conditioning variable configurations. An unavoidable consequence is that the computational complexity and memory requirement increase dramatically with increasing conditioning variables, especially when they have a large number of discrete levels. As such, it is of practical interest to restrict the size of conditioning sets to some user-specified $m>0$. Thus, for the evaluations in Eqs. (7) and (8) (Algorithm 2 lines 5 and 13), if for example $\left|\mathbf{N}_{i}^{\mathcal{G}} \cup \mathbf{N}_{j}^{\mathcal{G}}\right|>m$, we instead investigate the unique sets $\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{i}^{\mathcal{G}} \cup \mathbf{N}_{j}^{\mathcal{G}}$ such that $|\mathbf{k}|=m$. Furthermore, in the case that the considered neighborhood is large due

![img-0.jpeg](img-0.jpeg)

Fig. 1 Example of various stages of pPC (Algorithm 2). Node shading denotes clusters, lines represent estimated edges, with dashed lines representing false positive edges. The estimated graph after line 2 and after line 10 are shown in $\mathbf{a}$ and $\mathbf{b}$, respectively. The final output is equivalent to the CPDAG of the underlying DAG $\mathcal{G}^{*}$ in $\mathbf{c}$
to an unfavorable partition, the investigated conditioning sets may be limited to those contained within only a subset of the neighborhood, provided the subsequent step is adjusted accordingly [(b) in Eq. (9)].

However, it is important to note that the constraint-based criterion for edge existence expressed in Eq. (4) has not yet been fully investigated for all node pairs. The tests for edges within clusters only considered conditioning sets consisting of nodes within the same clusters, and tests for edges between clusters were limited to the empty set, $\mathbf{N}_{i}^{\mathcal{G}} \cup \mathbf{N}_{j}^{\mathcal{G}}$, $\mathbf{N}_{i}^{\mathcal{G}} \backslash\left\{X_{j}\right\}$, and $\mathbf{N}_{j}^{\mathcal{G}} \backslash\left\{X_{i}\right\}$. In particular, for each remaining adjacent node pair $i-j \in \mathbf{E}$, the possible separation sets that have not been evaluated are limited to either of the following cases, if any:
(a) $c_{i}=c_{j}$ (within clusters), sets $\mathbf{k}$ where $\exists k \in \mathbf{k}$ such that $c_{k} \neq c_{i}$;
(b) $c_{i} \neq c_{j}$ (between clusters), sets $\mathbf{k} \neq \emptyset$ not defined in Eq. (7) or Eq. (8).

The most straightforward continuation to achieve completeness in our partitioned skeleton learning process would be to exhaustively evaluate the dependence of the remaining connected node pairs in $\mathcal{G}$ conditioned on the remaining conditioning sets. We accomplish this by restarting the PC algorithm on the current skeleton, evaluating independence conditioned on sets restricted to criteria Eq. (9), before finally orienting the resulting skeleton to a CPDAG with skel-to-cpdag (Algorithm 6) to complete structure learning.

The resulting pPC algorithm is detailed in Algorithm 2, and an example of its execution is illustrated in Fig. 1, which provides intuition for its theoretical properties expressed in Theorem 2. The pPC algorithm first estimates the edges within the clusters to obtain $\kappa=3$ disconnected subgraphs (Fig. 1a). False positives may be present in these subgraphs in the case that conditioning sets that separate truly disconnected variables contain variables

belonging to different clusters, such as in the case of $X_{6}-X_{9}$ for which the common parent $X_{5}$ is in a different cluster. Similarly, two false positive edges are constructively connected along with all true positives according to Eq. (7) (Fig. 1b), but these are quickly pruned by the second screening of edges between clusters with Eq. (8) (not shown). $X_{6}-X_{9}$ remains to be separated, requiring $\left(X_{6} \perp X_{9} \mid X_{5}\right)_{P}$ to be investigated in line 18 to recover the underlying skeleton before orientation to the true CPDAG $\mathcal{G}^{*}$ in line 19 (Fig. 1c).

The pPC algorithm (Algorithm 2) is sound and complete, formalized in Theorem 2, which we prove in Appendix A.

Theorem 2 Suppose that probability distribution $P$ and $D A G \mathcal{G}^{*}$ are faithful to each other. Then given conditional independence oracles, the output of the pPC algorithm (Algorithm 2) is the CPDAG that represents the equivalence class of $\mathcal{G}^{*}$.

Its implication is the asymptotic consistency of pPC for fixed $p$ as $n \rightarrow \infty$, given a consistent conditional independence test such as the $G^{2}$ test (Cressie and Read 1989). Note that while the computational savings may depend heavily on the quality of the partitioning, Theorem 2 holds regardless of the obtained clusters.

# 3.2 p-value adjacency thresholding 

Despite the attractive theoretical properties of algorithms such as pPC and PC, it is wellknown that in practice, constraint-based algorithms suffer from the multiple testing problem, a challenge exacerbated when $p$ is large (Spirtes 2010). The effect of individual errors can compound throughout the conditional independence testing process, leading to erroneous inferences regarding both the existence and orientation of edges (Koller and Friedman 2009; Spirtes 2010). In addition to deteriorated quality of structures estimated, mistakes in conditional independence inferences can result in invalid PDAG estimates that do not admit a consistent extension (see Remark 2). In practical applications, the choice of conditional independence test threshold $\alpha$ can significantly control the sparsity and quality of the resulting estimate. To the best of our knowledge, proposed theoretical thresholds depend on unknown quantities and are not practically informative, such as in Kalisch and Bühlmann (2007). Empirically, the optimal choice of $\alpha$ varies depending on factors such as the sample size and the structure and parameters of the underlying Bayesian network, and no universally well-performing value is known.

We propose the PATH algorithm to generate and select from a CPDAG solution path across various values of $\alpha$ from a single execution of the pPC algorithm, or indeed from any constraint-based structure learning algorithm that is able to obtain the following. Define the maximum $p$-values $\Phi=\left(\Phi_{i j}\right)$ such that $\Phi_{i j}$ is the maximum $p$-value obtained by the conditional independence test between $i$ and $j$ across all conditioning sets $\mathbf{k} \in \mathcal{K}_{i j}$ visited in the algorithm, as well as the corresponding separation sets, thus extending the definition of $\mathbf{S}$. That is, for all distinct node pairs $i, j$,

$$
\begin{aligned}
& \Phi_{i j}=\Phi_{j i}:=\max _{\mathbf{k} \in \mathcal{K}_{i j}} \operatorname{Pr}\left(\chi_{f}^{2}>G_{i j \mid \mathbf{k}}^{2}\right) \\
& \mathbf{S}(i, j)=\mathbf{S}(j, i):=\operatorname{argmax}_{\mathbf{k} \in \mathcal{K}_{i j}} \operatorname{Pr}\left(\chi_{f}^{2}>G_{i j \mid \mathbf{k}}^{2}\right)
\end{aligned}
$$

For a connected node pair $i-j, \mathbf{S}(i, j)$ may be considered the conditioning set closest to separating $i$ and $j$, and $\Phi_{i j}$ measures how close.

The process itself is straightforward: for a sequence of significance levels $\left\{\alpha^{(t)}\right\}$, we obtain updated PDAG estimates $\mathcal{G}^{(t)}$ by thresholding the maximum achieved $p$-values $\Phi$ to obtain skeleton estimates with edge sets $\mathbf{E}^{(t)}=\left\{i-j: \Phi_{i j} \leq \alpha^{(t)}\right\}$ and then orienting them to CPDAGs according skel-to-cpdag (Algorithm 6) with the corresponding separation information $\mathbf{S}^{(t)}=\left\{\mathbf{S}(i, j): \Phi_{i j}>\alpha^{(t)}\right\}$. The quality of the estimates are then evaluated by a scoring criterion and the highest-scoring network is returned. In what follows, we develop the choice of the threshold values and present the strategy for estimate generation and selection.

We begin with a graph estimate obtained by executing the pPC algorithm with some maximal threshold value $\alpha$. The goal is to start with the densest graph so that the elements of $\Phi$ and $\mathbf{S}$ in Eq. (10) are maximized over a larger number of visited conditioning sets $|\mathcal{K}|$. We generate a sequence of $\tau$ values decreasing from $\alpha^{(1)}:=\alpha$ to some minimum threshold value $\alpha^{(\tau)}$. This sequence may be incremented according to some linear or log-linear scale, but we choose to achieve maximal difference in sparsity amongst estimates by utilizing the information in $\Phi$. Given each $\alpha^{(t)}$ corresponding to estimate $\mathcal{G}^{(t)}=\left(\mathbf{V}, \mathbf{E}^{(t)}\right)$, we choose $\alpha^{(t+1)}$ such that

$$
\left|\mathbf{E}^{(t)}\right|-\left|\mathbf{E}^{(t+1)}\right| \approx \frac{\left|\mathbf{E}^{(1)}\right|-\left|\mathbf{E}^{(\tau)}\right|}{\tau-1}
$$

Noting that $\left|\mathbf{E}^{(t)}\right|=\sum_{i<j} \mathbb{1}\left\{\Phi_{i j} \leq \alpha^{(t)}\right\}$ for indicator function $\mathbb{1}\{\cdot\}$, it is easy to see that the sequence $\alpha^{(1)}, \ldots, \alpha^{(\tau)}$ can be straightforwardly obtained using the order statistics of the elements of $\Phi$.

Once a solution path of CPDAG estimates $\left\{\mathcal{G}^{(t)}: t \in\{1, \ldots, \tau\}\right\}$ is obtained, we select the highest quality estimate by means of score-based selection. The Bayesian information criterion (BIC) is a penalized log-likelihood score derived from the asymptotic behavior of Bayesian network models, with established consistency (Schwarz 1978). The formulation of the BIC score makes clear its score decomposability [see Eq. (24) in Appendix C]; that is, the score $\phi(\mathcal{G}, \mathcal{D})$ can be computed as the sum of the scores of the individual variables with respect to their parents in $\mathcal{G}: \phi(\mathcal{G}, \mathcal{D})=\sum_{i=1}^{r} \phi\left(X_{i}, \boldsymbol{\Pi}_{i}^{\mathcal{G}}\right)$. The BIC score is additionally score equivalent, evaluating all Markov equivalent DAGs as of identical quality, with a higher value indicating a better fit to the data.

Due to score equivalence, it is sufficient to evaluate each CPDAG $\mathcal{G}^{(t)}$ with any arbitrary DAG $\widetilde{\mathcal{G}}^{(t)}$ in its equivalence class, called a consistent extension of $\mathcal{G}^{(t)}$. Dor and Tarsi (1992) proposed a simple algorithm, which we refer to as pdag-to-dag, that obtains such an extension by orienting the undirected (reversible) edges in $\mathcal{G}^{(t)}$ without inducing directed cycles or introducing new v-structures, and is guaranteed to succeed if a consistent extension exists (further discussed in Sect. 4.2). After obtaining these DAG extensions, in practice, score decomposability can be leveraged to avoid scoring $p$ nodes for $\tau$ estimates by setting $\Delta^{(1)}=0$ and computing the score differences between estimates $\Delta^{(t)}=\phi\left(\widetilde{\mathcal{G}}^{(t)}, \mathcal{D}\right)-\phi\left(\widetilde{\mathcal{G}}^{(t-1)}, \mathcal{D}\right)$ for $t=2, \ldots, \tau$, caching computed node score to avoid redundant computations. The best solution can then be straightforwardly obtained according to

$$
t^{*}=\operatorname{argmax}_{t \in\{1, \ldots, \tau\}} \phi\left(\mathcal{G}^{(t)}, \mathcal{D}\right)=\operatorname{argmax}_{t \in\{1, \ldots, \tau\}} \sum_{r=1}^{t} \Delta^{(r)}
$$

We detail the PATH solution path strategy in Algorithm 3.

```
Algorithm \(3 \mathrm{PATH}\left(\Phi, \mathbf{S}, \mathcal{D}, \tau, \alpha^{(\tau)}\right)\) (sample version)
input: maximum \(p\)-values \(\Phi\), separation sets \(\mathbf{S}\), data \(\mathcal{D}\), number of estimates \(\tau\),
        minimum threshold \(\alpha^{(\tau)}\)
    output: CPDAG \(\mathcal{G}\left(t^{*}\right)\), CPDAG solution path \(\left\{\mathcal{G}^{(t)}: t \in\{1, \ldots, \tau\}\right\}\)
    : generate a decreasing sequence of \(\tau\) values \(\left\{\alpha^{(t)}\right\}\) from \(\alpha^{(1)}:=\max _{i, j} \Phi_{i j}\) to \(\alpha^{(\tau)}\)
        by Eq. (11)
        for \(t=1,2, \ldots, \tau\) do
            obtain skeleton \(\mathcal{G}^{(t)}=\left(\mathbf{V}, \mathbf{E}^{(t)}\right)\) by thresholding: \(\mathbf{E}^{(t)}=\left\{i-j: \Phi_{i j} \leq \alpha^{(t)}\right\}\)
            obtain separation sets \(\mathbf{S}^{(t)}=\left\{\mathbf{S}(i, j): \Phi_{i j}>\alpha^{(t)}\right\}\)
            execute \(\mathcal{G}^{(t)} \leftarrow\) skel-to-cpdag \(\left(\mathcal{G}^{(t)}, \mathbf{S}^{(t)}\right)\) (Algorithm 6 in Appendix B)
            obtain DAG extension \(\tilde{\mathcal{G}}^{(t)} \leftarrow\) pdag-to-dag \(\left(\mathcal{G}^{(t)}\right)\) (Dor \& Tarsi, 1992)
            if \(t=1\) then
                \(\Delta^{(t)}=0\)
            else
                compute score difference \(\Delta^{(t)}=\phi\left(\tilde{\mathcal{G}}^{(t)}, \mathcal{D}\right)-\phi\left(\tilde{\mathcal{G}}^{(t-1)}, \mathcal{D}\right)\)
            end if
    end for
    select the best estimate \(t^{*}=\operatorname{argmax}_{t \in\{1, \ldots, \tau\}} \sum_{r=1}^{t} \Delta^{(\tau)}\)
    return \(\mathcal{G}\left(t^{*}\right)\) and \(\left\{\mathcal{G}^{(t)}: t \in\{1, \ldots, \tau\}\right\}\)
```

Remark 2 While pdag-to-dag is guaranteed to extend a PDAG $\mathcal{G}$ to a DAG if any consistent extension exists, in the presence of finite-sample error, Algorithm 6 may obtain a PDAG estimate $\mathcal{G}$ for which no such extension exists. In such a case, we say that $\mathcal{G}$ does not admit a consistent extension, and refer to it as an invalid CPDAG. Such PDAGs contain undirected edges that cannot be oriented without inducing cycles or constructing additional v-structures, and do not encode any probabilistic model of $P$. To account for these, we restrict the candidate graphs considered in line 13 to valid CPDAGs. In the case that no valid CPDAG is obtained, we obtain semi-arbitrary DAG extensions $\tilde{\mathcal{G}}^{0}$ by first applying the algorithm by Dor and Tarsi (1992) and randomly directing as many remaining undirected edges as possible without introducing any cycles, finally removing edges that cannot be oriented. The resulting DAGs are used to score the PDAGs, and the original PDAGs are returned in the output as these structures are nonetheless interpretable even as incomplete dependency structures.

The computational expense of executing Algorithm 3 can reasonably be expected to be insignificant compared to any constraint-based algorithm to which it is attached, supported by our empirical results in Sect. 5.2. Our exploitation of score decomposability reduces the order of score computations far below the worst case of $O(\tau p)$, which is already much more efficient than any favorable order of conditional independence tests such as polynomial with $p$. As for the $\tau$ executions of skel-to-cpdag and pdag-to-dag, Chickering (2002a) found the computational cost of applying the edge orientation heuristics to be insignificant, as did Madsen et al. (2017) for skel-to-cpdag in comparison to skeleton learning. As such, the computational cost for score-based selection from the solution path can be expected to be essentially inconsequential, an assertion further validated in our experiments.

In the large-sample limit, the correctness of Eq. (4) and skel-to-cpdag implies the asymptotic consistency of PC and pPC under certain conditions without any solution path (see Lemma 2 in Appendix A). This property can be achieved with a consistent conditional independence test by controlling type I error with $\alpha_{n} \rightarrow 0$ as $n \rightarrow \infty$, thus rendering the test Chernoff-consistent (Cressie and Read 1989; Shao 2003, Definition 2.13). As $\alpha_{n}$ is not practically informative due to its implicit dependence on $n$, Algorithm 3 contributes an element of accessibility to this asymptotic result in the form of the following theorem, a proof for which can be found in Appendix A.

Theorem 3 Suppose the distribution $P$ is fixed and faithful to a DAG with CPDAG $\mathcal{G}^{*}, \mathcal{D}$ is data containing $n$ i.i.d. samples from $P$, and $\phi$ is a consistent score. Let $\Phi_{n}=\left(\Phi_{n, i j}\right)$ and $\mathbf{S}_{n}$ be the maximum $p$-values and corresponding separation sets recorded for any exhaustive investigation of Eq. (4), executed with a consistent test applied with threshold $\alpha_{n}$. Let $\hat{\mathcal{G}}_{n}^{(\tau)}\left(\alpha_{n}\right)$ be the selected estimate of Algorithm 3 with parameters $\tau=1+\sum_{i<j} \mathbb{1}\left\{\Phi_{n, i j} \leq \alpha_{n}\right\}$ and $\alpha^{(\tau)}=0$ applied to $\Phi_{n}$ and $\mathbf{S}_{n}$. Then there exists $a_{n} \rightarrow 0$ as $n \rightarrow \infty$ such that if $\alpha_{n} \geq a_{n}$ when $n$ is large,

$$
\lim _{n \rightarrow \infty} \operatorname{Pr}\left[\hat{\mathcal{G}}_{n}^{(\tau)}\left(\alpha_{n}\right)=\mathcal{G}^{*}\right]=1
$$

In particular, Eq. (12) holds if $\alpha_{n}$ is fixed to some constant $\alpha \in(0,1)$ for all $n$.
In the finite-sample setting, the thresholded estimate $\mathcal{G}^{(t)}$ corresponding to $\alpha^{(t)}<\alpha^{(1)}$ typically does not correspond exactly to the estimate obtained by directly executing PC or pPC with significance level $\alpha^{(t)}$. Adjacencies that would be disconnected in the earlier stages of the learning process with threshold $\alpha^{(t)}$ may survive to the later stages with a more lenient threshold $\alpha^{(1)}$. The enlarged neighborhoods may persist as additional (potentially false positive) connections in the output structure, but may also cause more conditioning sets to be considered and thus lead to the deletion of edges that would not have been deleted in the execution with $\alpha^{(t)}$. Thus, while the estimated structure from executing with $\alpha^{(1)}$ may reasonably be expected to be denser than that of $\alpha^{(t)}$, it may not be a supergraph of the latter, and the $p$-values for each node pair [Eq. (10)] are optimized over different conditioning sets, so the thresholded estimate with PATH is likely to differ. Nonetheless, our empirical results demonstrate the potential of the solution path generated by thresholding, showing that PATH applied to pPC and PC is able to produce estimates of competitive quality to the best of those obtained by multiple executions with various $\alpha$.

To the best of our knowledge, there is currently no easy way to choose the optimal threshold $\alpha_{n}$ for PC (or pPC), and thus repeated executions are often needed for parameter tuning. The application of PATH pragmatically allows for a single execution of PC or pPC with fixed threshold $\alpha$ while returning estimates with both theoretical guarantees (Theorem 3) and empirical well-performance (Sect. 5.2).

# 4 Consistent hybrid structure learning 

Despite the accessibility provided by PATH (Algorithm 3), the asymptotic guarantees of constraint-based learning strategies do not necessarily translate to well-performance in practice. For this reason, based on their experiments with which our simulation results are in agreement, Tsamardinos et al. (2006a) preferred greedy search in the DAG space over

constraint-based orientation in their development of their algorithm, even though the former is lacking in comparable theoretical guarantees.

In the interest of elevating the class of algorithms that share such an compromise, we develop the HGI strategy to preserve the asymptotic guarantees of sound and complete constraint-based structure learning while improving on the empirical well-performance of the current standard hybrid framework. We motivate and develop HGI in this section, first reviewing relevant standard score-based and hybrid structure learning before describing the HGI strategy in detail.

# 4.1 Score-based and hybrid structure learning 

Chickering (2002a) distills score-based Bayesian network learning into two general problems: the evaluation problem and the identification problem. In this section, we begin by introducing the relevant tenets of score-based structure learning under these categories.

We have briefly interacted with the evaluation problem in our discussion of the BIC score in Sect. 3.2, which more broadly involves the development of scoring criteria to evaluate the goodness-of-fit of a Bayesian network to data. The existence of equivalence classes (Sect. 2.1) motivates the design of metrics that evaluate all structures within an equivalence class as of equal quality, satisfying the score equivalence property. The BIC score that we utilize satisfies this property, and is equivalent to the (negative) minimum description length (MDL) in Rissanen (1978). Other scores that are score equivalent include loglikelihood, Akaike's information criterion (AIC), and Bayesian Dirichlet equivalence score (BDeu) (Akaike 1974; Buntine 1991; Heckerman et al. 1995). Notwithstanding, prominent scores that are not score equivalent exist as well, such as the K2 score (Cooper and Herskovits 1991) and, more recently, $\ell_{1}$-regularized likelihood scores (Fu and Zhou 2013; Gu et al. 2019). In their investigation, Liu et al. (2012) found BIC to have favorable model selection performance relative to a number of other scores.

The consistency of the BIC score guarantees that in the large-sample limit, $\mathcal{G}^{*}=\operatorname{argmax}_{\mathcal{G}} \phi(\mathcal{G}, \mathcal{D})$ is in the equivalence class of the underlying DAG. BIC additionally retains the property of local consistency (Chickering 2002b), meaning for any DAG $\mathcal{G}$ and another DAG $\mathcal{G}^{\prime}$ resulting from adding the edge $X_{i} \rightarrow X_{j}$ to $\mathcal{G}$, the following two properties hold asymptotically:

$$
\begin{gathered}
\left(X_{j} \perp X_{i} \mid \boldsymbol{\Pi}_{j}^{\mathcal{G}}\right)_{P} \Rightarrow \phi\left(\mathbf{X} \mid \mathcal{G}^{\prime}, \mathcal{D}\right)>\phi(\mathbf{X} \mid \mathcal{G}, \mathcal{D}), \text { and } \\
\left(X_{j} \perp X_{i} \mid \boldsymbol{\Pi}_{j}^{\mathcal{G}}\right)_{P} \Rightarrow \phi\left(\mathbf{X} \mid \mathcal{G}^{\prime}, \mathcal{D}\right)<\phi(\mathbf{X} \mid \mathcal{G}, \mathcal{D})
\end{gathered}
$$

We have discussed the BIC score as having desirable qualities for evaluating Bayesian network structures, being decomposable, score equivalent, consistent, locally consistent, and empirically well-performing. However, finding the global optimum $\mathcal{G}^{*}$ is highly non-trivial, reminding us of the problem of identification.

Relevant to our work is the general greedy search algorithm which repeatedly moves from the current state to the neighboring state that maximally improves the optimization criterion (in our application, BIC) until no improvement can be thusly achieved (Russell and Norvig 2009). That is, the algorithm is guaranteed to terminate in a locally optimal state, where locality is determined by the chosen definitions of a state and its neighborhood. The popular hill-climbing (HC) algorithm is a greedy search in the state space of DAGs, with neighboring states defined as DAGs obtainable by a single directed edge

addition, deletion, or reversal applied to the current DAG (Heckerman et al. 1995; Russell and Norvig 2009). The greedy equivalence search (GES) algorithm is a sound and complete variation of greedy search in which the state space is CPDAGs representing equivalence classes, with a forward-stepping edge addition phase followed by an edge deletion phase (Meek 1997; Chickering 2002a, b).

While widely applied and regarded as efficient and well-performing, the locality of the HC search in the DAG space unavoidably risks the common problem of accepting locally optimal yet globally suboptimal solutions. Gámez et al. (2011) showed that under certain conditions, HC returns a minimal independence map of the probability distribution $P$, but it does not guarantee a globally optimal result. HC can be augmented to more thoroughly search the DAG space with one or both of tabu list and random restarts, respectively governed by parameters $\left(t_{0}, t_{1}\right)$ and $\left(r_{0}, r_{1}\right)$. In what is known as the tabu search, a solution is obtained through HC while a tabu list stores the last $t_{1}$ DAG structures visited during the search. Then, the HC procedure is continued for up to $t_{0}$ iterations while allowing for minimal score decreases, with a local neighborhood restricted by the tabu list to avoid previously visited structures. In HC with random restarts, the HC procedure is repeated $r_{0}$ times after the initial execution by perturbing the current solution with $r_{1}$ random local changes. In our work, we prefer augmenting HC with a tabu list rather than random restarts due to its generally superior efficiency and its reliable and deterministic well-performance.

As mentioned in Sect. 1, prominent hybrid structure learning algorithms are instantiations of what we call the GSC framework, in which HC is executed from an EG restricted to a sparse set of candidate edge connections. That is, for a graph $\mathcal{G}=(\mathbf{V}, \mathbf{E})$ estimated using a constraint-based approach, define $\mathbf{A}=\{(i, j): i$ and $j$ are connected in $\mathcal{G}\}$ as the set of candidates: the unordered node pairs that have not been determined to be conditionally independent. HC is then executed from an EG on $\mathbf{V}$, considering adding an edge $i \rightarrow j$ only if $(i, j) \in \mathbf{A}$. MMPC and H2PC are two well-known examples, obtaining $\mathbf{A}$ according to sound skeleton estimation algorithms max-min parents and children (MMPC) and hybrid parents and children (HPC), respectively (Tsamardinos et al. 2006a; Gasse et al. 2014). The GSC strategy guarantees estimation of a valid DAG restricted to $\mathbf{A}$, but often accepts locally optimal solutions that are structurally inaccurate due to the connectivity of the DAG space induced by the HC neighborhood. As will be seen in Sect. 5.3, this problem persists even when the search space is well-restricted and a tabu list is utilized, leaving much to be desired. In this work, we primarily focus on improving upon the theoretical properties and empirical performance of the GSC framework, though our contributions may be applied to another hybrid approach that uses greedy search in the space of equivalence classes instead of DAGs, which we discuss briefly in Sect. 6 and the Supplementary Information.

# 4.2 Hybrid greedy initialization 

We now develop our proposed HGI strategy to overcome the aforementioned difficulties for hybrid algorithms belonging to the GSC framework. Our method is designed to retain the soundness and completeness of constraint-based structure learning while empirically improving structural estimation accuracy and achieving higher-scoring structures as compared to those obtained by the GSC framework. The primary novel contribution is the introduction of a score-based ordering to the application of orientation heuristics to obtain a favorable initialization for HC. Given the skeleton output of a constraint-based algorithm, we sequentially add v-structures that most improve the score, scored with respect to directed edges. We then make greedy determinations for the remaining undirected edges

![img-1.jpeg](img-1.jpeg)

Fig. 2 Example of pdag-to-dag (Dor and Tarsi 1992) applied to a PDAG pattern structure
according to efficient criteria from pdag-to-dag, assisted by Meek's rules R1-4 (Dor and Tarsi 1992; Meek 1995). Finally, we execute HC initialized by the resulting DAG. From a score-based learning perspective, the formulation of HGI may be understood as a principled strategy for obtaining a good starting point for greedy search. In what follows, we further detail and discuss the HGI algorithm.

Recall that pdag-to-dag (introduced in Sect. 3.2) is guaranteed to obtain a consistent extension of a PDAG if one exists, and thus implicitly includes Meek's rules R1-4 when the given PDAG is a valid pattern that admits a consistent extension. Let $\mathcal{G}_{0}$ and $\mathcal{G}$ be identical copies of a PDAG to be oriented. The algorithm repeatedly searches for a node $j$ satisfying the following conditions in a PDAG $\mathcal{G}_{0}$ :
(a) $j$ is a sink: that is, $j$ has no edges directed outwards in $\mathcal{G}_{0}$;
(b) For every vertex $k$ connected to $j$ by an undirected edge in $\mathcal{G}_{0}, k$ is adjacent to all the other vertices which are adjacent to $j$ in $\mathcal{G}_{0}$.

If such a node $j$ can be found, all undirected edges adjacent to $j$ are oriented into $j$ in $\mathcal{G}$ and $\mathcal{G}_{0}$. Node $j$ is then a complete sink, a node satisfying (a) with no undirected edges incident to it, and is removed from $\mathcal{G}_{0}$ along with all edges incident to it in order to uncover subsequent candidate nodes. This process is repeated until $\mathcal{G}$ is fully oriented to a DAG, or until no such node $j$ can be found, in which case the initial PDAG does not admit a consistent extension. Briefly exposited, (a) ensures acyclicity by requiring that all directed paths induced by considered orientations terminate in sinks, and (b) ensures that considered orientations do not create new v-structures if applied.

Consider an example of pdag-to-dag applied to a PDAG in Fig. 2. The algorithm proceeds as follows. Starting from the PDAG structure in Fig. 2a, nodes $X_{1}, X_{7}$, and $X_{8}$ satisfy conditions (a) and (b), with $X_{8}$ additionally a complete sink. Nodes $X_{2}, X_{4}$, and $X_{6}$ violate condition (a), and $X_{3}$ and $X_{5}$ violate condition (b). Since $X_{1}, X_{7}$, and $X_{8}$ are not adjacent to each other, they may be selected by the algorithm in an arbitrary order without affecting the particular outcome of the DAG extension, resulting in orientations $X_{4} \rightarrow X_{1}, X_{5} \rightarrow X_{1}$, and $X_{5} \rightarrow X_{7}$. Once these nodes are removed from consideration, $X_{5}$ and $X_{6}$ are likewise removed as complete sinks, and the remaining undirected edge $X_{2}-X_{3}$ may be oriented in either direction as both $X_{2}$ and $X_{3}$ satisfy (a) and (b).

Since the implementation of pdag-to-dag, as proposed, does not straightforwardly lend itself to greedy application, we accomplish this by developing a decomposed version of

pdag-to-dag. Let $\mathcal{G}_{0}$ be a PDAG with only v-structures oriented, and let $\mathcal{G}$ be a DAG consisting of only the directed edges in $\mathcal{G}_{0}$. We prioritize checking for and removing all complete sinks from consideration by deleting all edges incident to such nodes in $\mathcal{G}_{0}$, and we greedily consider orienting $i \rightarrow j$ in $\mathcal{G}_{0}$ and $\mathcal{G}$ if $i-j$ is an undirected edge in $\mathcal{G}_{0}$ and conditions (a) and (b) are satisfied for node $j$. For example, in a single greedy step applied to Fig. 2a, we would first remove $X_{8}$ from $\mathcal{G}_{0}$ as a complete sink, resulting in nodes $X_{1}, X_{6}$, and $X_{7}$ satisfying (a) and (b). We then greedily consider the individual edge orientations $X_{4} \rightarrow X_{1}, X_{5} \rightarrow X_{1}, X_{5} \rightarrow X_{7}$, and $X_{3} \rightarrow X_{6}$, applying the orientation that most improves the score computed with respect to the structure of $\mathcal{G}$ (i.e., all edges that have determined orientations). This design essentially decomposes the nodecentric operations in pdag-to-dag into single edge operations (e.g., $X_{4} \rightarrow X_{1}$ and $X_{5} \rightarrow X_{1}$ are considered as individual orientations instead of both being considered with node $X_{1}$ ), and its result is a DAG in the same equivalence class as the output of pdag-to-dag given a valid PDAG. In practice, as with the sequential v-structure application, the greedy ordering filters edges and selects between ambiguous orientations. In the case that undirected edges still exist in $\mathcal{G}_{0}$ and no node satisfying (a) and (b) can be found, we likewise greedily consider transformations compelled by Meek's rules R1-4 applied to $\mathcal{G}_{0}$. We detail the HGI strategy in Algorithm 4.

```
Algorithm \(4 \mathrm{HGI}\left(\mathcal{G}_{0}, \mathcal{D}, \mathbf{U}\right)\) (sample version)
input: undirected graph \(\mathcal{G}_{0}\), data \(\mathcal{D}\), and v -structures \(\mathbf{U}\)
output: DAG \(\mathcal{G}\)
    initialize \(\mathcal{G}\) as the empty graph on \(\mathbf{V}\)
    repeat
        orient \(i \rightarrow k\) and \(j \rightarrow k\) in \(\mathcal{G}_{0}\) and \(\mathcal{G}\) for \((i, k, j) \in \mathbf{U}\) that most improves
        \(\phi(\mathcal{G}, \mathcal{D})\) and does not induce any cycles or conflict with any v-structures
        in \(\mathcal{G}\)
    until no such improvement possible
    repeat
        delete all edges incident to complete sinks in \(\mathcal{G}_{0}\)
        apply the first applicable of the following operations for \(i-j\) in \(\mathcal{G}_{0}\) :
            (i) apply \(i \rightarrow j\) to \(\mathcal{G}_{0}\) and \(\mathcal{G}\) satisfying (a) and (b) that most improves
                \(\phi(\mathcal{G}, \mathcal{D})\)
            (ii) delete \(i-j\) from \(\mathcal{G}_{0}\) satisfying (a) and (b) that if applied, would
                most deteriorate \(\phi(\mathcal{G}, \mathcal{D})\)
            (iii) apply \(i \rightarrow j\) to \(\mathcal{G}_{0}\) and \(\mathcal{G}\) compelled by R1-4 that most improves
                \(\phi(\mathcal{G}, \mathcal{D})\)
            (iv) delete \(i-j\) from \(\mathcal{G}_{0}\) with \(i \rightarrow j\) compelled by R1-4 such that if
                applied, would most deteriorate \(\phi(\mathcal{G}, \mathcal{D})\)
    until no such operation possible
```

Important to note is that in the population setting, v-structure detection and orientation is order-independent, and while the particular DAG obtained by (our decomposed) pdagto-dag is order-dependent, it will always recover a DAG in the same equivalence class if successful (i.e., a consistent extension of the input PDAG exists). In such a case, whatever ordering imposed on both or either of the heuristics has no meaningful effect on the result. Furthermore, given a greedy criterion, a locally consistent score will asymptotically accept proposed additions of truly connected edges due to Eq. (13), thus preserving guaranteed

identification of the equivalence class of the underlying DAG. Indeed, in such a setting, a lenient score that prefers denser graphs is sufficient as only property Eq. (13) is required.

In the finite-sample setting, incorrectly inferred conditional independence information can result in the determination of incomplete or extraneous and even conflicting v-structures, and could result in PDAGs that do not admit a consistent extension (Remark 2). The outcome of a naive non-greedy application of v-structures and (our decomposed) pdagto-dag empirically varies in quality depending on the order by which the operations are applied due to conflicting operations and obstacles induced by the acyclicity constraint, providing the primary incentive for greedy decisions regarding proposed constraint-based orientations. From a constraint-based learning perspective, greedy forward stepping imposes a greedy ordering on the application of v -structures and other potentially conflicting or ambiguous edge orientations, while additionally providing an element of selectivity by disregarding operations that deteriorate the score.

As already discussed, Algorithm 4 asymptotically preserves sound and complete orientation of the skeleton of the underlying DAG $\mathcal{G}$ to a DAG in its equivalence class, straightforwardly evident from our discussion thus far.

Lemma 1 Suppose that probability distribution $P$ is fixed and faithful to a $D A G \mathcal{G}^{*}, \mathcal{D}_{n}$ is data containing $n$ i.i.d. samples from $P$, and $\phi$ is a score satisfying local consistency. Let $\widetilde{\mathcal{G}}_{n}$ be the output of Algorithm 4. If $\mathcal{G}_{0}$ is the skeleton of $\mathcal{G}^{*}$ and $\mathbf{U}$ contains the v-structures of $\mathcal{G}^{*}$, then $\widetilde{\mathcal{G}}_{n}$ is in the same equivalence class as $\mathcal{G}^{*}$ with probability approaching one as $n \rightarrow \infty$.

Note that while we state Lemma 1 assuming possession of all v-structures $\mathbf{U}$ that are present in the underlying DAG, these may be correctly obtained asymptotically depending on what information is available from the skeleton estimation method, which we discuss in Appendix B.

Indeed, neither operations (ii)-(iv) in line 7 nor any subsequent score-based search is necessary for Lemma 1 to hold, but rather serve in a corrective capacity in the finite-sample setting. The process of completing and deleting sinks to uncover subsequent sinks in $\mathcal{G}_{0}$ requires decisions for each undirected edge participating in a node satisfying (a) and (b) in order to continually progress in the algorithm. Operation (ii) discards each proposed edge addition $i \rightarrow j$ that deteriorates the score when no improvement according to (i) is possible so that $j$ can be completed and removed. In the case that no node satisfying both (a) and (b) can be found, we apply the same greedy criterion to all edges compelled by Meek's rules R1-4 in operations (iii) and (iv). These rules are not subject to a leaf-to-root construction and often help resume applications of (i) and (ii), for example by deleting an undirected edge $i-j$ participating in an unshielded triple from $\mathcal{G}_{0}$ so that $j$ can satisfy (b).

Note that in finite-sample applications, repeated application of (i)-(iv) does not guarantee orientation or deletion of all undirected edges in $\mathcal{G}_{0}$ [e.g. consider an undirected square where no vertex satisfies (a) and (b) and no edge is compelled by R1-4], though we empirically find it to typically address most if not all edges. Furthermore, while the adjacency criterion (b) exists to prevent the creation of additional v-structures, it is still possible for new v-structures to be created by deletion. Consider an undirected triangle in $\mathcal{G}_{0}$ where all three vertices $i, j$, and $k$ satisfy (a) and (b). The greedy ordering may orient $i \rightarrow k$ and $j \rightarrow k$, remove node $k$ once it is a complete sink, and eventually delete $i-j$, leaving $i \rightarrow k \leftarrow j$ as a new v-structure in $\mathcal{G}$.

While essentially equivalent in the large sample setting, directly executing a greedy decomposed pdag-to-dag poses a number of pragmatic advantages over first greedily applying Meek's rules in the presence of finite-sample error. The sink criterion (a) effectively accomplishes acyclicity checks for each proposed edge orientation, which grow increasingly computationally burdensome for larger networks. It additionally induces a leaf-to-root construction with operations that minimally conflict with subsequent operations, with $i \rightarrow j$ only denying $i$ from satisfying (a) until $j$ is removed. This further strengthens the effect of the greedy ordering in minimizing ambiguity in the initial DAG construction process. Indeed, considering Theorem 1, the order of greedy v-structure application is unambiguous given a score equivalent metric. In contrast, HC from an EG restricted to sparse candidates $\mathbf{A}$ begins with $O\left(|\mathbf{A}|^{2}\right)$ ambiguous edge additions where, for any distinct node pair $(i, j) \in \mathbf{A}$, adding the edge $i \rightarrow j$ or $j \rightarrow i$ results in the same score improvement, again evident from Theorem 1. HC may encounter many such non-unique edge additions which are typically decided according to a node ordering that is often arbitrary, and their compounding effect can result in conflicts that, together with the acyclicity constraint, entrap HC in local solutions.

Remark 3 Relevant to our work is the PEF framework by Gu and Zhou (2020), a hybrid strategy consisting of a final fusion step that is conceptually analogous to a non-greedy form of sparse candidate HC initialized with the directed edges of an estimated PDAG rather than an EG. The algorithm removes all undirected edges from a PDAG input and performs local edge additions, reversals, and deletions to the resulting DAG that improve the overall score by repeatedly iterating through the surviving node pairs in a semi-arbitrary order, simultaneously testing for conditional independence. While they empirically demonstrated this process to correct many of the errors in the estimated structure, we find that the order with which the edges are visited can result in varying degrees of improvement, and the testing strategy performs redundant conditional independence tests. Furthermore, naively initializing a score-based search with the PDAG output of a constraint-based algorithm may prove volatile given the sensitivity of skel-to-cpdag to erroneous conditional independence inferences as well as its order-dependence. Lastly, even if initialized by the DAG consisting of the compelled edges of the underlying DAG and perfectly restricted to true connections, neither PEF nor HC with a consistent score guarantees asymptotic orientation to a DAG in the equivalence class of $\mathcal{G}$.

```
Algorithm \(5 \mathrm{pHGS}(\mathcal{D}, \alpha, \tau, \alpha^{(\tau)})\) (sample version)
input: data \(\mathcal{D}\), threshold \(\alpha\), number of estimates \(\tau\), minimum threshold \(\alpha^{(\tau)}\)
output: DAG \(\mathcal{G}\)
    execute \(\mathrm{pPC}(\mathcal{D}, \alpha)\) (the sample version of Algorithm 2), omitting edge
        orientation in line 19, to obtain \(\Phi\) and \(\mathbf{S}\) as in Eq. (10)
    execute \(\mathcal{G}\left({ }^{(t^{*})} \leftarrow \operatorname{PATH}\left(\Phi, \mathbf{S}, \mathcal{D}, \tau, \alpha^{(\tau)}\right)\right.\) (Algorithm 3) with the following
        modifications:
        line 5: detect v-structures \(\mathbf{U}^{(t)}\) with \(\mathbf{S}^{(t)}\) and execute \(\mathcal{G}^{(t)} \leftarrow\)
        HGI \(\left(\mathcal{G}^{(t)}, \mathcal{D}, \mathbf{U}^{(t)}\right)\) (Algorithm 4)
        line 6: \(\operatorname{copy} \tilde{\mathcal{G}}^{(t)} \leftarrow \mathcal{G}^{(t)}\)
    execute hill-climbing (or otherwise greedy search) to obtain \(\mathcal{G}\), initialized
        with the selected estimate \(\mathcal{G}\left(t^{*}\right)\) and restricted to \(\mathbf{A}=\left\{(i, j): \Phi_{i j} \leq \alpha^{(1)}\right\}\)
        where \(\alpha^{(1)}=\alpha\) is the maximum \(p\)-value (see Sect. 3.2)
```

Finally, we detail in Algorithm 5 the partitioned hybrid greedy search ( pHGS ) algorithm, a composition of pPC, PATH, and HGI. The pHGS algorithm efficiently restricts the search space with the pPC algorithm (Algorithm 2), obtaining $\Phi$ and $\mathbf{S}$ as in Eq. (10) for use in PATH. Instead of generating $\tau$ CPDAG estimates with skel-to-cpdag, PATH instead obtains $\tau$ DAG estimates by detecting v -structures $\mathbf{U}^{(t)}$ in each thresholded skeleton $\mathcal{G}^{(t)}$ and executing HGI (Algorithm 4). See Appendix B for details on v-structure detection. The highest-scoring of the $\tau$ estimates $\mathcal{G}^{\left(t^{*}\right)}$ is selected to initialize HC (or an alternate score-based search algorithm) restricted to the active set $\mathbf{A}=\left\{(i, j): \Phi_{i j} \leq \alpha^{(1)}\right\}$. We choose the maximum threshold $\alpha^{(1)}$ (see Sect. 3.2) for the restriction instead of $\alpha^{\left(t^{*}\right)}$ corresponding to the highest-scoring estimate to reduce false negatives that excessively restrict the score-based exploration in the finite-sample setting.

In the large-sample limit, under the same conditions and parameter specifications as Theorem 3 and Lemma 1, the output of pHGS (Algorithm 5) is a DAG that is Markov equivalent to the underlying DAG. Indeed, this result is already achieved by the modified PATH in line 2, and in such a case the subsequent greedy search exists only to verify its optimality.

# 5 Numerical results 

We conducted extensive simulations to demonstrate the merits of pPC, PATH, HGI, and pHGS alongside a number of other popular structure learning algorithms. In addition to considering data simulated from various reference Bayesian network configurations, which we introduce in Sect. 5.1, we analyze real data in the form of a well-known flow cytometry dataset in Sect. 5.4.

### 5.1 Simulation set-up

The performance of our methods were primarily evaluated in comparison to several structure learning algorithms on numerous reference Bayesian networks obtained from the

Table 1 Networks for data generation consisting of $\kappa$ connected sub-networks with $p$ nodes, $|\mathbf{E}|$ edges, average number of neighbors $\left|\overline{\mathbf{N}^{G}}\right|$, maximum in-degree $\max _{i}\left|\boldsymbol{\Pi}_{i}^{G}\right|$, and $|\boldsymbol{\Theta}|$ number of parameters


Bayesian network repository compiled alongside the R package bnlearn (Scutari 2010, 2017). Most available discrete networks were considered, with the MUNIN networks represented by MUNIN1 and the LINK network omitted because certain minuscule marginal probabilities required much larger sample sizes to generate complete sets of valid variables. The following preprocessing procedures were applied to each network. For each random variable $X_{i}$, non-informative states $x_{i}$ with $\operatorname{Pr}\left(X_{i}=x_{i}\right)=0$ were removed, and non-informative variables $X_{i}$ with $\left|r_{i}\right|=1$ were likewise removed. Furthermore, each variable $X_{i}$ was restricted to $\left|r_{i}\right| \leq 8$, with the extraneous discrete states of excessively granular variables removed by randomly merging states. The conditional probability distributions imposed by merged states were averaged, weighted according to their marginal probabilities.

In order to demonstrate the effectiveness of our methods for learning large discrete networks, we generated larger versions of each network with a house implementation of the tiling method proposed by Tsamardinos et al. (2006b), modified to approximately preserve the average in-degree amongst non-minimal nodes. In particular, let $\mathcal{G}=(\mathbf{V}, \mathbf{E})$ be the structure consisting of $\kappa$ disconnected subgraphs to be connected by tiling. For a minimal node $k$ (that is, $k$ has no parents), instead of probabilistically choosing the number of added interconnecting edges, denoted by $e_{k}$, according to $e_{k} \sim \operatorname{Unif}\left\{0, d:=\max _{i \in \mathbf{V}}\left|\boldsymbol{\Pi}_{i}^{G}\right|\right\}$, we let $\operatorname{Pr}\left(e_{k}=a\right)=\sum_{i \in \mathbf{V}} \mathbb{1}\left\{\left|\boldsymbol{\Pi}_{i}^{G}\right|=a\right\} /|\mathbf{V}|$ for $a=0, \ldots, \min \{d, 4\}$. Note that in this process we did not enforce any block structure on the tiled structures.

The considered networks, along with select descriptive characteristics, are presented in Table 1, ordered by increasing complexity. The MIX network consists of the 14

networks from Table 1 with the least complexity, tiled in random order. For each network configuration, we generated $N=100$ datasets with $n=25,000$ data samples each, for a total of 2000 datasets. The $p$ columns of each dataset were randomly permuted so as to obfuscate any information regarding the causal ordering. Note that while only one sample size was considered for all the networks of similar order in $p$, the networks vary significantly with respect to sparsity, structure, and complexity, thus representing a wide variety of conditions.

Algorithm implementations of competing algorithms MMPC, HPC, HITON, IAMB, MMHC, and H2PC, which we briefly introduce in their respective featuring sections, were obtained from the R package bnlearn, which is written in R with computationally intensive operations delegated to C (R Core Team 2021; Scutari 2010, 2017). We also compared against GES and FGES from rcausal, the R package wrapper for the Tetrad Library (Wongchokprasitti 2019). Our pPC, PATH, HGI, and pHGS implementations were built in R and Rcpp using tools from the bnlearn package, and the results for PC were obtained by executing pPC restricted to $\kappa=1$ for fair comparison. We have made our methods publicly available in the form of an R package at https://github.com/ jirehhuang/phsl.

We evaluate the quality of a graph estimate $\hat{\mathcal{G}}=(\mathbf{V}, \hat{\mathbf{E}})$ with respect to the underlying $\operatorname{DAG} \mathcal{G}=(\mathbf{V}, \mathbf{E})$ by considering the Jaccard index (JI) of the CPDAG of $\hat{\mathcal{G}}$ in comparison to the CPDAG of $\mathcal{G}$. JI is a normalized measure of accuracy (higher is better) that is monotonically associated with the F1 score, computed as $\mathrm{JI}=\mathrm{TP} /(|\mathbf{E}|+|\hat{\mathbf{E}}|-\mathrm{TP})$ where TP is the number of true positive edges: the number of edges in the CPDAG of $\hat{\mathcal{G}}$ that coincide exactly with the CPDAG of $\mathcal{G}$ (both existence and orientation).

We use the JI as our primary accuracy metric over the popular structural Hamming distance (SHD) as we find it to be consistent with SHD (higher JI almost always indicates lower SHD) and for its convenience as a normalized metric. The choice of evaluating the CPDAG estimates rather than DAG estimates is motivated foremost by the fact that given that our estimates are inferred from observational data, the orientation of reversible edges in DAGs provide no meaningful interpretation (see Sect. 2.1). Additionally, the aforementioned metrics allow for evaluation of the quality of estimated PDAGs that do not admit a consistent extension (see Remark 2).

Regarding efficiency, execution time is confounded by factors such as hardware, software platform, and implementation quality. Even if the aforementioned variables are accounted for, performing all simulations on the same device cannot guarantee consistent performance over all simulations and instead severely constrains the feasible scope of study. Thus, we evaluate the estimation speed of structure learning algorithms by the number of statistical calls to conditional independence tests or local score differences, with fewer calls indicating greater efficiency. For pPC, we additionally include mutual information and entropy evaluations to account for the expense of clustering (see Sect. 3.1.1).

Remark 4 In general, we find the relative execution time comparisons to be approximately equivalent to the relative number of statistical calls, within comparable implementations. For example, the relative estimation speed of pPC as compared to PC is approximately equivalently characterized by their relative execution time and relative number of statistical calls. The implementation of HC, however, does not scale as well as that of pPC, resulting in disproportionately greater relative execution times compared to relative number of statistical calls.

# 5.2 pPC and PATH 

As the pPC algorithm can be considered an augmentation of the PC algorithm by imposing an ordering to the conditional independence tests by partitioning, we highlight its performance against the PC algorithm. We additionally apply the PATH augmentation to pPC and PC.

Note that our proposed HGI strategy motivates the design of high-performing con-straint-based algorithms that not only efficiently restrict the search space, but also demonstrate potential for good score-based search initialization with HGI by producing structurally accurate estimates. As such, we further validate the performance of pPC and PATH against four other established constraint-based structure learning algorithms, all local discovery methods, modified with a symmetry correction for skeleton learning (Aliferis et al. 2010). Max-min parents and children (MMPC) uses a heuristic that selects variables that maximize a minimum association measure before removing false positives by testing for conditional independence (Tsamardinos et al. 2003b, 2006a). The fast version of the incremental association Markov blanket algorithm (Fast-IAMB; IAMB in this paper) is a twophase algorithm that consists of a speculative stepwise forward variable selection phase designed to reduce the number of conditional independence tests as compared to single forward variable selection, followed by a backward variable pruning phase by testing for conditional independence (Tsamardinos et al. 2003a; Yaramakala and Margaritis 2005). The semi-interleaved implementation of HITON ${ }^{1}$ parents and children (SI-HITON-PC; HITON in this paper) iteratively selects variables based on maximum pairwise marginal association while attempting to eliminate selected variables by testing for conditional independence (Aliferis et al. 2003, 2010). Finally, HPC is comprised of several subroutines designed to efficiently control the false discovery rate while reducing false negatives by increasing the reliability of the tests (Gasse et al. 2014). For each of these methods, following skeleton estimation, we orient edges by detecting and orienting v-structures according to Eq. (22) (in Appendix B) and applying Meek's rules R1-4.

The maximum size of considered conditioning sets $m$ was chosen empirically for a balance between efficiency and well-performance: $m=3$ for pPC and PC, $m=4$ for HPC, and $m=5$ for the remaining methods. We note that HPC insignificantly varies in efficiency with $m$ and produces the most accurate estimates in our simulations with $m=4$, and the remaining competing methods are more efficient but significantly less accurate with $m<5$. Additionally for pPC, we restricted the maximum set size to 3 for the evaluations in Eqs. (7) and (8), and the maximum considered neighborhood size to 5 (see Remark 1). We executed each algorithm with each of the following ten choices of significance level thresholds:

$$
\begin{gathered}
\alpha \in \mathcal{A}:=\{0.1,0.05,0.01,0.005,0.001,0.0005 \\
0.0001,0.00005,0.00001,0.000005\}
\end{gathered}
$$

For each execution of pPC and PC, estimates for $\tau=10$ thresholding values were automatically generated with PATH (Algorithm 3) according to Eq. (11), restricted to a minimum value of $\alpha^{(\tau)}=10^{-5}$.

The comparison results for pPC and PATH are reported in Table 2. We first compare pPC against PC in terms of computational efficiency and estimation accuracy.

[^0]
[^0]:    ${ }^{1}$ From the Greek word " $X \imath \tau o v$ ", pronounced "hee-tón", meaning "cover", "cloak", or "blanket".

Table 2 Accuracy (JI) and efficiency (Normalized Calls) comparison between pPC and PC, without and with PATH (indicated by None and $\tau=10$, respectively)


Columns $\mathrm{pPC}^{\mathrm{a}}$ and $\mathrm{PC}^{\mathrm{a}}$ provide the highest JI and total statistical calls of executions for all $10 \alpha \in \mathcal{A}$. Rows correspond to the networks in Table 1, and best values are provided in boldface
${ }^{a}$ Normalized by $\mathrm{pPC}-\mathrm{PATH}(\alpha=0.1, \tau=10)$

Unsurprisingly, pPC demonstrates the greatest computational benefit over PC for large $\alpha$, typically halving the number of conditional independence tests for $\alpha=0.1$, as seen from the normalized calls of PC with $\alpha=0.1$ and PATH $(\tau=10)$ in the table. Note that our partitioning strategy is solely responsible for this computational improvement as parallelization has no bearing on the efficiency metric, and by design pPC can, like PC, further benefit from parallel execution. The reduction suffers from diminishing returns with decreasing $\alpha$, with an average speed-up of about $22 \%$ across the ten $\alpha$. Notwithstanding, we found pPC and PC, even without PATH, to generally prefer larger $\alpha$. In particular, estimates with thresholds $\alpha=0.1$ and 0.05 respectively produced the best estimates (highest JI) for over $50 \%$ and $17 \%$ of datasets, resulted in the highest average JI scores for 13 and 3 network configurations, and achieved the highest two JI scores averaged across all datasets. As such, algorithm executions with large significance level thresholds are not unreasonable in practice, which coincides with the general strategy of PATH. We note that while pPC appears to be typically slightly more accurate than PC, we do not find the improvement to be substantial and primarily assert that pPC performs comparably to PC.

Additionally, we see from Table 2 that PATH applied to pPC and PC is able to obtain, from a single execution with $\alpha=0.1$ and $\tau=10$, estimates of similar and often superior quality compared to the best estimates without PATH ( $\mathrm{pPC}^{*}$ and $\mathrm{PC}^{*}$ ) obtained from 10 executions with the various $\alpha \in \mathcal{A}$. Important to note is that the solution path automatically selects an estimate based on a BIC selection strategy restricted to valid CPDAG estimates, if any (see Remark 2), whereas for the multiple executions the maximum JI (as computed with respect to the CPDAG of the underlying DAG) for each dataset was chosen. The BIC selection strategy appears less effective for a couple of networks (e.g., 15 and 19), where on average the original estimates without PATH were more structurally accurate than those chosen from a solution path. One explanation for the worse performance could be the presence of invalid CPDAG estimates. PATH prefers valid estimates, and may prefer lowerscoring valid estimates over more structurally accurate invalid estimates. In the case that all estimates are invalid, the semi-arbitrary DAG extension process can be volatile, resulting in structurally inaccurate estimates being selected. As anticipated in Sect. 3.2, the computational expense required to execute Algorithm 3 is practically negligible in comparison to skeleton estimation. The statistical calls for pPC and PC with PATH $(\alpha=0.1$ and $\tau=10)$ include the scores evaluated for BIC selection from the generated solutions by PATH, and are practically indistinguishable from those without PATH, with the score evaluations typically consisting of less than $0.1 \%$ of the statistical calls.

In Table 3, we compare pPC with PATH against other constraint-based structure learning algorithms. We exclude PC as its comparison with pPC is thoroughly demonstrated in Table 2. Again, competing methods report optimal results and total statistical calls for the executions across the 10 significance levels $\alpha \in \mathcal{A}$. In terms of structural accuracy, the only algorithm that can compete against pPC is HPC, which outperforms pPC in 12 of the network configurations, sometimes by a substantial margin. However, when it comes to efficiency, there is no contest against the pPC algorithm, in most cases even if the number of calls were averaged across the 10 executions instead of summed. Additionally, pPC most often produced valid CPDAG estimates, succeeding with $44 \%$ of the datasets with only $\alpha=0.1$ and $\tau=10$ in contrast to from $10 \%$ by HPC to up to $41 \%$ by IAMB with $\alpha \in \mathcal{A}$.

In the Supplementary Information, we provide additional results for the comparisons of pPC against three constraint-based methods, PC, MMPC, and HPC, thus far discussed in Tables 2 and 3. We include detailed tables that report additional metrics as well as standard deviations, and a figure that visualizes the comparisons and variability of the accuracy and efficiency results across executions by including the results for individual datasets for each network (Fig. S6). Furthermore, we provide extended simulation results investigating the effect of the clustering quality of pPC on its subsequent structure learning, as well as evaluating the performance of PATH for varying sample sizes.

# 5.3 HGI and pHGS 

Having discussed the theoretical merits of HGI in Sect. 4.2, we demonstrate the empirical performance of HGI and pHGS in this section, beginning with the comparison and application to the GSC framework. We refer to unrestricted HC as simply HC and perfectly restricted HC as GSC*. In general, for a restriction of the search space with constraintbased algorithm Alg, we refer to the GSC version as Alg-HC, and the version with HGI as Alg-HGI-HC. However, we refer to the versions of established algorithms MMHC and H2PC that are augmented with HGI as MMHC-HGI and H2PC-HGI.

Table 3 Accuracy (JI) and efficiency (Normalized Calls) comparison amongst constraint-based methods


Rows correspond to the networks in Table 1, and the best values are provided in boldface
${ }^{a}$ Normalized with respect to $\mathrm{pPC}-\mathrm{PATH}(\alpha=0.1, \tau=10)$
${ }^{\mathrm{b}} \mathrm{pPC}-\mathrm{PATH}(\alpha=0.1, \tau=10)$, while all other methods report the highest JI from and the (normalized) total statistical calls for the executions across the $10 \alpha \in \mathcal{A}$

The HC phase of each algorithm was augmented with a tabu list to avoid $t_{1}=100$ previously visited DAG structures for $t_{0}=100$ suboptimal iterations (see Sect. 4.1). All scorebased methods evaluated structures with the BIC score. We executed pHGS with significance level $\alpha=0.01$, and generated and selected from $\tau=10 \mathrm{HGI}$ estimates in PATH by thresholding to a minimum of $\alpha^{(\tau)}=10^{-5}$.

The accuracy results for HGI and pHGS are summarized in Table 4. All methods other than $\mathrm{HC}, \mathrm{GSC}^{*}$, and pHGS report the highest JI for the executions across the ten $\alpha \in \mathcal{A}$. In the first column, the performance of (unrestricted) HC leaves much to be desired with its generally lackluster structural accuracy in comparison with the hybrid methods. Exceptions exist, as anticipated by Table 3 in which constraint-based methods struggle to produce good estimates for some higher complexity networks, often inferring excessive false negatives that erroneously reduce the search space. In such cases, hybrid approaches are limited by their constraint-based component and thus perform worse than HC.

We first highlight the demonstrated improvement of initialization with HGI compared to the EG (as in the GSC framework) for different skeleton restriction methods. A perfect restriction to the true skeleton represents the most optimistic scenario for GSC and HGI, wherein all true positives are accessible and no false positives are considered. HGI

Table 4 Accuracy (JI) comparisons for CPDAGs estimated without and with HGI (indicated by EG for empty graph and HGI, respectively) given restrictions obtained by various skeleton methods


Rows correspond to the networks in Table 1, and best values amongst pHGS, HC, MMHC, and H2PC are provided in boldface
${ }^{\mathrm{a}} \mathrm{pHGS}(\alpha=0.01, \tau=10)$; all other methods, excluding HC and GSC $^{\mathrm{a}}$, report the highest JI for the executions across the $\operatorname{ten} \alpha \in \mathcal{A}$
additionally enjoys consideration of all true v-structures when detecting v-structures amongst unshielded triples according to Eq. (22). Unsurprisingly, perfectly restricted GSC uniformly improves on the performance of unrestricted HC. The addition of HGI achieves further improvements to structural accuracy of typically $28 \%$ and up to $139 \%$ (Table 4, True Skeleton). This same trend persists when comparing GSC without and with HGI for empirical skeleton estimation methods pPC, MMPC, and HPC, demonstrating the effectiveness of HGI. For the various skeleton estimation methods, the addition of HGI achieves estimates that are typically $14 \%$ and up to $120 \%$ more structurally accurate.

We now compare pHGS with established algorithms HC, MMHC, and H2PC, the best values amongst which are indicated in boldface in Table 4. In most of the network configurations, a single execution of pHGS learns estimates of higher quality than the best of the ten executions with $\alpha \in \mathcal{A}$ of MMHC and H2PC. Note that for the GSC framework, the goal of parameter tuning for $\alpha$ is to obtain a balance between true positives and true negatives. MMHC does not outperform pHGS in any meaningful capacity, and H2PC only substantially outperforms pHGS for higher complexity networks due to a mechanism in HPC to reduce false negative edges (Gasse et al. 2014). While the addition of HGI dramatically

Table 5 Median and $95 \%$ precision intervals of percent additional statistical calls by GSC and HGI-HC with respect to skeleton learning


Each data point represents one algorithm execution for each dataset
${ }^{a} \mathrm{pPC}$ under HGI-HC represents pHGS executed with $\tau=10$ and $\alpha=0.01$
${ }^{\mathrm{b}}$ MMPC and HPC include the results from every individual execution across the ten $\alpha \in \mathcal{A}$
improves the general accuracy of MMHC, only H2PC-HGI performs competitively with pHGS, reflective of the results in Table 3 where HPC rivaled pPC in the realm of structural accuracy. However, as we will see from our discussion of Table 5, the speed comparisons in Table 3 generally hold for these hybrid variants as well, with pHGS on average nearly an order of magnitude more efficient than H 2 PC and around 2.5 times more efficient than MMHC per execution, with or without HGI. HC only outperforms the hybrid methods for a few structures in which the latter overly restrict the search space. Overall, we find pHGS to be most well-performing method, followed by H2PC, MMHC, and HC. We provide detailed results for these methods in the Supplementary Information, with boxplots (Fig. S7) visualizing the accuracy comparisons across datasets for each network as well as tables with additional metrics.

In Table 5, we compare the computational expense of GSC and HGI-HC with respect to skeleton learning. Under HGI-HC, the Detect column refers to the computational expense of detecting v-structures necessary to execute HGI (Algorithm 4) (see Appendix B). While HGI-HC typically comes at greater computational cost compared to the HC step in GSC, the expense of either is largely negligible in comparison to that of skeleton learning, generally (and often significantly) fewer than an additional $2 \%$ statistical calls. Rare exceptions exist, in particular extreme cases where MMPC or HPC required a significant number of additional tests to detect v-structures. Here, pPC has a clear computational advantage, having the ability to detect v -structures using separation sets accrued throughout skeleton learning [see Eq. (21) in Appendix B], resulting in fewer than $4.8 \%$ additional calls for every dataset to execute HGI $\tau=10$ times in PATH and perform HC from the chosen initial DAG. Other algorithms must conduct additional conditional independence tests to detect v-structures via Eq. (22), which can quickly add up if the learned skeleton structure has a significant number of unshielded triples $i-k-j$, or if either or both of $\left|\mathbf{N}_{j}^{\mathcal{G}}\right|$ and $\left|\mathbf{N}_{j}^{\mathcal{G}}\right|$ are large. On the topic of efficiency, unrestricted HC typically requires three to five times the number of statistical calls to execute as compared to pHGS, providing further validation for the hybrid approach.

In general, we find the initial DAG obtained by HGI (Algorithm 4) through the greedy application of v-structures and greedy decomposed pdag-to-dag to be typically superior in structural accuracy compared to the direct application of skel-to-cpdag (Algorithm 6), the standard edge orientation strategy of constraint-based algorithms. HGI exhibits the greatest median improvement of $16.7 \%$ over skel-to-cpdag when applied to pPC , followed by $9.5 \%$ with $\mathrm{HPC}, 7.3 \%$ restricted to the

skeleton of the underlying DAG (True Skeleton), and 1.9\% with MMPC. In general, pPC detects the most v-structures as its detection criterion Eq. (21) may be considered less strict than Eq. (22) used by True Skeleton, MMPC, and HPC. Consequently, pPC generally detects a significant number of false positive v-structures, thus benefiting most significantly from the greedy v-structure determinations. The poor skeleton estimation performance of MMPC is likely responsible for its lackluster improvement, with its estimated skeletons generally containing the fewest unshielded triples corresponding to true v-structures in the underlying DAGs in comparison to pPC and HPC.

Next, we compare pHGS against GES, introduced in Sect. 4.1, along with one of its variants, which serve well as points of reference for evaluating pHGS as they share comparable theoretical guarantees in our investigative setting, being sound and complete for Bayesian network structure learning (Meek 1997; Chickering 2002a, b). Ramsey (2015) proposed the fast greedy (equivalence) search algorithm (in this paper, FGES), which featured a number of optimizations and adjustments to scale up GES to handle large networks. In addition to techniques such as parallelization and addressing redundant scoring, perhaps the most prominent improvement was that of blacklisting zero correlation edges when computing initial scores for the addition of edges to the EG. This drastically reduces the number of computations of local score differences. A highly optimized implementation of FGES is available in the R package rcausal, and we roughly recover an efficient implementation of the original GES algorithm by omitting the blacklisting step (Wongchokprasitti 2019).

In the detailed results in Table 6, in addition to the JI and $\log _{10}$ number of statistical calls (Calls), we report the number of predicted edges (P), true positives (TP), edges correctly present but with incorrect orientation (R), false positives (FP), and the SHD, which may be interpreted as the number of edge additions, deletions, and reversals required to traverse from one graph to another.

For most networks, pHGS executes significantly faster than GES, with a few exceptions, most notably in networks with higher complexity. With respect to FGES, we find pHGS to be approximately equivalently efficient in most cases, though considerably slower in some. The initial blacklisting feature in FGES functions similarly to that of Eq. (6) in the pPC algorithm, drastically reducing the number of considered edge connections. Furthermore, (F)GES conducts its greedy search in the reduced space of equivalence classes represented by CPDAGs rather than DAGs.

In terms of structural accuracy, pHGS performs competitively against GES and FGES. Consistent with the observations of Ramsey (2015), we find that the significant computational reductions achieved by FGES generally do not compromise the quality of learned structures compared to GES. The results for FGES are quite similar to that of GES for all metrics apart from number of statistical calls, though FGES does appear to obtain marginally sparser networks. As a hybrid algorithm that estimates the skeleton with a constraint-based approach, pHGS is much more restrictive in determining edge connections, resulting in significantly fewer true positives than (F)GES in some networks. As discussed previously in this section, in these scenarios, the pPC component excessively inferred false negatives that erroneously reduced the set of candidate edges. On the other hand, however, pHGS produced substantially fewer false positives than (F)GES for not only these networks but indeed in every network configuration. In such a way, pHGS appears more appropriate in applications where conservative estimation of edge connections is desired.

Table 6 Results comparing pHGS against GES and FGES


Table 6 (continued)


Calls reports $\log _{10}($ calls $)$

# 5.4 Real data application 

To evaluate our methods applied to real data, we analyzed a flow cytometry dataset generated by Sachs et al. (2005) through a series of experiments measuring $p=11$ phosphorylated proteins and phospholipids. In particular, we considered their preprocessed dataset containing $n=5400$ observations discretized to low, medium or high levels of the phosphorylated components, available in the R package sparsebn (Aragam et al. 2019). The structure of the currently accepted signalling network, which we refer to as the consensus network, is shown in Fig. 3a, and contains 20 directed edges.

We executed pHGS, MMHC, H2PC, HC, and FGES on this dataset, reporting the structure learning performance with respect to the consensus DAG. Since the dataset contains a mixture of observational and interventional data, we directly evaluate the DAG estimates against the consensus network instead of comparing their respective CPDAGs. For FGES, which outputs a CPDAG representing an equivalence class, we obtained a DAG extension by applying lines 5-8 of Algorithm 4 to evaluate the structure learning accuracy of FGES, which we note is significantly more favorable for FGES than comparing its CPDAG to the CPDAG of the consensus network. The hybrid algorithms pHGS, MMHC, and H2PC were executed with $\alpha \in \mathcal{A}$ in Eq. (15), with other parameters unchanged from Sect. 5.2 with the exception of $\alpha^{(\tau)}=10^{-6}$ to

![img-2.jpeg](img-2.jpeg)

Fig. 3 Comparison of a the consensus network and $\mathbf{b}$ the DAG estimated by pHGS. In b, edges correctly present in the consensus graph are drawn in solid black, edges with incorrect orientation in solid red, and false positive edges in dashed red (Color figure online)

Table 7 Structure learning and difference in test log-likelihood performance on discretized cytometry data


ensure $\alpha^{(r)}<\alpha$ for all executions of pHGS. For these methods, we present the results for the estimates closest in sparsity to the consensus graph ( 20 edges), which coincide with those with the highest JI. The results are reported in Table 7, and the pHGS estimate is shown in Fig. 3b.

By a substantial margin, pHGS produced the most structurally accurate estimate with respect to the consensus network, recovering 11 out of the 20 well-established causal relationships. The score-based algorithms FGES and HC obtained the densest networks as they do not conduct any restriction of the search space. In contrast, MMHC estimated the sparsest graph and indeed estimated the exact same graph for all $10 \alpha \in \mathcal{A}$, obtaining different restrictions of the search space via MMPC yet arriving at the same network structure in the restricted HC step.

# 6 Discussion 

In this paper, we proposed three independent yet compatible contributions to the general well-performance of discrete Bayesian network structure learning, culminating in the form of the pHGS algorithm.

First, the pPC algorithm improves on the empirical efficiency of the PC algorithm while retaining its soundness and completeness as well as its empirical performance. Though it is difficult to quantify the expected computational reduction, our simulation results in Table 2 indicate that for the empirically preferred significance level threshold, pPC typically requires less than half the number of conditional independence tests per execution compared to PC. This speed-up is enjoyed at no compromise to structural accuracy, with pPC performing comparably with PC. Second, the PATH algorithm effectively accomplishes the task of parameter tuning for certain constraint-based structure learning algorithms such as pPC and PC, theoretically preserving consistency in the classical setting and empirically achieving highly competitive structural accuracy at negligible computational expense. In the current landscape, the asymptotic result for sound and complete constraint-based structure learning asserts the existence of some uninformative sequence of significance levels $\alpha_{n} \rightarrow 0$ as $n \rightarrow \infty$ that recovers the underlying equivalence class in the large-sample limit. We prove that appropriately applied to pPC or PC executed with any fixed threshold $\alpha \in(0,1)$, PATH asymptotically includes and correctly selects the underlying CPDAG in its generated solution path. We demonstrate an analogous result in the empirical setting, wherein pPC with PATH returns estimates of competitive quality to that of optimistic parameter tuning, achieving significant computational reductions compared to the current standard.

Third, the HGI algorithm provides a principled strategy for initializing score-based search in hybrid methods that asymptotically preserves soundness and completeness of constraint-based structure learning, elevating the GSC framework to consistency in the classical setting while significantly improving its empirical performance. While popular hybrid algorithms MMHC and H2PC forego asymptotic consistency for empirical performance, our HGI strategy makes no such compromise. When applied to GSC with various skeleton estimation strategies (including MMHC and H2PC), HGI significantly improves the estimation accuracy with typically negligible additional computational expense. Notably, a more recent development in hybrid structure learning is ARGES, which adaptively relaxes the restricted search space in order to ensure a search path in the space of equivalence classes (CPDAGs) to the optimal solution (Nandy et al. 2018). Though in this paper we take primary interest in improving upon the GSC framework which operates in the space of DAGs, we present preliminary simulation results in Sect. S1 of the Supplementary Information that indicate significant potential for empirical improvement to ARGES through the initialization provided by HGI.

Altogether, we combined pPC, PATH, and HGI to create the pHGS algorithm, which enjoys the skeleton estimation efficiency of pPC , the parameter tuning by PATH, and the empirical well-performance afforded by HGI. In comparison to MMHC and H2PC, pHGS learns more accurate DAGs in nearly every considered underlying network configuration with significantly reduced computational cost.

While we have empirically demonstrated a significant reduction to the number of conditional independence tests executed by pPC in comparison to PC, we have not established any concrete theoretical complexity results. Indeed, the extent of computational reduction inevitably depends on the quality of the partition with respect to the underlying structure. As such, it is of interest to determine under what conditions pPC is guaranteed to perform fewer tests than PC, and to quantify the reduction. Such an investigation is crucial to establish structure learning consistency of pPC in the sparse high-dimensional setting with multivariate Gaussian distributions. The high-dimensional Gaussian consistency of PC proved in Kalisch and Bühlmann (2007) relies on the number of conditional independence tests performed, determined by the maximum size of conditioning sets reached by PC with no

errors. The same result holds for pPC under the same assumptions if the number of tests investigated by pPC is not greater than that of PC. Note that empirically, we find pPC to always perform fewer tests than PC.

In Sect. 5, we observed superior structure learning performance by HPC and H2PC-HGI against pPC-PATH and pHGS, respectively, though not without significantly greater computational expense. We note that since the skeleton learning phase of HPC involves independently estimating the parents and children of each variable and aggregating the results, there are many obvious opportunities to more efficiently execute a synchronized global version of HPC for skeleton learning that avoids redundant computations. For instance, the first subroutine estimates a supergraph by identifying, for each node $i \in \mathbf{V}$, every node $j \in \mathbf{V} \backslash\{i\}$ that cannot be separated from $i$ by conditioning sets $\{\mathbf{X} \subseteq \mathbf{V} \backslash\{i, j\}:|\mathbf{k}| \leq 1\}$. When considered node-wise, every conditional independence test is executed twice, once in the consideration of $i$ as a neighbor of $j$ and again in the consideration of $j$ as a neighbor of $i$. A global partition-based strategy, such as the pPC algorithm with the restriction to conditioning sets $|\mathbf{k}| \leq 1$, can be utilized to substantially reduce the computational expense compared to the original formulation.

As formulated, pPC is limited to obtaining $\kappa \leq 20$ clusters as per a loose suggestion by Hartigan (1981). Note that by our design, pPC is not limited to parallel processing utility from at most $\kappa$ processors, having comparable capacity for parallel execution as PC. Nonetheless, a future direction for further improvement would be the development of an unsupervised criterion to more flexibly determine the target number of clusters that optimizes the efficiency of pPC.

# A Proofs 

In this section, we prove Theorems 2 and 3.

## A. 1 Proof of Theorem 2

The proof of Theorem 2 regarding the soundness and completeness of the pPC algorithm (Algorithm 2) follows from the thorough investigation of the criterion expressed in Eq. (4) by the pPC algorithm.

## Proof of Theorem 2

Let $\mathbf{c}$ be any clustering labels obtained in the clustering step. Let $\hat{G}_{1}$ denote the estimated structure after estimating edges within clusters at line 3 , and $\hat{G}$ denote the final estimated skeleton at line 18 .

We first show that every truly adjacent node pair (that is, adjacent in $\mathcal{G}^{*}$ ) is also adjacent in the estimated structure at every stage of Algorithm 2 following line 10. An implication of the Markov condition (Sect. 2) is that no truly adjacent pair of nodes $i, j \in \mathbf{V}$ are independent conditioned on any set of variables not containing $X_{i}$ or $X_{j}$. Thus, every truly adjacent pair of nodes belonging to the same cluster are never disconnected after being connected in the first execution of Algorithm 2 in line 2:

$$
\mathbf{N}_{i}^{\hat{G}_{1}} \supseteq\left\{X_{k} \in \mathbf{N}_{i}^{\mathcal{G}^{*}}: c_{k}=c_{i}\right\} \quad \text { for all } i \in \mathbf{V}
$$

Similarly, every truly adjacent pair of nodes belonging to different clusters will necessarily be connected in the first screening of edges between clusters, and are never disconnected. Thus, $\hat{\mathcal{G}}$ is equivalent to or a supergraph of the skeleton of $\mathcal{G}^{*}$, with

$$
\mathbf{N}_{i}^{\hat{\mathcal{G}}} \supseteq \mathbf{N}_{i}^{\mathcal{G}^{*}} \quad \text { for all } i \in \mathbf{V}
$$

Next, we show that no truly nonadjacent node pair (that is, not adjacent in $\mathcal{G}^{*}$ ) will be connected in $\hat{\mathcal{G}}$. Restating Eq. (4), for every truly nonadjacent distinct node pair $i, j \in \mathbf{V}$ there exists at least one conditioning set $\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{i}^{\hat{\mathcal{G}}} \backslash X_{j}$ or $\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{j}^{\mathcal{G}^{*}} \backslash X_{i}$ such that $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$. Thus, it is sufficient to show that for every truly nonadjacent node pair, $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$ for one such separation set $\mathbf{S}(i, j):=\mathbf{k}$ is evaluated by Algorithm 2. Consider the following for any truly nonadjacent node pair $i, j \in \mathbf{V}$.

Suppose $c_{i}=c_{j}$. If there exists a conditioning set $\mathbf{X}_{\mathbf{k}}$ such that $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$ and $c_{k}=c_{j}$ for all $k \in \mathbf{k}$, then due to Eq. (16), $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$ is evaluated by the first modified execution of PC in line 2. Otherwise, if $\exists k \in \mathbf{k}$ such that $c_{k} \neq c_{j}$, then for any and every conditioning set $\mathbf{X}_{\mathbf{k}}$ such that $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}, \mathbf{X}_{\mathbf{k}}$ satisfies criteria (a) of Eq. (9). In such a case, because of Eq. (17), $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$ for one such conditioning set $\mathbf{X}_{\mathbf{k}}$ is evaluated by the second modified execution of PC in line 18.

Suppose $c_{i} \neq c_{j}$. Ideally, $i$ and $j$ will be separated during the screening of edges between clusters in lines 3-17. If they are not, then for any and every conditioning set $\mathbf{X}_{\mathbf{k}}$ such that $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}, \mathbf{X}_{\mathbf{k}}$ satisfies criteria (b) of Eq. (9). Since Eq. (17) holds, $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$ for one such $\mathbf{X}_{\mathbf{k}}$ is evaluated by the second modified execution of PC in line 18 .

We have shown that Algorithm 2 correctly estimates the skeleton of $\mathcal{G}^{*}$ and, in particular, for every truly nonadjacent $i, j \in \mathbf{V},\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}$ for some conditioning set $\mathbf{X}_{\mathbf{k}}$ has been evaluated, with separation set $\mathbf{S}(i, j):=\mathbf{k}$ stored as specified in Algorithm 2. Since these separation sets are guaranteed to be accurate with conditional independence oracles, orientation of $\hat{\mathcal{G}}$ to the CPDAG of $\mathcal{G}^{*}$ in line 19 follows directly from the correctness of skel-to-cpdag (Algorithm 6) (Spirtes and Glymour 1991; Meek 1995; Kalisch and Bühlmann 2007).

# A. 2 Proof of Theorem 3 

To prove Theorem 3, we begin by stating and proving a well-known consistency result for constraint-based structure learning in the classical setting.

Lemma 2 Suppose the distribution $P$ is fixed and faithful to a $D A G$ with $C P D A G \mathcal{G}^{*}$ and $\mathcal{D}$ is data containing $n$ i.i.d. samples from $P$. Let $\hat{\mathcal{G}}_{n}\left(\alpha_{n}\right)=\left(\mathbf{V}, \hat{\mathbf{E}}_{n}\right)$ be the graph output of any exhaustive investigation of Eq. (4) followed by Algorithm 6 executed with a consistent test applied with threshold $\alpha_{n}$. Then there exists $\alpha_{n} \rightarrow 0(n \rightarrow \infty)$ such that

$$
\lim _{n \rightarrow \infty} \operatorname{Pr}\left[\hat{\mathcal{G}}_{n}\left(\alpha_{n}\right)=\mathcal{G}^{*}\right]=1
$$

Proof of Lemma 2 Define $p_{n ; i, j \mid \mathbf{k}}$ and $p_{n ; i, j \mid \mathbf{k}}^{*}$ be the $p$-values for testing the independence between $i$ and $j$ conditioned on $\mathbf{k}$ with $n$ data samples when $i$ and $j$ are and are not $d$-separated by $\mathbf{k}$ in $\mathcal{G}^{*}$, respectively. For example,

$$
\begin{aligned}
& p_{n ; i, j \mid \mathbf{k}}=\operatorname{Pr}\left(\chi_{f}^{2}>G_{n ; i j \mid \mathbf{k}}^{2} \mid\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{\mathcal{G}}\right) \text {, and } \\
& p_{n ; i, j \mid \mathbf{k}}^{*}=\operatorname{Pr}\left(\chi_{f}^{2}>G_{n ; i j \mid \mathbf{k}}^{2} \mid\left(X_{i} \nmid X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{\mathcal{G}}\right)
\end{aligned}
$$

for the $G^{2}$ test of independence. Given faithfulness, $d$-separation in $\mathcal{G}^{*}$ corresponds one-toone with conditional independence in $P$. In the case that conditional independence holds (i.e. the null hypothesis is true), $p_{n ; i, j \mid \mathbf{k}} \sim \operatorname{Unif}(0,1)$, so $\operatorname{Pr}\left(p_{n ; i, j \mid \mathbf{k}} \leq \alpha_{n}\right)=\alpha_{n} \rightarrow 0(n \rightarrow \infty)$. Whereas whenever conditional independence does not hold, the consistency of the conditional independence test implies that $p_{n ; i, j \mid \mathbf{k}}^{*}=o(1)$. As these statements hold for every $i, j \in \mathbf{V}$ and $\mathbf{k} \subseteq \mathbf{V} \backslash\{i, j\}$ with fixed $p=|\mathbf{V}|$, what follows is the existence of $\alpha_{n} \rightarrow 0$ such that the probability of making any erroneous conditional independence inference in the investigation of Eq. (4) decays to zero when $n \rightarrow \infty$. That is,

$$
\lim _{n \rightarrow \infty} \operatorname{Pr}\left[\bigcup_{i, j, \mathbf{k}}\left(p_{n ; i, j \mid \mathbf{k}} \leq \alpha_{n}\right) \cup\left(p_{n ; i, j \mid \mathbf{k}}^{*}>\alpha_{n}\right)\right]=0
$$

Given perfect conditional independence inferences asymptotically, the consistency follows straightforwardly from the correctness of Eq. (4) for skeleton identification and the soundness and completeness of Algorithm 6 for CPDAG orientation.

The proof of Theorem 3 then proceeds from Lemma 2 and its proof as follows.
Proof of Theorem 3 Equation (18) indicates the existence of some $a_{n} \rightarrow 0(n \rightarrow \infty)$ such that

$$
\lim _{n \rightarrow \infty} \operatorname{Pr}\left[\sup _{i, j, \mathbf{k}} p_{n ; i, j \mid \mathbf{k}}^{*} \leq a_{n}<\inf _{i, j, \mathbf{k}} p_{n ; i, j \mid \mathbf{k}}\right]=1
$$

That is, in the large-sample limit, $a_{n}$ perfectly discriminates true positives from true negatives. For conditional independence inferred with threshold $\alpha_{n} \geq a_{n} \geq \sup _{i, j, \mathbf{k}} p_{n ; i, j \mid \mathbf{k}}^{*}$, only false positive edges are possible. This ensures that for every truly nonadjacent distinct node pair $i, j \in \mathbf{V}$ (that is, $i-j \notin \mathbf{E}^{*}$ where $\mathbf{E}^{*}$ is the edge set of the skeleton of $\mathcal{G}^{*}$ ), at least one conditioning set that separates $i$ and $j$ is considered in the investigation of Eq. (4) and stored in Eq. (10) since Eq. (19) holds asymptotically.

$$
\max _{i-j \in \mathbf{E}^{*}} \Phi_{n ; i j} \leq \sup _{i, j, \mathbf{k}} p_{n ; i, j \mid \mathbf{k}}^{*} \leq a_{n}<\inf _{i, j, \mathbf{k}} p_{n ; i, j \mid \mathbf{k}} \leq \min _{i-j \notin \mathbf{E}^{*}} \Phi_{n ; i j}
$$

Inspecting Eq. (20) confirms the existence of a threshold value $\hat{a}_{n}$, in particular $\hat{a}_{n}=\max _{i-j \in \mathbf{E}^{*}} \Phi_{n ; i, j}$, that perfectly discriminates true positives from true negatives. Consequently, $\mathbf{E}^{*}=\left\{i-j: \Phi_{n ; i j} \leq \hat{a}_{n}\right\}$, and $\left\{\mathbf{S}_{n}(i, j): \Phi_{n ; i j}>\hat{a}_{n}\right\}$ obtains correct separation sets for complete and sound orientation to $\mathcal{G}^{*}$ according to Algorithm 6.

Having verified the existence of a threshold $\hat{a}_{n}$ that recovers $\mathcal{G}^{*}$ by thresholding $\Phi_{n}$ and $\mathbf{S}_{n}$, it remains to show that $\hat{a}_{n}$ is recovered and selected by Algorithm 3. Parameter settings $\tau=1+\sum_{i<j} \mathbb{1}\left\{\Phi_{n ; i j} \leq \alpha_{n}\right\}=1+\left|\hat{\mathbf{E}}_{n}^{(1)}\right|$ and $\alpha^{(\tau)}=0$ regulate the generation of $\alpha^{(t)}$ such that the skeletons of sequential estimates differ in sparsity by exactly one edge. The resulting values $\mathcal{A}:=\left\{\alpha^{(1)}, \ldots, \alpha^{\tau}\right\}$ correspond to the order statistics of the upper triangular elements of $\Phi_{n}$ decreasing from $\alpha_{i}^{(1)}=\alpha_{n} \geq a_{n} \geq \hat{a}_{n}$ to $\alpha_{i}^{(\tau)}=0$, ensuring that $\hat{a}_{n}=\max _{i-j \in \mathbf{E}^{*}} \Phi_{n ; i, j} \in \mathcal{A}$ and so $\mathcal{G}^{*} \in\left\{\mathcal{G}^{(t)}: t \in\{1,2, \ldots, \tau\}\right\}$. The consistency of $\phi$ ensures that in the large-sample limit, $t^{*}=\operatorname{argmax}_{t \in\{1, \ldots, \tau\}} \phi\left(\mathbf{X} \mid \hat{\mathcal{G}}^{(t)}, \mathcal{D}\right)$ selects $\alpha^{\left(t^{*}\right)}=\hat{a}_{n}$ that results in the true CPDAG $\hat{\mathcal{G}}_{n}^{(t)}\left(\alpha_{n}\right)=\mathcal{G}^{*}$, with high probability.

Given that the arguments hold for any $\alpha_{n}$ as long as $\alpha_{n} \geq a_{n}$ when $n$ is large, it is not necessary for $\alpha_{n}$ to converge to zero. In particular, Eq. (12) holds for any fixed $\alpha_{n}=\alpha \in(0,1)$.

Note that while Theorem 3 generously allows for any $\alpha_{n} \in(0,1)$, in practice a small threshold is desirable in the interest of efficiency. Since $\operatorname{Pr}\left(p_{n ; i, j \mid \mathbf{k}} \leq \alpha_{n}\right)=\alpha_{n}$, the expected length of the solution path $\tau$ may be approximately bounded between $\left|\mathbf{E}^{*}\right|$ and $\left|\mathbf{E}^{*}\right|+\frac{p(p-1)}{\tau} \alpha_{n}$. The bounds may be further regulated if approximate knowledge of the sparsity of $\mathcal{G}^{*}$ is known.

Furthermore, an inspection of the proof of Theorem 3 more generally indicates that the solution path returned by Algorithm 3 with the same $\tau$ and $\alpha^{(\tau)}$ contains the CPDAG of the underlying $\mathrm{DAG} \mathcal{G}^{*}$ if there exists some $a \leq \alpha$ such that

$$
\max _{i, j \in \mathbf{E}^{*}} \Phi_{i j} \leq a<\min _{i, j \notin \mathbf{E}^{*}} \Phi_{i j}
$$

holds when Eq. (4) is investigated with threshold $\alpha$, which can hold even for a finite sample size $n$.

# B Constraint-based edge orientation 

In this section, we review established constraint-based strategies for determining edge orientations, summarized in Algorithm 6.

We begin by discussing the work of Verma and Pearl (1991) in determining edge orientations. Under faithfulness, knowledge about the conditional independence relationships between variables can be used to detect the existence of v-structures (defined in Sect. 2.1) as follows. A triplet of nodes $(i, k, j)$ configured $i-k-j$ with $i$ and $j$ not adjacent, called an unshielded triple, is a v-structure if and only if

$$
\exists \mathbf{k} \subseteq \mathbf{V} \backslash\{i, j, k\} \text { such that }\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}
$$

It is easy to see that any other directed configuration of $i-k-j$ requires $k$ to separate $i$ and $j$ (Spirtes et al. 2000, Lemma 5.1.3). To investigate this criterion, the separation sets $\mathbf{S}$ are recorded throughout the estimation process (e.g., line 9 of Algorithm 1), defined as $\mathbf{S}(i, j)=\mathbf{S}(j, i) \subseteq \mathbf{V} \backslash\{i, j\}$ such that $\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{S}(i, j)}\right)_{P}$ for distinct nodes $i$ and $j$. Assuming accurate separation sets, every v-structure in $\mathcal{G}$ can be recovered according to Eq. (21), guaranteeing extension of the skeleton of $\mathcal{G}$ to its pattern, to which Meek's rules can be straightforwardly applied to obtain its CPDAG (see Sect. 2.1).

Alternatively, considering the Markov condition, an unshielded triple $(i, k, j)$ in $\mathcal{G}$ with adjacencies $\mathbf{N}_{i}^{\mathcal{G}}$ and $\mathbf{N}_{j}^{\mathcal{G}}$ can be correctly identified as a v-structure by investigating the criteria Eq. (21) limited to sets $\mathbf{k}$ such that $\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{i}^{\mathcal{G}}$ or sets $\mathbf{k}$ such that $\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{j}^{\mathcal{G}}$. Margaritis (2003) proposed the following criteria for identifying $(i, k, j)$ as a v-structure:

$$
\left(X_{i} \notin X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P} \quad \text { for all } \mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{i}^{\mathcal{G}} \quad \text { or for all } \mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{j}^{\mathcal{G}} \quad \text { with } k \in \mathbf{k}
$$

investigating the smaller of $\left|\mathbf{N}_{i}^{\mathcal{G}}\right|$ and $\left|\mathbf{N}_{j}^{\mathcal{G}}\right|$ for efficiency. For constraint-based algorithms that do not record $\mathbf{S}$, we empirically prefer investigating Eq. (22) over Eq. (21) for both general well-performance and efficiency. As with Eq. (21), the correctness of Eq. (22) guarantees detection of all and only the v-structures in a DAG $\mathcal{G}$ faithful to $P$ given its skeleton and conditional independence oracles.

```
Algorithm 6 skel-to-cpdag \(\left(\mathcal{G}, \mathbf{S},\left\{\mathbb{L}_{P}\right\}\right)\)
input: undirected graph \(\mathcal{G}\), and separation sets \(\mathbf{S}\) or conditional independence
    information \(\left\{\mathbb{L}_{P}\right\}\)
output: CPDAG \(\mathcal{G}\)
    initialize \(\mathbf{U}=\emptyset\) to store v-structures
    for all triplets of nodes configured \(i-k-j\) in \(\mathcal{G}\) where \(i\) and \(j\) are not
    adjacent do
        if \(\mathbf{S}\) is supplied then
            if \(k \notin \mathbf{S}(i, j)\) then
                store \((i, k, j)\) in \(\mathbf{U}\)
            end if
        else
            let \(q=\operatorname{argmin}_{l \in\{i, j\}}\left|\mathbf{N}_{l}^{\mathcal{G}}\right|\)
            if \(\left(X_{i} \nsubseteq X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}\) for all \(\mathbf{X}_{\mathbf{k}} \subseteq \mathbf{N}_{q}^{\mathcal{G}}\) with \(k \in \mathbf{k}\) then
                store \((i, k, j)\) in \(\mathbf{U}\)
            end if
        end if
    end for
    for all triplets \((i, k, j) \in \mathbf{U}\) do
        orient \(i \rightarrow k\) and \(j \rightarrow k\) in \(\mathcal{G}\)
    end for
    repeatedly apply Meek's rules R1-4 to \(\mathcal{G}\) until no rule is applicable
```


# C Details regarding statistical evaluations 

In this section, we provide basic details omitted from the body of the paper for the sake of brevity.

We develop here the notation and evaluation of the popular $G^{2}$ log-likelihood ratio test of independence for empirical estimation of conditional independence in $P$ (Spirtes et al. 2000). For further details and examples, we refer to Neapolitan (2004) 10.3.1. Let $n\left[x_{i}\right]$ denote the number of counts for which random variable $X_{i}=x_{i}$ in $n$ data samples $\mathcal{D}$, with the definition extending similarly to $n\left[x_{i}, x_{j}\right]$ and so on. For $\mathbf{k} \subseteq \mathbf{V}$, let $n\left[x_{i}, x_{j}, \mathbf{x}_{\mathbf{k}}\right]$ denote the number of counts for which $X_{i}=x_{i}, X_{j}=x_{j}$, and $\mathbf{X}_{\mathbf{k}}$ attains one of its $\prod_{k \in \mathbf{k}} r_{k}$ state configurations $\mathbf{x}_{\mathbf{k}}$ in $\mathcal{D}$. Then the $G^{2}$ test statistic for testing $H_{0}:\left(X_{i} \perp X_{j} \mid X_{k}\right)_{P}$ is calculated as

$$
G_{i j \mid \mathbf{k}}^{2}=2 \sum_{x_{i}, x_{j}, \mathbf{x}_{\mathbf{k}}} n\left[x_{i}, x_{j}, \mathbf{x}_{\mathbf{k}}\right] \log \left(\frac{n\left[x_{i}, x_{j}, \mathbf{x}_{\mathbf{k}}\right] \cdot n\left[\mathbf{x}_{\mathbf{k}}\right]}{n\left[x_{i}, x_{j}\right] \cdot n\left[x_{j}, \mathbf{x}_{\mathbf{k}}\right]}\right)
$$

The equation can be applied to test marginal independence with $\mathbf{k}=\emptyset$. Under $H_{0}$, the $G^{2}$ statistic is asymptotically $\chi_{f}^{2}$ distributed with

$$
f=\left(r_{i}-1\right)\left(r_{j}-1\right) \prod_{k \in \mathbf{k}} r_{k}
$$

degrees of freedom. Then for a chosen significance level $\alpha$,

$$
\operatorname{Pr}\left(z_{f}^{2}>G_{i j \mid \mathbf{k}}^{2}\right) \leq \alpha \Rightarrow \operatorname{reject} H_{0}:\left(X_{i} \notin X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}
$$

Note that the PC algorithm (Algorithm 1) operates in a somewhat backwards fashion where the initialized complete graph on $\mathbf{V}$ assumes all distinct pairs of variables dependent rather than independent. A node pair $i$ and $j$ is then disconnected if

$$
\operatorname{Pr}\left(z_{f}^{2}>G_{i j \mid \mathbf{k}}^{2}\right)>\alpha \Rightarrow \operatorname{retain} H_{0}:\left(X_{i} \perp X_{j} \mid \mathbf{X}_{\mathbf{k}}\right)_{P}
$$

for some considered conditioning set $\mathbf{X}_{\mathbf{k}}$.
The mutual information $I\left(X_{i}, X_{j}\right)$ serves as a similarity measure between discrete random variables $X_{i}$ and $X_{j}$. It may be interpreted as the Kullback-Leibler divergence between the joint probability distribution and the product of the marginals, and it is empirically calculated for $n$ data observations as

$$
\hat{I}\left(X_{i}, X_{j}\right)=\sum_{x_{i}, x_{j}} \frac{n\left[x_{i}, x_{j}\right]}{n} \log \left(\frac{n\left[x_{i}, x_{j}\right] / n}{n\left[x_{i}\right] / n \cdot n\left[x_{j}\right] / n}\right)
$$

where $n\left[x_{i}, x_{j}\right]$ is the counts of the instances of the $n$ observations that satisfy $X_{i}=x_{i}$ and $X_{j}=x_{j}$, with corresponding definitions for $n\left[x_{i}\right]$ and $n\left[x_{j}\right]$. It is easy to see that $G_{i j}^{2}=2 n \cdot \hat{I}\left(X_{i}, X_{j}\right)$.

Lastly, we include the penalized multinomial log-likelihood score with penalty parameter $\lambda$. Following the notation from Eq. (23), let $\boldsymbol{\pi}_{i}^{\mathcal{G}}$ represent one of the $q_{i}$ unique state configurations of $\boldsymbol{\Pi}_{i}^{\mathcal{G}}$. Given the Bayesian network DAG structure $\mathcal{G}$ and empirical data $\mathcal{D}$ from $P$, the penalized score is computed as

$$
\begin{aligned}
\phi(\mathcal{G}, \mathcal{D}) & =\sum_{i, x_{i}, \boldsymbol{\pi}_{i}^{\mathcal{G}}} n\left[x_{i}, \boldsymbol{\pi}_{i}^{\mathcal{G}}\right] \log \left(\frac{n\left[x_{i}, \boldsymbol{\pi}_{i}^{\mathcal{G}}\right]}{n\left[\boldsymbol{\pi}_{i}^{\mathcal{G}}\right]}\right)-\lambda \sum_{i}\left(r_{i}-1\right) q_{i} \\
& =\sum_{i=1}^{P}\left(\sum_{x_{i}, \boldsymbol{\pi}_{i}^{\mathcal{G}}} n\left[x_{i}, \boldsymbol{\pi}_{i}^{\mathcal{G}}\right] \log \left(\frac{n\left[x_{i}, \boldsymbol{\pi}_{i}^{\mathcal{G}}\right]}{n\left[\boldsymbol{\pi}_{i}^{\mathcal{G}}\right]}\right)-\lambda\left(r_{i}-1\right) q_{i}\right) \\
& =\sum_{i=1}^{P} \phi\left(X_{i}, \boldsymbol{\Pi}_{i}^{\mathcal{G}}\right)
\end{aligned}
$$

In the penalty term, $\sum_{i=1}^{P}\left(r_{i}-1\right) q_{i}$ encodes model complexity, encouraging sparsity in the structure of $\mathcal{G}$. In the BIC score, $\lambda=\frac{1}{2} \log (n)$ (Schwarz 1978).

Supplementary Information The online version of this article (https://doi.org/10.1007/s10994-022-061454) contains supplementary material, which is available to authorized users.

Funding This study was funded by National Science Foundation (NSF) Division of Mathematical Sciences (Grant No. 1952929).

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not

permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
