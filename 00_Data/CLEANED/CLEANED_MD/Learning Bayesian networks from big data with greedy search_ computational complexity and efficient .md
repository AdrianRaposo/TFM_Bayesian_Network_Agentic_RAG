# Learning Bayesian networks from big data with greedy search: computational complexity and efficient implementation 

Marco Scutari ${ }^{1} \cdot$ Claudia Vitolo ${ }^{2} \cdot$ Allan Tucker ${ }^{3}$<br>Received: 21 April 2018 / Accepted: 2 February 2019 / Published online: 15 February 2019<br>© The Author(s) 2019


#### Abstract

Learning the structure of Bayesian networks from data is known to be a computationally challenging, NP-hard problem. The literature has long investigated how to perform structure learning from data containing large numbers of variables, following a general interest in high-dimensional applications ("small $n$, large $p$ ") in systems biology and genetics. More recently, data sets with large numbers of observations (the so-called "big data") have become increasingly common; and these data sets are not necessarily high-dimensional, sometimes having only a few tens of variables depending on the application. We revisit the computational complexity of Bayesian network structure learning in this setting, showing that the common choice of measuring it with the number of estimated local distributions leads to unrealistic time complexity estimates for the most common class of score-based algorithms, greedy search. We then derive more accurate expressions under common distributional assumptions. These expressions suggest that the speed of Bayesian network learning can be improved by taking advantage of the availability of closed-form estimators for local distributions with few parents. Furthermore, we find that using predictive instead of in-sample goodness-of-fit scores improves speed; and we confirm that it improves the accuracy of network reconstruction as well, as previously observed by Chickering and Heckerman (Stat Comput 10: 55-62, 2000). We demonstrate these results on large real-world environmental and epidemiological data; and on reference data sets available from public repositories.


Keywords Bayesian networks $\cdot$ Structure Learning $\cdot$ Big Data $\cdot$ Computational Complexity

## 1 Introduction

Bayesian networks (BNs; Pearl 1988) are a class of graphical models defined over a set of random variables $\mathbf{X}=$ $\left\{X_{1}, \ldots, X_{N}\right\}$, each describing some quantity of interest, that are associated with the nodes of a directed acyclic graph (DAG) $\mathcal{G}$. (They are often referred to interchangeably.) Arcs in $\mathcal{G}$ express direct dependence relationships between the variables in $\mathbf{X}$, with graphical separation in $\mathcal{G}$ implying conditional independence in probability. As a result, $\mathcal{G}$ induces the factorisation

[^0]$\mathrm{P}(\mathbf{X} \mid \mathcal{G}, \Theta)=\prod_{i=1}^{N} \mathrm{P}\left(X_{i} \mid \Pi_{X_{i}}, \Theta_{X_{i}}\right)$,
in which the joint probability distribution of $\mathbf{X}$ (with parameters $\Theta$ ) decomposes in one local distribution for each $X_{i}$ (with parameters $\Theta_{X_{i}}, \bigcup_{\mathbf{X}} \Theta_{X_{i}}=\Theta$ ) conditional on its parents $\Pi_{X_{i}}$.

While in principle there are many possible choices for the distribution of $\mathbf{X}$, the literature has focused mostly on three cases. Discrete BNs (Heckerman et al. 1995) assume that both $\mathbf{X}$ and the $X_{i}$ are multinomial random variables. Local distributions take the form
$X_{i} \mid \Pi_{X_{i}} \sim \operatorname{Mul}\left(\pi_{i k \mid j}\right), \quad \pi_{i k \mid j}=\mathrm{P}\left(X_{i}=k \mid \Pi_{X_{i}}=j\right)$;
their parameters are the conditional probabilities of $X_{i}$ given each configuration of the values of its parents, usually represented as a conditional probability table for each $X_{i}$. Gaussian BNs (GBNs; Geiger and Heckerman 1994) model $\mathbf{X}$ with a multivariate normal random variable and assume


[^0]:    1 Department of Statistics, University of Oxford, 24-29 St. Giles', Oxford OX1 3LB, UK
    2 Forecast Department, European Centre for Medium-range Weather Forecast, Reading, UK
    3 Department of Computer Science, Brunel University London, Kingston Lane, Uxbridge, UK

that the $X_{i}$ are univariate normals linked by linear dependencies. The parameters of the local distributions can be equivalently written (Weatherburn 1961) as the partial Pearson correlations $\rho_{X_{i}, X_{j} \mid \Pi_{X_{i}} \backslash X_{j}}$ between $X_{i}$ and each parent $X_{j}$ given the other parents; or as the coefficients $\boldsymbol{\beta}_{X_{i}}$ of the linear regression model
$X_{i}=\mu_{X_{i}}+\Pi_{X_{i}} \boldsymbol{\beta}_{X_{i}}+\varepsilon_{X_{i}}, \quad \varepsilon_{X_{i}} \sim N\left(0, \sigma_{X_{i}}^{2}\right)$,
so that $X_{i} \mid \Pi_{X_{i}} \sim N\left(\mu_{X_{i}}+\Pi_{X_{i}} \boldsymbol{\beta}_{X_{i}}, \sigma_{X_{i}}^{2}\right)$. Finally, conditional linear Gaussian BNs (CLGBNs; Lauritzen and Wermuth 1989) combine discrete and continuous random variables in a mixture model:

- discrete $X_{i}$ are only allowed to have discrete parents (denoted $\Delta_{X_{i}}$ ), are assumed to follow a multinomial distribution parameterised with conditional probability tables;
- continuous $X_{i}$ are allowed to have both discrete and continuous parents (denoted $\Gamma_{X_{i}}, \Delta_{X_{i}} \cup \Gamma_{X_{i}}=\Pi_{X_{i}}$ ), and their local distributions are
$X_{i} \mid \Pi_{X_{i}} \sim N\left(\mu_{X_{i}, \delta_{X_{i}}}+\Gamma_{X_{i}} \boldsymbol{\beta}_{X_{i}, \delta_{X_{i}}}, \sigma_{X_{i}, \delta_{X_{i}}}^{2}\right)$
which can be written as a mixture of linear regressions

$$
\begin{aligned}
X_{i}= & \mu_{X_{i}, \delta_{X_{i}}}+\Gamma_{X_{i}} \boldsymbol{\beta}_{X_{i}, \delta_{X_{i}}}+\varepsilon_{X_{i}, \delta_{X_{i}}} \\
& \varepsilon_{X_{i}, \delta_{X_{i}}} \sim N\left(0, \sigma_{X_{i}, \delta_{X_{i}}}^{2}\right)
\end{aligned}
$$

against the continuous parents with one component for each configuration $\delta_{X_{i}} \in \operatorname{Val}\left(\Delta_{X_{i}}\right)$ of the discrete parents. If $X_{i}$ has no discrete parents, the mixture reverts to a single linear regression.

Other distributional assumptions, such as mixtures of truncated exponentials (Moral et al. 2001) or copulas (Elidan 2010), have been proposed in the literature but have seen less widespread adoption due to the lack of exact conditional inference and simple closed-form estimators.

The task of learning a BN from a data set $\mathcal{D}$ containing $n$ observations is performed in two steps:
$\underbrace{\mathrm{P}(\mathcal{G}, \Theta \mid \mathcal{D})}_{\text {learning }}=\underbrace{\mathrm{P}(\mathcal{G} \mid \mathcal{D})}_{\text {structure learning }} \cdot \underbrace{\mathrm{P}(\Theta \mid \mathcal{G}, \mathcal{D})}_{\text {parameter learning }}$.
Structure learning consists in finding the DAG $\mathcal{G}$ that encodes the dependence structure of the data, thus maximising $\mathrm{P}(\mathcal{G} \mid \mathcal{D})$ or some alternative goodness-of-fit measure; parameter learning consists in estimating the parameters $\Theta$ given the $\mathcal{G}$ obtained from structure learning. If we assume parameters in different local distributions are independent
(Heckerman et al. 1995), we can perform parameter learning independently for each node following (1) because
$\mathrm{P}(\Theta \mid \mathcal{G}, \mathcal{D})=\prod_{i=1}^{N} \mathrm{P}\left(\Theta_{X_{i}} \mid \Pi_{X_{i}}, \mathcal{D}\right)$.

Furthermore, if $\mathcal{G}$ is sufficiently sparse each node will have a small number of parents; and $X_{i} \mid \Pi_{X_{i}}$ will have a lowdimensional parameter space, making parameter learning computationally efficient.

On the other hand, structure learning is well known to be both NP-hard (Chickering and Heckerman 1994) and NP-complete (Chickering 1996), even under unrealistically favourable conditions such as the availability of an independence and inference oracle (Chickering et al. 2004). ${ }^{1}$ This is despite the fact that if we take
$\mathrm{P}(\mathcal{G} \mid \mathcal{D}) \propto \mathrm{P}(\mathcal{G}) \mathrm{P}(\mathcal{D} \mid \mathcal{G})$,
again following (1) we can decompose the marginal likelihood $\mathrm{P}(\mathcal{D} \mid \mathcal{G})$ into one component for each local distribution

$$
\begin{aligned}
\mathrm{P}(\mathcal{D} \mid \mathcal{G}) & =\int \mathrm{P}(\mathcal{D} \mid \mathcal{G}, \Theta) \mathrm{P}(\Theta \mid \mathcal{G}) d \Theta \\
& =\prod_{i=1}^{N} \int \mathrm{P}\left(X_{i} \mid \Pi_{X_{i}}, \Theta_{X_{i}}\right) \mathrm{P}\left(\Theta_{X_{i}} \mid \Pi_{X_{i}}\right) d \Theta_{X_{i}}
\end{aligned}
$$

and despite the fact that each component can be written in closed form for discrete BNs (Heckerman et al. 1995), GBNs (Geiger and Heckerman 1994) and CLGBNs (Bøttcher 2001). The same is true if we replace $\mathrm{P}(\mathcal{D} \mid \mathcal{G})$ with frequentist goodness-of-fit scores such as BIC (Schwarz 1978), which is commonly used in structure learning because of its simple expression:
$\operatorname{BIC}(\mathcal{G}, \Theta \mid \mathcal{D})=\sum_{i=1}^{N} \log \mathrm{P}\left(X_{i} \mid \Pi_{X_{i}}, \Theta_{X_{i}}\right)-\frac{\log (n)}{2}\left|\Theta_{X_{i}}\right|$.

Compared to marginal likelihoods, BIC has the advantage that it does not depend on any hyperparameter, while converging to $\log \mathrm{P}(\mathcal{D} \mid \mathcal{G})$ as $n \rightarrow \infty$.

These score functions, which we will denote with $\operatorname{Score}(\mathcal{G}, \mathcal{D})$ in the following, have two important properties:

[^0]
[^0]:    ${ }^{1}$ Interestingly, some relaxations of BN structure learning are not NPhard; see for example Claassen et al. (2013) on learning the structure of causal networks.

- they decompose into one component for each local distribution following (1), say

$$
\operatorname{Score}(\mathcal{G}, \mathcal{D})=\sum_{i=1}^{N} \operatorname{Score}\left(X_{i}, \Pi_{X_{i}}, \mathcal{D}\right)
$$

thus allowing local computations (decomposability);

- they assign the same score value to DAGs that encode the same probability distributions and can therefore be grouped in an equivalence classes (score equivalence; Chickering 1995). ${ }^{2}$

Structure learning via score maximisation is performed using general-purpose optimisation techniques, typically heuristics, adapted to take advantage of these properties to increase the speed of structure learning. The most common are greedy search strategies that employ local moves designed to affect only few local distributions, to that new candidate DAGs can be scored without recomputing the full $\mathrm{P}(\mathcal{D} \mid \mathcal{G})$. This can be done either in the space of the DAGs with hill climbing and tabu search (Russell and Norvig 2009), or in the space of the equivalence classes with Greedy Equivalent Search (GES; Chickering 2002). Other options that have been explored in the literature are genetic algorithms (Larranaga et al. 1996) and ant colony optimisation (Campos et al. 2002). Exact maximisation of $\mathrm{P}(\mathcal{D} \mid \mathcal{G})$ and BIC has also become feasible for small data sets in recent years thanks to increasingly efficient pruning of the space of the DAGs and tight bounds on the scores (Cussens 2012; Suzuki 2017; Scanagatta et al. 2015).

In addition, we note that it is also possible to perform structure learning using conditional independence tests to learn conditional independence constraints from $\mathcal{D}$, and thus identify which arcs should be included in $\mathcal{G}$. The resulting algorithms are called constraint-based algorithms, as opposed to the score-based algorithms we introduced above; for an overview and a comparison of these two approaches see Scutari and Denis (2014). Chickering et al. (2004) proved that constraint-based algorithms are also NP-hard for unrestricted DAGs; and they are in fact equivalent to score-based algorithms given a fixed topological ordering when independence constraints are tested with statistical tests related to cross-entropy (Cowell 2001). For these reasons, in this paper we will focus only on score-based algorithms while recognising that a similar investigation of constraint-based algorithms represents a promising direction for future research.

The contributions of this paper are:

1. to provide general expressions for the (time) computational complexity of the most common class of score-
[^0]based structure learning algorithms, greedy search, as a function of the number of variables $N$, of the sample size $n$, and of the number of parameters $|\Theta|$;
2. to use these expressions to identify two simple yet effective optimisations to speed up structure learning in "big data" settings in which $n \gg N$.

Both are increasingly important when using BNs in modern machine learning applications, as data sets with large numbers of observations (the so-called "big data") are becoming as common as classic high-dimensional data ("small $n$, large $p$ ", or "small $n$, large $N$ " using the notation introduced above). The vast majority of complexity and scalability results (Kalisch and Bühlmann 2007; Scanagatta et al. 2015) and computational optimisations (Scutari 2017) in the literature are derived in the latter setting and implicitly assume $n \ll N$; they are not relevant in the former setting in which $n \gg N$. Our contributions also complement related work on advanced data structures for machine learning applications, which include ADtrees (Moore and Lee 1998), frequent sets (Goldenberg and Moore 2004) and more recently bitmap representations combined with radix sort (Karan et al. 2018). Such literature develops a framework for caching sufficient statistics, but concentrates on discrete variables, whereas we work in a more general setting in which data can include both discrete and continuous variables.

The material is organised as follows. In Sect. 2, we will present in detail how greedy search can be efficiently implemented thanks to the factorisation in (1), and we will derive its computational complexity as a function $N$; this result has been mentioned in many places in the literature, but to the best of our knowledge its derivation has not been described in depth. In Sect. 3, we will then argue that the resulting expression does not reflect the actual computational complexity of structure learning, particularly in a "big data" setting where $n \gg N$; and we will re-derive it in terms of $n$ and $|\Theta|$ for the three classes of BNs described above. In Sect. 4, we will use this new expression to identify two optimisations that can markedly improve the overall speed of learning GBNs and CLGBNs by leveraging the availability of closed-form estimates for the parameters of the local distributions and out-of-sample goodness-of-fit scores. Finally, in Sect. 5 we will demonstrate the improvements in speed produced by the proposed optimisations on simulated and real-world data, as well as their effects on the accuracy of learned structures.

## 2 Computational complexity of greedy search

A state-of-the-art implementation of greedy search in the context of BN structure learning is shown in Algorithm 1. It consists of an initialisation phase (steps 1 and 2) followed


[^0]:    ${ }^{2}$ All DAGs in the same equivalence class have the same underlying undirected graph and v-structures (patterns of arcs like $X_{i} \rightarrow X_{j} \leftarrow$ $X_{k}$, with no arcs between $X_{i}$ and $X_{k}$ ).

## Algorithm 1 Greedy Search

Input: a data set $\mathcal{D}$ from $\mathbf{X}$, an initial $\mathrm{DAG} \mathcal{G}$ (usually the empty DAG), a score function $\operatorname{Score}(\mathcal{G}, \mathcal{D})$.
Output: the DAG $\mathcal{G}_{\text {max }}$ that maximises $\operatorname{Score}(\mathcal{G}, \mathcal{D})$.

1. Compute the score of $\mathcal{G}, S_{\mathcal{G}}=\operatorname{Score}(\mathcal{G}, \mathcal{D})$.
2. Set $S_{\max }=S_{\mathcal{G}}$ and $\mathcal{G}_{\max }=\mathcal{G}$.
3. Hill climbing: repeat as long as $S_{\max }$ increases:
(a) for every possible arc addition, deletion or reversal in $\mathcal{G}_{\max }$ resulting in a DAG:
i. compute the score of the modified DAG $\mathcal{G}^{*}, S_{\mathcal{G}^{*}}=$ $\operatorname{Score}\left(\mathcal{G}^{*}, \mathcal{D}\right)$ :
ii. if $S_{\mathcal{G}^{*}}>S_{\max }$ and $S_{\mathcal{G}^{*}}>S_{\mathcal{G}}$, set $\mathcal{G}=\mathcal{G}^{*}$ and $S_{\mathcal{G}}=S_{\mathcal{G}^{*}}$.
(b) if $S_{\mathcal{G}}>S_{\max }$, set $S_{\max }=S_{\mathcal{G}}$ and $\mathcal{G}_{\max }=\mathcal{G}$.
4. Tabu search: for up to $t_{0}$ times:
(a) repeat step 3 but choose the DAG $\mathcal{G}$ with the highest $S_{\mathcal{G}}$ that has not been visited in the last $t_{1}$ steps regardless of $S_{\max }$;
(b) if $S_{\mathcal{G}}>S_{\max }$, set $S_{0}=S_{\max }=S_{\mathcal{G}}$ and $\mathcal{G}_{0}=\mathcal{G}_{\max }=\mathcal{G}$ and restart the search from step 3 .
5. Random restart: for up to $r$ times, perturb $\mathcal{G}_{\max }$ with multiple arc additions, deletions and reversals to obtain a new DAG $\mathcal{G}^{\prime}$ and:
(a) set $S_{0}=S_{\max }=S_{\mathcal{G}}$ and $\mathcal{G}_{0}=\mathcal{G}_{\max }=\mathcal{G}$ and restart the search from step 3 ;
(b) if the new $\mathcal{G}_{\max }$ is the same as the previous $\mathcal{G}_{\max }$, stop and return $\mathcal{G}_{\max }$.
by a hill climbing search (step 3), which is then optionally refined with tabu search (step 4) and random restarts (step 5). Minor variations of this algorithm have been used in large parts of the literature on BN structure learning with scorebased methods (some notable examples are Heckerman et al. 1995; Tsamardinos et al. 2006; Friedman 1997).

Hill climbing uses local moves (arc additions, deletions and reversals) to explore the neighbourhood of the current candidate DAG $\mathcal{G}_{\max }$ in the space of all possible DAGs in order to find the DAG $\mathcal{G}$ (if any) that increases the score $\operatorname{Score}(\mathcal{G}, \mathcal{D})$ the most over $\mathcal{G}_{\max }$. That is, in each iteration hill climbing tries to delete and reverse each arc in the current optimal DAG $\mathcal{G}_{\max }$; and to add each possible arc that is not already present in $\mathcal{G}_{\max }$. For all the resulting DAGs $\mathcal{G}^{*}$ that are acyclic, hill climbing then computes $S_{\mathcal{G}^{*}}=\operatorname{Score}\left(\mathcal{G}^{*}, \mathcal{D}\right)$; cyclic graphs are discarded. The $\mathcal{G}^{*}$ with the highest $S_{\mathcal{G}^{*}}$ becomes the new candidate DAG $\mathcal{G}$. If that DAG has a score $S_{\mathcal{G}}>S_{\max }$ then $\mathcal{G}$ becomes the new $\mathcal{G}_{\max }, S_{\max }$ will be set to $S_{\mathcal{G}}$, and hill climbing will move to the next iteration.

This greedy search eventually leads to a DAG $\mathcal{G}_{\max }$ that has no neighbour with a higher score. Since hill climbing is an optimisation heuristic, there is no theoretical guarantee that $\mathcal{G}_{\max }$ is a global maximum. In fact, the space of the DAGs grows super-exponentially in $N$ (Harary and Palmer 1973); hence, multiple local maxima are likely present even if the sample size $n$ is large. The problem may be compounded by the existence of score-equivalent DAGs, which by definition have the same $S_{\mathcal{G}}$ for all the $\mathcal{G}$ falling in the same equivalence
class. However, Gillispie and Perlman (2002) have shown that while the number of equivalence classes is of the same order of magnitude as the space of the DAGs, most contain few DAGs and as many as $27.4 \%$ contain just a single DAG. This suggests that the impact of score equivalence on hill climbing may be limited. Furthermore, greedy search can be easily modified into GES to work directly in the space of equivalence classes by using different set of local moves, side-stepping this possible issue entirely.

In order to escape from local maxima, greedy search first tries to move away from $\mathcal{G}_{\max }$ by allowing up to $t_{0}$ additional local moves. These moves necessarily produce DAGs $\mathcal{G}^{*}$ with $S_{\mathcal{G} *} \leqslant S_{\max }$; hence, the new candidate DAGs are chosen to have the highest $S_{\mathcal{G}}$ even if $S_{\mathcal{G}}<S_{\max }$. Furthermore, DAGs that have been accepted as candidates in the last $t_{1}$ iterations are kept in a list (the tabu list) and are not considered again in order to guide the search towards unexplored regions of the space of the DAGs. This approach is called tabu search (step 4) and was originally proposed by Glover and Laguna (1998). If a new DAG with a score larger than $\mathcal{G}_{\max }$ is found in the process, that DAG is taken as the new $\mathcal{G}_{\max }$ and greedy search returns to step 3 , reverting to hill climbing.

If, on the other hand, no such DAG is found then greedy search tries again to escape the local maximum $\mathcal{G}_{\max }$ for $r_{0}$ times with random non-local moves, that is, by moving to a distant location in the space of the DAGs and starting the greedy search again; hence, the name random restart (step 5). The non-local moves are typically determined by applying a batch of $r_{1}$ randomly chosen local moves that substantially alter $\mathcal{G}_{\max }$. If the DAG that was perturbed was indeed the global maximum, the assumption is that this second search will also identify it as the optimal DAG, in which case the algorithm terminates.

We will first study the (time) computational complexity of greedy search under the assumptions that are commonly used in the literature (see, for instance, Tsamardinos et al. 2006; Spirtes et al. 2001) for this purpose:

1. We treat the estimation of each local distribution as an atomic $O(1)$ operation; that is, the (time) complexity of structure learning is measured by the number of estimated local distributions.
2. Model comparisons are assumed to always add, delete and reverse arcs correctly with respect to the underlying true model which happens asymptotically for $n \rightarrow \infty$ since marginal likelihoods and BIC are globally and locally consistent (Chickering 2002).
3. The true DAG $\mathcal{G}_{\text {REF }}$ is sparse and contains $O(c N)$ arcs, where $c$ is typically assumed to be between 1 and 5 .

In steps 1 and 2, greedy search computes all the $N$ local distributions for $\mathcal{G}_{0}$. In step 3, each iteration tries all possible arc additions, deletions and reversals. Since there are $\binom{N}{2}$

possible arcs in a DAG with $N$ nodes, this requires $O\left(N^{2}\right)$ model comparisons. If we assume $\mathcal{G}_{0}$ is the empty DAG (that is, a DAG with no arcs), hill climbing will gradually add all the arcs in $\mathcal{G}_{\text {REF }}$, one in each iteration. Assuming $\mathcal{G}_{\text {REF }}$ is sparse, and assuming that arcs are removed or reversed a negligible number of times, the overall computational complexity of hill climbing is then $O\left(c N^{3}\right)$ model comparisons. Step 4 performs $t_{0}$ more iterations and is therefore $O\left(t_{0} N^{2}\right)$. Therefore, the combined time complexity of steps 3 and 4 is $O\left(c N^{3}+t_{0} N^{2}\right)$. Each of the random restarts involves changing $r_{1}$ arcs, and thus we can expect that it will take $r_{1}$ iterations of hill climbing to go back to the same maximum, followed by tabu search; and that happens for $r_{0}$ times. Overall, this adds $O\left(r_{0}\left(r_{1} N^{2}+t_{0} N^{2}\right)\right)$ to the time complexity, resulting in an overall complexity $g(N)$ of

$$
\begin{aligned}
O(g(N)) & =O\left(c N^{3}+t_{0} N^{2}+r_{0}\left(r_{1} N^{2}+t_{0} N^{2}\right)\right) \\
& =O\left(c N^{3}+\left(t_{0}+r_{0}\left(r_{1}+t_{0}\right)\right) N^{2}\right)
\end{aligned}
$$

The leading term is $O\left(c N^{3}\right)$ for some small constant $c$, making greedy search cubic in complexity.

Fortunately, the factorisation in (1) makes it possible to recompute only one or two local distributions for each model comparison:

- Adding or removing an arc only alters one parent set; for instance, adding $X_{j} \rightarrow X_{i}$ means that $\Pi_{X_{i}}=$ $\Pi_{X_{i}} \cup X_{j}$, and therefore $\mathrm{P}\left(X_{i} \mid \Pi_{X_{i}}\right)$ should be updated to $\mathrm{P}\left(X_{i} \mid \Pi_{X_{i}} \cup X_{j}\right)$. All the other local distributions $\mathrm{P}\left(X_{k} \mid \Pi_{X_{j}}\right), X_{k} \neq X_{i}$ are unchanged.
- Reversing an arc $X_{j} \rightarrow X_{i}$ to $X_{i} \rightarrow X_{j}$ means that $\Pi_{X_{i}}=\Pi_{X_{i}} \backslash X_{j}$ and $\Pi_{X_{j}}=\Pi_{X_{j}} \cup X_{i}$, and so both $\mathrm{P}\left(X_{i} \mid \Pi_{X_{i}}\right)$ and $\mathrm{P}\left(X_{j} \mid \Pi_{X_{j}}\right)$ should be updated.

Hence, it is possible to dramatically reduce the computational complexity of greedy search by keeping a cache of the score values of the $N$ local distributions for the current $\mathcal{G}_{\max }$
$B_{i}=\operatorname{Score}_{\max }\left(X_{i}, \Pi_{X_{i}}^{\max }, \mathcal{D}\right) ;$
and of the $N^{2}-N$ score differences

$$
\begin{aligned}
\Delta_{i j} & =S_{\max }-S_{\mathcal{G}^{*}} \\
& =\operatorname{Score}_{\max }\left(X_{i}, \Pi_{X_{i}}^{\max }, \mathcal{D}\right)-\operatorname{Score}_{\mathcal{G}^{*}}\left(X_{i}, \Pi_{X_{i}}^{\mathcal{G}^{*}}, \mathcal{D}\right), i \neq j
\end{aligned}
$$

where $\Pi_{X_{i}}^{\max }$ and $\Pi_{X_{i}}^{\mathcal{G}^{*}}$ are the parents of $X_{i}$ in $\mathcal{G}_{\max }$ and in the $\mathcal{G}^{*}$ obtained by removing (if present) or adding (if not) $X_{j} \rightarrow X_{i}$ to $\mathcal{G}_{\max }$. Only $N$ (for arc additions and deletions) or $2 N$ (for arc reversals) elements of $\Delta$ need to be actually computed in each iteration; those corresponding to the variable(s) whose parent sets were changed by the local move produced the current $\mathcal{G}_{\max }$ in the previous iteration. After that, all possible arc additions, deletions and reversals can be
evaluated without any further computational cost by adding or subtracting the appropriate $\Delta_{i j}$ from the $B_{i}$. Arc reversals can be handled as a combination of arc removals and additions (e.g. reversing $X_{i} \rightarrow X_{j}$ is equivalent to removing $X_{i} \rightarrow X_{j}$ and adding $X_{j} \rightarrow X_{i}$ ). As a result, the overall computational complexity of greedy search reduces from $O\left(c N^{3}\right)$ to $O\left(c N^{2}\right)$. Finally, we briefly note that score equivalence may allow further computational saving because many local moves will produce new $\mathcal{G}^{*}$ that are in the same equivalence class as $\mathcal{G}_{\max }$; and for those moves necessarily $\Delta_{i j}=0$ (for arc reversals) or $\Delta_{i j}=\Delta_{j i}$ (for adding or removing $X_{i} \rightarrow X_{j}$ and $X_{j} \rightarrow X_{i}$ ).

## 3 Revisiting computational complexity

In practice, the computational complexity of estimating a local distribution $\mathrm{P}\left(X_{i} \mid \Pi_{X_{i}}\right)$ from data depends on three of factors:

- the characteristics of the data themselves (the sample size $n$, the number of possible values for categorical variables);
- the number of parents of $X_{i}$ in the DAG, that is, $\left|\Pi_{X_{i}}\right|$;
- the distributional assumptions on $\mathrm{P}\left(X_{i} \mid \Pi_{X_{i}}\right)$, which determine the number of parameters $\left|\Theta_{X_{i}}\right|$.


### 3.1 Computational complexity for local distributions

If $n$ is large, or if $\left|\Theta_{X_{i}}\right|$ is markedly different for different $X_{i}$, different local distributions will take different times to learn, violating the $O(1)$ assumption from the previous section. In other words, if we denote the computational complexity of learning the local distribution of $X_{i}$ as $O\left(f_{\Pi_{X_{i}}}\left(X_{i}\right)\right)$, we find below that $O\left(f_{\Pi_{X_{i}}}\left(X_{i}\right)\right) \neq O(1)$.

### 3.1.1 Nodes in discrete BNs

In the case of discrete BNs, the conditional probabilities $\pi_{i k \mid j}$ associated with each $X_{i} \mid \Pi_{X_{i}}$ are computed from the corresponding counts $n_{i j k}$ tallied from $\left\{X_{i}, \Pi_{X_{i}}\right\}$; hence, estimating them takes $O\left(n\left(1+\left|\Pi_{X_{i}}\right|\right)\right)$ time. Computing the marginals counts for each configuration of $\Pi_{X_{i}}$ then takes $O\left(\left|\Theta_{X_{i}}\right|\right)$ time; assuming that each discrete variable takes at most $l$ values, then $\left|\Theta_{X_{i}}\right| \leqslant l^{1+\left|\Pi_{X_{i}}\right|}$ leading to
$O\left(f_{\Pi_{X_{i}}}\left(X_{i}\right)\right)=O\left(n\left(1+\left|\Pi_{X_{i}}\right|\right)+l^{1+\left|\Pi_{X_{i}}\right|}\right)$.

### 3.1.2 Nodes in GBNs

In the case of GBNs, the regressions coefficients for $X_{i} \mid \Pi_{X_{i}}$ are usually computed by applying a QR decomposition to the augmented data matrix $\left[1 \Pi_{X_{i}}\right]$ :

$[1 \Pi_{X_{i}}]=\mathbf{Q R} \quad$ leading to $\quad \mathbf{R}\left[\mu_{X_{i}}, \boldsymbol{\beta}_{X_{i}}\right]=\mathbf{Q}^{T} X_{i}$
which can be solved efficiently by backward substitution since $\mathbf{R}$ is upper-triangular. This approach is the de facto standard approach for fitting linear regression models because it is numerically stable even in the presence of correlated $\Pi_{X_{i}}$ (see Seber 2008, for details). Afterwards, we can compute the fitted values $\hat{x}_{i}=\Pi_{X_{i}} \hat{\boldsymbol{\beta}}_{X_{i}}$ and the residuals $X_{i}-\hat{x}_{i}$ to estimate $\hat{\sigma}_{X_{i}}^{2} \propto\left(X_{i}-\hat{x}_{i}\right)^{T}\left(X_{i}-\hat{x}_{i}\right)$. The overall computational complexity is

$$
\begin{aligned}
& O\left(f_{\Pi_{X_{i}}}\left(X_{i}\right)\right)= \\
& =\underbrace{O\left(n\left(1+\left|\Pi_{X_{i}}\right|\right)^{2}\right)}_{\text {QR decomposition }}+\underbrace{O\left(n\left(1+\left|\Pi_{X_{i}}\right|\right)\right)}_{\text {computing } \mathbf{Q}^{T} X_{i}} \\
& +\underbrace{O\left(\left(1+\left|\Pi_{X_{i}}\right|\right)^{2}\right)}_{\text {backwards substitution }}+\underbrace{O\left(n\left(1+\left|\Pi_{X_{i}}\right|\right)\right)}_{\text {computing } \hat{x}_{i}} \\
& +\underbrace{O(3 n)}_{\text {computing } \hat{\sigma}_{X_{i}}^{2}}
\end{aligned}
$$

with leading term $O\left((n+1)\left(1+\left|\Pi_{X_{i}}\right|\right)^{2}\right)$.

### 3.1.3 Nodes in CLGBNs

As for CLGBNs, the local distributions of discrete nodes are estimated in the same way as they would be in a discrete BN. For Gaussian nodes, a regression of $X_{i}$ against the continuous parents $\Gamma_{X_{i}}$ is fitted from the $n_{\delta_{X_{i}}}$ observations corresponding to each configuration of the discrete parents $\Delta_{X_{i}}$. Hence, the overall computational complexity is

$$
\begin{aligned}
& O\left(f_{\Pi_{X_{i}}}\left(X_{i}\right)\right) \\
& =\sum_{\delta_{X_{i}} \in \operatorname{Val}\left(\Delta_{X_{i}}\right)} O\left(n_{\delta_{X_{i}}}\left(1+\left|\Gamma_{X_{i}}\right|\right)^{2}\right) \\
& +O\left(2 n_{\delta_{X_{i}}}\left(1+\left|\Gamma_{X_{i}}\right|\right)\right)+O\left(1+\left|\Gamma_{X_{i}}\right|\right)^{2}\right) \\
& +O\left(3 n_{\delta_{X_{i}}}\right) \\
& =O\left(n\left(1+\left|\Gamma_{X_{i}}\right|\right)^{2}\right)+O\left(2 n\left(1+\left|\Gamma_{X_{i}}\right|\right)\right) \\
& +O\left(\left|\operatorname{Val}\left(\Delta_{X_{i}}\right)\right|\left(1+\left|\Gamma_{X_{i}}\right|\right)^{2}\right)+O(3 n) \\
& =O\left(\left(n+l^{\left|\Delta_{X_{i}}\right|}\right)\left(1+\left|\Gamma_{X_{i}}\right|\right)^{2}\right) \\
& +O\left(2 n\left(1+\left|\Gamma_{X_{i}}\right|\right)\right)+O(3 n)
\end{aligned}
$$

with leading term $O\left(\left(n+l^{\left|\Delta_{X_{i}}\right|}\right)\left(1+\left|\Gamma_{X_{i}}\right|\right)^{2}\right)$. If $X_{i}$ has no discrete parents, then (5) simplifies to (4) since $\left|\operatorname{Val}\left(\Delta_{X_{i}}\right)\right|=$ 1 and $n_{\delta_{X_{i}}}=n$.

### 3.2 Computational complexity for the whole BN

Let's now assume without loss of generality that the dependence structure of $\mathbf{X}$ can be represented by a DAG $\mathcal{G}$ with in-degree sequence $d_{X_{1}} \leqslant d_{X_{2}} \leqslant \ldots \leqslant d_{X_{N}}$. For a sparse graph containing $c N$ arcs, this means $\sum_{i=1}^{N} d_{X_{i}}=c N$. Then if we make the common choice of starting greedy search from the empty DAG, we can rewrite (2) as

$$
\begin{aligned}
O(g(N)) & =O\left(c N^{2}\right) \\
& =O\left(\sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} 1\right) \\
& =\sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} O(1)=O(g(N, \mathbf{d}))
\end{aligned}
$$

because:

- parents are added sequentially to each of the $N$ nodes;
- if a node $X_{i}$ has $d_{X_{i}}$ parents then greedy search will perform $d_{X_{i}}+1$ passes over the candidate parents;
- for each pass, $N-1$ local distributions will need to be relearned as described in Sect. 2.

The candidate parents in the $\left(d_{X_{i}}+1\right)$ th pass are evaluated but not included in $\mathcal{G}$, since no further parents are accepted for a node after its parent set $\Pi_{X_{i}}$ is complete. If we drop the assumption from Sect. 2 that each term in the expression above is $O(1)$, and we substitute it with the computational complexity expressions we derived above in this section, then we can write
$O(g(N, \mathbf{d}))=\sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} O\left(f_{j k}\left(X_{i}\right)\right)$.
where $O\left(f_{j k}\left(X_{i}\right)\right)=O\left(f_{\Pi_{X_{i}}^{(j-1)} \cup X_{k}}\left(X_{i}\right)\right)$, the computational complexity of learning the local distribution of $X_{i}$ conditional of $j-1$ parents $\Pi_{X_{i}}^{(j)}$ currently in $\mathcal{G}$ and a new candidate parent $X_{k}$.

### 3.2.1 Discrete BNs

For discrete BNs, $f_{j k}\left(X_{i}\right)$ takes the form shown in (3) and

$$
\begin{aligned}
& O(g(N, \mathbf{d})) \\
& \quad=\sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} O\left(n(1+j)+l^{1+j}\right)
\end{aligned}
$$

$$
\begin{aligned}
= & O\left(n(c+1)(N-1) N+n(N-1) \sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} j\right. \\
& \left.+(N-1) \sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} l^{1+j}\right) \\
\approx & O\left(n c N^{2}+n N \sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} j+N \sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} l^{1+j}\right)
\end{aligned}
$$

The second term is an arithmetic progression,
$\sum_{j=1}^{d_{X_{i}}+1} j=\frac{\left(d_{X_{i}}+1\right)\left(d_{X_{i}}+2\right)}{2}$
and the third term is a geometric progression
$\sum_{j=1}^{d_{X_{i}}+1} l^{1+j}=l^{2} \sum_{j=1}^{d_{X_{i}}+1} l^{j-1}=l^{2} \frac{l^{d_{X_{i}}+1}-1}{l-1}$
leading to

$$
\begin{aligned}
& O(g(N, \mathbf{d})) \\
& \quad \approx O\left(n c N^{2}+n N \sum_{i=1}^{N} \frac{d_{X_{i}}^{2}}{2}+N l^{2} \sum_{i=1}^{N} \frac{l^{d_{X_{i}}+1}-1}{l-1}\right)
\end{aligned}
$$

Hence, we can see that $O(g(N, \mathbf{d}))$ increases linearly in the sample size. If $\mathcal{G}$ is uniformly sparse, all $d_{X_{i}}$ are bounded by a constant $b\left(d_{X_{i}} \leqslant b, c \leqslant b\right)$ and
$O(g(N, \mathbf{d})) \approx O\left(N^{2}\left[n c+n \frac{b^{2}}{2}+l^{2} \frac{l^{b+1}-1}{l-1}\right]\right)$,
so the computational complexity is quadratic in $N$. Note that this is a stronger sparsity assumption than $\sum_{i=1}^{N} d_{X_{i}}=c N$, because it bounds individual $d_{X_{i}}$ instead of their sum; and it is commonly used to make challenging learning problems feasible (e.g. Cooper and Herskovits 1992; Friedman and Koller 2003). If, on the other hand, $G$ is dense and $d_{X_{i}}=$ $O(N)$, then $c=O(N)$
$O(g(N, \mathbf{d})) \approx O\left(N^{2}\left[n c+n \frac{N^{3}}{2}+l^{2} \frac{l^{N}-1}{l-1}\right]\right)$
and $O(g(N, \mathbf{d}))$ is more than exponential in $N$. In between these two extremes, the distribution of the $d_{X_{i}}$ determines the actual computational complexity of greedy search for a specific types of structures. For instance, if $\mathcal{G}$ is a scalefree DAG (Bollobás et al. 2003) the in-degree of most nodes will be small and we can expect a computational complexity
closer to quadratic than exponential if the probability of large in-degrees decays quickly enough compared to $N$.

### 3.2.2 GBNs

If we consider the leading term of (4), we obtain the following expression:

$$
\begin{aligned}
& O(g(N, \mathbf{d})) \\
& \quad=\sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} O\left((n+1)(j+1)^{2}\right) \\
& \quad=O\left((n+1)(N-1) \sum_{i=1}^{N} \sum_{j=1}^{d_{X_{i}}+1}(j+1)^{2}\right)
\end{aligned}
$$

Noting the arithmetic progression

$$
\sum_{j=1}^{d_{X_{i}}+1}(j+1)^{2}=\frac{2 d_{X_{i}}^{3}+15 d_{X_{i}}^{2}+37 d_{X_{i}}+24}{6}
$$

we can write
$O(g(N, \mathbf{d})) \approx O\left(n N \sum_{i=1}^{N} \frac{d_{X_{i}}^{3}}{3}\right)$,
which is again linear in $n$ but cubic in the $d_{X_{i}}$. We note, however, that even for dense networks $\left(d_{X_{i}}=O(N)\right)$ computational complexity remains polynomial
$O(g(N, \mathbf{d})) \approx O\left(n N^{2} \frac{N^{3}}{3}\right)$
which was not the case for discrete BNs. If, on the other hand $d_{X_{i}} \leqslant b$,
$O(g(N, \mathbf{d})) \approx O\left(n N^{2} \frac{b^{3}}{3}\right)$
which is quadratic in $N$.

### 3.2.3 CLGBNs

Deriving the computational complexity for CLGBNs is more complicated because of the heterogeneous nature of the nodes. If we consider the leading term of (5) for a BN with $M<N$ Gaussian nodes and $N-M$ multinomial nodes, we have

$$
\begin{aligned}
O(g(N, \mathbf{d}))= & \sum_{i=1}^{N-M} \sum_{j=1}^{d_{X_{i}}+1} \sum_{k=1}^{N-M-1} O\left(f_{j k}\left(X_{i}\right)\right) \\
& +\sum_{i=1}^{M} \sum_{j=1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} O\left(f_{j k}\left(X_{i}\right)\right)
\end{aligned}
$$

The first term can be computed using (7) since discrete nodes can only have discrete parents, and thus cluster in a subgraph of $N-M$ nodes whose in-degrees are completely determined by other discrete nodes; and the same considerations we made in Sect. 3.2.1 apply.

As for the second term, we will first assume that all $D_{i}$ discrete parents of each node are added first, before any of the $G_{i}$ continuous parents $\left(d_{X_{i}}=D_{i}+G_{i}\right)$. Hence, we write

$$
\begin{aligned}
& \sum_{i=1}^{M} \sum_{j=1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} O\left(f_{j k}\left(X_{i}\right)\right) \\
& =\sum_{i=1}^{M}\left[\sum_{j=1}^{D_{i}} \sum_{k=1}^{N-1} O\left(f_{j k}\left(X_{i}\right)\right)+\sum_{j=D_{i}+1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} O\left(f_{j k}\left(X_{i}\right)\right)\right]
\end{aligned}
$$

We further separate discrete and continuous nodes in the summations over the possible $N-1$ candidates for inclusion or removal from the current parent set, so that substituting (5) we obtain

$$
\begin{aligned}
& \sum_{j=1}^{D_{i}} \sum_{k=1}^{N-1} O\left(f_{j k}\left(X_{i}\right)\right) \\
& \quad=\sum_{j=1}^{D_{i}}\left[\sum_{k=1}^{N-M} O\left(f_{j k}\left(X_{i}\right)\right)+\sum_{k=1}^{M-1} O\left(f_{j k}\left(X_{i}\right)\right)\right] \\
& \quad=\sum_{j=1}^{D_{i}}\left[(N-M) O\left(n+l^{j}\right)+(M-1) O\left(4\left(n+l^{j}\right)\right)\right] \\
& \quad \approx O\left((N+3 M) \sum_{j=1}^{D_{i}}\left(n+l^{j}\right)\right) \\
& \quad=O\left((N+3 M)\left(n D_{i}+l \frac{l^{D_{i}}-1}{l-1}\right)\right) \\
& \sum_{j=D_{i}+1}^{d_{X_{i}}+1} \sum_{k=1}^{N-1} O\left(f_{j k}\left(X_{i}\right)\right) \\
& \quad=\sum_{j=D_{i}+1}^{d_{X_{i}}+1}\left[\sum_{k=1}^{N-M} O\left(f_{j k}\left(X_{i}\right)\right)+\sum_{k=1}^{M-1} O\left(f_{j k}\left(X_{i}\right)\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{j=1}^{G_{i}}\left[(N-M) O\left(n+l^{D_{i}}\right)\right. \\
& \left.\quad+(M-1) O\left(\left(n+l^{D_{i}}\right)(1+j)^{2}\right)\right] \\
& \approx O\left(\left(n+l^{D_{i}}\right)\left(G_{i}(N-M)+M \frac{G_{i}^{3}}{3}\right)\right)
\end{aligned}
$$

Finally, combining all terms we obtain the following expression:

$$
\begin{aligned}
& O(g(N, \mathbf{d})) \\
& \approx O\left(n c(N-M)^{2}+n(N-M) \sum_{i=1}^{N-M} \frac{d_{\mathrm{X}_{i}}^{2}}{2}\right. \\
&+(N-M) l^{2} \sum_{i=1}^{N-M} \frac{l^{d_{X_{i}}+1}-1}{l-1} \\
&+\sum_{i=1}^{M} O\left((N+3 M)\left(n D_{i}+l \frac{l^{D_{i}}-1}{l-1}\right)\right) \\
&+\sum_{i=1}^{M} O\left(\left(n+l^{D_{i}}\right)\left(G_{i}(N-M)+M \frac{G_{i}^{3}}{3}\right)\right)
\end{aligned}
$$

While it is not possible to concisely describe the behaviour resulting from this expression given the number of datadependent parameters $\left(D_{i}, G_{i}, M\right)$, we can observe that:

- $O(g(N, \mathbf{d}))$ is always linear in the sample size;
- unless the number of discrete parents is bounded for both discrete and continuous nodes, $O(g(N, \mathbf{d}))$ is again more than exponential;
- if the proportion of discrete nodes is small, we can assume that $M \approx N$ and $O(g(N, \mathbf{d}))$ is always polynomial.


## 4 Greedy search and big data

In Sect. 3, we have shown that the computational complexity of greedy search scales linearly in $n$, so greedy search is efficient in the sample size and it is suitable for learning BNs from big data. However, we have also shown that different distributional assumptions on $\mathbf{X}$ and on the $d_{X_{i}}$ lead to different complexity estimates for various types of BNs. We will now build on these results to suggest two possible improvements to speed up greedy search.

### 4.1 Speeding up low-order regressions in GBNs and CLGBNs

Firstly, we suggest that estimating local distributions with few parents can be made more efficient; if we assume that $\mathcal{G}$

is sparse, those make up the majority of the local distributions learned by greedy search and their estimation can potentially dominate the overall computational cost of Algorithm 1. As we can see from the summations in (6), the overall number of learned local distributions with $j$ parents is

$$
\sum_{i=1}^{N} \mathbb{1}_{\left\{d_{X_{i}} \geqslant j-1\right\}}(j)=N-\sum_{i=1}^{N} \mathbb{1}_{\left\{d_{X_{i}}<j-1\right\}}(j)
$$

that is, it is inversely proportional to the number of nodes for which $d_{X_{i}}$ is less than $j-1$ in the DAG we are learning. If that subset of nodes represents large fraction of the total, as is the case for scale-free networks and for networks in which all $d_{X_{i}} \leqslant b$, (8) suggests that a correspondingly large fraction of the local distributions we will estimate in Algorithm 1 will have a small number $j$ of parents. Furthermore, we find that in our experience BNs will typically have a weakly connected DAG (that is, with no isolated nodes); and in this case local distributions with $j=0,1$ will need to be learned for all nodes, and those with $j=2$ for all non-root nodes.

In the case of GBNs, local distributions for $j=0,1,2$ parents can be estimated in closed form using simple expressions as follows:
$-j=0$ corresponds to trivial linear regressions of the type

$$
X_{i}=\mu_{X_{i}}+\varepsilon_{X_{i}}
$$

in which the only parameters are the mean and the variance of $X_{i}$.
$-j=1$ corresponds to simple linear regressions of the type
$X_{i}=\mu_{X_{i}}+X_{j} \beta_{X_{j}}+\varepsilon_{X_{i}}$,
for which there are the well-known (e.g. Draper and Smith 1998) closed-form estimates

$$
\begin{aligned}
& \hat{\mu}_{X_{i}}=\hat{x}_{i}-\hat{\beta}_{X_{j}} \hat{x}_{j} \\
& \hat{\beta}_{X_{j}}=\frac{\operatorname{COV}\left(X_{i}, X_{j}\right)}{\operatorname{VAR}\left(X_{i}\right)} \\
& \hat{\sigma}_{X_{i}}^{2}=\frac{1}{n-2}\left(X_{i}-\hat{x}_{i}\right)^{T}\left(X_{i}-\hat{x}_{i}\right)
\end{aligned}
$$

where $\operatorname{VAR}(\cdot)$ and $\operatorname{COV}(\cdot, \cdot)$ are empirical variances and covariances.

- for $j=2$, we can estimate the parameters of

$$
X_{i}=\mu_{X_{i}}+X_{j} \beta_{X_{j}}+X_{k} \beta_{X_{k}}+\varepsilon_{X_{i}}
$$

using their links to partial correlations:

$$
\begin{aligned}
& \rho_{X_{i} X_{j} \mid X_{k}}=\frac{\rho_{X_{i} X_{j}}-\rho_{X_{i} X_{k}} \rho_{X_{j} X_{k}}}{\sqrt{1-\rho_{X_{i} X_{k}}^{2} \sqrt{1-\rho_{X_{j} X_{k}}^{2}}}} \\
& =\beta_{j} \frac{\sqrt{1-\rho_{X_{j} X_{k}}^{2}}}{\sqrt{1-\rho_{X_{i} X_{k}}^{2}}} \\
& \rho_{X_{i} X_{k} \mid X_{j}}=\beta_{k} \frac{\sqrt{1-\rho_{X_{j} X_{k}}^{2}}}{\sqrt{1-\rho_{X_{i} X_{j}}^{2}}} ;
\end{aligned}
$$

for further details we refer the reader to Weatherburn (1961). Simplifying these expressions leads to

$$
\begin{aligned}
& \hat{\beta}_{X_{j}}=\frac{1}{d}\left[\operatorname{VAR}\left(X_{k}\right) \operatorname{COV}\left(X_{i}, X_{j}\right)\right. \\
& \left.-\operatorname{COV}\left(X_{j}, X_{k}\right) \operatorname{COV}\left(X_{i}, X_{k}\right)\right] \\
& \hat{\beta}_{X_{k}}=\frac{1}{d}\left[\operatorname{VAR}\left(X_{j}\right) \operatorname{COV}\left(X_{i}, X_{k}\right)\right. \\
& \left.-\operatorname{COV}\left(X_{j}, X_{k}\right) \operatorname{COV}\left(X_{i}, X_{j}\right)\right]
\end{aligned}
$$

with denominator
$d=\operatorname{VAR}\left(X_{j}\right) \operatorname{VAR}\left(X_{k}\right)-\operatorname{COV}\left(X_{j}, X_{k}\right)$.
Then, the intercept and the standard error estimates can be computed as

$$
\begin{aligned}
& \hat{\mu}_{X_{i}}=\hat{x}_{i}-\hat{\beta}_{X_{j}} \hat{x}_{j}-\hat{\beta}_{X_{k}} \hat{x}_{k} \\
& \hat{\sigma}_{X_{i}}^{2}=\frac{1}{n-3}\left(X_{i}-\hat{x}_{i}\right)^{T}\left(X_{i}-\hat{x}_{i}\right)
\end{aligned}
$$

All these expressions are based on the variances and the covariances of $\left(X_{i}, \Pi_{X_{i}}\right)$, and therefore can be computed in

$$
\begin{aligned}
& \underbrace{O\left(\frac{1}{2} n(1+j)^{2}\right)}_{\text {covariance matrix of }\left(X_{i}, \Pi_{X_{i}}\right)} \\
& +\underbrace{O(n(1+j))}_{\text {computing } \hat{x}_{i}}+\underbrace{O(3 n)}_{\text {computing } \hat{\sigma}_{X_{i}}^{2}}
\end{aligned}
$$

This is faster than (4) for the same number of parents, albeit in the same class of computational complexity


and it suggests that learning low-order local distributions in this way can be markedly faster, thus driving down the overall computational complexity of greedy search without any change in its behaviour. We also find that issues with singularities and numeric stability, which are one of the reasons to use the QR decomposition to estimate the regression coefficients, are easy to diagnose using the variances and the covariances of $\left(X_{i}, \Pi_{X_{i}}\right)$; and they can be resolved without increasing computational complexity again.

As for CLGBNs, similar improvements in speed are possible for continuous nodes. Firstly, if a continuous $X_{i}$ has no discrete parents $\left(\Delta_{X_{i}}=\varnothing\right)$ then the computational complexity of learning its local distribution using QR is again given by (4) as we noted in Sect. 3.1.3; and we are in the same setting we just described for GBNs. Secondly, if $X_{i}$ has discrete parents $\left(D_{X_{i}}>0\right)$ and $j$ continuous parents $\left(G_{X_{i}}=j\right)$, the closed-form expressions above can be computed for all the configurations of the discrete parents in

$$
\begin{aligned}
& \sum_{\delta_{X_{i}} \in \operatorname{Val}\left(D_{X_{i}}\right)} O\left(\frac{1}{2} n_{\delta_{X_{i}}}(1+j)^{2}\right) \\
& \quad+O\left(n_{\delta_{X_{i}}}(1+j)\right)+O\left(3 n_{\delta_{X_{i}}}\right) \\
& =O\left(\frac{1}{2} n(1+j)^{2}\right)+O(n(1+j))+O(3 n)
\end{aligned}
$$

time, which is faster than the estimator from (5):


Interestingly we note that (10) does not depend on $D_{X_{i}}$, unlike (5); the computational complexity of learning local distributions with $G_{X_{i}} \leqslant 2$ does not become exponential even if the number of discrete parents is not bounded.

### 4.2 Predicting is faster than learning

BNs are often implicitly formulated in a prequential setting (Dawid 1984), in which a data set $\mathcal{D}$ is considered as a snapshot of a continuous stream of observations and BNs are learned from that sample with a focus on predicting future observations. Chickering and Heckerman (2000) called this the "engineering criterion" and set
$\operatorname{Score}(\mathcal{G}, \mathcal{D})=\log \mathrm{P}\left(\mathbf{X}^{(n+1)} \mid \mathcal{G}, \Theta, \mathcal{D}\right)$
as the score function to select the optimal $\mathcal{G}_{\max }$, effectively maximising the negative cross-entropy between the "correct" posterior distribution of $\mathbf{X}^{(n+1)}$ and that determined by the BN with DAG $\mathcal{G}$. They showed that this score is consistent and that even for finite sample sizes it produces BNs which are at least as good as the BNs learned using the scores in Sect. 1, which focus on fitting $\mathcal{D}$ well. Allen and Greiner (2000) and later Peña et al. (2005) confirmed this fact by embedding $k$-fold cross-validation into greedy search, and obtaining both better accuracy both in prediction and network reconstruction. In both papers, the use of cross-validation was motivated by the need to make the best use of relatively small samples, for which the computational complexity was not a crucial issue.

However, in a big data setting it is both faster and accurate to estimate (11) directly by splitting the data into a training and test set and computing
$\operatorname{Score}(\mathcal{G}, \mathcal{D})=\log \mathrm{P}\left(\mathcal{D}^{\text {test }} \mid \mathcal{G}, \Theta, \mathcal{D}^{\text {train }}\right) ;$
that is, we learn the local distributions on $\mathcal{D}^{\text {train }}$ and we estimate the probability of $\mathcal{D}^{\text {test }}$. As is the case for many other models (e.g., deep neural networks; Goodfellow et al. 2016), we note that prediction is computationally much cheaper than learning because it does not involve solving an optimisation problem. In the case of BNs, computing (12) is:

- $O\left(N \mid \mathcal{D}^{\text {test }} \mid\right)$ for discrete BNs, because we just have to perform an $O(1)$ look-up to collect the relevant conditional probability for each node and observation;
- $O\left(c N \mid \mathcal{D}^{\text {test }} \mid\right)$ for GBNs and CLGBNs, because for each node and observation we need to compute $\Pi_{X_{i}}^{(n+1)} \hat{\beta}_{X_{i}}$ and $\hat{\beta}_{X_{i}}$ is a vector of length $d_{X_{i}}$.

In contrast, using the same number of observations for learning in GBNs and CLGBNs involves a QR decomposition to estimate the regression coefficients of each node in both (4) and (5); and that takes longer than linear time in $N$.

Hence by learning local distributions only on $\mathcal{D}^{\text {train }}$ we improve the speed of structure learning because the perobservation cost of prediction is lower than that of learning; and $\mathcal{D}^{\text {train }}$ will still be large enough to obtain good estimates of their parameters $\Theta_{X_{i}}$. Clearly, the magnitude of the speedup will be determined by the proportion of $\mathcal{D}$ used as $\mathcal{D}^{\text {test }}$. Further improvements are possible by using the closed-form results from Sect. 4.1 to reduce the complexity of learning local distributions on $\mathcal{D}^{\text {train }}$, combining the effect of all the optimisations proposed in this section.

## 5 Benchmarking and simulations

We demonstrate the improvements in the speed of structure learning and we discussed in Sects. 4.1 and 4.2 using the MEHRA data set from Vitolo et al. (2018), which studied 50 million observations to explore the interplay between environmental factors, exposure levels to outdoor air pollutants, and health outcomes in the English regions of the UK between 1981 and 2014. The CLGBN learned in that paper is shown in Fig. 1: It comprises 24 variables describing the concentrations of various air pollutants ( $\mathrm{O} 3, \mathrm{PM}_{2.5}, \mathrm{PM}_{10}, \mathrm{SO}_{2}$, $\mathrm{NO}_{2}, \mathrm{CO}$ ) measured in 162 monitoring stations, their geographical characteristics (latitude, longitude, latitude, region and zone type), weather (wind speed and direction, temperature, rainfall, solar radiation, boundary layer height), demography and mortality rates.

The original analysis was performed with the bnlearn R package (Scutari 2010), and it was complicated by the fact that many of the variables describing the pollutants had significant amounts of missing data due to the lack of cov-
erage in particular regions and years. Therefore, Vitolo et al. (2018) learned the BN using the Structural EM algorithm (Friedman 1997), which is an application of the expectationmaximisation algorithm (EM; Dempster et al. 1977) to BN structure learning that uses hill climbing to implement the M step.

For the purpose of this paper, and to better illustrate the performance improvements arising from the optimisations from Sect. 4, we will generate large samples from the CLGBN learned by Vitolo et al. (2018) to be able to control sample size and to work with plain hill climbing on complete data. In particular:

1. we consider sample sizes of $1,2,5,10,20$ and 50 millions;
2. for each sample size, we generate 5 data sets from the CLGBN;
3. for each sample, we learn back the structure of the BN using hill climbing using various optimisations:
![img-0.jpeg](img-0.jpeg)

Fig. 1 Conditional Linear Gaussian BN from Vitolo et al. (2018). Yellow nodes are multinomial, blue nodes are Gaussian, and green nodes are conditional linear Gaussian

- QR: estimating all Gaussian and conditional linear Gaussian local distributions using the QR decomposition, and BIC as the score function;
- 1P: using the closed-form estimates for the local distributions that involve 0 or 1 parents, and BIC as the score function;
- 2P: using the closed-form estimates for the local distributions that involve 0,1 or 2 parents, and BIC as the score functions;
- PRED: using the closed-form estimates for the local distributions that involve 0,1 or 2 parents for learning the local distributions on $75 \%$ of the data and estimating (12) on the remaining $25 \%$.

For each sample and optimisation, we run hill climbing 5 times and we average the resulting running times to reduce the variability of each estimate. Furthermore, we measure the accuracy of network reconstruction using the Structural Hamming Distance (SHD; 2006), which measures the number of arcs that differ between the CPDAG representations of the equivalence classes of two network structures. In our case, those we learn from the simulated data and the original network structure from Vitolo et al. (2018). All computations are performed with the bnlearn package in R 3.3.3 on a machine with two Intel Xeon CPU E5-2690 processors (16 cores) and 384GB of RAM.

The running times for 1P, 2P and PRED, normalised using those for QR as a baseline, are shown in Fig. 2. As expected,
![img-1.jpeg](img-1.jpeg)

Fig. 2 Running times for the MEHRA data set, normalised using the baseline implementation based on the QR decomposition (blue), for 1P (pink), 2P (green) and PRED (red). Bars represent $95 \%$ confidence intervals. Average running times are reported for QR. (Color figure online)

Table 1 Sums of the SHDs between the network structures learned by BIC, PRED and that from Vitolo et al. (2018) for different sample sizes $n$


running times decrease with the level of optimisation: 1P (pink) is $\approx 20 \%$ faster than QR, 2P (green) is $\approx 25 \%$ faster and PRED (red) is $\approx 60 \%$ faster, with minor variations at different sample sizes. PRED exhibits a larger variability because of the randomness introduced by the subsampling of $\mathcal{D}^{\text {rest }}$ and provides smaller speed-ups for the smallest considered sample size ( 1 million). Furthermore, we confirm the results from Chickering and Heckerman (2000) on network reconstruction accuracy. In Table 1, we report the sums of the SHDs between the network structures learned by BIC and that from Vitolo et al. (2018), and the corresponding sum for the networks learned using PRED, for the considered sample sizes. Overall, we find that BIC results in 13 errors over the 30 learned DAGs, compared to 4 for (12). The difference is quite marked for samples of size 1 million ( 11 errors versus 2 errors). On the other hand, neither score results in any error for samples with more than 10 million observations, thus confirming the consistency of PRED. Finally we confirm that the observed running times increase linearly in the sample size as we show in Sect. 3.

In order to verify that these speed increases extend beyond the MEHRA data set, we considered five other data sets from the UCI Machine Learning Repository (Dheeru and Karra Taniskidou 2017) and from the repository of the Data Exposition Session of the Joint Statistical Meetings (JSM). These particular data sets have been chosen because of their large sample sizes and because they have similar characteristics to MEHRA (continuous variables, a few discrete variables, 20-40 nodes overall; see Table 2 for details). However, since their underlying "true DAGs" are unknown, we cannot comment on the accuracy of the DAGs we learn from them. For the same reason, we limit the density of the learned DAGs by restricting each node to have at most 5 parents; this produces DAGs with $2.5 N$ to $3.5 N$ arcs depending on the data set. The times for 1P, 2P and PRED, again normalised by those for QR, are shown in Fig. 3. Overall, we confirm that PRED is $\approx 60 \%$ faster on average than QR. Compared to MEHRA, 1 P and 2 P are to some extent slower with average speedups of only $\approx 15 \%$ and $\approx 22 \%$, respectively. However, it is apparent by comparing Figs. 2 and 3 that the reductions in running times are consistent over all the data sets considered

Table 2 Data sets from the UCI Machine Learning Repository and the JSM Data Exposition session, with their sample size ( $n$ ), multinomial nodes $(N-M)$ and Gaussian/conditional Gaussian nodes $(M)$


![img-2.jpeg](img-2.jpeg)

Fig. 3 Running times for the data sets in Table 2, normalised using the baseline implementation based on the QR decomposition (blue), for 1 P (pink), 2 P (green) and PRED (red). Bars represent $95 \%$ confidence intervals. Average running times are reported for QR
in this paper and hold for a wide range of sample sizes and combinations of discrete and continuous variables.

## 6 Conclusions

Learning the structure of BNs from large data sets is a computationally challenging problem. After deriving the computational complexity of the greedy search algorithm in closed form for discrete, Gaussian and conditional linear Gaussian BNs, we studied the implications of the resulting expressions in a "big data" setting where the sample size is very large, and much larger than the number of nodes in the BN. We found that, contrary to classic characterisations, computational complexity strongly depends on the class of BN being learned in addition to the sparsity of the underlying DAG. Starting from this result, we suggested two for greedy search with the aim to speed up the most common algorithm used for BN structure learning. Using a large environmental
data set and five data sets from the UCI Machine Learning Repository and the JSM Data Exposition, we show that it is possible to reduce the running time greedy search by $\approx 60 \%$.

Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.
