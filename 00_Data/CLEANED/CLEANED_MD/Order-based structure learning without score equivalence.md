# Order-based Structure Learning without Score Equivalence 

Hyunwoong Chang ${ }^{1}$, James Cai ${ }^{2}$ and Quan Zhou ${ }^{1, *}$<br>${ }^{1}$ Department of Statistics, Texas A\&M University<br>${ }^{2}$ Department of Veterinary Integrative Bioscience, Texas A\&M University


#### Abstract

We propose an empirical Bayes formulation of the structure learning problem, where the prior specification assumes that all node variables have the same error variance, an assumption known to ensure the identifiability of the underlying causal directed acyclic graph (DAG). To facilitate efficient posterior computation, we approximate the posterior probability of each ordering by that of a best DAG model, which naturally leads to an order-based Markov chain Monte Carlo (MCMC) algorithm. Strong selection consistency for our model in high-dimensional settings is proved under a condition that allows heterogeneous error variances, and the mixing behavior of our sampler is theoretically investigated. Further, we propose a new iterative top-down algorithm, which quickly yields an approximate solution to the structure learning problem and can be used to initialize the MCMC sampler. We demonstrate that our method outperforms other state-of-the-art algorithms under various simulation settings, and conclude the paper with a single-cell real-data study illustrating practical advantages of the proposed method.


Keywords: Directed acyclic graphs; Empirical Bayes methods; Strong selection consistency; Markov chain Monte Carlo methods; Non-decomposable scores.

## 1 Introduction

We consider Bayesian structure learning of a directed acyclic graph (DAG) model from observational data. Bayesian algorithms for structure learning are often classified as scorebased in the literature, since they assign a posterior probability to each candidate DAG, the logarithm of which can be interpreted as a score [Drton and Maathuis, 2017]. A Markov equivalence class is a set of all DAGs that encode the same set of conditional independence relations among node variables. Without a priori knowledge, we cannot distinguish between two Markov equivalent DAGs using only observational data [Koller and Friedman, 2009]. If a Bayesian model yields the same score for DAGs in the same equivalence class, we say it is score equivalent, which is widely considered a desirable property [Andersson et al., 1997]. Most Bayesian structure learning methods used in practice are score equivalent [Geiger and Heckerman, 2002].

[^0]
[^0]:    *Corresponding author: quan@stat.tamu.edu

Since the number of $p$-node DAGs grows super-exponentially with $p$, an exact evaluation of the posterior distribution is impossible unless $p$ is extremely small, and Markov chain Monte Carlo (MCMC) methods are commonly employed to generate samples from the posterior distribution. As a classical example, structure MCMC, which was proposed in the seminal work of Madigan et al. [1995], is a random walk Metropolis-Hastings algorithm on the DAG space that uses single-edge addition, deletion, and reversal as proposal moves. However, it is known that this algorithm can often suffer from computational inefficiency due to the considerable time it spends sampling DAGs within the same equivalence class [Andersson et al., 1997, Chickering, 2002]. Even if the data is very informative on the conditional independence relations among all variables, we are only able to learn the equivalence class of the underlying true DAG model, which can easily be very large and takes the chain a long time to explore. In order to overcome slow mixing behavior caused by equivalence classes, many DAG MCMC samplers have been proposed, which typically introduce new DAG operations that can realize jumps between very different DAGs, enabling the chain to move more efficiently across equivalence classes [Grzegorczyk and Husmeier, 2008, Su and Borsuk, 2016]. Another strategy is to devise MCMC samplers on some other spaces that might be easier to explore than the DAG space. Indeed, one can directly search on the equivalence class space so that redundant moves between Markov equivalent DAGs are avoided [Castelletti et al., 2018, Zhou and Chang, 2021]. But this approach is not commonly used in the Bayesian literature, and one likely reason is that, unlike DAG MCMC samplers, the implementation of graph operations for equivalence classes can be highly complicated.

A more popular approach is to perform MCMC sampling on the order space [Friedman and Koller, 2003, Agrawal et al., 2018, Kuipers et al., 2022]. Due to the acyclicity constraint, every $p$-node DAG has at least one consistent ordering of the $p$ nodes such that node $i$ precedes node $j$ whenever the edge $i \rightarrow j$ is in the DAG. Order-based MCMC methods are largely motivated by the following observation: the main computational challenge in structure learning lies in the uncertainty of order estimation, since once the ordering of variables is fixed, structure learning can be reduced to a collection of variable selection problems that are often considered to have a much smaller complexity. It is generally believed that the mixing of order MCMC is better than that of structure MCMC, because the search space is smaller and the posterior distribution on the order space tends to be smoother [Friedman and Koller, 2003]. However, the problem of traversing large equivalence classes still exists. To see this, assume again that all conditional independence relations can be learned from the data so that the posterior concentrates on one equivalence class. But any two DAGs in this equivalence class must have different orderings since at least one edge is flipped. This implies that the posterior distribution on the order space concentrates on a set at least as large as this equivalence class.

To mitigate the potential mixing problem caused by traversing large equivalence classes, we propose to impose identifiability conditions so that within each equivalence class, the posterior mass tends to concentrate on only one DAG. Consequently, the overall posterior distribution tends to have less and sharper modes. To this end, we follow the work of Peters and Bühlmann [2014] to consider Gaussian structural equation models with equal error variances. Intuitively, by assuming equal error variances, the data becomes informative on edge directions so that an MCMC sampler can quickly learn the best DAG in its equiva-

lence class. For example, consider two correlated variables $\mathrm{X}_{1}, \mathrm{X}_{2}$. The DAGs $\mathrm{X}_{1} \rightarrow \mathrm{X}_{2}$ and $\mathrm{X}_{2} \rightarrow \mathrm{X}_{1}$ are Markov equivalent, and in general, we cannot determine the causal direction if only observational data is available. But the equal variance assumption forces the posterior score to favor $\mathrm{X}_{1} \rightarrow \mathrm{X}_{2}$ if $\mathrm{X}_{2}$ has a larger marginal variance than $\mathrm{X}_{1}$. Though a score equivalent Bayesian procedure allows us to make posterior inferences by averaging over Markov equivalent DAGs, this advantage is often merely theoretical due to its slow convergence, even when dealing with a moderately large number of node variables. Our simulation study and real data analysis will show that the use of equal variance assumption does provide practical advantages, and it improves the posterior inference accuracy unless there is a huge degree of heterogeneity among error variances.

There is a rapidly growing literature on the identifiability conditions for structure learning [Shimizu et al., 2006, Hoyer et al., 2008, Peters et al., 2011, Peters and Bühlmann, 2014, Strieder et al., 2021, Drton and Maathuis, 2017, Glymour et al., 2019]. In particular, two deterministic search algorithms have been proposed recently for structure learning with equal error variances [Ghoshal and Honorio, 2018, Chen et al., 2019], and they are shown to be advantageous in terms of computational cost and scale well to high-dimensional data. But to our knowledge, the corresponding Bayesian theory and methodology is largely underdeveloped. Aiming to fill this gap, we formulate an empirical Bayes model under the equal variance assumption and obtain a posterior score that distinguishes between Markov equivalent DAGs. We prove a strong selection consistency result for our model, which shows that the posterior probability of the true DAG tends to one in probability under mild highdimensional conditions. In particular, while our prior distribution encodes the equal variance constraint, the consistency result holds under a weaker assumption known as the minimumtrace condition [Aragam et al., 2019]. Further, we extend the consistency result to cases where errors follow sub-Gaussian distributions, which include more interesting settings such as mixed discrete-Gaussian DAG models.

The posterior score derived from our model is non-decomposable (see Remark 2), which is expected since, under the equal variance assumption, the marginal likelihood of a DAG model should depend on how close the residual variances of the $p$ nodes are to each other. This poses new computational challenges and again makes our method very different from the existing Bayesian literature, where decomposable scores are almost always used because the decomposability enables one to evaluate the posterior probability of a DAG by local calculations at each node [Chickering, 2002].

To numerically evaluate the posterior distribution of our empirical Bayes model, in the same spirit of the minimal I-MAP MCMC of Agrawal et al. [2018], we approximate the posterior probability of an ordering by that of the best consistent DAG and then build a sampling algorithm on the order space. We show that, under some conditions on the edge weights, the chain will never get stuck at a sub-optimal local mode for exponentially many iterations in expectation, which partially explains why this order MCMC scheme may perform well in practice. Further, we propose a generalized iterative version of the top-down algorithm of Chen et al. [2019]. This algorithm is deterministic and quickly finds a likely ordering of the variables, which can be used as a warm start for our order MCMC sampler. When estimating edge inclusion probabilities, we tune our estimators via a conditional expectation calculation so that we can reduce the estimation variance caused by picking one single best

DAG for each ordering. Lastly, though the non-decomposable score of our model cannot be evaluated locally, we are able to devise an implementation strategy that makes the posterior evaluation for our model as efficient as that with a decomposable score. The key idea is to store the search paths of the forward-backward stepwise selection at each node, which can be reused in finding the best DAG consistent with a given ordering.

# 2 An empirical Bayes model for order-based structure learning 

### 2.1 Notation and terminology

We set up the notation and terminology to be used throughout the paper. Let $G=(V, E)$ denote a DAG, where $V$ is a node set and $E \subset V \times V$ is a set of directed edges that form no cycle. Without loss of generality, for a $p$-node DAG, we assume $V=[p]=\{1, \ldots, p\}$. For ease of notation, we write $\{i \rightarrow j\} \in G$ to mean that $(i, j) \in E$, and use $G \cup\{i \rightarrow j\}$ (respectively $G \backslash\{i \rightarrow j\}$ ) to denote the DAG obtained by adding (respectively removing) the edge $i \rightarrow j$. We use $|G|$ to denote then number of edges in $G$. We denote by $\mathbb{S}^{p}$ the set of all bijections from $[p]$ to $[p]$. An element $\sigma \in \mathbb{S}^{p}$ is said to be a topological ordering for a DAG $G$ if the following holds: for any indices $k<l$, the edge between the nodes $\sigma(k)$ and $\sigma(l)$ is directed as $\sigma(k) \rightarrow \sigma(l)$, if it exists in $G$. Let $\sigma^{-1}$ denote the inverse function of $\sigma$, and for each node $j \in[p]$, let

$$
P_{j}^{\sigma}=\left\{i: \sigma^{-1}(i)<\sigma^{-1}(j)\right\}
$$

denote the set of potential parents of node $j$ under the ordering $\sigma$, i.e., all nodes preceding $j$ in $\sigma$. Let $\mathcal{G}_{p}$ be the collection of all $p$-node DAGs and $\mathcal{G}_{p}^{\sigma}$ be the collection of all $p$-node DAGs consistent with topological ordering $\sigma$; that is, $\mathcal{G}_{p}^{\sigma}=\left\{G \in \mathcal{G}_{p}:\{i \rightarrow j\} \in G\right.$ implies $\left.\sigma^{-1}(i)<$ $\left.\sigma^{-1}(j)\right\}$. Given a node $j$, we use $\mathrm{Pa}_{j}(G)$ and $\mathrm{Ch}_{j}(G)$ to denote the set of its parent nodes and that of its child nodes, respectively, in the DAG $G$. If the underlying DAG is clear from the context, we simply write $\mathrm{Pa}_{j}$ and $\mathrm{Ch}_{j}$. Finally, given a matrix $A \in \mathbb{R}^{a \times b}, j \in[b], J \subseteq[b]$ and $I \subseteq[a], A_{j}$ denotes the $j$-th column of $A, A_{J}$ denotes the submatrix of $A$ containing columns indexed by $J$, and $A_{I, j}$ denotes the subvector of $A_{j}$ with entries $\left\{A_{i j}: i \in I\right\}$. We use $|J|$ to denote the cardinality of the set $J$.

### 2.2 Model specification

Let $\mathrm{X}=\left(\mathrm{X}_{1}, \ldots, \mathrm{X}_{p}\right)$ denote a $p$-dimensional random vector, and denote by $X$ an $n \times p$ data matrix, each row of which is an independent copy of X . For each $\sigma \in \mathbb{S}^{p}$ and $G \in \mathcal{G}_{p}^{\sigma}$, consider the following structural equation model for the random vector X ,

$$
\mathrm{X}_{j}=B_{\mathrm{Pa}_{j}(G), j}^{\mathrm{T}} \mathrm{X}_{\mathrm{Pa}_{j}(G)}+\mathrm{e}_{j}, \quad \mathrm{e}_{j} \mid \omega \stackrel{\text { i.i.d }}{\sim} N(0, \omega) \text { for } j=1, \ldots, p
$$

where $\mathrm{Pa}_{j}(G) \subseteq P_{j}^{\sigma}$ for each $j$, and $B$ is a $p \times p$ matrix. Entries of $B$ that are not involved in (2) are set to zero. $B$ can be seen as the weighted adjacency matrix of the DAG $G$ such that $\{i \rightarrow j\} \in G$ if $\left|B_{i j}\right|>0$.

We use the following empirical prior on the parameter $(\sigma, G, B, \omega)$, where $\pi_{0}$ denotes the prior density function:

$$
\begin{aligned}
B_{\mathrm{Pa}_{j}(G), j} \mid G, \omega \stackrel{\text { ind }}{\sim} N_{\left|\mathrm{Pa}_{j}(G)\right|}\left(\hat{B}_{\mathrm{Pa}_{j}(G), j}, \frac{\omega}{\gamma}\left(X_{\mathrm{Pa}_{j}(G)}^{\mathrm{T}} X_{\mathrm{Pa}_{j}(G)}\right)^{-1}\right), \quad \forall j \in[p] \\
\pi_{0}(\omega \mid \sigma) & \propto \omega^{-\frac{\kappa}{2}-1} \\
\pi_{0}(G, \sigma) & \propto\left(p^{c_{0}}\right)^{-|G|} \mathbb{1}_{\left\{\hat{G}_{\sigma}\right\}}(G)
\end{aligned}
$$

where $\hat{B}_{\mathrm{Pa}_{j}(G), j}$ is the least-squares estimator of $B_{\mathrm{Pa}_{j}(G), j}, c_{0}, \gamma, \kappa$ are hyperparamters of the prior, and $\hat{G}_{\sigma}$ in (5) is the best estimate for $G$ among $\mathcal{G}_{p}^{\sigma}$; we will detail how to obtain $\hat{G}_{\sigma}$ later. This prior is doubly empirical. First, given $G$ and $\omega$, we use an empirical prior on $B_{\mathrm{Pa}_{j}(G), j}$ for each $j$ in (3), where the conditional prior mean depends on the data. Following Martin et al. [2017] and Lee et al. [2019], when computing the posterior distribution, we raise the data likelihood to the power of $\alpha$, where $\alpha \in(0,1)$ is a constant, so that we can reduce the influence of the data that is inflated by the usage of the empirical prior. Lee et al. [2019] suggests setting $\alpha$ close to 1 to make the $\alpha$-likelihood behave similarly to the standard likelihood in finite sample scenarios. Observe that the covariance in (3) is identical to that of Zellner's g-prior, proportional to the inverse Fisher information matrix for $B_{\mathrm{Pa}_{j}(G), j}$ [Tadesse and Vannucci, 2021]. An alternative approach to specifying the prior is to use the fractional Bayes factor [Carvalho and Scott, 2009, Castelletti and Consonni, 2021]. This yields a fractional posterior with the value of $\alpha$ determined automatically, but the resulting posterior is more difficult to calculate than the proposed posterior. Second, according to (5), the conditional prior distribution of $G$ given $\sigma$ is again empirical: it assigns unit mass to some $\hat{G}_{\sigma}$ that can be seen as the solution to a DAG selection problem given ordering $\sigma$. This implies that the marginal prior distribution of $G$ has support $\hat{\mathcal{G}}=\left\{\hat{G}_{\sigma}: \sigma \in \mathbb{S}^{p}\right\}$. For moderately large $p$, searching the entire space $\mathcal{G}_{p}$ is impossible, but the empirical prior (5) reduces the size of the search space to that of the order space $\mathbb{S}^{p}$. Unfortunately, $\left|\mathbb{S}^{p}\right|=p$ ! is still super-exponential in $p$, making it challenging to devise an efficient MCMC sampler.

Remark 1. The use of the empirical prior (5) makes our approach very different from traditional Bayesian structure learning methods, where posterior inference is performed by averaging over all DAG models that satisfy certain sparsity constraints. The seminal orderbased MCMC sampler of Friedman and Koller [2003] imposes a uniform conditional prior given $\sigma$ on all DAGs satisfying degree constraints in $\mathcal{G}_{p}^{\sigma}$. But calculating the un-normalized marginal posterior probability of an ordering requires summation over all possible DAGs, which is infeasible unless $p$ is small or the degree constraint is highly demanding. Further, the technique used in Friedman and Koller [2003, Eq. (8)] to expedite this calculation is not applicable in our case since our score is not decomposable; see Remark 2. Therefore, we prefer using the empirical prior (5) for its computational efficiency. A similar approach is taken in Agrawal et al. [2018], which uses empirical conditional independence tests to construct a minimal independence map for each ordering and restricts the search space to the set of minimal independence maps. Henceforth, we will always use DAG selection to refer to the problem of identifying the best DAG with given ordering.

Let $\pi_{n}$ denote the posterior distribution given the observed data matrix $X$. By a standard

normal-inverse-gamma calculation that integrates out the parameters $B$ and $\omega$, we get

$$
\pi_{n}(G, \sigma) \propto e^{\phi(G)} \mathbb{1}_{\left\{\hat{G}_{\sigma}\right\}}(G)
$$

where $\phi(G)$ is called the score of $G$ and is given by

$$
\begin{aligned}
& \phi(G)=-|G| c_{0} \log p-\frac{|G|}{2} \log [(1+\alpha / \gamma)]-\frac{\alpha p n+\kappa}{2} \log \left(\sum_{j=1}^{p} \operatorname{RSS}_{j}(G)\right) \\
& \text { where } \operatorname{RSS}_{j}(G)=X_{j}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}(G)}^{\downarrow} X_{j}, \quad \Phi_{S}^{\downarrow}=I-X_{S}\left(X_{S}^{\mathrm{T}} X_{S}\right)^{-1} X_{S}
\end{aligned}
$$

We will also sometimes refer to $\phi(G)$ as the posterior score. For a detailed derivation of (6), see Section B. 7 in the supplementary material. The marginal posterior probability of an ordering $\sigma$ and that of a DAG $G$ are

$$
\pi_{n}(\sigma) \propto e^{\phi\left(\hat{G}_{\sigma}\right)}, \quad \pi_{n}(G) \propto e^{\phi(G)} \sum_{\sigma \in \mathbb{S}^{p}} \mathbb{1}_{\left\{\hat{G}_{\sigma}\right\}}(G)
$$

For our model, $\pi_{n}(G)$ is not exactly proportional to the exponentiation of the score of $G$ due to the factor $\sum_{\sigma \in \mathbb{S}^{p}} \mathbb{1}_{\left\{\hat{G}_{\sigma}\right\}}(G)$, and in our high-dimensional analysis we will show this term is negligible under mild assumptions.

In the rest of this work, we consider the following choice for $\hat{G}_{\sigma}$,

$$
\hat{G}_{\sigma}^{\mathrm{MAP}}\left(d_{\text {in }}\right)=\arg \max _{G \in \mathcal{G}_{p}^{\sigma}\left(d_{\text {in }}\right)} \phi(G), \quad \forall \sigma \in \mathbb{S}^{p}
$$

where $\mathcal{G}_{p}^{\sigma}\left(d_{\text {in }}\right)=\left\{G \in \mathcal{G}_{p}^{\sigma}:\left|\operatorname{Pa}_{j}(G)\right| \leq d_{\text {in }}\right.$ for all $\left.j \in[p]\right\}$ is the collection of all $p$-node DAGs with maximum in-degree bounded by $d_{\text {in }}$. For our high-dimensional analysis, we will impose the condition $d_{\text {in }} \log p=o(n)$, which is commonly used in the literature on high-dimensional DAG selection [Cao et al., 2019, Lee et al., 2019]. The superscript MAP indicates that $\hat{G}_{\sigma}^{\text {MAP }}$ is the DAG with the largest posterior score among $\mathcal{G}_{p}^{\sigma}\left(d_{\text {in }}\right)$, i.e., the maximum a posteriori estimate.

Remark 2. In most existing methods for Bayesian structure learning, the posterior score of a DAG $G$ takes a decomposable form in the sense that it can be written as the sum of $p$ terms, where the $i$-th term only involves node $i$ and its parent set and thus can be evaluated locally. But our posterior score given in (7) is not decomposable due to the equal variance assumption used in the prior: integrating out $\omega$ results in the logarithm of the sum of $p$ residual sum of squares (RSS) terms in (7). This non-decomposable score is able to discriminate between Markov equivalent DAGs, and as we will prove shortly, given sufficiently large sample size, the posterior distribution of our model concentrates on only the unique true DAG.

# 2.3 Strong model selection consistency 

We consider a high-dimensional setting where $n$ tends to infinity and both $p=p(n)$ and $d_{\text {in }}=d_{\text {in }}(n)$ may grow with $n$. Strong model selection consistency means that the posterior probability of the true model converges to 1 in probability with respect to the true probability measure from which the data is generated. This is often regarded as one of the most important theoretical guarantees for a high-dimensional Bayesian model selection procedure. In the DAG literature, it was proven for DAG selection with known ordering [Cao et al., 2019,

Lee et al., 2019] and structure learning up to equivalence class [Zhou and Chang, 2021]. To the best of our knowledge, there is no strong selection consistency result on Bayesian structure learning under an identifiability condition.

Though the equal variance assumption was used in the prior specification, for our consistency analysis, we consider a more general setting. Assume the data is generated according to the structural equation model

$$
\mathrm{X}_{j}=\left(B_{\mathrm{Pa}_{j}\left(G^{*}\right), j}^{*}\right)^{\mathrm{T}} \mathrm{X}_{\mathrm{Pa}_{j}\left(G^{*}\right)}+\mathrm{e}_{j}, \quad \mathrm{e}_{j} \sim N\left(0, \omega_{j}^{*}\right) \text { for } j=1, \ldots, p
$$

where $G^{*}, B^{*},\left\{\omega_{j}^{*}\right\}_{j=1}^{p}$ denote the true parameter values, and we assume $B_{i j}^{*} \neq 0$ if and only if $\{i \rightarrow j\} \in G$. Define $\Omega^{*}=\operatorname{diag}\left(\omega_{1}^{*}, \ldots, \omega_{p}^{*}\right)$. Let $\left[\sigma^{*}\right]$ denote the set of all orderings consistent with $G^{*}$, where $\sigma^{*}$ is some element in $\left[\sigma^{*}\right]$ interpreted as the true ordering. Thus, $G^{*} \in \mathcal{G}_{p}^{\sigma}$ if and only if $\sigma \in\left[\sigma^{*}\right]$. Let $\mathbb{P}^{*}$ denote the probability measure corresponding to the structural equation model (10). Observe that the covariance matrix of the random vector X can be written as $\Sigma^{*}=\Sigma\left(B^{*}, \Omega^{*}\right)$, where

$$
\Sigma(B, \Omega)=\left(I_{p}-B^{\mathrm{T}}\right)^{-1} \Omega\left(I_{p}-B\right)^{-1}
$$

This is known as the modified Cholesky decomposition. This decomposition of $\Sigma^{*}$ is not unique, as we explain in the following remark.
Remark 3. For each ordering $\sigma \in \mathbb{S}^{p}$, there exists a unique tuple $\left(B_{\sigma}^{*}, \Omega_{\sigma}^{*}\right)$ such that $B_{\sigma}^{*}$ is the weighted adjacency matrix of a DAG in $\mathcal{G}_{p}^{\sigma}, \Omega_{\sigma}^{*}$ is a diagonal matrix with all diagonal entries being strictly positive, and $\Sigma^{*}=\Sigma\left(B_{\sigma}^{*}, \Omega_{\sigma}^{*}\right)$. Write $\Omega_{\sigma}^{*}=\operatorname{diag}\left(\omega_{1}^{\sigma}, \ldots, \omega_{p}^{\sigma}\right)$ and use $G_{\sigma}^{*}$ to denote the DAG with edge set $E_{\sigma}^{*}=\left\{(i, j):\left|\left(B_{\sigma}^{*}\right)_{i j}\right|>0\right\}$ and define

$$
d^{*}=\max _{\sigma \in \mathbb{S}^{p}} \max _{j \in[p]}\left|\operatorname{Pa}_{j}\left(G_{\sigma}^{*}\right)\right|
$$

To prove that the empirical Bayes model specified in Section 2 has strong model selection consistency in high-dimensional settings, we make the following two assumptions.
Assumption A (Minimum-trace condition). There exists a universal constant $\eta \in(0, \infty)$ such that $\min _{\sigma \notin\left[\sigma^{*}\right]} \operatorname{tr}\left(\Omega_{\sigma}^{*}\right) / \operatorname{tr}\left(\Omega^{*}\right)>1+\eta^{-1}$, where tr denotes the trace.
Assumption B (Consistency of DAG selection given true ordering). The estimator $\hat{G}_{\sigma}$ satisfies $\mathbb{P}^{*}\left(\cap_{\sigma \in\left[\sigma^{*}\right]}\left\{\hat{G}_{\sigma}=G^{*}\right\}\right) \geq 1-\zeta(p)$ for some $\zeta(p) \rightarrow 0$.

The first assumption includes the equal variance assumption as a special case. To see this, suppose that $\Omega^{*}=\operatorname{diag}\left(\omega^{*}, \ldots, \omega^{*}\right)$ for some $\omega^{*}>0$. Since the determinant of $\Sigma^{*}$ satisfies $\operatorname{det}\left(\Sigma^{*}\right)=\left(\omega^{*}\right)^{p}=\prod_{j=1}^{p} \omega_{j}^{\sigma}$ for all $\sigma \in \mathbb{S}^{p}$, we have $p \omega^{*} \leq \sum_{j=1}^{p} \omega_{j}^{\sigma}$ by the inequality of arithmetic and geometric means. That is, the true ordering $\sigma^{*}$ satisfies $\operatorname{tr}\left(\Omega_{\sigma^{*}}^{*}\right)=\min _{\sigma} \operatorname{tr}\left(\Omega_{\sigma}^{*}\right)$. Hence, there always exists some $\eta(n)$ such that $\min _{\sigma \notin\left[\sigma^{*}\right]} \operatorname{tr}\left(\Omega_{\sigma}^{*}\right) / \operatorname{tr}\left(\Omega^{*}\right)>1+\eta(n)^{-1}$. Assumption A just requires that $\eta(n)^{-1}$ can be bounded away from zero so that we can replace it with some universal constant $\eta$. Under the equal variance assumption, we can rewrite Assumption A as follows, which has been used in Van de Geer and Bühlmann [2013] and is known as the omega-min condition.
Assumption A' (Assumption A with equal variances). Suppose $\Omega^{*}=\operatorname{diag}\left(\omega^{*}, \ldots, \omega^{*}\right)$, where $\omega^{*}>0$ is the error variance shared by all node variables. There exists a universal constant $\eta \in(0, \infty)$ such that $\min _{\sigma \notin\left[\sigma^{*}\right]} p^{-1} \sum_{j=1}^{p}\left(\omega_{j}^{\sigma} / \omega^{*}\right)>1+\eta^{-1}$.

Remark 4. Recall our score function given in (7) and that $\operatorname{RSS}_{j} / n$ is an estimate of the error variance $\omega_{j}^{\sigma}$. So our method essentially aims to select the DAG that provides the tightest fit to the data. More precisely, the score (7) aims to learn the best DAG in $\mathcal{G}_{p}^{\sigma}$ where $\sigma$ minimizes $\operatorname{tr}\left(\Omega_{\sigma}^{*}\right)$, the sum of error variances; such a DAG is called the minimum-trace DAG. Our strong consistency result, which only requires Assumption A instead of Assumption A', confirms that though the equal variance assumption was used to derive (7), our method has the theoretical guarantee under a more general setting. We refer readers to Aragam et al. [2019] for a general theory on structure learning using minimum-trace DAGs.

Remark 5. An interesting open question is, without the equal variance assumption, what choices of $\left(B^{*}, \Omega^{*}\right)$ can satisfy the minimum-trace condition so that the true model is identifiable. We conjecture that if for some $\sigma^{*} \in \mathbb{S}^{p}$, we have $\omega_{\sigma^{*}(1)}^{\sigma^{*}} \leq \omega_{\sigma^{*}(2)}^{\sigma^{*}} \leq \cdots \leq \omega_{\sigma^{*}(p)}^{\sigma^{*}}$, then $\operatorname{tr}\left(\Omega_{\sigma^{*}}^{*}\right)=\min _{\sigma} \operatorname{tr}\left(\Omega_{\sigma}^{*}\right)$. This weakly increasing variance condition falls under the broader identifiability conditions presented in Park [2020], which extend beyond the equal variance assumption. We have conducted extensive numerical experiments, which suggest that the conjecture is likely to be true, but a proof for every $p \geq 2$ seems highly challenging. Simulation studies are presented in Section C. 2 of the supplement.

The second assumption says that when we are given an ordering $\sigma \in\left[\sigma^{*}\right]$, the pre-specified DAG selection procedure is able to identify the true DAG with high probability. This is a very mild assumption since if the ordering is known, one can often apply an existing consistent algorithm for high-dimensional variable selection to select the parent set of node $j$ for each $j \in[p]$ separately [Ben-David et al., 2011, Yu and Bien, 2017, Shojaie and Michailidis, 2010, Cao et al., 2019, Lee et al., 2019]. We do not need any assumption on the behavior of $\hat{G}_{\sigma}$ when $\sigma \notin\left[\sigma^{*}\right]$. Among many possible DAG selection methods, we use the estimator defined in (9) for the following reason. If some other DAG selection method is used, for any $\sigma \notin\left[\sigma^{*}\right]$, there is no guarantee that $\hat{G}_{\sigma}$ has a sufficiently large posterior score compared with other DAGs in $\mathcal{G}_{p}^{\sigma}$, and the resulting posterior distribution on the order space $\mathbb{S}^{p}$ could be very irregular and contain more sub-optimal local modes. However, no existing consistency result can be readily applied to the estimator (9) due to the non-decomposable posterior score it uses. We prove in the following proposition that it does have strong consistency for DAG selection, and it satisfies Assumption B with $\zeta(p)=4 p^{-1}$. All the three conditions assumed in Proposition 1 are commonly used in the literature: (C1) is known as the restricted eigenvalue condition, (C2) assumes prior parameters are properly chosen, and (C3) is often called the $\beta$-min condition [Lee et al., 2019]. Except universal constants, all parameters are allowed to depend on $n$.

Proposition 1. Suppose $\max _{j}\left|\operatorname{Pa}_{j}\left(G^{*}\right)\right| \leq d_{\text {in }}$, and the following conditions hold.
(C1) There exist $\underline{\nu}, \bar{\nu}>0$ and a universal constant $\delta>0$ such that

$$
\frac{\underline{\nu}}{(1-\delta)^{2}} \leq \lambda_{\min }\left(\Sigma^{*}\right) \leq \lambda_{\max }\left(\Sigma^{*}\right) \leq \frac{\bar{\nu}}{(1+\delta)^{2}}
$$

where $\lambda_{\min }, \lambda_{\max }$ are the smallest and largest eigenvalues, respectively.
(C2) The sparsity parameter $d_{\text {in }}$ satisfies $d_{\text {in }} \log p=o(n)$, and prior parameters satisfy that $\kappa \leq n p, 0 \leq \alpha / \gamma \leq p^{2}-1, c_{0}>\rho(\alpha+1) \max _{i \neq j}\left(\omega_{j}^{*} / \omega_{i}^{*}\right)$, and $\rho>4 d_{\text {in }}+6$.

(C3) For the true weighted adjacency matrix $B^{*}$,

$$
C_{\min }=\min \left\{\left|\left(B^{*}\right)_{i j}\right|^{2}:\left(B^{*}\right)_{i j} \neq 0\right\} \geq 16 c_{0} \frac{\bar{\nu}^{2} \log p}{\alpha \underline{\nu}^{2} n}
$$

Consider the posterior score given in (7) and the estimator defined in (9). For sufficiently large $n$, with probability at least $1-4 p^{-1}$, all the following three events happen.
(i) For any $\sigma \in\left[\sigma^{*}\right], G \in \mathcal{G}_{p}^{\sigma}\left(2 d_{\text {in }}\right), j \in[p]$ such that $\mathrm{Pa}_{j}\left(G^{*}\right) \subset \mathrm{Pa}_{j}(G)$, there exists some $G^{\prime} \in \mathcal{G}_{p}^{\sigma}$ such that $\phi\left(G^{\prime}\right)>\phi(G)$ and $G^{\prime}=G \backslash\{i \rightarrow j\}$ for some $i \in[p]$.
(ii) For any $\sigma \in\left[\sigma^{*}\right], G \in \mathcal{G}_{p}^{\sigma}\left(2 d_{\text {in }}\right), j \in[p]$ such that $\mathrm{Pa}_{j}\left(G^{*}\right) \not \subset \mathrm{Pa}_{j}(G)$, there exists some $G^{\prime} \in \mathcal{G}_{p}^{\sigma}$ such that $\phi\left(G^{\prime}\right)>\phi(G)$ and $G^{\prime}=G \cup\{i \rightarrow j\}$ for some $i \in[p]$.
(iii) For any $\sigma \in\left[\sigma^{*}\right], \hat{G}_{\sigma}^{\mathrm{MAP}}=G^{*}$.

Proof. See Section B. 2 in the supplementary material.
Remark 6. For computational efficiency, to estimate $\hat{G}_{\sigma}^{\mathrm{MAP}}$, one may use a forward-backward stepwise selection to find $\mathrm{Pa}_{j}$ for each $j$ separately. This is outlined in Algorithm 4 in Section A. 2 of the supplementary material. Since the posterior score is not decomposable, the stepwise selection at node $j$ depends on the values of $\left\{\mathrm{RSS}_{i}: i \neq j\right\}$. A simple solution is to estimate $\mathrm{RSS}_{i}$ by $X_{i}^{\mathrm{T}} X_{i}$ for each $i \neq j$. Then, parts (i) and (ii) of Proposition 1 imply that this procedure is consistent as long as for each $j,\left|\mathrm{Pa}_{j}\right|$ is bounded by $d_{\text {in }}$ at the end of the forward phase in Algorithm 4. As shown in An et al. [2008] and Zhou [2010], this condition on the output of forward selection can often be satisfied, with high probability, by choosing some $d_{\text {in }}=O\left(\max _{j}\left|\mathrm{~Pa}_{j}\left(G^{*}\right)\right|\right)$; i.e., $d_{\text {in }}$ has the same order as the maximum in-degree of $G^{*}$. Actually, Proposition 1 implies that the following procedure is also consistent: starting from an arbitrary DAG $G$ with maximum in-degree bounded by $d_{\text {in }}$, one performs stepwise selection at each node $j$ by setting $\mathrm{RSS}_{i}=\mathrm{RSS}_{i}(G)$ for each $i \neq j$.
Remark 7. An alternative approach to performing forward-backward DAG selection with given ordering is to consider all the $p$ nodes jointly; see Algorithm 5 in Section A. 3 of the supplementary material. In the forward phase, we add one best edge consistent with the given ordering in each iteration, while in the backward phase, we remove one edge in each iteration. Proposition 1 implies that this algorithm is also consistent for $\sigma \in\left[\sigma^{*}\right]$, provided that the maximum in-degree of any DAG on the search path is bounded by $d_{\text {in }}$.

The main result of this section is given in the following theorem.
Theorem 1 (Strong selection consistency). Suppose Assumption A, B hold, and assume that $d^{*} \leq d_{\text {in }}$ and $d_{\text {in }} \log p=o(n)$. Then $\pi_{n}\left(G^{*}\right)$ converges in probability to 1 with respect to $\mathbb{P}^{*}$, where $\pi_{n}$ is as given in (8).

Proof. See Section B. 3 in the supplementary material.
Remark 8. The proof can be further extended to cases where the errors $\mathbf{e}_{j}, j=1, \ldots, p$ in (10) follow a sub-Gaussian distribution. As any bounded random variable is sub-Gaussian, this relaxation covers scenarios where some variables are normally distributed and others are discrete and bounded [Lauritzen, 1992]. The proof is given in Section B. 4 in the supplementary material. Some inequalities cannot be obtained as sharply as in the Gaussian case, because zero correlation does not imply independence in the sub-Gaussian case.

Consider the marginal posterior distribution on the order space $\mathbb{S}^{p}$. The following corollary shows that the posterior mass concentrates on the set of orderings consistent with $G^{*}$, and the posterior probabilities of all other orderings vanish.

Corollary 1. Under the setting of Theorem $1, \pi_{n}\left(\left[\sigma^{*}\right]\right)$ converges in probability to 1 with respect to $\mathbb{P}^{*}$.

Proof. This follows from Theorem 1 and $\pi_{n}\left(G^{*}\right)=\sum_{\sigma \in\left[\sigma^{*}\right]} \pi_{n}\left(G^{*}, \sigma\right)=\sum_{\sigma \in\left[\sigma^{*}\right]} \pi_{n}(\sigma)$.

# 3 Posterior sampling via order MCMC 

### 3.1 Metropolis-Hastings algorithms on the order space

To generate posterior samples for our model, we use random walk Metropolis-Hastings algorithms on the order space $\mathbb{S}^{p}$. For each $\sigma \in \mathbb{S}^{p}$, let $\mathbf{K}(\sigma, \cdot)$ denote the proposal distribution at state $\sigma$. We consider three types of random walk proposals: adjacent transposition, which is a standard choice for order-based MCMC methods [Friedman and Koller, 2003, Agrawal et al., 2018], random transpositions and random-to-random shuffles, which are more commonly seen in the literature on random walks on symmetric groups [Levin and Peres, 2017, Bernstein and Nestoridi, 2019]. All three types of proposals correspond to defining $\mathbf{K}(\sigma, \cdot)$ by

$$
\mathbf{K}(\sigma, A)=\frac{|\mathcal{N}(\sigma) \cap A|}{|\mathcal{N}(\sigma)|}, \quad \forall A \subseteq \mathbb{S}^{p}
$$

for some set $\mathcal{N}(\sigma) \subset \mathbb{S}^{p}$. We refer to $\mathcal{N}(\sigma)$ as the neighborhood of $\sigma$, and now we formally define this set for each type of proposal. Let $(\cdot)_{\mathrm{c}}$ denote an ordering in the cycle notation; for example, $\mu=(a, b, c)_{\mathrm{c}}$ is the ordering given by $\mu(a)=b, \mu(b)=c, \mu(c)=a$ and $\mu(k)=k$ for every $k \notin\{a, b, c\}$. Let $\circ$ denote the composition of two orderings; that is, $\tau=\sigma \circ \mu$ is defined by $\tau(i)=\sigma(\mu(i))$. Then, we can use $\sigma \circ(i, j)_{\mathrm{c}}$ to denote the ordering obtained by interchanging the $i$-th and the $j$-th elements of $\sigma$ while keeping the others unchanged. Let $\sigma \circ \xi(i, j)$ denote the ordering obtained by inserting the $i$-th element of $\sigma$ to the $j$-th position, where $\xi(i, j)$ is defined by $\xi(i, j)=(i, i+1, \ldots, j)_{\mathrm{c}}$ if $i<j$, and $\xi(i, j)=(i, i-1, \ldots, j)_{\mathrm{c}}$ if $i>j$. Define the adjacent transposition neighborhood by

$$
\mathcal{N}_{\mathrm{adj}}(\sigma)=\left\{\sigma^{\prime} \in \mathbb{S}^{p} \mid \sigma^{\prime}=\sigma \circ(i, i+1)_{\mathrm{c}}, i \in[p-1]\right\}
$$

that is, $\mathcal{N}_{\text {adj }}(\sigma)$ is the set of all orderings that can be obtained from $\sigma$ by one adjacent transposition. Similarly, we denote the neighborhood corresponding to random transpositions by $\mathcal{N}_{\text {rtp }}$ and that corresponding to random-to-random shuffles by $\mathcal{N}_{\text {rrs }}$, which are defined by

$$
\begin{aligned}
& \mathcal{N}_{\text {rtp }}(\sigma)=\left\{\sigma^{\prime} \in \mathbb{S}^{p} \mid \sigma^{\prime}=\sigma \circ(i, j)_{\mathrm{c}}, i<j, \text { and } i, j \in[p]\right\} \\
& \mathcal{N}_{\text {rrs }}(\sigma)=\left\{\sigma^{\prime} \in \mathbb{S}^{p} \mid \sigma^{\prime}=\sigma \circ \xi(i, j), i \neq j, \text { and } i, j \in[p]\right\}
\end{aligned}
$$

We provide an illustration of the three proposals in the supplementary material A.4. Observe that all the three neighborhood relations defined above are symmetric: if $\sigma^{\prime} \in \mathcal{N}(\sigma)$, then $\sigma \in \mathcal{N}\left(\sigma^{\prime}\right)$. Therefore, by the Metropolis rule, the transition matrix of the algorithm can be

calculated by

$$
\mathbf{P}\left(\sigma, \sigma^{\prime}\right)= \begin{cases}\mathbf{K}\left(\sigma, \sigma^{\prime}\right) \min \left\{1, \frac{\pi_{n}\left(\sigma^{\prime}\right) \mathbf{K}\left(\sigma^{\prime}, \sigma\right)}{\pi_{n}(\sigma) \mathbf{K}\left(\sigma, \sigma^{\prime}\right)}\right\}, & \text { if } \sigma^{\prime} \neq \sigma \\ 1-\sum_{\tau \neq \sigma} \mathbf{P}(\sigma, \tau), & \text { if } \sigma^{\prime}=\sigma\end{cases}
$$

where $\pi_{n}(\sigma)$ is the marginal posterior probability and also the stationary probability of $\sigma$. The Hastings ratio $\mathbf{K}\left(\sigma^{\prime}, \sigma\right) / \mathbf{K}\left(\sigma, \sigma^{\prime}\right)=1$ for all the three neighborhood relations we consider. As explained in Section 2, once we select an ordering $\sigma \in \mathbb{S}^{p}$, we can find the associated $\hat{G}_{\sigma}$ by a pre-specified DAG selection method. Further, given a stationary Markov chain $\left(\sigma_{t}\right)_{t \geq 1}$ with transition matrix $\mathbf{P},\left\{\hat{G}_{\sigma_{t}}\right\}_{t \geq 1}$ can be seen as correlated samples drawn from the marginal posterior distribution on the DAG space given in (8), which is just the pushforward of the marginal posterior distribution on $\mathbb{S}^{p}$ under the mapping $\sigma \mapsto \hat{G}_{\sigma}$.

The choice of the neighborhood $\mathcal{N}(\cdot)$ may affect the mixing of the chain significantly. In order to achieve efficient local exploration, the neighborhood size needs to be small. All the three types of proposals considered are desirable in this regard, since the corresponding neighborhood sizes grow at most quadratically in $p:\left|\mathcal{N}_{\text {adj }}(\sigma)\right|=p-1$, and $\left|\mathcal{N}_{\text {rtp }}(\sigma)\right|=$ $\left|\mathcal{N}_{\text {rrs }}(\sigma)\right|=p(p-1) / 2$. However, if the neighborhood size is too small, the chain might get stuck at sub-optimal local modes, where a local mode refers to a state with posterior probability larger than that of any neighboring state. We will present a simulation study in Section 4.1 which confirms that all three proposals yield good mixing of the sampler for moderately large $p$.

In general, theoretical analysis of the mixing behavior of order-based MCMC methods is very difficult. Existing results on the mixing of MCMC for high-dimensional model selection problems suggest that if the posterior distribution is unimodal and tails decay sufficiently fast, an MCMC sampler is expected to mix rapidly [Yang et al., 2016, Zhou and Chang, 2021, Chang et al., 2022]; this intuition is highly similar to the rapid mixing of the algorithms with log-concave targets on continuous spaces [Mangoubi and Smith, 2017, Dwivedi et al., 2018]. However, to rigorously prove a rapid mixing result for our problem seems very difficult. One possible strategy is to assume a permutation $\beta$-min condition [Aragam et al., 2019], but such a permutation $\beta$-min condition is very restrictive since it requires all nonzero edge weights to be sufficiently large no matter what topological ordering we assume; in our context, this condition means that $\hat{G}_{\sigma}$ is equal to $G_{\sigma}^{*}$ for any $\sigma \in \mathbb{S}^{p}$. Here we choose to consider a contrasting setting where all the edge weights of the true DAG $G^{*}$ are not too large. This is probably more realistic and complements the existing theory, though still being moderately restrictive; see Remark 10 below. We are able to prove that the acceptance probability cannot be extremely small for any state proposed from $\mathcal{N}_{\text {adj }}(\cdot)$; see Remark 9. That is, by using adjacent transpositions, the chain is able to escape from any sub-optimal local mode, if there is any, in a relatively short amount of time. Observe that for any $\sigma \in \mathbb{S}^{p}, \mathcal{N}_{\text {adj }}(\sigma)$ is a proper subset of both $\mathcal{N}_{\text {rtp }}(\sigma)$ and $\mathcal{N}_{\text {rrs }}(\sigma)$. Hence, our result partly explains why all the three proposals appear to work well.

Proposition 2. Assume (C1) in Proposition 1 and the following conditions hold.
$\left(\mathrm{C} 1^{\prime}\right)$ The true covariance matrix $\Omega^{*}=\operatorname{diag}\left(\omega^{*}, \ldots, \omega^{*}\right)$ for some universal constant $\omega^{*}>0$,

and the edge weights of $G^{*}$ satisfy

$$
\max _{i, j \in[p]}\left|B_{i j}^{*}\right|^{2}=O\left(\frac{\bar{\nu}^{2} \log p}{\underline{\nu}^{2} n}\right)
$$

(C2') The parameter $d_{\text {in }}$ satisfies $d^{*} \leq d_{\text {in }}$ and

$$
d_{\text {in }}^{2} \frac{\bar{\nu}^{2} \log p}{\underline{\nu}^{2} n} \rightarrow 0 \text { as } n \rightarrow \infty
$$

Let $\mathcal{N}_{\text {rev }}(G)$ denote the set of all DAGs that can be obtained by applying one edge reversal to $G$, and $c>0$ be an arbitrary universal constant. Then, for sufficiently large $n$,

$$
\max _{\sigma \in \mathbb{S}^{p}} \max _{G_{1} \in \mathcal{G}_{p}^{\sigma}\left(d_{\text {in }}\right)} \max _{G_{2} \in \mathcal{N}_{\text {rev }}\left(G_{1}\right)} \frac{\exp \left(\phi\left(G_{1}\right)\right)}{\exp \left(\phi\left(G_{2}\right)\right)} \leq p^{c \bar{\nu}^{2} / \nu^{3}}
$$

with probability at least $1-6 p^{-1}$.
Proof. See Section B. 5 in the supplementary material.
Remark 9. To see the implication of this result on the mixing of our order MCMC, consider $\sigma=(1,2, \ldots, p)$, and let $\tau=\sigma \circ(i, i+1)_{\mathrm{c}}$ for some $i$. Recall that we use $\hat{G}_{\sigma}=\hat{G}_{\sigma}^{\mathrm{MAP}}$ where $\hat{G}_{\sigma}^{\mathrm{MAP}}$ is defined in (9). Hence, $\pi_{n}(\sigma) / \pi_{n}(\tau) \leq \exp \left(\phi\left(\hat{G}_{\sigma}\right)\right) / \exp \left(\phi\left(G^{\prime}\right)\right)$ where $G^{\prime}$ is the DAG that results from reversing the edge $i \rightarrow(i+1)$ of $\hat{G}_{\sigma}$; if the edge does not exist, then $G^{\prime}=\hat{G}_{\sigma}$. Assuming $\bar{\nu}, \underline{\nu}$ are bounded, Proposition 2 implies that with high probability $\pi_{n}(\sigma) / \pi_{n}(\tau)$ is bounded from above by $p^{c}$ where $c>0$ is arbitrary, as long as $G^{\prime} \in \mathcal{G}_{p}^{\tau}\left(d_{\text {in }}\right)$. For the schemes we propose on $\mathbb{S}^{p}$, this further implies that an adjacent transposition proposal has acceptance probability greater than $p^{-c}$, and thus the chain cannot get trapped at a local mode for exponentially many iterations in expectation.

Remark 10. The purpose of Proposition 2 is to theoretically analyze the posterior landscape when we probably do not have posterior concentration at the true model and Proposition 1 no longer holds. In particular, Proposition 2 does not require any assumption on the hyperparameters of our model, so the nonzero entries in $B^{*}$ may or may not be detected, depending on the choice of $c_{0}$. Condition (C1') essentially requires that no signal size has a strictly larger order than the detection threshold given in condition (C3) of Proposition 1. This is restrictive but arguably represents a scenario of more practical interest than Proposition 1, since in reality signals of small or moderate sizes are common. It is possible to construct a scenario where the assumptions of Propositions 1 and 2 both hold. For example, assume $d^{*}=O(1)$, which is referred to as the ultra-high sparsity regime in the literature [Van de Geer and Bühlmann, 2013]. Then we can set $d_{\text {in }}=O(1)$, which implies that we can choose $c_{0}=O(1)$ to satisfy condition (C2) of Proposition 1. Assuming $\bar{\nu}, \underline{\nu}$ are bounded for convenience, in order to satisfy condition (C3) of Proposition 1 and condition (C1') of Proposition 2, we just need to require that the order of any nonzero entry $B_{i j}^{*}$ is exactly given by $n^{-1} \log p$.

# 3.2 Iterative top-down initialization 

Standard theory yields that the Markov chain defined in (14) converges to the marginal posterior distribution on $\mathbb{S}^{p}$ in total variation distance regardless of the initial state. However, the actual mixing rate of the chain we observe depends on the initial state [Sinclair, 1992, Proposition 1], and in general, it is desirable to start the chain at a state with reasonably high posterior probability. Since the size of $\mathbb{S}^{p}$ grows super-exponentially in $p$, choosing a warm start for our sampler can significantly improve the performance of posterior estimation with MCMC samples. We propose an initialization method for our order MCMC sampler, called iterative top-down, which aims to quickly find the topological ordering of the true data-generating DAG $G^{*}$.

Our method is based on the top-down method proposed by Chen et al. [2019], which we now briefly explain. We say a node in a DAG is a source if the node has no parents. If the data is generated according to (2), due to the equal variance assumption, a source node always has the smallest marginal variance, and any node with at least one parent has a strictly larger marginal variance. The top-down method first identifies a source node of $G^{*}$, which always exists, sets it to $\hat{\sigma}(1)$ and then removes it from $G^{*}$. The resulting subgraph is also a DAG, and thus we can set $\hat{\sigma}(2)$ to a source node of this subDAG; how to identify the source node is explained in the next paragraph. Repeating this procedure $p$ times, we obtain $\hat{\sigma}$, the top-down estimator for the ordering.

Suppose that in the first $k$ iterations of the top-down method we have identified $\sigma(j)=j$ for $j=1, \ldots, k$. Then in the $(k+1)$-th iteration, we need to estimate the variance of each remaining node that cannot be explained by the first $k$ nodes, and pick the node with the smallest unexplained variance, which we infer as a source node of the subDAG of the remaining $p-k$ nodes. Chen et al. [2019] estimated the unexplained variance of the node $j$ (assuming $j>k$ ) by $\min _{S \subseteq[k],|S|=d_{\text {in }}} X_{j}^{\mathrm{T}} \Phi_{S}^{\perp} X_{j}$, but they noted that a variable selection procedure may be applied as well. Since our purpose is to find a warm start for our order MCMC sampler, we estimate the unexplained variance of a node by performing a variable selection procedure that aims to maximize the score (7). One caveat is that since our score is non-decomposable, when inferring the parent set of node $j$, we need to know the residual

```
Algorithm 1: Score-based top-down algorithm
    Input: A positive vector \(\operatorname{RSS}=\left(\operatorname{RSS}_{1}, \ldots, \operatorname{RSS}_{p}\right)\) (for all displayed algorithms, we
        assume the data \(X\) and parameters \(\left(c_{0}, \gamma, \alpha, \kappa, d_{\text {in }}\right)\) are given).
    \(1 \hat{\sigma} \leftarrow \arg \min _{j \in[p]} \mathrm{RSS}_{j}\)
    while \(|\hat{\sigma}|<p\) do
        for \(j \in[p] \backslash \hat{\sigma}\) do
            \(S \leftarrow \arg \max _{S_{j} \subset \hat{\sigma}:|S_{j}| \leq d_{\text {in }}} \phi_{j}\left(S_{j}, \sum_{i \neq j} \mathrm{RSS}_{i}\right)\)
            \(\prime / \phi_{j}(S, R)=-|S| \log \left\{p^{c_{0}} \sqrt{(1+\alpha / \gamma)}\right\}-\frac{\alpha p n+\kappa}{2} \log \left(R+X_{j}^{\mathrm{T}} \Phi_{S}^{\perp} X_{j}\right)\)
            \(\mathrm{RSS}_{j} \leftarrow X_{j}^{\mathrm{T}} \Phi_{S}^{\perp} X_{j}\)
            \(j_{0} \leftarrow \arg \min _{j \in[p] \backslash \hat{\sigma}} \mathrm{RSS}_{j}\)
            \(\hat{\sigma} \leftarrow\left(\hat{\sigma}, j_{0}\right)\)
    Output: An ordering \(\hat{\sigma}\), a vector of estimated residual sums of squares RSS.
```

```
Algorithm 2: Iterative top-down algorithm
1 \(\left(\hat{\sigma}^{\mathrm{ITD}}, \mathrm{RSS}\right) \leftarrow \operatorname{STD}\left(X_{1}^{\mathrm{T}} X_{1}, \ldots, X_{p}^{\mathrm{T}} X_{p}\right) / /\) STD refers to Algorithm 1
2 while 1 do
    \(\left(\tilde{\sigma}, \mathrm{RSS}^{\prime}\right) \leftarrow \mathrm{STD}(\mathrm{RSS})\)
    if \(\hat{\sigma}^{\mathrm{ITD}} \neq \tilde{\sigma}\) then
        \(\mathrm{RSS} \leftarrow \mathrm{RSS}^{\prime}\)
        \(\hat{\sigma}^{\mathrm{ITD}} \leftarrow \tilde{\sigma}\)
    else
    return \(\hat{\sigma}^{\mathrm{ITD}}\)
```

Output: An ordering $\hat{\sigma}^{\mathrm{ITD}}$
sums of squares of all the other $p-1$ nodes. This motivates us to propose the iterative top-down method, detailed in Algorithm 2, which iteratively applies the top-down procedure and updates all the $p$ residual sums of squares. We prove below that under a condition similar to that of Chen et al. [2019, Theorem 2], the iterative top-down algorithm identifies an ordering consistent with $G^{*}$ with high probability. In our simulation studies, we observe that the algorithm usually converges within 5 iterations.

Theorem 2. Suppose the conditions in Proposition 1 hold, and let $\epsilon \in(0,1)$. If

$$
n>\left\{\bar{\nu}\left(d_{\text {in }}+1\right)\left(\underline{\nu}+3 \omega^{*}\left(1+1 / C_{\min }\right)\right) / \underline{\nu}^{2}\right\}^{2} 3200\left(\log \left(p^{2}-p\right)-\log (\epsilon / 4)\right)
$$

then for sufficiently large $n$, Algorithm 2 returns an ordering in $\left[\sigma^{*}\right]$ with probability at least $1-\epsilon$.

Proof. See Section B. 6 in the supplementary material.

# 3.3 Reducing variance of edge estimation 

One potential limitation of our order MCMC sampler is that it does not take into account the uncertainty in DAG selection with given ordering. So we propose to estimate edge posterior inclusion probabilities using a conditioning scheme. Let $\sigma^{(t)}$ denote the $t$-th sample from our order MCMC sampler, and $\Gamma^{(t)}$ denote the adjacency matrix of the DAG $G^{(t)}=\hat{G}_{\sigma^{(t)}}$ such that $\Gamma_{i j}^{(t)}=1$ if $\{i \rightarrow j\} \in G^{(t)}$ and $\Gamma_{i j}^{(t)}=0$ otherwise. The posterior inclusion probability of edge $i \rightarrow j$ can be estimated by $T^{-1} \sum_{t=1}^{T} \Gamma_{i j}^{(t)}$ where $T$ denotes the number of MCMC samples. To improve this estimator, for each pair $\left(\sigma^{(t)}, G^{(t)}\right)$, we calculate $\hat{\Gamma}^{(t)}=\hat{\Gamma}\left(\sigma^{(t)}, G^{(t)}\right)$, where the function $\hat{\Gamma}$ is given by

$$
\hat{\Gamma}_{i j}(\sigma, G)=\frac{e^{\phi\left(G \cup\{i \rightarrow j\}\right)}}{e^{\phi\left(G \cup\{i \rightarrow j\}\right)}+e^{\phi\left(G \backslash\{i \rightarrow j\}\right)}} \mathbb{1}_{P_{i j}^{\sigma}}(i), \quad \forall i, j \in[p]
$$

We can now estimate the posterior inclusion probability of edge $i \rightarrow j$ by $\hat{\Gamma}_{i j}^{\mathrm{RB}}=T^{-1} \sum_{t=1}^{T} \hat{\Gamma}_{i j}^{(t)}$. The superscript RB indicates that, in a general sense, this can be seen as a Rao-Blackwellizedtype estimator [Robert and Roberts, 2021]. In our numerical experiments, we find this scheme helps reduce the variance of edge posterior inclusion probability estimates.

# 4 Simulation studies 

### 4.1 Mixing behavior

We first present a numerical example which illustrates how the choice of neighborhood and score equivalence property affect the mixing behavior of order MCMC samplers. We generate a 20 -node random DAG $G^{*}$ where any two distinct nodes are connected by an edge with probability 0.1 , and sample the edge weight $B_{i j}^{*}$ for each $i \rightarrow j$ in $G^{*}$ uniformly from $[-1,-0.5] \cup[0.5,1]$. Then, we simulate the data matrix $X$ using the structural equation model in (2) with $n=1,000$ and error variance $\omega^{*}=1$.

We implement the order MCMC sampler described in Section 3 with $\mathcal{N}=\mathcal{N}_{\text {adj }}, \mathcal{N}_{\text {rtp }}$ or $\mathcal{N}_{\text {rrs }}$. To impartially compare the three types of proposal, we need to take into account the computational complexity of sampling from each type of neighborhood. Consider a proposal move from $\sigma$ to $\sigma^{\prime}=\sigma \circ(i, j)_{\mathrm{c}}$ for some $i<j$. In Section A. 3 of the supplementary material, we present a stepwise procedure for selecting the parent set of a given node in Algorithm 4, and describe how to efficiently obtain $\hat{G}_{\sigma^{\prime}}$ from $\hat{G}_{\sigma}$ by applying Algorithm 4 at nodes $\sigma(i), \sigma(i+1), \ldots, \sigma(j)$. Hence, an adjacent transposition always requires performing Algorithm 4 at two nodes, while for a random transposition, which randomly samples $\sigma^{\prime}$ from $\mathcal{N}_{\text {rtp }}(\sigma)$ with equal probability, on average we need to perform Algorithm 4 at $(p+4) / 3 \approx p / 3$ nodes, and the same holds true for a random-to-random shuffle. So, when we run the sampler defined in (14) for $T$ iterations, we say the effective number of iterations is $2 T$ if $\mathcal{N}=\mathcal{N}_{\text {adj }}$, and $p T / 3$ if $\mathcal{N}=\mathcal{N}_{\text {rtp }}$ or $\mathcal{N}=\mathcal{N}_{\text {rrs }}$. We let the effective number of iterations be 10,000 for all three samplers in our simulation; that is, we run our sampler with $\mathcal{N}=\mathcal{N}_{\text {adj }}$ for 5,000 iterations, and the samplers with $\mathcal{N}=\mathcal{N}_{\text {rtp }}$ and $\mathcal{N}=\mathcal{N}_{\text {rrs }}$ for 1,500 iterations. We plot the trajectories for 30 runs with random initialization in the panels (a), (b), (c) of Fig. 1, from which we see that all three proposals work well. We have also tried $n=100$ and observed good mixing performance, probably because with a smaller sample size the posterior distribution tends to be flatter [Agrawal et al., 2018]; we display the result in Section C. 1 of the supplementary material. Given that adjacent transposition appears to yield the best mixing, it will be used for all the remaining numerical studies.

To compare our method with a score equivalent procedure, we consider the following posterior score, which is decomposable and yields the same value for Markov equivalent DAGs,

$$
\phi_{\mathrm{eq}}(G)=-|G| c_{0} \log p-\frac{|G|}{2} \log [(1+\alpha / \gamma)]-\frac{\alpha n+\kappa}{2} \sum_{j=1}^{p} \log \left(\operatorname{RSS}_{j}(G)\right)
$$

This score can be derived by a slight modification of our model: instead of assuming equal error variances, use an error variance parameter $\omega_{j}$ for each $\mathrm{e}_{j}$ in (2) and put an inversegamma prior on $\omega_{j}$ [Zhou and Chang, 2021]. To sample from the corresponding posterior distribution, we use the minimal I-MAP MCMC sampler of Agrawal et al. [2018], which is also a Metropolis-Hastings algorithm defined on the order space and proposes moves from the adjacent transposition neighborhood $\mathcal{N}_{\text {adj }}(\cdot)$; compared with our method, the main difference is that the minimal I-MAP MCMC uses conditional independence tests to find $\hat{G}_{\sigma}$. We run the minimal I-MAP MCMC for 10,000 iterations, and plot 30 trajectories with random

![img-0.jpeg](img-0.jpeg)

Figure 1: Log posterior probability ×10<sup>−4</sup> versus the effective number of iterations in 30 MCMC runs with random initialization. The red line gives the log posterior probability of the true ordering σ*. Panel (d) is for the minimal I-MAP MCMC with decomposable score. Panels (a), (b), (c) correspond to our method with three types of proposals: (a) adjacent transposition, (b) random transposition, (c) random-to-random shuffle. We have checked that, for our method, all 30 × 3 = 90 runs have successfully reached the red line.

initialization in Fig. 1(d). Comparing it with Fig. 1(a), we see that our sampler with non-decomposable score mixes better in the sense that all 30 trajectories are able to visit some σ ∈ [σ*], while the minimal I-MAP MCMC may get stuck at local modes depending on the initialization. As we have explained in Section 1, score equivalence is likely to make the posterior distribution on the order space (or the DAG space) difficult to explore due to the existence of large equivalence classes. This simple numerical study verifies that the use of identifiability conditions does simplify the posterior distribution so that MCMC samplers tend to mix faster. In Section C.1 of the supplementary material, we show that the same observation can still be made if we simulate X using unequal error variances.

### 4.2 Performance evaluation

We conduct simulation studies to empirically evaluate the performance of the proposed order MCMC sampler. We still use G* to denote the true p-node DAG that governs the data generating process described in (2) and let Γ* be its adjacency matrix. Let Ğ and Ğ denote the corresponding estimators, and for our method, we always use ĥ = ĥRB where ĥRB is defined in Section 3.3. Entries of ĥ are edge posterior inclusion probability estimates and thus take value in [0, 1], while Γ* ∈ {0, 1}<sup>p×p</sup>. We use four performance metrics to evaluate an estimator. The structural Hamming distance (HD) between G* and Ğ is the number of different edges between G* and Ğ, which equals ∑<sub>i,j</sub> |Γ<sup>*</sup><sub>ij</sub> − ĥ<sub>ij</sub>|. False negative rate (FNR) and false discovery rate (FDR) are defined as (∑<sub>i,j</sub> Γ*<sup>*</sup><sub>ij</sub> (1 − ĥ<sub>ij</sub>)) / |G*| × 100% and (∑<sub>i,j</sub>(1 − Γ*<sup>*</sup><sub>ij</sub>) ĥ<sub>ij</sub>) / |Ğ| × 100%, respectively. The fourth metric, percentage of flipped edges, is calculated as (∑<sub>i,j</sub> Γ*<sup>*</sup><sub>ji</sub> ĥ<sub>ij</sub>) / |G*| × 100%. We compare our method with two competing algorithms, the top-down method [Chen et al., 2019] and the algorithm of Ghoshal and Honorio [2018], and we follow the suggestions given in the two papers to choose the tuning parameters. These two algorithms are reported to have better performance than others. For our method, we fix α = 0.99, γ = 0.01, κ = 0, c<sub>0</sub> = 3 and run MCMC for 3,000 iterations for each simulated data set and discard the first 1,500 samples as burn-in. We always use


Table 1: Uniform signal case with $p=40$. TD and LISTEN refer to the top-down algorithm and the algorithm of Ghoshal and Honorio [2018], respectively. Each entry gives mean $\pm 1$ standard error. Time is measured in seconds.
the following procedure to generate the true $\mathrm{DAG} G^{*}$. We fix the true ordering to be $\sigma^{*}=(1, \ldots, p)$, and for each pair $(i, j)$ such that $i<j$, we add edge $i \rightarrow j$ to $G^{*}$ with probability $p_{\text {edge }}=3 /(2 p-2)$. Hence, the expected number of edges of $G^{*}$ is $3 p / 4$. The $\mathrm{DAG} G^{*}$ is resampled for each simulated data set.

We first generate the data from the structural equation models given in (2). We fix $p=40$, set $\omega^{*}=1$, and draw the edge weight $B_{i j}^{*}$ for each edge $i \rightarrow j$ in $G^{*}$ independently from some distribution $F$. We let sample size $n$ be 100,500 or 1,000 , and repeat 30 times for each choice. In Table 1, we present the result for $F$ being the uniform distribution on $[-1,-0.3] \cup[0.3,1]$ and that for $F$ being the uniform distribution on $[-1,-0.1] \cup[0.1,1]$. The result for $F$ being the standard Gaussian distribution is displayed in Section C. 2 in the supplementary material. Table 1 shows that our method outperforms the other two methods in all settings by any of the four performance metrics, and in most cases, our method is better by a margin of at least one standard error.


Table 2: Simulation under a high-dimensional regime. Each entry gives mean $\pm 1$ standard error. Time is measured in seconds.

![img-1.jpeg](img-1.jpeg)

Figure 2: Boxplots for heterogeneous error variance case with n = 500, p = 40. We sample error variances from Uniform([1 − b, 1 + b]) for b = 0, 0.1, ..., 0.9 and nonzero edge weights from Uniform([−1, −0.3[∪[0.3, 1]). The x-axis indicates the heterogeneity parameter b, and the y-axis represents the Hamming distance between the estimated DAG and G*. MINIMAP is the minimal I-MAP MCMC that uses score (16), and thus it is score equivalent.

Next, we examine the performance of our method with varying n and p. To emulate a high-dimensional asymptotic regime where n grows linearly and p increases exponentially, we consider 7 settings where n = 30(k + 1) and p = 7 · 2<sup>k−1</sup> in the k-th setting. When k = 6 or 7, we have p > n. We generate G* with p<sub>edge</sub> = d/(p − 1), where d = 0.2√n is the expected number of neighbors for each node. We sample the edge weight B*<sub>ij</sub> for each i → j in G* uniformly from [−1, −0.5] ∪ [0.5, 1] and set the error variance ω* = 1. We use the same values for α, γ, κ, c<sub>0</sub> and run 3,000 MCMC iterations with 1,500 discarded samples as burn-in. The result of 30 replicates is summarized in Table 2, from which we see that FNR, FDR and flip rates all decrease as p increases. Further, the method is considerably scalable as it completes 3,000 iterations within an hour even when p = 448.

Lastly, we generate X by assuming each e<sub>j</sub> in the structural equation models (2) has variance ω<sub>j</sub>; thus, the equal variance assumption is violated. We repeat the simulation study presented in the left column of Table 1 by sampling ω<sub>j</sub> independently from the uniform distribution on [0.7, 1.3] for each j, and we observe that the advantage of the proposed method is more significant; see Section C.2 in the supplementary material for the result. To further examine how the heterogeneity of error variances affects the performance of our method, we fix n = 500 and p = 40, and sample ω<sub>j</sub> from Uniform([1 − b, 1 + b]) for b = 0, 0.1, ..., 0.9. We plot the distribution of the HD metric over 30 replicates against b in Fig. 2. The proposed order MCMC sampler again performs uniformly better than competing algorithms. Besides, our method appears to be more robust, especially when b is not too large, which is probably due to the use of model averaging in Bayesian posterior inference.

### 4.3 Quantification of the bias caused by the equal variance assumption

When the true data generating process does not satisfy the equal variance assumption, our method is expected to have some bias. This is confirmed in Fig. 2, from which we see that HD increases with the heterogeneity of error variances. For comparison, we have also included in Fig. 2 the score-equivalent minimal I-MAP MCMC with score given by (16). Since this score does not encode the equal variance assumption, the minimal I-MAP MCMC sampler cannot determine the direction of an edge if reversing it yields another Markov equivalent


Table 3: Analysis of the posterior distributions for $p=7$. MINIMAP uses score (16), and thus it is score equivalent. The posterior inclusion probabilities of all edges are calculated exactly for both methods. The error variances are sampled from Uniform $([1-b, 1+b])$ or inverse-Gamma $(3,2)$. Each entry gives mean $\pm 1$ standard error.

DAG. This can be clearly seen from Fig. 2: the performance of the minimal I-MAP MCMC does not change significantly with the heterogeneity level $b$, and it always has HD away from zero. When the heterogeneity level $b=0.6$, which implies that the ratio between the maximum and minimum error variances can be as large as 4 , the minimal I-MAP MCMC has a comparable performance to our method, and when $b \geq 0.7$, the minimal I-MAP MCMC performs better.

In order to better quantify the bias of our method, we exactly calculate the matrix $\Gamma$ whose $(i, j)$-th element gives the posterior inclusion probability of the edge $i \rightarrow j$. We fix $p=7$ so that we can enumerate all possible orderings, and the exact posterior inclusion probabilities corresponding to scores (7) and (16) can be calculated as

$$
\Gamma_{i j}=\sum_{\sigma \in \mathbb{S}^{p}} \frac{e^{\phi\left(\hat{G}_{\sigma}\right)}}{\sum_{\sigma \in \mathbb{S}^{p}} e^{\phi\left(\hat{G}_{\sigma}\right)}} \mathbb{1}\left(\{i \rightarrow j\} \in \hat{G}_{\sigma}\right), \quad \Gamma_{i j}^{\mathrm{eq}}=\sum_{\sigma \in \mathbb{S}^{p}} \frac{e^{\phi_{\mathrm{eq}}\left(\hat{G}_{\sigma}^{\mathrm{M}}\right)}}{\sum_{\sigma \in \mathbb{S}^{p}} e^{\phi_{\mathrm{eq}}\left(\hat{G}_{\sigma}^{\mathrm{M}}\right)}} \mathbb{1}\left(\{i \rightarrow j\} \in \hat{G}_{\sigma}^{\mathrm{M}}\right)
$$

where $\hat{G}_{\sigma}$ and $\hat{G}_{\sigma}^{\mathrm{M}}$ are the estimated DAGs given an ordering $\sigma$ by our method and the minimal I-MAP method, respectively. We set $n=100 p$ and $p_{\text {edge }}=3 /(2 p-2)$, sample nonzero edge weights from Uniform $([-1,-0.3] \cup[0.3,1])$, and sample error variances from Uniform $([1-b, 1+b])$ and the inverse gamma distribution $\operatorname{IG}\left(a_{1}, a_{2}\right)$. We set $a_{1}=3$, which is the smallest integer that yields a finite variance, and set $a_{2}=2$ so that the expected value equals 1 . We generate 30 replicates for each simulation setting. In Table 3, we report three metrics, HD, Flip, and the Hamming distance for skeletons (SHD); recall that the skeleton of a DAG is the undirected graph obtained by undirecting all edges. SHD is consistently close to zero throughout the simulation settings, which implies that the true skeleton is correctly identified by both methods regardless of the heterogeneity level $b$. Notably, in all the settings considered, even when $b=0.9$ or in the inverse-gamma case, our method has a smaller flip rate than the minimal I-MAP method. That is, imposing the equal variance assumption does not increase the flip rate compared to a score-equivalent approach, which suggests that the computational gain resulting from this assumption is essentially obtained for free in this example.

# 5 Single-cell real data analysis 

We use a real data set from the single-cell RNA database for Alzheimer's disease, known as scREAD [Jiang et al., 2020], to illustrate the advantages of the proposed algorithm. We

![img-2.jpeg](img-2.jpeg)

Figure 3: Result of the proposed method for the real data analysis. Given $\dot{\Gamma}_{ij}^{\text{RB}}$, we infer the edge $i \rightarrow j$ exists in the DAG if $\dot{\Gamma}_{i j}^{\text{RB}}>c$ where $c$ is the cutoff of posterior inclusion probability. For each $c$, we count the number of edges occurring in the DAG for control samples (black), the number of edges in the DAG for case samples (red), the number of edges with edge direction ignored in both DAGs (green), and the number of directed edges in both DAGs (blue).

Only consider genes involved in the brain-derived neurotrophic factor signaling pathway and expressed in the layer 2–3 glutamatergic neurons. The goal is to learn two DAG models, one from case samples and the other from control samples, and then inspect how different the two DAGs are. To mitigate potential batch effects, we only use samples that are generated at similar sequencing depths by checking the total and median expression level across all genes for each sample cell, which results in $n_0 = 2300$ control samples and $n_1 = 1666$ case samples. Next, we select the genes in this pathway expressed in at least half of the samples in both data sets, which yields $p = 73$. The data matrices for both case and control samples are obtained by performing normalization of log-transformed expression levels [Lee, 2007, Chapter 6].

For each of the two data sets, we run the proposed order MCMC sampler with iterative top-down initialization for $2 \times 10^5$ MCMC iterations, and then discard the first $10^5$ iterations as burn-in. It only takes about 480 seconds for each data set. To infer the edge posterior inclusion probabilities, we use the conditioning scheme described in Section 3.3, and the result is presented in Fig. 3. The two DAGs learned from the data share a significant proportion of undirected edges, and more importantly, most of these edges have the same direction in both data sets: the gap between the blue and green lines in Fig. 3 is narrow. In other words, the orderings of the variables learned from the two data sets are very similar. The true ordering of the variables is hard to determine as there may even exist feedback loops among the selected genes, and we do not know to what extent the true model satisfies the equal variance assumption. But Fig. 3 suggests that the use of this score is very reasonable from a pragmatic perspective. For comparison, we have also tried the minimal I-MAP MCMC with the decomposable score given in (16), which represents a state-of-the-art score equivalent Bayesian structure learning procedure, and the result is shown in Section C.3 of the supplementary material. Given the same initialization and same number of MCMC and burn-in iterations, our method yields a higher proportion of shared directed edges than the minimal I-MAP MCMC. For example, with the posterior inclusion probability cutoff being

0.5 , for our method $41 \%$ of the edges in the inferred DAG for case samples also occur in the same direction in the DAG for control samples, while this ratio drops to $26 \%$ for the minimal I-MAP MCMC.

To provide further evidence for the advantage of the proposed structure learning method, we repeat the above analysis 30 times using both our sampler with non-decomposable score and the minimal I-MAP MCMC with decomposable score. Then, for each pair $(i, j)$ with $i \neq j$, we calculate the Gelman-Rubin scale factor [Gelman and Rubin, 1992] using $\Gamma_{i j}$, which is equal to 1 if $i \rightarrow j$ is in the sampled DAG and 0 otherwise. Thus, we get $p(p-1)$ GelmanRubin statistics for each data set, one for each directed edge. We find that $99.7 \%$ of the directed edges in the two DAGs have Gelman-Rubin statistics lower than 1.1 for our method, and $93.7 \%$ for the minimal I-MAP MCMC; we use the threshold 1.1 since this is the most common choice according to Vats and Knudson [2021]. Moreover, for the minimal I-MAP MCMC, Gelman-Rubin statistics of 90 directed edges yield infinity, which means that the within-chain variance of $\Gamma_{i j}$ is zero for all 30 runs, but the between-chain variance is nonzero; that is, in some runs the edge $i \rightarrow j$ is selected in every iteration excluding burn-in, while in the other runs the edge $i \rightarrow j$ is never selected. This observation again illustrates that for a score equivalent procedure, traversing equivalence classes can sometimes be very difficult and cause slow mixing of MCMC samplers. In contrast, the maximum Gelman-Rubin statistic for our method is 2.56 for the control data set and 1.26 for the case data set.

# Acknowledgement 

The authors would like to thank the anonymous reviewers for their comments which helped improve the paper, and thank Prof. Mohsen Pourahmadi and Yongjian Yang for helpful discussions. HC and QZ were supported in part by NSF grant DMS-2245591. All authors were supported by the Triads for Transformation Grant of Texas A\&M University.

# Supplementary material 

## A Algorithms

## A. 1 Overview of the proposed method

We outline the proposed order MCMC algorithm in Algorithm 3. For all displayed algorithms, we assume the data matrix $X$ and model parameters $\left(c_{0}, \gamma, \alpha, \kappa, d_{\text {in }}\right)$ are given. The R code for the proposed method and simulation studies can be found at https://github. com/hwchang1201/bayes.eqvar.

```
Algorithm 3: Bayesian order-based structure learning
    Input: Number of MCMC iterations \(T\), neighborhood function \(\mathcal{N}=\mathcal{N}_{\text {adj }}, \mathcal{N}_{\text {rtr }}\) or
        \(\mathcal{N}_{\text {rrs }}\), a DAG selection procedure \(\hat{G}: \mathbb{S}^{p} \rightarrow \mathcal{G}_{p}\) (e.g. Algorithm 5)
    \(1 \sigma^{(0)} \leftarrow \hat{\sigma}^{\mathrm{ITD}} / / \hat{\sigma}^{\mathrm{ITD}}\) is the output of Algorithm 2
    \(2 G^{(0)} \leftarrow \hat{G}\left(\sigma^{(0)}\right)\)
    for \(t=1, \ldots, T\) do
        Draw \(\sigma\) uniformly from \(\mathcal{N}\left(\sigma^{(t-1)}\right)\)
        Draw \(u \sim \operatorname{Uniform}(0,1)\)
        \(a \leftarrow \min \left(\pi_{n}(\sigma) / \pi_{n}\left(\sigma^{(t-1)}\right), 1\right)\)
        if \(u \leq a\) then
            \(\sigma^{(t)} \leftarrow \sigma\)
            \(G^{(t)} \leftarrow \hat{G}(\sigma)\)
        else
            \(\sigma^{(t)} \leftarrow \sigma^{(t-1)}\)
            \(G^{(t)} \leftarrow G^{(t-1)}\)
            \(\hat{\Gamma}^{(t)}=\hat{\Gamma}\left(\sigma^{(t)}, G^{(t)}\right) / /\) See (15) for the definition of \(\hat{\Gamma}\)
    Output: "Rao-Blackwellized" adjacency matrices \(\left\{\hat{\Gamma}^{(t)}\right\}_{t=1}^{T}\)
```


## A. 2 Forward-backward algorithms with non-decomposable scores

Recall the posterior score of a DAG given in (7). Define the nodewise score at node $j$ by

$$
\phi_{j}\left(S, \operatorname{RSS}_{. j}\right)=-|S| \log \left\{p^{\alpha_{j}} \sqrt{(1+\alpha / \gamma)}\right\}-\frac{\alpha p n+\kappa}{2} \log \left(\operatorname{RSS}_{. j}+X_{j}^{\mathrm{T}} \Phi_{S}^{\perp} X_{j}\right)
$$

for $S \subseteq P_{j}$, where $\mathrm{RSS}_{. j}$ denotes the total residual sum of squares of nodes other than $j$, and $P_{j}$ is the potential parent set defined in (1). Hence, given $\mathrm{RSS}_{. j}$, we can use the standard forward-backward stepwise algorithm to select the parent set of node $j$; this is described in Algorithm 4. We allow using two different estimates for $\mathrm{RSS}_{. j}$, one for the forward phase and the other for the backward phase; the reason will become clear in the next subsection.

## A. 3 Implementation of order MCMC with non-decomposable scores

For our model, the main computational challenge is that a local change to the ordering $\sigma$ can cause some global changes to the maximum a posteriori DAG estimator $\hat{G}_{\sigma}^{\mathrm{MAP}}$, due to

```
Algorithm 4: Nodewise forward-backward selection
    Input: Node index \(j \in[p]\), a set of potential parent nodes \(P_{j} \subset[p]\), two estimates
        for the total residual of sum of squares of other nodes \(\mathrm{RSS}_{. j}, \mathrm{RSS}_{. j}^{\prime}\)
    Forward phase: \(S_{\mathrm{f}} \leftarrow \emptyset\)
    for \(k=1, \ldots,\left|P_{j}\right|\) do
        \(\ell_{0} \leftarrow \arg \max _{\ell \in P_{j} \backslash S_{\mathrm{f}}} \phi_{j}\left(S_{\mathrm{f}} \cup\{\ell\}, \mathrm{RSS}_{. j}\right)\)
        \(\tilde{S}_{\mathrm{f}} \leftarrow S_{\mathrm{f}} \cup\left\{\ell_{0}\right\}\)
        if \(\phi_{j}\left(\tilde{S}_{\mathrm{f}}, \mathrm{RSS}_{. j}\right) \geq \phi_{j}\left(S_{\mathrm{f}}, \mathrm{RSS}_{. j}\right)\) then
            \(S_{\mathrm{f}} \leftarrow \tilde{S}_{\mathrm{f}}\)
        else
            break
    Backward phase: \(S_{\mathrm{b}} \leftarrow S_{\mathrm{f}}\)
    for \(k=1, \ldots,\left|S_{\mathrm{f}}\right|\) do
        \(\ell_{1} \leftarrow \arg \max _{\ell \in S_{\mathrm{b}}} \phi_{j}\left(S_{\mathrm{b}} \backslash\{\ell\}, \mathrm{RSS}_{. j}^{\prime}\right)\)
        \(\tilde{S}_{\mathrm{b}} \leftarrow S_{\mathrm{b}} \backslash\left\{\ell_{1}\right\}\)
        if \(\phi_{j}\left(\tilde{S}_{\mathrm{b}}, \mathrm{RSS}_{. j}^{\prime}\right) \geq \phi_{j}\left(S_{\mathrm{b}}, \mathrm{RSS}_{. j}^{\prime}\right)\) then
            \(S_{\mathrm{b}} \leftarrow \tilde{S}_{\mathrm{b}}\)
        else
            break
    Output: A parent set \(S_{\mathrm{b}}\) of node \(j\)
```

the use of the non-decomposable posterior score. Were the posterior score decomposable, whenever we use an adjacent transposition to move from $\sigma$ to $\sigma^{\prime}=\sigma \circ(i, i+1)_{c}$, we know that $\mathrm{Pa}_{j}\left(\hat{G}_{\sigma}^{\mathrm{MAP}}\right)=\mathrm{Pa}_{j}\left(\hat{G}_{\sigma}^{\mathrm{MAP}}\right)$ for any $j \notin\{\sigma(i), \sigma(i+1)\}$, since maximizing the score of the entire DAG is equivalent to maximizing the local score at each node separately.

We describe a strategy for implementing local moves on $\mathbb{S}^{p}$ for our model, which is as efficient as with a decomposable posterior score. We start by proving two monotone properties of the nodewise score defined in (17).
Lemma 1. Let $\phi_{j}$ be as given in (17), $S \subset[p] \backslash\{j\}, k \notin S \cup\{j\}$ and $a>0$.
(i) If $\phi_{j}(S \cup\{k\}, a)>\phi_{j}(S, a)$, then $\phi_{j}(S \cup\{k\}, b)>\phi_{j}(S, b)$ for any $0<b<a$.
(ii) If $\phi_{j}(S \cup\{k\}, a)<\phi_{j}(S, a)$, then $\phi_{j}(S \cup\{k\}, b)<\phi_{j}(S, b)$ for any $b>a$.

Proof. To simplify the notation, let $K_{0}=\log \left\{p^{\epsilon_{0}} \sqrt{(1+\alpha / \gamma)}\right\}$ and $K_{1}=(\alpha p n+\kappa) / 2$. A routine calculation shows that $\phi_{j}(S \cup\{k\}, a)>\phi_{j}(S, a)$ if and only if

$$
\log \frac{a+X_{j}^{\mathrm{T}} \Phi_{\frac{\epsilon}{S}} X_{j}}{a+X_{j}^{\mathrm{T}} \Phi_{\frac{\epsilon}{S \cup\{k\}} X_{j}}}>\frac{K_{0}}{K_{1}}
$$

The claim follows by observing that the left-hand side is monotonically decreasing in $a$.
Motivated by Lemma 1, we use the following procedure to find $\hat{G}_{\sigma}^{\mathrm{MAP}}$ for a given $\sigma \in \mathbb{S}^{p}$. First, for $j=1, \ldots, p$, we find a lower bound and an upper bound on $\mathrm{RSS}_{j}$ such that

```
Algorithm 5: Forward-backward DAG selection
    Input: \(\sigma \in \mathbb{S}^{p}\)
    \(G \leftarrow\) empty DAG
    // Forward phase
    while 1 do
        \(\left(i_{0}, j_{0}\right) \leftarrow \arg \max _{i, j: \sigma^{-1}(i)<\sigma^{-1}(j),(i \rightarrow j) \notin G} \phi(G \cup\{i \rightarrow j\})\)
        \(\hat{G} \leftarrow G \cup\left\{i_{0} \rightarrow j_{0}\right\}\)
        if \(\phi(\hat{G}) \geq \phi(G)\) then
            \(G \leftarrow \hat{G}\)
        else
            break
    // Backward phase
    while 1 do
        \(\left(i_{1}, j_{1}\right) \leftarrow \arg \max _{i, j:\{i \rightarrow j\} \in G} \phi(G \backslash\{i \rightarrow j\})\)
        \(\hat{G} \leftarrow G \backslash\left\{i_{1} \rightarrow j_{1}\right\}\)
        if \(\phi(\hat{G}) \geq \phi(G)\) then
            \(G \leftarrow \hat{G}\)
        else
            break
    Output: DAG \(G\)
```

both bounds do not depend on $\sigma$. An obvious choice for the upper bound on $\mathrm{RSS}_{j}$ is given by $\bar{\mu}_{j}=X_{j}^{\mathrm{T}} X_{j}$, and if $p<n$, a lower bound is given by $\underline{\mu}_{j}=X_{j}^{\mathrm{T}} \Phi_{[p]}^{i} \backslash\{j\} X_{j}$ (we assume $\underline{\mu}_{j}$ is strictly positive). Next, for $j=1, \ldots, p$, we apply Algorithm 4 with input $\left(j, P_{j}, \sum_{k \neq j} \underline{\mu}_{k}, \sum_{k \neq j} \bar{\mu}_{k}\right)$; that is, in the forward stage, we let the algorithm select as many parent nodes as possible by using minimum estimates for the residual sum of squares of other nodes, and in the backward stage, we let the algorithm remove as many nodes as possible. For all nodes, save the search paths of Algorithm 4, including the changes in residual sum of squares in each step, in the internal memory, and let $\bar{S}_{j}^{\sigma}$ denote the parent set of node $j$ at the end of the forward stage. Denote by $\bar{G}_{\sigma}$ the DAG such that $\mathrm{Pa}_{j}\left(\bar{G}_{\sigma}\right)=\bar{S}_{j}^{\sigma}$ for each $j$. Now to find $\hat{G}_{\sigma}^{\mathrm{MAP}}$, we simply apply the backward stage of Algorithm 5 by initializing the DAG to $\bar{G}_{\sigma}$. This can be done very efficiently by using the search paths of Algorithm 4; no calculation of residual sum of squares is needed.

The above procedure enables an efficient updating algorithm for finding $\hat{G}_{\sigma}^{\mathrm{MAP}}$ when we move locally on the ordering space $\mathbb{S}^{p}$. For example, consider moving from $\sigma$ to $\sigma^{\prime}=$ $\sigma \circ(i, i+1)_{c}$. We only need to apply Algorithm 4 at nodes $\sigma(i)$ and $\sigma(i+1)$, and then perform backward DAG selection using the saved search paths of nodewise forward-backward selection. The computational time of the DAG selection step is negligible compared to that of Algorithm 4. Note that the parent sets of nodes other than $\sigma(i)$ and $\sigma(i+1)$ may change.

# A. 4 Three random walk proposals 

Figure 4 describes (1) adjacent transposition, (2) random transposition, and (3) random-torandom shuffle, given the current topological ordering $\sigma$. The random transposition $\sigma \circ(i, j)_{c}$ interchanges the $i$-th and the $j$-th elements of $\sigma$ while keeping the others unchanged. The adjacent transposition is a special case of random transposition where $i$ and $j$ are adjacent, i.e., $|i-j|=1$. The random-to-random shuffle $\sigma \circ \xi(i, j)$ inserts the $i$-th element of $\sigma$ to the $j$-th position.
![img-3.jpeg](img-3.jpeg)

Figure 4: Illustration of the three proposals introduced in Section 3.1: adjacent transposition, the random transposition and the random-to-random shuffle.

## B Proofs

## B. 1 High-probability events

Recall that we assume the data is generated according to the linear structural equation model (SEM) given in (10). Since the rows of $X$ are assumed to be i.i.d. copies of $X$, we have

$$
X_{j}=\sum_{i=1}^{p}\left(B^{*}\right)_{i j} X_{i}+\epsilon_{j}, \text { where } \epsilon_{j} \sim N_{n}\left(0, \omega_{j}^{*} I\right), \text { for all } j \in[p]
$$

By Remark 3, for each $\sigma \in \mathbb{S}^{p}$, we can derive a linear SEM equivalent to (18), which is given by

$$
X_{j}=\sum_{i=1}^{p}\left(B_{\sigma}^{*}\right)_{i j} X_{i}+\epsilon_{j}^{\sigma}, \text { where } \epsilon_{j}^{\sigma} \sim N_{n}\left(0, \omega_{j}^{\sigma} I\right), \text { for all } j \in[p]
$$

We define the normalized error vectors by

$$
z_{j}=\left(\omega_{j}^{*}\right)^{-\frac{1}{2}} \epsilon_{j} \text { for } j \in[p], \quad z_{j}^{\sigma}=\left(\omega_{j}^{\sigma}\right)^{-\frac{1}{2}} \epsilon_{j}^{\sigma} \text { for } \sigma \in \mathbb{S}^{p}, j \in[p]
$$

where $z_{j}$ and $z_{j}^{\sigma}$ are associated with the true model given in (18) and the linear SEM in (19), respectively. The sets of the corresponding normalized errors are defined by $\mathcal{Z}_{0}=\left\{z_{j}: j \in\right.$

$[p]\}$ and $\mathcal{Z}_{1}=\left\{z_{j}^{\sigma}: \sigma \in \mathbb{S}^{p}, j \in[p]\right\}$. Clearly, $\mathcal{Z}_{0} \subseteq \mathcal{Z}_{1}$ and $\left|\mathcal{Z}_{0}\right|=p$. Further, one can show that

$$
\left|\mathcal{Z}_{1}\right| \leq p \cdot\binom{ p}{d^{*}}
$$

where $d^{*}$ is defined in (12).
Before we prove the results given in the main text, we first define some event sets on which the random components of our generating SEM behaves as desired, and use concentration inequalities to show that they happen with high probability. We will then prove the main results of the paper by conditioning on these high-probability events. Recall $P_{j}^{\sigma}$ defined in (1) and let $\mathcal{M}_{p}(d, P)=\{S \subseteq P:|S| \leq d\}$. Define

$$
\begin{gathered}
\mathcal{A}=\left\{n \underline{\nu} \leq \min _{S \subseteq \mathcal{M}_{p}\left(2 d_{\text {in }},[p]\right)} \lambda_{\min }\left(X_{S}^{\mathrm{T}} X_{S}\right) \leq \max _{S \subseteq \mathcal{M}_{p}\left(2 d_{\text {in }},[p]\right)} \lambda_{\max }\left(X_{S}^{\mathrm{T}} X_{S}\right) \leq n \bar{\nu}\right\} \\
\mathcal{B}=\left\{\min _{j \in[p]} \min _{S \subseteq \mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)}\left(z_{j}\right)^{\mathrm{T}} \Phi_{S}^{\perp} z_{j} \geq \frac{1}{2} n\right\} \\
\mathcal{B}^{\prime}=\left\{\min _{j \in[p], \sigma \in \mathbb{S}^{p}} \min _{S \subseteq \mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)}\left(z_{j}^{\sigma}\right)^{\mathrm{T}} \Phi_{S}^{\perp} z_{j}^{\sigma} \geq \frac{1}{2} n\right\} \\
\mathcal{C}=\left\{\max _{j \in[p]} \max _{k \notin S} z_{j}^{\mathrm{T}}\left(\Phi_{S \cup\{k\}}-\Phi_{S}\right) z_{j} \leq \rho \log p\right\} \\
\mathcal{D}=\left\{\min _{j \in[p], \sigma \in \mathbb{S}^{p}} \min _{S \subseteq \mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)}\left(z_{j}^{\sigma}\right)^{\mathrm{T}} \Phi_{S}^{\perp} z_{j}^{\sigma}>\left(1-\frac{1}{2 \eta}\right) n\right\} \\
\mathcal{E}=\left\{\max _{j \in[p]} \max _{S \subseteq \mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)} z_{j}^{\mathrm{T}} \Phi_{S}^{\perp} z_{j}<\left(1+\frac{1}{4 \eta}\right) n\right\} \\
\mathcal{J}=\bigcap_{i, j \in[p]}\left\{\left|\frac{X_{i}^{\mathrm{T}} X_{j}}{n}-\Sigma_{i j}^{*}\right| \leq 160 \bar{\nu} \sqrt{\frac{\log p}{n}}\right\}
\end{gathered}
$$

where $\eta, \rho>0$ are universal constants.
Lemma 2. Under the conditions of Proposition 1, we have $\mathbb{P}^{*}(\mathcal{A} \cap \mathcal{B} \cap \mathcal{C}) \geq 1-4 p^{-1}$ for sufficiently large $n$.

Proof. From Lemma F1 of Zhou and Chang [2021], we have $\mathbb{P}^{*}(\mathcal{A}) \geq 1-p^{-1}$ for sufficiently large $n$. The proof for the bounds of $\mathbb{P}^{*}(\mathcal{B})$ and $\mathbb{P}^{*}(\mathcal{C})$ is analogous to that of Lemma F2 of Zhou and Chang [2021]. A standard calculation using the tail bounds for chi-squared distributions [Laurent and Massart, 2000][Lemma 1] yields

$$
\begin{gathered}
\mathbb{P}^{*}\left\{z_{j}^{\mathrm{T}} \Phi_{S}^{\perp} z_{j} \leq \frac{1}{2} n\right\} \leq e^{-n / 48} \\
\mathbb{P}^{*}\left\{z_{j}^{\mathrm{T}}\left(\Phi_{T \cup\{k\}}-\Phi_{T}\right) z_{j} \geq \rho \log p\right\} \leq 2 e^{-\rho \log p / 2}
\end{gathered}
$$

for any $j \in[p], S \subseteq \mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)$ and $T \cup\{k\} \subseteq \mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)$. To conclude the proof, apply union bounds with the observations $\left|\mathcal{Z}_{0}\right| \leq p$ and $\left|\mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)\right\}| \leq p^{2 d_{\text {in }}+1}$ and the assumptions $d_{\text {in }} \log p=o(n)$ and $\rho>4 d_{\text {in }}+6$.

Lemma 3. Assume $d_{\text {in }} \log p=o(n)$ and $d^{*} \leq d_{\text {in }}$. There exists some universal constant $c^{\prime}=c^{\prime}(\eta)>0$ such that $\mathbb{P}^{*}(\mathcal{D} \cap \mathcal{E}) \geq 1-2 e^{-c^{\prime} n}$ for all sufficiently large $n$.

Proof. By Lemma 1 of Laurent and Massart [2000],

$$
\mathbb{P}^{*}\left\{\frac{\chi_{d}^{2}}{d} \leq 1-a\right\} \leq e^{-a^{2} d / 4}, \quad \mathbb{P}^{*}\left\{\frac{\chi_{d}^{2}}{d} \geq 1+a+\frac{a^{2}}{2}\right\} \leq e^{-a^{2} d / 4}
$$

where $\chi_{d}^{2}$ denotes a chi-squared random variable with $d$ degrees of freedom and $a>0$ is arbitrary. Consider $\mathbb{P}^{*}(\mathcal{D})$ first. For any $j \in[p], \sigma \in \mathbb{S}^{p}$, and $S \in \mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma}\right)$, by (20),

$$
\mathbb{P}^{*}\left\{\frac{\left(z_{j}^{\sigma}\right)^{\mathrm{T}} \Phi_{S}^{\perp} z_{j}^{\sigma}}{n-|S|} \leq 1-\frac{1}{4 \eta}\right\} \leq \exp \left(-\frac{n-|S|}{64 \eta^{2}}\right)
$$

Since $|S| \leq 2 d_{\text {in }}=o(n / \log p), n(n-|S|)^{-1}\left(1-(2 \eta)^{-1}\right) \leq 1-(4 \eta)^{-1}$ for sufficiently large $n$. Applying the union bound with $\left|\mathcal{Z}_{1}\right| \leq p^{d_{\text {in }}+1}$ and $\left|\mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma}\right)\right| \leq p^{2 d_{\text {in }}+1}$, we obtain

$$
\mathbb{P}^{*}\left(\mathcal{D}^{\mathrm{c}}\right) \leq p^{3 d_{\text {in }}+2} \exp \left(-\frac{n}{128 \eta^{2}}\right) \leq e^{-c^{\prime} n}
$$

for sufficiently large $n$. Next, consider $\mathbb{P}^{*}(\mathcal{E})$. For any $j \in[p]$ and $S \in \mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)$, we have

$$
\mathbb{P}^{*}\left\{\frac{z_{j}^{\mathrm{T}} \Phi_{S}^{\perp} z_{j}}{n-|S|} \geq 1+\frac{1}{8 \eta}+\frac{1}{128 \eta^{2}}\right\} \leq \exp \left(-\frac{n-|S|}{256 \eta^{2}}\right)
$$

by (20). Since $\left|\mathcal{Z}_{0}\right|=p$ and $\left|\mathcal{M}_{p}\left(2 d_{\text {in }}, P_{j}^{\sigma^{*}}\right)\right| \leq p^{2 d_{\text {in }}+1}$, the union bound gives

$$
\mathbb{P}^{*}\left(\mathcal{E}^{\mathrm{c}}\right) \leq p^{2 d_{\text {in }}+2} \exp \left(-\frac{n}{512 \eta^{2}}\right) \leq e^{-c^{\prime} n}
$$

Another application of the union bound yields the conclusion.
Lemma 4. Under the conditions of Proposition 2, we have $\mathbb{P}^{*}\left(\mathcal{A} \cap \mathcal{B}^{\prime} \cap \mathcal{J}\right) \geq 1-6 p^{-1}$ for all sufficiently large $n$.

Proof. We have obtained the bound $\mathbb{P}^{*}(\mathcal{A}) \geq 1-p^{-1}$ from Lemma 2, and the bound on $\mathbb{P}^{*}\left(\mathcal{B}^{\prime}\right)$ is proved in Lemma F2 of Zhou and Chang [2021]. Consider $\mathbb{P}^{*}\left(\mathcal{J}^{\mathrm{c}}\right)$. Let

$$
\mathcal{J}_{i j}^{\mathrm{c}}=\left\{\left|\frac{X_{i}^{\mathrm{T}} X_{j}}{n}-\Sigma_{i j}^{*}\right|>160 \bar{\nu} \sqrt{\frac{\log p}{n}}\right\}
$$

By Ravikumar et al. [2011, Lemma 1],

$$
\mathbb{P}^{*}\left(\mathcal{J}_{i j}^{\mathrm{c}}\right) \leq 4 \exp \left(-3 \bar{\nu}^{2} \log p /\left(\max _{i} \Sigma_{i i}^{*}\right)^{2}\right) \leq 4 p^{-3}
$$

from which we obtain $\mathbb{P}^{*}\left(\mathcal{J}^{\mathrm{c}}\right)=\mathbb{P}^{*}\left(\cup_{i, j \in[p]} \mathcal{J}_{i j}^{\mathrm{c}}\right) \leq 4 p^{-1}$ by the union bound.

# B. 2 Proof of Proposition 1 

We consider the proof of consistency for the estimator $\hat{G}_{j}^{\text {MAP }}$ defined in (9); that is, we show that the scoring criterion $\phi$ is consistent when the ordering $\sigma$ is known. We first prove a technical lemma, which bounds the residual sum of squares $\operatorname{RSS}_{j}(G)$ when the node $j$ is underfitted (i.e., $\left.\operatorname{Pa}_{j}\left(G^{*}\right) \not \subset \operatorname{Pa}_{j}(G)\right)$.
Lemma 5. Fix some $S \subseteq[p]$ such that $|S| \leq d_{\text {in }}$ and $S \neq S^{*}=\operatorname{Pa}_{j}\left(G^{*}\right)$. Suppose we are on the event $\mathcal{A} \cap \mathcal{B} \cap \mathcal{C}$ and the conditions of Proposition 1 hold. Then

$$
X_{j}^{\mathrm{T}}\left(\Phi_{S \cup\left\{k_{0}\right\}}-\Phi_{S}\right) X_{j} \geq 9 c_{0} \bar{\nu} \log p / \alpha
$$

for some $k_{0} \in S^{*} \backslash S$.
Proof. We denote $X_{j}=Z_{j}+\epsilon_{j}, Z_{j}=X_{S^{*}}\left(B_{j}^{*}\right)_{S^{*}}$, where $B_{j}^{*}$ is $j$-th column of the true weighted adjacency matrix $B^{*}$. Let $k_{0}=\arg \max _{k \in S^{*} \backslash S} Z_{j}^{\mathrm{T}}\left(\Phi_{S \cup\{k\}}-\Phi_{S}\right) Z_{j}$. By the triangle inequality,

$$
X_{j}^{\mathrm{T}}\left(\Phi_{S \cup\left\{k_{0}\right\}}-\Phi_{S}\right) X_{j} \geq\left(\left\|\left(\Phi_{S \cup\left\{k_{0}\right\}}-\Phi_{S}\right) Z_{j}\right\|-\left\|\left(\Phi_{S \cup\left\{k_{0}\right\}}-\Phi_{S}\right) \epsilon_{j}\right\|\right)^{2}
$$

On the event set $\mathcal{C}$, we can use $c_{0}>\alpha \rho$ from condition (C2) to obtain that

$$
\left\|\left(\Phi_{S \cup\left\{k_{0}\right\}}-\Phi_{S}\right) \epsilon_{j}\right\|^{2} \leq \rho \omega_{j}^{*} \log p \leq \rho \bar{\nu} \log p<\frac{c_{0}}{\alpha} \bar{\nu} \log p
$$

and thus by Lemma E2 of Zhou and Chang [2021],

$$
\left\|\left(\Phi_{S \cup\left\{k_{0}\right\}}-\Phi_{S}\right) Z_{j}\right\|^{2} \geq \frac{\left\|B_{S^{*} \backslash S}^{*}\right\|^{2}}{\left|S^{*} \backslash S\right|} \frac{n \nu^{2}}{\bar{\nu}} \geq 16 c_{0} \frac{\bar{\nu}^{2} \log p}{\alpha \nu^{2} n} \frac{n \nu^{2}}{\bar{\nu}} \geq \frac{16 c_{0}}{\alpha} \bar{\nu} \log p
$$

The second inequality follows from condition (C3). Plugging the above two displayed bounds into (21), we obtain the asserted result.

Proof of Proposition 1. On the event $\mathcal{A} \cap \mathcal{B} \cap \mathcal{C}$ defined in Section B.1, we will show that all the three events stated in the proposition happen. For a non-negative integer $d$, define

$$
\mathcal{G}_{p}^{*}(d)=\bigcup_{\sigma \in\left[\sigma^{*}\right]} \mathcal{G}_{p}^{\sigma}(d)
$$

Event (i). Fix an arbitrary $G \in \mathcal{G}_{p}^{*}\left(2 d_{\text {in }}\right)$ such that $\operatorname{Pa}_{j}\left(G^{*}\right) \subset \operatorname{Pa}_{j}(G)$ for some $j \in[p]$. We prove that we can remove all the redundant parents of node $j$. This is slightly stronger than the asserted result, but it will be useful later for proving the claim for event (iii). Pick an arbitrary $k \in \operatorname{Pa}_{j}(G) \backslash \operatorname{Pa}_{j}\left(G^{*}\right)$ and define $G^{\prime}=G \backslash\{k \rightarrow j\}$. On the event $\mathcal{B} \cap \mathcal{C}$, we have

$$
\begin{gathered}
X_{j}^{\mathrm{T}}\left(\Phi_{\operatorname{Pa}_{j}\left(G^{\prime}\right)}^{\perp}-\Phi_{\operatorname{Pa}_{j}(G)}^{\perp}\right) X_{j}=\epsilon_{j}^{\mathrm{T}}\left(\Phi_{\operatorname{Pa}_{j}(G)}-\Phi_{\operatorname{Pa}_{j}\left(G^{\prime}\right)}\right) \epsilon_{j} \leq \omega_{j}^{*} \rho \log p \\
\operatorname{RSS}_{i}(G)=X_{i}^{\mathrm{T}} \Phi_{\operatorname{Pa}_{i}(G)}^{\perp} X_{i} \geq \epsilon_{i}^{\mathrm{T}} \Phi_{\operatorname{Pa}_{i}(G)}^{\perp} \epsilon_{i} \geq \frac{n \omega_{i}^{*}}{2} \text { for } i \in[p]
\end{gathered}
$$

Since $1+x \leq \exp (x)$ for $x \in \mathbb{R}$ and $\sqrt{1+\alpha / \gamma}>1$, we find that

$$
\begin{aligned}
\frac{\exp (\phi(G))}{\exp \left(\phi\left(G^{\prime}\right)\right)} & =\left(p^{c_{0}} \sqrt{1+\alpha / \gamma}\right)^{-1}\left(\frac{\sum_{i \neq j}^{p} \operatorname{RSS}_{i}(G)+\operatorname{RSS}_{j}\left(G^{\prime}\right)}{\sum_{i=1}^{p} \operatorname{RSS}_{i}(G)}\right)^{\frac{\alpha p n+\kappa}{2}} \\
& <p^{-c_{0}}\left(1+\frac{X_{j}^{\mathrm{T}}\left(\Phi_{\mathrm{Pa}_{j}\left(G^{\prime}\right)}^{\perp}-\Phi_{\mathrm{Pa}_{j}(G)}^{\perp}\right) X_{j}}{\sum_{i=1}^{p} \operatorname{RSS}_{i}(G)}\right)^{\frac{\alpha p n+\kappa}{2}} \\
& \leq p^{-c_{0}} \exp \left(\frac{\alpha n p+\kappa}{2} \frac{X_{j}^{\mathrm{T}}\left(\Phi_{\mathrm{Pa}_{j}\left(G^{\prime}\right)}^{\perp}-\Phi_{\mathrm{Pa}_{j}(G)}^{\perp}\right) X_{j}}{\sum_{i=1}^{p} \operatorname{RSS}_{i}(G)}\right) \\
& \leq p^{-c_{0}} \exp \left\{\frac{(\alpha n p+\kappa) \omega_{j}^{*} \rho \log p}{\left(\min _{i} \omega_{i}^{*}\right) n p}\right\} \\
& \leq p^{\left\{\max _{i \neq j}\left(\omega_{j}^{*} / \omega_{i}^{*}\right)\right\}(\alpha+1) \rho-c_{0}}<1
\end{aligned}
$$

In the last line, we have used $\kappa \leq n p$ and $c_{0}>\max _{i \neq j}\left(\omega_{j}^{*} / \omega_{i}^{*}\right)(\alpha+1) \rho$ from condition (C2). The same argument implies that if we define $G_{0}$ such that $\mathrm{Pa}_{j}\left(G_{0}\right)=\mathrm{Pa}_{j}\left(G^{*}\right)$ and $\mathrm{Pa}_{i}\left(G_{0}\right)=\mathrm{Pa}_{i}(G)$ for $i \neq j$, then we have

$$
\frac{\exp (\phi(G))}{\exp \left(\phi\left(G_{0}\right)\right)}<p^{\left(\left|\mathrm{Pa}_{j}(G)\right|-\left|\mathrm{Pa}_{j}\left(G^{*}\right)\right|\right)\left\{\max _{i \neq j}\left(\omega_{j}^{*} / \omega_{i}^{*}\right)(\alpha+1) \rho-c_{0}\right\}}<1
$$

Event (ii). Fix an arbitrary $G \in \mathcal{G}_{p}^{*}\left(d_{\text {in }}\right)$ such that $\mathrm{Pa}_{j}\left(G^{*}\right) \nsubseteq \mathrm{Pa}_{j}(G)$ for some $j \in[p]$. Since there exists some $\sigma \in\left[\sigma^{*}\right]$ such that $G, G^{*} \in \mathcal{G}_{p}^{\sigma}\left(d_{\text {in }}\right)$, we can apply Lemma 5 to show that there exists some $k \in \mathrm{~Pa}_{j}\left(G^{*}\right) \backslash \mathrm{Pa}_{j}(G)$ such that the $\mathrm{DAG} G^{\prime}=G \cup\{k \rightarrow j\}$ satisfies $X_{j}^{\mathrm{T}}\left(\Phi_{\mathrm{Pa}_{j}\left(G^{\prime}\right)}-\Phi_{\mathrm{Pa}_{j}(G)}\right) X_{j} \geq 9 c_{0} \bar{\nu} \log p / \alpha$. Further, on the event $\mathcal{A}$, we have $\operatorname{RSS}_{i}(G) \leq$ $X_{i}^{\mathrm{T}} X_{i} \leq n \bar{\nu}$. Now using $\sqrt{1+\alpha / \gamma} \leq p$, which follows from condition (C2), we find that

$$
\begin{aligned}
\frac{\exp (\phi(G))}{\exp \left(\phi\left(G^{\prime}\right)\right)} & =\left(p^{c_{0}} \sqrt{1+\alpha / \gamma}\right)\left(\frac{\sum_{i \neq j}^{p} \operatorname{RSS}_{i}(G)+\operatorname{RSS}_{j}\left(G^{\prime}\right)}{\sum_{i=1}^{p} \operatorname{RSS}_{i}(G)}\right)^{\frac{\alpha p n+\kappa}{2}} \\
& \leq p^{\left(c_{0}+1\right)}\left(1-\frac{X_{j}^{\mathrm{T}}\left(\Phi_{\mathrm{Pa}_{j}(G)}^{\perp}-\Phi_{\mathrm{Pa}_{j}\left(G^{\prime}\right)}^{\perp}\right) X_{j}}{\sum_{i=1}^{p} \operatorname{RSS}_{i}(G)}\right)^{\frac{\alpha p n+\kappa}{2}} \\
& \leq p^{\left(c_{0}+1\right)} \exp \left(-\frac{\alpha n p+\kappa}{2} \frac{X_{j}^{\mathrm{T}}\left(\Phi_{\mathrm{Pa}_{j}\left(G^{\prime}\right)}-\Phi_{\mathrm{Pa}_{j}(G)}\right) X_{j}}{\sum_{i=1}^{p} \operatorname{RSS}_{i}(G)}\right) \\
& \leq p^{\left(c_{0}+1\right)} \exp \left\{-\frac{\alpha n p+\kappa}{2} \frac{9 c_{0} \bar{\nu} \log p / \alpha}{n p \bar{\nu}}\right\} \leq p^{\left(-7 c_{0} / 2+1\right)}
\end{aligned}
$$

This implies $\exp (\phi(G))<\exp \left(\phi\left(G^{\prime}\right)\right)$ since $c_{0}>4 d_{\text {in }}+6>2 / 7$. The same argument shows that if we define $G_{1} \in \mathcal{G}_{p}^{\sigma}$ such that $\mathrm{Pa}_{j}\left(G_{1}\right)=\mathrm{Pa}_{j}\left(G^{*}\right) \cup \mathrm{Pa}_{j}(G)$ and $\mathrm{Pa}_{i}\left(G_{1}\right)=\mathrm{Pa}_{i}(G)$ for $i \neq j$, then we have

$$
\frac{\exp (\phi(G))}{\exp \left(\phi\left(G_{1}\right)\right)} \leq p^{\left|\mathrm{Pa}_{j}\left(G^{*}\right) \backslash \mathrm{Pa}_{j}(G)\right|\left(-7 c_{0} / 2+1\right)}
$$

Event (iii). Consider an arbitrary $G \in \mathcal{G}_{p}^{*}\left(d_{\text {in }}\right)$ such that $G \neq G^{*}$. Then, there exists some $j \in[p]$ such that $\mathrm{Pa}_{j}(G) \neq \mathrm{Pa}_{j}\left(G^{*}\right)$. If the node $j$ is overfitted (i.e., $\mathrm{Pa}_{j}\left(G^{*}\right) \subset \mathrm{Pa}_{j}(G)$ ), event (i) shows that there exists some $G_{0} \in \mathcal{G}_{p}^{*}\left(d_{\text {in }}\right)$ such that $\phi\left(G_{0}\right)>\phi(G)$. If the node $j$ is underfitted, i.e., $\mathrm{Pa}_{j}\left(G^{*}\right) \nsubseteq \mathrm{Pa}_{j}(G)$, inequality (22) shows that there exists some $G_{1} \in$

$\mathcal{G}_{p}^{*}\left(2 d_{\text {in }}\right)$ such that $\phi\left(G_{1}\right)>\phi(G)$ and node $j$ is overfitted. But event (i) again implies that there exists some $G_{2} \in \mathcal{G}_{p}^{*}\left(d_{\text {in }}\right)$ such that $\phi\left(G_{2}\right)>\phi\left(G_{1}\right)$. Hence, $G$ cannot be the maximizer of $\phi$ in $\mathcal{G}_{p}^{*}\left(d_{\text {in }}\right)$; that is, $G^{*}$ is the unique DAG in $\mathcal{G}_{p}^{*}\left(d_{\text {in }}\right)$ that maximizes $\phi$, which completes the proof.

# B. 3 Proof of Theorem 1 

For $\tau \notin\left[\sigma^{*}\right]$, the ratio of $\exp \left(\phi\left(\hat{G}_{\tau}\right)\right)$ to $\exp \left(\phi\left(G^{*}\right)\right)$ is

$$
\frac{\exp \left(\phi\left(\hat{G}_{\tau}\right)\right)}{\exp \left(\phi\left(G^{*}\right)\right)}=\left(p^{\epsilon_{0}} \sqrt{1+\alpha / \gamma}\right)^{\left|G^{*}\right|-\left|\hat{G}_{\tau}\right|}\left(\frac{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(\hat{G}_{\tau}\right)}{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(G^{*}\right)}\right)^{-\frac{\alpha p n+\kappa}{2}}
$$

On the event $\mathcal{D} \cap \mathcal{E}$ defined in Section B.1, we have

$$
\begin{aligned}
\frac{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(\hat{G}_{\tau}\right)}{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(G^{*}\right)} & \geq \frac{\sum_{j=1}^{p} X_{j}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}\left(\hat{G}_{\tau}\right) \cup \mathrm{Pa}_{j}\left(G_{\tau}^{*}\right)}^{\perp} X_{j}}{\sum_{j=1}^{p} X_{j}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}\left(G^{*}\right)}^{\perp} X_{j}} \\
& =\frac{\sum_{j=1}^{p}\left(\epsilon_{j}^{\tau}\right)^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}\left(\hat{G}_{\tau}\right) \cup \mathrm{Pa}_{j}\left(G_{\tau}^{*}\right)}^{\perp} \epsilon_{j}^{\tau}}{\sum_{j=1}^{p} \epsilon_{j}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}\left(G^{*}\right)}^{\perp} \epsilon_{j}} \\
& \geq \frac{\operatorname{tr}\left(\Omega_{\tau}^{*}\right)}{\operatorname{tr}\left(\Omega_{\sigma^{*}}^{*}\right)} \cdot \frac{(1-1 /(2 \eta))}{1+1 /(4 \eta)}
\end{aligned}
$$

where the error vectors $\epsilon_{j}, \epsilon_{j}^{\tau}$ are as defined in (18) and (19). Without loss of generality, we can assume $\eta>3$ in Assumption A, from which we obtain that

$$
\frac{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(\hat{G}_{\tau}\right)}{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(G^{*}\right)} \geq \frac{(1+1 / \eta)(1-1 /(2 \eta))}{1+1 /(4 \eta)}>\frac{1+1 /(3 \eta)}{1+1 /(4 \eta)}>1+\frac{1}{\eta^{\prime}}
$$

for some universal $\eta^{\prime}>0$. Hence,

$$
\frac{\exp \left(\phi\left(\hat{G}_{\tau}\right)\right)}{\exp \left(\phi\left(G^{*}\right)\right)} \leq p^{\epsilon_{0}\left|G^{*}\right|}\left(1+\frac{1}{\eta^{\prime}}\right)^{-\frac{\alpha p n+\kappa}{2}} \leq p^{\epsilon_{0} p d_{\text {in }}}\left(1+\frac{1}{\eta^{\prime}}\right)^{-\frac{\alpha p n+\kappa}{2}}
$$

Using $d_{\text {in }} \log p=o(n)$ and Stirling's formula, we get

$$
\frac{\sum_{\tau \notin\left[\sigma^{*}\right]} \exp \left(\phi\left(\hat{G}_{\tau}\right)\right)}{\exp \left(\phi\left(G^{*}\right)\right)} \leq p!\frac{\exp \left(\phi\left(\hat{G}_{\tau}\right)\right)}{\exp \left(\phi\left(G^{*}\right)\right)} \leq e^{-C n p}
$$

for some universal $C>0$. For sufficiently large $n$, by Assumption B and Lemma 3, the event $\mathcal{D} \cap \mathcal{E} \cap\left(\cap_{\sigma \in\left[\sigma^{*}\right]}\left\{\hat{G}_{\sigma}=G^{*}\right\}\right)$ happens with probability at least $1-\zeta(p)-2 e^{-c^{\epsilon} n}$, on which we have

$$
\pi_{n}\left(G^{*}\right)=\frac{\sum_{\sigma \in\left[\sigma^{*}\right]} e^{\phi\left(G^{*}\right)}}{\sum_{\tau \in \mathbb{S}^{p}} e^{\phi\left(\hat{G}_{\tau}\right)}} \geq 1-\frac{\sum_{\tau \notin\left[\sigma^{*}\right]} e^{\phi\left(\hat{G}_{\tau}\right)}}{\sum_{\sigma \in\left[\sigma^{*}\right]} e^{\phi\left(G^{*}\right)}} \geq 1-e^{-C n p}
$$

That is, $\pi_{n}\left(G^{*}\right)$ converges to 1 in probability.

# B. 4 Proof for the case of sub-Gaussian errors 

Let $X$ be an $n \times p$ random matrix, each of whose rows is an i.i.d. copy of $p$-dimensional sub-Gaussian random vector with mean zero and covariance matrix $\Sigma^{*}$ with a sub-Gaussian parameter bounded by a universal constant $C_{\text {sub }}$. We define $\Sigma_{S}^{*}$ as the submatrix of $\Sigma^{*}$ with both rows and columns indexed by the set $S$. Let $\Sigma_{j \mid S}^{*}=\Sigma_{j, j}^{*}-\Sigma_{j, S}^{*}\left(\Sigma_{S}^{*}\right)^{-1} \Sigma_{S, j}^{*}$ denote the partial covariance and let $\hat{\Sigma}_{j \mid S}=n^{-1} X_{j} \Phi_{S}^{\perp} X_{j}$ be its estimator for $|S| \leq d_{\text {in }}$ and $j \notin S$. Denote $\|\cdot\|_{\text {op }}$ as the operator norm.

In the sub-Gaussian case, zero correlation does not imply independence anymore, and thus we need more stringent assumptions. The first condition is that

$$
\frac{\bar{\nu}^{4} d_{\mathrm{in}} \log p}{\underline{\nu}^{6} n} \rightarrow 0
$$

as $n$ goes to infinity. Second, we need $\operatorname{Pa}_{j}\left(\hat{G}_{\tau}\right) \subseteq \operatorname{Pa}_{j}\left(G_{\tau}^{*}\right)$ for $\tau \notin\left[\sigma^{*}\right]$, which means that the stepwise selection method should estimate the minimal I-map $G_{\tau}^{*}$ sparser and should not include an edge that is not in $G_{\tau}^{*}$. For the consistency result, the ratio $\hat{\Sigma}_{j \mid S} / \Sigma_{j \mid S}^{*}$ need to be controlled. To this end, we need the following lemmas.
Lemma 6. Suppose $d_{\text {in }} \log p=o(n)$. There exists a constant $K_{0}$, which only depend on $C_{\text {sub }}$, satisfying for sufficiently large $n$,

$$
\max _{S \in \mathcal{M}_{p}\left(2 d_{\text {in }},[p]\right)}\left\|n^{-1} X_{S}^{\top} X_{S}-\Sigma_{S}^{*}\right\|_{\mathrm{op}} \leq K_{0} \sqrt{\frac{d_{\text {in }} \log p}{n}}
$$

with probability at least $1-2 p^{-d_{\text {in }}}$.
Proof. See Lemma F3 in Zhou and Chang [2021].
Lemma 7. Suppose $d_{\text {in }} \log p=o(n)$ and a set $S$ and $j$ satisfy $|S| \leq d_{\text {in }}$ and $j \notin S$. Let $K_{0}$ be the constant in Lemma 6. Then, for sufficiently large $n$, we have

$$
\left|\hat{\Sigma}_{j \mid S}-\Sigma_{j \mid S}^{*}\right| \leq K_{0} \frac{\bar{\nu}^{2}}{\underline{\nu}^{2}} \sqrt{\frac{d_{\text {in }} \log p}{n}}
$$

with probability at least $1-2 p^{-d_{\text {in }}}$.
Proof. Apply the proof of Lemma E4 of Zhou and Chang [2021] by setting $T=\{j\}$, where $T$ is a set defined in Lemma E4 of Zhou and Chang [2021].

Now, we are ready to prove the sub-Gaussian case. It is sufficient to show

$$
\frac{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(\hat{G}_{\tau}\right)}{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(G^{*}\right)}>1+\frac{1}{\eta^{\prime}}
$$

For fixed $\eta>0$, by the condition (24), a sufficiently large $n$ satisfies $K_{0}\left(\bar{\nu}^{2} / \underline{\nu}^{2}\right) \sqrt{d_{\text {in }} \log p / n}$ $<\underline{\nu} /(4 \eta)$. It follows that

$$
\begin{aligned}
\hat{\Sigma}_{j \mid S} & >\Sigma_{j \mid S}^{*}-K_{0} \frac{\bar{\nu}^{2}}{\underline{\nu}^{2}} \sqrt{\frac{d_{\text {in }} \log p}{n}} \\
& >\Sigma_{j \mid S}^{*}-\frac{\underline{\nu}}{2 \eta}
\end{aligned}
$$

which implies that $\hat{\Sigma}_{j \mid S} / \Sigma_{j \mid S}^{*}>1-(2 \eta)^{-1}$ by the fact $\underline{\nu} \leq \Sigma_{j \mid S}^{*}$. The other direction can be obtained by

$$
\begin{aligned}
\hat{\Sigma}_{j \mid S} & <\Sigma_{j \mid S}^{*}+K_{0} \frac{\bar{\nu}^{2}}{\underline{\nu}^{2}} \sqrt{\frac{d_{\mathrm{in}} \log p}{n}} \\
& <\Sigma_{j \mid S}^{*}+\frac{\underline{\nu}}{4 \eta}
\end{aligned}
$$

which yields $\hat{\Sigma}_{j \mid S} / \Sigma_{j \mid S}^{*}<1+(4 \eta)^{-1}$. Therefore,

$$
\begin{aligned}
\frac{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(\hat{G}_{\tau}\right)}{\sum_{j=1}^{p} \operatorname{RSS}_{j}\left(G^{*}\right)} & \geq \frac{\sum_{j=1}^{p} X_{j}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}\left(G_{\tau}^{*}\right)}^{\perp} X_{j}}{\sum_{j=1}^{p} X_{j}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}\left(G^{*}\right)}^{\perp} X_{j}} \\
& =\frac{\sum_{j=1}^{p} \hat{\Sigma}_{j \mid \mathrm{Pa}_{j}\left(G_{\tau}^{*}\right)}}{\sum_{j=1}^{p} \hat{\Sigma}_{j \mid \mathrm{Pa}_{j}\left(G^{*}\right)}} \\
& \geq \frac{\operatorname{tr}\left(\Omega_{\tau}^{*}\right)}{\operatorname{tr}\left(\Omega_{\sigma^{*}}^{*}\right)} \cdot \frac{(1-1 /(2 \eta))}{1+1 /(4 \eta)} \\
& \geq \frac{(1+1 / \eta)(1-1 /(2 \eta))}{1+1 /(4 \eta)}>1+\frac{1}{\eta^{\prime}}
\end{aligned}
$$

for some universal constant $\eta^{\prime}>0$. The rest of the proof is identical to the Gaussian case.

# B. 5 Proof of Proposition 2 

By $\left(C 1^{\prime}\right)$, we have $\omega_{1}^{*}=\cdots=\omega_{p}^{*}=\omega^{*}$ in (18) for the true data generating model. Without loss of generality, assume that id $=(1, \ldots, p)$ is a true ordering. Define

$$
\theta=d_{\mathrm{in}}^{2} \frac{\bar{\nu}^{2} \log p}{\underline{\nu}^{3} n}
$$

Lemma 8. Under the setting of Proposition 2,

$$
\Sigma_{i i}^{*}=\omega^{*}+O\left(\theta / d_{\mathrm{in}}\right), \quad \Sigma_{i j}^{*}=O\left(\sqrt{\theta} / d_{\mathrm{in}}\right)
$$

for all $i, j \in[p]$ and $i \neq j$.
Proof. For ease of notation, in this proof we write $B=B^{*}$, and without loss of generality, we assume the true error variance $\omega^{*}$ equals 1 . Since $B$ is a strictly upper triangular matrix, its operator norm is zero and $B^{p}=0$. So we can expand $\Sigma$ using the Neumann series by

$$
\begin{aligned}
\Sigma=\left(I-B^{\mathrm{T}}\right)^{-1}(I-B)^{-1} & =\sum_{k=0}^{\infty}\left(B^{\mathrm{T}}\right)^{k} \sum_{k=0}^{\infty} B^{k} \\
=\sum_{k=0}^{\infty} \sum_{r+s=k}\left(B^{\mathrm{T}}\right)^{r} B^{s} & =\sum_{k=0}^{2 p-2} \sum_{\substack{r+s=k \\
r, s<p}}\left(B^{\mathrm{T}}\right)^{r} B^{s}
\end{aligned}
$$

We can calculate $B^{s}$ and $\left(B^{\mathrm{T}}\right)^{r}$ by treating $B^{*}$ and $\left(B^{*}\right)^{\mathrm{T}}$ as weighted transition matrices for a random walk on the DAG with weighted adjacency matrix $B$. Explicitly, define the set of all paths from node $i$ to node $j$ with $s$ steps by

$$
\operatorname{PATH}_{i j}^{s}=\left\{q=\left(q_{0}, q_{1}, \ldots, q_{s}\right): B_{q_{k} q_{k+1}} \neq 0, \text { for } k=0, \ldots, s-1, q_{0}=i, q_{s}=j\right\}
$$

and the weight $W_{q}$ of an $s$-length path $q=\left(q_{0}, \ldots, q_{s}\right)$ by $W_{q}=\prod_{k=1}^{s} B_{q_{k-1} q_{k}}$. We have $\left|\mathrm{W}_{q}\right|=O\left(\theta^{s / 2} / d_{\mathrm{in}}^{s}\right)$, since $\left|B_{i j}\right|=O\left(\sqrt{\theta} / d_{\mathrm{in}}\right)$ for any $i, j$ by the condition (C1'). It follows that the $(i, j)$-th entry of $\left(B^{\mathrm{T}}\right)^{r} B^{s}$ is given by

$$
\begin{aligned}
\left(\left(B^{\mathrm{T}}\right)^{r} B^{s}\right)_{i j} & =\sum_{k \in[p]}\left(B^{\mathrm{T}}\right)_{i k}^{r} B_{k j}^{s}=\sum_{k \in[p]}\left(\sum_{q \in \operatorname{PATH}_{k j}^{s}} W_{q}\right)\left(\sum_{q \in \operatorname{PATH}_{k i}^{r}} W_{q}\right) \\
& =\sum_{k \in[p]} \sum_{q \in \operatorname{PATH}_{k j}^{s}, q^{\prime} \in \operatorname{PATH}_{k i}^{r}} W_{q^{\prime}} W_{q}=N^{r, s}(i, j) O\left(\theta^{(r+s) / 2} / d_{\mathrm{in}}^{r+s}\right)
\end{aligned}
$$

where $N^{r, s}(i, j)$ denotes the number of possible "paths" that start from node $i$, move backwards for $r$ steps, move forwards for $s$ steps and arrive at node $j$; such paths are called treks [Uhler et al., 2013, Sullivant et al., 2010] and we denote them by $q=\left(q_{0}^{\prime}, q_{1}^{\prime}, \ldots, q_{r-1}^{\prime}, q_{r}^{\prime}=\right.$ $\left.q_{s}, q_{s-1}, \ldots, q_{1}, q_{0}\right)$, where $q_{0}^{\prime}=i, q_{0}=j$. Since $d$ is the maximum number of parent nodes, given $i, j$, there are at most $d_{\text {in }}$ different choices for $q_{1}^{\prime}$ and $q_{1}$. Similarly, given $q_{1}^{\prime}$ and $q_{1}$, there are at most $d_{\text {in }}$ choices for $q_{2}^{\prime}$ and $q_{2}$. Repeating this argument yields that $N^{r, s}(i, j) \leq d_{\text {in }}^{r+s-1}$, and it follows that $\left(\left(B^{\mathrm{T}}\right)^{r} B^{s}\right)_{i i}=O\left(\theta^{(r+s) / 2} / d_{\text {in }}\right)$. Therefore, for sufficiently large $n$,

$$
\begin{aligned}
\Sigma_{i i} & =\sum_{k=0}^{2 p-2} \sum_{\substack{r+s=k \\
r, s<p}}\left(\left(B^{\mathrm{T}}\right)^{r} B^{s}\right)_{i i} \\
& =1+\sum_{k=2}^{p} \sum_{1 \leq r \leq k-1}\left(\left(B^{\mathrm{T}}\right)^{r} B^{k-r}\right)_{i i}+\sum_{k=p+1}^{2 p-2} \sum_{k-p+1 \leq r \leq p-1}\left(\left(B^{\mathrm{T}}\right)^{r} B^{k-r}\right)_{i i} \\
& =1+\sum_{k=2}^{p} d_{\mathrm{in}}^{-1}(k-1) O\left(\theta^{k / 2}\right)+\sum_{k=p+1}^{2 p-2} d_{\mathrm{in}}^{-1}(2 p-1-k) O\left(\theta^{k / 2}\right) \\
& =1+\sum_{k=2}^{\infty} d_{\mathrm{in}}^{-1} O\left(2^{k-2} \theta^{k / 2}\right)=1+O\left(\theta / d_{\mathrm{in}}\right)
\end{aligned}
$$

Similarly, for any $i<j$,

$$
\begin{aligned}
\Sigma_{i j} & =\sum_{k=0}^{2 p-2} \sum_{\substack{r+s=k \\
r, s<p}}\left(\left(B^{\mathrm{T}}\right)^{r} B^{s}\right)_{i j} \\
& =B_{i j}+\sum_{k=2}^{p} d_{\mathrm{in}}^{-1}(k-1) O\left(\theta^{k / 2}\right)+\sum_{k=p+1}^{2 p-2} d_{\mathrm{in}}^{-1}(2 p-1-k) O\left(\theta^{k / 2}\right)
\end{aligned}
$$

from which we obtain that $\Sigma_{i j}=O\left(\sqrt{\theta} / d_{\text {in }}\right)+O\left(\theta / d_{\text {in }}\right)=O\left(\sqrt{\theta} / d_{\text {in }}\right)$.

Proof of Proposition 2. Define $\mathcal{G}_{p}\left(d_{\text {in }}\right)=\cup_{\sigma \in \mathbb{S}^{p}} \mathcal{G}_{p}^{\sigma}\left(d_{\text {in }}\right)$. Let $G_{1}, G_{2} \in \mathcal{G}_{p}\left(d_{\text {in }}\right)$ be such that $\{i \rightarrow j\} \in G_{1}$ and $G_{2}$ can be obtained from $G_{1}$ by reversing $i \rightarrow j$. Let $S=\mathrm{Pa}_{i}\left(G_{1}\right)$ and $T=\mathrm{Pa}_{j}\left(G_{2}\right)$; see Fig. 5. The sets $S$ and $T$ may not be disjoint.

Assume we are on the event $\mathcal{B}^{\prime} \cap \mathcal{J}$ defined in Section B.1. Since $G_{1}, G_{2}$ have the same

![img-4.jpeg](img-4.jpeg)

Figure 5: Local structure of $G_{1}, G_{2}$ in the proof of Proposition 2.
number of edges, the posterior ratio of $G_{1}$ to $G_{2}$ is

$$
\begin{aligned}
\frac{\exp \left(\phi\left(G_{1}\right)\right)}{\exp \left(\phi\left(G_{2}\right)\right)} & =\left(\frac{\sum_{k=1}^{p} X_{k}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{k}\left(G_{2}\right)}^{\perp} X_{k}}{\sum_{k=1}^{p} X_{k}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{k}\left(G_{1}\right)}^{\perp} X_{k}}\right)^{\frac{\alpha p n+\kappa}{2}} \\
& =\left(1+\frac{X_{j}^{\mathrm{T}}\left(\Phi_{T \cup\{i\}}-\Phi_{T}\right) X_{j}-X_{i}^{\mathrm{T}}\left(\Phi_{S \cup\{j\}}-\Phi_{S}\right) X_{i}}{\sum_{k=1}^{p} X_{k}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{k}\left(G_{1}\right)}^{\perp} X_{k}}\right)^{\frac{\alpha p n+\kappa}{2}} \\
& \leq \exp \left(\frac{\alpha p n+\kappa}{2} \frac{X_{j}^{\mathrm{T}}\left(\Phi_{T \cup\{i\}}-\Phi_{T}\right) X_{j}-X_{i}^{\mathrm{T}}\left(\Phi_{S \cup\{j\}}-\Phi_{S}\right) X_{i}}{n p \underline{\nu} / 2}\right) \\
& \leq \exp \left\{\frac{\alpha+1}{\underline{\nu}}\left[X_{j}^{\mathrm{T}}\left(\Phi_{T \cup\{i\}}-\Phi_{T}\right) X_{j}-X_{i}^{\mathrm{T}}\left(\Phi_{S \cup\{j\}}-\Phi_{S}\right) X_{i}\right]\right\}
\end{aligned}
$$

where the first inequality follows from the inequality $1+x \leq \exp (x)$ for all $x \in \mathbb{R}$ and the second follows from the observation that $X_{k}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{k}\left(G_{1}\right)}^{\perp} X_{k} \geq n \underline{\nu} / 2$ for any $k \in[p]$ on the event $\mathcal{B}^{\prime}$. To conclude the proof, we need to show

$$
X_{j}^{\mathrm{T}}\left(\Phi_{T \cup\{i\}}-\Phi_{T}\right) X_{j}-X_{i}^{\mathrm{T}}\left(\Phi_{S \cup\{j\}}-\Phi_{S}\right) X_{i}=o\left(\left(\bar{\nu}^{2} / \underline{\nu}^{2}\right) \log p\right)
$$

By Lemma 8 and condition (C2'), on the event $\mathcal{J}$, we have

$$
\begin{aligned}
& \frac{X_{i}^{\mathrm{T}} X_{i}}{n}=\Sigma_{i i}+O\left(\underline{\nu} \sqrt{\theta} / d_{\mathrm{in}}\right)=\omega^{*}+O\left(\theta / d_{\mathrm{in}}\right)+O\left(\underline{\nu} \sqrt{\theta} / d_{\mathrm{in}}\right)=\omega^{*}+o(1) \\
& \frac{X_{i}^{\mathrm{T}} X_{j}}{n}=\Sigma_{i j}+O\left(\underline{\nu} \sqrt{\theta} / d_{\mathrm{in}}\right)=O\left(\sqrt{\theta} / d_{\mathrm{in}}\right)=o(1)
\end{aligned}
$$

Hence, by Neumann series, for any $S \subseteq[p]$ such that $|S| \leq d_{\text {in }}$, we have $\left(n^{-1} X_{S}^{\mathrm{T}} X_{S}\right)^{-1}=$ $\left(\omega^{*}\right)^{-1} I+R_{S}$ where $R_{S}$ is a matrix with all entries being $O\left(\sqrt{\theta} / d_{\text {in }}\right)$. This yields, for all $i, j \in[p] \backslash S$,

$$
\begin{aligned}
\frac{X_{i}^{\mathrm{T}} \Phi_{S} X_{j}}{n} & =\frac{X_{i}^{\mathrm{T}} X_{S}}{n}\left(\frac{X_{S}^{\mathrm{T}} X_{S}}{n}\right)^{-1} \frac{X_{S}^{\mathrm{T}} X_{j}}{n} \\
& =\left[\begin{array}{llll}
O\left(\sqrt{\theta} / d_{\mathrm{in}}\right) & \cdots & O\left(\sqrt{\theta} / d_{\mathrm{in}}\right)
\end{array}\right]\left(\left(\omega^{*}\right)^{-1} I+R_{S}\right)\left[\begin{array}{c}
O\left(\sqrt{\theta} / d_{\mathrm{in}}\right) \\
\vdots \\
O\left(\sqrt{\theta} / d_{\mathrm{in}}\right)
\end{array}\right] \\
& =d_{\mathrm{in}} O\left(\theta / d_{\mathrm{in}}^{2}\right)+d_{\mathrm{in}}^{2} O\left(\theta^{3 / 2} / d_{\mathrm{in}}^{3}\right)=O\left(\theta / d_{\mathrm{in}}\right)=o(1)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& X_{j}^{\mathrm{T}}\left(\Phi_{T \cup\{i\}}-\Phi_{T}\right) X_{j}-X_{i}^{\mathrm{T}}\left(\Phi_{S \cup\{j\}}-\Phi_{S}\right) X_{i}=\frac{\left(X_{j}^{\mathrm{T}} \Phi_{T}^{\perp} X_{i}\right)^{2}}{X_{i}^{\mathrm{T}} \Phi_{T}^{\perp} X_{i}}-\frac{\left(X_{j}^{\mathrm{T}} \Phi_{S}^{\perp} X_{i}\right)^{2}}{X_{j}^{\mathrm{T}} \Phi_{S}^{\perp} X_{j}} \\
& =n \frac{\left[\frac{X_{j}^{\mathrm{T}} X_{i}}{n}-\frac{X_{j}^{\mathrm{T}} \Phi_{T} X_{i}}{n}\right]^{2}}{\frac{X_{i}^{\mathrm{T}} X_{i}}{n}-\frac{X_{i}^{\mathrm{T}} \Phi_{T} X_{i}}{n}}-n \frac{\left[\frac{X_{j}^{\mathrm{T}} X_{i}}{n}-\frac{X_{j}^{\mathrm{T}} \Phi_{S} X_{i}}{n}\right]^{2}}{\frac{X_{j}^{\mathrm{T}} X_{j}}{n}-\frac{X_{j}^{\mathrm{T}} \Phi_{S} X_{j}}{n}} \\
& =n\left(\omega^{*}\right)^{-1}\left\{(1+o(1))\left[\frac{X_{j}^{\mathrm{T}} X_{i}}{n}-\frac{X_{j}^{\mathrm{T}} \Phi_{T} X_{i}}{n}\right]^{2}-(1+o(1))\left[\frac{X_{j}^{\mathrm{T}} X_{i}}{n}-\frac{X_{j}^{\mathrm{T}} \Phi_{S} X_{i}}{n}\right]^{2}\right\} \\
& =n\left(\omega^{*}\right)^{-1}\left\{-\frac{2 X_{j}^{\mathrm{T}} X_{i}}{n}\left[\frac{X_{j}^{\mathrm{T}} \Phi_{T} X_{i}}{n}-\frac{X_{j}^{\mathrm{T}} \Phi_{S} X_{i}}{n}\right]+\left(\frac{X_{j}^{\mathrm{T}} \Phi_{T} X_{i}}{n}\right)^{2}-\left(\frac{X_{j}^{\mathrm{T}} \Phi_{S} X_{i}}{n}\right)^{2}+o\left(\theta / d_{\mathrm{in}}^{2}\right)\right\} \\
& =n\left\{O\left(\sqrt{\theta} / d_{\mathrm{in}}\right) O\left(\theta / d_{\mathrm{in}}\right)+O\left(\theta^{2} / d_{\mathrm{in}}^{2}\right)+o\left(\theta / d_{\mathrm{in}}^{2}\right)\right\}=n o\left(\theta / d_{\mathrm{in}}^{2}\right)=o\left(\left(\overline{\nu}^{2} / \underline{\nu}^{2}\right) \log p\right)
\end{aligned}
$$

which completes the proof of (25).

# B. 6 Proof of Theorem 2 

Let $\delta=\underline{\nu}^{2} C_{\min }\left(d_{\text {in }}+1\right)^{-1}\left(\underline{\nu} C_{\min }+3 \omega^{*}\left(1+C_{\min }\right)\right)^{-1}$ and $\hat{\Sigma}_{i j}=X_{i}^{\mathrm{T}} X_{j} / n$ for each $(i, j)$. Define $\mathcal{K}=\left\{\max _{i, j \in[p]}\left|\hat{\Sigma}_{i j}-\Sigma_{i j}^{*}\right| \leq \delta\right\}$. For any $\epsilon>0$, using Lemma 1 of Ravikumar et al. [2011] and our Lemma 2, we can show that $\mathbb{P}^{*}(\mathcal{A} \cap \mathcal{B} \cap \mathcal{C} \cap \mathcal{K}) \geq 1-\epsilon$ and

$$
\mathbb{P}^{*}\left\{\left|\hat{\Sigma}_{i j}-\Sigma_{i j}^{*}\right|>\delta\right\} \leq 4 \exp \left\{-\frac{n \delta^{2}}{3200 \max _{k}\left(\Sigma_{i j}^{*}\right)^{2}}\right\} \leq \frac{\epsilon}{p(p+1)}
$$

Further, from the proof of Proposition 1, we know that on the event $\mathcal{A} \cap \mathcal{B} \cap \mathcal{C}$, we have

$$
\arg \max _{S \subset P_{j}:|S| \leq d_{\text {in }}} \phi_{j}\left(S, \sum_{i \neq j} \operatorname{RSS}_{i}(G)\right)=\operatorname{Pa}_{j}\left(G^{*}\right)
$$

for any $j \in[p], P_{j} \supseteq \mathrm{~Pa}_{j}\left(G^{*}\right)$, and $G \in \mathcal{G}_{p}^{*}\left(2 d_{\text {in }}\right)$. Observe that Theorem 2 holds if we can show that for any $G \in \mathcal{G}_{p}^{*}\left(d_{\text {in }}\right)$, Algorithm 1 with input $\operatorname{RSS}=\left(\operatorname{RSS}_{1}(G), \ldots, \operatorname{RSS}_{p}(G)\right)$ returns some $\sigma \in\left[\sigma^{*}\right]$, but this follows by an argument completely analogous to the proof of Theorem 2 of Chen et al. [2019].

## B. 7 Derivation of the posterior distribution

Let $L(B, \omega)$ be the likelihood function in (2). The $\alpha$-fractional posterior distribution of $B, \omega$, given the prior distributions in (3) and (4), is

$$
\begin{aligned}
\pi_{n}(B, \omega \mid G, \sigma) & \propto \pi_{0}(B, \omega \mid G, \sigma) L(B, \omega)^{\alpha} \\
& =\frac{\pi_{0}(B, \omega \mid G, \sigma)}{L(B, \omega)^{1-\alpha}} L(B, \omega)
\end{aligned}
$$

where the first term in the last equation can be regarded as the effective prior distribution for $(B, \omega) \mid(G, \sigma)$. By the normal-inverse-gamma conjugacy, the $\alpha$-fractional marginal likelihood

of $(G, \sigma)$ is given by

$$
\begin{aligned}
& f_{\alpha}(G, \sigma) \propto \int \pi_{0}(B, \omega \mid G, \sigma) L(B, \omega)^{\alpha} d(B, \omega) \\
& =\int \pi_{0}(B \mid \omega, G, \sigma) \pi_{0}(\omega \mid G, \sigma) L(B, \omega)^{\alpha} d(B, \omega) \\
& \propto \int\left(\frac{\omega}{\gamma}\right)^{-|G| / 2} \prod_{j=1}^{p} \operatorname{det}\left(X_{\mathrm{Pa}_{j}}^{\mathrm{T}} X_{\mathrm{Pa}_{j}}\right)^{1 / 2} \exp \left\{-\frac{\gamma}{2 \omega} \sum_{j=1}^{p}\left(B_{\mathrm{Pa}_{j}, j}-\hat{B}_{\mathrm{Pa}_{j}, j}\right)^{\mathrm{T}}\left(X_{\mathrm{Pa}_{j}}^{\mathrm{T}} X_{\mathrm{Pa}_{j}}\right)\left(B_{\mathrm{Pa}_{j}, j}-\hat{B}_{\mathrm{Pa}_{j}, j}\right)\right\} \times \\
& \left(\omega^{-\frac{\kappa}{2}-1}\right)\left[\omega^{-\frac{\alpha n p}{2}} \exp \left\{-\frac{\alpha}{2 \omega} \sum_{j=1}^{p}\left(X_{j}-B_{\mathrm{Pa}_{j}, j}^{\mathrm{T}} X_{\mathrm{Pa}_{j}}\right)^{\mathrm{T}}\left(X_{j}-B_{\mathrm{Pa}_{j}, j}^{\mathrm{T}} X_{\mathrm{Pa}_{j}}\right)\right\}\right] d(B, \omega) \\
& \propto \int\left(\frac{\omega}{\gamma}\right)^{-|G| / 2} \omega^{-\frac{\alpha n p+\kappa}{2}-1} \exp \left\{-\frac{\alpha}{2 \omega} \sum_{j=1}^{p} X_{j}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}}^{\perp} X_{j}\right\}\left(\frac{\alpha+\gamma}{\omega}\right)^{-|G| / 2} \times \\
& \int\left(\frac{\omega}{\alpha+\gamma}\right)^{-|G| / 2} \prod_{j=1}^{p} \operatorname{det}\left(X_{\mathrm{Pa}_{j}}^{\mathrm{T}} X_{\mathrm{Pa}_{j}}\right)^{1 / 2} \times \\
& \exp \left\{-\frac{\alpha+\gamma}{2 \omega} \sum_{j=1}^{p}\left(B_{\mathrm{Pa}_{j}, j}-\hat{B}_{\mathrm{Pa}_{j}, j}\right)^{\mathrm{T}}\left(X_{\mathrm{Pa}_{j}}^{\mathrm{T}} X_{\mathrm{Pa}_{j}}\right)\left(B_{\mathrm{Pa}_{j}, j}-\hat{B}_{\mathrm{Pa}_{j}, j}\right)\right\} d B d \omega \\
& =\left(1+\frac{\alpha}{\gamma}\right)^{-|G| / 2} \int \omega^{-\frac{\alpha n p+\kappa}{2}-1} \exp \left\{-\frac{\alpha}{2 \omega} \sum_{j=1}^{p} X_{j}^{\mathrm{T}} \Phi_{\mathrm{Pa}_{j}}^{\perp} X_{j}\right\} d \omega \\
& \propto\left(1+\frac{\alpha}{\gamma}\right)^{-|G| / 2}\left(\sum_{j=1}^{p} \operatorname{RSS}_{j}(G)\right)^{-\frac{\alpha n p+\kappa}{2}}
\end{aligned}
$$

Given the prior distribution (5), we obtain the posterior distribution of $(G, \sigma)$ as

$$
\begin{aligned}
\pi_{n}(G, \sigma) & \propto f_{\alpha}(G, \sigma) \pi_{0}(G, \sigma) \\
& =\left(1+\frac{\alpha}{\gamma}\right)^{-|G| / 2} \cdot\left(\sum_{j=1}^{p} \operatorname{RSS}_{j}(G)\right)^{-\frac{\alpha n p+\kappa}{2}} \cdot p^{-c_{0} \log p} \cdot \mathbb{1}_{\left\{\hat{G}_{\sigma}\right\}}(G) \\
& =e^{\phi(G)} \mathbb{1}_{\left\{\hat{G}_{\sigma}\right\}}(G)
\end{aligned}
$$

# C Simulation results 

## C. 1 Mixing behavior

In Fig. 6 we examine the mixing behavior of the three types of proposals for a moderately small sample size. We repeat the simulation studies shown in panels (a), (b), and (c) of Fig. 1 in Section 4.1 by choosing $n=100$ and keeping all the other simulation settings unchanged. We confirm that all 90 trajectories have reached the red line, which appears to be the global mode. Figure 7 shows the mixing behavior of our method and the minimal I-MAP MCMC for the heterogeneous case where, for each $j \in[p]$, we sample error variance $\omega_{j}$ for node $j$ uniformly from $[0.5,1.5]$. We still observe that some trajectories of the minimal

![img-5.jpeg](img-5.jpeg)

Figure 6: Log posterior probability times $10^{-3}$ versus the effective number of iterations of 30 MCMC runs for $p=20$ and $n=100$. The red line represents the true ordering $\sigma^{*}$.

![img-6.jpeg](img-6.jpeg)

Figure 7: Log posterior probability $\times 10^{-4}$ versus the effective number of iterations of 30 MCMC runs with random initialization for the heterogeneous case with $p=20$ and $n=1000$: (a) minimal I-MAP MCMC, (b) the proposed method. The red line represents the true ordering $\sigma^{*}$.

I-MAP MCMC get stuck at local modes, while the mixing behavior of the proposed method is consistently good despite of the model misspecification.

### C.2 Performance evaluation

We consider more scenarios for the simulation study described in Section 4.2. We always fix $p=40$. In Table 4, we still generate $X$ under the equal variance assumption but we sample each $B_{ij}^{*}$ for each edge $i \rightarrow j$ in the DAG $G^{*}$ from the standard Gaussian distribution. The advantage of the proposed method is as significant as in Table 1 presented in the main text. In Table 5, we sample the error variance $\omega_{j}$ for each $j$ uniformly from $[0.7,1.3]$ and sample each $B_{ij}^{*}$ from the uniform distribution on $[-1, -0.3] \cup [0.3, 1]$. Comparing Table 5 with the left column of Table 1, we see that the advantage of our method over the competing ones becomes more substantial.


Table 4: Standard Gaussian signal case with $p=40$. Each entry gives mean $\pm 1$ standard error. The best performance with a margin of more than one se is highlighted in boldface. Time is measured in seconds.

We also conduct simulation studies on the proposed algorithm with weakly increasing error variances. We fix $n=1,000$ and $p=40$, and sample the error variance $\omega_{j} \sim$ Uniform $([1-b, 1+b])$ for 6 different heterogeneity levels $b$. We set $\sigma^{*}=(1, \ldots, p)$ to be the true ordering and sort the error variances in ascending order to make them weakly increasing in $\sigma^{*}$. We generate $G^{*}$ by adding $i \rightarrow j$ for $i<j$ with probability $p_{\text {edge }}=3 /(2 p-2)$ and draw the edge weight $B_{i j}^{*}$ independently from some distribution $F$. In Table 6, we present the results with 4 metrics: Hamming distance (HD), the false negative rate (FNR), false discover rate (FDR), and the percentage of flipped edges (Flip). The rows of Uniform and Gaussian indicate the result for $F$ being Uniform $([-1,-0.3] \cup[0.3,1])$ and that for $F$ being the standard normal distribution, respectively. Notably, the Flip rate is always very low, which indicates that the algorithm can accurately identify the true ordering. When $b=0.9$, FNR tends to be significantly larger. This is because some nodes may have very large error variances when $b=0.9$, and thus the signal-to-noise ratio is low, making it challenging for the algorithm to detect edges.

# C. 3 Single-cell real data analysis 

Figure 8 shows the result of the minimal I-MAP MCMC (with decomposable score) for the real data analysis. See Section 5 in the main text for details.


Table 5: Heterogeneous error variance case with $p=40$. Each entry gives mean $\pm 1$ standard error. The best performance with a margin of more than one se is highlighted in boldface. Time is measured in seconds.


Table 6: A table for increasing error variances with heterogeneity level $b=0,0.1, \ldots, 0.9$ with $p=40$. We sample error variance from Uniform $([1-b, 1+b])$ and sort in ascending order. Nonzero edge weights are from Uniform $([-1,-0.3] \cup[0.3,1])$ in Uniform case and $N(0,1)$ in Gaussian case. Each entry gives mean $\pm 1$ standard error.
![img-7.jpeg](img-7.jpeg)

Figure 8: Result of the minimal I-MAP MCMC for the real case-control data analysis. Given an estimate $\hat{\Gamma}_{i j}$ from MCMC samples, we infer the edge $i \rightarrow j$ exists in the DAG if $\hat{\Gamma}_{i j}>c$ where $c$ is the posterior inclusion probability cutoff. For each $c$, we count the number of edges occurring in the DAG for control samples (black), the number of edges in the DAG for case samples (red), the number of edges (edge direction ignored) in both DAGs (green), and the number of directed edges in both DAGs (blue).