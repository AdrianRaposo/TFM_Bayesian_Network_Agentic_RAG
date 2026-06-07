# On Budgeted Influence Maximization in Social Networks 

Huy Nguyen<br>Department of Computer Science<br>University of Houston<br>Houston, TX 77204<br>hanguyen5@uh.edu

Rong Zheng<br>Department of Computing and Software<br>McMaster University<br>Hamilton, ON, L8S 4K1, Canada<br>rzheng@mcmaster.ca


#### Abstract

Given a budget and arbitrary cost for selecting each node, the budgeted influence maximization (BIM) problem concerns selecting a set of seed nodes to disseminate some information that maximizes the total number of nodes influenced (termed as influence spread) in social networks at a total cost no more than the budget. Our proposed seed selection algorithm for the BIM problem guarantees an approximation ratio of $(1-1 / \sqrt{e})$. The seed selection algorithm needs to calculate the influence spread of candidate seed sets, which is known to be \#P-complex. Identifying the linkage between the computation of marginal probabilities in Bayesian networks and the influence spread, we devise efficient heuristic algorithms for the latter problem. Experiments using both large-scale social networks and synthetically generated networks demonstrate superior performance of the proposed algorithm with moderate computation costs. Moreover, synthetic datasets allow us to vary the network parameters and gain important insights on the impact of graph structures on the performance of different algorithms.


Index Terms-Budgeted influence maximization, social network, information diffusion, belief propagation.

## I. INTRODUCTION

The social network of interactions among a group of individuals plays a fundamental role in the spread of information, ideas, and influence. Such effects have been observed in real life, when an idea or an action gains sudden widespread popularity through "word-of-mouth" or "viral marketing" effects. For example, free e-mail services such as Microsoft's Hotmail, later Google's Gmail, and most recently Google's Google+ achieved wide usage largely through referrals, rather than direct advertising.

In viral marketing, one important question is given limited advertisement resources, which set of customers should be targeted such that the resulting influenced population is maximized. Consider a social network modeled as a graph with vertices representing individuals and edges representing connections or relationship between two individuals. The influence maximization (IM) problem tries to find a seed set $S$ with cardinality $|S|=k$ in the graph such that the expected number of nodes influenced by $S$ is maximized [1], [2], [3]. With the cardinality constraint, the submodularity nature of the influence spread renders a greedy algorithm with $(1-1 / e)$ approximate ratio that in each round picks the seed with maximum influence spread and runs for $k$ rounds. However the assumption of equal costs for all seed nodes seldom holds in practice. With the proliferation of influence score services
such as Klout and PeerIndex ${ }^{1}$, one can easily measure his influence in the social sphere and use that to negotiate the price for services he provides. The higher the influence score of a user, the more costly it is to persuade him.

We consider in this paper a generalized version of the IM problem, namely, the budgeted influence maximization (BIM) problem: given a fixed budget $b$ and a random cost function $c$, find a seed set $S$ which fits the budget $\sum_{s_{i} \in S} c\left(s_{i}\right) \leq b$ and maximizes the number of influenced nodes. Clearly, BIM is more relevant in practice as there is typically a price associated with initializing the dissemination of information. With the budget constraint, we prove that direct application of the simple greedy algorithm may result in unbounded performance gap.

In this paper, we present a seed selection algorithm that can attain an approximation guarantee of $(1-1 / \sqrt{e})(\sim 0.394)$. One critical component of the seed selection process is the determination of influence spread of a set of seeds. Exact computation of influence spread is proven to be of \#Pcomplete [3]. Thus, efficient algorithms need to be devised. More specifically, we first establish the linkage between influence spread computation and belief propagation on a Bayesian network (modeled as a directed acyclic graph [DAG]), where the marginal conditional dependency corresponds to the influence probabilities. Belief propagation has been extensively studied in literatures, and thus many exact or approximation algorithms can be leveraged to estimate the influence spread. For a general graph that contains loops, we propose two approximation algorithms that prune some edges in the graph to obtain a DAG that captures the bulk of influence spread. To reduce the number of candidate seed nodes, we localize the influence spread region such that at each round, only nodes that are affected by the previously selected seed need to be evaluated. Empirical study shows that the proposed algorithms can scale up to large-scale graphs with millions of edges with high accuracy. On real-world social network graphs, our methods achieve influence spread comparable to that by Greedy algorithm [3] and incur significant less computation costs. In the unit-cost IM problem, the proposed methods outperform PMIA [4] in achievable influence spread at the expense of marginal increase in computation time. In the BIM problem, the proposed methods outperform CELF [5] in term of scalability and performance on dense graphs. We further

[^0]
[^0]:    ${ }^{1}$ http://www.klout.com and http://www.peerindex.com

study the effect of network structures on the performance of the algorithms.

The main contributions of this paper are summarized as follows:

- We propose a greedy algorithm for BIM with a constant approximation ratio.
- We cast the problem of inference spread computation on a DAG as an instance of belief propagation on a Bayesian network.
- We prove the #P-hardness of inference spread computation on a DAG.
- Two heuristics are proposed to construct DAGs from a general graph that capture the bulk of influence spread.
- We provide important insights on the impact of graph structures on performance of different algorithms.

The rest of this paper is organized as follows. In Section II, we give a comprehensive review of the related literatures. Section III presents the seed selection algorithm and proves its performance bound. Theoretical results concerning influence spread on DAGs are in Section IV. In Section V, we devise two heuristics to reduce a general directed graph into a DAG which captures the majority of influence spread. From the presented theoretical results, we have the main algorithm in Section VI. In Section VII, extensive experiment results are presented. Finally we conclude the paper and discuss future research directions in Section VIII.

## II. Related Work

Kempe et al. in [3] are the first to formulate the IM problem. The authors proved the submodularity of the influence spread function and suggested a greedy scheme (henceforth referred to as Greedy algorithm) with an incremental oracle that identifies, in each iteration, a new seed that maximizes the incremental spread. The approach was proven to be a $(1-1/e)$-approximation of the IM problem. However, Greedy suffers from two sources of computational deficiency: 1) the need to evaluate many candidate nodes before selecting a new seed in each round, and 2) the calculation of the influence spread of any seed set relies on Monte-Carlo simulations.

In an effort to improve Greedy, Leskovec et al. [5] recognized that not all remaining nodes need to be evaluated in each round and proposed the “Cost-Effective Lazy Forward” (CELF) scheme. Experimental results demonstrate that CELF optimization could achieve as much as 700-time speed-up in selecting seeds. However, even with CELF mechanism, the number of candidate seeds is still large. Recently, Goyal et al. proposed CELF++ [6] that has been shown to run from 35% to 55% faster than CELF. However, the improvement comes at the cost of higher space complexity to maintain a larger data structure to store the look-ahead marginal gains of each node.

Chen et al. devises several heuristic algorithms for influence spread computation [7], [4], [8]. In Degree Discount [7], the expected number of additional vertices influenced by adding a node $v$ in the seed set is estimated based on $v$’s one hop neighborhoods. It also assumes that the influence probability is identical on all edges. In [4] and [8], two approximation algorithms, PMIA and LDAG are proposed to compute the maximum influence set under IC and LT models, respectively. In LDAG, it has been proven that under the LT model, computing influence spread in a DAG has linear time complexity, and a heuristic on local DAG construction is provided to further reduce the compute time. We have proven in Section IV that computing influence spread in a DAG under the IC model remains #P-hard. The marked difference between the two results arises from the fact that in the LT model, the activation of incoming edges is coupled so that in each instance, only one neighbor can influence the node of interest in an equivalent random graph model.

Another line of work explores diffusion models beyond LT and IC. Even-Dar et al. [9] argue that the most natural model to represent diffusion of opinions in a social network is the probabilistic voter model where in each round, each person changes his opinion by choosing one of his neighbors at random and adopting the neighbor’s opinion. Interestingly, they show that the straightforward greedy solution, which picks the nodes in the network with the highest degree, is optimal. Sylvester [10] studies the spread maximization problem on dynamic networks and examines the use of dynamic measures with Greedy algorithm on both LT and IC models. Chen et al. [11] consider a new model that incorporates negativity bias and design an algorithm to compute influence on tree structures.

Inapproximability results of problems related to IM have also been investigated in literature. MINSEED is the problem of finding the minimized seed set size to activate all or a portion of vertices. Chen [12] proves that under LT model with a general threshold, MINSEED can not be approximated within a ratio of $O(2^{\log^{1.7n})}$, for any fixed $\varepsilon>0$, unless $N P \subseteq D T I M E\left(n^{p o l g l o g(n)}\right)$. In the case when the threshold equals two, the author proves that it is as hard as the case with a general threshold, even for constant degree graphs. Ackerman et al. [13] cast MINSEED and IM as maximization problems making them amenable to optimization techniques. However, since the number of variables and constraints grow in $O\left(n^{2}\right)$ and $O\left(n^{3}\right)$ respectively $-n$ being the number of vertices in the graph - this approach is only tractable in smallsize problems. MINTIME is the problem of finding a target size $k$ such that all or a portion of vertices are activated in the minimum possible time (in terms of spread time or hop count). With a given coverage threshold $\eta$, Goyal et al. [14] prove that under both IC and LT model, the greedy algorithm can produce the result covering $\eta-\varepsilon$ vertices $(\varepsilon>0)$ in min time, with seed size $|S| \leq k(1+\ln (\eta / \varepsilon))$. Ni et al. [15] investigate the MINTIME problem by proposing a new spread model and proving various timing bounds on the proposed model.

Literatures on epidemiology are also related to the IM problem that identifies nodes that can initiate viral propagation to most part of the network. Under the proposed model, the authors of [16] proved that the epidemic threshold for a network is exactly the inverse of the largest eigenvalue of its adjacency matrix. In a follow-up work [17], the authors used the previously defined epidemic threshold to quantify the vulnerability of a given network and devised a fast algorithm to choose the best $k$ nodes to be immunized (removed) so as to minimize network vulnerability. [18] considered the immu-

nization problem on dynamic networks. The key differences between work on viral immunization literatures and IM lie in the spreading model adopted (e.g.: SIS [susceptible-infected-susceptible] or SIR [susceptible-infected-recovered] vs. IC or LT) and whether the dynamics in the evolution of influence are of interest.

Most existing work on the IM problem only considers cardinality constraints. CELF [5] is the only applicable approach to the BIM problem. We will later show in our evaluation that the proposed methods outperform CELF in term of running time (several orders of magnitude faster) and performance on dense networks.

This article is an extended version of our conference paper in [19]. We modified our main algorithm to solve the BIM problem and prove its approximation factor. We added detailed algorithm description, complexity analysis, and report more comprehensive results regarding algorithm performance on different real datasets. We also conducted new experiment sets on synthetic networks and provide results on the impact of graph structure on different IM algorithms which, to the best of our knowledge, has never been studied before.

## III. The Budgeted Influence Maximization Problem

In this section, we consider the BIM problem with the objective to select the seed set that maximizes influence spread given a fixed budget and arbitrary node costs.

## A. Problem Formulation

Consider the network a directed graph $\mathcal{G}=(V, E)$ with $|V|=n$ vertices and $|E|=m$ edges. For every edge $(u, v) \in E, p(u, v)$ denotes the probability of influence being propagated on the edge. In this paper, we adopt the Independent Cascade (IC) model. Given a seed set $S \subseteq V$, the IC model works as follows. Let $S_{t} \subseteq V$ be the set of node (newly) activated at time $t$, with $S_{0}=S$ and $S_{t} \cap S_{t-1}=\emptyset$. At round $t+1$, every node $u \in S_{t}$ tries to activate its neighbors in $v \in V \backslash \bigcup_{0 \leq i \leq t} S_{i}$ independently with probability $p(u, v)$. The influence spread of $S$, denoted by $\sigma(S)$, is the expected number of activated nodes given seed set $S$.

Kempe et al. [3] proved two important properties of the $\sigma(\cdot)$ function: 1) $\sigma(\cdot)$ is submodular, namely, $\sigma(S \cup\{v\})-\sigma(S) \geq$ $\sigma(T \cup\{v\})-\sigma(T)$ for all $v \in V$ and all subsets $S$ and $T$ with $S \subseteq T \subseteq V$; 2) $\sigma(S)$ is monotone, i.e. $\sigma(S) \leq \sigma(T)$ for all set $S \leq T$. For any given spread function $\sigma(\cdot)$ that is both submodular and monotone, the problem of finding a set $S$ of size $k$ that maximizes $\sigma(S)$ can be approximated by a simple greedy approach.

Budgeted Influence Maximization: In BIM, each node $u$ is associated with an arbitrary cost $c(u)$. The goal is to select a seed set $S \subseteq V$ such that the total cost of this set is less than a budget $b$. Denote by $c(S)$ the total cost of a set, i.e., $c(S)=\sum_{u \in S} c(u)$. Budgeted IM (BIM) can be formulated as an optimization problem:

$$
\begin{array}{ll}
\max _{S \subseteq V} & \sigma(S) \\
\text { s.t. } & c(S) \leq b
\end{array}
$$

TABLE I: Notations


```
Algorithm 1: Naive Greedy
    input : \(G=(V, E), b\)
    \(S=\emptyset\)
    repeat
        \(\delta(v)=(\sigma(S \cup v)-\sigma(S)) / c(v), \forall v \in V\)
        \(u=\arg \max _{v \in V} \delta(v)\)
        if \(c(S \cup u) \leq b\) then
            \(S=S \cup u\)
        \(V=V \backslash u\)
    until \(V=\emptyset\);
    output: \(S\)
```

When $c(u) \equiv 1, \forall u \in S$, BIM degenerates to the original IM problem. Thus, we call IM the unit-cost BIM. Since IM is NP-hard, it is easy to see that BIM is NP-hard as well. Key notations used in this paper are summarized in Table I.

## B. The Seed Selection Algorithm

First, we consider an intuitive greedy strategy that selects at each step a node $u$ that maximizes the spread gained over cost ratio if the cost of $u$ is less than the remaining budget. We hereby refer to this scheme as the Naive Greedy approach. Let $r$ be the number of iterations executed and $S_{r}$ be the seed set at step $r$. Note that $\left|S_{r}\right| \leq r$. At step $r+1$, Naive Greedy calculates the incremental spread-cost ratio.

$$
\delta(v)=(\sigma(S \cup v)-\sigma(S)) / c(v), \forall v \in V \backslash S
$$

The algorithm chooses $u$ if $u=\arg \max _{v \in V, c(s_{r} \cup v) \leq b} \delta(v)$. The algorithm terminates when no budget remains, or no node can be added to $S$. Naive Greedy is summarized in Algorithm 1.

We first observe that Naive Greedy can have unbounded approximation ratio. Consider a network containing $l+1$ nodes $V=\left\{u, v_{1}, v_{2}, \cdots, v_{l}\right\}$. Every pair in $v_{1}, v_{2}, \cdots, v_{l}$ is connected by an edge with influence probability one, while $u$ is an isolated node. Let the cost $c(u)=1-\varepsilon, c\left(v_{i}\right)=$ $l, \forall i=1, \cdots, l$ and the budget $b=l$. The optimal solution will pick any node $v_{i}$ and achieve an influence spread of $l$. In contrast, Naive Greedy picks $u$ since it has the maximum

```
Algorithm 2: Improved Greedy
    input : \(G=(V, E), b\)
    \(S_{1}=\) result of Naive Greedy
    \(s_{\max }=\arg \max _{v \in V} \sigma(v)\)
    \(S=\arg \max \left(\sigma\left(S_{1}\right), \sigma\left(s_{\max }\right)\right)\)
    output: \(S\)
```

influence-cost ratio $1 / 1-\epsilon>1$. The resulting influence spread is 1 . Thus, the approximation ratio for Naive Greedy is $l$.

Next, we show that Naive Greedy can be modified to achieve a constant approximation ratio. This algorithm is an adaptation of an algorithm first proposed by Khuller et al. [20]. We assume that there is no node with a cost greater than the budget $b$, as it will never be a feasible solution to BIM. Let $S_{1}$ be the seed set selected by Naive Greedy, we consider another candidate solution $s_{\max }$, which is the node that has the largest influence. We compare the spread of $S_{1}$ and $s_{\max }$, then output the one with higher influence spread. The process is illustrated in Algorithm 2.

Theorem 1: Algorithm 2 provides a $(1-1 / \sqrt{e})-$ approximation for the BIM problem.

By considering the candidate solution with the maximum influence spread, Algorithm 2 guarantees the approximation ratio within a constant factor, while Algorithm 1 is unbounded. Note that Algorithm 2 is different from CELF presented by Leskovec et al. in [5]. CELF runs Naive Greedy on the budgeted and the unit-cost (by setting all costs to one) versions of the problem, and selects the set with the maximum influence spread. While finding the seed set to maximize IM consumes more time than what it takes to select a single node with the largest spread, CELF can only guarantee a looser bound of $\frac{1}{2}(1-1 / e)(\sim 0.316)$.

Complexity: Let $T$ be the maximum time needed to calculate the value of $\sigma(S), \forall S \subseteq V$. Algorithm 1 runs in $O\left(n^{2} T\right)$ time where $n$ is the number of nodes (i.e. $n=|V|$ ). Finding $S_{1}$ therefore costs $O\left(n^{2} T\right) . s_{\max }$ can be determined in in $O(n T)$ time. Algorithm 2 therefore runs in $O\left(n^{2} T\right)$ time. Note in [20] that Greedy with partial enumeration heuristic can achieve an approximation guarantee of $(1-1 / e)$. However, the improvement is attained at the expense of much higher computation complexity of $O\left(n^{4} d\right)$ [21].

Algorithm 2 calls $\sigma$ as a subroutine. The efficiency of $\sigma$ computation is thus critical to the overall running time of the algorithm. In the following sections, we develop efficient algorithms for approximating the spread function $\sigma$ . We first consider the special case when the network is a directed acyclic graph (DAG). Then, we provide two DAG construction algorithms from a general network graph. Finally, some techniques to further optimize the execution of Algorithm 2 is presented.

## IV. DETERMINING INFLUENCE SPREAD ON DAG

Given a seed set, estimating value of the $\sigma$ from that seed set was proven to be a \#P-complete problem [3]. We show in this section that under the IC model, calculation of $\sigma$ remains \# P-complete even when the underlying network  graph is a DAG. Then we establish the equivalence between computing $\sigma$ on a DAG and the computation of marginal probabilities in a Bayesian network.

## A. Hardness of Computing Influence Spread on DAGs

In [3], Kempe et al. proposed an equivalent process of influence spread under the IC model, where at the initial stage, an edge $(u, v)$ in $\mathcal{G}$ is declared to be live with probability $p(u, v)$ resulting in a subgraph of $\mathcal{G}$. A node $u$ is active if and only if there is at least one path from some node in $S$ to $u$ consisting entirely of live edges. In general graphs, the influencer-influencee relationship may differ in one realization to another for bi-directed edges. In a DAG, on the other hand, such relationship is fixed and is independent of the outcome of the coin flips at the initial stage (other than the fact that some of the edges may not be present). Let $x_{u}, u \in V$ denotes the binary random variable of the active state of node $u$, namely, $\mathbb{P}\left(x_{u}=1\right)=p(u)$. For each node $v$ in $S, \mathbb{P}\left(x_{v}=1\right)=1$. If a node $u \notin S$ does not have any parent in $\mathcal{G}$ then $\mathbb{P}\left(x_{u}=1\right)=0$. From $\mathcal{G}$, the conditional probability $p\left(x_{u} \mid x_{P a r(u)}\right)$ is uniquely determined by the edge probability, where $x_{P a r(u)}$ denotes the states of the parents of node $u$. In other words, influence spread can be modeled as a Bayesian network. If node $u$ does not have any parent, $p\left(x_{u} \mid x_{P a r\left(x_{u}\right)}\right)=p\left(x_{u}\right)$. The joint distribution is thus given by,

$$
p\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid x_{P a r\left(x_{i}\right)}\right)
$$

Given the outcome of coin flips $C, \sigma_{C}(S)=\sum_{u \in V} x_{u}$. Therefore,

$$
\sigma(S)=\mathbb{E}\left(\sigma_{C}(S)\right)=\sum_{u \in V} \mathbb{E}\left(x_{u}\right)=\sum_{u \in V} p(u)
$$

The second equality is due to the linearity of expectations. To compute $p(u)$, we can sum (3) over all possible configurations for $x_{v}, v \in V \backslash u$. Clearly, such a naive approach has complexity that is exponential in the network's treewidth. In fact, the marginalization problem is known to be \#P-complete on a DAG. However, since computing influence spread on a DAG can be reduced to a special instance of the marginalization problem, it remains to be shown if the former problem is \#P-complete. The main result is summarized in the following theorem ${ }^{2}$.

Theorem 2: Computing the influence spread $\sigma(S)$ on a DAG given a seed set $S$ is \#P-complete.

[^0]
[^0]:    ${ }^{2}$ All proofs are presented in the Appendix

### 4.2.1 B. Estimating $\sigma(\cdot)$ via Belief Propagation

Belief propagation (BP) is a message passing algorithm for performing inference on graphical models, such as Bayesian networks and Markov random fields. It calculates the marginal distribution for each unobserved node, conditional on any observed nodes [22]. For singly-connected DAGs, where between any two vertices there is only one simple path, the BP algorithm in [23] computes the exact solution with $O(n)$ complexity. For multi-connected DAGs, where multiple simple paths may exist between two vertices, belief propagation and many of its variants [22], [24], [25] have been shown to work well in general. Exact solutions such as junction tree [24] may incur the worst case complexity exponential to the number of vertices due to the need to enumerate all cliques in the DAG.

BP algorithms take as input a factor graph or a description of the underlying Bayesian Network. In the context of influence spreading, each node only has two states: active and inactive. BP algorithms calculate the probability of each node in either states. $\sigma(\cdot)$ can then be determined by summing up the probability of nodes being active.

Computation complexity: The complexity of $\sigma(\cdot)$ calculation is dominated by the execution of the BP algorithm. A variety of BP algorithms exist. In this work, we adopt the Loopy Belief Propagation (LBP) algorithm which was shown to perform well for various problems [26], [27]. LBP takes $O\left(M^{d}\right)$ to estimate the active probability of a node, where $M$ is the number of possible labels (states) for each variable $(M=2)$, and $d$ is the maximum in-degree. We denote by $n_{0}$ the number of vertices in a DAG. Thus, the complexity of LBP is $O\left(n_{0} 2^{d}\right)$.

### 4.2.2 C. A Single Pass Belief Propagation Heuristic for $\sigma(\cdot)$ Estimation

Calculating $\sigma(\cdot)$ with LBP produces highly accurate results, but the computation time remains to be high when the graph is multi-connected. The main complexity arises from the fact that the activation of parents of a node may be correlated in a multi-connected graph. Thus, in computing the activation probability of the node, one needs to account for the joint distribution of its parent nodes. Next, we propose a single pass belief propagation (SPBP) algorithm that ignores such correlation in determining $\sigma(\cdot)$. Note that the heuristic is exact when the graph is singly-connected.

Let $\mathcal{D}(\cdot)$ be the input DAG. Consider a node $v \in \mathcal{D}(\cdot)$. Given the activation probabilities of its parents $\operatorname{Par}(v)$, we approximate $p(v)$ as,

$$
p(v)=1-\prod_{u \in \operatorname{Par}(v)}(1-p(u) p(u, v))
$$

The algorithm is summarized in Algorithm 3. It starts with the seed nodes and proceeds with the topological sorting order. The total complexity is $O\left(n_{0} d\right)$. Clearly, SPBP is much faster than LBP.

## 5. DAG CONSTRUCTION

In general, real social networks are not DAGs (with the exception of advisor-advisee and parent-child relationship, for instance, which exhibit a natural hierarchy). To apply the BP algorithm in computing influence spread, one needs to selectively prune edges and reduce the graph to a DAG. Clearly, there are many ways to do so. The challenge is to find a DAG that approximates well the original graph in influence spread. In this section, we introduce two DAG construction algorithms, both retaining important edges where influences are likely to travel.

### 5.5. A. Localizing Influence Spread Region

One important observation in [4] is that the influence of a seed node diminishes quickly along a path away from the seed node. In other words, the "perimeter" of influence or the influence region of a seed node is in fact very small. One way to characterize the influence region of a node $v$ is through the union of maximum influence paths defined next.

Definition 1: (Path Propagation Probability)
For a given path $P(u, v)=\left\{u_{1}, u_{2}, \ldots, u_{l}\right\}$ of length $l$ from a vertex $u$ to $v$, with $u_{1}=u, u_{l}=v$ and $u_{2}, \ldots, u_{l-1}$ are intermediate vertices, define the propagation probability of the path, $p(P)$, as:

$$
p(P(u, v))=\prod_{i=1}^{l-1} p\left(u_{1}, u_{i+1}\right)
$$

$p(P(u, v))$ can be thought as the probability that $u$ will influence $v$ if $u$ is selected as a seed node. Obviously, the longer the path length $l$, the smaller the chance that $u$ can spread its influence to $v$.

Definition 2: (Maximum Influence Path)
Denote by $\mathcal{P}(\mathcal{G}, u, v)$ the set of all paths from $u$ to $v$ in $\mathcal{G}$. The maximum influence path $M I P(\mathcal{G}, u, v)$ from $u$ to $v$ is defined as:

$$
M I P(\mathcal{G}, u, v)=\arg \max _{P}\{p(P) \mid P \in \mathcal{P}(\mathcal{G}, u, v)\}
$$

Ties are broken in a predetermined and consistent way such that $M I P(\mathcal{G}, u, v)$ is always unique, and any sub-path in $M I P(\mathcal{G}, u, v)$ from $x$ to $y$ is also the $M I P(\mathcal{G}, x, y)$. In order to localize the influence region of nodes and reduce the complexity, we only consider influence spread on maximum influence paths.

Definition 3: (Maximum Influence Out-Arborescence)
For a graph $\mathcal{G}$, an influence threshold $\theta$, the maximum influence out-arborescence of a node $u \in V, M I O A(\mathcal{G}, u, \theta)$, is


defined as:

$$
M I O A(\mathcal{G}, u, \theta)=\bigcup_{v \in V, p(M I P(\mathcal{G}, u, v)) \geq \theta} M I P(\mathcal{G}, u, v)
$$

$M I O A(\mathcal{G}, u, \theta)$ is defined as the union of $M I P$ 's from $u$ to all other nodes in $V$. MIP's with propagation probabilities less than a threshold $\theta$ are not included to reduce the size of MIOA. One can think of $M I O A(\mathcal{G}, u, \theta)$ as a local region where $u$ can spread its influence to. $M I O A(\mathcal{G}, u, \theta)$ can be computed by first finding the Dijkstra tree rooted at $u$ with edge weight $-\log (p(u, v))$ for edge $(u, v)$, and then removing the paths whose cumulative weights are too high. By tuning the parameter $\theta$, influence regions of different sizes can be obtained. For a single node, its MIOA is clearly a tree. For multiple seed nodes, we build upon the idea of local influence region and propose two algorithms.

## B. Building DAGs from a Seed Set

DAG 1: We observe that any DAG has at least one topological ordering. Conversely, given a topological ordering, if only edges going from a node of low rank to one with high rank are allowed, the resulting graph is a DAG.

To obtain the topological ordering given seed set $S$, we first introduce a (virtual) super root node $R$ that is connected to all seed nodes with edge probability 1 . Let $\mathcal{G}_{R}=\left(V_{\mathcal{G}_{R}}, E_{\mathcal{G}_{R}}\right)$ where $V_{\mathcal{G}_{R}}=V \cup\{R\}$ and $E_{\mathcal{G}_{R}}=E \cup\left\{\left(R, S_{k}\right) \mid \forall S_{k} \in S\right\}$. We build $M I O A\left(\mathcal{G}_{R}, R, \theta\right)$ by calculating a Dijkstra tree from $R$. After removing $R$ and its edges from $M I O A\left(\mathcal{G}_{R}, R, \theta\right)$, we obtain a singly connected DAG $\mathcal{D}_{1}=\left(V_{\mathcal{D}_{1}}, E_{\mathcal{D}_{1}}\right)$ on which BP algorithms can be directly applied and used to estimate the influence spread from $S$. However, $\mathcal{D}_{1}(\cdot)$ is very sparse (with $n-k$ edges) since many edges are removed.

We then augment $\mathcal{D}_{1}(\cdot)$ with additional edges. Note that $M I O A\left(\mathcal{G}_{R}, R, \theta\right)$ provides a topology ordering. More specifically, let the rank of node $v$ be the sum weight of the shortest path from $R$, namely,

$$
r(v)=\min (-\log (p(P(s, v)))), \forall s \in S
$$

Rank grows as the node is further away from $R$. We include in $\mathcal{D}_{1}(\cdot)$ all edges in $\mathcal{G}$ whose end points are in $\mathcal{D}_{1}(\cdot)$ and go from a node with lower rank to one with higher rank. Clearly, the resulting graph is a DAG. The DAG constructing procedure is illustrated in Figure 1 and summarized in Algorithm 4.
![img-0.jpeg](img-0.jpeg)

Fig. 1: DAG due to Algorithm 4. $S_{1}$ and $S_{2}$ are seed nodes. Edges in $M I O A\left(\mathcal{G}_{R}, R, \theta\right)$ are in bold. $\left(S_{1}, B\right),\left(S_{2}, A\right),(A, B)$, and $(B, C)$ are added into $\mathcal{D}_{1}(S)$ to improve inference accuracy. $\theta=0.0001$.

```
Algorithm 5: Calculate \(\mathcal{D}_{2}(S)\) from a seed set \(S\)
    input : \(\mathcal{G}, S, M I O A(\mathcal{G}, v, \theta), \forall v \in V\)
    \(1 \mathcal{D}_{2}(S)=\bigcup_{\forall s \in S} M I O A(\mathcal{G}, s, \theta)\)
    2 Calculate \(r(v), \forall v \in V_{\mathcal{D}_{2}}\) (Eq. (9))
    3 foreach \((u, v) \in \mathcal{D}_{2}(S)\) do
        if \(r(u) \geq r(v)\) then
            \(\mathcal{D}_{2}(S)=\mathcal{D}_{2}(S) \backslash(u, v)\)
    output: \(\mathcal{D}_{2}(S)\)
```

DAG 2: In the second algorithm, we first compute the MIOA from each seed node and take the union of $M I O A(\mathcal{G}, s, \theta), \forall s \in S$. Denote the resulting graph $\mathcal{D}_{2}(S)=$ $\left(V_{\mathcal{D}_{2}}, E_{\mathcal{D}_{2}}\right)$. Note that $\mathcal{D}_{2}(S)$ is not necessary a DAG as there could be circles.To break the cycles, certain edges need to be removed. We adopt a similar approach as in Algorithm 4. A node $v$ is associated with a rank $r(v)$ as in (9). Only edges that connect a lower ranked node to higher ranked node are retained. Clearly, the resulting graph is a DAG. The approach is summarized in Algorithm 5.
![img-1.jpeg](img-1.jpeg)

Fig. 2: DAG due to Algorithm 5. $S_{1}$ and $S_{2}$ are seed nodes. $\mathcal{D}_{2}(S)$ is the union of $M I O A\left(\mathcal{G}, S_{1}, \theta\right)$ (solid edges) and $M I O A\left(\mathcal{G}, S_{2}, \theta\right)$ (dashed edges). $\theta=0.0001$.

The next proposition provides the relationship between DAGs constructed by Algorithm 4 and 5.

Proposition 1: Given a fixed influence threshold $\theta$, let $\mathcal{D}_{1}(\cdot)=\left(V_{\mathcal{D}_{1}},E_{\mathcal{D}_{1}}\right)$ and $\mathcal{D}_{2}(\cdot)=\left(V_{\mathcal{D}_{2}},E_{\mathcal{D}_{2}}\right)$ be the DAGs constructed by Algorithm 4 and Algorithm 5. Then, $V_{\mathcal{D}_{1}}=$ $V_{\mathcal{D}_{2}}$ and $E_{\mathcal{D}_{2}} \subseteq E_{\mathcal{D}_{1}}$.
Computation complexity: Building the Dijkstra tree from a source node takes $O\left(n_{0} \log n_{0}\right)$, where $n_{0}$ is the maximum number of vertices in the resulting DAG. Calculating the node rank $r(\cdot)$ takes $O\left(n_{0}\right)$, the union operation in DAG 2 takes $O\left(n_{0}-1\right)$, and the edge augmenting and pruning in DAG 1 and DAG 2 takes $O\left(m_{0}\right)$ and $O\left(\min \left(m_{0}, k\left(n_{0}-1\right)\right)\right)$, respectively, where $m_{0}$ is the maximum number of edges in a DAG and $k$ is the seed set cardinality.

Thus, the running time of DAG 1 and DAG 2 are $O\left(n_{0} \log n_{0}\right)$ and $O\left(n_{0}\right)$, respectively. Note that DAG 2 calculation requires the availability of $\operatorname{MIOA}(\mathcal{G}, v, \theta), \forall v \in V$ first, which can be built at the initialization stage at the cost of $O\left(n n_{0} \log n_{0}\right)$. Assuming that $k$ is small and $\theta$ is properly selected, we have $n 0 \ll n$.

## VI. Optimization of Seed Selection

In each round of Naive Greedy, a seed node with the maximum incremental spread-cost ratio is selected, namely, $v=$ $\max _{v \in V \backslash S} \delta(v)$. Recall that $\delta(v)=(\sigma(S \cup v)-\sigma(S)) / c(v)$ is the spread increment ratio of $v$ under $S$. Initially, when $S=\emptyset, \delta(v)=\sigma(v) / c(v)$. Evaluating $\delta(v)$ at each iteration for all $v \in V$ dominates the overall computation complexity.

To accelerate the execution of Naive Greedy, one can try to improve on two aspects, namely, 1) limiting the candidate set of nodes to pick from for the next seed, and 2) reducing the complexity of computing the spread increments. CELF algorithm [5] eliminates many nodes from being evaluated. We focus on the second aspect. The proposed mechanism can be used in conjunction with the idea from CELF.

Recall in Section V-A, we use $M I O A$ to localize the influence region of a node. Consider for now that influence from a node can only reach nodes in its MIOA. Then, we make the following claim.

Proposition 2: Given the current seed set $S$, adding $u$ to $S$ will not change the spread increment of $v$, namely, $\delta_{S}(v)=\delta_{S \cup u}(v)$ if $\operatorname{MIOA}(\mathcal{G}, u, \theta)$ and $\operatorname{MIOA}(\mathcal{G}, v, \theta)$ have no common vertex.

As a result of Proposition 2, each time we select a new seed, only the influence increments of nodes that have overlapping influence regions with the newly selected seed need to be reevaluated. Formally, we define the set of Peer Seeds (PS) of a vertex $v \in V$ as follow:
$P S(\mathcal{G}, v, \theta)=\{s \in V \mid M I O A(\mathcal{G}, s, \theta) \cap M I O A(\mathcal{G}, v, \theta) \neq \emptyset\}$
$P S(\mathcal{G}, v, \theta)$ can be computed efficiently just once at the beginning when all $\operatorname{MIOA}(\mathcal{G}, v, \theta)$ 's are available.

Combining the ideas of 1) limiting the region to be reevaluated using $P S, 2$ ) limiting the set of nodes to pick from (adopted from CELF), and 3) picking nodes w.r.t its cost and the remaining budget (Algorithm 2), we have the complete procedure to determine the optimal seed set in Algorithm 6. Figure 3 gives the block diagram of the proposed algorithm.
![img-2.jpeg](img-2.jpeg)

Fig. 3: The building blocks of our proposed algorithm. Details are presented in the previous sections.

The seed selection algorithm proceed as follow: In the initialization phase (lines $1-8$ ), MIOA's and PS'es are constructed. The second candidate solution $s_{\max }$ can be determined in $O(n)$ time (line 9). $S_{1}$ is computed by executing the loop in lines $10-26$. Each node in $V$ is ranked by its incremental spread-cost ratio and can be added to $S_{1}$ just once. The node with the highest ratio is included in $S_{1}$ if it does not violate the budget $b$ (line 12), and the corresponding nodes will be re-evaluated (lines $18-24$ ). The procedure terminates once all nodes were considered, or no more budget remains (line 26). Finally, the algorithm compares the spread of $S_{1}$, $s_{\max }$ and returns the solution with the larger spread.
Computation complexity: Recall that we denoted by $n_{0}$ the largest number of vertices, and by $d$ the largest in-degree of a node in a DAG. For each node $v \in V$ in the initialization phase, building $\operatorname{MIOA}(\mathcal{G}, v, \theta)$ takes $O\left(n_{0} \log n_{0}\right)$, and estimating $\sigma(v)$ takes $O\left(n_{0} d\right)$ using SPBP and $O\left(n_{0} 2^{d}\right)$ using LBP, respectively. Thus, depending on the algorithm used, the running time of initialization is $O\left(n n_{0}\left(\log n_{0}+d\right)\right)$ or $O\left(n n_{0}\left(\log n_{0}+2^{d}\right)\right)$.

Let $k$ be the number of seeds selected in the main loop (lines $10-26$ ) and $v_{0}$ be the cardinality of the largest set of peer seeds, namely, $v_{0}=\max _{\forall v \in V}\{|\operatorname{PS}(\mathcal{G}, v, \theta)|\}=O\left(n_{0}\right)$. Therefore, nodal influence spread is updated $O\left(k n_{0}\right)$ times. Note that this is much less than the number of updates required by Algorithm $1\left(O\left(n^{2}\right)\right)$ as we do not naively re-evaluate every node. Each time when the influence spread is updated, we need to rebuild the DAG (line $20-$ takes $O\left(n_{0} \log n_{0}\right)$ with DAG 1 or $O\left(n_{0}\right)$ with DAG 2) and calculate the influence spread (line $21-$ takes $O\left(n_{0} 2^{d}\right)$ with LBP or $O\left(n_{0} d\right)$ with SPBP). The total computation complexity for different combinations of algorithms is summarized as follows:


Clearly, combining DAG 1 and LBP incurs the highest complexity while the combination of DAG 2 and SPBP is the

```
Algorithm 6: The Proposed Algorithm
    input : network graph \(\mathcal{G}(V, E)\) and budget \(b\)
    // initialization
    \(S=S_{1}=s_{\max }=\emptyset, \sigma_{0}=0, \theta=\) influence threshold
    foreach \(v \in V\) do
        build \(M I O A(\mathcal{G}, v, \theta)\)
        \(\mathcal{D}(v)=M I O A(\mathcal{G}, v, \theta)\)
        calculate \(\sigma(v)\) (LBP or Algorithm 3)
        \(\delta(v)=\sigma(v) / c(v)\)
        \(\delta_{\text {old }}(v)=0\)
    build \(P S(\mathcal{G}, v, \theta), \forall v \in V\)
    // select \(s_{\max }\)
    \(s_{\max }=\arg \max _{v \in V} \sigma(v)\)
    // select \(S_{1}\)
    while true do
        // select a new seed
        \(u=\arg \max _{v \in V \backslash S}(\delta(v))\)
        if \(c\left(S_{1} \cup u\right) \leq B\) then
            \(S_{1}=S_{1} \cup\{u\}\)
            \(\sigma_{0}=\sigma(S)\)
            \(\delta_{\text {old }}(v)=\delta(v), \forall v \in V \backslash S_{1}\)
            \(b=b-c(u)\)
            // update incremental influence spread
            \(\delta_{\max }=0\)
            foreach \(v \in P S(\mathcal{G}, u, \theta) \backslash S_{1}\) do
                if \(\delta_{\text {old }}(v)>\delta_{\max }\) then
                    build \(\mathcal{D}\left(S_{1} \cup\{v\}\right)\) (Algorithm 4 and 5)
                    calculate \(\sigma\left(S_{1} \cup\{v\}\right)\) (LBP or Algorithm 3)
                    \(\delta(v)=\left(\sigma\left(S_{1} \cup\{v\}\right)-\sigma_{0}\right) / c(v)\)
                    if \(\delta(v)>\delta_{\max }\) then
                    \(\delta_{\max }=\delta(v)\)
            \(V=V \backslash u\)
            if \(V=\emptyset\) or \(b=0\) then
            break
    \(S=\arg \max \left(\sigma\left(S_{1}\right), \sigma\left(s_{\max }\right)\right)\)
    output: selected seed set \(S\)
```

fastest. From the analysis, it is easy to see that the computation complexity depends on $n_{0}$ and $d$. The proposed approach is more efficient with smaller $n_{0}$ and $d$; that is, when the graph is sparse and the edge propagation probabilities are small, both are likely true in social networks.

## VII. Evaluation

In this section, we evaluate the performance of the proposed framework. First, an illustrative example is provided to highlight the difference in the two DAG construction models, and spread computation methods. Next, we present the implementation details and experimental setup. Finally, we present the results on 1) performance on real-world social networks and 2) impact of network structures using synthetic graphs.

## A. An Illustrative Example

Here, we consider a small scale network as shown in Figure 4(a). Figure 4(b) and (c) show the DAG constructed by the two models, and the activation probabilities by the
two methods. DAG 1 retains all the edges in the network (since the original graph is in fact a DAG), while DAG 2 has fewer edges. When LBP is used to compute the influence spread (the numbers on top next to each node), DAG 1 yields higher activation probability compared to DAG 2 for node B and node C since A has a large influence to B (0.5), which is not considered in DAG 2. In both DAGs, ignoring the possible correlation among parent nodes in SPBP, the activation probabilities tend to be bigger. Interestingly, though DAG 2 is a multi-connected graph, the activation probabilities computed by both methods are identical. Upon a close examination, we find that even though the graph is multiconnected, the activations of A and B are in fact independent since both are direct descendents of seed nodes with activation probability one.

## B. Experiment Setup

The algorithms and implementation: In addition to the two DAG models and two methods to compute influence spread (a total of 4 combinations DAG1-LBP, DAG1-SPBP, DAG2-LBP, and DAG2-SPBP), we make comparison with the following algorithms:

- PMIA $(\theta)$ [4]: a very fast heuristic algorithm that builds a tree-like structure model on which influence is spread. $\theta$ is the influence threshold. We will set $\theta=1 / 160$ in all experiments as it was reported to yield the best performance. The PMIA implementation provided by the authors is optimized for IM, and thus its performance for BIM is excluded.
- Greedy/CELF: The greedy approach from [3] with CELF optimization in [5]. The number of simulation rounds for each $\sigma(\cdot)$ estimation is 10,000 .
- Weighted Degree: The simple heuristic that selects $k$ seeds that have maximum total out-connection weight. Weighted Degree has been reported to be working very well in practice.
We do not compare with other heuristics such as SP1M, SPM [28], PageRank [29], Random, DegreeDiscountIC [7] or Betweenness centrality [30] since they have been reported in previous studies [4], [3] to be either unscalable or have poorer performance.

We have implemented the proposed algorithms in C++. All experiments are conducted on a workstation running Ubuntu 11.04 with an Intel Core i5 CPU and 2GB memory. In order to implement LBP algorithm, we use libDAI [31] and Boost [32] libraries. We find out through the implementation that running LBP on networks with high in-degree nodes is very costly. Therefore when running LBP, we prune incoming edges on high in-degree nodes such that only ten edges with the highest propagation probabilities are retained. The implementation of PMIA is obtained from its authors. Note that with code optimization, the running time of our algorithms can be further reduced.

Datasets: We use four real-world network datasets from [33] and [34] to compare performance of different algorithms. The four datasets were selected so as they are representative of the

![img-3.jpeg](img-3.jpeg)
(a) Real active probabilities
![img-4.jpeg](img-4.jpeg)
(b) Inference on DAG 1
![img-5.jpeg](img-5.jpeg)
(c) Inference on DAG 2

Fig. 4: Inference result on 2 DAG models. The real active probabilities are in green, LBP results are on top, in blue, and SPBP results are below, in red.

TABLE II: Network datasets


structural features of large-scale social networks, and are of different scales - from several thousands to millions of edges. The first one is an email exchange network in a research lab, denoted by Email. Each researcher is a vertex and an email from a researcher $u$ to $v$ constitutes an edge. The second network, denoted by p2p-Gnutella is a snapshot of the Gnutella peer-to-peer file sharing network from August 2002. Nodes represent hosts in the Gnutella network and edges represent connections between the Gnutella hosts. The third network comes from Slashdot.org, a technology-related news website, denoted by soc-Slashdot. In 2002, Slashdot introduced the Slashdot Zoo feature that allows users to tag each other as friends or foes. The network contains friend/foe links between Slashdot users obtained in February 2009. Finally, Amazon dataset is the product co-purchasing network collected by crawling Amazon website on March 2, 2003. Details of the datasets are summarized in Table II.

In addition to real social networks, we modified DIGG [35] source code and generated scale-free networks with different network densities and node out-degree distributions. The purpose which allows us to study the impact of graph structures and network property on the algorithm performance.

Probability generation models: Two models that have been used in previous work [3], [4] are: 1) the Weighted Cascade (WC) model where $p(u, v)=1 / d(v)$ where $d(v)$ is the indegree of $v$ and 2) the Trivalency (TV) model where $p(u, v)$ is assigned a small value for any $(u, v) \in E$. We argue that both models are not truthful reflections of the probability model in practice. The WC model assign a very high probability for a connections to nodes with small number of incoming connections while the TV model assigns a similar probability to all edges. In the evaluation, we consider two additional
models: 1) Random (RA) where $p(u, v)$ is randomly selected in the range $[0.001,0.2]$. RA is useful when no prior information regarding the influence is available; and 2) Power Law (PL) where $p(u, v)$ follows the power law distribution with the density function $p(x)=\alpha / x^{\beta}$, with $x$ be the propagation probability between two random edges $p(u, v)$. Parameters $\alpha=0.05$ and $\beta=0.9$ are selected so that $p(u, v)$ has the mean value 0.1 in the range $[0.001,0.2]$.

## C. Real Social Networks

Unit-cost version of BIM: BIM with unit-cost is the traditional IM problem where the seed set size $k$ is fixed. In this experiment, we run 7 algorithms: Greedy, PMIA, Weighted Degree, and the 4 proposed methods on 4 datasets presented in Table II. $k$ varies from 1 to 50, and we adopt the RA probability generation model.

Figure 5 shows the influence spread generated by the best seed sets in different algorithms as the seed size changes. Since Greedy does not scale with large datasets, we only run Greedy on Email and p2p-Gnutella. The influence spread from the seed set selected by each algorithm is determined by 10,000 rounds of Monte Carlo simulations on the original graphs.

In Figure 5(a), the performance of DAG1-LBP and Greedy (known to be within a constant ratio of the optimal) are not distinguishable (and thus are represented in one curve). The influence spread of DAG1-SPBP and DAG2-LBP/SPBP are shortly behind, all outperforming PMIA and Weighted Degree. We observe on Email dataset (a small but dense network) that both the structure of the DAG (DAG 1 vs. DAG 2) as well as the BP algorithm used (LBP vs. SPBP) will affect performance of the proposed methods. In contrast, as shown in Figure 5(b) - (d), the influence spreads of the four approaches DAG1/2-

![img-6.jpeg](img-6.jpeg)

Fig. 5: Influence spread with node unit-cost on 4 datasets. DAG 1 results are in red curves, DAG 2 are in blue curves, and other methods are in black curves.

![img-7.jpeg](img-7.jpeg)

Fig. 6: Computation time with node unit-cost on 4 datasets.

LBP/SPBP are identical for sparser networks, and is the same as Greedy in *p2p-Gnutella* dataset.

In terms of running time, Weighted Degree is the fastest. Among the four proposed approaches, DAG2–SPBP is the fastest, next are DAG2–LBP, DAG1–SPBP, and finally DAG1–LBP. DAG2–SPBP and PMIA have comparable order in running time with DAG2–SPBP being 30-40% slower than PMIA in most cases. Again, this may be primarily attributed to the lack of code optimization in our proposed methods.

Interestingly, influence spread on *Amazon* grows linearly with the seed size. Our result matches with that in [4]. This can be explained by the sheer scale of the network, and thus the small number of selected seeds are likely to have non-overlapping influence regions.

**General cost version of BIM:** In this set of experiments, we compare only 4 algorithms: Greedy/CELF, Weighted Degree, and DAG1/DAG2–SPBP on 4 datasets presented in Table II. We also omit the two methods that use LBP (DAG1/DAG2–LBP) from the result since they have comparable performance as the SPBP approaches. The budget $b = \{10, 15, 25, 40, 60, 100\}$, and the RA probability generation model is used. Nodal costs are selected uniformly in [1.0, 3.0].

Results in Figures 7 and 8 are similar to that in Figures 5 and 6. In most cases, DAG1 has better performance compared to DAG2. Notably, DAG1–SPBP outperforms Greedy/CELF on *p2p-Gnutella* dataset. Figure 8 shows that the proposed methods are several orders of magnitude faster than Greedy/CELF. Weighted Degree while being the fastest algorithm, does not perform nearly as well as the others on a dense graph (*Email*).

**Comparison of Influence Spread on Two DAG Models:** To understand the behavior of the proposed algorithms, we conduct further experiments on *Email* dataset as it gives the largest performance difference between the algorithms.

Figure 9(a) gives the number of vertices and edges as the result of the two DAG models with varying sizes of seed sets. Since both have the same number of vertices, only one curve is shown. It is clear that DAG1 is much denser than DAG2 due to the inclusion of more edges. As the seed set grows, the gap becomes smaller.

We use Root Mean Square Error (RMSE) to compare the activation probabilities on nodes. RMSE is defined as,

$$RMSE(p, p') = \sqrt{\frac{\sum_{\forall v \in V} (p'(v) - p(v))^2}{n}} / \frac{\sum_{\forall v \in V}^{n} p(v)}{n},$$

where $p'(·)$ is the inferred result from the propose algorithms. The ground truth $p(·)$ is determined by Monte Carlo simulations. When $p'(v) = p(v)$, $\forall v \in V$ then $RMSE(p, p') = 0$.

Figure 9(b) shows that DAG1 has smaller RMSE since it constructs a denser graph. More edges clearly improves the quality of the seed selection process. In the comparing LBP and SPBP, LBP is slightly better since SPBP ignores the correlation among node states. The combination of DAG1 and LBP yields the best inference result, but incurs higher computation complexity. The results are consistent with those in Figure 5(a).

### *D. Synthetic Networks*

In this section, we conduct three sets of experiment with 5 methods: CELF, PMIA, Weighted Degree and DAG1/2–SPBP. Synthetically generated networks are used to study the impact of network structures and probability generation models on performance of the algorithms. To isolate the effects of network properties, we only consider the unit cost BIM problem.

**Impact of network density:** Results from Figure 5 and 7 indicate that our proposed methods perform best on dense networks (*Email* and *p2p-Gnutella*). To further validate this observation, we generate 4 networks with 20k, 50k, 100k, and 200k edges using DIGG [35]. The number of vertices is fixed at 5,000. Seed set size $k = 50$ and probability model is RA. We

![img-8.jpeg](img-8.jpeg)

Fig. 7: Influence spread with random node costs on 4 datasets.

![img-9.jpeg](img-9.jpeg)

Fig. 8: Computation time with random node costs on 4 datasets.

![img-10.jpeg](img-10.jpeg)

Fig. 9: Size of DAGs and RMSE of activation probabilities. Results are averages of 50 runs with different seed selections and symmetric error bars indicate standard deviations.

evaluate the spread ratio of various algorithms, defined as the ratio of the spread attained to that by Greedy/CELF algorithm. From Figure 10(a), as the network density increases, the performance gap between the proposed algorithms and existing algorithms including CELF increases. CELF relies on many rounds of simulations to determine the spread. For dense networks, more rounds of simulations are needed to produce a spread estimation that is close enough to the *ground truth*. As a result, with a fixed number of simulation rounds, CELF has worse performance at high network densities. We also observe that PMIA, which was designed to take advantage of network sparsity; and Weighted Degree, which only uses local node information, do not perform well on densely connected graphs.

**Impact of probability generation model:** In this set of experiments, we run 5 algorithms on a synthetic network with 5,000 nodes and 50,000 edges. Each algorithm selects a seed set with size *k* = 50 under 4 propagation probability models: RA, TV, PL and WC. All models give similar performance except Weighted Degree on WC model. Recall that WC generates the propagation probabilities based on the in-degree of nodes, thus strong connections are established between nodes with low in-degree. Weighted Degree can't "see" those strong ties beyond the local edges, and therefore, has the worst performance.

**Impact of node out-degree distribution:** It is known that node out-degree in real social networks follows the power-law distribution [36]. Let *y* be the percentage of nodes with degree *x*, then we have *y* ∼ *α*/*x*<sup>*β*</sup>. *α* and *β* can be seen as the intercept and the (negative) slope when degree sequence is plotted on a log-log scale. While varying *α* only scales the distribution up or down, changing *β* alters the "shape" of the distribution. More specifically, a high value of *β* means the node out-degree distribution exhibits larger skew. The network in this case contains few "hubs" that are connected to many other nodes. On the other hand, a small *β* means that the distribution is fat-tailed and the max out-degree in the network is not much larger than the average out-degree. We run 5 algorithms to solve the unit-cost BIM problem on 4 generated

![img-11.jpeg](img-11.jpeg)

Fig. 10: Algorithm performance on different network conditions.

networks with β = {0.5, 1.0, 1.5, 2.0}. The network size is 5,000 and α is adjusted accordingly such that the total number of edges is roughly 50,000. We see from Figure 10(c) that the performance gap among the algorithms reduces with larger β. This is because with a large degree distribution skewness, nodes with high out-degree (hub) will almost certainly be one of the best seed candidates (unless their costs are too high, which is not this case). Simple algorithms such as Weighted Degree can easily identify such hub nodes. On the other hand, when the network is more "flattened", more sophisticated algorithms are necessary.

### *E. Summary*

From the experiment results, Weighted Degree gives the best efficiency in terms of spread/complexity. However, its performance degrades significantly on dense networks or more heavy-tailed power-law graphs. The same conclusion is applied to PMIA. Even though being faster than our algorithms, PMIA shows little improvement in terms of attainable spread compared to Weighted Degree, except under the WC model. Our proposed schemes surpass the others in all the experimented datasets. They also offer more application flexibility: one would apply the best-performed algorithm (DAG1–LBP) on static networks (e.g.: network of connections between coworkers) to identify the most influential nodes, or apply the fastest algorithm (DAG2–SPBP) on rapidly changing communities (e.g.: network of connections between people in a social group) to obtain immediate results.

## VIII. CONCLUSION

While recent researches focus on solving the IM problem, we considered in this paper the BIM problem, which is a generalization of the former one. The study on real-world datasets and synthetic datasets with controllable network parameters provides convincing evidence that the proposed algorithms have superior performance. Furthermore, we gain some insights on the choice of algorithms in trading computation complexity with performance given the network structure.

## IX. ACKNOWLEDGMENT

This work is supported in part by the National Science Foundation under grants CNS-1117560 and CNS-0832084.

## APPENDIX

## Proof of Theorem 1:

Proof: The proof is an adaption of the proof in [4] and Valiant's original proofs of the \#P-completeness of the $s-t$ connectedness in a direct graph [37]. First, we define a few problems that are known or to be proven to be \#P-complete.

Definition 4: (SAT')
Input: $F=c_{1} \wedge c_{2} \wedge \ldots c_{r}$, where $c_{i}=\left(y_{i 1} \vee y_{i 2}\right)$ and $y_{i j} \in X$, Output: $\mid\left\{(\mathbf{x}, \mathbf{t}) \mid \mathbf{t}=\left(t_{1}, t_{2}, \ldots, t_{n}\right) \in\{1,2\}^{n}\right.$; for $1 \leq i \leq r$, $\mathbf{x}$ make $y_{i, k}$ true for $k=t_{i}$.
Definition 5: (S-SET CONNECTEDNESS on DAG)
Input: A DAG $\mathcal{D}=(V, E) ; s \in V ; V^{\prime} \in V$.
Output: Number of subgraphs of $\mathcal{D}$ in which for each $u \in V^{\prime}$, there is a (directed) path from $s$ to $u$.
Definition 6: (S-T CONNECTEDNESS on DAG)
Input: A DAG $\mathcal{D}=(V, E) ; s, t \in V$.

Output: Number of subgraphs of $\mathcal{D}$ in which there is a directed path from $s$ to $t$.
To prove Theorem 1, we first establish the following lemma.
Lemma 1: $S A T^{\prime} \preceq_{p}$ S-T CONNECTEDNESS on DAG.
Proof: Given $F$ construct a DAG $\mathcal{D}=\left(V, E_{1} \cup E_{2}\right)$ where $V=\left\{c_{1}, c_{2}, \ldots, c_{r+1}, x_{1}, \ldots, x_{n}, \bar{x}_{1}, \ldots, \bar{x}_{n}, s\right\}, E_{1}=$ $\left\{\left(x_{i}, c_{j}\right) \mid x_{i}\right.$ appears in clause $c_{j}$ in $\left.F\right\} \bigcup\left\{\left(x_{n}, c_{r+1}\right),\left(\bar{x}_{n}, c_{r+1}\right)\right\}$, and $E_{2}=\left\{\left(x_{i}, x_{i+1}\right),\left(\bar{x}_{i}, x_{i+1}\right),\left(\bar{x}_{i}, \bar{x}_{i+1}\right),\left(x_{i}, \bar{x}_{i+1}\right) \mid 1 \leq\right.$ $i \leq n\} \bigcup\left\{\left(s, x_{1}\right),\left(s, \bar{x}_{1}\right)\right\}$. The direction of each edge follows the order of the pairs. $\mathcal{D}$ is a DAG as edges only go from $x$ 's of smaller index to larger ones, and from $x$ 's to $c$ 's. Note the $\mathcal{D}$ is multi-connected. The rest of the proof follows that in [37].
Theorem 1 can then be proved using the same argument as in [4] with the exception that the reduction is from the S-T CONNECTEDNESS on DAGs due to Lemma 1.

## Proof of Proposition 1:

Proof: In both algorithms, a node $v$ is not included in the DAG if and only if $r(v)>\theta$. Thus, $V_{\mathcal{D}_{1}}=V_{\mathcal{D}_{2}}$.

To show $E_{\mathcal{D}_{2}} \subseteq E_{\mathcal{D}_{1}}$, it suffices to show that $\forall(u, v) \in$ $E_{\mathcal{D}_{2}},(u, v) \in E_{\mathcal{D}_{1}}$. Since $(u, v) \in E_{\mathcal{D}_{2}},(u, v) \in E$ and $r(u) \leq r(v)$. Therefore, according to Algorithm 2, $(u, v) \in$ $E_{\mathcal{D}_{2}}$. Clearly, the converse is not true as some edges in $E_{\mathcal{D}_{1}}$ may not be part of the $M I O A$ from any seed node.

## Proof of Proposition 2:

Proof: It is easy to see that by limiting the spread from $u$ in $\operatorname{MIOA}(\mathcal{G}, u, \theta)$, then $p(w), \forall w \in \operatorname{MIOA}(\mathcal{G}, v, \theta)$ will not be affected by the inclusion of $u$ in the seed set.

## Proof of Theorem 2:

First we establish the following lemma. Let $r$ be the number of iterations executed by the repeat loop in Algorithm 1. Let $S$ be the current seed set and $S^{*}$ be the optimal seed set. Without loss of generality, we may renumber nodes that was added to $S$ follow the chronicle order $S=\left\{u_{1}, u_{2}, \cdots, u_{l}\right\}$. Let $S_{i}=\bigcup_{j=1}^{i} u_{j}$ and let $j_{i}$ be the index of the iteration in which $u_{i}$ was considered.

Lemma 2: After each iteration $j_{i}, i=1, \cdots, l+1$, the following holds:

$$
\sigma\left(S_{i}\right) \geq\left[1-\prod_{k=1}^{i}\left(1-\frac{c(k)}{b}\right)\right] \sigma\left(S^{*}\right)
$$

Proof: The proof of Lemma 2 was first presented by Khuller et al. in [20] for the budgeted maximum coverage problem, which is a special case of BIM where all the active edge probabilities are 1. Later, it was extended by Krause et al. (Lemma 3 in [38]) for general submodular functions.

Now we're in position to prove Theorem 2:
Proof: (Adapted from [20]) We prove Theorem 1 by case analyzing Algorithm 2.

- Case 1: If there exist at lease a node $u \in V$ which has spread greater than $\frac{1}{2} \sigma\left(S^{*}\right)$, then $u$ or any other nodes which possess a greater spread, will be selected as the second candidate $S_{2}$. Algorithm 2 will therefore guarantee at least $\frac{1}{2} \sigma\left(S^{*}\right)$.

- Case 2: If there is no such node.
- Case 2.1: If $c(S)<\frac{1}{2} b$, then we have $c(u)>\frac{1}{2} b, \forall u \notin$ $S$ since there is no more node that can be added to $S$ without violating the budget constrain. W.l.o.g, we assume $S \neq S^{*}$. Therefore, $S^{*} \backslash S$ contains at most 1 node $v$, otherwise $c\left(S^{*}\right)>b$. By submodularity definition we have,

$$
\begin{aligned}
\sigma\left(S^{*} \cap S\right)+\sigma(v) & \geq \sigma\left(\left(S^{*} \cap S\right) \cup v\right)+\sigma\left(\left(S^{*} \cap S\right) \cap v\right) \\
& \geq \sigma\left(S^{*}\right)+\sigma(\emptyset) \\
& \geq \sigma\left(S^{*}\right)
\end{aligned}
$$

By assumption, we have $\sigma(v)<\frac{1}{2} \sigma\left(S^{*}\right)$, therefore $\sigma\left(S^{*} \cap S\right) \geq \frac{1}{2} \sigma\left(S^{*}\right)$. It follows that $\sigma(S) \geq \frac{1}{2} \sigma\left(S^{*}\right)$.

- Case 2.2: If $c(S) \geq \frac{1}{2} b$. We first observe that for $a_{1}, \cdots a_{n} \in \mathbb{R}$ and $\sum_{i=1}^{n} a_{i} \geq \alpha A$, the function,

$$
\prod_{i=1}^{n}\left(1-\frac{a_{i}}{A}\right)
$$

is maximized when $a_{i}=\frac{\alpha A}{n}$. By Lemma 2, we have,

$$
\begin{aligned}
\sigma\left(S_{i}\right) & \geq\left[1-\prod_{k=1}^{i}\left(1-\frac{c(k)}{b}\right)\right] \sigma\left(S^{*}\right) \\
& \geq\left[1-\left(1-\frac{1}{2 i}\right)^{i}\right] \sigma\left(S^{*}\right) \\
& \geq\left(1-\frac{1}{\sqrt{e}}\right) \sigma\left(S^{*}\right)
\end{aligned}
$$

Thus, in the worst case, Algorithm 2 provides a (1-$1 / \sqrt{e})$-approximation.