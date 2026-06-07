# HHS Public Access 

Author manuscript
Int J Data Sci Anal. Author manuscript; available in PMC 2019 August 01.
Published in final edited form as:
Int J Data Sci Anal. 2018 August ; 6(1): 3-18. doi:10.1007/s41060-017-0085-7.

## Scoring Bayesian Networks of Mixed Variables

Bryan Andrews,<br>University of Pittsburgh, Pittsburgh, PA 15260, USA<br>Joseph Ramsey, and<br>Carnegie Mellon University, Pittsburgh, PA 15213, USA<br>Gregory F. Cooper<br>University of Pittsburgh, Pittsburgh, PA 15260, USA


#### Abstract

In this paper we outline two novel scoring methods for learning Bayesian networks in the presence of both continuous and discrete variables, that is, mixed variables. While much work has been done in the domain of automated Bayesian network learning, few studies have investigated this task in the presence of both continuous and discrete variables while focusing on scalability. Our goal is to provide two novel and scalable scoring functions capable of handling mixed variables. The first method, the Conditional Gaussian (CG) score, provides a highly efficient option. The second method, the Mixed Variable Polynomial (MVP) score, allows for a wider range of modeled relationships, including non-linearity, but it is slower than CG. Both methods calculate log likelihood and degrees of freedom terms, which are incorporated into a Bayesian Information Criterion (BIC) score. Additionally, we introduce a structure prior for efficient learning of large networks and a simplification in scoring the discrete case which performs well empirically. While the core of this work focuses on applications in the search and score paradigm, we also show how the introduced scoring functions may be readily adapted as conditional independence tests for constraint-based Bayesian network learning algorithms. Lastly, we describe ways to simulate networks of mixed variable types and evaluate our proposed methods on such simulations.


## Keywords

Bayesian network structure learning; mixed variables; continuous and discrete variables

## 1 Introduction

Bayesian networks are a widely used graphical framework for representing probabilistic relationships among variables. In general, a Bayesian network consists of two components, a structure component and a distribution component. The structure component encodes conditional independence relationships between variables allowing for an efficient factorization of the joint distribution, while the distribution component parameterizes the probabilistic relationships among the variables. In this paper, our interests lie in learning the

structure component of Bayesian networks, represented by a Directed Acyclic Graph (DAG). Learning a DAG over a set of variables is of particular interest, because under assumptions a DAG can be interpreted as a causal model [26].

Automated Bayesian network learning from data is an important and active area of research. However, relatively few researchers have investigated this task in the presence of both continuous and discrete variables [3, 8, 13, 15, 21, 24, 25]. In the limited work that has been done, researchers either ignore the case where continuous variables are parents of discrete variables, or do not provide solutions that scale much beyond 100 variables. The goal of this paper is to provide solutions for researchers working with datasets containing hundreds of variables.

Most methods for learning Bayesian networks fall into one of two categories: search and score or constraint-based. Search and score methods heuristically search the space of possible structures using an objective function to evaluate fitness while constraint-based methods use conditional independence tests find patterns of independence that are consistent with a set of DAGs. The core of this paper focuses on the search and score paradigm, however, we also show how the scoring functions we propose may be readily adapted as conditional independence tests for constraint-based methods. For additional background information on Bayesian networks and learning their structures, see [6].

The remainder of this paper is organized as follows. Section 2 discusses general properties of scoring functions and the Bayesian Information Criterion (BIC). Sections 3 and 4 introduce the Conditional Gaussian (CG) score and the Mixed Variable Polynomial (MVP) score respectively. Section 5 details several adaptations of the introduced methods. Section 6 reports empirical results of the CG and MVP methods on data generated using simulation. Section 7 provides discussion and conclusions.

## 2 Scoring Bayesian Networks

Search and score methods utilize an objective function to evaluate the fitness of DAGs on a given dataset ⊿. Let S be a score function and ⊿ be a DAG containing m variables. Let Y_{i} be the i^{th} variable with parents Pa_{i} for i ∈ {1, 2, ... m}. When scoring ⊿, most search algorithms require that S decomposes into local components involving only Y_{i} and Pa_{i}. This property is known as decomposability. Given a score is decomposable, we need only compare the differing local components to decide which of any two DAGs is better. To solidify this concept, we say a score S is decomposable if it can be represented as a sum of local components. We score DAG ⊿ on dataset ⊿ using score S as,

S (⊿ , ⊿ ) = ∑ i = 1 m s (Y i , Pa i) ,

where s(Y_{i}, Pa_{i}) is the score for the i^{th} local component.

Note that several DAGs can encode the same set of conditional independence relationships. A set of DAGs which encodes the same independencies is known as a Markov Equivalence

Class (MEC). If a scoring function $S$ scores all DAGs in the same MEC equally, then $S$ is score equivalent. To clarify, let $\mathscr{G}$ and $\mathscr{G}^{\prime}$ be DAGs over the variables in dataset $\mathscr{D}$. If $\mathscr{G}$ and $\mathscr{G}^{\prime}$ encode the same conditional independence relationships and $S$ is score equivalent, then. This can be a desirable trait because it allows search algorithms, such as Greedy Equivalent Search (GES) [5], to search over MECs directly.

Another common trait for scoring functions that algorithms such as GES require for optimality is consistency. Let $\mathscr{D}$ be a dataset and $\mathscr{G}$ and $\mathscr{G}^{\prime}$ be DAGs. A scoring function $\mathscr{S}$ is consistent if in the large sample limit the following two conditions imply $\mathscr{G}$ will score higher than, $\mathscr{G}^{\prime}$ i.e. : (1) There exists a parameterization $\theta$ which allows $\mathscr{G}$ to represent the generating distribution of $\mathscr{D}$ and no such parameterization $\theta^{\prime}$ exists for $\mathscr{G}^{\prime}$ or (2) there exist parameterizations $\theta$ and $\theta^{\prime}$ which allow $\mathscr{G}$ and $\mathscr{G}^{\prime}$ each to represent the generating distribution of $\mathscr{D}$, but $\mathscr{G}$ contains fewer parameters.

# 2.1 The Bayesian Information Criterion 

The Bayesian Information Criterion (BIC) is a well studied and widely applied marginal log likelihood approximation that is generally used for model selection. Let $M$ be a model we wish to score given a dataset $\mathscr{D}$. We can write the probability of model $M$ given $\mathscr{D}$ using Bayes' rule as,

$$
p(M \mid \mathscr{D})=\frac{p(\mathscr{D} \mid M) p(M)}{p(\mathscr{D})}
$$

However, since the data are fixed, $p(\mathscr{D})$ will remain constant across different model choices. Thus, for model selection, we use,

$$
p(M \mid \mathscr{D}) \propto p(\mathscr{D} \mid M) p(M)
$$

BIC aims to approximate $p(M \mid \mathscr{D})$ in (1). For now, we assume $p(M)$ is distributed uniformly and thus drop it. Later in section 5.1, we introduce an alternative distribution for $p(M)$, which we find performs well in practice. Raftery [17] shows that when assuming a flat prior over the parameters, the logarithm of $p(\mathscr{D} \mid M)$ can be approximated as:

$$
\log p(\mathscr{D} \mid M) \approx 2 \ell(\boldsymbol{\theta})+d f \log n
$$

where $\ell(\theta)$ is the maximum log likelihood of the data, $d f$ are the degrees of freedom, and $n$ is the sample size. The approximation on the right hand side of (2) characterizes the BIC, introduced by Schwarz [23]. BIC is decomposable and can be readily applied to score Bayesian networks. In sections 3 and 4, we detail how to calculate the log likelihood and degrees of freedom terms for BIC using our proposed scoring methods. We score DAGs using BIC given such log likelihood and degrees of freedom calculations.

3 The Conditional Gaussian Score

In general, the Conditional Gaussian (CG) score calculates conditional Gaussian mixtures using the ratios of joint distributions. Since CG uses BIC as a framework to evaluate its approximations, the score is decomposable into a sum of parent-child relationships. In order to outline such a relationship, we introduce continuous variables C_{1}, C_{2} and discrete variables D_{1}, D_{2} Below we detail the CG score using these four variables, however this procedure straightforwardly generalizes to any number of variables. We compute the conditional distribution where C_{1} is a child with parents C_{2}, D_{1}, and D_{2} as, $$p\left(C_{1} \mid C_{2},D_{1},D_{2}\right) = \frac{p\left(C_{1}, C_{2},D_{1},D_{2}\right)}{p\left(C_{2},D_{1},D_{2}\right)} = \frac{p\left(C_{1}, C_{2} \mid D_{1},D_{2}\right)}{p\left(C_{2} \mid D_{1},D_{2}\right)}$$ and the conditional distribution where D_{1} is a child with parents C_{1}, C_{2}, and D_{2} as, $$p\left(D_{1} \mid C_{1},C_{2},D_{2}\right) = \frac{p\left(C_{1}, C_{2},D_{1},D_{2}\right)}{p\left(C_{1}, C_{2},D_{2}\right)} = \frac{p\left(C_{1}, C_{2} \mid D_{1},D_{2}\right)p\left(D_{1},D_{2}\right)}{p\left(C_{1}, C_{2} \mid D_{2}\right)p\left(D_{2}\right)}.$$

In (3) and (4), we can readily calculate p(C_{1}, C_{2}|D_{1}, D_{2}) and p(C_{1}, C_{2}|D_{2}) using Gaussian distributions partitioned on the discrete variables and p(D_{1}, D_{2}), p(D_{2}) using multinomial distributions. This raises the first of CG's assumptions.

### Assumption 1

The data were generated from a Gaussian mixture where each Gaussian component exists for a particular setting of the discrete variables.

This assumption allows for efficient calculations, but also assumes that the discrete variables take part in generating the continuous variables by defining the Gaussian mixture components, e.g. p(C_{1}, C_{2}, D_{1}, D_{2}) is a Gaussian mixture with a Gaussian component for each setting of D_{1} and D_{2}. Therefore, when scoring a discrete variable as the child of a continuous variable, our model assumption will inherently encode the reverse relationship. In section 6, we see that even with this assumption, CG performs quite well under this assumption.

### Assumption 2

The instances in the data are independent and identically distributed.

The data are assumed to be i.i.d. so that we can calculate the log likelihood as a sum over the marginal log probabilities for each instance in the data.

It is important to note that if we treat p(C_{1}, C_{2}, D_{1}, D_{2}) as a mixture distribution with a Gaussian component for each setting of D_{1} and D_{2}, to calculate p(C_{1}, C_{2}, D_{2}) correctly, we must marginalize D_{2} out and treat p(C_{1}, C_{2}, D_{2}) as a mixture distribution with a Gaussian mixture for each setting of D_{2}.

### Assumption 3

All Gaussian mixtures are approximately Gaussian.

For computational efficiency, we approximate all Gaussian mixtures resulting from marginalizing discrete variables out as single Gaussian distributions. In section 6.1, we evaluate this approximation experimentally and find that it performs well.

Under mild conditions, BIC is consistent for Gaussian mixture models [10]. Since CG assumes the data are generated according to a Gaussian mixture, under the same mild assumptions, CG is consistent. Additionally, CG is score equivalent; see Appendix A for a proof.

In the remainder of the current section, we provide a high-level overview of the CG method; sections 3.1 and 3.2 provide details. Let Y_{i} be the i^{th} variable in a DAG 57 with the set Pa_{i} containing the parents of Y_{i}. Furthermore, let Pa_{i} consist of two mutually exclusive subsets Pc_{i} and Pd_{i} such that Pc_{i} and Pd_{i} hold the continuous and discrete parents of Y_{i} respectively. To evaluate the parent-child relationship between a variable Y_{i} and its parents Pa_{i}, CG calculates the log likelihood and degrees of freedom for the joint distributions of two sets of variables, Y_{i} U Pa_{i} and Pa_{i}. The log likelihood of Y_{i} given its parents Pa_{i} is computed as the difference between the log likelihood terms for Y_{i} U Pa_{i} and Pa_{i}. Similarly, the degrees of freedom are calculated as the difference in parameters used to fit Y_{i} U Pa_{i} and Pa_{i}.

When evaluating the two sets of variables, the dataset 58 is first partitioned according to the discrete variables in each set. That is, we divide 58 using a partitioning set Π_{i} over all the instances in 58. Π_{i} contains a partition for each combination of values the discrete variables take on in 58. Further, we form a design matrix X_{p} for each partition p ∈ Π_{i}. X_{p} holds the data corresponding to the instances of the continuous variables in partition p. Gaussian and multinomial distributions are fit according to the continuous and discrete variables respectively to calculate log likelihood and degrees of freedom terms which BIC uses to compute the score.

### 3.1 Modeling a Set of Variables

When using CG, we have three different kinds of sets to model: Y_{i} U Pa_{i} where Y_{i} is continuous, Y_{i} U Pa_{i} where Y_{i} is discrete, and Pa_{i}. They all follow the same generic format so we will describe the process in general while pointing out any subtle differences where they apply.

First we partition the data with respect to a partitioning set Π_{i} generated according to the discrete variables Pd_{i}. Note that if our set includes a discrete child Y_{i}, then the discrete variables are comprised of Y_{i} U Pd_{i} and we partition according to these variables. Π_{i} contains a partition for every combination of values in the discrete variables. We define the partitioning set Π_{i} using a Cartesian product of the discrete variables. Let |Pd_{i}| = d, then partitioning set Π_{i} = (Y_{i})×Pd_{i}(1)×Pd_{i}(2)×⋯×Pd_{i}(d) where Y_{i} is the set of values for the child (included only if Y_{i} is discrete), Pd_{i}(1) is the set of values for the first discrete parent, Pd_{i}(2) is the set of values for the second discrete parent, and so forth.

Let |Pc_{i}| = c, then for each partition p ∈ Π_{i} we define a design matrix X_{p} with n_{p} observations and c variables. Here, if our set includes a continuous child Y_{i}, then we instead define X_{p} with c + 1 variables corresponding to the variables in Y_{i} U Pc_{i}. That is,

$$
\boldsymbol{x}_{p}=\left|\begin{array}{cccc}
x_{11} & x_{12} & \cdots & x_{1 c} & \left(y_{1}\right) \\
x_{21} & x_{22} & \cdots & x_{2 c} & \left(y_{2}\right) \\
\vdots & \vdots & \ddots & \vdots & (\vdots) \\
x_{n_{p} 1} & x_{n_{p} 2} & \cdots & x_{n_{p} c} & \left(y_{n_{p}}\right)
\end{array}\right|
$$

where $x_{j k}$ is the $j^{\text {th }}$ value with respect to partition $p$ of the $k^{\text {th }}$ variable in $P c_{i}$ and $y_{j}$ is the $j^{\text {th }}$ value with respect to $p$ of the child $Y_{i}$ (included only if $Y_{i}$ is continuous) for $j \in\{1,2, \ldots$, $\left.n_{p}\right\}$ and $k \in\{1,2, \ldots, c\}$.

# 3.2 Calculating the Log Likelihood and Degrees of Freedom 

The calculations for the three aforementioned sets are identical in formulation, so without loss of generality, we demonstrate the log likelihood and degrees of freedom calculations for the set $Y_{i} \cup P a_{i}$. The log likelihood for a set is calculated component-wise over each partition and summed together as follows,

$$
\mathscr{C}_{Y_{i} \cup P a_{i}}(\boldsymbol{\theta} \mid \boldsymbol{X})=\sum_{p \in \Pi_{i}} \mathscr{C}_{p}\left(\boldsymbol{\theta}_{p} \mid \boldsymbol{X}_{p}\right)
$$

The degrees of freedom are calculated in a similar manner,

$$
d f_{Y_{i} \cup P a_{i}}(\boldsymbol{\theta})=\sum_{p \in \Pi_{i}} d f_{p}\left(\boldsymbol{\theta}_{p}\right)-1
$$

where the minus 1 term accounts for the redundant mixing component. Let $n$ be the number of observations in the unpartitioned dataset. For each partition $p \in \Pi_{i}$, let $d$ be the number of variables in $\boldsymbol{X}_{p}$ and $x_{p, i}$ be the $j^{\text {th }}$ observation from $\boldsymbol{X}_{p}$. From [2], we calculate the Gaussian log likelihood for partition $p$ as,

$$
\mathscr{C}\left(\boldsymbol{\mu}_{p}, \sum_{p} \mid \boldsymbol{X}_{p}\right)=-\frac{n_{p} l}{2} \log 2 \pi-\frac{n_{p}}{2} \log \left\lvert\, \sum_{p} \left\lvert\,-\frac{1}{2} \sum_{j=1}^{n_{p}}\left(\boldsymbol{x}_{p, j}-\boldsymbol{\mu}_{p}\right)^{T} \sum_{p}^{-1}\left(\boldsymbol{x}_{p, j}-\boldsymbol{\mu}_{p}\right)\right.\right.
$$

where $\boldsymbol{\mu}_{p}, \Sigma_{p}$ are the mean and variance of the Gaussian distribution respectively. The maximum likelihood estimate $\sum_{p}$ is computed as,

$$
\widehat{\boldsymbol{\Sigma}}_{p}=\frac{1}{n_{p}} \sum_{j=1}^{n_{p}}\left(\boldsymbol{x}_{p, j}-\overline{\boldsymbol{x}}_{p}\right)\left(\boldsymbol{x}_{p, j}-\overline{\boldsymbol{x}}_{p}\right)^{T}
$$

Let $\mu_{p}=\bar{x}_{p}$. Note that $\bar{x}_{p}$ will converge quickly to $\mu_{P}$. Using the estimate in (8), the log likelihood in (7) simplifies to,

$$
\ell\left(\sum_{p}^{\hat{*}}\left|X_{p}\right\rangle=-\frac{n_{p}}{2}\left(\log \left|\sum_{p}^{\hat{*}}\right|+d \log 2 \pi+d\right) .\right.
$$

We use (9) to compute the log likelihood of a Gaussian conditioned on discrete variables. However, we still must add the log probability of an instance being from partition $p$ to calculate the desired joint log likelihood. These probabilities are computed using the maximum likelihood estimate of variables distributed according to a multinomial. This estimate is the count of instances in partition $p$ denoted $n_{p}$ over the total count $n$ of all instances: $\frac{n_{p}}{n}$. Thus, we calculate the log likelihood for partition $p$ as,

$$
\ell_{p}\left(\hat{\theta}_{p} \mid \boldsymbol{X}_{p}\right)=-\frac{n_{p}}{2}\left(\log \left|\sum_{p}^{\hat{*}}\right|+d \log 2 \pi+d\right)+n_{p} \log \frac{n_{p}}{n}
$$

We use (10) to calculate $\ell_{i}\left(\theta_{p} \mid \boldsymbol{X}_{p}\right)$ in (5). To find the number of parameters in partition $p$, we count the number of unique terms in $\sum_{p}^{\hat{*}}$ plus one for the mixing component. Therefore,

$$
d f_{p}\left(\hat{\theta}_{p}\right)=\frac{d(d+1)}{2}+1
$$

We use (11) to calculate $d f_{p}\left(\theta_{p}\right)$ in (6).
Using the form of (3) and (4), we calculate the log likelihood and degrees of freedom terms as,

$$
\begin{gathered}
\ell_{i}(\hat{\theta} \mid \boldsymbol{X})=\ell_{Y_{i} \cup P a_{i}}(\hat{\theta} \mid \boldsymbol{X})-\ell_{P a_{i}}(\hat{\theta} \mid \boldsymbol{X}) \\
d f_{i}(\hat{\theta})=d f_{Y_{i} \cup P a_{i}}(\hat{\theta})-d f_{P a_{i}}(\hat{\theta})
\end{gathered}
$$

BIC uses (12) and (13) to compute the score for the parent-child relationship of $Y_{i}$ given $P a_{i}$.

# 4 The Mixed Variable Polynomial Score 

The Mixed Variable Polynomial (MVP) score uses higher order polynomial functions to approximate relationships between any number of continuous and discrete variables. Since MVP uses BIC as a framework to evalute its approximations, the score is decomposable into

a sum of parent-child relationships. The MVP method scores the decomposed local components of a DAG $\mathscr{G}$ using approximating polynomial functions. To motivate the ideas underlying this approach, we note the implications of Weierstrass's approximation theorem.

Weierstrass Approximation Theorem—Suppose $f$ is a continuous real-valued function defined on the real interval $[a, b]$. For every $e>0$, there exists a polynomial p such that for all $x \in[a, b]$, we have $|f(x)-p(x)|<e$.

In short, as long as a function $f$ is continuous and the contributing variables exist within a bounded interval, then there exists a polynomial function which approximates $f$ to an arbitrary degree of accuracy [11]. This brings us to our first two assumptions.

Assumption 1-The sample space of each variable is finite.
To shed some light on this assumption, we note that MVP's approximations are functions of continuous variables in the data. Thus, the motivation for Assumption 1 becomes apparent as a prerequisite of the previously stated theorem; finite sample spaces are bounded.

Assumption 2-Each continuous variable is defined by continuous functions of their continuous parents plus additive Gaussian noise. The probability mass functions of each discrete variable are defined by positive continuous functions of their continuous parents.

The motivation for this assumption follows from Weierstrass's approximation theorem since $f$, the function to be approximated, must be continuous. However, along with assuming continuity, we restrict the model class in the continuous child case to have additive Gaussian noise. This assumption allows us to use least squares regression to obtain efficient maximum likelihood estimates. Additionally, we assume positive functions in the discrete case since we are estimating probability mass functions. It is worth noting that we do not assume linearity unlike other commonly used scores.

Assumption 3-There are no interaction terms between continuous parents.
We make this assumption for tractability. Modeling all interactions among the continuous parents is a combinatorial problem. Thus, we forgo such interaction terms.

Assumption 4-The instances in the data are independent and identically distributed.
The data are assumed to be i.i.d. so that we can calculate the log likelihood as a sum over the marginal log probabilities for each instance in the data.

Under these assumptions, the MVP score is consistent in the large sample limit with an adequate choice of maximum polynomial degree; see Appendix A for a proof. However, due to the use of non-linear functions, it is not score equivalent for any maximum polynomial degree greater than 1. In section 6, we see that even without this property, the MVP score still performs quite well. Moreover, in general, we do not expect causal relationships to be score equivalent, so using a framework that requires score equivalence would not be

desirable. As an example of previous work suggesting that asymmetric scores can be beneficial in inferring causation, see [12].

# 4.1 Partitioned Regression 

Let $Y_{i}$ be the $i^{\text {th }}$ variable in a DAG $\mathscr{G}$ and $P a_{i}$ be the set containing the parents of $Y_{i}$ in $\mathscr{G}$. Furthermore, let $P a_{i}$ consist of two mutually exclusive subsets $P c_{i}$ and $P d_{i}$ such that $P c_{i}$ and $P d_{i}$ hold the continuous and discrete parents of $Y_{i}$ respectively. In general, to evaluate the local score component between $Y_{i}$ and its parents $P a_{i}$, MVP first partitions the data with respect to the discrete parents $P d_{i}$ and performs least squares regression using the continuous parents $P c_{i}$. The log likelihood and degrees of freedom for the model are calculated depending on the variable type of $Y_{i}$. BIC uses the log likelihood and degrees of freedom terms to compute the score.

A partitioning set $\Pi_{i}$ partitions $\mathscr{D}$ with respect to the discrete parents $P d_{i}$ and contains a partition for every combination of values in the discrete parents. We define $\Pi_{i}$ using a Cartesian product of the discrete parents $P d_{i}$. Let $|P d_{i}|=d$, then partitioning set $\Pi_{i}=P d_{i}(1)$ $\times P d_{i}(2) \times \cdots \times P d_{i}(d)$ where $P d_{i}(1)$ is the set of values for the first discrete parent, $P d_{i}(2)$ is the set of values for the second discrete parent, and so forth.

Let $\left|P c_{i}\right|=c$, then for each partition $p \in \Pi_{i}$ we define a design matrix $\boldsymbol{X}_{p}$ with $n_{p}$ observations and $c$ variables. Additionally, we add a bias term and higher order polynomial terms for each variable in $P c_{i}$, stopping at a maximum polynomial order specified by $\mathrm{g}\left(n_{p}\right)$,

$$
\boldsymbol{x}_{p}=\left[\begin{array}{cccccccccc}
1 & x_{11} & \cdots & x_{1 c} & x_{11}^{2} & \cdots & x_{1 c}^{2} & \cdots & x_{11}^{2}\left(n_{p}\right) & \cdots & x_{1 c}^{2}\left(n_{p}\right) \\
1 & x_{21} & \cdots & x_{2 c} & x_{21}^{2} & \cdots & x_{2 c}^{2} & \cdots & x_{21}^{2}\left(n_{p}\right) & \cdots & x_{2 c}^{2}\left(n_{p}\right) \\
\vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \ddots & \vdots & \ddots & \vdots \\
1 & x_{n_{p} 1} & \cdots & x_{n_{p} c} & x_{n_{p} 1}^{2} & \cdots & x_{n_{p} c}^{2} & \cdots & x_{n_{p} 1}^{2}\left(n_{p}\right) & \cdots & x_{n_{p} c}^{2}\left(n_{p}\right)
\end{array}\right]
$$

where $x_{j k}$ is the $j^{\text {th }}$ value with respect to partition $p$ of the $k^{\text {th }}$ variable in $P c_{i}$ for $j \in\{1,2$, $\ldots, n_{p}\}$ and $k \in\{1,2, \ldots, c\}$. In this paper, we report two choices for $g\left(n_{p}\right): g\left(n_{p}\right)=1$, and $g\left(n_{p}\right)=\operatorname{Log} n_{p} \mathrm{~J}$. We have tried other choices, such as $g\left(n_{p}\right)=3$, but found the above options provide the best solutions. Define $\boldsymbol{x}_{j}$ and $\boldsymbol{y}_{p}$ as,

$$
\begin{gathered}
\boldsymbol{x}_{p, j}=\left[\begin{array}{llllll}
1 & x_{j 1} & \cdots & x_{j c} & x_{j 1}^{2} & \cdots & x_{j c}^{2} & \cdots & x_{j 1}^{2}\left(n_{p}\right) & \cdots & x_{j c}^{2}\left(n_{p}\right)
\end{array}\right] \\
\boldsymbol{y}_{p}=\left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n_{p}}
\end{array}\right]
\end{gathered}
$$

where $x_{p, j}$ is the $j^{\text {th }}$ observation in $\boldsymbol{X}_{p}$ and $y_{j}$ is the $j^{\text {th }}$ value with respect to partition $p$ of $Y_{i}$ for $j \in\left\{1,2, \ldots, n_{p}\right\}$.

We calculate the log likelihood of a variable $Y_{i}$ given a set of parents $P a_{i}$ as a sum over the log likelihoods from each partition $p$,

$$
\mathscr{C}_{i}(\boldsymbol{\theta} \mid \boldsymbol{X}, \boldsymbol{y})=\sum_{n \in \Pi_{i}} \mathscr{C}_{p}\left(\boldsymbol{\theta}_{p} \mid \boldsymbol{X}_{p}, \boldsymbol{y}_{p}\right)
$$

where $\hat{\mathscr{C}}\left(\boldsymbol{\theta}_{p} \mid \boldsymbol{X}_{p}, \boldsymbol{y}_{p}\right)$ is defined depending on whether $Y_{i}$ is discrete or continuous. Similarly, the degrees of freedom for $Y_{i}$ are calculated as a sum over the parameter counts in each partition $p$,

$$
d f_{i}(\boldsymbol{\theta})=\sum_{p \in \Pi_{i}} d f_{p}\left(\boldsymbol{\theta}_{p}\right)
$$

BIC computes the local score component using the log likelihood $\hat{\mathscr{Q}}(\boldsymbol{\theta} \mid \boldsymbol{X}, y)$ and degrees of freedom $d f_{i}(\boldsymbol{\theta})$.

# 4.2 Modeling a Continuous Child 

In the case where $Y_{i}$ is continuous, for partition $p$ with design matrix $\boldsymbol{X}_{p}$ and target vector $\boldsymbol{y}_{p}$, we use the maxmum likelihood estimate to determine the log likelihood $\hat{\mathscr{Q}}\left(\boldsymbol{\theta}_{p} \mid \boldsymbol{X}_{p}, y_{p}\right)$ and degrees of freedom $d f_{p}\left(\boldsymbol{\theta}_{p}\right)$. By Assumption 2, for partition $p$, each $y_{j}=f_{p}\left(x_{p, j}\right)+e_{p}$ where $f_{p}$ is a continuous function defined on a bounded interval and $\varepsilon_{p} \sim N\left(0, \sigma_{p}^{2}\right)$ is additive Gaussian noise with variance $\sigma_{p}^{2}$. By the Weierstrass Approximation Theorem, there exists a polynomial function $\hat{f}_{p}$ which approximates $f_{p}$ such that $y_{j} \approx f_{p}\left(\boldsymbol{x}_{p, j}\right)+\boldsymbol{\varepsilon}_{p}$. Estimating the parameters of $y_{j} \approx \hat{f}_{p}\left(\boldsymbol{x}_{p, j}\right)+\varepsilon_{p}$ using least squares regression, we have $\hat{\gamma}_{j} \sim N\left(\boldsymbol{X}_{p} \boldsymbol{\beta}_{p}, \sigma_{p}^{2}\right)$. Therefore the log likelihood partition $p$ becomes,

$$
\mathscr{C}_{p}\left(\boldsymbol{\beta}_{p}, \sigma_{p}^{2} \mid \boldsymbol{X}_{p}, \boldsymbol{y}_{p}\right)=-\frac{n_{p}}{2} \log 2 \pi-\frac{n_{p}}{2} \log \sigma_{p}^{2}-\frac{\left(\boldsymbol{y}_{p}-\boldsymbol{X}_{p} \boldsymbol{\beta}_{p}\right)^{T}\left(\boldsymbol{y}_{p}-\boldsymbol{X}_{p} \boldsymbol{\beta}_{p}\right)}{2 \sigma_{p}^{2}}
$$

where the maximum likelihood estimates are computed as,

$$
\hat{\sigma}_{p}^{2}=\frac{\left(\boldsymbol{y}_{p}-\boldsymbol{X}_{p} \hat{\boldsymbol{\beta}}_{p}\right)^{T}\left(\boldsymbol{y}_{p}-\boldsymbol{X}_{p} \hat{\boldsymbol{\beta}}_{p}\right)}{n_{p}}
$$

Using the estimates in (17) and (18), the log likelihood in (16) simplifies to,

$$
\ell_{p}^{\prime}\left(\hat{\beta}_{p}, \hat{\sigma}_{p}^{2} \mid \boldsymbol{X}_{p}, \boldsymbol{y}_{p}\right)=-\frac{n_{p}}{2}\left(\log 2 \pi+\log \hat{\sigma}_{p}^{2}+1\right)
$$

which we use to calculate $\ell_{p}^{\prime}\left(\boldsymbol{\theta}_{p} \mid \boldsymbol{X}_{p}, \boldsymbol{y}_{p}\right)$ in (14). To find the number of parameters in partition $p$ to calculate $d f_{p}\left(\boldsymbol{\theta}_{p}\right)$ for (15), we count the number of terms in $\hat{\beta}_{p}$,

$$
d f_{p}\left(\boldsymbol{\theta}_{p}\right)=c \cdot g\left(n_{p}\right)+1
$$

The BIC uses (14) and (15) to compute the parent-child relationship for $Y_{i}$ given $P a_{i}$.

# 4.3 Modeling a Discrete Child 

In the case where $Y_{i}$ is discrete, for partition $p$ with design matrix $\boldsymbol{X}_{p}$ and target vector $\boldsymbol{y}_{p}$, we calculate the log likelihood $\ell_{p}^{\prime}\left(\boldsymbol{\theta}_{p} \mid \boldsymbol{X}_{p}, \boldsymbol{y}_{p}\right)$ and degrees of freedom $d f_{p}\left(\boldsymbol{\theta}_{p} \mid \boldsymbol{X}_{p}, \boldsymbol{y}_{p}\right)$ using least squares regression. Suppose $Y_{i}$ consists of $d$ categories. Let $f_{p}, h$ calculate the probability of the $h^{\text {th }}$ category in $Y_{i}$ given the values of the continuous parents $P c_{i}$ where $h \in$ $\{1, \ldots, d\}$. By Assumption 2 and the Weierstrass Approximation Theorem, there exists a polynomial function $\hat{f}_{p, h}$ which approximates $f_{p}, h$ arbitrarily well. With this in mind, we aim to approximate each $f_{p}, h$ with the polynomial function $\boldsymbol{X}_{p} \hat{\beta}_{p, h}$ where $\hat{\beta}_{p, h}$ are the polynomial coefficients calculated from least squares regression. Our end goal is to use the approximations of each $f_{p}, h$ as components of a conditional probability mass function in order to calculate the log likelihood and degrees of freedom terms.

Define the categories of $\boldsymbol{y}_{p}$ such that each $y j \in\{1, \ldots, d\}$. Expand $\boldsymbol{y}_{p}$ into $d$ binary vectors where the $h^{\text {th }}$ vector represents the $h^{\text {th }}$ category. That is, the $j^{\text {th }}$ element from the $h^{\text {th }}$ vector asserts whether or not the $j^{\text {th }}$ observation of $\boldsymbol{y}_{p}$ is category $h$. To represent these binary vectors in matrix notation, we define $1\binom{$ condition }{ } as an indicator variable which is 1 if condition is true and 0 otherwise. The $h^{\text {th }}$ binary vector is then defined as,

$$
\mathbf{1}_{\left\{y_{p}=h\right\}}=\left[\begin{array}{c}
1_{\left\{y_{1}=h\right\}} \\
1_{\left\{y_{2}=h\right\}} \\
\vdots \\
1_{\left\{y_{n_{p}}=h\right\}}
\end{array}\right]
$$

We further define $\mathbf{1}_{p}$ to represent an $n_{p} \times 1$ vector of ones. Using the binary vectors as our targets, we calculate the least squares regression estimate, which yields,

$$
\hat{\hat{\beta}}_{p, h}=\left\langle X_{p}^{T} X_{p}\right\rangle^{-1} X_{p}^{T} \mathbf{1}_{\left\{y_{p}=h\right\}}
$$

If we want to interpret the results of least squares regression $\boldsymbol{X}_{p} \hat{\hat{\beta}}_{p, h}$ as probabilities, we first must ensure that,

1. $\sum_{h=1}^{d} \boldsymbol{X}_{p} \hat{\hat{\beta}}_{p, h}=\mathbf{1}_{p}$
2. $\quad x_{p, j} \hat{\hat{\beta}}_{p, h} \geq 0, \forall j \in\left\{1, \ldots, n_{p}\right\}, h \in\{1, \ldots, d\}$.

We prove condition 1 is necessarily true and that condition 2 holds for an adequate maximum polynomial degree in the sample limit; see Appendix A for the proofs.

Unfortunately, there is no guarantee the values given by least squares regression will be strictly non-negative for finite samples. Instead we define a procedure that maps the values calculated for each $y_{j}$ to a positive value. In the procedure, we avoid setting values directly to zero in order to prevent assigning zero probability to any observed instances. Instead, we use a value which tends towards zero; we insure the minimum value of each $y_{j}$ is at least $\frac{1}{n_{p}}$ and maintain the condition that each set of estimates sums to one. Therefore, we can treat the mapped estimates as probabilities. Algorithm 1 outlines how the procedure accomplishes this mapping. Figure 1 shows the effect of Algorithm 1 when applied to the least squares estimates of the conditional probability mass function for a particular category of a discrete variable.

In words, our procedure is as follows:

1. Shift the estimates such that they are centered about a non-informative center by subtracting $\frac{1}{d}$ (line 6 ).
2. Scale the estimates such that the smallest final values will be at least $\frac{1}{n_{p}}$ (line 7).
3. Shift the scaled estimates back to the original center by adding $\frac{1}{d}$ (line 8).

# Algorithm 1 

Maps least squares estimates to valid probability distributions.

```
Input: \(\boldsymbol{X}_{p, j}, \hat{\boldsymbol{\beta}}_{p, h}\)
Output: probs
1 probs \(=[] ; \quad / /\) list of conditional pdfs
2 for \(j \leftarrow 1\) to \(d\) do
    // calculate least squares estimates
3 \(l=\left\lceil\boldsymbol{x}_{p, j} \hat{\boldsymbol{\beta}}_{p, h}\right\rceil \forall h \in\{1, \ldots, d\} \mid ; \quad / /\) d-vector
    // calculate minimum value
4 \(m_{p, j}=\min \left\{\frac{1}{n_{p}}, l\right\}\)
    // calculate scaling term
5 \(\alpha_{p, j}=\left(\frac{1}{n_{p}}-\frac{1}{d}\right) /\left(m_{p, j}-\frac{1}{d}\right)\)
    // remap estimates
6 \(l=l-\frac{1}{d} ; \quad / /\) element-wise shift
7 \(l=\alpha_{p, j} \cdot l ; \quad / /\) element-wise scale
8 \(l=l+\frac{1}{d} ; \quad / /\) element-wise shift
    // add remap estimates to output
9 probs.append \((l)\);
10 end
```

Since we only want to perform this procedure if one of the least squares estimates is negative, we define $m_{p, j}=\min \left\{\frac{1}{n_{p}}, x_{p, j} \hat{\beta}_{p, h} \forall h\right\}$ so that $m_{p, j}$ is either the minimum estimate for $y_{j}$ or $\frac{1}{n_{p}}$ (line 4). We calculate the scaling factor $a_{p, j}$ (line 5) by noting that we want,

$$
\alpha_{p, j}\left(m_{p, j}-\frac{1}{d}\right)+\frac{1}{d}=\frac{1}{n_{p}}
$$

Solving for $a_{p, j}$ we find,

$$
\alpha_{j}=\frac{\frac{1}{n_{p}}-\frac{1}{k}}{m_{p, j}-\frac{1}{k}}
$$

Note, that if $m_{p, j}=\frac{1}{n_{p}}$, then $a_{p, j}=1$ and we do not transform the estimates. We compute the log likelihood in the discrete case as

$$
\ell_{p}\left(\hat{\boldsymbol{\theta}}_{p} \mid X_{p}, y_{p}\right)=\sum_{j=1}^{n_{p}} \log \left(\alpha_{p, j} x_{p, j} \hat{\boldsymbol{\beta}}_{p, y j}+\frac{1}{d}\left(1-\alpha_{p, j}\right)\right)
$$

We use (21) to calculate $\left(\left(\theta_{p} / X_{p}, y_{p}\right)\right.$ in (14). To find the number of parameters in $p$, we count the number of terms across all $\hat{\boldsymbol{\beta}}_{p, j}$. Each $\hat{\boldsymbol{\beta}}_{p, j}$ has $c \cdot g\left(n_{p}\right)+1$ parameters and $j$ ranges over $d$ categories. However, since Proposition 1 shows the estimated probabilities sum to one, the number of free parameters is

$$
d f_{p}\left(\hat{\boldsymbol{\theta}}_{p}\right)=(k-1)\left(c \cdot g\left(n_{p}\right)+1\right.
$$

As before, BIC uses (14) and (15) to compute the parent-child relationship for $Y_{i}$ given $P a_{i}$.

# 5 Implementation Details and Adaptations 

In this section we consider various adaptations of the two proposed scores. In section 5.1, we discuss a binomial structure prior which allows for efficient learning of large networks. In section 5.2, we discuss a simplification for scoring discrete children which performs well empirically. In section 5.3, we discuss how to adapt our scores into conditional independence test for constraint-based methods.

### 5.1 Binomial Structure Prior

We introduce a structure prior inspired by the binomial distribution. The idea is to give a prior distribution over the number of parents of each variable. We view the addition of each edge as an independent event that occurs with probability $q$. Therefore, we expect to see $q \bullet$ $m^{\prime}$ parents for any given variable where $m^{\prime}$ is the total number of possible parents. Then we have,

$$
\pi(k)=(q)^{k}(1-q)^{m^{\prime}-k}
$$

where $\pi(k)$ is the prior probability that any given variable $Y_{i}$ in DAG $\mathscr{G}$ has $k$ parents. Often it is more convenient to work in log space. Thus we calculate the log prior probability as,

$$
\log \pi(k)=k \log (q)+\left(m^{\prime}-k\right) \log (1-q)
$$

Note that since DAGs encode an ordering over the variables, the total number of possible parents is not necessarily all the variables in the data excluding the variable currently acting as a child. It is usually the case that $m^{\prime} \neq m-1$ where $m$ is the total number of variables in the data.

In section 6, we let $m^{\prime}=m$ in order to calculate the binomial structure prior more efficiency.

We calculate q as $q=\frac{r}{(m-1)}$, where $r$ represents a user-specified upper bound on the expected number of parents of any given node.

Usually, BIC assumes the prior probability of models in equation (1) is distributed uniformly. By using the binomial structure prior instead, we adapt BIC to further penalize networks with complex structure. There are other approaches that use a non-uniform prior for BIC, notability, the extended BIC (EBIC) [4], an similar modification to BIC which aims to address the small- $n$-large- $P$ situation. In section 6.2 we compare both the binomial structure prior and EBIC against the use of a uniform prior.

# 5.2 Multinomial Scoring with Continuous Parents 

Both scores presented in this paper reduce to multinomial scoring in the case of a discrete child with exclusively discrete parents. As an alternative, we explore the use of multinomial scoring when there are discrete children and any combination of parents. Before starting a search, we create discretized versions of each continuous variable using equal frequency binning with a predefined number of bins $b$. Whenever scoring a discrete child, we replace any continuous parents with the precomputed discretized versions of those variables. This allows us to quickly and efficiently perform multinomial scoring for all discrete children. We will henceforth refer to this adaptation as the discretization heuristic and report our finding when choosing $b=3$ as a modification to CG in section 6.4.

### 5.3 As a Conditional Independence Test

We can readily adapt CG and MVP to produce conitional independence tests; to do so, we calculate the log likelihood and degrees of freedom as usual, but perform a likelihood ratio test instead of scoring with BIC. Suppose we wish to test $Y_{0} \Perp Y_{1} \mid Z$ where $Y_{0}$ and $Y_{1}$ are variables (nodes) and Z is a conditioning set of variables. Define $\ell_{0}$ and $d l_{0}$ respectively as the log likelihood and degrees of freedom for $Y_{0}$ given $P a_{0}$ where $P a_{0}=Y_{1} \cup Z$. Further, define $\ell_{0}^{\prime}$ and $d f_{0}^{\prime}$ respectively as the log likelihood and degrees of freedom for $Y_{0}$ given $P a_{0}^{\prime}$ where $P a_{0}^{\prime}=Z$. Perform a likelihood ratio test with test statistic $2\left(\ell_{0}^{\prime}-\ell_{0}^{\prime}\right)$ and $d f_{0}-d f_{0}^{\prime}$ degrees of freedom. This tests whether the model encoding $Y_{0} \Perp Y_{1} \mid Z$ or the model encoding $Y_{0} \Perp Y_{1} \mid Z$ fits the data better. If the scoring method used is not score equivalent, then we must also perform a likelihood ratio test with test statistic $2\left(\ell_{1}^{\prime}-\ell_{1}^{\prime}\right)$ and $d f_{1}-d f_{1}^{\prime}$ degrees of freedom where $Y_{0}$ and $Y_{1}$ are swapped. In this case we decide the variables are dependent if there is enough evidence in either test to support that hypothesis.

## 6 Simulation Studies

To simulate mixed data, we first randomly generate a DAG $\mathscr{G}$ and designate each variable in $\mathscr{G}$ as either discrete or continuous. $\mathscr{G}$ is generated by randomly defining a causal order and adding edges between the variables. Edges are added between randomly chosen pairs of nodes such that the connections are true to the prespecified ordering; they are continually added until the average degree of the graph reaches a user specified amount. Variables in the network without parents are generated according to Gaussian and multinomial distributions. We create temporary discretized versions of each continuous variable using equal frequency

binning with 2 to 5 bins uniformly chosen, for reasons described below. In causal order, we simulate the remaining variables as follows. Continuous variables are generated by partitioning on the discrete parents and randomly parameterizing the coefficients of a linear regression for each partition. Discrete variables are generated via randomly parameterized multinomial distributions of the variable being simulated, the discrete parents, and the discretized versions of the continuous parents. All temporary variables are removed after the simulation is completed. For all simulations, each variable is assigned either continuous or discrete with equal probability. Additionally, discrete variables will have a uniformly chosen number of categories between 2 and 5, inclusive.

In order to prevent the number of multinomial cells for discrete variables from getting too large, we bound the maximum degree of any node in the generated graph to 5. In our experiments, we tested on graphs of average degree 2 and 4. Figures 2 and 3 show the distribution of the node degrees for different settings of average degree. All simulations and comparison took place within the Tetrad system's algorithm comparison tool [20]. Appendix B contains details about how the data were simulated and the parameters used.

We compare CG with and without the discretization heuristic and MVP with g(n_{p}) = 1, g(n_{p}) = √(√g(n_{p})√) using the following performance measures.

1. AP - adjacency precision: the ratio of correctly predicted adjacent to all predicted adjacent
2. AR - adjacency recall: the ratio of correctly predicted adjacent to all true adjacent
3. AHP - arrowhead precision: the ratio of correctly predicted arrowheads to all predicted arrowheads
4. AHR - arrowhead recall: the ratio of correctly predicted arrowheads to all true arrowheads (in found adjacencies)
5. T - elapsed time (seconds)

All results are averaged over 10 randomly simulated graphs and were run on a laptop with an Intel(R) Core I7 @ 3.1 GHz with 16GB of memory. The results in Tables 1 -- 5, used the same simulated dataset and can be directly compared to each other. The results in Tables 6 and 7 each required a different set of simulation parameters and thus use different simulated datasets. Prior to running tests on any algorithm, all continuous data were standardized to have mean 0 and standard deviation 1. As a search algorithm we use fGES [18], an optimized version of GES [5]. In general, algorithms in the GES family perform a two phased search. Starting from a completely disconnected graph, the first phase of the search algorithm greedily adds edges until there is no addition that can improve the score. The second phase then removes edges in the same greedy fashion until no more removals can improve the score. At that point, the current graph will be returned.

### 6.1 The Conditional Gaussian Approximation

We empirically evaluated the choice of approximating a mixture of Gaussians with a single Gaussian for CG (Assumption 3) in Table 1. We denote the use of a single Gaussian as Approx and the use of the correct mixture calculation as Exact. Originally the results did not

appear comparable as the approximate method output a much denser graph than the exact method. In the results shown, we use the binomial structure prior proposed in section 5.1 and achieve comparable results. We see that the approximation performs better in term of precision and comparably in term of recall when compared to the exact method. In the comparisons, we simulate graphs of average degree 2 and 4 with 200 and 1,000 samples and 100 measured variables using fGES. Results are given with the binomial structure prior adustment set to 1 .

### 6.2 Binomial Structure Prior

We tested the usefulness of the binomial structure prior by simulating 200 and 1,000 samples from graphs of average degree 2 and 4 with 100 measured variables using fGES. We compare our scoring functions with and without the binomial structure prior. Additionally we compare against extended BIC (EBIC). In these experiments the binomial structure prior is set to 1 and EBIC's gamma parameter is set to 0.5 upon suggestion of the authors [4]. In Tables 2 and 3 report findings when the average degrees of the graphs are 2 and 4 respectively.

While we set the binomial structure prior's parameter to 1 for the experiments presented in this paper, it is important to note that this parameter can be chosen to be any value greater than 0 . By varying the expected number parents, we can influence how sparse or dense the output graph will be. The choice of a low value results in a relatively sparse graph and a high value in a denser one.

From Table 2 and 3, for both the binomial structure prior and EBIC, we see boosts in precision with a reduction in recall. Additionally, we see vast reductions in the computation times. In general, EBIC seems to work better with small sample sizes. This makes sense, since EBIC is aimed at the small-n-large-P situation. However, for 1,000 samples, we find the binomial structure prior relatively well. We use the binomial structure prior for the remainder of our score based experiments.

### 6.3 Conditional Independence Tests

We tested the usefulness of the CG and MVP scores as conditional independence tests by simulating, 200 and 1,000 samples from graphs of average degree 2 and 4 with 100 measured variables. As a search algorithm, we used CPC Stable [19], which is a modified version of PC [26] that treats ambiguous triples as non-colliders. For independence testing, we set the significance level α = 0.001. Here we also use the discretization heuristic with b = 3 for CG, denoted CGd, however we do not use a structure prior since we are no longer scoring a full Bayesian network in this paradigm. We did not include results for a version of MVP which uses the discretization heuristic because it had little effect. The results are shown in Table 4.

In general, we find that our methods perform better as scores, but still perform reasonably well as conditional independence tests. This is promising for use in algorithms, such as FCI, that model the possibility of latent confounding [26].

6.4 Tests Against Baseline Scores

We used two simple baseline scores as a point of comparison for our methods. The first, which we denote MN, uses multinomial scoring for all cases. In order to do so, we essentially extend the discretization heuristic to the continuous child case so that we are always scoring with a multinomial. The second, which we denote as LR, uses partitioned linear regression in the continuous child case and partitioned logistic regression in the discrete child case. In our experiments, we applied Lib Linear [7], a widely used and efficient toolkit for logistic regression which uses truncated Newton optimization [9]. In a recent paper, Zaidi et al. [27] note that among the many optimization methods that have been evaluated, the truncated Newton method has been shown to converge the fastest, which provides support that Lib Linear is a competitive, state-of-the-art method to apply in our evaluation, as a baseline point of comparison. As with MVP, the appended term on LR denotes the maximum polynomial degree of the regressors.

We compared CG, CGd, MVP 1, LR 1, MVP log n, LR log n, and MN by simulating 200 and 1,000 samples from graphs of average degree 2 and 4 with 100 measured variables. As a search algorithm, we again used fGES. Here we also use the discretization heuristic with b = 3 for CGd and the binomial structure prior set to 1 for all scores. Additionally, boldface text highlights the best performing score for each statistic in each column of the table. The results are shown in Tables 5 and 6. For the results in Table 6, we extended our method for simulating data. Since MVP is designed to handle non-linearity, while CG is not, we modified the continuous child phase of data generation to allow for non-linearities. To do so, we additionally generate second, and third order polynomial terms. However, because of the nature of these non-linear functions, the values of the data often become unmanageably large. To correct for this issue, we resample a variable with square-root and cube-root relationships if the values are too large. Appendix B contains details about how the data were simulated and the parameters used.

Table 5 shows the results when using linearly generated data and 100 variables. As a general pattern, MN had better precision than the CG methods which had better precision than the MVP and LR methods. For recall, just the opposite pattern tended to occur. In terms of timing, in general, MN was faster than the CG methods, which were faster than the MVP methods, which were considerably faster than LR.

Table 6 shows the results when using non-linearly generated data and 100 variables. MN tended to have a higher precision than the MVP and LR methods, which often had higher precision than the CG methods. The relatively good performance of MN is surprising; although multinomial distributions can represent non-linear relationships, the process of discretizing continuous variables loses information; the manner in which we generated the data (see the beginning of section 6) when there is a discrete child and continuous parents may play a role in producing this result. The relatively better precision performance of the MVP methods compared to CG methods is not surprising, given that MVP can model non-linear relationships and CG cannot. In terms of recall, MVP and CG performed comparably, while both performed better than MN. The relative timing results in Table 6 are similar to those in Table 5.

In Tables 5 and 6, there is almost no difference in precision and recall performance between MVP and LR. This result is understandable, since MVP is using an approximation to logistic regression in the case of a discrete child with continuous parents and performing all other cases identically. However, MVP is often 10-fold or more faster than LR.

Table 7 shows the results of assessing the scalability of the methods. We simulated linear data on 500 variables. For average degree 4, no MVP results are shown because our machine ran out of memory while searching. Also, LR is not included at all in Table 7, because LR (as implemented) cannot scale to networks of this size due to time complexity. Table 7 shows that the CG methods had similar precision to MN, which generally had better precision than MVP. For the results shown, the recall of the MVP and CG methods were similar, which were generally better than the recall for MN. MN and the CG methods had similar timing results, which were faster than those of MVP.

In Table 7, we see that the CG and MVP methods are capable of scaling to graphs containing 500 measured variables, albeit sparse ones. CG was able to scale to a slightly denser graph of 500 variables. In general, we see the same performance on these larger networks as before on the networks of 100 measured variables. Additionally, for the smaller sample size of 200, MN performed comparably to CDd, but with a slightly higher precision and lower recall.

## 7 Conclusions

This paper introduces two novel scoring methods for learning Bayesian networks in the presence of both continuous and discrete variables. One of the methods scales to networks of 500 variables or more on a laptop. We introduce a structure prior for learning large networks and find that using a structure prior with BIC generally leads to relatively good network discovery performance, while requiring considerably less computation time. We showed how the CG and MVP scoring methods are readily adapted as conditional independence tests for constraint-based methods to support future use in algorithms such as FCI.

The MVP and LR methods had precision and recall results that were almost identical; however, MVP was considerably faster than LR. Such a speed difference is particularly important when performing Bayesian network learning, where the scoring method must be applied thousands of times in the course of learning a network. Using a different implementation of LR might affect the magnitude of this speed difference, but for the reasons we give in section 4.3, we would not expect it to lead to LR becoming faster than MVP.

The fully discrete approach, MN, performed surprisingly well in our experiments in terms of precision and speed, although recall was often lower, and sometimes much lower, than that of CG and MVP.

The results of the experiments reported here support using CG when recall is a priority and the relationships are linear. If the relationships are likely to be non-linear and recall remains a priority, then we suggest using MVP when there 100 or fewer variables and using CG when there are 500 variables or more. If precision is a priority, then our results support using MN.

All algorithms and simulation reported here were implemented in the Tetrad system [22] and the code is available in the Tetrad repository on GitHub ${ }^{1}$.

There are several directions for future work. First, we would like to apply the methods to real datasets for which knowledge of the causal relationships is available. Second, we would like to expand the CG and MVP methods to model ordinal discrete variables. Although the nominal discrete variables that these methods currently model can represent ordinal variables, we would expect the methods to have greater power when they take advantage of knowledge about particular discrete variables being ordinal versus nominal. Third, we would like to further explore how to adaptively discretize variables in the MN method in order to improve its recall, while not substantially reducing its precision. Fourth, we would like to investigate alternative basis functions to polynomials for the MVP method.

# Acknowledgments 

We thank Clark Glymour, Peter Spirtes, Takis Benos, Dimitrios Manatakis, and Vineet Raghu for helpful discussions about the topics in this paper. We also thank the reviewers for their helpful comments.

Research reported in this publication was supported by grant U54HG008540 from the National Human Genome Research Institute through funds provided by the trans-NIH Big Data to Knowledge (BD2K) initiative, by grant R01LM012087 from the National Library of Medicine, by grant IIS-1636786 from the National Science Foundation, and by grant \#4100070287 from the Pennsylvania Department of Health (PA DOH). The PA DOH specifically disclaims responsibility for any analyses, interpretations, or conclusions. The content of this paper is solely the responsibility of the authors and does not necessarily represent the official views of the granting agencies.

## Appendix A

## Proposition 1

The Conditional Gaussian Score is score equivalent.

## Proof

Let $\mathscr{G}_{1}$ and $\mathscr{G}_{2}$ be directed acyclic graphs with Conditional Gaussian scores $\mathscr{S}_{1}$ and $\mathscr{S}_{2}$ respectively. Further, let $\mathscr{G}_{1} \neq \mathscr{G}_{2}$, but $\mathscr{G}_{1}$ and $\mathscr{G}_{2}$ in the same Markov equivalence class.

Remove all shared local components between $\mathscr{S}_{1}$ and $\mathscr{S}_{2}$ and the corresponding edges in $\mathscr{G}_{1}$ and $\mathscr{G}_{2}$. Call the newly pruned scores $\mathscr{S}_{1}^{\prime}$ and $\mathscr{S}_{2}^{\prime}$ and the newly pruned graphs $\mathscr{G}_{1}^{\prime}$ and $\mathscr{G}_{2}^{\prime}$ respectively. Note that we have removed all initial unshielded colliders common to both $\mathscr{G}_{1}$ and $\mathscr{G}_{2}$. Additionally, it follows from Meek's rules that $\mathscr{G}_{1}^{\prime}$ and $\mathscr{G}_{2}^{\prime}$ must contain no unshielded colliders since any component which could have become an unshielded collider is necessarily shared between graphs $\mathscr{G}_{1}$ and $\mathscr{G}_{2}$ and thus pruned [14].

Since $\mathscr{G}_{1}^{\prime}$ and $\mathscr{G}_{2}^{\prime}$ are acyclic graphs without any unshielded colliders, we can represent them both as a join tree of cliques. Further, they share the same skeleton because they come from

[^0]
[^0]:    ${ }^{1}$ https://github.com/cmu-phil/tetrad

the same Markov equivalence class, and thus, they can be represented by the same join tree of cliques.

It follows from Pearl, Probabilistic Reasoning in Intelligent Systems 3.2.4, Theorem 8, that the distribution encoded by $\mathscr{G}_{1}$ and $\mathscr{G}_{2}$ can be written as a product of the distributions of the cliques of $\mathscr{G}_{1}$ and $\mathscr{G}_{2}$ divided by a product of the distributions of their intersections [16]. Therefore, when we calculate $\mathscr{S}_{1}$ and $\mathscr{S}_{2}$ we can use the same ratio of joint distributions to obtain the log likelihood and degrees of freedom terms. Hence $\mathscr{S}_{1}^{\prime}=\mathscr{S}_{2}^{\prime}$ and therefore, after adding back the shared local components, we have $\mathscr{S}_{1}^{\prime}=\mathscr{S}_{2}$.

# Proposition 2 

If the approximating polynomial from Weierstrass Approximation Theorem for the data generating function is a polynomial of degree d , and the maximum-degree polynomial used by MVP is at least d, then the MVP score will be consistent in the large sample limit.

## Proof

Let $\boldsymbol{p}$ be the approximating polynomial(s) from Weierstrass Approximation Theorem [11]. Assuming the least squares estimate(s) contains the same polynomials degrees as $\boldsymbol{p}$, the least squares estimate will converge to $\boldsymbol{p}$ as the number of samples $n \rightarrow \infty[1]$. Therefore, by Weierstrass Approximation Theorem, the least squares estimate(s) will converge to the true data generating function(s). Accordingly, the log likelihood term of MVP will be maximal for any model that has either been correctly specified or over specified, where by over over specified we are referring to a model containing all the true parameters and more.

However for any over specified model, the parameter penalty will necessarily be larger and hence the MVP score in that case will be lower for the over specified model.

Additionally, in the case of an underspecified model, note that the parameter penalty term is of order $O(\log n)$ while the likelihood term is of order $O(n)$. This means that in the large sample limit, when comparing an underspecified model to any model containing the correctly specified model, the MVP score will be lower for the under specified model since the log likelihood is not maximal while in the other case it is.

Therefore, the MVP score is consistent.

## Proposition 3

The approximated values from least squares regression sum to one.

## Proof

Let the terms in the below equation be defined according to Section 4.3.

$$
\sum_{h=1}^{d} x_{p} \hat{\beta}_{h}=x_{p}\left(X_{p}^{T} x_{p}\right)^{-1} x_{p}^{T} \sum_{h=1}^{d} 1_{\left\{x_{p}=h\right\}}=x_{p}\left(X_{p}^{T} x_{p}\right)^{-1} x_{p}^{T} 1_{p}=1_{p}
$$

For the last step, we use that $\mathbf{1}_{p}$ is in the column space of $\boldsymbol{X}_{p}$ and is thus projected to itself.

# Proposition 4 

If the approximating polynomial from Weierstrass Approximation Theorem for the data generating function is a polynomial of degree d, and the maximum degree polynomial used by MVP is at least d, then the least squares approximations for probability mass functions will be strictly non-negative in the large sample limit.

## Proof

Let $f$ be a generating component of a conditional probability mass function. Since the Weierstrass Approximation Theorem is satisfied by the assumptions of MVP, there must exists a polynomial $p$ such that for every $e>0$ and all $x \in[a, b]$, we have $|f(x)-p(x)|<e$ [11].

For $x \in[a, b]$ where $p(x) \geq f(x), p(x)$ is trivially non-negative since $f(x)>0$.
For $x \in[a, b]$ where $p(x)<f(x)$, let $m=f(x)$ and choose $\varepsilon=\frac{m}{2}$. Then,

$$
\begin{aligned}
& |f(x)-p(x)|<\varepsilon \\
& f(x)-p(x)<\varepsilon \\
& p(x)>f(x)-\varepsilon \\
& p(x)>m-\frac{m}{2} \\
& p(x)>0
\end{aligned}
$$

since $m>0$.
Assuming the least squares estimate(s) contains the same polynomials degrees as $p$, the least squares estimate will converge to $p$ as the number of samples $n \rightarrow \infty$ [1]. Thus, as the number of samples $n \rightarrow \infty$, the least squares approximations are strictly non-negative.

## Appendix B

In this appendix, we detail the parameters used for simulation of the data. Each parameter will be followed by the values we used in simulation and a short description. We split the parameters into 3 groups: general parameters used across all simulations, parameters specific to linear simulation, and parameters specific to non-linear simulation.

## General Parameters

numRuns: 10 - number of runs
numMeasures: 100, 500 - number of measured variables

avgDegree: 2, 4 - average degree of graph
sampleSize: 200, 1000 - sample size
minCategories: 2 - minimum number of categories
maxCategories: 5 - maximum number of categories
percentDiscrete: 50 - percentage of discrete variables $(0-100)$ for mixed data
differentGraphs: true - true if a different graph should be used for each run
maxDegree: 5 - maximum degree of the graph
maxIndegree: 5 - maximum indegree of graph
maxOutdegree: 5 - maximum outdegree of graph
coefSymmetric: true - true if negative coefficient values should be considered

# Linear Parameters 

varLow: 1 - low end of variance range
varHigh: 3 - high end of variance range
coefLow: 0.05 - low end of coefficient range
coefHigh: 1.5 - high end of coefficient range
meanLow: -1 - low end of mean range
meanHigh: 1 - high end of mean range

## Non-linear Parameters

dirichlet: 0.5 - alpha parameter for Dirichlet to draw multinomials
interceptLow: 1 - low end of intercept range
interceptHigh: 2 - high end of intercept range
linearLow: 1.0 - low end of linear coefficient range
linearHigh: 2.0 - high end of linear coefficient range
quadraticLow: 0.5 - low end quadratic coefficient range
quadraticHigh: 1.0 - high end of quadratic coefficient range
cubicLow: 0.2 - low end of cubic coefficient range
cubicHigh: 0.3 - high end of cubic coefficient range
varLow: 0.5 - low end of variance range
varHigh: 0.5 - high end of variance range
