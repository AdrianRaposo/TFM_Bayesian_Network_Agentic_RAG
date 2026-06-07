# Article 

## Entropy and the Kullback-Leibler Divergence for Bayesian Networks: Computational Complexity and Efficient Implementation

Marco Scutari (D)

Istituto Dalle Molle di Studi Sull'Intelligenza Artificiale (IDSIA), 6900 Lugano, Switzerland; scutari@bnlearn.com


#### Abstract

Bayesian networks (BNs) are a foundational model in machine learning and causal inference. Their graphical structure can handle high-dimensional problems, divide them into a sparse collection of smaller ones, underlies Judea Pearl's causality, and determines their explainability and interpretability. Despite their popularity, there are almost no resources in the literature on how to compute Shannon's entropy and the Kullback-Leibler (KL) divergence for BNs under their most common distributional assumptions. In this paper, we provide computationally efficient algorithms for both by leveraging BNs' graphical structure, and we illustrate them with a complete set of numerical examples. In the process, we show it is possible to reduce the computational complexity of KL from cubic to quadratic for Gaussian BNs.


Keywords: Bayesian networks; Shannon entropy; Kullback-Leibler divergence

## 1. Introduction

Bayesian networks [1] (BNs) have played a central role in machine learning research since the early days of the field as expert systems [2,3], graphical models [4,5], dynamic and latent variables models [6], and as the foundation of causal discovery [7] and causal inference [8]. They have also found applications as diverse as comorbidities in clinical psychology [9], the genetics of COVID-19 [10], the Sustainable Development Goals of the United Nations [11], railway disruptions [12] and industry 4.0 [13].

Machine learning, however, has evolved to include a variety of other models and reformulated them into a very general information-theoretic framework. The central quantities of this framework are Shannon's entropy and the Kullback-Leibler divergence. Learning models from data relies crucially on the former to measure the amount of information captured by the model (or its complement, the amount of information lost in the residuals) and on the latter as the loss function we want to minimise. For instance, we can construct variational inference [14], the Expectation-Maximisation algorithm [15], Expectation Propagation [16] and various dimensionality reduction approaches such as t-SNE [17] and UMAP [18] using only these two quantities. We can also reformulate classical maximumlikelihood and Bayesian approaches to the same effect, from logistic regression to kernel methods to boosting $[19,20]$.

Therefore, the lack of literature on how to compute the entropy of a BN and the Kullback-Leibler divergence between two BNs is surprising. While both are mentioned in Koller and Friedman [5] and discussed at a theoretical level in Moral et al. [21] for discrete BNs, no resources are available on any other type of BN. Furthermore, no numerical examples of how to compute them are available even for discrete BNs. We fill this gap in the literature by:

- Deriving efficient formulations of Shannon's entropy and the Kullback-Leibler divergence for Gaussian BNs and conditional linear Gaussian BNs.
- Exploring the computational complexity of both for all common types of BNs.

- Providing step-by-step numeric examples for all computations and all common types of BNs.

Our aim is to make apparent how both quantities are computed in their closed-form exact expressions and what is the associated computational cost.

The common alternative is to estimate both Shannon's entropy and the KullbackLeibler divergence empirically using Monte Carlo sampling. Admittedly, this approach is simple to implement for all types of BNs. However, it has two crucial drawbacks:

1. Using asymptotic estimates voids the theoretical properties of many machine learning algorithms: Expectation-Maximisation is not guaranteed to converge [5], for instance.
2. The number of samples required to estimate the Kullback-Leibler divergence accurately on the tails of the global distribution of both BNs is also an issue [22], especially when we need to evaluate it repeatedly as part of some machine learning algorithm. The same is true, although to a lesser extent, for Shannon's entropy as well. In general, the rate of convergence to the true posterior in Monte Carlo particle filters is proportional to the number of variables squared [23].
Therefore, efficiently computing the exact value of Shannon's entropy and the KullbackLeibler divergence is a valuable research endeavour with a practical impact on BN use in machine learning. To help its development, we implemented the methods proposed in the paper in our bnlearn R package [24].

The remainder of the paper is structured as follows. In Section 2, we provide the basic definitions, properties and notation of BNs. In Section 3, we revisit the most common distributional assumptions in the BN literature: discrete BNs (Section 3.1), Gaussian BNs (Section 3.2) and conditional linear Gaussian BNs (Section 3.3). We also briefly discuss exact and approximate inferences for these types of BNs in Section 3.4 to introduce some key concepts for later use. In Section 4, we discuss how we can compute Shannon's entropy and the Kullback-Leibler divergence for each type of BN. We conclude the paper by summarising and discussing the relevance of these foundational results in Section 5. Appendix A summarises all the computational complexity results from earlier sections, and Appendix B contains additional examples we omitted from the main text for brevity.

# 2. Bayesian Networks 

Bayesian networks (BNs) are a class of probabilistic graphical models defined over a set of random variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{N}\right\}$, each describing some quantity of interest, that are associated with the nodes of a directed acyclic graph (DAG) $\mathcal{G}$. Arcs in $\mathcal{G}$ express direct dependence relationships between the variables in $\mathbf{X}$, with graphical separation in $\mathcal{G}$ implying conditional independence in probability. As a result, $\mathcal{G}$ induces the factorisation

$$
\mathrm{P}(\mathbf{X} \mid \mathcal{G}, \Theta)=\prod_{i=1}^{N} \mathrm{P}\left(X_{i} \mid \Pi_{X_{i}}, \Theta_{X_{i}}\right)
$$

in which the global distribution (of $\mathbf{X}$, with parameters $\Theta$ ) decomposes into one local distribution for each $X_{i}$ (with parameters $\Theta_{X_{i}}, \bigcup_{\mathbf{X}} \Theta_{X_{i}}=\Theta$ ) conditional on its parents $\Pi_{X_{i}}$.

This factorisation is as effective at reducing the computational burden of working with BNs as the DAG underlying the BN is sparse, meaning that each node $X_{i}$ has a small number of parents $\left(\left|\Pi_{X_{i}}\right|<c\right.$, usually with $\left.c \in\right| 2,5\left|\right)$. For instance, learning BNs from data is only feasible in practice if this holds. The task of learning a BN $\mathcal{B}=(\mathcal{G}, \Theta)$ from a data set $\mathcal{D}$ containing $n$ observations comprises two steps:

$$
\underbrace{\mathrm{P}(\mathcal{G}, \Theta \mid \mathcal{D})}_{\text {learning }}=\underbrace{\mathrm{P}(\mathcal{G} \mid \mathcal{D})}_{\text {structure learning }} \cdot \underbrace{\mathrm{P}(\Theta \mid \mathcal{G}, \mathcal{D})}_{\text {parameter learning }}
$$

If we assume that parameters in different local distributions are independent [25], we can perform parameter learning independently for each node. Each $X_{i} \mid \Pi_{X_{i}}$ will have a low-dimensional parameter space $\Theta_{X_{i}}$, making parameter learning computationally

efficient. On the other hand, structure learning is well known to be both NP-hard [26] and NP-complete [27], even under unrealistically favourable conditions such as the availability of an independence and inference oracle [28]. However, if $\mathcal{G}$ is sparse, heuristic learning algorithms have been shown to run in quadratic time [29]. Exact learning algorithms, which have optimality guarantees that heuristic algorithms lack, retain their exponential complexity but become feasible for small problems because sparsity allows for tight bounds on goodness-of-fit scores and the efficient pruning of the space of the DAGs [30-32].

# 3. Common Distributional Assumptions for Bayesian Networks 

While there are many possible choices for the distribution of $\mathbf{X}$ in principle, the literature has focused on three cases.

### 3.1. Discrete BNs

Discrete BNs [25] assume that both $\mathbf{X}$ and the $X_{i}$ are multinomial random variables (The literature sometimes denotes discrete BNs as "dBNs" or "DBNs"; we do not do that in this paper to avoid confusion with dynamic BNs, which are also commonly denoted as "dBNs"). Local distributions take the form

$$
X_{i} \mid \Pi_{X_{i}} \sim \operatorname{Mul}\left(\pi_{i k \mid j}\right), \quad \pi_{i k \mid j}=\mathrm{P}\left(X_{i}=k \mid \Pi_{X_{i}}=j\right)
$$

their parameters are the conditional probabilities of $X_{i}$ given each configuration of the values of its parents, usually represented as a conditional probability table (CPT) for each $X_{i}$. The $\pi_{i k \mid j}$ can be estimated from data via the sufficient statistic $\left\{n_{i j k}, i=1, \ldots N ; j=1, \ldots, q_{i}\right.$; $k=1, \ldots, r_{i}\}$, the corresponding counts tallied from $\left\{X_{i}, \Pi_{X_{i}}\right\}$ using maximum likelihood, Bayesian or shrinkage estimators as described in Koller and Friedman [5] and Hausser and Strimmer [33].

The global distribution takes the form of an $N$-dimensional probability table with one dimension for each variable. Assuming that each $X_{i}$ takes at most $l$ values, the table will contain $|\operatorname{Val}(\mathbf{X})|=O\left(l^{N}\right)$ cells, where $\operatorname{Val}(\cdot)$ denotes the possible (configurations of the) values of its argument. As a result, it is impractical to use for medium and large BNs. Following standard practices from categorical data analysis [34], we can produce the CPT for each $X_{i}$ from the global distribution by marginalising (that is, summing over) all the variables other than $\left\{X_{i}, \Pi_{X_{i}}\right\}$ and then normalising over each configuration of $\Pi_{X_{i}}$. Conversely, we can compose the global distribution from the local distributions of the $X_{i}$ by multiplying the appropriate set of conditional probabilities. The computational complexity of the composition is $O\left(N I^{N}\right)$ because applying (1) for each of the $I^{N}$ cells yields

$$
\mathrm{P}(\mathbf{X}=\mathbf{x})=\prod_{i=1}^{N} \mathrm{P}\left(X_{i}=x_{i} \mid \Pi_{X_{i}}=\mathbf{x}_{\Pi_{X_{i}}}\right)
$$

which involves $N$ multiplications. As for the decomposition, for each node, we:

1. Sum over $N-\left|\Pi_{X_{i}}\right|-1$ variables to produce the joint probability table for $\left\{X_{i}, \Pi_{X_{i}}\right\}$, which contains $O\left(l^{\left|\Pi_{X_{i}}\right|+1}\right)$ cells. The value of each cell is the sum of $O\left(l^{N-\left|\Pi_{X_{i}}\right|-1}\right)$ probabilities.
2. Normalise the columns of the joint probability table for $\left\{X_{i}, \Pi_{X_{i}}\right\}$ over each of the $O\left(l^{\left|\Pi_{X_{i}}\right|}\right)$ configurations of values of $\Pi_{X_{i}}$, which involves summing $O(l)$ probabilities and dividing them by their total.
The resulting computational complexity is

$$
\underbrace{O\left(l^{\left|\Pi_{X_{i}}\right|+1} \cdot l^{N-\left|\Pi_{X_{i}}\right|-1}\right)}_{\text {marginalisation }}+\underbrace{O\left(l \cdot l^{\left|\Pi_{X_{i}}\right|}\right)}_{\text {normalisation }}=O\left(l^{N}+l^{\left|\Pi_{X_{i}}\right|+1}\right)
$$

for each node and $O\left(N I^{N}+l \sum_{i=1}^{N} l^{\left|\Pi_{X_{i}}\right|}\right)$ for the whole BN.

Example 1 (Composing and decomposing a discrete BN). For reasons of space, this example is presented as Example A1 in Appendix B.

# 3.2. Gaussian BNs 

Gaussian BNs [35] (GBNs) model $\mathbf{X}$ with a multivariate normal random variable $N\left(\boldsymbol{\mu}_{\mathcal{B}}\right.$, $\Sigma_{\mathcal{B}}$ ) and assume that the $X_{i}$ are univariate normals linked by linear dependencies,

$$
X_{i} \mid \Pi_{X_{i}} \sim N\left(\mu_{X_{i}}+\Pi_{X_{i}} \boldsymbol{\beta}_{X_{i}}, \sigma_{X_{i}}^{2}\right)
$$

which can be equivalently written as linear regression models of the form

$$
X_{i}=\mu_{X_{i}}+\Pi_{X_{i}} \boldsymbol{\beta}_{X_{i}}+\varepsilon_{X_{i}}, \quad \varepsilon_{X_{i}} \sim N\left(0, \sigma_{X_{i}}^{2}\right)
$$

The parameters in (3) and (4) are the regression coefficients $\boldsymbol{\beta}_{X_{i}}$ associated with the parents $\Pi_{X_{i}}$, an intercept term $\mu_{X_{i}}$ and the variance $\sigma_{X_{i}}^{2}$. They are usually estimated by maximum likelihood, but Bayesian and regularised estimators are available as well [1].

The link between the parameterisation of the global distribution of a GBN and that of its local distributions is detailed in Pourahmadi [36]. We summarise it here for later use.

- Composing the global distribution. We can create an $N \times N$ lower triangular matrix $C_{\mathcal{B}}$ from the regression coefficients in the local distributions such that $C_{\mathcal{B}} C_{\mathcal{B}}^{\mathrm{T}}$ gives $\Sigma_{\mathcal{B}}$ after rearranging rows and columns. In particular, we:

1. Arrange the nodes of $\mathcal{B}$ in the (partial) topological ordering induced by $\mathcal{G}$, denoted $X_{(i)}, i=1, \ldots, N$.
2. The $i$ th row of $C_{\mathcal{B}}$ (denoted $C_{\mathcal{B}}[i ; \cdot], i=1, \ldots, N$ ) is associated with $X_{(i)}$. We compute its elements from the parameters of $X_{(i)} \mid \Pi_{X_{(i)}}$ as

$$
C_{\mathcal{B}}[i ; i]=\sqrt{\sigma_{X_{(i)}}^{2}} \quad \text { and } \quad C_{\mathcal{B}}[i ; \cdot]=\boldsymbol{\beta}_{X_{(i)}} C_{\mathcal{B}}\left[\Pi_{X_{(i)}} ; \cdot\right]
$$

where $C_{\mathcal{B}}\left[\Pi_{X_{(i)}} ; \cdot\right]$ are the rows of $C_{\mathcal{B}}$ that correspond to the parents of $X_{(i)}$. The rows of $C_{\mathcal{B}}$ are filled following the topological ordering of the BN.
3. Compute $\tilde{\Sigma}_{\mathcal{B}}=C_{\mathcal{B}} C_{\mathcal{B}}^{\mathrm{T}}$.
4. Rearrange the rows and columns of $\tilde{\Sigma}_{\mathcal{B}}$ to obtain $\Sigma_{\mathcal{B}}$.

Intuitively, we construct $C_{\mathcal{B}}$ by propagating the node variances along the paths in $\mathcal{G}$ while combining them with the regression coefficients, which are functions of the correlations between adjacent nodes. As a result, $C_{\mathcal{B}} C_{\mathcal{B}}^{\mathrm{T}}$ gives $\Sigma_{\mathcal{B}}$ after rearranging the rows and columns to follow the original ordering of the nodes.
The elements of the mean vector $\boldsymbol{\mu}_{\mathcal{B}}$ are similarly computed as $\mathrm{E}\left(X_{(i)}\right)=\Pi_{X_{(i)}} \boldsymbol{\beta}_{X_{(i)}}$ iterating over the variables in topological order.

- Decomposing the global distribution. Conversely, we can derive the matrix $C_{\mathcal{B}}$ from $\Sigma_{\mathcal{B}}$ by reordering its rows and columns to follow the topological ordering of the variables in $\mathcal{G}$ and computing its Cholesky decomposition. Then

$$
R=\mathrm{I}_{N}-\operatorname{diag}\left(C_{\mathcal{B}}\right) C_{\mathcal{B}}^{-1}
$$

contains the regression coefficients $\boldsymbol{\beta}_{X_{(i)}}$ in the elements corresponding to $X_{(i)}, \Pi_{X_{(i)}}$ (Here $\operatorname{diag}\left(C_{\mathcal{B}}\right)$ is a diagonal matrix with the same diagonal elements as $C_{\mathcal{B}}$ and $\mathrm{I}_{N}$ is the identity matrix.) Finally, we compute the intercepts $\mu_{X_{i}}$ as $\boldsymbol{\mu}_{\mathcal{B}}-R \boldsymbol{\mu}_{\mathcal{B}}$ by reversing the equations we used to construct $\boldsymbol{\mu}_{\mathcal{B}}$ above.
The computational complexity of composing the global distribution is bound by the matrix multiplication $C_{\mathcal{B}} C_{\mathcal{B}}^{\mathrm{T}}$, which is $O\left(N^{3}\right)$; if we assume that $\mathcal{G}$ is sparse as in Scutari et al. [29], the number of arcs is bound by some $c N$, computing the $\boldsymbol{\mu}_{\mathcal{B}}$ takes $O(N)$ operations. The complexity of decomposing the global distribution is also $O\left(N^{3}\right)$ because both inverting $C_{\mathcal{B}}$ and multiplying the result by $\operatorname{diag}\left(C_{\mathcal{B}}\right)$ are $O\left(N^{3}\right)$.

Example 2 (Composing and decomposing a GBN). Consider the GBN $\mathcal{B}$ from Figure 1 top. The topological ordering of the variables defined by $\mathcal{B}$ is $\left\{\left\{X_{1}, X_{2}\right\}, X_{4}, X_{3}\right\}$, so

$$
C_{\mathcal{B}}=\begin{gathered}
X_{1} \quad X_{2} \quad X_{4} \quad X_{3} \\
X_{1} \\
X_{2} \\
X_{4} \\
X_{3}
\end{gathered}\left(\begin{array}{cccc}
0.894 & 0 & 0 & 0 \\
0 & 0.774 & 0 & 0 \\
1.341 & 2.014 & 1.049 & 0 \\
1.610 & 2.416 & 1.258 & 0.948
\end{array}\right)
$$

where the diagonal elements are

$$
C_{\mathcal{B}}\left[X_{1} ; X_{1}\right]=\sqrt{0.8}, \quad C_{\mathcal{B}}\left[X_{2} ; X_{2}\right]=\sqrt{0.6}, \quad C_{\mathcal{B}}\left[X_{4} ; X_{4}\right]=\sqrt{1.1}, \quad C_{\mathcal{B}}\left[X_{3} ; X_{3}\right]=\sqrt{0.9}
$$

and the elements below the diagonal are taken from the corresponding cells of

$$
\begin{aligned}
& C_{\mathcal{B}}\left[X_{4} ; \cdot\right]=\left(\begin{array}{lll}
1.5 & 2.6
\end{array}\right)\left(\begin{array}{cccc}
0.894 & 0 & 0 & 0 \\
0 & 0.774 & 0 & 0
\end{array}\right) \\
& C_{\mathcal{B}}\left[X_{3} ; \cdot\right]=\left(\begin{array}{ll}
1.2
\end{array}\right)\left(\begin{array}{lll}
1.341 & 2.014 & 1.049
\end{array} 0\right)
\end{aligned}
$$

Computing $C_{\mathcal{B}} C_{\mathcal{B}}^{\mathrm{T}}$ gives

$$
\overline{\Sigma}_{\mathcal{B}}=\begin{gathered}
X_{1} \quad X_{2} \quad X_{4} \quad X_{3} \\
X_{1} \\
X_{2} \\
X_{4} \\
X_{3} \\
X_{3}
\end{gathered}\left(\begin{array}{cccc}
0.800 & 0 & 1.200 & 1.440 \\
0 & 0.600 & 1.560 & 1.872 \\
1.200 & 1.560 & 6.956 & 8.347 \\
1.440 & 1.872 & 8.347 & 10.916
\end{array}\right)
\end{gathered}
$$

and reordering the rows and columns of $\overline{\Sigma}_{\mathcal{B}}$ gives

$$
\Sigma_{\mathcal{B}}=\begin{gathered}
X_{1} \quad X_{2} \quad X_{3} \quad X_{4} \\
X_{1} \\
X_{2} \\
X_{3} \\
X_{4}
\end{gathered}\left(\begin{array}{cccc}
0.800 & 0 & 1.440 & 1.200 \\
0 & 0.600 & 1.872 & 1.560 \\
1.440 & 1.872 & 10.916 & 8.347 \\
1.200 & 1.560 & 8.347 & 6.956
\end{array}\right)
$$

The elements of the corresponding expectation vector $\boldsymbol{\mu}_{\mathcal{B}}$ are then

$$
\begin{aligned}
& \mathrm{E}\left(X_{1}\right)=2.400 \\
& \mathrm{E}\left(X_{2}\right)=1.800 \\
& \mathrm{E}\left(X_{4}\right)=0.2+1.5 \mathrm{E}\left(X_{1}\right)+2.6 \mathrm{E}\left(X_{2}\right)=8.480 \\
& \mathrm{E}\left(X_{3}\right)=2.1+1.2 \mathrm{E}\left(X_{4}\right)=12.276
\end{aligned}
$$

Starting from $\Sigma_{\mathcal{B}}$, we can reorder its rows and columns to obtain $\overline{\Sigma}_{\mathcal{B}}$. The Cholesky decomposition of $\overline{\Sigma}_{\mathcal{B}}$ is $C_{\mathcal{B}}$. Then

$$
\begin{aligned}
& \sigma_{X_{1}}^{2}=C_{\mathcal{B}}\left[X_{1} ; X_{1}\right]^{2}=0.8, \quad \sigma_{X_{2}}^{2}=C_{\mathcal{B}}\left[X_{2} ; X_{2}\right]^{2}=0.6, \\
& \sigma_{X_{3}}^{2}=C_{\mathcal{B}}\left[X_{3} ; X_{3}\right]^{2}=0.9, \quad \sigma_{X_{4}}^{2}=C_{\mathcal{B}}\left[X_{4} ; X_{4}\right]^{2}=0.11 .
\end{aligned}
$$

The coefficients $\boldsymbol{\beta}_{X_{i}}$ of the local distributions are available from

$$
\begin{aligned}
& R=\mathrm{I}_{N}-\left[\begin{array}{cccc}
0.894 & 0 & 0 & 0 \\
0 & 0.774 & 0 & 0 \\
0 & 0 & 1.049 & 0 \\
0 & 0 & 0 & 0.948
\end{array}\right]\left[\begin{array}{cccc}
1.118 & 0 & 0 & 0 \\
0 & 1.291 & 0 & 0 \\
-1.430 & -2.479 & 0.953 & 0 \\
0 & 0 & -1.265 & 1.054
\end{array}\right] \\
& \operatorname{diag}\left(C_{\mathcal{B}}\right) \\
& X_{1} \quad X_{2} \quad X_{4} \quad X_{3} \\
& =\begin{array}{c}
X_{1} \\
X_{2} \\
X_{4} \\
X_{3}
\end{array}\left(\begin{array}{cccc}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
1.500 & 2.600 & 0 & 0 \\
0 & 0 & 1.200 & 0
\end{array}\right)
\end{aligned}
$$

where we can read $R_{X_{4}, X_{1}}=1.5=\beta_{X_{4}, X_{1}}, R_{X_{4}, X_{2}}=2.6=\beta_{X_{4}, X_{2}}, R_{X_{3}, X_{4}}=1.2=\beta_{X_{3}, X_{4}}$.
We can read the standard errors of $X_{1}, X_{2}, X_{3}$ and $X_{4}$ directly from the diagonal elements of $C_{\mathcal{B}}$, and we can compute the intercepts from $\boldsymbol{\mu}_{\mathcal{B}}-R \boldsymbol{\mu}_{\mathcal{B}}$ which amounts to

$$
\begin{aligned}
& \mu_{X_{1}}=\mathrm{E}\left(X_{1}\right)=2.400 \\
& \mu_{X_{2}}=\mathrm{E}\left(X_{2}\right)=1.800 \\
& \mu_{X_{4}}=\mathrm{E}\left(X_{4}\right)-\mathrm{E}\left(X_{1}\right) \beta_{X_{4}, X_{1}}-\mathrm{E}\left(X_{2}\right) \beta_{X_{4}, X_{2}}=0.200 \\
& \mu_{X_{3}}=\mathrm{E}\left(X_{3}\right)-\mathrm{E}\left(X_{4}\right) \beta_{X_{3}, X_{4}}=2.100
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

$$
\begin{array}{ll}
X_{1}=2.4+\varepsilon_{X_{1}}, & \varepsilon_{X_{1}} \sim N(0,0.8) \\
X_{2}=1.8+\varepsilon_{X_{2}}, & \varepsilon_{X_{2}} \sim N(0,0.6) \\
X_{3}=2.1+1.2 X_{4}+\varepsilon_{X_{3}}, & \varepsilon_{X_{3}} \sim N(0,0.9) \\
X_{4}=0.2+1.5 X_{1}+2.6 X_{2}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,1.1)
\end{array}
$$

![img-1.jpeg](img-1.jpeg)

$$
\begin{array}{ll}
X_{1}=2.4+\varepsilon_{X_{1}}, & \varepsilon_{X_{1}} \sim N(0,0.8) \\
X_{2}=0.5+1.4 X_{1}+1.2 X_{3}+\varepsilon_{X_{2}}, & \varepsilon_{X_{2}} \sim N(0,1.1) \\
X_{3}=3.1+1.3 X_{1}+\varepsilon_{X_{3}}, & \varepsilon_{X_{3}} \sim N(0,0.3) \\
X_{4}=2.7+0.8 X_{1}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.5)
\end{array}
$$

Figure 1. DAGs and local distributions for the GBNs $\mathcal{B}$ (top) and $\mathcal{B}^{\prime}$ (bottom) used in Examples 2 and 6-9.

# 3.3. Conditional Linear Gaussian BNs 

Finally, conditional linear Gaussian BNs [37] (CLGBNs) subsume discrete BNs and GBNs as particular cases by combining discrete and continuous random variables in a mixture model. If we denote the former with $\mathbf{X}_{D}$ and the latter with $\mathbf{X}_{G}$, so that $\mathbf{X}=\mathbf{X}_{D} \cup \mathbf{X}_{G}$, then:

- Discrete $X_{i} \in \mathbf{X}_{D}$ are only allowed to have discrete parents (denoted $\Delta_{X_{i}}$ ), and are assumed to follow a multinomial distribution parameterised with CPTs. We can estimate their parameters in the same way as those in a discrete BN.

- Continuous $X_{i} \in \mathbf{X}_{G}$ are allowed to have both discrete and continuous parents (denoted $\Gamma_{X_{i}}, \Delta_{X_{i}} \cup \Gamma_{X_{i}}=\Pi_{X_{i}}$ ). Their local distributions are

$$
X_{i} \mid \Pi_{X_{i}} \sim N\left(\mu_{X_{i}, \delta_{X_{i}}}+\Gamma_{X_{i}} \not{\delta}_{X_{i}, \delta_{X_{i}}}, \sigma_{X_{i}, \delta_{X_{i}}}^{2}\right)
$$

which is equivalent to a mixture of linear regressions against the continuous parents with one component for each configuration $\delta_{X_{i}} \in \operatorname{Val}\left(\Delta_{X_{i}}\right)$ of the discrete parents:

$$
X_{i}=\mu_{X_{i}, \delta_{X_{i}}}+\Gamma_{X_{i}} \not \delta_{X_{i}, \delta_{X_{i}}}+\varepsilon_{X_{i}, \delta_{X_{i}}}, \quad \varepsilon_{X_{i}, \delta_{X_{i}}} \sim N\left(0, \sigma_{X_{i}, \delta_{X_{i}}}^{2}\right)
$$

If $X_{i}$ has no discrete parents, the mixture reverts to a single linear regression like that in (4). The parameters of these local distributions are usually estimated by maximum likelihood like those in a GBN; we have used hierarchical regressions with random effects in our recent work [38] for this purpose as well. Bayesian and regularised estimators are also an option [5].
If the CLGBN comprises $\left|\mathbf{X}_{D}\right|=M$ discrete nodes and $\left|\mathbf{X}_{G}\right|=N-M$ continuous nodes, these distributional assumptions imply the partial topological ordering

$$
\underbrace{\left\{X_{(1)}, \ldots, X_{(M)}\right\}}_{\text {discrete nodes }}, \underbrace{\left\{X_{(M+1)}, \ldots, X_{(N)}\right\}}_{\text {continuous nodes }}
$$

The discrete nodes jointly follow a multinomial distribution, effectively forming a discrete BN. The continuous nodes jointly follow a multivariate normal distribution, parameterised as a GBN, for each configuration of the discrete nodes. Therefore, the global distribution is a Gaussian mixture in which the discrete nodes identify the components, and the continuous nodes determine their distribution. The practical link between the global and local distributions follows directly from Sections 3.1 and 3.2.

Example 3 (Composing and decomposing a CLGBN). For reasons of space, this example is presented as Example A2 in Appendix B.

The complexity of composing and decomposing the global distribution is then

$$
\underbrace{O\left(M I^{M}\right)}_{\text {convert between CPTs and component probabilities }}+\underbrace{O\left((N-M)^{3} I^{\operatorname{Val}(\boldsymbol{\Delta})}\right)}_{\text {de)compose the distinct component distributions }}
$$

where $\boldsymbol{\Delta}=\bigcup_{X_{i} \in \mathbf{X}_{G}} \Delta_{X_{i}}$ are the discrete parents of the continuous nodes.

# 3.4. Inference 

For BNs, inference broadly denotes obtaining the conditional distribution of a subset of variables conditional on a second subset of variables. Following older terminology from expert systems [2], this is called formulating a query in which we ask the BN about the probability of an event of interest after observing some evidence. In conditional probability queries, the event of interest is the probability of one or more events in (or the whole distribution of) some variables of interest conditional on the values assumed by the evidence variables. In maximum a posteriori ("most probable explanation") queries, we condition the values of the evidence variables to predict those of the event variables.

All inference computations on BNs are completely automated by exact and approximate algorithms, which we will briefly describe here. We refer the interested reader to the more detailed treatment in Castillo et al. [2] and Koller and Friedman [5].

Exact inference algorithms use local computations to compute the value of the query. The seminal works of Lauritzen and Spiegelhalter [39], Lauritzen and Wermuth [37] and Lauritzen and Jensen [40] describe how to transform a discrete BN or a (CL)GBN into

a junction tree as a preliminary step before using belief propagation. Cowell [41] uses elimination trees for the same purpose in CLGBNs. (A junction tree is an undirected tree whose nodes are the cliques in the moral graph constructed from the BN and their intersections. A clique is the maximal subset of nodes such that every two nodes in the subset are adjacent).

Namasivayam et al. [42] give the computational complexity of constructing the junction tree from a discrete BN as $O\left(N w+w l^{w} N\right)$ where $w$ is the maximum number of nodes in a clique and, as before, $l$ is the maximum number of values that a variable can take. We take the complexity of belief propagation to be $O\left(N w l^{w}+|\Theta|\right)$, as stated in Lauritzen and Spiegelhalter [39] ("The global propagation is no worse than the initialisation [of the junction tree]"). This is confirmed by Pennock [43] and Namasivayam and Prasanna [44].

As for GBNs, we can also perform exact inference through their global distribution because the latter has only $O\left(N^{2}+N\right)$ parameters. The computational complexity of this approach is $O\left(N^{3}\right)$ because of the cost of composing the global distribution, which we derived in Section 3.2. However, all the operations involved are linear, making it possible to leverage specialised hardware such as GPUs and TPUs to the best effect. Koller and Friedman [5] (Section 14.2.1) note that "inference in linear Gaussian networks is linear in the number of cliques, and at most cubic in the size of the largest clique" when using junction trees and belief propagation. Therefore, junction trees may be significantly faster for GBNs when $w \ll N$. However, the correctness and convergence of belief propagation in GBNs require a set of sufficient conditions that have been studied comprehensively by Malioutov et al. [45]. Using the global distribution directly always produces correct results.

Approximate inference algorithms use Monte Carlo simulations to sample from the global distribution of $\mathbf{X}$ through the local distributions and estimate the answer queries by computing the appropriate summary statistics on the particles they generate. Therefore, they mirror the Monte Carlo and Markov chain Monte Carlo approaches in the literature: rejection sampling, importance sampling, and sequential Monte Carlo among others. Two state-of-the-art examples are the adaptive importance sampling (AIS-BN) scheme [46] and the evidence pre-propagation importance sampling (EPIS-BN) [47].

# 4. Shannon Entropy and Kullback-Leibler Divergence 

The general definition of Shannon entropy for the probability distribution $P$ of $\mathbf{X}$ is

$$
\mathrm{H}(P)=\mathrm{E}_{P}(-\log P(\mathbf{X}))=-\int_{V a l(\mathbf{X})} P(\mathbf{x}) \log P(\mathbf{x}) d \mathbf{x}
$$

The Kullback-Leibler divergence between two distributions $P$ and $Q$ for the same random variables $\mathbf{X}$ is defined as

$$
\mathrm{KL}(P \| Q)=\mathrm{E}_{P(\mathbf{X})}\left(-\log \frac{P(\mathbf{X})}{Q(\mathbf{X})}\right)=-\int_{V a l(\mathbf{X})} \mathrm{P}(\mathbf{x}) \log \frac{P(\mathbf{x})}{Q(\mathbf{x})} d \mathbf{x}
$$

They are linked as follows:

$$
\underbrace{\mathrm{E}_{P(\mathbf{X})}\left(-\log \frac{P(\mathbf{X})}{Q(\mathbf{X})}\right)}_{\mathrm{KL}(P(\mathbf{X}) \| Q(\mathbf{X}))}=\underbrace{\mathrm{E}_{P(\mathbf{X})}(-\log P(\mathbf{X}))}_{\mathrm{H}(P(\mathbf{X}))}+\underbrace{\mathrm{E}_{P(\mathbf{X})}(\log Q(\mathbf{X}))}_{\mathrm{H}(P(\mathbf{X}), Q(\mathbf{X}))}
$$

where $\mathrm{H}(P(\mathbf{X}), Q(\mathbf{X}))$ is the cross-entropy between $P(\mathbf{X})$ and $Q(\mathbf{X})$. For the many properties of these quantities, we refer the reader to Cover and Thomas [48] and Csiszár and Shields [49]. Their use and interpretation are covered in depth (and breadth!) in Murphy [19,20] for general machine learning and in Koller and Friedman [5] for BNs.

For a BN $\mathcal{B}$ encoding the probability distribution of $\mathbf{X}$, (6) decomposes into

$$
\mathrm{H}(\mathcal{B})=\sum_{i=1}^{N} \mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{B}\right)
$$

where $\Pi_{X_{i}}^{B}$ are the parents of $X_{i}$ in $\mathcal{B}$. While this decomposition looks similar to (1), we see that its terms are not necessarily orthogonal, unlike the local distributions.

As for (7), we cannot simply write

$$
\mathrm{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=\sum_{i=1}^{N} \mathrm{KL}\left(X_{i} \mid \Pi_{X_{i}}^{B} \| X_{i} \mid \Pi_{X_{i}}^{B^{\prime}}\right)
$$

because, in the general case, the nodes $X_{i}$ have different parents in $\mathcal{B}$ and $\mathcal{B}^{\prime}$. This issue impacts the complexity of computing Kullback-Leibler divergences in different ways depending on the type of BN.

# 4.1. Discrete BNs 

For discrete BNs, $\mathrm{H}(\mathcal{B})$ does not decompose into orthogonal components. As pointed out in Koller and Friedman [5] (Section 8.4.12),

$$
\begin{aligned}
& \mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{B}\right)=\sum_{j=1}^{q_{i}} \mathrm{P}\left(\Pi_{X_{i}}^{B}=j\right) \mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{B}=j\right) \quad \text { where } \\
& \mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{B}=j\right)=-\sum_{k=1}^{r_{i}} \pi_{i k \mid j}(\mathcal{B}) \log \pi_{i k \mid j}(\mathcal{B})
\end{aligned}
$$

If we estimated the conditional probabilities $\pi_{i k \mid j}(\mathcal{B})$ from data, the $\mathrm{P}\left(\Pi_{X_{i}}^{B}=j\right)$ are already available as the normalising constants of the individual conditional distributions $\left\{\pi_{i k \mid j}(\mathcal{B}), j=1, \ldots, q_{i}\right\}$ in the local distribution of $X_{i}$. In this case, the complexity of computing $\mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{B}\right)$ is linear in the number of parameters: $O(|\Theta|)=\sum_{i=1}^{N} O\left(\left|\Theta_{X_{i}}\right|\right)$.

In the general case, we need exact inference to compute the probabilities $\mathrm{P}\left(\Pi_{X_{i}}^{B}=j\right)$. Fortunately, they can be readily extracted from the junction tree derived from $\mathcal{B}$ as follows:

1. Identify a clique containing both $X_{i}$ and $\Pi_{X_{i}}^{B}$. Such a clique is guaranteed to exist by the family preservation property [5] (Definition 10.1).
2. Compute the marginal distribution of $\Pi_{X_{i}}^{B}$ by summing over the remaining variables in the clique.
Combining the computational complexity of constructing the junction tree from Section 3.4 and that of marginalisation, which is at most $O\left(I^{w-1}\right)$ for each node as in (2), we have

$$
\begin{aligned}
& \underbrace{O\left(N w+w I^{w} N\right)}_{\text {create the junction tree }}+\underbrace{O\left(N I^{w-1}\right)}_{\text {compute the } \mathrm{P}\left(\Pi_{X_{i}}^{B}=j\right)}+\underbrace{O(|\Theta|)}_{\text {compute } \mathrm{H}(\mathcal{B})}= \\
& O\left(N\left(w\left(1+I^{w}\right)+I^{w-1}\right)+|\Theta|\right),
\end{aligned}
$$

which is exponential in the maximum clique size $w$. (The maximum clique size in a junction tree is proportional to the treewidth of the BN the junction tree is created from, which is also used in the literature to characterise computational complexity in BNs.) Interestingly, we do not need to perform belief propagation, so computing $\mathrm{H}(\mathcal{B})$ is more efficient than other inference tasks.

Example 4 (Entropy of a discrete BN). For reasons of space, this example is presented as Example A3 in Appendix B.

The Kullback-Leibler divergence has a similar issue, as noted in Koller and Friedman [5] (Section 8.4.2). The best and most complete explanation of how to compute it for discrete

BNs is in Moral et al. [21]. After decomposing $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$ following (8) to separate $\mathrm{H}(\mathcal{B})$ and $\mathrm{H}\left(\mathcal{B}, \mathcal{B}^{\prime}\right)$, Moral et al. [21] show that the latter takes the form

$$
\mathrm{H}\left(\mathcal{B}, \mathcal{B}^{\prime}\right)=\sum_{i=1}^{N} \sum_{j \in \operatorname{Val}\left(\Pi_{X_{i}}^{B^{\prime}}\right)}\left[\sum_{k=1}^{r_{i}} \pi_{i k j}(\mathcal{B}) \log \pi_{i k \mid j}\left(\mathcal{B}^{\prime}\right)\right]
$$

where:

- $\pi_{i k j}(\mathcal{B})=\mathrm{P}\left(X_{i}=k, \Pi_{X_{i}}\left(\mathcal{B}^{\prime}\right)=j\right)$ is the probability assigned by $\mathcal{B}$ to $X_{i}=k$ given that the variables that are parents of $X_{i}$ in $\mathcal{B}^{\prime}$ take value $j$;
- $\pi_{i k \mid j}\left(\mathcal{B}^{\prime}\right)=\mathrm{P}\left(X_{i}=k \mid \Pi_{X_{i}}\left(\mathcal{B}^{\prime}\right)=j\right)$ is the $(k, j)$ element of the CPT of $X_{i}$ in $\mathcal{B}^{\prime}$.

In order to compute the $\pi_{i k j}(\mathcal{B})$, we need to transform $\mathcal{B}$ into its junction tree and use belief propagation to compute the joint distribution of $X_{i} \cup \Pi_{X_{i}}^{B^{\prime}}$. As a result, $\mathrm{H}\left(\mathcal{B}, \mathcal{B}^{\prime}\right)$ does not decompose at all: each $\pi_{i k j}(\mathcal{B})$ can potentially depend on the whole BN $\mathcal{B}$.

Algorithmically, to compute $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$ we:

1. Transform $\mathcal{B}$ into its junction tree.
2. Compute the entropy $\mathrm{H}(\mathcal{B})$.
3. For each node $X_{i}$ :
(a) Identify $\Pi_{X_{i}}^{B^{\prime}}$, the parents of $X_{i}$ in $\mathcal{B}^{\prime}$.
(b) Obtain the distribution of the variables $\left\{X_{i}, \Pi_{X_{i}}^{B^{\prime}}\right\}$ from the junction tree of $\mathcal{B}$, consisting of the probabilities $\pi_{i k j}(\mathcal{B})$.
(c) Read the $\pi_{i k \mid j}\left(\mathcal{B}^{\prime}\right)$ from the local distribution of $X_{i}$ in $\mathcal{B}^{\prime}$.
4. Use the $\pi_{i k j}(\mathcal{B})$ and the $\pi_{i k \mid j}\left(\mathcal{B}^{\prime}\right)$ to compute (10).

The computational complexity of this procedure is as follows:

$$
\begin{aligned}
& O\left(N\left(w\left(1+l^{w}\right)+l^{w-1}\right)+|\Theta|\right) \quad+\underbrace{O\left(N l^{c}\left(N w l^{w}+|\Theta|\right)\right)}_{\text {produce the } \pi_{i k j}(\mathcal{B})}+\underbrace{O(|\Theta|)}_{\text {compute } \mathrm{H}\left(\mathcal{B}, \mathcal{B}^{\prime}\right)}= \\
& O\left(N^{2} w l^{w+c}+N\left(w+w l^{w}+l^{w-1}\right)+\left(N l^{c}+2\right)|\Theta|\right) .
\end{aligned}
$$

As noted in Moral et al. [21], computing the $\pi_{i k j}(\mathcal{B})$ requires a separate run of belief propagation for each configuration of the $\Pi_{X_{i}}^{B^{\prime}}$, for a total of $\sum_{i=1}^{N} l^{\left|\Pi_{X_{i}}^{B^{\prime}}\right|}$ times. If we assume that the DAG underlying $\mathcal{B}^{\prime}$ is sparse, we have that $\left|\Pi_{X_{i}}^{B^{\prime}}\right| \leqslant c$ and the overall complexity of this step becomes $O\left(N l^{c} \cdot\left(N w l^{w}+|\Theta|\right)\right), N$ times that listed in Section 3.4. The caching scheme devised by Moral et al. [21] is very effective in limiting the use of belief propagation, but it does not alter its exponential complexity.

Example 5 (KL between two discrete BNs). Consider the discrete BN $\mathcal{B}$ from Figure 2 top. Furthermore, consider the $B N \mathcal{B}^{\prime}$ from Figure 2 bottom. We constructed the global distribution of $\mathcal{B}$ in Example A1; we can similarly compose the global distribution of $\mathcal{B}^{\prime}$, shown below.


Since both global distributions are limited in size, we can then compute the Kullback-Leibler divergence between $\mathcal{B}$ and $\mathcal{B}^{\prime}$ using (7).

$$
\begin{aligned}
\mathrm{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right) & =-0.013 \log 0.013-0.016 \log 0.016-0.022 \log 0.022-0.016 \log 0.016- \\
0.072 \log 0.072-0.013 \log 0.013-0.029 \log 0.029-0.079 \log 0.079- \\
0.033 \log 0.033-0.144 \log 0.144-0.054 \log 0.054-0.139 \log 0.139- \\
-0.062 \log 0.062-0.04 \log 0.04-0.025 \log 0.025-0.243 \log 0.243=0.687
\end{aligned}
$$

In the general case, when we cannot use the global distributions, we follow the approach described in Section 4.1. Firstly, we apply (8) to write

$$
\mathrm{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=\mathrm{H}(\mathcal{B})-\mathrm{H}\left(\mathcal{B}, \mathcal{B}^{\prime}\right)
$$

we have from Example A3 that $\mathrm{H}(\mathcal{B})=2.440$. As for the cross-entropy $\mathrm{H}\left(\mathcal{B}, \mathcal{B}^{\prime}\right)$, we apply (10):

1. We identify the parents of each node in $\mathcal{B}^{\prime}$ :

$$
\Pi_{\mathrm{X}_{1}}^{B^{\prime}}=\{\varnothing\}, \quad \Pi_{\mathrm{X}_{2}}^{B^{\prime}}=\left\{\mathrm{X}_{1}, \mathrm{X}_{4}\right\}, \quad \Pi_{\mathrm{X}_{3}}^{B^{\prime}}=\left\{\mathrm{X}_{1}\right\}, \quad \Pi_{\mathrm{X}_{4}}^{B^{\prime}}=\left\{\mathrm{X}_{3}\right\}
$$

2. We construct a junction tree from $\mathcal{B}$ and we use it to compute the distributions $\mathrm{P}\left(X_{1}\right)$, $\mathrm{P}\left(X_{2}, X_{1}, X_{4}\right), \mathrm{P}\left(X_{3}, X_{1}\right)$ and $\mathrm{P}\left(X_{4}, X_{3}\right)$.

$$
\begin{aligned}
& \frac{\left\{X_{1}, X_{4}\right\}}{\left\{\begin{array}{l}
a, g\} \\
a, h\} \\
b, g\} \\
b, h\}
\end{array}\right.} \\[6pt]
& \frac{a}{0.53} \quad \frac{b}{0.47} \\[6pt]
& \text{X}_{2} \begin{array}{l}
c \\
d
\end{array}
\begin{array}{llll}
0.070 & 0.110 & 0.053 & 0.107 \\
0.089 & 0.261 & 0.076 & 0.235
\end{array} \\[6pt]
& \text{X}_{1} \quad \frac{X_{3}}{c} \\[6pt]
& \text{X}_{3} \begin{array}{l}
e \\
f
\end{array}
\begin{array}{ll}
0.289 & 0.312 \\
0.241 & 0.158
\end{array} \\[6pt]
& \text{X}_{4} \begin{array}{l}
g \\
h
\end{array}
\begin{array}{ll}
0.120 & 0.167 \\
0.481 & 0.231
\end{array}
\end{aligned}
$$

3. We compute the cross-entropy terms for the individual variables in $\mathcal{B}$ and $\mathcal{B}^{\prime}$ :

$$
\begin{aligned}
& \mathrm{H}\left(X_{1}^{B}, X_{1}^{B^{\prime}}\right)=0.53 \log 0.31+0.47 \log 0.69=-0.795 \\
& \mathrm{H}\left(X_{2}^{B}, X_{2}^{B^{\prime}}\right)=0.070 \log 0.38+0.089 \log 0.62+0.110 \log 0.71+0.261 \log 0.29+ \\
& 0.053 \log 0.51+0.076 \log 0.49+0.107 \log 0.14+0.235 \log 0.86 \\
& =-0.807 \\
& \mathrm{H}\left(X_{3}^{B}, X_{3}^{B^{\prime}}\right)=0.289 \log 0.44+0.241 \log 0.56+0.312 \log 0.18+0.158 \log 0.82 \\
& =-0.943 ; \\
& \mathrm{H}\left(X_{4}^{B}, X_{4}^{B^{\prime}}\right)=0.120 \log 0.26+0.481 \log 0.74+0.167 \log 0.50+0.231 \log 0.50 \\
& =-0.582
\end{aligned}
$$

which sum up to $\mathrm{H}\left(\mathcal{B}, \mathcal{B}^{\prime}\right)=\sum_{i=1}^{N} \mathrm{H}\left(X_{i}^{B}, X_{i}^{B^{\prime}}\right)=-3.127$.
4. We compute $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=2.440-3.127=0.687$, which matches the value we previously computed from the global distributions.

![img-2.jpeg](img-2.jpeg)

Figure 2. DAGs and local distributions for the discrete BNs $\mathcal{B}$ (top) and $\mathcal{B}^{\prime}$ (bottom) used in Examples 1, 4 and 5.

# 4.2. Gaussian BNs 

$\mathrm{H}(\mathcal{B})$ decomposes along with the local distributions $X_{i} \mid \Pi_{X_{i}}$ in the case of GBNs: from (3), each $X_{i} \mid \Pi_{X_{i}}$ is a univariate normal with variance $\sigma_{X_{i}}^{2}(\mathcal{B})$ and therefore

$$
\mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{\mathcal{B}}\right)=\frac{1}{2} \log \left(2 \pi \sigma_{X_{i}}^{2}(\mathcal{B})\right)+\frac{1}{2}
$$

which has a computational complexity of $O(1)$ for each node, $O(N)$ overall. Equivalently, we can start from the global distribution of $\mathcal{B}$ from Section 3.2 and consider that

$$
\operatorname{det}(\Sigma)=\operatorname{det}\left(C_{\mathcal{B}^{\prime}} C_{\mathcal{B}^{\prime}}^{T}\right)=\operatorname{det}\left(C_{\mathcal{B}}\right)^{2}=\left(\prod_{i=1}^{N} C_{\mathcal{B}}[i ; i]\right)^{2}=\prod_{i=1}^{N} \sigma_{X_{i}}^{2}(\mathcal{B})
$$

because $C_{\mathcal{B}}$ is lower triangular. The (multivariate normal) entropy of $\mathbf{X}$ then becomes

$$
\begin{aligned}
& \mathrm{H}(\mathcal{B})=\frac{N}{2}+\frac{N}{2} \log 2 \pi+\frac{1}{2} \log \operatorname{det}(\Sigma)=\frac{N}{2}+\frac{N}{2} \log 2 \pi+\frac{1}{2} \sum_{i=1}^{N} \log \sigma_{X_{i}}^{2}(\mathcal{B}) \\
&=\sum_{i=1}^{N} \frac{1}{2}+\frac{1}{2} \log \left(2 \pi \sigma_{X_{i}}^{2}(\mathcal{B})\right)=\sum_{i=1}^{N} \mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{\mathcal{B}}\right)
\end{aligned}
$$

in agreement with (12).
Example 6 (Entropy of a GBN). For reasons of space, this example is presented as Example A4 in Appendix B.

In the literature, the Kullback-Leibler divergence between two GBNs $\mathcal{B}$ and $\mathcal{B}^{\prime}$ is usually computed using the respective global distributions $N\left(\boldsymbol{\mu}_{\mathcal{B}}, \Sigma_{\mathcal{B}}\right)$ and $N\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}, \Sigma_{\mathcal{B}^{\prime}}\right)$ [50,51,52]. The general expression is

$$
\mathrm{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=\frac{1}{2}\left[\operatorname{tr}\left(\Sigma_{\mathcal{B}^{\prime}}^{-1} \Sigma_{\mathcal{B}}\right)+\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}-\boldsymbol{\mu}_{\mathcal{B}}\right)^{\mathrm{T}} \Sigma_{\mathcal{B}^{\prime}}^{-1}\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}-\boldsymbol{\mu}_{\mathcal{B}}\right)-N+\log \frac{\operatorname{det}\left(\Sigma_{\mathcal{B}^{\prime}}\right)}{\operatorname{det}\left(\Sigma_{\mathcal{B}}\right)}\right]
$$

which has computational complexity

$$
\begin{aligned}
& \underbrace{O\left(2 N^{3}+2 N\right)}_{\text {compute } \mu_{B}, \mu_{B^{\prime}}} \underbrace{\Sigma_{B^{\prime}}}_{\Sigma_{B^{\prime}}}+\underbrace{O\left(N^{3}\right)}_{\text {invert } \Sigma_{B^{\prime}}}+\underbrace{O\left(N^{3}\right)}_{\text {multiply } \Sigma_{B^{\prime}}^{-1} \text { and } \Sigma_{B^{\prime}}}+\underbrace{O(N)}_{\text {trace of } \Sigma_{B}^{-1} \Sigma_{B^{\prime}}}+ \\
& \underbrace{O\left(N^{2}+2 N\right)}_{\text {compute }\left(\mu_{B^{\prime}}-\mu_{B}\right)^{\mathrm{T}} \Sigma_{B^{\prime}}^{-1}\left(\mu_{B^{\prime}}-\mu_{B}\right)} \underbrace{+\underbrace{O\left(N^{3}\right)}_{\text {determinant of } \Sigma_{B^{\prime}}}+\underbrace{O\left(N^{3}\right)}_{\text {determinant of } \Sigma_{B}}= \\
& O\left(6 N^{3}+N^{2}+5 N\right) .
\end{aligned}
$$

The spectral decomposition $\Sigma_{B^{\prime}}=U \Lambda_{B^{\prime}} U^{\mathrm{T}}$ gives the eigenvalues $\operatorname{diag}\left(\Lambda_{B^{\prime}}\right)=\left\{\lambda_{1}\left(\mathcal{B}^{\prime}\right), \ldots\right.$, $\left.\lambda_{N}\left(\mathcal{B}^{\prime}\right)\right\}$ to compute $\Sigma_{B^{\prime}}^{-1}$ and $\operatorname{det}\left(\Sigma_{B^{\prime}}\right)$ efficiently as illustrated in the example below. (Further computing the spectral decomposition of $\Sigma_{\mathcal{B}}$ to compute $\operatorname{det}\left(\Sigma_{\mathcal{B}}\right)$ from the eigenvalues $\left\{\lambda_{1}(\mathcal{B}), \ldots, \lambda_{N}(\mathcal{B})\right\}$ does not improve complexity because it just replaces a single $O\left(N^{3}\right)$ operation with another one.) We thus somewhat improve the overall complexity of $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$ to $O\left(5 N^{3}+N^{2}+6 N\right)$.

Example 7 (General-case KL between two GBNs). Consider the GBN $\mathcal{B}$ Figure 1 top, which we know has global distribution

$$
\left[\begin{array}{l}
X_{1} \\
X_{2} \\
X_{3} \\
X_{4}
\end{array}\right] \sim N\left(\left[\begin{array}{c}
2.400 \\
1.800 \\
12.276 \\
8.848
\end{array}\right],\left[\begin{array}{cccc}
0.800 & 0 & 1.440 & 1.200 \\
0 & 0.600 & 1.872 & 1.560 \\
1.440 & 1.872 & 10.916 & 8.347 \\
1.200 & 1.560 & 8.347 & 6.956
\end{array}\right]\right)
$$

from Example 2. Furthermore, consider the GBN $\mathcal{B}^{\prime}$ from Figure 1 bottom, which has global distribution

$$
\left[\begin{array}{l}
X_{1} \\
X_{2} \\
X_{3} \\
X_{4}
\end{array}\right] \sim N\left(\left[\begin{array}{c}
2.400 \\
11.324 \\
6.220 \\
4.620
\end{array}\right],\left[\begin{array}{cccc}
0.800 & 2.368 & 1.040 & 0.640 \\
2.368 & 8.541 & 3.438 & 1.894 \\
1.040 & 3.438 & 1.652 & 0.832 \\
0.640 & 1.894 & 0.832 & 1.012
\end{array}\right]\right)
$$

In order to compute $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$, we first invert $\Sigma_{\mathcal{B}^{\prime}}$ to obtain

$$
\Sigma_{B^{\prime}}^{-1}=\left[\begin{array}{cccc}
9.945 & -1.272 & -2.806 & -1.600 \\
-1.272 & 0.909 & -1.091 & 0 \\
-2.806 & -1.091 & 4.642 & 0 \\
-1.600 & 0 & 0 & 2.000
\end{array}\right]
$$

which we then multiply by $\Sigma_{\mathcal{B}}$ to compute the trace $\operatorname{tr}\left(\Sigma_{B^{\prime}}^{-1} \Sigma_{\mathcal{B}}\right)=57.087$. We also use $\Sigma_{B^{\prime}}^{-1}$ to compute $\left(\boldsymbol{\mu}_{B^{\prime}}-\boldsymbol{\mu}_{\mathcal{B}}\right)^{\mathrm{T}} \Sigma_{B^{\prime}}^{-1}\left(\boldsymbol{\mu}_{B^{\prime}}-\boldsymbol{\mu}_{\mathcal{B}}\right)=408.362$. Finally, $\operatorname{det}\left(\Sigma_{B^{\prime}}\right)=0.475, \operatorname{det}\left(\Sigma_{\mathcal{B}}\right)=0.132$ and therefore

$$
\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=\frac{1}{2}\left[57.087+408.362-4+\log \left(\frac{0.475}{0.132}\right)\right]=230.0846
$$

As an alternative, we can compute the spectral decompositions $\Sigma_{\mathcal{B}}=U_{\mathcal{B}} \Lambda_{\mathcal{B}} U_{\mathcal{B}}^{\mathrm{T}}$ and $\Sigma_{\mathcal{B}^{\prime}}=U_{\mathcal{B}^{\prime}} \Lambda_{\mathcal{B}^{\prime}} U_{\mathcal{B}^{\prime}}^{\mathrm{T}}$ as an intermediate step. Multiplying the sets of eigenvalues

$$
\Lambda_{\mathcal{B}}=\operatorname{diag}(\{18.058,0.741,0.379,0.093\}) \quad \text { and } \quad \Lambda_{\mathcal{B}^{\prime}}=\operatorname{diag}(\{11.106,0.574,0.236,0.087\})
$$

gives the corresponding determinants; and it allows us to easily compute

$$
\Sigma_{B^{\prime}}^{-1}=U_{B^{\prime}} \Lambda_{B^{\prime}}^{-1} U_{B^{\prime}}^{T}, \quad \text { where } \quad \Lambda_{B^{\prime}}^{-1}=\operatorname{diag}\left(\left\{\frac{1}{11.106}, \frac{1}{0.574}, \frac{1}{0.236}, \frac{1}{0.087}\right\}\right)
$$

for use in both the quadratic form and in the trace.
However, computing $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$ from the global distributions $N\left(\boldsymbol{\mu}_{\mathcal{B}}, \Sigma_{\mathcal{B}}\right)$ and $N\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}, \Sigma_{\mathcal{B}^{\prime}}\right)$ disregards the fact that BNs are sparse models that can be characterised more compactly by $\left(\boldsymbol{\mu}_{\mathcal{B}}, C_{\mathcal{B}}\right)$ and $\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}, C_{\mathcal{B}^{\prime}}\right)$ as shown in Section 3.2. In particular, we can revisit several operations that are in the high-order terms of (15):

- Composing the global distribution from the local ones. We avoid computing $\Sigma_{\mathcal{B}}$ and $\Sigma_{\mathcal{B}^{\prime}}$, thus reducing this step to $O(2 N)$ complexity.
- Computing the trace $\operatorname{tr}\left(\Sigma_{\mathcal{B}}^{-1} \Sigma_{\mathcal{B}}\right)$. We can reduce the computation of the trace as follows.

1. We can replace $\Sigma_{\mathcal{B}}$ and $\Sigma_{\mathcal{B}^{\prime}}$ in the trace with any reordered matrix [53] (Result 8.17): we choose to use $\widetilde{\Sigma}_{\mathcal{B}^{\prime}}$ and $\widetilde{\Sigma}_{\mathcal{B}}^{*}$ where $\widetilde{\Sigma}_{\mathcal{B}^{\prime}}$ is defined as before and $\widetilde{\Sigma}_{\mathcal{B}}^{*}$ is $\Sigma_{\mathcal{B}}$ with the rows and columns reordered to match $\widetilde{\Sigma}_{\mathcal{B}^{\prime}}$. Formally, this is equivalent to $\widetilde{\Sigma}_{\mathcal{B}}^{*}=P \widetilde{\Sigma}_{\mathcal{B}} P^{\mathrm{T}}$ where $P$ is a permutation matrix that imposes the desired node ordering: since both the rows and the columns are permuted in the same way, the diagonal elements of $\widetilde{\Sigma}_{\mathcal{B}}$ are the same as those of $\widetilde{\Sigma}_{\mathcal{B}}^{*}$ and the trace is unaffected.
2. We have $\widetilde{\Sigma}_{\mathcal{B}^{\prime}}=C_{\mathcal{B}^{\prime}} C_{\mathcal{B}^{\prime}}^{\mathrm{T}}$.
3. As for $\widetilde{\Sigma}_{\mathcal{B}}^{*}$, we can write $\widetilde{\Sigma}_{\mathcal{B}}^{*}=P \widetilde{\Sigma}_{\mathcal{B}} P=\left(P C_{\mathcal{B}}\right)\left(P C_{\mathcal{B}}\right)^{\mathrm{T}}=C_{\mathcal{B}}^{*}\left(C_{\mathcal{B}}^{*}\right)^{\mathrm{T}}$ where $C_{\mathcal{B}}^{*}=P C_{\mathcal{B}}$ is the lower triangular matrix $C_{\mathcal{B}}$ with the rows re-ordered to match $\widetilde{\Sigma}_{\mathcal{B}^{\prime}}$. Note that $C_{\mathcal{B}}^{*}$ is not lower triangular unless $\mathcal{G}$ and $\mathcal{G}^{\prime}$ have the same partial node ordering, which implies $P=\mathrm{I}_{N}$.
Therefore

$$
\operatorname{tr}\left(\Sigma_{\mathcal{B}}^{-1} \Sigma_{\mathcal{B}}\right)=\operatorname{tr}\left(\left(C_{\mathcal{B}}^{-1} C_{\mathcal{B}}^{*}\right)^{\mathrm{T}}\left(C_{\mathcal{B}}^{-1} C_{\mathcal{B}}^{*}\right)\right)=\left\|C_{\mathcal{B}}^{-1} C_{\mathcal{B}}^{*}\right\|_{\mathrm{F}}^{2}
$$

where the last step rests on Seber [53] (Result 4.15). We can invert $C_{\mathcal{B}^{\prime}}$ in $O\left(N^{2}\right)$ time following Stewart [54] (Algorithm 2.3). Multiplying $C_{\mathcal{B}}^{-1}$ and $C_{\mathcal{B}}^{*}$ is still $O\left(N^{3}\right)$. The Frobenius norm $\|\cdot\|_{F}$ is $O\left(N^{2}\right)$ since it is the sum of the squared elements of $C_{\mathcal{B}}^{-1} C_{\mathcal{B}}^{*}$.

- Computing the determinants $\operatorname{det}\left(\Sigma_{\mathcal{B}^{\prime}}\right)$ and $\operatorname{det}\left(\Sigma_{\mathcal{B}}\right)$. From (13), each determinant can be computed in $O(N)$.
- Computing the quadratic term $\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}-\boldsymbol{\mu}_{\mathcal{B}}\right)^{\mathrm{T}} \Sigma_{\mathcal{B}^{\prime}}^{-1}\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}-\boldsymbol{\mu}_{\mathcal{B}}\right)$. Decomposing $\Sigma_{\mathcal{B}}^{-1}$ leads to

$$
\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}-\boldsymbol{\mu}_{\mathcal{B}}\right)^{\mathrm{T}} \Sigma_{\mathcal{B}}^{-1}\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}-\boldsymbol{\mu}_{\mathcal{B}}\right)=\left(C_{\mathcal{B}}^{-1}\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}^{*}-\boldsymbol{\mu}_{\mathcal{B}}^{*}\right)\right)^{\mathrm{T}} C_{\mathcal{B}}^{-1}\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}^{*}-\boldsymbol{\mu}_{\mathcal{B}}^{*}\right)
$$

where $\boldsymbol{\mu}_{\mathcal{B}}^{*}$ and $\boldsymbol{\mu}_{\mathcal{B}}^{*}$ are the mean vectors re-ordered to match $C_{\mathcal{B}}^{-1}$. The computational complexity is still $O\left(N^{2}+2 N\right)$ because $C_{\mathcal{B}}^{-1}$ is available from previous computations. Combining (17), (13) and (18), the expression in (14) becomes

$$
\begin{aligned}
& \operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)= \\
& \quad \frac{1}{2}\left[\left\|C_{\mathcal{B}}^{-1} C_{\mathcal{B}}^{*}\right\|_{\mathrm{F}}^{2}+\left(C_{\mathcal{B}}^{-1}\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}^{*}-\boldsymbol{\mu}_{\mathcal{B}}^{*}\right)\right)^{\mathrm{T}} C_{\mathcal{B}}^{-1}\left(\boldsymbol{\mu}_{\mathcal{B}^{\prime}}^{*}-\boldsymbol{\mu}_{\mathcal{B}}^{*}\right)-N+2 \log \frac{\prod_{i=1}^{N} C_{\mathcal{B}^{\prime}}[i ; i]}{\prod_{i=1}^{N} C_{\mathcal{B}}[i ; i]}\right]
\end{aligned}
$$

The overall complexity of (19) KL is

$$
\begin{aligned}
& \underbrace{O\left(2 N^{2}+2 N\right)}_{\text {compute } \boldsymbol{\mu}_{\mathcal{B}}, \boldsymbol{\mu}_{\mathcal{B}^{\prime}}} C_{\mathcal{B}}, C_{\mathcal{B}^{\prime}}}+\underbrace{O\left(2 N^{2}+N^{3}\right)}_{\text {compute }\left\|C_{\mathcal{B}}^{-1} C_{\mathcal{B}}\right\|_{\mathrm{F}}^{2}}+\underbrace{O\left(N^{2}+2 N\right)}_{\text {compute the quadratic form }}+ \\
& \underbrace{O(2 N)}_{\text {compute det }\left(\Sigma_{\mathcal{B}}\right), \operatorname{det}\left(\Sigma_{\mathcal{B}^{\prime}}\right)}=O\left(N^{3}+5 N^{2}+6 N\right) ;
\end{aligned}
$$

while still cubic, the leading coefficient suggests that it should be about 5 times faster than the variant of (15) using the spectral decomposition.

Example 8 (Sparse KL between two GBNs). Consider again the two GBNs from Example 7. The corresponding matrices

$$
C_{B}=\begin{array}{ccccc}
X_{1} & X_{2} & X_{4} & X_{3} \\
X_{1} & 0.894 & 0 & 0 & 0 \\
X_{2} & 0 & 0.774 & 0 & 0 \\
X_{4} & 1.341 & 2.014 & 1.049 & 0 \\
X_{3} & 1.610 & 2.416 & 1.258 & 0.948
\end{array}
$$

readily give the determinants of $\Sigma_{B}$ and $\Sigma_{B^{\prime}}$ following (13):

$$
\begin{aligned}
\operatorname{det}\left(C_{B}\right) & =(0.894 \cdot 0.774 \cdot 1.049 \cdot 0.948)^{2}=0.475 \\
\operatorname{det}\left(C_{B^{\prime}}\right) & =(0.894 \cdot 0.548 \cdot 0.707 \cdot 1.049)^{2}=0.132
\end{aligned}
$$

As for the Frobenius norm in (17), we first invert $C_{B^{\prime}}$ to obtain

$$
C_{B^{\prime}}^{-1}=\begin{array}{l}
X_{1} \\
X_{3} \\
X_{4} \\
X_{2}
\end{array}\left(\begin{array}{ccc}
X_{3} & X_{4} & X_{2} \\
1.118 & 0 & 0 & 0 \\
-2.373 & 1.825 & 0 & 0 \\
-1.131 & 0 & 1.414 & 0 \\
-1.334 & -1.144 & 0 & 0.953
\end{array}\right)
$$

then we reorder the rows and columns of $C_{B}$ to follow the same node ordering as $C_{B^{\prime}}$ and compute

$$
\left\|\left(\begin{array}{cccc}
1.118 & 0 & 0 & 0 \\
-2.373 & 1.825 & 0 & 0 \\
-1.131 & 0 & 1.414 & 0 \\
-1.334 & -1.144 & 0 & 0.953
\end{array}\right)\left(\begin{array}{cccc}
0.894 & 0 & 0 & 0 \\
1.610 & 0.948 & 1.258 & 2.416 \\
1.341 & 0 & 1.049 & 2.014 \\
0 & 0 & 0 & 0.774
\end{array}\right)\right\|_{F}^{2}=57.087
$$

which, as expected, matches the value of $\operatorname{tr}\left(\Sigma_{B^{\prime}}^{-1} \Sigma_{B}\right)$ we computed in Example 7. Finally, $C_{B^{\prime}}^{-1}\left(\boldsymbol{\mu}_{B^{\prime}}^{*}-\boldsymbol{\mu}_{B}^{*}\right)$ in (18) is

$$
\left(\begin{array}{cccc}
1.118 & 0 & 0 & 0 \\
-2.373 & 1.825 & 0 & 0 \\
-1.131 & 0 & 1.414 & 0 \\
-1.334 & -1.144 & 0 & 0.953
\end{array}\right)\left[\left(\begin{array}{c}
2.400 \\
6.220 \\
4.620 \\
11.324
\end{array}\right)-\left(\begin{array}{c}
2.400 \\
12.1276 \\
8.848 \\
1.800
\end{array}\right)\right]=\left(\begin{array}{c}
0 \\
-11.056 \\
-5.459 \\
16.010
\end{array}\right)
$$

The quadratic form is then equal to 408.362 , which matches the value of $\left(\boldsymbol{\mu}_{B^{\prime}}-\boldsymbol{\mu}_{B}\right)^{\mathrm{T}} \Sigma_{B^{\prime}}^{-1}\left(\boldsymbol{\mu}_{B^{\prime}}-\boldsymbol{\mu}_{B}\right)$ in Example 7. As a result, the expression for $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$ is the same as in (16).

We can further reduce the complexity (20) of (19) when an approximate value of KL is suitable for our purposes. The only term with cubic complexity is $\operatorname{tr}\left(\Sigma_{B^{-1}}^{-1} \Sigma_{B}\right)=\left\|C_{B^{-1}}^{-1} C_{B}^{-}\right\|_{F}^{2}$ : reducing it to quadratic complexity or lower will eliminate the leading term of (20), making it quadratic in complexity. One way to do this is to compute a lower and an upper bound for $\operatorname{tr}\left(\Sigma_{B^{-1}}^{-1} \Sigma_{B}\right)$, which can serve as an interval estimate, and take their geometric mean as an approximate point estimate.

A lower bound is given by Seber [53] (Result 10.39):

$$
\operatorname{tr}\left(\Sigma_{B^{\prime}}^{-1} \Sigma_{B}\right) \geqslant \log \operatorname{det}\left(\Sigma_{B^{\prime}}^{-1} \Sigma_{B}\right)+N=-\log \operatorname{det}\left(\Sigma_{B^{\prime}}\right)+\log \operatorname{det}\left(\Sigma_{B}\right)+N
$$

which conveniently reuses the values of $\operatorname{det}\left(\Sigma_{B}\right)$ and $\operatorname{det}\left(\Sigma_{B^{\prime}}\right)$ we have from (13). For an upper bound, Seber [53] (Result 10.59) combined with Seber [53] (Result 4.15) gives

$$
\operatorname{tr}\left(\Sigma_{B^{-1}}^{-1} \Sigma_{B}\right) \leqslant \operatorname{tr}\left(\Sigma_{B^{-1}}^{-1}\right) \operatorname{tr}\left(\Sigma_{B}\right)=\operatorname{tr}\left(\left(C_{B^{\prime}} C_{B^{\prime}}^{\mathrm{T}}\right)^{-1}\right) \operatorname{tr}\left(C_{B} C_{B}^{\mathrm{T}}\right)=\left\|C_{B^{-1}}^{-1}\right\|_{F}^{2}\left\|C_{B}\right\|_{F}^{2}
$$

a function of $C_{\mathcal{B}}$ and $C_{\mathcal{B}^{\prime}}$ that can be computed in $O\left(2 N^{2}\right)$ time. Note that, as far as the point estimate is concerned, we do not care about how wide the interval is: we only need its geometric mean to be an acceptable approximation of $\operatorname{tr}\left(\Sigma_{\mathcal{B}}^{-1} \Sigma_{\mathcal{B}}\right)$.

Example 9 (Approximate KL). From Example 7, we have that $\operatorname{tr}\left(\Sigma_{\mathcal{B}}^{-1} \Sigma_{\mathcal{B}}\right)=57.087$, $\operatorname{det}\left(\Sigma_{\mathcal{B}^{\prime}}\right)=0.475$ and $\operatorname{det}\left(\Sigma_{\mathcal{B}}\right)=0.132$. The lower bound in (21) is then

$$
-\log \operatorname{det}\left(\Sigma_{\mathcal{B}^{\prime}}\right)+\log \operatorname{det}\left(\Sigma_{\mathcal{B}}\right)+4=5.281
$$

and the upper bound in (22) is

$$
\left\|C_{\mathcal{B}}^{-1}\right\|_{F}^{2}\left\|C_{\mathcal{B}}\right\|_{\bar{F}}^{2}=17.496 \cdot 19.272=337.207
$$

Their geometric mean is 42.199 , which can serve as an approximate value for $\mathrm{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$.
If we are comparing two GBNs whose parameters (but not necessarily network structures) have been learned from the same data, we can sometimes approximate $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$ using the local distributions $X_{i} \mid \Pi_{X_{i}}^{B}$ and $X_{i} \mid \Pi_{X_{i}}^{B^{\prime}}$ directly. If $\mathcal{B}$ and $\mathcal{B}^{\prime}$ have compatible partial orderings, we can define a common total node ordering for both such that

$$
\begin{aligned}
\mathrm{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right) & =\mathrm{KL}\left(X_{(1)} \mid\left\{X_{(2)}, \ldots, X_{(N)}\right\} \cdots X_{N} \| X_{(1)} \mid\left\{X_{(2)}, \ldots, X_{(N)}\right\} \cdots X_{N}\right) \\
& =\mathrm{KL}\left(X_{(1)} \mid \Pi_{\mathrm{X}_{(1)}}^{\mathcal{B}} \ldots \cdot X_{(N)} \mid \Pi_{\mathrm{X}_{(N)}}^{\mathcal{B}} \| X_{(1)} \mid \Pi_{\mathrm{X}_{(1)}}^{\mathcal{B}^{\prime}} \ldots \cdot X_{(N)} \mid \Pi_{\mathrm{X}_{(N)}}^{\mathcal{B}^{\prime}}\right)
\end{aligned}
$$

By "compatible partial orderings", we mean two partial orderings that can be sorted into at least one shared total node ordering that is compatible with both. The product of the local distributions in the second step is obtained from the chain decomposition in the first step by considering the nodes in the conditioning other than the parents to have associated regression coefficients equal to zero. Then, following the derivations in Cavanaugh [55] for a general linear regression model, we can write the empirical approximation

$$
\mathrm{KL}\left(X_{i} \mid \Pi_{X_{i}}^{B} \| X_{i} \mid \Pi_{X_{i}}^{B^{\prime}}\right) \approx \frac{1}{2}\left(\log \frac{\partial_{\tilde{X}_{i}}^{2}\left(\mathcal{B}^{\prime}\right)}{\partial_{\tilde{X}_{i}}^{2}(\mathcal{B})}+\frac{\partial_{\tilde{X}_{i}}^{2}(\mathcal{B})}{\partial_{\tilde{X}_{i}}^{2}\left(\mathcal{B}^{\prime}\right)}-1\right)+\frac{1}{2 n}\left(\frac{\left\|\tilde{\mathbf{x}}_{i}(\mathcal{B})-\tilde{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)\right\|_{2}^{2}}{\partial_{\tilde{X}_{i}}^{2}\left(\mathcal{B}^{\prime}\right)}\right)
$$

where, following a similar notation to (4):

- $\tilde{\mu}_{X_{i}}(\mathcal{B}), \tilde{\boldsymbol{\beta}}_{X_{i}}(\mathcal{B}), \tilde{\mu}_{X_{i}}\left(\mathcal{B}^{\prime}\right), \tilde{\boldsymbol{\beta}}_{X_{i}}\left(\mathcal{B}^{\prime}\right)$ are the estimated intercepts and regression coefficients;
- $\tilde{\mathbf{x}}_{i}(\mathcal{B})$ and $\tilde{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)$ are the $n \times 1$ vectors

$$
\tilde{\mathbf{x}}_{i}(\mathcal{B})=\tilde{\mu}_{X_{i}}(\mathcal{B})+\mathbf{x}\left[\cdot ; \Pi_{X_{i}}(\mathcal{B})\right] \tilde{\boldsymbol{\beta}}_{X_{i}}(\mathcal{B}), \quad \tilde{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)=\tilde{\mu}_{X_{i}}\left(\mathcal{B}^{\prime}\right)+\mathbf{x}\left[\cdot ; \Pi_{X_{i}}\left(\mathcal{B}^{\prime}\right)\right] \tilde{\boldsymbol{\beta}}_{X_{i}}\left(\mathcal{B}^{\prime}\right)
$$

the fitted values computed from the data observed for $X_{i}, \Pi_{X_{i}}(\mathcal{B}), \Pi_{X_{i}}\left(\mathcal{B}^{\prime}\right)$;

- $\quad \sigma_{X_{i}}^{2}(\mathcal{B})$ and $\sigma_{X_{i}}^{2}\left(\mathcal{B}^{\prime}\right)$ are the residual variances in $\mathcal{B}$ and $\mathcal{B}^{\prime}$.

We can compute the expression in (23) for each node in

$$
\begin{aligned}
& \underbrace{O\left(n\left(\left|\Pi_{X_{i}}(\mathcal{B})\right|+\mid \Pi_{X_{i}}\left(\mathcal{B}^{\prime}\right)\right|+2\right)}_{\text {compute } \tilde{\mathbf{x}}_{i}(\mathcal{B}) \text { and } \tilde{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)}+\underbrace{O(n)}_{\text {compute the norm }\left\|\tilde{\mathbf{x}}_{i}(\mathcal{B})-\tilde{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)\right\|_{2}^{2}}= \\
& O\left(n\left(\left|\Pi_{X_{i}}(\mathcal{B})\right|+\mid \Pi_{X_{i}}\left(\mathcal{B}^{\prime}\right)\right|+5 / 2\right)\right),
\end{aligned}
$$

which is linear in the sample size if both $\mathcal{G}$ and $\mathcal{G}^{\prime}$ are sparse because $\left|\Pi_{X_{i}}(\mathcal{B})\right| \leqslant c,\left|\Pi_{X_{i}}\left(\mathcal{B}^{\prime}\right)\right| \leqslant c$. In this case, the overall computational complexity simplifies to $O(n N(2 c+5 / 2))$. Furthermore, as we pointed out in Scutari et al. [29], the fitted values $\tilde{\mathbf{x}}_{i}(\mathcal{B}), \tilde{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)$ are computed as a by-product of parameter learning: if we consider them to be already available, the above computational complexity is reduced to just $O(n)$ for a single node and $O(n N)$ overall.

We can also replace the fitted values $\widehat{\mathbf{x}}_{i}(\mathcal{B}), \widehat{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)$ in (23) with the corresponding residuals $\widehat{\boldsymbol{\varepsilon}}_{i}(\mathcal{B}), \widehat{\boldsymbol{\varepsilon}}_{i}\left(\mathcal{B}^{\prime}\right)$ because

$$
\left\|\widehat{\mathbf{x}}_{i}(\mathcal{B})-\widehat{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)\right\|_{2}^{2}=\left\|\left(\mathbf{x}\left[\cdot ; X_{i}\right]-\widehat{\mathbf{x}}_{i}(\mathcal{B})\right)-\left(\mathbf{x}\left[\cdot ; X_{i}\right]-\widehat{\mathbf{x}}_{i}\left(\mathcal{B}^{\prime}\right)\right)\right\|_{2}^{2}=\left\|\widehat{\boldsymbol{\varepsilon}}_{i}(\mathcal{B})-\widehat{\boldsymbol{\varepsilon}}_{i}\left(\mathcal{B}^{\prime}\right)\right\|_{2}^{2}
$$

if the latter are available but the former are not.
Example 10 (KL between GBNs with parameters estimated from data). For reasons of space, this example is presented as Example A5 in Appendix B.

# 4.3. Conditional Gaussian BNs 

The entropy $\mathrm{H}(\mathcal{B})$ decomposes into a separate $\mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{B}\right)$ for each node, of the form (9) for discrete nodes and (12) for continuous nodes with no discrete parents. For continuous nodes with both discrete and continuous parents,

$$
\mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{B}\right)=\frac{1}{2} \sum_{\delta_{X_{i}} \in \operatorname{Val}\left(\Delta_{X_{i}}\right)} \pi_{\delta_{X_{i}}} \log \left(2 \pi \sigma_{X_{i}, \delta_{X_{i}}}^{2}(\mathcal{B})\right)+\frac{1}{2}
$$

where $\pi_{\delta_{X_{i}}}$ represents the probability associated with the configuration $\delta_{X_{i}}$ of the discrete parents $\Delta_{X_{i}}$. This last expression can be computed in $O\left(\left|\operatorname{Val}\left(\Delta_{X_{i}}\right)\right|\right)$ time for each node. Overall, the complexity of computing $\mathrm{H}(\mathcal{B})$ is

$$
O\left(\sum_{X_{i} \in \mathbf{X}_{D}}\left|\Theta_{X_{i}}\right|+\sum_{X_{i} \in \mathbf{X}_{G}} \max \left\{1,\left|\operatorname{Val}\left(\Delta_{X_{i}}\right)\right|\right\}\right)
$$

where the max accounts for the fact that $\left|\operatorname{Val}\left(\Delta_{X_{i}}\right)\right|=0$ when $\Delta_{X_{i}}=\varnothing$ but the computational complexity is $O(1)$ for such nodes.

Example 11 (Entropy of a CLGBN). For reasons of space, this example is presented as Example A6 in Appendix B.

As for $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$, we could not find any literature illustrating how to compute it. The partition of the nodes in (5) implies that

$$
\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=\underbrace{\operatorname{KL}\left(\mathbf{X}_{D}^{B} \| \mathbf{X}_{D}^{B^{\prime}}\right)}_{\text {discrete nodes }}+\underbrace{\operatorname{KL}\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B} \| \mathbf{X}_{G}^{B^{\prime}} \mid \mathbf{X}_{D}^{B^{\prime}}\right)}_{\text {continuous nodes }}
$$

We can compute the first term following Section 4.1: $\mathbf{X}_{D}^{B}$ and $\mathbf{X}_{D}^{B^{\prime}}$ form two discrete BNs whose DAGs are the spanning subgraphs of $\mathcal{B}$ and $\mathcal{B}^{\prime}$ and whose local distributions are the corresponding ones in $\mathcal{B}$ and $\mathcal{B}^{\prime}$, respectively. The second term decomposes into

$$
\mathrm{KL}\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B} \| \mathbf{X}_{G}^{B^{\prime}} \mid \mathbf{X}_{D}^{B^{\prime}}\right)=\sum_{\mathbf{x}_{D} \in \operatorname{Val}\left(\mathbf{X}_{D}\right)} \mathrm{P}\left(\mathbf{X}_{D}^{B}=\mathbf{x}_{D}\right) \operatorname{KL}\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B}=\mathbf{x}_{D} \| \mathbf{X}_{G}^{B^{\prime}} \mid \mathbf{X}_{D}^{B^{\prime}}=\mathbf{x}_{D}\right)
$$

similarly to (10) and (24). We can compute it using the multivariate normal distributions associated with the $\mathbf{X}_{D}^{B}=\mathbf{x}_{D}$ and the $\mathbf{X}_{D}^{B^{\prime}}=\mathbf{x}_{D}$ in the global distributions of $\mathcal{B}$ and $\mathcal{B}^{\prime}$.

Example 12 (General-case KL between two CLGBNs). Consider the CLGBNs $\mathcal{B}$ from Figure 3 top, which we already used in Examples 3 and 11, and $\mathcal{B}^{\prime}$ from Figure 3 bottom. The variables $\mathbf{X}_{D}^{B^{\prime}}$ identify the following mixture components in the global distribution of $\mathcal{B}^{\prime}$ :

$$
\begin{aligned}
\{a, c, e\},\{b, c, e\},\{a, d, e\},\{b, d, e\} & \mapsto\{e\} \\
\{a, c, f\},\{b, c, f\},\{a, d, f\},\{b, d, f\} & \mapsto\{f\}
\end{aligned}
$$

Therefore, $\mathcal{B}^{\prime}$ only encodes two different multivariate normal distributions.
Firstly, we construct two discrete BNs using the subgraphs spanning $\mathbf{X}_{D}^{B}=\mathbf{X}_{D}^{B^{\prime}}=\left\{X_{1}, X_{2}, X_{3}\right\}$ in $\mathcal{B}$ and $\mathcal{B}^{\prime}$, which have arcs $\left\{X_{1} \rightarrow X_{2}\right\}$ and $\left\{X_{1} \rightarrow X_{2}, X_{2} \rightarrow X_{3}\right\}$, respectively. The CPTs for $X_{1}, X_{2}$ and $X_{3}$ are the same as in $\mathcal{B}$ and in $\mathcal{B}^{\prime}$. We then compute $\operatorname{KL}\left(\mathbf{X}_{D}^{B} \| \mathbf{X}_{D}^{B^{\prime}}\right)=0.577$ following Example 5.

Secondly, we construct the multivariate normal distributions associated with the components of $\mathcal{B}^{\prime}$ following Example 3 (in which we computed those of $\mathcal{B}$ ). For $\{e\}$, we have

$$
\left[\begin{array}{l}
X_{4} \\
X_{5} \\
X_{6}
\end{array}\right] \sim N\left(\left[\begin{array}{l}
0.300 \\
1.400 \\
1.140
\end{array}\right],\left[\begin{array}{lll}
0.160 & 0.000 & 0.032 \\
0.000 & 1.690 & 1.183 \\
0.032 & 1.183 & 2.274
\end{array}\right]\right)
$$

for $\{f\}$, we have

$$
\left[\begin{array}{l}
X_{4} \\
X_{5} \\
X_{6}
\end{array}\right] \sim N\left(\left[\begin{array}{l}
1.000 \\
0.500 \\
0.650
\end{array}\right],\left[\begin{array}{lll}
0.090 & 0.000 & 0.018 \\
0.000 & 2.250 & 1.575 \\
0.018 & 1.575 & 2.546
\end{array}\right]\right)
$$

Then,

$$
\begin{aligned}
& \operatorname{KL}\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B} \| \mathbf{X}_{G}^{B^{\prime}} \mid \mathbf{X}_{D}^{B^{\prime}}\right) \\
& =\sum_{x_{1} \in\{a, b\}} \sum_{x_{2} \in\{c, d\}} \sum_{x_{3} \in\{e, f\}} \mathrm{P}\left(\mathbf{X}_{D}^{B}=\left\{x_{1}, x_{2}, x_{3}\right\}\right) \cdot \\
& \quad \operatorname{KL}\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B}=\left\{x_{1}, x_{2}, x_{3}\right\} \| \mathbf{X}_{G}^{B^{\prime}} \mid \mathbf{X}_{D}^{B^{\prime}}=\left\{x_{1}, x_{2}, x_{3}\right\}\right) \\
& =\underbrace{0.040 \times 1.721}_{\{a, c, e\}}+\underbrace{0.036 \times 1.721}_{\{b, c, e\}}+\underbrace{0.040 \times 2.504}_{\{a, d, e\}}+\underbrace{0.084 \times 2.504}_{\{b, d, e\}}+ \\
& \underbrace{0.16 \times 4.303}_{\{a, c, f\}}+\underbrace{0.144 \times 4.303}_{\{b, c, f\}}+\underbrace{0.16 \times 6.31}_{\{a, d, f\}}+\underbrace{0.336 \times 6.31}_{\{b, d, f\}} \\
& =4.879
\end{aligned}
$$

and $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=\operatorname{KL}\left(\mathbf{X}_{D}^{B} \| \mathbf{X}_{D}^{B^{\prime}}\right)+\operatorname{KL}\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B} \| \mathbf{X}_{G}^{B^{\prime}} \mid \mathbf{X}_{D}^{B^{\prime}}\right)=0.577+4.879=5.456$.
The computational complexity of this basic approach to computing $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$ is

$$
\begin{aligned}
& \underbrace{O\left(M w l^{w+c}+M\left(w+w l^{w}+l^{w-1}\right)+\left(M l^{c}+2\right) \mid \Theta_{\mathbf{X}_{D}}\right)}_{\text {compute KL }\left(\mathbf{X}_{D}^{B} \| \mathbf{X}_{D}^{B^{\prime}}\right)}+ \\
& \underbrace{O\left(l^{M} \cdot\left(6(N-M)^{3}+(N-M)^{2}+5(N-M)\right)\right)}_{\text {compute all the KL }\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B}=\mathbf{x}_{D} \| \mathbf{X}_{G}^{B^{\prime}} \mid \mathbf{X}_{D}^{B^{\prime}}=\mathbf{x}_{D}\right)},
\end{aligned}
$$

which we obtain by adapting (11) and (15) to follow the notation $\left|\mathbf{X}_{D}\right|=M$ and $\left|\mathbf{X}_{G}\right|=N-M$ we established in Section 3.3. The first term implicitly covers the cost of computing the $\mathrm{P}\left(\mathbf{X}_{D}^{B}=\mathbf{x}_{D}\right)$, which relies on exact inference like the computation of $\operatorname{KL}\left(\mathbf{X}_{D}^{B} \| \mathbf{X}_{D}^{B^{\prime}}\right)$. The second term is exponential in $M$, which would lead us to conclude that it is computationally unfeasible to compute $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)$ whenever we have more than a few discrete variables in $\mathcal{B}$ and $\mathcal{B}^{\prime}$. Certainly, this would agree with Hershey and Olsen [22], who reviewed various scalable approximations of the KL divergence between two Gaussian mixtures.

![img-3.jpeg](img-3.jpeg)

Figure 3. DAGs and local distributions for the CLGBNs $\mathcal{B}$ (top) and $\mathcal{B}^{\prime}$ (bottom) used in Examples 3 and 11-13.

However, we would again disregard the fact that BNs are sparse models. Two properties of CLGBNs that are apparent from Examples 3 and 12 allow us to compute (26) efficiently:

- We can reduce $\mathbf{X}_{\mathrm{G}}^{B} \mid \mathbf{X}_{\mathrm{D}}^{B}$ to $\mathbf{X}_{\mathrm{G}}^{B} \mid \Delta^{B}$ where $\Delta^{B}=\bigcup_{\mathrm{X}_{i} \in \mathbf{X}_{\mathrm{G}}} \Delta_{X_{i}}^{B} \subseteq \mathbf{X}_{\mathrm{D}}^{B}$. In other words, the continuous nodes are conditionally independent on the discrete nodes that are not their parents $\left(\mathbf{X}_{\mathrm{D}}^{B} \backslash \Delta^{B}\right)$ given their parents $\left(\Delta^{B}\right)$. The same is true for $\mathbf{X}_{\mathrm{G}}^{B^{\prime}} \mid \mathbf{X}_{\mathrm{D}}^{B^{\prime}}$. The number of distinct terms in the summation in (26) is then given by $\left|\operatorname{Val}\left(\Delta^{B} \cup \Delta^{B^{\prime}}\right)\right|$ which will be smaller than $\left|\operatorname{Val}\left(\mathbf{X}_{\mathrm{D}}^{B}\right)\right|$ in sparse networks.
- The conditional distributions $\mathbf{X}_{\mathrm{G}}^{B} \mid \mathbf{X}_{\mathrm{D}}^{B}=\delta$ and $\mathbf{X}_{\mathrm{G}}^{B^{\prime}} \mid \mathbf{X}_{\mathrm{D}}^{B^{\prime}}=\delta$ are multivariate normals (not mixtures). They are also faithful to the subgraphs spanning the continuous nodes $\mathbf{X}_{G}$, and we can represent them as GBNs whose parameters can be extracted directly from $\mathcal{B}$ and $\mathcal{B}^{\prime}$. Therefore, we can use the results from Section 4.2 to compute their Kullback-Leibler divergences efficiently.

As a result, (26) simplifies to

$$
\begin{aligned}
& \operatorname{KL}\left(\mathbf{X}_{\mathrm{G}}^{B} \mid \mathbf{X}_{\mathrm{D}}^{B} \| \mathbf{X}_{\mathrm{G}}^{B^{\prime}} \mid \mathbf{X}_{\mathrm{D}}^{B^{\prime}}\right)= \\
& \sum_{\delta \in \operatorname{Val}\left(\Delta^{B} \cup \Delta^{B^{\prime}}\right)} \mathrm{P}\left(\left\{\Delta^{B} \cup \Delta^{B^{\prime}}\right\}=\delta\right) \operatorname{KL}\left(\mathbf{X}_{\mathrm{G}}^{B} \mid\left\{\Delta^{B} \cup \Delta^{B^{\prime}}\right\}=\delta \| \mathbf{X}_{\mathrm{G}}^{B^{\prime}} \mid\left\{\Delta^{B} \cup \Delta^{B^{\prime}}\right\}=\delta\right)
\end{aligned}
$$

where $\mathrm{P}\left(\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\delta\right)$ is the probability that the nodes $\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}$ take value $\boldsymbol{\delta}$ as computed in $\mathcal{B}$. In turn, (27) reduces to

$$
\begin{aligned}
& \underbrace{O\left(M w l^{w+c}+M\left(w+w l^{w}+l^{w-1}\right)+\left(M l^{c}+2\right) \mid \Theta_{\mathbf{X}_{D}}\right)}_{\text {compute KL }\left(\mathbf{X}_{D}^{B} \| \mathbf{X}_{D}^{B^{\prime}}\right)}+ \\
& \underbrace{O\left(l^{\left|V a l\left(\Delta^{B} \cup \Delta^{B^{\prime}}\right)\right|} \cdot\left((N-M)^{3}+5(N-M)^{2}+6(N-M)\right)\right)}_{\text {compute all the KL }\left(\mathbf{X}_{G}^{B} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\delta \| \mathbf{X}_{G}^{B^{\prime}} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\delta\right)}
\end{aligned}
$$

because we can replace $l^{M}$ with $l^{\left|V a l\left(\Delta^{B} \cup \Delta^{B^{\prime}}\right)\right|}$, which is an upper bound to the unique components in the mixture, and because we replace the complexity in (15) with that (20). We can also further reduce the second term to quadratic complexity as we discussed in Section 4.2. The remaining drivers of the computational complexity are:

- the maximum clique size $w$ in the subgraph spanning $\mathbf{X}_{D}^{B}$;
- the number of arcs from discrete nodes to continuous nodes in both $\mathcal{B}$ and $\mathcal{B}^{\prime}$ and the overlap between $\boldsymbol{\Delta}^{B}$ and $\boldsymbol{\Delta}^{B^{\prime}}$.

Example 13 (Sparse KL between two CLGBNs). Consider again the CLGBNs $\mathcal{B}$ and $\mathcal{B}^{\prime}$ from Example 12. The node sets $\Delta^{B}=\left\{X_{2}, X_{3}\right\}$ and $\Delta^{B^{\prime}}=\left\{X_{3}\right\}$ identify four KL divergences to compute: $\operatorname{Val}\left(\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right)=\{\{c, e\},\{c, f\},\{d, e\},\{d, f\}\}$.

$$
\begin{aligned}
& \operatorname{KL}\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B} \| \mathbf{X}_{G}^{B^{\prime}} \mid \mathbf{X}_{D}^{B^{\prime}}\right)= \\
& \mathrm{P}\left(\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{c, e\}\right) \mathrm{KL}\left(\mathbf{X}_{G}^{B} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{c, e\} \| \mathbf{X}_{G}^{B^{\prime}} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{c, e\}\right)+ \\
& \mathrm{P}\left(\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{c, f\}\right) \mathrm{KL}\left(\mathbf{X}_{G}^{B} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{c, f\} \| \mathbf{X}_{G}^{B^{\prime}} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{c, f\}\right)+ \\
& \mathrm{P}\left(\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{d, e\}\right) \mathrm{KL}\left(\mathbf{X}_{G}^{B} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{d, e\} \| \mathbf{X}_{G}^{B^{\prime}} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{d, e\}\right)+ \\
& \mathrm{P}\left(\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{d, f\}\right) \mathrm{KL}\left(\mathbf{X}_{G}^{B} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{d, f\} \| \mathbf{X}_{G}^{B^{\prime}} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}=\{d, f\}\right)
\end{aligned}
$$

All the BNs in the Kullback-Leibler divergences are GBNs whose structure and local distributions can be read from $\mathcal{B}$ and $\mathcal{B}^{\prime}$. The four GBNs associated with $\mathbf{X}_{G}^{B} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}$ have nodes $\mathbf{X}_{G}^{B}=\left\{X_{4}, X_{5}, X_{6}\right\}$, arcs $\left\{X_{5} \rightarrow X_{4}, X_{4} \rightarrow X_{6}\right\}$ and the local distributions listed in Figure 3. The corresponding GBNs associated with $\mathbf{X}_{G}^{B^{\prime}} \mid\left\{\boldsymbol{\Delta}^{B} \cup \boldsymbol{\Delta}^{B^{\prime}}\right\}$ are, in fact, only two distinct GBNs associated with $\{e\}$ and $\{f\}$. They have arcs $\left\{X_{4} \rightarrow X_{6}, X_{5} \rightarrow X_{6}\right\}$ and local distributions: for $\{e\}$,

$$
\begin{array}{ll}
X_{4}=0.3+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.16) \\
X_{5}=1.4+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,1.69) \\
X_{6}=0.1+0.2 X_{4}+0.7 X_{5}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1.44)
\end{array}
$$

for $\{f\}$,

$$
\begin{array}{ll}
X_{4}=1.0+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.09) \\
X_{5}=0.5+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,2.25) \\
X_{6}=0.1+0.2 X_{4}+0.7 X_{5}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1.44)
\end{array}
$$

Plugging in the numbers,

$$
\begin{aligned}
& \operatorname{KL}\left(\mathbf{X}_{G}^{B} \mid \mathbf{X}_{D}^{B^{\prime}} \| \mathbf{X}_{G}^{B^{\prime \prime}} \mid \mathbf{X}_{D}^{B^{\prime \prime}}\right)=\underbrace{0.076 \times 1.721}_{\{c, e\}}+\underbrace{0.304 \times 4.303}_{\{c, f\}}+ \\
& \underbrace{0.124 \times 2.504}_{\{d, e\}}+\underbrace{0.496 \times 6.310}_{\{d, f\}}=4.879
\end{aligned}
$$

which matches the value we computed in Example 12.

# 5. Conclusions 

We started this paper by reviewing the three most common distributional assumptions for BNs: discrete BNs, Gaussian BNs (GBNs) and conditional linear Gaussian BNs (CLGBNs). Firstly, we reviewed the link between the respective global and local distributions, and we formalised the computational complexity of decomposing the former into the latter (and vice versa).

We then leveraged these results to study the complexity of computing Shannon's entropy. We can, of course, compute the entropy of a BN from its global distribution using standard results from the literature. (In the case of discrete BNs and CLGBNS, only for small networks because $|\Theta|$ grows combinatorially.) However, this is not computationally efficient because we incur the cost of composing the global distribution. While the entropy does not decompose along with the local distributions for either discrete BNs or CLGBNS, we show that it is nevertheless efficient to compute it from them.

Computing the Kullback-Leibler divergence between two BNs following the little material found in the literature is more demanding. The discrete case has been thoroughly investigated by Moral et al. [21]. However, the literature typically relies on composing the global distributions for GBNs and CGBNs. Using the local distributions, thus leveraging the intrinsic sparsity of BNs, we showed how to compute the Kullback-Leibler divergence exactly with greater efficiency. For GBNs, we showed how to compute the Kullback-Leibler divergence approximately with quadratic complexity (instead of cubic). If the two GBNs have compatible node orderings and their parameters are estimated from the same data, we can also approximate their Kullback-Leibler divergence with complexity that scales with the number of parents of each node. All these results are summarised in Table A1 in Appendix A.

Finally, we provided step-by-step numeric examples of how to compute Shannon's entropy and the Kullback-Leibler divergence for discrete BNs, GBNs and CLGBNs. (See also Appendix B). Considering this is a highly technical topic, and no such examples are available anywhere in the literature, we feel that they are helpful in demystifying this topic and in integrating BNs into many general machine learning approaches.

Funding: This research received no external funding.
Data Availability Statement: Data are contained within the article.
Conflicts of Interest: The author declares no conflict of interest.

## Appendix A. Computational Complexity Results

For ease of reference, we summarise here all the computational complexity results in this paper, including the type of BN and the page where they have been derived.

Table A1. Summary of all the computational complexity results in this paper, including the type of BN and the page where they have been derived.


# Appendix B. Additional Examples 

Example A1 (Composing and decomposing a discrete BN). Consider the discrete BN $\mathcal{B}$ shown in Figure 2 (top). Composing its global distribution entails computing the joint probabilities of all possible states of all variables,

$$
\{a, b\} \times\{c, d\} \times\{e, f\} \times\{g, h\}
$$

and arranging them in the following four-dimensional probability table in which each dimension is associated with one of the variables.


The joint probabilities are computed by multiplying the appropriate cells of the CPTs, for instance

$$
\begin{aligned}
& \mathrm{P}(\mathbf{X}=\{a, d, f, h\})= \\
& \mathrm{P}\left(X_{1}=a\right) \mathrm{P}\left(X_{2}=d\right) \mathrm{P}\left(X_{3}=f \mid X_{1}=a, X_{2}=d\right) \mathrm{P}\left(X_{4}=h \mid X_{3}=f\right)= \\
& 0.53 \cdot 0.66 \cdot 0.25 \cdot 0.58=0.051
\end{aligned}
$$

Conversely, we can decompose the global distribution into the local distributions by summing over all variables other than the nodes and their parents. For $X_{1}$, this means

$$
\begin{aligned}
& \mathrm{P}\left(X_{1}=a\right)=\sum_{x_{2} \in\{c, d\}} \sum_{x_{3} \in\{c, f\}} \sum_{x_{4} \in\{g, h\}} \mathrm{P}\left(X_{1}=a, X_{2}=x_{2}, X_{3}=x_{3}, X_{4}=x_{4}\right) \\
& =0.005+0.064+0.022+0.089+0.052+0.037+0.210+0.051=0.53 \\
& \mathrm{P}\left(X_{1}=b\right)=\sum_{x_{2} \in\{c, d\}} \sum_{x_{3} \in\{c, f\}} \sum_{x_{4} \in\{g, h\}} \mathrm{P}\left(X_{1}=b, X_{2}=x_{2}, X_{3}=x_{3}, X_{4}=x_{4}\right) \\
& =0.013+0.040+0.051+0.056+0.050+0.026+0.199+0.036=0.47
\end{aligned}
$$

Similarly, for $X_{2}$ we obtain

$$
\begin{aligned}
& \mathrm{P}\left(X_{2}=c\right)=\sum_{x_{1} \in\{a, b\}} \sum_{x_{3} \in\{c, f\}} \sum_{x_{4} \in\{g, h\}} \mathrm{P}\left(X_{1}=x_{1}, X_{2}=c, X_{3}=x_{3}, X_{4}=x_{4}\right) \\
& =0.005+0.064+0.022+0.089+0.013+0.040+0.051+0.056=0.34 \\
& \mathrm{P}\left(X_{2}=d\right)=\sum_{x_{1} \in\{a, b\}} \sum_{x_{3} \in\{c, f\}} \sum_{x_{4} \in\{g, h\}} \mathrm{P}\left(X_{1}=x_{1}, X_{2}=d, X_{3}=x_{3}, X_{4}=x_{4}\right) \\
& =0.052+0.037+0.210+0.051+0.050+0.026+0.199+0.036=0.66
\end{aligned}
$$

For $X_{4}$, we first compute the joint distribution of $X_{4}$ and $X_{3}$ by marginalising over $X_{1}$ and $X_{2}$,

$$
\begin{aligned}
& \underbrace{\underbrace{\begin{array}{c}
e \\
0.005 \\
0.089
\end{array}\left(\begin{array}{l}
0.064 \\
0.089
\end{array}\right)}_{\{a, c\}}}+\underbrace{\underbrace{\begin{array}{c}
e \\
0.052 \\
0.210
\end{array}\left(\begin{array}{l}
0.037 \\
0.051
\end{array}\right)}_{\{a, d\}}+\underbrace{\underbrace{\begin{array}{c}
e \\
0.013 \\
0.051
\end{array}\left(\begin{array}{l}
0.040 \\
0.056
\end{array}\right)}_{\{b, c\}}+ \\
& \underbrace{\underbrace{\begin{array}{l}
e \\
0.050 \\
0.199
\end{array}\left(\begin{array}{l}
0.026 \\
0.036
\end{array}\right)}_{\{b, d\}}=\underbrace{\begin{array}{l}
g \\
g \\
h
\end{array}\left(\begin{array}{l}
0.120 \\
0.481
\end{array}\left(\begin{array}{l}
0.167 \\
0.232
\end{array}\right)}_{\{b, d\}}
\end{aligned}
$$

from which we obtain the CPT for $X_{4} \mid X_{3}$ by normalising its columns.
As for $X_{3}$, we marginalise over $X_{2}$ to obtain the joint distribution of $X_{3}, X_{1}$ and $X_{2}$

$$
\begin{aligned}
& \{a, c\} \quad\{a, d\} \quad\{b, c\} \quad\{b, d\} \\
& \begin{array}{l}
e \\
f
\end{array}\left(\begin{array}{ll}
0.005+0.022=0.027 & 0.052+0.210=0.262 & 0.013+0.051=0.064 & 0.050+0.199=0.248 \\
0.064+0.089=0.153 & 0.037+0.051=0.087 & 0.040+0.056=0.096 & 0.026+0.036=0.062
\end{array}
\end{aligned}
$$

and we obtain the CPT for $X_{3} \mid X_{1}, X_{2}$ by normalising its columns as we did earlier with $X_{4}$.
Example A2 (Composing and decomposing a CLGBN). Consider the CLGBN $\mathcal{B}$ from Figure 3 top. The $M=3$ discrete variables at the top of the network have the joint distribution below:

$$
\begin{aligned}
& \left\{\begin{array}{l}
\{a, c, e\} \\
\hline 0.040
\end{array} \quad \begin{array}{l}
\{b, c, e\} \\
\hline 0.036
\end{array} \quad \begin{array}{l}
\{a, d, e\} \\
\hline 0.040
\end{array} \quad \begin{array}{l}
\{b, d, e\} \\
\hline 0.084
\end{array} \quad \begin{array}{l}
\{a, c, f\} \\
\hline 0.160
\end{array} \quad \begin{array}{l}
\{b, c, f\} \\
\hline 0.144
\end{array} \quad \begin{array}{l}
\{a, d, f\} \\
\hline 0.160
\end{array} \quad \begin{array}{l}
\{b, d, f\} \\
\hline 0.336
\end{array}
\end{aligned}
$$

Its elements identify the components of the mixture that make up the global distribution of $\mathcal{B}$, and the associated probabilities are the probabilities of those components.

We can then identify which parts of the local distributions of the $N-M=3$ continuous variables ( $X_{4}, X_{5}$ and $X_{6}$ ) we need to compute $\mathrm{P}\left(X_{4}, X_{5}, X_{6} \mid X_{1}, X_{2}, X_{3}\right)$ for each element of the mixture. The graphical structure of $\mathcal{B}$ implies that $\mathrm{P}\left(X_{4}, X_{5}, X_{6} \mid X_{1}, X_{2}, X_{3}\right)=$ $\mathrm{P}\left(X_{4}, X_{5}, X_{6} \mid X_{2}, X_{3}\right)$ because the continuous nodes are d-separated from $X_{1}$ by their parents. As

a result, the following mixture components will share identical distributions which only depend on the configurations of $X_{2}$ and $X_{3}$ :

$$
\begin{array}{ll}
\{a, c, e\},\{b, c, e\} \mapsto\{c, e\}, & \{a, d, e\},\{b, d, e\} \mapsto\{d, e\} \\
\{a, c, f\},\{b, c, f\} \mapsto\{c, f\}, & \{a, d, f\},\{b, d, f\} \mapsto\{d, f\}
\end{array}
$$

For the mixture components with a distribution identified by $\{c, e\}$, the relevant parts of the distributions of $X_{4}, X_{5}$ and $X_{6}$ are:

$$
\begin{array}{ll}
X_{4}=0.1+0.2 X_{5}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.09) \\
X_{5}=0.1+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,0.09) \\
X_{6}=0.1+0.2 X_{4}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1)
\end{array}
$$

We can treat them as the local distributions in a GBN over $\left\{X_{4}, X_{5}, X_{6}\right\}$ with a DAG equal to the subgraph of $\mathcal{B}$ spanning only these nodes. If we follow the steps outlined in Section 3.2 and illustrated in Example 2, we obtain

$$
\left[\begin{array}{l}
X_{4} \\
X_{5} \\
X_{6}
\end{array}\right] \sim N\left(\left[\begin{array}{l}
0.120 \\
0.100 \\
0.124
\end{array}\right], \Sigma_{\{c, e\}}(\mathcal{B})=\left[\begin{array}{lll}
0.094 & 0.018 & 0.019 \\
0.018 & 0.090 & 0.004 \\
0.019 & 0.004 & 1.004
\end{array}\right]\right)
$$

which is the multivariate normal distribution associated with the components $\{a, c, e\}$ and $\{b, c, e\}$ in the mixture. Similarly, the relevant parts of the distributions of $X_{4}, X_{5}$ and $X_{6}$ for $\{d, e\}$ are

$$
\begin{array}{ll}
X_{4}=0.6+0.8 X_{5}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.36) \\
X_{5}=0.2+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,0.36) \\
X_{6}=0.1+0.2 X_{4}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1)
\end{array}
$$

and jointly

$$
\left[\begin{array}{l}
X_{4} \\
X_{5} \\
X_{6}
\end{array}\right] \sim N\left(\left[\begin{array}{l}
0.760 \\
0.200 \\
0.252
\end{array}\right], \Sigma_{\{d, e\}}(\mathcal{B})=\left[\begin{array}{lll}
0.590 & 0.288 & 0.118 \\
0.288 & 0.360 & 0.058 \\
0.118 & 0.058 & 1.024
\end{array}\right]\right)
$$

for the components $\{a, d, e\}$ and $\{b, d, e\}$. For the components $\{a, c, f\}$ and $\{b, c, f\}$, the local distributions identified by $\{c, f\}$ are

$$
\begin{array}{ll}
X_{4}=0.1+0.2 X_{5}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.09) \\
X_{5}=0.4+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,0.81) \\
X_{6}=0.1+0.2 X_{4}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1)
\end{array}
$$

and the joint distribution of $X_{4}, X_{5}$ and $X_{6}$ is

$$
\left[\begin{array}{l}
X_{4} \\
X_{5} \\
X_{6}
\end{array}\right] \sim N\left(\left[\begin{array}{l}
0.180 \\
0.400 \\
0.136
\end{array}\right], \Sigma_{\{c, f\}}(\mathcal{B})=\left[\begin{array}{lll}
0.122 & 0.162 & 0.024 \\
0.162 & 0.810 & 0.032 \\
0.024 & 0.032 & 1.005
\end{array}\right]\right)
$$

Finally, the local distributions identified by $\{d, f\}$ are

$$
\begin{array}{ll}
X_{4}=0.6+0.8 X_{5}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.36) \\
X_{5}=0.4+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,1.44) \\
X_{6}=0.1+0.2 X_{4}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1)
\end{array}
$$

and the joint distribution of $X_{4}, X_{5}$ and $X_{6}$ for the components $\{a, d, f\},\{b, d, f\}$ is

$$
\left[\begin{array}{l}
X_{4} \\
X_{5} \\
X_{6}
\end{array}\right] \sim N\left(\left[\begin{array}{l}
0.920 \\
0.400 \\
0.284
\end{array}\right], \Sigma_{\{d, f\}}(\mathcal{B})=\left[\begin{array}{lll}
1.282 & 1.152 & 0.256 \\
1.152 & 1.440 & 0.230 \\
0.256 & 0.230 & 1.051
\end{array}\right]\right)
$$

We follow the same steps in reverse to decompose the global distribution into the local distributions. The joint distribution of $\mathbf{X}$ is a mixture with multivariate normal components and the associated probabilities. The latter are a function of the discrete variables $X_{1}, X_{2}, X_{3}$ : rearranging them as the three-dimensional table

$$
\begin{aligned}
& X_{1}=a \\
& X_{2} \\
& \begin{array}{c|c}
X_{2} \\
\hline e & c & d \\
\hline f & 0.040 & 0.040 \\
\hline 0.160 & 0.160
\end{array}
\end{aligned}
$$

$$
\begin{aligned}
& X_{1}=b \\
& \begin{array}{c|c}
X_{2} \\
\hline e & c & d \\
\hline e & 0.036 & 0.084 \\
\hline f & 0.144 & 0.336
\end{array}
\end{array}
$$

gives us the typical representation of $\mathrm{P}\left(X_{1}, X_{2}, X_{3}\right)$, which we can work with by operating over the different dimensions. We can then compute the conditional probability tables in the local distributions of $X_{1}$ and $X_{3}$ by marginalising over the remaining variables:

$$
\begin{aligned}
& \mathrm{P}\left(X_{1}\right)=\sum_{X_{2} \in\{c, d\}} \sum_{X_{3} \in\{c, f\}} \mathrm{P}\left(X_{1}, X_{2}, X_{3}\right) \\
& a \\
&=\left(0.040+0.160+0.040+0.160 \quad 0.036+0.144+0.084+0.336\right) \\
& a \quad b \\
&=\left(\begin{array}{ll}
0.4 & 0.6
\end{array}\right) \\
& \mathrm{P}\left(X_{3}\right)=\sum_{X_{1} \in\{a, b\}} \sum_{X_{2} \in\{c, d\}} \mathrm{P}\left(X_{1}, X_{2}, X_{3}\right) \\
& e \\
& \left(0.040+0.040+0.036+0.084 \quad 0.160+0.160+0.144+0.336\right) \\
& e \quad f \\
&=\left(\begin{array}{ll}
0.2 & 0.8
\end{array}\right)
\end{aligned}
$$

As for $X_{2}$, we marginalise over $X_{3}$ and normalise over $X_{1}$ to obtain

$$
\mathrm{P}\left(X_{2} \mid X_{1}\right)=\sum_{X_{3} \in\{c, f\}} \frac{\mathrm{P}\left(X_{1}, X_{2}, X_{3}\right)}{\mathrm{P}\left(X_{1}\right)}=\begin{array}{cc}
a & b \\
c & 0.040 \pm 0.160 \\
d & \frac{0.040}{0.4} \frac{0.160}{0.160}
\end{array} \quad \frac{0.036+0.144}{0.6} \quad \frac{0.084+0.336}{0.6} \quad \begin{array}{ll}
a & b \\
c \\
d
\end{array}
$$

The multivariate normal distributions associated with the mixture components are a function of the continuous variables $X_{4}, X_{5}, X_{6} . X_{4}$ has only one discrete parent $\left(X_{2}\right), X_{5}$ has two ( $X_{2}$ and $X_{3}$ ) and $X_{6}$ has none. Therefore, we only need to examine four mixture components to obtain the parameters of the local distributions of all three variables: one for which $\left\{X_{2}=c, X_{3}=e\right\}$, one for which $\left\{X_{2}=d, X_{3}=e\right\}$, one for which $\left\{X_{2}=c, X_{3}=f\right\}$ and one for which $\left\{X_{2}=d, X_{3}=f\right\}$.

If we consider the first mixture component $\{a, c, e\}$, we can apply the steps described Section 3.2 to decompose it into the local distributions of $X_{4}, X_{5}, X_{6}$ and obtain

$$
\begin{array}{ll}
X_{4}=0.1+0.2 X_{5}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.09) ; \\
X_{5}=0.1+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,0.09) ; \\
X_{6}=0.1+0.2 X_{4}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1) .
\end{array}
$$

Similarly, the third mixture component $\{a, d, e\}$ yields

$$
\begin{array}{ll}
X_{4}=0.6+0.8 X_{5}+\varepsilon_{X_{4}} & \varepsilon_{X_{4}} \sim N(0,0.36) \\
X_{5}=0.2+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,0.36) \\
X_{6}=0.1+0.2 X_{4}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1)
\end{array}
$$

The fifth mixture component $\{a, c, f\}$ yields

$$
\begin{array}{ll}
X_{4}=0.1+0.2 X_{5}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.09) \\
X_{5}=0.4+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,0.81) \\
X_{6}=0.1+0.2 X_{4}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1)
\end{array}
$$

The seventh mixture component $\{a, d, f\}$ yields

$$
\begin{array}{ll}
X_{4}=0.6+0.8 X_{5}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,0.36) \\
X_{5}=0.4+\varepsilon_{X_{5}}, & \varepsilon_{X_{5}} \sim N(0,1.44) \\
X_{6}=0.1+0.2 X_{4}+\varepsilon_{X_{6}}, & \varepsilon_{X_{6}} \sim N(0,1)
\end{array}
$$

Reorganising these distributions by variables we obtain the local distributions of $\mathcal{B}$ shown in Figure 3 top.
Example A3 (Entropy of a discrete BN). Consider again the discrete BN from Example A1. In this simple example, we can use its global distribution and (6) to compute

$$
\begin{aligned}
& \mathrm{H}(\mathcal{B})=-0.005 \log 0.005-0.013 \log 0.013-0.052 \log 0.052-0.050 \log 0.050- \\
& 0.064 \log 0.064-0.040 \log 0.040-0.037 \log 0.037-0.026 \log 0.026- \\
& 0.022 \log 0.022-0.051 \log 0.051-0.210 \log 0.210-0.199 \log 0.199- \\
& 0.089 \log 0.089-0.056 \log 0.056-0.051 \log 0.051-0.036 \log 0.036=2.440
\end{aligned}
$$

In the general case, we compute $\mathrm{H}(\mathcal{B})$ from the local distributions using (9). Since $X_{1}$ and $X_{2}$ have no parents, their entropy components simply sum over their marginal distributions:

$$
\begin{aligned}
& \mathrm{H}\left(X_{1}\right)=-0.53 \log 0.53-0.47 \log 0.47=0.691 \\
& \mathrm{H}\left(X_{2}\right)=-0.34 \log 0.34-0.66 \log 0.66=0.641
\end{aligned}
$$

For $X_{3}$,

$$
\mathrm{H}\left(X_{3} \mid X_{1}, X_{2}\right)=\sum_{x_{1} \in\{a, b\}} \sum_{x_{2} \in\{c, d\}} \mathrm{P}\left(X_{1}=x_{1}, X_{2}=x_{2}\right) \mathrm{H}\left(X_{3} \mid X_{1}=x_{1}, X_{2}=x_{2}\right)
$$

where

$$
\begin{aligned}
& \mathrm{H}\left(X_{3} \mid X_{1}=a, X_{2}=c\right)=-0.15 \log 0.15-0.85 \log 0.85=0.423 \\
& \mathrm{H}\left(X_{3} \mid X_{1}=a, X_{2}=d\right)=-0.75 \log 0.75-0.25 \log 0.25=0.562 \\
& \mathrm{H}\left(X_{3} \mid X_{1}=b, X_{2}=c\right)=-0.40 \log 0.40-0.60 \log 0.60=0.673 \\
& \mathrm{H}\left(X_{3} \mid X_{1}=b, X_{2}=d\right)=-0.80 \log 0.80-0.20 \log 0.20=0.500
\end{aligned}
$$

and where (multiplying the marginal probabilities for $X_{1}$ and $X_{2}$, which are marginally independent)

$$
\begin{array}{ll}
\mathrm{P}\left(X_{1}=a, X_{2}=c\right)=0.180, & \mathrm{P}\left(X_{1}=a, X_{2}=d\right)=0.350 \\
\mathrm{P}\left(X_{1}=b, X_{2}=c\right)=0.160, & \mathrm{P}\left(X_{1}=b, X_{2}=d\right)=0.310
\end{array}
$$

giving

$$
\mathrm{H}\left(X_{3} \mid X_{1}, X_{2}\right)=(0.180 \cdot 0.423+0.350 \cdot 0.562+0.160 \cdot 0.673+0.310 \cdot 0.500)=0.536
$$

Finally, for $X_{4}$

$$
\mathrm{H}\left(X_{4} \mid X_{3}\right)=\sum_{x_{3} \in\{e, f\}} \mathrm{P}\left(X_{3}=x_{3}\right) \mathrm{H}\left(X_{4} \mid X_{3}=x_{3}\right)
$$

where

$$
\begin{aligned}
& \mathrm{H}\left(X_{4} \mid X_{3}=e\right)=-0.20 \log 0.20-0.80 \log 0.80=0.500 \\
& \mathrm{H}\left(X_{4} \mid X_{3}=f\right)=-0.42 \log 0.42-0.58 \log 0.58=0.680
\end{aligned}
$$

and $\mathrm{P}\left(X_{3}=e\right)=0.601, \mathrm{P}\left(X_{3}=f\right)=0.399$, giving

$$
\mathrm{H}\left(X_{4} \mid X_{3}\right)=0.601 \cdot 0.500+0.399 \cdot 0.680=0.572
$$

Combining all these figures, we obtain $\mathrm{H}(\mathcal{B})$ as

$$
\mathrm{H}\left(X_{1}\right)+\mathrm{H}\left(X_{2}\right)+\mathrm{H}\left(X_{3} \mid X_{1}, X_{2}\right)+\mathrm{H}\left(X_{4} \mid X_{3}\right)=0.691+0.641+0.536+0.572=2.440
$$

as before.
In general, we would have to compute the probabilities of the parent configurations of each node using a junction tree as follows:

1. We construct the moral graph of $\mathcal{B}$, which contains the same arcs (but undirected) as its DAG plus $X_{1}-X_{2}$.
2. We identify two cliques $C_{1}=\left\{X_{1}, X_{2}, X_{3}\right\}$ and $C_{2}=\left\{X_{3}, X_{4}\right\}$ and a separator $S_{12}=\left\{X_{3}\right\}$.
3. We connect them to create the junction tree $C_{1}-S_{12}-C_{2}$.
4. We initialise the cliques with the respective distributions $\mathrm{P}\left(C_{1}\right)=\mathrm{P}\left(X_{1}, X_{2}, X_{3}\right)$, $\mathrm{P}\left(C_{2}\right)=\mathrm{P}\left(X_{3}, X_{4}\right)$ and $\mathrm{P}\left(S_{12}\right)=\mathrm{P}\left(X_{3}\right)$.
5. We compute $\mathrm{P}\left(X_{1}, X_{2}\right)=\sum_{x_{3} \in\{e, f\}} \mathrm{P}\left(C_{1}\right)$ and $\mathrm{P}\left(X_{3}\right)=\mathrm{P}\left(S_{12}\right)$.

Example A4 (Entropy of a GBN). Consider the GBN $\mathcal{B}$ from Figure 1 top, whose global distribution we derived in Example 2. If we plug its covariance matrix $\Sigma_{\mathcal{B}}$ into the entropy formula for the multivariate normal distribution we obtain

$$
\mathrm{H}(\mathcal{B})=\frac{4}{2}+\frac{4}{2} \log 2 \pi+\frac{1}{2} \log \operatorname{det}\left(\Sigma_{\mathcal{B}}\right)=2+3.676+0.5 \log 0.475=5.304
$$

Equivalently, plugging the $\sigma_{X_{i}}^{2}(\mathcal{B})$ into (12) we have

$$
\begin{aligned}
& \mathrm{H}(\mathcal{B})=\sum_{i=1}^{N} \mathrm{H}\left(X_{i} \mid \Pi_{X_{i}}^{B}\right)= \\
& \frac{1}{2}[\log (2 \pi \cdot 0.8)+\log (2 \pi \cdot 0.6)+\log (2 \pi \cdot 0.9)+\log (2 \pi \cdot 1.1)]+\frac{4}{2}=5.304
\end{aligned}
$$

Example A5 (KL between GBNs with parameters estimated from data). Consider the DAGs for the BNs $\mathcal{B}$ and $\mathcal{B}^{\prime}$ and the 10 observations shown in Figure A1. The partial topological ordering of the nodes in $\mathcal{B}$ is $\left\{\left\{X_{1}, X_{2}\right\}, X_{4}, X_{3}\right\}$ and that in $\mathcal{B}^{\prime}$ is $\left\{X_{1}, X_{2},\left\{X_{3}, X_{4}\right\}\right\}$ : the total ordering that is compatible with both is $\left\{X_{1}, X_{2}, X_{4}, X_{3}\right\}$.

If we estimate the parameters of the local distributions of $\mathcal{B}$ by maximum likelihood we obtain

$$
\begin{array}{ll}
X_{1}=2.889+\varepsilon_{X_{1}}, & \varepsilon_{X_{1}} \sim N(0,0.558) \\
X_{2}=1.673+\varepsilon_{X_{2}}, & \varepsilon_{X_{2}} \sim N(0,1.595) \\
X_{3}=0.896+1.299 X_{4}+\varepsilon_{X_{3}}, & \varepsilon_{X_{3}} \sim N(0,1.142) \\
X_{4}=-2.095+2.222 X_{1}+2.613 X_{2}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,1.523)
\end{array}
$$

and the associated fitted values are

$$
\begin{aligned}
& \widehat{\mathbf{x}}_{1}(\mathcal{B})=(2.889,2.889,2.889,2.889,2.889,2.889,2.889,2.889,2.889,2.889) \\
& \widehat{\mathbf{x}}_{2}(\mathcal{B})=(1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673,1.673) \\
& \widehat{\mathbf{x}}_{3}(\mathcal{B})=(17.293,14.480,8.675,13.937,14.846,12.801,13.449,2.394,9.670,14.381) \\
& \widehat{\mathbf{x}}_{4}(\mathcal{B})=(13.307,11.447,5.852,8.635,8.475,9.018,10.370,2.376,7.014,10.489)
\end{aligned}
$$

Similarly, for $\mathcal{B}^{\prime}$ we obtain

$$
\begin{array}{ll}
X_{1}=2.889+\varepsilon_{X_{1}}, & \varepsilon_{X_{1}} \sim N(0,0.558) \\
X_{2}=3.505-0.634 X_{1}+\varepsilon_{X_{2}}, & \varepsilon_{X_{2}} \sim N(0,1.542) \\
X_{3}=7.284+2.933 X_{2}+\varepsilon_{X_{3}}, & \varepsilon_{X_{3}} \sim N(0,6.051) \\
X_{4}=5.151+2.120 X_{2}+\varepsilon_{X_{4}}, & \varepsilon_{X_{4}} \sim N(0,3.999)
\end{array}
$$

and the associated fitted values are

$$
\begin{aligned}
& \widehat{\mathbf{x}}_{1}(\mathcal{B})=(2.889,2.889,2.889,2.889,2.889,2.889,2.889,2.889,2.889,2.889) \\
& \widehat{\mathbf{x}}_{2}(\mathcal{B})=(1.207,2.304,1.778,1.625,1.754,2.044,1.127,2.037,0.840,2.019) \\
& \widehat{\mathbf{x}}_{3}(\mathcal{B})=(15.529,17.760,9.408,11.931,12.261,14.009,11.918,6.528,7.019,15.564) \\
& \widehat{\mathbf{x}}_{4}(\mathcal{B})=(11.110,12.722,6.686,8.509,8.748,10.011,8.500,4.604,4.959,11.135)
\end{aligned}
$$

Therefore,

$$
\begin{array}{ll}
\left\|\widehat{\mathbf{x}}_{1}(\mathcal{B})-\widehat{\mathbf{x}}_{1}\left(\mathcal{B}^{\prime}\right)\right\|_{2}^{2}=0, & \left\|\widehat{\mathbf{x}}_{2}(\mathcal{B})-\widehat{\mathbf{x}}_{2}\left(\mathcal{B}^{\prime}\right)\right\|_{2}^{2}=2.018 \\
\left\|\widehat{\mathbf{x}}_{3}(\mathcal{B})-\widehat{\mathbf{x}}_{3}\left(\mathcal{B}^{\prime}\right)\right\|_{2}^{2}=54.434, & \left\|\widehat{\mathbf{x}}_{4}(\mathcal{B})-\widehat{\mathbf{x}}_{4}\left(\mathcal{B}^{\prime}\right)\right\|_{2}^{2}=21.329
\end{array}
$$

and the values of the Kullback-Leibler divergence for the individual nodes are

$$
\begin{aligned}
& \operatorname{KL}\left(X_{1} \mid \Pi_{X_{1}}^{B} \| X_{1} \mid \Pi_{X_{1}}^{B^{\prime}}\right) \approx \frac{1}{2}\left(\log \frac{0.558}{0.558}+\frac{0.558}{0.558}-1\right)+\frac{1}{20}\left(\frac{0}{0.558}\right)=0 \\
& \operatorname{KL}\left(X_{2} \mid \Pi_{X_{2}}^{B} \| X_{2} \mid \Pi_{X_{2}}^{B^{\prime}}\right) \approx \frac{1}{2}\left(\log \frac{1.542}{1.595}+\frac{1.595}{1.542}-1\right)+\frac{1}{20}\left(\frac{2.018}{1.542}\right)=0.066 \\
& \operatorname{KL}\left(X_{3} \mid \Pi_{X_{3}}^{B} \| X_{3} \mid \Pi_{X_{3}}^{B^{\prime}}\right) \approx \frac{1}{2}\left(\log \frac{6.051}{1.142}+\frac{1.142}{6.051}-1\right)+\frac{1}{20}\left(\frac{54.434}{6.051}\right)=0.878 \\
& \operatorname{KL}\left(X_{4} \mid \Pi_{X_{4}}^{B} \| X_{4} \mid \Pi_{X_{4}}^{B^{\prime}}\right) \approx \frac{1}{2}\left(\log \frac{3.999}{1.523}+\frac{1.523}{3.999}-1\right)+\frac{1}{20}\left(\frac{21.329}{3.999}\right)=0.440
\end{array}
$$

which sum up to $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right) \approx 1.383$. The exact value, which we can compute as shown in Section 4.2, is 1.692 .

The quality of the empirical approximation improves with the number of observations. For reference, we generated the data in Figure A1 from the GBN in Example 2. With a sample of size $n=100$ from the same network, $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right) \approx 1.362$ with $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=1.373$; with $n=1000$, $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right) \approx 1.343$ with $\operatorname{KL}\left(\mathcal{B} \| \mathcal{B}^{\prime}\right)=1.345$.

![img-4.jpeg](img-4.jpeg)


Figure A1. The DAGs for the GBNs $\mathcal{B}$ (top left) and $\mathcal{B}^{\prime}$ (bottom left) and the data (right) used in Example A5.

Example A6 (Entropy of a CLGBN). Consider again the CLGBN $\mathcal{B}$ from from Figure 3 (top). For such a simple BN, we can use its global distribution (which we derived in Example A2) directly to compute the entropies of the multivariate normal distributions associated with the mixture components

$$
\begin{aligned}
& \mathrm{H}\left(X_{4}, X_{5}, X_{6} \mid\{c, e\}\right)=\frac{3}{2}+\frac{3}{2} \log (2 \pi)+\frac{1}{2} \log \operatorname{det}\left(\Sigma_{\{c, e\}}(\mathcal{B})\right)=1.849 \\
& \mathrm{H}\left(X_{4}, X_{5}, X_{6} \mid\{d, e\}\right)=\frac{3}{2}+\frac{3}{2} \log (2 \pi)+\frac{1}{2} \log \operatorname{det}\left(\Sigma_{\{d, e\}}(\mathcal{B})\right)=3.235 \\
& \mathrm{H}\left(X_{4}, X_{5}, X_{6} \mid\{c, f\}\right)=\frac{3}{2}+\frac{3}{2} \log (2 \pi)+\frac{1}{2} \log \operatorname{det}\left(\Sigma_{\{c, f\}}(\mathcal{B})\right)=2.947 \\
& \mathrm{H}\left(X_{4}, X_{5}, X_{6} \mid\{d, f\}\right)=\frac{3}{2}+\frac{3}{2} \log (2 \pi)+\frac{1}{2} \log \operatorname{det}\left(\Sigma_{\{d, f\}}(\mathcal{B})\right)=3.928
\end{aligned}
$$

and to combine them by weighting with the component probabilities

$$
\begin{gathered}
\mathrm{H}\left(X_{4}, X_{5}, X_{6} \mid X_{1}, X_{2}, X_{3}\right)=\underbrace{0.040 \cdot 1.849}_{\{a, c, e\}}+\underbrace{0.036 \cdot 1.849}_{\{b, c, e\}}+\underbrace{0.040 \cdot 3.235}_{\{a, d, e\}}+\underbrace{0.084 \cdot 3.235}_{\{b, d, e\}}+ \\
\underbrace{0.160 \cdot 2.947}_{\{a, c, f\}}+\underbrace{0.144 \cdot 2.947}_{\{b, c, f\}}+\underbrace{0.160 \cdot 3.928}_{\{a, d, f\}}+\underbrace{0.336 \cdot 3.928}_{\{b, d, f\}}=3.386
\end{gathered}
$$

The entropy of the discrete variables is

$$
\begin{gathered}
\mathrm{H}\left(X_{1}, X_{2}, X_{3}\right)=-0.040 \log 0.040-0.036 \log 0.036-0.040 \log 0.040-0.084 \log 0.084- \\
0.160 \log 0.160-0.144 \log 0.144-0.160 \log 0.160-0.336 \log 0.336=1.817
\end{gathered}
$$

and then $\mathrm{H}(\mathcal{B})=\mathrm{H}\left(X_{1}, X_{2}, X_{3}\right)+\mathrm{H}\left(X_{4}, X_{5}, X_{6} \mid X_{1}, X_{2}, X_{3}\right)=5.203$.

If we use the local distributions instead, we can compute the entropy of the discrete variables using (9) from Section 4.1:

$$
\begin{aligned}
\mathrm{H}\left(X_{1}\right) & =-0.4 \log 0.4-0.6 \log 0.6=0.673 \\
\mathrm{H}\left(X_{2} \mid X_{1}\right) & =0.4(-0.5 \log 0.5-0.5 \log 0.5)+0.6(-0.3 \log 0.3-0.7 \log 0.7)=0.644 \\
\mathrm{H}\left(X_{3}\right) & =-0.2 \log 0.2-0.8 \log 0.8=0.500
\end{aligned}
$$

We can compute the entropy of the continuous variables with no discrete parents using (12) from Section 4.2:

$$
\mathrm{H}\left(X_{6} \mid X_{4}\right)=\frac{1}{2} \log (2 \pi \cdot 1)+\frac{1}{2}=1.419
$$

Finally, we can compute the entropy of the continuous variables with discrete parents using (24) from Section 4.3:

$$
\begin{aligned}
\mathrm{H}\left(X_{4} \mid X_{2}, X_{5}\right)= & 0.38\left(\frac{1}{2} \log (2 \pi \cdot 0.09)+\frac{1}{2}\right)+0.62\left(\frac{1}{2} \log (2 \pi \cdot 0.36)+\frac{1}{2}\right) \\
= & 0.645 \\
\mathrm{H}\left(X_{5} \mid X_{2}, X_{3}\right)= & 0.076\left(\frac{1}{2} \log (2 \pi \cdot 0.09)+\frac{1}{2}\right)+0.124\left(\frac{1}{2} \log (2 \pi \cdot 0.36)+\frac{1}{2}\right)+ \\
& 0.304\left(\frac{1}{2} \log (2 \pi \cdot 0.81)+\frac{1}{2}\right)+0.496\left(\frac{1}{2} \log (2 \pi \cdot 1.44)+\frac{1}{2}\right) \\
= & 1.322
\end{aligned}
$$

As before, we confirm that overall

$$
\begin{aligned}
\mathrm{H}(\mathcal{B})=\mathrm{H}\left(X_{1}\right)+ & \mathrm{H}\left(X_{2} \mid X_{1}\right)+\mathrm{H}\left(X_{3}\right)+\mathrm{H}\left(X_{4} \mid X_{2}, X_{5}\right)+\mathrm{H}\left(X_{5} \mid X_{2}, X_{3}\right)+ \\
& \mathrm{H}\left(X_{6} \mid X_{4}\right)=0.673+0.644+0.500+0.645+1.322+1.419=5.203
\end{aligned}
$$
