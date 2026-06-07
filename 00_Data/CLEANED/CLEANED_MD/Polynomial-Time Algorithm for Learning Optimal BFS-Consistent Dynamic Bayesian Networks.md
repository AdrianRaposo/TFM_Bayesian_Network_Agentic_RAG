# Article 

## Polynomial-Time Algorithm for Learning Optimal BFS-Consistent Dynamic Bayesian Networks

Margarida Sousa and Alexandra M. Carvalho *<br>Instituto de Telecomunicações, Instituto Superior Técnico, Universidade de Lisboa, 1049-001 Lisboa, Portugal; margarida.sousa@tecnico.ulisboa.pt<br>* Correspondence: alexandra.carvalho@tecnico.ulisboa.pt; Tel.: +351-218-418-454

Received: 22 March 2018; Accepted: 10 April 2018; Published: 12 April 2018


#### Abstract

Dynamic Bayesian networks (DBN) are powerful probabilistic representations that model stochastic processes. They consist of a prior network, representing the distribution over the initial variables, and a set of transition networks, representing the transition distribution between variables over time. It was shown that learning complex transition networks, considering both intra- and inter-slice connections, is NP-hard. Therefore, the community has searched for the largest subclass of DBNs for which there is an efficient learning algorithm. We introduce a new polynomial-time algorithm for learning optimal DBNs consistent with a breadth-first search (BFS) order, named bcDBN. The proposed algorithm considers the set of networks such that each transition network has a bounded in-degree, allowing for $p$ edges from past time slices (inter-slice connections) and $k$ edges from the current time slice (intra-slice connections) consistent with the BFS order induced by the optimal tree-augmented network (tDBN). This approach increases exponentially, in the number of variables, the search space of the state-of-the-art tDBN algorithm. Concerning worst-case time complexity, given a Markov lag $m$, a set of $n$ random variables ranging over $r$ values, and a set of observations of $N$ individuals over $T$ time steps, the bcDBN algorithm is linear in $N, T$ and $m$; polynomial in $n$ and $r$; and exponential in $p$ and $k$. We assess the bcDBN algorithm on simulated data against tDBN, revealing that it performs well throughout different experiments.


Keywords: dynamic Bayesian networks; optimum branching; score-based learning; theoreticalinformation scores

## 1. Introduction

Bayesian networks (BN) represent, in an efficient and accurate way, the joint probability of a set of random variables [1]. Dynamic Bayesian networks (DBN) are the dynamic counterpart of BNs and model stochastic processes [2]. DBNs consist of a prior network, representing the distribution over the initial attributes, and a set of transition networks, representing the transition distribution between attributes over time. They are used in a large variety of applications such as protein sequencing [3], speech recognition [4] and clinical forecasting [5].

The problem of learning a BN given data consists in finding the network that best fits the data. In a score-based approach, a scoring criterion is considered, which measured how well the network fits the data [6-10]. In this case, learning a BN reduces to the problem of finding the network that maximizes the score, given the data. Methods for learning DBNs are simple extensions of those considered for BNs [2]. Not taking into account the acyclicity constraints, it was proved that learning BNs does not have to be NP-hard [11]. This result can be applied to DBNs, not considering the intra-slice connections, as the resulting unrolled graph, which contains a copy of each attribute in each time slice, is acyclic. Profiting from this result, a polynomial-time algorithm for learning optimal DBN was proposed using the Mutual Information Tests (MIT) [12]. However, none of these algorithms

learns general $m$ th-order Markov DBNs such that each transition network has inter- and intra-slice connections. More recently, a polynomial-time algorithm was proposed that learns both the inter- and intra-slice connections in a transition network [13]. The search space considered, however, is restricted to the tree-augmented network structures, resulting in the so-called tDBN.

By looking into lower-bound complexity results for learning BNs, it is known that learning tree-like structures is polynomial [14]. However, learning 2-polytrees is already NP-hard [15]. Learning efficiently structures richer than branchings (a.k.a. tree-like structures) has eluded the community, that resorted to use heuristic approaches. Carvalho et al. [16] suggested to search over graphs consistent with the topological order of an optimal branching. The advantage of this approach is that the search space increased exponentially with respect to branchings, while keeping the learning complexity in polynomial time. Later, the breadth-first search (BFS) order of an optimal branching was also considered [17], further improving the previous results in terms of search space.

In this paper, we propose a generalization of the tDBN algorithm, considering DBNs such that each transition network is consistent with the order induced by the BFS order of the optimal branching of the tDBN network, that we call bcDBN. Furthermore, we prove that the search space increases exponentially, in the number of attributes, comparing with the tDBN algorithm, while running in polynomial time.

We start by reviewing the basic concepts of Bayesian networks, dynamic Bayesian networks and their learning algorithms. Then, we present the proposed algorithm and the experimental results. The paper concludes with a brief discussion and directions for future work.

# 2. Bayesian Networks 

Let $X$ denote a discrete random variable that takes values over a finite set $\mathcal{X}$. Furthermore, let $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$ represent an $n$-dimensional random vector, where each $X_{i}$ takes values in $\mathcal{X}_{i}=\left\{x_{i 1}, \ldots, x_{i r_{i}}\right\}$, and $P(\mathbf{x})$ denotes the probability that $\mathbf{X}$ takes the value $\mathbf{x}$. A Bayesian network encodes the joint probability distribution of a set of $n$ random variables $\left\{X_{1}, \ldots, X_{n}\right\}$ [1].

Definition 1 (Bayesian Network). A n-dimensional Bayesian Network (BN) is a triple $B=(\mathbf{X}, G, \Theta)$, where:

- $\quad \mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$ and each random variable $X_{i}$ takes values in the set $\left\{x_{i 1}, \ldots, x_{i r_{i}}\right\}$, where $x_{i k}$ denotes the $k$-th value $X_{i}$ takes.
- $\quad G=(\mathbf{X}, E)$ is a directed acyclic graph (DAG) with nodes in $\mathbf{X}$ and edges $E$ representing direct dependencies between the nodes.
- $\Theta=\left\{\Theta_{i j k}\right\}_{i \in 1 \ldots n, j \in 1 \ldots q_{i}, k \in 1, \ldots, r_{i}}$ encodes the parameters of the network G, a.k.a. conditional probability tables (CPT):

$$
\Theta_{i j k}=P_{B}\left(X_{i}=x_{i k} \mid \Pi_{X_{i}}=w_{i j}\right)
$$

where $\Pi_{X_{i}}$ denotes the set of parents of $X_{i}$ in the network $G$ and $w_{i j}$ is the $j$-th configuration of $\Pi_{X_{i}}$, among all possible configurations given by $\left\{w_{i 1}, \ldots, w_{i q_{i}}\right\}$, with $q_{i}=\prod_{X_{j} \in \Pi_{X_{i}}} r_{j}$ denoting the total number of parent configurations.

A BN $B$ induces a unique joint probability distribution over $\mathbf{X}$ given by:

$$
P_{B}\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P_{B}\left(X_{i} \mid \Pi_{X_{i}}\right)
$$

Let $N_{i j k}$ be the number of instances in data set $D$ of size $N$, where variable $X_{i}$ takes the value $x_{i k}$ and the set of parents $\Pi_{X_{i}}$ takes the configuration $w_{i j}$. Denote the number of instances in $D$ where the set of parents $\Pi_{X_{i}}$ takes the configuration $w_{i j}$ by

$$
N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}
$$

Observe that,

$$
X_{i} \mid \Pi_{X_{i}} \sim \operatorname{Multinomial}\left(N_{i j}, \theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)
$$

for $i \in\{1, \ldots, n\}$ and $j \in\left\{1, \ldots, q_{i}\right\}$.
Intuitively, the graph of a BN can be viewed as a network structure that provides the skeleton for representing the joint probability compactly in a factorized way, and making inferences in the probabilistic graphical model provides the mechanism for gluing all these components back together in a probabilistic coherent manner [18].

An example of a BN is depicted in Figure 1. It describes cash compensation and overnight accommodation to air passengers in the event of long flight delays. A flight may be delayed due to aircraft maintenance problems or severe weather (hurricane, blizzard, etc.). Whenever the delay is not caused by an external event to the airline company, a passenger may be entitled to a monetary compensation. Regardless of the cause, if the delay is long enough, the passenger might be offered an overnight accommodation. As a result of the dependences encoded by the graph, the joint probability distribution of the network can be factored as

$$
P(M, S, F, O, C)=P(M) P(S) P(F \mid M, S) P(O \mid F) P(C \mid F, S)
$$

where only the first letter of a variable name is used: $M$-Maintenance problems; $S$-Severe weather; $F$-Flight delay; $O$-Overnight accommodation; and $C$-Cash compensation. In this simple example, all variables are Bernoulli (ranging over $T$ and $F$ ). Inside the callouts only the CPTs for variables taking the value $T$ are given.
![img-0.jpeg](img-0.jpeg)

Figure 1. A BN example regarding airline regulations with conditional probability tables.

# 3. Learning Bayesian Networks 

Learning a Bayesian network is two-fold: parameter learning and structure learning. When learning the parameters, we assume the underlying graph $G$ is given, and our goal is to estimate the set of parameters of the network $\Theta$. When learning the structure, the goal is to find a structure $G$, given only the training data. We assume data is complete, i.e., each instance is fully observed, there are no missing values nor hidden variables, and the training set $D=\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{N}\right\}$ is given by a set of $N$ i.i.d. instances. Using general results of the maximum likelihood estimate in a multinomial distribution we get the following estimate for the parameters of a BN $B$ :

$$
\hat{\theta}_{i j k}=\frac{N_{i j k}}{N_{i j}}
$$

that is denoted by observed frequency estimate (OFE).
In score-based learning, a scoring function $\phi: \mathcal{S} \times \mathcal{X} \rightarrow \mathbb{R}$ is required to measure how well a BN $B$ fits the data $D$ (where $\mathcal{S}$ denotes the search space). In this case, the learning procedure can be extremely efficient if the employed score is decomposable. A scoring function $\phi$ is said to be decomposable if the score can be expressed as a sum of local scores that depends only on each node and its parents, that is, in the form:

$$
\phi(B, D)=\sum_{i=1}^{n} \phi_{i}\left(\Pi_{X_{i}}, D\right)
$$

Well-known decomposable scores are divided in two classes: Bayesian and information-theoretical. Herein, we focus only on two information-theoretical criteria, namely Log-Likelihood (LL) and Minimum Description Length (MDL) [19]. Information-theoretical scores are based on the compression achieved to describe the data, given an optimal code induced by a probability distribution encoded by a BN.

The LL is given by:

$$
L L(B \mid D)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \log \left(\theta_{i j k}\right)
$$

This criterion favours complete network structures, and does not generalize well, leading to the overfitting of the model to the training data. The MDL criterion, proposed by Rissanen [19], imposes that the parameters of the model, ignored in the LL score, must also be accounted. The MDL score for learning BNs is defined by:

$$
M D L(B \mid D)=L L(B \mid D)-\frac{1}{2} \ln (N)|B|
$$

where $|B|$ corresponds to the number of parameters $\Theta$ of the network, given by:

$$
$$

The penalty introduced by MDL creates a trade off between fitness and model complexity, providing a model selection criterion robust to overfitting.

The structure learning reduces to an optimization problem: given a scoring function, a data set, a search space and a search procedure, find the network that maximizes this score. Denote the set of BNs with $n$ random variables by $\mathcal{B}_{n}$.

Definition 2 (Learning a Bayesian Network). Given a data $D=\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{N}\right\}$ and a scoring function $\phi$, the problem of learning a Bayesian network is to find a Bayesian network $B \in \mathcal{B}_{n}$ that maximizes the value $\phi(B, D)$.

The space of all Bayesian networks with $n$ nodes has a superexponential number of structures, $2^{\mathcal{O}\left(n^{2}\right)}$. Learning general Bayesian networks is a NP-hard problem [20-22]. However, if we restrict the search space $\mathcal{S}$ to tree-like structures [14,23] or to networks with bounded in-degree and a known ordering over the variables [24], it is possible to obtain a global optimal solution for this problem. Polynomial-time algorithms to learn BNs with underlying consistent $k$-graphs ( C $k \mathrm{G}$ ) [16] and breadth-first search consistent $k$-graphs ( $\mathrm{BC} k \mathrm{G}$ ) [17] network structures were proposed. The sets of C $k \mathrm{G}$ and $\mathrm{BC} k \mathrm{G}$ graphs are exponentially larger, in the number of variables, when compared with branchings $[16,17]$.

Definition 3 ( $k$-graph). A $k$-graph is a graph where each node has in-degree at most $k$.

Definition 4 (Consistent $k$-graph). Given a branching $R$ over a set of nodes $V$, a graph $G=(V, E)$ is said to be a consistent $k$-graph (CkG) w.r.t. $R$ if it is a $k$-graph and for any edge in $E$ from $X_{i}$ to $X_{j}$ the node $X_{i}$ is in the path from the root of $R$ to $X_{j}$.

Definition 5 (BFS-consistent $k$-graph). Given a branching $R$ over a set of nodes $V$, a graph $G=(V, E)$ is said to be a BFS-consistent $k$-graph (BCkG) w.r.t. $R$ if it is a $k$-graph and for any edge in $E$ from $X_{i}$ to $X_{j}$ the node $X_{i}$ is visited in breadth-first search (BFS) of $R$ before $X_{j}$.

Observe that the order induced by the optimal branching might be partial, while its BFS order is always total (and refines it). Given a BFS-consistent $k$-graph, there can only exist an edge from $X_{i}$ to $X_{j}$ if $X_{i}$ is less than or as deep as $X_{j}$ in $R$. We assume that if $i<j$ and $X_{i}$ and $X_{j}$ are at the same level, then the BFS over $R$ reaches $X_{i}$ before $X_{j}$. An example is given in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Given the branching $R$ represented in (a); (b) represents a consistent 2-graph with respect to $R$; (c) represents the BFS of R and (d) represents a BFS-consistent 2-graph of $R$ (not consistent with $R$ ).

# 4. Dynamic Bayesian Networks 

Dynamic Bayesian networks (DBN) model the stochastic evolution of a set of random variables over time [2]. Consider the discretization of time in time slices given by the set $\mathcal{T}=\{0, \ldots, T\}$. Let $\mathbf{X}[t]=\left(X_{1}[t], \ldots, X_{n}[t]\right)$ be a random vector that denotes the value of the set of attributes at time $t$. Furthermore, let $\mathbf{X}\left[t_{1}: t_{2}\right]$ denote the set of random variables $\mathbf{X}$ for the interval $t_{1} \leq t \leq t_{2}$. Consider a set of individuals $\mathcal{H}$ measured over $T$ sequential instants of time. The set of observations is represented as $\left\{\mathbf{x}^{h}[t]\right\}_{h \in \mathcal{H}, t \in \mathcal{T}}$, where $\mathbf{x}^{h}[t]=\left(x_{1}^{h}, \ldots, x_{n}^{h}\right)$ is a single observation of $n$ attributes, measured at time $t$ and referring to individual $h$.

In the setting of DBNs the goal is to define a probability joint distribution over all possible trajectories, i.e., possible values for each attribute $X_{i}$ and instant $t, X_{i}[t]$. Let $P\left(\mathbf{X}\left[t_{1}: t_{2}\right]\right)$ denote the joint probability distribution over the trajectory of the process from $\mathbf{X}\left[t_{1}\right]$ to $\mathbf{X}\left[t_{2}\right]$. The space of possible trajectories is very large, therefore in order to define a tractable problem it is necessary to make assumptions and simplifications.

Observations are viewed as i.i.d. samples of a sequence of probability distributions $\left\{P_{\theta[t]}\right\}_{t \in \mathcal{T}}$. For all individuals $h \in \mathcal{H}$, and a fixed time $t$, the probability distribution is considered constant, i.e., $\mathbf{x}^{h}[t] \sim P_{\theta[t]}, h \in \mathcal{H}$. Using the chain rule the joint probability over $\mathbf{X}$ is given by:

$$
P(\mathbf{X}[0: T])=P(\mathbf{X}[0] \prod_{t=0}^{T-1} P(\mathbf{X}[t+1] \mid \mathbf{X}[0: t])
$$

Definition 6 ( $m$ th-Order Markov assumption). A stochastic process over $\mathbf{X}$ satisfies the mth-order Markov assumption if, for all $t \geq 0$

$$
P(\mathbf{X}[t+1] \mid \mathbf{X}[0: t])=P(\mathbf{X}[t+1] \mid \mathbf{X}[t-m+1: t])
$$

In this case $m$ is called the Markov lag of the process.

If all conditional probabilities in Equation (7) are invariant to shifts in time, that is, are the same for all $t \in \mathcal{T}$, then the stochastic process is called a stationary $m$ th-order Markov process.

Definition 7 (First-order Markov DBN). A non-stationary first-order Markov DBN consists of:

- A prior network $B^{0}$, which specifies a distribution over the initial states $\mathbf{X}[0]$.
- A set of transition networks $B_{t}^{t+1}$ over the variables $\mathbf{X}[t: t+1]$, representing the state transition probabilities, for $0 \leq t \leq T-1$.

We denote by $G_{t+1}$ the subgraph of $B_{t}^{t+1}$ with nodes $\mathbf{X}[t+1]$, that contains only the intra-slice dependencies. The transition network $B_{t}^{t+1}$ has the additional constraint that edges between slices (inter-slice connections) must flow forward in time. Observe that in the case of a first-order DBN a transition network encodes the inter-slice dependencies (from time transitions $t \rightarrow t+1$ ) and intra-slice dependencies (in the time slice $t+1$ ).

Figure 3 shows an example of a DBN, aiming to infer a driver behaviour. The model describes the state of a car, including its velocity and distance to the following vehicle, as well as, the weather and the type of road (highway, arterial, local road, etc.). In the beginning, the speed depends only if there is a car nearby. After that, the velocity depends on: (i) the previous weather (the road might be icy because it snowed last night); (ii) the current weather (it might be raining now); (iii) how close the car was from another (if it gets too close the driver might need to break); and (iv) the current type of road (with different velocity limits). The current distance to the following car depends on the previous car velocity and on the previous distance to the next vehicle. Figure 4 joins the prior and transition networks and extends the unrolled DBN to a third time slice.
![img-2.jpeg](img-2.jpeg)

Figure 3. A simple example of a first-order Markov stationary DBN. On the left, the prior network $B_{0}$, for $t=0$. On the right, a two-slice transition network $B_{t}^{t+1}$.

Learning DBNs, considering no hidden variables or missing values, i.e., considering a fully observable process, reduces simply to applying the methods described for BNs for each transition of time [25]. Several algorithms for learning DBNs are concerned with identifying inter-slice connections only, disregarding intra-slice dependencies or assuming they are given by some prior network and kept fixed over time [11,12,26]. Recently, a polynomial-time algorithm was proposed that learns both the inter and intra-slice connections in a transition network [13]. However, the search space is restricted to tree-augmented network structures (tDBN), i.e., acyclic networks such that each attribute has one parent from the same time slice, but can have at most $p$ parents from the previous time slices.

![img-3.jpeg](img-3.jpeg)

Figure 4. The DBN example from Figure 3 is unrolled for the first three time slices.

Definition 8 (Tree-augmented DBN). A dynamic Bayesian network is called tree-augmented (tDBN) if for each transition network $\{t-m+1, \ldots, t\} \rightarrow t+1$ each attribute $X_{i}[t+1]$ has exactly one parent in the time slice $t+1$, except the root, and at most $p$ parents from the preceding time slices $\{t-m+1, \ldots, t\}$.

# 5. Learning Consistent Dynamic Bayesian Networks 

We introduce a polynomial-time algorithm for learning DBNs such that: the intra-slice network has in-degree at most $k$ and is consistent with the BFS order of the tDBN; the inter-slice network has in-degree of at most $p$. The main idea of this approach is to add dependencies that were lost due to the tree-augmented restriction of the tDBN and, furthermore, remove irrelevant ones that might be present because a connected graph was imposed. Moreover, we also consider the BFS order of the intra-slice network as an heuristic for a causality order between variables. We make this concept rigorous with the following definition.

Definition 9 (BFS-consistent $k$-graph DBN). A dynamic Bayesian network is called BFS-consistent $k$-graph (bcDBN) if for each intra-slice network $G_{t+1}$, with $t \in\{0, \ldots, T-1\}$, the following holds:

- $G_{t+1}$ is a k-graph, i.e., each node has in-degree at most $k$;
- Given an optimal branching $R_{t+1}$ over the set of nodes $\mathbf{X}[t+1]$, for every edge in $G_{t+1}$ from $X_{i}[t+1]$ to $X_{j}[t+1]$, the node $X_{i}[t+1]$ is visited in the BFS of $R_{t+1}$ before $X_{j}[t+1]$.

Moreover, each node $X_{i}[t+1]$ has at most $p$ parents from previous time slices.
Before we present the learning algorithm, we need to introduce some notation, namely, the concept of ancestors of a node.

Definition 10 (Ancestors of a node). The ancestors of a node $X_{i}$ in time slice $t+1$, denoted by $a_{i, t+1}^{B F S}$, are the set of nodes in slice $t+1$ connecting the root of the BFS of an optimal branching $R_{t+1}$ and $X_{i}[t+1]$.

We will now describe briefly the proposed algorithm for learning a transition network of a $m$ th-order bcDBN. Let $\mathcal{P}_{\leq p}(\mathbf{X}[t-m+1: t])$ be the set of subsets of $\mathbf{X}[t-m+1: t]$ of cardinality less than or equal to $p$. For each node $X_{i}[t+1] \in \mathbf{X}[t+1]$, the optimal set of past parents $\left(\mathbf{X}_{p s} \in \mathcal{P}_{\leq p}(\mathbf{X}[t-m+1: t])\right.$ ) and maximum score $\left(s_{i}\right)$ is found,

$$
s_{i}=\max _{\mathbf{X}_{p s}[t-m+1: t] \in \mathcal{P}_{\leq p}(\mathbf{X}[t-m+1: t])} \phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t], D_{t-m+1}^{t+1}\right)
$$

where $\phi_{i}$ is the local contribution of $X_{i}[t+1]$ for the overall score $\phi$ and $D_{t-m+1}^{t+1}$ is the subset of observations concerning the time transition $t-m+1 \rightarrow t+1$. For each possible edge in $t+1$, $X_{j}[t+1] \rightarrow X_{i}[t+1]$, the optimal set of past parents and maximum score $\left(s_{i j}\right)$ is determined,

$$
s_{i j}=\max _{\mathbf{X}_{p s}[t-m+1: t] \in \mathcal{P}_{\leq p}(\mathbf{X}[t-m+1: t])} \phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t] \cup\left\{X_{j}[t+1]\right\}, D_{t-m+1}^{t+1}\right)
$$

We note that the set $\mathbf{X}_{p s}[t-m+1: t]$ that maximizes Equations (8) and (9) needs not to be the same. The one in Equation (8) refers to the best set of $p$ parents from past time slices, and the one in Equation (9) concerns the best set of $p$ parents from the past time slices when $X_{j}[t+1]$ is also a parent of $X_{i}[t+1]$.

A complete directed graph is built such that each edge $X_{j}[t+1] \rightarrow X_{i}[t+1]$ has the following weight,

$$
e_{i j}=s_{i j}-s_{i}
$$

that is, the gain in the network score of adding $X_{j}[t+1]$ as a parent of $X_{i}[t+1]$. Generally $e_{i j} \neq e_{j i}$, as the edge $X_{i}[t+1] \rightarrow X_{j}[t+1]$ may account for the contribution from the inter-slice parents and, in general, inter-slice parents of $X_{i}[t+1]$ and $X_{j}[t+1]$ are not the same. Therefore, Edmond's algorithm is applied to obtain a maximum branching for the intra-slice network [27]. In order to obtain a total order, the BFS order of the output maximum branching is determined and the set of candidate ancestors $\alpha_{i, t+1}^{B F S}$ is computed. For node $X_{i}[t+1]$, the optimal set of past parents $\mathbf{X}_{p s}[t-m+1: t]$ and intra-slice parents, denoted by $\mathbf{X}_{p s}[t+1]$, are obtained in a one-step procedure by finding

$$
\max _{\mathbf{X}_{p s}[t-m+1: t] \in \mathcal{P}_{\leq p}(\mathbf{X}[t-m+1: t])} \max _{\mathbf{X}_{p s}[t+1] \in \mathcal{P}_{\leq k}\left(\alpha_{i, t+1}^{B F S}\right)} \phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t] \cup \mathbf{X}_{p s}[t+1], D_{t-m+1}^{t+1}\right)
$$

where $\mathcal{P}_{\leq k}\left(\alpha_{i, t+1}^{B F S}\right)$ is the set of all subsets of $\alpha_{i, t+1}^{B F S}$ of cardinality less than or equal to $k$. Note that, if $X_{i}[t+1]$ is the root, $\mathcal{P}_{\leq k}\left(\alpha_{i, t+1}^{B F S}\right)=\{\varnothing\}$, so the set of intra-slice parents $\mathbf{X}_{p s}[t+1]$ of $X_{i}[t+1]$ is always empty.

The pseudo-code of the proposed algorithm is given in Algorithm 1. As parameters, the algorithm needs: a dataset $D$, a Markov lag $m$, a decomposable scoring function $\phi$, a maximum number of inter-slice parents $p$ and a maximum number of intra-slice parents $k$.

```
Algorithm 1 Learning optimal \(m\) th-order Markov bcDBN
    for each transition \(\{t-m+1, \ldots, t\} \rightarrow t+1\) do
        Build a complete directed graph in \(\mathbf{X}[t+1]\).
        Weight all edges \(X_{j}[t+1] \rightarrow X_{i}[t+1]\) of the graph with \(e_{i j}\) as in Equation (10) (Algorithm 2).
        Apply Edmond's algorithm to the intra-slice network, to obtain an optimal branching.
        Build the BFS order of the output optimal branching.
        for all nodes \(X_{i}[t+1]\) do
            Compute the set of parents of \(X_{i}[t+1]\) as in Equation (11) (Algorithm 3).
        end for
    end for
    Collect the transition networks to obtain the optimal bcDBN structure.
```

The algorithm starts by building the complete directed graph in Step 2, after which the graph is weighted according to Equation (10); this procedure is described in detail in Algorithm 2. The Edmonds' algorithm is then applied to the intra-slice network, resulting from that an optimal branching (Step 4). The BFS order of this branching is computed (Step 5) and the final transition network is redefined to be consistent with it. This is done by computing the parents of $X_{i}[t+1]$ given by Equation (11) (Steps 6-7), further detailed in Algorithm 3.

Theorem 1. Algorithm 1 finds an optimal mth-order Markov bcDBN, given a decomposable scoring function $\phi$, a set of $n$ random variables, a maximum intra-slice network in-degree of $k$ and a maximum inter-slice network in-degree of $p$.

Proof. Let $B$ be the optimal bcDBN and $B^{\prime}$ be the DBN output of Algorithm 1. Consider without loss of generality the time transition $\{t-m+1, \ldots, t\} \rightarrow t+1$. The proof follows by contradiction, assuming that the score of $B^{\prime}$ is lower than $B$. The contradiction found is the following: the optimal branching algorithm applied to the intra-slice graph, Step 4 of Algorithm 1, outputs an optimal branching; moreover, all sets of parents with cardinality of at most $k$ consistent with the BFS order of the optimal branching and all sets of parents from the previous time slices with cardinality of at most $p$ are checked in the for-loop at Step 6. Therefore, the optimal set of parents is found for each node. Finally, note that the selected graph is acyclic since: (i) in the intra-slice network the graph is consistent with a total order (so no cycle can occur); and (ii) in the inter-slice network there are only dependencies from previous time slices to the present one (and not on the other way).

```
Algorithm 2 Compute all the weights \(e_{i j}\)
    for all nodes \(X_{i}[t+1]\) do
        Let \(s_{i}=-\infty\).
        for \(\mathbf{X}_{p s}[t-m+1: t] \in \mathcal{P}_{\leq p}(\mathbf{X}[t-m+1: t])\) do
            if \(\phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t], D_{t-m+1}^{t+1}\right)>s_{i}\) then
                Let \(s_{i}=\phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t], D_{t-m+1}^{t+1}\right)\).
            end if
        end for
        for all nodes \(X_{j}[t+1] \neq X_{i}[t+1]\) do
            Let \(s_{i j}=-\infty\).
            for \(\mathbf{X}_{p s}[t-m+1: t] \in \mathcal{P}_{\leq p}(\mathbf{X}[t-m+1: t])\) do
                if \(\phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t] \cup\left\{X_{j}[t+1]\right\}, D_{t-m+1}^{t+1}\right)>s_{i j}\) then
                    Let \(s_{i j}=\phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t] \cup\left\{X_{j}[t+1]\right\}, D_{t-m+1}^{t+1}\right)\).
            end if
            end for
        end for
        Let \(e_{i j}=s_{i j}-s_{i}\).
    end for
```

```
Algorithm 3 Compute the set of parents of \(X_{i}[t+1]\)
    Let \(\max =-\infty\).
    for \(\mathbf{X}_{p s}[t-m+1: t] \in \mathcal{P}_{\leq p}(\mathbf{X}[t-m+1: t])\) do
        for \(\mathbf{X}_{p s}[t+1] \in \mathcal{P}_{\leq k}\left(\alpha_{i, t+1}^{B F S}\right)\) do
            if \(\phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t] \cup \mathbf{X}_{p s}[t+1], D_{t-m+1}^{t+1}\right)>\max\) then
                Let \(\max =\phi_{i}\left(\mathbf{X}_{p s}[t-m+1: t] \cup \mathbf{X}_{p s}[t+1], D_{t-m+1}^{t+1}\right)\).
                Let the parents of \(X_{i}[t+1]\) be \(\mathbf{X}_{p s}[t-m+1: t] \cup \mathbf{X}_{p s}[t+1]\).
            end if
        end for
    end for
```

Theorem 2. Algorithm 1 takes time

$$
\max \left\{\mathcal{O}\left(n^{p+3}(m+1)^{3} m^{p} r^{p+2} N(T-m+1)\right), \mathcal{O}\left(n^{p+k+2} m^{p}(m+1) r^{p+k+1} N(T-m+1)\right)\right\}
$$

given a decomposable scoring function $\phi$, a Markov lag $m$, a set of $n$ random variables, a bounded in-degree of each intra-slice transition network of $k$, a bounded in-degree of each inter-slice transition network of $p$ and a set of observations of $N$ individuals over $T$ time steps.

Proof. For each time transition $\{t-m+1, \ldots, t\} \rightarrow t+1$, in order to compute all weights $e_{i j}$ (Algorithm 2), it is necessary to iterate over all the edges, that takes time $\mathcal{O}\left((n(m+1))^{2}\right)$. The number of subsets of parents from the preceding time slices with at most $p$ elements is given by:

$$
\left|\mathcal{P}_{\leq p}(\mathbf{X}[t])\right|=\sum_{i=0}^{p}\binom{n m}{i}<\sum_{i=0}^{p}(n m)^{i} \in \mathcal{O}\left((n m)^{p}\right)
$$

Calculating the score of each parent set (Step 11 of Algorithm 2), considering that the maximum number of states a variable may take is $r$, and that each variable has at most $p+1$ parents ( $p$ from the past and 1 in $t+1$ ), the number of possible configurations is given by $r^{p+2}$. The score of each configuration is computed over the set of observations $D_{t-m+1}^{t+1}$, therefore taking $\mathcal{O}\left((m+1) r^{p+2} n N\right)$. Applying Edmond's optimal branching algorithm to the intra-slice network and computing its BFS order, in Steps 4 and 5, takes $\mathcal{O}\left(n^{2}\right)$ time. Hence, Steps 1-5 take time $\mathcal{O}\left(n^{p+3}(m+1)^{3} m^{p} r^{p+2} N\right)$. Step 6 iterates over all nodes in time slice $t+1$, therefore iterates $\mathcal{O}(n)$ times. In Algorithm 3, Step 7, the number of subsets with at most $p$ elements from the past and $k$ elements from the present is upper bounded by $\mathcal{O}\left((n m)^{p} n^{k}\right)$. Computing the score of each configuration takes time complexity of $\mathcal{O}\left((m+1) n r^{p+k+1} N\right)$. Therefore Steps 6-9 take time complexity of $\mathcal{O}\left(n^{p+k+2} m^{p}(m+1) r^{p+k+1} N\right)$. Algorithm 1 ranges over all $T-m+1$ time transitions, hence, takes time $\max \left\{\mathcal{O}\left(n^{p+3}(m+1)^{3} m^{p} r^{p+2} N(T-m+1)\right), \mathcal{O}\left(\left(n^{p+k+2} m^{p}(m+1) r^{p+k+1} N(T-m+1)\right)\right\}$.

Theorem 3. There are at least $2^{\left(n k-\frac{k^{2}}{2}-\frac{k}{2}-1\right)(T-m+1)}$ non-tDBN transition networks in the set of bcDBN structures, where $n$ is the number of variables, $T$ is the number of time steps considered, $m$ is the Markov lag and $k$ is the maximum intra-slice in-degree considered.

Proof. Consider without loss of generality the time transition $\{t-m+1, \ldots, t\} \rightarrow t+1$ and the optimal branching in $t+1, R_{t+1}$. Let $\left(V, \subseteq_{B F S}\right)$ be the total order induced by the BFS over $R_{t+1}$. For any two nodes $X_{i}[t+1]$ and $X_{j}[t+1]$, with $i \neq j$, we say that node $X_{i}[t+1]$ is lower than $X_{j}[t+1]$ if $X_{i}[t+1] \subseteq_{B F S} X_{j}[t+1]$. The $i$-th node of $R_{t+1}$ has precisely $i-1$ lower nodes. When $i>k$, there are at least $2^{k}$ subsets of $V$ with at most $k$ lower nodes. When $i \leq k$, only $2^{i-1}$ subsets of $V$ with at most $k$ lower nodes exist. Therefore, there are at least

$$
\left(\prod_{i=k+1}^{n} 2^{k}\right) \times\left(\prod_{i=1}^{k} 2^{i-1}\right)=2^{n k-\frac{k^{2}}{2}-\frac{k}{2}}
$$

BFS-consistent $k$-graphs.
Let $X_{R}$ be the root of $R_{t+1}$ and $X_{j}$ its child node. Let $\varnothing$ denote the empty set. $X_{R}$ and $\varnothing$ are the only possible ancestors of $X_{j}$. If $\varnothing$ is the optimal one, then the resultant graph will not be a tree-augmented network. Therefore there are at least

$$
2^{n k-\frac{k^{2}}{2}-\frac{k}{2}-1}
$$

non-tree-augmented graphs in the set of BFS-consistent $k$-graphs.
There are $T-m+1$ transition networks, hence, there are at least $2^{\left(n k-\frac{k^{2}}{2}-\frac{k}{2}-1\right)(T-m+1)}$ non-tDBN network structures in the set of bcDBN network structures.

# 6. Experimental Results 

We assess the merits of the proposed algorithm comparing it with one state-of-the-art DBN learning algorithm, tDBN [13]. Our algorithm was implemented in Java using an object-oriented paradigm

and was released under a free software license (https://margaridanarsousa.github.io/learn_cDBN/). The experiments were run on an Intel ${ }^{\circledR}$ Core $^{\mathrm{TM}}$ i5-3320M CPU @ $2.60 \mathrm{GHz} \times 4$ machine.

We analyze the performance of the proposed algorithm for synthetic data generated from stationary first-order Markov bcDBNs. Five bcDBN structures were determined, parameters were generated arbitrarily, and observations were sampled from the networks, for a given number of observations $N$. The parameters $p$ and $k$ were taken to be the maximum in-degree of the inter and intra-slice network, respectively, of the transition network considered.

In detail, the five first-order Markov stationary transition networks considered were:

- one intra-slice complete bcDBN network with $k=2$ and at most $p=2$ parents from the previous time slice (Figure 5a);
- one incomplete bcDBN network, such that each node in $t+1$ has a random number of inter-slice $(p=2)$ and intra-slice $(k=2)$ parents between 0 and $p+k \leq 4$ (Figure 5b);
- two incomplete intra-slice bcDBN network $(k=3)$ such that each node has at most $p=2$ parents from the previous time slice (Figure 5c,e);
- one tDBN $(k=1)$, such that each node has at most $p=2$ parents from the previous time slice (Figure 5d).

The tDBN and bcDBN algorithms were applied to the resultant data sets, and the ability to learn and recover the original network structure was measured. We compared the original and recovered networks using the precision, recall and $F_{1}$ metrics:

$$
\text { precision }=\frac{T P}{T P+F P}, \text { recall }=\frac{T P}{T P+F N} \text { and } F_{1}=2 \times \frac{\text { precision } \times \text { recall }}{\text { precision }+ \text { recall }}
$$

where $T P$ are the true positive edges, $F P$ are the false positive edges and $F N$ are the false negative edges.
The results are depicted in Table 1 and the presented values are annotated with a $95 \%$ confidence interval, over five trials. The tDBN+LL and tDBN+MDL denote, respectively, the tDBN learning algorithm with LL and MDL criteria. Similarly, the bcDBN+LL and bcDBN+MDL denote, respectively, the bcDBN learning algorithm with LL and MDL scoring functions.

Considering Network 1, the tDBN recovers a significantly lower number of edges, giving raise to lower recalls and similar precisions, when comparing with bcDBN for LL and MDL. The bcDBN+LL and bcDBN+MDL have similar performances. For $N=2000$, bcDBN+LL and bcDBN+MDL are able to recover in average $99 \%$ of the total number of edges.

For Networks 2 and 5, considering incomplete networks, the tDBN has again lower recalls and similar precisions than bcDBN. However, in this case, the bcDBN+MDL clearly outperforms bcDBN+LL for all number of instances $N$ considered.

Moreover, in Network 5, taking a maximum intra-slice in-degree $k=3$, bcDBN only recovers $84 \%$ of the total number of edges, for $N=2000$. These results suggest that a considerable number of observations are necessary to fully reconstruct the complex BFS-consistent $k$-structures.

Curiously, the bcDBN+MDL algorithm has better results considering a complete tree-augmented initial structure (Network 4), with higher precision scores and similar recall, comparing with tDBN+MDL.

For both algorithms, in general, the LL gives raise to better results, when considering a complete network structure and a lower number of instances, whereas taking an incomplete network structure and a higher number of instances, the MDL outperforms LL. The complexity penalization term of MDL prevents the algorithms of choosing false positive edges and gives raise to higher precision scores. The LL selects more complex structures, such that each node has exactly $p+k$ parents.

We stress that in all settings considered both algorithms improve their performance when increasing the number of observations $N$. In order to understand the number of instances $N$ needed to fully recover the initial transition network, we designed two new experiments where five samples where generated from the first-order Markov transition networks depicted in Figure 6.

![img-4.jpeg](img-4.jpeg)
(a) Network 1 (bcDBN with $p=k=2$ ).
![img-5.jpeg](img-5.jpeg)
(c) Network 3 (bcDBN with $p=2$ and $k=3$ ).
![img-6.jpeg](img-6.jpeg)
(b) Network 2 (bcDBN with $p=k=2$ ).
![img-7.jpeg](img-7.jpeg)
(d) Network 4 (tDBN with $p=2$ ).
![img-8.jpeg](img-8.jpeg)
(e) Network 5 (bcDBN with $p=2$ and $k=3$ ).

Figure 5. First-order Markov stationary transition networks considered in the experiments.

Table 1. Comparative structure recovery results for tDBN and bcDBN on simulated data. For each network, $n$ is the number of network attributes, $p$ is the maximum inter-slice in-degree, $k$ is the maximum intra-slice in-degree, and $r$ is the number of states of all attributes. On the left, $N$ is the number of observations. Precision (Pre.), recall (Rec.) and $F_{1}$-measure $\left(F_{1}\right)$ values are presented as percentages, running time is in seconds.


![img-9.jpeg](img-9.jpeg) (a) Network 6 (bcDBN with $p=1$ and $k=2$ ). Figure 6. Two additional transition networks to test structure recovery in terms of number of observations $N$.

The number of observations needed for the bcDBN+MDL to recover the aforementioned networks are $1120.0 \pm 478.18$ (Figure 6a) and $2900.0 \pm 1134.77$ (Figure 6b), with a $95 \%$ confidence interval, where the five trials were done for each network. When increasing $k$, the number of necessary observations to totally recover the initial structure increases significantly.

When considering more complex BFS-consistent $k$-structures, the bcDBN algorithm achieved consistently significantly higher $F_{1}$ measures than tDBN. As expected, bcDBN+LL obtained better results for complete structures, whereas bcDBN+MDL achieved better results for incomplete structures.

# 7. Conclusions 

The bcDBN learning algorithm has polynomial-time complexity with respect to the number of attributes and can be applied to stationary and non-stationary Markov processes. The proposed algorithm increases the search space exponentially, in the number of attributes, comparing with the state-of-the-art tDBN algorithm. When considering more complex structures, the bcDBN is a good alternative to the tDBN. Although a higher number of observations are necessary to fully recover the transition network structure, bcDBN is able to recover a significantly larger number of dependencies and surpasses, in all experiments, the tDBN algorithm in terms of $F_{1}$-measure.

A possible line of future research is to consider hidden variables and incorporate a structural Expectation-Maximization procedure in order to generalize hidden Markov models. Another possible path to follow is to consider mixtures of bcDBNs, both for classification and clustering.

Acknowledgments: This work was supported by national funds through FCT, Fundação para a Ciência e a Tecnologia, under contract IT (UID/EEA/50008/2013), and by projects PERSEIDS (PTDC/EMS-SIS/0642/2014), NEUROCLINOMICS2 (PTDC/EEI-SII/1937/2014), and internal IT projects QBigData and RAPID.
Author Contributions: Alexandra M. Carvalho and Margarida Sousa conceived the proposed algorithm and wrote the paper; Margarida Sousa performed the experimental results.
Conflicts of Interest: The authors declare no conflict of interest.
