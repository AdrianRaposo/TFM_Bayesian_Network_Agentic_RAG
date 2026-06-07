# HHS Public Access 

Author manuscript
Neural Comput. Author manuscript; available in PMC 2019 November 23.
Published in final edited form as:
Neural Comput. 2019 June ; 31(6): 1183-1214. doi:10.1162/neco_a_01190.

## Learning Moral Graphs in Construction of High-Dimensional Bayesian Networks for Mixed Data

Suwa Xu,<br>Department of Biostatistics, University of Florida, Gainesville, FL 32611, U.S.A.<br>Bochao Jia,<br>Lilly Corporate Center, Eli Lilly and Company, Indianapolis, IN 46285, U.S.A.<br>Faming Liang<br>Department of Statistics, Purdue University, West Lafayette, IN 47906, U.S.A.


#### Abstract

Bayesian networks have been widely used in many scientific fields for describing the conditional independence relationships for a large set of random variables. This letter proposes a novel algorithm, the so-called $p$-learning algorithm, for learning moral graphs for high-dimensional Bayesian networks. The moral graph is a Markov network representation of the Bayesian network and also the key to construction of the Bayesian network for constraint-based algorithms. The consistency of the $p$-learning algorithm is justified under the small- $n$, large- $p$ scenario. The numerical results indicate that the $p$-learning algorithm significantly outperforms the existing ones, such as the PC, grow-shrink, incremental association, semi-interleaved hiton, hill-climbing, and max-min hill-climbing. Under the sparsity assumption, the $p$-learning algorithm has a computational complexity of $O\left(p^{2}\right)$ even in the worst case, while the existing algorithms have a computational complexity of $O\left(p^{3}\right)$ in the worst case.


## 1. Introduction

Graphical models have proven to be a useful tool for describing conditional independence relationships for a large set of random variables. Two types of graphical models are commonly used, Markov networks and Bayesian networks. The Markov network, also known as the Markov random field, is a model over an undirected graph. During the past decade, the gaussian graphical model (GGM), as a special case of Markov networks, has been used in many scientific fields, from computer vision to natural language processing to genomics. Due to the mathematical tractability of the gaussian distribution, some efficient algorithms have been developed for learning the structure of GGMs-for example, graphical Lasso (Yuan \& Lin, 2007; Friedman, Hastie, \& Tibshirani, 2008), nodewise regression (Meinshausen \& Bühlmann, 2006), and $\psi$-learning (Liang, Song, \& Qiu, 2015).

[^0]
[^0]:    Correspondence should be addressed to F.L. fmliang@purdue.edu.
    S.X. and B.J. are co-first authors and contributed equally to this letter.

The Bayesian network is a model over a directed acyclic graph. Regarding the relationship between Markov networks and Bayesian networks, Pearl (1988) stated that the major weakness of Markov networks is their inability to represent induced and nontransitive dependencies; two independent variables will be directly connected by an edge merely because some other variable depends on both. As a result, many useful independencies go unrepresented in the network. Bayesian networks overcome this deficiency by using the richer language of directed graphs, where the directions of the arrows permit us to distinguish genuine dependencies from spurious dependencies induced by hypothetical observations. To illustrate this point, let us consider a set of random variables, where there can be four combinations of independence statements for any two variables. Table 1 gives an example for each of the three cases that are representable by Markov networks. The fourth case, that X and Y are marginally independent but dependent conditioned on variable Z, is not representable by a Markov network. As a compromise, the Markov network uses a cycle ② - ② - ③ to represent the mutual dependence of the three variables. However, the fourth case can be easily represented by a Bayesian network using a v-structure (defined in section 2) ② → ② ← ③, which includes two convergent directions on the edges ② - ② and ③ - ②. In Bayesian formula, this situation can be described by $$\pi(X,Y|Z) = \frac{\pi(Z|X,Y)\pi(X)\pi(Y)}{\pi(Z)} \neq \pi(X|Z)\pi(Y|Z),$$

which quite often holds for real problems. In Bayesian networks, the direction of edges represents the “parent of” relationship. For this reason, Bayesian networks have often been used in causal inference (see e.g., Spirtes, 2010).

Although the Bayesian network is statistically attractive, learning its structure can be difficult, especially under the small-n, large-p scenario, where n denotes the sample size and p denotes the number of random variables involved in the network. None of the existing algorithms developed for high-dimensional GGMs (e.g., graphical Lasso, nodewise regression, and ψ-learning) can be trivially extended to Bayesian networks due to the fundamental difference in their structures. In particular, the v-structure needs care, especially when extending a Markov network learning algorithm to Bayesian networks.

The existing Bayesian network learning algorithms can be traced to three categories: constraint based, score based, and hybrid. The constraint-based algorithms, stemming from the inductive causation (IC) algorithm (Verma & Pearl, 1991), are to learn Bayesian networks by conducting a series of conditional independence tests. The grow-shrink (GS; Margaritis, 2003), incremental association (Tsamardinos, Aliferis, & Statnikov, 2003; Yaramakala & Margaritis, 2005), and PC (Spirtes, Glymour, & Scheines, 2000) algorithms belong to this category. These algorithms basically consist of three stages: they first learn the moral graph of the Bayesian network, then identify the v-structures contained in the moral graph, and finally identify the derived directions for nonconvergent edges according to logic rules. The moral graph, which is formally defined in section 2, can be viewed as a Markov network representation of the Bayesian network. The difficulty with these algorithms is that they are not well scaled for high-dimensional problems (Aliferis, Statnikov, Tsamardinos, Mani, & Koutsoukos, 2010). They often involve some conditional tests with the conditioning

set size close to $p$, which cannot be carried out or is very unreliable when $p$ is greater than $n$. It is remarkable that under the sparsity assumption, which bounds the neighborhood size of each node, the PC algorithm has been shown by Kalisch and Bühlmann (2007) to be consistent and can execute in a polynomial time of $p$. Therefore, the PC algorithm has been considered in the literature as the state-of-the-art algorithm for learning high-dimensional Bayesian networks. Recent applications and extensions of the algorithm can be found in Colomboi, Maathuis, Kalisch, and Richardson (2012), Verdugo et al. (2013), Harris and Drton (2013), McGeachie, Chang, and Weiss (2014), Cui, Groot, and Heskes (2016), Ha, Sun, and Xie (2016), among others.

The score-based algorithms are to find a network that optimizes a selected scoring function (e.g., entropy; Herskovits \& Cooper, 1990), minimum description length (Lam \& Bacchus, 1994), and Bayesian scores (Cooper \& Herskovits, 1992; Heckerman, Geiger, \& Chickering, 1995), which measures the fitness of each feasible network to the data. Under appropriate conditions, the score-based algorithms can also be shown to be consistent (see Chickering, 2002, and Nandy, Hauser, \& Maathuis, 2016, for the low- and high-dimensional cases, respectively). Unfortunately, the task of finding a network structure that optimizes the scoring function is NP-hard (Chickering, 1996), and the search process often stops at a local optimal structure. The hybrid algorithms are to combine constraint-based and score-based algorithms to offset their respective weakness. Both the sparse candidate algorithm (Friedman, Pe'er, \& Nachman, 1999) and the max-min hill-climbing (MMHC) algorithm (Tsamardinos, Brown, \& Aliferis, 2006) belong to this category. They first restrict the parent set of each node to a smaller set and then search for the network that maximizes a scoring function subject to the constraints imposed by the restricted parent sets.

In this letter, we propose a new algorithm for learning moral graphs for high-dimensional mixed types of data. With the moral graph, the structure of the Bayesian network can be easily determined by completing the remaining stages of the constrained-based algorithms: $v$-structure identification and derived direction identification. For example, the $v$-structure can be identified using the collider set algorithm (Pellet \& Elisseeff, 2008) or local neighborhood algorithm (Margaritis \& Thrun, 2000). Upon completion of the $v$-structure identification stage, the skeleton and colliders of the Bayesian network can be identified. Given the skeleton and colliders, a maximally directed Bayesian network can be obtained following the four necessary and sufficient rules (see, e.g., Verma \& Pearl, 1992, and Kjaerulff \& Madsen, 2010), which ensure that no directed cycles and additional colliders are created in the graph. The consistency of the proposed algorithm is justified under the small$n$, large- $p$ scenario. The numerical results indicate the superiority of the proposed algorithm over the existing ones. Under the sparsity assumption, the proposed algorithm has a computational complexity bounded by $O\left(p^{2}\right)$, while the computational complexity of the existing algorithms is $O\left(p^{2+a}\right)$ for some $a>0$.

In this letter, the mixed data are restricted to those consisting of gaussian and multinomial or binomial variables only. In this scenario, the joint distribution of the mixed variables is well defined for the moral graph (see Lee \& Hastie, 2015), for which the conditional distribution of each continuous variable given the rest is still gaussian and the conditional distribution of each discrete variable given the rest is still multinomial. Therefore, all conditional

independence tests involved in the proposed algorithm can be conducted under the framework of generalized linear models (GLMs). Extension of the proposed algorithm to other types of mixed data is discussed in section 6.

The remainder of this letter is organized as follows. Section 2 gives a brief review of the theory of Bayesian networks. Section 3 describes the proposed algorithm, with the theoretical justification for its consistency deferred to the appendix. Section 4 illustrates the proposed algorithm using simulated examples along with comparisons with some existing algorithms. Section 5 reports the results for two real data examples. Section 6 concludes with a brief discussion of possible extensions of the proposed algorithm to other types of mixed data.

# 2. A Brief Review of Bayesian Network Theory 

This section gives a brief review for the Bayesian network theory required by this letter. For a full account of the theory, we refer to Jensen and Nielsen (2007) and Scutari and Denis (2015).

A Bayesian network can be represented by a directed acyclic graph (DAG) $\boldsymbol{G}=(\boldsymbol{V}, \boldsymbol{E})$, where $\boldsymbol{V}$, with a slight abuse of notation, denotes a set of $p$ nodes corresponding to the $p$ variables $X_{1}, \ldots, X_{p}$, and $\boldsymbol{E}=\left(e_{i j}\right)$ denotes the adjacency matrix or arc sets. The joint distribution of $X_{1}, \ldots, X_{p}$ is given by

$$
P(\boldsymbol{X})=\prod_{i} q\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

where $P a\left(X_{i}\right)$ denotes the parent nodes or variables of $X_{i}$ in the network, and $q(\cdot \mid \cdot)$ specifies the conditional distribution of $X_{i}$ given its parent nodes. In Bayesian networks, each node $X_{i}$ is conditionally independent of its non-descendants (the nodes for which there is no path to reach from $X_{i}$ ) given its parents. This is the so-called local Markov property of Bayesian networks. The local Markov property implies that the parents are not completely independent from their children in the Bayesian network. With Bayes's theorem, it is easy to show how information on a child can change the distribution of the parent. A convergent connection $X_{i} \rightarrow X_{k} \leftarrow X_{j}$ is called a $v$-structure if there is no arc connecting $X_{i}$ and $X_{j}$. In addition, $X_{k}$ is often called a collider node, and the convergent connection is then called an unshielded collider. The $v$-structure enables Bayesian networks to represent a type of relationship that Markov networks cannot, that is, $X_{i}$ and $X_{j}$ are marginally independent but also dependent conditional on $X_{k}$.

The Markov blanket of a node $X_{i}$ is the set consisting of the parents of $X_{i}$, the children of $X_{i}$, and the spouse nodes that share a child with $X_{i}$. The Markov blanket of a node $X_{i} \in \boldsymbol{V}$ is the minimal subset of $\boldsymbol{V}$ such that $X_{i}$ is independent of all other nodes conditioned on it. The Markov blanket is symmetric; if node $X_{i}$ is in the Markov blanket of $X_{i}$, then $X_{j}$ is also in the Markov blanket of $X_{i}$.

The moral graph, illustrated by Figure 1, is an undirected graph that is constructed by (1) connecting the nonadjacent nodes in each $v$-structure with an undirected arc and (2)

ignoring the directions of other arcs. This transformation, called moralization, provides a simple way to transform a Bayesian network into the corresponding Markov network. In the Markov network, all dependencies are explicitly represented, even those that would be implicitly implied by v-structures in a Bayesian network. In the moral graph, the neighboring set of each node forms its Markov blanket.

Finally, we give the definition for the faithfulness of graphical models. Let M denote the dependence structure of the probability distribution of $\boldsymbol{X}$-the set of conditional dependence relationships between any triplet $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}$ of subsets of $\boldsymbol{X}$. The graph $\boldsymbol{G}$ is said to be faithful or isomorphic to $\boldsymbol{M}$ if for all disjoint subsets $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}$ of $\boldsymbol{X}$, we have

$$
\boldsymbol{A} \perp_{p} \boldsymbol{B} \mid \boldsymbol{C} \Leftrightarrow \boldsymbol{A} \perp_{G} \boldsymbol{B} \mid \boldsymbol{C}
$$

where the left denotes the conditional independence in probability, and the right denotes the separation in graph (i.e., $\boldsymbol{C}$ is a separator of $\boldsymbol{A}$ and $\boldsymbol{B}$ ). For a Markov network, $\boldsymbol{C}$ is said to be a separator of $\boldsymbol{A}$ and $\boldsymbol{B}$ if for every $a \in \boldsymbol{A}$ and $b \in \boldsymbol{B}$, all paths from $a$ to $b$ have at least one node in $\boldsymbol{C}$. For Bayesian networks, $\boldsymbol{C}$ is said to be a separator of $\boldsymbol{A}$ and $\boldsymbol{B}$ if, along every path between a node in $\boldsymbol{A}$ and a node in $\boldsymbol{B}$, there is a node $v$ satisfying one of the following two conditions: (1) $v$ has converging arcs and neither $v$ nor any of its descendants is in $\boldsymbol{C}$, and (2) $v$ is in $\boldsymbol{C}$ and does not have converging arcs. The faithfulness provides a theoretical basis for establishing consistency for constraint-based algorithms.

# 3. Learning High-Dimensional Moral Graphs 

### 3.1 The $p$-Learning Algorithm.

Under the assumption of faithfulness, the moral graph can be learned via conditional independence tests $X_{i} \perp_{P} X_{b}^{1} S_{i j} \backslash\left\{X_{i}, X_{j}\right\}$ for all ordered pairs of $(i, j)$, where $S_{i j}$ denotes the Markov blanket of $X_{i}$ or $X_{j}$. If the conditional independence is true, then there is no arc between $X_{i}$ and $X_{j}$. Otherwise, $X_{i}$ and $X_{j}$ are in each other's Markov blanket.

In the literature, quite a few algorithms have been proposed for learning Markov blankets, including the grow-shrink Markov blanket (Margaritis, 2003) and incremental association (Tsamardinos, Aliferis, \& Statnikov, 2003; Yaramakala \& Margaritis, 2005) algorithms. The grow-shrink Markov blanket algorithm works like a forward selection procedure, which first continues to add new variables to the conditioning set (starting with an empty set) until the conditional independence holds or there are no more variables to add, and then shrinks the conditioning set by removing the variables outside the blanket. The incremental association algorithm is an enhancement of the grow-shrink Markov blanket algorithm, which reduces the number of conditional tests by arranging the order of the variables to add to the conditioning set. A fundamental problem with these algorithms is that they often need to perform some conditional tests with the size of the conditioning set close to $p$. When $p$ is greater than $n$, such tests cannot be carried out or are very unreliable. Their computational complexity is $O\left(p^{2+a}\right)$ for some $0<a \leq 1$, where the factor $p^{a}$ accounts for the number of conditional independence tests performed for each of $p^{2}$ pairs of nodes. In the worst case that the graph is fully connected, $a$ is equal to 1 for all the algorithms.

In what follows, we present a new algorithm for learning moral graphs, which can work under the scenario $n \ll p$ and has a computational complexity of $O\left(p^{2}\right)$ even in the worst case. Instead of identifying the exact Markov blanket for each node, we propose to identify a super-Markov blanket $\overline{\boldsymbol{S}}_{i}$ for each node $X_{i}$ such that $S_{i} \subseteq \overline{\boldsymbol{S}}_{i}$ holds, where $\boldsymbol{S}_{i}$ denotes the Markov blanket of the node $X_{i}$. Let $\phi_{i j}$ denote the output of the conditional independence test $X_{i} \perp_{P} X_{i}^{\prime} \boldsymbol{S}_{i} \backslash\left\{X_{i}, X_{j}\right\}$, that is, $\phi_{i j}=1$ if the conditional independence holds and 0 otherwise. Let $\bar{\phi}_{i j}$ denote the output of the conditional independence test $X_{i} \perp_{P} X_{j} \mid \bar{S}_{i} \backslash\left\{X_{i}, X_{j}\right\}$. Theorem 1 shows that under the faithfulness assumption, $\phi_{i j}$ and $\bar{\phi}_{i j}$ are equivalent in learning moral graphs.

Theorem 1. Assume the faithfulness holds. Let $\boldsymbol{S}_{i}$ denote the Markov blanket of $\boldsymbol{X}_{i}$, and let $\overline{\boldsymbol{S}}_{i}$ denote a superset of $\boldsymbol{S}_{i}$. Then $\phi_{i j}$ and $\bar{\phi}_{i j}$ are equivalent in learning moral graphs in the sense that

$$
\phi_{i j}=1 \Leftrightarrow \bar{\phi}_{i j}=1
$$

Proof. If $\phi_{i j}=1$, then $\boldsymbol{S}_{i} \backslash\left\{X_{i}, X_{j}\right\}$ forms a separator of $X_{i}$ and $X_{j}$. Since $S_{i} \subset \overline{\boldsymbol{S}}_{i}, \bar{S}_{i} \backslash\left\{X_{i}, X_{j}\right\}$ is also a separator of $X_{i}$ and $X_{j}$. By faithfulness, we have $\bar{\phi}_{i j}=1$. If $\bar{\phi}_{i j}=1$, then $X_{i}$ and $X_{j}$ are conditionally independent and $\overline{\boldsymbol{S}}_{i} \backslash\left\{X_{i}, X_{j}\right\}$ forms a separator of $X_{i}$ and $X_{j}$. Since $\overline{\boldsymbol{S}}_{i} \subset \boldsymbol{V}, \boldsymbol{V} \backslash$ $\left\{X_{i}, X_{j}\right\}$ is also a separator of $X_{i}$ and $X_{j}$ and the conditional independence $X_{i} \perp_{P} X_{i}^{\prime} \boldsymbol{V} \backslash\left\{X_{i}\right.$, $\left.X_{j}\right\}$ holds. By the total conditioning property (property 7 in Pellet \& Elisseeff, 2008), which shows that $X_{j} \in S_{i} \Leftrightarrow X_{i} \mathcal{L}_{p} X_{j} \mid \boldsymbol{V} \backslash\left\{X_{i}, X_{j}\right\}$, we have $X_{j} \notin \boldsymbol{S}_{i}$. Therefore, $\phi i j=1$ holds.

By the symmetry of $X_{i}$ and $X_{j}$, theorem 1 also holds if $\boldsymbol{S}_{i}$ is replaced by $\boldsymbol{S}_{j}$ and $\bar{S}_{i}$ is replaced by $\overline{\boldsymbol{S}}_{j}$. Although $\phi_{i j}$ and $\bar{\phi}_{i j}$ are equivalent in learning moral graphs, the size of the superMarkov blanket $\overline{\boldsymbol{S}}_{i}$ should be as small as possible considering the power of the conditional independence tests. A large $\overline{\boldsymbol{S}}_{i}$ often reduces the power of the conditional independence test.

Based on theorem 1, we propose the so-called $p$-learning algorithm (see algorithm 1) for learning moral graphs, which provides an efficient way to learn the Markov blanket for each node simultaneously.

# Algorithm 1: $\boldsymbol{p}$-Learning Algorithm 

a. Screening for parents and children nodes: Find a superset of parentsand children for each node $X_{i}$ :
i. For each ordered pair of nodes $\left(X_{i}, X_{j}\right), i, j=1,2, \ldots, p$, conduct the marginal independence test $X_{i} \perp_{p} X_{j}$ and obtain the $p$-value.
ii. Conduct a multiple hypothesis test at level $\alpha_{1}$ to identify the pairs of nodes that are dependent. Denote the superset by $\boldsymbol{A}_{i}$ for $i=1, \ldots, p$. If the size of $\boldsymbol{A}_{i}$ is greater than $n /\left(c_{n 1} \log (n)\right)$ for a prespecified constant

$c_{n 1}$, reduce it to $n /\left(c_{n 1} \log (n)\right)$ by removing the variables having larger $p$-values in the marginal independence tests.
b. Spouse nodes amendment. For each node $X_{i}$, find the spouse nodes that are not included in $\boldsymbol{A}_{i}$, that is, find the set $\boldsymbol{B}_{i}=\left\{X_{j}: X_{j} \notin \boldsymbol{A}_{i}, \exists X_{k} \in \boldsymbol{A}_{i} \cap \boldsymbol{A}_{j}\right\}$ for $i=1$, $\ldots, p$, where $X_{j}$ is a node not connected but sharing a common neighbor with $X_{i}$. If the size of $\boldsymbol{B}_{i}$ is greater than $n /\left(c_{n 2} \log (n)\right)$ for a prespecified constant $c_{n 2}$, reduce it to $n /\left(c_{n 2} \log (n)\right)$ by removing the variables having larger $p$-values in the spouse test $X_{i} \perp_{p} X_{j} X_{k}$.
c. Screening for the moral graph. Construct the moral graph based on conditional independence tests:
i. For each ordered pair of nodes $\left(X_{i}, X_{j}\right), i, j=1,2, \ldots, p$, conduct the conditional independence test $X_{i} \perp_{p} X_{j}\left|\bar{S}_{i j} \backslash\{i, j\}\right.$, where $\bar{S}_{i j}=A_{i} \cup B_{i}$ if $\mid$ $\boldsymbol{A}_{i} \cup \boldsymbol{B}_{i} \backslash\{i, j\} \mid \leq\left|\boldsymbol{A}_{j} \cup \boldsymbol{B}_{j} \backslash\{i, j\}\right|$ and $\bar{S}_{i j}=\boldsymbol{A}_{j} \cup \boldsymbol{B}_{j}$ otherwise.
ii. Conduct a multiple hypothesis test at level $\alpha_{2}$ to identify the pairs of nodes for which they are conditionally dependent, and set the adjacency matrix $\hat{E}_{m b}$ accordingly, where $\hat{E}_{m b}$ denotes the adjacency matrix of the moral graph.

As annotated in algorithm 1, step a is to find a superset of parents and children for each node. As pointed out in the appendix, $A_{i}$ also contains the spouse nodes that are marginally dependent with $X_{i}$. Step b is to find the spouse nodes that are not included in the superset $A_{i}$, that is, the nodes that are marginally independent of $X_{i}$ but dependent on $X_{i}$ conditioned on their common child. Then for each node $X_{i}$, we have $\boldsymbol{S}_{i} \subset \boldsymbol{A}_{i} \cup \boldsymbol{B}_{i}$. Hence, we can set $\bar{S}_{i}=A_{i} \cup B_{i}$. It follows from theorem 1 that this algorithm is valid for learning moral graphs.

The $p$-values of the individual tests for the marginal independence and conditional independence were obtained via the likelihood ratio tests (LRT) under the GLM setting. The multiple hypothesis tests were done using an empirical Bayes method developed by Liang and Zhang (2008). The advantage of this method is that it allows for the general dependence between test statistics. Other multiple hypothesis tests, which account for the dependence between test statistics (e.g., Benjamini, Krieger, \& Yekutieli, 2006) can also be applied here. The performance of multiple hypothesis tests depends on their significance levels. Following from theorem 1, a slightly large value of $\alpha_{1}$ should be used to reduce the risk of $\boldsymbol{S}_{i} \not \subset \boldsymbol{A}_{i} \cup \boldsymbol{B}_{i}$. On the other hand, the power of the conditional independence tests in step c is adversely affected by the size of the superset $\bar{S}_{i}$ and thus by the value of $\alpha_{1}$. However, we also find that such an effect is not very sensitive to the size of $\bar{S}_{i}$; including a few extra variables in $\bar{S}_{i}$ will not hurt the power of the moral graph screening tests much. To balance the two ends, we suggest setting $\alpha_{1}=0.1$ or 0.2 . Throughout examples in this letter, we set $\alpha_{1}=0.1$ and $\alpha_{2}=$ 0.05 unless otherwise stated.

In the algorithm, we have restricted the sizes of $\boldsymbol{A}_{i}$ and $\boldsymbol{B}_{i}$ based on the sparsity assumption, given by condition C of section 3.2, for the high-dimensional Bayesian network. By

assuming that each conditional distribution $\boldsymbol{q}(\cdot)$ in equation 2.1 can be represented by the probability distribution function of a normal linear regression or multiclass logistic regression, we are able to bound the size of each set $\boldsymbol{A}_{i}$ by $O\left(n / \log (n)\right)$ based on the theory of sure independence screening (Fan \& Lv, 2008; Fan \& Song, 2010). (Refer to the appendix for details on theoretical development). Further, under the sparsity assumption, we are also able to bound the size of each set $\boldsymbol{B}_{i}$ by $O\left(n / \log (n)\right)$. Therefore, the size of each superset $\tilde{S}_{i}=A_{i} \cup B_{i}$ can be bounded by $O\left(n / \log (n)\right)$. With appropriate choices of $c_{n 1}$ and $c_{n 2}$, we can always have $\left|\tilde{S}_{i}\right|<n$ holding for all $i=1,2, \ldots, p$ when $n$ is reasonably large. In this letter, we set $c_{n 1}=c_{n 2}=1$ for all examples. In practice, when the sample size $n$ is small, even the size of $\boldsymbol{B}_{i}$ is smaller than the prespecified threshold, we might still conduct spouse tests to reduce its size further. Since the size of $\tilde{S}_{i}$ adversely affects the power of the moral graph screening test, a smaller $\boldsymbol{B}_{i}$ is always preferred.

Since both the marginal tests in step a and the conditional independence tests in step c need to be performed only once for each ordered pair of nodes, and the multiple hypothesis tests can be done in a linear time of the total number of $p$-values, the computational complexity of the $p$-learning algorithm is $O\left(p^{2}\right)$, which is independent of the underlying structure of the Bayesian network. In the worst case, the computational complexity of the existing algorithms is $O\left(p^{3}\right)$.

# 3.2 Consistency of the $p$-Learning Algorithm. 

This section establishes the consistency of the proposed $p$-learning algorithm. To achieve this goal, we assume that the joint distribution of the underlying true moral graph can be reexpressed as

$$
\begin{aligned}
& p(\boldsymbol{x}, \boldsymbol{y} \mid \Theta) \propto \exp \left\{-\frac{1}{2} \sum_{s=1}^{P_{c}} \sum_{t=1}^{P_{c}} \theta_{s t} x_{s} x_{t}+\sum_{s=1}^{P_{c}} \theta_{s} x_{s}+\sum_{s=1}^{P_{c}} \sum_{j=1}^{P_{d}} \rho_{s j}\left(y_{j}\right) x_{s}\right. \\
& \left.+\sum_{j=1}^{P_{d}} \sum_{r=1}^{P_{d}} \psi_{r j}\left(y_{r}, y_{j}\right)\right\}
\end{aligned}
$$

where $x_{s}$ denotes the $s$ th of $p_{c}$ continuous variables and $y_{j}$ denotes the $j$ th of $p_{d}$ discrete variables. The joint model is parameterized by $\Theta=\left[\left\{\theta_{s t}\right\},\left\{\boldsymbol{\theta}_{s}\right\},\left\{\rho_{s j}\right\},\left\{\psi_{r j}\right\}\right]$. (See Yang et al., 2014, for more general developments for the joint distribution of mixed graphical models.)

As Lee and Hastie (2015) showed, the conditional distributions of equation 3.1 are given by gaussian linear regression and multiclass logistic regressions. Therefore, all the conditional independence tests conducted in the moral graph learning and $v$-structure identification stages are well defined, which are equivalent to test whether the corresponding regression coefficients equal to zero. To be specific, the test in step a of algorithm 1 is equivalent to testing the coefficient of $X_{i}$ in the GLM,

$$
X_{i}-1+X_{j}
$$

the test in step c of algorithm 1 is equivalent to testing the coefficient of $X_{j}$ in the GLM,

$$
X_{i} \sim 1+X_{j}+\sum_{k \in \mathrm{~S}_{i j} \backslash\{i, j\}} X_{k}
$$

and the test in the $v$-structure identification stage is equivalent to testing the coefficient of $X_{j}$ in the GLM

$$
X_{i} \sim 1+X_{j}+\sum_{k \in \boldsymbol{D}_{i j}} X_{k}
$$

where $\boldsymbol{D}_{i j}$ denotes a subset of $B d\left(X_{i}\right) \backslash\left\{X_{j}\right\}$ and $B d\left(X_{i}\right)$ denotes the neighboring set of $X_{i}$ in the moral graph.

Under the GLM assumption, the consistency of algorithm 1 can be proved based on the theory of sure independence screening established in Fan and Song (2010), the theory of the $\psi$-learning algorithm established in Liang et al. (2015), and the theory established in Kalisch and Bühlmann (2007) for the PC algorithm. Parallel to the conditions assumed by the PC algorithm for the gaussian case, we assume the following conditions:
A. Faithfulness: The moral graph is faithful, for which the joint distribution can be expressed in a gaussian-multinomial distribution, equation 3.1.
B. High dimensionality: The dimension $p_{n}=O\left(\exp \left(n^{b}\right)\right)$, where $0 \leq b<(1-$ $2 \kappa) \alpha /(\alpha+2)$ for some positive constants $\kappa<1 / 2$ and $\alpha>0$, and the subscript $n$ of $p_{n}$ indicates the dependence of the dimension $p$ on the sample size $n$.
C. Sparsity: The maximum size of the Markov blanket of each node, denoted by $\tilde{q}_{n}=\max _{1 \leq j \leq p_{n}} \mid S_{i} \mid$, satisfies $\tilde{q}_{n}=O\left(n^{b}\right)$ for some constant $0 \leq b<(1-2 \kappa) \alpha /(\alpha$ $+2)$, where $S_{i}$ denotes the Markov blanket of node $i$.
D. Identifiability: The regression coefficients satisfy

$$
\inf \left\{\left|\beta_{i j}\right| C^{i}, \beta_{i j} \mid C \neq 0, i, j=1,2, \ldots, p_{n}, C \subseteq\left\{1,2, \ldots, p_{n}\right\} \backslash\{i, j\}, \mid \mathrm{Cl} \leq O(n / \log (n))\right\} \geq c_{0} n^{-\kappa}
$$

for some constant $c_{0}>0$, where $\kappa$ is as defined in condition B and $\beta_{i j C}$ denotes the true regression coefficient of $X_{j}$ in the GLM, equations 3.2, 3.3, or 3.4.

Since the $p$-learning algorithm works based on the theory of sure independence screening, we follow Fan and Song (2010) to give some conditions for GLMs (see the appendix for details) such that the resulting Bayesian network satisfies the sparsity condition C. Fan and Song (2010) showed that variable screening can be done in regression coefficients or in $p$ values of the conditional independence tests ( $\chi^{2}$ test with a degree of freedom of 1), which are equivalent to each other. For this reason, the identifiability condition, D, is given in terms of regression coefficients. Under these conditions, we show in the appendix that algorithm 1 is consistent, that is, $P\left(\bar{E}_{m b}^{(n)}=\boldsymbol{E}_{m b}^{(n)}\right) \rightarrow 1$ and $P\left(\bar{E}_{v}^{(n)}=\boldsymbol{E}_{v}^{(n)} \mid \bar{E}_{m b}^{(n)}=\boldsymbol{E}_{m b}^{(n)}\right) \rightarrow 1$ as $n \rightarrow \infty$, where $E_{m b}^{(n)}$ denotes the adjacency matrix of the moral graph, $E_{v}^{(n)}$ denotes the set of $v$-structures,

and $\overline{E}_{m b}^{(n)}$ and $\overline{E}_{v}^{(n)}$ denote the estimators of $E_{m b}^{(n)}$ and $E_{v}^{(n)}$ obtained by the $p$-learning algorithm, respectively.

# 4. Simulation Studies 

This section illustrates algorithm 1 for learning moral graphs using simulated examples, along with comparisons with a variety of existing algorithms.

### 4.1 Mixed Data with an AR(2) Structure.

Following Kalisch and Bühlmann (2007), we simulated the mixed data in the following procedure: (1) fix an order of variables, (2) randomly mark half of the variables as continuous and the rest as binary, (3) fill the adjacency matrix $\boldsymbol{E}$ with some given structures, and (4) generate the data according to the adjacency matrix in a sequential manner.

For this example, the variable $X_{1}$, which corresponds to the first node of the Bayesian network, was generated through a gaussian random variable $Y_{1} \sim N(0,1)$. We set $1 X_{1}=Y_{1}$ if $X_{1}$ was set to be continuous, and $X_{1} \sim$ Binomial $\left(n, 1 /\left(1+e^{-Y_{1}}\right)\right)$ otherwise. The other variables $X_{j}^{\prime} \mathrm{s}, j=2,3, \ldots, p$, were then sequentially generated by setting

$$
\begin{gathered}
Y_{j}=\sum_{i=1}^{p} 0.5 E_{i j} X_{i} \\
X_{j}=\left\{\begin{array}{lr}
Y_{j}+\epsilon_{j}, & \text { if } X_{j} \text { is continuous, } \\
\text { Binomial }\left(n, \frac{\exp \left(Y_{j}\right)}{1+\exp \left(Y_{j}\right)}\right), & \text { if } X_{j} \text { is binary, }
\end{array}\right.
\end{gathered}
$$

where $\epsilon_{1}, \ldots, \epsilon_{p}$ are independent and identically distributed standard gaussian random variables, and $E_{i j}$ denotes the $(i, j)$ th entry of $\boldsymbol{E}$. In this example, we first set $\boldsymbol{E}$ to be of an $\operatorname{AR}(2)$ structure given by

$$
E_{i, j}= \begin{cases}1, & \text { if } j-i=1, i=1, \ldots,(j-1) \\ 1, & \text { if } j-i=2, i=1, \ldots,(j-2) \\ 0, & \text { otherwise }\end{cases}
$$

Let $p_{c}$ and $p_{d}$ denote the numbers of continuous and discrete variables, respectively. In our simulations, we fixed $p_{c}=p_{d}=100$, while varying the sample size $n$ at four values: $n=100$, 200,500 , and 1000 . For each value of $n, 10$ data sets were generated independently. The $p$ learning algorithm was first applied to this example with the default settings $\alpha_{1}=0.1$ and $\alpha_{2}$ $=0.05$ and then compared with several popular algorithms that were originally designed for learning Bayesian networks. The popular algorithms include the constraint-based algorithms such as PC, grow-shrink (GS), incremental association Markov blanket (IAMB), and semiinterleaved HITON-PC (hiton); the score-based algorithm such as hill-climbing (HC); and the hybridbased algorithm such as max-min hill-climbing (MMHC). All of these algorithms

were first employed to learn the Bayesian networks using the R package bnlearn under their default settings, and then the moral graphs were generated from the learned Bayesian networks via the function moral in the R package. The Markov blanket discovery algorithms by Gao and Ji (2017a, 2017b) can also be applied to produce a moral graph, but their codes are not available to the public and thus are not included for comparison.

To evaluate the performance of each algorithm, the receiver operating characteristic (ROC) curve was drawn. The ROC curve is a plot of false-positive rate (FPR) versus true-positive rate (TPR), defined by

$$
\text { FPR }=\frac{F P}{F P+T N}, \quad \text { TPR }=\frac{T P}{T P+F N}
$$

where $T P, F P$, and $F N$ denote true positives, false positives and false negatives, respectively. Figure 2 shows the average ROC curves over 10 independent data sets for each algorithm. For the algorithm 1, in order to plot the ROC curve, we vary the value of $\alpha_{2}$. For all other algorithms, the package bnlearn provides a bootstrap method to calculate the arc presence probabilities, and the ROC curve can be plotted by varying the cutoff value of the probability. Table 2 reports the averaged area under the ROC curve and the associated standard deviation for all the algorithms. The comparison indicates the superiority of the proposed algorithm over the existing ones.

# 4.2 Sensitivity Analysis. 

The $p$-learning algorithm consists of two parameters: $\alpha_{1}$ and $\alpha_{2}$. The $\alpha_{1}$ controls the size of the super-Markov blanket for each node, while $\alpha_{2}$ controls the false discovery rate (FDR) and thus sparsity of the resulting moral graph. In general, we suggest that $\alpha_{1}$ be set to a reasonably large value in order to reduce the risk of $S_{i} \notin \hat{S}_{i}$, where $S_{i}$ and $\hat{S}_{i}$ denote the Markov blanket and super-Markov blanket of node $i$, respectively. The $\alpha_{2}$ is a user-specified parameter, which should be set by the user according to his or her own purpose. For $\alpha 1$, we conducted a sensitivity analysis with the results reported in Table 3, where the data were generated as in section 4.1 with an $\operatorname{AR}(2)$ structure and $p_{c}=p_{d}=p / 2$, and the ROC curve was plotted by fixing the value of $\alpha_{1}$ and varying the value of $\alpha_{2}$ from 0 to 1 . The results show that the performance of the $p$-learning algorithm is quite robust to the choice of $\alpha_{1}$; the AUC (area under the ROC curve) values are not much changed as $\alpha_{1}$ varies from 0.05 to 0.25 .

### 4.3 Mixed Data with General Dependence Structures.

For a thorough comparison, we also considered several other moral graph structures such as alarm, barley, ecoli, and magic, which are four popular networks obtained at the Bayesian Network Repository (http://www.bnlearn.com/bnrepository/). Since the data for these networks are not of mixed type, we simulated the mixed type of data with their known network structures as follows. We first randomly marked half of the variables as continuous and the rest as binary, filled the adjacency matrix $\boldsymbol{E}$ with the given DAG structure, and then simulated the observations in the following steps:

1. Define an ancestor set of variables $\boldsymbol{A}$, which refer to the nodes with no parents.

2. For each node $i \in \boldsymbol{A}$, generate a gaussian random variable $Y_{i} \sim \mathcal{N}(0,1)$. Set $X_{i}=$ $Y_{i}$ if $X_{i}$ is continuous, and set $X_{i} \sim$ Binomial $\left(n, 1 /\left(1+e^{-Y_{i}}\right)\right)$ otherwise.
3. Define the offspring set $\boldsymbol{O}$, which refers to the nodes with parents in the ancestor set $\boldsymbol{A}$ but $\boldsymbol{O} \cap \boldsymbol{A}=\emptyset$.
4. For each node $j \in \boldsymbol{O}$, generate $X_{j}$ by setting

$$
\begin{gathered}
Y_{j}=\sum_{i \in A} 0.5 E_{i j} X_{i} \\
X_{j}=\left\{\begin{array}{lr}
Y_{j}+\epsilon_{j}, & \text { if } X_{j} \text { is continuous, } \\
\text { Binomial }\left(n, \frac{\exp \left(Y_{j}\right)}{1+\exp \left(Y_{j}\right)}\right), & \text { if } X_{j} \text { is binary, }
\end{array}\right.
\end{gathered}
$$

where $\epsilon_{j}$ is a standard gaussian random variable and $E_{i j}$ denotes the $(i, j)$ entry of E.
5. Update the ancestor set by $\boldsymbol{A}=\boldsymbol{A} \cup \boldsymbol{O}$.
6. Iterate between steps 3 and 5 until all nodes are included in the ancestor set $\boldsymbol{A}$.

For each structure, 10 independent data sets were simulated. Figure 3 and Table 4 report the averaged ROC curves and areas under the curves (AUCs) produced by different algorithms for these data sets. The comparison shows that algorithm 1 outperforms other algorithms `for all types of Bayesian network structures.

# 4.4 Binary Data with an AR(2) Structure. 

For a thorough test for the performance of the proposed algorithm, we have also considered the case with binary variables only. We simulated 10 independent data sets as in section 4.1, except that all $p=200$ variables were set to binary. Figure 4 shows the average ROC curves over the 10 data sets for different algorithms, and Table 5 reports the averaged area under the ROC curve and the associated standard deviation. The comparison indicates the superiority of the proposed algorithm over the existing ones.

### 4.5 Time Complexity.

This study compares the time complexity of the proposed algorithm with the existing ones. In this study, we let the dimension $p$ increase with $n$ in the polynomial $p=0.01 n^{2}$. Such a polynomial setting facilitates the measurement of the time complexity of each algorithm in the form of $O\left(p^{4}\right)$. Different settings of $(n, p)$ were considered, including (100, 100), (141, 200), (200, 400), (264, 700), and (300, 900). For each setting of $(n, p)$, an independent data set was simulated as in section 4.1 with $p_{c}=p_{d}=p / 2$, different algorithms were applied to learn the moral graph from the data set, and the CPU time (in minutes) was recorded on a Xeon Gold 6126 CPU@2.60 GHz machine. (See Table 6 for details.) For each algorithm, the recorded CPU time was fitted by a linear regression

where σ^{2} denotes the variance of the random error and T denotes the recorded CPU time. The fitting results, including R^{2} and the OLS estimate of ν and its standard deviation, are reported in Table 6. In addition, we report in Table 6 the p-values of the tests for the hypotheses, *H*_{0} : *ν*_{*m*} ≤ *ν*_{*p*} versus *H*_{1} : *ν*_{*m*} > *ν*_{*p*}, *m* ∈ {GS, IAMB, hiton, PC, hc, mmhc}, where ν_{p} = 1.861 denotes the value of ν for the p-learning algorithm and ν_{m} denotes the value of ν for the algorithm m. The tests show that the time complexity of the p-learning algorithm is significantly lower than the existing algorithms (at a significance level of 0.05). More important, algorithm 1 outperforms the existing algorithms in recovering the underlying moral graph.

## 5. Real Example

This study aims to learn an interactive genomics network for Breast Cancer (BRCA), which incorporates gene expressions (mRNA-array data), mutations, and DNA methylations. The data set was downloaded from the Cancer Genome Atlas (TCGA) at https://tcga-data.nci.nih.gov/tcga/. For mRNA gene expressions, we used the microarray data collected from the Agilent custom 244,000 array (Agilent) platform, which includes 17,814 normalized mRNA expressions. The mutations were defined by a binary variable, where 1 stands for all the nonsilent mutations and 0 for silent mutations or not being mutated, resulting in 16,806 genes with mutations. DNA methylations were measured at the probe level, where each probe represents a CpG site. This data set consists of 27,578 CpG sites. Based on the suggestions from Zhang, Burdette, and Wang (2014), we classified methylation levels using the k-means clustering algorithm into either hyper or hypo states, which are represented as 0 and 1, respectively. In summary, the data set consists of mRNA gene expressions, mutations, and DNA methylations, which are either gaussian or binary distributed. We present our analysis for the genes that overlap with the BRCA pathways available in the Kyoto Encyclopedia of Genes and Genomes (KEGG). For mutations, we use only those included in the BRCA pathway. For methylations, we include only the CpG islands where the genes in the BRCA pathway locate. As a result, we have a data set with 129 mRNA gene expressions, 11 mutations, and 315 DNA methylations, with 287 observations.

In the genomics network, there exist some parents-children associations from mutations or DNA methylation to gene expressions, which imply that the mutations and DNA methylations can regulate gene expressions. However, according to biological knowledge, there should not exist the parents-children association among themselves; that is, any mutation-mutation, methylation-methylation, or mutation-methylation edges should not exist in the skeleton of Bayesian networks. Therefore, to generate biologically meaningful network structures, edge restriction rules should be considered when constructing mixed

graphical models. Under the framework of algorithm 1, these restriction rules can be easily incorporated into network construction.

Suppose that edges in the skeleton network can exist only among a subset of variables or they are exempt among certain types of variables. In this scenario, we define a set $\overline{\boldsymbol{E}}$, which contains all pairs of variables with possible edges. For example, in the genomic network, edges are exempted from the pairs between discrete variables; hence, $\overline{\boldsymbol{E}}$ contains all $(i, j)$ pairs, $i, j=1,2, \ldots, p$ excluding the pairs between discrete variables. Then a restricted $p$ learning algorithm can be proposed by modifying steps a.i and c.i in algorithm 1 as follows:
a. $i^{\prime}$. For each ordered pair of nodes $\left(X_{i}, X_{j}\right)$, where $(i, j) \in \overline{\boldsymbol{E}}$, conduct the marginal independence test $X_{i} \perp_{p} X_{j}$ and obtain the $p$-value.
c. $i^{\prime}$. For each ordered pair of nodes $\left(X_{i}, X_{j}\right)$, where $(i, j) \in \overline{\boldsymbol{E}}$, conduct the conditional independence test $X_{i} \perp_{p} X_{j}\left|\bar{S}_{i j}\right|\{i, j\}$, where $\bar{S}_{i j}=A_{i} \cup B_{i}$ if $\left|A_{i} \cup B_{i}\right|\{i, j\} \mid \leq\left|A_{j} \cup B_{j}\right|\{i, j\} \mid$ and $\bar{S}_{i j}=A_{j} \cup B_{j}$ otherwise.

Under the edge restriction case, the independence and conditional independence screening are conducted only for the potential pairs of nodes in the set $\overline{\boldsymbol{E}}$, and therefore the edges in the resulting network can be chosen only from the set $\overline{\boldsymbol{E}}$. However, based on the definition of moral graphs, which should link the two nodes together if they have at least one common child, we should finally add edges between the pairs $(i, j) \notin \overline{\boldsymbol{E}}$ if they share at least a common child. In applying the $p$-learning algorithm to this example, we set the parameters $\alpha_{1}=0.05$ and $\alpha_{2}=0.02$. The resulting moral network is shown in Figure 5.

From Figure 5, some hub genes, mutations, or methylations can be identified, which might play an important role in the development of breast cancer. A hub gene refers to a gene with with strong connectivity to other genes, mutations, or methylations. The hub mutation or hub methylation can be defined similarly, which might regulate the expression of quite a few genes. Table 7 lists the top five hub genes, mutations, and methylations identified by algorithm 1 for this data set, some of which have been verified in the existing literature. For example, PIK3R1 is the first hub gene, for which Cizkova et al. (2013) stated that PIK3R1 underexpression is an independent prognostic marker in breast cancer. NOTCH2 is another hub gene, for which Wang et al. (2016) claimed that NOTCH2 is downregulated and plays suppressive roles in breast cancer and the high NOTCH2 expression is shown to predict good survival for breast cancer patients. We also identified the mutation TP53, which is known to be the most frequent genetic alterations in breast cancer (Bertheau et al., 2013; Silwal-Pandit et al., 2014). Moreover, Silwal-Pandit et al. (2014) reported that TP53 mutation status is a strong marker of prognosis and has distinct prognostic relevance across different breast cancer subtypes. As for hub methylations, we identified CpG sites cg01230931, which is located in the promoter region of the gene APC. Virmani et al. (1998) mentioned that the aberrant of APC methylation had been reported in breast cancer and the frequency of APC methylation is significantly higher in breast cancer cases groups than healthy controls and also increases with tumor stage and size.

For comparison, we have applied other algorithms to this data set. Figure 6 showed the networks produced by the incremental association Markov blanket (IAMB), hill-climbing

(hc), max-min hill-climbing (mmhc), and semi-interleaved HITON-PC (hiton) algorithms under their default settings in the bnlearn package. The networks produced by the IAMB and hiton algorithms are too sparse and lose too much information about genomics associations. The network produced by the mmhc algorithm reveals some hub genes such as PIK3CD and FGF1, but it fails to identify the TP53 mutation and many important methylations. The hc algorithm produced an overly dense network, which has too many highly connected genes. Both the grow-shrink (GS) and PC algorithms produced an empty network. The comparison indicates that the proposed algorithm outperforms all others for this example.

## 6. Discussion

We have proposed a novel algorithm, the so-called p-learning algorithm, for learning moral graphs for high-dimensional Bayesian networks, and justified the consistency of the p-learning algorithm under the small-n, large-p scenario. The numerical results indicate that algorithm 1 significantly outperforms the existing ones, such as the PC, grow-shrink, IAMB, hiton-pc, hill-climbing, and max-min hill-climbing algorithms.

In this letter, we consider only the binary data and the mixed data of gaussian and binary variables. Extension of algorithm 1 to some other types of mixed data is straightforward. For example, for nongaussian continuous random variables, the nonparanormal transformation proposed by Liu, Lafferty, and Wasserman (2009) can be applied to gaussianize the data prior to applying the proposed algorithm. For Poisson random variables, the random-effect model-based transformation proposed by Jia, Xu, Xiao, Lamba, and Liang (2017) can be first applied to continuize the data, and the nonparanormal transformation can then be applied to gaussianize the data. The negative binomial data can be treated in the same way. For some other types of discrete data, we might regroup and treat them as multinomial data.

Finally, we note that the moral graph is a Markov network representation of a Bayesian network, and learning the Markov network for mixed data is of great interest in the current literature. For example, Cheng, Li, Levina, and Zhu (2013) proposed a conditional gaussian distribution-based algorithm and Fan, Liu, and Ning (2017) proposed a semiparametric latent variable algorithm to tackle the problem. The conditional gaussian distribution used in Cheng et al. (2013) is similar to equation 3.1 but includes more interaction terms. They used the nodewise regression method to estimate the Markov network structure. The semiparametric latent variable algorithm works by introducing a latent gaussian variable for each of the discrete variables and then estimating the Markov network using a regularization method. However, as Fan et al. (2017) stated, the conditional independence between the latent variables does not imply the conditional independence between the observed discrete variables. The copula PC algorithm (Cui et al. 2016) might suffer from the same problem.

F.L.'s research was partially supported by grants DMS-1612924, R01GM117597, and R01-GM126089. We thank the editor, associate editor, and two referees for their constructive comments, which led to significant improvement of this letter.

# Appendix:: Consistency of Moral Graph Learning 

To indicate that $p$ can grow as a function of $n$, we rewrite $p$ as $p_{n}$, rewrite the distribution function $P$ in (2.1) as $P^{(n)}$, and rewrite the true Bayesian network $\boldsymbol{G}$ as $\boldsymbol{G}^{(n)}=\left(\boldsymbol{V}^{(n)}, \boldsymbol{E}^{(n)}\right)$. Let $\mathscr{G}^{(n)}=\left(\mathscr{V}^{(n)}, \mathscr{E}^{(n)}\right)$ denote the marginal association network, where $\mathscr{V}^{(n)}=V^{(n)}$ and the association are measured by the coefficients of the marginal regression,

$$
X_{i} \sim 1+X_{j}, \quad i, j=1,2, \ldots, p_{n}
$$

which can be normal linear regression or multiclass logistic regression depending on the type of $X_{i}$. Let $\gamma_{i j}$ denote the coefficient of $X_{i}$ in equation A.1, which is called the marginal regression coefficient (MRC) in this letter. Then we have

$$
\mathscr{E}^{(n)}=\left\{(i, j): \gamma_{i j} \neq 0, i, j=1, \ldots, p_{n}\right\}
$$

Let $v_{n}$ denote a threshold value of the MRC, let $\widehat{\mathscr{E}}_{v_{n}}$ denote the edge set of the network obtained through MRC thresholding at $v_{n}$, and let $\widehat{\mathscr{E}}_{v_{n}}$ denote the neighborhood of node $i$ in $\widehat{\mathscr{E}}_{v_{n}}$. That is, we define

$$
\widehat{\mathscr{E}}_{v_{n}}=\left\{(i, j): \mid \widehat{\gamma}_{i j} \mid>v_{n}\right\}, \quad \text { and } \quad \widehat{\mathscr{E}}_{v, i}=\left\{j: j \neq i, \mid \widehat{\gamma}_{i j} \mid>v_{n}\right\}
$$

For convenience, we call the network with the edge set $\widehat{\mathscr{E}}_{v_{n}}$ the thresholding MRC network.

Similarly, we let $\beta_{i j}$ denote the regression coefficient of $X_{j}$ in the nodewise GLM:

$$
X_{i} \sim 1+X_{j}+\sum_{k \in V^{(n)} \backslash\{i, j\}} X_{k}
$$

Following from the total conditioning property of Bayesian networks (Pellet \& Elisseeff, 2008), which shows that $X_{j} \in \boldsymbol{S}_{i} \Leftrightarrow X_{i} \mathcal{L}_{p} X_{j} \mid \boldsymbol{V} \backslash\left\{X_{i}, X_{j}\right\}$, we have $\beta_{i j} \neq 0 \Leftrightarrow X_{j} \notin \boldsymbol{S}_{i}$. Let $\boldsymbol{E}_{m b}^{(n)}=\left\{(i, j): \beta_{i j} \neq 0, i, j=1, \ldots, p_{n}\right\}$ denote the edge set of the moral graph. We partition $\boldsymbol{E}_{m b}^{(n)}$ into two subsets: $\boldsymbol{E}_{p}^{(n)}=\left\{(i, j): \beta_{i j} \neq 0, \gamma_{i j} \neq 0\right\}$ and $\boldsymbol{E}_{s}^{(n)}=\left\{(i, j): \beta_{i j} \neq 0, \gamma_{i j}=0\right\}$ The former set contains the parent-child links as well as the spouse links for which the two spouse variables are marginally dependent. The latter set contains the spouse links for which the two spouse variables are marginally independent but dependent conditioned on their common child.

Let $\boldsymbol{Z}_{i}=\left(1, X_{i, 1}, \ldots, X_{i, q_{n}}\right)$, where $\left\{X_{i, 1}, \ldots, X_{i, q_{n}}\right\} \subset\left\{X_{1}, X_{2}, \ldots, X_{p_{n}}\right\} \backslash\left\{X_{i}\right\}$, and $q_{n}$ is bounded by $O\left(n / \log (n)\right)$. In this letter, $q_{n}$ is allowed to increase with $n$ at an appropriate rate. The regression model $X_{i} \sim \boldsymbol{Z}_{i}$ is assumed with quasi-likelihood function $-i\left(\boldsymbol{Z}_{i}^{\top} \xi_{i}, X_{i}\right)$, where $\xi_{i}$ denotes the vector of regression coefficients. Let

$$
\boldsymbol{\xi}_{i}^{n}=\arg \min _{\boldsymbol{\xi}_{i}} E I\left(\boldsymbol{Z}_{i} \xi_{i}, X_{i}\right)
$$

be the population parameter and

$$
\tilde{\xi}_{i}^{n}=\arg \min _{\xi_{i}} P_{n} I\left(Z_{i} \xi_{i}, X_{i}\right)
$$

be the maximum likelihood estimator (MLE), where $P_{n} f(X, Y)=n^{-1} \sum_{i=1}^{n} f\left(X_{i}, Y_{i}\right)$ is the empirical measure and

$$
I(X ; \theta)=-[\theta X-b(\theta)-\log c(X)]
$$

denotes the log-density function (in the canonical form) of the exponential family, where $b(\cdot)$ and $c(\cdot)$ denote some known functions. Assume that $\xi_{i}^{n}$ is an interior point of a sufficiently large, compact, and convex set $\boldsymbol{F} \in \boldsymbol{R}^{q_{n}+1}$. For any pair $\left(\boldsymbol{Z}_{i}, \boldsymbol{X}_{i}\right)$, the following conditions are assumed:

E1: The Fisher information,

$$
I\left(\xi_{i}\right)=E\left\{\left|\frac{\partial}{\partial \xi_{i}} I\left(Z_{i}^{T} \xi_{i}, X_{i}\right)\right|\right\} \frac{\partial}{\partial \xi_{i}} I\left(Z_{i}^{T} \xi_{i}, X_{i}\right)\left.\right|^{T}
$$

is finite and positive at $\xi_{i}=\xi_{i}^{n}$. Moreover, $\left\|I\left(\xi_{i}\right)\right\|_{F}=\sup _{\xi_{i}} \in \boldsymbol{F},\|z\|=1\left\|I\left(\xi_{i}\right)^{1 / 2} z\right\|$ exists, where $\|\cdot\|$ is the Euclidean norm.

E2: The function $I\left(z_{i}^{T} \xi_{i}, x_{i}\right)$ satisfies the Lipschitz property with positive constant $k_{n}$,

$$
U\left(z_{i}^{T} \xi_{i}, x_{i}\right)-I\left(z_{i}^{T} \xi_{i}, x_{i}\right) I_{n}\left(z_{i}, x_{i}\right) \leq k_{n} z_{i}^{T} \xi_{i}-z_{i}^{T} \xi_{i}^{\prime} I_{n}\left(z_{i}, x_{i}\right)
$$

for $\boldsymbol{\xi}_{i}, \boldsymbol{\xi}_{i}^{\prime} \in \boldsymbol{F}$, where $I_{n}\left(z_{i}, x_{i}\right)=I\left(z_{i}, x_{i}\right) \in \Omega_{n}$ ) with $\Omega_{n}=\left\{(z, x):|(z, x)|_{\infty} \leq K_{n}\right\}$ for some sufficiently large, positive constants $K_{n}$, and $\|\cdot\|_{\infty}$ is the supremum norm. In addition, there exists a sufficiently large constant $C$ such that with $b_{n}=C k_{n} V_{n}^{-1}(q / n)^{1 / 2}$ and

$$
\xi_{i} \in \boldsymbol{F},\left\|\xi_{i}^{\sup }-\xi_{i}^{n}\right\| \leq b_{n} \quad\left\{E\left|I\left(Z_{i}^{T} \xi, X_{i}\right)-I\left(Z_{i}^{T} \xi_{i}^{n}, X_{i}\right)\right|\left(1-I_{n}\left(Z_{i}, X_{i}\right)\right)\right\} \leq o(q / n)
$$

where $V_{n}$ is the constant given in condition E3.
E3: The function $I\left(X_{i}^{T} \xi_{i}, X_{i}\right)$ is convex in $\boldsymbol{\xi}_{i}$, satisfying

$$
E\left\{\left(\mathbf{Z}_{i}^{T} \xi_{i} \cdot X_{i}\right)-i\left(\mathbf{Z}_{i}^{T} \xi_{i}^{s} \cdot X_{i}\right)\right\} \geq V_{n}\left\|\xi_{i}-\xi_{i}^{s}\right\|^{2}
$$

for all $\left\|\xi_{i}-\xi_{i}^{s}\right\| \leq b_{n}$ and some positive constants $V_{n}$.
E4: There exist some positive constants $m_{0}, m_{1}, s_{0}, s_{1}$, and $\alpha$, such that for sufficiently large $t$,

$$
P\left(\left|X_{j}\right|>t\right) \leq\left(m_{1}-s_{1}\right) \exp \left\{-m_{0} t^{\alpha}\right\}, \quad j=1, \ldots, p_{n}
$$

where $\alpha$ is as defined in condition B of section 3.2 , and

$$
E \exp \left(b\left(\overline{\mathbf{Z}}_{i}^{T} \bar{\xi}_{i}+s_{0}\right)-b\left(\overline{\mathbf{Z}}_{i}^{T} \bar{\xi}_{i}\right)\right)+E \exp \left(b\left(\overline{\mathbf{Z}}_{i}^{T} \bar{\xi}_{i}-s_{0}\right)-b\left(\overline{\mathbf{Z}}_{i}^{T} \bar{\xi}_{i}\right)\right) \leq s_{1}
$$

where $\bar{\xi}_{i}=\left\{\beta_{i j}: \beta_{i j} \neq 0, j \in \bar{P}(i)\right\}, \bar{P}(i)=\left\{j:(i, j) \in \boldsymbol{E}_{\bar{P}}^{(n)}\right\}$, and $\bar{Z}_{i}$ contains the corresponding predictors defined in model 2.1- $\overline{\mathbf{Z}}_{i}^{T} \bar{\xi}_{i}=\beta_{i 0}+\sum_{j \in \bar{P}(i)} x_{j} \beta_{i j}$.

E5: The variance $\operatorname{Var}\left(\overline{\mathbf{Z}}_{i}^{T} \bar{\xi}_{i}\right)$ is bounded from above and below for all $i=1, \ldots, p_{n}$, where $\overline{\mathbf{Z}}_{i}$ and $\bar{\xi}_{i}$ are as specified in condition D in section 3.2 .

E6: Either $b^{\prime \prime}(\cdot)$ is bounded or $\boldsymbol{X}_{M}=\left(X_{1}, \ldots, X_{p_{n}}\right)^{T}$ follows an elliptically contoured distribution, that is,

$$
\boldsymbol{X}_{M}=\Sigma^{1 / 2} R \boldsymbol{U}
$$

and $\left|E b^{\prime}\left(\overline{\mathbf{Z}}_{i}^{T} \bar{\xi}_{i}\right)\left(\overline{\mathbf{Z}}_{i}^{T} \bar{\xi}_{i}-\beta_{i 0}\right)\right|$ is bounded, where $\boldsymbol{U}$ is uniformly distributed on the unit sphere in $p$-dimensional Euclidean space, independent of the nonnegative random variable $R, \Sigma=\operatorname{Var}\left(\boldsymbol{X}_{M}\right)$, and $\lambda_{\max }(\Sigma)=O\left(n^{\tau}\right)$ for some constant $0 \leq \tau<1-2 \kappa$, where $\kappa$ is as defined in condition B of section 3.2 .

Assumption $E 6$ implies that the largest eigenvalue of $\Sigma$ is allowed to grow with $n$, but the growth rate should be restricted. Otherwise, the resulting thresholding network can be dense.

To establish the consistency of the $p$-screening algorithm for moral graph learning, we first note that following from the definition of $\bar{P}(i)$ and condition D of section 3.2, there exists a constant $c_{2}$ such that

$$
\min _{i} \min _{j \in \bar{P}(i)}\left|y_{i j}\right| \geq c_{2} n^{-\kappa}
$$

Lemma 1 concerns the sure screening property of the thresholded association network, and lemma 2 concerns the neighborhood size of each node of the thresholded association

network. Their proofs can be simply modified from that of theorems 4 and 5 of Fan and Song (2010), respectively.

Lemma 1. Suppose that the conditions $A, B$, and E1 to E4 hold:
i. If $K_{n}=o\left(n^{(1-2 \kappa) /(\alpha+2)}\right)$, then for any $c_{3}>0$, there exists a positive constant $c_{4}$ such that

$$
P\left(\max _{1 \leq i, j \leq p_{n}}\left|\bar{\gamma}_{i j}-\gamma_{i j}\right| \geq c_{3} n^{-\kappa}\right) \leq O\left(p_{n}^{2} \exp \left(-c_{4} n^{(1-2 \kappa) \alpha /(\alpha+2)}\right)\right)=o(1)
$$

ii. If, in addition, condition D holds, then by taking $v_{n}=c_{5} n^{-\kappa}$ with $0<c_{5} \leq c_{2} / 2$, we have

$$
\begin{aligned}
& P\left(\bar{P}(i) \subseteq \overline{\mathscr{R}}_{v_{n^{\prime}} i}\right) \geq 1-O\left(p_{n} \exp \left(-c_{4} n^{(1-2 \kappa) \alpha /(\alpha+2)}\right)\right)=1-o(1) \\
& P\left(E_{\bar{P}}^{(n)} \subseteq \overline{\mathscr{R}}_{v_{n}}\right) \geq 1-O\left(p_{n}^{2} \exp \left(-c_{4} n^{(1-2 \kappa) \alpha /(\alpha+2)}\right)\right)=1-o(1)
\end{aligned}
$$

Lemma 2. Suppose that conditions $A, B$, and E1 to E6 hold. If $K_{n}=o\left(n^{(1-2 \kappa) /(\alpha+2)}\right)$, then for any $v_{n} c_{5} n^{-\kappa}$, we have

$$
P\left(\left|\overline{\mathscr{R}}_{v_{n, i}}\right| \leq O\left\{n^{2 \kappa+\tau}\right\}\right) \geq 1-O\left(p_{n} \exp \left(-c_{4} n^{(1-2 \kappa) \alpha /(\alpha+2)}\right)\right)=1-o(1)
$$

Since the exact value of $2 \kappa+\tau$ is unknown, we may bound the size of the neighboring set $\overline{\mathscr{R}}_{v_{n^{\prime}}} i$ by $O\left(n / \log (n)\right)$ in practice. However, when $n$ is large, $n / \log (n)$ can be too large. An excessively large size of the set will adversely affect the power of the moral graph screening tests. To address this issue, we propose a multiple hypothesis test-based procedure: step a.ii for preidentification of the nonzero marginal association measure. To justify this procedure, we have the following lemmas.

Lemma 3. Assume conditions $A, B, D$, and E1 to E4 hold. If $\eta_{n}=\frac{1}{2} c_{2} n^{-k}$, where $c_{2}$ is defined in equation A.6, then

$$
P\left|E_{\bar{P}}^{(n)} \subset \overline{\mathscr{R}}_{\eta_{n}}\right|=1-o(1), \quad \text { as } n \rightarrow \infty
$$

Proof. Let $A_{i j}$ denote that an error event occurs when testing the hypotheses $H_{0}: \gamma_{i j}=0$ versus $H: \gamma_{i j} \neq 0$ for variables $X_{i}$ and $X_{j}$. Let $A_{i j}^{I}$ and $A_{i j}^{I I}$ denote the false-positive and falsenegative errors, respectively. Then $A_{i j}=A_{i j}^{I} \cup A_{i j}^{I I}$, where

$$
\left\{\begin{array}{l}
\text { False-positive error } A_{i j}^{I} ;\left|\tilde{\gamma}_{i j}\right|>\frac{c_{2}}{2} n^{-\kappa} \quad \text { and } \gamma_{i j}=0 \\
\text { False-negative error } A_{i j}^{I I} ;\left|\tilde{\gamma}_{i j}\right| \leq \frac{c_{2}}{2} n^{-\kappa} \quad \text { and } \gamma_{i j} \neq 0
\end{array}\right.
$$

By equation A.6, $\min _{i j}\left|\gamma_{i j}\right| \geq c_{2} n^{-\kappa}$ for the links in $\boldsymbol{E}_{\tilde{p}}^{(n)}$. Therefore, by lemma 1.i,
$P_{1}$ Missing a link of $\boldsymbol{E}_{\tilde{p}}^{(n)}$ in $\widetilde{\mathscr{E}}_{\eta_{n}}$

$$
\leq P\left(\max _{1 \leq i, j \leq p_{n}}\left|\tilde{\gamma}_{i j}-\gamma_{i j}\right| \geq c_{2} / 2 n^{-\kappa}\right) \leq o(1)
$$

Therefore, based on lemmas 1, 2, and 3, we propose to restrict the size of the set $\boldsymbol{A}_{i}$ (in algorithm 1) for each node to be

$$
\min \left\{\left|\widetilde{\mathscr{E}}_{\eta_{n^{\prime}}}\right| ; \frac{n}{c_{n 1} \log (n)}\right\}
$$

where $c_{n 1}$ is a small constant-for example, $c_{n}=1,2$, or 3 . The value of $\eta_{n}$ can be determined through a simultaneous test for the hypotheses $H_{0}: \gamma_{i j}=0 \leftrightarrow H_{1}: \gamma_{i j} \neq 0,1 \leq i$ $\leq j \leq p_{n}$, at a significance level of $\alpha_{1}$.

Lemma 4 concerns the convergence of the MLE of the regression coefficients for which all the true predictors have been included. The lemma is a restatement of theorem 1 of Fan and Song (2010):

Lemma 4. Assume conditions $A, B$, and E1 to E3 hold. If $K_{n}=o\left(n^{(1-2 \kappa) /(\alpha+2)}\right)$, then for any constant $c_{7}>0$, there exists a constant $c_{8}>0$ such that

$$
P\left(\max _{1 \leq i \leq p_{n}}\left|\tilde{\xi}_{i}-\xi_{i}^{*}\right| \geq c_{7} n^{-\kappa}\right) \leq O\left(p_{n} \exp \left(-c_{8} n^{(1-2 \kappa) \alpha /(\alpha+2)}\right)\right)=o(1)
$$

where $\xi_{i}^{*}$ is defined in equation A. 4 and $\tilde{\xi}_{i}$ is the MLE of $\xi_{i}^{*}$.
Recall that if the Markov blanket $\boldsymbol{S}_{i}$ (of node $\boldsymbol{X}_{i}$ ) is contained in $\boldsymbol{Z}_{i}$, then $\xi_{i, i_{k}}^{*}=\beta_{i j}$ for $j \in \boldsymbol{S}_{i}$ and $X_{j}=X_{i, i_{k}}$, and $\xi_{i, i_{k}}^{*}=0$ otherwise.

Let $\hat{\beta}_{i j}$ denote the estimate of $\beta_{i j}$ obtained in step c of algorithm 1 . Let $\zeta_{n}$ denote the threshold value of $\hat{\beta}_{i j}$, and let $\tilde{E}_{m b, \zeta_{n}}^{(n)}$ denote the network obtained through thresholding $\hat{\beta}_{i j}$. That is, we define

$$
\overline{E}_{m b, \zeta_{n}}^{(n)}=\left\{\left(i, j\right):\left|\bar{\beta}_{i j}\right|>\zeta_{n}\right\}
$$

To establish the consistency of $\overline{\boldsymbol{E}}_{m b, \zeta_{n}}$, we first note that as implied by condition D and the total conditioning property, there exists a constant $c_{6}$ such that the true regression coefficients $\left\{\beta_{i j}\right\}$ defined in equation A. 3 satisfy

$$
\min _{i} \min _{j \in S_{i}}\left|\beta_{i j}\right| \geq c_{6} \eta^{-\kappa}
$$

where $\boldsymbol{\kappa}$ is as defined in condition $(B)$. Let $\overline{\mathscr{E}}_{\kappa}$ denote the edge set of a marginal association network for which each node has a degree of $O\left(n / \log (n)\right)$, adjacent to $O\left(n / \log (n)\right)$ highest associated nodes. It follows from lemmas 1 and 2 that

$$
P\left\{\boldsymbol{E}_{p}^{(n)} \subseteq \overline{\mathscr{E}}_{\kappa}\right\} \geq 1-O\left(p_{n}^{2} \exp \left(-c_{4} n^{(1-2 \kappa) \alpha /(\alpha+2)}\right)\right)=1-o(1)
$$

Let $\overline{\boldsymbol{B}}=\cup_{i=1}^{p_{n}} \boldsymbol{B}_{i}$, where $\boldsymbol{B}_{i}$ is defined in step b of the $p$-screening algorithm. We have $\boldsymbol{E}_{\hat{s}}^{(n)} \subset \overline{\boldsymbol{B}}$. Further, by lemma 3, we have $\boldsymbol{E}_{m b}^{(n)}=\boldsymbol{E}_{\hat{p}}^{(n)} \cup \boldsymbol{E}_{\hat{s}}^{(n)} \subset\left(\overline{\mathscr{E}}_{\kappa} \cap \overline{\mathscr{E}}_{\eta_{n}}\right) \cup \overline{\boldsymbol{B}}$.

Lemma 5 establishes the consistency of $\overline{E}_{m b, \zeta_{n}}^{(n)}$ as an estimate of $\boldsymbol{E}_{m b}^{(n)}$ conditioned on $\boldsymbol{E}_{m b}^{(n)} \subseteq\left(\overline{\mathscr{E}}_{\kappa} \cap \overline{\mathscr{E}}_{\eta_{n}}\right) \cup \overline{\boldsymbol{B}}$. Its proof is based on equation A. 15 and follows closely the proof of lemma 3, and is thus omitted here.

Lemma 5. Assume that the conditions $A, B, C, D$, and E1 to E6 hold and that $\boldsymbol{E}_{m b}^{(n)} \subseteq\left(\overline{\mathscr{E}}_{\kappa} \cap \overline{\mathscr{E}}_{\eta_{n}}\right) \cup \overline{\boldsymbol{B}}$ is true. Let $\zeta_{n}=\frac{1}{2} c_{6} n^{-\kappa}$. If $K_{n}=o\left(n^{(1-2 \kappa) /(\alpha+2)}\right)$. Then

$$
P\left\{\overline{E}_{m b, \zeta_{n}}^{(n)}=\boldsymbol{E}_{m b}^{(n)} \mid \boldsymbol{E}_{m b}^{(n)} \subseteq\left(\overline{\mathscr{E}}_{\kappa} \cap \overline{\mathscr{E}}_{\eta_{n}}\right) \cup \overline{\boldsymbol{B}}\right\}=1-o(1), \quad \text { as } n \rightarrow \infty
$$

As a summary for the above results, we have the following theorem, which establishes the consistency of $\overline{E}_{m b, \zeta_{n}}^{(n)}$ as an estimate of the adjacency matrix of the moral graph $\boldsymbol{E}_{m b}^{(n)}$.

Theorem 2. Consider a Bayesian network with distribution $P^{(n)}$ defined in equation 2.1 for mixed GLM variables. Assume the conditions $A, B, C, D$, and E1 to E6 hold. If $K_{n}=$ $o\left(n^{(1-2 \kappa) /(\alpha+2)}\right)$, then

$$
P\left\{\overline{E}_{m b, \zeta_{n}}^{(n)}=\boldsymbol{E}_{m b}^{(n)}\right\} \geq 1-o(1), \quad \text { as } n \rightarrow \infty
$$

Proof. By invoking lemma 3, equation A.16, and lemma 5, we have

$$
\begin{aligned}
& P\left[\hat{E}_{m b}^{(n)}, \zeta_{n}=E_{m b}^{(n)}\right] \geq P\left[\hat{E}_{m b}^{(n)}, \zeta_{n}=E_{m b}^{(n)} \mid E_{m b}^{(n)} \subseteq\left(\widetilde{\mathbb{F}}_{*} \cap \widetilde{\mathbb{F}}_{\eta_{n}}\right) \cup \tilde{B}\right] P\left[E_{m b}^{(n)} \subseteq\left(\widetilde{\mathbb{F}}_{*} \cap \widetilde{\mathbb{F}}_{\eta_{n}}\right) \cup \tilde{B}\right] \geq[1-o(1)][1-o(1) \\
& )+1-o(1)-1]=1-o(1)
\end{aligned}
$$
