# A Birth and Death Process for Bayesian Network Structure Inference 

D. Jennings and J. N. Corcoran<br>University of Colorado

July 2, 2018


#### Abstract

Bayesian networks (BNs) are graphical models that are useful for representing highdimensional probability distributions. There has been a great deal of interest in recent years in the NP-hard problem of learning the structure of a BN from observed data. Typically, one assigns a score to various structures and the search becomes an optimization problem that can be approached with either deterministic or stochastic methods. In this paper, we walk through the space of graphs by modeling the appearance and disappearance of edges as a birth and death process and compare our novel approach to the popular Metropolis-Hastings search strategy. We give empirical evidence that the birth and death process has superior mixing properties.


## 1 Introduction

Bayesian networks (Pearl [13]) are convenient graphical expressions for high dimensional probability distributions representing complex relationships between a large number of random variables. A Bayesian network is a directed acyclic graph consisting of nodes which represent random variables and arrows which correspond to probabilistic dependencies between them.

There has been a great deal of interest in recent years on the NP-hard problem of learning the structure (placement of directed edges) of Bayesian networks from data ([1],[2],[4],[5], [6],[8],[9],[11],[12]). Much of this has been driven by the study of genetic regulatory networks in molecular biology due to advances in technology and, specifically, microarray techniques that allow scientists to rapidly measure expression levels of genes in cells. As an integral part of machine learning, Bayesian networks have also been used for pattern recognition, language processing including speech recognition, and credit risk analysis.

Structure learning typically involves defining a network score function and is then, in theory, a straightforward optimization problem. In practice, however, it is quite a different story as

[^0]
[^0]:    ${ }^{0}$ Keywords: Bayesian networks, structure learning, birth and death processes AMS Subject classification: 60J20, 60J75, 68T05

the number of possible networks to be scored and compared grows super-exponentially with the number of nodes. Simple greedy hill climbing with random restarts is understandably inefficient yet surprisingly hard to beat. There have been many deterministic and stochastic alternatives proposed in recent years such as gradient descent, genetic, tempering, and Metropolis-Hastings algorithms. There have been different approaches to the task, including order space sampling and the scoring of graph "features" rather than graphs themselves. Several of these methods have offered some improvement over greedy hill climbing but can be difficult to implement. Deterministic methods tend to get stuck in local maxima and probabilistic methods tend to suffer from slow mixing.

In this paper we consider a new stochastic algorithm in which the appearance and disappearance of edges are modeled as a birth and death process. We compare our algorithm with the popular Metropolis-Hastings algorithm and give empirical evidence that ours has better mixing properties.

# 2 Bayesian Networks 

Bayesian networks are graphical representations of the relationships between random variables from high dimensional probability distributions. A Bayesian Network on $N$ nodes is a directed acyclic graph (DAG) where the nodes (vertices), labeled $1,2, \ldots, N$, correspond to random variables $X_{1}, X_{2}, \ldots, X_{N}$ and directed edges correspond to probabilistic dependencies between them. We say that node $i$ is a parent of node $j$ and node $j$ is a child of node $i$ if there exists a directed edge from $i$ to $j$, (in which case we write $i \rightarrow j$ ), and use the notation $p a_{j}$ to denote the collection of all parents of node $j$. We will refer to nodes and their associated random variables interchangeably. Thus, $p a_{j}$ may also represent the collection of parent random variables for $X_{j}$. Rigorously, a Bayesian network consists of a DAG and a set of conditional densities $\left\{P\left(X_{i} \mid p a_{i}\right)\right\}_{i=1}^{N}$ along with the assumption that the joint density for the $N$ random variables can be written as the product

$$
P\left(X_{1}, X_{2}, \ldots, X_{N}\right)=\prod_{i=1}^{N} P\left(X_{i} \mid p a_{i}\right)
$$

In other words, all nodes are conditionally independent given their parents.
In the problem of structure inference, the DAG is not explicitly known. A set of observations $D=\left(D_{1}, D_{2}, \ldots, D_{M}\right)$ is given, where each $D_{i}$ is an $N$-tuple realization of $\left(X_{1}, X_{2}, \ldots, X_{N}\right)$. The goal is then to recover the "best" edge structure of the underlying Bayesian Network, which may be measured in many ways. For example, one may consider the best DAG as the one that maximizes the posterior probability

$$
P(G \mid D) \propto P(D \mid G) P(G)
$$

over $G$. Indeed, (1) is important for many measures of "best DAGs" and it is the goal of this paper to simulate DAGs efficiently from this distribution.

Throughout this paper, we will use the common assumption that the data $D$ come from a multinomial distribution, allowing us to analytically integrate out parameters to obtain a score which is proportional to $P(G \mid D)$.

# 3 Jump Processes 

Let $(\Omega, \mathcal{F})$ be a state space consisting of a non-empty set $\Omega$ and a sigma algebra $\mathcal{F}$ on $\Omega$. A jump process on $(\Omega, \mathcal{F})$ is a continuous time stochastic process that is characterized as follows. Assume the process is in some some state $x \in \Omega$.

- The waiting time until the next jump follows an exponential distribution with rate (or intensity) $\lambda(x)$ and is independent of the past history.
- The probability that the jump lands the process in $F \in \mathcal{F}$ is given by a transition kernel $K(x, F)$.

It is known (e.g. [3], [14]) that there exists a $Q_{t}: \Omega \times \mathcal{F} \rightarrow \mathbb{R}^{+}$so that $Q_{t}(x, F)$ is the probability that at time $t$ the process is in $F$ given that the process was in state $x$ at time 0 . Such $Q_{t}$ are defined as the solution to Kolmogorov's backward equation

$$
\frac{\partial}{\partial t} Q_{t}(x, F)=-\lambda(x) Q_{t}(x, F)+\lambda(x) \int_{\Omega} Q_{t}(y, F) K(x, d y)
$$

Furthermore, let $Q_{t}^{(n)}(x, F)$ be the probability of a transition from $x$ to $F$ using at most $n$ jumps. If $\lambda(x)$ is bounded then

$$
Q_{t}^{(\infty)}(x, F):=\lim _{n \rightarrow \infty} Q_{t}^{(n)}(x, F)
$$

is the unique minimal solution to Kolmogorov's forward equation

$$
\frac{\partial}{\partial t} Q_{t}(x, F)=-\int_{F} \lambda(z) Q_{t}(x, d z)+\int_{\Omega} \lambda(z) K(z, F) Q_{t}(x, d z)
$$

(It is "minimal" in the sense that if $R_{t}(x, F)$ is any other nonnegative solution, then $\left.R_{t}(x, F) \geq Q_{t}^{(\infty)}(x, F)\right)$ for all $\left.t \geq 0, x \in \Omega$, and $F \in \mathcal{F}.\right)$
For a distribution, $\pi$, to be invariant under such a process, $\pi$ must satisfy the detailed balance conditions

$$
\pi(x) \lambda(x) K(x, d y) d \mu(x)=\pi(y) \lambda(y) K(y, d x) d \mu(y)
$$

with respect to some density $\mu$.
Preston [14] extended this jump process to the trans-dimensional case where jumps from states in $\Omega_{n}$ can move the process to a one dimension higher state, living in $\Omega_{n+1}$, with (birth) rate $\lambda_{b}(x)$ or to a one dimension lower state, living in $\Omega_{n-1}$, with (death) rate $\lambda_{d}(x)$. Associated with these birth and death rates are birth and death kernels, $K_{b}$ and $K_{d}$. The total jump rate and the transition kernel are then given by

$$
\begin{gathered}
\lambda(x)=\lambda_{b}(x)+\lambda_{d}(x) \\
K(x, F)=\frac{\lambda_{b}(x)}{\lambda(x)} K_{b}(x, F)+\frac{\lambda_{d}(x)}{\lambda(x)} K_{d}(x, F)
\end{gathered}
$$

For a configuration $x$ with $n$ points to move to a configuration $x^{\prime}$ with $n+1$ points (or vice versa), the detailed balance conditions simplify ([14], [15]). In this case one needs the the birth rates to balance the death rates with respect to $\pi$. That is, we require that

$$
\pi(x) b\left(x, x^{\prime} \backslash x\right)=\pi\left(x^{\prime}\right) d\left(x^{\prime}, x^{\prime} \backslash x\right)
$$

where $b\left(x, x^{\prime} \backslash x\right)$ is the birth rate of the single point $x^{\prime} \backslash x$ given that the current configuration of points is $x$, and $d\left(x^{\prime}, x^{\prime} \backslash x\right)$ is the death rate of the single point $x^{\prime} \backslash x$ given that the current configuration of points is $x^{\prime}$. These relate to the total birth and death rates in that

$$
\begin{aligned}
\lambda_{b}(x) & =\sum b\left(x, x^{\prime} \backslash x\right) \\
\lambda_{d}\left(x^{\prime}\right) & =\sum d\left(x^{\prime}, x^{\prime} \backslash x\right)
\end{aligned}
$$

where the birth sum is taken over all states $x^{\prime}$ that consist of configuration $x$ with the addition of a single point and the death sum is taken over all states $x$ that consist of configuration $x^{\prime}$ with a single point deleted.

# 4 A Birth and Death Process on Edges of a BN 

To construct a jump process for BN structure inference, our goal is to construct a birth and death process acting on edges of a BN which has invariant distribution $P(G \mid D)$.
The relevant state space is $\left(\mathcal{G}, 2^{\mathcal{G}}\right)$, where $\mathcal{G}$ is the set of all DAGs with $N$ nodes and $2^{\mathcal{G}}$ is the power set of $\mathcal{G}$. We define the disjoint sets $\mathcal{G}_{k}, k=0, \ldots, \frac{N(N-1)}{2}$, to be the set of DAGs with exactly $k$ edges. Our jump process will then jump between the $\mathcal{G}_{k}$ for adjacent values of $k$.

For $G \in \mathcal{G}_{k}$, denote the graph with the addition of the edge from node $i$ to node $j$ by $(G \cup\{i \rightarrow j\}) \in \mathcal{G}_{k+1}$, and the graph with the removal of the edge from $i$ to $j$ by $(G \backslash\{i \rightarrow$ $j\}) \in \mathcal{G}_{k-1}$. Detailed balance then requires that, for every edge $i \rightarrow j$ that is a valid (non-cycle causing) addition,

$$
P(G \mid D) b(G,\{i \rightarrow j\})=P(G \cup\{i \rightarrow j\} \mid D) d(G \cup\{i \rightarrow j\},\{i \rightarrow j\})
$$

It is convenient to let

$$
d(G \cup\{i \rightarrow j\},\{i \rightarrow j\})=1
$$

so that

$$
\begin{aligned}
b(G,\{i \rightarrow j\}) & =\frac{P(G \cup\{i \rightarrow j\} \mid D)}{P(G \mid D)} \\
& =\frac{P(D \mid G \cup\{i \rightarrow j\}) P(G \cup\{i \rightarrow j\})}{P(D \mid G) P(G)}
\end{aligned}
$$

If we let $\Delta_{j}$ denote the $M$-dimensional vector of observations of $X_{j}$ in the data set $D$, this birth rate may be rewritten as

$$
b(G,\{i \rightarrow j\})=\frac{P\left(\Delta_{j} \mid \Delta_{p a_{j}^{\prime}}, G \cup\{i \rightarrow j\}\right) P(G \cup\{i \rightarrow j\})}{P\left(\Delta_{j} \mid \Delta_{p a_{j}}, G\right) P(G)}
$$

Here, $\Delta_{p a_{j}}$ is the $M \times k$ matrix of data points for the $k$ parents of node $j$ in $G\left(\Delta_{p a_{j}}=\emptyset\right.$ if $k=0$ ) and $\Delta_{p a_{j}^{\prime}}$ is the $M \times(k+1)$ matrix of data points for the $k$ parents of node $j$ in $G \cup\{i \rightarrow j\}$.

The transition rates are then given by

$$
\begin{gathered}
\lambda_{b}(G)=\sum_{\text {valid } i \rightarrow j} b(G,\{i \rightarrow j\}) \\
\lambda_{d}(G)=\sum_{\{i \rightarrow j\} \in G} 1
\end{gathered}
$$

With this, we can easily construct a way to simulate from this process in the following way.

1. Start with an arbitrary initial DAG, $G$
2. Compute the birth rates $b(G,\{i \rightarrow j\})$ for all possible valid $i \rightarrow j$ edge additions to G. Compute

$$
\lambda_{b}(G)=\sum_{\text {valid } i \rightarrow j} b(G,\{i \rightarrow j\})
$$

and

$$
\lambda_{d}(G)=\sum_{\{i \rightarrow j\} \in G} 1
$$

3. With probability $\lambda_{d}(G) /\left(\lambda_{b}(G)+\lambda_{d}(G)\right)$, remove a randomly selected existing edge. Otherwise, add valid edge $i \rightarrow j$ with probability $b(G,\{i \rightarrow j\}) / \lambda_{b}(G)$.
4. Return to step 2 .

At first glance, it may seem like such an algorithm would be computationally expensive, as the required birth rates depend on computing the score for two different graphs. However, if we assume a modular score, the computation at each step is manageable. A modular score means we have

$$
P(D \mid G)=\prod_{i=1}^{N} P\left(\Delta_{i} \mid \Delta_{p a_{i}}, G\right)
$$

which leads to a birth rate of

$$
\begin{aligned}
b(g,\{i \rightarrow j\}) & =\frac{P(G \cup\{i \rightarrow j\}) \prod_{i=1}^{N} P\left(\Delta_{i} \mid \Delta_{p a_{i}^{\prime}}, G \cup\{i \rightarrow j\}\right)}{P(G) \prod_{i=1}^{N} P\left(\Delta_{i} \mid \Delta_{p a_{i}^{\prime}}, G\right)} \\
& =\frac{P(G \cup\{i \rightarrow j\}) P\left(\Delta_{j} \mid \Delta_{p a_{j}^{\prime}}, G \cup\{i \rightarrow j\}\right)}{P(G) P\left(\Delta_{j} \mid \Delta_{p a_{j}}, G\right)}
\end{aligned}
$$

So, for each birth rate, we only need the ratio of the altered score to current score of a single node corresponding to the child end of the proposed edge.

Further computational relief comes from the fact that most of the birth rates can be stored from previous steps. After adding or removing an edge, the only birth rates that need to be recalculated are for edges pointing to nodes whose parent set has been altered, edges which were not previously valid, or edges which are no longer valid.

These realizations allow for a more complete and efficient algorithm

1. Start with an initial DAG, $G$
2. For all possible edge additions, $i \rightarrow j$, calculate the birth rate $b(G,\{i \rightarrow j\})$
3. With probability $\lambda_{d}(G) /\left(\lambda_{b}(G)+\lambda_{d}(G)\right)$, remove a randomly selected existing edge. Otherwise, add a valid edge $k \rightarrow \ell$ with probability $b(G,\{k \rightarrow \ell\})$.
4. If any of the following are true, update the birth rate $b(G,\{i \rightarrow j\})$.

- $j=\ell$
- Edge $i \rightarrow j$ was not a valid addition before the addition or removal of edge $k \rightarrow \ell$ but now is valid
- Edge $i \rightarrow j$ was a valid addition before the addition or removal of edge $k \rightarrow \ell$ but now is not longer valid

5. Return to step 3 .

# 5 Experimental Results 

While the theory guarantees that our edge birth and death process will have the correct stationary distribution, in this Section we investigate the mixing time and whether or not Monte Carlo simulation of graphs from $P(G \mid D)$ using our method is feasible in practice. We first consider a simple 4 node graph so that we may compare our results with exact computations. We generated 50 observations of $X_{1}, X_{2}, X_{3}, X_{4}$ as related by the DAG in Figure 1. Each node was allowed to take on values in $\{1,2,3,4\}$, with equal probability.

We then ran both the standard Metropolis Hastings chain for BNs ([10]) and our edge birth and death algorithm. Figure 2 shows two independent runs of each algorithm. While both algorithms tend to find high probability regions of the state space, our edge birth and death algorithm explores much more of the state space.

One benefit of running Monte Carlo methods is they allow us to easily calculate the probabilities of specific graph features, e.g. edge probabilities. With the edge birth and death process, the edge probabilities correspond to the proportion of time that the graphs contain the given edge. With the same 4 node graph as before, we calculated the edge probabilities and compare them to the true edge probabilities both for $m=100$ observations and $m=500$ observations. The results are shown in Table 1.

Next, we tested our edge birth and death algorithm on the "Alarm data set" compiled by Herskovits ([7]). This data set, often used as a benchmark for structure learning algorithms,

![img-0.jpeg](img-0.jpeg)

Figure 1: 4 Node Graph Used for Testing

![img-1.jpeg](img-1.jpeg)

Figure 2: (a) Paths of two (red and blue) independent Metropolis Hastings chains of 20000 steps. (b) Paths of two independent edge birth and death process runs of 1500 jumps. The circles represent each of the 543 possible DAGs, with size proportional to the posterior probability of the graph.



Table 1: Magnitudes of errors between estimated and exact probabilities of edges in a 4 node Bayesian network from one run of the edge birth and death algorithm for 100 observations (left) and 500 observations (right).

![img-2.jpeg](img-2.jpeg)

Figure 3: (a) AIC score of a Metropolis Hastings run of $2 \times 10^{6}$ steps. (b) AIC score of an edge birth and death process run of $10^{5}$ steps.
consists of 1000 observations of 37 random variables, each taking on 4 possible values. We ran our edge birth and death algorithm for $10^{5}$ time steps. For comparison, we ran the standard Metropolis-Hastings scheme for $2 \times 10^{6}$ steps which took approximately the same amount of CPU time. Akaike's information criteria (AIC) was recorded at each step and is plotted for one of these runs in Figure 3. As is well known, the MH scheme is prone to getting trapped in local minima, and takes many steps to escape these points whereas our edge birth and death algorithm appears to mix more easily.

# 6 Conclusions 

We have presented a new algorithm for sampling from the posterior distribution of Bayesian Networks given data based on a birth and death process. This new edge birth and death algorithm allows for probabilistic inferences to be made about Bayesian Network structures while avoiding some of the downfalls of existing methods. In particular, our edge birth and death process does not get trapped in local extrema as easily as structure MCMC and allows for less restrictive choices of priors over graphs compared to order MCMC.

An open question related to this new algorithm is whether it can be made perfect by applying similar constructions to perfect algorithms for spatial point processes.
