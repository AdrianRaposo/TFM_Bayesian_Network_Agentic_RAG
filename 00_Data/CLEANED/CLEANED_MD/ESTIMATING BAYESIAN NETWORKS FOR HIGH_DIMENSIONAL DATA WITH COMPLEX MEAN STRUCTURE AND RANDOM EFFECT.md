# Estimating Bayesian networks for high-dimensional data with complex mean structure and random effects 

Jessica Kasza, Gary Glonek, Patty Solomon

## Abstract

The estimation of Bayesian networks given high-dimensional data, in particular gene expression data, has been the focus of much recent research. Whilst there are several methods available for the estimation of such networks, these typically assume that the data consist of independent and identically distributed samples. However, it is often the case that the available data have a more complex mean structure plus additional components of variance, which must then be accounted for in the estimation of a Bayesian network. In this paper, score metrics that take account of such complexities are proposed for use in conjunction with score-based methods for the estimation of Bayesian networks. We propose firstly, a fully Bayesian score metric, and secondly, a metric inspired by the notion of restricted maximum likelihood. We demonstrate the performance of these new metrics for the estimation of Bayesian networks using simulated data with known complex mean structures. We then present the analysis of expression levels of grape berry genes adjusting for exogenous variables believed to affect the expression levels of the genes. Demonstrable biological effects can be inferred from the estimated conditional independence relationships and correlations amongst the grape-berry genes.

Bayesian network; complex mean structure; exogenous variable; grapeberry gene expression; regulatory network; score-based metric; variance components.

# 1 Introduction 

The inner workings of a cell are very complex, with many interacting components. Determining how the genes within a cell interact with each other is an important, but difficult, field of research, often requiring the application of advanced statistical methods. Systems of these gene interactions are known as genetic regulatory networks, and the extent to which such networks may be inferred from observational gene expression data remains largely undetermined. To explore this question carefully and quantitatively, high-dimensional multivariate models, including Bayesian networks, need to be considered. The use of Bayesian networks for the modelling of genetic regulatory networks has been discussed by several authors: see for example $[3,7,8,18]$. Their popularity lies in the provision of a flexible framework for the estimation of conditional dependence relationships, thereby providing a means to estimate a covariance matrix given a high-dimensional sample when maximum likelihood methods are unavailable, [5]. Estimation of such structures allows insight into how the expression levels of large groups of genes are related to one another, which, in turn, should help shed light on genetic regulatory networks involving the genes.

For the most part, it has been assumed that the data used to estimate the networks are independent and identically distributed. In the present paper, we consider the important case where the assumption of independent and identically distributed samples is not satisfied, and propose new methods to allow for the estimation of effects of interest given such complexity. Our theoretical development has been motivated by an observational time course microarray study, involving expression levels of grape-berry genes observed over time and known to be associated with changes in temperature. The grapes were sampled from three vineyards in different regions of southern Australia and data on the ambient temperatures during the times leading up to the picking of each sample of grapes was also measured. We want to investigate the conditional dependence structure of the genes, adjusting for the exogenous effects of temperature and vineyards, and we aim to do this through the estimation of a Bayesian network. If the effect of temperature is unaccounted for in the estimation of a Bayesian network for these genes, because of their common relationship with temperature, many pairs of genes will exhibit strong correlations. Unless the gross effects of vineyard and temperature are removed, one cannot hope to detect more subtle associations between genes.

There are many methods available for the estimation of Bayesian networks given microarray and other high-dimensional datasets, and these may be divided into two broad categories, namely, score-based and constraint-based

methods, [22]. Score-based methods attempt to maximize some score metric associated with the estimated Bayesian network, whilst constraint-based methods estimate conditional independence relationships directly from the data, and combine these to form a Bayesian network. Constraint-based methods test for conditional independence relationships, so the networks obtained through their application can be quite sensitive to Type I and Type II errors, particularly when the sample sizes are small. Score-based methods on the other hand are not as sensitive to small sample sizes, and instead of finding the best local structure for each node, find the best global structure given the data, often resulting in more parsimonious models. Given that gene expression data sets tend to be high-dimensional with the attendant 'small $n$, large $p$ ' problem, we approach the problem of Bayesian network estimation from a score-based perspective, and extend these to include exogenous variables and dependent data.

The outline of the paper is as follows. In Section 2, Bayesian networks and score metrics are briefly reviewed, and our two new score metrics for datasets with complex mean structure and random effects are presented. The new score metrics are used to estimate Bayesian networks for simulated datasets with a known complex mean structure in Section 3.2, and then applied to the analysis of the grape-berry gene expression data in Section 4. In Section 5 , we present a brief summary of our overall findings.

# 2 Bayesian networks and Score Metrics 

### 2.1 BGe, the basic Bayesian score metric

Consider a random vector $X=\left(X_{1}, \ldots, X_{p}\right)^{T}$. A Bayesian network $B$ for $X$ consists of two components: a directed acyclic graph $G=(V, E)$ with $V=\left\{X_{1}, \ldots, X_{p}\right\}$, often written as $V=\{1, \ldots, p\}$, and assumed conditional distributions $f\left(x_{i} \mid x_{P_{i}}, \theta_{i}\right), i=1, \ldots, p$. The set $P_{i}$ is the set of parents of $X_{i}$ in $G$ and $\Theta=\left\{\theta_{1}, \ldots, \theta_{p}\right\}$ is the set of parameters associated with the conditional distributions. The graph and conditional distributions then specify a joint distribution for $X$ :

$$
f(x \mid G, \Theta)=\prod_{i=1}^{p} f\left(x_{i} \mid x_{P_{i}}, \theta_{i}\right)
$$

Bayesian networks encode information about the conditional independence relationships between the variables in $X$. The directed Markov properties, as described in [17], for example, allow conditional independence statements about $X$ to be read from the graph $G$. Additionally, when the available data

set is high-dimensional, and maximum likelihood estimation of the covariance matrix of $X$ is unavailable, estimation of a Bayesian network allows the estimation of the covariance matrix.

Here we consider a vector of pre-processed, normalized expression levels for $p$ genes, and suppose that $X \sim N_{p}(0, \Sigma)$, where $\Sigma$ is unknown. We consider a data set $d=\left\{x_{1}, \ldots, x_{p}\right\}$, where $x_{i}=\left(x_{i 1}, \ldots, x_{i n}\right)^{T}$ is the vector containing the $n$ samples of the expression levels of gene $i$. The estimation of a Bayesian network for $X$ given this data set $d$ consists of learning the structure of a directed acyclic graph encoding the conditional independence relationships between the variables, and the estimation of the parameters $\Theta$.

As described in the Introduction, a score-based approach to learning the structure of the graph encoding the conditional dependence relationships of $X$ is taken. After deciding on a score metric, we want to find a graph that maximises that score metric, and an obvious choice is the likelihood function of directed acyclic graphs given the data. The maximum likelihood score turns out not to be a good idea, however, as it inevitably assigns the complete graph, encoding no conditional independence relationships, the maximum score. For more detail, readers are directed to Section 18.3 of [15].

To avoid the problems with overfitting associated with the maximum likelihood score, the Bayesian score was developed. Following [9] among others, the Bayesian score metric for the estimation of a directed acyclic graph $G$ given some data set $d$ is proportional to the posterior probability of that graph:

$$
S(G \mid d)=p(G) f(d \mid G)=p(G) \int_{\mathbb{R}^{n p}} f(d \mid G, \Theta) f(\Theta \mid G) d \Theta
$$

Here the focus is on the second component of this score, the marginal model likelihood of the data given the graph $G$, where the density of $d$ given $G$ and $\Theta$ is assumed to be an $n p$-dimensional normal density, with mean vector 0 and covariance matrix $\Sigma \otimes I_{n}$. As per Equation (1), this joint density may be decomposed into a product of $p$ conditional densities. When the data set $d$ consists of independent and identically normally distributed samples, $\theta_{i}=\left\{\gamma_{i}, \psi_{i}\right\}$, and

$$
x_{i} \mid x_{P_{i}}, \gamma_{i}, \psi_{i} \sim N_{n}\left(x_{P_{i}} \gamma_{i}, \psi_{i} I_{n}\right)
$$

Given normal-inverse gamma priors for each $\theta_{i}$, or an equivalent inverse Wishart prior on $\Theta$, the score metric of Equation (2) can be written as the product of the prior density on the space of directed acyclic graphs, $p(G)$, and $p$ multivariate $t$ densities. This score metric, only appropriate in the case of independent and identically distributed samples, is known as the BGe metric: "Bayesian metric for Gaussian networks with score equivalence".

# 2.2 BGeCM, the score metric for data sets with complex mean structure 

We now consider the case of a more complex data set $d$, that does not consist of independent and identically distributed samples, such as the grape-berry gene data set described in Section 1. As explained there, contained within that data set is information about exogenous variables thought to affect the expression levels of the genes under study. Given such a data set, we now express the model for the vector of expression levels of gene $i$ as

$$
x_{i} \mid x_{P_{i}}, \gamma_{i}, \psi_{i}, b_{i}, \phi_{i} \sim N_{n}\left(x_{P_{i}} \gamma_{i}+Q b_{i}, \psi_{i} I\right)
$$

where $b_{i}$ is the $m$-vector of the effects of the $m$ exogenous variables on gene $i, \phi_{i}$ are the parameters associated with the (as yet to be selected) prior distribution for $b_{i}$, and $Q$ is the $n \times m$ matrix containing the data associated with the $m$ exogenous variables. It can be seen that in this specification, we retain linear dependence upon expression levels of parent genes, but now, in addition to that dependence, more complex sampling schemes and the influence of exogenous variables are accounted for through the linear dependence of expression levels upon $b_{i}$.

Including exogenous variables in the estimation of a Bayesian network is important in order to obtain an unbiased estimate of the conditional dependence relationships between the genes of interest. For example, the expression levels of two genes may both be dependent upon changes in an exogenous variable, but conditionally independent of each other. If dependence upon exogenous variables is not accounted for, an edge between these two genes is likely to be present in an estimated graph. By accounting for the effects of exogenous variables, we can have more confidence that the conditional dependence relationships obtained represent actual dependence relationships, and are not due to common relationships with exogenous variables.

As can be seen by the definition of the Bayesian score metric given by Equation (2), a joint prior distribution for $\gamma_{i}, \psi_{i}, b_{i}$ and $\phi_{i}$ is required for the calculation of a score metric. Care is required in the specification of this prior distribution, since if priors are not properly selected, a score metric that gives different scores to directed acyclic graphs encoding equivalent conditional independence restrictions will be induced. A score metric that does not discriminate between equivalent directed acyclic graphs is called an equivalent score metric. Discrimination between equivalent graphs is tantamount to assigning causal meaning to the directed edges of $G$, and since the emphasis here is on the estimation of graphs given observational data, the assignation of causal meaning to the estimated relationships is not appropriate.

Extension of the results in [10] to our model indicates that the joint prior distribution for $\gamma_{i}, \psi_{i}, b_{i}$ given $\phi_{i}$ must have a normal-inverse gamma form, and that the effects of the exogenous variables on one gene must be a priori independent of the effects upon another gene, for the induced score metric to satisfy equivalence. The following system of priors are used:

$$
\begin{gathered}
\gamma_{i}\left|\psi_{i} \sim N_{\mid P_{i}}\right|\left(0, \tau^{-1} \psi_{i} I_{\mid P_{i}}\right), \quad \psi_{i}^{-1} \sim G a\left(\frac{\delta+\left|P_{i}\right|}{2}, \frac{\tau}{2}\right) \\
b_{i} \mid \phi_{i} \sim N_{m}\left(0, \phi_{i} I\right)
\end{gathered}
$$

There are several possible assumptions about the form of the prior distribution of the variance of the random effects for gene $i, f\left(\phi_{i}\right)$. Among other choices, the variance of the random effects could be assumed known, a uniform prior could be placed on $\sqrt{\phi_{i}}$, or an inverse gamma prior could be placed on $\phi_{i}$. However, by an extension of the results in [10], when $\phi_{i} \neq v^{-1} \psi_{i}$, any choice of prior distribution on $\phi_{i}$ will result in a marginal model likelihood without a closed form, requiring numerical integration to compute and slowing down computations.

A simulation study in [14] showed that the learnt network structure is quite robust to the misspecification of the prior density for $\phi_{i}$, provided the magnitude of $\phi_{i}$ is correctly specified. Hence, for computational simplicity, the following prior for the variance of the effects of exogenous variables is used:

$$
b_{i} \mid \phi_{i} \sim N_{m}\left(0, v^{-1} \psi_{i} I\right)
$$

where $v$ is some positive parameter that is constant from gene to gene. If $v=\tau$, then $b_{i}$ and $\gamma_{i}$ are independent and identically distributed. Taking $v>\tau$ implies that the $b_{i}$ are less variable than the $\gamma_{i}$, while $v<\tau$ implies that the $b_{i}$ are more variable than the $\gamma_{i}$. If $v$ is taken to be very large, this is equivalent to assuming that the effects of exogenous variables do not contribute much to the overall variability of the expression levels of genes.

Although it will be application dependent, it may be that the assumption the variance of the exogenous variables is related to the variance of the regression parameters in the same way for each gene is not be valid. In this situation, a separate $v_{i}$ could be specified for each gene, but such specification would require information that is most probably unavailable. Alternatively, a hyperprior distribution could be placed upon the $v_{i}$. However, any choice of such a distribution would lead to a score metric without an exact form, again requiring numerical integration to compute.

When $b_{i} \sim N_{m}\left(0, v^{-1} \psi_{i} I\right)$, the marginal model likelihood for a particular random variable given its parents in the graph $G$, can be shown to be

$$
x_{i} \mid x_{P_{i}} \sim t_{\delta+\mid P_{i} \mid}\left(0, \Sigma_{x_{i} \mid x_{P_{i}}}\right)
$$

with

$$
\begin{aligned}
\Sigma_{x_{i} \mid x_{P_{i}}} & =\frac{\tau}{\delta+\left|P_{i}\right|}\left\{J-J x_{P_{i}}\left(\tau I+x_{P_{i}}^{T} J x_{P_{i}}\right)^{-1} x_{P_{i}}^{T} J\right\}^{-1} \\
J & =I-Q\left(v I+Q^{T} Q\right)^{-1} Q^{T}
\end{aligned}
$$

We call the resultant score metric the BGeCM metric: "Bayesian metric for Gaussian networks having score equivalence for data sets with a complex mean structure".

Posterior distributions of the parameters $\gamma_{i}, \psi_{i}$ and $b_{i}$ allow a detailed analysis of the relationships between random effects and the expression levels of the genes of interest. The posterior distributions of $\gamma_{i}$ given $\psi_{i}, b_{i}$ given $\psi_{i}$ and $\psi_{i}$ are given by

$$
\gamma_{i} \mid x_{i}, \psi_{i}, x_{P_{i}} \sim N_{\left|P_{i}\right|}\left(\left(\tau I+x_{P_{i}}^{T} J x_{P_{i}}\right)^{-1} x_{P_{i}}^{T} J x_{i}, \psi_{i}\left(\tau I+x_{P_{i}}^{T} J x_{P_{i}}\right)^{-1}\right)
$$

where $J$ is as given in Equation (4). Further,

$$
\begin{aligned}
b_{i} \mid x_{i}, \psi_{i}, x_{P_{i}} & \sim N_{m}\left(\left(v I+Q^{T} J^{*} Q\right)^{-1} Q^{T} J^{*} x_{i}, \psi_{i}\left(v I+Q^{T} J^{*} Q\right)^{-1}\right) \\
J^{*} & =I-x_{P_{i}}\left(\tau I+x_{P_{i}}^{T} x_{P_{i}}\right)^{-1} x_{P_{i}}^{T}
\end{aligned}
$$

and

$$
\begin{aligned}
\psi_{i} \mid x_{i}, x_{P_{i}} & \sim \operatorname{Inv} \operatorname{Gamma}\left(\frac{n+\left|P_{i}\right|+\delta}{2}, \beta_{\psi_{i}}\right) \\
\beta_{\psi_{i}} & =\frac{\tau}{2}+\frac{1}{2} x_{i}^{T}\left\{J-J x_{P_{i}}\left(\tau I+x_{P_{i}}^{T} J x_{P_{i}}\right)^{-1} x_{P_{i}}^{T} J\right\} x_{i}
\end{aligned}
$$

Note that instead of using a score metric as developed above to allow for the inclusion of exogenous variables in the model, an extended directed acyclic graph could be learnt, where exogenous variables are included as vertices in the graph. There are however, a couple of difficulties presented by such an approach. The first is that if the exogenous variables are discrete, methods for Bayesian networks on both continuous and discrete variables are required. Additionally, many algorithms for learning directed acyclic graphs incorporate sparsity constraints, and if it is believed that many of the genes are affected by these exogenous variables, these sparsity constraints will require modification.

# 2.3 Removal of random effects through analysis of residuals 

In the derivation of the BGeCM score metric, it was assumed that the effects of exogenous variables on gene expression were of intrinsic interest. However,

in many situations, the effects of exogenous variables can be thought of as nuisance variables, complicating the estimation of Bayesian networks for the given gene expression levels. It may be desirable to ignore the possible influences of such effects upon gene expression levels, and on the relationships between genes. Of course, simply ignoring such effects is not recommended. Instead, we develop a non-parametric approach that adjusts for the effects of exogenous variables, without making assumptions about the form of their distributions. This approach, instead of directly using the gene expression data, is based upon the use of linear combinations of residuals left over after the data is regressed upon the effects of the exogenous variables. We call this the "residual approach", and it is inspired by the restricted maximum likelihood procedure used in inference for mixed linear models; see for example Section 12.2 of [2], or Speed [21], which provides a good overview of REML.

The utility of the residual approach is that it makes no assumptions about the distributional form of the random effects of interest. Since no such assumptions are made, the approach is correct no matter what the true distribution of the random effects may be. Hence, in situations when the assumption that $b_{i} \mid \phi_{i} \sim N_{m}\left(0, v^{-1} \psi_{i} I\right)$ is not satisfied, the residual approach provides a useful alternative to the BGeCM score metric, and, as we demonstrate below, is considerably easier to implement.

We consider an $(n-m) \times 1$ random variable $y_{i}=P^{T} x_{i}$, where $P$ is an $n \times(n-m)$ matrix such that

$$
P^{T} Q=0, \quad P^{T} P=I_{n-m}, \quad P P^{T}=I_{n}-Q\left(Q^{T} Q\right)^{-1} Q^{T}
$$

Hence,

$$
y_{i} \mid \gamma_{i}, \psi_{i}, y_{P_{i}} \sim N_{n-m}\left(y_{P_{i}} \gamma_{i}, \psi_{i} I\right)
$$

and the score metric associated with this set of marginal model likelihoods is invariant to the choice of $P$. Implementation of the residual approach to the estimation of Bayesian networks is therefore simple: after selection of an appropriate matrix $P$ and computation of $y_{i}=P^{T} x_{i}$ for $i=1, \ldots, n$, the BGe score metric may be applied to this reduced data set in conjunction with the score-based method of choice.

A drawback of the residual approach is that posterior estimates of the random effects $b_{i}$ are not admitted. However, any potential loss of information about the underlying covariance matrix when the residual approach is used, compared to the 'full' BGeCM score metric, has been investigated in [13], and found to be typically small.

# 3 Numerical study of BGeCM and the residual score metrics 

### 3.1 Implementation of BGeCM and the residual score metrics

In this section, the necessity of score metrics that take account of complex mean structure are demonstrated through the application of the residual approach and the BGeCM score metric to simulated and real data sets.

First, a note on implementation. The BGeCM score metric and the residual approach may be incorporated into any score-based algorithm for the estimation of Bayesian networks, without the need for any additional programming. In the case of the residual approach, all that is required is the calculation of the matrix $P$, satisfying the conditions in Equation (2.3). Then, instead of inputting $d$ into the algorithm of choice, the augmented data set $P^{T} d$ is input. Similarly, when the BGeCM score metric is used, an augmented data set $L^{T} d$ will be the input into the algorithm, where $L^{T}$ is a matrix such that $J=L L^{T}$, where $J$ is as given in Equation (4).

Here we apply the residual approach and BGeCM score metrics in conjunction with the high-dimensional Bayesian covariance selection algorithm, [4], a score-based method for the estimation of Bayesian networks. This algorithm works by constructing and combining regression models for each $X_{i}$.

### 3.2 Simulated data sets

Example 1: In this first example, 10 data sets were generated according to the following system of linear recursive equations:

$$
X_{i j k}=b_{i j}+\epsilon_{i j k}, \quad \epsilon_{i} \sim N\left(0, \psi_{i}\right) \quad(i=1, \ldots, 100 ; j=1,2 ; k=1, \ldots, 50)
$$

The values of $\psi_{i}$ were obtained by sampling from an Inverse $\operatorname{Gamma}(1,1 / 2)$ distribution, and are constant for each of the samples generated. Similarly, $b_{i}=\left(b_{i 1}, b_{i 2}\right)^{T}, i=1, \ldots, 100$, are fixed across data sets, obtained by sampling from

$$
b_{i j} \sim N\left(0, \psi_{i}\right) \quad(i=1, \ldots, 100 ; j=1,2)
$$

corresponding to $v=1$. The non-zero mean structure of this example corresponds to two groups, and the true underlying directed acyclic graph is the empty graph.

Example 2: The system of linear recursive equations governing this example is

$$
\begin{gathered}
X_{i k}=q_{1 k} b_{i 1}+q_{2 k} b_{i 2}+q_{3 k} b_{i 3}+\epsilon_{i k} \quad(i=1, \ldots, 18) \\
X_{19, k}=q_{1 k} b_{19,1}+q_{2 k} b_{19,2}+q_{3 k} b_{19,3}+\gamma_{19,1} X_{1 k}+\gamma_{19,2} X_{2 k}+\epsilon_{19, k} \\
X_{20, k}=q_{1 k} b_{20,1}+q_{2 k} b_{20,2}+q_{3 k} b_{20,3}+\gamma_{20,19} X_{19, k}+\epsilon_{20, k} \\
\epsilon_{i k} \sim N\left(0, \psi_{i}\right) \quad(i=1, \ldots, 20 ; k=1, \ldots, 10)
\end{gathered}
$$

Ten data sets were generated according to this system of equations, and the parameters $\psi_{i}(i=1, \ldots, 20), \gamma_{19}=\left(\gamma_{19,1}, \gamma_{19,2}\right)^{T}$ and $\gamma_{20,19}$ were assumed constant across these data sets. The values of these parameters were obtained by sampling from the following distributions:

$$
\begin{gathered}
\psi_{i} \sim \operatorname{Inv} \operatorname{Gamma}\left(\frac{2+\left|P_{i}\right|}{2}, \frac{1}{2}\right), \quad\left|P_{i}\right|=0 \quad(i=1, \ldots, 18), \quad\left|P_{19}\right|=2, \quad\left|P_{20}\right|=1 \\
\gamma_{19} \sim N_{2}\left(0, \psi_{19} I_{2}\right), \gamma_{20,19} \sim N\left(0, \psi_{20}\right)
\end{gathered}
$$

Similarly, the random effects $b_{i}=\left(b_{i 1}, b_{i 2}, b_{i 3}\right)^{T}(i=1, \ldots, 20)$, were constant across the 10 data sets generated, obtained by sampling from

$$
b_{i j} \sim N\left(0, \psi_{i}\right) \quad(i=1, \ldots, 20 ; j=1,2,3)
$$

again corresponding to $v=1$.
The true model for each variable may be written as

$$
\begin{gathered}
x_{i} \mid \psi_{i}, b_{i} \sim N_{10}\left(Q b_{i}, \psi_{i} I_{10}\right) \quad(i=1, \ldots, 18) \\
x_{19} \mid \gamma_{19}, \psi_{19}, b_{19} \sim N_{10}\left(x_{P_{19}} \gamma_{19}+Q b_{19}, \psi_{19} I_{10}\right) \\
x_{20} \mid \gamma_{20}, \psi_{20}, b_{20} \sim N_{10}\left(x_{P_{20}} \gamma_{20}+Q b_{20}, \psi_{20} I_{10}\right)
\end{gathered}
$$

where

$$
\begin{gathered}
x_{i}=\left(\begin{array}{c}
x_{i 1} \\
\vdots \\
x_{i 10}
\end{array}\right) \\
x_{P_{19}}=\left(x_{1}, x_{2}\right), \quad x_{P_{20}}=x_{19}
\end{gathered}
$$

Table 1: Mean and standard deviation of the number of spurious and correct edges in the highest-scoring Bayesian networks obtained when the score metrics are applied to data sets simulated according to Examples 1 and 2


and

$$
Q=\left(\begin{array}{ccc}
q_{11} & q_{21} & q_{31} \\
\vdots & \vdots & \vdots \\
q_{1,10} & q_{2,10} & q_{3,10}
\end{array}\right)=\left(\begin{array}{rrrr}
-1 \cdot 32 & 0 \cdot 83 & -1 \cdot 74 \\
0 \cdot 22 & -1 \cdot 37 & 0 \cdot 55 \\
0 \cdot 37 & 0 \cdot 61 & 0 \cdot 60 \\
-1 \cdot 53 & 1 \cdot 52 & 0 \cdot 82 \\
-0 \cdot 73 & -0 \cdot 01 & 0 \cdot 93 \\
0 \cdot 92 & 0 \cdot 87 & -0 \cdot 09 \\
1 \cdot 02 & -0 \cdot 44 & -0 \cdot 04 \\
0 \cdot 27 & -0 \cdot 59 & 0 \cdot 11 \\
-0 \cdot 64 & 0 \cdot 20 & -0 \cdot 21 \\
-0 \cdot 15 & 0 \cdot 48 & -0 \cdot 12
\end{array}\right)
$$

In this case, elements of the $Q$ matrix consist of random samples from the standard normal distribution, treated as known constants in the analysis, and the true underlying graph has three edges.

Bayesian networks were estimated for each of the data sets generated according to Examples 1 and 2, using the BGe and BGeCM score metrics and the residual approach in conjunction with the High-dimensional Bayesian Covariance Selection algorithm. After assessing the performance of the BGeCM score metric under ideal conditions, we assess the sensitivity of this metric to the misspecification of $v$.

For each of these analyses, the number of spurious and correct edges in the highest-scoring network found by the algorithm was recorded. The results are summarized in Tables 1 and 2. Table 1 gives the mean and standard deviation of the number of spurious and correct edges in the highest-scoring Bayesian networks found when $\mathrm{BGe}, \mathrm{BGeCM}$ and the residual approach, with $v$ set at the correct value, that is $v=1$, are used to estimate the true graph encoding the conditional independence relationships. Table 2 gives the numbers of correct and spurious edges when BGeCM is used given a range of values of $v$.

Comparing the results obtained when the BGe score metric is used to

Table 2: Mean and standard deviation of the number of spurious and correct edges in the highest-scoring graphs found through the application of BGeCM for varying values of $v$, (standard deviation in brackets).


analyse the simulated data sets demonstrates the utility of both the BGeCM score metric and the residual approach. The two new score metrics result in the estimation of structure which is much closer to the true structure. In addition, Table 2 shows that the results obtained from the BGeCM score metric are quite robust to the misspecification of $v$, producing accurate results when the value of $v$ selected departs as much as one or two orders of magnitude from its true value. As $v$ gets larger, the highest scoring graphs obtained become more and more similar to those obtained when the BGe metric is used. This is a result of the fact that as $v$ approaches $\infty$, the limit of the BGeCM metric is the BGe metric, [13].

# 4 Analysis of the grape-berry microarray data 

The data analysed here consisted of 50 samples of gene expression levels for 26 grape genes measured over a four-week period. The gene expression levels were derived from grape-berry tissue samples grown in three different vineyards in three different wine-growing regions of southern Australia. Twenty samples were taken from a vineyard in Clare, 20 from the Wingara Vineyard in Mildura and 10 from a vineyard in Willunga. Table 3 provides the reference numbers for the 26 grape genes, together with a brief summary of their functions. All the genes in Table 3 are known to code for heat shock proteins (HSPs), [24], which are responsible for protecting the grapes against heat-induced stress. In addition to data on the gene expression levels, temperature in degrees celcius was recorded during the time leading up to the picking of the grapes.

These data are part of a larger dataset on grape-berry tissue samples measured between 2003 and 2005. At each vineyard, grapes were sampled roughly weekly over the period of development of the berries, i.e., from the time buds formed on the vines, to the time when the grapes were ripe. In general, grape berries follow a double sigmoidal pattern of growth that consists of two distinct growth phases, with a lag period between these phases (see $[1,19])$. The second stage of grape-berry growth commences upon the occurrence of veraison, when the grape berries start to change colour. Robinson and Davies, [19], suggest that at veraison and during ripening, there are many changes in the expression levels of many different genes in grape berries. The observed developmental time period from bud formation to grape ripeness differed between vineyards in the present study. The shorter four-week time period we analysed occurred after fruit set, but well before veraison for all three vineyards. We restricted attention to samples corresponding to the third to seventh sampling weeks at each vineyard because the relationships between genes are thought to be more stable during this period, and the modelling assumption of identically distributed samples is therefore more likely to be valid.
mRNA expression levels for each of the grape tissue samples was measured using Affymetrix Vitis vinifera oligonucleotide arrays. Background subtraction and normalisation was carried out using robust microarray analysis (RMA), as described in Irizarry et al, [11]. Note that all samples were processed at the same laboratory.

Understanding the stress tolerance mechanisms of plants is important, and the heat shock protein network, as discussed by [16] and [24], is very complex. The heat shock protein network of plants is believed to consist of interactions between small Hsps, Hsp60, Hsp70, Hsp90 and Hsp100, [24]. Precisely how Hsps interact with one another and how they protect against heat stress is not yet completely understood, and here we seek to gain some insight into the heat shock protein network by examining the conditional dependence structure of the genes given in Table 3.

Given the known functions of the genes considered in this study and the climatic and geographic disparities between the regions where the grape berries were sampled, it would incorrect to ignore the effects of vineyard and temperature in the estimation of a Bayesian network for the grape genes. The essential point is that if the expression levels of these genes are strongly influenced by these exogenous variables, then accounting for variation due to such variables in the estimation of a Bayesian network should result in a network that more accurately encodes the dependence structure of the genes. A further important point is that given the grape gene expression levels analysed are observational data, causal interpretations should not be

applied to the directed edges present in any network estimated given the data. Hence, moralized versions of directed acyclic graphs are used to summarize conditional independence relationships of the grape genes.

To begin, the initial (null) model omitted the effects of vineyard and temperature on the expression levels of the genes. That is, if $x_{i}$ is the 50 vector of the expression levels for grape gene $i$, it is assumed that

$$
\begin{aligned}
& x_{i} \mid x_{P_{i}}, \gamma_{i}, \psi_{i} \sim N_{50}\left(x_{P_{i}} \gamma_{i}, \psi_{i} I_{50}\right) \\
& \gamma_{i} \mid \psi_{i} \sim N_{\left|P_{i}\right|}\left(0, \tau^{-1} \psi_{i} I_{\left|P_{i}\right|}\right), \quad \psi_{i}^{-1} \sim G a\left(\frac{\delta+\left|P_{i}\right|}{2}, \frac{\tau}{2}\right)
\end{aligned}
$$

where $x_{P_{i}}$ is a $50 \times\left|P_{i}\right|$ matrix. The columns of this matrix consist of the expression levels of the grape genes in the dataset that the expression level of gene $i$ is dependent upon, $\gamma_{i}=\left(\gamma_{i j}\right)_{j \in P_{i}}$ and $\gamma_{i j}$ is the effect of the expression level of gene $j$ on the expression level of gene $i$. Following the analysis of Affymetrix gene expression data in [4], $\tau=1$ and $\delta=2$.

The highest scoring Bayesian network found through the application of the high-dimensional Bayesian covariance selection algorithm to the full dataset (ignoring the exogenous variables of vineyard and temperature) has 55 edges, and the moralized version has 130 edges. The moralized version is shown in Figure 1(a).

Next, graphs were estimated separately for each of the three vineyards. The highest-scoring directed acyclic graphs obtained for the Clare, Wingara and Willunga vineyards had, respectively, 22, 23 and 17 edges. These graphs were quite different from one another, with the three graphs having only two edges in common, the Wingara and Clare graphs sharing eight edges, and the Willunga graph having three edges in common with the Wingara and Clare graphs. Given the paucity of the data and the complexity of the models, this lack of concordance between the graphs obtained separately for each vineyard is not surprising.

In order to make more efficient use of the data, models incorporating data from all three vineyards simultaneously were then considered.

The question of how best to include temperature and vineyard effects in the model for gene expression was investigated using linear regression models with forward and backward selection. The largest model fitted for each gene contains separate intercepts for the data from each vineyard, and terms for each of the temperatures recorded $30,90,150,210,270$ and 330 minutes before the grapes were picked. We also considered the model including vineyard and temperature main effects and two-way temperature interactions. For the full model with interactions, it was observed that the adjusted $R^{2}$ of many of the regressions was above 0.99 , indicating that some over-fitting was taking

![img-0.jpeg](img-0.jpeg)

Figure 1: The moral versions of the highest-scoring graphs obtained for the grape genes when (a) the effects of temperature and vineyard are ignored, and when the residual approach is used to include (b) vineyard effects, and (c) vineyard effects and main temperature effects.

place. We therefore exclude two-way temperature interaction effects in what follows.

Results of the stepAIC function in R, [23], indicate that there is not a single backwards elimination step that would apply to all genes. That is, each of the vineyard or temperature variables is significant in at least one of the 26 regression models estimated. In any case, use of separate regression models for each gene is beyond the scope of the present score metrics. As such, the largest model considered is as follows:

$$
\begin{gathered}
x_{i} \mid x_{P_{i}}, \gamma_{i}, \psi_{i}, b_{i} \sim N_{50}\left(x_{P_{i}} \gamma_{i}+Q b_{i}, \psi_{i} I_{50}\right) \\
\gamma_{i} \mid \psi_{i} \sim N_{\left|P_{i}\right|}\left(0, \tau^{-1} \psi_{i} I_{\left|P_{i}\right|}\right) \\
\psi_{i}^{-1} \sim G a\left(\frac{\delta+\left|P_{i}\right|}{2}, \frac{\tau}{2}\right)
\end{gathered}
$$

where $b_{i}=\left(b_{i 1}, \ldots, b_{i 9}\right)$ and $b_{i j}(j=1,2,3)$ is the effect of vineyard $j$ on the expression level of gene $i, b_{i 4}$, and $\ldots, b_{i 9}$ are the temperature effects.

Histograms of the marginal standard deviations of the expression data for each gene, and the residual standard errors from the regressions containing vineyard, and vineyard and temperature as covariates, are shown in Figure 2. Note that there are three genes with very small standard deviations. These plots show that vineyard variables account for only some of the variation in the gene expression levels. Changes in temperature and vineyard account for much more of the observed variation, but there remains some residual variation to be explained. On the basis of these histograms, we expect that the graph obtained when only vineyard is included as an exogenous variable will be somewhat similar to that obtained when the exogenous variables are ignored, whilst we would expect to see a reasonably different structure when both vineyard and temperature are accounted for.

In accounting for the effects of vineyard and temperature, we find highscoring Bayesian networks using the BGeCM score metric, first fitting the model with vineyard effects only, then the model with vineyard and main temperature effects. The highest-scoring Bayesian networks found for $v=$ $0.5,1$ and 10 were recorded and their moral graphs summarized in Table 4. It can be seen that as more covariates are included in the model, more of the variation in the expression levels of the grapes is explained, and the highestscoring graphs obtained have fewer edges. Edges that are removed as more exogenous variables are included in the model can be interpreted as being explained by common relationships of genes with these additional covariates.

The BGeCM score metric assumes that the effects of the exogenous variables are independent and identically distributed, an assumption that must

![img-1.jpeg](img-1.jpeg)
(a) Standard errors of expression levels
![img-2.jpeg](img-2.jpeg)
(b) Residual standard errors after regressing expression levels on vineyard
![img-3.jpeg](img-3.jpeg)
(c)Residual standard errors after regressing expression levels on vineyard and temperature

Figure 2: Histograms of the marginal standard deviations of the grape gene expression levels and the residual standard errors after regressing the expression levels on vineyard only, then vineyard and temperature.

be questioned. The effects of temperature and vineyard are almost certainly not iid. However, there is little information available to provide a useful estimate of the covariance structure of the effects of these exogenous variables. Therefore, the residual approach, which makes no assumptions about the covariance structure of the effects included in the model, is preferred here.

The number of edges in the moralized versions of the highest-scoring networks obtained using the residual method are summarized in Table 4. When only the effects of vineyards are included in the model, the results obtained using the residual method are similar to those obtained when the BGeCM score is used, as expected on the basis of the histograms in Figure 2. When the effects of temperature are included in the model, the residual method produces high-scoring graphs with fewer edges than the BGeCM score metric. This indicates that whilst the BGeCM score metric may account correctly for the covariance structure of the effects of vineyard, the effects of temperature may have a more complicated variance structure, that is not adequately modelled by the iid assumption.

The moralized graphs obtained from the residual method are displayed in Figure 1. These graphs, drawn using GraphViz, [6], show that as more of the variation in gene expression due to exogenous sources is accounted for in the model, the moral graphs of the highest-scoring networks obtained have fewer edges. The graph obtained by including both temperature and vineyard as exogenous variables, Figure 1(c), is preferable to that obtained when only vineyard is included, Figure 1(b). For most genes, very little variation in the gene expression values is accounted for by the relationship with vineyard alone.

There are a number of interesting features to be observed in graph Figure 1(c), which is the graph obtained when both vineyard and temperature effects are accounted for in the model. We observe that seven nodes in this graph are completely disconnected from all other nodes, which implies that once relationships with temperature and vineyard have been accounted for, the expression levels of each of these genes are independent of the expression levels of all other genes. (Recall that absence of an edge between two genes in Figure 1(c) indicates that the expression levels of these nodes are independent, a relationship which can be refined through application of Markov properties.)

It is apparent that three of these seven disconnected nodes, corresponding to genes 14,18 and 23 , are already disconnected from the rest of the graph when only vineyard is included in the model; see Figure 1(b), where it is observed that these are the only three unconnected nodes. The expression levels of these three genes are observed to have the lowest standard deviations of all the genes, at $0.037,0.034$ and 0.068 respectively, and are in fact the

three genes at the left-most end of the rug in Figure 2(a). When these three genes are regressed on vineyard, the residual standard deviations are even smaller ( $0.029,0.023$ and 0.047 ). In other words, there is no variation in the expression levels of these genes to be explained by relationships with other genes, so it is not surprising that they are unconnected in the graph. Very small gene standard deviations can be problematic in microarray data analysis, and methods have been proposed for adjusting the standard deviation estimates upwards by adding a constant term or by application of empirical Bayes methods when constructing $t$-tests, for example, [20]. Such adjustment is beyond the scope of our present analysis however. Note that the fact the three genes are connected in Figure 1(a) is suggestive of overfitting when the BGe metric is used.

Genes 9, 10 and 11 are also disconnected in the final graph, Figure 1(c), and correspond to Hsp81, which is an early response to dehydration. According to the KEGG data base, [12], they are predicted to be similar to Hsp90. The role of these sets of genes in the heat shock network of grapes is not entirely understood. The role of Hsp81 proteins in Arabidopsis thaliana, more commonly known as thale cress, has been discussed in [25], who note that an increase in the expression level of Hsp81-1 is possibly caused by a regulatory pathway other than the heat shock pathway. Our analysis supports this finding for Vitis Vinifera, indicating that Hsp81 may not be implicated in the heat shock protein network of grapes, at least over the four-week time period studied. We have established that variation in the Hsp81 genes is accounted for directly by the effects of the exogenous variables, and that they are uncorrelated with the other HSPs in the final graph.

The seventh gene, number 26, which is a mitochondrial small Hsp, is not implicated in the final network either. This gene is the only mitochondrial gene considered. That it is unconnected from the rest of the network indicates that variation in this gene is explained purely by exogenous temperature and vineyard effects, and is not dependent upon any of the other genes in the dataset. This suggests that the mitochondrial HSP are not regulated in the same way as other cellular HSPs.

On the whole, relatively little is known about the heat shock regulatory network for grapes. Typically in the representation of the heat response network for plants, relationships between classes of genes, such as small Hsps or Hsp70s are discussed, [24]. The graph obtained here provides a good starting point for the development of a finer structure, which can then be further developed. The edges between the genes in Figure 1(c) can be interpreted as encoding conditional dependence relationships. This graph is the moralized version of the directed acyclic graph found, and more detail is available through consideration of the class partially directed acyclic graph,

or class PDAG, of the underlying directed acyclic graph. However, since we are analysing observational data, we will consider here edges in the moralized version of the graph only. We observe that there are two pairs of genes connected by a single edge. The first pair of nodes is $(12,19)$, representing a chaperone gene (gene 12) which promotes the folding and unfolding of proteins and a class I small HSP (gene 19). This is an undirected edge, but the two genes are correlated after adjusting for the exogenous variables, and the chaperone gene 12 has no other connecting edges. The second pair of connected nodes is $(2,8)$, representing a glucose regulated HSP (gene 2) and the ubiquitin conjugating enzyme 4 e (gene 8); again these two genes are correlated after adjusting for the exogenous variables, and the enzyme gene 8 has no other connecting edges.

Further investigation of the connected nodes and possible regulatory heat shock mechanisms is beyond the scope of the present paper, and would require further biological evidence and possible investigation. It is clear from the detection of the unconnected nodes together with the plausible relationships between nodes connected by a single edge, that analysis of the data using the new score metrics has demonstrable utility and has detected real biological effects.

# 5 Discussion 

The BGeCM score metric and the residual approach presented in this paper enable Bayesian network structures to be learnt given datasets that do not consist of independent and identically distributed samples, and may be used in conjunction with any score-based method for the estimation of a Bayesian network. Furthermore, the residual approach allows the estimation of a Bayesian network for datasets with a complex mean structure without the need to specify the variance structure of the mean effects. This approach proved useful for the analysis of the grape-berry gene data, where it could not reasonably be supposed that the effects of the exogenous variables were independent and identically distributed. Our analysis of the grape-berry gene microarray data has resulted in biologically plausible conclusions on the heat shock regulatory network of grape genes. These inferences could not have been drawn without the availability of suitable score metrics to account for the effects of exogenous variables.
