# Learning the Information Divergence 

Onur Dikmen, Zhirong Yang, and Erkki Oja,


#### Abstract

Information divergence that measures the difference between two nonnegative matrices or tensors has found its use in a variety of machine learning problems. Examples are Nonnegative Matrix/Tensor Factorization, Stochastic Neighbor Embedding, topic models, and Bayesian network optimization. The success of such a learning task depends heavily on a suitable divergence. A large variety of divergences have been suggested and analyzed, but very few results are available for an objective choice of the optimal divergence for a given task. Here we present a framework that facilitates automatic selection of the best divergence among a given family, based on standard maximum likelihood estimation. We first propose an approximated Tweedie distribution for the $\beta$-divergence family. Selecting the best $\beta$ then becomes a machine learning problem solved by maximum likelihood. Next, we reformulate $\alpha$-divergence in terms of $\beta$-divergence, which enables automatic selection of $\alpha$ by maximum likelihood with reuse of the learning principle for $\beta$-divergence. Furthermore, we show the connections between $\gamma$ and $\beta$-divergences as well as Rényi- and $\alpha$-divergences, such that our automatic selection framework is extended to nonseparable divergences. Experiments on both synthetic and realworld data demonstrate that our method can quite accurately select information divergence across different learning problems and various divergence families.


Index Terms-information divergence, Tweedie distribution, maximum likelihood, nonnegative matrix factorization, stochastic neighbor embedding.

## I. INTRODUCTION

Information divergences are an essential element in modern machine learning. They originated in estimation theory where a divergence maps the dissimilarity between two probability distributions to nonnegative values. Presently, information divergences have been extended for nonnegative tensors and used in many learning problems where the objective is to minimize the approximation error between the observed data and the model. Typical applications include Nonnegative Matrix Factorization (see e.g. [1], [2], [3], [4]), Stochastic Neighbor Embedding [5], [6], topic models [7], [8], and Bayesian network optimization [9].

There exist a large variety of information divergences. In Section II, we summarize the most popularly used parametric families including $\alpha$-, $\beta$-, $\gamma$ - and Rényi-divergences [10], [11], [12], [13], [14] and their combinations (e.g. [15]). The four parametric families in turn belong to broader ones such as the Csiszár-Morimoto $f$-divergences [16], [17] and Bregman divergences [18]. Data analysis techniques based on information divergences have been widely and successfully applied to various data such as text [19], electroencephalography [3], facial images [20], and audio spectrograms [21].

[^0]Compared to the rich set of available information divergences, there is little research on how to select the best one for a given application. This is an important issue because the performance of a given divergence-based estimation or modeling method in a particular task very much depends on the divergence used. Formulating a learning task in a family of divergences greatly increases the flexibility to handle different types of noise in data. For example, Euclidean distance is suitable for data with Gaussian noise; Kullback-Leibler divergence has shown success for finding topics in text documents [7]; and Itakura-Saito divergence has proven to be suitable for audio signal processing [21]. A conventional workaround is to select among a finite number of candidate divergences using a validation set. This however cannot be applied to divergences that are non-separable over tensor entries. The validation approach is also problematic for tasks where all data are needed for learning, for example, cluster analysis.

In Section III, we propose a new method of statistical learning for selecting the best divergence among the four popular parametric families in any given data modeling task. Our starting-point is the Tweedie distribution [22], which is known to have a relationship with $\beta$-divergence [23], [24]. The Maximum Tweedie Likelihood (MTL) is in principle a disciplined and straightforward method for choosing the optimal $\beta$ value. However, in order for this to be feasible in practice, two shortcomings with the MTL method have to be overcome: 1) Tweedie distribution is not defined for all $\beta ; 2$ ) calculation of Tweedie likelihood is complicated and prone to numerical problems for large $\beta$. To overcome these drawbacks, we propose here a novel distribution using an exponential over the $\beta$-divergence with a specific augmentation term. The new distribution has the following nice properties: 1) it is close to the Tweedie distribution, especially at four important special cases; 2) it exists for all $\beta \in \mathbb{R}$; 3) its likelihood can be calculated by standard statistical software. We call the new density the Exponential Divergence with Augmentation (EDA). EDA is a non-normalized density, i.e., its likelihood includes a normalizing constant which is not analytically available. But, since the density is univariate the normalizing constant can be efficiently and accurately estimated by numerical integration. The method of Maximizing the Exponential Divergence with Augmentation Likelihood (MEDAL) thus gives a more robust $\beta$ selection in a wider range than MTL. $\beta$ estimation on EDA can also be carried out using parameter estimation methods, e.g., Score Matching (SM) [25], specifically proposed for nonnormalized densities. In the experiments section, we show that SM on EDA also performs as accurately as MEDAL.

Besides $\beta$-divergence, the MEDAL method is extended to select the best divergence in other parametric families. We reformulate $\alpha$-divergence in terms of $\beta$-divergence after a change of parameters so that $\alpha$ can be optimized using the


[^0]:    The authors are with Department of Information and Computer Science, Aalto University, 00076, Finland. e-mail: onur.dikmen@aalto.fi; zhirong.yang@aalto.fi; erkki.oja@aalto.fi

MEDAL method. Our method can also be applied to nonseparable cases. We show the equivalence between $\beta$ and $\gamma$-divergences, and between $\alpha$ and Rényi divergences by a connecting scalar, which allows us to choose the best $\gamma$ - or Rényi-divergence by reusing the MEDAL method.

We tested our method with extensive experiments, whose results are presented in Section IV. We have used both synthetic data with a known distribution and real-world data including music, stock prices, and social networks. The MEDAL method is applied to different learning problems: Nonnegative Matrix Factorization (NMF) [26], [3], [1], Projective NMF [27], [28] and Symmetric Stochastic Neighbor Embedding for visualization [5], [6]. We also demonstrate that our method outperforms Score Matching on Exponential Divergence distribution (ED), a previous approach for $\beta$-divergence selection [29]. Conclusions and discussions on future work are given in Section V.

## II. INFORMATION DIVERGENCES

Many learning objectives can be formulated as an approximation of the form $\mathbf{x} \approx \boldsymbol{\mu}$, where $\mathbf{x}>0$ is the observed data (input) and $\boldsymbol{\mu}$ is the approximation given by the model. The formulation for $\boldsymbol{\mu}$ totally depends on the task to be solved. Consider Nonnegative Matrix Factorization: then $\mathbf{x}>0$ is a data matrix and $\boldsymbol{\mu}$ is a product of two lower-rank nonnegative matrices which typically give a sparse representation for the columns of $\mathbf{x}$. Other concrete examples are given in Section IV.

The approximation error can be measured by various information divergences. Suppose $\boldsymbol{\mu}$ is parameterized by $\boldsymbol{\Theta}$. The learning problem becomes an optimization procedure that minimizes the given divergence $D(\mathbf{x} \| \boldsymbol{\mu}(\boldsymbol{\Theta}))$ over $\boldsymbol{\Theta}$. Regularization may be applied for $\boldsymbol{\Theta}$ for complexity control. For notational brevity we focus on definitions over vectorial $\mathbf{x}$, $\boldsymbol{\mu}, \boldsymbol{\Theta}$ in this section, while they can be extended to matrices or higher order tensors in a straightforward manner.

In this work we consider four parametric families of divergences, which are the widely used $\alpha$-, $\beta$-, $\gamma$ - and Rényidivergences. This collection is rich because it covers most commonly used divergences. The definition of the four families and some of their special cases are given below.

- $\alpha$-divergence [10], [11] is defined as

$$
D_{\alpha}(\mathbf{x} \| \boldsymbol{\mu})=\frac{\sum_{i} x_{i}^{\alpha} \mu_{i}^{1-\alpha}-\alpha x_{i}+(\alpha-1) \mu_{i}}{\alpha(\alpha-1)}
$$

The family contains the following special cases:

$$
\begin{aligned}
D_{\alpha=2}(\mathbf{x} \| \boldsymbol{\mu}) & =D_{\mathrm{P}}(\mathbf{x} \| \boldsymbol{\mu})=\frac{1}{2} \sum_{i} \frac{\left(x_{i}-\mu_{i}\right)^{2}}{\mu_{i}} \\
D_{\alpha \rightarrow 1}(\mathbf{x} \| \boldsymbol{\mu}) & =D_{\mathrm{I}}(\mathbf{x} \| \boldsymbol{\mu})=\sum_{i}\left(x_{i} \ln \frac{x_{i}}{\mu_{i}}-x_{i}+\mu_{i}\right) \\
D_{\alpha=1 / 2}(\mathbf{x} \| \boldsymbol{\mu}) & =2 D_{\mathrm{H}}(\mathbf{x} \| \boldsymbol{\mu})=2 \sum_{i}\left(\sqrt{x_{i}}-\sqrt{\mu_{i}}\right)^{2} \\
D_{\alpha \rightarrow 0}(\mathbf{x} \| \boldsymbol{\mu}) & =D_{\mathrm{I}}(\boldsymbol{\mu} \| \mathbf{x})=\sum_{i}\left(\mu_{i} \ln \frac{\mu_{i}}{x_{i}}-\mu_{i}+x_{i}\right) \\
D_{\alpha=-1}(\mathbf{x} \| \boldsymbol{\mu}) & =D_{\mathrm{IP}}(\mathbf{x} \| \boldsymbol{\mu})=\frac{1}{2} \sum_{i} \frac{\left(x_{i}-\mu_{i}\right)^{2}}{x_{i}}
\end{aligned}
$$

where $D_{\mathrm{I}}, D_{\mathrm{P}}, D_{\mathrm{IP}}$, and $D_{\mathrm{H}}$ denote non-normalized Kullback-Leibler, Pearson Chi-square, inverse Pearson and Hellinger distances, respectively.

- $\beta$-divergence [30], [31] is defined as

$$
D_{\beta}(\mathbf{x} \| \boldsymbol{\mu})=\frac{\sum_{i} x_{i}^{\beta+1}+\beta \mu_{i}^{\beta+1}-(\beta+1) x_{i} \mu_{i}^{\beta}}{\beta(\beta+1)}
$$

The family contains the following special cases:

$$
\begin{aligned}
D_{\beta=1}(\mathbf{x} \| \boldsymbol{\mu}) & =D_{\mathrm{EU}}(\mathbf{x} \| \boldsymbol{\mu})=\frac{1}{2} \sum_{i}\left(x_{i}-\mu_{i}\right)^{2} \\
D_{\beta \rightarrow 0}(\mathbf{x} \| \boldsymbol{\mu}) & =D_{\mathrm{I}}(\mathbf{x} \| \boldsymbol{\mu})=\sum_{i}\left(x_{i} \ln \frac{x_{i}}{\mu_{i}}-x_{i}+\mu_{i}\right) \\
D_{\beta \rightarrow-1}(\mathbf{x} \| \boldsymbol{\mu}) & =D_{\mathrm{IS}}(\mathbf{x} \| \boldsymbol{\mu})=\sum_{i}\left(\frac{x_{i}}{\mu_{i}}-\ln \frac{x_{i}}{\mu_{i}}-1\right) \\
D_{\beta=-2}(\mathbf{x} \| \boldsymbol{\mu}) & =\sum_{i}\left(\frac{x_{i}}{2 \mu_{i}^{2}}-\frac{1}{\mu_{i}}+\frac{1}{2 x_{i}}\right)
\end{aligned}
$$

where $D_{\mathrm{EU}}$ and $D_{\mathrm{IS}}$ denote the Euclidean distance and Itakura-Saito divergence, respectively.

- $\gamma$-divergence [13] is defined as

$$
\begin{aligned}
D_{\gamma}(\mathbf{x} \| \boldsymbol{\mu})= & \frac{1}{\gamma(\gamma+1)}\left[\ln \left(\sum_{i} x_{i}^{\gamma+1}\right)+\gamma \ln \left(\sum_{i} \mu_{i}^{\gamma+1}\right)\right. \\
& \left.-(\gamma+1) \ln \left(\sum_{i} x_{i} \mu_{i}^{\gamma}\right)\right]
\end{aligned}
$$

The normalized Kullback-Leibler (KL) divergence is a special case of $\gamma$-divergence:

$$
D_{\gamma \rightarrow 0}(\mathbf{x} \| \boldsymbol{\mu})=D_{\mathrm{KL}}(\tilde{\mathbf{x}} \| \tilde{\boldsymbol{\mu}})=\sum_{i} \tilde{x}_{i} \ln \frac{\tilde{x}_{i}}{\tilde{\mu}_{i}}
$$

where $\tilde{x}_{i}=x_{i} / \sum_{j} x_{j}$ and $\tilde{\mu}_{i}=\mu_{i} / \sum_{j} \mu_{j}$.

- Rényi divergence [32] is defined as

$$
D_{\rho}(\mathbf{x} \| \boldsymbol{\mu})=\frac{1}{\rho-1} \ln \left(\tilde{x}_{i}^{\rho} \tilde{\mu}_{i}^{1-\rho}\right)
$$

for $\rho>0$. The Rényi divergence also includes the normalized Kullback-Leibler divergence as its special case when $\rho \rightarrow 1$.

## III. Divergence Selection by Statistical Learning

The above rich collection of information divergences basically allows great flexibility to the approximation framework. However, practitioners must face a choice problem: how to select the best divergence in a family? In most existing applications the selection is done empirically by the human. A conventional automatic selection method is cross-validation [33], [34], where the training only uses part of the entries of $\mathbf{x}$ and the remaining ones are used for validation. This method has a number of drawbacks: 1) it is only applicable to the divergences where the entries are separable (e.g. $\alpha$ or $\beta$-divergence). Leaving out some entries for $\gamma$ - and Rényi divergences is infeasible due to the logarithm or normalization; 2) separation of entries is not applicable in some applications

where all entries are needed in the learning, for example, cluster analysis.

Our proposal here is to use the familiar and proven technique of maximum likelihood estimation for automatic divergence selection, using a suitably chosen and very flexible probability density model for the data. In the following we discuss this statistical learning approach for automatic divergence selection in the family of $\beta$-divergences, followed by its extensions to the other divergence families.

## A. Selecting $\beta$-divergence

1) Maximum Tweedie Likelihood (MTL): We start from the probability density function (pdf) of an exponential dispersion model (EDM) [22]:

$$
p_{\mathrm{EDM}}(x ; \theta, \phi, p)=f(x, \phi, p) \exp \left[\frac{1}{\phi}(x \theta-\kappa(\theta))\right]
$$

where $\phi>0$ is the dispersion parameter, $\theta$ is the canonical parameter, and $\kappa(\theta)$ is the cumulant function (when $\phi=1$ its derivatives w.r.t. $\theta$ give the cumulants). Such a distribution has mean $\mu=\kappa^{\prime}(\theta)$ and variance $V(\mu, p)=\phi \kappa^{\prime \prime}(\theta)$. This density is defined for $x \geq 0$, thus $\mu>0$.

A Tweedie distribution is an EDM whose variance has a special form, $V(\mu)=\mu^{p}$ with $p \in \mathbb{R} \backslash(0,1)$. The canonical parameter and the cumulant function that satisfy this property are [22]
$\theta=\left\{\begin{array}{cl}\frac{\mu^{1-p}-1}{1-p}, & \text { if } p \neq 1 \\ \ln \mu, & \text { if } p=1\end{array}, \quad \kappa(\theta)=\left\{\begin{array}{cl}\frac{\mu^{2-p}-1}{2-p}, & \text { if } p \neq 2 \\ \ln \mu, & \text { if } p=2\end{array}\right.\right.$.

Note that $\ln \mu$ is the limit of $\frac{\mu^{t}-1}{t}$ as $t \rightarrow 0$. Finite analytical forms of $f(x, \phi, p)$ in Tweedie distribution are generally unavailable. The function can be expanded with infinite series [35] or approximated by saddle point estimation [36].

It is known that the Tweedie distribution has a connection to $\beta$-divergence (see, e.g., [23], [24]): maximizing the likelihood of Tweedie distribution for certain $p$ values is equivalent to minimizing the corresponding divergence with $\beta=1-p$. Especially, the gradients of the log-likelihood of Gamma, Poisson and Gaussian distributions over $\mu_{i}$ are equal to the ones of $\beta$ divergence with $\beta=-1,0,1$, respectively. This motivates a $\beta$ divergence selection method by Maximum Tweedie Likelihood (MTL).

However, MTL has the following two shortcomings. First, Tweedie distribution is not defined for $p \in(0,1)$. That is, if the best $\beta=1-p$ happens to be in the range $(0,1)$, it cannot be found by MTL; in addition, there is little research on the Tweedie distribution with $\beta>1(p<0)$. Second, $f(x, \phi, p)$ in Tweedie distribution is not the probability normalizing constant (note that it depends on $x$ ), and its evaluation requires ad hoc techniques. The existing software using the infinite series expansion approach [35] (see Appendix A) is prone to numerical computation problems especially for $-0.1<\beta<0$. There is no existing implementation that can calculate Tweedie likelihood for $\beta>1$.
2) Maximum Exponential Divergence with Augmentation Likelihood (MEDAL): Our answer to the above shortcomings in MTL is to design an alternative distribution with the following properties: 1) it is close to the Tweedie distribution, especially for the four crucial points when $\beta \in\{-2,-1,0,1\}$; 2) it should be defined for all $\beta \in \mathbb{R}$; 3) its pdf can be evaluated more robustly by standard statistical software.

From (10) and (11) the pdf of the Tweedie distribution is written as

$$
p_{\mathrm{Tw}}(x ; \mu, \phi, \beta)=f(x, \phi, \beta) \exp \left[\frac{1}{\phi}\left(\frac{x \mu^{\beta}}{\beta}-\frac{\mu^{\beta+1}}{\beta+1}\right)\right]
$$

w.r.t. $\beta$ instead of $p$, using the relation $\beta=1-p$. This holds when $\beta \neq 0$ and $\beta \neq-1$. The extra terms $1 /(1-p)$ and $1 /(2-p)$ in (11) have been absorbed in $f(x, \phi, \beta)$. The cases $\beta=0$ or $\beta=-1$ have to be analyzed separately.

To make an explicit connection with $\beta$-divergence defined in (2), we suggest a new distribution given in the following form:

$$
\begin{aligned}
& p_{\text {approx }}(x ; \mu, \phi, \beta)=g(x, \phi, \beta) \exp \left\{-\frac{1}{\phi} D_{\beta}(x \| \mu)\right\} \\
& =g(x, \phi, \beta) \exp \left[\frac{1}{\phi}\left(-\frac{x^{\beta+1}}{\beta(\beta+1)}+\frac{x \mu^{\beta}}{\beta}-\frac{\mu^{\beta+1}}{\beta+1}\right)\right]
\end{aligned}
$$

Now the $\beta$-divergence for scalar $x$ appears in the exponent, and $g(x, \phi, \beta)$ will be used to approximate this with the Tweedie distribution. Ideally, the choice

$$
g(x, \phi, \beta)=f(x, \phi, \beta) / \exp \left[\frac{1}{\phi}\left(-\frac{x^{\beta+1}}{\beta(\beta+1)}\right)\right]
$$

would result in full equivalence to Tweedie distribution, as seen from (12). However, because $f(x, \phi, \beta)$ is unknown in the general case, such $g$ is also unavailable.

We can, however, try to approximate $g$ using the fact that $p_{\text {approx }}$ must be a proper density whose integral is equal to one. From (13) it then follows

$$
\begin{aligned}
& \exp \left[\frac{1}{\phi} \frac{\mu^{\beta+1}}{\beta+1}\right] \\
& \quad=\int d x g(x, \phi, \beta) \exp \left[\frac{1}{\phi}\left(-\frac{x^{\beta+1}}{\beta(\beta+1)}+\frac{x \mu^{\beta}}{\beta}\right)\right]
\end{aligned}
$$

This integral is, of course, impossible to evaluate because we do not even know the function inside. However, the integral can be approximated nicely by Laplace's method. Laplace's approximation is

$$
\int_{a}^{b} d x f(x) e^{M h(x)} \approx \sqrt{\frac{2 \pi}{M\left|h^{\prime \prime}\left(x_{0}\right)\right|}} f\left(x_{0}\right) e^{M h\left(x_{0}\right)}
$$

where $x_{0}=\arg \max _{x} h(x)$ and $M$ is a large constant.
In order to approximate (14) by Laplace's method, $1 / \phi$ takes the role of $M$ and thus the approximation is valid for small $\phi$. We need the maximizer of the exponentiated term $h(x)=-\frac{x^{\beta+1}}{\beta(\beta+1)}+\frac{x \mu^{\beta}}{\beta}$. This term has a zero first derivative

and negative second derivative, i.e., it is maximized, at $x=\mu$. Thus, Laplace's method gives us

$$
\begin{aligned}
& \exp \left[\frac{1}{\phi} \frac{\mu^{\beta+1}}{\beta+1}\right] \\
& \approx \sqrt{\frac{2 \pi \phi}{\left|-\mu^{\beta-1}\right|}} g(\mu, \phi, \beta) \exp \left[\frac{1}{\phi}\left(-\frac{\mu^{\beta+1}}{\beta(\beta+1)}+\frac{\mu^{\beta+1}}{\beta}\right)\right] \\
& =\sqrt{\frac{2 \pi \phi}{\mu^{\beta-1}}} g(\mu, \phi, \beta) \exp \left[\frac{1}{\phi} \frac{\mu^{\beta+1}}{\beta+1}\right]
\end{aligned}
$$

The approximation gives $g(\mu, \phi, \beta)=\frac{1}{\sqrt{2 \pi \phi}} \mu^{(\beta-1) / 2}$ which suggests the function

$$
g(x, \phi, \beta)=\frac{1}{\sqrt{2 \pi \phi}} x^{(\beta-1) / 2}=\frac{1}{\sqrt{2 \pi \phi}} \exp \left[\frac{(\beta-1)}{2} \ln x\right]
$$

Putting this result into (13) as such does not guarantee a proper pdf however, because it is an approximation, only valid at the limit $\phi \rightarrow 0$. To make it proper, we have to add a normalizing constant into the density in (13).

The pdf of the final distribution, for a scalar argument $x$, thus becomes
$p_{\text {approx }}(x ; \mu, \beta, \phi)=\frac{1}{Z(\mu, \beta, \phi)} \exp \left\{R(x, \beta)-\frac{1}{\phi} D_{\beta}(x \| \mu)\right\}$
where $Z(\mu, \beta, \phi)$ is the normalizing constant counting for the terms which are independent of $x$, and $R(x, \beta)$ is an augmentation term given as

$$
R(x, \beta)=\frac{\beta-1}{2} \ln x
$$

This pdf is a proper density for all $\beta \in \mathbb{R}$, which is guaranteed by the following theorem.

Theorem 1: Let $f(x)=\exp \left\{\frac{\beta-1}{2} \ln x-\frac{1}{\phi} D_{\beta}(x \| \mu)\right\}$. The improper integral $\int_{0}^{\infty} f(x) d x$ converges.

Proof: Let $q=\left|\frac{\beta-1}{2}\right|+1+\epsilon$ with any $\epsilon \in(0, \infty)$, and $g(x)=x^{-q}$. By these definitions, we have $q>\left|\frac{\beta-1}{2}\right|$, and then for $x \geq 1,\left(\frac{\beta-1}{2}+q\right) \phi \ln x \leq 0 \leq D_{\beta}(x \| \mu)$, i.e. $0 \leq f(x) \leq g(x)$. By Cauchy convergence test, we know that $\int_{1}^{\infty} g(x) d x$ is convergent because $q>1$, and so is $\int_{1}^{\infty} f(x) d x$. Obviously $f(x)$ is continuous and bounded for $x \in[0,1]$. Therefore, for $x \geq 0, \int_{0}^{\infty} f(x) d x=\int_{0}^{1} f(x) d x+$ $\int_{1}^{\infty} f(x) d x$ also converges.

Finally, for vectorial $\mathbf{x}$, the pdf is a product of the marginal densities:
$p_{\mathrm{EDA}}(\mathbf{x} ; \boldsymbol{\mu}, \beta, \phi)=\frac{1}{Z(\boldsymbol{\mu}, \beta, \phi)} \exp \left\{R(\mathbf{x}, \beta)-\frac{1}{\phi} D_{\beta}(\mathbf{x} \| \boldsymbol{\mu})\right\}$
where $D_{\beta}(\mathbf{x} \| \boldsymbol{\mu})$ is defined in (2) and

$$
R(\mathbf{x}, \beta)=\frac{\beta-1}{2} \sum_{i} \ln x_{i}
$$

We call (17) the Exponential Divergence with Augmentation (EDA) distribution, because it applies an exponential over an information divergence plus an augmentation term.

The log-likelihood of the EDA density can be written as

$$
\begin{aligned}
& \ln p(\mathbf{x} ; \boldsymbol{\mu}, \beta, \phi)=\sum_{i} \ln p\left(x_{i} ; \mu_{i}, \beta, \phi\right) \\
& =\sum_{i}\left[\frac{\beta-1}{2} \ln x_{i}-\frac{1}{\phi} D_{\beta}\left(x_{i} \| \mu_{i}\right)-\ln Z\left(\mu_{i}, \beta, \phi\right)\right]
\end{aligned}
$$

due to the fact that $D_{\beta}(\mathbf{x} \| \boldsymbol{\mu})$ in Eq. (2) and the augmentation term in (18) are separable over $x_{i}$, (i.e. $x_{i}$ are independent given $\mu_{i}$ ). The best $\beta$ is now selected by

$$
\beta^{*}=\arg \max _{\beta}\left[\max _{\phi} \ln p(\mathbf{x} ; \boldsymbol{\mu}, \beta, \phi)\right]
$$

where $\boldsymbol{\mu}=\arg \min _{\boldsymbol{\eta}} D_{\beta}(\mathbf{x} \| \boldsymbol{\eta})$. We call the new divergence selection method Maximum EDA Likelihood (MEDAL).

Let us look at the four special cases of Tweedie distribution: Gaussian $(\mathcal{N})$, Poisson $(\mathcal{P O})$, Gamma $(\mathcal{G})$ and Inverse Gaussian $(\mathcal{L N})$. They correspond to $\beta=1,0,-1,-2$. For simplicity of notation, we may drop the subscript $i$ and write $x$ and $\mu$ for one entry in $\mathbf{x}$ and $\boldsymbol{\mu}$. Then, the log-likelihoods of the above four special cases are

$$
\begin{aligned}
\ln p_{\mathcal{N}}(x ; \mu, \phi)= & -\frac{1}{2} \ln (2 \pi \phi)-\frac{1}{2 \phi}(x-\mu)^{2} \\
\ln p_{\mathcal{P O}}(x ; \mu)= & x \ln \mu-\mu-\ln \Gamma(x+1) \\
\approx & x \ln \mu-\mu-\ln (2 \pi x) / 2-x \ln x+x \\
\ln p_{\mathcal{G}}(x ; 1 / \phi, \phi \mu)= & (1 / \phi-1) \ln x-\frac{x}{\phi \mu} \\
& -(1 / \phi) \ln (\phi \mu)-\ln \Gamma(1 / \phi) \\
\ln p_{\mathcal{L N}}(x ; \mu, 1 / \phi)= & -\frac{1}{2} \ln \left(2 \pi \phi x^{3}\right)-\frac{1}{\phi}\left(\frac{1}{2} \frac{x}{\mu^{2}}-\frac{1}{\mu}+\frac{1}{2 x}\right)
\end{aligned}
$$

where in the Poisson case we employ Stirling's approximation ${ }^{1}$. To see the similarity of these four special cases with the general expression for the EDA log-likelihood in Eq. (19), let us look at one term in the sum there. It is a fairly straightforward exercise to plug in the $\beta$-divergences from Eqs. $(3,4,5,6)$ and the augmentation term from Eq. (18) and see that the log-likelihoods coincide. The normalizing term $\ln Z(\mu, \beta, \phi)]$ for these special cases can be determined from the corresponding density.

In general, the normalizing constant $Z(\boldsymbol{\mu}, \beta, \phi)$ is intractable except for a few special cases. Numerical evaluation of $Z(\boldsymbol{\mu}, \beta, \phi)$ can be implemented by standard statistical software. Here we employ the approximation with GaussLaguerre quadratures (details in Appendix B).

Finally, let us note that in addition to the maximum likelihood estimator, Score Matching (SM) [25], [37] can be applied to estimation of $\beta$ as a density parameter (see Section IV-A). In a previous effort, Lu et al. [29] proposed a similar exponential divergence (ED) distribution

$$
p_{\mathrm{ED}}(\mathbf{x} ; \boldsymbol{\mu}, \beta) \propto \exp \left[-D_{\beta}(\mathbf{x} \| \boldsymbol{\mu})\right]
$$

but without the augmentation. It is easy to show that ED also exists for all $\beta$ by changing $q=1+\epsilon$ in the proof of Theorem

[^0]
[^0]:    ${ }^{1}$ The case $\beta=0$ and $\phi \neq 1$ does not correspond to Poisson distribution, but the transformation $p_{\mathrm{EDM}}(x ; \mu, \phi, 1)=p_{\mathcal{P O}}(x / \phi ; \mu / \phi) / \phi$ can be used to evaluate the pdf.

1. We will empirically illustrate the discrepancy between ED and EDA in Section IV-A, showing that the selection based on ED is however inaccurate, especially for $\beta \leq 0$.

## B. Selecting $\alpha$-divergence

We extend the MEDAL method to $\alpha$-divergence selection. This is done by relating $\alpha$-divergence to $\beta$-divergence with a nonlinear transformation between $\alpha$ and $\beta$. Let $y_{i}=x_{i}^{\alpha} / \alpha^{2 \alpha}$, $m_{i}=\mu_{i}^{\alpha} / \alpha^{2 \alpha}$ and $\beta=1 / \alpha-1$ for $\alpha \neq 0$. We have

$$
\begin{aligned}
D_{\beta}\left(y_{i} \| m_{i}\right) & =\frac{1}{\beta(\beta+1)}\left(y_{i}^{\beta+1}+\beta m_{i}^{\beta+1}-(\beta+1) y_{i} m_{i}^{\beta}\right) \\
& =\frac{-\alpha^{2}}{\alpha-1}\left(\frac{x_{i}}{\alpha^{2}}+\frac{1-\alpha}{\alpha} \frac{\mu_{i}}{\alpha^{2}}-\frac{1}{\alpha} \frac{x_{i}^{\alpha}}{\alpha^{2 \alpha}} \frac{\mu_{i}^{1-\alpha}}{\alpha^{2(1-\alpha)}}\right) \\
& =D_{\alpha}\left(x_{i} \| \mu_{i}\right)
\end{aligned}
$$

This relationship allows us to evaluate the likelihood of $\mu$ and $\alpha$ using $y_{i}$ and $\beta$ :

$$
\begin{aligned}
p\left(x_{i} ; \mu_{i}, \alpha, \phi\right) & =p\left(y_{i} ; m_{i}, \beta, \phi\right)\left\lvert\, \frac{d y_{i}}{d x_{i}}\right. \\
& =p\left(y_{i} ; m_{i}, \beta, \phi\right) \frac{x_{i}^{\alpha-1}}{\alpha^{2(\alpha-1 / 2)}} \\
& =p\left(y_{i} ; m_{i}, \beta, \phi\right) y_{i}^{-\beta}|\beta+1|
\end{aligned}
$$

In vectorial form, the best $\alpha$ for $D_{\alpha}(\mathbf{x} \| \boldsymbol{\mu})$ is then given by $\alpha^{*}=1 /\left(\beta^{*}+1\right)$ where

$$
\begin{aligned}
\beta^{*} & =\arg \max _{\beta}\left\{\max _{\phi}[\ln p(\mathbf{y} ; \mathbf{m}, \beta)\right. \\
& \left.-\beta \ln y_{i}+\ln |\beta+1|]\right\}
\end{aligned}
$$

where $\mathbf{m}=\arg \min _{\boldsymbol{\eta}} D_{\beta}(\mathbf{y} \| \boldsymbol{\eta})$. This transformation method can handle all $\alpha$ except $\alpha \rightarrow 0$ since it corresponds to $\beta \rightarrow \infty$.

## C. Selecting $\gamma$ - and Rényi divergences

Above we presented the selection methods for two families where the divergence is separable over the tensor entries. Next we consider selection among $\gamma$ - and Rényi divergence families where their members are not separable. Our strategy is to reduce $\gamma$-divergence to $\beta$-divergence with a connecting scalar. This is formally given by the following result.
Theorem 2: For $\mathbf{x} \geq \mathbf{0}$ and $\tau \in \mathbb{R}$,

$$
\arg \min _{\boldsymbol{\mu} \geq \mathbf{0}} D_{\gamma \rightarrow \tau}(\mathbf{x} \| \boldsymbol{\mu})=\arg \min _{\boldsymbol{\mu} \geq \mathbf{0}}\left[\min _{c>0} D_{\beta \rightarrow \tau}(\mathbf{x} \| c \boldsymbol{\mu})\right]
$$

The proof is done by zeroing the derivative right hand side with respect to $c$ (details in Appendix C).

Theorem 2 states that with a positive scalar, the learning problem formulated by a $\gamma$-divergence is equivalent to the one by the corresponding $\beta$-divergence. The latter is separable and can be solved by the methods described in the Section III-A. An example is between normalized KL-divergence (in $\gamma$-divergence) and the non-normalized KL-divergence (in $\beta$ divergence) with the optimal connecting scalar $c=\sum_{i} \frac{x_{i}}{\sum_{i} \mu_{i}}$. Example applications on selecting the best $\gamma$-divergence are given in Section IV-D.

Similarly, we can also reduce a Rényi divergence to its corresponding $\alpha$-divergence with the same proof technique (see Appendix C).

Theorem 3: For $\mathbf{x} \geq \mathbf{0}$ and $\tau>0$,

$$
\arg \min _{\boldsymbol{\mu} \geq \mathbf{0}} D_{\rho \rightarrow \tau}(\mathbf{x} \| \boldsymbol{\mu})=\arg \min _{\boldsymbol{\mu} \geq \mathbf{0}}\left[\min _{c>0} D_{\alpha \rightarrow \tau}(\mathbf{x} \| c \boldsymbol{\mu})\right]
$$

## IV. EXPERIMENTS

In this section we demonstrate the proposed method on various data types and learning tasks. First we provide the results on synthetic data, whose density is known, to compare the behavior of MTL, MEDAL and the score matching method [29]. Second, we illustrate the advantage of the EDA density over ED. Third, we apply our method on $\alpha$ - and $\beta$-divergence selection in Nonnegative Matrix Factorization (NMF) on realworld data including music and stock prices. Fourth, we test MEDAL in selecting non-separable cases (e.g. $\gamma$-divergence) for Projective NMF and s-SNE visualization learning tasks across synthetic data, images, and a dolphin social network.

## A. Synthetic data

1) $\beta$-divergence selection: We use here scalar data generated from the four special cases of Tweedie distributions, namely, Inverse Gaussian, Gamma, Poisson, and Gaussian distributions. We simply fit the best Tweedie, EDA or ED density to the data using either the maximum likelihood method or score matching (SM).

In Fig. 1 (first row), the results of the Maximum Tweedie Likelihood (MTL) are shown. The $\beta$ value that maximizes the likelihood in Tweedie distribution is consistent with the true parameters, i.e., $-2,-1,0$ and 1 respectively for the above distributions. Note that Tweedie distributions are not defined for $\beta \in(0,1)$, but $\beta$-divergence is defined in this region, which will lead to discontinuity in the log-likelihood over $\beta$.

The second and third rows in Fig. 1 present results of the exponential divergence density ED given in Eq. (21). The loglikelihood and negative score matching objectives [29] on the same four datasets are shown. The estimates are consistent with the ground truth Gaussian and Poisson data. However, for Gamma and Inverse Gaussian data, both $\beta$ estimates deviate from the ground truth. Thus, estimators based on ED do not give as accurate estimates as the MTL method. The ED distribution [29] has an advantage that it is defined also for $\beta \in(0,1)$. In the above, we have seen that $\beta$ selection by using ED is accurate when $\beta \rightarrow 0$ or $\beta=1$. However, as explained in Section III-A2, in the other cases ED and Tweedie distributions are not the same because the terms containing the observed variable in these distributions are not exactly the same as those of the Tweedie distributions.

EDA, the augmented ED density introduced in Section III-A, not only has both the advantage of continuity but also gives very accurate estimates for $\beta<0$. The MEDAL loglikelihood curves over $\beta$ based on EDA are given in Fig. 1 (fourth row). In the $\beta$ selection of Eq. (20), the $\phi$ value that maximizes the likelihood with $\beta$ fixed is found by a grid search. The likelihood values are the same as those of special Tweedie distributions and there are no abrupt changes

![img-0.jpeg](img-0.jpeg)

Fig. 1. β selection using (from top to bottom) Tweedie likelihood, ED likelihood, negative SM objective of ED, EDA likelihood, and negative SM objective of EDA. Data were generated using Tweedie distribution with β = −2, −1, 0, 1 (from left to right).

or discontinuities in the likelihood surface. We also estimated β for the EDA density using Score Matching, and curves of the negative SM objective are presented in the bottom row of Fig. 1. They also recover the ground truth accurately.

2) α-divergence selection: There is only one known generative model for which the maximum likelihood estimator corresponds to the minimizer of the corresponding α divergence. It is the Poisson distribution. We thus reused the Poisson-distributed data of the previous experiments with the β-divergence. In Fig. 2a, we present the log-likelihood objective over α obtained with Tweedie distribution (MTL) and the transformation from Section III-B. The ground truth α → 1 is successfully recovered with MTL. However, there are no likelihood estimates for α ∈ (0.5, 1), corresponding to β ∈ (0, 1) for which no Tweedie distributions are defined. Moreover, to our knowledge there are no studies concerning the pdf's of Tweedie distributions with β > 1. For that reason, the likelihood values for α ∈ [0, 0.5) are left blank in the plot.

It can be seen from Fig. 2b and 2c, that the augmentation in the MEDAL method also helps in α selection. Again, both ED and EDA solve most of the discontinuity problem except α = 0. Selection using ED fails to find the ground truth

![img-1.jpeg](img-1.jpeg)

Fig. 2. Log-likelihood of (a) Tweedie, (b) ED, and (c) EDA distributions for α-selection. In the Tweedie plot, blanks correspond to β = 1/α − 1 values for which a Tweedie distribution pdf does not exist or cannot be evaluated, i.e., β ∈ (0, 1) ∪ (1, ∞). In (d), negative SM objective function values are plotted for EDA.

which equals 1, which is however successfully found by the MEDAL method. SM on EDA recovers the ground truth as well (Fig. 2d).

### *B. Divergence selection in NMF*

The objective in nonnegative matrix factorization (NMF) is to find a low-rank approximation to the observed data by expressing it as a product of two nonnegative matrices, i.e., **V** ≈ **V̂** = **WH** with **V** ∈ **R**<sup>*F* × *N*</sup> , **W** ∈ **R**<sup>*F* × *K*</sup> and **H** ∈ **R**<sup>*K* × *N*</sup> . This objective is pursued through the minimization of an information divergence between the data and the approximation, i.e., *D*(**V**||**V̂**). The divergence can be any appropriate one for the data/application such as β, α, γ, Rényi, etc. Here, we chose the β and α divergences to illustrate the MEDAL method for realistic data.

The optimization of β-NMF was implemented using the standard multiplicative update rules [23], [38]. Similar multiplicative update rules are also available for α-NMF [23]. Alternatively, the algorithm for β-NMF can be used for α-divergence minimization as well, using the transformation explained in Section III-B.

*1) A Short Piano Excerpt:* We consider the piano data used in [21]. It is an audio sequence recorded in real conditions, consisting of four notes played all together in the first measure and in all possible pairs in the subsequent measures. A power spectrogram with analysis window of size 46 ms was computed, leading to *F* = 513 frequency bins and *N* = 676 time frames. These make up the data matrix **V**, for which a matrix factorization **V̂** = **WH** with low rank *K* = 6 is sought for.

In Fig. 3a and 3b, we show the log-likelihood values of the MEDAL method for β and α, respectively. For each parameter value β and α, the multiplicative algorithm for the respective divergence is run for 100 iterations and likelihoods are evaluated with mean values calculated from the returned matrix factorizations. For each value of β and α, the highest likelihood w.r.t. φ (see Eq. (20)) is found by a grid search.

The found maximum likelihood estimate β = −1 corresponds to Itakura-Saito divergence, which is in harmony with the empirical results presented in [21] and the common belief that IS divergence is most suitable for audio spectrograms. The optimal α value value was 0.5 corresponding to Hellinger distance. We can also see that the log likelihood value associated

![img-2.jpeg](img-2.jpeg)

Fig. 3. (a, b) Log likelihood values for β and α for the spectrogram of a short piano excerpt with *F* = 513, *N* = 676, *K* = 6. (c) Negative SM objective for β.

with α = 0.5 is still much less than the one for β = −1. SM also finds β = −1 as can be seen from Fig. 3c.

### *C. Stock Prices*

Next, we repeat the same experiment on a stock price dataset which contains Dow Jones Industrial Average. There are 30 companies included in the data. They are major American companies from various sectors such as services (e.g., Walmart), consumer goods (e.g., General Motors) and healthcare (e.g., Pfizer). The data was collected from 3rd January 2000 to 27th July 2011, in total 2543 trading dates. We set *K* = 5 in NMF and masked 50% of the data by following [39]. The stock data curves are displayed in Fig. 4 (left).

The EDA likelihood curve with β ∈ [−2, 2] is shown in Figure 4 (bottom left). We can see that the best divergence selected by MEDAL is β = 0.4. The corresponding best φ = 0.006. These results are in harmony with the findings of Tan and Févotte [39] using the remaining 50% of the data as validation set, where they found that β ∈ [0, 0.5] (mind that our β values equal their minus one) performs

![img-3.jpeg](img-3.jpeg)

Fig. 4. Top: the stock data. Bottom left: the EDA log-likelihood for $\beta \in$ $[-2,2]$. Bottom right: negative SM objective function for $\beta \in[-2,2]$.
well for a large range of $\phi$ 's. Differently, our method is more advantageous because we do not need additional criteria nor data for validations. In Figure 4 (bottom right), negative SM objective function is plotted for $\beta \in[-2,2]$. With SM, the optimal $\beta$ is found to be 1 .

## D. Selecting $\gamma$-divergence

In this section we demonstrate that the proposed method can be applied to applications beyond NMF and to nonseparable divergence families. To our knowledge, no other existing methods can handle these two cases.

1) Multinomial data: We first exemplify $\gamma$-divergence selection for synthetic data drawn from a multinomial distribution. We generated a 1000-dimensional stochastic vector $\mathbf{p}$ from the uniform distribution. Next we drew $\mathbf{x} \sim$ $\operatorname{Multinomial}(n, \mathbf{p})$ with $n=10^{7}$. The MEDAL method is applied to find the best $\gamma$-divergence for the approximation of $\mathbf{x}$ by $\mathbf{p}$.

Fig. 6 (1st row, left) shows the MEDAL log-likelihood. The peak appears when $\gamma=0$, which indicates that the normalized KL-divergence is the most suitable one among the $\gamma$-divergence family. Selection using score matching of EDA gives the best $\gamma$ also close to zero (Fig. 6 1st row, right). The result is expected, because the maximum likelihood estimator of $\mathbf{p}$ in multinomial distribution is equivalent to minimizing the KL-divergence over $\mathbf{p}$. Our finding also justifies the usage of KL-divergence in topic models with the multinomial distribution [40], [7].
2) Projective NMF: Next we apply the MEDAL method to Projective Nonnegative Matrix Factorization (PNMF) [27], [28] based on $\gamma$-divergence [13], [19]. Given a nonnegative matrix $\mathbf{V} \in \mathbb{R}_{+}^{F \times N}$, PNMF seeks a low-rank nonnegative matrix $\mathbf{W} \in \mathbb{R}_{+}^{F \times K}(K<F)$ that minimizes $D_{\gamma}(\mathbf{V} \| \widetilde{\mathbf{V}})$, where $\widetilde{\mathbf{V}}=\mathbf{W} \mathbf{W}^{T} \mathbf{V}$. PNMF is able to produce a highly orthogonal $\mathbf{W}$ and thus finds its applications in part-based feature extraction and clustering analysis, etc. Different from conventional NMF (or linear NMF) where each factorizing
matrix only appears once in the approximation, the matrix $\mathbf{W}$ occurs twice in $\widetilde{\mathbf{V}}$. Thus it is a special case of Quadratic Nonnegative Matrix Factorization (QNMF) [41].

We choose PNMF for two reasons: 1) we demonstrate the MEDAL performance on QNMF besides the linear NMF already shown in Section IV-B; 2) PNMF contains only one variable matrix in learning, without the issue of how to interleave the updates of different variable matrices.

We first tested MEDAL on a synthetic dataset. We generated a diagonal blockwise data matrix $\mathbf{V}$ of size $50 \times 30$, where two blocks are of sizes $30 \times 20$ and $20 \times 10$. The block entries are uniformly drawn from $[0,10]$. We then added uniform noise from $[0,1]$ to the all matrix entries. For each $\gamma$, we ran the multiplicative algorithm of PNMF by Yang and Oja [28], [42] to obtain $\mathbf{W}$ and $\widetilde{\mathbf{V}}$. The MEDAL method was then applied to select the best $\gamma$. The resulting approximated log-likelihood for $\gamma \in[-2,2]$ is shown in Fig. 6 (2nd row). We can see MEDAL and score matching of EDA give similar results, where the best $\gamma$ appear at -0.76 and -0.8 , respectively. Both resulting $W$ 's give perfect clustering accuracy of data rows.

We also tested MEDAL on the swimmer dataset [43] which is popularly used in the NMF field. Some example images from this dataset are shown in Fig. 5 (left). We vectorized each image in the dataset as a column and concatenated the columns into a $1024 \times 256$ data matrix $\mathbf{V}$. This matrix is then fed to PNMF and MEDAL as in the case for the synthetic dataset. Here we empirically set the rank to $K=17$ according to Tan and Févotte [44] and Yang et al. [45]. The matrix W was initialized by PNMF based on Euclidean distance to avoid poor local minima. The resulting approximated log-likelihood for $\gamma \in[-1,3]$ is shown in Figure 6 (3rd row, left). We can see a peak appearing around 1.7. Zooming in the region near the peak shows the best $\gamma=1.69$. The score matching objective over $\gamma$ values (Fig. 6 3rd row, right) shows a similar peak and the best $\gamma$ very close to the one given by MEDAL. Both methods result in excellent and nearly identical basis matrix (W) of the data, where the swimmer body as well as four limbs at four angles are clearly identified (see Fig. 5 bottom row).
3) Symmetric Stochastic Neighbor Embedding: Finally, we show an application beyond NMF, where MEDAL is used to find the best $\gamma$-divergence for the visualization using Symmetric Stochastic Neighbor Embedding (s-SNE) [5], [6].

Suppose there are $n$ multivariate data samples $\left\{\mathbf{x}_{i}\right\}_{i=1}^{n}$ with $\mathbf{x}_{i} \in \mathbb{R}^{D}$ and their pairwise similarities are represented by an $n \times n$ symmetric nonnegative matrix $\mathbf{P}$ where $P_{i i}=0$ and $\sum_{i j} P_{i j}=1$. The s-SNE visualization seeks a lowdimensional embedding $\mathbf{Y}=\left[\mathbf{y}_{1}, \mathbf{y}_{2}, \ldots, \mathbf{y}_{n}\right]^{T} \in \mathbb{R}^{n \times d}$ such that pairwise similarities in the embedding approximate those in the original space. Generally $d=2$ or $d=3$ for easy visualization. Denote $q_{i j}=q\left(\left\|\mathbf{y}_{i}-\mathbf{y}_{j}\right\|^{2}\right)$ with a certain kernel function $q$, for example $q_{i j}=\left(1+\left\|\mathbf{y}_{i}-\mathbf{y}_{j}\right\|^{2}\right)^{-1}$. The pairwise similarities in the embedding are then given by $Q_{i j}=q_{i j} / \sum_{k l: k \neq l} q_{k l}$. The s-SNE target is that $\mathbf{Q}$ is as close to $\mathbf{P}$ as possible. To measure the dissimilarity between $\mathbf{P}$ and $\mathbf{Q}$, the conventional s-SNE uses the Kullback-Leibler divergence $D_{\mathrm{KL}}(\mathbf{P} \| \mathbf{Q})$. Here we generalize s-SNE to the

![img-4.jpeg](img-4.jpeg)

Fig. 5. Swimmer dataset: (top) example images; (bottom) the best PNMF basis (W) selected by using (bottom left) MEDAL and (bottom right) score matching of EDA. The visualization reshapes each column of W to an image and displays it by the Matlab function imagesc.
whole family of $\gamma$-divergences as dissimilarity measures and select the best divergence by our MEDAL method.

We have used a real-world dolphins dataset ${ }^{2}$. It is the adjacency matrix of the undirected social network between 62 dolphins. We smoothed the matrix by PageRank random walk in order to find its macro structures. The smoothed matrix was then fed to s-SNE based on $\gamma$-divergence, with $\gamma \in[-2,2]$. The EDA log-likelihood is shown in Fig. 6 (4th row, left). By the MEDAL principle the best divergence is $\gamma=-0.6$ for s-SNE and the dolphins dataset. Score matching of EDA also indicates the best $\gamma$ is smaller than 0 . The resulting visualizations created by s-SNE with the respective best gamma-divergence are shown in Fig. 7, where the node layouts by both methods are very similar. In both visualizations we can clearly see two dolphin communities.

## V. CONCLUSIONS

We have presented a new method called MEDAL to automatically select the best information divergence in a parametric family. Our selection method is built upon a statistical learning approach, where the divergence is learned as the result of standard density parameter estimation. Maximizing the likelihood of the Tweedie distribution is a straightforward way for selecting $\beta$-divergence, which however has some shortcomings. We have proposed a novel distribution, the Exponential Divergence with Augmentation (EDA), which overcomes these shortcomings and thus can give a more robust

[^0]![img-5.jpeg](img-5.jpeg)

Fig. 6. Selecting the best $\gamma$-divergence: (1st row) for multinomial data, (2nd row) in PNMF for synthetic data, (3rd row) in PNMF for the swimmer dataset, and (4th row) in s-SNE for the dolphins dataset; (left column) using MEDAL and (right column) using score matching of EDA. The red star highlights the peak and the small subfigures in each plot shows the zoom-in around the peak. The sub-figures in the 3rd row zoom in the area near the peaks.
selection for the parameter over a wider range. The new method has been extended to $\alpha$-divergence selection by a nonlinear transformation. Furthermore, we have provided new results that connect the $\gamma$ - and $\beta$-divergences, which enable us to extend the selection method to non-separable cases. The extension also holds for Rényi divergence with similar relationship to $\alpha$-divergence. As a result, our method can be applied to most commonly used information divergences in learning.

We have performed extensive experiments to show the accuracy and applicability of the new method. Comparison on synthetic data has illustrated that our method is superior to Maximum Tweedie Likelihood, i.e., it finds the ground truth as accurately as MTL, while being defined on all values of $\beta$ and being less prone to numerical problems (no abrupt changes in the likelihood). We also showed that a previous estimation


[^0]:    ${ }^{2}$ available at http://www-personal.umich.edu/ mejn/netdata/

![img-6.jpeg](img-6.jpeg)

Fig. 7. Visualization of the dolphins social network with the best $\gamma$ using (top) MEDAL and (bottom) score matching of EDA. Dolphins and their social connections are shown by circles and lines, respectively. The background illustrates the node density by the Parzen method [46].
approach by Score Matching on Exponential Divergence distribution (ED, i.e., EDA before augmentation) is not accurate, especially for $\beta<0$. In the application to NMF, we have provided experimental results on various kinds of data including audio and stock prices. In the non-separable cases, we have demonstrated selecting $\gamma$-divergence for synthetic data, Projective NMF, and visualization by s-SNE. In those cases where the correct parameter value is known in advance for the synthetic data, or there is a wide consensus in the application community on the correct parameter value for real-world data, the MEDAL method gives expected results. These results show that the presented method has not only broad applications but also accurate selection performance. In the case of new kinds of data, for which the appropriate information divergence is not known, the MEDAL method provides a disciplined and rigorous way to compute the optimal parameter values.

In this paper we have focused on information divergence for vectorial data. There exist other divergences for higher-order tensors, for example, LogDet divergence and von Newmann divergence (see e.g. [47]) that are defined over eigenvalues of matrices. Selection among these divergences remains an open problem.

Here we mainly consider a positive data matrix and selecting the divergence parameter in $(\infty,+\infty)$. Tweedie distribution has no support for zero entries when $\beta<0$ and thus gives zero likelihood of the whole matrix/tensor by independence. In future work, extension of EDA to accommodate nonnegative data matrices could be developed for $\beta \geq 0$.

MEDAL is a two-phase method: the $\beta$ selection is based on the optimization result of $\boldsymbol{\mu}$. Ideally, both variables should be selected by optimizing the same objective. For maximum log-likelihood estimator, this requires that the negative loglikelihood equals the $\beta$-divergence, which is however infes-
sible for all $\beta$ due to intractability of integrals. Non-ML estimators could be used to attack this open problem.

The EDA distribution family includes the exact Gaussian, Gamma, and Inverse Gaussian distributions, and approximated Poisson distribution. In the approximation we used the firstorder Stirling expansion. One could apply higher-order expansions to improve the approximation accuracy. This could be implemented by further augmentation with higher-order terms around $\beta \rightarrow 0$.

## VI. ACKNOWLEDGMENT

This work was financially supported by the Academy of Finland (Finnish Center of Excellence in Computational Inference Research COIN, grant no 251170; Zhirong Yang additionally by decision number 140398).

## APPENDIX A

## INFINITE SERIES EXPANSION IN TWEEDIE DISTRIBUTION

In the series expansion, an EDM random variable is represented as a sum of $G$ independent Gamma random variables $x=\sum_{g}^{G} y_{g}$, where $G$ is Poisson distributed with parameter $\lambda=\frac{\mu^{2}}{\phi(2-p)}$; and the shape and scale parameters of the Gamma distribution are $-a$ and $b$, with $a=\frac{2-p}{1-2}$ and $b=\phi(p-1) \mu^{p-1}$.

The pdf of the Tweedie distribution is obtained analytically at $x=0$ as $e^{-\frac{\mu^{2}-x}{\phi(2-p)}}$. For $x>0$ the function $f(x, \phi, p)=$ $\frac{1}{x} \sum_{j=1}^{\infty} W_{j}(x, \phi, p)$, where for $1<p<2$

$$
W_{j}=\frac{x^{-j a}(p-1)^{j a}}{\phi^{j(1-a)}(2-p)^{j} j!\Gamma(-j a)}
$$

and for $p>2$

$$
W_{j}=\frac{1}{\pi} \frac{\Gamma(1+j a) \phi^{j(a-1)}(p-1)^{j a}}{\Gamma(1+j)(p-1)^{j} x^{j a}}(-1)^{j} \sin (-\pi j a)
$$

This infinite summation needs approximation in practice. Dunn and Smyth [35] described an approach to select a subset of these infinite terms to accurately approximate $f(x, \phi, p)$. In their approach, Stirling's approximation of the Gamma functions are used to find the index $j$ which gives the highest value of the function. Then, in order to find the most significant region, the indices are progressed in both directions until negligible terms are reached.

## APPENDIX B

## GAUSS-LAGUERRE QUADRATURES

This method (e.g. [48]) can evaluate definite integrals of the form

$$
\int_{0}^{\infty} e^{-z} f(z) d z \approx \sum_{i}^{n} f\left(z_{i}\right) w_{i}
$$

where $z_{i}$ is the $i$ th root of the $n$-th order Laguerre polynomial $L_{n}(z)$, and the weights are given by

$$
w_{i}=\frac{z_{i}}{(n+1)^{2} L_{n}^{2}\left(z_{i}\right)}
$$

The recursive definition of $L_{n}(z)$ is given by

$$
L_{n+1}(z)=\frac{1}{n+1}\left[(2 n+1-z) L_{n}(z)-n L_{n-1}(z)\right]
$$

with $L_{0}(z)=1$ and $L_{1}(z)=1-z$. In our experiments, we used the Matlab implementation by Winckel ${ }^{3}$ with $n=5000$.

## APPENDIX C

## Proofs of THEOREMS 2 AND 3

Lemma 4: $\arg \min _{z} a f(z)=\arg \min _{z} a \ln f(z)$ for $a \in \mathbb{R}$ and $f(z)>0$.
The proof of the lemma is simply by the monotonicity of $\ln$.
Next we prove Theorem 2. For $\beta \in \mathbb{R} \backslash\{-1,0\}$, zeroing $\frac{\partial D_{\beta}(\mathbf{x} \| c \boldsymbol{\mu})}{\partial c}$ gives

$$
c^{*}=\frac{\sum_{i} x_{i} \mu_{i}^{\beta}}{\sum_{i} \mu_{i}^{1+\beta}}
$$

Putting it back to $\min _{\boldsymbol{\mu}} \min _{c} D_{\beta}(\mathbf{x} \| c \boldsymbol{\mu})$, we obtain:

$$
\begin{aligned}
& \min _{\boldsymbol{\mu}} \min _{c} D_{\beta}(\mathbf{x} \| c \boldsymbol{\mu}) \\
= & \min _{\boldsymbol{\mu}} \frac{1}{\beta(1+\beta)}\left[\sum_{i} x_{i}^{1+\beta}+\beta \sum_{i}\left(\frac{\sum_{j} x_{j} \mu_{j}^{\beta}}{\sum_{j} \mu_{j}^{1+\beta}} \mu_{i}\right)^{1+\beta}\right. \\
& \left.-(1+\beta) \sum_{i} x_{i}\left(\frac{\sum_{j} x_{j} \mu_{j}^{\beta}}{\sum_{j} \mu_{j}^{1+\beta}} \mu_{i}\right)^{\beta}\right] \\
= & \min _{\boldsymbol{\mu}} \frac{1}{\beta(1+\beta)}\left[\sum_{i} x_{i}^{1+\beta}-\frac{\left(\sum_{i} x_{i} \mu_{i}^{\beta}\right)^{1+\beta}}{\left(\sum_{j} \mu_{j}^{1+\beta}\right)^{\beta}}\right]
\end{aligned}
$$

Dropping the constant, and by Lemma 4, the above is equivalent to minimizing

$$
\frac{1}{\beta(1+\beta)}\left[\beta \ln \left(\sum_{j} \mu_{j}^{1+\beta}\right)-(1+\beta) \ln \left(\sum_{i} x_{i} \mu_{i}^{\beta}\right)\right]
$$

Adding a constant $\frac{1}{\beta(1+\beta)} \ln \left(\sum_{i} x_{i}^{1+\beta}\right)$, the objective becomes minimizing $\gamma$-divergence (replacing $\beta$ with $\gamma$; see Eq. (7)).

We can apply the similar technique to prove Theorem 3. For $\alpha \in \mathbb{R} \backslash\{0,1\}$, zeroing $\frac{\partial D_{\alpha}(\mathbf{x} \| c \boldsymbol{\mu})}{\partial c}$ gives

$$
c^{*}=\left(\frac{\sum_{i} x_{i}^{\alpha} \mu_{i}^{1-\alpha}}{\sum_{i} \mu_{i}}\right)^{1 / \alpha}
$$

Putting it back, we obtain

$$
\begin{aligned}
& D_{\alpha}(\mathbf{x} \| c^{*} \boldsymbol{\mu}) \\
= & \frac{1}{\alpha(1-\alpha)} \sum_{i}\left\{\alpha x_{i}+(1-\alpha)\left(\frac{\sum_{j} x_{j}^{\alpha} \mu_{j}^{1-\alpha}}{\sum_{j} \mu_{j}}\right)^{1 / \alpha} \mu_{i}\right. \\
& \left.-x_{i}^{\alpha}\left[\left(\frac{\sum_{j} x_{j}^{\alpha} \mu_{j}^{1-\alpha}}{\sum_{j} \mu_{j}}\right)^{1 / \alpha} \mu_{i}\right]^{1-\alpha}\right\} \\
= & \frac{1}{\alpha-1}\left[\sum_{i} x_{i}^{\alpha}\left(\frac{\mu_{i}}{\sum_{j} \mu_{j}}\right)^{1-\alpha}\right]^{1 / \alpha}+\frac{\sum_{i} x_{i}}{1-\alpha}
\end{aligned}
$$

${ }^{3}$ available at http://www.mathworks.se/matlabcentral/fileexchange/

Dropping the constant $\frac{\sum_{i} x_{i}}{1-\alpha}$, and by Lemma 4, minimizing the above is equivalent to minimization of (for $\alpha>0$ )

$$
\frac{1}{\alpha-1} \ln \left[\sum_{i} x_{i}^{\alpha}\left(\frac{\mu_{i}}{\sum_{j} \mu_{j}}\right)^{1-\alpha}\right]
$$

Adding a constant $\frac{\alpha}{1-\alpha} \ln \sum_{i} x_{i}$ to the above, the objective becomes minimizing Rényi-divergence (replacing $\alpha$ with $\rho$; see Eq. (9)).

The proofs for the special cases are similar, where the main steps are given below

- $\beta=\gamma \rightarrow 0$ (or $\alpha=\rho \rightarrow 1$ ): zeroing $\frac{\partial D_{\beta \rightarrow 0}(\mathbf{x} \| c \boldsymbol{\mu})}{\partial c}$ gives $c^{*}=\frac{\sum_{i} x_{i}}{\sum_{i} \mu_{i}}$. Putting it back, we obtain $D_{\beta \rightarrow 0}(\mathbf{x} \| c^{*} \boldsymbol{\mu})=$ $\left(\sum_{i} x_{i}\right) D_{\gamma \rightarrow 0}(\mathbf{x} \| \boldsymbol{\mu})$.
- $\beta=\gamma \rightarrow-1$ : zeroing $\frac{\partial D_{\beta \rightarrow-1}(\mathbf{x} \| c \boldsymbol{\mu})}{\partial c}$ gives $c^{*}=$ $\frac{1}{M} \sum_{i} \frac{x_{i}}{\mu_{i}}$, where $M$ is the length of $\mathbf{x}$. Putting it back, we obtain $D_{\beta \rightarrow-1}(\mathbf{x} \| c^{*} \boldsymbol{\mu})=M D_{\gamma \rightarrow-1}(\mathbf{x} \| \boldsymbol{\mu})$.
- $\alpha=\rho \rightarrow 0$ : zeroing $\frac{\partial D_{\alpha \rightarrow 0}(\mathbf{x} \| c \boldsymbol{\mu})}{\partial c}$ gives

$$
c^{*}=\exp \left(-\frac{\sum_{i} \mu_{i} \ln \frac{\mu_{i}}{x_{i}}}{\sum_{i} \mu_{i}}\right)
$$

Putting it back, we obtain

$$
D_{\alpha \rightarrow 0}(\mathbf{x} \| c^{*} \boldsymbol{\mu})=-\exp \left(-\sum_{i} \tilde{\mu}_{i} \ln \frac{\tilde{\mu}_{i}}{x_{i}}\right)+\sum_{i} x_{i}
$$

where $\tilde{\mu}_{i}=\mu_{i} / \sum_{j} \mu_{j}$. Dropping the constant $\sum_{i} x_{i}$, minimizing $D_{\alpha \rightarrow 0}(\mathbf{x} \| c^{*} \boldsymbol{\mu})$ is equivalent to minimization of $\sum_{i} \tilde{\mu}_{i} \ln \frac{\tilde{\mu}_{i}}{x_{i}}$. Adding the constant $\ln \sum_{j} x_{j}$ to the latter, the objective becomes identical to $D_{\rho \rightarrow 0}(\mathbf{x} \| \boldsymbol{\mu})$, i.e. $D_{\mathrm{KL}}(\boldsymbol{\mu} \| \mathbf{x})$.
