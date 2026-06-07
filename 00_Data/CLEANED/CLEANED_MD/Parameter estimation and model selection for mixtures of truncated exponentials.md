# Aalborg Universitet 

## AALBORG UNIVERSITY

## Parameter Estimation and Model Selection for Mixtures of Truncated Exponentials

Langseth, Helge; Nielsen, Thomas Dyhre; Rumí, Rafael; Salmerón, Antonio

Published in:
International Journal of Approximate Reasoning

DOI (link to publication from Publisher):
10.1016/j.ijar.2010.01.008

Publication date:
2010

Document Version
Early version, also known as pre-print

Link to publication from Aalborg University

Citation for published version (APA):
Langseth, H., Nielsen, T. D., Rumí, R., \& Salmerón, A. (2010). Parameter Estimation and Model Selection for Mixtures of Truncated Exponentials. International Journal of Approximate Reasoning, 51(5), 485-498. https://doi.org/10.1016/j.ijar.2010.01.008

## General rights

Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.

- Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
- You may not further distribute the material or use it for any profit-making activity or commercial gain
- You may freely distribute the URL identifying the publication in the public portal -


## Take down policy

If you believe that this document breaches copyright please contact us at vbn@aub.aau.dk providing details, and we will remove access to the work immediately and investigate your claim.

# Parameter Estimation and Model Selection for Mixtures of Truncated Exponentials 

Helge Langseth ${ }^{\mathrm{a}}$, Thomas D. Nielsen ${ }^{\mathrm{b}}$, Rafael Rumi ${ }^{\mathrm{c}}$, Antonio Salmerón ${ }^{\mathrm{c}}$<br>${ }^{a}$ Department of Computer and Information Science, The Norwegian University of Science and Technology, Trondheim (Norway)<br>${ }^{\mathrm{b}}$ Department of Computer Science, Aalborg University, Aalborg (Denmark)<br>${ }^{\text {c }}$ Department of Statistics and Applied Mathematics, University of Almería, Almería (Spain)


#### Abstract

Bayesian networks with mixtures of truncated exponentials (MTEs) support efficient inference algorithms and provide a flexible way of modeling hybrid domains (domains containing both discrete and continuous variables). On the other hand, estimating an MTE from data has turned out to be a difficult task, and most prevalent learning methods treat parameter estimation as a regression problem. The drawback of this approach is that by not directly attempting to find the parameter estimates that maximize the likelihood, there is no principled way of performing subsequent model selection using those parameter estimates. In this paper we describe an estimation method that directly aims at learning the parameters of an MTE potential following a maximum likelihood approach. Empirical results demonstrate that the proposed method yields significantly better likelihood results than existing regression-based methods. We also show how model selection, which in the case of univariate MTEs amounts to partitioning the domain and selecting the number of exponential terms, can be performed using the BIC-score.


## 1. Introduction

Domains involving both discrete and continuous variables represent a challenge to Bayesian networks. The main difficulty is to find a representation of the joint distribution of the continuous and discrete variables that supports an efficient implementation of the usual inference operations over Bayesian networks (like those found in junction tree-based algorithms for exact inference). Computationally, exact inference algorithms require that the joint distribution over the variables of the domain is from a distribution-class that is closed under addition and multiplication. The simplest way of obtaining such a distribution is to perform a discretization of the continuous variables (Friedman and Goldszmidt, 1996; Kozlov and Koller, 1997). Mathematically, this amounts to approximating the density function of every continuous variable by a step-function. However, discretization of variables can lead to a dramatic loss in precision, which is one of the reasons why other approaches have received much attention recently. The

mixtures of truncated exponentials (MTE) framework (Moral et al., 2001) has also received increasing interest over the last few years. One of the advantages of this representation is that MTE distributions allow discrete and continuous variables to be treated in a uniform fashion, and since the family of MTEs is closed under addition and multiplication, inference in an MTE network can be performed efficiently using the Shafer-Shenoy architecture (Shafer and Shenoy, 1990).

Cobb et al. (2006) empirically showed that many distributions can be approximated accurately by means of an MTE distribution, and they argue that this makes the MTE framework very attractive for Bayesian network models. Nevertheless, data-driven learning methods for MTE networks have received only little attention. In this context, focus has mainly been directed towards parameter estimation, where the most prevalent methods look for the MTE parameters minimizing the mean squared error w.r.t. a kernel density estimate of the data (Romero et al., 2006).

Although the least squares estimation procedure can yield a good MTE model in terms of generalization properties, there is no guarantee that the estimated parameter values will be close to the maximum likelihood (ML) parameters. This has a significant impact when considering more general problems such as model selection and structural learning, as many standard score functions for model selection, including the Bayesian information criterion (BIC) (Schwarz, 1978), assume ML parameter estimates to be available.

In this paper we propose a new parameter estimation procedure for univariate MTE potentials. The procedure directly aims at estimating the ML parameters for an MTE density, and we show how to utilize the learned ML estimates for model selection using the BIC score. The proposed learning method is empirically compared to the least squares estimation method described by Romero et al. (2006), and it is shown that it offers a significant improvement in terms of likelihood as well as in generalization ability.

The method described in this paper is a first step towards a general maximum likelihood-based approach for learning Bayesian networks with MTE potentials. Thus, our objective is solely to demonstrate that maximum likelihood estimators for MTE distributions can be found, and show how these estimators can be utilised for model selection. We will therefore prefer simple and robust methods over state-of-the-art optimisation techniques that can be harder to understand, implement, and examine. Furthermore, we shall only hint at some of the complexity problems that are involved in learning general MTE potentials. Learning MTE potentials using more efficient techniques is left as a topic for future research.

# 2. Preliminaries 

Throughout this paper, random variables will be denoted by capital letters, and their values by lowercase letters. In the multi-dimensional case, boldfaced characters will be used. The domain of the variables $\mathbf{X}$ is denoted by $\Omega_{\mathbf{X}}$. The

MTE model is defined by its corresponding potential and density as follows (Moral et al., 2001):

Definition 1. (MTE potential) Let $\mathbf{X}$ be a mixed $n$-dimensional random vector. Let $\mathbf{W}=\left(W_{1}, \ldots, W_{d}\right)^{\mathrm{T}}$ and $\mathbf{Z}=\left(Z_{1}, \ldots, Z_{c}\right)^{\mathrm{T}}$ be the discrete and continuous parts of $\mathbf{X}$, respectively, with $c+d=n$. We say that a function $f: \Omega_{\mathbf{X}} \mapsto \mathbb{R}_{0}^{+}$ is a Mixture of Truncated Exponentials (MTE) potential if for each fixed value $\mathbf{w} \in \Omega_{\mathbf{W}}$ of the discrete variables $\mathbf{W}$, the potential over the continuous variables $\mathbf{Z}$ is defined as:

$$
f(\mathbf{z})=a_{0}+\sum_{i=1}^{m} a_{i} \exp \left\{\mathbf{b}_{i}^{\top} \mathbf{z}\right\}
$$

for all $\mathbf{z} \in \Omega_{\mathbf{Z}}$, where $a_{i} \in \mathbb{R}$ and $\mathbf{b}_{i} \in \mathbb{R}^{c}, i=1, \ldots, m$. We also say that $f$ is an MTE potential if there is a partition $D_{1}, \ldots, D_{k}$ of $\Omega_{\mathbf{Z}}$ into hypercubes and in each $D_{\ell}, f$ is defined as in Equation (1). An MTE potential is an MTE density if it integrates to 1 .

In the remainder of this paper we shall focus on estimating the parameters for a univariate MTE density. Not surprisingly, the proposed methods also immediately generalize to the special case of conditional MTEs having only discrete conditioning variables.

# 3. Expressiveness of the MTE models 

In this section we will explore the expressiveness of the MTE framework, with the aim of showing that any univariate distribution function can be approximated arbitrarily well by an MTE potential. We will tie our argument to the example in Figure 1, but the results obtained are general in nature.

Consider first the left panel of Figure 1, where the target distribution of our example is given by the solid line. The target distribution, $f(x)$, is a mixture of two Gaussian distributions, one centred at $-\frac{1}{2}$ and the other at $\frac{1}{2}$. Both Gaussian distributions have standard deviation 1, and the mixture weights are .25 and .75 , respectively. The left panel of Figure 1 also shows how a standard discretization scheme can be utilised to approximate $f(x)$. Let $\hat{f}_{D}(x \mid k)$ be the approximation of $f(x)$ obtained by dividing the range of $X$ into $k$ equally sized intervals. Note that $\hat{f}_{D}(x \mid k)$ requires $k-1$ parameters to be fully specified, namely the amount of mass allocated to each interval except the last one. It is obvious that if we measure the error of $\hat{f}_{D}(x \mid k)$ as $\int_{x=a}^{b}\left(\hat{f}_{D}(x \mid k)-f(x)\right)^{2} \mathrm{~d} x$, then this error can be made arbitrarily small by increasing $k$. Since the class of MTE distributions contains all distributions obtainable by discretization, we can also approximate any $f(x)$ arbitrarily well using MTEs. This representation may not be optimal, though. In the left panel of Figure 1, 15 parameters were used to obtain the approximation, but it is still rather crude and the representational power of MTEs are not fully utilised.

The right panel of Figure 1 explore a different strategy for approximating $f(x)$, as we here define an approximation by increasing the number of exponential terms, without dividing the support of the distribution into intervals. We will denote approximations generated in this way by $\hat{f}_{e}(x \mid m)$, and for a given set of parameters $\boldsymbol{\alpha}$ we define $\hat{f}_{e}(x \mid m, \boldsymbol{\alpha})=\sum_{s=-m}^{m} \alpha_{s} \exp (s x)$. In the reminder of this section we investigate approximations of the type $\hat{f}_{e}(x \mid m, \boldsymbol{\alpha})$ and we will show that this strategy for approximating $f(x)$ can also be made arbitrarily accurate (wrt. our error measure) simply by increasing $m$. The right panel of Figure 1 shows this visually: We are again using 15 parameters, but the quality of the approximation is now so good that it is not possible to visually distinguish the true distribution from the approximation.
![img-0.jpeg](img-0.jpeg)
(a) Approximation improved by increasing no. intervals
![img-1.jpeg](img-1.jpeg)
(b) Approximation improved by increasing no. exponential terms

Figure 1: Two different strategies for approximating a distribution function. The gold standard model is in this case a mixture of two Gaussians, one centred at $-\frac{1}{2}$, the other at $\frac{1}{2}$.

We will make this argument by first restating a basic result from linear algebra, and then show how this generalises to our setting. Let us start by considering an $n$-dimensional real vector $\mathbf{z} \in \mathbb{R}^{n}$. Let $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{k}\right\}$ be a set of orthogonal basis vectors in $\mathbb{R}^{n}(k<n)$, and consider the task of approximating $\mathbf{z}$ by a vector in the span of the basis vectors. Let $\langle\mathbf{x}, \mathbf{y}\rangle$ denote the inner product between two vectors $\mathbf{x}$ and $\mathbf{y}$; when both $\mathbf{x}$ and $\mathbf{y}$ are in $\mathbb{R}^{n}$ we use $\langle\mathbf{x}, \mathbf{y}\rangle=\mathbf{x}^{\top} \mathbf{y}$. It is well-known that the least-squares solution to this approximation problem is to find the projection of $\mathbf{z}$ onto the space spanned by the basis vectors, i.e., to choose

$$
\hat{\mathbf{z}} \leftarrow \sum_{j=1}^{k} \frac{\left\langle\mathbf{e}_{j}, \mathbf{z}\right\rangle}{\sqrt{\left\langle\mathbf{e}_{j}, \mathbf{e}_{j}\right\rangle}} \cdot \mathbf{e}_{j}
$$

Next, we generalize this result from approximations in $\mathbb{R}^{n}$ to approximations in a space containing functions, with the idea that we can approximate a function $f$ as a linear combination of basis functions. In particular, we will consider the space of all functions that are squared integrable on an interval $[a, b]$. This space

is often denoted $L_{2}[a, b]$, so for a real function $f$ we have that $f \in L_{2}[a, b]$ if and only if $\int_{x=a}^{b} f(x) \cdot f(x) \mathrm{d} x<\infty$. To find an analogue to the projections in Equation (2) we must define the inner product between two functions $f$ and $g$, and in $L_{2}[a, b]$ this is done as $\langle f, g\rangle=\int_{a}^{b} f(x) \cdot g(x) d x$. Furthermore, we say that two functions $f$ an $g$ are orthogonal if and only if $\langle f, g\rangle=0$.

Focus on $L_{2}[0,2 \pi]$ and consider the task of finding the Fourier series approximation of a function $f$. This amounts to approximating $f$ by a sum of trigonometric functions, i.e., it is a solution to our original approximation problem, where the functions $\{1, \sin (x), \cos (x), \sin (2 x), \cos (2 x), \sin (3 x), \ldots\}$ take the role of the orthogonal ${ }^{1}$ basis-vectors $\left\{\mathbf{e}_{1} \ldots \mathbf{e}_{k}\right\}$ used when making approximations in $\mathbb{R}^{n}$. Recall that the Fourier series approximation of $f$ can be written as

$$
\hat{f}(x) \leftarrow \sum_{j=1}^{k} \frac{\left\langle e_{j}, f\right\rangle}{\sqrt{\left\langle e_{j}, e_{j}\right\rangle}} \cdot e_{j}(x)
$$

This gives an operational description of how to approximate any $f \in L_{2}[0,2 \pi]$ by a sum of trigonometric functions.

The last step in our argument is to recall that the approach of Equation (3) is valid also when the trigonometric functions are replaced by other orthogonal basis functions; in this case Equation (3) is called a Generalized Fourier series. Since we look for MTE approximations, we are interested in the span of the exponential functions $\{1, \exp (x), \exp (-x), \exp (2 x), \exp (-2 x), \ldots\}$. The exponential functions are dense in $L_{2}[a, b]$, loosely meaning that any function $f$ can be approximated arbitrarily well by a linear combination of exponential functions. Unfortunately, the specified exponential functions are not orthogonal, so an orthogonalisation process (also known as a Gram-Schmidt process) must be conducted before the generalised Fourier coefficients can be found. The approximation of Figure 1 is made in this way, starting from the 15 functions $\{\exp (-7 x), \ldots, \exp (7 x)\}$.

When we in the following look at ways to learn MTEs, we are trying to find a balance between the number of split points and the number of exponential terms: we aim for an approximation, where the support of the density may be divided into "a few" intervals, each interval containing "a few" exponential terms. Our goal is therefore to find a parameterization that is close to minimal, and that at the same time offers robust techniques for learning the parameters from data. This will be the topic of the remainder of the paper.

# 4. Maximum Likelihood Parameter Estimation for Univariate MTEs 

The problem of estimating a univariate MTE density from data can be divided into three tasks: $i$ ) Partition the domain of the variable into disjoint

[^0]
[^0]:    ${ }^{1}$ Recall that we have $\int_{x=0}^{2 \pi} \sin (n x) \cos (m x) \mathrm{d} x \equiv 0$ for integer $n, m$, and that if we also assume that $n \neq m$ we get $\int_{x=0}^{2 \pi} \sin (n x) \sin (m x) \mathrm{d} x=\int_{x=0}^{2 \pi} \cos (n x) \cos (m x) \mathrm{d} x \equiv 0$.

intervals, $i i$ ) determine the number of exponential terms for each interval, and iii) estimate the parameters for a given interval and a fixed number of exponential terms. At this point we will concentrate on the estimation of the parameters, assuming that the split points are known, and that the number of exponential terms is fixed. We will return to the two remaining tasks in Section 5.

We start this section by introducing some notation. Consider a random variable $X$ with density function $f(x)$ and assume that the support of $f(x)$ is divided into $M$ intervals $\left\{\Omega_{i}\right\}_{i=1}^{M}$. Focus on one particular interval $\Omega_{m}$. As a target density for $x \in \Omega_{m}$ we will consider an MTE with 2 exponential terms:

$$
f\left(x \mid \boldsymbol{\theta}_{m}\right)=k_{m}+a_{m} e^{b_{m} x}+c_{m} e^{d_{m} x}, x \in \Omega_{m}
$$

This function has 5 parameters, namely $\boldsymbol{\theta}_{m}=\left(k_{m}, a_{m}, b_{m}, c_{m}, d_{m}\right)^{\top}$. For notational convenience we may sometimes drop the subscript $m$ when clear from the context.

# 4.1. The Likelihood Landscape 

For an MTE of the form given in Equation (4), the shape of the likelihood landscape is not well-known. To investigate this, we sampled two datasets of 50 and 1000 samples from the distribution

$$
f(x)= \begin{cases}\frac{5}{2(\exp (5)-1)} \exp (5 x)-\frac{5}{2(\exp (-5)-1)} \exp (-5 x) & \text { if } x \in[-1,1] \\ 0 & \text { otherwise }\end{cases}
$$

The profile likelihood of the two datasets are shown in Figure 2, where the value at the point $\left(b_{0}, d_{0}\right)$ is given as $\max _{k, a, c} \prod_{i}\left\{k+a \exp \left(b_{0} \cdot x_{i}\right)+c \exp \left(d_{0} \cdot x_{i}\right)\right\}$ and the product is over all samples in the data set.

From the figure we see that the profile likelihood is symmetric around the line $b=d$, i.e. that the profile likelihood of a sample at point $\left(b_{0}, d_{0}\right)$ is identical to the one at $\left(d_{0}, b_{0}\right)$. The consequence is that the parameters of an MTE are not identifiable in a strict sense. This is not surprising, as MTE models are generalized mixture models ("generalized" because we do not demand the weights to be positive and sum to one). Furthermore, we see that for the relatively small dataset of 50 samples, the profile likelihood is fairly flat, so finding a local maxima using a standard hill-climbing approach may be very slow. Furthermore, the profile likelihood is multi-modal. On the other hand, the profile likelihood is peaked for the large sample. To be successful in learning MTEs, an algorithm must therefore be able to handle "flat" multi-modal likelihood landscapes as well as very peaked likelihood landscapes.

### 4.2. Parameter Estimation by Maximum Likelihood

Assume that we have a sample $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)^{\mathrm{T}}$ and that $n_{m}$ of the $n$ observations are in $\Omega_{m}$. To ensure that the overall parameter-set is a maximum likelihood estimate for $\boldsymbol{\Theta}=\cup_{m} \boldsymbol{\theta}_{m}$, it is required that

$$
\int_{x \in \Omega_{m}} f\left(x \mid \boldsymbol{\theta}_{m}\right) d x=n_{m} / n
$$

![img-2.jpeg](img-2.jpeg)

Figure 2: Profile likelihood of example data sampled from a known distribution. The left panel shows the results using 50 samples, the right plot gives the result for 1000 samples.

Given this normalization, we can fit the parameters for each interval $\Omega_{m}$ separately, i.e., the parameters in $\boldsymbol{\theta}_{m}$ are optimized independently of those in $\boldsymbol{\theta}_{m^{\prime}}$. Based on this observation, we shall only describe the learning procedure for a fixed interval $\Omega_{m}$, since the generalization to the whole support of $f(x)$ is immediate.

Assume now that the target density is as given in Equation (4), in which case the likelihood function for a sample $\mathbf{x}$ is

$$
L\left(\boldsymbol{\theta}_{m} \mid \mathbf{x}\right)=\prod_{i: x_{i} \in \Omega_{m}}\left\{k_{m}+a_{m} e^{b_{m} x_{i}}+c_{m} e^{d_{m} x_{i}}\right\}
$$

To find a closed-form solution for the maximum likelihood estimators, we need to differentiate Equation (6) wrt. the different parameters and set the results equal to zero. To exemplify, we perform this exercise for $b_{m}$, and obtain

$$
\begin{gathered}
\frac{\partial L\left(\boldsymbol{\theta}_{m} \mid \mathbf{x}\right)}{\partial b_{m}}=\sum_{i: x_{i} \in \Omega_{m}}\left\{\frac{\partial L\left(\boldsymbol{\theta}_{m} \mid x_{i}\right)}{\partial b_{m}} \prod_{j: x_{j} \in \Omega_{m}, j \neq i} L\left(\boldsymbol{\theta}_{m} \mid x_{j}\right)\right\} \\
=a_{m} x_{i} \sum_{i: x_{i} \in \Omega_{m}} e^{b_{m} x_{i}}\left\{\prod_{j: x_{j} \in \Omega_{m}, j \neq i}\left(k_{m}+a_{m} e^{b_{m} x_{j}}+c_{m} e^{d_{m} x_{j}}\right)\right\}
\end{gathered}
$$

Unfortunately, Equation (7) is non-linear in the unknown parameters $\boldsymbol{\theta}_{m}$. Furthermore, both the number of terms in the sum as well as the number of terms inside the product operator grows as $O\left(n_{m}\right)$; thus, the maximization of the likelihood becomes increasingly difficult as the number of observations rise.

Alternatively, one might consider maximizing the logarithm of the likelihood, or more specifically a lower bound for the likelihood using Jensen's inequality. By assuming that $k_{m}>0, a_{m}>0$ and $c_{m}>0$ we have

$$
\begin{aligned}
& \log \left(L\left(\boldsymbol{\theta}_{m} \mid \mathbf{x}\right)\right)=\sum_{i: x_{i} \in \Omega_{m}} \log \left(k_{m}+a_{m} \exp \left(b_{m} x_{j}\right)+c_{m} \exp \left(d_{m} x_{j}\right)\right) \\
& \geq \sum_{i: x_{i} \in \Omega_{m}} \log \left(k_{m}\right)+\sum_{i: x_{i} \in \Omega_{m}} \log \left(a_{m} \exp \left(b_{m} x_{j}\right)\right)+\sum_{i: x_{i} \in \Omega_{m}} \log \left(c_{m} \exp \left(d_{m} x_{j}\right)\right) \\
& =n_{m}\left[\log \left(k_{m}\right)+\log \left(a_{m}\right)+\log \left(c_{m}\right)\right]+\left(b_{m}+d_{m}\right) \sum_{i: x_{i} \in \Omega_{m}} x_{i}
\end{aligned}
$$

and the idea would then be to maximize the lowerbound of Equation (8) to push the likelihood upwards (following the same reasoning underlying the EM algorithm (Dempster et al., 1977) and variational methods (Jordan et al., 1999)). Unfortunately, though, restricting $k_{m}, a_{m}$ and $c_{m}$ to be positive enforces too strict a limitation on the expressiveness of the distributions we learn.

Another possibility would be to use a modified version of the EM algorithm able to handle negative components. For example, Farag et al. (2004) consider the estimation of linear combinations of Gaussians. However, in each iteration of their procedure, the parameters are optimized by Lagrange maximization, which in the case of our likelihood function (Equation (6)) does not provide any simplification.

The main problem when trying to apply the EM algorithm to MTE densities is to find a formulation of the problem, where the inclusion of latent variables simplifies the estimation when the values of the latent variables are fixed. However, if this conditional density is also of MTE shape, the maximisation of the conditional expectation with respect to the parameters in each iteration would again be as difficult as the original problem. In this case, even the use of a flexible implementation like Monte Carlo EM (see, for instance Tanner (1996)) does not provide any simplification, as approximating the integral associated with the conditional expectation by simulation produces a sum of MTE functions, which again is as difficult to optimize as the original likelihood.

Instead, we opt for an approximate solution obtained by solving the likelihood equations by numerical means. The proposed method for maximizing the likelihood is based on the observation that maximum likelihood estimation for MTEs can be seen as a constrained optimization problem, where constraints are introduced to ensure that both $f\left(x \mid \boldsymbol{\theta}_{m}\right) \geq 0$, for all $x \in \Omega_{m}$, and that Equation (5) is fulfilled. A natural framework for solving this is the Lagrange multipliers, but since solving the Lagrange equations are inevitably at least as difficult as solving the unconstrained problem, this cannot be done analytically. In our implementation we have settled for a numerical solution based on Newton's method; this is described in detail in Section 4.2.2. However, it is well-known that Newton's method is quite sensitive to the initialization-values, meaning that if we initialize a search for a solution to the Lagrange equations from a parameter-set far from the optimal values, it will not necessarily converge to a useful solution. Thus, we need a simple and robust procedure for initializing Newton's method, and this is described next.

# 4.2.1. Naïve Maximum Likelihood for MTE Distributions 

The general idea of the naïve approach is to iteratively update the parameter estimates until convergence. More precisely, this is done by iteratively tuning pairs of parameters, while the other parameters are kept fixed. We do this in a round-robin manner, making sure that all parameters are eventually tuned. Denote by $\hat{\boldsymbol{\theta}}^{\dagger}=\left(k^{t}, a^{t}, b^{t}, c^{t}, d^{t}\right)^{\top}$ the parameter values after iteration $t$ of this iterative scheme. Algorithm 4.1 is a top-level description of this procedure, where steps 4 and 5 correspond to the optimization of the shape-parameters and steps 6 and 7 distribute the mass between the terms in the MTE potential (the different steps are explained below).

```
Algorithm 4.1 The algorithm learns a "rough" estimate of the parameters of
an MTE with two exponential terms.
    function NAÏVE_MTE(x)
        Initialize \(\hat{\boldsymbol{\theta}}^{0} ; t \leftarrow 0\).
        repeat
            \(\left(a^{\prime}, b^{\prime}\right) \leftarrow \arg \max _{a, b} L\left(k^{t}, a, b, c^{t}, d^{t} \mid \mathbf{x}\right)\)
            \(\left(c^{\prime}, d^{\prime}\right) \leftarrow \arg \max _{c, d} L\left(k^{t}, a^{\prime}, b^{\prime}, c, d \mid \mathbf{x}\right)\)
            \(\left(k^{\prime}, a^{\prime}\right) \leftarrow \arg \max _{k, a} L\left(k, a, b^{\prime}, c^{\prime}, d^{\prime} \mid \mathbf{x}\right)\)
            \(\left(k^{\prime}, c^{\prime}\right) \leftarrow \arg \max _{k, c} L\left(k, a^{\prime}, b^{\prime}, c, d^{\prime} \mid \mathbf{x}\right)\)
            \(\boldsymbol{\theta}^{t+1} \leftarrow\left(k^{\prime}, a^{\prime}, b^{\prime}, c^{\prime}, d^{\prime}\right)^{\top}\)
            \(t \leftarrow t+1\)
        until convergence
        return \(\hat{\boldsymbol{\theta}}^{\dagger}\)
```

For notational convenience we shall define the auxiliary function $p(s, t)=$ $\int_{x \in \Omega_{m}} s \exp (t x) d x ; p(s, t)$ is the integral of the exponential function over the interval $\Omega_{m}$. Note, in particular, that $p(s, t)=s \cdot p(1, t)$, and that $p(1,0)=$ $\int_{x \in \Omega_{m}} d x$ is the length of the interval $\Omega_{m}$. The first step above is initialization. In our experiments we have chosen $b^{0}$ and $d^{0}$ as +1 and -1 , respectively. The parameters $k^{0}, a^{0}$, and $c^{0}$ are set to ensure that each of the three terms in the integral of Equation (5) contribute with equal probability mass, i.e.,

$$
\begin{aligned}
k^{0} & \leftarrow \frac{n_{m}}{3 n \cdot p(1,0)} \\
a^{0} & \leftarrow \frac{n_{m}}{3 n \cdot p\left(1, b^{0}\right)} \\
c^{0} & \leftarrow \frac{n_{m}}{3 n \cdot p\left(1, d^{0}\right)}
\end{aligned}
$$

Iteratively improving the likelihood under the constraints is actually quite simple as long as the parameters are considered in pairs. Consider Step 4 above, where we optimize $a$ and $b$ under the constraint of Equation (5) while keeping the other parameters ( $k^{t}, c^{t}$, and $d^{t}$ ) fixed. Observe that if Equation (5) is to be satisfied after this step we need to make sure that $p\left(a^{\prime}, b^{\prime}\right)=p\left(a^{t}, b^{t}\right)$.

Equivalently, there is a functional constraint between the parameters that we enforce by setting $a^{\prime} \leftarrow p\left(a^{t}, b^{t}\right) / p\left(1, b^{\prime}\right)$. Optimizing the value for the pair $(a, b)$ is now simply done by line-search, where only the value for $b$ is considered:

$$
b^{\prime}=\arg \max _{b} L\left(k, \frac{p\left(a^{t}, b^{t}\right)}{p(1, b)}, b, c^{t}, d^{t} \mid \mathbf{x}\right)
$$

Note that at the same time we choose $a^{\prime} \leftarrow p\left(a^{t}, b^{t}\right) / p\left(1, b^{\prime}\right)$. A similar procedure is used in Step 5 to find $c^{\prime}$ and $d^{\prime}$.

Steps 6 and 7 utilize the same idea, but with a different normalization equation. We only consider Step 6 here, since the generalization is immediate. For this step we need to make sure that $\int_{x \in \Omega_{m}} k+a \exp \left(b^{\prime} x\right) d x=\int_{x \in \Omega_{m}} k^{t}+$ $a^{t} \exp \left(b^{\prime} x\right) d x$, for any pair of parameter candidates $(k, a)$. By rephrasing, we find that this is obtained if we insist that $k^{\prime} \leftarrow k^{t}-p\left(a^{\prime}-a^{t}, b^{\prime}\right) / p(1,0)$. Again, the constrained optimization of the pair of parameters can be performed using line-search in one dimension (and let the other parameter be adjusted to keep the total probability mass constant).

Note that Steps 4 and 5 do not move "probability mass" between the three terms in Equation (4), these two steps only fit the shape of the two exponential functions. On the other hand, Steps 6 and 7 assume the shape of the exponentials fixed, and proceed by moving "probability mass" between the three terms in the sum of Equation (4).

# 4.2.2. Refining the Initial Estimate 

The parameter estimates returned by the line-search method can be further refined by using these estimates to initialize a nonlinear programming problem formulation of the original optimization problem. In this formulation, the function to be maximized is again the log-likelihood of the data, subject to the constraints that the MTE potential should be nonnegative, and that

$$
g_{0}(\mathbf{x}, \boldsymbol{\theta}) \equiv \int_{x \in \Omega_{m}} f(x \mid \boldsymbol{\theta}) d x-\frac{n_{m}}{n}=0
$$

Ideally the nonnegative constraints should be specified for all $x \in \Omega_{m}$, but since this is not feasible we only encode that the function should be nonnegative in the endpoints $\omega_{s}$ and $\omega_{e}$ of the interval (we shall return to this issue later). Thus, we arrive at the following formulation:

$$
\begin{aligned}
& \text { Maximize } \log L(\boldsymbol{\theta} \mid \mathbf{x})=\sum_{i: x_{i} \in \Omega_{m}} \log L\left(\boldsymbol{\theta} \mid x_{i}\right) \\
& \text { Subject to } g_{0}(\mathbf{x}, \boldsymbol{\theta})=0 \\
& \qquad f\left(\omega_{s} \mid \boldsymbol{\theta}\right) \geq 0 \\
& \qquad f\left(\omega_{e} \mid \boldsymbol{\theta}\right) \geq 0
\end{aligned}
$$

To convert the two inequalities into equalities we introduce slack variables:

$$
f(x \mid \boldsymbol{\theta}) \geq 0 \Leftrightarrow f(x \mid \boldsymbol{\theta})-s^{2}=0, \text { for some } s \in \mathbb{R}
$$

we shall refer to these new equalities using $g_{1}\left(e_{1}, \boldsymbol{\theta}, s_{1}\right)$ and $g_{2}\left(e_{2}, \boldsymbol{\theta}, s_{2}\right)$, respectively. We now have the following equality constrained optimization problem:

$$
\begin{aligned}
& \text { Maximize } \log L(\boldsymbol{\theta} \mid \mathbf{x})=\sum_{i: x_{i} \in \Omega_{m}} \log L\left(\boldsymbol{\theta} \mid x_{i}\right) \\
& \text { Subject to } \mathbf{g}(\mathbf{x}, \boldsymbol{\theta})=\left[\begin{array}{c}
g_{0}(\mathbf{x}, \boldsymbol{\theta}) \\
g_{1}\left(\omega_{s}, \boldsymbol{\theta}, s_{1}\right) \\
g_{2}\left(\omega_{e}, \boldsymbol{\theta}, s_{2}\right)
\end{array}\right]=\mathbf{0}
\end{aligned}
$$

This optimization problem can be solved using the method of Lagrange multipliers. That is, with the Lagrangian function $l(\mathbf{x}, \boldsymbol{\theta}, \boldsymbol{\lambda}, \mathbf{s})=\log L(\boldsymbol{\theta} \mid \mathbf{x})+$ $\lambda_{0} g_{0}(x, \boldsymbol{\theta})+\lambda_{1} g_{1}\left(\omega_{s}, \boldsymbol{\theta}, s_{1}\right)+\lambda_{2} g_{2}\left(\omega_{e}, \boldsymbol{\theta}, s_{2}\right)$ we look for a solution to the equalities defined by

$$
A(\mathbf{x}, \boldsymbol{\theta}, \boldsymbol{\lambda}, \mathbf{s})=\nabla l(\mathbf{x}, \boldsymbol{\theta}, \boldsymbol{\lambda}, \mathbf{s})=0
$$

Such a solution can be found numerically by applying Newton's method. Specifically, by letting $\boldsymbol{\theta}^{\prime}=\left(\boldsymbol{\theta}^{+}, s_{1}, s_{2}\right)^{+}$, the Newton updating step is given by

$$
\left[\begin{array}{c}
\boldsymbol{\theta}_{t+1}^{\prime} \\
\boldsymbol{\lambda}_{t+1}
\end{array}\right]=\left[\begin{array}{c}
\boldsymbol{\theta}_{t}^{\prime} \\
\boldsymbol{\lambda}_{t}
\end{array}\right]-\nabla A\left(\mathbf{x}, \boldsymbol{\theta}_{t}^{\prime}, \boldsymbol{\lambda}_{t}\right)^{-1} A\left(\mathbf{x}, \boldsymbol{\theta}_{t}^{\prime}, \boldsymbol{\lambda}_{t}\right)
$$

where $\boldsymbol{\theta}_{t}^{\prime}$ and $\boldsymbol{\lambda}_{t}$ are the current estimates and

$$
\begin{gathered}
A\left(\mathbf{x}, \boldsymbol{\theta}_{t}^{\prime}, \boldsymbol{\lambda}_{t}\right)=\left[\begin{array}{cc}
\nabla \boldsymbol{\theta}^{\prime} l\left(\mathbf{x}, \boldsymbol{\theta}^{\prime}, \boldsymbol{\lambda}\right) \\
\mathbf{g}\left(\mathbf{x}, \boldsymbol{\theta}^{\prime}\right)
\end{array}\right] \\
\nabla A\left(\mathbf{x}, \boldsymbol{\theta}_{t}^{\prime}, \boldsymbol{\lambda}_{t}\right)=\left[\begin{array}{cc}
\nabla_{\boldsymbol{\theta}^{\prime}}^{2} \boldsymbol{\theta}^{\prime} l\left(\mathbf{x}, \boldsymbol{\theta}^{\prime}, \boldsymbol{\lambda}\right) & \nabla \mathbf{g}\left(\mathbf{x}, \boldsymbol{\theta}^{\prime}\right) \\
\nabla \mathbf{g}\left(\mathbf{x}, \boldsymbol{\theta}^{\prime}\right)^{T} & 0
\end{array}\right]
\end{gathered}
$$

As initialization values, $\boldsymbol{\theta}_{0}$, we use the maximum likelihood estimates returned by the line-search method described in Section 4.2, and in order to control the step size during updating, we employ the Armijo rule (Bertsekas, 1996). For the test results reported in Section 7, the Lagrange multipliers were initialized (somewhat arbitrarily) to 1 and the slack variables were set to $\sqrt{f\left(\omega_{s} \mid \boldsymbol{\theta}_{0}\right)}$ and $\sqrt{f\left(\omega_{e} \mid \boldsymbol{\theta}_{0}\right)}$, respectively.

Finally, it should be emphasized that the above search procedure may lead to $f(x \mid \boldsymbol{\theta})$ being negative for some $x$. In the current implementation we have addressed this problem rather crudely: simply terminate the search when negative values are encountered. Moreover, due to numerical instability, the search is also terminated if the determinant for the system is close to zero $\left(<10^{-9}\right)$ or if the condition number is large $\left(>10^{9}\right)$. Note that by terminating the search before convergence, we have no guarantees about the solution. In particular, the solution may be worse than the initial estimate. In order to overcome this problem, we always store the best parameter estimates found so far (including those found by line search) and return these estimates upon termination.

# 5. Model Selection for Univariate MTE 

So far we have mainly considered MTEs with two exponential terms and with pre-specified spilt points. However, when learning an MTE potential these model parameters (i.e., the model structure) should ideally also be deduced from data.

In this section we pose MTE structure learning as a model selection problem. For the score function specification, one might take a Bayesian approach and define a candidate score function based on a conjugate prior for the MTE distribution. As a possible prior distribution, we could again look towards the MTE distribution; recall that the class of MTE distributions is closed under addition and multiplication. Unfortunately, the parameters defining an MTE distribution are not independent (as we shall see below), and it is not apparent how to specify a joint prior MTE distribution so that only admissible parameter configurations (i.e., those specifying an MTE density) contribute with non-zero probability mass. As an alternative, we resort to penalized log-likelihood when scoring the model structures. Specifically, we use the Bayesian information criterion (BIC) (Schwarz, 1978):

$$
\operatorname{BIC}(f)=\sum_{i=1}^{n} \log f\left(x_{i} \mid \hat{\boldsymbol{\theta}}\right)-\frac{\operatorname{dim}(f)}{2} \log (n)
$$

where $\operatorname{dim}(f)$ is the number of free parameters in the model. To determine $\operatorname{dim}(f)$, consider an MTE potential $f(x \mid \boldsymbol{\theta})$ defined by the functions

$$
f_{j}\left(x \mid \boldsymbol{\theta}_{j}\right)=a_{0}^{(j)}+\sum_{i=1}^{m_{j}} a_{i}^{(j)} \exp \left(b_{i}^{(j)} \cdot x\right), \quad 1 \leq j \leq M
$$

for all $x \in \Omega_{j}=\left[\omega_{x}^{(j)} ; \omega_{e}^{(j)}\right]$. In order for $f(x)$ to be a density, each sub-function $f_{j}\left(x \mid \boldsymbol{\theta}_{j}\right)$ should be both non-negative and account for some probability mass $c_{j}$ (i.e., $\left.\int_{x \in \Omega_{j}} f_{j}\left(x \mid \boldsymbol{\theta}_{j}\right) d x=c_{j}\right)$ s.t. $\sum_{j=1}^{M} c_{j}=1$. First, we ensure that $f_{j}\left(x \mid \boldsymbol{\theta}_{j}\right)$ is non-negative by adding a positive value $a_{0}^{\prime}$, thus tying the parameter $a_{0}$ in $\boldsymbol{\theta}_{j}$. Next, to ensure that $\int_{x \in \Omega_{j}} f_{j}\left(x \mid \boldsymbol{\theta}_{j}\right) d x=c_{j}$ we note that
$\int_{x \in \Omega_{j}} f\left(x \mid \boldsymbol{\theta}_{j}\right) d x=a_{0}\left(\omega_{e}^{(j)}-\omega_{s}^{(j)}\right)+\sum_{i=1}^{m_{j}} \frac{a_{i}^{(j)}}{b_{i}^{(j)}}\left(\exp \left(b_{i}^{(j)} \omega_{e}^{(j)}\right)-\exp \left(b_{i}^{(j)} \omega_{s}^{(j)}\right)\right)$,
and by tying, say $a_{1}^{(j)}$, such that
$a_{1}^{(j)}=b_{1}^{(j)}\left[\frac{c_{j}-\sum_{i=2}^{m_{j}} \frac{a_{i}^{(j)}}{b_{i}^{(j)}}\left(\exp \left(b_{i}^{(j)} \omega_{e}^{(j)}\right)-\exp \left(b_{i}^{(j)} \omega_{s}^{(j)}\right)\right)-a_{0}\left(\omega_{e}^{(j)}-\omega_{s}^{(j)}\right)}{\exp \left(b_{1}^{(j)} \omega_{e}^{(j)}\right)-\exp \left(b_{1}^{(j)} \omega_{s}^{(j)}\right)}\right]$
we have that $\int_{x \in \Omega_{j}} f(x) d x=c_{j}$. For the function $f_{j}\left(x \mid \boldsymbol{\theta}_{j}\right)$, the number of free parameters is therefore $2 \cdot m_{j}-1$, and hence the number of free parameters in

$f(x \mid \boldsymbol{\theta})$ is given by $\operatorname{dim}(f)=\sum_{j=1}^{M}\left(2 \cdot m_{j}-1\right)+(M-1)=\sum_{j=1}^{M} 2 \cdot m_{j}-1$, where the last $M-1$ parameters encode the probability masses assigned to the $M$ intervals or, equivalently, the choice of split points.

Based on the score function above, we can now define a search method for learning the structure of an MTE. The method is recursive and relies on two other methods for learning the number of exponential terms and the location of the split points, respectively.

When learning the number of exponential terms, for a fixed interval $\Omega_{j}$, we follow a greedy approach and iteratively add exponential terms (starting with the MTE potential having only a constant term) as long as the BIC score improves or until some other termination criterion is met. The method is summarized by the pseudo-code in Algorithm 5.1, where the function Estimate_MTE_Parameters $\left(\mathbf{x}, \omega_{s}, \omega_{e}, i\right)$ implements the parameter estimation procedure described in Section 4.2 for an MTE density defined over the interval $\left[\omega_{s}, \omega_{e}\right]$ and with $i$ exponential terms. It should be emphasized that the main aim of Algorithm 5.1 (as well as Algorithms 5.2 and 5.3 below) is only to convey the general structure of a possible learning algorithm. Time complexity is therefore given less attention at this point, but will be further addressed at the end of the section.

```
Algorithm 5.1 The algorithms learns an MTE density (including the number
of exponential terms) for the interval \(\left[\omega_{s}, \omega_{e}\right]\).
function CANDIDATE_MTE \(\left(\mathbf{x}, \omega_{s}, \omega_{e}\right)\)
    \(i \leftarrow 0 \quad \triangleright i\) specifies the number of exponential terms
    \((t m p \boldsymbol{\theta}, t m p B I C) \leftarrow\) Estimate_MTE_Parameters \(\left(\mathbf{x}, \omega_{s}, \omega_{e}, i\right)\)
    repeat
        \(i \leftarrow i+1\)
        \((\) best \(\boldsymbol{\theta}\), bestBIC \() \leftarrow(t m p \boldsymbol{\theta}, t m p B I C)\)
        \((t m p \boldsymbol{\theta}, t m p B I C) \leftarrow\) Estimate_MTE_Parameters \(\left(\mathbf{x}, \omega_{s}, \omega_{e}, i\right)\)
    until termination \(\quad \triangleright\) E.g. \(t m p B I C \leq\) bestBIC or max-iter. reached
    return (best \(\boldsymbol{\theta}\), bestBIC \()\)
```

For a given interval $\Omega_{j}$ there is in principle an uncountable number of possible split points; however, the BIC function will assign the same score to any two split points that define the same partitioning of the training data. We therefore define the candidate split points based on the number of ways in which we can split the training data. Given these candidate split points we take a myopic approach and select the split point with the highest BIC score, assuming that the score cannot be improved by further refinement of the two sub-intervals defined by the chosen split point (see Algorithm 5.2).

Based on the two methods above, we can now outline a simple procedure for learning the structure (and the parameters) for an MTE density: recursively select the best split point (if any) for the current (sub)-interval. The overall algorithm is summarized in Algorithm 5.3, which takes as input an MTE model current $\boldsymbol{\theta}$ defined over the interval $\left[\omega_{s}, \omega_{e}\right]$, i.e., the algorithm should be invoked

```
Algorithm 5.2 The algorithm finds a candidate split point for the interval
\(\left[\omega_{s}, \omega_{e}\right]\). We use the notation \(\mathbf{x}\left(x>x_{i}\right)\) to denote the data points \(x\) in \(\mathbf{x}\) for
which \(x>x_{i}\); analogously for \(\mathbf{x}\left(x \leq x_{i}\right)\).
    function CANDIDATE_SPLIT_MTE \(\left(\mathbf{x}, \omega_{s}, \omega_{e}\right)\)
        bestBIC \(\leftarrow-\infty\)
        for \(i \leftarrow 1: n-1\) do \(\triangleright n\) is the number of data points
            \(\boldsymbol{\theta}_{1} \leftarrow\) CANDIDATE_MTE \(\left(\mathbf{x}\left(x \leq x_{i}\right), \omega_{s}, x_{i}\right)\)
            \(\boldsymbol{\theta}_{2} \leftarrow \operatorname{CANDIDATE}_{-} \operatorname{MTE}\left(\mathbf{x}\left(x>x_{i}\right), x_{i}, \omega_{e}\right)\)
            if \(\operatorname{BIC}\left(\boldsymbol{\theta}_{1}, \boldsymbol{\theta}_{2}, \mathbf{x}\right)>\) bestBIC then
                bestBIC \(\leftarrow \operatorname{BIC}\left(\boldsymbol{\theta}_{1}, \boldsymbol{\theta}_{2}, \mathbf{x}\right)\)
                bestSplit \(\leftarrow\left(x_{i+1}-x_{i}\right) / 2\)
                \(\boldsymbol{\theta}_{1}^{*} \leftarrow \boldsymbol{\theta}_{1}\)
                \(\boldsymbol{\theta}_{2}^{*} \leftarrow \boldsymbol{\theta}_{2}\)
            return \(\left(\boldsymbol{\theta}_{1}^{*}, \boldsymbol{\theta}_{2}^{*}\right.\), bestBIC, bestSplit \()\)
```

with $\mathbf{x}, \omega_{s}, \omega_{e}$, and $\operatorname{CANDIDATE}_{-} \operatorname{MTE}\left(\mathbf{x}, \omega_{s}, \omega_{e}\right)$.
Algorithm 5.3 The algorithm learns the parameters and the structure of an MTE potential for the interval $\left[\omega_{s}, \omega_{e}\right]$. The algorithm is invoked with current $\boldsymbol{\theta}$, which is an MTE for $\left[\omega_{s}, \omega_{e}\right]$ without split points (found using Algorithm 4.1). Note that $\mathbf{x}(x \leq$ candSplit $)$ denotes the data points $x$ in $\mathbf{x}$ for which $x \leq$ candSplit; analogously for $\mathbf{x}(x>$ candSplit $)$
function Learn_MTE( $\left.\mathbf{x}, \omega_{s}, \omega_{e}, \operatorname{current} \boldsymbol{\theta}\right)$
currentBIC $\leftarrow \operatorname{BIC}\left(\mathbf{x}, \omega_{s}, \omega_{e}, \operatorname{current} \boldsymbol{\theta}\right)$
$\left[\boldsymbol{\theta}_{1}, \boldsymbol{\theta}_{2}\right.$, candSplit, candBIC $\left.\left[\leftarrow \mathrm{CANDIDATE}_{-} \mathrm{S} P L I T_{-} \mathrm{M} T E\left(\mathbf{x}, \omega_{s}, \omega_{e}\right)\right.\right.$
if candBIC $>$ currentBIC then
$\left(\right.$ splits $\left._{i}, \boldsymbol{\theta}_{i}\right) \leftarrow \operatorname{Learn} \_\mathrm{MTE}\left(\mathbf{x}(x \leq\right.$ candSplit $), \omega_{s}$, candSplit, $\left.\boldsymbol{\theta}_{1}\right)$
(splits $\left., \boldsymbol{\theta}_{r}$ ) $\leftarrow \operatorname{Learn}_{-} \operatorname{MTE}\left(\mathbf{x}(x>\right.$ candSplit $)$, candSplit, $\left.\omega_{e}, \boldsymbol{\theta}_{2}\right)$
splits $\leftarrow\left[\right.$ splits $\left._{i}\right.$, candSplit, splits $\left._{r}\right]$
$\Theta \leftarrow\left(\boldsymbol{\theta}_{l} ; \boldsymbol{\theta}_{r}\right)$
else
splits $=[]$
$\Theta=[]$
return (splits, $\theta$ )

The worst case computational complexity of the algorithm above is $O\left(n^{3}\right)$, where $n$ is the number of data points (we assume that the number of exponential terms is significantly smaller than $n$ ). This is clearly prohibitive for all but the smallest data sets. In order to overcome this problem, we can instead prespecify a collection of candidate split points found by making an equal-width or equal frequency partitioning of the data. If there are $r$ such split points, then the worst case time complexity becomes $O\left(n \cdot r^{2}\right)$. The results presented in Section 7 are based on $r=5$ candidate split points found by equal frequency partitioning of the data.

# 6. Parameter Estimation by Least Squares 

We have now presented a maximum likelihood framework for learning univariate MTE potentials from data. In order to compare the merits of this new learning algorithm with a baseline method, we will proceed by describing the hitherto most used method for learning MTEs from data (Rumí et al., 2006; Romero et al., 2006). This technique is commonly denoted least squares (LS) estimation because it looks for parameter values that minimize the mean squared error between the fitted model and the empirical density of the sample. In early work on MTE parameter estimation (Rumí et al., 2006), the empirical density was estimated using a histogram. In order to avoid the lack of smoothness, especially when data is scarce, Romero et al. (2006) proposed to use kernels to approximate the empirical density instead of histograms, and this is also the approach we will follow here.

As the LS method does not directly seek to maximize the likelihood of the model, the resulting LS parameters are not guaranteed to be close to the ML parameters. This difference was confirmed by our preliminary experiments, and has resulted in a few modifications to the LS method presented by Romero et al. (2006): i) Instead of using Gaussian kernels, we used Epanechnikov kernels, which tended to provide better ML estimates in our preliminary experiments. ii) Since the smooth kernel density estimate assigns positive probability mass, $p^{*}$, outside the truncated region (called the boundary bias by Simonoff (1996)), we truncate and reweight the kernel density with $1 /\left(1-p^{*}\right)$. iii) In order to reduce the effect of low probability areas during the least squares calculations, the summands in the mean squared error are weighted according to the empirical density at the corresponding points.

Assume that there are $n_{m}$ points in the original sample, $\mathbf{x}$, that fall inside $\Omega_{m}$. Without loss of generality, in order to simplify the notation, we will assume within this section that all the elements of sample $\mathbf{x}$ belong to $\Omega_{m}$. In what follows we denote by $\mathbf{y}=\left(y_{1}, \ldots, y_{n_{m}}\right)^{\mathrm{v}}$ the values of the empirical kernel for sample $\mathbf{x}=\left(x_{1}, \ldots, x_{n_{m}}\right)^{\mathrm{v}}$, and with reference to the target density in Equation (4), we assume initial estimates for $a_{0}, b_{0}$ and $k_{0}$ (we will later discuss how to get these initial estimates). With this outset, $c$ and $d$ can be estimated by minimizing the weighted mean squared error between the function $c \exp \{d \mathbf{x}\}$ and the points $(\mathbf{x}, \mathbf{w})$, where $\mathbf{w}=\mathbf{y}-a_{0} \exp \left\{b_{0} \mathbf{x}\right\}-k_{0}$. Specifically, by taking logarithms, the problem reduces to linear regression:

$$
\ln \{\mathbf{w}\}=\ln \{c \exp \{d \mathbf{x}\}\}=\ln \{c\}+d \mathbf{x}
$$

which can be written as $\mathbf{w}^{*}=c^{*}+d \mathbf{x}$; here $c^{*}=\ln \{c\}$ and $\mathbf{w}^{*}=\ln \{\mathbf{w}\}$. Note that we here assume that $c>0$. In fact the data $(\mathbf{x}, \mathbf{w})$ is transformed, if necessary, to fit this constraint, i.e., to be convex and positive. This is achieved by changing the sign of the values $\mathbf{w}$ and then adding a constant to make them positive. We then fit the parameters taking into account that afterwards the sign of $c$ should be changed and the constant used to make the values positive should be subtracted.

A solution to the regression problem is then defined by

$$
\left(c^{*}, d\right)=\arg \min _{c^{*}, d}\left(\mathbf{w}^{*}-c^{*}-d \mathbf{x}\right)^{\mathrm{T}} \operatorname{diag}(\mathbf{y})\left(\mathbf{w}^{*}-c^{*}-d \mathbf{x}\right)
$$

where $\operatorname{diag}(\cdot)$ takes a vector as input and returns a diagonal matrix with that vector on its diagonal.

The solution can be described analytically:

$$
\begin{aligned}
c^{*} & =\frac{\mathbf{w}^{\mathrm{T}} \operatorname{diag}(\mathbf{y}) \mathbf{x}-d \cdot\left(\mathbf{x}^{\mathrm{T}} \mathbf{y}\right)^{2}}{\mathbf{x}^{\mathrm{T}} \mathbf{y}} \\
d & =\frac{\left(\mathbf{w}^{\mathrm{T}} \mathbf{y}\right)\left(\mathbf{x}^{\mathrm{T}} \mathbf{y}\right)-\left(\sum_{i} y_{i}\right)\left(\mathbf{w}^{\mathrm{T}} \operatorname{diag}(\mathbf{y}) \mathbf{x}\right)}{\left(\mathbf{x}^{\mathrm{T}} \mathbf{y}\right)^{2}-\left(\sum_{i} y_{i}\right) \cdot \mathbf{x}^{\mathrm{T}} \operatorname{diag}(\mathbf{y}) \mathbf{x}}
\end{aligned}
$$

Once $a, b, c$ and $d$ are known, we can estimate $k$ in $f^{*}(x)=k+a e^{b x}+c e^{d x}$. If we let $\mathbf{s}=\mathbf{y}-a e^{b \mathbf{x}}-c e^{d \mathbf{x}}-k$, we have that $k \in \mathbb{R}$ should be the value minimizing the error

$$
\operatorname{Error}(k)=\frac{1}{n_{m}} \mathbf{s}^{\mathrm{T}} \operatorname{diag}(\mathbf{y}) \mathbf{s}
$$

This is achieved for

$$
\hat{k}=\frac{\left(\mathbf{y}-a e^{b \mathbf{x}}-c e^{d \mathbf{x}}\right)^{\mathrm{T}} \mathbf{y}}{\sum_{i} y_{i}}
$$

Here we are assuming a fixed number of exponential terms. However, as the parameters are not optimized globally, there is no guarantee that the fitted model minimizes the weighted mean squared error. This fact can be somewhat corrected by determining the contribution of each term to the reduction of the error as described by Rumí et al. (2006).

The initial values $a_{0}, b_{0}$ and $k_{0}$ can be arbitrary, but "good" values can speed up convergence. We consider two alternatives: $i$ ) Initialize the values by fitting a curve $a e^{b x}$ to the modified sample by exponential regression, and compute $k$ as before. ii) Force the empiric density and the initial model to have the same derivative. In the current implementation, we try both initializations and choose the one that minimizes the squared error.

# 7. Experimental Comparison 

In order to evaluate the proposed learning algorithm we have sampled datasets from six distributions: An MTE density defined by two regions, a beta distribution $\operatorname{Beta}(0.5,0.5)$, a standard normal distribution, a $\chi^{2}$ distribution with eight degrees of freedom, and a log-normal distribution $L N(0,1)$. From each distribution we sampled two different training sets having sizes 1000 and 50 , respectively. This last dataset is devoted to show the performance of the different methods when data is scarce. In order to check the predictive ability of the estimated models, a test set of size 1000 was also sampled.


Table 1: Comparison of ML vs. LS in terms of likelihood. In the upper table the split points were found using the method described in (Rumí et al., 2006), and in the lower table they were defined by the extreme points and the inflexion points of the exact density.


Table 2: Comparison of ML vs. LS in terms of the test set likelihood. In the upper table the split points were found using the method described in (Rumí et al., 2006), and in the lower table they were defined by the extreme points and the inflexion points of the exact density.

Our first group of tests consider learning of MTEs assuming that the domain has already been divided into intervals, and that the number of exponential terms has been fixed to 2 . When testing with data from the MTE, beta and normal distributions, we have used one split point, whereas for the log-normal and the $\chi^{2}$ distributions, the number of split points was set to three. We have also run the experiment with three split points for the standard normal distribution. We have used two methods for finding split points: $i$ ) Define the split points to be the extreme points and inflection points of the true generating density function, and $i i$ ) use the procedure described by Rumí et al. (2006). The plots of the fitted models using the training set of size 1000 together with the original density are displayed in Figure 3. The split points used for these plots were selected using the second approach above; results using the former approach for detecting split points are qualitatively similar.

Turning to the quantitative results, Table 1 shows the likelihood of the different samples for the models fitted with the 1000 size training set using the direct ML approach, the modified LS method, and the original LS method described in Rumí et al. (2006). The two sub-tables correspond to the split points found using the method described in Rumí et al. (2006) and split points found by identifying the extreme points and the inflexion points of the true density, respectively. Table 2 shows the likelihood of the test set for the same models,

![img-3.jpeg](img-3.jpeg)

Figure 3: The plots show the results of samples from different distributions. The gold-standard distribution is drawn with a thick line, the MTE with Lagrange-parameters are given with the dashed line, and the results of the LS approach are given with the thin, solid line.


Table 3: Comparison of ML vs. LS estimated with a sample of size 50 in terms of the test set likelihood. In the upper table the split points were found using the method described in (Ruml et al., 2006), and in the lower table they were defined by the extreme points and the inflexion points of the exact density.
and Table 3 shows the likelihood of the test set for the models fitted with the 50 size training set. From the results we clearly see that the ML-based method outperforms the LS method in terms of likelihood. This is hardly a surprise, as the ML method is actively using likelihood maximization as its target, whereas the LS methods do not. On the other hand, the LS and Original LS seem to be working at comparable levels. Most commonly (in 15 out of 24 runs), LS is an improvement over its original version with large training sets, but with small training sets it behaves much worse. The explanation is that the weights used in the new version of LS are not so accurate, and so the estimations are unstable. We can also see from Table 3 that the ML approach appears to overfit the data, and therefore achieves a lower testset likelihood than the original LS for the "Normal 3 splits" and "Log-normal" datasets. This is not surprising, as the number of parameters used by the ML approach to fit the distributions are far above what turns out to be "BIC-optimal" (see below).

Our last set of tests focused on the BIC-based model selection algorithm for finding split points and determining the number of parameters inside each interval; for these tests we allowed at most two exponential terms and five candidate split points (found using equal-frequency binning). The results, given in Table 4, clearly show the desired effect: The BIC-based method is less prone to overfitting the data, and although a smaller likelihood is obtained on the training data, the predictive ability of the data is better than when learning with fixed split points. Plots of the learned MTEs are shown in Figure 4, where it is interesting to note how the BIC-based learning algorithm chooses different model structures for the different data-sizes. Look, for instance, at the Beta distribution in Part (b) of Figure 4. When only 50 training examples are used, we fit a function with two exponential terms to the whole support of the density (no split points are selected); when 1000 cases are available, the learning prefers to use two intervals. Furthermore, for the first interval of the MTE distribution (Part (a)), the learning based on 1000 cases finds support for using one exponential term to approximate the density. When learning from 50 cases, the algorithm did not get the same support, and therefore opted for


Table 4: The results of the BIC-based learning approach. In the upper table the results are based on learning from 50 data-points, the lower table reports the results based on 1000 training examples.
a constant in that part of the domain. Finally, it is interesting to see that the log-normal (Part (e)) is approximated using 0 split points (when learning from 50 cases) or 1 split point (when learning from 1000 cases). This should be compared to the 3 split points used to generate the results in Figure 3 (f).

# 8. Conclusions and Future Work 

In this paper we have introduced maximum likelihood learning of MTEs. Finding maximum likelihood parameter estimates is interesting not only in its own right, but also as a tool for doing more advanced learning, like model selection. We have proposed algorithms that use the BIC criteria (Schwarz, 1978) to choose the number of exponential terms required to approximate the density function properly, as well as for determining the location of the splitpoints for partitioning the domain of the variables. The experiments carried out show that the estimations obtained by ML improve the ones provided by the least squares method both in terms of likelihood of the training data and of the predictive ability (measured by likelihood of a separate test-set).

We are currently working on ML-based learning of conditional distributions, starting from the ideas published in (Moral et al., 2003). However, accurately locating the split-points for a conditional MTE is even more difficult than when learning marginal distributions; locating the split-points for a variable will not only influence the approximation of its distribution, but also the distributions for all its children.

## Acknowledgments

This work has been partly supported by the Spanish Ministry of Science and Innovation through project TIN2007-67418-C03-02 and by EFRD (FEDER) funds.
