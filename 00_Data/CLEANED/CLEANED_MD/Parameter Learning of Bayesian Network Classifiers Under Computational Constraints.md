# Parameter Learning of Bayesian Network Classifiers Under Computational Constraints 

Sebastian Tschiatschek ${ }^{1(\boxtimes)}$ and Franz Pernkopf ${ }^{2}$<br>${ }^{1}$ Learning and Adaptive Systems Group, ETH Zurich, Zürich, Switzerland<br>sebastian.tschiatschek@inf.ethz.ch<br>${ }^{2}$ Signal Processing and Speech Communication Laboratory, Graz University of Technology, Graz, Austria<br>pernkopf@tugraz.at


#### Abstract

We consider online learning of Bayesian network classifiers (BNCs) with reduced-precision parameters, i.e. the conditional-probability tables parameterizing the BNCs are represented by low bit-width fixed-point numbers. In contrast to previous work, we analyze the learning of these parameters using reduced-precision arithmetic only which is important for computationally constrained platforms, e.g. embeddedand ambient-systems, as well as power-aware systems. This requires specialized algorithms since naive implementations of the projection for ensuring the sum-to-one constraint of the parameters in gradient-based learning are not sufficiently accurate. In particular, we present generative and discriminative learning algorithms for BNCs relying only on reduced-precision arithmetic. For several standard benchmark datasets, these algorithms achieve classification-rate performance close to that of BNCs with parameters learned by conventional algorithms using doubleprecision floating-point arithmetic. Our results facilitate the utilization of BNCs in the foresaid systems.


Keywords: Bayesian network classifiers $\cdot$ Reduced-precision $\cdot$ Resourceconstrained computation $\cdot$ Generative/discriminative learning

## 1 Introduction

Most commonly Bayesian network classifiers (BNCs) are implemented on nowadays desktop computers, where double-precision floating-point numbers are used for parameter representation and arithmetic operations. In these BNCs, inference and classification is typically performed using the same precision for parameters and operations, and the executed computations are considered as exact. However, there is a need for BNCs working with limited computational resources. Such resource-constrained BNCs are important in domains such as ambient computing, on-satellite computations ${ }^{1}$ or acoustic environment classification in hearing

[^0]
[^0]:    F. Pernkopf-This work was supported by the Austrian Science Fund (FWF) under the project number P25244-N15.
    ${ }^{1}$ Computational capabilities on satellites are still severely limited due to power constraints and restricted availability of hardware satisfying the demanding requirements with respect to radiation tolerance.
    (C) Springer International Publishing Switzerland 2015
    A. Appice et al. (Eds.): ECML PKDD 2015, Part I, LNAI 9284, pp. 86-101, 2015.

    DOI: 10.1007/978-3-319-23528-8_6

aids, machine learning for prosthetic control, e.g. a brain implant to control hand movements, amongst others. In all these applications, a trade-off between accuracy and required computational resources is essential.

In this paper, we investigate BNCs with limited computational demands by considering BNCs with reduced-precision parameters, i.e. fixed-point parameters with limited precision. ${ }^{2}$ Using reduced-precision parameters is advantageous in many ways, e.g. power consumption compared to full-precision implementations can be reduced [20] and reduced-precision parameters enable one to implement many BNCs in parallel on field programmable gate arrays (FPGAs), i.e. the circuit area requirements on the FPGA correlate with the parameter precision [9]. Our investigations are similar to those performed in digital signal-processing, where reduced-precision implementations for digital signal processors are of great importance [10]. Note that there is also increased interest in implementing other machine learning models, e.g. neural networks, using reduced-precision parameters/computations to achieve faster training and to facilitate the implementation of larger models $[2,18]$.

We are especially interested in learning the reduced-precision parameters using as little computational resources as possible. To decide on how to perform this learning, several questions should be answered. Should reduced-precision parameters be learned in a pre-computation step in which we can exploit the full computational power of nowadays computers? Or is it necessary to learn/adopt parameters using reduced-precision arithmetic only? The answers to these questions depend on the application of interest and identify several learning scenarios that are summarized in Figure 1. In the following, we discuss these scenarios briefly:
(a) Training and testing using full-precision arithmetic. This corresponds to what machine learners typically do, i.e. all computations are performed using full-precision arithmetic.
(b) Training using reduced-precision and testing using full-precision arithmetic. A rash thought rejects this option. But it might be interesting in the vicinity of big-data where the amount of data is so huge that it can only be processed in a compressed form, i.e. in reduced-precision.
(c) Training using full-precision and testing using reduced-precision arithmetic. This describes an application scenario where BNCs with precomputed parameters can be used, e.g. hearing-aids for auditory scene classification. This scenario enables one to exploit large computational resources for parameter learning, while limiting computational demands at test time. Recent work considered this for BNCs [22].
(d) Training and testing using reduced-precision arithmetic. This is the scenario considered within this paper. It opens the door to many interesting applications, e.g. continuous parameter adaptation in hearing-aids using reduced-precision computations only. Another example could be a

[^0]
[^0]:    ${ }^{2}$ We are interested in fixed-point arithmetic and not in floating-point arithmetic, because typically the implementation of fixed-point processing units requires less resources than the implementation of floating-point processing units.

Training


Fig. 1. Combinations of training/testing using full-precision/reduced-precision arithmetic.
satellite-based system for remote sensing that tunes its parameter according to changing atmospheric conditions.

We start our investigation of parameter learning using reduced-precision computations by analyzing the effect of approximate computations on online parameter learning. This leads to the observation that the approximate projections needed in the used projected gradient ascent/descent algorithms to ensure the sum-to-one normalization constraints of the parameters can severely affect the learning process. We circumvent the need for these projections by proposing special purpose learning algorithms for generative maximum likelihood (ML) and discriminative maximum margin (MM) parameters.

This paper is structured as follows: In Section 2 we consider related work, followed by an introduction of the used notation and some background on parameter learning in Bayesian networks (BNs) in Section 3. We derive our proposed algorithms in Section 4 and test them in experiments in Section 5. In Section 6 we conclude the paper.

# 2 Related Work 

For undirected graphical models, approximate inference and learning using integer parameters has been proposed [16]. While undirected graphical models are more amenable to integer approximations mainly due to the absence of sum-toone constraints, there are domains where probability distributions represented by directed graphical models are desirable, e.g. in expert systems in the medical domain.

Directly related work can be summarized as follows:

- The feasibility of BNCs with reduced-precision floating-point parameters has been empirically investigated in [14,24]. These papers analyzed (i) the effect of precision-reduction of the parameters on the classification performance of BNCs, and (ii) how BNCs with reduced-precision parameters can be implemented using integer computations only.
- The above mentioned experimental studies where extended by a thorough theoretical analysis of using fixed-point parameters in BNCs [23]. The authors used fixed-point numbers for the following two reasons: First, because fixed-point parameters can even be used on computing platforms without floating-point processing capabilities. Second, because summation of fixed-point numbers is exact (neglecting the possibility of overflows), while summation of floating-point numbers is in general not exact.
In particular, theoretical bounds on the classification performance when using reduced-precision fixed-point parameters have been analyzed in [21, 23]. The authors derived worst-case and probabilistic bounds on the classification rate (CR) for different bit-widths. Furthermore, they compared the classification performance and the robustness of BNCs with generatively and discriminatively optimized parameters, i.e. parameters optimized for high data likelihood and parameters optimized for classification, with respect to parameter quantization.
- In [22], learning of reduced-precision parameters using full-precision computations was addressed while the work mentioned above considers only rounding of double-precision parameters. An algorithm for the computation of MM reduced-precision parameters was presented and its efficiency was demonstrated. The resulting parameters had superior classification performance compared to parameters obtained by simple rounding of double-precision parameters, particularly for very low numbers of bits.


# 3 Background and Notation 

Probabilistic Classification. Probabilistic classifiers are embedded in the framework of probability theory. One assumes a random variable (RV) $C$ denoting the class and RVs $X_{1}, \ldots, X_{L}$ representing the attributes/features of the classifier. Each $X_{i}$ can take one value in the set $\operatorname{val}\left(X_{i}\right)$. Similarly, $C$ can assume values in $\operatorname{val}(C)$, i.e. $\operatorname{val}(C)$ is the set of classes. We denote the random vector consisting of $X_{1}, \ldots, X_{L}$ as $\mathbf{X}=\left(X_{1}, \ldots, X_{L}\right)$. Instantiations of RVs are denoted using lower case letters, i.e. $\mathbf{x}$ is an instantiation of $\mathbf{X}$ and $c$ an instantiation of $C$, respectively. The RVs $C, X_{1}, \ldots, X_{L}$ are assumed to be jointly distributed according to the distribution $\mathrm{P}^{*}(C, \mathbf{X})$. In typical settings, $\mathrm{P}^{*}(C, \mathbf{X})$ is unknown, but a number of samples drawn iid from $\mathrm{P}^{*}(C, \mathbf{X})$ is at hand, i.e. a training set $\mathcal{D}=\left(\left(c^{(n)}, \mathbf{x}^{(n)}\right) \mid 1 \leq n \leq N\right)$, where $c^{(n)}$ denotes the instantiation of the RV $C$ and $\mathbf{x}^{(n)}$ the instantiation of $\mathbf{X}$ in the $n^{\text {th }}$ training sample. The aim is to induce good classifiers provided the training set, i.e. classifiers with low generalization error. Any probability distribution $\mathrm{P}(C, \mathbf{X})$

naturally induces a classifier $h_{\mathrm{P}(C, \mathbf{X})}$ according to $h_{\mathrm{P}(C, \mathbf{X})}: \operatorname{val}(\mathbf{X}) \rightarrow \operatorname{val}(C)$, $\mathbf{x} \mapsto \arg \max _{c^{\prime} \in \operatorname{val}(C)} \mathrm{P}\left(c^{\prime} \mid \mathbf{x}\right)$. In this way, each instantiation $\mathbf{x}$ of $\mathbf{X}$ is classified by the maximum a-posteriori (MAP) estimate of $C$ given $\mathbf{x}$ under $\mathrm{P}(C, \mathbf{X})$. Note that $\arg \max _{c^{\prime} \in \operatorname{val}(C)} \mathrm{P}\left(c^{\prime} \mid \mathbf{x}\right)=\arg \max _{c^{\prime} \in \operatorname{val}(C)} \mathrm{P}\left(c^{\prime}, \mathbf{x}\right)$.

Bayesian Networks and Bayesian Network Classifiers. We consider probability distributions represented by BNs $[7,11]$. A BN $\mathcal{B}=\left(\mathcal{G}, \mathcal{P}_{\mathcal{G}}\right)$ consists of a directed acyclic graph (DAG) $\mathcal{G}=(\mathbf{Z}, \mathbf{E})$ and a collection of conditional probability distributions $\mathcal{P}_{\mathcal{G}}=\left(\mathrm{P}\left(X_{0} \mid \mathbf{P a}\left(X_{0}\right)\right), \ldots, \mathrm{P}\left(X_{L} \mid \mathbf{P a}\left(X_{L}\right)\right)\right)$, where the terms $\mathbf{P a}\left(X_{i}\right)$ denote the set of parents of $X_{i}$ in $\mathcal{G}$. The nodes $\mathbf{Z}=\left(X_{0}, \ldots, X_{L}\right)$ correspond to RVs and the edges $\mathbf{E}$ encode conditional independencies among these RVs. Throughout this paper, we often denote $X_{0}$ as $C$, i.e. $X_{0}$ represents the class. Then, a BN defines the joint distribution

$$
\mathrm{P}^{\mathcal{B}}\left(C, X_{1}, \ldots, X_{L}\right)=\mathrm{P}(C \mid \mathbf{P a}(C)) \prod_{i=1}^{L} \mathrm{P}\left(X_{i} \mid \mathbf{P a}\left(X_{i}\right)\right)
$$

According to the joint distribution, a BN $\mathcal{B}$ induces the classifier $h_{\mathcal{B}}=h_{\mathrm{P}^{\mathcal{B}}(C, \mathbf{X})}$.
In this paper, we assume discrete valued RVs only. Then, a general representation of $\mathcal{P}_{\mathcal{G}}$ is a collection of conditional probability tables (CPTs), i.e. $\mathcal{P}_{\mathcal{G}}=\left(\boldsymbol{\theta}^{0}, \ldots, \boldsymbol{\theta}^{L}\right)$, with $\boldsymbol{\theta}^{i}=\left(\theta_{j \mid \mathbf{h}}^{i} \mid j \in \operatorname{val}\left(X_{i}\right), \mathbf{h} \in \operatorname{val}\left(\mathbf{P a}\left(X_{i}\right)\right)\right)$, where $\theta_{j \mid \mathbf{h}}^{i}=\mathrm{P}\left(X_{i}=j \mid \mathbf{P a}\left(X_{i}\right)=\mathbf{h}\right)$. The BN distribution can then be written as

$$
\mathrm{P}^{\mathcal{B}}(C=c, \mathbf{X}=\mathbf{x})=\prod_{i=0}^{L} \prod_{j \in \operatorname{val}\left(X_{i}\right)} \prod_{\mathbf{h} \in \operatorname{val}\left(\mathbf{P a}\left(X_{i}\right)\right)} \theta_{j \mid \mathbf{h}}^{i} \nu_{j \mid \mathbf{h}}^{i}
$$

where $\nu_{j \mid \mathbf{h}}^{i}=\mathbf{1}_{\left([c, \mathbf{x}]\left(X_{i}\right)=j\right.}$ and $\left.[c, \mathbf{x}]\left(\mathbf{P a}\left(X_{i}\right)\right)=\mathbf{h}\right) .{ }^{3}$ We typically represent the BN parameters in the logarithmic domain, i.e. $w_{j \mid \mathbf{h}}^{i}=\log \theta_{j \mid \mathbf{h}}^{i}, \mathbf{w}^{i}=\left(w_{j \mid \mathbf{h}}^{i} \mid j \in\right.$ $\left.\operatorname{val}\left(X_{i}\right), \mathbf{h} \in \operatorname{val}\left(\mathbf{P a}\left(X_{i}\right)\right)\right)$, and $\mathbf{w}=\left(\mathbf{w}^{0}, \ldots, \mathbf{w}^{L}\right)$. In general, we will interpret $\mathbf{w}$ as a vector, whose elements are addressed as $w_{j \mid \mathbf{h}}^{i}$. We define a vector-valued function $\boldsymbol{\phi}(c, \mathbf{x})$ of the same length as $\mathbf{w}$, collecting $\nu_{j \mid \mathbf{h}}^{i}$, analog to the entries $w_{j \mid \mathbf{h}}^{i}$ in $\mathbf{w}$. In that way, we can express the logarithm of (2) as

$$
\log \mathrm{P}^{\mathcal{B}}(C=c, \mathbf{X}=\mathbf{x})=\boldsymbol{\phi}(c, \mathbf{x})^{T} \mathbf{w}
$$

Consequently, classification, can be performed by simply adding the logprobabilities corresponding to an instantiation $[c, \mathbf{x}]$ for all $c \in \operatorname{val}(C) .{ }^{4}$

Fixed-Point Numbers. Fixed-point numbers are essentially integers scaled by a constant factor, i.e. the fractional part has a fixed number of digits. We characterize fixed-point numbers by the number of integer bits $b_{i}$ and the number

[^0]
[^0]:    ${ }^{3}$ Note that $[c, \mathbf{x}]$ denotes the joint instantiation of $C$ and $\mathbf{X}$ and $[c, \mathbf{x}](\mathbf{A})$ corresponds to the subset of values of $[c, \mathbf{x}]$ indexed by $\mathbf{A} \subseteq\left\{X_{0}, \ldots, X_{L}\right\}$.
    ${ }^{4}$ In general graphs, potentially with latent variables, the needed inference can be performed using max-sum message passing $[7,13]$.

of fractional bits $b_{f}$. The addition of two fixed-point numbers can be easily and accurately performed, while the multiplication of two fixed-point numbers often leads to overflows and requires truncation to achieve results in the same format.

# Learning Bayesian Network Classifiers 

BNs for classification can be optimized in two ways: firstly, one can select the graph structure $\mathcal{G}$ (structure learning), and secondly, one can learn the conditional probability distributions $\mathcal{P}_{\mathcal{G}}$ (parameter learning). In this paper, we consider fixed structures of the BNCs, namely naive Bayes (NB) and tree augmented network (TAN) structures [4], i.e. 1-tree among the attributes. The NB structure implies conditional independence of the features, given the class. Obviously, this conditional independence assumption is often violated in practice. TAN structures relax these strong independence assumptions, enabling better classification performance. ${ }^{5}$

Parameter Learning. The conditional probability densities (CPDs) $\mathcal{P}_{\mathcal{G}}$ of BNs can be optimized either generatively or discriminatively. Two standard approaches for optimizing $\mathcal{P}_{\mathcal{G}}$ are:

- Generative Maximum Likelihood Parameters. In generative parameter learning one aims at identifying parameters modeling the generative process that results in the data of the training set, i.e. generative parameters are based on the idea of approximating $\mathrm{P}^{*}(C, \mathbf{X})$ by a distribution $\mathrm{P}^{\mathcal{B}}(C, \mathbf{X})$. An example of this paradigm is maximum likelihood (ML) learning. Its objective is maximization of the likelihood of the training data given the parameters, i.e.

$$
\mathcal{P}_{\mathcal{G}}^{\mathrm{ML}}=\arg \max _{\mathcal{P}_{\mathcal{G}}} \prod_{n=1}^{N} \mathrm{P}^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)
$$

Note that the above optimization problem implicitly includes sum-to-one constraints because the learned parameters in $\mathcal{P}_{\mathcal{G}}^{\mathrm{ML}}$ must represent normalized probabilities. Maximum likelihood parameters minimize the KullbackLeibler (KL)-divergence between $\mathrm{P}^{\mathcal{B}}(C, \mathbf{X})$ and $\mathrm{P}^{*}(C, \mathbf{X})$ [7].

- Discriminative Maximum Margin Parameters [5,12,15]. In discriminative learning one aims at identifying parameters leading to good classification performance on new samples from $\mathrm{P}^{*}(C, \mathbf{X})$. This type of learning is for example advantageous in cases where the assumed model distribution $\mathrm{P}^{\mathcal{B}}(C, \mathbf{X})$ cannot approximate $\mathrm{P}^{*}(C, \mathbf{X})$ well, for example because of a too limited BN structure [17].
Discriminative MM parameters $\mathcal{P}_{\mathcal{G}}^{\mathrm{MM}}$ are found as

$$
\mathcal{P}_{\mathcal{G}}^{\mathrm{MM}}=\arg \max _{\mathcal{P}_{\mathcal{G}}} \prod_{n=1}^{N} \min \left(\gamma, d^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)\right)
$$

[^0]
[^0]:    ${ }^{5}$ Note that the parameter learning approach can be applied to more complex structures, e.g. $k$-trees among the attributes.

where $d^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)$ is the margin of the $n^{\text {th }}$ sample given as

$$
d^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)=\frac{\mathrm{P}^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)}{\max _{c \neq c^{(n)}} \mathrm{P}^{\mathcal{B}}\left(c, \mathbf{x}^{(n)}\right)}
$$

and where the hinge loss function is denoted as $\min \left(\gamma, d^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)\right)$. The parameter $\gamma>1$ controls the margin. In this way, the margin measures the ratio of the likelihood of the $n^{\text {th }}$ sample belonging to the correct class $c^{(n)}$ to the likelihood of belonging to the most likely competing class. The $n^{\text {th }}$ sample is correctly classified iff $d^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)>1$ and vice versa.

# 4 Algorithms for Online Learning of Reduced-Precision Parameters 

We start by considering learning ML parameters in Section 4.1 and then move on to learning MM parameters in Section 4.2. We claim that learning using reducedprecision arithmetic is most useful in online settings, i.e. parameters are updated on a per-sample basis. This online learning scenario captures the important case in which initially pre-computed parameters are used and these parameters are updated online as new samples become available, e.g. adaptation of a hearing-aid to a new acoustic environment. In this setting, learning using reduced-precision computations requires specialized algorithms, i.e. gradient-descent (or gradientascent) procedures using reduced-precision arithmetic do not perform well. The reason is that the necessary exact projections of the parameters onto the sum-to-one constraints cannot be accurately performed. Another issue is the limited resolution of the learning rate. However, we find this issue less important as the inexact projections.

### 4.1 Learning Maximum Likelihood Parameters

We consider an online algorithm for learning ML parameters. The ML objective (4) for the offline scenario can be equivalently written as

$$
\mathbf{w}^{\mathrm{ML}}=\arg \max _{\mathbf{w}} \sum_{n=1}^{N} \boldsymbol{\phi}\left(c^{(n)}, \mathbf{x}^{(n)}\right)^{T} \mathbf{w} \quad \text { s.t. } \sum_{j} \exp \left(w_{j \mid \mathbf{h}}^{i}\right)=1, \forall i, j, \mathbf{h}
$$

where optimisation is performed over the log-parameters $\mathbf{w}$. In an online scenario, not all samples are available for learning at once but are available one at a time; the parameters $\mathbf{w}^{\mathrm{ML}, t}$ at time-step $t$ are updated according to the gradient of a single sample $(c, \mathbf{x})$ (or, alternatively, a batch of samples) and projected such that they satisfy the sum-to-one constraints, i.e.

$$
\begin{aligned}
\mathbf{w}^{\mathrm{ML}, t+1} & =\Pi\left[\mathbf{w}^{\mathrm{ML}, t}+\eta\left(\nabla_{\mathbf{w}} \boldsymbol{\phi}(c, \mathbf{x})^{T} \mathbf{w}\right)\left(\mathbf{w}^{\mathrm{ML}, t}\right)\right] \\
& =\Pi\left[\mathbf{w}^{\mathrm{ML}, t}+\eta \boldsymbol{\phi}(c, \mathbf{x})\right]
\end{aligned}
$$

where $\eta$ is the learning rate, $\nabla_{\mathbf{w}}(f)(\mathbf{a})$ denotes the gradient of $f$ with respect to $\mathbf{w}$ at $\mathbf{a}$, and $\Pi[\mathbf{w}]$ denotes the $\ell_{2}$-norm projection of the parameter vector $\mathbf{w}$ onto the set of normalized parameter vectors. Note that the gradient has a simple form: it consists only of zeros and ones, where the ones are indicators of active entries in the CPTs of sample $(c, \mathbf{x})$. Furthermore, assuming normalized parameters at time-step $t$, the direction of the gradient is always such that the parameters $\mathbf{w}^{\mathrm{ML}, t+1}$ are super-normalized. Consequently, after (exact) projection the parameters satisfy the sum-to-one constraints.

We continue by analyzing the effect of using reduced-precision arithmetic on the online learning algorithm. Therefore, we performed the following experiment: Assume that the projection can only be approximately performed. We simulate the approximate projection by performing an exact projection and subsequently adding quantization noise (this is similar to reduced-precision analysis in signal processing [10]). We sample the noise from a Gaussian distribution with zero mean and with variance $\sigma^{2}=q^{2} / 12$, where $q=2^{-b_{f}}$. For the satimage dataset from the UCI repository [1] we construct BNCs with TAN structure. As initial parameters we use rounded ML parameters computed from one tenth of the training data. Then, we present the classifier further samples in an online manner and update the parameters according to (9). During learning, we set the learning rate $\eta$ to $\eta=\eta_{0} / \sqrt{1+t}$, where $\eta_{0}$ is some constant ( $\eta_{0}$ is tuned by hand such that the test set performance is maximized). The resulting classification performance is shown in Figures 2a and 2b for the exact and the approximate projection, respectively. One can observe, that the algorithm does not properly learn using the approximate projection. Thus, it seems crucial to perform the projections rather accurately. To circumvent the need for accurate projections, we propose a method that avoids computing a projection at all in the following.

Consider again the offline parameter learning case. ML parameters can be computed in closed-form by computing relative frequencies, i.e.

$$
\theta_{j \mid \mathbf{h}}^{i}=\frac{m_{j \mid \mathbf{h}}^{i}}{m_{\mathbf{h}}^{i}}
$$

where

$$
m_{j \mid \mathbf{h}}^{i}=\sum_{n=1}^{N} \boldsymbol{\phi}\left(c^{(n)}, \mathbf{x}^{(n)}\right)_{j \mid \mathbf{h}}^{i}, \text { and } m_{\mathbf{h}}^{i}=\sum_{j} m_{j \mid \mathbf{h}}^{i}
$$

This can be easily extended to online learning. Assume that the counts $m_{j \mid \mathbf{h}}^{i, t}$ at time $t$ are given and that a sample $\left(c^{t}, \mathbf{x}^{t}\right)$ is presented to the learning algorithm. Then, the counts are updated according to

$$
m_{j \mid \mathbf{h}}^{i, t+1}=m_{j \mid \mathbf{h}}^{i, t}+\boldsymbol{\phi}\left(c^{t}, \mathbf{x}^{t}\right)_{j \mid \mathbf{h}}^{i}
$$

![img-0.jpeg](img-0.jpeg)
(a) exact projection
![img-1.jpeg](img-1.jpeg)
(c) proposed algorithm

Fig. 2. Classification performance of BNCs with TAN structure for satimage data in an online learning scenario; (a) Online ML parameter learning with exact projection after each parameter update, (b) online ML parameter learning with approximate projection after each parameter update (see text for details), (c) proposed algorithm for online ML parameter learning.

Exploiting these counts, the logarithm of the ML parameters $\theta_{j \mid \mathbf{h}}^{i, t}$ at time $t$ can be computed as

$$
w_{j \mid \mathbf{h}}^{i, t}=\log \left(\frac{m_{j \mid \mathbf{h}}^{i, t}}{m_{\mathbf{h}}^{i, t}}\right)
$$

where similarly to before $m_{\mathbf{h}}^{i, t}=\sum_{j} m_{j \mid \mathbf{h}}^{i, t}$. A straightforward approximation of (13) is to (approximately) compute the counts $m_{j \mid \mathbf{h}}^{i, t}$ and $m_{\mathbf{h}}^{i, t}$, respectively, and to use a lookup table to determine $w_{j \mid \mathbf{h}}^{i, t}$. The lookup table can be indexed in terms of $m_{j \mid \mathbf{h}}^{i, t}$ and $m_{\mathbf{h}}^{i, t}$ and stores values for $w_{j \mid \mathbf{h}}^{i, t}$ in the desired reduced-precision format. To limit the maximum size of the lookup table and the bit-width required for the counters for $m_{j \mid \mathbf{h}}^{i, t}$ and $m_{\mathbf{h}}^{i, t}$, we assume some maximum integer number $M$. We pre-compute the lookup table $L$ such that

$$
L(i, j)=\left[\frac{\log _{2}(i / j)}{q}\right]_{R} \cdot q
$$

where $[\cdot]_{R}$ denotes rounding to the closest the integer, $q$ is the quantization interval of the desired fixed-point representation, $\log _{2}(\cdot)$ denotes the base-2 logarithm, and where $i$ and $j$ are in the range $0, \ldots, M-1$. Given sample $\left(c^{t}, \mathbf{x}^{t}\right)$, the counts $m_{j \mid \mathbf{h}}^{i, t+1}$ and $m_{\mathbf{h}}^{i, t+1}$ are computed according to Algorithm 1 from the counts $m_{j \mid \mathbf{h}}^{i, t}$ and $m_{\mathbf{h}}^{i, t}$. To guarantee that the counts stay in range, the algorithm identifies counters that reach their maximum value, and halfs these counters as well as all other counters corresponding to the same CPTs. This division by 2 can be implemented as a bitwise shift operation.

```
Algorithm 1. Reduced-precision ML online learning
Require: Old counts \(m_{j \mid \mathbf{h}}^{i, t}\); sample \(\left(c^{t}, \mathbf{x}^{t}\right)\)
    \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow m_{j \mid \mathbf{h}}^{i, t}+\boldsymbol{\phi}\left(c^{t}, \mathbf{x}^{t}\right)_{j \mid \mathbf{h}}^{i} \quad \forall i, j, \mathbf{h} \quad \triangleright\) update counts
    for \(i, j, \mathbf{h}\) do
        if \(m_{j \mid \mathbf{h}}^{i, t+1}=M\) then \(\triangleright\) maximum value of counter reached?
            \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow\left\lfloor m_{j \mid \mathbf{h}}^{i, t+1} / 2\right\rfloor \quad \forall j \quad \triangleright\) half counters of considered CPT (round down)
        end if
    end for
    return \(m_{j \mid \mathbf{h}}^{i, t+1}\)
```

Initially, we set all counts to zero, i.e. $m_{j \mid \mathbf{h}}^{i, 0}=0$, respectively. For the cumulative counts, i.e. $m_{\mathbf{h}}^{i, t}$ in (13), we did not limit the number of bits (for real implementations the necessary number of bits for this counter can be computed from the bit-width of the individual counters that are summed up and the graph structure of the considered BNC). Logarithmic parameters $w_{j \mid \mathbf{h}}^{i, t}$ are computed using the lookup table described above and using Algorithm 2. The classification performance during online learning is shown in Figure 2c. We can observe, that the algorithm behaves pleasant and the limited range of the used counters does not seem to affect classification performance (compared to the classification performance using rounded ML parameters computed using full-precision computations and all training samples). Further experimental results can be found in Section 5 .

# 4.2 Learning Maximum Margin Parameters 

In this section, we consider a variant of the MM objective proposed in [12] that balances the MM objective (5) against the ML objective (4), i.e. the objective is to maximize

```
Algorithm 2. Computation of logarithmic probabilities from lookup table
Require: Counts \(m_{j \mid \mathbf{h}}^{i, t}\) and \(m_{\mathbf{h}}^{i, t}\); lookup table \(L\) of size \(M \times M\)
    \(\operatorname{div} \leftarrow 0\)
    while \(m_{\mathbf{h}}^{i, t} \geq M\) do \(\triangleright\) ensure that index into lookup table is in range
        \(m_{\mathbf{h}}^{i, t} \leftarrow\left\lfloor m_{\mathbf{h}}^{i, t} / 2\right\rfloor \quad \triangleright\) half and round down
        \(\operatorname{div} \leftarrow \operatorname{div}+1\)
    end while
    \(w_{j \mid \mathbf{h}}^{i, t} \leftarrow L\left(m_{j, \mathbf{h}}^{i, t}, m_{\mathbf{h}}^{i, t}\right) \quad \forall j \quad \triangleright\) get log-probability from lookup table
    while \(\operatorname{div}>0\) and \(\forall j: w_{j \mid \mathbf{h}}^{i, t}>\left(-2^{b_{i}}+2^{b_{f}}\right)+1\) do \(\triangleright\) revise index correction
        \(w_{j \mid \mathbf{h}}^{i, t} \leftarrow w_{j \mid \mathbf{h}}^{i, t}-1 \quad \forall j\)
        \(\operatorname{div} \leftarrow \operatorname{div}-1\)
    end while
    return \(w_{j \mid \mathbf{h}}^{i, t}\)
```

$$
\underbrace{\log \left[\prod_{n=1}^{N} \mathrm{P}^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)\right]}_{\mathrm{ML}}+\underbrace{\lambda \log \left[\prod_{n=1}^{N} \min \left(\gamma, \frac{\mathrm{P}^{\mathcal{B}}\left(c^{(n)}, \mathbf{x}^{(n)}\right)}{\max _{c \neq c^{(n)}} \mathrm{P}^{\mathcal{B}}\left(c, \mathbf{x}^{(n)}\right)}\right)\right]}_{\mathrm{MM}}
$$

In this way, generative properties, e.g. the ability to marginalize over missing features, are combined with good discriminative performance. This variant of the MM objective can be easily written in the form

$$
\begin{aligned}
\mathbf{w}^{\mathrm{MM}}=\arg \max _{\mathbf{w}}[ & \sum_{n=1}^{N} \boldsymbol{\phi}\left(c^{(n)}, \mathbf{x}^{(n)}\right)^{T} \mathbf{w}+ \\
& \lambda \sum_{n=1}^{N} \min \left(\gamma, \min _{c \neq c^{(n)}}\left[\left(\boldsymbol{\phi}\left(c^{(n)}, \mathbf{x}^{(n)}\right)-\boldsymbol{\phi}\left(c, \mathbf{x}^{(n)}\right)\right)^{T} \mathbf{w}\right]\right)
\end{aligned}
$$

and, for simplicity, we will refer to this modified objective as the MM objective. Note that there are implicit sum-to-one constraints in problem (16), i.e. any feasible solution $\mathbf{w}$ must satisfy $\sum_{j} \exp \left(w_{j \mid \mathbf{h}}^{i}\right)=1$ for all $i, j, \mathbf{h}$. In the online learning case, given sample $(c, \mathbf{x})$, the parameters $\mathbf{w}^{\mathrm{MM}, t+1}$ at time $t+1$ are computed from the parameters $\mathbf{w}^{\mathrm{MM}, t}$ at time $t$ as

$$
\mathbf{w}^{\mathrm{MM}, t+1}=\Pi\left[\mathbf{w}^{\mathrm{MM}, t}+\eta \boldsymbol{\phi}(c, \mathbf{x})+\eta \lambda \mathbf{g}(c, \mathbf{x})\right]
$$

where

$$
\mathbf{g}(c, \mathbf{x})= \begin{cases}0 & \min _{c^{\prime} \neq c}\left[\left(\boldsymbol{\phi}(c, \mathbf{x})-\boldsymbol{\phi}\left(c^{\prime}, \mathbf{x}\right)\right)^{T} \mathbf{w}\right] \geq \gamma \\ \boldsymbol{\phi}(c, \mathbf{x})-\boldsymbol{\phi}\left(c^{\prime}, \mathbf{x}\right) & \text { o.w., } c^{\prime}=\arg \min _{c^{\prime}}\left[\left(\boldsymbol{\phi}(c, \mathbf{x})-\boldsymbol{\phi}\left(c^{\prime}, \mathbf{x}\right)\right)^{T} \mathbf{w}\right]\end{cases}
$$

and where similar as before $\Pi[\mathbf{w}]$ denotes the projection.

For learning MM parameters, a similar observation with respect to the accuracy of the projection can be made as for ML parameters. But we cannot proceed exactly as in the case of learning ML parameters because we cannot compute MM parameters in closed-form. As in the ML parameter learning case, the gradient for the parameter update has a rather simple form, but the projection to satisfy the sum-to-one constraints is difficult to compute. Therefore, for online MM parameter learning, we propose Algorithm 3 that is similar to Algorithm 1 in Section 4.1, i.e. we avoid to compute the projection explicitly. From the counts computed by the algorithm, log-probabilities can be computed using Algorithm 2. Note that the proposed algorithm does not exactly optimize (16) but a, not explicitly defined, surrogate. The idea behind the algorithm is (1) to optimize the likelihood term in (16) as in the algorithm for ML parameter learning, and (2) to optimize the margin term by increasing the likelihood for the correct class and simultaneously decreasing the likelihood for the strongest competitor class. Note that the idea of optimizing the margin term as explained above is similar in spirit to that of discriminative frequency estimates [19]. However, discriminative frequency estimates do not optimize a margin term but a term more closely related to the class-conditional likelihood.

# 5 Experiments 

### 5.1 Datasets

In our experiments, we considered the following datasets.

1. UCI data [1]. This is in fact a large collection of datasets, with small to medium number of samples. Features are discretized as needed using the algorithm proposed in [3]. If not stated otherwise, in case of the datasets chess, letter, mofn-3-7-10, segment, shuttle-small, waveform-21, abalone, adult, car, mushroom, nursery, and spambase, a test set was used to estimate the accuracy of the classifiers. For all other datasets, classification accuracy was estimated by 5 -fold cross-validation. Information on the number of samples, classes and features for each dataset can be found in [1].
2. USPS data [6]. This data set contains 11000 handwritten digit images from zip codes of mail envelopes. The data set is split into 8000 images for training and 3000 for testing. Each digit is represented as a $16 \times 16$ greyscale image. These greyscale values are discriminatively quantized [3] and each pixel is considered as feature.
3. MNIST Data [8]. This dataset contains 70000 samples of handwritten digits. In the standard setting, 60000 samples are used for training and 10000 for testing. The digits represented by grey-level images were down-sampled by a factor of two resulting in a resolution of $16 \times 16$ pixels, i.e. 196 features.

### 5.2 Results

We performed experiments using $M=1024$, i.e. we used counters with 10 bits $\left(b_{i}+b_{f}=10\right)$. The splitting of the available bits into integer bits and fractional bits was set using 10 -fold cross-validation. Experimental results for BNCs

```
Algorithm 3. Reduced-precision MM online learning
Require: Old counts \(m_{j \mid \mathbf{h}}^{i, t}\); sample \(\left(c^{t}, \mathbf{x}^{t}\right)\); hyper-parameters \(\gamma, \lambda \in \mathbb{N}_{+}\)for MM for-
    mulation
    \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow m_{j \mid \mathbf{h}}^{i, t}+\boldsymbol{\phi}\left(c^{t}, \mathbf{x}^{t}\right)_{j \mid \mathbf{h}}^{i} \quad \forall i, j, \mathbf{h} \quad \triangleright\) update counts (likelihood term)
    for \(i, j, \mathbf{h}\) do \(\triangleright\) ensure that parameters stay in range
        if \(m_{j \mid \mathbf{h}}^{i, t+1}=M\) then
            \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow\left\lfloor m_{j \mid \mathbf{h}}^{i, t+1} / 2\right\rfloor \quad \forall j\)
        end if
    end for
    \(c^{\prime} \leftarrow\) strongest competitor of class \(c\) for features \(\mathbf{x}\)
    if \(\left[\left(\boldsymbol{\phi}\left(c^{t}, \mathbf{x}^{(n)}\right)-\boldsymbol{\phi}\left(c^{\prime}, \mathbf{x}^{(n)}\right)\right)^{T} \mathbf{w}<\gamma\right]\) then
        \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow m_{j \mid \mathbf{h}}^{i, t} \quad \forall i, j, \mathbf{h}\)
        for \(k=1, \ldots, \lambda\) do \(\triangleright\) Add-up gradient in \(\lambda\) steps
            \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow m_{j \mid \mathbf{h}}^{i, t+1}+\boldsymbol{\phi}\left(c^{t}, \mathbf{x}^{t}\right)_{j \mid \mathbf{h}}^{i} \quad \forall i, j, \mathbf{h} \quad \triangleright\) update counts (margin term)
            \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow m_{j \mid \mathbf{h}}^{i, t+1}-\boldsymbol{\phi}\left(c^{\prime}, \mathbf{x}^{t}\right)_{j \mid \mathbf{h}}^{i} \quad \forall i, j, \mathbf{h} \quad \triangleright\) update counts (margin term)
            for \(i, j, \mathbf{h}\) do \(\triangleright\) ensure that parameters stay in range
                if \(m_{j \mid \mathbf{h}}^{i, t+1}=0\) then
                    \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow m_{j \mid \mathbf{h}}^{i, t+1}+1 \quad \forall j\)
                end if
                if \(m_{j \mid \mathbf{h}}^{i, t+1}=M\) then
                    \(m_{j \mid \mathbf{h}}^{i, t+1} \leftarrow\left\lfloor m_{j \mid \mathbf{h}}^{i, t+1} / 2\right\rfloor \quad \forall j\)
                end if
            end for
        end for
    end if
    return \(m_{j \mid \mathbf{h}}^{i, t+1}\)
```

with NB and TAN structures are shown in Table 1 for the datasets described above. All samples from the training set were presented to the proposed algorithm twenty times in random order. The absolute reduction in classification rate (CR) compared to the exact CR, i.e. using BNCs with the optimal doubleprecision parameters, for the considered datasets is, with few exceptions, relatively small. Thus the proposed reduced-precision computation scheme seems to be sufficiently accurate to yield good classification performance while employing only range-limited counters and a lookup table of size $M \times M$. Clearly, the performance of the proposed method can be improved by using larger and more accurate lookup tables and counters with larger bit-width.

For discriminative parameter learning, we set the hyper-parameters $\lambda \in$ $\{0,1,2,4,8,16\}$ and $\gamma \in\{0.25,0.5,1,2,4,8$.$\} using 10$-fold cross-validation. For this setup, we observed the classification performance summarized in Table 1. While the results are not as good as those of the exact MM solution, in terms of the absolute reduction in CR, we can clearly observe an improvement in classification performance using the proposed MM parameter learning method over the proposed ML parameter learning method for many datasets. The performance of BNCs using

Table 1. Classification performance. CRs using ML/MM parameters according to $(10) /(16)$ in double-precision are denoted as $M L$ exact $/ M M$ exact. CRs using reduced-precision ML/MM parameters computed according to Algorithm 1/Algorithm 3 using only reduced-precision arithmetic are denoted as $M L$ prop./MM prop.; ML abs./MM abs. denote the absolute reduction in CR for doubleprecision ML/MM parameters to reduced-precision ML/MM parameters.


the optimal double-precision parameters is in many cases not significantly better. Note that the hyper-parameters used for determining double-precision parameters are different than those used for determining reduced-precision parameters, i.e. a larger range of values is used (details are provided in [12]). The larger range of values cannot be used in case of reduced-precision parameters because of the limited parameter resolution.

# 6 Discussions 

We proposed online algorithms for learning BNCs with reduced-precision fixedpoint parameters using reduced-precision computations only. This facilitates the utilization of BNCs in computationally constrained platforms, e.g. embeddedand ambient-systems, as well as power-aware systems. The algorithms differ from naive implementations of conventional algorithms by avoiding error-prone parameter projections commonly used in gradient ascent/descent algorithms. In experiments, we demonstrated that our algorithms yield parameters that achieve classification performances close to that of optimal double-precision parameters for many of the investigated datasets.

Our algorithms have similarities with a very simple method for learning discriminative parameters of BNCs known as discriminative frequency estimates [19]. According to this method, parameters are estimated using a perceptron-like algorithm, where parameters are updated by the prediction loss, i.e. the difference of the class posterior of the correct class (which is assumed to be 1 for the data in the training set) and the class posterior according to the model using the current parameters.
