# Identifiability and Consistent Estimation for Gaussian Chain Graph Models 

Ruixuan Zhao ${ }^{\dagger}$, Haoran Zhang ${ }^{\ddagger}$ and Junhui Wang*<br>${ }^{\dagger}$ School of Data Science<br>City University of Hong Kong<br>${ }^{\ddagger}$ Department of Statistics and Data Science<br>Southern University of Science and Technology<br>*Department of Statistics<br>The Chinese University of Hong Kong


#### Abstract

The chain graph model admits both undirected and directed edges in one graph, where symmetric conditional dependencies are encoded via undirected edges and asymmetric causal relations are encoded via directed edges. Though frequently encountered in practice, the chain graph model has been largely under investigated in the literature, possibly due to the lack of identifiability conditions between undirected and directed edges. In this paper, we first establish a set of novel identifiability conditions for the Gaussian chain graph model, exploiting a low rank plus sparse decomposition of the precision matrix. Further, an efficient learning algorithm is built upon the identifiability conditions to fully recover the chain graph structure. Theoretical analysis on the proposed method is conducted, assuring its asymptotic consistency in recovering the exact chain graph structure. The advantage of the proposed method is also supported by numerical experiments on both simulated examples and a real application on the Standard \& Poor 500 index data.


Keywords: Causal inference, tangent space, directed acyclic graph, Gaussian graphical model, low-rank plus sparse decomposition

# 1 Introduction 

Graphical models have attracted tremendous attention in recent years, which provide an efficient modeling framework to characterize various relationships among multiple objects of interest. They find applications in a wide spectrum of scientific domains, ranging from finance[41], information system [43], genetics [14], neuroscience [10] to public health [29].

In the literature, two types of graphical models have been extensively studied. The first type is the undirected graphical model, which encodes conditional dependences among collected nodes via undirected edges. Various learning methods have been proposed to reconstruct the undirected graph, especially under the well-known Gaussian graphical model [14, 5] where conditional dependences are encoded via the zero pattern of the precision matrix. Another well-studied graphical model is the directed acyclic graphical model, which uses directed edges to represent causal relationships among collected nodes in a directed acyclic graph (DAG). To reconstruct the DAG structure, linear Gaussian structural equation model (SEM) has been popularly considered in the literature where causal relations are encoded via the sign pattern of the coefficient matrix. Various identifiability conditions [38, 35] have been established for the linear Gaussian SEM model, leading to a number of DAG learning methods [8, 35].

Another more flexible graphical model, known as the chain graph model, can be traced back to the early work in [25, 47]. It admits both undirected and directed edges in one graph, where symmetric conditional dependencies are encoded via undirected edges and asymmetric causal relations are encoded via directed edges. Further, it is often assumed that no semi-directed cycles are allowed in the chain graph. As a direct consequence, the chain graph model can be seen as a special DAG model with multiple chain components, where each chain component is a subset of nodes connected via undirected edges, and directed edges are only allowed across different chain components. It has been frequently encountered in various application domains, ranging from genetics [17], social science [34] to computer science [7]. For instance, in pan-cancer network analysis

[17], there are three kinds of variables: DNA-level variables containing copy number and methylation, transcriptomic variables containing mRNA expression and proteomic variables. It is believed that there only exist symmetric dependencies within three kinds of variables and asymmetric casual relationships across different kinds of variables. Also, in the stock market, the relationship among different stocks can be multi-faceted, where there are symmetric competitive or cooperative relationship and asymmetric causal relationship between pairs of stocks.

The chain graph model can have different interpretations, including the Andersson-MadiganPerlman (AMP) interpretation [1], the Lauritzen-Wermuth-Frydenberg (LWF) interpretation [25, 15] and the multivariate regression (MVR) interpretation [11]. Each interpretation implies a different conditional independence relationship from the chain graph structure. Particularly, the LWF interpretation leads to a natural interpretation [11, 1], where each node affects its children and the nodes in the same chain components of these children [22]. The AMP interpretation, however, is more suitable for statistical modeling via the SEM model, which also facilitates the data generating scheme of the chain graph [1, 12]. In contrast to the LWF chain graph models, each node in AMP chain graph models only affects its children, but no other nodes in the same chain components of these children [22]. The MVR interpretation corresponds to the acyclic directed mixed graph (ADMG) with no partially directed cycle [20].

Based on different interpretations, several structure learning methods are established, including the IC like algorithm [44], the CKES algorithm [37] and the decomposition-based algorithm [30], the Markov blanket based algorithm [23], the pseudolikelihood-type algorithm [2] for LWF chain graphs, the PC like algorithm [42] and the decomposition-based algorithm [21] for MVR chain graphs, and the PC like algorithm [36] and the decomposition-based algorithm [22] for AMP chain graphs. Yet, all these methods can only estimate some Markov equivalence classes of the chain graph model, and provide no guarantee for the reconstruction of the exact chain graph structure, mostly due to the lack of identifiability conditions between undirected and directed edges. It was until very recently that [46] extends the equal noise variance assumption for DAG [38] to establish

the identifiability of the chain graph model under the AMP interpretation, which is rather difficult to verify in practice. It is also worth mentioning that if the chain components and their causal ordering are known a priori, then the chain graph model degenerates to a sequence of multivariate regression models, and various methods [12, 32, 17] have been developed to recover the graphical structure.

In this paper, we establish a set of novel identifiability conditions for the Gaussian chain graph model under AMP interpretation, exploiting a low rank plus sparse decomposition of the precision matrix. Further, an efficient learning algorithm is developed to recover the exact chain graph structure, including both undirected and directed edges. Specifically, we first reconstruct the undirected edges by estimating the precision matrix of the noise vector through a regularized likelihood optimization. Then, we identify each chain component and determine its causal ordering based on the conditional variances of its nodes. Finally, the directed edges are reconstructed via multivariate regression coupled with truncated singular value decomposition (SVD). Theoretical analysis shows that the proposed method can consistently reconstruct the exact chain graph structure, which, to the best of our knowledge, is the first asymptotic consistency result in terms of exact graph recovery for the Gaussian chain graph with AMP interpretation and linear SEM model. The advantage of the proposed method is supported by numerical experiments on both simulated examples and a real application on the Standard \& Poor 500 index data, which reveals some interesting impacts of the COVID-19 pandemic on the stock market.

The rest of the paper is organized as following. Section 2 introduces some preliminaries on the chain graph model. Section 3 proposes the identifiability conditions for linear Gaussian chain graph model, and develops an efficient learning algorithm to reconstruct the exact chain graph structure. The asymptotic consistency of the proposed method is established in Section 4. Numerical experiments of the proposed method on both simulated and real examples are included in Section 5. Section 6 concludes the paper, and technical proofs are provided in the Appendix. Auxiliary lemmas and further computational details are deferred to a separate Supplementary File.

Before moving to Section 2, we define some notations. For an integer $m$, denote $[m]=$ $\{1, \ldots, m\}$. For a real value $x$, denote $\lceil x\rceil$ as the largest integer less than or equal to $x$. For two nonnegative sequences $a_{n}$ and $b_{n}, a_{n} \lesssim b_{n}$ means there exists a constant $c>0$ such that $a_{n} \leq c b_{n}$ when $n$ is sufficiently large. Further, $a_{n} \lesssim_{P} b_{n}$ means there exists a constant $c>0$ such that $\operatorname{Pr}\left(a_{n} \leq c b_{n}\right) \rightarrow 1$ as $n$ grows to infinity. For a vector $\mathbf{x}$, the sub-vector corresponding to an index subset $S$ is denoted as $\mathbf{x}_{S}=\left(\mathbf{x}_{i}\right)_{i \in S}$. For a matrix $\mathbf{A}=\left(a_{i j}\right)_{p \times p}$, the sub-matrix corresponding to rows in $S_{1}$ and columns in $S_{2}$ is denoted as $\mathbf{A}_{S_{1}, S_{2}}=\left(a_{i j}\right)_{i \in S_{1}, j \in S_{2}}$, and let $\mathbf{A}_{S_{1}, S_{2}}^{-1}$ denote the corresponding sub-matrix of $\mathbf{A}^{-1}$. Also, let $\|\mathbf{A}\|_{1, \text { off }}=\sum_{i \neq j}\left|a_{i j}\right|,\|\mathbf{A}\|_{\max }=\max _{i j}\left|a_{i j}\right|,\|\mathbf{A}\|_{2}$ denote the spectrum norm, $\|\mathbf{A}\|_{*}$ denote the nuclear norm and $v(\mathbf{A}) \in \mathbb{R}^{p^{2}}$ denote the vectorization of $\mathbf{A}$.

# 2 Chain graph model 

Suppose the joint distribution of $\mathbf{x}=\left(x_{1}, \ldots, x_{p}\right)^{\top}$ can be depicted as a chain graph $\mathcal{G}=(\mathcal{N}, \mathcal{E})$, where $\mathcal{N}=\{1, \ldots, p\}$ represents the node set and $\mathcal{E} \subset \mathcal{N} \times \mathcal{N}$ represents the edge set containing all undirected and directed edges. To differentiate, we denote $(i-j)$ for an undirected edge between nodes $i$ and $j,(i \rightarrow j)$ for a directed edge pointing from node $i$ to node $j$, and suppose that at most one edge is allowed between two nodes. Then, there exists a positive integer $m$ such that $\mathcal{N}$ can be uniquely partitioned into $m$ disjoint chain components $\mathcal{N}=\bigcup_{k=1}^{m} \tau_{k}$, where each $\tau_{k}$ is a connected component of nodes via undirected edges. Suppose that only undirected edges exist within each chain component, and directed edges are only allowed across different chain components [31, 12]. Further suppose that there exists a permutation $\boldsymbol{\pi}=\left(\pi_{1}, \ldots, \pi_{m}\right)$ such that for $i \in \tau_{\pi_{k}}$ and $j \in \tau_{\pi_{l}}$, if $(i \rightarrow j) \in \mathcal{E}$, then $k<l$. This excludes the existence of semi-directed cycle in $\mathcal{G}$ [31]. We call such permutation $\boldsymbol{\pi}$ as the causal ordering of the chain components, and directed edges could only point from nodes in higher-order $\tau_{k}$ to nodes in lower-order one.

Let $\operatorname{pa}(i)=\{j \in \mathcal{N}:(j \rightarrow i) \in \mathcal{E}\}, \operatorname{ch}(i)=\{j \in \mathcal{N}:(i \rightarrow j) \in \mathcal{E}\}$ and $\operatorname{ne}(i)=\{j \in$

$\mathcal{N}:(j-i) \in \mathcal{E}\}$ denote the parents, children and neighbors of node $i$, respectively. Further, let $\mathrm{pa}\left(\tau_{k}\right)=\bigcup_{i \in \tau_{k}} \mathrm{pa}(i)$ be the parent set of chain component $\tau_{k}$. Suppose the joint distribution of $\mathbf{x}$ satisfies the AMP Markov property [1, 26] with respect to $\mathcal{G}$, and follows the linear structural equation model (SEM),

$$
\mathbf{x}=\mathbf{B} \mathbf{x}+\boldsymbol{\epsilon}
$$

where $\mathbf{B}=\left(\beta_{i j}\right)_{p \times p}$ is the coefficient matrix, $\boldsymbol{\epsilon}=\left(\epsilon_{1}, \ldots, \epsilon_{p}\right)^{\top} \sim N\left(\mathbf{0}, \boldsymbol{\Omega}^{-1}\right)$, and $\boldsymbol{\Omega}=\left(\omega_{i j}\right)_{p \times p}$ is the precision matrix of $\boldsymbol{\epsilon}$. Further, suppose that $\beta_{i j} \neq 0$ if and only if $j \in \mathrm{pa}(i)$, and $\omega_{i j} \neq 0$ if and only if $j \in \operatorname{ne}(i)$. Therefore, the undirected and directed edges in $\mathcal{G}$ can be directly implied by the zero patterns in $\Omega$ and $\mathbf{B}$, respectively. The joint density of $\mathbf{x}$ can then be factorized as

$$
P(\mathbf{x})=\prod_{k=1}^{m} P\left(\mathbf{x}_{\tau_{k}} \mid \mathbf{x}_{\mathrm{pa}\left(\tau_{k}\right)}\right)
$$

where $\mathbf{x}_{\tau_{k}} \mid \mathbf{x}_{\mathrm{pa}\left(\tau_{k}\right)} \sim N\left(\mathbf{B}_{\tau_{k}, \mathrm{pa}\left(\tau_{k}\right)} \mathbf{x}_{\mathrm{pa}\left(\tau_{k}\right)}, \boldsymbol{\Omega}_{\tau_{k}, \tau_{k}}^{-1}\right)$ for $k \in[m]$, and $\boldsymbol{\Omega}_{\tau_{k}, \tau_{k}}$ is not necessarily a diagonal matrix. This is a key component of the chain graph model to allow undirected edges within each $\tau_{k}$, and thus differs from most existing SEM models with diagonal $\Omega$ in the literature [39, 38, 35, 8].

It is also interesting to compare the AMP, LWF and MVR interpretations of $\mathcal{G}$ with the SEM model in (1). Let $\Theta^{k}$ be the precision matrix corresponding to $\tau_{k} \cup \mathrm{pa}\left(\tau_{k}\right)$, then different interpretations lead to different implications on $\Omega$ and $\mathbf{B}$. Particularly,

- AMP interpretation: $(j \rightarrow i) \notin \mathcal{E}$ for $i \in \tau_{k}$ and $j \in \mathrm{pa}\left(\tau_{k}\right) \Longrightarrow \mathbf{B}_{i j}=0 ;(j-i) \notin \mathcal{E}$ for $i, j \in \tau_{k} \Longrightarrow \boldsymbol{\Omega}_{i j}=0$.
- LWF interpretation: $(j \rightarrow i) \notin \mathcal{E}$ for $i \in \tau_{k}$ and $j \in \mathrm{pa}\left(\tau_{k}\right) \Longrightarrow\left[\Theta_{\tau_{k}, \mathrm{pa}\left(\tau_{k}\right)}^{k}\right]_{i j}=0$; $(j-i) \notin \mathcal{E}$ for $i, j \in \tau_{k} \Longrightarrow \boldsymbol{\Omega}_{i j}=0$.
- MVR interpretation: $(j \rightarrow i) \notin \mathcal{E}$ for $i \in \tau_{k}$ and $j \in \mathrm{pa}\left(\tau_{k}\right) \Longrightarrow \mathbf{B}_{i j}=0 ;(j \leftrightarrow i) \notin \mathcal{E}$ for $i, j \in \tau_{k} \Longrightarrow \boldsymbol{\Omega}_{i j}^{-1}=0$.

It is clear that AMP interpretation matches well with the linear SEM model so that the graph structure in $\mathcal{G}$ can be fully captured by the supports of $\Omega$ and B, which also greatly facilitates the data generating scheme of the chain graph [1, 12]. Yet, the directed edges in the LWF chain graph corresponds to more involved parameter $\Theta_{\tau_{k}, \mathrm{pa}\left(\tau_{k}\right)}^{k}=-\Omega_{\tau_{k}, \tau_{k}} \mathbf{B}_{\tau_{k}, \mathrm{pa}\left(\tau_{k}\right)}$, whereas the undirected edges in the MVR chain graph corresponds to the noise covariance matrix $\Omega^{-1}$. Here $\left[\Theta_{\tau_{k}, \mathrm{pa}\left(\tau_{k}\right)}^{k}\right]_{i j}$ represents the element in matrix $\Theta_{\tau_{k}, \mathrm{pa}\left(\tau_{k}\right)}^{k}$ corresponding to nodes $i$ and $j$.

Furthermore, to assure the acyclicity among chain components in $\mathcal{G}$, we say $(\Omega, \mathbf{B})$ is CGfeasible if there exists a permutation matrix $\mathbf{P}$ such that both $\mathbf{P} \Omega \mathbf{P}^{\top}$ and $\mathbf{P B P}^{\top}$ share the same block structure, where $\mathbf{P} \Omega \mathbf{P}^{\top}$ is a block diagonal matrix and $\mathbf{P B P}^{\top}$ is a block lower triangular matrix with zero diagonal blocks. Figure 1 shows a toy chain graph, as well as the supports of the original and permuted $(\Omega, \mathbf{B})$. Let $\Theta$ denote the precision matrix for $\mathbf{x}$, then it follows from (1) that

$$
\Theta=\left(\mathbf{I}_{p}-\mathbf{B}\right)^{\top} \Omega\left(\mathbf{I}_{p}-\mathbf{B}\right)=: \Omega+\mathbf{L}
$$

where $\mathbf{L}=\mathbf{B}^{\top} \Omega \mathbf{B}-\mathbf{B}^{\top} \Omega-\Omega \mathbf{B}$.

# 3 Proposed method 

### 3.1 Identifiability of $\mathcal{G}$

A key challenge in the chain graph model is the identifiability of the graph structure $\mathcal{G}$, due to the fact that $\Omega$ and $\mathbf{B}$ are intertwined in the SEM model in (1). To proceed, we assume that $\Omega$ is sparse with $\|\Omega\|_{0}=S$ and $\mathbf{L}$ is a low-rank matrix with $\operatorname{rank}(\mathbf{L})=K$. The sparseness of $\Omega$ implies the sparseness of undirected edges in $\mathcal{G}$, which has been well adopted in the literature of Gaussian graphical models [33, 14, 5]. The low-rank of $\mathbf{L}$ inherits from that of B [13], which essentially assumes the presence of hub nodes in $\mathcal{G}$ or nodes with multiple children or parents.

![img-0.jpeg](img-0.jpeg)

Figure 1: The left panel displays a toy chain graph with colors indicating different chain components, and the right panel displays the supports of the original $(\Omega, \mathbf{B})$ in the first column and the permuted $(\Omega, \mathbf{B})$ in the second column.

Let $\mathbf{L}=\mathbf{U}_{1} \mathbf{D}_{1} \mathbf{U}_{1}^{\top}$ be the eigen decomposition of $\mathbf{L}$, where $\mathbf{U}_{1}^{\top} \mathbf{U}_{1}=\mathbf{I}_{K}$ and $\mathbf{D}_{1}$ is a $K \times K$ diagonal matrix. We define two linear subspaces,

$$
\begin{aligned}
& \mathcal{S}(\Omega)=\left\{\mathbf{S} \in \mathbb{R}^{p \times p}: \mathbf{S}^{\top}=\mathbf{S}, \text { and } s_{i j}=0 \text { if } \omega_{i j}=0\right\} \\
& \mathcal{T}(\mathbf{L})=\left\{\mathbf{U}_{1} \mathbf{Y}+\mathbf{Y}^{\top} \mathbf{U}_{1}^{\top}: \mathbf{Y} \in \mathbb{R}^{K \times p}\right\}
\end{aligned}
$$

where $\mathcal{S}(\Omega)$ is the tangent space, at point $\Omega$, of the manifold containing symmetric matrices with at most $S$ non-zero entries, and $\mathcal{T}(\mathbf{L})$ is the tangent space, at point $\mathbf{L}$, of the manifold containing symmetric matrices with rank at most $K$ [6].

Assumption 1. $\mathcal{S}(\boldsymbol{\Omega})$ and $\mathcal{T}(\mathbf{L})$ intersect at the origin only; that is, $\mathcal{S}(\boldsymbol{\Omega}) \cap \mathcal{T}(\mathbf{L})=\left\{\mathbf{0}_{p \times p}\right\}$.

Assumption 1 is the same as the transversality condition in [6], which assures the identifiability of $(\Omega, \mathbf{L})$ in the sense that $\Theta$ can be uniquely decomposed as the sum of a matrix in $\mathcal{S}(\Omega)$ and the other one in $\mathcal{T}(\mathbf{L})$. It essentially holds if $\Omega$ is sparse but not low-rank and $\mathbf{L}$ is low-rank but not sparse. Note that $\Omega$ is the precision matrix and thus full-rank, yet its sparsity corresponds to the

sparseness of undirected edges in $\mathcal{G}$. The low-rank of $\mathbf{L}$ inherits from that of $\mathbf{B}$, which corresponds to the presence of hub nodes in $\mathcal{G}$ [13]. Further, we have

$$
L_{j k}=\sum_{l=1}^{p} \sum_{i=1}^{p} \beta_{i j} \omega_{i l} \beta_{l k}-\sum_{i=1}^{p} \beta_{i j} \omega_{i k}-\sum_{i=1}^{p} \omega_{j i} \beta_{i k}
$$

where the first term corresponds to the path $j \rightarrow i-l \leftarrow k$ if $l \neq i$ or the path $j \rightarrow i \leftarrow k$ if $l=i$, the second term corresponds to the path $j \rightarrow i-k$ if $i \neq k$ and $j \rightarrow k$ if $i=k$, and the third term corresponds to the path $j-i \leftarrow k$ if $i \neq j$ and $j \leftarrow k$ if $i=j$. Therefore, $L_{j k} \neq 0$ if any one of these paths exists between nodes $j$ and $k$, and thus it is reasonable to assume $\mathbf{L}$ to be non-sparse.

Assumption 2. The $K$ eigenvalues of $\mathbf{L}$ are distinct.

Assumption 2 is necessary to identify the eigen space of the low-rank matrix $\mathbf{L}$, which has been commonly assumed in the literature of matrix perturbation [50]. Let $\mathcal{Q}$ be the parameter space of CG-feasible $(\boldsymbol{\Omega}, \mathbf{B})$, where $\boldsymbol{\Omega} \succ 0, \boldsymbol{\Omega}+\mathbf{L} \succ 0,\|\boldsymbol{\Omega}\|_{0} \leq S, \operatorname{rank}(\mathbf{L}) \leq K$, and Assumptions 1 and 2 are met. Let $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right)$ denote the true parameters of the linear SEM model (1) satisfying $\left\|\boldsymbol{\Omega}^{*}\right\|_{0}=S$ and $\operatorname{rank}\left(\mathbf{L}^{*}\right)=K$

Theorem 1. Suppose $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right) \in \mathcal{Q}$. Then, there exists a small $\epsilon>0$ such that for any $(\boldsymbol{\Omega}, \mathbf{B}) \in \mathcal{Q}$ satisfying $\left\|\boldsymbol{\Omega}-\boldsymbol{\Omega}^{*}\right\|_{\max }<\epsilon$ and $\left\|\mathbf{B}-\mathbf{B}^{*}\right\|_{\max }<\epsilon$, if

$$
\left(\mathbf{I}_{p}-\mathbf{B}\right)^{\top} \boldsymbol{\Omega}\left(\mathbf{I}_{p}-\mathbf{B}\right)=\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)^{\top} \boldsymbol{\Omega}^{*}\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)
$$

it holds true that $(\boldsymbol{\Omega}, \mathbf{B})=\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right)$.
Theorem 1 establishes the local identifiability of $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right)$ in (1), which further implies the local identifiability of the chain graph $\mathcal{G}$. It essentially states that $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right) \in \mathcal{Q}$ can be uniquely determined, within its neighborhood in $\mathcal{Q}$, by the precision matrix $\boldsymbol{\Theta}^{*}=\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)^{\top} \boldsymbol{\Omega}^{*}\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)$, which can be consistently estimated from the observed sample.

Remark 1 (Identifiability for DAG). When $\Omega$ is indeed a diagonal matrix, each chain component contains exactly one node and thus $\mathcal{G}$ reduces to a DAG. By Theorem 1, it is identifiable as long as the eigenvalues of $\mathbf{L}^{*}$ are distinct and $\mathbf{e}_{j} \notin \operatorname{span}\left(\mathbf{U}_{1}^{*}\right)$ for any $j \in[p]$, where $\mathbf{U}_{1}^{*} \in \mathbb{R}^{p \times K}$ contains eigenvectors of $\mathbf{L}^{*}$ and $\left\{\mathbf{e}_{j}\right\}_{j=1}^{p}$ are the standard basis of $\mathbb{R}^{p}$. It provides an alternative identifiability condition for DAG, in contrast to the popularly-employed equal noise variance assumption [38]. These two assumptions are incomparable though. Particularly, in our identifiability condition for DAG, $\Omega$ is a diagonal matrix but the diagonal elements can vary. On the other hand, the equal noise variance assumption also does not imply our identifiability condition. For example, let $p=3, \boldsymbol{\Omega}=\mathbf{I}_{3}$ and $\mathbf{B}=\left(b_{i j}\right)_{3 \times 3}$ with $b_{21}=1$ and other entries being 0 , then

$$
\mathbf{L}=\left(\begin{array}{ccc}
1 & -1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & 0
\end{array}\right)
$$

where it is easy to verify that $\mathbf{e}_{1}, \mathbf{e}_{2} \in \operatorname{span}\left(\mathbf{U}_{1}\right)$.

# 3.2 Learning algorithm 

We now develop a learning algorithm to estimate $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right)$ and reconstruct the chain graph $\mathcal{G}$. Suppose we observe independent copies $\mathbf{x}_{1}, \ldots, \mathbf{x}_{n} \in \mathbb{R}^{p}$ and denote $\mathbf{X}=\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)^{\top} \in \mathbb{R}^{n \times p}$. We first estimate $\Omega^{*}$ via the following regularized likelihood,

$$
\begin{aligned}
(\widehat{\Omega}, \widehat{\mathbf{L}}) & =\underset{\boldsymbol{\Omega}, \mathbf{L}}{\operatorname{argmin}}\left\{-l(\boldsymbol{\Omega}+\mathbf{L})+\lambda_{n}\left(\|\boldsymbol{\Omega}\|_{1, \text { off }}+\gamma\|\mathbf{L}\|_{*}\right)\right\} \\
& \text { subject to } \boldsymbol{\Omega} \succ 0 \text { and } \boldsymbol{\Omega}+\mathbf{L} \succ 0
\end{aligned}
$$

where $l(\boldsymbol{\Theta})=-\operatorname{tr}(\boldsymbol{\Theta} \widehat{\boldsymbol{\Sigma}})+\log \{\operatorname{det}(\boldsymbol{\Theta})\}$ is the Gaussian log-likelihood with $\widehat{\boldsymbol{\Sigma}}=\frac{1}{n} \mathbf{X}^{\top} \mathbf{X}$, and $\lambda_{n}$ and $\gamma$ are tuning parameters. Here $\|\boldsymbol{\Omega}\|_{1, \text { off }}=\sum_{i \neq j}\left|\omega_{i j}\right|$ induces sparsity in $\boldsymbol{\Omega},\|\mathbf{L}\|_{*}$ induces

low-rank of $\mathbf{L}$, and the constraints are due to the fact that both $\boldsymbol{\Omega}$ and $\boldsymbol{\Theta}=\boldsymbol{\Omega}+\mathbf{L}$ are precision matrices. Note that the optimization task in (6) is convex, and can be efficiently solved via the alternative direction method of multipliers (ADMM; [3]). More computational details are deferred to the Supplementary Files.

Once $\widehat{\Omega}$ is obtained, we connect nodes $i$ and $j$ with undirected edges if $\widehat{\omega}_{i j} \neq 0$, which leads to multiple estimated chain components, denoted as $\widehat{\tau}_{1}, \ldots, \widehat{\tau}_{\widehat{m}}$. We can further determine their causal ordering by comparing the estimated conditional variance of node $i \in \widehat{\tau}_{k}$ with $\widehat{\Omega}_{i i}^{-1}$. Particularly, the conditional variance of node $i$ can be decomposed into two parts, with one corresponding to its parent nodes and the other from $\Omega_{i i}^{-1}$. Therefore, if all the parent nodes of node $i$ are given, the remaining variance should all come from $\Omega_{i i}^{-1}$, otherwise the remaining variance should be larger than $\Omega_{i i}^{-1}$. This observation shares the same spirit as [8] in determining causal ordering, without requiring equal noise variances though. More specifically, for each $\widehat{\tau}_{k}$ and any $\mathcal{C} \subset[p] \backslash \widehat{\tau}_{k}$, we define

$$
\widehat{\mathcal{D}}\left(\widehat{\tau}_{k}, \mathcal{C}\right)=\max _{i \in \widehat{\tau}_{k}}\left\{\widehat{\Sigma}_{i i}-\widehat{\Sigma}_{i \mathcal{C}} \widehat{\Sigma}_{\mathcal{C} \mathcal{C}}^{-1} \widehat{\Sigma}_{\mathcal{C} i}-\widehat{\Omega}_{i i}^{-1}\right\}
$$

where $\widehat{\Sigma}_{i i}-\widehat{\Sigma}_{i \mathcal{C}} \widehat{\Sigma}_{\mathcal{C} \mathcal{C}}^{-1} \widehat{\Sigma}_{\mathcal{C} i}$ is the estimated conditional variance for node $i \in \widehat{\tau}_{k}$ given nodes in $\mathcal{C}$, and $\widehat{\Omega}_{i i}^{-1}$ is the estimated variance for node $i \in \widehat{\tau}_{k}$ given its parent chain components. It is thus clear that $\widehat{\mathcal{D}}\left(\widehat{\tau}_{k}, \mathcal{C}\right)$ shall be close to 0 if $\mathcal{C}$ consists of all upper chain components of $\widehat{\tau}_{k}$. We start with $\widehat{\mathcal{D}}\left(\widehat{\tau}_{k}, \emptyset\right)=\max _{i \in \widehat{\tau}_{k}}\left\{\widehat{\Sigma}_{i i}-\widehat{\Omega}_{i i}^{-1}\right\}$ for each chain component $\widehat{\tau}_{k}$, and select the first chain component by $\widehat{\pi}_{1}=\operatorname{argmin}_{l \in[\widehat{m}]} \widehat{\mathcal{D}}\left(\widehat{\tau}_{l}, \emptyset\right)$. Suppose the first $s$ chain components $\widehat{\tau}_{\widehat{\pi}_{1}}, \ldots, \widehat{\tau}_{\widehat{\pi}_{s}}$ have been selected, let $\widehat{\mathcal{C}}_{s}=\cup_{k=1}^{s} \widehat{\tau}_{\widehat{\pi}_{k}}$ and $\widehat{\pi}_{s+1}=\operatorname{argmin}_{l \in[\widehat{m}] \cup_{k=1}^{s} \widehat{\pi}_{k}} \widehat{\mathcal{D}}\left(\widehat{\tau}_{l}, \widehat{\mathcal{C}}_{s}\right)$. We repeat this procedure until the causal orderings of all $\widehat{\tau}_{k}$ 's are determined, which are denoted as $\widehat{\boldsymbol{\pi}}=\left(\widehat{\pi}_{1}, \ldots, \widehat{\pi}_{\widehat{m}}\right)$.

Finally, we estimate $\mathbf{B}^{*}$ based on the estimated causal ordering $\widehat{\boldsymbol{\pi}}$ of the chain components. Particularly, $\widehat{\mathcal{C}}_{k-1}$ consists of all the chain components in front of $\widehat{\pi}_{k}$, and then the directed edges, if present, can only point from nodes in $\widehat{\mathcal{C}}_{k-1}$ to nodes in $\widehat{\pi}_{k}$. Thus, we first give an intermediate estimate $\widehat{\mathbf{B}}^{\text {reg }}$, whose submatrix $\widehat{\mathbf{B}}_{\widehat{\tau}_{\widehat{\pi}_{k}}, \widehat{\mathcal{C}}_{k-1}}^{\text {reg }}$ is obtained via a multivariate regression of $\mathbf{x}_{\widehat{\tau}_{\widehat{\pi}_{k}}}$ on

$\mathbf{x}_{\mathcal{C}_{k-1}}$. Given $\widehat{\mathbf{B}}^{\text {reg }}$, we conduct singular value decomposition (SVD) as $\widehat{\mathbf{B}}^{\text {reg }}=\widehat{\mathbf{U}}^{\text {reg }} \widehat{\mathbf{D}}^{\text {reg }}\left(\widehat{\mathbf{V}}^{\text {reg }}\right)^{\top}$ with $\widehat{\mathbf{D}}^{\text {reg }}=\operatorname{diag}\left(\widehat{\sigma}_{1}^{\text {reg }}, \ldots, \widehat{\sigma}_{p}^{\text {reg }}\right)$, and then truncate the small singular values to obtain $\widehat{\mathbf{B}}^{\text {svd }}=$ $\widehat{\mathbf{U}}^{\text {reg }} \widehat{\mathbf{D}}^{\text {svd }}\left(\widehat{\mathbf{V}}^{\text {reg }}\right)^{\top}$, where $\widehat{\mathbf{D}}^{\text {svd }}=\operatorname{diag}\left(\widehat{\sigma}_{1}^{\text {svd }}, \ldots, \widehat{\sigma}_{p}^{\text {svd }}\right)$ with $\widehat{\sigma}_{j}^{\text {svd }}=0$ if $\widehat{\sigma}_{j}^{\text {reg }} \leq \kappa_{n}$ and $\widehat{\sigma}_{j}^{\text {svd }}=\widehat{\sigma}_{j}^{\text {reg }}$ if $\widehat{\sigma}_{j}^{\text {reg }}>\kappa_{n}$, for some pre-specified $\kappa_{n}>0$. The final estimate $\widehat{\mathbf{B}}=\left(\widehat{\beta}_{i j}\right)_{p \times p}$ is obtained by truncating the diagonal and upper triangular blocks to 0 , and conducting a hard thresholding to the lower triangular blocks with some pre-specified $\nu_{n}>0$, where $\widehat{\beta}_{i j}=0$ if $\left|\widehat{\beta}_{i j}^{\text {svd }}\right| \leq \nu_{n}$ and $\widehat{\beta}_{i j}=\widehat{\beta}_{i j}^{\text {svd }}$ if $\left|\widehat{\beta}_{i j}^{\text {svd }}\right|>\nu_{n}$. The nonzero elements of $\widehat{\mathbf{B}}$ then lead to the estimated directed edges.

The proposed learning algorithm is computational efficient, whose computational complexity is roughly of polynomial order of $p$. Specifically, in estimating $\Omega^{*}$, the optimization (6) is convex and can be solved in polynomial time. The causal ordering of chain components is recovered via iteratively computing $\widehat{\mathcal{D}}\left(\widehat{\tau}_{k}, \mathcal{C}\right)$ and searching for the chain component with minimal $\widehat{\mathcal{D}}\left(\widehat{\tau}_{k}, \mathcal{C}\right)$. It is clear that the above procedure involves computing conditional variances, and finding maximum and minimum, whose complexity is of polynomial order in $p$. Finally, the complexity of multivariate regressions coupled with truncated SVD to reconstruct the directed edges is also of polynomial order in $p$.

# 4 Asymptotic theory 

This section quantifies the asymptotic behavior of $(\widehat{\Omega}, \widehat{\mathbf{B}})$, and establishes its consistency for reconstructing the chain graph $\mathcal{G}^{*}=\left(\mathcal{N}, \mathcal{E}^{*}\right)$. Let $\boldsymbol{\Theta}^{*}=\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)^{\top} \boldsymbol{\Omega}^{*}\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)$, and the Fisher information matrix takes the form

$$
\mathcal{I}^{*}=-\mathbb{E}\left[\frac{\partial^{2} l\left(\boldsymbol{\Theta}^{*}\right)}{\partial \boldsymbol{\Theta}^{2}}\right]=\left(\boldsymbol{\Theta}^{*}\right)^{-1} \otimes\left(\boldsymbol{\Theta}^{*}\right)^{-1}
$$

where $\otimes$ denotes the Kronecker product. For a linear subspace $\mathcal{M}$, let $\mathcal{P}_{\mathcal{M}}$ denote the projection onto $\mathcal{M}$, and $\mathcal{M}^{\perp}$ denote the orthogonal complement of $\mathcal{M}$. We further define two linear operators

$F: \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times \mathcal{T}\left(\mathbf{L}^{*}\right) \rightarrow \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times \mathcal{T}\left(\mathbf{L}^{*}\right)$ and $F^{\perp}: \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times \mathcal{T}\left(\mathbf{L}^{*}\right) \rightarrow \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)^{\perp} \times \mathcal{T}\left(\mathbf{L}^{*}\right)^{\perp}$ such that

$$
\begin{aligned}
F\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right) & =\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)}\left(\mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)\right), \mathcal{P}_{\mathcal{T}\left(\mathbf{L}^{*}\right)}\left(\mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)\right)\right) \\
F^{\perp}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right) & =\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)^{\perp}}\left(\mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)\right), \mathcal{P}_{\mathcal{T}\left(\mathbf{L}^{*}\right)^{\perp}}\left(\mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)\right)\right)
\end{aligned}
$$

According to Assumption 1 and Lemma 1 in the Supplementary Files, $F$ is invertible and thus $F^{-1}$ is well defined.

Let $g_{\gamma}(\boldsymbol{\Omega}, \mathbf{L})=\max \left\{\|\boldsymbol{\Omega}\|_{\max },\|\mathbf{L}\|_{2} / \gamma\right\}$, where $\gamma>0$ is the same as that in (6). Let $\mathbf{L}^{*}=$ $\mathbf{U}_{1}^{*} \mathbf{D}_{1}^{*}\left(\mathbf{U}_{1}^{*}\right)^{\top}$ be the eigen decomposition of $\mathbf{L}^{*}$.

Assumption 3. $g_{\gamma}\left(F^{\perp} F^{-1}\left(\operatorname{sign}\left(\boldsymbol{\Omega}^{*}\right), \gamma \mathbf{U}_{1}^{*} \operatorname{sign}\left(\mathbf{D}_{1}^{*}\right)\left(\mathbf{U}_{1}^{*}\right)^{\top}\right)\right)<1$.
Assumption 3 is essential for establishing the selection and rank consistency of $(\widehat{\boldsymbol{\Omega}}, \widehat{\mathbf{L}})$ through penalties in (6). For example, in a special case when $\Theta^{*}=\mathbf{I}_{p}$ and $\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \perp \mathcal{T}\left(\mathbf{L}^{*}\right)$, Assumption 3 simplifies to $\max \left\{\gamma\left\|\mathbf{U}_{1}^{*} \operatorname{sign}\left(\mathbf{D}_{1}^{*}\right)\left(\mathbf{U}_{1}^{*}\right)^{\top}\right\|_{\max },\left\|\operatorname{sign}\left(\boldsymbol{\Omega}^{*}\right)\right\|_{2} / \gamma\right\}<1$, implying that $\mathbf{U}_{1}^{*}$ is not sparse and $\operatorname{sign}\left(\boldsymbol{\Omega}^{*}\right)$ is not a low-rank matrix. Similar technical conditions have also been assumed in the literature $[6,9]$.

Theorem 2. Suppose $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right) \in \mathcal{Q}$ and Assumption 3 holds. Let $\lambda_{n}=n^{-1 / 2+\eta}$ with a sufficiently small positive constant $\eta$. Then, with probability approaching 1, (6) has a unique solution $(\widehat{\boldsymbol{\Omega}}, \widehat{\mathbf{L}})$. Furthermore, we have

$$
\begin{array}{ll}
\left\|\widehat{\boldsymbol{\Omega}}-\boldsymbol{\Omega}^{*}\right\|_{\max } \lesssim_{P} n^{-\frac{1}{2}+2 \eta}, & \operatorname{Pr}\left(\operatorname{sign}(\widehat{\boldsymbol{\Omega}})=\operatorname{sign}\left(\boldsymbol{\Omega}^{*}\right)\right) \rightarrow 1 \\
\left\|\widehat{\mathbf{L}}-\mathbf{L}^{*}\right\|_{\max } \lesssim_{P} n^{-\frac{1}{2}+2 \eta}, & \operatorname{Pr}\left(\operatorname{rank}(\widehat{\mathbf{L}})=\operatorname{rank}\left(\mathbf{L}^{*}\right)\right) \rightarrow 1
\end{array}
$$

Theorem 2 shows that $\widehat{\boldsymbol{\Omega}}$ has both estimation and sign consistency, which implies that the undirected edges in $\mathcal{G}^{*}$ could be exactly reconstructed with high probability. It can also be shown that $\widehat{\mathbf{B}}$ attains both estimation and selection consistency, implying the exact recovery of the directed edges in $\mathcal{G}^{*}$. Furthermore, given $(\widehat{\boldsymbol{\Omega}}, \widehat{\mathbf{B}})$, we reconstruct the chain graph as $\widehat{\mathcal{G}}=(\mathcal{N}, \widehat{\mathcal{E}})$, where

$(i \rightarrow j) \in \widehat{\mathcal{E}}$ if and only if $\widehat{\beta}_{j i} \neq 0$, and $(i-j) \in \widehat{\mathcal{E}}$ if and only if $\widehat{\omega}_{i j} \neq 0$. The following Theorem 3 establishes the consistency of $\widehat{\mathcal{G}}$.

Theorem 3. Suppose all the conditions in Theorem 2 are satisfied, and we set $\kappa_{n}=n^{-1 / 2+\eta}$ and $\nu_{n}=n^{-1 / 2+2 \eta}$ with a sufficiently small positive constant $\eta$. Then, we have

$$
\left\|\widehat{\mathbf{B}}-\mathbf{B}^{*}\right\|_{\max } \lesssim_{P} n^{-\frac{1}{2}+\eta}, \quad \operatorname{Pr}\left(\operatorname{sign}(\widehat{\mathbf{B}})=\operatorname{sign}\left(\mathbf{B}^{*}\right)\right) \rightarrow 1
$$

Furthermore, it also holds true that

$$
\operatorname{Pr}\left(\widehat{\mathcal{G}}=\mathcal{G}^{*}\right) \rightarrow 1 \text { as } n \rightarrow \infty
$$

Theorem 3 shows that $\widehat{\mathbf{B}}$ achieves both estimation and sign consistency, which further leads to exact recovery of $\mathcal{G}^{*}$ with high probability. This is in sharp contrast to the existing methods only recovering some Markov equivalent class of the chain graph [44, 37, 30, 42, 21, 36, 22].

# 5 Numerical experiments 

### 5.1 Simulated examples

We examine the numerical performance of the proposed method ${ }^{1}$ and compare it against existing structural learning methods for chain graph, including the decomposition-based algorithm (LCD, [22]) and PC like algorithm (PC-like, [36, 22]), as well as the PC algorithm for DAG (PC, [24]). The implementations of LCD and PC-like are available at https://github.com/ma javid/ AMPCGs2019. We implement PC algorithm through R packages pcalg and then convert the resulted partial DAG to DAG by pdag2dag. The significance level of all tests in LCD, PC-like and PC is set as $\alpha=0.05$. For the proposed method, we set $\eta=1 / 8, \gamma=2$ and $\lambda_{n}, \kappa_{n}$ and $\nu_{n}$

[^0]
[^0]:    ${ }^{1}$ An R package "LearnCG" has been developed and can be downloaded from https://github.com/RuixuanZhao/LearnCG.

following the results in Theorems 2 and 3. Note that the numerical performance of the proposed method can be further refined if these tuning parameters are properly tuned via some data-adaptive scheme, at the cost of increased computational expense.

We evaluate the numerical performances of all four methods in terms of the estimation accuracy of undirected edges, directed edges and the overall chain graph. Specifically, we report recall, precision and Matthews correlation coefficient (MCC) as evaluation metrics for the estimated undirected edges and directed edges, respectively. Furthermore, we employ Structural Hamming Distance (SHD) [45, 22] to evaluate the estimated chain graph, which is the number of edge insertions, deletions or flips to change the estimated chain graph to the true one. Note that large values of recall, precision and MCC and small values of SHD indicate good estimation performance.

Example 1. We consider a classic two-layer Gaussian graphical model [27, 32] with two layers $\mathcal{A}_{1}=\{1, \ldots,\lceil 0.1 p\rceil\}$ and $\mathcal{A}_{2}=\{\lceil 0.1 p\rceil+1, \ldots, p\}$, whose structure is illustrated in Figure 2(a). Within each layer, we randomly connect each pair of nodes by an undirected edge with probability 0.02 , and note that one layer may contain multiple chain components. Then, we generate the directed edges from nodes in $\mathcal{A}_{1}$ to nodes in $\mathcal{A}_{2}$ with probability 0.8 . Furthermore, the non-zero values of $\omega_{i j}$ and $\beta_{i j}$ are uniformly generated from $[-1.5,-0.5] \cup[0.5,1.5]$. To guarantee the positive definiteness of $\Omega$, each diagonal element is set as $\omega_{i i}=\sum_{j=1, j \neq i}^{p} \omega_{j i}+0.1$.

Example 2. The structure of the second chain graph is illustrated in Figure 2(b). Particularly, we randomly connect each pair of nodes by an undirected edge with probability 0.03 , and read off multiple chain components $\left\{\tau_{1}, \ldots, \tau_{m}\right\}$ from the set of undirected edges. Then, we set the causal ordering of the chain components as $\left(\pi_{1}, \ldots, \pi_{m}\right)=(1, \ldots, m)$. For each chain component $\tau_{k}$, we randomly select the nodes as hubs with probability 0.2 , and let each hub node points to the nodes in $\cup_{i=k+1}^{m} \tau_{i}$ with probability 0.8 . Similarly, the non-zero values of $\omega_{i j}$ and $\beta_{i j}$ are uniformly generated from $[-1.5,-0.5] \cup[0.5,1.5]$, and $\omega_{i i}=\sum_{j=1, j \neq i}^{p} \omega_{j i}+0.1$.

For each example, we consider four cases with $(p, n)=(50,500),(50,1000),(100,500)$ and $(100,1000)$, and the averaged performance of all four methods over 50 independent replications

![img-1.jpeg](img-1.jpeg)

Figure 2: The chain graph structures in Examples 1 and 2.

are summarized in Tables 1 and 2. As PC only outputs the DAGs with no undirected edges, its evaluation metrics on $\widehat{\Omega}$ are all NA.

Table 1: The averaged evaluation metrics of all the methods in Example 1 together with their standard errors in parentheses.


From Tables 1 and 2, it is clear that the proposed method outperforms all competitors in most scenarios. In Example 1, the proposed method produces a much better estimation of the undirected edges than all other methods. For directed edges, the proposed method achieves the highest $\operatorname{Recall}(\widehat{\mathbf{B}})$ and $\operatorname{MCC}(\widehat{\mathbf{B}})$. It is interesting to note that LCD gets higher Precision( $\widehat{\mathbf{B}})$ than the pro

Table 2: The averaged evaluation metrics of all the methods in Example 2 together with their standard errors in parentheses. Here ** denotes the fact that the corresponding methods take too long to produce any results.


posed method, possibly due to the fact that LCD tends to produce fewer estimated directed edges, resulting in large Precision( $\widehat{\mathbf{B}}$ ) but small Recall( $\widehat{\mathbf{B}}$ ). In Example 2, the proposed method outperforms all competitors in terms of almost all the evaluation metrics. Note that LCD and PC-like take too long to produce any results when $p=100$, due to their expensive computational cost when there exist many hub nodes.

# 5.2 Standard \& Poor index data 

We apply the proposed method to study the relationships among stocks in the Standard \& Poor's 500 index, and analyze the impact of the COVID-19 pandemic on the stock market. Chain graph can accurately reveal various relationships among stocks, with undirected edges for symmetric competitive or cooperative relationship between stocks and directed edges for asymmetric causal relation from one stock to the another.

To proceed, we select $p=100$ stocks with the largest market sizes in the Standard \& Poor's 500 index, and retrieve their adjusted closing prices during the pre-pandemic period, August 2017February 2020, and the post-pandemic period, March 2020-September 2022. The data is publicly available on many finance websites and has been packaged in some standard softwares, such as the R package quantmod. For each period, we first calculate the daily returns of each stock based

on its adjusted closing prices, and then apply the proposed method to construct the corresponding chain graph.

Figure 3 displays the undirected edges between stocks in both estimated chain graphs, which consist of 39 and 21 undirected edges in pre-pandemic and post-pandemic, respectively. It is clear that there are more estimated undirected edges in the pre-pandemic chain graph than in the post-pandemic one, which echos the empirical findings that business expansion were more active, company cooperations were closer and competition were fiercer before the COVID-19 pandemic. Furthermore, there are 13 common undirected edges in both chain graphs, and all these 13 connected stock pairs are from the same sector, including VISA(V) and MASTERCARD(MA), JPMORGAN CHASE(JPM) and BANK OF AMERICA(BAC), MORGAN STANLEY(MS) and GOLDMAN SACHS(GS), and HOME DEPOT(HD) and LOWE'S(LOW). All these pairs share the same type of business, and their competition or cooperation receive less impact by the COVID19 pandemic. In Figure 3, it is also interesting to note that the number of the undirected edges between stocks from different sectors have reduced in the post-pandemic chain graph. This concurs with the fact that diversified business transactions between companies have been decreased and only essential business contacts have been maintained during the COVID-19 pandemic.

Figure 4 displays the boxplots of causal orderings of all stocks within each sector in both pre-pandemic and post-pandemic, where the causal ordering of a stock is set as that of the corresponding chain component. It is generally believed that causal ordering implies the imbalance of social demand and supply; that is, if a sector is getting more demanded, its causal ordering is inclined to move up to upstream. Evidently, Energy and Materials are always at the top of the causal ordering in both periods, as they are upstream industries and provide inputs for most other sectors. The median causal ordering of Telecommunication Services goes from downstream to upstream after the outbreak of the COVID-19 pandemic, since people travel less and rely more on telecommunication for business communication. The median causal ordering of Finances goes down during the pandemic, as commercial entities are more cautious about credit expansion and

![img-2.jpeg](img-2.jpeg)

Figure 3: The left and right panel display all the estimated undirected edges for pre-pandemic and post-pandemic, respectively. Stocks from the same sectors are dyed with the same color, and the common undirected edges in both chain graphs are boldfaced.

Demand for financial services is likely to decline to battle the financial uncertainty. It is somewhat surprising that the median causal ordering of *Healthcares* appears invariant, but many pharmaceutical and biotechnology corporations in this section actually have changed from downstream to upstream, due to the rapid development of vaccine and treatment during the pandemic.

![img-3.jpeg](img-3.jpeg)

Figure 4: The left and right panel display the boxplots of the estimated causal ordering of the top 100 stocks in each sector for pre-pandemic and post-pandemic, respectively. The sectors are ordered according to the median causal ordering of stocks in post-pandemic.

In addition, the estimated chain graphs in pre-pandemic and post-pandemic consist of 149 and 190 directed edges, respectively. While many directed edges remain unchanged, there are some stocks whose roles have changed dramatically in the chain graphs. In particular, some stocks with no child but multiple parents in the pre-pandemic chain graph become ones with no parent but multiple children in the post-pandemic chain graph, such as COSTCO(COST), APPLE(AAPL), ACCENTURE(ACN), INTUIT(INTU), AT\&T(T) and CHUBB(CB). This finding appears reasonable, as most of these stocks correspond to the high demanded industries during pandemic, such as COSTCO for stocking up groceries, AT\&T for remote communication, and APPLE for providing communication and online learning equipment. On the other hand, there are some other stocks with no parent but multiple children in the pre-pandemic chain component becoming ones with no child but multiple parents in the post-pandemic chain component, including TESLA(TSLA), TJX(TJX), BRISTOL-MYERS SQUIBB(BMY), PAYPAL(PYPL), AUTOMATIC DATA PROCESSING(ADP) and BOEING(BA). Many of these companies have been severely impacted during pandemic, such as BOEING due to minimized travels and TESLA due to shrunk consumer purchasing power.

# 6 Conclusion 

In this paper, we establish a set of novel identifiability conditions for the Gaussian chain graph model under AMP interpretation, exploiting a low rank plus sparse decomposition of the precision matrix. An efficient learning algorithm is developed to recover the exact chain graph structure, including both undirected and directed edges. Theoretical analysis shows that the proposed method consistently reconstructs the exact chain graph structure. Its advantage is also supported by various numerical experiments on both simulated and real examples. It is also interesting to extend the proposed identifiability conditions and learning algorithm to accommodate non-linear chain graph model with non-Gaussian noise.

# Acknowledgment 

This work is supported in part by HK RGC Grants GRF-11304520, GRF-11301521 and GRF11311022. The authors report there are no competing interests to declare.

## Appendix: Proof of theorems

In the sequel, we use $c$ and $C$ to denote generic positive constants whose values may vary according to context. For a matrix $\mathbf{M} \in \mathbb{R}^{p \times p}$, let $\mathbf{O}(\mathbf{M}) \in \mathbb{R}^{p \times p}$ denote the matrix with the same off-diagonal elements as $\mathbf{M}$ but all diagonal elements being 0 . Denote $\Lambda_{\max }(\mathbf{M})$ and $\Lambda_{\min }(\mathbf{M})$ as the maximal and minimal eigenvalue of a matrix $\mathbf{M}$, respectively. Let $\mathcal{A}$ be the matrix addition operator such that $\mathcal{A}(\mathbf{A}, \mathbf{B})=\mathbf{A}+\mathbf{B}$ for two matrices $\mathbf{A}$ and $\mathbf{B}$ with the same dimension.

By the definition of $\mathcal{T}(\mathbf{L})$ in (5), it can be shown that $\mathcal{T}(\mathbf{L})$ is uniquely determined by $\mathbf{U}_{1} \in$ $\mathbb{R}^{p \times K}$, where $\mathbf{L}=\mathbf{U}_{1} \mathbf{D}_{1} \mathbf{U}_{1}^{\top}$ is the eigen decomposition of $\mathbf{L}$. With a slight abuse of notation, we denote $\mathcal{T}\left(\mathbf{U}_{1}\right)=\mathcal{T}(\mathbf{L})$. Further, define $F_{\mathbf{U}_{1}}: \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times \mathcal{T}\left(\mathbf{U}_{1}\right) \rightarrow \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times \mathcal{T}\left(\mathbf{U}_{1}\right)$ as

$$
F_{\mathbf{U}_{1}}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right)=\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right), \mathcal{P}_{\mathcal{T}\left(\mathbf{U}_{1}\right)} \mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)\right)
$$

and $F_{\mathbf{U}_{1}}^{\perp}: \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times \mathcal{T}\left(\mathbf{U}_{1}\right) \rightarrow \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)^{\perp} \times \mathcal{T}\left(\mathbf{U}_{1}\right)^{\perp}$ as

$$
F_{\mathbf{U}_{1}}^{\perp}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right)=\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)^{\perp}} \mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right), \mathcal{P}_{\mathcal{T}\left(\mathbf{U}_{1}\right)^{\perp}} \mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)\right)
$$

For any $\mathbf{U}_{1} \in \mathbb{R}^{p \times K}$, define $D\left(\mathbf{U}_{1}\right)=\left\{\mathbf{U}_{1} \mathbf{D}_{1} \mathbf{U}_{1}^{\top}: \mathbf{D}_{1}\right.$ is a $K \times K$ diagonal matrix $\}$. Recall the operators $F$ and $F^{\perp}$ defined in Section 4, and we have $F_{\mathbf{U}_{1}^{*}}=F$ and $F_{\mathbf{U}_{1}^{*}}^{\perp}=F^{\perp}$.

Let $\mathcal{O}_{0}=\left\{(\boldsymbol{\Omega}, \mathbf{L}) \in \mathbb{R}^{p \times 2 p}: \boldsymbol{\Omega} \succ 0, \boldsymbol{\Omega}+\mathbf{L} \succ 0\right\}$, and define a localization set,

$$
\begin{aligned}
& \mathcal{O}(\epsilon)=\left\{(\boldsymbol{\Omega}, \mathbf{L}) \subset \mathcal{O}_{0}: \boldsymbol{\Omega}=\boldsymbol{\Omega}^{*}+\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\boldsymbol{\Omega}} \in \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right),\left\|\boldsymbol{\Delta}_{\boldsymbol{\Omega}}\right\|_{\max } \leq \epsilon\right. \\
& \mathbf{L}=\mathbf{U}_{1} \mathbf{D}_{1} \mathbf{U}_{1}^{\top}, \mathbf{U}_{1} \text { is } p \times K \text { orthogonal matrix with }\left\|\mathbf{U}_{1}-\mathbf{U}_{1}^{*}\right\|_{\max } \leq \epsilon \\
& \left.\mathbf{D}_{1} \text { is } K \times K \text { diagonal matrix with }\left\|\mathbf{D}_{1}-\mathbf{D}_{1}^{*}\right\|_{\max } \leq \epsilon\right\}
\end{aligned}
$$

We rewrite $l(\boldsymbol{\Omega}+\mathbf{L})$ as $l(\boldsymbol{\Omega}, \mathbf{L})$, and define $\bar{l}(\boldsymbol{\Omega}, \mathbf{L})=\mathbb{E} l(\boldsymbol{\Omega}+\mathbf{L})$. Proposition 1 is a key intermediate result to the proof of Theorem 1.

Proposition 1. Suppose $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right) \in \mathcal{Q}$. Then, there exists a small constant $\epsilon>0$ such that $\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ is the unique maximizer of $\bar{l}(\boldsymbol{\Omega}, \mathbf{L})$ in $\mathcal{O}(\epsilon)$.

Proof of Proposition 1. The proof is deferred to the supplement.
Proof of Theorem 1. The proof proceeds in two steps, and we first show that $\boldsymbol{\Omega}=\boldsymbol{\Omega}^{*}$. By Proposition 1, there exists an $\epsilon_{0}$ such that $\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ is the unique maximizer of $\bar{l}(\boldsymbol{\Omega}, \mathbf{L})$ in $\mathcal{O}\left(\epsilon_{0}\right)$.

Note that for any $\epsilon>0$ and $(\boldsymbol{\Omega}, \mathbf{B}) \in \mathcal{Q}$ satisfying $\left\|\boldsymbol{\Omega}-\boldsymbol{\Omega}^{*}\right\|_{\max }<\epsilon$ and $\left\|\mathbf{B}-\mathbf{B}^{*}\right\|_{\max }<\epsilon$, it implies that $\left\|\mathbf{L}-\mathbf{L}^{*}\right\|_{\max } \lesssim \epsilon$. Then, by Weyl's inequality, we have $\left\|\mathbf{D}_{1}-\mathbf{D}_{1}^{*}\right\|_{\max } \lesssim \epsilon$. By the Davis-Kahan theorem [50] and Assumption 2, we have $\left\|\mathbf{U}_{1}-\mathbf{U}_{1}^{*}\right\|_{\max } \lesssim \epsilon$.

Therefore, there exists a sufficiently small $\epsilon>0$ such that for any $(\boldsymbol{\Omega}, \mathbf{B}) \in \mathcal{Q}$ satisfying $\left\|\boldsymbol{\Omega}-\boldsymbol{\Omega}^{*}\right\|_{\max }<\epsilon$ and $\left\|\mathbf{B}-\mathbf{B}^{*}\right\|_{\max }<\epsilon$, we have $(\boldsymbol{\Omega}, \mathbf{L}) \in \mathcal{O}\left(\epsilon_{0}\right)$. If $\left(\mathbf{I}_{p}-\mathbf{B}\right)^{\top} \boldsymbol{\Omega}\left(\mathbf{I}_{p}-\mathbf{B}\right)=$ $\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)^{\top} \boldsymbol{\Omega}^{*}\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)$, we have $\boldsymbol{\Omega}+\mathbf{L}=\boldsymbol{\Omega}^{*}+\mathbf{L}^{*}$, implying that $\bar{l}(\boldsymbol{\Omega}, \mathbf{L})=\bar{l}\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$. By the fact that $\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ is the unique maximizer of $\bar{l}(\boldsymbol{\Omega}, \mathbf{L})$ in $\mathcal{O}\left(\epsilon_{0}\right)$, it must hold true that $(\boldsymbol{\Omega}, \mathbf{L})=\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$.

Next we turn to show that $\mathbf{B}=\mathbf{B}^{*}$. Note that $\boldsymbol{\Omega}=\boldsymbol{\Omega}^{*}$ leads to the same set of chain components $\left\{\tau_{k}\right\}_{k=1}^{m}$, and the assumption that $\left(\mathbf{I}_{p}-\mathbf{B}\right)^{\top} \boldsymbol{\Omega}\left(\mathbf{I}_{p}-\mathbf{B}\right)=\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)^{\top} \boldsymbol{\Omega}^{*}\left(\mathbf{I}_{p}-\mathbf{B}^{*}\right)$ leads to $\boldsymbol{\Sigma}^{*}=\boldsymbol{\Sigma}$. Furthermore, let

$$
\mathcal{D}\left(\tau_{k}, \mathcal{C}\right):=\max _{i \in \tau_{k}}\left\{\operatorname{Var}\left(x_{i} \mid \mathbf{x}_{\mathcal{C}}\right)-\boldsymbol{\Omega}_{i i}^{-1}\right\}
$$

$$
=\max _{i \in \tau_{k}}\left\{\boldsymbol{\Sigma}_{i i}-\boldsymbol{\Sigma}_{i \mathcal{C}} \boldsymbol{\Sigma}_{\mathcal{C} \mathcal{C}}^{-1} \boldsymbol{\Sigma}_{\mathcal{C} i}-\boldsymbol{\Omega}_{i i}^{-1}\right\}
$$

and $\mathcal{D}\left(\tau_{k}, \emptyset\right):=\max _{i \in \tau_{k}}\left\{\boldsymbol{\Sigma}_{i i}-\boldsymbol{\Omega}_{i i}^{-1}\right\}$. The Lemma 3 in the supplement implies that $\mathcal{D}\left(\tau_{\pi_{1}}, \emptyset\right)=0$ for a root chain component $\tau_{\pi_{1}}$ with $\operatorname{pa}\left(\tau_{\pi_{1}}\right)=\emptyset$, and that $\mathcal{D}\left(\tau_{k}, \emptyset\right)>0$ for any other chain component $\tau_{k}$ with $\operatorname{pa}\left(\tau_{k}\right) \neq \emptyset$. Further, let $\mathcal{C}_{j}=\cup_{k=1}^{j} \tau_{\pi_{k}}$ for any $j \geq 1$, and the Lemma 3 in the supplement implies that $\mathcal{D}\left(\tau_{\pi_{j+1}}, \mathcal{C}_{j}\right)=0$ for the $(j+1)$-th chain component $\tau_{\pi_{j+1}}$, and $\mathcal{D}\left(\tau_{k}, \mathcal{C}_{j}\right)>0$ for any chain component $\tau_{k}$ with $\operatorname{pa}\left(\tau_{k}\right) \not \subset \mathcal{C}_{j}$. Therefore, the causal ordering among $\left\{\tau_{k}\right\}_{k=1}^{m}$, denoted as $\left\{\pi_{k}\right\}_{k=1}^{m}$, can be recovered via mathematical induction.

Corresponding to $\left\{\tau_{\pi_{1}}, \ldots, \tau_{\pi_{m}}\right\}$, there exists a permutation matrix $\mathbf{P}_{\pi}$ such that

$$
\mathbf{P}_{\pi} \boldsymbol{\Omega}^{*} \mathbf{P}_{\pi}^{\top}=\mathbf{P}_{\pi} \boldsymbol{\Omega} \mathbf{P}_{\pi}^{\top}=\operatorname{diag}\left(\boldsymbol{\Omega}_{\tau_{\pi_{1}}, \tau_{\pi_{1}}}, \ldots, \boldsymbol{\Omega}_{\tau_{\pi_{m}}, \tau_{\pi_{m}}}\right)
$$

Since $(\boldsymbol{\Omega}, \mathbf{B}),\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right) \in \mathcal{Q}, \mathbf{P}_{\pi} \mathbf{B} \mathbf{P}_{\pi}^{\top}$ and $\mathbf{P}_{\pi} \mathbf{B}^{*} \mathbf{P}_{\pi}^{\top}$ are block lower triangular matrices with $m$ zero diagonal blocks, which implies that the submatrices $\mathbf{B}_{\tau_{\pi_{k}}, \tau_{\pi_{j}}}$ and $\mathbf{B}_{\tau_{\pi_{k}}, \tau_{\pi_{j}}}^{*}$ are zeros for $k \geq j$. Then, for $(\boldsymbol{\Omega}, \mathbf{B}) \in \mathcal{Q}$, it follows from (1) that

$$
\mathbf{x}_{\tau_{\pi_{k}}}=\mathbf{B}_{\tau_{\pi_{k}}, \mathcal{C}_{k-1}} \mathbf{x}_{\mathcal{C}_{k-1}}+\epsilon_{\tau_{\pi_{k}}}
$$

with $\mathbf{x}_{\mathcal{C}_{k-1}} \Perp \epsilon_{\tau_{k}}$, which implies $\mathbf{B}_{\tau_{\pi_{k}}, \mathcal{C}_{k-1}}=\boldsymbol{\Sigma}_{\tau_{\pi_{k}}, \mathcal{C}_{k-1}} \boldsymbol{\Sigma}_{\mathcal{C}_{k-1}, \mathcal{C}_{k-1}}^{-1}$. Similarly, for $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right) \in \mathcal{Q}$, we obtain $\mathbf{B}_{\tau_{\pi_{k}}, \mathcal{C}_{k-1}}^{*}=\boldsymbol{\Sigma}_{\tau_{\pi_{k}}, \mathcal{C}_{k-1}}^{*}\left(\boldsymbol{\Sigma}_{\mathcal{C}_{k-1}, \mathcal{C}_{k-1}}^{*}\right)^{-1}$. Since $\boldsymbol{\Sigma}=\boldsymbol{\Sigma}^{*}, \mathbf{B}_{\tau_{\pi_{k}}, \mathcal{C}_{k-1}}=\mathbf{B}_{\tau_{\pi_{k}}, \mathcal{C}_{k-1}}^{*}$ for any $2 \leq k \leq m$. Therefore, $\mathbf{B}=\mathbf{B}^{*}$, which completes the proof of Theorem 1.

Proof of Theorem 2. Let $h(\boldsymbol{\Omega}, \mathbf{L})=-l(\boldsymbol{\Omega}+\mathbf{L})+\lambda_{n}\left(\|\boldsymbol{\Omega}\|_{1, \text { off }}+\gamma\|\mathbf{L}\|_{*}\right)$,

$$
\begin{aligned}
& \mathcal{O}_{1}=\left\{(\boldsymbol{\Omega}, \mathbf{L}) \subset \mathcal{O}_{0}: \boldsymbol{\Omega}=\boldsymbol{\Omega}^{*}+\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\boldsymbol{\Omega}} \text { is } p \times p\right. \text { symmetric matrix with }\left\|\boldsymbol{\Delta}_{\boldsymbol{\Omega}}\right\|_{\max } \leq \lambda_{n}^{1-2 \eta}, \\
& \mathbf{L}=\mathbf{U D U}^{\top}, \mathbf{U} \text { is } p \times p \text { orthogonal matrix with }\left\|\mathbf{U}-\mathbf{U}^{*}\right\|_{\max } \leq \lambda_{n}^{1-\eta} \\
& \mathbf{D} \text { is } p \times p \text { diagonal matrix with }\left\|\mathbf{D}-\mathbf{D}^{*}\right\|_{\max } \leq \lambda_{n}^{1-2 \eta}\}
\end{aligned}
$$

with $\eta>0$, and $\mathcal{O}_{2}=\left\{(\boldsymbol{\Omega}, \mathbf{L}) \in \mathcal{O}_{1}: \boldsymbol{\Omega}-\boldsymbol{\Omega}^{*} \in \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right), \operatorname{rank}(\mathbf{L}) \leq K\right\}$.
By the compactness of $\mathcal{O}_{2}, h(\boldsymbol{\Omega}, \mathbf{L})$ has a minimizer in $\mathcal{O}_{2}$, denoted as $\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)$, and let $\widehat{\mathbf{L}}_{\mathcal{O}_{2}}=\widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{D}}_{\mathcal{O}_{2}} \widehat{\mathbf{U}}_{\mathcal{O}_{2}}^{\top}$ be its eigen decomposition, where $\widehat{\mathbf{D}}_{\mathcal{O}_{2}}$ is a $K \times K$ diagonal matrix. Further, let $\widehat{\mathcal{O}}=\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)$. By Lemma 4, with probability approaching $1, h(\boldsymbol{\Omega}, \mathbf{L})$ has a unique minimizer in $\widehat{\mathcal{O}}$, denoted as $\left(\widehat{\Omega}_{\widehat{\mathcal{O}}}, \widehat{\mathbf{L}}_{\widehat{\mathcal{O}}}\right)$, and we have $\left(\widehat{\Omega}_{\widehat{\mathcal{O}}}, \widehat{\mathbf{L}}_{\widehat{\mathcal{O}}}\right) \in \mathcal{O}_{2}$. By the definition of $\widehat{\mathcal{O}}$, we also have $\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right) \in \widehat{\mathcal{O}}$. Then, $h\left(\widehat{\Omega}_{\widehat{\mathcal{O}}}, \widehat{\mathbf{L}}_{\widehat{\mathcal{O}}}\right)=h\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)$, which immediately implies that $\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)=\left(\widehat{\Omega}_{\widehat{\mathcal{O}}}, \widehat{\mathbf{L}}_{\widehat{\mathcal{O}}}\right)$,

$$
\left\|\widehat{\Omega}_{\mathcal{O}_{2}}-\boldsymbol{\Omega}^{*}\right\|_{\max }<_{P} \lambda_{n}^{1-\eta}, \text { and }\left\|\widehat{\mathbf{D}}_{\mathcal{O}_{2}}-\mathbf{D}_{1}^{*}\right\|_{\max }<_{P} \lambda_{n}^{1-\eta}
$$

We now turn to bound $\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }$. For any $\boldsymbol{\Delta} \in \mathbb{R}^{p \times p}$, let

$$
R_{n}(\boldsymbol{\Delta})=l\left(\boldsymbol{\Theta}^{*}+\boldsymbol{\Delta}\right)-\bar{l}\left(\boldsymbol{\Theta}^{*}\right)+\frac{1}{2} v(\boldsymbol{\Delta})^{\top} \mathcal{I}^{*} v(\boldsymbol{\Delta})
$$

Then, as $n \rightarrow \infty$ and $\|\boldsymbol{\Delta}\|_{\max } \rightarrow 0$, we have

$$
\begin{aligned}
\left|R_{n}(\boldsymbol{\Delta})-R_{n}(\mathbf{0})\right| & =\left|l\left(\boldsymbol{\Theta}^{*}+\boldsymbol{\Delta}\right)-l\left(\boldsymbol{\Theta}^{*}\right)+\frac{1}{2} v(\boldsymbol{\Delta})^{\top} \mathcal{I}^{*} v(\boldsymbol{\Delta})\right| \\
& =\left|\left\langle\nabla l\left(\boldsymbol{\Theta}^{*}\right), \boldsymbol{\Delta}\right\rangle\right|+O\left(\|\boldsymbol{\Delta}\|_{\max }^{3}\right) \\
& =O_{p}\left(\|\boldsymbol{\Delta}\|_{\max } / \sqrt{n}\right)+O\left(\|\boldsymbol{\Delta}\|_{\max }^{3}\right)
\end{aligned}
$$

where the last equality follows from the fact that $\left\|\nabla l\left(\boldsymbol{\Theta}^{*}\right)\right\|_{\max }=\left\|\widehat{\boldsymbol{\Sigma}}-\left(\boldsymbol{\Theta}^{*}\right)^{-1}\right\|_{\max }=O_{p}(1 / \sqrt{n})$ by the law of large number. Similarly, it can be verified that

$$
\begin{aligned}
\left|\nabla R_{n}(\boldsymbol{\Delta})\right| & =O_{p}(1 / \sqrt{n})+O\left(\|\boldsymbol{\Delta}\|_{\max }^{2}\right) \\
\left|\nabla^{2} R_{n}(\boldsymbol{\Delta})\right| & =O\left(\|\boldsymbol{\Delta}\|_{\max }\right)
\end{aligned}
$$

Particularly, let $\boldsymbol{\Delta}=\widehat{\Omega}_{\widetilde{\mathcal{O}}}+\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}-\boldsymbol{\Omega}^{*}-\mathbf{L}^{*}$,

$$
\begin{aligned}
\|\boldsymbol{\Delta}\|_{\max } & =\left\|\widehat{\Omega}_{\widetilde{\mathcal{O}}}+\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}-\boldsymbol{\Omega}^{*}-\mathbf{L}^{*}\right\|_{\max } \geq\left\|\widehat{\Omega}_{\widetilde{\mathcal{O}}}-\boldsymbol{\Omega}^{*}+\widehat{\Delta}_{\mathbf{L}}\right\|_{\max }-\left\|\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}-\mathbf{L}^{*}-\widehat{\Delta}_{\mathbf{L}}\right\|_{\max } \\
& \gtrsim\left\|\widehat{\Delta}_{\mathbf{L}}\right\|_{\max }-\left\|\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}-\mathbf{L}^{*}-\widehat{\Delta}_{\mathbf{L}}\right\|_{\max }>_{P} c\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }-c \lambda_{n}^{2(1-\eta)}
\end{aligned}
$$

where $\widehat{\Delta}_{\mathbf{L}}=\mathbf{U}_{1}^{*} \mathbf{D}_{1}^{*}\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right)^{\top}+\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right) \mathbf{D}_{1}^{*}\left(\mathbf{U}_{1}^{*}\right)^{\top}+\mathbf{U}_{1}^{*}\left(\widehat{\mathbf{D}}_{\widetilde{\mathcal{O}}}-\mathbf{D}_{1}^{*}\right)\left(\mathbf{U}_{1}^{*}\right)^{\top}$, the second inequality is due to Lemma 2, and the third inequality is due to Lemma 6. By the fact that $\mathcal{I}^{*}$ is positive definite, we have

$$
\frac{1}{2} v(\boldsymbol{\Delta})^{\top} \mathcal{I}^{*} v(\boldsymbol{\Delta}) \geq \frac{1}{2} \Lambda_{\min }\left(\mathcal{I}^{*}\right)\|\boldsymbol{\Delta}\|_{\max }^{2}>_{p} c\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }^{2}-c \lambda_{n}^{4(1-\eta)}
$$

On the other hand, we also have

$$
\begin{aligned}
& \frac{1}{2} v(\boldsymbol{\Delta})^{\top} \mathcal{I}^{*} v(\boldsymbol{\Delta})=\left[R_{n}(\boldsymbol{\Delta})-R_{n}(\mathbf{0})\right]-\left[l\left(\widehat{\Omega}_{\widetilde{\mathcal{O}}}+\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}\right)-l\left(\boldsymbol{\Omega}^{*}+\mathbf{L}^{*}\right)\right] \\
& \leq\left[R_{n}(\boldsymbol{\Delta})-R_{n}(\mathbf{0})\right]+\left[h\left(\widehat{\Omega}_{\widetilde{\mathcal{O}}}, \widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}\right)-h\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)\right]+\lambda_{n}\left\{\left|\left\|\widehat{\Omega}_{\widetilde{\mathcal{O}}}\right\|_{1, \text { off }}-\left\|\boldsymbol{\Omega}^{*}\right\|_{1, \text { off }}\right|+\left|\gamma\left\|\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}\right\|_{*}-\gamma\left\|\mathbf{L}^{*}\right\|_{*}\right|\right\} \\
& \leq\left[R_{n}(\boldsymbol{\Delta})-R_{n}(\mathbf{0})\right]+\lambda_{n}\left\{\left|\left\|\widehat{\Omega}_{\widetilde{\mathcal{O}}}\right\|_{1, \text { off }}-\left\|\boldsymbol{\Omega}^{*}\right\|_{1, \text { off }}\right|+\left|\gamma\left\|\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}\right\|_{*}-\gamma\left\|\mathbf{L}^{*}\right\|_{*}\right|\right\} \\
& \lesssim_{P}\left[R_{n}(\boldsymbol{\Delta})-R_{n}(\mathbf{0})\right]+\lambda_{n}^{2-\eta}=O_{p}(\|\boldsymbol{\Delta}\|_{\max } / \sqrt{n})+O\left(\|\boldsymbol{\Delta}\|_{\max }^{3}+\lambda_{n}^{2-\eta}\right)
\end{aligned}
$$

where the last inequality is due to (11). Therefore, together with the fact that $\|\boldsymbol{\Delta}\|_{\max } \lesssim_{P} \lambda_{n}^{1-\eta}$, we obtain

$$
\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }=O_{p}\left(n^{-\frac{1}{4}} \lambda_{n}^{\frac{1}{2}(1-\eta)}+\lambda_{n}^{1-\frac{\eta}{2}}\right)<_{P} \lambda_{n}^{1-\eta}
$$

Combing the upper bounds for $\left\|\widehat{\Omega}_{\mathcal{O}_{2}}-\boldsymbol{\Omega}^{*}\right\|_{\max },\left\|\widehat{\mathbf{D}}_{\mathcal{O}_{2}}-\mathbf{D}_{1}^{*}\right\|_{\max }$ and $\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }$, we conclude that $\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)$ lies in the interior of $\mathcal{O}_{2}$. Further, let $\boldsymbol{\Delta}_{\mathcal{O}_{2}}=\widehat{\Omega}_{\mathcal{O}_{2}}+\widehat{\mathbf{L}}_{\mathcal{O}_{2}}-\boldsymbol{\Omega}^{*}-\mathbf{L}^{*}$, and $\mathbf{V}_{1}^{*} \in \mathbb{R}^{K \times p}$ contain the right singular vectors of $\mathbf{L}^{*}$, then $\mathbf{V}_{1}^{*}=\mathbf{U}_{1}^{*} \operatorname{sign}\left(\mathbf{D}_{1}^{*}\right)$. Similar as Lemma 5 in [9], we have that $\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)$ is the unique minimizer of $h(\boldsymbol{\Omega}, \mathbf{L})$ in $\mathcal{O}_{2}$, and that

$$
\boldsymbol{\Delta}_{\mathcal{O}_{2}}=\lambda_{n} \mathcal{A}\left[F_{\mathbf{U}_{1}^{*}}^{-1}\left(\operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \mathbf{U}_{1}^{*}\left(\mathbf{V}_{1}^{*}\right)^{\top}\right)\right]+o_{p}\left(\lambda_{n}\right)
$$

Next, we show that $\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)$ is also a minimizer of $h(\boldsymbol{\Omega}, \mathbf{L})$ in $\mathcal{O}_{1}$ by verifying the first order condition. Since $\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)$ is the minimizer of $h(\boldsymbol{\Omega}, \mathbf{L})$ in $\mathcal{O}_{2}$ and lies in its interior,

$$
\mathbf{0} \in \mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \partial_{\boldsymbol{\Omega}} h\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right), \text { and } \mathbf{0} \in \mathcal{P}_{\mathcal{T}\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \partial_{\mathbf{L}} h\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)
$$

Then, it suffices to show that

$$
\mathbf{0} \in \mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)^{\perp}} \partial_{\boldsymbol{\Omega}} h\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right), \text { and } \mathbf{0} \in \mathcal{P}_{\mathcal{T}\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)^{\perp}} \partial_{\mathbf{L}} h\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)
$$

Taking derivatives on both sides of (10) and substituting $\Delta$ by $\Delta_{\mathcal{O}_{2}}$, it follows from (12) and (14) that

$$
\nabla l\left(\widehat{\Omega}_{\mathcal{O}_{2}}+\widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)=\lambda_{n} \mathcal{I}^{*}\left(\mathcal{A}\left[F_{\mathbf{U}_{1}^{*}}^{-1}\left(\operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \mathbf{U}_{1}^{*}\left(\mathbf{V}_{1}^{*}\right)^{\top}\right)\right]\right)+o_{p}\left(\lambda_{n}\right)
$$

which further implies that

$$
\begin{aligned}
\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)^{\perp}} \nabla l\left(\widehat{\Omega}_{\mathcal{O}_{2}}+\widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right) & =\lambda_{n} \mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)^{\perp}} \mathcal{I}^{*}\left(\mathcal{A}\left[F_{\mathbf{U}_{1}^{*}}^{-1}\left(\operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \mathbf{U}_{1}^{*}\left(\mathbf{V}_{1}^{*}\right)^{\top}\right)\right]\right)+o_{p}\left(\lambda_{n}\right) \\
\mathcal{P}_{\mathcal{T}\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)^{\perp}} \nabla l\left(\widehat{\Omega}_{\mathcal{O}_{2}}+\widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right) & =\lambda_{n} \mathcal{P}_{\mathcal{T}\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)^{\perp}} \mathcal{I}^{*}\left(\mathcal{A}\left[F_{\mathbf{U}_{1}^{*}}^{-1}\left(\operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \mathbf{U}_{1}^{*}\left(\mathbf{V}_{1}^{*}\right)^{\top}\right)\right]\right)+o_{p}\left(\lambda_{n}\right) \\
& =\lambda_{n} \mathcal{P}_{\mathcal{T}\left(\mathbf{U}_{1}^{*}\right)^{\perp}} \mathcal{I}^{*}\left(\mathcal{A}\left[F_{\mathbf{U}_{1}^{*}}^{-1}\left(\operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \mathbf{U}_{1}^{*}\left(\mathbf{V}_{1}^{*}\right)^{\top}\right)\right]\right)+o_{p}\left(\lambda_{n}\right)
\end{aligned}
$$

where the last equality is due to the Lipchitz continuity of the projection operator and the fact that $\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }<_{P} \lambda_{n}^{1-\eta}$. Therefore, by Assumption 3, we have

$$
\begin{aligned}
& g_{\gamma}\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)^{\perp}} \nabla l\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right), \mathcal{P}_{\mathcal{T}\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)^{\perp}} \nabla l\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)\right) \\
= & \lambda_{n} g_{\gamma}\left(F_{\mathbf{U}_{1}^{*}}^{-1} F_{\mathbf{U}_{1}^{*}}^{-1}\left(\operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \mathbf{U}_{1}^{*}\left(\mathbf{V}_{1}^{*}\right)^{\top}\right)+o_{p}\left(\lambda_{n}\right)\right.
\end{aligned}
$$

Then the desired first order condition in (15) holds in probability following Lemma 6 in [9], which

means $\left(\widehat{\Omega}_{\mathcal{O}_{2}}, \widehat{\mathbf{L}}_{\mathcal{O}_{2}}\right)$ is a minimizer of $h(\boldsymbol{\Omega}, \mathbf{L})$ in $\mathcal{O}_{1}$. Its uniqueness can be shown following similar argument as for Lemma 7 in [9].

Therefore, $h(\boldsymbol{\Omega}, \mathbf{L})$ has a unique minimizer in $\mathcal{O}_{1} \subset \mathcal{O}_{0}$, denoted as $(\widehat{\Omega}, \widehat{\mathbf{L}})$, which is in the interior of $\mathcal{O}_{1}$ and also belongs to $\mathcal{O}_{2}$. As $h(\boldsymbol{\Omega}, \mathbf{L})$ is a convex function, $\mathcal{O}_{0}$ is a convex set, and $\mathcal{O}_{1}$ contains an open neighborhood of $(\widehat{\Omega}, \widehat{\mathbf{L}})$, we conclude that $(\widehat{\Omega}, \widehat{\mathbf{L}})$ is also the unique minimizer of $h(\boldsymbol{\Omega}, \mathbf{L})$ in $\mathcal{O}_{0}$. The estimation consistencies in (7) also hold due to the fact that $\lambda_{n}^{1-2 \eta}<n^{-1 / 2+2 \eta}$. Furthermore, by definition of $\mathcal{O}_{2}$, we have $\widehat{\Omega}-\boldsymbol{\Omega}^{*} \in \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)$ and $\operatorname{rank}(\widehat{\mathbf{L}}) \leq K$. Then, the sign consistency of $\widehat{\Omega}$ follows since $\min \left\{\left|\omega_{i j}^{*}\right|: \omega_{i j}^{*} \neq 0\right\} \geq c>0$ for a constant $c$, and the rank consistency of $\widehat{\mathbf{L}}$ follows since

$$
\begin{aligned}
& \sigma_{K}(\widehat{\mathbf{L}}) \geq \sigma_{K}\left(\mathbf{L}^{*}\right)-\left\|\widehat{\mathbf{L}}-\mathbf{L}^{*}\right\|_{2} \geq \sigma_{K}\left(\mathbf{L}^{*}\right)-\left\|\widehat{\mathbf{L}}-\mathbf{L}^{*}\right\|_{F} \\
& \geq \sigma_{K}\left(\mathbf{L}^{*}\right)-p\left\|\widehat{\mathbf{L}}-\mathbf{L}^{*}\right\|_{\max }>_{P} \frac{1}{2} \sigma_{K}\left(\mathbf{L}^{*}\right)>0
\end{aligned}
$$

This completes the proof of Theorem 2.

Proposition 2. Under the same conditions of Theorem 2, there holds $\operatorname{Pr}\left(\widehat{\boldsymbol{\pi}} \in \Pi^{*}\right) \rightarrow 1$ as $n \rightarrow \infty$, where $\Pi^{*}$ is the set of all possible true causal orderings of the chain components.

Proof of Proposition 2. The proof is deferred to the supplement.
Proof of Theorem 3. Let $\mathcal{E}=\mathcal{E}_{u} \cup \mathcal{E}_{d}$, where $\mathcal{E}_{u}$ is the set of undirected edges and $\mathcal{E}_{d}$ is the set of directed edges. Then,

$$
\begin{aligned}
\operatorname{Pr}\left(\widehat{\mathcal{G}} \neq \mathcal{G}^{*}\right) & =\operatorname{Pr}\left(\left\{\widehat{\mathcal{E}}_{u} \neq \mathcal{E}_{u}^{*}\right\} \cup\left\{\widehat{\mathcal{E}}_{d} \neq \mathcal{E}_{d}^{*}\right\} \cup\left\{\widehat{\boldsymbol{\pi}} \notin \Pi^{*}\right\}\right) \\
& \leq \operatorname{Pr}\left(\widehat{\mathcal{E}}_{u} \neq \mathcal{E}_{u}^{*}\right)+\operatorname{Pr}\left(\widehat{\boldsymbol{\pi}} \notin \Pi^{*}, \widehat{\mathcal{E}}_{u}=\mathcal{E}_{u}^{*}\right)+\operatorname{Pr}\left(\widehat{\mathcal{E}}_{d} \neq \mathcal{E}_{d}^{*}, \widehat{\mathcal{E}}_{u}=\mathcal{E}_{u}^{*}, \widehat{\boldsymbol{\pi}} \in \Pi^{*}\right) \\
& \leq \operatorname{Pr}\left(\widehat{\mathcal{E}}_{u} \neq \mathcal{E}_{u}^{*}\right)+\operatorname{Pr}\left(\widehat{\boldsymbol{\pi}} \notin \Pi^{*}\left|\widehat{\mathcal{E}}_{u}=\mathcal{E}_{u}^{*}\right)+\operatorname{Pr}\left(\widehat{\mathcal{E}}_{d} \neq \mathcal{E}_{d}^{*}\right| \widehat{\mathcal{E}}_{u}=\mathcal{E}_{u}^{*}, \widehat{\boldsymbol{\pi}} \in \Pi^{*}\right)
\end{aligned}
$$

By Theorem 2 and Proposition 2, we have $\operatorname{Pr}\left(\widehat{\mathcal{E}}_{u} \neq \mathcal{E}_{u}^{*}\right) \rightarrow 0$ and $\operatorname{Pr}\left(\widehat{\boldsymbol{\pi}} \notin \Pi^{*}\left|\widehat{\mathcal{E}}_{u}=\mathcal{E}_{u}^{*}\right\rangle \rightarrow 0\right.$, respectively. It then suffices to bound $\operatorname{Pr}\left(\widehat{\mathcal{E}}_{d} \neq \mathcal{E}_{d}^{*} \mid \widehat{\mathcal{E}}_{u}=\mathcal{E}_{u}^{*}, \widehat{\boldsymbol{\pi}} \in \Pi^{*}\right)$.

Note that $\left\{\operatorname{sign}(\widehat{\mathbf{B}})=\operatorname{sign}\left(\mathbf{B}^{*}\right)\right\} \subseteq\left\{\widehat{\mathcal{E}}_{d}=\mathcal{E}_{d}^{*}\right\}$, where $\widehat{\mathbf{B}}$ is obtained by truncating $\widehat{\mathbf{B}}^{\text {svd }}$ with a thresholding value $\nu_{n}$. Therefore, we turn to bound

$$
\left\|\widehat{\mathbf{B}}^{\mathrm{svd}}-\mathbf{B}^{*}\right\|_{\max } \leq\left\|\widehat{\mathbf{B}}^{\mathrm{reg}}-\mathbf{B}^{*}\right\|_{\max }+\left\|\widehat{\mathbf{B}}^{\mathrm{svd}}-\widehat{\mathbf{B}}^{\mathrm{reg}}\right\|_{\max }
$$

To bound the first term of (16), we assume the true causal ordering of the chain components is $\boldsymbol{\pi}^{*}=$ $\left(\pi_{1}^{*}, \ldots, \pi_{m^{*}}^{*}\right)$. Since $\widehat{\mathbf{B}}_{\pi_{*}^{*}}^{\text {reg }} c_{k-1}^{*}=\widehat{\mathbf{\Sigma}}_{\pi_{k}^{*}} c_{k-1}^{*}\left(\widehat{\mathbf{\Sigma}}_{\mathcal{C}_{k-1}^{*}} c_{k-1}^{*}\right)^{-1}$ and $\mathbf{B}_{\pi_{*}^{*}}^{*} c_{k-1}^{*}=\mathbf{\Sigma}_{\pi_{*}^{*}}^{*} c_{k-1}^{*}\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)^{-1}$, we have

$$
\left\|\widehat{\mathbf{B}}^{\mathrm{reg}}-\mathbf{B}^{*}\right\|_{\max } \leq \max _{2 \leq k \leq m^{*}}\left\|\widehat{\mathbf{\Sigma}}_{\pi_{k}^{*}} c_{k-1}^{*}\left(\widehat{\mathbf{\Sigma}}_{\mathcal{C}_{k-1}^{*}} c_{k-1}^{*}\right)^{-1}-\mathbf{\Sigma}_{\pi_{*}^{*}}^{*} c_{k-1}^{*}\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)^{-1}\right\|_{\max }
$$

It follows from the triangle inequality that

$$
\begin{aligned}
& \left\|\widehat{\mathbf{\Sigma}}_{\pi_{*}^{*}} c_{k-1}^{*}\left(\widehat{\mathbf{\Sigma}}_{\mathcal{C}_{k-1}^{*}} c_{k-1}^{*}\right)^{-1}-\mathbf{\Sigma}_{\pi_{*}^{*}}^{*} c_{k-1}^{*}\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)^{-1}\right\|_{\max } \\
= & \left\|\widehat{\mathbf{\Sigma}}_{\pi_{*}^{*}} c_{k-1}\left(\left(\widehat{\mathbf{\Sigma}}_{\mathcal{C}_{k-1}^{*}} c_{k-1}^{*}\right)^{-1}-\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)^{-1}\right)+\left(\widehat{\mathbf{\Sigma}}_{\pi_{k}^{*}} c_{k-1}^{*}-\mathbf{\Sigma}_{\pi_{*}^{*}}^{*} c_{k-1}^{*}\right)\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)^{-1}\right\|_{\max } \\
\leq & \left\|\widehat{\mathbf{\Sigma}}_{\pi_{*}^{*}} c_{k-1}\right\|_{2}\left\|\left(\widehat{\mathbf{\Sigma}}_{\mathcal{C}_{k-1}^{*}} c_{k-1}^{*}\right)^{-1}-\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)^{-1}\right\|_{2}+\left\|\widehat{\mathbf{\Sigma}}_{\pi_{*}^{*}} c_{k-1}-\mathbf{\Sigma}_{\pi_{*}^{*}}^{*} c_{k-1}\right\|_{2}\left\|\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)^{-1}\right\|_{2}
\end{aligned}
$$

By Corollary 2.4.5 of [16], we have $\left\|\widehat{\mathbf{\Sigma}}_{\pi_{k}^{*}} c_{k-1}\right\|_{2}-\left\|\mathbf{\Sigma}_{\pi_{*}^{*}}^{*} c_{k-1}\right\|_{2} \leq\left\|\widehat{\mathbf{\Sigma}}_{\pi_{*}^{*}} c_{k-1}-\mathbf{\Sigma}_{\pi_{*}^{*}}^{*} c_{k-1}\right\|_{2} \leq$ $\left\|\widehat{\mathbf{\Sigma}}_{\mathcal{C}_{k}^{*}} c_{k}-\mathbf{\Sigma}_{\mathcal{C}_{k}^{*}}^{*} c_{k}\right\|_{2}$. Also, it follows from Lemma 1 of [40] that

$$
\left\|\widehat{\mathbf{\Sigma}}_{\mathcal{C}_{k-1}^{*}} c_{k-1}^{*}-\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}} c_{k-1}^{*}\right\|_{\max } \leq\left\|\widehat{\mathbf{\Sigma}}-\mathbf{\Sigma}^{*}\right\|_{\max } \lesssim_{P} n^{-\frac{1}{2}+\eta}
$$

Since $\left|\mathcal{C}_{k-1}^{*}\right|$ and $\Lambda_{\min }\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*}\right)$ are fixed, we have $n^{-\frac{1}{2}+\eta} \leq \frac{\Lambda_{\min }\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)}{2\left|\mathcal{C}_{k-1}^{*}\right|}$ when $n$ is sufficiently large. It then follows from Lemma 7 that

$$
\left\|\left(\widehat{\mathbf{\Sigma}}_{\mathcal{C}_{k-1}^{*}} c_{k-1}^{*}\right)^{-1}-\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)^{-1}\right\|_{\max } \lesssim_{P} \frac{2\left|\mathcal{C}_{k-1}^{*}\right|}{\Lambda_{\min }^{2}\left(\mathbf{\Sigma}_{\mathcal{C}_{k-1}^{*}}^{*} c_{k-1}^{*}\right)} n^{-\frac{1}{2}+\eta}
$$

Combing all these results, we have

$$
\begin{aligned}
& \left\|\widehat{\mathbf{B}}^{\text {reg }}-\mathbf{B}^{*}\right\|_{\max } \\
\leq & \max _{2 \leq k \leq m^{*}}\left\{\left(\left\|\boldsymbol{\Sigma}_{\tau_{\sigma_{k}}^{*} c_{k-1}^{*}}^{*}\right\|_{2}+\left\|\widehat{\boldsymbol{\Sigma}}_{c_{k}^{*} c_{k}}-\boldsymbol{\Sigma}_{\mathcal{C}_{k}^{*} c_{k}^{*}}^{*}\right\|_{2}\right)\left\|\left(\widehat{\boldsymbol{\Sigma}}_{\mathcal{C}_{k-1}^{*} c_{k-1}^{*}}\right)^{-1}-\left(\boldsymbol{\Sigma}_{\mathcal{C}_{k-1}^{*} c_{k-1}^{*}}^{*}\right)^{-1}\right\|_{2}\right. \\
& \left.+\left\|\widehat{\boldsymbol{\Sigma}}_{\tau_{\sigma_{k}}^{*} c_{k-1}^{*}}-\boldsymbol{\Sigma}_{\tau_{\sigma_{k}}^{*} c_{k-1}^{*}}^{*}\right\|_{2}\right\|\left(\boldsymbol{\Sigma}_{\mathcal{C}_{k-1}^{*} c_{k-1}^{*}}^{*}\right)^{-1}\left\|_{2}\right\} \\
\leq & \max _{2 \leq k \leq m^{*}}\left\{\left(\Lambda_{\max }\left(\boldsymbol{\Sigma}^{*}\right)+\left\|\widehat{\boldsymbol{\Sigma}}_{\mathcal{C}_{k}^{*} c_{k}}-\boldsymbol{\Sigma}_{\mathcal{C}_{k}^{*} c_{k}^{*}}^{*}\right\|_{2}\right)\left\|\left(\widehat{\boldsymbol{\Sigma}}_{\mathcal{C}_{k-1}^{*} c_{k-1}^{*}}\right)^{-1}-\left(\boldsymbol{\Sigma}_{\mathcal{C}_{k-1}^{*} c_{k-1}^{*}}^{*}\right)^{-1}\right\|_{2}\right. \\
& +\left\|\widehat{\boldsymbol{\Sigma}}_{\tau_{\sigma_{k}}^{*} c_{k-1}^{*}}-\boldsymbol{\Sigma}_{\tau_{\sigma_{k}}^{*} c_{k-1}^{*}}^{*}\right\|_{2} \frac{1}{\Lambda_{\min }\left(\boldsymbol{\Sigma}^{*}\right)}\right\} \\
\leq_{P} & \max _{v m^{*}}\left\{\left(\Lambda_{\max }\left(\boldsymbol{\Sigma}^{*}\right)+n^{-\frac{1}{2}+\eta}\right) \frac{2\left|\mathcal{C}_{k-1}^{*}\right|}{\Lambda_{\min }^{2}\left(\boldsymbol{\Sigma}_{\mathcal{C}_{k-1}^{*} c_{k-1}^{*}}^{*}\right)} n^{-\frac{1}{2}+\eta}+\frac{1}{\Lambda_{\min }\left(\boldsymbol{\Sigma}^{*}\right)} n^{-\frac{1}{2}+\eta}\right\} \\
\leq & \left(\frac{2 \Lambda_{\max }\left(\boldsymbol{\Sigma}^{*}\right) p}{\Lambda_{\min }^{2}\left(\boldsymbol{\Sigma}^{*}\right)}+\frac{1}{\Lambda_{\min }\left(\boldsymbol{\Sigma}^{*}\right)}+\frac{2 p}{\Lambda_{\min }^{2}\left(\boldsymbol{\Sigma}^{*}\right)} n^{-\frac{1}{2}+\eta}\right) n^{-\frac{1}{2}+\eta} \lesssim_{P} n^{-\frac{1}{2}+\eta}
\end{aligned}
$$

To bound the second term of (16), we have

$$
\begin{aligned}
\left\|\widehat{\mathbf{B}}^{\text {svd }}-\widehat{\mathbf{B}}^{\text {reg }}\right\|_{\max } & =\left\|\widehat{\mathbf{U}}^{\text {svd }}\left(\widehat{\mathbf{D}}^{\text {svd }}-\widehat{\mathbf{D}}^{\text {reg }}\right)\left(\widehat{\mathbf{V}}^{\text {svd }}\right)^{\top}\right\|_{\max } \\
& \leq\left\|\widehat{\mathbf{U}}^{\text {svd }}\right\|_{2}\left\|\widehat{\mathbf{D}}^{\text {svd }}-\widehat{\mathbf{D}}^{\text {reg }}\right\|_{2}\left\|\widehat{\mathbf{V}}^{\text {svd }}\right\|_{2}=\left\|\widehat{\mathbf{D}}^{\text {svd }}-\widehat{\mathbf{D}}^{\text {reg }}\right\|_{\max } \leq \kappa_{n}
\end{aligned}
$$

Therefore, $\left\|\widehat{\mathbf{B}}^{\text {svd }}-\mathbf{B}^{*}\right\|_{\max } \lesssim_{P} n^{-\frac{1}{2}+\eta}$. Then, since $\nu_{n}=n^{-\frac{1}{2}+2 \eta}$, we obtain

$$
\operatorname{Pr}\left(\operatorname{sign}(\widehat{\mathbf{B}})=\operatorname{sign}\left(\mathbf{B}^{*}\right) \mid \widehat{\mathcal{E}}_{u}=\mathcal{E}_{u}^{*}, \widehat{\boldsymbol{\pi}} \in \Pi^{*}\right) \rightarrow 1
$$

We complete the proof since $\left\{\operatorname{sign}(\widehat{\mathbf{B}})=\operatorname{sign}\left(\mathbf{B}^{*}\right)\right\} \subseteq\left\{\widehat{\mathcal{E}}_{d}=\mathcal{E}_{d}^{*}\right\}$.

# Supplement: Auxiliary lemmas 

Similar to $F_{\mathbf{U}_{1}}$, we denote $G_{\mathbf{U}_{1}}: \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times\left(D\left(\mathbf{U}_{1}\right)-\mathbf{L}^{*}\right) \rightarrow \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times D\left(\mathbf{U}_{1}\right)$ as

$$
G_{\mathbf{U}_{1}}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right)=\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right), \mathcal{P}_{D\left(\mathbf{U}_{1}\right)} \mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)\right)
$$

Lemma 1. For $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right) \in \mathcal{Q}$, both $F_{\mathbf{U}_{1}^{*}}$ and $G_{\mathbf{U}_{1}^{*}}$ are invertible. Furthermore, there exists a small $\epsilon>0$ such that for any $\mathbf{U}_{1} \in \mathbb{R}^{p \times K}$ satisfying $\left\|\mathbf{U}_{1}-\mathbf{U}_{1}^{*}\right\|_{\max }<\epsilon$, it holds true that $\left\|F_{\mathbf{U}_{1}}^{-1}\right\| \leq C$ and $\left\|G_{\mathbf{U}_{1}}^{-1}\right\| \leq C$, where the norm is the operator norm induced by $g_{\gamma}$.

Proof of Lemma 1. The invertibility of $F_{\mathbf{U}_{1}^{*}}$ and $G_{\mathbf{U}_{1}^{*}}$ is shown by Lemma 1 in [9]. Further, it is not difficult to show that for there exists a $\epsilon>0$ such that if $\left\|\mathbf{U}_{1}-\mathbf{U}_{1}^{*}\right\|_{\max }<\epsilon$, then $\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \cap \mathcal{T}\left(\mathbf{U}_{1}\right)=$ $\emptyset$, which implies the invertibility of $F_{\mathbf{U}_{1}}$ and $G_{\mathbf{U}_{1}}$. The boundedness of their inverses follows.

Lemma 2. For $\left(\boldsymbol{\Omega}^{*}, \mathbf{B}^{*}\right) \in \mathcal{Q}$, it holds true that

$$
\inf _{\substack{(\boldsymbol{\Omega}, \mathbf{L}) \in \mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times \mathcal{T}\left(\mathbf{L}^{*}\right)}} \frac{\|\boldsymbol{\Omega}+\mathbf{L}\|_{\max }}{\|\mathbf{L}\|_{\max }}>0
$$

Proof of Lemma 2. The proof of Lemma 2 is similar to Lemma 3 in [9], and thus omitted here.
Lemma 3. Suppose that $\mathbf{x}=\left(x_{1}, \ldots, x_{p}\right)^{\top} \in \mathbb{R}^{p}$ is generated from the linear SEM model (1) with parameters $(\boldsymbol{\Omega}, \mathbf{B}) \in \mathcal{Q}$. For any $0 \leq s \leq m-2$ and $k \in[m] \backslash \cup_{j=1}^{s} \pi_{j}$, it holds true that

$$
\mathcal{D}\left(\tau_{k}, \mathcal{C}_{s}\right)=\max _{i \in \tau_{k}}\left(\operatorname{Var}\left(x_{i} \mid \mathbf{x}_{\mathcal{C}_{s}}\right)-\boldsymbol{\Omega}_{i i}^{-1}\right)\left\{\begin{array}{lll}
=0, & \text { if } p a\left(\tau_{k}\right) \subseteq \mathcal{C}_{s} \\
>0, & \text { if } p a\left(\tau_{k}\right) \not \subseteq \mathcal{C}_{s}
\end{array}\right.
$$

where $\mathcal{C}_{0}=\emptyset$ and $\mathcal{C}_{s}=\cup_{j=1}^{s} \tau_{\pi_{j}}$.
Proof of Lemma 3. It follows from (1) that

$$
\operatorname{Cov}(\mathbf{X})=\boldsymbol{\Sigma}=\mathbf{M M}^{\top}
$$

where $\mathbf{M}=\mathbf{A} \boldsymbol{\Omega}^{-1 / 2}$ and $\mathbf{A}=\left(\mathbf{I}_{p}-\mathbf{B}\right)^{-1}=\left(a_{i j}\right)_{p \times p}$. Note that the off-diagonal element of $\mathbf{A}$ is called the total causal effect [8] from one node to another. Particularly, $a_{i j}$ is the sum of the effects of all directed paths from node $j$ to node $i$, where the effect of each directed path is the product of the coefficient of all directed edges, and $a_{i i}=1$ for $i \in[p]$. Then, it follows from (19) that the submatrix of $\boldsymbol{\Sigma}$ corresponding to the node set $\mathcal{C}_{s} \cup \tau_{k}$ is

$$
\boldsymbol{\Sigma}_{\mathcal{C}_{s} \cup \tau_{k}, \mathcal{C}_{s} \cup \tau_{k}}=\mathbf{M}_{\mathcal{C}_{s} \cup \tau_{k}, \mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}} \mathbf{M}_{\mathcal{C}_{s} \cup \tau_{k}, \mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}}^{\top}
$$

where $\mathcal{C}_{s}^{c}=[p] \backslash \mathcal{C}_{s}$ and

$$
\mathbf{M}_{\mathcal{C}_{s} \cup \tau_{k}, \mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}}=\left(\begin{array}{cc}
\mathbf{M}_{\mathcal{C}_{s}, \mathcal{C}_{s}} & \mathbf{M}_{\mathcal{C}_{s}, \mathcal{C}_{s}^{c}} \\
\mathbf{M}_{\tau_{k}, \mathcal{C}_{s}} & \mathbf{M}_{\tau_{k}, \mathcal{C}_{s}^{c}}
\end{array}\right)
$$

Note that

$$
\mathbf{M}_{\mathcal{C}_{s} \cup \tau_{k}, \mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}}=\mathbf{A}_{\mathcal{C}_{s} \cup \tau_{k}, \mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}} \boldsymbol{\Omega}_{\mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}, \mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}}^{-1 / 2}
$$

where

$$
\mathbf{A}_{\mathcal{C}_{s} \cup \tau_{k}, \mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}}=\left(\begin{array}{cc}
\mathbf{A}_{\mathcal{C}_{s}, \mathcal{C}_{s}} & \mathbf{A}_{\mathcal{C}_{s}, \mathcal{C}_{s}^{c}} \\
\mathbf{A}_{\tau_{k}, \mathcal{C}_{s}} & \mathbf{A}_{\tau_{k}, \mathcal{C}_{s}^{c}}
\end{array}\right)
$$

and

$$
\boldsymbol{\Omega}_{\mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}, \mathcal{C}_{s} \cup \mathcal{C}_{s}^{c}}^{1 / 2}=\left(\begin{array}{cc}
\boldsymbol{\Omega}_{\mathcal{C}_{s}, \mathcal{C}_{s}}^{-1 / 2} & \boldsymbol{\Omega}_{\mathcal{C}_{s}, \mathcal{C}_{s}^{c}}^{-1 / 2} \\
\boldsymbol{\Omega}_{\mathcal{C}_{s}^{c}, \mathcal{C}_{s}} & \boldsymbol{\Omega}_{\mathcal{C}_{s}^{c}, \mathcal{C}_{s}^{c}}^{-1 / 2}
\end{array}\right)
$$

It follows from the fact that there exists no directed edge from node in lower chain components to nodes in upper chain components that $\mathbf{A}_{\mathcal{C}_{s}, \mathcal{C}_{s}^{c}}=\mathbf{0}_{\left|\mathcal{C}_{s}\right| \times\left|\mathcal{C}_{s}^{c}\right|}$. Further, since there is no undirected edge across different chain components, we have $\boldsymbol{\Omega}_{\mathcal{C}_{s}, \mathcal{C}_{s}^{c}}^{-1 / 2}=\left(\boldsymbol{\Omega}_{\mathcal{C}_{s}^{c}, \mathcal{C}_{s}}^{-1 / 2}\right)^{\top}=\mathbf{0}_{\left|\mathcal{C}_{s}\right| \times\left|\mathcal{C}_{s}^{c}\right|}$. Thus, there holds

$$
\mathbf{M}_{\mathcal{C}_{s}, \mathcal{C}_{s}^{c}}=\mathbf{A}_{\mathcal{C}_{s}, \mathcal{C}_{s}} \boldsymbol{\Omega}_{\mathcal{C}_{s}, \mathcal{C}_{s}^{c}}^{-1 / 2}+\mathbf{A}_{\mathcal{C}_{s}, \mathcal{C}_{s}^{c}} \boldsymbol{\Omega}_{\mathcal{C}_{s}^{c}, \mathcal{C}_{s}^{c}}^{-1 / 2}=\mathbf{0}_{\left|\mathcal{C}_{s}\right| \times\left|\mathcal{C}_{s}^{c}\right|}
$$

Then, we have

$$
\begin{aligned}
\operatorname{Cov}\left(\mathbf{x}_{\tau_{k}} \mid \mathbf{x}_{\mathcal{C}_{s}}\right) & =\boldsymbol{\Sigma}_{\tau_{k}, \tau_{k}}-\boldsymbol{\Sigma}_{\tau_{k}, \mathcal{C}_{s}}\left(\boldsymbol{\Sigma}_{\mathcal{C}_{s}, \mathcal{C}_{s}}\right)^{-1} \boldsymbol{\Sigma}_{\mathcal{C}_{s}, \tau_{k}} \\
& =\mathbf{M}_{\tau_{k}, \mathcal{C}_{s}} \mathbf{M}_{\tau_{k}, \mathcal{C}_{s}}^{\top}+\mathbf{M}_{\tau_{k}, \mathcal{C}_{s}^{c}} \mathbf{M}_{\tau_{k}, \mathcal{C}_{s}^{c}}^{\top}-\mathbf{M}_{\tau_{k}, \mathcal{C}_{s}} \mathbf{M}_{\mathcal{C}_{s}, \mathcal{C}_{s}}^{\top}\left(\mathbf{M}_{\mathcal{C}_{s}, \mathcal{C}_{s}} \mathbf{M}_{\mathcal{C}_{s}, \mathcal{C}_{s}}^{\top}\right)^{-1} \mathbf{M}_{\mathcal{C}_{s}, \mathcal{C}_{s}} \mathbf{M}_{\tau_{k}, \mathcal{C}_{s}}^{\top} \\
& =\mathbf{M}_{\tau_{k}, \mathcal{C}_{s}^{c}} \mathbf{M}_{\tau_{k}, \mathcal{C}_{s}^{c}}^{\top} \\
& =\mathbf{A}_{\tau_{k}, \mathcal{C}_{s}^{c}} \boldsymbol{\Omega}_{\mathcal{C}_{s}^{c}, \mathcal{C}_{s}^{c}}^{-1} \mathbf{A}_{\tau_{k}, \mathcal{C}_{s}^{c}}^{\top} \\
& =\boldsymbol{\Omega}_{\tau_{k}, \tau_{k}}^{-1}+\sum_{j \in[m] \backslash\left(\left(\cup_{j=1}^{s} \pi_{j}\right) \cup\{k\}\right)} \mathbf{A}_{\tau_{k}, \tau_{j}} \boldsymbol{\Omega}_{\tau_{j}, \tau_{j}}^{-1} \mathbf{A}_{\tau_{k}, \tau_{j}}^{\top}
\end{aligned}
$$

where the second equality follows from (20) and the fourth equality follows from (21).
If $\operatorname{pa}\left(\tau_{k}\right) \subseteq \mathcal{C}_{s}$, it follows from the fact that $\mathbf{A}_{\tau_{k}, \tau_{j}}=\mathbf{0}_{\left|\tau_{k}\right| \times\left|\tau_{j}\right|}$ for $j \in[m] \backslash\left(\left(\cup_{j=1}^{s} \pi_{j}\right) \cup\{k\}\right)$ that (22) can be rewritten as $\operatorname{Cov}\left(\mathbf{x}_{\tau_{k}} \mid \mathbf{x}_{\mathcal{C}_{s}}\right)=\boldsymbol{\Omega}_{\tau_{k}, \tau_{k}}^{-1}$, which implies that $\mathcal{D}\left(\tau_{k}, \mathcal{C}_{s}\right)=0$.

If $\operatorname{pa}\left(\tau_{k}\right) \nsubseteq \mathcal{C}_{s}$, it follows from no semi-directed cycle assumption that there exists a node $l \in \tau_{k}$ and another node $t \in \tau_{i} \subseteq \mathcal{C}_{s}^{c} \backslash \tau_{k}$ such that $t \in \operatorname{pa}(l)$ and no other directed path from node $t$ to node $l$. Then, we have

$$
\begin{aligned}
\operatorname{Var}\left(x_{l} \mid \mathbf{x}_{\mathcal{C}_{s}}\right) & =e_{l}^{\top} \operatorname{Cov}\left(\mathbf{x}_{\tau_{k}} \mid \mathbf{x}_{\mathcal{C}_{s}}\right) e_{l} \\
& =\boldsymbol{\Omega}_{l l}^{-1}+\sum_{j \in[m] \backslash\left(\left(\cup_{j=1}^{s} \pi_{j}\right) \cup\{k\}\right)} e_{l}^{\top} \mathbf{A}_{\tau_{k}, \tau_{j}} \boldsymbol{\Omega}_{\tau_{j}, \tau_{j}}^{-1} \mathbf{A}_{\tau_{k}, \tau_{j}}^{\top} e_{l} \\
& \geq \boldsymbol{\Omega}_{l l}^{-1}+\left(\mathbf{A}_{\tau_{k}, \tau_{i}}^{\top} e_{l}\right)^{\top} \boldsymbol{\Omega}_{\tau_{i}, \tau_{i}}^{-1} \mathbf{A}_{\tau_{k}, \tau_{i}}^{\top} e_{l}
\end{aligned}
$$

where $e_{l} \in\{0,1\}^{\left|\tau_{k}\right|}$ and only the element of $e_{l}$ corresponding to node $l$ is equal to 1 , and the last inequality follows from the fact that $\boldsymbol{\Omega}_{\tau_{j}, \tau_{j}}^{-1}$ is positive definite. Next, denote $\left[\mathbf{A}_{\tau_{k}, \tau_{i}}\right]_{l t}$ as the element of $\mathbf{A}_{\tau_{k}, \tau_{i}}$ corresponding to node $l \in \tau_{k}$ and $t \in \tau_{i}$. Since $t \in \mathrm{pa}(l)$ and there is no other directed path from node $t$ to node $l$, we have $\left[\mathbf{A}_{\tau_{k}, \tau_{i}}\right]_{l t}=\beta_{l t} \neq 0$ which implies $\mathbf{A}_{\tau_{k}, \tau_{i}}^{\top} e_{l} \neq \mathbf{0}_{\left|\tau_{i}\right|}$.

Then, it follows from (23) and the fact that $\Omega_{\tau_{i}, \tau_{i}}^{-1}$ is positive definite that

$$
\operatorname{Var}\left(x_{l} \mid \mathbf{x}_{\mathcal{C}_{s}}\right)>\boldsymbol{\Omega}_{l l}^{-1}
$$

Thus, there holds

$$
\mathcal{D}\left(\tau_{k}, \mathcal{C}_{s}\right)=\max _{i \in \tau_{k}}\left\{\operatorname{Var}\left(x_{i} \mid \mathbf{x}_{\mathcal{C}_{s}}\right)-\boldsymbol{\Omega}_{i i}^{-1}\right\} \geq \operatorname{Var}\left(x_{l} \mid \mathbf{x}_{\mathcal{C}_{s}}\right)-\boldsymbol{\Omega}_{l l}^{-1}>0
$$

This completes the proof.

Lemma 4. Let $\widehat{\mathcal{O}}=\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)$. Then, with probability approaching $1, h(\boldsymbol{\Omega}, \mathbf{L})$ has a unique minimizer in $\widehat{\mathcal{O}}$, denoted as $\left(\widehat{\Omega}_{\widehat{\mathcal{O}}}, \widehat{\mathbf{L}}_{\widehat{\mathcal{O}}}\right)$. Let $\widehat{\mathbf{L}}_{\widehat{\mathcal{O}}}=\widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{D}}_{\widehat{\mathcal{O}}} \widehat{\mathbf{U}}_{\mathcal{O}_{2}}^{\top}$ be the eigen decomposition, then we have

$$
\left\|\widehat{\mathbf{D}}_{\widehat{\mathcal{O}}}-\mathbf{D}_{1}^{*}\right\|_{\max } \lesssim_{P} \lambda_{n}^{1-\eta}, \text { and }\left\|\widehat{\Omega}_{\widehat{\mathcal{O}}}-\boldsymbol{\Omega}^{*}\right\|_{\max } \lesssim_{P} \lambda_{n}^{1-\eta}
$$

Proof of Lemma 4. We first show the existence and uniqueness for the minimizer of $h(\boldsymbol{\Omega}, \mathbf{L})$ in $\widehat{\mathcal{O}}=\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right) \times D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)$. This is equivalent to show that there exists a unique $(\boldsymbol{\Omega}, \mathbf{L}) \in \widehat{\mathcal{O}}$ such that the following first order condition holds:

$$
\mathbf{0} \in \mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \partial_{\boldsymbol{\Omega}} h(\boldsymbol{\Omega}, \mathbf{L}), \text { and } \mathbf{0} \in \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \partial_{\mathbf{L}} h(\boldsymbol{\Omega}, \mathbf{L})
$$

Since $h(\boldsymbol{\Omega}, \mathbf{L})$ is convex on the linear subspace $\widehat{\mathcal{O}}$, it suffices to show there exists a unique $(\boldsymbol{\Omega}, \mathbf{L}) \in$ $\mathcal{B}$ such that (24) holds, where

$$
\mathcal{B}=\left\{(\boldsymbol{\Omega}, \mathbf{L}) \in \widehat{\mathcal{O}}: g_{\gamma}\left(\boldsymbol{\Omega}-\boldsymbol{\Omega}^{*}, \mathbf{L}-\mathbf{L}^{*}\right) \leq \lambda_{n}^{1-\eta}\right\}
$$

is a neighborhood of $\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ in $\widehat{\mathcal{O}}$. Note that for $(\boldsymbol{\Omega}, \mathbf{L}) \in \mathcal{B}$, we have

$$
\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \partial_{\boldsymbol{\Omega}}\|\boldsymbol{\Omega}\|_{1, \text { off }}=\operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right) \text { and } \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \partial_{\mathbf{L}}\|\mathbf{L}\|_{*}=\widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{V}}_{\mathcal{O}_{2}}^{\top}
$$

where $\widehat{\mathbf{U}}_{\mathcal{O}_{2}}$ contains the right singular vectors of $\widehat{\mathbf{L}}_{\mathcal{O}_{2}}$, which is the same as $\widehat{\mathbf{U}}_{\mathcal{O}_{2}}$ except that the columns corresponding to the negative eigenvalues are multiplied by a negative sign.

In the following, we denote $\boldsymbol{\Delta}_{\boldsymbol{\Omega}}=\boldsymbol{\Omega}-\boldsymbol{\Omega}^{*}, \boldsymbol{\Delta}_{\mathbf{L}}=\mathbf{L}-\mathbf{L}^{*}$ and $\boldsymbol{\Delta}=\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}$. By (10), we have

$$
\begin{aligned}
& \mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \partial_{\boldsymbol{\Omega}} h(\boldsymbol{\Omega}, \mathbf{L})=\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)+\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla R_{n}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)+\lambda_{n} \operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right) \\
& \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \partial_{\mathbf{L}} h(\boldsymbol{\Omega}, \mathbf{L})=\mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \mathcal{I}^{*} v\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)+\mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \nabla R_{n}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}\right)+\gamma \lambda_{n} \widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{V}}_{\mathcal{O}_{2}}^{\top} .
\end{aligned}
$$

Then, the first order condition becomes

$$
G_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right)=-\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla R_{n}(\boldsymbol{\Delta})+\lambda_{n} \operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \nabla R_{n}(\boldsymbol{\Delta})+\gamma \lambda_{n} \widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{V}}_{\mathcal{O}_{2}}^{\top}\right)
$$

By Lemma 1, the mapping $G_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}$ is invertible and $G_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}^{-1}$ is bounded. Define an operator on $\mathcal{B} \backslash$ $\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ as
$\mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right)=-G_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}^{-1}\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla R_{n}(\boldsymbol{\Delta})+\lambda_{n} \operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \nabla R_{n}(\boldsymbol{\Delta})+\gamma \lambda_{n} \widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{V}}_{\mathcal{O}_{2}}^{\top}\right)$.

Lemma 5 shows that, with probability approaching $1, \mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}$ is a contraction mapping on $\mathcal{B}$. By the fixed point theorem, there exists a unique solution $\left(\widehat{\Delta}_{\Omega}, \widehat{\Delta}_{\mathbf{L}}\right) \in \mathcal{B}$ such that

$$
\mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}\left(\widehat{\Delta}_{\Omega}, \widehat{\Delta}_{\mathbf{L}}\right)=\left(\widehat{\Delta}_{\Omega}, \widehat{\Delta}_{\mathbf{L}}\right)
$$

We complete the proof by letting $\widehat{\Omega}_{\widehat{\mathcal{O}}}=\boldsymbol{\Omega}^{*}+\widehat{\Delta}_{\boldsymbol{\Omega}}$ and $\widehat{\mathbf{L}}_{\widehat{\mathcal{O}}}=\mathbf{L}^{*}+\widehat{\Delta}_{\mathbf{L}}$.
Lemma 5. With probability approaching 1, $\mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}(\mathcal{B}) \subset \mathcal{B}$. Furthermore, $\mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}$ is a contraction mapping on $\mathcal{B}$.

Proof of Lemma 5. For $\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right) \in \mathcal{B}$, denote $\boldsymbol{\Delta}=\boldsymbol{\Delta}_{\boldsymbol{\Omega}}+\boldsymbol{\Delta}_{\mathbf{L}}$. Then, we have

$$
\begin{aligned}
& g_{\gamma}\left(\mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right)\right) \\
& \leq g_{\gamma}\left(G_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}^{-1}\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla R_{n}(\boldsymbol{\Delta}), \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \nabla R_{n}(\boldsymbol{\Delta})\right)\right)+g_{\gamma}\left(G_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}^{-1}\left(\lambda_{n} \operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \lambda_{n} \widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{V}}_{\mathcal{O}_{2}}^{\top}\right)\right) \\
& \lesssim g_{\gamma}\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla R_{n}(\boldsymbol{\Delta}), \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \nabla R_{n}(\boldsymbol{\Delta})\right)+g_{\gamma}\left(\lambda_{n} \operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \lambda_{n} \widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{V}}_{\mathcal{O}_{2}}^{\top}\right)
\end{aligned}
$$

where the second inequality is due to Lemma 1. By (12), we have

$$
g_{\gamma}\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla R_{n}(\boldsymbol{\Delta}), \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)} \nabla R_{n}(\boldsymbol{\Delta})\right)=O_{p}\left(\frac{1}{\sqrt{n}}\right)+O\left(\lambda_{n}^{2(1-\eta)}\right) \lesssim_{P} \lambda_{n}^{1-\eta}
$$

and it hold true that $g_{\gamma}\left(\lambda_{n} \operatorname{sign}\left(\mathbf{O}\left(\boldsymbol{\Omega}^{*}\right)\right), \gamma \lambda_{n} \widehat{\mathbf{U}}_{\mathcal{O}_{2}} \widehat{\mathbf{V}}_{\mathcal{O}_{2}}^{\top}\right)=\lambda_{n} \leq \lambda_{n}^{1-\eta}$. Therefore, $\mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right) \in$ $\mathcal{B}$.

For any other $\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}}\right) \in \mathcal{B}$, denote $\widetilde{\boldsymbol{\Delta}}=\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}+\widetilde{\boldsymbol{\Delta}}_{\mathbf{L}}$, we have

$$
\begin{aligned}
& g_{\gamma}\left(\mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}\right)-\mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}}\right)\right) \\
& =g_{\gamma}\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)}\left[\nabla R_{n}(\boldsymbol{\Delta})-\nabla R_{n}(\widetilde{\boldsymbol{\Delta}})\right], \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)}\left[\nabla R_{n}(\boldsymbol{\Delta})-\nabla R_{n}(\widetilde{\boldsymbol{\Delta}})\right]\right) \\
& =g_{\gamma}\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)}\left[\nabla R_{n}^{2}(\hat{\boldsymbol{\Delta}}) v(\boldsymbol{\Delta}-\widetilde{\boldsymbol{\Delta}})\right], \mathcal{P}_{D\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}\right)}\left[\nabla R_{n}^{2}(\hat{\boldsymbol{\Delta}}) v(\boldsymbol{\Delta}-\widetilde{\boldsymbol{\Delta}})\right]\right) \\
& \lesssim\left\|\nabla R_{n}^{2}(\hat{\boldsymbol{\Delta}})\right\|_{\max }\|\boldsymbol{\Delta}-\widetilde{\boldsymbol{\Delta}}\|_{\max } \\
& \lesssim\left\|\nabla R_{n}^{2}(\hat{\boldsymbol{\Delta}})\right\|_{\max } g_{\gamma}\left(\boldsymbol{\Delta}_{\boldsymbol{\Omega}}-\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \boldsymbol{\Delta}_{\mathbf{L}}-\widetilde{\boldsymbol{\Delta}}_{\mathbf{L}}\right)
\end{aligned}
$$

where the second equality is due to Taylor's expansion. According to (13), with probability approaching $1, \mathbf{C}_{\widehat{\mathbf{U}}_{\mathcal{O}_{2}}}$ is a contraction mapping on $\mathcal{B}$.

Lemma 6. Let $\widehat{\boldsymbol{\Delta}}_{\mathbf{L}}=\mathbf{U}_{1}^{*} \mathbf{D}_{1}^{*}\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right)^{\top}+\left(\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right) \mathbf{D}_{1}^{*}\left(\mathbf{U}_{1}^{*}\right)^{\top}+\mathbf{U}_{1}^{*}\left(\widehat{\mathbf{D}}_{\mathcal{\mathcal { G }}}-\mathbf{D}_{1}^{*}\right)\left(\mathbf{U}_{1}^{*}\right)^{\top}$, then the followings hold:

1. $\widehat{\boldsymbol{\Delta}}_{\mathbf{L}} \in \mathcal{T}\left(\mathbf{L}^{*}\right)$;
2. $\left\|\widehat{\mathbf{L}}_{\mathcal{\mathcal { G }}}-\mathbf{L}^{*}-\widehat{\boldsymbol{\Delta}}_{\mathbf{L}}\right\|_{\max } \lesssim_{P} \lambda_{n}^{2(1-\eta)}$;

3. there exists a constant $c>0$ such that $\left\|\widehat{\mathbf{\Delta}}_{\mathbf{L}}\right\|_{\max }>_{P} c\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }-c \lambda_{n}^{2(1-\eta)}$.

Proof of Lemma 6. The first two results follow directly from Lemma 4 in [9]. For the third one, by the Davis-Kahan theorem [50], we obtain

$$
\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{2} \leq \frac{\left\|\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}-\mathbf{L}^{*}\right\|_{F}}{\min _{1 \leq k \leq K}\left\{\lambda_{k}\left(\mathbf{L}^{*}\right)-\lambda_{k+1}\left(\mathbf{L}^{*}\right)\right\}}
$$

where $\lambda_{k}\left(\mathbf{L}^{*}\right)$ is the $k$-th largest eigenvalues of $\mathbf{L}^{*}$. By Assumption 2, it implies that $\| \widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}-$ $\left.\mathbf{L}^{*}\right\|_{\max }>c\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }$ for a constant $c>0$. Therefore, we obtain $\left\|\widehat{\mathbf{\Delta}}_{\mathbf{L}}\right\|_{\max }>\| \widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}-$ $\left.\mathbf{L}^{*}\right\|_{\max }-\left\|\widehat{\mathbf{L}}_{\widetilde{\mathcal{O}}}-\mathbf{L}^{*}-\widehat{\mathbf{\Delta}}_{\mathbf{L}}\right\|_{\max }>_{P} c\left\|\widehat{\mathbf{U}}_{\mathcal{O}_{2}}-\mathbf{U}_{1}^{*}\right\|_{\max }-c \lambda_{n}^{2(1-\eta)}$, which completes the proof.

Lemma 7. Suppose $\mathbf{A} \in \mathbb{R}^{p \times p}$ is a positive definite matrix with $\Lambda_{\min }(\mathbf{A}) \geq 2 p \epsilon$, and $\mathbf{E} \in \mathbb{R}^{p \times p}$ is a symmetric error matrix with $\|\mathbf{E}\|_{\max } \leq \epsilon$, then $\mathbf{A}+\mathbf{E}$ is invertible and

$$
\left\|(\mathbf{A}+\mathbf{E})^{-1}-\mathbf{A}^{-1}\right\|_{\max } \leq \frac{2 p}{\Lambda_{\min }^{2}(\mathbf{A})} \epsilon
$$

Proof of Lemma 7. Note that Lemma 7 modifies the results in Lemma 5 in [18] and Lemma 29 in [28]. First, to prove that $\mathbf{A}+\mathbf{E}$ is inverible, we note that $\mathbf{A}+\mathbf{E}=\left(\mathbf{I}+\mathbf{E A}^{-1}\right) \mathbf{A}$, and

$$
\left\|\mathbf{E A}^{-1}\right\|_{2} \leq\|\mathbf{E}\|_{2}\left\|\mathbf{A}^{-1}\right\|_{2} \leq p\|\mathbf{E}\|_{\max }\left\|\mathbf{A}^{-1}\right\|_{2} \leq \frac{p}{\Lambda_{\min }(\mathbf{A})} \epsilon \leq \frac{1}{2}
$$

which implies $\mathbf{I}+\mathbf{E A}^{-1}$ is invertible, and thus $\mathbf{A}+\mathbf{E}$ is also invertible.
Moreover, we have

$$
\begin{aligned}
\left\|(\mathbf{A}+\mathbf{E})^{-1}-\mathbf{A}^{-1}\right\|_{\max } & \leq\left\|(\mathbf{A}+\mathbf{E})^{-1}-\mathbf{A}^{-1}\right\|_{2}=\left\|(\mathbf{A}+\mathbf{E})^{-1}(\mathbf{A}+\mathbf{E}-\mathbf{A}) \mathbf{A}^{-1}\right\|_{2} \\
& \leq\left\|(\mathbf{A}+\mathbf{E})^{-1}\right\|_{2}\left\|\mathbf{E A}^{-1}\right\|_{2} \leq \frac{\left\|\mathbf{A}^{-1}\right\|_{2}}{1-\left\|\mathbf{E A}^{-1}\right\|_{2}}\left\|\mathbf{E A}^{-1}\right\|_{2} \\
& \leq 2\left\|\mathbf{A}^{-1}\right\|_{2}\left\|\mathbf{E A}^{-1}\right\|_{2} \leq \frac{2 p}{\Lambda_{\min }^{2}(\mathbf{A})} \epsilon
\end{aligned}
$$

where the third inequality follows the inequality (5.8.2) in [19], and the last inequality follows from (25).

# Supplement: Proof of Propositions 1 and 2 

Proof of Propositions 1. First of all, it can be verified that $\partial_{\boldsymbol{\Omega}} \bar{l}\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)=\partial_{\mathbf{L}} \bar{l}\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)=\mathbf{0}$. By the concavity of $\bar{l}\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$, this implies that $\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ is a maximizer of $\bar{l}\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$.

For any small $\epsilon>0$, let $(\widetilde{\boldsymbol{\Omega}}, \widetilde{\mathbf{L}}) \in \mathcal{O}(\epsilon)$ be a maximizer of $\bar{l}(\boldsymbol{\Omega}, \mathbf{L})$ in the interior of $\mathcal{O}(\epsilon)$. Then, the first order conditions hold:

$$
\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \partial_{\boldsymbol{\Omega}} \bar{l}(\widetilde{\boldsymbol{\Omega}}, \widetilde{\mathbf{L}})=\mathbf{0}, \text { and } \mathcal{P}_{\mathcal{T}(\widetilde{\mathbf{L}})} \partial_{\mathbf{L}} \bar{l}(\widetilde{\boldsymbol{\Omega}}, \widetilde{\mathbf{L}})=\mathbf{0}
$$

Let $\widetilde{\mathbf{L}}=\widetilde{\mathbf{U}}_{1} \widetilde{\mathbf{D}}_{1} \widetilde{\mathbf{U}}_{1}^{\top}$ be the eigen decomposition of $\widetilde{\mathbf{L}}$. Define $\widetilde{\Delta}_{\boldsymbol{\Omega}}=\widetilde{\boldsymbol{\Omega}}-\boldsymbol{\Omega}^{*}, \widetilde{\Delta}_{\mathbf{L}}=\widetilde{\mathbf{L}}-\mathbf{L}^{*}$ and $\widetilde{\Delta}=\widetilde{\Delta}_{\boldsymbol{\Omega}}+\widetilde{\Delta}_{\mathbf{L}}$. Further let $\widetilde{\Delta}_{\mathbf{L}}=\widetilde{\Delta}_{\mathbf{L}, 1}+\widetilde{\Delta}_{\mathbf{L}, 2}$, where

$$
\widetilde{\Delta}_{\mathbf{L}, 1}=\widetilde{\mathbf{U}}_{1} \widetilde{\mathbf{D}}_{1}\left(\widetilde{\mathbf{U}}_{1}-\mathbf{U}_{1}^{*}\right)^{\top}+\left(\widetilde{\mathbf{U}}_{1}-\mathbf{U}_{1}^{*}\right) \widetilde{\mathbf{D}}_{1} \widetilde{\mathbf{U}}_{1}^{\top}+\widetilde{\mathbf{U}}_{1}\left(\widetilde{\mathbf{D}}_{1}-\mathbf{D}_{1}^{*}\right) \widetilde{\mathbf{U}}_{1}^{\top}
$$

It can be verified that $\widetilde{\Delta}_{\mathbf{L}, 1} \in \mathcal{T}(\widetilde{\mathbf{L}})$ and $\left\|\widetilde{\Delta}_{\mathbf{L}, 2}\right\|_{\max } \leq C \epsilon^{2}$ for some constant $C$ [9, Lemma 4].
By Taylor's expansion, we have

$$
\bar{l}\left(\Theta^{*}+\widetilde{\Delta}\right)=\bar{l}\left(\Theta^{*}\right)-\frac{1}{2} v(\widetilde{\Delta})^{\top} \mathcal{I}^{*} v(\widetilde{\Delta})+R(\widetilde{\Delta})
$$

where it can be verified that $\|R(\widetilde{\Delta})\|_{\max }=O\left(\|\widetilde{\Delta}\|_{\max }^{3}\right)$ and $\|\nabla R(\widetilde{\Delta})\|_{\max }=O\left(\|\widetilde{\Delta}\|_{\max }^{2}\right)$. Then,

by (26) and (27), we obtain

$$
\begin{aligned}
& \mathbf{0}=-\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla \bar{l}\left(\boldsymbol{\Theta}^{*}+\widetilde{\boldsymbol{\Delta}}\right)=\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)}\left(\mathcal{I}^{*} v(\widetilde{\boldsymbol{\Delta}})\right)-\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)}(\nabla R(\widetilde{\boldsymbol{\Delta}})) \\
& \mathbf{0}=-\mathcal{P}_{\mathcal{T}(\widetilde{\mathbf{L}})} \nabla \bar{l}\left(\boldsymbol{\Theta}^{*}+\widetilde{\boldsymbol{\Delta}}\right)=\mathcal{P}_{\mathcal{T}(\widetilde{\mathbf{L}})}\left(\mathcal{I}^{*} v(\widetilde{\boldsymbol{\Delta}})\right)-\mathcal{P}_{\mathcal{T}(\widetilde{\mathbf{L}})}(\nabla R(\widetilde{\boldsymbol{\Delta}}))
\end{aligned}
$$

which leads that

$$
F_{\widetilde{\mathbf{U}}_{1}}\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 1}\right)=\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla R(\widetilde{\boldsymbol{\Delta}}), \mathcal{P}_{\mathcal{T}(\widetilde{\mathbf{L}})}\left(\nabla R(\widetilde{\boldsymbol{\Delta}})-\mathcal{I}^{*} v\left(\widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 2}\right)\right)\right)
$$

When $\epsilon$ is sufficiently small, Lemma 1 implies that $F_{\widetilde{\mathbf{U}}_{1}}$ is invertible and $F_{\widetilde{\mathbf{U}}_{1}}^{-1}$ is bounded. Then, we have

$$
\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 1}\right)=-F_{\widetilde{\mathbf{U}}_{1}}^{-1}\left(\mathcal{P}_{\mathcal{S}\left(\boldsymbol{\Omega}^{*}\right)} \nabla R(\widetilde{\boldsymbol{\Delta}}), \mathcal{P}_{\mathcal{T}(\widetilde{\mathbf{L}})}\left(\nabla R(\widetilde{\boldsymbol{\Delta}})-\mathcal{I}^{*} v\left(\widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 2}\right)\right)\right)
$$

By Lemma 1 and the fact that $\|\nabla R(\widetilde{\boldsymbol{\Delta}})\|_{\max }=O\left(\|\widetilde{\boldsymbol{\Delta}}\|_{\max }^{2}\right)=O\left(\left\|\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 1}\right)\right\|_{\max }^{2}+\left\|\widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 2}\right\|_{\max }^{2}\right)$, we have $\left\|\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 1}\right)\right\|_{\max } \leq C\left[\left\|\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 1}\right)\right\|_{\max }^{2}+\left\|\widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 2}\right\|_{\max }\right]$. Then,

$$
\left\|\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 1}\right)\right\|_{\max } \leq C\left\|\widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 2}\right\|_{\max } \leq C \epsilon^{2}
$$

for possibly different constants $C$, which further implies that

$$
\left\|\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}}\right)\right\|_{\max } \leq\left\|\left(\widetilde{\boldsymbol{\Delta}}_{\boldsymbol{\Omega}}, \widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 1}\right)\right\|_{\max }+\left\|\widetilde{\boldsymbol{\Delta}}_{\mathbf{L}, 2}\right\|_{\max } \leq C \epsilon^{2}
$$

and hence that $(\widetilde{\boldsymbol{\Omega}}, \widetilde{\mathbf{L}}) \in \mathcal{O}\left(C \epsilon^{2}\right)$. Then, when $\epsilon$ is sufficiently small, we have $C \epsilon^{2}<\epsilon / 2$, and thus $(\widetilde{\boldsymbol{\Omega}}, \widetilde{\mathbf{L}})$ must be a maximizer of $\bar{l}(\boldsymbol{\Omega}, \mathbf{L})$ in the interior of $\mathcal{O}(\epsilon / 2)$.

Repeating the above derivation implies that $(\widetilde{\boldsymbol{\Omega}}, \widetilde{\mathbf{L}})=\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$. Therefore, $\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ is the unique maximizer of $\bar{l}\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ in the interior of $\mathcal{O}(\epsilon)$, which implies that it is the unique maximizer of $\bar{l}\left(\boldsymbol{\Omega}^{*}, \mathbf{L}^{*}\right)$ in $\mathcal{O}(\epsilon / 2)$. This completes the proof of Proposition 1.

Proof of Proposition 2. We restrict the following analysis on the event $\left\{\widehat{m}=m^{*}\right\} \cap\left\{\widehat{\tau}_{i}=\tau_{i}^{*}\right.$ : $\left.i \in\left[m^{*}\right]\right\}$, which occurs with probability approaching 1 according to Theorem 2. We establish the results by mathematical induction. Specifically, suppose we have correctly determined the first $k$ chain components among $\widehat{\tau}_{i}$ 's, so that $\left(\widehat{\pi}_{1}, \ldots, \widehat{\pi}_{k}\right) \in \Pi_{k}^{*}$, where $\Pi_{k}^{*}$ denotes the set of all possible true causal ordering of the first $k$ chain components among $\tau_{l}^{*}$ 's. Let $\widehat{\mathcal{C}}_{k}=\cup_{s=1}^{k} \widehat{\tau}_{\widehat{\pi}_{s}}$, and we consider two chain components $\widehat{\tau}_{i}$ and $\widehat{\tau}_{j}$ that are not subsets of $\widehat{\mathcal{C}}_{k}$, but $\operatorname{pa}\left(\widehat{\tau}_{j}\right) \subseteq \widehat{\mathcal{C}}_{k}$ and $\operatorname{pa}\left(\widehat{\tau}_{i}\right) \not \subset \widehat{\mathcal{C}}_{k}$. It then suffices to show that $\widehat{\mathcal{D}}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\widehat{\mathcal{D}}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right)>0$.

Simple algebra yields that

$$
\begin{aligned}
& \widehat{\mathcal{D}}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\widehat{\mathcal{D}}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right) \\
= & \left(\mathcal{D}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\mathcal{D}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right)\right)+\left(\widehat{\mathcal{D}}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\mathcal{D}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)\right)+\left(\mathcal{D}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right)-\widehat{\mathcal{D}}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right)\right) \\
\geq & \left(\mathcal{D}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\mathcal{D}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right)\right)-2 \max _{\widehat{\tau}_{i} \nsubseteq \widehat{\mathcal{C}}_{k}}\left|\widehat{\mathcal{D}}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\mathcal{D}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)\right|
\end{aligned}
$$

By Lemma 3, and facts $\widehat{m}=m^{*}$ and $\widehat{\tau}_{i}=\tau_{i}^{*}$ for $i \in\left[m^{*}\right]\}$, we have $\mathcal{D}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right)=0$. Furthermore, there exists a node $l \in \widehat{\tau}_{i}$ such that $\operatorname{pa}(l) \backslash \widehat{\mathcal{C}}_{k} \neq \emptyset$, and thus

$$
\mathcal{D}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right) \geq \sum_{t \in \operatorname{pa}(l) \backslash \widehat{\mathcal{C}}_{k}} \beta_{l t}^{2} \operatorname{Var}\left(x_{t} \mid \mathbf{x}_{\widehat{\mathcal{C}}_{k}}\right)>0
$$

where the first inequality follows from (3) in Lemma 3. Therefore, there exists a positive constant $c$ such that $\mathcal{D}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\mathcal{D}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right) \geq c>0$.

For the second term in (28), let $\boldsymbol{\Sigma}^{*}\left(l, \widehat{\mathcal{C}}_{k}\right)=\boldsymbol{\Sigma}_{l l}^{*}-\boldsymbol{\Sigma}_{l \widehat{\mathcal{C}}_{k}}^{*}\left(\boldsymbol{\Sigma}_{\widehat{\mathcal{C}}_{k} \widehat{\mathcal{C}}_{k}}^{*}\right)^{-1} \boldsymbol{\Sigma}_{\widehat{\mathcal{C}}_{k} l}^{*}$ and $\widehat{\boldsymbol{\Sigma}}\left(l, \widehat{\mathcal{C}}_{k}\right)=\widehat{\boldsymbol{\Sigma}}_{l l}-$ $\widehat{\boldsymbol{\Sigma}}_{l \widehat{\mathcal{C}}_{k}} \widehat{\boldsymbol{\Sigma}}_{\widehat{\mathcal{C}}_{k} \widehat{\mathcal{C}}_{k}}^{-1} \widehat{\boldsymbol{\Sigma}}_{\widehat{\mathcal{C}}_{k} l}$. It holds that

$$
\begin{aligned}
\left|\widehat{\mathcal{D}}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\mathcal{D}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)\right| & =\left|\max _{l \in \widehat{\tau}_{i}}\left\{\widehat{\boldsymbol{\Sigma}}\left(l, \widehat{\mathcal{C}}_{k}\right)-\widehat{\boldsymbol{\Omega}}_{l l}^{-1}\right\}-\max _{l \in \widehat{\tau}_{i}}\left\{\boldsymbol{\Sigma}^{*}\left(l, \widehat{\mathcal{C}}_{k}\right)-\left(\boldsymbol{\Omega}^{*}\right)_{l l}^{-1}\right\}\right| \\
& \leq \max _{l \in \widehat{\tau}_{i}}\left|\left\{\widehat{\boldsymbol{\Sigma}}\left(l, \widehat{\mathcal{C}}_{k}\right)-\widehat{\boldsymbol{\Omega}}_{l l}^{-1}\right\}-\left\{\boldsymbol{\Sigma}^{*}\left(l, \widehat{\mathcal{C}}_{k}\right)-\left(\boldsymbol{\Omega}^{*}\right)_{l l}^{-1}\right\}\right|
\end{aligned}
$$

$$
\leq \max _{l \in \widehat{\tau}_{i}}\left|\widehat{\Sigma}\left(l, \widehat{\mathcal{C}}_{k}\right)-\Sigma^{*}\left(l, \widehat{\mathcal{C}}_{k}\right)\right|+\max _{l \in \widehat{\tau}_{i}}\left|\widehat{\Omega}_{l l}^{-1}-\left(\Omega^{*}\right)_{l l}^{-1}\right|
$$

which converges to 0 in probability by Theorem 2 and $\widehat{\Sigma} \xrightarrow{p r} \Sigma^{*}$. Therefore,

$$
\widehat{\mathcal{D}}\left(\widehat{\tau}_{i}, \widehat{\mathcal{C}}_{k}\right)-\widehat{\mathcal{D}}\left(\widehat{\tau}_{j}, \widehat{\mathcal{C}}_{k}\right)>_{P} 0
$$

As a direct consequence, the selected chain component has to be the one whose parent nodes are contained in $\widehat{\mathcal{C}}_{k}$, and thus $\left(\widehat{\pi}_{1}, \ldots, \widehat{\pi}_{k+1}\right) \in \Pi_{k+1}^{*}$. The desired result then follows from mathematical induction.

# Supplement: Computation details of (6) 

We first replace the positive definite constraint of $\Omega$ in (6) with a slightly stronger constraint $\Omega \succeq$ $\delta \mathbf{I}_{p}$ for some small $\delta>0$ [48], and then the optimization task in (6) becomes

$$
\begin{aligned}
(\widehat{\boldsymbol{\Theta}}, \widehat{\boldsymbol{\Omega}}, \widehat{\mathbf{L}})= & \underset{\boldsymbol{\Theta}, \boldsymbol{\Omega}, \mathbf{L}}{\operatorname{argmin}}-\log \operatorname{det} \boldsymbol{\Theta}+\operatorname{tr}(\boldsymbol{\Theta} \widehat{\boldsymbol{\Sigma}})+\lambda_{n}\left(\|\boldsymbol{\Omega}\|_{1, \text { off }}+\gamma\|\mathbf{L}\|_{*}\right) \\
& \text { such that } \boldsymbol{\Theta}=\boldsymbol{\Omega}+\mathbf{L}, \boldsymbol{\Theta} \succ 0, \boldsymbol{\Omega} \succeq \delta \mathbf{I}_{p}
\end{aligned}
$$

The augmented Lagrangian function of (29) is defined as

$$
\begin{aligned}
L_{\mu}(\boldsymbol{\Theta}, \boldsymbol{\Omega}, \mathbf{L}, \mathbf{U}):= & -\log \operatorname{det} \boldsymbol{\Theta}+\operatorname{tr}(\boldsymbol{\Theta} \widehat{\boldsymbol{\Sigma}})+\lambda_{n}\left(\|\boldsymbol{\Omega}\|_{1, \text { off }}+\gamma\|\mathbf{L}\|_{*}\right) \\
& +\operatorname{tr}(\mathbf{U}(\boldsymbol{\Theta}-\boldsymbol{\Omega}-\mathbf{L}))+\frac{\mu}{2}\|\boldsymbol{\Theta}-\boldsymbol{\Omega}-\mathbf{L}\|_{F}^{2}
\end{aligned}
$$

where $\mathbf{U} \in \mathbb{R}^{p \times p}$ is a dual variable matrix and $\mu>0$ is a penalty parameter. The corresponding dual problem is

$$
\max _{\mathbf{U}} \min _{\boldsymbol{\Theta}>0, \boldsymbol{\Omega} \succeq \delta \mathbf{I}_{p}, \mathbf{L}} L_{\mu}(\boldsymbol{\Theta}, \boldsymbol{\Omega}, \mathbf{L}, \mathbf{U})
$$

It can be solved by the alternative direction method of multipliers (ADMM), consisting of the following iteration steps,

$$
\begin{array}{ll}
\Theta \text {-step: } & \boldsymbol{\Theta}^{k+1}:=\underset{\boldsymbol{\Theta} \succ 0}{\operatorname{argmin}} L_{\mu}\left(\boldsymbol{\Theta}, \boldsymbol{\Omega}^{k}, \mathbf{L}^{k}, \mathbf{U}^{k}\right) \\
\boldsymbol{\Omega} \text {-step: } & \boldsymbol{\Omega}^{k+1}:=\underset{\boldsymbol{\Omega} \succeq \delta \mathbf{I}_{p}}{\operatorname{argmin}} L_{\mu}\left(\boldsymbol{\Theta}^{k+1}, \boldsymbol{\Omega}, \mathbf{L}^{k}, \mathbf{U}^{k}\right) \\
\mathbf{L} \text {-step: } & \mathbf{L}^{k+1}:=\underset{L}{\operatorname{argmin}} L_{\mu}\left(\boldsymbol{\Theta}^{k+1}, \boldsymbol{\Omega}^{k+1}, \mathbf{L}, \mathbf{U}^{k}\right) \\
\mathbf{U} \text {-step: } & \mathbf{U}^{k+1}:=\mathbf{U}^{k}+\mu\left(\boldsymbol{\Theta}^{k+1}-\boldsymbol{\Omega}^{k+1}-\mathbf{L}^{k+1}\right)
\end{array}
$$

For the $\Theta$-step, we follow the similar procedure in [49], leading to the explicit of (31),

$$
\Theta^{k+1}=\frac{\mathbf{R}_{1}^{k}+\sqrt{\left(\mathbf{R}_{1}^{k}\right)^{2}+4 \mu \mathbf{I}_{p}}}{2 \mu}
$$

where $\mathbf{R}_{1}^{k}=\mu\left(\boldsymbol{\Omega}^{k}+\mathbf{L}^{k}\right)-\widehat{\boldsymbol{\Sigma}}-\mathbf{U}^{k}$ and $\sqrt{\mathbf{A}}$ denotes the square root of a symmetric positive definite matrix $\mathbf{A}$.

For the $\Omega$-step, the sub-optimization problem in (32) can be re-formulated as

$$
\begin{aligned}
\boldsymbol{\Omega}^{k+1} & =\underset{\boldsymbol{\Omega} \succeq \delta \mathbf{I}_{p}}{\operatorname{argmin}} \lambda_{n}\|\boldsymbol{\Omega}\|_{1, \text { off }}+\operatorname{tr}\left(\mathbf{U}^{k}\left(\boldsymbol{\Theta}^{k+1}-\boldsymbol{\Omega}-\mathbf{L}^{k}\right)\right)+\frac{\mu}{2}\left\|\boldsymbol{\Theta}^{k+1}-\boldsymbol{\Omega}-\mathbf{L}^{k}\right\|_{F}^{2} \\
& =\underset{\boldsymbol{\Omega} \succeq \delta \mathbf{I}_{p}}{\operatorname{argmin}} \frac{\lambda_{n}}{\mu}\|\boldsymbol{\Omega}\|_{1, \text { off }}+\frac{1}{2}\left\|\boldsymbol{\Omega}-\mathbf{R}_{2}^{k}\right\|_{F}^{2}
\end{aligned}
$$

where $\mathbf{R}_{2}^{k}=\boldsymbol{\Theta}^{k+1}-\mathbf{L}^{k}+\mu^{-1} \mathbf{U}^{k}$. Similar as [48], we introduce a new variable $\boldsymbol{\Phi} \in \mathbb{R}^{p \times p}$, and

thus

$$
\begin{aligned}
\left(\boldsymbol{\Phi}^{k+1}, \boldsymbol{\Omega}^{k+1}\right)= & \underset{\boldsymbol{\Phi}, \boldsymbol{\Omega}}{\operatorname{argmin}} \frac{\lambda_{n}}{\mu}\|\boldsymbol{\Omega}\|_{1, \text { off }}+\frac{1}{2}\left\|\boldsymbol{\Omega}-\mathbf{R}_{2}^{k}\right\|_{F}^{2} \\
& \text { s.t. } \boldsymbol{\Phi}=\boldsymbol{\Omega}, \boldsymbol{\Phi} \succeq \delta \mathbf{I}_{p}
\end{aligned}
$$

The augmented Lagrangian function of (36) is defined as

$$
L_{\rho}(\boldsymbol{\Phi}, \boldsymbol{\Omega}, \mathbf{V}):=\frac{\lambda_{n}}{\mu}\|\boldsymbol{\Omega}\|_{1, \text { off }}+\frac{1}{2}\left\|\boldsymbol{\Omega}-\mathbf{R}_{2}^{k}\right\|_{F}^{2}+\operatorname{tr}(\mathbf{V}(\boldsymbol{\Phi}-\boldsymbol{\Omega}))+\frac{\rho}{2}\|\boldsymbol{\Phi}-\boldsymbol{\Omega}\|_{F}^{2}
$$

where $\mathbf{V} \in \mathbb{R}^{p \times p}$ is a dual variable matrix and $\rho>0$ is a penalty parameter. We also employ ADMM to solve (36), which consists of the following iterations,

$$
\begin{aligned}
\boldsymbol{\Phi}^{l+1} & :=\underset{\boldsymbol{\Phi} \succeq \delta \mathbf{I}_{p}}{\operatorname{argmin}} L_{\rho}\left(\boldsymbol{\Phi}, \boldsymbol{\Omega}^{l}, \mathbf{V}^{l}\right) \\
\boldsymbol{\Omega}^{l+1} & :=\underset{\boldsymbol{\Omega}}{\operatorname{argmin}} L_{\rho}\left(\boldsymbol{\Phi}^{l+1}, \boldsymbol{\Omega}, \mathbf{V}^{l}\right) \\
\mathbf{V}^{l+1} & :=\mathbf{V}^{l}+\rho\left(\boldsymbol{\Phi}^{l+1}-\boldsymbol{\Omega}^{l+1}\right)
\end{aligned}
$$

Here, (37) can be solved as

$$
\begin{aligned}
\boldsymbol{\Phi}^{l+1} & =\underset{\boldsymbol{\Phi} \succeq \delta \mathbf{I}_{p}}{\operatorname{argmin}} \operatorname{tr}\left(\mathbf{V}^{l}\left(\boldsymbol{\Phi}-\boldsymbol{\Omega}^{l}\right)\right)+\frac{\rho}{2}\left\|\boldsymbol{\Phi}-\boldsymbol{\Omega}^{l}\right\|_{F}^{2} \\
& =\underset{\boldsymbol{\Phi} \succeq \delta \mathbf{I}_{p}}{\operatorname{argmin}}\left\|\boldsymbol{\Phi}-\left(\boldsymbol{\Omega}^{l}-\rho^{-1} \mathbf{V}^{l}\right)\right\|_{F}^{2}=\left(\boldsymbol{\Omega}^{l}-\rho^{-1} \mathbf{V}^{l}\right)_{+}
\end{aligned}
$$

where $(\mathbf{A})_{+}$denotes the projection of a matrix $\mathbf{A}$ onto the convex cone $\left\{\boldsymbol{\Phi} \succeq \delta \mathbf{I}_{p}\right\}$. Specifically, if the eigen decomposition of $\mathbf{A}$ is $\sum_{j=1}^{p} s_{j} \mathbf{v}_{j} \mathbf{v}_{j}^{T}$, then $(\mathbf{A})_{+}=\sum_{j=1}^{p} \max \left(s_{j}, \delta\right) \mathbf{v}_{j} \mathbf{v}_{j}^{T}$. Furthermore, (38) can be solved as

$$
\boldsymbol{\Omega}^{l+1}=\underset{\boldsymbol{\Omega}}{\operatorname{argmin}} \frac{\lambda_{n}}{\mu}\|\boldsymbol{\Omega}\|_{1, \text { off }}+\frac{1}{2}\left\|\boldsymbol{\Omega}-\mathbf{R}_{2}^{k}\right\|_{F}^{2}+\operatorname{tr}\left(\mathbf{V}\left(\boldsymbol{\Phi}^{l+1}-\boldsymbol{\Omega}\right)\right)+\frac{\rho}{2}\left\|\boldsymbol{\Phi}^{l+1}-\boldsymbol{\Omega}\right\|_{F}^{2}
$$

$$
\begin{aligned}
& =\underset{\boldsymbol{\Omega}}{\operatorname{argmin}} \frac{\lambda_{n}}{\mu(1+\rho)}\|\boldsymbol{\Omega}\|_{1, \text { off }}+\frac{1}{2}\left\|\boldsymbol{\Omega}-\frac{\mathbf{R}_{2}^{k}+\mathbf{V}^{l}+\rho \boldsymbol{\Phi}^{l+1}}{1+\rho}\right\|_{F}^{2} \\
& =\frac{1}{1+\rho} \mathcal{S}_{\frac{\lambda_{n}}{\mu}}\left(\mathbf{R}_{2}^{k}+\mathbf{V}^{l}+\rho \boldsymbol{\Phi}^{l+1}\right)
\end{aligned}
$$

where $\mathcal{S}_{\tau}(\mathbf{A})=\left(s_{\tau}\left(A_{i j}\right)\right)_{i j} \in \mathbb{R}^{p \times p}$, and $s_{\tau}\left(A_{i j}\right)=\operatorname{sign}\left(A_{i j}\right) \max \left(\left|A_{i j}\right|-\tau, 0\right) \mathbf{1}(i \neq j)+A_{i j} \mathbf{1}(i=$ $j)$ denotes entry-wise soft-thresholding operator for off-diagonal entries of $\mathbf{A}$.

For the L-step, it follows from Theorem 2.1 in [4] that

$$
\begin{aligned}
\mathbf{L}^{k+1} & =\underset{\mathbf{L}}{\operatorname{argmin}} \lambda_{n} \gamma\|\mathbf{L}\|_{*}+\operatorname{tr}\left(\mathbf{U}^{k}\left(\boldsymbol{\Theta}^{k+1}-\boldsymbol{\Omega}^{k+1}-\mathbf{L}\right)\right)+\frac{\mu}{2}\left\|\boldsymbol{\Theta}^{k+1}-\boldsymbol{\Omega}^{k+1}-\mathbf{L}\right\|_{F}^{2} \\
& =\underset{\mathbf{L}}{\operatorname{argmin}} \frac{\lambda_{n} \gamma}{\mu}\|\mathbf{L}\|_{*}+\frac{1}{2}\left\|\mathbf{L}-\left(\boldsymbol{\Theta}^{k+1}-\boldsymbol{\Omega}^{k+1}+\mu^{-1} \mathbf{U}^{k}\right)\right\|_{F}^{2} \\
& =\mathcal{T}_{\frac{\lambda_{n} \gamma}{\mu}}\left(\boldsymbol{\Theta}^{k+1}-\boldsymbol{\Omega}^{k+1}+\mu^{-1} \mathbf{U}^{k}\right)
\end{aligned}
$$

where $\mathcal{T}_{\tau}(\mathbf{A})$ denotes the singular value shrinkage operator for a matrix $\mathbf{A}$. Specifically, if the SVD of $\mathbf{A}$ with rank $r$ is $\sum_{j=1}^{p} d_{j} \mathbf{u}_{j} \mathbf{v}_{j}^{T}$, then $\mathcal{T}_{\tau}(\mathbf{A})=\sum_{j=1}^{r} \max \left(d_{j}-\tau, 0\right) \mathbf{u}_{j} \mathbf{v}_{j}^{T}$.
