# Structural factor equation models for causal network construction via directed acyclic mixed graphs 

Yan Zhou ${ }^{1}$ | Peter X.-K. Song ${ }^{2}$ | Xiaoquan Wen ${ }^{2}$<br>${ }^{1}$ Gilead Sciences, Foster City, California<br>${ }^{2}$ Department of Biostatistics, University of Michigan, Ann Arbor, Michigan

## Correspondence

Peter X.-K. Song, Department of Biostatistics, University of Michigan, Ann Arbor, MI.
Email: pxsong@umich.edu

## Funding information

National Institute of Environmental Health Sciences, Grant/Award Number: R01ES024732; National Science Foundation, Division of Mathematical Sciences, Grant/Award Number: 1181734


#### Abstract

Directed acyclic mixed graphs (DAMGs) provide a useful representation of network topology with both directed and undirected edges subject to the restriction of no directed cycles in the graph. This graphical framework may arise in many biomedical studies, for example, when a directed acyclic graph (DAG) of interest is contaminated with undirected edges induced by some unobserved confounding factors (eg, unmeasured environmental factors). Directed edges in a DAG are widely used to evaluate causal relationships among variables in a network, but detecting them is challenging when the underlying causality is obscured by some shared latent factors. The objective of this paper is to develop an effective structural equation model (SEM) method to extract reliable causal relationships from a DAMG. The proposed approach, termed structural factor equation model (SFEM), uses the SEM to capture the network topology of the DAG while accounting for the undirected edges in the graph with a factor analysis model. The latent factors in the SFEM enable the identification and removal of undirected edges, leading to a simpler and more interpretable causal network. The proposed method is evaluated and compared to existing methods through extensive simulation studies, and illustrated through the construction of gene regulatory networks related to breast cancer.


KEYWORDS
directed acyclic graph, factor analysis model, network data, regularization, semi-Markov model

## 1 | INTRODUCTION

Reconstructing gene regulatory networks (GRN) using gene expression data furthers our understanding of gene function and cellular dynamics in biological systems by elucidating regulatory mechanisms. Graphical models are a popular tool to analyze and visualize conditional independence among variables of interest. A graphical model includes nodes representing random variables and edges encoding relationships between the enclosing nodes. Graphical models are classified into two classes depending on whether edges are directional: directed graphical mod-
els and undirected graphical models. A directed graphical model, also known as a Bayesian network, is a graphical model whose dependence structure is represented by a directed acyclic graph (DAG). For example, a directed edge between two genes may represent a molecular chain reaction of one gene regulating the other. The utility of DAGs for inferring causality has received much attention in the reconstruction of GRNs (Friedman et al., 2000; Pe'er et al., 2001; Hartemink et al., 2002; Segal et al., 2003).

When a DAG is used for causal network inference, some of the directed edges are often masked by undirected edges induced by unmeasured confounding variables.

The resulting graph may become a mixed graph with both directed and undirected edges, or even an undirected graph (Anandkumar et al., 2013). Thus, it seems inevitable to invoke a more general graph than a DAG to analyze the underlying network topology, in which undirected edges are allowed. This motivates us to focus on an analysis of causal relationships in a directed acyclic mixed graph (DAMG). DAMG is sometimes called an acyclic directed mixed graph (DMG), and also known as a semi-Markov model. It contains both directed and undirected edges, subject to the restriction of no directed cycles in the graph. In a DAMG, the set of directed edges represents the causal relationships between nodes and constitutes the DAG of interest. It can, however, be contaminated by undirected edges introduced by some unobserved factors. In practice, the latent factors may include, for example, biomarkers that are not included in experimental chips, environmental variables, and underlying populations among experimental samples. Unfortunately, such shared masking factors are often not directly measured in experiments despite their potential influence on measurements. In the literature, methods for removing these masking factors have not been systematically investigated. Here, we propose a new method that identifies and removes nuisance undirected edges in the reconstruction of causal relationships to obtain an interpretable causal network.

Learning the dependence structure of a DAG from data presents a significant challenge because the number of candidate DAGs can grow super-exponentially along with the number of nodes (Robinson, 1973). There are three types of approaches to learning DAG structures: search-and-score approaches, constraint-based approaches, and hybrid approaches. A search-and-score approach attempts to learn a DAG structure by optimizing some criteria, such as the Bayesian information criterion (BIC) or validation set likelihood, using either a search algorithm (Lam and Bacchus, 1994; Heckerman et al., 1995) or Bayesian posterior distribution (Friedman and Koller, 2003; Ellis and Wong, 2008; Zhou, 2011). A constraint-based approach tries to prune a set of possible edges identified by conditional independence hypothesis tests, including the wellknown Peter-Clark (PC) algorithm (Spirtes et al., 2000), or by removing conditional dependencies that fall below a threshold (Cheng et al., 2002). A constraint-based method is developed to prune a set of edges with a focus of improving computational efficiency (Li and Yang, 2004; Tsamardinos et al., 2006).

A vast majority of recent work has focused on the reconstruction of a sparse DAG through a penalized likelihood approach. In the special case where a topological ordering of the nodes is given, learning the structure of a DAG is equivalent to sparse estimation of the mod-
ified Cholesky decomposition of a concentration matrix (ie, the inverse of the corresponding covariance matrix), which is computationally feasible; see, for example, Li and Yang (2005), Huang et al. (2006), Levina et al. (2008), and Shojaie and Michailidis (2010), among others. The information on node ordering is usually determined by a natural ordering of temporal observations, previous experiments, and a priori knowledge (Shojaie and Michailidis, 2010). For example, when learning GRNs for microarray data, a priori knowledge of the node ordering could be obtained from the existing annotation software such as Cytoscape (Lopes et al., 2010). If there is no established known node ordering, some penalized score-based methods (eg, Fu and Zhou, 2013; Aragam and Zhou, 2015) may be first applied to estimate DAG structures, which is done without a priori knowledge of node ordering, followed by extracting the node ordering from the estimated DAG.

To fill in the technical gap where no systematic work is available to assess sparse causal relationships in DAMGs, we develop a regularization estimation method to extract and evaluate a sparse causal network in the form of a DAG. We develop a new method based on the structural factor equation model (SFEM) introduced in detail in Section 2 with conditions for model identifiability. Section 3 concerns the penalized estimation of DAGs based on an EM-coordinate-descent (EM-CD) algorithm for numerical implementation. Operating characteristics of the proposed method are examined on both simulated and real data in Sections 4 and 5. We conclude with a discussion in Section 6 in which we discuss the estimation of DAGs with unknown node ordering.

## 2 STRUCTURAL FACTOR EQUATION MODEL

## 2.1 | Model

Given a $P$-dimensional random vector $\mathbf{y}=\left(y_{1}, \ldots, y_{P}\right)^{T}$ with known variable ordering, we use a DAG $\mathcal{G}=(V, E)$ to describe causal relations, where $V$ is the set of vertices (or variables or nodes) and $E$ is the collection of edges. That is, each variable $y_{i}$ corresponds to one node in the DAG, and a directed edge between two nodes indicates a causal relationship between them. Without loss of generality, we assume that $\mathbf{y}$ has been sorted according to its known ordering, which means a causal relationship is only possible from variable $y_{j}$ to variable $y_{i}$, denoted by $y_{j} \rightarrow y_{i}$, for $j<i$. The set of parental nodes of $y_{i}$ is denoted by $p a(i)=\left\{j: j<i, y_{j} \rightarrow y_{i}\right\}$. Specifically, for any $k<i$, if $k \notin p a(i)$, then $y_{i}$ is independent of $y_{k}$ conditioning on $\left\{y_{j}\right\}_{j \in p a(i)}$.

To model causality among the components of $\mathbf{y}$, we invoke a structural equation model (SEM): $y_{i}=$ $\sum_{j \in p a(i)} \tilde{\sigma}_{i j} y_{j}+\varepsilon_{i}, i=1, \ldots, P$, where $\varepsilon_{i}$ 's are normal random errors with mean 0 and independent of $y_{i}$ 's parental nodes. Regression parameter $\tilde{\sigma}_{i j}$ is a coefficient representing the association of $y_{i}$ with $y_{j}$, conditional on all other parental nodes of $y_{i}$. The matrix form of the SEM is: $\mathbf{y}=\Theta \mathbf{y}+\boldsymbol{\varepsilon}$, where the vector of errors $\boldsymbol{\varepsilon}=\left(\varepsilon_{1}, \ldots, \varepsilon_{P}\right)^{T}$ has mean 0 and covariance $W$. Here, $\Theta=\left\{\tilde{\sigma}_{i j}\right\}$ is a $P \times P$ lower triangular matrix with zeros on the diagonal, and is termed the weighted adjacency matrix of the DAG $\mathcal{G}$. Given both $\Theta$ of DAG $\mathcal{G}$ and $W$, the first two moments of the SEM are $\boldsymbol{\mu}=E(\mathbf{y})=0$ and $\Sigma=\operatorname{Cov}(\mathbf{y})=(I-\Theta)^{-T} W(I-$ $\Theta)^{-1}$, which are uniquely determined by the two matrices $\Theta$ and $W$. This formulation requires a priori variable ordering.

We propose to model the covariance $W$ by the classical factor analysis model (FAM): $W=B B^{T}+\Psi$, where $B$ is a $P \times K$ factor loading matrix for $K(\leq P)$ latent factors and $\Psi$ is a $P \times P$ diagonal matrix of uniqueness (Johnson and Wichern, 2007). Combining the SEM and FAM models leads to the following SFEM:

$$
\mathbf{y}=\Theta \mathbf{y}+B \mathbf{z}+\mathbf{e}
$$

where $\mathbf{z}$ is a $K$-variate vector of uncorrelated latent factors following multivariate normal distribution $\operatorname{MVN}_{K}(0, I)$ and $\mathbf{e}$ is an error vector distributed according to $\operatorname{MVN}_{P}(0, \Psi)$ and is independent of $\mathbf{z}$. Moreover, the first two moments of $\mathbf{y}$ are, respectively, $\boldsymbol{\mu}=0$ and $\Sigma=(I-\Theta)^{-T}\left(B B^{T}+\Psi\right)(I-\Theta)^{-1}$. It is obvious that SFEM in (1) reduces to the classical SEM when $K=0$. From (1), we can also see that conditioning on the vector of $K$ unobserved latent variables $\mathbf{z}$, the vector of variables y satisfies the SEM for a DAG. Our objective is to estimate the weighted adjacency matrix $\Theta$ of interest, the loading matrix $B$ and uniqueness $\Psi$, as well as to determine the number of factors $K$.

## 2.2 | Graphical representation of SFEM

Due to the potential influence of latent factors on causal relationships, we consider a more general graphical model than a DAG to accommodate undirected edges. We consider the class of DMGs that contain both directed and undirected edges. A mixed graph is defined by $\mathcal{G}=$ $(V, E, U)$, where $V$ is a finite set of vertices and $E, U \subseteq$ $V \times V$ are two disjoint sets of edges. The edges in $E$ are directed; that is, $(i, j) \in E \Rightarrow(j, i) \notin E$, denoted by $i \rightarrow j$. The edges in $U$ are undirected or bidirected; that is, $(i, j) \in$ $E \Rightarrow(j, i) \in E$ and vice versa, denoted by $i \leftrightarrow j$. Part A of Figure 1 displays four examples of DMGs. The DMG shown
in Panel A(b) is cyclic, a type of DMG that is not considered in this paper.

In this paper, we focus on DAMGs, a subclass of DMGs that do not include directed cycles. More specifically, a DAMG $(V, E, U)$ consists of two subgraphs: one is a DAG $(V, E)$ consisting of all directed edges, which is captured by a weighted adjacency matrix $\Theta$; and the other is a subgraph containing all undirected edges $(V, U)$, which are obtained by nonzero entries in the covariance matrix $W=$ $B B^{T}+\Psi$ with $W_{i j}=W_{j i} \neq 0$ for $(i, j) \in U$ or $i=j$. In the GRN study, common factors attributed to matrix $B$ could include, for example, environmental variables, which are not measured but may alter gene expressions substantially. These factors are useful to explain the mechanism of generation of undirected edges that contaminate the underlying causal relationships of interest. For example, Figures 1A(c) and A(d) show that the directed chain networks among nodes $Y_{1}, Y_{2}$, and $Y_{3}$ (which contains a subgraph of interest, namely, Figure 1A(a), shown by the arrowed solid edges) are masked by undirected edges (indicated by dashed lines). Intuitively, it would be impossible to reconstruct a DAG (ie, the chain graph in Panel A(a)) if these nuisance undirected edges were not properly removed. Our strategy is to identify and quantify potential triggers of undirected edges via the factor model, as illustrated in Part B of Figure 1. Figure 1B shows an example in which undirected edges arise from three shared common latent factors $z_{1}, z_{2}$, and $z_{3}$ among the nine measured variables $y_{1}, \ldots, y_{9}$; marginalizing these latent factors will lead to many nuisance undirected edges in a complex DAMG. The proposed SFEM is developed to identify and reconstruct this DAG by conditioning out the three latent triggers responsible for the nuisance edges.

## 2.3 | Parameter identifiability in SFEM

The parameters in the SFEM (1) include a lower triangular $P \times P$-weighted adjacency matrix $\Theta$, a $P \times K$ factor loading matrix $B$, and a diagonal $P \times P$ uniqueness matrix $\Psi$. The SFEM (1) may be rewritten as

$$
\mathbf{y}=(I-\Theta)^{-1} B \mathbf{z}+(I-\Theta)^{-1} \mathbf{e}=\Gamma \mathbf{z}+\boldsymbol{\delta}
$$

where $\Gamma=(I-\Theta)^{-1} B$ and $\boldsymbol{\delta}=(I-\Theta)^{-1} \mathbf{e}$. The resulting covariance matrix of $\mathbf{y}$ is $\Sigma=\Gamma \Gamma^{T}+\Sigma_{\delta}$ with $\Sigma_{\delta}=(I-$ $\Theta)^{-1} \Psi(I-\Theta)^{-T}$. It is well known that the factors and loadings are not separably identified without further restrictions. Note that the factors $\mathbf{z} \sim \operatorname{MVN}_{K}(0, I)$ and loadings $B$ enter the likelihood through $\Gamma \Gamma^{T}$. Hence, for any $K \times$ $K$ rotation matrix $\Pi$, we have $\Gamma \Gamma^{T}=\Gamma \Pi \Pi^{T} \Gamma^{T}$, producing observationally equivalent models. Thus, we impose the

A. Four examples of directed mixed graphs.
![img-0.jpeg](img-0.jpeg)
B. An acyclic directed mixed graph containing a DAG.
![img-1.jpeg](img-1.jpeg)

FIG U R E 1 Part A presents four examples of directed mixed graphs. The graph in A(b) is cyclic, while all others are acyclic. An arrowed solid line indicates a directed edge and a dashed line denotes an undirected (or bidirected) edge. Part B presents an acyclic directed mixed graph that contains a DAG with the directed edges (arrowed solid lines) among nine observed variables $y_{1}, \ldots, y_{9}$ and a set of undirected edges induced by three common latent factors $z_{1}, z_{2}$, and $z_{3}$. This figure appears in color in the electronic version of this article, and any mention of color refers to that version
following regularity conditions to identify parameters in both $\Sigma_{\delta}$ and $\Gamma$ in model (2).

- Condition (A): Assume that $\Gamma^{T} \Sigma_{\delta}^{-1} \Gamma=B^{T} \Psi^{-1} B$ is diagonal with distinct entries arranged in a decreasing order.
- Condition (B): Assume that there exists a unique modified Cholesky decomposition of $\Sigma_{\delta}=(I-\Theta)^{-1} \Psi(I-$ $\Theta)^{-T}$.

Condition (A) is a usual restriction for maximum likelihood estimation (MLE) in FAM (see, eg, Lawley and Maxwell, 1962; Bai and Li, 2012). This condition is needed to ensure that the reparameterization does not affect the decomposition of the total variance into a sum of loadings $B$ and uniqueness $\Psi$. In other words, it ensures that solutions from the MLE obtained under the reparameterization can be uniquely transformed back to the origi-
nal parameterization. Condition (B) is required to prohibit the arbitrary permutation of node ordering, so that the solution from the algorithm is unique. By taking $\Sigma_{\delta}^{-1}=$ $(I-\Theta)^{T} \Psi^{-1}(I-\Theta)$, we obtain an alternative estimator to the classic SEM. The fact that the DAG representation $(\Theta, \Psi)$ encodes more conditional independence relations than the inverse covariance matrix $\Sigma_{\delta}^{-1}$ motivates us to obtain $\Theta$ for a simple and interpretable causal network.

## 3 | REGULARIZED ESTIMATION

## 3.1 | Formulation

Regularization methods are appealing in network learning settings because the dimension of unknown parameters (eg, entries in $\Theta$ ) can quickly exceed the sample size

of the data. When natural ordering of the variables is available, and the number of latent factors $K=0$ (ie, $B=0$ ), the reconstruction of a sparse DAG is equivalent to the sparse estimation of the modified Cholesky decomposition of $\Sigma_{g}^{-1}$. In this case, the identifiability condition (A) automatically holds. Several regularization approaches have been proposed to shrink elements in $\Theta$ to zero. See Pourahmadi (1999), Wu and Pourahmadi (2003), Huang et al. (2006), Bickel and Levina (2008), and Levina et al. (2008), just to name a few. More specifically, Huang et al. (2006) proposed adding an $L_{1}$ norm penalty on $\Theta$ to encourage zeros. Levina et al. (2008) proposed a banding procedure using a nested LASSO penalty. Recently, Shojaie and Michailidis (2010) employed the adaptive LASSO penalty to estimate the skeleton of a DAG in SEMs and showed that the LASSO method is not sensitive to random permutations of the order of variables in $\mathbf{y}$.

Given $N$ samples $\mathbf{y}_{n}=\left(y_{n 1}, \ldots, y_{n P}\right)^{T}, n=1, \ldots, N$, we want to detect the sparse skeleton of a DAG adjusting for latent factors. We propose the following penalized loss function:

$$
\begin{aligned}
& \min _{\Theta} \frac{1}{2 N} \sum_{n=1}^{N}\left(\mathbf{y}_{n}-\Theta \mathbf{y}_{n}\right)^{T}\left(B B^{T}+\Psi\right)^{-1}\left(\mathbf{y}_{n}-\Theta \mathbf{y}_{n}\right) \\
& \quad+\lambda \sum_{i=1}^{P} \sum_{j=1}^{i-1} \xi_{i j}\left|c_{i j} \mathcal{O}_{i j}\right|
\end{aligned}
$$

where $\lambda$ is a nonnegative tuning parameter, $c_{i j}$ represents the prior causal relationship of $y_{j}$ on $y_{i}$, and $\xi_{i j}$ is the adaptive weights of $y_{j}$ on $y_{i}$. The $L_{1}$ norm penalty term in the above loss function (3) regularizes the sparsity in $\Theta$.

Prior knowledge on the existence of causal relationships in $\mathbf{y}$ can be incorporated into the regularization procedure through a prespecified $P \times P$ flag matrix $C=\left\{c_{i j}\right\}$, whose $(i, j)$ th element is given by:

$$
c_{i j}= \begin{cases}1 & \text { if there is no prior information of causality } \\ & \text { between } j \text { and } i \text {, when } j<i \\ 0 & \text { if there exists prior knowledge of } \\ & \text { causality } j \rightarrow i \text {, when } j<i\end{cases}
$$

Matrix $C$ in the penalty function is useful for screening all available edges in exploratory analyses. In addition, $\Xi=$ $\left\{\xi_{i j}\right\}$ is a $P \times P$ lower triangular matrix of adaptive weights with the $(i, j)$ th element given by

$$
\xi_{i j}= \begin{cases}\max \left(1,\left|\tilde{\mathcal{O}}_{i j}\right|^{-y}\right), & \text { if } c_{i j}=1 \text { and } j<i \\ 0, & \text { otherwise }\end{cases}
$$

where $\tilde{\mathcal{O}}_{i j}$ is the estimate of $\mathcal{O}_{i j}$ obtained from the classical LASSO estimation given by (3) with $\xi_{i j}=1$ if $c_{i j}=1$ and $j<i$.

### 3.2 | EM-coordinate-descent algorithm

We propose a two-step iterative approach to estimate three unknown matrices $(\Theta, B, \Psi)$. Given the current estimates $\left(B^{(t)}, \Psi^{(t)}\right), \Theta^{(t+1)}$ is updated by minimizing the penalized loss function (3) using the coordinate descent (CD) algorithm, and then $\left(B^{(t+1)}, \Psi^{(t+1)}\right)$ are updated through the EM algorithm. Both the EM and CD algorithms are discussed below. Repeating the two-step procedure iteratively until convergence yields estimates $(\hat{\Theta}, \hat{B}, \hat{\Psi})$.

EM algorithm. We use the EM algorithm to estimate $(B, \Psi)$ in the FAM. We can implement the EM algorithm by treating the latent factors $\mathbf{z}_{n}=\left(z_{n 1}, \ldots, z_{n K}\right)^{T}, n=1, \ldots, N$ as "missing data" and $\Theta$ as a fixed "known" constant matrix. The M-step maximizes the log-likelihood of the full data $\left\{\left(\mathbf{y}_{n}^{*} \triangleq \mathbf{y}_{n}-\Theta \mathbf{y}_{n}, \mathbf{z}_{n}\right), n=1, \ldots, N\right\}$. We outline the EM algorithm to update $B$ and $\Psi$, respectively, at the $(t+1)$ th iteration. In the E-step, we obtain the following moments of $\mathbf{z}_{n}, n=1, \ldots, N$,

$$
\begin{aligned}
E\left(\mathbf{z}_{n} \mid \mathbf{y}_{n}^{*} ; B, \Psi\right)= & \left(B^{T} \Psi^{-1} B+I_{K}\right)^{-1} B^{T} \Psi^{-1} \mathbf{y}_{n}^{*} \\
\operatorname{Var}\left(\mathbf{z}_{n} \mid \mathbf{y}_{n}^{*} ; B, \Psi\right)= & I_{K}-B^{T} \Psi^{-1} B\left(B^{T} \Psi^{-1} B+I_{K}\right)^{-1} \\
E\left(\mathbf{z}_{n} \mathbf{z}_{n}^{T} \mid \mathbf{y}_{n}^{*} ; B, \Psi\right)= & E\left(\mathbf{z}_{n} \mid \mathbf{y}_{n}^{*} ; B, \Psi\right) E\left(\mathbf{z}_{n}^{T} \mid \mathbf{y}_{n}^{*} ; B, \Psi\right) \\
& +\operatorname{Var}\left(\mathbf{z}_{n} \mid \mathbf{y}_{n}^{*} ; B, \Psi\right)
\end{aligned}
$$

In the M-step, $B$ and $\Psi$ are updated at the $(t+1)$ th iteration by, respectively,

$$
\begin{aligned}
B^{(t+1)}= & \left\{\sum_{n=1}^{N} \mathbf{y}_{n}^{*} E\left(\mathbf{z}_{n}^{T} \mid \mathbf{y}_{n}^{*} ; B^{(t)}, \Psi^{(t)}\right)\right\} \\
& {\left[\sum_{n=1}^{N}\left\{E\left(\mathbf{z}_{n} \mathbf{z}_{n}^{T} \mid \mathbf{y}_{n}^{*} ; B^{(t)}, \Psi^{(t)}\right)\right\}\right]^{-1}} \\
\Psi^{(t+1)}= & \frac{1}{N} \sum_{n=1}^{N} E\left\{\left(\mathbf{y}_{n}^{*}-B \mathbf{z}_{n}\right)\left(\mathbf{y}_{n}^{*}-B \mathbf{z}_{n}\right)^{T} \mid \mathbf{y}_{n}^{*} ; B^{(t)}, \Psi^{(t)}\right\}
\end{aligned}
$$

Noting that when $\Psi$ takes the special form $\Psi=\sigma^{2} I_{P}$, we consider a simple reparameterization by letting $\hat{B}=\sigma^{-1} B$ and $\hat{\mathbf{z}}_{n}=\sigma \mathbf{z}_{n}$. Clearly, $B \mathbf{z}_{n}$ and $\hat{B} \hat{\mathbf{z}}_{n}$ follow the same distribution. Thus, the EM algorithm updates $\hat{B}$ and $\sigma^{2}$ by the

following expressions:

$$
\begin{aligned}
& \hat{B}^{(t+1)}=\left\{\sum_{n=1}^{N} \mathbf{y}_{n}^{*} E\left(\hat{\mathbf{z}}_{n}^{T} \mid \mathbf{y}_{n}^{*} ; \hat{B}^{(t)}, \sigma^{2^{(t)}}\right)\right\} \\
& \times\left\{\sum_{n=1}^{N} E\left(\hat{\mathbf{z}}_{n} \hat{\mathbf{z}}_{n}^{T} \mid \mathbf{y}_{n}^{*} ; \hat{B}^{(t)}, \sigma^{2^{(t+1)}}\right)\right\}^{-1} \\
& \sigma^{2^{(t+1)}}=\frac{1}{N Q} \sum_{n=1}^{N} \mathbf{y}_{n}^{* T}\left\{I_{Q}-\hat{B}^{(t)}\left(I_{K}+\hat{B}^{T(t)} \hat{B}^{(t)}\right)^{-1} \hat{B}^{T(t)}\right\} \mathbf{y}_{n}^{*}
\end{aligned}
$$

Coordinate descent algorithm. We implement a CD algorithm to obtain the optimal solution that minimizes the $L_{1}$-norm penalized loss function (3) under a fixed positivedefinite matrix $W=B B^{T}+\Psi$. The sparse solution of $\Theta$ is obtained efficiently by an active-shooting algorithm. Refer to Section 1 of the Supporting Information for details.

EM-CD algorithm. Combining the EM and CD algorithms, termed the EM-CD algorithm, we can iteratively update $\Theta, B$, and $\Psi$ as follows:

Step 1. Initialization of $\Theta^{(0)}, \Psi^{(0)}$, and $\Theta^{(0)}$ with some suitable values.
Step 2. Given $\left(B^{(t)}, \Psi^{(t)}, \Theta^{(t)}\right)$, update $\Theta^{(t+1)}$ by the CD active-shooting algorithm.
Step 3. Given $\Theta^{(t+1)}$, update $\left(B^{(t+1)}, \Psi^{(t+1)}\right)$ via the EM algorithm until convergence.
Step 4. Repeat steps 2 to 3 above until convergence.

## 3.3 | Tuning parameter selection

Choosing the number of latent factors $K$ and tuning the sparsity parameter $\lambda$ are both of critical importance in the proposed method. Since $K$ can affect the resulting sparsity in the estimated $\Theta$, it has to be tuned properly. In the FAM literature, some methods have been developed for selecting $K$. For example, Bai and Ng (2002) and Onatski (2010) proposed methods to determine the number of factors in certain approximate FAMs. Onatski (2009) developed test statistics for a hypothesized number of factors using the empirical distribution of eigenvalues of the sample covariance matrix. Hirose and Konishi (2012) and Caner and Han (2014) employed shrinkage estimation to determine relevant factors. Here, we invoke an "eigenvalue ratio (ER)" criterion (Ahn and Horenstein, 2013) to select $K$, mainly for its simplicity and computational ease. In a general factor model given in (2), we can convert the selection of $K$ in the original loading matrix $B$ to that in the new loading
matrix Г. Following Ahn and Horenstein (2013), for a sample covariance matrix $Y Y^{T} /(N P)$, denote its $k$ th largest eigenvalues by $\eta_{k}, k=1, \ldots, \min (N, P)$. The corresponding ER is given by $\operatorname{ER}(k)=\eta_{k} / \eta_{k+1}$. The ER criterion is given by $K_{\mathrm{ER}}=\arg \max _{K_{\min } \leq k \leq K_{\max }} \operatorname{ER}(k)$, where $K_{\min }$ and $K_{\max }$ may be prespecified according to the scree plot, say, $K_{\min }=1$ or 2 and $K_{\max }=\min (N, P) / 2$.

To select tuning parameter $\lambda$, we adopt $M$-fold crossvalidation. Since the true model is believed to be sparse, we use the ordinary least squares (OLS) estimates instead of the shrunken estimates to calculate the cross-validation error score. This is because the cross-validation error score based on the shrunken estimates often leads to severe false positive (FP) rates when there are many potential poor predictors (Efron et al., 2004; Peng et al., 2010). The OLS estimates are suggested in the literature as a reasonable remedy, as confirmed in our simulation studies. The BIC, another popular tuning parameter selection method, is not considered here mainly because estimating the degrees of freedom required by the BIC is difficult under a nonorthogonal design.

## 4 | SIMULATION EXPERIMENTS

## 4.1 | Simulation setup

To examine the performance of the proposed SFEM for the estimation of a sparse DAG in DAMGs, we consider two types of DAG designs.

In simulation experiment I, we consider a small and simple DAG with $P=50$ nodes and $M=25$ edges that is randomly generated by the R-package pcalg (Kalisch and Bühlmann, 2007). To control for the sparsity of the DAG, we set the maximum number of parents for each node at 2 , and the depth of the DAG to 3 , and then randomly generate DAGs until the exact number of $M=25$ edges is achieved.

In simulation experiment II, we consider a more complex DAG consisting of 19 master regulators (ie, parental nodes). Among them, four are strong master regulators, each influencing 14 to 18 nodes, seven are moderate master regulators, each influencing three to seven nodes, and the rest are 8 weak parental nodes that link to only one or two offspring nodes. Such a DAG is generated by first randomly selecting 19 master parental nodes, and then further randomly selecting offspring nodes within each parental node. As a result, we create a DAG with $M=100$ edges. In this second experiment, we vary both the number of nodes and the number of latent factors. We set up the SFEM with fixed $P=200$ nodes and a varying number of latent factors $K=1,5,10$, and also set up the SFEM with fixed $K=5$ but

varying number of nodes $P=50,100,200$. Clearly, with a fixed number of edges $M=100$, a larger number of nodes $P$ leads to a sparser network.

In both simulation designs, we generate $N=25$ and 100 units of networks, respectively, from the specified SFEMs above. In addition, we generate the elements of the weighted adjacency matrix $\Theta$ by $\theta_{i j} \stackrel{i . i . d .}{\sim}$ $U([-3,-1] \bigcup[1,3])$ in Simulation I, and set constant $\theta_{i j}=$ 0.5 in Simulation II. In each case, we simulate latent factors $z_{n k} \stackrel{i . i . d .}{\sim} N(0,1)$, loadings $B_{i k} \stackrel{i . i . d .}{\sim} U([-b,-a] \bigcup[a, b])$ and noise $e_{n j} \stackrel{i . i . d}{\sim} N\left(0, \sigma^{2}\right)$, where the parameters $a, b$, and $\sigma^{2}$ are chosen to satisfy a prespecified percent of explained variability (PEV): $P E V=\sqrt{\operatorname{tr}\left(\Sigma_{\delta}\right) / \operatorname{tr}(\Sigma)}$, where $\Sigma_{\delta}=(I-$ $\Theta)^{-1} \Psi(I-\Theta)^{-T}$ and $\Sigma=(I-\Theta)^{-1}\left(B B^{T}+\Psi\right)(I-\Theta)^{-T}$. The tuning parameter $\lambda$ is determined by five-fold crossvalidation. In both simulation studies, 50 replicates are carried out to draw summary statistics.

The performances of the proposed estimation method and algorithm are compared mainly under three cases, including (a) the latent factors are ignored, ie, $K=0$, which is equivalent to the method proposed by Shojaie and Michailidis (2010); (b) the number of latent factors $K$ is overspecified or underspecified, corresponding to overestimation or underestimation of the latent factors covariance $W$ in a DAMG; and (c) the number of latent factors $K$ is selected by the proposed ER method, ie, $K=K_{E R}$. See the detail in Section 3.3.

For each simulated dataset, we generate the solution paths for the elements of $\Theta$ using a geometric sequence of values for $\lambda$, starting from the largest value $\lambda_{\max }$ at which $\widehat{\Theta}_{\lambda_{\max }}=\mathbf{0}$ and decreasing to the smallest value $\lambda_{\min }=10^{-4}$. Note that the total number of detected edges increases as $\lambda$ decreases. We then evaluate the performances of both estimation method and algorithm under different numbers of latent factors nested within a series of tuning parameter values. We also compare the performances of the proposed estimation method and algorithm with two top methods in the literature, namely, the score-based method available in the R-package sparsebn (Aragam et al., 1956) (which is referred to as sparsebn hereafter), and the PC-algorithm implemented in the Rpackage pcalg (Kalisch and Bühlmann, 2007), where the significance levels of the PC-algorithm are given by a geometric sequence of values $\left\{10^{-15}, \ldots, 0.95\right\}$. Neither the sparsebn nor the PC-algorithm requires the knowledge of node ordering as an input. An advantage of the SFEM is that it enables the use of partial knowledge on the node order to improve the statistical analysis. In practice, partial prior knowledge of biological network structure may be obtained from existing pathway databases. To give the highest favor to these existing methods, when reporting the results from the software, we simply ignore the edge direc-
tion or equivalently assume that the direction is always correctly detected.

### 4.2 Findings from simulation studies

Figure 2 shows two plots of the average number of correctly detected edges against the total number of detected edges over different numbers of latent factors $K$ over 50 replicates. This figure appears in color in the electronic version of this article, and any mention of color refers to that version. Here, "oracle" refers to the case where the proposed regularized estimation is carried out by using the true covariance matrix $W=B B^{T}+\Psi$ without estimating $B$ and $\Psi$, namely, the EM algorithm is not used in the estimation. We find that the proposed SFEM method in the case of $K=K_{E R}$ with estimated $B$ and $\Psi$ produces results very close to those obtained in the "oracle" case. This suggests that the EM algorithm works well to estimate the $W$ matrix. Also, we see that the SFEM method with $K=K_{\text {true }}$, equal to 2 in the top Panel A and 5 in the bottom Panel B of Figure 2, outperforms all the other cases with misspecified $K$.

The performances of the PC-algorithm and the sparsebn method appear to be the worst, and are even worse than the SFEM with $K=0$ where no latent factors are accounted for in the analysis. Figure 2A shows that under a relatively light degree of masking $(K=2)$, the proposed $\operatorname{SFEM}(K=0)$ can gradually pick up more true signals when more false discoveries are allowed. In contrast, neither the PC-algorithm nor the sparsebn method show any noticeable improvement. This is probably because both the PC-algorithm and the sparsebn method do not use any a priori knowledge of node ordering. In Figure 2B with 100 detected edges, the sparse SFEM with $K=K_{\mathrm{ER}}$ can detect more than $95 \%$ of the true edges correctly with an average standard deviation of 1.45 edges, whereas the PC-algorithm or the score-based method can only detect about $10 \%$ of the true edges successfully. In other words, the unmeasured confounding factors can severely impair the performances of the PC-algorithm and the sparsebn method. The quality of our method is further measured by the average number of true positive (TP), FP and false negative (FN) edges, sensitivity (Sen), and Matthews correlation coefficient score (MCC). Table 1 summarizes the average performance of the SFEM with $K=K_{E R}$ for different numbers of $P$ in the second simulation experiment with $K_{\text {true }}=5$. For example, when $P=200$, on average, the estimated graph is able to identify 104.04 directed edges, of which 98.12 edges are the true edges, and the other 5.92 edges are false. In the case of $P=200$, the number of parameters to be estimated is around 20000 , which is much larger than the sample size

![img-2.jpeg](img-2.jpeg)

FIG U R E 2 Summary results from two DAGs designed in the simulation studies. The $x$-axis is the total number of detected edges, and the $y$-axis is the average number of correctly identified edges over 50 replicates. The vertical (gray) line corresponds to the number of true edges. Panel A displays the results from the first small DAG simulation design with $P=50, M=25, K=2, N=25$ as well as the estimated $K_{E R}=2$. Panel B shows the results of the second large DAG simulation design with $P=200, M=100, K=5, N=100$ as well as the estimated $K_{E R}=5$. This figure appears in color in the electronic version of this article, and any mention of color refers to that version

TABLE 1 Performance comparison with different number of nodes, $P=50,100,200$ under the second large DAG simulation design with $M=100, K=5$, and $N=100$


$N=100$. In this high-dimensional setting with a substantial amount of masking by $K=5$ latent factors, results in Table 1 suggest that our regularization method can estimate the DAG structure with reasonable accuracy even with the limited sample size $N=100$. When the network is relatively simpler with $P=50$ or 100 , the proposed estimation method and algorithm perform even better.

Table 2 lists the results of both simulation experiments I and II with different numbers of latent factors and different percents of explained variability. Table 2 suggests that the proposed ER criterion works well in selecting the number of latent factors, except for the case of Simulation II with $\mathrm{PEV}=1: 2$. This is because in this setting, PEV is relatively small, and the ER criterion is always in favor of a stronger nuisance covariance structure with two latent factors. However, it is interesting to notice that, although the nuisance structure is slightly overestimated (ie, one additional factor to the true $K=1$ ), the resulting performance $\left(K_{E R}=2\right)$ still appears much better than that with an underspecified nuisance structure $(K=0)$, judging by, for example, $\mathrm{MCC}=0.85$ versus 0.29 . As shown in Table 2, either ignoring or underspecifying the number of latent
factors results in abundant nonzero entries in $\Theta$, many of which may be false edges. In contrast, if the number of factors is overestimated, the proposed method would produce a sparse $\Theta$ matrix, leading to many FN discoveries. The latter presents a conservative analysis that fails to detect some of the true signals, which is often a more favorable scenario than the former, which reports excessive false signals. In summary, the proposed SFEM with $K_{E R}$ shows a satisfactory performance with the highest sensitivity and MCC, as well as the lowest false discovery rate.

Section 2 of the Supporting Information provides some additional simulation results for the comparison of SFEM, PC-algorithm, and sparsebn in both DAG simulation settings.

### 4.3 | Sensitivity analysis on the knowledge of node ordering

An input of a priori node ordering presents a noticeable limitation on the proposed SFEM method. We further assess the performance of the proposed method under three scenarios: (a) fully known node ordering, (b) fully unknown node ordering, and (c) partially known node ordering. The third scenario is most likely to occur in practice, given that practitioners often know part of a network under investigation based on their own experiences and relevant publications. Here, we use the setting of Simulation II with $P=200, K=5, N=100, P E V=1: 4$, and $M=100$. Figure 3 reports the results.

In scenario (b) of fully unknown node ordering, we first apply the sparsebn method on each of 50 simulated

TABLE 2 Results from both small and large DAG simulation designs, respectively, where the number of latent factors $K$ and the percent of explained variability (PEV) vary over four cases


![img-3.jpeg](img-3.jpeg)

FIGURE 3 Summary results based on the large DAG simulation design with $P=200, M=100, K=5, N=100$ as well as the estimated $K_{E R}=5$. The $x$-axis is the total number of detected edges, and the $y$-axis is the number of correctly identified edges averaged over 50 replicates. The vertical (black) line corresponds to the number of true edges. This figure appears in color in the electronic version of this article, and any mention of color refers to that version
datasets $Y_{(s)}, s=1, \ldots, 50$ to learn the underlying node ordering order ${ }_{(s)}$ of the network. Reordering the nodes $Y_{(s)}$ based on the learned order ${ }_{(s)}$ leads to a reordered $Y_{(s)}^{*}$. Finally, we apply our SFEM method on $Y_{(s)}^{*}, s=$ $1, \ldots, 50$. In scenario (c) of partially known node ordering, our design is given as follows. Since the true DAG in the Simulation II design consists of four strong master regulators (or hubs), we randomly pick two of them and treat the corresponding sub-DAG as our prior knowledge about the network. So, we know a priori part of the true node ordering of the network, called order ${ }_{(\text {prior) }}$. For the rest of nodes, we once again learn the node ordering by the sparsebn method. We merge these two pieces as $\left(\widehat{\text { order }_{(s)}}, \text { order }_{(p r i o r)}\right)$ to form the node ordering of the network.

We also apply the proposed ER method, which consistently selects $K=5(100 \%)$ under each scenario. Thus, we compare the performance of our method $\operatorname{SFEM}_{K=5}$ under the three levels of node ordering knowledge, as well as the naive PC-algorithm and sparsebn method that do not input any knowledge of node ordering. From Figure 3, with no surprise, our $\operatorname{SFEM}_{K=5}$ method significantly outperforms
the PC-algorithm and the sparsebn method in all scenarios. This figure appears in color in the electronic version of this article, and any mention of color refers to that version. Interestingly, accounting for latent factors with our SFEM method in scenario (b) clearly helps boost the detection power compared to the sparsebn method that supplies the node ordering to the SFEM method. In the presence of such strong masking due to five unmeasured factors, it is certainly beneficial to use our SFEM method. Another important conclusion from this comparison is that knowing the node ordering partially can help a lot. The proposed SFEM method has the flexibility to accommodate some incomplete knowledge for improvement of detection power.

Under the same DAG setting, Section 2 of the Supporting Information provides an expanded simulation experiment II with 500 replicates. Section 3 of the Supporting Information reports the results of average computation time for the EM-CD algorithm over different $K$ values based on 50 rounds of simulations. It ranges from 3 minutes with $K=0$ to 7 minutes with $K=5$, which is reasonably fast given the size and complexity of the computational operations.

## 5 | ANALYSIS OF METABRIC GENE EXPRESSION DATA

This section demonstrates the application of the proposed SFEM method to the METABRIC data, which consists of gene expression measurements collected from a study of the genomic landscape of breast cancers (Pereira et al., 2016). In the analysis of genetic regulatory networks, we focus on 82 driver genes identified by Pereira et al. (2016), which are measured from 1222 primary tumor samples. This set of driver genes is known for their individual causal effects on breast cancer outcomes, which have been established through somatic mutation patterns that are independent of their gene expression profiles. Applying the proposed method, we hope to estimate DAGs involving these causal genes to learn about biological interactions and pathways relevant to the disease.

To obtain the node ordering required by our SFEM method, we first apply the sparsebn method to obtain an estimated ordering of 82 driver genes. We do not use the node ordering from the PC algorithm simply because it is sensitive to a predefined threshold required by the method. The SFEM method is then applied with $K$ varying from 0 to 5 . At $K=0$ (no latent factors), 211 edges are detected, some of which may be potentially masked by ubiquitous confounding in the experiment. When applying the ER method to select $K$, we get $K=2$, leading to 170 detected edges. The reduction of the detected edges seems to suggest that some of the detected edges at $K=0$ can be explained by the unmeasured confounding that is accounted for with $K=2$. Thus, the edges inferred at $K=2$ are likely more robust. The related details can be found in Section 5 of the Supporting Information.

To enhance the stability of the analysis results, we generated 50 bootstrap samples with replacements from the gene expression data under the previously given node ordering. For each bootstrap sample, we apply the SFEM method in which $K$ is determined by the ER method, and the tuning parameter $\lambda$ is selected by the five-fold cross-validation. The final GRN is drawn following the majority voting strategy; that is, a final edge is reported only if it is detected at least $50 \%$ of the time out of 50 bootstrap samples. As shown in Table S5 of the Supporting Information, $K=$ 2 appears to be the dominant mode. In the final causal network voted by the 50 bootstrap samples, we detect 125 causal relationships among 71 genes. The detail of the regulatory network is shown in Figure S7 of the Supporting Information.

The GRN constructed by the SFEM shows some delicate structures among these breast cancer driver genes. Within the network, we find some interesting subnetworks, displayed in Figure 4. Unlike a star-shape topology where each driver gene independently causes the
disease, our result reveals a pattern of complicated interactions between the driver genes. We find that the biggest hub is gene CCND2, which regulates the other eight genes (BRCA1, JAK2, ABCC4, ERCC4, MLH1, DHRS13, LMO2, NFIB), while CCND2 is regulated by genes BIRC3 and FBN1. Another major hub is gene RUNX1, which regulates seven genes (RAD51C, CCT2, BCL10, NDRG1, PTEN, HERPUD1, EXT1), and while itself is regulated by TRIP11 and COL1A1. See Part A of Figure 4. In addition, we find that genes BRCA1 and LMO2 are two major offspring nodes, each of which is regulated by five genes. BRCA1 is a well-known breast cancer oncogene that is regulated by RAD51C, EZH2, RECQL4, NF1, and CCND2. Also, LMO2 is regulated by FH, PIK3C3, EZH2, CCND2, and FOXA1. See Part B of Figure 4. These intriguing results illustrate how pathway analysis can shed light on the regulatory mechanisms of these important disease genes.

Another real data example using cell signaling data is given in Section 4 of the Supporting Information. This is a multivariate flow cytometry dataset that has previously been analyzed by many statisticians. Our analysis using the proposed SFEM method gives similar findings to those published.

## 6 | DISCUSSION

Given prior knowledge on node ordering among variables, we proposed a class of SFEMs for an exploratory analysis of causal network construction. The proposed methodology combines the SEM and the FAM. Our SFEM method may be regarded as a general FAM that enables to effectively segregate a DAG with directed edges from an acyclic DMG, where undirected edges induced by unmeasured confounding factors are identified and removed. In this way, a simpler and more interpretable causal network is obtained. When there are no latent factors included, the proposed SFEM reduces to the classical SEM. In this case, the reconstruction of DAGs based on our proposed $L_{1}$ norm regularization method is equivalent to the $L_{1}$ norm penalized likelihood method proposed by Shojaie and Michailidis (2010).

We developed a two-step EM-CD algorithm for implementation of the proposed method that works reasonably well and can be applied to large networks, as shown in various numerical settings. However, our objective function for the whole set of parameters is nonconvex, which might yield multiple local solutions in the optimization. Since both the CD algorithm and EM algorithm solve their respective convex functions, the algorithm convergence is certain. Finding a global optimal solution for nonconvex problems is numerically very challenging, and worth fur-

A. Sub-networks for master regulator genes.

Sub-network for CCND2
Sub-network for RUNX1
![img-4.jpeg](img-4.jpeg)

# B. Sub-networks for master offspring genes. 

Sub-network for BRCA1
Sub-network for LMO2
![img-5.jpeg](img-5.jpeg)

FIG URE 4 Subnetworks for master regulator genes (CCND2 and RUNXI) and master offspring genes (BRCA1 and LMO2), respectively. This figure appears in color in the electronic version of this article, and any mention of color refers to that version
ther exploration. In addition, if information on node ordering is fully or partially unavailable, our method can incorporate an estimated ordering obtained from existing methods (eg, the score-based method). Our simulation studies have demonstrated a clear improvement of the proposed SFEM method on detection power over existing methods in the presence of masking factors. We expect that our
method can further improve detection power given better estimation of causality direction among network nodes. In addition, in the real data analysis, causal relations in GRNs are possibly nonlinear and may not be detectable using the linear SFEM proposed in this paper. Learning nonlinear causality presents another interesting extension of this research topic.

## ACKNOWLEDGMENTS

The authors are grateful to Drs. Ji Zhu and Matthias Kretzler for their constructive comments on an early draft of this paper. They like to thank the Co-Editor, an associate editor, and two referees for their valuable suggestions that significantly improved the clarity of the manuscript. Song's research is supported by an NIH grant (R01ES024732) and an NSF grant (DMS1181734).

## ORCID

PeterX.-K. Song https://orcid.org/0000-0001-7881-7182

## SUPPORTING INFORMATION

Web Appendices, Tables, and Figures referenced in Sections 4 and 5 are available with this paper at the Biometrics website on Wiley Online Library. In addition, some of the computing code used in the simulation studies is available in Section 6 of the Supporting Information.

How to cite this article: Zhou Y, Song PX-K, Wen X. Structural factor equation models for causal network construction via directed acyclic mixed graphs. Biometrics. 2021;77:573-586.
https://doi.org/10.1111/biom. 13322