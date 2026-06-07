# Efficient Learning of Quadratic Variance Function Directed Acyclic Graphs via Topological Layers 

Wei Zhou* ${ }^{\dagger}$, Xin $\mathrm{He}^{\ddagger}$, Wei Zhong ${ }^{\dagger}$, Junhui Wang*


#### Abstract

Directed acyclic graph (DAG) models are widely used to represent casual relationships among random variables in many application domains. This paper studies a special class of non-Gaussian DAG models, where the conditional variance of each node given its parents is a quadratic function of its conditional mean. Such a class of non-Gaussian DAG models are fairly flexible and admit many popular distributions as special cases, including Poisson, Binomial, Geometric, Exponential, and Gamma. To facilitate learning, we introduce a novel concept of topological layers, and develop an efficient DAG learning algorithm. It first reconstructs the topological layers in a hierarchical fashion and then recoveries the directed edges between nodes in different layers, which requires much less computational cost than most existing algorithms in literature. Its advantage is also demonstrated in a number of simulated examples, as well as its applications to two real-life datasets, including an NBA player statistics data and a cosmetic sales data collected by Alibaba.


Key Words and Phrases: Causality, quadratic variance function, non-Gaussian DAG, structural equation model (SEM)

## 1 Introduction

Directed acyclic graph (DAG) model plays a crucial role in causal inference, which is widely used to represent casual relationships among random variables, and has a wide range of applications such as genetics, finance and machine learning [Sachs et al., 2005, Sanford and Moosa, 2012, Koller and Friedman, 2009]. Yet, learning a DAG model from observed data is challenging both methodologically and computationally, largely due to the identifiability issue and the required acyclicity.

[^0]
[^0]:    *School of Data Science, City University of Hong Kong
    ${ }^{\dagger}$ Wang Yanan Institute for Studies in Economics, Department of Statistics, School of Economics, Fujian Key Lab of Statistics and MOE Key Lab of Econometrics, Xiamen University
    ${ }^{\ddagger}$ School of Statistics and Management, Shanghai University of Finance and Economics

Most of the earlier DAG learning approaches in literature ignore the identifiability issue and mainly focus on recovering the Markov equivalent class [Spirtes et al., 2000] of the DAG model. For example, the search-and-score algorithm [Chickering, 2003, Nandy et al., 2018, Zheng et al., 2018, Zhu et al., 2020] maximized the regularized likelihood for a DAG model with the best score, and the constrained-based method [Kalisch and Bühlmann, 2007, Spirtes et al., 2000, Tsamardinos et al., 2006] first conducted local conditional independence tests to learn the skeleton of the DAG model, and then determined the edge directions based on acyclicity, v-structures, and other available structures. These methods are able to recover the Markov equivalent class of the DAG model under some assumptions, such as the Markov property and the faithfulness condition. To fully identify DAG models, a number of learning algorithms have been developed under various assumptions on the underlying probability distribution of the DAG model, often represented as a structural equation model (SEM). Particularly, Peters and Bühlmann [2014] established the identifiability of linear Gaussian SEM models with equal error variances, and various algorithms have been developed accordingly [Peters and Bühlmann, 2014, Chen et al., 2019, Yuan et al., 2019]. Following this line, Shimizu et al. [2006, 2011] and Wang and Drton [2020] established the identifiability of linear non-Gaussian SEM model and developed the corresponding learning algorithms, and Bühlmann et al. [2014] and Peters et al. [2014] established the identifiability of nonparametric SEM model with additive noise assumption.

More recently, Park and Raskutti [2018] and Park and Park [2019] studied a general class of non-Gaussian DAG models, denoted as QVF-DAGs, which require that the conditional variance of each node given its parents is a quadratic function of its conditional mean. This assumption provides a natural criterion for determining the causal ordering of nodes without making additional distributional assumptions, and contains many non-Gaussian distributions as its special cases. An over-dispersion scoring (ODS; Park and Raskutti [2018]) algorithm is also developed for learning QVF-DAG, which first estimates the moral graph of the QVF-DAG model and learns the causal ordering of all nodes sequentially, and then determines the parents of each node through some sparse regression models over the nodes which are causally ahead of it. Yet the computational cost of the ODS algorithm is usually expensive even for learning a medium-size QVF-DAG model.

In this article, we propose a computationally efficient learning algorithm for QVF-DAGs based on a novel concept of topological layers. The idea is very intuitive and any DAG model can be reorganized into an equivalent topological structure with multiple layers, which automatically ensures acyclicity as a node can only have children and offsprings in its lower layers. More importantly, QVF-DAGs can be reconstructed via topological layers based on the proposed ratio-based criterion, which can be used to hierarchically determine the membership of each layer. Once the layers

are determined, parents of each node can be recovered by applying some sparse regression methods over all nodes in its upper layers.

Compared with the ODS algorithm in Park and Raskutti [2018], the proposed learning algorithm has a number of advantages. First, the topological layers in the proposed algorithm are unique for any given QVF-DAG model, whereas the ODS algorithm needs to estimate the indeterministic causal ordering of nodes. Second, the computational cost of the proposed algorithm is much less than that of the ODS algorithm, especially in some wide yet shallow QVF-DAG models, such as a hub graph, which has attracted tremendous interest in network analysis as it is a main building block for many network architectures. More precisely, to learn a hub graph with $p$ nodes and $n$ samples as in Figure 2, the computational complexity of our proposed algorithm is of order $O(n p)$, which is much more efficient than the ODS algorithm, whose computational complexity is of order $O\left(n p^{2}\right)$ [Park and Raskutti, 2018].

The rest of this paper is organized as follows. Section 2 introduces QVF-DAGs and the concept of topological layers, and the reconstruction criterion of QVF-DAGs based on topological layers. Section 3 provides the details of the proposed learning algorithm for QVF-DAGs. Numerical experiments on simulated examples are conducted in Section 4 to demonstrate the advantages of the proposed algorithm compared with some existing competitors. Section 5 applies the proposed algorithm to analyze two real-life datasets, including an NBA player statistics data and a cosmetic sales data from Alibaba company. A summary is given in Section 6, and Appendix is devoted to some computational details and technical proofs.

# 2 QVF-DAG and topological layers 

### 2.1 QVF-DAG

DAG models are widely used to encode joint distribution of a random vector $\left(X_{1}, \ldots, X_{p}\right)$. Precisely, let $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ denote a DAG, where $\mathcal{V}=\{1, \ldots, p\}$ represents a set of nodes associated with variables $X=\left(X_{j}\right)_{j \in \mathcal{V}}$, and $\mathcal{E} \subset \mathcal{V} \times \mathcal{V}$ denote a set of directed edges without directed cycles. A directed edge from node $k$ to node $j$ is denoted as $k \rightarrow j$, and then node $k$ is a parent of node $j$, and the set of node $j$ 's parents is denoted as $\mathrm{pa}_{j}$. Let $X_{\mathrm{pa}_{j}}:=\left\{X_{k}: k \in \mathrm{pa}_{j} \subset \mathcal{V}\right\}$ and $X_{\mathcal{S}}:=\left\{X_{k}: k \in \mathcal{S} \subset \mathcal{V}\right\}$ for any subset $\mathcal{S}$ of $\mathcal{V}$. We assume that the joint distribution $P(X)$ satisfies the Markov property with respect to $\mathcal{G}$, and thus it allows for the following factorization,

$$
P(X)=\prod_{j \in \mathcal{V}} P\left(X_{j} \mid X_{\mathrm{pa}_{j}}\right)
$$

where $P\left(X_{j} \mid X_{\mathrm{pa}_{j}}\right)$ denotes the conditional distribution of $X_{j}$ given its parents $X_{\mathrm{pa}_{j}}$.
In this paper, we focus on the non-Gaussian DAG models with the quadratic variance function (QVF) property [Park and Raskutti, 2018]. Specifically, we assume that $P\left(X_{j} \mid X_{\mathrm{pa}_{j}}\right)$ satisfies the QVF property that there exist some constants $\beta_{j 1}$ and $\beta_{j 2}$ such that

$$
\operatorname{Var}\left(X_{j} \mid X_{\mathrm{pa}_{j}}\right)=\beta_{j 1} E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right]+\beta_{j 2}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right]\right)^{2}
$$

In literature, the natural exponential family with the QVF property has been extensively studied [Morris, 1982, Brown et al., 2010], which further assumes that $P\left(X_{j} \mid X_{\mathrm{pa}_{j}}\right)$ belongs to the exponential family,

$$
P\left(X_{j} \mid X_{\mathrm{pa}_{j}}\right)=\exp \left(\theta_{j} X_{j}+\sum_{k \in \mathrm{pa}_{j}} \theta_{j k} X_{k} X_{j}-B_{j}\left(X_{j}\right)-A_{j}\left(\theta_{j}+\sum_{k \in \mathrm{pa}_{j}} \theta_{j k} X_{k}\right)\right)
$$

where $A_{j}(\cdot)$ is a log-partition function, $B_{j}(\cdot)$ is determined by a given distribution in the exponential family, and the parameter $\theta_{j k} \in \mathcal{R}$ represents the effect from node $k$ to node $j$. As pointed out in Park and Raskutti [2018], the QVF-DAG model is identifiable and many popular non-Gaussian distributions satisfy both assumptions (1) and (2), including Poisson, Binomial, Geometric, Exponential, Gamma, and so on.

# 2.2 Topological layers 

We introduce a novel concept of topological layers, to reformulate a QVF-DAG model into an equivalent topological structure with multiple layers. Particularly, all root nodes in the QVF-DAG model are assigned to the top layer, and other nodes are assigned to different layers according to their longest distances to a root node. It is also important to point out that the induced topological layers are unique for the given QVF-DAG model, and the parents of each node must belong to its upper layers, thus automatically assuring acyclicity.

Suppose there are a total of $T$ layers, where $T$ denotes the longest possible distance from some node in the QVF-DAG model to a root node. Let $\mathcal{A}_{0}$ denote the set of root nodes and isolated nodes in the top layer, $\mathcal{A}_{t}$ denote the set of nodes in the $(t+1)$-th topological layer, and $\mathcal{S}_{t}=\cup_{d=0}^{t-1} \mathcal{A}_{d}$ denote all the nodes in the layers above the $(t+1)$-th layer. For any node $k \in \mathcal{A}_{t}$, its parent nodes are denoted as $\mathrm{pa}_{k}$, and thus $\mathrm{pa}_{k} \subseteq \mathcal{S}_{t}$.

Figure 1 provides a toy QVF-DAG model with three topological layers. Note that node 1 is a root node and node 4 is an isolated node, and thus both nodes belong to $\mathcal{A}_{0}$. Node 2 belongs to $\mathcal{A}_{1}$ as its longest distance to the root node is 1 , but node 3 belongs to $\mathcal{A}_{2}$ instead of $\mathcal{A}_{1}$ since its longest

Figure 1: A toy QVF-DAG model in the left panel, and its equivalent topological structure with three layers in the right panel.
![img-0.jpeg](img-0.jpeg)
path to the root node is $1 \rightarrow 2 \rightarrow 3$. Note that the topological layers is closely related with the key ideas of the depth-first search (DFS) and breadth-first search (BFS) algorithms [Cormen et al., 2009]. Specifically, the number of topological layer for a DAG is defined by the longest distance to a root node, which is similar to the DFS algorithm exploring as far as possible starting from a root node. The idea that nodes with the same distance to a root node are in the same layer is similar to that of the BFS algorithm, which explores all of the neighbor nodes of the current depth before moving to the next depth level.

# 2.3 Reconstruction of topological layers 

Let $\mathrm{nd}_{j}$ denote all the non-descendant nodes of node $j$ excluding itself, then the topological layers of a QVF-DAG model can be reconstructed under some mild technical conditions.
Condition 1: For any node $j \in \mathcal{V}$ and any set $\mathcal{S}$ satisfying that $\mathrm{pa}_{j} \not \mathcal{S} \subset \mathrm{nd}_{j}$, we have $E\left[\omega_{j}^{2}(\mathcal{S}) \operatorname{Var}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right)\right]>0$, and $\omega_{j}(\mathcal{S})=\left(\beta_{j 1}+\beta_{j 2} E\left[X_{j} \mid X_{\mathcal{S}}\right]\right)^{-1}$ exists.

Condition 1 is quite general and can be verified for many popular distributions, including Poisson, Binomial, Exponential, Gamma, Geometric, Negative Binomial and so on. The first part of Condition 1 requires all the parents of node $j$ should contribute to its variability, which is more general than that in Park and Raskutti [2018] assuming $\operatorname{Var}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right)>0$ for all $X_{\mathcal{S}}$, and can reduce to the identifiability condition in Park and Park [2019] when the underlying distribution is indeed Poisson. For illustration, we consider a toy example with $X_{1} \sim \operatorname{Poisson}(\lambda)$, $X_{2} \mid X_{1} \sim \operatorname{Poisson}\left(\lambda+X_{1}\right)$ and $X_{3} \mid X_{1}, X_{2} \sim \operatorname{Poisson}\left(\lambda+X_{2} 1_{\left\{X_{1} \neq 1\right\}}\right)$, where $1_{\{\cdot\}}$ is an indicator function. It can be verified that $\operatorname{Var}\left(E\left[X_{3} \mid X_{1}, X_{2}\right] \mid X_{1}=1\right)=0$ and thus the identifiability condition in Park and Raskutti [2018] is violated, but this toy example still satisfies the

first part of Condition 1. The second part of Condition 1 requires that $\beta_{j 1}$ and $\beta_{j 2}$ should satisfy $\beta_{j 1}+\beta_{j 2} E\left[X_{j} \mid X_{\mathcal{S}}\right] \neq 0$, which ensures that $\omega_{j}(\mathcal{S})=\left(\beta_{j 1}+\beta_{j 2} E\left[X_{j} \mid X_{\mathcal{S}}\right]\right)^{-1}$ is well-defined. Moreover, $\beta_{j 2}>-1$ is required to rule out some distributions, including Bernoulli and multinomial distributions, which are known to be unidentifiable in literature [Heckerman et al., 1995].

Lemma 1. Suppose that $X \in \mathcal{R}^{p}$ is generated by a QVF-DAG model and Condition 1 is satisfied. For any node $j \in \mathcal{V}$ and any set $\mathcal{S} \subseteq n d_{j}$, we have

$$
E\left[\operatorname{Var}\left(\omega_{j}(\mathcal{S}) X_{j} \mid X_{\mathcal{S}}\right)\right] \geq E\left[\omega_{j}(\mathcal{S}) X_{j}\right]
$$

provided that $\beta_{j 2}>-1$. The equality holds if and only if $p a_{j} \subseteq \mathcal{S}$.
Lemma 1 provides a crucial criterion to reconstruct the topological layers of a QVF-DAG model in a top-down fashion. Specifically, if $\mathrm{pa}_{j} \subseteq \mathcal{S}$, the conditional ratio

$$
\mathcal{R}(j, \mathcal{S}):=\frac{E\left[\operatorname{Var}\left(\omega_{j}(\mathcal{S}) X_{j} \mid X_{\mathcal{S}}\right)\right]}{E\left[\omega_{j}(\mathcal{S}) X_{j}\right]}
$$

should be exactly 1 . Motivated by this fact, Theorem 1 shows that the topological layers $\left\{\mathcal{A}_{t}\right\}_{t=0}^{T-1}$ of a QVF-DAG model, defined in Section 2.2, can be exactly reconstructed.

Theorem 1. Suppose that all the conditions of Lemma 1 are satisfied and $\mathcal{A}_{0}, \ldots, \mathcal{A}_{t-1}$ have been identified with $\mathcal{S}_{0}=\emptyset$ and $\mathcal{S}_{t}=\cup_{d=0}^{t-1} \mathcal{A}_{d}$. It then holds true that

$$
\mathcal{R}\left(j, \mathcal{S}_{t}\right) \begin{cases}=1, & \text { for any } j \in \mathcal{A}_{t} \\ \neq 1, & \text { for any } j \in \mathcal{V} \backslash\left\{\mathcal{S}_{t} \cup \mathcal{A}_{t}\right\}\end{cases}
$$

for $t=0, \ldots, T-1$, and thus the topological layers can be exactly reconstructed.
Theorem 1 provides a constructive result for the reconstruction of a general class of nonGaussian DAG models with the QVF property. Its proof follows from Lemma 1, the criterion in (4), and the assumption that a node's parents should all contribute to its variability. Particularly, for any root or isolated node $j \in \mathcal{V}$ with $\mathrm{pa}_{j}=\emptyset$, Theorem 1 shows that the topological layer $\mathcal{A}_{0}$ can be exactly reconstructed by the fact that

$$
\mathcal{R}(j, \emptyset)=\frac{E\left[\operatorname{Var}\left(\omega_{j}(\emptyset) X_{j}\right)\right]}{E\left[\omega_{j}(\emptyset) X_{j}\right]}=\frac{\operatorname{Var}\left(X_{j}\right)}{\left(\beta_{j 1}+\beta_{j 2} E\left[X_{j}\right]\right) E\left[X_{j}\right]}=1
$$

for any root or isolated node $j \in \mathcal{V}$, and $\mathcal{R}(j, \emptyset) \neq 1$ otherwise. Further, if the longest distance

of a node $j$ to a root node is $t \geq 1$, then $j \in \mathcal{A}_{t}$ by definition, and Theorem 1 guarantees that $\mathcal{R}\left(j, \mathcal{S}_{t}\right)=1$ and $\mathcal{R}\left(l, \mathcal{S}_{t}\right) \neq 1$ for any node $l$ contained in lower layers.

# 3 Proposed algorithm 

In this section, we illustrate the proposed algorithm with natural exponential family assumption in (2), but the algorithm can be adapted to learn a general QVF-DAG model as well. Motivated by Lemma 1 and Theorem 1, learning a QVF-DAG model from the observed data can be decomposed into a two-step procedure, where the topological layers can be reconstructed in a top-down fashion at the first step, and then the directed edges can be recovered by using sparse regression models in a parallel fashion.

### 3.1 Two-step learning algorithm

Given a training sample $X^{n}=\left(X_{i}^{n}\right)_{i=1}^{n}$ with $X_{i}^{n}=\left(X_{i, 1}^{n}, \ldots, X_{i, p}^{n}\right)^{T}$, we first attempt to estimate the top layer $\mathcal{A}_{0}$. Specifically, for each node $j \in \mathcal{V}$, we compute the estimated unconditional ratio,

$$
\widehat{\mathcal{R}}(j, \emptyset)=\frac{\widehat{\operatorname{Var}}\left(X_{j}\right)}{\left(\beta_{j 1}+\beta_{j 2} \widehat{E}\left[X_{j}\right]\right) \widehat{E}\left[X_{j}\right]}
$$

where $\widehat{\operatorname{Var}}\left(X_{j}\right)=\widehat{E}\left[X_{j}^{2}\right]-\left(\widehat{E}\left[X_{j}\right]\right)^{2}, \widehat{E}\left[X_{j}\right]=\frac{1}{n} \sum_{i=1}^{n} X_{i, j}^{n}$ and $\widehat{E}\left[X_{j}^{2}\right]=\frac{1}{n} \sum_{i=1}^{n}\left(X_{i, j}^{n}\right)^{2}$. By Theorem $1, \mathcal{A}_{0}$ can be estimated as $\widehat{\mathcal{A}}_{0}=\left\{j,|\widehat{\mathcal{R}}(j, \emptyset)-1| \leq \epsilon_{0}\right\}$ for some small constant $\epsilon_{0}>0$.

Suppose that the topological layers $\widehat{\mathcal{A}}_{0}, \ldots, \widehat{\mathcal{A}}_{t-1}$ have been estimated and $\widehat{\mathcal{S}}_{t}=\cup_{d=0}^{t-1} \widehat{\mathcal{A}}_{d}$, we now proceed to estimate $\mathcal{A}_{t}$. For each node $j \in \mathcal{V} \backslash \widehat{\mathcal{S}}_{t}$, we compute the estimated conditional ratio,

$$
\widehat{\mathcal{R}}\left(j, \widehat{\mathcal{S}}_{t}\right)=\frac{\widehat{E}\left[\widehat{\operatorname{Var}}\left(\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right)\right]}{\widehat{E}\left[\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{j}\right]}
$$

where $\widehat{E}\left[\widehat{\operatorname{Var}}\left(\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right)\right]=\widehat{E}\left[\widehat{\omega}_{j}^{2}\left(\widehat{\mathcal{S}}_{t}\right)\left(\widehat{E}\left[X_{j}^{2} \mid X_{\widehat{\mathcal{S}}_{t}}\right]-\left(\widehat{E}\left[X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right]\right)^{2}\right)\right], \widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right)=\left(\beta_{j 1}+\right.$ $\left.\beta_{j 2} \widehat{E}\left[X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right]\right)^{-1}$. By Theorem 1, $\mathcal{A}_{t}$ can be estimated as $\widehat{\mathcal{A}}_{t}=\left\{j,|\widehat{\mathcal{R}}\left(j, \widehat{\mathcal{S}}_{t}\right)-1| \leq \epsilon_{t}\right\}$ for some small positive constant $\epsilon_{t}$. This procedure is repeated until there are no remaining nodes, and then the topological layers of the DAG model are reconstructed. Note that the details for estimating $\widehat{\mathcal{R}}(j, \emptyset)$ and $\widehat{\mathcal{R}}\left(j, \widehat{\mathcal{S}}_{t}\right)$ may vary from one distribution to another, and we illustrate some details for both Poisson and Binomial DAGs in Appendix I, where $\widehat{E}\left[X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right]$ is estimated via the generalized linear model (GLM). The computation of $\widehat{\mathcal{R}}\left(j, \widehat{\mathcal{S}}_{t}\right)$ involves two terms, $\widehat{E}\left[X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right]$ and $\widehat{E}\left[X_{j}^{2} \mid X_{\widehat{\mathcal{S}}_{t}}\right]$,

whose computational details are provided in Appendix I.
Once all the topological layers are reconstructed, the directed edges between nodes can be recovered via standard sparse regression models [Meinshausen and Bühlmann, 2006, Yang et al., 2015] in a parallel fashion. Specifically, for each node $j \in \widehat{\mathcal{A}}_{t}$, we conduct a sparse regression of $X_{j}$ against $X_{\widehat{\mathcal{S}}_{t}}$, and any non-zero coefficient leads to a directed edge pointing from the corresponding node in $\widehat{\mathcal{S}}_{t}$ to the node $j$. This sparse regression procedure can be done for all nodes simultaneously to expedite the computation.

The proposed two-step learning algorithm for a QVF-DAG via topological layer is summarized in Algorithm 1, denoted as the TLDAG algorithm.

# Algorithm 1 

1: Input: sample matrix $X^{n} \in \mathcal{R}^{n \times p}, \widehat{\mathcal{S}}=\emptyset$, and $t=0$;
2: Until $\widehat{\mathcal{S}}=\mathcal{V}$ :
a. For any $j \in \mathcal{V} \backslash \widehat{\mathcal{S}}$, compute the ratio $\widehat{\mathcal{R}}\left(j, \widehat{\mathcal{S}}_{t}\right)=\frac{\widehat{E}\left[\widehat{\operatorname{Var}}\left(\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right)\right]}{\widehat{E}\left[\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{j}\right]}$;
b. Define $\widehat{\mathcal{A}}_{t}=\left\{j,\left|\widehat{\mathcal{R}}\left(j, \widehat{\mathcal{S}}_{t}\right)-1\right| \leq \epsilon_{t}\right\}$ and let $\widehat{\mathcal{S}}=\widehat{\mathcal{S}} \cup \widehat{\mathcal{A}}_{t}$;
c. $t \leftarrow t+1$.
3: Let $\widehat{T}=t$.
4: For any node $j \in \widehat{\mathcal{A}}_{t}$, fit a sparse regression model of $X_{j}$ against $X_{\widehat{\mathcal{S}}_{t}}$ to obtain the estimated directed edges pointing to node $j$, denoted as $\widehat{\mathcal{E}}_{j}=\left\{k \rightarrow j \mid k \in \widehat{\mathcal{S}}_{t}\right\}$.
5: Return: $\left\{\widehat{\mathcal{A}}_{t}\right\}_{t=0}^{\widehat{T}-1}$ and $\left\{\widehat{\mathcal{E}}_{j}\right\}_{j=\widehat{\mathcal{A}}_{t}}^{\widehat{\mathcal{A}}_{\widehat{T}-1}}$.

Note that Algorithm 1 can be modified to deal with the case with large $p$, by replacing the GLM model in Step 2 with the $\ell_{1}$-regularized GLM model. It is also worth pointing out that the asymptotic consistency of the TLDAG algorithm can be established following a similar treatment as in Park and Raskutti [2018] and Sun et al. [2013], with some slight modification by involving the concept of topological layers and considering the stability selection for $\epsilon_{t}$. More precisely, the assumption similar to Park and Raskutti [2018] assumes that the true ratio for all the nodes contained in the lower layers must be bounded away from $1+\eta_{\min }$ for some $\eta_{\min }>0$. Moreover, following the proof of Theorem 1 in Sun et al. [2013], we can show that the reconstructed topological layers with $\epsilon_{t}$ selected by the stability selection procedure is exactly the same as the true topological layers with high probability. Then, sparse regression, such as $\ell_{1}$-regularized regression, can be applied among each topological layer to recover directed structures among the nodes in the layers,

and the selection consistency can also be established under mild conditions as in the literature of sparse regression. Combining the above results, the consistency of the proposed algorithm can be established in the sense that it can exactly recover the true DAG with high probability.

# 3.2 Computational complexity 

In literature, the ODS algorithm [Park and Raskutti, 2018] is developed for learning QVF-DAG, and the moments ratio scoring algorithm (MRS; Park and Park [2019]) extends the ODS algorithm for a special type of QVF-DAGs, yet the computational complexities of both algorithms are of order $O\left(n p^{2}\right)$ and $O\left(n p^{3}\right)$, respectively, which are still relatively high and difficult to scale up for large-scale QVF-DAGs.

By contrast, the computational complexity of the proposed TLDAG algorithm can be much less than that of ODS and MRS, especially when dealing with shallow QVF-DAGs with $T \ll p$. For example, to learn a hub graph with $T=2$ as in Figure 2, TLDAG needs to first identify $\mathcal{A}_{0}$ and $\mathcal{A}_{1}$ and then reconstruct the parent-child relationship. More precisely, identifying $\mathcal{A}_{0}$ requires estimation of the unconditional ratio for $p$ nodes, which amounts to the complexity of order $O(n p)$, and identifying $\mathcal{A}_{1}$ requires estimation of the conditional ratio for the remaining $p-1$ nodes via GLM with only one predictor in $\mathcal{A}_{0}$, which also amounts to the complexity of order $O(n p)$. For parent-child reconstruction, we just need to fit the GLM model for each node in $\mathcal{A}_{1}$ against the only predictor in $\mathcal{A}_{0}$, which amounts to the complexity of order $O(n p)$. Therefore, the computational complexity of TLDAG is only of order $O(n p)$, which is much more efficient than both ODS and MRS algorithms.

In general, the complexity of TLDAG in estimating a random graph with $T$ layers is of order $O\left(n p(T-1)+\sum_{t=1}^{T-1} n\left(\sum_{k=0}^{t-1} a_{k}\right) a_{t}\right)$, where $a_{t}$ denotes the number of nodes in $\mathcal{A}_{t}$ and $\sum_{t=0}^{T-1} a_{t}=$ $p$. Clearly, TLDAG needs to first reconstruct the topological layers $\left\{\mathcal{A}_{t}\right\}_{t=0}^{T-1}$ in a sequential fashion, and then conduct $\ell_{1}$-regularized GLM regressions to recover the parent-child relation. Specifically, for reconstructing the topological layers, the total number of ratios needed to be computed is bounded by $O(p(T-1))$, and each ratio calculation requires $n$ samples. Thus, the complexity for reconstructing all layers is of order $O(n p(T-1))$. Furthermore, the directed parent-child structure can be recovered in a parallel fashion, and for each node, $\ell_{1}$-regularized GLM regression is fitted using coordinate descent [Friedman et al., 2010, Park and Park, 2019], with all the nodes in the upper layers as predictors, leading to the total complexity of order $O\left(\sum_{t=1}^{T-1} n\left(\sum_{k=0}^{t-1} a_{k}\right) a_{t}\right)$. It is clear that the computational complexity of TLDAG is the same as that of ODS when $T=p$, and it can be significantly better than ODS when the QVF-DAG has a shallow structure with $T<p$.

# 3.3 Tuning 

The numerical performance of the proposed TLDAG algorithm depends on the layer reconstruction parameter $\epsilon_{t}$ and the tuning parameter in the sparse regression algorithm. Whereas the latter can be determined via cross-validation, we need to modify the stability-based criterion in Sun et al. [2013] to select the optimal parameter $\epsilon_{t}$ for each layer.

The key idea is to measure the reconstruction stability by randomly splitting the training sample into two parts and comparing the disagreement between the two estimated active sets. Specifically, given a value $\epsilon_{t}$, we randomly split the training sample $\mathcal{Z}^{M}$ into two parts $\mathcal{Z}_{1}^{M}$ and $\mathcal{Z}_{2}^{M}$. Then the proposed method is applied to $\mathcal{Z}_{1}^{M}$ and $\mathcal{Z}_{2}^{M}$ and obtain two estimated active sets $\widehat{\mathcal{A}}_{1, \epsilon_{t}}$ and $\widehat{\mathcal{A}}_{2, \epsilon_{t}}$, respectively. The disagreement between $\widehat{\mathcal{A}}_{1, \epsilon_{t}}$ and $\widehat{\mathcal{A}}_{2, \epsilon_{t}}$ is measured by Cohen's kappa coefficient

$$
\kappa\left(\widehat{\mathcal{A}}_{1, \epsilon_{t}}, \widehat{\mathcal{A}}_{2, \epsilon_{t}}\right)=\frac{\operatorname{Pr}(a)-\operatorname{Pr}(e)}{1-\operatorname{Pr}(e)}
$$

where $\operatorname{Pr}(a)=\frac{n_{11}+n_{22}}{p_{n}}$ and $\operatorname{Pr}(e)=\frac{\left(n_{11}+n_{12}\right)\left(n_{11}+n_{21}\right)}{p_{n}^{2}}+\frac{\left(n_{12}+n_{22}\right)\left(n_{21}+n_{22}\right)}{p_{n}^{2}}$ with $n_{11}=\left|\widehat{\mathcal{A}}_{1, \epsilon_{t}} \cap\right.$ $\left.\widehat{\mathcal{A}}_{2, \epsilon_{t}}\right|_{, n_{12}}=\left|\widehat{\mathcal{A}}_{1, \epsilon_{t}} \cap \widehat{\mathcal{A}}_{2, \epsilon_{t}}^{C}\right|_{, n_{21}}=\left|\widehat{\mathcal{A}}_{1, \epsilon_{t}}^{C} \cap \widehat{\mathcal{A}}_{2, \epsilon_{t}}^{C}\right|, n_{22}=\left|\widehat{\mathcal{A}}_{1, \epsilon_{t}}^{C} \cap \widehat{\mathcal{A}}_{2, \epsilon_{t}}^{C}\right|$ and $|\cdot|$ denotes the set cardinality. The procedure is repeated for $B$ times and the estimated reconstruction stability is measured as

$$
\hat{s}\left(\Psi_{\epsilon_{t}}\right)=\frac{1}{B} \sum_{b=1}^{B} \kappa\left(\widehat{\mathcal{A}}_{1, \epsilon_{t}}^{b}, \widehat{\mathcal{A}}_{2, \epsilon_{t}}^{b}\right)
$$

where $\widehat{\mathcal{A}}_{1, \epsilon_{t}}^{b}$ and $\widehat{\mathcal{A}}_{2, \epsilon_{t}}^{b}$ are the estimated active sets in the $b$-th splitting. Finally, we set $\epsilon_{t}=\min \left\{\epsilon_{t}\right.$ : $\left.\frac{\hat{s}\left(\Psi_{\epsilon_{t}}\right)}{\max _{\epsilon_{t}} \hat{s}\left(\Psi_{\epsilon_{t}}\right)} \geq c\right\}$, where $c \in(0,1)$ is some given percentage. For illustration, $c=0.9$ and $B=5$ are used in all the numerical examples, and yield satisfactory performance.

## 4 Simulated experiments

In this section, we examine the numerical performance of the proposed TLDAG algorithm, and compare it against some state-of-the-art methods in terms of estimation accuracy of directed edges and computational efficiency. Specifically, five competitors are considered, including the ODS algorithm, the MRS algorithm, a direct linear non-Gaussian DAG method (DLiNGAM; Shimizu et al. [2011]), the greedy equivalence search method (GES; Chickering [2003]), and the max-min hill climbing method (MMHC; Tsamardinos et al. [2006]). We implement TLDAG, ODS and MRS in R and the source codes are available in https://github.com/WeiZHOU23/TLDAG, implementation of DLiNGAM is available on the author's website https://github.com/

cdt15/lingam, and GES and MMHC are implemented in the R packages "pcalg" [Kalisch et al., 2012] and "bnlearn" [Scutari, 2010], respectively. For GES, the output is a partial DAG, and we follow the treatment of Yuan et al., 2019 and extend the output to DAG for fair comparison. For TLDAG, the tuning parameter $\epsilon_{t}$ 's are adaptively chosen for each layer via the stability selection procedure in Section 3.3, where the grid search is conducted over grids $\left\{10^{-2+0.15 s} ; s=0, \ldots, 60\right\}$.

For comparison metrics, we use Recall, Precision, F1-score and the normalized hamming distance (HM) to evaluate the estimation accuracy. Whereas the first three metrics are standard and popularly used in literature, HM measures the number of edge insertions, deletions or flips needed to transform one graph to another [Tsamardinos et al., 2006]. Large values of Recall, Precision and F1-score and small values of HM indicate good estimation accuracy.

In all simulated examples, we generate data for QVF-DAG models with both hub graphs and random graphs. The conditional distribution of each node given its parents follows either a Poisson distribution with rate $\exp \left(\theta_{j}+\sum_{k \in \text { pa }_{j}} \theta_{j k} X_{k}\right)$, or a Binomial distribution with $N_{j}$ trials and success rate $\operatorname{logit}^{-1}\left(\theta_{j}+\sum_{k \in \text { pa }_{j}} \theta_{j k} X_{k}\right)$ ). A non-zero coefficient $\theta_{j k}$ indicates a directed edge from node $k$ to node $j$, and $\theta_{j k}=0$ otherwise.

# 4.1 Hub graphs 

The hub graph is a special type of DAGs, which consists of a hub node and a number of other nodes, and directed edges only pointing from the hub node to other nodes. In this section, we consider the following hub graphs, and similar examples have also been considered in Park and Park [2019] and Yuan et al. [2019].
Example 1 (Poisson hub graph). The generated DAG model is depicted in Figure 2. We first generate the hub node $X_{1}$ in $\mathcal{A}_{0}$ from $\operatorname{Pois}\left(\exp \left(\theta_{1}\right)\right)$, and then $X_{j}$ in $\mathcal{A}_{1}$ from $\operatorname{Pois}\left(\exp \left(\theta_{j}+\theta_{j 1} X_{1}\right)\right)$ for $j=2, \ldots, p$. The parameters $\theta_{j}$ and $\theta_{j 1}$ are generated uniformly from $[1,3]$ and $[0.1,0.5]$ for $j=1, \ldots, p$, respectively.

Figure 2: The hub graph for Examples 1 and 2.
![img-1.jpeg](img-1.jpeg)

Example 2 (Mixed hub graph). The generated DAG is the same as that in Example 1, but each

node is generated from a mixed distribution. Particularly, we first generate the hub node $X_{1}$ in $\mathcal{A}_{0}$ from $0.5 \operatorname{Pois}\left(\exp \left(\theta_{1}\right)\right)+0.5 \operatorname{Bin}\left(4 \mid \theta_{1}\right)$ and then $X_{j}$ in $\mathcal{A}_{1}$ from $0.5 \operatorname{Pois}\left(\exp \left(\theta_{j}+\theta_{j 1} X_{1}\right)\right)+$ $0.5 \operatorname{Bin}\left(4 \mid \theta_{j}+\theta_{j 1} X_{1}\right)$ for $j=2, \ldots, p$. For $X_{j}$ from the Poisson distribution, the parameters $\theta_{j}$ and $\theta_{j k}$ are generated uniformly from $[1,3]$ and $[0.1,0.3],[0.1,0.2]$ and $[0.05,0.2]$ for for $p=5$, $20, p=100$, respectively; and for $X_{j}$ from the Binomial distribution, the parameters $\theta_{j}$ and $\theta_{j k}$ are both generated uniformly from $[0.1,0.2]$ for $p=5$ and 20 , and $[0.05,0.2]$ for $p=100$. Note that the shrunk interval for large $p$ is used to avoid large values of $\theta_{j}+\theta_{j 1} X_{1}$, which leads to a contradiction with Condition 1.

In each example, the averaged performance metrics of all the competing methods over 50 independent replications as well as their standard errors are summarized in Tables 1-2.

It is evident that TLDAG yields superior numerical performance and outperforms the other five competitors in almost all the scenarios. In Table 1 with the Poisson hub graph, TLDAG yields a small HM and the largest Precision and F1-score, and the recalls of TLDAG, ODS and MRS are all close to 1 , but the other three methods have much smaller recalls. In Table 2 with the mixed hub graph, TLDAG yields the best performance in terms of Precision and F1-score, and comparable performance to the best performer in terms of HM and Recall.

# 4.2 Random graphs 

We now consider two commonly used models for the random graphs, including the Erdös and Rényi (ER) model [Erdös and Rényi, 1960] and the Barabási-Albert (BA) model [Barabási and Albert, 1999]. It is interesting to note that the BA model generates scale-free graphs, which commonly appears in many science problems, such as the gene networks.
Example 3 (Mixed ER graph). The generated DAG model is depicted in Figure 3. We set the probability of connecting an edge as $P_{E}=0.35$ for $p=5$ and 20 , and $P_{E}=0.1$ for $p=$ 100 and generate a random DAG. Then, we convert the generated random DAG into topological structure, and generate the data for the root nodes $X_{j}$ 's from $0.5 \operatorname{Pois}\left(\exp \left(\theta_{j}\right)\right)+0.5 \operatorname{Bin}\left(4 \mid \theta_{j}\right)$ and the remaining nodes $X_{k}$ 's from $0.5 \operatorname{Pois}\left(\exp \left(\theta_{k}+\sum_{l \in \mathrm{pa}_{k}} \theta_{k l} X_{l}\right)\right)+0.5 \operatorname{Bin}\left(4 \mid \theta_{k}+\sum_{l \in \mathrm{pa}_{k}} \theta_{k l} X_{l}\right)$. Precisely, the parameter $\theta_{k}$ for the Poisson distribution is generated uniformly from $[1,3]$, and $\theta_{k l}$ are generated uniformly from $[0.01,0.05],[0.005,0.015],[0.001,0.01]$ for $p=\{5,20,100\}$ respectively. The parameter $\theta_{k}$ and $\theta_{k l}$ for the Binomial distribution are all generated uniformly from $[0.01,0.05],[0.005,0.015],[0.005,0.01]$ for $p=\{5,20,100\}$ respectively.
Example 4 (Mixed BA graph). The generated DAG is the same as that in Example 3 except that we set the number of edges to be added as $e=2$ for the BA model. Additionally, the parameter $\theta_{k}$ for the Poisson distribution is generated uniformly from $[1,3]$, and $\theta_{k l}$ are generated uniformly

Table 1: The averaged performance metrics of various methods as well as their standard errors in parentheses in Example 1.


Table 2: The averaged performance metrics of various methods as well as their standard errors in parentheses in Example 2.


from $[0.01,0.03],[0.005,0.02],[0.001,0.01]$ for $p=\{5,20,100\}$ respectively. The parameter $\theta_{k}$ and $\theta_{k l}$ for the Binomial distribution are all generated uniformly from $[0.01,0.05],[0.005,0.02]$, $[0.001,0.01]$ for $p=\{5,20,100\}$ respectively.

In each example, the averaged performance metrics of all the competing methods over 50 independent replications as well as their standard errors are summarized in Tables 3-4. Note that

Figure 3: The random graph for Examples 3 and 4.
![img-2.jpeg](img-2.jpeg)
the averaged number of topological layers considered in Example 3 and 4 for the case $p=100$ are as large as 18 and 9 , respectively.

From Tables 3 and 4, it is clear that TLDAG still performs well on the random graphs. Precisely, in the both two examples, TLDAG is the best performer in terms of HM and Precision, and yields comparable performance to the other competitors in term of F1-score in almost all the scenarios. Note that TLDAG achieves the highest Precision in all scenarios, largely due to the fact that TLDAG can obtain high layer-recovery accuracy, leading to the better DAG estimation accuracy. It is worthy pointing out that DLiNGAM achieves the highest Recall in some cases, due to the fact that it tends to produce a very dense graph with many false edges, leading to small Precision. Note that the MMHC method does not return any result after running for more than 24 hours for the cases with $p=100$ in Example 4, and thus is omitted in Table 4 correspondingly.

# 4.3 Computational comparison 

We now turn to examine the computational efficiency of the proposed TLDAG algorithm. The averaged computing time (in seconds) of TLDAG, ODS and MRS in the Poisson hub graph and the mixed random graph with $p \in\{50,100,200\}$ and $n \in\{400,500\}$ is summarized in Table 5.

It is evident that TLDAG is much more efficient than other methods in terms of computational cost, where all the tuning procedures are taken into consideration. The computational efficiencies reported in Table 5 also support the computational complexity analysis in Section 3.2.

Table 3: The averaged performance metrics of various methods as well as their standard errors in parentheses in Example 3.


# 5 Real applications 

We now apply the proposed TLDAG algorithm to analyze two real examples, including an NBA player statistics data and a cosmetic sales data. The NBA player statistics data is publicly available in the R package "SportsAnalytics", and the cosmetic sales data is collected by Alibaba, one of the largest online stores in China.

Table 4: The averaged performance metrics of various methods as well as their standard errors in parentheses in Example 4.


# 5.1 NBA player data 

The NBA player statistics data consists of a number of statistics for 441 NBA players in the season 2009/2010. For illustration, we focus on 18 informative statistics, including TotalMinutesPlayed, FieldGoalsMade, FieldGoalsAttempted, ThreesMade, ThreesAttempted, FreeThrowsMade, FreeThrowsAttempted, OffensiveRebounds, TotalRebounds, Assists, Steals, Turnovers, Blocks,

Table 5: Comparison of TLDAG with ODS and MRS in terms of averaged run-time (in seconds) in Examples 1 and 4.


PersonalFouls, Disqualifications, TotalPoints, Technicals and GamesStarted.
Following the same treatment as in Park and Raskutti [2018], we assume the conditional distribution of each node given its parents follows a Poisson distribution. We then apply TLDAG to estimate the directed structures among the 18 statistics, as shown in Figure 4.

Figure 4: The estimated DAG among 18 statistics in the NBA player data.
![img-3.jpeg](img-3.jpeg)

The estimated DAG in Figure 4 has four topological layers and twenty directed edges. Compared with the estimated DAG by ODS, it contains six more directed edges and reverses six directed edges, and the difference is summarized in Figure 5.

It is evident that TLDAG produces a much more reasonable DAG compared with ODS. The added edges appear reasonable and agree with common sense. The more GamesStarted and the less Turnovers a player has, the more FieldGoalsMade and TotalRebounds he may obtain by controlling and dribbling more balls; if a player has competitive ability in Steals and Assists and makes more

Figure 5: The difference between the estimated DAGs by TLDAG and ODS.


three point shots, he is more likely to be a key player in the team and thus plays more minutes in the game. For the reversed edges, it is reasonable that a larger number of FieldGoalMade implies more total points, but the reverse is not necessarily true; if a player is in center or Power Forward position, he is likely to have more PersonalFouls, also more OffensiveRebounds, and thus more TotalRebouds. Note that the position variable is seen as a latent variable and excluded in this graph. Furthermore, strong ability of taking more TotalRebounds for a player leads to his more minutes to play, and more FieldGoalsAttempted and less PersonalFouls show the player's offensive and defensive abilities, which results in more minutes he plays in the game.

# 5.2 Alibaba cosmetic sales data 

The cosmetic sales data set consists of 35102 samples and 6 features of liquid essences of some anonymous brands, including the number of orders in one month (NO), the level of brand (LB), the star level of the seller (SLS), the place of origin (PO), the effect (EF) and the ingredient (IND). Note that NO is a continuous variable and the other five variables are discrete. Specifically, LB and SLS take values in $\{0,1,2,3,4,5\}$ and $\{0,1,2,3\}$, where a larger value indicates higher reputation for the brand and seller. PO takes value in $\{0,1,2, \ldots, 21\}$ representing 22 different countries of origin, EF takes value in $\{0,1,2, \ldots, 31\}$ for effects including moisurization, skin whitening, despeckle and so on, and IND takes value in $\{0,1,2, \ldots, 122\}$ for different ingredients such as water, polyois, essence, solubilizer and so on.

As suggested by the descriptive statistics, it is reasonable to assume that the conditional distribution of NO given its parents follows an exponential distribution, and the conditional distributions of the other five discrete variables given their parents are Binomial. We then apply the proposed TLDAG algorithm to the dataset and the estimated DAG is shown in the left panel of Figure 6, which has four topological layers and ten directed edges.

In Figure 6, some of estimated directed edges are highly interpretable. For example, a higher star level of the seller indicates a better reputation and higher customer loyalty, which leads to

Figure 6: The estimated DAGs in the cosmetic sales data by TLDAG (left) and ODS (right).
![img-4.jpeg](img-4.jpeg)
a larger number of orders; different origins have their unique materials and ingredients for the specific effect; the higher the brand level is, the more various and advanced effects the liquid essence has. The last two directed edges, however, are missed in the estimated DAG by ODS, shown in the right panel of Figure 6. It is also interesting to point out that the imposed conditional distribution assumptions may not be satisfied by the cosmetic sales data, and thus some of estimated edges are not easy to interpret, such as the seller level $\rightarrow$ the brand level/origin.

# 6 Summary 

In this paper, we propose a computationally efficient learning algorithm for a large class of nonGaussian DAGs, denoted as QVF-DAGs. The proposed algorithm is based on a novel concept of topological layers, and consists of two steps of learnings. It first reconstructs the topological layers in a hierarchical fashion, and then reconstructs the directed edges between nodes in different layers. The computational complexity of the proposed algorithm is much less than the existing learning algorithms in literature. The computational efficiency and the estimation accuracy of the proposed method are also supported by a number of simulated examples and two real applications.

## Acknowledgments

The authors thank the editor, the associate editor and the two anonymous referees for their constructive suggestions, which significantly improve this paper. The first two authors contribute

equally to this paper. Xin He's research is supported in part by NSFC-11901375 and Shanghai Pujiang Program 2019PJC051, Wei Zhong's research is supported in part by NSFC-11671334, NSFC-11922117 and Fujian Provincial Natural Science Fund for Distinguish Young Scholars (2019J06004), and Junhui Wang's research is supported in part by HK RGC Grants GRF-11303918, GRF-11300919 and GRF-11304520.

# Appendix I: Computational details 

In this part, we provide some computational details for the Poisson and Binomial DAGs. For the Poisson distribution with $\beta_{j 1}=1$ and $\beta_{j 2}=0$, we have

$$
\begin{aligned}
\widehat{E}\left[\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{j}\right] & =\widehat{E}\left(X_{j}\right)=\frac{1}{n} \sum_{i=1}^{n} X_{i, j}^{n} \\
\widehat{E}\left[\widehat{\omega}_{j}^{2}\left(\widehat{\mathcal{S}}_{t}\right) \widehat{E}\left[X_{j}^{2} \mid X_{\widehat{\mathcal{S}}_{t}}\right]\right] & =\frac{1}{n} \sum_{i=1}^{n} \exp \left(\widehat{\theta}_{j}^{\widehat{\mathcal{S}}_{t}}+\sum_{k \in \widehat{\mathcal{S}}_{t}} \widehat{\theta}_{j k}^{\widehat{\mathcal{S}}_{t}} X_{i, t}^{n}\right) \\
\text { and } \widehat{E}\left[\widehat{\omega}_{j}^{2}\left(\widehat{\mathcal{S}}_{t}\right)\left(\widehat{E}\left[X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right]\right)^{2}\right] & =\frac{1}{n} \sum_{i=1}^{n} \exp \left(2\left(\widehat{\theta}_{j}^{\widehat{\mathcal{S}}_{t}}+\sum_{k \in \widehat{\mathcal{S}}_{t}} \widehat{\theta}_{j k}^{\widehat{\mathcal{S}}_{t}} X_{i, t}^{n}\right)\right)
\end{aligned}
$$

where $\widehat{\theta}^{\widehat{\mathcal{S}}_{t}}(j)=\left(\widehat{\theta}_{j}^{\widehat{\mathcal{S}}_{t}}, \widehat{\theta}_{j}^{\widehat{\mathcal{S}}_{t}}\right)$ is the solution of the following optimization task that

$$
\widehat{\theta}^{\widehat{\mathcal{S}}_{t}}(j):=\operatorname{argmin} \frac{1}{n} \sum_{i=1}^{n}\left(-X_{i, j}^{n}\left(\theta_{j}+\sum_{k \in \widehat{\mathcal{S}}_{t}} \theta_{j k} X_{i, k}^{n}\right)+\exp \left(\theta_{j}+\sum_{k \in \widehat{\mathcal{S}}_{t}} \theta_{j k} X_{i, k}^{n}\right)\right)
$$

For the Binomial distribution with $\beta_{j 1}=1$ and $\beta_{j 2}=-\frac{1}{N}$, we have

$$
\begin{aligned}
\widehat{E}\left[\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{j}\right] & =\frac{1}{n} \sum_{i=1}^{n} \widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{i, j}^{n} \\
\widehat{E}\left[\widehat{\omega}_{j}^{2}\left(\widehat{\mathcal{S}}_{t}\right) \widehat{E}\left[X_{j}^{2} \mid X_{\widehat{\mathcal{S}}_{t}}\right]\right] & =\frac{1}{n} \sum_{i=1}^{n}\left[\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) \widehat{p}\left(X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right)\left(X_{i, j}^{n}\right)^{2}\right] \\
\text { and } \widehat{E}\left[\widehat{\omega}_{j}^{2}\left(\widehat{\mathcal{S}}_{t}\right)\left(\widehat{E}\left[X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right]\right)^{2}\right] & =\widehat{\omega}_{j}^{2}\left(\widehat{\mathcal{S}}_{t}\right)\left(\frac{1}{n} \sum_{i=1}^{n} \widehat{p}\left(X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right) X_{i, j}^{n}\right)^{2}
\end{aligned}
$$

where $\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right)=\left(1-\frac{1}{N n} \sum_{i=1}^{n} \widehat{p}\left(X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right) X_{i, j}^{n}\right)^{-1}$ with $\widehat{p}\left(X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right)=\frac{\exp \left(\widehat{\theta}_{j}^{\widehat{\mathcal{S}}_{t}} X_{i, j}^{n}+\sum_{k \in \widehat{\mathcal{S}}_{t}} \widehat{\theta}_{j k}^{\widehat{\mathcal{S}}_{t}} X_{i, k}^{n} X_{i, j}^{n}\right)\left(\frac{N_{j}}{X_{i, j}^{n}}\right)}{\exp \left(N_{j} \log \left(1+\exp \left(\widehat{\theta}_{j}^{\widehat{\mathcal{S}}_{t}}+\sum_{k \in \widehat{\mathcal{S}}_{t}} \widehat{\theta}_{j k}^{\widehat{\mathcal{S}}_{t}} X_{i, k}^{n}\right)\right)\right)}$ and $\left(\widehat{\theta}_{j}^{\widehat{\mathcal{S}}_{t}}, \widehat{\theta}_{j^{\prime}}^{\widehat{\mathcal{S}}_{t}}\right)$ denotes the solution of the following optimization task that
$\widehat{\theta}^{\widehat{\mathcal{S}}_{t}}(j):=\operatorname{argmin} \frac{1}{n} \sum_{i=1}^{n}\left(-X_{i, j}^{n}\left(\theta_{j}+\sum_{k \in \widehat{\mathcal{S}}_{t}} \theta_{j k} X_{i, k}^{n}\right)+N_{j} \log \left(1+\exp \left(\theta_{j}+\sum_{k \in \widehat{\mathcal{S}}_{t}} \theta_{j k} X_{i, k}^{n}\right)\right)\right)$
Finally, the estimated ratio for each node $j=1, \ldots, p$, can be written as

$$
\widehat{\mathcal{R}}\left(j, \widehat{\mathcal{S}}_{t}\right)=\frac{\widehat{E}\left[\widehat{\omega}_{j}^{2}\left(\widehat{\mathcal{S}}_{t}\right) \widehat{E}\left[X_{j}^{2} \mid X_{\widehat{\mathcal{S}}_{t}}\right]\right]-\widehat{E}\left[\widehat{\omega}_{j}^{2}\left(\widehat{\mathcal{S}}_{t}\right)\left(\widehat{E}\left[X_{j} \mid X_{\widehat{\mathcal{S}}_{t}}\right]\right)^{2}\right]}{\widehat{E}\left[\widehat{\omega}_{j}\left(\widehat{\mathcal{S}}_{t}\right) X_{j}\right]}
$$

# Appendix II : Proof of Lemma 1 

Simple algebra yields that

$$
\begin{aligned}
E\left[\operatorname{Var}\left(\omega_{j}(\mathcal{S}) X_{j} \mid X_{\mathcal{S}}\right)\right]-E\left[\omega_{j}(\mathcal{S}) X_{j}\right] & =E\left[\operatorname{Var}\left(\omega_{j}(\mathcal{S}) X_{j} \mid X_{\mathcal{S}}\right)-E\left[\omega_{j}(\mathcal{S}) X_{j} \mid X_{\mathcal{S}}\right]\right] \\
& =E\left[\omega_{j}^{2}(\mathcal{S})\left(\operatorname{Var}\left(X_{j} \mid X_{\mathcal{S}}\right)-\omega_{j}^{-1}(\mathcal{S}) E\left[X_{j} \mid X_{\mathcal{S}}\right]\right)\right]
\end{aligned}
$$

Then by total variance decomposition, (7) can be decomposed as

$$
\begin{aligned}
& E\left[\omega_{j}^{2}(\mathcal{S})\left(\operatorname{Var}\left(X_{j} \mid X_{\mathcal{S}}\right)-\omega_{j}^{-1}(\mathcal{S}) E\left[X_{j} \mid X_{\mathcal{S}}\right]\right)\right] \\
& =E\left[\omega_{j}^{2}(\mathcal{S})\left(\operatorname{Var}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right)+E\left[\operatorname{Var}\left(X_{j} \mid X_{\mathrm{pa}_{j}}\right) \mid X_{\mathcal{S}}\right]-\left(\beta_{j 1}+\beta_{j 2} E\left[X_{j} \mid X_{\mathcal{S}}\right]\right) E\left[X_{j} \mid X_{\mathcal{S}}\right]\right)\right] \\
& =E\left[\omega_{j}^{2}(\mathcal{S})\left(\operatorname{Var}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right)+\beta_{j 1} E\left[X_{j} \mid X_{\mathcal{S}}\right]+\beta_{j 2} E\left[E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right]^{2} \mid X_{\mathcal{S}}\right]\right.\right. \\
& \left.\left.-\left(\beta_{j 1}+\beta_{j 2} E\left[X_{j} \mid X_{\mathcal{S}}\right]\right) E\left[X_{j} \mid X_{\mathcal{S}}\right]\right)\right] \\
& =E\left[\omega_{j}^{2}(\mathcal{S})\left(\operatorname{Var}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right)+\beta_{j 2} E\left[E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right]^{2} \mid X_{\mathcal{S}}\right]-\beta_{j 2} E\left[E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right]^{2}\right)\right] \\
& =E\left[\omega_{j}^{2}(\mathcal{S})\left(\operatorname{Var}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right)+\beta_{j 2} \operatorname{Var}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right)\right)\right] \\
& =\left(1+\beta_{j 2}\right) E\left[\omega_{j}^{2}(\mathcal{S}) \operatorname{Var}\left(E\left[X_{j} \mid X_{\mathrm{pa}_{j}}\right] \mid X_{\mathcal{S}}\right)\right] .
\end{aligned}
$$

where the first equality follows from (1) and the last inequality is greater than 0 by Condition 1 if $\mathrm{pa}_{j} \nsubseteq \mathcal{S} \subset \mathrm{nd}_{j}$, and equals 0 when $\mathrm{pa}_{j} \subseteq \mathcal{S} \subseteq \mathrm{nd}_{j}$ and with the fact that $\beta_{j 2}>-1$. This completes the proof.
