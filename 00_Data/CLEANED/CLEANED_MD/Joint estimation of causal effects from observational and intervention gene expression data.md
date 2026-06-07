# Joint estimation of causal effects from observational and intervention gene expression data 

Andrea Rau ${ }^{1,2^{*}}$, Florence Jaffrézic ${ }^{1,2}$ and Grégory Nuel ${ }^{3,4}$


#### Abstract

Background: In recent years, there has been great interest in using transcriptomic data to infer gene regulatory networks. For the time being, methodological development in this area has primarily made use of graphical Gaussian models for observational wild-type data, resulting in undirected graphs that are not able to accurately highlight causal relationships among genes. In the present work, we seek to improve the estimation of causal effects among genes by jointly modeling observational transcriptomic data with arbitrarily complex intervention data obtained by performing partial, single, or multiple gene knock-outs or knock-downs.


Results: Using the framework of causal Gaussian Bayesian networks, we propose a Markov chain Monte Carlo algorithm with a Mallows proposal model and analytical likelihood maximization to sample from the posterior distribution of causal node orderings, and in turn, to estimate causal effects. The main advantage of the proposed algorithm over previously proposed methods is its flexibility to accommodate any kind of intervention design, including partial or multiple knock-out experiments. Using simulated data as well as data from the Dialogue for Reverse Engineering Assessments and Methods (DREAM) 2007 challenge, the proposed method was compared to two alternative approaches: one requiring a complete, single knock-out design, and one able to model only observational data.
Conclusions: The proposed algorithm was found to perform as well as, and in most cases better, than the alternative methods in terms of accuracy for the estimation of causal effects. In addition, multiple knock-outs proved to contribute valuable additional information compared to single knock-outs. Finally, the simulation study confirmed that it is not possible to estimate the causal ordering of genes from observational data alone. In all cases, we found that the inclusion of intervention experiments enabled more accurate estimation of causal regulatory relationships than the use of wild-type data alone.

Keywords: Causal inference, Gaussian Bayesian network, Intervention calculus, Metropolis-Hastings, Maximum likelihood

## Background

The inference of gene regulatory networks from transcriptomic data has been a wide research area in recent years. Several approaches have been proposed to infer networks from observational transcriptomic data (also referred to as wild-type or steady-state expression data), mainly based

[^0]on the use of graphical Gaussian models [1]. These methods, however, rely on the estimation of partial correlations and result in undirected graphs that cannot highlight the causal relationships among genes. For this reason, a great deal of research has focused instead on the use of causal Bayesian networks for a wide variety of applications $[2,3]$.

As an example, [4] and [5] make use of causal Bayesian networks in the case of multinomial data, where the former applies a score-based method and the latter samples graph structures using a Markov chain Monte


[^0]:    *Correspondence: andrea.rau@jouy.inra.fr
    ${ }^{1}$ INRA, UMR1313 Génétique animale et biologie intégrative, 78352
    Jouy-en-Josas, France
    ${ }^{2}$ AgroParisTech, UMR1313 Génétique animale et biologie intégrative, 75231 Paris 05, France
    Full list of author information is available at the end of the article

Carlo (MCMC) approach. Using Gaussian causal Bayesian networks (GBN), Maathuis et al. [6,7] recently proposed a method called Intervention-calculus when the DAG is Absent (IDA) to predict bounds for causal effects from observational data alone. In the IDA, the PC-algorithm [2,8,9] is first applied to find the associated completed partially directed acyclic graph (CPDAG), corresponding to the graphs belonging to the appropriate equivalence class. Following this step, bounds for total causal effects of each gene on the others are estimated using intervention calculus [10] for each directed acyclic graph (DAG) in the equivalence class.

However, if intervention experiments such as gene knock-outs or knock-downs are available, it is valuable to jointly perform causal network inference from a combination of wild-type and intervention data. One such approach has been proposed by Pinna et al. [11], based on the simple idea of calculating the deviation between observed gene expression values and the expression under each systematic intervention. In particular, Pinna et al. propose the calculation of several matrices to evaluate the differences between observational and intervention expression values: a simple deviation matrix, a standardized deviation matrix, and a z-score deviation matrix. In addition, for large networks (e.g., 100 genes), a down-ranking algorithm is applied to the initial graph obtained from these deviation matrices to remove feed-forward edges. In order to evaluate all possible causal links among genes, the method requires a single replicate of observational data as well as a single knock-out experiment for each gene in the network. An improved version of the Pinna approach was very recently proposed [12] to provide more accurate network inference for large-scale networks through a novel implemention of the transitive reduction step. As with the originally proposed method, this approach also requires systematic single knock-outs for all genes in the network.

The method proposed in [11] has the dual advantages of being very fast to compute and being quite general, as it does not require any assumption of acyclicity of the graph. In addition, as this method provided the best network estimation in the Dialogue for Reverse Engineering Assessments and Methods (DREAM4) in silico 100-gene network sub-challenge [13-16], it may be considered as a reference. We note that the method with the best performance for the DREAM4 10-gene network subchallenge was that of [17], based on an automated approach using Petri Nets with Fuzzy Logic; unfortunately, no software is publicly available to implement this method, making it difficult to use in practice.

In this work we propose a novel method in the context of GBNs using a Markov chain Monte Carlo (MCMC) algorithm and Mallows model that is flexible enough to accurately infer causal gene networks from an arbitrary mixture of observational and intervention data, including partial and multiple gene knock-out experiments. As such, the novelty of the proposed method is as follows: 1) it is the only method able to fully make use of all available intervention information, 2) it does not require a systematic intervention experiment to be performed for each gene, and 3) it can deal with sophisticated multiple intervention designs. To benchmark its performance on observational data alone as well as systematic single knock-out data, the proposed method was compared to those of [7] and [11] on simulated data as well as the data from the DREAM4 challenge [13]; in addition, we also consider more complicated simulations based on partial and multiple knock-out designs.

## Methods

## Gaussian Bayesian network framework

Let $G=(V, E)$ be a graph defined by a set of vertices $V$ and edges $E \subset(V \times V)$. Let the vertices of a graph represent $p$ random variables $X_{1}, \ldots, X_{p}$. As in the approach of [7], we consider here the framework of causal GBNs, which correspond to Bayesian networks where the nodes have a Gaussian residual distribution and edges represent linear dependencies. In this case, it also follows that the joint distribution of the network is multivariate Gaussian.

In DAGs such as GBNs, we often encounter the presence of Markov equivalence classes, i.e. multiple network structures that yield the same joint distribution; in such cases, observational data alone generally cannot orient edges. For this reason, in many cases the use of intervention data can help overcome this issue, as presented below.

## Calculation of causal effects

Following an intervention on a given node $X_{i}$, denoted $\operatorname{do}\left(X_{i}=x\right)$, we consider the expected value of each other gene in the network via do-calculus as shown in Theorem 3.2.2 (Adjustment for direct causes) in [10]:

$$
\begin{aligned}
& \mathbb{E}\left(X_{j} \mid \operatorname{do}\left(X_{i}=x\right)\right) \\
& \quad=\left\{\begin{array}{ll}
\mathbb{E}\left(X_{j}\right) & \text { if } \quad X_{j} \in \operatorname{pa}\left(X_{i}\right) \\
\int \mathbb{E}\left(X_{j} \mid x, \operatorname{pa}\left(X_{i}\right)\right) \mathbb{P}\left(\operatorname{pa}\left(X_{i}\right)\right) d \operatorname{pa}\left(X_{i}\right) & \text { if } \quad X_{j} \notin \operatorname{pa}\left(X_{i}\right)
\end{array}\right.
\end{aligned}
$$

where $\operatorname{pa}\left(X_{i}\right)$ represents the parents of node $X_{i}$. It is important to point out that $\mathbb{P}(Y \mid \operatorname{do}(X=x))$ is different from the conditional probability $\mathbb{P}(Y \mid X=x)$. Using this framework, the total causal effects may be defined as follows:

$$
\beta_{i j}=\frac{\partial}{\partial x} \mathbb{E}\left(X_{j} \mid \operatorname{do}\left(X_{i}=x\right)\right)
$$

and are equal to 0 if $X_{i}$ is not an ancestor of $X_{j}$. On the other hand, the direct causal effects (i.e. the edges in the graph) are defined as:

$$
\alpha_{i j}=\frac{\partial}{\partial x} \mathbb{E}\left(X_{j} \mid \mathrm{pa}\left(X_{j}\right), \mathrm{do}\left(X_{i}=x\right)\right)
$$

## Proposed causal inference method

In the GBN framework, when observational data are jointly modeled with intervention data for an arbitrary subset of genes, the network follows a multivariate Gaussian distribution of dimension equal to the number of genes that had no intervention (as the expression value of the gene under intervention is fixed to a given value), and the log-likelihood value can subsequently be calculated for a proposed network.

The calculations in the following section assume that the nodes in the graph have been sorted according to an appropriate causal ordering in the graph such that if $i<j$, then $X_{j}$ is not an ancestor of $X_{i}$; we note that such an ordering is possible under the assumption of acyclicity of the graph. In practice, of course, it is typically not possible to correctly order nodes in such a way without knowledge of the underlying DAG. For this reason, we aim to explore various network structures based on causal orderings, and to choose among those with the best likelihood value for an arbitrary set of observational and intervention data. The Metropolis-Hastings algorithm [18,19], through the use of a proposal distribution for causal orderings, allows such an exploration to take place and to approach a local maximum of the likelihood.

## Likelihood calculation

Let $p$ be the number of nodes in the graph, $G$ the DAG structure and $\mathbf{W}$ the matrix containing the values for all edges. The nodes are assumed to have been sorted by parental order for $G$ and $\mathbf{W}$, i.e. if $i<j$, then $X_{j}$ is not an ancestor of $X_{i}$. This sorting is possible under the assumption of acyclicity and may not necessarily be unique. Under this ordering, $\mathbf{W}$ is an upper triangular matrix and thus nilpotent. In the GBN framework, it is assumed that each node of $G$ has a residual Gaussian distribution, independently from the rest of the network. Let us consider $X_{\mathcal{I}}$ with $\mathcal{I}=\{1, \ldots, p\}$, a set of $p$ Gaussian random variables defined by:

$$
X_{j}=m_{j}+\sum_{i \in \mathrm{pa}(j)} w_{i, j} X_{i}+\varepsilon_{j} \quad \text { with } \quad \varepsilon_{j} \sim \mathcal{N}\left(0, \sigma_{j}^{2}\right)
$$

We assume that the $\varepsilon_{j}$ are independent, and that $i \in$ $\mathrm{pa}(j) \Rightarrow i<j$ (this assumption is equivalent to assuming that the directed graph obtained using the parental relationships is acyclic). Given the parental structure of the graph, $w_{i, j}$ may only be nonzero on the edge set, $(i, j) \in$ $\mathcal{E}=\{i \in \mathrm{pa}(j), j \in \mathcal{I}\}$.

Let us now consider the matrix form of Equation (1):

$$
\mathbf{X}=\mathbf{m}+\mathbf{X} \mathbf{W}+\boldsymbol{\varepsilon}
$$

where $\mathbf{X}=\left(X_{1}, \ldots, X_{p}\right), \mathbf{m}=\left(m_{1}, \ldots, m_{p}\right)$, and $\boldsymbol{\varepsilon}=$ $\left(\varepsilon_{1}, \ldots, \varepsilon_{p}\right)$ are row-vectors of dimension $p$, and $\mathbf{W}=$ $\left(w_{i, j}\right)_{1 \leqslant i, j \leqslant p}$ is a $p$-dimensional square matrix. By recursively applying this formula and taking advantage of the nilpotence of matrix $\mathbf{W}$, we obtain:

$$
\mathbf{X}=\mathbf{m L}+\boldsymbol{\varepsilon} \mathbf{L}
$$

where $\mathbf{L}=(\mathbf{I}-\mathbf{W})^{-1}=\mathbf{I}+\mathbf{W}+\ldots+\mathbf{W}^{p-1}$. This proves that the model defined in Equation (1) is equivalent to $\mathbf{X} \sim$ $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with:

$$
\boldsymbol{\mu}=\mathbf{m L} \quad \text { and } \quad \boldsymbol{\Sigma}=\mathbf{L}^{T} \operatorname{diag}\left(\boldsymbol{\sigma}^{2}\right) \mathbf{L}=\sum_{j \in \mathcal{I}} \sigma_{j}^{2} \mathbf{L}^{T} \mathbf{e}_{j}^{T} \mathbf{e}_{j} \mathbf{L}
$$

where $\mathbf{e}_{j}$ is a $p$-dimensional null row-vector except for its $j^{\text {th }}$ term which is equal to 1 , and where $\boldsymbol{\sigma}=\left(\sigma_{1}, \ldots, \sigma_{p}\right)$ is a row-vector of dimension $p$.

The log-likelihood of the model given $N$ observations $\mathbf{x}^{k}=\left(x_{1}^{k}, \ldots, x_{p}^{k}\right)(1 \leqslant k \leqslant N)$ is then:

$$
\begin{aligned}
\ell(\mathbf{m}, \boldsymbol{\sigma}, \mathbf{W})= & -\frac{N p}{2} \log (2 \pi)-N \sum_{j \in \mathcal{I}} \log \left(\sigma_{j}\right) \\
& -\frac{1}{2} \sum_{k=1}^{N} \sum_{j \in \mathcal{I}} \frac{1}{\sigma_{j}^{2}}\left(x_{j}^{k}-\mathbf{x}^{k} \mathbf{W} \mathbf{e}_{j}^{T}-m_{j}\right)^{2}
\end{aligned}
$$

To see this, let us define $\mathbf{A}_{k}=\left(\mathbf{x}^{k}-\mathbf{m L}\right) \boldsymbol{\Sigma}^{-1}\left(\mathbf{x}^{k}-\mathbf{m L}\right)^{T}$ for all $k$. Since $\boldsymbol{\Sigma}^{-1}=(\mathbf{I}-\mathbf{W}) \operatorname{diag}\left(1 / \boldsymbol{\sigma}^{2}\right)(\mathbf{I}-\mathbf{W})^{T}$ we get:

$$
\begin{aligned}
\mathbf{A}_{k} & =\sum_{j \in \mathcal{I}} \frac{1}{\sigma_{j}^{2}}\left(\mathbf{x}^{k}(\mathbf{I}-\mathbf{W})-\mathbf{m}\right) \mathbf{e}_{j}^{T} \mathbf{e}_{j}\left(\mathbf{x}^{k}(\mathbf{I}-\mathbf{W})-\mathbf{m}\right)^{T} \\
& =\sum_{j \in \mathcal{I}} \frac{1}{\sigma_{j}^{2}}\left(x_{j}^{k}-\mathbf{x}^{k} \mathbf{W} \mathbf{e}_{j}^{T}-m_{j}\right)^{2}
\end{aligned}
$$

As shown in the Additional file 1, analytical formulae can be obtained for the derivatives with respect to parameters $\boldsymbol{\theta}=(\mathbf{m}, \boldsymbol{\sigma}, \mathbf{W})$.

The likelihood presented above only takes into account observational data. Let us now consider the case of an arbitrary mixture of observational and intervention data. We assume that we perform an intervention on a subset $\mathcal{J} \subset \mathcal{I}=\{1, \ldots, p\}$ of variables by artificially fixing the level of the corresponding variables to a value (typically 0 in the case of knock-out experiments): $\operatorname{do}\left(X_{\mathcal{J}}=x_{\mathcal{J}}\right)$. The model is then obtained by assuming that all $w_{i, j}=0$ for $(i, j) \in \mathcal{E}$ and $j \in \mathcal{J}$; we denote the corresponding matrix $\mathbf{W}_{\mathcal{J}}$. We also assume that the variables $X_{j}$ for $j \in \mathcal{J}$ are

fully deterministic. As before, the resulting model is hence Gaussian: $X_{\mathcal{I}} \mid \operatorname{do}\left(X_{\mathcal{J}}=x_{\mathcal{J}}\right) \sim \mathcal{N}\left(\boldsymbol{\mu}_{\mathcal{J}}\left(x_{\mathcal{J}}\right), \boldsymbol{\Sigma}_{\mathcal{J}}\right)$ with

$$
\boldsymbol{\mu}_{\mathcal{J}}\left(x_{\mathcal{J}}\right)=\boldsymbol{v}_{\mathcal{J}}\left(x_{\mathcal{J}}\right) \mathbf{L}_{\mathcal{J}}, \quad \boldsymbol{\Sigma}_{\mathcal{J}}=\sum_{j \notin \mathcal{J}} \sigma_{j}^{2} \mathbf{L}_{\mathcal{J}}^{T} \mathbf{e}_{j}^{T} \mathbf{e}_{j} \mathbf{L}_{\mathcal{J}}
$$

where

$$
\begin{aligned}
& \boldsymbol{v}_{\mathcal{J}}\left(x_{\mathcal{J}}\right) e_{j}^{T} \\
& =\left\{\begin{array}{l}
x_{j} \text { if } j \in \mathcal{J} \\
m_{j} \text { otherwise }
\end{array} \text { and } \mathbf{L}_{\mathcal{J}}=\left(\mathbf{I}-\mathbf{W}_{\mathcal{J}}\right)^{-1}=\mathbf{I}+\mathbf{W}_{\mathcal{J}}+\ldots+\mathbf{W}_{\mathcal{J}}^{p-1}\right.
\end{aligned}
$$

For the likelihood calculation, we consider $N$ data generated under $x^{k}=\left(x_{1}^{k}, \ldots, x_{p}^{k}\right)(1 \leqslant k \leqslant N)$ with intervention on $\mathcal{J}_{k}$ (where $\mathcal{J}_{k}=\emptyset$ means no intervention). We denote by $\mathcal{K}_{j}=\left\{k, j \notin \mathcal{J}_{k}\right\}$, and by $N_{j}=\left|\mathcal{K}_{j}\right|$ its cardinal. The log-likelihood of the model can then be written as:

$$
\begin{aligned}
\ell(\mathbf{m}, \boldsymbol{\sigma}, \mathbf{W})= & -\frac{\log (2 \pi)}{2} \sum_{j} N_{j}-\sum_{j} N_{j} \log \left(\sigma_{j}\right) \\
& -\frac{1}{2} \sum_{k} \sum_{j \notin \mathcal{J}_{k}} \frac{1}{\sigma_{j}^{2}}\left(x_{j}^{k}-\mathbf{x}^{k} \mathbf{W e}_{j}^{T}-m_{j}\right)^{2}
\end{aligned}
$$

This is mainly due to the fact that for any intervention set $\mathcal{J}$ we have $\mathbf{W}_{\mathcal{J}} \mathbf{e}_{j}^{T}=\mathbf{W e}_{j}^{T}$ for all $j \notin \mathcal{J}$. Considering the derivative with respect to $m_{j}$ for all $j$ such that $N_{j}>0$, we obtain:

$$
m_{j}=\frac{1}{N_{j}} \sum_{k \in \mathcal{K}_{j}}\left(x_{j}^{k}-\mathbf{x}^{k} \mathbf{W e}_{j}^{T}\right)
$$

which can be plugged into the likelihood expression to get:

$$
\begin{aligned}
\tilde{\ell}(\boldsymbol{\sigma}, \mathbf{W})= & -\frac{\log (2 \pi)}{2} \sum_{j} N_{j}-\sum_{j} N_{j} \log \left(\sigma_{j}\right) \\
& -\frac{1}{2} \sum_{k} \sum_{j \notin \mathcal{J}_{k}} \frac{1}{\sigma_{j}^{2}}\left(y_{j}^{k, j}-\mathbf{y}^{k, j} \mathbf{W e}_{j}^{T}\right)^{2}
\end{aligned}
$$

where for $(k, j)$ such that $j \notin \mathcal{J}_{k}$ we have:

$$
\mathbf{y}^{k, j}=\mathbf{x}^{k}-\frac{1}{N_{j}} \sum_{k^{\prime} \in \mathcal{K}_{j}} \mathbf{x}^{k^{\prime}}
$$

and $\mathbf{W}$ can be estimated by solving the following linear system:

$$
\sum_{i^{\prime},(i^{\prime}, j) \in \mathcal{E}} w_{i^{\prime}, j} \sum_{k \in \mathcal{K}_{j}} y_{i}^{k, j} y_{i^{\prime}}^{k, j}=\sum_{k \in \mathcal{K}_{j}} y_{i}^{k, j} y_{j}^{k, j} \quad \text { for all }(i, j) \in \mathcal{E}
$$

Note that the system might be degenerate if the intervention design gives no insight on some parameters. It is hence finally possible to obtain $\boldsymbol{\sigma}$ through:

$$
\sigma_{j}^{2}=\frac{1}{N_{j}} \sum_{k \in \mathcal{K}_{j}}\left(y_{j}^{k, j}-\mathbf{y}^{k, j} \mathbf{W e}_{j}^{T}\right)^{2}
$$

## Proposed MCMC algorithm

The Metropolis-Hastings algorithm [18,19] is a random walk over $\Omega$, the parameter space of the model. It relies on an instrumental probability distribution $Q$ which defines the transition from position $X_{t}$ to a new position $X$. The probability of moving from state $X_{t}$ to the new state $X$ is defined by:

$$
P\left(X_{t+1}=X \mid X_{t}\right)=\min \left\{\frac{\pi(X) Q\left(X_{t}, X\right)}{\pi\left(X_{t}\right) Q\left(X, X_{t}\right)}, 1\right\}
$$

where $\pi(X)$ is the likelihood function.
In order to propose a new causal node ordering $\mathcal{O}^{\star}$ from the previous ordering $\mathcal{O}$, we propose to make use of the Mallows model [20]. Briefly, under this model, the density of a proposed causal ordering is defined as follows:

$$
\begin{aligned}
P\left(\mathcal{O}^{\star}\right) & =P\left(\mathcal{O}^{\star} \mid \mathcal{O}, \phi\right) \\
& =\frac{1}{Z} \phi^{d\left(\mathcal{O}^{\star}, \mathcal{O}\right)}
\end{aligned}
$$

where $\phi \in(0,1]$ is a fixed temperature parameter, $Z$ is a normalizing constant, and $d(\cdot, \cdot)$ is a dissimilarity measure between $\mathcal{O}$ and $\mathcal{O}^{\star}$ based on the number of pairwise ranking disagreements. In addition, we remark that as the temperature parameter $\phi$ approaches zero, the Mallows model approaches a uniform distribution over all causal orderings, and if $\phi=1$, the model corresponds to a dirac distribution on the reference ordering $\mathcal{O}$. In the following, we will use a reparameterization of the temperature coefficient $\phi$ such that $\phi=\exp (-1 / \eta)$, with $\eta>0$. Due to the symmetry of $d$, it is clear that $P\left(\mathcal{O}^{\star} \mid \mathcal{O}, \phi\right)=P\left(\mathcal{O} \mid \mathcal{O}^{\star}, \phi\right)$, which allows a simplification of the $Q$ terms in the acceptance ratio in Equation (4). We note that a related MCMC approach to explore the space of causal node orderings was recently proposed by [5] in the case of categorical data, making use of an equi-energy sampler.
Proposals for causal node orderings using the aforementioned Mallows model may be obtained by sampling using a repeated insertion model as described in [21]. Based on this new proposal for the node ordering $\mathcal{O}^{\star}$, maximum likelihood estimators may be calculated for the model parameters $\boldsymbol{\theta}=(\mathbf{m}, \boldsymbol{\sigma}, \mathbf{W})$ using the likelihood described in Equation (2). Subsequently, the MetropolisHastings ratio may be calculated and used to determine whether the proposed causal node ordering is accepted or rejected.
R code to implement the proposed MCMC-Mallows algorithm, as well as a sample script providing an example to run the algorithm for a set of simulated data, may be found in Additional files 2 and 3.

## Results and discussion

## Simulation study

Data were simulated under a GBN as in Equation (1) with 10 genes and 21 edges and as described in [9]; the

underlying structure is given in Figure 1. For the residual distributions of each gene, we chose 0.5 for the means and three settings for the standard deviations (σ = 0.01, 0.1 and 0.5), which correspond to small, moderate and large noise for the marginal distributions. Non-zero parameters w_{i,j} were simulated with values drawn uniformly from (-1, -0.25) ∪ (0.25, 1), and for each setting, 100 datasets were generated. The goal was to try to accurately infer the total and direct causal effects among genes.

Several intervention designs were simulated: 1) 20 observational (wild-type) replicates with no interventions, 2) a mixed setting with 10 wild-types and one knock-out per gene, 3) a partial knock-out design with 15 wild-types and one knock-out for five genes: {N1, N4, N6, N7, N9}, 4) a multiple knock-out design with 10 wild types, one knock-out per gene and five double knock-outs: {N1, N5}, {N1, N6}, {N4, N7}, {N6, N9}, and {N7, N10} and 5) a multiple knock-out design as in the previous setting, where all simulated data for three randomly chosen genes were removed (resulting in a set of three hidden variables). Note that we have previously shown [22] that observational data alone (Setting 1 described above) are not informative for the causal node ordering as in such a case, the likelihood is invariant to permutations of the order. Consequently, in this setting node orderings were uniformly sampled rather

![img-0.jpeg](img-0.jpeg)

**Figure 1** Graph structure used in simulation study. Graph structure taken from [9] used for the simulation study for a graph with ten nodes and 21 edges.

than using the MCMC-Mallows algorithm; we refer to this strategy as MCMC-uniform.

An MCMC algorithm with Mallows proposal distribution was run to explore the posterior distribution of causal node orderings, as presented in the previous section, with full estimation of θ = (m, σ, W) using the maximum likelihood estimators. For the simulations, a small trial run of 1000 iterations was run over a range of possible temperature values η (0.2 to 1.5 by 0.1) for the Mallows model, and the value yielding an acceptance rate closest to 30 to 40% [23] was subsequently used for the full run of the MCMC algorithm. In all simulation settings tested here, this value was chosen to be η = 0.6 (for σ = 0.01 and 0.1) or η = 1 (for σ = 0.5). As a comparison, we also attempted a trial run of the algorithm using a naive uniform proposal distribution (η = 10^{10}) in place of the Mallows model, which generally led to acceptance rates of less than 1%. The MCMC-Mallows algorithm was subsequently run for 50,000 iterations, including a burn-in of 5000 iterations and thinning every 50 iterations. We note that due to the analytical maximization step of the likelihood, the method is quite fast and takes only a few minutes to run for each dataset.

In order to benchmark its performance on observational data alone as well as systematic single knock-out data, the proposed algorithm was compared to two previously proposed methods: 1) Pinna [11], which requires a single, systematic knock-out to be performed for every gene, and 2) IDA [7] using the PC-algorithm [2], which only makes use of the observational data. As the PC-algorithm used by [7] provides bounds (a, b) for the estimated causal effects, we considered two options to facilitate comparisons with the other methods: an "optimistic" calculation, where we use the value max(abs(a, b)), and a more conservative "pessimistic" strategy, using the value min(abs(a, b)) if a and b have the same sign, 0 otherwise.

Finally, several criteria were used to compare the different methods on both total causal effects and direct causal effects: area under the receiver operating characteristic (ROC) curve (AUROC), area under the precision-recall curve (AUPRC), Spearman correlation between true and estimated total or direct causal effects, and the mean squared error (MSE) of estimated total or direct causal effects. Note that the results are calculated for the full L = (I - W)^{-1} (total causal effects) and W matrices (direct causal effects) and not just the upper triangular. For the AUROC and AUPRC calculations, positive edges corresponded to (total or direct) causal effects with a nonzero value, and negatives corresponded to (total or direct) causal effects with a null value.

Results for total causal effects are presented in Table 1 for σ = 0.1, and in Tables S1 and S2 in Additional file 1 for σ = 0.01 and 0.5. It can first be noted that results for the IDA method are identical for different levels of

Table 1 Comparison of methods for total causal effects for simulated data with moderate variability ( $\sigma=0.1$ )


Several intervention designs were simulated: 1) 20 observational (wild-type) replicates with no interventions, 2) mixed setting with 10 wild-types and one knock-out per gene, 3) partial knock-out design with 15 wild-types and one knock-out for five genes (N1, N4, N6, N7, N9), 4) multiple knock-out design with 10 wild types, one knock-out per gene and five double knock-outs: (N1, N5), (N1, N6), (N4, N7), (N6, N9), and (N7, N10), and 5) a multiple knock-out design as in the previous setting, with three hidden variables. Results were averaged over 100 simulations (standard deviations in parentheses): area under the ROC curve (AUROC), area under the precision-recall curve (AUPRC), Spearman correlation between true and estimated total causal effects, and mean squared error (MSE) of estimated total causal effects. variation $\sigma$; this is due to the fact that it operates on sufficient statistics (correlation matrices) rather than on the data themselves. Similarly, results are identical for the MCMC-uniform method at different levels of $\sigma$ when only observational data are present. Based on observational data only, we note that the proposed algorithm performs as well as the IDA approach; this is unsurprising as both methods are based on GBNs.

When single knock-outs were simulated (one for each gene) with a large variability ( $\sigma=0.5$ ), the IDA [7] approach has slightly more accurate estimation of causal effects than Pinna [11], although we recall that the former method solely makes use of the observational data. On the other hand, when the amount of variability decreases ( $\sigma=$ 0.1 and 0.01 ), the Pinna approach outperforms IDA, even for the optimistic version. In all three settings ( $\sigma=0.5$, $0.1,0.01$ ), the proposed MCMC-Mallows algorithm was better able to estimate the causal effects than either Pinna or IDA, as shown by the different criteria presented here. Similar conclusions may be obtained in the context of partial intervention designs. The MCMC-Mallows approach was found to outperform the IDA approach, especially for moderate and low variability. As it requires knock-outs to be performed for all genes in the network, the performance of the Pinna approach suffers when only a subset of interventions are available.

In addition, it was found that considering multiple knock-outs led to an improvement of the estimation of the causal effects over single knock-outs alone. We note that, like the partial knock-out design, this complex intervention design can only be fully accommodated by the proposed MCMC-Mallows method. In this setting, the Pinna method uses only information on the 10 single knockouts and the IDA approach only the observational data. Finally, in the multiple knock-out setting where data for three genes were hidden, resulting in a set of latent variables, we note that the MCMC-Mallows approach appears to be least affected by the missing information and maintains a satisfactory performance. Similar conclusions may be drawn concerning the comparisons among methods for the direct total causal effects, shown in Table 2 and Tables S3 and S4 in Additional file 1.

Figure 2 presents the posterior distribution of causal node ordering from the MCMC-Mallows method ave-

Table 2 Comparison of methods for direct causal effects for simulated data with moderate variability ( $\sigma=0.1$ )


Several intervention designs were simulated: 1) 20 observational (wild-type) replicates with no interventions, 2) mixed setting with 10 wild-types and one knock-out per gene, 3) partial knock-out design with 15 wild-types and one knock-out for five genes (N1, N4, N6, N7, N9), 4) multiple knock-out design with 10 wild types, one knock-out per gene and five double knock-outs: (N1, N5), (N1, N6), (N4, N7), (N6, N9), and (N7, N10), and 5) a multiple knock-out design as in the previous setting, with three hidden variables. Results were averaged over 100 simulations (standard deviations in parentheses): area under the ROC curve (AUROC), area under the precision-recall curve (AUPRC), Spearman correlation between true and estimated direct causal effects, and mean squared error (MSE) of estimated direct causal effects. raged over 100 simulations for the observation data only (top left), the mixed setting with 10 wild types and one knock-out for each gene (top right), the partial knock-out setting (bottom left), and the multiple knock-out setting (bottom right) for moderately noisy data ( $\sigma=0.1$ ). Note that a plot is not included for the hidden variable design, as the true and estimated node orderings are dependent on which three genes are selected to be removed. In these plots, node labels are included on the vertical axis, and estimated positions within orderings along the horizontal axis. Potential orderings for each node within the true graph are highlighted with black outlines; as an example, node N6 could be placed in the first, second, or third position, while node N3 could only be placed in the tenth position in the true graph. The intensity of colors within each box represents the average proportion of iterations in which a node was placed in a particular order. To follow our example, in the mixed setting (top right of Figure 2), on average node N6 was most often placed in the first position, and occasionally positioned second or third, while node N3 was nearly always placed in the last position.

We may remark on several points. First, as shown in the Methods section, it is not possible to estimate the node orders from observational data only. As expected, the node orders were more accurately estimated when a complete knock-out design was considered, with one knock-out for each gene, than for a partial knock-out design. For low to medium variability ( $\sigma=0.01$ and 0.1 ) the proposed algorithm was able to very accurately estimate the potential node orders for the complete and multiple knock-out designs (see Figures S1-S4 in Additional file 1). Finally, we note that the node ordering is not unique for the DAG considered here, as illustrated by the black squares in Figure 2.

## DREAM data analysis

The proposed MCMC-Mallows algorithm as well as the two previously presented methods $[7,11]$ were applied to data from the DREAM4 challenge, an international competition held yearly to contribute to the development of powerful inference methods [13-16]. In the DREAM4 in silico network challenge, network topologies (with feedback loops) were extracted from transcriptional regula-

![img-1.jpeg](img-1.jpeg)

**Figure 2 Posterior distribution of node orders from the MCMC-Mallows approach, averaged over 100 simulations.** Results from simulation setting with σ = 0.1: Observations only (top left), complete single knock-outs (top right), partial single knock-outs (bottom left), multiple knock-outs (bottom right). Node labels are included on the vertical axis, estimated positions within causal orderings along the horizontal axis, and the intensity of color of each square corresponds to the average proportion of iterations in which a given node was placed in a given position. As the causal node ordering is not unique for this DAG, true potential positions for each node are outlined in black.

The network is composed of a network of *E. coli* and *S. cerevisiae*, and data were subsequently simulated and distributed to the participants. The goal was to infer directed regulatory networks from simulated data with either 10 or 100 genes. Based on the considered evaluation criteria (AUROC and AUPRC), the Petri Nets with Fuzzy Logic method [17] and Pinna method [11] were found to be the best performers for the 10-gene and 100-gene network challenges, respectively. In this paper we will focus on the five simulated 10-gene networks and perform inference based on wild type and multifactorial perturbation data (jointly considered to be observational data) as well as knock-out data.

Figure 3 presents the ROC curves as well as the precision-recall curves for the different methods in each of the five DREAM4 datasets. Table 3 contains the values for the AUROC and AUPRC for each method on each of the five DREAM4 datasets, as well as the overall DREAM score for each. The overall DREAM score is calculated

![img-2.jpeg](img-2.jpeg)

**Figure 3 Comparison of methods on data with a complete design from the DREAM4 challenge.** ROC curves (top) and precision-recall curves (bottom) for the five simulated 10-gene networks of the DREAM4 challenge [13] for the MCMC-Mallows, Pinna, and IDA (optimistic and pessimistic) methods.

culated as the average of global AUROC and AUPR scores, which are calculated across all datasets as the mean of the $-\log_{10} p$-values (calculated via permuation tests) for each dataset. As a point of reference, the reported performance of the top-performing method from the DREAM4 challenge, Petri Nets with Fuzzy Logic [17], is also provided; we could not confirm these results as no software is publicly available for its implementation.

Nets | MCMC-
Mallows | Pinna | IDA
(opt) | IDA
(pes)  |

**Table 3 Comparison of methods on complete DREAM4 data**

Area under the ROC curve (AUROC), area under the precision-recall curve (AUPRC), and DREAM score for each of the five DREAM datasets for the Petri Nets [17], MCMC-Mallows, Pinna *et al*., and IDA (optimistic and pessimistic) methods. Results for the Petri Nets method [17] and evaluation scripts for the overall DREAM score were obtained from the DREAM4 evaluation page, located at http://wiki.c2b2.columbia.edu/dream/results/DREAM4.

It can first be observed that the IDA [7], whether optimistic or pessimistic versions of the causal effects estimations are used, performs the worst; this is unsurprising, as it only makes use of the observational data. On the other hand, the proposed MCMC-Mallows method compares quite well to the Pinna approach, except for the first data set where Pinna clearly outperforms the others. We note that the simulated intervention setting was well adapted to the Pinna method, as one knockout was available for each gene; in addition, we note that as the MCMC-Mallows and IDA methods are based on a causal Bayesian network framework, feedback loops in the network cannot be modeled due to the assumption of acyclicity in the graph. Finally, it can be seen that the Petri Nets method of [17] significantly outperforms the other methods on these data; however, we recall that the major contribution of our proposed MCMC-Mallows approach is not its ability to best model complete, single knock-out intervention designs but rather its unique flexibility to accommodate more complex or incomplete intervention designs, as we demonstrate in the following.

To assess the performance of each of the methods on the DREAM4 data with only an incomplete set of gene knock-out experiments (similar to the partial knock-out simulation above), we remove half of the knock-out experiments (chosen at random) from each dataset. Figure 4 presents the ROC and precision-recall curves for this partial knock-out setting and Table 4 provides the AUROC, AUPRC, and overall DREAM scores. As no software is publicly available to implement the Petri Nets approach,

![img-3.jpeg](img-3.jpeg)

**Figure 4 Comparison of methods on data with a partial design from the DREAM4 challenge.** ROC curves (top) and precision-recall curves (bottom) for the five simulated 10-gene networks of the DREAM4 challenge [13], where for each dataset five knock-outs were removed at random, for the MCMC-Mallows, Pinna, and IDA (optimistic and pessimistic) methods.

No results for this method may be obtained in this context. The performance of IDA is identical in this setting to that of the full data, as it uses the observational data alone. The loss of information as compared to the complete data is reflected in the lower overall DREAM scores for both the MCMC-Mallows and Pinna approaches; we note that in nearly all cases (with the exception of the second dataset), the Pinna method is adversely affected by the loss of intervention data as compared to the previous results. On the other hand, the MCMC-Mallows appears to be the least adversely affected by the incomplete design and maintains a similar performance to the complete design. As such, although the complete intervention design clearly yields more information about causal effects among genes, the MCMC-Mallows approach appears to be best able to extract pertinent information when only partial intervention designs are available.


**Table 4 Comparison of methods on partial DREAM4 data**

Area under the ROC curve (AUROC), area under the precision-recall curve (AUPRC), and DREAM score for each of the five DREAM4 partial datasets, where only five of the single-gene knock-outs are included, for the MCMC-Mallows, Pinna et al., and IDA (optimistic and pessimistic) methods. Results for the Petri Nets method [17] are not provided as no software is publicly available to implement this approach. Evaluation scripts for the overall DREAM score were obtained from the DREAM4 evaluation page, located at http://wiki.c2b2.columbia.edu/dream/results/DREAM4.

### Conclusions

In this paper we proposed a flexible and powerful approach for joint causal network inference from both observational and intervention data, using an MCMC algorithm and Mallows model. The computational efficiency of the method is very much improved by the analytical maximization step of the likelihood.

In the simulation study presented above, the proposed MCMC-Mallows algorithm was found to perform better than Pinna [11] and IDA [7] in terms of accuracy of estimation of the causal effects, as evidenced by the tendency to have larger AUROC, larger Spearman correlation coefficients and smaller MSE than the other approaches. Additionally, our simulations demonstrated that multiple knock-out designs contributed valuable additional information for causal network inference beyond single knock-outs; we therefore anticipate that the need for methods able to accommodate complex intervention designs will only increase as such data become more common. The results for the complete DREAM4 data are somewhat inconclusive, with Pinna performing best on two datasets,

MCMC-Mallows best on two others, and nearly equivalent performance on the last; in addition, all methods considered here performed considerably worse than the winning Petri Nets method of [17] on the complete set of data. We note that the DREAM networks, like many real biological networks, contain feedback loops that cannot be modeled by methods based on causal Bayesian networks such as MCMC-Mallows and IDA. However, despite this limitation, the results of the partial design for DREAM4 data demonstrate that the MCMC-Mallows method is best able to accommodate complex intervention designs, including partial gene knock-outs. In fact, the novelty of the MCMC-Mallows approach, and the primary contribution of this work, lies in its flexibility to model arbitrary single, multiple, and partial knock-out designs.

In its present form, the proposed algorithm is not applicable to large-scale networks made up of several hundreds of nodes. Due to the curse of dimensionality, the size of the search space of causal node orderings explodes in dimension as the number of nodes increases, meaning that alternative MCMC samplers, such as parallel tempering, may be better suited to such situations. In addition, the resolution of the linear system in Equation (3) needed for the likelihood calculation has complexity $O\left(p^{6}\right)$ when no sparsity constraints are included for matrix $\mathbf{W}$. As such, the generalization of the proposed algorithm to a $p>>n$ situation will require the addition of a ridge or Lasso penalty, as recently proposed by [24], as well as a modification of the proposal distribution and sampling strategy. The current algorithm is fully compatible with such extensions and this will be the focus of our research in the near future.

The choice of optimal experimental knock-out designs is an important issue for causal inference and merits further attention. Hauser and Bühlmann [25] recently proposed two strategies for the choice of optimal interventions. The first is a greedy approach using single-vertex interventions that maximizes the number of edges that can be oriented after each intervention; the second yields a minimum set of targets of arbitrary size that guarantee full identifiability. However, alternative approaches could be envisaged in future research. In particular, recall that in the GBN framework, the likelihood associated to the multivariate Gaussian distribution of the network can be explicitly written as presented in this work. The choice of optimal knock-outs to be performed to improve and validate the causal inference can then rely on the evaluation of the amount of information contributed by each possible intervention, which can for example be obtained by the Fisher information. Its calculation requires the derivation of the likelihood function, which is not trivial but has already been derived in [22]. We anticipate that this issue will remain an interesting challenge for future research.

## Additional files

Additional file 1: Supplementary materials. This file contains details for calculations as well as additional results from the simulation study presented in the main paper.
Additional file 2: R code to implement MCMC-Mallows approach. This file contains the R code to implement the proposed MCMC-Mallows approach.
Additional file 3: Example R code to run MCMC-Mallows approach. This file contains the R code to run the proposed MCMC-Mallows approach for a set of simulated data.

## Competing interests

The authors declare that they have no competing interests.

## Authors' contributions

All participated in the design of the study, performed simulations and data analyses, and helped draft the manuscript. FJ participated in the design of the study and drafted the manuscript. GN designed the study, performed the analytical likelihood calculations and helped draft the manuscript. All authors read and approved the final manuscript.

## Acknowledgements

We thank Rèmi Barical for his work during his master internship, as well as the editor and two anonymous reviewers for their helpful comments and suggestions. GN received financial support from the Sorbonne Paris Cité IDEX grant "SA-flex."

## Author details

${ }^{1}$ INRA, UMR1313 Génétique animale et biologie intégrative, 78352 Jouy-en-Josas, France. ${ }^{2}$ AgroParisTech, UMR1313 Génétique animale et biologie intégrative, 75231 Paris 05, France. ${ }^{3}$ MAPS, UMR CNRS 8145, University Paris Descartes, 45 rue des Saints-Pères, F-75006 Paris, France. ${ }^{4}$ Sorbonne Paris Cité, Paris, France.

Received: 30 July 2013 Accepted: 7 October 2013
Published: 31 October 2013

## Submit your next manuscript to BioMed Central and take full advantage of:

- Convenient online submission
- Thorough peer review
- No space constraints or color figure charges
- Immediate publication on acceptance
- Inclusion in PubMed, CAS, Scopus and Google Scholar
- Research which is freely available for redistribution

Submit your manuscript at www.biomedcentral.com/submit
(1) BioMed Central