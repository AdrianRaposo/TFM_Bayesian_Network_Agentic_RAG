# Article 

## Conditional Deep Gaussian Processes: Empirical Bayes Hyperdata Learning

Chi-Ken Lu ${ }^{1, *}$ and Patrick Shafto ${ }^{1,2}$

## check for updates

Citation: Lu, C.-K.; Shafto, P. Conditional Deep Gaussian Processes: Empirical Bayes Hyperdata Learning. Entropy 2021, 23, 1387. https:// doi.org/10.3390/e23111387

Academic Editors: Eric Nalisnick and Dustin Tran

Received: 1 October 2021
Accepted: 20 October 2021
Published: 23 October 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Mathematics and Computer Science, Rutgers University, Newark, NJ 07102, USA; patrick.shafto@rutgers.edu
2 School of Mathematics, Institute for Advanced Studies, Princeton, NJ 08540, USA

* Correspondence: cl1178@rutgers.edu

Abstract: It is desirable to combine the expressive power of deep learning with Gaussian Process (GP) in one expressive Bayesian learning model. Deep kernel learning showed success as a deep network used for feature extraction. Then, a GP was used as the function model. Recently, it was suggested that, albeit training with marginal likelihood, the deterministic nature of a feature extractor might lead to overfitting, and replacement with a Bayesian network seemed to cure it. Here, we propose the conditional deep Gaussian process (DGP) in which the intermediate GPs in hierarchical composition are supported by the hyperdata and the exposed GP remains zero mean. Motivated by the inducing points in sparse GP, the hyperdata also play the role of function supports, but are hyperparameters rather than random variables. It follows our previous moment matching approach to approximate the marginal prior for conditional DGP with a GP carrying an effective kernel. Thus, as in empirical Bayes, the hyperdata are learned by optimizing the approximate marginal likelihood which implicitly depends on the hyperdata via the kernel. We show the equivalence with the deep kernel learning in the limit of dense hyperdata in latent space. However, the conditional DGP and the corresponding approximate inference enjoy the benefit of being more Bayesian than deep kernel learning. Preliminary extrapolation results demonstrate expressive power from the depth of hierarchy by exploiting the exact covariance and hyperdata learning, in comparison with GP kernel composition, DGP variational inference and deep kernel learning. We also address the non-Gaussian aspect of our model as well as way of upgrading to a full Bayes inference.

Keywords: deep Gaussian process; approximate inference; deep kernel learning; Bayesian learning; moment matching; inducing points; neural network

## 1. Introduction

The deep Gaussian process [1] is a Bayesian learning model which combines both the expressive power of deep neural networks [2] and calibrated uncertainty estimation. The hierarchical composition of Gaussian Processes (GPs) [3] is the origin of expressiveness, but also renders inference intractable, as the marginalization of GPs in the stage of computing evidence is not analytically possible. Expectation propagation [4,5] and variational inference [6-9] are approximate inference schemes for DGP. The latter has issues of posterior collapse, which turns DGP into a GP with transformed input. References [8,9] address this issue and compositional freedom [10] in such hierarchical learning. Nevertheless, inferential challenges continue to slow the adoption of DGP.

Despite challenges, there has been progresses in understanding this seemingly simple yet profound model. In the case where the GPs in the hierarchy are zero-mean, DGP exhibits pathology, becoming a constant function as the depth increases [11]. Using the fact that the exponential covariance function is strictly convex, references [12,13] studied the conditional statistics for squared distance in function space, suggesting region in hyperparameter space to avoid the pathology. Recently, reference [14] showed the connection between DGP and a deep neural network with bottlenecked layers, and reference [15] suggested that a DGP with a large width may collapse back to a GP.

Others have found ways to work around the challenges of DGPs. The deep kernel learning proposed in [16] gained the Bayesian character of GP and the expressive power of a deep neural network without encountering intractability, as the learning of weight parameters, treated as kernel hyperparameters, is an empirical Bayes. Similar ideas also appeared in [17,18]. Hyperparameter learning in [16] was performed through marginal likelihood, which can in principle prevent overfitting due to the built-in competition between data fitting and model complexity [3]. However, [19] suggested that the lack of Bayesian character in the deep feature extracting net might still result in overfitting if the network has too many parameters.

Here, we propose a conditional DGP model in which the intermediate GPs (all but the exposed GP) in the hierarchical composition are conditioned on a set of hyperdata. These hyperdata are inspired by the inducing points in sparse GP [20,21,22], but they are hyperparameters, not random variables. The conditional DGP is motivated by the expressive power and Bayesian character of DGP [1], and the deep kernel learning with an objective in marginal likelihood [16]. Due to the conditioning on the hyperdata, the intermediate GPs can be viewed as collections of random feature functions centered around the deterministic conditional mean. Thus, the intermediate GPs become approximately deterministic functions when the hyperdata are sufficiently dense. Besides, lifting the intermediate GPs from being zero mean might help avoid pathology too. Mathematically, we defined a marginal prior for the conditional DGP; i.e., all intermediate GPs are marginalized, which assures the Bayesian character when dealing with the feature functions. We then use the moment matching method to approximate the non-Gaussian marginal prior as a GP [23], which connects with observed data and allows the marginal likelihood objective. It should be stressed that the effective kernel depends on the conditional mean and conditional covariance in feature function via the hyperdata, which are optimized in the spirit of empirical Bayes [24]. In the implementation, the hyperdata supporting each intermediate GP are represented as a neural network function, $u=\mathrm{nn}_{\mathbf{w}}(z)$ with $u$ and $z$ being the output and input of hyperdata, similarly to the trick used in modeling the mean and variance for data in the variational autoencoder [25].

The paper is organized as follows. Section 2 gives a short survey of the current literature on deep probabilistic models; the usage of moment matching in approximate inference; and the inducing points in GP and DGP. Background on mathematical models of GP and DGP, the marginal prior for DGP and the moment matching method are introduced in Section 3. The conditional DGP with SE kernel in the exposed layer, its mathematical connection with deep kernel learning, the parameter learning and the non-Gaussian aspect, are described in Section 4. A preliminary demonstration on extrapolating two time-series data is in Section 5, followed by a discussion in Section 6.

# 2. Related Work 

In the literature on deep probabilistic models, [26] proposed the conditional neural process in which the mean and variance functions are learned from the encoded representation of context data in a regression setup for target data. Deep Gaussian processes (DGPs) constitute one family of models for composition functions by conditioning input to a GP on the output of another GP [1]. A similar idea appeared in the works of warped GP [27,28]. The implicit process in [29] is a stochastic process embedding the Gaussian distribution into a neural network. Solutions of stochastic differential equation driven by GP are also examples of composite processes [30]. Variational DGP casts the inference problem in terms of optimizing ELBO [6] or EP [5]. However, the multi-modalness of DGP posterior [10,23] may arise from the fact that the hidden mappings in intermediate layers are dependent [9]. Inference schemes capable of capturing the multi-modal nature of DGP posterior were recently proposed by [8,9]. Depth of neural network models and the function expressivity were studied in [31,32], and uncertainty estimates were investigated in [33]. DGP in weight space representation and its variational Bayesian approach to DGP inference were introduced in [34], which were based on the notion of random feature

expansion of Gaussian [35] and arcsine [36] kernels. Deep hierarchical SVMs and PCAs were introduced in [37].

Moment matching is a way to approximate a complex distribution with, for instance, a Gaussian by capturing the mean and the second moment. Reference [38] considered a GP regression with uncertain input, and replaced the non-Gaussian predictive distribution with a Gaussian carrying the matched mean and variance. Expectation propagation, in [4], computed the vector of mean and variance parameters of non-Gaussian posterior distributions. Reference [21] approximated the distribution over unseen pixels as a multivariate Gaussian with matched mean and covariance. Moment matching is also extensively applicable to comparing two distributions [39] where the embedded means in RKHS are computed. In generative models, the model parameters are learned from comparing the model and data distributions [40].

Inducing points are an important technique in sparse GP [20,22,41,42] and DGP. In addition to being locally defined as a function's input and output, [43] introduced a transformation to form a global set of inducing features. One popular transformation uses the basis of Gaussian so that one can recover the local inducing points easily [43]. Transformation using the basis of spherical harmonic functions in [44] allows orthogonal inducing features and connects with the arcsine kernels of Bayesian deep neural network [45]. Reference [46] employed the inter-domain features in DGP inference. Recently, [47] proposed a method to express the local inducing points in the weight space representation. All the methods cited here treated the inducing points or features in a full Bayes approach, as they are random variables associated with an approximate distribution [24].

# 3. Background 

Here, we briefly introduce the notions of the Gaussian process as a model for random continuous function $f(\mathbf{x}): \mathbb{R}^{d} \mapsto \mathbb{R}$. A deep Gaussian process [1] is a hierarchical composition of Gaussian processes for modeling general composite function $\mathbf{f}_{L} \circ \mathbf{f}_{L-1} \circ \cdots \mathbf{f}_{2} \circ \mathbf{f}_{1}(\mathbf{x})$ where the bold faced function $\mathbf{f}_{1}: \mathbb{R}^{d} \mapsto \mathbb{R}^{H_{1}}$ has an output consisting of $H_{1}$ independent GPs, and similarly for $\mathbf{f}_{2}: \mathbb{R}^{H_{1}} \mapsto \mathbb{R}^{H_{2}}$ and so on. The depth and width of DGP are thus denoted by $L$ and $H_{1: L}$, respectively.

### 3.1. Gaussian Process

In machine learning, the attention is often restricted to the finite set of correlated random variables $\mathbf{f}:=\left\{f\left(\mathbf{x}_{1}\right), \cdots, f\left(\mathbf{x}_{N}\right)\right\}$ corresponding to the design location $\mathbf{X}=\left(\mathbf{x}_{1}, \cdots, \mathbf{x}_{N}\right)^{T}$. Denoting $f_{i}:=f\left(\mathbf{x}_{i}\right)$, the above set of random variables is a GP if and only if the following relations,

$$
\mathbb{E}\left[f_{i}\right]=\mu\left(\mathbf{x}_{i}\right), \mathbb{E}\left[\left(f_{i}-\mu_{i}\right)\left(f_{j}-\mu_{j}\right)\right]=k\left(\mathbf{x}_{i}, \mathbf{x}_{j}\right)
$$

are satisfied for all indices $i, j$. For convenience, we can use $f \sim \mathcal{G P}(\mu, k)$ to denote the above. The mean function $\mu(\cdot): \mathbb{R}^{d} \mapsto \mathbb{R}$ and the covariance function $k(\cdot, \cdot): \mathbb{R}^{d} \times \mathbb{R}^{d} \mapsto \mathbb{R}$ then fully specify the GP. One can proceed to write down the multivariate normal distribution as the pdf

$$
p(\mathbf{f})=\frac{1}{\sqrt{(2 \pi)^{N}|K|}} \exp \left[-\frac{1}{2}(\mathbf{f}-\mathbf{m})^{t} K^{-1}(\mathbf{f}-\mathbf{m})\right]
$$

The covariance matrix $K$ has matrix element $K_{i j}=k\left(\mathbf{x}_{i}, \mathbf{x}_{j}\right)$, characterizing the correlation between the function values. The covariance function $k$ encodes function properties such as smoothness. The vector $\mathbf{m}:=\mu(\mathbf{X})$ represents the mean values at corresponding inputs. Popular covariance functions include the squared exponential (SE) $k\left(\mathbf{x}_{i}, \mathbf{x}_{j}\right)=\sigma^{2} \exp \left[-| | \mathbf{x}_{i}-\mathbf{x}_{j} \mid\left\lvert\,{ }^{2} /\left(2 \ell^{2}\right)\right.\right]$ and the family of Matern functions. The signal magnitude $\sigma$ and length scale $\ell$ are hyper-parameters.

The conditional property of Gaussians allows one to place constraint on the model $p(\mathbf{f})$. Given a set of function values $\mathbf{u}=f(\mathbf{Z})$, the space of random function $f$ now only

includes those passing through these fixed points. Then the conditional pdf $p(\mathbf{f} \mid \mathbf{u})$ has the conditional mean and covariance:

$$
\begin{aligned}
\mathbf{m} & \rightarrow \mathbf{m}+K_{\mathbf{x z}} K_{\mathbf{z Z}}^{-1}[\mathbf{u}-\mathbf{m}] \\
\mathbf{K}_{\mathbf{X}} & \rightarrow \mathbf{K}_{\mathbf{X}}-\mathbf{K}_{\mathbf{X Z}} \mathbf{K}_{\mathbf{Z}}^{-1} \mathbf{K}_{\mathbf{Z X}}
\end{aligned}
$$

where the matrix $\mathbf{K}_{\mathbf{X Z}}$ represents the covariance matrix evaluated at $\mathbf{X}$ against $\mathbf{Z}$.

# 3.2. Deep Gaussian Process 

We follow the seminal work in [1] to generalize the notion of GP to the composite functions $\mathbf{f}_{L} \circ \mathbf{f}_{L-1} \circ \cdots \mathbf{f}_{2} \circ \mathbf{f}_{1}(\mathbf{x})$. In most literature, DGP is defined from a generative point of view. Namely, the joint distribution for the simplest zero-mean DGP with $L=2$ and $H_{2}=H_{1}=1$ can be expressed as

$$
p\left(f_{2}, f_{1} \mid \mathbf{X}\right)=p\left(f_{2} \mid f_{1}\right) p\left(f_{1} \mid \mathbf{X}\right)
$$

with the conditional defined as $f_{2} \mid f_{1} \sim \mathcal{G} \mathcal{P}\left(0, k\left(f_{1}, f_{1}\right)\right)$ and $f_{1} \sim \mathcal{G} \mathcal{P}(0, k(\mathbf{X}, \mathbf{X})$.

### 3.3. Marginal Prior, Covariance and Marginal Likelihood

In the above DGP model, the exposed GP for $f_{2}$ is connected with the data output $\mathbf{y}$, and the intermediate GP for $f_{1}$ with the data input $\mathbf{X}$. In Bayesian learning, both $f$ s shall be marginalized when computing the evidence. Now we define the marginal prior as

$$
p(\mathbf{f})=\int d \mathbf{f}_{1} p\left(\mathbf{f}_{2} \mid \mathbf{f}_{1}\right) p\left(\mathbf{f}_{1} \mid \mathbf{X}\right)
$$

in which the bold faced $\mathbf{f}_{1}$ representing the set of intermediate function values are marginalized, but the exposed $\mathbf{f}_{2}$ is not. Note that the notation $f(\mathbf{x})=f_{2}\left(f_{1}(\mathbf{x})\right)$ is not ambiguous in a generative view, but may cause some confusion in the marginal view as the label $f_{1}$ has been integrated out. To avoid confusing with the exposed function $f_{2}(\cdot)$, we still use $f(\cdot)$ to denote the marginalized composite function unless otherwise stated.

Motivated to write down an objective in terms of marginal likelihood, the moment matching method in [23] was proposed, so one can approximate Equation (6) with a multivariate Gaussian $q(\mathbf{f} \mid \mathbf{X})$ such that the mean and the covariance are matched. In the zero-mean DGP considered in [23], the covariance matching refers to

$$
\mathbb{E}_{\mathbf{f} \sim q}\left[f_{i} f_{j}\right]=\mathbb{E}_{\mathbf{f}_{1}}\left[\mathbb{E}_{\mathbf{f}_{2} \mid \mathbf{f}_{1}}\left[f_{i} f_{j}\right]\right]=\int d \mathbf{f}_{2} d \mathbf{f}_{1} f_{2}\left(f_{1}\left(\mathbf{x}_{i}\right)\right) f_{2}\left(f_{1}\left(\mathbf{x}_{j}\right)\right) p\left(\mathbf{f}_{2} \mid \mathbf{f}_{1}\right) p\left(\mathbf{f}_{1} \mid \mathbf{X}\right)
$$

In the case where the squared exponential kernel is used in both GPs, the approximate marginal prior $q(\mathbf{f} \mid \mathbf{X})=\mathcal{N}\left(0, K_{\text {eff }}\right)$, with the effective kernel being $k_{\text {eff }}=\sigma_{2}^{2}\left[1+2 \frac{\sigma_{1}^{2}}{\ell_{2}^{2}}(1-\right.$ $\left.\exp \left(- \mid \mathbf{x}_{i}-\mathbf{x}_{j}{ }^{2} / 2 \ell_{1}^{2}\right)\right)\right]^{-\frac{1}{2}}$ [23]. The hyperparameters include the length scale $\ell$ and signal magnitude $\sigma$ with layer indexed at the subscript.

Consequently, the evidence of the data $\mathbf{X}, \mathbf{y}$ associated with the 2-layer DGP can be approximately expressed as

$$
p(\mathbf{y} \mid \mathbf{X}) \approx \int d \mathbf{f} p(\mathbf{y} \mid \mathbf{f}) q(\mathbf{f} \mid \mathbf{X})
$$

Thus, the learning of hyperparameters $\sigma \mathrm{s}$ and $\ell \mathrm{s}$ in the zero-mean DGP model is through the gradient descent on $\log p(\mathbf{y} \mid \mathbf{X})$, and the gradient components $\frac{\partial K}{\partial \ell_{1,2}}$ and $\frac{\partial K}{\partial \sigma_{1,2}}$ are needed in the framework of GPy [48].

## 4. Model

Following the previous discussion, we shall introduce the model of conditional DGP along with the covariance and marginal prior. The mathematical connection with deep

kernel learning and the non-Gaussian aspect of marginal prior will be discussed. The difference between the original DGP and the conditional DGP is that the intermediate GPs in the latter are conditioned on the hyperdata. Learning the hyperdata via the approximate marginal likelihood is, loosely speaking, an empirical Bayesian learning of the feature function in the setting of deep kernel learning.

# 4.1. Conditional Deep Gaussian Process 

In the simple two-layer hierarchy with width $H_{1}=H_{2}=1$, the hyperdata $\{\mathbf{Z}, \mathbf{u}\}=$ $\left\{\mathbf{z}_{1: M} \in \mathbb{R}^{d}, u_{1: M} \in \mathbb{R}\right\}$ are introduced as support for the intermediate GP for $f_{1}$, and the exposed GP for $f_{2}$ remains zero-mean and does not condition on any point. Thus, $f_{1}$ can be viewed as a space of random functions constrained with $f_{1}\left(\mathbf{z}_{1: M}\right)=u_{1: M}$, and the Gaussian distribution $p\left(f_{1}\left(\mathbf{x}_{1: N}\right) \mid \mathbf{Z}, \mathbf{u}\right)$ has its conditional mean and covariance in Equation (3) (with $\mathbf{m}$ on RHS set to zero) and (4), respectively. Following Equation (6), the marginal prior for this conditional DGP can be similarly expressed as

$$
p(\mathbf{f})=\int d \mathbf{f}_{1} p\left(\mathbf{f}_{2} \mid \mathbf{f}_{1}\right) p\left(\mathbf{f}_{1} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u}\right)
$$

With $f_{1}$ being conditioned on the hyperdata $\{\mathbf{Z}, \mathbf{u}\}$, one can see that the multivariate Gaussian $p\left(f_{1}\left(\mathbf{x}_{1: N}\right) \mid \mathbf{Z}, \mathbf{u}\right)$ emits samples in the space of random functions passing through the fixed hyperdata so that Equation (9) is a sum of an infinite number of GPs. Namely,

$$
f \sim \sum_{f_{1}} \mathcal{G} \mathcal{P}\left(0, k_{2}\left(f_{1}(\mathbf{X}), f_{1}(\mathbf{X})\right)\right)
$$

with $f_{1}$ under the constraints due to the hyperdata and the smoothness implied in kernel $k_{1}$. Therefore, $f$ are represented by an ensemble of GPs with same kernel but different feature functions. We shall come back to this point more rigorously in Section 4.2.

Now we shall approximate the intractable distribution in Equation (9) with a multivariate Gaussian $q(\mathbf{f} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u})$ carrying the matched covariance. The following lemma is useful for the case where the exposed GP for $f_{2} \mid f_{1}$ uses the squared exponential (SE) kernel.

Lemma 1. (Lemma 3 in [49]) The covariance in $p(\mathbf{f})$ (Equation (9)) with the SE kernel $k_{2}(x, y)=\sigma_{2}^{2} \exp \left[-(x-y)^{2} / 2 \ell_{2}^{2}\right]$ in the exposed GP for $f_{2} \mid f_{1}$ can be calculated analytically. With the Gaussian conditional distribution, $p\left(\mathbf{f}_{1} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u}\right)$, supported by the hyperdata, the effective kernel reads

$$
k_{\mathrm{eff}}\left(\mathbf{x}_{i}, \mathbf{x}_{j}\right)=\frac{\sigma_{2}^{2}}{\sqrt{1+\delta_{i j}^{2} / \ell_{2}^{2}}} \exp \left[-\frac{\left(m_{i}-m_{j}\right)^{2}}{2\left(\ell_{2}^{2}+\delta_{i j}^{2}\right)}\right]
$$

where $m_{i, j}:=m\left(\mathbf{x}_{i, j}\right)$ and $c_{i j}:=\operatorname{cov}\left(f_{1}\left(\mathbf{x}_{i}\right), f_{1}\left(\mathbf{x}_{j}\right)\right)$ are the conditional mean and covariance, respectively, at the inputs $\mathbf{x}_{i, j}$. The positive parameter $\delta_{i j}^{2}:=c_{i i}+c_{j j}-2 c_{i j}$ and the the length scale $\ell_{2}$ dictates how the uncertainty about $f_{1}$ affects the function composition.

Next, in addition to the hyperparameters such as $\sigma \mathrm{s}$ and $\ell \mathrm{s}$, the function values $u_{1: M}$ are hyperdata that shall be learned from the objective. With approximating the non-Gaussian marginal prior $p(\mathbf{f} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u})$ with $q(\mathbf{f} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u})$, we are able to compute the approximate marginal likelihood as the objective

$$
\mathcal{L}=-\log \int d \mathbf{f} p(\mathbf{y} \mid \mathbf{f}) q(\mathbf{f} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u})
$$

The learning of all hyperparameter data follows the standard gradient descent used in GPy [48], and the gradient components include the usual ones, such as $\partial K_{\text {eff }} / \partial \ell_{2}$ in exposed layer and those related to the intermediate layer $\partial K_{\text {eff }} / \partial \ell_{1}$ and the hyperdata $\partial K_{\text {eff }} / \partial u_{1: M}$ through chaining with $\partial K_{\text {eff }} / \partial\left(m_{i}-m_{j}\right)$ and $\partial K_{\text {eff }} / \partial \delta_{i j}^{2}$ via Equations (3) and (4). To exploit

the expressive power of neural network during optimization, the hyperdata can be further modeled by a neural network; i.e.,

$$
u_{1: M}=\operatorname{nn}_{\mathbf{w}}\left(\mathbf{z}_{1: M}\right)
$$

with $\mathbf{w}$ denoting the weight parameters. In such case, the weights $\mathbf{w}$ are learned instead of the hyperdata $u_{1: M}$.

# 4.2. When Conditional DGP Is Almost a GP 

In the limiting case where the probabilistic nature of $f_{1}$ is negligible, then the conditional DGP becomes a GP with the transformed input; i.e., the distribution $p\left(\mathbf{f}_{1} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u}\right)$ becomes highly concentrated around a certain conditional mean $\overline{f_{1}}(\mathbf{x})$. To get insight, we reexamine the covariance in the setting where $f_{1}$ is almost deterministic. We can reparameterize the random function $f_{1}$ at two distinct inputs $\mathbf{x}_{1,2}$ for the purpose of computing covariance:

$$
f_{1}\left(\mathbf{x}_{i, j}\right)=m\left(\mathbf{x}_{i, j}\right)+\epsilon_{i, j}
$$

where $m(\mathbf{x})$ is the conditional mean given the fixed $\mathbf{Z}$ and $\mathbf{u}$. The random character lies in the two correlated random variables, $\left(\epsilon_{i}, \epsilon_{j}\right)^{T} \sim \mathcal{N}(0, C)$, corresponding to the weak but correlated signal around zero. Under that assumption, we follow the analysis in [9,38] and prove the following lemma.

Lemma 2. Consider $p(f)$ defined in Equation (9), with $f_{2} \mid f_{1}$ being a more general $\mathcal{G} \mathcal{P}\left(\mu_{2}, k_{2}\right)$ and $f_{1}$ reparametrized as in Equation (13). The covariance, $\operatorname{cov}\left(f_{2}\left(f_{1}\left(\mathbf{x}_{i}\right)\right), f_{2}\left(f_{1}\left(\mathbf{x}_{j}\right)\right)\right)$, has the following form:

$$
\left[1+\frac{c_{i j}}{2} \partial_{m_{j}}^{2}+\frac{c_{i j}}{2} \partial_{m_{i}}^{2}+c_{i j} \partial_{m_{i} m_{j}}^{2}\right] k_{2}\left(m_{i}, m_{j}\right)+c_{i j} \mu_{2}^{\prime}\left(m_{i}\right) \mu_{2}^{\prime}\left(m_{j}\right)
$$

where the cs are matrix elements of kernel matrix $C$ associated with the weak random variables $\epsilon_{i, j}$ in Equation (13). The notation $m_{i, j}:=m\left(\mathbf{x}_{i, j}\right)$ and prime as derivative is used.

Proof. The assumption is that $f_{2} \mid f_{1} \sim \mathcal{G} \mathcal{P}\left(\mu_{2}, k_{2}\right)$ and that $f_{1}(x)$ a weak random function $\epsilon(x)$ overlaying a fixed function $m(x)$. At any two inputs $x_{i, j}$, we expand the target function $f$ to the second order:

$$
f\left(x_{i, j}\right)=f_{2}\left(f_{1}\left(x_{i, j}\right)\right) \approx f_{2}\left(m_{i, j}\right)+\epsilon_{i, j} f_{2}^{\prime}\left(m_{i, j}\right)+\frac{\epsilon_{i, j}^{2}}{2} f_{2}^{\prime \prime}\left(m_{i, j}\right)
$$

where the shorthanded notation $m_{i}:=m\left(x_{i}\right)$ and $\epsilon\left(x_{i}\right):=\epsilon_{i}$ is used. Note that $\left(\epsilon_{i}, \epsilon_{j}\right)$ is bivariate Gaussian with zero mean and covariance matrix $\mathbf{C}$. We use the law of total covariance, $\operatorname{cov}[a, b]=\operatorname{cov}(\mathbb{E}[a \mid d], \mathbb{E}[b \mid d])+\mathbb{E}[\operatorname{cov}(a, b \mid d)]$ with $a, b$ and $d$ being some random variables. To proceed with the first term, we calculate the conditional mean given the $\epsilon \mathrm{s}$ :

$$
\mathbb{E}\left[f\left(x_{i, j}\right) \mid \epsilon_{i}, \epsilon_{j}\right]=\mu_{2}\left(m_{i, j}\right)+\epsilon_{i, j} \mu^{\prime}\left(m_{i, j}\right)
$$

Then one uses the fact that $f_{2} \mid f_{1}, f_{2}^{\prime} \mid f_{1}$ and $f_{2}^{\prime \prime} \mid f_{1}$ are jointly Gaussian to compute the conditional covariance, which can be expressed in a compact form:

$$
\operatorname{cov}\left[f\left(x_{i}\right) f\left(x_{j}\right) \mid \epsilon_{i}, \epsilon_{j}\right]=\hat{O}\left(\epsilon_{i}, \epsilon_{j}\right) k\left(m_{i}, m_{j}\right)
$$

The operator $\hat{O}$ accounts for the fact that $\operatorname{cov}\left[f_{2}^{\prime}\left(m_{i}\right), f_{2}^{\prime}\left(m_{j}\right)\right]=\partial_{m_{i} m_{j}}^{2} k_{2}\left(m_{i}, m_{j}\right)$ and $\operatorname{cov}\left[f_{2}\left(m_{i}\right), f_{2}^{\prime \prime}\left(m_{j}\right)\right]=\partial_{m_{j}}^{2} k_{2}\left(m_{i}, m_{j}\right)$. Thus, the operator reads

$$
\hat{O}=1+\epsilon_{i} \partial_{m_{i}}+\epsilon_{j} \partial_{m_{j}}+\frac{\epsilon_{i}^{2}}{2} \partial_{m_{i}}^{2}+\frac{\epsilon_{i}^{2}}{2} \partial_{m_{j}}^{2}+\epsilon_{i} \epsilon_{j} \partial_{m_{i} m_{j}}^{2}
$$

Now we are ready to deal with the outer expectation with respect to the $\epsilon \mathrm{s}$. Note that the covariance $c_{i j}:=\mathbb{E}\left[\epsilon_{i} \epsilon_{j}\right]=c\left(x_{i}, x_{j}\right)$ and variance $c_{i i}:=\mathbb{E}\left[\epsilon_{i}^{2}\right]=c\left(x_{i}, x_{i}\right)$ are matrix elements of $\mathbf{C}$. Consequently, we prove the total covariance in Equation (14).

Remark 1. Since the second derivatives $\partial_{m_{i}}^{2} k_{2}\left(m_{i}, m_{j}\right)=\partial_{m_{j}}^{2} k_{2}\left(m_{i}, m_{j}\right)=-\partial_{m_{i} m_{j}}^{2} k_{2}\left(m_{i}, m_{j}\right)$ hold for the stationary $k_{2}$, the above covariance (Equation (14)) with $\mu_{2}=0$ is identical to the effective kernel in Equation (10) in the limit $\ell_{2}^{2} \gg \delta_{i j}^{2}$, which reads

$$
\operatorname{cov}\left(f\left(x_{i}\right) f\left(x_{j}\right)\right) \propto\left[1+\frac{\left(m_{i}-m_{j}\right)^{2}-\ell_{2}^{2}}{2 \ell_{2}^{4}} \delta_{i j}^{2}\right] \exp \left[-\frac{\left(m_{i}-m_{j}\right)^{2}}{2 \ell_{2}^{2}}\right]
$$

Such a situation occurs when the inputs $\mathbf{Z}$ in hyperdata are dense enough so that $f_{1}$ becomes almost deterministic.

Consequently, in the limit when the conditional covariance in $\delta^{2}$ is small compared with the length scale $\ell_{2}^{2}$, Equation (19) indicates that the effective kernel is the SE kernel with a deterministic input $m(\mathbf{x})$, which is equivalent to the deep kernel with SE as the base kernel (see Equation (5) in [16]). On the other hand, when $\delta^{2}$ and $\ell_{2}$ are comparable, the terms within the first bracket in the RHS of Equation (19) are a non-stationary function which may attribute multiple frequencies in the function $f$. The deep kernel with the spectral mixture kernel (Equation (6) in [16]) as the base is similar to the effective kernel.

# 4.3. Non-Gaussian Aspect 

The statistics of the non-Gaussian marginal prior $p(\mathbf{f} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u})$ are not solely determined by the moments up to the second order. The fourth moment can be derived in a similar manner in [23] with the help of the theorem in [50]. Relevant discussion of the heavy-tailed character in Bayesian deep neural network can be found in [51-53]. See Lemma A1 for the details of computing the general fourth moment in the case where SE kernel is used in $f_{2} \mid f_{1}$ in the conditional 2-layer DGP. Here, we briefly discuss the non-Gaussian aspect, focusing on the variance of covariance, i.e., by comparing $\mathbb{E}_{p}\left[\left(f\left(\mathbf{x}_{i}\right) f\left(\mathbf{x}_{j}\right)\right)^{2}\right]$ and $\mathbb{E}_{q}\left[\left(f\left(\mathbf{x}_{i}\right) f\left(\mathbf{x}_{j}\right)\right)^{2}\right]$, with $p$ being the true distribution (Equation (9)) and $q$ being the approximating Gaussian.

In the SE case, one can verify the difference in the fourth order expectation value:

$$
\mathbb{E}_{p}\left[\left(f\left(\mathbf{x}_{i}\right) f\left(\mathbf{x}_{j}\right)\right)^{2}\right]-\mathbb{E}_{q}\left[\left(f\left(\mathbf{x}_{i}\right) f\left(\mathbf{x}_{j}\right)\right)^{2}\right]=\frac{e^{-\frac{\left(m_{i}-m_{j}\right)^{2}}{1+2 \delta_{i j}^{2}}}}{\left[1+2 \delta_{i j}^{2}\right]^{1 / 2}}-\frac{e^{-\frac{\left(m_{i}-m_{j}\right)^{2}}{1+\delta_{i j}^{2}}}}{\left[1+\delta_{i j}^{2}\right]} \geq 0
$$

where we have used the fact that the inequalities $\left(1+2 \delta^{2}\right)^{-1 / 2} \geq\left(1+\delta^{2}\right)^{-1}$ and $\exp \left[-\left(1+2 \delta^{2}\right)^{-1}\right] \geq \exp \left[-\left(1+\delta^{2}\right)^{-1}\right]$ hold. Therefore, the inequality suggests the heavytailed statistics of the marginal prior $p\left(f\left(\mathbf{x}_{i}\right), f\left(\mathbf{x}_{j}\right)\right)$ over any pair of function values.

## 5. Results

The works in [54,55] demonstrate that GPs can still have superior expressive power and generalization if the kernels are dedicatedly designed. With the belief that deeper models generalize better than the shallower counterparts [56], DGP models are expected to perform better in fitting and generalization than GP models do if the same kernel is used in both. However, such expectation may not be fully realized, as the approximate inference may lose some power in DGP. For instance, diminishing variance in the posterior over the latent function was reported in [9] regarding the variational inference for DGP [6]. Here, with a demonstration of extrapolating real-world time series data with the conditional DGP, we shall show that the depth, along with optimizing the hyperdata, does enhance the expressive power and the generalization due to the multiple length scale and multiplefrequency character of the effective kernel. In addition, the moment matching method as

an approximate inference for conditional DGP does not suffer from the posterior collapse. The simulation codes can be found in the github repository.

### 5.1. Mauna Loa Data

Figure 1a,b shows fitting and extrapolating the classic carbon dioxide data (yellow marks for training, red for test) with GPs using, respectively, the SE kernel and a mixture of SE, periodic SE and rational quadratic kernels [3].

$$
k_{\operatorname{mix}}\left(t, t^{\prime}\right)=\theta_{1}^{2} \exp \left[-\frac{\left(t-t^{\prime}\right)^{2}}{\theta_{2}^{2}}\right]+\theta_{3}^{2} \exp \left[-\frac{\sin ^{2}\left(t-t^{\prime}\right)}{\theta_{4}^{2}}\right]+\theta_{5}^{2}\left[1+\frac{\left(t-t^{\prime}\right)^{2}}{\theta_{6}^{2}}\right]^{-\theta_{7}}
$$

All the $\theta$ s are hyperparameters in the mixture kernel. As a result of the multiple time scales appearing in the data, the vanilla GP fails to capture the short time trend, but the GP with mixture of kernels can still present excellent expressivity and generalization. The log marginal likelihoods (logML) were 144 and 459 for the vanilla GP and kernel mixture GP, respectively. The two-layer zero-mean DGP with SE kernel in both layers performed better than the single-layer counterpart. In Figure 1c, the GP with the SE[SE] effective kernel has excellent fitting with the training data but has extrapolated poorly. The good fitting may have resulted from the fact that the SE[SE] kernel does capture the character of multiple length scales in DGP. The logML for the SE[SE] GP is 338.
![img-0.jpeg](img-0.jpeg)

Figure 1. Extrapolation of standardized $\mathrm{CO}_{2}$ time series data (yellow dots for training and red dots for test) using GP with three kernels. The dark solid line represents the predictive mean, and the shaded area is the the model's confidence. Panel (a) displays the result using a single GP with an SE kernel. Panel (b) was obtained following the kernel composition in [3]. Panel (c) came from using the effective kernel of 2-layer zero-mean DGP with SE used in both layers [23]. (a) SE kernel; (b) SE+periodic SE+RQ kernel; (c) SE[SE] kernel.

Next, we shall see whether improved extrapolation can arise in other deep models or other inference schemes. In Figure 2, the results from DKL and from DGP using the variational inference are shown. Both were implemented in GPFlux [57]. We modified the tutorial code for hybrid GP with three-layer neural network as the code for DKL. The result in Figure 2a does not show good fitting nor good extrapolation, which is to some extent consistent with the simulation of a Bayesian neural network with ReLu activation [32]. As for the DGP using variational inference, the deeper models do not show much improvement compared to the vanilla GP, and the obtained ELBO was 135 for the two-layer DGP (Figure 2b), and it was 127 for three-layer (Figure 2c).
![img-1.jpeg](img-1.jpeg)

Figure 2. Extrapolation of standardized $\mathrm{CO}_{2}$ using DKL and variational inference [6] for the DGP implemented in GPFlux [57]. Panel (a) was obtained using the DKL with three-layer RELU network. Panel (b) shows the results from the two-layer zero-mean DGP model. Panel (c) shows the results of the three-layer zero-mean DGP. (a) DKL; (b) Two-layer DGP; (c) Three-layer DGP.

Now we continue to show the performance of our model. In the two-layer model, we have 50 points in hyperdata supporting the intermediate GP. A width-5 tanh neural network is used to represent the hyperdata, i.e., $u_{1: 50}=\mathrm{nn}_{\mathbf{w}}\left(z_{1: 50}\right)$. Then, the hyperparameters, including $\sigma_{1,2}, \ell_{1,2}$ and weight parameter $\mathbf{w}$, were learned from gradient descent upon the approximate marginal likelihood. The top panel in Figure 3a displays the prediction and confidence from the posterior over $f_{1}$, obtained from a GP conditioned on the learned hyperparameters and hyperdata. The logML of the two-layer model was also 338, the same as the SE[SE] GP, and in the bottom panel of Figure 3a one can observe a good fit with the training data. More importantly, the extrapolation shows some high frequency signal in the confidence (shaded region). In comparing ot with Figure 3 of [54], the high-frequency signal only appeared after a periodic kernel was inserted. We attribute the high-frequency signal to the propagation of uncertainty in $f_{1}$ (top panel) to the exposed layer (see discussion in Section 4.2).

Lastly, the three-layer model using 37 and 23 hyperdata in the $f_{1}$ and $f_{2}$ layer, respectively, has its results in Figure 3b. Those hyperdata were parameterized by the same neural network used in the two-layer model. The training had a logML of 253, resulting in a good fit with the data. The extrapolation captured the long term trend in its predictive mean, and the test data were mostly covered in the confidence region. In the latent layers, more expressive patterns overlaying the latent mappings seemed to emerge due to the uncertainty and the depth of the model. The learned $\sigma_{1,2,3} \approx(0.49,0.86,2.56)$ and $\ell_{1,2,3} \approx(0.014,1.2,0.46)$ show that different layers managed to learn different resolutions.
![img-2.jpeg](img-2.jpeg)

Figure 3. Extrapolation of the standardized $\mathrm{CO}_{2}$ using conditional DGP. Panel (a) is for the two-layer model, and (b) for the three-layer model. Top and middle panels shows the mean and confidence in the posterior over the latent functions. See text for details. (a) Two-layer conditional DGP; (b) Three-layer conditional DGP.

# 5.2. Airline Data 

The models under consideration can be applied to the airline data too. It can be seen in Figure 4 that the vanilla GP was too simple for the complex time-series data, and the GP with the same kernel composition could both fit and extrapolate well. The logML values were -11.7 and 81.9 for the vanilla GP and kernel mixture GP, respectively. Similarly, the SE[SE] kernel captured the multiple length scale character in the data, resulting in a good fit with logML 20.9, but poor extrapolation.

![img-3.jpeg](img-3.jpeg)

Figure 4. Extrapolation of the standardized airline data with three different GPs. (a) SE kernel; (b) SE+periodic SE+RQ kernel; (c) SE[SE] kernel.

Here, we display the results using the DKL, variational inference DGP, both two-layer and three-layer, in Figure 5. For the airline data, the DKL with a ReLu neural network as feature extractor panel (Figure 5a) had similar performance to its counterpart on $\mathrm{CO}_{2}$ data, as did the variational DGP(Figure 5b,c).
![img-4.jpeg](img-4.jpeg)

Figure 5. Extrapolation of the standardized airline data using DKL (a), 2-layer DGP (b) and 3-layer DGP (c). (a) DKL; (b) Two-layer DGP; (c) Three-layer DGP.

Our two-layer model, aided by the probabilistic latent layer supported by 13 hyperdata, showed improved extrapolation along with the high-frequency signal in prediction and confidence. The optimal $\log \mathrm{ML}$ was 28.5 , along with the learned $\sigma_{1,2}=(3.03,0.73), \ell_{1,2}=$ $(0.026,2.19)$ and noise level $\sigma_{n}=0.004$. As shown in Figure 6b, the latent function supported by learned hyperdata shows an increasing trend on top of an oscillating pattern, which led to the periodic extrapolation in the predictive distribution, albeit only the vanilla kernels were used. It is interesting to compare Figure 6b with Figure 6a, as the latter model had 23 hyperdata supporting the latent function, and the vanishing uncertainty learned in the latent function produced an extrapolation that collapsed to zero. The $\log \mathrm{ML}$ in Figure 6a is 7.25 with learned $\sigma_{1,2}=(2.18,0.59), \ell_{1,2}=(0.3,0.07)$, and noise level $\sigma_{n}=0.02$.
![img-5.jpeg](img-5.jpeg)

Figure 6. Extrapolation of airline data using conditional DGP. The upper panel shows the learned latent function and uncertainty from hyperdata learning, and the bottom panel shows the extrapolation from the past data. (a) The first model had 23 hyperdata supporting the latent GP. (b) The other model had 13. (a) 2-layer cDGP with 23 hyperdata; (b) 2-layer cDGP with 13 hyperdata.

# 6. Discussion 

What did we gain and lose while modifying the original DGP defined in Equation (6) by additionally conditioning the intermediate GPs on the hyperdata? On one hand, when the hyperdata are dense, the conditional DGP is mathematically connected with the deep kernel learning, i.e., a GP with warped input. On the other hand, in the situations when less dense hyperdata are present and the latent GPs are representations of random functions passing through the hyperdata, the conditional DGP can be viewed as an ensemble of deep kernels, and the moment matching method allows us to express it in a closed form. What do we lose in such an approximation? Apparently, the approximate $q$ for the true marginal prior $p$ in Equation (9) cannot account for the heavy-tailed statistics.

In the demonstration, the presence of hyperdata constrains the space of the intermediate functions and moves the mass of the function distribution toward the more probable ones in the process of optimization. Comparing the SE[SE] GP, which represents an approximate version of zero-mean 2-layer DGP, against the conditional DGP model, the constrained space of intermediate functions does not affect the learning significantly, and the generalization is improved. Besides, the uncertainty in the latent layers is not collapsed.

One possible criticism of the present model may result from the empirical Bayes learning of the weight parameters. Although the weight parameters are hyperparameters in both our model and in DKL, it is important to distinguish that the weight parameters in our model parameterize $u_{1: M}$, which supports the intermediate GP, representing an ensemble of latent functions. In DKL, however, the weight parameters fully determine the one latent function, which might lead to overfitting even though marginal likelihood is used as an objective [19]. A possible extension is to consider upgrading the hyperdata to random variables, and the associated mean and variance in $q\left(u_{1: M}\right)$ can also be modeled as neural network functions of $\mathbf{Z}$. The moment matching can then be applied to approximate the marginal prior $\int d \mathbf{f}_{1} d \mathbf{u} p\left(\mathbf{f}_{2} \mid \mathbf{f}_{1}\right) p\left(\mathbf{f}_{1} \mid \mathbf{X}, \mathbf{Z}, \mathbf{u}\right) q(\mathbf{u})$.

## 7. Conclusions

Deep Gaussian processes (DGPs), based on nested Gaussian processes (GPs), offer the possibility of expressive inference and calibrated uncertainty, but are limited by intractable marginalization. Approximate inference for DGPs via inducing points and variational inference allows scalable inference, but incurs costs by limiting expressiveness and causing an inability to propagate uncertainty. We introduce effectively deep kernels with optimizable hyperdata supporting latent GPs via a moment-matching approximation. The approach allows joint optimization of hyperdata and GP parameters via maximization of marginal likelihood. We show that the approach avoids mode collapse, connects DGPs and deep kernel learning, effectively propagating uncertainty. Future directions on conditional DGP include that consideration of randomness in the hyperdata and the corresponding inference.

Author Contributions: Conceptualization, C.-K.L. and P.S.; methodology, C.-K.L.; software, C.-K.L.; validation, C.-K.L. and P.S.; formal analysis, C.-K.L.; investigation, C.-K.L.; resources, C.-K.L.; data curation, C.-K.L.; writing-original draft preparation, C.-K.L.; writing-review and editing, C.-K.L. and P.S.; visualization, C.-K.L.; supervision, P.S.; project administration, C.-K.L.; funding acquisition, P.S. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Air Force Research Laboratory and DARPA under agreement number FA8750-17-2-0146.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to thank the members of CoDaS Lab for stimulating discussions.

Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, or in the decision to publish the results.

# Abbreviations 

The following abbreviations are used in this manuscript:
GP Gaussian Process
DGP Deep Gaussian Process
DKL Deep Kernel Learning
SE Squared Exponential

## Appendix A

Lemma A1. Consider the marginal prior for 2-layer conditional DGP [Equation (9)] with $f_{2} \mid f_{1}$ being a GP with SE kernel, and $f_{1} \mid \mathbf{Z}, \mathbf{u}$ being another GP with conditional mean $\mu$ and conditional covariance $k$. The general fourth moment is the following sum over distinct doublet decomposition,

$$
\mathbb{E}\left[f\left(\mathbf{x}_{i}\right) f\left(\mathbf{x}_{j}\right) f\left(\mathbf{x}_{m}\right) f\left(\mathbf{x}_{l}\right)\right]=o_{2}^{4} \sum \frac{\alpha_{a b, c d} \alpha_{c d, a b} \beta_{a b, c d}}{\sqrt{D_{a b} D_{c d}-V_{a b, c d}^{2}}}
$$

with $V_{a b, c d}=\left(k_{a d}+k_{b c}-k_{a c}-k_{b d}\right) / \ell_{2}^{2}$ and $D_{a b}=1+\left(k_{a a}+k_{b b}-2 k_{a b}\right) / \ell_{2}^{2}$. Furthermore, the expressions,

$$
\alpha_{a b, c d}=\exp \left[\frac{-\left(m_{a}-m_{b}\right)^{2}}{2 \ell_{2}^{2}\left(D_{a b}-V_{a b, c d}^{2} / D_{c d}\right)}\right]
$$

and

$$
\beta_{a b, c d}=\exp \left[-\frac{\left(m_{a}-m_{b}\right)\left(m_{c}-m_{d}\right) V_{a b, c d}}{\ell_{2}^{2}\left(D_{a b} D_{c d}-V_{a b, c d}^{2}\right)}\right]
$$

Proof. Denoting the function value $h_{a}:=f_{1}\left(\mathbf{x}_{a}\right)$, we can rewrite the product of the covariance function $k_{2}\left(h_{a}, h_{b}\right) k_{2}\left(h_{c}, h_{d}\right)=\exp \left(-\frac{[\mathbf{h}]_{a, c d}^{T} \mathbb{J}_{4}[\mathbf{h}]_{a b, c d}}{2}\right)$ where the row vector $[\mathbf{h}]_{a b, c d}^{T}=\left(h_{a}, h_{b}, h_{c}, h_{d}\right)$ and the matrix

$$
\mathbb{J}_{4}=\left(\begin{array}{cc}
\mathbb{J}_{2} & 0 \\
0 & \mathbb{J}_{2}
\end{array}\right)
$$

where $\mathbb{J}_{2}$ is the 2-by-2 matrix with ones in the diagonal and minus ones in the off-diagonal. The above zeros stand for 2-by-2 zero matrices in the off-diagonal blocks. The procedure of obtaining expectation value with respect to the 4 -variable multivariate Gaussian distribution $\mathcal{N}\left([\mathbf{h}]_{a b, c d} \mid \mathbb{V}_{4}, \mathbb{K}_{4}\right)$ is similar to the previous one in obtaining the second moment. Namely, applying Lemma 2 in [23],

$$
\mathbb{E}\left[k_{2}\left(h_{a}, h_{b}\right) k_{2}\left(h_{c}, h_{d}\right)\right]=\frac{\exp \left(-\frac{1}{2} \mathbb{V}_{4}^{\prime} \mathbb{A}_{4} \mathbb{V}_{4}\right)}{\sqrt{I_{4}+\mathbb{K}_{4} \mathbb{J}_{4}}}
$$

in which the calculation of inverse of 4-by-4 matrix $I_{4}+\mathbb{K}_{4} \mathbb{J}_{4}$ and its determinant is quite tedious but tractable.
