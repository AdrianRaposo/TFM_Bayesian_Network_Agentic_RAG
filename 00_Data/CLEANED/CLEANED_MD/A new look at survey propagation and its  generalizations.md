# A New Look at Survey Propagation and its Generalizations 

Elitza Maneva* Elchanan Mossel ${ }^{\dagger}$ Martin J. Wainwright ${ }^{\ddagger}$<br>October 24, 2018


#### Abstract

This paper provides a new conceptual perspective on survey propagation, which is an iterative algorithm recently introduced by the statistical physics community that is very effective in solving random $k$-SAT problems even with densities close to the satisfiability threshold. We first describe how any SAT formula can be associated with a novel family of Markov random fields (MRFs), parameterized by a real number $\rho \in[0,1]$. We then show that applying belief propagation - a well-known "message-passing" technique for estimating marginal probabilitiesto this family of MRFs recovers a known family of algorithms, ranging from pure survey propagation at one extreme $(\rho=1)$ to standard belief propagation on the uniform distribution over SAT assignments at the other extreme $(\rho=0)$. Configurations in these MRFs have a natural interpretation as partial satisfiability assignments, on which a partial order can be defined. We isolate cores as minimal elements in this partial ordering, which are also fixed points of survey propagation and the only assignments with positive probability in the MRF for $\rho=1$. Our experimental results for $k=3$ suggest that solutions of random formulas typically do not possess non-trivial cores. This makes it necessary to study the structure of the space of partial assignments for $\rho<1$ and investigate the role of assignments that are very close to being cores. To that end, we investigate the associated lattice structure, and prove a weight-preserving identity that shows how any MRF with $\rho>0$ can be viewed as a "smoothed" version of the uniform distribution over satisfying assignments $(\rho=0)$. Finally, we isolate properties of Gibbs sampling and message-passing algorithms that are typical for an ensemble of $k$-SAT problems.


Keywords: Satisfiability problems; $k$-SAT; survey propagation; belief propagation; sum-product; message-passing; factor graph; Markov random field; Gibbs sampling.

[^0]
[^0]:    *Department of Electrical Engineering and Computer Science, UC Berkeley, CA. Email: elitza@eecs.berkeley.edu. Supported by NSF grant CCR-0121555.
    ${ }^{\dagger}$ Department of Statistics, UC Berkeley, CA. Email: mossel@stat.berkeley.edu. Supported by a Miller Fellowship in Computer Science and Statistics, NSF grant DMS-0504245 and a Sloan Fellowship in Mathematics
    ${ }^{\ddagger}$ Department of Electrical Engineering and Computer Science and Department of Statistics, UC Berkeley, CA. Email: wainwrig@eecs.berkeley.edu. Supported by a Sloan Fellowship in Computer Science and a grant from Intel Corporation.

# 1 Introduction 

Constraint satisfaction problems play an important role across a broad spectrum of computer science, including computational complexity theory [9], coding theory [19, 35], and artificial intelligence $[34,14]$. Important but challenging problems include devising efficient algorithms for finding satisfying assignments (when the problem is indeed satisfiable), or conversely providing a certificate of unsatisfiability. One of the best-known examples of a constraint satisfaction problem is the $k$-SAT problem, which is a classical NP complete problem [9] for all $k \geq 3$. In trying to understand the origin of its hardness, a great deal of research has been devoted to the properties of formulas drawn from different probability distributions. One of the most natural models for random $k$-SAT problems is the following: for a fixed density parameter $\alpha>0$, choose $m=\alpha n$ clauses uniformly and with replacement from the set of all $k$-clauses on $n$ variables. Despite its simplicity, many essential properties of this model are yet to be understood: in particular, the hardness of deciding if a random formula is satisfiable and finding a satisfying assignment for a random formula are both major open problems $[25,42,16]$.

One of the most exciting recent developments in satisfiability problems has its origins not in computer science, but rather in statistical physics. More specifically, the ground-breaking contribution of Mézard, Parisi and Zecchina [28], as described in an article published in "Science", is the development of a new algorithm for solving $k$-SAT problems. A particularly dramatic feature of this method, known as survey propagation, is that it appears to remain effective at solving very large instances of random $k$-SAT problems - even with densities very close to the satisfiability threshold, a regime where other "local" algorithms (e.g., the WSAT method [37]) typically fail. Given this remarkable behavior, the survey propagation algorithm has generated a great deal of excitement and follow-up work in both the statistical physics and computer science communities [e.g., $6,5,7,3,2,32,33,41]$. Nonetheless, despite the considerable progress to date, the reasons underlying the remarkable performance of survey propagation are not yet fully understood.

### 1.1 Our contributions

This paper provides a novel conceptual perspective on survey propagation - one that not only sheds light on the reasons underlying its success, but also places it within a broader framework of related "message-passing" algorithms that are widely used in different branches of computer science. More precisely, by introducing a new family of Markov random fields (MRFs) that are associated with any $k$-SAT problem, we show how a range of algorithms - including survey propagation as a special case - can all be recovered as instances of the well-known belief propagation algorithm [34], as applied to suitably restricted MRFs within this family. This equivalence is important because belief propagation is a message-passing algorithm - widely used and studied in various areas, including coding theory $[35,24,44]$, computer vision $[17,11]$ and artificial intelligence $[34,45]$ - for computing approximations to marginal distributions in Markov random fields. Moreover, this equivalence motivates a deeper study of the combinatorial properties of the family of extended MRFs associated with survey propagation. Indeed, one of the main contributions of our work is to reveal the combinatorial structures underlying the survey propagation algorithm.

The configurations in our extended MRFs turn out to have a natural interpretation as particular types of partial SAT assignments, in which a subset of variables are assigned 0 or 1 variables in such a way that the remaining formula does not contain any empty or unit clauses. To provide some geometrical intuition for our results, it is convenient to picture these partial assignments as

![img-0.jpeg](img-0.jpeg)

Figure 1. The set of fully assigned satisfying configurations occupy the top plane, and are arranged into clusters. Enlarging to the space of partial assignments leads to a new space with better connectivity. Minimal elements in the partial ordering are known as cores. Each core corresponds to one or more clusters of solutions from the top plane. In this example, one of the clusters has as a core a non-trivial partial assignment, whereas the others are connected to the all-∗ assignment.
arranged in layers depending on the number of assigned variables, so that the top layer consists of fully assigned satisfying configurations. Figure 1 provides an idealized illustration of the space of partial assignments viewed in this manner. It is argued [29, 32, 2] that for random formulas with high density of clauses, the set of fully assigned configurations are separated into disjoint clusters that cause local message-passing algorithms like belief propagation to break down (see Figure 2 for an illustration). Based on our results, the introduction of partial SAT assignments yields a modified search space that is far less fragmented, thereby permitting a local algorithm like belief propagation to find solutions.

We show that there is a natural partial ordering associated with this enlarged space, and we refer to minimal elements in this partial ordering as cores. We prove that any core is a fixed point of the pure form of survey propagation $(\rho=1)$. This fact indicates that each core represents a summary of one cluster of solutions. However, our experimental results for $k=3$ indicate that the solutions of random formulas typically have trivial cores (i.e., the empty assignment). This observation motivates deeper study of the full family of Markov random fields for the range $0 \leq \rho \leq 1$, as well as the associated belief propagation algorithms, which we denote by $\operatorname{SP}(\rho)$. Accordingly, we study the lattice structure of the partial assignments, and prove a combinatorial identity that reveals how the distribution for $\rho \in(0,1)$ can be viewed as a "smoothed" version of the MRF with $\rho=0$. Our experimental results on the $\operatorname{SP}(\rho)$ algorithms indicate that they are most effective for values of $\rho$ close to and not necessarily equal to 1 . One intriguing possibility is that the effectiveness of pure survey propagation (i.e., $\mathrm{SP}(1)$ ) may be a by-product of the fact that $\operatorname{SP}(\rho)$ is most effective for values of $\rho$ less than 1 , but going to 1 as $n$ goes to infinity. The near-core assignments which are the ones of maximum weight in this case, may correspond to quasi-solutions of the cavity equations, as defined by Parisi [33]. In addition, we consider alternative sampling-based methods (e.g., Gibbs sampling) for computing marginals for the extended MRFs. We also study properties of both message-passing and Gibbs sampling that are typical over a random ensemble of $k$-SAT problems. We establish results that link the typical behavior of Gibbs sampling and messagepassing algorithms under suitable initialization, and when applied to the extended family of MRFs

with $\rho$ sufficiently close to one.
The fact that the pure form of survey propagation (i.e., $\mathrm{SP}(1)$ in our notation) is a form of belief propagation was first conjectured by Braunstein et al. [6], and established independently of our work by Braunstein and Zecchina [7]. In other independent work, Aurell et al. [3] provided an alternative derivation of $\mathrm{SP}(1)$ that established a link to belief propagation. However, both of these papers treat only the case $\rho=1$, and do not provide a combinatorial interpretation based on an underlying Markov random field. The results established here are a strict generalization, applying to the full range of $\rho \in[0,1]$. Moreover, the structures intrinsic to our Markov random fields - namely cores and lattices - highlight the importance of values $\rho \neq 1$, and place the survey propagation algorithm on a combinatorial ground. As we discuss later, this combinatorial perspective has already inspired subsequent work [2] on survey propagation for satisfiability problems. Looking forward, the methodology of partial assignments may also open the door to other problems where a complicated landscape prevents local search algorithms from finding good solutions. As a concrete example, a subset of the current authors [41] have recently shown that related ideas can be leveraged to perform lossy data compression at near-optimal (Shannon limit) rates.

# 1.2 Organization 

The remainder of this paper is organized in the following way:

- In Section 1.3, we provide further background on the $k$-SAT problem, as well as previous work on survey propagation.
- In Section 2, we introduce required notation and set up the problem more precisely.
- In Section 3, we define a family of Markov random fields (MRFs) over partial satisfiability assignments, and prove that survey propagation and related algorithms correspond to belief propagation on these MRFs.
- Section 4 is devoted to analysis of the combinatorial properties of this family of extended MRFs, as well as some experimental results on cores and Gibbs sampling.
- In Section 5, we consider properties of random ensembles of SAT formulae, and prove results that link the performance of survey propagation and Gibbs sampling to the choice of Markov random field.
- We conclude with a discussion in Section 6.

We note that many of the results reported here have been presented (without proofs or details) as an extended SODA abstract [26].

### 1.3 Previous work on $k$-SAT and survey propagation

As a classical NP complete problem [9], the $k$-SAT problem for $k \geq 3$ has been extensively studied. One approach is to consider ensembles of random formulas; in particular, a commonly studied ensemble is based on choosing $m=\alpha n$ clauses uniformly and with replacement from the set of all $k$-clauses on $n$ variables. Clearly, a formula drawn randomly from this ensemble becomes increasingly difficult to satisfy as the clause density $\alpha>0$ increases. There is a large body of

![img-1.jpeg](img-1.jpeg)

Figure 2. The black dots represent satisfying assignments, and white dots unsatisfying assignments. Distance is to be interpreted as the Hamming distance between assignments. (a) For low densities the space of satisfying assignments is well connected. (b) As the density increases above $\alpha_{d}$ the space is believed to break up into an exponential number of clusters, each containing an exponential number of assignments. These clusters are separated by a "sea" of unsatisfying assignments. (c) Above $\alpha_{c}$ all assignments become unsatisfying.

work $[18,20,8,13,15,22,1]$ devoted to the study of the threshold density where the formula becomes unsatisfiable; however, except for the case $k=2$, the value of the threshold is currently unknown. However, non-rigorous techniques from statistical physics can be applied to yield estimates of the threshold; for instance, results from Mézard and Zecchina [31] yield a threshold estimate of $\alpha_{c} \approx 4.267$ for $k=3$.

The survey propagation (SP) algorithm, as introduced by Mézard, Parisi and Zecchina [28], is an iterative message-passing technique that is able to find satisfying assignments for large instances of SAT problems at much higher densities than previous methods. The derivation of SP is based on the cavity method in conjunction with the 1-step replica summetry breaking (1-RSB) ansatz of statistical physics. We do not go into these ideas in depth here, but refer the reader to the physics literature $[30,6,28]$ for further details. In brief, the main assumption is the existence of a critical value $\alpha_{d}$ for the density, smaller than the threshold density $\alpha_{c}$, at which the structure of the space of solutions of a random formula changes. For densities below $\alpha_{d}$ the space of solutions is highly connected - in particular, it is possible to move from one solution to any other by single variable flips, ${ }^{1}$ staying at all times in a satisfying assignment. For densities above $\alpha_{d}$, the space of solutions breaks up into clusters, so that moving from a SAT assignment within one cluster to some other assignment within another cluster requires flipping some constant fraction of the variables simultaneously. Figure 2 illustrates how the structure of the space of solutions evolves as the density of a random formula increases. The clustering phenomenon that is believed to occur in the second phase is known in the statistical physics literature as 1-step replica symmetry breaking [30], and the estimated value for $\alpha_{d}$ in the case $k=3$ is $\alpha_{d} \approx 3.921$. Within each cluster, a distinction can be made between frozen variables - ones that do not change their value within the cluster - and free variables that do change their value in the cluster. A concise description of a cluster is an assignment of $\{0,1, *\}$ to the variables with the frozen variables taking their frozen

[^0]
[^0]:    ${ }^{1}$ There is no general agreement on whether assignments should be considered neighbors if they differ in only one variable, or any constant number of variables

value, and the free variables taking the joker or wild card value $*$. The original argument for the clustering assumption was the analysis of simpler satisfiability problems, such as XOR-SAT, where the existence of clusters can be demonstrated by rigorous methods [29]. In addition, if one assumes that there are no clusters, the cavity method calculation yields a value for $\alpha_{c}>5$ (for $k=3$ ), which is known to be wrong. More recently, Mora, Mézard and Zecchina [32] have demonstrated via rigorous methods that for $k \geq 8$ and some clause density below the unsatisfiability threshold, clusters of solutions do indeed exist.

The survey propagation (SP) algorithm is so-named, because like the belief propagation algorithm $[34,45]$, it entails propagating statistical information in the form of messages between nodes in the graph. In the original derivation of the updates [28, 6], the messages are interpreted as "surveys" taken over the clusters in solution space, which provide information about the fraction of clusters in which a given variable is free or frozen. However, prior to the work presented here, it was not clear how to interpret the algorithm as an instantiation of belief propagation, and thus as a method for computing (approximations) to marginal distributions in a certain Markov random field (MRF). Moreover, as discussed above, our formulation of SP in this manner provides a broader view, in which SP is one of many possible message-passing algorithms that can be applied to smoothed MRF representations of SAT problems.

# 2 Background and problem set-up 

In this section, we begin with notation and terminology necessary to describe the $k$-SAT problem, and then provide a precise description of the survey propagation updates.

### 2.1 The $k$-SAT problem and factor graphs

Basic notation: Let $C$ and $V$ represent index sets for the clauses and variables, respectively, where $|V|=n$ and $|C|=m$. We denote elements of $V$ using the letters $i, j, k$, etc., and members of $C$ with the letters $a, b, c$, etc. We use $x_{S}$ to denote the subset of variables $\left\{x_{i}: i \in S\right\}$. In the $k$-SAT problem, the clause indexed by $a \in C$ is specified by the pair $\left(V(a), J_{a}\right)$, where $V(a) \subset V$ consists of $k$ elements, and $J_{a}:=\left(J_{a, i}: i \in V(a)\right)$ is a $k$-tuple of $\{0,1\}$-valued weights. The clause indexed by $a$ is satisfied by the assignment $x$ if and only if $x_{V(a)} \neq J_{a}$. Equivalently, letting $\delta(y, z)$ denote an indicator function for the event $\{y=z\}$, if we define the function

$$
\psi_{J_{a}}(x):=1-\prod_{i \in V(a)} \delta\left(J_{a, i}, x_{i}\right)
$$

then the clause $a$ is satisfied by $x$ if and only if $\psi_{J_{a}}(x)=1$. The overall formula consists of the AND of all the individual clauses, and is satisfied by $x$ if and only if $\prod_{a \in C} \psi_{J_{a}}(x)=1$.

Factor graphs: A convenient graphical representation of any $k$-SAT problem is provided by the formalism of factor graphs (see [24] for further background). As illustrated in Figure 3, any instance of the $k$-SAT problem can be associated with a particular bipartite graph on the variables (denoted by circular nodes) and clauses (denoted by square nodes), where the edge $(a, i)$ between the clause $a \in C$ and variable $i \in V$ is included in $E$ if and only if $i \in V(a)$. Following Braunstein et al. [6], it is convenient to introduce two labellings of any given edge-namely, solid or dotted, corresponding to whether $J_{a, i}$ is equal to 0 or 1 respectively.

![img-2.jpeg](img-2.jpeg)

Figure 3. Factor graph representation of a 3-SAT problem on $n=5$ variables with $m=4$ clauses, in which circular and square nodes correspond to variables and clauses respectively. Solid and dotted edges $(a, i)$ correspond to the weightings $J_{a, i}=0$ and $J_{a, i}=1$ respectively. The clause $a$ is defined by the neighborhood set $V(a)=\{1,2,3\}$ and weights $J_{a}=(0,1,1)$. In traditional notation, this corresponds to the formula $\left(x_{1} \vee \bar{x}_{2} \vee \bar{x}_{3}\right) \wedge\left(\bar{x}_{1} \vee x_{2} \vee x_{4}\right) \wedge\left(\bar{x}_{2} \vee x_{3} \vee x_{5}\right) \wedge\left(\bar{x}_{2} \vee x_{4} \vee x_{5}\right)$.

For later use, we define (for each $i \in V$ ) the set $C(i):=\{a \in C: i \in V(a)\}$, corresponding to those clauses that impose constraints on variable $x_{i}$. This set of clauses can be decomposed into two disjoint subsets

$$
C^{-}(i):=\left\{a \in C(i): J_{a, i}=1\right\}, \quad C^{+}(i):=\left\{a \in C(i): J_{a, i}=0\right\}
$$

according to whether the clause is satisfied by $x_{i}=0$ or $x_{i}=1$ respectively. Moreover, for each pair $(a, i) \in E$, the set $C(i) \backslash\{a\}$ can be divided into two (disjoint) subsets, depending on whether their preferred assignment of $x_{i}$ agrees (in which case $b \in C_{a}^{s}(i)$ ) or disagrees (in which case $b \in C_{a}^{u}(i)$ ) with the preferred assignment of $x_{i}$ corresponding to clause $a$. More formally, we define

$$
C_{a}^{s}(i):=\{b \in C(i) \backslash\{a\}: J_{a, i}=J_{b, i}\}, \quad C_{a}^{u}(i):=\left\{b \in C(i) \backslash\{a\}: J_{a, i} \neq J_{b, i}\right\}
$$

Our focus is on random ensembles of $k$-SAT instances: for a given clause density $\alpha>0$, a random instance is obtained by sampling $m=\alpha n$ clauses uniformly and with replacement from the set of all $k$-clauses on $n$ variables. In terms of the factor graph representation, this procedure samples a random $(n, m)$-bipartite graph, in which each clause $a \in C$ has degree $k$.

Markov random fields and marginalization: The $k$-SAT problem can also be associated with a particular distribution defined as a Markov random field. Recall that a given instance of $k$-SAT can be specified by the collection of clause functions $\left\{\psi_{J_{a}}: a \in C\right\}$, as defined in equation (1). Using these functions, let us define a probability distribution over binary sequences via

$$
p(x):=\frac{1}{Z} \prod_{a \in C} \psi_{J_{a}}(x)
$$

where $Z:=\sum_{x \in\{0,1\}^{n}} \prod_{a \in C} \psi_{J_{a}}(x)$ is the normalization constant Note that this definition makes sense if and only if the $k$-SAT instance is satisfiable, in which case the distribution (4) is simply the uniform distribution over satisfying assignments.

This Markov random field representation (4) of any satisfiable formula motivates a marginalizationbased approach to finding a satisfying assignment. In particular, suppose that we had an oracle that could compute exactly the marginal probability

$$
p\left(x_{i}\right)=\sum_{\left\{x_{j}, j \in V \backslash\{i\}\right\}} p\left(x_{1}, x_{2}, \ldots, x_{n}\right)
$$

for a particular variable $x_{i}$. Note that this marginal reveals the existence of SAT configurations with $x_{i}=0$ (if $p\left(x_{i}=0\right)>0$ ) or $x_{i}=1$ (if $p\left(x_{i}=1\right)>0$ ). Therefore, a SAT configuration could be obtained by a recursive marginalization-decimation procedure, consisting of computing the marginal $p\left(x_{i}\right)$, appropriately setting $x_{i}$ (i.e., decimating), and then re-iterating the modified Markov random field.

Of course, exact marginalization is computationally intractable in general [10, 12], which motivates the use of efficient algorithms for approximate marginalization. An example of such an algorithm is what we will refer to as the "naive belief propagation algorithm". The belief propagation (BP) algorithm, described in detail in Appendix A, can be applied to a MRF of the form 4 to estimate the marginal probabilities. Even though the BP algorithm is not exact, an intuitively reasonable approach is to set the variable that has the largest bias towards a particular value, and repeat. In fact, this marginalization-decimation approach based on naive BP finds a satisfying assignment for $\alpha$ up to approximately 3.9 for $k=3$; for higher $\alpha$, however, the iterations for BP typically fail to converge $[28,3,6]$.

# 2.2 Survey propagation 

In contrast to the naive BP approach, a marginalization-decimation approach based on survey propagation appears to be effective in solving random $k$-SAT problems even close to threshold [28, 6]. Here we provide an explicit description of what we refer to as the $\mathrm{SP}(\rho)$ family of algorithms, where setting the parameter $\rho=1$ yields the pure form of survey propagation. For any given $\rho \in[0,1]$, the algorithm involves updating messages from clauses to variables, as well as from variables to clauses. Each clause $a \in C$ passes a real number $\eta_{a \rightarrow i} \in[0,1]$ to each of its variable neighbors $i \in V(a)$. In the other direction, each variable $i \in V$ passes a triplet of real numbers $\Pi_{i \rightarrow a}=\left(\Pi_{i \rightarrow a}^{u}, \Pi_{i \rightarrow a}^{s}, \Pi_{i \rightarrow a}^{*}\right)$ to each of its clause neighbors $a \in C(i)$. The precise form of the updates are given in Figure 4.

Message from clause $a$ to variable $i$ :

$$
\eta_{a \rightarrow i}=\prod_{j \in V(a) \backslash\{i\}}\left[\frac{\Pi_{j \rightarrow a}^{u}}{\Pi_{j \rightarrow a}^{u}+\Pi_{j \rightarrow a}^{s}+\Pi_{j \rightarrow a}^{*}}\right]
$$

Message from variable $i$ to clause $a$ :

$$
\begin{aligned}
& \Pi_{i \rightarrow a}^{u}=\left[1-\rho \prod_{b \in C_{a}^{u}(i)}\left(1-\eta_{b \rightarrow i}\right)\right] \prod_{b \in C_{a}^{s}(i)}\left(1-\eta_{b \rightarrow i}\right) \\
& \Pi_{i \rightarrow a}^{s}=\left[1-\prod_{b \in C_{a}^{s}(i)}\left(1-\eta_{b \rightarrow i}\right)\right] \prod_{b \in C_{a}^{u}(i)}\left(1-\eta_{b \rightarrow i}\right) \\
& \Pi_{i \rightarrow a}^{s}=\prod_{b \in C_{a}^{s}(i)}\left(1-\eta_{b \rightarrow i}\right) \prod_{b \in C_{a}^{u}(i)}\left(1-\eta_{b \rightarrow i}\right)
\end{aligned}
$$

Figure 4: $\mathrm{SP}(\rho)$ updates
We pause to make a few comments about these $\mathrm{SP}(\rho)$ updates:

1. Although we have omitted the time step index for simplicity, equations (6) and (7) should be interpreted as defining a recursion on $(\eta, \Pi)$. The initial values for $\eta$ are chosen randomly in the interval $(0,1)$.
2. The idea of the $\rho$ parameter is to provide a smooth transition from the original naive belief propagation algorithm to the survey propagation algorithm. As shown in [6], setting $\rho=0$ yields the belief propagation updates applied to the probability distribution (4), whereas setting $\rho=1$ yields the pure version of survey propagation.

# 2.2.1 Intuitive "warning" interpretation 

To gain intuition for these updates, it is helpful to consider the pure SP setting of $\rho=1$. As described by Braunstein et al. [6], the messages in this case have a natural interpretation in terms of probabilities of warnings. In particular, at time $t=0$, suppose that the clause $a$ sends a warning message to variable $i$ with probability $\eta_{a \rightarrow i}^{0}$, and a message without a warning with probability $1-\eta_{a \rightarrow i}^{0}$. After receiving all messages from clauses in $C(i) \backslash\{a\}$, variable $i$ sends a particular symbol to clause $a$ saying either that it can't satisfy it ("u"), that it can satisfy it ("s"), or that it is indifferent (" $*$ "), depending on what messages it got from its other clauses. There are four cases:

1. If variable $i$ receives warnings from $C_{a}^{u}(i)$ and no warnings from $C_{a}^{s}(i)$, then it cannot satisfy $a$ and sends "u".
2. If variable $i$ receives warnings from $C_{a}^{s}(i)$ but no warnings from $C_{a}^{u}(i)$, then it sends an "s" to indicate that it is inclined to satisfy the clause $a$.
3. If variable $i$ receives no warnings from either $C_{a}^{u}(i)$ or $C_{a}^{s}(i)$, then it is indifferent and sends "*".
4. If variable $i$ receives warnings from both $C_{a}^{u}(i)$ and $C_{a}^{s}(i)$, a contradiction has occurred.

The updates from clauses to variables are especially simple: in particular, any given clause sends a warning if and only if it receives "u" symbols from all of its other variables.

In this context, the real-valued messages involved in the pure $\mathrm{SP}(1)$ all have natural probabilistic interpretations. In particular, the message $\eta_{a \rightarrow i}$ corresponds to the probability that clause $a$ sends a warning to variable $i$. The quantity $\Pi_{j \rightarrow a}^{u}$ can be interpreted as the probability that variable $j$ sends the "u" symbol to clause $a$, and similarly for $\Pi_{j \rightarrow a}^{s}$ and $\Pi_{j \rightarrow a}^{*}$. The normalization by the sum $\Pi_{j \rightarrow a}^{u}+\Pi_{j \rightarrow a}^{s}+\Pi_{j \rightarrow a}^{*}$ reflects the fact that the fourth case is a failure, and hence is excluded a priori from the probability distribution

Suppose that all of the possible warning events were independent. In this case, the SP message update equations (6) and (7) would be the correct estimates for the probabilities. This independence assumption is valid on a graph without cycles, and in that case the SP updates do have a rigorous probabilistic interpretation. It is not clear if the equations have a simple interpretation in the case $\rho \neq 1$.

# 2.2.2 Decimation based on survey propagation 

Supposing that these survey propagation updates are applied and converge, the overall conviction of a value at a given variable is computed from the incoming set of equilibrium messages as

$$
\begin{aligned}
& \mu_{i}(1) \propto\left[1-\rho \prod_{b \in C^{+}(j)}\left(1-\eta_{b \rightarrow j}\right)\right] \prod_{b \in C^{-}(j)}\left(1-\eta_{b \rightarrow j}\right) \\
& \mu_{i}(0) \propto\left[1-\rho \prod_{b \in C^{-}(j)}\left(1-\eta_{b \rightarrow j}\right)\right] \prod_{b \in C^{+}(j)}\left(1-\eta_{b \rightarrow j}\right) \\
& \mu_{i}(*) \propto \prod_{b \in C^{+}(j)}\left(1-\eta_{b \rightarrow j}\right) \prod_{b \in C^{-}(j)}\left(1-\eta_{b \rightarrow j}\right)
\end{aligned}
$$

To be consistent with their interpretation as (approximate) marginals, the triplet $\left\{\mu_{i}(0), \mu_{i}(*), \mu_{i}(1)\right\}$ at each node $i \in V$ is normalized to sum to one. We define the bias of a variable node as $B(i):=\left|\mu_{i}(0)-\mu_{i}(1)\right|$.

The marginalization-decimation algorithm based on survey propagation [6] consists of the following steps:

1. Run $\mathrm{SP}(1)$ on the SAT problem. Extract the fraction $\beta$ of variables with the largest biases, and set them to their preferred values.
2. Simplify the SAT formula, and return to Step 1.

Once the maximum bias over all variables falls below a pre-specified tolerance, the Walk-SAT algorithm is applied to the formula to find the remainder of the assignment (if possible). Intuitively, the goal of the initial phases of decimation is to find a cluster; once inside the cluster, the induced problem is considered easy to solve, meaning that any "local" algorithm should perform well within a given cluster.

## 3 Markov random fields over partial assignments

In this section, we show how a large class of message-passing algorithms-including the $\mathrm{SP}(\rho)$ family as a particular case - can be recovered by applying the well-known belief propagation algorithm to a novel class of Markov random fields (MRFs) associated with any $k$-SAT problem. We begin by introducing the notion of a partial assignment, and then use it to define the family of MRFs over these assignments.

### 3.1 Partial assignments

Suppose that the variables $x=\left\{x_{1}, \ldots, x_{n}\right\}$ are allowed to take values in $\{0,1, *\}$, which we refer to as a partial assignment. It will be convenient, when discussing the assignment of a variable $x_{i}$ with respect to a particular clause $a$, to use the notation $s_{a, i}:=1-J_{a, i}$ and $u_{a, i}:=J_{a, i}$ to indicate, respectively, the values that are satisfying and unsatisfying for the clause $a$. With this set-up, we have the following:

Definition 1. A partial assignment $x$ is invalid for a clause a if either
(a) all variables are unsatisfying (i.e., $x_{i}=u_{a, i}$ for all $i \in V(a)$ ), or
(b) all variables are unsatisfying except for exactly one index $j \in V(a)$, for which $x_{j}=*$.

Otherwise, the partial assignment $x$ is valid for clause $a$, and we denote this event by $\mathrm{VAL}_{a}\left(x_{V(a)}\right)$. We say that a partial assignment is valid for a formula if it is valid for all of its clauses.

The motivation for deeming case (a) invalid is clear, in that any partial assignment that does not satisfy the clause must be excluded. Note that case (b) is also invalid, since (with all other variables unsatisfying) the variable $x_{j}$ is effectively forced to $s_{a, i}$, and so cannot be assigned the $*$ symbol.

For a valid partial assignment, the subset of variables that are assigned either 0 or 1 values can be divided into constrained and unconstrained variables in the following way:

Definition 2. We say that a variable $x_{i}$ is the unique satisfying variable for a clause if it is assigned $s_{a, i}$ whereas all other variables in the clause (i.e., the variables $\left\{x_{j}: j \in V(a) \backslash\{i\}\right\}$ ) are assigned $u_{a, j}$. A variable $x_{i}$ is constrained by clause $a$ if it is the unique satisfying variable.

We let $\operatorname{CON}_{i, a}\left(x_{V(a)}\right)$ denote an indicator function for the event that $x_{i}$ is the unique satisfying variable in the partial assignment $x_{V(a)}$ for clause $a$. A variable is unconstrained if it has 0 or 1 value, and is not constrained. Thus for any partial assignment the variables are divided into stars, constrained and unconstrained variables. We define the three sets

$$
S_{*}(x):=\left\{i \in V: x_{i}=*\right\} \quad S_{c}(x):=\left\{i \in V: x_{i} \text { constrained }\right\} \quad S_{o}(x):=\left\{i \in V: x_{i} \text { unconstrained }\right\}
$$

of $*$, constrained and unconstrained variables respectively. Finally, we use $n_{*}(x), n_{c}(x)$ and $n_{o}(x)$ to denote the respective sizes of these three sets.

Various probability distributions can be defined on valid partial assignments by giving different weights to stars, constrained and unconstrained variables, which we denote by $\omega_{c}, \omega_{*}$ and $\omega_{o}$ respectively. Since only the ratio of the weights matters, we set $\omega_{c}=1$, and treat $\omega_{o}$ and $\omega_{*}$ as free non-negative parameters (we generally take them in the interval $[0,1]$ ). We define the weights of partial assignments in the following way: invalid assignments $x$ have weight $W(x)=0$, and for any valid assignment $x$, we set

$$
W(x):=\left(\omega_{o}\right)^{n_{o}(x)} \times\left(\omega_{*}\right)^{n_{*}(x)}
$$

Our primary interest is the probability distribution given by $p_{W}(x) \propto W(x)$. In contrast to the earlier distribution $p$, it is important to observe that this definition is valid for any SAT problem, whether or not it is satisfiable, as long as $\omega_{*} \neq 0$, since the all-* vector is always a valid partial assignment. Note that if $\omega_{o}=1$ and $\omega_{*}=0$ then the distribution $p_{W}(x)$ is the uniform distribution on satisfying assignments. Another interesting case that we will discuss is that of $\omega_{o}=0$ and $\omega_{*}=1$, which corresponds to the uniform distribution over valid partial assignments without unconstrained variables.

# 3.2 Associated Markov random fields 

Given our set-up thus far, it is not at all obvious whether or not the distribution $p_{W}$ can be decomposed as a Markov random field based on the original factor graph. Interestingly, we find that $p_{W}$ does indeed have such a Markov representation for any choices of $\omega_{o}, \omega_{*} \in[0,1]$. Obtaining this representation requires the addition of another dimension to our representation, which allows us to assess whether a given variable is constrained or unconstrained. We define the parent set of a given variable $x_{i}$, denoted by $P_{i}$, to be the set of clauses for which $x_{i}$ is the unique satisfying variable. Immediate consequences of this definition are the following:
(a) If $x_{i}=0$, then we must have $P_{i} \subseteq C^{-}(i)$.
(b) If $x_{i}=1$, then there must hold $P_{i} \subseteq C^{+}(i)$.
(c) The setting $x_{i}=*$ implies that $P_{i}=\emptyset$.

Note also that $P_{i}=\emptyset$ means that $x_{i}$ cannot be constrained. For each $i \in V$, let $\mathcal{P}(i)$ be the set of all possible parent sets of variable $i$. Due to the restrictions imposed by our definition, $P_{i}$ must be contained in either $C^{+}(i)$ or $C^{-}(i)$ but not both. Therefore, the cardinality ${ }^{2}$ of $\mathcal{P}(i)$ is $2^{\left|C^{-}(i)\right|}+2^{\left|C^{+}(i)\right|}-1$.

Our extended Markov random field is defined on the Cartesian product space $\mathcal{X}_{1} \times \ldots \times \mathcal{X}_{n}$, where $\mathcal{X}_{i}:=\{0,1, *\} \times \mathcal{P}(i)$. The distribution factorizes as a product of compatibility functions at the variable and clause nodes of the factor graph, which are defined as follows:

Variable compatibilities: Each variable node $i \in V$ has an associated compatibility function of the form:

$$
\Psi_{i}\left(x_{i}, P_{i}\right):=\left\{\begin{array}{rll}
\omega_{o} & : & P_{i}=\emptyset, x_{i} \neq * \\
\omega_{*} & : & P_{i}=\emptyset, x_{i}=* \\
1 & : & \text { for any other valid }\left(P_{i}, x_{i}\right)
\end{array}\right.
$$

The role of these functions is to assign weight to the partial assignments according to the number of unconstrained and star variables, as in the weighted distribution $p_{W}$.

Clause compatibilities: The compatibility functions at the clause nodes serve to ensure that only valid assignments have non-zero probability, and that the parent sets $P_{V(a)}:=\left\{P_{i}: i \in V(a)\right\}$ are consistent with the assignments $x_{V(a)}:=\left\{x_{i}: i \in V(a)\right\}$ in the neighborhood of $a$. More precisely, we require that the partial assignment $x_{V(a)}$ is valid for $a$ (i.e., $\operatorname{VAL}_{a}\left(x_{V(a)}\right)=1$ ) and that for each $i \in V(a)$, exactly one of the two following conditions holds:
(a) $a \in P_{i}$ and $x_{i}$ is constrained by $a$ or
(b) $a \notin P_{i}$ and $x_{i}$ is not constrained by $a$.

The following compatibility function corresponds to an indicator function for the intersection of these events:

$$
\Psi_{a}\left(x_{V(a)}, P_{V(a)}\right):=\operatorname{VAL}_{a}\left(x_{V(a)}\right) \times \prod_{i \in V(a)} \delta\left(\operatorname{Ind}\left[a \in P_{i}\right], \operatorname{CON}_{a, i}\left(x_{V(a)}\right)\right)
$$

[^0]
[^0]:    ${ }^{2}$ Note that it is necessary to subtract one so as not to count the empty set twice.

We now form a Markov random field over partial assignments and parent sets by taking the product of variable (10) and clause (11) compatibility functions

$$
p_{g e n}(x, P) \propto \prod_{i \in V} \Psi_{i}\left(x_{i}, P_{i}\right) \prod_{a \in C} \Psi_{a}\left(x_{V_{a}}, P_{V(a)}\right)
$$

With these definitions, some straightforward calculations show that $p_{g e n}=p_{W}$.

# 3.3 Survey propagation as an instance of belief propagation 

We now consider the form of the belief propagation (BP) updates as applied to the MRF $p_{g e n}$ defined by equation (12). We refer the reader to Section A for the definition of the BP algorithm on a general factor graph. The main result of this section is to establish that the $\mathrm{SP}(\rho)$ family of algorithms are equivalent to belief propagation as applied to $p_{g e n}$ with suitable choices of the weights $\omega_{o}$ and $\omega_{*}$. In the interests of readability, most of the technical lemmas will be presented in the appendix.

We begin by introducing some notation necessary to describe the BP updates on the extended MRF. The BP message from clause $a$ to variable $i$, denoted by $M_{a \rightarrow i}(\cdot)$, is a vector of length $\left|\mathcal{X}_{i}\right|=3 \times|\mathcal{P}(i)|$. Fortunately, due to symmetries in the variable and clause compatibilities defined in equations (10) and (11), it turns out that the clause-to-variable message can be parameterized by only three numbers, $\left\{M_{a \rightarrow i}^{u}, M_{a \rightarrow i}^{s}, M_{a \rightarrow i}^{*}\right\}$, as follows:

$$
M_{a \rightarrow i}\left(x_{i}, P_{i}\right)= \begin{cases}M_{a \rightarrow i}^{s} & \text { if } x_{i}=s_{a, i}, P_{i}=S \cup\{a\} \text { for some } S \subseteq C_{a}^{s}(i) \\ M_{a \rightarrow i}^{u} & \text { if } x_{i}=u_{a, i}, P_{i} \subseteq C_{a}^{u}(i) \\ M_{a \rightarrow i}^{s} & \text { if } x_{i}=s_{a, i}, P_{i} \subseteq C_{a}^{s}(i) \text { or } x_{i}=*, P_{i}=\emptyset \\ 0 & \text { otherwise. }\end{cases}
$$

where $M_{a \rightarrow i}^{s}, M_{a \rightarrow i}^{u}$ and $M_{a \rightarrow i}^{*}$ are elements of $[0,1]$.
Now turning to messages from variables to clauses, it is convenient to introduce the notation $P_{i}=S \cup\{a\}$ as a shorthand for the event

$$
a \in P_{i} \quad \text { and } \quad S=P_{i} \backslash\{a\} \subseteq C_{a}^{s}(i)
$$

where it is understood that $S$ could be empty. In Appendix B, we show that the variable-to-clause message $M_{i \rightarrow a}$ is fully specified by values for pairs $\left(x_{i}, P_{i}\right)$ of six general types:

$$
\left\{\left(s_{a, i}, S \cup\{a\}\right),\left(s_{a, i}, \emptyset \neq P_{i} \subseteq C_{a}^{s}(i)\right),\left(u_{a, i}, \emptyset \neq P_{i} \subseteq C_{a}^{u}(i)\right),\left(s_{a, i}, \emptyset\right),\left(u_{a, i}, \emptyset\right),(*, \emptyset)\right\}
$$

The BP updates themselves are most compactly expressed in terms of particular linear combinations of such basic messages, defined in the following way:

$$
\begin{aligned}
R_{i \rightarrow a}^{s} & :=\sum_{S \subseteq C_{a}^{s}(i)} M_{i \rightarrow a}\left(s_{a, i}, S \cup\{a\}\right) \\
R_{i \rightarrow a}^{u} & :=\sum_{P_{i} \subseteq C_{a}^{u}(i)} M_{i \rightarrow a}\left(u_{a, i}, P_{i}\right) \\
R_{i \rightarrow a}^{*} & :=\sum_{P_{i} \subseteq C_{a}^{u}(i)} M_{i \rightarrow a}\left(s_{a, i}, P_{i}\right)+M_{i \rightarrow a}(*, \emptyset)
\end{aligned}
$$

Note that $R_{i \rightarrow a}^{s}$ is associated with the event that $x_{i}$ is the unique satisfying variable for clause $a ; R_{i \rightarrow a}^{u}$ with the event that $x_{i}$ does not satisfy $a$; and $R_{i \rightarrow a}^{s}$ with the event that $x_{i}$ is neither unsatisfying nor uniquely satisfying (i.e., either $x_{i}=*$, or $x_{i}=s_{a, i}$ but is not the only variable that satisfies $a$ ).

With this terminology, the BP algorithm on the extended MRF can be expressed in terms of the following recursions on the triplets $\left(M_{a \rightarrow i}^{s}, M_{a \rightarrow i}^{u}, M_{a \rightarrow i}^{*}\right)$ and $\left(R_{i \rightarrow a}^{s}, R_{i \rightarrow a}^{u}, R_{i \rightarrow a}^{s}\right)$ :

# BP updates on extended MRF: 

Messages from clause a to variable $i$

$$
\begin{aligned}
& M_{a \rightarrow i}^{s}=\prod_{j \in C(a) \backslash\{i\}} R_{j \rightarrow a}^{u} \\
& M_{a \rightarrow i}^{u}=\prod_{j \in C(a) \backslash\{i\}}\left(R_{j \rightarrow a}^{u}+R_{j \rightarrow a}^{*}\right)+\sum_{k \in C(a) \backslash\{i\}}\left(R_{k \rightarrow a}^{s}-R_{k \rightarrow a}^{*}\right) \prod_{j \in C(a) \backslash\{i, k\}} R_{j \rightarrow a}^{u}-\prod_{j \in C(a) \backslash\{i\}} R_{j \rightarrow a}^{u} \\
& M_{a \rightarrow i}^{*}=\prod_{j \in C(a) \backslash\{i\}}\left(R_{j \rightarrow a}^{u}+R_{j \rightarrow a}^{*}\right)-\prod_{j \in C(a) \backslash\{i\}} R_{j \rightarrow a}^{u}
\end{aligned}
$$

Messages from variable $i$ to clause $a$ :

$$
\begin{aligned}
& R_{i \rightarrow a}^{s}=\prod_{b \in C_{a}^{w}(i)} M_{b \rightarrow i}^{u}\left[\prod_{b \in C_{a}^{w}(i)}\left(M_{b \rightarrow i}^{s}+M_{b \rightarrow i}^{*}\right)\right] \\
& R_{i \rightarrow a}^{u}=\prod_{b \in C_{a}^{v}(i)} M_{b \rightarrow i}^{u}\left[\prod_{b \in C_{a}^{w}(i)}\left(M_{b \rightarrow i}^{s}+M_{b \rightarrow i}^{*}\right)-\left(1-\omega_{o}\right) \prod_{b \in V_{a}^{w}(i)} M_{b \rightarrow i}^{*}\right] \\
& R_{i \rightarrow a}^{*}=\prod_{b \in C_{a}^{w}(i)} M_{b \rightarrow i}^{u}\left[\prod_{b \in C_{a}^{v}(i)}\left(M_{b \rightarrow i}^{s}+M_{b \rightarrow i}^{*}\right)-\left(1-\omega_{o}\right) \prod_{b \in C_{a}^{v}(i)} M_{b \rightarrow i}^{*}\right]+\omega_{*} \prod_{b \in C_{a}^{i}(i) \cup C_{a}^{w}(i)} M_{b \rightarrow i}^{*}
\end{aligned}
$$

We provide a detailed derivation of these BP equations on the extended MRF in Appendix B. Since the messages are interpreted as probabilities, we only need their ratio, and we can normalize them to any constant. At any iteration, approximations to the local marginals at each variable node $i \in V$ are given by (up to a normalization constant):

$$
\begin{aligned}
& F_{i}(0) \propto \prod_{b \in C^{+}(i)} M_{b \rightarrow i}^{u}\left[\prod_{b \in C^{-}(i)}\left(M_{b \rightarrow i}^{s}+M_{b \rightarrow i}^{*}\right)-\left(1-\omega_{o}\right) \prod_{b \in C^{-}(i)} M_{b \rightarrow i}^{*}\right] \\
& F_{i}(1) \propto \prod_{b \in C^{-}(i)} M_{b \rightarrow i}^{u}\left[\prod_{b \in C^{+}(i)}\left(M_{b \rightarrow i}^{s}+M_{b \rightarrow i}^{*}\right)-\left(1-\omega_{o}\right) \prod_{b \in C^{+}(i)} M_{b \rightarrow i}^{*}\right] \\
& F_{i}(*) \propto \omega_{*} \prod_{b \in C(i)} M_{b \rightarrow i}^{*}
\end{aligned}
$$

The following theorem establishes that the $\mathrm{SP}(\rho)$ family of algorithms is equivalent to belief propagation on the extended MRF:

Theorem 3. For all $\omega_{*} \in[0,1]$, the $B P$ updates on the extended $\left(\omega_{*}, \omega_{o}\right)$-MRF $p_{\text {gen }}$ are equivalent to the $\mathrm{SP}\left(\omega_{*}\right)$ family of algorithms under the following restrictions:
(a) the constraint $\omega_{o}+\omega_{*}=1$ is imposed, and

(b) all messages are initialized such that $M_{a \rightarrow i}^{u}=M_{a \rightarrow i}^{*}$ for every edge $(a, i)$.

Proof. Under the constraint $\omega_{o}+\omega_{*}=1$, if we initialize $M_{a \rightarrow i}^{u}=M_{a \rightarrow i}^{*}$ on every edge, then there holds $R_{i \rightarrow a}^{s}=R_{i \rightarrow a}^{*}$ and consequently $M_{a \rightarrow i}^{u}=M_{a \rightarrow i}^{*}$ remains true at the next iteration. Initializing the parameters in this way and imposing the normalization $M_{a \rightarrow i}^{u}+M_{a \rightarrow i}^{*}=1$ leads to the following recurrence equations:

$$
M_{a \rightarrow i}^{s}=\frac{\prod_{j \in C(a) \backslash\{i\}} R_{j \rightarrow a}^{u}}{\prod_{j \in C(a) \backslash\{i\}}\left(R_{j \rightarrow a}^{s}+R_{j \rightarrow a}^{u}\right)}
$$

where:

$$
\begin{aligned}
& R_{i \rightarrow a}^{u}=\prod_{b \in C_{a}^{s}(i)}\left(1-M_{b \rightarrow i}^{s}\right)\left[1-\omega_{*} \prod_{b \in C_{a}^{u}(i)}\left(1-M_{b \rightarrow i}^{s}\right)\right] \\
& R_{i \rightarrow a}^{*}=\prod_{b \in C_{a}^{u}(i)}\left(1-M_{b \rightarrow i}^{s}\right)
\end{aligned}
$$

These updates are equivalent to $\operatorname{SP}\left(\omega_{*}\right)$ by setting $\eta_{a \rightarrow i}=M_{a \rightarrow i}^{s}, \Pi_{i \rightarrow a}^{u}=R_{i \rightarrow a}^{u}$, and $\Pi_{i \rightarrow a}^{s}+\Pi_{i \rightarrow a}^{s}=$ $R_{i \rightarrow a}^{s}$.

# Remarks: 

1. Theorem 3 is a generalization of the result of Braunstein and Zecchina [7], who showed that $\mathrm{SP}(1)$ is equivalent to belief propagation on a certain MRF.
2. The essence of Theorem 3 is that the pure survey propagation algorithm, as well as all the $\rho$-variants thereof, are all equivalent to belief propagation on our extended MRF with suitable parameter choices. This equivalence is important for a number of reasons:
(a) Belief propagation is a widely-used algorithm for computing approximations to marginal distributions in general Markov random fields [45, 24]. It also has a variational interpretation as an iterative method for attempting to solve a non-convex optimization problem based on the Bethe approximation [45]. Among other consequences, this variational interpretation leads to other algorithms that also solve the Bethe problem, but unlike belief propagation, are guaranteed to converge [43, 46, 40].
(b) Given the link between SP and extended MRFs, it is natural to study combinatorial and probabilistic properties of the latter objects. In Section 4, we show how so-called "cores" arise as fixed points of $\mathrm{SP}(1)$, and we prove a weight-preserving identity that shows how the extended MRF for general $\rho$ is a "smoothed" version of the naive MRF.
(c) Finally, since BP (and hence SP) is computing approximate marginals for the MRF, it is natural to study other ways of computing marginals and examine if these lead to an effective way for solving random $k$-SAT problems. We begin this study in Section 4.5.
3. The initial messages have very small influence on the behavior of the algorithm, and they are typically chosen to be uniform random variables in $(0,1)$. In practice, for $\omega_{o}+\omega_{*}=1$ if we start with different values for $M_{a \rightarrow i}^{u}$ and $M_{a \rightarrow i}^{*}$ they soon converge to become equal.

4. If we restrict our attention to 3-SAT, the equations have simpler form. In particular for a clause $a$ on $x_{i}, x_{j}, x_{k}$, the messages to variable node $i$ are:

$$
\begin{aligned}
& M_{a \rightarrow i}^{*}=R_{j \rightarrow a}^{u} R_{k \rightarrow a}^{u} \\
& M_{a \rightarrow i}^{u}=R_{j \rightarrow a}^{*} R_{k \rightarrow a}^{*}+R_{j \rightarrow a}^{s} R_{k \rightarrow a}^{u}+R_{j \rightarrow a}^{u} R_{k \rightarrow a}^{s} \\
& M_{a \rightarrow i}^{*}=R_{j \rightarrow a}^{*} R_{k \rightarrow a}^{*}+R_{j \rightarrow a}^{s} R_{k \rightarrow a}^{u}+R_{j \rightarrow a}^{u} R_{k \rightarrow a}^{*}
\end{aligned}
$$

# 4 Combinatorial properties 

This section is devoted to an investigation of the combinatorial properties associated with the family of extended Markov random fields defined in the previous section. We begin by defining an acyclic directed graph on all valid partial assignments. Of particular interest are the minimal elements in the resulting partial ordering. We refer to these as cores.

### 4.1 Directed graph and partial ordering

The vertex set of the directed graph $G$ consists of all valid partial assignments. The edge set is defined in the following way: for a given pair of valid partial assignments $x$ and $y$, the graph includes a directed edge from $x$ to $y$ if there exists an index $i \in V$ such that (i) $x_{j}=y_{j}$ for all $j \neq i$; and (ii) $y_{i}=*$ and $x_{i} \neq y_{i}$. We label the edge between $x$ and $y$ with the index $i$, corresponding to the fact that $y$ is obtained from $x$ by adding one extra $*$ in position $i$.

This directed graph $G$ has a number of properties:
(a) Valid partial assignments can be separated into different levels based on their number of star variables. In particular, assignment $x$ is in level $n_{*}(x)$. Thus, every edge is from an assignment in level $l-1$ to one in level $l$, where $l$ is at most $n$.
(b) The out-degree of any valid partial assignment $x$ is exactly equal to its number of unconstrained variables $n_{o}(x)$.
(c) It is an acyclic graph so that its structure defines a partial ordering; in particular, we write $y<x$ if there is a directed path in $G$ from $x$ to $y$. Notice that all directed paths from $x$ to $y$ are labeled by indices in the set $T=\left\{i \in V: x_{i} \neq y_{i}=*\right\}$, and only the order in which they appear is different.

Given the partial ordering defined by $G$, it is natural to consider elements that are minimal in this partial ordering. For any valid partial assignment $x$ and a subset $S \subseteq V$, let $\gamma_{S}(x)$ be the minimal $y<x$, such that the path from $x$ to $y$ is labeled only by indices in $S$. In particular $\gamma_{V}(x)$ is a minimal assignment in the order. It is easy to show that there always exists a unique $\gamma_{S}(x)$.

Proposition 4. For any valid assignment $x$ and $S \subseteq V$, there is a unique minimal $y<x$ such that the path from $x$ to $y$ is labeled only by indices in $S$. Furthermore $S_{o}(y) \cap S=\emptyset$ and $S_{*}(y)=S_{*}(x) \cup T$, where $T \subseteq S$ is the set of labels on any path from $x$ to $y$.

Proof. To prove the second assertion in the proposition statement for a minimal $y$, suppose there exists $i \in S \cap S_{o}(y)$. Then there must be be an outgoing edge from $y$ labeled by an element in $S$, which contradicts the assumed minimality of $y$. The equivalence $S_{*}(y)=S_{*}(x) \cup T$ follows directly from the definition of $G$ and its edge labels.

To establish the uniqueness statement, suppose that there are two minimal such assignments $y_{1}$ and $y_{2}$, and the paths from $x$ to $y_{1}$ and $y_{2}$ are labeled by sets of indices $T_{1}, T_{2} \subseteq S$ respectively. If $T_{1}=T_{2}$ then $y_{1}=y_{2}$, so let us assume that $T_{1}$ and $T_{2}$ are distinct. Without loss of generality, we may take $T_{1} \backslash T_{2} \neq \emptyset$. Consider a particular path from $x$ to $y_{1}$, with labels $t_{1}, t_{2}, \ldots t_{r}$, where $r=\left|T_{1}\right|$. Let $t_{i}$ be the first label such that $t_{i} \notin T_{2}$. Then its corresponding variable is unconstrained when the variables indexed by $\left\{t_{1}, \ldots t_{i-1}\right\} \cup S_{*}(x) \subseteq T_{2} \cup S_{*}(x)$ are assigned $*$, therefore it is unconstrained in $y_{2}$. This implies that there exists an edge out of $y_{2}$ that is labeled by $t_{i} \in S$, which contradicts the assumption that $y_{2}$ is minimal.

We define a core assignment to be a valid partial assignment $y \in\{0,1, *\}^{n}$ that contains no unconstrained variables. We say that a core assignment $y$ is non-trivial if $n_{*}(y)<n$, so that it has at least one constrained $\{0,1\}$ variable. Under this definition, it follows that for any partial assignment $x$, the associated minimal element $\gamma_{V}(x)$ is a core assignment.

Given a valid ordinary assignment $z \in\{0,1\}^{n}$, an interesting object is the subgraph of partial assignments that lie below it in the partial ordering. It can be seen that any pair of elements in this subgraph have both a unique maximal element and a unique minimal element, so that any such subgraph is a lattice [38].

In examples shown in Figure 5, only a subset of the partial assignments is shown, since even for small formulas the space of partial assignments is quite large. For the first formula all satisfying assignments have a trivial core. For the second one, on the other hand, there are assignments with non-trivial cores.

# 4.2 Pure survey propagation as a peeling procedure 

As a particular case of Theorem 3, setting $\omega_{*}=1$ and $\omega_{o}=0$ yields the extended MRF that underlies the $\mathrm{SP}(1)$ algorithm. In this case, the only valid assignments with positive weight are those without any unconstrained variables - namely, core assignments. Thus, the distribution $p_{W}$ for $\left(\omega_{o}, \omega_{*}\right)=(0,1)$ is simply uniform over the core assignments. The following result connects fixed points of $\mathrm{SP}(1)$ to core assignments:

Proposition 5. For a valid assignment $x$, let $\mathrm{SP}(1)$ be initialized by:

$$
\Pi_{i \rightarrow a}^{u}=\delta\left(x_{i}, u_{a, i}\right), \quad \Pi_{i \rightarrow a}^{s}=\delta\left(x_{i}, s_{a, i}\right), \quad \Pi_{i \rightarrow a}^{*}=0
$$

Then within a finite number of steps, the algorithm converges and the output fields are

$$
\mu_{i}(b)=\delta\left(y_{i}, b\right)
$$

where $y=\gamma_{V}(x)$ and $b \in\{0,1, *\}$.
Proof. We say that a variable $i$ belongs to the core if $y_{i} \neq *$. We say that a clause $a$ belongs to the core if all the variables in the clause belong to the core. We first show by induction that
I. If $a$ and $i$ belong to the core and $y_{i}$ is not the unique satisfying variable for $a$ then $\Pi_{i \rightarrow a}^{u}=$ $\delta\left(x_{i}, u_{a, i}\right)$ and $\Pi_{i \rightarrow a}^{s}=\delta\left(x_{i}, s_{a, i}\right)$, and

![img-3.jpeg](img-3.jpeg)

Figure 5. Portion of the directed graph on partial assignments for two different formulas: (a) $\left(\bar{x}_{1} \vee \bar{x}_{2} \vee x_{3}\right) \wedge\left(x_{2} \vee \bar{x}_{3} \vee \bar{x}_{4}\right)$. highlighted is the lattice below the satisfying assignment $z=(1,1,1,1)$, whose core is trivial (i.e., $\gamma_{V}(z)=(*, *, *, *)$ ). (b) $\left(\bar{x}_{1} \vee x_{2} \vee x_{3}\right) \wedge\left(x_{1} \vee \bar{x}_{2} \vee x_{3}\right) \wedge\left(x_{2} \vee \bar{x}_{3} \vee x_{1}\right) \wedge$ $\left(x_{2} \vee \bar{x}_{3} \vee x_{5}\right) \wedge\left(x_{1} \vee x_{5} \vee \bar{x}_{4}\right)$. the satisfying assignment $z=(0,0,0,0,1)$ has the non-trivial core $\gamma_{V}(z)=(0,0,0,*, *)$. For the same formula there are other satisfying assignments, e.g. $(1,0,1,0,1)$ which have a trivial core.

II. If $a$ and $i$ belong to the core and $y_{i}$ is the unique satisfying variable for $a$ then $\eta_{a \rightarrow i}=1$.

Clearly, property I holds at time 0 . Therefore, it suffices to prove that if property I holds at time $t$ then so does II. and that if property II holds at time $t$ then property I holds at time $t+1$.

Suppose that property I holds at time $t$. Let $a$ and $i$ belong to the core such that $y_{i}$ is the unique satisfying variable of the clause $a$. By the induction hypothesis for all $j \in V(a) \backslash\{i\}$ it holds that $\Pi_{j \rightarrow a}^{u}=\delta\left(x_{j}, u_{a, j}\right)=1$. This implies that $\eta_{a \rightarrow i}=1$ as needed.

Suppose that property II holds at time $t$. Let $a$ and $i$ belong to the core such that $y_{i}$ is not unique satisfying for $a$. By the assumption, it follows that there exists $b$ which belongs to the core such that $y_{i}$ is the unique satisfying variable for $b$. This implies by the induction hypothesis that $\eta_{b \rightarrow i}=1$. It is now easy to see that at update $t+1: \Pi_{i \rightarrow a}^{u}=\delta\left(x_{i}, u_{a, i}\right)$ and $\Pi_{i \rightarrow a}^{s}=\delta\left(x_{i}, s_{a, i}\right)$. Note that the claim above implies that for all times $t$ and all $i$ such that $y_{i} \neq *$, it holds that $\mu_{i}(b)=\delta\left(y_{i}, b\right)$.

Let $i_{1}, i_{2}, \ldots, i_{s}$ be a "peeling-path" from $x$ to $y$. In other words, the variable $i_{1}$ is not uniquely satisfying any clause. Once, this variable is set to $*$, the variable $i_{2}$ is not uniquely satisfying any clause etc. We claim that for all $1 \leq t \leq s$, for all updates after time $t$ and for all clauses $a$ such that $i_{t} \in V(a)$ it holds that $\eta_{a \rightarrow i_{t}}=0$. The proof follows easily by induction on $t$. This in turn implies that if for all updates after time $t \mu_{i_{t}}(b)=\delta\left(y_{i}, *\right)$, from which the result follows.

Thus, $\mathrm{SP}(1)$, when suitably initialized, simply strips the valid assignment $x$ down to its core $\gamma_{V}(x)$. Moreover, Proposition 5, in conjunction with Theorem 3, leads to viewing the pure form of survey propagation $\mathrm{SP}(1)$ as performing an approximate marginalization over cores. Therefore, our results raise the crucial question: do cores exist for random formulas? Motivated by this perspective, Achlioptas and Ricci-Tersenghi [2] has answered this question affirmatively for $k$-SAT with $k \geq 9$. In Section 5, we show that cores, if they exist, must be "large" in a suitable sense (see Proposition 8). In the following section, we explore the case $k=3$ via experiments on large instances.

# 4.3 Peeling experiments 

We have performed a large number of the following experiments:

1. starting with a satisfying assignment $x$, change a random one of its unconstrained variables to $*$,
2. repeat until there are no unconstrained variables.

This procedure, which we refer to as "peeling", is equivalent to taking a random path from $x$ in $G$, by choosing at each step a random outgoing edge. Any such path terminates at the core $\gamma_{V}(x)$. It is interesting to examine at each step of this process the number of unconstrained variables (equivalently, the number of outgoing edges in the graph $G$ ). For $k=3$ SAT problems, Figure 6 shows the results of such experiments for $n=100,000$, and using different values of $\alpha$. The plotted curves are the evolution of the number of unconstrained variables as the number of $*$ 's increases. We note that for $n=100$ and $\alpha$ close to the threshold, satisfying assignments often correspond to core assignments; a similar observation was also made by Braunstein and Zecchina [7]. In contrast, for larger $n$, this correspondence is rarely the case. Rather, the generated curves suggest that $\gamma_{V}(x)$ is almost always the all-* assignment, and moreover that for high density $\alpha$, there is a critical level

![img-4.jpeg](img-4.jpeg)

Figure 6. Evolution of the number of unconstrained variables in the peeling process: start with a satisfying assignment, change a random unconstrained variable to $*$ and repeat. Plotted is the result of an experiment for $n=100,000$, for random formulas with $k=3$ and $\alpha=\{2,2.5,3,3.5,4,4.1,4.2\}$. In particular, core assignments are on the $x$-axis, and satisfying assignments are on the $y$-axis.
in $G$ where the out-degrees are very low. Increasing $\alpha$ results in failure of the algorithm itself, rather than in the formation of real core assignments.

For $k=2$, the event that there is a path in $G$ from a satisfying assignment to the all-* assignment has a very natural interpretation. In particular, it is equivalent to the event that the pure-literal rule succeeds in finding an assignment. The pure-literal rule [36] is an algorithm consisting of the following steps: assign 1 to a variable if it only appears positively in a clause, and 0 if it only appears negatively in a clause, reduce the formula, and repeat the procedure. It is straightforward to check that the sequence of variables given by the labels on any path from the all-* assignment to a satisfying assignment can be identified with a sequence of steps of the pure-literal type. Furthermore, it is known [36] that there is a phase transition for the event that the pure-literal rule succeeds at $\alpha=1$.

Interestingly, as mentioned earlier, for $k \geq 9$ there are values for $\alpha<\alpha_{c}$ such that this peeling procedure provably results in a non-trivial core assignment with high probability, according to [2]. The fact that we do not observe core assignments for $k=3$, and yet the algorithm is successful, means that an alternative explanation is required. Accordingly, we propose studying the behavior of $\mathrm{SP}(\rho)$ for $\rho \in(0,1)$. Our experimental results, consistent with similar reports from Kirkpatrick [23], show that $\mathrm{SP}(\rho)$ tends to be most effective in solving $k$-SAT for values of $\rho<1$. If so, the good behavior of $\mathrm{SP}(1)$ may well follow from the similarity of $\mathrm{SP}(1)$ updates to $\mathrm{SP}(\rho)$ updates for $\rho \approx 1$. To further explore this issue, the effects of varying the weight distribution $\left(\omega_{o}, \omega_{*}\right)$, and consequently the parameter $\rho$, are discussed in the following section.

# 4.4 Weight distribution and smoothing 

One of the benefits of our analysis is that it suggests a large pool of algorithms to be investigated. One option is to vary the values of $\omega_{o}$ and $\omega_{*}$. A "good" setting of these parameters should place significant weight on precisely those valid assignments that can be extended to satisfying assignments. At the same time, the parameter setting clearly affects the level of connectivity in the

![img-5.jpeg](img-5.jpeg)

Figure 7. Performance of BP for different choices of $\left(\omega_{o}, \omega_{*}\right)$ as applied to a particular randomly chosen formula with $n=10000, k=3, \alpha=4.2$. Four distinct cases can be distinguished: (i) BP converges and the decimation steps yields a complete solution, (ii) BP converges and the decimation steps yield a partial solution, completed by using Walk-SAT, (iii) BP converges, but the decimation steps don't lead to a solution, and (iv) BP does not converge.
space of valid assignments. Connectivity most likely affects the performance of belief propagation, as well as any other algorithm that we may apply to compute marginals or sample from the distribution.

Figure 7(a) shows the performance of belief propagation on the extended MRF for different values of $\left(\omega_{o}, \omega_{*}\right)$, and applied to particular random formula with $n=10,000, k=3$ and $\alpha=4.2$. The most successful pairs in this case were $(0.05,0.95),(0.05,0.9),(0.05,0.85)$, and $(0.05,0.8)$. For these settings of the parameters the decimation steps reached a solution, so a call to WalkSAT was not needed. For weights satisfying $\omega_{o}+\omega_{*}>1$, the behavior is very predictable: although the algorithm converges, the choices that it makes in the decimation steps lead to a contradiction. Note that there is a sharp transition in algorithm behavior as the weights cross the line $\omega_{o}+\omega_{*}=1$, which is representative of the more general behavior.

The following result provides some justification for the excellent performance in the regime $\omega_{o}+\omega_{*} \leq 1$.

Theorem 6. If $\omega_{o}+\omega_{*}=1$, then $\sum_{y \leq x} W(y)=\omega_{*}^{n_{*}(x)}$ for any valid assignment $x$. If $\omega_{o}+\omega_{*}<1$, then $\sum_{y \leq x} W(y) \geq\left(\omega_{*}\right)^{n_{*}(x)}$ for any valid assignment $x$.

It should be noted that Theorem 6 has a very natural interpretation in terms of a "smoothing" operation. In particular, the $\left(\omega_{o}, \omega_{*}\right)$-MRF may be regarded as a smoothed version of the uniform distribution over satisfying assignments, in which the uniform weight assigned to each satisfying assignment is spread over the lattice associated with it. ${ }^{3}$

The remainder of this section is devoted to the proof of Theorem 6.
Proof. We start with the case $\omega_{o}+\omega_{*}=1$. Let $A$ denote the set of partial assignments $z$ such that $z_{j} \in\left\{x_{j}, *\right\}$ for all $j \in V$. We refer to these as the set of assignments consistent with $x$. Let

[^0]
[^0]:    ${ }^{3}$ Note, however, that any partial assignment that belongs to two or more lattices is assigned a weight only once. Otherwise, the transformation would be a convolution operation in a strict sense.

![img-6.jpeg](img-6.jpeg)

Figure 8. The directed graph $G$ and the map $\sigma$ for the formula $\left(x_{1} \vee x_{2} \vee x_{3}\right) \wedge\left(\bar{x}_{2} \vee \bar{x}_{3} \vee x_{4}\right)$ and the satisfying assignment $(0,0,1,0)$. The solid arrows denote edges in $G$ and the dashed arrows denote $\sigma$.
$B=\{y: y \leq x\}$ be the set of valid assignments that are reachable from $x$. Notice that all $y \in B$ are valid and consistent with $x$, but not every valid assignment in $A$ is reachable from $x$. We will let $S_{*}(z)$ denote the set of variables assigned $*$ both for valid and invalid assignments $z$.

We define a map between all assignments consistent with $x$ and the set of reachable ones. Let $\sigma: A \rightarrow B$ be defined as

$$
\sigma(z):=\gamma_{S_{*}(z)}(x)
$$

Notice that if $y \in B$ then $\sigma(y)=y$. The map is, of course, many-to-one. We define what we'll show is the reverse map. For $y \in B$ let

$$
\tau(y):=\left\{z \in A: S_{*}(z)=S_{*}(y) \cup T, T \subseteq S_{c}(y)\right\}
$$

Lemma 7. For any $y \in B$ and $z \in A, z \in \tau(y)$ if and only if $\sigma(z)=y$.
Proof. Let $z \in \tau(y)$ so that $S_{*}(z)=S_{*}(y) \cup T$ for some $T \subseteq S_{c}(y) . \sigma(z)=\gamma_{S_{*}(z)}(x)$ is the minimal valid assignment such that the path from $x$ to it is labeled only by elements in $S_{*}(z)$. We'll show that $y$ satisfies these properties, and therefore by proposition $4, y=\sigma(z)$. Any path from $x$ to $y$ (which exists since $y \in B$ ) is labeled by $S_{*}(y) \backslash S_{*}(x) \subseteq S_{*}(z)$. Furthermore, for every $i \in S_{*}(z)$, $i \notin S_{o}(y)$ so there is no outgoing edge from $y$ labeled by an element in $S_{*}(z)$. Therefore $y$ is minimal.

Let $y=\sigma(z)=\gamma_{S_{*}(z)}(x)$. By proposition 4 there is no $i \in S_{*}(z)$ such that $i \in S_{o}(y)$. Therefore $S_{*}(z) \subseteq S_{*}(y) \cup S_{c}(y)$. Further we have that $S_{*}(y) \subseteq S_{*}(z) \cup S_{*}(x)=S_{*}(z)$, therefore $S_{*}(z)=$ $S_{*}(y) \cup T$ for some $T \subseteq S_{c}(y)$. Hence $z \in \tau(y)$.

For a set of partial assignments $X$ let $W(X)=\sum_{x \in X} W(x)$. Let $W^{\emptyset}(z)=\left(\omega_{*}\right)^{n_{*}(z)} \times$ $\left(\omega_{o}\right)^{n-n_{*}(z)}$, denote the weight of any partial assignment, if the formula had no clauses. For such a formula all partial assignments are valid. Observe that if we restrict our attention to the assign-

ments that are consistent with $x$,

$$
\begin{aligned}
W^{\emptyset}(A) & =\sum_{z \in A} W^{\emptyset}(z) \\
& =\sum_{S \subseteq V \backslash S_{*}(x)}\left(\omega_{*}\right)^{\left|S_{*}(x)\right|+|S|} \times\left(\omega_{o}\right)^{n-\left|S_{*}(x)\right|-|S|} \\
& =\left(\omega_{*}\right)^{\left|S_{*}(x)\right|} \times\left(\omega_{*}+\omega_{o}\right)^{n-\left|S_{*}(x)\right|} \\
& =\left(\omega_{*}\right)^{n_{*}(x)}
\end{aligned}
$$

We show that when clauses are added to the formula, the total weight under $x$ is preserved as long as $x$ is still valid. In particular when an assignment $z$ that is consistent with $x$ becomes invalid, it passes its weight to an assignment that is still valid, namely $\sigma(z)$, which has fewer * variables than $z$.

$$
\begin{aligned}
W(y) & =\left(\omega_{*}\right)^{n_{*}(y)} \times\left(\omega_{o}\right)^{n_{o}(y)} \times 1^{n_{c}(y)} \\
& =\left(\omega_{*}\right)^{n_{*}(y)} \times\left(\omega_{o}\right)^{n_{o}(y)} \times\left(\omega_{*}+\omega_{o}\right)^{n_{c}(y)} \\
& =\sum_{T \subseteq S_{c}(y)}\left(\omega_{*}\right)^{n_{*}(y)+|T|} \times\left(\omega_{o}\right)^{n_{o}(y)+n_{c}(y)-|T|} \\
& =\sum_{T \subseteq S_{c}(y)} W^{\emptyset}\left(z: S_{*}(z)=S_{*}(y) \cup T\right) \\
& =W^{\emptyset}\left(\left\{z: S_{*}(z)=S_{*}(y) \cup T, T \subseteq S_{c}(y)\right\}\right) \\
& =W^{\emptyset}(\tau(y))
\end{aligned}
$$

Finally, we have:

$$
\sum_{y \leq x} W(y)=\sum_{y \leq x} W^{\emptyset}(\tau(y))=W^{\emptyset}(A)=\left(\omega_{*}\right)^{n_{*}(x)}
$$

where we used the fact that the sets $\tau(y)$ for $y \in B$ partition $A$ by lemma 7 .
The proof of the case $\omega_{o}+\omega_{*}<1$ is similar except that equation (17) becomes an inequality:

$$
W(y)=\left(\omega_{o}\right)^{n_{o}(y)} \times\left(\omega_{*}\right)^{n_{*}(y)} \times 1^{n_{c}(y)} \geq \sum_{T \subseteq S_{c}(S)} W^{\emptyset}(\tau(y))
$$

When an assignment $z$ that is consistent with $x$ becomes invalid, it passes more than its own weight to $\sigma(z)$.

# 4.5 Gibbs sampling 

Based on our experiments, the algorithm $\mathrm{SP}(\rho)$ is very effective for appropriate choices of the parameter $\rho$. The link provided by Theorem 6 suggests that the distribution $p_{W}$, for which $\mathrm{SP}(\rho)$ —as an instantiation of belief propagation on the extended MRF-is computing approximate marginals, must posses good "smoothness" properties. One expected consequence of such "smoothness" is that algorithms other than BP should also be effective in computing approximate marginals. Interestingly, rigorous conditions that imply (rapid) convergence of BP [39]-namely, uniqueness of Gibbs measures on the computation tree-are quite similar to conditions implying rapid convergence of

Gibbs samplers, which are often expressed in terms of "uniqueness", "strong spatial mixing", and "extremality" (see, for example [27, 4]).

In this section, we explore the application of sampling methods to the extended MRF as a means of computing unbiased stochastic approximations to the marginal distributions, and hence biases at each variable. More specifically, we implemented a Gibbs sampler for the family of extended MRFs


(a) Comparison to $\operatorname{SP}(0.95)$


(b) Comparison to $\operatorname{SP}(0.9)$


(c) Comparison to $\operatorname{SP}(0.7)$


(d) Comparison to $\operatorname{SP}(0.5)$

Figure 9. Comparison of $S P(\beta)$ pseudomarginals for $\beta \in\{0.95,0.9,0.7,0.5\}$ to marginals estimated by Gibbs sampling on weighted MRFs with $\rho \in\{0.4,0.5,0.7,0.9\}$ for the range of SAT problems $\alpha \in\{4.2,4.1,4.0 .3 .8,3.6,3.4\}$. Each entry in each table shows the average $\ell_{1}$ error between the biases computed from the $S P(\beta)$ pseudomarginals compared to the biases computed from Gibbs sampling applied to $\operatorname{MRF}(\rho)$. Calculations were based on top 50 most biased nodes on a problem of size $n=1000$. The bold entry within each row (corresponding to a fixed $\alpha$ ) indicates the $\operatorname{MRF}(\rho)$ that yields the smallest $\ell_{1}$ error in comparison to the SP biases.
developed in Section 3. The Gibbs sampler performs a random walk over the configuration space of the extended MRF-that is, on the space of partial valid assignments. Each step of the random walk entails picking a variable $x_{i}$ uniformly at random, and updating it randomly to a new value $b \in\{0,1, *\}$ according to the conditional probability $p_{W}\left(x_{i}=b \mid\left(x_{j}: j \neq i\right)\right)$. By the construction of our extended MRF (see equation (12)), this conditional probability is an (explicit) function of the variables $x_{j}$ and $x_{i}$ appear together in a clause, and of the variables $x_{k}$ such that $x_{k}$ and $x_{j}$ appear together in a clause, where $x_{j}$ and $x_{i}$ appear together in a clause.

It is of interest to compare the approximate marginals computed by the $\operatorname{SP}(\beta)$ family of algorithms (to which we refer as pseudomarginals) to the (stochastic) estimates computed by Gibbs sampler. Given the manner in which the SP pseudomarginals are used in the decimation procedure, the most natural comparison is between the biases $\mu_{i}(0)-\mu_{i}(1)$ provided by the $S P(\beta)$ algorithm, and the biases $\tau_{i}(0)-\tau_{i}(1)$ associated with the Gibbs sampler (where $\tau_{i}$ are the approx-

imate marginals obtained from Gibbs sampling on the extended MRF with parameter $\rho$ (denoted $\operatorname{MRF}(\rho)$ ). The results of such comparisons for the SP parameter $\beta \in\{0.95,0.9,0.7,0.5\}$ and the Gibbs sampling parameter $\rho \in\{0.4,0.5,0.7,0.9\}$ are shown in Figure 9. Comparisons are made for each pair $(\beta, \rho)$ in these sets, and over a range of clause densities $\alpha \in\{4.2,4.1,4.0 .3 .8,3.6,3.4\}$. For fairly dense formulas (e.g., $\alpha \geq 4.0$ ), the general trend is that the $\operatorname{SP}(\beta)$ biases with larger $\beta$ agree most closely with the Gibbs biases with $\rho$ relatively smaller (i.e., $\rho<\beta$ ). For lower clause densities (e.g., $\alpha=3.4$ ), the agreement between the $\operatorname{SP}(\beta)$ and Gibbs biases on $\operatorname{MRF}(\rho)$ when $\beta=\rho$ is substantially closer.

# 5 Expansion arguments for random formulas 

This section is devoted to the study of properties of the MRF on random formulas. We will use simple random graph arguments in order to obtain typical properties of cores, as well as the behavior of Gibbs sampling or message-passing algorithms applied to the MRF associated with a randomly chosen formula. Throughout this section, we denote $p_{W}^{\phi}$ to denote the MRF distribution for a fixed formula $\phi$. Otherwise, we write $\mathbb{P}^{n, m}$ for the uniform measure on $k$-sat formulas with $n$ variables and $m$ clauses, and $\mathbb{P}^{n, \alpha}$ for the uniform measure on $k$-sat formulas with $n$ variables and $m=\alpha n$ clauses. We often drop $n, m$, and/or $\alpha$ when they are clear from the context. Finally, we use $\mathrm{E}_{W}^{\phi}, \mathbb{E}^{n, m}$ and $\mathbb{E}^{n, \alpha}$ to denote expectations with respect to the distributions $p_{W}^{\phi}, \mathbb{P}^{n, m}$ and $\mathbb{P}^{n, \alpha}$ respectively.

### 5.1 Size of cores

We first prove a result that establishes that cores, if they exist, are typically at least a certain linear fraction $c(\alpha, k)$ of the total number $n$ of variables.
Proposition 8. Let $\phi$ be a random $k$-sat formula with $m=\alpha n$ clauses where $k \geq 3$. Then for all positive integers $C$ it holds that

$$
\mathbb{P}^{n, \alpha}\left[\phi \text { has a core with } C \text { clauses }\right] \leq\left(\frac{e^{2} \alpha C^{k-2}}{n^{k-2}}\right)^{C}
$$

Consequently, if we define $c(\alpha, k):=\left(\alpha e^{2}\right)^{-1 /(k-2)}$, then with $\mathbb{P}^{n, \alpha}$-probability tending to one as $n \rightarrow+\infty$, there are no cores of size strictly less than $c(\alpha, k) n$.
Proof. Suppose that the formula $\phi$ has a core with $C$ clauses. Note that the variables in these clauses all lie in some set of at most $C$ variables. Thus the probability that a core with $C$ clauses exist is bounded by the probability that there is a set of $C$ clauses all whose variables lie in some set of size $\leq C$. This probability is bounded by

$$
\binom{m}{C}\binom{n}{C}\left(\frac{C}{n}\right)^{C k}
$$

which can be upper bounded by

$$
\left(\frac{e m}{C}\right)^{C}\left(\frac{e n}{C}\right)^{C}\left(\frac{C}{n}\right)^{C k}=\left(\frac{e^{2} \alpha C^{k-2}}{n^{k-2}}\right)^{C}
$$

as needed.

# 5.2 (Meta)-stability of the all * assignment for small $\rho$ 

By definition, the extended MRF for $\rho=1$ assigns positive mass to the all-* vector. Moreover, Proposition 8 implies that the size of cores (when they exist) is typically linear in $n$. It follows that the state space of the MRF for $\rho=1$ typically satisfies one of the following properties:

- Either the state space is trivial, meaning that it contains only the all $*$ state, or
- The state space is disconnected with respect to all random walks based on updating a small linear fraction of the coordinates in each step.

The goal of this section is to establish that a similar phenomenon persists when $\rho$ is close to 1 (i.e., when $1-\rho$ is small).

We begin by introducing some notions from the analysis of the mixing properties of Markov chains. Let $T$ be a reversible chain with respect to a measure $p$ on a state space $\Omega$. For sets $A, B \subset \Omega$, write

$$
q_{T}(A, B)=\sum_{x \in A, y \in B} p(x) T_{x \rightarrow y}=\sum_{x \in A, y \in B} p(y) T_{y \rightarrow x}
$$

The conductance of the chain $T$ is defined as

$$
c(T)=\inf _{S \subset \Omega}\left\{\frac{q_{T}\left(S, S^{c}\right)}{p(S)(1-p(S))}\right\}
$$

It is well-known that $c(T) / 2$ is an upper bound on the spectral gap of the chain $T$ and that $2 / c(T)$ is a lower bound on the mixing time of the chain. We note moreover that the definition of $T$ implies that for every two sets $A, B$ it holds that $q_{T}(A, B) \leq \min \{p(A), p(B)\}$.

Definition 9. Consider a probability measure $p$ on a space $\Omega$ of strings of length $n$. Let $T$ be a Markov chain on $\Omega$. The radius of $T$ denoted by $r(T)$ is defined by

$$
r(T):=\sup \left\{d_{H}(x, y): T_{x, y}>0\right\}
$$

where $d_{H}$ is the Hamming distance. We let the radius $r$-conductance of $p$ denote by $c(r, p)$ be

$$
c(r, p):=\sup \{c(T): T \text { is reversible with respect to } p \text { and } r(T) \leq r\}
$$

Now returning to the random $k$-SAT problem, we write $p_{\rho}$ for the measure $p_{W}=p_{W}^{\phi}$ with $\omega_{*}=\rho$ and $\omega_{o}=1-\rho$.

Proposition 10. Consider a randomly chosen $k$-SAT formula with density $\alpha$. Then there exists a $\rho_{0} \in(0,1)$ such that if $\rho>\rho_{0}$ then $\mathbb{P}^{n}\left[\phi \in A_{n} \cup B_{n}\right] \rightarrow 1$ as $n \rightarrow+\infty$ where $A_{n}$ and $B_{n}$ are the following events:
(I) $A_{n}$ consists of all the formulas $\phi$ satisfying $p_{\rho}^{\phi}\left[n-n_{*}(x) \leq 2 \sqrt{(1-\rho)} n\right] \geq 1-\exp (-\Omega(n))$.
(II) $B_{n}$ consists of all the formulas $\phi$ for which the measure $p_{\rho}^{\phi}$ satisfies $c\left(\sqrt{(1-\rho)} n, p_{\rho}\right) \leq$ $\exp (-\Omega(n))$.

Proof. We let $\delta$ be a small positive number to be determined, and set $1-\rho=\delta^{2}$. As it suffices to work with ratios of probabilities, we use the unnormalized weight $W^{\phi}(x)$ instead of $p_{W}^{\phi}(x)$.

The proof requires the following:

Lemma 11. Let $d$ be an integer satisfying $\delta n \leq d \leq 2 \delta n$. For $\delta$ sufficiently small, it holds that with $\mathbb{P}^{n}$ probability going to 1 as $n \rightarrow \infty$

$$
\frac{\sum_{d=\delta n}^{2 \delta n} W^{\phi}\left[n-n_{*}=d\right]}{\rho^{3 n}}=\exp (-\Omega(n))
$$

Proof. See Appendix C.1.
To establish the proposition, it suffices to show that for any formula $\phi$ for which equation (21) of Lemma 11 is valid, then one of either condition (I) or condition (II) must hold.
(i) First suppose that $W^{\phi}\left[n-n_{*}(x)>2 \delta n\right] \leq \rho^{3 n / 2}$. In this case, condition (I) in the statement of the proposition follows immediately.
(ii) Otherwise, we may take $W^{\phi}\left[n-n_{*}(x)>2 \delta n\right] \geq \rho^{3 n / 2}$. In this case, we can apply the conductance bound in order to bound the gap of any operator with radius $\leq \delta n$. Take the set $A$ to be all $x$ with $n-n_{*}(x)<\delta n$ and $B$ be the set of all $x$ with $\delta n \leq n-n_{*}(x) \leq 2 \delta n$. Let $T$ be any Markov chain with radius $\delta n$ that is reversible with respect to $p_{W}$. Then we have $q_{T}\left(A, A^{c}\right)=q_{T}(A, B) \leq p(B)$. In addition, it holds that $W^{\phi}\left[n-n_{*}(x)<\delta n\right] \geq \rho^{n}$ (since if $x$ is the all-* assignment, we have $W^{\phi}(x)=\rho^{n}$ ); moreover, if we take $n$ sufficiently large, then we have $W^{\phi}[\delta n \leq n-n_{*}(x) \leq 2 \delta n] \leq \rho^{3 n}$ by Lemma 11. Combining these inequalities, we obtain that the conductance of $T$ is bounded above by

$$
\begin{aligned}
\frac{q\left(A, A^{c}\right)}{p(A) p\left(A^{c}\right)} & \leq \frac{p(B)}{p(A) p\left(A^{c}\right)} \\
& \leq \frac{W^{\phi}[\delta n \leq n-n_{*}(x) \leq 2 \delta n]}{W^{\phi}\left[n-n_{*}(x)<\delta n\right] W^{\phi}\left[n-n_{*}(x)>2 \delta n\right]} \\
& \leq \frac{\rho^{3 n}}{\rho^{n} \rho^{\frac{3 n}{2}}}=\rho^{n / 2}
\end{aligned}
$$

which implies condition (II).

# 5.3 Message-passing algorithms on random ensembles 

The analysis of the preceding section demonstrated that for values of $\rho$ close to 1 , any random sampling technique based on local moves (e.g., Gibbs sampling), if started at the all $*$ assignment, will take exponentially long to get to an assignment with more than a negligible fraction of non-*. This section is devoted to establishing an analogous claim for the belief propagation updates on the extended Markov random fields. More precisely, we prove that if $\rho$ is sufficiently close to 1 , then running belief propagation with initial messages that place most of their mass on on $*$ will result assignments that also place most of the mass on $*$.

This result is proved in the "density-evolution" setting [e.g., 35] (i.e., the number of iterations is taken to be less than the girth of the graph, so that cycles have no effect). More formally, we establish the following:

Theorem 12. For every formula density $\alpha>0$, arbitrary scalars $\epsilon^{\prime \prime}>0$ and $\delta>0$, there exists $\rho^{\prime}<1, \epsilon^{\prime} \in\left(0, \epsilon^{\prime \prime}\right)$ and $\gamma>0$ such that for all $\rho \in\left(\rho^{\prime}, 1\right]$ and $\epsilon \in\left(0, \epsilon^{\prime}\right)$, the algorithm $S P(\rho)$ satisfies the following condition.

Consider a random formula $\phi$, a random clause $b$ and a random variable $i$ that belongs to the clause $b$. Then with probability at least $1-\delta$, if $S P(\rho)$ is initialized with all messages $\eta_{a \rightarrow j}^{0}<\epsilon$, then the inequality $\eta_{b \rightarrow i}^{t}<\epsilon^{\prime}$ holds for all iterations $t=0,1, \ldots, \gamma \log n$.

The first step of the proof is to compare the SP iterations to simpler "sum-product" iterations.
Lemma 13. For any $\rho \in[0,1]$, the $S P(\rho)$ iterations satisfy the inequality:

$$
\eta_{a \rightarrow i}^{t+1} \leq \prod_{j \in V(a) \backslash\{i\}} \min \left(1,(1-\rho)+\rho \sum_{b \in C(j) \backslash\{a\}} \eta_{b \rightarrow j}^{t}\right)
$$

Proof. See Appendix C.2.
Since our goal is to bound the messages $\eta_{a \rightarrow i}^{t+1}$, Lemma 13 allows us to analyze the simpler message-passing algorithm with updates specified by:

$$
\eta_{a \rightarrow i}^{t+1}=\prod_{j \in V(a) \backslash\{i\}} \min \left(1,(1-\rho)+\rho \sum_{b \in C(j) \backslash\{a\}} \eta_{b \rightarrow j}^{t}\right)
$$

The next step is to bound the probability of "short-cycles" in the computation tree corresponding to the message-passing updates specified in equation (22). More formally, given a formula $\phi$, we define a directed graph $G(\phi)=(V, E)$, in which the vertex set $V$ consists of messages $\eta_{a \rightarrow i}$. The edge set $E$ includes the edge $\eta_{a \rightarrow i} \rightarrow \eta_{b \rightarrow j}$ belongs to $E$ if and only if $j \in V(a) \backslash\{i\}$ and $b \in C_{a}^{u}(i)$. In words, the graph $G(\phi)$ includes an edge between the $\eta_{a \rightarrow i}$ and $\eta_{b \rightarrow j}$ if the latter is involved in the update of $\eta_{a \rightarrow i}$ specified in equation (22).

Lemma 14. Let $G(\phi)$ be the random graph generated by choosing a formula $\phi$ uniformly at random with on clauses and $n$ variables. Let $v$ be a vertex of $G(\phi)$ chosen uniformly at random. For all clause densities $\alpha>0$, there exists $\gamma>0$ such that with probability $1-o(1)$, the vertex $v$ does not belong to any directed cycle of length smaller than $\gamma \log n$ in $G(\phi)$.

Proof. The proof is based on standard arguments from random graph theory [e.g., 21].
Our analysis of the the recursion (22) on the computation tree in based on an edge exposure technique that generates a neighborhood of a vertex $v$ in the graph $G(\phi)$ for a random $\phi$. More specifically, pick a clause $a$ and a variable $i$ in $a$ at random. Now for each variable $j \in V(a) \backslash\{i\}$, expose all clauses $b$ containing $j$ (but not any other of the variables appearing so far). Then for each such $b$, we look at all variables $k \in V(b) \backslash\{j\}$, and so on. We consider the effect of repeating this exposure procedure over $t=\gamma \log n$ steps. When the vertex $\eta_{a \rightarrow i}$ does not belong to cycles shorter than $t$ in $G(\phi)$, such an analysis yields a bound on $\eta_{a \rightarrow i}^{t}$.

Note that each clause can expose at most $k-1$ variables. Recall that we generate the formula $\phi$ by choosing each of the $N_{c}=2^{k}\binom{n}{k}$ clauses with probability $\alpha n / N_{c}$. The distribution of the number of clauses exposed for each variable is thus dominated by $\operatorname{Bin}\left(M_{c}, \alpha n / N_{c}\right)$ where $M_{c}=2^{k}\binom{n}{k-1}$. An equivalent description of this process is the following: each vertex $v=\eta_{a \rightarrow i}$ exposes $X_{v}$ neighbors

$\eta_{b \rightarrow j}$, where the distribution of the collection $\left\{X_{v}\right\}$ is dominated by a collection $\left\{Y_{v}\right\}$ of i.i.d. random variables. Moreover, the $Y$ 's are jointly distributed as the sum of $k-1$ i.i.d. $\operatorname{Bin}\left(M_{c}, \alpha n / N_{c}\right)$ variables.

The proof requires the following lemma on branching processes.
Lemma 15. Consider a branching process where each vertex gives birth to $Y$ children. Assume further that the branching process is stopped after $m$ levels and let $K>0$ be given.

The notion of a good vertex is defined inductively as follows. All vertices at level $m$ are good. A vertex at level $m-1$ is good if it has $\ell$ children and $\ell \leq K$. By induction for $s \geq 2$ we call a vertex at level $m-s$ good if $v$ has $\ell$ children $v_{1}, \ldots, v_{\ell}$ with $\ell \leq K$ and
(a) Either all of $v_{1}, \ldots, v_{\ell}$ have at most $K$ children, of which all are good; or
(b) all of $v_{1}, \ldots, v_{\ell}$ have at most $K$ children, of which all but one are good.

Denote by $p(m, K)$ the probability that the root of the branching process is good. Then

$$
\inf _{0 \leq m<\infty} p(m, K)=1-\exp (-\Omega(K))
$$

Proof. See Appendix C.3.
We are now equipped to complete the proof of Theorem 12. Using Lemma 14, first choose $\gamma=\gamma(\alpha)$ such that a random vertex in $G(\phi)$ does not belong to cycles shorter than $\gamma \log n$ with probability $1-o(1)$. Next use Lemma 15 to choose $K$ such that the probability $\inf _{0 \leq m<\infty} p(m, K)$ that the root of the branching process is good is at least $1-\delta / 2$.

Next we define a pair of functions $\theta$ and $\zeta$ (each mapping $R \times R$ to the real line) in the following way:

$$
\theta(\epsilon, \rho):=((1-\rho)+K \rho \epsilon), \quad \zeta(\epsilon, \rho):=\theta(\theta(\epsilon, \rho), \rho) \times \theta\left(\theta(\epsilon, \rho)^{2}, \rho\right)
$$

Setting $\epsilon^{\prime}:=\min \left(\epsilon^{\prime \prime}, \frac{1}{2 K^{3}}\right)$, observe that $\theta\left(\epsilon^{\prime}, 1\right)=K \epsilon^{\prime}$ and therefore $\theta^{2}\left(\epsilon^{\prime}, 1\right) \leq \frac{\epsilon^{\prime}}{4}$ and

$$
\zeta\left(\epsilon^{\prime}, 1\right)=\theta\left(K \epsilon^{\prime}, 1\right) \theta\left(\left(K \epsilon^{\prime}\right)^{2}, 1\right)=\left(K^{2} \epsilon^{\prime}\right)\left(K^{4} \epsilon^{\prime 2}\right)=K^{6} \epsilon^{\prime 3} \leq \frac{\epsilon^{\prime}}{4}
$$

It now follows by continuity that there exists $\rho^{\prime}<1$ such that for all $1 \geq \rho \geq \rho^{\prime}$ it holds that

$$
\theta^{2}\left(\epsilon^{\prime}, \rho\right) \leq \frac{\epsilon^{\prime}}{2}, \quad \zeta\left(\epsilon^{\prime}, \rho\right) \leq \frac{\epsilon^{\prime}}{2}
$$

We claim that the statement of the theorem holds with the choices of $\gamma, \epsilon^{\prime}$ and $\rho^{\prime}$ above. Indeed, choose a formula $\phi$ with density $\alpha$ at random and let $v=\eta_{a \rightarrow i}$ be a random vertex of $G(\phi)$. With probability at least $1-\delta / 2$, the vertex $v$ does not belong to any cycle shorter than $t=\gamma \log n$.

Since $v$ does not belong to any such cycle, the first $t$ levels of the computation tree of $v$ may be obtained by the exposure process defined above. We will then compare the computation tree to an exposure process where each variable gives birth to exactly $\operatorname{Bin}\left(M_{c}, \alpha n / N_{c}\right)$ clauses. Since the messages are generated according to (22), any bound derived on the values of non-* messages for the larger tree implies the same bound for the real computation tree.

We now claim that if $v$ is a good vertex on that tree, then the message at $v$ after $t$ iterationsnamely, $\eta_{a \rightarrow i}^{t} \longrightarrow$ is at most $\epsilon^{\prime}$. Since a vertex of the tree is good with probability $1-\delta / 2$, proving this claim will establish the theorem.

We prove this claim by induction on $s$, where $m-s$ is the level of $w$. For $s=0$, the claim follows immediately from the initialization of the messages. For $s=1$, observe that equation (22) implies that if $w=\eta_{b \rightarrow j}$ is good at level $m-1$, then

$$
\eta_{b \rightarrow j} \leq \theta^{k-1}(\rho, \epsilon) \leq \theta^{2}\left(\rho, \epsilon^{\prime}\right) \leq \frac{\epsilon^{\prime}}{2}
$$

For the general induction step, assume that $w=\eta_{b \rightarrow j}$ at level $m-s$ is good and $s \geq 2$. There are two cases to consider:
(i) $w$ has all its grand children good. In this case we repeat the argument above twice to obtain $\eta_{b \rightarrow j} \leq \epsilon^{\prime}$.
(ii) Exactly one of $w=\eta_{b \rightarrow j}$ grand children is not good. Let $y^{\prime}=\eta_{d^{\prime} \rightarrow \ell^{\prime}}$ denote the grand-child and $y=\eta_{d \rightarrow \ell}$ denote $y$ parent. Then by equation (22):

$$
\eta_{d \rightarrow \ell} \leq(1-\rho)+K \rho \epsilon^{\prime}=\theta\left(\epsilon^{\prime}, \rho\right)
$$

Using (13) again yields

$$
\begin{aligned}
\eta_{d \rightarrow \ell} & \leq((1-\rho)+K \rho \theta\left(\epsilon^{\prime}, \rho\right))\left((1-\rho)+K \rho \theta^{2}\left(\epsilon^{\prime}, \rho\right)\right)^{k-2} \\
& \leq((1-\rho)+K \rho \theta\left(\epsilon^{\prime}, \rho\right))\left((1-\rho)+K \rho \theta^{2}\left(\epsilon^{\prime}, \rho\right)\right)=\zeta\left(\epsilon^{\prime}, \rho\right) \leq \epsilon^{\prime} / 2
\end{aligned}
$$

which completes the proof.

# 6 Conclusion 

The survey propagation algorithm, recently introduced by Mézard, Parisi and Zecchina [28] for solving random instances of $k$-SAT problems, has sparked a great deal of excitement and research in both the statistical physics and computer science communities [e.g., $6,5,7,3,2,32,33,41]$. This paper provides a new interpretation of the survey propagation algorithm - namely, as an instance of the well-known belief propagation algorithm but as applied to a novel probability distribution over the partial satisfiability assignments associated with a $k$-SAT formula. The perspective of this paper reveals the combinatorial structure that underlies survey propagation algorithm, and we established various results on the form of these structures and the behavior of message-passing algorithms, both for fixed instances and over random ensembles.

The current work suggests various questions and open issues for further research. As we described, associated with any $k$-SAT problem is a large family of Markov random fields over partial assignments, as specified by the parameter $\rho$ (or more generally, the parameters $\omega_{o}$ and $\omega_{*}$ ). Further analysis of survey propagation and its generalizations requires a deeper understanding of the following two questions. First, for what parameter choices do the marginals of the associated Markov random field yield useful information about the structure of satisfiability assignments? Second, for what parameter choices do efficient message-passing algorithms like belief propagation yield accurate approximations to these marginals? Our results show that the success of SP-like algorithms depends on a delicate balance between these two factors. (For instance, the marginals of the uniform distribution over SAT assignments clearly contain useful information, but belief propagation fails to yield good approximations for sufficiently large clause densities.) More generally, these questions

fall in a broader collection of issues, all related to a deeper understanding of satisfiability problems and especially the relationship between finite satisfiability problems and their asymptotic analysis. Given the fundamental role that satisfiability plays in diverse branches of computer science, further progress on these issues is of broad interest.

# 7 Acknowledgments 

We would like to thank Dimitris Achlioptas, Federico Ardila, Andrea Montanari, Mark Mézard, Giorgio Parisi and Alistair Sinclair for helpful discussions.

## A Belief propagation on a generic factor graph

Given a subset $S \subseteq\{1,2, \ldots, n\}$, we define $x_{S}:=\left\{x_{i} \mid i \in S\right\}$. Consider a probability distribution on $n$ variables $x_{1}, x_{2}, \ldots, x_{n}$, that can be factorized as

$$
p\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\frac{1}{Z} \prod_{i=1}^{n} \psi_{i}\left(x_{i}\right) \prod_{a \in C} \psi_{a}\left(x_{V(a)}\right)
$$

where for each $a \in C$ the set $V(a)$ is a subset of $\{1,2, \ldots n\}$; and $\psi_{i}\left(x_{i}\right)$ and $\psi_{a}\left(x_{V(a)}\right)$ are nonnegative real functions, referred to as compatibility functions, and

$$
Z:=\sum_{x}\left[\prod_{i=1}^{n} \psi_{i}\left(x_{i}\right) \prod_{a \in C} \psi_{a}\left(x_{V(a)}\right)\right]
$$

is the normalization constant or partition function. A factor graph representation of this probability distribution is a bipartite graph with vertices $V$ corresponding to the variables, called variable nodes, and vertices $C$ corresponding to the sets $V(a)$ and called function nodes. There is an edge between a variable node $i$ and function node $a$ if and only if $i \in V(a)$. We write also $a \in C(i)$ if $i \in V(a)$.

Suppose that we wish to compute the marginal probability of a single variable $i$ for such a distribution, as defined in equation (5). The belief propagation or sum-product algorithm [24] is an efficient algorithm for computing the marginal probability distribution of each variable, assuming that the factor graph is acyclic. The essential idea is to use the distributive property of the sum and product operations to compute independent terms for each subtree recursively. These recursions can be cast as a message-passing algorithm, in which adjacent nodes on the factor graph exchange intermediate values. Let each node only have access to its corresponding compatibility function. As soon as a node has received messages from all neighbors below it, it can send a message up the tree containing the term in the computation corresponding to it. In particular, let the vectors $M_{i \rightarrow a}$ denote the message passed by variable node $i$ to function node $a$; similarly, the quantity $M_{a \rightarrow i}$ denotes the message that function node $a$ passes to variable node $i$.

The messages from function to variables are updated in the following way:

$$
M_{a \rightarrow i}\left(x_{i}\right) \propto \sum_{x_{V(a) \backslash\{i\}}}\left[\psi_{a}\left(x_{V(a)}\right) \prod_{j \in V(a) \backslash\{i\}} M_{j \rightarrow a}\left(x_{j}\right)\right]
$$

In the other direction, the messages from variable nodes to function nodes are updated as follows

$$
M_{i \rightarrow a}\left(x_{i}\right) \propto \psi_{i}\left(x_{i}\right) \prod_{b \in C(i) \backslash\{a\}} M_{b \rightarrow i}\left(x_{i}\right)
$$

It is straightforward to show that for a factor graph without cycles, these updates will converge after a finite number of iterations. Upon convergence, the local marginal distributions at variable nodes and function nodes can be computed, using the message fixed point $\hat{M}$, as follows:

$$
\begin{aligned}
F_{i}\left(x_{i}\right) & \propto \psi_{i}\left(x_{i}\right) \prod_{b \in C(i)} \hat{M}_{b \rightarrow i}\left(x_{i}\right) \\
F_{a}\left(x_{V(a)}\right) & \propto \psi_{a}\left(x_{V(a)}\right) \prod_{j \in V(a)} \hat{M}_{j \rightarrow a}\left(x_{j}\right)
\end{aligned}
$$

The same updates, when applied to a graph with cycles, are no longer exact due to presence of cycles. An exact algorithm will generally require exponential time. For certain problems, including error-control coding, applying belief propagation to a graph with cycles gives excellent results. Since there are no leaves on graphs with cycles, usually the algorithm is initialized by sending random messages on all edges, and is run until the messages converge to some fixed value [24].

# B Derivation of BP updates on the extended MRF 

## B. 1 Messages from variables to clauses

We first focus on the update of messages from variables to clauses. Recall that we use the notation $P_{i}=S \cup\{a\}$ as a shorthand for the event

$$
a \in P_{i} \quad \text { and } \quad S=P_{i} \backslash\{a\} \subseteq C_{a}^{s}(i)
$$

where it is understood that $S$ could be empty.
Lemma 16 (Variable to clause messages). The variable to clause message vector $M_{i \rightarrow a}$ is fully specified by values for pairs $\left(x_{i}, P_{i}\right)$ of the form:

$$
\left\{\left(s_{a, i}, S \cup\{a\}\right),\left(s_{a, i}, \emptyset \neq P_{i} \subseteq C_{a}^{s}(i)\right),\left(u_{a, i}, \emptyset \neq P_{i} \subseteq C_{a}^{u}(i)\right),\left(s_{a, i}, \emptyset\right),\left(u_{a, i}, \emptyset\right),(*, \emptyset)\right\}
$$

Specifically, the updates for these five pairs take the following form:

$$
\begin{aligned}
& M_{i \rightarrow a}\left(s_{a, i}, P_{i}=S \cup\{a\}\right)=\prod_{b \in S} M_{b \rightarrow i}^{s} \prod_{b \in C_{a}^{s}(i) \backslash S} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{u} \\
& M_{i \rightarrow a}\left(s_{a, i}, \emptyset \neq P_{i} \subseteq C_{a}^{s}(i)\right)=\prod_{b \in P_{i}} M_{b \rightarrow i}^{s} \prod_{b \in C_{a}^{s}(i) \backslash P_{i}} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{u} \\
& M_{i \rightarrow a}\left(u_{a, i}, \emptyset \neq P_{i} \subseteq C_{a}^{u}(i)\right)=\prod_{b \in P_{i}} M_{b \rightarrow i}^{s} \prod_{b \in C_{a}^{u}(i) \backslash P_{i}} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{s}(i)} M_{b \rightarrow i}^{u} \\
& M_{i \rightarrow a}\left(s_{a, i}, P_{i}=\emptyset\right)=\omega_{o} \prod_{b \in C_{a}^{s}(i)} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{u} \\
& M_{i \rightarrow a}\left(u_{a, i}, P_{i}=\emptyset\right)=\omega_{o} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{u} \\
& M_{i \rightarrow a}\left(*, P_{i}=\emptyset\right)=\omega_{*} \prod_{b \in C(i) \backslash\{a\}} M_{b \rightarrow i}^{*}
\end{aligned}
$$

Proof. The form of these updates follows immediately from the definition (10) of the variable compatibilities in the extended MRF, and the BP message update (27).

# B. 2 Forms of $R$ quantities 

In this section, we compute the specific forms of the linear sums of messages defined in equation (14). First, we use the definition (14a) and Lemma 16 to compute the form of $R_{i \rightarrow a}^{s}$ :

$$
\begin{aligned}
R_{i \rightarrow a}^{s} & :=\sum_{S \subseteq C_{a}^{s}(i)} M_{i \rightarrow a}\left(s_{a, i}, P_{i}=S \cup\{a\}\right) \\
& =\sum_{S \subseteq C_{a}^{s}(i)} \prod_{b \in S} M_{b \rightarrow i}^{s} \prod_{b \in C_{a}^{s}(i) \backslash S} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{u} \\
& =\prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{u}\left[\prod_{b \in C_{a}^{s}(i)}\left(M_{b \rightarrow i}^{s}+M_{b \rightarrow i}^{s}\right)\right]
\end{aligned}
$$

Similarly, the definition (14b) and Lemma 16 allows us compute the following form of $R_{i \rightarrow a}^{u}$ :

$$
\begin{aligned}
R_{i \rightarrow a}^{u} & =\sum_{S \subseteq C_{a}^{u}(i)} M_{i \rightarrow a}\left(u_{a, i}, P_{i}=S\right) \\
& =\sum_{S \subseteq C_{a}^{u}(i), S \neq \emptyset} \prod_{b \in S} M_{b \rightarrow i}^{s} \prod_{b \in C_{a}^{u}(i) \backslash S} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{s}(i)} M_{b \rightarrow i}^{u}+\omega_{o} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{s}(i)} M_{b \rightarrow i}^{u} \\
& =\prod_{b \in C_{a}^{s}(i)} M_{b \rightarrow i}^{u}\left[\prod_{b \in C_{a}^{u}(i)}\left(M_{b \rightarrow i}^{s}+M_{b \rightarrow i}^{*}\right)-\left(1-\omega_{o}\right) \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{*}\right]
\end{aligned}
$$

Finally, we compute $R_{i \rightarrow a}^{*}$ using the definition (14c) and Lemma 16:

$$
\begin{aligned}
R_{i \rightarrow a}^{*}= & {\left[\sum_{S \subseteq C_{a}^{s}(i)} M_{i \rightarrow a}\left(s_{a, i}, P_{i}=S\right)\right]+M_{i \rightarrow a}\left(*, P_{i}=\emptyset\right) } \\
= & {\left[\sum_{S \subseteq C_{a}^{s}(i), S \neq \emptyset} \prod_{b \in S} M_{b \rightarrow i}^{s} \prod_{b \in C_{a}^{s}(i) \backslash S} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{u}\right]+\omega_{o} \prod_{b \in C_{a}^{s}(i)} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{u}((i i)} M_{b \rightarrow i}^{u} \\
& +\omega_{*} \prod_{b \in C_{a}^{s}(i)} M_{b \rightarrow i}^{*} \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{*} \\
= & \prod_{b \in C_{a}^{u}(i)} M_{b \rightarrow i}^{u}\left[\prod_{b \in C_{a}^{s}(i)}\left(M_{b \rightarrow i}^{s}+M_{b \rightarrow i}^{*}\right)-\left(1-\omega_{o}\right) \prod_{b \in C_{a}^{s}(i)} M_{b \rightarrow i}^{*}\right]+\omega_{*} \prod_{b \in C_{a}^{s}(i) \cup C_{a}^{u}(i)} M_{b \rightarrow i}^{*}
\end{aligned}
$$

## B. 3 Clause to variable updates

In this section, we derive the form of the clause to variable updates.
Lemma 17 (Clause to variable messages). The updates of messages from clauses to variables in the extended MRF take the following form:

$$
\begin{aligned}
& M_{a \rightarrow i}^{s}=\prod_{j \in V(a) \backslash\{i\}} R_{j \rightarrow a}^{u} \\
& M_{a \rightarrow i}^{u}=\prod_{j \in V(a) \backslash\{i\}}\left(R_{j \rightarrow a}^{u}+R_{j \rightarrow a}^{*}\right)+\sum_{k \in V(a) \backslash\{i\}}\left(R_{k \rightarrow a}^{s}-R_{k \rightarrow a}^{*}\right) \prod_{j \in V(a) \backslash\{i, k\}} R_{j \rightarrow a}^{u}-\prod_{j \in V(a) \backslash\{i\}} R_{j \rightarrow a}^{u} \\
& M_{a \rightarrow i}^{*}=\prod_{j \in V(a) \backslash\{i\}}\left(R_{j \rightarrow a}^{u}+R_{j \rightarrow a}^{*}\right)-\prod_{j \in V(a) \backslash\{i\}} R_{j \rightarrow a}^{u}
\end{aligned}
$$

Proof. (i) We begin by proving equation (30a). When $x_{i}=s_{a, i}$ and $P_{i}=S \cup\{a\}$ for some $S \subseteq C_{a}^{s}(i)$, then the only possible assignment for the other variables at nodes in $V(a) \backslash\{i\}$ is $x_{j}=u_{a, j}$ and $P_{j} \subseteq C_{a}^{u}(j)$. Accordingly, using the BP update equation (26), we obtain the following update for $M_{a \rightarrow i}^{s}=M_{a \rightarrow i}\left(s_{a, i}, P_{i}=S \cup\{a\}\right)$ :

$$
\begin{aligned}
M_{a \rightarrow i}^{s} & =\prod_{j \in V(a) \backslash\{i\}} \sum_{P_{j} \subseteq C_{a}^{u}(j)} M_{j \rightarrow a}\left(u_{a, j}, P_{j}\right) \\
& =\prod_{j \in V(a) \backslash\{i\}} R_{j \rightarrow a}^{u}
\end{aligned}
$$

(ii) Next we prove equation (30c). In the case $x_{i}=*$ and $P_{i}=\emptyset$, the only restriction on the other variables $\left\{x_{j}: j \in V(a) \backslash\{i\}\right\}$ is that they are not all unsatisfying. The weight assigned to the event that they are all unsatisfying is

$$
\begin{aligned}
\sum_{\left\{S_{j} \subseteq C_{a}^{u}(j): j \in V(a) \backslash\{i\}\right\}} \prod_{j \in V(a) \backslash\{i\}} M_{j \rightarrow a}\left(u_{a, j}, S_{j}\right) & =\prod_{j \in V(a) \backslash\{i\}}\left[\sum_{S_{j} \subseteq C_{a}^{u}(j)} M_{j \rightarrow a}\left(u_{a, j}, S_{j}\right)\right] \\
& =\prod_{j \in V(a) \backslash\{i\}} R_{j \rightarrow a}^{u}
\end{aligned}
$$

On the other hand, the weight assigned to the event that each is either unsatisfying, satisfying or * can be calculated as follows. Consider a partition $J^{u} \cup J^{s} \cup J^{*}$ of the set $V(a) \backslash\{i\}$, where $J^{u}, J^{s}$ and $J^{*}$ corresponds to the subsets of unsatisfying, satisfying and $*$ assignments respectively. The weight $W\left(J^{u}, J^{s}, J^{*}\right)$ associated with this partition takes the form

$$
\sum_{\left\{S_{j} \subseteq C_{a}^{u}(j): j \in J^{u}\right\}} \sum_{\left\{S_{j} \subseteq C_{a}^{s}(j): j \in J^{s}\right\}} \prod_{j \in J^{u}} M_{j \rightarrow a}\left(u_{a, j}, S_{j}\right) \prod_{j \in J^{s}} M_{j \rightarrow a}\left(s_{a, j}, S_{j}\right) \prod_{j \in J^{*}} M_{j \rightarrow a}(*, \emptyset)
$$

Simplifying by distributing the sum and product leads to

$$
\begin{aligned}
W\left(J^{u}, J^{s}, J^{*}\right) & =\prod_{j \in J^{u}}\left[\sum_{S_{j} \subseteq C_{a}^{u}(j)} M_{j \rightarrow a}\left(u_{a, j}, S_{j}\right)\right] \prod_{j \in J^{*}}\left[\sum_{S_{j} \subseteq C_{a}^{s}(j)} M_{j \rightarrow a}\left(s_{a, j}, S_{j}\right)\right] \prod_{j \in J^{*}} M_{j \rightarrow a}(*, \emptyset) \\
& =\prod_{j \in J^{u}} R_{j \rightarrow a}^{u} \prod_{j \in J^{s}}\left[R_{j \rightarrow a}^{*}-M_{j \rightarrow a}(*, \emptyset)\right] \prod_{j \in J^{*}} M_{j \rightarrow a}(*, \emptyset)
\end{aligned}
$$

where we have used the definitions of $R_{j \rightarrow a}^{u}$ and $R_{j \rightarrow a}^{*}$ from Section B.2. Now summing $W\left(J^{u}, J^{s}, J^{*}\right)$ over all partitions $J^{u} \cup J^{s} \cup J^{*}$ of $V(a) \backslash\{i\}$ yields

$$
\begin{aligned}
& \sum_{J^{u} \cup J^{s} \cup J^{*}} W\left(J^{u}, J^{s}, J^{*}\right) \\
& =\sum_{J^{u} \subseteq V(a) \backslash\{i\}} \prod_{j \in J^{u}} R_{j \rightarrow a}^{u} \sum_{J^{s} \cup J^{*}=V(a) \backslash\left\{J^{u} \cup i\right\}}\left\{\prod_{j \in J^{s}}\left[R_{j \rightarrow a}^{*}-M_{j \rightarrow a}(*, \emptyset)\right] \prod_{j \in J^{*}} M_{j \rightarrow a}(*, \emptyset\right\} \\
& =\sum_{J^{u} \subseteq V(a) \backslash\{i\}} \prod_{j \in J^{u}} R_{j \rightarrow a}^{u} \prod_{j \in V(a) \backslash\left\{J^{u} \cup i\right\}} R_{j \rightarrow a}^{*} \\
& =\prod_{j \in V(a) \backslash\{i\}}\left[R_{j \rightarrow a}^{u}+R_{j \rightarrow a}^{*}\right]
\end{aligned}
$$

where we have used the binomial identity twice. Overall, equations (31) and (32) together yield that

$$
M_{a \rightarrow i}^{*}=\prod_{j \in V(a) \backslash\{i\}}\left[R_{j \rightarrow a}^{u}+R_{j \rightarrow a}^{*}\right]-\prod_{j \in V(a) \backslash\{i\}} R_{j \rightarrow a}^{u}
$$

which establishes equation (30c).
(iii) Finally, turning to equation (30b), for $x_{i}=u_{a, i}$ and $P_{i} \subseteq C_{a}^{u}(i)$, there are only two possibilities for the values of $x_{V(a) \backslash\{i\}}$ :
(a) either there is one satisfying variable and everything else is unsatisfying, or
(b) there are at least two variables that are satisfying or $*$.

We first calculate the weight $W(A)$ assigned to possibility (a), again using the BP update equation (26):

$$
\begin{aligned}
W(A) & =\sum_{k \in V(a) \backslash\{i\}} \sum_{S^{k} \subseteq C_{a}^{u}(k)} M_{k \rightarrow a}\left(s_{a, k}, S^{k} \cup\{a\}\right) \prod_{j \in V(a) \backslash\{i, k\}} \sum_{S^{j} \subseteq C_{a}^{u}(j)} M_{j \rightarrow a}\left(u_{j, a}, S^{j}\right) \\
& =\sum_{k \in V(a) \backslash\{i\}} R_{k \rightarrow a}^{s} \prod_{j \in V(a) \backslash\{i, k\}} R_{j \rightarrow a}^{u}
\end{aligned}
$$

where we have used the definitions of $R_{k \rightarrow a}^{s}$ and $R_{k \rightarrow a}^{u}$ from Section B.2.
We now calculate the weight $W(B)$ assigned to possibility (b) in the following way. From our calculations in part (ii), we found that the weight assigned to the event that each variable is either unsatisfying, satisfying or $*$ is $\prod_{j \in V(a) \backslash\{i\}}\left[R_{j \rightarrow a}^{u}+R_{j \rightarrow a}^{*}\right]$. The weight $W(B)$ is given by subtracting from this quantity the weight assigned to the event that there are not at least two $*$ or satisfying assignments. This event can be decomposed into the disjoint events that either all assignments are unsatisfying (with weight $\prod_{j \in V(a) \backslash\{i\}} R_{j \rightarrow a}^{u}$ from part (ii)); or that exactly one variable is $*$ or satisfying. The weight corresponding to this second possibility is

$$
\begin{aligned}
\sum_{k \in V(a) \backslash\{i\}} & {\left[M_{k \rightarrow a}(*, \emptyset)+\sum_{S^{k} \subseteq C_{a}^{u}(k)} M_{k \rightarrow a}\left(s_{k, a}, S^{k}\right)\right] \prod_{j \in V(a) \backslash\{i, k\}} \sum_{S^{j} \subseteq C_{j}^{u}(a)} M_{j \rightarrow a}\left(u_{j, a}, S^{j}\right) } \\
& =\sum_{k \in V(a) \backslash\{i\}} R_{k \rightarrow a}^{*} \prod_{j \in V(a) \backslash\{i, k\}} R_{j \rightarrow a}^{u}
\end{aligned}
$$

Combining our calculations so far we have

$$
W(B)=\prod_{j \in V(a) \backslash\{i\}}\left[R_{j \rightarrow a}^{u}+R_{j \rightarrow a}^{*}\right]-\sum_{k \in V(a) \backslash\{i\}} R_{k \rightarrow a}^{*} \prod_{j \in V(a) \backslash\{i, k\}} R_{j \rightarrow a}^{u}-\prod_{j \in V(a) \backslash\{i\}} R_{j \rightarrow a}^{u}
$$

Finally, summing together the forms of $W(A)$ and $W(B)$ from equations (33) and (34) respectively, and then factoring yields the desired equation (30b).

# C Proofs for random formulae 

## C. 1 Proof of Lemma 11

In order to prove (21), it suffices by the Markov inequality to show that for every integer $d$ in the interval $[\delta n, 2 \delta n]$, it holds that

$$
\frac{\mathbb{E}^{n}\left[W^{\phi}\left[n-n_{*}=d\right]\right]}{\rho^{3 n}}=\exp (-\Omega(n))
$$

To establish (35), consider a fixed set of $d$ variables. The average $W$-weight assigned to the event that this set of size $d$ constitutes all the non-star variables is bounded by

$$
\rho^{n-d} \sum_{r=0}^{d}(1-\rho)^{d-r}\binom{d}{r}\binom{\alpha n}{r}(d / n)^{k r}
$$

where $r$ represents the number of constrained variables. We obtain this bound by the following reasoning. First, the $n-d$ variables assigned $*$ all receive weight $\rho$. Otherwise, if $r$ out of the remaining $d$ variables are constrained, there must be $r$ clauses chosen from a total of $\alpha n$, and each such clause must have all of its $k$ variables chosen from within the set of $d$ non-star variables.

Consequently, the total probability of having $d$ non-star variables is bounded by

$$
\begin{aligned}
\rho^{n-d}\binom{n}{d} \sum_{r=0}^{d}(1-\rho)^{d-r}\binom{d}{r}\binom{\alpha n}{r}\left(\frac{d}{n}\right)^{k r} & \leq \rho^{n-d}\left(\frac{e n}{d}\right)^{d} \sum_{r=0}^{d}(1-\rho)^{d-r}\left(\frac{e d}{r}\right)^{r}\left(\frac{\alpha e n}{r}\right)^{r}\left(\frac{d}{n}\right)^{k r} \\
& =\rho^{n-d}\left(\frac{(1-\rho) e n}{d}\right)^{d} \sum_{r=0}^{d}\left(\frac{e^{2} d^{k+1} \alpha}{r^{2}(1-\rho) n^{k-1}}\right)^{r}
\end{aligned}
$$

Recalling that $1-\rho=\delta^{2}$ and $d \in[\delta n, 2 \delta n]$, we obtain that the last expression is at most

$$
\begin{aligned}
\rho^{n-2 \delta n}\left(\frac{\delta^{2} e n}{\delta n}\right)^{d} \sum_{r=0}^{2 \delta n}\left(\frac{e^{2}(2 \delta n)^{k+1} \alpha}{r^{2} \delta^{2} n^{k-1}}\right)^{r} & =\rho^{n-2 \delta n}(\delta e)^{d} \sum_{r=0}^{2 \delta n}\left(\frac{e^{2} 2^{k+1} \delta^{k-1} n^{2} \alpha}{r^{2}}\right)^{r} \\
& \leq \rho^{n-2}(\delta e)^{\delta n} \sum_{r=0}^{2 \delta n}\left(\frac{2^{k+1} \alpha \delta^{k-1} n^{2} e^{2}}{r^{2}}\right)^{r}
\end{aligned}
$$

where the final inequality is valid when $\delta e<1$. A straightforward calculation yields that the function $g(r):=\left(\frac{2^{k+1} \alpha \delta^{k-1} e^{2} n^{2}}{r^{2}}\right)^{r}$ is maximized at $r^{*}=\sqrt{2^{k+1} \alpha \delta^{k-1}} n$ and the associated value is $g\left(r^{*}\right)=e^{2 r^{*}}$. Consequently, the sum above is bounded by

$$
\begin{aligned}
2 \delta n \rho^{n-2 \delta n}(\delta e)^{\delta n} e^{2 r^{*}} & =2 \delta n \rho^{n-2 \delta n}\left[\delta \exp \left(1+\frac{2 r^{*}}{\delta n}\right)\right]^{\delta n} \\
& =2 \delta n \rho^{n-2 \delta n}\left[\delta \exp \left(1+\sqrt{2^{k+3} \alpha \delta^{k-3}}\right)\right]^{\delta n} \\
& \leq 2 \delta n \rho^{n-2 \delta n}\left[\delta \exp \left(1+\sqrt{2^{k+3} \alpha}\right)\right]^{\delta n}
\end{aligned}
$$

This expression is exponentially smaller than $\rho^{3 n}$ for large $n$ if

$$
\left[\delta \exp \left(1+\sqrt{2^{k+3} \alpha}\right)\right]^{\delta}<\rho^{3}=\left(1-\delta^{2}\right)^{3}
$$

Inequality (36) holds for sufficiently small $\delta>0$, which establishes the lemma.

# C. 2 Proof of Lemma 13 

It will be useful to denote $\prod_{b \in C_{a}^{s}(i)}\left(1-\eta_{b \rightarrow i}\right)$ by $P_{s}(i)$ and $\prod_{b \in C_{a}^{u}(i)}\left(1-\eta_{b \rightarrow i}\right)$ by $P_{u}(j)$. With this notation, the $j$ 'th term in (6) is given by

$$
\begin{aligned}
\frac{\Pi_{j \rightarrow a}^{u}}{\Pi_{j \rightarrow a}^{u}+\Pi_{j \rightarrow a}^{s}+\Pi_{j \rightarrow a}^{s}} & =\frac{\left(1-\rho P_{u}(j)\right) P_{s}(j)}{\left(1-\rho P_{u}(j)\right) P_{s}(j)+\left(1-P_{s}(j)\right) P_{u}(j)+P_{s}(j) P_{u}(j)} \\
& =\frac{\left(1-\rho P_{u}(j)\right) P_{s}(j)}{P_{s}(j)+P_{u}(j)-\rho P_{s}(j) P_{u}(j)} \leq 1-\rho P_{u}(j)
\end{aligned}
$$

We therefore conclude that

$$
\eta_{a \rightarrow i} \leq \prod_{j \in V(a) \backslash\{i\}}\left(1-\rho P_{u}(j)\right)
$$

On the other hand, we have $P_{u}(j)=\prod_{b \in C_{a}^{u}(i)}\left(1-\eta_{b \rightarrow i}\right) \geq \max \left(0,1-\sum_{b \in C_{a}^{u}(i)} \eta_{b \rightarrow i}\right)$, so that

$$
1-\rho P_{u}(j) \leq \min \left(1,(1-\rho)+\rho \sum_{b \in C_{a}^{u}(i)} \eta_{b \rightarrow i}\right)
$$

This yields the bound $\eta_{a \rightarrow i}^{t+1} \leq \prod_{j \in V(a) \backslash\{i\}} \min \left(1,(1-\rho)+\rho \sum_{b \in C_{a}^{u}(i)} \eta_{b \rightarrow j}^{t}\right)$, from which equation (22) follows.

## C. 3 Proof of Lemma 15

We start by estimating the probability that a vertex is bad by induction. Let $g_{K}$ denote the probability that $v$ has more than $K$ children, or that one of $v$ 's children has more than $K$ children. Clearly,

$$
g_{K} \leq(K+1) \mathbb{P}[Y \geq K] \leq(K+1)(k-1) \mathbb{P}\left[\operatorname{Bin}\left(M_{c}, \frac{\alpha n}{N_{c}}\right) \geq \frac{K}{k-1}\right] \leq \exp (-\Omega(K))
$$

Write $q(m, K)=1-p(m, K)$ and note that $q(0, K)=0$ and $q(1, K) \leq g_{K}$. By induction, A vertex can be bad for two reasons: it has two many descendants in the two levels below it, or it has 2 bad descendant in the two levels below it. We may thus bound the probability of a vertex being bad as

$$
q(s, K) \leq g_{K}+\mathbb{P}\left[\operatorname{Bin}\left(K^{2}, q(s-2, K)\right) \geq 2\right]
$$

Note also that

$$
\mathbb{P}\left[\operatorname{Bin}\left(K^{2}, q(s-2, K)\right) \geq 2\right] \leq K^{4} q(s-2, K)^{2}
$$

Combining (38) and (39) yields

$$
q(s, K) \leq g_{K}+K^{4} q(s-2, K)^{2}
$$

By (37) when $K$ is sufficiently large $K^{4}\left(2 g_{K}\right)^{2}<g_{K}$. Thus when $K$ is sufficiently large, it follows from equation (40) that

$$
q(s, K) \leq 2 g_{K}
$$

for all $s$. Finally when $K$ is sufficiently large $p(s, K) \geq 1-2 g_{K}$ for all $s$ and $1-2 g_{K} \geq 1-$ $\exp (-\Omega(K))$ as needed.
