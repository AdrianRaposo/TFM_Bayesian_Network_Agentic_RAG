# Reconstructing Bayesian Networks on a Quantum Annealer 

Enrico Zardini ${ }^{* \dagger}$, Massimo Rizzoli ${ }^{*}$, Sebastiano Dissegna*, Enrico Blanzieri ${ }^{* \ddagger}$, Davide Pastorello ${ }^{* \ddagger}$<br>* Department of Information Engineering and Computer Science<br>University of Trento<br>via Sommarive 9, 38123 Povo, Trento, Italy<br>${ }^{\dagger}$ enrico.zardini@unitn.it<br>${ }^{\ddagger}$ Trento Institute for Fundamental Physics and Applications<br>via Sommarive 14, 38123 Povo, Trento, Italy


#### Abstract

Bayesian networks are widely used probabilistic graphical models, whose structure is hard to learn starting from the generated data. O'Gorman et al. have proposed an algorithm to encode this task, i.e., the Bayesian network structure learning (BSNL), into a form that can be solved through quantum annealing, but they have not provided an experimental evaluation of it. In this paper, we present (i) an implementation in Python of O'Gorman's algorithm, (ii) a divide et impera approach that allows addressing BNSL problems of larger sizes in order to overcome the limitations imposed by the current architectures, and (iii) their empirical evaluation. Specifically, several problems with an increasing number of variables have been used in the experiments. The results have shown the effectiveness of O'Gorman's formulation for BNSL instances of small sizes, and the superiority of the divide et impera approach on the direct execution of O'Gorman's algorithm.


Keywords: Bayesian Network Structure Learning, Quantum Annealing, Quantum Software, Empirical Evaluation

## 1 Introduction

Bayesian networks (BNs) are graphical probabilistic models in which the joint density distribution of multiple random variables is represented over a directed acyclic graph [1]. In detail, each variable corresponds to a node of the graph, and the overall joint density distribution is obtained by multiplying the conditional density distribution of each variable given its parents on the graph. As a consequence, the topology of the graph defines the independence conditions, i.e., a variable is independent of its non-descendants given its parents. BNs are widely used for representing uncertain domains and their structure allows for probabilistic reasoning. Obtaining a BN representation from data is a learning task with a long history; in particular, the subtask of learning the topology, also known as BN reconstruction, has received much attention [2], especially when BNs are used to represent causal relationships [3]. Moreover, some recent papers have dealt with the possible application of quantum computing to Bayesian networks [4, 5, 6].

Quantum computing (QC) is a kind of computation that exploits quantum mechanical phenomena for information processing, and, nowadays, working quantum computers are available on the market [7]. QC will have an impact on artificial intelligence and machine learning. Indeed, it

has the potentiality to allow efficient solutions to many of the search and optimization problems encountered in these fields. In the last years, some applications of quantum computing to Bayesian networks have been proposed, such as the following: a method for learning the structure of a BN using a quantum annealer 4]; an algorithm for Bayesian inference based on amplitude amplification, which is a quantum version of the classical rejection sampling algorithm used for inference in Bayesian networks [5]; a systematic method for designing a quantum circuit to represent a generic discrete BN [6]. In particular, the proposal of O'Gorman et al. [4] considers a quantum annealing architecture instead of a gate-based quantum computer. Quantum annealing is a type of heuristic search for solving optimization problems by finding the low-energy states of a quantum system [8], and quantum annealers are non-universal specific-purpose quantum computers implementing quantum annealing. The advantage of the existing quantum annealers lies in the high number of qubits w.r.t. the available prototypes of general-purpose quantum computers. The paper by O'Gorman et al. describes an effective encoding of the BN reconstruction problem into a quantum annealer architecture. However, no implementation and empirical evaluation on a real quantum machine are provided.

In this paper, we present an empirical evaluation of the proposal of O'Gorman et al. in order to assess its practical applicability using the available architectures. Since the problem encoding and the subsequent embedding in the quantum architecture limit the direct application to around 18 Bayesian variables (at time of writing), we also propose a divide-et-impera approach to overcome this limitation. Both the original algorithm and the new scheme have been tested on different problems with a growing number of variables. The code is available under the GPLv2 licence [9, 10].

The paper is organized as follows: Section 2 provides some background information; Section 3 describes the implementation of O'Gorman's algorithm [4]; Section 4 presents the so-called divide et impera approach; Section 5 is devoted to the empirical evaluation; Section 6 contains the concluding remarks.

# 2 Background 

This section provides information about QUBO problems, quantum annealing and D-Wave, the embedding into quantum processing units (QPUs), the Bayesian network structure learning problem, and O'Gorman's QUBO algorithm [4] to address it.

### 2.1 QUBO problems

Quadratic Unconstrained Binary Optimization (QUBO) problems are optimization problems of the form

$$
\arg \min _{x} x^{T} Q x
$$

where $x$ is a binary vector, and $Q$ is an upper triangular (or symmetric) matrix of real values. In particular, let $x$ be an $n \times 1$ vector and $Q$ a $n \times n$ upper triangular matrix; then, it is possible to rewrite the QUBO problem as follows:

$$
\begin{aligned}
x^{T} Q x & =\sum_{i=1}^{n} q_{i i} x_{i}^{2}+\sum_{i=1}^{n} \sum_{j=i+1}^{n} q_{i j} x_{i} x_{j} \\
& =\sum_{i=1}^{n} q_{i i} x_{i}+\sum_{i=1}^{n} \sum_{j=i+1}^{n} q_{i j} x_{i} x_{j}
\end{aligned}
$$

where $x_{i}^{2}=x_{i}$ since $x_{i} \in \mathbb{B}=\{0,1\}$. In practice, the main diagonal of $Q$ contains the linear coefficients $\left(q_{i i}\right)$, whereas the rest of the matrix contains the quadratic ones $\left(q_{i j}\right)$. Although QUBO

problems are unconstrained by definition, it is actually possible to introduce constraints by representing them as penalties. Several examples are provided by Glover et al. 11].

The significance of the QUBO formulation mainly lies in its computational equivalence with the Ising model, which is the physical model upon which annealers are built. The only difference is the domain of variables: $\{0,1\}$ for the QUBO formulation, $\{-1,+1\}$ for the Ising one. Hence, by applying a trivial conversion, it is possible to exploit quantum annealers to solve problems expressed as QUBO.

# 2.2 Quantum annealing and D-Wave machine 

Quantum annealing (QA) is a heuristic search used to solve optimization problems 8. The solution of a given problem corresponds to the ground state (the less energetic physical state) of a $n$-qubit system with energy described by a problem Hamiltonian $H_{P}$, which is a Hermitian $2^{n} \times 2^{n}$ matrix. The annealing procedure is implemented by a time evolution of the quantum system towards the ground state of the problem Hamiltonian. More precisely, let us consider the time-dependent Hamiltonian

$$
H(t)=\Gamma(t) H_{D}+H_{P}
$$

where $H_{P}$ is the problem Hamiltonian, and $H_{D}$ is the transverse field Hamiltonian, which gives the kinetic term inducing the exploration of the solution landscape by means of quantum fluctuations. $\Gamma$ is a decreasing function that attenuates the kinetic term, driving the system towards the global minimum of the problem landscape represented by $H_{P}$.

QA can be physically realized by considering a quantum spin glass, which is a network of qubits arranged on the vertices of a graph $\langle V, E\rangle$, with $|V|=n$ and whose edges $E$ represent the couplings among the qubits. The problem Hamiltonian is defined as

$$
H_{P}=H(\boldsymbol{\Theta})=\sum_{i \in V} \theta_{i} \sigma_{z}^{(i)}+\sum_{(i, j) \in E} \theta_{i j} \sigma_{z}^{(i)} \sigma_{z}^{(j)}
$$

where the real coefficients $\theta_{i}, \theta_{i j}$ are arranged into the matrix $\boldsymbol{\Theta} . H(\boldsymbol{\Theta})$ is an operator on the $n$-qubit Hilbert space $\mathrm{H}=\left(\mathbb{C}^{2}\right)^{\otimes n}$, whereas $\sigma_{z}^{(i)}$ acts as the Pauli matrix

$$
\sigma_{z}=\left(\begin{array}{cc}
1 & 0 \\
0 & -1
\end{array}\right)
$$

on the $i$ th tensor factor and as the $2 \times 2$ identity matrix on the other tensor factors. Regarding the coefficient matrix $\boldsymbol{\Theta}$, it is the $n \times n$ symmetric square matrix of real coefficients of E (called weights) defined as

$$
\boldsymbol{\Theta}_{i j}:= \begin{cases}\theta_{i}, & i=j \\ \theta_{i j}, & (i, j) \in E \\ 0, & (i, j) \notin E\end{cases}
$$

with $\theta_{i}$ physically corresponding to the local field on the $i$ th qubit, and $\theta_{i j}$ to the coupling between the qubits $i$ and $j$. In particular, the Pauli matrix $\sigma_{z}$ has two eigenvalues $\{-1,1\}$, which correspond to the binary states, spin down and spin up, of each qubit. Thus, the spectrum of eigenvalues of the problem Hamiltonian (Eq. (4) is the set of all possible values of the cost function given by the energy of the well-known Ising model:

$$
\mathrm{E}(\boldsymbol{\Theta}, \boldsymbol{z})=\sum_{i \in V} \theta_{i} z_{i}+\sum_{(i, j) \in E} \theta_{i j} z_{i} z_{j}, \quad \boldsymbol{z}=\left(z_{1}, \ldots, z_{n}\right) \in\{-1,1\}^{|V|}
$$

In practice, the annealing procedure, also called cooling, drives the system into the ground state of $H(\Theta)$, which corresponds to the spin configuration encoding the solution:

$$
\boldsymbol{z}^{*}=\underset{\boldsymbol{z} \in\{-1,1\}^{|V|}}{\arg \min } \mathrm{E}(\boldsymbol{\Theta}, \boldsymbol{z})
$$

Given a problem, the annealer is initialized using a suitable choice of the weights $\boldsymbol{\Theta}$, and the binary variables $z_{i} \in\{-1,1\}$ are physically realized by the outcomes of the measurements performed on the qubits located in the vertices $V$. In order to solve a general optimization problem through QA, it is first necessary to find an encoding of the objective function in terms of the cost function (7), which is not easy in general.

D-Wave Systems is a Canadian company producing quantum annealers, i.e., physical machines implementing the quantum annealing process. Currently, the available models are the D-Wave 2000Q, exploiting the Chimera topology, and the D-Wave Advantage, featuring the Pegasus topology. The former has 2048 qubits, each connected to 6 other qubits, whereas the latter has 5640 qubits, each connected to 15 other qubits. A higher amount of qubits allows for larger problems to be submitted, but the most relevant feature is the connectivity, which determines the complexity of the representable problems. For these reasons, the D-Wave Advantage has been chosen for the experiments.

# 2.3 Quantum processing unit (QPU) embedding 

To practically use quantum annealing for solving QUBO problems, the problem variables must be mapped to the QPU qubits. However, due to the sparseness of the available annealer topologies, a direct representation of the problem is typically not possible. The solution consists in chaining together multiple physical qubits that will act as a single logical qubit. In this way, the connectivity of the annealer graph is increased at the price of reducing the number of logical qubits available and, consequently, the size of representable problems. The entire process is known as embedding or minor embedding (in the glossary of D-Wave) [12, 13]. In particular, D-Wave's Ocean library provides the EmbeddingComposite class [14] to automatically perform the minor embedding of the supplied QUBO matrices, and a new embedding is computed for every annealer read.

### 2.4 Bayesian network structure learning (BSNL)

A Bayesian network (BN) is a directed acyclic graph (DAG) representing the conditional dependencies of a set of random variables. In particular, the nodes of the graph represent the variables, whereas the edges represent the conditional dependencies between them. Moreover, each node is associated with the conditional probability distribution of the node itself given its parents.

The method proposed by O'Gorman et al. [4] focuses on the network structure learning (BNSL) problem, which consists in finding the Bayesian network that most likely has generated a given set of data. The problem is NP-Complete [15], and the authors expect a polynomial speedup using quantum annealing. In detail, to take advantage of the new technology, a hardware compatible QUBO formulation of the BNSL problem is provided in the paper together with sufficient lower bounds for the penalties.

More formally, a Bayesian network can be defined as a pair $\left(B_{s}, B_{p}\right)$, where $B_{s}$ is a DAG and $B_{p}$ is the set of associated conditional probabilities. Then, given a database $D=\left\{\mathbf{x}_{i} \mid 1 \leq i \leq N\right\}$ with $\mathbf{x}_{i}$ representing the state of all variables, the objective consists in finding the structure that maximises the posterior probability distribution $p\left(B_{s} \mid D\right)$. However, due to the proportionality of $p\left(B_{s} \mid D\right)$ and $p\left(D \mid B_{s}\right)$ by Bayes' Theorem, it is possible to reformulate the problem as maximizing $p\left(D \mid B_{s}\right)$, which is given by

$$
p\left(D \mid B_{s}\right)=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\Gamma\left(\alpha_{i j}\right)}{\Gamma\left(N_{i j}+\alpha_{i j}\right)} \prod_{k=1}^{r_{i}} \frac{\Gamma\left(N_{i j k}+\alpha_{i j k}\right)}{\Gamma\left(\alpha_{i j k}\right)}
$$

where $\Gamma$ is the gamma function, $q_{i}$ is the number of joint states of the parent set of the $i$-th random variable, $r_{i}$ is the number of states of the random variable itself, $N_{i j k}$ is the number of occurrences in $D$ with the $i$-th random variable in its $k$-th state and the variable's parent set in its $j$-th state, $\alpha_{i j k}$ is the hyperparameter of the assumed Dirichlet prior for the node's conditional probability distribution, $N_{i j}$ and $\alpha_{i j}$ are the sums of the corresponding parameter values over $k$.

# 2.4.1 QUBO formulation of BNSL 

In their work [4], O'Gorman et al. provide a Hamiltonian function for the BNSL problem. Given the BNSL Hamiltonian, the construction of the QUBO matrix is straightforward: it is sufficient to map the coefficients of the variables into the matrix entries. In particular, the BNSL Hamiltonian consists of three components: the score Hamiltonian $\left(H_{\text {score }}\right)$, which is responsible for evaluating the quality of the solution graph; the max Hamiltonian $\left(H_{\max }\right)$, which is in charge of penalising the solutions including nodes with a number of parents greater than $m$, a constraint dictated by resource limits; the cycle Hamiltonian $\left(H_{\text {cycle }}\right)$, further divided in consistency Hamiltonian $\left(H_{\text {consist }}\right)$ and transitivity Hamiltonian $\left(H_{\text {trans }}\right)$, which penalises the solutions containing cycles. Hence, the full Hamiltonian $(H)$ is given by

$$
H(\mathbf{d}, \mathbf{y}, \mathbf{r})=H_{\text {score }}(\mathbf{d})+H_{\max }(\mathbf{d}, \mathbf{y})+H_{\text {cycle }}(\mathbf{d}, \mathbf{r})
$$

where $\mathbf{d}$ corresponds to the $n(n-1)$ bits used to represent the presence/absence of edges between nodes, whereas $\mathbf{y}$ and $\mathbf{r}$ are additional variables exploited to encode the constraints.

## Score Hamiltonian

The score Hamiltonian $\left(H_{\text {score }}\right)$ is calculated separately for each variable, and the components are then summed together. In detail, the score Hamiltonian for the $i$-th variable is given by

$$
H_{\text {score }}^{(i)}\left(\mathbf{d}_{i}\right)=\sum_{\substack{J \subset\{1 . . n\} \backslash\{i\} \\|J| \leq m}}\left(w_{i}(J) \prod_{j \in J} d_{j i}\right)
$$

where $\mathbf{d}_{i}$ includes all the bits $\left(d_{j i}\right)$ encoding edges towards the considered node, $m$ is the largest allowed size for the parent set, and $w_{i}$ is computed as follows:

$$
w_{i}(J)=\sum_{l=0}^{|J|}(-1)^{|J|-l} \sum_{\substack{K \subset J \\|K|=l}} s_{i}(K)
$$

with $s_{i}$ being score values obtained from Eq. (9), introducing a logarithm for numerical efficiency. Specifically, $s_{i}$ is given by

$$
s_{i}\left(\Pi_{i}\left(B_{s}\right)\right)=-\log \left(\prod_{j=1}^{y_{i}} \frac{\Gamma\left(\alpha_{i j}\right)}{\Gamma\left(N_{i j}+\alpha_{i j}\right)} \prod_{k=1}^{r_{i}} \frac{\Gamma\left(N_{i j k}+\alpha_{i j k}\right)}{\Gamma\left(\alpha_{i j k}\right)}\right)
$$

where $\Pi_{i}\left(B_{s}\right)$ denotes the parent set of the $i$-th node. In practice, the sum of the $s_{i}$ values is equal to $-\log p\left(D \mid B_{s}\right)$.

## Max Hamiltonian

Analogously to the score Hamiltonian, the max Hamiltonian is computed separately for each variable as

$$
H_{\max }^{(i)}\left(\mathbf{d}_{i}, \mathbf{y}_{i}\right)=\delta_{\max }^{(i)}\left(m-d_{i}-y_{i}\right)^{2}
$$

where $\delta_{\text {max }}^{(i)}>0$ is the penalty weight, $d_{i}$ is the in-degree of the considered node (given by $\sum_{1 \leq j \leq n \cap j \neq i} d_{j i}$ ), and $y_{i} \in \mathbb{Z}$ is a slack variable (encoded via binary expansion in $\mathbf{y}_{i}$ using $\mu$ bits ${ }^{\mathrm{a}}$ ) that allows $H_{\text {max }}^{(i)}$ being zero when the constraint is satisfied. Indeed, $H_{\text {max }}^{(i)}$ is zero if the considered node has at most $m$ parents, otherwise it carries a positive penalty.

# Cycle Hamiltonian 

As mentioned previously, the cycle Hamiltonian is defined as the sum of two components:

$$
H_{\text {cycle }}(\mathbf{d}, \mathbf{r})=H_{\text {trans }}(\mathbf{r})+H_{\text {consist }}(\mathbf{d}, \mathbf{r})
$$

where $\mathbf{r}$ represents $n(n-1) / 2$ additional boolean variables encoding a topological order ( $r_{i j}$ is 1 if the $i$-th node precedes the $j$-th one, 0 otherwise). In detail, the transitivity Hamiltonian penalises the cycles of length three in the $r_{i j}$ values, and is computed separately for each possible 3 -set of variables as

$$
H_{\text {trans }}^{(i j k)}\left(r_{i j}, r_{j k}, r_{i k}\right)=\delta_{\text {trans }}^{(i j k)}\left(r_{i k}+r_{i j} r_{j k}-r_{i j} r_{i k}-r_{j k} r_{i k}\right)
$$

where $\delta_{\text {trans }}^{(i j k)}$ is the positive penalty added if the $i$-th, $j$-th and $k$-th variables form a 3 -cycle. As in the previous cases, the $H_{\text {trans }}^{(i j k)}$ components are summed up to obtain the full $H_{\text {trans }}$. Instead, the consistency Hamiltonian penalises the solutions for which the topological order contained in $\mathbf{r}$ is inconsistent with the graph structure encoded in $\mathbf{d}$. In practice, it makes disadvantageous the solutions in which $r_{i j}=1$ and $d_{j i}=1$, or $r_{i j}=0$ and $d_{i j}=1$. The Hamiltonian is computed separately for each pair of variables as

$$
H_{\text {consist }}^{(i j)}\left(d_{i j}, d_{j i}, r_{i j}\right)=\delta_{\text {consist }}^{(i j)}\left(d_{j i} r_{i j}+d_{i j}-d_{i j} r_{i j}\right)
$$

where $\delta_{\text {consist }}^{(i j)}$ is the positive penalty associated with the inconsistency. It is also worth highlighting that the penalties $\delta_{\text {trans }}^{(i j k)}$ and $\delta_{\text {consist }}^{(i j)}$ are invariant to the permutation of the superscript indices (the set of variables remains the same).

### 2.4.2 QUBO size and penalty values

The QUBO formulation of the BNSL problem consist of $n(n-1)$ binary variables $\left(d_{i j}\right)$ encoding the graph structure, $n \mu=n\left\lceil\log _{2}(m+1)\right\rceil$ binary slack variables $\left(y_{i l}\right)$ related to the maximum parent constraint, and $n(n-1) / 2$ binary variables $\left(r_{i j}\right)$ encoding a topological order (related to the absence of cycles constraint). Hence, the QUBO encoding of $n$ Bayesian variables requires $\mathcal{O}\left(n^{2}\right)$ binary variables. Nevertheless, since $H_{\text {score }}$ contains multiplications with $m$ factors, if $m \geq 3$, additional steps and slack variables are needed to convert the problem into a quadratic equation. For instance, according to O'Gorman et al., $n\left\lfloor\frac{(n-2)^{2}}{4}\right\rfloor$ binary slack variables are needed to reduce a BNSL problem with $m=3$ to a quadratic form, increasing the total number of binary variables to $\mathcal{O}\left(n^{3}\right)$. In this work, only the formulation for $m=2$ has been used in the experiments, although some problems taken into account have more than two parents per node.

Concerning the penalty values, O'Gorman et al. provide the following lower bounds (they have also demonstrated their sufficiency):

$$
\begin{gathered}
\delta_{\max }^{\left(i\right)}>\max _{j \neq i} \Delta_{j i}, 1 \leq i \leq n \\
\delta_{\text {consist }}^{(i j)}>(n-2) \max _{k \notin\{i, j\}} \delta_{\text {trans }}^{(i j k)}, 1 \leq i<j \leq n
\end{gathered}
$$

[^0]
[^0]:    ${ }^{\mathrm{a}} y_{i}=\sum_{l=1}^{\mu} 2^{l-1} y_{i l}$, with $\mu=\left\lceil\log _{2}(m+1)\right\rceil$

$$
\delta_{\text {trans }}^{(i j k)}=\delta_{\text {trans }}>\max _{\substack{1 \leq i^{\prime}, j^{\prime} \leq n \\ i^{\prime} \neq j^{\prime}}} \Delta_{i^{\prime} j^{\prime}}, 1 \leq i<j<k \leq n
$$

where $\Delta_{j i}$ is an estimate of the largest increase in score due to the insertion of an arc from the $j$-th to the $i$-th node. In the case of $m=2$, it is given by

$$
\begin{gathered}
\Delta_{j i}=\max \left\{0, \Delta_{j i}^{\prime}\right\} \\
\Delta_{j i}^{\prime}=-w_{i}(\{j\})-\sum_{\substack{1 \leq k \leq n \\
k \neq i, j}} \min \left\{0, w_{i}(\{j, k\})\right\}
\end{gathered}
$$

Instead, for $m \geq 3$, computing $\Delta_{j i}$ becomes an intractable optimization problem.

# 3 O'Gorman's Algorithm Implementation 

A Python implementation of O'Gorman's algorithm, which provides a way to build the QUBO matrix for a BNSL problem, has been developed in this work. Since the D-Wave's Ocean suite, which is necessary for interacting with the quantum annealer, is implemented in Python, the programming language in question has turned out to be the most reasonable choice. This section provides the implementation details, some considerations about the complexity of the implementation, and the description of a method to speed up the execution.

```
Input: number of Bayesian variables \(n\), list \(r=\left(r_{i}\right)_{i=1}^{n}\) with \(r_{i}\) being the number of states of the \(i^{t h}\)
    variable, dataset examples
Result: QUBO matrix \(Q\)
    // calculation of the values needed to construct \(Q\)
    1 parentSets \(\leftarrow\) calcParentSets \((n)\);
    \(2 \alpha \leftarrow\) calcAlpha \((n, r\), parentSets \()\);
    \(3 s \leftarrow\) calcS \((n, r\), parentSets, \(\alpha\), examples \() ;\)
    \(4 w \leftarrow\) calcW \((n\), parentSets, \(s\) );
    \(5 \Delta \leftarrow\) calcDelta \((n\), parentSets, \(w)\);
    \(6 \delta_{\max } \leftarrow\) calcDeltaMax \((n, \Delta) ;\)
    \(7 \delta_{\text {trans }} \leftarrow\) calcDeltaTrans \((n, \Delta) ;\)
    \(8 \delta_{\text {consist }} \leftarrow\) calcDeltaConsist \(\left(n, \delta_{\text {trans }}\right) ;\)
    // construction of \(Q\)
    \(9 Q \leftarrow\) zeroMatrix( );
    \(10 Q \leftarrow\) fillQ \((Q, n\), parentSets, \(w, \delta_{\max }, \delta_{\text {trans }}, \delta_{\text {consist }}) ;\)
    11 return \(Q\);
```

```
// Algorithm 1: calcQUBOMatrix( \(n, r\), examples \()\)
```


### 3.1 QUBO matrix construction

The pseudocode of the implementation of O'Gorman's algorithm is shown in Algorithm 1, which includes calls to Algorithms 2-3-4. In particular, the main algorithm takes as input the number of Bayesian variables $n$, the number of states $r_{i}$ for each variable, and the dataset of examples, and produces as output the QUBO matrix $Q$ that represents the considered BNSL problem.

Before effectively building the matrix, it is necessary to compute several intermediate values. First, all possible parent sets $\left(\Pi_{i}\left(B_{s}\right)\right.$ in O'Gorman's formulation) are calculated for each Bayesian variable. The maximum number of parents $m$ has been set to two (for the reasons explained in Section 2.4.2) and, as a consequence, the complexity of this step turns out to be $\mathcal{O}\left(n^{3}\right)$. It is also worth noticing that the empty set is a valid parent set.

After that, the $\alpha_{i j k}$ hyperparameters of the Dirichlet priors are set to the uninformative value $1 /\left(r_{i} \cdot q_{i}\right)$, with $r_{i}$ being the number of states of the $i$-th variable and $q_{i}$ (denoted as $q_{i \pi}$ in the

pseudocode) being the number of states of the considered parent set. In practice, all $\alpha_{i j k}$ related to a specific variable $i$ and parent set $\pi$ (denoted as $\alpha_{i \pi j k}$ in the pseudocode) have the same value; further details about this choice are provided in Section 5.4. In this step, the $\alpha_{i j k}$ value for all possible "variable" - "parent set" - "parent set state" - "variable state" combinations must be generated; hence, the complexity is $\mathcal{O}\left(n^{3} r_{\max }^{3}\right)$, where $r_{\max }$ is the maximum number of states of the Bayesian variables.

The next step consists in computing the local scores $s$ for all possible "Bayesian variable" "parent set" combinations according to Eq. (13). Nevertheless, due to the factorial nature of the $\Gamma$ function and the presence of multiplications of $\Gamma$ values, the calculations turn out to be feasible only for very small datasets; indeed, the values quickly go out of range. The solution lies in moving the logarithm inside through algebraic steps until its argument becomes the gamma function alone. In the implementation presented here, the natural logarithm (ln) has been used, and the resulting formula, the one employed in Algorithm 2, is the following:

$$
s_{i}\left(\Pi_{i}\left(B_{s}\right)\right)=-\sum_{j=1}^{q_{i}}\left[\ln \left(\Gamma\left(\alpha_{i j}\right)\right)-\ln \left(\Gamma\left(N_{i j}+\alpha_{i j}\right)\right)+\sum_{k=1}^{r_{i}}\left[\ln \left(\Gamma\left(N_{i j k}+\alpha_{i j k}\right)\right)-\ln \left(\Gamma\left(\alpha_{i j k}\right)\right)\right]\right]
$$

This form allows exploiting the (natural) log-gamma function (denoted as $\ln \Gamma$ in the pseudocode) instead of the gamma one, a function characterised by a far slower growth. Moreover, by doing this, the products in Eq. (13) are replaced by additions, further decreasing the risk of out of range values. Concerning the pseudocode, the calcNi $\pi j k$ procedure just computes the number of times the variable $i$ is in its $k$-th state while its parent set $\pi$ is in its $j$-th state (in the case of an empty parent set, the state of the $i$-th variable alone is considered). The complexity of the algorithm is $\mathcal{O}\left(n^{3} N r_{\max }^{3}\right)$

Once the score values $s$ have been calculated, it is possible to compute the parent set weights $w$ for the score Hamiltonian according to (12). The pseudocode for this step is available in Algorithm 3. As previously mentioned, the maximum number of allowed parents has been set to two, hence the pseudocode does not take into account cases with larger parent sets. The complexity of
```
Input: number of Bayesian variables $n$, list of number of states $r$, list of parent sets parentSets, prior distributions hyperparameters $\alpha=\left(\alpha_{i \pi j k}\right)$, dataset examples
Result: $s=\left(\left\{s_{i}(\pi)\right.\right.$ s.t. $\left.\pi \in \operatorname{parentSets}[i]\right\})_{i=1}^{n}$ with $s_{i}(\pi)$ being the score for the Bayesian variable $i$ given the parent set $\pi$
1 function $\operatorname{calcSi}(i, \pi, r, \alpha$, examples $)$
// Eq. (23)
$q_{i \pi} \leftarrow \prod_{p \in \pi} r_{p} ; \quad / / q_{i \pi}=1$ if $\pi=\emptyset$
sum $\leftarrow 0 ;$
for $j \leftarrow 1$ to $q_{i \pi}$ do
$\alpha_{i \pi j} \leftarrow \sum_{k=1}^{r_{i}} \alpha_{i \pi j k} ;$
$N_{i \pi j} \leftarrow \sum_{k=1}^{r_{i}} \operatorname{calcNiz} j k\left(\right.$ examples, $\left.\pi, i, j, k, r\right) ;$
sum $\leftarrow \operatorname{sum}+\ln \Gamma\left(\alpha_{i \pi j}\right)-\ln \Gamma\left(\alpha_{i \pi j}+N_{i \pi j}\right) ;$
for $k \leftarrow 1$ to $r_{i}$ do
$N_{i \pi j k} \leftarrow \operatorname{calcNiz} j k\left(\right.$ examples, $\left.\pi, i, j, k, r\right) ;$
sum $\leftarrow \operatorname{sum}+\ln \Gamma\left(\alpha_{i \pi j k}+N_{i \pi j k}\right)-\ln \Gamma\left(\alpha_{i \pi j k}\right) ;$
end
end
return -sum;
for $i \leftarrow 1$ to $n$ do
for $\pi \in$ parentSets $[i]$ do
$s_{i}(\pi) \leftarrow \operatorname{calcSi}(i, \pi, r, \alpha$, examples $))$;
end
end
return $s$;
```
Algorithm 2: $\operatorname{calcS}(n, r$, parentSets, $\alpha$, examples $)$
```
Input: number of Bayesian variables $n$, list of parent sets parentSets, score values $s$
Result: $w=\left(\left\{w_{i}(\pi)\right.\right.$ s.t. $\left.\pi \in \operatorname{parentSets}[i]\right\})_{i=1}^{n}$ with $w_{i}(\pi)$ being the weight calculated for the Bayesian variable $i$ given the parent set $\pi$
function $\operatorname{calc} W i(i, \pi, s)$ :
// Eq. (12)
if $\pi=\emptyset$ then
return $s_{i}(\emptyset)$;
else if $\operatorname{size}(\pi)=1$ then
return $s_{i}(\pi)-s_{i}(\emptyset)$
else if $\operatorname{size}(\pi)=2$ then
$p_{1}, p_{2} \leftarrow \pi[1], \pi[2] ;$
return $s_{i}(\pi)-s_{i}\left(\left\{p_{1}\right\}\right)-s_{i}\left(\left\{p_{2}\right\}\right)+s_{i}(\emptyset) ;$
end
for $i \leftarrow 1$ to $n$ do
for $\pi \in$ parentSets $[i]$ do
$w_{i}(\pi) \leftarrow \operatorname{calc} W i(i, \pi, s) ;$
end
end
return $w$;
```
Algorithm 3: $\operatorname{calc} W(n$, parentSets, $s)$
the algorithm for the computation of $w$ is $\mathcal{O}\left(n^{3}\right)$.
Eventually, the penalty values must be calculated, starting from the auxiliary quantities $\Delta$, which are computed according to Eq. (21) and (22) with a complexity of $\mathcal{O}\left(n^{4}\right)$; actually, this complexity derives from the data structure used in the code to store the parent sets (according to the formulas, the complexity would be $\mathcal{O}\left(n^{3}\right)$ ). Given $\Delta$, all penalties can be determined. In detail, $\delta_{\text {max }}^{(i)}$ is computed for each Bayesian variable according to (18) with a resulting complexity (for all $\delta_{\text {max }}^{(i)}$ ) of $\mathcal{O}\left(n^{2}\right)$. Instead, the penalty bound related to the consistency Hamiltonian (Eq. (19)) can be simplified due to independence of $\delta_{\text {trans }}$ from its superscript indices. The outcome is the following:

$$
\delta_{\text {consist }}>(n-2) \delta_{\text {trans }}
$$

In practice, $\delta_{\text {trans }}$ is computed according to Eq. (20) with complexity $\mathcal{O}\left(n^{2}\right)$ (notice that $\delta_{\text {trans }}$ is a single value). Then, $\delta_{\text {consist }}$ is calculated according to the simplified bound (Eq. (24)) with complexity $\mathcal{O}(1)$. In order to satisfy the lower bounds, the penalty values have been set to the boundary values plus one.

At this point, it is possible to fill the QUBO matrix $Q$ as shown in Algorithm 4; the matrix, whose size has been already described in Section 2.4.2, initially contains only zeros (see line 9 of Algorithm 1, whose complexity is $O\left(n^{4}\right)$ ). In detail, the first section of Algorithm 4 (lines 2-12) is related to the score Hamiltonian, namely, to Eq. (11). For each "Bayesian variable" - "parent set" combination, the parent set weight $w_{i}(\pi)\left(w_{i}(J)\right.$ in O'Gorman's formulation) is added to the appropriate cell; the outermost loop, which includes almost all the pseudocode, is the one iterating on the Bayesian variables. In practice, the coefficients of the linear terms of Eq. (11), i.e., the terms involving only one QUBO variable $\left(d_{j i}\right)$, are summed to cells of $Q$ located on the main diagonal. Instead, the coefficients of the quadratic terms, which involve two QUBO variables $\left(d_{x i} d_{y i}\right)$, contribute to cells outside the diagonal; indeed, the first variable determines the row, while the other the column. The subsequent part of the algorithm is related to the max Hamiltonian (lines 13-25), i.e., to Eq. (14). The approach used for the coefficient insertion is similar to that employed for the score Hamiltonian, however the presence of a square must be taken into account. Hence, for each Bayesian variable (outermost loop), the binary variables involved in Eq. (14) and their coefficients inside the square are determined and stored in two lists (lines 14-15). Then, based on the square expansion, the resulting linear and quadratic coefficients (which include the multiplication by $\delta_{\text {max }}^{(i)}$ ) are summed to the respective cells. Finally, there is the section related to the transitivity
```
Input: zero matrix $Q$, number of Bayesian variables $n$, list of parent sets parentSets, parent set weights $w$, list of penalty values $\delta_{\text {max }}$, penalty value $\delta_{\text {trans }}$, penalty value $\delta_{\text {consist }}$
Result: QUBO matrix $Q$ filled according to $H_{\text {score }}, H_{\text {max }}, H_{\text {trans }}$, and $H_{\text {consist }}$
for $i \leftarrow 1$ to $n$ do
/* $H_{\text {score }}$-related terms (Eq. (11)) */
for $\pi \in$ parentSets $[i]$ do
if size $(\pi)=1$ then
$j \leftarrow \pi[1]$
row $\leftarrow$ col $\leftarrow$ indexOf $\left(d_{j i}\right)$;
$Q[$ row $][\operatorname{col}] \leftarrow Q[$ row $][\operatorname{col}]+w_{i}(\pi)$
else if size $(\pi)=2$ then
$x, y \leftarrow \pi[1], \pi[2]$
row, col $\leftarrow$ indexOf $\left(d_{x i}\right)$, indexOf $\left(d_{y i}\right)$;
$Q[$ row $][\operatorname{col}] \leftarrow Q[$ row $][\operatorname{col}]+w_{i}(\pi)$
end
end
/* $H_{\text {max }}$-related terms (Eq. (14)) */
$m \leftarrow 2 ; \quad / /$ max. num. of parents
sqBinVars $\leftarrow$ binaryVarsInSquare(); // $d_{i}$ and $y_{i}$ in (14) are sums of binary vars
$c \leftarrow$ binaryVarsCoefficientsInSquare(); // the coefficients are either -1 or -2
for $j \leftarrow 1$ to size(sqBinVars) do
row $\leftarrow$ col $\leftarrow$ indexOf(sqBinVars[j]);
// diagonal elements indices
$Q[$ row $][\operatorname{col}] \leftarrow Q[$ row $][\operatorname{col}]+\delta_{\text {max }}^{(1)} \cdot c[j]^{2} ; \quad / /$ squared term
$Q[$ row $][\operatorname{col}] \leftarrow Q[$ row $][\operatorname{col}]+\delta_{\text {max }}^{(1)} \cdot(2 \cdot m \cdot c[j]) ; \quad / /$ double product with $m$
for $k \leftarrow j+1$ to size(sqBinVars) do // out-of-diagonal elements row $\leftarrow$ indexOf(sqBinVars[j]);
col $\leftarrow$ indexOf(sqBinVars $[k])$;
$Q[$ row $][\operatorname{col}] \leftarrow Q[\operatorname{row}][\operatorname{col}]+\delta_{\text {max }}^{(1)} \cdot(2 \cdot c[j] \cdot c[k]) ; \quad / /$ double product between vars
end
end
/* $H_{\text {cycle }}$-related terms */
for $j \leftarrow i+1$ to $n$ do
/* $H_{\text {trans }}$-related terms (Eq. (16)) */
for $k \leftarrow j+1$ to $n$ do
row $\leftarrow$ col $\leftarrow$ indexOf $\left(r_{i k}\right)$;
$Q[$ row $][\operatorname{col}] \leftarrow Q[$ row $][\operatorname{col}]+\delta_{\text {trans }} ; \quad / / r_{i k}$ coefficient (diagonal element)
row, col $\leftarrow$ indexOf $\left(r_{i j}\right)$, indexOf $\left(r_{j k}\right)$;
$Q[$ row $][\operatorname{col}] \leftarrow Q[\operatorname{row}][\operatorname{col}]+\delta_{\text {trans }} ; \quad / / r_{i j} \cdot r_{j k}$ coefficient
row, col $\leftarrow$ indexOf $\left(r_{i j}\right)$, indexOf $\left(r_{i k}\right)$;
$Q[$ row $][\operatorname{col}] \leftarrow Q[\operatorname{row}][\operatorname{col}]-\delta_{\text {trans }} ; \quad / / r_{i j} \cdot r_{i k}$ coefficient
row, col $\leftarrow$ indexOf $\left(r_{i k}\right)$, indexOf $\left(r_{j k}\right)$;
$Q[$ row $][\operatorname{col}] \leftarrow Q[\operatorname{row}][\operatorname{col}]-\delta_{\text {trans }} ; \quad / / r_{i k} \cdot r_{j k}$ coefficient
end
/* $H_{\text {consist }}$-related terms (Eq. (17) */
row, col $\leftarrow$ indexOf $\left(d_{j i}\right)$, indexOf $\left(r_{i j}\right)$;
$Q[$ row $][\operatorname{col}] \leftarrow Q[\operatorname{row}][\operatorname{col}]+\delta_{\text {consist }} ; \quad / / d_{j i} \cdot r_{i j}$ coefficient
row $\leftarrow$ col $\leftarrow$ indexOf $\left(d_{i j}\right)$;
$Q[\operatorname{row}][\operatorname{col}] \leftarrow Q[\operatorname{row}][\operatorname{col}]+\delta_{\text {consist }} ; \quad / / d_{i j}$ coefficient (diagonal element)
row, col $\leftarrow$ indexOf $\left(d_{i j}\right)$, indexOf $\left(r_{i j}\right)$;
$Q[\operatorname{row}][\operatorname{col}] \leftarrow Q[\operatorname{row}][\operatorname{col}]-\delta_{\text {consist }} ; \quad / / d_{i j} \cdot r_{i j}$ coefficient
end
end
return $Q$;
```
Algorithm 4: fillQ( $Q$, $n$, parentSets, $w, \delta_{\text {max }}, \delta_{\text {trans }}, \delta_{\text {consist }}$ )

and consistency Hamiltonians (lines 26-43), namely, to Eq. (16) and (17). In this case, due to the small amount of terms in the formulas and the absence of squares, the procedure is simpler. In detail, lines 28-35 sum the coefficients given by Eq. (16) to the corresponding locations for each set of three Bayesian variables ( $H_{\text {trans }}$ penalties). Analogously, lines 37-42 add the coefficients given by Eq. (17) to the appropriate cells for any pair of Bayesian variables ( $H_{\text {consist }}$ penalties). The resulting complexity for the matrix filling procedure (Algorithm 4) is $\mathcal{O}\left(n^{3}\right)$.

It is also worth mentioning that, in the QUBO matrix $Q$, the variables are ordered in the following way: first, the binary variables encoding the edges $\left(d_{i j}\right)$; then, the binary slack variables $\left(y_{i l}\right)$ related to the maximum parent constraint; finally, the binary variables $\left(r_{i j}\right)$ encoding the topological order. By sorting appropriately the variables in the quadratic terms (they define the row and column indices), the outcome is an upper triangular matrix; otherwise, the content of the non-zero cells below the main diagonal should be transferred to the corresponding cells above the diagonal (summing up the values).

# 3.2 Complexity 

The overall complexity of the QUBO matrix construction (Algorithm 1) is $\mathcal{O}\left(n^{4}+n^{3} N r_{\max }^{3}\right)$. Hence, it is determined by several factors: the number of Bayesian variables $(n)$ of the considered BNSL problem, the number of examples $(N)$ in the dataset, and the maximum number of states $\left(r_{\max }\right)$ among the Bayesian variables. In particular, if the number of Bayesian variables is smaller than the dataset size, the dominant complexity term becomes $n^{3} N r_{\max }^{3}$. The situation just depicted is typical. Indeed, $n$ cannot be too big due to the the limitations (in the number of qubits and connectivity) of the current quantum annealers, whereas $N$ must be considerably large to provide enough information to learn from. Therefore, typically, the calculation of the local score values $s$ (Algorithm 2) turns out to be the most expensive operation in the QUBO matrix construction; otherwise, it would be the initialization of $Q$ to zero (on a par with the $\Delta$ calculation, given the implementation of the operation in question). Concerning the maximum number of states of the Bayesian variables, its contribution is particularly relevant for Bayesian variables with continuous states. In fact, the variables in question must be discretized, and the greater the representation accuracy, the higher the execution time.

### 3.3 Execution speedup

The construction of the QUBO matrix (including the intermediate values calculation) is what takes most of the execution time. In general, a speedup could be obtained by using a different programming language such as C++; nevertheless, this is not feasible here due to D-Wave's Ocean library, which is necessary to interface with the quantum annealer and is written in Python. Instead, a valid solution consists in performing a dynamic compilation of the code through Numba [16], a just-in-time compiler for Python. In detail, Numba requires to apply a decorator to the functions that must be compiled. Then, during the execution, the first time a function with a decorator is called, it is compiled into machine code, and all the subsequent calls will run the machine code instead of the original Python code. It is important to notice that Numba works better on code including loops, NumPy arrays and library functions. Moreover, the speedup is effective only if a function is called several times; otherwise, in the case of one call in a run, the execution will be slower.

Actually, Numba has been exploited only in the experiments related to the divide et impera approach (Section 5.5), since it has been introduced after the completion of the experiments related to O'Gorman's algorithm (Section 5.4). It is also worth mentioning that the dynamic compilation has been applied only to the two functions called most often in the execution (i.e., calcNi $\pi j k$ and another internal procedure).

# 4 Divide et Impera Approach 

Embedding problems in the QPU topology requires a huge number of qubits due to the limited connectivity of the current quantum annealers. Moreover, the QUBO formulation of the BNSL problem proposed by O'Gorman et al. is densely connected by definition, making infeasible its application even to instances with a not-so-high number of variables. For these reasons, a divide et impera approach has been developed and tested; the pseudocode is shown in Algorithm 5.

```
Input: number of variables of the original BNSL problem \(n\), number of variables for each subproblem \(k\),
    list of number of states \(r\), dataset examples
Output: adjacency matrix of the solution to the original problem sol
/* Subproblems formulation */
1 subproblems \(\leftarrow\) combinations \((n, k)\);
2 subproblems \(R \leftarrow\) filter \((r\), subproblems \()\);
3 subproblemsEx \(\leftarrow\) filter(examples, subproblems);
    /* Subproblems solution */
4 \(S \leftarrow \operatorname{Set}()\);
5 for \(i \leftarrow 0\) to size(subproblems) do
    subprob, subprobR, subprobEx \(\leftarrow\) subproblems \([i]\), subproblemsR \([i]\), subproblemsEx \([i] ;\)
7 subprobQ \(\leftarrow\) calcQUBOMatrix(size(subprob), subprobR, subprobEx); // Algorithm 1
8 subprobAdjMatrix \(\leftarrow\) solveQUBO(subprobQ);
9 S.add(subprob, subprobAdjMatrix);
10 end
    /* Original solution reconstruction */
11 C, P \(\leftarrow\) countEdgesAndPenalties \((S, k)\);
12 sol \(\leftarrow\) zeroMatrix();
13 for \(i \leftarrow 0\) to \(n\) do
14 for \(j \leftarrow 0\) to \(n\) do
15 if \(i \neq j\) then
16 if \(\left(C_{i j}-P_{i j}\right)>0\) then // first strategy's condition: \(C_{i j}>C_{j i}\)
17 sol \([i][j]=1\);
18
19 end
20 end
21 end
22 return sol;
```

Algorithm 5: divideEtImpera $(S, k, N)$

The first step is the subproblems formulation (lines 1-3). Let $n$ be the number of variables of the original BNSL problem, $r$ be an array containing the number of states for each variable, and examples be a $N \times n$ matrix representing the dataset. The BNSL subproblems are generated as combinations of the $n$ variables taken $k$ at a time, where $k$ represents the desired number of variables for each subproblem. In detail, all possible combinations of variables are generated, and each subproblem is identified by the (examples matrix column) indices of the variables included. In practice, the combinations function from the Python itertools module is used. The complexity of this procedure is $O\left(c\binom{n}{k}\right)$, where $c$ is the (constant) cost for creating a list of indices. It is also worth mentioning that $k$ should be larger or equal than 3 since that is the minimum reasonable number of variables for the QUBO encoding ( $H_{\text {trans }}$ assumes $n \geq 3$ ). Then, for each $k$-variables combination, it is necessary to filter the $r$ vector and the examples matrix, obtaining a vector of $k$ elements and a $N \times k$ matrix, respectively. The total complexity of the filtering operations is $O\left(\binom{n}{k}(k+N k)\right)$.

After the subproblems generation, the implementation of O'Gorman's algorithm presented in Section 3 can be applied to each subproblem (line 7), obtaining the respective QUBO matrices, which can be submitted to the annealer or solved with alternative methods (line 8). The outcome

is an adjacency matrix for each subproblem. Regarding the complexity of this step, it is linear with respect to the number of subproblems $\left(\binom{n}{k}\right.$.

Eventually, the solution to the original BNSL problem must be reconstructed starting from the subproblems solutions (lines 11-21). Let $S$ be the set of all subproblems solutions, where each solution consists of the list of indices of the variables included and an adjacency matrix for the corresponding graph. The relevant information here is the presence of edges, thus the first step consists in counting how many times each edge appears in the subproblems solutions. Indeed, each pair of variables is present in more than one subproblem. Let $C$ be the set of counts, with $C_{i j}$ representing the number of appearances of the $(i, j)$ edge (the edges are directed, hence $(i, j)$ and $(j, i)$ are different). After the counting phase, whose complexity is $O\left(\binom{n}{k} k^{2}\right)$, the reconstruction of the solution can start. Actually, two strategies have been developed for this. The first one (the simplest one) consists in inserting in the adjacency matrix of the original problem every edge $(i, j)$ that appears at least one time in one subproblem, i.e., for which $C_{i j}>0$. If both $C_{i j}$ and $C_{j i}$ are larger than 0 , then the edge with the highest number of counts is picked; in this way, cycles of two nodes are avoided (the resulting graph must be a DAG). Instead, the second strategy (the one shown in the pseudocode) requires additional information to perform the reconstruction, namely, the penalty values $P_{i j}$. Basically, $P_{i j}$ represents the number of subproblems including the variables $i$ and $j$ in which the edge $(i, j)$ is not present; hence, the computation complexity is the same as for $C$. In practice, an edge $(i, j)$ is added to the final solution if the difference between $C_{i j}$ and $P_{i j}$ is larger than 0 , otherwise is discarded. Note that if this condition is satisfied, so are those of the first method $\left(C_{i j}>0\right.$ and $\left.C_{i j}>C_{j i}\right)$. In the experiments presented in the next section, only the second strategy has been exploited, since some preliminary experiments have confirmed its superiority. Concerning the resulting complexity of the reconstruction phase, it is $O\left(\binom{n}{k} k^{2}+n^{2}\right)$.

# 5 Empirical Evaluation 

This section deals with the Bayesian problems selected, the datasets generation procedure employed, the methods tested, the experimental setup, and the results obtained for both O'Gorman's algorithm and the divide et impera approach.

### 5.1 Bayesian problems

Three out of the four Bayesian problems used have been selected from the examples provided by the Bayes Server site [17], whereas the last one (the Lung Cancer) has been taken from a different source [18]. In detail, the implementation of O'Gorman's algorithm has been tested on the Monty Hall, the Lung Cancer and the Waste problem. Instead, the divide and impera approach has been tested on the Lung Cancer, the Waste, and the Alarm problem. It is also worth highlighting that most of these problems have been subjected to some modifications (explained in the following paragraphs) before applying the presented methods.

## Monty Hall Problem

The Monty Hall Problem (MHP) has been chosen because of its simplicity. In detail, the Bayesian network of the problem (see Figure 1, on the left) is composed of three variables $(n=3)$, and each variable has three possible states $(\{1,2,3\})$. Actually, three is also the minimum reasonable number of variables for O'Gorman's QUBO formulation. Indeed, the transitivity Hamiltonian is based on the assumption that at least three Bayesian variables are present.

## Lung Cancer

The Lung Cancer problem has been selected due to its (not excessively) higher number of variables with respect to the MHP. In particular, the original network (LC) consists of $n=5$ variables and

![img-0.jpeg](img-0.jpeg)

Figure 1: Monty Hall Problem (left) and Lung Cancer (right).
each Bayesian variable admits two possible states. Actually, also a variant (LC4Vars) with $n=4$ variables obtained by removing the "Dyspnoea" node has been tested here. In this way, a more accurate analysis on the problem size scaling could be performed. Both networks are shown in Figure 1 (right).

# Waste 

The Waste problem has been chosen for different reasons: it has a considerably larger size than the previous two; it includes continuous Bayesian variables, and also a variable with more than two parents. In detail, the Bayesian network of the original problem is composed of nine variables $(n=9)$, of which three are discrete with two states, and six are continuous. Since the QUBO encoding admits only discrete variables, a discretization has been required for the continuous ones. However, it is not possible to use a single discretization threshold because the variables have different mean values. Hence, each continuous variable has been transformed into a discrete one with two states by applying the following procedure: first, the lowest and the highest values are identified by evaluating all the settings of the parent variables (this is possible since the number of variables and states are small), and the average of the two values is kept as a discretization threshold; then, for each combination of parent states, the mean and the variance of the continuous variable are taken
![img-1.jpeg](img-1.jpeg)

Figure 2: Waste.

down, and the probability of the Gaussian with these parameters having a value higher than the threshold is set as the probability of the high state ( $H$, opposed to the low state $L$ ). Specifically, to determine the lowest (highest) value, the respective variance is subtracted from (summed to) the minimum (maximum) mean value observed; moreover, in the case of a continuous variable with a continuous parent, the parent is discretized first, and the lowest and highest values are used as evidence for the parent states $L$ and $H$. The resulting Bayesian problem is denoted here as Waste.

Figure 2 summarizes all the considered variants of the problem. In particular, Waste differs from the original problem only in the lack of the edge between Waste Type and Filter Efficiency, which has been lost in the discretization procedure. Instead, in Waste2P (variant of Waste), the edge between Waste Type and Dust Emission has been removed so that the maximum number of parents is equal to two (in practice, the most balanced probability values have been kept for the Dust Emission node). Finally, Waste2PDep is a variant of Waste2P in which the edge between Waste Type and Filter Efficiency has been reintroduced by manually altering some probability values (in the Filter Efficiency probability table). In addition, in Waste2PDep, some other probabilities have been slightly changed (Dust Emission and Metals Emission tables) in order to have more balanced probability distributions.

# Alarm 

Eventually, Alarm has been picked mainly for its size. Indeed, it is quite close to the maximum BNSL problem size that can be embedded in the Pegasus topology using O'Gorman's formulation $(\approx 18)$. Moreover, the presence of a variable with four parents allows evaluating the ability of the divide et impera approach to reconstruct Bayesian networks with more than two parents for a single variable. Actually, the original Alarm problem consists of 38 Bayesian variables, whereas the version used here includes only 15 of them (with their structure preserved). The Bayesian network employed in the experiments is shown in Figure 3.

### 5.2 Datasets generation

For each problem, several datasets have been generated varying both the size and the creation method. Specifically, three dataset sizes $(N)$ have been used, namely, $10^{4}(10 \mathrm{~K}), 10^{5}(100 \mathrm{~K})$, and $10^{6}(1 \mathrm{M})$. Regarding the generation methods, two have been employed. The first one consists in generating $N$ examples through the uniform function from the Python random module by sampling from the network probability distribution. Instead, the second method aims at generating datasets with zero variance, i.e., with combinations of states appearing exactly the expected amount of times. In particular, in order to generate the expected datasets, the probability $p$ of every combination of states of the network variables is calculated; then, for each combination, $\lfloor N * p\rfloor$ examples are inserted in the dataset. Actually, for some probability values, it may not be possible to generate an integer number of examples, and, consequently, the variance of the dataset is not exactly zero. In addition, the resulting dataset may have a number of samples lower than the desired one. For instance, for the Alarm problem, the dataset of size $N=10^{4}$ generated using this method has a considerably lower number of samples $(\approx 9000)$ due to the presence of many state combinations that are not represented at all because of their very low probability values (the other problem datasets are not significantly affected by this issue). The datasets generated using the second method are denoted as Exp.

### 5.3 Methods and experimental setup

After the application of O'Gorman's algorithm, the BNSL problem encoded in the QUBO matrix must be solved. For this purpose, three methods have been exploited in the experiments: quantum annealing (QA), simulated annealing (SA) and exhaustive search (ES). The functioning of quantum annealing has been already explained in Section 2.2. Instead, simulated annealing is a well-known

Reconstructing Bayesian Networks on a Quantum Annealer
![img-2.jpeg](img-2.jpeg)

classical metaheuristic technique used for solving optimization problems [19]; further details about the algorithm can be found here ${ }^{\mathrm{b}}$. Eventually, the exhaustive search represents an optimized brute force approach.

In detail, a simple brute force on the QUBO representation would be unfeasible even for small BNSL instances due to the high number of binary variables. Hence, ES limits the brute force to the edge binary variables $d_{i j}$, while considering only the best setup of $y_{i l}$ and $r_{i j}$. In particular, for each Bayesian variable $i$, the $y_{i l}$ binary variables must be set so that $y_{i}$ (in Eq. (14)) is equal to the difference between $m$ and $d_{i}$. In this way, there is no penalty from the max Hamiltonian. Obviously, this is possible only for nodes that do not have more than $m$ parents; otherwise, the minimum penalty is given by $y_{i}$ equal to zero. Instead, setting the $r_{i j}$ binary variables is more complex. Indeed, computing the topological order of the graph encoded in $d_{i j}$ is not enough since, if two Bayesian variables $i$ and $j$ are not connected (i.e., it does not exist a path from one variable to the other), there is no straightforward setup for $r_{i j}$. In addition, setting all the uncertain binary variables to either 0 or 1 does not solve the problem since a cycle might be produced, with consequent penalty from $H_{\text {trans }}$. The solution consists in completing the graph encoded in $d_{i j}$ by adding one edge at a time (while verifying that no cycle is formed), and then computing the topological order of the resulting graph. In this way, it is possible to properly set all $r_{i j}$ binary variables and avoid any penalty from the cycle Hamiltonian. Obviously, if the graph encoded in $d_{i j}$ contains a cycle, it is not possible to avoid the penalty. The resulting complexity for setting $y_{i l}$ and $r_{i j}$ turns out to be $\mathcal{O}\left(n^{3}\right)$ for sparse graphs and $\mathcal{O}\left(n^{4}\right)$ for dense graphs. In the end, these optimizations do not change the complexity class of ES with respect to the simple brute force (it remains exponential in the number of Bayesian variables $n$ ) but significantly reduce the number of operations to be performed. Another improvement that has been introduced in ES is the parallelization of the solutions evaluation.

Regarding the setup for the experiments on the implementation of O'Gorman's algorithm, different combinations of annealing parameters (number of annealer reads and annealing time) [20] have been tested for QA; the specific values are reported in the various results sections. In addition, the default annealing schedule has been employed (the system used is Advantage 1.1), and the QPU embedding has been performed through the EmbeddingComposite class (see Section 2.3). As concerns SA, the implementation provided by D-Wave [21] has been exploited. Except for the number of reads (different values have been employed), the default configuration has been used, and the execution has been carried out on a local machine. Eventually, ES does not require to set parameters and has also been executed locally. In detail, a machine with a quad-core CPU (Intel i5-6400) and 16 GB of RAM has been used for the datasets generation, the QUBO matrices construction, and the execution of the classical methods.

Concerning the divide et impera approach, only one configuration of annealing parameters has been evaluated for QA; the reason and the values are specified in the related results section. Furthermore, the default annealing schedule has been employed, but, in this case, the system used is Advantage 4.1 since the previous model had already been dismissed. Instead, the QPU embedding method and the SA implementation are the same as those exploited in the experiments on O'Gorman's algorithm; the only difference lies in the number of reads used for SA, which has been set to a single value too. Finally, ES has not been evaluated on this approach due to its high time requirements. All the classical operations for the divide et impera approach have been executed on a machine with a quad-core CPU (Intel i7-7700HQ) and 16 GB of RAM.

Eventually, it is worth mentioning that, for both the implementation of O'Gorman's algorithm and the divide et impera approach, the performance-related analyses presented here involve only Exp datasets because some preliminary tests have confirmed that the difference in terms of performance when working on Exp or non-Exp datasets is negligible.

[^0]
[^0]:    ${ }^{\mathrm{b}}$ https://en.wikipedia.org/wiki/Simulated_annealing

# 5.4 O'Gorman's algorithm results 

Several experiments have been performed on the implementation of O'Gorman's algorithm. The results obtained are presented in the subsequent paragraphs.

## QUBO formulation correctness and $\alpha_{i j k}$ hyperparameters

The QUBO encoding must accurately represent the original BNSL problem; to this end, the $\alpha_{i j k}$ hyperparameters must be set appropriately. In detail, if $\alpha_{i j k}$ have suitable values, the image $\left(x^{T} Q x\right)$ of the expected solution will be the global minimum. To verify this, it is necessary to find the global minimum solution through ES and compare it with the expected one. In particular, the QUBO version of the expected solution $(x)$ is obtained as follows: the Bayesian network that has been used to generate the dataset is exploited to set the $d_{i j}$ binary variables encoding the edges, whereas the best setup of $y_{i l}$ and $r_{i j}$ is found using the same approach employed by ES (see Section 5.3).

Since the objective is to learn the structure of a Bayesian network from a set of data, the values of $\alpha_{i j k}$ must be uninformative, i.e., they must not encode information about the target Bayesian network. For this reason, the first values of $\alpha_{i j k}$ that have been tested are $N /\left(r_{i} \cdot q_{i}\right)$ and 1 , as proposed by Heckerman et al. [22]. The results obtained are reported in Table 1. In detail, the first alternative $\left(N /\left(r_{i} \cdot q_{i}\right)\right)$ has performed decently on the MHP problem (the smallest one), and extremely bad on all the others (characterised by a higher number of variables); in practice, $N$ prior counts uniformly distributed among all "variable" - "parent set" state combinations are added in Eq. (13). Instead, the second possibility (i.e., 1) has not worked at all. Therefore, other values have been evaluated, namely, $1 /\left(r_{i} \cdot q_{i}\right)$ and $1 / r_{i}$, which have been selected with the idea of influencing the counts as little as possible. As reported in the same table, both of them have shown the desired behaviour, and the first one has been chosen as the default setup.

In particular, the ratios in Table 1 have been obtained using 8 datasets for each "problem" - " $\alpha_{i j k}$ value" combination; the datasets in question have been created with different sizes and exploiting both generation methods (see Section 5.2). Specifically, four datasets of size $N=10^{4}$ (of which one Exp), two datasets of size $N=10^{5}$ (of which one Exp), and two datasets of size $N=10^{6}$ (of which one Exp) have been used.

Table 1: Ratio of the number of times in which the best and the expected solutions coincide to the number of tests ( 8 for each cell), for different problems and $\alpha_{i j k}$ values.


## Dataset size and QUBO matrix construction time

After the choice of the $\alpha_{i j k}$ value, the impact of the dataset size on the QUBO matrix construction time has been analyzed. As shown in Table 2, the required time increases linearly with the dataset size in accordance with the complexity $\mathcal{O}\left(n^{4}+n^{3} N r_{\max }^{3}\right)$ discussed in Section 3.2. In practice, large dataset sizes turn out to be prohibitive, especially when constructing the QUBO matrix for problems with a high number of variables. Because of this and the fact that a dataset size larger than $N=10^{4}$ leads to no improvement in terms of performance (see Table 3), it is advantageous to keep the dataset size limited.

Regarding the tables data, the time values in Table 2 have been obtained using one Exp and four non-Exp datasets for each "problem" - "dataset size" combination (hence, five runs for each entry). Instead, the values in Table 3 have been acquired through QA, using Exp datasets only, $10^{4}$ reads, $20 \mu \mathrm{~s}$ of annealing time, and 10 runs for each dataset size. The metric reported in the

second table is described in the performance section later on; for the time being, it is sufficient to know that larger values in the table correspond to better performance.

Table 2: Average QUBO matrix $(Q)$ construction time in seconds, for different problems and dataset sizes. For each entry, 5 different datasets (of which one Exp) have been used.


Table 3: Average solution value found by QA in Waste2PDep on Exp datasets of different sizes. $10^{4}$ reads, $20 \mu \mathrm{~s}$ of annealing time, and 10 runs (for each dataset size) have been used.


# Number of reads and annealing time (QA) 

The number of reads, i.e., measurements, and the annealing time per read are two extremely relevant parameters for the performance of QA. Hence, an extensive experimental evaluation has been performed, with 10 runs for each configuration; the results are reported in Table 4. In detail, the maximum allowed number of reads (on D-Wave systems) is $10^{4}$, whereas the maximum annealing time per read is $2000 \mu \mathrm{~s}$. However, there is also an internal constraint that prevents an annealing time larger than $999 \mu \mathrm{~s}$ with $10^{3}$ reads, and an annealing time larger than $99 \mu \mathrm{~s}$ with $10^{4}$ reads. Looking at the results, it is clear that a higher number of reads provides better performance, and the same holds for the annealing time. Nevertheless, the number of reads has a more significant impact. Indeed, the results achieved with the maximum allowed number of reads and an annealing time far lower than the joint limit are clearly better than those achieved with the annealing time maximized. Hence, the best setup corresponds to the maximum allowed number of reads $\left(10^{4}\right)$ and the joint limit annealing time $(99 \mu \mathrm{~s})$.

Table 4: Ratio of the number of times the global minimum is found by QA to the number of experiments ( 10 for each configuration), for different numbers of reads and annealing times on the LC Exp dataset with size $N=10^{4}$.


## Performance

Finally, all the methods described in Section 5.3 have been applied to all the problems presented in Section 5.1 with the purpose of comparing their performance; the results are reported in Table 5. In particular, for these experiments, Exp datasets of size $N=10^{4}$ have been employed. Moreover, $10^{4}$ reads have been used for SA, whereas, for QA, the best setup has been exploited (i.e., $10^{4}$ reads and an annealing time per read equal to $99 \mu \mathrm{~s}$ ). The number of runs, for both SA and QA, is 10 , and the success rate is given by the ratio between the number of runs in which the expected solution has been discovered and the total number of runs. Instead, the result value represents the ratio between the QUBO image $\left(x^{T} Q x\right)$ of the solution found and the QUBO image of the

Table 5: Comparison of ES, SA, and QA performances on different problems, using Exp datasets of size $N=10^{4}$, $10^{4}$ reads for SA, and the best setup for QA ( $10^{4}$ reads, $99 \mu \mathrm{~s}$ annealing time). The number of runs, for both SA and QA, is 10 .


expected solution, averaged over the runs (larger values correspond to better performance, since the image value of the expected solution is always negative in these experiments). Regarding the time values, they include only the resolution of the QUBO matrix; specifically, in the case of QA, they correspond to the QPU access time (see [23] for additional details). Eventually, for QA, the last column (Average \# exp. sol.) reports the number of times that the expected solution has been found in a single run, averaged over the runs.

In practice, ES has outperformed both SA and QA on the smallest problems, i.e., MHP and LC4Vars, always finding the minimum in less time. However, due to its exponential complexity, it has lost the comparison on the LC problem $(n=5)$, and has turned out to be too time-consuming on the largest ones.

Concerning the other methods, QA has always managed to find the optimum solution to the problems with three and four Bayesian variables, also outperforming SA in terms of execution time. Moreover, it has detected the global minimum several times in each run ( $10^{4}$ measurements per run are performed), which suggests that a fewer number of reads could be enough to achieve the same results on these problems. Instead, for the five-variable problem, QA has managed to discover the minimum only half of the times (with the minimum occasionally appearing more than once), whereas SA has always found it at the cost of a slightly higher runtime. Eventually, neither QA nor SA have ever detected the optimum solution to the largest problems $(n=9)$. Nevertheless, the quality of the solutions found is good on average, especially of those found by SA, whose execution time has turned out to be slightly higher also in this case. It is also worth highlighting that, for the Waste problem, solutions with a better score than that of the expected solution have been found; this has always happened with SA (the average result value is larger than 1.0) and sometimes with QA. The reason lies in the presence of a node with three parents in the expected solution. Basically, this penalizes the expected solution and makes possible to have other solutions respecting the maximum parent constraint $(m \leq 2)$ with a better score.

In addition, the impact of the annealing time on the performance of QA in the same experiments has been analyzed; the results for an annealing time of $1 \mu \mathrm{~s}$ and $99 \mu \mathrm{~s}$ are reported in Table 6. In

Table 6: Comparison of quantum annealing performances on several problems for different values of annealing time, using Exp datasets of size $N=10^{4}$ and $10^{4}$ reads. The number of runs is 10 .


practice, a higher annealing time has led to no improvement on the smallest problem (MHP) but has provided better results on average, with only a little additional time required, on all the others. In particular, for the problems with four (LC4Vars) and five (LC) Bayesian variables, it has also provided a higher success rate and a higher number of occurrences of the minimum solution.

Eventually, since SA does not have limits on the number of reads, further experiments have been executed on the Waste2PDep problem with the Exp dataset of size $N=10^{4}$, using a number of reads equal to $10^{5}$ and $10^{6}$, respectively. The execution time has increased linearly, but no substantial improvement in the performance has been observed.

# 5.5 Divide et impera results 

As mentioned in Section 5.1, the divide et impera approach has been tested on two problems used for the evaluation of O'Gorman's algorithm, namely, LC and Waste (only in their main variant), and a new additional problem, i.e., Alarm. The results are presented in the following paragraphs.

## Execution speedup and timing

First of all, the speedup achieved exploiting the technique illustrated in Section 3.3 has been analyzed. In particular, for each problem taken into account, one Exp dataset of size $N=10^{4}$ and one run have been used. Moreover, regarding the number of variables for each subproblem $(k)$, all values between three (the minimum reasonable value, see Section 4) and $n$ have been tested; it is also worth highlighting that $k=n$ corresponds to the direct application of the implementation of O'Gorman's algorithm. The results are reported in Table 7, with the time values including the subproblems formulation and the QUBO matrices construction (thus, neither the subproblems resolution nor the final solution reconstruction). In detail, only LC and Waste have been considered here, since the times without speedup for Alarm would have been unfeasible to collect using the machine available. Concerning LC, the time required has been reduced by $\approx 9$ times on average for the divide et impera approach and $\approx 5.6$ times for O'Gorman's algorithm. Instead, for the Waste problem, the speedup has been more significant due to the higher number of variables and/or subproblems, with an average of $\approx 38.4$ times for the divide et impera approach and $\approx 17$ times for O'Gorman's algorithm.

Table 7: Speedup achieved for different $k$ values on LC and Waste, using an Exp datasets of size $N=10^{4}$ and a single run. The time values, expressed in seconds, include the subproblems formulation and the QUBO matrices construction. In particular, D.e.I. $=$ divide et impera, O'G. $=$ O'Gorman.


Instead, Table 8 reports some statistics computed on analogous time values (including subproblems formulation and QUBO matrices construction), which have been obtained using four different non-Exp datasets of size $N=10^{4}$. The Exp datasets have not been included since they may have a lower number of samples, as explained in Section 5.2. In this case, also the Alarm problem has been considered; indeed, all the time values refer to the optimized code (i.e., with speedup). However, due to the still high times, the maximum $k$ value used for it is 9 . Eventually, it is worth

highlighting that the limit case corresponding to the direct execution of O'Gorman's algorithm $(k=n)$ has not been taken into account here. In detail, the highest average time across $k$ values is determined by both the subproblems size and the number of subproblems. Indeed, the average time per subproblem grows with the subproblem size (see the last column). Moreover, looking at the standard deviation (STD) and the coefficient of variation (CV), it turns out that the variance in the input data does not significantly affect the time values. Specifically, the CV value is always lower than 0.05 .

Table 8: Statistics on subproblems formulation and QUBO matrices construction time for different $k$ values. Specifically, 4 non-Exp datasets of size $N=10^{4}$ have been used for each problem (one run for each dataset). In addition, the time values, expressed in seconds, refer to the optimized code (i.e., with speedup).


# Performance 

To evaluate the performance of the divide et impera approach, the following setup has been used for each problem: one Exp dataset of size $N=10^{4}$, five runs, and a number of variables for each subproblem $(k)$ ranging from three (the minimum reasonable value) to $n$ (the total number of Bayesian variables), with the upper limit representing the direct application of O'Gorman's algorithm. Regarding the methods for solving the QUBO encoding, only SA and QA have been exploited in these experiments. Indeed, ES would have required an unreasonable amount of time to solve the subproblems generated with a high $k$ value. Furthermore, 100 reads and an annealing time equal to $1 \mu \mathrm{~s}$ have been used for QA due to the limited quantum resources available and the high number of subproblems to resolve (considering all experiments). To make a fair comparison, 100 reads have been used also for SA. Eventually, it is worth highlighting that only the second reconstruction strategy developed for the divide et impera approach has been applied in these experiments, as explained in Section 4.

Starting from LC, the results achieved for it are reported in Table 9. In addition, a "ROC curve"-like plot is provided in Figure 4. In practice, SA has turned out to perform better than QA on LC, and the divide et impera approach has outperformed the direct application of O'Gorman's algorithm for both resolution methods. Indeed, the higher the sensitivity and the specificity, the better the result. It is also worth mentioning that SA with $k=4$ has been able to find the perfect solution (four correct and zero wrong edges) in all five runs. In addition, by looking at the number of unique edges found across all runs (fifth column), it turns out that, for the divide et impera approach, SA tends to find always the same correct and wrong edges, whereas QA shows more variability, as well as O'Gorman's algorithm.

Table 9: Results achieved by the divide et impera approach on the LC problem, for different numbers of variables per subproblem $(k)$ and methods (SA/QA), using an Exp dataset of size $N=10^{4}$, five runs, 100 reads for SA, and 100 reads and $1 \mu$ s of annealing time for QA. The last $k$ value (5) corresponds to the direct application of the implementation of O'Gorman's algorithm. In particular, D.e.I. $=$ divide et impera, O'G. $=$ O'Gorman.


![img-3.jpeg](img-3.jpeg)

Figure 4: Sensitivity versus (1 - Specificity) for the LC problem. This plot results from the data reported in Table 9.

Concerning the Waste problem, whose results are reported in Table 10 and displayed in Figure 5, the overall performance is worse for both SA and QA. Specifically, also in this case, SA has performed better than QA overall. Only for $k=3$, QA has been able to achieve better results on average. Instead, the superiority of the divide et impera approach w.r.t. the direct application of O'Gorman's algorithm has turned out to be less marked. In detail, for SA, the divide et impera approach has won the comparison for almost all (but not all) $k$ values. Regarding QA, O'Gorman's algorithm has achieved a relatively high sensitivity (w.r.t. all QA results), but the corresponding specificity is quite low. In the end, for both methods (SA and QA), it is possible to find a $k$ value for which the divide et impera approach has performed better than O'Gorman's algorithm. Actually,

Table 10: Results achieved by the divide et impera approach on the Waste problem, for different numbers of variables per subproblem $(k)$ and methods (SA/QA), using an Exp dataset of size $N=10^{4}$, five runs, 100 reads for SA, and 100 reads and $1 \mu \mathrm{~s}$ of annealing time for QA. The last $k$ value (9) corresponds to the direct application of the implementation of O'Gorman's algorithm. In particular, D.e.I. $=$ divide et impera, O'G. $=$ O'Gorman, Sens. $=$ sensitivity, Spec. $=$ specificity.


for this problem, the perfect solution has never been found. The best results have been achieved by SA with $k=6$, which has discovered four correct edges out of nine in almost all runs and only two wrong edges on average. In addition, the maximum number of correct edges that have been found in a single run is equal to 6 (SA with $k=4$ ). However, it is worth remarking that the problem in question has been subjected to a discretization procedure and includes a node with three parents. Eventually, in general, the observations made for LC on the number of unique edges found turn out to be valid also for the Waste problem. The only difference lies in the correct edges found by the divide et impera approach with QA; indeed, they tend to be the same across runs.

Finally, the results related to the Alarm problem are reported in Table 11 and shown in Figure 6. In particular, the divide et impera approach with QA has not been evaluated in this case because the number of subproblems is really high and the sequential submission of numerous QUBO problems to the D-Wave's annealer tends to fail due to connectivity issues (from D-Wave's side), invalidating the run. As for the other problems, the divide et impera approach has outperformed the direct application of O'Gorman's algorithm. Indeed, the latter has won the comparison (with a worse

![img-4.jpeg](img-4.jpeg)

Figure 5: Sensitivity versus (1 - Specificity) for the Waste problem. This plot results from the data reported in Table 10 .
![img-5.jpeg](img-5.jpeg)

Figure 6: Sensitivity versus (1 - Specificity) for the Alarm problem. This plot results from the data reported in Table 11 .

Table 11: Results achieved by the divide et impera approach on the Alarm problem, for different numbers of variables per subproblem $(k)$, using an Exp dataset of size $N=10^{4}$, five runs, 100 reads for SA, and 100 reads and $1 \mu \mathrm{~s}$ of annealing time for QA. The last $k$ value (15) corresponds to the direct application of the implementation of O'Gorman's algorithm. In particular, D.e.I. $=$ divide et impera, O'G. $=$ O'Gorman, Sens. $=$ sensitivity, Spec. $=$ specificity.


specificity) only for $k=12$. In addition, SA has achieved far better results than O'Gorman's algorithm with QA. Concerning the quality of the solution found, the best results have been achieved by SA with $k=4$, which has been capable of detecting 12.6 correct edges out of 15 on average (note that the problem includes a variable with four parents). However, the number of wrong edges is quite high ( 16.4 on average). The same configuration has also discovered the highest number of correct edges (13). Eventually, it is worth making two last observations: the number of edges (both correct and wrong) detected by the divide et impera approach tends to decrease by increasing the value of $k$; the divide et impera approach tends to discover always the same correct and wrong edges across runs (look at the fifth column), whereas O'Gorman's algorithm exhibits more variability. Actually, the wrong edges for $k=3$ and the correct edges for O'Gorman's algorithm with SA represent two exceptions.

# 6 Conclusion 

In this work, we have presented an implementation in Python of the algorithm proposed by O'Gorman et al. for solving the BNSL problem on a quantum annealer, a divide et impera approach that allows addressing BNSL instances with a higher number of variables, a complexity analysis of them, and their experimental evaluation. In detail, to make O'Gorman's formulation effectively usable, algebraic manipulations have been applied to the computation of the local scores $s_{i}\left(\Pi_{i}\left(B_{s}\right)\right)$. Moreover, a simplified lower bound has been introduced for the penalty value $\delta_{\text {consist }}$, and the best setup of the $\alpha_{i j k}$ hyperparameters has been empirically determined. The results achieved in the experiments have demonstrated that O'Gorman's algorithm can be effectively used to reconstruct Bayesian networks of small sizes $(n<=5)$ with less than three parents per node $(m<3)$. Instead, in presence of more Bayesian variables $(n=9)$, the algorithm performance have turned out to be worse. Indeed, good quality solutions (in terms of QUBO image value) have been found, but not the correct one. It is also worth remarking that one of these larger problems includes a node with three parents. In addition, the linear dependency between the dataset size and the QUBO matrix construction time has been confirmed. Eventually, QA (using the best annealing parameters) has been able to achieve comparable or slightly worse results with respect to SA, proving the competitiveness of the current annealing architectures on this task.

Concerning the divide et impera approach, which has been developed to overcome the limitation on the problem size dictated by the available annealing devices, the results have demonstrated that it performs better than the direct application of O'Gorman's algorithm. Indeed, in all problems considered, for all resolution methods tested, there is more than one $k$ value for which the divide et impera approach has achieved better results; actually, in almost all cases, these $k$ values represent the majority. Instead, in general, the quality (in terms of resulting Bayesian network) of the solutions found has turned out to be not optimal. However, non-ideal annealing parameters have been used for QA due to the limited quantum resources at our disposal, and the number of reads for SA has also been reduced (w.r.t. the value used for the experiments on O'Gorman's algorithm) for a fair comparison. Moreover, in this second set of experiments, unlike in the first one, SA has performed definitely better than QA; nevertheless, this is probably related to the less-performing parameters used here. Finally, the experiments on the subproblems formulation and QUBO matrices construction time have confirmed the effectiveness of the technique used to speed up the execution (and also the independence of the times from the variance in the input data).

Future work includes the following possibilities: testing the divide et impera approach on Bayesian problems whose size is larger than the maximum size embeddable in the Pegasus architecture using O'Gorman's algorithm; evaluating the aforementioned approach with QA using moreperforming annealing parameters; analysing the impact of considering only part of the subproblems of size $k$. We conclude by reminding that the code of both the implementation of O'Gorman's algorithm and the divide et impera approach is available under the GPLv2 licence $[9,10]$.

## Acknowledgements

This work was supported by Q@TN, the joint lab between University of Trento, FBK-Fondazione Bruno Kessler, INFN-National Institute for Nuclear Physics and CNR-National Research Council. In addition, the authors gratefully acknowledge the Jülich Supercomputing Center (https://www. fz-juelich.de/ias/jsc) for funding this project by providing computing time through the Jülich UNified Infrastructure of Quantum computing (JUNIQ) on the D-Wave quantum annealer.
