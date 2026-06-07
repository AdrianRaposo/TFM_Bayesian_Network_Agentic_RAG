# Model averaging for sparse seemingly unrelated regression using Bayesian networks among the errors 

Abdul Salam ${ }^{1,2} \cdot$ Marco Grzegorczyk ${ }^{1}$ (D)


#### Abstract

: 12 November 2021 / Accepted: 21 June 2022 / Published online: 19 July 2022 (c) The Author(s) 2022


#### Abstract

Multivariate Bayesian linear regression (MBLR) is a popular statistical tool with many applications in a variety of scientific fields. However, a shortcoming is potential model over-complexity, as the model assumes that all responses depend on the same covariates and that all errors are mutually pairwise correlated. The class of Bayesian seemingly unrelated regression (SUR) models generalizes the class of MBLR models by allowing for response-specific covariate sets. In a recent work it has been proposed to employ Gaussian graphical models for learning sparse SUR (SSUR) models with conditional independencies among the errors. The proposed SSUR model infers undirected edges among the errors, and the proposed Reversible Jump Markov Chain Monte Carlo (RJMCMC) inference algorithm relies on approximations of the marginal likelihoods. In this paper, we propose a new refined SSUR model that replaces the undirected graphs (Gaussian graphical models) by directed acyclic graphs (Gaussian Bayesian networks). Unlike the earlier proposed model, our new model is therefore able to learn some directed edges among the errors. And we derive a RJMCMC algorithm that does not require approximations of the marginal likelihoods. In particular, we present an algorithm for sampling covariance matrices that are coherent with a given directed acyclic graph. The proposed RJMCMC algorithm allows for exact Bayesian model averaging across both: the response-specific covariate sets and the directed acyclic graphs.


Keywords Multivariate Bayesian linear regression $\cdot$ Seemingly unrelated regression $\cdot$ Gaussian Bayesian networks $\cdot$ Exact Bayesian model averaging

[^0]
[^0]:    $\boxtimes$ Marco Grzegorczyk
    m.a.grzegorczyk@rug.nl

    1 Bernoulli Institute, Groningen University, Groningen, The Netherlands
    2 Department of Statistics, University of Malakand, Chakdara, Pakistan

# 1 Introduction 

Multivariate Bayesian linear regression (MBLR) is an important statistical tool for modelling the relationship between covariates $z_{1}, \ldots, z_{N}$ and a continuous multivariate response vector $\mathbf{y}=\left(y_{1}, \ldots, y_{S}\right)^{\mathrm{T}}$. The idea is to impose a univariate linear regression model for each element $y_{s}$ of $\mathbf{y}$ and to infer the covariance matrix among the response-specific errors $e_{1}, \ldots, e_{S}$. Because of the correlated errors, there is information-sharing among the univariate models. MBLR was proposed by Tiao and Zellner (1964); Geisser (1965) and detailed descriptions can be found in many textbooks, e.g. in Sect. 2.8.5 of Rossi et al. (2005). Recent applications range from the earth (Arroyo and Ordaz 2010) and climate (Seidou et al. 2007) sciences over geophysics (Talarico et al. 2017) to quality control (Ahmadi Yazdi et al. 2019). In other works it was proposed to exchange the inverse Wishart prior of the covariance matrix by other priors, such as a multivariate Gaussian prior for the unique elements of the matrix logarithm of the covariance matrix (Sinay and Hsu 2014), or a non-informative Jeffrey's prior (Saputro et al. 2018). In some scientific fields MBLR appears as vector auto regressive (VAR) model. VAR models are popular tools for modelling multivariate time series and they are effectively a special case of MBLR models, where the observations $\mathbf{y}_{t} \in \mathbb{R}^{S}$ at the current time point $t$ are the responses and the observations $\mathbf{y}_{t-1}, \ldots, \mathbf{y}_{t-\tau} \in \mathbb{R}^{S}$ at the previous time points are the $N=S \cdot \tau$ covariates. Applications of VAR models be found in econometrics (Banbura et al. 2010), in the behavioural sciences (Beltz and Molenaar 2016) and in neuroimaging (Chiang et al. 2017). The above works use 'full models' that feature all $N \cdot S$ possible covariate-response interactions. To compensate for the over-complexity, Bayesian parameter shrinkage is applied, but shrinkage priors are often inferior to Bayesian model averaging (BMA), see, e.g., Hoeting et al. (1999); Wasserman (2000); Fragoso et al. (2018). Seemingly unrelated regression (SUR) models (Zellner 1962; Zellner and Huang 1962) avoid the over-complexity of MBLR by allowing for response-specific covariate sets. But unlike for MBLR models, the inference for SUR models is challenging and ranges from Reversible Jump MCMC (RJMCMC) techniques (Green 1995) for sampling response-specific covariate sets (Holmes et al. 2002) to direct Monte Carlo approaches for sampling the model parameters (Zellner and Ando 2010). A promising sparse SUR (SSUR) model has been proposed by Wang (2010). The SSUR model from Wang imposes a spike-and-slab prior on the regression coefficients and uses Gaussian graphical models (Lauritzen 1996) to model conditional independencies among the errors. A disadvantage of the SSUR model is that the marginal likelihoods that are required for the RJMCMC inference algorithm in the model space (covariate sets and undirected graphs) cannot be computed analytically, so that the algorithm has to rely on marginal likelihood approximations. Wang proposes to use Chib's method (Chib 1995) to approximate the marginal likelihoods by MCMC techniques. This leads to inflated computational costs, since every RJMCMC step in the model space requires separate MCMC simulations for approximating the model-specific marginal likelihoods. The intention of our work is to improve the SSUR model from Wang (2010) in three important respects:

(i) We do not use a spike-and-slab prior for the regression coefficients. Instead we apply Bayesian model averaging (Holmes et al. 2002) and sample responsespecific covariate sets from the posterior distribution.
(ii) For modelling the conditional independencies among the errors we replace the undirected graphs (Gaussian graphical models) by directed acyclic graphs (Gaussian Bayesian networks). Unlike the earlier proposed SSUR model, our model can therefore learn a mixture of directed and undirected edges among the errors; cf. Sect. 2.5 for more details.
(iii) Third, for the new model we derive a RJMCMC algorithm that does not need marginal likelihood approximations. We reach this by combining Bayesian model averaging (BMA) across the response-specific covariate sets along the lines of Raftery et al. (1997); Holmes et al. (2002) with BMA across all possible error Bayesian networks (directed acyclic graphs) along the lines of Giudici and Castelo (2003). We show that the therefore required marginal likelihoods and full conditional distributions have analytic solutions. An important methodological contribution of our work is that we show how to sample covariance matrices that are coherent with a given directed acyclic graph (DAG); cf. Sect. 2.4.2.

The remainder of this paper is organised as follows. Section 2 is on the mathematical background. We briefly review the traditional MBLR in Sect. 2.1 and the SUR model in Sect. 2.2. In Sect. 2.3 we present the new sparse SUR (SSUR) model, and Sect. 2.4 is devoted to the prior distributions and the proposed RJMCMC sampling scheme. Sections 2.5 and 2.6 are on Bayesian model averaging and predictive probabilities, respectively. In Sect. 2.7 we distinguish 6 model variants that we crosscompare in our empirical studies. Section 3 provides technical and implementation details. The synthetic and the three real-world data sets, on which we cross-compare the model variants, are described in Sect. 4. In Sect. 5 we perform the cross-method comparison, before we conclude with a discussion in Sect. 6.

# 2 Theory 

### 2.1 Traditional multivariate Bayesian linear regression

The traditional multivariate Bayesian linear regression (MBLR) model (Tiao and Zellner 1964; Geisser 1965) assumes a set of $S$ regression models that are related by common covariates and correlated errors. There are $S$ regression equations

$$
y_{s}=\mathbf{x}^{\mathrm{T}} \boldsymbol{\beta}_{s}+e_{s} \quad(s=1, \ldots, S)
$$

where $y_{s}$ is the $s$-th response, $\mathbf{x} \in \mathbb{R}^{N}$ is the shared vector of covariate values, and $\boldsymbol{\beta}_{s} \in \mathbb{R}^{N}$ and $e_{s}$ are $s$-th regression (coefficient) vector and error, respectively. An $S$-dimensional Gaussian distribution with zero mean vector $\mathbf{0} \in \mathbb{R}^{S}$ and covariance matrix $\boldsymbol{\Sigma} \in \mathbb{R}^{S, S}$ is assumed for the error vector:

$$
\mathbf{e}:=\left(e_{1}, \ldots, e_{S}\right)^{\top} \sim \mathcal{N}_{S}(\mathbf{0}, \Sigma)
$$

Given observations, $\left\{y_{1, t}, \ldots, y_{S, t}, \mathbf{x}_{t}\right\}_{t=1, \ldots, T}$, one can compactly write

$$
\mathbf{y}_{t}:=\left(y_{1, t}, \ldots, y_{S, t}\right)^{\top} \sim \mathcal{N}_{S}\left(\mathbf{B}^{\top} \mathbf{x}_{t}, \boldsymbol{\Sigma}\right) \quad(t=1, \ldots, T)
$$

where $\mathbf{B}:=\left(\boldsymbol{\beta}_{1}, \ldots, \boldsymbol{\beta}_{S}\right) \in \mathbb{R}^{N, S}$ is the matrix of regression coefficients, $y_{s, t}$ is the $t$-th value of response $y_{s}$, and $\mathbf{x}_{t} \in \mathbb{R}^{N}$ is the covariate vector of observation $t$. By using a matrix-variate Gaussian distribution, Eq. (3) can be written as:

$$
\mathbf{Y}=\mathbf{X B}+\mathbf{E}, \text { where } \mathbf{X}:=\left(\begin{array}{c}
\mathbf{x}_{1}^{\top} \\
\vdots \\
\mathbf{x}_{T}^{\top}
\end{array}\right) \in \mathbb{R}^{T, N} \quad \text { and } \quad \mathbf{Y}:=\left(\begin{array}{c}
\mathbf{y}_{1}^{\top} \\
\vdots \\
\mathbf{y}_{T}^{\top}
\end{array}\right) \in \mathbb{R}^{T, S}
$$

The random matrix $\mathbf{E} \in \mathbb{R}^{T, S}$, whose elements are the errors $e_{t, s}:=y_{t, s}-\mathbf{x}_{t}^{\top} \boldsymbol{\beta}_{s}$, has a matrix-variate Gaussian distribution

$$
\mathbf{E} \sim \mathcal{N}_{T, S}(\mathbf{0}, \mathbf{I}, \boldsymbol{\Sigma}) \Leftrightarrow \operatorname{vec}(\mathbf{E}) \sim \mathcal{N}_{T \cdot S}(\operatorname{vec}(\mathbf{0}), \boldsymbol{\Sigma} \otimes \mathbf{I})
$$

where $\mathbf{0}$ is a zero matrix, $\mathbf{I}$ is the identity matrix, vec (.) is the vectorisation operator that stacks the columns, and $\otimes$ is the Kronecker product. For each row $\mathbf{e}_{t}^{\top}:=\left(e_{1, t}, \ldots, e_{S, t}\right)$ of $\mathbf{E}$ we then have $\mathbf{e}_{t} \sim \mathcal{N}_{S}(\mathbf{0}, \boldsymbol{\Sigma})$. For $\boldsymbol{\Sigma}$ an inverse Wishart distribution with positive definite scale matrix $\mathbf{V} \in \mathbb{R}^{S, S}$ and $\alpha>S+1$ degrees of freedom is used, $\Sigma \sim \mathcal{W}_{S}^{-1}(\mathbf{V}, \alpha)$. Given $\Sigma$, a matrix-variate Gaussian prior is used for B :

$$
\begin{aligned}
\mathbf{B} & \sim \mathcal{N}_{N, S}\left(\mathbf{B}_{0}, \Delta_{0}^{-1}, \boldsymbol{\Sigma}\right) \\
\Leftrightarrow \operatorname{vec}(\mathbf{B}) & \sim \mathcal{N}_{N \cdot S}\left(\operatorname{vec}\left(\mathbf{B}_{0}\right), \boldsymbol{\Sigma} \otimes \Delta_{0}^{-1}\right)
\end{aligned}
$$

where the expectation matrix $\mathbf{B}_{0} \in \mathbb{R}^{N, S}$ and the 'scale' matrix $\Delta_{0}^{-1} \in \mathbb{R}^{N, N}$ are hyperparameters. Sampling from the posterior distribution, $p(\boldsymbol{\Sigma}, \mathbf{B} \mid \mathbf{Y})$, is computationally convenient, since the fully conjugate prior allows $p(\boldsymbol{\Sigma} \mid \mathbf{Y})$ to be computed in closed form, so that $\boldsymbol{\Sigma}$ can be sampled by a collapsed Gibbs sampling step (marginalised over $\mathbf{B}$ ), before $\mathbf{B}$ is sampled from its full conditional distribution $p(\mathbf{B} \mid \boldsymbol{\Sigma}, \mathbf{Y})$. For the analytic closed form solutions of this Gibbs sampling scheme we refer to Sect. 2.8.5 in Rossi et al. (2005).

# 2.2 Seemingly unrelated regression (SUR) modelling 

Allowing for response-specific covariate sets, $\pi_{1}, \ldots, \pi_{S} \subset\left\{z_{1}, \ldots, z_{N}\right\}$, yields the so called 'seemingly unrelated regression' (SUR) model from Zellner (1962) and Zellner and Huang (1962), in which Eq. (1) becomes:

$$
y_{s}=\mathbf{x}_{s}^{\top} \boldsymbol{\beta}_{s}+e_{s} \quad(s=1, \ldots, S)
$$

where $\mathbf{x}_{s} \in \mathbb{R}^{k_{s}}$ contains the values of the covariates in $\pi_{s}$, and $\boldsymbol{\beta}_{s} \in \mathbb{R}^{k_{s}}$. One then gets in replacement of Eq. (3):

$$
\begin{gathered}
\mathbf{y}_{t}:=\left(y_{1, t}, \ldots, y_{S, t}\right)^{\top} \sim \mathcal{N}_{S}\left(\mathbf{X}_{t} \boldsymbol{\beta}, \boldsymbol{\Sigma}\right) \\
\text { where } \boldsymbol{\beta}:=\left(\boldsymbol{\beta}_{1}^{\top}, \ldots, \boldsymbol{\beta}_{S}^{\top}\right)^{\top} \in \mathbb{R}^{k}
\end{gathered}
$$

staples the vectors $\boldsymbol{\beta}_{s} \in \mathbb{R}^{k_{s}}$, so that $k:=\sum_{s=1}^{S} k_{s}$, and

$$
\mathbf{X}_{t}=\left(\begin{array}{llll}
\mathbf{x}_{t, 1}^{\top} & & & \\
& \mathbf{x}_{t, 2}^{\top} & & \mathbf{0} \\
& & \mathbf{x}_{t, 3}^{\top} & & \\
& \mathbf{0} & & \ddots & \\
& & & & \mathbf{x}_{t, S}^{\top}
\end{array}\right) \in \mathbb{R}^{S, k}
$$

$\mathbf{x}_{t, s} \in \mathbb{R}^{k_{s}}$ contains the values of the covariates in $\pi_{s}$ from observation $t$. Optionally, we can extend each $\mathbf{x}_{t, s}$ by an initial ' 1 ' element for the intercept. For $\boldsymbol{\beta}_{s} \in \mathbb{R}^{k_{s}}$ we thus either have $k_{s}=\left|\pi_{s}\right|$ (without intercept) or $k_{s}=\left|\pi_{s}\right|+1$ (with intercept).

# 2.3 The refined sparse SUR (SSUR) model 

We identify the $S$ response-specific covariate sets, $\pi_{1}, \ldots, \pi_{S} \subset\left\{z_{1}, \ldots, z_{N}\right\}$, with an $N$-by- $S$ 'covariate matrix' $\mathcal{D}$. The elements of $\mathcal{D}$ indicate all covariate-response interactions: if $z_{i} \in \pi_{s}$ we set $\mathcal{D}_{i, s}=1$, and for $z_{i} \notin \pi_{s}$ we set $\mathcal{D}_{i, s}=0$. Moreover, we use Gaussian Bayesian networks (Geiger and Heckerman 2002; Kuipers et al. 2014) to model the conditional independencies among the errors. Let $\mathcal{G}$ denote the $S$-by- $S$ adjacency matrix of a directed acyclic graph (DAG) among $e_{1}, \ldots, e_{S}$. There is a directed edge $e_{i} \rightarrow e_{j}$ if $\mathcal{G}_{i, j}=1$ and there is no edge from $e_{i}$ to $e_{j}$ if $\mathcal{G}_{i, j}=0$. We define $\tau_{j}$ as the parent set of $e_{j}$, so that $e_{i} \in \tau_{j} \Leftrightarrow \mathcal{G}_{i, j}=1$. We refer to $\mathcal{G}$ as 'error DAG'. Given $\mathcal{G}$, the joint distribution of the errors can be factorised into univariate conditional distributions:

$$
p(\mathbf{e} \mid \mathcal{G})=p\left(e_{1}, \ldots, e_{S} \mid \mathcal{G}\right)=\prod_{s=1}^{S} p\left(e_{s} \mid \tau_{s}\right)=\prod_{s=1}^{S} \frac{p\left(e_{s}, \tau_{s}\right)}{p\left(\tau_{s}\right)}
$$

Each model $\mathcal{M}$ thus consists of two components: the $S$-by- $S$ error DAG $\mathcal{G}$ and the $N$-by- $S$ covariate matrix $\mathcal{D}$. We write $\mathcal{M}=(\mathcal{G}, \mathcal{D})$. While $\mathcal{G}$ has to be a DAG, there is no restriction on $\mathcal{D}$. The model parameters are the covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$ and the regression vector $\boldsymbol{\beta}_{\mathcal{D}}$, where the subscripts indicate that the parameters must be coherent with $\mathcal{G}$ and $\mathcal{D}$, respectively. For a given model $\mathcal{M}=(\mathcal{G}, \mathcal{D})$, we can rewrite Eq. (8) as:

$$
\mathbf{y}_{t} \mid\left(\boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right) \sim \mathcal{N}_{S}\left(\mathbf{X}_{t} \boldsymbol{\beta}_{\mathcal{D}}, \boldsymbol{\Sigma}_{\mathcal{G}}\right)
$$

Given data $\mathbf{Y}=\left\{\mathbf{y}_{t}, \mathbf{z}_{t}\right\}_{t=1, \ldots, T}$, where $\mathbf{z}_{t}$ is the vector of the $N$ covariate values in observation $t$, our goal is to posterior sample models $\mathcal{M}=(\mathcal{G}, \mathcal{D})$ along with their parameters $\left(\boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right)$.

Given $\mathcal{M}=(\mathcal{G}, \mathcal{D})$, the likelihood, $p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right)$, is the product over $T$ observations

$$
p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right)=\prod_{t=1}^{T} p\left(\mathbf{y}_{t} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right)
$$

where $p\left(\mathbf{y}_{t} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right)$ denotes the density of the $\mathcal{N}_{S}\left(\mathbf{X}_{t} \boldsymbol{\beta}_{\mathcal{D}}, \boldsymbol{\Sigma}_{\mathcal{G}}\right)$ distribution.

# 2.4 Conjugate priors and RJMCMC inference 

For the posterior density of the models $\mathcal{M}=(\mathcal{G}, \mathcal{D})$ we have:

$$
p(\mathcal{G}, \mathcal{D} \mid \mathbf{Y}) \propto p(\mathbf{Y} \mid \mathcal{G}, \mathcal{D}) p(\mathcal{G}) p(\mathcal{D})
$$

where $p(\mathbf{Y} \mid \mathcal{G}, \mathcal{D})$ is the marginal likelihood (marginalised over $\boldsymbol{\Sigma}_{\mathcal{G}}$ and $\boldsymbol{\beta}_{\mathcal{D}}$ ), and $p(\mathcal{G})$ and $p(\mathcal{D})$ are the prior probabilities of $\mathcal{G}$ and $\mathcal{D}$, respectively. As there is no analytic solution for the marginal likelihood (double integral):

$$
p(\mathbf{Y} \mid \mathcal{G}, \mathcal{D})=\iint p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right) p\left(\boldsymbol{\Sigma}_{\mathcal{G}}\right) p\left(\boldsymbol{\beta}_{\mathcal{D}}\right) d \boldsymbol{\Sigma}_{\mathcal{G}} d \boldsymbol{\beta}_{\mathcal{D}}
$$

Eq. (12) does not allow for exact posterior inference. However, when imposing conjugate priors on $\boldsymbol{\beta}_{\mathcal{D}}$ and $\boldsymbol{\Sigma}_{\mathcal{G}}$, we can compute the marginal likelihoods (single integrals):

$$
\begin{aligned}
p\left(\mathbf{Y} \mid \mathcal{G}, \boldsymbol{\beta}_{\mathcal{D}}\right) & =\int p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right) p\left(\boldsymbol{\Sigma}_{\mathcal{G}}\right) d \boldsymbol{\Sigma}_{\mathcal{G}} \\
p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}\right) & =\int p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right) p\left(\boldsymbol{\beta}_{\mathcal{D}}\right) d \boldsymbol{\beta}_{\mathcal{D}}
\end{aligned}
$$

and we show how to sample from the full conditional distributions:

$$
p\left(\boldsymbol{\beta}_{\mathcal{D}} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}, \mathbf{Y}\right) \text { and } p\left(\boldsymbol{\Sigma}_{\mathcal{G}} \mid \mathcal{G}, \boldsymbol{\beta}_{\mathcal{D}}, \mathbf{Y}\right)
$$

While sampling from $p\left(\boldsymbol{\beta}_{\mathcal{D}} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}, \mathbf{Y}\right)$ is conceptually easy, sampling a covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$ that is coherent with a given $\mathrm{DAG} \mathcal{G}$ is challenging. Since to the best of our knowledge no algorithm has been described in the literature yet, we build on results from Geiger and Heckerman (2002) and derive an algorithm for sampling from $p\left(\boldsymbol{\Sigma}_{\mathcal{G}} \mid \mathcal{G}, \boldsymbol{\beta}_{\mathcal{D}}, \mathbf{Y}\right)$; please see Sect. 2.4.2 for the details.

We use the four 'ingredients' to design a Reversible Jump Markov Chain Monte Carlo (RJMCMC) algorithm for exact posterior inference. From a given state $\left(\mathcal{G}^{*}, \mathcal{D}^{*}, \boldsymbol{\Sigma}_{\mathcal{G}^{*}}^{*}, \boldsymbol{\beta}_{\mathcal{D}^{*}}^{*}\right)$ we move in four steps to a new state $\left(\mathcal{G}^{\star}, \mathcal{D}^{\star}, \boldsymbol{\Sigma}_{\mathcal{G}^{\star}}^{\star}, \boldsymbol{\beta}_{\mathcal{D}^{\star}}^{\star}\right)$.

1. Given $\mathcal{D}^{*}$ with parameters $\boldsymbol{\beta}_{\mathcal{D}^{*}}^{*}$, we use the marginal likelihood $p\left(\mathbf{Y} \mid \mathcal{G}, \boldsymbol{\beta}_{\mathcal{D}^{*}}^{*}\right)$ and a Metropolis-Hastings step to sample a new $\mathrm{DAG} \mathcal{G}^{\star}$; see Sect. 2.4.1.
2. Given $\mathcal{G}^{\star}$ and $\mathcal{D}^{*}$ with parameters $\boldsymbol{\beta}_{\mathcal{D}^{*}}^{*}$, we sample new parameters $\boldsymbol{\Sigma}_{\mathcal{G}}^{\star}$, for $\mathcal{G}^{\star}$ from the full conditional $p\left(\boldsymbol{\Sigma}_{\mathcal{G}^{\star}} \mid, \mathcal{G}^{\star}, \boldsymbol{\beta}_{\mathcal{D}^{*}}^{*}, \mathbf{Y}\right)$; see Sect. 2.4.2.

3. Given $\mathcal{G}^{\star}$ with parameters $\boldsymbol{\Sigma}_{\mathcal{G}^{\star}}^{\star}$, we use the marginal likelihood $p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}^{\star}}^{\star}, \mathcal{D}\right)$ and a Metropolis-Hastings step to sample a new covariate matrix $\mathcal{D}^{\star}$; see Sect. 2.4.3.
4. Given $\mathcal{D}^{\star}$ and $\mathcal{G}^{\star}$ with parameters $\boldsymbol{\Sigma}_{\mathcal{G}^{\star}}^{\star}$, we sample new parameters $\boldsymbol{\beta}_{\mathcal{D}^{\star}}^{\star}$ from the full conditional $p\left(\boldsymbol{\beta}_{\mathcal{D}^{\star}} \mid \boldsymbol{\Sigma}_{\mathcal{G}^{\star}}^{\star}, \mathcal{D}^{\star}, \mathbf{Y}\right)$; see Sect. 2.4.4.

# 2.4.1 Metropolis Hastings step for the error DAG 

Given the covariate matrix $\mathcal{D}$ with regression vector $\boldsymbol{\beta}_{\mathcal{D}}$, we build the design matrices $\mathbf{X}_{t} \in \mathbb{R}^{S, k}$ with Eq. (10), and we define the error vectors $\mathbf{e}_{t}:=\mathbf{y}_{t}-\mathbf{X}_{t} \boldsymbol{\beta}_{\mathcal{D}}$. From Eq. (8) it then follows:

$$
\mathbf{e}_{t} \sim \mathcal{N}_{S}(\mathbf{0}, \Sigma) \quad(t=1, \ldots, T)
$$

In terms of the precision matrix, $\mathbf{W}:=\boldsymbol{\Sigma}^{-1}$, we then have the error likelihood (see Supplement S1):

$$
p(\mathbf{E} \mid \mathbf{W})=(2 \pi)^{-\frac{k T}{2}} \cdot \operatorname{det}(\mathbf{W})^{\frac{T}{2}} \cdot \exp \left(-\frac{1}{2} \operatorname{tr}(\mathbf{S W})\right)
$$

where $\mathbf{E}:=\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{T}\right\}$, and $\mathbf{S}:=\sum_{t=1}^{T} \mathbf{e}_{t} \cdot \mathbf{e}_{t}^{\top}$. On the precision matrix $\mathbf{W}$ we impose the Wishart prior, $\mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha)$, with scale matrix $\mathbf{V}$ and $\alpha>S+1$ degrees of freedom. ${ }^{1}$ In Supplement S1 we show that this implies for the errors the marginal likelihood:

$$
p(\mathbf{E})=\pi^{-\frac{k T}{2}} \cdot \frac{\Gamma_{S}\left(\frac{\alpha+T}{2}\right)}{\Gamma_{S}\left(\frac{\alpha}{2}\right)} \cdot \operatorname{det}\left(\mathbf{V}^{-1}\right)^{\frac{\alpha}{2}} \cdot \operatorname{det}\left(\mathbf{V}^{-1}+\mathbf{S}\right)^{-\frac{\alpha+T}{2}}
$$

where $\Gamma_{q}(a):=\pi^{q(q-1) / 4} \cdot \prod_{j=1}^{q} \Gamma\left(a+\frac{1-j}{2}\right)$ is the multivariate Gamma function. If we compute the marginal likelihood for only an $l$-dimensional subset $L \subset\left\{e_{1}, \ldots, e_{S}\right\}$ of the errors, symbolically $\mathbf{E}^{L}$, we get (Geiger and Heckerman 2002; Kuipers et al. 2014):

$$
\begin{aligned}
p\left(\mathbf{E}^{L}\right)= & \pi^{-\frac{l T}{2}} \cdot \frac{\Gamma_{l}\left(\frac{\alpha-S+l+T}{2}\right)}{\Gamma_{l}\left(\frac{\alpha-S+l}{2}\right)} \cdot \operatorname{det}\left(\mathbf{V}_{L, L}^{-1}\right)^{\frac{\alpha-S+l}{2}} \\
& \cdot \operatorname{det}\left(\mathbf{V}_{L, L}^{-1}+\mathbf{S}_{L, L}\right)^{-\frac{\alpha-S+l+T}{2}}
\end{aligned}
$$

where $\mathbf{V}_{L, L}$ and $\mathbf{S}_{L, L}$ are submatrices of $\mathbf{V}$ and $\mathbf{S}$ that keep only the rows and columns that belong to $L$.

[^0]
[^0]:    ${ }^{1}$ Geiger and Heckerman (2002) show that only this Wishart prior, $\mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha)$, leads to 'score equivalence' in Gaussian Bayesian networks. 'Score equivalence' is required in Bayesian networks, as it ensures that equivalent DAGs, i.e. DAGs that impose the same conditional independencies among the nodes (errors), have the same marginal likelihood value; cf. Eq. (18).

The error DAG $\mathcal{G}$ imposes conditional independence relations among the errors $e_{1}, \ldots, e_{S}$. Therefore, conditional on $\mathcal{G}$, the covariance matrix $\boldsymbol{\Sigma}$ is enforced to be consistent with those relations, symbolically $\boldsymbol{\Sigma}=\boldsymbol{\Sigma}_{\mathcal{G}}$. We need the equivalence relation (cf. Eq. 11):

$$
\mathbf{e} \sim \mathcal{N}_{S}\left(\mathbf{0}, \boldsymbol{\Sigma}_{\mathcal{G}}\right) \Leftrightarrow p(\mathbf{e})=\prod_{s=1}^{S} p\left(e_{s} \mid \mathbf{e}_{\tau_{s}},\left\{\boldsymbol{\Sigma}_{\mathcal{G}}\right\rangle_{\left\{e_{s}, \tau_{s}\right\},\left\{e_{s}, \tau_{s}\right\}}\right)
$$

where $\tau_{s}$ is the parent set of $e_{s}$ in $\mathcal{G}$, and $\mathbf{e}_{\tau_{s}}$ and $\left\{\boldsymbol{\Sigma}_{\mathcal{G}}\right\}_{L_{s}, L_{s}}$ are the subvector and submatrix that keep only the elements that belong to $\tau_{s}$ and $L_{s}:=\left\{e_{s}, \tau_{s}\right\}^{2}$

With the BGe score (Geiger and Heckerman 1994, 2002; Kuipers et al. 2014) the marginal likelihood of any error DAG $\mathcal{G}$ can be computed:

$$
p(\mathbf{E} \mid \mathcal{G})=\prod_{s=1}^{S} p\left(\mathbf{E}^{\left\{e_{s} \mid \tau_{s}\right\}}\right)=\prod_{s=1}^{S} \frac{p\left(\mathbf{E}^{\left\{e_{s}, \tau_{s}\right\}}\right)}{p\left(\mathbf{E}^{\left\{\tau_{s}\right\}}\right)}
$$

where $\tau_{s}$ is the parent set of $e_{s}$ in $\mathcal{G}$, and the marginal likelihoods $p\left(\mathbf{E}^{\left\{e_{s}, \tau_{s}\right\}}\right)$ and $p\left(\mathbf{E}^{\left\{\tau_{s}\right\}}\right)$ of $L_{1}:=\left\{e_{s}, \tau_{s}\right\}$ and $L_{2}:=\left\{\tau_{s}\right\}$ can be computed with Eq. (16). Recalling that we defined $\mathbf{e}_{t}:=\mathbf{y}_{t}-\mathbf{X}_{t} \boldsymbol{\beta}_{\mathcal{D}}$, we have

$$
p\left(\mathbf{Y} \mid \mathcal{G}, \boldsymbol{\beta}_{\mathcal{D}}\right)=p(\mathbf{E} \mid \mathcal{G})
$$

Hence, given any covariate matrix $\mathcal{D}$ with regression vector $\boldsymbol{\beta}_{\mathcal{D}}$, the marginal likelihood $p\left(\mathbf{Y} \mid \mathcal{G}, \boldsymbol{\beta}_{\mathcal{D}}\right)$ of any error DAG $\mathcal{G}$ can be computed analytically. ${ }^{3}$

For sampling error DAGs, we use the 'structure MCMC' Metropolis-Hastings (MH) sampling scheme from Madigan and York (1995), which we implement using the algorithms from Giudici and Castelo (2003). Let $N(\mathcal{G})$ denote the 'neighbourhood' of $\mathcal{G}$, i.e. the set of all DAGs that can be reached from $\mathcal{G}$ by adding, deleting or reversing one single edge. Given the current error DAG $\mathcal{G}$, we propose to move to a randomly selected neighbour $\mathcal{G}^{\star} \in N(\mathcal{G})$. The acceptance probability for the move is:

$$
A\left(\mathcal{G}, \mathcal{G}^{\star}\right)=\min \left\{1, \frac{p\left(\mathbf{Y} \mid \mathcal{G}^{\star}, \boldsymbol{\beta}_{\mathcal{D}}\right)}{p\left(\mathbf{Y} \mid \mathcal{G}, \boldsymbol{\beta}_{\mathcal{D}}\right)} \cdot \frac{p\left(\mathcal{G}^{\star}\right)}{p(\mathcal{G})} \cdot \operatorname{HR}\left(\mathcal{G}, \mathcal{G}^{\star}\right)\right\}
$$

where the Hastings ratio is $\operatorname{HR}\left(\mathcal{G}, \mathcal{G}^{\star}\right)=\frac{|N(\mathcal{G})|}{\left|N\left(\mathcal{G}^{\star}\right)\right|}$ with 1.1 denoting the cardinality. If the move is accepted, we exchange $\mathcal{G}$ by $\mathcal{G}^{\star}$, otherwise we keep $\mathcal{G}$ unchanged.

# 2.4.2 Sampling covariance matrices for error DAGs 

Given the error DAG $\mathcal{G}$, we need to posterior sample a covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$ that is coherent with $\mathcal{G}$; cf. Eq. (17). To this end, we first specify the prior distribution of

[^0]
[^0]:    ${ }^{2}$ The conditional Gaussian of $e_{s} \mid \tau_{s}$ can be computed from $\mathbf{e}_{\tau_{s}}$ and $\left\{\boldsymbol{\Sigma}_{\mathcal{G}}\right\rangle_{\left\{e_{s}, \tau_{s}\right\},\left\{e_{s}, \tau_{s}\right\}}$.
    ${ }^{3}$ BGe stands for Bayesian metric for Gaussian networks having score equivalence. Geiger and Heckerman (2002) show that only the Wishart prior, $\mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha)$, yields 'score equivalence' in Eq. (18), i.e.: $p\left(\mathbf{E} \mid \mathcal{G}_{1}\right)=p\left(\mathbf{E} \mid \mathcal{G}_{2}\right)$ for equivalent DAGs $\mathcal{G}_{1}$ and $\mathcal{G}_{2}$.

$\Sigma_{\mathcal{G}}$, where $\mathcal{G}$ can be any valid DAG. We follow Geiger and Heckerman (2002) and exploit that a Wishart prior for the 'unrestricted' precision matrix $\mathbf{W}:=\Sigma^{-1}$ of a 'full' DAG $\mathcal{G}^{F}$, i.e. a DAG $\mathcal{G}^{F}$ that does not impose any pairwise independencies, also implies a prior distribution for every precision matrix $\mathbf{W}_{\mathcal{G}}$ that is coherent with a given DAG $\mathcal{G}$. Inverting $\mathbf{W}_{\mathcal{G}}$ then yields $\boldsymbol{\Sigma}_{\mathcal{G}}$. Consider the Wishart prior for $\mathcal{G}^{F}$, $\mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha)$, let $L \subset\left\{e_{1}, \ldots, e_{S}\right\}$ be an $l$-dimensional error subset, and let $\mathbf{W}_{L, L}$ denote the submatrix of $\mathbf{W}$ that keeps only the rows and columns that belong to $L$. Theorem 5.1.4 in Press (1972) implies

$$
\mathbf{W}_{L, L} \sim \mathcal{W}_{l}\left(\mathbf{V}_{L, L}, \alpha-S+l\right)
$$

As the DAG $\mathcal{G}$ implies the factorization (conditional independence relations) given in Eq. (11), we can assign as prior probability for $\mathbf{W}_{\mathcal{G}} \mid \mathcal{G}$

$$
p\left(\mathbf{W}_{\mathcal{G}} \mid \mathcal{G}\right)=\prod_{s=1}^{S} p\left(\mathbf{W}_{\left\{e_{s}, \tau_{s}\right\},\left\{e_{s}, \tau_{s}\right\}} \mid \mathbf{W}_{\tau_{s}, \tau_{s}}\right)=\prod_{s=1}^{S} \frac{p\left(\mathbf{W}_{\left\{e_{s}, \tau_{s}\right\},\left\{e_{s}, \tau_{s}\right\}}\right)}{p\left(\mathbf{W}_{\tau_{s}, \tau_{s}}\right)}
$$

where $\tau_{s}$ is the $\left|\tau_{s}\right|$ dimensional parent node set of $e_{s}$ implied by $\mathcal{G}$, and $L_{s}:=\left\{e_{s}, \tau_{s}\right\}$ is an $l_{s}=\left|\tau_{s}\right|+1$ dimensional subset of errors, so that the densities on the right hand side are marginal Wishart densities; cf. Eq. (20).

On the other hand, it is not straightforward to sample a precision matrix, $\mathbf{W}_{\mathcal{G}}$, which is coherent with a given DAG $\mathcal{G}$; cf. Eqs. (17) and (21). The Wishart distribution of the 'unrestricted' precision matrix, $\mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha)$, implies the conditional distributions $\mathbf{W}_{\left\{e_{s}, \tau_{s}\right\},\left\{e_{s}, \tau_{s}\right\}} \mid \mathbf{W}_{\tau_{s}, \tau_{s}}$, but the difficulty arises from the fact that these conditionals are not of a standard form, so that it cannot be sampled from them. To the best of our knowledge, in the literature no sampling algorithm has been proposed yet. ${ }^{4}$ We propose the following algorithm, which exploits that any 'unrestricted' precision matrix $\mathbf{W}$ implies a unique precision matrix $\mathbf{W}_{\mathcal{G}}$ for any DAG $\mathcal{G}$ (Geiger and Heckerman 2002). Therefore, given any DAG $\mathcal{G}$, we first sample an 'unrestricted' precision matrix $\mathbf{W}$, before our algorithm extracts the coherent precision matrix $\mathbf{W}_{\mathcal{G}}$ from $\mathbf{W}$. Inversion of $\mathbf{W}_{\mathcal{G}}$ yields the covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$. Our algorithm consists of three consecutive steps. (1) Sample an 'unrestricted' precision matrix, $\mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha)$. Inverting $\mathbf{W}$ yields the 'unrestricted' covariance matrix $\boldsymbol{\Sigma}$. (2) For a full DAG $\mathcal{G}^{F}$ the error vector would have the multivariate Gaussian distribution, $\mathbf{e} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma})$, but the DAG $\mathcal{G}$ implies the factorization (conditional independencies) given in Eq. (17). That is, $\mathcal{G}$ implies that error $e_{s}$ is only allowed to depend on its parent nodes in $\tau_{s}$. Standard rules (see Supplement S2) allow us to compute the univariate conditional Gaussians appearing in Eq. (17):

$$
e_{s}\left\{\left(\mathbf{e}_{\tau_{s}},\left\{\boldsymbol{\Sigma}_{\mathcal{G}}\right\}_{\left\{e_{s}, \tau_{s}\right\},\left\{e_{s}, \tau_{s}\right\}}\right) \sim \mathcal{N}\left(\mu_{e_{s} \mid \tau_{s}}, \sigma_{e_{s} \mid \tau_{s}}^{2}\right) \quad(s=1, \ldots, S)\right.
$$

with conditional mean and conditional variance

[^0]
[^0]:    ${ }^{4}$ Gaussian Bayesian network inference is based on the marginal likelihoods, $p(\mathbf{E} \mid \mathcal{G})$, from Eq. (18) but does not require sampling covariance matrices, $\boldsymbol{\Sigma}_{\mathcal{G}}$, that are coherent with $\mathcal{G}$.

$$
\begin{aligned}
& \mu_{e_{s} \mid \tau_{s}}:=\boldsymbol{\Sigma}_{e_{s}, \tau_{s}}\left\{\boldsymbol{\Sigma}_{\tau_{s}, \tau_{s}}\right\}^{-1} \mathbf{e}_{\tau_{s}} \\
& \sigma_{e_{s} \mid \tau_{s}}^{2}:=\boldsymbol{\Sigma}_{e_{s}, e_{s}}-\boldsymbol{\Sigma}_{e_{s}, \tau_{s}}\left\{\boldsymbol{\Sigma}_{\tau_{s}, \tau_{s}}\right\}^{-1} \boldsymbol{\Sigma}_{\tau_{s}, e_{s}}
\end{aligned}
$$

where all submatrices and subvectors consist of only those rows and columns that belong to the elements in the subscripts. The $\left|\tau_{s}\right|$ elements of the row vector

$$
\boldsymbol{\beta}_{e_{s} \mid \tau_{s}}:=\boldsymbol{\Sigma}_{e_{s}, \tau_{s}}\left\{\boldsymbol{\Sigma}_{\tau_{s}, \tau_{s}}\right\}^{-1}
$$

are often referred to as as (partial) regression coefficients. (3) To extract the precision matrix $\mathbf{W}_{\mathcal{G}}$ which is coherent with the DAG $\mathcal{G}$, we apply the recursion from Shachter and Kenley (1989). The recursion (see Supplement S3) allows us to compute $\mathbf{W}_{\mathcal{G}}$ from $\sigma_{e_{s} \mid \tau_{s}}^{2}$ and $\boldsymbol{\beta}_{e_{s} \mid \tau_{s}}(s=1, \ldots, S)$. The key idea is to recompose the univariate conditional Gaussians from Eq. (22), which were computed from $\boldsymbol{\Sigma}=\mathbf{W}^{-1}$, back into a joint Gaussian, $\mathbf{e} \sim \mathcal{N}\left(\mathbf{0}, \mathbf{W}_{\mathcal{G}}^{-1}\right)$. By construction only the conditional dependencies captured in Eq. (22) are brought into $\mathbf{W}_{\mathcal{G}}$ while all other conditional dependencies (present in $\mathbf{W}$ but not coherent with $\mathcal{G}$ ) are omitted from $\mathbf{W}_{\mathcal{G}}$. In Supplement S4 we give a more comprehensive description of this third step.

The proposed algorithm can also be used for generating posterior samples of covariance matrices $\boldsymbol{\Sigma}_{\mathcal{G}}$ that are coherent with a DAG $\mathcal{G}$. For a given covariate matrix $\mathcal{D}$ with regression vector $\boldsymbol{\beta}_{\mathcal{D}}$, we defined: $\mathbf{e}_{t}:=\mathbf{y}_{t}-\mathbf{X}_{t} \boldsymbol{\beta}_{\mathcal{D}}$ and $\mathbf{E}:=\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{T}\right\}$. In Supplement S5 we show that the Gaussian likelihood from Eq. (14) in combination with the Wishart prior, $\mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha)$, implies for the 'unrestricted' precision matrix the posterior distribution:

$$
\mathbf{W}\left|\mathbf{E} \sim \mathcal{W}_{S}\left(\left(\mathbf{S}+\mathbf{V}^{-1}\right)^{-1}, \alpha+T\right) \quad \text { where } \mathbf{S}:=\sum_{t=1}^{T} \mathbf{e}_{t} \cdot \mathbf{e}_{t}^{\top}\right.
$$

Henceforth, for posterior sampling $\boldsymbol{\Sigma}_{\mathcal{G}}$, we replace in step (1) the Wishart prior, $\mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha)$, by the Wishart posterior, $\mathbf{W}\left|\mathbf{E} \sim \mathcal{W}_{S}\left(\left(\mathbf{S}+\mathbf{V}^{-1}\right)^{-1}, \alpha+T\right)\right.$.

# 2.4.3 Metropolis-Hastings step for the covariate matrix 

Given the error $\operatorname{DAG} \mathcal{G}$ with covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$ and the covariate matrix $\mathcal{D}$, we have:

$$
\mathbf{y}_{t} \mid\left(\boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right) \sim \mathcal{N}_{S}\left(\mathbf{X}_{t} \boldsymbol{\beta}_{\mathcal{D}}, \boldsymbol{\Sigma}_{\mathcal{G}}\right) \quad(t=1, \ldots, T)
$$

where the block design matrices $\mathbf{X}_{t} \in \mathbb{R}^{S, k}$ depend on the covariate matrix $\mathcal{D}$ and have the form of Eq. (10), and $\boldsymbol{\beta}_{\mathcal{D}} \in \mathbb{R}^{k}$ has the form of Eq. (9) and consists of $S$ stapled regression vectors. With the definitions:

$$
\mathbf{y}:=\left(\mathbf{y}_{1}^{\top}, \ldots, \mathbf{y}_{T}^{\top}\right)^{\top} \in \mathbb{R}^{T \cdot S}
$$

$$
\mathbf{X}:=\left(\mathbf{X}_{1}^{\top}, \ldots, \mathbf{X}_{T}^{\top}\right)^{\top} \in \mathbb{R}^{T \cdot S, k}
$$

we can compactly write:

$$
\mathbf{y} \mid\left(\boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right) \sim \mathcal{N}_{T \cdot S}\left(\mathbf{X} \boldsymbol{\beta}_{\mathcal{D}}, \mathbf{I} \otimes \boldsymbol{\Sigma}_{\mathcal{G}}\right)
$$

On $\boldsymbol{\beta}_{\mathcal{D}}$ we impose a Gaussian prior, $\boldsymbol{\beta}_{\mathcal{D}} \sim \mathcal{N}_{k}\left(\boldsymbol{\mu}_{0}, \boldsymbol{\Sigma}_{0}\right)$, where $\boldsymbol{\mu}_{0} \in \mathbb{R}^{k}$ and $\boldsymbol{\Sigma}_{0} \in \mathbb{R}^{k, k}$ are hyperparameters. A rule for Gaussian integrals (see Supplement S6) implies the marginal likelihood (marginalised over $\boldsymbol{\beta}_{\mathcal{D}}$ ):

$$
\mathbf{y} \mid\left(\boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}\right) \sim \mathcal{N}_{T \cdot S}\left(\mathbf{X} \boldsymbol{\mu}_{0}, \mathbf{I} \otimes \boldsymbol{\Sigma}_{\mathcal{G}}+\mathbf{X} \boldsymbol{\Sigma}_{0} \mathbf{X}^{\top}\right)
$$

For computing the density $p\left(\mathbf{y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}\right)$ we require the inverse and the determinant of:

$$
\tilde{\boldsymbol{\Sigma}}:=\mathbf{I} \otimes \boldsymbol{\Sigma}_{\mathcal{G}}+\mathbf{X} \boldsymbol{\Sigma}_{0} \mathbf{X}^{\top}
$$

In Supplement S8 we show how the matrix inversion lemma and the matrix determinant lemma (see Supplement S7) can be applied to compute the density in Eq. (28) more efficiently. Hence, given the error $\mathrm{DAG} \mathcal{G}$ with covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$, the marginal likelihood $p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}\right)$ of each covariate matrix $\mathcal{D}$ can be computed in closed form.

For sampling covariate matrices, we apply a Metropolis-Hastings (MH) move. We randomly select one of the elements of $\mathcal{D}$, say $\mathcal{D}_{n, s}$, and we propose to flip its value $1 \leftrightarrow 0$. That is, we propose either to add $z_{n}$ to the covariate set $\pi_{s}$ (if $\mathcal{D}_{s, n}=0$ ) or to remove $z_{n}$ from $\pi_{s}$ (if $\mathcal{D}_{s, n}=1$ ). This yields a new candidate covariate matrix $\mathcal{D}^{\star}$, and the acceptance probability is:

$$
A\left(\mathcal{D}, \mathcal{D}^{\star}\right)=\min \left\{1, \frac{p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}^{\star}\right)}{p\left(\mathbf{Y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}\right)} \cdot \frac{p\left(\mathcal{D}^{\star}\right)}{p(\mathcal{D})} \cdot \mathrm{HR}\right\}
$$

The move design ensures that forward and backward move are equally likely so that the Hastings ratio HR is equal to 1 . If the move is accepted, we exchange $\mathcal{D}$ by $\mathcal{D}^{\star}$, or otherwise we keep $\mathcal{D}$ unchanged.

# 2.4.4 Sampling regression vectors 

Given the error $\mathrm{DAG} \mathcal{G}$ with covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$ and the covariate matrix $\mathcal{D}$, we have for the full conditional:

$$
p\left(\boldsymbol{\beta}_{\mathcal{D}} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}, \mathbf{y}\right) \propto p\left(\mathbf{y} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right) \cdot p\left(\boldsymbol{\beta}_{\mathcal{D}}\right)
$$

In Supplement S9 we show that:

$$
\begin{aligned}
\mathbf{y} \mid\left(\boldsymbol{\Sigma}_{\mathcal{G}}, \boldsymbol{\beta}_{\mathcal{D}}\right) & \sim \mathcal{N}_{T \cdot S}\left(\mathbf{X} \boldsymbol{\beta}_{\mathcal{D}}, \mathbf{I} \otimes \boldsymbol{\Sigma}_{\mathcal{G}}\right) \\
\boldsymbol{\beta}_{\mathcal{D}} & \sim \mathcal{N}_{k}\left(\boldsymbol{\mu}_{0}, \boldsymbol{\Sigma}_{0}\right)
\end{aligned}
$$

implies the full conditional distribution

$$
\begin{aligned}
& \boldsymbol{\beta}_{\mathcal{D}} \mid\left(\boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}, \mathbf{y}\right) \sim \mathcal{N}_{k}\left(\boldsymbol{\mu}^{\star}, \boldsymbol{\Sigma}^{\star}\right), \text { where } \\
& \boldsymbol{\Sigma}^{\star}:=\left(\boldsymbol{\Sigma}_{0}^{-1}+\sum_{t=1}^{T} \mathbf{X}_{t}^{\top} \boldsymbol{\Sigma}_{\mathcal{G}}^{-1} \mathbf{X}_{t}\right)^{-1} \quad \text { and } \quad \boldsymbol{\mu}^{\star}:=\boldsymbol{\Sigma}^{\star}\left(\sum_{t=1}^{T} \mathbf{X}_{t}^{\top} \boldsymbol{\Sigma}_{\mathcal{G}}^{-1} \mathbf{y}_{t}+\boldsymbol{\Sigma}_{0}^{-1} \boldsymbol{\mu}_{0}\right)
\end{aligned}
$$

Hence, given the error $\mathrm{DAG} \mathcal{G}$ with covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$ and the covariate matrix $\mathcal{D}$, we can Gibbs-sample $\boldsymbol{\beta}_{\mathcal{D}}$ from its full conditional distribution $p\left(\boldsymbol{\beta}_{\mathcal{D}} \mid \boldsymbol{\Sigma}_{\mathcal{G}}, \mathcal{D}, \mathbf{y}\right)$.

# 2.5 Bayesian model averaging and equivalence classes of DAGs 

The RJMCMC algorithm from Sect. 2.4 generates a posterior sample

$$
\left(\mathcal{G}^{(r)}, \mathcal{D}^{(r)}, \boldsymbol{\Sigma}_{\mathcal{G}^{(r)}}^{(r)}, \boldsymbol{\beta}_{\mathcal{D}^{(r)}}^{(r)}\right)_{r=1, \ldots, R}
$$

Given the sample, marginal posterior probabilities, such as the probability $p_{i, j}^{\dagger}$ that covariate $z_{i}$ has an effect on response $y_{j}$, or the probability $p_{i, j}^{\ddagger}$ that there is an edge from error $e_{i}$ to error $e_{j}$, can be estimated. We refer to these probabilities as covari-ate-response $\left(p_{i, j}^{\dagger} \in[0,1]\right)$ and error-error $\left(p_{i, j}^{\ddagger} \in[0,1]\right)$ interaction scores. For the covariate-response interactions we compute the mean scores:

$$
\bar{p}_{i, j}^{\dagger}=\frac{1}{R} \sum_{r=1}^{R} \mathcal{D}_{i, j}^{(r)} \text { and variances } V_{i, j}^{\dagger}=\frac{1}{R-1} \sum_{r=1}^{R}\left(\mathcal{D}_{i, j}^{(r)}-\bar{p}_{i, j}^{\dagger}\right)^{2}
$$

For the error-error interactions we have to take into account that DAGs fall into equivalence classes. Each equivalence class contains the DAGs that encode the same conditional independence relations (Chickering 1995). In Chickering (2002) it has been shown that each equivalence class of DAGs can be represented by a 'completed partially directed acyclic graph' (CPDAG). Loosely speaking, the CPDAG replaces some of the directed edges of the DAG by undirected edges, so as to indicate that their directions are not unique within its equivalence class. ${ }^{5}$ A directed edge in a CPDAG indicates that all DAGs within the equivalence class agree on this edge direction. That means that the inferred conditional independence relations require the edge to have this particular direction. Henceforth, the edge has been learned along with its direction. On the other hand, an undirected edge in a CPDAG indicates that the DAGs within the equivalence class disagree on the direction of this edge, so that the edge direction is not unique and stays unclear. When computing marginal edge posterior probabilities, we interpret undirected CPDAG edges as bidirectional edges $e_{i} \leftrightarrow e_{j}$. With this interpretation we translate each $\mathrm{DAG} \mathcal{G}^{(r)}$ into a graph $\mathcal{G}^{(r), \ddagger}$, whose element $\mathcal{G}_{i, j}^{(r), \ddagger}$ is 1 if the CPDAG of $\mathcal{G}^{(r)}$ contains either the directed edge $e_{i} \rightarrow e_{j}$ or an undirected edge $e_{i}-e_{j}$, which we interpret as $e_{i} \leftrightarrow e_{j}$. For the error-error interactions we compute the mean scores:

[^0]
[^0]:    ${ }^{5}$ The edge between $e_{i}$ and $e_{j}$ is undirected in the CPDAG if and only if the equivalence class contains DAGs that have the edge $e_{i} \rightarrow e_{j}$ as well as DAGs that have the edge $e_{i} \leftarrow e_{j}$.

$$
\bar{p}_{i, j}^{ \xi}=\frac{1}{R} \sum_{r=1}^{R} \mathcal{G}_{i, j}^{(r), \xi} \quad \text { and variances } \quad V_{i, j}^{\xi}=\frac{1}{R-1} \sum_{r=1}^{R}\left(\mathcal{G}_{i, j}^{(r), \xi}-\bar{p}_{i, j}^{\xi}\right)^{2}
$$

Since MCMC samples can be strongly auto-correlated, we note that the effective sample size (ESS) can be substantially lower than $R$; see Sect. 2.9 for details on how to estimate interaction-specific ESSs. For each interaction $i \rightarrow j$ we have an effective sample size $\mathrm{ESS}_{i, j}$ and a marginal existence probability, $p_{i, j}$, which we estimate by the mean $\bar{p}_{i, j}$. When the MCMC generated Bernoulli sample of size $R$ is of effective size $\mathrm{ESS}_{i, j}$, asymptotic $1-\alpha$ confidence intervals for $p_{i, j}$ are:

$$
\bar{p}_{i, j} \pm q_{1-\alpha / 2} \cdot \sqrt{\frac{\bar{p}_{i, j}\left(1-\bar{p}_{i, j}\right)}{\operatorname{ESS}_{i, j}}}
$$

where $q_{1-\alpha / 2}$ is the $(1-\alpha / 2)$ quantile of the $\mathcal{N}(0,1)$ distribution.

# 2.6 Predictive probabilities 

Given a validation data set $\overline{\mathbf{Y}}$ with $\bar{T}$ observations, $\overline{\mathbf{Y}}=\left\{\overline{\mathbf{y}}_{t}, \overline{\mathbf{z}}_{t}\right\}_{t=1, \ldots, \bar{T}}$, where $\overline{\mathbf{z}}_{t}$ contains the values of the covariates in observation $t$, we can Monte-Carlo approximate the predictive probability:

$$
\hat{p}(\overline{\mathbf{Y}} \mid \mathbf{Y})=\frac{1}{R} \sum_{r=1}^{R} \prod_{t=1}^{\bar{T}} p\left(\overline{\mathbf{y}}_{t} \mid \overline{\mathbf{X}}_{t, \mathcal{D}^{(r)}} \boldsymbol{\beta}_{\mathcal{D}^{(r)}}^{(r)}, \boldsymbol{\Sigma}_{\mathcal{G}^{(r)}}^{(r)}\right)
$$

where $\overline{\mathbf{X}}_{t, \mathcal{D}^{(r)}}$ is a block design matrix (cf. Eq. 10), built from the covariates values in $\overline{\mathbf{z}}_{t}$ using the covariate sets implied by $\mathcal{D}^{(r)}$, and $p(\mathbf{y} \mid \boldsymbol{\mu}, \Sigma)$ denotes the density of the $\mathcal{N}_{S}(\boldsymbol{\mu}, \Sigma)$ distribution.

### 2.7 Model variants and their scores

The proposed SSUR model adds two features to the traditional MBLR model. It infers response-specific covariate sets, and it infers a Bayesian network among the errors. The traditional MBLR is akin to the new model with the DAG being enforced to be a 'full' DAG, $\mathcal{G}^{F}$, and the covariate matrix being enforced to be a matrix full of 1's $\left(\mathcal{D}^{F}:=\mathbf{1}_{N, S}\right)$. A full DAG $\mathcal{G}^{F}$ has maximal number of edges (e.g. $\mathcal{G}_{i, j}^{F}=1$ for all $i<j$ ), so that the errors are mutually pairwise dependent. A full covariate matrix $\mathcal{D}^{F}$ implies that all responses depend on all covariates. As the two model refinements can be implemented separately, we can build two 'in-between' models, each featuring only one of the two refinements. In total, we have four model variants:

- The model $\mathcal{M}_{0,0}$ enforces a full DAG, $\mathcal{G}^{F}$, and a full covariate matrix, $\mathcal{D}^{F}$, and only samples the model parameters $\left(\Sigma_{\mathcal{G}^{F}}^{(r)}, \boldsymbol{\beta}_{\mathcal{D}^{F}}^{(r)}\right)$. We refer to $\mathcal{M}_{0,0}$ as 'baseline' model, since it is akin to the traditional MBLR.

- The model $\mathcal{M}_{1,0}$ enforces a full covariate matrix $\mathcal{D}^{F}$, and only samples error DAGs $\mathcal{G}^{(r)}$ along with parameters of the form $\left(\boldsymbol{\Sigma}_{\mathcal{G}^{(r)}}^{(r)}, \boldsymbol{\beta}_{\mathcal{D}^{F}}^{(r)}\right)$.
- The model $\mathcal{M}_{0,1}$ enforces a full error DAG $\mathcal{G}^{F}$, and only samples covariate matri$\operatorname{ces} \mathcal{D}^{(r)}$ along with parameters of the form $\left(\boldsymbol{\Sigma}_{\mathcal{G}^{F}}^{(r)}, \boldsymbol{\beta}_{\mathcal{D}^{(r)}}^{(r)}\right)$.
- $\mathcal{M}_{1,1}$ is the newly proposed model. It samples error DAGs $\mathcal{G}^{(r)}$ and covariate matrices $\mathcal{D}^{(r)}$ along with their parameters $\left(\boldsymbol{\Sigma}_{\mathcal{G}^{(r)}}^{(r)}, \boldsymbol{\beta}_{\mathcal{D}^{(r)}}^{(r)}\right)$.

We also consider two model variants that correspond to static $\left(\mathcal{M}_{S}\right)$ and dynamic $\left(\mathcal{M}_{D}\right)$ Bayesian networks.

- The model $\mathcal{M}_{S}$ does not allow for covariate-response $\left(z_{i} \rightarrow y_{j}\right)$ interactions, so that the covariate matrix $\mathcal{D}$ is enforced to be a zero matrix. The model is akin to a static Bayesian model that only infers the error interactions $\left(e_{i} \rightarrow e_{j}\right)$ in form of DAGs $\mathcal{G}$. Then, the design matrices contain only the intercepts.
- The model $\mathcal{M}_{D}$ does not allow for error interactions $\left(e_{i} \rightarrow e_{j}\right)$, so that the error DAG $\mathcal{G}$ is enforced to be a graph without any edges. The model only learns the covariate-response interactions $\left(z_{i} \rightarrow y_{j}\right)$. The error covariance matrix is a diagonal matrix, whose diagonal entries are the $S$ error variances. For vector auto regressive (VAR) modelling approaches, where the current observations of a time series take the role of responses and past observations become the covariates, the model is thus akin to a dynamic Bayesian network model; cf. Sects. 4.2 and 4.3.

Our major goal is to show that the new $\mathcal{M}_{1,1}$ model performs better than the traditional/baseline $\mathcal{M}_{0,0}$ model. But we will also cross-compare with the 'in between' models $\left(\mathcal{M}_{1,0}\right.$ and $\left.\mathcal{M}_{0,1}\right)$, so as to elucidate what the individual gains of the two model refinements are. In two time series applications (mTOR and ANDRO) we also compare the $\mathcal{M}_{1,1}$ model with the static $\left(\mathcal{M}_{S}\right)$ and the dynamic $\left(\mathcal{M}_{D}\right)$ Bayesian network, so as to provide empirical evidence that simultaneously learning both types of interactions leads to improved inference results. In an additional study on synthetic data we also compare with the traditional MBLR, as described in Sect. 2.1.

Since all models generate parameter samples, we can cross-compare them in terms of predictive probabilities; cf. Eq. (30). But we have to take into account that we cannot compute interactions scores from a constantly full DAG $\mathcal{G}^{F}$ and/or from a constantly full covariate matrix $\mathcal{D}^{F}=\mathbf{1}_{N, S}$. We then replace the interaction scores by the fraction of sampled parameters that have the same sign. The $\mathcal{M}_{0,1}$ model samples regression vectors $\boldsymbol{\beta}_{\mathcal{D}^{F}}^{(r)}$ that have a specific regression coefficient $\beta_{i, j}^{(r)}$ for each possible interaction $z_{i} \rightarrow y_{j}$. We determine the fraction of positive $p_{i, j}^{*,+}$ and negative $p_{i, j}^{*,-}$regression coefficients in the sample $\beta_{i, j}^{(1)}, \ldots, \beta_{i, j}^{(R)}$, and we use $\bar{p}_{i, j}^{*}:=2 \cdot \max \left\{p_{i, j}^{*,+}, p_{i, j}^{*,-}\right\}-1$ for scoring the interaction $z_{i} \rightarrow y_{j}$. Accordingly, in the $\mathcal{M}_{1,0}$ model for each error-error interaction $e_{i} \rightarrow e_{j}$ we extract the $(i, j)$ elements from the sampled covariance matrices, $\boldsymbol{\Sigma}_{i, j}^{(1)}, \ldots, \boldsymbol{\Sigma}_{i, j}^{(R)}$, and determine the fraction of positive $p_{i, j}^{*,+}$and negative $p_{i, j}^{*,-}$elements among them. We then use: $\bar{p}_{i, j}^{*}:=2 \cdot \max \left\{p_{i, j}^{*,+}, p_{i, j}^{*,-}\right\}-1$ for scoring the error-error interaction $e_{i} \rightarrow e_{j}$.

# 2.8 Reconstruction accuracy 

The covariate-response and the error-error interaction scores defined in Sect. 2.5 and in Sect. 2.7 allow for rankings of the interactions. If the true interactions are known, the rankings can be used to define precision recall (PR) curves. For each threshold $\xi \in[0,1]$ we extract the interactions whose scores exceed $\xi$. We then compute the precision $p_{\xi}$ (fraction of true interactions among the extracted interactions, $\frac{T P}{T P+F P}$ ) and the recall $r_{\xi}$ (fraction of true interactions that have been extracted, $\frac{T P}{T P+F N}$ ). Plotting $p_{\xi}$ against $r_{\xi}$ yields the PR curve, and the area under the curve (AUC) is a measure for quantifying the accuracy of the inferred interactions (Davis and Goadrich 2006). AUC values are in between 0 and 1, and higher AUCs indicate a higher accuracy (Davis and Goadrich 2006).

### 2.9 Convergence diagnostics and effective sample sizes

Trace plot diagnostics and potential scale reduction factors (PSRFs) are widely applied tools for assessing MCMC convergence. On a given data set we perform $H$ independent MCMC simulations with $V=100,000(100 k)$ iterations each. With trace plots we monitor global characteristics, such as the number of interactions of the sampled models. To monitor convergence via PSRFs we evaluate at equidistant time points, say after $2 s \in\{10,20, \ldots, 100 k\}$ iterations, and compute the interac-tion-specific PSRFs. When withdrawing the first $s$ samples to account for a burn-in phase, we keep $s$ MCMC samples. Let $\bar{p}_{i, j}^{[h, 2 s]}$ and $V_{i, j}^{[h, 2 s]}$ denote the mean and the variance of the interaction $i \rightarrow j$ obtained from simulation $h$ computed from the last $R=s$ samples of a run with $2 s$ iterations (cf. Sect. 2.5). The 'between-chain' variance $\mathcal{B}_{2 s}(i, j)$ is the variance of the means $\bar{p}_{i, j}^{[1,2 s]}, \ldots, \bar{p}_{i, j}^{[H, 2 s]}$. The 'within-chain" variance $\mathcal{W}_{2 s}(i, j)$ is the mean of the variances $V_{i, j}^{[1,2 s]}, \ldots, V_{i, j}^{[H, 2 s]}$. Brooks and Gelman (1998) define the PSRF as

$$
\operatorname{PSRF}_{2 s}(i, j):=\frac{H+1}{H}\left(\frac{\left(1-\frac{1}{s}\right) \mathcal{W}_{2 s}(i, j)+\mathcal{B}_{2 s}(i, j)}{\mathcal{W}_{2 s}(i, j)}\right)-\frac{s-1}{s \cdot H}
$$

where $H$ is the number of MCMC simulations, $s$ is the number of taken samples after a burn-in phase of the same length $s$. PSRFs near 1 indicate that the simulations are close to the stationary distribution (Brooks and Gelman 1998), where $\xi=1.1$ has become a widely applied threshold. We use the more conservative threshold $\xi=1.05$, and as convergence diagnostic we monitor the fraction of edges $\mathcal{F}_{2 s}$ whose PSRF is lower than $\xi$ against the numbers of MCMC iterations $2 s$. Hence, $\mathcal{F}_{2 s} \in[0,1]$ is the relative frequency of edges that have a PSRF lower than 1.05 after $2 s$ iterations. For estimating the effective sample sizes (ESSs) we use the approach from Vehtari et al. (2021). For each interaction $i \rightarrow j$ the ESS is defined as:

$$
\operatorname{ESS}_{i, j}=\frac{R}{1+2 \sum_{i=1}^{\infty} \rho_{i, j}^{t}}
$$

where $R=s$ is the number of MCMC samples taken during the sampling phase and $\rho_{i, j}^{t}$ is the auto-correlation of interaction $i \rightarrow j$ at lag $t$, which can be estimated from the $H$ independent MCMC runs using the estimator (Vehtari et al. 2021)

$$
\hat{\rho}_{i, j}^{t}=1-\frac{\mathcal{W}_{2 s}(i, j)-\frac{1}{H} \sum_{h=1}^{H} V_{i, j}^{[h, 2 s]} \cdot \hat{\rho}_{i, j}^{t,[h]}}{\mathcal{W}_{2 s}(i, j) \cdot \frac{R-1}{R}+\mathcal{B}_{2 s}(i, j)}
$$

where $\hat{\rho}_{i, j}^{t,[h]}$ is the auto-correlation at lag $t$ estimated from the output of simulation $h$. To avoid that $\operatorname{ESS}_{i, j}$ is biased by noisy estimates of very large lags, we again follow Vehtari et al. (2021) and apply the truncation rule from Geyer (1992).

# 3 Simulation details 

### 3.1 Hyperparameter settings

In absence of prior knowledge, we impose uniform distributions on $\mathcal{G}$ and $\mathcal{D}$. We then have in Eq. (12):

$$
p(\mathcal{G}, \mathcal{D} \mid \mathbf{Y}) \propto p(\mathbf{Y} \mid \mathcal{G}, \mathcal{D})
$$

The model uses an inverse Wishart prior for the covariance matrix $\boldsymbol{\Sigma}$, from which it extracts the covariance matrix $\boldsymbol{\Sigma}_{\mathcal{G}}$ for any DAG $\mathcal{G}$, and it uses a Gaussian prior for the regression vector $\boldsymbol{\beta}_{\mathcal{D}}$, whose individual vectors $\boldsymbol{\beta}_{s}$ (cf. Eq. 9) always include an initial intercept parameter (see text below Eq. 10):

$$
\boldsymbol{\Sigma}^{-1}=: \mathbf{W} \sim \mathcal{W}_{S}(\mathbf{V}, \alpha) \quad \text { and } \quad \boldsymbol{\beta}_{\mathcal{D}} \sim \mathcal{N}_{k}\left(\boldsymbol{\mu}_{0}, \boldsymbol{\Sigma}_{0}\right)
$$

This implies that $\boldsymbol{\Sigma}$ is inverse Wishart distributed with scale matrix $\mathbf{V}^{-1}$ and $\alpha$ degrees of freedom, so that $E[\boldsymbol{\Sigma}]=\frac{1}{\alpha-S-1} \mathbf{V}^{-1}$. We set $\mathbf{V}^{-1}=(\alpha-S-1) \mathbf{I}$ to get $E[\boldsymbol{\Sigma}]=\mathbf{I}$. For $\alpha=S+2$ we obtain an uninformative prior (our standard choice). In Sect. 5.2.1 we make the prior stronger by setting: $\alpha=x(S+2)$ with $x=1, \ldots, 4$. We set $\boldsymbol{\mu}_{0}=\mathbf{0}$ and $\boldsymbol{\Sigma}_{0}=\lambda \mathbf{I}$ with $\lambda>0$, so that all regression coefficients $\beta_{i, s}$ (for $z_{i} \rightarrow y_{s}$ ) have independent $\mathcal{N}(0, \lambda)$ priors. The prior covariance matrix $\boldsymbol{\Sigma}$ imposes regression relationships among the errors, and the joint distribution $\mathbf{e} \sim \mathcal{N}_{S}(\mathbf{0}, \boldsymbol{\Sigma})$ can be factorised (see Supplement S4) :

$$
e_{s}\left|\left(e_{1}, \ldots, e_{s-1}\right) \sim \mathcal{N}\left(\sum_{i=1}^{s-1} \bar{\beta}_{i, s} e_{i}, v_{s}^{2}\right)\right.
$$

We define $y_{s}:=\mu_{s}+e_{s}$ with $\mu_{s}=\mathbf{x}_{s}^{\top} \boldsymbol{\beta}_{s}$, so that

$$
\left.y_{s}\right|\left(y_{1}, \ldots, y_{s-1}\right) \sim \mathcal{N}\left(\mu_{s}+\sum_{i=1}^{s-1} \bar{\beta}_{i, s}\left(y_{i}-\mu_{i}\right), v_{s}^{2}\right)
$$

For our setting $E[\Sigma]=\mathbf{I}$ the prior expectation of each $\bar{\beta}_{i, s}$ (for $e_{i} \rightarrow e_{s}$ or $y_{i} \rightarrow y_{s}$ ) is zero, and we can Monte Carlo approximate the prior variance $\operatorname{VAR}\left(\bar{\beta}_{i, s}\right)$. We sample 10,000 covariance matrices from the prior, extract the conditional Gaussians, and compute the empirical variance of each $\bar{\beta}_{i, s}$. In $\beta_{i, s} \sim \mathcal{N}(0, \lambda)$ we then set $\lambda$ equal to the mean variance, so as to ensure that the two regression coefficient types $\beta_{i, s}$ (for $z_{i} \rightarrow y_{s}$ ) and $\bar{\beta}_{i, s}$ (for $y_{i} \rightarrow y_{s}$ ) have the same (average) prior variance $\lambda$, depending on $S, \mathbf{V}$ and $\alpha$.

# 3.2 MCMC simulations and software (Matlab) implementation 

We run all RJMCMC simulations for $V=100,000(100 k)$ iterations. Setting the burn-in to $0.5 \mathrm{~V}(50 \%)$ and thinning out by a factor of 10 during the sampling phase, yields $R=5 k$ MCMC samples. In Sect. 5.1 we provide exemplary convergence diagnostics and effective sample size calculations. Measurements of the computational costs for running RJMCMC simulations with our Matlab code are provided in Table 2 of Sect. 5.3. Our Matlab (MATLAB 2020) implementation of the models from Sect. 2.7 is available as supplementary material. In script files we provide worked examples that show how to apply the models to the mTOR data from Sect. 4.2 and how to reproduce the mTOR results (cf. Sect. 5.2.2).

## 4 Data

### 4.1 Synthetic data

We generate models with $S=10$ responses and $N=20$ covariates. Since we have dependent errors in the regression equations $y_{s}=\mathbf{x}_{s}^{\top} \boldsymbol{\beta}_{s}+e_{s}$, we start with the error DAG $\mathcal{G}$. Without loss of generality, we assume the topological order $e_{1}, \ldots, e_{S}$, so that $\mathcal{G}$ can only have edges $e_{i} \rightarrow e_{s}$ with $i<s$. We randomly select 10 edges from $\left\{\mathcal{G}_{i, s}: i<s\right\}$ and for each of the 10 regression coefficients $\bar{\beta}_{i, s}$ we sample its absolute value from a uniform distribution on the interval $[1 ; 2]$, before we assign a random sign to $\bar{\beta}_{i, s}$. Among the errors we then impose relationships of the form:

$$
e_{s}=\sum_{i: \mathcal{G}_{i, s}=1} \bar{\beta}_{i, s} \cdot e_{i}+\bar{\beta}_{0, s} \cdot v_{s}
$$

where $v_{s} \sim \mathcal{N}(0,1)$ is unexplained noise and $\bar{\beta}_{0, s}=1$. To ensure that each error $e_{s}$ has a $\mathcal{N}(0,1)$ marginal distribution, we re-scale the coefficients in Eq. (32) to Euclidean norm 1. For $i \in\{0, \ldots, s-1\}$ with $\bar{\beta}_{i, s} \neq 0$ :

$$
\tilde{\beta}_{i, x} \leftarrow \frac{\tilde{\beta}_{i, x}}{\sqrt{\tilde{\beta}_{0, x}^{2}+\sum_{i: \tilde{\beta}_{i, x} \neq 0} \tilde{\beta}_{i, x}^{2}}}
$$

After re-scaling, we follow the topological order and successively sample the $e_{t, x}$ 's from Eq. (32), so as to obtain realisations $\mathbf{e}_{t}=\left(e_{t, 1}, \ldots, e_{t, N}\right)$. Subsequently, we randomly select 10 covariate-response connections $\left(z_{i} \rightarrow y_{s}\right)$ from $\mathcal{D} \in \mathbb{R}^{N, S}$. For each of the 10 regression coefficients $\beta_{i, x}$ we sample its absolute value from a uniform distribution on the interval $[0.25 ; 0.50]$, before we assign a random sign to $\beta_{i, x}$. Data points $\left(\mathbf{z}_{t}, \mathbf{y}_{t}\right)$ with $\mathbf{z}_{t}=\left(z_{t, 1}, \ldots, z_{t, N}\right)$ and $\mathbf{y}_{t}=\left(y_{t, 1}, \ldots, y_{t, S}\right)$ can be generated by sampling error values $\mathbf{e}_{t} \in \mathbb{R}^{S}$, as described above, and covariate values $\mathbf{z}_{t} \sim \mathcal{N}_{N}\left(\mathbf{0}, \Sigma^{z}\right)$. For the response values we then have:

$$
y_{t, s} \mid\left(\mathbf{z}_{t}, e_{t, s}\right)=\sum_{i: \mathcal{D}_{s, s}=1} z_{t, i} \beta_{i, s}+e_{t, s}
$$

We set $\Sigma_{i, j}^{z}=0.25+0.75 \delta_{i, j}$, where $\delta_{i, j}$ is the Kronecker delta, so that each covariate has expectation 0 , variance 1 , and the pairwise correlation is 0.25 . For our study we sample 50 different models $(\mathcal{D}, \mathcal{G})$ along with parameters, and for each model we simulate two data sets. One data set $\mathbf{Y}$ with $T=50$ observations for inference and another data set $\tilde{\mathbf{Y}}$ with $\tilde{T}=10$ observations for validation (predictive probabilities).

# 4.2 Protein signalling (mTOR) data 

The mammalian target of rapamycin complex 1 pathway (mTOR) is an important protein signalling pathway in all eukaryotic cells. The proteins activate and inactivate each other by phosphorylation, and the activity of each protein depends on which of its sites are phosphorylated. The immunoblotting data from Dalle Pezze et al. (2016) contain measurements of $S=11$ phosphorylation states of eight key proteins across the mTOR signalling network. ${ }^{6}$ After two treatments (only amino acids vs. amino acids and insulin) the phosphorylation states were measured at 10 non-equidistant time points $m_{t}[$ in min]

$$
\left(m_{1}, \ldots, m_{10}\right)=(0,1,3,5,10,15,30,45,60,120)
$$

We follow Shafiee Kamalabad et al. (2019) and zscore standardise the values of each phosphorylation site to mean 0 and variance 1. For our analyses we select a vector auto regressive (VAR) approach, which is a special case of the MBLR approach. Let $y_{m_{t}, i}$ denote the measurement for protein site $i \in\{1, \ldots, 11\}$ at time point $m_{t}$. From both experiments we build nine data points, $\left(\mathbf{y}_{t}, \mathbf{z}_{t}\right)_{t=1, \ldots, 9}$, where $\mathbf{y}_{t}=\left(y_{m_{t+1}, 1}, \ldots, y_{m_{t+1}, 11}\right)^{\top}$ and $\mathbf{z}_{t}=\left(y_{m_{t}, 1}, \ldots, y_{m_{t}, 11}\right)^{\top}$ are the measurements at time

[^0]
[^0]:    ${ }^{6}$ IR-beta (insulin receptor beta) at $p Y 1146$, IRS1 (insulin receptor substrate 1) at $p S 636$, AMPK (AMPdependent protein kinase) at $p T 172$, TSC2 (tuberous sclerosis 2 protein) at $p S 1387$, AKT(protein kinase B) at $p T 308$ and at $p S 473$, mTOR (mammalian target of rapamycin) at $p S 2448$ and at $p S 2481, \mathrm{p} 70-\mathrm{S} 6 \mathrm{~K}$ (ribosomal protein S6 kinase beta-1) at $p T 389$, PRAS40 (proline-rich AKT/PKB substrate 40 kDa ) at $p S 183$ and at $p T 246$.

points $m_{t+1}$ and $m_{t}$. By merging the data points from both experiments, we get $T=18$ data points. The model infers error-error $\left(e_{i} \rightarrow e_{j}\right)$ and covariate-response $\left(z_{i} \rightarrow y_{j}\right)$ interactions, which here correspond to static $\left(y_{i, m_{t}} \rightarrow y_{j, m_{t}}\right)$ and dynamic $\left(y_{i, m_{t}} \rightarrow y_{j, m_{t+1}}\right)$ protein interactions. We provide the mTOR data as supplementary material.

# 4.3 Andromeda (ANDRO) data 

In Hatzikos et al. (2008) water quality data of the Thermaikos Gulf of Thessaloniki (Greece) was provided. The data set contains daily under water measurements of six variables, namely: temperature, pH , conductivity, salinity, oxygen, and turbidity. The data are available from Hatzikos et al. (2008). We follow Spyromitros-Xioufis et al. (2016) and apply a vector auto regressive (VAR) approach in which the $S=6$ variables are the responses, $\mathbf{y}_{t}=\left(y_{t, 1}, \ldots, y_{t, 6}\right)^{\top} \in \mathbb{R}^{6}$, and the measurements of the same variables from 6-10 days before are the $N=30$ potential covariates, symbolically $\mathbf{z}_{t}=\left(\mathbf{y}_{t-6}^{\top}, \ldots, \mathbf{y}_{t-10}^{\top}\right)^{\top} \in \mathbb{R}^{30}$. With the time lag of up to $\Delta=10$ days, $T=49$ data points $\left(\mathbf{z}_{t}, \mathbf{y}_{t}\right)$ can be built from the data. Like for the mTOR data from Sect. 4.2, the model infers static $\left(y_{t, i} \rightarrow y_{t, j}\right)$ and dynamic interactions $\left(y_{t-\Delta, i} \rightarrow y_{t, j}\right)$, where the latter can be subject to different time lags $\Delta \in\{6, \ldots, 10\}$.

### 4.4 Occupational Employment Survey (OES) 2010

On a yearly basis, the US Bureau of Labor Statistics performs occupational employment surveys (OES) in large US cities. For each city the number of full-time equivalent employees for different job types is reported. The OES data set from 2010 are available from Spyromitros-Xioufis et al. (2016), where they were used to compare the performances of multi-target prediction algorithms. We follow SpyromitrosXioufis et al. (2016) and (i) focus only on those job types that were present in at least 50 percent of the cities and (ii) replace missing values by job type sample means. This way one obtains 403 cities (observations) and 314 job types (variables). As the counts differ in magnitudes (range from 30 to 156740), we zscore standardise the counts of each city to mean 0 and variance 1 . For our empirical studies, we generate data sets with $S=20$ job types as responses and $N=20$ other job types as covariates, and we then sample $T \in\{10,20,40,80,160,320\}$ cities as data points. For each $T$ we generate 10 data instantiations. Each time we randomly sample $S$ responses, $N$ covariates, $T$ cities, and $\hat{T}=10$ more cities for validation (predictive probabilities).

# 5 Results 

In Sect. 5.1 we provide exemplary convergence diagnostics and effective sample size calculations. In Sect. 5.2 we cross-compare the performances of the different models described in Sect. 2.7 in terms of predictive probabilities and precision-recall AUC scores. Finally, in Sect. 5.3 we investigate the scalability of the proposed RJMCMC inference algorithm and we provide measurements of the computational costs.

### 5.1 Convergence diagnostics and effective sample sizes

To assess whether $V=100 k$ MCMC iterations are sufficient to reach satisfactory convergence, we employ trace plot and potential scale reduction factor (PSRF) diagnostics. In this subsection our focus is on the mTOR data from Sect. 4.2 and the ANRO data from Sect. 4.3 to exemplify how we assessed convergence. ${ }^{7}$ With the trace plots we monitor global quantities, such as the numbers of static and dynamic interactions or the posterior scores of the sampled models. Example trace plots are provided in Supplement S10. The trace plot diagnostics in Figs. 1-2 of Supplement S10 show the same trend: Already after relatively few iterations, the trace plots of $H=10$ independent MCMC simulations run into plateaus and overlay smoothly. In Fig. 1 we monitor the fraction $\mathcal{F}_{2 x}$ of edges that meet the criterion of a PSRF lower than $\xi=1.05$, see Sect. 2.9 for the technical details. It can be seen that at the end of the burn-in phase of length $50 k(50 \%$ of $V=100 k)$ all interactions fulfill the PSRF-based convergence criterion. During the subsequent sampling phase (results not shown) the fractions stayed constantly equal to 1 . For each possible interaction $i \rightarrow j$ we also compute the individual effective sample size $\operatorname{ESS}_{i, j}$, as explained in Sect. 2.9. Figure 2 shows boxplots of the effective sample sizes (ESSs), distinguishing for both data sets (mTOR vs. ANDRO) the two interaction types (contemporaneous vs. dynamic). The boxplots display the distribution of the interaction-specific ESS values with medians being across all interactions of that type; the medians are also provided in Table 1 along with the average computing time [in seconds] for $50 k$ MCMC iterations. The efficiency sample is the ratio of ESS and computing time and refers to the number of (effective) posterior samples that are generated per second. Although the ESSs are rather small relative to the sampling phase length of $50 k$ MCMC iterations, they seem sufficiently large for reliably estimating the marginal edges scores; cf. the asymptotic confidence intervals from Sect. 2.5.

[^0]
[^0]:    ${ }^{7}$ For selected synthetic and subsampled OES data sets we performed the same convergence diagnostics and observed comparable trends.

![img-0.jpeg](img-0.jpeg)

Fig. 1 Convergence diagnostics based on potential scale reduction factors (PSRFs). For each individual interaction we computed a PSRF, and the panels show trace plots of the fractions of the edges whose PSRF was lower than the threshold 1.05 (vertical axis) monitored along the number of MCMC iterations (horizontal axis). At the end of the burn-in phase ( 50 k iterations) all PSRFs were below 1.05 and this did not change anymore during the sampling phase. The rows correspond to the mTOR (top) and to the ANDRO (bottom) data. The columns refer to the contemporaneous (left) and dynamic (right) interactions
![img-1.jpeg](img-1.jpeg)

Fig. 2 Effective sample sizes (ESSs) per data set and interaction type. Each ESS was computed from the 50 k samples that were taken during the sampling phase and averaged across $H=10$ independent MCMC simulations. Each panel refers to a data set (mTOR or ANDRO) and interaction type (contemporaneous or dynamic interactions). The boxplots display the distributions of the interaction-specific ESSs. The medians of the boxplots are provided in Table 1

Table 1 Computational time and sampling efficiency during sampling phase of length 50k


For each combination of data set and interaction type, the table shows the medians of effective sample size (ESS), computational time [in seconds] and the resulting efficiency ratio [samples per second]. The ESS medians are across the interactions shown in Fig. 2, while the computing time medians are across $H=10$ simulations, performed with our Matlab code on computers with Intel Xeon 2.5 GHz processor and 4GB of RAM

# 5.2 Method comparisons 

### 5.2.1 Synthetic data

First, we cross-compare the performances of the four models: $\mathcal{M}_{0,0}$ (baseline), $\mathcal{M}_{1,1}$ (proposed), and $\mathcal{M}_{1,0}$ and $\mathcal{M}_{0,1}$ ('in-between') on the 50 synthetically generated data sets (see Sect. 4.1). Figure 3 shows the results in terms of predictive probabilities and areas under precision recall curves (AUCs). In both criteria the proposed $\mathcal{M}_{1,1}$ model clearly outperforms the over-complex baseline model, $\mathcal{M}_{0,0}$, that employs a full error DAG and a full covariate matrix. The predictive probabilities of the $\mathcal{M}_{1,1}$ model are consistently higher than those of the $\mathcal{M}_{0,0}$ model. To gain more insight, where the improvement comes from, we compute separate AUCs for the two types of interactions (error-error and covariate-response). We see that both AUC types are significantly in favour of the $\mathcal{M}_{1,1}$ model. The average AUC improvements are 0.34 (error-error) and 0.33 (covariate-response). The AUC results for the two 'in-between' models meet our expectations. While the $\mathcal{M}_{1,0}$ model (full covariate matrix) mainly loses accuracy w.r.t. the covariate-response interactions, the $\mathcal{M}_{0,1}$ model (full error DAG) yields lower accuracies for the error-error interactions. This suggests that the two improvements are independent and that each (mainly) concerns a specific interaction type. Interestingly, a decreased accuracy in the covar-iate-response interactions also seems to result in a slightly decreased accuracy for the error-error interactions (see results of $\mathcal{M}_{1,0}$ ). In terms of predictive probabilities the $\mathcal{M}_{1,1}$ significantly outperforms all three competitors (Wilcoxon signed-rank test). However, the predictive probabilities of the $\mathcal{M}_{0,1}$ are only slightly worse and partly overlap. Apparently, with regard to the prediction accuracy the over-complexity of a full error graph $\left(\mathcal{M}_{0,1}\right)$ is less misleading than over-complex covariate sets $\left(\mathcal{M}_{1,0}\right)$. In Supplement S11 we provide more empirical results. First, we studied other hyperparameters with stronger penalties for the regression parameters. We used $\alpha \in\{24,36,48\}$ rather than $\alpha=12$ like in Fig. 3. Second, we cross-compared the performances of the $\mathcal{M}_{1,1}$ and the traditional MBLR model from Sect. 2.1. Our findings can be summarised as follows: For larger hyperparameters $\alpha$ the trends from Fig. 3 are conserved and the differences stay significant, but the relative differences get smaller as $\alpha$ increases (see Supplementary Figs. 3-5). The traditional

![img-2.jpeg](img-2.jpeg)

Fig. 3 Results for the synthetic data from Sect. 4.1. Results are averaged across data sets from 50 models with $S=10$ responses, $N=20$ covariates and $T=50$ observations. For each model we generated $\bar{T}=10$ additional observations for the predictive probabilities. The top row shows box plots of the predictive probabilities achieved with the four models $\mathcal{M}_{i, j}(i, j \in\{0,1\})$ (top left) and the relative gains of model $\mathcal{M}_{1,1}$ over the three competitors (top right). The three differences are highly significant (Wilcoxon signed-rank p-values $<1.3 \cdot 10^{-5}$ ). The bottom row shows histograms of the the areas under the precision recall curves (AUCs) and the relative gains of model $\mathcal{M}_{1,1}$ over the three competitors (bottom right). For clarity, we computed separate AUCs for the error-error ( $e_{i} \rightarrow e_{j}$, light grey) and the covariate-response ( $z_{i} \rightarrow y_{s}$, dark grey) interactions. The error bars correspond to $95 \%$ confidence intervals. In Supplement S11 we provide additional figures for the synthetic data

MBLR model performs worse than the $\mathcal{M}_{0,0}$ model, and hence clearly inferior to the $\mathcal{M}_{1,1}$ model. From the AUC histograms (see right panel of Figure 6 in Supplement S11) it can be seen that the traditional MBLR model yields a low accuracy for the error-error interactions ( $A U C \approx 0.32$ ). A possible explanation is that the traditional model re-employs the error covariance matrix $\Sigma$ in the regression parameter prior; cf. Eq. (6). The interference between the regression parameters and the error covariance matrix might introduce a systematic bias. For more details we refer to Supplement S11.

# 5.2.2 mTOR and ANDRO data 

For the mTOR (see Sect. 4.2) and the ANDRO data (see Sect. 4.3) we follow a vector auto-regressive (VAR) approach, so that the observations at the previous time points (=covariates) explain the observations at the current time point (= responses). Covariate-response interactions then refer to dynamic interactions (with a time lag), while error-error interactions refer to contemporaneous interactions (within the time points). Unlike the ANDRO data, the mTOR data were measured at non-equidistant time points. Therefore neither static Bayesian networks (which ignore the data point order) nor dynamic Bayesian networks (which assume equidistant data points) seem appropriate. In our study, we cross-compare the performances of static Bayesian

![img-3.jpeg](img-3.jpeg)

Fig. 4 mTOR results, see Sect. 4.2. We applied leave-one-out cross-validation to compute a predictive probability for each of the 18 data points. The left panel shows box plots of the log predictive probabilities for the models $\mathcal{M}_{D}, \mathcal{M}_{S}, \mathcal{M}_{0,0}$ and $\mathcal{M}_{1,1}$. The right panel shows the gains of model $\mathcal{M}_{1,1}$ over the competitors. The differences are significant (Wilcoxon signed-rank p-values: $0.0016,0.0016$ and 0.0040 ). In Supplement S12 we provide a figure that compares the models $\mathcal{M}_{i, j}(i, j \in\{0,1\})$
![img-4.jpeg](img-4.jpeg)

Fig. 5 ANDRO results, see Sect. 4.3. We applied leave-one-out cross-validation to compute a predictive probability for each of the 49 data points. The left panel shows box plots of the log predictive probabilities for the models $\mathcal{M}_{D}, \mathcal{M}_{S}, \mathcal{M}_{0,0}$ and $\mathcal{M}_{1,1}$. The right panel shows the gains of $\mathcal{M}_{1,1}$ over the competitors. The three differences are significant (Wilcoxon signed-rank p-values: $p<10^{-7}$ ). In Supplement S12 we provide a figure that compares the models $\mathcal{M}_{i, j}(i, j \in\{0,1\})$
networks $\mathcal{M}_{S}$, dynamic Bayesian networks $\mathcal{M}_{D}$, the baseline model $\mathcal{M}_{0,0}$, and the proposed MBLR model $\mathcal{M}_{1,1}$, where the latter two models combine features of $\mathcal{M}_{S}$ and $\mathcal{M}_{D}$. Since the true interactions are unknown, we resort to predictive probabilities, and we follow a leave-one-out cross-validation approach, yielding a predictive probability for each individual left-out data point. Figure 4 shows the results for the mTOR data. It can be seen that the dynamic $\mathcal{M}_{D}$ model performs slightly better than the static $\mathcal{M}_{S}$ model (p-value: $p=0.1297$ ) and that the two MBLR models, $\mathcal{M}_{0,0}$ and $\mathcal{M}_{1,1}$, improve over the two Bayesian network types. In consistency with our finding for the synthetic data, the proposed $\mathcal{M}_{1,1}$ model yields the best results and significantly outperforms the $\mathcal{M}_{0,0}$ baseline model (see right panel of Fig. 4). The results for the ANDRO data are shown in Fig. 5. Unlike for the mTOR data, here the

![img-5.jpeg](img-5.jpeg)

Fig. 6 OES 2010 results, see Sect. 4.4. For different samples sizes $T$ we sampled 10 random data subsets with $S=20$ responses and $N=20$ covariates. Each panel refers to a sample size $T$ and shows box plots of the log predictive probability differences in favour of the $\mathcal{M}_{1,1}$ model. For computing the predictive probabilities we each time generated validation data with $\hat{T}=10$ observations. In Supplement S13 we provide three additional figures
static $\mathcal{M}_{S}$ model performs better than the dynamic $\mathcal{M}_{D}$ model (p-value: $p<10^{-4}$ ), indicating that the contemporaneous interactions are of greater importance. Again the two MBLR models $\left(\mathcal{M}_{0,0}\right.$ and $\left.\mathcal{M}_{1,1}\right)$ improve over both Bayesian network types, and the proposed $\mathcal{M}_{1,1}$ performs best and significantly superior to its three competitors $\mathcal{M}_{D}, \mathcal{M}_{S}$ and $\mathcal{M}_{0,0}$ (see right panel of Fig. 5). In Supplement S12 we compare the results of the four MBLR model variants $\mathcal{M}_{i, j}(i, j \in\{0,1\})$. The results can be summarised as follows: While the models $\mathcal{M}_{0,0}$ and $\mathcal{M}_{1,0}$ (with full covariate matrix) perform worse than the $\mathcal{M}_{1,1}$ model, the predictive probabilities of the $\mathcal{M}_{0,1}$ model (with full error DAG) are comparable to those of the $\mathcal{M}_{1,1}$ model. A possible explanation is that our data have in common that there are more possible covariateresponse interactions than error-error interactions. For more details we refer to Supplement S12.

# 5.2.3 OES 2010 data 

We use the OES 2010 data from Sect. 4.4 to study sample size effects. We crosscompare the performances of the four model variants $\mathcal{M}_{i, j}(i, j \in\{0,1\})$ on data sets with different sample sizes $T$. For each $T \in\{10,20, \ldots, 320\}$ we generate 10 independent data sets. For each we sample $N=20$ covariates, $S=20$ responses, and then $T+10$ observations, where the last $\hat{T}=10$ are for computing predictive probabilities. Figure 6 shows boxplots of the relative log predictive probability differences. The proposed $\mathcal{M}_{1,1}$ model yields for all sample sizes $T$ the highest predictive probabilities, and the relative differences decrease as the sample size $T$ increases. The baseline model $\mathcal{M}_{0,0}$ shows the worst performance. And, as observed before, averaging across the covariate matrices $\left(\mathcal{M}_{0,1}\right)$ yields more improvement than averaging across the error DAGs $\left(\mathcal{M}_{1,0}\right)$. In Supplement S13 we provide more result

Table 2 Average computational costs


In hours [h] and minutes [m] along with standard deviations ( $\pm \mathrm{sd}$ ) for 100 k iterations for different combinations of numbers of responses $S$, covariates $N$, and data points $T$. For each setting 10 data sets were sub-sampled from the OES 2010 data. Simulations were performed using Matlab code on computers with Intel Xeon 2.5 GHz nodes and 4GB RAM
figures. Figure 9 in S13 shows boxplots of the model-specific predictive probabilities from which the differences in Fig. 6 were computed. Figure 10 in S13 shows how the predictive probabilities of the $\mathcal{M}_{1,1}$ model increase in the sample size $T$. Figure 11 in S13 rearranges the results from Fig. 6, so as to show more explicitly how the relative predictive probability differences decrease as the sample size $T$ increases.

# 5.3 Scalability and computational costs 

We also use the OES 2010 data to monitor the scalability of the RJMCMC algorithm from Sect. 2.4. For all combinations of $N \in\{10,20,30\}, S \in\{10,20,30\}$ and $T \in\{25,50,100,200\}$ we generate 10 data sets, each consisting of $N$ random covariates, $S$ random responses and $T$ random data points. Table 2 lists the average computational costs for $V=100 k$ RJMCMC iterations. It can be seen that the no. of covariates $N$ has only a minor effect, while the no. of responses $S$ and data points $T$ clearly affect the run times. While the computational costs seem to increase linearly in $T$, the increase in $S$ does not follow a clear trend. While the transition from $S=10$ to $S=20$ increases the computational costs by factors in the range $2-3$, the transition from $S=20$ to $S=30$ increases the computational costs only by factors in the range 1-2. An exact investigation of the computational costs is beyond the scope of this paper and might be difficult, as our algorithm combines algorithms for Bayesian networks (Giudici and Castelo 2003) and Bayesian linear regression (Raftery

et al. 1997). However, the measured run times suggest that our Matlab implementation does not scale well in $S$ and $T$. For example, running 100k RJMCMC iterations on a data set with $S=30$ responses and $T=200$ data points takes more than 8 hours of computational time on a standard desktop PC. For large sample sizes $T$ one could resort to the traditional MBLR, as our results from Sect. 5.2.3 suggest that the performance differences decrease as $T$ increases. For high-dimensional response vectors $(S>30)$ our current Matlab implementation seems to require 'unreasonably' long run times. ${ }^{8}$ However, we would argue that there are plenty of applications, where the number of responses is (clearly) below $S=30$ and where the new model can yield a substantial improvement in reasonable time (in terms of hours). To improve scalability, one could implement the algorithm in a more efficient programming language, such as $\mathrm{C}++$, or parallelize the code and run it onto a computer cluster. For example the shotgun stochastic search method from Hans et al. (2007) could directly be adapted for speeding up the covariate sampling part. In Supplement S14. we propose and briefly discuss alternative strategies and approximations that might improve scalability.

# 6 Discussion and conclusion 

In this work, we have proposed a new sparse seemingly unrelated regression (SSUR) model. The new model improves in two important respects over earlier proposed SSUR models (Wang 2010). First, our model employs directed acyclic graphs (Gaussian Bayesian networks) rather than undirected graphs (Gaussian graphical models) to model the conditional independencies among the errors. Unlike all earlier proposed SSUR models, our new model is therefore capable of learning some directed edges among the errors. Second, the RJMCMC scheme from Wang (2010) requires computational expensive approximations of the marginal likelihood. For the new model we have designed a RJMCMC algorithm that does not have to rely on approximations. We have shown that all required marginal likelihoods and full conditional distributions can be computed analytically. In particular, we have presented an algorithm for sampling covariance matrices that are coherent with a given directed acyclic graph. When compared with the multivariate Bayesian regression model (MBLR), the proposed SSUR model improves in two ways: It infers response-specific covariate sets and it infers directed acyclic graphs (Gaussian Bayesian networks) among the errors. In a comparative evaluation study we have compared the new SSUR model with the traditional MBLR model as well as with two 'in-between' models, each featuring only one of the two improvements. The results suggest that allowing for response-specific covariate sets yields clearer gains than inferring Gaussian Bayesian networks among the errors. For synthetic data, where the ground truth is known, we have shown that the new model identifies the true interactions with a higher accuracy than the competing model variants. Our current implementation of the RJMCMC algorithm does not scale up well. In

[^0]
[^0]:    ${ }^{8}$ We would not mind investing a few days of computational time on a remote computer for running a RJMCMC simulation on a large data set with $S>30$.

particular, the computational costs increase in the number of responses and in the sample size. We feel that the new SSUR model might be of high relevance for vector auto regressive (VAR) models. In VAR models one distinguishes between dynamic and contemporaneous interactions and both interaction types are considered to be (equally) important. The existing VAR and SSUR models only learn undirected contemporaneous interactions, while our new model can learn a mixture of directed and undirected edges among the errors. When applied in a vector auto regressive fashion, the error-error edges correspond to response-response edges, so that our model is capable of learning some directed contemporaneous interactions. Our future work will aim to improve the scalability of the RJMCMC algorithm so that new model features can be added. For VAR models, it would for example be interesting to combine our new method with multiple change point processes (Fearnhead 2006), so as to be able to infer time-varying VAR models (Koop and Korobilis 2013), where the model parameters can undergo temporal changes. Although conceptually easy to achieve, changepoints increase the model complexity further. Henceforth, the combination of both approaches is subject to the condition that the scalability can be improved.

Supplementary Information The online version contains supplementary material available at https://doi. org/10.1007/s00180-022-01258-9.

Acknowledgements A.S. is funded by University of Malakand (Pakistan) under the Faculty Development Programme to carry out his overseas PhD studies at Groningen University (NL).

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licen ses/by/4.0/.
