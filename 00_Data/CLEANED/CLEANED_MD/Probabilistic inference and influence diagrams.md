# Probabilistic Inference in Influence Diagrams 

Nevin Lianwen Zhang<br>Department of Computer Science, Hong Kong University of Science \& Technology<br>lzhang@cs.ust.hk


#### Abstract

This paper is about reducing influence diagram (ID) evaluation into Bayesian network (BN) inference problems. Such reduction is interesting because it enables one to readily use one's favorite BN inference algorithm to efficiently evaluate IDs. Two such reduction methods have been proposed previously (Cooper 1988, Shachter and Peot 1992). This paper proposes a new method. The BN inference problems induced by the mew method are much easier to solve than those induced by the two previous methods.


Keywords: Decision analysis, influence diagrams, Bayesian networks, inference.

## 1 Introduction

Influence diagrams (IDs) (Howard and Matheson 1984) are a popular framework for decision analysis. An ID is an acyclic graph with three types of nodes: random nodes, decision nodes, and a single value node. Each random node is associated with a conditional probability table (CPT) and the value node is associated with a utility function. Evaluating an ID means finding an optimal decision rule for each of its decision nodes.

IDs without decision and value nodes are called Bayesian networks ${ }^{1}$ (BNs) (Pearl 1988). They are widely used by AI researchers as a knowledge representation framework for reasoning under uncertainty. There is a rich collection of exact and approximate algorithms for inference in BNs. This paper is about how to reduce ID evaluation into BN inference problems that are as easy to solve as possible. Such reduction is interesting because it enables one to readily

[^0]use one's favorite BN inference algorithm to efficiently evaluate IDs.

Cooper (1988) initiated research in this direction. He proposed a transformation of an ID into a BN and showed that optimal decision rules can be found by posing an appropriate sequence of queries to the BN. Several improvements were later introduced by Shachter and Peot (1992). This paper proposes a new method. The BN inference problems induced by the new method are much easier to solve than those induced by the two previous methods.

There are several algorithms that evaluate IDs directly without the reduction into BN inference problems (Shachter 1986, Shenoy 1992, Ndilikilikesha 1994, and Jensen et al 1994). We call them direct evaluation algorithms. An method that reduces ID evaluation into BN inference problems would be unattractive if, no matter what BN inference algorithms are used, it is less efficient than the best direct evaluation algorithm. We show that the performance of our new method, when coupled with a BN inference algorithm called VE (Zhang and Poole 1996), is always within a constant factor of the performance of the best direct evaluation method and argue that it is usually more efficient.

The fact that arbitrary BN inference algorithms can used for probabilistic calculations makes our method very attractive as compared to direct evaluation algorithms. From a system development point of view, the method enables one to easily add ID evaluation capabilities to any BN inference packages. From the efficiency point of view, speeding up inference in BNs has been and still is an active research area. There are algorithms that exploit independence of causal influence (e.g. Zhang and Poole 1996) and that exploit special structures in the conditional probability tables. The new method facilitates ready incorporation of those algorithms, as well as future advances in BN inference, in ID evaluation. We are not aware of any approximate algorithms for IDs, while there is a rich collection of


[^0]:    ${ }^{1}$ Also known as belief networks and probabilistic influence diagrams.

approximate and simulation algorithms for BNs. The new method also opens up the possibility of approximate algorithms for ID, which might be necessary in order to solve large decision problems.

We will begin with definitions related to influence diagrams and a brief review of Shachter and Peot's method (Section 2). Foundations for our new method will be laid in Section 3 and details will be worked out in Section 4. The new method will be illustrated through an example in Section 5 and compared with Shachter and Peot's method and direct evaluation algorithms in Section 6. Conclusions will be drawn in Section 7.

## 2 Influence diagrams

In the original definition of IDs (Howard and Matheson 1984), there is only one value node. We allow multiple value nodes here so that separability in the utility function can be represented. See Tatman and Shachter (1990) for discussions on separability of utility functions.

IDs are required to satisfy several constraints. First, value nodes cannot have children. Second, IDs must be regular in the sense that there must be a directed path that contains all the decision nodes. The last decision node on the path will be referred to as the tail decision node. Third, they must be no-forgetting in the sense that a decision node and its parents be parents to all subsequent decision nodes. The rationale behind the no-forgetting constraint is that information available now should also be available later if the decision-maker does not forget.

Value networks refer to IDs that do not contain decision nodes. Bayesian networks (BNs) (Pearl 1988) are IDs that consists of only random nodes. In the following, the terms "nodes" and "variables" will be used interchangeably.

We shall use $\Omega_{x}$ to denote the frame of variable $x$, i.e. the set of possible values of $x$. For a set $X$ of variables, $\Omega_{X}$ stands for the Cartesian product $\prod_{x \in X} \Omega_{x}$.
Let $d_{1}, \ldots, d_{k}$ be all the decision nodes in an ID $\mathcal{N}$. A decision rule for a decision node $d_{i}$ is a mapping $\delta_{i}: \Omega_{\pi_{d_{i}}} \rightarrow \Omega_{d_{i}}$. A policy is a list of decision rules $\Delta=\left(\delta_{1}, \ldots, \delta_{k}\right)$ consisting of one rule for each decision node. To evaluate an ID is to find an optimal policy that maximizes the expected utility and to compute the optimal expected utility.
ID evaluation requires a lot of probabilistic calculations. This paper is concerned with identifying a set of probabilistic inference problems such that optimal decision rules can be readily obtained from their so-
lutions. The problems should be as easy to solve as possible.
Cooper (1988) initiated research in this direction. Several improvements to Cooper's method were proposed by Shachter and Peot (1992). This section briefly reviews the method by Shachter and Peot.

The method applies only in the case when there is one value node. Let $\mathcal{N}$ be an ID with one value node. Denote the value node by $v$. For simplicity, assume that the utility function $f_{v}\left(\pi_{v}\right)$ of $v$ is non-negative ${ }^{2}$. The node is converted into a binary random node with the following conditional probability:

$$
\begin{aligned}
& P\left(v=1 \mid \pi_{v}\right)=\frac{f_{v}\left(\pi_{v}\right)}{M_{v}} \\
& P\left(v=0 \mid \pi_{v}\right)=1-P\left(v=1 \mid \pi_{v}\right)
\end{aligned}
$$

where $M_{v}=\max _{\pi_{v}} f_{v}\left(\pi_{v}\right)$. This transformation will be referred to as Cooper's transformation.
Each decision node $d$ is also converted into a random node with the following conditional probability:

$$
P\left(d=\alpha \mid \pi_{d}\right)=1 /\left|\Omega_{d}\right|
$$

for each possible value $\alpha$ of $d$, where $\left|\Omega_{d}\right|$ is the number of possible values of $d$. After the transformations, $\mathcal{N}$ becomes a BN. Denote the BN by $\mathcal{N}^{\prime}$.

According to the regularity constraint, there exists a directed path that contains all decision nodes. Let $d_{1}$, $\ldots, d_{k}$ an enumeration of the decision nodes in the order they appear in the path. It is shown that an optimal decision rule $\delta_{k}^{*}$ for $d_{k}$ can be obtained by

$$
\delta_{k}^{*}\left(\pi_{d_{k}}\right)=\arg \max _{d_{k}} P_{\mathcal{N}^{\prime}}\left(d_{k}, \pi_{d_{k}} \mid v=1\right)
$$

After the rule has been computed, the conditional probability of $d_{k}$ is changed to $P_{\delta_{k}^{*}}\left(d_{k} \mid \pi_{d_{k}}\right)$. An optimal decision rule for $d_{k-1}$ is then computed using the same formula except with $k$ replaced by $k-1$. Optimal decision rules for $d_{k-2}, \ldots, d_{1}$ are computed recursively in the same fashion.

Shachter and Peot's method reduces the evaluation of $\mathcal{N}$ into the following BN inference problems:
$P_{\mathcal{N}^{\prime}}\left(d_{k}, \pi_{d_{k}} \mid v=1\right), P_{\mathcal{N}^{\prime}}\left(d_{k-1}, \pi_{d_{k-1}} \mid v=1\right), \ldots, P_{\mathcal{N}^{\prime}}\left(d_{1}, \pi_{d_{1}} \mid v=\right.$
We will show that an ID can be evaluated by solving BN inference problems that are much easier than those listed above.

[^0]
[^0]:    ${ }^{2}$ If the utility function takes negative values, a constant can be added to it so that it takes only non-negative values. Addition of a constant to the utility function does not change the optimal policies. Moreover, the optimal expected value of an ID equals to its optimal expected value after the addition of the constant minus the constant.

![img-0.jpeg](img-0.jpeg)

Figure 1: An ID. Random nodes are drawn as ellipses, decision nodes as rectangles, and value nodes as diamonds.

## 3 Decomposition theorem

Suppose $\mathcal{N}$ is an ID and $d$ is the tail decision node. This section shows that $\mathcal{N}$ can be decomposed into two components, called tail and body respectively, such that an optimal decision rule for $d$ can be found in the tail and optimal decision rules for all other decision nodes can be found in the body. The body is again an ID and hence the decomposition can be repeated in the body.

### 3.1 Downstream and upstream sets

We begin by partitioning the set of nodes in $\mathcal{N}$ into several subsets w.r.t to the tail decision node $d$. The moral graph of an ID is obtained by first adding undirected edges between pairs of parents of each node so that they are pairwise connected and then dropping directions of all the directed edges. Let $x$ and $y$ be two nodes and $S$ be a set of nodes that does not contain $x$ or $y$. We say that $S m$-separates $x$ and $y$ if, in the moral graph, every path connecting them contains at least one node in $S$.

Let $X$ be the set of all nodes in an ID $\mathcal{N}$. The $u p$ stream set of $\mathcal{N}$ w.r.t to $d$, denoted by $X_{1}$, is the set of nodes in $X \backslash \pi_{d}$ that are m-separated from $d$ by $\pi_{d}$. The downstream set of $\mathcal{N}$ w.r.t d, denoted by $X_{2}$, is the set of nodes in $X \backslash \pi_{d}$ that are not m-separated from $d$ by $\pi_{d}$. Note that $d \in X_{2}$ and that the three sets $X_{1}, \pi_{d}$ and $X_{2}$ constitute a partition of the set $X$.

Define $\pi_{d, 2}$ be the set of nodes in $\pi_{d}$ that have at least one parent in $X_{2}$ and set $\pi_{d, 1}=\pi_{d} \backslash \pi_{d, 2}$. The four sets $X_{1}, X_{2}, \pi_{d, 1}$, and $\pi_{d, 2}$ constitute another partition of $X$.

Consider the ID in Figure 1. The set of parents of $d_{2}$ is $\pi_{d_{2}}=\left\{d_{1}, c_{3}, c_{4}\right\}$ and the downstream set $X_{2}$ w.r.t $d_{2}$ is $X_{2}=\left\{d_{2}, c_{6}, v_{2}\right\}$. Since $c_{4}$ the only parent of $d_{2}$ that has a parent in the downstream set, $\pi_{d_{2}, 2}=\left\{c_{4}\right\}$. Hence $\pi_{d_{2}, 1}=\left\{d_{1}, c_{3}\right\}$.
A node $x$ is an ancestor to another node $y$ if there is a directed path from $x$ to $y$. A ancestral set an $(A)$ of a
![img-1.jpeg](img-1.jpeg)

Figure 2: Tail and body: The BN in (2) is the tail of the influence diagram in Figure 2 w.r.t $d_{2}$; probabilities of the dashed nodes are uniform distributions. The ID in (1), with the value node $u$ ignored, is the body of the ID in Figure 2 with w.r.t $d_{2}$. With $u$, it is the augmented body (Subsection 3.2).
set of nodes $A$ consists of nodes in $A$ and their ancestors. The following proposition summarizes properties of the aforementioned sets.

Proposition 1 Suppose $d$ is the tail decision node in an ID. Then (1) the node $d$ is the only decision node in the downstream set $X_{2}$; (2) all nodes in $\pi_{d, 2}$ are random nodes; (3) all nodes in an $\left(\pi_{d, 2}\right) \cap X_{2}$ are random nodes; and (4) all other decision nodes are in $\pi_{d, 1}$.

### 3.2 Bodies and tails

The body of $\mathcal{N}$ w.r.t $d$ is an ID given by:
Procedure body $(\mathcal{N}, d)$ :

1. Prune from $\mathcal{N}$ all the nodes in $X_{2} \backslash a n\left(\pi_{d, 2}\right)$.
2. Return the resulting ID.

We use $\mathcal{B}$ to denote the body. According to Proposition 1 (4), for any decision node $d^{\prime} \neq d, d^{\prime}$ is in $\mathcal{B}$ and it has the same parents in $\mathcal{B}$ as in $\mathcal{N}$.

Define the tail of $\mathcal{N}$ w.r.t d by the following procedure:
Procedure $\operatorname{tail}(\mathcal{N}, d)$ :

1. Prune from $\mathcal{N}$ all nodes in $X_{1}$.
2. Prune arcs into $d$ and nodes in $\pi_{d, 1}$.
3. Prune conditional probabilities of random nodes in $\pi_{d, 1}$.
4. For each node $x \in\{d\} \cup \pi_{d, 1}$, set $P_{T}(x)=1 /\left|\Omega_{x}\right|$, where $\left|\Omega_{x}\right|$ is the number of possible values of $x$.
5. Convert all the value nodes in $X_{2}$ into random nodes by Cooper's transformation.
6. Return the resulting BN.

We use $\mathcal{T}$ to denote the tail. It is a BN for the following reasons. It consists the decision node $d$, nodes in $\pi_{d, 1}$, nodes in $\pi_{d, 2} \cup X_{2} \backslash\{d\}$. The node $d$ and nodes in $\pi_{d, 1}$ are associated with uniform distributions. According to Proposition 1, nodes in $\pi_{d, 2} \cup X_{2} \backslash\{d\}$ are either random nodes or value nodes. Random nodes in the set inherit their conditional probabilities from $\mathcal{N}$, while conditional probabilities for value nodes in the set are obtained from their utility functions via Cooper's transformation. So all nodes in $\mathcal{T}$ are associated with probabilities and hence $\mathcal{T}$ is a BN.

Let $V_{2}$ be the set of all value nodes in the tail. Define the evaluation functional $e_{\mathcal{T}}\left(\pi_{d}, d\right)$ of the tail $\mathcal{T}$ by

$$
e_{\mathcal{T}}\left(\pi_{d}, d\right)=\sum_{v \in V_{2}} P_{\mathcal{T}}\left(v=1 \mid \pi_{d}, d\right) M_{v}
$$

### 3.3 Decomposition theorem

Define the augmented body of $\mathcal{N}$ w.r.t $d$ by the following procedure:

Procedure augBody $\left(\mathcal{N}, d, e_{\mathcal{T}}\left(\pi_{d}, d\right)\right)$ :

1. $\mathcal{B}=\operatorname{body}(\mathcal{N}, d)$.
2. Introduce a new value node $u$ to $\mathcal{B}$. Make it a child of each node in $\pi_{d}$ and set its utility function as follows:

$$
f_{u}\left(\pi_{u}\right)=\max _{d} e_{\mathcal{T}}\left(\pi_{d}, d\right)
$$

3. Return the resulting ID.

We use $\mathcal{B}$ to denote the augmented body from now on.
Theorem 1 (Decomposition Theorem)

1. An optimal decision rule $\delta^{*}$ for the tail decision node $d$ is given by

$$
\delta^{*}\left(\pi_{d}\right)=\arg \max _{d} e_{\mathcal{T}}\left(\pi_{d}, d\right)
$$

2. A policy $\Delta_{1}$ for the augmented body $\mathcal{B}$ of $\mathcal{N}$ w.r.t $d$ is optimal if and only if the policy $\left(\Delta_{1}, \delta^{*}\right)$ is optimal for $\mathcal{N}$.
3. The optimal expected value of $\mathcal{B}$ is the same as that of $\mathcal{N}$.

## 4 Evaluating IDs

The decomposition theorem gives us the following procedure for evaluating an ID: (1) decompose it to two components - tail and body - w.r.t the tail decision node, (2) find an optimal decision rule for the tail decision node in the tail, and (3) repeat the process in
the body. This section looks at the necessary computations in more detail and identifies the BN inference problems that one needs to solve. We also introduce several optimizations that make the BN inference problems easier to solve.

### 4.1 Simplifying computations in the tail

To obtain the evaluation functional $e_{\mathcal{T}}\left(\pi_{d}, d\right)$ of the tail $\mathcal{T}$, we need to compute the marginal probability $P_{\mathcal{T}}\left(\pi_{d}, d\right)$ and the marginal probability $P_{\mathcal{T}}\left(v=1, \pi_{d}, d\right)$ for each value node $v \in V_{2}$. This subsection shows that some of the nodes that appear in the marginal probabilities can be deleted and that some of the nodes in $\mathcal{T}$ can be pruned when computing each of the marginal probabilities.

### 4.1.1 Irrelevant parents of decision nodes

Let $\pi_{d, i}$ be the set of nodes in $\pi_{d, 1}$ that, in $\mathcal{N}$, are not parents to nodes in $\pi_{d, 2} \cup X_{2} \backslash\{d\}$. Each $x \in \pi_{d, i}$ is an isolated node in $\mathcal{T}$ for the following reasons. First, $x$ has no parents in $\mathcal{T}$ since arcs into nodes in $\pi_{d, 1}$ have been removed by tail. Second, $x$ has no children in $\mathcal{T}$. This is because $\mathcal{T}$ consists of the node $d$, nodes in $\pi_{d, 1}$, and nodes in $\pi_{d, 2} \cup X_{1} \backslash\{d\}$. The node $d$ and nodes in $\pi_{d, 1}$ cannot be children of $x$ since all arcs into them have been removed by tail and nodes $\pi_{d, 2} \cup X_{1} \backslash\{d\}$ are not children of $x$ by the definition of $\pi_{d, i}$. Define the reduced tail of $\mathcal{N}$ w.r.t $d$ by the following procedure:

Procedure redTail $(\mathcal{N}, d)$ :

1. $\mathcal{T}=\operatorname{tail}(\mathcal{N}, d)$.
2. Prune from $\mathcal{T}$ nodes in $\pi_{d, i}$.
3. Return the resulting BN.

We use $\mathcal{T}_{r}$ to denote the reduced tail. It consists of nodes in $\pi_{d, r} \cup X_{2}$, where $\pi_{d, r}=\pi_{d} \backslash \pi_{d, i}$. Because each member of $\pi_{d, i}$ is an isolated node in $\mathcal{T}$ and its probability is the uniform distribution, the joint probabilities of $\mathcal{T}$ and $\mathcal{T}_{r}$ are related by

$$
P_{\mathcal{T}}\left(\pi_{d}, X_{2}\right)=P_{\mathcal{T}_{r}}\left(\pi_{d, r}, X_{2}\right) \prod_{x \in \pi_{d, i}} 1 /\left|\Omega_{x}\right|
$$

where $\left|\Omega_{x}\right|$ is the number of possible values of $x$. Therefore

$$
e_{\mathcal{T}}\left(\pi_{d}, d\right)=\sum_{v \in V_{2}} \frac{P_{\mathcal{T}_{r}}\left(v=1, \pi_{d, r}, d\right)}{P_{\mathcal{T}_{r}}\left(\pi_{d, r}, d\right)} M_{v}
$$

Hence the evaluation functional can be computed from the marginal probability $P_{\mathcal{T}_{r}}\left(\pi_{d, r}, d\right)$ and the marginal probability $P_{\mathcal{T}_{r}}\left(v=1, \pi_{d, r}, d\right)$ for each value node $v \in V_{2}$. Those marginal probabilities involve less nodes than $P_{\mathcal{T}}\left(\pi_{d}, d\right)$ and $P_{\mathcal{T}}\left(v=1, \pi_{d}, d\right)$.

Equation (4) also implies that the evaluation functional does not depend on nodes in $\pi_{i}$ and can be rewritten as $e_{\mathcal{T}}\left(\pi_{d, r}, d\right)$. This fact in turn has two implications. First, the optimal decision rule for $d$ given by equation (3) does not depend on nodes in $\pi_{d, i}$. For this reason, nodes in $\pi_{d, i}$ will be called irrelevant parents of $d$ (Tatman and Shachter 1990) and the nodes in $\pi_{d, r}$ will be called relevant parents of $d$.

Second, the utility function of the new value node $u$ in the augmented body $\mathcal{B}$ does not depend on the irrelevant parents of $d$. Consequently there is no need to make $u$ a child to those nodes. From now on we assume that, in $\mathcal{B}, u$ is a child of only relevant parents of $d$ and its utility function of $u$ is given by

$$
f_{u}\left(\pi_{d, r}\right)=\max _{d} e_{\mathcal{T}}\left(\pi_{d, r}, d\right)
$$

We will use $\mathcal{T}$ to denote the reduced body from now on.

### 4.1.2 Pruning irrelevant nodes

For any $v \in V_{2}$, consider $P_{\mathcal{T}}\left(v=1, \pi_{d, r}, d\right)$. It is well known that nodes outside $a n\left(\pi_{d, r} \cup\{d, v\}\right)$ are irrelevant to the marginal probability (e.g. Shachter 1988). Let $\mathcal{T}_{v}$ be the BN obtained from $\mathcal{T}$ by pruning nodes outside $a n\left(\pi_{d, r} \cup\{d, v\}\right)$. Then $P_{\mathcal{T}}\left(v=1, \pi_{d, r}, d\right)=$ $P_{\mathcal{T}_{v}}\left(v=1, \pi_{d, r}, d\right)$.
Similarly, let $\mathcal{T}^{\prime}$ be the BN obtained from $\mathcal{T}$ by pruning nodes outside $a n\left(\pi_{d, r} \cup\{d\}\right)$. Then $P_{\mathcal{T}}\left(\pi_{d, r}, d\right)=$ $P_{\mathcal{T}^{\prime}}\left(\pi_{d, r}, d\right)$. Consider the node $d$. It has no parents in $\mathcal{T}$ and hence has no parents in $\mathcal{T}^{\prime}$. Children of $d$ in $\mathcal{T}$ cannot be in the ancestral set $q n\left(\pi_{d, r} \cup\{d\}\right.$, for otherwise there would directed loops in the original ID. Hence children of $d$ are not in $\mathcal{T}^{\prime}$. Therefore $d$ is an isolated node in $\mathcal{T}^{\prime}$. Let $\mathcal{T}_{c}$ be obtained from $\mathcal{T}^{\prime}$ by pruning the isolated node $d$. Since the probability of $d$ is the uniform distribution, $P_{\mathcal{T}^{\prime}}\left(\pi_{d, r}, d\right)=P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right) /\left|\Pi_{d}\right|$.
For any BN $\mathcal{M}$ and any subset $A$ of nodes in $\mathcal{M}$, let $\operatorname{BNinf}(A, \mathcal{M})$ be a procedure that computes the marginal probability $P_{\mathcal{M}}(A)$. Arbitrary BN inference algorithms can be used in the procedure. According to the foregoing discussions, the evaluation functional $e_{\mathcal{T}}\left(\pi_{d, r}, d\right)$ can be obtained by using the following procedure:

Procedure evalFun $(\mathcal{T}, d)$

1. Obtain $\mathcal{T}_{c}$ from $\mathcal{T}$ by pruning nodes outside $a n\left(\pi_{d, r}\right)$. Compute $P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right)$ by calling $\operatorname{BNinf}\left(\pi_{d, r}, \mathcal{T}_{c}\right)$.
2. For each $v \in V_{2}$, obtain $\mathcal{T}_{v}$ by pruning nodes outside $a n\left(\pi_{d, r} \cup\{d, v\}\right)$. Compute $P_{\mathcal{T}_{v}}\left(v=1, \pi_{d, r}, d\right) \quad$ by calling $\operatorname{BNinf}\left(\left(v=1, \pi_{d, r}\right), \mathcal{T}_{v}\right)$
3. Set

$$
e_{\mathcal{T}}\left(\pi_{d, r}, d\right)=\frac{\sum_{v \in V_{2}} P_{\mathcal{T}_{v}}\left(v=1, \pi_{d, r}, d\right)}{P_{\mathcal{T}_{v}}\left(\pi_{d, r}\right) /\left|\Pi_{d}\right|}
$$

4. Return $e_{\mathcal{T}}\left(\pi_{d, r}, d\right)$ and $P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right)$.

Note that the following BN inference problems are solved:

$$
P_{\mathcal{T}_{v}}\left(\pi_{d, r}\right), P_{\mathcal{T}_{v}}\left(v=1, \pi_{d, r}, d\right) \text { for each } v \in V_{2}
$$

Also note that in addition to the evaluation functional, evalFun also returns the marginal potential $P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right)$. It will be used in the next subsection.

### 4.2 Simplifying computations in the body

The augmented body $\mathcal{B}$ contains nodes in the set $a n\left(\pi_{d, 2}\right) \cap X_{2}$. The set is empty when no nodes in $\pi_{d}$ have parents in $X_{2}$, i.e. when $\pi_{d, 2}=\emptyset$. This subsection is concerned with the case when the set is not empty and shows that nodes in the set can be pruned from $\mathcal{B}$. Pruning nodes from $\mathcal{B}$ simplifies computations in the body.

Pruning nodes in $a n\left(\pi_{d, 2}\right) \cap X_{2}$ from $\mathcal{B}$ requires conditional probabilities of some of the remaining nodes be changed. The changes can be made with little numerical computation by using the marginal probability $P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right)$. Since the marginal probability must be computed in order to obtain the evaluation functional of the reduced tail, the cost of node pruning is small.
The resulting ID after pruning $a n\left(\pi_{d, 2}\right) \cap X_{2}$ from $\mathcal{B}$ will be called the reduced body of $\mathcal{N}$ w.r.t $d$. Formally, it is obtained from the augmented body $\mathcal{B}$, the reduced tail $\mathcal{T}$, and the marginal probability $P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right)$ via the following procedure:

Procedure redBody $\left(\mathcal{B}, P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right), \mathcal{T}\right)$ :

1. Prune from $\mathcal{B}$ all nodes in $a n\left(\pi_{d, 2}\right) \cap X_{2}$.
2. Prune arcs into and conditional probabilities of nodes in $\pi_{d, 2}$.
3. (Enumerate all nodes in $\pi_{d, 2}$ as $c_{1}, \ldots$, $c_{k}$ such that, in $\mathcal{N}, c_{i}$ is not an ancestor of $c_{j}$ if $i>j$. Let $Z_{i}$ be the set of nodes in $Z=\pi_{d, r} \cap \pi_{d, 1}$ that, in $\mathcal{T}$, are ancestors to $c_{1}$, or $c_{2}, \ldots$, or $c_{i}$.) For each $i$, make $c_{i}$ a child of each node in $\left\{c_{1}, \ldots, c_{i-1}\right\} \cup Z_{i}$ and define

$$
P\left(c_{i} \mid c_{1}, \ldots, c_{i-1}, Z_{i}\right)=\frac{\sum_{c_{i+1}, \ldots, c_{k}} P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right)}{\sum_{c_{i}, c_{i+1}, \ldots, c_{k}} P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right)}
$$

4. Return the resulting ID.

It is proved in the longer version of the paper that the reduced body is indeed an ID and it has the same optimal policies and optimal expected value as the body.

### 4.3 Expected values of value networks

The expected value of a value network is the sum of the expectations of all its utility functions. If one evaluates an ID using the scheme outlined at the beginning of this section, one will be left with a value network after finding optimal decision rules for all the decision nodes. The expected value of this network is the optimal expected value of the original ID.
Let $\mathcal{N}$ be a value network. If all value nodes are converted into random nodes via Cooper's transformation, then $\mathcal{N}$ becomes a BN. Denote the BN also by $\mathcal{N}$. The expected value of the value network is $\sum_{v \in V} P_{\mathcal{N}}(v=1) M_{v}$, where $V$ is the set of value nodes. For any value node $v$, let $\mathcal{N}_{v}$ be obtained from the BN $\mathcal{N}$ by pruning nodes outside $a n(\{v\})$. Then $P_{\mathcal{N}}(v=1)=P_{\mathcal{N}_{v}}(v=1)$. Thus, the expected value can be obtained using the following procedure.

Procedure $\exp \operatorname{Val}(\mathcal{N})$

1. For each $v \in V$, obtain $\mathcal{N}_{v}$ from $\mathcal{N}$ by pruning nodes outside $a n(\{v\})$. Compute $P_{\mathcal{N}_{v}}(v=1)$ by calling $\operatorname{BNinf}\left(v, \mathcal{N}_{v}\right)$.
2. Return $\sum_{v \in V} P_{\mathcal{N}_{v}}(v=1) M_{v}$.

Note that the following BN inference problems are solved:

$$
P_{\mathcal{N}_{v}}(v=1) \text { for each } v \in V
$$

### 4.4 An algorithm

The foregoing discussions lead to the following algorithm for evaluating IDs.

Procedure evalID $(\mathcal{N})$ :

1. While there are decision nodes in $\mathcal{N}$
(a) Find the tail decision node $d$.
(b) $\mathcal{T}=\operatorname{redTail}(\mathcal{N}, d)$.
(c) Call evalFun $(\mathcal{T}, d)$ to compute $e_{\mathcal{T}}\left(\pi_{d, r}, d\right)$ and $P_{\mathcal{T}_{r}}\left(\pi_{d, r}\right)$.
(d) Find an optimal decision rule for $d$ via

$$
\delta^{*}\left(\pi_{d, r}\right)=\arg \max _{d} e_{\mathcal{T}}\left(\pi_{d, r}, d\right)
$$

(e) $\mathcal{B}=\operatorname{augBody}\left(\mathcal{N}, d, e_{\mathcal{T}}\left(\pi_{d, r}, d\right)\right)$.
(f) If some nodes in $\pi_{d}$ have parents in the downstream set $X_{2}$ of $\mathcal{N}$ w.r.t $d$,

$$
\mathcal{B}=\operatorname{redBody}\left(\mathcal{B}, P_{\mathcal{T}_{r}}\left(\pi_{d, r}\right), \mathcal{T}\right)
$$

![img-2.jpeg](img-2.jpeg)

Figure 3: An ID.
(g) $\mathcal{N}=\mathcal{B}$.
(After the while-loop, $\mathcal{N}$ becomes a value network.)
2. Return the optimal decision rules and $\exp \operatorname{Val}(\mathcal{N})$.

The procedure evalID identifies a list BN inference problems and specifies how optimal decision rules can be obtained from the solutions of those problems. It leaves it to the user to choose an algorithm for solving the BN inference problems. As such, it is really an algorithm for reducing ID evaluation into BN inference problems.

## 5 An example

This section illustrates evalID by using the ID in Figure 3, which is borrowed from Jensen et al (1994). Arcs into decision nodes are dashed for readability.

Denote the ID by $\mathcal{N}$. Since it contains decision node, evalID enters the while-loop. In the while-loop, Step 1(a) finds that $d_{4}$ is the tail decision node and Step 1(b) constructs that reduced tail $\mathcal{T}=\operatorname{redTail}\left(\mathcal{N}, d_{4}\right)$. To get a clear picture of $\mathcal{T}$, note that the downstream set $X_{2}$ is $\left\{d_{4}, c_{11}, c_{12}, v_{4}\right\}$. Since no parents of $d_{2}$ have parents in $X_{2}, \pi_{d_{4}, 2}=\emptyset$. Among the parents of $d_{4}$, only $c_{10}$ and $d_{4}$ are parents to nodes in $\pi_{d_{4}, 2} \cup X_{2} \backslash\left\{d_{4}\right\}=X_{2} \backslash\left\{d_{4}\right\}$, hence $c_{10}$ and $d_{2}$ are the all the relevant parents of $d_{4}$. In other words, $\pi_{d_{4}, r}=\left\{c_{10}, d_{2}\right\}$. Consequently, $\mathcal{T}$ consists of nodes $c_{10}$, $d_{2}, d_{4}, c_{11}, c_{12}$, and $v_{4}$ and is as shown in Figure 4 (2), where $v_{4}$ have been converted into a random node by Cooper's transformation.
Step 1(c) calculates the evaluation functional $e_{\mathcal{T}}\left(\pi_{d_{4}, r}, d_{4}\right)$. In the process, the BNs $\mathcal{T}_{c}$ and $\mathcal{T}_{v_{4}}$ are obtained from $\mathcal{T}$ by pruning nodes outside $a n\left(\pi_{d_{4}, r}\right)$ and $a n\left(\pi_{d_{4}, r} \cup\left\{d_{4}, v_{4}\right\}\right)$ respectively. Since $a n\left(\pi_{d_{4}, r}\right)=\pi_{d_{4}, r}=\left\{c_{10}, d_{2}\right\}, \mathcal{T}_{c}$ consists of two nodes $c_{10}$ and $d_{2}$. They are isolated from each other and both have uniform distributions. Since $a n\left(\pi_{d_{4}, r} \cup\left\{v_{4}\right\}\right)$ contains all nodes in the tail, $\mathcal{T}_{v_{4}}$ is the same as $\mathcal{T}$. The

![img-3.jpeg](img-3.jpeg)

Figure 4: Reduced tail and augmented body w.r.t $d_{4}$.
subroutine BNinf is called to compute the following probabilities:

$$
P_{\mathcal{T}_{c}}\left(c_{10}, d_{2}\right), P_{\mathcal{T}_{v_{4}}}\left(v_{4}=1, c_{10}, d_{2}, d_{4}\right)
$$

Thereafter, the evaluation functional is obtained by

$$
e_{\mathcal{T}}\left(c_{10}, d_{2}, d_{4}\right)=\frac{P_{\mathcal{T}_{v_{4}}}\left(v_{4}=1, c_{10}, d_{2}, d_{4}\right) M_{v_{4}}}{P_{\mathcal{T}_{c}}\left(c_{10}, d_{2}\right) /\left|\Omega_{d_{4}}\right|}
$$

Step 1(d) finds an optimal decision rule for $d_{4}$ via $\delta_{4}^{*}\left(c_{10}, d_{2}\right)=\arg \max _{d_{4}} e_{\mathcal{T}}\left(c_{10}, d_{2}, d_{4}\right)$.
Step 1(e) calls augBody to construct the augmented body of $\mathcal{N}$ w.r.t $d_{4}$, which is shown in Figure 4 (1). The utility function of the new value node $u_{4}$ is given by $f_{u_{4}}\left(c_{10}, d_{2}\right)=\max _{d_{4}} e_{\mathcal{T}}\left(c_{10}, d_{2}, d_{4}\right)$. Since no nodes in $\pi_{d_{4}, r}$ have parents in $X_{2}$, Step 1(f) is skipped.
We stop here due to space limit. Interested readers are referred to a longer version of the paper for the remaining steps.

## 6 Comparisons with previous methods

Both evalID and the Shachter-Peot algorithm reduce ID evaluation into BN inference problems, which can be solved using arbitrary BN inference algorithms. This section shows that the probabilistic inference problems induced by evalID are easier to solve than those induced by the Shachter-Peot algorithm.
Among all previous algorithms, Shenoy's fusion algorithm (Shenoy 1992) and the algorithms by Ndilikilikesha (1994) and Jensen et al (1994) are the most efficient. Those three algorithms are basically equivalent in the sense that they all carry out essentially the same numerical computations. They are direct evaluation algorithms in the sense that they evaluate IDs directly without the reduction to BN inference problems. An method that reduces ID evaluation into BN inference problems would be unattractive if it is less efficient than those direct evaluation algorithms no matter what BN inference algorithm is used. We will show
that this is not the case for evalID by comparing it with Shenoy's fusion algorithm.

Non-numerical computations in evalID include the identification of tail decision nodes, the construction of reduced tails and bodies, and pruning of nodes in a reduced tail that are irrelevant to particular BN inference problems . They are negligible compared to numerical computations. We will hence focus the comparisons on numerical computations.

### 6.1 Comparisons with Shachter and Peot's algorithm

The Shachter-Peot algorithm applies only when there is one value node. Let $\mathcal{N}$ be an ID with one value node. Assume that there are no barren random nodes, i.e. random nodes that have no children ${ }^{3}$.

Let $\mathcal{N}^{\prime}$ be the BN defined in Section 2. In the Shachter-Peot algorithm, the BN inference problem $P_{\mathcal{N}^{\prime}}\left(\pi_{d}, d \mid v=1\right)$ needs to be solved in order to obtain an optimal decision rule for the tail decision node $d$. Let $\mathcal{T}$ be the reduced tail of $\mathcal{N}$ w.r.t $d$. In evalID, we need to solve two BN inference problems, namely $P_{\mathcal{T}}\left(\pi_{d, r}\right)$ and $P_{\mathcal{T}}\left(\pi_{d, r}, d, v=1\right)$.
The inference problem $P_{\mathcal{N}^{\prime}}\left(\pi_{d}, d \mid v=1\right)$ is more difficult to solve than $P_{\mathcal{T}}\left(\pi_{d, r}\right)$ and $P_{\mathcal{T}}\left(\pi_{d, r}, d, v=1\right)$ than for two reasons. First, it involves more variables. Due to the no-forgetting constraint, all other decision nodes and their parents must be parents of $d$, i.e. in $\pi_{d}$. However, as we have seen in the example of the previous section, many of the parents of $d$ are irrelevant to $d$. The set $\pi_{d, r}$ usually contains much less variables than $\pi_{d}$. Second, $\mathcal{N}^{\prime}$ usually consists of many more nodes than the reduced tail $\mathcal{T}$. Moreover, since $\mathcal{N}$ has no barren random nodes, no nodes in $\mathcal{N}^{\prime}$ can be pruned when computing $P_{\mathcal{N}^{\prime}}\left(\pi_{d}, d \mid v=1\right)$, while $\mathcal{T}$ can be further reduced to $\mathcal{T}_{c}$ when computing $P_{\mathcal{T}}\left(\pi_{d, r}\right)$ and $\mathcal{T}_{v}$ when computing $P_{\mathcal{T}}\left(\pi_{d, r}, d, v=1\right)$.
In evalID, nodes in the downstream set $X_{2}$ are pruned after an optimal decision rule for $d$ has been obtained. In other words, those nodes do no participate in the computations for other decision nodes. However, no nodes are pruned in the Shachter-Peot algorithm. Computations for each decision node involve all nodes in $\mathcal{N}$.

### 6.2 Comparisons with Shenoy's fusion algorithm

This subsection first introduces a variation of evalID, called evalID1, that performs essentially the same

[^0]
[^0]:    ${ }^{3}$ Barren random nodes, if exist, can be pruned at a preprocessing step (Shachter 1986).

numerical computations as Shenoy's fusion algorithm and then compares evalID with evalID1.

### 6.2.1 A variation of evalID

We will refer to non-negative functions of a set of variables simply as factors. Conditional probabilities and utility functions are all factors. Let $\rho$ be an ordering of the nodes in $X_{2} \backslash V_{2} \cup\{d\}$. In stead of evalFun, evalID1 uses the following procedure to compute the evaluation functional of the reduced tail $\mathcal{T}$ and the marginal probability $P_{\mathcal{T}}\left(\pi_{d, r}\right)$.

Procedure evalFun1 $(\mathcal{T}, d)$

1. Let $\mathcal{F}$ be the list of utility functions of value nodes in $V_{2}$ and let $\mathcal{P}$ be the list of conditional probabilities of nodes in $X_{2} \backslash V_{2} \cup\{d\}$.
2. While $\rho \neq \emptyset$, remove the first node $x$ from $\rho$ and call fuse $(\mathcal{P}, \mathcal{F}, x)$.
3. Multiply all factor in $\mathcal{P}$ (the product is $P_{\mathcal{T}}\left(\pi_{d, r}, d\right)$.)
4. Sum all factors in $\mathcal{F}$ (the result is $e_{T}\left(\pi_{d, r}, d\right)$ ).
5. Return $e_{T}\left(\pi_{d, r}, d\right)$ and $\sum_{d} P_{\mathcal{T}}\left(\pi_{d, r}, d\right)$.

The subroutine fuse is given as follows:
Procedure fuse $(\mathcal{P}, \mathcal{F}, x)$

1. Remove from $\mathcal{P}$ all the factors $p_{1}, \ldots$, $p_{k}$ that involve $x$. If such factors exist, add the new factor $p=\sum_{x} \prod_{i=1}^{k} p_{i}$ to $\mathcal{P}$.
2. Remove from $\mathcal{F}$ all the factors $f_{1}, \ldots, f_{l}$ that involve $x$. If such factors exist, add the new factor $\sum_{x}\left[\sum_{i=1}^{l} f_{i}\right]\left[\prod_{i=1}^{k} p_{i}\right] / p$ to $\mathcal{F}$.

Let $\mathcal{N}$ be a value network and $\rho$ be an ordering of the random nodes. Instead of expVal, evalID1 uses the following procedure to compute the expected value of $\mathcal{N}$.

Procedure expVal1 $(\mathcal{N})$ :

1. Let $\mathcal{F}$ be the list of utility functions of value nodes in $\mathcal{N}$ and let $\mathcal{P}$ be the list of conditional probabilities of random nodes in $\mathcal{N}$.
2. While $\rho \neq \emptyset$, remove the first node $x$ from $\rho$ and call fuse $(\mathcal{P}, \mathcal{F}, x)$.
3. Return the sum all factors in $\mathcal{F}$ (which is the expected value of $\mathcal{N}$ ).

Shenoy's fusion algorithm requires an ordering, say $\rho_{s}$, of all the random and decision nodes. If the orderings in evalFun1 and expVal1 conforms to $\rho_{s}$ in the sense that relative orders of nodes are the same, than evalID1 carries out essentially the same numerical computations as Shenoy's fusion algorithm (see Shenoy 1992).

### 6.2.2 Comparisons

We now set out to compare evalID1 and evalID. Suppose evalID employs the VE (variable elimination) algorithm ${ }^{4}$ for probabilistic inference. Let $A$ be a subset of nodes in a BN $\mathcal{M}$ and let $\rho$ be an ordering of nodes outside $A$. VE computes the marginal probability $P_{\mathcal{M}}(A)$ as follows:

Procedure BNinf-VE $(\mathcal{M}, A)$ :

1. Let $\mathcal{P}$ be the list of conditional probabilities in $\mathcal{M}$.
2. While $\rho \neq \emptyset$, remove the first node $x$ from $\rho$ and remove from $\mathcal{P}$ all the factors $f_{1}, \ldots, f_{k}$ that involve $x$. If such factors exist, add the new factor $\sum_{x} \prod_{i=1}^{k} f_{i}$ to the list $\mathcal{P}$.
3. Multiply all factors in $\mathcal{P}$ and return the result (which is $P_{\mathcal{M}}(A)$ ).

Consider computing $P_{\mathcal{T}_{c}}\left(\pi_{d, r}\right)$ and $P_{\mathcal{T}_{v}}\left(\pi_{d, r}, d, v=1\right)$ using BNinf-VE. If the ordering in BNinf-VE conforms to the ordering in evalFun1, BNinf performs no more numerical computations than evalFun1 $(\mathcal{T}, d)$. Therefore, the amount of numerical computations carried out by evalFun $(\mathcal{T}, d)$ is at most $1+m$ times that carried by evalFun1 $(\mathcal{T}, d)$, where $m$ is the number of value nodes in $\mathcal{T}$. Similarly, for any value network $\mathcal{N}$, the amount of numerical computations carried out by $\operatorname{expVal}(\mathcal{N})$ is at most $m$ times that carried by $\operatorname{expVal1}(\mathcal{N})$, where $m$ is the number of value nodes in $\mathcal{N}$.

We argue that evalFun $(\mathcal{T}, d)$ is usually more efficient that evalFun1 $(\mathcal{T}, d)$, especially when $\mathcal{T}$ is large. Define the size of a factor to be the number of variables involved in the factor. It is well understood in the BN literature that the complexities of BNinf and evalFun1 is largely determined by the sizes of the largest factors encountered; they are exponential in the largest factors sizes. The BNs $\mathcal{T}_{c}$ and each $\mathcal{T}_{v}$ are subnetworks of $\mathcal{T}$. When $\mathcal{T}$ is large, the differences between $\mathcal{T}$ and $\mathcal{T}_{c}$ or $\mathcal{T}_{v}$ are usually also large. In

[^0]
[^0]:    ${ }^{4}$ The idea behind VE is implicit in many papers (e.g. Shenoy 1992). It was first made explicit in Zhang and Poole (1994) and extended to exploit independence of causal influence by Zhang and Poole (1996).

such a case, the maximum factor sizes encountered by BNinf are smaller than those encountered by evalFun1 and hence the amount of time BNinf-VE spends in computing $P_{\mathcal{T}_{v}}\left(\pi_{d, r}\right)$ or $P_{\mathcal{T}_{u}}\left(\pi_{d, r}, d, v=1\right)$ is much less than that evalFun1 $(\mathcal{T}, d)$ takes. Consequently, evalFun $(\mathcal{T}, d)$ takes less time than evalFun1 $(\mathcal{T}, d)$.
A second reason for evalFun $(\mathcal{T}, d)$ being more efficient than evalFun1 $(\mathcal{T}, d)$ is the fact that the former does not perform numerical divisions until the last step, while the latter might divide factors when fusing each node.

Similarly, expVal is usually more efficient than expVal. Hence evalID is usually more efficient than evalID1 and therefore more efficient than Shenoy's fusion algorithm.

We would like to emphasize that arbitrary BN inference algorithms can be used in evalID, while this is not the case in Shenoy's fusion algorithm and all the direct evaluation algorithms for that matter. This is a big advantage (see discussions in the next section).

## 7 Conclusions

This paper is about reducing ID evaluation into BN inference problems. Such an exercise is interesting because it allows the use of arbitrary BN inference algorithms in evaluating IDs. Two reduction methods have been proposed previously (Cooper 1988 and Shachter and Peot 1994). A new method is presented in this paper. The BN inference problems induced by the new method are easier to solve than those induced by earlier methods.

When coupled with the VE algorithm, the performance of the new method is, in the worst case, within a small constant factor of that of the most efficient previous algorithms, which evaluate ID directly without the reduction into BN inference problems. We have argued that the combination of the new method and VE is usually more efficient in large IDs.
The fact that it allows arbitrary BN inference algorithms is big advantage of the new method. From a system development point of view, the method enables one to easily add ID evaluation capabilities to any BN inference packages. From the efficiency point of view, speeding up inference in BNs has been and still is an active research area. There are algorithms that exploit independence of causal influence (e.g. Zhang and Poole 1996) and that exploit special structures in the conditional probability tables. The new method facilitates ready incorporation of those algorithms, as well as future advances in BN inference, in ID evaluation. We are not aware of any approximate algorithms for IDs, while there is a rich collection of approximate and
simulation algorithms for BNs. The new method also opens up the possibility of approximate algorithms for ID, which might be necessary in order to solve large decision problems.
