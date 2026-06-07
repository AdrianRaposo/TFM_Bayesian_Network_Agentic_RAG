# Modulation Classification for MIMO-OFDM Signals via Approximate Bayesian Inference 

Yu Liu, Osvaldo Simeone, Fellow, IEEE, Alexander M. Haimovich, Fellow, IEEE, Wei Su, Fellow, IEEE


#### Abstract

The problem of modulation classification for a multiple-antenna (MIMO) system employing orthogonal frequency division multiplexing (OFDM) is investigated under the assumption of unknown frequency-selective fading channels and signal-to-noise ratio (SNR). The classification problem is formulated as a Bayesian inference task, and solutions are proposed based on Gibbs sampling and mean field variational inference. The proposed methods rely on a selection of the prior distributions that adopts a latent Dirichlet model for the modulation type and on the Bayesian network formalism. The Gibbs sampling method converges to the optimal Bayesian solution and, using numerical results, its accuracy is seen to improve for small sample sizes when switching to the mean field variational inference technique after a number of iterations. The speed of convergence is shown to improve via annealing and random restarts. While most of the literature on modulation classification assume that the channels are flat fading, that the number of receive antennas is no less than that of transmit antennas, and that a large number of observed data symbols are available, the proposed methods perform well under more general conditions. Finally, the proposed Bayesian methods are demonstrated to improve over existing non-Bayesian approaches based on independent component analysis and on prior Bayesian methods based on the 'superconstellation' method.


Index Terms-Bayesian inference; Modulation classification; MIMO-OFDM; Gibbs sampling; Mean field variational inference; Latent Dirichlet model.

## I. INTRODUCTION

Cognitive radio is a wireless communication technology that addresses the inefficiency of the radio resource usage via computational intelligence [1], [2]. Cognitive radios have both civilian and military applications [3]. A major task in such radios is the classification of the modulation format of unknown received signals. As the pairing of multiple-antenna (MIMO) transmission and orthogonal frequency division multiplexing (OFDM) data modulation has become central to fourth generation (4G) and fifth generation (5G) wireless technologies, a need has arisen for the development of new classification algorithms capable of handling MIMO-OFDM signals.

Modulation classification methods are generally classified as inference-based or pattern recognition-based [3]. The

[^0]inference-based approaches fall into two categories, namely Bayesian and non-Bayesian methods [4]. Bayesian methods model unknown parameters as random variables with some prior distributions, and aim to evaluate the posterior probability of the modulation type. Non-Bayesian methods, instead, model unknown parameters as nuisance variables that need to be estimated before performing modulation classification. With pattern recognition-based methods, specific features are extracted from the received signal and then used to discriminate among the candidate modulations. Compared to the pattern recognition-based approaches, inference-based methods generally achieve better classification performance at the cost of a higher computational complexity [3].

There is ample literature on classification algorithms for single-antenna (SISO) systems [3], [5]-[20]. Among them, a Bayesian method using Gibbs sampling is proposed in [19]. In [20], a systematic Bayesian solution based on the latent Dirichlet Bayesian Network (BN) is proposed, which generalizes and improves upon the work in [19]. A preprocessor for modulation classification is developed in [21], whereby the timing offset is estimated using grid-based Gibbs sampling ${ }^{1}$. We note that, while most algorithms rely on the assumption that the channels are flat fading or additive white Gaussian noise channels, the approaches in [19]-[21] are well-suited also for frequency selective fading channels.

Only few publications address modulation classification in MIMO systems [22]-[26]. The task of modulation classification for MIMO is more challenging than for SISO due to the mutual interference between the received signals and to the multiplicity of unknown channels. In [22], a non-Bayesian approach, referred to as independent component analysis (ICA)phase correction (PC), is proposed, where the channel matrix required for the calculation of the hypotheses test is estimated blindly by ICA [27]. Several related pattern recognitionbased algorithms are introduced in [23]-[25], where source streams are separated by ICA-PC or a constant modulus algorithm, and diverse higher-order signal statistics are used as discriminating features. Moreover, a pattern recognitionbased algorithm using spatial and temporal correlation functions as distinctive features is reported in [26] for MIMO frequency-selective channels with time-domain transmission. The approach is not applicable to modulation classification for MIMO-OFDM systems. As for MIMO-OFDM systems, a non-Bayesian approach is proposed in [28] based on ICA-PC and an assumed invariance of the frequency-domain channels

[^1]
[^0]:    Copyright (c) 2015 IEEE. Personal use of this material is permitted. However, permission to use this material for any other purposes must be obtained from the IEEE by sending a request to pubs-permissions@ieee.org. Y. Liu, O. Simeone and A. M. Haimovich are with the Center for Wireless Communications and Signal Processing Research (CWCSPR), ECE Department, New Jersey Institute of Technology (NJIT), Newark, NJ 07102, USA (email: [y1227, osvaldo.simeone, haimovic] @njit.edu).
    W. Su is with the U.S. Army Communication-Electronics Research Development and Engineering Center, I2WD, Aberdeen Proving Ground, MD 21005, USA (email: wei.su@ieee.org).

    DISTRIBUTION STATEMENT A: Approved for public release, distribution is unlimited

[^1]:    ${ }^{1}$ In grid-based Gibbs sampling, a grid of points is first selected within the domain of a variable $x$ to be sampled. Then the conditional probability density function (normalized or non-normalized) of variable $x$ is computed at each selected point, which is used for sampling $x$.

across the coherence bandwidth. It is finally noted that the results in this paper were partially presented in [29].

Main Contributions: In this work, we develop Bayesian modulation classification techniques for MIMO-OFDM systems operating over frequency-selective fading channels, assuming unknown channels and signal-to-noise ratio (SNR). Our main contributions are as follows.

1) A modulation classification technique is proposed based on Gibbs sampling for MIMO-OFDM systems. Inspired by the latent Dirichlet models in machine learning [30], this approach leverages a novel selection of the prior distributions for the unknown variables, the modulation format and the transmitted symbols. This selection was first adopted by some of the authors in [20] for SISO systems. As compared to SISO systems, a Gibbs sampling implementation such as in [20] may have an impractically slow convergence due to the high-dimensional and multimodal distributions in MIMO systems. The strategy of annealing [31]-[33] combined with multiple random restarts [34]-[37] is hence proposed here to improve the convergence speed.
2) An alternative Bayesian solution for modulation classification in MIMO-OFDM systems that leverages mean field variational inference [38] is proposed, based on the same latent Dirichlet prior selection.
3) A hybrid approach that switches from Gibbs sampling to mean field variational inference is proposed for modulation classification in MIMO-OFDM systems. The hybrid approach is motivated by the fact that the Gibbs sampler is superior to mean field as a method for exploring the global solution space, while the mean field algorithm has better convergence speed in the vicinity of a local optima [38]-[40].
4) Extensive numerical results demonstrate that the proposed Gibbs sampling method converges to an effective solution, and its accuracy improves for small sample sizes when switching to the mean field variational inference technique after a number of iterations. Moreover, the speed of convergence is seen to be generally improved by multiple random restarts and annealing [31]-[37]. Overall, while most of the reviewed existing modulation classification algorithms for MIMO-OFDM systems work under the assumptions that the channels are flat fading [22]-[25], that the number of receive antennas is no less than the number of transmit antennas [22]-[25], and/or that the number of samples is large (as for pattern recognition-based methods) [23]-[26], the proposed method achieves satisfactory performance under more general conditions.

The rest of the paper is organized as follows. The signal model is introduced in Sec. II. In Sec. III, we briefly review some necessary preliminary concepts, including Bayesian inference and BNs, while in Sec. IV, we formulate the modulation classification problem under study as a Bayesian inference task, and propose solutions based on Gibbs sampling and on mean field variational inference. Numerical results of the proposed methods are presented in Sec. V. Finally, conclusions
are drawn in Sec. VI.
Notation: The superscripts $T$ and $H$ denote matrix or vector transpose and Hermitian, respectively. The $i$-th row of the matrix $\mathbf{B}$ is denoted as $\mathbf{B}_{(i, \cdot)}$ and the $j$-th column is denoted as $\mathbf{B}_{(\cdot, j)}$. Lower case bold letters and upper case bold letters are used to denote column vectors and matrices, respectively. The notation $\mathbf{b} \backslash b_{i}$, where $\mathbf{b}=\left[b_{1}, \ldots, b_{n}\right]^{T}$ and $i \in\{1, \ldots, n\}$, denotes the vector composed of all the elements of $\mathbf{b}$ except $b_{i}$. We use an angle bracket $\langle\cdot\rangle$, to represent the expectation with respect to the random variables indicated in the subscript. For notational simplicity, we do not indicate the variables in the subscript when the expectation is taken with respect to all the random variables inside the bracket $\langle\cdot\rangle$, The notations $\psi(\cdot)$ and $\mathbf{1}(\cdot)$ stand for the digamma function [41] and the indicator function, respectively. The cardinality of a set $\mathcal{B}$ is denoted $|\mathcal{B}|$. We use the same notation, $p(\cdot)$, for both probability density functions (pdf) and probability mass function (pmf). Moreover, we will identify a pdf or pmf by its arguments, e.g., $p(X \mid Y)$ represents the distribution of random variable $X$ given the random variable $Y$. The notations $\mathcal{C N}(\boldsymbol{\mu}, \mathbf{C})$ and $\mathcal{I G}(a, b)$ represent the the circularly symmetric complex Gaussian distribution with mean vector $\boldsymbol{\mu}$ and covariance matrix $\mathbf{C}$ and the inverse gamma distribution with shape parameter $a$ and scale parameter $b$, respectively.

## II. SYSTEM MODEL

Consider a MIMO-OFDM system operating over a frequency-selective fading channel with $N$ subcarriers, $M_{t}$ transmit antennas, $M_{r}$ receive antennas and a coherence period of $K$ OFDM symbols. All frequency-domain symbols transmitted during the coherence period are taken from a finite constellation $A \in \mathcal{A}$, such as $M$-PSK or $M$-QAM, where $\mathcal{A}$ is the (finite) set containing all possible constellations. Without loss of generality, $A$ is assumed to be a constellation of symbols with average power equal to 1 . The number of transmit antennas $M_{t}$ is assumed known. We observe that several algorithms have been proposed for the estimation of $M_{t}$ [42], [43]. We focus on the problem of detecting the constellation $A$ in the absence of information about the SNR, the transmitted symbols and the fading channel coefficients.

After matched filtering and sampling, assuming that time synchronization has been successfully performed at least within the error margin afforded by the cyclic prefix, the frequency-domain samples $\mathbf{y}[n, k]=\left[y_{1}[n, k], \ldots, y_{M_{r}}[n, k]\right]^{T}$, received across the $M_{r}$ receive antennas, at the $n$-th subcarrier of the $k$-th OFDM frame, are expressed as

$$
\mathbf{y}[n, k]=\mathbf{H}[n] \mathbf{s}[n, k]+\mathbf{z}[n, k]
$$

where $\mathbf{H}[n]$ is the $M_{r} \times M_{t}$ frequency-domain channel matrix associated with the $n$-th subcarrier; $\mathbf{s}[n, k]$ is the $M_{t} \times 1$ vector composed of the symbols transmitted by the $M_{t}$ antennas, i.e., $\mathbf{s}[n, k]=\left[s_{1}[n, k], \ldots, s_{M_{t}}[n, k]\right]^{T}$, with $s_{m_{t}}[n, k] \in A$ being the symbol transmitted by the $m_{t}$-th transmit antenna over the $n$-th subcarrier of the $k$-th OFDM symbol; and $\mathbf{z}[n, k]=\left[z_{1}[n, k], \ldots, z_{M_{r}}[n, k]\right]^{T} \sim \mathcal{C N}\left(\mathbf{0}, \sigma^{2} \mathbf{I}\right)$ is complex

white Gaussian noise, which is independent over indices $n$ and $k$. The frequency-domain channel matrix $\mathbf{H}[n]$ can be written

$$
\mathbf{H}[n]=\left[\begin{array}{ccc}
\tilde{h}_{1,1}[n] & \cdots & \tilde{h}_{M_{t}, 1}[n] \\
\vdots & \ddots & \vdots \\
\tilde{h}_{1, M_{r}}[n] & \cdots & \tilde{h}_{M_{t}, M_{r}}[n]
\end{array}\right]
$$

where $\tilde{\mathbf{h}}_{m_{t}, m_{r}}=\left[\tilde{h}_{m_{t}, m_{r}}[1], \ldots, \tilde{h}_{m_{t}, m_{r}}[N]\right]^{T}$ denotes the $N \times 1$ frequency-domain channel vector between the $m_{t}$-th transmit antenna and the $m_{r}$-th receive antenna. Assuming that the channel for any pair $\left(m_{t}, m_{r}\right)$ has at most $L$ symbolspaced taps, we write $\tilde{\mathbf{h}}_{m_{t}, m_{r}}=\mathbf{W} \mathbf{h}_{m_{t}, m_{r}}$, with $\mathbf{h}_{m_{t}, m_{r}}$ the $L \times 1$ time-domain channel vector and $\mathbf{W}$ the $N \times L$ matrix composed of the first $L$ columns of the DFT matrix of size $N$. Note that the channel is fixed within the coherence frame of $K$ OFDM symbols.

According to (1) and (2), the $N K \times 1$ received frequencydomain signals $\mathbf{y}_{m_{r}}=\left[\mathbf{y}_{m_{r}}[1]^{T}, \ldots, \mathbf{y}_{m_{r}}[K]^{T}\right]^{T}$ at the $m_{r}$-th receive antenna is given by

$$
\mathbf{y}_{m_{r}}=\sum_{m_{t}=1}^{M_{t}} \mathbf{D}_{m_{t}} \tilde{\mathbf{h}}_{m_{t}, m_{r}}+\mathbf{z}_{m_{r}}, m_{r}=1, \ldots, M_{r}
$$

where $\quad \mathbf{y}_{m_{r}}[k] \quad=\quad\left[y_{m_{r}}[1, k], \ldots, y_{m_{r}}[N, k]\right]^{T}$; $\mathbf{D}_{m_{t}}=\left[\mathbf{D}_{m_{t}, 1}, \ldots, \mathbf{D}_{m_{t}, K}\right]^{T}$ is an $N K \times N$ matrix representing the transmitted symbols with $\mathbf{D}_{m_{t}, k}$ an $N \times N$ diagonal matrix whose $(n, n)$ element is $s_{m_{t}}[n, k] ;$ and $\mathbf{z}_{m_{r}}=\left[\mathbf{z}_{m_{r}}[1]^{T}, \ldots, \mathbf{z}_{m_{r}}[K]^{T}\right]^{T}$ with $\mathbf{z}_{m_{r}}[k]=\left[z_{m_{r}}[1, k], \ldots, z_{m_{r}}[N, k]\right]^{T}$.

Let us further define the $N K M_{t} \times 1$ vector $\mathbf{s}=$ $\left[\mathbf{s}_{1}, . ., \mathbf{s}_{K}\right]^{T}$ containing all the transmitted symbols with $\mathbf{s}_{k}=[\mathbf{s}[1, k]^{T}, \ldots, \mathbf{s}[N, k]^{T}]^{T} ;$ the $L M_{t} M_{r} \times 1$ vector $\mathbf{h}=\left[\mathbf{h}_{1}^{T}, \ldots, \mathbf{h}_{M_{r}}^{T}\right]^{T}$ for the time domain channels associated with all the transmit-receive antenna pairs, where $\mathbf{h}_{m_{r}}=$ $\left[\mathbf{h}_{1, m_{r}}^{T}, \ldots, \mathbf{h}_{M_{t}, m_{r}}^{T}\right]^{T}$; and the $N K M_{r} \times 1$ receive signal vector $\mathbf{y}=\left[\mathbf{y}_{1}^{T}, \ldots, \mathbf{y}_{M_{r}}^{T}\right]^{T}$. The task of modulation classification is for the receiver to correctly detect the modulation format $A$ given only the received samples $\mathbf{y}$, while being uninformed about the symbols $\mathbf{s}$, the channel $\mathbf{h}$ and the noise power $\sigma^{2}$. Using (1) and (3), the likelihood function $p\left(\mathbf{y} \mid A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)$ of the observation is given by

$$
\begin{aligned}
& p\left(\mathbf{y} \mid A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right) \\
= & \prod_{n, k} p\left(\mathbf{y}[n, k] \mid \mathbf{s}[n, k], \mathbf{H}[n], \sigma^{2}\right) \\
= & \prod_{m_{r}} p\left(\mathbf{y}_{m_{r}} \mid \mathbf{s}, \mathbf{h}_{m_{r}}, \sigma^{2}\right)
\end{aligned}
$$

with $\mathbf{y}_{m_{r}} \mid\left(\mathbf{s}, \mathbf{h}_{m_{r}}, \sigma^{2}\right) \sim \mathcal{C N}\left(\sum_{m_{t-1}}^{M_{t}} \mathbf{D}_{m_{t}} \mathbf{W} \mathbf{h}_{m_{t}, m_{r}}, \sigma^{2} \mathbf{I}\right)$ and $\mathbf{y}[n, k] \mid\left(\mathbf{s}[n, k], \mathbf{H}[n], \sigma^{2}\right) \sim \mathcal{C N}(\mathbf{H}[n] \mathbf{s}[n, k], \sigma^{2} \mathbf{I})$.

## III. Preliminaries

As formalized in the next section, in this paper we formulate the modulation classification problem as a Bayesian inference task. In this section, we review some necessary preliminary concepts. Specifically, we start by introducing the general task of Bayesian inference in Sec. III-A; we review the definition of BN, which is a useful graphical tool to represent knowledge
about the structure of a joint distribution, in Sec. III-B; and, finally, we review approximate solutions to the Bayesian inference task, namely, Gibbs sampling in Sec. III-C, and mean field variational inference in Sec. III-D.

## A. Bayesian Inference

Bayesian inference aims to compute the posterior probability of the variables of interest given the evidence, where the evidence is a subset of the random variables in the model. Specifically, given the values of some evidence variables $\boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}$, one wishes to estimate the posterior distribution of a subset of the unknown variables $\boldsymbol{\Theta}_{u}=\left[\Theta_{1}, \ldots, \Theta_{G}\right]^{T}$. We assume here for simplicity of exposition that all variables are discrete with finite cardinality. However, the extension to continuous variables with pdfs is immediate, as it will be argued. The conditional pmf of $\boldsymbol{\Theta}_{u}$ given the evidence $\boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}$ is proportional to the product of a prior distribution $p\left(\boldsymbol{\Theta}_{u}\right)$ on the unknown variables $\boldsymbol{\Theta}_{u}$ and of the likelihood of the evidence $p\left(\boldsymbol{\Theta}_{e} \mid \boldsymbol{\Theta}_{u}\right)$ :

$$
p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}\right) \propto p\left(\boldsymbol{\Theta}_{u}\right) p\left(\boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e} \mid \boldsymbol{\Theta}_{u}\right)
$$

If one is interested in computing the posterior distribution of the unknown variable $\Theta_{j}$, then a direct approach would be to write

$$
p\left(\Theta_{j}=\theta_{j} \mid \boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}\right)=\sum_{\boldsymbol{\theta}_{u} \backslash \theta_{j}} p\left(\boldsymbol{\Theta}_{u}=\boldsymbol{\theta}_{u} \mid \boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}\right)
$$

The inference task (6) is made difficult in practice by the multidimensional summation over all the values of the variables $\boldsymbol{\Theta}_{u} \backslash \Theta_{j}$. Note also that, if the variables are continuous, the operation of summation is replaced by integration and a similar discussion applies. Next, we discuss the BN model.

## B. Bayesian Network

A BN is an acyclic graph that can be used to represent useful aspects of the structure of a joint distribution. Each node in the graph represents a random variable, while the directed edges between the nodes encode the probabilistic influence of one variable on another. Node $\Theta_{i}$ is defined to be a parent of $\Theta_{j}$, if an edge from node $\Theta_{i}$ to node $\Theta_{j}$ exists in the graph. According to the BN's chain rule [38], the influence encoded in a BN for a set of variables $\boldsymbol{\Theta}=\left[\Theta_{1}, \ldots, \Theta_{J}\right]^{T}$ can be interpreted as the factorization of the joint distribution in the form

$$
p(\boldsymbol{\Theta})=\prod_{j=1}^{J} p\left(\Theta_{j} \mid \mathrm{Pa}_{\Theta_{j}}\right)
$$

where we use $\mathrm{Pa}_{\Theta_{j}}$ to denote the set of parent variables of variable $\Theta_{j}$. Note that (7) encodes the fact that each variable $\Theta_{j}$ is independent of its ancestors in the BN, when conditioning on its parent variables $\mathrm{Pa}_{\Theta_{j}}$. In the following, we will find it useful to rewrite (7) in a more abstract way as [38]

$$
p(\boldsymbol{\Theta})=\prod_{\phi} \phi\left(\mathcal{B}_{\phi}\right)
$$

where the product is taken over all $J$ factor $\phi\left(\mathcal{B}_{\phi}\right)=$ $p\left(\Theta_{j} \mid \mathrm{Pa}_{\Theta_{j}}\right)$ with $\mathcal{B}_{\phi}=\left\{\Theta_{j}, \mathrm{Pa}_{\Theta_{j}}\right\}$.

## C. Gibbs Sampling

Markov chain Monte Carlo (MCMC) techniques provide effective iterative approximate solutions to the Bayesian inference task (6) that are based on randomization and can obtain increasingly accurate posterior distributions as the number of iterations increases. The goal of these techniques is to generate $M$ random samples $\boldsymbol{\theta}_{u}^{(1)}, \ldots, \boldsymbol{\theta}_{u}^{(M)}$ from the desired posterior distribution $p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}\right)$. This is done by running a Markov chain whose equilibrium distribution is $p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}\right)$. As a result, according to the law of large numbers, the multidimensional summation (or integration) (6) can be approximated by an ensemble average. In particular, the marginal distribution of any particular variable $\Theta_{j}$ in $\boldsymbol{\Theta}_{u}$ can be estimated as

$$
p\left(\Theta_{j}=\theta_{j} \mid \boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}\right) \approx \frac{1}{M} \sum_{m=M_{0}+1}^{M} \mathbf{1}\left(\theta_{j}^{(m)}=\theta_{j}\right)
$$

where $\theta_{j}^{(m)}$ is the $m$-th sample for $\Theta_{j}$ generated by the Markov chain, and $M_{0}$ denotes the number of samples used as burn-in period to reduce the correlations with the initial values [35].

Gibbs sampling is a classical MCMC algorithm that defines the aforementioned Markov chain by sampling all the variables in $\boldsymbol{\Theta}_{u}$ one-by-one. Specifically, the algorithm begins with a set of arbitrary feasible values for $\boldsymbol{\Theta}_{u}$. Then, at step $m$, a sample for a given variable $\Theta_{j}$ is drawn from the conditional distribution $p\left(\Theta_{j} \mid \boldsymbol{\Theta}_{u} \backslash \Theta_{j}, \boldsymbol{\Theta}_{e}\right)$. Whenever a sample is generated for a variable, the value of that variable is updated within the vector $\boldsymbol{\Theta}_{u}$. It can be shown that the required conditional distributions $p\left(\Theta_{j} \mid \boldsymbol{\Theta}_{u} \backslash \Theta_{j}, \boldsymbol{\Theta}_{e}\right)$ may be calculated by multiplying all the factors in the factorization (8) that contain the variable of interest and then normalizing the resulting distribution, i.e., we have

$$
p\left(\Theta_{j} \mid \boldsymbol{\Theta}_{u} \backslash \Theta_{j}, \boldsymbol{\Theta}_{e}\right) \propto \prod_{\phi: \Theta_{j} \in B_{\phi}} \phi\left(\mathcal{B}_{\phi}\right)
$$

where the right-hand side of (10) is the product of the factors in (8) that involve the variable $\Theta_{j}$.

Remark 1: In order for Markov chain Monte Carlo algorithms to converge to a unique equilibrium distribution, the associated Markov chain needs to be irreducible and aperiodic [38, Ch. 12]. In the context of the Gibbs sampling, a sufficient condition for asymptotic correctness of Gibbs sampling is that the distributions $p\left(\Theta_{j} \mid \boldsymbol{\Theta}_{u} \backslash \Theta_{j}, \boldsymbol{\Theta}_{e}\right)$ are strictly positive in their domains for all $j$.

Remark 2: When applying Gibbs sampling to practical problems, in particular those with high-dimensional and multimodal posterior distribution $p\left(\Theta_{j} \mid \boldsymbol{\Theta}_{u} \backslash \Theta_{j}, \boldsymbol{\Theta}_{e}\right)$, slow convergence may be encountered due to the local nature of the updates. One approach to address this issue is to run Gibbs sampling with multiple random restarts that are initialized with different feasible solutions [34]-[37]. Moreover, within each run, simulated annealing may be used to avoid low-probability "traps." Accordingly, the prior probability, or the likelihood, may be parametrized by a temperature parameter $T$, such that a large temperature implies a lower reliance on the evidence aimed at exploring more thoroughly the range of the variables.

Samples are generated, starting with a high temperature and ending with a low temperature [31]-[33].

## D. Mean Field Variational Inference

Mean field variational inference provides an alternative way to approach the Bayesian inference problem of calculating $p\left(\Theta_{j}=\theta_{j} \mid \boldsymbol{\Theta}_{e}=\boldsymbol{\theta}_{e}\right)$. The key idea of this method is that of searching for a distribution $q\left(\boldsymbol{\Theta}_{u}\right)$ that is closest to the desired posterior distribution $p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\theta}_{e}\right)$, in terms of the Kullback-Leibler (KL) divergence $\operatorname{KL}\left(q\left(\boldsymbol{\Theta}_{u}\right) \| p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\theta}_{e}\right)\right)$, within the class $\mathcal{Q}$ of distributions that factorize as the product of marginals, i.e., $q\left(\boldsymbol{\Theta}_{u}\right)=\prod_{j=1}^{G} q\left(\Theta_{j}\right)$ [38, Ch. 11]. The corresponding variational problem is given as

$$
\begin{gathered}
\underset{q}{\operatorname{minimize}} \mathrm{KL}\left(q\left(\boldsymbol{\Theta}_{u}\right) \| p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\theta}_{e}\right)\right) \\
\text { s.t. } q \in \mathcal{Q}
\end{gathered}
$$

By imposing the necessary optimality conditions for problem (11), one can prove that the mean field approximation $q\left(\boldsymbol{\Theta}_{u}\right)$ is locally optimal only if the proportionality [38]

$$
q\left(\Theta_{j}\right) \propto \exp \left\{\sum_{\phi: \Theta_{j} \in \mathcal{B}_{\phi}}\left\langle\ln \phi\left(\mathcal{B}_{\phi}\right)\right\rangle_{q\left(\mathcal{B}_{\phi} \backslash \Theta_{j}\right)}\right\}
$$

holds for all $j=1, . ., G$, where the expectation in (12) is taken with respect to the distribution $q\left(\mathcal{B}_{\phi} \backslash \Theta_{j}\right)=q\left(\boldsymbol{\Theta}_{u}\right) / q\left(\Theta_{j}\right)$. The idea of the mean field variational inference is to solve (12) by means of fixed-point iterations (see [38] for details). It can be shown that each iteration of (12) results in a better approximation $q$ to the target distribution $p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\theta}_{e}\right)$, hence guaranteeing convergence to a local optimum of problem (11) [38, Sec. 11.5.1]. Once an approximating distribution $q\left(\boldsymbol{\Theta}_{u}\right)$ is obtained, an approximation of the desired posterior $p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\theta}_{e}\right)$ can be obtained as $p\left(\boldsymbol{\Theta}_{u} \mid \boldsymbol{\theta}_{e}\right) \approx q\left(\boldsymbol{\Theta}_{u}\right)$, and the marginal posterior distribution may be approximated as $p\left(\Theta_{j} \mid \boldsymbol{\theta}_{e}\right) \approx q\left(\Theta_{j}\right)$.

## IV. BAYESIAN INFERENCE FOR MODULATION CLASSIFICATION

In this section, we solve the problem of detecting the modulation $A \in \mathcal{A}$ by adopting a Bayesian inference formulation. First, in Sec. IV-A, we discuss the problem of selecting a proper prior distribution, and argue that a latent Dirichlet model inspired by [30] and first used for modulation classification in [20], provides an effective choice. Then, based on this prior model, we develop two solutions, one based on Gibbs sampling, in Sec. IV-B, and the other based on mean field variational inference, in Sec. IV-C.

## A. Latent Dirichlet Bayesian Network

According to (5), the joint distribution of the unknown variables $\left(A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)$ may be expressed

$$
p\left(A, \mathbf{s}, \mathbf{h}, \sigma^{2} \mid \mathbf{y}\right) \propto p\left(\mathbf{y} \mid A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right) p\left(A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)
$$

where the likelihood function $p\left(\mathbf{y} \mid A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)$ is given in (4), and the term $p\left(A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)$ stands for the prior information

![img-0.jpeg](img-0.jpeg)

Figure 1. BN $\mathcal{G}_{1}$ for the modulation classification scheme based on the factorization (13). The nodes inside the rectangle are repeated $N K$ times.
on the unknown quantities. The prior is assumed to factorize as

$$
\begin{aligned}
p\left(A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)= & p(A)\left\{\prod_{n, k, m_{t}} p\left(s_{m_{t}}[n, k] \mid A\right)\right\} \\
& \cdot \prod_{m_{t}, m_{r}} p\left(\mathbf{h}_{m_{t}, m_{r}}\right) p\left(\sigma^{2}\right)
\end{aligned}
$$

1) Conventional Prior: A natural choice for the prior distribution of the unknown variables $\left(A, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)$ is given by $A \sim \operatorname{uniform}(\mathcal{A}), s_{m_{t}}[n, k] \mid A \sim \operatorname{uniform}(A), \mathbf{h}_{m_{t}, m_{r}} \sim$ $\mathcal{C N}(\mathbf{0}, \alpha \mathbf{I})$, and $\sigma^{2} \sim \mathcal{I G}\left(\alpha_{0}, \beta_{0}\right)$ with fixed parameters $\left(\alpha, \alpha_{0}, \beta_{0}\right)$ [20]. Recall that the inverse Gamma distribution is the conjugate prior for the Gaussian likelihood at hand, and that uninformative priors can be obtained by selecting sufficiently large $\alpha$ and $\beta_{0}$ and sufficiently small $\alpha_{0}$ [35]. The factorization (14) implies that, under the prior information, the variables $A, \mathbf{h}_{m_{t}, m_{r}}$ and $\sigma^{2}$ are independent of each other, and that the transmitted symbols $s_{m_{t}}[n, k]$ are independent of all the other variables in (14) when conditioned on the modulation $A$. The $\mathrm{BN} \mathcal{G}_{1}$ that encodes the factorization given by (13), along with (4) and (14), is shown in Fig. 1.

The Bayesian inference task for modulation classification of MIMO-OFDM is to compute the posterior probability of the modulation $A$ conditioned on the received signal $\mathbf{y}$, namely

$$
p(A \mid \mathbf{y})=\sum_{\mathbf{s}} \int p\left(A, \mathbf{s}, \mathbf{h}, \sigma^{2} \mid \mathbf{y}\right) d \mathbf{h} d \sigma^{2}
$$

Following the discussion in Sec. III, the calculation in (15) is intractable because of the multidimensional summation and integration. Gibbs sampling (Sec. III-C) and mean field variational inference (Sec. III-D) offer feasible alternatives. However, the prior distribution (14) does not satisfy the sufficient condition mentioned in Remark 1, since some of the conditional distributions required for Gibbs sampling are not strictly positive in their domains. In particular, the required conditional distribution for modulation $A$ can be expressed as

$$
p\left(A=a \mid \mathbf{s}, \mathbf{h}, \sigma^{2}, \mathbf{y}\right) \propto p(A) \prod_{n, k, m_{t}} p\left(s_{m_{t}}[n, k] \mid A\right)
$$

The conditional distribution term $p\left(s_{m_{t}}[n, k] \mid A=a\right)$ in (16) is zero for all values of $s_{m_{t}}[n, k]$ not belonging to the
constellation $a$, i.e., $p\left(s_{m_{t}}[n, k] \mid a\right)=0$ for $s_{m_{t}}[n, k] \notin a$. Therefore, the conditional distribution $p(A=a \mid \mathbf{s}, \mathbf{h}, \sigma^{2}, \mathbf{y})$ is equal to zero if the transmitted symbols $\mathbf{s}$ do not belong to $a$. As a result, the Gibbs sampler may fail to converge to the posterior distribution (see, e.g., [21]). In order to alleviate the problem outlined above, we propose to adopt a prior distribution encoded on a latent Dirichlet $\mathrm{BN} \mathcal{G}_{2}$ shown in Fig. 2.
2) Latent Dirichlet BN: Next, we introduce the Gibbs sampler based on on a latent Dirichlet $\mathrm{BN} \mathcal{G}_{2}$ in details. Accordingly, each transmitted symbol $s_{m_{t}}[n, k]$ is distributed as a random mixture of uniform distributions on the different constellations in the set $\mathcal{A}$. Specifically, a random vector $\mathbf{p}_{A}$ of length $|\mathcal{A}|$ is introduced to represent the mixture weights, with $\mathbf{p}_{A}(a)$ being the probability that each symbol $s_{m_{t}}[n, k]$ belongs to the constellation $a \in \mathcal{A}$. Given the mixture weights $\mathbf{p}_{A}$, the transmitted symbols $s_{m_{t}}[n, k]$ are mutually independent and distributed according to a mixture of uniform distributions, i.e., $p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}\right)=\sum_{a: s_{m_{t}}[n, k] \in a} \mathbf{p}_{A}(a) /|a|$. The Dirichlet distribution is selected as the prior distribution of $\mathbf{p}_{A}$ in order to simplify the development of the proposed solutions, as shown in the following subsections. In particular, given a set of nonnegative parameters $\gamma=\left[\gamma_{1}, \cdots, \gamma_{|\mathcal{A}|}\right]^{T}$, we have $\mathbf{p}_{A} \sim \operatorname{Dirichlet}(\gamma)$ [38]. We recall that the parameter $\gamma_{a}$ has an intuitive interpretation as it represents the number of symbols in constellation $a \in \mathcal{A}$ observed during some preliminary measurements.
![img-1.jpeg](img-1.jpeg)

Figure 2. $\quad \mathrm{BN} \mathcal{G}_{2}$ for the modulation classification scheme based on the Dirichlet latent variable $\mathbf{p}_{A}$. The nodes inside the rectangle are repeated $N K$ times.

The $\mathrm{BN} \mathcal{G}_{2}$ encodes a factorization of the conditional distribution $p\left(\mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2} \mid \mathbf{y}\right)$

$$
\begin{aligned}
& p\left(\mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2} \mid \mathbf{y}\right) \\
\propto & p\left(\mathbf{y} \mid \mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2}\right) p\left(\mathbf{p}_{A}\right)\left\{\prod_{n, k, m_{t}} p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}\right)\right\} \\
& \cdot \prod_{m_{t}, m_{r}} p\left(\mathbf{h}_{m_{t}, m_{r}}\right) p\left(\sigma^{2}\right)
\end{aligned}
$$

where we have $\mathbf{p}_{A} \sim \operatorname{Dirichlet}(\gamma)$ with a set of nonnegative parameters $\gamma=\left[\gamma_{1}, \cdots, \gamma_{|\mathcal{A}|}\right]^{T}$ [38], $p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}\right)=$ $\sum_{a: s_{m_{t}}[n, k] \in a} \mathbf{p}_{A}(a) /|a|$, and the other distributions are as in (4) and (14). The Bayesian inference task for modulation

classification is to compute the posterior probability of the mixture weight vector $\mathbf{p}_{A}$ conditional on the received signal $\mathbf{y}$, namely

$$
p\left(\mathbf{p}_{A} \mid \mathbf{y}\right)=\sum_{\mathbf{s}} \int p\left(\mathbf{p}_{A} \mid \mathbf{s}, \mathbf{h}, \sigma^{2} \mid \mathbf{y}\right) d \mathbf{h} d \sigma^{2}
$$

and then to estimate $A$ as the value that maximize the a posteriori mean of $\mathbf{p}_{A}$ :

$$
\hat{A}=\arg \max _{a \in \mathcal{A}}\left\langle\mathbf{p}_{A}(a) \mid \mathbf{y}\right\rangle_{p\left(\mathbf{p}_{A} \mid \mathbf{y}\right)}
$$

The proposed approach guarantees that all the conditional distributions needed for Gibbs sampling based on the BN $\mathcal{G}_{2}$ are non-zero, and therefore the aforementioned convergence problem for the inference based on $\mathrm{BN} \mathcal{G}_{1}$ is avoided.

## B. Modulation Classification via Gibbs Sampling

In this subsection, we elaborate on Gibbs sampling for modulation classification. As explained in Sec. III-C, in order to sample from the joint posterior distribution (17), the distribution of each variable conditioned on all other variables is needed. According to (10), we have (for derivations see Appendix II):

1) The conditional distribution of the vector $\mathbf{p}_{A}$, given $\mathbf{s}$, $\mathbf{h}, \sigma^{2}$ and $\mathbf{y}$ can be expressed as

$$
p\left(\mathbf{p}_{A} \mid \mathbf{s}, \mathbf{h}, \sigma^{2}, \mathbf{y}\right) \sim \operatorname{Dirichlet}(\gamma+\mathbf{c})
$$

where $\mathbf{c}=\left[c_{1}, \cdots, c_{|\mathcal{A}|}\right]^{T}$, and $c_{a}$ is the number of samples of transmitted symbols in constellation $a \in \mathcal{A}$;
2) The distribution of transmitted symbols $s_{m_{t}}[n, k]$, conditioned on $\mathbf{p}_{A}, \mathbf{s} \backslash s_{m_{t}}[n, k], \mathbf{h}, \sigma^{2}$ and $\mathbf{y}$, is given by

$$
\begin{aligned}
& p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}, \mathbf{s} \backslash s_{m_{t}}[n, k], \mathbf{h}, \sigma^{2}, \mathbf{y}\right) \\
\propto & p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}\right) p\left(\mathbf{y}[n, k] \mid \mathbf{s}[n, k], \mathbf{H}[n], \sigma^{2}\right)
\end{aligned}
$$

where we recall that when a new sample is generated for $s_{m_{t}}[n, k]$, the new value is updated and used in computing subsequent samples in $\mathbf{s}$;
3) The required distribution for channel vector $\mathbf{h}_{m_{t}, m_{r}}$ is given by

$$
\begin{aligned}
& \mathbf{h}_{m_{t}, m_{r}} \mid\left(\mathbf{P}_{A}, \mathbf{s}, \mathbf{h} \backslash \mathbf{h}_{m_{t}, m_{r}}, \sigma^{2}, \mathbf{y}\right) \\
\sim & \mathcal{C N}\left(\hat{\mathbf{h}}_{m_{t}, m_{r}}, \hat{\boldsymbol{\Sigma}}_{m_{t}, m_{r}}\right)
\end{aligned}
$$

where we have

$$
\left(\hat{\boldsymbol{\Sigma}}_{m_{t}, m_{r}}\right)^{-1}=\frac{1}{\sigma^{2}} \mathbf{W}^{H} \mathbf{D}_{m_{t}}^{H}\left(\mathbf{D}_{m_{t}} \mathbf{W}\right)
$$

and

$$
\begin{aligned}
\hat{\mathbf{h}}_{m_{t}, m_{r}}= & \frac{\hat{\boldsymbol{\Sigma}}_{m_{t}, m_{r}}}{\sigma^{2}} \mathbf{W}^{H} \mathbf{D}_{m_{t}}^{H} \\
& \cdot\left(\mathbf{y}_{m_{r}}-\sum_{m_{t}^{\prime} \neq m_{t}} \mathbf{D}_{m_{t}^{\prime}} \hat{\mathbf{h}}_{m_{t}^{\prime}, m_{r}}\right)
\end{aligned}
$$

4) The conditional distribution for $\sigma^{2}$, conditioned on $\mathbf{p}_{A}$, $\mathbf{s}, \mathbf{h}$, and $\mathbf{y}$, is given by

$$
\sigma^{2} \mid \mathbf{p}_{A} \mathbf{s}, \mathbf{h}, \mathbf{y} \sim \mathcal{I G}(\alpha, \beta)
$$

where $\alpha=\alpha_{0}+N K M_{r}$ and $\beta=\beta_{0}+$ $\sum_{m_{r}}\left\|\mathbf{y}_{m_{r}}-\sum_{m_{t}} \mathbf{D}_{m_{t}} \hat{\mathbf{h}}_{m_{t}, m_{r}}\right\|^{2}$. Note that (20) is a consequence of the fact that Dirichlet distribution is the conjugate prior of the categorical likelihood [38]; (22) can be derived by following from standard MMSE channel estimation results [44]; and (25) follows the fact that the inverse Gamma distribution is the conjugate prior for the Gaussian distribution [45].
We summarize the proposed Gibbs sampler for modulation classification in Algorithm 1.

## Algorithm 1 Gibbs Sampling

- Initialize $\boldsymbol{\theta}_{a}^{(0)}=\left\{\mathbf{p}_{A}^{(0)}, \mathbf{s}^{(0)}, \mathbf{h}^{(0)}, \sigma^{2^{(0)}}\right\}$ from prior distributions as discussed in Sec. IV-A
- for each iteration $m=1: M$
- given $\left\{\mathbf{s}^{(m-1)}, \mathbf{h}^{(m-1)}, \sigma^{2^{(m-1)}}\right\}$ draw a sample $\mathbf{p}_{A}^{(m)}$ from $p\left(\mathbf{p}_{A} \mid \mathbf{s}, \mathbf{h}, \sigma^{2}, \mathbf{y}\right)$ in (20);
- given $\left\{\mathbf{p}_{A}^{(m)}, \mathbf{h}^{(m-1)}, \sigma^{2^{(m-1)}},\left(\mathbf{s} \backslash s_{m_{t}}[n, k])^{(m)}\right\}\right.$, draw a sample $s_{m_{t}}^{(m)}[n, k]$ from $p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}, \mathbf{s} \backslash s_{m_{t}}[n, k], \mathbf{h}, \sigma^{2}, \mathbf{y}\right)$ in (21);
- given $\left\{\mathbf{p}_{A}^{(m)}, \mathbf{s}^{(m)}, \sigma^{2^{(m-1)}},\left(\mathbf{h} \backslash \mathbf{h}_{m_{t}, m_{r}}\right)^{(m)}\right\}$ and the current sample values for, draw a sample $\mathbf{h}_{m_{t}, m_{r}}^{(m)}$ from $p\left(\mathbf{h}_{m_{t}, m_{r}}:\left(\mathbf{P}_{A}, \mathbf{s}, \mathbf{h} \backslash \mathbf{h}_{m_{t}, m_{r}}, \sigma^{2}, \mathbf{y}\right)\right)$ in (22);
- given $\left\{\mathbf{p}_{A}^{(m)}, \mathbf{s}^{(m)}, \mathbf{h}^{(m)}\right\}$ draw sample $\sigma^{2^{(m)}}$ from $p\left(\sigma^{2} \mid \mathbf{p}_{A} \mathbf{s}, \mathbf{h}, \mathbf{y}\right)$ in (25);
- end for

Remark 3: In [19], an alternative Gibbs sampling approach based on a "superconstellation" is proposed to solve the convergence problem at hand for modulation classification in SISO. The Gibbs sampling scheme in [19] can be viewed as an approximation of the approach based on the latent Dirichlet BN obtained by setting the prior distribution $\mathbf{p}_{A} \sim$ Dirichlet $(\gamma)$ such that $\gamma=\mathbf{0}$ and by setting the sample value of $\mathbf{p}_{A}$ to be equal to the mean of the conditional distribution $p\left(\mathbf{p}_{A} \mid \mathbf{s}, \mathbf{h}, \sigma^{2}, \mathbf{y}\right)$, i.e., $\mathbf{p}_{A}^{(m)}=\mathbf{c} / \sum_{a \in A} c_{a}$ [20], where we recall that $c_{a}$ is the number of symbols that belong to constellation $a \in \mathcal{A}$. The performance of the "superconstellation" approach extended to MIMO OFDM is discussed in Sec. V.

Remark 4: When the SNR is high, the convergence speed is severely limited by the close-to-zero probabilities in the conditional distribution (21). Specifically, as the Gibbs sampling proceeds with its iterations, the samples of $\sigma^{2}$ tend to be small, making the relationship between $\mathbf{y}[n, k]$ and $s_{m_{t}}[n, k]$ almost deterministic. In particular, the term $p(\mathbf{y}[n, k] \mid \mathbf{s}[n, k], \mathbf{H}[n], \sigma^{2})$ in (21) satisfies $p\left(\mathbf{y}[n, k] \mid \mathbf{s}^{(m)}[n, k], \mathbf{H}^{(m)}[n],\left(\sigma^{2}\right)^{(m)}\right) \simeq 1$ for the selected sample value $\mathbf{s}^{(m)}[n, k]$, and $p\left(\mathbf{y}[n, k] \mid \mathbf{s}^{(m)}[n, k], \mathbf{H}^{(m)}[n],\left(\sigma^{2}\right)^{(m)}\right) \simeq 0$ for all other possible values for $\mathbf{s}[n, k]$. As a result, transition between states with different values in the Markov chain occurs with a very low probability leading to extremely slow convergence. As discussed in Remark 2, the strategy of Gibbs sampling with multiple random restarts and annealing may be adopted to address this issue. For simulated annealing, we substitute

the conditional distribution (25) for $\sigma^{2}$ with an iteration dependent prior given as [33]

$$
\sigma^{2} \mid \mathbf{p}_{A} \mathbf{s}, \mathbf{h}, \mathbf{y} \sim \mathcal{I} \mathcal{G}\left(\alpha^{\prime}, \beta\right)
$$

where we have $\alpha^{\prime}(m)=\left(1-\left(1-p_{0}\right) \exp \left(-m / m_{0}\right)\right) \alpha$, with $m$ denoting the current iteration index, $p_{0}=0.1$ and $m_{0}=0.3 M$, where $M$ is the total number of iterations. For multiple restarts, we propose to use the entropy of the $\operatorname{pmf}\left\langle\mathbf{p}_{A}\right\rangle_{p\left(\mathbf{p}_{A} \mid \mathbf{y}\right)}$, estimated in a run as the metric, to choose among the $N_{\text {run }}$ runs of Gibbs sampling which one should be used in (19). Specifically, the run with the minimum entropy estimate $\left\langle\mathbf{p}_{A}\right\rangle_{p\left(\mathbf{p}_{A} \mid \mathbf{y}\right)}$ is selected. The rationale of this choice is that an estimate $\left\langle\mathbf{p}_{A}\right\rangle_{p\left(\mathbf{p}_{A} \mid \mathbf{y}\right)}$ with a low entropy identifies a specific modulation type with a smaller uncertainty than an estimate $\left\langle\mathbf{p}_{A}\right\rangle_{p\left(\mathbf{p}_{A} \mid \mathbf{y}\right)}$ with higher entropy (i.e., closer to a uniform distribution).

## C. Modulation classification via Mean Field Variational Inference

Following the discussion in Sec. III-D, the goal of mean field variational inference applied to the problem at hand is that of searching for a distribution $q\left(\mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)$ that is closest to the desired posterior distribution $p\left(\mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2} \mid \mathbf{y}\right)$, in terms of the Kullback-Leibler (KL) divergence $\mathrm{KL}\left(q\left(\mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2}\right) \| p\left(\mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2} \mid \mathbf{y}\right)\right)$, within the class $\mathcal{Q}$ of distributions that factorize as

$$
q\left(\mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2}\right)=q\left(\mathbf{p}_{A}\right) q(\mathbf{s}) q(\mathbf{h}) q\left(\sigma^{2}\right)
$$

where $q(\mathbf{s})=\prod_{k=1}^{K} \prod_{n=1}^{N} \prod_{m_{\ell}}^{M_{\ell}} q\left(s_{m_{\ell}}[n, k]\right)$, and $q(\mathbf{h})=$ $\prod_{m_{\ell}}^{M_{\ell}} \prod_{m_{r}}^{M_{r}} \mathbf{h}_{m_{\ell}, m_{r}}$. Next, we present the fixed-point equations for mean field variational inference. These update equations may be derived by applying (12) to the joint pdf (17). We recall that (12) requires taking expectations of the relevant variables with respect to updated distribution $q$. If all distributions $q\left(\mathbf{p}_{A}\right), q(\mathbf{h})$ and $q\left(\sigma^{2}\right)$ are initialized by choosing from the conjugate exponential prior family [39], [46] in a way being consistent with the priors in (17), namely $q\left(\mathbf{p}_{A}\right)$ being a Dirichlet distribution, $q(\mathbf{h})$ being a circularly complex Gaussian distribution, and $q\left(\sigma^{2}\right)$ being an inverse Gamma distribution, these fixed point update equations can be calculated, using a similar approach as in the Appendix I, as follows.

1) The fixed point update equation for the mixture weight vector $\mathbf{p}_{A}$ can be expressed as

$$
q\left(\mathbf{p}_{A}\right)=\operatorname{Dirichlet}(\gamma+\mathbf{g})
$$

where $\mathbf{g}=\left[g_{1}, \cdots, g_{|\mathcal{A}|}\right]^{T}$ and $g_{a}=$ $\sum_{n, k, m_{\ell}} \sum_{s_{m_{\ell}}[n, k] \in a} q\left(s_{m_{\ell}}[n, k]\right)$.
2) The update equation for the transmitted symbol $s_{m_{\ell}}[n, k]$ is given by

$$
\begin{aligned}
& q\left(s_{m_{\ell}}[n, k]\right) \propto \exp \left[\left\langle\ln p\left(s_{m_{\ell}}[n, k] \mid \mathbf{p}_{A}\right)\right\rangle_{q\left(\mathbf{p}_{A}\right)}+\right. \\
& \left.\left\langle\ln p\left(\mathbf{y}[n, k] \mid \mathbf{s}[n, k], \mathbf{H}[n], \sigma^{2}\right)\right\rangle_{q\left(\mathbf{s}[n, k] \backslash s_{m_{\ell}}[n, k], \mathbf{h}, \sigma^{2}\right)}\right]
\end{aligned}
$$

where the detailed expression of (29) is shown in Appendix III.
3) The equation for the channel vector $\mathbf{h}_{m_{\ell} m_{r}}$ is given by

$$
q\left(\mathbf{h}_{m_{\ell} m_{r}}\right)=\mathcal{C N}\left(\hat{\mathbf{h}}_{m_{\ell}, m_{r}}, \hat{\boldsymbol{\Sigma}}_{m_{\ell}, m_{r}}\right)
$$

where

$$
\begin{gathered}
\left(\hat{\boldsymbol{\Sigma}}_{m_{\ell}, m_{r}}\right)^{-1}=\frac{\alpha}{\beta} \mathbf{W}^{H}\left\langle\mathbf{D}_{m_{\ell}}^{H} \mathbf{D}_{m_{\ell}}\right\rangle \mathbf{W} \\
\hat{\mathbf{h}}_{m_{\ell}, m_{r}} \\
=\frac{\alpha}{\beta} \mathbf{W}^{H}\left\langle\mathbf{D}_{m_{\ell}}\right\rangle^{H}\left(\mathbf{y}_{m_{r}}-\sum_{m_{\ell}^{\prime} \neq m_{\ell}} \boldsymbol{\Lambda}_{m_{\ell}^{\prime}, m_{r}}\right) \\
\boldsymbol{\Lambda}_{m_{\ell}^{\prime}, m_{r}}=\left\langle\mathbf{D}_{m_{\ell}}\right\rangle \mathbf{W} \hat{\mathbf{h}}_{m_{\ell}^{\prime}, m_{r}}
\end{gathered}
$$

and $\left\langle\mathbf{D}_{m_{\ell}}^{H} \mathbf{D}_{m_{\ell}}\right\rangle$ is a diagonal matrix whose $(n, n)$ element is equal to $\sum_{k=1}^{K}\left\langle\left|s_{m_{\ell}}[n, k]\right|^{2}\right\rangle$.
4) The fixed point update equation for the noise variance $\sigma^{2}$ can be expressed as

$$
q\left(\sigma^{2}\right)=\mathcal{I} \mathcal{G}(\alpha, \beta)
$$

where $\alpha=\alpha_{0}+N K M_{r}$, and $\beta=\beta_{0}+\sum_{m_{r}} \beta_{m_{r}}$ with

$$
\begin{aligned}
\beta_{m_{r}}= & \left|\mathbf{y}_{m_{r}}\right|^{2}-2 \operatorname{real}\left[\mathbf{y}_{m_{r}}^{H} \sum_{m_{\ell}} \boldsymbol{\Lambda}_{m_{\ell}, m_{r}}\right]+ \\
& +\sum_{m_{\ell}} \boldsymbol{\Psi}_{m_{\ell}, m_{r}}+\sum_{m_{\ell}} \boldsymbol{\Xi}_{m_{\ell}, m_{r}} \\
\boldsymbol{\Psi}_{m_{\ell}, m_{r}}= & \operatorname{tr}\left[\mathbf{W}^{H}\left\langle\mathbf{D}_{m_{\ell}}^{H} \mathbf{D}_{m_{\ell}}\right\rangle \mathbf{W} \hat{\boldsymbol{\Sigma}}_{m_{\ell}, m_{r}}\right]+ \\
& \hat{\mathbf{h}}_{m_{\ell}, m_{r}}^{H} \mathbf{W}^{H}\left\langle\mathbf{D}_{m_{\ell}}^{H} \mathbf{D}_{m_{\ell}}\right\rangle \mathbf{W} \hat{\mathbf{h}}_{m_{\ell}, m_{r}}
\end{aligned}
$$

and

$$
\boldsymbol{\Xi}_{m_{\ell}, m_{r}}=\hat{\mathbf{h}}_{m_{\ell}, m_{r}}^{H} \mathbf{W}^{H}\left\langle\mathbf{D}_{m_{\ell}}\right\rangle^{H}\left\langle\mathbf{D}_{m_{\ell}^{\prime}}\right\rangle \mathbf{W} \hat{\mathbf{h}}_{m_{\ell}^{\prime}, m_{r}}
$$

where we use $\operatorname{tr}[\cdot]$ to denote the trace of a matrix.
We summarize the proposed iterative mean field variational inference for modulation classification in Algorithm 2.

## Algorithm 2 Mean Field Variational Inference

- Initialize $q\left(\mathbf{p}_{A}\right), q(\mathbf{s}), q(\mathbf{h})$ and $q\left(\sigma^{2}\right)$
- for each iteration $m=1: M$
- given the most updated distribution $q(\mathbf{s}), q(\mathbf{h})$ and $q\left(\sigma^{2}\right)$, update the distribution $q\left(\mathbf{p}_{A}\right)$ using (28);
- given the most updated distribution $q\left(\mathbf{p}_{A}\right)$, $q\left(\mathbf{s} \backslash s_{m_{\ell}}[n, k]\right), q(\mathbf{h})$ and $q\left(\sigma^{2}\right)$, update the distribution $q\left(s_{m_{\ell}}[n, k]\right)$ using (29);
- given the most updated distribution $q\left(\mathbf{p}_{A}\right), q(\mathbf{s})$, $q\left(\mathbf{h} \backslash \mathbf{h}_{m_{\ell}, m_{r}}\right)$ and $q\left(\sigma^{2}\right)$, update the distribution $q\left(\mathbf{h}_{m_{\ell}, m_{r}}\right)$ using (30);
- given the most updated distribution $q\left(\mathbf{p}_{A}\right), q(\mathbf{s})$, and $q(\mathbf{h})$, update the distribution $q\left(\sigma^{2}\right)$ according to (34);
- end for

Remark 5: While Gibbs sampler is generally known to be superior to mean field as a method for exploring the global solution space, the mean field algorithm is known to have

Table I
Computational Complexity for Gibbs SAMPLING


better convergence speed in the vicinity of a local optima [38], [39], [40]. Following [39], we then propose a hybrid strategy strategy that switches from Gibbs sampling to mean field variational inference to "zoom in" on the local minimum of the optimization problem (11). Additional discussion on this point can be found in the next section. A break-down of the contribution to the computational complexity of each iteration for the proposed Gibbs sampler are shown in Table I. In summary, the Gibbs sampler requires $\mathcal{O}\left\{N_{i t} M_{t} M_{r}\left[N K\left(N L+L^{2}+\right.\right.\right.$ $\left.\left.\left.M_{t} N+M_{t} M_{A}\right)+L^{3}\right]\right\}$ basic arithmetic operations, where $N_{i t}$ is the total number of iterations and $M_{A}$ is the total number of states of all possible constellations, i.e., $M_{A}=\sum_{a \in A}|a|$. At each iteration, the number of the basic arithmetic operations required for mean field variational inference is of the same order of magnitude as that for Gibbs sampling. This similarity of the computational complexity of Gibbs sampling and mean field variational inference is also reported in [39], [40] and [47].

## V. NUMERICAL RESULTS AND DISCUSSIONS

In this section, we evaluate the performance of the proposed modulation classification schemes for the detection of three possible modulation formats within a MIMO-OFDM system. The performance criterion is the probability of correct classification assuming that all the modulations are equally likely. Normalized Rayleigh fading channels are assumed such that $E\left[\left\|\mathbf{h}_{m_{t}, m_{r}}\right\|^{2}\right]=1$. We define the average SNR as $10 \log \left(M_{t} / \sigma^{2}\right)$. Unless stated otherwise, the following conditions are assumed: $i) \mathcal{A}=\{$ QPSK, 8-PSK, 16QAM $\}$; ii) $M_{t}=M_{r}=2$ antennas; iii) $K=2$ OFDM symbols; and $i v) L=5$ taps with relative powers given by $[0 \mathrm{~dB},-4.2 \mathrm{~dB},-11.5 \mathrm{~dB},-17.6 \mathrm{~dB},-21.5 \mathrm{~dB}]$.

## A. Performance of Gibbs Sampling

1) Gibbs Sampling with Restarts and Annealing: We first investigate the performance of the proposed Gibbs sampling algorithms with or without multiple random restarts and simulated annealing within each run (see Remark 4). The number of runs in each process of Gibbs sampling with multiple random restarts is selected to be $N_{r u n}=5$, and the number of iterations in each run is $M=2000$, where $M_{0}=0.85 M$ initial samples are used as burn-in period. ${ }^{2}$ Note here that the total number of iterations required for Gibbs sampling is $N_{i t}=N_{r u n} M$. All elements of the vector parameter $\gamma$

[^0]of the prior distribution $\mathbf{p}_{A} \sim \operatorname{Dirichlet}(\gamma)$ are selected to be equal to a parameter $\gamma$. As also reported in [20], it may be shown, via numerical results, that the modulation classification performance is not sensitive to the choice of parameter $\gamma$ as long as the value of the virtual observation $\gamma$ (see Sec. IV-A2) is not very small $(\gamma<1)$. For the numerical experiments in this paper, we select the values of $\gamma$ to be equal to $8 \%$ of the total number of symbols, e.g., in this example $\gamma=\left[0.08 N K M_{t}\right]=40$.

In Fig. 3, the probabilities of correct classification for regular Gibbs sampling, Gibbs sampling with multiple random restarts, Gibbs sampling with annealing and Gibbs sampling with both multiple random restarts and annealing are plotted as a function of SNR. We also show for reference the performance of the 'superconstellation' scheme, with both multiple random restarts and annealing, of [19] (see Remark 3) extended to MIMO OFDM systems. From Fig. 3, it can be seen that the proposed strategy outperforms the approach in [19]. Moreover, both strategies of multiple random restarts and annealing improve the success rate, and that the best performance is achieved by Gibbs sampling with both random restarts and annealing. As discussed in Remark 4, annealing is seen to be especially effective in the high-SNR regime.
![img-2.jpeg](img-2.jpeg)

Figure 3. Probability of correct classification using Gibbs sampling versus $\operatorname{SNR}\left(N=128, M_{t}=M_{r}=2, K=2\right.$ and $\left.L=5\right)$.
2) Performance Under Incorrect Channel Length Estimates: Next, we study the effect of incorrect channel length estimates. The relative powers of the considered channel taps are $[0 \mathrm{~dB},-2 \mathrm{~dB},-2.5 \mathrm{~dB}]$. We considered the performance of the proposed scheme under overestimated, correctly estimated, or underestimated channel lengths. Specifically, the channel length estimates take three possible values, namely $\hat{L}=1$, $\hat{L}=3$ or $\hat{L}=5$, while $L=3$. The same values for the parameters of Gibbs sampler are used as in Sec. V-A1. Fig. 4 shows the probabilities of correct classification for Gibbs sampling with both random restarts and annealing versus SNR. It is observed that there is a minor performance degradation with an overestimated channel length. Here, for this example, the degradation caused by the overfitting when a more complex model with $\hat{L}=5$ is used is minor. In contrast, a more severe performance degradation is observed for the


[^0]:    ${ }^{2}$ The samples in the burn-in period are not used to evaluate the average in (19).

Table II
CONFUSION MATRIX OF THE PROPOSED GIBBS SAMPLER FOR THREE MODULATION FORMATS AT 5 DB


case of the underestimated channel length. This significant degradation is caused by the bias introduced by the simpler model with $\hat{L}=1$. We also carried out the experiments for $L=5$ taps with relative powers of $[0 \mathrm{~dB},-2 \mathrm{~dB},-2.5 \mathrm{~dB}$, $-3.1 \mathrm{~dB},-4.2 \mathrm{~dB}]$. The performance is very similar to that for the case of $L=3$ shown in Fig. 4 and is hence not reported here.
![img-3.jpeg](img-3.jpeg)

Figure 4. Probability of correct classification using Gibbs sampling versus SNR with different channel length estimates $\hat{L}\left(N=128, M_{t}=M_{r}=2\right.$, $K=2$ and $L=3$ ).
3) Performance with a Larger $\mathcal{A}$ : To study the effect of modulation pool $\mathcal{A}$ with a larger size, besides the three modulations considered above, we added 16-PSK into the modulation pool, i.e., $\mathcal{A}=\{$ QPSK, 8-PSK, 16QAM, 16-PSK $\}$. The relative powers of the multi-path components and the parameters of the Gibbs sampler take the same value as in Sec. V-A2. The performance of the proposed Gibbs sampler for the cases of three and four modulation formats is shown in Fig. 4. As expected, some performance degradation is observed for a larger set of possible modulation schemes. To gain more insight into the classifier behavior, the confusion matrices for both cases of three and four modulation schemes for SNR of 5 dB are shown in Tables II and III, respectively. The confusion matrices show the probabilities of deciding for a given modulation format when another format is the correct one. For instance, the element associated with row ' 8 -PSK' and column 'QPSK' in Table II indicates that, when the actual modulation scheme is 8-PSK, the probability that the estimated modulation is QPSK is $9.2 \%$. Comparing Table II with Table III, it can be seen that the decreased accuracy is mainly caused by the confusion between the two most similar modulation formats, namely 8-PSK and 16-PSK.
![img-4.jpeg](img-4.jpeg)

Figure 5. Probability of correct classification using Gibbs sampling versus SNR with different sets $\mathcal{A}$ of possible modulation schemes ( $N=128, M_{t}=$ $M_{r}=2, K=2$ and $L=3$ ).

Table III
CONFUSION MATRIX OF THE PROPOSED GIBBS SAMPLER FOR FOUR MODULATION FORMATS AT 5 DB


## B. Performance of Mean Field Variational Inference

Here, we study the performance of a hybrid scheme, inspired by [39], that starts with a Gibbs sampler in order to perform a global search in the parameter space and then switches to mean field variational inference to speed up the convergence to a nearby local optima. In the switching iteration, all the needed marginal distributions for mean field variational inference are initialized as the conditional distributions for Gibbs sampling in the previous iteration, namely the marginal distributions are initialized as follows,

$$
\begin{gathered}
q^{\left(m_{s}\right)}\left(\mathbf{p}_{A}\right)=p^{\left(m_{s}-1\right)}\left(\mathbf{p}_{A} \mid \mathbf{s}, \mathbf{h}, \sigma^{2}, \mathbf{y}\right) \\
q^{\left(m_{s}\right)}\left(s_{m_{t}}[n, k]\right) \\
=p^{\left(m_{s}-1\right)}\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}, \mathbf{s} \backslash s_{m_{t}}[n, k], \mathbf{h}, \sigma^{2}, \mathbf{y}\right) \\
q^{\left(m_{s}\right)}\left(\mathbf{h}_{m_{t} m_{r}}\right) \\
=p^{\left(m_{s}-1\right)}\left(\mathbf{h}_{m_{t}, m_{r}} \mid \mathbf{P}_{A}, \mathbf{s}, \mathbf{h} \backslash \mathbf{h}_{m_{t}, m_{r}}, \sigma^{2}, \mathbf{y}\right)
\end{gathered}
$$

and

$$
q^{\left(m_{s}\right)}\left(\sigma^{2}\right)=p^{\left(m_{s}-1\right)}\left(\sigma^{2} \mid \mathbf{p}_{A} \mathbf{s}, \mathbf{h}, \mathbf{y}\right)
$$

where $m_{s}$ denotes the index of the switching iteration.
To demonstrate the effectiveness of this approach, we consider modulation classification using received samples within one OFDM frame $(K=1)$ over Rayleigh fading channels with two taps $(L=2)$ and with the relative powers $[0 \mathrm{~dB},-4.2 \mathrm{~dB}]$. The SNR is 10 dB and the DFT size is $N=64$ or 128 . After the first eight iterations of regular Gibbs sampling (without random restarts and annealing), we switch to the mean field

variational inference. The probability of correct classification of both regular Gibbs sampling and the hybrid approach versus the number of iterations $M$ with $M_{0}=0.9 M$ burn-in samples is shown in Fig. 6. It can be observed that the hybrid approach outperforms Gibbs sampling especially when the number of iterations is small.
![img-5.jpeg](img-5.jpeg)

Figure 6. Probability of correct classification using Gibbs sampling and mean field variational inference versus $M\left(M_{t}=M_{r}=2, K=1, L=2\right.$ and $\left.\mathrm{SNR}=10 \mathrm{~dB}\right)$.

## C. Comparison of Gibbs Sampling and ICA-PC [28]

Here, we compare the classification results achieved by the proposed Gibbs sampling scheme with the ICA-PC approach of [28], which extends to MIMO-OFDM the techniques studied in [22]. The approach in [28] exploits the invariance of the frequency-domain channels across the coherence bandwidth to perform classification. Specifically, the subcarriers are grouped in sets of $D$ adjacent subcarriers whose frequency-domain channel matrices are assumed to be identical. Let us denote the frequency-domain channel matrix and the received samples for the $i$-th group by $\mathbf{H}_{i}$ and $\mathbf{y}_{i}$ respectively, $i=1, \ldots, N / D$. To compute the likelihood function $p\left(\mathbf{y}_{i} \mid A=a, \mathbf{H}_{i}\right)$ of the received samples $\mathbf{y}_{i}$ over the subcarriers within group $i$, an estimate $\hat{\mathbf{H}}_{i}$ of the channel matrix $\mathbf{H}_{i}$ is first obtained using ICA-PC, and then the likelihood $p\left(\mathbf{y}_{i} \mid A=a, \mathbf{H}_{i}\right)$ is approximated as $p\left(\mathbf{y}_{i} \mid A=a, \hat{\mathbf{H}}_{i}\right)$. Accordingly, the likelihood function $p(\mathbf{y} \mid A=a, \mathbf{H})$ of all the received samples $\mathbf{y}$ is approximated as $p(\mathbf{y} \mid A=a, \hat{\mathbf{H}})=\prod_{i} p\left(\mathbf{y}_{i} \mid A=a, \hat{\mathbf{H}}_{i}\right)$, where $\hat{\mathbf{H}}=\left\{\hat{\mathbf{H}}_{i}\right\}_{i=1}^{N / D}$. The detected modulation is selected as $\widehat{A}=\arg \max _{a \in \mathcal{A}} p(\mathbf{y} \mid A=a, \hat{\mathbf{H}})$.

In Fig. 7, we plot the performance of the approach based on ICA-PC with different values of $D$ and Gibbs sampling with random restarts and annealing. The number of runs are $N_{r u n}=5$, and the annealing schedule is (26). It can be seen from Fig. 7 that Gibbs sampling significantly outperforms ICA-PC. In this regard, note that, with $D=4$, the accuracy in ICA-PC is poor due to the insufficient number of observed data samples; while with $D=16$, the model mismatch problem becomes more severe due to the assumption of equal channel matrices in each subcarrier group.

To further emphasize the advantages of the proposed Bayesian techniques, in Fig. 7, we consider the case in which there are fewer receive antennas than transmit antennas by setting $M_{r}=1$ and all other parameters as above. While ICA-PC cannot be applied due to the ill-posedness of the ICA problem, it can be observed that a success rate of $71 \%$ can be attained by the proposed Gibbs scheme at 15 dB . It should be mentioned however, that the complexity of ICA-PC of the order of $\mathcal{O}\left\{M_{t} M_{r} K N M_{a}^{M_{t}}\right\}$ [24] is smaller than that of Gibbs sampling (see Remark 5), where $M_{u}$ denotes the maximum number of states of a constellation among all the possible modulation types, i.e., $M_{u}=\max _{a \in \mathcal{A}}\{|a|\}$.
![img-6.jpeg](img-6.jpeg)

Figure 7. Probability of correct classification using Gibbs sampling with multiple random restarts and annealing and approach of [28] based on ICAPC versus SNR $(N=128, K=2$ and $L=5)$.

## D. Performance for Coded OFDM Signals

To investigate the performance of the proposed Gibbs sampling approach in the presence of a model mismatch, we study here the case of coded OFDM. Specifically, we assume that the information bits are first encoded using a convolutional code, and then modulated. We apply Gibbs sampling with multiple random restarts and annealing with all relevant parameters being the same as in Sec. V-A. The code rates are $1 / 3,1 / 2$ and $2 / 3$, respectively. In Fig. 8, the probability of correct classification is shown versus SNR. It can be seen from the figure that the success rate decreases only slightly (up to $6 \%$ ) as the code rate decreases. The degradation is caused by the fact that the coded transmitted symbols are not mutually independent due to the convolutional coding, and hence their prior distribution is mismatched with respect to the model (17). As the SNR increases, the performance degradation for coded signals become minor, because, in this regime, Gibbs sampling relies more on the observed samples than on the priors. We also studied the performance of the proposed Gibbs sampling for OFDM systems with spacefrequency coded symbols (SF-OFDM) [48]. Compared to the uncoded case, minor performance degradation ( $2 \%$ at 15 dB and up to $8 \%$ at 0 dB ) is observed also due to the presence of a model mismatch.

![img-7.jpeg](img-7.jpeg)

Figure 8. Probability of correct classification using Gibbs sampling with multiple random restarts and annealing versus SNR for convolution coded OFDM signals with different code rate $(N=128, M_{t}=M_{r}=2, K=2$ and $L=5$ ).

## VI. CONCLUSIONS

In this paper, we have proposed two Bayesian modulation classification schemes for MIMO-OFDM systems based on a selection of the prior distributions that adopts a latent Dirichlet model and on the Bayesian network formalism. The proposed Gibbs sampling method converges to an effective solution and, using numerical results, its accuracy is demonstrated to improve for small sample sizes when switching to the mean field variational inference technique after a number of iterations. The speed of convergence is shown to improve via multiple random restarts and annealing. The techniques are seen to overcome the performance limitation of state-of-the-art non-Bayesian schemes based on ICA and Bayesian schemes based on "superconstellation" methods. In fact, while most of the mentioned existing modulation classification algorithms rely on the assumptions that the channels are flat fading, that the number of receive antennas is no less than the number of transmit antenna, and/or that a large amount of samples are available (as for pattern recognition-based methods), the proposed schemes achieve satisfactory performance under more general conditions. For example, with $M_{t}=2$ transmit antennas and under frequency selective fading channels with $L=5$ taps, a correct classification rate of above $97 \%$ may be attained with $M_{r}=2$ receive antennas and with 256 received samples at each antenna; and a success rate of above $70 \%$ may be achieved with $M_{r}=1$ receive antenna and 256 received samples at the antenna. Moreover, the proposed Gibbs sampler presents a graceful degradation in the presence of a model mismatch caused by channel coding, e.g., a decrease in the success rate by $6 \%$ with a code rate of $1 / 3$. Future works include devising a Gibbs sampling scheme that accounts for the effects of the timing and carrier frequency offsets for MIMO systems following, e.g., [21], [44], [49]. In addition, the development of Bayesian classification techniques that address non-Gaussian noise is also a topic for further investigation.

## APPENDIX I

## DISTRIBUTIONS

In this Appendix, we give the expressions for all standard distributions that are useful to derive the conditional distributions for Gibbs sampling in Appendix II.

1) Dirichlet Distribution: $\mathbf{Z} \sim \operatorname{Dirichlet}(\mathbf{c})$,

$$
p(\mathbf{Z})=\frac{\Gamma\left(\sum_{i=1}^{k_{z}} c_{i}\right)}{\prod_{i=1}^{k_{z}} \Gamma\left(c_{i}\right)} \prod_{i=1}^{k_{z}} z_{i}^{c_{i}-1}
$$

where $k_{z}$ denotes the length of the vector $\mathbf{Z}$, and $\Gamma(\cdot)$ stands for the gamma function [41].
2) Circular complex Gaussian distribution: $\mathbf{Z} \sim \mathcal{C N}(\mu, \boldsymbol{\Sigma})$, $p(\mathbf{Z})=\frac{1}{\pi^{k_{z}} \operatorname{det}(\boldsymbol{\Sigma})} \exp \left\{-(\mathbf{Z}-\mu)^{H} \boldsymbol{\Sigma}^{-1}(\mathbf{Z}-\mu)\right\}$,
where we use $\operatorname{det}(\cdot)$ to denote the determinant of a matrix.
3) Inverse Gamma distribution:: $z \sim \mathcal{I G}(c, d)$,

$$
p(\mathbf{Z})=\frac{d^{c}}{\Gamma(c)} z^{-c-1} \exp \left(-\frac{d}{z}\right)
$$

## APPENDIX II

## DERIVATIONS OF CONDITIONAL DISTRIBUTIONS FOR GIBBS SAMPLING

In this Appendix, the required conditional distributions for Gibbs sampling are derived.
A. Expression for $p\left(\mathbf{p}_{A} \mid \mathbf{s}, \mathbf{h}, \sigma^{2}, \mathbf{y}\right)$

Applying (10) to (17), we have

$$
\begin{aligned}
& p\left(\mathbf{p}_{A} \mid \mathbf{s}, \mathbf{h}, \sigma^{2}, \mathbf{y}\right) \\
& \propto p\left(\mathbf{p}_{A}\right)\left\{\prod_{n, k, m_{t}} p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}\right)\right\} \\
& \propto \prod_{a \in \mathcal{A}}\left[\mathbf{p}_{A}(a)\right]^{\gamma(a)-1} \prod_{n, k, m_{t}}\left[\sum_{a: s_{m_{t}}[n, k] \in a} \mathbf{p}_{A}(a) /|a|\right] \\
& =\prod_{a \in \mathcal{A}} \frac{1}{|a|}\left[\mathbf{p}_{A}(a)\right]^{\gamma(a)-1+c_{a}} \\
& \sim \operatorname{Dirichlet}(\gamma+\mathbf{c})
\end{aligned}
$$

where $\mathbf{c}=\left[c_{1}, \cdots, c_{|\mathcal{A}|}\right]^{T}$, and $c_{a}$ is the number of samples of transmitted symbols in constellation $a \in \mathcal{A}$.
B. Expression for $p\left(\mathbf{h}_{m_{t}, m_{r}} \mid\left(\mathbf{P}_{A}, \mathbf{s}, \mathbf{h} \backslash \mathbf{h}_{m_{t}, m_{r}}, \sigma^{2}, \mathbf{y}\right)\right)$

Applying (10) to (17), we have

$$
\begin{aligned}
& p\left(\mathbf{h}_{m_{t}, m_{r}} \mid\right.\left(\mathbf{P}_{A}, \mathbf{s}, \mathbf{h} \backslash \mathbf{h}_{m_{t}, m_{r}}, \sigma^{2}, \mathbf{y}\right)) \\
& \propto p\left(\mathbf{h}_{m_{t}, m_{r}}\right) p\left(\mathbf{y} \mid \mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2}\right) \\
& \propto \exp \left\{-\mathbf{h}_{m_{t}, m_{r}}^{H}\left(\hat{\boldsymbol{\Sigma}}_{m_{t}, m_{r}}\right)^{-1} \mathbf{h}_{m_{t}, m_{r}}+\right. \\
& \left.\quad 2 \operatorname{real}\left[\mathbf{h}_{m_{t}, m_{r}}^{H}\left(\hat{\boldsymbol{\Sigma}}_{m_{t}, m_{r}}\right)^{-1} \hat{\mathbf{h}}_{m_{t}, m_{r}} \mathbf{h}_{m_{t}, m_{r}}\right]\right\} \\
& \sim \mathcal{C N}\left(\hat{\mathbf{h}}_{m_{t}, m_{r}}, \hat{\boldsymbol{\Sigma}}_{m_{t}, m_{r}}\right)
\end{aligned}
$$

where

$$
\begin{aligned}
\left(\hat{\boldsymbol{\Sigma}}_{m_{t}, m_{r}}\right)^{-1} & =\frac{1}{\alpha_{h}} \mathbf{I}+\frac{1}{\sigma^{2}} \mathbf{W}^{H} \mathbf{D}_{m_{t}}^{H} \mathbf{D}_{m_{t}} \mathbf{W} \\
& \approx \frac{1}{\sigma^{2}} \mathbf{W}^{H} \mathbf{D}_{m_{t}}^{H} \mathbf{D}_{m_{t}} \mathbf{W}
\end{aligned}
$$

and

$$
\begin{aligned}
\hat{\mathbf{h}}_{m_{t}, m_{r}}= & \hat{\boldsymbol{\Sigma}}_{m_{t}, m_{r}} \frac{1}{\sigma^{2}} \mathbf{W}^{H} \mathbf{D}_{m_{t}}^{H} \\
& \cdot\left(\mathbf{y}_{m_{r}}-\sum_{m_{t}^{\prime} \neq m_{t}} \mathbf{D}_{m_{t}^{\prime}} \hat{\mathbf{h}}_{m_{t}^{\prime}, m_{r}}\right)
\end{aligned}
$$

where the approximation in (47) follows from the fact that $\alpha_{h}$ is very large such that the term $1 / \alpha_{h} \mathbf{I}$ can be neglected.

## C. Expression for $p\left(\sigma^{2} \mid \mathbf{p}_{A} \mathbf{s}, \mathbf{h}, \mathbf{y}\right)$

Applying (10) to (17), we have

$$
\begin{aligned}
& p\left(\sigma^{2} \mid \mathbf{p}_{A} \mathbf{s}, \mathbf{h}, \mathbf{y}\right) \\
& \propto p\left(\sigma^{2}\right) p\left(\mathbf{y} \mid \mathbf{p}_{A}, \mathbf{s}, \mathbf{h}, \sigma^{2}\right) \\
& \propto\left(\sigma^{2}\right)^{-\alpha_{0}-1} \exp \left(-\frac{\beta_{0}}{\sigma^{2}}\right) \\
& \prod_{m_{r=1}}^{M_{r}} \frac{1}{\sigma^{2 N K}} \exp \left\{-\frac{1}{\sigma^{2}}\left\|\mathbf{y}_{m_{r}}-\sum_{m_{t=1}}^{M_{t}} \mathbf{D}_{m_{t}} \mathbf{W} \mathbf{h}_{m_{t}, m_{r}}\right\|^{2}\right\} \\
& \propto\left(\sigma^{2}\right)^{-\left(\alpha_{0}+M_{r} N K\right)-1} \\
& \cdot \exp \left(-\frac{\beta_{0}+\sum_{m_{r=1}}^{M_{r}}\left\|\mathbf{y}_{m_{r}}-\sum_{m_{t=1}}^{M_{t}} \mathbf{D}_{m_{t}} \mathbf{W} \mathbf{h}_{m_{t}, m_{r}}\right\|}{\sigma^{2}}\right) \\
& \sim \mathcal{2 G}(\alpha, \beta)
\end{aligned}
$$

where $\alpha=\alpha_{0}+N K M_{r}$ and $\beta=\beta_{0}+$ $\sum_{m_{r}}\left\|\mathbf{y}_{m_{r}}-\sum_{m_{t}} \mathbf{D}_{m_{t}} \hat{\mathbf{h}}_{m_{t}, m_{r}}\right\|^{2}$.

## APPENDIX III

## EVALUATION OF (29)

By taking expectation with respect to updated distribution $q\left(\mathbf{p}_{\mathbf{A}}\right)$ and $q\left(\mathbf{s}[n, k] \backslash s_{m_{t}}[n, k], \mathbf{h}, \sigma^{2}\right)$ receptively, it can be shown that the expression for $\left\langle\ln p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}\right)\right\rangle_{\mathbf{p}_{A}}$ is

$$
\begin{aligned}
& \left\langle\ln p\left(s_{m_{t}}[n, k] \mid \mathbf{p}_{A}\right)\right\rangle_{q\left(\mathbf{p}_{\mathbf{A}}\right)} \\
= & \sum_{a \in \mathcal{A}} \mathbf{1}\left(s_{m_{t}}[n, k] \in a\right)\left[\psi\left(\gamma_{a}\right)-\psi\left(\gamma_{0}\right)-\ln |a|\right]
\end{aligned}
$$

where $\gamma_{0}=\sum_{a \in \mathcal{A}} \gamma_{a}$; and the expression for $\left\langle\ln p\left(\mathbf{y}[n, k] \mid \mathbf{s}[n, k], \mathbf{H}[n], \sigma^{2}\right)\right\rangle$ is

$$
\begin{aligned}
& \left\langle\ln p\left(\mathbf{y}[n, k] \mid \mathbf{s}[n, k], \mathbf{H}[n], \sigma^{2}\right)\right\rangle_{q\left(\mathbf{s}[n, k] \backslash s_{m_{t}}[n, k], \mathbf{h}, \sigma^{2}\right)} \\
& \propto \frac{\alpha}{2}\left\{2 \operatorname{real}\left[\mathbf{y}^{H}[n, k]\right]\langle\mathbf{H}[n]\rangle\langle\mathbf{s}[n, k]\rangle_{q\left(\mathbf{s}[n, k] \backslash s_{m_{t}}[n, k]\right)}\right. \\
& -\operatorname{tr}\left(\left\langle\mathbf{H}^{H}[n] \mathbf{H}[n]\right\rangle \operatorname{cov}(\mathbf{s}[n, k])\right) \\
& -\langle\mathbf{s}[n, k]\rangle_{q\left(\mathbf{s}[n, k] \backslash s_{m_{t}}[n, k]\right)}^{H} \\
& \left.\cdot\left\langle\mathbf{H}^{H}[n] \mathbf{H}[n]\right\rangle\langle\mathbf{s}[n, k]\rangle_{q\left(\mathbf{s}[n, k] \backslash s_{m_{t}}[n, k]\right)}\right\}
\end{aligned}
$$

with the $\left(m_{t}^{\prime}, m_{t}^{\prime \prime}\right)$ element of the covariance matrix of the vector $\mathbf{s}[n, k]$

$$
\begin{aligned}
& \operatorname{cov}(\mathbf{s}[n, k])\left(m_{t}^{\prime}, m_{t}^{\prime \prime}\right) \\
= & \operatorname{var}\left(s_{m_{t}^{\prime}}[n, k]\right) \\
= & \left\{\begin{array}{ll}
\left\langle\left|s_{m_{t}^{\prime}}[n, k]\right|^{2}\right\rangle-\left\langle\left|s_{m_{t}^{\prime}}[n, k]\right|\right\rangle^{2}, & \text { if } m_{t}^{\prime}=m_{t}^{\prime \prime} \\
0, & m_{t}^{\prime \prime} \neq m_{t} \\
\text { otherwise. }
\end{array}\right.
\end{aligned}
$$

the $m_{t}^{\prime}$-th element of $\langle\mathbf{s}[n, k]\rangle_{q\left(\mathbf{s}[n, k] \backslash s_{m_{t}}[n, k]\right)}$ being

$$
\langle\mathbf{s}[n, k]\rangle_{\left(m_{t}^{\prime}\right)}= \begin{cases}\left\langle s_{m_{t}^{\prime}}[n, k]\right\rangle, & \text { if } m_{t}^{\prime} \neq m_{t} \\ s_{m_{t}}[n, k], & \text { if } m_{t}^{\prime}=m_{t}\end{cases}
$$

the $\left(m_{r}^{\prime}, m_{t}^{\prime}\right)$ element of $\langle\mathbf{H}[n]\rangle$ being the $n$-th element of the matrix product $\mathbf{W} \hat{\mathbf{h}}_{\mathbf{m}_{t}^{\prime}, \mathbf{m}_{t}^{\prime}}$, and the $\left(m_{t}^{\prime}, m_{t}^{\prime \prime}\right)$ element of $\left\langle\mathbf{H}^{H}[n] \mathbf{H}[n]\right\rangle$ being

$$
\begin{aligned}
& {\left[\left\langle\mathbf{H}^{H}[n] \mathbf{H}[n]\right\rangle\right]_{\left(m_{t}^{\prime}, m_{t}^{\prime \prime}\right)}=} \\
& \left\{\begin{array}{ll}
\sum_{m_{r}=1}^{M_{r}}\left\{\operatorname{tr}\left[\left[\mathbf{W}_{\left(n_{:}\right)}\right]^{H} \mathbf{W}_{\left(n_{:}\right)} \boldsymbol{\Sigma}_{m_{t}^{\prime \prime}, m_{r}}\right]+\right. \\
\left\langle\mathbf{h}_{m_{t}^{\prime \prime}, m_{r}}\right\rangle^{H}\left[\mathbf{W}_{\left(n_{:}\right)}\right]^{H} \mathbf{W}_{\left(n_{:}\right)}\left\langle\mathbf{h}_{m_{t}^{\prime \prime}, m_{r}}\right\rangle\right\}, & \text { if } m_{t}^{\prime}=m_{t}^{\prime \prime} \\
\langle\mathbf{H}[n]\rangle_{\left(\cdot, m_{t}^{\prime}\right)}\langle\mathbf{H}[n]\rangle_{\left(\cdot, m_{t}^{\prime \prime}\right)}, & \text { if } m_{t}^{\prime} \neq m_{t}^{\prime \prime}
\end{array}\right.
\end{aligned}
$$
