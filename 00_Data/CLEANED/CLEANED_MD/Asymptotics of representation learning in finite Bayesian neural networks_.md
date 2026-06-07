# Asymptotics of representation learning in finite Bayesian neural networks 

Jacob A. Zavatone-Veth ${ }^{1,2}$, Abdulkadir Canatar ${ }^{1,2}$, Benjamin S. Ruben ${ }^{3}$, Cengiz Pehlevan ${ }^{2,4}$<br>${ }^{1}$ Department of Physics, ${ }^{2}$ Center for Brain Science, ${ }^{3}$ Biophysics Graduate Program, ${ }^{4}$ John A. Paulson School of Engineering and Applied Sciences Harvard University Cambridge, MA 02138<br>\{jzavatoneveth, canatara, benruben\}@g.harvard.edu<br>cpehlevan@seas.harvard.edu


#### Abstract

Recent works have suggested that finite Bayesian neural networks may sometimes outperform their infinite cousins because finite networks can flexibly adapt their internal representations. However, our theoretical understanding of how the learned hidden layer representations of finite networks differ from the fixed representations of infinite networks remains incomplete. Perturbative finite-width corrections to the network prior and posterior have been studied, but the asymptotics of learned features have not been fully characterized. Here, we argue that the leading finitewidth corrections to the average feature kernels for any Bayesian network with linear readout and Gaussian likelihood have a largely universal form. We illustrate this explicitly for three tractable network architectures: deep linear fully-connected and convolutional networks, and networks with a single nonlinear hidden layer. Our results begin to elucidate how task-relevant learning signals shape the hidden layer representations of wide Bayesian neural networks.


## 1 Introduction

The expressive power of deep neural networks critically depends on their ability to learn to represent the features of data [1-24]. However, the structure of their hidden layer representations is only theoretically well-understood in certain infinite-width limits, in which these representations cannot flexibly adapt to learn data-dependent features [3-11, 24]. In the Bayesian setting, these representations are described by fixed, deterministic kernels [3-11]. As a result of this inflexibility, recent works have suggested that finite Bayesian neural networks (henceforth BNNs) may generalize better than their infinite counterparts because of their ability to learn representations [10].
Theoretical exploration of how finite and infinite BNNs differ has largely focused on the properties of the prior and posterior distributions over network outputs [12-17]. In particular, several works have studied the leading perturbative finite-width corrections to these distributions [12-16]. Yet, the corresponding asymptotic corrections to the feature kernels, which measure how representations evolve from layer to layer, have only been studied in a few special cases [16]. Therefore, the structure of these corrections, as well as their dependence on network architecture, remain poorly understood. In this paper, we make the following contributions towards the goal of a complete understanding of feature learning at asymptotically large but finite widths:

- We argue that the leading finite-width corrections to the posterior statistics of the hidden layer kernels of any BNN with a linear readout layer and Gaussian likelihood have a largely

prescribed form (Conjecture 1). In particular, we argue that the posterior cumulants of the kernels have well-defined asymptotic series in terms of their prior cumulants, with coefficients that have fixed dependence on the target outputs.
- We explicitly compute the leading finite-width corrections for deep linear fully-connected networks (§4.1), deep linear convolutional networks (§4.2), and networks with a single nonlinear hidden layer (§4.3). We show that our theory yields quantitatively accurate predictions for the result of numerical experiment for tractable linear network architectures, and qualitatively accurate predictions for deep nonlinear networks, where quantitative analytical predictions are intractable.

Our results begin to elucidate the structure of learned representations in wide BNNs. The assumptions of our general argument are satisfied in many regression settings, hence our qualitative conclusions should be broadly applicable.

# 2 Preliminaries 

We begin by defining our notation, setup, and assumptions. We will index training and test examples by Greek subscripts $\mu, \nu, \ldots$, and layer dimensions (that is, neurons) by Latin subscripts $j, l, \ldots$. Layers will be indexed by the script Latin letter $\ell$. Matrix- or vector-valued quantities corresponding to a given layer will be indexed with a parenthesized superscript, while scalar quantities that depend only on the layer will be indexed with a subscript. Depending on context, $\|\cdot\|$ will denote the $\ell_{2}$ norm on vectors or the Frobenius norm on matrices. We denote the standard Euclidean inner product of two vectors $\mathbf{a}, \mathbf{b} \in \mathbb{R}^{n}$ by $\mathbf{a} \cdot \mathbf{b}$.

### 2.1 Bayesian neural networks with linear readout

Throughout this paper, we consider deep Bayesian neural networks with fully connected linear readout. Such a network $\mathbf{f}: \mathbb{R}^{n_{0}} \rightarrow \mathbb{R}^{n_{d}}$ with $d$ layers can be written as

$$
\mathbf{f}\left(\mathbf{x} ; W^{d}, \mathcal{W}\right)=\frac{1}{\sqrt{n_{d-1}}} W^{(d)} \boldsymbol{\psi}(\mathbf{x} ; \mathcal{W})
$$

where the feature map $\boldsymbol{\psi}(\cdot ; \mathcal{W}): \mathbb{R}^{n_{0}} \rightarrow \mathbb{R}^{n_{d-1}}$ includes all $d-1$ hidden layers, collectively parameterized by $\mathcal{W}$. Here, $\boldsymbol{\psi}$ can be some combination of fully-connected feedforward networks, convolutional networks, recurrent networks, et cetera; we assume only that it has a well-defined infinite-width limit in the sense of $\S 2.2$. We let the widths of the hidden layers be $n_{1}, n_{2}, \ldots, n_{d-1}$; we define the width of a convolutional layer to be its channel count [7]. We assume isotropic Gaussian priors over the trainable parameters [1-23], with $W_{i j}^{(d)} \sim_{\text {i.i.d }} \mathcal{N}\left(0, \sigma_{d}^{2}\right)$ in particular.
In our analysis, we fix an arbitrary training dataset $\mathcal{D}=\left\{\left(\mathbf{x}_{\mu}, \mathbf{y}_{\mu}\right)\right\}_{\mu=1}^{p}$ of $p$ examples. We define the input and output Gram matrices of this dataset as $\left[G_{x x}\right]_{\mu \nu} \equiv n_{0}^{-1} \mathbf{x}_{\mu} \cdot \mathbf{x}_{\nu}$ and $\left[G_{y y}\right]_{\mu \nu} \equiv n_{d}^{-1} \mathbf{y}_{\mu} \cdot \mathbf{y}_{\nu}$, respectively. For analytical tractability, we consider a Gaussian likelihood $p(\mathcal{D} \mid \Theta) \propto \exp (-\beta E)$ for

$$
E(\Theta ; \mathcal{D})=\frac{1}{2} \sum_{\mu=1}^{p}\left\|\mathbf{f}\left(\mathbf{x}_{\mu} ; \Theta\right)-\mathbf{y}_{\mu}\right\|^{2}
$$

where $\beta \geq 0$ is an inverse temperature parameter that sets the variance of the likelihood and $\Theta=\left\{W^{(d)}, \mathcal{W}\right\}$ [23]. We then introduce the Bayes posterior over parameters given these data:

$$
p(\Theta \mid \mathcal{D})=\frac{p(\mathcal{D} \mid \Theta) p(\Theta)}{p(\mathcal{D})}
$$

we denote averages with respect to this distribution by $\langle\cdot\rangle$. By tuning $\beta$, one can then adjust whether the posterior is dominated by the prior $(\beta \ll 1)$ or the likelihood $(\beta \gg 1)$. We will mostly focus on the case in which the input dimension is large and the training dataset can be linearly interpolated; the low-temperature limit $\beta \rightarrow \infty$ then enforces the interpolation constraint.

### 2.2 The Gaussian process limit

We consider the limit of large hidden layer widths $n_{1}, n_{2}, \ldots, n_{d-1} \rightarrow \infty$ with $n_{0}, n_{d}, p$, and $d$ fixed. More precisely, we consider a limit in which $n_{\ell}=\alpha_{\ell} n$ for $\ell=1, \ldots, d-1$, where $\alpha_{\ell} \in(0, \infty)$ and

$n \rightarrow \infty$, as studied by [3-15, 17-19, 24] and others. Importantly, we note that size of $n_{0}$ relative to $n$ is unimportant for our results, whereas $n_{d} / n$ and $d / n$ must be small [10, 12, 17].
In this limit, for $\psi$ built out of compositions of most standard neural network architectures, the prior over function values $\mathbf{f}$ tends to a Gaussian process (GP) [3-8]. Moreover, with our choice of a Gaussian likelihood, the posterior over function values also tends weakly to the posterior induced by the limiting GP prior [25]. The kernel of the limiting GP prior is given by the deterministic limit $K_{\infty}^{(d-1)}$ of the inner product kernel of the postactivations of the final hidden layer,

$$
K^{(d-1)}\left(\mathbf{x}, \mathbf{x}^{\prime}\right) \equiv n_{d-1}^{-1} \boldsymbol{\psi}(\mathbf{x}, \mathcal{W}) \cdot \boldsymbol{\psi}\left(\mathbf{x}^{\prime}, \mathcal{W}\right)
$$

multiplied by the prior variance $\sigma_{d}^{2}$ [3-8]. For a broad range of network architectures, $K_{\infty}^{(d-1)}$ can be computed recursively [5-8]. For brevity, we define the kernel matrix evaluated on the training data: $\left[K^{(d-1)}\right]_{\mu \nu} \equiv K^{(d-1)}\left(\mathbf{x}_{\mu}, \mathbf{x}_{\nu}\right)$.

# 3 Elementary perturbation theory for finite Bayesian neural networks 

We first present our main result, which shows that the form of the leading perturbative correction to the average hidden layer kernels of a BNN is tightly constrained by the assumptions that the readout is linear, that the cost is quadratic, and that the GP limit is well-defined.

### 3.1 Finite-width corrections to the posterior cumulants of hidden layer observables

Our main result is as follows:
Conjecture 1 Consider a BNN of the form (1), with posterior (3). Assume that this network admits a well-defined GP limit as discussed in $\S 2.2$. Let $O$ be a hidden layer observable, that is, a function of the hidden layer activations that is not a function of the readout weights $W_{d}$. Assume that $O$ tends in probability to a finite, deterministic limit $O_{\infty}$ under the posterior in the GP limit.
Then, the posterior cumulants of this observable admit well-behaved asymptotic series at large widths in terms of its joint prior cumulants with the postactiviation kernel $K^{(d-1)}$. In particular, the asymptotic expansion of the posterior mean $\langle O\rangle$ has leading terms

$$
\langle O\rangle=\mathbb{E}_{\mathcal{W}} O+\frac{1}{2} n_{d} \sum_{\rho, \lambda=1}^{p}\left[\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right]_{\rho \lambda} \operatorname{cov}_{\mathcal{W}}\left(O, K_{\rho \lambda}^{(d-1)}\right)+\ldots
$$

where $\Gamma \equiv K_{\infty}^{(d-1)}+\beta^{-1} \sigma_{d}^{-2} I_{p}$. Here, the cumulants of the kernels are computed with respect to the prior, and are themselves given by asymptotic series at large widths. The ellipsis denotes terms that are of subleading order in the inverse hidden layer widths.

In Appendix B, we derive this result perturbatively by expanding the posterior cumulant generating function of $O$ in powers of the deviations of $O$ and $K^{(d-1)}$ from their deterministic infinite-width values. There, we also give an asymptotic formula for the posterior covariance of two observables. However, the resulting perturbation series may not rigorously be an asymptotic series, and this method does not yield quantitative bounds for the width-dependence of the terms. We therefore frame it as a conjecture. We note that similar methods can be applied to compute asymptotic corrections to the posterior predictive statistics; we comment on this possibility in Appendix G.
Though this conjecture applies to a broad class of hidden layer observables, the observables of greatest interest are the preactivation or postactivation kernels of the hidden layers within the feature map $\psi$. We will focus on the postactivation kernels $K^{(\ell)}$, which measure how the similarities between inputs evolve as they are propagated through the network [5-10].
Conjecture 1 posits that there are two possible types of leading finite-width corrections to the average kernels. The first class of corrections are deviations of $\mathbb{E}_{\mathcal{W}} K^{(\ell)}$ from $K_{\infty}^{(\ell)}$. These terms reflect corrections to the prior, and do not reflect non-trivial representation learning as they are independent of the outputs. For fully-connected networks, also known as multilayer perceptrons (MLPs), work by Yaida [12] and by Gur-Ari and colleagues $[18,19]$ shows that $\mathbb{E}_{\mathcal{W}} K^{(\ell)}=K_{\infty}^{(\ell)}+\mathcal{O}\left(n^{-1}\right)$. The

second type of correction is the output-dependent term that depends on $\operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu}^{(\ell)}, K_{\rho \lambda}^{(d-1)}\right)$. For deep linear MLPs or MLPs with a single hidden layer, $\mathbb{E}_{\mathcal{W}} K^{(\ell)}$ is exactly equal to $K_{\infty}^{(\ell)}$ at any width (see Appendix C) [3, 12, 18], and only the covariance term contributes. More broadly, these prior works show that $\operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu}^{(\ell)}, K_{\rho \lambda}^{(d-1)}\right)=\mathcal{O}\left(n^{-1}\right)$ for MLPs, and that higher cumulants are of $\mathcal{O}\left(n^{-2}\right)$ [12, 18, 19]. Some of these results have recently been extended to convolutional networks by Andreassen and Dyer [26]. Thus, the finite-width correction to the prior mean should not dominate the feature-learning covariance term, and the terms hidden in the ellipsis should indeed be suppressed.

The leading output-dependent correction has several interesting features. First, it includes a factor of $n_{d}$, reflecting the fact that inference in wide Bayesian networks with many outputs is qualitatively different from that in networks with few outputs relative to their hidden layer width [10]. If $n_{d} / n$ does not tend to zero with increasing $n$, the infinite-width behavior is not described by a standard GP [8, 10]. Moreover, we note that the matrix $\Gamma$ is invertible at any finite temperature, even when $K_{\infty}^{(d-1)}$ is singular. Therefore, provided that one can extend the GP kernel by continuity to non-invertible $G_{x x}$, Conjecture 1 can be applied in the data-dense regime $n_{0}<p$ as well as the data-sparse regime $n_{0}>p$. Furthermore, we observe that the correction depends on the outputs only through their Gram matrix $G_{y y}$. This result is intuitively sensible, since with our choice of likelihood and prior the function-space posterior is invariant under simultaneous rotation of the output activations and targets. Finally, $G_{y y}$ is transformed by factors of the matrix $\Gamma^{-1}$, hence the correction depends on certain interactions between the output similarities and the GP kernel $K_{\infty}^{(d-1)}$.

# 3.2 High- and low-temperature limits of the leading correction 

To gain some intuition for the properties of the leading finite-width corrections, we consider their high- and low-temperature limits. These limits correspond to tuning the posterior (3) to be dominated by the prior or the likelihood, respectively. At high temperatures ( $\beta \ll 1$ ), expanding $\Gamma^{-1}$ as a Neumann series (see Appendix A and [27]) yields

$$
\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}=-\beta \sigma_{d}^{2} I_{p}+\left(\beta \sigma_{d}^{2}\right)^{2}\left(\sigma_{d}^{-2} G_{y y}+K_{\infty}^{(d-1)}\right)+\mathcal{O}\left[\left(\beta \sigma_{d}^{2}\right)^{3}\right]
$$

Thus, at high temperatures, the outputs only influence the average kernels of Conjecture 1 to subleading order in both width and $\beta$, which reflects the fact that the likelihood is discounted relative to the prior in this regime. Moreover, the leading output-dependent contribution averages together $G_{y y}$ and $K_{\infty}^{(d-1)}$, hence, intuitively, there is no way to 'cancel' the GP contributions to the average kernels. We note that, at infinite temperature $(\beta=0)$, the posterior reduces to the prior, and all finite-width corrections to the average kernels arise from the discrepancy between $\mathbb{E}_{\mathcal{W}} K^{(\ell)}$ and $K_{\infty}^{(\ell)}$.

At low temperatures $(\beta \gg 1)$, the behavior of $\Gamma^{-1}$ differs depending on whether or not $K_{\infty}^{(d-1)}$ is of full rank. Assuming for simplicity that it is invertible, we have

$$
\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}=\left[K_{\infty}^{(d-1)}\right]^{-1}\left(\sigma_{d}^{-2} G_{y y}-K_{\infty}^{(d-1)}\right)\left[K_{\infty}^{(d-1)}\right]^{-1}+\mathcal{O}\left[\left(\beta \sigma_{d}^{2}\right)^{-1}\right]
$$

in the non-invertible case there are additional contributions involving projectors onto the null space of $K_{\infty}^{(d-1)}$. Therefore, the leading-order low temperature correction depends on the difference between the target and GP kernels, while the leading non-trivial high temperature correction depends on their sum.

## 4 Learned representations in tractable network architectures

Having derived the general form of the leading perturbative finite-width correction to the average feature kernels, we now consider several example network architectures. For these tractable examples, we provide explicit formulas for the feature-learning corrections to the hidden layer kernels, and test the accuracy of our theory with numerical experiments.

### 4.1 Deep linear fully-connected networks

We first consider deep linear fully-connected networks with no bias terms. Concretely, we consider a network with activations $\mathbf{h}^{(\ell)} \in \mathbb{R}^{n_{\ell}}$ recursively defined via $\mathbf{h}^{(\ell)}=n_{\ell-1}^{-1 / 2} W^{(\ell)} \mathbf{h}^{(\ell-1)}$ with base case

$\mathbf{h}^{(0)}=\mathbf{x}$, where the prior distribution of weights is $\left[W^{(\ell)}\right]_{i j} \sim_{\text {i.i.d. }} \mathcal{N}\left(0, \sigma_{\ell}^{2}\right)$. For such a network, the hidden layer kernels $\left[K^{(\ell)}\right]_{\mu \nu} \equiv n_{\ell}^{-1} \mathbf{h}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\nu}^{(\ell)}$ have deterministic limits $K_{\infty}^{(\ell)}=m_{\ell}^{2} G_{x x}$, where $m_{\ell}^{2} \equiv \sigma_{\ell}^{2} \sigma_{\ell-1}^{2} \cdots \sigma_{\mathrm{I}}^{2}$ is the product of prior variances up to layer $\ell$. Higher prior cumulants of the kernels are easy to compute with the aid of Isserlis' theorem for Gaussian moments (see Appendix C) [28, 29], yielding

$$
\frac{\left\langle K^{(\ell)}\right\rangle}{m_{\ell}^{2}}=G_{x x}+\left(\sum_{\ell^{\prime}=1}^{\ell} \frac{n_{d}}{n_{\ell^{\prime}}}\right) G_{x x} \Gamma^{-1}\left(m_{d}^{-2} G_{y y}-\Gamma\right) \Gamma^{-1} G_{x x}+\mathcal{O}\left(n^{-2}\right)
$$

where $\Gamma \equiv G_{x x}+I_{p} /\left(\beta m_{d}^{2}\right)$ and $\ell=1, \ldots, d-1$. In Appendix D, we show that this result can be derived directly through an ab initio perturbative calculation of the cumulant generating function of the kernels, without relying on our heuristic argument for the general version of Conjecture 1. Moreover, in Appendix E, we show that the form of the correction remains the same even if one allows arbitrary forward skip connections, though the dependence on width and depth is given by a more complex recurrence relation.

Thus, the leading corrections to the normalized average kernels $\left\langle K^{(\ell)}\right\rangle / m_{\ell}^{2}$ are identical across all hidden layers up to a scalar factor that encodes the width-dependence of the correction. This sum-of-inverse-widths dependence was previously noted by Yaida [12] in his study of the corrections to the prior of a deep linear network. For a network with hidden layers of equal width $n$, we have the simple linear dependence $\sum_{\ell^{\prime}=1}^{\ell}\left(n_{d} / n_{\ell^{\prime}}\right)=n_{d} \ell / n$. If one instead includes a narrow bottleneck in an otherwise wide network, this dependence predicts that the kernels before the bottleneck should be close to their GP values, while those after the bottleneck should deviate strongly.
This result simplifies further at low temperatures, where, by the result of $\S 3.2$, we have

$$
\frac{\left\langle K^{(\ell)}\right\rangle}{m_{\ell}^{2}}=G_{x x}+\left(\sum_{\ell^{\prime}=1}^{\ell} \frac{n_{d}}{n_{\ell^{\prime}}}\right)\left(m_{d}^{-2} G_{y y}-G_{x x}\right)+\mathcal{O}\left(n^{-2}, \beta^{-1}\right)
$$

in the regime in which $G_{x x}$ is invertible. We thus obtain the simple qualitative picture that the low-temperature average kernels linearly interpolate between the input and output Gram matrices. In Appendix F, we show that this limiting result can be recovered from the recurrence relation derived through other methods by Aitchison [10], who did not use it to compute finite-width corrections. We note that the low-temperature limit is peculiar in that the mean predictor reduces to the least-norm pseudoinverse solution to the underlying underdetermined linear system $X W=Y$; we comment on this property in Appendix G.
We can gain some additional understanding of the structure of the correction by using the eigendecomposition of $G_{x x}$. As $G_{x x}$ is by definition a real positive semidefinite matrix, it admits a unitary eigendecomposition $G_{x x}=U \Lambda U^{\dagger}$ with non-negative eigenvalues $\Lambda_{\mu \mu}$. In this basis, the average kernel is

$$
\frac{1}{m_{\ell}^{2}} U^{\dagger}\left\langle K^{(\ell)}\right\rangle U=\Lambda+\left(\sum_{\ell^{\prime}=1}^{\ell} \frac{n_{d}}{n_{\ell^{\prime}}}\right)\left(m_{d}^{-2} \tilde{\Lambda} U^{\dagger} G_{y y} U \tilde{\Lambda}-\tilde{\Lambda} \Lambda\right)+\mathcal{O}\left(n^{-2}\right)
$$

where we have defined the diagonal matrix $\tilde{\Lambda} \equiv \beta m_{d}^{2} \Lambda\left(I_{p}+\beta m_{d}^{2} \Lambda\right)^{-1}$. As $\beta m_{d}^{2} \Lambda \geq 0$, the diagonal elements of $\tilde{\Lambda}$ are bounded as $0 \leq \tilde{\Lambda}_{\mu \mu} \leq 1$. Thus, the factors of $\Gamma^{-1} G_{x x}$ by which $G_{y y}$ is conjugated have the effect of suppressing directions in the projection of $G_{y y}$ onto the eigenspace of $G_{x x}$ with small eigenvalues. We can see that this effect will be enhanced at high temperatures $(\beta \ll 1)$ and small scalings $\left(m_{d}^{2} \ll 1\right)$, and suppressed at low temperatures and large scalings. For this linear network, similarities are not enhanced, only suppressed. Moreover, if $G_{x x}$ is diagonal, then a given element of the average kernel will depend only on the corresponding element of $G_{y y}$.
We now seek to numerically probe how accurately these asymptotic corrections predict learned representations in deep fully-connected linear BNNs. Using Langevin sampling [30, 31], we trained deep linear networks of varying widths, and compared the difference between the empirical and GP kernels with theory predictions. We provide a detailed discussion of our numerical methods in Appendix I. In Figure 1, we present an experiment with a 2-layer linear neural network trained on the MNIST dataset of handwritten digit images [32] using the Neural Tangents library [33]. We find an excellent agreement with our theory, confirming the inverse scaling with width and linear scaling with depth for the deviations from GP kernel.

![img-0.jpeg](img-0.jpeg)

Figure 1: Learned representations in two-hidden-layer linear fully-connected neural networks with varying widths trained via Langevin sampling on 5000 MNIST images (see Appendix I for more details). **a)** The Frobenius norm of the deviation of the empirical average kernel of each layer from its GP value (in this case, simply $G_{xx}$) for varying widths. We see perfect match with theoretical predictions, which are shown as dashed lines. We obtain the predicted $1/n$ decay with increasing width and the linear scaling with the depth where the deviations for first and second layers differ by a factor of 2. **b)-c)** Scatter plot of individual elements of the experimental (ordinate) and theoretical (abscissa) kernels for both layers. For low widths a slight deviation is visible between experiment and theory, while for larger widths the agreement is better.

### 4.2 Deep linear convolutional networks

To demonstrate the applicability of Conjecture 1 to non-fully-connected BNNs, we consider deep convolutional linear networks with no bias terms. Here, the appropriate notion of width is the number of channels in each hidden layer [7]. Following the setup of Novak et al. [7] and Xiao et al. [34], we consider a network consisting of $d-1$ linear convolutional layers followed by a fully-connected linear readout layer. For simplicity, we restrict our attention to convolutions with periodic boundary conditions, and do not include internal pooling layers (see Appendix C for more details). Concretely, we consider a network with hidden layer activations $h_{i,\mathfrak{a}}^{(\ell)}$, where $i$ indexes the $n_{\ell}$ channels of the layer and $\mathfrak{a}$ is a spatial multi-index. The hidden layer activations are then defined through the recurrence

$$h_{i,\mathfrak{a}}^{(\ell)}(x) = \frac{1}{\sqrt{n_{\ell-1}}} \sum_{j=1}^{n_{\ell-1}} \sum_{\mathfrak{b}} w_{ij,\mathfrak{b}}^{(\ell)} h_{j,\mathfrak{a}+\mathfrak{b}}^{(\ell-1)}(x) \tag{11}$$

with base case $h_{i,\mathfrak{a}}^{(0)}(x) = x_{i,\mathfrak{a}}$, where $i$ indexes the input channels (e.g., image color channels). The feature map is then formed by flattening the output of the last hidden layer into an $n_{d-1} s$-dimensional vector, where $s$ is the total dimensionality of the inputs (see Appendix C for details). We fix the prior distribution of the filter elements to be $w_{ij,\mathfrak{a}}^{(\ell)} \underset{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma_{\ell}^2 v_{\mathfrak{a}})$, where $v_{\mathfrak{a}} > 0$ is a weighting factor that sets the fraction of receptive field variance at location $\mathfrak{a}$ (and is thus subject to the constraint $\sum_{\mathfrak{a}} v_{\mathfrak{a}} = 1$). For inputs $[x_{\mu}]_{i,\mathfrak{a}}$ and $[x_{\nu}]_{i,\mathfrak{a}}$, we introduce the four-index hidden layer kernels

$$K_{\mu\nu, \mathfrak{a}\mathfrak{b}}^{(\ell)} \equiv \frac{1}{n_{\ell}} \sum_{i=1}^{n_{\ell}} h_{i,\mathfrak{a}}^{(\ell)}(x_{\mu})h_{i,\mathfrak{b}}^{(\ell)}(x_{\nu}). \tag{12}$$

With the given readout strategy, the two-index feature map kernel appearing in Conjecture 1 is related to the four-index kernel of the last hidden layer by $K_{\mu\nu}^{(d-1)} = \frac{1}{s} \sum_{\mathfrak{a}} K_{\mu\nu, \mathfrak{a}\mathfrak{a}}^{(d-1)}$. We discuss other readout strategies in Appendix C, but use this vectorization strategy in our numerical experiments.

As shown by Xiao et al. [34], the infinite-width four-index kernel obeys the recurrence

$$[K_{\infty}^{(\ell)}]_{\mu\nu, \mathfrak{a}\mathfrak{b}} = \sigma_{\ell}^2 \sum_{\mathfrak{c}} v_{\mathfrak{c}}[K_{\infty}^{(\ell-1)}]_{\mu\nu, (\mathfrak{a}+\mathfrak{c})(\mathfrak{b}+\mathfrak{c})} \tag{13}$$

with base case $[K_{\infty}^{0}]_{\mu\nu, \mathfrak{a}\mathfrak{b}} = [G_{xx}]_{\mu\nu, \mathfrak{a}\mathfrak{b}} \equiv \frac{1}{n_{0}} \sum_{i=1}^{n_{0}} [x_{\mu}]_{i,\mathfrak{a}} [x_{\nu}]_{i,\mathfrak{b}}$. This gives convolutional linear networks a sense of spatial hierarchy that is not present in the fully-connected case: even at infinite width, the kernels include iterative spatial averaging.

In Appendix C, we derive the kernel covariances appearing in Conjecture 1. As in the fully-connected case, this computation is easy to perform with the aid of Isserlis' theorem. The general result is

![img-1.jpeg](img-1.jpeg)

Figure 2: The MNIST image dataset and experiments for neural networks with two 1D convolutional layers. (a) A 10 × 10 MNIST image downsized from 28 × 28 pixels. (b) Input Gram matrix for 300 MNIST images. (c) A single (µ, ν) component of the input tensor [G_{xx}]_{µν,ab} obtained using Eq. (13). (d) The output Gram matrix. (e) The Frobenius norm of the correction to the 1D convolutional GP kernel is inversely proportional to the width. Here, the dashed lines are the theoretical predictions. (f) Scatter plots of individual elements of the empirical corrections to the GP kernels against the theoretical predictions for both layers show excellent agreement.

somewhat complicated, but things simplify under the assumption that readout is performed using vectorization. Then, one finds that

$$
\langle K_{\mu \nu, \mathbf{ab}}^{(\ell)}\rangle = [K_{\infty}^{(\ell)}]_{\mu \nu, \mathbf{ab}} + \left(\prod_{\ell'=\ell''}^{\ell''} \sigma_{\ell''}^{2}\right) \left(\sum_{l''=1}^{\ell} \frac{n_{d}}{n_{l''}}\right) \frac{1}{s} \sum_{i=1}^{s} \sum_{\rho, \lambda=1}^p [K_{\infty}^{(\ell)}]_{\mu \rho, \mathbf{ab}} \Phi_{\rho\lambda} [K_{\infty}^{(\ell)}]_{\lambda \nu, \mathbf{ab}} + \mathcal{O}(n^{-2}), \tag{14}
$$

where we have defined Φ_{ρλ} ≡ [σ_{d}^{-2}Γ^{-1}G_{yy}Γ^{-1} - Γ^{-1}]_{ρλ} for brevity. Thus, the correction to the convolutional kernel is quite similar to that obtained in the fully-connected case. To this order, the difference between these network architectures manifests itself largely through the difference in the infinite-width kernels. In Appendix C, we show that a similar simplification holds if readout is performed using global average pooling over space.

As we did for fully-connected networks, we test whether our theory accurately predicts the results of numerical experiment, using the MNIST digit images illustrated in 2(a-d). We consider a network with one-dimensional (Figure 2e and f) and two-dimensional (Figure 3) convolutional hidden layers, trained to classify 50 MNIST images (see Appendix I for details of our numerical methods). As shown in Figure 2(e, f) (Figure 3(a,b) for 2D convolutions), we again obtain good quantitative agreement between the predictions of our asymptotic theory and the results of numerical experiment. In Figure 3c, we directly visualize the learned feature kernels for 2D convolutional layers, illustrating the good agreement between theory and experiment. Therefore, our asymptotic theory can be applied to accurately predict learned representations in deep convolutional linear networks.

### 4.3 Networks with a single nonlinear hidden layer

Finally, we would like to gain some understanding of how including nonlinearity affects the structure of learned representations. However, for a nonlinear MLP, it is usually not possible to analytically compute cov_{W}(K_{µν}^{ℓ, ϕ, K}_{µλ}) to the required order [9, 12, 18, 19]. Here, we consider the case of a network with a single nonlinear layer and no bias terms, in which we can both summarize the key obstacles to studying deep nonlinear networks and gain some intuitions about how they might differ from linear BNNs. Concretely, we consider a network with feature map ψ(x;W(1)) =

![img-2.jpeg](img-2.jpeg)

Figure 3: Learned representations in two-hidden-layer linear 2-D convolutional networks of varying channel widths. (a) The Frobenius norm of the correction to the GP kernel is inversely proportional to the width. Here, the dashed lines represent theory predictions. (b) Scatter plots of individual elements of the empirical corrections to the GP kernels against the theoretical predictions for both layers show good agreement. (c) A single component (µ, ν) of the learned feature kernels in 2-layer CNN experiments for both convolutional layers. While the experimental kernel looks quite similar the GP (first and second columns), their difference shows the finite width corrections to the GP (last column).

φ(n<sup>−1/2</sup> W(1) x) for an elementwise activation function φ, where the weight matrix W(1) has prior distribution [W(1)]<sub>ij</sub> ∼<sub>i+1</sub> N(0, σ<sub>1</sub><sup>2</sup>). The only hidden layer kernel of this network is the feature map postactivation kernel K<sub>µν</sub> defined in (4), where we drop the layer index for brevity. As detailed in Appendix H, for such a network we have the exact expressions

$$
\begin{aligned}
{[K_{\infty}]_{\mu\nu} = \mathbb{E}_{\mathcal{W}}K_{\mu\nu} &= \mathbb{E}[\phi(h_{\mu})\phi(h_{\nu})],} \\
n_1 \operatorname{cov}_{\mathcal{W}}(K_{\mu\nu}, K_{\rho\lambda}) &= \mathbb{E}[\phi(h_{\mu})\phi(h_{\nu})\phi(h_{\rho})\phi(h_{\lambda})] - [K_{\infty}]_{\mu\nu}[K_{\infty}]_{\rho\lambda},
\end{aligned}
\tag{15}
$$

where expectations are taken over the p-dimensional Gaussian random vector h<sub>µ</sub>, which has mean zero and covariance cov(h<sub>µ</sub>, h<sub>ν</sub>) = σ<sub>1</sub><sup>2</sup>[G<sub>xx</sub>]<sub>µν</sub>. Unlike for deeper nonlinear networks, here there are no finite-width corrections to the prior expectations [3, 12, 18].

Though these expressions are easy to define, it is not possible to evaluate the four-point expectation in closed form for general Gram matrices G<sub>xx</sub> and activation functions φ, including ReLU and erf. This obstacle has been noted in previous studies [9, 12, 15], and makes it challenging to extend approaches similar to those used here to deeper nonlinear networks. For polynomial activation functions, the required expectations can be evaluated using Isserlis' theorem (see Appendix A). However, even for a quadratic activation function φ(x) = x<sup>2</sup>, the resulting formula for the kernel will involve many elementwise matrix products, and cannot be simplified into an intuitively comprehensible form.

If the input Gram matrix G<sub>xx</sub> is diagonal, the four-point expectation becomes tractable because the required expectations factor across sample indices. In this simple case, there is an interesting distinction between the behavior of activation functions that yield Eφ(h) = 0 and those that yield Eφ(h) ≠ 0. As detailed in Appendix D, if Eφ(h) = 0, K<sub>∞</sub> is diagonal, and a given element of the leading finite-width correction to 〈K〉 depends only on the corresponding element of G<sub>yy</sub>. However, if Eφ(h) ≠ 0, then K<sub>∞</sub> includes a rank-1 component, and each element of the correction depends on all elements of G<sub>yy</sub>. This means that the case in which G<sub>xx</sub> is diagonal is qualitatively distinct from the case in which there is only a single training input for such activation functions.

## 5 Learned representations in deep nonlinear networks

In the preceding section, we noted that analytical study of learned representations in deep nonlinear BNNs is generally quite challenging. Here, we use numerical experiments to explore whether any

![img-3.jpeg](img-3.jpeg)

Figure 4: 3-hidden layer neural network with ReLU activations trained via Langevin sampling on 1000 MNIST images (see Appendix I). (a) The empirical average kernels subtracted from their corresponding GP kernels for all layers with varying widths. Labels on the y -axes indicate the widths of each layer. We observe that for networks with bottleneck layers, the deviation from $K_{\infty}^{(t)}$ is largest at the bottleneck indicating representation learning; without a bottleneck deviations are considerably less (the last row). (b) Hidden layer kernel deviation from GP kernels as a function of width for bottleneck networks. While the first layer shows $1 / n$ scaling, the bottleneck layer and the $3^{\text {rd }}$ layer deviations stay almost constant. This behavior is predicted analytically for linear networks. (c) As in (b) for networks without a bottleneck. Consistent with our theory, all layers display $1 / n$ decay.
of the intuitions gained in the linear setting carry over to nonlinear networks. Concretely, we study how narrow bottlenecks affect representation learning in a more realistic nonlinear network. We train a network with three hidden layers and ReLU activations on a subset of the MNIST dataset [32]. Despite its analytical simplicity, ReLU is among the activation functions for which the covariance term in Conjecture 1 cannot be evaluated in closed form (see §4.3). However, it is straightforward to simulate numerically. Consistent with the predictions of our theory for linear networks, we find that introducing a narrow bottleneck leads to more representation learning in subsequent hidden layers, even if those layers are quite wide (Figure 4). Quantitatively, if one increases the width of the hidden layers between which the fixed-width bottleneck is sandwiched, the deviation of the first layer's kernel from its GP value decays roughly as $1 / n$ with increasing width, while the deviations for the bottleneck and subsequent layers remain roughly constant. In contrast, the kernel deviations throughout a network with equal-width hidden layers decay roughly as $1 / n$ (Figure 4). These observations are qualitatively consistent with the width-dependence of the linear network kernel (8), as well as with previous studies of networks with infinitely-wide layers separated by a finite bottleneck [35]. Keeping in mind the obstacles noted in $\S 4.3$, precise characterization of nonlinear networks will be an interesting objective for future work.

# 6 Related work 

Our work is closely related to several recent analytical studies of finite-width BNNs. First, Aitchison [10] argued that the flexibility afforded by finite-width BNNs can be advantageous. He derived a

recurrence relation for the learned feature kernels in deep linear networks, which he solved in the limits of infinite width and few outputs, narrow width and many outputs, and infinite width and many outputs. As discussed in $\S 4.1$ and in Appendix F, our results on deep linear networks extend those of his work. Furthermore, our numerical results support his suggestion that networks with narrow bottlenecks may learn interesting features.
Moreover, our analytical approach and the asymptotic regime we consider mirror recent perturbative studies of finite-width BNNs. As noted in $\S 3$ and Appendix B, we make use of the results of Yaida [12], who derived recurrence relations for the perturbative corrections to the cumulants of the finitewidth prior for an MLP. However, Yaida did not attempt to study the statistics of learned features; the goal of his work was to establish a general framework for the study of finite-width corrections. Bounds on the prior cumulants of a broader class of observables have been studied by Gur-Ari and colleagues [18, 19, 26]; these results could allow for the identification of observables to which Conjecture 1 should apply. Finally, perturbative corrections to the network prior and posterior have been studied by Halverson et al. [13] and Naveh et al. [15], respectively. Our work builds upon these studies by perturbatively characterizing the internal representations that are learned upon inference.
Following the appearance of our work in preprint form, Roberts et al. [36] announced an alternative derivation of the zero-temperature limit of Conjecture 1 for MLPs; we have adopted their terminology of hidden layer observables. As in Yaida [12]'s earlier work, they rely on sequential perturbative approximation of the prior over preactivations as the hidden layers are marginalized out in order from the first to the last. While our elementary perturbative argument for Conjecture 1 does not require assuming a particular network architecture for the hidden layers, it takes as input information regarding the prior cumulants that would have to be approximated using such methods. Moreover, the approach of layer-by-layer approximation to the prior could enable a fully rigorous version of Conjecture 1 to be proved on an architecture-by-architecture basis [37].
Our work, like most studies of wide BNNs [3-15, 17-19, 24], focuses on the regime in which the sample size $p$ is held fixed while the hidden layer width scale $n$ tends to infinity, i.e., $p \ll n$. One can instead consider regimes in which $p$ is not negligible relative to $n$, in which the posterior would be expected to concentrate. The behavior of deep linear BNNs in this regime was recently studied by Li and Sompolinsky [16], who computed asymptotic approximations for the predictor statistics and hidden layer kernels. In Appendix F, we show that our result (9) for the zero-temperature kernel can be recovered as the $p / n \downarrow 0$ limit of their result. As the dataset size $p$ appears only implicitly in our approach, we leave the incorporation of large- $p$ corrections as an interesting objective for future work. We note, however, that alternative methods developed to study the large- $p$ regime $[16,38]$ cannot overcome the obstacles to analytical study of deep nonlinear networks encountered here.

# 7 Conclusions 

In this paper, we have shown that the leading perturbative feature learning corrections to the infinitewidth kernels of wide BNNs with linear readout and least-squares cost should be of a tightly constrained form. We demonstrate analytically and with numerical experiments that these results hold for certain tractable network architectures, and conjecture that they should extend to more general network architectures that admit a well-defined GP limit.
Limitations. We emphasize that our perturbative argument for Conjecture 1 is not rigorous, and that we have not obtained quantitative bounds on the remainder for general network architectures. It is possible that there are non-perturbative contributions to the posterior statistics that are not captured by Conjecture 1; non-perturbative investigation of feature learning in finite BNNs will be an interesting objective for future work [17, 39]. More broadly, we leave rigorous proofs of the applicability of our results to more general architectures and of the smallness of the remainder as objective for future work. As mentioned above, one could attempt such a proof on an architecture-by-architecture basis [12, 36, 37]. Alternatively, one could attempt to treat all sufficiently sensible architectures uniformly $[8,9]$. Furthermore, we have considered only one possible asymptotic regime: that in which the width is taken to infinity with a finite training dataset and small output dimensionality. As discussed above in reference to the work of Aitchison [10] and Li and Sompolinsky [16], investigation of alternative limits in which output dimension, dataset size, depth, and hidden layer width are all taken to infinity with fixed ratios may be an interesting subject for future work.

# Acknowledgments and Disclosure of Funding 

We thank B. Bordelon for helpful comments on our manuscript. JAZ-V acknowledges partial support from the NSF-Simons Center for Mathematical and Statistical Analysis of Biology at Harvard and the Harvard Quantitative Biology Initiative. This work was further supported by the Harvard Data Science Initiative Competitive Research Fund, the Harvard Dean's Competitive Fund for Promising Scholarship, and a Google Faculty Research Award. The authors declare no conflict of interest.

# Supplemental Information 

A Preliminary technical results ..... S1
B Perturbation theory for wide Bayesian neural networks with linear readout ..... S2
C Explicit covariance computations in deep linear networks ..... S6
D Direct computation of the average hidden layer kernels of a deep linear MLP ..... S10
E Average kernels in a deep feedforward linear network with skip connections ..... S18
F Comparison to the results of Aitchison (2020) and Li \& Sompolinsky (2020) ..... S22
G Predictor statistics and generalization in deep linear networks ..... S24
H Derivation of the average kernels for a depth-two network ..... S27
I Numerical methods ..... S28

## A Preliminary technical results

In this appendix, we review useful technical results upon which our calculations rely.

## A. 1 Isserlis' theorem for Gaussian moments

Let $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ be a zero-mean Gaussian random vector. Then, Isserlis' theorem [28] states that

$$
\mathbb{E}\left[x_{1} x_{2} \cdots x_{n}\right]= \begin{cases}\sum_{p \in P_{n}^{2}} \prod_{(i, j) \in p} \operatorname{cov}\left(x_{i}, x_{j}\right) & n \text { even } \\ 0 & n \text { odd }\end{cases}
$$

where the sum is over all pairings $p$ of $\{1,2, \ldots, n\}$ and the product is over all pairs contained in $p$. In particular, for $n=4$, we have

$$
\mathbb{E}\left[x_{1} x_{2} x_{3} x_{4}\right]=\operatorname{cov}\left(x_{1}, x_{2}\right) \operatorname{cov}\left(x_{3}, x_{4}\right)+\operatorname{cov}\left(x_{1}, x_{3}\right) \operatorname{cov}\left(x_{2}, x_{4}\right)+\operatorname{cov}\left(x_{1}, x_{4}\right) \operatorname{cov}\left(x_{2}, x_{3}\right)
$$

In physics, Isserlis' theorem is often known as Wick's probability theorem [29].

## A. 2 Neumann series for matrix inverses near the identity

The Neumann series is the generalization of the geometric series to bounded linear operators, including square matrices. In particular, let $A$ be a $p \times p$ square matrix. Then, we have

$$
\left(I_{p}-A\right)^{-1}=\sum_{k=0}^{\infty} A^{k}
$$

provided that the series converges in the operator norm [27]. We will use this result without concern for rigorous convergence conditions, as we are interested only in asymptotic expansions.

## A. 3 Series expansion of the log-determinant near the identity

Let $A$ be a $p \times p$ square matrix, and let $t$ be a small parameter. Then, we have

$$
\log \operatorname{det}\left(I_{p}+t A\right)=\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} \operatorname{tr}\left(A^{k}\right) t^{k}
$$

assuming that the series converges. We will not concern ourselves with rigorous convergence conditions, as we will use this expansion formally.
This result follows from the fact that

$$
\frac{\partial^{k}}{\partial t^{k}} \log \operatorname{det}\left(I_{p}+t A\right)=(-1)^{k+1}(k-1)!\operatorname{tr}\left(\left(I_{p}+t A\right)^{-k} A^{k}\right) \quad(k=1,2, \ldots)
$$

The base case $k=1$ is given by Jacobi's formula [27]:

$$
\frac{\partial}{\partial t} \log \operatorname{det}\left(I_{p}+t A\right)=\operatorname{tr}\left(\left(I_{p}+t A\right)^{-1} A\right)
$$

Then, using the identity

$$
\frac{\partial}{\partial t}\left(I_{p}+t A\right)^{-1}=-\left(I_{p}+t A\right)^{-1} A\left(I_{p}+t A\right)^{-1}
$$

and the fact that $A$ commutes with $\left(I_{p}+t A\right)^{-1}$, we find that the claim holds by induction. As $\left.\log \operatorname{det}\left(I_{p}+t A\right)\right|_{t=0}=0$, this implies the desired Maclaurin series.

# B Perturbation theory for wide Bayesian neural networks with linear readout 

In this appendix, we derive Conjecture 1. As outlined in the main text, we consider a depth- $d$ neural network $\mathbf{f}: \mathbb{R}^{n_{0}} \rightarrow \mathbb{R}^{n_{d}}$ with linear readout, written as

$$
\mathbf{f}\left(\mathbf{x} ; W^{d}, \mathcal{W}\right)=\frac{1}{\sqrt{n_{d-1}}} W^{(d)} \boldsymbol{\psi}(\mathbf{x} ; \mathcal{W})
$$

in terms of the hidden layer feature map $\boldsymbol{\psi}(\cdot ; \mathcal{W}): \mathbb{R}^{n_{0}} \rightarrow \mathbb{R}^{n_{d-1}}$. The full set of trainable parameters is then $\Theta=\left\{W^{(d)}, \mathcal{W}\right\}$, where $\mathcal{W}$ is the set of feature map parameters. We assume isotropic Gaussian priors over these parameters, with, for instance,

$$
W_{i j}^{(d)} \underset{\text { i.i.d. }}{\sim} \mathcal{N}\left(0, \sigma_{d}^{2}\right)
$$

We fix an arbitrary training dataset $\mathcal{D}=\left\{\left(\mathbf{x}_{\mu}, \mathbf{y}_{\mu}\right)\right\}_{\mu=1}^{p}$ of $p$ examples, and use a Gaussian likelihood $p(\mathcal{D} \mid \Theta) \propto \exp (-\beta E)$, where

$$
E(\Theta ; \mathcal{D})=\frac{1}{2} \sum_{\mu=1}^{p}\left\|\mathbf{f}\left(\mathbf{x}_{\mu}\right)-\mathbf{y}_{\mu}\right\|^{2}
$$

is a quadratic cost. We then introduce the Bayes posterior

$$
p(\Theta \mid \mathcal{D})=\frac{p(\mathcal{D} \mid \Theta) p(\Theta)}{p(\mathcal{D})}
$$

averages with respect to this distribution will be denoted by $\langle\cdot\rangle$.
We define the postactivation feature map kernel

$$
K^{(d-1)}\left(\mathbf{x}, \mathbf{x}^{\prime}\right) \equiv n_{d-1}^{-1} \boldsymbol{\psi}(\mathbf{x}, \mathcal{W}) \cdot \boldsymbol{\psi}\left(\mathbf{x}^{\prime}, \mathcal{W}\right)
$$

and write $\left[K^{(d-1)}\right]_{\mu \nu} \equiv K^{(d-1)}\left(\mathbf{x}_{\mu}, \mathbf{x}_{\nu}\right)$ for the kernel evaluated on the training set. For brevity, we will frequently abbreviate $K \equiv K^{(d-1)}$ throughout this appendix.
We denote expectation by $\mathbb{E}$, and prior expectation by $\mathbb{E}_{\mathcal{W}}$. We also introduce the joint cumulant operator $\mathbb{K}$ and its prior counterpart $\mathbb{K}_{\mathcal{W}}$. We will only require the second and third joint cumulants, which, for random variables $A, B$, and $C$, are given as

$$
\mathbb{K}(A, B)=\mathbb{E}[(A-\mathbb{E} A)(B-\mathbb{E} B)]
$$

and

$$
\mathbb{K}(A, B, C)=\mathbb{E}[(A-\mathbb{E} A)(B-\mathbb{E} B)(C-\mathbb{E} C)]
$$

respectively.
Our starting point is the partition function $Z$ of the Bayes posterior (3) for the network (1), including a source term for the (generically matrix-valued) observable $O$ :

$$
Z(J)=\mathbb{E}_{W^{(d)}} \mathbb{E}_{\mathcal{W}} \exp \left(-\beta E+\operatorname{tr}\left(J^{\top} O\right)\right)
$$

where $\mathcal{W}$ denotes all of the parameters except for the readout weight matrix $W^{(d)}$ and expectation is taken with respect to the Gaussian prior. The logarithm of the partition function is the posterior cumulant generating function of the observable $O$, with

$$
\langle O\rangle=\left.\frac{\delta \log Z}{\delta J}\right|_{J=0}
$$

and covariance

$$
\operatorname{cov}\left(O_{\rho \gamma}, O_{\omega \chi}\right)=\left.\frac{\partial^{2} \log Z}{\partial J_{\rho \gamma} \partial J_{\omega \chi}}\right|_{J=0}
$$

# B. 1 Integrating out the readout layer 

We first show that the readout layer can be integrated out exactly. As the source term is independent of $W^{(d)}$, Fubini's theorem yields

$$
Z=\mathbb{E}_{\mathcal{W}}\left[\exp \left(\operatorname{tr}\left(J^{\top} O\right)\right) \mathbb{E}_{W^{(d)}} \exp (-\beta E)\right]
$$

The expectation over $W^{d}$ is a Gaussian integral, hence it is easy to evaluate exactly:

$$
\begin{aligned}
& \mathbb{E}_{W^{(d)}} \exp (-\beta E) \\
& =\mathbb{E}_{W^{(d)}} \exp \left(-\frac{1}{2} \beta \sum_{\mu=1}^{p}\left\|\frac{1}{\sqrt{n_{d-1}}} W^{(d)} \boldsymbol{\psi}_{\mu}-\mathbf{y}_{\mu}\right\|^{2}\right) \\
& =\exp \left(-\frac{1}{2} \beta \operatorname{tr}\left(Y^{\top} Y\right)\right) \\
& \quad \times \prod_{j=1}^{n_{d}}\left[\int \frac{d \mathbf{w}_{j}}{\left(2 \pi \sigma_{d}^{2}\right)^{n_{d-1} / 2}} \exp \left(-\frac{1}{2} \mathbf{w}_{j}^{\top}\left(\sigma_{d}^{-2} I_{n}+\frac{\beta}{n_{d-1}} \Psi^{\top} \Psi\right) \mathbf{w}_{j}+\frac{\beta}{\sqrt{n_{d-1}}}\left(Y^{\top} \Psi\right)_{j} \cdot \mathbf{w}_{j}\right)\right] \\
& =\operatorname{det}\left(I_{n}+\frac{\beta \sigma_{d}^{2}}{n_{d-1}} \Psi^{\top} \Psi\right)^{-n_{d} / 2} \\
& \quad \times \exp \left(\frac{1}{2} \frac{\beta^{2} \sigma_{d}^{2}}{n_{d-1}} \operatorname{tr}\left[Y^{\top} \Psi\left(I_{n}+\frac{\beta \sigma_{d}^{2}}{n_{d-1}} \Psi^{\top} \Psi\right)^{-1} \Psi^{\top} Y\right]-\frac{1}{2} \beta \operatorname{tr}\left(Y^{\top} Y\right)\right)
\end{aligned}
$$

where we abbreviate $\boldsymbol{\psi}_{\mu} \equiv \boldsymbol{\psi}\left(\mathbf{x}_{\mu} ; \mathcal{W}\right)$ and introduce the matrices $\Psi_{\mu j} \equiv \psi_{\mu, j}$ and $Y_{\mu j} \equiv y_{\mu, j}$. Here, we have used the fact that the matrix $I_{n}+\left(\beta \sigma_{d}^{2} / n_{d-1}\right) \Psi^{\top} \Psi$ is invertible at any finite temperature. By the Weinstein-Aronszajn identity [27],

$$
\operatorname{det}\left(I_{n}+\frac{\beta \sigma_{d}^{2}}{n_{d-1}} \Psi^{\top} \Psi\right)=\operatorname{det}\left(I_{p}+\frac{\beta \sigma_{d}^{2}}{n_{d-1}} \Psi \Psi^{\top}\right)=\operatorname{det}\left(I_{p}+\beta \sigma_{d}^{2} K\right)
$$

where we introduce the (non-constant) kernel matrix

$$
K=K^{(d-1)} \equiv \frac{1}{n_{d-1}} \Psi \Psi^{\top}
$$

as mentioned above, we abbreviate $K \equiv K^{(d-1)}$ for brevity. By the push-through identity [27],

$$
\frac{1}{n_{d-1}} \Psi\left(I_{n}+\frac{\beta \sigma_{d}^{2}}{n_{d-1}} \Psi^{\top} \Psi\right)^{-1} \Psi^{\top}=\left(I_{p}+\frac{\beta \sigma_{d}^{2}}{n_{d-1}} \Psi \Psi^{\top}\right)^{-1} \frac{1}{n_{d-1}} \Psi \Psi^{\top}=\left(I_{p}+\beta \sigma_{d}^{2} K\right)^{-1} K
$$

hence, using the cyclic property of the trace,

$$
\begin{aligned}
& \frac{1}{2} \frac{\beta^{2} \sigma_{d}^{2}}{n_{d-1}} \operatorname{tr}\left[Y^{\top} \Psi\left(I_{n}+\frac{\beta \sigma_{d}^{2}}{n_{d-1}} \Psi^{\top} \Psi\right)^{-1} \Psi^{\top} Y\right]-\frac{1}{2} \beta \operatorname{tr}\left(Y^{\top} Y\right) \\
& \quad=\frac{1}{2} \beta n_{d} \operatorname{tr}\left[\left(\beta \sigma_{d}^{2}\left(I_{p}+\beta \sigma_{d}^{2} K\right)^{-1} K-I_{p}\right) G_{y y}\right] \\
& \quad=-\frac{1}{2} \beta n_{d} \operatorname{tr}\left[\left(I_{p}+\beta \sigma_{d}^{2} K\right)^{-1} G_{y y}\right]
\end{aligned}
$$

where we have defined the normalized Gram matrix of the outputs

$$
G_{y y} \equiv \frac{1}{n_{d}} Y Y^{\top}
$$

and noticed that

$$
I_{p}-\beta \sigma_{d}^{2}\left(I_{p}+\beta \sigma_{d}^{2} K\right)^{-1} K=\left(I_{p}+\beta \sigma_{d}^{2} K\right)^{-1}
$$

Therefore, we conclude that

$$
Z=\mathbb{E}_{\mathcal{W}} \exp \left[\operatorname{tr}\left(J^{\top} O\right)-\frac{n_{d}}{2}\left(\beta \operatorname{tr}\left[\left(I_{p}+\beta \sigma_{d}^{2} K\right)^{-1} G_{y y}\right]+\log \operatorname{det}\left(I_{p}+\beta \sigma_{d}^{2} K\right)\right)\right]
$$

at any width.

# B. 2 Perturbative expansion 

We now consider how this expression behaves in the large-width limit. We assume that this limit is well-defined in the sense that the readout kernel $K$ tends in probability to the constant GP kernel $K_{\infty}$ [5-8], and that the observable $O$ similarly tends to a deterministic limit $O_{\infty}$. Then, we formally write $K$ and $O$ as their infinite-width limits plus corrections which are small at large hidden layer widths:

$$
\begin{aligned}
K & =K_{\infty}+\lambda \delta K \\
O & =O_{\infty}+\lambda \delta O
\end{aligned}
$$

where the parameter $\lambda$ is used to track powers of the small deviations.
We first expand the term resulting from integrating out the readout layer into its infinite-width limit and a finite-width correction. We define the constant matrix

$$
\Gamma \equiv K_{\infty}+\frac{1}{\beta \sigma_{d}^{2}} I_{p}
$$

which is invertible at any finite temperature. Then, by the Woodbury identity [27], we have,

$$
\beta \sigma_{d}^{2}\left(I_{p}+\beta \sigma_{d}^{2} K\right)^{-1}=(\Gamma+\lambda \delta K)^{-1}=\Gamma^{-1}-\lambda \Gamma^{-1} \delta K(\Gamma+\lambda \delta K)^{-1}
$$

and, similarly,

$$
\log \operatorname{det}\left(I_{p}+\beta \sigma_{d}^{2} K\right)=\log \operatorname{det}\left(\beta \sigma_{d}^{2} \Gamma\right)+\log \operatorname{det}\left(I_{p}+\lambda \Gamma^{-1} \delta K\right)
$$

Noting that that both $\lambda \Gamma^{-1} \delta K(\Gamma+\lambda \delta K)^{-1}$ and $\log \operatorname{det}\left(I_{p}+\lambda \Gamma^{-1} \delta K\right)$ are $\mathcal{O}(\lambda)$, we expand the logarithm of the partition function as

$$
\log Z=\log Z_{\infty}+\operatorname{tr}\left(J^{\top} O_{\infty}\right)+\log \mathbb{E}_{\mathcal{W}} \exp \left[\lambda \operatorname{tr}\left(J^{\top} \delta O\right)+\lambda \Omega\right]
$$

where

$$
Z_{\infty} \equiv \operatorname{det}\left(\beta \sigma_{d}^{2} \Gamma\right)^{-n_{d} / 2} \exp \left(-\frac{1}{2} n_{d} \sigma_{d}^{-2} \operatorname{tr}\left(\Gamma^{-1} G_{y y}\right)\right)
$$

is the GP partition function and

$$
\Omega \equiv \frac{1}{2} n_{d} \operatorname{tr}\left[\sigma_{d}^{-2} \Gamma^{-1} \delta K(\Gamma+\lambda \delta K)^{-1} G_{y y}\right]-\frac{1}{2} n_{d} \lambda^{-1} \log \operatorname{det}\left(I_{p}+\lambda \Gamma^{-1} \delta K\right)
$$

is the remainder. $\log \mathbb{E}_{\mathcal{W}} \exp \left[\lambda \operatorname{tr}\left(J^{\top} \delta O\right)+\lambda \Omega\right]$ has the form of a cumulant generating function, hence it has a formal series expansion in $\lambda$ given by

$$
\begin{aligned}
\log \mathbb{E}_{\mathcal{W}} \exp \left[\lambda \operatorname{tr}\left(J^{\top} \delta O\right)+\lambda \Omega\right]= & \lambda \mathbb{E}_{\mathcal{W}}\left[\operatorname{tr}\left(J^{\top} \delta O\right)+\Omega\right] \\
& +\frac{1}{2} \lambda^{2} \mathbb{E}_{\mathcal{W}}\left\{\operatorname{tr}\left[J^{\top}\left(\delta O-\mathbb{E}_{\mathcal{W}} \delta O\right)\right]+\Omega-\mathbb{E}_{\mathcal{W}} \Omega\right]\right\}^{2} \\
& +\frac{1}{6} \lambda^{3} \mathbb{E}_{\mathcal{W}}\left\{\operatorname{tr}\left[J^{\top}\left(\delta O-\mathbb{E}_{\mathcal{W}} \delta O\right)\right]+\Omega-\mathbb{E}_{\mathcal{W}} \Omega\right]\right\}^{3} \\
& +\mathcal{O}\left(\lambda^{4}\right)
\end{aligned}
$$

We can then see that the $k$-th cumulant is $\mathcal{O}\left(J^{k}\right)$, hence the $k$-th posterior cumulant of $O$ will be $\mathcal{O}\left(\lambda^{k}\right)$. Specifically, we can read off the posterior mean

$$
\langle O\rangle=O_{\infty}+\lambda \mathbb{E}_{\mathcal{W}} \delta O+\lambda^{2} \mathbb{K}_{\mathcal{W}}(\delta O, \Omega)+\frac{1}{2} \lambda^{3} \mathbb{K}_{\mathcal{W}}(\delta O, \Omega, \Omega)+\mathcal{O}\left(\lambda^{4}\right)
$$

and covariance

$$
\operatorname{cov}\left(O_{\rho \gamma}, O_{\omega \chi}\right)=\lambda^{2} \mathbb{K}_{\mathcal{W}}\left(\delta O_{\rho \gamma}, \delta O_{\omega \chi}\right)+\lambda^{3} \mathbb{K}_{\mathcal{W}}\left(\delta O_{\rho \gamma}, \delta O_{\omega \chi}, \Omega\right)+\mathcal{O}\left(\lambda^{4}\right)
$$

To make further progress, we expand $\Omega$ in powers of $\lambda$. Using the Neumann series for the matrix inverse (see Appendix A), we have

$$
(\Gamma+\lambda \delta K)^{-1}=\Gamma^{-1}-\lambda \Gamma^{-1} \delta K \Gamma^{-1}+\mathcal{O}\left(\lambda^{2}\right)
$$

and, using the series expansion of the log-determinant near the identity (see Appendix A), we have

$$
\lambda^{-1} \log \operatorname{det}\left(I_{p}+\lambda \Gamma^{-1} \delta K\right)=\operatorname{tr}\left(\Gamma^{-1} \delta K\right)-\frac{1}{2} \lambda \operatorname{tr}\left(\Gamma^{-1} \delta K \Gamma^{-1} \delta K\right)+\mathcal{O}\left(\lambda^{2}\right)
$$

This yields

$$
\begin{aligned}
\Omega= & \frac{n_{d}}{2} \operatorname{tr}\left[\left(\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right) \delta K\right] \\
& -\frac{n_{d}}{2} \lambda \operatorname{tr}\left[\left(\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\frac{1}{2} \Gamma^{-1}\right) \delta K \Gamma^{-1} \delta K\right] \\
& +\mathcal{O}\left(\lambda^{2}\right)
\end{aligned}
$$

The leading term is simple because it is linear in $\delta K$. Then, keeping only the leading non-trivial corrections and recognizing that

$$
\begin{aligned}
O_{\infty}+\lambda \mathbb{E}_{\mathcal{W}} \delta O & =\mathbb{E}_{\mathcal{W}} O \\
\lambda^{2} \mathbb{K}_{\mathcal{W}}\left(\delta O, \delta K_{\mu \nu}\right) & =\mathbb{K}_{\mathcal{W}}\left(O, K_{\mu \nu}\right) \\
\lambda^{2} \mathbb{K}_{\mathcal{W}}\left(\delta O_{\rho \gamma}, \delta O_{\omega \chi}\right) & =\mathbb{K}_{\mathcal{W}}\left(O_{\rho \gamma}, O_{\omega \chi}\right), \quad \text { and } \\
\lambda^{3} \mathbb{K}_{\mathcal{W}}\left(\delta O_{\rho \gamma}, \delta O_{\omega \chi}, \delta K_{\mu \nu}\right) & =\mathbb{K}_{\mathcal{W}}\left(O_{\rho \gamma}, O_{\omega \chi}, K_{\mu \nu}\right)
\end{aligned}
$$

we have

$$
\langle O\rangle=\mathbb{E}_{\mathcal{W}} O+\frac{1}{2} n_{d} \sum_{\mu, \nu=1}^{p}\left(\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right)_{\mu \nu} \mathbb{K}_{\mathcal{W}}\left(O, K_{\mu \nu}\right)+\mathcal{O}\left(\lambda^{3}\right)
$$

and

$$
\begin{aligned}
\operatorname{cov}\left(O_{\rho \gamma}, O_{\omega \chi}\right)= & \mathbb{K}_{\mathcal{W}}\left(O_{\rho \gamma}, O_{\omega \chi}\right) \\
& +\frac{1}{2} n_{d} \sum_{\mu, \nu=1}^{p}\left(\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right)_{\mu \nu} \mathbb{K}_{\mathcal{W}}\left(O_{\rho \gamma}, O_{\omega \chi}, K_{\mu \nu}\right) \\
& +\mathcal{O}\left(\lambda^{4}\right)
\end{aligned}
$$

Restoring the layer indices to $K=K^{(d-1)}$, the above result for $\langle O\rangle$ yields the expression (5) given in the main text. From the structure of these expressions, we can see that higher-order terms (in $\lambda$ ) will involve higher joint cumulants of the kernel deviations $\delta K^{(\ell)}$, which can in turn be converted into joint cumulants of the kernels $K^{(\ell)}$. Therefore, to show that the perturbative expansion yields a valid asymptotic series, one would need to show that these joint cumulants themselves have asymptotic series expansions at large width, with leading terms that are successively suppressed by powers of $n^{-1}$.

# C Explicit covariance computations in deep linear networks 

In this appendix, we detail how to compute the prior covariances appearing in (5) for the hidden layer kernels of deep linear fully-connected and convolutional networks.

## C. 1 Fully-connected linear networks

In this brief subsection, we provide a self-contained derivation of the behavior of the prior cumulants of the kernels of a deep fully-connected linear network with no bias terms. This is a special case of Yaida [12]'s results, and provides some intuition for his results on general MLPs. As in the main text, we consider a network with activations $\mathbf{h}^{(\ell)} \in \mathbb{R}^{n_{\ell}}$ recursively defined as

$$
\mathbf{h}^{(\ell)}=n_{\ell-1}^{-1 / 2} W^{(\ell)} \mathbf{h}^{(\ell-1)} \quad(\ell=1, \ldots, d)
$$

with base case $\mathbf{h}^{(0)}=\mathbf{x}$. We take the prior distribution over weights to be $\left[W^{(\ell)}\right]_{i j} \sim_{\text {i.i.d. }} \mathcal{N}\left(0, \sigma_{\ell}^{(2)}\right)$, and define the hidden layer kernels $\left[K^{(\ell)}\right]_{\mu \nu} \equiv n_{\ell}^{-1} \mathbf{h}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\nu}^{(\ell)}$ for $\ell=1, \ldots, d-1$. Then, we have

$$
\begin{aligned}
\mathbb{E}_{\mathcal{W}} K_{\mu \nu}^{(\ell)} & =\frac{1}{n_{\ell} \cdots n_{0}} \mathbb{E}_{\mathcal{W}} \mathbf{x}_{\mu}^{\top}\left(W^{(1)}\right)^{\top} \cdots\left(W^{(\ell)}\right)^{\top} W^{(\ell)} \cdots W^{(1)} \mathbf{x}_{\nu} \\
& =\sigma_{1}^{2} \cdots \sigma_{\ell}^{2} \frac{\mathbf{x}_{\mu} \cdot \mathbf{x}_{\nu}}{n_{0}} \\
& =\left[K_{\infty}^{(\ell)}\right]_{\mu \nu}
\end{aligned}
$$

at any width, as $\mathbb{E}_{W^{(\ell)}}\left(W^{(\ell)}\right)^{\top} W^{(\ell)} / n_{\ell}=\sigma_{\ell}^{2} I_{n_{\ell-1}}$. We now consider the second moments of the kernels. We first note that

$$
\mathbb{E}_{\mathcal{W}} K_{\mu \nu}^{(\ell)} K_{\rho \lambda}^{(\ell+\tau)}=\sigma_{\ell+\tau}^{2} \cdots \sigma_{\ell+1}^{2} \mathbb{E}_{\mathcal{W}} K_{\mu \nu}^{(\ell)} K_{\rho \lambda}^{(\ell)}
$$

for any $\tau \geq 1$. By Isserlis' theorem (see Appendix A), we have

$$
\mathbb{E}_{W^{(\ell)}} W_{i k}^{(\ell)} W_{i l}^{(\ell)} W_{j m}^{(\ell)} W_{j r}^{(\ell)}=\sigma_{\ell}^{4} \delta_{i j}\left(\delta_{k m} \delta_{l r}+\delta_{k r} \delta_{l m}\right)+\sigma_{\ell}^{4} \delta_{k l} \delta_{m r}
$$

hence we have the exact recursion

$$
\begin{aligned}
\mathbb{E}_{\mathcal{W}} K_{\mu \nu}^{(\ell)} K_{\rho \lambda}^{(\ell)}= & \frac{1}{\left(n_{\ell} \cdots n_{0}\right)^{2}} \mathbb{E}_{\mathcal{W}} \sum_{i, j=1}^{n_{\ell}} \sum_{k, l, m, r=1}^{n_{\ell-1}} W_{i k}^{(\ell)} W_{i l}^{(\ell)} W_{j m}^{(\ell)} W_{j r}^{(\ell)} \\
& \times\left[W^{(\ell-1)} \cdots W^{(1)} \mathbf{x}_{\rho}\right]_{k}\left[W^{(\ell-1)} \cdots W^{(1)} \mathbf{x}_{\nu}\right]_{l} \\
& \times\left[W^{(\ell-1)} \cdots W^{(1)} \mathbf{x}_{\rho}\right]_{m}\left[W^{(\ell-1)} \cdots W^{(1)} \mathbf{x}_{\lambda}\right]_{r} \\
= & \sigma_{\ell}^{4} \mathbb{E}_{\mathcal{W}} K_{\mu \nu}^{(\ell-1)} K_{\rho \lambda}^{(\ell-1)}+\frac{1}{n_{\ell}} \sigma_{\ell}^{4}\left(\mathbb{E}_{\mathcal{W}} K_{\mu \rho}^{(\ell-1)} K_{\nu \lambda}^{(\ell-1)}+\mathbb{E}_{\mathcal{W}} K_{\mu \lambda}^{(\ell-1)} K_{\nu \rho}^{(\ell-1)}\right)
\end{aligned}
$$

with base case

$$
\begin{aligned}
\mathbb{E}_{\mathcal{W}} K_{\mu \nu}^{(1)} K_{\rho \lambda}^{(1)} & =\frac{1}{\left(n_{1} n_{0}\right)^{2}} \sum_{i, j=1}^{n_{1}} \sum_{k, l, m, r=1}^{n_{0}} \mathbb{E}_{\mathcal{W}} W_{i k}^{(1)} W_{i l}^{(1)} W_{j m}^{(1)} W_{j r}^{(1)} x_{\rho, k} x_{\nu, l} x_{\rho, m} x_{\lambda, r} \\
& =\sigma_{1}^{4} \frac{\mathbf{x}_{\mu} \cdot \mathbf{x}_{\nu}}{n_{0}} \frac{\mathbf{x}_{\rho} \cdot \mathbf{x}_{\lambda}}{n_{0}}+\frac{1}{n_{1}} \sigma_{1}^{4}\left(\frac{\mathbf{x}_{\mu} \cdot \mathbf{x}_{\rho}}{n_{0}} \frac{\mathbf{x}_{\nu} \cdot \mathbf{x}_{\lambda}}{n_{0}}+\frac{\mathbf{x}_{\mu} \cdot \mathbf{x}_{\lambda}}{n_{0}} \frac{\mathbf{x}_{\nu} \cdot \mathbf{x}_{\rho}}{n_{0}}\right) \\
& =\left[K_{\infty}^{(1)}\right]_{\mu \nu}\left[K_{\infty}^{(1)}\right]_{\rho \lambda}+\frac{1}{n_{1}}\left(\left[K_{\infty}^{(1)}\right]_{\mu \rho}\left[K_{\infty}^{(1)}\right]_{\nu \lambda}+\left[K_{\infty}^{(1)}\right]_{\mu \lambda}\left[K_{\infty}^{(1)}\right]_{\nu \rho}\right)
\end{aligned}
$$

for the second moments of the kernels at each layer. This recurrence relation is in principle exactly solvable for any finite width, but we are interested only in its leading-order behavior at large widths. In particular, we can read off that

$$
\begin{aligned}
\operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu}^{(\ell)}, K_{\rho \lambda}^{(\ell+\tau)}\right)= & \sigma_{\ell+\tau}^{2} \cdots \sigma_{\ell+1}^{2}\left(\sum_{\ell^{\prime}=1}^{\ell} \frac{1}{n_{\ell^{\prime}}}\right)\left(\left[K_{\infty}^{(\ell)}\right]_{\mu \rho}\left[K_{\infty}^{(\ell)}\right]_{\nu \lambda}+\left[K_{\infty}^{(\ell)}\right]_{\mu \lambda}\left[K_{\infty}^{(\ell)}\right]_{\nu \rho}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

Moreover, one can see by Isserlis' theorem that the third and higher cumulants will be $\mathcal{O}\left(n^{-2}\right)$. Substituting this result into (5) with the hidden layer kernel as the observable of interest, we obtain the expression (8) given in the main text.

# C. 2 Convolutional linear networks 

In this subsection, we derive the prior cumulants required to compute corrections to the average feature kernels of deep convolutional linear networks. As described in the main text, following the setup of Novak et al. [7] and Xiao et al. [34], we consider a network consisting of $d-1$ linear convolutional layers followed by a fully-connected linear readout layer. For simplicity, we assume circular padding and no internal pooling. As discussed in Novak et al. [7], this setup could be easily extended to other padding strategies, strided convolutions, and average pooling in intermediate layers.

We write the activations at the $\ell$-th hidden layer as $h_{i, \mathfrak{a}}^{(\ell)}$, where $i$ indexes the $n_{\ell}$ channels of the layer and $\mathfrak{a}$ is a $q$-dimensional spatial multi-index. We take the filters to be of size $(2 k+1) \times \cdots \times(2 k+1)$ in all convolutional layers; the extension to differently-sized filters would be straightforward but notationally cumbersome. The ranges of all spatial summations will be implied.
The hidden layer activations are then defined through the recurrence

$$
h_{i, \mathfrak{a}}^{(\ell)}(x)=\frac{1}{\sqrt{n_{\ell-1}}} \sum_{j=1}^{n_{\ell-1}} \sum_{\mathfrak{b}} w_{i j, \mathfrak{b}}^{(\ell)} h_{j, \mathfrak{a}+\mathfrak{b}}^{(\ell-1)}(x)
$$

with base case $h_{i, \mathfrak{a}}^{(0)}(x)=x_{i, \mathfrak{a}}$. We fix the prior distribution of the filter elements to be

$$
w_{i j, \mathfrak{a}}^{(\ell)} \underset{i \epsilon, \mathfrak{a}}{\sim} \mathcal{N}\left(0, \sigma_{\ell}^{2} v_{\mathfrak{a}}\right)
$$

where $v_{\mathfrak{a}}>0$ is a weighting factor that sets the fraction of receptive field variance at location $\mathfrak{a}$ (and is thus subject to the constraint $\sum_{\mathfrak{a}} v_{\mathfrak{a}}=1$ ). For inputs $\left[x_{\mu}\right]_{i, \mathfrak{a}}$ and $\left[x_{\nu}\right]_{i, \mathfrak{a}}$, we introduce the hidden layer kernels

$$
K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)} \equiv \frac{1}{n_{\ell}} \sum_{i=1}^{n_{\ell}} h_{i, \mathfrak{a}}^{(\ell)}\left(x_{\mu}\right) h_{i, \mathfrak{b}}^{(\ell)}\left(x_{\nu}\right)
$$

We will first compute the prior mean and covariance of these four-indexed kernels, and then address how to handle readout across space.
As shown by Xiao et al. [34], the prior mean obeys the recurrence

$$
\begin{aligned}
& \mathbb{E}_{\mathcal{W}} K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)} \\
& \quad=\mathbb{E}_{W^{(1)} \ldots W^{(\ell-1)}} \frac{1}{n_{\ell} n_{\ell-1}} \sum_{i=1}^{n_{\ell}} \sum_{j, j^{\prime}=1}^{n_{\ell-1}} \sum_{\mathfrak{c}, \mathcal{F}} h_{j, \mathfrak{a}+\mathfrak{c}}^{(\ell-1)}\left(x_{\mu}\right) h_{j^{\prime}, \mathfrak{b}+\mathfrak{b}}^{(\ell-1)}\left(x_{\nu}\right) \mathbb{E}_{W^{(\ell)}} w_{i j, \mathfrak{c}}^{(\ell)} w_{i j^{\prime}, \mathfrak{b}}^{(\ell)} \\
& \quad=\sigma_{\ell}^{2} \mathbb{E}_{W^{(1)} \ldots W^{(\ell-1)}} \sum_{\mathfrak{c}} v_{\mathfrak{c}} \frac{1}{n_{\ell-1}} \sum_{j=1}^{n_{\ell-1}} h_{j, \mathfrak{a}+\mathfrak{c}}^{(\ell-1)}\left(x_{\mu}\right) h_{j, \mathfrak{b}+\mathfrak{c}}^{(\ell-1)}\left(x_{\nu}\right) \\
& \quad=\sigma_{\ell}^{2} \sum_{\mathfrak{c}} v_{\mathfrak{c}} \mathbb{E}_{\mathcal{W}} K_{\mu \nu,(\mathfrak{a}+\mathfrak{c})(\mathfrak{b}+\mathfrak{c})}^{(\ell-1)}
\end{aligned}
$$

with base case

$$
\mathbb{E}_{\mathcal{W}} K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(1)}=\sigma_{\mathrm{I}}^{2} \sum_{\mathfrak{c}} v_{\mathfrak{c}}\left[G_{x x}\right]_{\mu \nu,(\mathfrak{a}+\mathfrak{c})(\mathfrak{b}+\mathfrak{c})}
$$

for

$$
\left[G_{x x}\right]_{\mu \nu, \mathfrak{a} \mathfrak{b}} \equiv \frac{1}{n_{0}} \sum_{i=1}^{n_{0}}\left[x_{\mu}\right]_{i, \mathfrak{a}}\left[x_{\nu}\right]_{i, \mathfrak{b}}
$$

This recurrence yields

$$
\mathbb{E}_{\mathcal{W}} K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}=\sigma_{\mathrm{I}}^{2} \cdots \sigma_{\ell}^{2} \sum_{\mathfrak{c}_{1}, \ldots, \mathfrak{c}_{\ell}} v_{\mathfrak{c}_{1}} \cdots v_{\mathfrak{c}_{\ell}}\left[G_{x x}\right]_{\mu \nu,\left(\mathfrak{a}+\mathfrak{c}_{1}+\cdots+\mathfrak{c}_{\ell}\right)\left(\mathfrak{b}+\mathfrak{c}_{1}+\cdots+\mathfrak{c}_{\ell}\right)}
$$

Moreover, as in the fully-connected case considered in the preceding section, we have

$$
\left[K_{\infty}^{(\ell)}\right]_{\mu \nu, \mathfrak{a} \mathfrak{b}}=\mathbb{E}_{\mathcal{W}} K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}
$$

at any width.
We now consider the prior covariance of the kernels of two different hidden layers $\ell$ and $\ell+\tau$. As the weight prior factors across layers, we have

$$
\begin{aligned}
& \mathbb{E}_{\mathcal{W}} K_{\mu \nu, \mathfrak{a b}}^{(\ell)} K_{\rho \lambda, \mathfrak{c} \mathfrak{d}}^{(\ell+\tau)}=\sigma_{\ell+1}^{2} \cdots \sigma_{\ell+\tau}^{2} \sum_{\mathfrak{e}_{1}, \ldots, \mathfrak{e}_{\tau}} v_{\mathfrak{e}_{1}} \cdots v_{\mathfrak{e}_{\tau}} \\
& \times \mathbb{E}_{\mathcal{W}} K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)} K_{\rho \lambda,\left(\mathfrak{c}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{\tau}\right)\left(\mathfrak{d}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{\tau}\right)} .
\end{aligned}
$$

By Isserlis' theorem (see Appendix A),

$$
\begin{aligned}
\mathbb{E}_{W^{(\ell)}} w_{i j, \mathfrak{c}}^{(\ell)} w_{i j^{\prime}, \mathfrak{f}}^{(\ell)} w_{i^{\prime} j^{\prime \prime}, \mathfrak{d}}^{(\ell)} w_{i^{\prime} j^{\prime \prime \prime}, \mathfrak{h}}^{(\ell)}= & \sigma_{\ell}^{4} v_{\mathfrak{c}} v_{\mathfrak{g}} \delta_{j j^{\prime}} \delta_{j^{\prime \prime} j^{\prime \prime \prime}} \delta_{\mathfrak{c} \mathfrak{f}} \delta_{\mathfrak{g} \mathfrak{h}} \\
& +\sigma_{\ell}^{4} v_{\mathfrak{c}} v_{\mathfrak{f}} \delta_{i i^{\prime}} \delta_{j j^{\prime \prime}} \delta_{j^{\prime} j^{\prime \prime \prime}} \delta_{\mathfrak{c} \mathfrak{g}} \delta_{\mathfrak{f} \mathfrak{h}} \\
& +\sigma_{\ell}^{4} v_{\mathfrak{c}} v_{\mathfrak{f}} \delta_{i i^{\prime}} \delta_{j j^{\prime \prime}} \delta_{j^{\prime} j^{\prime \prime}} \delta_{\mathfrak{c} \mathfrak{h}} \delta_{\mathfrak{f} \mathfrak{g}}
\end{aligned}
$$

hence we have the recurrence

$$
\begin{aligned}
& \mathbb{E}_{\mathcal{W}} K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)} K_{\rho \lambda, \mathfrak{c} \mathfrak{d}}^{(\ell)} \\
& =\mathbb{E}_{W^{(1)} \ldots W^{(\ell-1)}} \frac{1}{n_{\ell}^{2} n_{\ell-1}^{2}} \sum_{i, i^{\prime}=1}^{n_{\ell}} \sum_{j, j^{\prime}, j^{\prime \prime}, j^{\prime \prime \prime}=1}^{n_{\ell-1}} \sum_{\mathfrak{c}, \mathfrak{f}, \mathfrak{g}, \mathfrak{h}} \\
& \times h_{j, \mathfrak{a}+\mathfrak{c}}^{(\ell-1)}\left(x_{\rho}\right) h_{j^{\prime}, \mathfrak{b}+\mathfrak{f}}^{(\ell-1)}\left(x_{\nu}\right) h_{j^{\prime \prime}, \mathfrak{c}+\mathfrak{g}}^{(\ell-1)}\left(x_{\rho}\right) h_{j^{\prime \prime \prime}, \mathfrak{d}+\mathfrak{h}}^{(\ell-1)}\left(x_{\lambda}\right) \\
& \times \mathbb{E}_{W^{(\ell)}} w_{i j, \mathfrak{c}}^{(\ell)} w_{i j^{\prime}, \mathfrak{f}}^{(\ell)} w_{i^{\prime} j^{\prime \prime}, \mathfrak{d}}^{(\ell)} w_{i^{\prime} j^{\prime \prime}, \mathfrak{h}}^{(\ell)} \\
& =\sigma_{\ell}^{4} \sum_{\mathfrak{c}, \mathfrak{f}} v_{\mathfrak{c}} v_{\mathfrak{f}}\left[\mathbb{E}_{\mathcal{W}} K_{\mu \nu,(\mathfrak{a}+\mathfrak{c})(\mathfrak{b}+\mathfrak{c})}^{(\ell-1)} K_{\rho \lambda,(\mathfrak{c}+\mathfrak{f})(\mathfrak{d}+\mathfrak{f})}^{(\ell-1)}\right. \\
& +\frac{1}{n_{\ell}} \mathbb{E}_{\mathcal{W}} K_{\mu \rho,(\mathfrak{a}+\mathfrak{c})(\mathfrak{c}+\mathfrak{c})}^{(\ell-1)} K_{\nu \lambda,(\mathfrak{b}+\mathfrak{f})(\mathfrak{d}+\mathfrak{f})}^{(\ell-1)} \\
& \left.+\frac{1}{n_{\ell}} \mathbb{E}_{\mathcal{W}} K_{\mu \lambda,(\mathfrak{a}+\mathfrak{c})(\mathfrak{d}+\mathfrak{c})}^{(\ell-1)} K_{\nu \rho,(\mathfrak{a}+\mathfrak{f})(\mathfrak{c}+\mathfrak{f})}^{(\ell-1)}\right]
\end{aligned}
$$

with base case

$$
\begin{aligned}
& \mathbb{E}_{\mathcal{W}} K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(1)} K_{\rho \lambda, \mathfrak{c} \mathfrak{d}}^{(\ell)}=\sigma_{1}^{4} \sum_{\mathfrak{c}, \mathfrak{f}} v_{\mathfrak{c}} v_{\mathfrak{f}}\left[\left[G_{x x}\right]_{\mu \nu,(\mathfrak{a}+\mathfrak{c})(\mathfrak{b}+\mathfrak{c})}\left[G_{x x}\right]_{\rho \lambda,(\mathfrak{c}+\mathfrak{f})(\mathfrak{d}+\mathfrak{f})}\right. \\
&+\frac{1}{n_{\ell}}\left[G_{x x}\right]_{\mu \rho,(\mathfrak{a}+\mathfrak{c})(\mathfrak{c}+\mathfrak{c})}\left[G_{x x}\right]_{\nu \lambda,(\mathfrak{b}+\mathfrak{f})(\mathfrak{d}+\mathfrak{f})} \\
& \left.+\frac{1}{n_{\ell}}\left[G_{x x}\right]_{\mu \lambda,(\mathfrak{a}+\mathfrak{c})(\mathfrak{d}+\mathfrak{c})}\left[G_{x x}\right]_{\nu \rho,(\mathfrak{a}+\mathfrak{f})(\mathfrak{c}+\mathfrak{f})}\right] \\
&=\left[K_{\infty}^{(1)}\right]_{\mu \nu, \mathfrak{a} \mathfrak{b}}\left[K_{\infty}^{(1)}\right]_{\rho \lambda, \mathfrak{c} \mathfrak{d}} \\
&+\frac{1}{n_{\ell}}\left[\left[K_{\infty}^{(1)}\right]_{\mu \rho, \mathfrak{a} \mathfrak{c}}\left[K_{\infty}^{(1)}\right]_{\nu \lambda, \mathfrak{b} \mathfrak{d}}+\left[K_{\infty}^{(1)}\right]_{\mu \lambda, \mathfrak{a} \mathfrak{d}}\left[K_{\infty}^{(1)}\right]_{\nu \rho, \mathfrak{b} \mathfrak{c}}\right]
\end{aligned}
$$

for the second prior moments of the kernels. As in the fully-connected case, these recurrence relations could in principle be solved exactly, but we are only interested in their large-width behavior. Using the forward recurrence for the GP kernels, we can easily read off that

$$
\begin{aligned}
\operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda, \mathfrak{c} \mathfrak{d}}^{(\ell)}\right)= & \left(\sum_{\ell^{\prime}=1}^{\ell} \frac{1}{n_{\ell^{\prime}}}\right)\left(\left[K_{\infty}^{(\ell)}\right]_{\mu \rho, \mathfrak{a} \mathfrak{c}}\left[K_{\infty}^{(\ell)}\right]_{\nu \lambda, \mathfrak{b} \mathfrak{d}}+\left[K_{\infty}^{(\ell)}\right]_{\mu \lambda, \mathfrak{a} \mathfrak{d}}\left[K_{\infty}^{(\ell)}\right]_{\nu \rho, \mathfrak{b} \mathfrak{c}}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

which can then be substituted into the desired cross-layer covariance:

$$
\begin{aligned}
& \operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda, \mathfrak{c} \mathfrak{d}}^{(\ell+\tau)}\right)=\sigma_{\ell+1}^{2} \cdots \sigma_{\ell+\tau}^{2} \sum_{\mathfrak{e}_{1}, \ldots, \mathfrak{e}_{\tau}} v_{\mathfrak{e}_{1}} \cdots v_{\mathfrak{e}_{\tau}} \\
& \times \operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda,\left(\mathfrak{c}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{\tau}\right)\left(\mathfrak{d}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{\tau}\right)}^{(\ell-\ell+\cdots+\epsilon_{\tau})}\right) .
\end{aligned}
$$

We now address the question of how to read out the convolutional layer activities across space. Following Novak et al. [7], we consider two strategies: vectorization and projection. With vectorization, the output of the final convolutional layer is flattened into a $n_{d-1} s$-dimensional vector before readout, i.e., $\psi_{i+s(\mathfrak{a}-1)}(x)=h_{i, \mathfrak{a}}^{(d-1)}(x)$ or $\psi_{n_{d}(i-1)+\mathfrak{a}}(x)=h_{i, \mathfrak{a}}^{(d-1)}(x)$. The two-index feature map kernel appearing in Conjecture 1 is then related to the four-index convolutional hidden layer kernel analyzed above via

$$
K_{\mu \nu}^{(d-1)}=\frac{1}{s} \sum_{\mathfrak{a}} K_{\mu \nu, \mathfrak{a} \mathfrak{a}}^{(d-1)}
$$

With projection, the feature map is formed by contracting the final convolutional layer with a fixed vector $\mathbf{u}$, i.e.,

$$
\psi_{i}(x)=\sum_{\mathfrak{a}} u_{\mathfrak{a}} h_{i, \mathfrak{a}}^{(d-1)}(x)
$$

The feature map kernel is then given as

$$
K_{\mu \nu}^{(d-1)}=\sum_{\mathfrak{a}, \mathfrak{b}} u_{\mathfrak{a}} u_{\mathfrak{b}} K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(d-1)}
$$

Examples of common projection readout strategies include global average pooling ( $u_{\mathfrak{a}}=1 / s$ ) and single-pixel subsampling ( $u_{\mathfrak{a}}=\delta_{\mathfrak{a} \mathfrak{c}}$ for some desired location $\mathfrak{c}$ ). These readout approaches endow the network with differing properties under spatial transformations; global average pooling has the particular property of making the output translation-invariant.
We now seek to simplify the resulting expression for the leading-order correction to the posterior mean of some four-index feature kernel $K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}$. Per Conjecture 1, the general form of this correction is

$$
\frac{1}{2} n_{d} \sum_{\rho, \lambda=1}^{p} \Phi_{\rho \lambda} \operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda}^{(d-1)}\right)
$$

where we have defined $\Phi_{\rho \lambda}=\left[\sigma_{\beta}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right]_{\rho \lambda}$ for notational convenience. As elsewhere, $\Gamma \equiv K_{\infty}^{(d-1)}+\beta^{-1} \sigma_{\beta}^{-2} I_{p}$ for $K_{\infty}^{(d-1)}$ the two-index kernel determined by the chosen readout strategy. Depending on the chosen readout strategy, this general expression can be simplified dramatically. In particular, for vectorization or global average pooling, the correction does not depend on the particular form of $v_{\mathfrak{a}}$.
To show this for vectorization (the strategy used in our experiments), we substitute the definition of $K_{\infty}^{(d-1)}$ from (C.31) and the expression for the cross-layer kernel covariance from (C.30) into the general expression for the correction to obtain

$$
\begin{aligned}
& \frac{n_{d}}{2 s} \sigma_{\ell+1}^{2} \cdots \sigma_{d-1}^{2} \\
& \times \sum_{\rho, \lambda} \Phi_{\rho \lambda} \sum_{\mathfrak{e}_{1}, \cdots, \mathfrak{e}_{d-\ell-1}} v_{\mathfrak{e}_{1}} \cdots v_{\mathfrak{e}_{d-\ell-1}} \sum_{\mathfrak{c}} \operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda,\left(\mathfrak{c}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{d-\ell-1}\right)\left(\mathfrak{c}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{d-\ell-1}\right)}^{(\ell)}\right)
\end{aligned}
$$

Thanks to the periodic boundary conditions, the summation over $\mathfrak{c}$ is independent of the index shift $\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{d-\ell-1}$. Then, the sums over $\mathfrak{e}_{1}, \cdots, \mathfrak{e}_{d-\ell-1}$ factor, yielding

$$
\frac{n_{d}}{2 s} \sigma_{\ell+1}^{2} \cdots \sigma_{d-1}^{2} \sum_{\rho, \lambda=1}^{p} \Phi_{\rho \lambda} \sum_{\mathfrak{c}} \operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda, \mathfrak{c} \mathfrak{c}}^{(\ell)}\right)
$$

thanks to the normalization constraint $\sum_{\mathfrak{c}} v_{\mathfrak{c}}=1$. We now notice that $\Phi_{\rho \lambda}$ is a symmetric matrix, and that the kernel remains invariant under the simultaneous exchange of indices $\rho \leftrightarrow \lambda$ and $\mathfrak{c} \leftrightarrow \mathfrak{d}$. Then, substituting in the expression for the same-layer kernel covariance (C.29), it is easy to show that the correction reduces to

$$
\sigma_{\ell+1}^{2} \cdots \sigma_{d-1}^{2}\left(\sum_{\ell^{\prime}=1}^{\ell} \frac{n_{d}}{n_{\ell^{\prime}}}\right) \frac{1}{s} \sum_{\mathfrak{c}} \sum_{\rho, \lambda=1}^{p}\left[K_{\infty}^{(\ell)}\right]_{\mu \rho, \mathfrak{a} \mathfrak{c}} \Phi_{\rho \lambda}\left[K_{\infty}^{(\ell)}\right]_{\lambda \nu, \mathfrak{c} \mathfrak{b}}
$$

This yields the expression given in the main text.
For projection, an analogous simplification is possible in the case of global average pooling ( $u_{\mathrm{a}}=$ $1 / s)$. Substituting the definition of $K_{\infty}^{(d-1)}$ from (C.33) and expression for the cross-layer kernel covariance (C.30) into the correction, we have

$$
\frac{n_{d}}{2 s^{2}} \sigma_{\ell+1}^{2} \cdots \sigma_{d-1}^{2} \sum_{\rho, \lambda=1}^{p} \Phi_{\rho \lambda} \sum_{\mathfrak{c}, \mathfrak{d}} \operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda, \mathfrak{c} \mathfrak{d}}^{(\ell)}\right)
$$

Substituting in the expression for the same-layer kernel covariance (C.29), it is again easy to show that the correction reduces to

$$
\sigma_{\ell+1}^{2} \cdots \sigma_{d-1}^{2}\left(\sum_{\ell^{\prime}=1}^{\ell} \frac{n_{d}}{n_{\ell^{\prime}}}\right) \frac{1}{s^{2}} \sum_{\mathfrak{c}, \mathfrak{d}} \sum_{\rho, \lambda=1}^{p}\left[K_{\infty}^{(\ell)}\right]_{\mu \rho, \mathfrak{a} \mathfrak{c}} \Phi_{\rho \lambda}\left[K_{\infty}^{(\ell)}\right]_{\lambda \nu, \mathfrak{d} \mathfrak{b}}
$$

For projection strategies other than global average pooling (more precisely, for strategies for which $u_{\mathrm{a}}$ is not constant), the sum over indices in the cross-layer covariance is not independent of the shift, hence we cannot simplify the correction in a similar fashion. This can be seen explicitly when treating the case of single-pixel subsampling ( $u_{\mathrm{a}}=\delta_{\mathrm{a} \mathfrak{c}}$ for some desired location $\mathfrak{c}$ ). In this case, the correction reduces to

$$
\begin{aligned}
& \frac{n_{d}}{2} \sigma_{\ell+1}^{2} \cdots \sigma_{d-1}^{2} \\
& \times \sum_{\rho, \lambda} \Phi_{\rho \lambda} \sum_{\mathfrak{e}_{1}, \cdots, \mathfrak{e}_{d-\ell-1}} v_{\mathfrak{e}_{1}} \cdots v_{\mathfrak{e}_{d-\ell-1}} \operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda,\left(\mathfrak{c}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{d-\ell-1}\right)\left(\mathfrak{c}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{d-\ell-1}\right)}^{(\ell-1)} .
\end{aligned}
$$

Unlike for vectorization or for projection using global average pooling, this expression is manifestly dependent on the form of $v_{\mathrm{a}}$.
Naïvely, the computation of the corrections to the linear convolutional kernels requires the computation of $\operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu, \mathfrak{a} \mathfrak{b}}^{(\ell)}, K_{\rho \lambda,\left(\mathfrak{c}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{d-\ell-1}\right)\left(\mathfrak{d}+\mathfrak{e}_{1}+\cdots+\mathfrak{e}_{d-\ell-1}\right)}^{(\ell)}\right)$ for each index, which takes impractical amounts of compute time and storage. We only found it practical to compute the theoretical kernels in the special cases presented above.

# D Direct computation of the average hidden layer kernels of a deep linear MLP 

In this appendix, we provide a self-contained derivation of the average hidden layer kernels of a deep linear fully-connected network (MLP). This derivation relies upon neither the results of Appendices B and C nor those of Yaida [12].

## D. 1 The cumulant generating function of learned features for a MLP

In this section, we briefly describe the full partition function of the Bayes posterior for a general fully connected network, or multi-layer perceptron (MLP), with no bias terms. An MLP $\mathbf{f}: \mathbb{R}^{n_{0}} \rightarrow \mathbb{R}^{n_{d}}$ with $d$ layers, no biases, and parameters $\Theta=\left\{W^{(\ell)}\right\}_{\ell=1}^{d}$ can be defined recursively in terms of its layer-wise preactivations $\mathbf{h}^{(\ell)} \in \mathbb{R}^{n_{\ell}}$ as

$$
\begin{aligned}
\mathbf{h}^{(0)} & =\mathbf{x} \\
\mathbf{h}^{(\ell)} & =\frac{1}{\sqrt{n_{\ell-1}}} W^{(\ell)} \phi_{\ell-1}\left(\mathbf{h}^{(\ell-1)}\right) \quad(\ell=1, \ldots, d) \\
\mathbf{f} & =\phi_{d}\left(\mathbf{h}^{(d)}\right)
\end{aligned}
$$

where the activation functions $\phi_{\ell}$ act elementwise. As always, we focus on networks with linear readout, i.e., $\phi_{d}(x)=x$, and assume Gaussian priors over the weights:

$$
W_{\mathrm{ij}}^{(\ell)} \underset{\text { i.i.d. }}{\sim} \mathcal{N}\left(0, \sigma_{\ell}^{2}\right)
$$

We enforce the definition of the network architecture via Fourier representations of the Dirac distribution, with $\mathbf{q}_{\mu}^{(\ell)}$ being the Lagrange multiplier that enforces the definition of the preactivation $\mathbf{h}_{\mu}^{(\ell)}$. Then, after integrating out the weights using the fact that the relevant integrals are Gaussian, this allows us to write the partition function as

$$
Z=\int \prod_{\mu=1}^{p} \prod_{\ell=1}^{d} \frac{d \mathbf{h}_{\mu}^{(\ell)} d \mathbf{q}_{\mu}^{(\ell)}}{(2 \pi)^{n_{\ell}}} \exp \left[S\left(\left\{\mathbf{h}_{\mu}^{(\ell)}\right\},\left\{\mathbf{q}_{\mu}^{(\ell)}\right\}\right)\right]
$$

where the "effective action" for the preactivations and Lagrange multipliers is

$$
\begin{aligned}
S= & -\frac{1}{2} \beta \sum_{\mu=1}^{p}\left\|\mathbf{h}_{\mu}^{(d)}-\mathbf{y}_{\mu}\right\|^{2}+\sum_{\ell=1}^{d} \sum_{\mu=1}^{p} i \mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\mu}^{(\ell)} \\
& -\frac{1}{2} \sum_{\ell=1}^{d} \frac{\sigma_{\ell}^{2}}{n_{\ell-1}} \sum_{\mu, \nu=1}^{p} \mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{q}_{\nu}^{(\ell)} \phi_{\ell-1}\left(\mathbf{h}_{\mu}^{(\ell-1)}\right) \cdot \phi_{\ell-1}\left(\mathbf{h}_{\nu}^{(\ell-1)}\right)
\end{aligned}
$$

As described in Appendix B, source terms can be added to the effective action to allow computation of various averages. For deep linear networks, it is convenient to scale the source terms by an overall factor of $-1 / 2$, for which we must correct when computing the averages:

$$
S_{\mathrm{J}}=-\frac{1}{2} \sum_{\ell=1}^{d-1} \sum_{\mu, \nu=1}^{p} J_{\mu \nu}^{(\ell)} \phi_{\ell}\left(\mathbf{h}_{\mu}^{(\ell)}\right) \cdot \phi_{\ell}\left(\mathbf{h}_{\nu}^{(\ell)}\right)
$$

For an MLP, our task is therefore to integrate out the preactivations and corresponding Lagrange multipliers. We will do so sequentially from the first layer to the last, keeping terms up to the desired order at each step, akin to the approach of Yaida [12]. So long as $n_{d}$ and $d$ are fixed and small relative to the width of the hidden layers, this is a consistent perturbative approach, as noted by Yaida [12].

# D. 2 General form of the perturbative layer integrals for a deep linear network 

In this section, we evaluate the general form of the integrals required to perturbatively marginalize out a given layer of a deep linear network to $\mathcal{O}\left(n^{-1}\right)$. These integrals are generically of the form

$$
\begin{aligned}
I=\int \prod_{\mu=1}^{p} \frac{d \mathbf{h}_{\mu} d \mathbf{q}_{\mu}}{(2 \pi)^{n_{2}}} \exp \left(\sum_{\mu=1}^{p} i \mathbf{q}_{\mu} \cdot \mathbf{h}_{\mu}-\frac{1}{2} \sum_{\mu, \nu=1}^{p} G_{\mu \nu}\left(\mathbf{q}_{\mu} \cdot \mathbf{q}_{\nu}\right)+\sum_{\mu=1}^{p} \mathbf{j}_{\mu} \cdot \mathbf{h}_{\mu}\right. \\
& -\frac{1}{2} \frac{1}{n_{2}} \sum_{\mu, \nu=1}^{p} A_{\mu \nu}\left(\mathbf{h}_{\mu} \cdot \mathbf{h}_{\nu}\right) \\
& +\frac{1}{4} \frac{g}{n_{1}} \sum_{\mu, \nu, \rho, \lambda=1}^{p} G_{\mu \nu}\left(\mathbf{q}_{\nu} \cdot \mathbf{q}_{\rho}\right) G_{\rho \lambda}\left(\mathbf{q}_{\lambda} \cdot \mathbf{q}_{\mu}\right) \\
& \left.+\frac{1}{2} \frac{1}{n_{1}} \sum_{\mu, \nu=1}^{p} B_{\mu \nu}\left(\mathbf{q}_{\mu} \cdot \mathbf{q}_{\nu}\right)\right)
\end{aligned}
$$

where $\mathbf{h}_{\mu}, \mathbf{q}_{\mu} \in \mathbb{R}^{n_{2}}$. Here, $G$ is a positive semidefinite matrix, while $A$ and $B$ are symmetric matrices that need not be positive semidefinite. Furthermore, $\mathbf{j}_{\mu}$ is some source, while $g$ is a coupling constant. We will first evaluate this integral up to terms of $\mathcal{O}\left(n_{1}^{-1}\right)$ for $n_{1} \gg 1$, assuming that $G, A, B, \mathbf{j}_{\mu}$, and $g$ are $\mathcal{O}(1)$ functions of $n_{1}$, and then evaluate it up to terms of $\mathcal{O}\left(n_{1}^{-1}, n_{2}^{-1}\right)$ for $n_{1}, n_{2} \gg 1$, assuming that $G, A, B, \mathbf{j}_{\mu}$, and $g$ are also $\mathcal{O}(1)$ functions of $n_{2}$.
We will proceed by evaluating the integrals for $G$ invertible, and then infer the general case by a continuity argument. We treat the quartic term perturbatively, and all other terms directly. Writing

$$
C \equiv G-\frac{1}{n_{1}} B
$$

the leading term in the integral over $\mathbf{q}_{\mu}$ is

$$
\frac{1}{(2 \pi)^{n_{2} p / 2} \operatorname{det}(C)^{n_{2} / 2}} \exp \left(-\frac{1}{2} \sum_{\mu, \nu=1}^{p} C_{\mu \nu}^{-1}\left(\mathbf{h}_{\mu} \cdot \mathbf{h}_{\nu}\right)\right)
$$

Multiplying and dividing by this quantity, we can compute the perturbative correction from the quartic term using the fact that $\mathbf{q}_{\mu}$ then behaves as a Gaussian random vector of mean $\overline{\mathbf{q}}_{\mu}=i \sum_{\nu=1}^{p} C_{\mu \nu}^{-1} \mathbf{h}_{\nu}$ and covariance $C_{\mu \nu}^{-1} I_{n_{2}}$. Denoting expectation with respect to this distribution as $\langle\langle\cdot\rangle\rangle_{q}$ and writing $\overline{\mathbf{q}}_{\mu} \equiv \mathbf{q}_{\mu}-\overline{\mathbf{q}}_{\mu}$, Isserlis' theorem yields

$$
\begin{aligned}
& \left\langle\left\langle\left(\mathbf{q}_{\nu} \cdot \mathbf{q}_{\rho}\right)\left(\mathbf{q}_{\lambda} \cdot \mathbf{q}_{\mu}\right)\right\rangle\right\rangle_{q}=\left\langle\left(\left[\overline{\mathbf{q}}_{\nu}+\overline{\mathbf{q}}_{\nu}\right] \cdot\left[\overline{\mathbf{q}}_{\rho}+\overline{\mathbf{q}}_{\rho}\right]\right)\left(\left[\overline{\mathbf{q}}_{\lambda}+\overline{\mathbf{q}}_{\lambda}\right] \cdot\left[\overline{\mathbf{q}}_{\mu}+\overline{\mathbf{q}}_{\mu}\right]\right)\right\rangle_{q} \\
& =\left\langle\left(\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}+\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}+\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}+\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\right.\right. \\
& \left.\times\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}+\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}+\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}+\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right)\right\rangle_{q} \\
& =\left\langle\left(\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right)\right\rangle_{q}+\left\langle\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\right\rangle_{q}\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right) \\
& +\left\langle\left(\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right)\right\rangle_{q}+\left\langle\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right)\right\rangle_{q} \\
& +\left\langle\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right)\right\rangle_{q}+\left\langle\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right)\right\rangle_{q} \\
& +\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\left\langle\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right)\right\rangle_{q}+\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right) \\
& =n_{2}^{2} C_{\nu \rho}^{-1} C_{\lambda \mu}^{-1}+n_{2} C_{\nu \lambda}^{-1} C_{\rho \mu}^{-1}+n_{2} C_{\nu \mu}^{-1} C_{\rho \lambda}^{-1}+n_{2} C_{\nu \rho}^{-1}\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right) \\
& +C_{\nu \lambda}^{-1}\left(\overline{\mathbf{q}}_{\rho} \cdot \overline{\mathbf{q}}_{\mu}\right)+C_{\nu \mu}^{-1}\left(\overline{\mathbf{q}}_{\rho} \cdot \overline{\mathbf{q}}_{\lambda}\right) \\
& +C_{\rho \lambda}^{-1}\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\mu}\right)+C_{\rho \mu}^{-1}\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\lambda}\right) \\
& +n_{2}\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right) C_{\mu \lambda}^{-1}+\left(\overline{\mathbf{q}}_{\nu} \cdot \overline{\mathbf{q}}_{\rho}\right)\left(\overline{\mathbf{q}}_{\lambda} \cdot \overline{\mathbf{q}}_{\mu}\right) .
\end{aligned}
$$

Then, the quartic correction to the integral over $\mathbf{q}_{\mu}$ is proportional to

$$
\begin{aligned}
\sum_{\mu, \nu, \rho, \lambda=1}^{p} G_{\mu \nu} G_{\rho \lambda}\left\langle\left(\mathbf{q}_{\nu} \cdot \mathbf{q}_{\rho}\right)\left(\mathbf{q}_{\lambda} \cdot \mathbf{q}_{\mu}\right)\right\rangle_{q}= & n_{2}\left(n_{2}+1\right) \operatorname{tr}\left(G C^{-1} G C^{-1}\right)+n_{2} \operatorname{tr}\left(G C^{-1}\right)^{2} \\
& -2\left(n_{2}+1\right) \operatorname{tr}\left(G C^{-1} G C^{-1} H C^{-1}\right) \\
& -2 \operatorname{tr}\left(G C^{-1}\right) \operatorname{tr}\left(G C^{-1} H C^{-1}\right) \\
& +\operatorname{tr}\left(G C^{-1} H C^{-1} G C^{-1} H C^{-1}\right)
\end{aligned}
$$

where we write $H_{\mu \nu} \equiv \mathbf{h}_{\mu} \cdot \mathbf{h}_{\nu}$.
We now must integrate over $\mathbf{h}_{\mu}$. The leading term is simply

$$
\operatorname{det}(C D)^{-n_{2} / 2} \exp \left(\frac{1}{2} \sum_{\mu, \nu=1}^{p} D_{\mu \nu}^{-1} J_{\mu \nu}\right)
$$

where we have defined

$$
D \equiv C^{-1}+\frac{1}{n_{2}} A
$$

and $J_{\mu \nu} \equiv \mathbf{j}_{\mu} \cdot \mathbf{j}_{\nu}$. Multiplying and dividing by this quantity, we can compute the perturbative correction from the quartic term using the fact that $\mathbf{h}_{\mu}$ then behaves as a Gaussian random vector of mean $\overline{\mathbf{h}}_{\mu}=\sum_{\nu=1}^{p} D_{\mu \nu}^{-1} \mathbf{j}_{\nu}$ and covariance $D_{\mu \nu}^{-1} I_{n_{2}}$. We denote expectations with respect to this distribution by $\langle\langle\cdot\rangle\rangle_{h}$, and define $\overline{\mathbf{h}}_{\mu} \equiv \mathbf{h}_{\mu}-\overline{\mathbf{h}}_{\mu}$. Then, we have

$$
\langle H_{\mu \nu}\rangle\rangle_{h}=\left\langle\left(\mathbf{h}_{\mu} \cdot \mathbf{h}_{\nu}\right\rangle\right\rangle_{h}=\overline{\mathbf{h}}_{\mu} \cdot \overline{\mathbf{h}}_{\nu}+n_{2} D_{\mu \nu}^{-1}
$$

and, by analogy to the corresponding four-point average for $\mathbf{q}_{\mu}$,

$$
\begin{aligned}
\left\langle\left(\mathbf{h}_{\nu} \cdot \mathbf{h}_{\rho}\right)\left(\mathbf{h}_{\lambda} \cdot \mathbf{h}_{\mu}\right)\right\rangle_{h}= & n_{2}^{2} D_{\nu \rho}^{-1} D_{\lambda \mu}^{-1}+n_{2} D_{\nu \lambda}^{-1} D_{\rho \mu}^{-1}+n_{2} D_{\nu \mu}^{-1} D_{\rho \lambda}^{-1}+n_{2} D_{\nu \rho}^{-1}\left(\overline{\mathbf{h}}_{\lambda} \cdot \overline{\mathbf{h}}_{\mu}\right) \\
& +D_{\nu \lambda}^{-1}\left(\overline{\mathbf{h}}_{\rho} \cdot \overline{\mathbf{h}}_{\mu}\right)+D_{\nu \mu}^{-1}\left(\overline{\mathbf{h}}_{\rho} \cdot \overline{\mathbf{h}}_{\lambda}\right) \\
& +D_{\rho \lambda}^{-1}\left(\overline{\mathbf{h}}_{\nu} \cdot \overline{\mathbf{h}}_{\mu}\right)+D_{\rho \mu}^{-1}\left(\overline{\mathbf{h}}_{\nu} \cdot \overline{\mathbf{h}}_{\lambda}\right) \\
& +n_{2}\left(\overline{\mathbf{h}}_{\nu} \cdot \overline{\mathbf{h}}_{\rho}\right) D_{\mu \lambda}^{-1}+\left(\overline{\mathbf{h}}_{\nu} \cdot \overline{\mathbf{h}}_{\rho}\right)\left(\overline{\mathbf{h}}_{\lambda} \cdot \overline{\mathbf{h}}_{\mu}\right) .
\end{aligned}
$$

Then, the correction to the integral over $\mathbf{h}_{\mu}$ is proportional to

$$
\begin{aligned}
\sum_{\mu, \nu, \rho, \lambda=1}^{p} G_{\mu \nu} G_{\rho \lambda}\left\langle\left(\left(\mathbf{q}_{\nu} \cdot \mathbf{q}_{\rho}\right)\left(\mathbf{q}_{\lambda} \cdot \mathbf{q}_{\mu}\right)\right\rangle\right\rangle= & n_{2}\left(n_{2}+1\right) \operatorname{tr}\left(G C^{-1} G C^{-1}\right)+n_{2} \operatorname{tr}\left(G C^{-1}\right)^{2} \\
& -2\left(n_{2}+1\right) \operatorname{tr}\left(G C^{-1} G C^{-1} D^{-1} J D^{-1} C^{-1}\right) \\
& -2 n_{2}\left(n_{2}+1\right) \operatorname{tr}\left(G C^{-1} G C^{-1} D^{-1} C^{-1}\right) \\
& -2 \operatorname{tr}\left(G C^{-1}\right) \operatorname{tr}\left(G C^{-1} D^{-1} J D^{-1} C^{-1}\right) \\
& -2 n_{2} \operatorname{tr}\left(G C^{-1}\right) \operatorname{tr}\left(G C^{-1} D^{-1} C^{-1}\right) \\
& +n_{2}\left(n_{2}+1\right) \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1} C^{-1} G C^{-1} D^{-1}\right) \\
& +n_{2} \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1}\right)^{2} \\
& +2\left(n_{2}+1\right) \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1} C^{-1} G C^{-1} D^{-1} J D^{-1}\right) \\
& +2 \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1}\right) \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1} J D^{-1}\right) \\
& +\operatorname{tr}\left(C^{-1} G C^{-1} D^{-1} J D^{-1} C^{-1} G C^{-1} D^{-1} J D^{-1}\right)
\end{aligned}
$$

where we have noted that

$$
\begin{aligned}
& \left\langle\left\langle\operatorname{tr}\left(G C^{-1} H C^{-1} G C^{-1} H C^{-1}\right)\right\rangle\right\rangle_{h} \\
& \quad=\sum_{\mu, \nu, \rho, \lambda=1}^{p}\left(C^{-1} G C^{-1}\right)_{\mu \nu}\left(C^{-1} G C^{-1}\right)_{\rho \lambda}\left\langle\left(\mathbf{h}_{\nu} \cdot \mathbf{h}_{\rho}\right)\left(\mathbf{h}_{\lambda} \cdot \mathbf{h}_{\rho}\right)\right\rangle_{h} \\
& \quad=n_{2}\left(n_{2}+1\right) \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1} C^{-1} G C^{-1} D^{-1}\right)+n_{2} \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1}\right)^{2} \\
& \quad+2\left(n_{2}+1\right) \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1} C^{-1} G C^{-1} D^{-1} J D^{-1}\right) \\
& \quad+2 \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1}\right) \operatorname{tr}\left(C^{-1} G C^{-1} D^{-1} J D^{-1}\right) \\
& \quad+\operatorname{tr}\left(C^{-1} G C^{-1} D^{-1} J D^{-1} C^{-1} G C^{-1} D^{-1} J D^{-1}\right)
\end{aligned}
$$

by analogy with the corresponding quartic expectation for $\mathbf{q}_{\mu}$.
We must now expand our results in $n_{1}^{-1}$. The inverses of the matrices $C$ and $D$ have Neumann series

$$
C^{-1}=G^{-1}+\frac{1}{n_{1}} G^{-1} B G^{-1}+\mathcal{O}\left(n_{1}^{-2}\right)
$$

and

$$
\begin{aligned}
D^{-1} & =\left(C^{-1}+\frac{1}{n_{2}} A\right)^{-1} \\
& =\left(G^{-1}+\frac{1}{n_{1}} G^{-1} B G^{-1}+\frac{1}{n_{2}} A+\mathcal{O}\left(n_{1}^{-2}\right)\right)^{-1} \\
& =F^{-1} G-\frac{1}{n_{1}} F^{-1} B F^{-\top}+\mathcal{O}\left(n_{1}^{-2}\right)
\end{aligned}
$$

where we have defined

$$
F \equiv I_{p}+\frac{1}{n_{2}} G A
$$

and we write $F^{-\top}=\left(F^{-1}\right)^{\top}=\left(F^{\top}\right)^{-1}$. Then, using the series expansion of the log-determinant, we find that the logarithm of the leading term expands as

$$
\begin{aligned}
\frac{1}{2} \operatorname{tr}\left(D^{-1} J\right)-\frac{1}{2} n_{2} \log \operatorname{det}(C D)= & \frac{1}{2} \operatorname{tr}\left(F^{-1} G J\right)-\frac{1}{2} n_{2} \log \operatorname{det}(F) \\
& -\frac{1}{2} \frac{1}{n_{1}} \operatorname{tr}\left(F^{-1} B F^{-\top} J\right)+\frac{1}{2} \frac{1}{n_{1}} \operatorname{tr}\left(F^{-1} B A\right) \\
& +\mathcal{O}\left(n_{1}^{-2}\right)
\end{aligned}
$$

while the quartic correction simplifies to

$$
\begin{aligned}
& \frac{1}{4} \frac{g}{n_{1}} \sum_{\mu, \nu, \rho, \lambda=1}^{p} G_{\mu \nu} G_{\rho \lambda}\left\langle\left(\mathbf{q}_{\nu} \cdot \mathbf{q}_{\rho}\right)\left(\mathbf{q}_{\lambda} \cdot \mathbf{q}_{\mu}\right)\right\rangle \\
& =\frac{1}{4} \frac{g}{n_{1}} n_{2}\left(n_{2}+p+1\right) p \\
& +\frac{1}{4} \frac{n_{2} g}{n_{1}}\left(\left(n_{2}+1\right) \operatorname{tr}\left(F^{-2}\right)+\operatorname{tr}\left(F^{-1}\right)^{2}-2\left(n_{2}+p+1\right) \operatorname{tr}\left(F^{-1}\right)\right) \\
& +\frac{1}{2} \frac{g}{n_{1}}\left(\left(n_{2}+1\right) \operatorname{tr}\left(F^{-3} G J\right)+\operatorname{tr}\left(F^{-1}\right) \operatorname{tr}\left(F^{-2} G J\right)-\left(n_{2}+p+1\right) \operatorname{tr}\left(F^{-2} G J\right)\right) \\
& +\frac{1}{4} \frac{g}{n_{1}} \operatorname{tr}\left(F^{-2} G J F^{-2} G J\right) \\
& +\mathcal{O}\left(n_{1}^{-2}\right)
\end{aligned}
$$

Combining these results, we find that the result of integrating out the layer to $\mathcal{O}\left(n_{1}^{-1}\right)$ is

$$
\begin{aligned}
\log I= & \frac{1}{2} \operatorname{tr}\left(F^{-1} G J\right)-\frac{1}{2} n_{2} \log \operatorname{det}(F) \\
& -\frac{1}{2} \frac{1}{n_{1}} \operatorname{tr}\left(F^{-1} B F^{-\top} J\right)+\frac{1}{2} \frac{1}{n_{1}} \operatorname{tr}\left(F^{-1} B A\right) \\
& +\frac{1}{4} \frac{g}{n_{1}} n_{2}\left(n_{2}+p+1\right) p \\
& +\frac{1}{4} \frac{n_{2} g}{n_{1}}\left(\left(n_{2}+1\right) \operatorname{tr}\left(F^{-2}\right)+\operatorname{tr}\left(F^{-1}\right)^{2}-2\left(n_{2}+p+1\right) \operatorname{tr}\left(F^{-1}\right)\right) \\
& +\frac{1}{2} \frac{g}{n_{1}}\left(\left(n_{2}+1\right) \operatorname{tr}\left(F^{-3} G J\right)+\operatorname{tr}\left(F^{-1}\right) \operatorname{tr}\left(F^{-2} G J\right)-\left(n_{2}+p+1\right) \operatorname{tr}\left(F^{-2} G J\right)\right) \\
& +\frac{1}{4} \frac{g}{n_{1}} \operatorname{tr}\left(F^{-2} G J F^{-2} G J\right) \\
& +\mathcal{O}\left(n_{1}^{-2}\right)
\end{aligned}
$$

As this result is a continuous function of $G$, as the set of full-rank positive definite matrices is dense in the space of positive semidefinite matrices, this result holds for all positive-semidefinite $G$.
We now further expand this result in $n_{2}^{-1}$. This yields

$$
F^{-1}=I_{p}-\frac{1}{n_{2}} G A+\frac{1}{n_{2}^{2}} G A G A+\mathcal{O}\left(n_{2}^{-3}\right)
$$

and

$$
\log \operatorname{det}(F)=\frac{1}{n_{2}} \operatorname{tr}(G A)-\frac{1}{2} \frac{1}{n_{2}^{2}} \operatorname{tr}(G A G A)+\mathcal{O}\left(n_{2}^{-3}\right)
$$

hence we find that the logarithm of the leading term yields

$$
\begin{aligned}
\frac{1}{2} \operatorname{tr}\left(D^{-1} J\right)-\frac{1}{2} n_{2} \log \operatorname{det}(C D)= & \frac{1}{2} \operatorname{tr}(G J)-\frac{1}{2} \operatorname{tr}(G A)+\frac{1}{4} \frac{1}{n_{2}} \operatorname{tr}(G A G A) \\
& -\frac{1}{2} \frac{1}{n_{2}} \operatorname{tr}(G A G J)+\frac{1}{2} \frac{1}{n_{1}} \operatorname{tr}(B(A-J)) \\
& +\mathcal{O}\left(n_{1}^{-2}, n_{2}^{-2}, n_{1}^{-1} n_{2}^{-1}\right)
\end{aligned}
$$

After some straightforward but tedious algebra, the quartic term reduces to

$$
\begin{aligned}
\frac{1}{4} \frac{g}{n_{1}} \sum_{\mu, \nu, \rho, \lambda=1}^{p} G_{\mu \nu} G_{\rho \lambda}\left\langle\left(\mathbf{q}_{\nu} \cdot \mathbf{q}_{\rho}\right)\left(\mathbf{q}_{\lambda} \cdot \mathbf{q}_{\mu}\right)\right\rangle= & \frac{1}{4} \frac{g}{n_{1}} \operatorname{tr}(G(A-J) G(A-J)) \\
& +\mathcal{O}\left(n_{1}^{-2}, n_{2}^{-2}, n_{1}^{-1} n_{2}^{-1}\right)
\end{aligned}
$$

Combining these results, we find that the result of integrating out the layer is

$$
\begin{aligned}
\log I= & \frac{1}{2} \operatorname{tr}(G J)-\frac{1}{2} \operatorname{tr}(G A)+\frac{1}{4} \frac{1}{n_{2}}\left(1+\frac{n_{2}}{n_{1}} g\right) \operatorname{tr}(G A G A) \\
& -\frac{1}{2}\left(1+\frac{n_{2}}{n_{1}} g\right) \operatorname{tr}(G A G J)+\frac{1}{2} \frac{1}{n_{1}} \operatorname{tr}(B(A-J))+\frac{1}{4} \frac{1}{n_{1}} g \operatorname{tr}(G J G J) \\
& +\mathcal{O}\left(n_{1}^{-2}, n_{2}^{-2}, n_{1}^{-1} n_{2}^{-1}\right)
\end{aligned}
$$

Again, this result is continuous in $G$, hence it holds even if $G$ is rank-deficient.

# D. 3 Perturbative computation of the partition function of a deep linear network 

We now apply the results of Appendix D. 2 to compute the partition function for a deep linear network to the desired order. Our starting point is the effective action before any of the layers have been integrated out, including a source term:

$$
\begin{aligned}
S= & -\frac{1}{2} \beta \sum_{\mu=1}^{p}\left\|\mathbf{h}_{\mu}^{(d)}-\mathbf{y}_{\mu}\right\|^{2}+\sum_{\ell=1}^{d} \sum_{\mu=1}^{p} i \mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\mu}^{(\ell)}-\frac{1}{2} \sum_{\mu, \nu=1}^{p}\left(\sigma_{1}^{2} G_{x x}\right)_{\mu \nu}\left(\mathbf{q}_{\mu}^{(1)} \cdot \mathbf{q}_{\nu}^{(1)}\right) \\
& -\frac{1}{2} \sum_{\ell=1}^{d-1} \frac{1}{n_{\ell}} \sum_{\mu, \nu=1}^{p}\left(J_{\mu \nu}^{(\ell)}+\sigma_{\ell+1}^{2} \mathbf{q}_{\mu}^{(\ell+1)} \cdot \mathbf{q}_{\nu}^{(\ell+1)}\right)\left(\mathbf{h}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\nu}^{(\ell)}\right)
\end{aligned}
$$

Applying the results of Appendix D. 2 with

$$
\begin{aligned}
G & =\sigma_{1}^{2} G_{x x} \\
\mathbf{j}_{\mu} & =0 \\
A & =J^{(1)}+\sigma_{2}^{2} Q^{(2)} \\
B & =0, \quad \text { and } \\
g & =0
\end{aligned}
$$

we find that the effective action after integrating out the first layer is

$$
\begin{aligned}
S^{(1)}= & -\frac{1}{2} \beta \sum_{\mu=1}^{p}\left\|\mathbf{h}_{\mu}^{(d)}-\mathbf{y}_{\mu}\right\|^{2}+\sum_{\ell=2}^{d} \sum_{\mu=1}^{p} i \mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\mu}^{(\ell)}-\frac{1}{2} \sum_{\mu, \nu=1}^{p}\left(m_{2}^{2} G_{x x}\right)_{\mu \nu}\left(\mathbf{q}_{\mu}^{(2)} \cdot \mathbf{q}_{\nu}^{(2)}\right) \\
& -\frac{1}{2} \sum_{\ell=2}^{d-1} \frac{1}{n_{\ell}} \sum_{\mu, \nu=1}^{p}\left(J_{\mu \nu}^{(\ell)}+\sigma_{\ell+1}^{2} \mathbf{q}_{\mu}^{(\ell+1)} \cdot \mathbf{q}_{\nu}^{(\ell+1)}\right)\left(\mathbf{h}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\nu}^{(\ell)}\right) \\
& +\frac{1}{4} \frac{g_{1}}{n_{1}} m_{2}^{4} \operatorname{tr}\left(G_{x x} Q^{(2)} G_{x x} Q^{(2)}\right)+\frac{1}{2} \frac{g_{1}}{n_{1}} m_{2}^{2} \operatorname{tr}\left(G_{x x} \tilde{J}_{1} G_{x x} Q^{(2)}\right) \\
& -\frac{1}{2} \operatorname{tr}\left(m_{1}^{2} G_{x x} J^{(1)}\right)+\frac{1}{4} \frac{g_{1}}{n_{1}} m_{1}^{4} \operatorname{tr}\left(G_{x x} J^{(1)} G_{x x} J^{(1)}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where we have defined

$$
\begin{aligned}
m_{1} & \equiv \sigma_{1} \\
m_{2} & \equiv \sigma_{2} m_{1} \\
g_{1} & \equiv 1, \quad \text { and } \\
\tilde{J}_{1} & \equiv m_{1}^{2} J^{(1)}
\end{aligned}
$$

Assuming that the network has more than one hidden layer, if we now again apply the results of Appendix D. 2 with

$$
\begin{aligned}
G & =m_{2}^{2} G_{x x} \\
\mathbf{j}_{\mu} & =0 \\
A & =J^{(2)}+\sigma_{3}^{2} Q^{(3)} \\
B & =g_{1} m_{2}^{2} G_{x x} \tilde{J}_{1} G_{x x}, \quad \text { and } \\
g & =g_{1}
\end{aligned}
$$

we find that the effective action after integrating out the first two layers is

$$
\begin{aligned}
S^{(2)}= & -\frac{1}{2} \beta \sum_{\mu=1}^{p}\left\|\mathbf{h}_{\mu}^{(d)}-\mathbf{y}_{\mu}\right\|^{2}+\sum_{\ell=3}^{d} \sum_{\mu=1}^{p} i \mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\mu}^{(\ell)}-\frac{1}{2} \sum_{\mu, \nu=1}^{p}\left(m_{3}^{2} G_{x x}\right)_{\mu \nu}\left(\mathbf{q}_{\mu}^{(3)} \cdot \mathbf{q}_{\nu}^{(3)}\right) \\
& -\frac{1}{2} \sum_{\ell=3}^{d-1} \frac{1}{n_{\ell}} \sum_{\mu, \nu=1}^{p}\left(J_{\mu \nu}^{(\ell)}+\sigma_{\ell+1}^{2} \mathbf{q}_{\mu}^{(\ell+1)} \cdot \mathbf{q}_{\nu}^{(\ell+1)}\right)\left(\mathbf{h}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\nu}^{(\ell)}\right) \\
& +\frac{1}{4} \frac{g_{2}}{n_{2}} m_{3}^{4} \operatorname{tr}\left(G_{x x} Q^{(3)} G_{x x} Q^{(3)}\right) \\
& +\frac{1}{2} \frac{g_{2}}{n_{2}} m_{3}^{2} \operatorname{tr}\left(G_{x x} \tilde{J}_{2} G_{x x} Q^{(3)}\right) \\
& -\frac{1}{2} \operatorname{tr}\left(m_{1}^{2} G_{x x} J^{(1)}\right)-\frac{1}{2} \operatorname{tr}\left(m_{2}^{2} G_{x x} J^{(2)}\right) \\
& +\frac{1}{4} \frac{g_{1}}{n_{1}} m_{1}^{4} \operatorname{tr}\left(G_{x x} J^{(1)} G_{x x} J^{(1)}\right)+\frac{1}{4} \frac{g_{2}}{n_{2}} m_{2}^{4} \operatorname{tr}\left(G_{x x} J^{(2)} G_{x x} J^{(2)}\right) \\
& +\frac{1}{2} \frac{g_{1}}{n_{1}} m_{2}^{2} \operatorname{tr}\left(G_{x x} \tilde{J}_{1} G_{x x} J^{(2)}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where we have defined

$$
\begin{aligned}
m_{3} & \equiv \sigma_{3} m_{2} \\
g_{2} & \equiv 1+\frac{n_{2}}{n_{1}} g_{1}, \quad \text { and } \\
\tilde{J}_{2} & \equiv m_{2}^{2} J^{(2)}+\frac{n_{2}}{n_{1}} \frac{g_{1}}{g_{2}} \tilde{J}_{1}
\end{aligned}
$$

Then, by induction, we can see that we can iterate this procedure to integrate out all of the hidden layers, yielding

$$
\begin{aligned}
S^{(d-1)}= & -\frac{1}{2} \beta \sum_{\mu=1}^{p}\left\|\mathbf{h}_{\mu}^{(d)}-\mathbf{y}_{\mu}\right\|^{2}+\sum_{\mu=1}^{p} i \mathbf{q}_{\mu}^{(d)} \cdot \mathbf{h}_{\mu}^{(d)}-\frac{1}{2} \sum_{\mu, \nu=1}^{p}\left(m_{d}^{2} G_{x x}\right)_{\mu \nu}\left(\mathbf{q}_{\mu}^{(d)} \cdot \mathbf{q}_{\nu}^{(d)}\right) \\
& +\frac{1}{4} \frac{g_{d-1}}{n_{d-1}} m_{d}^{4} \operatorname{tr}\left(G_{x x} Q^{(d)} G_{x x} Q^{(d)}\right) \\
& +\frac{1}{2} \frac{g_{d-1}}{n_{d-1}} m_{d}^{2} \operatorname{tr}\left(G_{x x} \tilde{J}_{d-1} G_{x x} Q^{(d)}\right) \\
& -\frac{1}{2} \sum_{\ell=1}^{d-1} \operatorname{tr}\left(m_{\ell}^{2} G_{x x} J^{(\ell)}\right) \\
& +\frac{1}{4} \sum_{\ell=1}^{d-1} \frac{g_{\ell}}{n_{\ell}} m_{\ell}^{4} \operatorname{tr}\left(G_{x x} J^{(\ell)} G_{x x} J^{(\ell)}\right) \\
& +\frac{1}{2} \sum_{\ell=1}^{d-2} \frac{g_{\ell}}{n_{\ell}} m_{\ell+1}^{2} \operatorname{tr}\left(G_{x x} \tilde{J}_{\ell} G_{x x} J^{(\ell+1)}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where $m_{d}, g_{d-1}$, and $\tilde{J}_{d-1}$ are defined by the closed recurrences

$$
\begin{aligned}
m_{\ell} & \equiv \sigma_{\ell} m_{\ell-1} \\
g_{\ell} & \equiv 1+\frac{n_{\ell}}{n_{\ell-1}} g_{\ell-1}, \quad \text { and } \\
\tilde{J}_{\ell} & \equiv m_{\ell}^{2} J^{(\ell)}+\frac{n_{\ell}}{n_{\ell-1}} \frac{g_{\ell-1}}{g_{\ell}} \tilde{J}_{\ell-1}
\end{aligned}
$$

Applying the results of Appendix D. 2 one final time with

$$
\begin{aligned}
G & =m_{d}^{2} G_{x x} \\
\mathbf{j}_{\mu} & =\beta \mathbf{y} \\
A & =\beta n_{d} I_{p} \\
B & =g_{d-1} m_{d}^{2} G_{x x} \tilde{J}_{d-1} G_{x x}, \quad \text { and } \\
g & =g_{d-1}
\end{aligned}
$$

we conclude that

$$
\begin{aligned}
\log Z= & -\frac{1}{2} \beta n_{d} \operatorname{tr}\left(\tilde{\Gamma}^{-1} G_{y y}\right)-\frac{1}{2} n_{d} \log \operatorname{det}(\tilde{\Gamma}) \\
& +\frac{1}{4} \frac{n_{d} g_{d-1}}{n_{d-1}}\left(\left(n_{d}+p+1\right) p+\left(n_{d}+1\right) \operatorname{tr}\left(\tilde{\Gamma}^{-2}\right)+\operatorname{tr}\left(\tilde{\Gamma}^{-1}\right)^{2}-2\left(n_{d}+p+1\right) \operatorname{tr}\left(\tilde{\Gamma}^{-1}\right)\right) \\
& +\frac{1}{2} \frac{g_{d-1}}{n_{d-1}} \beta^{2} n_{d} m_{d}^{2}\left(\left(n_{d}+1\right) \operatorname{tr}\left(\tilde{\Gamma}^{-3} G_{x x} G_{y y}\right)+\operatorname{tr}\left(\tilde{\Gamma}^{-1}\right) \operatorname{tr}\left(\tilde{\Gamma}^{-2} G_{x x} G_{y y}\right)\right. \\
& \left.-\left(n_{d}+p+1\right) \operatorname{tr}\left(\tilde{\Gamma}^{-2} G_{x x} G_{y y}\right)\right) \\
& +\frac{1}{4} \frac{g_{d-1}}{n_{d-1}} \beta^{4} n_{d}^{2} m_{d}^{4} \operatorname{tr}\left(\tilde{\Gamma}^{-2} G_{x x} G_{y y} \tilde{\Gamma}^{-2} G_{x x} G_{y y}\right) \\
& -\frac{1}{2} \frac{g_{d-1}}{n_{d-1}} n_{d} m_{d}^{2} \operatorname{tr}\left[\left(\beta^{2} G_{x x} \tilde{\Gamma}^{-1} G_{y y} \tilde{\Gamma}^{-1} G_{x x}-\beta G_{x x} \tilde{\Gamma}^{-1} G_{x x}\right) \tilde{J}_{d-1}\right] \\
& -\frac{1}{2} \sum_{\ell=1}^{d-1} \operatorname{tr}\left(m_{\ell}^{2} G_{x x} J^{(\ell)}\right) \\
& +\frac{1}{4} \sum_{\ell=1}^{d-1} \frac{g_{\ell}}{n_{\ell}} m_{\ell}^{4} \operatorname{tr}\left(G_{x x} J^{(\ell)} G_{x x} J^{(\ell)}\right) \\
& +\frac{1}{2} \sum_{\ell=1}^{d-2} \frac{g_{\ell}}{n_{\ell}} m_{\ell+1}^{2} \operatorname{tr}\left(G_{x x} \tilde{J}_{\ell} G_{x x} J^{(\ell+1)}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where we have defined the matrix

$$
\tilde{\Gamma} \equiv I_{p}+\beta m_{d}^{2} G_{x x}
$$

and absorbed the normalizing constant using the fact that $I_{p}-\beta m_{d}^{2} \tilde{\Gamma}^{-1} G_{x x}=\tilde{\Gamma}^{-1}$. As was the case for the individual layer integrals, a continuity argument implies that this expression can be applied even if $G_{x x}$ is rank-deficient.

# D. 4 Computing the average hidden layer kernels of a deep linear network 

With the relevant partition function in hand, we can finally compute the average hidden layer kernels. In particular, we can immediately read off that

$$
\begin{aligned}
\left\langle K^{(\ell)}\right\rangle= & m_{\ell}^{2} G_{x x} \\
& +\frac{g_{d-1}}{n_{d-1}} n_{d} m_{d}^{2} \operatorname{tr}\left[\left(\beta^{2} G_{x x} \tilde{\Gamma}^{-1} G_{y y} \tilde{\Gamma}^{-1} G_{x x}-\beta G_{x x} \tilde{\Gamma}^{-1} G_{x x}\right) \frac{\delta \tilde{J}_{d-1}}{\delta J^{(\ell)}}\right|_{J^{(\ell)}=0}\right] \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

hence our only task is to determine how the effective source $\tilde{J}_{d-1}$ depends on the source for a given layer. Fortunately, the recurrence relation for the effective source is extremely easy to solve, yielding

$$
\tilde{J}_{d-1}=\sum_{\ell=1}^{d-1} m_{\ell}^{2} \frac{n_{d-1}}{n_{\ell}} \frac{g_{\ell}}{g_{d-1}} J^{(\ell)}
$$

Thus, defining the matrix

$$
\Gamma \equiv \frac{1}{\beta m_{d}^{2}} \tilde{\Gamma}=G_{x x}+\frac{1}{\beta m_{d}^{2}} I_{p}
$$

we find that

$$
\left\langle K^{(\ell)}\right\rangle=m_{\ell}^{2} G_{x x}+\frac{g_{\ell}}{n_{\ell}} n_{d} m_{\ell}^{2}\left(m_{d}^{-2} G_{x x} \Gamma^{-1} G_{y y} \Gamma^{-1} G_{x x}-G_{x x} \Gamma^{-1} G_{x x}\right)+\mathcal{O}\left(n^{-2}\right)
$$

To obtain the expression listed in the main text, we note that

$$
\frac{g_{\ell}}{n_{\ell}}=\frac{1}{n_{\ell}}+\frac{g_{\ell-1}}{n_{\ell-1}}
$$

hence we have

$$
\frac{g_{\ell}}{n_{\ell}}=\sum_{\ell^{\prime}=1}^{\ell} \frac{1}{n_{\ell^{\prime}}}
$$

mirroring the width dependence found by Yaida [12] in his study of the prior of deep linear networks.

# E Average kernels in a deep feedforward linear network with skip connections 

In this appendix, we show that Conjecture 1 holds perturbatively for a linear feedforward network with arbitrary skip connections, following the method of Appendix D. Concretely, we consider a network defined as

$$
\begin{aligned}
\mathbf{h}^{(0)} & =\mathbf{x} \\
\mathbf{h}^{(\ell)} & =\sum_{\ell^{\prime}=0}^{\ell-1} \frac{\sigma_{\ell, \ell^{\prime}}}{\sqrt{n_{\ell^{\prime}}}} W^{\left(\ell, \ell^{\prime}\right)} \mathbf{h}^{\left(\ell^{\prime}\right)} \quad \ell=1, \ldots, d \\
\mathbf{f} & =\mathbf{h}^{(d)}
\end{aligned}
$$

where $\sigma_{\ell, \ell^{\prime}}$ is positive if layer $\ell$ receives input from an earlier layer $\ell^{\prime}<\ell$, and zero otherwise.

## E. 1 Perturbative computation of the partition function

Upon integrating out the weights, we obtain an effective action for the preactivations and the corresponding Lagrange multipliers of

$$
\begin{aligned}
S= & -\beta \sum_{\mu=1}^{p} \varepsilon\left(\mathbf{h}_{\mu}^{(d)}, \mathbf{y}_{\mu}\right)+\sum_{\mu=1}^{p} \sum_{\ell=1}^{d} i \mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\mu}^{(\ell)} \\
& -\frac{1}{2} \sum_{\ell=1}^{d-1} \frac{1}{n_{\ell}} \sum_{\mu, \nu=1}^{p}\left[J^{(\ell)}+\sum_{\ell^{\prime}=\ell+1}^{d} \sigma_{\ell^{\prime}, \ell}^{2}\left(\mathbf{q}_{\mu}^{\left(\ell^{\prime}\right)} \cdot \mathbf{q}_{\nu}^{\left(\ell^{\prime}\right)}\right)\right]\left(\mathbf{h}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\nu}^{(\ell)}\right) \\
& -\frac{1}{2} \sum_{\ell=1}^{d} \sigma_{\ell, 0}^{2} \sum_{\mu, \nu=1}^{p}\left(G_{x x}\right)_{\mu \nu}\left(\mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{q}_{\nu}^{(\ell)}\right)
\end{aligned}
$$

Applying the result of Appendix D. 2 with

$$
\begin{aligned}
G & =\sigma_{1,0}^{2} G_{x x} \\
\mathbf{j}_{\mu} & =\mathbf{0} \\
A & =J^{(1)}+\sum_{\ell^{\prime}=2}^{d} \sigma_{\ell^{\prime}, 1}^{2} Q^{\left(\ell^{\prime}\right)} \\
B & =0, \quad \text { and } \\
g & =0
\end{aligned}
$$

we find that the effective action after integrating out the first layer is

$$
\begin{aligned}
S^{(1)}= & -\beta \sum_{\mu=1}^{p} \varepsilon\left(\mathbf{h}_{\mu}^{(d)}, \mathbf{y}_{\mu}\right)+\sum_{\mu=1}^{p} \sum_{\ell=2}^{d} i \mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\mu}^{(\ell)} \\
& -\frac{1}{2} \sum_{\ell=2}^{d-1} \frac{1}{n_{\ell}} \sum_{\mu, \nu=1}^{p}\left[J^{(\ell)}+\sum_{\ell^{\prime}=\ell+1}^{d} \sigma_{\ell^{\prime}, \ell}^{2}\left(\mathbf{q}_{\mu}^{\left(\ell^{\prime}\right)} \cdot \mathbf{q}_{\nu}^{\left(\ell^{\prime}\right)}\right)\right]\left(\mathbf{h}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\nu}^{(\ell)}\right) \\
& -\frac{1}{2} \sum_{\ell=2}^{d} m_{\ell, 1}^{2} \operatorname{tr}\left(G_{x x} Q^{(\ell)}\right)+\frac{1}{4} \frac{1}{n_{1}} \sum_{\ell, \ell^{\prime}=2}^{d} g_{\ell, \ell^{\prime}, 1} \operatorname{tr}\left(G_{x x} Q^{(\ell)} G_{x x} Q^{\left(\ell^{\prime}\right)}\right) \\
& +\frac{1}{2} \frac{1}{n_{1}} \sum_{\ell=2}^{d} \operatorname{tr}\left(G_{x x} \bar{J}_{\ell, 1} G_{x x} Q^{(\ell)}\right) \\
& -\frac{1}{2} m_{1,0}^{2} \operatorname{tr}\left(G_{x x} J^{(1)}\right) \\
& +\frac{1}{4} \frac{1}{n_{1}} \sigma_{1,0}^{4} \operatorname{tr}\left(G_{x x} J^{(1)} G_{x x} J^{(1)}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where we have defined

$$
\begin{aligned}
m_{\ell, 0}^{2} & \equiv \sigma_{\ell, 0}^{2} \\
m_{\ell, 1}^{2} & \equiv m_{\ell, 0}^{2}+\sigma_{\ell, 1}^{2} m_{1,0}^{2} \\
g_{\ell, \ell^{\prime}, 1} & \equiv \sigma_{\ell, 1}^{2} \sigma_{\ell^{\prime}, 1}^{2} \sigma_{1,0}^{4}, \quad \text { and } \\
\bar{J}_{\ell, 1} & \equiv \sigma_{\ell, 1}^{2} \sigma_{1,0}^{4} J^{(1)}
\end{aligned}
$$

where $\ell, \ell^{\prime}>1$ for all cases but $m_{1,0}^{2}$. Assuming the network has more than one hidden layer, if we now again apply the results of Appendix D. 2 with

$$
\begin{aligned}
G & =m_{2,1}^{2} G_{x x} \\
\mathbf{j}_{\mu} & =\mathbf{0} \\
A & =J^{(2)}+\sum_{\ell^{\prime}=3}^{d} \sigma_{\ell^{\prime}, 2}^{2} Q^{\left(\ell^{\prime}\right)} \\
B & =G_{x x} \bar{J}_{2,1} G_{x x}+\sum_{\ell^{\prime}=3}^{d} g_{\ell^{\prime}, 2,1} G_{x x} Q^{\left(\ell^{\prime}\right)} G_{x x}, \quad \text { and } \\
g & =g_{2,2,1} / m_{2,1}^{4}
\end{aligned}
$$

we find that the effective action after integrating out the first two layers of the network is

$$
\begin{aligned}
S^{(2)}= & -\beta \sum_{\mu=1}^{p} \varepsilon\left(\mathbf{h}_{\mu}^{(d)}, \mathbf{y}_{\mu}\right)+\sum_{\mu=1}^{p} \sum_{\ell=1}^{d} i \mathbf{q}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\mu}^{(\ell)} \\
& -\frac{1}{2} \sum_{\ell=3}^{d-1} \frac{1}{n_{\ell}} \sum_{\mu, \nu=1}^{p}\left[J_{\mu \nu}^{(\ell)}+\sum_{\ell^{\prime}=\ell+1}^{d} \sigma_{\ell^{\prime}, \ell}^{2}\left(\mathbf{q}_{\mu}^{\left(\ell^{\prime}\right)} \cdot \mathbf{q}_{\nu}^{\left(\ell^{\prime}\right)}\right)\right]\left(\mathbf{h}_{\mu}^{(\ell)} \cdot \mathbf{h}_{\nu}^{(\ell)}\right) \\
& -\frac{1}{2} \sum_{\ell=3}^{d} m_{\ell, 2}^{2} \operatorname{tr}\left(G_{x x} Q^{(\ell)}\right)+\frac{1}{4} \frac{1}{n_{2}} \sum_{\ell, \ell^{\prime}=3}^{d} g_{\ell, \ell^{\prime}, 2} \operatorname{tr}\left(G_{x x} Q^{(\ell)} G_{x x} Q^{\left(\ell^{\prime}\right)}\right) \\
& +\frac{1}{2} \frac{1}{n_{2}} \sum_{\ell=3}^{d} \operatorname{tr}\left(G_{x x} \tilde{J}_{\ell, 2} G_{x x} Q^{(\ell)}\right) \\
& -\frac{1}{2} \sum_{\ell=1}^{2} m_{\ell, \ell-1}^{2} \operatorname{tr}\left(G_{x x} J^{(\ell)}\right) \\
& +\frac{1}{4} \frac{1}{n_{1}} m_{1,0}^{4} \operatorname{tr}\left(G_{x x} J^{(1)} G_{x x} J^{(1)}\right)+\frac{1}{4} \frac{1}{n_{2}}\left(m_{2,1}^{4}+\frac{n_{2}}{n_{1}} g_{2,2,1}\right) \operatorname{tr}\left(G_{x x} J^{(2)} G_{x x} J^{(2)}\right) \\
& +\frac{1}{2} \frac{1}{n_{1}} \operatorname{tr}\left(G_{x x} \tilde{J}_{2,1} G_{x x} J^{(2)}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where we now define

$$
\begin{aligned}
m_{\ell, 2}^{2} & \equiv m_{\ell, 1}^{2}+m_{2,1}^{2} \sigma_{\ell, 2}^{2} \\
g_{\ell, \ell^{\prime}, 2} & \equiv m_{2,1}^{4}+\frac{n_{2}}{n_{1}}\left(g_{\ell, \ell^{\prime}, 1}+g_{2,2,1} \sigma_{\ell, 2}^{2} \sigma_{\ell^{\prime}, 2}^{2}+g_{\ell, 2,1} \sigma_{\ell^{\prime}, 2}^{2}+\sigma_{\ell, 2}^{2} g_{2, \ell^{\prime}, 1}\right), \quad \text { and } \\
\tilde{J}_{\ell, 2} & \equiv \frac{n_{2}}{n_{1}} \tilde{J}_{\ell, 1}+\left(m_{2,1}^{4}+\frac{n_{2}}{n_{1}} g_{2,2,1}\right) \sigma_{\ell, 2}^{2} J^{(2)}+\frac{n_{2}}{n_{1}} \sigma_{\ell, 2}^{2} \tilde{J}_{2,1}+\frac{n_{2}}{n_{1}} g_{\ell, 2,1} J^{(2)}
\end{aligned}
$$

for $\ell, \ell^{\prime}>2$. We can now see that we can repeat this procedure to integrate out all of the hidden layers of the network, yielding an effective action of

$$
\begin{aligned}
S^{(d-1)}= & -\beta \sum_{\mu=1}^{p} \varepsilon\left(\mathbf{h}_{\mu}^{(d)}, \mathbf{y}_{\mu}\right)+\sum_{\mu=1}^{p} i \mathbf{q}_{\mu}^{(d)} \cdot \mathbf{h}_{\mu}^{(d)} \\
& -\frac{1}{2} m_{d, d-1}^{2} \operatorname{tr}\left(G_{x x} Q^{(d)}\right)+\frac{1}{4} \frac{1}{n_{d-1}} g_{d, d, d-1} \operatorname{tr}\left(G_{x x} Q^{(d)} G_{x x} Q^{(d)}\right) \\
& +\frac{1}{2} \frac{1}{n_{d-1}} \operatorname{tr}\left(G_{x x} \tilde{J}_{d, d-1} G_{x x} Q^{(d)}\right) \\
& -\frac{1}{2} \sum_{\tau=1}^{d-1} m_{\tau, \tau-1}^{2} \operatorname{tr}\left(G_{x x} J^{(\tau)}\right) \\
& +\frac{1}{4} \sum_{\tau=2}^{d-1}\left(\frac{1}{n_{\tau}} m_{\tau, \tau-1}^{4}+\frac{1}{n_{\tau-1}} g_{\tau, \tau, \tau-1}\right) \operatorname{tr}\left(G_{x x} J^{(\tau)} G_{x x} J^{(\tau)}\right) \\
& +\frac{1}{2} \sum_{\tau=2}^{d-1} \frac{1}{n_{\tau-1}} \operatorname{tr}\left(G_{x x} \tilde{J}_{\tau, \tau-1} G_{x x} J^{(\tau)}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where the coupling constants and effective source obey the recurrences

$$
\begin{aligned}
m_{\ell, \tau}^{2} \equiv & m_{\ell, \tau-1}^{2}+m_{\tau, \tau-1}^{2} \sigma_{\ell, \tau}^{2} \\
g_{\ell, \ell^{\prime}, \tau} \equiv & m_{\tau, \tau-1}^{4} \sigma_{\ell, \tau}^{2} \sigma_{\ell^{\prime}, \tau}^{2} \\
& +\frac{n_{\tau}}{n_{\tau-1}}\left(g_{\ell, \ell^{\prime}, \tau-1}+g_{\tau, \tau, \tau-1} \sigma_{\ell, \tau}^{2} \sigma_{\ell^{\prime}, \tau}^{2}+g_{\ell, \tau, \tau-1} \sigma_{\ell^{\prime}, \tau}^{2}+\sigma_{\ell, \tau}^{2} g_{\tau, \ell^{\prime}, \tau-1}\right), \quad \text { and } \\
\tilde{J}_{\ell, \tau} \equiv & \frac{n_{\tau}}{n_{\tau-1}} \tilde{J}_{\ell, \tau-1}+\frac{n_{\tau}}{n_{\tau-1}} \sigma_{\ell, \tau}^{2} \tilde{J}_{\tau, \tau-1} \\
& +\left(m_{\tau, \tau-1}^{4} \sigma_{\ell, \tau}^{2}+\frac{n_{\tau}}{n_{\tau-1}} g_{\tau, \tau, \tau-1} \sigma_{\ell, \tau}^{2}+\frac{n_{\tau}}{n_{\tau-1}} g_{\ell, \tau, \tau-1}\right) J^{(\tau)}
\end{aligned}
$$

for $\ell, \ell^{\prime}>\tau$. Applying the results of Appendix D. 2 once more with

$$
\begin{aligned}
G & =m_{d, d-1}^{2} G_{x x} \\
\mathbf{j}_{\mu} & =\beta \mathbf{y}_{\mu} \\
A & =\beta n_{d} I_{p} \\
B & =G_{x x} \tilde{J}_{d, d-1} G_{x x}, \quad \text { and } \\
g & =g_{d, d, d-1} / m_{d, d-1}^{4}
\end{aligned}
$$

we find the source-dependent terms in the logarithm of the partition function are

$$
\begin{aligned}
\log Z \supset & -\frac{1}{2} \frac{1}{n_{1}} \beta^{2} n_{d} \operatorname{tr}\left(\Gamma^{-1} G_{x x} \tilde{J}_{d, d-1} G_{x x} \Gamma^{-1} G_{y y}\right)+\frac{1}{2} \frac{1}{n_{d-1}} \beta n_{d} \operatorname{tr}\left(\Gamma^{-1} G_{x x} \tilde{J}_{d, d-1} G_{x x}\right) \\
& -\frac{1}{2} \sum_{\tau=1}^{d-1} m_{\tau, \tau-1}^{2} \operatorname{tr}\left(G_{x x} J^{(\tau)}\right) \\
& +\frac{1}{4} \sum_{\tau=2}^{d-1}\left(\frac{1}{n_{\tau}} m_{\tau, \tau-1}^{4}+\frac{1}{n_{\tau-1}} g_{\tau, \tau, \tau-1}\right) \operatorname{tr}\left(G_{x x} J^{(\tau)} G_{x x} J^{(\tau)}\right) \\
& +\frac{1}{2} \sum_{\tau=2}^{d-1} \frac{1}{n_{\tau-1}} \operatorname{tr}\left(G_{x x} \tilde{J}_{\tau, \tau-1} G_{x x} J^{(\tau)}\right) \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where

$$
\Gamma \equiv I_{p}+\beta m_{d, d-1}^{2} G_{x x}
$$

# E. 2 Computing the average hidden layer kernels 

With the source-dependent terms of the relevant partition function in hand, we can compute the average hidden layer kernels for a feedforward linear network with arbitrary skip connections. We can immediately read off that

$$
\begin{aligned}
\left\langle K^{(\ell)}\right\rangle= & m_{\ell, \ell-1}^{2} G_{x x} \\
& +\frac{n_{d}}{n_{d-1}} \operatorname{tr}\left[\left(\beta^{2} G_{x x} \Gamma^{-1} G_{y y} \Gamma^{-1} G_{x x}-\beta G_{x x} \Gamma^{-1} G_{x x}\right) \frac{\delta \tilde{J}_{d, d-1}}{\delta J^{(\ell)}}\right|_{J^{(\ell)}=0}\right] \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

hence our only task is to compute the derivative of the effective source $\tilde{J}_{d, d-1}$ with respect to the source for the $\ell$-th hidden layer. Singling out the $\ell$-th layer, we can set all sources except $J^{(\ell)}$ to zero. Then, the 'earliest' effective source to be non-zero is

$$
\tilde{J}_{\ell^{\prime}, \ell}=\left(m_{\ell, \ell-1}^{4} \sigma_{\ell^{\prime}, \ell}^{2}+\frac{n_{\ell}}{n_{\ell-1}} g_{\ell, \ell, \ell-1} \sigma_{\ell^{\prime}, \ell}^{2}+\frac{n_{\ell}}{n_{\ell-1}} g_{\ell^{\prime}, \ell, \ell-1}\right) J^{(\ell)}
$$

for $\ell^{\prime}>\ell$, and the recurrence relation for $\tau>\ell$ is

$$
\tilde{J}_{\ell^{\prime}, \tau}=\frac{n_{\tau}}{n_{\tau-1}}\left(\tilde{J}_{\ell^{\prime}, \tau-1}+\sigma_{\ell^{\prime}, \tau}^{2} \tilde{J}_{\tau, \tau-1}\right)
$$

From the form of these recurrences, we can see that

$$
\begin{aligned}
\left\langle K^{(\ell)}\right\rangle= & m_{\ell, \ell-1}^{2} G_{x x} \\
& +\frac{n_{d}}{n_{d-1}} \tilde{g}_{\ell} G_{x x}\left(\beta^{2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\beta \Gamma^{-1}\right) G_{x x} \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

where $\tilde{g}_{\ell}$ is a layer-dependent scalar. Even without explicitly solving the recurrences to obtain $\tilde{g}_{\ell}$, this shows that Conjecture 1 holds perturbatively for linear networks with arbitrary skip connections. We leave detailed study of these recurrences-and therefore of the precise dependence of the corrections on width, depth, and skip connection structure-as an interesting objective for future work.

# F Comparison to the results of Aitchison [10] and Li and Sompolinsky [16] 

In this appendix, we compare our results for the average kernels of deep linear networks to those of Aitchison [10] and Li and Sompolinsky [16].

## F. 1 Comparison to the results of Aitchison [10]

We first show that our result (9) for the low-temperature limit of the average kernels of a deep linear network can be recovered from the results of Aitchison [10]. Working in what corresponds to the zero-temperature limit of our setup, Aitchison derives the following implicit recurrence

$$
0=-\left(n_{\ell+1}-n_{\ell}\right)\left(K^{(\ell)}\right)^{-1}+n_{\ell+1}\left(K^{(\ell)}\right)^{-1}\left(K^{(\ell+1)}\right)\left(K^{(\ell)}\right)^{-1}-n_{\ell}\left(K^{(\ell-1)}\right)^{-1}
$$

for $\ell=1, \ldots, d-1$, where the boundary conditions of the recurrence are $K^{(0)}=G_{x x}$ and $K^{(d)}=G_{y y}$. We will self-consistently solve this recurrence relation in the limit $n_{1}, \ldots, n_{d-1} \rightarrow \infty$, $n_{0}, n_{d}, p=\mathcal{O}(1)$. Concretely, we make the ansatz that the zero-temperature kernels are of the form

$$
K^{(\ell)}=K_{\infty}^{(\ell)}+\frac{1}{n_{\ell}} K_{1}^{(\ell)}+\mathcal{O}\left(n_{\ell}^{-2}\right)
$$

and solve the recurrence relations order-by-order using the resulting Neumann series

$$
\left(K^{(\ell)}\right)^{-1}=\left(K_{\infty}^{(\ell)}\right)^{-1}-\frac{1}{n_{\ell}}\left(K_{\infty}^{(\ell)}\right)^{-1} K_{1}^{(\ell)}\left(K_{\infty}^{(\ell)}\right)^{-1}+\mathcal{O}\left(n_{\ell}^{-2}\right)
$$

The leading-order recurrence is simply

$$
0=\left(1-\frac{n_{\ell+1}}{n_{\ell}}\right)\left(K_{\infty}^{(\ell)}\right)^{-1}+\frac{n_{\ell+1}}{n_{\ell}}\left(K_{\infty}^{(\ell)}\right)^{-1}\left(K_{\infty}^{(\ell+1)}\right)\left(K_{\infty}^{(\ell)}\right)^{-1}-\left(K_{\infty}^{(\ell-1)}\right)^{-1}
$$

with boundary conditions $K_{\infty}^{(0)}=G_{x x}$ and $K_{\infty}^{(d)}=G_{y y}$. For the last hidden layer, we have $n_{\ell+1} / n_{\ell}=n_{d} / n_{d-1} \rightarrow 0$, hence the recurrence reduces to

$$
K_{\infty}^{(d-1)}=K_{\infty}^{(d-2)}
$$

If we iterate this procedure backwards through the network, it is easy to see that the $n_{\ell+1} / n_{\ell^{-}}$ dependent terms at each layer will cancel, leaving

$$
K_{\infty}^{(d-1)}=K_{\infty}^{(d-2)}=\cdots=K_{\infty}^{(1)}=G_{x x}
$$

We now consider the leading finite-width correction. For the last hidden layer, we obtain

$$
0=n_{d}\left(G_{y y}-G_{x x}\right)-K_{1}^{(d-1)}+\frac{n_{d-1}}{n_{d-2}} K_{1}^{(d-2)}
$$

after dropping all terms that are of $\mathcal{O}\left(n^{-2}\right)$ and multiplying on the left and right by $G_{x x}$. For the first hidden layer, we have

$$
0=K_{1}^{(2)}-\left(1+\frac{n_{2}}{n_{1}}\right) K_{1}^{(1)}
$$

Finally, for intermediate hidden layers (i.e., $\ell=2,3, \ldots, d-2$ ), we have

$$
0=K_{1}^{(\ell+1)}-\left(1+\frac{n_{\ell+1}}{n_{\ell}}\right) K_{1}^{(\ell)}+\frac{n_{\ell}}{n_{\ell-1}} K_{1}^{(\ell-1)}
$$

Based on the form of these recurrences, we make the ansatz that the solution is of the form

$$
K_{1}^{(\ell)}=n_{d} a_{\ell}\left(G_{y y}-G_{x x}\right)
$$

for some sequence $a_{\ell}$, where we assume that $G_{y y} \neq G_{x x}$. Then, the recurrence for the last hidden layer is satisfied provided that

$$
a_{d-1}=1+\frac{n_{d-1}}{n_{d-2}} a_{d-2}
$$

those for the intermediate layers if

$$
0=a_{\ell+1}-\left(1+\frac{n_{\ell+1}}{n_{\ell}}\right) a_{\ell}+\frac{n_{\ell}}{n_{\ell-1}} a_{\ell-1}
$$

and that for the first hidden layer if

$$
a_{2}=\left(1+\frac{n_{2}}{n_{1}}\right) a_{1}
$$

Substituting the expression for $a_{d-1}$ into the condition resulting from the recurrence relation centered on $a_{d-2}$, we find that we must have

$$
a_{d-2}=1+\frac{n_{d-2}}{n_{d-3}} a_{d-3}
$$

hence we can iterate this process backwards to the second hidden layer, yielding

$$
a_{\ell}=1+\frac{n_{\ell}}{n_{\ell-1}} a_{\ell-1}
$$

for $\ell=2,3, \ldots, d-1$. Then, the condition relating $a_{2}$ and $a_{1}$ resulting from the recurrence relation for the first layer implies that we must have $a_{1}=1$. Thus, we recover our zero-temperature result from solving Aitchison's recurrence relations order-by-order.

# F. 2 Comparison to the results of Li and Sompolinsky [16] 

We now show that our result (9) for the low-temperature limit of the average kernels of a deep linear network can be recovered as a limiting case of the result of Li and Sompolinsky [16]. Their result for the zero-temperature kernel in the limit $n_{0}, n, p \rightarrow \infty$ with $n_{1}=n_{2}=\cdots=n_{d-1}=n$, $n_{0} / n \in(0, \infty), \alpha \equiv p / n \in(0, \infty)$, and $\sigma_{1}=\cdots=\sigma_{d}=\sigma$ is, in our notation,

$$
\sigma^{-2(\ell+1)}\left\langle K^{(\ell)}\right\rangle \sim\left(1-\frac{n_{d}}{n}\right)^{\ell} G_{x x}+\frac{1}{n} \sigma^{-2 d} Y V M_{\ell} V^{\top} Y^{\top}
$$

where $Y \in \mathbb{R}^{p \times n_{d}}$ is the matrix of targets and $M_{\ell} \in \mathbb{R}^{n_{d} \times n_{d}}$ is a diagonal matrix with non-zero elements

$$
\left[M_{\ell}\right]_{k k}=z_{k}^{-(d-1)} \frac{z_{k}^{\ell}-1}{z_{k}-1}
$$

Here, the orthogonal matrix $V$ is the matrix of eigenvectors of

$$
R=\frac{1}{\sigma^{2} p} Y^{\top} G_{x x}^{+} Y=V \Omega V^{\top}
$$

for $G_{x x}^{+}$the pseudoinverse of $G_{x x}$, and the scalars $z_{k}$ are in turn defined in terms of the eigenvalues $\Omega_{k k}=\omega_{k}$ as

$$
1-\alpha=z_{k}-\alpha \sigma^{-2(d-1)} z_{k}^{-(d-1)} \omega_{k}
$$

we note that Li and Sompolinsky [16] use variables $u_{k 0}=\sigma^{2} z_{k}$.
As we are interested in the limit $\alpha \downarrow 0$, it is useful to write the implicit equation for $z_{k}$ as

$$
z_{k}=1+\alpha\left(\sigma^{-2 L} z_{k}^{-(d-1)} \omega_{k}-1\right)
$$

hence we expect $z_{k} \rightarrow 1$ as $\alpha \downarrow 0$. Thus, we have

$$
\left[M_{\ell}\right]_{k k} \rightarrow \ell
$$

which gives

$$
V M_{\ell} V^{\top} \rightarrow \ell I_{n_{d}}
$$

Using the expansion $\left(1-n_{d} / n\right)^{\ell}=1-n_{d} \ell / n+\mathcal{O}\left(n^{-2}\right)$, we therefore find that

$$
\sigma^{-2(\ell+1)}\left\langle K^{(\ell)}\right\rangle \sim G_{x x}+\frac{n_{d} \ell}{n}\left(\sigma^{-2 d} G_{y y}-G_{x x}\right)
$$

in the limit in which $n_{d} / n \downarrow 0$ and $p / n \downarrow 0$. Therefore, combining this result with that of the previous subsection, our result (9) agrees with those of Aitchison [10] and of Li and Sompolinsky [16] in the appropriate limit. Whether the full result of Li and Sompolinsky [16] agrees with that of Aitchison [10] is an interesting question, but is well beyond the scope of the present work.

# G Predictor statistics and generalization in deep linear networks 

Though the main focus of our work is on the asymptotics of representation learning, we have also computed the leading finite-width corrections to the predictor statistics. Though one can derive the analogy of Conjecture 1 for the predictor statistics of a general BNN with linear readout, the resulting formula is not particularly illuminating. We will therefore present results only for linear networks. As was true of the hidden layer kernels of deep linear networks, this calculation can be performed either using methods similar to those described in Appendix B or Appendix D. As the steps are largely identical to those calculations, we only briefly summarize the results.
In short, we fix a test dataset $\hat{\mathcal{D}}=\left\{\left(\hat{\mathbf{x}}_{\mu}, \hat{\mathbf{y}}_{\mu}\right)\right\}_{\mu=1}^{\hat{p}}$ of $\hat{p}$ examples, and define the Gram matrices

$$
\begin{aligned}
& \left(G_{\hat{x} \hat{x}}\right)_{\hat{\mu} \hat{\nu}} \equiv n_{0}^{-1} \hat{\mathbf{x}}_{\hat{\mu}} \cdot \hat{\mathbf{x}}_{\hat{\nu}} \\
& \left(G_{\hat{y} \hat{y}}\right)_{\hat{\mu} \hat{\nu}} \equiv n_{d}^{-1} \hat{\mathbf{y}}_{\hat{\mu}} \cdot \hat{\mathbf{y}}_{\hat{\nu}} \\
& \left(G_{x \hat{x}}\right)_{\mu \hat{\mu}} \equiv n_{0}^{-1} \mathbf{x}_{\mu} \cdot \hat{\mathbf{x}}_{\hat{\mu}}, \quad \text { and } \\
& \left(G_{y \hat{y}}\right)_{\mu \hat{\nu}} \equiv n_{d}^{-1} \mathbf{y}_{\mu} \cdot \hat{\mathbf{y}}_{\hat{\nu}}
\end{aligned}
$$

Introducing appropriate source terms to allow us to compute predictor statistics, we then proceed perturbatively as before, assuming that the combined input Gram matrix

$$
\left[\begin{array}{ll}
G_{x x} & G_{x \hat{x}} \\
G_{x \hat{x}}^{\top} & G_{\hat{x} \hat{x}}
\end{array}\right]
$$

is invertible. Again, the final result can be extended to the case in which this matrix is not invertible by a continuity argument.
Our notation in this appendix will follow that of Appendix B rather than Appendix D in that we will introduce matrices

$$
\begin{aligned}
& K_{\infty} \equiv \sigma_{1}^{2} \cdots \sigma_{d-1}^{2} G_{x x} \\
& \hat{R}_{\infty} \equiv \sigma_{1}^{2} \cdots \sigma_{d-1}^{2} G_{x \hat{x}}, \quad \text { and } \\
& \hat{K}_{\infty} \equiv \sigma_{1}^{2} \cdots \sigma_{d-1}^{2} G_{\hat{x} \hat{x}}
\end{aligned}
$$

to denote the blocks of the infinite-width kernel of the last hidden layer, rather than introducing scalar parameters to represent the products of variances. This will make our expressions somewhat more compact than they would be under the conventions of Appendix D.

# G. 1 Predictor statistics 

Defining the matrix $\hat{F}_{\hat{\mu} j} \equiv f_{j}\left(\hat{\mathbf{x}}_{\hat{\mu}}\right)$, we find that the mean predictor can be written compactly as

$$
\langle\hat{F}\rangle=\hat{R}_{\infty}^{\top}\left[\Gamma^{-1}-\frac{1}{\beta \sigma_{d}^{2}}\left(\sum_{\ell=1}^{d-1} \frac{1}{n_{\ell}}\right) \Gamma^{-1} M \Gamma^{-1}\right] Y+\mathcal{O}\left(n^{-2}\right)
$$

for

$$
M \equiv \Gamma^{-1} K_{\infty}+\operatorname{tr}\left(\Gamma^{-1} K_{\infty}\right) I_{p}-n_{d}\left(\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right) K_{\infty}
$$

The predictor covariance is given as

$$
\begin{aligned}
& \sigma_{d}^{-2} \operatorname{cov}\left(\hat{F}_{\hat{\mu} j}, \hat{F}_{\hat{\nu} k}\right) \\
& =\left(\hat{K}_{\infty}-\hat{R}_{\infty}^{\top} \Gamma^{-1} \hat{R}_{\infty}\right)_{\hat{\mu} \hat{\nu}} \delta_{j k} \\
& +\left(\sum_{\ell=1}^{d-1} \frac{1}{n_{\ell}}\right)\left[\hat{M}_{\hat{\mu} \hat{\nu}} \delta_{j k}\right. \\
& +\sigma_{d}^{-2}\left(Y^{\top} \Gamma^{-1} K_{\infty} \Gamma^{-1} Y\right)_{j k}\left(\hat{K}_{\infty}-\hat{R}_{\infty}^{\top} \Gamma^{-1} \hat{R}_{\infty}\right)_{\hat{\mu} \hat{\nu}} \\
& -\frac{1}{\beta \sigma_{d}^{4}}\left(Y^{\top} \Gamma^{-1} K_{\infty} \Gamma^{-1} Y\right)_{j k}\left(\hat{R}_{\infty}^{\top} \Gamma^{-2} \hat{R}_{\infty}\right)_{\hat{\mu} \hat{\nu}} \\
& \left.+\frac{1}{\beta^{2} \sigma_{d}^{6}}\left(Y^{\top} \Gamma^{-2} \hat{R}_{\infty}\right)_{j \hat{\nu}}\left(Y^{\top} \Gamma^{-2} \hat{R}_{\infty}\right)_{k \hat{\mu}}\right] \\
& +\mathcal{O}\left(n^{-2}\right)
\end{aligned}
$$

for

$$
\begin{aligned}
\hat{M} \equiv & -\operatorname{tr}\left(\Gamma^{-1} K_{\infty}\right)\left(\hat{K}_{\infty}-\hat{R}_{\infty}^{\top} \Gamma^{-1} \hat{R}_{\infty}\right)+\frac{1}{\beta \sigma_{d}^{2}} \operatorname{tr}\left(\Gamma^{-1} K_{\infty}\right) \hat{R}_{\infty}^{\top} \Gamma^{-2} \hat{R}_{\infty}-\frac{1}{\beta^{2} \sigma_{d}^{4}} \hat{R}_{\infty}^{\top} \Gamma^{-3} \hat{R}_{\infty} \\
& +n_{d} \frac{1}{\beta^{2} \sigma_{d}^{4}} \hat{R}_{\infty}^{\top} \Gamma^{-1}\left(\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right) \Gamma^{-1} \hat{R}_{\infty}
\end{aligned}
$$

The mean and covariance of the training set predictor $F_{\mu j} \equiv f_{j}\left(\mathbf{x}_{\mu}\right)$ can be obtained by setting $\hat{R}_{\infty}$ and $\hat{K}_{\infty}$ to $K_{\infty}$ in the above expressions.

## G. 2 Bias-variance decompositions and the low-temperature limit

These results allow us to define thermal bias-variance decompositions of the form

$$
\langle E\rangle=\frac{1}{2} \sum_{\mu=1}^{p}\left\|\left\langle\mathbf{f}\left(\mathbf{x}_{\mu}\right)\right\rangle-\mathbf{y}_{\mu}\right\|_{2}^{2}+\frac{1}{2} \sum_{\mu=1}^{p} \sum_{k=1}^{n_{d}} \operatorname{cov}\left[f_{k}\left(\mathbf{x}_{\mu}\right), f_{k}\left(\mathbf{x}_{\mu}\right)\right] \equiv E_{b}+E_{v}
$$

for the mean training and test errors. However, the resulting expressions are not particularly illuminating except in the low-temperature limit $\beta \rightarrow \infty$. We will focus on the regime in which $G_{x x}$ (and thus $K_{\infty}$ ) is invertible, in which the underlying linear system $X W=Y$ is underdetermined and the training set can be interpolated. In this regime, $\Gamma^{-1}=K_{\infty}^{-1}+\mathcal{O}\left(\beta^{-1}\right)$, and the mean predictor reduces to the least-norm pseudoinverse solution to the linear system, with mean training and test predictions of

$$
\langle F\rangle=Y+\mathcal{O}\left(\beta^{-1}\right)
$$

and

$$
\langle\hat{F}\rangle=\hat{R}_{\infty}^{\top} K_{\infty}^{-1} Y+\mathcal{O}\left(\beta^{-1}\right)=G_{x x}^{\top} G_{x x}^{-1} Y+\mathcal{O}\left(\beta^{-1}\right)=\hat{X} X^{\top}\left(X X^{\top}\right)^{-1} Y+\mathcal{O}\left(\beta^{-1}\right)
$$

respectively. The training and test set covariances have low-temperature limits of

$$
\operatorname{cov}\left(F_{\mu j}, F_{\nu k}\right)=\mathcal{O}\left(\beta^{-1}\right)
$$

and

$$
\begin{aligned}
\operatorname{cov}\left(\hat{F}_{\hat{\mu} j}, \hat{F}_{\hat{\nu} k}\right)= & \sigma_{d}^{2}\left(\hat{K}_{\infty}-\hat{R}_{\infty}^{\top} K_{\infty}^{-1} \hat{R}_{\infty}\right)_{\hat{\mu} \hat{\nu}}\left[\delta_{j k}+\left(\sum_{\ell=1}^{d-1} \frac{1}{n_{\ell}}\right)\left(\sigma_{d}^{-2} Y^{\top} K_{\infty}^{-1} Y-p I_{n_{2}}\right)_{j k}\right] \\
& +\mathcal{O}\left(\beta^{-1}, n^{-2}\right)
\end{aligned}
$$

respectively. Then, it is easy to see that both $E_{b}$ and $E_{v}$ are $\mathcal{O}\left(\beta^{-1}\right)$, while

$$
\hat{E}_{b}=\frac{1}{2}\left\|\hat{R}_{\infty}^{\top} K_{\infty}^{-1} Y-\hat{Y}\right\|_{F}^{2}+\mathcal{O}\left(\beta^{-1}\right)
$$

and

$$
\begin{aligned}
\hat{E}_{v}= & \frac{1}{2} n_{d} \sigma_{d}^{2} \operatorname{tr}\left(\hat{K}_{\infty}-\hat{R}_{\infty}^{\top} K_{\infty}^{-1} \hat{R}_{\infty}\right)\left[1+\left(\sum_{\ell=1}^{d-1} \frac{1}{n_{\ell}}\right)\left(\sigma_{d}^{-2} \operatorname{tr}\left(K_{\infty}^{-1} G_{y y}\right)-p\right)\right] \\
& +\mathcal{O}\left(\beta^{-1}, n^{-2}\right)
\end{aligned}
$$

Thus, at least to leading order, width affects the low-temperature test error only through the variance term. Substituting in the definition of $K_{\infty}$, we find that to leading order the test error decreases with increasing width if

$$
\frac{1}{p} \operatorname{tr}\left(G_{x x}^{-1} G_{y y}\right)>\sigma_{1}^{2} \cdots \sigma_{d}^{2}
$$

and increases with increasing width otherwise. This small-initialization condition is the generalization of that found by Li and Sompolinsky [16] to our asymptotic regime.

# G. 3 Effects of alternative regularization temperature-dependence 

In this appendix, we comment on the possibility of alternative temperature-dependent posteriors. This possibility arises from the interpretation of the Bayes posterior (3) as the equilibrium distribution of the Langevin dynamics

$$
d \Theta^{(\ell)}(t)=-\left(\lambda(\beta) \Sigma \Theta+\nabla_{\Theta} E\right) d t+\sqrt{2 \beta^{-1}} d B^{(\ell)}(t)
$$

at inverse temperature $\beta$, where $B^{(\ell)}(t)$ is a standard Wiener process, $\Sigma$ is the diagonal matrix of prior variances, and $\lambda(\beta)=1 / \beta$. As elsewhere, we focus on the regime in which the training dataset can be linearly interpolated, in which the thermal variance of the test set predictions need not vanish. Moreover, it suffices to consider only the GP contributions; the finite-width corrections computed above do not change the qualitative results. In these statistics, the case of general $\lambda(\beta)$ is related to $\lambda(\beta)=1 / \beta$ by the replacement

$$
\sigma_{1}^{2} \cdots \sigma_{d}^{2} \leftarrow \frac{\sigma_{1}^{2} \cdots \sigma_{d}^{2}}{\beta^{d} \lambda(\beta)^{d}}
$$

Then, if we assume a low-temperature power-law dependence $\lambda(\beta) \sim \beta^{\omega}$ for simplicity, we find that the zero-temperature limits of the training set predictor mean and covariance are

$$
\lim _{\beta \rightarrow \infty}\langle F\rangle= \begin{cases}0 & \omega>1 / d-1 \\ K_{\infty}\left(\sigma_{d}^{-2} I_{p}+K_{\infty}\right)^{-1} Y & \omega=1 / d-1 \\ Y & \omega<1 / d-1\end{cases}
$$

and

$$
\lim _{\beta \rightarrow \infty} \operatorname{cov}\left(F_{\mu j}, F_{\nu k}\right)=0
$$

respectively, while those of the test set mean and covariance are

$$
\lim _{\beta \rightarrow \infty}\langle\hat{F}\rangle= \begin{cases}0 & \omega>1 / d-1 \\ \hat{R}_{\infty}^{\top}\left(\sigma_{d}^{-2} I_{p}+K_{\infty}\right)^{-1} Y & \omega=1 / d-1 \\ \hat{R}_{\infty}^{\top} K_{\infty}^{-1} Y & \omega<1 / d-1\end{cases}
$$

and

$$
\lim _{\beta \rightarrow \infty} \operatorname{cov}\left(\hat{F}_{\hat{\mu} j}, \hat{F}_{\hat{\nu} k}\right)= \begin{cases}0 & \omega>-1 \\ \sigma_{d}^{2}\left(\hat{K}_{\infty}-\hat{R}^{\top} K_{\infty}^{-1} \hat{R}_{\infty}\right)_{\hat{\mu} \hat{\nu}} \delta_{j k} & \omega=-1 \\ \infty & \omega<-1\end{cases}
$$

respectively. Therefore, taking $\lambda(\beta)=1 / \beta$ yields sensible zero-temperature infinite-width behavior for a linear network of any depth in the underdetermined regime.

# H Derivation of the average kernels for a depth-two network 

In this appendix, we derive the average feature kernel for a network with a single (possibly nonlinear) hidden layer and a linear readout. This derivation is a simple extension of the perturbative derivation of Conjecture 1 in Appendix B, using the fact that the size of the terms in the expansion for two-layer networks can be directly controlled in terms of the inverse hidden layer width.

Concretely, we consider a network defined as

$$
\begin{aligned}
\mathbf{h}^{(1)} & =\frac{\sigma_{1}}{\sqrt{n_{0}}} W^{(1)} \mathbf{x} \\
\mathbf{h}^{(2)} & =\frac{\sigma_{2}}{\sqrt{n_{1}}} W^{(2)} \phi\left(\mathbf{h}^{(1)}\right) \\
\mathbf{f} & =\mathbf{h}^{(2)}
\end{aligned}
$$

Our task is to control the prior cumulants of the hidden layer feature kernel

$$
K_{\mu \nu} \equiv \frac{1}{n_{1}} \phi\left(\mathbf{h}_{\mu}^{(1)}\right) \cdot \phi\left(\mathbf{h}_{\nu}^{(1)}\right)
$$

We can use the fact that the rows $\left[\mathbf{w}_{j}^{(1)}\right]^{\top}$ of $W^{(1)}$ are independent and identically distributed under the prior to obtain

$$
\begin{aligned}
{\left[K_{\infty}\right]_{\mu \nu} } & =\mathbb{E}_{\mathcal{W}} K_{\mu \nu} \\
& =\frac{1}{n_{1}} \sum_{j=1}^{n_{1}} \mathbb{E}_{\mathbf{w}_{j}^{(1)}}\left[\phi\left(\frac{\sigma_{1}}{\sqrt{n_{0}}} \mathbf{w}_{j}^{(1)} \cdot \mathbf{x}_{\mu}\right) \phi\left(\frac{\sigma_{1}}{\sqrt{n_{0}}} \mathbf{w}_{j}^{(1)} \cdot \mathbf{x}_{\nu}\right)\right] \\
& =\mathbb{E}\left[\phi\left(h_{\mu}^{(1)}\right) \phi\left(h_{\nu}^{(1)}\right): \mathbf{h}^{(1)} \sim \mathcal{N}\left(\mathbf{0}, \sigma_{1}^{2} G_{x x}\right)\right]
\end{aligned}
$$

at any hidden layer width [3, 4]. Similarly, we can easily see that

$$
\operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu}, K_{\rho \lambda}\right)=\frac{1}{n_{1}}\left(\mathbb{E}\left[\phi\left(h_{\mu}^{(1)}\right) \phi\left(h_{\nu}^{(1)}\right) \phi\left(h_{\rho}^{(1)}\right) \phi\left(h_{\lambda}^{(1)}\right)\right]-\left[K_{\infty}\right]_{\mu \nu}\left[K_{\infty}\right]_{\rho \lambda}\right)
$$

where $\mathbf{h}^{(1)} \sim \mathcal{N}\left(\mathbf{0}, \sigma_{1}^{2} G_{x x}\right)$, and that higher cumulants are $\mathcal{O}\left(n_{1}^{-2}\right)$. Then, we can directly apply the result of Appendix B to conclude that

$$
\left\langle K_{\mu \nu}\right\rangle=\left[K_{\infty}\right]_{\mu \nu}+\frac{1}{2} n_{d} \sum_{\rho, \lambda=1}^{p}\left(\sigma_{d}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right)_{\rho \lambda} \operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu}, K_{\rho \lambda}\right)+\mathcal{O}\left(n_{1}^{-2}\right)
$$

for $\Gamma=\sigma_{1}^{2} K_{\infty}+I_{p} / \beta \sigma_{2}^{2}$. Depending on the nonlinearity, this result may be continuous in $G_{x x}$, and therefore extensible to the non-invertible case via a continuity argument. In particular, as noted in Appendix D, this holds for a linear network.
To gain some intuition for how different choices of nonlinear activation function affect the learned representations, we consider the case in which $G_{x x}$ is diagonal. In this special case, the four-point term simplifies dramatically. In particular, we have

$$
\left(K_{\infty}\right)_{\mu \nu}=\operatorname{var}\left[\phi\left(h_{\mu}^{(1)}\right)\right] \delta_{\mu \nu}+\mathbb{E}\left[\phi\left(h_{\mu}^{(1)}\right)\right] \mathbb{E}\left[\phi\left(h_{\nu}^{(1)}\right)\right]
$$

and

$$
\begin{aligned}
\operatorname{cov}_{\mathcal{W}}\left(K_{\mu \nu}, K_{\rho \lambda}\right)= & \frac{1}{n_{1}}\left(\operatorname{var}\left[\phi\left(h_{\mu}^{(1)}\right)^{2}\right] \delta_{\mu \nu} \delta_{\mu \rho} \delta_{\mu \lambda}\right. \\
& \left.+\operatorname{var}\left[\phi\left(h_{\mu}^{(1)}\right)\right] \operatorname{var}\left[\phi\left(h_{\nu}^{(1)}\right)\right]\left(1-\delta_{\mu \nu}\right)\left(\delta_{\mu \rho} \delta_{\nu \lambda}+\delta_{\mu \lambda} \delta_{\nu \rho}\right)\right)
\end{aligned}
$$

which yields

$$
\begin{aligned}
& \left\langle K_{\mu \nu}\right\rangle=\left(K_{\infty}\right)_{\mu \nu}+\frac{1}{2} \frac{n_{2}}{n_{1}}\left(\sigma_{2}^{-2} \Gamma^{-1} G_{y y} \Gamma^{-1}-\Gamma^{-1}\right)_{\mu \nu} \\
& \times\left[\operatorname{var}\left[\phi\left(h_{\mu}^{(1)}\right)^{2}\right] \delta_{\mu \nu}+2 \operatorname{var}\left[\phi\left(h_{\mu}^{(1)}\right)\right] \operatorname{var}\left[\phi\left(h_{\nu}^{(1)}\right)\right]\left(1-\delta_{\mu \nu}\right)\right]+\mathcal{O}\left(n_{1}^{-2}\right)
\end{aligned}
$$

Moreover, applying the Sherman-Morrison formula [27], we have

$$
\frac{1}{\beta \sigma_{2}^{2}} \Gamma_{\mu \nu}^{-1}=\frac{\delta_{\mu \nu}}{\gamma_{\mu}}-\frac{1}{1+\sum_{\rho=1}^{p} \mathbb{E}\left[\phi\left(h_{\rho}^{(1)}\right)\right]^{2} / \gamma_{\rho}} \frac{\mathbb{E}\left[\phi\left(h_{\rho}^{(1)}\right)\right]}{\gamma_{\mu}} \frac{\mathbb{E}\left[\phi\left(h_{\nu}^{(1)}\right)\right]}{\gamma_{\nu}}
$$

where we have defined the vector $\gamma_{\mu} \equiv 1+\beta \sigma_{2}^{2} \operatorname{var}\left[\phi\left(h_{\mu}^{(1)}\right)\right]$ for brevity. Thus, in this simple setting, activation functions with $\mathbb{E} \phi(h) \neq 0$ yield qualitatively different behavior from those with $\mathbb{E} \phi(h)=0$ : non-vanishing $\mathbb{E} \phi(h)$ introduces a rank-1 component in the GP kernel, which in turn couples elements of $G_{y y}$ in the leading finite-width correction.

# I Numerical methods 

In this appendix, we describe the numerical methods used in our experiments. We perform our simulations by sampling network parameters at each time step of the Langevin update G. 21 after some large burn-in period when the loss function stabilizes around a fixed number. We used EulerMaruyama method [30] to obtain the discretized Langevin equation:

$$
\Theta(t+1)-\Theta(t)=-\beta^{-1} \Theta(t) d t-\nabla_{\Theta} E(t) d t+\xi \sqrt{2 \beta^{-1} d t}
$$

where $\xi \sim \mathcal{N}(0,1)$ is a standard Gaussian random variable sampled i.i.d. at each time step and $d t$ is the time step. The first, second and last terms represent the weight decay, the gradient descent update and the stochastic Wiener process, respectively.
We used the Neural Tangents framework [33] and PyTorch deep learning library [31] to generate the neural networks and trained them according to the discretized full-batch Langevin update rule. A typical burn-in time was $\sim 2 \times 10^{6}$ iterations and after that the parameters were sampled over $\sim 2 \times 10^{6}$ iterations where we chose a learning rate of $d t \sim 10^{-4}$. Simulations have been performed on a cluster with NVIDIA Tesla V100 GPU's with 32 GB RAM and a typical simulation run took $\sim 2-6 \mathrm{hr}$ depending on the architecture and the network width. All code used throughout this work can be reached at https://github.com/Pehlevan-Group/finite-width-bayesian/.
All figures shown here are results of a single instance of a trained neural network on a fixed dataset. Since we performed all our experiments with $\beta=1$, we observed that the different initializations of a network did not influence the final posterior mean due to the weight decay and long burn-in periods.
Throughout all experiments, the MNIST digits were downsized from $28 \times 28$ pixels to $10 \times 10$ pixels without distorting the original digits. This was done to accelerate the training process since large input dimensions would take an order of magnitude more time to obtain well estimated posterior means. We considered 10-dimensional outputs corresponding to one-hot encoded digits. Both inputs and labels were ordered according to their class. Figure 2 shows an example of MNIST digits and the input $G_{x x}$ and output $G_{y y}$ Gram matrices.