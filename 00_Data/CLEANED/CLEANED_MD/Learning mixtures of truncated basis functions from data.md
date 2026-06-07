# Learning Mixtures of Truncated Basis Functions from Data 

Helge Langseth<br>Department of Computer and Information Science<br>The Norwegian University of Science and Technology<br>Trondheim (Norway)<br>helgel@idi.ntnu.no

Thomas Dyhre Nielsen<br>Department of Computer Science<br>Aalborg University<br>Aalborg (Denmark)<br>tdn@cs.aau.dk

Antonio Salmerón<br>Department of Statistics and Applied Mathematics<br>University of Almería, Almería (Spain)<br>antonio.salmeron@ual.es


#### Abstract

In this paper we describe a new method for learning hybrid Bayesian network models from data. The method utilizes a kernel density estimator, which is in turn "translated" into a mixture of truncated basis functions-representation using a convex optimization technique. We argue that these estimators approximate the maximum likelihood estimators, and compare our approach to previous attempts at learning hybrid Bayesian networks from data. We conclude that while the present method produces estimators that are slightly poorer than the state of the art (in terms of log likelihood), it is significantly faster.


## 1 Introduction

In domains involving both discrete and continuous variables, Bayesian networks with mixtures of truncated exponentials (MTEs) (Moral et al., 2001) and mixtures of truncated polynomials (MOPs) (Shenoy and West, 2011) have received increasing interest over the last few years. A recent addition to the fold is the mixtures of truncated basis functions (MoTBFs) framework (Langseth et al., 2012), which offers a unified theory for MTEs and MoPs. The MoTBFs framework allows discrete and continuous variables to co-exist in a Bayesian network without any structural constraints, and since the family of MoTBFs is closed under addition, multiplication, and integration, inference in an MoTBF network can be performed efficiently using the Shafer-Shenoy architecture (Shafer and Shenoy, 1990).

The problem of learning MoTBF models from data has been only scarcely considered, with the main body of work relating to MTEs (Romero et al., 2006; Langseth et al., 2009, 2010); we are not aware of published contributions focusing
on the MoP framework. Romero et al. (2006) used a kernel estimator to represent the data distribution, and thereafter fitted an MTE to the kernel using regression. Langseth et al. $(2009,2010)$ attempted to find maximum likelihood parameters directly but since the maximum likelihood equations have no analytic solution in general, they instead proposed an iterative scheme utilizing Newton's method and Lagrange multipliers. This resulted in better estimators (in terms of likelihood on the trainingset as well as on a hold-out test-set), but at the cost of a steep increase in the computational complexity.

We present a new parameter estimation method, which aims at approximating the maximum likelihood parameters of an MoTBF network with known structure. We compare our results to those of Langseth et al. $(2009,2010)$, and find that although the new method finds parameters that are slightly poorer (in terms of likelihood), it is more than an order of magnitude faster than previous techniques.

The rest of the paper is organized as follows:

We start with an introduction to the MoTBF framework in Section 2. The simplified problem of learning univariate MoTBFs from data is considered in Section 3, and we discuss learning conditional distributions in Section 4. We report on some experiments in Section 5, and finally we conclude in Section 6.

## 2 The MoTBF model

The MoTBF framework is based on the abstract notion of real-valued basis functions $\psi(\cdot)$, which includes both polynomial and exponential functions as special cases. The first building-block of the framework is the marginal distribution: Let $X$ be a continuous variable with domain $\Omega_{X} \subseteq \mathbb{R}$ and let $\psi_{i}: \mathbb{R} \rightarrow \mathbb{R}$, for $i=0, \ldots, k$, define a collection of real basis functions. We say that a function $g_{k}: \Omega_{X} \mapsto \mathbb{R}_{0}^{+}$is a mixture of truncated basis functions (MoTBF) potential of level $k$ wrt. $\Psi=\left\{\psi_{0}, \psi_{1}, \ldots, \psi_{k}\right\}$ if $g_{k}$ can be written as

$$
g_{k}(x)=\sum_{i=0}^{k} a_{i} \psi_{i}(x)
$$

where $a_{i}$ are real numbers. The potential is a density if $\int_{\Omega_{X}} g_{k}(x) d x=1$. Note that as opposed to the MTE and MoP definitions, a marginal MoTBF potential does not employ interval refinement to improve its expressive power.

Next, we turn to the MoTBF definition of conditional distributions, which mirrors the corresponding definition for MTEs. Thus, the influence a set of continuous parent variables $\mathbf{Z}$ has on their child variable $X$ is encoded only through the partitioning of the domain of $\mathbf{Z}$, $\Omega_{\mathbf{Z}}$, into hyper-cubes, and not directly in the functional form of $g_{k}^{(l)}(x \mid \mathbf{z})$ inside each hypercube $\Omega_{\mathbf{Z}}^{l}$. More precisely, for a partitioning $\mathcal{P}=$ $\left\{\Omega_{\mathbf{Z}}^{l}, \ldots, \Omega_{\mathbf{Z}}^{m}\right\}$ of $\Omega_{\mathbf{Z}}$, the conditional MoTBF is

[^0]defined for $\mathbf{z} \in \Omega_{\mathbf{Z}}^{j}, 1 \leq j \leq m$, as

$$
g_{k}^{(j)}\left(x \mid \mathbf{z} \in \Omega_{\mathbf{Z}}^{j}\right)=\sum_{i=0}^{k} a_{i, j} \psi_{i}(x)
$$

Finally, the joint MoTBF distribution over $\mathbf{x}=$ $\left(x_{1}, \ldots, x_{n}\right)$ is found using the usual factorization, $g_{\boldsymbol{k}}(\mathbf{x})=\prod_{i=1}^{n} g_{k_{i}}\left(x_{i} \mid \mathrm{pa}\left(x_{i}\right)\right)$, where the marginals and conditional distributions are defined using Equations (1) and (2), respectively.

Langseth et al. (2012) describe a "translation" procedure for efficiently finding an MoTBF approximation of any density function. The approximation procedure assumes that the basis functions $\Psi$ are both legal and orthonor$\mathrm{mal}:$ If $\mathcal{Q}$ is the set of all linear combinations of the members of a set of basis functions $\Psi=\left\{\psi_{i}(\cdot)\right\}_{i=0}^{\infty}$, then $\Psi$ is said to be a legal set of basis functions if the following conditions hold:

- $\psi_{0}$ is constant in its argument.
- If $\phi_{i} \in \mathcal{Q}$ and $\phi_{j} \in \mathcal{Q}$, then $\left(\phi_{i} \cdot \phi_{j}\right) \in \mathcal{Q}$.
- For any pair of real numbers $s$ and $t$, there exists a function $\phi \in \mathcal{Q}$ such that $\phi(s) \neq$ $\phi(t)$.

When considering orthonormal basis functions, we focus on the space $L^{2}[a, b]$ of quadratically integrable real functions over the finite interval $\Omega=[a, b]$. For two functions $\phi_{i}$ and $\phi_{j}$ defined on $\Omega$ we define the inner product as

$$
\left\langle\phi_{i}, \phi_{j}\right\rangle=\int_{\Omega} \phi_{i}(x) \phi_{j}(x) d x
$$

and say that two functions are orthonormal if $\left\langle\phi_{i}, \phi_{j}\right\rangle=\delta_{i j}$, where $\delta_{i j}$ is the Kronecker delta. A set of non-orthonormal basis functions can easily be orthonormalized using, for instance, the Gram-Schmidt procedure.

To set the scene, we let $f(x)$ be the (target) density, and let $g_{k}(x \mid \boldsymbol{\theta})$ be an MoTBF of order $k$. The key idea of Langseth et al. (2012) is to use generalized Fourier series to find "optimal" values for $\boldsymbol{\theta}=\left(\theta_{0}, \ldots, \theta_{k}\right)$, that is, choosing $\hat{\theta}_{i}=\left\langle f, \psi_{i}\right\rangle$. It can easily be shown that while the generalized Fourier approximation up to degree $k$ is guaranteed to minimize the $L^{2}$ distance


[^0]:    ${ }^{1}$ In this paper we will often refer to MoTBF potentials defined only over continuous variables. In such cases, we understand, unless the contrary is specified, that all the claims about such potentials are extensible to those potentials also containing discrete variables in their domains, simply by having the claims hold for each configuration of the discrete variables.

$\int_{x}\left(f(x)-g_{k}(x \mid \hat{\boldsymbol{\theta}})\right)^{2} d x, g_{k}$ is not always positive, and is thus not a density approximation. A convex optimization scheme (initialized with the generalized Fourier series coefficients) was therefore employed to obtain parameters that guarantee that $g_{k}(x)$ is a density, and at the same time minimize an upper bound of the KL divergence $D\left(f \| g_{k}\right)$ (Langseth et al., 2012). It was also shown that the approximation can be made arbitrarily tight, simply by increasing $k$.

## 3 Learning univariate distributions

While Langseth et al. (2012) defined their translation procedure as a means to create MoTBF approximations of known distributions, this paper will utilize the translation for learning hybrid BNs from data. The top-level algorithm is to (1) approximate the data using a kerneldensity, and (2) approximate the kernel density with an MoTBF parameterization. We discuss each step below, and start by looking at univariate (marginal) distributions. We will move on to conditional distributions in Section 4.

Assume that $f(x)$ is the (unknown) density, which generated the univariate sample $\mathcal{D}=$ $\left\{x_{1}, \ldots, x_{N}\right\}$. Next, let $h_{\mathcal{D}}\left(\cdot \mid t_{w}\right)$ be a kernel density estimator based on the samples $\mathcal{D}$ using kernel function $t_{w}$ with bandwidth $w$. We define the kernel density estimator s.t. $w$ approaches zero as $N \rightarrow \infty$. Now, the soundness of the approach rests upon the following proposition:
Proposition 1. Let $\hat{\boldsymbol{\theta}}_{N}$ be chosen to minimize $D\left(h_{\mathcal{D}}\left(x \mid t_{w}\right) \| g_{k}\left(x \mid \hat{\boldsymbol{\theta}}_{N}\right)\right)$. Then $\hat{\boldsymbol{\theta}}_{N}$ converges to the maximum likelihood estimator of $\boldsymbol{\theta}$ as $N \rightarrow \infty$.

## Sketch of proof:

First we note that since

$$
\begin{aligned}
& D\left(h_{\mathcal{D}}\left(x \mid t_{w}\right) \| g_{k}(x \mid \boldsymbol{\theta})\right)= \\
& \quad \int_{x} h_{\mathcal{D}}\left(x \mid t_{w}\right) \log \left(\frac{h_{\mathcal{D}}\left(x \mid t_{w}\right)}{g_{k}(x \mid \boldsymbol{\theta})}\right) d x
\end{aligned}
$$

minimizing $D\left(h_{\mathcal{D}}\left(x \mid t_{w}\right) \| g_{k}(x \mid \boldsymbol{\theta})\right)$ wrt. $\boldsymbol{\theta}$ is equivalent to maximizing $\mathbb{E}_{h_{\mathcal{D}}}\left[\log g_{k}(X \mid \boldsymbol{\theta})\right]$ wrt. $\boldsymbol{\theta}$; the expectation is taken wrt. $X$, which is assumed to have density function $h_{\mathcal{D}}\left(\cdot \mid t_{w}\right)$. Next,
since the bandwidth of $h_{\mathcal{D}}\left(\cdot \mid t_{w}\right)$ decreases to 0 as $N \rightarrow \infty$, we have that

$$
h_{\mathcal{D}}\left(x \mid t_{w}\right) \rightarrow \frac{1}{N} \sum_{\ell=1}^{N} \delta\left(x-x_{\ell}\right)
$$

as $N \rightarrow \infty$, where $\delta(\cdot)$ is Dirac's delta. Therefore, $\mathbb{E}_{h_{\mathcal{D}}}\left[\log g_{k}(X \mid \boldsymbol{\theta})\right] \rightarrow \int_{x} \sum_{\ell} \frac{1}{N} \delta\left(x-x_{\ell}\right)$. $\log g_{k}(x \mid \boldsymbol{\theta}) d x=\frac{1}{N} \sum_{\ell} \log g_{k}\left(x_{\ell} \mid \boldsymbol{\theta}\right)$. It follows that the parameters that minimize the KL divergence are asymptotically also those that maximize the likelihood.

The MoTBF density $g_{k}(x \mid \boldsymbol{\theta})$ uses $k+2$ parameters: The interval of support ( 2 values) and the $k$ "free" $\theta$-values ( $\theta_{0}$ is fixed to make sure the function integrates to one; recall that an MoTBF density is defined without interval refinement). Thus, we can choose between models $g_{\ell}$ and $g_{m}$ using an (approximate) BIC-score: The (approximate) ML parameters are found, and each model is penalized according to complexity. In the experiments reported in Section 5 we have used a greedy approach starting from $g_{0}$ and stopping as soon as an approximation $g_{k}$ is better (in terms of BIC) than both $g_{k+1}$ and $g_{k+2} .{ }^{2}$ Our greedy procedure is exemplified in Figure 1, where an MoTBF is learned from 50 samples from a standard Gaussian distribution (shown as crosses on the $x$-axis). The kernel density approximation is drawn with a dashed line, and the MoTBF approximations from $g_{0}$ up to $g_{10}$ are shown; $g_{5}$ is the best in terms of BIC-score, and is drawn with double line-width.

To fully specify the learning of univariate MoTBF distributions from data, we need to further analyze the use of kernel density approximations as an intermediate representation between the data and the learned MoTBF. The use of kernel estimators for learning MTEs was first proposed by Romero et al. (2006), and further analyzed by Langseth et al. (2010). The Epanechnikov kernel was found to offer the most consistent results in the case of MTE learning (Langseth et al., 2010), but we nevertheless use

[^0]
[^0]:    ${ }^{2}$ Computationally more demanding procedures can also be devised, e.g., to compare all subsets of basis functions from a fixed set $\left\{\psi_{0}, \psi_{1}, \ldots, \psi_{k}\right\}$.

![img-0.jpeg](img-0.jpeg)

Figure 1: BIC-based learning: 50 samples from a standard Gaussian (crosses on the x-axis) are evaluated. The density estimator (thin dashed line) is the target of the MoTBF translations. g₀ up to g₁₀ are shown; g₅ is the best in terms of BIC-score, and is drawn with double line-width.

The Gaussian kernel in our work is to speed up the implementation. Previous attempts used Silverman's rule of thumb when selecting the bandwidth, tᵢₖ ≈ 1.06·∂·N⁻¹/⁵, where ∂ is the empirical standard deviation of the dataset. By following that procedure, we get the results shown in Figure 2 (left-hand part of figure): a kernel density estimator is fitted to 50 samples from a standard Gaussian distribution, and the kernel density (drawn with the thin line) is then used as a starting point for the BIC-based MoTBF learning. The learned MoTBF representation is defined using 3 basis functions. Visually, the MoTBF approximation is quite poor (it does not resemble the standard Gaussian drawn with a dashed line), and we argue that the reason for the poor result is that using tᵢₖ is an unfortunate bandwidth choice, as it in principle leads us to smoothing the data twice: once when employing the kernel density, and once when the MoTBF is fitted to the kernel density. Rather, we want the kernel density to be a faithful representation of the data. To illustrate the effect, the righthand part of Figure 2 shows the result of using the scaled bandwidth tᵢₖ/25. For this bandwidth, the BIC-score is optimized using 5 basis functions. The results are visually more appealing, and this is underlined when calculating the log likelihood of a hold-out set, giving -1541.02 and -1464.86 for the two bandwidths, respectively. We have investigated this further by examining a range of different datasets, both small and large, as defined by Langseth et al. (2010). For each dataset, we have learned an MoTBF representation using the BIC score for model selection and with a set of bandwidths defined by tᵥ ← tᵢₖ/α, where α ∈ {1, 2, 5, 10, 25, 50} is the bandwidth scale. Table 1 lists the results of the experiment in terms of the number of basis functions that are selected as well as the obtained log likelihood on a hold-out dataset. The results appear to be robust across the data sets as long as the bandwidth is "sufficiently small". We have therefore used a fixed value of tᵢₖ/10 in the following, unless stated otherwise.

## 4 Learning conditional distributions

Recall that for a conditional MoTBF f(x|z), the variables Z influence X only through the partitioning of Ωz, see Equation (2). Learning a conditional MoTBF therefore amounts to finding

- a partitioning of Ωz, and
- a (univariate) MoTBF for each hyper-cube in the partitioning.

![img-1.jpeg](img-1.jpeg)

Figure 2: 50 samples from a Gaussian distribution are learned using a kernel density. The kernel density is shown in a thin line, where the bandwidth is the Silverman's rule of thumb (left figure) and one twenty-fifth of Silverman's rule of thumb (right). The learned MoTBF representations are defined using 3 and 5 basis functions in the left and right hand plots, respectively, and drawn in a thick line. Visually, the right-hand figure gives a better fit (compare to the standard Gaussian density drawn with the dashed line), and this is also the case when evaluated using log likelihood of a hold-out set (–1541.020 and –1465.585, respectively).

The algorithm for learning conditionals MoTBFs proceeds by iterating over the two steps above.

## 4.1 Finding an MoTBF for a fixed partitioning

For a given hyper-cube $\Omega_{\mathbf{Z}}^{l} \in \mathcal{P}$ we start by approximating the conditional empirical distribution with a conditional kernel density estimate. For ease of exposition, consider a variable $Y$ with parent $X$ for which we have a data sample $\mathcal{D} = \{\boldsymbol{d}_1, \ldots, \boldsymbol{d}_N\}$, where $\boldsymbol{d}_i = (x_i, y_i)$. We now define the conditional kernel density estimate for $Y$ given $X$ as

$$h_{\mathcal{D}}(y|x, t_{w_y}, t_{w_x}) = \frac{\sum_{i=1}^{N} h_{y_i}(y|t_{w_y})h_{x_i}(x|t_{w_x})}{\sum_{i=1}^{N} h_{x_i}(x|t_{w_x})},$$

where $h_{x_i}(x|t_{w_x})$ is a kernel density estimator based on $x_i$ only and with bandwidth $t_{w_x}$; $h_{y_i}(y|t_{w_y})$ is defined similarly. Given a conditional kernel density estimator $h_{\mathcal{D}}(y|x, t_{w_y}, t_{w_x})$ and a partitioning $\mathcal{P}$ of $\Omega_X$, we approximate $h_{\mathcal{D}}(y|x, t_{w_y}, t_{w_x})$ with an MoTBF potential $f(y|x)$ (see Equation (2)) by following the procedure of Langseth et al. (2012). Thus, for all $\Omega_{X}^{l} \in \mathcal{P}$, we seek

$$f(y|x \in \Omega_{X}^{l}) \sim h_{\mathcal{D}}(y|x \in \Omega_{X}^{l}, t_{w_y}, t_{w_x}) = \int_x h_{\mathcal{D}}(y|x, t_{w_y}, t_{w_x})h_{\mathcal{D}}(x|x \in \Omega_{X}^{l}, t_{w_x})dx,$$

where the integral can be approximated by $\sum_{i=1}^{n} h_{\mathcal{D}}(y|x_i, t_{w_y}, t_{w_x})h_{\mathcal{D}}(x_i |x_i \in \Omega_{X}^{l}, t_{w_x})$ using data samples $x_1, \ldots, x_n$ from $\mathcal{D}$ belonging to $\Omega_{X}^{l}$. That is, for a fixed partitioning of $\Omega_X$ learning a conditional MoTBF potential reduces to estimating a univariate MoTBF potential (as described in Section 3) for each partition $\Omega_{X}^{l} \in \mathcal{P}$.

## 4.2 Finding a partitioning of the conditioning variables

In order to find a partitioning of $\Omega_{\mathbf{Z}}$ we employ a myopic strategy, where we in each step consider a bisection of an existing partition along each $Z \in \mathbf{Z}$. That is, for each partition $\Omega_{\mathbf{Z}}^{l} \in \mathcal{P}$ the algorithm evaluates the potential gain of splitting the partition along $Z \in \mathbf{Z}$. After scoring the candidate partitions the algorithm selects the highest scoring partition $\Omega_{\mathbf{Z}}^{\text{BS}}$ and splitting variable $Z_{\text{BS}}$, and learns MoTBF representations of the two induced sub-partitions $\Omega_{\mathbf{Z}}^{\text{BS},1}$ and $\Omega_{\mathbf{Z}}^{\text{BS},2}$. To guide the selection of a candidate partition $\Omega_{\mathbf{Z}}^{\prime}$ we consider the potential improvement in BIC score resulting from splitting that partition:

$$\text{BIC-Gain}(\Omega_{\mathbf{Z}}^{\prime}, Z) = BIC(f', \mathcal{D}) - BIC(f, \mathcal{D}),$$

where $f'$ is the conditional MoTBF potential defined over the partitioning $\{\mathcal{P} \setminus \Omega_{\mathbf{Z}}^{\prime}\} \cup$


Table 1: The effect of the chosen bandwidth wrt. log likelihood of a test-set. In general, we see that results for "large" bandwidths $(\alpha=1)$ are poor due to "double smoothing". Additionally, results using large scalers $(\alpha=50)$ are also sometimes unsatisfactory; typically due to numerical instabilities in the solution method due to the peakedness of the kernel approximation, which in turn leads to numerically unstable calculations.
$\left\{\Omega_{\mathbf{Z}}^{Z, 1}, \Omega_{\mathbf{Z}}^{Z, 2}\right\}$. In principle, when scoring the model $f^{\prime}$ one would need to find the basis functions (and the corresponding parameters) maximizing this score. This will, however, be computationally difficult, and instead we lower-bound the improvement in BIC score by using the same set of basis functions as was used for the parent partition $\Omega_{\mathbf{Z}}^{\prime}$. It should be noted that for the calculation of the improvement in BIC score, we only need to consider the parts of the score relating to the partition $\Omega_{\mathbf{Z}}^{\prime}$, since the contributions from the partitions for which $f$ and $f^{\prime}$ agree cancel out; this property also sup-

```
Algorithm 1 Learning conditional MoTBFs.
    \(\mathcal{P} \leftarrow\left\{\Omega_{\mathbf{Z}}\right\}\)
    repeat
        \(\left(\Omega_{\mathbf{Z}}^{\mathrm{BS}}, Z_{\mathrm{BS}}\right) \leftarrow\)
            \(\arg \max _{\Omega_{\mathbf{Z}}^{\prime} \in \mathcal{P}, Z \in \mathbf{Z}} \mathrm{BIC}-\operatorname{Gain}\left(\Omega_{\mathbf{Z}}^{\prime}, Z\right)\)
        if BIC-Gain \(\left(\Omega_{\mathbf{Z}}^{\mathrm{BS}}, Z_{\mathrm{BS}}\right)>0\) then
            Learn MoTBF potentials for
                \(\Omega_{\mathbf{Z}}^{\mathrm{BS}, 1}\) and \(\Omega_{\mathbf{Z}}^{\mathrm{BS}, 2}\).
            \(\mathcal{P} \leftarrow\left\{\mathcal{P} \backslash \Omega_{\mathbf{Z}}^{\mathrm{BS}}\right\} \cup\left\{\Omega_{\mathbf{Z}}^{\mathrm{BS}, 1}, \Omega_{\mathbf{Z}}^{\mathrm{BS}, 2}\right\}\)
        else
            terminate.
        end if
    until false
```

ports an efficient caching scheme for BIC-Gain. The overall procedure for learning conditional MoTBFs is summarized in Algorithm 1.

## 5 Experiments

In this section we will report on two small experimental studies undertaken to compare the merits of the proposed method to its most immediate competitors. Firstly, we will compare the new method of learning marginal MoTBF densities to the results obtained by Romero et al. (2006) and Langseth et al. (2010), as reported by Langseth et al. (2010). Datasets, each containing 1000 training examples, generated from five different distributions were used. Table 2 reports the log likelihood of each dataset using the obtained estimator of each of the techniques. We have used the polynomials as basis functions, meaning that $\psi_{\ell}$ in Equations (1) and (2) is the (scaled and stretched) Legendre polynomial of order $\ell$. The number of basis functions was chosen so that the number of free parameters corresponds to the number of parameters used by Langseth et al. (2010); recall that the MoTBF distribution $g_{k}$ on $\Omega_{\mathbf{Z}}$ is specified using $k+2$ parameters. Note that where the methods by Romero et al. (2006) and Langseth et al. (2010) divide the support of the distribution into sub-intervals and fit one model per interval, the current approach does not use interval refinement. This may harm the fit of the MoTBF distributions, when the gold-standard distribu-


Table 2: The obtained log likelihood of the training data when learning from 1000 samples from different distributions.
tion is not continuous. In general, though, the results of the new method seem to be better than those by Romero et al. (2006), and comparable to those by Langseth et al. (2010).

The speedup from the direct maximum likelihood approach (Langseth et al., 2010) to our approach is above a factor 10. The main contribution to the speed increase is that while the previous technique was based on an iterative scheme, where each potential solution (living in a very complicated likelihood-landscape) needed to be evaluated using a computationally expensive procedure, the current approach casts the learning problem as a convex optimization problem, with much cheaper evaluations.

Next, we compare the predictive performance of the method in Langseth et al. (2010) to ours. We used the same training data as reported in Table 2, but this time used the (approximate) BIC score for model selection. The chosen models were examined by calculating the log likelihood of a separate dataset of 1000 cases.


Table 3: Test-set log likelihood of estimators after learning models using the BIC score.

The results in Table 3 indicate that the method by Langseth et al. (2010) is slightly better than our procedure, but the speedup of the current approach is more than a factor 15. The main source of the extra speed-increase is that the relatively costly initialization of the MoTBF technique (finding and representing the orthonormal
basis functions) needs not be performed each time a new candidate model is evaluated.

Finally, we exemplify the learning of conditional distributions by generating data from a model where $X$ is standard Gaussian, and $Y \mid\{X=x\} \sim \mathcal{N}(x / 2,1)$. Datasets containing $50,500,2500$ and 5000 cases were generated, and given to Algorithm 1. The resulting conditional distributions are shown in Figure 3, with the parent on the $x$-axis and the child on the $y$-axis. For the smallest dataset of 50 cases, the BIC-score only gave support for a single splitpoint, inserted at the midpoint of the support for $X$. As the size of the training-sets increases, the BIC score selects more and more refined models, allowing itself to use more parameters to represent the correlation between $X$ and $Y$ as it is more and more clearly manifested in the training data. Notice that the algorithm uses more effort on refining the model where the bulk of the data is found (i.e., around $x \approx 0$ ).

## 6 Conclusions

In this paper we have examined a new technique for (approximately) learning maximum likelihood parameters of a hybrid Bayesian network from data. The main idea is to find a kernel density estimate of the data and utilize an effective "translation" procedure designed for approximating any marginal or conditional distribution function (in this case a kernel density) by an MoTBF distribution. Although the method was found to be slightly worse than state-of-the-art techniques in terms of the log-likelihood score, the speed-up over previous methods is substantial, and we are currently investigating how the method scales to larger domains.

![img-2.jpeg](img-2.jpeg)

Figure 3: Learning a conditional linear Gaussian distribution using BIC score. Note how finer model granularity is selected as the size of training-set grows, and how the discretization effort is is kept to the area with the bulk of the data.

## Acknowledgments

This work has been supported by a Senior Grant in the frame of the CALL UCM-EEA-ABEL-02-2009 of the Abel Extraordinary Chair (NILS Project), and by the Spanish Ministry of Science and Innovation, through projects TIN2010-20900-C04-02,03 (entitled Data mining with PGMs: New algorithms and applications) and by ERDF (FEDER) funds.
