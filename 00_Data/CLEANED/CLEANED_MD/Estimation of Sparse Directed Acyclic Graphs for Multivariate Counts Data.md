# HHS Public Access 

Author manuscript
Biometrics. Author manuscript; available in PMC 2016 September 07.
Published in final edited form as:
Biometrics. 2016 September ; 72(3): 791-803. doi:10.1111/biom. 12467.

## Estimation of Sparse Directed Acyclic Graphs for Multivariate Counts Data

Sung Won Han and<br>Division of Biostatistics, School of Medicine, New York University, 650 First Avenue, Room 577, New York, NY, 10016

## Hua Zhong

Division of Biostatistics, School of Medicine, New York University, 650 First Avenue, Room 512, New York, NY, 10016

Sung Won Han: SungWon.Han@nyumc.org; Hua Zhong: judy.zhong@nyumc.org

## Summary

The next-generation sequencing data, called high throughput sequencing data, are recorded as count data, which is generally far from normal distribution. Under the assumption that the count data follow the Poisson log-normal distribution, this paper provides an $L_{1}$-penalized likelihood framework and an efficient search algorithm to estimate the structure of sparse directed acyclic graphs (DAGs) for multivariate counts data. In searching for the solution, we use iterative optimization procedures to estimate the adjacency matrix and the variance matrix of the latent variables. The simulation result shows that our proposed method outperforms the approach which assumes multivariate normal distributions, and the log-transformation approach. It also shows that the proposed method outperforms the rank-based PC method under sparse network or hub network structures. As a real data example, we demonstrate the efficiency of the proposed method in estimating the gene regulatory networks of the ovarian cancer study.

## Keywords

Bayesian network; Count data; Directed acyclic graph; Lasso estimation; Penalized likelihood estimation; Unknown variable ordering

## 1. Introduction

Probabilistic graphical models are often used to find conditional dependencies between expression levels of different genes in regulatory networks or pathways (Friedman, Hastie, and Tibshirani, 2008). Gaussian graphical models have been commonly used to infer gene networks since gene expression data from microarray technology can be approximated by normal distribution after log transformation. However, recently, the next-generation

[^0]
[^0]:    6. Supplementary Materials

    Web Appendices including mathematical derivation, algorithm descriptions, tables, and figures referenced in Sections 2, 3, and 4 are available with this paper at the Biometrics website on Wiley Online Library. The R code for the plnDAG method is available on the journal website as supplementary material codes.

sequencing technology, which is also called high throughput sequencing, has been applied for measuring gene expressions and monitoring genome-wide transcription (Marioni et al. 2008). The data for each gene from the next-generation sequencing are counts based on sequencing reads. Such count data have been approximated as Poisson distribution or negative binomial distribution (Srivastava and Chen, 2010; Anders and Huber, 2010). However, the statistical analysis of multivariate counts data has proved difficult due to insufficient parametric class representing correlation structures (Aitchison and Ho, 1989).

Most literature on the graphical model, either an undirected graph or a directed graph, is based on Gaussian distribution. Undirected graph models imply full conditional independence graphs, where an edge between two nodes is absent if and only if the corresponding random variables are conditionally independent (Lauritzen, 1996; Hastie, Tibshirani, and Friedman, 2009). Such dependency is obtained by a nonzero element in the inverse covariance matrix for Gaussian variables. A graphical lasso algorithm is a popular method for the sparse inverse covariance estimation (Friedman, Hastie, and Tibshirani, 2008). If the number of variables is larger than the sample size, several penalized methods have been proposed to estimate the inverse covariance matrix.

Directed acyclic graphs (DAGs) are a special class of directed graphical models, where all the edges are directed edges and contain no directed cycles (Pearl, 2000). A connection in DAGs can be made from a causal inference by applying the directed Markov property under certain assumptions (Pearl, 2000; Friedman, Hastie, and Tibshirani, 2008). Estimation of the structure of DAGs from observed data has been studied by many groups (for review, see Neapolitan (2004); Daly, Shen, and Aitken (2011)). The most common way to estimate the structure of DAGs is a score-and-search approach, in which a network is identified by maximizing a certain objective function (Neapolitan, 2004), and often heuristic search algorithms are developed to find a high score (Daly, Shen, and Aitken, 2011). Other approaches to estimate the structure of DAGs are the constraint-based approach such as the PC-algorithm (Spirtes, Glymour, and Scheines, 2000), which uses statistical tests to find conditional independence of data, or the hybrid approach, which combines the score-and-search approach and the constraint-based approach to make a computationally competitive algorithm in high-dimensional settings. To estimate the DAG under known variable order in high dimensional data, the L_{1}-penalized likelihood approach was first studied by Shojaie and Michailidis (2010). The likelihood was formulated as a function of the adjacency matrix of the graph, and it is converted to separable lasso problems (Shojaie and Michailidis, 2010), which resulted in an efficient algorithm to estimate the structure of directed graphs. Fu and Zhou (2013) proposed an L_{1}-penalized likelihood approach to estimate sparse DAG structures with experimental intervention. The proposed objective function has a log term, which causes non-convexity. Han et al. (2014) used an approximated convex objective function based on the L_{1}-penalized likelihood to estimate DAGs given an unknown order of variables.

Unlike Gaussian distribution, a graphical model under count data is rarely studied even though the next-generation sequencing technology generates more precise data with count values. Allen and Liu (2013) propose a local Poisson graphical model, which is essentially a neighbor selection algorithm to find the undirected graph. Choi et al. (2013) proposed the

undirected graphical model based on Poisson distribution. For estimating DAGs of non-normal data, Harris and Drton (2013) proposed the Rank-based PC-algorithm (RPC), which uses nonparametric rank correlation coefficients.

In this paper, we propose an L_{1}-penalized likelihood approach based on multivariate Poisson log-normal distributions to estimate DAGs for multivariate count data. An efficient solution search algorithm is proposed to estimate the DAG by optimizing a lasso-based objective function within feasible computational time for high dimensional data. To the best of our knowledge, this is the first method that estimates DAGs for multivariate count data based on L1-penalized likelihood without knowing variable orders. Here, the variable orders indicate directional causal relationships between variables. The organization of this paper is as follows. In Section 2, we define the model formulation and derive the objective function by approximation, and discuss iterative optimization algorithms to estimate DAGs under unknown variable order. In Section 3, we investigate the performance of the proposed method by simulation studies. The real data application is studied in Section 4, and we conclude our results in Section 5.

## 2. Mathematical Formulation

In this section, we explain the multivariate Poisson log-normal model for count data, and the objective function based on the penalized likelihood followed by iterative optimization algorithms.

### 2.1 Multivariate Poisson log-normal model

Suppose that we have p random variables, Y_{1}, Y_{2}, Y_{3}, ..., Y_{p}. Let Y be a vector with p random variables, say Y = [Y_{1}, Y_{2}, ..., Y_{p}]^{T}. Y_{k} (k = 1, 2, ..., p) follows a Poisson distribution Poisson(φ_{k}), where φ_{k} follows a log-normal distribution for k = 1, 2, ..., p, such that

log (φ k) = σ k X k + μ k .

X = [X_{1}, X_{2}, ..., X_{p}]^{T} follows a multivariate-normal distribution MN(0, Σ_{X}). Only Y_{k} (k = 1, 2, ..., p) is observed, while X_{k} is the underlying hidden variable.

The likelihood can be represented by

P (Y | μ, σ, ∑ X ) = ∫ P (Y , X | μ, σ, ∑ X ) d X = ∫ P (Y | X , μ, σ) × P (X | ∑ X ) d X .

Define y_{jk} as the j_{th} realization of Y_{k}, and define the data matrix y = [y_{jk}], where j = 1, 2, ..., n, and k = 1, 2, ..., p. y_{j} is the column vector of the j_{th} row of y. The term in (2), P(Y;X, μ, σ), can be extended by independence of Y_{k} given X. Thus,

$$
\sum_{j=1}^{n} \sum_{k=1}^{p} \log P\left(y_{j k} \mid X_{k}, \mu, \sigma\right)=\sum_{j=1}^{n} \sum_{k=1}^{p}\left[C_{j k} X_{k}+F_{j k}-\exp \left(\sigma_{k} X_{k}+\mu_{k}\right)\right]
$$

where $C_{j k}=y_{j k} \sigma_{k}$ and $F_{k j}=y_{j k} \mu_{k}-\log \left(y_{j k}!\right) . y_{j k}!$ means $y_{j k} \times\left(y_{j k}-1\right) \times \cdots \times 2 \times 1$.
Parameters $\mu_{k}$ and $\sigma_{k}^{2}$ can be estimated by the marginal expectation and variance of $Y_{k}$. After we define the sample mean $\bar{y}_{k}=\sum_{j=1}^{n} y_{j k} / n$ and the sample variance
$\hat{\sigma}_{y_{k}}^{2}=\sum_{j=1}^{n}\left(y_{j k}-\bar{y}_{k}\right)^{2} / n, \hat{\mu_{k}}$ and $\hat{\sigma}_{k}^{2}$ can be obtained by methods of moments,

$$
\hat{\sigma}_{k}^{2}=\log \left[\frac{\hat{\sigma}_{y_{k}}^{2}-\bar{y}_{k}}{\bar{y}_{k}^{2}}+1\right]
$$

and

$$
\hat{\mu}_{k}=\log \bar{y}_{k}-\frac{1}{2} \hat{\sigma}_{k}^{2}
$$

Note that the multivariate Poisson log-normal model allows an unequal mean and variance of $Y_{k}$, which is more flexible than a simple Poisson distribution.

Equation (2) shows that the likelihood of $\mathbf{Y}$ is defined by two parts: the likelihood of $y_{j}$ given the latent variable $X$, and the likelihood of $X$ with covariance matrix $\Sigma_{X}$. In the next section, we use Linear Structural Equations to model the DAG structures on latent variable $\mathbf{X}$.

# 2.2 Linear structural equations regarding hidden variable $X$ 

To obtain the relationships among $Y_{1}$ to $Y_{K}$, we define the graphical relationship from the hidden variable $\mathbf{X}$. The variable and underlying causal relation can be represented by graph $G=(V, E)$, where $V$ indicates the node set and $E$ indicates the edge set represented by $V \times$ $V$. We assume that the graph $G$ is a DAG, so $(i, j)$ is not in $E$ if $(j, i)$ belongs to $E$. In the underlying relationship, $j$ is denoted as a parent if $i \leftarrow j$, and the set of parent nodes for a child node $i$ is represented by $p a_{i}$. The structural equation model (Pearl, 2000) explains the underlying causal relationship of random variables in a DAG. Let $\Gamma=\left[\Gamma_{1}, \Gamma_{2}, \ldots, \Gamma_{p}\right]^{T}$ be a vector of latent variables, which is not observed but assumed to follow a normal distribution as

$$
\Gamma \sim M N(0, D)
$$

where $D$ is a diagonal matrix with the entries $\sigma_{1}^{2}, \sigma_{1}^{2}, \ldots, \sigma_{1_{p}}^{2}$. We assume that the variances may be unequal and unknown. The structural equation model for the underlying relation in the graph is

$$
X_{i}=\sum_{j \in p a_{i}} a_{i j} X_{j}+\Gamma_{i}
$$

where $a_{i j}$ is a direct underlying causal effect from a parent $j$ to a child $i$. We can represent Equation (5) by the matrix form $\mathbf{X}=A \mathbf{X}+\Gamma$, where $\mathbf{X}=\left[X_{1}, X_{2}, \ldots, X_{p}\right]^{T}$, and $A$ is the adjacency matrix by

$$
A=\left(\begin{array}{ccccc}
0 & a_{12} & \cdots & a_{1(p-1)} & a_{1 p} \\
a_{21} & 0 & \cdots & a_{2(p-1)} & a_{2 p} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{(p-1) 1} & a_{(p-1) 2} & \cdots & 0 & a_{(p-1) p} \\
a_{p 1} & a_{p 2} & \cdots & a_{p(p-1)} & 0
\end{array}\right)
$$

The form in (5) can be a compact form expressed by $\mathbf{X}=(I-A)^{-1} \Gamma$. Thus, $\mathbf{X}$ is a vector of multivariate normal variables with $E[\mathbf{X}]=0$ and $\operatorname{Var}[\mathbf{X}]=(I-A)^{-1} D\left((I-A)^{-1}\right)^{T}$. In other words, $\mathbf{X}$ follows the multivariate normal distribution $M N\left(0, \Sigma_{\mathbf{X}}\right)$, where
$\sum_{\mathbf{x}}^{-1}=(I-A)^{T} D^{-1}(I-A)$. The log-likelihood of $A$ and $D$ can therefore be expressed by

$$
-\frac{n}{2} \log P(\mathbf{X} \mid A, D) \propto \frac{1}{2} \log \left|D^{-1}\right|-\frac{1}{2} \mathbf{X}^{T}(I-A)^{T} D^{-1}(I-A) \mathbf{X}
$$

Apparently, we can learn the structure of the graph $G$ by estimating the adjacency matrix $A$. For directed graphs, $A$ is not symmetric since $A_{i j}$ and $A_{j i}$ represent the edge from node $X_{j}$ to $X_{i}$ and the edge from node $X_{i}$ to $X_{j}$ in $G$, respectively. In fact, if the underlying graph $G$ is a DAG, $A_{i j}$ and $A_{j i}$ cannot both be non-zero. Therefore, there needs to be acyclic restrictions on the structure of the adjacency matrix $A$ of a DAG.

Let $T_{A}$ denote the structure matrix induced by $A$, where the $(i, j)_{t h}$ entry of $T_{A}$ is 1 if $A_{i j} \neq 0$. The following lemma proposed in Han et al. (2014) conveniently establishes the relationship between $A$ and the acyclic restriction.

Lemma 1-The adjacency matrix A is acyclic if and only if

$$
\sum_{l=1}^{\min \left(\operatorname{Card}\left(T_{A}\right), p\right)} \sum_{m=1}^{p}\left[T_{A}^{l}\right]_{m, m}=0
$$

where $\min ()$ means a minimum value function, and $\operatorname{Card}\left(T_{A}\right)$ is the number of non-zero entries indicating a cardinality of $T_{A} . T_{A}^{l}$ indicates $l$ times the product of $T_{A}$ matrix, and $\left[T_{A}^{l}\right]_{m, m}$ indicates the $(m, m)$ entry of the matrix $T_{A}^{l}$.

For many applications, it is often the case that the underlying DAG structure is sparse. It is therefore important to find a sparse structure for the adjacency matrix $A$. Therefore, the estimation of DAGs can be pursued by minimizing the penalized likelihood function in terms of $A$ under the acyclic restriction of the structure matrix, $T_{A}$, as follows.

$$
\begin{array}{cc}
\min _{A} & -\frac{n}{2} \log P(\mathbf{X} \mid A, D)+\lambda(A) \\
\text { s.t. } & T_{A} \text { satisfies the acyclic constraint (7), }
\end{array}
$$

where $\lambda(A)$ is a penalty function.
The recent work of Shojaie and Michailidis (2010) assumed a known ordering of the variables to simplify the optimization, which eliminates the need for the acyclicity constraint. The computation for optimizing function (8) without assuming known variable orders is challenging because it is a mixed integer nonlinear optimization problem with the acyclicity constraint. Fu and Zhou (2013) proposed a heuristic algorithm based on a coordinate descent search approach. Han et al. (2014) proposed a meta-heuristic search algorithm, called the Discrete Improving Search with a TABU (DIST) algorithm, and they presented its effectiveness and computational efficiency.

# 2.3 Penalized likelihood and iterative optimization 

Based on the log-likelihood $\ell(A, D \mid \mathbf{y}_{j}, \mu, \sigma)$ for each $\mathbf{y}_{j}$, we define the objective function as the lasso penalized log-likelihood of $A$ in terms of the observation matrix $y$, which is

$$
S(A, D \mid y, \mu, \sigma, \lambda) \equiv-\frac{2}{n} \sum_{j=1}^{n} \ell\left(A, D \mid \mathbf{y}_{j}, \mu, \sigma\right)+\lambda|A|
$$

where $\lambda$ is a penalty parameter, and $/ A /$ is the $L_{1}$-norm defined as $/ A /=\Sigma_{i} \Sigma_{j} / A_{i j} /$. By replacing $\mu$ and $\sigma$ with their marginal estimates $\hat{\mu}$ in (3) and $\hat{\sigma}$ in (4), the problem is essentially to minimize Equation (9) with respect to $A$ and the nuisance parameter $D$ under the acyclic constraint (7). The log-likelihood of the observed data can be represented by the log-likelihood of the complete data as

$$
-\frac{2}{n} \sum_{j=1}^{n} \ell\left(A, D \mid \mathbf{y}_{j}, \hat{\mu}, \hat{\sigma}\right)=-\frac{2}{n} \sum_{j=1}^{n} \log \int \exp \left[\ell\left(A, D \mid \mathbf{y}_{j}, \mathbf{X}, \hat{\mu}, \hat{\sigma}\right)\right] d \mathbf{X}
$$

However, $\int \exp (\hat{k} A, D / y_{j}, \mathbf{X}, \hat{\mu}, \hat{\sigma}) d \mathbf{X}$ in Equation (10) does not have a closed form, which makes the minimization problem much more challenging. We propose a second order Laplace integral approximation of $S(A, D / y, \hat{\mu}, \hat{\sigma}, \lambda)$ into a function with a closed form, $S(A$, $D / y, \hat{\chi}, \hat{\mu}, \hat{\sigma}, \lambda)$, which is defined as

$$
\begin{aligned}
& S(A, D \mid y, \hat{\chi}, \hat{\mu}, \hat{\sigma}, \lambda) \equiv-\frac{2}{n} \sum_{j=1}^{n}\left[\frac{1}{2} \log \left|D^{-1}\right|-\frac{1}{2} \hat{\chi}_{j}^{T}(I-A)^{T} D^{-1}(I-A) \hat{\chi}_{j}\right] \\
& -\frac{2}{n} \sum_{j=1}^{n}\left[-\frac{p}{2} \log (2 \pi)\right] \\
& +-\frac{2}{n} \sum_{j=1}^{n} \sum_{k=1}^{p}\left[C_{j k} \hat{\chi}_{j k}+F_{j k}-\exp \left(\hat{\sigma}_{k} \hat{\chi}_{j k}+\hat{\mu}_{k}\right)\right] \\
& +\frac{1}{n} \sum_{j=1}^{n} \log \left|(I-A)^{T} D^{-1}(I-A)+\operatorname{diag}_{k=1}^{p}\left(\hat{\sigma}_{k}^{2} \exp \left(\hat{\sigma}_{k} \hat{\chi}_{j k}+\hat{\mu}_{k}\right)\right|\right. \\
& +\lambda|A|
\end{aligned}
$$

where $\hat{\chi}_{j}=\arg \max _{\mathbf{X}} \log P\left(\mathbf{X}, \mathbf{y}_{j} / A, D, \hat{\mu}, \hat{\sigma}\right)$, and $\hat{\chi}$ is the $n \times p$ matrix defined as $\hat{\chi}=[\hat{\chi}_{1}$, $\hat{\chi}_{2}, \hat{\chi}_{3}, \ldots, \hat{\chi}_{n}]^{T} \hat{\chi}_{j k}$ is the $(j, k)$ entry of $\hat{\chi}$ matrix. By introducing the intermediate estimated variable $\hat{\chi}$, the objective function $S(A, D / y, \hat{\chi}, \mu, \sigma, \lambda)$ has a closed form. The details are in Web Appendix A of Supplementary Materials.

Based on the Laplace approximation, we propose an iterative optimization procedure to minimize the objective function by iteratively estimating $\hat{\chi}, A$, and $D$ until $\hat{\chi}$ converges. We iterate two steps: estimating $\hat{\chi}$ at fixed $A$ and $D$, and minimizing the penalized loglikelihood objective function over the two parameters $A$ and $D$ respectively given the estimated $\hat{\chi}$. The details of the algorithm are outlined below.

We first estimate $\hat{\chi}$ by maximizing the log-likelihood of the complete data over $\mathbf{X}$ at each iteration $t$ given $\hat{A}^{(t)}$ and $\hat{D}^{(t)}$, which is

$$
\hat{\chi}_{j}^{(t)}=\arg \max _{\mathbf{X}} \log P\left(\mathbf{X}, \mathbf{y}_{j} \mid \hat{A}^{(t)}, \hat{D}^{(t)}, \hat{\mu}, \hat{\sigma}\right)
$$

As discussed in the previous two sections, $\log P\left(\mathbf{X}, \mathbf{y}_{j} / \hat{A}^{(t)}, \hat{D}^{(t)}, \hat{\mu}, \hat{\sigma}\right)$ can be decomposed into $\log P\left(\mathbf{y}_{j} / \mathbf{X}, \mu, \sigma\right)+\log P(\mathbf{X} / A, D)$, the sum of log-likelihood of $y_{j}$ given latent variable $\mathbf{X}$, and the log-likelihood of $\mathbf{X}$ under the DAG adjacency matrix $A$ and variance matrix $D$. As further detailed in Web Appendix B of Web-based Supplementary Materials,
$\hat{\chi}_{j}^{(t)}=\arg \max _{\mathbf{X}}\left[-\frac{1}{2} \mathbf{X}^{T}\left(I-\hat{A}^{(t)}\right)^{T}\left(\hat{D}^{(t)}\right)^{-1}\left(I-\hat{A}^{(t)}\right) \mathbf{X}+\mathbf{X}^{T} C_{j}-\exp (\hat{\mu})^{T} \exp (\hat{\sigma} * \mathbf{X})\right]$,
where * indicates an element-by-element multiplication. Maximizing Equation (13) is a separate optimization problem in terms of $j$. Maximizing Equation (13) can be achieved by a

gradient search algorithm such as a quasi-Newton method with box constraints of a lower and upper bound (Byrd et al., 1995). We use the function optint) in R package.

We then minimize the objective function $S\left(A, \hat{D}^{(t)} \underline{b} ; \chi^{2} \underline{b}, \hat{\mu}_{k}, \hat{\sigma}_{k}, \lambda\right)$ with respect to the parameter matrix $A$ given $\chi^{2} \underline{b}$. Note that this minimization is subject to the acyclic restriction of the structure matrix $T_{A}$.

$$
\begin{aligned}
\hat{A}^{(t+1)} & =\operatorname{argmin}_{A} S\left(A, \hat{D}^{(t)} \mid y, \hat{\chi}^{(t)}, \hat{\mu}_{k}, \hat{\sigma}_{k}, \lambda\right) \\
& \text { s.t. } T_{\lambda}^{(t+1)} \text { satisfies the acyclic constraint (7). }
\end{aligned}
$$

As detailed in Supplementary Materials (Web Appendix A), $S\left(A, \hat{D}^{(t)} \underline{b} ; \chi^{2} \underline{b}, \hat{\mu}_{k}, \hat{\sigma}_{k}, \lambda\right)$ can be further approximated by

$$
\begin{aligned}
& S\left(A, \hat{D}^{(t)} \mid y, \hat{\chi}^{(t)}, \hat{\mu}_{k}, \hat{\sigma}_{k}, \lambda\right) \propto \frac{1}{n} \sum_{k=1}^{p}\left\|\hat{\chi}_{k}^{(t)}-\hat{\chi}^{(t)} \mathbf{a}_{k}\right\|_{2}^{2} \\
& +\frac{1}{n\left(\hat{\sigma}_{1, i}^{2}\right)^{(t)}} \sum_{k=1}^{p}\left\|g_{k}-g \mathbf{a}_{k}\right\|_{2}^{2} \\
& +\lambda \sum_{i} \sum_{j}\left|a_{i j}\right| \\
& -\frac{2}{n} \sum_{j=1}^{n} \sum_{k=1}^{p} Q\left(\hat{\chi}_{j k}^{(k)}, y_{j k}, \widehat{\mu_{k}}, \widehat{\sigma_{k}}\right)
\end{aligned}
$$

where $\mathbf{a}_{k}$ is a coefficient vector, $\left[a_{k 1}, a_{k 2}, \ldots, a_{k(p-1)}, a_{k p}\right]^{T}$, which is a column vector representing a $k^{\text {th }}$ row in A matrix. $g$ is the matrix of $\left[g_{j k}\right]$ with $\frac{1}{\sigma_{j k}}=\sigma_{k} \exp \left\{\left(\sigma_{k} \hat{\chi}_{j k}+\mu_{k}\right) / 2\right\}$, and $g_{k}$ is the $k_{t h}$ column vector of $g . Q\left(\chi_{j k}, y_{j k}, \mu_{k}, \sigma_{k}\right)$ is a term independent of $A$, defined by

$$
Q\left(\hat{\chi}_{j k}, y_{j k}, \mu_{k}, \sigma_{k}\right)=y_{j k} \sigma_{k} \hat{\chi}_{j k}+y_{j k} \mu_{k}-\log \left(y_{j k}!\right)-\exp \left(\sigma_{k} \hat{\chi}_{j k}+\mu_{k}\right)-\log \left(\sigma_{k}\right)-\frac{\sigma_{k} \hat{\chi}_{j k}+\mu_{k}}{2}
$$

Minimizing Equation (15) becomes separable lasso problems in terms of $k$.
This problem of minimizing function (15) with the acyclic constraint (7) is very similar to the optimization of function (8). We propose to use the DIST algorithm detailed in Han et al. (2014) and in Web Appendix B of Web-based Supplementary Materials. Last, we update $\hat{D}^{(t+1)}$ by

$$
\hat{D}^{(t+1)}=\operatorname{diag}\left[\sum_{j=1}^{n} \frac{1}{n}\left(I-\hat{A}^{(t+1)}\right) \hat{\chi}_{j}^{(t)}\left(\left(I-\hat{A}^{(t+1)}\right) \hat{\chi}_{j}^{(t)}\right)^{T}\right]
$$

The description of the complete algorithm referred to as Poisson Log-Normal DAG estimation (plnDAG) is shown in Figure 1. For the initial step, we set $A^{(0)}=0, D^{(0)}=I$, and $\hat{\chi}^{(0)}=\left[\hat{\chi}_{1}^{(0)}, \hat{\chi}_{2}^{(0)}, \ldots, \hat{\chi}_{n}^{(0)}\right]^{T}$ such that $\hat{\chi}_{j k}^{(0)}$, which is the $k^{t h}$ entry of $\hat{\chi}_{j}^{(0)}$, is a standardized value from $\frac{\log \chi_{j k}-\rho_{k}}{\sigma_{k}}$. The iterative optimization steps estimate $A, D$, and $\chi$ repeatedly numerically until $\left\|\chi^{2 t)}-x^{2 t+1}\right\|<\delta$, or we stop the algorithm at a certain step $\kappa$. The essence of the proposed algorithm is similar to the Expectation Conditional Maximization (ECM) algorithm, which can be viewed as a joint maximization method for the objective function over the parameters and latent variables by fixing one argument and maximizing over the others (Neal and Hinton, 1999; Hastie, Tibshirani, and Friedman, 2009).

For some joint distributions, there exist possibly many factorizations of the likelihood function (10). Those DAGs encode the same set of joint distributions, called an equivalence class. Equivalent DAGs cannot be distinguished from observational data. The equivalence class can be described by a completed partially directed acyclic graph (cpDAG) (Chickering, 1995, 2002), which has the following properties: every directed edge exists in all DAGs of the equivalence class, and for every undirected edge $X_{i}-X_{j}$, there exists a DAG with $X_{i} \rightarrow$ $X_{j}$ and a DAG with $X_{i} \leftarrow X_{j}$ in the equivalence class. Chickering $(1995,2002)$ discussed an algorithm to extend a DAG to a cpDAG by identifying the reversible edges in the DAG estimate. We can also apply the algorithm on $D A G_{A}$ to obtain $c p D A G_{A}$. This step is implemented by essentialGraph function of R package ggm (Chickering, 1995, 2002).

# 2.4 Selection of the penalty parameter 

For a pre-determined integer $K$, one can employ a $K$-fold cross-validation (CV) method to select the best tuning parameter in the proposed plnDAG model by criteria such as minimizing the prediction error or the Bayesian information criterion (BIC) (Rothman et al., 2008; Yuan and Lin, 2007). This is sometimes computationally expensive for highdimensional count data. Meinshausen and Buhlmann (2006) proposed an $\alpha$-based $\lambda$, $\lambda_{\alpha}=\frac{2 \delta \chi_{k}}{\sqrt{n}}\left[1-\Phi^{-1}\left(\frac{\alpha}{2 p \alpha}\right)\right]$, where $\Phi^{-1}()$ is the cumulative distribution function of $N(0,1)$, to control the error rate $\alpha$ of the neighborhood estimation with computational simplicity. Shojaie and Michailidis (2010) demonstrated the asymptotic consistency for $\lambda_{k}(\alpha)=\frac{2 \delta \chi_{k}}{\sqrt{n}}\left[1-\Phi^{-1}\left(\frac{\alpha}{2 p(k-1)}\right)\right]$. Here, we adopt a similarly defined $\alpha$-based $\lambda$ as

$$
\lambda_{k}(\alpha)=\frac{2}{\sqrt{n}}\left[1-\Phi^{-1}\left(\frac{\alpha}{2 p(p-1)}\right)\right]
$$

3. Simulation Study

In this section, we discuss the simulation study for the proposed algorithm, plnDAG, and compare it with other existing methods. We consider various simulation scenarios in terms of dimension-to-sample size ratio, network topological structure, and density. Edges are created according to either a random topological structure or a hub topological structure (Margolin et al. 2006). In a random network, edges are randomly created so that each node is equally likely to be connected to any other node. In a hub network, edges are created from a small number of hub nodes to their child nodes. The hub network structure mimics many real biological networks where only a small number of nodes are regulators and each of them has many targets to regulate (Margolin et al. 2006). To create a hub network, we first pick a certain proportion P_{h} of nodes to be hub nodes (parents' nodes), then simulate edges from the selected hub node to multiple child nodes. We explored P_{h} = 20% and 10%. We use the number of variables, p = 200, and the sample size n = 100 for the scenario of n < p and n = 400 for the scenario of n > p. The density of the graph is defined by d, which indicates the average number of parents per child. We use d = 1 or d = 2, and the edges are distributed randomly. For the connectivity of graphs, we control the minimum number of parents for each child by 1 and the maximum number by 3. For the existing edge (i, j), the value of a_{i,j} in matrix A is set at 0.8. The latent variables Γ_{k}'s are generated from independent standard normal distributions. The multivariate normal distributions with variables, X_{1}, ..., X_{p}, are generated from the linear structural equations of (5). Then, to generate Poisson data based on (1), we set μ_{k} = μ and σ_{k} = σ for k = 1, 2, ..., p. Based on gene expressions in ovarian cancer discussed later, the scatter plot of $\hat{\mu}$'s and $\hat{\sigma}$'s is in Web Appendix H of Web-based Supplementary Materials. The scatter plot, which is fitted by a smoothing spline, shows a decreasing trend of σ as μ increases. We select μ =2, 5, and 8, and we select σ which is on the fitted line or maximum σ given μ. Thus, we can investigate the performance in the case of average variability and large variability given each μ. The combinations of (μ, σ) are (2,1.2), (2,2), (5,0.7), (5,1.5), (8,0.5), and (8,1.5). We use 20 replications for each scenario, and for the stopping rule in the plnDAG method, we use δ = 10^{-9} and κ = 15.

We adopt Receiver Operating Characteristic (ROC) curves to examine the true and false positive rates (TPR and FPR) plotted across a range of λ(α) values. TPR is calculated by $\frac{\text{TP}}{\text{TP}} \text{,}$ where TP (True Positive) is the number of correctly detected edges regardless of directionality, and TE is the number of true edges simulated in the DAG. FPR is calculated by $\frac{\text{FP}}{\text{TP}(\mu - \text{TP}) \cdot \text{TP}} \text{,}$ where FP (False Positive) is the number of edges detected by mistake. In addition, we calculate the False Discovery Rate (FDR) as 1 - TP/EE, where EE is the number of all estimated edges. In addition, we consider directed TP(dTP) as detected edges with correctly estimated directions; and directed FDR as dFDR = 1 -dTP/EE. Therefore, for a cpDAG estimate, correctly detected directions, undecided directions, or reversely detected directions are counted as TPs if the true edge is estimated, but only correctly detected directions are counted as dTPs. These two sets of metrics can comprehensively assess the performance of each method with respect to edge detections and direction detections.

3.1 Comparison of the plnDAG method with the alternative approaches

We apply the plnDAG method following Section 2.3, and compare its performance with the performance of three alternative methods. The first approach is to directly apply the L_{1}-penalized likelihood framework assuming multivariate normal distribution, referred to as a like-norm approach. The second comparison method is to first log-transform the count data, then apply the L_{1}-penalized likelihood model assuming multivariate normal distribution to the transformed data. We refer to it as a like-log approach. Note that log-transformation is a widely applied approach for multivariate count data. For both approaches, to find the solution to minimize the L_{1}-penalized likelihood objective function under a multivariate normal distribution, we use the DIST search algorithm by Han et al. (2014), which shows improvements in performances over the coordinate descent search algorithm (Fu and Zhou, 2013). The DIST algorithm is also used to estimate Equation (14) in the proposed plnDAG algorithm. As the same optimization algorithm is used to optimize Equation (14), the differences in simulation performances can be attributed to the model difference. The third approach is the RPC-algorithm by Harris and Drton (2013), which incorporates rank-based correlations with the PC-algorithm.

To investigate the performance of the plnDAG method with other methods, we show the ROC curves for μ=5 when p=200 and n=100 (n < p) and p=200 and n=400 (n > p) in Figures 2 and 3, respectively. The ROC curves for μ=2 or μ=8 show similar patterns, which are in web Appendix C of Supplementary Materials.

We first compare the plnDAG method (solid black line) with the like-norm approach (solid gray line) which assumes multivariate normal distribution. For the count data with small σ/μ ratios such as (μ, σ)=(5,0.7), the ROC curves between the plnDAG and the like-norm approaches are relatively close. However, the performance difference is clearly shown as σ/μ ratios increase, where the count data deviate more from normal distributions. The TPRs and dTPRs of the like-norm approach are much lower than those of the plnDAG method for all scenarios. Similar patterns are also shown in the scenarios of μ=2 and μ=8 in Web Appendix C of Supplementary Materials. Under the scenarios of μ = 5, the like-log approach (dashed black line), which assumes multivariate normal distribution of the log transformed data, showed performances close to those of the plnDAG methods for sparse networks. When the underlying graphs get less sparse, the performance difference between the two methods increases. The plnDAG showed higher TPRs and dTPRs especially for random structures and for directed edge detections. The performance difference between the plnDAG method and the rank-based RPC method (dashed gray line) depends on network structures and sparsity. Under the random network structure, the plnDAG method showed better or close performances for sparse networks, but was out-performed by the RPC method for dense networks. However, the performance of the RPC method is negatively impacted under hub network structures, and the impact is more severe as more edges are concentrated around a smaller number of hub nodes (i.e. from random networks to hub networks (Ph=10%)). The decrease in performance is also more severe in small sample sizes (e.g. n = 100 than n = 400). The PC-like approaches, such as the RPC method, utilize a universal threshold on the conditional independence tests to control sparsity on a whole view. For hub networks with unbalanced edge distributions, this universal sparsity control approach might generate an

overly-sparse estimate around the hub nodes. On the other hand, the penalized likelihood based objective function is more flexible, so it generates more robust performance with respect to the underlying random or hub network structure.

To estimate DAGs, the plnDAG method estimates $\hat{\mu}$ and $\hat{\sigma}$ first in Equations (3) and (4), then plugs the estimates into the objective function $S(A, D \underline{y}, \hat{\mu}, \hat{\sigma}, \lambda)$. To investigate the effect of the plug-in approach, we compared its performance to that of the plnDAG method with $S(A$, $D \underline{y}, \mu, \sigma, \lambda)$ where the Poisson parameters $\mu$ and $\sigma$ are from the true values in simulations. The ROC curves of the two approaches are in Web Appendix D of Supplementary Materials. As the curves show, the performances are almost identical. We also compared the values of the objective function $S(A, D \underline{y}, \hat{\mu}, \hat{\sigma}, \lambda)$ estimated by the second order Laplace integral approximation in Equation (11) with its values estimated by numerical calculation in simulations for $p=5$ (Web Appendix E of Supplementary Materials). As shown, the ratios between the values obtained from the two approaches from all simulations with various parameters are randomly distributed around 1 and bounded between $95 \%$ to $110 \%$. Therefore, we believe the approximation performs reasonably well and enables the algorithm to be computed much faster.

The computational time of the plnDAG is very efficient and feasible. Table 1 shows the computational time of the three methods based on all cases of $d, \mu$, and $\sigma$. Note that the computational time of the RPC method is small for sparse networks when $d=1$, but significantly increases as the network gets dense when $\mathrm{d}=2$; while the plnDAG is reasonably fast for all scenarios.

# 3.2 Performance of the plnDAG 

To investigate the performance of the plnDAG method, we first examine its performance as a function of the $\lambda(a)$. For this purpose, we showed the Matthew's correlation coefficient (MCC) of the plnDAG along a range of $\lambda(a)$ (Web Appendix F of Supplementary Materials). The above simulation results suggest that the performance of the plnDAG method is not very sensitive to the choice of $a$ as long as $a$ is in a reasonable range; however, a value of $a=0.1$ seems to deliver more reliable estimates for most simulated scenarios.

Table 2 summarizes the average performance and CPU time of the plnDAG method at $\lambda(a=$ 0.1 ) over 20 replicates for each combination of network density, $\mu, \sigma$, and the number of nodes ( $\mathrm{p}=200$ or 500 ) when $\mathrm{d}=1$ and $\mathrm{n}=100$. The summary table for $\mathrm{n}=400$ is in Web Appendix G of Supplementary Materials. Results in the tables suggest that the plnDAG method can efficiently estimate DAGs with reasonable performance accuracy and running time even for high dimensional sparse networks ( $p=500$ and $n=100$ or 400). Under the sparse network, most FDRs are controlled below $10 \%$, and dFDRs are controlled below $30 \%$.

## 4. Application

We applied the plnDAG algorithm to derive the gene networks in a dataset of 265 ovarian adenocarcinomas tumor samples (The Cancer Genome Atlas Research Network, 2011),

obtained from TCGA (http://tcga - data.nci.nih.gov/docs/publications/ov2011). The goal of our application is to find regulatory relationships among genes, that is, to determine which are the regulators (Transcription Factor encoding genes) and which are the regulated target encoding genes, through the analysis of mRNA expression data obtained by the level 3 data with RNASeqV2 platform that contains normalized count data. Several papers in the literature have found a list of genes, which have important roles in ovarian cancer growth or treatment. Bolton et al. (2012) has studied candidate genes related to ovarian cancers for several decades with respect to biological pathways. The list of 38 important candidate genes is shown in Web Appendix H of Supplementary Materials.

The gene-gene interaction networks provided in NetBox (http://cbio.mskcc.org/tools/netbox/index.html), which extracts the information of gene interaction from four curated data sources: Human Protein Reference Database (Keshava Prasad et al. 2009), Reactome (Joshi-Tope et al. 2005; Matthews et al. 2009), NCI-Nature Pathway Interaction Database (Schaefer et al. 2009), and MSKCC Cancer Cell Map (http://www.mskcc.org/) were used as the basis to evaluate the performance of the plnDAG algorithm.

After we estimate the network, we check how many edges are overlapped with the previously found interactions. Since there may be undetected interactions at a current stage in this area, we calculate how many edges among those detected from the plnDAG method, the like-log approach, the like-norm approach, or the RPC method are overlapped with the known interactions. Figure (a) shows true positive rate (TPR*) and false positive rate (FPR*) based on known interactions. TPR* is defined by DE/KE, and FPR* is defined by (EE-DE)/ (p(p-1)/2-KE), where DE is the number of detected edges (overlapped with known interactions), KE is the number of known interactions, and EE is the number of total estimated edges. The range of x-axis (FPR*) in the plot is from about a half of the number of genes to the triple of it. As the plot shows, the plnDAG method has more overlapped edges than the other methods given the same number of estimated edges. The estimated network by the plnDAG with the penalty parameter selected by the formula in (16) is shown in Figure (b). The nodes are colored based on their functional roles. The edges that are overlapped with the known interactions are colored in red. The overlapped edges are in the edges among the genes functioning in DNA repair (BRCA1, BRCA2, BRIP1), FOXM1 signaling (PLK1, CCNB1, AURKB, BIRC5, CDC25B, FOXM1, and ATR), steroid hormone (ESR1), and therapeutic target gene (CCNE1). In addition, the tumor suppressor (TP53) and the cell cycle control gene (CREBBP) are also overlapped.

## 5. Conclusion and Discussion

This paper discusses how to estimate the structure of directed acyclic graphs under the count data. We provide the L_{1}-penalized likelihood model based on the Poisson log-normal distribution under the assumption that the variances of latent variables are unknown, and variable ordering is unknown. The observed data are assumed to be compounded Poisson data, but the underlying variables follow multivariate normal distributions based on the coefficient matrix. We also propose an efficient solution search algorithm based on iterative optimization steps. The coefficient matrix is estimated by separable lasso problems, and the

unobserved data parameters of the normal distribution are estimated by separate optimization problems.

The simulation result shows that our proposed method outperforms the approach based on the assumption of the normal distribution in most cases. It also performs better than or as well as the data transformed approach. The proposed method performs better than the rankbased PC method under the sparse network or hub network. Overall, our proposed method is robust against the network structure, the variability of the data, and dimensionality (dimension-to-sample size ratio) with good performance. We also discuss how to apply it to the gene expression data in ovarian cancer. It is the first method to explore DAGs for multivariate count data, and it is efficient and achieves satisfactory performance.

It is not straightforward to find the asymptotic property in the plnDAG algorithm because $A$ is not identifiable. Shojaie and Michailidis (2010) discussed variable selection consistency of DAGs with the $L_{1}$-penalized likelihood under normal distribution in sparse network when the variable order is known. Fu and Zhou (2013) studied the model selection consistency when the variable order is unknown but the data have experimental interventions. Chickering (2002) mentioned that searching for solutions within the same equivalence class requires additional computational time, so searching for solutions among equivalence classes is efficient. If two graphs are under the same equivalence class, the objective function values based on the $L_{1}$-penalized likelihood are same. The plnDAG algorithm incorporating the DIST algorithm improves the objective function value at each iteration, so score equivalence does not affect the computational time much.

# Supplementary Material 

Refer to Web version on PubMed Central for supplementary material.

## Acknowledgments

Research is supported by NIH-1-R21 GM110450-01.
