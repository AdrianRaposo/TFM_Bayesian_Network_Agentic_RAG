# Corrected score methods for estimating Bayesian networks with error-prone nodes 

Xianzheng Huang*1, Hongmei Zhang ${ }^{2}$<br>${ }^{1}$ Department of Statistics, University of South Carolina, Columbia, SC 29208, U.S.A.<br>${ }^{2}$ Division of Epidemiology, Biostatistics, and Environmental Health,<br>University of Memphis, Memphis, TN 38111, U.S.A.<br>*huang@stat.sc.edu


#### Abstract

Motivated by inferring cellular signaling networks using noisy flow cytometry data, we develop procedures to draw inference for Bayesian networks based on error-prone data. Two methods for inferring causal relationships between nodes in a network are proposed based on penalized estimation methods that account for measurement error and encourage sparsity. We discuss consistency of the proposed network estimators and develop an approach for selecting the tuning parameter in the penalized estimation methods. Empirical studies are carried out to compare the proposed methods and a naive method that ignores measurement error with applications to synthetic data and to single cell flow cytometry data.


Key words: False discovery rate; Frobenius norm; information criterion; specificity; topological sorting.

# 1 Introduction 

### 1.1 Motivations

The study of cellular signaling networks has been a major research area in biology for several decades. By analyzing how multiple cell signaling pathways affect each other and, in turn, cellular processes within a network, scientists gain valuable insights on normal cellular responses in a biological system, and their potential disregulation in disease (Jordan et al., 2000; Quaranta and Tyson, 2013; Madireddy et al., 2019). Statistical models that mathematically conceptualize these signaling networks have been developed, which advance experimental cell biology, and influence the way biologists view, monitor, and study signaling networks by perturbing them in designed experiments (Janes and Lauffenburger, 2013; Karamouzis and Papavassiliou, 2014).

Among these models, Bayesian networks (Jensen, 1996) have been widely adopted as an attractive model for characterizing complex cell signaling cascades. With recent advances in biochemistry, molecular biology, and cell physiology, rich data information become available at the cell level from high throughput technologies. For example, flow cytometry is an important tool in a broad range of biological and clinical research, which makes measuring physical and chemical characteristics of cells possible. This technology produces abundant data that can be used to infer cellular signalling networks (Sachs et al., 2005; Friedman et al., 2008; Shojaie and Michailidis, 2010; Luo and Zhao, 2011; Fu and Zhou, 2013). However, measurement errors in flow cytometry data inevitably arise from imperfect measurements, photon-counting statistics, and data storage methods (Roederer, 2001; Petrunkina and Harrison, 2010; Tiberi et al., 2018; Galbusera et al., 2019). This motivates our study presented in this article, where we develop methods for inferring Bayesian networks representing cellular signaling networks using error-prone flow cytometry data.

The proposed methods can be used to infer Bayesian networks arising in other applications, such as for constructing social networks based on survey data subject to imperfect respondent recall (Wang et al., 2012), studying connectivity and association between different regions of one's brain in the default mode network using preprocessed noisy brain image data (Li et al., 2013), and modeling gene regulatory pathways using gene expression data that are prone to measurement error due to experimental errors (Ma et al., 2006), stray background signal irrelevant to mRNA transcripts (Strimmer, 2003), or data normalization (Evans et al., 2016). It is thus instructive to have an overview of literature on networks and network inference in a general context next.

# 1.2 Literature Review 

Networks, or graphs, have been a topic of great interest that started mostly in the artificial intelligence community (Jensen, 1996; Neapolitan, 2012; Pearl, 2014). Later its application became more widespread, motivating statistical research on graphical models used in biology, genetics, social science, and physics (Lauritzen, 1996; Edwards, 2012). A network consists of a set of nodes, also referred to as vertices or variables, and a set of edges connecting nodes. Graphs with undirected edges are called undirected graphs. In an undirected graph, a set of nodes connecting to a particular node form a neighborhood of this node. Given its neighborhood, this node is independent of nodes outside of the neighborhood. This type of graphs is useful for characterizing correlations between nodes. When causal relationships are of interest, directed edges are used, giving rise to the so-called directed acyclic graphs (DAG). Pairing such a graph with a joint probability distribution of all nodes produces a Bayesian network. When there is an edge pointing from one node to another node, these two nodes are referred to as a parent node (of the latter) and a child node (of the former), respectively. Given its parents, a node is independent of its non-descendant nodes, which is

more formally known as the local Markov property of DAG. In this sense, a Bayesian network encodes the joint distribution of the set of nodes in the graph. Provided with this encoding, not only can one uncover the correlation structure among nodes, but one can also reveal if a correlation between two nodes is due to a direct causal relationship between them or an indirect dependence mediated by other nodes. The latter piece of information is especially of interest in biology and genetics (Friedman et al., 2000). Because of this, some researchers refer to Bayesian networks as causal networks to signify causality as their research focal point, as in our motivating study of cellular signaling networks.

There is a large collection of works on inferring Bayesian networks. Many existing works follow the theme of search-and-score (Suzuki, 1993; Heckerman et al., 1995; Xiang et al., 1997; Friedman et al., 1999; Chickering, 2002; Moore and Wong, 2003; Bartlett and Cussens, 2017; Correia et al., 2019). Following this theme, one formulates a scoring criterion, and searches for a directed graph, or an equivalent class of directed graphs (Andersson et al., 1997), that optimizes the score. The score can be constructed based on a likelihood function of observed data in the frequentist framework (Shojaie and Michailidis, 2010); it can also originate from a posterior distribution of a graph in the Bayesian framework (Heckerman et al., 1995). Scores formulated borrowing these two schools of statistics have also been used, such as the Bayesian Dirichlet equivalent uniform score defined as the log likelihood of the observed data given suitably chosen Dirichlet priors over the parameters of a network structure (Correia et al., 2019). When the number of nodes is large, scores designed to penalize complexity of a graph are often employed (Alon et al., 1995; Van de Geer et al., 2013). Another well explored theme for inferring Bayesian networks leads to the constraintbased approaches that involve testing conditional independence among nodes (Spirtes and Glymour, 1991; Spirtes et al., 2000). To lessen the computational burden in the presence of many nodes, Tsamardinos et al. (2006) proposed the max-min hill-climbing algorithm

that combines ideas from search-and-score, constraint-based approaches, and local learning. Friedman and Koller (2003) used a Markov chain Monte Carlo (MCMC) method over the space of node orders, which is smaller and more regular than the space of graph structures. Eaton and Murphy (2012) suggested to apply dynamic programming algorithm on the space of node orders, then used the resultant proposal distribution for MCMC methods in the DAG space. Also considering the order space, Ellis and Wong (2008) developed a fast MCMC algorithm based on data that include interventional data and observational data. Ye et al. (2019) proposed to minimize a regularized Cholesky score over the space of topological orderings and achieved improved performance in network structure learning compared with several competing methods when applied to both observational and interventional data. Interventional data arise from intervention experiments, such as flow cytometry experiments considered in our study. In such an experiment, one forces the values of some node(s) to be certain values, which in effect destroys the causal dependencies of the intervened node(s). Inclusion of interventional data greatly improves the identifiability of a Bayesian network, as Hauser and Bühlmann (2012) explained in great detail.

All aforementioned existing works rely on observed data as precise measures of nodes. But, as seen in the motivating examples, measures of nodes can be imprecise. For flow cytometry experiments, Galbusera et al. (2019) showed that flow cytometry measurements contain a significant amount of shot-noise that can be easily mistaken for true biological variability. Although measurement error problems have been long investigated in many regression settings (Carroll et al., 2006; Fuller, 2009; Grace, 2016), there is very limited research in the context of inferring Bayesian networks. One exception is the work by Luo and Zhao (2011), who used Bayesian hierarchical modeling to incorporate measurement error and random error that represent intrinsic noise in flow cytometry data when inferring signaling pathways. In this article, we tackle this problem from the frequentist point of view.

To the best of our knowledge, this is the first frequentist work addressing this problem.
The data structure considered in our study and mathematical formulations of the data generating mechanism are described in Section 2. We then outline the proposed penalized estimation methods in Section 3, which includes detailed algorithms for implementing the proposed methods. To choose the tuning parameter in the penalized estimation, we construct a tuning parameter selector in Section 4. In Section 5, simulation studies are reported, where we compare finite sample performance of the proposed methods and a naive method that ignores measurement error. We also apply these methods to a flow cytometry data set to infer a signaling network of immune system cells. In Section 6, we summarize the contribution of our study and discuss follow-up research.

# 2 Data and Model 

Denote by $\mathbf{X}$ the $N \times p$ (unobserved) data matrix as error-free measures of $p$ nodes in a network, including interventional data and observational data from $N$ experimental units. Refer to node $j$ as $X_{j}$, denote by $n_{j}$ and $n_{-j}$ the number of interventional data points and the number observational data points associated with $X_{j}$, respectively, and by $O_{j}$ the set of row indices corresponding to the observational data for $X_{j}$ in $\mathbf{X}$, for $j=1, \ldots, p$. The observed data matrix of the same dimension, $\mathbf{W}$, is an error-contaminated surrogate of $\mathbf{X}$.

Taking the data structure into consideration, we assume that the causal relationships of the $p$ nodes are specified by

$$
\mathbf{X}\left[O_{j}, j\right]=\mathbf{X}\left[O_{j},-j\right] \mathbf{B}_{j}+\boldsymbol{\epsilon}\left[O_{j}, j\right], \text { for } j=1, \ldots, p
$$

where $\boldsymbol{\epsilon}$ is the $N \times p$ matrix of model error representing intrinsic noise due to unmodelling variation, $\boldsymbol{\epsilon}\left[O_{j}, j\right]$ consists of $n_{-j}$ independent and identically distributed (i.i.d.) mean-zero random errors, $\mathbf{B}=\left[\beta_{i j}\right]_{i, j=1, \ldots, p}$ is the $p \times p$ matrix of regression coefficients with zero diagonal

entries, and $\mathbf{B}_{j}=\mathbf{B}[-j, j]$. The regression model representation of a Bayesian network in (1) is the same as that formulated in Fu and Zhou (2013). It is assumed that $\boldsymbol{b}=\left(\mathbf{B}_{1}^{\mathrm{T}}, \ldots, \mathbf{B}_{p}^{\mathrm{T}}\right)^{\mathrm{T}}$ is a vector of natural parameters in the sense that, given sufficient interventional data associated with each node, $\boldsymbol{b}$ is identifiable (Fu and Zhou, 2013). For $X_{j}$, the nodes on the right-handside of (1) associated with nonzero entries in $\mathbf{B}_{j}$ are parents of $X_{j}$. Having $\mathbf{B}_{j}=\mathbf{0}$ means that $X_{j}$ has no parent, and is referred to as a root node. Having the $j$ th row, $\mathbf{B}[j$,$] , as a$ zero vector implies that $X_{j}$ a childless node. Assume that $\mathbf{W}$ results from contaminating $\mathbf{X}$ with additive mean-zero normal measurement error independent of $\mathbf{X}$, that is,

$$
\mathbf{W}=\mathbf{X}+\mathbf{U}
$$

where $\mathbf{U}$ is the $N \times p$ matrix of nondifferential measurement error (Carroll et al., 2006, Section 2.5). It is further assumed in this study that, for each node $X_{j}$, the measurement error associated with the interventional data of $X_{j}$ and the measurement error associated with the observational data of $X_{j}$ follow the same distribution. This implies that $\{\mathbf{U}[\ell,]\}_{\ell=1}^{N}$ are i.i.d. random vectors from $N_{p}\left(\mathbf{0}, \boldsymbol{\Sigma}_{u}\right)$, where $\boldsymbol{\Sigma}_{u}$ is the $p \times p$ variance-covariance matrix of the measurement error associated with nodes $\left(X_{1}, \ldots, X_{p}\right)$.

According to (1) and (2), the Bayesian network with error-prone nodes consists of $p$ hierarchical measurement error models, with the $j$ th hierarchical model consisting of two submodels,

$$
\begin{aligned}
\mathbf{W}\left[O_{j}, j\right] & =\mathbf{X}\left[O_{j},-j\right] \mathbf{B}_{j}+\boldsymbol{\epsilon}\left[O_{j}, j\right]+\mathbf{U}\left[O_{j}, j\right] \\
\mathbf{W}\left[O_{j},-j\right] & =\mathbf{X}\left[O_{j},-j\right]+\mathbf{U}\left[O_{j},-j\right]
\end{aligned}
$$

where the first submodel is for the error-contaminated node $j$ regressing on the remaining $p-1$ error-free nodes, and the second submodel relates the observed covariates with the true covariates in the $j$ th regression model, for $j=1, \ldots, p$. Given the set of $p$ measurement error models, making inference for an underlying Bayeisan network that relates the $p$ nodes mainly

involves inferring $\mathbf{B}$ using $\mathbf{W}$. The variance-covariance associated with $\boldsymbol{\epsilon}\left[O_{j}, j\right]$ does not need to be estimated for the proposed methods. Estimating $\boldsymbol{\Sigma}_{u}$ requires either external validation data or replicate measures of the same set of error-free measures of nodes. For instance, it has been a routine practice in the measurement error literature that, with replicate measures on the true covariates, one can use equation (4.3) in Carroll et al. (2006) to estimate $\boldsymbol{\Sigma}_{u}$, which usually has little impact on the final inference on regression parameters. In order to focus on inference on $\mathbf{B}$, we assume $\boldsymbol{\Sigma}_{u}$ known in this study.

# 3 Estimation of B 

### 3.1 Penalized Objective Functions

When $\mathbf{X}$ is observed, Fu and Zhou (2013) proposed to estimate $\mathbf{B}$ via minimizing a penalized log-likelihood function corresponding to the graphical model in (1). In the presence of measurement error, a naive approach for estimating $\mathbf{B}$ is to ignore measurement error and use $\mathbf{W}$ in place of $\mathbf{X}$ in the penalized log-likelihood function in Fu and Zhou (2013),

$$
R_{\mathrm{nv}}(\mathbf{B})=\sum_{j=1}^{p}\left\{V_{j, \mathrm{nv}}+\sum_{i=1}^{p} P_{\lambda}\left(\left|\beta_{i j}\right|\right)\right\}
$$

where, for $j=1, \ldots, p$,

$$
V_{j, \mathrm{nv}}=\frac{n_{-j}}{2} \log \left\{\sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\mathbf{W}[\ell,-j] \mathbf{B}_{j}\right)^{2}\right\}
$$

and $P_{\lambda}(\cdot)$ a penalty function. One may choose a penalty according to the LASSO (Tibshirani, 1996), the adaptive LASSO (ALASSO) (Zou, 2006), or the SCAD penalty (Fan and Li, 2001). Both ALASSO and SCAD have been shown to enjoy the appealing oracle properties

in variable selections. In this study we adopt SCAD in (5), defined as

$$
\begin{aligned}
P_{\lambda}(t)= & \lambda t I(t \in[0, \lambda))+\frac{\left(a^{2}-1\right) \lambda^{2}-(t-a \lambda)^{2}}{2(a-1)} I(t \in[\lambda, a \lambda)) \\
& +\frac{(a+1) \lambda^{2}}{2} I(t \geq a \lambda)
\end{aligned}
$$

in which $\lambda$ is a tuning parameter and $a=3.7$. Besides avoiding the adaptive weights required in ALASSO, our choice of the SCAD penalty is also motivated by findings in Aragam and Zhou (2015), who showed that a concave penalty, such as SCAD, offers improved performance in Bayesian network structure learning when comparing with an $L_{1}$-based penalty like LASSO. Denote the estimator of $\mathbf{B}$ by $\hat{\mathbf{B}}_{\mathrm{nv}}$, as a minimizer of (5) that induces a DAG.

To account for measurement error in node data, we construct a penalized objective function based on the corrected score function (Nakamura, 1990). Assuming normal model error and measurement error, the corrected score function associated with the $j$ th measurement error model is given by

$$
\begin{aligned}
\boldsymbol{\Psi}_{j}\left(\mathbf{B}_{j}\right) & =\sum_{\ell \in O_{j}} \boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right) \\
& =\sum_{\ell \in O_{j}}\left\{\left(\mathbf{W}[\ell, j]-\mathbf{W}[\ell,-j] \mathbf{B}_{j}\right) \mathbf{W}[\ell,-j]^{t}+\boldsymbol{\Sigma}_{u}[-j,-j] \mathbf{B}_{j}\right\}
\end{aligned}
$$

When $\boldsymbol{\Sigma}_{u}=\mathbf{0}$, the summand in (7), $\boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right)$, reduces to the score used in the least squared method for estimating the regression coefficients in the $j$ th regression model, for $j=1, \ldots, p$. In the presence of measurement error, one can show that $E\left\{\boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}^{*}\right)\right\}=\mathbf{0}$ (Carroll et al., 2006, Section A.6), where $\mathbf{B}_{j}^{*}$ is the truth of $\mathbf{B}_{j}$, for $\ell \in O_{j}$ and $j=1, \ldots, p$. In other words, the corrected score $\boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right)$ is an unbiased score that corrects the score used in the least squared method for measurement error.

For each $j \in\{1, \ldots, p\}$, we follow the construction of quadratic inference functions ( Qu

et al., 2000) and propose the penalized score-based objective function given by

$$
R(\mathbf{B})=\sum_{j=1}^{p}\left\{V_{j}+\sum_{i=1}^{p} P_{\lambda}\left(\left|\beta_{i j}\right|\right)\right\}
$$

where

$$
V_{j}=\left\{\frac{1}{n_{-j}} \sum_{\ell \in O_{j}} \boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right)\right\}^{t}\left\{\mathbf{H}_{j}\left(\mathbf{B}_{j}\right)\right\}^{-1}\left\{\frac{1}{n_{-j}} \sum_{\ell \in O_{j}} \boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right)\right\}
$$

in which $\mathbf{H}_{j}\left(\mathbf{B}_{j}\right)=n_{-j}^{-1} \sum_{\ell \in O_{j}} \boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right) \boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right)^{t}$ is a consistent estimator of the variancecovariance matrix of the corrected score, which is "sandwiched" between the scores to achieve optimality in efficiency of the score-based inference (Hansen, 1982). A non-naive estimator of $\mathbf{B}$, denoted by $\hat{\mathbf{B}}$, is a minimizer of $R(\mathbf{B})$.

In Appendix A of the Supplementary Materials, we establish the consistency of the estimator as a minimizer of (8) with a fixed $p$ under regularity conditions. The conclusion is summarized in the following theorem.
Theorem 3.1 Under assumptions (A1)-(A5) in Appendix A, as $n=\min _{1 \leq j \leq p} n_{-j} \rightarrow \infty$, if $\sqrt{n} \lambda_{n}=o_{p}(1)$, then there exists a local minimizer of $R(\mathbf{B})$ defined in (8), denoted by $\hat{\mathbf{B}}$, such that $\left\|\hat{\boldsymbol{b}}-\boldsymbol{b}^{*}\right\|=O_{p}\left(n^{-1 / 2}\right)$, where $\lambda_{n}$ is the tuning parameter $\lambda$ in (8) with the added subscript $n$ to signify its dependence on $n$ in the discussion of asymptotics, $\boldsymbol{b}^{*}=\left(\mathbf{B}_{1}^{\mathrm{ex}}, \ldots, \mathbf{B}_{p}^{\mathrm{ex}}\right)^{\mathrm{T}}$, in which $\mathbf{B}_{j}^{*}=\mathbf{B}^{*}[-j, j]$, for $j=1, \ldots, p$, and $\mathbf{B}^{*}$ is the true value of $\mathbf{B} ; \hat{\boldsymbol{b}}$ is similarly defined from $\hat{\mathbf{B}}$.

# 3.2 Algorithms for Estimating B 

To find a minimizer of the penalized log-likelihood, Fu and Zhou (2013) developed a pairwise coordinate descent (PCD) algorithm to iteratively update each of the $p(p-1) / 2$ pairs, $\left(\beta_{i j}, \beta_{j i}\right)$, for $i \neq j=1, \ldots, p$, with all other entries of $\mathbf{B}$ fixed at their values from the preceding iteration. The algorithm is designed to avoid estimates for $\beta_{i j}$ and $\beta_{j i}$ to be nonzero

simultaneously, since $\beta_{i j}$ and $\beta_{j i}$ both being nonzero is a violation of acyclicity. But PCD cannot avoid other forms of acyclicity violation. To thoroughly check for cycles in an estimated regression coefficients matrix, we implement Kahn's topological sorting algorithm (Kahn, 1962) along with PCD.

Given a directed graph structure $G$, a topological sorting algorithm is an iterative procedure that yields a sorted sequence of nodes such that a child node always comes after its parent nodes, thus provides an order of these nodes compatible with $G$. A topological sorting algorithm can be used to detect cycles because a topological ordering of nodes does not exist as long as there exists a cycle in the graph (Cormen et al., 2001). In particular, Kahn's sorting algorithm is developed based on the fact that a DAG must have at least one root node; moreover, removing root nodes and their out-going edges from a DAG always yields a subgraph that is still a DAG. Hence, an early termination of the sorting algorithm will only occur if a subgraph at that step has no root node, which directly indicates existence of at least one cycle in the subgraph, and thus in the original graph as well. When this occurs, we will strategically remove edges until root nodes emerge so that the sorting algorithm can resume. Figure 1 illustrates the application of Kahn's sorting algorithm for the purpose of cycle detection and elimination for an initial graph structure as the input of the algorithm. The output of the depicted algorithm is an order compatible with the resultant acyclic graph indicated by a queue of $p$ nodes, denoted by $\mathscr{T}$, which starts as an empty queue at the beginning of the algorithm, and stores the root nodes of the graph and subgraphs created during the iterative procedure.

In Figure 1, the weakest edge in $G$ mentioned in the middle gray-shaded box corresponds to the edge associating with an estimated regression coefficient that indicates the weakest association between two nodes connected by this edge among all associations between connected pairs of nodes. We use $p$-values of the estimated regression coefficients to identify the

![img-0.jpeg](img-0.jpeg)

Figure 1: Kahn's topological sorting algorithm for eliminating cycles in $G$ and finding a topological ordering, $\mathscr{T}$, compatible with the resultant acyclic graph.
weakest edge to be removed until the sorting algorithm resumes due to newly emerging root nodes. By the time the queue $\mathscr{T}$ collects all $p$ nodes, we obtain a final regression coefficient matrix estimate by placing zeros in the entries corresponding to the removed weak edges.

A complete algorithm for finding a minimizer of the penalized score-based objective function $R(\mathbf{B})$ in (8) that corresponds to a DAG is related next, which uses the PCD algorithm in conjunction with Kahn's sorting algorithm.

Step 1: Obtain an initial estimate of $\mathbf{B}$ by solving $p$ unpenalized corrected score estimating equations one at a time. Denote by $\hat{\mathbf{B}}^{(0)}$ the resultant initial estimate of $\mathbf{B}$. Set the iteration index $t=0$.

Step 2: For $i \neq j=1, \ldots, p$, define $\tilde{\beta}_{i j}=\hat{\mathbf{B}}^{(t)}[i, j]$ and $\tilde{\beta}_{j i}=\hat{\mathbf{B}}^{(t)}[j, i]$. For each pair of nodes $i$ and $j$, update $\left(\tilde{\beta}_{i j}, \tilde{\beta}_{j i}\right)$ to $\left(\tilde{\beta}_{i j}^{*}, \tilde{\beta}_{j i}^{*}\right)$ by minimizing the penalized scorebased objective function following the algorithm elaborated in Appendix B of the

Supplementary Materials. Set $\hat{\mathbf{B}}^{(t+1)}=\left[\tilde{\beta}_{i j}^{*}\right]_{i, j=1, \ldots, p}$. Denote by $\tilde{G}$ the graph structure indicated by $\hat{\mathbf{B}}^{(t+1)}$, which may not be a DAG.

Step 3: For $j=1, \ldots, p$, compute unpenalized corrected score estimates for regression coefficients associated with the parents of $X_{j}$ suggested by $\tilde{G}$. Obtain estimated standard errors associated with these unpenalized regression coefficients estimates via sandwich variance estimation for M-estimators. Produce $p$-values based on the corrected score estimate for $\beta_{i j}$ and its estimated standard error for testing $H_{0}: \beta_{i j}=0$ versus $H_{1}: \beta_{i j} \neq 0$, if $X_{i}$ is a parent of $X_{j}$ in $\tilde{G}$.

Step 4: Implement Kahn's sorting algorithm to eliminate cycles in $\tilde{G}$ by setting some (initially nonzero in Step 3) coefficients in $\hat{\mathbf{B}}^{(t+1)}$ to be zero that have the largest $p$-values, unless $\tilde{G}$ from Step 3 is a DAG.

Step 5: If $\left|\hat{\mathbf{B}}^{(t+1)}-\hat{\mathbf{B}}^{(t)}\right|_{\infty}>10^{-4}$, set $t=t+1$, and return to Step 2. Otherwise, output $\hat{\mathbf{B}}^{(t+1)}$ as a minimizer of $R(\mathbf{B})$ that corresponds to a DAG. Here, for a matrix $\mathbf{A},|\mathbf{A}|_{\infty}$ denotes the largest entry of $\mathbf{A}$ in absolute value.

One can follow a similar algorithm described above to find the miminizer of the naive penalized log-likelihood function $R_{\mathrm{nv}}(\mathbf{B})$ in (5) that relates to a DAG. This is elaborated in Appendix C of the Supplementary Materials, where formulas for updating each pair of regression coefficients in Step 2 are provided. The algorithm implemented in Fu and Zhou (2013) to minimize their penalized log-likelihood function using error-free data does not include Steps 3 and 4 above and thus does not guarantee to return a DAG in the end.

When implementing the PCD algorithm, one essentially considers one pair of regression models at a time in each iteration, which are the $j$ th and the $i$ th regression models, that is, the regression model with $X_{j}$ as the response and the one with $X_{i}$ as the response, respectively. For each pair of models, one focuses on inferring one regression coefficient

in each model in that iteration. In particular, one infers if $X_{i}$ should be included as an influential covariate in the $j$ th regression model or if $X_{j}$ should be an influential covariate in the $i$ th regression model, given all other covariates chosen from the previous iteration for that model. Alternatively, instead of updating $\hat{\mathbf{B}}^{(t)}$ one pair of entries at a time, one may update one column of $\hat{\mathbf{B}}^{(t)}$ at a time by selecting important covariates for the $j$ th regression model, for $j=1, \ldots, p$. This leads to another approach for estimating $\mathbf{B}$ that follows a similar algorithm but with the following step replacing Step 2 above:

Step $2^{*}$ : For $j=1, \ldots, p$, use $\hat{\mathbf{B}}_{j}^{(t)}$ as the starting value to solve the following penalized score estimating equation,

$$
n_{-j}^{-1} \sum_{\ell \in O_{j}} \boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right)-\tilde{P}_{\lambda}\left(\mathbf{B}_{j}\right)=\mathbf{0}
$$

where $\tilde{P}_{\lambda}\left(\mathbf{B}_{j}\right)$ is a $(p-1) \times 1$ vector with entries given by, for $k \neq j$,

$$
\frac{\partial}{\partial \beta_{k j}} P_{\lambda}\left(\left|\beta_{k j}\right|\right)=\lambda\left\{I\left(\left|\beta_{k j}\right| \leq \lambda\right)+\frac{\left(a \lambda-\left|\beta_{k j}\right|\right)_{+}}{(a-1) \lambda}\right\} \operatorname{sign}\left(\beta_{k j}\right)
$$

Let the resultant $p$ sets of solutions as the $p$ columns in the updated estimated $\mathbf{B}$, $\hat{\mathbf{B}}^{(t+1)}$. Denote by $\tilde{G}$ the graph structure indicated by $\hat{\mathbf{B}}^{(t+1)}$.

We use Newton-Raphson algorithm to solve (10), where the derivative of $\tilde{P}_{\lambda}\left(\mathbf{B}_{j}\right)$ is approximated by a $(p-1) \times(p-1)$ diagonal matrix whose diagonal entries are given by $I\left(\beta_{k j} \neq 0\right)\left|\left(\partial / \partial \beta_{k j}\right) P_{\lambda}\left(\left|\beta_{k j}\right|\right)\right| /\left|\beta_{k j}\right|$, for $k \neq j$. This is also the local quadratic approximation used in Fan and Li (2001). We refer to this algorithm as the node-wise parent selection (NPS) algorithm to distinguish from the previous algorithm that involves PCD.

For each node, the NPS algorithm in Step $2^{*}$ is precisely the algorithm proposed by Huang and Zhang (2013) for variable selection in one linear regression model with errorprone covariates. Consistency of this method for one regression model is established by the

authors. Hence, without considering the correlation between $p$ regression models that the Bayesian network decomposes into, we expect that this alternative algorithm can yield a sensible estimate for $\mathbf{B}$ that ignores the acyclicity constraint, and the cycle detection and elimination in Step 3 allows one to impose this constraint on the output of the NPS algorithm. Putting the penalty term aside, solving the $p$ sets of penalized score estimation equations in (10) is intrinsically related to minimizing the penalized score-based objective function in (8) since they both originate from the corrected score.

# 4 Tuning Parameter Selection 

We are now in the position to discuss choices of the tuning parameter $\lambda$ in the penalized score-based objective function in (8) and the penalized score estimating equation in (10). In principle, it is desirable to use a consistent information criterion to choose $\lambda$. Assume that the class of candidate models includes a true model which the observed data come from, then a consistent information criterion refers to a criterion approaching (in probability) to its optimal value as the sample size tends to infinity when evaluated at the true model. In the context of variable selection in a regression model, within the class of all candidate models, a correct model includes all truly influential predictors in the true model and may also include non-influential predictors; the rest are incorrect models, which are referred to as underfitted models. In other words, the true model is the most parsimonious correct model, and a correct model that is not the true model is an overfitted model. Hence, with probability tending to one as the sample size increases, a consistent information criterion evaluated at the true model reaches its optimal value compared to when it is evaluated at an overfitted or underfitted model.

To infer a Bayesian network consisting of error-prone nodes, we propose the score-based

information criterion evaluated at a graph $G$ given by

$$
\operatorname{SIC}(G)=\sum_{j=1}^{p}\left(\hat{V}_{j}+e_{j} \frac{\log n_{-j}}{n_{-j}}\right)
$$

where $e_{j}$ is the number of parents of $X_{j}$ according to $G$, and $\hat{V}_{j}$ is equal to $V_{j}$ evaluated at the unpenalized corrected score estimate of $\mathbf{B}_{j}$ given the structure of $G$. In the context of linear regression with error-prone covariates, Huang and Zhang (2013) developed two score-based information criteria very much in the same spirit as the summand in (11) to facilitate variable selection in one regression model. The proposed information criterion in (11) is essentially the sum of $p$ score-based information criteria associated with $p$ regression models as the decomposition of a Bayesian network. To establish its consistency as a model criterion, it is instructive to relate arguments for model selection in the context of one regression model to arguments for graph selection, where a graph can be decomposed into $p$ regression models.

Denote by $\mathbf{E}_{G}$ the set of directed edges in $G$, and by $\left|\mathbf{E}_{G}\right|$ the size of this set. Suppose there exists a true graph $G_{0}$ in the class of graphs under consideration, which dictates the data generating process. Parallel with notions in variable selection in the regression setting, let $G_{-}$and $G_{+}$denote generically an underfitted graph and an overfitted graph, respectively, where $G_{-}$satisfies $\mathbf{E}_{G_{0}} \not \subset \mathbf{E}_{G_{-}}$, and $G_{+}$satisfies $\mathbf{E}_{G_{0}} \subset \mathbf{E}_{G_{+}}$. Then $G_{0}$ and $G_{+}$are correct graphs, with the former more parsimonious than the latter, that is, $\left|\mathbf{E}_{G_{0}}\right|<\left|\mathbf{E}_{G_{+}}\right|$. In contrast, $G_{-}$is an incorrect graph, and one does not necessarily have $\left|\mathbf{E}_{G_{-}}\right|<\left|\mathbf{E}_{G_{0}}\right|$. To establish the consistency of $\operatorname{SIC}(G)$, it suffices to show that

$$
\begin{array}{ll}
\operatorname{SIC}\left(G_{-}\right)-\operatorname{SIC}\left(G_{0}\right) \quad>0 & \text { with probability approaching one, as } n \rightarrow \infty \text { and, } \\
\operatorname{SIC}\left(G_{+}\right)-\operatorname{SIC}\left(G_{0}\right) \rightarrow 0^{+} & \text { in probability as } n \rightarrow \infty
\end{array}
$$

where $n=\min _{1 \leq j \leq p} n_{-j}$. These assertions are proved in Appendix D of the Supplementary Materials, where $p$ is allowed to diverge as $n \rightarrow \infty$.

# 5 Empirical Evidence 

### 5.1 Competing Methods

In this section, we implement the proposed score-based methods and the naive likelihoodbased method using simulated network data to assess their finite sample performance. For the score-based methods, we use the SIC tuning parameter selector to choose $\lambda$. For the naive method, we adopt the tuning parameter selection method employed in Fu and Zhou (2013) based on the relative change in the prediction error.

Denote by $e_{\lambda}$ the number of edges of an estimated graph when the tuning parameter is set at $\lambda$, and by $\hat{\mathbf{B}}_{\mathrm{nv}}^{(\lambda)}$ the corresponding naive estimate of $\mathbf{B}$. Define the prediction error by $\mathrm{PE}_{\lambda}=\sum_{j=1}^{p} \sum_{\ell \in O_{j}}(\mathbf{W}[\ell, j]-\hat{\mathbf{W}}^{(\lambda)}[\ell, j])^{2}$, where $\hat{\mathbf{W}}^{(\lambda)}[\ell, j]=\mathbf{W}[\ell,-j] \hat{\mathbf{B}}_{\mathrm{nv}, j}^{(\lambda)}$. Suppose one considers $m$ candidate values for $\lambda, \lambda_{1}>\lambda_{2}>\ldots>\lambda_{m}$. For each $k=2, \ldots, m$, one computes the relative change in prediction error defined by $\mathrm{RCP}_{k-1, k}=\left(\mathrm{PE}_{\lambda_{k-1}}-\mathrm{PE}_{\lambda_{k}}\right) /\left(e_{\lambda_{k}}-e_{\lambda_{k-1}}\right)$, if $e_{\lambda_{k}}-e_{\lambda_{k-1}}>0$, and $\mathrm{RCP}_{k-1, k}=0$ otherwise. Then one chooses $\lambda_{K}$ as the tuning parameter value, where $K=\max \left\{k: \mathrm{RCP}_{k-1, k} \geq \alpha \max \left(\mathrm{RCP}_{1,2}, \ldots, \mathrm{RCP}_{m-1, m}\right), k=2, \ldots, m\right\}$, in which $\alpha$ is a threshold parameter set at 0.1 in our simulation study. The quantity defined as $\mathrm{RCP}_{k-1, k}$ essentially quantifies how much one gains in prediction accuracy at the price of increasing graph complexity (as $e_{\lambda}$ increases) when one drops $\lambda$ from $\lambda_{k-1}$ to $\lambda_{k}$. The use of the threshold $\alpha$ is to further guard again overly dense graphs. The constructions of RCP and $K$ together aim to balance graph complexity and prediction accuracy.

In summary, there are three methods implemented in the simulation study: the naive likelihood-based method using the PCD algorithm with $\lambda$ chosen by RCP, the score-based method using the PCD algorithm with $\lambda$ chosen by SIC, and the score-based method using the NPS algorithm with $\lambda$ chosen by SIC.

# 5.2 Simulation Settings 

The simulation experiment involves two factors: the number of nodes $p$ and the variancecovariance matrix of the measurement error $\boldsymbol{\Sigma}_{u}$. There are two levels for $p, 10$ and 20. Given $p$, the total number of edges of a true graph is set to be $3 p$, and each node has at most four parents. Once such a graph is created randomly, we set the entries in $\mathbf{B}$ associated with the first half of edges at 0.5 , and entries associated with the second half of edges at 1 . Then we generate $n_{j}=5$ interventional data points from $N(0,1)$, for $j=1, \ldots, p$. When generating normal measurement errors, we first set $\boldsymbol{\Sigma}_{u}=\sigma_{u}^{2} \mathbf{I}_{p}$, where $\sigma_{u}^{2}$ varies across 5 levels to produce reliability ratio associated with each $X_{j}$, defined by $\tau=\operatorname{Var}\left(X_{j}\right) /\left\{\operatorname{Var}\left(X_{j}\right)+\sigma_{u}^{2}\right\}$, ranging from 0.8 to 1 at increments of 0.05 , for $j=1, \ldots, p$. In a different setting we let $\boldsymbol{\Sigma}_{u}=\sigma_{u}^{2} \mathbf{V}_{p}$, where $\sigma_{u}^{2}$ takes the five aforementioned levels, and $\mathbf{V}_{p}$ is a $p \times p$ matrix with entries given by $\mathbf{V}_{p}\left[j, j^{\prime}\right]=0.5^{\left|j-j^{\prime}\right|}$, for $j, j^{\prime}=1, \ldots, p$. For each simulation setting, we randomly generate ten graphs, from each of which an $N \times p$ data matrix $\mathbf{W}$ is generated according to (3) and (4) with $\{\boldsymbol{\epsilon}[\ell, j], \ell=1, \ldots, N\}_{j=1}^{p}$ being independent realizations from $N(0,1)$.

Given a true graph $G$, the following five metrics are used to assess the quality of an estimated graph $\hat{G}$ : the true positive rate, $\operatorname{TPR}=\left|\mathbf{E}_{\hat{G}} \cap \mathbf{E}_{G}\right| /(3 p)$; the false discovery rate, $\operatorname{FDR}=\left(\mathrm{R}+\left|\mathbf{E}_{\hat{G}} \cap \mathbf{E}_{G}^{c}\right|\right) /\left|\mathbf{E}_{\hat{G}}\right|$, where R denotes the number of edges in $G$ that show up in $\hat{G}$ in the reversed direction; the specificity $=\left|\mathbf{E}_{\hat{G}}^{c} \cap \mathbf{E}_{G}^{c}\right| /\{p(p-4)\}$, where $p(p-4)=p^{2}-p-3 p$ is the number of zero non-diagonal entries in $\mathbf{B}$; the rate of correct identification of existence (with the right direction) and non-existence of edges defined as $\left(\left|\mathbf{E}_{\hat{G}} \cap \mathbf{E}_{G}\right|+\left|\mathbf{E}_{\hat{G}}^{c} \cap \mathbf{E}_{G}^{c}\right|\right) /\{p(p-1) / 2\}$; and lastly, the Frobenius norm of $\mathbf{B}-\hat{\mathbf{B}}$ divided by the number of off-diagonal entries of $\mathbf{B}$, that is, $\operatorname{trace}\left\{(\mathbf{B}-\hat{\mathbf{B}})(\mathbf{B}-\hat{\mathbf{B}})^{\mathrm{T}}\right\} /\{p(p-1)\}$. The first four metrics are of interest when one is concerned about inference on the graph structure, and the last metric is of interest when one wishes to understand the strength of associations between nodes, and to use the estimated graph for prediction.

# 5.3 Simulation Results 

Figure 2 depicts the Monte Carlo (MC) averages (across ten graphs) of TPR, FDR, specificities, and rates of correct identification of existence/non-existence of directed edges associated with three considered methods when $p=10$ under two specifications of $\boldsymbol{\Sigma}_{u}$. Figure 3 shows the same collection of results when $p=20$. Across these four metrics, the advantages of the score-based methods pairing with the SIC tuning parameter selector are evident over a wide range of reliability ratio $\tau$, whether the PCD algorithm is used for implementing the corrected score method, or the NPS algorithm is used. The naive likelihood-based method suffers from low TPR, although it is comparable with the score-based methods in terms of specificity. This phenomenon can be explained by the well-known attenuation effect of measurement error on slope parameters estimates in a linear regression model with classical measurement error in covariates (Fuller, 2009, Section 1.1). More specifically, in the context of linear regression with covariates measurement error, naive estimators of covariate effects tend to attenuate towards zero, which explains the low TPR. Such attenuation effect does not compromise naive estimation of a null covariate effect, which explains the robustness of specificity to measurement error. As a combination of TPR and specificity, the correction rate observed for the naive method is also less affected by measurement error than TPR alone. This robustness is more evident in a sparser graph, such as a graph consisting of $p=20$ nodes with $3 p$ edges when comparing with a graph consisting of $p=10$ nodes with $3 p$ edges. Here, a measure of sparsity of a graph $G$ can be defined as $\left|\mathbf{E}_{G}\right| /\{p(p-1) / 2\}$, where $p(p-1) / 2$ is the largest number of edges possible for a DAG with $p$ nodes. Finally, even in the absence of measurement error (i.e., with $\tau=1$ in Figures 2 and 3), the two score-based methods still outperform the likelihood-based method when TPR and correction rate are considered. This implies that the construction of the (unpenalized) objective function plays an important role in network inference.

Figure 4 shows MC medians of the Frobenius norm of $\mathbf{B}-\hat{\mathbf{B}}$ divided by $p(p-1)$. This figure suggests that the PCD algorithm can lead to some numerical instability for the corrected score method, and the NPS algorithm produces more stable regression coefficients estimates from the corrected score method that are also less biased than the naive estimates. In fact, between the two score-based methods, the one using the NPS algorithm yields better inference outcomes in all aspects depicted in Figures 2-4 than those resulting from the PCD algorithm. This suggests that there may exist some interaction effect of regression coefficients estimation and cycle elimination procedure on the finite sample performance of a method.

![img-1.jpeg](img-1.jpeg)

Figure 2: Monte Carlo averages of TPR, FDR, specificity, and correctness rate versus the reliability ratio $\tau$ across ten graphs with $p=10$ nodes associated with three methods, the method by Fu and Zhou (2013) (dash-dotted lines), corrected score method using PCD algorithm (dashed lines), and corrected score method using NPS algorithm (solid lines), when $\boldsymbol{\Sigma}_{u}$ is a diagonal matrix (top panels) and when it is not a diagonal matrix (bottom panels).

![img-2.jpeg](img-2.jpeg)

Figure 3: Monte Carlo averages of TPR, FDR, specificity, and correctness rate versus the reliability ratio $\tau$ across ten graphs with $p=20$ nodes associated with three methods, the method by Fu and Zhou (2013) (dash-dotted lines), corrected score method using PCD algorithm (dashed lines), and corrected score method using NPS algorithm (solid lines), when $\boldsymbol{\Sigma}_{u}$ is a diagonal matrix (top panels) and when it is not a diagonal matrix (bottom panels).

# 5.4 Application to Flow Cytometry Data 

Now we return to the application of inferring cellular signaling networks using flow cytometry data. In particular, the flow cytometry data we entertain in this section consist of $p=11$ phosphomolecular measurements from each of $N=7466$ human immune system cells collected in an experiment described in Sachs et al. (2005). In this experiment, a series of stimulatory cues and inhibitory interventions were imposed, producing the observed data matrix as a mixture of observational data and interventional data for the eleven phosphorylated proteins and phospholipids (see Table 1 in Sachs et al., 2005). Shojaie and Michailidis (2010) applied a penalized likelihood estimation method with LASSO and ALASSO penalty to infer the signaling network while assuming ordering of the eleven nodes known. Without assuming ordering known, Fu and Zhou (2013) applied their likelihood-based penalized estimation method on this data set to infer a directed signaling network using the PCD algorithm, also treating the data as measures of the true nodes. Luo and Zhao (2011) viewed the observed data as error-contaminated surrogates of the true protein activity levels, and assumed a normal additive measurement error, with an inverse gamma prior distribution for the measurement error variance (common for all nodes). Neither of the aforementioned methods guarantees that the inferred graph is acyclic.

Because this data do not contain replicate measures of the same underlying protein activity level, error variance is not identifiable, even with the normality assumption imposed. A widely adopted practice in the measurement error literature in this case is to carry out sensitivity analysis, where one assumes different values for the error variance to observe how inference results from a considered method vary. This exercise can be helpful for addressing the robustness of a method to the misspecification of measurement error variance. For the purpose of comparing our proposed score-based methods that account for measurement error with the naive likelihood-based method that ignores measurement error in nodes, we follow

![img-3.jpeg](img-3.jpeg)

Figure 4: Monte Carlo medians of the Frobenius norm of $\mathbf{B}-\hat{\mathbf{B}}$ divided by $p(p-1)$ versus the reliability ratio $\tau$ across ten graphs with $p=10$ nodes (top panels) and $p=20$ nodes (bottom panels) associated with three methods, the method by Fu and Zhou (2013) (dashdotted lines), corrected score method using PCD algorithm (dashed lines), and corrected score method using NPS algorithm (solid lines), when $\boldsymbol{\Sigma}_{u}$ is a diagonal matrix (left panels) and when it is not a diagonal matrix (right panels).

the viewpoint in Fu and Zhou (2013) and treat the observed phosphomolecular measurements as the intended (error-free) measures of the true nodes, whose ordering is unknown. This allows us to have benchmark inferences, based on which we are able to compare results from the two proposed methods with those from the naive method, all three applied to error-contaminated data.

We apply our score-based penalized estimation methods based on error-prone data $\mathbf{W}$ generated from contaminating $\mathbf{X}$ according to (2) with an estimated reliability ratio of 0.8 , where the variance of each node is estimated by its interventional data. The computer code for this data analysis along with the data are available in the supplementary materials. Panel (a) in Figure 5 shows a network with directed edges reflecting causal relationships between these nodes that are currently well accepted in the literature. Networks shown in panels (b)-(f) in Figure 5 include the one from Shojaie and Michailidis (2010) using the ALASSO penalty and assuming data free of measurement error with ordering known, the network from Fu and Zhou (2013) applied to $\mathbf{X}$, the naively inferred network based on $\mathbf{W}$, and two networks obtained from the corrected score methods, implemented via the PCD algorithm and via the NPS algorithm, respectively. When comparing each of the latter five networks with the consensus graph, the network from Shojaie and Michailidis (2010) includes 14 edges in the consensus network among a total of 27 edges in their inferred graph; and there are 8 edges in the consensus network included in the network from Fu and Zhou (2013), which also has a total of 27 edges. When error-prone data are used (see panels (d)-(f)), the naive method produces a very sparse graph, with merely 8 edges, among which 4 are in the consensus graph; the corrected score method implemented via the PCD algorithm leads to a much denser graph, with 37 edges, 9 of which are in the consensus graph; the corrected score method using the NPS algorithm results in a graph with 28 edges, 10 of which are in the consensus graph.

Using the consensus graph as a gold standard, the above comparisons between the six networks suggests that, when error-prone data are used for inferring a Bayesian network, the naive likelihood-based method can lead to low discovery rate, and the corrected score methods can identify more truly existing causal relationships between nodes, although using the PCD algorithm can result in a higher false discovery rate than when the NPS algorithm is used.

# 6 Discussion 

We proposed score-based methods to infer a Bayesian network using error-prone data from interventional experiments. When only observational data are available, the proposed method can be used to infer graphs within a Markov equivalence class (Andersson et al., 1997) since a graph is not identifiable using observational data only but a Markov equivalence class is. A consistent model criterion is also constructed based on the same score function for tuning parameter selection. Besides establishing the consistency in the resulting regression coefficients estimator, we also provide convincing empirical evidence to show that the proposed score-based methods can substantially outperform a naive likelihood-based method that ignores measurement error. And, even in the absence of measurement error in nodes, using a quadratic inference function constructed based on an unbiased score is more preferable than using a likelihood function to formulate a penalized objective function for network estimation. We exploit Kahn's topological sorting algorithm along with the PCD algorithm or the NPS algorithm to estimate the regression coefficients matrix, which are computationally less burdensome than many search-and-score methods that attempt to select a graph from a DAG family of size that grows super-exponentially fast as $p$ grows (Robinson, 1973). One computational hurdle remains for the proposed method when $p$ is large is the inversion of a

$(p-1) \times(p-1)$ matrix in (9). A model criterion that does not involve the inversion of a large matrix is more desirable in that case.

It is assumed that both model error in (1) and measurement error in (2) are Gaussian. When the normality assumption is violated, the corrected score in (7) may not be an unbiased score. Constructing score functions that are robust to the normality assumption and also account for measurement error is a follow-up research direction. This is also the direction one can follow to relax the linearity assumption of the regression model in (1).

![img-4.jpeg](img-4.jpeg)

Figure 5: Six signaling networks associated with the flow cytometry data set: (a) the consensus graph, (b) the estimated graph from Shojaie and Michailidis (2010) assuming ordering known, (c) the estimated graph based on $\mathbf{X}$ from Fu and Zhou (2013), (d) the estimated graph based on $\mathbf{W}$ using the naive method, (e) the estimated graph based on $\mathbf{W}$ using the corrected score method and PCD algorithm, (f) the estimated graph based on $\mathbf{W}$ using the corrected score method and NPS algorithm. In graphs (b)-(f), the inferred edges in agreement with (a) are highlighted as red dashed edges.

# Appendix A: Proof of Theorem 3.1 

Denote by $\mathbf{B}^{*}$ the true value of $\mathbf{B}$. Define $\boldsymbol{b}=\left(\mathbf{B}_{1}^{\mathrm{T}}, \ldots, \mathbf{B}_{p}^{\mathrm{T}}\right)^{\mathrm{T}}$, where $\mathbf{B}_{j}=\mathbf{B}[-j, j]$, for $j=1, \ldots, p ; \hat{\boldsymbol{b}}$ and $\boldsymbol{b}^{*}$ are similarly defined. In this appendix, we prove the following theorem.

Theorem 3.1 Under assumptions (A1)-(A5), as $n=\min _{1 \leq j \leq p} n_{-j} \rightarrow \infty$, if $\sqrt{n} \lambda_{n}=o_{p}(1)$, then there exists a local minimizer of $R(\mathbf{B})$ defined in equation (8) in the main article, denoted by $\hat{\mathbf{B}}$, such that $\left\|\hat{\boldsymbol{b}}-\boldsymbol{b}^{*}\right\|=O_{p}\left(n^{-1 / 2}\right)$.

For $j=1, \ldots, p$, we impose the following assumptions,
(A1) the truth, $\mathbf{B}_{j}^{*}$, is a solution to $\lim _{n_{-j} \rightarrow \infty} n_{-j}^{-1} \sum_{\ell \in O_{j}} E\left\{\boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right)\right\}=\mathbf{0}$;
(A2) $\lim _{n_{-j} \rightarrow \infty} n_{-j}^{-1} \sum_{\ell \in O_{j}} E\left\{\boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}^{*}\right) \boldsymbol{\Psi}_{j \ell}^{\dagger}\left(\mathbf{B}_{j}^{*}\right)\right\}$ exists and is positive definite;
(A3) $\lim _{n_{-j} \rightarrow \infty} n_{-j}^{-1} \sum_{\ell \in O_{j}} E\left\{\left.-\left(\partial / \partial \mathbf{B}_{j}^{\ell}\right) \boldsymbol{\Psi}_{j \ell}\left(\mathbf{B}_{j}\right)\right|_{\mathbf{B}_{j}=\mathbf{B}_{j}^{*}}\right\}$ exists and is positive definite;
(A4) $\lim _{n_{-j}^{-1} \rightarrow \infty} n_{-j} \sum_{\ell \in O_{j}}\left(\partial / \partial \mathbf{B}_{j}^{\mathrm{T}}\right)\left\{\left.\mathbf{H}_{j}^{-1}\left(\mathbf{B}_{j}\right) \boldsymbol{\psi}_{j \ell}\left(\mathbf{B}_{j}\right)\right\}\right|_{\mathbf{B}_{j}=\mathbf{B}_{j}^{*}}$ exists;
(A5) $E\left\{V_{j}^{(2)}\left(\mathbf{B}_{j}^{*}\right)\right\}$ is positive definite with eigenvalues uniformly bounded by a positive constant.

Recall that the penalized objective function is

$$
R(\mathbf{B})=\sum_{j=1}^{p}\left\{V_{j}\left(\mathbf{B}_{j}\right)+\sum_{i=1}^{p} P_{\lambda_{n}}\left(\left|\beta_{i j}\right|\right)\right\}
$$

To show $\left\|\hat{\boldsymbol{b}}-\boldsymbol{b}^{*}\right\|=O_{p}\left(n^{-1 / 2}\right)$, it suffices to show that, for any $\epsilon>0$, there exists a large enough positive constant $C$ such that

$$
P\left\{\inf _{\|\operatorname{vec}(\boldsymbol{u})\|=C} R\left(\mathbf{B}^{*}+n^{-1 / 2} \boldsymbol{u}\right)>R\left(\mathbf{B}^{*}\right)\right\} \geq 1-\epsilon
$$

where $\boldsymbol{u}$ is a non-random $p \times p$ matrix with zeros on the diagonal, and $\operatorname{vec}(\boldsymbol{u})=\left(\boldsymbol{u}_{1}^{\mathrm{T}}, \ldots, \boldsymbol{u}_{p}^{\mathrm{T}}\right)^{\mathrm{T}}$.

Denote by $\Pi_{j}=\{i \in\{1, \ldots, p\}: \beta_{i j}^{*} \neq 0\}$, that is, $\Pi_{j}$ is the index set corresponding to the parents of $X_{j}$, for $j=1, \ldots, p$. By the definition of $R(\mathbf{B})$, we have

$$
\begin{aligned}
& R\left(\mathbf{B}^{*}+n^{-1 / 2} \boldsymbol{u}\right)-R\left(\mathbf{B}^{*}\right) \\
= & \sum_{j=1}^{p}\left\{V_{j}\left(\mathbf{B}_{j}^{*}+n^{-1 / 2} \boldsymbol{u}_{j}\right)-V_{j}\left(\mathbf{B}_{j}^{*}\right)\right\}+\sum_{j=1}^{p} \sum_{i=1}^{p}\left\{P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}+n^{-1 / 2} u_{i j}\right|\right)-P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}\right|\right)\right\} \\
= & \sum_{j=1}^{p}\left[n^{-1 / 2}\left\{V_{j}^{(1)}\left(\mathbf{B}_{j}^{*}\right)\right\}^{\mathrm{T}} \boldsymbol{u}_{j}+0.5 n^{-1} \boldsymbol{u}_{j}^{\mathrm{T}} V_{j}^{(2)}\left(\mathbf{B}_{j}^{*}\right) \boldsymbol{u}_{j}\left\{1+o_{p}(1)\right\}\right]+ \\
& \sum_{j=1}^{p}\left[\sum_{i \in \Pi_{j}}\left\{P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}+n^{-1 / 2} u_{i j}\right|\right)-P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}\right|\right)\right\}+\sum_{i \notin \Pi_{j}}\left\{P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}+n^{-1 / 2} u_{i j}\right|\right)-P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}\right|\right)\right\}\right]
\end{aligned}
$$

where we apply the second order Taylor expansion of $V_{j}\left(\mathbf{B}_{j}^{*}+n^{-1 / 2} \boldsymbol{u}_{j}\right)$ around $\mathbf{B}_{j}^{*}$ in the first sum above; and, since $\beta_{i j}^{*}=0$ for $i \notin \Pi_{j}$, the second sum is equal to

$$
\begin{aligned}
& \sum_{j=1}^{p}\left[\sum_{i \in \Pi_{j}}\left\{P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}+n^{-1 / 2} u_{i j}\right|\right)-P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}\right|\right)\right\}+\sum_{i \notin \Pi_{j}} P_{\lambda_{n}}\left(\left|n^{-1 / 2} u_{i j}\right|\right)\right] \\
\geq & \sum_{j=1}^{p} \sum_{i \in \Pi_{j}}\left\{P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}+n^{-1 / 2} u_{i j}\right|\right)-P_{\lambda_{n}}\left(\left|\beta_{i j}^{*}\right|\right)\right\} \\
\geq & \sum_{j=1}^{p} \sum_{i \in \Pi_{j}} P_{\lambda_{n}}^{\prime}\left(\left|\beta_{i j}^{*}+n^{-1 / 2} u_{i j}\right|\right)\left(\left|\beta_{i j}^{*}+n^{-1 / 2} u_{i j}\right|-\left|\beta_{i j}^{*}\right|\right)
\end{aligned}
$$

in which the last inequality is due to the concavity of $P_{\lambda_{n}}(t)$ on $[0, \infty)$. It follows that, for a large enough $n$,

$$
\begin{aligned}
& R\left(\mathbf{B}^{*}+n^{-1 / 2} \boldsymbol{u}\right)-R\left(\mathbf{B}^{*}\right) \\
\geq & \sum_{j=1}^{p}\left[n^{-1 / 2}\left\{V_{j}^{(1)}\left(\mathbf{B}_{j}^{*}\right)\right\}^{\mathrm{T}} \boldsymbol{u}_{j}+0.5 n^{-1} \boldsymbol{u}_{j}^{\mathrm{T}} V_{j}^{(2)}\left(\mathbf{B}_{j}^{*}\right) \boldsymbol{u}_{j}\left\{1+o_{p}(1)\right\}+\right. \\
& \left.\sum_{i \in \Pi_{j}} P_{\lambda_{n}}^{\prime}\left(\left|\beta_{i j}^{*}+n^{-1 / 2} u_{i j}\right|\right) n^{-1 / 2} u_{i j} \operatorname{sgn}\left(\beta_{i j}^{*}\right)\right]
\end{aligned}
$$

where, within the summand, since $P_{\lambda_{n}}^{\prime}(t)=O_{p}\left(\lambda_{n}\right)$, the third term is of order $o_{p}\left(n^{-1}\right)$; and by assumption (A5), the second term is bounded from below by a term of the same order as $0.5 n^{-1} v_{j} C$, where $v_{j}$ is the smallest eigenvalue (which is positive) of the limit of $\mathbf{V}_{j}^{(2)}\left(\mathbf{B}_{j}^{*}\right)$ as $n \rightarrow \infty$. As for the first term of the summand in (A.13), we have

$$
\begin{aligned}
& n^{-1 / 2}\left\{V_{j}^{(1)}\left(\mathbf{B}_{j}^{*}\right)\right\}^{\mathrm{T}} \boldsymbol{u}_{j} \\
= & n^{-1 / 2} n_{-j}^{-1} \sum_{\ell \in O_{j}} \boldsymbol{\psi}_{j \ell}^{\mathrm{T}}\left(\mathbf{B}_{j}^{*}\right)\left[\mathbf{H}_{j}^{-1}\left(\mathbf{B}_{j}^{*}\right) n_{-j}^{-1} \sum_{\ell \in O_{j}}\left(\partial / \partial \mathbf{B}_{j}^{\mathrm{T}}\right) \boldsymbol{\psi}_{j \ell}\left(\mathbf{B}_{j}\right)\right|_{\mathbf{B}_{j}=\mathbf{B}_{j}^{*}}+ \\
& n_{-j} \sum_{\ell \in O_{j}}\left(\partial / \partial \mathbf{B}_{j}^{\mathrm{T}}\right)\left\{\left.\mathbf{H}_{j}^{-1}\left(\mathbf{B}_{j}\right) \boldsymbol{\psi}_{j \ell}\left(\mathbf{B}_{j}\right)\right\}\right|_{\mathbf{B}_{j}=\mathbf{B}_{j}^{*}} \boldsymbol{u}_{j}
\end{aligned}
$$

of which, by assumptions (A2)-(A4), the terms inside the square brackets altogether converge in probability to a bounded squared matrix; and, under (A1)-(A3), $\left\|n_{-j}^{-1} \sum_{\ell \in O_{j}} \boldsymbol{\psi}_{j \ell}\left(\mathbf{B}_{j}^{*}\right)\right\|=$ $O_{p}\left(n_{-j}^{-1 / 2}\right)=O_{p}\left(n^{-1 / 2}\right)$. Hence $n^{-1 / 2}\left\{V_{j}^{(1)}\left(\mathbf{B}_{j}^{*}\right)\right\}^{\mathrm{T}} \boldsymbol{u}_{j}=O_{p}\left(n^{-1}\right)$.

Combining the discussions on the three terms in (A.13), we have that, as $n \rightarrow \infty$, for a large enough $C$, the second term in (A.13) dominates the first and the third terms, thus $R\left(\mathbf{B}^{*}+n^{-1 / 2} \boldsymbol{u}\right)-R\left(\mathbf{B}^{*}\right)>0$ in probability. This proves (A.12) and thus Theorem 3.1.

# Appendix B: The PCD algorithm for the score-based 

## method

Entering Step 2 in the algorithm in Section 3.2 of the main article, one implements the PCD algorithm to update one pair of regression coefficients $\left(\beta_{i j}, \beta_{j i}\right)$ at a time by minimizing the penalized score-based objective function with all other entries in $\mathbf{B}$ fixed. More specifically, for $i \neq j=1, \ldots, p$, define $\tilde{\beta}_{i j}=\hat{\mathbf{B}}^{(t)}[i, j]$ and $\tilde{\beta}_{j i}=\hat{\mathbf{B}}^{(t)}[j, i]$, one uses the following algorithm to update $\left(\tilde{\beta}_{i j}, \tilde{\beta}_{j i}\right)$ to $\left(\tilde{\beta}_{i j}^{*}, \tilde{\beta}_{j i}^{*}\right)$ :

PCD-1: Find

$$
\tilde{\beta}_{i j}^{*}=\underset{\beta_{i j}}{\arg \min }\left\{\tilde{V}_{j}+\sum_{k \neq i, j} P_{\lambda}\left(\left|\tilde{\beta}_{k j}\right|\right)+P_{\lambda}\left(\left|\beta_{i j}\right|\right)\right\}
$$

where

$$
\tilde{V}_{j}=\left\{n_{-j}^{-1} \sum_{\ell \in O_{j}} \boldsymbol{\Psi}_{j \ell}\left(\tilde{\mathbf{B}}_{j}^{*}\right)\right\}^{t}\left\{\mathbf{H}_{j}\left(\tilde{\mathbf{B}}_{j}^{*}\right)\right\}^{-1}\left\{n_{-j}^{-1} \sum_{\ell \in O_{j}} \boldsymbol{\Psi}_{j \ell}\left(\tilde{\mathbf{B}}_{j}^{*}\right)\right\}
$$

in which $\tilde{\mathbf{B}}_{j}^{*}$ is the same as $\hat{\mathbf{B}}_{j}^{(t)}$ except that $\tilde{\beta}_{i j}$ in $\hat{\mathbf{B}}_{j}^{(t)}$ is replaced by $\beta_{i j}$. Note that $\beta_{i j}$ appears in both $\tilde{V}_{j}$ and $P_{\lambda}\left(\left|\beta_{i j}\right|\right)$.

PCD-2: Find

$$
\tilde{\beta}_{j i}^{*}=\underset{\beta_{j i}}{\arg \min }\left\{\tilde{V}_{i}+\sum_{k \neq i, j} P_{\lambda}\left(\left|\tilde{\beta}_{k i}\right|\right)+P_{\lambda}\left(\left|\beta_{j i}\right|\right)\right\}
$$

where $\tilde{V}_{i}$ is similarly defined as $\tilde{V}_{j}$ in (B.2). Note that $\beta_{j i}$ appears in both $\tilde{V}_{i}$ and $P_{\lambda}\left(\left|\beta_{j i}\right|\right)$

PCD-3: Compute

$$
\begin{aligned}
& S_{1}=\left\{\left.\tilde{V}_{i}\right|_{\beta_{j i}=0}+\sum_{k \neq i, j} P_{\lambda}\left(\left|\tilde{\beta}_{k i}\right|\right)\right\}+\left\{\left.\tilde{V}_{j}\right|_{\beta_{i j}=\tilde{\beta}_{i j}^{*}}+\sum_{k \neq i, j} P_{\lambda}\left(\left|\tilde{\beta}_{k j}\right|\right)+P_{\lambda}\left(\left|\tilde{\beta}_{i j}^{*}\right|\right)\right\} \\
& S_{2}=\left\{\left.\tilde{V}_{i}\right|_{\beta_{j i}=\tilde{\beta}_{j i}^{*}}+\sum_{k \neq i, j} P_{\lambda}\left(\left|\tilde{\beta}_{k i}\right|\right)+P_{\lambda}\left(\left|\tilde{\beta}_{j i}^{*}\right|\right)\right\}+\left\{\left.\tilde{V}_{j}\right|_{\beta_{i j}=0}+\sum_{k \neq i, j} P_{\lambda}\left(\left|\tilde{\beta}_{k j}\right|\right)\right\}
\end{aligned}
$$

where, in $S_{1},\left.\tilde{V}_{j}\right|_{\beta_{i j}=\tilde{\beta}_{i j}^{*}}$ is $\tilde{V}_{j}$ in (B.2) with $\beta_{i j}$ evaluated at $\tilde{\beta}_{i j}^{*}$ from PCD-1, and $\left.\tilde{V}_{i}\right|_{\beta_{j i}=0}$ is $\tilde{V}_{i}$ with $\beta_{j i}$ evaluated at zero. In $\left.S_{2}, \tilde{V}_{i}\right|_{\beta_{j i}=\tilde{\beta}_{j i}^{*}}$ and $\left.\tilde{V}_{j}\right|_{\beta_{i j}=0}$ are similarly defined.

PCD-4: If $S_{1} \leq S_{2}$, then update $\left(\tilde{\beta}_{i j}, \tilde{\beta}_{j i}\right)$ to $\left(\tilde{\beta}_{i j}^{*}, 0\right)$; otherwise, update $\left(\tilde{\beta}_{i j}, \tilde{\beta}_{j i}\right)$ to $\left(0, \tilde{\beta}_{j i}^{*}\right)$.

In PCD-1 and PCD-2, we use the Newton-Raphson method to obtain $\tilde{\beta}_{i j}^{*}$ and $\tilde{\beta}_{j i}^{*}$. More generically, denoting the value of $\beta_{i j}$ at the $t^{\text {th }}$ iteration of PCD as $\beta_{i j}^{(t)}$, we update it to

$\beta_{i j}^{(t+1)}=\beta_{i j}^{(t)}-\left\{\tilde{V}_{j}^{(1)}\left(\beta_{i j}^{(t)}\right)+P_{\lambda}^{\prime}\left(\left|\beta_{i j}^{(t)}\right|\right)\right\} /\left\{\tilde{V}_{j}^{(2)}\left(\beta_{i j}^{(t)}\right)+P_{\lambda}^{\prime \prime}\left(\left|\beta_{i j}^{(t)}\right|\right)\right\}$, where $\tilde{V}_{j}^{(1)}\left(\beta_{i j}^{(t)}\right)$ denotes $\left(\partial / \partial \beta_{i j}\right) \tilde{V}_{j}$ evaluated at $\beta_{i j}=\beta_{i j}^{(t)}, \tilde{V}_{j}^{(2)}\left(\beta_{i j}^{(t)}\right)$ is equal to $\left(\partial^{2} / \partial \beta_{i j}^{2}\right) \tilde{V}_{j}$ evaluated at $\beta_{i j}=\beta_{i j}^{(t)}$, and $\beta_{i j}^{(0)}=\tilde{\beta}_{i j}$. Elaborating these derivatives gives the following formula leading to $\tilde{\beta}_{i j}^{*}$ at convergence,

$$
\beta_{i j}^{(t+1)}=\beta_{i j}^{(t)}-\frac{\mathbf{1}^{\mathrm{T}} \mathbf{F}_{j}\left(\mathbf{I}_{n_{-j}}-\mathbf{Q}_{j}\right) \mathbf{1}+n_{-j} P_{\lambda}^{\prime}\left(\left|\beta_{i j}^{(t)}\right|\right)}{\mathbf{1}^{\mathrm{T}}\left\{\left(\mathbf{P}_{j}-\mathbf{Q}_{j} \mathbf{P}_{j}-\mathbf{F}_{j} \mathbf{F}_{j}\right)\left(\mathbf{I}_{n_{-j}}-\mathbf{Q}_{j}\right)-\mathbf{F}_{j} \mathbf{T}_{j}\right\} \mathbf{1}+0.5 n_{-j} P_{\lambda}^{\prime \prime}\left(\left|\beta_{i j}^{(t)}\right|\right)}
$$

where $\mathbf{1}$ is an $n_{-j} \times 1$ vector of 1 's, $\mathbf{I}_{n_{-j}}$ is the $n_{-j} \times n_{-j}$ identity matrix, $\mathbf{F}_{j}=\mathbf{C}_{j}\left(\mathbf{C}_{j}^{\mathrm{T}} \mathbf{C}_{j}\right)^{-1} \mathbf{R}_{j}^{\mathrm{T}}$, $\mathbf{P}_{j}=\mathbf{R}_{j}\left(\mathbf{C}_{j}^{\mathrm{T}} \mathbf{C}_{j}\right)^{-1} \mathbf{R}_{j}^{\mathrm{T}}, \mathbf{Q}_{j}=\mathbf{C}_{j}\left(\mathbf{C}_{j}^{\mathrm{T}} \mathbf{C}_{j}\right)^{-1} \mathbf{C}_{j}^{\mathrm{T}}, \mathbf{T}_{j}=\mathbf{F}_{j}+\mathbf{F}_{j}^{\mathrm{T}}-\mathbf{Q}_{j} \mathbf{F}_{j}^{\mathrm{T}}-\mathbf{F}_{j} \mathbf{Q}_{j}$, in which

$$
\mathbf{C}_{j}=\left[\begin{array}{c}
\boldsymbol{\Psi}_{j 1}^{\mathrm{T}}\left(\beta_{i j}^{(t)}\right) \\
\boldsymbol{\Psi}_{j 2}^{\mathrm{T}}\left(\beta_{i j}^{(t)}\right) \\
\vdots \\
\boldsymbol{\Psi}_{j, n_{-j}}^{\mathrm{T}}\left(\beta_{i j}^{(t)}\right)
\end{array}\right], \mathbf{R}_{j}=\left[\begin{array}{c}
\left(\partial / \partial \beta_{i j}\right) \boldsymbol{\Psi}_{j 1}^{\mathrm{T}}\left(\tilde{\mathbf{B}}_{j}\right)\left.\right|_{\beta_{i j}=\beta_{i j}^{(t)}} \\
\left(\partial / \partial \beta_{i j}\right) \boldsymbol{\Psi}_{j 2}^{\mathrm{T}}\left(\tilde{\mathbf{B}}_{j}\right)\left.\right|_{\beta_{i j}=\beta_{i j}^{(t)}} \\
\vdots \\
\left(\partial / \partial \beta_{i j}\right) \boldsymbol{\Psi}_{j, n_{-j}}^{\mathrm{T}}\left(\tilde{\mathbf{B}}_{j}\right)\left.\right|_{\beta_{i j}=\beta_{i j}^{(t)}}
\end{array}\right]
$$

with $\boldsymbol{\Psi}_{j \ell}\left(\beta_{i j}^{(t)}\right)$ denoting $\boldsymbol{\Psi}_{j \ell}\left(\tilde{\mathbf{B}}_{j}\right)$ evaluated at $\beta_{i j}=\beta_{i j}^{(t)},\left(\partial / \partial \beta_{i j}\right) \boldsymbol{\Psi}_{j \ell}\left(\tilde{\mathbf{B}}_{j}\right)=-\mathbf{W}[\ell, i] \mathbf{W}^{\mathrm{T}}[\ell,-j]+$ $\boldsymbol{\Sigma}_{u}[-j,-j] \boldsymbol{e}_{j}$, and $\boldsymbol{e}_{j}$ is a $(p-1) \times 1$ vector whose entries are zero except for the entry corresponding to the location of $\beta_{i j}$ in $\mathbf{B}_{j}$ being one. Finally, in (B.4), the first two derivatives of the SCAD penalty are

$$
\begin{aligned}
& P_{\lambda}^{\prime}\left(\left|\beta_{i j}\right|\right)=\left\{\lambda I\left(\left|\beta_{i j}\right| \leq \lambda\right)+\frac{a \lambda-\left|\beta_{i j}\right|}{a-1} I\left(\lambda<\left|\beta_{i j}\right| \leq a \lambda\right)\right\} \operatorname{sgn}\left(\beta_{i j}\right) \\
& P_{\lambda}^{\prime \prime}\left(\left|\beta_{i j}\right|\right)=-\frac{1}{a-1} I\left(\lambda<\left|\beta_{i j}\right| \leq a \lambda\right)
\end{aligned}
$$

where $\operatorname{sgn}(t)=I(t>0)-I(t<0)$.
In PCD-3 and PCD-4, we choose between $\left(\tilde{\beta}_{i j}^{*}, 0\right)$ and $\left(0, \tilde{\beta}_{j i}^{*}\right)$ to decide if $X_{i}$ is a parent of $X_{j}$ or the other way around. The choice is made based on the sum of the two (partially updated) penalized objective functions, one associated with $X_{j}$ and the other associated with $X_{i}$, evaluated at each pair. The pair leading to a smaller sum is chosen as the updated value

of $\left(\tilde{\beta}_{i j}, \tilde{\beta}_{j i}\right)$. If the chosen pair contains a nonzero component smaller than a pre-specified threshold in absolute value, such as $10^{-4}$, we conclude that there is no edge between the two nodes.

# Appendix C: The PCD algorithm for the naive likelihoodbased method 

One can follow a similar algorithm described in Appendix B to find the miminizer of the naive penalized log-likelihood function $R_{\mathrm{nv}}(\mathbf{B})$ in equation (5) in the main article that relates to a DAG. In this case, one may use the naive least square estimate of $\mathbf{B}_{j}$, for $j=1, \ldots, p$, to construct an initial estimate for $\mathbf{B}$ in Step 1. In Step 2, one would replace $\tilde{V}_{j}$ and $\tilde{V}_{i}$ above by $\tilde{V}_{j, \mathrm{nv}}$ and $\tilde{V}_{i, \mathrm{nv}}$, respectively, where

$$
\tilde{V}_{j, \mathrm{nv}}=\frac{n_{-j}}{2} \log \left\{\sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}-\mathbf{W}[\ell, i] \beta_{i j}\right)^{2}\right\}
$$

and $\tilde{V}_{i, \mathrm{nv}}$ is similarly defined. After these replacements, $\tilde{\beta}_{i j}^{*}$ and $\tilde{\beta}_{j i}^{*}$ in PCD-1 and PCD-2 are solutions to polynomial equations of order $r$, where $r \leq 3$. Hence, $\tilde{\beta}_{i j}^{*}$ and $\tilde{\beta}_{j i}^{*}$ can be found explicitly (when $r<3$ ) or computed numerically via a polynomial equation solver (when $r=3$ ). In particular, the equation to solve in order to find

$$
\tilde{\beta}_{i j}^{*}=\underset{\beta_{i j}}{\arg \min }\left\{\tilde{V}_{j, \mathrm{nv}}+\sum_{k \neq i, j} P_{\lambda}\left(\left|\tilde{\beta}_{k j}\right|\right)+P_{\lambda}\left(\left|\beta_{i j}\right|\right)\right\}
$$

is given by

$$
\begin{aligned}
0= & n_{-j} \sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}-\mathbf{W}[\ell, i] \beta_{i j}\right) \mathbf{W}[\ell, i]- \\
& P_{\lambda}^{\prime}\left(\left|\beta_{i j}\right|\right) \operatorname{sgn}\left(\beta_{i j}\right) \sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}-\mathbf{W}[\ell, i] \beta_{i j}\right)^{2}
\end{aligned}
$$

If a solution exists that satisfies $\left|\tilde{\beta}_{i j}^{*}\right| \geq a \lambda$, then (C.1) reduces to a linear equation in $\beta_{i j}$, and the solution can be trivially found to be

$$
\tilde{\beta}_{i j}^{*}=\frac{\sum_{\ell \in O_{j}}\left(\mathbf{W}_{[ } \ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}\right) \mathbf{W}[\ell, i]}{\sum_{\ell \in O_{j}} \mathbf{W}[\ell, i]^{2}}
$$

If a non-zero solution exists in $[-\lambda, \lambda]$, (C.1) is a quadratic equation, $c_{2} \beta_{i j}^{2}+c_{1} \beta_{i j}+c_{0}=0$, and $\tilde{\beta}_{i j}^{*}$ is the root given by $\left(-c_{1}+\sqrt{c_{1}^{2}-4 c_{2} c_{0}}\right) /\left(2 c_{2}\right)$, where
$c_{2}=\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right) \lambda \sum_{\ell \in O_{j}} \mathbf{W}[\ell, i]^{2}$
$c_{1}=2 c_{2}+n_{-j} \sum_{\ell \in O_{j}} \mathbf{W}[\ell, i]^{2}-\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right) 2 \lambda \sum_{\ell \in O_{j}} \mathbf{W}[\ell, i] \sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}$,
$c_{0}=\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right) \lambda \sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}\right)^{2}-n_{-j} \sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}\right) \mathbf{W}[\ell, i]$.
At the first glance, it may seem strange to have $c_{2}, c_{1}$, and $c_{0}$ depend on the solution via $\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right)$. It actually is a way to check the existence of a minimizer of the optimization problem. It is only when the sign of the root $\left(-c_{1}+\sqrt{c_{1}^{2}-4 c_{2} c_{0}}\right) /\left(2 c_{2}\right)$ agrees with the value of $\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right)$ used in $c_{2}, c_{1}$, and $c_{0}$ do we claim that a non-zero minimizer in $[-\lambda, \lambda]$ is found, and it is equal to this root.

Lastly, if a solution exists that satisfies $\lambda<\left|\tilde{\beta}_{i j}^{*}\right| \leq a \lambda$, then (C.1) is a cubic equation,

$c_{3} \beta_{i j}^{3}+c_{2} \beta_{i j}^{2}+c_{1} \beta_{i j}+c_{0}=0$, where

$$
\begin{aligned}
& c_{3}=\frac{1}{a-1} \sum_{\ell \in O_{j}} \mathbf{W}[\ell, i]^{2} \\
& c_{2}=-\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right) a \lambda c_{3}-\frac{2}{a-1} \sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}\right) \mathbf{W}[\ell, i] \\
& c_{1}=-n_{-j}(a-1) c_{3}-a \lambda\left\{a \lambda c_{3}+\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right) c_{2}\right\}+\frac{1}{a-1} \sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}\right)^{2} \\
& c_{0}=-\frac{a-1}{2} n_{-j}\left\{\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right) a \lambda c_{3}+c_{2}\right\}-\operatorname{sgn}\left(\tilde{\beta}_{i j}^{*}\right) \frac{a \lambda}{a-1} \sum_{\ell \in O_{j}}\left(\mathbf{W}[\ell, j]-\sum_{k \neq i, j} \mathbf{W}[\ell, k] \tilde{\beta}_{k j}\right)^{2}
\end{aligned}
$$

The solution is the real root of this equation.

# Appendix D: Proof of the consistency of SIC 

Recall that the tuning parameter selector is, with the subscript $n$ added to highlight its dependence on $n=\min _{1 \leq j \leq p} n_{-j}$,

$$
\operatorname{SIC}_{n}(G)=\sum_{j=1}^{p}\left(\hat{V}_{j}+e_{j} \frac{\log n_{-j}}{n_{-j}}\right)
$$

where $e_{j}$ is the number of parents of $X_{j}$ according to $G$, and $\hat{V}_{j}$ is equal to $V_{j}$ evaluated at the unpenalized corrected score estimate of $\mathbf{B}_{j}$ given the structure of $G$. For notational simplicity, we assume $n_{-j}=n$, for $j=1, \ldots, p$, in the sequel, and the proposed information criterion can be re-expressed as

$$
\operatorname{SIC}_{n}(G)=\sum_{j=1}^{p} \hat{V}_{j}+e_{G}(\log n) / n=Q_{n}(G)+P_{n}(G)
$$

where $e_{G}$ is the number of edges in $G, Q_{n}(G)=\sum_{j=1}^{p} \hat{V}_{j}$ is the sum of $p$ quadratic forms that depends on the unpenalized estimate of $\mathbf{B}$ given the structure of $G$, and $P_{n}(G)=e_{G}(\log n) / n$

assesses the complexity of $G$ while accounting for the sample size. Denote by $\mathbf{E}_{G}$ the set of directed edges in $G$, and by $\left|\mathbf{E}_{G}\right|$ the size of this set, i.e., $\left|\mathbf{E}_{G}\right|=e_{G}$.

To prove the consistency of $\operatorname{SIC}_{n}(G)$, it suffices to establish the following two assertions,

$$
\begin{aligned}
& \operatorname{SIC}_{n}\left(G_{-}\right)-\operatorname{SIC}_{n}\left(G_{0}\right) \quad>0 \quad \text { with probability approaching one, as } n \rightarrow \infty \\
& \operatorname{SIC}_{n}\left(G_{+}\right)-\operatorname{SIC}_{n}\left(G_{0}\right) \rightarrow 0^{+} \quad \text { in probability as } n \rightarrow \infty
\end{aligned}
$$

If one allows $p$ to increase as $n \rightarrow \infty$, in order to show (D.2) and (12), we also need to assume (A6) $p^{2}(\log n) / n \rightarrow 0$ as $n \rightarrow \infty$, besides regularity conditions (A1)-(A3) listed in Web Appendix A. Without imposing sparsity assumption on $G, e_{G}$ is at most $p(p-1) / 2=O\left(p^{2}\right)$, and (A6) guarantees the penalty $P_{n}(G)$ for graph complexity shrinks to zero as $n \rightarrow \infty$ even for dense graphs. In addition, given (A2), (A6) is a sufficient condition for $Q_{n}(G)$ to be bounded. In this study we assume $e_{G_{0}}<p(p-1) / 2$.

To show (D.2), we will relate graph selection with variable selection in a regression model given a set of candidate predictors as follows. Denote by $\mathscr{M}_{j}$ a regression model with $X_{j}$ being the response variable and the remaining nodes as potential predictors. One selecting an underfitted graph, $G_{-}$, means that, for at least one edge in $G_{0}$, one either reverses it or completely misses it in the selected graph. Suppose in $G_{0}$, there is an edge pointing from $X_{i}$ to $X_{j}$, where $i \neq j$, and it is reversed in the selected $G_{-}$; this means that one underfits the regression model $\mathscr{M}_{j}$ and overfits the regression model $\mathscr{M}_{i}$. If this directed edge in $G_{0}$ is missing in $G_{-}$, it means that one underfits $\mathscr{M}_{j}$. In conclusion, whenever one selects an underfitted graph, one must have underfitted $\mathscr{M}_{j}$ for at least one $j \in\{1, \ldots, p\}$. For such $\mathscr{M}_{j}$, under (A1)-(A2), the $j$ th summand in $Q_{n}\left(G_{-}\right)$is strictly positive in probability as $n \rightarrow \infty$, whereas each summand in $Q_{n}\left(G_{0}\right)$ converges to zero in probability. It follows that,

in

$$
\begin{aligned}
\operatorname{SIC}_{n}\left(G_{-}\right)-\operatorname{SIC}_{n}\left(G_{0}\right) & =\left\{Q_{n}\left(G_{-}\right)-Q_{n}\left(G_{0}\right)\right\}+\left\{P_{n}\left(G_{-}\right)-P_{n}\left(G_{0}\right)\right\} \\
& =\left\{Q_{n}\left(G_{-}\right)-Q_{n}\left(G_{0}\right)\right\}+\left(e_{G_{-}}-e_{G_{0}}\right)(\log n) / n
\end{aligned}
$$

the first difference is positive in probability, which is bounded even when $p \rightarrow \infty$ given (A6), and the second difference converges to zero as $n \rightarrow \infty$ under (A6). Hence (D.2) holds.

To show (12), note that, one selecting an overfitted graph, $G_{+}$, is equivalent to one choosing an overfitted model for $\mathscr{M}_{j}$ for at least one node $X_{j}$. Under (A1)-(A3), overfitting $\mathscr{M}_{j}$ does not inflate the $j$ th summand in $Q_{n}\left(G_{+}\right)$in probability, which is the key difference from underfitting $\mathscr{M}_{j}$ considered earlier. More importantly, by Hansen (1982), evaluated at the overfitted $\mathscr{M}_{j}$ or the true $\mathscr{M}_{j}$ both yield $\hat{V}_{j}$ converging to a quantity of order $O_{P}\left(n^{-1}\right)+$ $o_{P}(\log n / n)$, as $n \rightarrow \infty$. Hence, in

$$
\begin{aligned}
\operatorname{SIC}_{n}\left(G_{+}\right)-\operatorname{SIC}_{n}\left(G_{0}\right) & =\left\{Q_{n}\left(G_{+}\right)-Q_{n}\left(G_{0}\right)\right\}+\left\{P_{n}\left(G_{+}\right)-P_{n}\left(G_{0}\right)\right\} \\
& =\left\{O_{P}(p / n)+o_{P}(p \log n / n)\right\}+\left(e_{G_{+}}-e_{G_{0}}\right)(\log n) / n
\end{aligned}
$$

given (A6), the first two terms in conjunction converge to zero in probability, and so does the latter difference, and latter difference tends to zero from above since it is strictly positive for all $n$ and $p$. Hence (12) holds. This completes the proof that $\operatorname{SIC}_{n}(G)$ is a consistent information criterion for selecting DAGs. The arguments in this appendix still carry over following similar ideas when $\left\{n_{-j}\right\}_{j=1}^{p}$ are not all the same and $n=\min _{1 \leq j \leq p} n_{-j}$.
