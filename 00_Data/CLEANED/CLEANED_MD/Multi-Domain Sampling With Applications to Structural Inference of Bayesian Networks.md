# Multi-Domain Sampling With Applications to Structural Inference of Bayesian Networks * 

Qing Zhou ${ }^{\dagger}$


#### Abstract

When a posterior distribution has multiple modes, unconditional expectations, such as the posterior mean, may not offer informative summaries of the distribution. Motivated by this problem, we propose to decompose the sample space of a multimodal distribution into domains of attraction of local modes. Domain-based representations are defined to summarize the probability masses of and conditional expectations on domains of attraction, which are much more informative than the mean and other unconditional expectations. A computational method, the multi-domain sampler, is developed to construct domain-based representations for an arbitrary multimodal distribution. The multi-domain sampler is applied to structural learning of protein-signaling networks from high-throughput single-cell data, where a signaling network is modeled as a causal Bayesian network. Not only does our method provide a detailed landscape of the posterior distribution but also improves the accuracy and the predictive power of estimated networks.


Key words: Domain-based representation; Multimodal distribution; Monte Carlo; Network structure; Protein-signaling network; Wang-Landau algorithm.

## 1 Introduction

In Bayesian inference the information on an unknown parameter $\boldsymbol{\theta}$ given an observed dataset $\mathbf{y}_{o b s}$ is contained in the posterior distribution $p\left(\boldsymbol{\theta} \mid \mathbf{y}_{o b s}\right)$. When a posterior distribution

[^0]
[^0]:    *To appear in Journal of the American Statistical Association.
    ${ }^{\dagger}$ Qing Zhou is Assistant Professor, Department of Statistics, University of California, Los Angeles, CA 90095 (Email: zhou@stat.ucla.edu). This work was supported in part by NSF grant DMS-0805491 and NSF CAREER Award DMS-1055286. The author thanks the editor, the associate editor, and the two referees for helpful comments and suggestions which significantly improved the manuscript.

does not belong to a well-characterized family of distributions, Markov chain Monte Carlo (MCMC) is a standard computational approach to Bayesian inference via sampling from the posterior distribution. Typical examples of MCMC include the Metropolis-Hastings (MH) algorithm (Metropolis et al. 1953, Hastings 1970) and the Gibbs sampler (Geman and Geman 1984, Gelfand and Smith 1990, Tanner and Wong 1987). Thorough reviews of recent developments on Monte Carlo methods and their applications in Bayesian computation can be found in Chen et al. (2001) and Liu (2008). The posterior mean $E\left(\boldsymbol{\theta} \mid \mathbf{y}_{\text {obs }}\right)$ and other expectations are usually approximated from a Monte Carlo sample to summarize the posterior distribution. However, these unconditional expectations may not offer good summaries of the information for Bayesian inference when a posterior distribution has multiple local modes. One can easily construct a multimodal posterior distribution of which the mean is located in a low-density region and thus using it as an estimator for $\boldsymbol{\theta}$ lacks a conventional interpretation. To extract more information contained in a multimodal posterior distribution, it is desired to identify all major modes and calculate various statistics in appropriate neighborhoods of these modes.

To achieve these tasks, we propose to partition the sample space of $\boldsymbol{\theta}$ into a collection of domains such that the posterior distribution restricted to each domain is unimodal. The most parsimonious partition that minimizes the number of domains is to use the domains of attraction (to be defined rigorously later) of the local modes. Take the trimodal distribution $p(\boldsymbol{\theta})$ in Figure 1 as an illustration. The space is partitioned into three domains, denoted by $\Theta_{1}, \Theta_{2}$ and $\Theta_{3}$ : Each domain contains exactly one local mode; if we move any $\boldsymbol{\theta} \in \Theta_{k}$ $(k=1,2,3)$ along the trajectory that always follows the gradient direction of $p(\boldsymbol{\theta})$, it will eventually reach the mode in the domain $\Theta_{k}$. We may then calculate various conditional expectations on these domains, $E\left[h(\boldsymbol{\theta}) \mid \boldsymbol{\theta} \in \Theta_{k}\right](k=1,2,3)$, for different functions $h$. Together with the probability masses of the domains, $P\left(\boldsymbol{\theta} \in \Theta_{k}\right)$, they provide more informative summaries of the distribution $p(\boldsymbol{\theta})$ than unconditional expectations. Such a summary is called a domain-based representation (DR) for $p(\boldsymbol{\theta})$.

Although desired, construction of DRs for an arbitrary distribution is very challenging in practice. Sufficient Monte Carlo samples from domains of all local modes are necessary for estimating DRs, but efficient sampling from a multimodal distribution has always been a

![img-0.jpeg](img-0.jpeg)

Figure 1: Contour plot of a two-dimensional density with three modes labeled A, B and C. The numbers report log densities of contours and the dashed curves mark the boundaries between domains of attraction.

The hard problem. In this article, we develop a computational method that is able to construct domain-based representations for an arbitrary multimodal distribution. We partition the sample space into domains of attraction and utilize an iterative weighting scheme aiming at sampling from each domain with an equal frequency. The weighting scheme was proposed by Wang and Landau (2001), and further developed and generalized by Liang (2005), Liang et al. (2007) and Atchadé and Liu (2010) among others. However, a direct application of these existing methods cannot provide accurate estimation of DRs, due to at least two reasons. First, sample space partition used in these methods is usually predetermined according to a set of selected density levels. But partitioning the space into domains of attraction, as employed in our method, cannot be completed beforehand because it is a nontrivial job to detect all local modes and their domains in real applications. Second, the above methods mostly rely on simple local moves and lack a coherent global move to jump between different local modes. To obtain accurate estimation of DRs, we propose a dynamic scheme to partition the sample space into domains of attraction and devise a global move that utilizes estimated DRs along sampling iterations to enable fast transitions between multiple domains. Since the main feature of our method is to sample from multiple domains and construct DRs, we call it the multi-domain (MD) sampler.

The MD sampler can be applied to a wide range of Bayesian inference problems and

it is particularly powerful in tackling problems with complicated posterior distributions. Although there are many such applications in different fields, this article mainly concerns structural learning of causal Bayesian networks from experimental data. Learning network structure via Monte Carlo sampling is very challenging as the multimodality of the posterior distribution is extremely severe (Friedman and Koller 2003, Ellis and Wong 2008, Liang and Zhang 2009). In this problem, a domain of attraction is defined by a set of network structures, each represented by a directed acyclic graph (DAG). In a sense, the goal of the MD sampler is to construct a detailed landscape of the posterior distribution, which can provide new insights into the structural learning problem. Application of our method to a scientific problem is illustrated by a study on constructing protein-signaling networks from single-cell experimental data. A living cell is highly responsive to its environment due to the existence of widespread and diverse signal transduction pathways. These pathways constitute a complex signaling network as cross-talks usually exist between them. Knowledge of the structure of this network is critical to the understanding of various cellular behaviors and human diseases. Recent advances in biotechnology allow the biologist to measure the states of a collection of molecules on a cell-by-cell basis. Such large-scale data contain rich information for statistical inference of signaling networks, but powerful computational methods are needed given the complexity in the likelihood function and the posterior distribution. With the MD sampler, not only can we build a signaling network from the posterior mean graph, but also we may discover new pathway connections revealed by different domains of the posterior distribution, which are not accessible by other approaches.

The remaining part of this article is organized as follows. Section 2 defines the domain of attraction and domain-based representation. In Section 3 we develop the MD sampler and its estimation of DRs, with convergence and ergodicity of the sampler established in Appendix. The method is tested in Section 4 on an example in Euclidean space and implemented in Section 5 for Bayesian inference of network structure with a simulation study. Section 6 is the main application to the construction of signaling networks in human T cells. The article concludes with a discussion on related and future works.

# 2 Domain-based representation 

Let $p(\mathbf{x}), \mathbf{x} \in \mathcal{X} \subseteq \mathbb{R}^{m}$, be the density of the target distribution. Suppose that $p(\mathbf{x})$ is differentiable and denote by $\nabla p(\mathbf{x})$ the gradient of $p$ at $\mathbf{x}$. Define a differential equation

$$
\frac{d \mathbf{x}(t)}{d t}=\nabla p(\mathbf{x}(t))
$$

and write a solution path of this equation as $\mathbf{x}(t), t \in[0, \infty)$, where $\mathbf{x}(0)$ is a chosen initial point. Under some mild regularity conditions, $\mathbf{x}(\infty)$ converges to a local mode of $p(\mathbf{x})$, which is the basic intuition behind the gradient descent algorithm to maximize $p(\mathbf{x})$. Denote by $\left\{\boldsymbol{\nu}_{1}, \ldots, \boldsymbol{\nu}_{K}\right\}$ all the local modes, including the global mode, of $p(\mathbf{x})$. For $\mathbf{x} \in \mathcal{X}$, let $\mathbf{x}(0)=\mathbf{x}$ and define the domain partition index by

$$
I(\mathbf{x})= \begin{cases}k, & \text { if } \mathbf{x}(\infty)=\boldsymbol{\nu}_{k}, \text { for } k=1, \ldots, K \\ 0, & \text { otherwise }\end{cases}
$$

It maps $\mathbf{x}$ to the index of the local mode to which the solution path starting at $\mathbf{x}$ converges.
Definition 1. The domain of attraction of $\boldsymbol{\nu}_{k}$ is $D_{k}=\{\mathbf{x} \in \mathcal{X}: I(\mathbf{x})=k\}$ for $k=1, \ldots, K$. For simplicity we may call $D_{k}$ an attraction domain or a domain of $p$.

If the stationary points of $p(\mathbf{x})$ have zero probability mass, then $\left\{D_{k}: k=1, \ldots, K\right\}$ form a partition of the sample space $\mathcal{X}$ except for a set of zero probability mass. This is the default setting for this article.

Let $h(\mathbf{x})$ be a $p$-integrable function of $\mathbf{x}$. Write the probability mass of $D_{k}$ and the conditional expectation of $h(\mathbf{X})$ given $\mathbf{X} \in D_{k}$ as

$$
\begin{aligned}
\lambda_{k} & =P\left(\mathbf{X} \in D_{k}\right)=\int_{D_{k}} p(\mathbf{x}) d \mathbf{x} \\
\mu_{h, k} & =E\left[h(\mathbf{X}) \mid \mathbf{X} \in D_{k}\right]=\frac{1}{\lambda_{k}} \int_{D_{k}} h(\mathbf{x}) p(\mathbf{x}) d \mathbf{x}
\end{aligned}
$$

respectively, for $k=1, \ldots, K$.
Definition 2. The domain-based representation of $h$ with respect to the distribution $p$ is a $2 \times K$ array, $D R_{p}(h)=\left\{\left(\mu_{h, k}, \lambda_{k}\right): k=1, \ldots, K\right\}$.

The DR is equivalent to the probability mass function of $E[h(\mathbf{X}) \mid I(\mathbf{X})]$ that assigns probability $\lambda_{k}$ to $\mu_{h, k}$ for $k=1, \ldots, K$. It provides the expectation $E[h(\mathbf{X})]=\sum_{k} \lambda_{k} \mu_{h, k}$ and the decomposed contributions from the attraction domains of $p(\mathbf{x})$. Such a representation gives an informative low-dimensional summary of a multimodal distribution. For a complex distribution with many local modes, however, we cannot afford to estimate $\left(\mu_{h, k}, \lambda_{k}\right)$ for every domain when $K$ is too large and are less interested in domains of negligible probability masses ( $\lambda_{k}$ very close to zero). Due to these reasons we define domain-based representations with respect to a set of local modes $\left\{\boldsymbol{\nu}_{k}: k=1, \ldots, M\right\}$. Index all the local modes as $\boldsymbol{\nu}_{1}, \ldots, \boldsymbol{\nu}_{M}, \ldots, \boldsymbol{\nu}_{K}(M \leq K)$. Define the domain partition index with respect to $\left\{\boldsymbol{\nu}_{k}\right\}_{k=1}^{M}$ by $I_{M}(\mathbf{x})=I(\mathbf{x})$ if $1 \leq I(\mathbf{x}) \leq M$ and $I_{M}(\mathbf{x})=0$ otherwise. Then the sample space $\mathcal{X}$ can be partitioned into $D_{k}=\left\{\mathbf{x} \in \mathcal{X}: I_{M}(\mathbf{x})=k\right\}$ for $k=0, \ldots, M$, where $D_{k}$ is the domain of $\boldsymbol{\nu}_{k}(k \geq 1)$ and $D_{0}=\mathcal{X}-\bigcup_{k=1}^{M} D_{k}$. The DR of $h$ with respect to $\left\{\boldsymbol{\nu}_{k}\right\}_{k=1}^{M}$ is defined by the array $\left\{\left(\mu_{h, k}, \lambda_{k}\right): k=0, \ldots, M\right\}$, where $\lambda_{0}$ and $\mu_{h, 0}$ are defined for $D_{0}$ similarly as in Equations (3) and (4), respectively. Note that one can still obtain $E[h(\mathbf{X})]=\sum_{k=0}^{M} \lambda_{k} \mu_{h, k}$ after merging $D_{M+1}, \ldots, D_{K}$ into $D_{0}$.

There is a geometric interpretation for the attraction domains of a posterior distribution. Suppose that $\mathbf{Y}=\left(\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{n}\right)$ is a sample from an unknown distribution $\psi(\mathbf{y})$. We assume a parametric family $f_{\boldsymbol{\theta}}=f(\cdot \mid \boldsymbol{\theta}), \boldsymbol{\theta} \in \Theta$, as the model for $\mathbf{Y}$ and put a prior $\pi(\boldsymbol{\theta})$ on the unknown parameter $\boldsymbol{\theta}$. The posterior distribution of $\boldsymbol{\theta}$ is given by

$$
p(\boldsymbol{\theta} \mid \mathbf{Y}) \propto \pi(\boldsymbol{\theta}) \prod_{i=1}^{n} f\left(\mathbf{Y}_{i} \mid \boldsymbol{\theta}\right) \approx e^{n E\left[\log f\left(\mathbf{Y}_{1} \mid \boldsymbol{\theta}\right)\right]}
$$

when the sample size $n$ is large, where $E\left[\log f\left(\mathbf{Y}_{1} \mid \boldsymbol{\theta}\right)\right]=\int \log [f(\mathbf{y} \mid \boldsymbol{\theta})] \psi(\mathbf{y}) d \mathbf{y}$. Denote the Kullback-Leibler (KL) divergence between $\psi$ and $f_{\boldsymbol{\theta}}$ by

$$
d_{K L}\left(\psi \| f_{\boldsymbol{\theta}}\right)=\int \log \left[\frac{\psi(\mathbf{y})}{f(\mathbf{y} \mid \boldsymbol{\theta})}\right] \psi(\mathbf{y}) d \mathbf{y}
$$

Then, $p(\boldsymbol{\theta} \mid \mathbf{Y}) \propto \exp \left[-n d_{K L}\left(\psi \| f_{\boldsymbol{\theta}}\right)\right]$ when $n$ is large. In the space of density functions, we can regard $d_{K L}\left(\psi \| f_{\boldsymbol{\theta}}\right)$ as the "distance" to the point $\psi$ from a point in the manifold $\mathcal{M}=\left\{f_{\boldsymbol{\theta}}: \boldsymbol{\theta} \in \Theta\right\}$. Note that $\psi$ is not necessarily in $\mathcal{M}$ if our model assumption on $\mathbf{Y}$ is

incorrect. Then $p(\boldsymbol{\theta} \mid \mathbf{Y})$ may be interpreted as a Boltzmann distribution on the manifold $\mathcal{M}$ under a potential field $n d_{K L}\left(\psi \| f_{\boldsymbol{\theta}}\right)$. This potential pushes every $f_{\boldsymbol{\theta}}$, indexed by $\boldsymbol{\theta}$, towards $\psi$, and the collection of $\boldsymbol{\theta}$ which will be driven to an identical stationary point in $\mathcal{M}$ forms an attraction domain of $p(\boldsymbol{\theta} \mid \mathbf{Y})$.

# 3 The multi-domain sampler 

To develop an algorithm that is able to construct domain-based representations with respect to the target distribution $p$, it is necessary to identify the attraction domain of any $\mathbf{x} \in \mathcal{X}$. When $p(\mathbf{x})$ is differentiable, this can be achieved by application of the gradient descent (GD) algorithm that finds local modes of $p(\mathbf{x})$, or $\log p(\mathbf{x})$ for computational convenience. Generalization to the space of network structures will be discussed later.

A naive two-step approach to the construction of DRs is quite obvious. We may first apply a Monte Carlo algorithm to simulate a sample $\left\{\mathbf{X}^{t}\right\}_{t=1}^{n}$ from $p(\mathbf{x})$ or from a diffuse version of $p(\mathbf{x})$, e.g., $[p(\mathbf{x})]^{1 / \tau}$ for $\tau>1$ as used in parallel tempering (Geyer 1991). Then, for every $t$ we determine $I\left(\mathbf{X}^{t}\right)$ by a GD search initiated at $\mathbf{X}^{t}$ to find to which domain it belongs. This approach partitions the sample into attraction domains so that we can estimate the probability masses and conditional expectations for all identified domains. Although simple to implement, this two-step approach has a few drawbacks in terms of efficiency. Without a careful and specific design the Monte Carlo algorithm, even targeting at a diffuse version of $p(\mathbf{x})$, may not generate enough samples from all major domains or may completely miss some modes. As a result, estimation on some attraction domains may be inaccurate or unavailable. In addition, this approach does not utilize the information on the target distribution provided by the constructed DRs. To overcome these drawbacks, we develop the MD sampler that may achieve simultaneously an efficient simulation from a multimodal distribution and an accurate construction of domain-based representations, with comparable computational complexity as the naive two-step approach.

# 3.1 The main algorithm 

We wish to sample sufficiently from the majority of attraction domains. However, the density at the boundary between two neighboring domains is often exponentially low (e.g., Figure 1), which makes it difficult for an MH algorithm or a Gibbs sampler to jump across multiple domains. Thus, we need to allow the sampler to generate enough samples from such low-density regions that connect different domains. These considerations motivate the following double-partitioning design in the MD sampler.

Suppose that we are given a set of local modes of $p(\mathbf{x}),\left\{\boldsymbol{\nu}_{1}, \ldots, \boldsymbol{\nu}_{M}\right\}$, which may include the global mode. Given $\infty=H_{0}>H_{1}>\ldots>H_{L}=-\infty$, define the density partition index $J(\mathbf{x})=j$ if $\log p(\mathbf{x}) \in\left[H_{j}, H_{j-1}\right)$ for $j=1, \ldots, L$. We partition the space $\mathcal{X}$ into $(M+1) \times L$ subregions,

$$
D_{k j}=\left\{\mathbf{x} \in \mathcal{X}: I_{M}(\mathbf{x})=k, J(\mathbf{x})=j\right\}, k=0, \ldots, M, j=1, \ldots, L
$$

where $I_{M}(\mathbf{x})$ is the domain partition index with respect to $\left\{\boldsymbol{\nu}_{k}\right\}_{k=1}^{M}$. Then, the attraction domain of the local mode $\boldsymbol{\nu}_{k}$ is $D_{k}=\bigcup_{j} D_{k j}(1 \leq k \leq M)$. Note that some $D_{k j}$ may be empty; if $\log p\left(\boldsymbol{\nu}_{k}\right)<H_{i}$ then all $D_{k j}$ for $j \leq i$ are empty. In what follows, we only consider nonempty subregions. For a given matrix $\mathbf{W}=\left(w_{k j}\right)_{(M+1) \times L}$, define a working density

$$
p(\mathbf{x} ; \mathbf{W}) \propto \sum_{k=0}^{M} \sum_{j=1}^{L} \frac{p(\mathbf{x}) \mathbf{1}\left(\mathbf{x} \in D_{k j}\right)}{\exp \left(w_{k j}\right)}
$$

where $\mathbf{1}(\cdot)$ is an indicator function. Let $\mathbf{W}^{*}=\left(w_{k j}^{*}\right)$ such that $\exp \left(w_{k j}^{*}\right)=\int_{D_{k j}} p(\mathbf{x}) d \mathbf{x}$. Then, the probability masses of $D_{k j}$ are identical under $p\left(\mathbf{x} ; \mathbf{W}^{*}\right)$. Sampling from $p\left(\mathbf{x} ; \mathbf{W}^{*}\right)$ has two immediate implications. First, the sample sizes on the attraction domains, $\left\{D_{k}\right\}_{k=1}^{M}$, will be comparable, and thus, domain-based representations can be constructed with a high accuracy. Note that commonly used MCMC strategies for multimodal distributions, such as tempering, cannot generate samples of comparable sizes from different domains. Second, the sampler will stay in low-density regions (e.g., $D_{k L}$ ) for a substantial fraction of time, which makes it practically possible to jump between domains. Conversely, domain-based representations may be utilized to design efficient local and global moves for sampling from

$p\left(\mathbf{x} ; \mathbf{W}^{*}\right)$. We may construct online estimate of the covariance matrix on the domain of a local mode, which can be used for tuning the step size of a local move in this domain. For a multimodal distribution, tuning step size for each domain is more useful than tuning the overall step size (Harrio et al. 2001). Once we have identified sufficient local modes and estimated covariances of their respective domains, we can use them to design global moves that may jump from one domain to another. As one can see, these proposals can be implemented only if we have partitioned samples into attraction domains.

For $\mathbf{x}, \mathbf{y} \in \mathcal{X}$, let $q(\mathbf{x}, \mathbf{y})$ be a proposal from $\mathbf{x}$ to $\mathbf{y}$ and $r(\mathbf{x} ; \boldsymbol{\theta}, \mathbf{V})$ a distribution with parameters $\boldsymbol{\theta}$ and $\mathbf{V} \in \mathcal{V}$. We first develop the main algorithm of the MD sampler, assuming that the density ladder $\left\{H_{j}\right\}$ is fixed and $M$ local modes $\left\{\boldsymbol{\nu}_{k}\right\}_{k=1}^{M}$ have been identified. Dynamic update of these parameters will be discussed in Section 3.2 as the burn-in algorithm. Let $\mathbf{g}_{k}(\mathbf{x})$ be a map from $\mathcal{X}$ to $\mathcal{V}$ for $k=1, \ldots, M$.

Algorithm 1 (The main algorithm). Initialize $\mathbf{W}^{1}=\left(w_{k j}^{1}\right)$, parameters $\mathbf{V}_{k}^{1} \in \mathcal{V}(k=$ $1, \ldots, M), p_{m x} \in[0,1)$, and $\mathbf{X}^{1} \in \mathcal{X}$. Set $\gamma_{1} \leq 1$. For $t=1, \ldots, n$ :

1. Draw $\mathbf{Y}$ from $q\left(\mathbf{X}^{t}, \mathbf{y}\right)$ with probability $\left(1-p_{m x}\right)$ or from the mixture distribution $\frac{1}{M} \sum_{k=1}^{M} r\left(\mathbf{y} ; \boldsymbol{\nu}_{k}, \mathbf{V}_{k}^{t}\right)$ with probability $p_{m x}$.
2. Determine the density partition index $J(\mathbf{Y})$ and perform a GD search initiated at $\mathbf{Y}$ to determine the domain partition index $I_{M}(\mathbf{Y})$.
3. Accept or reject $\mathbf{Y}$ according to the MH ratio targeting at $p\left(\mathbf{x} ; \mathbf{W}^{t}\right)$ to obtain $\mathbf{X}^{t+1}$.
4. For $k=0, \ldots, M$ and $j=1, \ldots, L$ update

$$
w_{k j}^{t+1}=w_{k j}^{t}+\gamma_{t} \mathbf{1}\left(I_{M}\left(\mathbf{X}^{t+1}\right)=k, J\left(\mathbf{X}^{t+1}\right)=j\right)
$$

for $k=1, \ldots, M$ update

$$
\mathbf{V}_{k}^{t+1}=\mathbf{V}_{k}^{t}+\frac{\gamma_{t}}{2}\left[\mathbf{g}_{k}\left(\mathbf{X}^{t+1}\right)-\mathbf{V}_{k}^{t}\right] \mathbf{1}\left(I_{M}\left(\mathbf{X}^{t+1}\right)=k\right)
$$

and determine $\gamma_{t+1}$.

We may regard $w_{k j}^{t}$ as a weight for the subregion $D_{k j}$. After each visit to $D_{k j}$, the weight $w_{k j}^{t+1}$ increases by $\gamma_{t}$ unit (7), which decreases the probability mass of $D_{k j}$ under the working density $p\left(\mathbf{x} ; \mathbf{W}^{t+1}\right)(6)$. Such a weighting scheme aims to visit every $D_{k j}$ uniformly. There are two typical choices of $\left\{\gamma_{t}\right\}$. The first choice follows the standard design in stochastic approximation which employs a predetermined sequence such that $\sum_{t=1}^{\infty} \gamma_{t}=\infty$ and $\sum_{t=1}^{\infty} \gamma_{t}^{\zeta}<\infty$ for $\zeta \in(1,2)$ (Andrieu et al. 2005, Andrieu and Moulines 2006, Liang et al. 2007). The second design, originally proposed by Wang and Landau (2001), adjusts $\gamma_{t}$ in an adaptive way. However, there is difficulty in establishing its convergence (Atchadé and Liu 2010), and thus we adopt a modified Wang-Landau (MWL) design to update $\left\{\gamma_{t}\right\}$ in the MD sampler. Initialize $c_{k j}^{1}=0$ for all $k$ and $j$ in Algorithm 1. The MWL update at iteration $t(t=1, \ldots, n)$ is given below.

Routine 1 (MWL update). If $\gamma_{t}<\epsilon_{\gamma}$, set $\gamma_{t+1}=\gamma_{t}\left(\gamma_{t}+1\right)^{-1}$; otherwise:

- Set $c_{k j}^{t+1}=c_{k j}^{t}+\mathbf{1}\left(\mathbf{X}^{t+1} \in D_{k j}\right)$ for all $k, j$ and calculate $\Delta c_{\max }^{t+1}=\max _{k, j}\left|c_{k j}^{t+1}-\bar{c}^{t+1}\right|$, where $\bar{c}^{t+1}$ is the average of all $c_{k j}^{t+1}$.
- If $\Delta c_{\max }^{t+1} \geq \eta \bar{c}^{t+1}$, set $\gamma_{t+1}=\gamma_{t}$; otherwise, set $\gamma_{t+1}=\rho \gamma_{t}$ and $c_{k j}^{t+1}=0$ for all $k, j$.

That is, if $\gamma_{t} \geq \epsilon_{\gamma}$ we decrease $\gamma_{t}(\rho<1)$ only when the sampler has visited every subregion $D_{k j}$ with a roughly equal frequency since our last modification of $\gamma_{t}$. Let $t_{c}=$ $\min \left\{t: \gamma_{t}<\epsilon_{\gamma}\right\}$. For $t>t_{c}$ the update becomes deterministic with $\gamma_{t}=1 /(t+\xi)$, where $\xi=\gamma_{t_{c}}^{-1}-t_{c}$. The default setting for all the results in this article is given by $\rho=0.5$, $\eta=0.25$ and $\epsilon_{\gamma}=10^{-4}$.

Under some regularity conditions and the MWL update of $\left\{\gamma_{t}\right\}$,

$$
\exp \left(w_{k j}^{n}\right) \xrightarrow{a . s} \int_{D_{k j}} p(\mathbf{x}) d \mathbf{x}=\exp \left(w_{k j}^{*}\right)
$$

after being normalized to sum up to one,

$$
\begin{aligned}
& \mathbf{V}_{k}^{n} \xrightarrow{a . s} \frac{\int_{D_{k}} \mathbf{g}_{k}(\mathbf{x}) p\left(\mathbf{x} ; \mathbf{W}^{*}\right) d \mathbf{x}}{\int_{D_{k}} p\left(\mathbf{x} ; \mathbf{W}^{*}\right) d \mathbf{x}} \stackrel{\Delta}{=} \mathbf{V}_{k}^{*} \\
& \frac{1}{n} \sum_{t=1}^{n} h\left(\mathbf{X}^{t}\right) \xrightarrow{a . s} \int_{\mathcal{X}} h(\mathbf{x}) p\left(\mathbf{x} ; \mathbf{W}^{*}\right) d \mathbf{x}
\end{aligned}
$$

as $n \rightarrow \infty$. See Theorem 2 in Appendix for more details. If $\mathcal{X} \subseteq \mathbb{R}^{m}$, we often choose $\mathbf{g}_{k}(\mathbf{x})=\left(\mathbf{x}-\boldsymbol{\nu}_{k}\right)\left(\mathbf{x}-\boldsymbol{\nu}_{k}\right)^{\top}$ so that $\mathbf{V}_{k}^{*}$ is close to the covariance matrix of the conditional distribution $\left[\mathbf{X} \mid \mathbf{X} \in D_{k}\right]$, where $\mathbf{X} \sim p\left(\mathbf{x} ; \mathbf{W}^{*}\right)$. We use the mode $\boldsymbol{\nu}_{k}$ instead of the mean because the mode can be obtained accurately via a GD algorithm. The use of $\gamma_{t} / 2(<1)$ in Equation (8) ensures that $\mathbf{V}_{k}^{t+1}$ is positive definite if $\mathbf{V}_{k}^{t}$ is positive definite.

There are two types of proposals in step 1 of the algorithm, a local proposal $q\left(\mathbf{X}^{t}, \mathbf{y}\right)$ and a mixture distribution proposal. One advantage of partitioning samples into attraction domains is embodied in the mixture distribution proposal, in which we randomly draw a domain partition index $k \in\{1, \ldots, M\}$ and then propose a sample $\mathbf{Y}$ from $r\left(\mathbf{y} ; \boldsymbol{\nu}_{k}, \mathbf{V}_{k}^{t}\right)$. Equal mixture proportions $(1 / M)$ are used because a uniform sampling across domains is preferred. The default choice of the distribution $r\left(\mathbf{y} ; \boldsymbol{\nu}_{k}, \mathbf{V}_{k}^{t}\right)$ in $\mathbb{R}^{m}$ is $\mathcal{N}\left(\boldsymbol{\nu}_{k}, \mathbf{V}_{k}^{t}\right)$ for $k=$ $1, \ldots, M$, which gives a mixture normal proposal that matches the mode and the covariance on each domain of the working target $p\left(\mathbf{x} ; \mathbf{W}^{t}\right)$. This proposal uses a mixture distribution to approximate the multimodal target. It can generate efficient global jumps from one domain to another if $p\left(\mathbf{x} ; \mathbf{W}^{t}\right)$ on the domain $D_{k}$ can be well approximated by $r\left(\mathbf{x} ; \boldsymbol{\nu}_{k}, \mathbf{V}_{k}^{t}\right)$ with the identified mode $\boldsymbol{\nu}_{k}$ and the estimated $\mathbf{V}_{k}^{t}$. For simplicity we call this proposal the mixed jump. The typical design for $q\left(\mathbf{X}^{t}, \mathbf{y}\right)$ in $\mathbb{R}^{m}$ is to proposal $\mathbf{Y} \sim \mathcal{N}\left(\mathbf{X}^{t}, \sigma^{2} \mathbf{I}\right)$, where $\sigma^{2}$ is a scalar and $\mathbf{I}$ is the identity matrix. However, when the covariances are very different between domains, using a single local proposal may cause high autocorrelation, since the step size might be either too big for domains with small covariances or too small for those with large covariances, or both. In this case, we may incorporate an adaptive local proposal, $\mathbf{Y} \sim \mathcal{N}\left(\mathbf{X}^{t}, \sigma^{2} \mathbf{V}_{I_{M}\left(\mathbf{X}^{t}\right)}^{t}\right)$, in addition to $q\left(\mathbf{X}^{t}, \mathbf{y}\right)$, such that the learned covariance structure of a domain is utilized to guide the local proposal. This shows another advantage of the domain-partitioning design.

Remark 1. We summarize the unique features of the main algorithm. First, domain partitioning is incorporated in the framework of the Wang-Landau (WL) algorithm. This allows a more uniform sampling from different domains, which facilitates construction of DRs. At each iteration, a GD search is employed to determine $I_{M}(\mathbf{Y})$ and thus the computational complexity of this algorithm is comparable to the naive two-step approach. Second, an

adaptive global move, the mixed jump, is proposed given DRs constructed along the iteration, which utilizes identified modes and learned covariances to achieve between-domain moves.

Remark 2. Verification of the regularity conditions for convergence of the algorithm (see Appendix) is recommended before application. Furthermore, we suggest a few convergence diagnostics that can be conveniently used in practice. First, $\gamma_{n}$ should be small enough at the final iteration and the frequency of visiting different $D_{k j}$ should be roughly identical. Second, $\mathbf{W}^{n}$ and $\mathbf{V}_{k}^{n}$ should have converged with an acceptable accuracy. Violations of these two criteria indicate that more iterations may be necessary. Third, the adaptive parameters used in the mixed jump $\left(\mathbf{V}_{k}^{t}\right)$ should always stay in a reasonable range. For example, if $\mathbf{V}_{k}^{t}$ is a covariance matrix, one may check whether its eigenvalues are close to zero or unreasonably large, which may indicate divergence of the current run. If the last criterion is not satisfied, it is suggested to reinitialize the MD sampler with a smaller $\gamma_{1}$.

# 3.2 The burn-in algorithm 

In practical applications of the MD sampler, the density ladder $\left\{H_{j}\right\}$ and the local modes $\left\{\boldsymbol{\nu}_{k}\right\}$ are updated dynamically in a burn-in period before the main algorithm (Algorithm 1). The dynamic updating schemes are crucial steps for constructing domain-based representations in real applications, as one cannot partition the sample space into domains of attraction beforehand. We set $H_{1}, \ldots, H_{L-1}$ as an evenly spaced sequence so that $\Delta H=H_{j}-H_{j+1}$ is a constant for $j=1, \ldots, L-2$. Let $\left\{H_{j}^{t}\right\}$ be the density ladder and $\Lambda^{t}=\left\{\boldsymbol{\nu}_{k}^{t}: k=1, \ldots, M^{t}\right\}$ be the set of $M^{t}$ identified modes at iteration $t$. Let $K^{*}$ be the maximum number of modes to be recorded and denote by $\boldsymbol{\nu}_{(\mathbf{x})}$ the mode of the domain that $\mathbf{x}$ belongs to. Let $\mathbf{0}$ be the zero matrix with dimension determined by the context. The following routine is used to update $\Lambda^{t}$ when a new sample $\mathbf{Y}$ is proposed.

Routine 2. Let $s^{t}=\underset{1 \leq k \leq M^{t}}{\operatorname{argmin}} p\left(\boldsymbol{\nu}_{k}^{t}\right)$.

- If $\boldsymbol{\nu}_{(\mathbf{Y})} \notin \Lambda^{t}$ and $M^{t}<K^{*}$, set $\Lambda^{t+1}=\Lambda^{t} \cup\left\{\boldsymbol{\nu}_{(\mathbf{Y})}\right\}, M^{t+1}=M^{t}+1$, and initialize $w_{M^{t+1} j}^{t}=0$ for all $j$;

- if $\boldsymbol{\nu}_{(\mathbf{Y})} \notin \Lambda^{t}, M^{t}=K^{*}$ and $p\left(\boldsymbol{\nu}_{(\mathbf{Y})}\right)>p\left(\boldsymbol{\nu}_{s^{t}}^{t}\right)$, set $\boldsymbol{\nu}_{s^{t}}^{t+1}=\boldsymbol{\nu}_{(\mathbf{Y})}, \boldsymbol{\nu}_{k}^{t+1}=\boldsymbol{\nu}_{k}^{t}$ for $k \neq s^{t}$, $M^{t+1}=M^{t}$, and assign $w_{0 j}^{t} \Leftarrow w_{0 j}^{t}+w_{s^{t} j}^{t}$ and $w_{s^{t} j}^{t} \Leftarrow 0$ for all $j$.
- otherwise set $\Lambda^{t+1}=\Lambda^{t}$ and $M^{t+1}=M^{t}$.

According to this routine, we record at most the $K^{*}$ highest modes identified during the burn-in period. If there are more than $K^{*}$ modes, Algorithm 1 will construct DRs with respect to the recorded modes. The weights $\left(w_{k j}^{t}\right)$ are updated when a new mode replaces an old one in $\Lambda^{t}$, for which the assignment operator ' $\Leftarrow$ ' is used to distinguish from equality.

The density ladder $\left\{H_{j}^{t}\right\}$ is adjusted such that $H_{1}^{t}$, the lower bound of the highest density partition interval, is close to $\log u^{*}$, where $u^{*}$ is the density of the highest mode identified so far. If $\log u^{*}>H_{1}^{t}+\Delta H$ we move upwards the density ladder by $\Delta H$ unit and update the weights $\left(w_{k j}^{t}\right)$ accordingly, with details provided in Routine 3. This strategy helps the sampler to explore the high-density part, which is important for statistical estimation and finding the global mode.

Routine 3. Given $\Lambda^{t+1}$, find $u^{t+1}=\max \left\{p\left(\boldsymbol{\nu}_{k}^{t+1}\right): k=1, \ldots, M^{t+1}\right\}$.

- If $\log u^{t+1}>H_{1}^{t}+\Delta H$, set $H_{j}^{t+1}=H_{j}^{t}+\Delta H$ for $j=1, \ldots, L-1$; for $k=0, \ldots, M^{t+1}$, assign $w_{k L}^{t} \Leftarrow w_{k(L-1)}^{t}+w_{k L}^{t}, w_{k j}^{t} \Leftarrow w_{k(j-1)}^{t}$ for $j=L-1, \ldots, 2$, and $w_{k 1}^{t} \Leftarrow 0$;
- otherwise set $\left\{H_{j}^{t+1}\right\}=\left\{H_{j}^{t}\right\}$.

Algorithm 2 (The burn-in algorithm). Input $L, \Delta H$ and $K^{*}$. Set $\gamma_{0}=1$. Initialize $\mathbf{X}^{1} \in \mathcal{X}, \Lambda^{1}=\left\{\boldsymbol{\nu}_{\left(\mathbf{X}^{1}\right)}\right\}, M^{1}=1, \mathbf{W}^{1}=\left(w_{k j}^{1}\right)_{2 \times L}=\mathbf{0}$, and $\mathbf{V}_{1}^{1}$. Set $H_{1}^{1}=\log p\left(\boldsymbol{\nu}_{\left(\mathbf{X}^{1}\right)}\right)$ and $H_{j}^{1}=H_{j-1}^{1}-\Delta H$ for $j=2, \ldots, L-1$. For $t=1, \ldots, B$ :

1. Draw $\mathbf{Y} \sim q\left(\mathbf{X}^{t}, \mathbf{y}\right)$ and find $\boldsymbol{\nu}_{(\mathbf{Y})}$ by a GD search.
2. Given $\boldsymbol{\nu}_{(\mathbf{Y})}$, update $\Lambda^{t+1}$ and $M^{t+1}$ by Routine 2 ; if $\boldsymbol{\nu}_{\ell}^{t+1}=\boldsymbol{\nu}_{(\mathbf{Y})}$ is a new mode in $\Lambda^{t+1}$, initialize $\mathbf{V}_{\ell}^{t}$. Given $\Lambda^{t+1}$, update $\left\{H_{j}^{t+1}\right\}$ by Routine 3.
3. Given $\Lambda^{t+1}$ and $\left\{H_{j}^{t+1}\right\}$, accept or reject $\mathbf{Y}$ with the MH ratio targeting at $p\left(\mathbf{x} ; \mathbf{W}^{t}\right)$ to obtain $\mathbf{X}^{t+1}$.
4. Execute step 4 of Algorithm 1 with $\gamma_{t}=\gamma_{0}$.

Remark 3. Note that $\gamma_{t}=1$ for every iteration in the burn-in algorithm. This pushes the sampler to explore different regions in the sample space so that more local modes can be identified. In this case, the weight $w_{k j}^{t}$ records the number of visits to $D_{k j}$ before the $t$ th iteration, which is the reason for our updating schemes on $\left\{w_{k j}^{t}\right\}$ in Routine 2 when a mode is updated in $\Lambda^{t+1}$ and in Routine 3 when the density ladder changes.

Remark 4. The burn-in algorithm can be used as an optimization method that searches for up to $K^{*}$ local modes of the highest densities. As demonstrated in the Bayesian network applications, this algorithm is very powerful in finding global modes.

The MD sampler requires only a few input parameters, $L, \Delta H, p_{m x}$, and $K^{*}$. A practical rule is to choose $L$ and $\Delta H$ such that the range of the density partition intervals, $L \Delta H$ in log scale, is wide enough to cover important regions. In this paper, we set $L \Delta H$ around 20 for the low-dimensional test example in Section 4 and around 200 for learning Bayesian networks in Sections 5 and 6. By default the probability of proposing a mixed jump $p_{m x}=0.1$. The effect of keeping only $K^{*}$ modes will be studied later with the examples.

# 3.3 Statistical estimation 

The domain-based representation of $h$ is constructed by estimating $\lambda_{k}$ (3) and $\mu_{h, k}$ (4) for $k=0, \ldots, M$ with post burn-in samples, denoted by $\left\{\mathbf{X}^{t+1}\right\}_{t=1}^{n}$. Let $k^{t}=I_{M}\left(\mathbf{X}^{t+1}\right), j^{t}=$ $J\left(\mathbf{X}^{t+1}\right), a_{t}=\sum_{k, j} \exp \left(w_{k j}^{t}\right)$, and $\exp \left(\tilde{w}_{k j}^{t}\right)=\exp \left(w_{k j}^{t}\right) / a_{t}$ such that $\sum_{k, j} \exp \left(\tilde{w}_{k j}^{t}\right)=1$. The key identity for our estimation is

$$
\frac{\sum_{t=1}^{\infty} h\left(\mathbf{X}^{t+1}\right) \exp \left(\tilde{w}_{k^{t} j^{t}}^{t}\right)}{\sum_{t=1}^{\infty} \exp \left(\tilde{w}_{k^{t} j^{t}}^{t}\right)} \xrightarrow{a . s} \int_{\mathcal{X}} h(\mathbf{x}) p(\mathbf{x}) d \mathbf{x}
$$

which follows from (11) as $\exp \left(\tilde{w}_{k^{t} j^{t}}^{t}\right) \xrightarrow{a . s} \exp \left(w_{k^{t} j^{t}}^{*}\right) \propto p\left(\mathbf{X}^{t+1}\right) / p\left(\mathbf{X}^{t+1} ; \mathbf{W}^{*}\right)$ asymptotically (9). See Liang (2009) and Atchadé and Liu (2010) for similar results. However, $\tilde{\mathbf{W}}^{t}=\left(\tilde{w}_{k j}^{t}\right)$ may be far from $\mathbf{W}^{*}$ even for post burn-in iterations. Thus, it is desired to use a weighted version of (12) so that $\mathbf{X}^{t+1}$ will carry a higher weight if $\tilde{\mathbf{W}}^{t}$ is closer to $\mathbf{W}^{*}$. Since decrease in $\gamma_{t}$ indicates convergence of the MD sampler and $a_{t+1} / a_{t} \xrightarrow{a . s} e^{c \gamma_{t}}$ for $c \in(0,1)$ (supplementary document), a reasonable choice is to weight $\mathbf{X}^{t+1}$ by $a_{t}$ so that

unnormalized $\left(w_{k j}^{t}\right)$ will be used in (12). Consequently, $D R_{p}(h)$ is constructed with

$$
\begin{aligned}
\hat{\lambda}_{k} & =\frac{\sum_{t=1}^{n} \mathbf{1}\left(\mathbf{X}^{t+1} \in D_{k}\right) \exp \left(w_{k^{t} j^{t}}^{t}\right)}{\sum_{t=1}^{n} \exp \left(w_{k^{t} j^{t}}^{t}\right)} \\
\hat{\mu}_{h, k} & =\frac{\sum_{t=1}^{n} h\left(\mathbf{X}^{t+1}\right) \mathbf{1}\left(\mathbf{X}^{t+1} \in D_{k}\right) \exp \left(w_{k^{t} j^{t}}^{t}\right)}{\sum_{t=1}^{n} \mathbf{1}\left(\mathbf{X}^{t+1} \in D_{k}\right) \exp \left(w_{k^{t} j^{t}}^{t}\right)}
\end{aligned}
$$

for $k=0, \ldots, M$. Then, $\mu_{h}=E[h(\mathbf{X})]$ is estimated by $\hat{\mu}_{h}=\sum_{k} \hat{\lambda}_{k} \hat{\mu}_{h, k}$. Please see supplementary document for more discussion on this weighted estimation.

In the next three sections we demonstrate the effectiveness of the MD sampler in statistical estimation, especially estimation of DRs, compared to the naive two-step approach. For all examples, we employ the WL algorithm with the MWL update (Routine 1) as the Monte Carlo method in the two-step approach. To minimize hidden artifacts in a comparison due to coding differences, we implement the WL algorithm with the same burn-in and main algorithms of the MD sampler. In the main algorithm (Algorithm 1) we replace the updating scheme in Equation (7) with

$$
w_{k j}^{t+1}=w_{k j}^{t}+\gamma_{t} \mathbf{1}\left(J\left(\mathbf{X}^{t+1}\right)=j\right)
$$

for $k=0, \ldots, M$ and $j=1, \ldots, L$ and modify the burn-in algorithm accordingly, so that $w_{0 j}^{t}=\cdots=w_{M j}^{t} \triangleq w_{j}^{t}$ for every iteration. Consequently, the working density is effectively

$$
p\left(\mathbf{x} ; \mathbf{W}^{t}\right) \propto \sum_{j=1}^{L} \frac{p(\mathbf{x}) \mathbf{1}(J(\mathbf{x})=j)}{\exp \left(w_{j}^{t}\right)}
$$

as used in the WL algorithm, which is a diffuse version of $p(\mathbf{x})$ such that each density partition interval will be equally sampled after convergence. Note that the same GD search is applied at each iteration to partition samples into attraction domains for estimating DRs. Our comparison aims to highlight the effect of domain partitioning and the mixed jump in the MD sampler which are the key differences from the WL algorithm.

# 4 A test example 

We test the MD sampler with an example in $\mathbb{R}^{m}$. For this example, domain-based representations can be obtained via one-dimensional numerical integration with a high accuracy, which provides the basis to evaluate our estimation. We choose $K^{*}=100$, which is greater than the total number of local modes, to construct complete DRs.

Let $\mathbf{x}=\left(x_{1}, \ldots, x_{m}\right)$. The Rastrigin function (Gordon and Whitley 1993) is defined as

$$
R(\mathbf{x})=\sum_{i=1}^{m} x_{i}^{2}+A\left[m-\sum_{i=1}^{m} \cos \left(\pi x_{i}\right)\right]
$$

where $A$ is a positive constant. We set $A=2$ and $m=4$ in (15) to obtain our target distribution $p(\mathbf{x}) \propto \exp [-R(\mathbf{x})]$, which has $3^{4}=81$ local modes formed by all the elements of the product set $\{-1.805,0,1.805\}^{4}$. These local modes have five distinct log density values, $0,-3.62,-7.24,-10.87$, and -14.49 , dependent on the combinations of their coordinates. They are grouped accordingly into five layers so that the number of zeros and the number of $\pm 1.805$ in the coordinates of a local mode at the $k$ th layer are $(5-k)$ and $(k-1)$, respectively, for $k=1, \ldots, 5$. The attraction domains of local modes at the same layer have identical probability masses and identical conditional means up to a permutation and change of signs of the coordinates.

We applied the MD sampler 100 times independently, each run with $L=10$ density partition intervals, $\Delta H=2, B=50 \mathrm{~K}$ burn-in iterations and a total of 5 million (M) iterations (including the burn-in iterations). The local proposal was simply $\mathcal{N}\left(\mathbf{X}^{t}, \mathbf{I}\right)$. The average acceptance rate was 0.26 for the local move and was 0.56 for the mixed jump. Let $\mathbf{X}=\left(X_{1}, \ldots, X_{4}\right)$ and $S=\sum_{i} X_{i}$. We estimated $E(\mathbf{X}), E\left(e^{2 S}\right), E\left(\prod_{i} X_{i}\right), E\left(\sum_{i} X_{i}^{5}\right)$, and $E\left(\sum_{i} X_{i}^{6}\right)$, all via domain-based representations. Since the target density of this example is a product of one-dimensional marginal densities, the above expectations can be calculated accurately through one-dimensional numerical integration. We compared our estimates from MD sampling with the results from numerical integration by computing mean squared errors (MSEs). We report the average MSE of the estimated log probability masses $\left(\log \lambda_{k}\right)$ and the average MSE of the estimated conditional means $\left(\boldsymbol{\mu}_{\mathbf{X}, k}\right)$ over all the local modes

Table 1: MSE comparison on the Rastrigin function


at the same layer $(k=1, \ldots, 5)$, and for other functions we only report the MSEs of the estimated expectations to save space (Table 1).

As a comparison, we also applied the WL algorithm (as in the naive two-step approach) to this problem with the same parameter setting. The ratio (RMSE) of the MSE of the WL algorithm over that of the MD sampler for each estimate is given in Table 1. The WL algorithm showed larger MSEs than the MD sampler for almost all the estimates, especially for those on domains at layers 3,4 and 5 . For example, the MD sampler was at least 16 times more efficient than the WL algorithm for estimating $\log \lambda_{5}$ and $\mu_{\mathbf{X}, 5}$. The WL algorithm did not simulate sufficient samples from these domains, although it visited uniformly different density partition intervals. On the contrary, the double-partitioning design facilitated the MD sampler to explore every domain in a uniform manner, which led to a substantial improvement in estimation for these layers. This shows the critical role of domain partitioning in estimating DRs. To study the effect of the mixed jump, we re-applied the MD sampler with $p_{m x}=0$, and calculated the ratio of the resulting MSE ( $\mathrm{MD}_{0}$ in Table 1) over that of the MD sampler with $p_{m x}=0.1$, the default setting. One sees an increase of two folds or more in MSEs without the mixed jump. The convergence of the MD sampler without the mixed jump became slower, reflected by a five-fold increase in $\gamma_{n}$ after the same number of iterations, averaging over 100 independent runs. These observations demonstrate that the mixed jump served as an efficient global move which accelerated convergence of the MD sampler and improved estimation accuracy.

# 5 Learning Bayesian networks 

A Bayesian network (BN) factorizes the joint distribution of $m$ variables $Z=\left\{Z_{1}, \ldots, Z_{m}\right\}$ into

$$
P(Z)=\prod_{i=1}^{m} P\left(Z_{i} \mid \Pi_{i}^{G}\right)
$$

where $\Pi_{i}^{G} \subset Z$ is the parent set of $Z_{i}$. A graph $G$ is constructed to code the structure of a BN by connecting each variable (node) to its child variables via directed edges. For (16) to be a well-defined joint distribution, the graph $G$ must be a DAG. We consider the use of Bayesian networks in causal inference (Spirtes, Glymour and Scheines 1993, Pearl 2000), which is tightly connected to many areas in statistics, such as structural equations, potential outcomes, and randomization (Holland 1988, Neyman 1990, Rubin 1978, Robins 1986). Here we follow Pearl's formulation of causal networks by modeling experimental intervention. If $Z_{j}$ is a parent of $Z_{i}$ in a causal Bayesian network, then experimental interventions that change the value of $Z_{j}$ may affect the distribution of $Z_{i}$, but not conversely. Once all the parents of $Z_{i}$ are fixed by intervention, the distribution of $Z_{i}$ will not be affected by interventions on any variables in the set $Z \backslash\left(\Pi_{i}^{G} \cup\left\{Z_{i}\right\}\right)$. In the example causal network of Figure 2, if we fix $Z_{1}$ and $Z_{3}$ by experimental intervention, then the distribution of $Z_{4}$ will not be affected by perturbations on $Z_{2}, Z_{5}$, or $Z_{6}$.
![img-1.jpeg](img-1.jpeg)

Figure 2: An example Bayesian network of six variables.

### 5.1 Posterior distribution

We focus on the discrete case where each $Z_{i}$ takes $r_{i}$ states indexed by $1, \ldots, r_{i}$ and the parents of $Z_{i}$ take $q_{i}=\prod_{Z_{j} \in \Pi_{i}^{G}} r_{j}$ joint states. Let $\theta_{i j k}$ be the causal probability for $Z_{i}=j$ given the $k$ th joint state of its parent set. A causal BN with a given structure $G$ is

parameterized by $\boldsymbol{\Theta}=\left\{\theta_{i j k}: \sum_{j} \theta_{i j k}=1, \theta_{i j k} \geq 0\right\}$.
We infer network structure from two types of data jointly, experimental data and observational data. For experimental data, a subset of variables are known to be fixed by intervention. Inferring causality with intervention has been extensively studied in various contexts (e.g., Robins 1986, 1987, Pearl 1993). We adopt Cooper and Yoo (1999) for calculating the posterior probability of a network structure given a mix of experimental and observational data. Suppose that $N_{i j k}$ is the number of data points for which $Z_{i}$ is not fixed by intervention and is found in state $j$ with its parent set in joint state $k$. Then, the collection of counts $\mathbf{N}=\left\{N_{i j k}\right\}$ is the sufficient statistic for $\boldsymbol{\Theta}$ (Ellis and Wong 2008). Let $\left|\Pi_{i}^{G}\right|$ be the size of the parent set of $Z_{i}$. The prior distribution over network structures is specified as $\pi(G) \propto \beta^{\sum_{i}\left|\Pi_{i}^{G}\right|}, \beta \in(0,1)$, which penalizes graphs with a large number of edges. With a product-Dirichlet prior for $\boldsymbol{\Theta}$, the posterior distribution $[G \mid \mathbf{N}]$ (Cooper and Herskovits 1992) is

$$
P(G \mid \mathbf{N}) \propto \prod_{i=1}^{m}\left\{\beta\left|\Pi_{i}^{G}\right| \prod_{k=1}^{q_{i}}\left[\frac{\Gamma\left(\alpha_{i \cdot k}\right)}{\Gamma\left(\alpha_{i \cdot k}+N_{i \cdot k}\right)} \prod_{j=1}^{r_{i}} \frac{\Gamma\left(\alpha_{i j k}+N_{i j k}\right)}{\Gamma\left(\alpha_{i j k}\right)}\right]\right\}
$$

where $\alpha_{i j k}=\alpha /\left(r_{i} q_{i}\right)$ is the pseudo count for the causal probability $\theta_{i j k}$ in the productDirichlet prior and $N_{i \cdot k}=\sum_{j} N_{i j k}$ (similarly for $\alpha_{i \cdot k}$ ). The hyperparameters in the prior distributions are chosen as $\beta=0.1$ and $\alpha=1$.

# 5.2 MD sampling over DAGs 

The space of DAGs is discrete in nature. We define domains of attraction for $P(G \mid \mathbf{N})$ (17) with a move set composed of addition, deletion and reversal of an edge. Given a DAG $G_{a}$, we say that another DAG $G_{b}$ is a neighbor of $G_{a}$ if $G_{b}$ can be obtained via a single move starting from $G_{a}$, i.e., by adding, deleting or reversing an edge of $G_{a}$. Denote by $n g b\left(G_{a}\right)$ all the neighbors of $G_{a}$ and let $\overline{n g b}\left(G_{a}\right)=n g b\left(G_{a}\right) \cup\left\{G_{a}\right\}$. A DAG $G^{*}$ is defined as a local mode of a probability density (mass) function $p(G)$ if $p\left(G^{*}\right)>p\left(G^{\prime}\right)$ for every

$G^{\prime} \in n g b\left(G^{*}\right)$. Let $G^{0}$ be a DAG and define recursively

$$
G^{t+1}=\underset{G \in \overline{n g b}\left(G^{t}\right)}{\operatorname{argmax}} p(G), \text { for } t=0,1, \ldots
$$

That is, we recursively find the single move that leads to the greatest increase in $p$ until a local mode is reached, which can be viewed as a discrete counterpart of the gradient descent algorithm. If there are more than one maximum in (18) with an identical function value, we take the first maximum according to a fixed ordering of the neighbors. We call this recursion the steepest neighbor ascent (SNA). Based on SNA, we define the domain partition index $I(G)$ and the attraction domains of $p$ in the same manner as for a differentiable density (Equation 2 and Definition 1).

The target distribution in this application is the posterior distribution $P(G \mid \mathbf{N})$ and we define working density $P(G \mid \mathbf{N} ; \mathbf{W})$ similarly as in (6). To implement the MD sampler for DAGs, we employ the move set as the local proposal and develop the following mixed jump. For a DAG $G$, we define an edge variable $E_{i j}^{G}$ for every pair of nodes $Z_{i}$ and $Z_{j}$ $(i<j)$ such that $E_{i j}^{G}=1$ if $Z_{i}$ is a parent of $Z_{j}, E_{i j}^{G}=-1$ if $Z_{j}$ is a parent of $Z_{i}$, and $E_{i j}^{G}=0$ otherwise. Given a DAG $\nu$, let $\mathbf{C}(G ; \nu)=\left(C_{a}(G ; \nu), C_{d}(G ; \nu), C_{r}(G ; \nu)\right)$ be a map of $G$, where

$$
\begin{aligned}
C_{a}(G ; \nu) & =\sum_{i<j} \mathbf{1}\left(E_{i j}^{G} \neq 0, E_{i j}^{\nu}=0\right) \\
C_{d}(G ; \nu) & =\sum_{i<j} \mathbf{1}\left(E_{i j}^{G}=0, E_{i j}^{\nu} \neq 0\right) \\
C_{r}(G ; \nu) & =\sum_{i<j} \mathbf{1}\left(E_{i j}^{G} \cdot E_{i j}^{\nu}=-1\right)
\end{aligned}
$$

In words, $\mathbf{C}(G ; \nu)$ gives the numbers of additions, deletions and reversals needed to obtain $G$ from $\nu$. Let $T=m(m-1) / 2$ be the total number of node pairs and $\left|E_{\nu}\right|$ be the number of edges in $\nu$. Then, the number of common edges between $G$ and $\nu$ is $\left|E_{\nu}\right|-$ $\left[C_{r}(G ; \nu)+C_{d}(G ; \nu)\right]$ and the number of node pairs with no edge in either DAG is $T-$ $\left|E_{\nu}\right|-C_{a}(G ; \nu)$. Given a set of local modes of $P(G \mid \mathbf{N}),\left\{\nu_{k}\right\}_{k=1}^{M}$, let $\mathbf{g}_{k}(G)=\mathbf{C}\left(G ; \nu_{k}\right)$ in the update of $\mathbf{V}_{k}^{t}$ (8) of Algorithm 1, where $\mathbf{V}_{k}^{t}=\left(v_{k, a}^{t}, v_{k, d}^{t}, v_{k, r}^{t}\right)$ is a vector. As $n \rightarrow \infty$, $\mathbf{V}_{k}^{n} \xrightarrow{\text { a.s. }} E\left[\mathbf{C}\left(G ; \nu_{k}\right) \mid G \in D_{k}\right]$, where the expectation is taken with respect to the limiting working density $P\left(G \mid \mathbf{N} ; \mathbf{W}^{*}\right)$ (10). In the mixed jump, after a local mode $\nu_{k}$ is randomly chosen, we sequentially modify the edge variables of $\nu_{k}$ to propose a new DAG $Y$. The

proposal is designed according to $\mathbf{V}_{k}^{t}$, the current estimate of the expected numbers of additions, deletions and reversals of DAGs in the domain $D_{k}$ relative to the mode $\nu_{k}$. Let $\left|E_{k}\right|$ be the number of edges in $\nu_{k}$. If $E_{i j}^{\nu_{k}} \neq 0$, we propose to reverse, delete, or retain the edge $E_{i j}^{\nu_{k}}$ (i.e., $E_{i j}^{Y}=-E_{i j}^{\nu_{k}}, 0$, or $E_{i j}^{\nu_{k}}$ ) with probabilities proportional to the vector $\left(v_{k, r}^{t}, v_{k, d}^{t},\left|E_{k}\right|-\left(v_{k, r}^{t}+v_{k, d}^{t}\right)\right)+b$, where $b>0$ is a small prior count added to each category. Analogously, if $E_{i j}^{\nu_{k}}=0$ we propose $E_{i j}^{Y}=0,1$, or $-1$ with probabilities proportional to $\left(T-\left|E_{k}\right|-v_{k, a}^{t}, v_{k, a}^{t} / 2, v_{k, a}^{t} / 2\right)+b$. Lastly, to ensure a proposed graph is acyclic, a check for cycles is performed when we propose to add or reverse an edge in either the local proposal or the mixed jump. If the resulting graph is cyclic, we suppress the probability for the corresponding move.

Following the common practice in structural learning of discrete BNs, we set an upper bound for the number of parents (indegree) of a node. In all the following examples and applications, this upper bound is chosen to be four. We are interested in the posterior expected adjacency matrix $\mathbf{A}=\left(a_{i j}\right)_{m \times m}$ and its domain-based representation, where $a_{i j}$ $(1 \leq i, j \leq m)$ is the posterior probability for a directed edge from $Z_{i}$ to $Z_{j}$. For each identified local mode $\nu_{k}$, we estimate the probability mass $\lambda_{k}$ of its attraction domain $D_{k}$ and the conditional expected adjacency matrix $\mathbf{A}_{k}$ on the domain. Then, $\mathbf{A}$ is estimated by $\hat{\mathbf{A}}=\sum_{k} \hat{\lambda}_{k} \hat{\mathbf{A}}_{k}$.

# 5.3 Simulation 

We simulated data from two BNs, each of six binary variables $\left(m=6, r_{i}=2, \forall i\right)$. This is the maximum number of nodes for which we can enumerate all DAGs, numbering about four million, to obtain true posterior distributions and domain-based representations as the ground truth for testing a computational method. The first network has a chain structure in which $Z_{i}$ is the only parent of $Z_{i+1}$ for $i=1, \ldots, 5$ and $Z_{1}$ has no parent. The second network has a more complex structure shown in Figure 2. We simulated 50 datasets independently from each network. In each dataset, $20 \%$ of the data points were generated with interventions. Please see supplementary document for data simulation details.

The MD sampler was applied to the 100 datasets with $L=15, \Delta H=10, p_{m x}=0.1$, $K^{*}=100$ and a total of 5 M iterations with the first 50 K as burn-in iterations. To verify its

Table 2: Comparison on simulated data from two BNs


The top and bottom panels report the results for the chain and the graph networks, respectively. For each estimate, reported are the MSE of the MD sampler and the RMSEs (ratios) of the other methods relative to the MD sampler.
performance, we compared identified local modes, estimated probability masses $\left\{\log \hat{\lambda}_{k}\right\}$, conditional expected adjacency matrices $\left\{\hat{\mathbf{A}}_{k}\right\}$, and expected adjacency matrix $\hat{\mathbf{A}}$ to their respective true values obtained via enumerating all DAGs. Our enumeration confirms that the posterior distributions indeed have multiple local modes. The chain and the graph (Figure 2) networks have on average 3.57 and 7.06 modes over the simulated datasets, respectively, and the maximum number of modes is 29 for the chain and 34 for the graph. As reported in Table 2, the MD sampler did not miss a single local mode for any dataset, which demonstrates its global search ability. Recall that all recorded modes are detected in the burn-in algorithm. In fact, all modes, including the global mode, were identified within 10 K iterations for every dataset. This observation confirms the notion that the burn-in algorithm alone may serve as a powerful optimization algorithm (Remark 4). We calculated the MSE of the vector $\left(\log \hat{\lambda}_{1}, \ldots, \log \hat{\lambda}_{K}\right)$, where $K$ is the number of local modes, and the average MSE of $\hat{\mathbf{A}}_{1}, \ldots, \hat{\mathbf{A}}_{K}$. When calculating the MSE of the log probability vector, we ignored those tiny domains with a probability mass $<10^{-4}$. These estimates are seen to be very accurate as reported in Table 2.

We also applied the MD sampler with $p_{m x}=0\left(\mathrm{MD}_{0}\right)$ and the WL algorithm with the same parameter setting to these datasets (Table 2). The degraded performance of $\mathrm{MD}_{0}$ demonstrates the effectiveness of the mixed jump for sampling DAGs. The WL al-

gorithm missed 0.12 modes on average for the second network, and its estimation of the $\operatorname{DR}\left\{\left(\hat{\mathbf{A}}_{k}, \hat{\lambda}_{k}\right)\right\}$ was much less accurate compared to that of the MD sampler. The average MSE of $\hat{\mathbf{A}}_{1}, \ldots, \hat{\mathbf{A}}_{K}$ and the MSE of $\left(\log \hat{\lambda}_{k}\right)_{1: K}$ were more than 10 and 1,000 times greater than those of the MD sampler, respectively. The huge MSE of the $\left(\log \hat{\lambda}_{k}\right)$ constructed by the WL algorithm was often due to severe underestimation of the probability masses of domains sampled insufficiently. This result implies that without domain partitioning, the WL algorithm is unable to estimate domain-based representations for a BN of a moderately complicated structure. Since the number of local modes often increases very fast with the complexity of a problem, we re-applied the MD sampler with $K^{*}=10$ to investigate the effect of keeping only a subset of local modes. Obviously, the algorithm missed a few local modes when the total number of modes exceeded $K^{*}$. But in terms of estimating $\mathbf{A}$ and $\mathbf{A}_{k}$, the performance of the MD sampler with $K^{*}=10$ was very comparable to its performance when all the local modes were kept (Table 2). The probability mass outside the domains of recorded modes, $\lambda_{0}=1-\sum_{k=1}^{K^{*}} \lambda_{k}$, is less than 0.007 averaging over the 15 datasets where the posterior distributions have more than 10 local modes. This confirms that the MD sampler indeed captured major modes in the burn-in period.

# 6 Protein-signaling networks 

### 6.1 Background and data

The ability of cells to properly respond to environment is the basis of development, tissue repair, and immunity. Such response is established via information flow along signaling pathways mediated by a series of signaling proteins. Cross-talks and interplay between pathways reflect the network nature of the interaction among these signaling molecules. Construction of signaling networks is an important step towards a global understanding of normal cellular responses to various environmental stimuli and more effective treatment of complex diseases caused by malfunction of components in a pathway. Causal Bayesian networks may be used for modeling signaling networks as the relation among pathway components has a natural causal interpretation. That is, the activation or inhibition of a set of upstream molecules in a network causes the state change of downstream molecules.

An edge from molecule A to molecule B in a signaling network implies that a change in the state of A causes a change in the state of B via a direct biochemical reaction. Here, a state change refers to a chemical, physical or locational modification of a molecule. However, as there may exist mutual regulation between two signaling molecules, the use of DAGs for modeling signaling networks is only a first-step approximation.

In this study, we construct protein-signaling networks from flow cytometry data. Polychromatic flow cytometry is a high-throughput technique for probing simultaneously the (phosphorylation) states of multiple proteins in a single cell. Since measurements are collected on a cell-by-cell basis, huge amounts of data can be produced in one experiment. Sachs et al. (2005) made flow cytometry measurements of 11 proteins and phospholipids in the signaling network of human primary naive $\mathrm{CD} 4^{+} \mathrm{T}$ cells under nine different experimental perturbations that either activate or inhibit a particular molecule or activate the entire pathway. Note that a perturbation that activates or inhibits a particular molecule is essentially an intervention on the molecule, so that causal structures of the underlying network may be inferred. Under each perturbation, 600 cells were collected with 11 measurements for each. The measurements in the data were discretized into three levels, high, medium, and low by Sachs et al. In summary, this dataset contains 5,400 data points for 11 ternary variables. Since naive T cells are essential for the immune system to continuously respond to unfamiliar pathogens, extensive studies have been conducted to establish the signaling pathways. An annotated signaling network among the 11 molecules, provided by Sachs et al., is depicted as a causal Bayesian network in Figure 3. This network contains 18 edges that are well-established in the literature and two edges (PKC $\rightarrow$ PKA and Erk $\rightarrow$ Akt) reported from recent experiments independent of the flow cytometry data.

# 6.2 Predicted networks 

The MD sampler was applied to this dataset with $L=20, \Delta H=10, p_{m x}=0.1$, and $K^{*}=10$. The total number of iterations was 5 M , of which the first 50 K were used for burn-in. We estimated the posterior expected adjacency matrix $\mathbf{A}$ and its domain-based representation. Three predicted networks were constructed by thresholding posterior edge probabilities at $c=0.5,0.7,0.9$, i.e., an edge from $Z_{i}$ to $Z_{j}$ was predicted if the edge

![img-2.jpeg](img-2.jpeg)

Figure 3: An annotated protein-signaling network in naive CD4+ T cells.

probability $\hat{a}_{ij} \geq c$. For simplicity we call such a predicted network a mean network (with a threshold $c$ ). Table 3 (top panel) reports the number of true positive edges (TP) that are both predicted by the MD sampler and annotated in Figure 3 and the number of false positive edges (FP) that are predicted but not annotated, together with the (unnormalized) log posterior probability of the identified global maximum DAG. To compare the results, we re-applied the MD sampler with the same parameters except that $p_{m x}=0$ (MD 0 in Table 3) and applied the WL algorithm with the same parameters as used in the MD sampler to the same data. The average result over 20 independent runs of each method is summarized in Table 3. In terms of finding the global mode, the MD sampler was much more effective and robust than the other two algorithms, reflected by a much higher average log probability and a much smaller standard deviation across multiple runs. The MD sampler with or without the mixed jump showed comparable results in predicting network structures, and both predicted more true positives and fewer false positives than the WL algorithm did for all the three thresholds. We noticed that the mean networks constructed with different thresholds $(c=0.5,0.7,0.9)$ were almost identical. This was due to the fact that the posterior edge probabilities were close to either 1 or 0 because of the large data size. The network constructed from the same data by the order-graph sampler, reported in Figure 11 of Ellis and Wong (2008), has 9 true positive and 11 false positive edges, which misses much more true edges and includes more false positives than the networks predicted by the MD sampler. These results demonstrate that the MD sampler is very powerful in learning

Table 3: Results on the flow cytometry data


The top and bottom panels report the average results over 20 independent runs on the full dataset and the average results over ten test datasets in cross validation, respectively. Predictive probabilities (Log pred) are reported as log ratios over the predictive probability given the mean network of the MD sampler.
underlying network structures from experimental data compared to other advanced Monte Carlo techniques.

Next, we focus on the estimation of the DR, $\left\{\left(\hat{\mathbf{A}}_{k}, \hat{\lambda}_{k}\right): k=0, \ldots, K^{*}\right\}$, and its scientific implications. A network $\hat{G}_{k}$ can be constructed for an attraction domain by thresholding $\hat{\mathbf{A}}_{k}$, the conditional expected adjacency matrix on the domain $D_{k}$, for $k=1, \ldots, K^{*}$. To distinguish it from the mean network, we call $\hat{G}_{k}$ a local network. We take the result of a representative run of the MD sampler $\left(p_{m x}=0.1\right)$ to demonstrate local networks with the threshold $c=0.9$. The parent sets of eight nodes are identical across the $K^{*}=10$ local networks. We report in Table 4 the parents of the other three nodes, PLC, PIP3, and Erk, which are distinct among the local networks, together with the probability masses $\left(\log \hat{\lambda}_{k}\right)$ of the 10 domains and the probabilities of the local modes $\left[\log P\left(\nu_{k} \mid \mathbf{N}\right)\right]$. The local networks may predict meaningful alternative edges not included in the mean network, as illustrated by the result on a particular pathway, Raf $\rightarrow$ Mek $\rightarrow$ Erk (Figure 3). This expected pathway was predicted by all the local networks and the mean network. However, some local networks also contained a direct link from Raf to Erk (Table 4). As Mek was inhibited in one of the experimental conditions, this finding suggests that the cells may have another pathway that passes the signal from Raf to Erk via some indirect regulation or via molecules not included in this analysis, when Mek is not functioning properly. Such

Table 4: Local networks constructed from domain-based representation


compensational mechanisms exist widely in many biological networks. Indeed, Raf has been reported to enhance the kinase activity of $\mathrm{PKC} \theta$, an isoform of PKC, although $\mathrm{PKC} \theta$ is unlikely a direct phosphorylation target of Raf (Hindley and Kolch 2007). As indicated by Figure 3, Erk is a downstream node of PKC and thus may be regulated indirectly by Raf via the enhanced kinase activity of $\mathrm{PKC} \theta$. Such novel hypotheses could not be proposed if we did not construct the DR for the posterior distribution. Clearly, the DR of network structures not only gives a detailed landscape of various local domains but also provides new insights into the underlying scientific problem.

From Table 4 we find that the probability mass is dominated by the domain of the identified global mode with a log probability of -31757 . Consistent with the summary in Table 3, the MD sampler almost always reached this global mode for different runs. On the contrary, the highest mode detected by the WL algorithm with an average log probability of -31938 is even much lower than the lowest mode in Table 4. In other words, the WL algorithm was inevitably trapped to some local modes with negligible probability masses. This again demonstrates the advantage of the MD sampler, particularly the burn-in algorithm, in finding global modes. Even when the probability mass of the global mode is dominant and other domains occupy only a small fraction of the sample space, without the domain-partitioning design the WL algorithm may be trapped to a local mode of a tiny probability mass and produce severely biased estimates.

# 6.3 Cross validation 

To check the statistical variability and the predictive power of our method, we conducted ten-fold cross validation on this dataset. We partitioned randomly the 5,400 data points into ten subsets of equal sizes. We used nine subsets as training data to learn a mean network and calculated the predictive probability of data points in the other subset (test data) given the learned mean network. This procedure was repeated 10 times to test on every subset. We verified the average accuracy of the mean networks constructed from the 10 training datasets with different thresholds. The performance of the MD sampler on the training datasets was comparable to its performance on the full dataset, which implies its robustness to random sampling of input data. The improvement in accuracy (TP/FP) of the MD sampler over the other two methods became more significant, especially compared to the WL algorithm (Table 3, bottom panel). The average predictive probability of the test datasets given the mean networks constructed from the training datasets by each method with $c=0.9$ is reported in Table 3 [Log pred (mean)], from which we see that the predictive power of the networks constructed by the two MD samplers was much higher than that of the WL algorithm ( $>60$ in log probability ratio). In addition, we utilized the estimated domain-based representations to calculate the predictive probability of a test data point $\mathbf{y}$ by

$$
P\left(\mathbf{y} \mid\left\{\hat{G}_{k}, \hat{\lambda}_{k}\right\}\right) \triangleq \sum_{k=0}^{K^{*}} \hat{\lambda}_{k} P\left(\mathbf{y} \mid \hat{G}_{k}\right)
$$

where $P\left(\mathbf{y} \mid \hat{G}_{k}\right)$ is the marginal likelihood of $\mathbf{y}$ given the local network $\hat{G}_{k}$. This can be regarded as a domain-based approximation to the posterior predictive distribution

$$
P\left(\mathbf{y} \mid \mathbf{y}_{o b s}\right)=\sum_{G} P\left(G \mid \mathbf{y}_{o b s}\right) P(\mathbf{y} \mid G)
$$

i.e., we use estimated probability masses $\hat{\lambda}_{k}$ and conditional mean networks $\hat{G}_{k}$ to approximate the posterior predictive probability. The advantage is that there is no need to store a large posterior sample of networks but only an estimated DR. Since Equation (19) captures the variability among different domains, it is expected to outperform the mean network in prediction. In fact, for each method the predictive probability calculated by (19) [Table 3,

Log pred (DR)] was indeed significantly greater than the predictive probability calculated given its mean network, especially for the two MD samplers.

In real applications, we are interested in predicting results for a new experimental condition given observed data from other conditions. Thus, we also performed a nine-fold cross validation where a training dataset was composed of cells from eight experimental conditions and a test dataset only included cells in the other one condition. We applied the MD sampler to construct mean networks and DRs $\left\{\hat{G}_{k}, \hat{\lambda}_{k}\right\}_{k=1}^{10}$ from the training datasets. The mean networks with $c=0.9$ included, on average, 13.2 true edges with 10.8 false edges, which was slightly worse than the result from the ten-fold cross validation. The degraded performance is expected as removing all cells from one experimental perturbation will increase the uncertainty in determining the directionality of the network. The domainbased prediction (19) was compared against the annotated network $G^{*}$ given in Figure 3, which presumably has the highest predictive power, by evaluating the log likelihood ratio (LLR) $\log R=\log \left[P\left(\mathbf{y} \mid\left\{\hat{G}_{k}, \hat{\lambda}_{k}\right\}\right) / P\left(\mathbf{y} \mid G^{*}\right)\right]$, where $\mathbf{y}$ is a test data point. The average $\log R$ over all test data points was -0.062 , and thus the predictive probability for a new observation given the constructed DR is expected to be higher than $94 \%\left(=e^{-0.062}\right)$ of its likelihood given the annotated graph. This demonstrates the high predictive power of the domain-based prediction constructed by our method. As expected, the average LLR of the mean networks over $G^{*}$ was $26 \%$ lower than the average of $\log R$.

# 7 Discussion 

The central idea of this article is to construct domain-based representations with the MD sampler. Related works have been seen in the physics literature under the name of superposition approximation. Please see Wales and Bogdan (2006) for a recent review. Given a Boltzmann distribution $p_{B}(\mathbf{x} ; \tau) \propto \exp [-H(\mathbf{x}) / \tau]$, a superposition approach identifies the local minima of $H(\mathbf{x})$, i.e., the local modes of $p_{B}(\mathbf{x} ; \tau)$, and approximates $H(\mathbf{x})$ on the attraction domain of a local minimum by quadratic or high-order functions. The approximation is often proposed based on expert knowledge about the physical model under study. Expectations with respect to $p_{B}(\mathbf{x} ; \tau)$ are then estimated by summing over approximations

from identified domains. The accuracy of this approach largely depends on the employed approximation to $H(\mathbf{x})$ on a domain and thus may not work well for an arbitrary distribution. The MD sampler differs in that domain-based representations are constructed by Monte Carlo sampling which is able to provide accurate estimation with large-size samples; no expert knowledge about the target distribution is needed. In addition, our method also contains a coherent component for finding local modes, while the superposition approximation works more like a two-step approach.

From a computational perspective, the MD sampler integrates Monte Carlo and deterministic optimization. A few other methods also have the two ingredients, such as Monte Carlo optimization (Li and Scheraga 1987), the basin hopping algorithm (Wales and Doye 1997), and conjugate gradient Monte Carlo (CGMC) (Liu, Liang, and Wong 2000). In Monte Carlo optimization and the basin hopping algorithm, the target distribution $p(\mathbf{x})$ is modified to $\tilde{p}(\mathbf{x})=p\left(\boldsymbol{\nu}_{k}\right)$ for all $\mathbf{x} \in D_{k}$, where $D_{k}$ is the attraction domain of the mode $\boldsymbol{\nu}_{k}$. Then a Metropolis-type MCMC is used to sample from $\tilde{p}$, in which a local optimization algorithm is employed at each iteration to find $\tilde{p}\left(\mathbf{X}^{t}\right)$ for the current state $\mathbf{X}^{t}$. These methods have been applied to identification of minimum-energy structures of proteins and other molecules. However, its application to other fields is limited as the modified density $\tilde{p}(\mathbf{x})$ may be improper when the sample space is unbounded. In CGMC, a population of samples is evolved and a line sampling step (Gilks, Roberts, and George 1994) is performed on a sample along a direction pointing to a local mode found by local optimization initiated at another sample. In this way promising proposal may be constructed by borrowing local mode information from other samples. A possible future work on the MD sampler is to utilize a population of samples. Because local modes are recorded, similar proposals as the line sampling can be developed for the MD sampler to further enhance sampling effectiveness. Another future direction is to construct disconnectivity graphs (Becker and Karplus 1997) or trees of sublevel sets (Zhou and Wong 2008) from samples generated by the MD sampler. Since samples have been partitioned into domains of attraction, we only need to determine the barrier between a pair of domains, defined by $\max _{s \in \mathcal{S}} \min _{\mathbf{x} \in s} p(\mathbf{x})$, where $\mathcal{S}$ is the collection of all the paths between the two domains. A few candidate approaches towards this direction are under current investigation (Zhou 2011).

# Appendix: Theoretical analysis 

In this Appendix we establish the convergence and ergodicity properties of the MD sampler. Our analysis is conducted for a doubly adaptive MCMC, i.e., both the target distribution and the proposal may change along the iteration, which includes the MD sampler as a special case. Furthermore, the MWL design (Routine 1) is employed to adjust $\gamma_{t}$.

Assume that the sample space $\mathcal{X}$ is equipped with a countably generated $\sigma$-field, $\mathcal{B}(\mathcal{X})$. Let $\left\{\mathcal{X}_{i}\right\}_{i=1}^{\kappa}$ be a partition of $\mathcal{X}$, where each $\mathcal{X}_{i}$ is nonempty, and $\mathcal{B}\left(\mathcal{X}_{i}\right)=\{A \in \mathcal{B}(\mathcal{X}): A \subseteq$ $\left.\mathcal{X}_{i}\right\}$ for $i=1, \ldots, \kappa$. Let $\boldsymbol{\omega}=\left(\omega_{i}\right)_{1: \kappa} \in \Omega$ and $\boldsymbol{\phi} \in \Phi$ be two vectors of real parameters. Denote the product parameter space by $\Theta=\Omega \times \Phi$ and write $\boldsymbol{\theta}=(\boldsymbol{\omega}, \boldsymbol{\phi}) \in \Theta$. For $\boldsymbol{\omega} \in \Omega$, define working density

$$
p_{\boldsymbol{\omega}}(\mathbf{x}) \propto \sum_{i=1}^{\kappa} e^{-\omega_{i}} p(\mathbf{x}) \mathbf{1}\left(\mathbf{x} \in \mathcal{X}_{i}\right)
$$

Let $q(\mathbf{x}, \cdot)$ and $t_{\boldsymbol{\phi}}(\mathbf{x}, \cdot), \boldsymbol{\phi} \in \Phi$, be two transition kernels on $(\mathcal{X}, \mathcal{B}(\mathcal{X}))$. Hereafter, the same notation will be used for a kernel and its density with respect to the Lebesgue measure on $\mathcal{X}$, e.g., $q(\mathbf{x}, d \mathbf{y}) \equiv q(\mathbf{x}, \mathbf{y}) d \mathbf{y}$. For $j=0,1$, define $Q_{j, \boldsymbol{\phi}}(\mathbf{x}, \cdot)=(1-j) q(\mathbf{x}, \cdot)+j t_{\boldsymbol{\phi}}(\mathbf{x}, \cdot)$. Let $K_{j, \boldsymbol{\theta}}$ be the MH transition kernel with $p_{\boldsymbol{\omega}}$ as the target distribution and $Q_{j, \boldsymbol{\phi}}$ as the proposal, i.e.,

$$
K_{j, \boldsymbol{\theta}}(\mathbf{x}, d \mathbf{y})=S_{j, \boldsymbol{\theta}}(\mathbf{x}, d \mathbf{y})+\mathbf{1}(\mathbf{x} \in d \mathbf{y})\left[1-\int_{\mathcal{X}} S_{j, \boldsymbol{\theta}}(\mathbf{x}, d \mathbf{z})\right]
$$

where $S_{j, \boldsymbol{\theta}}(\mathbf{x}, d \mathbf{y})=Q_{j, \boldsymbol{\phi}}(\mathbf{x}, d \mathbf{y}) \min \left[1, p_{\boldsymbol{\omega}}(\mathbf{y}) Q_{j, \boldsymbol{\phi}}(\mathbf{y}, \mathbf{x}) / p_{\boldsymbol{\omega}}(\mathbf{x}) Q_{j, \boldsymbol{\phi}}(\mathbf{x}, \mathbf{y})\right]$, representing an accepted move. As $Q_{0, \boldsymbol{\phi}}=q, K_{0, \boldsymbol{\theta}}$ and $S_{0, \boldsymbol{\theta}}$ do not depend on $\boldsymbol{\phi}$ and thus reduce to $K_{0, \boldsymbol{\omega}}$ and $S_{0, \boldsymbol{\omega}}$, respectively. Furthermore, if we let $\boldsymbol{\omega}=\mathbf{0}$ then $p_{\boldsymbol{\omega}}(\mathbf{x})=p(\mathbf{x})$, in which case we simply use $K_{0}$ and $S_{0}$. Given $\alpha \in[0,1)$, define a mixture proposal $Q_{\boldsymbol{\phi}}=(1-\alpha) q+\alpha t_{\boldsymbol{\phi}}$, its accepted move $S_{\boldsymbol{\theta}}=(1-\alpha) S_{0, \boldsymbol{\omega}}+\alpha S_{1, \boldsymbol{\theta}}$, and the corresponding MH kernel $K_{\boldsymbol{\theta}}=(1-\alpha) K_{0, \boldsymbol{\omega}}+\alpha K_{1, \boldsymbol{\theta}}$. Table 5 summarizes the notations, from left to right, for target distributions, proposals, MH kernels, and accepted moves for different scenarios involved in this analysis.

Denote by $Z(\boldsymbol{\omega})$ the normalizing constant of (20). Then $Z(\boldsymbol{\omega})=\sum_{i=1}^{\kappa} Z_{i}\left(\omega_{i}\right)$, where $Z_{i}\left(\omega_{i}\right)=e^{-\omega_{i}} \int_{\mathcal{X}_{i}} p(\mathbf{x}) d \mathbf{x}$. Let $U$ be a nonempty subset of $\{1, \ldots, \kappa\}$ and $\mathcal{X}_{U}=\bigcup_{i \in U} \mathcal{X}_{i}$. Given a map $\mathbf{g}: \mathcal{X} \rightarrow \Phi$, let $\boldsymbol{\mu}_{\mathbf{g}, U}(\boldsymbol{\omega})=E\left[\mathbf{g}(\mathbf{X}) \mid \mathbf{X} \in \mathcal{X}_{U}\right]$ with respect to $p_{\boldsymbol{\omega}}$. Define a

Table 5: Summary of notations


$\operatorname{map} \mathbf{H}: \Theta \times \mathcal{X} \rightarrow \Theta$ by

$$
\mathbf{H}(\boldsymbol{\theta}, \mathbf{x})=\left[\left(\mathbf{1}\left(\mathbf{x} \in \mathcal{X}_{i}\right)-1 / \kappa\right)_{1: \kappa},(\mathbf{g}(\mathbf{x})-\boldsymbol{\phi}) \mathbf{1}\left(\mathbf{x} \in \mathcal{X}_{U}\right)\right]
$$

and the mean field $\mathbf{F}(\boldsymbol{\theta})=\int_{\mathcal{X}} \mathbf{H}(\boldsymbol{\theta}, \mathbf{x}) p_{\boldsymbol{\omega}}(\mathbf{x}) d \mathbf{x}$, i.e.,

$$
\mathbf{F}(\boldsymbol{\theta})=\left[\left(\frac{Z_{i}\left(\omega_{i}\right)}{Z(\boldsymbol{\omega})}-\frac{1}{\kappa}\right)_{1: \kappa}, \frac{\sum_{u \in U} Z_{u}\left(\omega_{u}\right)}{Z(\boldsymbol{\omega})}\left(\boldsymbol{\mu}_{\mathbf{g}, U}(\boldsymbol{\omega})-\boldsymbol{\phi}\right)\right]
$$

Consider the equation $\mathbf{F}(\boldsymbol{\theta})=\mathbf{0}$. Let $\boldsymbol{\omega}^{*}=\left[\log Z_{i}(0)\right]_{1: \kappa}$ and $\boldsymbol{\phi}^{*}=\boldsymbol{\mu}_{\mathbf{g}, U}\left(\boldsymbol{\omega}^{*}\right)$. As $\mathbf{F}(\boldsymbol{\theta})$ is invariant to translation of $\boldsymbol{\omega}$ by a scalar: $\boldsymbol{\omega} \rightarrow(\boldsymbol{\omega}+\beta) \stackrel{\Delta}{=}\left(\omega_{i}+\beta\right)_{1: \kappa}, \beta \in \mathbb{R}$, the solution set to this equation is $\left\{\boldsymbol{\theta}^{*}(\beta) \stackrel{\Delta}{=}\left(\boldsymbol{\omega}^{*}+\beta, \boldsymbol{\phi}^{*}\right)\right\} \cap \Theta \stackrel{\Delta}{=} \Theta^{*}$. Set $\gamma_{1}=1$ and choose an arbitrary point $(\tilde{\mathbf{x}}, \tilde{\boldsymbol{\theta}}) \in \mathcal{X} \times \Theta$ to initialize $\left(\mathbf{X}^{1}, \boldsymbol{\theta}^{1}\right)$. A doubly adaptive MCMC is employed to find a solution $\boldsymbol{\theta}^{*}(\beta) \in \Theta^{*}$ and to estimate $\mu_{h}\left(\boldsymbol{\omega}^{*}\right)=\int_{\mathcal{X}} h(\mathbf{x}) p_{\boldsymbol{\omega}^{*}}(\mathbf{x}) d \mathbf{x}$ for a function $h: \mathcal{X} \rightarrow \mathbb{R}$.

Algorithm 3 (Doubly adaptive MCMC). Choose a fixed $\alpha \in[0,1)$. For $t=1, \ldots, n$ :

1. If $\boldsymbol{\theta}^{t} \notin \Theta$, set $\mathbf{X}^{t+1}=\tilde{\mathbf{x}}$ and $\boldsymbol{\theta}^{t+1}=\tilde{\boldsymbol{\theta}}$; otherwise draw $\mathbf{X}^{t+1} \sim K_{\boldsymbol{\theta}^{t}}\left(\mathbf{X}^{t}, \cdot\right)$ and set $\boldsymbol{\theta}^{t+1}=\boldsymbol{\theta}^{t}+\gamma_{t} \mathbf{H}\left(\boldsymbol{\theta}^{t}, \mathbf{X}^{t+1}\right)$.
2. Determine $\gamma_{t+1}$ by the MWL design in Routine 1 with $\left\{\mathcal{X}_{i}\right\}$ in place of $\left\{D_{k j}\right\}$.

Denote the $L_{2}$ norm by $|\cdot|$ and let $d(\mathbf{x}, A) \stackrel{\Delta}{=} \inf _{\mathbf{y} \in A}|\mathbf{x}-\mathbf{y}|$, where $\mathbf{x}, \mathbf{y}$ are vectors and $A$ is a set. Our goal is to establish that $d\left(\boldsymbol{\theta}^{n}, \Theta^{*}\right) \rightarrow 0$ almost surely (with respect to the probability measure of the process $\left\{\mathbf{X}^{t}, \boldsymbol{\theta}^{t}\right\}$ ) and that $\left\{\mathbf{X}^{t}\right\}$ is ergodic. Clearly, translation of $\boldsymbol{\omega}^{t}$ by a scaler does not change the working density $p_{\boldsymbol{\omega}^{t}}$ or affect the convergence of $\boldsymbol{\theta}^{t}$ to $\Theta^{*}$. Thus, the theory for Algorithm 3 can be applied to the MD sampler with reinitialization (Remark 2). The update of $\boldsymbol{\omega}^{t}$, up to translation by a scalar, and the update of $\boldsymbol{\phi}^{t}$ correspond to, respectively, the update of $\mathbf{W}^{t}$ (7) and the update of $\mathbf{V}_{k}^{t}$ (8) for any $k$ in the MD sampler. We state four conditions for establishing the main results.

(C1) The sample space $\mathcal{X}$ is compact, $p(\mathbf{x})>0$ for all $\mathbf{x} \in \mathcal{X}, \Theta$ is bounded, and $\Theta^{*}$ is nonempty. The map $\mathbf{g}$ and the function $h$ are $p$-integrable and bounded.
(C2) There exist $\delta_{q}>0$ and $\epsilon_{q}>0$ such that $|\mathbf{x}-\mathbf{y}| \leq \delta_{q}$ implies that $q(\mathbf{x}, \mathbf{y}) \geq \epsilon_{q}$ for all $\mathbf{x}, \mathbf{y} \in \mathcal{X}$.
(C3) There exist an integer $\ell, \delta>0$ and a probability measure $\nu$, such that $\nu\left(\mathcal{X}_{i}\right)>0$ for $i=1, \ldots, \kappa$ and $S_{0}^{\ell}(\mathbf{x}, A) \geq \delta \nu(A), \forall \mathbf{x} \in \mathcal{X}$ and $A \in \mathcal{B}(\mathcal{X})$.
(C4) For all $\mathbf{x}, \mathbf{y} \in \mathcal{X}$ and all $\boldsymbol{\phi} \in \Phi, t_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y})>0$ and $\log t_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y})$ has continuous partial derivatives with respect to all the components of $\boldsymbol{\phi}$.

To avoid mathematical complexity, we assume that $\mathcal{X}$ is compact (C1). This assumption does not lose much generality in practice as we may always restrict the sample space to $\left\{\mathbf{x}: p(\mathbf{x}) \geq \epsilon_{p}\right\}$ given an sufficiently small $\epsilon_{p}$. Due to the compactness of $\mathcal{X}$, any continuous map and function on $\mathcal{X}$ will be bounded. Conditions (C2, C3) are standard conditions on the fixed proposal $q(\mathbf{x}, \mathbf{y})$ to guarantee irreducibility and aperiodicity of the MH kernel $K_{0}$. They are satisfied by all the local moves used in this article. A regularity condition on the adaptive proposal $t_{\boldsymbol{\phi}}$ is specified in (C4). For the mixed jumps in the examples, $\boldsymbol{\phi}$ is either the covariance matrix of a multivariate normal distribution or the cell probability vector of a multinomial distribution, and (C4) is satisfied.

Lemma 1. Let $\alpha \in[0,1)$. For any $i, j \in\{1, \ldots, \kappa\}$ and $\boldsymbol{\theta} \in \Theta$, if $e^{\omega_{i}-\omega_{j}} \geq c_{1} \in(0,1]$ then $K_{\boldsymbol{\theta}}(\mathbf{x}, A) \geq(1-\alpha) c_{1} S_{0}(\mathbf{x}, A), \forall \mathbf{x} \in \mathcal{X}_{i}$ and $A \in \mathcal{B}\left(\mathcal{X}_{j}\right)$.

Proof. By definition, $K_{\boldsymbol{\theta}}(\mathbf{x}, A) \geq(1-\alpha) K_{0, \boldsymbol{\omega}}(\mathbf{x}, A) \geq(1-\alpha) S_{0, \boldsymbol{\omega}}(\mathbf{x}, A)$ for every $\boldsymbol{\theta}=(\boldsymbol{\omega}, \boldsymbol{\phi})$. For any $\mathbf{x} \in \mathcal{X}_{i}$ and $\mathbf{y} \in \mathcal{X}_{j}$,

$$
\begin{aligned}
S_{0, \boldsymbol{\omega}}(\mathbf{x}, d \mathbf{y}) & =q(\mathbf{x}, d \mathbf{y}) \min \left[1, e^{\omega_{i}-\omega_{j}} \frac{p(\mathbf{y}) q(\mathbf{y}, \mathbf{x})}{p(\mathbf{x}) q(\mathbf{x}, \mathbf{y})}\right] \\
& \geq c_{1} q(\mathbf{x}, d \mathbf{y}) \min \left[1, \frac{p(\mathbf{y}) q(\mathbf{y}, \mathbf{x})}{p(\mathbf{x}) q(\mathbf{x}, \mathbf{y})}\right]=c_{1} S_{0}(\mathbf{x}, d \mathbf{y})
\end{aligned}
$$

Thus, $K_{\boldsymbol{\theta}}(\mathbf{x}, A) \geq(1-\alpha) c_{1} S_{0}(\mathbf{x}, A)$ for all $A \in \mathcal{B}\left(\mathcal{X}_{j}\right)$.

Theorem 2. If (C1)-(C4) hold, then $d\left(\boldsymbol{\theta}^{n}, \Theta^{*}\right) \xrightarrow{a . s} 0$ and

$$
\frac{1}{n} \sum_{t=1}^{n} h\left(\mathbf{X}^{t}\right) \xrightarrow{a . s} \mu_{h}\left(\boldsymbol{\omega}^{*}\right), \text { as } n \rightarrow \infty
$$

Proof. Lemma 1 and (C3) implies that $\forall \mathbf{x} \in \mathcal{X}_{i}, K_{\boldsymbol{\theta}}^{\ell}\left(\mathbf{x}, \mathcal{X}_{j}\right) \geq \epsilon_{\nu} \nu\left(\mathcal{X}_{j}\right)>0$ if $e^{\omega_{i}-\omega_{j}} \geq c_{1}$, where $\epsilon_{\nu}>0$. By Theorem 4.2 of Atchadé and Liu (2010),

$$
\max _{i, j} \limsup _{n \rightarrow \infty}\left|v_{i}^{n}-v_{j}^{n}\right|<\infty, \text { a.s. }
$$

where $v_{i}^{n}=\sum_{t=1}^{n} \mathbf{1}\left(\mathbf{X}^{t} \in \mathcal{X}_{i}\right)$. This implies that the $\left\{\gamma_{t}\right\}$ defined by the MWL update (Routine 1) will decrease below any given $\epsilon_{\gamma}>0$ after a finite number of iterations, i.e., $t_{c}<\infty$, almost surely. Then, Algorithm 3 becomes a stochastic approximation algorithm with a deterministic sequence of $\left\{\gamma_{t}\right\}$. According to Proposition 6.1 and Theorem 5.5 in Andrieu et al. (2005), we only need to verify the drift conditions (DRI1-3) and assumptions (A1, A4) given in that paper to show the convergence of $\boldsymbol{\theta}^{n}$.

Verifying the drift conditions. Let $\mathcal{D}$ be any compact subset of $\Theta$, and $\mathcal{D}_{1}$ and $\mathcal{D}_{2}$ be the projections of $\mathcal{D}$ into $\Omega$ and $\Phi$, respectively. Since $\mathcal{D}_{1}$ is compact, there is an $\epsilon_{\mathcal{D}} \in(0,1]$ such that $\min _{i, j} \inf _{\boldsymbol{\omega} \in \mathcal{D}_{1}} e^{\omega_{i}-\omega_{j}} \geq \epsilon_{\mathcal{D}}$. By Lemma 1 and (C3), there is a $\delta_{\mathcal{D}}>0$ such that

$$
\inf _{\boldsymbol{\theta} \in \mathcal{D}} K_{\boldsymbol{\theta}}^{\ell}(\mathbf{x}, A) \geq \delta_{\mathcal{D}} \nu(A), \forall \mathbf{x} \in \mathcal{X}, A \in \mathcal{B}(\mathcal{X})
$$

where $\ell$ and $\nu$ are defined in (C3). This gives the minorization condition in (DRI1). Given (C2) and that $p_{\boldsymbol{\omega}}, \boldsymbol{\omega} \in \mathcal{D}_{1}$, is bounded away from 0 and $\infty$ under (C1), $K_{0, \boldsymbol{\omega}}$ is irreducible and aperiodic for every $\boldsymbol{\omega} \in \mathcal{D}_{1}$, according to Theorem 2.2 of Roberts and Tweedie (1996). Consequently, for every $\boldsymbol{\theta} \in \mathcal{D}, K_{\boldsymbol{\theta}}$ is also irreducible and aperiodic as $\alpha<1$. Let $V(\mathbf{x})=1$ for all $\mathbf{x} \in \mathcal{X}$. It is then easy to verify other conditions in (DRI1).

Since both $\mathbf{g}$ and $\Theta$ are bounded (C1), there is a $c_{2}>0$ such that for all $\mathbf{x} \in \mathcal{X}$,

$$
\begin{gathered}
\sup _{\boldsymbol{\theta} \in \Theta}|\mathbf{H}(\boldsymbol{\theta}, \mathbf{x})| \leq \kappa+|\mathbf{g}(\mathbf{x})|+\sup _{\boldsymbol{\phi} \in \Phi}|\boldsymbol{\phi}| \leq c_{2} \\
\left|\mathbf{H}(\boldsymbol{\theta}, \mathbf{x})-\mathbf{H}\left(\boldsymbol{\theta}^{\prime}, \mathbf{x}\right)\right| \leq\left|\boldsymbol{\phi}-\boldsymbol{\phi}^{\prime}\right| \leq c_{2}\left|\boldsymbol{\theta}-\boldsymbol{\theta}^{\prime}\right|, \forall \boldsymbol{\theta}, \boldsymbol{\theta}^{\prime} \in \Theta
\end{gathered}
$$

These two inequalities imply (DRI2) with $V(\mathbf{x})=1$.
Condition (DRI3) can be verified by the same argument used in Liang et al. (2007) once we find a constant $c_{3}>0$ such that

$$
\left|\frac{\partial S_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{y})}{\partial \theta_{i}}\right| \leq c_{3} Q_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y})
$$

for all $\mathbf{x}, \mathbf{y} \in \mathcal{X}, \boldsymbol{\theta} \in \mathcal{D}$ and all $i$, where $\theta_{i}$ is the $i$ th component of $\boldsymbol{\theta}=(\boldsymbol{\omega}, \boldsymbol{\phi})$. Denote by $\phi_{j}$ the $j$ th component of $\boldsymbol{\phi}$. Straightforward calculation leads to $\left|\partial S_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{y}) / \partial \omega_{i}\right| \leq Q_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y})$ and

$$
\frac{\partial S_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{y})}{\partial \phi_{j}}= \begin{cases}R_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{y})\left[\partial \log t_{\boldsymbol{\phi}}(\mathbf{y}, \mathbf{x}) / \partial \phi_{j}\right] \alpha t_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y}), & \text { if } R_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{y})<1 \\ {\left[\partial \log t_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y}) / \partial \phi_{j}\right] \alpha t_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y}),} & \text { otherwise }\end{cases}
$$

where $R_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{y})=p_{\boldsymbol{\omega}}(\mathbf{y}) t_{\boldsymbol{\phi}}(\mathbf{y}, \mathbf{x}) / p_{\boldsymbol{\omega}}(\mathbf{x}) t_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y})$. Condition (C4) with the compactness of $\mathcal{D}_{2}$ and $\mathcal{X}$ guarantees that

$$
\sup _{\mathbf{x}, \mathbf{y} \in \mathcal{X}} \sup _{\boldsymbol{\phi} \in \mathcal{D}_{2}}\left|\partial \log t_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y}) / \partial \phi_{j}\right|<\infty
$$

As $\alpha t_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y}) \leq Q_{\boldsymbol{\phi}}(\mathbf{x}, \mathbf{y})$, (25) holds and (DRI3) is verified.
Verifying assumptions (A1, A4). It is assumed in assumption (A1) the existence of a global Lyapunov function for $\mathbf{F}(\boldsymbol{\theta})$. Let $L(\boldsymbol{\theta})=\frac{c_{4}}{2} \sum_{i=1}^{\kappa}\left(Z_{i}\left(\omega_{i}\right)-\bar{Z}(\boldsymbol{\omega})\right)^{2}+\frac{1}{2}\left|\boldsymbol{\phi}-\boldsymbol{\mu}_{\mathbf{g}, U}(\boldsymbol{\omega})\right|^{2}$, where $\bar{Z}(\boldsymbol{\omega})=Z(\boldsymbol{\omega}) / \kappa$. Using straightforward algebra one can show that

$$
-Z\langle\nabla L, \mathbf{F}\rangle=\sum_{i=1}^{\kappa} c_{4} Z_{i} \cdot\left(\Delta Z_{i}\right)^{2}+(\Delta \boldsymbol{\phi})^{\top} \sum_{u \in U} \Delta Z_{u} \frac{\partial \boldsymbol{\mu}_{\mathbf{g}, U}(\boldsymbol{\omega})}{\partial \omega_{u}}+\sum_{u \in U} Z_{u}|\Delta \boldsymbol{\phi}|^{2}
$$

where $\Delta Z_{i}=Z_{i}\left(\omega_{i}\right)-\bar{Z}(\boldsymbol{\omega}), \Delta \boldsymbol{\phi}=\boldsymbol{\phi}-\boldsymbol{\mu}_{\mathbf{g}, U}(\boldsymbol{\omega})$, and the arguments $\left(\omega_{i}\right.$ and $\left.\boldsymbol{\omega}\right)$ in $Z_{i}\left(\omega_{i}\right)$ and $Z(\boldsymbol{\omega})$ have been dropped. Since $\Theta$ is bounded, $Z_{i}\left(\omega_{i}\right)>\epsilon_{\Omega}>0$ for all $i$. Because $\mathbf{g}$ is $p$-integrable, $\boldsymbol{\mu}_{\mathbf{g}, i} \stackrel{\Delta}{=} \boldsymbol{\mu}_{\mathbf{g},\{i\}}(\mathbf{0})$ is bounded for all $i$ and

$$
\left|\frac{\partial \boldsymbol{\mu}_{\mathbf{g}, U}(\boldsymbol{\omega})}{\partial \omega_{u}}\right| \leq\left|\boldsymbol{\mu}_{\mathbf{g}, u}\right|+\max _{i \in U}\left|\boldsymbol{\mu}_{\mathbf{g}, i}\right| \leq 2 \max _{1 \leq i \leq \kappa}\left|\boldsymbol{\mu}_{\mathbf{g}, i}\right|<\infty
$$

Thus, choosing a sufficiently large $c_{4}$ ensures that $\langle\nabla L(\boldsymbol{\theta}), \mathbf{F}(\boldsymbol{\theta})\rangle \leq 0$ for any $\boldsymbol{\theta} \in \Theta$ with equality if and only if $\boldsymbol{\theta} \in \Theta^{*}$. Furthermore, $\left\{\boldsymbol{\theta} \in \Theta: L(\boldsymbol{\theta}) \leq C_{L}\right\}$ is compact for some $C_{L}>$

0 and the closure of $L\left(\Theta^{*}\right)$ has an empty interior. Thus, all the conditions in assumption (A1) are satisfied. Since $\left|\boldsymbol{\theta}^{t+1}-\boldsymbol{\theta}^{t}\right| \leq \gamma_{t} \sup _{\boldsymbol{\theta}, \mathbf{x}}|\mathbf{H}(\boldsymbol{\theta}, \mathbf{x})| \leq c_{2} \gamma_{t}$ (23) and $\gamma_{t}=1 /(t+\xi)$ for $t>t_{c}$, verifying assumption (A4) is immediate. This completes the proof of the convergence of $\boldsymbol{\theta}^{n}$.

The result (21) can be established similarly as the proof of Proposition 6.2 in Atchadé and Liu (2010). We only give an outline here. The drift conditions imply that for any $\boldsymbol{\theta} \in \mathcal{D}$, there exist $h_{\boldsymbol{\theta}}(\mathbf{x}), c_{5}>0$, and $b \in(0,1]$ such that $h_{\boldsymbol{\theta}}-K_{\boldsymbol{\theta}} h_{\boldsymbol{\theta}}=h-\mu_{h}(\boldsymbol{\omega})$ and

$$
\begin{gathered}
\sup _{\boldsymbol{\theta} \in \mathcal{D}}\left(\left\|h_{\boldsymbol{\theta}}\right\|+\left\|K_{\boldsymbol{\theta}} h_{\boldsymbol{\theta}}\right\|\right)<\infty \\
\left\|h_{\boldsymbol{\theta}}-h_{\boldsymbol{\theta}^{\prime}}\right\|+\left\|K_{\boldsymbol{\theta}} h_{\boldsymbol{\theta}}-K_{\boldsymbol{\theta}^{\prime}} h_{\boldsymbol{\theta}^{\prime}}\right\|<c_{5}\left|\boldsymbol{\theta}-\boldsymbol{\theta}^{\prime}\right|^{b}, \forall \boldsymbol{\theta}, \boldsymbol{\theta}^{\prime} \in \mathcal{D}
\end{gathered}
$$

where $K_{\boldsymbol{\theta}} h_{\boldsymbol{\theta}}(\mathbf{x})=\int_{\mathcal{X}} K_{\boldsymbol{\theta}}(\mathbf{x}, d \mathbf{y}) h_{\boldsymbol{\theta}}(\mathbf{y})$ and for $f: \mathcal{X} \rightarrow \mathbb{R},\|f\|=\sup _{\mathbf{x} \in \mathcal{X}}|f(\mathbf{x})|$. See Proposition 6.1 and assumption (A3) of Andrieu et al. (2005). Then, following an essentially identical proof to that of Lemma 6.6 in Atchadé and Liu (2010), we can show that $\sum_{t=1}^{\infty} t^{-1}\left[h\left(\mathbf{X}^{t+1}\right)-\mu_{h}\left(\boldsymbol{\omega}^{t}\right)\right]$ has a finite limit almost surely. Since $\mu_{h}\left(\boldsymbol{\omega}^{t}\right) \xrightarrow{a . s} \mu_{h}\left(\boldsymbol{\omega}^{*}\right)$ as $t \rightarrow \infty$, Kronecker's lemma applied to the above infinite sum leads to the desired result.
