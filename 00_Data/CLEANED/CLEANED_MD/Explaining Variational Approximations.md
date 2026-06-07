University of Wollongong
Research Online
Centre for Statistical \& Survey Methodology Faculty of Engineering and Information
Working Paper Series Sciences
2009

# Explaining Variational Approximations 

## J. T. Ormerod

University of Wollongong, johno@uow.edu.au
M. P. Wand

University of Wollongong, mwand@uow.edu.au

Follow this and additional works at: https://ro.uow.edu.au/cssmwp

## Recommended Citation

Ormerod, J. T. and Wand, M. P., Explaining Variational Approximations, Centre for Statistical and Survey Methodology, University of Wollongong, Working Paper 07-09, 2009, 23p.
https://ro.uow.edu.au/cssmwp/27

Research Online is the open access institutional repository for the University of Wollongong. For further information contact the UOW Library: research-pubs@uow.edu.au

![img-0.jpeg](img-0.jpeg)

# Centre for Statistical and Survey Methodology 

## The University of Wollongong

## Working Paper

$07-09$

## Explaining Variational Approximations.

Ormerod, J.T. and Wand, M.P.

Copyright © 2008 by the Centre for Statistical \& Survey Methodology, UOW. Work in progress, no part of this paper may be reproduced without permission from the Centre.

Centre for Statistical \& Survey Methodology, University of Wollongong, Wollongong NSW 2522. Phone +61 24221 5435, Fax +61 24221 4845. Email: anica@uow.edu.au

# Explaining Variational Approximations 

By J.T. Ormerod \& M.P. WAND ${ }^{1}$<br>1st October, 2009<br>SUMMARY

Variational approximations facilitate approximate inference for the parameters in complex statistical models and provide fast, deterministic alternatives to Monte Carlo methods. However, much of the contemporary literature on variational approximations is in Computer Science rather than Statistics, and uses terminology, notation and examples from the former field. In this article we explain variational approximation in statistical terms. In particular, we illustrate the ideas of variational approximation using examples that are familiar to statisticians.

Keywords: Bayesian inference; Bayesian networks; Directed acyclic graphs; Generalized linear mixed models; Kullback-Leibler divergence; Linear mixed models.

## 1 Introduction

Variational approximations is a body of deterministic techniques for making approximate inference for parameters in complex statistical models. It is now part of mainstream Computer Science methodology, where it enjoys use in elaborate problems such as speech recognition, document retrieval and genetic linkage analysis (Jordan, 2004). Summaries of contemporary variational approximations can be found in Jordan, Ghahramani, Jaakkola \& Saul (1999), Jordan (2004), Titterington (2004) and Bishop (2006, Chapter 10). In 2008, a variational approximation-based software package named Infer.NET (Minka, Winn, Guiver \& Kannan, 2008) emerged with claims of being able to handle a wide variety of statistical problems.

The name 'variational approximations' has its roots in the mathematical topic known as variational calculus. Variational calculus is concerned with the problem of optimizing a functional over a class of functions on which that functional depends. Approximate solutions arise when the class of functions is restricted in some way - usually to enhance tractability.

Despite their statistical overtones, variational approximations are not well-known within the statistical community. In particular, they are overshadowed by Monte Carlo methods, especially Markov chain Monte Carlo (MCMC), for performing approximate inference, as well as Laplace approximation methods. Variational approximations are a much faster alternative to MCMC, especially for large models, and are a richer class of methods than the Laplace variety. They are, however, limited in their approximation accuracy - as opposed to MCMC which can be made arbitrarily accurate through increases in the Monte Carlo sample sizes. In the interests of brevity, we will not discuss the quality of variational approximations in any detail. Jordan (2004) and Titterington (2004) point to some relevant literature on variational approximation accuracy.

In the statistics literature, variational approximations are beginning to have a presence. Examples include Teschendorff et al. (2005), McGrory \& Titterington (2007) and

[^0]
[^0]:    ${ }^{1}$ J.T. Ormerod is a Post-doctoral Research Fellow and M.P. Wand is a Research Professor in Statistics at the Centre for Statistical and Survey Methodology, School of Mathematics and Applied Statistics, University of Wollongong, Wollongong 2522, Australia. We are grateful to an associate editor, two referees for their suggestions for improvement. We also thank Christel Faes, Doug Simpson, Mike Titterington and Shen Wang for helpful comments. This research was partially supported by Australian Research Council Discovery Project DP0877055.

McGrory, Titterington, Reeves \& Pettitt (2009) on new variational approximation methodology for particular applications, and Hall, Humphreys \& Titterington (2002) and Wang \& Titterington (2006) on the statistical properties of estimators obtained via variational approximation.

In this article we explain variational approximation in terms that are familiar to a statistical readership. Most of our exposition involves working through several illustrative examples, starting with what is perhaps the most basic: inference from a Normal random sample. Other contexts that are seen to benefit from variational approximation include Bayesian generalized linear models, Bayesian linear mixed models and non-Bayesian generalized linear mixed models. It is anticipated that a statistically literate reader who works through all of the examples will have gained a good understanding of variational approximations.

Variational approximations can be useful for both likelihood-based and Bayesian inference. However, their utility is much greater for Bayesian inference where intractable calculus problems abound. Hence, most of our description of variational approximations is for Bayesian inference. It is also worth noting that situations in which variational approximations are useful closely correspond to situations where MCMC is useful.

It is helpful, although not necessary, to work with directed acyclic graph (DAG) depictions of Bayesian statistical models. The nodes of the DAG correspond to random variables or random vectors in the Bayesian model, and the directed edges convey conditional independence. Because of this connection with Bayesian (hierarchical) models, DAGs with random nodes are known as Bayesian networks in the Computer Science literature. Figure 1 provides DAGs corresponding to the Bayesian Poisson mixed model (with notation as defined in Section 1.1):

$$
\begin{aligned}
& Y_{i j}\left|U_{i} \stackrel{\text { int }}{=} \operatorname{Poisson}\left(e^{\beta_{0}+U_{i}}\right), i=1,2,3 ; j=1,2, \quad U_{i}\right| \sigma_{U}^{2} \stackrel{\text { ind }}{=} N\left(0, \sigma_{U}^{2}\right) \\
& \beta_{0} \sim N\left(0, \sigma_{\beta_{0}}^{2}\right), \quad \sigma_{U}^{2} \sim \operatorname{IG}(A, B) \quad \text { for constants } \sigma_{\beta_{0}}^{2}, A, B>0
\end{aligned}
$$

The DAG on the left side of Figure 1 has a separate node for each scalar random variable and each constant. The arrows convey the conditional dependence structure. On the right side the constant nodes are suppressed and two of the nodes correspond to the random vectors $\boldsymbol{u} \equiv\left(U_{1}, U_{2}, U_{3}\right)$ and $\boldsymbol{y}=\left(Y_{11}, \ldots, Y_{32}\right)$.

Section 2 explains the most common variant of variational approximation, which we call the density transform approach. A different type, the tangent transform approach, is explained in Section 3. Sections 2 and 3 focus exclusively on Bayesian inference. In Section 4 we point out that the same ideas transfer to frequentist contexts. Some concluding remarks are made in Section 5.

# 1.1 Notation 

Integrals without limits or subscripts are assumed to be over the entire space of the integrand argument. If $\mathcal{P}$ is a logical condition then $I(\mathcal{P})=1$ if $\mathcal{P}$ is true and $I(\mathcal{P})=0$ if $\mathcal{P}$ is false. We use $\Phi$ and $\phi$ to denote the standard normal distribution function and density function, respectively. The Gamma function, denoted by $\Gamma$, is given by $\Gamma(x)=$ $\int_{0}^{\infty} u^{x-1} e^{-u} d u$ and the digamma function, denoted by $\psi$, is given by $\psi(x)=\frac{d}{d x} \log \Gamma(x)$.

Column vectors with entries consisting of sub-scripted variables are denoted by a bold-faced version of the letter for that variable. Round brackets will be used to denote the entries of column vectors. For example $\boldsymbol{x}=\left(x_{1}, \ldots, x_{n}\right)$ denotes a $n \times 1$ vector with entries $x_{1}, \ldots, x_{n}$. Scalar functions applied to vectors are evaluated element-wise. For example,

$$
\exp \left(a_{1}, a_{2}, a_{3}\right) \equiv\left(\exp \left(a_{1}\right), \exp \left(a_{2}\right), \exp \left(a_{3}\right)\right)
$$

Similarly, $\left(a_{1}, a_{2}, a_{3}\right)^{\left(b_{1}, b_{2}, b_{3}\right)} \equiv\left(a_{1}^{b_{1}}, a_{2}^{b_{2}}, a_{3}^{b_{3}}\right)$. The element-wise product of two matrices $\boldsymbol{A}$ and $\boldsymbol{B}$ is denoted by $\boldsymbol{A} \odot \boldsymbol{B}$. We use $\mathbf{1}_{d}$ to denote the $d \times 1$ column vector with all entries

![img-1.jpeg](img-1.jpeg)

Figure 1: DAGs corresponding to the Bayesian Poisson regression model (1). Left: the large nodes correspond to scalar random variables in the model. The smaller nodes correspond to constants and the observed data are shaded. Right: abbreviated DAG for the same model. The constants are suppressed and the nodes $\boldsymbol{u}$ and $\boldsymbol{y}$ correspond to random vectors containing the $U_{i}$ and $y_{i j}$ respectively.
equal to 1 . The norm of a column vector $\boldsymbol{v}$, defined to be $\sqrt{\boldsymbol{v}^{T} \boldsymbol{v}}$ is denoted by $\|\boldsymbol{v}\|$. For a $d \times 1$ vector $\boldsymbol{a}$ we let $\operatorname{diag}(\boldsymbol{a})$ denote the $d \times d$ diagonal matrix containing the the entries of $\boldsymbol{a}$ along the main diagonal. For a $d \times d$ square matrix $\boldsymbol{A}$, we let diagonal $(\boldsymbol{A})$ denote the $d \times 1$ vector containing the diagonal entries of $\boldsymbol{A}$. For square matrices $\boldsymbol{A}_{1}, \ldots, \boldsymbol{A}_{r}$ we let blockdiag $\left(\boldsymbol{A}_{1}, \ldots, \boldsymbol{A}_{r}\right)$ denote the block diagonal matrix, with $i$ th block equal to $\boldsymbol{A}_{i}$.

The density function of a random vector $\boldsymbol{u}$ is denoted by $p(\boldsymbol{u})$. The conditional density of $\boldsymbol{u}$ given $\boldsymbol{v}$ is denoted by $p(\boldsymbol{u} \mid \boldsymbol{v})$. The covariance matrix of $\boldsymbol{u}$ is denoted by $\operatorname{Cov}(\boldsymbol{u})$. A $d \times 1$ random vector $\boldsymbol{x}$ has a Multivariate Normal distribution with parameters $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$, denoted by $\boldsymbol{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, if its density function is

$$
p(\boldsymbol{x})=(2 \pi)^{-d / 2}|\boldsymbol{\Sigma}|^{-1 / 2} \exp \left\{-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu})\right\}
$$

A random variable $x$ has an Inverse Gamma distribution with parameters $A, B>0$, denoted by $x \sim \operatorname{IG}(A, B)$ if its density function is $p(x)=B^{A} \Gamma(A)^{-1} x^{-A-1} e^{-B / x}, x>0$. A random vector $\boldsymbol{x}=\left(x_{1}, \ldots, x_{K}\right)$ has a Dirichlet distribution with parameter vector $\boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{K}\right)$, where each $\alpha_{k}>0$, if its density function is

$$
p(\boldsymbol{x})= \begin{cases}\left\{\Gamma\left(\sum_{k=1}^{K} \alpha_{k}\right) / \prod_{k=1}^{K} \Gamma\left(\alpha_{k}\right)\right\} \prod_{k=1}^{K} x_{k}^{\alpha_{k}-1}, & \sum_{k=1}^{K} x_{k}=1 \\ 0, & \text { otherwise }\end{cases}
$$

We write $\boldsymbol{x} \sim \operatorname{Dirichlet}(\boldsymbol{\alpha})$. If $y_{i}$ has distribution $D_{i}$ for each $1 \leq i \leq n$, and the $y_{i}$ are independent, then we write $y_{i} \stackrel{\text { ind }}{ } D_{i}$.

# 2 Density Transform Approach 

The density transform approach to variational approximation involves approximation of posterior densities by other densities for which inference is more tractable. The approximations are guided by the notion of Kullback-Leibler divergence, which we now explain.

# 2.1 Kullback-Leibler Divergence 

Consider a generic Bayesian model with parameter vector $\boldsymbol{\theta} \in \Theta$ and observed data vector $\boldsymbol{y}$. Bayesian inference is based on the posterior density function

$$
p(\boldsymbol{\theta} \mid \boldsymbol{y})=\frac{p(\boldsymbol{y}, \boldsymbol{\theta})}{p(\boldsymbol{y})}
$$

The denominator $p(\boldsymbol{y})$ is known as the marginal likelihood (or model evidence in the Computer Science literature) and forms the basis of model comparison via Bayes factors (e.g. Kass \& Raftery, 1995). Throughout this section we assume that $\boldsymbol{y}$ and $\boldsymbol{\theta}$ are continuous random vectors. The discrete case has a similar treatment, but with summations rather than integrals.

Let $q$ be an arbitrary density function over $\Theta$. Then the logarithm of the marginal likelihood satisfies

$$
\begin{aligned}
\log p(\boldsymbol{y}) & =\log p(\boldsymbol{y}) \int q(\boldsymbol{\theta}) d \boldsymbol{\theta}=\int q(\boldsymbol{\theta}) \log p(\boldsymbol{y}) d \boldsymbol{\theta} \\
& =\int q(\boldsymbol{\theta}) \log \left\{\frac{p(\boldsymbol{y}, \boldsymbol{\theta}) / q(\boldsymbol{\theta})}{p(\boldsymbol{\theta} \mid \boldsymbol{y}) / q(\boldsymbol{\theta})}\right\} d \boldsymbol{\theta} \\
& =\int q(\boldsymbol{\theta}) \log \left\{\frac{p(\boldsymbol{y}, \boldsymbol{\theta})}{q(\boldsymbol{\theta})}\right\} d \boldsymbol{\theta}+\int q(\boldsymbol{\theta}) \log \left\{\frac{q(\boldsymbol{\theta})}{p(\boldsymbol{\theta} \mid \boldsymbol{y})}\right\} d \boldsymbol{\theta} \\
& \geq \int q(\boldsymbol{\theta}) \log \left\{\frac{p(\boldsymbol{y}, \boldsymbol{\theta})}{q(\boldsymbol{\theta})}\right\} d \boldsymbol{\theta}
\end{aligned}
$$

The inequality arises from the fact that

$$
\begin{aligned}
& \int q(\boldsymbol{\theta}) \log \left\{\frac{q(\boldsymbol{\theta})}{p(\boldsymbol{\theta} \mid \boldsymbol{y})}\right\} d \boldsymbol{\theta} \geq 0 \quad \text { for all densities } q \\
& \text { with equality if and only if } q(\boldsymbol{\theta})=p(\boldsymbol{\theta} \mid \boldsymbol{y}) \text { almost everywhere }
\end{aligned}
$$

(Kullback \& Leibler, 1951). The integral in (3) is known as the Kullback-Leibler distance between $q$ and $p(\cdot \mid \boldsymbol{y})$. Note that the lower bound $\underline{p}(\boldsymbol{y} ; q)$ can also be derived more directly using Jensen's inequality, but the above derivation has the advantage of quantifying the gap between $p(\boldsymbol{y})$ and $\underline{p}(\boldsymbol{y} ; q)$. From (2), it follows immediately that

$$
p(\boldsymbol{y}) \geq \underline{p}(\boldsymbol{y} ; q)
$$

where the $q$-dependent lower bound on the marginal likelihood is given by

$$
\underline{p}(\boldsymbol{y} ; q) \equiv \exp \int q(\boldsymbol{\theta}) \log \left\{\frac{p(\boldsymbol{y}, \boldsymbol{\theta})}{q(\boldsymbol{\theta})}\right\} d \boldsymbol{\theta}
$$

The essence of the density transform variational approach is approximation of the posterior density $p(\boldsymbol{\theta} \mid \boldsymbol{y})$ by a $q(\boldsymbol{\theta})$ for which $\underline{p}(\boldsymbol{y} ; q)$ is more tractable than $p(\boldsymbol{y})$. Tractability is achieved by restricting $q$ to a more manageable class of densities, and then maximizing $\underline{p}(\boldsymbol{y} ; q)$ over that class. According to (2), maximization of $\underline{p}(\boldsymbol{y} ; q)$ is equivalent to minimization of the Kullback-Leibler distance or divergence between $q$ and $p(\cdot \mid \boldsymbol{y})$.

The most common restrictions for the $q$ density are:
(a) $q(\boldsymbol{\theta})$ factorizes into $\prod_{i=1}^{M} q_{i}\left(\boldsymbol{\theta}_{i}\right)$, for some partition $\left\{\boldsymbol{\theta}_{1}, \ldots, \boldsymbol{\theta}_{M}\right\}$ of $\boldsymbol{\theta}$.
(b) $q$ is a member of a parametric family of density functions.

In the case of (a), note that the product form is the only assumption being made. Hence (a) represents a type of nonparametric restriction. Restriction (a) is also known as mean field approximation and has its roots in physics (e.g. Parisi, 1988). The term variational Bayes has become commonplace for approximate Bayesian inference under product density restrictions.

Depending on the Bayesian model at hand, both restrictions can have minor or major impacts on the resulting inference. For example, if $p\left(\boldsymbol{\theta}_{1}, \boldsymbol{\theta}_{2} \mid \boldsymbol{y}\right)$ is such that $\boldsymbol{\theta}_{1}$ and $\boldsymbol{\theta}_{2}$ have

a high degree of dependence then the restriction $q\left(\boldsymbol{\theta}_{1}, \boldsymbol{\theta}_{2}\right)=q_{1}\left(\boldsymbol{\theta}_{1}\right) q_{2}\left(\boldsymbol{\theta}_{2}\right)$ will lead to a degradation in the resulting inference. Conversely, if the posterior dependence between $\boldsymbol{\theta}_{1}$ and $\boldsymbol{\theta}_{2}$ is weak then the product density restriction could lead to very accurate approximate inference. Further discussion on this topic, including references, may be found in Section 3.2 of Titterington (2004).

# 2.2 Product Density Transforms 

Restriction of $q$ to a sub-class of product densities gives rise to explicit solutions for each product component in terms of the others. These, in turn, lead to an iterative scheme for obtaining the simultaneous solution. The solutions rely on the following result, which we call Result 1. Note that Result 1 follows immediately from (2) and (3) above. However, it is useful to present the result for general random vectors.

Result 1. Let $\boldsymbol{u}$ and $\boldsymbol{v}$ be two continuous random vectors with joint density function $p(\boldsymbol{u}, \boldsymbol{v})$. The maximum value of

$$
\int q(\boldsymbol{u}) \log \left\{\frac{p(\boldsymbol{u}, \boldsymbol{v})}{q(\boldsymbol{u})}\right\} d \boldsymbol{u}
$$

over all density functions $q$ is attained by $q^{*}(\boldsymbol{u})=p(\boldsymbol{u} \mid \boldsymbol{v})$.
Return now to the Bayesian model setting of Section 2.1 and suppose that $q$ is subject to the product restriction (a). Then

$$
\begin{aligned}
\log \underline{p}(\boldsymbol{y} ; q)= & \int \prod_{i=1}^{M} q_{i}\left(\boldsymbol{\theta}_{i}\right)\left\{\log p(\boldsymbol{y}, \boldsymbol{\theta})-\sum_{i=1}^{m} \log q_{i}\left(\boldsymbol{\theta}_{i}\right)\right\} d \boldsymbol{\theta}_{1} \cdots d \boldsymbol{\theta}_{M} \\
= & \int q_{1}\left(\boldsymbol{\theta}_{1}\right)\left\{\int \log p(\boldsymbol{y}, \boldsymbol{\theta}) q_{2}\left(\boldsymbol{\theta}_{2}\right) \cdots q_{M}\left(\boldsymbol{\theta}_{M}\right) d \boldsymbol{\theta}_{2} \cdots d \boldsymbol{\theta}_{M}\right\}-\int q_{1}\left(\boldsymbol{\theta}_{1}\right) \log q_{1}\left(\boldsymbol{\theta}_{1}\right) d \boldsymbol{\theta}_{1} \\
& +\text { terms not involving } q_{1} .
\end{aligned}
$$

Define the new joint density function $\widetilde{p}\left(\boldsymbol{y}, \boldsymbol{\theta}_{1}\right)$ by

$$
\widetilde{p}\left(\boldsymbol{y}, \boldsymbol{\theta}_{1}\right) \equiv \frac{\exp \int \log p(\boldsymbol{y}, \boldsymbol{\theta}) q_{2}\left(\boldsymbol{\theta}_{2}\right) \cdots q_{M}\left(\boldsymbol{\theta}_{M}\right) d \boldsymbol{\theta}_{2} \cdots d \boldsymbol{\theta}_{M}}{\iint\left\{\exp \int \log p(\boldsymbol{y}, \boldsymbol{\theta}) q_{2}\left(\boldsymbol{\theta}_{2}\right) \cdots q_{M}\left(\boldsymbol{\theta}_{M}\right) d \boldsymbol{\theta}_{2} \cdots d \boldsymbol{\theta}_{M}\right\} d \boldsymbol{\theta}_{1} d \boldsymbol{y}}
$$

Then

$$
\log \underline{p}(\boldsymbol{y} ; q)=\int q_{1}\left(\boldsymbol{\theta}_{1}\right) \log \left\{\frac{\widetilde{p}\left(\boldsymbol{y}, \boldsymbol{\theta}_{1}\right)}{q\left(\boldsymbol{\theta}_{1}\right)}\right\} d \boldsymbol{\theta}_{1}+\text { terms not involving } q_{1}
$$

By Result 1, the optimal $q_{1}$ is then

$$
q_{1}^{*}\left(\boldsymbol{\theta}_{1}\right)=\widetilde{p}\left(\boldsymbol{\theta}_{1} \mid \boldsymbol{y}\right) \equiv \frac{\widetilde{p}\left(\boldsymbol{y}, \boldsymbol{\theta}_{1}\right)}{\int \widetilde{p}\left(\boldsymbol{y}, \boldsymbol{\theta}_{1}\right) d \boldsymbol{\theta}_{1}} \propto \exp \left\{\int \log p(\boldsymbol{y}, \boldsymbol{\theta}) q_{2}\left(\boldsymbol{\theta}_{2}\right) \cdots q_{M}\left(\boldsymbol{\theta}_{M}\right) d \boldsymbol{\theta}_{2} \cdots d \boldsymbol{\theta}_{M}\right\}
$$

Repeating the same argument for maximizing $\log \underline{p}(\boldsymbol{y} ; q)$ over each of $q_{2}, \ldots, q_{M}$ leads to the optimal densities satisfying:

$$
q_{i}^{*}\left(\boldsymbol{\theta}_{i}\right) \propto \exp \left\{E_{-\boldsymbol{\theta}_{i}} \log p(\boldsymbol{y}, \boldsymbol{\theta})\right\}, \quad 1 \leq i \leq M
$$

where $E_{-\boldsymbol{\theta}_{i}}$ denotes expectation with respect to the density $\prod_{j \neq i} q_{j}\left(\boldsymbol{\theta}_{j}\right)$. The iterative scheme, labelled Algorithm 1, can be used to solve for the $q_{i}^{*}$.

Convexity properties can be used to show that convergence to at least local optima is guaranteed (Boyd \& Vandenberghe, 2004). If conjugate priors are used then the $q_{i}^{*}$ belong to recognizable density families and the $q_{i}^{*}$ updates reduce to updating parameters in the $q_{i}^{*}$ family (e.g. Winn \& Bishop, 2005). Also, in practice it is common to monitor convergence using $\log \{\underline{p}(\boldsymbol{y} ; q)\}$ rather than $\underline{p}(\boldsymbol{y} ; q)$. Sections 2.2.2-2.2.4 provide illustrations.

Initialize: $q_{2}^{*}\left(\boldsymbol{\theta}_{2}\right), \ldots, q_{M}^{*}\left(\boldsymbol{\theta}_{M}\right)$.
Cycle:

$$
\begin{gathered}
q_{1}^{*}\left(\boldsymbol{\theta}_{1}\right) \leftarrow \frac{\exp \left\{E_{-\boldsymbol{\theta}_{1}} \log p(\boldsymbol{y}, \boldsymbol{\theta})\right\}}{\int \exp \left\{E_{-\boldsymbol{\theta}_{1}} \log p(\boldsymbol{y}, \boldsymbol{\theta})\right\} d \boldsymbol{\theta}_{1}} \\
\vdots \\
q_{M}^{*}\left(\boldsymbol{\theta}_{M}\right) \leftarrow \frac{\exp \left\{E_{-\boldsymbol{\theta}_{M}} \log p(\boldsymbol{y}, \boldsymbol{\theta})\right\}}{\int \exp \left\{E_{-\boldsymbol{\theta}_{M}} \log p(\boldsymbol{y}, \boldsymbol{\theta})\right\} d \boldsymbol{\theta}_{M}}
\end{gathered}
$$

until the increase in $\underline{p}(\boldsymbol{y} ; q)$ is negligible.

Algorithm 1: Iterative scheme for obtaining the optimal densities under product density restriction (a). The updates are based on the solutions given at (5).

# 2.2.1 Connection with Gibbs Sampling 

It is easily shown that a valid alternative expression for the $q_{i}^{*}\left(\boldsymbol{\theta}_{i}\right)$ is

$$
q_{i}^{*}\left(\boldsymbol{\theta}_{i}\right) \propto \exp \left\{E_{-\boldsymbol{\theta}_{i}} \log p\left(\boldsymbol{\theta}_{i} \mid \text { rest }\right)\right\}
$$

where

$$
\text { rest } \equiv\left\{\boldsymbol{y}, \boldsymbol{\theta}_{1}, \ldots, \boldsymbol{\theta}_{i-1}, \boldsymbol{\theta}_{i+1}, \ldots, \boldsymbol{\theta}_{M}\right\}
$$

is the set containing the rest of the random vectors in the model, apart from $\boldsymbol{\theta}_{i}$. The distributions $\boldsymbol{\theta}_{i} \mid$ rest, $1 \leq i \leq M$, are known, in the MCMC literature, as the full conditionals. This form of the optimal densities reveals a link with Gibbs sampling (e.g. George \& Casella, 1992) which involves successive draws from these full conditionals. Indeed, it becomes apparent from the upcoming examples that the product density transform approach leads to tractable solutions in situations where Gibbs sampling is also viable.

The DAG viewpoint of Bayesian models also gives rise to a useful result arising from the notion of Markov blankets. The Markov blanket of a node is the set of children, parents and co-parents of that node. The result

$$
p\left(\boldsymbol{\theta}_{i} \mid \text { rest }\right)=p\left(\boldsymbol{\theta}_{i} \mid \text { Markov blanket of } \boldsymbol{\theta}_{i}\right)
$$

(Pearl, 1988) means that determination of the required full conditionals involves localized calculations on the DAG. It follows from this fact and expression (6) that the product density approach involves a series of local operations. In Computer Science, this has become known as variational message passing (Winn \& Bishop, 2005). See the example in Section 2.2.3 for illustration of (7) and localization of variational updates.

### 2.2.2 Normal random sample

Our first and most detailed illustration of variational approximation involves approximate Bayesian inference for the most familiar of statistical settings: a random sample from a Normal distribution. Specifically, consider

$$
X_{i} \mid \mu, \sigma^{2} \stackrel{\text { red }}{\sim} N\left(\mu, \sigma^{2}\right)
$$

with conjugate priors

$$
\mu \sim N\left(\mu_{\mu}, \sigma_{\mu}^{2}\right) \quad \text { and } \quad \sigma^{2} \sim \operatorname{IG}(A, B)
$$

The product density transform approximation to $p\left(\mu, \sigma^{2} \mid \boldsymbol{x}\right)$ is

$$
q(\mu, \sigma)=q_{\mu}(\mu) q_{\sigma^{2}}\left(\sigma^{2}\right)
$$

The optimal densities take the form

$$
q_{\mu}^{*}(\mu) \propto \exp \left[E_{\sigma^{2}}\left\{\log p\left(\mu \mid \sigma^{2}, \boldsymbol{x}\right)\right\}\right] \quad \text { and } \quad q_{\sigma^{2}}^{*}\left(\sigma^{2}\right) \propto \exp \left[E_{\mu}\left\{\log p\left(\sigma^{2} \mid \mu, \boldsymbol{x}\right)\right\}\right]
$$

where $\boldsymbol{x}=\left(X_{1}, \ldots, X_{n}\right)$. Standard manipulations lead to the full conditionals being
$\mu \mid \sigma^{2}, \boldsymbol{x} \sim N\left(\frac{n \bar{X} / \sigma^{2}+\mu_{\mu} / \sigma_{\mu}^{2}}{n / \sigma^{2}+1 / \sigma_{\mu}^{2}}, \frac{1}{n / \sigma^{2}+1 / \sigma_{\mu}^{2}}\right)$ and $\sigma^{2} \mid \mu, \boldsymbol{x} \sim \operatorname{IG}\left(A+\frac{n}{2}, B+\frac{1}{2}\left\|\boldsymbol{x}-\mu \mathbf{1}_{n}\right\|^{2}\right)$
where $\bar{X}=\left(X_{1}+\ldots+X_{n}\right) / n$ is the sample mean. The second of these, combined with (6), leads to

$$
\begin{aligned}
q_{\sigma^{2}}^{*}\left(\sigma^{2}\right) & \propto \exp E_{\mu}\left\{-\left(A+\frac{n}{2}+1\right) \log \left(\sigma^{2}\right)-\left(B+\frac{1}{2}\left\|\boldsymbol{x}-\mu \mathbf{1}_{n}\right\|^{2}\right) / \sigma^{2}\right\} \\
& \propto\left(\sigma^{2}\right)^{-\left(A+\frac{n}{2}+1\right)} \exp \left\{-\left(B+E_{\mu}\left\|\boldsymbol{x}-\mu \mathbf{1}_{n}\right\|^{2}\right) / \sigma^{2}\right\}
\end{aligned}
$$

We recognize this as a member of the Inverse Gamma family:

$$
q_{\sigma^{2}}^{*}\left(\sigma^{2}\right) \quad \text { is } \quad \operatorname{IG}\left(A+\frac{n}{2}, B+\frac{1}{2} E_{\mu}\left\|\boldsymbol{x}-\mu \mathbf{1}_{n}\right\|^{2}\right)
$$

Note that $E_{\mu}\left\|\boldsymbol{x}-\mu \mathbf{1}_{n}\right\|^{2}=\left\|\boldsymbol{x}-E_{\mu}(\mu) \mathbf{1}_{n}\right\|^{2}+n \operatorname{Var}_{\mu}(\mu)$ where

$$
E_{\mu}(\mu)=\int_{-\infty}^{\infty} \mu_{0} q_{\mu}\left(\mu_{0}\right) d \mu_{0} \quad \text { and } \quad \operatorname{Var}_{\mu}(\mu)=\int_{-\infty}^{\infty}\left\{\mu_{0}-E_{\mu}(\mu)\right\}^{2} q_{\mu}\left(\mu_{0}\right) d \mu_{0}
$$

are the mean and variance of the $q_{\mu}$ density. Similar arguments lead to

$$
q_{\mu}^{*}(\mu) \quad \text { is } \quad N\left(\frac{n \bar{X} E_{\sigma^{2}}\left(1 / \sigma^{2}\right)+\mu_{\mu} / \sigma_{\mu}^{2}}{n E_{\sigma^{2}}\left(1 / \sigma^{2}\right)+1 / \sigma_{\mu}^{2}}, \frac{1}{n E_{\sigma^{2}}\left(1 / \sigma^{2}\right)+1 / \sigma_{\mu}^{2}}\right)
$$

where $E_{\sigma^{2}}\left(1 / \sigma^{2}\right)=\int_{0}^{\infty}\left(1 / \sigma_{0}^{2}\right) q_{\sigma^{2}}\left(\sigma_{0}^{2}\right) d \sigma_{0}^{2}$. When $q_{\sigma^{2}}=q_{\sigma^{2}}^{*}$ we get

$$
E_{\sigma^{2}}\left(1 / \sigma^{2}\right)=\frac{A+n / 2}{B+\frac{1}{2}\left\{\left\|\boldsymbol{x}-E_{\mu}(\mu) \mathbf{1}_{n}\right\|^{2}+n \operatorname{Var}_{\mu}(\mu)\right\}}
$$

It is now apparent that the functional forms of the optimal densities $q_{\mu}^{*}$ and $q_{\sigma^{2}}^{*}$ are Normal and Inverse Gaussian respectively, but the parameters need to be determined from relationships such as (9) and (10). Let

$$
\mu_{q(\mu)} \equiv E_{\mu}(\mu), \quad \sigma_{q(\mu)}^{2} \equiv \operatorname{Var}_{\mu}(\mu) \quad \text { and } \quad B_{q\left(\sigma^{2}\right)} \equiv\left(A+\frac{n}{2}\right) / E\left(1 / \sigma^{2}\right)
$$

Using the relationships established at (9) and (10) we arrive at Algorithm 2, which can be used to obtain the optimal values of $\mu_{q(\mu)}, \sigma_{q(\mu)}^{2}$ and $B_{q\left(\sigma^{2}\right)}$.

Note that $\log \underline{p}(\boldsymbol{x} ; q)$ admits the explicit expression:

$$
\begin{aligned}
\log \underline{p}(\boldsymbol{x} ; q)= & \frac{1}{2}-\frac{n}{2} \log (2 \pi)+\frac{1}{2} \log \left(\sigma_{q(\mu)}^{2} / \sigma_{\mu}^{2}\right)-\frac{\left(\mu_{q(\mu)}-\mu_{\mu}\right)^{2}+\sigma_{q(\mu)}^{2}}{2 \sigma_{\mu}^{2}} \\
& +A \log (B)-\left(A+\frac{n}{2}\right) \log \left(B_{q\left(\sigma^{2}\right)}\right)+\log \Gamma\left(A+\frac{n}{2}\right)-\log \Gamma(A)
\end{aligned}
$$

However, within each iteration of Algorithm 2, this expression is valid only after each of the parameter updates have been made.

Initialize: $B_{q\left(\sigma^{2}\right)}>0$.
Cycle:

$$
\begin{aligned}
& \sigma_{q(\mu)}^{2} \leftarrow\left\{n\left(A+\frac{n}{2}\right) / B_{q\left(\sigma^{2}\right)}+1 / \sigma_{\mu}^{2}\right\}^{-1} \\
& \mu_{q(\mu)} \leftarrow\left\{n \bar{X}\left(A+\frac{n}{2}\right) / B_{q\left(\sigma^{2}\right)}+\mu_{\mu} / \sigma_{\mu}^{2}\right\} \sigma_{q(\mu)}^{2} \\
& B_{q\left(\sigma^{2}\right)} \leftarrow B+\frac{1}{2}\left(\left\|\boldsymbol{x}-\mu_{q(\mu)} \mathbf{1}_{n}\right\|^{2}+n \sigma_{q(\mu)}^{2}\right)
\end{aligned}
$$

until the increase in $\underline{p}(\boldsymbol{x} ; q)$ is negligible.

Algorithm 2: Iterative scheme for obtaining the parameters in the optimal densities $q_{\mu}^{*}$ and $q_{\sigma^{2}}^{*}$ in the normal random sample example.

Upon convergence to $\mu_{q(\mu)}^{*},\left(\sigma_{q(\mu)}^{2}\right)^{*}$ and $B_{q\left(\sigma^{2}\right)}^{*}$, the approximations to the individual posterior densities are:

$$
p(\mu \mid \boldsymbol{x}) \approx\left\{2 \pi\left(\sigma_{q(\mu)}^{2}\right)^{*}\right\}^{-1 / 2} \exp \left[-\left(\mu-\mu_{q(\mu)}^{*}\right)^{2} /\left\{2\left(\sigma_{q(\mu)}^{2}\right)^{*}\right\}\right]
$$

and

$$
p\left(\sigma^{2} \mid \boldsymbol{x}\right) \approx \frac{\left(B_{q\left(\sigma^{2}\right)}^{*}\right)^{A+\frac{n}{2}}}{\Gamma\left(A+\frac{n}{2}\right)}\left(\sigma^{2}\right)^{-A-\frac{n}{2}-1} \exp \left(B_{q\left(\sigma^{2}\right)}^{*} / \sigma^{2}\right), \quad \sigma^{2}>0
$$

Figure 2 illustrates these variational approximations for a simulated sample of size $n=20$ from the $N(100,225)$ density. For priors we used $\mu \sim N\left(0,10^{8}\right)$ and $\sigma^{2} \sim \operatorname{IG}\left(\frac{1}{100}, \frac{1}{100}\right)$, corresponding to vague beliefs about the mean and variance, and such that the prior mean of the precision, $1 / \sigma^{2}$, is unity. The initial value for the iterative scheme is $B_{q\left(\sigma^{2}\right)}=1$. The exact posterior densities, obtained via highly accurate quadrature, are also displayed. Note that, in this example, convergence is very rapid and the accuracy of the variational approximation is quite good.
![img-2.jpeg](img-2.jpeg)

Figure 2: Results from applying the product density variational approximation to a simulated normal random sample. The exact posterior density functions are added for comparison. The vertical dotted line in the posterior density plots correspond to the true value of the parameter.

# 2.2.3 Linear Mixed Model 

The Bayesian version of the Gaussian linear mixed model takes the general form

$$
\boldsymbol{y} \mid \boldsymbol{\beta}, \boldsymbol{u}, \boldsymbol{G}, \boldsymbol{R} \sim N(\boldsymbol{X} \boldsymbol{\beta}+\boldsymbol{Z} \boldsymbol{u}, \boldsymbol{R}), \quad \boldsymbol{u} \mid \boldsymbol{G} \sim N(\mathbf{0}, \boldsymbol{G})
$$

where $\boldsymbol{y}$ is an $n \times 1$ vector of response variables, $\boldsymbol{\beta}$ is a $p \times 1$ vector of fixed effects, $\boldsymbol{u}$ is a vector of random effects, $\boldsymbol{X}$ and $\boldsymbol{Z}$ are corresponding design matrices and $\boldsymbol{G}$ and $\boldsymbol{R}$ are covariance matrices. While several possibilities exist for $\boldsymbol{G}$ and $\boldsymbol{R}$ (e.g. McCulloch, Searle \& Neuhaus, 2008), we restrict attention here to variance component models with

$$
\boldsymbol{G}=\operatorname{blockdiag}\left(\sigma_{u 1}^{2} \boldsymbol{I}_{K_{1}}, \ldots, \sigma_{u r}^{2} \boldsymbol{I}_{K_{r}}\right) \quad \text { and } \quad \boldsymbol{R}=\sigma_{\varepsilon}^{2} \boldsymbol{I}
$$

We also impose the conjugate priors:

$$
\boldsymbol{\beta} \sim N\left(\mathbf{0}, \sigma_{\beta}^{2} \boldsymbol{I}\right), \quad \sigma_{u \ell}^{2} \sim \operatorname{IG}\left(A_{u \ell}, B_{u \ell}\right), 1 \leq \ell \leq r, \quad \sigma_{\varepsilon}^{2} \sim \operatorname{IG}\left(A_{\varepsilon}, B_{\varepsilon}\right)
$$

for some $\sigma_{\beta}^{2}, A_{u \ell}, B_{u \ell}, A_{\varepsilon}, B_{\varepsilon}>0$. Figure 3 is the DAG corresponding to model (11)-(13).
![img-3.jpeg](img-3.jpeg)

Figure 3: DAG corresponding to the model (11)-(13).
Somewhat remarkably, a tractable solution arises for the two-component product

$$
q\left(\boldsymbol{\beta}, \boldsymbol{u}, \sigma_{u 1}^{2}, \ldots, \sigma_{u r}^{2}, \sigma_{\varepsilon}^{2}\right)=q_{\boldsymbol{\beta}, \boldsymbol{u}}(\boldsymbol{\beta}, \boldsymbol{u}) q_{\boldsymbol{\sigma}^{2}}\left(\sigma_{u 1}^{2}, \ldots, \sigma_{u r}^{2}, \sigma_{\varepsilon}^{2}\right)
$$

Application of (5) leads to the optimal densities taking the form

$$
\begin{aligned}
& q_{\boldsymbol{\beta}, \boldsymbol{u}}^{*}(\boldsymbol{\beta}, \boldsymbol{u}) \text { is a Multivariate Normal density function, } \\
& q_{\boldsymbol{\sigma}^{2}}^{*} \text { is a product of } r+1 \text { Inverse Gamma density functions. }
\end{aligned}
$$

It should be stressed that these forms are not imposed at the outset, but arise as optimal solutions for model (11)-(13) and product restriction (14). Moreover, the factorization of $q_{\boldsymbol{\sigma}^{2}}^{*}$ into $r+1$ separate components is also a consequence of (5) for the current model, rather than an imposition. This example also benefits from the Markov blanket result (7) described in Section 2.2.1 and Figure 3. For example, the full conditional density of $\sigma_{u 1}^{2}$ is

$$
p\left(\sigma_{u 1}^{2} \mid \text { rest }\right)=p\left(\sigma_{u 1}^{2} \mid \text { Markov blanket of } \sigma_{u 1}^{2}\right)=p\left(\sigma_{u 1}^{2} \mid \boldsymbol{u}, \sigma_{u 2}^{2}, \ldots, \sigma_{u r}^{2}\right)
$$

Hence, determination of $q_{\sigma_{\sigma_{i}}}^{*}$ requires calculations involving only the subset of the DAG consisting of $\boldsymbol{u}$ and the variance parameters.

Let $\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}$ and $\boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}$ be the mean and covariance matrix for the $q_{\boldsymbol{\beta}, \boldsymbol{u}}^{*}$ density and set $\boldsymbol{C} \equiv[\boldsymbol{X} \boldsymbol{Z}]$. For the $q_{\boldsymbol{\sigma}^{2}}^{*}$ density the shape parameters for the $r+1$ components can be shown to be deterministic: $A_{u 1}+\frac{1}{2} K_{1}, \ldots, A_{u r}+\frac{1}{2} K_{r}, A_{\varepsilon}+\frac{1}{2} n$. Let $B_{q\left(\sigma_{u 1}^{2}\right)}, \ldots, B_{q\left(\sigma_{u r}^{2}\right)}, B_{q\left(\sigma_{\varepsilon}^{2}\right)}$ be the accompanying rate parameters. The relationships between $\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)$ and $\left(B_{q\left(\sigma_{u 1}^{2}\right)}, \ldots, B_{q\left(\sigma_{u r}^{2}\right)}, B_{q\left(\sigma_{\varepsilon}^{2}\right)}\right)$ enforced by (5) lead to the iterative scheme in Algorithm 3. The scheme uses notation such as $\left(\boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{u}_{\ell}}$, which is defined as follows. Note that restriction (12) means that

$$
\operatorname{Cov}\left[\begin{array}{l}
\boldsymbol{\beta} \\
\boldsymbol{u}
\end{array}\right]=\operatorname{blockdiag}\left(\sigma_{\beta}^{2} \boldsymbol{I}, \sigma_{u 1}^{2} \boldsymbol{I}_{K_{1}}, \ldots, \sigma_{u r}^{2} \boldsymbol{I}_{K_{r}}\right)
$$

Let $\left(\boldsymbol{\beta}, \boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}\right)$ be the partition of $(\boldsymbol{\beta}, \boldsymbol{u})$ corresponding to the blocks in (15) (for example, $\operatorname{Cov}\left(\boldsymbol{u}_{1}\right)=\sigma_{u 1}^{2} \boldsymbol{I}_{K_{1}}$ ). Then

$$
\left(\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{\beta}},\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{u}_{1}}, \ldots,\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{u}_{r}}\right)
$$

is the partition of $\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}$ corresponding to $\left(\boldsymbol{\beta}, \boldsymbol{u}_{1}, \ldots, \boldsymbol{u}_{r}\right)$. Similarly, $\left(\boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{u}_{\ell}}$ is the $K_{\ell} \times K_{\ell}$ diagonal block of $\boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}$ with rows and columns corresponding to the position of $\boldsymbol{u}_{\ell}$ within $(\boldsymbol{\beta}, \boldsymbol{u})$.

Initialize: $B_{q\left(\sigma_{\varepsilon}^{2}\right)}, B_{q\left(\sigma_{u 1}^{2}\right)}, \ldots, B_{q\left(\sigma_{u r}^{2}\right)}>0$.
Cycle:

$$
\begin{aligned}
& \boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})} \leftarrow\left\{\frac{A_{\varepsilon}+\frac{n}{2}}{B_{q\left(\sigma_{\varepsilon}^{2}\right)}} \boldsymbol{C}^{T} \boldsymbol{C}+\operatorname{blockdiag}\left(\sigma_{\beta}^{-2} \boldsymbol{I}_{p}, \frac{A_{u 1}+\frac{1}{2} K_{1}}{B_{q\left(\sigma_{u 1}^{2}\right)}} \boldsymbol{I}_{K_{1}}, \ldots, \frac{A_{u r}+\frac{1}{2} K_{r}}{B_{q\left(\sigma_{u r}^{2}\right)}} \boldsymbol{I}_{K_{r}}\right)\right\}^{-1} \\
& \boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})} \leftarrow\left(\frac{A_{\varepsilon}+\frac{n}{2}}{B_{q\left(\sigma_{\varepsilon}^{2}\right)}}\right) \boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})} \boldsymbol{C}^{T} \boldsymbol{y} \\
& B_{q\left(\sigma_{\varepsilon}^{2}\right)} \leftarrow B_{\varepsilon}+\frac{1}{2}\left\{\left\|\boldsymbol{y}-\boldsymbol{C} \boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right\|^{2}+\operatorname{tr}\left(\boldsymbol{C}^{T} \boldsymbol{C} \boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)\right\} \\
& B_{q\left(\sigma_{u \ell}^{2}\right)} \leftarrow B_{u \ell}+\frac{1}{2}\left\{\left\|\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{u}_{\ell}}\right\|^{2}+\operatorname{tr}\left(\left(\boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{u}_{\ell}}\right)\right\} \text { for } 1 \leq \ell \leq r
\end{aligned}
$$

until the increase in $\underline{p}(\boldsymbol{y} ; q)$ is negligible.

Algorithm 3: Iterative scheme for obtaining the parameters in the optimal densities $q_{\boldsymbol{\beta}, \boldsymbol{u}}^{*}$ and $q_{\boldsymbol{\sigma}^{2}}^{*}$ in the Bayesian linear mixed model example.

In this case $\log \underline{p}(\boldsymbol{y} ; q)$ takes the form

$$
\begin{aligned}
\log \underline{p}(\boldsymbol{y} ; q)= & \frac{1}{2}\left(p+\sum_{\ell=1}^{r} K_{\ell}\right)-\frac{n}{2} \log (2 \pi)-\frac{p}{2} \log \left(\sigma_{\beta}^{2}\right)+\frac{1}{2} \log \left|\boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right|-\frac{1}{2 \sigma_{\beta}^{2}}\left\{\left\|\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{\beta}}\right\|^{2}\right. \\
& +\operatorname{tr}\left(\left(\boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}\right)_{\boldsymbol{\beta}}\right)+A_{\varepsilon} \log \left(B_{\varepsilon}\right)-\left(A_{\varepsilon}+\frac{n}{2}\right) \log \left(B_{q\left(\sigma_{\varepsilon}^{2}\right)}\right)+\log \Gamma\left(A_{\varepsilon}+\frac{n}{2}\right)-\log \Gamma\left(A_{\varepsilon}\right) \\
& +\sum_{\ell=1}^{r}\left\{A_{u \ell} \log \left(B_{u \ell}\right)-\left(A_{u \ell}+\frac{K_{\ell}}{2}\right) \log \left(B_{q\left(\sigma_{u \ell}^{2}\right)}\right)+\log \Gamma\left(A_{u \ell}+\frac{K_{\ell}}{2}\right)-\log \Gamma\left(A_{u \ell}\right)\right\}
\end{aligned}
$$

Note that, within each iteration of Algorithm 3, this expression applies only after each of the parameter updates have been made.

Upon convergence to $\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}^{*}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}^{*}, B_{q\left(\sigma_{u 1}^{2}\right)}^{*}, \ldots, B_{q\left(\sigma_{u r}^{2}\right)}^{*}$ and $B_{q\left(\sigma_{\varepsilon}^{2}\right)}^{*}$ the approximate posteriors are:

$$
p(\boldsymbol{\beta}, \boldsymbol{u} \mid \boldsymbol{y}) \approx \text { the } N\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta}, \boldsymbol{u})}^{*}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta}, \boldsymbol{u})}^{*}\right) \text { density function }
$$

and

$$
\begin{aligned}
p\left(\sigma_{u 1}^{2}, \ldots, \sigma_{u r}^{2}, \sigma_{\varepsilon}^{2} \mid \boldsymbol{y}\right) \approx & \text { product of the } \operatorname{IG}\left(A_{u \ell}+\frac{1}{2} K_{\ell}, B_{q\left(\sigma_{u \ell}^{2}\right)}^{*}\right), 1 \leq \ell \leq r \text {, density functions } \\
& \text { together with the } \operatorname{IG}\left(A_{\varepsilon}+\frac{1}{2} n, B_{q\left(\sigma_{\varepsilon}^{2}\right)}^{*}\right) \text { density function. }
\end{aligned}
$$

We now provide an illustration for Bayesian analysis of data set involving longitudinal orthodontic measurements on 27 children (source: Pinheiro \& Bates, 2000). The data are available in the $R$ computing environment via the package nlme (Pinheiro et al. 2009), in the object Orthodont. We entertained the random intercept model

$$
\begin{aligned}
& \text { distance }_{i j}\left|U_{i} \stackrel{\text { ind. }}{\sim} N\left(\beta_{0}+U_{i}+\beta_{1} \text { age }_{i j}+\beta_{2} \text { male }_{i}, \sigma_{\varepsilon}^{2}\right)\right. \\
& U_{i} \mid \sigma_{u}^{2} \stackrel{\text { ind. }}{\sim} N\left(0, \sigma_{u}^{2}\right), \quad 1 \leq i \leq 27,1 \leq j \leq 4 \\
& \beta_{i} \stackrel{\text { ind. }}{\sim} N\left(0, \sigma_{\beta}^{2}\right), \quad \sigma_{u}^{2}, \sigma_{\varepsilon}^{2} \stackrel{\text { ind. }}{\sim} \operatorname{IG}(A, B)
\end{aligned}
$$

where distance ${ }_{i j}$ is the distance from the pituitary to the pterygomaxillary fissure (mm) for patient $i$ at time point $j$. Similarly, age ${ }_{i j}$ correspond to the longitudinal age values in years and male $_{i}$ is an indicator of the $i$ th child being male. This fits into framework (11)-(12) with $\boldsymbol{y}$ containing the distance ${ }_{i j}$ measurement, $\boldsymbol{X}=\left[1\right.$, age $\left._{i j}, \mathrm{male}_{i}\right]$ and $\boldsymbol{Z}=\boldsymbol{I}_{27} \otimes \mathbf{1}_{4}$ is an indicator matrix for the random intercepts. We used the vague priors $\sigma_{\beta}^{2}=10^{8}, A=B=\frac{1}{100}$ and used standardized versions of the distance and age data during the fitting. The results were then converted back to the original units. For comparison, we obtained 1 million samples from the posteriors using MCMC (with a burn-in of length 5000) and, from these, constructed kernel density estimate approximations to the posteriors. For such a high Monte Carlo sample size we would expect these MCMCbased approximations to be very accurate.

Figure 4 shows the progressive values of $\log p(\boldsymbol{y} ; q)$ and the approximate posterior densities obtained from applying Algorithm 3. Once again, convergence of $\log \{p(\boldsymbol{y} ; q)\}$ to a maximum is seen to be quite rapid. The variational approximate posterior densities are quite close to those obtained via MCMC, and indicate statistical significance of all model parameters.

# 2.2.4 Probit Regression and the Use of Auxiliary Variables 

As shown by Albert \& Chib (1993), Gibbs sampling for the Bayesian probit regression model becomes tractable when a particular set of auxiliary variables is introduced. The same trick applies to product density variational approximation (Girolami \& Rogers, 2006), as we now show.

The Bayesian probit regression model that we consider here is

$$
Y_{i} \mid \beta_{0}, \ldots, \beta_{k} \stackrel{\text { ind. }}{\sim} \operatorname{Bernoulli}\left(\Phi\left(\beta_{0}+\beta_{1} x_{1 i}+\ldots+\beta_{k} x_{k i}\right)\right), \quad 1 \leq i \leq n
$$

where the prior distribution on the coefficient vector $\boldsymbol{\beta}=\left(\beta_{0}, \ldots, \beta_{k}\right)$ takes the form $\boldsymbol{\beta} \sim N\left(\boldsymbol{\mu}_{\boldsymbol{\beta}}, \boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right)$. Letting $\boldsymbol{X} \equiv\left[1 x_{1 i} \cdots x_{k i}\right]_{1 \leq i \leq n}$, the likelihood can be written compactly as

$$
p(\boldsymbol{y} \mid \boldsymbol{\beta})=\Phi(\boldsymbol{X} \boldsymbol{\beta})^{\boldsymbol{y}}\left\{\mathbf{1}_{n}-\Phi(\boldsymbol{X} \boldsymbol{\beta})\right\}^{\mathbf{1}_{n}-\boldsymbol{y}}, \quad \boldsymbol{\beta} \sim N\left(\boldsymbol{\mu}_{\boldsymbol{\beta}}, \boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right)
$$

Introduce the vector of auxiliary variables $\boldsymbol{a}=\left(a_{1}, \ldots, a_{n}\right)$, where

$$
a_{i} \mid \boldsymbol{\beta} \stackrel{\text { ind. }}{\sim} N((\boldsymbol{X} \boldsymbol{\beta})_{i}, 1)
$$

This allows us to write

$$
p\left(y_{i} \mid a_{i}\right)=I\left(a_{i} \geq 0\right)^{y_{i}} I\left(a_{i}<0\right)^{1-y_{i}}, \quad 1 \leq i \leq n
$$

![img-4.jpeg](img-4.jpeg)

Figure 4: Approximate posterior densities from applying the product density variational approximation to (11)-(13) for the orthodontic data. 'Exact' posterior densities, based on kernel density estimates of 1 million MCMC samples, are shown for comparison.

In graphical model terms we are introducing a new node to the graph, as conveyed by Figure 5. Expansion of the parameter set from $\{\boldsymbol{\beta}\}$ to $\{\boldsymbol{a}, \boldsymbol{\beta}\}$ is the key to achieving a tractable solution.
![img-5.jpeg](img-5.jpeg)

Figure 5: Graphical representations of the probit regression model. The left-hand graph does not admit a tractable product density variational approximation. The right-hand graph overcomes this with the addition of an auxiliary variable node.

Consider the product restriction

$$
q(\boldsymbol{a}, \boldsymbol{\beta})=q_{\boldsymbol{a}}(\boldsymbol{a}) q_{\boldsymbol{\beta}}(\boldsymbol{\beta})
$$

Then application of (5) leads to
$q_{\boldsymbol{a}}^{*}(\boldsymbol{a})=\left[\prod_{i=1}^{n}\left\{\frac{I\left(a_{i} \geq 0\right)}{\Phi\left(\left(\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)_{i}\right)}\right\}^{y_{i}}\left\{\frac{I\left(a_{i}<0\right)}{1-\Phi\left(\left(\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)_{i}\right)}\right\}^{1-y_{i}}\right](2 \pi)^{-n / 2} \exp \left\{-\frac{1}{2}\left\|\boldsymbol{a}-\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right\|^{2}\right\}$
and $q_{\boldsymbol{\beta}}^{*}(\boldsymbol{\beta})$ is the $N\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta})},\left(\boldsymbol{X}^{T} \boldsymbol{X}+\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}\right)^{-1}\right)$ density function. These optimal densities are specified up to the parameter vector $\boldsymbol{\mu}_{q(\boldsymbol{\beta})} \equiv E_{\boldsymbol{\beta}}(\boldsymbol{\beta})$. We also need to work with the $q$-density mean of the auxiliary variable vector $\boldsymbol{\mu}_{q(\boldsymbol{a})} \equiv E_{\boldsymbol{a}}(\boldsymbol{a})$. The iterative scheme, Algorithm 4, emerges.

Initialize: $\boldsymbol{\mu}_{q(\boldsymbol{a})}(n \times 1)$.
Cycle:

$$
\begin{aligned}
& \boldsymbol{\mu}_{q(\boldsymbol{\beta})} \leftarrow\left(\boldsymbol{X}^{T} \boldsymbol{X}+\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}\right)^{-1}\left(\boldsymbol{X}^{T} \boldsymbol{\mu}_{q(\boldsymbol{a})}+\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1} \boldsymbol{\mu}_{\boldsymbol{\beta}}\right) \\
& \boldsymbol{\mu}_{q(\boldsymbol{a})} \leftarrow \boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}+\frac{\phi\left(\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)}{\Phi\left(\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)^{\boldsymbol{y}}\left\{\Phi\left(\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)-\mathbf{1}_{n}\right\}^{\mathbf{1}_{n}-\boldsymbol{y}}}
\end{aligned}
$$

until the increase in $\underline{p}(\boldsymbol{y} ; q)$ is negligible.

Algorithm 4: Iterative scheme for obtaining the parameters in the optimal densities $q_{\boldsymbol{\beta}}^{*}$ and $q_{\boldsymbol{a}}^{*}$ in the Bayesian probit regression example.

The $\log \underline{p}(\boldsymbol{y} ; q)$ expression in this case is

$$
\begin{aligned}
\log \underline{p}(\boldsymbol{y} ; q)=\boldsymbol{y}^{T} \log & \left\{\Phi\left(\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)\right\}+\left(\mathbf{1}_{n}-\boldsymbol{y}\right)^{T} \log \left\{\mathbf{1}_{n}-\Phi\left(\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)\right\} \\
& -\frac{1}{2}\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta})}-\boldsymbol{\mu}_{\boldsymbol{\beta}}\right)^{T} \boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta})}-\boldsymbol{\mu}_{\boldsymbol{\beta}}\right)-\frac{1}{2} \log \left|\boldsymbol{\Sigma}_{\boldsymbol{\beta}} \boldsymbol{X}^{T} \boldsymbol{X}+\boldsymbol{I}\right|
\end{aligned}
$$

Upon convergence, the approximate posterior distribution of the regression coefficients is

$$
\boldsymbol{\beta} \mid \boldsymbol{y} \stackrel{\text { approx }}{\sim} N\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta})}^{*},\left(\boldsymbol{X}^{T} \boldsymbol{X}+\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}\right)^{-1}\right)
$$

# 2.2.5 Finite Normal Mixture Model 

Our last example of product density variational approximation is of interest within both Statistics and Computer Science: inference for finite mixture models. Let $X_{1}, \ldots, X_{n}$ be a univariate sample that is modeled as a random sample from a mixture of $K$ Normal density functions with parameters $\left(\mu_{k}, \sigma_{k}^{2}\right), 1 \leq k \leq K$. Accordingly, the joint density function of the sample is

$$
p\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n}\left[\sum_{k=1}^{K} w_{k}\left(2 \pi \sigma_{k}^{2}\right)^{-1 / 2} \exp \left\{-\frac{1}{2}\left(x_{i}-\mu_{k}\right)^{2} / \sigma_{k}^{2}\right\}\right]
$$

where the weights $w_{k}, 1 \leq k \leq K$, are non-negative, and sum to unity. Let $\left(w_{1}, \ldots, w_{K}\right)$ have prior distribution:

$$
\left(w_{1}, \ldots, w_{K}\right) \sim \operatorname{Dirichlet}(\alpha, \ldots, \alpha), \quad \alpha>0
$$

We will take the prior distributions for the mean and variance parameters to be:

$$
\mu_{k} \stackrel{\text { ind. }}{\sim} N\left(\mu_{\mu_{k}}, \sigma_{\mu_{k}}^{2}\right), \quad \sigma_{k}^{2} \stackrel{\text { ind. }}{\sim} \operatorname{IG}\left(A_{k}, B_{k}\right), \quad 1 \leq k \leq K
$$

As with the probit regression model, a tractable product density transform requires the introduction of the auxiliary variable vectors:

$$
\left[a_{i 1}, \ldots, a_{i k}\right]\left|\left(w_{1}, \ldots, w_{K}\right) \stackrel{\text { ind }}{=}\right. \text { Multinomial }\left(1 ; w_{1}, \ldots, w_{K}\right), \quad 1 \leq i \leq n
$$

According to this notation, $\sum_{k=1}^{K} a_{i k}=1$ and $w_{k}=P\left(a_{i k}=1\right)$. If we set

$$
p\left(x_{i} \mid a_{i 1}, \ldots, a_{i K}\right)=\prod_{k=1}^{K}\left[\left(2 \pi \sigma_{k}^{2}\right)^{-1 / 2} \exp \left\{-\frac{1}{2}\left(x_{i}-\mu_{k}\right)^{2} / \sigma_{k}^{2}\right\}\right]^{a_{i k}}
$$

independently for each $1 \leq i \leq n$ then, using (18), the joint density function of the $X_{1}, \ldots, X_{n}$ is easily shown to be (17).

Let $\boldsymbol{w}, \boldsymbol{\mu}, \boldsymbol{\sigma}^{2}$ and $\boldsymbol{a}$ be the vectors containing the corresponding subscripted random variables. Then either of the product density restrictions

$$
q\left(\boldsymbol{w}, \boldsymbol{\mu}, \boldsymbol{\sigma}^{2}, \boldsymbol{a}\right)=q(\boldsymbol{w}, \boldsymbol{\mu}) q\left(\boldsymbol{\sigma}^{2}\right) q(\boldsymbol{a}) \quad \text { or } \quad q\left(\boldsymbol{w}, \boldsymbol{\mu}, \boldsymbol{\sigma}^{2}, \boldsymbol{a}\right)=q\left(\boldsymbol{w}, \boldsymbol{\sigma}^{2}\right) q(\boldsymbol{\mu}) q(\boldsymbol{a})
$$

is sufficient for a closed form solution. Note that subscripting on the $q$ densities is being suppressed to reduce clutter. Regardless of which restriction in (19) is chosen, application of Algorithm 1 leads to the optimal density for the model parameters having the product structure

$$
q^{*}\left(\boldsymbol{w}, \boldsymbol{\mu}, \boldsymbol{\sigma}^{2}\right)=q^{*}(\boldsymbol{w}) q^{*}(\boldsymbol{\mu}) q^{*}\left(\boldsymbol{\sigma}^{2}\right)
$$

where

$$
\begin{aligned}
q^{*}(\boldsymbol{w}) & =\text { density function of a Dirichlet distribution, } \\
q^{*}(\boldsymbol{\mu}) & =\text { product of } K \text { Normal density functions } \\
\text { and } q^{*}\left(\boldsymbol{\sigma}^{2}\right) & =\text { product of } K \text { Inverse Gamma density functions. }
\end{aligned}
$$

For $1 \leq k \leq K$, let $\mu_{q\left(\mu_{k}\right)}$ and $\sigma_{q\left(\mu_{k}\right)}^{2}$ denote the mean and variance for $q^{*}\left(\mu_{k}\right)$ and let $A_{q\left(\sigma_{k}^{2}\right)}$ and $B_{q\left(\sigma_{k}^{2}\right)}$ denote the shape and rate parameters for $q^{*}\left(\sigma_{k}^{2}\right)$. Also, let

$$
\boldsymbol{\alpha}_{q(\boldsymbol{w})} \equiv\left(\alpha_{q\left(w_{1}\right)}, \ldots, \alpha_{q\left(w_{1}\right)}\right)
$$

be the Dirichlet parameter vector for $q^{*}(\boldsymbol{w})$. The optimal parameters may be found obtained using Algorithm 5. Recall, from Section 1.1, that $\psi$ denotes the digamma function.

The $\log \underline{p}(\boldsymbol{x} ; q)$ expression in this case is

$$
\begin{aligned}
\log \underline{p}(\boldsymbol{x} ; q)= & \frac{1}{2} K\{1-n \log (2 \pi)\}+\log \Gamma(K \alpha)-K \log \Gamma(\alpha)-\log \Gamma(n+K \alpha) \\
& +\sum_{k=1}^{k}\left[A_{k} \log \left(B_{k}\right)-A_{q\left(\sigma_{k}^{2}\right)} \log \left(B_{q\left(\sigma_{k}^{2}\right)}\right)+\log \Gamma\left(A_{q\left(\sigma_{k}^{2}\right)}\right)-\log \Gamma\left(A_{k}\right)\right. \\
& +\log \Gamma\left(\alpha_{q\left(w_{k}\right)}\right)+\frac{1}{2} \log \left(\sigma_{q\left(\mu_{k}\right)}^{2} / \sigma_{\mu_{k}}^{2}\right)-\frac{1}{2}\left\{\left(\mu_{q\left(\mu_{k}\right)}-\mu_{\mu_{k}}\right)^{2}+\sigma_{q\left(\mu_{k}\right)}^{2}\right\} / \sigma_{\mu_{k}}^{2} \\
& \left.-\sum_{i=1}^{n} \omega_{i k} \log \left(\omega_{i k}\right)\right]
\end{aligned}
$$

Note that, for each iteration of Algorithm 5, this expression is valid only after each of the parameter updates have been made.

Algorithm 5 is similar to the EM algorithm for fitting a finite normal mixture model. Comparison and contrast are given in Section 10.2.1 of Bishop (2006).

Figure 6 shows the result of applying Algorithm 5 to data on the duration of geyser eruptions. The data are available in the $R$ computing environment via the package MASS (Venables and Ripley, 2009), in the object geyser duration. The number of mixtures

Initialize: $\mu_{q\left(\mu_{k}\right)} \in \mathbb{R}$ and $\boldsymbol{\alpha}_{q(\boldsymbol{w})}, \sigma_{q\left(\mu_{k}\right)}^{2}, A_{q\left(\sigma_{k}^{2}\right)}, B_{q\left(\sigma_{k}^{2}\right)}, \omega_{\bullet k}>0,1 \leq k \leq K$,

$$
\text { such that } \sum_{k=1}^{K} \omega_{\bullet k}=1
$$

Cycle:
For $i=1, \ldots, n$ and $k=1, \ldots, K$ :

$$
\begin{aligned}
& \nu_{i k} \leftarrow \psi\left(\alpha_{q\left(w_{k}\right)}\right)-\psi\left(\mathbf{1}_{K}^{T} \boldsymbol{\alpha}_{q(\boldsymbol{w})}\right)+\frac{1}{2} \psi\left(A_{q\left(\sigma_{k}^{2}\right)}\right)-\frac{1}{2} \log \left(2 \pi B_{q\left(\sigma_{k}^{2}\right)}\right) \\
& -\frac{1}{2} A_{q\left(\sigma_{k}^{2}\right)}\left\{\left(X_{i}-\mu_{q\left(\mu_{k}\right)}\right)^{2}+\sigma_{q\left(\mu_{k}\right)}^{2}\right\} / B_{q\left(\sigma_{k}^{2}\right)} \\
& \text { For } i=1, \ldots, n \text { and } k=1, \ldots, K: \quad \omega_{i k} \leftarrow \exp \left(\nu_{i k}\right) / \sum_{k=1}^{K} \exp \left(\nu_{i k}\right) \\
& \text { For } k=1, \ldots, K: \\
& \omega_{\bullet k} \leftarrow \sum_{i=1}^{n} \omega_{i k} ; \quad \sigma_{q\left(\mu_{k}\right)}^{2} \leftarrow 1 /\left\{1 / \sigma_{\mu_{k}}^{2}+A_{q\left(\sigma_{k}^{2}\right)} \omega_{\bullet k} / B_{q\left(\sigma_{k}^{2}\right)}\right\} \\
& \mu_{q\left(\mu_{k}\right)} \leftarrow \sigma_{q\left(\mu_{k}\right)}^{2}\left\{\mu_{\mu_{k}} / \sigma_{\mu_{k}}^{2}+A_{q\left(\sigma_{k}^{2}\right)} \sum_{i=1}^{n} \omega_{i k} X_{i} / B_{q\left(\sigma_{k}^{2}\right)}\right\} \\
& \alpha_{q\left(w_{k}\right)} \leftarrow \alpha+\omega_{\bullet k} ; \quad A_{q\left(\sigma_{k}^{2}\right)} \leftarrow A_{k}+\frac{1}{2} \omega_{\bullet k} \\
& B_{q\left(\sigma_{k}^{2}\right)} \leftarrow B_{k}+\frac{1}{2} \sum_{i=1}^{n} \omega_{i k}\left\{\left(X_{i}-\mu_{q\left(\mu_{k}\right)}\right)^{2}+\sigma_{q\left(\mu_{k}\right)}^{2}\right\}
\end{aligned}
$$

until the increase in $\underline{p}(\boldsymbol{x} ; q)$ is negligible.

Algorithm 5: Iterative scheme for obtaining the parameters in the optimal densities $q_{\boldsymbol{w}}^{*}, q_{\boldsymbol{\mu}}^{*}$ and $q_{\boldsymbol{\sigma}^{2}}^{*}$ in the finite normal mixtures example.
was set at $K=2$ and, as in the earlier examples, vague priors $\mu_{k} \sim N\left(0,10^{8}\right)$ and $\sigma_{k}^{2} \sim$ $\operatorname{IG}\left(\frac{1}{100}, \frac{1}{100}\right)$ were used. The upper panel of Figure 6 shows that convergence of $\log \underline{p}(\boldsymbol{x} ; q)$ was obtained after about 20 iterations from naïve starting values. In the lower panel, the curve corresponds to the approximate posterior mean of the common density function. The shade region corresponds to approximate pointwise $95 \%$ credible sets. These were obtained using 10000 draws from $q^{*}\left(\boldsymbol{w}, \boldsymbol{\mu}, \boldsymbol{\sigma}^{2}\right)$.

Finally, we note that variational approximation methodology could also be used to choose the number of mixtures $K$. See, for example, Bishop (2006, Section 10.2.4) and McGrory \& Titterington (2007).

# 2.3 Parametric Density Transforms 

Rather than assuming that $q(\boldsymbol{\theta})$ has product density structure, we may instead, assume that it belongs to a particular parametric family and hope that this results in a more tractable approximation to the posterior density $p(\boldsymbol{\theta} \mid \boldsymbol{y})$. This approach has received less attention in the Computer Science literature (e.g. Barber \& Bishop, 1998; Seeger 2000,2004; Honkela \& Valpola 2005; Archambeau, Cornford, Opper \& Shawe-Taylor 2007) but, nonetheless, is worthy of discussion. Next, we illustrate parametric density transforms with a simple example.

### 2.3.1 Poisson Regression with Gaussian Transform

Consider the Bayesian Poisson regression model

$$
Y_{i} \mid \beta_{0}, \ldots, \beta_{k} \stackrel{\text { ind }}{\sim} \operatorname{Poisson}\left(\exp \left(\beta_{0}+\beta_{1} x_{1 i}+\ldots+\beta_{k} x_{k i}\right)\right), \quad 1 \leq i \leq n
$$

![img-6.jpeg](img-6.jpeg)

Figure 6: Results from application of Algorithm 5 to data on the duration of geyser eruptions. The upper panel shows successive values of $\log p(\boldsymbol{x} ; q)$. The lower panel shows approximate mean and pointwise $95 \%$ credible sets for the common density function. The data are shown at the base of the plot.
where the prior distribution on the coefficient vector $\boldsymbol{\beta} \equiv\left(\beta_{0}, \ldots, \beta_{k}\right)$ takes the form $\boldsymbol{\beta} \sim N\left(\boldsymbol{\mu}_{\boldsymbol{\beta}}, \boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right)$. As before, we let $\boldsymbol{X}=\left[\begin{array}{lll}1 & x_{1 i} & \cdots & x_{k i}\end{array}\right]_{1 \leq i \leq n}$. Then the likelihood is

$$
p(\boldsymbol{y} \mid \boldsymbol{\beta})=\exp \left\{\boldsymbol{y}^{T} \boldsymbol{X} \boldsymbol{\beta}-\mathbf{1}_{n}^{T} \exp (\boldsymbol{X} \boldsymbol{\beta})-\mathbf{1}_{n}^{T} \log (\boldsymbol{y}!) \boldsymbol{\}}\right.
$$

and the marginal likelihood is

$$
\begin{aligned}
p(\boldsymbol{y})= & (2 \pi)^{-(k+1) / 2}\left|\boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right|^{-1 / 2} \\
& \times \int_{\mathbb{R}^{k+1}} \exp \left\{\boldsymbol{y}^{T} \boldsymbol{X} \boldsymbol{\beta}-\mathbf{1}_{n}^{T} \exp (\boldsymbol{X} \boldsymbol{\beta})-\mathbf{1}_{n}^{T} \log (\boldsymbol{y}!)-\frac{1}{2}\left(\boldsymbol{\beta}-\boldsymbol{\mu}_{\boldsymbol{\beta}}\right)^{T} \boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}\left(\boldsymbol{\beta}-\boldsymbol{\mu}_{\boldsymbol{\beta}}\right)\right\} d \boldsymbol{\beta}
\end{aligned}
$$

Note that $p(\boldsymbol{y})$, and hence $p(\boldsymbol{\beta} \mid \boldsymbol{y})$, involves an intractable integral over $\mathbb{R}^{k+1}$.
Take $q$ to be the $N\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta})}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right)$ density:

$$
q\left(\boldsymbol{\beta} ; \boldsymbol{\mu}_{q(\boldsymbol{\beta})}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right)=(2 \pi)^{-p / 2}\left|\boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right|^{-1 / 2} \exp \left\{-\frac{1}{2}\left(\boldsymbol{\beta}-\boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)^{T} \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}^{-1}\left(\boldsymbol{\beta}-\boldsymbol{\mu}_{q(\boldsymbol{\beta})}\right)\right\}
$$

Then the lower bound (4) admits the explicit expression

$$
\begin{aligned}
\log \underline{p}\left(\boldsymbol{y} ; \boldsymbol{\mu}_{q(\boldsymbol{\beta})}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right)= & \boldsymbol{y}^{T} \boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}-\mathbf{1}_{n}^{T} \exp \left\{\boldsymbol{X} \boldsymbol{\mu}_{q(\boldsymbol{\beta})}+\frac{1}{2} \operatorname{diagonal}\left(\boldsymbol{X} \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})} \boldsymbol{X}^{T}\right)\right\} \\
& -\frac{1}{2}\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta})}-\boldsymbol{\mu}_{\boldsymbol{\beta}}\right)^{T} \boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta})}-\boldsymbol{\mu}_{\boldsymbol{\beta}}\right)-\frac{1}{2} \operatorname{tr}\left(\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1} \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right) \\
& +\frac{1}{2} \log \left|\boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right|-\frac{1}{2} \log \left|\boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right|+\frac{k+1}{2}-\mathbf{1}_{n}^{T} \log (\boldsymbol{y}!)
\end{aligned}
$$

Note that, from (2),

$$
\log p(\boldsymbol{y}) \geq \log \underline{p}\left(\boldsymbol{y} ; \boldsymbol{\mu}_{q(\boldsymbol{\beta})}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right)
$$

for all choices of the mean vector $\boldsymbol{\mu}_{q(\boldsymbol{\beta})}$ and covariance matrix $\boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}$. Choosing these variational parameters to maximize $\log \underline{p}\left(\boldsymbol{y} ; \boldsymbol{\mu}_{q(\boldsymbol{\beta})}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right)$ makes the approximation as good as possible. The optimal Gaussian density transform $q^{*}(\boldsymbol{\beta})$ is the $N\left(\boldsymbol{\mu}_{q(\boldsymbol{\beta})}^{*}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}^{*}\right)$ density function, where $\boldsymbol{\mu}_{q(\boldsymbol{\beta})}^{*}$ and $\boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}^{*}$ are the maximizers of $\log \underline{p}\left(\boldsymbol{y} ; \boldsymbol{\mu}_{q(\boldsymbol{\beta})}, \boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}\right)$. NewtonRaphson iteration can be used to determine $\boldsymbol{\mu}_{q(\boldsymbol{\beta})}^{*}$ and $\boldsymbol{\Sigma}_{q(\boldsymbol{\beta})}^{*}$. Further details may be found in Ormerod (2008).

# 3 Tangent Transform Approach 

Not all variational approximations fit within the Kullback-Leibler divergence framework. Another variety are what might be called tangent transform variational approximations since they work with 'tangent-type' representations of concave and convex functions. An example of such a representation is

$$
\log (x)=\min _{\xi>0}\{\xi x-\log (\xi)-1\}, \quad \text { for all } x>0
$$

Figure 7 provides a graphical description of (21).
![img-7.jpeg](img-7.jpeg)

Figure 7: Variational representation of the logarithmic function. Left axes: members of family of functions $f(x, \xi) \equiv \xi x-\log (\xi)-1$ versus $\xi>0$, for $x \in\{0.25,0.5,1,2,4\}$, shown as gray curves. Right axes: For each $x$, the minimum of $f(x, \xi)$ over $\xi$ corresponds to $\log (x)$. In the $x$ direction the $f(x, \xi)$ are linear and are shown in gray.

The representation (21) implies that

$$
\log (x) \leq \xi x-\log (\xi)-1, \quad \text { for all } \xi>0
$$

The fact that $\xi x-\log (\xi)-1$ is linear in $x$ for every value of the variational parameter $\xi>0$ allows for simplifications of expressions involving the logarithmic function. The value of $\xi$ can then be chosen to make the approximation as accurate as possible.

Tangent transform variational approximations are underpinned by the theory of convex duality (e.g. Rockafellar, 1972). We will not delve into that here, and instead stay on course with statistical examples. The interested reader should consult Jordan et al. (1999).

# 3.1 Bayesian Logistic Regression 

As described by Jaakkola \& Jordan (2000), Bayesian logistic regression lends itself to tangent transform variational approximation. Hence, we consider the Bayesian logistic regression model

$$
Y_{i} \mid \beta_{0}, \ldots, \beta_{k} \stackrel{\text { iud }}{=} \text { Bernoulli }\left(\left[1+\exp \left\{-\left(\beta_{0}+\beta_{1} x_{1 i}+\ldots+\beta_{k} x_{k i}\right)\right\}\right]^{-1}\right), \quad 1 \leq i \leq n
$$

where the prior distribution on the coefficient vector $\boldsymbol{\beta}=\left(\beta_{0}, \ldots, \beta_{k}\right)$ takes the form $\boldsymbol{\beta} \sim N\left(\boldsymbol{\mu}_{\boldsymbol{\beta}}, \boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right)$. The likelihood is

$$
p(\boldsymbol{y} \mid \boldsymbol{\beta})=\exp \left[\boldsymbol{y}^{T} \boldsymbol{X} \boldsymbol{\beta}-\mathbf{1}_{n}^{T} \log \left\{\mathbf{1}_{n}+\exp (\boldsymbol{X} \boldsymbol{\beta})\right\}\right]
$$

where $\boldsymbol{X}=\left[\begin{array}{lll}1 & x_{1 i} & \cdots & x_{k i}\end{array}\right]_{1 \leq i \leq n}$. The posterior density of $\boldsymbol{\beta}$ is

$$
p(\boldsymbol{\beta} \mid \boldsymbol{y})=p(\boldsymbol{y}, \boldsymbol{\beta}) / \int_{\mathbb{R}^{k+1}} p(\boldsymbol{y}, \boldsymbol{\beta}) d \boldsymbol{\beta}
$$

where

$$
\begin{gathered}
p(\boldsymbol{y}, \boldsymbol{\beta})=\exp \left[\boldsymbol{y}^{T} \boldsymbol{X} \boldsymbol{\beta}-\mathbf{1}_{n}^{T} \log \left\{\mathbf{1}_{n}+\exp (\boldsymbol{X} \boldsymbol{\beta})\right\}-\frac{1}{2}\left(\boldsymbol{\beta}-\boldsymbol{\mu}_{\boldsymbol{\beta}}\right)^{T} \boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}\left(\boldsymbol{\beta}-\boldsymbol{\mu}_{\boldsymbol{\beta}}\right)\right. \\
\left.-\frac{k+1}{2} \log (2 \pi)-\frac{1}{2} \log \left|\boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right|\right]
\end{gathered}
$$

Once again, we are stuck with a multivariate intractable integral in the normalizing factor. We get around this by noting the following representation of $-\log \left(1+e^{x}\right)$ as the maxima of a family of parabolae:

$$
-\log \left(1+e^{x}\right)=\max _{\xi \in \mathbb{R}}\left\{A(\xi) x^{2}-\frac{1}{2} x+C(\xi)\right\} \quad \text { for all } x \in \mathbb{R}
$$

where

$$
A(\xi) \equiv-\tanh (\xi / 2) /(4 \xi) \quad \text { and } \quad C(\xi) \equiv \xi / 2-\log \left(1+e^{\xi}\right)+\xi \tanh (\xi / 2) / 4
$$

Whilst the genesis of (23) may be found in Jaakkola \& Jordan (2000), it is easily checked via elementary calculus methods. It follows from (23) that

$$
\begin{aligned}
-\mathbf{1}_{n}^{T} \log \left\{\mathbf{1}_{n}+\exp (\boldsymbol{X} \boldsymbol{\beta})\right\} & \geq \mathbf{1}_{n}^{T}\left\{A(\boldsymbol{\xi}) \odot(\boldsymbol{X} \boldsymbol{\beta})^{2}-\frac{1}{2} \boldsymbol{X} \boldsymbol{\beta}+C(\boldsymbol{\xi})\right\} \\
& =\boldsymbol{\beta}^{T} \boldsymbol{X}^{T} \operatorname{diag}\{A(\boldsymbol{\xi})\} \boldsymbol{X} \boldsymbol{\beta}-\frac{1}{2} \mathbf{1}_{n}^{T} \boldsymbol{X} \boldsymbol{\beta}+\mathbf{1}_{n}^{T} C(\boldsymbol{\xi})
\end{aligned}
$$

where $\boldsymbol{\xi}=\left(\xi_{1}, \ldots, \xi_{n}\right)$ is an $n \times 1$ vector of variational parameters. This gives us following lower bound on $p(\boldsymbol{y}, \boldsymbol{\beta})$ :

$$
\begin{aligned}
\underline{p}(\boldsymbol{y}, \boldsymbol{\beta} ; \boldsymbol{\xi})=\exp [ & \left.-\frac{1}{2} \boldsymbol{\beta}^{T}\left\{\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}-2 \boldsymbol{X}^{T} \operatorname{diag}\{A(\boldsymbol{\xi})\} \boldsymbol{X}\right\} \boldsymbol{\beta}+\left\{\left(\boldsymbol{y}-\frac{1}{2} \mathbf{1}_{n}\right)^{T} \boldsymbol{X}+\boldsymbol{\mu}_{\boldsymbol{\beta}}^{T} \boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}\right\} \boldsymbol{\beta}\right. \\
& \left.-\frac{1}{2} \boldsymbol{\mu}_{\boldsymbol{\beta}}^{T} \boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1} \boldsymbol{\mu}_{\boldsymbol{\beta}}+\mathbf{1}_{n}^{T} C(\boldsymbol{\xi})-\frac{k+1}{2} \log (2 \pi)-\frac{1}{2} \log \left|\boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right|\right]
\end{aligned}
$$

which is proportional to a Multivariate Normal density in $\boldsymbol{\beta}$. Upon normalization we obtain the following family of variational approximations to $\boldsymbol{\beta} \mid \boldsymbol{y}$ :

$$
\boldsymbol{\beta} \mid \boldsymbol{y} ; \boldsymbol{\xi} \sim N(\boldsymbol{\mu}(\boldsymbol{\xi}), \boldsymbol{\Sigma}(\boldsymbol{\xi}))
$$

where

$$
\boldsymbol{\Sigma}(\boldsymbol{\xi}) \equiv\left[\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}-2 \boldsymbol{X}^{\top} \operatorname{diag}\{A(\boldsymbol{\xi})\} \boldsymbol{X}\right]^{-1} \quad \text { and } \quad \boldsymbol{\mu}(\boldsymbol{\xi}) \equiv \boldsymbol{\Sigma}(\boldsymbol{\xi})\left\{\boldsymbol{X}^{\top}\left(\boldsymbol{y}-\frac{1}{2} \mathbf{1}\right)+\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1} \boldsymbol{\mu}_{\boldsymbol{\beta}}\right\}
$$

We are left with the problem of determining the vector of variational parameters $\boldsymbol{\xi} \in$ $\mathbb{R}^{n}$. A natural way of choosing these is to make

$$
\underline{p}(\boldsymbol{y} ; \boldsymbol{\xi}) \equiv \int \underline{p}(\boldsymbol{y}, \boldsymbol{\beta} ; \boldsymbol{\xi}) d \boldsymbol{\beta}
$$

as close as possible to $p(\boldsymbol{y})$. Since $\underline{p}(\boldsymbol{y} ; \boldsymbol{\xi}) \leq p(\boldsymbol{y})$ for all $\boldsymbol{\xi}$, this reduces to the problem of maximizing $\underline{p}(\boldsymbol{y} ; \boldsymbol{\xi})$ over $\boldsymbol{\xi}$. Note that this lower bound on $\log p(\boldsymbol{y})$ has explicit expression:

$$
\begin{aligned}
\log \underline{p}(\boldsymbol{y} ; \boldsymbol{\xi})=\frac{1}{2} \log & |\boldsymbol{\Sigma}(\boldsymbol{\xi})|-\frac{1}{2} \log \left|\boldsymbol{\Sigma}_{\boldsymbol{\beta}}\right|+\frac{1}{2} \boldsymbol{\mu}(\boldsymbol{\xi})^{T} \boldsymbol{\Sigma}(\boldsymbol{\xi})^{-1} \boldsymbol{\mu}(\boldsymbol{\xi})-\frac{1}{2} \boldsymbol{\mu}_{\boldsymbol{\beta}}^{T} \boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1} \boldsymbol{\mu}_{\boldsymbol{\beta}} \\
& +\sum_{i=1}^{n}\left\{\xi_{i} / 2-\log \left(1+e^{\xi_{i}}\right)+\left(\xi_{i} / 4\right) \tanh \left(\xi_{i} / 2\right)\right\}
\end{aligned}
$$

Even though this can be maximized numerically in a similar fashion to (20), Jaakkola \& Jordan (2000) derive a simpler algorithm based on the notion of Expectation Maximization (EM) (e.g. McLachlan \& Krishnan, 1997) with $\boldsymbol{\beta}$ playing the role of a set of latent variables. Treating $\boldsymbol{y}, \boldsymbol{\beta}$ as the set of 'complete data' the E-step of the their EM algorithm involves

$$
Q\left(\boldsymbol{\xi}^{\text {new }} \mid \boldsymbol{\xi}\right) \equiv E_{\boldsymbol{\beta} \mid \boldsymbol{y} ; \boldsymbol{\xi}}\left\{\log \underline{p}\left(\boldsymbol{y}, \boldsymbol{\beta} ; \boldsymbol{\xi}^{\text {new }}\right)\right\}
$$

where $\underline{p}(\boldsymbol{y}, \boldsymbol{\beta} ; \boldsymbol{\xi})$ is interpreted as the variational lower bound on the 'complete data likelihood'. This results in the explicit expression

$$
\begin{aligned}
Q\left(\boldsymbol{\xi}^{\text {new }} \mid \boldsymbol{\xi}\right)= & \operatorname{tr}\left[\boldsymbol{X}^{T} \operatorname{diag}\left\{A\left(\boldsymbol{\xi}^{\text {new }}\right)\right\} \boldsymbol{X}\left\{\boldsymbol{\Sigma}(\boldsymbol{\xi})+\boldsymbol{\mu}(\boldsymbol{\xi}) \boldsymbol{\mu}(\boldsymbol{\xi})^{T}\right\}\right]+\mathbf{1}_{n}^{T} C\left(\boldsymbol{\xi}^{\text {new }}\right) \\
& + \text { terms not involving } \boldsymbol{\xi}^{\text {new }} .
\end{aligned}
$$

Differentiating with respect to $\boldsymbol{\xi}^{\text {new }}$ and using the fact that $A(\boldsymbol{\xi})$ is a monotonically increasing over $\xi>0$, the M-step can be shown to have the exact solution

$$
\left(\boldsymbol{\xi}^{\text {new }}\right)^{2}=\text { diagonal }\left[\boldsymbol{X}\left\{\boldsymbol{\Sigma}(\boldsymbol{\xi})+\boldsymbol{\mu}(\boldsymbol{\xi}) \boldsymbol{\mu}(\boldsymbol{\xi})^{\top}\right\} \boldsymbol{X}^{\top}\right]
$$

Taking positive square-roots on both sides of (26) leads to Algorithm 6.

```
Initialize: \(\boldsymbol{\xi}(n \times 1 ;\) all entries positive).
Cycle:
    \(\boldsymbol{\Sigma}(\boldsymbol{\xi}) \leftarrow\left[\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1}-2 \boldsymbol{X}^{\top} \operatorname{diag}\{A(\boldsymbol{\xi})\} \boldsymbol{X}\right]^{-1}\)
    \(\boldsymbol{\mu}(\boldsymbol{\xi}) \leftarrow \boldsymbol{\Sigma}(\boldsymbol{\xi})\left\{\boldsymbol{X}^{\top}\left(\boldsymbol{y}-\frac{1}{2} \mathbf{1}_{n}\right)+\boldsymbol{\Sigma}_{\boldsymbol{\beta}}^{-1} \boldsymbol{\mu}_{\boldsymbol{\beta}}\right\}\)
    \(\xi \leftarrow \sqrt{\operatorname{diagonal}\left[\boldsymbol{X}\left\{\boldsymbol{\Sigma}(\boldsymbol{\xi})+\boldsymbol{\mu}(\boldsymbol{\xi}) \boldsymbol{\mu}(\boldsymbol{\xi})^{\top}\right\} \boldsymbol{X}^{\top}\right]}\)
until the increase in \(\underline{p}(\boldsymbol{y} ; \boldsymbol{\xi})\) is negligible.
```

Algorithm 6: Iterative scheme for obtaining the optimal model and variational parameters in the Bayesian logistic regression example.

Convergence of Algorithm 6 is monotone and usually quite rapid (Jaakkola \& Jordan, 2000).

# 4 Frequentist Inference 

Up until now, we have only dealt with approximate inference in Bayesian models via variational methods. In this section we point out that variational approximations can be used in frequentist contexts. However, frequentist inferential problems that stand to benefit from variational approximations are much rarer. Possible candidates are frequentist models for which specification of the likelihood involves conditioning on a vector of

latent variables $\boldsymbol{u}$. In this case, the log-likelihood of the model parameter vector $\boldsymbol{\theta}$ takes the form

$$
\ell(\boldsymbol{\theta}) \equiv \log p(\boldsymbol{y} ; \boldsymbol{\theta})=\int p(\boldsymbol{y} \mid \boldsymbol{u} ; \boldsymbol{\theta}) p(\boldsymbol{u} ; \boldsymbol{\theta}) d \boldsymbol{u}
$$

The maximum likelihood estimate of $\boldsymbol{\theta}$ is exactly

$$
\widehat{\theta}=\underset{\boldsymbol{\theta}}{\operatorname{argmax}} \ell(\boldsymbol{\theta})
$$

but, because of the integral in (27), $\ell(\boldsymbol{\theta})$ may not be available in closed form. Depending on the forms of $p(\boldsymbol{y} \mid \boldsymbol{u} ; \boldsymbol{\theta})$ and $p(\boldsymbol{u} ; \boldsymbol{\theta})$, either the density transform or tangent transform approaches can result in more tractable approximations to $\ell(\boldsymbol{\theta})$. For the remainder of this section we restrict discussion to the density transform approach. The tangent transform approach has a similar treatment.

Let $q(\boldsymbol{u})$ be an arbitrary density function in $\boldsymbol{u}$. Repeating the steps given at (2), but with the log marginal likelihood $\log p(\boldsymbol{y})$ replaced by the log-likelihood $\ell(\boldsymbol{\theta})$, we obtain

$$
\ell(\boldsymbol{\theta})=\int q(\boldsymbol{u}) \log \left\{\frac{p(\boldsymbol{y}, \boldsymbol{u} ; \boldsymbol{\theta})}{q(\boldsymbol{u})}\right\} d \boldsymbol{u}+\int q(\boldsymbol{u}) \log \left\{\frac{q(\boldsymbol{u})}{p(\boldsymbol{u} \mid \boldsymbol{y} ; \boldsymbol{\theta})}\right\} d \boldsymbol{u} \geq \underline{\ell}(q ; \boldsymbol{\theta})
$$

where

$$
\underline{\ell}(q ; \boldsymbol{\theta}) \equiv \int q(\boldsymbol{u}) \log \left\{\frac{p(\boldsymbol{y}, \boldsymbol{u} ; \boldsymbol{\theta})}{q(\boldsymbol{u})}\right\} d \boldsymbol{u}
$$

We now have the option of choosing $q$ to make $\underline{\ell}(q ; \boldsymbol{\theta})$ more tractable while also aiming to minimize the Kullback-Leibler distance between $q$ and $p(\boldsymbol{u} \mid \boldsymbol{y} ; \boldsymbol{\theta})$. In theory, the product density methodology of Section 2.2 could be used to guide the choice of $q$. However, we are yet to find a non-trivial frequentist example where an explicit solution arises. Suppose, instead, that we restrict $q$ to a parametric family of densities $\{q(\boldsymbol{u} ; \boldsymbol{\xi}): \boldsymbol{\xi} \in \Xi\}$. Then the log-likelihood lower bound (28) becomes

$$
\underline{\ell}(q ; \boldsymbol{\theta}, \boldsymbol{\xi})=\int q(\boldsymbol{u} ; \boldsymbol{\xi}) \log \left\{\frac{p(\boldsymbol{y}, \boldsymbol{u} ; \boldsymbol{\theta})}{q(\boldsymbol{u} ; \boldsymbol{\xi})}\right\} d \boldsymbol{u}
$$

We should maximize over the variational parameters $\boldsymbol{\xi}$ to minimize the Kullback-Leibler divergence between $q(\boldsymbol{u} ; \boldsymbol{\xi})$ and $p(\boldsymbol{u} \mid \boldsymbol{y} ; \boldsymbol{\theta})$, and over the model parameters $\boldsymbol{\theta}$ to maximize the approximate log-likelihood. This leads to the new maximization problem:

Then $\underline{\widehat{\boldsymbol{\theta}}}$ is a variational approximation to the maximum likelihood estimator $\widehat{\boldsymbol{\theta}}$. Standard error estimates can be obtained by plugging in $\underline{\widehat{\boldsymbol{\theta}}}$ for $\boldsymbol{\theta}$ and $\boldsymbol{\xi}$ for $\boldsymbol{\xi}$ in the variational approximate Fisher information matrix, the matrix that arises from replacement of $\ell(\boldsymbol{\theta})$ by $\underline{\ell}(q ; \boldsymbol{\theta}, \boldsymbol{\xi})$ in the definition of Fisher information. However, to our knowledge, asymptotic normality theory that justifies such standard error estimation has not yet been done.

# 4.1 Poisson Mixed Model 

Consider the (non-Bayesian) Poisson mixed model

$$
Y_{i j} \mid U_{i} \stackrel{\text { ind. }}{\sim} \operatorname{Poisson}\left\{\exp \left(\beta_{0}+\beta_{1} x_{i j}+U_{i}\right)\right\}, \quad U_{i} \stackrel{\text { ind. }}{\sim} N\left(0, \sigma^{2}\right), \quad 1 \leq j \leq n_{i}, 1 \leq i \leq m
$$

where $y_{i j}$ is the $j$ th response measurement for unit $i$, and the deterministic predictors $x_{i j}$ are defined similarly. The log-likelihood of $\left(\beta_{0}, \beta_{1}, \sigma^{2}\right)$ involves intractable integrals, but

the lower bound (29) takes the form

$$
\begin{aligned}
\underline{\ell}\left(q ; \beta_{0}, \beta_{1}, \sigma^{2}\right)=\int_{\mathbb{R}^{m}} & \left(\sum_{i=1}^{m}\left[\sum_{j=1}^{n_{i}}\left\{y_{i j}\left(\beta_{0}+\beta_{1} x_{i j}+u_{i}\right)-e^{\beta_{0}+\beta_{1} x_{i j}+u_{i}}-\log \left(y_{i j}!\right)\right\}-\frac{u_{i}^{2}}{2 \sigma^{2}}\right]\right. \\
& \left.-\frac{m}{2} \log \left(2 \pi \sigma^{2}\right)-\log q\left(u_{1}, \ldots, u_{m}\right)\right) q\left(u_{1}, \ldots, u_{m}\right) d u_{1} \cdots d u_{m}
\end{aligned}
$$

Setting $q$ to be the product of $m$ univariate Normal densities with mean $\mu_{i}$ and variance $\lambda_{i}>0,1 \leq i \leq m$, leads to the closed form lower bound:

$$
\begin{aligned}
\underline{\ell}\left(q ; \beta_{0}, \beta_{1}, \sigma^{2}, \boldsymbol{\mu}, \boldsymbol{\lambda}\right)=\sum_{i=1}^{m} & \sum_{j=1}^{n_{i}}\left\{y_{i j}\left(\beta_{0}+\beta_{1} x_{i j}+\mu_{i}\right)+e^{\beta_{0}+\beta_{1} x_{i j}+\mu_{i}+\frac{1}{2} \lambda_{i}}-\log \left(y_{i j}!\right)\right\} \\
& +\frac{m}{2}\left\{1-\log \left(\sigma^{2}\right)\right\}+\frac{1}{2} \sum_{i=1}^{m}\left\{\log \left(\lambda_{i}\right)-\frac{\mu_{i}^{2}+\lambda_{i}}{\sigma^{2}}\right\}
\end{aligned}
$$

for all values of the variational parameters $\boldsymbol{\mu}=\left(\mu_{1}, \ldots, \mu_{m}\right)$ and $\boldsymbol{\lambda}=\left(\lambda_{1}, \ldots, \lambda_{m}\right)$. Maximizing over these parameters narrows the gap between $\underline{\ell}\left(\beta_{0}, \beta_{1}, \sigma^{2}, \boldsymbol{\mu}, \boldsymbol{\lambda}\right)$ and $\ell\left(\beta_{0}, \beta_{1}, \sigma^{2}\right)$ and so sensible estimators of the model parameters are:

$$
\left(\widehat{\underline{\beta_{0}}}, \widehat{\underline{\beta_{1}}}, \underline{\widehat{\sigma}}^{2}\right)=\left(\beta_{0}, \beta_{1}, \sigma^{2}\right) \text { component of } \underset{\beta_{0}, \beta_{1}, \sigma^{2}, \boldsymbol{\mu}, \boldsymbol{\lambda}}{\operatorname{argmax}} \underline{\ell}\left(q ; \beta_{0}, \beta_{1}, \sigma^{2}, \boldsymbol{\mu}, \boldsymbol{\lambda}\right) .
$$

Recently, Hall, Ormerod \& Wand (2009) established consistency and rates of convergence results for $\widehat{\beta_{0}}, \widehat{\beta_{1}}$ and $\underline{\widehat{\sigma}}^{2}$.

# 5 Closing Discussion 

Our goal in this article is to explain variational approximations in a digestible form for a statistical audience. As mentioned in the introduction, the important issue of accuracy of variational approximations is not dealt with here. The expositions by Jordan (2004) and Titterington (2004) provide access to some of the literature on variational approximation accuracy.

Variational approximations have the potential to become an important player in statistical inference. New variational approximation methods are continually being developed. The recent emergence of formal software for variational inference is certain to accelerate its widespread use. Their usefulness increases as the size of the problem increases and Monte Carlo methods such as MCMC start to become untenable.
