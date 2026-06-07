# Conditional Density Approximations with Mixtures of Polynomials 

Gherardo Varando, ${ }^{1, \pm}$ Pedro L. López-Cruz, ${ }^{1, \dagger}$ Thomas D. Nielsen, ${ }^{2, \ddagger}$ Pedro Larrañaga, ${ }^{1, \S}$ Concha Bielza ${ }^{1, \S}$<br>${ }^{1}$ Departamento de Inteligencia Artificial, Computational Intelligence Group, Universidad Politécnica de Madrid, Spain<br>${ }^{2}$ Department of Computer Science, Aalborg University, Denmark

Mixtures of polynomials (MoPs) are a nonparametric density estimation technique especially designed for hybrid Bayesian networks with continuous and discrete variables. Algorithms to learn one- and multidimensional (marginal) MoPs from data have recently been proposed. In this paper, we introduce two methods for learning MoP approximations of conditional densities from data. Both approaches are based on learning MoP approximations of the joint density and the marginal density of the conditioning variables, but they differ as to how the MoP approximation of the quotient of the two densities is found. We illustrate and study the methods using data sampled from known parametric distributions, and demonstrate their applicability by learning models based on real neuroscience data. Finally, we compare the performance of the proposed methods with an approach for learning mixtures of truncated basis functions (MoTBFs). The empirical results show that the proposed methods generally yield models that are comparable to or significantly better than those found using the MoTBF-based method. (c) 2014 Wiley Periodicals, Inc.

## 1. INTRODUCTION

Mixtures of polynomials (MoPs), ${ }^{1,2}$ mixtures of truncated basis functions (MoTBFs), ${ }^{3}$ and mixtures of truncated exponentials (MTEs) ${ }^{4}$ have recently been proposed as nonparametric density estimation techniques for hybrid Bayesian networks (BNs) that include both continuous and discrete random variables (MoTBF includes MTEs and MoPs as special cases, and at a slight loss of precision we will sometimes simplify the presentation by simply referring to this joint collection of

[^0]
[^0]:    ${ }^{+}$Author to whom all correspondence should be addressed; e-mail: gherardo.varando@ upm.es.
    ${ }^{\dagger}$ e-mail: pedro.lcruz@upm.es
    ${ }^{\ddagger}$ e-mail: tdn@cs.aau.dk
    ${ }^{\ddagger}$ e-mail: pedro.larranaga@fi.upm.es
    $\S_{\text {e-mail: mcbielza@fi.upm.es. }}$

potentials as MoTBF potentials and MoTBF networks by extension). These classes of densities are closed under multiplication and marginalization, and they therefore support exact inference schemes over BNs without deterministic conditionals based on the Shenoy-Shafer architecture. ${ }^{5,6}$ Furthermore, the densities are integrable in closed form, thereby avoiding any structural constraints on the model, unlike, for example, conditional linear Gaussian (CLG) networks.

Typically, an MoTBF network is constructed by either making an MoTBFtranslation of the densities in an existing hybrid network or by automatically learning the MoTBF densities from data. Methods for translating standard statistical density functions have been explored, for example, in Cobb et al. ${ }^{7}$ and include regular discretization as a special case. For learning MoTBF densities, research has mainly been directed toward learning univariate densities from data. Moral et al. ${ }^{8}$ and Romero et al. ${ }^{9}$ used iterative least squares estimation procedures to obtain MTE potentials based on, respectively, an empirical histogram and a kernel-based density representation of the data. Although least squares estimation procedures may provide potentials with good generalization properties, there is no guarantee that the estimated parameter values will be close to the maximum likelihood values. This shortcoming has motivated alternative learning schemes that perform direct maximum likelihood estimation. For example, Langseth et al. ${ }^{10}$ consider optimizing the likelihood function using numerical methods, whereas Langseth et al. ${ }^{11,12}$ use a kernel density estimate of the data as a proxy for learning the maximum likelihood parameters, and López-Cruz et al. ${ }^{13}$ present a maximum likelihood based learning method relying on B-spline interpolation.

In spite of the advances in learning univariate densities, methods for learning conditional densities have so far only receive limited attention. There are two immediate approaches for learning conditional MoTBF densities: (1) express the conditional density $f(x \mid \mathbf{y})$ as the quotient $f(x, \mathbf{y}) / f(\mathbf{y})$ and learn an MoTBF representation $\varphi(x \mid \mathbf{y})$ by finding MoTBF representations of the two components in the quotient and (2) learn an MoTBF representation of $f(x \mid \mathbf{y})$ directly from the data. The problem with the first approach is that neither MoPs, MTEs, nor MoTBFs are closed under division, hence the resulting potential does not belong to the class of MoTBFpotentials. The second approach is hampered by the difficulty of ensuring that the learned MoTBF representation is a proper conditional density. In general, the learning problem can be considered an overspecified optimization problem, where we have an uncountable number of constraints (one for each value of the conditioning variables), but only a finite number of parameters. ${ }^{14}$ Hence, directly learning $\varphi(x \mid \mathbf{y})$ from data is not immediately feasible. As a result of these difficulties, conditional MoTBFs are typically being obtained by simply discretizing the parent variables and learning a marginal density for each of the discretized regions of these variables. Thus, the estimation of a conditional density is equivalent to estimating a collection of marginal densities, where the correlation between the variable and the conditioning variables is captured by the discretization procedure only; each marginal density is a constant function over the region for which it is defined. ${ }^{11,14}$ One exception to this approach is a recently proposed specification/translation method by Shenoy ${ }^{2}$ who defines MoPs based on hyperrhombuses, which generalize the hyperrectangles underlying the traditional MoP definition. However, this extension mainly addresses

the need for modeling multidimensional linear deterministic conditionals as well as high-dimensional CLG distributions.

In this paper, we present two new methods for learning conditional MoP densities: one is based on conditional sampling and the other on interpolation. Thus, our approaches differ from previous methods in several ways. First, as opposed to Shenoy and West, ${ }^{1}$ Shenoy, ${ }^{2}$ and Langseth et al., ${ }^{3}$ we learn conditional MoPs directly from data without any parametric assumptions. Second, we do not rely on a discretization of the conditioning variables to capture the correlation among the variables. ${ }^{11,14}$ On the downside, the conditional MoPs being learned are not guaranteed to be proper conditional densities, hence the posterior distributions established during inference have to be normalized so that they integrate to one. We analyze the methods using data sampled from known parametric distributions as well as real-world neuroscience data. Finally, we compare the proposed methods with an algorithm for learning MoTBFs. ${ }^{11}$ The results show that the proposed methods generally yield results that are either comparable to or significantly better than those obtained using the MoTBF-based method.

The results in this paper extend those published in López-Cruz et al. ${ }^{15}$ In comparison, the added contributions of the present paper include a new method for learning the structure defining parameters of the conditional MoP potentials. The empirical analysis is extended to also cover the new learning method and we expand on the scope of this analysis by including additional data sets (both synthetic and real world).

The paper is organized as follows. Section 2 reviews MoPs. Section 3 details the two new approaches for learning conditional MoPs and provides an empirical study with artificial data sampled from known distributions. An experimental comparison with MoTBFs is shown in Section 4. Section 5 includes the application of the new methods to real neuroscience data. Section 6 ends with conclusions and outlines future work.

# 2. PRELIMINARIES 

In this section, we review the one- and multidimensional MoP approximations of a probability density function and how they are learnt using B-spline interpolation.

### 2.1. Mixtures of Polynomials

Let $X$ be a one-dimensional continuous random variable with probability density $f_{X}(x)$. Shenoy and West ${ }^{1}$ defined a one-dimensional MoP approximation of $f_{X}(x)$ over a closed domain $\Omega_{X}=\left[\epsilon_{X}, \xi_{X}\right] \subset \mathbb{R}$ as an $L_{X}$-piece $d_{X}$-degree piecewise function of the form

$$
\varphi_{X}(x)= \begin{cases}\operatorname{pol}_{l_{X}}(x) & \text { for } x \in A_{l_{X}}, l_{X}=1, \ldots, L_{X} \\ 0 & \text { otherwise }\end{cases}
$$

where $\operatorname{pol}_{l_{X}}(x)=b_{0, l_{X}}+b_{1, l_{X}} x+b_{2, l_{X}} x^{2}+\cdots+b_{d_{X}, l_{X}} x^{d_{X}}$ is a polynomial function with degree $d_{X}$ (and order $r_{X}=d_{X}+1$ ), $b_{0, l_{X}}, \ldots, b_{d_{X}, l_{X}}$ are constants, and $A_{1}, \ldots, A_{L_{X}}$ are disjoint intervals in $\Omega_{X}$, which do not depend on $x$ and with $\Omega_{X}=\cup_{l_{X}=1}^{L_{X}} A_{l_{X}}$

Let $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$ be a multidimensional continuous random variable with probability density $f_{\mathbf{X}}(\mathbf{x})$. A multidimensional MoP approximation ${ }^{1}$ of $f_{\mathbf{X}}(\mathbf{x})$ over a closed domain $\Omega_{\mathbf{X}}=\left[\epsilon_{1}, \xi_{1}\right] \times \ldots \times\left[\epsilon_{n}, \xi_{n}\right] \subset \mathbb{R}^{n}$ is an $L$-piece $d$-degree piecewise function of the form

$$
\varphi_{\mathbf{X}}(\mathbf{x})= \begin{cases}\operatorname{pol}_{l}(\mathbf{x}) & \text { for } \mathbf{x} \in A_{l}, l=1, \ldots, L \\ 0 & \text { otherwise }\end{cases}
$$

where $\operatorname{pol}_{l}(\mathbf{x})$ is a multivariate polynomial function with degree $d$ (and order $r=$ $d+1)$ and $A_{1}, \ldots, A_{L}$ are disjoint hyperrectangles in $\Omega_{\mathbf{X}}$, which do not depend on $\mathbf{x}$ and with $\Omega_{\mathbf{X}}=\cup_{l=1}^{L} A_{l}, d$ is defined as the maximum degree of any multivariate monomial for all $l=1, \ldots, L$.

If $\varphi_{\mathbf{X}}(\mathbf{x}) \geq 0$ and $\int_{\Omega_{\mathbf{X}}} \varphi_{\mathbf{X}}(\mathbf{x}) d \mathbf{x}=1$, then $\varphi_{\mathbf{X}}$ is said to be a density. We say that $\varphi_{X_{1} \mid \mathbf{X}^{\prime}}\left(x_{1} \mid \mathbf{x}^{\prime}\right)$ is a conditional density for $X_{1}$ given $\mathbf{x}^{\prime}=\left(x_{2}, \ldots, x_{n}\right)$ if $\varphi_{X_{1} \mid \mathbf{X}^{\prime}}\left(x_{1} \mid \mathbf{x}^{\prime}\right) \geq$ 0 and $\int_{\epsilon_{1}}^{\xi_{1}} \varphi_{\mathbf{X}}\left(x_{1}, \mathbf{x}^{\prime}\right) d x_{1}=1$ for all $\mathbf{x}^{\prime} \in \Omega_{\mathbf{X}^{\prime}}=\left[\epsilon_{2}, \xi_{2}\right] \times \ldots \times\left[\epsilon_{n}, \xi_{n}\right]$.

Example. The following $\varphi_{\mathbf{X}}\left(x_{1}, x_{2}, x_{3}\right)$ is an example of an MoPapproximation with $L=4$ pieces and degree $d=7$ defined for $\mathbf{X}=\left(X_{1}, X_{2}, X_{3}\right)$ in the closed domain $\Omega_{\mathbf{X}}=[-4,4] \times[-4,4] \times[-4,4] \subset \mathbb{R}^{3}$ :

$$
\begin{aligned}
& \varphi_{\mathbf{X}}\left(x_{1}, x_{2}, x_{3}\right) \\
& = \begin{cases}a x_{1}^{2} x_{2} x_{3}^{2} & \text { for }-4 \leq x_{1} \leq 0,-4 \leq x_{2} \leq 0,-4 \leq x_{3} \leq 4 \\
b x_{1}^{4} x_{2} x_{3}^{2}+c x_{3}^{3} & \text { for }-4 \leq x_{1} \leq 0,0<x_{2} \leq 4,-4 \leq x_{3} \leq 4 \\
d x_{1}^{5} x_{3} & \text { for } 0<x_{1} \leq 4,-4 \leq x_{2} \leq 0,-4 \leq x_{3} \leq 4 \\
e x_{2}^{2} x_{3}^{3} & \text { for } 0<x_{1} \leq 4,0<x_{2} \leq 4,-4 \leq x_{3} \leq 4 \\
0 & \text { otherwise }\end{cases}
\end{aligned}
$$

where $a, b, c, d, e \in \mathbb{R}$.

# 2.2. Learning MoPs Using B-Spline Interpolation 

Shenoy and West found MoP approximations of known parametric univariate probability density functions $f_{X}(x)$ by using two methods: (a) computing the Taylor series expansion (TSE) ${ }^{1}$ around the middle point of each subinterval $A_{l_{X}}$ in the MoP and (b) estimating $\operatorname{pol}_{l_{X}}(x)$ as the Lagrange interpolation (LI) ${ }^{2}$ over the Chebyshev points defined in $A_{l_{X}}$. Method (a) requires the mathematical expression of the probability density $f_{X}(x)$, whereas method (b) requires the true probability densities of the Chebyshev points in each $A_{l_{X}}$. Moreover, TSE cannot ensure that MoP approximations are valid densities, that is, they are nonnegative and integrate to one,

and although LI can ensure nonnegativity it cannot ensure that the resulting MoP integrates to one.

In López-Cruz et al., ${ }^{13}$ a new proposal for learning MoP approximations of oneand multidimensional probability densities from data using B-spline interpolation does not assume any prior knowledge about the true density. It ensures that the resulting MoP approximation is nonnegative and integrates to one and provides maximum likelihood estimators of some parameters. Additionally, it ensures that the obtained densities are continuous, which can be advantageous in some scenarios, for example, for visual analysis or expert validation.

B-splines or basis splines ${ }^{16}$ are polynomial curves that form a basis for the space of piecewise polynomial functions ${ }^{17}$ over a closed domain $\Omega_{X}=\left[\epsilon_{X}, \xi_{X}\right] \subset \mathbb{R}$. Given an increasing knot sequence (or split points) of $L_{X}+1$ real numbers $\delta_{X}=$ $\left\{a_{0}, a_{1}, \ldots, a_{L_{X}}\right\}$ in the approximation domain $\Omega_{X}=\left[\epsilon_{X}, \xi_{X}\right]$ with $a_{i-1}<a_{i}, \epsilon_{X}=$ $a_{0}$ and $\xi_{X}=a_{L_{X}}$, one can define $M_{X}=L_{X}+r_{X}-1$ different B-splines with order $r_{X}$ spanning the whole domain $\Omega_{X}$. The $j_{X}$ th B-spline $B_{X, j_{X}}^{r_{X}}(x), j_{X}=1, \ldots, M_{X}$, is

$$
\begin{aligned}
B_{X, j_{X}}^{r_{X}}(x)= & \left(a_{j_{X}}-a_{j_{X}-r_{X}}\right) H\left(x-a_{j_{X}-r_{X}}\right) \sum_{t=0}^{r_{X}} \\
& \times \frac{\left(a_{j_{X}-r_{X}+t}-x\right)^{r_{X}-1} H\left(a_{j_{X}-r_{X}+t}-x\right)}{w_{j_{X}-r_{X}}^{\prime}\left(a_{j_{X}-r_{X}+t}\right)}, \quad x \in \Omega_{X}
\end{aligned}
$$

where $w_{j_{X}-r_{X}}^{\prime}(x)$ is the first derivative of $w_{j_{X}-r_{X}}(x)=\prod_{u=0}^{r_{X}}\left(x-a_{j_{X}-r_{X}+u}\right)$ and $H(x)$ is the Heaviside function

$$
H(x)= \begin{cases}1 & x \geq 0 \\ 0 & x<0\end{cases}
$$

A B-spline $B_{X, j_{X}}^{r_{X}}(x)$ can be written as an MoP function with $L_{X}$ pieces, where each piece $p o l_{l_{X}}(x)$ is defined as the expansion of Equation (2) in the interval $A_{l_{X}}=$ $\left[a_{l_{X}-1}, a_{l_{X}}\right), l_{X}=1, \ldots, L_{X}$. B-splines have a number of interesting properties ${ }^{18}$ for approximating probability densities, for example, $B_{X, j_{X}}^{r_{X}}(x)$ is right-side continuous, differentiable, positive in and zero outside $\left(a_{j_{X}}, a_{j_{X}-r_{X}}\right)$.

Zong ${ }^{19}$ proposed using B-spline interpolation to find an approximation of the one-dimensional density $f_{X}(x)$ as a linear combination of $M_{X}=L_{X}+r_{X}-1$ B-splines

$$
\varphi_{X}(x ; \boldsymbol{\alpha})=\sum_{j_{X}=1}^{M_{X}} \alpha_{j_{X}} B_{X, j_{X}}^{r_{X}}(x), \quad x \in \Omega_{X}
$$

where $\boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{M_{X}}\right)$ are the mixing coefficients and $B_{X, j_{X}}^{r_{X}}(x), j_{X}=1, \ldots, M_{X}$ are B-splines with order $r_{X}$ (degree $d_{X}=r_{X}-1$ ) as defined in Equation (2).

Therefore, the MoP defined using B-spline interpolation requires four kinds of parameters: the order $\left(r_{X}\right)$, the number of intervals/pieces $\left(L_{X}\right)$, the knot sequence $\left(\delta_{X}\right)$ and the mixing coefficients $(\boldsymbol{\alpha})$. In López-Cruz et al., ${ }^{13}$ we used uniform B-splines, that is, equal width intervals $A_{l_{X}}$, to determine the knots in $\delta_{X} . r_{X}$ and $L_{X}$ were found by trying different values and selecting those with the highest BIC score (see Section 3.3). We used the Zong's ${ }^{19}$ iterative procedure for computing the maximum likelihood estimators of the mixing coefficients, $\hat{\alpha}$.

Zong and Lam's ${ }^{20}$ and Zong's ${ }^{19}$ methods for two-dimensional densities were extended in López-Cruz et al. ${ }^{13}$ to general $n$-dimensional joint probability density functions. Given a vector of $n$ random variables $\mathbf{X}=\left(X_{1}, \ldots, X_{n}\right)$, the joint probability density function $f_{\mathbf{X}}(\mathbf{x})$ is approximated with a multidimensional linear combination of B-splines:

$$
\begin{gathered}
\varphi_{\mathbf{X}}(\mathbf{x} ; \boldsymbol{\alpha})=\sum_{j_{X_{1}}=1, \ldots, M_{X_{1}}} \alpha_{j_{X_{1}}, \ldots, j_{X_{n}}} \prod_{i=1}^{n} B_{X_{i}, j_{X_{i}}}^{r_{X_{i}}}\left(x_{i}\right), \quad \mathbf{x} \in \Omega_{\mathbf{X}} \\
\vdots \\
j_{X_{n}}=1, \ldots, M_{X_{n}}
\end{gathered}
$$

where $r_{X_{i}}$ is the order of the B-splines for variable $X_{i}, M_{X_{i}}=L_{X_{i}}+r_{X_{i}}-1$ is the number of B-splines for variable $X_{i}, L_{X_{i}}$ is the number of pieces for variable $X_{i}$, and $\alpha_{j_{X_{1}}, \ldots, j_{X_{n}}}$ is the mixing coefficient for the combination of B-splines given by the indices $j_{X_{1}}, \ldots, j_{X_{n}}$.

Thus, the multidimensional MoP requires four kinds of parameters: the number of intervals $\left(L_{X_{1}}, \ldots, L_{X_{n}}\right)$, the order of the polynomials $\left(r_{X_{1}}, \ldots, r_{X_{n}}\right)$, the knot sequence $\left(\delta_{\mathbf{X}}\right)$, and the mixing coefficients $(\boldsymbol{\alpha})$. In López-Cruz et al., ${ }^{13}$ we used the multidimensional knots given by the Cartesian product of the knot sequences of each dimension $\boldsymbol{\delta}_{\mathbf{X}}=\boldsymbol{\delta}_{X_{1}} \times \cdots \times \boldsymbol{\delta}_{X_{n}}$, where $\boldsymbol{\delta}_{X_{i}}$ correspond to equal width intervals as in the one-dimensional case. Similarly, the mixing coefficient vector has one value for each combination of one-dimensional B-splines, that is, $\boldsymbol{\alpha}=\left(\alpha_{1, \ldots, 1}, \ldots, \alpha_{M_{X_{1}}, \ldots, M_{X_{n}}}\right)$. The resulting MoP has $L=\prod_{i=1}^{n} L_{X_{i}}$ pieces, where each piece $p o l_{l_{X_{1}}, \ldots, l_{X_{n}}}(\mathbf{x})$ is defined in an $n$-dimensional hyperrectangle $A_{l_{X_{1}}, \ldots, l_{X_{n}}}=\left[a_{l_{X_{1}}-1}, a_{l_{X_{1}}}\right] \times \cdots \times\left[a_{l_{X_{n}}-1}, a_{l_{X_{n}}}\right]$.

# 3. LEARNING CONDITIONAL DISTRIBUTIONS 

Given a sample $\mathcal{D}_{X, \mathbf{Y}}=\left\{\left(x_{i}, \mathbf{y}_{i}\right), i=1, \ldots, N\right\}$, from the joint density of $(X, \mathbf{Y})$, the aim is to learn an MoP approximation $\varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$ of the conditional density $f_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$ of $X \mid \mathbf{Y}$ from $\mathcal{D}_{X, \mathbf{Y}}$. Following the terminology used for BNs, we consider the conditional random variable $X$ as the child variable and the vector of conditioning random variables $\mathbf{Y}=\left(Y_{1}, \ldots, Y_{n}\right)$ as the parent variables.

# 3.1. Learning Conditional MoPs Using Sampling 

The proposed method is based on first obtaining a sample from the conditional density of $X \mid \mathbf{Y}$ and then learning a conditional MoP density from the sampled values. Algorithm 1 shows the main steps of the procedure.

## Algorithm 1.

Input: A training data set $\mathcal{D}_{X, \mathbf{Y}}=\left\{\left(x_{i}, \mathbf{y}_{i}\right), i=1, \ldots, N\right\}$.
Output: $\varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$, the MoP approximation of the density of $X \mid \mathbf{Y}$. Steps:

1. Learn an $\operatorname{MoP} \varphi_{X, \mathbf{Y}}(x, \mathbf{y})$ of the joint density of $(X, \mathbf{Y})$ from the data set $\mathcal{D}_{X, \mathbf{Y}}$ using the algorithm in López-Cruz et al. ${ }^{13}$
2. Marginalize out $X$ from $\varphi_{X, \mathbf{Y}}(x, \mathbf{y})$ to yield an $\operatorname{MoP} \varphi_{\mathbf{Y}}(\mathbf{y})$ of the marginal density of the parent variables $\mathbf{Y}: \varphi_{\mathbf{Y}}(\mathbf{y})=\int_{\Omega_{X}} \varphi_{X, \mathbf{Y}}(x, \mathbf{y}) d x$.
3. Use the Metropolis-Hastings algorithm (Algorithm 2) to produce a sample $\mathcal{D}_{X \mid \mathbf{Y}}$ from a density proportional to the conditional density $\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$.
4. Find an unnormalized conditional $\operatorname{MoP} \varphi_{X \mid \mathbf{Y}}^{(u)}(x \mid \mathbf{y})$ based on $\mathcal{D}_{X \mid \mathbf{Y}}$ and using the algorithm in López-Cruz et al. ${ }^{13}$
5. Partially normalize the conditional MoP $\varphi_{X \mid \mathbf{Y}}^{(u)}(x \mid \mathbf{y})$ to make it integrate the Lebesgue measure of the $\mathbf{Y}$ domain (as the true conditional density).

First, we find an MoP representation of the joint density $\varphi_{X, \mathbf{Y}}(x, \mathbf{y})$ (step 1) using the B-spline interpolation approach proposed in López-Cruz et al. ${ }^{13}$ and reviewed in Section 2. Second, we obtain an MoP of the marginal density of the parents $\varphi_{\mathbf{Y}}(\mathbf{y})$ by marginalization (step 2). Next, we use a sampling algorithm to obtain a sample $\mathcal{D}_{X \mid \mathbf{Y}}$ from a distribution proportional to the conditional density of $X \mid \mathbf{Y}$ (step 3), where the conditional density values are obtained by evaluating the quotient $\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$. More specifically, we have used a standard MetropolisHastings sampler for the reported experimental results, as specified in Algorithm 2. Finally, we find an MoP approximation, $\varphi_{X \mid \mathbf{Y}}^{(u)}(x \mid \mathbf{y})$, from data set $\mathcal{D}_{X \mid \mathbf{Y}}$ (step 4). The $\operatorname{MoP} \varphi_{X \mid \mathbf{Y}}^{(u)}(x \mid \mathbf{y})$ is an approximation of a proper density that is proportional to the conditional density $f_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$. To normalize it, we know that

$$
\int_{\Omega_{X} \times \Omega_{\mathbf{Y}}} f_{X \mid \mathbf{Y}}(x \mid \mathbf{y}) \mathrm{d} x \mathrm{~d} y=\int_{\Omega_{\mathbf{Y}}} 1 \mathrm{~d} y=\left|\Omega_{\mathbf{Y}}\right|
$$

Consequently, to find the partial normalization constant, we can impose the analogous constraint to the approximating MoP. In particular, we find $K$ such that

$$
\frac{1}{K} \int_{\Omega_{X} \times \Omega_{\mathbf{Y}}} \varphi_{X \mid \mathbf{Y}}^{(u)}(x \mid \mathbf{y}) \mathrm{d} x \mathrm{~d} y=\left|\Omega_{\mathbf{Y}}\right|
$$

and set $\varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})=\frac{1}{K} \varphi_{X \mid \mathbf{Y}}^{(u)}(x \mid \mathbf{y})$ as the approximating MoP of the conditional density $f_{X \mid \mathbf{Y}}(x \mid \mathbf{y})($ step 5$)$.

For the sampling process described in Algorithm 2, we generate uniformly distributed values over $\Omega_{\mathbf{Y}}$ for the parent variables $\mathbf{Y}$, whereas we use a Gaussian distribution $Q\left(x_{\text {new }} ; x\right) \equiv \mathcal{N}(x, \sigma)$ as proposal distribution for the child variable; in

the experiments we set $\sigma^{2}=0.5$. The Metropolis-Hastings algorithm is a Markov Chain Monte Carlo method, that is, it is based on building a Markov chain that has as stationary distribution the one we would like to sample from. Consequently, we have to wait (termed the burn in period) until the Markov chain is close to its stationary distribution before sampling from it. This is the purpose of discarding the first $h$ values. Another consequence of the Metropolis-Hastings algorithm is the correlation that may be present between near sampled values, which follows from the Markov chain assumption. This is partially avoided by setting a jumping width, $h^{\prime}$.

# Algorithm 2. 

Input: $\varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$, an approximation to the conditional density of $X \mid \mathbf{Y}$.
Output: $\mathcal{D}_{X \mid \mathbf{Y}}$ a sample of a distribution, with density proportional to the conditional density $\varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$. Steps:

1. Initialize $x=x_{0}, \mathbf{y}=\mathbf{y}_{0}$.
2. Generate a candidate $\left(x_{--}, y_{\text {new }}\right)$ from the product of a proposal distribution for the $X_{\text {new }}$ variable, $Q\left(X_{\text {new }} ; x\right)$, and an independent uniform distribution for $\mathbf{y}_{\text {new }}$.
3. Calculate the acceptance ratio $t=\varphi_{X \mid \mathbf{Y}}\left(x_{\text {new }} \mid \mathbf{y}_{\text {new }}\right) / \varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$.
4. if $t \geq u$, where $u$ is a realization from a uniform distribution in $[0,1]$, the candidate is accepted and we set $(x, \mathbf{y})=\left(x_{\text {new }}, \mathbf{y}_{\text {new }}\right)$, otherwise the candidate is rejected and the old values $(x, \mathbf{y})$ are kept.
5. Repeat from step 1, discarding the first $h$ values generated and storing the following values, one every $h^{\prime}$ repetitions.

The proposed method has some interesting properties. The B-spline interpolation algorithm for learning MoPs in López-Cruz et al. ${ }^{13}$ guarantees that the approximations are continuous, nonnegative, and integrate to one. Therefore, the conditional MoPs obtained using Algorithm 1 are also continuous and nonnegative. Continuity is not required for inference in BNs, but it is usually a desirable property, for example, for visualization purposes. The algorithm provides maximum likelihood estimators of the mixing coefficients of the linear combination of the B-splines when learning MoPs of the joint density $\varphi_{X \mathbf{Y}}(x, \mathbf{y})$ and the marginal density $\varphi_{\mathbf{y}}(\mathbf{y})$. Hence, the quotient $\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$ corresponds to a maximum likelihood model of the conditional distribution. It should be noted, though, that this property is not shared by the model learned in step 4, that is, it is not necessarily a maximum likelihood model. Furthermore, since the partial normalization (step 5) does not ensure that the learned MoP is a proper conditional density, the posterior densities may need to be normalized to integrate to one during inference.

### 3.2. Learning Conditional MoPs Using Interpolation

The preliminary empirical results provided by Algorithm 1 show that the sampling approach can produce good approximations. However, it is difficult to control or guarantee the quality of the approximation due to the sampling procedure and the partial normalization in the last step.

This shortcoming has motivated an alternative method for learning an MoP approximation of a conditional probability density for $X \mid \mathbf{Y}$. The main steps of the

procedure are summarized in Algorithm 3. First, we find MoP approximations of both the joint density of $(X, \mathbf{Y})$ and the marginal density of $\mathbf{Y}$ following the same procedure as in Algorithm 1 (steps 1 and 2). Next, we build the conditional MoP $\varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$ by finding, for each piece $\operatorname{pol}_{l}(x, \mathbf{y})$ defined in the hyperrectangle $A_{l}$, a multidimensional interpolation polynomial of the function given by the quotient of the joint and the marginal densities $\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$.

# Algorithm 3. 

Input: A training data set $\mathcal{D}_{X, \mathbf{Y}}=\left\{\left(x_{i}, \mathbf{y}_{i}\right), i=1, \ldots, N\right\}$.
Output: $\varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$, the MoP approximation of the density of $X \mid \mathbf{Y}$. Steps:

1. Find an MoP $\varphi_{X, \mathbf{Y}}(x, \mathbf{y})$ of the joint density of the variables $X$ and $\mathbf{Y}$ from the data set $\mathcal{D}_{X, \mathbf{Y}}$ using the method in López-Cruz et al. ${ }^{13}$
2. Marginalize out $X$ from $\varphi_{X, \mathbf{Y}}(x, \mathbf{y})$ to obtain an $\operatorname{MoP} \varphi_{\mathbf{Y}}(\mathbf{y})$ of the marginal density of the parent variables $\mathbf{Y}: \varphi_{\mathbf{Y}}(\mathbf{y})=\int_{\Omega_{X}} \varphi_{X, \mathbf{Y}}(x, \mathbf{y}) d x$.
3. For piece $\operatorname{pol}_{l}(x, \mathbf{y})$, defined in $A_{l}, l=1, \ldots, L$, in the conditional MoP $\varphi_{X \mid \mathbf{Y}}(x \mid \mathbf{y})$ : Find a multidimensional polynomial approximation of the function $g(x, \mathbf{y})=$ $\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$ using an interpolation method with polynomial degree equal to the degree of the MoP of the joint density.

We consider two multidimensional interpolation methods to obtain the polynomials of the pieces $\operatorname{pol}_{l}(x, \mathbf{y})$ in step 3 of Algorithm 3:

- The multidimensional TSE for a point yields a polynomial approximation of any differentiable function $g$. The quotient of any two functions is differentiable as long as the two functions are also differentiable and the denominator is not zero. In our scenario, polynomials are differentiable functions and, thus, we can compute the TSE of the quotient of two polynomials. Consequently, we can use multidimensional TSEs to find a polynomial approximation of $g(x, \mathbf{y})=\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$ for each piece $\operatorname{pol}_{l}(x, \mathbf{y})$. We computed these TSEs of $g(x, \mathbf{y})$ for the midpoint of the hyperrectangle $A_{l}$.
- LI finds a polynomial approximation of any function $g$. Before finding the LI polynomial, we need to evaluate function $g$ on a set of interpolation points. In the one-dimensional scenario, Chebyshev points are frequently used as interpolation points. ${ }^{21}$ However, multidimensional LI is not a trivial task because it is difficult to find good interpolation points in a multidimensional space. Some researchers have recently addressed the twodimensional scenario. ${ }^{21,22}$ To find a conditional MoP using LI, we first find and evaluate the conditional density function $g(x, \mathbf{y})=\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$ on the set of interpolation points in $A_{l}$. Next, we compute the polynomial $\operatorname{pol}_{l}(x, \mathbf{y})$ for the piece as the LI polynomial over the interpolation points defined in $A_{l}$. Note that other approaches, for example, kernel-based conditional estimation methods, can also be used to evaluate the conditional density $g(x, \mathbf{y})$ on the set of interpolation points.

Compared with Algorithm 1, there are some apparent (dis)advantages. First, the conditional MoPs produced by Algorithm 3 are not necessarily continuous. Second, interpolation methods cannot in general ensure nonnegativity, although LI can be used to ensure it by increasing the order of the polynomials. On the other hand, the learning method in Algorithm 3 does not need a partial normalization (step 2). Thus, if the polynomial approximations are close to the conditional density $\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$, then the conditional MoP using these polynomial interpolations is expected to be close to normalized. As a result, we can more directly control the quality of the approximation by varying the degree of the polynomials and the

number of hyperrectangles. It should be observed that both Algorithms 1 and 3 output MoPs approximations, but the approximations are built differently and lead to different models. Algorithm 1 uses B-spline interpolation and so the number of parameters in the resulting models is

$$
\left(L_{X}+r_{X}-1\right) \prod_{i=1}^{n}\left(L_{Y_{i}}+r_{Y_{i}}-1\right)
$$

On the other hand, Algorithm 3 builds MoPs that are not necessarily continuous and therefore more general. The number of parameters in the learned models is

$$
r_{X} L_{X} \prod_{i=1}^{n} L_{Y_{i}} r_{Y_{i}}
$$

# 3.3. Heuristic to Search for a Good MoP Approximation 

Steps 1 and 4 in Algorithm 1 and step 1 in Algorithm 3 require finding an MoP approximation starting from a data set $\mathcal{D}_{X, \mathbf{Y}}$. The algorithm proposed in LópezCruz et al. ${ }^{13}$ provides a way to compute a multidimensional MoP approximation given a data set, the orders of the polynomials, and the pieces of the domains of approximation for each dimension. Here, we use a penalized likelihood-based search iterating over the algorithm in López-Cruz et al. ${ }^{13}$ to find the best MoP approximation for the data set $\mathcal{D}_{X, \mathbf{Y}}$. The method performs a simple greedy search for the optimal parameters. From now on, we will refer to those parameters as follows: $r$ is the order of the polynomials in each dimension, $L_{X}$ is the number of pieces for variable $X$, and $L_{Y}$ is the number of pieces for variable $Y$ (to simplify the presentation we assume a single parent variable). The algorithm starts from the initial point $\left(r, L_{X}, L_{Y}\right)=(2,1,1)$, computes the MoP with these parameters, and compares its BIC score to those of the nearest neighbor solutions: $\left(r+1, L_{X}, L_{Y}\right),\left(r, L_{X}+\right.$ $\left.1, L_{Y}\right),\left(r, L_{X}, L_{Y}+1\right)$, and $\left(r, L_{X}+1, L_{Y}+1\right)$. The parameters $\left(r, L_{X}, L_{Y}\right)$ are updated to the best ones and the steps are iterated until no improvement in BIC score is achieved or the parameters $\left(r, L_{X}, L_{Y}\right)$ reach some user predefined boundaries. Algorithm 4 lists the steps of this heuristic search.

## Algorithm 4.

Input: A training data set $\mathcal{D}_{X, Y}=\left\{\left(x_{i}, y_{i}\right), i=1, \ldots, N\right\}$.
Output: $\varphi_{X, Y}(x, y)$, the MoP approximation of the density of $(X, Y)$.
Steps:

1. Set $r=2$ and $L_{X}=L_{Y}=1$.
2. Calculate, using the method given in López-Cruz et al., ${ }^{13}$ MoP approximations given the data set $\mathcal{D}_{X, Y}$ with the following parameters:

- $\left(r, L_{X}, L_{Y}\right)$.
- $\left(r+1, L_{X}, L_{Y}\right)$.
- $\left(r, L_{X}+1, L_{Y}\right)$.

- $\left(r, L_{X}, L_{Y}+1\right)$.
- $\left(r, L_{X}+1, L_{Y}+1\right)$.
3. Compute the BIC score of the five MoPs computed in the previous step with the data set $\mathcal{D}_{X, Y}$.
4. Select the MoP with the highest BIC score and update $r, L_{X}$, and $L_{Y}$ to their parameters.
5. Repeat from step 2 until there is no gain in the BIC score or the maximum boundaries for the parameters are reached.

The BIC score ${ }^{23}$ is defined as

$$
\operatorname{BIC}\left(\varphi_{X, Y}(x, y), \mathcal{D}_{X, Y}\right)=\ell\left(\mathcal{D}_{X, Y} \mid \varphi_{X, Y}(x, y)\right)-\frac{\operatorname{dim}\left(\varphi_{X, Y}(x, y)\right) \log N}{2}
$$

where $\ell\left(\mathcal{D}_{X, Y} \mid \varphi_{X, Y}(x, y)\right)$ is the log-likelihood of the training data set $\mathcal{D}_{X, Y}$ given an MoP model $\varphi_{X, Y}(x, y), N$ is the number of observations in the data set $\mathcal{D}_{X, Y}$, and $\operatorname{dim}\left(\varphi_{X, Y}(x, y)\right)$ is the number of free parameters in the model encoding the split points and the coefficients in the polynomials.

The previous algorithm could be implemented with uniform knots or using data-dependent knots. In particular, it is possible to use empirical quantiles (i.e., an equal frequency rather than an equal width approach), calculated over the data set $\mathcal{D}_{X, Y}=\left\{\left(x_{i}, y_{i}\right), i=1, \ldots, N\right\}$.

Conceptually, the algorithm can also easily be extended to handle a multidimensional parent set $\mathbf{Y}$, but at the cost of a considerable increase in the computational complexity. Introducing a multidimensional parent set $\mathbf{Y}$ means that at each iteration of Algorithm 4, we have to compute an increasing number of candidate MoPs resulting in a corresponding increase in the computational cost: If at every iteration we select the best parameter set among all possible combinations of parameters, the number of MoP computations increases exponentially with the size of $\mathbf{Y}$. As an alternative, one may attempt to devise heuristic-based search strategies or constrain the parameter combinations. However, even if this approach would turn out successful we still have to face the fact that Algorithm 4 uses the procedure described in López-Cruz et al. ${ }^{13}$ to compute multidimensional MoPs and this procedure is not immediately scalable. In summary, to ensure scalability a new algorithm for computing multidimensional MoPs might be developed and more efficient search strategies should be deployed.

# 3.4. Illustrative Examples 

We apply the proposed algorithms to three examples, all of them are thought of as graphical models with two variables, a parent $Y$ and a child $X$. In the first example, we consider a joint Gaussian distribution, $(X, Y) \sim \mathcal{N}\left(\left(\begin{array}{l}0 \\ 0\end{array}\right),\left(\begin{array}{ll}2 & 1 \\ 1 & 1\end{array}\right)\right)$. This two-dimensional density corresponds to a Gaussian BN, where $Y \sim \mathcal{N}(0,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$.

In the second example, we consider $Y$ distributed as a gamma distribution with rate $=10$ and shape $=10$, and $X$ distributed, conditionally to $Y=y$, as an exponential distribution with rate $=y$.

a $Y \sim \mathcal{N}(0,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$
![img-0.jpeg](img-0.jpeg)
b $Y \sim$ Gamma(rate $=10$, shape $=10)$ and $X \mid Y \sim \operatorname{Exp}(y)$
![img-1.jpeg](img-1.jpeg)
c $Y \sim 0.5 \mathcal{N}(-3,1)+0.5 \mathcal{N}(3,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$
![img-2.jpeg](img-2.jpeg)

Figure 1. For the three examples (in rows), true conditional density and MoP approximation obtained using Algorithm 1 (second column) and Algorithm 3 with LI (third column), case $N=5000$.

In the third example, we model $Y$ as a mixture of two Gaussian distributions, $Y \sim 0.5 \mathcal{N}(-3,1)+0.5 \mathcal{N}(3,1)$. The distribution of $X$, conditioned on $Y=y$, is considered a Gaussian with mean $y$ and unit variance, that is, $X \mid Y \sim \mathcal{N}(y, 1)$.

For each model, we generate sets of $10(X, Y)$ samples of length equal to $N=$ $25,500,2500,5000$. For each example, we apply the two algorithms (Algorithms 1 and 3) to approximate the conditional density (see Figure 1 for $N=5000$ ). In Algorithm 2, we set the parameters $h$ and $h^{\prime}$ to 1000 and 3 samples, respectively,

Table I. Mean MSE between the MoP approximations and the true conditional densities for 10 data sets sampled from the BN, where $Y \sim \mathcal{N}(0,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$. Mean order $r$ and mean number of pieces in the $X$ and $Y$ domains $L_{X}, L_{Y}$ are also reported.


and in Algorithm 4, we set the boundaries artificially high so that they are not reached.

To check the goodness of the learned MoP, we evaluate the mean square error (MSE) between the approximated conditional densities $\varphi_{X \mid Y}(x \mid y)$ and the true one $f_{X \mid Y}(x \mid y)$, for three values of $y_{0}$, corresponding to the percentiles 25,50 , and 75 of the distribution of $Y$. The results can be found in Tables I-III. The comparison is done without normalizing the approximated conditional densities $\varphi_{X \mid Y}\left(x \mid y_{0}\right)$, hence Kullback-Leibler (KL) divergence cannot be used as an evaluation measure.

The results in Tables I and II show that Algorithms 1 and 3 perform similarly with respect to the Gaussian model, but Algorithm 3 achieves better results with respect to the exp-gamma model. The results in Table III show that even in the more complex mixture model, the proposed algorithms perform quite well with respect to the mean squared errors. Moreover, with respect to the complexity of the learned MoPs, we can see that the algorithms deal with the increasing complexity by learning MoPs with more pieces instead of MoPs with higher orders. The main problem with Algorithm 1 is the partial normalization step and the loose link between the MoP approximation for the joint density (step 1) and the MoP approximation of the conditional density (steps 4 and 5).

Next, we perform inference based on the MoP learned with the algorithms. We compute the posterior density of $Y \mid X$ and compare it with the true one (Figures 2-4). The comparison is done based on the MSE and the KL divergence. The posterior density is calculated conditional on nine different values for the child variable, corresponding to the percentiles $10,20,30,40,50,60,70,80$, and 90 . The results of the comparison are shown in Tables IV-IX.

For both algorithms, we cannot ensure that the approximated conditional densities, $\varphi_{X \mid Y}\left(x \mid y_{0}\right)$, integrate to one for every $y_{0}$. This is not necessarily a problem when doing inference, though, as one may perform an additional normalization step to obtain proper densities.

Table II. Mean MSE between the MoP approximations and the true conditional densities for 10 data sets sampled from the BN, where $Y \sim$ Gamma (rate $=10$, shape $=10$ ) and $X \mid Y \sim$ $\operatorname{Exp}(y)$. Mean order $r$ and mean number of pieces in the $X$ and $Y$ domains $L_{X}, L_{Y}$ are also reported.


Table III. Mean MSE between the MoP approximations and the true conditional densities for 10 data sets sampled from the BN, where $Y \sim 0.5 \mathcal{N}(-3,1)+0.5 \mathcal{N}(3,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$. Mean order $r$ and mean number of pieces in the $X$ and $Y$ domains $L_{X}, L_{Y}$ are also reported.


To compare the algorithms, we apply a paired Wilcoxon signed-rank test. For every pair of algorithms, for every $N$, and for every fixed value $x_{o b s}$ of the conditioning variable, we run a Wilcoxon signed-rank over the results of the comparison between the approximated posterior density and the true posterior density. The results are reported in Table X. We list the number of cases in which the algorithm on the left significantly outperforms (significance level $\alpha=0.05$ ) the algorithm on the top. Recall that the total number of cases is 36 for each of the data sets ( 4 values for $N$ and 9 quantiles corresponding to the $x_{o b s}$ values).

With respect to the posterior density approximation, the results of the Wilcoxon signed-rank test based on KL divergence indicate that Algorithm 1 outperforms Algorithm 3 using LI in the exp-gamma model (Table X). This is shown in Figure 3. However, for the Gaussian model, Algorithm 3 achieves statistically significant better results with respect to KL (Table X) in some cases. The mixture model is the one that shows the greatest difference between the two algorithms (Table X and Figure 4 ). From the results of the Wilcoxon signed-rank test with respect to the mixture model, we see that Algorithm 3 outperforms Algorithm 1 in almost one-third of the cases (Table X). When looking closer at the results (Tables VIII and IX), we observe that Algorithm 3 achieves better results for the largest sample cases $(N=5000)$, where, according to the Wilcoxon signed-rank tests, Algorithm 3 outperforms Algorithm 1 for every value of the child variable. In comparison, the cases for which Algorithm 1 outperforms Algorithm 3 are mainly found when dealing with smaller data sets $(N=25,500)$.

Note that Algorithm 1 is computationally more costly than Algorithm 3 due to the use of Algorithm 4 in two steps. From Figures 2 and 3, we also see that Algorithm 3 provides posterior densities that are almost continuous in the two first simpler models. In the mixture model, however, the TSE variant of Algorithm 3 outputs MoP approximations of conditional densities, which show strong discontinuities in the form of high peaks. Those errors are due to approximation faults in the computations of the ratio between the joint and the marginal distributions in step 3 of Algorithm 3. These errors are not observed using interpolation over Padua points.

On the basis of previous observations over the artificial examples as well as the theoretical properties of the algorithms proposed, we suggest that:

- when dealing with small data sets and when requiring continuous densities, the use of Algorithm 1 provides better results;
- in case of large data sets, Algorithm 3 using interpolation over Padua point is to be preferred; it outputs almost continuous MoPs and is generally faster than Algorithm 1.


# 4. A COMPARISON WITH MoTBFs 

In this section, we compare the two proposed learning methods with the method described in Langseth et al. ${ }^{11}$ for learning conditional MoTBFs from data. The MoTBF-based learning method relies on a kernel density estimate representation of the data, which is subsequently translated into an MoTBF representation. In the limit, it can be shown that the learned/translated MoTBF parameters converge to the maximum likelihood parameters.

Figure 5 shows the MoTBFs of the conditional (a) and the posterior (c,d,e) densities approximated using the first data described in Section 3.4. The conditional MoTBF has six pieces and each piece defines an MoP with at most six parameters; polynomial basis functions are used in all the experiments. MoTBF approximations of conditional densities are obtained by discretizing the parent variables and fitting a one-dimensional MoTBF for each hyperrectangle defined by the split points of the parents. Compared with the two learning methods proposed in Algorithms 1 and 3, the method in Langseth et al. ${ }^{11}$ therefore captures the correlation between the parent

![img-3.jpeg](img-3.jpeg)

Figure 2. True posterior densities (red dashed) and approximated one (solid blue) for $Y \sim \mathcal{N}(0,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$, case $N=5000$.

![img-4.jpeg](img-4.jpeg)

Figure 3. True posterior densities (red dashed) and approximated one (solid blue) for $Y \sim$ Gamma (rate $=10$, shape $=10$ ) and $X \mid Y \sim \operatorname{Exp}(y)$, case $N=5000$.

![img-5.jpeg](img-5.jpeg)

Figure 4. True posterior densities (red dashed) and approximated one (solid blue) for $Y \sim 0.5 \mathcal{N}(-3,1)+0.5 \mathcal{N}(3,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$, case $N=$ 5000 .

![img-6.jpeg](img-6.jpeg)

Figure 5. Example of $Y \sim \mathcal{N}(0,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$, case $N=5000$. (a) Conditional MoTBF of $X \mid Y$ learned with the approach in. ${ }^{11}$ (b) True conditional density of $X \mid Y \sim \mathcal{N}(y, 1)$. (c,d,e) MoTBF approximations (solid) and true posterior densities (dashed) of $Y \mid X$ for three values of $X$.

Table IV. Comparison between the true posterior density and the one learned with the MoP approximation obtained using Algorithm 1. Mean KL and MSE for 10 data sets sampled from the BN, where $Y \sim \mathcal{N}(0,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$.


Table V. Comparison between the true posterior density and the one learned with the MoP approximation obtained using Algorithm 3 and Lagrange interpolation. Mean KL and MSE for 10 data sets sampled from the BN, where $Y \sim \mathcal{N}(0,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$.


Table VI. Comparison between the true posterior density and the one learned with the MoP approximation obtained using Algorithm 1. Mean KL and MSE for 10 data sets sampled from the BN, where $Y \sim$ Gamma $(\operatorname{rate}=10$, shape $=10)$ and $X \mid Y \sim \operatorname{Exp}(y)$.


variables and the child variable through the hyperrectangles instead of directly in the functional polynomial expressions. The selection of split-points and number of basis functions is guided by a greedy search strategy that optimizes the BIC score of the model by iteratively evaluating the BIC-gain of bisecting an existing candidate hyperrectangle and relearning the number of basis functions.

If there is a weak correlation between the child and parent variables, then the conditional MoTBF approach is expected to yield approximations with few pieces.

Table VII. Comparison between the true posterior density and the one learned with the MoP approximation obtained using Algorithm 3 with Lagrange interpolation. Mean KL and MSE for 10 data sets sampled from the BN, where $Y \sim$ Gamma $(\operatorname{rate}=10$, shape $=10)$ and $X \mid Y \sim \operatorname{Exp}(y)$.


Table VIII. Comparison between the true posterior density and the one learned with the MoP approximation obtained using Algorithm 1 . Mean KL and MSE for 10 data sets sampled from the BN, where $Y \sim 0.5 \mathcal{N}(-3,1)+0.5 \mathcal{N}(3,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$.


Table IX. Comparison between the true posterior density and the one learned with the MoP approximation obtained using Algorithm 3 with Lagrange interpolation. Mean KL and MSE for 10 data sets sampled from the BN, where $Y \sim 0.5 \mathcal{N}(-3,1)+0.5 \mathcal{N}(3,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$.


On the other hand, as the variables become more strongly correlated, additional subintervals will be introduced by the learning algorithm. The MoTBF learning algorithm does not rely on a discretization of the child variable, but it rather approximates the density using a higher-order polynomial/exponential function. In contrast, Algorithms 1 and 3 yield conditional MoPs with more pieces because the domain of approximation $\Omega_{X, \mathbf{Y}}$ is split into hyperrectangles in all the dimensions.

Table X. Results of the Wilcoxon signed-rank test.


Notes Roman results for KL and italic results for MSE.

However, with the finer-grained division of the domain into hyperrectangles, the polynomial functions of the conditional MoPs will usually also have a lower order.

We empirically compared Algorithms 1 and 3 (using both TSE and LI) to the method proposed in Langseth et al. ${ }^{11}$ by employing the greedy search strategy in Section 3.3 and using the three data sets described in Section 3.4.

Tables XI, XII, and XIII show the mean KL divergences and MSEs between the MoPs and the true posterior densities $Y \mid X$ for three values of $X$ in the 10 repetitions. We applied a paired Wilcoxon signed-rank test and report statistically significant differences at a significance level $\alpha=0.05$. The null hypothesis is that the two methods perform similarly. The alternative hypothesis is that the algorithm in the column outperforms the algorithm shown with a symbol: $\neq$ for Algorithm 1, $\dagger$ for Algorithm 3 with TSE, $\ddagger$ for Algorithm 3 with LI, and $\star$ for conditional MoTBFs. For instance, a $\star$ symbol in the column corresponding to Algorithm 1 in Table XI shows that Algorithm 1 significantly outperforms MoTBFs for the corresponding values for $N$ and $X$. From the gamma-exponential distribution (Table XII), we see that the models produced by Algorithms 1 and 3 are generally comparable to or slightly worse than those learned using the MoTBF-based method. However, when considering Table XI we see that Algorithm 3 significantly outperforms the MoTBFbased method, especially for the larger data sets. When further analyzing the models learned for the data sets with 5000 observations, we find that the learned MoTBF models contain at most six pieces each holding an MoP with at most six parameters (hence a total of 36 parameters, not counting the parameters defining the pieces). In comparison, Algorithm 3 produce models with 256 parameters ( 16 pieces each holding a polynomial of degree 3 in each variable) and Algorithm 1 outputs models with 49 parameters $(7=4+4-1$ parameters for each dimension). Thus, for these data sets the proposed learning algorithms seem to allow more complex models to be learned than when using the MoTBF approach. With respect to the mixture model

Table XI. Mean Kullback-Leibler divergences and MSE between the approximations and the true posterior densities for 10 data sets sampled from the BN, where $Y \sim \mathcal{N}(0,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$.


Notes The best results for each sample size are highlighted in bold. Statistically significant differences at $\alpha=0.05$ are shown with symbols $*, \dagger, \ddagger, \star$.

Table XII. Mean Kullback-Leibler divergences and MSE between the approximations and the true posterior densities for 10 data sets sampled from the BN, where $Y \sim$ Gamma $(\operatorname{rate}=10$, shape $=10)$ and $X \mid Y \sim \operatorname{Exp}(y)$.


Notes The best results for each sample size are highlighted in bold. Statistically significant differences at $\alpha=0.05$ are shown with symbols $*, \dagger, \ddagger, *$.

Table XIII. Mean Kullback-Leibler divergences and MSE between the approximations and the true posterior densities for 10 data sets sampled from the BN, where $Y \sim 0.5 \mathcal{N}(-3,1)+0.5 \mathcal{N}(3,1)$ and $X \mid Y \sim \mathcal{N}(y, 1)$.


Notes The best results for each sample size are highlighted in bold. Statistically significant differences at $\alpha=0.05$ are shown with symbols $+, \dagger, \ddagger, \star$.

![img-7.jpeg](img-7.jpeg)

Figure 6. Conditional density (top) and posterior densities ( $x=0.38$ left; $x=0.79$ middle; $x=1.50$ right) learned with Algorithm 1 in neuronal morphological data.

(Table XIII), we observe that the proposed algorithms outperform the MoTBF-based method both in the small data sets (Algorithm 1) and larger data sets (Algorithm 3).

# 5. A REAL-WORLD EXAMPLE IN NEUROANATOMY 

As a real-world example, we build a MoP model over some variables describing neurons by their morphological features. We use the database studied in Guerra et al., ${ }^{24}$ which addresses the problem of classifying a neuron based on its morphological features. The database is made up of 327 observations concerning 52 variables describing morphological and spatial neuron characteristics. We select the variable relative distance to pia as the parent variable $Y$, and the variable area of the dendrite's convex hull as the child $X$. The relative distance to pia is the ratio of the straight-line distance from soma to pia and the straight-line distance from white matter to pia. Thus, a value close to 0 (resp. 1) corresponds to a soma in a superficial (resp. deep) layer. Convex hull analysis draws a two-dimensional convex shape around the dendrites. The area $\left(\mu \mathrm{m}^{2}\right)$ of this shape is then calculated. Before applying our MoP approximations to $X \mid Y$, the data are divided by their sample standard deviation. Also, only $96 \%$ of the central values of the transformed data have been maintained; the remaining values have been discarded.

Since the data set considered is quite small and continuous densities are desirable for this particular domain, we apply Algorithm 1 for learning the MoP representations, (cf. the discussion in Section 3.4). The results are shown in Figure 6.

The conditional MoP of $X \mid Y$ in Figure 6 (top) shows that for small values of the distance to pia the dendrite areas are mostly concentrated around small values, whereas for larger distances the areas spread over more values, that is, dendrite areas present a higher dispersion when the neurons are further away from the pia. This MoP has $L_{X}=4$ and $L_{Y}=2$ pieces for $X$ and $Y$, respectively, each one with order 3. For the posterior distributions $Y \mid X$ in the bottom figures, for area $x=0.38$ (left) the distance to pia is asymmetrically distributed with a mode close to 1 , whereas for $x=1.50$ (right) the density is rather symmetric with a mode close to 2 .

## 6. CONCLUSIONS

In this paper, we have considered two methods for learning MoP approximations of conditional densities $X \mid \mathbf{Y}$ from data. The initializing step in both methods involves estimating the joint density $\varphi_{X, \mathbf{Y}}(x, \mathbf{y})$ and the marginal density of the parents $\varphi_{\mathbf{Y}}(\mathbf{y})$. In the first method, we use the two learned densities to obtain a sample from the quotient $\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$ based on which an unnormalized conditional MoP is learned. Proper normalization of the learned MoP is not feasible since the resulting potential would be outside the MoP model class, hence we instead resort to a partial normalization. Although the models obtained from the partial normalization can provide good accuracy results, it is difficult to control the quality of the approximation. This shortcoming has motivated the second learning algorithm,

where a conditional MoP is obtained using multidimensional interpolation based on the quotient $\varphi_{X, \mathbf{Y}}(x, \mathbf{y}) / \varphi_{\mathbf{Y}}(\mathbf{y})$ obtained from the initial step of the algorithm; for the actual estimation, we have considered multidimensional TSE and LI.

The proposed methods have been empirically analyzed and evaluated using data sampled from three different statistical models: first model corresponds to a two-dimensional Gaussian distribution, second model involves an exponentially distributed variable with a rate parameter following a gamma distribution, and third model includes a Gaussian distribution with mean parameter following a mixture of two Gaussian distributions. From the experimental results, we have observed that both methods yield good approximations (low KL and MSE values) of the true conditional densities. The observations from these studies were supplemented with an analysis of a real-world neuroanatomy data set. For comparison, we have analyzed the proposed methods relative to the MoTBF learning method described by Langseth et al. ${ }^{11,12}$ using the previously generated artificial data sets. From the results, we observed that although the three methods yield comparable results for the gamma-exponential distributed data, we also found that the proposed algorithms significantly outperformed the MoTBF-based algorithm on the Gaussian data sets and the mixture model data sets.

In this paper, equal width intervals $\left[\epsilon_{i}, \xi_{i}\right]$ are assumed in each dimension and the hyperrectangles $A_{l}$ have the same size. In the future, we would like to further study how to automatically find appropriate values for the limits $\left[\epsilon_{i}, \xi_{i}\right]$. For a given configuration of the model parameters, the computational complexity is dominated by the algorithm for learning the joint and the marginal densities. We would like to investigate methods for improving the computational complexity of this particular step of the algorithm as well as methods for improving the overall runtime of the algorithm. Finally, we intend to use these approaches to learn more complex BNs, which also involve adapting the learned potentials to support efficient inference and considering BN structure learning.

# Acknowledgments 

This work has been partially supported by the Spanish Ministry of Economy and Competitiveness through Cajal Blue Brain (C080020-09) and TIN2013-41592-P projects and by the Madrid Regional government through S2013/ICE-2845-CASI-CAM-CM project.
