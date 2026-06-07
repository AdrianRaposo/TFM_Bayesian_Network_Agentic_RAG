# On the Bias of Directed Information Estimators 

Gabriel Schamberg, Student Member, IEEE, Todd P. Coleman, Senior Member, IEEE


#### Abstract

When estimating the directed information between two jointly stationary Markov processes, it is typically assumed that the recipient of the directed information is itself Markov of the same order as the joint process. While this assumption is often made explicit in the presentation of such estimators, a characterization of when we can expect the assumption to hold is lacking. Using the concept of d-separation from Bayesian networks, we present sufficient conditions for which this assumption holds. We further show that the set of parameters for which the condition is not also necessary has Lebesgue measure zero. Given the strictness of these conditions, we introduce a notion of partial directed information, which can be used to bound the bias of directed information estimates when the directed information recipient is not itself Markov. Lastly we estimate this bound on simulations in a variety of settings to assess the extent to which the bias should be cause for concern.


Index Terms—Directed Information, Estimation, Bias Quantification, Markov

## I. INTRODUCTION

The directed information (DI) is a popular measure of asymmetric relationships between two stochastic processes. Since its origination in 1973 [1] and its reemergence in 1990 [2], the DI has been increasingly pervasive throughout science and engineering disciplines. When using the DI to study the inter-process relationships exhibited by real data, i.e. when the true underlying joint statistics are unknown, it is necessary to utilize DI estimation techniques. DI estimators have been studied extensively in the literature using a variety of approaches, including sequential estimation using universal probability assignments [3], maximum likelihood estimation of generalized linear models for DI between point processes [4], $k$-NN estimation [5], and plug-in estimation [6]. With a couple exceptions, when estimating the DI from $Y$ to $X$, these estimators assume that (i) $X$ and $Y$ are jointly stationary ergodic Markov processes and (ii) $X$ is itself a jointly stationary ergodic Markov process of the same order. While [3] includes theoretical results for the non-Markov setting, only the context tree weighting (CTW) based estimators (which assume (i) and (ii)) are implemented due to the computational complexity of universal probability assignments for general finite-alphabet stationary ergodic sequences. In [6] it is noted that when assumption (ii) does not hold, the quantity being estimated is in fact not the DI, but rather an upper bound for the DI. Despite the common adoption of assumptions (i) and (ii), the conditions under which they hold and the implications when they do not are not well studied. Our present work seeks to fill this gap in order to ensure that the estimation of DI across scientific disciplines can be conducted in a manner such that the results are reliable.

Relevant discussions regarding the issues surrounding assumption (ii) have been held in the literature on Granger
causality (GC) [7]. GC can be viewed as a special case of DI where the processes in question obey a vector autoregressive (VAR) model with Gaussian noise. It is noted in the GC literature that subsets of finite-order VAR processes are in general infinite order autoregressive processes [8]. Thus, estimating a "restricted" model (i.e. one where the candidate influencer is hidden) from data requires estimating a truncated model and induces a bias-variance trade-off. For the linear Gaussian case, this issue can be avoided by computing the restricted model directly from the full model using the Yule-Walker equations [9]. Unfortunately, there is no clear extension of this approach for arbitrary Markov processes, and other techniques are required.

We here employ a Bayesian network perspective to identify when the independence statements required by DI estimators hold. In particular, by representing a collection of interacting processes as a Bayesian network, we can use the d-separation criterion to identify conditional independencies in relevant subsets of the network. Using this perspective, we provide sufficient conditions under which assumptions (i) and (ii) are satisfied and show that these conditions are also necessary with the exception of a set of parameters with Lebesgue measure zero. We further present a bound for the estimation bias that can be estimated reliably without requiring assumption (ii). Finally, to understand the magnitude of the biases in question, we compute the proposed bound for simulated processes in a variety of problem settings.

## II. Preliminaries

## A. Notation

We will be considering collections of jointly stationary discrete processes $X, Y$, and $Z$, where, at any time $i, X_{i} \in \mathcal{X}$, $Y_{i} \in \mathcal{Y}$, and $Z_{i} \in \mathcal{Z}$. Without loss of generality, $Z$ may represent a collection of processes $\left(Z^{(1)}, \ldots, Z^{(m)}\right) \in \mathcal{Z}_{1} \times$ $\cdots \times \mathcal{Z}_{m} \triangleq \mathcal{Z}$. Collections of samples are indicated with superscripts as $X_{i}^{i+k} \triangleq\left\{X_{i}, \ldots, X_{i+k}\right\}$ and $X^{n} \triangleq X_{1}^{n}$. In general, capital letters will represent random entities and lower case letters will represent their realizations. When a process is Markov of order $d$ we will refer to it as $d$-Markov, unless $d=1$, in which case we will simply refer to it as Markov. We will use $p$ to represent probability distributions, with the specific distribution being made clear from context.

## B. Directed Information

Consider a collection of processes $(X, Y, Z)$. Define the causally conditional DI from $Y$ to $X$ given $Z$ as:

$$
I\left(Y^{n} \rightarrow X^{n} \| Z^{n}\right)=\sum_{i=1}^{n} I\left(X_{i} ; Y^{i} \mid X^{i-1}, Z^{i}\right)
$$

and the associated causally conditional DI rate (when it exists) as:

$$
\bar{I}(Y \rightarrow X \| Z)=\lim _{n \rightarrow \infty} \frac{1}{n} I\left(Y^{n} \rightarrow X^{n} \| Z^{n}\right)
$$

In the context of a collection of processes, the aforementioned assumptions are: (i) $(X, Y, Z)$ are jointly $d$-Markov, i.e. the second entropy term in (2) can be simplified to $H\left(X_{i} \mid X_{i-d}^{i-1}, Y_{i-d}^{i}, Z_{i-d}^{i}\right)$ and (ii) $X$ is "conditionally $d$ Markov given $Z$ ", i.e. the first entropy term can be simplified as $H\left(X_{i} \mid X_{i-d}^{i-1}, Z_{i-d}^{i}\right)$. Once these assumptions are made, it is clear that the DI can be estimated from data by splitting a stream $\left(X^{n}, Y^{n}, Z^{n}\right)$ into a collection of samples $\left\{\left(X_{i-d}^{i}, Y_{i-d}^{i}, Z_{i-d}^{i}\right)\right\}_{i= d}^{n}$ and estimating the appropriate distributions using the methods of [3]-[6]. The goal of this work is to understand when we can expect both of these assumptions to hold, and to understand what the consequences are of assuming they both hold when in fact only the first holds. It should be noted that while we only consider networks of processes and the causally conditional DI as above, all of the results hold when $Z=\emptyset$, in which case the standard DI is recovered and the assumptions above revert to the assumptions discussed in the introduction.

## C. Bayesian Networks

To understand the conditions under which the desired independence relationships hold, we can use Bayesian networks, which represent conditional independencies in collections of random variables using a directed acyclic graph (DAG) $G=$ $(V, E)$, where $V=\left\{V^{(1)}, \ldots, V^{(m)}\right\}$ is a set of random variables (equivalently nodes or vertices) and $E \subset V \times V$ is a set of directed edges that does not contain any cycles [10]. The parent set of a node $V^{(i)}$ in a DAG is defined as the set of nodes with arrows going into $V^{(i)}, \mathcal{P}_{V^{(i)}} \triangleq\left\{V^{(j)}:\left(V^{(j)} \rightarrow\right.\right.$ $\left.V^{(i)}\right) \in E\}$. The defining characteristic of a Bayesian network representation of a joint distribution over the nodes $V \sim p$ is the ability to factorize the distribution as:

$$
p(V)=\prod_{i=1}^{m} p\left(V_{i} \mid \mathcal{P}_{V^{(i)}}\right)
$$

If this factorization holds for a given $p$ and $G$, we say $G$ is a Bayesian network for $p$. A key concept when working with Bayesian networks is the d-separation criterion, which is used to identify subsets of nodes whose conditional independence is implied by the graphical structure. In particular, when given three disjoint subsets of nodes $A, B, C \subset V$ in a graph $G$, a straightforward algorithm (shown in Algorithm 1) can be used to determine if $C$ d-separates $A$ and $B$. When $C$ d-separates $A$ and $B$, then for any joint distribution $p(V)$ such that $G$ is a Bayesian network for $p, A$ and $B$ will be conditionally independent given $C$. While the converse is not true in general (i.e. independence does not imply d-separation), it has been shown that for specific classes of Bayesian networks, the set of parameters for which the converse does not hold has

Lebesgue measure zero [10], [11]. When a graph $G$ and joint distribution $p$ are such that d-separation holds if and only if conditional independence holds for all subsets of nodes, then the distribution $p$ is called "faithful" to $G[10]$.

## Algorithm 1 d-Separation [12]

Input: DAG $G=(V, E)$ and disjoint sets $A, B, C \subset V$
1: Create a subgraph containing only nodes in $A, B$, or $C$ or with a directed path to $A, B$, or $C$
2: Connect with an undirected edge any two variables that share a common child
3: For each $c \in C$, remove $c$ and any edge connected to $c$
4: Make every edge an undirected edge
5: Conclude that $A$ and $B$ are d-separated by $C$ if and only if there is no path connecting $A$ and $B$

## III. Characterization of Processes with CONDITIONAL MARKOVICITY

## A. Network Representation of Markov Processes

A Bayesian network is a very natural representation for collections of Markov processes. In particular, using the chain rule to factorize the joint distribution over $n$ time steps of the processes $(X, Y, Z)$ yields:

$$
p\left(X^{n}, Y^{n}, Z^{n}\right)=\prod_{i=1}^{n} p\left(X_{i}, Y_{i}, Z_{i} \mid X_{i-d}^{i-1}, Y_{i-d}^{i-1}, Z_{i-d}^{i-1}\right)
$$

We next make the additional assumption (A1) that $X_{i}, Y_{i}$, and $Z_{i}$ are pairwise conditionally independent given the past $\left\{X_{i-d}^{i-1}, Y_{i-d}^{i-1}, Z_{i-d}^{i-1}\right\}$. This assumption facilitates construction of a Bayesian network, as we can rely on the arrow of time to determine the direction of arrows in the network. In the absence of (A1), we cannot construct a unique Bayesian network representation of Markov processes without making alternative assumptions. This is similar reasoning to that of [13], where (A1) is used for establishing the equivalence between DI graphs and minimal generative model graphs. Under (A1), we can further simplify (5) as:

$$
p\left(X^{n}, Y^{n}, Z^{n}\right)=\prod_{i=1}^{n} \prod_{S \in\left\{X_{i}, Y_{i}, Z_{i}\right\}} p\left(S \mid X_{i-d}^{i-1}, Y_{i-d}^{i-1}, Z_{i-d}^{i-1}\right)
$$

Comparing (4) and (6), it is clear that we can represent a collection of processes as a Bayesian network by letting each node be a single time point of a process (i.e. $X_{i}, Y_{i}$, or $Z_{i}$ ) with parents $\mathcal{P}_{X_{i}}, \mathcal{P}_{Y_{i}}, \mathcal{P}_{Z_{i}} \subseteq\left\{X_{i-d}^{i-1}, Y_{i-d}^{i-1}, Z_{i-d}^{i-1}\right\}$. In general, there may be multiple valid Bayesian networks for a particular distribution. In this case, we note that $X_{i}, Y_{i}$, and $Z_{i}$ may not all depend on the entire set $\left\{X_{i-d}^{i-1}, Y_{i-d}^{i-1}, Z_{i-d}^{i-1}\right\}$. Thus, we construct a unique Bayesian network for $(X, Y, Z)$ by including an edge $S_{i-k} \rightarrow S_{i}^{\prime}$ for $S, S^{\prime} \in\{X, Y, Z\}$ and $k=1, \ldots, d$ if and only if:

$$
I\left(S_{i-k} ; S_{i}^{\prime} \mid\left\{X_{i-d}^{i-1}, Y_{i-d}^{i-1}, Z_{i-d}^{i-1}\right\} \backslash S_{i-k}\right)>0
$$

### V-B Necessary and Sufficient Conditions for d-Separation

Using the Bayesian network construction given by (7), we can leverage the d-separation criterion to gain a better understanding of the types of conditions which give rise to the conditional independence relationships needed for DI estimation. To start, we identify necessary and sufficient conditions for which $X_{i}$ will be d-separated from $\left(X^{i-l-1},Z^{i-l-1}\right)$ by $\left(X_{i-l}^{i-1},Z_{i-l}^{i-1}\right)$. In other words, the following theorem gives us a characterization of processes that are guaranteed to have the conditional independence relationships typically assumed by DI estimators:

Theorem 1. Let $(X, Y, Z)$ be a collection of jointly stationary $d$-Markov processes satisfying (A1). If $I\left(Y^{n} \rightarrow X^{n} \| Z^{n}\right)=$ 0 , then $X$ is conditionally $d$-Markov given $Z$. If $I\left(Y^{n} \rightarrow\right.$ $\left.X^{n} \| Z^{n}\right)>0, X$ is conditionally Markov given $Z$ of order $2 d$ or less if:

$$
I\left(Y_{j} ; Y_{k} \mid X^{i}, Z^{i}\right)=0 \forall j<k \leq i
$$

If $I\left(Y^{n} \rightarrow X^{n} \| Z^{n}\right)>0$ but (8) is not satisfied, there will not exist any positive integer $l$ such that $\left(X_{i-l}^{i-1}, Z_{i-l}^{i-1}\right) d$ separates $X_{i}$ from $\left(X^{i-l-1}, Z^{i-l-1}\right)$ in the Bayesian network generated according to (7).

Proof. The first statement of the theorem follows trivially from the removal of $Y_{i-d}^{i-1}$ from $p\left(X_{i} \mid X_{i-d}^{i-1}, Y_{i-d}^{i-1}, Z_{i-d}^{i-1}\right)$. Now assume that (8) holds. Note that:

$$
\begin{aligned}
& p\left(X_{i} \mid X^{i-1}, Z^{i-1}\right) \\
& =\sum_{\substack{y_{i-d}^{i-1} \\
y_{i-d}^{i-1}}} p\left(X_{i} \mid X^{i-1}, y_{i-d}^{i-1}, Z^{i-1}\right) \prod_{j=i-d}^{i-1} p\left(y_{j} \mid X^{i-1}, Z^{i-1}\right) \\
& =\sum_{\substack{y_{i-d}^{i-1} \\
y_{i-d}^{i-1}}} p\left(X_{i} \mid X_{i-d}^{i-1}, y_{i-d}^{i-1}, Z_{i-d}^{i-1}\right) \prod_{j=i-d}^{i-1} p\left(y_{j} \mid X_{j-d}^{i-1}, Z_{j-d}^{i-1}\right) \\
& =\sum_{\substack{y_{i-d}^{i-1} \\
y_{i-d}^{i-1}}} p\left(X_{i} \mid X_{i-2 d}^{i-1}, y_{i-d}^{i-1}, Z_{i-2 d}^{i-1}\right) \prod_{j=i-d}^{i-1} p\left(y_{j} \mid X_{i-2 d}^{i-1}, Z_{i-2 d}^{i-1}\right) \\
& =p\left(X_{i} \mid X_{i-2 d}^{i-1}, Z_{i-2 d}^{i-1}\right)
\end{aligned}
$$

where (9) follows from the chain rule and the conditional independence of $y_{i-d}^{i-1}$ given $\left(X^{i-1}, Z^{i-1}\right)$, (10) follows from the joint Markovicity of $X$ and $Y$ and the conditional independence of $y_{i-d}^{i-1}$, and (11) follows from the conditional independence of the past and the future given the present for Markov processes. Thus it follows that $X$ is conditionally Markov given $Z$ of order at most $2 d$.

Now assume $I\left(Y^{n} \rightarrow X^{n} \| Z^{n}\right)>0$ but (8) does not hold. Then we will show there is no positive integer $l$ such that $\left(X_{i-l}^{i-1}, Z_{i-l}^{i-1}\right)$ d-separates $\left(X^{i-l-1}, Z^{i-l-1}\right)$ from $X_{i}$. To do this, we first note that $\left(X^{i}, Z^{i}\right)$ does not d-separate $Y_{j}$ and $Y_{k}$, because if it did, they would be conditionally independent. As such, when performing the d-separation algorithm given by

Algorithm 1, $Y_{j}$ and $Y_{k}$ will be connected by an undirected edge after completing step 4. Furthermore, if we let $\tau_{1}=k-j$, then by the joint stationarity of $(X, Y, Z)$, every $Y_{i}$ will be connected to $Y_{i-\tau_{1}}$ at the end of step 4. Furthermore, we know that $I\left(Y^{n} \rightarrow X^{n} \| Z^{n}\right)>0$ implies that for some $q \leq m$, there is a directed edge from $Y_{q}$ to $X_{m}$. Letting $\tau_{2}=m-q$, we know from the joint stationarity of $(X, Y, Z)$ that for every $X_{i}$, there is an incoming directed edge from $Y_{i-\tau_{2}}$. As such, at the end of step 4, every $X_{i}$ will be part of an undirected path connecting $Y_{i-\tau_{2}}, Y_{i-\tau_{2}-\tau_{1}}, Y_{i-\tau_{2}-2 \tau_{1}}, \ldots$ Thus, for any $l \geq 1$ this path can be followed $r$ steps such that $r \tau_{1}>d$. Then we know that $Y_{i-\tau_{2}-r \tau_{1}}$ is connected via an undirected edge to $X_{i-\tau_{2}-r \tau_{1}+\tau_{2}}=X_{i-r \tau_{1}}$. Recalling that in step 3 of the d-separation algorithm, $\left(X_{i-l}^{i-1}, Z_{i-l}^{i-1}\right)$ have been removed from the graph, we note that since $i-r \tau_{1}<i-l, X_{i-r \tau_{1}}$ is in the graph. Thus, there is an undirected path connecting $X_{r \tau_{1}} \in X^{i-l-1}$ and $X_{i}$, which implies that $\left(X_{i-l}^{i-1}, Z_{i-l}^{i-1}\right)$ does not d-separate $\left(X^{i-l-1}, Z^{i-l-1}\right)$ and $X_{i}$ for any $l$.

We can see that the conditions presented by Theorem 1 are rather restrictive. With regard to the processes for which we cannot guarantee the desired conditional independence relations (i.e. those not satisfying (8)), the only distributions for which the assumptions in question hold are those that are unfaithful to their graphs. While there is ample discussion in the literature noting that these distributions are typically not seen in practice (see [10] and citations therein), a formal characterization within the present context is desired.

## C. Completeness of d-Separation

For a DAG $G=(V, E)$, define $\Gamma_{G} \subset \mathbb{R}^{M}$ to represent the set of $M$ parameters needed to specify all discrete distributions $p(V)$ such that the $G$ is a Bayesian network for $p$. Further define $\Gamma_{G}^{n} \subset \Gamma_{G}$ to be the subset of those distributions that are unfaithful to $G$. Then, it was shown in [11] the $\Gamma_{G}^{n}$ has Lebesgue measure zero with respect to $\mathbb{R}^{M}$. Unfortunately, this result cannot be directly applied to our problem. Let $\Theta_{G} \subset \mathbb{R}^{N}$ represent the set of parameters defining discrete jointly stationary $d$-Markov processes satisfying (A1) for which $G$ gives the Bayesian network constructed according (7). Defining the probabilities $\theta_{x, y, z}^{s_{i}} \triangleq p\left(s_{i} \mid x_{i-d}^{i-1}, y_{i-d}^{i-1}, z_{i-d}^{i-1}\right)$ for $s \in\{x, y, z\}$, we can see that $N \triangleq(|\mathcal{X}|+|\mathcal{Y}|+|\mathcal{Z}|-$ $3)|\mathcal{X}|^{d}|\mathcal{Y}|^{d}|\mathcal{Z}|^{d}$ many of these parameters uniquely define such a process. For a particular process, the collection of all these parameters is given by $\theta \in \Theta_{G} \subset \mathbb{R}^{N}$. Next define $\Theta_{G}^{n} \subset \Theta_{G}$ to be the subset of parameterizations such that the distribution $p$ induced by $\theta \in \Theta_{G}^{n}$ is unfaithful to $G$. It is clear that, due to the stationarity constraint, $N<<M$, and the Lebesgue measure of $\Gamma_{G}^{n}$ with respect to $\mathbb{R}^{M}$ does not tell us what the Lebesgue measure of $\Theta_{G}^{n}$ is with respect to $\mathbb{R}^{N}$. We seek to know when we can expect $X$ to be conditionally $d$-Markov given $Z$ despite the conditional independence not being implied by d-separation, i.e. when $p\left(X^{n}, Y^{n}, Z^{n}\right)$ is unfaithful. Using a similar technique to [11], the following theorem states that, when $d=1$, the set of such parameters has Lebesgue measure zero:

Theorem 2. The set of parameters defining a collection $(X, Y, Z)$ of jointly stationary irreducible aperiodic Markov processes such that there exists a positive integer $l$ where $X$ is conditionally $l$-Markov given $Z$ but $\left(X_{i-l}^{i-1}, Z_{i-l}^{i-1}\right)$ does not d-separate $X_{i}$ from $\left(X^{i-l-1}, Z^{i-l-1}\right)$ in the Bayesian network constructed by (7) has Lebesgue measure zero with respect to $\mathbb{R}^{N}$.

Proof. We will show that the statement holds for a fixed $l$, noting that a countably infinite union of measure zero sets has measure zero. First note that, if $X$ is conditionally $l$-Markov given $Z$, then for any $x_{i-l-1}^{i-1} \in \mathcal{X}^{l}, x_{i-l-1}^{l} \in \mathcal{X}, z_{i-l-1}^{i-1} \in$ $\mathcal{Z}^{l}, z_{i-l-1}^{i} \in \mathcal{Z}$, the following equality must hold:

$$
p\left(x_{i} \mid x_{i-l-1}^{i-1}, z_{i-l-1}^{i-1}\right)=p\left(x_{i} \mid \tilde{x}_{i-l-1}^{i-1}, \tilde{z}_{i-l-1}^{i-1}\right)
$$

where we define $\tilde{x}_{i-l-1}^{i-1} \triangleq\left\{x_{i-l}^{i-1}, x_{i-l-1}^{i}\right\}$ and $\tilde{z}_{i-l-1}^{i-1} \triangleq$ $\left\{z_{i-l}^{i-1}, z_{i-l-1}^{i}\right\}$. We will demonstrate that the equation given by (12) amounts to solving a polynomial function of the parameters $\theta$. It is shown in [14] that the set of solutions to a non-trivial polynomial (i.e. one that is not solved by all of $\mathbb{R}^{N}$ ) will have Lebesgue measure zero with respect to $\mathbb{R}^{N}$. Focusing on the left side of (12), we see that:

$$
\begin{aligned}
& p\left(x_{i} \mid x_{i-l-1}^{i-1}, z_{i-l-1}^{i-1}\right)=\sum_{y_{i-l-1}^{i-1}} \theta_{x, y, z}^{x_{i}} p\left(y_{i-l-1}^{i-1} \mid x_{i-l-1}^{i-1}, z_{i-l-1}^{i-1}\right) \\
& =\sum_{y_{i-l-1}^{i-1}} \theta_{x, y, z}^{x_{i}} \frac{p\left(x_{i-l-1}^{i-1}, y_{i-l-1}^{i-1}, z_{i-l-1}^{i-1}\right)}{p\left(x_{i-l-1}^{i-1}, z_{i-l-1}^{i-1}\right)} \\
& =\frac{\sum_{y_{i-l-1}^{i-1}} \theta_{x, y, z}^{x_{i}} \pi\left(x_{i-l-1}, y_{i-l-1}, z_{i-l-1}\right) \prod_{j=1}^{l} \theta_{x, \tilde{y}, z}^{(x, y, z)_{i-j}}}{\sum_{\tilde{y}_{i-l-1}^{i-1}} \pi\left(x_{i-l-1}, \tilde{y}_{i-l-1}, z_{i-l-1}\right) \prod_{j=1}^{l} \theta_{x, \tilde{y}, z}^{(x, \tilde{y}, z)_{i-j}}}
\end{aligned}
$$

where $\pi: \mathcal{X} \times \mathcal{Y} \times \mathcal{Z} \rightarrow[0,1]$ is the invariant distribution and $\theta_{x, y, z}^{(x, y, z)} \triangleq \theta_{x, y, z}^{x_{i}} \theta_{x, y, z}^{y_{i}} \theta_{x, y, z}^{z_{i}}$. Next, define a matrix $A \in$ $\mathbb{R}^{|\mathcal{X}||\mathcal{Y}||\mathcal{Z}| \times|\mathcal{X}||\mathcal{Y}||\mathcal{Z}|}$ containing the transition probabilities, i.e. $A_{j, k}=\theta_{R_{j}}^{R_{k}}$ some enumeration $R$ over the $|\mathcal{X}||\mathcal{Y}||\mathcal{Z}|$ possible values taken by $(X, Y, Z)$. Then we can represent $\pi$ in vector form $\vec{\pi} \in[0,1]^{|\mathcal{X}||\mathcal{Y}||\mathcal{Z}|}$ as a solution to $\vec{\pi}=\vec{\pi} A$. Given $\left(A^{T}-I\right) \vec{\pi}=0$, it is straightforward to show that each element of $\vec{\pi}_{j}$ (and thus each value of $\pi(x, y, z)$ ) can be written as fractions of polynomial functions of the entries of $A$, each of which is one of the parameters in $\theta$. As such, (13) can be written using fractions of polynomial functions of $\theta$. Repeating this process, we can see that the same applies to the RHS of (12). Thus, we can represent (12) as a polynomial function of $\theta$ by recursively multiplying both sides by any term that appears in the denominator on either side. Finally, we note that the polynomial given by (12) is trivial only if every process is a solution. Though omitted here for brevity, it can be show that the polynomial is non-trivial by constructing a counterexample.

It should be noted that the challenge for situations where $d>1$ arises in the representation of the invariant distribution as the solution to a matrix vector multiplication, and thus other proof techniques may be required.

## IV. QUANTIFYING ESTIMATION BIAS

We have shown that DI estimators are reliant upon a condition that is unlikely to be satisfied. Thus, we now define two augmented notions of DI that do not require $X$ to be conditionally Markov in order to be accurately estimated.

Definition 1. The $k^{\text {th }}$-order causally conditional truncated directed information (TDI) from $Y$ to $X$ given $Z$ is defined as:

$$
I_{T}^{(k)}\left(Y^{n} \rightarrow X^{n} \| Z^{n}\right) \triangleq \sum_{i=1}^{n} I\left(X_{i} ; Y_{i-k}^{i} \mid X_{i-k}^{i-1}, Z_{i-k}^{i}\right)
$$

The TDI in its unconditional form is discussed in [6] in the context of plug-in estimators of DI. Should both Markovicity and conditional Markovicity hold for a collection of processes, then the TDI and the DI are equivalent. However, having shown that conditional Markovicity is unlikely to hold, we here name the TDI to emphasize that it is a fundamentally different measure from the traditional DI.

Definition 2. The $k^{\text {th }}$-order causally conditional partial directed information (PDI) from $Y$ to $X$ given $Z$ is defined as:

$$
I_{P}^{(k)}\left(Y^{n} \rightarrow X^{n} \| Z^{n}\right) \triangleq \sum_{i=1}^{n} I\left(X_{i} ; Y_{i-k}^{i} \mid X^{i-1}, Y^{i-k-1}, Z^{i}\right)
$$

The PDI can be thought of as measuring the unique influence of the $k$ most recent samples of $Y$ on $X$. It is important to note that, under the assumption that $(X, Y, Z)$ are jointly $d$ Markov, we have that:

$$
\begin{aligned}
& I\left(X_{i} ; Y_{i-k}^{i} \mid X^{i-1}, Y^{i-k-1}, Z^{i}\right)= \\
& H\left(X_{i} \mid X_{i-k-d}^{i-1}, Y_{i-k-d}^{i-k-1}, Z_{i-k-d}^{i}\right)-H\left(X_{i} \mid X_{i-d}^{i-1}, Y_{i-d}^{i}, Z_{i-d}^{i}\right)
\end{aligned}
$$

Thus, it is clear that estimators of DI can be extended to estimate the PDI without the additional requirement of conditional Markovicity, though the details of these estimators are postponed for future work. Defining the TDI and PDI rates $\bar{I}_{T}^{(k)}$ and $\bar{I}_{P}^{(k)}$ to be the normalized limits analogous with the DI rate given by (3), we are able to bound the DI rate from above and below as follows:

Theorem 3. Let $(X, Y, Z)$ be jointly stationary d-Markov. For $k_{1} \geq 1$ and $k_{2} \geq d$, the causally conditional PDI and TDI rates bound the DI rate as:

$$
\bar{I}_{P}^{\left(k_{1}\right)}(Y \rightarrow X \| Z) \leq \bar{I}(Y \rightarrow X \| Z) \leq \bar{I}_{T}^{\left(k_{2}\right)}(Y \rightarrow X \| Z)
$$

with both bounds becoming equalities as $k_{1}, k_{2} \rightarrow \infty$.
Proof. Note that for any $k_{1} \geq 1$ and $k_{2} \geq d$ :

$$
\begin{aligned}
& H\left(X_{i} \mid X^{i-1}, Y^{i-k_{1}-1}, Z^{i}\right)-H\left(X_{i} \mid X^{i-1}, Y^{i}, Z^{i}\right) \\
& \leq H\left(X_{i} \mid X^{i-1}, Z^{i}\right)-H\left(X_{i} \mid X^{i-1}, Y^{i}, Z^{i}\right) \\
& \leq H\left(X_{i} \mid X_{i-k_{2}}^{i-1}, Z_{i-k_{2}}^{i}\right)-H\left(X_{i} \mid X^{i-1}, Y^{i}, Z^{i}\right) \\
& =H\left(X_{i} \mid X_{i-k_{2}}^{i-1}, Z_{i-k_{2}}^{i}\right)-H\left(X_{i} \mid X_{i-d}^{i-1}, Y_{i-d}^{i}, Z_{i-d}^{i}\right)
\end{aligned}
$$

$\leq H(X_{i}\mid X_{i-k_{2}}^{i-1},Z_{i-k_{2}}^{i})-H(X_{i}\mid X_{i-k_{2}}^{i-1},Y_{i-k_{2}}^{i},Z_{i-k_{2}}^{i})$ (21)

where (18), (19), and (21) follow from conditioning reduces entropy and (20) follows from joint $d$-Markovicity of $(X,Y,Z)$. Taking the sum over $i=1,\ldots,n$ and the normalized limit as $n\rightarrow\-\infty$ gives the desired result, noting that (17), (18), and (21) become the PDI, DI, and TDI rates, respectively.

## V. SIMULATIONS

In the above sections we have demonstrated that while one cannot reasonably expect data to satisfy the necessary assumptions for obtaining unbiased estimates of DI, the TDI and PDI can be used to provide upper and lower bounds for the true DI. A natural next question is, how significant is the difference between PDI and TDI? To address this question, we simulate a pair of jointly stationary Markov discrete processes in four settings, each characterized by a particular simplification of the generative distribution $p(X_{i},Y_{i}\mid X^{i-1},Y^{i-1})$:

$p(X_{i}\mid Y_{i-1})p(Y_{i}\mid Y_{i-1})$ (S1)
$p(X_{i}\mid X_{i-1},Y_{i-1})p(Y_{i}\mid Y_{i-1})$ (S2)
$p(X_{i}\mid X_{i-1},Y_{i-1})p(Y_{i}\mid X_{i-1},Y_{i-1})$ (S3)
$p(X_{i}\mid X_{i-2}^{i-1},Y_{i-2}^{i-1})p(Y_{i}\mid X_{i-2}^{i-1},Y_{i-2}^{i-1})$ (S4)

For each of these graphical structures, we conducted 100 experiments with $|\mathcal{X}|=|\mathcal{Y}|=4$ for (S1)-(S3) and $|\mathcal{X}|=|\mathcal{Y}|=$ $3$ for (S4). In each experiment, the parameters were sampled as independent exponential random variables and then appropriately normalized, yielding parameters drawn uniformly from the probability simplex [15]. Using the sampled parameters, sequences $(x^{n},y^{n})$ were generated with $n=300000$ (large enough to ensure that accurate estimates of the TDI and PDI could be obtained). $\tilde{I}_{T}^{(k)}(Y\rightarrow X)$ and $\tilde{I}_{P}^{(k)}(Y\rightarrow X)$ were estimated using CTW estimators in the style of $\tilde{I}_{3}$ in [3] for $k=d$, $d+1$, and $d+2^{1}$. Figure 1 shows boxplots representing $\tilde{I}_{T}^{(k)}(Y\rightarrow X)-\tilde{I}(Y\rightarrow X)$ and $\tilde{I}_{P}^{(k)}(Y\rightarrow X)-\tilde{I}(Y\rightarrow X)$

[1] Code and additional figures can be found in the following repository: https://github.com/gabeschamberg/directed_info_bias.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Difference between TDI and DI (blue) and PDI and DI (orange) for different values of $k$ (x-axis) under different process structures (panels).

for varying values of $k$ along with the mean (across trials) DI rate, which was determined by the value converged upon by the TDI and PDI. We can see that the TDI is very close to the true DI for simpler structures (i.e. (S1) and (S2)), and in these cases the PDI is not a very tight lower bound. However, for the fully connected structures (S3) and (S4) the TDI may be considerably larger than the true DI and the PDI serves as a useful lower bound for the true DI. This figure suggests that while (S4) is not covered by Theorem 2, alternative proof techniques may exist for demonstrating that the results hold for $d>1$.
