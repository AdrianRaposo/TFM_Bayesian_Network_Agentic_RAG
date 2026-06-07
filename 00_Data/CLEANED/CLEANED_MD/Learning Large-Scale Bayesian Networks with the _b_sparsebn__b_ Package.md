# Learning Large-Scale Bayesian Networks with the sparsebn Package 

Bryon Aragam<br>University of Chicago

Jiaying Gu<br>University of California, Los Angeles

Qing Zhou<br>University of California, Los Angeles


#### Abstract

Learning graphical models from data is an important problem with wide applications, ranging from genomics to the social sciences. Nowadays datasets often have upwards of thousands - sometimes tens or hundreds of thousands - of variables and far fewer samples. To meet this challenge, we have developed a new R package called sparsebn for learning the structure of large, sparse graphical models with a focus on Bayesian networks. While there are many existing software packages for this task, this package focuses on the unique setting of learning large networks from high-dimensional data, possibly with interventions. As such, the methods provided place a premium on scalability and consistency in a high-dimensional setting. Furthermore, in the presence of interventions, the methods implemented here achieve the goal of learning a causal network from data. Additionally, the sparsebn package is fully compatible with existing software packages for network analysis.


Keywords: Bayesian networks, causal networks, graphical models, machine learning, structural equation modeling, multi-logit regression, experimental data.

## 1. Introduction

Graphical models are a popular tool in machine learning and statistics, and have been used in a variety of applications including genetics (Gao and Cui 2015; Isci, Dogan, Ozturk, and Otu 2014), computational biology (Jones, Buchan, Cozzetto, and Pontil 2012), oncology (Chen et al. 2015), medicine and health care (Nicholson, Cozman, Velikova, Van Scheltinga, Lucas, and Spaanderman 2014), logistics (Garvey, Carnovale, and Yeniyurt 2015), finance (Sanford and Moosa 2012), and even software testing (Dejaeger, Verbraken, and Baesens 2013). The widespread growth of high-dimensional biological data in particular has spurred a renewed interest in the use of graphical models to aid in the discovery of novel biological

mechanisms (Bühlmann, Kalisch, and Meier 2014). While the past decade has witnessed tremendous developments towards understanding undirected graphical models (Meinshausen and Bühlmann 2006; Ravikumar, Wainwright, and Lafferty 2010; Yang, Ravikumar, Allen, and Liu 2015), there has been less progress towards understanding directed graphical models - also known as Bayesian networks (BNs) or structural equation models (SEM) - for highdimensional data with $p \gg n$. A BN is represented by a directed acyclic graph (DAG), whose structure contains a richer and different set of conditional independence relations than an undirected graph. Moreover, DAGs are commonly used in causal inference where the direction of an edge encodes causality. Consequently, there have been continuing efforts in structure learning of directed graphs from data.
Unlike their undirected counterparts, however, the structure learning problem for directed graphical models is complicated by the nonconvexity, nonsmoothness, and nonidentifiability of the underlying statistical problem. These issues have no doubt slowed progress towards fast, scalable algorithms for learning in the presence of thousands - let alone tens of thousands - of variables. Despite progress at the theoretical (Van de Geer and Bühlmann 2013; Aragam, Amini, and Zhou 2015) and computational level (Schmidt, Niculescu-Mizil, and Murphy 2007; Xiang and Kim 2013; Fu and Zhou 2013), there is still a lack of user-friendly software for putting these modern tools into the hands of practitioners.
To bridge this gap we have developed sparsebn, a new R (R Core Team 2019) package for structure learning and parameter estimation of large-scale Bayesian networks from highdimensional data. When experimental data are available, an estimated DAG from this package has a natural causal interpretation. While there are many R packages for learning Bayesian networks (Section 2.4), none that we are aware of are specifically tailored to highdimensional data with experimental interventions. The sparsebn package has been developed from the ground up using recent developments in structure learning (Fu and Zhou 2013; Aragam and Zhou 2015; Gu, Fu, and Zhou 2018) and statistical optimization (Friedman, Hastie, Höfling, and Tibshirani 2007; Friedman, Hastie, and Tibshirani 2010; Mazumder, Friedman, and Hastie 2011). In addition to methods for learning Bayesian networks, this package also includes procedures for learning undirected graphs, fitting structural equation models, and is compatible with existing packages in R. All of the code for this package is open-source and available through the Comprehensive R Archive Network (CRAN) at http://CRAN.R-project.org/package=sparsebn.
To briefly illustrate the use of sparsebn, the code below learns the structure of the pathfinder network (Heckerman, Horvitz, and Nathwani 1992):

```
R> library("sparsebn")
R> data("pathfinder")
R> data <- sparsebnData(pathfinder$data, type = "continuous")
R> dags <- estimate.dag(data)
R> plotDAG(dags)
```

This code estimates a solution path with 16 total estimates (see Section 3.2) and takes approximately one second to run. The first four estimated networks with an increasing number of edges are shown in Figure 1. This example is explored in more detail in Section 6.2.

![img-0.jpeg](img-0.jpeg)

Figure 1: Example output from learning the pathfinder network. To save space, only the first four nontrivial estimates are shown here out of the 16 total estimates in the full solution path.

# 2. Learning Bayesian networks from data 

We begin by reviewing the necessary background and definitions, and then discuss the existing literature and methods.

### 2.1. Background

The basic model we work with is a $p$-dimensional random vector $X=\left(X_{1}, \ldots, X_{p}\right)$ with joint distribution $\mathrm{P}\left(X_{1}, \ldots, X_{p}\right)$. Bayesian networks are directed graphical models whose edges encode conditional independence constraints implied by the joint distribution of $X$. For continuous data, we assume that $X$ follows a multivariate Gaussian distribution; for discrete data we assume each $X_{j}$ is a factor with $r_{j}$ levels. We do not consider so-called hybrid Bayesian networks that allow for graphs with both continuous and discrete nodes, although this is an interesting future direction for this package.
The general theory of Bayesian networks is quite intricate, and we will make no attempt to cover it in detail here. The interested reader is referred to one of the many excellent textbooks on this subject: Koller and Friedman (2009); Spirtes, Glymour, and Scheines (2000); Lauritzen (1996).

Formally, a Bayesian network is defined as a directed acyclic graph $G=(V, E)$ that satisfies the following factorization condition with respect to the joint distribution of $X$ :

$$
\mathrm{P}\left(X_{1}, \ldots, X_{p}\right)=\prod_{j=1}^{p} \mathrm{P}\left(X_{j} \mid \operatorname{pa}\left(X_{j}\right), \theta_{j}\right)
$$

Here, $\operatorname{pa}\left(X_{j}\right)=\left\{X_{i}: X_{i} \rightarrow X_{j} \in E\right\}$ is the parent set of $X_{j}$ and $\theta_{j}$ encodes the parameters that define the conditional probability distribution (CPD) for $X_{j}$.
Traditional methods for learning Bayesian networks start with this definition and develop algorithms from a graph-theoretic perspective (Spirtes and Glymour 1991). This approach comes with restrictive assumptions such as strong faithfulness (Uhler, Raskutti, Bühlmann, and Yu 2013; Zhang and Spirtes 2002), which hinders their use in practice. To motivate our work, we adopt a more general approach to Bayesian networks via structural equation models. In this approach, we start by directly modeling each $\operatorname{CPD} \mathrm{P}\left(X_{j} \mid \operatorname{pa}\left(X_{j}\right), \theta_{j}\right)$ via a generalized linear model. We will consider two special cases: Gaussian CPDs for continuous data and multi-logit CPDs for discrete data. This approach also fits naturally our framework for learning causal networks discussed in Section 2.2.

# Continuous data 

Suppose that for each $j=1, \ldots, p$ there exists $\beta_{j}=\left(\beta_{1 j}, \ldots, \beta_{p j}\right) \in \mathbb{R}^{p}$ such that

$$
X_{j}=\beta_{j}^{\top} X+\varepsilon_{j}
$$

where $\beta_{j j}=0$ (to avoid trivialities) and $\varepsilon_{j} \sim \mathcal{N}\left(0, \omega_{j}^{2}\right)$. By writing $B=\left[\beta_{1}|\cdots| \beta_{p}\right] \in \mathbb{R}^{p \times p}$ and $\varepsilon=\left(\varepsilon_{1}, \ldots, \varepsilon_{p}\right) \in \mathbb{R}^{p}$, we can rewrite Equation 1 as a matrix equation:

$$
X=B^{\top} X+\varepsilon
$$

The model (2) is called a structural equation model for $X$. The matrix $B$ defines the weighted adjacency matrix of a directed graph which, when acyclic, is also a BN for $X$. Note that to estimate $B$ from data it is not enough to simply regress $X_{j}$ onto the rest of variables this leads to the so-called neighbourhood regression estimator of the Gaussian graphical model introduced in Meinshausen and Bühlmann (2006). The problem with this approach is that there is no guarantee that the resulting adjacency matrix will be acyclic. In order to produce a BN, we must constrain $B$ to be acyclic, which couples the parameters of each CPD to one another and induces a nonconvex constraint during the learning phase. For this reason, learning directed graphs is substantially more difficult than learning undirected graphs.
By writing $\Omega=\operatorname{COV}(\varepsilon)$, we see that the parameters $(B, \Omega)$ specify a unique normal distribution $\mathcal{N}(0, \Sigma)$ for $X$. In fact, a little algebra on Equation 2 shows that

$$
\Sigma=(I-B)^{-\top} \Omega(I-B)^{-1}
$$

This gives a way to compute $\Sigma$ from $(B, \Omega)$, and suggests a way to estimate the covariance matrix by setting $\widehat{\Sigma}=(I-\widehat{B})^{-\top} \widehat{\Omega}(I-\widehat{B})^{-1}$. By taking $\Gamma=\Sigma^{-1}$, we obtain an alternative estimator of the Gaussian graphical model, given by

$$
\widehat{\Gamma}=(I-\widehat{B}) \widehat{\Omega}^{-1}(I-\widehat{B})^{\top}
$$

This idea was first explored by Rütimann and Bühlmann (2009) using the PC algorithm (Section 2.3), and a similar idea using our methods is implemented in sparsebn. In many situations, the DAG representation $(B, \Omega)$ encodes more conditional independence relations than the inverse covariance matrix $\Gamma$, which is one of the motivations for learning DAGs from observational data.

# Discrete data 

In a discrete Bayesian network, each $X_{j}$ is a finite random variable with $r_{j}$ states. Instead of a traditional product multinomial model, sparsebn uses a multi-logit model for discrete data. One of the advantages of this approach is a significant reduction in the number of parameters, and recent work suggests that this model serves as a good approximation to the product multinomial model (Gu et al. 2018). Here, we briefly introduce the multi-logit model, and describe how it is used for structure learning.
We use a standard form of the multi-logit model in which each variable $X_{j}$ is encoded by $d_{j}=r_{j}-1$ dummy variables (Dobson and Barnett 2008). More specifically, given a reference category (which may be arbitrary), the $r_{j}$ possible values of $X_{j}$ are encoded by a vector of dummy variables $\mathbf{z}_{j}=\left(z_{j k}, k=1, \ldots, d_{j}\right) \in\{0,1\}^{d_{j}}$. Let $I(\cdot)$ denote the usual indicator function, so that e.g., $I\left(X_{j}=k\right)=1$ if $X_{j}=k$ and $I\left(X_{j}=k\right)=0$ otherwise. If we choose the last category as the reference, then $z_{j k}=I\left(X_{j}=k\right)$ for $k=1, \ldots, d_{j}$ so that the reference category is coded as $\mathbf{z}_{j}=\mathbf{0}$.
Under this parametrization, the conditional distributions take the form

$$
\mathrm{P}\left(X_{j}=u \mid \operatorname{pa}\left(X_{j}\right)\right)=\frac{\exp \left(\beta_{0 u j}+\sum_{i \in \mathrm{pa}\left(X_{j}\right)} \mathbf{z}_{i}^{\top} \boldsymbol{\beta}_{i u j}\right)}{\sum_{m=1}^{r_{j}} \exp \left(\beta_{0 u j}+\sum_{i \in \mathrm{pa}\left(X_{j}\right)} \mathbf{z}_{i}^{\top} \boldsymbol{\beta}_{i m j}\right)}, u=1, \ldots, r_{j}
$$

where $\boldsymbol{\beta}_{i u j} \in \mathbb{R}^{d_{i}}$ is the coefficient vector for variable $X_{i}$ to predict the $u$ th level of $X_{j}$ with intercept $\beta_{0 u j}$. In this model, if $X_{i} \notin \mathrm{pa}\left(X_{j}\right)$ then we have equivalently $\boldsymbol{\beta}_{i u j}=\mathbf{0}$ for all $u$. Let $\boldsymbol{\beta}_{i j}=\left(\boldsymbol{\beta}_{i 1 j}, \ldots, \boldsymbol{\beta}_{i r_{j} j}\right) \in \mathbb{R}^{d_{i} r_{j}}$ be the coefficient vector for edge $i$ to $j$. Therefore, by estimating $\boldsymbol{\beta}_{i j}$, we can infer the structure of a network. If $\boldsymbol{\beta}_{i j}=\mathbf{0}$, there does not exist an edge from $X_{i}$ to $X_{j}$. For more details on this model, see Gu et al. (2018).

### 2.2. Causal DAG learning from interventions

DAGs are a popular model for causal networks, particularly when combined with experimental interventions in addition to observational data (Pearl 2000). Cooper and Yoo (1999); Meganck, Leray, and Manderick (2006); Ellis and Wong (2008) proposed methods to learn causal networks with a mixture of observational and experimental data, and Peér, Regev, Elidan, and Friedman (2001); Pournara and Wernisch (2004) inferred gene networks with perturbed expression data. Each of the methods in sparsebn can take experimental data as input in order to learn the precise causal relationships in a system.
The following simple example illustrates how interventions can be used for learning causal relations: Assume the true causal graph is $\mathcal{G}^{*}: X_{1} \rightarrow X_{2}$, i.e., $X_{1}$ is a direct cause of $X_{2}$. This is observationally equivalent to the graph $\mathcal{G}: X_{1} \leftarrow X_{2}$ - we cannot distinguish between these two graphs using observational data alone. Instead, by manipulating $X_{2}$ experimentally and fixing its value, we can "cut off" the edge from $X_{1}$ to $X_{2}$ since the value of $X_{2}$ would no longer be associated with (i.e., is independent of) $X_{1}$. This is an example of an experimental

intervention. In doing so, the joint distribution factors as $\mathrm{P}\left(X_{1}\right) \mathrm{P}\left(X_{2}\right)$. Instead, if we manipulated $X_{1}$, the relation between $X_{1}$ and $X_{2}$ would stay the same, and the joint distribution factors as $\mathrm{P}\left(X_{1}\right) \mathrm{P}\left(X_{2} \mid X_{1}\right)$. By exploiting these interventions, it is possible to uncover the true causal structure in a physical system.
To see how this can be applied in a statistical setting, we now show how a general form of the density function for experimental data can be derived from the pure observational joint density function. Let $\mathcal{M} \subset\{1, \ldots, p\}$ be the set of variables under intervention, so the joint probability decomposes as

$$
\mathrm{P}\left(X_{1}, \ldots, X_{p}\right)=\prod_{i \notin \mathcal{M}} \mathrm{P}\left(X_{i} \mid \operatorname{pa}\left(X_{i}\right)\right) \prod_{i \in \mathcal{M}} \mathrm{P}\left(X_{i} \mid \bullet\right)
$$

where $\mathrm{P}\left(X_{i} \mid \bullet\right)$ is the marginal distribution of $X_{i}$ from which experimental samples are drawn. Thus, experimental data sets generated from the true DAG $\mathcal{G}$ can be considered as data sets generated from a DAG $\mathcal{G}^{\prime}$, where $\mathcal{G}^{\prime}$ is obtained by removing all directed edges in $\mathcal{G}$ pointing to the variables under intervention. Furthermore, we can see that when $\mathcal{M}=\emptyset$, Equation 6 is the density function for observational data. For more details regarding causal DAG learning, please refer to Pearl (2000) and the references therein.

# 2.3. Previous work 

The various algorithms in the literature for structure learning of Bayesian networks fall into three main categories: constraint-based methods, score-based methods and hybrid methods.

## Constraint-based methods

Constraint-based methods rely on repeated conditional independence tests in order to learn the structure of a network. The main idea is to determine which edges cannot exist in a DAG using statistical tests of independence, a procedure which is justified whenever the so-called faithfulness assumption holds. These algorithms first use independence tests to learn the skeleton of the network, and then orient $v$-structures along with the rest of the edges. Because of the existence of Markov equivalent DAGs, the direction of some edges may not be decided (for details, see e.g., Koller and Friedman 2009). The PC algorithm proposed by Spirtes and Glymour (1991) is a well-known example of this kind of method. Another example is the Fast Causal Inference (FCI) algorithm (Spirtes et al. 2000; Colombo, Maathuis, Kalisch, and Richardson 2012), which allows for latent variables in the network. The output of these algorithms is a partially directed graph, which means that there may be some undirected edges in the estimated graph. While the PC algorithm is a powerful method to learn Bayesian networks in low-dimensions with $n$ very large, the performance of the PC algorithm is less competitive in high-dimensions compared to recent score-based methods (Aragam and Zhou 2015).

## Score-based methods

Score-based methods rely on scoring functions such as the log-likelihood or some other loss function. The goal of these algorithms is to find a DAG that optimizes a given scoring function. Some popular scoring functions include several Bayesian Dirichlet metrics (Buntine 1991; Cooper and Herskovits 1992; Heckerman, Geiger, and Chickering 1995), Bayesian information criterion (Chickering and Heckerman 1997), minimum description length (Bouckaert 1993;

Suzuki 1993; Lam and Bacchus 1994), and entropy (Herskovits and Cooper 1990). One of the classic score-based methods is the greedy hill climbing (HC) algorithm (Russell and Norvig 1995). This algorithm is fast but tends to predict too many edges in high-dimensional settings. For discrete networks, the K2 algorithm (Cooper and Herskovits 1992) is another popular method, however, this method requires prior knowledge about the ordering of the network which is often unavailable in applications. There are also Monte Carlo methods (Ellis and Wong 2008; Zhou 2011; Niinimäki, Parviainen, and Koivisto 2016), which are quite accurate but also computationally demanding. This limits Monte Carlo methods to smaller networks with only tens of nodes. Each of the learning algorithms implemented in sparsebn is a score-based method, and as such this package represents an attempt to resolve many of the computational and statistical issues cited here with respect to these methods.

# Hybrid methods 

Finally, there are hybrid methods which combine constraint-based and score-based methods. Hybrid methods first prune the search space by using a constraint-based search, and then learn an optimal DAG structure via score-based search (Tsamardinos, Brown, and Aliferis 2006; Perrier, Imoto, and Miyano 2008; Gámez, Mateo, and Puerta 2011). The max-min hillclimbing (MMHC) algorithm proposed by Tsamardinos et al. (2006) is a powerful method of this kind.

### 2.4. Existing R packages for structure learning

There are several existing R packages for learning and manipulating Bayesian networks. bnlearn is a thorough and actively maintained package that implements a wide variety of classical approaches such as HC and MMHC (Scutari 2010, 2017). pcalg focuses on the causal interpretation of Bayesian networks, and implements the PC and FCI algorithms along with methods for inferring causal effects (Kalisch, Mächler, Colombo, Maathuis, and Bühlmann 2012). Other packages include deal for mixed data (Boettcher and Dethlefsen 2003) and gRain (Højsgaard 2012) for exact and approximate computations. For structural equation models in particular, lavaan is a modern R package that implements many of the standard fitting procedures for SEM (Rosseel 2012). There are also many software packages available on platforms besides R (for a more complete list see Murphy 2014) such as BEANDisco (Niinimäki et al. 2016, https://www.cs.helsinki.fi/u/tzniinim/BEANDisco/), AMIDST (Masegosa et al. 2017, http://www.amidsttoolbox.com/), and GOBNILP (Cussens, Haws, and Studený 2017, https://www.cs.york.ac.uk/aig/sw/gobnilp/).
Motivated by applications to computational biology and machine learning, sparsebn was designed for the following types of applications:

- Datasets with several thousand variables, which arise in computational biology and machine learning,
- High-dimensional data with $p \gg n$, which is common in genomics applications with high-throughput datasets, such as gene expression data that have $p \sim 20,000$ and $n \sim 100$,
- Experimental data with interventions, which is also common in genomics applications.

Unfortunately, the aforementioned packages either do not scale to handle these types of problems, or cannot process high-dimensional data at all. By contrast, the sparsebn package was specifically designed to fill this gap, with an orientation towards large, high-dimensional, experimental data. In order to achieve this, the methods contained in this package rely on a combination of novel methodology and algorithms in order to scale to larger and larger datasets. Of course, these methods also gracefully degrade to handle simpler settings with observational and/or low-dimensional data. Moreover, whenever possible, cross-compatibility with the above mentioned packages has been provided (Section 4.5).

# 3. Learning with sparse regularization 

To learn a Bayesian network from data, we use a score-based approach based on regularized maximum likelihood estimation that allows for the incorporation of experimental data. In this section we discuss these details as well as the block coordinate descent algorithm used to approximate the resulting optimization problem.

### 3.1. Regularized maximum likelihood

Suppose $\mathbf{X} \in \mathbb{R}^{n \times p}$ is a matrix of observations, and let $\ell$ denote the negative log-likelihood and $\rho_{\lambda}$ be some regularizer. For example, $\rho_{\lambda}$ may be the $\ell_{1}$ penalty (Tibshirani 1996), the group norm penalty (Yuan and Lin 2006), or a nonconvex penalty such as the smoothly clipped absolute deviation (SCAD, Fan and Li 2001) or minimax concave penalty (MCP, Zhang 2010). Furthermore, we assume that $\mathbf{X}$ does not contain any missing values. If the data contains missing values, these should be imputed first.
We consider the following program:

$$
\min _{B \in \mathbb{D}} \ell(B ; \mathbf{X})+\rho_{\lambda}(B)
$$

where $\mathbb{D} \subset \mathbb{R}^{p \times p}$ is the set of weighted adjacency matrices that represent directed graphs without cycles. The resulting problem (7) is a nonconvex program, where the nonconvexity arises from (potentially) all three terms: The constraint $\mathbb{D}$, the loss function $\ell$, and the regularizer $\rho_{\lambda}$.
For continuous data, we use a Gaussian likelihood derived from Equation 2 combined with $\ell_{1}$ or MCP regularization, and for discrete data we use a multi-logit model as in Equation 5 combined with a group lasso penalty. When some data are generated under experimental intervention, we can derive the form of $\ell(B ; \mathbf{X})$ using the strategy discussed in Section 2.2: When $X_{i}$ is under intervention, its marginal distribution is known and hence can be considered constant in Equation 6. Let $\mathcal{I}_{j}$ be the set of row indices of the data matrix $\mathbf{X}$ where node $X_{j}$ is under intervention, and $\mathcal{O}_{j}=\{1, \ldots, n\}-\mathcal{I}_{j}$ be the collection of observations for which $X_{j}$ is not under intervention. Then, according to Equation 6, the negative log-likelihood factorizes as

$$
\ell(B ; \mathbf{X})=-\sum_{j=1}^{p} \sum_{h \in \mathcal{O}_{j}} \log f_{\beta_{j}}\left(\mathbf{x}_{h j} \mid \mathrm{pa}\left(\mathbf{x}_{h j}\right)\right)
$$

where $B=\left[\beta_{1}|\cdots| \beta_{p}\right], f_{\beta_{j}}$ is the conditional density for the $j$ th node, and $\mathbf{x}_{h j}$ is the value of node $X_{j}$ at the $h$ th data point. Note that multiple nodes may be intervened for a

particular data point. By incorporating experimental interventions in this way, we are able to orient the edges in a causal Bayesian network and thus distinguish between equivalent DAGs. A similar strategy from a Bayesian perspective was first adopted in Cooper and Yoo (1999). Evidently, one advantage of this framework is its universal applicability to different data types and various likelihood models.
Since the program (7) is nonconvex it is generally regarded as infeasible to find an exact global minimizer of this problem. Indeed, score-based structure learning is known to be NP-hard (Chickering, Heckerman, and Meek 2004). Instead, we seek local minimizers of (7) through an optimization scheme based on block coordinate descent. The method is based on the following observation: The difficulty in solving (7) lies in enforcing the constraint $B \in \mathbb{D}$, which is a highly nonconvex and singular parameter constraint. Instead, if we consider (7) one edge at a time, the problem simplifies considerably. This is the heuristic exploited by many score-based methods (most notably greedy hill climbing). Unlike conventional methods, however, Fu and Zhou (2013) propose a block-cyclic strategy and show that it outperforms existing approaches based on greedy updates. This general observation has been exploited to construct the family of fast algorithms implemented in sparsebn.

# 3.2. Algorithm details 

Recalling that $B=\left(\beta_{i j}\right)$, the high-level idea behind the method is the following:

1. Repeat outer loop until stopping criterion met:
2. Outer loop. For each pair $(j, k), j \neq k$ :
(a) Minimize (7) with respect to $\left(\beta_{k j}, \beta_{j k}\right)$, holding all other parameters fixed;
(b) If the edge $k \rightarrow j$ (resp. $j \rightarrow k$ ) induces a cycle in the graph, set $\beta_{k j} \leftarrow 0$ (resp. $\beta_{j k} \leftarrow 0$ ) and then update $\beta_{j k}$ (resp. $\beta_{k j}$ );
(c) Repeat inner loop until convergence:
3. Inner loop. Fix the edge set $E$ from the outer loop and minimize (7) by cycling through the edge weights $\beta_{k j}$ for $(k, j) \in E$.

Since the program (7) depends on the unknown regularization parameter $\lambda$, this value must be supplied in advance to the algorithm. In practice, we wish to solve (7) for several values of the regularization parameter, so instead of returning a single DAG estimate, the output of this meta-algorithm is a solution path (also called a regularization path, Friedman et al. 2010): A sequence of estimates $\left\{\widehat{B}\left(\lambda_{\max }\right), \widehat{B}\left(\lambda_{1}\right), \ldots, \widehat{B}\left(\lambda_{\min }\right)\right\}$ for a pre-determined grid of values $\lambda_{\max }>\lambda_{1}>\cdots>\lambda_{\min }$. This is standard practice in the literature on coordinate descent (Friedman et al. 2007; Wu and Lange 2008), and is similar to the well-known graphical lasso for undirected graphs (Friedman, Hastie, and Tibshirani 2008).
As $\lambda$ decreases, there is less regularization, hence the resulting estimates $\widehat{B}\left(\lambda_{m}\right)$ become more dense (i.e., contain more edges). Since our focus is on sparse graphs, in practice we use this fact to terminate the algorithm early if the solution path becomes too dense, i.e., if the number of edges in $\widehat{B}\left(\lambda_{m}\right)$ exceeds some user-defined threshold. The default values used in sparsebn are $10 p$ edges for continuous data and $3 p$ edges for discrete data. The smaller threshold for discrete data is due to the higher computational complexity of the underlying algorithm as compared with the continuous case.

The detailed implementation of the algorithms uses several tricks from the literature on coordinate descent in order to speed up the algorithm:

- Warm starts. Given the previous estimate $\widehat{B}\left(\lambda_{m-1}\right)$ in the solution path, we use $\widehat{B}\left(\lambda_{m-1}\right)$ as the initial guess for the next iterate $\widehat{B}\left(\lambda_{m}\right)$. Furthermore, it is always possible to choose $\lambda_{\max }$ so that $\widehat{B}\left(\lambda_{\max }\right)=\mathbf{0}$ (i.e., the zero matrix), which is the default implementation used by sparsebn.
- Active set iterations. In the inner loop above, the algorithm only updates the nonzero parameters by solving at most $p$ penalized regression or multi-logit regression problems. These subproblems are computationally tractable and can be solved efficiently, which yields significant performance improvements for large graphs.
- Block updates. Instead of updating each $\beta_{j k}$ one at a time, the algorithms update each parameter as a block $\left\{\beta_{j k}, \beta_{k j}\right\}$. This is justified by the acyclicity assumption: If $\beta_{j k} \neq 0$ and $\beta_{k j} \neq 0$, then the acyclic constraint is violated, and this fact is exploited to update both parameters simultaneously.
- Sparse data structures. Internally, everything is stored using sparse data structures for representing directed acyclic graphs. This saves memory and speeds up the computation of each update.

Compared with existing packages for structure learning, the main novelties of the present methods are (1) The use of $\ell_{1}$ and MCP regularization, (2) Block-cyclic (as opposed to greedy, one-at-a-time) updates, and (3) The use of warm starts in computing the solution path. Further details can be found in Fu and Zhou (2013) and Aragam and Zhou (2015).

# 3.3. Parameter estimation 

After learning the structure of a Bayesian network, often it is of interest to then estimate the parameters of the local conditional distributions associated with the learned structure. For causal DAGs, these parameters determine the causal effect sizes between the parents and their children.
For Gaussian data, this is straightforward by regressing each node onto its parents, using (unpenalized) least squares regression. Note that this requires that the maximum number of parents is at most $n$, which is another motivation for leveraging sparsity in our algorithms. This produces a weighted adjacency matrix $\widehat{B}=\left(\widehat{\beta}_{i j}\right)$ (or more specifically, a solution path of adjacency matrices). Given these weights, we can estimate the conditional variance of each node given its parents by:

$$
\widehat{\omega}_{j}^{2}:=\operatorname{VAR}\left(\mathbf{x}_{j}-\mathbf{X} \widehat{\beta}_{j}\right)
$$

This yields a variance matrix $\widehat{\Omega}=\operatorname{diag}\left(\widehat{\omega}_{1}^{2}, \ldots, \widehat{\omega}_{p}^{2}\right)$, and together $(\widehat{B}, \widehat{\Omega})$ can be used to estimate the covariance matrix $\Sigma$ (see Section 2.1).
For discrete data, we regress each node onto its parents set using multi-logit regression via the R package nnet (Venables and Ripley 2002). Note that for discrete data, instead of a coefficient matrix we get a 4 -way array $\widehat{B}=\left(\widehat{\boldsymbol{\beta}}_{i j}\right)$, where $\widehat{\boldsymbol{\beta}}_{i j}$ is a matrix and the $(u, k)$ entry of this matrix is the influence that level $k$ of $X_{i}$ has on level $u$ of $X_{j}$.

# 4. The sparsebn package 

Based on the framework described in Section 3, sparsebn implements four structure learning algorithms that are each tailored to a specific type of data:

- Experimental, Gaussian data (Zhang 2016).
- Experimental, discrete data (Gu et al. 2018).
- Observational, Gaussian data (Aragam and Zhou 2015).
- Observational, discrete data (Gu et al. 2018).

By combining these approaches, sparsebn automatically handles datasets with mixed observational and experimental data. Each algorithm is implemented in C++ using Rcpp (Eddelbuettel and François 2011; Eddelbuettel 2013). In addition to the main algorithms, the package implements high-level methods for fitting, plotting, and manipulating graphical models.
Furthermore, sparsebn is actually a family of R packages, designed to be cross-compatible with minimal external dependencies. To date, sparsebn imports the following packages:

- ccdrAlgorithm, based on Aragam and Zhou (2015) and Fu and Zhou (2013).
- discretecdAlgorithm (Gu 2017), based on Gu et al. (2018).
- sparsebnUtils (Aragam, Gu, and Zhou 2017), for housing various common utilities and classes.

The idea is that the codebase for each algorithm is housed inside its own package, allowing for rapid development and convenient extensibility. This allows us to add new algorithms and features rapidly without significant dependency or compatibility constraints.

### 4.1. Speed and scalability improvements

sparsebn is designed to handle large, high-dimensional datasets with $p$ potentially in the thousands. To illustrate this, Figure 2 provides a comparison of our methods with the PC algorithm from the pcalg package and the MMHC algorithm from the bnlearn package. Due to the higher computational workload for discrete algorithms in general, the results here are for Gaussian data only. Furthermore, although these numbers are intended to be illustrative, the interested reader may find more extensive simulations corroborating these results for both types of data in Aragam and Zhou (2015); Gu et al. (2018).
In order to provide a direct comparison, the times reported in Figure 2 reflect the total time to learn graphs of the same complexity (number of edges), even though sparsebn is capable of computing further into the solution path if desired. Note also that both the PC and MMHC algorithms output only a single graph, whereas our method outputs a solution path with multiple graph estimates. The results illustrate how sparsebn provides a more favorable scaling when $p$ is large: For the largest graph with 1090 nodes, sparsebn is 17 x faster compared to the PC algorithm in pcalg and 52x faster compared to the MMHC algorithm in bnlearn. These computational improvements are made possible by the use of an efficient block coordinate descent algorithm that leverages warm starts and active set updates; for more details see Section 3.2.

![img-1.jpeg](img-1.jpeg)

Figure 2: Timing comparison (in seconds). Each point represents the total runtime to execute an algorithm on simulated Gaussian data as a function of the number of nodes $p=109 k$ $(k=1, \ldots, 10)$. The DAGs were constructed by tiling $k$ independent copies of the pathfinder network $(p=109)$, and $n=50$ samples were randomly generated for each dataset. (solid black line) $\mathrm{C}=\mathrm{CCDr}$ algorithm implemented in sparsebn, (dashed blue line) $\mathrm{P}=\mathrm{PC}$ algorithm implemented in pcalg, (dotted red line) $\mathrm{M}=\mathrm{MMHC}$ algorithm implemented in bnlearn.

# 4.2. Experimental interventions 

In addition to scalability, another feature that distinguishes sparsebn is its native support for mixed observational and experimental data. As discussed in Section 2.2, experimental interventions allow observationally equivalent DAGs to be distinguished, thereby uncovering the structure of the true causal DAG. To illustrate this, we ran two simulation experiments, reported in Figures 3 and 4. To keep things simple, we focus on discrete data. (Code to run these experiments on continuous data can be found at https: //github.com/itsrainingdata/sparsebn-reproduce.) As in the previous subsection, a more thorough evaluation of the effect of interventions can be found in Gu et al. (2018); Zhang (2016); Fu and Zhou (2013).

Figure 3 illustrates how the accuracy of reconstruction improves as interventions are added to each node in the network. We can see that as we process more interventions per node (denoted by $m$ ) with $n$ held fixed, the true positive rate (TPR) increases. Further analysis of these results indicates furthermore that the number of reversed edges decreases along with the number of false positives, and as a result the overall structural Hamming distance (SHD) - the total number of edge additions, deletions, and reversals needed to convert one directed graph into another - decreases.

Figure 4 considers the more practical scenario in which only $k(k<p)$ nodes in the network are under intervention, and over time more interventions on more nodes are able to be collected. This is common, for example, when reconstructing large networks in biological applications. Again, we see that overall the true positive rate increases as more nodes are under intervention, and further analysis shows that the SHD decreases as well.

![img-2.jpeg](img-2.jpeg)

Figure 3: The effect of interventions in learning discrete DAGs. For every node, $m$ interventions are added to otherwise observational data with $n=500$ and $p=50$. (A) Scale-free network with 49 edges (solid green line), small-world network with 100 edges (dashed red line), polytree with 49 edges (dashed blue line), and bipartite graph with 50 edges (dashed black line); (B) Plot for each network individually.
![img-3.jpeg](img-3.jpeg)

Figure 4: The effect of interventions in learning discrete DAGs. For each $k=0, \ldots, 50$, $m=10$ interventions for $k$ randomly selected nodes are added to otherwise observational data with $n=500$ and $p=50$. Results are averaged over 20 random permutations of the order in which each node is intervened on as $k$ is increased. (A) Scale-free network with 49 edges (solid green line), small-world network with 100 edges (dashed red line), polytree with 49 edges (dashed blue line), and bipartite graph with 50 edges (dashed black line); (B) Plot for each network individually.

Since $n$ is held fixed in each simulation, the improvements observed here cannot be attributed to an increase in sample size, illustrating how sparsebn is able to improve estimation of the true causal graph under experimental interventions. In particular, reducing reversed edges that are observationally equivalent shows in an obvious way the utility of interventions for causal inference.

# 4.3. Functions 

The main purpose of the sparsebn package is estimation of graphical models, which is accomplished through the methods prefaced with "estimate.". In this section, we present an overview of the main estimation methods. In addition, sparsebn includes methods for generating random graphs, simulating random data, visualization, and conversion between various graph classes, which are documented extensively in the package manual.
The main function is estimate. dag, which can be called as follows:

```
estimate.dag(data, lambdas = NULL, lambdas.length = 20, whitelist = NULL,
    blacklist = NULL, error.tol = 1e-04, max.iters = NULL,
    edge.threshold = NULL, concavity = 2, weight.scale = 1, convLb = 0.01,
    upperbound = 100, adaptive = FALSE, verbose = FALSE)
```

The main arguments are data, lambdas, and lambdas.length. By default, the lambdas argument is NULL and a standard sequence of $L=20$ regularization parameters is generated. If desired, the user can pre-compute a vector of regularization parameters to be used instead, in which case this vector should be passed through the lambdas argument. If there is prior knowledge of (directed) edges that are known to be present in the network, these can be specified via the whitelist argument. Similarly, if there is prior knowledge of (directed) edges that are known to be absent from the network, these can be specified via the blacklist argument. The rest of the arguments control the convergence of the internal algorithms, and are intended for advanced users. This method returns a sparsebnPath object (Section 4.4), which stores the solution path described in Section 3.2.
It is important to bear in mind that the objects returned by estimate. dag are graphs, and in particular they do not include estimates of model parameters such as edge weights or conditional variances. To obtain these parameters, sparsebn includes the estimate. parameters method, which can be called as follows:
estimate.parameters(fit, data, ...)
where fit is the output of estimate. dag and data is the data to be used for parameter estimation.
In addition to estimating DAGs, sparsebn can estimate the precision and/or covariance matrix for multivariate Gaussian data. The nonzero entries in the precision matrix in particular yield the so-called Gaussian graphical model, which is an undirected graphical model for multivariate Gaussian data. This can be done via the estimate. precision and estimate. covariance methods:
estimate.covariance(data, ...)
estimate.precision(data, ...)
Internally, these methods call estimate. dag and use Equation 4 to compute the estimated precision (or covariance) matrix. The ... argument here allows the user to specify any of the optional arguments from estimate. dag.

### 4.4. Data structures

sparsebn uses three different S3 classes in order to represent data (sparsebnData), graphs (sparsebnFit), and solution paths (sparsebnPath). For each of these classes, the usual generics are defined such as print, summary, and plot.

The sparsebnData class is used to represent both continuous and discrete data with experimental interventions. Observational data corresponds to the degenerate case where $\mathbf{X}$ does not contain any interventions, and is treated as such by the sparsebn package. The slots are:

- data: This is the original data as a data frame with $n$ observations and $p$ variables.
- type: Either "continuous" or "discrete".
- levels: A list of levels for each variable. This is a list of length $p$ whose $j$ th component is a vector containing the levels of the $j$ th variable.
- ivn: The list of interventions for each observations. This is a list of length $n$ whose $i$ th component is a vector of node names (or indices) that are under intervention for the $i$ th observation.

The sparsebnPath class represents a solution path, which is the output of the main function estimate.dag. Internally, this is a list of sparsebnFit objects whose $j$ th component corresponds to the $j$ th value of $\lambda$ in the solution path, $\lambda_{\max }>\lambda_{1}>\cdots>\lambda_{\min }$. Since this class is essentially a wrapper for this list, it has no named slots.
The sparsebnFit class represents an individual graph estimate from a DAG learning algorithm. The graph itself is stored as an edgeList object in the edges slot, which is an internal implementation of a child-parent edge list. Alternatively, this graph can also be stored in a variety of other formats including graphNEL (from the graph package), igraph (from the igraph package), and network (from the network package) by using the setGraphPackage method (Section 4.5). The slots are:

- edges: A directed graph corresponding to the estimated network, stored internally as an edgeList by default.
- nodes: A vector of node names for the graph.
- lambda: The value of $\lambda$ used to estimate the network.
- nedge: The total number of edges in the graph.
- pp, nn, time: The number of nodes, number of samples, and clock time to estimate this network (these are mainly used internally by the package).


# 4.5. Compatibility 

Unfortunately, there is no consistent standard in R for storing and representing graphs. As a result, different domains have adopted different R packages as a de facto standard for graph and network representation. For example, in biology the graph package (Gentleman, Whalen, Huber, and Falcon 2011) seems to be the most popular, whereas in social science and demography the network package (Butts 2008) is more popular. In other domains, the igraph package (Csardi and Nepusz 2006) is popular, which has libraries in R, Python, and C. For this reason, sparsebn does not provide its own mechanism for manipulating graphs, and instead provides cross-compatibility with each of these three packages. By default, all methods

output graphs stored as an edgeList object, which is an internal class with little builtin functionality outside of being a storage mechanism for graph data. In order to make use of the extensive capabilities of the different graph packages in $R$, we have included the setGraphPackage method to allow users to set a global preference for which graph package to use. Once this preference is set, the full feature set of the selected package (e.g., plotting, manipulation, network statistics, etc.) becomes available to the user. We emphasize that the purpose of sparsebn is not to provide a new library for graph representation and visualization, but instead to provide algorithms for learning their structure. The manipulation of graphs is appropriately left to libraries designed explicitly for that purpose.
Furthermore, to allow cross-compatibility with existing packages for structure learning, we have provided methods to convert the output of sparsebn methods to bnlearn-compatible objects. Compatibility with the pcalg package is possible via the aforementioned graph package, which is the default representation used by pcalg.
The setGraphPackage method sets a global preference for the underlying class used to store graphs by the package. That is, all of the existing graph objects and any subsequent output will be coerced to the desired class. Generally speaking, this corresponds to the output of estimate.dag and any corresponding sparsebnPath objects. Alternatively, users can manually do this conversion on an object-by-object basis using the following methods:

- to_igraph: Conversion to and from igraph graphs from the igraph package;
- to_graphNEL: Conversion to and from graphNEL graphs from the graph package;
- to_network: Conversion to and from network graphs from the network package;
- to_bn: Conversion to and from bn graphs from the bnlearn package.

Each of these methods works on sparsebnPath, sparsebnFit, edgeList objects, in addition to any of the objects listed above.
Finally, the sparsebn package is compatible with the popular Cytoscape application (Shannon et al. 2003). This is a standalone graphical interface for visualizing and analyzing complex networks. This is accomplished via the openCytoscape method, which leverages the RCy3 package (Shannon, Grimes, Kutlu, Bot, and Galas 2013) under the hood. In order to use this method, both RCy3 and Cytoscape must be installed. For an example of this method in use, see Section 5.7.

# 4.6. Installation 

sparsebn is an open-source package and is made freely available through CRAN. To install the latest stable version in R,
```
R> install.packages("sparsebn")
```
For advanced users, the development versions can be downloaded directly from GitHub. Using devtools (Wickham, Hester, Chang, RStudio, and R Core Team 2018), the entire suite of packages can be installed via

```
R> devtools::install_github(c("itsrainingdata/sparsebnUtils@dev",
+ "itsrainingdata/ccdrAlgorithm@dev", "gujyjean/discretecdAlgorithm@dev",
+ "itsrainingdata/sparsebn@dev"))
```

Note that before being released to CRAN, development versions may be unstable.

# 5. Example: Cytometry data 

To illustrate the use of this package, we will use the flow cytometry dataset from Sachs, Perez, Pe'er, Lauffenburger, and Nolan (2005) as a working example in this section. The original dataset consists of $n=7466$ observations of $p=11$ continuous variables corresponding to different proteins and phospholipids in human immune system cells, and each observation indicates the measured level of each biomolecule in a single cell under different experimental interventions. A network consisting of all well-established causal interactions between these molecules has been constructed based on biological experiments and literature. This network is frequently used as a benchmark to assess the accuracy of BN learning algorithms on real data. Therefore, we refer to this as the consensus network in the sequel.
The consensus network is visualized in Figure 5, in which a directed edge indicates that a change in the level of the parent will cause a change in the level of the child. This is a relatively small network which we use in order to keep the exposition simple. More examples, including a discrete version of this dataset and applications to large networks with hundreds or thousands of nodes, will be discussed in Section 6.
First, we load this data:

```
R> library("sparsebn")
R> data("cytometryContinuous")
R> names("cytometryContinuous")
```

[1] "dag" "data" "ivn"
![img-4.jpeg](img-4.jpeg)

Figure 5: The consensus cytometry network (11 nodes, 17 edges). A topological ordering of this network is PIP3 $\prec$ PLCg $\prec$ PIP2 $\prec$ PKC $\prec$ PKA $\prec$ raf $\prec$ mek $\prec$ erk $\prec$ akt $\prec$ p38 $\prec$ jnk.

Note that this is not a data.frame, but instead a list of R objects that will be useful for this specific example. Each component of this list stores an important part of the experiment:

- dag is the consensus network with 11 nodes and 17 edges, as described above.
- data is raw data collected from these experiments.
- ivn is a list of interventions for each observation in the dataset.

To illustrate the use of this package, the rest of this section describes the main steps to learning Bayesian networks from data: (1) Loading the data, (2) Learning the structure, (3) Incorporating prior knowledge, (4) Exploring the solution path and estimated networks, (5) Estimating the parameters, (6) Selecting the regularization parameter, and (7) Visualizing and assessing the output.

# 5.1. Loading data 

In order to distinguish different types of data - namely, experimental versus observational and continuous versus discrete - we use the sparsebnData class which wraps a data.frame into an object containing this auxiliary information. All of the methods implemented in sparsebn expect input as sparsebnData.
To use this class, we need two important pieces of information: The raw data as a data.frame, and a list of interventions for each observation in the dataset. If the dataset does not contain any interventions, then the latter can be omitted. In order to create a sparsebnData object from the cytometry data, we first extract the necessary objects from cytometryContinuous:

```
R> cyto.raw <- cytometryContinuous$data
R> cyto.ivn <- cytometryContinuous$ivn
```

Now we can create the required sparsebnData object:

```
R> cyto.data <- sparsebnData(cyto.raw, type = "continuous",
+ ivn = cyto.ivn)
```

Notice that we need to explicitly specify that the data is continuous (for discrete data, one would specify type = "discrete").
Finally, for discrete data, we may wish to manually specify the levels of each variable, which can be done using the levels argument. When this argument is omitted, we attempt to automatically infer the levels. Note that in doing so, however, levels which are missing from the data will not be recognized by the sparsebnData constructor.

```
R> print(cyto.data)



5: 3.52 2.98568 1.65 2.28 3.211 3.05 3.83 5.72 1.54 3.246 4.398
7462: 3.89 2.51770 3.49 3.33 3.122 2.46 3.64 7.04 0.00 0.936 0.000
7463: 3.15 1.52823 2.88 3.10 2.701 3.89 4.21 6.83 0.00 2.284 0.000
7464: 3.34 1.50185 2.93 3.01 2.322 1.12 3.09 6.59 0.00 0.560 0.693
7465: 3.54 1.96009 1.75 3.03 2.715 3.47 3.72 6.70 3.80 7.231 0.892
7466: 3.42 0.00995 1.99 5.15 3.131 1.89 2.62 6.79 0.00 0.000 0.501

7466 total rows ( 7456 rows omitted)
Continuous data w/ interventions on 4863/7466 rows.
R> summary(cyto.data)


7466 total rows ( 7456 rows omitted)
Continuous data w/ interventions on 4863/7466 rows.
```
Note that some of the observations were not under intervention - such datasets with mixed observational and experimental samples are automatically handled by the methods in this package.

# 5.2. Structure learning 

To learn the structure of a Bayesian network from this data we use the estimate.dag() method, which runs the algorithm outlined in Section 3.2. To call this method using the default parameter settings, use:

```
R> cyto.learn <- estimate.dag(cyto.data)
R> print(cyto.learn)
sparsebn Solution Path
    11 nodes
    7466 observations
    20 estimates for lambda in [0.8641, 86.406]
    Number of edges per solution: 0-1-6-8-13-15-15-19-22-21-26-33-35-36-38-38-
    41-43-46-50
R> summary(cyto.learn)
sparsebn Solution Path
    11 nodes
    7466 observations
    20 estimates for lambda in [0.8641, 86.406]
    Number of edges per solution: 0-1-6-8-13-15-15-19-22-21-26-33-35-36-38-38-
    41-43-46-50
```


In addition to data, there are several optional parameters that can be passed to estimate. dag. The main arguments of interest are lambdas and lambdas.length, which allow the user to adjust the grid of regularization parameters $\lambda_{\max }>\lambda_{1}>\cdots>\lambda_{\min }$ used by the algorithms (Section 3.2).
By default, estimate. dag produces a solution path of 20 estimates with the grid chosen adaptively to the data. This grid can be shortened or lengthened by specifying lambdas.length:
```
R> estimate.dag(cyto.data, lambdas.length $=50$ )
sparsebn Solution Path
11 nodes
7466 observations
50 estimates for lambda in [0.8641, 86.406]
Number of edges per solution: 0-0-1-1-2-6-6-7-8-11-12-12-13-15-15-16-16-17-
19-19-20-21-21-21-21-24-27-28-31-35-35-35-34-36-36-37-38-38-38-38-39-41-42-
$42-44-45-45-47-48-50$

For even more fine-tuning, the lambdas argument allows the user to explicitly input their own grid. For convenience we have included the generate.lambdas method, which provides a mechanism for generating grids of arbitrary lengths on either a linear or log scale. To generate a grid with a linear scale, use scale = "linear":

R> cyto.lambdas <- generate.lambdas(lambda.max $=10$, lambdas.ratio $=0.001$,
$+\quad$ lambdas.length $=10$, scale $=$ "linear")
R> cyto.lambdas
[1] $10.008 .89 \quad 7.78 \quad 6.67 \quad 5.56 \quad 4.45 \quad 3.34 \quad 2.23 \quad 1.12 \quad 0.01$

To use a log scale, use scale = "log":
R> cyto.lambdas <- generate.lambdas(lambda.max $=10$, lambdas.ratio $=0.001$,
$+\quad$ lambdas.length $=10$, scale $=$ "log")
R> cyto.lambdas
[1] $10.00004 .6416 \quad 2.1544 \quad 1.0000 \quad 0.4642 \quad 0.2154 \quad 0.1000 \quad 0.0464$
[9] $0.0215 \quad 0.0100$

This grid can also be generated manually, although this is not recommended. To run the algorithm using cyto.lambdas (output suppressed below):
R> estimate.dag(cyto.data, lambdas = cyto.lambdas)
```
Another argument of interest is edge.threshold, which is another way to specify when the algorithm terminates. Specifically, if any point on the solution path contains an estimate with more than edge. threshold edges, the algorithm will terminate immediately and return what has been estimated up to that point. This makes our methods anytime algorithms, in the sense that they can be interrupted at anytime while still producing valid output. This is convenient when running tests on very large graphs.

# 5.3. Prior knowledge 

In some contexts, users may have prior knowledge regarding edges that must be present or absent from the network. For example, it may already be known that PIP3 regulates PIP2 (see Figure 5). In this case, estimation of the underlying network can be substantially improved

by incorporating this information into the estimation procedure. With the sparsebn package, this can be done via whitelists and blacklists, which specify edges that must be present and absent, respectively.
For example, to specify a known relationship between PIP3 and PIP2, we can create a whitelist as follows:

```
R> whitelist <- matrix(c("pip3", "pip2"), nrow = 1)
R> estimate.dag(cyto.data, whitelist = whitelist)
```

The whitelist argument should be a two-column matrix, where the first column stores parents and the second stores children (i.e., a from-to adjacency list):

```
R> whitelist
    [,1] [,2]
[1,] "pip3" "pip2"
```

Thus, this whitelist ensures that the edge PIP3 $\rightarrow$ PIP2 will be present in the final estimates. Similarly, we can specify a blacklist, which stores edges that are known to be absent. For example, we can forbid any edges between RAF and MEK as follows:

```
R> blacklist <- rbind(c("raf", "jnk"), c("jnk", "raf"))
R> estimate.dag(cyto.data, blacklist = blacklist)
```

As with the whitelist, the blacklist should be a two-column matrix. Note that we specify both directions $\mathrm{RAF} \rightarrow \mathrm{MEK}$ and $\mathrm{MEK} \rightarrow \mathrm{RAF}$. If it is known that the direction can only go in one direction, then a single direction may be specified instead.
Blacklists are useful for specifying known root and leaf nodes in a Bayesian network. In the cytometry network, PIP3 is a root node (i.e., it has no parents). Thus, we can forbid any edges pointing into PIP3. Similarly, JNK, P38, and AKT are leaf nodes (i.e., they have no children), so we can forbid any edges pointing away from all three nodes. To specify this, we make use of the specify.prior function, which automatically builds an appropriate blacklist given the names of the root and leaf nodes. Any number of root and/or leaf nodes can be specified.

```
R> blacklist <- specify.prior(roots = "pip3", leaves = c("jnk", "p38", "akt"),
+ nodes = names(cyto.data$data))
R> estimate.dag(cyto.data, blacklist = blacklist)
```

Finally, whitelists and blacklists can be combined arbitrarily, as long as they are consistent in the sense that no edge appearing in the whitelist appears in the blacklist, and vice versa. This allows for a powerful specification of prior knowledge in learning networks from data.

# 5.4. Solution paths 

The output of estimate. dag is a sparsebnPath object, which stores the entire solution path that is returned by the method. This is similar in spirit to the glasso package (Friedman,

Hastie, and Tibshirani 2018), however, instead of storing each estimate as an R matrix we use the internal class sparsebnFit. Since sparsebnPath objects also inherit from the list class in base R, we can inspect the first solution using ordinary R indexing. Note that for sparsebnFit objects, the print and summary methods are identical, so the output below is shown only once.

```
R> print(cyto.learn[[1]])
R> summary(cyto.learn[[1]])

CCDr estimate
7466 observations
lambda = 86.4060183089118

DAG:
<Empty graph on 11 nodes.>
```

The first estimate will always be the empty graph, which is a consequence of how we employ warm starts in the solution path. The third estimate, for example, shows a bit more structure:

```
R> print(cyto.learn[[3]])
R> summary(cyto.learn[[3]])


CCDr estimate
7466 observations
lambda $=53.2129918008817$


DAG:
[raf] mek
[mek]
[plc]
[pip2] plc
[pip3]
[erk] akt
[akt]
[pka] p38
[pkc]
[p38] pkc
[jnk] pkc
```

Each row in the output above corresponds to a child node - indicated by the square brackets - with its parents listed to the right without brackets. Formally, this is an adjacency list ordered by children. For large graphs, explicit output of the parental structure as shown here is omitted by default, however, this behavior can be overridden via the maxsize argument. Alternatively, we can retrieve the adjacency matrix, $\left\{I\left(\tilde{\beta}_{i j} \neq 0\right)\right\}_{p \times p}$, for this estimate:
```
R> get.adjacency.matrix(cyto.learn[[3]])


11 x 11 sparse Matrix of class "dgCMatrix"
raf
mek 1
plc . . . 1
pip2
pip3
erk
akt . . . . . 1
pka
pkc . . . . . . . . . . 1 1
p38 . . . . . . . 1
jnk
```

Note the use of the Matrix package (Bates and Mächler 2019), which reduces the memory footprint on large graphs.
Finally, for large graphs, it may be desirable to inspect a subset of nodes, which can be done using the show. parents method:
```
R> show.parents(cyto.learn[[3]], c("raf", "pip2"))
[raf] mek
[pip2] plc
```
# 5.5. Parameter estimation 

It is important to note that the output of estimate.dag is a sequence of graphs, i.e., no parameters (edge weights, variances, etc.) have been estimated at this stage. The next step is to estimate the values of the parameters associated with the underlying joint distribution. This is easy to do:
```
R> cyto.param <- estimate.parameters(cyto.learn, data = cyto.data)
The output is a list with each entry containing a component for the weighted adjacency matrix (coefs) and a diagonal matrix for the conditional variances (vars). For example, the coeffients of the third estimate in the solution path with six edges are (rounded to two decimal places):
R> cyto.param [[3]]\$coefs
11 x 11  sparse Matrix of class "dgCMatrix"
```
![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

Similarly, we can inspect the estimated conditional variances:
```
R> Matrix: :diag(cyto.param [[3]]\$vars)
[1] 1.1652 .6321 .5832 .1110 .9920 .6840 .9688 .4251 .8311 .5061 .676
```
Although the vars argument is a diagonal matrix, we have invoked the diag method above purely to save space.
For Gaussian data, we can also use Equation 3 to estimate the implied covariance matrix for each solution in the solution path. This is implemented via the get.covariance method (see also get.precision for computing the precision, or inverse covariance, matrix). If the user is only interested in the covariance matrix (resp. precision matrix) and not the underlying DAG, then this extra step can be skipped by directly using the estimate.covariance method (resp. estimate.precision).

# 5.6. Model selection 

Unlike existing methods, the output of estimate. dag is a solution path with multiple estimates of increasing complexity, indexed by the regularization parameter. Thus, it is important to be able to pick out estimates for inspection and further exploration. For ad hoc exploration, the select method is useful: This allows one to select an estimate from a sparsebnPath object based on the number of edges, the regularization parameter $\lambda$, or the index $j$. When selecting by the number of edges or by $\lambda$, fuzzy matching is used by default so that the closest match is returned to within a given tolerance. Selecting by index is equivalent to subsetting as usual with the subset operator ' [['. To save space, the output of the following code is suppressed:
```

R> select(cyto.learn, edges $=8$ )
R> select(cyto.learn, edges $=10$ )
In the first line above, an exact match is returned. In the second line, the closest match is returned since there is no graph with exactly 10 edges in the solution path.
R> select(cyto.learn, lambda $=41.75$ )
R> select(cyto.learn, lambda $=41.7$ )
In both of the above examples, the closest match is returned.
R> select(cyto.learn, index $=4$ )
R> cyto.learn [[4]]
```

In the both lines above, an exact match is returned. Note that the second line is equivalent to the first.
For practical applications, one is often concerned with selecting an optimal value of $\lambda$. In high-dimensions, optimal selection of $\lambda$ for finite samples is an open problem, and past work has shown that both the prediction oracle and cross-validated choices perform poorly (Meinshausen and Bühlmann 2006; Fu and Zhou 2013). Instead, Fu and Zhou (2013) suggest a practical method for selecting $\lambda$ based on a trade-off between the increase in log-likelihood and the increase in complexity between solutions. This method is implemented in sparsebn via the method select. parameter:
```

R> selected.lambda <- select.parameter(cyto.learn, cyto.data)
R> selected.lambda
[1] 8
select.parameter returns the optimal index according to this method, in this case $j=8$, corresponding to a value of $\lambda \approx 15.83806$ and an estimated network of 19 edges.
```


# 5.7. Visualization 

In order to visualize graphs estimated by the sparsebn package, we make use of the visualization capabilities of existing graph packages (see Section 4.5). By default, sparsebn uses the popular igraph package:
```

R> getPlotPackage()
[1] "igraph"
In addition to igraph, sparsebn is also compatible with the plotting features of the graph (via Rgraphviz, Hansen et al. 2008) and network packages. It is easy to change which package is used for plotting:
R> setPlotPackage("network")
R> getPlotPackage()
[1] "network"
R> setPlotPackage("graph")
R> getPlotPackage()
[1] "graph"
R> setPlotPackage("igraph")
R> getPlotPackage()
[1] "igraph"
```

![img-7.jpeg](img-7.jpeg)

Figure 6: Cleaned up plots of (a) The consensus cytometry network, (b) The learned network based on continuous data, and (c) The learned network based on discretized data. Both learned networks were estimated using estimate.dag.

This allows the user complete flexibility over which R package is used for storing data and for visualizing data. In fact, sparsebn even allows one package to be used for visualization and a different package for storage. For large graphs, it is helpful to use a different set of defaults, provided in a separate method, plotDAG, which can be used for quick plotting (see, for example, Figure 1).
Visualizing the full solution path is easy: Simply call plot(cyto.learn). In order to ensure flexibility, we maintain all of the defaults used by the selected package for the plot method. It is easy, however, to customize the appearance of the plots if desired. For example, if we would like to compare the consensus cytometry network and the estimated network side by side, we can adjust the arguments to plot as follows:

```
R> plot(cytometryContinuous$dag,
+ layout = igraph::layout_(to_igraph(cytometryContinuous$dag),
+ igraph::in_circle()),
+ vertex.label = names(cytometryContinuous$dag), vertex.size = 30,
+ vertex.label.color = gray(0), vertex.color = gray(0.9),
+ edge.color = gray(0), edge.arrow.size = 0.5)
R> plot(cyto.learn[[selected.lambda]],
+ layout = igraph::layout_(to_igraph(cytometryContinuous$dag),
+ igraph::in_circle()),
+ vertex.label = get.nodes(cyto.learn), vertex.size = 30,
+ vertex.label.color = gray(0), vertex.color = gray(0.9),
+ edge.color = gray(0), edge.arrow.size = 0.5)
```

The output can be seen in Figures 6a and 6b.
Finally, any object produced by sparsebn can be sent to the external application Cytoscape (http://www.cytoscape.org/) via the openCytoscape method. To use this method, Cytoscape must already be open and running in the background, and the RCy3 package (Ono, Muetze, Kolishovski, Shannon, and Demchak 2015) from Bioconductor must also be installed.

# 6. Further examples 

In this section we provide three more examples of the functionality of sparsebn: (1) An example with discrete data, (2) A benchmark network from the Bayesian network repository, and (3) A gene expression dataset with $p=5000$ nodes.

### 6.1. Discrete cytometry data

In the previous section we used the cytometry network as an instructional example based on the original, continuous dataset. Sachs et al. (2005) also provided a cleaned, discretized version of this dataset which can be used to illustrate how these methods apply to discrete data. After cleaning and pre-processing, the original continuous measurements were binned into one of three levels: low $=0$, medium $=1$, or high $=2$. Due to the pre-processing, the discrete data contains fewer observations $(n=5400)$ compared to the raw, continuous data. To use this data, we start by loading it as usual:

```
R> library("sparsebn")
R> data("cytometryDiscrete")
```

The code to estimate this graph is essentially the same as in Section 5. For completeness, we present only the essential steps here. As before, the first step is to pass the data into a sparsebnData object:

```
R> cyto.data <- sparsebnData(cytometryDiscrete$data, type = "discrete",
+ ivn = cytometryDiscrete$ivn)
R> cyto.data
```


5400 total rows ( 5390 rows omitted)
Discrete data w/ interventions on 3600/5400 rows.
One of the main purposes of the sparsebnData class is to encode all of the necessary information needed to run the main algorithms; now that the data has been converted into a sparsebnData object, the user will notice almost no difference between the code in Section 5 and the sequel.
To estimate a DAG based on the discrete data, use estimate.dag:

```
R> cyto.learn <- estimate.dag(cyto.data)
R> cyto.learn
sparsebn Solution Path
    11 nodes
    5400 observations
    8 estimates for lambda in [1.791, 9.7712]
    Number of edges per solution: 0-6-9-13-15-21-30-38
```

It is easy to adjust lambdas and lambdas.length as before. Note also the difference between the number of solutions here and in Section 5.2; this is a consequence of the stopping criterion used for discrete data (see also Section 3.2). For comparison with the network selected in Section 5.6 which had 19 edges, we use select to choose the estimate that is closest in complexity; the closest such network in the present case has 21 edges and is shown in Figure 6c. The code to reproduce this figure is below:

```
R> plot(select(cyto.learn, edges = 19),
+ layout = igraph::layout_(to_igraph(cytometryContinuous$dag),
+ igraph::in_circle()),
+ vertex.label = get.nodes(cyto.learn), vertex.size = 30,
+ vertex.label.color = gray(0), vertex.color = gray(0.9),
+ edge.color = gray(0), edge.arrow.size = 0.5)
```

To estimate the parameters associated with the multi-logit model, use estimate. parameters:
```

R> cyto.param <- estimate.parameters(cyto.learn, data = cyto.data)
```

As the parameter space for the multi-logit model is much larger than for the Gaussian model, the output is much more complicated. For example, the node RAF has a single parent PKA in the DAG selected above, and so the parameter space for this node is a $2 \times 3$ matrix:

```
R> cyto.param[[5]][["raf"]]
    (Intercept) pka_1 pka_2
    1 0.4219942 -0.9457959 -2.282747
    2 1.8258925 -3.6595227 -5.034717
```

For each extra parent, there will be two more columns added to this matrix, owing to the fact that each variable has three levels. There is one such matrix for each node (see Section 3.3 for details on the estimated parameters of the multi-logit model).

# 6.2. The pathfinder network 

In order to illustrate this package on a larger network, we will reconstruct the pathfinder network (Heckerman et al. 1992). The pathfinder network has 109 nodes and 195 edges and is part of the Bayesian network repository at http://www.bnlearn.com/bnrepository/, a centralized repository of benchmark networks for testing structure learning algorithms.
We first load the dataset:
```
R> data("pathfinder")
R> dat <- sparsebnData(pathfinder\$data, type = "c")
```
The data was generated from a Gaussian SEM with $\beta_{i j}=1$ whenever $\beta_{i j} \neq 0$ and $\omega_{j}^{2}=1$ for each $j$. By Equation 3, we were able to compute the implied covariance matrix and use mvtnorm to generate samples from this distribution (Genz et al. 2019). For this example, $n=1000$ samples were drawn.
For illustrative purposes, we will estimate a longer solution path with 50 DAGs:

```
R> nn <- num.samples(dat)
R> lambdas <- generate.lambdas(sqrt(nn), 0.05, lambdas.length = 50,
+ scale = "linear")
R> dags <- estimate.dag(data = dat, lambdas = lambdas, edge.threshold = 500,
+ verbose = FALSE)
R> dags
1 0 9 \text { nodes}
1 0 0 0 \text { observations}
5 0 \text { estimates for lambda in [1.5811, 31.6228]}
Number of edges per solution: 0-17-22-29-34-37-39-50-58-59-63-63-64-64-
65-78-103-108-108-108-108-108-108-108-108-108-108-108-108-108-113-115-
119-121-121-121-124-130-135-137-139-144-153-166-180-189-206-219-249-370
```

The choice of $\lambda_{\max }=n^{1 / 2}$ in generate.lambdas is important as it guarantees that the first solution will be the empty graph (see Aragam and Zhou 2015, Section 5.3). We use a linear scale for the grid and we set edge.threshold $=500$ in order to terminate the algorithm early if any estimate has more than 500 edges (although note that in this case this constraint never becomes active).
Furthermore, there are no difficulties if the data is high-dimensional $(p>n)$. Let us extract the first 50 rows of $\mathbf{X}$, so that $p=109>n=50$ :

```
R> dat <- sparsebnData(pathfinder$data[1:50, ], type = "c")
R> nn <- num.samples(dat)
R> lambdas <- generate.lambdas(sqrt(nn), 0.05, lambdas.length = 50,
+ scale = "linear")
R> dags <- estimate.dag(data = dat, lambdas = lambdas, edge.threshold = 500,
+ verbose = FALSE)
R> dags
sparsebn Solution Path
1 0 9 \text { nodes}
5 0 \text { observations}
4 3 \text { estimates for lambda in [1.3132, 7.0711]}
Number of edges per solution: 0-16-21-23-28-39-39-42-44-49-53-58-63-64-67-
69-71-80-81-84-88-92-99-102-107-111-116-116-118-123-127-134-142-149-161-
173-193-217-229-262-311-382-477
```

Note that in this case the algorithm terminates just shy of the full 50 estimates, since the 44th solution apparently exceeds the threshold of 500 edges. Finally, for this high-dimensional example, there is no noticeable slowdown compared to the previous case with $n=1000$.

# 6.3. Large networks 

To conclude the examples, we finish with an application to the estimation of very large networks using gene expression data collected from 129 late-onset Alzheimer's disease (LOAD) patients and 101 healthy patients (Zhang et al. 2013). The data consists of post-mortem whole-genome gene-expression profiles from autopsied brain tissues and in particular constitutes a purely observational sample. In total there are three datasets, each corresponding to tissue samples collected from a different brain region: (1) Dorsolateral prefrontal cortex (PFC), (2) Visual cortex (VC) and (3) Cerebellum (CR). Since ground truth networks have not been established for these datasets, the main purpose of this example is to illustrate how sparsebn scales to real world, high-dimensional data with thousands of variables.
Each dataset contains expression measurements from 39,280 probes, of which we extracted the first $p=5,000$ columns for use in this example. For this example, we focused on LOAD patients only, so $n=129$. We then used estimate.dag to learn a solution path from each dataset, and kept track of the time. In our experiments, it took a little over four minutes for our package to estimate each solution path, assuming a maximum of 5000 edges. For example, assuming the output has been stored in a variable called dags, the resulting output for the PFC data is
```

R> dags
sparsebn Solution Path
5000 nodes
129 observations
15 estimates for lambda in [2.9973, 11.3578]
Number of edges per solution: 0-79-523-1297-2200-2999-3675-4315-4929-4946-
4957-4963-4984-4988-5000
```

The output for the remaining two datasets is similar, consisting of 15 DAGs for the VC data and 16 DAGs for the CR data. Code to reproduce this experiment can be found in supplementary file v91i11.R (and at https://github.com/itsrainingdata/sparsebn-reproduce).
Some comments on the timing are in order. The edge.threshold argument was used here to terminate the algorithm at 5000 edges - in practice, of course, we do not know the true number of edges and so this is meant to be purely illustrative. Moreover, since this parameter can be set arbitrarily high, the algorithm can in principle run for arbitrarily long. In fact, one of the advantages of our methods is that they can be interrupted at anytime, bearing in mind that the result may be a subgraph of the true graph. The edge.threshold parameter allows the user to incorporate prior knowledge of the sparsity (or lack thereof) of the underlying graph.

## 7. Conclusion

sparsebn is a fast, modern package for learning the structure of sparse Bayesian networks. By leveraging recent trends in nonconvex optimization, sparse regularization, and causal

inference, we are able to scale structure learning to problems containing high-dimensional data with thousands of variables and experimental interventions. This fills a gap within existing software packages for learning Bayesian networks, which already provide excellent coverage for traditional problems with large samples and without interventions. All of the code to reproduce the results presented here is available on GitHub, along with the source code of the sparsebn package, which is available on CRAN.
Given the nonconvex nature of the minimization problems here, one future direction is to incorporate stochastic optimization into our package to enhance its global search ability. For example, stochastic gradient descent may be used in the algorithm for discrete Bayesian networks, which will reduce the computational complexity as well. We are also interested in developing divide-and-conquer strategies for ultra-large graphs, say on the scale of $10^{5}$ nodes. Along these lines, we are also exploring parallel and distributed implementations of these algorithms. Finally, our package can be combined with various post-learning functions for multi-stage learning of causal networks. Given the DAG learned from sparsebn, one may further infer causal relations in a subgraph of interest by making additional causal assumptions or with new experimental data.

# Acknowledgements 

This work was supported by NSF grants IIS-1546098 and DMS-1055286 to Q.Z. The authors thank Dacheng Zhang for helpful discussions and computational assistance.

# Affiliation: 

Qing Zhou
UCLA Department of Statistics
Los Angeles, CA 90095, United States of America
E-mail: zhou@stat.ucla.edu
URL: http://www.stat.ucla.edu/ zhou/
fournal of Statistical Software
http://www.jstatsoft.org/
published by the Foundation for Open Access Statistics
http://www.foastat.org/
November 2019, Volume 91, Issue 11
Submitted: 2017-03-07
doi:10.18637/jss.v091.i11
Accepted: 2018-03-08