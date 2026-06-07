# Research Article 

## A Hypothesis Test for Equality of Bayesian Network Models

Anthony Almudevar<br>Department of Computational Biology, University of Rochester, 601 Elmwood Avenue, Rochester, NY 14642, USA<br>Correspondence should be addressed to Anthony Almudevar, anthony_almudevar@urmc.rochester.edu

Received 26 March 2010; Revised 9 July 2010; Accepted 5 August 2010
Academic Editor: A. Datta
Copyright © 2010 Anthony Almudevar. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

Bayesian network models are commonly used to model gene expression data. Some applications require a comparison of the network structure of a set of genes between varying phenotypes. In principle, separately fit models can be directly compared, but it is difficult to assign statistical significance to any observed differences. There would therefore be an advantage to the development of a rigorous hypothesis test for homogeneity of network structure. In this paper, a generalized likelihood ratio test based on Bayesian network models is developed, with significance level estimated using permutation replications. In order to be computationally feasible, a number of algorithms are introduced. First, a method for approximating multivariate distributions due to Chow and Liu (1968) is adapted, permitting the polynomial-time calculation of a maximum likelihood Bayesian network with maximum indegree of one. Second, sequential testing principles are applied to the permutation test, allowing significant reduction of computation time while preserving reported error rates used in multiple testing. The method is applied to gene-set analysis, using two sets of experimental data, and some advantage to a pathway modelling approach to this problem is reported.

## 1. Introduction

Graphical models play a central role in modelling genomic data, largely because the pathway structure governing the interactions of cellular components induces statistical dependence naturally described by directed or undirected graphs [1-3]. These models vary in their formal structure. While a Boolean network can be interpreted as a set of state transition rules, Bayesian or Markov networks reduce to static multivariate densities on random vectors extracted from genomic data. Such densities are designed to model coexpression patterns resulting from functional cooperation. Our concern will be with this type of multivariate model. Although the ideas presented here extend naturally to various forms of genomic data, to fix ideas we will refer specifically to multivariate samples of microarray gene expression data.

In this paper, we consider the problem of comparing network models for a common set of genes under varying phenotypes. In principle, separately fit models can be directly compared. This approach is discussed in [3] and is based on distances definable on a space of graphs. Significance levels
are estimated using replications of random graphs similar in structure to the estimated models.

The algorithm proposed below differs significantly from the direct graph approach. We will formulate the problem as a two-sample test in which significance levels are estimated by randomly permuting phenotypes. This requires only the minimal assumption of independence with respect to subjects.

Our strategy will be to confine attention to Bayesian network models (Section 2). Fitting Bayesian networks is computationally difficult, so a simplified model is developed for which a polynomial-time algorithm exists for maximum likelihood calculations. A two-sample hypotheses test based on the general likelihood ratio test statistic is introduced in Section 3. In Section 4, we discuss the application of sequential testing principles to permutation replications. This may be done in a way which permits the reporting of error rates commonly used in multiple testing procedures. In Section 5, the methodology is applied to the problem of gene set (GS) analysis, in which high dimensional arrays of gene expression data are screened for differential expression (DE) by comparing gene sets defined by known functional relationships,

in place of individual gene expressions. This follows the paradigm originally proposed in gene set enrichment analysis (GSEA) [4-6]. The method will be applied to two wellknown microarray data sets.

An R library of source code implementing the algorithms proposed here may be downloaded at http://www.urmc .rochester.edu/biostat/people/faculty/almudevar.cfm.

## 2. Network Models

A graphical model is developed by defining each of $n$ genes as a graph node, labelled by gene expression level $X_{i}$ for gene $i$. The model incorporates two elements, first, a topology $G$ (a directed or undirected graph on the $n$ nodes), then, a multivariate distribution $f$ for $X=\left(X_{1}, \ldots, X_{n}\right)$ which conforms to $G$ in some well defined sense. In a Bayesian network (BN), model $G$ is a directed acyclic graph (DAG), and $f$ assumes the form

$$
f(x)=\prod_{i=1}^{n} f_{i}\left(x_{i} \mid x_{j}, j \in P a_{G}(i)\right)
$$

where $P a_{G}(i)$ is the set of parents of node $i$. Intuitively, $f_{i}\left(x_{i} \mid x_{j}, j \in P a_{G}(i)\right)$ describes a causal relationship between node $i$ and nodes $P a_{G}(i)$.

The advantage of (1) is the reduction in the degrees of freedom of the model while preserving coexpression structure. Also, some flexibility is available with respect to the choice of the conditional densities of (1), with Gaussian, multinomial, and Gamma forms commonly used [7]. We note that BNs are commonly used in many genomic applications [7-9].
2.1. Gaussian Bayesian Network Model. For this application, we will use the Gaussian BN. These models are naturally expressed using a linear regression model of node $i$ data $X_{i}$ on the data $X_{j}, j \in P a_{G}(i)$. In [10], it is noted that in microarray data gene expression levels are aggregated over large numbers of individual cells. Linear correlations are preserved under this process, but other forms of dependence generally will not be, so we can expect linear regression to capture the dominant forms of interaction which are statistically observable. In this case the maximum loglikelihood function for a given topology reduces to

$$
L(G)=\sum_{i}-\ln \left(\operatorname{MSE}\left[P a_{G}(i)\right]\right)
$$

where $\operatorname{MSE}\left[P a_{G}(i)\right]$ is the mean squared error of a linear regression fit of the offspring expressions onto those of the parents.
2.2. Restricted Bayesian Networks. Fitting BNs involves optimization over the space of topologies and hence is computationally intensive [9]. While exact algorithms are available [11], they will generally require too great a computation time for the application described below. A recent application of exact techniques to the problem of pedigree reconstruction (a BN with maximum indegree of 2 ) was described in [12].

Using methods proposed in [13] the exact computation of the maximum likelihood of a pedigree with 29 individuals (nodes) required 8 minutes. The author of [12] agrees with the conclusion reported in [13], that the method is not viable for BNs with greater than 32 nodes.

It is possible to control the size of the computation by placing a cap $K$ on the permissable indegree of each node, though the problem remains difficult even for $K=$ 2 (see, e.g., [14]). On the other hand, a method for fitting BNs with constraint $K=1$ in polynomial time is available under certain assumptions satisfied in our application. This method is based on the equivalence of the approximation of multivariate probability models using tree-structured dependence and the minimum spanning tree (MST) problem as described in [15]. The objective is the minimization of an information difference $I\left(P, P_{t}\right)$, where $P$ is the target density, and $P_{t}$ is selected from a class of tree-structured approximating densities. Interest in [15] is restricted to discrete densities. We find, however, that the basic idea extends to general BNs in a natural way. See [16] for further discussion of this model.

Many heuristic or approximate methods exist for fitting Bayesian networks. See [17] for a recent survey. Such algorithms are usually based on MCMC techniques or heuristic algorithms such as TABU searches [18]. We note that the proposed hypothesis test will depend on the calculation of a maximum likelihood ratio, hence it is important to have reasonable guarantees that a maximum has been reached. Thus, given the choice between an exact solution of a restricted class of models or an approximate solution of a general class of models, the former seems preferable. Considering also that in the application described below a solution is required for cases number in " 10 s or 100 s " of thousands, a polynomial time exact solution to a restricted class of models appears to be the best choice.

Suppose we are given an $n$-dimensional random vector $X$. We will assume that the density is taken from a parametric family $f^{\theta}(x)=f^{\theta}\left(x_{1}, \ldots, x_{n}\right), \theta \in \Theta$. We write first- and second-order marginal densities $f^{\theta_{i}}\left(x_{i}\right)$ and $f^{\theta_{i j}}\left(x_{i}, x_{j}\right)$, with conditional densities $f^{\theta_{i j}}\left(x_{i} \mid x_{j}\right)=f^{\theta_{i j}}\left(x_{i}, x_{j}\right) / f^{\theta_{j}}\left(x_{j}\right)$. For convenience, we introduce a dummy vector component $x_{0}$, for which $f^{\theta_{i k}}\left(x_{i} \mid x_{0}\right)=f^{\theta_{i}}\left(x_{i}\right)$. Let $\mathcal{G}_{1}$ be the set of DAGs on nodes $(1, \ldots, n)$ with maximum indegree 1 . This means that a graph $g \in \mathcal{G}_{1}$ may be written as a mapping $g:(1, \ldots, n)=$ $(0,1, \ldots, n)$. If $i$ has indegree 0 set $g(i)=0$, otherwise $g(i)$ is the parent node of $i$. We must have $g(i)=0$ for at least one $i$. For each $g \in \mathcal{G}_{1}$ let $\Theta \mathcal{\varepsilon} \subset \Theta$ be the set of parameters admitting the BN decomposition

$$
\begin{aligned}
f^{\theta}(x) & =\prod_{i=1}^{n} f^{\theta_{g(i)}}\left(x_{i} \mid x_{g(i)}\right) \\
& =\left(\prod_{i=1}^{n} f^{\theta_{i}}\left(x_{i}\right)\right) \times\left(\prod_{\substack{i \leq g(i)>0 \\
\left(x_{i} \mid f^{\theta}\left(x_{i}\right)\right.}}\right) f^{\theta_{g(i)}}\left(x_{g(i)}\right)
\end{aligned}
$$

Now suppose we are given $N$ independent and complete replicates $\tilde{X}=(X(1), \ldots, X(N))$ of $X$. Write components

$X(k)=\left(X_{1}(k), \ldots, X_{n}(k)\right), k=1, \ldots, N$. The log likelihood function becomes, for $\theta \in \Theta^{g}$,

$$
\begin{aligned}
L(\theta \mid \tilde{X}) & =\sum_{i=1}^{n} L_{i}\left(\theta_{i}\right)+\sum_{i: g(i)>0} L_{i g(i)}\left(\theta_{i g(i)}\right), \text { where } \\
L_{i}(\theta_{i}) & =\sum_{k=1}^{N} \log \left(f^{\theta_{i}}\left(X_{i}(k)\right)\right) \\
L_{i j}\left(\theta_{i j}\right) & =\sum_{k=1}^{N} \log \left(\frac{f^{\theta_{i j}}\left(X_{i}(k), X_{j}(k)\right)}{f^{\theta_{i}}\left(X_{i}(k)\right) f^{\theta_{j}}\left(X_{j}(k)\right)}\right)
\end{aligned}
$$

Suppose we may construct estimators $\hat{\theta}_{l}=\hat{\theta}_{l}(\tilde{X}), \hat{\theta}_{i j}=$ $\hat{\theta}_{i j}(\tilde{X})$. We then assume there is some selection rule $\hat{\theta}^{g}=$ $\hat{\theta}^{g}(\tilde{X}) \in \Theta^{g}$ for each $g \in \mathcal{G}_{1}$. This will typically be the exact or approximate maximum likelihood estimate (MLE) on parameter space $\Theta^{g}$. We will need the following assumptions.
(A1) For each $g \in \mathcal{G}_{1}, \hat{\theta}_{i}^{g}=\hat{\theta}_{l}$, and $\hat{\theta}_{i g(i)}^{g}=\hat{\theta}_{i g(i)}$.
(A2) For each $i, j$ we have $L_{i j}\left(\hat{\theta}_{i j}^{g}\right) \geq 0$.
We now consider the problem of maximizing $L^{*}(g \mid \tilde{X})=$ $L(\hat{\theta}^{g} \mid \tilde{X})$ over $g \in \mathcal{G}_{1}$. It will be convenient to isolate the term

$$
L_{2}^{*}(g \mid \tilde{X})=\sum_{i: g(i)>0} L_{i g(i)}\left(\hat{\theta}_{i g(i)}^{g}\right)
$$

A spanning tree on nodes $(1, \ldots, n)$ is an acyclic connected undirected graph. Given edge weights $w_{i j}$, a minimum spanning tree (MST) is any spanning tree minimizing the sum of its edge weights among all spanning trees. A number of well-known polynomial time algorithms exist to construct a MST. Two that are commonly described are Prim's and Kruskal's algorithms [19]. Kruskal's algorithm is described in [15]. In the following theorem, the problem of maximizing $L^{*}(g \mid \tilde{X})$ is expressed as a MST problem.

Theorem 1. If assumptions (A1)-(A2) hold, then maximizing $L^{*}(g \mid \tilde{X})$ over $\mathcal{G}_{1}$ is equivalent to determining the MST for edge weights $w_{i j}=-L_{i j}\left(\hat{\theta}_{i j}^{g}\right)$.

Proof. Under assumption (A1), from definition (4) it follows that $L^{*}(g \mid \tilde{X})$ depends on $g$ only through the term $L_{2}^{*}(g \mid$ $\tilde{X})$. Then suppose $g^{\prime}$ maximizes $L_{2}^{*}(g \mid \tilde{X})$. For any spanning tree $t$ define $W_{t}=\sum_{(i j) \in t ; i<j} w_{i j}$ and suppose $t^{\prime}$ minimizes $W_{t}$. Assume $g^{\prime}$ is not connected. There must be at least two nodes $i, j$ for which $g(i)=g(j)=0$, and for which the respective subgraphs containing $i, j$ are unconnected. In this case, extend $g^{\prime}$ to $g^{\prime \prime}$ by adding directed edge $(i, j)$. We must have $g^{\prime \prime} \in \mathcal{G}_{1}$, and by (A2) we have $L_{2}^{*}\left(g^{\prime \prime} \mid \tilde{X}\right) \geq L_{2}^{*}\left(g^{\prime} \mid \tilde{X}\right)$. We may therefore assume $g^{\prime}$ is connected. The undirected graph of $g^{\prime}$ is a spanning tree, so $W_{t^{\prime}} \leq-L_{2}^{*}\left(g^{\prime} \mid \tilde{X}\right)$.

Next, note that $t^{\prime}$ can be identified with an element of $\mathcal{G}_{1}$ by defining any node as a root node, enumerating all paths
from the root node to terminal nodes, then assigning edge directions to conform to these paths. This implies $L_{2}^{*}\left(g^{\prime} \mid\right.$ $\tilde{X}) \geq-W_{t^{\prime}}$, which in turn implies $L_{2}^{*}\left(g^{\prime} \mid \tilde{X}\right)=-W_{t^{\prime}}$, and that $g^{\prime}, t^{\prime}$ may be selected so that $t^{\prime}$ can be identified with $g^{\prime}$.

Remark 1. In general, the optimizing graph from $\mathcal{G}_{1}$ will not be unique. First, the solution to the MST problem need not be unique. Second, there will always be at least two extensions of a spanning tree to a BN.

Marginal means, variances and, correlations of $X$ are denoted $\mu_{i}, \sigma_{i}^{2}, \rho_{i j}$, leading to parameters $\theta_{i}=\left(\mu_{i}, \sigma_{i}^{2}\right), \theta_{i j}=$ $\left(\theta_{i}, \theta_{j}, \rho_{i j}\right)$. Each parameter in the set $\Theta^{g}$ represents the class of Gaussian BNs which conform to graph $g$. Following the construction in assumption (A1), let $\tilde{\theta}_{i}=\left(\bar{X}_{i}, S_{i}^{2}\right), \hat{\theta}_{i j}=$ $\left(\hat{\theta}_{i}, \hat{\theta}_{j}, R_{i j}\right)$ using summary statistics $\bar{X}_{i}=N^{-1} \sum_{k} X_{i}(k)$, $S_{i}^{2}=N^{-1} \sum_{k}\left(X_{i}(k)-\bar{X}_{i}\right)^{2}, R_{i j}=N^{-1}\left(S_{i} S_{j}\right)^{-1} \sum_{k}\left(X_{i}(k)-\right.$ $\left.\bar{X}_{i}\right)\left(X_{j}(k)-\bar{X}_{j}\right)$. Under the usual parameterization, it can be shown that (omitting constants)

$$
\begin{array}{r}
L_{i}\left(\tilde{\theta}_{i}^{g}\right)=-\left(\frac{N}{2}\right) \log \left(S_{i}^{2}\right) \\
L_{i j}\left(\hat{\theta}_{i j}^{g}\right)=-\left(\frac{N}{2}\right) \log \left(1-R_{i j}^{2}\right)
\end{array}
$$

noting that, since $0 \leq R_{i j}^{2} \leq 1$, assumption (A2) holds.

## 3. General Maximum Likelihood Ratio Test

Identification of nonhomogeneity between two Bayesian networks will be based on a general maximum likelihood ratio test (MLRT). It is important to note the properties of the MLRT are well understood in parametric inference of limited dimension, and a sampling distribution can be accurately approximated with a large enough sample size. These known properties no longer apply in the type of problem considered here, primarily due to the small sample size, large number of parameters, and the fact that optimization over a discrete space is performed. In addition, the maximum likelihood principle itself favors spurious complexity when no model selection principles are used. While we cannot claim that the MLRT possesses any optimum properties in this application, the use of a permutation procedure will permit accurate estimates of the observed significance level while the use of the restricted model class will control to some degree the degrees of freedom of the model. See, for example, [20] for a general discussion of these issues.

Suppose $\left\{f_{\theta}: \theta \in \Theta\right\}$ is a family of densities defined on some parameter set $\Theta$. We are given two random samples $\tilde{X}=\left(X_{1}, \ldots, X_{n_{1}}\right)$ and $\tilde{Y}=\left(Y_{1}, \ldots, Y_{n_{2}}\right)$ from respective densities $f^{\theta_{1}}$ and $f^{\theta_{2}}$. Denote pooled sample $\tilde{X} \tilde{Y}=$ $(\tilde{X}, \tilde{Y})$. The density of $\tilde{X}$ and $\tilde{Y}$, respectively, are $f_{\tilde{X}}^{\theta_{1}}(\widetilde{x})=$ $\prod_{i=1}^{n_{1}} f^{\theta_{1}}\left(x_{i}\right)$ and $f_{\tilde{Y}}^{\theta_{2}}(\widetilde{y})=\prod_{i=1}^{n_{2}} f^{\theta_{2}}\left(y_{i}\right)$. We consider null hypothesis $H_{0}: \theta_{1}=\theta_{2}$. Under $H_{0}$ the joint density of $\widetilde{X} \widetilde{Y}$ is $f_{\widetilde{X} \widetilde{Y}}^{\theta}(\widetilde{x}, \widetilde{y})=f_{\widetilde{Y}}^{\theta}(\widetilde{x}) f_{\widetilde{Y}}^{\theta}(\widetilde{y})$ for some parameter $\theta^{\prime}$. Assume the existence of maximum likelihood estimators

$\theta_{X}^{*}=\arg \max _{\theta} L(\theta \mid \widetilde{X}), \theta_{Y}^{*}=\arg \max _{\theta} L(\theta \mid \widetilde{Y})$, and $\theta_{S Y}^{*}=$ $\arg \max _{\theta} L(\theta \mid \widetilde{X} \widetilde{Y})$. The general likelihood ratio statistic in logarithmic scale is then (with large values rejecting $H_{0}$ )

$$
\Lambda(\widetilde{X}, \widetilde{Y})=L\left(\theta_{X}^{*} \mid \widetilde{X}\right)+L\left(\theta_{Y}^{*} \mid \widetilde{Y}\right)-L\left(\theta_{S Y}^{*} \mid \widetilde{X} \widetilde{Y}\right)
$$

Asymptotic distribution theory is not relevant here due to small sample size and the fact that optimization is performed in part over a discrete space of models, so a two sample permutation procedure will be used. Permutations will be approximately balanced to reduce spurious variability when a true difference in expression pattern exists (see, e. g., [21] for discussion). This can be done by changing group labels of $\bar{n} \approx n_{1} n_{2} /\left(n_{1}+n_{2}\right)$ randomly selecting sample vectors from each of $\widetilde{X}$ and $\widetilde{Y}$. This results in permutation replicate samples $\widetilde{X}^{P}$ and $\widetilde{Y}^{P}$. The balanced procedure ensures that each permutation replicate sample contains approximately equal proportions of the original samples.

We now define Algorithm 1.
Algorithm 1. (1) Determine $g_{1}, g_{2}, g_{12}$ by maximizing $L_{2}^{*}(g \mid$ $\left.\widetilde{X}), L_{2}^{*}(g \mid \widetilde{Y}), L_{2}^{*}(g \mid \widetilde{X}, \widetilde{Y}) \text { (MST algorithm }\right)$.
(2) Set $\Lambda^{\text {obs }}=L^{*}\left(g_{12} \mid \widetilde{X}, \widetilde{Y}\right)-L^{*}\left(g_{1} \mid \widetilde{X}\right)-L^{*}\left(g_{2} \mid \widetilde{Y}\right)$.
(3) Construct $M$ replications $\Lambda_{1}^{P}, \ldots, \Lambda_{M}^{P}$ in the following way. For each replication $i$, create random replicate samples $\widetilde{X}^{P}$ and $\widetilde{Y}^{P}$, then determine $g_{i}^{P}, g_{i}^{P}$ which maximize $L_{2}^{*}\left(g \mid \widetilde{X}^{P}\right), L_{2}^{*}\left(g \mid \widetilde{Y}^{P}\right)$. Set $\Lambda_{i}^{P}=L^{*}\left(g_{12} \mid\right.$ $\left.\widetilde{X Y}\right)-L^{*}\left(g_{1}^{P} \mid \widetilde{X}^{P}\right)-L^{*}\left(g_{2}^{P} \mid \widetilde{Y}^{P}\right)$.
(4) Set $P$-value

$$
\widehat{p}=\frac{\left|\left|\Lambda_{i}^{P} \geq \Lambda^{\mathrm{obs}}\right|\right|+1}{M+1}
$$

Note that the quantity $L^{*}\left(g_{12} \mid \widetilde{X} \widetilde{Y}\right)$ is permutation invariant and hence need not be recalculated within the permutation procedure.

## 4. Permutation Tests with Stopping Rules

Permutation or bootstrap tests usually reduce to the estimation of a binomial probability by direct simulation. Since interest is usually in identifying small values, it would seem redundant to continue sampling when, for example, the first ten simulations lead to an estimate of $1 / 2$. This suggests that a stopping rule may be applied to permutation sampling, resulting in significant reduction in computation time, provided it can be incorporated into a valid inference statement. A variety of such procedures have been described in the literature but do not seem to have been widely adopted in genomic discovery applications [22-24].

Suppose, as in Algorithm 1, we have an observed test statistic $\Lambda^{\text {obs }}$, and can simulate indefinitely a sequence $\Lambda_{1}^{P}, \Lambda_{2}^{P}, \ldots$ from a null distribution $P_{0}$. By convention we assume that large values of $\Lambda^{\text {obs }}$ tend to reject the null hypothesis. To develop a stopping rule for this sequence set

$$
S_{i}=\sum_{i^{\prime}=1}^{i} I\left|\Lambda_{i^{\prime}}^{P} \geq \Lambda^{\text {obs }}\right|
$$

Formally, $T$ is a stopping time if the occurrence of event $\{T>$ $t\}$ can be determined from $S_{1}, \ldots, S_{t}$. We may then design an algorithm which terminates after sampling a sequence of exactly length $T$ from $P_{0}$, then outputs $\Lambda_{1}^{P}, \ldots, \Lambda_{T}^{P}$, from which the hypothesis decision is resolved. We refer to such a procedure as a stopped procedure. A fixed procedure (such as Algorithm 1) can be regarded as a special case of a stopped procedure in which $T \equiv M$.

An important distinction will have to be made between a single test and a multiple testing procedure (MTP), which is a collection of $K$ hypothesis tests with rejection rules that control for a global error rate such as false discovery rate (FDR), family-wise error rate (FWER), or per family error rate (PFER) [25]. In the single test application, we may set a fixed significance level $\alpha$ and continue replications until we conclude that the $P$-value is above or below $\alpha$. For an MTP, it will be important to be able to estimate small $P$-values, so a stopping rule which permits this is needed. Although the two cases have different structure, in our development they will both be based on the sequential probability ratio test (SPRT), first proposed in [26], which we now describe.
4.1. Sequential Probability Ratio Test (SPRT). Formally (see [27, Chapter 2]) the SPRT tests between two simple alternatives $H_{0}: \theta=\theta_{0}$ versus $H_{1}: \theta=\theta_{1}$, where $\theta$ parametrizes a family of distributions $f_{\theta}$. We assume there is a sequence of iid observations $x_{1}, x_{2} \ldots$ from $f_{\theta}$ where $\theta \in\left\{\theta_{0}, \theta_{1}\right\}$. Let $l_{n}(\theta)$ be the likelihood function based on $\left(x_{1}, \ldots, x_{n}\right)$ and define the likelihood ratio statistic $\lambda_{n}=l_{n}\left(\theta_{1}\right) / l_{n}\left(\theta_{0}\right)$. For two constants $A<1<B$, define stopping time

$$
T=\min \left\{n: \lambda_{n} \notin(A, B)\right\}
$$

It can be shown that $E_{\theta}[T]<\infty$. If $\lambda_{T} \leq A$ we conclude $H_{0}$ and conclude $H_{1}$ otherwise. We define errors $\alpha_{0}=P_{\theta_{0}}\left(\lambda_{T} \geq\right.$ $B)$ and $\alpha_{1}=P_{\theta_{1}}\left(\lambda_{T} \leq A\right)$. It turns out that the SPRT is optimal under the given assumptions in the sense that it minimizes $E_{\theta}[T]$ among all sequential tests (which includes fixed sample tests) with respective error probabilities no larger than $\alpha_{0}, \alpha_{1}$. Approximate formulae for $\alpha_{0}, \alpha_{1}$ and $E_{\theta_{1}}[T], E_{\theta_{1}}[T]$ are given in [27].

Hypothesis testing usually involves composite hypotheses, with distinct interpretations for the null and alternative hypothesis. One method of adapting the SPRT to this case is to select surrogate simple hypotheses. For example, to test $H_{0}: \theta \geq \theta^{\prime}$ versus $H_{1}: \theta<\theta^{\prime}$, we could select simple hypotheses $\theta_{0} \geq \theta^{\prime}$ and $\theta_{1}<\theta^{\prime}$. In this case, we would need to know the entire power function, which may be estimated using simulations.

An additional issue then arises in that the expected stopping time may be very large for $\theta \in\left(\theta_{0}, \theta_{1}\right)$. This can be accommodated using truncation. Suppose a reasonable choice for a fixed sample size is $M$. We would then use truncated stopping time $T^{M}=\min \{T, M\}$, with $T$ defined in (10). When $T>M$, we could, for example, select hypothesis $H_{0}$ if $\lambda_{M} \leq 1$. These modifications are discussed in [27].
4.2. Single Hypothesis Test. Suppose we adopt a fixed significance level $\alpha$ for a single hypothesis test. If $\alpha^{\text {obs }}$ is

the (unknown) true significance level, we are interested in resolving the hypothesis $H: \alpha^{\text {obs }} \leq \alpha$. The properties of the test are summarized in a power curve, that is, the probability of deciding $H$ is true for each $\alpha^{\text {obs }}$. An example of this procedure is given in [28], for $\alpha=0.05$, using a SPRT with parameters $A=0.0010101, B=99.9, \theta_{0}=0.03, \theta_{1}=0.05$, and truncation at $M=2000$. Hypothesis $H$ is concluded if $\lambda_{T^{M}} \leq A$ when $T<M$; otherwise when $\lambda_{M} \leq 1$.
4.3. Multiple Hypothesis Tests. We next assume that we have $K$ hypothesis tests based on sequences of the form (9). We wish to report a global error rate, in which case specific values of small $P$-values are of importance. We will consider specifically the class of MTPs referred to as either step-up or step-down procedures. If we are given a sequence of $K P$ values $p_{1}, \ldots, p_{K}$ which have ranks $\nu_{1}, \ldots, \nu_{K}$, then adjusted $P$-values, $p_{v_{i}}^{\alpha}$ are given by:

$$
\begin{aligned}
& p_{v_{i}}^{\alpha}=\max _{j \leq i} \min \left(C\left(K, j, p_{\nu_{j}}\right), 1\right)(\text { step-down procedure }) \\
& p_{v_{i}}^{\alpha}=\min _{j \leq i} \min \left(C\left(K, j, p_{\nu_{j}}\right), 1\right)(\text { step-up procedure })
\end{aligned}
$$

where the quantity $C(K, j, p)$ defines the particular MTP. It is assumed that $C(K, j, p)$ is an increasing function of $p$ for all $K, j$. The procedure is implemented by rejecting all null hypotheses for which $p_{i}^{\alpha} \leq \alpha$. Depending on the MTP, various forms of error, usually either family-wise error rate (FWER) or false discovery rate (FDR), are controlled at the $\alpha$ level. For example, the Benjamini-Hochberg (BH) procedure is a step-up procedure defined by $C(K, j, p)=$ $j^{-1} K p$ and controls for FDR for independent hypothesis tests. A comprehensive treatment of this topic is given in, for example, [25].

Suppose we have $K$ probabilities $p_{1}, \ldots, p_{K}$ ( $P$-values associated with $K$ tests). For each test $i=1, \ldots, K$, we may generate $S_{j}^{i} \sim \operatorname{bin}(p_{i}, j)$ as the cumulative sum defined in (9). Now suppose we define any stopping time $T_{i}$, bounded by $M$, for each sequence $S_{1}^{i}, \ldots, S_{M}^{i}$ (this may or may not be related to the SPRT). Then define estimates $\widehat{p}_{i}=\widehat{p}_{i} I\left\{T_{i}=\right.$ $M\}+I\left\{T_{i}<M\right\}$, with $\widehat{p}_{i}=\left(\left|\left\{\Lambda_{i}^{P} \geq \Lambda^{\text {obs }}\right\}\right|+1\right) /(M+1)$.

For a fixed MTP, the estimates $\widehat{p}_{1}, \ldots, \widehat{p}_{K}$ would replace the true values in (11), yielding estimated adjusted $P$-values $\widehat{p}_{i}^{\alpha}$ while for the stopped MTP adjusted $P$-values $\widehat{p}_{i}^{\alpha}$ are produced in the same manner using $\widehat{p}_{1}, \ldots, \widehat{p}_{K}$. It is easily seen that $\widehat{p}_{i} \geq \widehat{p}_{i}$ while the rankings of $\widehat{p}_{i}$ (accounting for ties) are equal to the rankings of $\widehat{p}_{i}$. Furthermore, the formulae in (11) are monotone in $p_{i}$, so we must have $\widehat{p}_{i}^{\alpha} \geq \widehat{p}_{i}^{\alpha}$. Thus, the stopped procedure may be seen as being embedded in the fixed procedure. It inherits whatever error control is given for the fixed MTP, with the advantage that the calculation of the adjusted $P$-values $\widehat{p}_{i}^{\alpha}$ uses only the first $T_{i}$ replications for the $i$ th test.

The procedure will always be correct in that it is strictly more conservative than the fixed MTP in which it is embedded, no matter which stopping time is used. The remaining issue is the selection of $T_{i}$ which will equal $M$ for small enough values of $p_{i}$ but will also have $E\left[T_{i}\right] \ll M$
for larger values of $p_{i}$. It is a simple matter, then, to modify the SPRT described in Section 4.2 by eliminating the lower bound $A$ (equivalently $A=0$ ). We will adopt this design in this paper. This gives Algorithm 2.

Algorithm 2. (1) Same as Algorithm 1, step 1.
(2) Same as Algorithm 1, step 2.
(3) Simulate replicates $\Lambda_{i}^{P}$ in Algorithm 1, step 3, until the following stopping criterion is met. Set $S_{i}=$ $\sum_{i^{\prime}=1}^{i} I\left\{\Lambda_{i^{\prime}}^{P} \geq \Lambda^{\text {obs }}\right\} \mid$, and let $\lambda_{i}=\left[\theta_{1} / \theta_{0}\right]^{\mathrm{S}_{i}}\left[(1-\right.$ $\left.\theta_{1}\right) / 1-\theta_{0}\right]^{i-S_{i}}$, where $\theta_{0} \leq \alpha<\theta_{1}$. Stop sampling at the $i$ th replication if $\lambda_{i} \geq B$, where $B>1$, or until $i=M$, whichever occurs first.
(4) Let $T^{\prime}$ be the number of replications in step 3. If $T^{\prime}=$ $M$, set

$$
\widetilde{p}=\frac{\left|\left\{\Lambda_{i}^{p} \geq \Lambda^{\text {obs }}\right\}\right|+1}{M+1}
$$

otherwise set $\widetilde{p}=1$.
The values $\widetilde{p}$ generated by Algorithm 2 can then be used in a stopped MTP as described in this section.

## 5. Gene-Set Analysis

A recent trend in the analysis of microarray data has been to base the discovery of phenotype-induced DE on gene sets rather than individual genes. The reasoning is that if genes in a given set are related by common pathway membership or other transcriptional process, then there should be an aggregate change in gene expression pattern. This should give increased statistical power, as well as enhanced interpretability, especially given the lack of reproducibility in univariate gene discovery due to the stringent requirements imposed by multiple testing adjustments. Thus, the discovery process reduces to a much smaller number of hypothesis tests with more direct biological meaning. Some objections may be raised concerning the selection of the gene sets when theses sets are themselves determined experimentally. Additionally, gene sets may overlap. While these problems need to be addressed, it is also true that such gene set methods have been shown to detect DE not uncovered by univariate screens.

A crucial problem in gene set analysis is the choice of test statistic. The problem of testing against equality of random vectors in $\mathfrak{R}^{d}, d>1$, is fundamentally different from the univariate case $d=1$. The range of statistics one would consider for $d=1$ is reasonably limited, the choice being largely driven by distributional considerations. For $d>1$, new structural or geometric considerations arise. For example, we may have differential expression between some but not all genes in the gene set, which makes selection of a single optimal test statistic impossible. Alternatively, the experimental random vectors may differ in their level of coexpression independently of their level of marginal DE.

In fact, almost all GS procedures directly measure aggregate DE, so an important question is whether or not phenotypic variation is almost completely expressible

as DE. If so, then a DE based statistic will have fewer degrees of freedom, hence more power, than one based on a more complex model. Otherwise, a reasonable conjecture is that a compound GS analysis will work best, employing a DE statistic as well as one more sensitive to changes in coexpression patterns.

Correlations have been used in a number of gene discovery applications. They may be used to associate genes of unknown function with known pathways [29, 30]. Additionally, a number of GS procedures exist which incorporate correlation structure into the procedure [31–33]. However, a direct comparison of correlations is not practical due to the large number (d(d − 1)/2) of distinct correlation parameters. Therefore, there is a considerable advantage to the statistic (7) based on the reduced BN model, in that the correlation structure can be summarized by the d correlation parameters output by the MST algorithm, yielding a transitive dependence model similar to that effectively exploited in [29].

It is important to refer to a methodological characterization given in [34]. A distinction is made between two types of null hypotheses. Suppose we are given samples of expression levels from a gene set G from two phenotypes. Suppose also that for each gene in G and its complement G^{c}, a statistical measure of differential expression is available. For a competitive test, the null hypothesis H<sup>nemp</sup><sub>0</sub> is that the prevalence of differential expression in G is no greater than in G^{c}. For a self-contained test, the null hypothesis H<sup>self</sup><sub>0</sub> is that no genes in G are differentially expressed. In the GSEA method of [4, 5] concern is with H<sup>nemp</sup><sub>0</sub>. In most subsequent methods, including the one proposed here, H<sup>self</sup><sub>0</sub> is used.

For general discussions of the issues raised here, see [35–37]. Comprehensive surveys of specific methods can be found in [38] or [39].

### 5.1. Experimental Data

We will demonstrate the algorithm proposed here on two data sets examined elsewhere in the literature. These were obtained from the GSEA website www.broad.mit.edu/gsea [6]. In [5], a data set p53 is extracted from the NCI-60 collection of cancer cell lines, with 17 cell lines classified as normal, and 33 classified as carrying mutations of p53. We also examine the DIABETES data set introduced in [4], consisting of microarray profiles of skeletal muscle biopsies from 43 males. For the DIABETES data set used here, there were 17 normal glucose tolerance (NGT) subjects and 17 diabetes (DMT) subjects. For gene sets, we used one of the gene set lists compiled in [5], denoted C<sub>2</sub>, consisting of 472 gene sets with products collectively involved in various metabolic and signalling pathways, as well as 50 sets containing genes exhibiting coregulated response to various perturbations. In our analyses, FDR will be estimated using the BH procedure.

#### 5.1.1. P53 Data

A t-test was performed on each of the 10,100 genes. Only 1 gene had an adjusted P-value less than FDR = 0.25 (bax, P = 5 × 10<sup>−6</sup>, P<sub>adj</sub> = 0.05). Several GS analyses for this data set (using C<sub>2</sub>) have been reported. We cite the GSEA analysis in [5] and a modification of the GSEA proposed in [40]. Also, in [38], this data set is used to test three procedures, each using various standardization procedures. Two are based on logistic regression (Global test [41] ANCOVA Global test [42]). The third is an extension of the Significance Analysis of Microarray (SAM) procedure [43] to gene sets proposed in [44] (SAM-GS).

Table 1 lists pathways selected from C<sub>2</sub> for the analysis proposed here using FDR ≤ 0.25, including unadjusted and adjusted P-values. For each entry we indicate whether or not the pathway was selected under the analyses reported in [5] (Sub, FDR ≤ 0.25), [40] (Efr, FDR ≤ 0.1) and [38] (Liu, nominal P-value ≤ .001 in at least one procedure). It is important to note that the results indicated with an asterisk (*) are not directly comparable due to differing MTP control, and are included for completeness.

The first five pathways are directly comparable. Of these, two were not detected in any other analysis. Our procedure was repeated for these pathways using the sum of the squared t-statistics across genes. The nominal P-values for g2 Pathway and cell cycle checkpoint II were .0044 and >.05, respectively. Since we are interested in identifying pathways which may be detectable by pathway methods, but not DE based methods we will examine cell cycle checkpoint II more closely. Applying a univariate t-test to each of the 10 genes yields one P-value of 0.001 (cdkn2a), with the remaining P-values greater than 0.1 hence a DE-based approach is unlikely to select this pathway. Furthermore, P-values under 0.05 for change in correlation are reported for rbbp8/rb1, nbs1/ccng2, atr/ccne2, nbs1/tp53, and ccng2/tb53 (P = .002, .006, .008, .035, and .036). Clearly, the difference in gene expression pattern is determined by change in coexpression pattern. In Figure 1, the correlations for all gene pairs for wild-type and mutation

![img-0.jpeg](img-0.jpeg)

Figure 2: Bayesian network fits for mutation data for cycle checkpoint II pathway using (a) Minimum Spanning Tree algorithm (maximum indegree of 1); (b) Bayesian Information Criterion (maximum indegree of 2).
groups are indicated. A clear pattern is evident, by which correlation structure present in the wildtype class does not exist in the mutation class.

To further clarify the procedure, we compare the BN model obtained from the data for the ten genes associated with the cell cycle checkpoint II pathway, separately for mutation and wildtype conditions. If there is interest in a post-hoc analysis of any particular pathway, the rational for the MST algorithm no longer holds, since only one fit is required. It is therefore instructive to compare the MST model to a more commonly used method. In this case, we will use the Bayesian Information Criterion (BIC) (see, e.g., [7]), with a maximum indegree of 2 . To fit the model we use a simulated annealing algorithm adapted from [45]. The resulting graphs are shown in Figures 2 (mutation) and 3 (wildtype). The MST and BIC fits are labelled (a) and (b) respectively. For the mutation fit, there is a very close correspondence between the topologies produced by the respective methods. For the wildtype data, some correspondence still exists, but less so then for the mutation data. The topologies between the conditions differ more significantly, as predicted by the hypothesis test.
5.1.2. Diabetes. No pathways were detected at a FDR of 0.25 . The two pathways with the smallest $P$-values were atrbrca Pathway and MAP00252 Alanine and aspartate metabolism ( $P=.0026, .003$ ). In [33] the latter pathway was the single pathway reported with PFER $=1$. The comparable PFER
![img-1.jpeg](img-1.jpeg)

Figure 3: Bayesian network fits for wildtype data for cycle checkpoint II pathway using (a) Minimum Spanning Tree algorithm (maximum indegree of 1). (b) Bayesian Information Criterion (maximum indegree of 2 ).
rate of the two pathways reported here would be 1.36 and 1.57. The atrbrca Pathway contains 25 genes. Of these, only fance differentially expressed at a 0.05 significance level ( $P=.0059$ ). For each gene pair, correlation coefficients were calculated and tested for equality between classes $N G T$ and DMT. Table 2 lists the 10 highest ranking gene pairs in terms of correlation magnitude within the NGT class. Also listed is the corresponding correlation within the DMT class, as well as the two-sample $P$-value for correlation difference. The analysis is repeated after exchanging classes, also in Table 2. We note that for a sample size of 17 , an approximate $95 \%$ confidence interval for a reported correlation of $R=0.6$ is $(0.17,0.84)$ whereas the standard deviation of a sample correlation coefficient of mean zero is approximately 0.27 . There is likely to be considerable statistical variation in graphical structure under the null hypothesis.

Examining the first table, differences in correlation appear to be explainable by sampling variation. In the second there are two gene pairs fanca/fance and fanca/hus1 with

Table 1: P53 pathways, with GS size $(N)$, unadjusted and FDR adjusted $P$-values $\left(P, P^{*}\right)$. Inclusion in analyses cited in Section 5.1 indicated. †The complete name of DNA_DAMAGE is DNA_DAMAGE_SIGNALLING. ‡The complete name of MAP00562 is MAP00562_Inositol_phosphate_metabolism. *Inclusion criterion based on control rate of original analysis.


Table 2: Correlation analysis for DIABETES data. For each pathway and phenotype, 10 gene pairs with the largest correlation ( $\times 100$ ) magnitudes; correlation ( $\times 100$ ) of alternative phenotype; and $P$-value ( $\times 1000$ ) against equality.


Table 3: For stopped (St) and fixed (Fx) procedures, the table gives computation times; mean number of replications; \% gene sets completely sampled; number of pathways with $P$-values $\leq .01$; and number of such pathways in agreement.


small $P$-values $(.009, .002)$. We note that they share a common gene fanca and that they involve the only gene fance exhibiting differential expression. The correlation patterns within the two samples are otherwise similar, suggesting a specific alteration of the network model.

The situation differs for the pathway MAP00252 Alanine and aspartate metabolism, summarized in Table 2 using the same analysis. The change in correlation is more widespread. The 8 gene pairs with the highest correlation magnitudes within the $N G T$ sample differ between $N G T$ and $D M T$ at a 0.05 significance level. Furthermore, the number of gene pairs with correlation magnitudes exceeding 0.7 is 9 in the $N G T$ sample, but only 3 in the $D M T$ sample.
5.1.3. Comparison of Fixed and Stopped Procedures. Both the fixed and stopped procedures were applied to the preceding analysis. The SPRT used parameters $A=0, B=99.9$, $\theta_{0}=0.05, \theta_{1}=0.07$, and truncation at $M=5000$. Table 3 summarizes the computation times for each method as well as the selection agreement. In these examples, the stopped procedure required significantly less computation time with no apparent loss in power.

## 6. Conclusion

We have introduced a two-sample general likelihood ratio test for the equality of Bayesian network models. Significance levels are estimated using a permutation procedure. The algorithm was proposed as an alternative form of gene-set analysis. It was noted that the fitting of Bayesian networks is computationally time consuming, hence a need for the efficient calculation of a model fit was identified, particularly for this application.

Two procedures were introduced to meet this requirement. First, we implemented a version of a minimum spanning tree algorithm first proposed in [15] which permits the polynomial-time calculation of the maximum likelihood Bayesian network among those with maximum indegree of one. Second, we introduced sequential testing principles to the problem of multiple testing, finding that a straightforward stopping rule could be developed which preserves group error rates for a wide range of procedures.

We may expect this form of test to be especially sensitive to changes in coexpression patterns, in contrast to most geneset procedures, which directly measure aggregate differential expression. In an application of the algorithm to two data sets considered in [5], a number of selected gene-sets exhibited clear differences in coexpression patterns while exhibiting very little differential expression. This leads to the conjecture
that the optimal approach to gene-set analysis is to couple a test which directly measures aggregate differential expression with one designed to detect differential coexpression.

## Acknowledgments

This paper was supported by NIH Grant no. R21HG004648. The Clinical Translational Science Institute of the University of Rochester Medical Center also provided funding for this research.

## Preliminary call for papers

The 2011 European Signal Processing Conference (EUSIPCO-2011) is the nineteenth in a series of conferences promoted by the European Association for Signal Processing (EURASIP, www.eurasip.org). This year edition will take place in Barcelona, capital city of Catalonia (Spain), and will be jointly organized by the Centre Tecnològic de Telecomunicacions de Catalunya (CTTC) and the Universitat Politècnica de Catalunya (UPC).
EUSIPCO-2011 will focus on key aspects of signal processing theory and applications as listed below. Acceptance of submissions will be based on quality, relevance and originality. Accepted papers will be published in the EUSIPCO proceedings and presented during the conference. Paper submissions, proposals for tutorials and proposals for special sessions are invited in, but not limited to, the following areas of interest.

## Areas of Interest

- Audio and electro-acoustics.
- Design, implementation, and applications of signal processing systems.
- Multimedia signal processing and coding.
- Image and multidimensional signal processing.
- Signal detection and estimation.
- Sensor array and multi-channel signal processing.
- Sensor fusion in networked systems.
- Signal processing for communications.
- Medical imaging and image analysis.
- Non-stationary, non-linear and non-Gaussian signal processing.


## Submissions

Procedures to submit a paper and proposals for special sessions and tutorials will be detailed at www.eusipco2011.org. Submitted papers must be camera-ready, no more than 5 pages long, and conforming to the standard specified on the EUSIPCO 2011 web site. First authors who are registered students can participate in the best student paper competition.

## Important Deadlines:


Organizing Committee
Honorary Chair
Miguel A. Lagunas (CTTC)
General Chair
Ana I. Pérez-Neira (UPC)
General Vice-Chair
Carles Antón-Haro (CTTC)
Technical Program Chair
Xavier Mestre (CTTC)
Technical Program Co-Chairs
Javier Hernando (UPC)
Montserrat Pardàs (UPC)
Plenary Talks
Ferran Marqués (UPC)
Yonina Eldar (Technion)
Special Sessions
Ignacio Santamaría (Unversidad
de Cantabria)
Mats Bengtsson (KTH)
Finances
Montserrat Nàjar (UPC)
Tutorials
Daniel P. Palomar
(Hong Kong UST)
Beatrice Pesquet-Popescu (ENST)
Publicity
Stephan Pfletschinger (CTTC)
Mònica Navarro (CTTC)
Publications
Antonio Pascual (UPC)
Carles Fernández (CTTC)
Industrial Liaison \& Exhibits
Angeliki Alexiou
(University of Piraeus)
Albert Sitja (CTTC)
International Liaison
Ju Liu (Shandong University-China)
Jinhong Yuan (UNSW-Australia)
Tamas Sziranyi (SZTAKI -Hungary)
Rich Stern (CMU-USA)
Ricardo L. de Queiroz (UNB-Brazil)
![img-3.jpeg](img-3.jpeg)

Webpage: www.eusipco2011.org